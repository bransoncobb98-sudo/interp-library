# Dry run over incoming/

Nothing was written to the database. Parser code version f7a9f58fe160.

## Files by folder

| Folder | Files | byte-identical copy | error | parsed | parsed, duplicate text | refused: two_column (no parser yet) | refused: unrecognised |
|---|---|---|---|---|---|---|---|
| incoming/DI | 19 | 9 | 0 | 0 | 0 | 0 | 10 |
| incoming/DI/Any Gender DI | 46 | 1 | 0 | 1 | 44 | 0 | 0 |
| incoming/DI/Female DIs | 252 | 8 | 0 | 232 | 0 | 2 | 10 |
| incoming/DI/Male DIs | 179 | 1 | 0 | 154 | 0 | 1 | 23 |
| incoming/Duo-Duet/Any-Any Duos & Duets | 80 | 0 | 0 | 59 | 1 | 1 | 19 |
| incoming/Duo-Duet/F-F Duos & Duets | 169 | 17 | 0 | 107 | 7 | 5 | 33 |
| incoming/Duo-Duet/M-F Duos & Duets | 271 | 2 | 0 | 228 | 11 | 0 | 30 |
| incoming/Duo-Duet/M-M Duos & Duets | 113 | 1 | 0 | 75 | 11 | 0 | 26 |
| incoming/HI | 46 | 22 | 0 | 1 | 0 | 4 | 19 |
| incoming/HI/Any Gender HI | 141 | 0 | 0 | 121 | 14 | 1 | 5 |
| incoming/HI/Female HIs | 74 | 2 | 0 | 58 | 8 | 0 | 6 |
| incoming/HI/Male HIs | 138 | 2 | 0 | 121 | 7 | 0 | 8 |
| incoming/Needs to be classified (zip) | 195 | 16 | 0 | 23 | 0 | 5 | 151 |
| incoming/POI Program Starter | 1 | 0 | 0 | 1 | 0 | 0 | 0 |
| incoming/Poetry/Any Gender Poetry | 260 | 2 | 5 | 30 | 0 | 146 | 77 |
| incoming/Poetry/Poetry Female | 124 | 2 | 1 | 13 | 0 | 77 | 31 |
| incoming/Poetry/Poetry Male | 70 | 0 | 0 | 8 | 0 | 49 | 13 |
| incoming/Prose/Mushroom Cloud Press - Classic Prose Collection/MushroomCloudPress_ClassicProseCollection | 17 | 0 | 0 | 0 | 0 | 0 | 17 |
| incoming/Prose/Mushroom Cloud Press - Classic Prose Collection/zip contents | 34 | 30 | 4 | 0 | 0 | 0 | 0 |
| incoming/Prose/Prose Any Gender | 218 | 1 | 0 | 26 | 0 | 171 | 20 |
| incoming/Prose/Prose- Female | 188 | 0 | 0 | 23 | 0 | 140 | 25 |
| incoming/Prose/Prose- Male | 167 | 3 | 0 | 15 | 0 | 132 | 17 |
| **Total** | 2802 | 119 | 10 | 1296 | 103 | 734 | 540 |

## Parsed files (1399)

| Measure | Count |
|---|---|
| layout: di_cutting | 1357 |
| layout: publisher_script | 42 |
| introduction boundary: High | 1078 |
| introduction boundary: Medium | 279 |
| introduction boundary: Not applicable | 42 |
| teaser: Yes | 1107 |
| teaser: No | 292 |
| text layout: prose | 1121 |
| text layout: mixed | 251 |
| text layout: verse | 27 |
| source citation: Complete | 1382 |
| source citation: Partial | 12 |
| source citation: Not stated | 5 |

## Two-column measure (share of multi-word lines with a mid-page gap)

Files above 0.25 are refused as two-column. A clean split between the groups means the threshold is safe.

| Share | Parsed | Refused as two-column |
|---|---|---|
| 0.00 to 0.05 | 1187 | 0 |
| 0.05 to 0.10 | 94 | 0 |
| 0.10 to 0.15 | 28 | 0 |
| 0.15 to 0.20 | 41 | 0 |
| 0.20 to 0.25 | 50 | 0 |
| 0.25 to 0.30 | 0 | 98 |
| 0.30 to 0.35 | 0 | 74 |
| 0.35 to 0.40 | 0 | 57 |
| 0.40 to 0.45 | 0 | 93 |
| 0.45 to 0.50 | 0 | 87 |
| 0.50 to 0.55 | 0 | 93 |
| 0.55 to 0.60 | 0 | 96 |
| 0.60 to 0.65 | 0 | 60 |
| 0.65 to 0.70 | 0 | 59 |
| 0.70 to 0.75 | 0 | 16 |
| 0.75 to 0.80 | 0 | 4 |

