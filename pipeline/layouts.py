"""Layout parsers for interp cutting PDFs.

Layouts recognised so far (force one with: python pipeline/ingest.py FILE --layout NAME):

  di_cutting        Title, "By Author", optional teaser text, an "INTRODUCTION"
                    heading (Arial Black) followed by the introduction set in
                    Times New Roman Italic, the rest of the cutting, then a
                    "SOURCE INFORMATION" heading (Arial Black) and optional
                    "AWARD HISTORY"/"AWARDS" back matter.  45 of the 46 files
                    in the first upload.

  publisher_script  A published script (for example SpeechGeek): cover page
                    with title and author, a copyright page, then the script.
                    No introduction, no source block.  1 of 46.

Each parser returns the same dictionary shape (see parse_pdf) in which EVERY
text line of the PDF is placed in exactly one bucket.  ingest.py verifies this
with a word-conservation test, so nothing can silently disappear or leak.
"""
import bisect
import collections
import re
import pdfplumber

FOOTER_RE = re.compile(r"^(Page\s+)?\d+\s+of\s+\d+$", re.I)
SECTION_HEADINGS = ("INTRODUCTION", "SOURCE INFORMATION", "AWARD HISTORY", "AWARDS")
LABEL_RE = re.compile(r"^([A-Z][A-Z0-9 .'’/#&-]{0,28}):(\s|$)")
BYLINE_RE = re.compile(r"^by\s+\S", re.I)
BYLINE_WRAP_RE = re.compile(r"(,|\band|&|\b(Dr|Mr|Ms|Mrs|Prof)\.)$", re.I)
IN_TEXT_HEAD_RE = re.compile(r"^(TRANSITION|CONCLUSION|CLOSING)\b", re.I)
AWARDISH_RE = re.compile(r"(?i)\b(qualifier|finalist|semifinalist|quarterfinalist|champion|winner|place|nietoc|ncfl|toc|tournament)\b")
URL_RE = re.compile(r"https?://|www\.", re.I)
WORD_RE = re.compile(r"[\w][\w'’]*", re.UNICODE)
LIGATURES = {"\ufb01": "fi", "\ufb02": "fl", "\ufb00": "ff", "\ufb03": "ffi", "\ufb04": "ffl",
             "\u00a0": " ", "\u00ad": "", "\u200b": ""}


def clean_chars(s, notes=None):
    out = s
    for k, v in LIGATURES.items():
        if k in out:
            out = out.replace(k, v)
            if notes is not None:
                msg = "Replaced character U+%04X" % ord(k)
                if msg not in notes:
                    notes.append(msg)
    return out


def words(text):
    return len(WORD_RE.findall(text))


# ------------------------------------------------------------------ lines --
class Line:
    __slots__ = ("text", "x0", "x1", "top", "bottom", "page", "col", "twocol", "font", "size", "bold_lead", "italic")

    def __repr__(self):
        return "Line(p%d %r %s)" % (self.page, self.text[:40], self.font)




class ColumnError(Exception):
    """A page looks two-column but cannot be split without losing or cutting characters."""


def _row_segments(chars):
    """Group characters into text rows; return [(top, bottom, [(x0, x1), ...] merged spans)]."""
    rows = collections.defaultdict(list)
    for c in chars:
        rows[round(c["top"] / 3)].append(c)
    out = []
    for cs in rows.values():
        spans = []
        for c in sorted(cs, key=lambda c: c["x0"]):
            if spans and c["x0"] - spans[-1][1] < 3:
                spans[-1][1] = max(spans[-1][1], c["x1"])
            else:
                spans.append([c["x0"], c["x1"]])
        out.append((min(c["top"] for c in cs), max(c["bottom"] for c in cs), spans))
    return sorted(out)


