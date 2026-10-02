# Dry run over incoming/

Nothing was written to the database. Parser code version 92fd7bc731f9.

## Files by folder

| Folder | Files | byte-identical copy | excluded by decision | parsed | parsed, duplicate text | refused: di_cutting: sections not in the expected order | refused: two_column (could not split cleanly) | refused: unrecognised |
|---|---|---|---|---|---|---|---|---|
| incoming/DI | 19 | 9 | 0 | 0 | 0 | 0 | 0 | 10 |
| incoming/DI/Any Gender DI | 46 | 1 | 0 | 1 | 44 | 0 | 0 | 0 |
| incoming/DI/Female DIs | 252 | 8 | 0 | 238 | 0 | 0 | 0 | 6 |
| incoming/DI/Male DIs | 179 | 1 | 0 | 162 | 0 | 0 | 0 | 16 |
| incoming/Duo-Duet/Any-Any Duos & Duets | 80 | 0 | 0 | 62 | 1 | 0 | 0 | 17 |
| incoming/Duo-Duet/F-F Duos & Duets | 169 | 17 | 5 | 109 | 7 | 0 | 0 | 31 |
| incoming/Duo-Duet/M-F Duos & Duets | 271 | 2 | 0 | 231 | 12 | 0 | 1 | 25 |
| incoming/Duo-Duet/M-M Duos & Duets | 113 | 1 | 0 | 77 | 11 | 0 | 0 | 24 |
| incoming/HI | 46 | 22 | 3 | 1 | 0 | 0 | 0 | 20 |
| incoming/HI/Any Gender HI | 141 | 0 | 0 | 123 | 15 | 0 | 0 | 3 |
| incoming/HI/Female HIs | 74 | 2 | 0 | 59 | 9 | 0 | 0 | 4 |
| incoming/HI/Male HIs | 138 | 2 | 0 | 123 | 8 | 0 | 0 | 5 |
| incoming/Needs to be classified (zip) | 195 | 13 | 8 | 23 | 0 | 0 | 17 | 134 |
| incoming/POI Program Starter | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| incoming/Poetry/Any Gender Poetry | 260 | 2 | 0 | 155 | 3 | 1 | 0 | 99 |
| incoming/Poetry/Poetry Female | 124 | 2 | 0 | 87 | 3 | 0 | 0 | 32 |
| incoming/Poetry/Poetry Male | 70 | 0 | 0 | 52 | 2 | 0 | 0 | 16 |
| incoming/Prose/Mushroom Cloud Press - Classic Prose Collection/MushroomCloudPress_ClassicProseCollection | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 17 |
| incoming/Prose/Mushroom Cloud Press - Classic Prose Collection/zip contents | 17 | 17 | 0 | 0 | 0 | 0 | 0 | 0 |
| incoming/Prose/Prose Any Gender | 218 | 1 | 0 | 152 | 47 | 0 | 0 | 18 |
| incoming/Prose/Prose- Female | 188 | 0 | 0 | 137 | 38 | 0 | 0 | 13 |
| incoming/Prose/Prose- Male | 167 | 3 | 0 | 102 | 41 | 1 | 0 | 20 |
| **Total** | 2785 | 103 | 16 | 1895 | 241 | 2 | 18 | 510 |

## Parsed files (2136)

| Measure | Count |
|---|---|
| layout: di_cutting | 2094 |
| layout: publisher_script | 42 |
| introduction boundary: High | 1781 |
| introduction boundary: Medium | 313 |
| introduction boundary: Not applicable | 42 |
| teaser: Yes | 1532 |
| teaser: No | 604 |
| text layout: prose | 1616 |
| text layout: mixed | 329 |
| text layout: verse | 191 |
| source citation: Complete | 2123 |
| source citation: Partial | 8 |
| source citation: Not stated | 5 |

## Reading order check

Share of 5-word runs in the extracted introduction and performance text that also appear in pdftotext's own
reading-order output. Files below 0.85 are refused. Column mistakes keep every word but scramble the order.