## QC findings in parsed files

| Kind | Findings |
|---|---|
| artifact | 428 |
| balance | 202 |
| truncated | 170 |
| length | 155 |
| mid-sentence start | 69 |
| leak | 29 |
| font encoding | 17 |
| name variant | 16 |

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
- `incoming/DI/Female DIs/Runs Girl - DI.pdf`: capital J where I is expected, possibly a text-layer error: NJIDEKA
- `incoming/DI/Female DIs/WWJD - DI.pdf`: capital J where I is expected, possibly a text-layer error: WWJD
- `incoming/Duo-Duet/Any-Any Duos & Duets/Charlie and the Chocolate Factory - DUO.pdf`: capital J where I is expected, possibly a text-layer error: GPJOE
- `incoming/Duo-Duet/Any-Any Duos & Duets/Gods Favorite - DUO.pdf`: capital J where I is expected, possibly a text-layer error: BENJAMIN

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
- `incoming/Poetry/Any Gender Poetry/130 Million Shattered Lives - PO.pdf`: ISBN line in performance_text: 'gees-and-asylum-seekers\n\nISBN: N/A Meetings held in sec'

## Not parsed (1284)

| File | Status | Detail |
|---|---|---|
| incoming/DI/Female DIs/Blue Dress - DI.pdf | refused: two_column (no parser yet) | 26% of lines have a gap across the middle of the page: two columns. |
| incoming/DI/Female DIs/French Fries - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Female DIs/Mushroom Cloud - Babe.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Female DIs/MushroomCloud_ANewWorld.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Female DIs/MushroomCloud_GodIfYoureReally.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Female DIs/MushroomCloud_HowToEatCatFood.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Female DIs/Palace of the End - Instruments of Yearning - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Female DIs/Scraps - DI.pdf | refused: two_column (no parser yet) | 41% of lines have a gap across the middle of the page: two columns. |
| incoming/DI/Female DIs/Silver Water - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Female DIs/Southern Utah - Another Tragedy - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Female DIs/Stolen Moments - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Female DIs/Zlatas Diary - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/Alien Boy - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/Blackout - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/Brief Moment in the Life of Angus Bethune - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/Coax - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/Dramatic Faces of Robin Williams - A Tribute - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/Elephants Graveyard - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/Fences - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/Guns for Geeks - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/Joey Pigza Swallowed the Key - DI.pdf | refused: unrecognised | No parser matched this layout. |
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
| incoming/DI/Male DIs/Perfect Moments - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/Truth in Dreams - DI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/DI/Male DIs/Walking on Glass - DI.pdf | refused: two_column (no parser yet) | 26% of lines have a gap across the middle of the page: two columns. |
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
| incoming/Duo-Duet/Any-Any Duos & Duets/Fantastic Mr Fox - DUO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/Any-Any Duos & Duets/How to be a Villain - DUO.pdf | refused: two_column (no parser yet) | 25% of lines have a gap across the middle of the page: two columns. |
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
| incoming/Duo-Duet/Any-Any Duos & Duets/Playwriting 101 - The Rooftop Lesson - DUO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/A Girl_s Guide to Science_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/Answsering 911 - Life in the Hot Seat - DUO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/F-F Duos & Duets/Grandpa - DUO.pdf | refused: unrecognised | No parser matched this layout. |
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
| incoming/Duo-Duet/F-F Duos & Duets/SpeechGeek Presents Female-Female Duo Vol 2.pdf | refused: two_column (no parser yet) | 70% of lines have a gap across the middle of the page: two columns. |
| incoming/Duo-Duet/F-F Duos & Duets/SpeechGeek Presents Female-Female Duo Vol 3.pdf | refused: two_column (no parser yet) | 55% of lines have a gap across the middle of the page: two columns. |
| incoming/Duo-Duet/F-F Duos & Duets/SpeechGeek Presents Female-Female Duo.pdf | refused: two_column (no parser yet) | 48% of lines have a gap across the middle of the page: two columns. |
| incoming/Duo-Duet/F-F Duos & Duets/SpeechGeek-Presents-Female-Female-Duo-Vol-4.pdf | refused: two_column (no parser yet) | 57% of lines have a gap across the middle of the page: two columns. |
| incoming/Duo-Duet/F-F Duos & Duets/SpeechGeek-Presents-Female-Female-Duo-Vol-5.pdf | refused: two_column (no parser yet) | 55% of lines have a gap across the middle of the page: two columns. |
| incoming/Duo-Duet/M-F Duos & Duets/13 Things You Don_t Know By Swans_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/4-0_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/Bar Mitzvah Boy - DUO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/Boy Gets Girl - DUO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/Dining Room - DUO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/Fat Pig - DUO.pdf | refused: unrecognised | No parser matched this layout. |
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
| incoming/Duo-Duet/M-F Duos & Duets/Time Flies - DUO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-F Duos & Duets/Two Rooms - DUO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Duo-Duet/M-M Duos & Duets/Arrangement - DUO.pdf | refused: unrecognised | No parser matched this layout. |
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
| incoming/Duo-Duet/M-M Duos & Duets/Pillowman - DUO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Any Gender HI/Complete Works of William Shakespeare Abridged-Revised - HI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Any Gender HI/How to be a Villain - HI.pdf | refused: two_column (no parser yet) | 28% of lines have a gap across the middle of the page: two columns. |
| incoming/HI/Any Gender HI/Mushroom Cloud - Introvert_s Guide to Quarantine.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Any Gender HI/Mushroom Cloud - Nora Wants a Baby.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Any Gender HI/Puberty - The Game Show - HI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Any Gender HI/Time Flies - HI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Female HIs/Amazing Bone - HI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Female HIs/French Fries - HI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Female HIs/Mushroom Cloud - Dinosaurs Love Chips.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Female HIs/Mushroom Cloud - KTDs.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Female HIs/Mushroom Cloud - Talking to Teddy.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Female HIs/Mushroom Cloud - We Had Chemistry.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Male HIs/5 Lessons I Learned in my First Year of Teaching_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Male HIs/Angelas Ashes - HI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Male HIs/Confessions of a Burglar - HI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Male HIs/Cyclops - HI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Male HIs/Mushroom Cloud - Dis-Orientation.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Male HIs/Naked Mole Rat Gets Dressed - HI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Male HIs/Story in Harlem Slang from Spunk - HI.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/Male HIs/Wanda Hickeys Night of Golden Memories - HI.pdf | refused: unrecognised | No parser matched this layout. |
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
| incoming/HI/MushroomCloud_MaryChoppins(1).pdf | refused: two_column (no parser yet) | 48% of lines have a gap across the middle of the page: two columns. |
| incoming/HI/MushroomCloud_Moonraker(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_Penny(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_RidgevilleTalintedShow(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_SarahGlowingOrb(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_TheAnyThing(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_TheAudacityOfNope(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/MushroomCloud_WilliamShakespearesJerseyShore(1).pdf | refused: unrecognised | No parser matched this layout. |
| incoming/HI/SpeechGeek-Presents-HIlarious-Vol-1.pdf | refused: two_column (no parser yet) | 60% of lines have a gap across the middle of the page: two columns. |
| incoming/HI/SpeechGeek-Presents-HIlarious-Vol-2.pdf | refused: two_column (no parser yet) | 54% of lines have a gap across the middle of the page: two columns. |
| incoming/HI/SpeechGeek-Presents-HIlarious-Vol-3.pdf | refused: two_column (no parser yet) | 58% of lines have a gap across the middle of the page: two columns. |
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
| incoming/Needs to be classified (zip)/MushroomCloud_Camp.pdf | refused: two_column (no parser yet) | 49% of lines have a gap across the middle of the page: two columns. |
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
| incoming/Needs to be classified (zip)/SG_Presents_Junior_Vol_2__Dads_Coming_Home.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/SG_Presents_Junior_Vol_2__Rose_and_June.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/SG_Presents_Junior_Vol_2__The_Crayon_Map.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/SG_Presents_Junior_Vol_2__The_King_of_Nerd_Camp.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/SG_Presents_Junior_Vol_2__The_Remarkable_Adventure_of_States_the_Obvious_Girl.pdf | refused: unrecognised | No parser matched this layout. |
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
| incoming/Needs to be classified (zip)/Season_Four_-_Spring_2007__Program_Builder_-_Past_the_Profundity.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Four_-_Spring_2007__Saving_Face.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Four_-_Spring_2007__Schrodingers_Kiss.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Four_-_Spring_2007__Thrift.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Four_-_Spring_2007__Topaz.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Four_-_Winter_2007__Faux_Real.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Four_-_Winter_2007__The_Man_Who_Loved_Her.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Four_-_Winter_2007__The_Music_Teacher.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Four_-_Winter_2007__Totally_Sheltered.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Four_-_Winter_2007__Trash_Can_Heart.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_One_-_Fall_2003__Being_That_Guy.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_One_-_Fall_2003__Canada_Eh_-_A_Salute_to_All_Things_Canuck.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_One_-_Fall_2003__Learning_to_Fall.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_One_-_Fall_2003__The_Amazing_Presto.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_One_-_Fall_2003__The_Apology_of_Socrates.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Ten_-_Winter_2013__Bruise_Ship.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Ten_-_Winter_2013__Burned_Out.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Ten_-_Winter_2013__Content.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Ten_-_Winter_2013__Dividing_by_Zero.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Ten_-_Winter_2013__Forever_As_the_Stars.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Three_-_Fall_2005__In_A_Specimen_Box.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Three_-_Fall_2005__My_Other.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Three_-_Fall_2005__Pipe_Dreams_-_A_Mockumentary.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Three_-_Fall_2005__Take_43.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Season_Three_-_Fall_2005__The_General_Salute.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/Shrinkage_0.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Needs to be classified (zip)/SpeechGeek-Season-Eight-Fall-2010.pdf | refused: two_column (no parser yet) | 44% of lines have a gap across the middle of the page: two columns. |
| incoming/Needs to be classified (zip)/SpeechGeek-Season-Eight-Winter-2011.pdf | refused: two_column (no parser yet) | 59% of lines have a gap across the middle of the page: two columns. |
| incoming/Needs to be classified (zip)/SpeechGeek-Season-Five-Nationals-2008.pdf | refused: two_column (no parser yet) | 38% of lines have a gap across the middle of the page: two columns. |
| incoming/Needs to be classified (zip)/SpeechGeek-Season-Seven-Nats-2010.pdf | refused: two_column (no parser yet) | 28% of lines have a gap across the middle of the page: two columns. |
| incoming/Needs to be classified (zip)/SpeechGeek-Season-Six-Nationals-2009.pdf | refused: unrecognised | No parser matched this layout. |
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
| incoming/Poetry/Any Gender Poetry/1990 - PO.pdf | refused: two_column (no parser yet) | 56% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/Abridged History of America - PO.pdf | refused: two_column (no parser yet) | 59% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/After the Death of Anna Gonzales - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Agrippa (A Book of the Dead) - PO.pdf | refused: two_column (no parser yet) | 62% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/America - Its Gotta be the Cheese - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/America Poem - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/America Reloading - A Program - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/America the Beautiful - A Program - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/American Poetry - PO.pdf | refused: two_column (no parser yet) | 49% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/Angel Island - Words from the Barracks - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Anthem - PO.pdf | refused: two_column (no parser yet) | 52% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/Art of Teaching - PO.pdf | refused: two_column (no parser yet) | 58% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/Away from the Sun - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Ballad of the Seven Songs - PO.pdf | refused: two_column (no parser yet) | 49% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/Behind the Staff Room Door - A Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Between the Star and the Street - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Birmingham Collection - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Blessed are the Confused - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Body of an American - PO.pdf | refused: two_column (no parser yet) | 43% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/Borders Accents and Weapons - PO.pdf | refused: two_column (no parser yet) | 31% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/Bouquets - PO.pdf | refused: two_column (no parser yet) | 26% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/Broken - A Collection in Memory of Matthew Shepard - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Buddy Wakefield Collection - PO.pdf | refused: two_column (no parser yet) | 30% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/Bully - PO.pdf | refused: two_column (no parser yet) | 58% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/Burning Down the House - PO.pdf | refused: two_column (no parser yet) | 38% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/Butcher (Poems from) - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Cats in the Cradle and Love You Forever - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Cautionary Tales for Children - PO.pdf | refused: two_column (no parser yet) | 54% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/Challenges of Education - PO.pdf | refused: two_column (no parser yet) | 52% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/Chambers of a Gun if the Bullet Does Not Exist - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Cherokee Lottery Collection - PO (1).pdf | refused: two_column (no parser yet) | 29% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/City of Slaughter - PO.pdf | refused: two_column (no parser yet) | 58% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/Cliched Meaning of Life - PO - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Code Orange and the Good News - PO.pdf | refused: two_column (no parser yet) | 30% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/Collection from Chasing Utopia - PO.pdf | refused: two_column (no parser yet) | 27% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/Collection of Childhood Memories - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Collection on Cancer - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Collection on Suicide - PO.pdf | refused: two_column (no parser yet) | 46% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/Coming of Archy and Mehitabel and her Kittens - PO.pdf | refused: two_column (no parser yet) | 39% of lines have a gap across the middle of the page: two columns. |
| incoming/Poetry/Any Gender Poetry/Commercial Break and Midnight - PO.pdf | refused: unrecognised | No parser matched this layout. |
| incoming/Poetry/Any Gender Poetry/Coney Island of the Mind - PO.pdf | refused: two_column (no parser yet) | 27% of lines have a gap across the middle of the page: two columns. |
