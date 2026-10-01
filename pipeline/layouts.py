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
    __slots__ = ("text", "x0", "x1", "top", "bottom", "page", "col", "font", "size", "bold_lead", "italic")

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


def find_gutter(page):
    """Return the x position of a column gutter, or None for a one-column page.  A gutter is an x position in
    the middle 30% of the page that almost no text row comes within 3 points of (at most 2 rows or 5%, such as
    a full-width title or footer), with at least 20% of the page's characters on each side.  The two columns'
    lines need not line up.  Of the widest such band, the middle is returned."""
    chars = [c for c in page.chars if c["text"].strip()]
    rows = _row_segments(chars)
    if len(chars) < 150 or len(rows) < 8:
        return None
    left, _, right, _ = page.bbox
    w = float(right - left)
    allowed = max(2, 0.05 * len(rows))
    xs0 = sorted(c["x0"] for c in chars)
    xs1 = sorted(c["x1"] for c in chars)
    ok = []
    for x in range(int(left + w * 0.35), int(left + w * 0.65) + 1):
        cross = sum(1 for _, _, spans in rows if any(a - 3 < x < b + 3 for a, b in spans))
        n_left = bisect.bisect_right(xs1, x)
        n_right = len(xs0) - bisect.bisect_left(xs0, x)
        ok.append(cross <= allowed and min(n_left, n_right) >= 0.2 * len(chars))
    best, run, start = (0, None), 0, None
    for i, good in enumerate(ok + [False]):
        if good:
            start = i if run == 0 else start
            run += 1
        else:
            if run > best[0]:
                best = (run, start + run // 2)
            run = 0
    return int(left + w * 0.35) + best[1] if best[1] is not None and best[0] >= 6 else None


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
    px0, py0, px1, py1 = page.bbox
    regions = []
    for i, (k, top, bottom) in enumerate(runs):
        y0 = py0 if i == 0 else (runs[i - 1][2] + top) / 2
        y1 = py1 if i == len(runs) - 1 else (bottom + runs[i + 1][1]) / 2
        if k == "full":
            regions.append((0, page.within_bbox((px0, y0, px1, y1))))
        else:
            regions.append((0, page.within_bbox((px0, y0, gx, y1))))
            regions.append((1, page.within_bbox((gx, y0, px1, y1))))
    got = sum(1 for _, r in regions for c in r.chars if c["text"].strip())
    if got != len(chars):
        raise ColumnError("page %s: %d characters on the page but %d in the column regions" % (page.page_number, len(chars), got))
    return regions


def _make_lines(region, pn, col):
    out = []
    for raw in region.extract_text_lines(layout=False, strip=True, return_chars=True):
        text = raw["text"].strip()
        if not text:
            continue
        chars = [c for c in raw["chars"] if c["text"].strip()]
        if not chars:
            continue
        fonts = collections.Counter((c["fontname"].split("+")[-1], round(c["size"])) for c in chars)
        (fname, fsize), _ = fonts.most_common(1)[0]
        ln = Line()
        ln.text, ln.page, ln.col = text, pn, col
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


def read_lines(pdf_path, stats=None):
    """Return (lines, n_pages) for every non-empty text line in the PDF, in reading order.
    Two-column pages are read left column then right column (see find_gutter); right-column lines are
    shifted left so indentation reads the same in both columns, and carry col = 1.
    If a dict is given as stats, stats["two_column_pages"] lists the page numbers read as two columns."""
    lines, two = [], []
    with pdfplumber.open(pdf_path) as pdf:
        n = len(pdf.pages)
        for pn, page in enumerate(pdf.pages, 1):
            gx = find_gutter(page)
            if gx is None:
                lines += _make_lines(page, pn, 0)
                continue
            two.append(pn)
            page_lines = []
            for col, region in _crops(page, gx):
                page_lines += _make_lines(region, pn, col)
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
    return lines, n


def reading_order_agreement(pdf_path, text, n=5):
    """Share of the n-word runs in text that also occur in pdftotext's own reading-order output of the file
    (an independent extractor that orders columns itself).  Scrambled column text scores low.  Returns None
    if pdftotext is not installed or the text is too short."""
    import subprocess
    try:
        ref = subprocess.run(["pdftotext", str(pdf_path), "-"], capture_output=True, text=True, timeout=60).stdout
    except (OSError, subprocess.TimeoutExpired):
        return None
    # words written in capitals (speaker names, shouted words) are dropped from both sides: some files set
    # speaker names in a margin column that pdftotext reads as a separate block
    caps = {w.lower() for w in re.findall(r"\b[A-Z][A-Z'’]+\b", text)}
    norm = lambda s: [w for w in re.findall(r"[a-z0-9]+", s.lower().replace("’", "'")) if w not in caps]     # noqa: E731
    a, b = norm(text), norm(ref)
    grams = lambda w: {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}   # noqa: E731
    ga, gb = grams(a), grams(b)
    return round(len(ga & gb) / len(ga), 3) if len(ga) >= 20 else None


def is_heading(ln, name=None):
    if "Black" not in ln.font:
        return False
    t = ln.text.strip().upper()
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
    paras.append(cur)

    out = []
    for p in paras:
        short = [l for l in p[:-1] if (l.x1 - base) < 0.85 * width]
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
    """Return (title, byline_author, index of first line after the byline)."""
    t, a, k = _split_header(lines, notes)
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
    method = "font"
    # If the run contains a 'Title by Author' line near its end, anything italic after it is performance text.
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
        run_end = cut + 1
        method = "font+byline (trailing italic lines treated as performance text)"
    elif cut is not None:
        method = "font+byline (agree)"
    else:
        method = "font only (no 'Title by Author' end marker)"
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


PARSERS = [
    ("di_cutting", detect_di_cutting, parse_di_cutting),
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
    stats = {}
    try:
        lines, n = read_lines(path, stats)
    except ColumnError as e:
        return {"layout": "two_column (could not split cleanly)", "pages": None, "all_lines": [], "two_column_pages": [],
                "notes": [str(e)]}
    two = stats["two_column_pages"]
    for name, det, par in PARSERS:
        if (force and name == force) or (not force and det(lines)):
            r = par(lines, n)
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