| Agreement | Parsed, one column | Parsed, some pages read as two columns | Refused |
|---|---|---|---|
| 0.00 to 0.50 | 0 | 0 | 0 |
| 0.50 to 0.70 | 0 | 0 | 0 |
| 0.70 to 0.80 | 0 | 0 | 0 |
| 0.80 to 0.85 | 0 | 0 | 0 |
| 0.85 to 0.90 | 3 | 0 | 0 |
| 0.90 to 0.95 | 0 | 1 | 0 |
| 0.95 to 0.98 | 85 | 4 | 0 |
| 0.98 to 1.00 | 1184 | 859 | 0 |
| not measured | 0 | 0 | |

## Files already in the library, parsed again

45 identical to the stored record (title, author, work, publisher, introduction, source block, raw text).

- `incoming/DI/Any Gender DI/Live to Tell - DI.pdf` (IC-0032): now byte-identical copy of incoming/DI/Any Gender DI/Live to Tell - DI (1).pdf

## QC findings in parsed files

| Kind | Findings |
|---|---|
| artifact | 605 |
| balance | 231 |
| truncated | 218 |
| length | 61 |
| mid-sentence start | 30 |
| name variant | 29 |
| font encoding | 20 |
| leak | 18 |

### First QC findings of each kind

**artifact**

- `incoming/DI/Any Gender DI/26 Pebbles - DI.pdf`: stray single letter 'l' in performance_text: ...as a hive of people l that would be there ...
- `incoming/DI/Any Gender DI/After I Was Thrown in the River - DI.pdf`: possible unjoined hyphenation: 't- fast'
- `incoming/DI/Any Gender DI/After the Death of Anna Gonzales - DI.pdf`: stray single letter 'Y' in performance_text: ...t want to live- And Y I never noticed.  TR...
- `incoming/DI/Any Gender DI/Aunt Leaf - DI.pdf`: possible unjoined hyphenation: 't- and'
- `incoming/DI/Any Gender DI/Beyond Magenta - DI.pdf`: stray single letter 'V' in performance_text: ...48-49) Send Matthew V to the principal’s o...
- `incoming/DI/Any Gender DI/Book Thief - DI.pdf`: stray single letter 'U' in introduction_text: ...U Krakovianki once sta...

**balance**

- `incoming/DI/Any Gender DI/26 Pebbles - DI.pdf`: performance_text has 29 '(' and 30 ')'
- `incoming/DI/Any Gender DI/Act of Devotion - DI.pdf`: performance_text has 4 '[' and 3 ']'
- `incoming/DI/Any Gender DI/Book Thief - DI.pdf`: performance_text has 6 '[' and 4 ']'
- `incoming/DI/Any Gender DI/Therac 25 - DI.pdf`: performance_text has 33 '(' and 32 ')'
- `incoming/DI/Any Gender DI/Widows and Children First - DI.pdf`: introduction_text has 0 '(' and 2 ')'
- `incoming/DI/Female DIs/An Push Da Wind Down - DI.pdf`: performance_text has 69 '(' and 71 ')'

**length**

- `incoming/DI/Any Gender DI/Act of Devotion - DI.pdf`: 2795 spoken words (long)
- `incoming/DI/Female DIs/Burned Alive - DI.pdf`: 2694 spoken words (long)
- `incoming/DI/Female DIs/Chain - DI.pdf`: 2659 spoken words (long)
- `incoming/DI/Female DIs/Emma Goldman - DI.pdf`: 3038 spoken words (long)
- `incoming/DI/Female DIs/Gargoyle - DI.pdf`: 2878 spoken words (long)
- `incoming/DI/Female DIs/Having our Say - DI.pdf`: 2731 spoken words (long)

**name variant**

- `incoming/DI/Any Gender DI/Life Support - DI.pdf`: byline author 'Stephanie Summerville' but introduction ends 'by Stephanie Summerfield.'
- `incoming/DI/Female DIs/Antigone - DI.pdf`: byline author 'Sophocles (Translated by R.C. Jebb)' but introduction ends 'by Sophocles.'
- `incoming/DI/Female DIs/Bald in the Land of Big Hair - DI.pdf`: byline author 'Joni Rogers' but introduction ends 'by Joni Rodgers'
- `incoming/DI/Female DIs/Cats in the Courtyard - DI.pdf`: byline author 'Patti Feuereisen (ed)' but introduction ends 'by Patti Feuereisen'
- `incoming/DI/Female DIs/Rodeo - DI.pdf`: byline author 'Jane Anderson' but introduction ends 'by Jane Martin.'
- `incoming/DI/Female DIs/Sacrifice - DI.pdf`: byline author 'Joyce Carol Oates' but introduction ends 'by Joyce Carol Oats.'