def find_gutter(page, min_share=0.2, near=None):
    """Return the x position of a column gutter, or None for a one-column page.  A gutter is an x position in
    the middle 30% of the page that almost no text row comes within 3 points of (at most 2 rows or 5%, such as
    a full-width title or footer), with at least 20% of the page's characters on each side.  The two columns'
    lines need not line up.  Of the widest such band, the middle is returned."""
    # near: the gutter of the page before.  A page that follows a two-column page may carry only a short right
    # column (often the source block), so near that position a smaller share of text on the right is enough.
    chars = [c for c in page.chars if c["text"].strip()]
    rows = _row_segments(chars)
    if len(chars) < (150 if near is None else 40) or len(rows) < (8 if near is None else 4):
        return None
    left, _, right, _ = page.bbox
    w = float(right - left)
    allowed = max(2, 0.05 * len(rows))
    xs0 = sorted(c["x0"] for c in chars)
    xs1 = sorted(c["x1"] for c in chars)
    ok = []
    lo_x = int(left + w * 0.35) if near is None else int(near) - 15
    hi_x = int(left + w * 0.65) if near is None else int(near) + 15
    for x in range(lo_x, hi_x + 1):
        cross = sum(1 for _, _, spans in rows if any(a - 3 < x < b + 3 for a, b in spans))
        n_left = bisect.bisect_right(xs1, x)
        n_right = len(xs0) - bisect.bisect_left(xs0, x)
        ok.append(cross <= allowed and min(n_left, n_right) >= min_share * len(chars))
    best, run, start = (0, None), 0, None
    for i, good in enumerate(ok + [False]):
        if good:
            start = i if run == 0 else start
            run += 1
        else:
            if run > best[0]:
                best = (run, start + run // 2)
            run = 0
    return lo_x + best[1] if best[1] is not None and best[0] >= 6 else None


def _crops(page, gx):
    """Split a page into regions in reading order: runs of two-column rows become (left, right) crops and
    rows that cross the gutter (titles, footers) become full-width crops.  Every character must land in
    exactly one crop, or ColumnError is raised."""
    chars = [c for c in page.chars if c["text"].strip()]
    rows = _row_segments(chars)
    kinds = ["full" if any(a - 3 < gx < b + 3 for a, b in spans) else "cols" for _, _, spans in rows]
    runs = []
    for (top, bottom, _), k in zip(rows, kinds):
        if runs and runs[-1][0] == k:
            runs[-1][2] = max(runs[-1][2], bottom)
        else:
            runs.append([k, top, bottom])
    inf = float("inf")

    def region(x0, y0, x1, y1):
        # every character goes to the one region that holds its centre, so none is lost at a boundary
        return page.filter(lambda o: o.get("object_type") == "char"
                           and x0 <= (o["x0"] + o["x1"]) / 2 < x1 and y0 <= (o["top"] + o["bottom"]) / 2 < y1)
    regions = []
    for i, (k, top, bottom) in enumerate(runs):
        y0 = -inf if i == 0 else (runs[i - 1][2] + top) / 2
        y1 = inf if i == len(runs) - 1 else (bottom + runs[i + 1][1]) / 2
        if k == "full":
            regions.append((0, region(-inf, y0, inf, y1), False))
        else:
            regions.append((0, region(-inf, y0, gx, y1), True))
            regions.append((1, region(gx, y0, inf, y1), True))
    got = sum(1 for _, r, _ in regions for c in r.chars if c["text"].strip())
    if got != len(chars):
        raise ColumnError("page %s: %d characters on the page but %d in the column regions" % (page.page_number, len(chars), got))
    return regions


def _make_lines(region, pn, col, twocol=False, y_tol=3):
    out = []
    for raw in region.extract_text_lines(layout=False, strip=True, return_chars=True, y_tolerance=y_tol):
        text = raw["text"].strip()
        if not text:
            continue
        chars = [c for c in raw["chars"] if c["text"].strip()]
        if not chars:
            continue
        fonts = collections.Counter((c["fontname"].split("+")[-1], round(c["size"])) for c in chars)
        (fname, fsize), _ = fonts.most_common(1)[0]
        ln = Line()
        ln.text, ln.page, ln.col, ln.twocol = text, pn, col, twocol
        ln.x0, ln.x1, ln.top, ln.bottom = raw["x0"], raw["x1"], raw["top"], raw["bottom"]
        ln.font, ln.size = fname, fsize
        lead = ""
        for c in sorted(chars, key=lambda c: c["x0"]):
            if "Bold" in c["fontname"] or "Black" in c["fontname"]:
                lead += c["text"]
            else:
                break
        ln.bold_lead = lead
        ln.italic = sum(1 for c in chars if "Italic" in c["fontname"]) / len(chars) > 0.6
        out.append(ln)
    return out


def source_award_row(page):
    """If a row on this page reads 'SOURCE INFORMATION ... AWARD HISTORY' (two side-by-side blocks), return
    (top of that row, x where the award block starts); else None."""
    words = page.extract_words(use_text_flow=False, keep_blank_chars=False)
    for i, w in enumerate(words[:-1]):
        if w["text"].upper() == "SOURCE" and words[i + 1]["text"].upper().startswith("INFORMATION"):
            info = words[i + 1]
            for a in words:
                if a["text"].upper() in ("AWARD", "AWARDS") and abs(a["top"] - w["top"]) < 3 and a["x0"] > info["x1"] + 20:
                    return min(w["top"], a["top"]) - 1, a["x0"] - 4
    return None


def read_lines(pdf_path, stats=None, split_source_row=False, y_tol=3):
    """Return (lines, n_pages) for every non-empty text line in the PDF, in reading order.
    Two-column pages are read left column then right column (see find_gutter); right-column lines are
    shifted left so indentation reads the same in both columns, and carry col = 1.
    If a dict is given as stats, stats["two_column_pages"] lists the page numbers read as two columns."""
    lines, two, split = [], [], []
    with pdfplumber.open(pdf_path) as pdf:
        n = len(pdf.pages)
        prev_gx = None
        for pn, page in enumerate(pdf.pages, 1):
            gx = find_gutter(page)
            if gx is None and prev_gx is not None:
                gx = find_gutter(page, min_share=0.03, near=prev_gx)
            prev_gx = gx
            if gx is None:
                sa = source_award_row(page) if split_source_row else None
                if sa is None:
                    lines += _make_lines(page, pn, 0, y_tol=y_tol)
                    continue
                # one column above; the side-by-side source and award blocks below are read as two columns
                top, ax = sa
                px0, py0, px1, py1 = page.bbox
                above, below = page.within_bbox((px0, py0, px1, top)), page.within_bbox((px0, top, px1, py1))
                n_chars = sum(1 for c in page.chars if c["text"].strip())
                got = sum(1 for c in above.chars if c["text"].strip()) + sum(1 for c in below.chars if c["text"].strip())
                if got != n_chars:
                    raise ColumnError("page %d: source block split lost characters (%d of %d)" % (pn, got, n_chars))
                lines += _make_lines(above, pn, 0, y_tol=y_tol)
                for col, region, _ in _crops(below, ax):
                    lines += _make_lines(region, pn, col, y_tol=y_tol)
                split.append(pn)
                continue
            two.append(pn)
            page_lines = []
            for col, region, in_cols in _crops(page, gx):
                page_lines += _make_lines(region, pn, col, in_cols, y_tol=y_tol)
            left = [l.x0 for l in page_lines if l.col == 0]
            right = [l.x0 for l in page_lines if l.col == 1]
            if left and right:
                shift = min(right) - min(left)
                for l in page_lines:
                    if l.col == 1:
                        l.x0, l.x1 = l.x0 - shift, l.x1 - shift
            lines += page_lines
    if stats is not None:
        stats["two_column_pages"] = two
        stats["source_split_pages"] = split
    return lines, n


def reading_order_agreement(pdf_path, text, n=5):
    """Share of the n-word runs in text that also occur in pdftotext's own reading of the file, an independent
    extractor.  pdftotext's normal mode and its -raw mode (content order) are both tried and the better score is
    kept, because the two pdftotext programs in use (poppler and xpdf) order some pages differently.  Scrambled
    column text matches neither.  Returns None if pdftotext is missing or the text is too short."""
    import subprocess
    # words written in capitals (speaker names, shouted words) are dropped from both sides: some files set
    # speaker names in a margin column that pdftotext reads as a separate block
    caps = {w.lower() for w in re.findall(r"\b[A-Z][A-Z'’]+\b", text)}
    norm = lambda s: [w for w in re.findall(r"[a-z0-9]+", s.lower().replace("’", "'")) if w not in caps]     # noqa: E731
    grams = lambda w: {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}   # noqa: E731
    ga = grams(norm(text))
    if len(ga) < 20:
        return None
    best = None
    for mode in ([], ["-raw"]):
        try:
            ref = subprocess.run(["pdftotext"] + mode + [str(pdf_path), "-"], capture_output=True, text=True, timeout=60).stdout
        except (OSError, subprocess.TimeoutExpired):
            continue
        score = round(len(ga & grams(norm(ref))) / len(ga), 3)
        best = score if best is None else max(best, score)
    return best


def is_heading(ln, name=None):
    """A section heading: one of SECTION_HEADINGS alone on its line, in Arial Black (the house style) or, in some
    files, in a bold face, written in capitals."""
    raw = ln.text.strip()
    if "Black" not in ln.font and not ("Bold" in ln.font and raw == raw.upper()):
        return False
    t = raw.upper()
    return (t == name) if name else (t in SECTION_HEADINGS)


def is_label_line(ln):
    if LABEL_RE.match(ln.text):
        return True
    lead = ln.bold_lead.strip()
    return bool(lead.endswith(":") and 2 <= len(lead) <= 32 and lead[0].isalpha())


def label_of(text):
    m = LABEL_RE.match(text)
    return m.group(1).strip() if m else None


# -------------------------------------------------------- text assembly --
def lines_to_text(lines, notes=None):
    """Turn lines into paragraphs.  Verse (short lines) keeps its line breaks;
    prose has wrapped lines joined.  The raw lines are kept separately by the caller."""
    if not lines:
        return ""
    has_labels = sum(1 for l in lines if is_label_line(l)) >= 3
    x0s = collections.Counter(round(l.x0) for l in lines)
    base = min(x0s) if x0s else 72
    base = max(base, 0)
    width = max(l.x1 for l in lines) - base or 1
    hanging = sum(1 for l in lines if l.x0 > base + 8) / len(lines) > 0.5
    gaps = [b.top - a.bottom for a, b in zip(lines, lines[1:]) if (a.page, a.col) == (b.page, b.col) and b.top > a.bottom - 1]
    typical = sorted(gaps)[len(gaps) // 2] if gaps else 2.0
    paras, cur = [], [lines[0]]
    for prev, ln in zip(lines, lines[1:]):
        if (ln.page, ln.col) == (prev.page, prev.col):
            gap = ln.top - prev.bottom
        else:                                   # page or column break: new paragraph only if the sentence ended
            gap = 99 if prev.text.rstrip().endswith(('.', '!', '?', '"', '”', ')', ']', '…')) else 0
        start = False
        if has_labels:
            start = is_label_line(ln)
        elif hanging:                           # first line flush left, continuation lines indented
            if ln.x0 > base + 8:
                start = False
            else:                               # flush left: new paragraph after an indented run or a finished sentence
                start = prev.x0 > base + 8 or prev.text.rstrip().endswith((".", "!", "?", '"', "”", ")", "]", "…", ":"))
        else:                                   # first line indented
            start = ln.x0 > base + 8
        if gap > typical + 4.0:
            start = True
        # a fully italic parenthetical direction on its own line starts a block
        if ln.text.startswith("(") and ln.italic and not prev.text.endswith(","):
            start = True
        if start:
            paras.append(cur)
            cur = [ln]
        else:
            cur.append(ln)
    # on two-column pages a line is "short" against the width of its own column, not of the whole text
    col_width = collections.defaultdict(float)
    for l in lines:
        if l.twocol:
            col_width[(l.page, l.col)] = max(col_width[(l.page, l.col)], l.x1 - base)
    paras.append(cur)

    out = []
    for p in paras:
        tw = [col_width[(l.page, l.col)] for l in p if l.twocol]
        pw = max(tw) if tw else width
        short = [l for l in p[:-1] if (l.x1 - base) < 0.85 * pw]
        verse = len(p) >= 4 and len(short) / max(1, len(p) - 1) > 0.6
        texts = [clean_chars(l.text, notes) for l in p]
        if verse:
            out.append("\n".join(texts))
        else:
            joined = texts[0]
            for t in texts[1:]:
                joined = (joined + t) if joined.endswith("-") and joined[-2:-1].isalpha() and t[:1].islower() else (joined + " " + t)
            out.append(joined)
    return "\n\n".join(out)


def raw_text(lines):
    return "\n".join(clean_chars(l.text) for l in lines)


# ---------------------------------------------------------- source block --
SRC_KEY_RE = re.compile(r"^(Author|Authors|Book|Magazine|Journal|Publisher|ISBN|ISSN|Date[^:]{0,20}|Weblink|Website|URL|Web Link|Title|Source)\s*:\s*(.*)$", re.I)
AWARD_TAIL_RE = re.compile(r"\s+(19|20)\d\d\s+(National|State|District|Regional|NIETOC|NCFL|TOC)\b.*$", re.I)
AWARD_LINE_RE = re.compile(r"^(19|20)\d\d\s+(National|State|District|Regional|NIETOC|NCFL|TOC)\b", re.I)


def parse_source_block(lines):
    """Return (fields, award_lines, note_lines).  Award text that shares a line with a field
    (a second column in the PDF) is trimmed from the value and kept in award_lines."""
    fields, awards, notes, last = {}, [], [], None
    for ln in lines:
        t = ln.text.strip()
        m = SRC_KEY_RE.match(t)
        if m:
            key, val = m.group(1).strip(), m.group(2).strip()
            tail = AWARD_TAIL_RE.search(val)
            if tail:
                awards.append(tail.group(0).strip())
                val = val[:tail.start()].strip()
            if key.lower().startswith("date"):
                key = "Date"
            fields[key] = val
            last = key
        elif AWARD_LINE_RE.match(t):
            awards.append(t)
        elif t.upper().startswith("NOTE"):
            notes.append(t)
            last = "NOTE"
        elif t.lower().startswith("http"):
            if last == "NOTE":
                notes.append(t)
            else:
                fields["Weblink"] = (fields.get("Weblink", "") + " " + t).strip()
                last = "Weblink"
        elif last in ("Weblink", "Publisher", "Book", "Magazine"):
            fields[last] = (fields[last] + " " + t).strip()
        else:
            notes.append(t)
    return fields, awards, notes


CUTTER_RE = re.compile(r"Cutting\s+compliments\s+of\s+(.+?)(?:\s*\*|$)", re.I | re.S)


def parse_back_matter(lines):
    text = " ".join(l.text for l in lines)
    cutter = None
    m = CUTTER_RE.search(text)
    if m:
        cutter = re.sub(r"\s+", " ", m.group(1)).strip()
    return {"cutter_credit": cutter}


# ------------------------------------------------------------------ parse --
def _absorb_byline_tail(lines, k):
    """Bold lowercase lines straight after the byline ('with contributions from ...') belong to the byline block."""
    while k < len(lines) and lines[k].page == 1 and lines[k].text[:1].islower() and "Bold" in lines[k].font:
        k += 1
    return k


def split_header(lines, notes):
    """Return (title, byline_author, index of first line after the byline).  A byline that wraps (it ends with a
    comma, 'and', '&' or a title such as 'Dr.', or the next line starts with 'and') continues on the next line."""
    t, a, k = _split_header(lines, notes)
    def name_tail(t):                   # the rest of a name that wrapped: a few capitalised words, no sentence ending
        w = t.split()
        return 0 < len(w) <= 3 and all(x[:1].isupper() for x in w) and not t.rstrip().endswith((".", "!", "?", ":"))
    while a and 0 < k < len(lines) and lines[k].page == 1 and lines[k].font == lines[k - 1].font and not is_heading(lines[k]) \
            and (BYLINE_WRAP_RE.search(a.strip()) or re.match(r"(and|&)\s", lines[k].text.strip())
                 or (re.search(r"\b(and|&)\s+\S+(\s+\S+)?$", a.strip()) and name_tail(lines[k].text.strip()))):
        a = a.strip() + " " + lines[k].text.strip()
        k += 1
    return t, a, _absorb_byline_tail(lines, k)


def _split_header(lines, notes):
    limit = min(len(lines), 8)
    for i in range(limit):
        if lines[i].page == 1 and lines[i].text.strip().lower() == "by" and i + 1 < len(lines):
            title = " ".join(l.text for l in lines[:i]).strip()
            return title, lines[i + 1].text.strip(), i + 2      # "By" and the name on separate lines
        if BYLINE_RE.match(lines[i].text) and lines[i].page == 1:
            title = " ".join(l.text for l in lines[:i]).strip()
            author = re.sub(r"^by\s+", "", lines[i].text, flags=re.I).strip()
            return title, author, i + 1
    notes.append("No 'By Author' line found near the top of page 1.")
    return (lines[0].text if lines else ""), "", (1 if lines else 0)


def detect_di_cutting(lines):
    return sum(1 for l in lines if is_heading(l, "INTRODUCTION")) == 1 and \
        sum(1 for l in lines if is_heading(l, "SOURCE INFORMATION")) == 1


def detect_publisher_script(lines):
    if any(is_heading(l, "INTRODUCTION") for l in lines):
        return False
    page2 = " ".join(l.text for l in lines if l.page == 2)
    return bool(re.search(r"(?i)copyright", page2))


def _intro_run(rest, j, i_end, author, notes):
    """The introduction is the italic run starting at rest[j] and ending before rest[i_end].  If the run
    contains a 'Title by Author' line near its end, italic lines after it are performance text.
    Returns (end index of the run, method)."""
    if j < i_end and rest[j].italic:
        run_end = j

        def in_run(k):
            if k >= i_end:
                return False
            ln = rest[k]
            if is_heading(ln):
                return False
            if ln.italic and ln.font == rest[j].font:
                return True
            # a lone bullet glyph in a symbol font inside an italic run
            return ln.text.strip() in ("•", "·", "") and k + 1 < i_end and rest[k + 1].italic and rest[k + 1].font == rest[j].font
        while run_end < i_end and in_run(run_end):
            run_end += 1
    else:
        run_end = j
        notes.append("Introduction text after the heading is not in the usual italic font.")
    cut = None
    if author:
        name = re.sub(r",.*$", "", author).strip()                 # drop ', Editor'
        pat = re.compile(r"\bby\s+" + r"\s+".join(re.escape(w) for w in name.split()), re.I)
        pos, joined = [], ""
        for k in range(j, run_end):
            joined += rest[k].text + " "
            pos.append(len(joined))
        hits = list(pat.finditer(joined))
        if hits:
            end = hits[-1].end()
            cut = next(k for k, e in zip(range(j, run_end), pos) if e >= end)
    if cut is not None and run_end - (cut + 1) in (1, 2, 3):
        return cut + 1, "font+byline (trailing italic lines treated as performance text)"
    if cut is not None:
        return run_end, "font+byline (agree)"
    return run_end, "font only (no 'Title by Author' end marker)"


def parse_di_cutting(lines, n_pages):
    notes = []
    footers = [l for l in lines if FOOTER_RE.match(l.text)]
    body = [l for l in lines if not FOOTER_RE.match(l.text)]
    title, author, start = split_header(body, notes)
    header_lines = body[:start]
    rest = body[start:]

    i_intro = next(i for i, l in enumerate(rest) if is_heading(l, "INTRODUCTION"))
    i_src = next(i for i, l in enumerate(rest) if is_heading(l, "SOURCE INFORMATION"))
    if i_src < i_intro:
        notes.append("SOURCE INFORMATION appears before INTRODUCTION; layout needs a hand check.")
    # back matter starts at the first section heading after the introduction (in a two-column
    # source block AWARD HISTORY can sit just above SOURCE INFORMATION)
    i_end = next(i for i, l in enumerate(rest) if i > i_intro and is_heading(l) and not is_heading(l, "INTRODUCTION"))
    teaser = rest[:i_intro]

    # introduction = the italic run straight after the heading
    j = i_intro + 1
    run_end, method = _intro_run(rest, j, i_end, author, notes)
    intro = rest[j:run_end]
    main = rest[run_end:i_end]

    pre = rest[i_end:i_src]                       # headings/lines that sit above SOURCE INFORMATION
    back = rest[i_src + 1:]
    # source block ends at the next section heading, the rest is back matter
    k = next((x for x, l in enumerate(back) if is_heading(l)), len(back))
    source_lines, back_lines = back[:k], pre + back[k:]
    source, src_awards, src_notes = parse_source_block(source_lines)
    if "Author" in source and author:
        a, b = source["Author"].lower(), author.lower()
        if b.split() and re.sub(r",.*", "", b).split()[-1] not in a:
            notes.append("Byline author '%s' differs from source-block author '%s'." % (author, source["Author"]))
    perf = teaser + main
    return {
        "layout": "di_cutting", "pages": n_pages, "title": title, "byline_author": author,
        "header_lines": header_lines, "teaser_lines": teaser, "intro_lines": intro, "body_lines": main,
        "performance_lines": perf, "source_lines": source_lines, "source_fields": source,
        "back_lines": back_lines, "back": parse_back_matter(back_lines), "source_awards": src_awards, "source_notes": src_notes,
        "headings": [l for l in rest if is_heading(l)], "footers": footers,
        "intro_method": method, "notes": notes, "copyright": "",
    }


def parse_publisher_script(lines, n_pages):
    notes = []
    footers = [l for l in lines if FOOTER_RE.match(l.text)]
    body = [l for l in lines if not FOOTER_RE.match(l.text)]
    title, author, start = split_header(body, notes)
    header_lines = body[:start]
    rest = body[start:]
    cover_rest = [l for l in rest if l.page == 1]
    copy_lines = [l for l in rest if l.page == 2]
    script = [l for l in rest if l.page >= 3]
    text2 = " ".join(l.text for l in copy_lines)
    src = {}
    m = re.search(r"ISBN:\s*([\d-]+)", text2)
    if m:
        src["ISBN"] = m.group(1)
    m = re.search(r"Copyright\s+(\d{4})\s+by\s+([^.]+)\.", text2)
    if m:
        src["Date"] = m.group(1)
        src["Publisher"] = m.group(2).strip()
    if author:
        src["Author"] = author
    # copyright notice exactly as given: from 'Copyright' through the sentence ending 'reserved.'
    cn = re.search(r"Copyright.*?reserved\.", text2)
    copyright_notice = re.sub(r"\s+", " ", cn.group(0)) if cn else ""
    if not cn:
        notes.append("No 'All other rights reserved.' sentence found on the copyright page.")
    return {
        "layout": "publisher_script", "pages": n_pages, "title": title, "byline_author": author,
        "header_lines": header_lines + cover_rest, "teaser_lines": [], "intro_lines": [], "body_lines": script,
        "performance_lines": script, "source_lines": copy_lines, "source_fields": src,
        "back_lines": [], "back": {"cutter_credit": None}, "source_awards": [], "source_notes": [], "headings": [], "footers": footers,
        "intro_method": "none (no introduction in this layout)", "notes": notes, "copyright": copyright_notice,
    }


def is_source_heading(ln):
    return "Black" in ln.font and ln.text.strip().upper().startswith("SOURCE INFORMATION")


def is_award_heading(ln):
    return is_heading(ln, "AWARD HISTORY") or is_heading(ln, "AWARDS")


def detect_program(lines):
    """A program: several selections, each followed by its own SOURCE INFORMATION block."""
    return sum(1 for l in lines if is_source_heading(l)) >= 2 and any(is_heading(l, "INTRODUCTION") for l in lines)


def parse_program(lines, n_pages):
    """Program layout (POI and poetry or prose collections).  Title, 'By' line, optional teaser, INTRODUCTION
    with the italic introduction, then selections.  Each selection is its text followed by a SOURCE INFORMATION
    block (source fields in the source font) and sometimes its own AWARD HISTORY lines.  Transitions and poem
    titles are part of the text that follows them.  Text after the last source block becomes a final selection
    with no source, and a note says so."""
    notes = []
    footers = [l for l in lines if FOOTER_RE.match(l.text)]
    body = [l for l in lines if not FOOTER_RE.match(l.text)]
    title, author, start = split_header(body, notes)
    header_lines = body[:start]
    rest = body[start:]
    i_intro = next(i for i, l in enumerate(rest) if is_heading(l, "INTRODUCTION"))
    if sum(1 for l in rest if is_heading(l, "INTRODUCTION")) > 1:
        notes.append("More than one INTRODUCTION heading; the first is used. Needs a hand check.")
    plain = [l for l in rest if not is_heading(l) and not is_source_heading(l) and not l.italic]
    perf_font = collections.Counter(l.font for l in plain).most_common(1)[0][0] if plain else None

    def heading_like(ln):
        return is_heading(ln) or is_source_heading(ln)

    stop = next((i for i, l in enumerate(rest) if i > i_intro and heading_like(l)), len(rest))
    run_end, method = _intro_run(rest, i_intro + 1, stop, author, notes)
    role = {i_intro: "heading"}
    for k in range(i_intro + 1, run_end):
        role[k] = "intro"
    for s, l in enumerate(rest):
        if s in role:
            continue
        if is_source_heading(l) or is_award_heading(l):
            kind = "src" if is_source_heading(l) else "award"
            role[s] = kind + "head"
            k = s + 1
            block_font = rest[k].font if k < len(rest) else None
            in_url = False
            while k < len(rest) and k not in role and not heading_like(rest[k]):
                t = rest[k].text.strip()
                if IN_TEXT_HEAD_RE.match(t):
                    break                                   # a transition starts the next selection's text
                if kind == "award":
                    # award lines only; the next selection's text (or a note) ends the block
                    if not AWARDISH_RE.search(t) or len(t) > 90:
                        break
                else:
                    # a link can wrap over several lines: follow it while the lines look like pieces of a link
                    url_tail = in_url and (" " not in t or "/" in t.split()[0])
                    # the block runs on while lines look like source details: field lines, links and their wrapped
                    # tails, or lines in the block's own font when that differs from the performance font
                    if not (SRC_KEY_RE.match(t) or URL_RE.match(t) or url_tail or
                            (rest[k].font == block_font and block_font != perf_font)):
                        break
                role[k] = kind
                if kind == "src":
                    in_url = bool(URL_RE.search(t)) or url_tail
                k += 1
    selections, cur, teaser, main, headings, src_all, award_all = [], [], [], [], [], [], []
    i, last_was_source = 0, False
    while i < len(rest):
        r = role.get(i, "text")
        l = rest[i]
        if r == "text":
            last_was_source = False
            cur.append(l)
            (teaser if i < i_intro else main).append(l)
        elif r in ("heading", "srchead", "awardhead"):
            headings.append(l)
            if r == "srchead":
                block = []
                i += 1
                while i < len(rest) and role.get(i) == "src":
                    block.append(rest[i])
                    i += 1
                src_all += block
                if not cur and selections and last_was_source:
                    # a second source block straight after the first: both belong to the same selection
                    selections[-1]["source_lines"] += block
                    selections[-1]["extra_source_headings"] = selections[-1].get("extra_source_headings", 0) + 1
                else:
                    selections.append({"text_lines": cur, "source_lines": block, "award_lines": [], "before_intro": i <= i_intro})
                cur = []
                last_was_source = True
                continue
            if r == "awardhead":
                aw = []
                i += 1
                while i < len(rest) and role.get(i) == "award":
                    aw.append(rest[i])
                    i += 1
                award_all += aw
                if selections:
                    selections[-1]["award_lines"] += aw
                continue
        i += 1
    if cur:
        selections.append({"text_lines": cur, "source_lines": [], "award_lines": [], "before_intro": False})
        notes.append("Text after the last source block has no source of its own (kept as a final selection).")
    for sel in selections:
        sel["fields"], sel["src_awards"], sel["src_notes"] = parse_source_block(sel["source_lines"])
    intro = rest[i_intro + 1:run_end]
    return {
        "layout": "program", "pages": n_pages, "title": title, "byline_author": author,
        "header_lines": header_lines, "teaser_lines": teaser, "intro_lines": intro, "body_lines": main,
        "performance_lines": teaser + main, "source_lines": src_all, "source_fields": {},
        "back_lines": award_all, "back": parse_back_matter(award_all), "source_awards": [], "source_notes": [],
        "headings": headings, "footers": footers, "selections": selections,
        "intro_method": method, "notes": notes, "copyright": "",
    }


MCP_RE = re.compile(r"mushroom\s*cloud\s*press", re.I)
PAGE_NO_RE = re.compile(r"^\d{1,3}$")
GENRE_LINE_RE = re.compile(r"^an?\s+(\w+\s+)?(monologue|duo|duet|play|scene|short story)$", re.I)   # 'A Monologue' under a title
COPY_RE = re.compile(r"^(©|\(c\)|�|Copyright)\s*(\d{4})\b\s*(.*)$", re.I)


def detect_mcp(lines):
    """Mushroom Cloud Press: the publisher's name on page 1 (cover page, notice block, or story header)."""
    return not any(is_heading(l, "INTRODUCTION") for l in lines) and any(l.page == 1 and MCP_RE.search(l.text) for l in lines)


def parse_mcp(lines, n_pages):
    """Mushroom Cloud Press scripts, three variants:
      cover   (2018 on): page 1 is a cover with 'Title:', 'Author:', a (c) line, 'Publication Date:', 'Published by'
              and a permission notice; the script starts on page 2 with its title and a 'By' line.
      series  ('Intriguing Interp Series', 2001-2005): title, a (c) line with the authors, a notice ending in
              '... TO VERIFY.', then the script on the same page.
      classic (Classic Prose Collection): 'Mushroom Cloud Press | Classic Prose Collection', title, 'By' line, story.
    Bare page numbers are footers.  No introduction.  The notice is kept exactly as given."""
    notes, src = [], {"Publisher": "Mushroom Cloud Press"}
    footers = [l for l in lines if PAGE_NO_RE.match(l.text.strip()) or FOOTER_RE.match(l.text)]
    body = [l for l in lines if l not in footers]
    p1 = [l for l in body if l.page == 1]
    texts = [l.text.strip() for l in p1]
    title, author, copyright_notice = "", "", ""
    if any(t.lower().startswith("title:") for t in texts) and any(t.lower().startswith("author:") for t in texts):
        variant = "cover"

        def after(label):
            i = next(i for i, t in enumerate(texts) if t.lower().startswith(label))
            rest_ = texts[i][len(label):].strip()
            return rest_ or (texts[i + 1] if i + 1 < len(texts) else "")
        title, author = after("title:"), after("author:")
        m = next((re.search(r"Publication Date:\s*(.+)", t) for t in texts if "Publication Date" in t), None)
        if m:
            src["Date"] = m.group(1).strip()
        i_c = next((i for i, t in enumerate(texts) if COPY_RE.match(t)), None)
        copyright_notice = " ".join(texts[i_c:]) if i_c is not None else ""
        header = p1
        script = [l for l in body if l.page >= 2]
        # the script's own title and 'By' line at the top of page 2
        k = 0
        same = lambda s: re.sub(r"[’‘]", "'", s).strip().lower()                    # noqa: E731
        while k < min(3, len(script)) and ((title and same(script[k].text).startswith(same(title))) or BYLINE_RE.match(script[k].text.strip())):
            k += 1
        header, script = header + script[:k], script[k:]
    elif texts and texts[0].lower().startswith("mushroom cloud press |"):
        variant = "classic"
        src["Book"] = texts[0].split("|", 1)[1].strip()
        title = texts[1] if len(texts) > 1 else ""
        k = 2
        if len(texts) > 2 and BYLINE_RE.match(texts[2]):
            author = re.sub(r"^by\s+", "", texts[2], flags=re.I).strip()
            k = 3
        header, script = body[:k], body[k:]
        notes.append("Classic Prose Collection story; the collection's ISBN and permission notice are in a separate file.")
    else:
        variant = "series"
        i_c = next((i for i, t in enumerate(texts) if COPY_RE.match(t)), None)
        if i_c is None:                       # no (c) line: the notice starts at 'Free performance ...'
            i_c = next((i for i, t in enumerate(texts) if t.lower().startswith("free performance")), None)
        i_v = next((i for i, t in enumerate(texts) if re.search(r"TO VERIFY\.?$", t)), None)
        if i_c is None or i_v is None or i_v < i_c:
            raise ValueError("Mushroom Cloud notice block not found")
        before = [t for t in texts[:i_c] if t not in ("( )", "()")]
        i_by = next((i for i, t in enumerate(before) if BYLINE_RE.match(t)), None)
        if i_by is not None:                  # 'Title', optional genre line, 'by Author', then the notice
            author = re.sub(r"^by\s+", "", before[i_by], flags=re.I).strip()
            before = before[:i_by]
        title = " ".join(t for t in before if not GENRE_LINE_RE.match(t))
        m = COPY_RE.match(texts[i_c])
        if m:
            author = author or re.split(r"\.\s+", m.group(3).strip())[0].rstrip(".")   # 'Name. Published by ...' -> 'Name'
            src["Date"] = m.group(2)
        copyright_notice = " ".join(texts[i_c:i_v + 1])
        header, script = p1[:i_v + 1], body[len(p1[:i_v + 1]):]
        # some files print the title and a 'By' line after the notice, at the top of the script
        k = next((x for x in range(min(3, len(script))) if BYLINE_RE.match(script[x].text.strip())), None)
        if k is not None:
            if not title:
                title = " ".join(l.text.strip() for l in script[:k])
            author = re.sub(r"^by\s+", "", script[k].text.strip(), flags=re.I)
            header, script = header + script[:k + 1], script[k + 1:]
    notes.append("Mushroom Cloud Press, %s layout." % variant)
    if author:
        src["Author"] = author
    if not copyright_notice:
        notes.append("No copyright or permission notice in this file.")
    return {
        "layout": "mcp", "variant": variant, "pages": n_pages, "title": clean_chars(title), "byline_author": clean_chars(author),
        "header_lines": header, "teaser_lines": [], "intro_lines": [], "body_lines": script, "performance_lines": script,
        "source_lines": [], "source_fields": src, "back_lines": [], "back": {"cutter_credit": None}, "source_awards": [],
        "source_notes": [], "headings": [], "footers": footers, "intro_method": "none (no introduction in this layout)",
        "notes": notes, "copyright": re.sub(r"\s+", " ", clean_chars(copyright_notice)).strip(),
    }


PARSERS = [
    ("program", detect_program, parse_program),
    ("di_cutting", detect_di_cutting, parse_di_cutting),
    ("mcp", detect_mcp, parse_mcp),
    ("publisher_script", detect_publisher_script, parse_publisher_script),
]


BUCKETS = ("header_lines", "teaser_lines", "intro_lines", "body_lines", "source_lines", "back_lines", "footers")


def conservation(result):
    """Every line of the PDF must sit in exactly one bucket.  Returns (ok, detail).
    Section headings that are not inside a bucket (INTRODUCTION, SOURCE INFORMATION) are counted as headings."""
    seen, dup = {}, 0
    for k in BUCKETS:
        for l in result[k]:
            if id(l) in seen:
                dup += 1
            seen[id(l)] = k
    total = result["all_lines"]
    lone_headings = [l for l in result["headings"] if id(l) not in seen]
    for l in lone_headings:
        seen[id(l)] = "heading"
    missing = [l for l in total if id(l) not in seen]
    # performance text must be exactly teaser + body
    perf_ok = [id(l) for l in result["performance_lines"]] == [id(l) for l in result["teaser_lines"] + result["body_lines"]]
    words_total = sum(words(l.text) for l in total)
    words_seen = sum(words(l.text) for l in total if id(l) in seen)
    ok = not dup and not missing and perf_ok and words_total == words_seen
    return ok, {"lines": len(total), "duplicates": dup, "missing": len(missing), "words": words_total,
                "performance_is_teaser_plus_body": perf_ok}


ORDER_MIN = 0.85                # least share of 5-word runs that must match pdftotext's own reading order


def parse_pdf(path, force=None):
    r = _parse_once(path, force, 3)
    if r["layout"] == "reading order disagrees with pdftotext":
        # two lines at almost the same height can be merged letter by letter; read again with tighter line
        # grouping, and keep that only if it passes the same independent check
        r2 = _parse_once(path, force, 1)
        if r2["layout"] in [name for name, _, _ in PARSERS]:
            r2["notes"].append("Re-read with tighter line grouping after the first reading failed the reading-order check.")
            return r2
    return r


def _parse_once(path, force, y_tol):
    stats = {}
    try:
        lines, n = read_lines(path, stats, y_tol=y_tol)
    except ColumnError as e:
        return {"layout": "two_column (could not split cleanly)", "pages": None, "all_lines": [], "two_column_pages": [],
                "notes": [str(e)]}
    merged = [l for l in lines if "Black" in l.font and re.match(r"SOURCE INFORMATION\s+AWARDS?\b", l.text.strip().upper())]
    if merged and not any(is_heading(l, "SOURCE INFORMATION") for l in lines):
        # the source and award blocks sit side by side and were read as one; read that block as two columns
        try:
            lines, n = read_lines(path, stats, split_source_row=True, y_tol=y_tol)
        except ColumnError as e:
            return {"layout": "source block (could not split cleanly)", "pages": n, "all_lines": [], "two_column_pages": [],
                    "notes": [str(e)]}
    two = stats["two_column_pages"]
    for name, det, par in PARSERS:
        if (force and name == force) or (not force and det(lines)):
            try:
                r = par(lines, n)
            except (StopIteration, ValueError, IndexError):
                # e.g. a program with several source blocks, or headings arranged across columns
                return {"layout": "%s: sections not in the expected order" % name, "pages": n, "all_lines": lines,
                        "two_column_pages": two, "notes": ["The section headings are not in the order this layout expects; needs a hand check."]}
            r["all_lines"], r["two_column_pages"] = lines, two
            # independent check of reading order: column mistakes keep every word (so conservation passes)
            # but put them in the wrong order
            agree = reading_order_agreement(path, " ".join(l.text for l in r["intro_lines"] + r["performance_lines"]))
            r["reading_order_agreement"] = agree
            if agree is not None and agree < ORDER_MIN:
                return {"layout": "reading order disagrees with pdftotext", "pages": n, "all_lines": lines,
                        "two_column_pages": two, "reading_order_agreement": agree,
                        "notes": ["Only %.0f%% of 5-word runs match pdftotext's reading order (%s parser)." % (100 * agree, name)]}
            return r
    return {"layout": "unrecognised", "pages": n, "all_lines": lines, "two_column_pages": two, "notes": ["No parser matched this layout."]}