**truncated**

- `incoming/DI/Any Gender DI/My Children My Africa - DI.pdf`: performance text ends without closing punctuation: ...eacher, being the Mr. M we knew. You'll be near him up there
- `incoming/DI/Any Gender DI/Zooman and the Sign - DI.pdf`: performance text ends without closing punctuation: ...WILL BE MJSSED BY FAMJLY AND FRJENDS. HE WAS KNOWN AS ZOOMAN
- `incoming/DI/Female DIs/Aftermath - DI.pdf`: performance text ends without closing punctuation: ... I have been – we have been – inthulmat -?  SHAHID: Darkened
- `incoming/DI/Female DIs/And Then (Hanadi and Lynndie) - DI.pdf`: introduction ends without closing punctuation: ...rson account of a female suicide bomber. Meet Hanadi Jaradat
- `incoming/DI/Female DIs/Bellyfruit - DI.pdf`: introduction ends without closing punctuation: ...ia Bernhard, Susannah Blinkoff, Janet Borrus puts a face and
- `incoming/DI/Female DIs/Claire - DI.pdf`: performance text ends without closing punctuation: ... free Turning around on this music box That's wound by a key

**font encoding**

- `incoming/DI/Any Gender DI/Zooman and the Sign - DI.pdf`: capital J where I is expected, possibly a text-layer error: FAMJLY, FRJENDS, JDENTJFY, KJLLED, MJSSED
- `incoming/DI/Female DIs/Jewel - DI.pdf`: capital J where I is expected, possibly a text-layer error: MARJORIE
- `incoming/DI/Female DIs/Palace of the End - Instruments of Yearning - DI.pdf`: capital J where I is expected, possibly a text-layer error: NEHRJAS
- `incoming/DI/Female DIs/Runs Girl - DI.pdf`: capital J where I is expected, possibly a text-layer error: NJIDEKA
- `incoming/DI/Female DIs/WWJD - DI.pdf`: capital J where I is expected, possibly a text-layer error: WWJD
- `incoming/Duo-Duet/Any-Any Duos & Duets/Charlie and the Chocolate Factory - DUO.pdf`: capital J where I is expected, possibly a text-layer error: GPJOE

**mid-sentence start**

- `incoming/DI/Female DIs/Missing Natalie and Victim - DI.pdf`: performance text starts: twin sister. . Missing Natalie  Most of my friends don't kno...
- `incoming/DI/Female DIs/New York - DI.pdf`: performance text starts: introduce you to two . . . Mary and Sarah. Mary? (by way of ...
- `incoming/DI/Male DIs/Hydraphobia - DI.pdf`: performance text starts: the Hydra: A Greek root meaning a multifarious evil, or an e...
- `incoming/Duo-Duet/Any-Any Duos & Duets/Book of Awesome - DUO.pdf`: performance text starts: humanity and a big celebration of life's little moments.  AC...
- `incoming/Duo-Duet/F-F Duos & Duets/Dos Corazones (Two Hearts) - DUO.pdf`: performance text starts: sort of lake-I was way out there. And I got so tired of kick...
- `incoming/Duo-Duet/F-F Duos & Duets/Fin and Euba - DUO.pdf`: performance text starts: note to actors Fin and Euba are poor and scrappy. They say a...

**leak**

- `incoming/DI/Male DIs/Imagine--The Killing of John Lennon by Lee Brown.pdf`: introduction heading in performance_text: "ang, bang.\n\nYou're dead.\n\nINTRODUCTION\n\nMark David Chapman singl"
- `incoming/HI/Male HIs/Most Fabulous Story Ever Told - HI.pdf`: award text in performance_text: '. Merry Christmas.\n\n2004 National Qualifier'
- `incoming/Needs to be classified (zip)/Roses-In-December-by-Gregg-Moeller.pdf`: introduction heading in performance_text: 're still breathing well.\n\nINTRODUCTION\n\nANN. Ah—the successful w'
- `incoming/Needs to be classified (zip)/The Yates Transcript by Erica Mehl.pdf`: introduction heading in performance_text: 'd us all to be punished.\n\nINTRODUCTION\n\nIt is impossible for any'
- `incoming/Needs to be classified (zip)/The Yates Transcript by Erica Mehl.pdf`: ISBN line in performance_text: 'ranscript by Erica Mehl\n\nISBN: 978-1-61387-007-5\n\nCopyr'
- `incoming/Poetry/Any Gender Poetry/Last Days - PO.pdf`: award text in performance_text: 'MN State Qualifier\n\n2008 National Qualifier\nIn the last hours, she k'

## Not parsed (530)

| File | Status | Detail |
|---|---|---|
| incoming/Poetry/Any Gender Poetry/Homesick - A Plea for our Planet - PO.pdf | refused: di_cutting: sections not in the expected order | The section headings are not in the order this layout expects; needs a hand check. |
| incoming/Prose/Prose- Male/Jeffreys Moatmeal Accident - PR.pdf | refused: di_cutting: sections not in the expected order | The section headings are not in the order this layout expects; needs a hand check. |
| incoming/Duo-Duet/M-F Duos & Duets/Little Footsteps - Serious - DUO.pdf | refused: two_column (could not split cleanly) | page 10: 303 characters on the page but 230 in the column regions |
| incoming/Needs to be classified (zip)/SG_Presents_Junior_Vol_2__Dads_Coming_Home.pdf | refused: two_column (could not split cleanly) | page 2: 2586 characters on the page but 2548 in the column regions |
| incoming/Needs to be classified (zip)/SG_Presents_Junior_Vol_2__Rose_and_June.pdf | refused: two_column (could not split cleanly) | page 2: 2586 characters on the page but 2548 in the column regions |
| incoming/Needs to be classified (zip)/SG_Presents_Junior_Vol_2__The_Crayon_Map.pdf | refused: two_column (could not split cleanly) | page 2: 2586 characters on the page but 2548 in the column regions |
| incoming/Needs to be classified (zip)/SG_Presents_Junior_Vol_2__The_King_of_Nerd_Camp.pdf | refused: two_column (could not split cleanly) | page 2: 2586 characters on the page but 2548 in the column regions |
| incoming/Needs to be classified (zip)/SG_Presents_Junior_Vol_2__The_Remarkable_Adventure_of_States_the_Obvious_Girl.pdf | refused: two_column (could not split cleanly) | page 2: 2586 characters on the page but 2548 in the column regions |
| incoming/Needs to be classified (zip)/Season_Four_-_Spring_2007__Program_Builder_-_Past_the_Profundity.pdf | refused: two_column (could not split cleanly) | page 3: 2799 characters on the page but 1290 in the column regions |
| incoming/Needs to be classified (zip)/Season_One_-_Fall_2003__Being_That_Guy.pdf | refused: two_column (could not split cleanly) | page 2: 2823 characters on the page but 2780 in the column regions |
| incoming/Needs to be classified (zip)/Season_One_-_Fall_2003__Canada_Eh_-_A_Salute_to_All_Things_Canuck.pdf | refused: two_column (could not split cleanly) | page 2: 2823 characters on the page but 2780 in the column regions |
| incoming/Needs to be classified (zip)/Season_One_-_Fall_2003__Learning_to_Fall.pdf | refused: two_column (could not split cleanly) | page 2: 2823 characters on the page but 2780 in the column regions |
| incoming/Needs to be classified (zip)/Season_One_-_Fall_2003__The_Amazing_Presto.pdf | refused: two_column (could not split cleanly) | page 2: 2823 characters on the page but 2780 in the column regions |
| incoming/Needs to be classified (zip)/Season_One_-_Fall_2003__The_Apology_of_Socrates.pdf | refused: two_column (could not split cleanly) | page 2: 2823 characters on the page but 2780 in the column regions |
| incoming/Needs to be classified (zip)/Season_Ten_-_Winter_2013__Burned_Out.pdf | refused: two_column (could not split cleanly) | page 3: 779 characters on the page but 434 in the column regions |
| incoming/Needs to be classified (zip)/Season_Three_-_Fall_2005__In_A_Specimen_Box.pdf | refused: two_column (could not split cleanly) | page 2: 2855 characters on the page but 2658 in the column regions |
| incoming/Needs to be classified (zip)/Season_Three_-_Fall_2005__My_Other.pdf | refused: two_column (could not split cleanly) | page 2: 2855 characters on the page but 2658 in the column regions |
| incoming/Needs to be classified (zip)/Season_Three_-_Fall_2005__Pipe_Dreams_-_A_Mockumentary.pdf | refused: two_column (could not split cleanly) | page 2: 2855 characters on the page but 2658 in the column regions |
| incoming/Needs to be classified (zip)/Season_Three_-_Fall_2005__Take_43.pdf | refused: two_column (could not split cleanly) | page 2: 2855 characters on the page but 2658 in the column regions |
| incoming/Needs to be classified (zip)/Season_Three_-_Fall_2005__The_General_Salute.pdf | refused: two_column (could not split cleanly) | page 2: 2855 characters on the page but 2658 in the column regions |
| incoming/DI/Female DIs/Mushroom Cloud - Babe.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Female DIs/MushroomCloud_ANewWorld.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Female DIs/MushroomCloud_GodIfYoureReally.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Female DIs/MushroomCloud_HowToEatCatFood.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Female DIs/Southern Utah - Another Tragedy - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Female DIs/Zlatas Diary - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/Brief Moment in the Life of Angus Bethune - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/Dramatic Faces of Robin Williams - A Tribute - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/Elephants Graveyard - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/Looking a Lot Like Christmas - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/MushroomCloud_Brothers.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/MushroomCloud_HistoryLesson.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/MushroomCloud_HowToRideAMotorcycleBadly.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/MushroomCloud_JackTheLionheart.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/MushroomCloud_LivingInColor.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/MushroomCloud_MyPerfectFeet.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/MushroomCloud_NoLongerTheFirst.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/MushroomCloud_RedGod.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/MushroomCloud_Revolution.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/MushroomCloud_TallerToday.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/MushroomCloud_TheYearbook.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/Truth in Dreams - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Mushroom Cloud - Fighting Stance.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Mushroom Cloud - I Have Recently Returned.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Mushroom Cloud - It’s A Girl Problem.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Mushroom Cloud - My All-Time Favorites.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/MushroomCloud - An Evening With Julia Maggiano.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/MushroomCloud - H for Hercules.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/MushroomCloud - Mothers Day.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/MushroomCloud - Remember One Word.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/MushroomCloud - Sister of Mercy.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/MushroomCloud - Thomas More Doesn_t Know Me.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/Any-Any Duos & Duets/A Very Clean Place_0_Duet-Duo.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/Any-Any Duos & Duets/Burning Down the House - DUO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/Any-Any Duos & Duets/Complete Works of William Shakespeare Abridged-Revised - DUO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/Any-Any Duos & Duets/Elephants Graveyard - DUO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/Any-Any Duos & Duets/Math Curse - DUO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/Any-Any Duos & Duets/Mushroom Cloud - After You.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/Any-Any Duos & Duets/Mushroom Cloud - Anxiety Versus You.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/Any-Any Duos & Duets/Mushroom Cloud - Assignment Apple.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/Any-Any Duos & Duets/Mushroom Cloud - Beauty and the Beast - Human Resources.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/Any-Any Duos & Duets/Mushroom Cloud - Brooke Marigold, PI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/Any-Any Duos & Duets/Mushroom Cloud - C and K Save a Non-Verbal Child .pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/Any-Any Duos & Duets/Mushroom Cloud - Emily_s Post-Apocaylptic Book of Zombie Etiquette.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/Any-Any Duos & Duets/Mushroom Cloud - In A Jam.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/Any-Any Duos & Duets/Mushroom Cloud - PinocchioNoStringsAttached.pages.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/Any-Any Duos & Duets/Mushroom Cloud - The Mulligan.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/Any-Any Duos & Duets/Mushroom Cloud - The Organ Ordeal.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/Any-Any Duos & Duets/Mushroom Cloud - The Perfect Son.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/A Girl_s Guide to Science_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/Mushroom Cloud - A Dozen Red Flags(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/Mushroom Cloud - A.I. Speech Bot.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/Mushroom Cloud - D and Me(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/Mushroom Cloud - Fairytale Feud(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/Mushroom Cloud - Going Down.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/Mushroom Cloud - Hashtag(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/Mushroom Cloud - In Plain Sight(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/Mushroom Cloud - Katy and Sara(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/Mushroom Cloud - Power Struggle.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/Mushroom Cloud - Rapunzel and EllaΓÇÖs Magical Hair Salon.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/Mushroom Cloud - The Big Decision(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/Mushroom Cloud - The Main Character(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/MushroomCloud_BeautyBootCamp.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/MushroomCloud_BirthdayCandles.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/MushroomCloud_CavegirlTeachesEvolution.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/MushroomCloud_Declined.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/MushroomCloud_GirlsGuide.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/MushroomCloud_GoodMorningGlory.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/MushroomCloud_HowMuchILoveYou.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/MushroomCloud_LockedAway.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/MushroomCloud_MissErma.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/MushroomCloud_MotherDaughter.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/MushroomCloud_Rush Hour.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/MushroomCloud_TheDuffingOfEunicePowell.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/MushroomCloud_TheEmancipationOfMrTinkles.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/MushroomCloud_TheGirlInThePicture.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/MushroomCloud_ThePrincessAndTheP.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/MushroomCloud_TheUltimateDrama.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/MushroomCloud_Unfunny.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/MushroomCloud_Unplugged.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/13 Things You Don_t Know By Swans_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/4-0_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/Dining Room - DUO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/Life Cycles - DUO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/Mushroom Cloud - 20 Questions and a Motive for Murder.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/Mushroom Cloud - A Trip Through Monte Carla.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/Mushroom Cloud - Junk We Never Said Thank You For.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/Mushroom Cloud - Office Case.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/Mushroom Cloud - Play Nice.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/Mushroom Cloud_It_s An Emergency.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/Mushroom Cloud_Shakespeare in Like.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/Mushroom Cloud_The Next Table.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/Mushroom Cloud_Tutoring Session.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/MushroomCloud_40.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/MushroomCloud_BudsWithSpuds.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/MushroomCloud_ChildsPlay.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/MushroomCloud_CountdownToLove.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/MushroomCloud_ExitInterview.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/MushroomCloud_Face-Baggage.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/MushroomCloud_GR8TXTMSGWAR.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/MushroomCloud_Minnesota.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/MushroomCloud_NotForSale.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/MushroomCloud_Playdate.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/MushroomCloud_STOP.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/MushroomCloud_TheAssistant.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/Midnight Clear - DUO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/Mushroom Cloud - Dinner Dilemma.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/Mushroom Cloud - Everything Bagel.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/Mushroom Cloud - HowTybaltCapuletAlmostSavedItaly.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/Mushroom Cloud - Imaginary Friend.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/Mushroom Cloud - The Ad Lib.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/Mushroom Cloud - The Leak.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/Mushroom Cloud - Winnebago.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/MushroomCloud_DuckSurgeon.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/MushroomCloud_EveryonesGonnaDie.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/MushroomCloud_EveryonesStillDead.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/MushroomCloud_EverythingFallsOff.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/MushroomCloud_FloridaMaeTuesdaysSecond6thBirthday.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/MushroomCloud_FrontPorchChronicles.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/MushroomCloud_HamiltonSasquatch.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/MushroomCloud_LuigiAndMario.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/MushroomCloud_Overcooked.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/MushroomCloud_PostInferno.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/MushroomCloud_Shrinkage.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/MushroomCloud_TheAltos.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/MushroomCloud_TheBrightSideofDeath.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/MushroomCloud_TheCommander.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/MushroomCloud_TheLoreOfTheDRings.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/MushroomCloud_ThePrincipalsOfDrugs.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Any Gender HI/Complete Works of William Shakespeare Abridged-Revised - HI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Any Gender HI/Mushroom Cloud - Introvert_s Guide to Quarantine.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Any Gender HI/Mushroom Cloud - Nora Wants a Baby.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Female HIs/Mushroom Cloud - Dinosaurs Love Chips.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Female HIs/Mushroom Cloud - KTDs.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Female HIs/Mushroom Cloud - Talking to Teddy.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Female HIs/Mushroom Cloud - We Had Chemistry.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Male HIs/5 Lessons I Learned in my First Year of Teaching_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Male HIs/Confessions of a Burglar - HI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Male HIs/Mushroom Cloud - Dis-Orientation.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Male HIs/Naked Mole Rat Gets Dressed - HI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Male HIs/Story in Harlem Slang from Spunk - HI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_BadDetective(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_BlackFedora(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_CityMorgue(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_CouncilOfDoom(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_EverythingUnderTheSun(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_FastFoodFairytale(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_HoHoHo(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_HotDogTimeMachine(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_InvestigatorQ(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_JerryAWizardSchoolDropout(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_KidInControl(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_LittleSuzySeesGod(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_MaryChoppins(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_Moonraker(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_Penny(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_RidgevilleTalintedShow(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_SarahGlowingOrb(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_TheAnyThing(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_TheAudacityOfNope(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_WilliamShakespearesJerseyShore(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Andrew Green_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Appropriate Diet for a Pet_0_Duet-Duo.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Brothers_0_Duet-Duo.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Buds with Spuds_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Calvin Coolidge v The Dinosaurs_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Cooper_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Countdown to Love_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/DYSLEXIC DAVE_0_Duet-Duo.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Depressed White GirlThe World_s Worst DI_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Dr Wilderness_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Dude, Attorney at Law_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Everyone_s Gonna Die_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Everyone_s Still Dead_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Everything falls Off_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Evolution of Manford_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Face-Baggage_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Forensicator Forever_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Fragments of Life_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Front Porch Chronicles_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/GOODBYE MOM, I LOVE YOU_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Ghetto Blaster_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Gone Batty_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Good Morning Glory_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/HI-Larious Volume 1 _0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Heal_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/I Love All of Yous_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/I_m Mean to My Kids_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Indian Rap All-Star_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Jack in the Box_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/KABLOOEY_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Kid In Control_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Luigi _ Mario_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Minutes From the Council United For World Destruction_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Mrs. Needy_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Mushroom Cloud - Press Play.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Mushroom Cloud - Ringing.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Mushroom Cloud - Screaming Timmy Must Die.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Mushroom Cloud - Sibling Rivalry.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Mushroom Cloud - So You Want to Date a Superhero.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Mushroom Cloud - Soccer Moms (and a Dad).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Mushroom Cloud - SpaceCadets.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Mushroom Cloud - Sports Atheist.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Mushroom Cloud - Swipe Up.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Mushroom Cloud - Take Care Of It.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Mushroom Cloud - The Chess Piece Piece.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Mushroom Cloud - The Furious Fists of Julia.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Mushroom Cloud - The Ruler.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Mushroom Cloud - The Worst Day Ever.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Mushroom Cloud - Under a Curtain of Stars.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_13ThingsAboutSwans.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_BeneathThePuppetStand.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_CalvinCoolidge.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_Camp.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_DepressedWhiteGirl.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_DrWilderness.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_Finding Ryan.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_GeraldTheSpork.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_Girls.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_GreatIdeas.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_MaytheBestManWin.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_NewLeashOnLife.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_PhysicallyImpossible.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_RhymesWithOrange.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_SesameLifeOnTheStreets.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_SingleWhiteFemale.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_SnowWhite.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_TableFor2PartyOf4.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_TheBoShow.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_TheDisappointingSon.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_VirtuallyDateable.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/MushroomCloud_iWant.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/My Life in Babysittters_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/My Tiny Dancer_s Hands_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/No Longer The First_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/One_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Papa Oscar_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Penny _ The Adventures of Tickle-Me Elmo_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Play Descriptions - Mushroom Cloud Press - New Scripts 2024.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Play This at My Funeral_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Post Inferno_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Promiscuoous Ankles_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Red God_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Ridgeville Elementary School_s Extremely Talinted Show_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Scars_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Eight_-_Winter_2011__Chasing_Snowflakes.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Eight_-_Winter_2011__For_My_Baby.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Eight_-_Winter_2011__How_to_do_Nothing_Successfully.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Eight_-_Winter_2011__Hypothetically_Yours.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Eight_-_Winter_2011__Reggie_Wilson_-_Boy_Detective.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Eleven_-_Winter_2014__Cat_and_Mouse.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Eleven_-_Winter_2014__Pigskin.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Eleven_-_Winter_2014__Reflection.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Eleven_-_Winter_2014__The_Best_Worst_Date.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Eleven_-_Winter_2014__The_Dragon_Slayer_of_Eastman_Senior_High.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Four_-_Spring_2007__Saving_Face.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Four_-_Spring_2007__Schrodingers_Kiss.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Four_-_Spring_2007__Thrift.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Four_-_Spring_2007__Topaz.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Four_-_Winter_2007__Faux_Real.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Four_-_Winter_2007__The_Man_Who_Loved_Her.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Four_-_Winter_2007__The_Music_Teacher.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Four_-_Winter_2007__Totally_Sheltered.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Four_-_Winter_2007__Trash_Can_Heart.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Ten_-_Winter_2013__Bruise_Ship.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Ten_-_Winter_2013__Content.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Ten_-_Winter_2013__Dividing_by_Zero.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Ten_-_Winter_2013__Forever_As_the_Stars.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Shrinkage_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Stop!_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Superman_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Surprised We Haven_t Met Before_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/THE YEARBOOK_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Table for 2, Party of 4_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/The Assistant_0_Duet-Duo.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/The Audacity of Nope_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/The Christmas Box_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/The City Morgue_s Second AnnualTake Your Daughter to Work Day_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/The GR8 TXT MSG WAR_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/The Girl in the Picture_0_Duet-Duo.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/The Great Stravinsky_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/The Grim Reaper is a Hot Chick_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/The Hamilton Sasquatch_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/The Ride_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/The Spoon Incident_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/The Thief of Snow_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/The Toilet Paper Ration_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/The Ultimate Drama_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/The World_s Greatest Toe Show (10 MIN HI CUT).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Time of Our Lives_0_Duet-Duo.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Unfunny_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Wall Flower_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/You Can_t Take Them Home at Night_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/his sunt dracones_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/squirrel_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/130 Million Shattered Lives - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Almost - A Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/America - Its Gotta be the Cheese - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/America Reloading - A Program - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/America the Beautiful - A Program - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/American Poetry - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Behind the Staff Room Door - A Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Between the Star and the Street - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Birmingham Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Blessed are the Confused - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Borders Accents and Weapons - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Broken - A Collection in Memory of Matthew Shepard - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Burning Down the House - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Cats in the Cradle and Love You Forever - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Challenges of Education - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Chambers of a Gun if the Bullet Does Not Exist - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Collection on Cancer - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Collection on Suicide - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Commercial Break and Midnight - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Confronting  American Apathy - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Conversations about Home and Rigged Game - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Definition and A Familiar Letter - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Den of Lions (2) - PO (1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Echoes of Teachers - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Fight Evil with Poetry - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/For Black Boys - A Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Freed Between the Lines - A Program - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/From the Afterlife - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Fury of Rain Storms - A Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Gender Boxes - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Gentrification - A Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Gift and Train Platform - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Hands Still Raised - A Program - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Hir and Swing-Set - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/History of Fury and Faith - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Holy Saturday and Long Term Memory - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Hope for Humanity - COVID 19 - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Horton Hears a Who - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/How Many Degrees are We from Fahrenheit 451 - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/I Wanted to Grow Old With You - A Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/If Lady LIberty Could See Us Now - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/If You Have to Ask - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Imagine and OCD - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Impact of Teachers - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/In Remembrance - A Holocaust Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/In Response to Columbine - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/In a Shared Land - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Instructions and Locks - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Israeli-Palestinian Conflict - A Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Jubilee of People Dreaming Wildly - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Lift Off and Miracle Workers - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Loch Ness Monsters and Something Like Fire - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Medical Profession - A Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Mrs Riberio and What Teachers Make - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Multi-Cultural Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Next Life Soundtrack - A Program - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Nice Thing About Counting Stars - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/No Child Left Behind - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Nothing New Here - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Ode to Blue-Collar Workers - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Of Loss and Grieving (A Collection) - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/On Being Transgender - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/On Childhood - A Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/On the Pulse of a Brave and Startling Truth - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Outside Ourselves - A Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Palestinian Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Parents - A Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Privilege to Complain - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Proud to be Latina-Latino - A Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Pursuit of Happiness and When the Bough Breaks - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Racial Profiling Poetry Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Rain Compilation - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Red White and Bruised - A Program.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Refugee Women - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Rest in Peace - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Scratch and Dent Dreams and Angelic Insanity - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Shosholoza and Hand Me Downs - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Silence is Not an Option - A Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Speaking Truth - A Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Standardized Education - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Stereotypically Asian - A Program - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Suicide Note(s) - A Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Symbols of the Holocaust - A Poetry Compilation - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Television Poetry Program - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Ten Thousand Stories - A Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
