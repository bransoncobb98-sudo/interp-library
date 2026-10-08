# Classification request: batch 51 of 63 (40 records, IC-2001 to IC-2040)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-051-reply.json`.

## Rules

- Source text is authoritative. Metadata is secondary and never justifies altering the text.
- If a value cannot be supported by the text or the source document, leave it empty or use 'Not specified'. Do not guess.
- Every value carries provenance: source (stated in the document), computed (derived by a script), ai (suggested by an AI model), or human (entered or confirmed by a reviewer). Human values are never overwritten.
- Every AI value carries a confidence (high, medium, low) and one sentence of evidence that points to the text.
- The library records what sources state. It never asserts that a piece is legal or eligible for any league.
- Classify the PERFORMANCE TEXT. The introduction and the source block are context only.
- `content_warnings` must come from the performance text alone. Its evidence must quote the performance text in
  double quotes, for example: "he hung himself right there" describes a suicide. A quote taken from the
  introduction or the source block is rejected. If you find no sensitive content, give an empty list with evidence.
- `audience_level` is a suggestion, never a claim that a piece is appropriate. Give it only together with
  `content_warnings` for the same record.
- Omit a field when the text does not support a value. Never write 'Not specified' or 'Not assessed'; omit instead.
- Use only the allowed values below, spelled exactly. Single-value fields take a string; list fields take a list.
- `evidence` is one specific sentence: quote a few words in double quotes or name the passage. Never invent facts
  about the work, the author, a production or a league.
- Do not supply title, author, work, publisher, event, rights, word counts or any field not listed below.
- Fields a record lists as 'already set' were stated by the source or entered by a reviewer. Do not supply them.
- Performance marks such as (Pg 4), (Pause) or [bracketed words] are part of the text. Do not treat them as content.

## Fields to supply

### Literary form of the source work  (`literary_form`, ONE value (a string))

- Definition: The form of the published work the cutting comes from.
- Assign when: The form is stated in the source or evident from the text layout (stage directions and speaker labels mean Drama; lineated verse means Poetry).
- Do not assign when: Do not assign from tone or topic.
- Example: Speaker labels and stage directions: Drama.
- Allowed values:
  - "Prose": Fiction in sentences and paragraphs.
  - "Poetry": Writing arranged in verse lines.
  - "Drama": A play or screenplay.
  - "Nonfiction": Essay, memoir, journalism, transcript or other factual writing.
  - "Mixed": More than one form in the cutting.

### Overall tone  (`tone`, a LIST of values (an empty list means none present))

- Definition: The overall register of the cutting, distinct from the specific emotions played.
- Assign when: The register is evident from word choice and situation.
- Do not assign when: Do not list emotions; do not assign from the topic alone.
- Example: A comic account of a funeral: Lighthearted, Ironic.
- Allowed values:
  - "Lighthearted": Buoyant, amusing or breezy.
  - "Earnest": Sincere and heartfelt.
  - "Serious": Grave; weighty subject treated soberly.
  - "Bittersweet": Happiness and sadness together.
  - "Dark": Bleak or disturbing.
  - "Ironic": Meaning differs from the surface statement.
  - "Satirical": Mocks people, institutions or customs to criticise them.
  - "Whimsical": Playful and fanciful.

### Content warnings  (`content_warnings`, a LIST of values (an empty list means none present))

- Definition: Sensitive content that is present in the cutting text.
- Assign when: The text contains or directly describes the content.
- Do not assign when: Do not assign for a topic mentioned only in the introduction or the source block.
- Example: A narrator describes a shooting: Violence, Death, War/Trauma.
- Allowed values:
  - "Death": A death occurs or is described.
  - "Grief": Mourning or bereavement is central.
  - "Violence": Physical violence occurs or is described.
  - "Abuse": Physical, emotional or sexual abuse of a person.
  - "Sexual Content": Sexual acts or explicit references.
  - "Sexual Assault": Rape or sexual assault.
  - "Self-harm": Deliberate self-injury.
  - "Suicide": Suicide or suicidal thoughts.
  - "Substance Use": Drugs or alcohol use.
  - "Discrimination/Slurs": Discrimination, hate speech or slurs.
  - "Mental Health": Mental illness is depicted.
  - "War/Trauma": War, mass violence or traumatic events.

### Difficulty  (`difficulty`, ONE value (a string))

- Definition: How demanding the cutting is to perform well.
- Assign when: Sustained demands are evident (many characters, dialect, wide emotional range).
- Do not assign when: Do not assign from length alone.
- Allowed values:
  - "Beginner": One voice, a simple arc.
  - "Intermediate": A few characters or shifts.
  - "Advanced": Many characters, rapid shifts, dialect or a very wide emotional range.

### Performance demands  (`performance_demands`, a LIST of values (an empty list means none present))

- Definition: Skills the text clearly requires.
- Assign when: The text clearly requires it (many labelled speakers, written dialect, stated physical business).
- Do not assign when: Do not assign for one speaker with one voice.
- Allowed values:
  - "Character Differentiation": Several distinct characters.
  - "Vocal Variety": Wide vocal range or rapid pacing changes.
  - "Dialect": A dialect is stated or written.
  - "Physicality": Physical business is stated.
  - "Pacing/Timing Control": Pauses, beats or rhythm drive the piece.

### Suggested audience level  (`audience_level`, ONE value (a string))

- Definition: A suggestion only, never a claim of appropriateness.
- Assign when: Judged from content warnings and complexity; always labelled AI-suggested.
- Do not assign when: Do not assign when content warnings have not been assessed.
- Allowed values:
  - "Middle School": Little mature content.
  - "High School": Suitable for general high school use.
  - "Upper High School (mature content)": Contains mature content; reviewer discretion.

### Themes  (`themes`, a list of short phrases, at most 8, each under 60 characters)

- Short noun phrases for what the cutting is about. Only themes the text supports.

### Subject matter  (`subject_matter`, one sentence under 300 characters)

- One sentence describing what happens in the cutting.

## Records

---

## IC-2001: Clean, Cleaner, Cleanest

- Title: Clean, Cleaner, Cleanest
- Author (byline): Sherman Alexie
- Work: Not specified
- Publisher: The New Yorker Magazine
- Publication date as stated: The Fiction Issue: June 5 & 12,
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MARIE, NARRATOR, OWNER
- Teaser before the introduction: Yes
- Spoken words (computed): 1300
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sherman Alexie
ASIN: B071244LRM
Publisher: The New Yorker Magazine
Date (Month/Year): The Fiction Issue: June 5 & 12,
2017, Pgs 48-54
```

### Introduction (context only: never use it for content warnings)

```text
Hotel cleaning staff, predominantly women of color and immigrants, continue to face profound inequities in the hospitality industry. Despite their crucial role in maintaining cleanliness and ensuring guest safety, they rarely earn more than minimum wage, or have access to health insurance, sick leave, or job security. Many endure physically taxing and hazardous working conditions. These workers remain largely invisible, seldom acknowledged or valued by their employers or the guests they serve.

Marie’s been doing this job for decades. This is her story, well . . . the end of her story and what she has seen may shock you.

Clean, Cleaner, Cleanest by Sherman Alexie
```

### Performance text (classify this)

```text
MARIE: (Pgs 45-54) (knocking) Housekeeping. (louder) Housekeeping.

NARRATOR: On a Tuesday morning Marie knocked on the door of Room 213. A corner room. Larger than standard. With two big windows instead of one. Twenty dollars more a night. The guest had been there for a few nights and was supposed to check out by eleven. (Marie knocks again) There was no response. (Marie pushes it open, takes a step back) That was a learned self-defense behavior. You didn’t enter the room until you had a clear idea of what was waiting for you.

MARIE: Housekeeping.

NARRATOR: There was nobody in the living area. But the bathroom door was shut, so there could be somebody in there. A few years earlier, a naked guest had walked out of the bathroom as she was making the bed. They’d both yelped in surprise. Marie couldn’t stop laughing as she fled the room. But her fear of used hypodermics had lessened over the years. She got needle-stuck once when she was pulling off a pillowcase. She rarely saw a needle after crack and meth became more popular and cheaper than any other drug. You could shoot up meth, but it seemed that most people snorted it. Or smoked it. And accidentally started fires in small motel rooms. But the needles were starting to reappear. She felt sorry for those addicts -- for any addicts. They ended up looking like starving ravens. Like scarecrows after a brush fire. Like the babies born when starved ravens conceived with burned scarecrows.

Seven people had died at the motel. Two from overdoses, four from heart attacks, and one when a woman drunkenly fell over the second-floor railing and landed headfirst on somebody else’s minivan.

But she needed her job. She believed in her job. So, she cleaned the room. First, she picked up the dirty towels and shoved them into the laundry bag. She draped clean towels over the thin metal rod. The towels had been washed, yes, but they were so old that they’d forgotten how to be towels. And that thin metal rod had been pulled out of the wall so often by clumsy guests that it barely supported the weight of the towels. But no matter -- she still draped the towels with an eye-pleasing symmetry. Then she sprayed minty soap into the sink and the shower, did a quick wipe, and ran hot water to wash the soap down the drain. She knew she’d only cleaned the surface of things, but the soap’s strong minty smell would make it seem as if she’d cleaned more thoroughly.

MARIE: The illusion of clean.

NARRATOR: She’d once used that phrase when she’d been talking to Father James about her job, and he’d said that the phrase accurately described humans as well.

It took her only fifteen minutes to clean that room. That was good, because a mother and father with four kids had checked out of Room 144. The youngest kid, a toddler in a polo shirt, had taken off his pants and underwear -- had gone full Porky Pig -- then squatted and pushed out a public feces in front of the soda machine.

After so many years, Marie didn’t even mind cleaning up people’s feces and urine. She had discovered that it was vital to say “feces” and “urine” instead of using cruder terms for the messes that people left in the toilet. Or on the toilet. Or in the general vicinity of the toilet. Or sometimes not even in the bathroom at all. “Feces” and “urine” were medical terms. She was a motel maid, but it helped to think like a doctor or a nurse. It helped to think that she was helping people.

Marie was deathly afraid of what that family might have done in the privacy of their room. She dreaded the marathon of cleaning that likely awaited her. (beat)

In the beginning, there was Marie, Agnes, Rosa, and the other Rosa. Agnes was a drunk. She got fired for stealing from the guests. Rosa No. 1 married her high-school sweetheart and moved away; Rosa No. 2 was undocumented and quit after she heard rumors about an immigration sweep of local businesses. The sweep didn’t happen. Not that time.

Over the years, thirty or forty women had quit without saying a word. Many of them never bothered to pick up their last paychecks. Marie feared that some of those women might have been disappeared by the men in their lives. But most of them just didn’t care. Over the decades, Marie had worked with two or three hundred women.

There were drug addicts and alcoholics and women who dowsed their cleaning rags with disinfectant and huffed those poisonous fumes into their lungs. There were illegal and legal immigrants, though Marie didn’t care about their status. Every refugee is a precious child, she thought. There were maids of every race. Of every color. Of every religion.

There were women who cried often but would never explain their tears. There were women who never stopped talking about their aches and pains.

Marie’s knees and ankles hurt because she had so often squatted and kneeled to clean the floors. Her feet hurt because she stood for most of the day. And she’d never owned a good pair of work shoes.

One day, she’d twisted her back so severely that she’d collapsed in pain on the sidewalk. At the free clinic, she learned that “back spasms” was the fancy way to say “torn muscles.” Once or twice a year since then, she’d torn her back again. But she’d missed only a few days of work. She’d spend one day in bed, recovering, and then she’d force herself back to cleaning.

She’d slowly gained weight, three or four pounds a year. Not much, until you add it all up and discover that you’re a two-hundred-pound woman. The extra weight didn’t help her back. She went on dozens of diets. She failed.

Her hands hurt. Arthritis. And the recurring rashes caused by the soaps and disinfectants. Her skin itched and burned. She tried wearing gloves at work, but that only made her rashes migrate from her hands to her wrists, forearms, and elbows.

Some mornings, she woke with hands so stiff that she could not make fists. She could not hold her coffee cup or toothbrush. She’d submerge her hands in hot water and flex and flex until her fingers worked properly again.

MARIE: It’s hard work. But it’s not like working in a coal mine . . . Everything is temporary.

NARRATOR: On her last day of work, at age sixty-three, Marie was given a peculiar honor.

OWNER: You only have to clean one room.

MARIE: But I want the last full shift.

NARRATOR: Why? Because she needed that sense of completion. Because she wanted to use that last bit of money to buy herself a retirement gift. A new watch, perhaps, now that she didn’t have to worry about ruining it with water or cleaning fluids.

OWNER: I’ll pay you full shift for cleaning one room. That is my gift to you.

NARRATOR: So, she took her time. She scrubbed the toilet, sink, and shower with bleach. She picked wildflowers from a sidewalk crack, placed them in a plastic cup and set that on the bathroom windowsill. Then she polished all the wooden furniture. It was too cheap and old and battered to sparkle. But a dim star is more visible than a dark star. She cleaned the windows. That took a long time, because the windows had rarely been cleaned. This was the kind of motel where the curtains were rarely opened.

Finally, after three hours of cleaning Marie stepped out of the room and locked the door behind her.

The owner gave Marie her last paycheck in cash. Two weeks’ worth of money. Six hundred dollars. With Social Security and Medicaid and Medicare and good luck, Marie and her husband would survive.
```

---

## IC-2002: The Clown of God

- Title: The Clown of God
- Author (byline): Tomie dePaola
- Work: Not specified
- Publisher: Voyager Books
- Publication date as stated: 978-0156181921
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, GIOVANNI, MAESTRO, CROWD, BROTHER, TOWNPERSON, PEOPLE, WOMAN, BROTHER SEXTON, PRIEST
- Teaser before the introduction: No
- Spoken words (computed): 1277
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tomie dePaola
ISBN: 978-0156181921
Publisher: Voyager Books
Date (Month/Year): 978-0156181921
*The Arlecchino mask is one of the most popular masks in
the Commedia dell'Arte series. Arlecchino's usual role is
that of a faithful valet or servant, but in this context he is
also the clown, the acrobat providing lots of comic relief!
As soon as this character appears on stage there is always
lots of laughter at his absurd actions and words,
alternating between flashes of brilliance and plain idiocy.
You can't predict which will manifest itself at any time!
This is overlaid with wit and charm, as well as scheming to
meet his own objectives.
Colombina is usually cast as a mischievous maid in the
Commedia dell'Arte, a comic but not always virtuous figure
with a best friend (and sometimes lover) of Arlecchino.
Music and Lyrics of Little Drummer Boy – Our favorite
version is by Penatonix
https://www.youtube.com/watch?v=qJ_MGWio-vc
```

### Introduction (context only: never use it for content warnings)

```text
(Hum a few lines from The Little Drummer Boy)

It was Saint Therese of Lisieux who said: “You know well enough that Our Lord does not look so much at the greatness of our actions, nor even at their difficulty, but at the love with which we do them.” This was true of America’s Little Drummer boy and can be found in many legends and fables world-wide. A poor soul with little worthy to give a King, but with a heart so big, so open – that in itself becomes a gift.

based upon a French legend . . . The Clown of God by Tomie dePaola
```

### Performance text (classify this)

```text
NARRATOR: Many, many years ago, in Sorrento . . . there lived a small boy named Giovanni who had no mother and not father. He dressed in rags and begged his bread and slept in doorways. But he was happy, and he could do something wonderful. He could juggle. Every day he would go to Signor Baptista’s fruit and vegetable stall and juggle.

He would juggle lemons and oranges, apples and eggplants, and even zucchini. Crowds would gather to watch, and when Giovanni had finished, they would buy from Signor Baptista. Then Signor Baptista’s wife would give Giovanni a bowl of hot soup. It was a very good arrangement.

One day a troupe of traveling players came to town, and Giovani watched as Arlecchino and Colombina*, in their beautiful clothes, danced and sang.

GIOVANNI: (wonderstruck) Oh, that is the life for me!

NARRATOR: So when the play was over, Giovanni went and spoke to the Maestro.

MAESTRO: No, no. I have no need for a ragamuffin. Go beg your bread somewhere else.

GIOVANNI: (pleading) But I could be very helpful. I could help unpack and pack up. I could take care of the donkey, And, Maestro . . . . I can juggle! (he demonstrates)

MAESTRO: Not bad. With a bit more training and practice . . . All right! But no money. A place to sleep, the companionship of the finest players in Italy, and a bowl of noodles. That’s all.

GIOVANNI: Grazi, Signor.

MAESTRO: Go get your things. We leave in an hour.

NARRATOR: And so Giovanni said good-bye to Signor and Signora Baptista and became a traveling player.

Not long after, the Maestro gave him a costume and Giovanni juggled for the crowds. He would put on a clown face, step out from the curtain before the play began, bow, open up a colorful bag, roll out a carpet, and begin. He would juggle sticks. Plates. Then he would balance the plates on the sticks and twirl them. He would juggle clubs, rings, and burning torches.

Finally he would toss a red ball and an orange ball. Then a yellow ball. A green, a blue, and a violet ball until it looked as if he were juggling the rainbow.

GIOVANNI: And now for the Sun in the Heavens!

NARRATOR: Still juggling, he would pick up a shining golden ball and toss it higher and higher, faster and faster. And how the crows would cheer.

CROWD: (cheering)

NARRATOR: Giovanni became very famous, and it wasn’t long before he said good-bye to the traveling troupe and set off on his own. Up and down Italy he traveled, and although his costume became more beautiful, he always kept the face of a clown. Once he juggled for a duke. Once for a prince! And it was always the same.

First the sticks, then plates, then the clubs, rings, and burning torches. Finally the rainbow of colored balls.

GIOVANNI: And now for the Sun in the Heavens!

NARRATOR: And the golden ball would fly higher and higher and the crowds would laugh and clap and cheer. One day, between two towns, Giovanni was sitting in the shade of a tree, eating a lunch of bread and cheese. Two Little Brothers came down the road.

BROTHER: Will you share your food with us, good clown, for the love of God and the blessing of our Brother Francis?

GIOVANNI: Sit down, good fellows. There is more than enough.

NARRATOR: As the three men ate, the two Little Brothers told Giovanni how they went from town, begging their food and spreading the joy of God.

BROTHER: Our founder, Brother Francis says that everything signs of the glory of God. Why, even your juggling.

GIOVANNI: That’s well and good for men like you, but I only juggle to make people laugh and applaud.

BROTHER: It’s the same thing. If you give happiness to people, you give glory to God as well.

GIOVANNI: (laughing) If you say so! But now I must be off to the next town. Arrivederi, good brothers – and good luck!

NARRATOR: Wherever Giovanni went, the air was filled with his flying sticks and plates, his clubs and rings and torches. And, always, his rainbow of balls and “the Sun in the Heavens.” And wherever Giovanni went, the faces of the crowds would be all smiles, and the sound of laughter and cheers would ring through the towns. Years passed. Giovanni grew old and times became hard. People no longer stopped to watch.

TOWNPERSON: It’s only the old clown who juggles things. We’ve all seen him before.

NARRATOR: Giovanni was sad, but still he juggled, until one day he dropped “the Sun in the Heavens,” and the rainbow of balls came crashing down and the crowd stood around him and laughed!

CROWD: (pointing and laughing)

NARRATOR: But not from joy. Then they did a terrible thing. They threw vegetables and stones at Giovanni, so that he had to run for his life.

Beside a stream, Giovanni took off his clown face. He put away his sticks and his plates, his clubs and rings and colored balls. He put away his costume and he gave up juggling forever. What little money he had soon was gone, and his clothes became rags. He begged his bread and slept in doorways as he had done as a child.

GIOVANNI: (wearily) It’s time to go home.

NARRATOR: And he headed back to Sorrento. It was a cold winter night when he finally arrived. The wind blew hard, and an icy rain was falling. Up ahead loomed the monastery church of the Little Brothers.

The windows were in darkness. Wet and cold, old Giovanni crept inside and fell in a heap in a corner. Soon he was asleep. (Giovanni snores softly) It was the music that woke him up. The church was blazing with candlelight and filled with people singing

PEOPLE: (singing) Gloria! Gloria!

NARRATOR: Giovanni could scarcely believe his eyes. So much beauty! A long procession of brothers, priests, sisters and townspeople, all carrying beautiful gifts was winding its way through the church. They placed their gifts in front of a statute – of a lady and her child.

GIOVANNI: What is all this?

WOMAN: Why, old man, it’s the birthday of the Holy Child. It’s the procession of the gifts.

NARRATOR: Giovanni watched in amazement until the singing was over. Then the church emptied of all the people and was darkened except for the bright candles surrounding the Lady and the Child. Giovanni moved closer. The Child in the Lady’s arms seemed so serious, so stern.

GIOVANNI: (kneeling) Oh, Lady. I wish I had something to offer, too. Your child seems so dad, even with all these beautiful gifts. But wait – I used to make people smile.

NARRATOR: Giovanni opened his bag and shook out his old costume. Then he put on his clown face, bowed, rolled out the little rug, and began to juggle. First the sticks. Then the plates. Next he twirled the plates on the sticks. And then the clubs and rings . . .

The Brother Sexton, who was coming in to lock the doors, saw Giovanni juggling. He was horrified.

BROTHER SEXTON: Father Master! A sacrilege! Come quickly!

NARRATOR: But Giovanni didn’t hear or notice him.

GIOVANNI: (smiling at the Child) And now . . . First the red ball, then the orange . . . Next the yellow. And the green, blue and violet.

NARRATOR: Around and up they went until they looked like a rainbow.

GIOVANNI: And finally . . . The Sun in the Heavens!

NARRATOR: The gold ball flew up and around and around, higher and higher. Giovanni had never juggled so well in all his life. Higher and higher, faster and faster. A blaze of color filled the air. It was magnificent! Giovanni’s heart was pounding.

GIOVANNI: For You, sweet Child, for You! (he suddenly collapses)

NARRATOR: The priest and Brother Sexton came rushing in.

PRIEST: (kneeling over Giovanni, he makes the sign of the cross) Why, the poor clown is dead. May his soul rest in peace.

NARRATOR: But the Brother Sexton backed away . . .

BROTHER SEXTON: (backing away, he gapes at the statue of the Lady and her Holy Child; he points) Oh, Father! Oh, Father, look!

NARRATOR: The Child was smiling, and in His hand He held the golden ball.
```

---

## IC-2003: Crack and the Box

- Title: Crack and the Box
- Author (byline): Pete Hamill
- Work: Four in One: Rhetoric, Reader, Research Guide, and Handbook
- Publisher: Longman
- Publication date as stated: March 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2003
- Already set (do not supply): none

### Source block (context only)

```text
Author: Pete Hamill
Book: Four in One: Rhetoric, Reader, Research Guide,
and Handbook
ISBN: 978-0321481269
Publisher: Longman
Date (Month/Year): March 2007
```

### Introduction (context only: never use it for content warnings)

```text
In this original essay, a college student expresses his views regarding the relationship between drug consumers and television consumers. Despite the tragic American Situation regarding these issues, Hamill remains hopeful and proactive in providing a solution to Society’s addiction to “Crack and the Box” by Pete Hamill
```

### Performance text (classify this)

```text
One sad rainy morning last winter, I talked to a woman who was addicted to crack cocaine. She was twenty-two, stiletto-thin, with eyes as old as tombs. She was living in two rooms in a welfare hotel with her children, who were two, three, and five years of age. Her story was the usual tangle of human woe: early pregnancy, dropping out of school, vanished men, smack and then crack, tricks with johns in parked cars to pay for the dope. I asked her why she did drugs. She shrugged in an empty way and couldn't really answer beyond "makes me feel good." While we talked and she told her tale of squalor, the children ignored us. They were watching television.

Walking back to my office in the rain, I brooded about the woman, her zombielike children, and my own callous indifference. I'd heard so many versions of the same story that I almost never wrote them anymore; the sons of similar women, glimpsed a dozen years ago, are now in Dannemora or Soledad or Joliet; in a hundred cities, their daughters are moving into the same loveless rooms. As I walked, a series of homeless men approached me for change, most of them junkies. Others sat in doorways, staring at nothing. They were additional casualties of our time of plague, demoralized reminders that although this country holds only 2 percent of the world's population, it consumes 65 percent of the world's supply of hard drugs.

Why, for God's sake? Why do so many millions of Americans of all ages, races, and classes choose to spend all or part of their lives stupefied? I've talked to hundreds of addicts over the years; some were my friends. But none could give sensible answers. They stutter about the pain of the world, about despair or boredom, the urgent need for magic or pleasure in a society empty of both. But then they just shrug. Americans have the money to buy drugs; the supply is plentiful. But almost nobody in power asks, Why? Least of all, George Bush and his drug warriors.

William Bennett talks vaguely about the heritage of sixties permissiveness, the collapse of Traditional Values, and all that. But he and Bush offer the traditional American excuse: It Is Somebody Else's Fault. This posture set the stage for the self-righteous invasion of Panama, the bloodiest drug arrest in world history. Bush even accused Manuel Noriega of "poisoning our children." But he never asked why so many Americans demand the poison.

And then, on that rainy morning in New York, I saw another one of those ragged men staring out at the rain from a doorway. I suddenly remembered the inert postures of the children in that welfare hotel, and I thought: television.

Ah, no, I muttered to myself: too simple. Something as complicated as drug addiction can't be blamed on television. Come on.... but I remembered all those desperate places I'd visited as a reporter, where there were no books and a TV set was always playing and the older kids had gone off somewhere to shoot smack, except for the kid who was at the mortuary in a coffin. I also remembered when I was a boy in the forties and early fifties, and drugs were a minor sideshow, a kind of dark little rumor. And there was one major difference between that time and this: television.

We had unemployment then; illiteracy, poor living conditions, racism, governmental stupidity, a gap between rich and poor. We didn't have the all-consuming presence of television in our lives. Now two generations of Americans have grown up with television from their earliest moments of consciousness. Those same American generations are afflicted by the pox of drug addiction.

Only thirty-five years ago, drug addiction was not a major problem in this country. There were drug addicts. We had some at the end of the nineteenth century, hooked on the cocaine in patent medicines. During the placid fifties, Commissioner Harry Anslinger pumped up the butt of the old Bureau of Narcotics with fantasies of reefer madness. Heroin was sold and used in most major American cities, while the bebop generation of jazz musicians got jammed up with horse.

But until the early sixties, narcotics were still marginal to American life; they weren't the $120-billion market they make up today. If anything, those years have an eerie innocence. In 1955 there were 31,700,000 TV sets in use in the country (the number is now past 184 million). But the majority of the audience had grown up without the dazzling new medium. They embraced it, were diverted by it, perhaps even loved it, but they weren't formed by it. That year, the New York police made a mere 1,234 felony drug arrests; in 1988 it was 43,901. They confiscated ninety-seven ounces of cocaine for the entire year; last year it was hundreds of pounds.

During each year of the fifties in New York, there were only about a hundred narcotics-related deaths. But by the end of the sixties, when the first generation of children formed by television had come to maturity (and thus to the marketplace), the number of such deaths had risen to 1,200. The same phenomenon was true in every major American city.

In the last Nielsen survey of American viewers, the average family was watching television seven hours a day. This has never happened before in history. No people have ever been entertained for seven hours a day. The Elizabethans didn't go to the theater seven hours a day. The pre-TV generation did not go to the movies seven hours a day. Common sense tells us that this all-pervasive diet of instant imagery, sustained now for forty years, must have changed us in profound ways.

Television, like drugs, dominates the lives of its addicts. And though some lonely Americans leave their sets on without watching them, using them as electronic companions, television usually absorbs its viewers the way drugs absorb their users. Viewers can't work or play while watching television; they can't read; they can't be out on the streets, falling in love with the wrong people, learning how to quarrel and compromise with other human beings. In short they are asocial. So are drug addicts.

One Michigan State University study in the early eighties offered a group of four- and five-year-olds the choice of giving up television or giving up their fathers. Fully one third said they would give up Daddy. Given the choice (between cocaine or heroin and father, mother, brother, sister, wife, husband, children, job), almost every stoned junkie would do the same.

There are other disturbing similarities. Television itself is a consciousness-altering instrument. With the touch of a button, it takes you out of the "real" world in which you reside and can place you at a basketball game, the back alleys of Miami, the streets of Bucharest, or the cartoony living rooms of Sitcom Land. Each move from channel to channel alters mood, usually with music or a laugh track. On any given evening, you can laugh, be frightened, feel tension, thump with excitement. You can even tune in MacNeil Lehrer and feel sober.

But none of these abrupt shifts in mood is earned. They are attained as easily as popping a pill. Getting news from television, for example, is simply not the same experience as reading it in a newspaper. Reading is active. The reader must decode little symbols called words, then create ideas and make them connect; at its most basic level, reading 'images or an act of the imagination. But the television viewer doesn't go through that process. The words are spoken to him by Dan Rather or Tom Brokaw or Peter Jennings. There isn't much decoding to do when watching television, no time to think or ponder before the next set of images and spoken words appears to displace the present one. The reader, being active, works at his or her own pace; the viewer, being passive, proceeds at a pace determined by the show. Except at the highest levels, television never demands that its audience take part in an act of imagination. Reading always does.

In short, television works on the same imaginative and intellectual level as psychoactive drugs. If prolonged television viewing makes the young passive (dozens of studies indicate that it does), then moving to drugs has a certain coherence. Drugs provide an unearned high (in contrast to the earned rush that comes from a feat accomplished, a human breakthrough earned by sweat or thought or love).

And because the television addict and the drug addict are alienated from the hard and scary world, they also feel they make no difference in its complicated events. For the junkie, the world is reduced to him and the needle, pipe, or vial; the self is absolutely isolated, with no desire for choice. The television addict lives the same way. Many Americans who fail to vote in presidential elections must believe they have no more control over such a choice than they do over the casting of L.A. Law.

The drug plague also coincides with the unspoken assumption of most television shows: Life should be easy. The most complicated events are summarized on TV news in a minute or less. Cops confront murder, chase the criminals, and bring them to justice (usually violently) within an hour. In commercials, you drink the right beer and you get the girl. Easy! So why should real life be a grind? Why should any American have to spend years mastering a skill or a craft, or work eight hours a day at an unpleasant job, or endure the compromises and crises of a marriage? Nobody works on television (except cops, doctors, and lawyers). Love stories on television are about falling in love or breaking up; the long, steady growth of a marriage - it’s essential dailiness - is seldom explored, except as comedy. Life on television is almost always simple: good guys and bad, nice girls and whores, smart guys and dumb. And if life in the real world isn't that simple, well, hey, man, have some dope, man, be happy, feel good.

The doper always whines about how he feels; drugs are used to enhance his feelings or obliterate them, and in this the doper is very American. No other people on earth spend so much time talking about their feelings; hundreds of thousands go to shrinks, they buy self-help books by the millions, they pour out intimate confessions to virtual strangers in bars or discos. Our political campaigns are about emotional issues now, stated in the simplicities of adolescence. Even alleged statesmen can start a sentence, "I feel that the Sandinistas should . . ." when they once might have said, "I think . . ." I'm convinced that this exaltation of cheap emotions over logic and reason is one by-product of hundreds of thousands of hours of television.

Most Americans under the age of fifty have now spent their lives absorbing television; that is, they've had the structures of drama pounded into them. Drama is always about conflict. So news shows, politics, and advertising are now all shaped by those structures. Nobody will pay attention to anything as complicated as the part played by Third World debt in the expanding production of cocaine; it's much easier to focus on Manuel Noriega, a character right out of Miami Vice, and believe that even in real life there's a Mister Big.

What is to be done? Television is certainly not going away, but it’s addictive qualities can be controlled. It's a lot easier to "just say no" to television than to heroin or crack. As a beginning, parents must take immediate control of the sets, teaching children to watch specific television programs, not "television," to get out of the house and play with other kids. Elementary and high schools must begin teaching television as a subject, the way literature is taught, showing children how shows are made, how to distinguish between the true and the false, how to recognize cheap emotional manipulation. All Americans should spend more time reading. And thinking.

For years, the defenders of television have argued that the networks are only giving the people what they want. That might be true. But so is the Medellin cartel.
```

---

## IC-2004: The Day I Swapped My Dad for Two Goldfish

- Title: The Day I Swapped My Dad for Two Goldfish
- Author (byline): Neil Gaiman
- Work: Not specified
- Publisher: HarperCollins
- Publication date as stated: May 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: BOY, NATHAN, SISTER, MOTHER, VASHTI, BLINKY, PATTI, DAD
- Teaser before the introduction: Yes
- Spoken words (computed): 1429
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Gaiman
ISBN: 978-0060587017
Publisher: HarperCollins
Date (Month/Year): May 1997
```

### Introduction (context only: never use it for content warnings)

```text
When a boy swaps his dad for two goldfish, he doesn’t really think about the consequences . . .

BOY: Did so! After all, who would have suspected that other kids would go around swapping stuff too.

BOY: Okay . . . maybe I didn’t think about that! And when his mom finds out . . .

BOY: Who knew he’d be that valuable anyway??

The Day I Swapped My Dad for Two Goldfish by Neil Gaiman
```

### Performance text (classify this)

```text
BOY: One day my mom went out and left me at home with just my little sister and my dad. My dad sat in front of the television, reading his newspaper. My dad doesn’t pay much attention to anything, when he’s reading his newspaper. My little sister and I played in the garden. My sister played with her Barbie dolls, and I played at putting mud down my sister’s neck. My friend Nathan came over to my house. He had a glass bowl with him. There was something in the glass bowl. (to Nathan) “What’s that?”

NATHAN: Two goldfish. They are called Sawney and Beaney. Aren’t they neat?

BOY: They were pretty neat. (to Nathan) I’ll swap you them.

NATHAN: What for?

BOY: We went up to my bedroom. My little sister tagged along. I showed Nathan my old transformer robots and my baseball cards and my books. I showed him my old punching bag and my penny whistle that Mommy said made her head ache when I blew it. I showed him my old spaceship that didn’t float in the bath anymore, and the puppet with the tangled strings, and I even shoed him Clownie, my clown that I sleep with. And every time I showed him something, Nathan said, “No.” We went downstairs. (to Nathan) Isn’t there anything you would swap for the goldfish? (to audience) They were very nice goldfish. They were reddy-gold, and they swam backwards and forwards in their bowl.

NATHAN: No, not transformer robots or baseball cards or books or a punching bag., or a penny whistle, even if it does make your mom’s head ache, or a spaceship or a puppet or even that old Clownie.

BOY: I thought for a bit. Some people have great ideas maybe once or twice in their life, and then they discover electricity or fire or outer space or something. I mean, the kind of brilliant ideas that change the whole world. Some people never have them at all. I get them two or three times a week. (to Nathan) I’ll swap you my dad.

SISTER: Oh-oh!

NATHAN: That’s not a fair swap. I’ve got two goldfish and you’ve only got one dad.

BOY: He’s bigger than your goldfish, though. He’s as big as a hundred goldfish.

NATHAN: Can he swim?

BOY: Better than a goldfish.

SISTER: Liar. He splashes and splashes at the swimming pool.

NATHAN: Okay.

BOY: He gave me the two goldfish in the goldfish bowl, and took my dad away with him. I watched the goldfish for a while.

SISTER: You’ll get into big trouble when Mommy gets home. You’ll see.

BOY: When my mother came home I said . . . Mom, can we buy some gold fish food?

MOTHER: If we have to, dear. Where’s your father?

BOY: (to mother) Come and see my goldfish. Aren’t they pretty? (to audience) She shouted up the stairs. She knocked on the door of the bathroom. She called out into the garden. My father didn’t reply.

SISTER: Mumf, mumf, mumf!

BOY: (to mother) Don’t pay any attention to her. Come and look at my goldfish. (to audience) But my mother untied my little sister and took the sock out of her mouth.

MOTHER: Do you know where your father is?

SISTER: (pointing at the speaker) He swapped him to his friend Nathan for those two goldfish.

MOTHER: (sharply) Young man, is this true?

BOY: (to audience) She only calls me young man if she’s very, very mad. (to mother) Yes.

MOTHER: Right. (picking up the bowl of goldfish and handing it to speaker) You can take these goldfish over to Nathan this minute, and don’t you come back without your father.

SISTER: I told you so!

MOTHER: And you can go with him. Fancy allowing your brother to swap your father for two goldfish and a bowl. The very idea.

BOY: So we went to Nathan’s house. He only lives over the road. I knocked on the door. Nathan’s mother came out. (to Nathan’s mother) Is Nathan here?

N’s MOM: Where did you get those goldfish?They were a present to Nathan from his Aunt Violet.

BOY: I swapped them. And now I have to swap them back again. (to audience) She sent Nathan out to talk to me. (to Nathan) Here are your gold fish. Now can I have my dad back, please?

NATHAN: Well, yes and no.

SISTER: Oh-oh!

BOY: We went upstairs to Nathan’s bedroom. It was even messier than my bedroom. Nathan had an electric guitar, a big white one.

NATHAN: I swapped this electric guitar with Vashti Singh.

BOY: Nathan, what did you swap to Vashti, so she would give you her electric guitar?”

NATHAN: If you get off me, I will tell you . . . I swapped her your dad. Well, he wasn’t very exciting. All he did was read the paper.

BOY: I took the guitar and we walked over to Vashti’s house. (to sister) I could be a rock and roll star!

SISTER: You could be an idiot.

BOY: I rang Vashti’s doorbell. (to Vashti) I’ve got your guitar for you. (to audience) Vashti giggled. All Vashti’s sisters giggled too. (to Vashti) Can I have my dad back, please? (to audience) They giggled again.

VASHTI: (shrugging her shoulders) Wait here.

BOY: She took the guitar away from me. When she came back she was carrying a gorilla mask. (to Vashti) Oh, no.

VASHTI: I swapped your dad with Blinky. Blinky had this really good gorilla mask “

BOY: Where’s Blinky’s house?” (to audience) She told me how to get there. It was going to be a long walk. We set off.

SISTER: Can I put on the gorilla mask?

BOY: She put on the gorilla mask. (to sister - laughing) When are you going to put it on? When are you going to put on the gorilla mask? (to audience) My little sister took off the gorilla mask. We walked some more. I put on the gorilla mask. My sister went over to a policeman.

SISTER: Help! Quick! That gorilla is escaping from the zoo!

BOY: The policeman ran over and caught me. He made me take off the mask. Then he told me off. He would have told my sister off, only she did her innocent little girl face so he didn’t. It’s not fair. (sister giggles) (to sister) Watch it. Just watch it that’s all. (to audience) Blinky had a very big house. We went up to the front and rang the bell. The butler came out. (to butler) Can we speak to Blinky? (to audience) Blinky came down the big stairs. He looked very pleased to see the gorilla mask.

BLINKY: Are you bringing it back?

BOY: Yes, we are. (to audience) Blinky made the butler give us ginger beer. I liked it even though the bubbles tickled my nose. My sister made a face. (to Blinky after drinking the ginger beer) Now, where’s my dad? (to audience) He went away again around the side of the house.

BLINKY: (returning) This is Galveston.

BOY: Galveston was a fat white rabbit with one black ear.

BLINKY: Galveston’s what I swapped your father for.

BOY: I gave him the gorilla mask. He gave me Galveston and a map he drew of how to get to Patti’s house. I’d never walked so far in my whole life.

SISTER: I think ginger beer is the most horrible thing in the whole world.

BOY: Worse than boiled beets?

SISTER: No, not that bad.

BOY: While we walked, Galveston the Rabbit sat in my arms and made its nose go woffly. My sister tried to make her nose go as woffly as Galveston’s, but she couldn’t do it. I knocked on the door of Patti’s house.

PATTI: Galveston!

BOY: [She] took the rabbit away from us and fussed over it and gave it some lettuce, [then she] took my hand. We walked into the back garden. There was a little rabbit hutch there and next to the rabbit hutch was a little run with chicken wire all around it. My dad sat on the grass, in the chicken wire run reading his newspaper and eating a carrot. He looked a bit lonely, and he had grass all over his trousers. (to Dad – opening the gate) Come on, Dad. (to audience) My dad crawled through the gate on his hands and knees.

PATTI: He’s not a very good rabbit.

BOY: He’s not meant to be. He’s a very good daddy.

PATTI: He can keep the carrot. Thanks for bringing back Galveston.

BOY: No problem. Seeya.

SISTER: You like her. I can tell. I’m going to tell everyone at school.

BOY: Last week my little sister told everyone at school that I was adopted. The week before she told everyone at school that I was a space alien pretending to be me.

SISTER: If you do, I’ll tell everyone that you’re secretly fat.

DAD: Children.

BOY: And he carried on eating his carrot and reading his paper until we go home. When we got home my mother said things like, “Just look at the state of him!” and she made him go and have a bath and she put all his clothes into the washing. While Dad was in the bath, my mother told me off. And when she’d finished telling me off, she made me promise, cross my heart, that I would never – ever – swap my dad for anything ever, ever again. And I promised. So I won’t. But I never promised anything about my little sister . . . . .
```

---

## IC-2005: The Day the Crayons Quit

- Title: The Day the Crayons Quit
- Author (byline): Drew Daywalt
- Work: Not specified
- Publisher: HarperCollins
- Publication date as stated: July 2014
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, RED, PURPLE, BEIGE, GRAY, WHITE, BLACK, GREEN, YELLOW, ORANGE, BLUE, PINK, PEACH
- Teaser before the introduction: No
- Spoken words (computed): 1075
- Already set (do not supply): none

### Source block (context only)

```text
Author: Drew Daywalt
ISBN: 978-0007513765
Publisher: HarperCollins
Date (Month/Year): July 2014
```

### Introduction (context only: never use it for content warnings)

```text
I have a secret . . . (whispering) I still like to color! And even though my mom doesn’t put my pictures on the refrigerator anymore . . . I still color. Sometimes in coloring books (which I get in my stocking for Christmas each year) and sometimes pictures I draw myself. I love crayons!!!! And you know what . . . I’m proud of it. Heck, they are even making ADULT coloring books now! I saw them at the craft store, so I know I’m not the only one. But then I got to thinking . . . what if Crayons could talk? What would they say? How do they feel? The Day the Crayons Quit by Drew Daywalt.
```

### Performance text (classify this)

```text
NARRATOR: One day in class, Duncan went to take out his crayons and found a stack of letter with his name on them.

RED: Hey Duncan, It’s me RED crayon. We need to talk. You make me work harder than any of your other crayons. All year long I wear myself out coloring fire engines, apples, strawberries and everything else that’s Red. I even work on holidays! I have to color all the Santas at Christmas and all the hearts on Valentine’s day! I need a rest! Your overworked friend, RED crayon.

PURPLE: Dear Duncan, All right, listen, I love that I’m your favorite crayon for grapes, dragons and wizards’ hats, but it makes me crazy that so much of my gorgeous color goes outside the lines. If you don’t start coloring inside the lines soon . . . I’m going to completely lose it. Your very neat friend, PURPLE crayon.

BEIGE: Dear Duncan, I’m tired of being called “light brown” or “dark tan” because I am neither. I am BEIGE and I am proud. I’m also tired of being second place to Mr. BROWN crayon. It’s not fair that BROWN gets all the bears, ponies and puppies while the only things I get are turkey dinners (if I’m lucky) and wheat, and let’s be honest – when was the last time you saw a kid excited about coloring wheat? Your BEIGE friend, BEIGE crayon.

GRAY: Duncan, GRAY crayon here. You’re killing me! I know you love elephants and I know that elephants are gray, but that’s a lot of space to color in all by myself. And don’t even get me started on your rhinos, hippos and humpback whales. You know how tired I am after handling one of those things? Such BIG animals. . . baby penguins are gray, you know. So are very tiny rocks . . . pebbles. How about one of those once in a while to give me a break? Your very tired friend, GRAY crayon.

WHITE: Dear Duncan, You color with me, but why? Most of the time I’m the same color as the page you are using me on – WHITE. If I didn’t have a black outline, you wouldn’t even know I was there! I’m not even in the rainbow. I’m only used to color snow or to fill in empty space between other things, and it leaves me feeling . . . well . . . empty. We need to talk. Your empty friend, WHITE crayon.

BLACK: Hi, Duncan, I hate being used to draw the outline of things . . . things that are colored in by other colors, all of which think they’re brighter than me! It’s not fair when you use me to draw a nice beach ball and then fill in the colors of the ball with all the other crayons. How about a BLACK beach ball sometime? Is that too much to ask? Your friend, BLACK crayon.

GREEN: Dear Duncan, As GREEN crayon, I am writing for two reasons. One is to say that I like my work – loads of crocodiles, trees dinosaurs and frogs. I have no problems and wish to congratulate you on a very successful “coloring things GREEN” career so far. The second reason I write is for my friends, YELLOW crayon and ORANGE crayon, who are no longer speaking to each other. Both crayons feel they should be the color of the sun. Please settle this soon because they’re driving the rest of us crazy! Your happy friend, GREEN crayon.

YELLOW: Dear Duncan, YELLOW crayon here I need you to tell ORANGE crayon that I am the color of the sun. I would tell him, but we are no longer speaking. And I can prove I’m the color of the sun too! Last Tuesday you used me to color in the sun on your “Happy Farm” coloring book. In case you’ve forgotten, it’s on page 7. You can’t miss me. I’m shining down brilliantly on a field of YELLOW corn! Your pal and the true color of the sun, YELLOW crayon.

ORANGE: Dear Duncan, I see YELLOW crayon already talked to you, the big whiner. Anyway, could you please tell Mr. Tattletale that he IS NOT the color of the sun? I would, but we’re no longer speaking. We both know I am clearly the color of the sun because on Thursday you used me to color the sun on BOTH the “Monkey Island” and the “Meet the Zookeeper” pages in your “Day at the Zoo” coloring book. Orange you glad I’m here? Ha! Your Pal (and the real color of the sun). ORANGE crayon

BLUE: Dear Duncan, It has been great being your favorite color this past year, and the year before, and the year before that! I have really enjoyed all those oceans, lakes, rivers, raindrops, rain clouds and clear skies. But the bad news is that I am so short and stubby, I can’t even see over the railing in the crayon box anymore! I need a break! Your very stubby friend, BLUE Crayon

PINK: Duncan, Okay, listen here, kid! You have not used me ONCE in the past year. It’s because you think I am a girls’ color, isn’t it? Speaking of which, please tell your little sister I said thank you for using me to color her “Little Princess” coloring book. I think she did a fabulous job of staying inside the lines! Now, back to us. Could you please use me sometime to color the occasional pink dinosaur or monster or cowboy? Goodness knows they could use a splash of color. Your unused friend, PINK crayon

PEACH: Hey, Duncan, It’s me, PEACH Crayon. Why did you peel off my paper wrapping?? Now I’m naked and too embarrassed to leave the crayon box. I don’t even have any underwear! How would you like to go to school naked? I need some clothes. HELP! Your naked friend, PEACH crayon

NARRATOR: Well, poor Duncan just wanted to color . . . and of course he wanted his crayons to be happy. And that gave him an idea. (pantomime Duncan coloring with all his crayons) TRANSITION He created a GREEN and BLUE ocean, with an ORANGE whale giving a lift to two small GRAY penguins, a PINK policeman, a BLUE crocodile and a GREEN monkey. An ORANGE sun shone down from a YELLOW sky sporting a BLACK rainbow. PURPLE and PINK dragons and a WHITE polar bear frolicked in the waves, while a RED Santa watched a PINK bus driver give a floating lift to a GREEN pig. And as for BEIGE and PEACH . . . well . . . he tried!

NARRATOR: When Duncan showed his teacher his new picture, she gave him an A for coloring . . . . and an A+ for creativity!
```

---

## IC-2006: The Death of Tommy Grimes

- Title: The Death of Tommy Grimes
- Author (byline): R.J. Meaddough
- Work: Modern Black Stories
- Publisher: Barron's Educational Series
- Publication date as stated: 1971
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1776
- Already set (do not supply): none

### Source block (context only)

```text
Author: R.J. Meaddough
Book: Modern Black Stories
ISBN: 978-0764191527
Publisher: Barron's Educational Series
Date(Month/Year): 1971
```

### Introduction (context only: never use it for content warnings)

```text
Some have said that “The ethical fabric of society is made weaker and more dangerous by encouraging children, who are in the process of learning values, to inflict pain and suffering.” Others believe that the sport of hunting is one of the most exciting pastimes available – pitting man against nature. I hesitate to endorse either stance, as I believe that decision is an individual one for each person. However, the following selection “The Death of Tommy Grimes” by R.J. Meaddough did cause me to stop and think about my own personal value system. I hope it does the same for you.
```

### Performance text (classify this)

```text
Tommy had become part of the ground. At least he felt that way as he watched the dew and the daylight make giant shiny cobwebs of the treetops. The sun had not yet risen and a mist lay over the ground, which made the forest seem rather spooky to him.

His nose itched and he longed to scratch it, maybe just nudge it a little, but Pa said don ‘t move, don’t twitch, don’t even breathe hard. Not one arm, one hand, even one finger, he said. “He knows the woods,” Pa told him; “you’ll never know he’s there; suddenly he’ll just be there looking at you, just looking.”

It started so long ago, Tommy remembered, almost a year, when he was just eleven. That night, in the henyard, with the weasel’s eyes glistening in the flashlight. He never even fired a shot, just stood there with his mouth open, foolish, while the weasel dashed into the woods.

And Pa knocking the rifle from his hands and asking, “Why didn’t you shoot? What you waiting on? What’s wrong with you boy?”

“Pa, I . . . I couldn’t, Pa. I just couldn’t.”

“You never did like to kill nothing did you, boy? Even when you was small.”

Tommy looked at the ground without saying anything and his father sighed, “Tommy, dammit, a man always dies a little when he kills something, but it just plain has to be done. Some animals just ain’t no damn good and got to be killed. Understand?”

He nodded without answering, still looking at the ground, and Pa stood up with a groan and they walked into the henhouse without speaking. They counted forty-three dead pullets, lying in red and white patches of feathers, blood and confusion.

So he began to practice with the rifle, shooting at moving targets, and the rifle became part of his arm.

It got so that he could hit anything he aimed at, even things a good bit out. And sometimes, when he turned real quick, he would see pride in Pa’s eyes. But then Pa would always make his face blank and say, “We-e-ell, Tommy,” real grim-like, “you’re getting better but you need more practice.”

Pa taught him how to track animals and how to lead quail, and how to lean into the rifle to take up the recoil. And Pa showed him how to lie quiet so the forest forgot he was there and Nature went on about her business.

And the time came last night when Pa came home and mentioned that some of the men were going into the forest to get a buck; and how it might be some good shooting because bucks were fast, real fast.

“Pa,” he murmured, “think maybe I could go a time at that old buck?”

“Boy, this ain’t no old buck, it’s a young one,” Pa said, making like he was surprised. “Boy, you might get hurt.”

“Some time, I think I’d like to take my turn,“ he answered..

“Well I’ll think about it, boy,” Pa mumbled, but he couldn’t hide a gleam in his eye.

Tommy slowly, ever so slowly, rubbed his forehead along his sleeve and watched the gloom in front of him. Somewhere out there Pa had circled around and was trampling through the woods, scaring everything away, away toward the clearing where he lay waiting.

He laughed in his mind when he thought of the last time when Pa had gone down to the Hut for a drink with the “boys,” as he called them. And when he came out his eyes were gleaming like the mischief and he wobbled into the yard like he didn’t know how to walk. He had gone downstairs in his pajamas and they sat on the back porch and listened to the crickets and looked at the stars. Then Pa filled his pipe and stared out across the backyard toward the north pasture.

“Dawn in the forest is a beautiful thing, boy, beautiful. All the colors and wild flowers, fresh streams, cool breeze, you feel like, boy, feel it! Even though there ain’t a sound you feel it. You see a flash of white and you know some rabbit’s going home. Or you might see a chuck burrowing in. And the trees,” he whispered, “They just stand there watching you. Been there before you came, be there after you gone.”

“Gee, Pa,” he murmured, “you make it sound so nice I don’t know’s I want to hunt tomorrow.”

Pa smiled. “It is nice, boy, real nice, but things got to be done to keep it that way. Fox eats a rabbit he keeps the rabbit population down, else they’d overrun the land. Same here. You hunt ‘cause you hungry and got to eat, that’s one reason. Then you might hunt for the sport – pit your mind against animal cunning – ‘course I don’t hold much with that, but some do. Some do. But there’s some varmints that do damage and just plain got to be killed. Understand?

“I . . . think so. But what about what you said about a man dying when he kills something?”

“Man kills once and he starts to get callous. Next time it ain’t so hard. Then you get so’s you make a decision that something’s got to die and you kill it, just like that. Then you dead, boy. You got no feeling no more so you just as good as dead. You just ain’t had time to lay down.”

Tommy wiggled his toes and got no response. They felt like sticks of wood, stilts that somebody had glued on his legs. The mist was thinning and the sun began to shine dully through the trees. Pa was right, he thought. Seems as if everything had a place in the scheme of things. Birds ate worms they found on the ground. Then they got eaten by bigger birds. Rabbits got eaten by foxes and foxes by bobcats, and bobcats by bears or something all the way up to elephants. And elephants were killed by man. Pa said that ma preyed on himself, whatever that meant, but everything had a place, and when they got out of place they upset the balance. Like too many rabbits or squirrels or anything.

The silence somehow nettled him . . . the silence! Not a sound! No crickets, no chirping, no rustling, nothing. There was something out there! The happy-scared feeling ran up and down Tommy’s back and his breath came in painful gasps. His chest hammered, almost pushing his lungs into his mouth with its rhythm which seemed to be saying: Soon! Soon! Soon they would be calling him Tom Grimes like his father. Soon he would be able to go into the Hut and drink liquor with the rest of the men. Soon the waiting would be over. Soon he would be grown. Soon! Soon! Soon!

There! In the bushes! A little pinch of color behind the bramble bush moving light and easy, so very easy, behind the bushes. He slid down still further behind the gun and spread his feet wide, toes digging into the soft earth. “Put the whole side of your body behind the gun to take the recoil,” Pa had said. “Spread your legs wide to brace yourself. Make the gun, your arm, your hoip, your leg into one long ine.” Tommy drew his breath in and nearly gagged trying to hold it, sighting along the clean black ridges of the rifle. The outline was clear behind the bush, creeping, sniffling, gliding along.

“You won’t see it, or hear it, or smell it, or anything,” Pa had told him. “You’ll just feel it, and it’ll be there.”

Tommy breathed out and in, let some of the air out and chokingly began to squeeze the trigger. Would it never go off, his mind asked, reeling and stumbling and clinging desperately to reality, and the earth stuttered. The light blinked. His ears rang. His nose reacted to the smell of smoke and the taste of ink crept into his mouth. There was a rustling sound in the bushes and a thrashing, a terrible thrashing and rattling, but it stopped. Suddenly it stopped. Tommy blinked. It was over; just like that, it was over.

He got to his feet and the stiffness forced him to lean against a tree trunk. Before there had been nothing, then suddenly there was something, a small patch of color the same as Pa’s jacket. Tommy blinked and listened for the crashing sound of someone coming through the forest – but there was nothing. Nothing. He strained his ears and heard new-sprung crickets and birdcalls, but no crashing, no rustling, no voice, and he started for the bush and then stopped, trembling.

“Pa?” he whispered, “Pa-a-a?” There was no sound except his own voice, twisted and shapeless and mocking, twirling through the trees like vapors in the dull, chilly air. “Pa! Pa! Pa!”

Then came the rushing and the crashing to the left and the tall husky figure coming out of the gloom saying, “Boy? What’s wrong, boy?” And Tommy ran over and slammed his head against his father’s chest. “Pa! I thought I killed you, Pa. I thought I killed a man!”

“Now, Tommy, it’s all right, everything’s all right,” Pa said, walking behind the bush and kneeling and then rising and coming back.

“See?” he said. “What did I tell you? Right through the heart. Now that’s good shooting. Come on over here and look; come on, now.”

So he looked, and then it wasn’t so bad.

Later, much later, they walked the mile from town to the Hut and walked inside together. There were some men sitting at tables and they looked up as Pa hoisted him onto the bar, running his fingers through his dark, blond hair.

“Boys, I wanna tell you my boy became a man today. Yessir, killed his first nigger.”

“No!” a man said. “Who?”

“Swamp-buck got away from the chain gang yes-tidy. Yessir, got him right though the heart.”

The man grabbed Tommy and hugged him around the knees. “You a man now, boy!” he yelled, “you a real live honest-to-goodness ‘fore God man!”

And Pa, his blue eyes agleam, yelled out, “Bartender! Don’t just stand there! Give this man a drink!”

The man sat Tommy down on the bar and the liquor made him cough a bit as it coursed down his throat and it made his ears ring like the tolling of bells. But he smiled happily as the feeling of warmth like Mississippi sunshine spread through his insides. For now he belonged.
```

---

## IC-2007: The Department of Nothing

- Title: The Department of Nothing
- Author (byline): Colin Firth
- Work: Speaking with the Angel
- Publisher: Riverhead Trade
- Publication date as stated: Feb 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1547
- Already set (do not supply): none

### Source block (context only)

```text
Author: Colin Firth
Book: Speaking with the Angel
ISBN: 978-1573228589
Publisher: Riverhead Trade
Date (Month/Year): Feb 2001
```

### Introduction (context only: never use it for content warnings)

```text
The relationship between a young child and his grandmother is unmeasurable. Henry defines the hours spent with Grandma as the “best thing” and the time away from her and her stories as “time waiting to get back to this place of adventure, love, and imagination.”

The Department of Nothing by Colin Firth
```

### Performance text (classify this)

```text
Items indicated this way <> are suggestions to convey the story. ***Directing note: at the start turn the clock away --- at the end turn the clock back to the audience.

Emma wildly fought for passage --- and lo! By grace, she fell upon a door which gave onto . . . The Night Garden: full of eerie beauty and tranquility. Here the wind fell silent --- All around were crumbling walls and sundials, terrible gargoyles. What she didn’t see were little devilish faces poking from behind rocks. Then, one of them said, “Who are you?”

Before anyone could answer, this big loud voice from somewhere else, suddenly shouted, “Henry!!!” Which is my name . . .

And then it was just me sitting next to my grandma’s bed, probably late for school, wishing Grandma’s stories didn’t have to be always interrupted. I still wanted Grandma to go on, but that’s always when she gets strict and says, “No more talking, the session is closed.”

Whenever I’m listening to a story I always turn her bedside clock away (turn the clock away) so I don’t see the time. She says I’m not allowed to, because I have to respect punctuality – but I always manage it.

It’s strange, because the place where clocks most can’t get you is in her stories.

So when I came out of Grandma’s room I already knew I’d be thinking about the rest of the story until five o’clock. Your life is made of half-finished stories.

There’s a name for all this: most people call it real life, but actually it’s called the Department of Nothing. It’s not just one department, but loads of mini departments. School is the Paper Department, where they have this special doom-paper so that anything you write on it is doomed. Then there’s the Waiting Room of Nothing where you get told Not now, I’m busy, or You’re not old enough yet and all that.

Absolutely everyone lives there --- unless they get to go to Grandma’s room, which is the only way out of the Department. The trick is holding on to the magic to get you through the Department of Nothing.

Grandma doesn’t live in the world anymore, because she has to live in her room. Her health isn’t brilliant. And sometimes when she’s doing a story, I look at her hands, which I know are really old and kind of baggy but they’ve got paths that lead where you don’t know, like a map of mountains and rivers of countries you wish you could get to.

When you go to Grandma’s room, it’s like exploring with no fence at the end. She makes her room seem bigger than the world outside, which she wants to escape into, and I think it’s sad that there’s something back-to-front about it all. I want to escape to her room, and she wants to escape into the Department of Nothing.

Grandma tries to persuade Mum to let her go out—to church or something. That’s what she talks about wanting to do, and she talks about it a lot. Grandma said she felt like Rapunzel, but who everyone’s forgotten about. She said, “My prince would get a bit of a nasty shock if he climbed the walls and saw me now, wouldn’t he?

I did get detention. When I got there <Mr.> McVittie had started a biology lesson. The thing is, at that exact same moment I was quite sure I saw a Devil Creature from Grandma’s story sitting at my desk. He was only there for a second and then he was gone and McVittie was saying, “look at me when I’m talking to you,” and then he said, “Don’t look at me like that.”

Lynne Lassin saw it and asked me what it was, so I told her . . . and it meant telling a bit of the story . . . and you know what? She thought it was very cool indeed. And when it came lunchtime she wanted to hear the rest. I didn’t mind/

I carried on the story and Deborah Willis and Zena Whitechurch came and listened as well.

I wasn’t sure about telling Grandma about it all, because I thought maybe I should have asked her permission or something. But when I told her, she acted like she was about seven. She clapped her hands and kept asking what they’d said, and how she wished she could have seen their faces.

I said, “Why don’t I bring you to school so you can see them?” And she said, “You don’t bring old ladies to school, Henry.” She said I would take her stories out of here and that was wonderful, because that way I’d be taking her out of her room every day. She did this big smile and said, “I’m your muse!”

The next day I had about fifteen people listening to the story. It was brilliant, but I started to get so many questions that it got quite difficult to carry on, without being able to ask Grandma.

Finally, I told them all about Grandma, and now everyone wants to meet her. So I decided to bust Grandma out of her room. That way she can see people’s faces at last when she tells a story and they can see she’s real and maybe see other things are real, too --- and the Department of Nothing might not be so nothing.

Grandma did escape, but I didn’t bust her out. She bust herself out, by ambulance.

The visit to the hospital was like a visit to the Nothing Department of the Department of Nothing…only more depressing --- like a place where everyone’s been in detention for about five hundred years; I was a bit scared. I didn’t know what it would be like trying to talk to her, but I really really wanted to know how the story ended. It was a bit creepy ‘cause she was in bed and only her bedside light was on and I thought she was asleep, but when I got close to her she opened her eyes quickly like a vampire. I said “Bugger” really loudly and it’s the only time I’ve ever said that in front of Grandma, and she didn’t tell me off. I said, “I came to sit with you for a while, Grandma.” And she said, “That’s another ring on your tree of shadows.” I didn’t know if it was a secret message, or what. Anyway it seemed very serious and it made me say what normally I would have been embarrassed to, which was, “I love you, Grandma.” And then she smiled this huge smile, which started out really nice but then it kept getting bigger until I could see all her dentures and then I realized she wasn’t smiling, she was poking out her teeth. She reached up and put them in the glass. This always means no more talking. The session is at an end. Anyway it didn’t look much like I was going to find out what happened.

The next day all the people who had listened to the stories, because I couldn’t tell the rest, started saying there was no such thing as my grandma.

That evening I fell asleep in Grandma’s room and I dreamt that I heard her dentures talking by themselves in the glass. They introduced themselves as “A fine set of molars, eight incisors, upper and lower, and four canines with a perfectly sound bite. How do you do.” And they had this really strong Scottish accent.

I asked them if they could finish Grandma’s story and they said yes, but not yet. I said why not, and they said ‘cause we hadn’t got to the end. And I got angry with the teeth and threatened to pour their water out.

I said, “Are you saying she’s definitely going to die?” And they said, “I don’t know, I’m a set of teeth!”

I just knew when it happened. I was on the railway line going to school, and it was a bit rainy, and I suddenly got the smell of Grandma’s room in a gust of wind. I didn’t even think about it; I turned around and ran home.

The house was locked, so I went up the drainpipe into Grandma’s room. Her eyes and her mouth were open and her skin was all stretched and her head was kind of back on the pillow. I stopped looking at her and ran out where the woods start. It was all slippery on the gravel from wet leaves and I kept falling over.

I went home in the afternoon. My mum knew that I knew when she saw me. She hugged me and I cried again.

During the funeral I kept trying to think up an ending for the story. Emma, maybe she goes off happily ever after with Blind Jack who’s not blind any more …’cause it’s a story. Actually, you know what? Jack could rescue her, ‘cause with being blind it wouldn’t make any difference, the castle being invisible! That’s not bad, is it? So maybe that’s the ending.

So it’s back to the Department of Nothing but I had one or two tales to tell myself now, and maybe I should try them out. So that’s what I just did.

And the session is now closed. (Turn the clock back to the audience)
```

---

## IC-2008: Dinorella: A Prehistoric Fairy Tale

- Title: Dinorella: A Prehistoric Fairy Tale
- Author (byline): Pamela Duncan Edwards
- Work: Not specified
- Publisher: Scholastic, Inc.
- Publication date as stated: Jan 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, DORIS, DORA, DINORELLA, FAIRYDACTYL, DUKE, DEINONYCHUS, DINOSAUR, DINOSAUR DAME 1, DINOSAUR DAME 2, DORA/DORIS
- Teaser before the introduction: No
- Spoken words (computed): 504
- Already set (do not supply): none

### Source block (context only)

```text
Author: Pamela Duncan Edwards
ISBN: 978-0590689489
Publisher: Scholastic, Inc.
Date (Month/Year): Jan 1997
```

### Introduction (context only: never use it for content warnings)

```text
Ready for a new twist on the Cinderella fairy tale? A tale full of dinosaurs, mistaken identity and a battle? Well, wait no longer! It’s . . .

Dinorella: A Prehistoric Fairy Tale by Pamela Duncan Edwards
```

### Performance text (classify this)

```text
NARRATOR: Dora, Doris and Dinorella lived down in the sand dunes in a dinosaur den. Dora and Doris did nothing all day. They dumped debris around the den. They never did the dusting or the dishes. Dinorella was dainty and dependable. Dora and Doris were dreadful to Dinorella. All day they demanded . . .

DORIS: Dinorella, dig the garden.

DORA: Dinorella, fetch us drinks.

DORIS: Dinorella, start the dinner.

DORA: (sniggering) She’s a dingbat!

DORIS: (giggling) She’s a dumbhead!

NARRATOR: One day a card was delivered to the den:
Dinosaur Dance
Duke Dudley’s Den at dusk
Hors d’oeuvers, Dandelion Cola
Dancing until dawn

Duke Dudley was the most dashing dinosaur in the dunes.

DORA: (decorating herself with dinosaur jewels) I would die for a date with the duke.

DORIS: (sighing as she dolls up for the dance) Definitely.

DINORELLA: A dance. How divine!

DORIS: You can’t go to the dance. You’re too dowdy.

DORA: You’re too dull. And you don’t have decent dinosaur jewels. Of course you can’t go to the dance.

NARRATOR: Poor Dinorella felt down in the dumps as she watched her stepsisters depart. Suddenly, Dinorella heard a droning noise.

FAIRYDACTYL: Don’t be dismal. You shall go to the dance.

DINORELLA: But I’m so drab, and I don’t have decent dinosaur jewels.

FAIRYDACTYL: I’ll soon deal with that. (waves her wand and jewels magically appear) These will outdazzle all other dinosaur jewels.

DINORELLA: Darling, Fairydactyl!

NARRATOR: With her diamonds dangling, she set out for the dance. Dusk had fallen when Dinorella heard a deafening disturbance coming from the direction of Duke Dudley’s Den. A dastardly deed was taking place. A Deinonychus was dragging off the Duke.

DUKE: I’m done for! He will devour me!

DEINONYCHUS: Indeed, I will! (evil laugh) I’ll be digesting you by daybreak!

NARRATOR: Dinorella was not a daring dinosaur, but something drastic had to be done.

DINORELLA: I may become dessert, but I’m determined to drive away that dreaded carnivore. (climbing to the top of a dune and roared) You disgusting dummy, drop the Duke! (grabs some dirt and gets ready to attack)

NARRATOR: Dinorella began to hurl dirt balls at the deinonychus. The dumbfounded deinonychus stopped in disbelief.

DEINONYCHUS: Who called me a dummy?

NARRATOR: The moon’s light caught Dinorella’s dangling diamonds. Dots and dabs of light darted toward the deinonychus.

DEINONYCHUS: (blinded by the light) A devil! See its dreadful demon eyes?

NARRATOR: Dinorella detached a diamond and directed it toward the deinonychus. The diamond hit the deinonychus hard in his dentures.

DEINONYCHUS: (bellowing) The devil will destroy me with its deadly eyes!

NARRATOR: He dumped Duke Dudley and departed double-quick. (Deinonychus runs away) The den was dense with dinosaurs dashing about in distress.

DINOSAUR: A demon! We’re doomed!

DUKE: Dimwits! Demons don’t throw diamonds. It was a damsel who defended me with her dazzling dinosaur jewel. When I discover her, I shall ask her to be my darling.

NARRATOR: All the dinosaur dames were delirious.

DINOSAUR DAME 1: The jewel is mine!

DINOSAUR DAME 2: The jewel is mine!

DORIS: Mine!

DORA: (bellowing) No, definitely mine. I am the damsel you desire.

DUKE: I doubt it. Your dinosaur jewels don’t match.

NARRATOR: Just then, Fairydactyl arrived at the dance. She quickly saw the dilemma.

FAIRYDACTYL: Where is Dinorella?

DORA: (scoffing) Dinorella! That dopey domestic?

DORIS: (laughing) Dinorella! She’s back at the den.

NARRATOR: But Fairydactyl spied Dinorella dodging behind the dune.

FAIRYDACTYL: Dinorella, come down!

NARRATOR: So down came Dinorella, looking distracted.

DUKE: She wears but one dazzling jewel! (Dinorella’s hands rush to her ears where there is only one dangling diamond left) Dinorella, you are adorable. You’re definitely quite a dish. I beg you to be my dearest.

DINORELLA: Dreamy! (they dance off into the dawn)

DORA/DORIS: Drat!
```

---

## IC-2009: Doc Brackett

- Title: Doc Brackett
- Author (byline): Damon Runyon
- Work: The World's Best Bathroom Book
- Publisher: Honor Books
- Publication date as stated: 2005
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 449
- Already set (do not supply): none

### Source block (context only)

```text
Author: Damon Runyon
Book: The World's Best Bathroom Book
ISBN: 978-1562927264
Publisher: Honor Books
Date (Month/Year): 2005
```

### Introduction (context only: never use it for content warnings)

```text
Popular culture presents a variety of mythic frontier doctors, like Doc Baker from the 1970s television series Little House on the Prairie, galloping across the prairie to save young Billy or help Ma deliver a baby at the Nelson farm. In many ways, the myth was real. Most country doctors lived in town and traveled widely to visit sick patients on their homesteads.

Doc Brackett speaks to the strong (almost religious) beliefs about the power of medicine in American culture. In a culture whose main values are narcissism and materialism, medicine appears to hold the "keys to the kingdom" once held by religion. On a more personal level, the story symbolizes the experience of being a healer at any time or place. The sick are needy, vulnerable, and sometimes demanding; the physician is only human, can only accomplish so much. Doc Brackett by Damon Runyon.
```

### Performance text (classify this)

```text
.

Doc Brackett was a fine man. He doctored in our town for many years. He doctored more people than any other doctor in our town but made less money. That was because Doc Brackett was always doctoring poor people, who had no money to pay.

He would get up in the middle of the coldest night and ride twenty miles to doctor a sick woman or child or to patch up some fellow who got hurt. Everybody in our town knew Doc Brackett's office was over Rice's clothing store. It was up a narrow flight of stairs. His office was always filled with people. A sign at the foot of the stairs said: "DR. BRACKETT, OFFICE UPSTAIRS"

Doc Brackett was a bachelor. He was once supposed to marry Miss Elvira Cromwell, the daughter of old Julius Cromwell, the banker. But, on the day the wedding was supposed to take place Doc Brackett got a call to go out into the country and doctor a Mexican child.

Miss Elvira got sore at him and called off the wedding. She said that a man who would think more of a Mexican child than of his wedding was no good. Many women in our town agreed with Miss Elvira Cromwell, but the parents of the Mexican child were very grateful to Doc Brackett when the child recovered.

For forty years the lame and the halt and the blind of our town had climbed up and down the stairs to Doc Brackett's office. He never turned away anybody. He lived to be seventy years old and then one day he just keeled over on the sofa and died. By this time his black hair had turned white. Doc Brackett had one of the biggest funerals ever seen in our town. Everybody went to pay their last respects when he was laid out in Grubers undertaking parlor. He was buried in Riverview Cemetery.

There was talk of raising money to put a nice tombstone on Doc Brackett's grave as a memorial. The talk got as far as arguing about what should be carved on the stone about him. Some thought poetry would be very nice. Doc Brackett hated poetry. The matter dragged along and nothing whatever was done.

Then, one day George Gruber, the undertaker, said that Doc Brackett's memorial was already over his grave, with epitaph and all. George Gruber said the parents of the Mexican child that Doc Brackett had saved years ago had worried about him having no tombstone. They had no money themselves, so they took the sign from the foot of the stairs at Doc Brackett's office and stuck it over his grave. It read: "DR. BRACKETT, OFFICE UPSTAIRS."
```

---

## IC-2010: Don’t Blame it on Adam

- Title: Don’t Blame it on Adam
- Author (byline): Anonymous Folktale
- Work: 101 African-American Read-Aloud Stories
- Publisher: Black Dog & Levanthal Publishers
- Publication date as stated: Jan 1998
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1032
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kantor, Susan (ed)
Book: 101 African-American Read-Aloud Stories
ISBN: 1579120393
Publisher: Black Dog & Levanthal Publishers
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
God created Adam and Eve and placed them in a garden of numerous fruit trees from which they could eat anything, except the fruit from one tree. Although Adam and Eve had no concept of good and evil, they obviously did know about disobedience, since Eve told the serpent, "From the fruit of the trees of the garden we may eat; but from the fruit of the tree which is in the middle of the garden, God has said, 'You shall not eat from it or touch it, or you will die.'" From her statement, it is clear that Eve knew that she shouldn't eat the fruit. However, she chose to disregard the instruction and did eat of the forbidden fruit. When confronted, she did not admit fault but blamed the serpent for it. It is enough of a mistake to disobey God, but to compound it by not admitting that she was at fault was sheer folly. Adam too chose to eat of the forbidden fruit, and did the same as Eve. Instead of admitting his fault, he blamed Eve.

Today the issues of responsibility for one-s own actions is still of great concern to our society. It seems that individuals have the innate propensity to blame their misfortunes, not on their own choice, but on everything and everyone else. In this African folk-tale, a working man named Moses finally learns his lesson: Don’t Blame it on Adam.
```

### Performance text (classify this)

```text
There once was a freed slave named Moses who lived at the edge of the woods in a small hut.

Every morning Moses arose early and went deep into the forest to chop wood. Then he bundled the wood up and carried it to town to sell. Moses wouldn’t have enough money to buy breakfast until he sold some wood.

So every morning a hungry Moses walked up and down the streets calling, “Wood, wood. Who will buy some of my wood? It’s all the fault of Adam. Good wood for sale.”

One day as Moses was selling his wood. a rich man heard what he was saying. “Who is this person,” he asked, “and why does he say that it’s all the fault of Adam?” Because he wanted to know the answers to these questions, the rich man went up to Moses and asked him what he meant.

This is what Moses said: “I have heard that long ago Adam disobeyed God and ate the forbidden fruit. If he had not, we would all now be living in the Garden of Eden and I would never go hungry. That is why I say it is the fault of Adam.”

“I see,” said the rich man. “You work hard, yet you go hungry. It does not seem fair that you are suffering because of Adam’s mistake. I will help you.”

The rich man brought Moses to his house. Moses took a long, hot bath, after which the rich man gave him new clothes. Then the rich man took Moses down the hall and showed him a room in which he could stay.

The rich man said to Moses, “From now on you can call me brother. We will share everything. You can do anything you like except for one thing – you may not open the green door at the end of the hall. This is the one and only thing you may never do. Do you understand?”

Moses thanked the man and said, “What reason would I ever have to open the green door? I have food, clothes and shelter; I now have a brother who cares for me. What more could I want?”

And so Moses began a life of comfort. He never had to get up early or work hard. He had so much to eat that he was starting to get fat.

Moses had forgotten all about the green door until one day he happened to pass by it, and as he did, he remembered that it was the door he was never to open. However, he couldn’t help but wonder why he, the rich man’s brother, was not allowed to find out what was in the room behind the door. Moses sighed and walked on.

During the next few days, Moses seemed to be drawn to the green door. Several times a day he found himself outside the door, and each time he became more and more curious as to what was behind it. Sometimes, without realizing it, his hand actually moved toward the handle but he managed to stop himself each time.

One day the rich man said, “Brother, I have been called away to another town, and I will not be back until late today. I am entrusting my home to you. Please take care that nothing happens.”

After the rich man left Moses started thinking: “I am responsible for the house so surely I am responsible for the room behind the green door as well. I am going to find out what is hidden there.”

After checking that no one was looking, Moses put his ear against the door. He could not hear anything.

“I must know what is in there,” he said to himself. “ I will just open the door a crack and close it again. My brother will never know.” And so Moses opened the door a tiny bit. The room was dark, but after a while Moses could see that all that was in there were the old rags he used to wear and the wood he used to sell. Just then a mouse ran out the door.

“Oh no,” Moses cried. “My brother was hiding a mouse in the room and now it has escaped. I must catch it.” As Moses ran after the mouse, his shoes fell off. He tripped over the bottom of his long fancy pants and had to take them off. Still, he could not catch the mouse, and now he was very tired and out of breath.

Suddenly the rich man appeared. He had returned early. “What are you doing, Moses?” boomed the rich man. “Why are you running around my house naked?”

Moses threw himself at the rich man’s feet. “I’m sorry,” he sobbed. “I did not mean to let your mouse go.”

“What mouse?” asked the rich man. “I have no mouse.”

“The mouse in the room. When I opened the green door...”

“You opened the green door?”

“I did not mean to. It was wrong, but my feet kept taking me there, and I was curious, and I was...”

“Moses, I am very disappointed in you. Opening the green door was the one thing I told you not to do. You are as bad as Adam. You should have learned from Adam’s mistake.”

“I am sorry, my brother. It will never happen again. I promise. What do you wish me to do?”

The rich man’s anger had disappeared. Now he had tears in his eyes. “Go back to the room,” he said sadly, “ and take your rags and sticks. Return to the market and sell your wood.”

“Yes, sir” was all Moses could say. He returned to the market. Once again he shouted, “Good wood for sale. Who wants to buy good wood?”

Later Moses realized that no one else can make you happy or sad – that it is up to every person to determine his or her fate. Moses worked hard, and when things went well, he looked at what he had done to make good things happen. So, too, when things went badly, he looked at what he could change and what he could not. But he never mentioned Adam again.
```

---

## IC-2011: Don’t Fall in Love with Your Monkey

- Title: Don’t Fall in Love with Your Monkey
- Author (byline): Ari Handel
- Work: The Moth: 50 True Stories; Pgs 67-74
- Publisher: Hyperion
- Publication date as stated: Sept 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ARI
- Teaser before the introduction: Yes
- Spoken words (computed): 1466
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ari Handel
Book: The Moth: 50 True Stories; Pgs 67-74
ISBN: 978-1401311117
Publisher: Hyperion
Date (Month/Year): Sept 2013
```

### Introduction (context only: never use it for content warnings)

```text
The U.S. uses about 70,000 monkeys per year in studies of the brain. But controversy over animal research goes back a long way: In one corner, the world of biomedical research insists animals are crucial in developing new treatments and that their pain is properly overseen and mitigated. In the other, animal rights activists say lab animals suffer and die needlessly, and that humans have no moral or ethical right to use other species in this way.

Did you know that the United Nations considers more than 15 days of solitary confinement in humans to be torture? But research monkeys often get a lifetime of solitary confinement in a 2.5 square foot cage. To cope, some monkeys pace in circles. Others rock or bounce for hours. A few self-stimulate by sticking their fingers into their eyes. Except for the monkeys in one Harvard University study where researchers have sewed baby macaques’ eyelids shut to investigate how visual deprivation affects brain development.

In Don’t Fall in Love with Your Monkey by Ari Handel,
```

### Performance text (classify this)

```text
ARI: (Pg 67-74) Santiago is a wild animal. He does not want to be taken out of his cage. He keeps trying to hit my hand when I reach for him. He's big, and he's fast, and he's nimble. And I'm slow, in bulky clothing, and I'm starting to get hot. The monkeys in the room can sense that there's a conflict going on. They're starting to hoot and holler and screech.

Finally, I get one hand around Santiago's bicep, and [he] does exactly what you would do if some blue ogre reached into your house and grabbed you by the arm. He bites me as hard as he possibly can right here in the soft part of my hand. And it hurts. It really hurts. Every nerve in my hand is screaming, Drop the monkey. Instead, I reach my other hand in, grab his other bicep, and pull his arms behind his back. I stick him into his monkey chair and bring him down to the lab.

one researcher witnesses firsthand the psychological trauma of his research monkey, Santiago; and how easy it is to break the spirit of an animal in the name of research.

ARI: Down in the lab, Santiago is now the one who is frightened. He is quaking, he is shivering in his chair. So, I take a bottle, and I fill it with juice -- Hawaiian punch. I can see his little mouth around the edge of the bottle, the juice is dripping down his chin, and he is so cute. I see this look in his eyes, and it is joy.

When neurobiologists want to study the human mind, they look at the brains of monkeys. And I wanted to ask complex questions about mental functioning, and that meant that Santiago had to learn to play a video game. So I put him in a room facing a giant screen with a tube connected to his mouth that contained juice. I would go into the next room, where I had could control all these lights that would flash on that screen. Santiago's job was to look at the lights in the right order and with the right timing. If he did it right, he would get juice.

Now, this was not a very complicated game, but it was hard to teach Santiago how to play. I could not just tell him how. We had to invent our own language. I would watch Santiago's eye movements. If they were drifting slowly, that meant he was very frustrated, but if they were shimmering very fast, that meant he was excited. So I would watch his eyes and adjust the difficulty of the task accordingly, to cajole him forward or to calm him down. Slowly and surely, we learned together.

And when we did, Santiago got very, very happy. He was like a gambler who had just cracked the code of the blackjack tables, because now he could get juice, juice, juice, as much as he wanted, and he would sit in that room, and play that game all day long. And he would drink tremendous volumes of juice; and that made me happy too, because I could lower a probe into Santiago's brain.

I would listen to the activity of individual neurons while he performed this task. And what I found was that there were neurons in Santiago's brain that would become activated every time he made an eye movement. But the thing that was cool, so cool, so cool it was mind-blowing, was that these neurons did not get activated just when he made a movement; they got activated as soon as I gave him enough information that he could choose which eye movement to make. Listening to these neurons, I could predict in advance what he was going to do before he did it. I was eavesdropping on him while he was making a decision. I was reading my monkey's mind.

Santiago would get juice, and I would get data out of his brain, and we would do this for days and days and days. And then something happened. I went upstairs to get Santiago, and he tried to bite me. And when I brought him downstairs to the game room, he would not work, he just banged and banged and aborted every trial. Bang, bang, bang!

I couldn't figure it out at first, and then it slowly dawned on me that Santiago must have figured out sometime during the night that I was not bringing him down to that room so that he could play games, so that he could have fun. I was bringing him down there for my benefit and he didn't want to do it anymore. I had a monkey who was on strike.

So . . . I turned off the water in Santiago's cage. He's only going to get enough water, but anything extra, he's going to have to earn. Every night I would give Santiago his little supplement of water, and he would drink it right down and then he would have nothing. I [was] filled with guilt over what I was doing to him. But when I put him in that booth and he still wouldn't work, that guilt turned to anger. Whose fault was it really that Santiago was not drinking? Whose fault was it that I felt guilty every day? It was Santiago's fault. He was sitting with the juice tube in his mouth, there was a game he knew how to play, and he wasn't playing. And I would get so angry with him sometimes, I would pull on his little monkey ear and he would go "EEEH." And then the anger would turn back to guilt.

This went on day after day after day after day. And I got so frustrated that eventually, I walked into the room and said, "I know you're thirsty. I'll show you how thirsty you are." I poured myself a huge glass of Hawaiian punch. I made eye contact with Santiago. And I drank that juice down, taunting him. And he just looked at me.

I was engaged in a battle of will with an animal whose brain was the size of my fist, and I was losing. I was supposed to be training him, and he was training me to get guilty, get angry, cross the line, get guilty again. No more. I was going to be hard. I was going to be serious.

When it was treat time, I went up to the room, and every monkey got treats: cucumbers and apples and grapes. But not Santiago. For Santiago, it was cashews and peanuts and crackers. Eventually there came a day, after months and months of suffering, I walked up to the monkey cage and Santiago just did this [extends one arm]. And when I took his hand in my hand, Santiago did this [places his other arm behind his back]. And I grabbed him, and I brought him downstairs to work. And he started to play the game. But he didn't play with the exceptional enthusiasm he had played it with before. He wasn't like, Wow, this is the greatest thing. He played the game like a factory worker on an assembly line whish, whish, whish.

That should have been a good day for me. I was getting back to the science now. I would get my data, Santiago would get his juice. The suffering for us was over. But it wasn't a good day, because I had gotten to know Santiago. And now that Santiago wasn't there. I was sitting with just another monkey with a broken will. And I was the one who had broken it. The mystique of being a scientist -- of finding out all this stuff about the mind -- just didn't seem so magical anymore.

There were other monkeys. I didn't need to be told not to fall in love with them. Instinctively, I held myself aloof from them, and because of that, I had no mercy on them. And when they went on strike, when they got upset and it was time to break them, I broke them like that [snaps fingers]. But I also didn't go up to the monkey room anymore. I didn't want to see those monkeys while they were still a little bit wild. I didn't want to be reminded of what I was going to do to that part of them.

It took me eight years, but I got all the data I needed, piece by piece by piece. And I got my Ph.D. And then I quit. My thesis is 364 pages long and s filled with facts and data and graphs and theories. But the most significant page for me is the first one, which says simply: "Dedicated to the memory of Santiago."
```

---

## IC-2012: “Edmond Kirsch’s Presentation” from Origin

- Title: “Edmond Kirsch’s Presentation” from Origin
- Author (byline): Dan Brown
- Work: Origin
- Publisher: Anchor
- Publication date as stated: July 2018 (Reprint edition)
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1228
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dan Brown
Book: Origin
ISBN: 978-0525563709
Publisher: Anchor
Date (Month/Year): July 2018 (Reprint edition)
```

### Introduction (context only: never use it for content warnings)

```text
“Edmond Kirsch’s Presentation on The Origin of Life” from Origin by Dan Brown
```

### Performance text (classify this)

```text
(Pg 78-84) [Today] let us be like the early explorers -- those who left everything behind and set out across vast oceans . . . those who first glimpsed a land that had never before been seen . . . those who fell to their knees in awestruck realization that the world was far greater than their philosophies had dared imagine. Their long-held beliefs about their world disintegrated in the face of new discovery. This will be our mind-set.

Early humans had a relationship of wonder with their universe, especially with those phenomena they could not rationally understand. To solve these mysteries, they created a vast pantheon of gods and goddesses to explain anything that was beyond their understanding—thunder, tides, earthquakes, volcanoes, infertility, plagues, even love.

For the early Greeks, the ebb and flow of the ocean was attributed to the shifting moods of Poseidon. Infertility was caused by falling out of favor with the goddess Juno. Love was the result of being targeted by Eros. Epidemics were explained as a punishment sent by Apollo. When the ancients experienced gaps in their understanding of the world around them, they filled those gaps with God.

Countless gods filled countless gaps. And yet, over the centuries, scientific knowledge increased. As the gaps in our understanding of the natural world gradually disappeared, our pantheon of gods began to shrink. For example, when we learned that the tides were caused by lunar cycles, Poseidon was no longer necessary, and we banished him as a foolish myth of an unenlightened time.

We are an intellectually evolved and technologically skilled people. We do not believe in giant blacksmiths working under volcanoes or in gods that control the tides or seasons. We are nothing like our ancient ancestors. Or are we?

We consider ourselves modern rational individuals, and yet our species’ most widespread religion includes a whole host of magical claims—humans inexplicably rising from the dead, miraculous virgin births, vengeful gods that send plagues and floods, mystical promises of an afterlife in cloud swept heavens or fiery hells.

So just for a moment, let us imagine the reaction of humankind’s future historians and anthropologists. With the benefit of perspective, will they look back on our religious beliefs and categorize them as the mythologies of an unenlightened time? Will they look at our gods as we look at Zeus? Will they collect our sacred scriptures and banish them to that dusty bookshelf of history?

Yes, I believe all of that will happen. I believe future generations will ask themselves how a technologically advanced species like ours could possibly believe most of what our modern religions teach us. Future generations will look at our current traditions and conclude that we lived during an unenlightened time. As evidence, they will point to our beliefs that we were divinely created in a magical garden, or that our omnipotent Creator demands that women cover their heads, or that we risk burning our own bodies to honor our gods.

How can it be that the modern human mind is capable of precise logical analysis, and yet simultaneously permits us to accept religious beliefs that should crumble beneath even the slightest rational scrutiny? As it turns out the answer is quite simple.

The human brain. Why does it believe what it believes? If we could look into the human mind and read its operating system, we would find something like this.

DESPISE CHAOS.

CREATE ORDER.

For the human brain any answer is better than no answer. We feel enormous discomfort when faced with ‘insufficient data,’ and so our brains invent the data— offering us, at the very least, the illusion of order— creating myriad philosophies, mythologies, and religions to reassure us that there is indeed an order and structure to the unseen world.

Where do we come from? Where are we going? Tragically, on account of religious dogma, millions of people believe they already know the answers to these big questions. And because not every religion offers the same answers, entire cultures end up warring over whose answers are correct, and which version of God’s story is the One True Story.

Since the beginning of religious history, our species has been caught in a never-ending cross fire— atheists, Christians, Muslims, Jews, Hindus, the faithful of all religions—and the only thing that unites us all is our deep longing for peace. But faith, by its very definition, requires placing your trust in something that is unseeable and indefinable, accepting as fact something for which there exists no empirical evidence. And so, understandably, we all end up placing our faith in different things because there is no universal truth.

Science is the antithesis of faith. Science, by definition, is the attempt to find physical proof for that which is unknown or not yet defined, and to reject superstition and misperception in favor of observable facts. When science offers an answer, that answer is universal. Humans do not go to war over it; they rally around it.

(Pg 93) Consider this! It took early humans over a million years to progress from discovering fire to inventing the wheel. Then it took only a few thousand years to invent the printing press. Then it took only a couple hundred years to build a telescope. In the centuries that followed, in ever-shortening spans, we bounded from the steam engine, to gas-powered automobiles, to the Space Shuttle! And then, it took only two decades for us to start modifying our own DNA!

(Pg 372-375) - New species of technology are being born daily, evolving at a blinding rate, and each new technology becomes a tool to create other new technologies. The invention of the computer has helped us build astonishing new tools, from smartphones to spaceships to robotic surgeons. We are witnessing a burst of innovation that is happening faster than our minds can comprehend. We are now starting to embed computer chips directly into our brains, inject our blood with tiny cholesterol-eating nanobots that live in us forever, build synthetic limbs that are controlled by our minds, use genetic editing tools like CRISPR to modify our genome, and, quite literally, engineer an enhanced version of ourselves.

Human beings are evolving into something different. We are becoming a hybrid species—a fusion of biology and technology. The same tools that today live outside our bodies—smartphones, hearing aids, reading glasses, most pharmaceuticals—in fifty years will be incorporated into our bodies to such an extent that we will no longer be able to consider ourselves Homo sapiens.

We are now perched on a strange cusp of history -- a time when the world feels like it’s been turned upside down, and nothing is quite as we imagined. But uncertainty is always a precursor to sweeping change; transformation is always preceded by upheaval and fear. I urge you to place your faith in the human capacity for creativity and love, because these two forces, when combined, possess the power to illuminate any darkness.

As we move into an undefined tomorrow, we will transform ourselves into something greater than we can yet imagine, with powers beyond our wildest dreams. And as we do, may we never forget the wisdom of Churchill, who warned us: ‘The price of greatness … is responsibility.’

May our philosophies keep pace with our technologies. May our compassion keep pace with our powers. And may love, not fear, be the engine of change.
```

---

## IC-2013: Elevator ER

- Title: Elevator ER
- Author (byline): Jon Levine
- Work: The Moth, Pg 103-111
- Publisher: Hachette Books
- Publication date as stated: Sept 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1245
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jon Levine
Book: The Moth, Pg 103-111
ISBN: 978-1401311117
Publisher: Hachette Books
Date (Month/Year): Sept 2013
```

### Introduction (context only: never use it for content warnings)

```text
Jon Levine was lost . . . floating through life. No goals, no purpose, no ambition. But all that changed one fateful night in the most unexpected way possible.

Elevator ER by Jon Levine
```

### Performance text (classify this)

```text
When I was young, I was a bright, happy, enthusiastic kid. Years later I had become and angry, sullen, disaffected high school dropout.

If I could’ve signed a form to officially drop out of American society or the human race, that would've been next. So when I applied for a job working the night shift in the OR, it was not out of a great desire to help my fellow man. I was only doing it because the job paid really well -- $9 an hour.

The fact that the hospital hired me at that time in my life should be sufficient to scare all of you into taking excellent care of yourselves from now on. But hire me they did, and my actual job title was OR nursing assistant, night shift.

The most fundamental part of the job was transporting patients to surgery, which I was trained to do during the day shift when the patients are in stable condition, usually awake but mildly sedated, and it's pretty simple. On the night shift nothing is scheduled. Patients are usually kinda bloody. Sometimes they're highly agitated and need to be restrained. But for the most part they were completely unconscious. I didn't see them as human beings at a time of great need so much as packages that needed to be delivered to a specific room as efficiently as possible.

You know:

• "Burst appendix to OR 22,"

• "Multiple stab wounds to OR 27,"

• "Guy who shot his face off to OR 33."

All manner of human suffering, but to me, it was all the same.

So, it's three in the morning, and there's a call from the ICU. They have a patient. So I go up to get him, and the nurses are disconnecting him from his respirator and his EKG and attaching a portable heart monitor to the rolling ICU bed and an air bag to his breathing tube, which I'm going to have to squeeze to breathe for him during the trip. This means that someone's gonna have to come with me, because you can't really steer an ICU bed and squeeze an air bag at the same time.

Unfortunately, the nurses in the ICU couldn't spare anyone except a young woman named Melissa, a nursing student. She was very nervous because she'd never been anywhere else in the hospital before and had never really been given much responsibility. But the nurses assured us that, despite appearances, Mr. Williams was pretty much okay and this would be totally routine.

So I'm pushing from the back and squeezing the air bag with my free hand, and I have Melissa steering from the front as I direct her on the shortest route to the OR.

So this old, crappy elevator arrives. We get in. The doors close. I push the button. And nothing happens. And then the lights go out. We start to move. But it's not right, and we're moving too fast, and the elevator's not making its normal sound. And my stomach is in my throat, and we're falling, WE'RE FALLING!

And if I had had time for a thought process, it probably would've been like, I'm not ready to die. I didn't sign up for this. But before any of that can take place, the elevator's emergency brake kicks in and slams us to a stop so violently that I'm thrown to my knees and Mr. Williams is bouncing in his bed.

So now we're stopped in this tiny, dark box, and there's three sounds I can hear: the elevator's emergency signal buzzing, Melissa screaming, and Mr. Williams's heart monitor indicating that, like our elevator, his heart has stopped.

No, no, no, no, NO! But denial and anger quickly give way to, in this case, bargaining: Well, Melissa's got some actual medical education, so she should be in charge.

But then reality sets in. Melissa's cowering in the corner, wondering if we're all gonna die. But if we don't do something right away, ONE of us is DEFINITELY gonna die.

So I then hit acceptance and admitted to myself that I had to get in the game here. Fortunately, the hospital had trained me to do CPR when they hired me. So I had Melissa stand up, and by the dim lights of the LEDs on the heart monitor, I said, "Okay, you do the air bagging. I'm going to do chest compressions."

I moved around to the side, but Mr. Williams was a big guy, and I couldn't get good leverage. So I did something I had seen one of the emergency ward doctors do one time. I climbed up, sort of mounting Mr. Williams, and did chest compressions from above. And it seemed to work.

I have no idea how long we were like that in the dark, but it felt like hours, until the lights flickered and came back on, and the buzzing emergency thing stopped. We finally arrived at the third-floor OR and the doors opened. And Melissa was so eager to get us out of there, she started pushing us forward. And that's when something bad happened.

The wheels on the front of the ICU bed swiveled around ninety degrees, right as they were situated over the gap be-tween the elevator and the floor and slid down into the gap like slices of bread going into a toaster.

And then, of course, the elevator doors started slamming on us over and over again. I was still doing chest com-pressions, and we both started screaming for help. Finally, someone showed up, a wonderful older gentleman named Mr. Selwin, who was one of the night cleaning crew.

He comes running in, and in his thick island accent says, "What's all the commotion? Oh my God! Keep doing what you're doing. I'll go get more help." And he runs out.

Within a few moments, he comes back with "reinforcements" and finally, with a horrible metal scraping sound, they wrench us free. And suddenly all the panic and confusion recede, and we are in motion. We're off to OR 29!

The double doors open, and we're whipping around corners and everything's very effortless, and we're flying now - Melissa is running, trying to keep up, while still doing the air bagging.

And of course, I'm still on top of Mr. Williams, still pumping away at his chest, and there's a breeze in my face from our newfound velocity. And I have to say, it was absolutely exhilarating, to the point where I had to stifle the urge to laugh out loud.

So I screw my face up into a mask of seriousness because it would be a tad unseemly to appear to be enjoying riding a patient down the hall. And we get to OR 29, and the entire surgical team fly into action and seamlessly take over for everybody. They save him, and he lives. Not only did he live through the night, but he recovered and left the hospital!

That exhilarating feeling didn't go away. It seems kind of obvious in retrospect, but at the time I was so unaccustomed to feeling anything positive, that it took me a really long time to recognize that I enjoyed what I did, and I enjoyed caring about it. I enjoyed caring about Mr. Williams and myself.

Six months later, I found myself mentioning the incident in a personal essay that was part of an application to get back into college.
```

---

## IC-2014: The Elves and the Shoemaker

- Title: The Elves and the Shoemaker
- Author (byline): AJ Jacobs
- Work: Fractured Fairy Tales
- Publisher: Bantam Books
- Publication date as stated: Jan 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 838
- Already set (do not supply): none

### Source block (context only)

```text
Author: AJ Jacobs
Book: Fractured Fairy Tales
ISBN: 978-0553099805
Publisher: Bantam Books
Date (Month/Year): Jan 1999
```

### Introduction (context only: never use it for content warnings)

```text
Things aren't going well in the Herman’s shop. The old shoemaker is hungry and cold and down to the final piece of leather to make one last pair of shoes. But help comes in a very unexpected way...This is Herman’s story.

PAINTER’S VOICE: Whaa Whaa Whaa . . . . Who wants to hear that tired old tale? The guy goes to sleep the elves make the shoes, he had no vision, no creativity . . . . Heck even I could do better . . . and I wouldn’t need the help of any old elves either! Why don’t you tell MY story?

The Elves and the Shoemaker (who used to be a painter) by AJ Jacobs.
```

### Performance text (classify this)

```text
Once upon a time, there was a painter. He was a good painter and he made a modest living for his wife and himself. All was well, except for one thing. The painter didn't want to be a painter. He wanted to be a shoemaker.

"I'm drudging my way through life!" he whined to his wife one morning. "Every day, from nine to five, it's canvas and landscapes and easels and, oh, it's so dull. I want to do something creative!"

"But I always thought painting was creative," said his wife. "You deal with light and shade and perspective and such."

"You call that creative?" The painter shook his head sadly. "I'll tell you creative. Making shoes. That's creative-Something for the feet. Something that lives. Something to last through eternity. Shoes that sing!"

But just then, the clock struck nine. Time for work. The painter shuffled off to the nearest still life and, with a sigh, began dabbing and swirling the canvas. "I wish I were a shoemaker. I wish I were a shoemaker. I wish I were a shoemaker." POOF! the third time he said the magic phrase, an elf appeared-the patron elf of shoemakers.

"So you want to be like Herman Cappachino,"

said the elf.

"Who are you and who is Herman Cappachino?"

"No need to explain who I am," said the elf, "But Herman Cappachino-he was just the greatest little shoemaker to ever live. When Napoleon tromped through Russia, whose shoes was he wearing? When Hannibal crossed the Alps? And when Dorothy, that girl from Iowa or something, clicked her heels? Whose shoes did they have on? Herman Cappachino, that's who."

"Oooh," said the painter. "How can I be a famous shoemaker like Herman Cappachino?"

"It ain't easy," replied the elf. "You gotta suffer. You gotta spend time on the Left Bank of Paris. You gotta study. You gotta wear berets and develop poor hygiene habits."

That night, the painter told his wife of his plans. She shook her head. "Great shoemakers are not made," she said. "They are born. Why don't you forget it and go back to something sensible like your painting."

"No!" shouted the painter, stamping his feet and clenching his fists. "Anyone can paint. I want to sit in cafes, discuss shoelace exhibitions, make loafers in a garret. And above all, suffer!"

So that night, the painter left for Paris. He en-tered the famous shoe school, Beau Chaussure, and under the tutelage of the famous, if unwashed, pro-fessor, Jean-Claude Louis-Mark-Paul, he learned all there was to know about shoemaking. He took The History of the Heel in Eighteenth-Century Brazil. He read all the books on tongue theory and practice. He wrote an essay called "What Those Plastic Things on the End of Shoelaces Are Really Called." But alas, he never learned how to make a shoe that sang.

"If only I could make a shoe that sings of spring, of love. How can I make a shoe with a soul as well as a sole?"

Just then, as he stood on Paris's main boulevard, pulling the rest of his hair out, he heard the most beautiful music. He followed the lovely sound. And there, on the feet of a goatee-wearing man, was a singing shoe. The shoe sang its song, then said, "Thank you. Thank you very much. You've been a great audience. And it's for you, the audience, that I sing. Your appreciation is what- "

"Now, that is truly a shoe with a soul!" inter-rupted the painter. "I must have that shoe!" He reached down and started pulling it off.

"What are you doing'?" the man demanded.

"I just wanted to know where you bought your shoes."

"I got them in Elvesville!"

Elvesville! Why, that was the painter's hometown. He had been suffering around Europe, when he could be home, making shoes that sing. So the painter returned to Elvesville and found that everyone in town was wearing the same exquisite singing shoes.

"Where did you get those exquisite singing shoes?" he asked a passerby.

"Twenty-three eleven South Budlong. You turn left, go about three. , ,"

"You don't have to tell me!" exclaimed the painter. 'That's my house!" And sure enough, when the painter got home, he found the walls of his cottage lined with exquisite shoes, all of them singing merrily away. And who did he find sitting behind the cobbler's bench, but his wife!

"Why didn't you tell me you made exquisite singing shoes?" he asked.

"You never asked me."

And so from that day on, the painter went back to his easel every day from nine to five. Eventually, his paintings started selling like hotcakes and he became a very famous painter indeed. And his paintings hung in all the famous museums in Europe. But he never did become a shoemaker and had to be content with just being a wealthy man.

Which just goes to prove. Not everybody can be Herman Cappachino. Whatever that means.
```

---

## IC-2015: Encouraging Kelly

- Title: Encouraging Kelly
- Author (byline): Seema Renee Gertsen
- Work: Chicken Soup for the Teacher's Soul
- Publisher: Health Communications, Inc.
- Publication date as stated: April 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1165
- Already set (do not supply): none

### Source block (context only)

```text
Author: Seema Renee Gertsen
Book: Chicken Soup for the Teacher's Soul
ISBN: 978-1558749788
Publisher: Health Communications, Inc.
Date (Month/Year): April 2002
```

### Introduction (context only: never use it for content warnings)

```text
What makes some children special? Perhaps they have a physical or mental handicap; But does that condition warrant that these children be treated differently than other children? The answer is really quite simple. There should be no difference in the way we treat or acknowledge them. Special children laugh and cry and savor and hurt just like other children.... In Encouraging Kelly, a first year teacher learns this very valuable lesson in the process of Encouraging Kelly by Seema Renee Gertsen.
```

### Performance text (classify this)

```text
It was my very first teaching job, and I was anxious to make an excellent first impression. I had been hired to lead a vibrant group of four-year-olds. As the parents escorted children into the room, I attempted to deal with crying kids, teary-eyed moms and tense dads. Finally, I managed to seat the kids on the carpet and we were ready to start our "morning circle time."

We were in the middle of a rousing rendition of "Old McDonald" when the door opened and a mysterious woman entered the room. She stood next to the door quietly observing the children and me. My voice and smile never faltered, but quite frankly I was very nervous. Who is this woman? Why is she here? What exactly is she observing? When I looked up again she was gone.

The day went relatively smoothly, but by the time the last child was picked up, I was physically and emotionally drained. I longed for a nonfat latte, some Chopin and a bubble bath. Then my director came in and asked to meet with me before I left for the day.

My heart raced. Did this have anything to do with the woman who had observed my class? Did I choose the wrong songs? Was the circle time too long? Too short? By the time I reached the office, I was an emotional wreck. I sat perched on the edge of my seat and waited for the axe to fall. My director told me the woman who had visited my room earlier was a potential parent to the school and was concerned about how her daughter would function in a regular classroom. Her little girl was born with a birth defect that required she wear leg braces from the knees down. The child was ambulatory but walked very slowly with a lopsided gait. She would need to be carried out to the yard and back to the classroom. Her balance was poor, and she had a tendency to topple over if she was jostled, even slightly. We would need to remind the other children to be careful when walking near her so they wouldn't accidentally cause her to fall.

The director asked me how I felt about her becoming a member of my group. I was speechless. Here I was wondering if I could possibly survive a school year with fifteen of the liveliest four-year-olds in North America, and now I was being asked to take on a child with special needs? I replied that I would accept the child on a trial basis.

That night I couldn't fall asleep. I tossed and turned until morning, then drove to work with my stomach in knots. We were all gathered on the carpet for our morning circle when the door opened and the woman walked in carrying her daughter. She introduced herself as Kelly's mommy and she gingerly sat her daughter down on the edge of the carpet. Most of the children knew Kelly from synagogue and greeted her with warm, affectionate hugs. I looked at Kelly and she looked at me. "Welcome to our room, Kelly. We are so excited that you will be a member of our group."

The first day went really well; Kelly only fell over twice. After several days of carrying her to and from the yard, I thought, Why not encourage her to walk down the hallway a little by herself? I asked Kelly if she would like to try it, and she became very excited. The next day I sent the class out to the yard with my two assistants, and Kelly began her first journey down the hallway. She walked all the way to the next classroom, a total of ten feet. We were both thrilled! But my assistants were aghast that I was encouraging this poor child to walk. They pleaded with me to carry her outside and seat her on the bench so she could watch the other children run and play. "It would be so much easier," they murmured. But Kelly was persistent and eager to give it her best shot.

And so we began the strenuous task of walking daily down the hall. I winced when Kelly teetered precariously too far to the right, but she just giggled and told me not to worry, she was perfectly fine. I began to cherish our quiet moments alone in the hallway, my arms outstretched to help her regain her balance. Kelly always grinned and told me she had never felt better.

Each day Kelly and I continued our slow walk down the corridor. I charted her progress with little pencil marks on the wall. Every few days the pencil marks got farther and farther apart. Kelly's classmates started to notice and began cheering for her as she plodded along. After several weeks, Kelly made it all the way to the yard! She positively glowed as the children congratulated her with gentle pats on the back and warm hugs. My assistants were astonished and prepared a special snack in honor of Kelly's tremendous accomplishment. Weeks passed and Kelly continued to walk out to the yard every single day. We rarely carried her as she became more independent.

One week in mid-December, Kelly was absent for several days. When I called her home I was told she was in Manhattan getting her annual checkup with her doctors. On Monday morning, when her mom brought her back to school, she inquired if I had been doing anything differently with Kelly. I wasn't quite sure what she meant. Then came the dreaded question: "Have you been forcing Kelly to walk?"

I was dumbfounded. Maybe I shouldn't have encouraged Kelly to walk to the yard every day. Maybe I had caused permanent damage to her weakened legs. Maybe Kelly would need to be in a wheelchair for the rest of her life.

I very softly told Kelly's mom that I had encouraged her to walk outside to the yard by herself. I explained that she seemed to enjoy walking independently. The mother gently lifted Kelly's dress to show me that Kelly's knee braces had been replaced with ankle braces.

"Her legs have gotten more exercise in the past few months than in the past four years of her life." She looked at me with tears in her eyes. "I don't know how to thank you for everything you have done for my daughter."

I hugged her. "Having Kelly as a member of my group has been a privilege."

Seventeen years later, I still think back to the first time Kelly made it down the long hallway. Whenever I have a bad day teaching and life seems too overwhelming, I think of Kelly and her exuberant smile as she painstakingly walked down that hallway. She taught me that no obstacle in life is too big to overcome. You just need to keep working at it-one step at a time.
```

---

## IC-2016: Encyclopedia Brown and the Case of the Barefoot Thieves

- Title: Encyclopedia Brown and the Case of the Barefoot Thieves
- Author (byline): Donald J. Sobol
- Work: Encyclopedia Brown Takes the Case
- Publisher: Penguin
- Publication date as stated: 2008
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, TYRONE, ENCYCLOPEDIA, MR. BROWN
- Teaser before the introduction: Yes
- Spoken words (computed): 1121
- Already set (do not supply): none

### Source block (context only)

```text
Author: Donald J. Sobol
Book: Encyclopedia Brown Takes the Case
ISBN: 978-0142410851
Publisher: Penguin
Date (Month/Year): 2008
```

### Introduction (context only: never use it for content warnings)

```text
Encyclopedia Brown and the Case of the Barefoot Thieves by Donald J. Sobol
```

### Performance text (classify this)

```text
Police officers across America were asking the same question. Why did everyone who broke the law in Idaville get caught? Idaville looked like many seaside towns its size. It had delicatessens, three movie theatres, and four banks. It had churches, a synagogue, and lovely white beaches. And it had a certain Red Brick house on Rover Avenue. In the house lived Idaville’s secret weapon against law breakers—ten year old Encyclopedia Brown. Mr. Brown was the chief of the Idaville police force. He was proud of his men. But he was not too proud to get them help. Whenever Chief Brown came up against a case that no on the force could solve, he knew what to do. He went home and ate dinner. Before the meal was over, Encyclopedia had solved the case for him. Chief Brown wanted to tell the world about his only child—to announce over satellite television “my son is the greatest detective who ever shot a water pistol!” But what good would it do? Who would believe that the mastermind behind Idaville’s spotless police record was only a fifth-grader? Encyclopedia never let slip a work about the help he gave his father. He didn’t want to seem different from other boys his age. But there was nothing he could do about his nickname. Only his parents and teachers called him by his real name, Leroy. Everyone else called him Encyclopedia. An Encyclopedia is a book or set of books filled with facts from A to Z—just like Encyclopedia’s head. He had read more books that anyone in Idaville, and he never forgot what he read. All this knowledge gave him the ability to start his very own, Brown Detective Agency.

NARRATOR: Tyrone Taylor knew how to treat the fair sex. He was the only boy in Idaville who got up to give a girl his seat- even when they were the only two passengers on the bus. The other fifth grade boys called him Sir Galahad. Monday afternoon Tyrone came into the Brown Detective Agency. He looked sick as a horse.

TYRONE: (sadly) Don’t call me Sir Galahad . . . call me Sir Had-a-Gal.

ENCYCLOPEDIA: Who was it this time?

TYRONE: Betty Holden. Just when I figured I had a chance with her, what happens? She goes out with Stingy Stenson!

ENCYCLOPEDIA: Don’t worry. Stingy is so tight that if he blinks his eyes, his knuckles crack. When he dates a girl, the money flows like glue

TYRONE: That’s what I thought. But last night I saw them together in Mr. O’Hara’s drugstore. Stingy bought her the Idaville Special with three scoops of ice cream!

ENCYCLOPEDIA: Wow! That costs twenty cents extra!

TYRONE: I want to hire you. (slams a quarter on the gasoline can beside Encyclopedia). Find out where Stingy stole the money he’s spending.

ENCYCLOPEDIA: Just a minute. You can’t go around accusing him of stealing --

TYRONE: (snapping) What was he doing outside the Medical Building yesterday morning? It was Sunday. The building was closed. And you should have seen his crazy walk.

ENCYCLOPEDIA: (scratching his head) You better show me.

NARRATOR: The two boys biked to the Medical building. It was after five o’clock when they arrived. The doctors had all gone home. The parking lot was empty.

TYRONE: Sunday was a hot day. So I sat under that shade tree while I thought about Betty. Suddenly I saw Stingy and his big brother Pete. They were walking in the parking lot, one behind the other. Crazy!

ENCYCLOPEDIA: Crazy?

TYRONE: They walked as if they couldn’t keep their balance. Then they jumped into a red truck that had “Mac’s Service Station” written on the door. They drove away, zoom!

ENCYCLOPEDIA: Sit under the same tree. I’ll do what they did

NARRATOR: He went down to the parking lot, which was enclosed by a seven-foot stonewall. He walked across the blacktop surface till he could see Tyrone over the wall.

TYRONE: Stingy and Pete were farther back. I can see only your head above the wall. I saw them down to the waist. (Encyclopedia moved back a few steps.) Stop! That’s where they were

NARRATOR: Encyclopedia had halted on a long, narrow white line. Branching out on either side of it were short white lines to mark spaces for cars to park.

ENCYCLOPEDIA: Stingy and Pete were walking a narrow white line you can’t see from there! They were having fun keeping their balance

TYRONE: Fun, nothing. They were celebrating. They probably just robbed some doctor’s office.

NARRATOR: Tyrone refused to believe anything but the worst about Stingy. He made Encyclopedia promise to ask his father if the medical building had been robbed yesterday. At dinner, Encyclopedia put the question to his father.

MR. BROWN: Why yes, Officer Clancy handled the case. I learned about it this morning. Thieves took about two hundred dollars altogether from the petty-cash boxes in several offices.

ENCYCLOPEDIA: Isn’t the medical building locked on Sunday?

MR. BROWN: The front door lock was broken Saturday. A watchman was hired till it could be repaired today

ENCYCLOPEDIA: Where was the watchman during the robbery?

MR. BROWN: He was drinking at the water fountain when he glimpsed two pairs of bare feet disappearing us the stairs. He chased them. As he turned a corner, he was struck and knocked out. He awoke to see Mac’s red service truck leave the parking lot. The watchman telephoned Mac immediately. Sundays, the truck is driven by Pete Stetson. Sometimes he takes his younger brother, the one everyone calls Stingy, along on service calls. When they returned to the station, both boys had on shoes

ENCYCLOPEDIA: What were the Stetson boys doing at the parking lot?

MR. BROWN: Pete says he was looking for a key, which he thought he dropped Saturday after visiting Dr. Marshall. He did see the doctor. We checked on that. No doubt the thieves removed their shoes in order to walk more quietly. Pete and Stingy may have robbed the offices. But we can’t shake their alibi.

ENCYCLOPEDIA: You mean, you need a clue to prove they had their shoes off when they entered the building?

MR. BROWN: One clue will do, but we don’t even have one!

ENCYCLOPEDIA: (grinning) I have!

NARRATOR: Pete and Stingy had taken off their shoes and socks in the truck in order to walk quietly. They had entered and left the building by walking along the white stripes of the parking lot. As they left, Tyrone Taylor had sat down under the tree. The brothers did not see him. But he saw them, from the waist up, walking back to the truck. Encyclopedia realized the brothers had not walked along the sidewalk just for fun. It was a hot day, remember? The blacktop burned their feet. So they had walked along the white strip—which was cooler. Faced with proof revealed by Tyrone’s sharp eyes and Encyclopedia’s sharp brain, the Stetson brothers confessed. Thanks to Encyclopedia, the money was returned and Tyrone—I mean, Sir Galahad, got the girl.
```

---

## IC-2017: Enemy Pie

- Title: Enemy Pie
- Author (byline): Derek Munson
- Work: Not specified
- Publisher: Chronicle Books
- Publication date as stated: Oct 2000
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, DAD, JEREMY, JEREMY’S MOM
- Teaser before the introduction: Yes
- Spoken words (computed): 1454
- Already set (do not supply): none

### Source block (context only)

```text
Author: Derek Munson
ISBN: 978-0811827782
Publisher: Chronicle Books
Date (Month/Year): Oct 2000
```

### Introduction (context only: never use it for content warnings)

```text
Enemy Pie by Derek Munson
```

### Performance text (classify this)

```text
NARRATOR: It should have been a perfect summer. My dad helped me build a treehouse in our backyard. My sister was at camp for three whole weeks. And I was on the best baseball team in town. It should have been a perfect summer. But it wasn’t.

It was all good until Jeremy Ross moved into the neighborhood, right next door to my best friend Stanley. I did not like Jeremy Ross. He laughed at me when he struck me out in a baseball game. He had a party on his trampoline, and I wasn’t even invited. But my best friend Stanley was.

Jeremy Ross was the one and only person on my enemy list. I never even had an enemy list until he moved into the neighborhood. But as soon as he came along, I needed one. I hung it up in my tree house, where Jeremy Ross was not allowed to go.

Dad understood stuff like enemies. He told me that when he was my age, he had enemies, too. But he knew of a way to get rid of them. I asked him to tell me how.

DAD: Tell you how? I’ll show you how!

NARRATOR: He pulled a really old recipe book off the kitchen shelf. Inside, there was a worn-out scrap of paper with faded writing.

DAD: (holding up the recipe and squinting) Enemy Pie!

NARRATOR: You may be wondering what exactly is in Enemy Pie. I was wondering, too. But Dad said the recipe was so secret, he couldn’t even tell me. I decided it must be magic. I begged him to tell me something -- anything.

DAD: I will tell you this. Enemy Pie is the fastest known way to get rid of enemies.

NARRATOR: Now, of course, this got my mind working. What kinds of things -- disgusting things -- would I put into a pie for an enemy? I brought Dad some weeds from the garden, but he just shook his head. I brought him earthworms and rocks, but he didn’t think he’d need those. I gave him the gum I’d been chewing on all morning. He gave it right back to me.

I went out to play, alone. I shot baskets until the ball got stuck on the roof. I threw a boomerang that never came back to me. And all the while, I listened to the sounds of my dad chopping and stirring and blending the ingredients of Enemy Pie. This could be a great summer after all.

Enemy Pie was going to be awful. I tried to imagine how horrible it must smell, or worse yet, what it would look like. But when I was in the backyard, looking for ladybugs, I smelled something really, really, really good. And as far as I could tell, it was coming from our kitchen. I was a bit confused.

I went in to ask Dad what was wrong. Enemy Pie shouldn’t smell this good. But Dad was smart.

DAD: If Enemy Pie smelled bad, your enemy would never eat it.

NARRATOR: I could tell he’d made Enemy Pie before.

The buzzer rang, and Dad put on the oven mitts and pull the pie out of the oven. It looked like plain, old pie. It looked good enough to eat!

But still. I wasn’t really sure how this Enemy Pie worked. What exactly did it do to enemies? Maybe it made their hair fall out, or their breath stinky. Maybe it made bullies cry. I asked Dad but he was no help. He wouldn’t tell me a thing. But while the pie cooled, he filled me in on my job.

DAD: (quietly) There is one part of Enemy Pie that I can’t do. In order for it to work, you need to spend a day with your enemy. Even worse, you have to be nice to him. It’s not easy. But that’s the only way that Enemy Pie can work. Are you sure you want to go through with this?

NARRATOR: Of course, I was. It sounded horrible. It was scary. But it was worth a try. All I had to do was spend one day with Jeremy Ross, then he’d be out of my hair for the rest of my life. I rode my bike to his house and knocked on the door. When Jeremy opened the door, he seemed surprised. He stood on the other side of the screen door and looked at me, waiting for me to say something. I was nervous. (to Jeremy) Can you play?

JEREMY: (looking confused) I’ll go ask my mom.

NARRATOR: He came back with his shoes in his hand. His mom walked around the corner to say hello.

JEREMY’S MOM: (smiling) You boys stay out of trouble.

NARRATOR: We rode bikes for a while and played on the trampoline. Then we made some water balloons and threw them at the neighbor girls, but we missed. Jeremy’s mom made us lunch.

After lunch we went over to my house. It was strange, but I was kind of having fun with my enemy. He almost seemed nice. But of course, I couldn’t tell Dad that, since he had worked so hard to make this Enemy Pie.

Jeremy Ross liked my basketball hoop. He said he wished he had a basketball hoop, but they didn’t have room for one. I let him win a game, just to be nice.

Jeremy Ross knew how to throw a boomerang. He threw it and it came right back to him. I threw it and it went over my house and into the backyard. When we climbed over the fence to find it, the first thing Jeremy noticed was my tree house.

My treehouse was my treehouse. I was the boss. If my sister wanted in, I didn’t have to let her. If my dad wanted in, I didn’t have to let him. And if Jeremy wanted in. . .

JEREMY: Can we go in it?

NARRATOR: I knew he was going to ask me that! But he was the top person, the ONLY person, on my enemy list. And enemies aren’t allowed in my tree house. But, he did teach me to throw a boomerang. And he did have me over for lunch. And he did let me play on his trampoline. He wasn’t being a very good enemy. (to Jeremy) Okay, but hold on.

I climbed up ahead of him and tore the enemy list off the wall. I had a checkerboard and some cards in the tree house, and we played games until my dad called us down for dinner. We pretended we didn’t hear him, and when he came out to get us, we tried to hide from him. But somehow, he found us.

Dad made us macaroni and cheese for dinner -- my favorite. It was Jeremy’s favorite too! Maybe Jeremy Ross wasn’t so bad after all. I was beginning to think that maybe we should just forget about Enemy Pie.

But sure enough, after dinner, Dad brought out the pie. I watched as he cut the pie into eight thick slices. (to Dad) Dad, it sure is nice having a new friend in the neighborhood. (to audience) I was trying to get his attention and trying to tell him that Jeremy Ross was no longer my enemy. But Dad only smiled and nodded. I think he thought I was just pretending.

Dad dished up three plates, side by side, with big pieces of pie and giant scoops of ice cream. He passed one to me and one to Jeremy.

JEREMY: Wow! My dad never makes pies like this!

NARRATOR: It was at this point that I panicked. I didn’t want Jeremy to eat Enemy Pie! He was my friend! I couldn’t let him eat it! (to Jeremy) Jeremy, don’t eat it! It’s bad pie! I think it’s poisonous or something! (mime Jeremy’s reaction as the next lines are spoken) Jeremy’s fork stopped before reaching his mouth. He crumpled his eyebrows and looked at me funny. I felt relieved. I had saved his life. I was a hero.

JEREMY: If it’s so bad, then why has your dad already eaten half of it?

NARRATOR: I turned to look at my dad. Sure enough, he was eating Enemy Pie! (mime Dad happily enjoying the pie)

DAD: (with his mouth full) Good stuff!

NARRATOR: And that was all he said. I sat there watching them eat Enemy Pie for a few seconds. Dad was laughing. Jeremy was happily eating. And neither of them was losing any hair! It seemed safe enough, so I took a tiny taste. Enemy Pie was delicious!

After dessert, Jeremy rode his bike home but not before inviting me over to play on his trampoline in the morning. He said he’d teach me how to flip.

As for Enemy Pie, I still don’t know how to make it. I still wonder if enemies really do hate it or if their hair falls out or their breath turns bad. But I don’t know if I’ll ever get an answer, because I just lost my best enemy.
```

---

## IC-2018: Exchange

- Title: Exchange
- Author (byline): Ray Bradbury
- Work: In the Stacks
- Publisher: Overlook
- Publication date as stated: Feb 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1671
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ray Bradbury
Book: In the Stacks
ISBN: 978-1585672592
Publisher: Overlook
Date (Month/Year): Feb 2002
```

### Introduction (context only: never use it for content warnings)

```text
There is only one form of magic in the world: reading. Think about it for a moment. Reading can transport you to places you've never been and never will go. It can be your best friend and your escape from realities that are too difficult to manage. If there is any gift I could pass on to my own kids, it would be this one. Teaching them that reading is magic– true magic–and that libraries are the sanctuaries where you learn that magic. They are places where newcomers can be introduced to the magic, and old-timers can revel in it, one page at a time. Here, let me show you . . Exchange by Ray Bradbury.
```

### Performance text (classify this)

```text
There were too many cards in the file, too many books on the shelves, too many children laughing in the children's room, too many newspapers to fold and stash on the racks. . .

Finally the last book was stamped, the last child fed through the great brass doors, and with immense weariness, Miss Adams moved back through a silence of forty years of books and being keeper of the books, and stood for a long moment by the main desk. Taking up her rubber stamp, she probed the files, weeding out errors, her fingers whispering between Dante and Darwin.

A moment later she heard the rapping on the front-door glass and saw a man's shadow outside, wanting in. Sighing, Miss Adams opened the door, saw a young man in uniform, and said, "It's late. We're closed." She glanced at his insignia and added, "Captain."

"Hold on!" said the captain. "Remember me?" And repeated it, as she hesitated. "Remember?"

She studied his face, trying to bring light out of shadow. "Yes, I think I do," she said at last. "You once borrowed books here. Many years ago.”

"May I come in?"

She hesitated, [then] led the way up the steps into the immense twilight of books. The young officer looked around and let his breath out slowly, then reached to take a book and hold it to his nose, inhaling, then almost laughing.

"Don't mind me, Miss Adams. You ever smell new books? Binding, pages, print. Like fresh bread when you're hungry." His eyes were troubled and he fretted his cap, turning it in his long, slender fingers.

She said gently, "Is anything wrong? Anything I can help you with?"

He glanced out the window at the dark town, with just a few lights in the windows of the small houses across the way. "I was surprised. I don't know what I expected. Pretty dumb to expect that when I went away, everyone froze in place waiting for me to come home. That when I stepped off the train, all my old pals would unfreeze, run down, meet me at the station. Silly."

"Did anyone know you were coming?" she asked.

"I wrote a few, but no answers. I figured, they're busy, but they'll be there. They weren't."

"I'm still here," she said.

"You are," he said with a quick smile. "And I can't tell you how glad I am."

"You know," she said, "I must confess you look familiar, but I don't quite fit your face with the boy who came here-"

"Twenty years ago! And as for what he looked like, that other one, me, well-" He brought out a wallet and handed over a photograph of a boy perhaps twelve years old, with an impish smile and wild blond hair, looking as if he might catapult out of the frame.

"Ah, yes." Miss Adams closed her eyes to remember. "Spaulding. William Henry Spaulding?"

"Was I a lot of trouble?"

"Yes." She nodded and held the picture closer and glanced up at him. "A fiend." She handed the picture back. "But I loved you."

"Did you?" he said and smiled more broadly.

"In spite of you, yes. A good question. Let's not stand like your frozen friends. Come along. Take off that coat. The file index is there. Go look up your old library cards.”

He stood staring down into the index file like a bird fixing its gaze on a half-empty nest. He handed her one of the old purple-stamped cards. "I took out a lot of books."

"Ten at a time. I said no, but you took them. And read them!”

“Over here, of course, is the adult section."

"I begged you to let me cross over when I was thirteen. 'You're not ready,' you said. But-"

"I let you cross over anyway?"

"I hope you won't be upset, but when I was a boy I used to look up and see you behind your desk, so near but far away, and, how can I say this, I used to think that you were Mrs. God, and that the library was a whole world, and that no matter what part of the world or what people or thing I wanted to see and read, you'd find and give it to me . . . You did, too. You had the world ready for me every time I asked. There was always a place I hadn't seen, a country I hadn't visited where you took me. I've never forgotten."

She looked around, slowly, at the thousands of books. She felt her heart move quietly. "Did you really call me what you just said?"

"Mrs. God? Oh, yes. Often. Always." He suddenly leaned against the banister, holding tight. "Miss Adams.” He exhaled. "I'm scared. I don't want to leave. I'm afraid. I don't want to go away without saying good-bye. If I never return, I want to see all my friends . . . But I walk around town and nobody knows me. Everyone's gone."

Miss Adams took his arm and guided him to a brightly decorated room. ”Do you realize Thomas Wolfe was wrong?"

"Wolfe? The great literary beast? Wrong?"

"The title of one of his books."

"You Can't Go Home Again?" he guessed.

"That's it. He was wrong. This is home. Your friends are still here. This was your summer place."

"Yes. Myths. Legends. Mummies. Aztec kings. Wicked sisters who spat toads. Where I really lived. But I don't see my people."

She switched on a green-shaded lamp that shed a private light on a small table. "Isn't this nice? Most libraries today, too much light. There should be shadows, don't you think? Some mystery, yes? So that late nights the beasts can prowl out of the stacks and crouch by this jungle light to turn the pages with their breath. Am I crazy?"

She vanished into the stacks and came out with ten books that she placed upright, their pages a trifle spread so they could stand and he could read the titles.

"The summer of 1930, when you were, what? ten, you read all of these in one week."

"Oz? Dorothy? The Wizard? Oh, yes."

She placed still others nearby.

"Alice in Wonderland. Through the Looking- Glass; Tarzan of the Apes; John Carter, Warlord of Mars. Dear lady, how come you remember all this?"

"You never left. Summertimes you were here when I unlocked the doors. You sometimes brought sandwiches and sat out by the stone lion at noon. Your father pulled you home by your ear some nights when you stayed late. How could I forget a boy like that? You never played, never ran out in baseball weather, or football. Why?"

He glanced toward the front door. "They were waiting for me . . . You know. The ones who never borrowed books, never read. They. Them. Those."

"It's a wonder you survived. I used to watch you reading hunchbacked late afternoons. You looked so lonely."

"No. I had these. Company."

"Here's more." She put down Ivanhoe, Robin Hood, and Treasure Island. She came out not carrying many books but one at a time, as if each one were, indeed, special. She began to make a circle and as she placed the books, in lonely splendor, he said their names and then the names of the authors who had written them. She placed the first book and someone, far away, called "Kathy" a girl he had walked to school in the sixth grade [was] seated across the table.

A second book was set in place and another girl [appeared], who hid behind the book and dared to pass him notes when he was twelve.

And then [the girl] who always skirted the outer rim of school and went to swim in the deep lake ten thousand afternoons ago and never came out, so was never found, but suddenly now she made landfall here in the green-shaded light and opened Yeats.

And on her right: John Huff, whose name came clearer than the rest, who claimed to have climbed every tree in town and fallen from none, who yodeled at your sun-up window and wrote the same Mark Twain book report in four different grades.

And next to him was yet another girl.

And next to her ...

And just beyond ...

And it was finished, all the books were placed. He sat for a long moment and then, one by one, opened them and read. Behind him, he heard the lady librarian quietly back away to leave him with words.

A long while later he sat back, rubbed his yes, and looked around at the fortress of books, and nodded, his eyes wet.

"Yes . . . Thomas Wolfe, the title of that book of his. Wrong. Everything's here. Nothing's changed."

"Nothing will as long as I can help it . . . she said. Just then, from below the town, a train whistle blew. “Is that yours?"

"No, but the one soon after," he said and got up and moved around the small monuments that stood very tall and one by one, shut the covers, his lips moving to sound the old titles and the old, dear names. Do we have to put them back on the shelves?"

She looked at him and after a long moment said, "Tomorrow will do. Why?"

"Maybe during the night, because of the color of those lamps, green, the jungle, maybe those creatures you mentioned will come out and turn the pages with their breath. And maybe . . . Maybe my friends, who've hid in the stacks all these years, will come out, too.”

"They're already here.” She backed off across the room without making any sound, and when she reached her desk she called back, the last call of the night. "Closing time. Closing time, children." And turned the lights quickly off and then on and then halfway between; a library twilight.

He moved from the table with the double circle of books and came to her and said, "I can go now."

"Yes, William Henry Spaulding. You can
```

---

## IC-2019: Fahrenheit 451

- Title: Fahrenheit 451
- Author (byline): Ray Bradbury
- Work: Not specified
- Publisher: Del ray
- Publication date as stated: Aug 1987
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1859
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ray Bradbury
ISBN: 978-0345342966
Publisher: Del ray
Date (Month/Year): Aug 1987
```

### Introduction (context only: never use it for content warnings)

```text
Fahrenheit 451 takes place in an unspecified future time in a hedonistic and rabidly anti-intellectual America that has completely abandoned self-control and bans the possession of books. People are now only entertained by in-ear radio and an interactive form of television. Firemen in this futuristic setting are not enlisted to fight first, but rather to burn books and the houses that hold them, and to persecuting anyone in possession of the banned material Over the years, the novel has been subject to various interpretations, primarily focusing on the historical role of book burning in suppressing dissenting ideas. However, Bradbury has stated that the novel is not about censorship, but is a story about how television destroys interest in reading literature, which ultimately leads to ignorance of total facts. Fahrenheit 451, “"the temperature at which book-paper catches fire, and burns …" by Ray Bradbury
```

### Performance text (classify this)

```text
Montag looked at these men whose faces were sunburnt by a thousand real and ten thousand imaginary fires, whose work flushed their cheeks and fevered their eyes. These men who looked steadily into their platinum igniter flames as they lit their eternally burning black pipes. They and their charcoal hair and soot-colored brows and bluish-ash-smeared cheeks where they had shaven close; but their heritage showed.

Montag started up, his mouth opened. Had he ever seen a fireman that didn't have black hair, black brows, a fiery face, and a blue-steel shaved but unshaved look? These men were all mirror images of himself! Were all firemen picked then for their looks as well as their proclivities? The color of cinders and ash about them, and the continual smell of burning from their pipes. Captain Beatty there, rising in thunderheads of tobacco smoke. Beatty opening a fresh tobacco packet, crumpling the cellophane into a sound of fire.

Montag looked at the cards in his own hands. "I- I've been thinking. About the fire last week. About the man whose library we fixed. What happened to him?"

"They took him screaming off to the asylum."

"He wasn't insane."

Beatty arranged his cards quietly. "Any man's insane who thinks he can fool the government and us."

"I've tried to imagine," said Montag, "just how it would feel. I mean, to have firemen burn our houses and our books."

We haven't any books."

"But if we did have some."

"You got some?"

Beatty blinked slowly.

"No." Montag gazed beyond them to the wall with the typed lists of a million forbidden books. Their names leapt in fire, burning down the years under his ax and his hose which sprayed not water but kerosene. "No." But in his mind, a cool wind started up and blew out of the ventilator grille at home, softly, softly, chilling his face. And, again, he saw himself in a green park talking to an old man, a very old man, and the wind from the park was cold, too.

Montag hesitated. "Was-was it always like this? The firehouse, our work? I mean, well, once upon a time. . ."

"Once upon a time!" Beatty said. "What kind of talk is that?"

Fool, thought Montag to himself, you'll give it away. At the last fire, a book of fairy tales, he'd glanced at a single line. "I mean," he said, "in the old days, before homes were completely fireproofed-" Suddenly it seemed a much younger voice was speaking for him. He opened his mouth and it was Clarisse McClellan saying, "Didn't firemen prevent fires rather than stoke them up and get them going?" "That's rich!" Stoneman and Black drew forth their rule books, which also contained brief histories of the Firemen of America, and laid them out where Montag, though long familiar with them, might read: "Established, 1790, to bum English-influenced books in the Colonies. First Fireman: Benjamin Franklin."

RULE 1. Answer the alarm quickly.

2. Start the fire swiftly.

3. Burn everything.

4. Report back to firehouse immediately.

5. Stand alert for other Alarms.

Everyone watched Montag. He did not move.

The alarm sounded.

The bell in the ceiling kicked itself two hundred times. Suddenly there were four empty chairs. The cards fell in a flurry of snow. The brass pole shivered. The men were gone.

Montag sat in his chair. Below, the orange dragon coughed to life. Montag slid down the pole like a man in a dream.

The Mechanical Hound leapt up in its kennel, its eyes all green flame.

"Montag, you forgot your helmet!"

He seized it off the wall behind him, ran, leapt, and they were off, the night wind hammering about their siren scream and their mighty metal thunder! It was a flaking three-story house in the ancient part of the city, a century old if it was a day, but like all houses it had been given a fireproof plastic sheath many years ago, and this preservative shell seemed to be the only thing holding it in the sky.

"Here we are!"

The engine slammed to a stop. Beatty, Stoneman, and Black ran up the sidewalk, suddenly odious and fat in their plump fireproof slickers. Montag followed. They crashed the front door and grabbed at a woman, though she was not running, she was not trying to escape. She was only standing, weaving from side to side, her eyes fixed upon a nothingness in the wall, as if they had struck her a terrible blow upon the head. Her tongue was moving in her mouth, and her eyes seemed to be trying to remember something and then they remembered and her tongue moved again:

" 'Play the man, Master Ridley; we shall this day light such a candle, by

God's grace, in England, as I trust shall never be put out.' "

"Enough of that!" said Beatty. "Where are they?" He slapped her face with amazing objectivity and repeated the question. The old woman's eyes came to a focus upon Beatty. ''You know where they are or you wouldn't be here," she said.

Stoneman held out the telephone alarm card with the complaint signed in telephone duplicate on the back: "Have reason to suspect attic; II No. Elm, City. E. B."

"That would be Mrs. Blake, my neighbor," said the woman, reading the initials.

"All right, men, let's get 'em!"

Next thing they were up in musty blackness swinging silver hatchets at doors that were, after all, unlocked, tumbling through like boys all rollick and shout. "Hey!" A fountain of books sprang down upon Montag as he climbed shuddering up the sheer stair well. How inconvenient! Always before it had been like snuffing a candle. The police went first and adhesive taped the victim's mouth and bandaged him off into their glittering beetle cars, so when you arrived you found an empty house. You weren't hurting anyone, you were hurting only things! And since things really couldn't be hurt, since things felt nothing, and things don't scream or whimper, as this woman might begin to scream and cry out, there was nothing to tease your conscience later.

You were simply cleaning up. Janitorial work, essentially. Everything to its proper place. Quick with the kerosene! Who's got a match!

But now, tonight, someone had slipped. This woman was spoiling the ritual. The men were making too much noise, laughing, joking, to cover her terrible accusing silence below. She made the empty rooms roar with accusation and shake down a fine dust of guilt that was sucked in their nostrils as they plunged about. It was neither cricket nor correct. Montag felt an immense irritation. She shouldn't be here, on top of everything!

Books bombarded his shoulders, his arms, his upturned face. A book lit, almost obediently, like a white pigeon, in his hands, wings fluttering. In the dim, wavering light, a page hung open and it was like a snowy feather, the words delicately painted thereon. In all the rush and fervor, Montag had only an instant to read a line, but it blazed in his mind for the next minute as if stamped there with fiery steel. "Time has fallen asleep in the afternoon sunshine." He dropped the book. Immediately, another fell into his arms.

"Montag, up here!"

Montag's hand closed like a mouth, crushed the book with wild devotion, with an insanity of mindlessness to his chest. The men above were hurling shovelfuls of magazines into the dusty air. They fell like slaughtered birds and the woman stood below, like a small girl, among the bodies.

Montag had done nothing. His hand had done it all, his hand, with a brain of its own, with a conscience and a curiosity in each trembling finger, had turned thief. Now, it plunged the book back under his arm, pressed it tight to sweating armpit, rushed out empty, with a magician's flourish! Look here! Innocent! Look! He gazed, shaken, at that white hand. He held it way out, as if he were farsighted. He held it close, as if he were blind.

"Montag!"

He jerked about.

"Don't stand there, idiot!"

The books lay like great mounds of fishes left to dry. The men danced and slipped and fell over them.

Titles glittered their golden eyes, falling, gone. "Kerosene!"

They pumped the cold fluid from the numeraled 451 tanks strapped to their shoulders. They coated each book, they pumped rooms full of it.

They hurried downstairs, Montag staggering after them in the kerosene fumes.

"Come on, woman!"

The woman knelt among the books, touching the drenched leather and cardboard, reading the gilt titles with her fingers while her eyes accused

Montag.

"You can't ever have my books," she said.

"You know the law," said Beatty. "Where's your common sense? None of those books agree with each other. You've been locked up here for years with a regular Tower of Babel. Snap out of it! The people in those books never lived. Come on now!"

She shook her head.

"The whole house is going up," said Beatty.

The men walked clumsily to the door. They glanced back at Montag, who stood near the woman.

"You're not leaving her here?" he protested.

"She won't come."

"Force her, then!"

Beatty raised his hand in which was concealed the igniter. "We're due back at the House. Besides, these fanatics always try suicide; the pattern's familiar." Montag placed his hand on the woman's elbow. ''You can come with me." "No," she said. "Thank you, anyway."

“I’m counting to ten," said Beatty. "One. Two."

"Please," said Montag.

"Go on," said the woman.

"Three. Four."

"Here." Montag pulled at the woman.

The woman replied quietly, "I want to stay here."

"Five. Six."

“You can stop counting," she said. She opened the fingers of one hand slightly and in the palm of the hand was a single slender object. An ordinary kitchen match.

The sight of it rushed the men out and down away from the house. Captain Beatty, keeping his dignity, backed slowly through the front door, his pink face burnt and shiny from a thousand fires and night excitements. Montag thought, how true! Always at night the alarm comes. Never by day! Is it because fire is prettier by night? More spectacle, a better show? The pink face of Beatty now showed the faintest panic in the door. The woman's hand twitched on the single matchstick. The fumes of kerosene bloomed up about her. Montag felt the hidden book pound like a heart against his chest.

"Go on," said the woman, and Montag felt himself back away and away out the door, after Beatty, down the steps, across the lawn, where the path of kerosene lay like the track of some evil snail.

On the front porch where she had come to weigh them quietly with her eyes, her quietness a vondemnation, the woman stood motionless. Beatty flicked his fingers to spark the kerosene.

He was too late. Montag gasped.

The woman on the porch reached out with contempt to them all, and struck the kitchen match against the railing.

People ran out of houses all down the street.
```

---

## IC-2020: The Fall of Freddie the Leaf

- Title: The Fall of Freddie the Leaf
- Author (byline): Leo Buscalgia
- Work: Not specified
- Publisher: Slack
- Publication date as stated: Sept 1982
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1326
- Already set (do not supply): none

### Source block (context only)

```text
Author: Leo Buscaglia
ISBN: 978-0805010640
Publisher: Slack
Date (Month/Year): Sept 1982
```

### Introduction (context only: never use it for content warnings)

```text
This is the story of the life of a leaf named Freddie. On one level, it is a story of the seasons written in language simple enough for a child to understand. However, it is also a story of gentle depth, a meditation on the purpose of life, and a metaphor about the mystery and meaning of death.

The Fall of Freddie the Leaf by Leo Buscalgia
```

### Performance text (classify this)

```text
Spring had passed. So had Summer. Freddie, the leaf, had grown large. His mid section was wide and strong, and his five extensions were firm and pointed. He had first appeared in Spring as a small sprout on a rather large branch near the top of a tall tree.

Freddie was surrounded by hundreds of other leaves just like himself, or so it seemed. Soon he discovered that no two leaves were alike, even though they were on the same tree. Alfred was the leaf next to him. Ben was the leaf on his right side, and Clare was the lovely leaf overhead. They had all grown up together.

They had learned to dance in the Spring breezes, bask lazily in the Summer sun and wash off in the cooling rains.

But it was Daniel who was Freddie's best friend. He was the largest leaf on the limb and seemed to have been there before anyone else. It appeared to Freddie that Daniel was also the wisest among them. It was Daniel who told them that they were part of a tree. It was Daniel who explained that they were growing in a public park. It was Daniel who told them that the tree had strong roots which were hidden in the ground below. He explained about the birds who came to sit on their branch and sing morning songs. He explained about the sun, the moon, the stars, and the seasons.

Freddie loved being a leaf. He loved his branch, his light leafy friends, his place high in the sky, the wind that jostled him about, the sun rays that warmed him, the moon that covered him with soft, white shadows. Summer had been especially nice. The long hot days felt good and the warm nights were peaceful and dreamy.

There were many people in the park that Summer. They often came and sat under Freddie's tree. Daniel told him that giving shade was part of his purpose.

"What's a purpose?" Freddie had asked.

"A reason for being," Daniel had answered. "To make things more pleasant for others is a reason for being. To make shade for old people who come to escape the heat of their homes is a reason for being. To provide a cool place for children to come and play. To fan with our leaves the picnickers who come to eat on checkered tablecloths. These are all the reasons for being."

Freddie especially liked the old people. They sat so quietly on the cool grass and hardly ever moved. They talked in whispers of times past. The children were fun, too, even though they sometimes tore holes in the bark of the tree or carved their names into it. Still, it was fun to watch them move so fast and to laugh so much.

But Freddie's Summer soon passed. It vanished on an October night. He had never felt it so cold. All the leaves shivered with the cold. They were coated with a thin layer of white which quickly melted and left them dew drenched and sparkling in the morning sun. Again, it was Daniel who explained that they had experienced their first frost, the sign that it was Fall and that Winter would come soon.

Almost at once, the whole tree, in fact, the whole park was transformed into a blaze of color. There was hardly a green leaf left. Alfred had turned a deep yellow. Ben had become a bright orange. Clare had become a blazing red, Daniel a deep purple and Freddie was red and gold and blue. How beautiful they all looked. Freddie and his friends had made their tree a rainbow.

"Why did we turn different colors," Freddie asked, "when we are on the same tree?"

"Each of us is different. We have had different experiences. We have faced the sun differently. We have cast shade differently. Why should we not have different colors?" Daniel said matter-of-factly. Daniel told Freddie that this wonderful season was called Fall.

One day a very strange thing happened. The same breezes that, in the past, had made them dance began to push and pull at their stems, almost as if they were angry. This caused some of the leaves to be torn from their branches and swept up in the wind, tossed about and dropped softly to the ground. All the leaves became frightened.

"What's happening?" they asked each other in whispers.

"It's what happens in Fall," Daniel told them. "It's the time for leaves to change their home. Some people call it to die."

"Will we all die?" Freddie asked.

"Yes," Daniel answered. "Everything dies. No matter how big or small, how weak or strong. We first do our job. We experience the sun and the moon, the wind and the rain. We learn to dance and to laugh. Then we die."

"I won't die!" said Freddie with determination. "Will you, Daniel?"

"Yes," answered Daniel, "when it's my time."

"When is that?" asked Freddie.

"No one knows for sure," Daniel responded.

Freddie noticed that the other leaves continued to fall. He thought, "It must be their time." He saw that some of the leaves lashed back at the wind before they fell, others simply let go and dropped quietly. Soon the tree was almost bare.

"I'm afraid to die," Freddie told Daniel. "I don't know what's down there."

"We all fear what we don't know, Freddie. It's natural," Daniel reassured him. "Yet, you were not afraid when Summer became Fall. They were natural changes. Why should you be afraid of the season of death?"

"Does the tree die, too?" Freddie asked.

"Someday. But there is something stronger than the tree. It is Life. That lasts forever and we are all a part of Life."

"Where will we go when we die?"

"No one knows for sure. That's the great mystery!"

"Will we return in the Spring?"

"We may not, but Life will."

"Then what has been the reason for all of this?" Freddie continued to question. "Why were we here at all if we only have to fall and die?"

Daniel answered in his matter-of-fact way, "It's been about the sun and the moon. It's been about happy times together. It's been about the shade and the old people and the children. It's been about colors in Fall. It's been about seasons. Isn't that enough?"

"That afternoon, in the golden light of dusk, Daniel let go. He fell effortlessly. He seemed to smile peacefully as he fell. "Goodbye for now, Freddie," he said.

Then, Freddie was all alone, the only leaf on his branch. The first snow fell the following morning. It was soft, white, and gentle; but it was bitter cold. There was hardly any sun that day, and the day was very short. Freddie found himself losing his color, becoming brittle. It was constantly cold and the snow weighed heavily upon him.

At dawn the wind came that took Freddie from his branch. It didn't hurt at all. He felt himself float quietly, gently and softly downward. As he fell, he saw the whole tree for the first time. How strong and firm it was! He was sure that it would live for a long time and he knew that he had been part of its life and made him proud.

Freddie landed on a clump of snow. It somehow felt soft and even warm. In this new position he was more comfortable than he had ever been. He closed his eyes and fell asleep. He did not know that Spring would follow Winter and that the snow would melt into water. He did not know that what appeared to be his useless dried self would join with the water and serve to make the tree stronger. Most of all, he did not know that there, asleep in the tree and the ground, were already plans for new leaves in the Spring.
```

---

## IC-2021: Fear (from Seven Signs of Life)

- Title: Fear (from Seven Signs of Life)
- Author (byline): Aoife Abbey
- Work: Sevens Signs of Life, Pgs 17-31
- Publisher: Arcade
- Publication date as stated: Oct 2019
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1852
- Already set (do not supply): none

### Source block (context only)

```text
Author: Aoife Abbey
Book: Sevens Signs of Life, Pgs 17-31
ISBN: 978-1948924825
Publisher: Arcade
Date (Month/Year): Oct 2019
```

### Introduction (context only: never use it for content warnings)

```text
Grief. Anger. Hope. Joy . . . Fear. All emotions we expect to encounter over our lifetime. But what if this was every day? And what if your ability to manage them was the difference between life and death? For a doctor in Intensive Care this is part of the job. And the fear in the eyes of a terminally ill patient who pleads with you to not let them die can be overwhelming.

In the words of Nelson Mandela: I learned that courage was not the absence of fear, but the triumph over it ...

Fear from Seven Signs of Life by Aoife Abbey
```

### Performance text (classify this)

```text
(Pgs 17-31) If someone had asked me in medical school what I might be most afraid of, dead people wouldn't even have made the list. The first body I ever saw was when my grandmother died. She was laid out in her best clothes on top of her own duvet on her own bed. I remember being 11 years old and sitting on the bed beside my cousin, chatting, whilst absent-mindedly rearranging the rosary beads around her cold, dead fingers.

My first job as a doctor was on an elderly care ward and, for obvious reasons, it didn't take long until the issue of a dead patient presented itself. I don't think I had even considered it might be my job to 'verify' death. I entered the room alone and shut the door behind me. I approached the bedside and when I placed my stethoscope on her chest, I could hear those hollow noises that rumble inside the thorax of somebody who is dead - the sort of noises that make a newly qualified doctor think: What if they're not dead at all? What if I say they are dead, and then the family walk in the door and she moves?

Verification of death involves looking in the pupils, checking for a response to pain and stating that there is no respiratory effort, no palpable pulse and no heart sounds. I stood for the requisite 2 minutes with my stethoscope on her chest and my hand on her neck, where you would find a carotid pulse in a living person. I became convinced that she was going to open her eyes. I pictured them snapping open, her hand lurching towards my wrist, clamping shut with a strength that I knew she did not have in recent life. I let my imagination construct the whole terrifying ordeal; I couldn't stop it, and when the second-hand signaled the passing of 2 minutes, I raced out of the room, heart pounding.

I don't know if I've ever experienced undiluted fear quite like that again, though I do think that at least some of what I do requires a level of courage. And how can I call myself brave, if I cannot admit to still feeling fear?

It reminds me of something . . . In my childhood home, we had a staircase, and the first seven steps had empty spaces between the treads. As a child, I would convince myself that a hand was about to spring from one of those holes and grab my ankles. It wasn't real, I knew it wasn't, but I let myself believe it and I ran so fast up those stairs. Perhaps it is true that we create most of the fear we experience.

George Eliot said that 'we learn words by rote, but not their meaning; that must be paid for with our life-blood, and printed in the subtle fibers of our nerves'. From the first day that I started working as a doctor, I knew what a 'Do not Resuscitate' (DNR) order was. But more than 3 years into my career, I stood with a patient and a DNR order, and fear made me question everything I knew.

It was 4 a.m. and I had found myself on the way to the oncology ward to see a woman in her fifties. She was about the same age as my own mother and was very short of breath. I still recall thinking how calm and composed she was, for somebody who was struggling so obviously. I enquired if the woman had any pain. She shook her head. 'You don't have any pain in your chest? Can you slow your breathing down?' I placed my stethoscope on the patient's back and listened to her breath sounds; air moved in and out of her lungs, and they sounded clear. 'I'll be back,' I said, as I left her behind me to look at the ECG, which had been placed on the nurses' station outside. I picked up her folder and there, poking out of the front cover, was the DNR order. It had been discussed and signed just two days before, citing metastatic cancer. I remembered only in that instant that I was on the oncology ward.

The nurse called from the patient's bedside, 'You better come back in here, Doctor.' My patient lay flat on top of her bed: breathing, heart beating, but unresponsive.

Seconds ticked past and I was helpless, standing there thinking that I owed her something, but she was dying so abruptly. The nurse said she would go and call her family, although the patient would probably be dead before they arrived. I couldn't bring myself just to leave this woman alone.

In that moment, time surrounded me like an army advancing: step, step, the sound of heavy boots on ground, rifles brandished with their bayonets pointed in. Was there even a minuscule chance that there was something else that could be done, beyond standing there and watching her die? For a doctor who was scared, yes, it was the right thing for me. Within seconds, I felt my patient's pulse slip away and then she was dead. Was it the right thing for my patient? I don't believe it was, entirely. The best thing would have been for me to hold her hand and be present with her for her death. That wasn't the doctor she got that night; I did not have that presence of mind, and I don't mind admitting it.

Doctors have coping strategies to explain away fear. Mostly this happens unconsciously - the goal is to micromanage it. You cannot be a rabbit in the headlights - it simply isn't helpful. As an intensive-care doctor, my patients are often afraid. In many ways, their fear becomes routine. It is something I expect, and there is a standard reassuring phrase that I have come to say: 'Don't worry, everything is going to be okay. We're all here to keep you safe.' When I call a patient's fear 'routine', it is not a value judgement, it is just part of my routine. The sort of work I do doesn't leave a lot of time to work through the origins of fear with a patient. They need something, urgently, and you are required to deliver it, urgently, whether or not they're frightened. So you find yourself focusing on reassurance: ‘. . . everything is going to be okay, we've got you.’ In practical terms, what else can you say?

I'm not sure why, but one day I tried an approach that was less paternalistic in its reassurance. The patient had been thrown through a windscreen in a car accident. He was a young male in his twenties, bleeding, a lot, and I had found myself in the position of keeping my hand pressed on his previously gushing neck-wound.

'Am I going to die?' he asked suddenly. 'We're doing absolutely everything we can to help you. I know it is hard, but I need you to try and stay calm. Louder: 'But am I going to die?' 'You've got some significant wounds; we're going to do everything we can to make sure that doesn't happen.' Now shouting: 'AM I GOING TO DIE?'

He wanted a definitive: a yes or no, and I could have chosen either, but they would both have been a lie. I had no guarantees. The reality is that some patients look at you through their terrified, dilated pupils and they want you to say it's going to be okay. In the end, either I am right and they will be okay, or I am wrong and I will live with the fact that I chose to tell them otherwise: 'Don't worry, everything is going to be okay. We're all here to keep you safe.' Was I strong enough to cope with the burden of telling patients they would be all right, when actually there was always some chance - however remote - that they might be dead. Maybe it wasn't my job to take away a patient's fear -- usually what was happening to them was frightening . . . But you go to work the next day and stare into the next set of terrified eyes. That patient's fear explodes into the moment that you share together.

I have distracted frightened children with YouTube videos and teddy bears, so that somebody can put a cannula into their hand. I have stood by an MRI machine with a claustrophobic patient while she had her whole spine scanned and massaged her feet, because it helped her get through the scan. Sometimes, though, patients hand you their fear and you can do absolutely nothing about it.

I met Gloria when I was less than a month qualified. She was ninety years old and had been in hospital for many weeks. She was frail and had become immobile with pneumonia. It was clear that she was in the last days of her life. I remember standing by her bed one morning, when she gripped my hand suddenly and, looking at me with desperation, said, 'Please, don't let me die.'

What could I do? You can't say, 'Of course you are dying, Gloria; you are ninety years old, you have been dying for weeks and I can't change that now.' I tried to explain, to soothe her, but she couldn't hear me through her anguish. As a new doctor, I don't think I expected elderly people to be frightened of dying. I guess it is just easier if they are not; easier for me, anyway.

I prescribed Gloria medications to help her death pass as comfortably and painlessly as possible, but that didn't seem helpful enough, so I called the consultant. I told him that I thought Gloria needed emotional support. The consultant suggested we should phone and invite the family in that afternoon for a conversation. With apprehension, I asked them if they had any thoughts about how Gloria was feeling. As it turned out, they had already suspected she was frightened, and they thought what would bring Gloria comfort was a chaplain. It seemed like such a straightforward and obvious answer. Why did I not think of it myself? Confronted by her fear, I had panicked because I had no medical solutions.

Gloria died that night, sooner than any of us had expected. I believe the chaplains gave her what she needed - that which I couldn't give her - and I don't think she died frightened. I like to think that Gloria's fear became something else. If you are lucky, I believe that is what happens. Your fear of death becomes an impetus to find comfort. Your fear of losing your hard-fought independence becomes the momentum you need to stand on your feet again. Your fear of becoming the reason your family must experience grief gives you the strength to seek out truths that may be painful to hear.

And the fear of standing over a patient, with their life in your hands? [That fear] becomes the push you need to know that you did your best. . . . 'Don't worry, everything is going to be okay.
```

---

## IC-2022: The Final Days of Dog-Baby

- Title: The Final Days of Dog-Baby
- Author (byline): Mary O’Connell
- Work: Not specified
- Publisher: Chicago Tribune
- Publication date as stated: Sept 26, 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1684
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mary O’Connell
ISBN: Newspaper
Publisher: Chicago Tribune
Date (Month/Year): Sept 26, 1999
```

### Introduction (context only: never use it for content warnings)

```text
The birth of a baby affects everyone in the family: mom, dad, and siblings. But what about the family pet? Mary O’Connell explores the mind of a dog going through this traumatic change in “The Final Days ofDog-Baby” by Mary O’Connell.
```

### Performance text (classify this)

```text
Some younger age “cut” suggestions are designated by parenthesis

Mark and I were snuggled up on the couch, watching a little basketball, and I felt happy. Then we heard Beth screaming in the bathroom. She rushed out to us, waving the pregnancy-test stick in the air, yelling, "It's a cross, it's a cross."

It wasn't a cross, of course, it was an X. The X means you are pregnant.

I had been dreading this news. But God knows I'm a sucker for fun, so I hopped off the couch and ran in a circle around their feet as they jumped up and down, game-show style.

"A baby," Mark said.

"A baby," Beth said.

A fierce premonition of loneliness flooded my heart, and I slunk away from them, trying to steel myself against the love that would soon be taken so cruelly. I imagined myself staked in the back yard the following winter, parched and starving, gnawing ice chips from a dented water bowl. With their love for the baby, I would become a curiosity: "Why did we ever want this old thing? Dog-Baby, free to good home."

When I started to cry, they (said) "Give us some kisses, Dog-Baby, you big velvet schmutz.” and I was happy again. Hey, I'm moody.

In the beginning I was Dahlia, named for the flowers on the patio: Legend has it that the day they brought me home from the kennel, I stretched my neck up to the terra-cotta pots, and smelled the flowers.

Beth yelled, "Dahlia." Mark had reservations, and he was right, because the name never stuck. By the second day, enamored of my tight, round tummy, caramel-colored eyes and they cuddled me to their shoulders and called me Dog-Baby.

But my name has caused real pain for all of us. Recently, Mark and Beth had a dinner guest who told endless stories about her brilliant toddler. This was back when they believed the doctors who claimed they would never have a baby, and they both sat there with stiff smiles stretched across their faces. To break up the tension, I sprang out from my post under the kitchen table and started barking. The woman gaped at me with an expression of repulsed curiosity. "Dog-Baby. So your dog's like your. . . baby."

When it was just the three of us again, Beth raged: "This is who we are, Mark. We're yuppies who treat our dog like a baby.”

Mark tried to comfort her.

Anyway, Beth stormed out of the house and soon

we heard the car rocketing down the street.

Mark gave me a peanut-butter biscuit, then

poured a juice glass. I held the biscuit in my

mouth, watching him; I cannot eat on a nervous

stomach. When I rested my head on his knee and

sighed, Mark reached under the table and

stroked my ears.

After some time, he raised his glass. "Here's to us, Dog-Baby." For as long as I can remember, I have been the Dog-Baby.

Strange how the days gallop past when you dread the future. It is the first Saturday in November, misty and gray, and Beth is eight months along. Mark is painting "the nursery," I'm relegated to the back yard for the morning--the beginning of the end. I peer through the planks in the fence and see Trixie, the dachshund who lives in the house behind us, skitter through her tiny dog-door.

"Trixie," I yell, "over here," and she runs across her yard and zips under the fence.

We sniff each other's butt, then kiss-kiss.

"Trixie," I say, my lips quivering like Bette Davis, "if they forget to feed me when the baby comes, will you save your Snausages for me?"

"Aw, Dog-Baby, they won't forget to feed you! After Madison came, Sue and Campbell never forgot to feed me. They let my water dish go dry a time or two, but I just licked the shower floor, no problem!"

I shudder at this image. How can I expect her to understand? She was a pound dog and lived through atrocities before Sue and Campbell brought her home and made her perpetually grateful. But I have known only opulence: a king-size bed, organic biscuits, and love. Now that unhappiness looms ahead of me, I find myself more than a little ill-prepared.

"Dog-Baby, I know you've been sad about the little baby comin' and you have what I consider to be a classic fear of displacement. But I'm here to tell you: Buck up, buttercup! They'll still love you. When a baby comes, it just means the pack gets bigger!"

Sue calls out the kitchen window for Trixie to come home.

"Okay, Trix," I sigh, "we'll be seeing you,"

"Not if I see you first, Dog-Baby," she says, flashing the smile that saved her from Death Row.

The bed shrinks as Beth gets bigger and bigger. Tonight, as I listen to the rain, I suffer from a kind of self-induced insomnia. Since time is my enemy, I keep my eyes open, trying to hold on to the day, watching the numbers slip past on the digital clock. Beth turns on her side, and spoons her body to mine. Pressed against my spine I feel the great weight of Beth's stomach, and then, movement, like a giant heart beating.

"The baby is kicking you, Dog-Baby."

And I'm thinking about how true that is, when Beth sits up in bed. "Holy Mother of God, I'd like a cigarette." (Possible substitution for younger ages: "Oh my gosh, I need ice-cream.”)

Next thing you know she's slogging her big body out of bed and putting on slippers. I follow her.

I sit on the rug and watch her with disdain.

"Don't give me that look, Dog-Baby. I haven't had a cigarette for ages. I know it's disgusting; I don't know why I love it so much." (Possible substitution for younger ages: I haven't had ice cream for ages.)

It's chilly. Beth notices me shivering and takes a sequined sweater from the garbage bag of clothes destined for the Salvation Army. She buttons the top button of the sweater around my neck, arranging the arms of the sweater to look like human arms jutting out of my Dog-Baby body.

She just leans back and laughs. "Dog-Baby, you look just like a glamorous spinster aunt sitting at a soda fountain! Miss Prim!"

I've heard it all before.

And I prefer when she wants to watch "I Love Lucy" at 2 a.m. and we cuddle under a quilt on the couch. "See how Ricky loves Lucy, the look in his eyes?” And there are the night sounds of the house: the hiss of the furnace, the refrigerator's song, mice running in the walls, the perpetual drip of the kitchen faucet.

Beth takes a last drag on her cigarette (Possible substitution for younger ages: Beth takes a last spoonful of ice-cream), and bursts into tears. I whimper along with her--it's my way. She's worried the baby will have six heads because she smoked a cigarette (Possible substitution: She's worried the baby will have six heads because she had too much sugar;) me, I'm sad our private late-night rendezvous are coming to an end.

The digital clock reads 8:10 when Mark walks into the bedroom carrying a blue blanket with white stars, and right away I know I slept through the whole deal.

The blanket is in front of my face.

"Smell, Dog-Baby."

This is what it says to do in the books. The books have a lot of crazy advice. It is upon us. Acceptance is the only choice. I sniff the dog blanket, Mark takes me in his arms and I feel his love, but it's like how you love an old aunt in a nursing home: Gosh, you were nice. We have a lot of really nice pictures of you.

Beth staggers in the door carrying a white baby carrier and the big, black diaper bag. Mark comes next, carrying the actual baby in a mint green blanket. I sit stoically, holding my head up but casting my eyes down, ever the brave coquette.

Beth winces as she bends down and lays her head on my bony shoulder. She bursts into tears. "Oh, Dog- Baby, it's like I haven't seen you in a million trillion years."

Which is the reception I've been hoping for. It's a relief when Mark sits on the couch and motions for me to join him. He pulls the blanket back from the baby's face and offers me a look.

"Here's the baby, Dog-Baby."

Well. He's nothing like the big, rubbery babies on TV. He is small and red and ancient-looking, a tiny guy in a panda outfit. As I gaze at him, I feel the weird miracle of it all, how odd it is that a body can produce another body.

The baby cries out, and Beth coos to it nervously as Mark caresses the baby's cheek with his quivering finger. They are afraid of this baby! This is something I never anticipated, and I can't help but feel a little smug, for certainly they were never afraid of me.

The first night, I stand at the doorway as Mark and Beth climb into bed. The baby is sleeping in the bassinet on Beth's side of the bed. I chant to myself, "I am a dog," a mantra for the future, when Mark whispers, "Dog-Baby, do you need an engraved invitation get in the bed?" My heart leaps up, and I sail onto the bed, snuggle down between them.

Beth puts her finger to her lips and whispers, "I just wanted to make sure he was still breathing."

Of course, it's me who's in danger of falling into that final sleep, me who has the arthritis and poor circulation and iffy heart. But my ears are perfect; I hear each breath expanding in the baby's new lungs. I hope I live to see this baby grow into his childhood. I want to be stranded, say, in Antarctica, and have him make a solo journey to rescue me, as brave children do in the movies. But for now he is just a baby, living every second at the mercy of others. My brother.
```

---

## IC-2023: Fly Away Home

- Title: Fly Away Home
- Author (byline): Eve Bunting
- Work: Not specified
- Publisher: Clarion Books
- Publication date as stated: Mar 1993
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: CHILD, MR. SLOCUM, DAD, STRANGER 1, STRANGER 2, DENNY
- Teaser before the introduction: Yes
- Spoken words (computed): 1081
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eve Bunting
ISBN: 978-0395664155
Publisher: Clarion Books
Date (Month/Year): Mar 1993
```

### Introduction (context only: never use it for content warnings)

```text
There is a common misconception that homelessness is an issue that only pertains to single men and women, but **according to the National Alliance to End Homelessness, almost 60,000 families are homeless on a given night in the United States.

Homelessness is a devastating experience for families. It disrupts every aspect of their lives, damaging their physical and emotional health and interfering with children’s education and development. *** According to the Bassuk Center: 1 in 30 children in the US experience homelessness – That’s 2.5 million children! This is Andrew’s story . . .

Fly Away Home by Eve Bunting
```

### Performance text (classify this)

```text
CHILD: (sings) * I never dreamed I'd ever be,
Without a home to comfort me
'Til a friend of mine this very Spring
Lost his whole house and everything.

CHILD: My dad and I live in an airport. That's because we don't have a home and the airport is better than the streets. We are careful not to get caught. (beat) Mr.

Slocum and Mr. Vail were caught last night.

MR. SLOCUM: (singing) Ten green bottles, hanging on the wall . . .

CHILD: They were as loud as two moose bellowing. Dad said they broke the first rule of living here.

DAD: Don't get noticed.

CHILD: Dad and I try not to get noticed. We stay among the crowds. We change airlines.

DAD: Delta, TWA, Northwest, we love them all.

CHILD: He and I wear blue jeans and blue T-shirts and blue jackets. We each have a blue zippered bag with a change of blue clothes. Not to be noticed is to look like nobody at all. Once we saw a woman pushing a metal cart full of stuff. She wore a long dirty coat and she lay down across a row of seats in front of Continental Gate 6. The cart, the dirty coat, the lying down were all noticeable. Security Moved her out real fast. Dad and I sleep sitting up. We use different airport areas. (to Dad) Where are we tonight?

DAD: (checking his notebook) Alaska Air. Over in the other terminal.

CHILD: That's OK. We like to walk. We know some of the airport regulars by name and by sight. There's Idaho Joe and Annie Frannie and Mars Man. But we don't sit together.

DAD: Sitting together will get you noticed faster than anything.

CHILD: Everything in the airport is on the move -- passengers, pilots, flight attendants, cleaners with their brooms. Jets roar in, close to the windows. Other jets roar out. Luggage bounces down chutes, escalators glide up and down, disappearing under floors. Everyone's going somewhere except Dad and me. We stay.

Once a little brown bird got into the main terminal and couldn't get out. It fluttered in the high, hollow spaces. It threw itself at the glass, fell panting on the floor, flew to a tall metal girder, and perched there exhausted. (to bird) Don't stop trying. Don't! You can get out!

(to audience) For days the bird flew around, dragging one wing. And then it found the instant when a sliding door was open and slipped through. I watched it rise. Its wing seemed OK. (whispering to bird) Fly bird. Fly away home! (to audience) Though I couldn't hear it, I knew it was singing. Nothing made me as happy as that bird.

The airport's busy and noisy even at night. Dad and I sleep anyway. When it gets quiet, between two and four a.m., we wake up.

DAD: Dead time. Almost no flights coming in or going out.

CHILD: At dead time there aren't many people around, so we're extra careful. In the mornings Dad and I wash up in one of the bathrooms, and he shaves. The bathrooms are crowded, no matter how early. And that's the way we like it. (beat) Strangers talk to strangers . . .

STRANGER 1: Where did you get in from?

STRANGER 2: Three hours our flight was delayed. Ma, am I bushed!

CHILD: Dad and I, we don't talk to anyone. We buy doughnuts and milk for breakfast at one of the cafeterias, standing in line with our red trays. Sometimes Dad gets me a carton of juice.

On the weekends Dad takes the bus to work. He's a janitor in an office in the city. The bus fare's a dollar each way. On those days Mrs. Medina looks out for me. The Medinas live in the airport too - Grandma, Mrs. Medina and Denny, who's my friend. He and I collect rented luggage carts that people have left outside and return them for fifty cents each. If the crowds are big and safe, we offer to carry bags.

(to traveler) Get this one for you, lady? It looks heavy. (to another traveler) Can I call you a cab?

Denny's real good at calling cabs. That's because he's seven already. Sometimes passengers don't tip. Then Denny whispers, stingy! But he doesn't whisper too loud. The Medinas understand that it's dangerous to be noticed.

When Dad comes home from work, he buys hamburgers for us and the Medinas. That's to pay them for watching out for me. If Denny and I've had a good day, we treat for pie. But I've stopped doing that. I save my money in my shoe.

(to Dad) Will we ever have our apartment again? (to audience) I'd like it to be the way it was before Mom died.

DAD: Maybe we will. If I can find more work. If we can save some money. (tousling the child’s hair) It's nice right here, though, isn't it? It's warm. It's safe. And the price is right.

CHILD: But I know he's trying all the tme to find us a place. He takes newspapers from the trash baskets and makes pencil circles around letters and numbers. Then he goes to the phones. When he comes back he looks sad. Sad and angry. I know he's been calling about an apartment. I know the rents are too high for us.

(to Dad) I'm saving money, too! (lifts one foot and points to shoe)

DAD: (smiling) Atta boy!

DENNY: If we get a place, you and your dad can come live with us.

CHILD: And we get a place, you and your mom and your grandma can come live with us.

DENNY: Yeah!

CHILD: (to audience) We shake on it. That's going to be so great! After next summer, Dad says, I have to start school. (to Dad) How?

DAD: I don't know. But it's important. We'll work it out.

CHILD: Denny's momsays he can wait for a while. But Dad says I can't wait. (long beat) Sometimes I watch people meeting people.

STRANGER 1: We missed you.

STRANGER 2: It's so good to be home.

CHILD: Sometimes I get mad, and I want to run at them and push them and shout.

(shouting) Why do you have homes when we don't? What makes you so special?

(to audience) That would get us noticed, all right. Sometimes I just want to cry. (long beat) I think Dad and I will be here forever. (beat) Then I remember the bird. (whispering to himself) Don't stop trying. Don't! You can get out!

It took a while, but a door opened. And when the bird left, when it flew free, I know it was singing

(sings) * I never dreamed I'd ever be,
Without a home to comfort me
'Til a friend of mine this very Spring
Lost his whole house and everything.
So now I know that life is strange,
That all is luck and luck can change,
And don't forget, it's sad but true,
The next time around it could be you . . .
```

---

## IC-2024: Fortunately, the Milk

- Title: Fortunately, the Milk
- Author (byline): Neil Gaiman
- Work: Not specified
- Publisher: HarperCollins
- Publication date as stated: Sept 2014
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ME, DAD, SISTER, ALIEN, PIRATE QUEEN, STEG, PONY, VAMPIRE, POLICE
- Teaser before the introduction: Yes
- Spoken words (computed): 1684
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Gaiman
ISBN: 978-0062224088
Publisher: HarperCollins
Date (Month/Year): Sept 2014
```

### Introduction (context only: never use it for content warnings)

```text
Author Neil Gaiman is a phenomenon. I'm not saying that's good. I'm not saying that's bad. I'm simply stating a fact. A fellow author recently commented that when Gaiman talks, people clap. When he coughs, they laugh. And there’s no better way to introduce you to his unique storytelling style than to take you on a mystical adventure with an imaginative and creative father in Fortunately, the Milk by Neil Gaiman
```

### Performance text (classify this)

```text
ME: (searching the refrigerator) There was only orange juice in the fridge. Nothing else that you could put on cereal, unless you think that ketchup or mayonnaise or pickle juice would be nice, which I do not.

DAD: Eat your cereal. Remember, it’s Orchestra Practice this afternoon

SISTER: We can’t eat our cereal. No milk.

ME: He looked like he was going to suggest that we have something for breakfast that you do not need milk for, like sausages, but then he remembered that, without milk, he couldn’t have his tea.

DAD: You poor children. I will get milk . . .

SISTER: Where have you been all this time?

DAD: I bought the milk. I walked out of the corner shop and heard something odd coming from above me. It was a noise like this: thummthumm. I looked up and saw a huge silver disc hovering in the air. And the next thing I knew, I was being sucked up into the disc. Fortunately, I had put the milk into my coat pocket. The people in the disc were a bit green and rather globby and they looked very grumpy indeed.

ALIEN: As a representative of your species, we demand that you give us ownership of the whole planet. We are going to remodel it.

DAD: I jolly well won’t. (to the kids) I noticed a large metal door with EMERGENCY EXIT DO NOT OPEN FOR ANY REASON THIS MEANS YOU! on it. I opened the door.

ALIEN: Don’t do that. You’ll let the space-time continuum in.

DAD: But it was too late; I had already pushed open the door. I JUMPED. Fortunately, I had kept tight hold of the milk, so when I splashed into the sea I didn’t lose it.

PIRATE QUEEN: What was that? A big fish? A mermaid? Or was it a spy?

DAD: I wanted to say that I wasn’t any of those things, but my mouth was full of seawater. I felt myself being hauled up onto the deck. There were a number of men and a woman on the deck, and they all looked very cross.

PIRATE QUEEN: Who be ye, landlubber? What are you doing here?

DAD: Well . . . I just set out to the corner shop for some milk for my children’s breakfast and for my tea, and the next thing I knew—

PIRATE QUEEN: You dare lie to the Queen of the Pirates?

DAD: If I did not go to the corner shop to fetch the milk, then where did this milk come from? (showing her the milk)

PIRATE QUEEN: You’re on a pirate ship now, my fine bucko. There are only two choices—you can join my pirate crew, or refuse to join and we will slit your cowardly throat and you will go to the bottom of the sea, where you will feed the fishes.

DAD: I wish that I could, but I have children. And they need their breakfast.

PIRATE QUEEN: Then you must die! Walk the plank!

DAD: I edged out to the end of the plank. Sharks were circling. So were piranhas—

ME: Hang on. Piranhas are a freshwater fish. What were they doing in the sea?

DAD: You’re right. Right. So . . . I was out at the end of the plank, facing certain death, when a rope ladder hit my shoulder . . .

STEG: QUICKLY! CLIMB UP THE ROPE LADDER!

DAD: Fortunately, the milk was pushed deep into the pocket of my coat. And I soon made it to the top of the rope ladder. I’d never been in the basket of a hot air balloon before.

STEG: I hope you don’t mind me helping, but it looked like you were having problems down there.

DAD: You’re a stegosaurus!

STEG: I am an inventor. I have invented the thing we are traveling in, which I call Professor Steg’s Floaty-Ball- Person-Carrier.

DAD: (to Steg) I call it a balloon . . . (to the kids) He showed me his Time Machine. He was very proud of it. It was a large cardboard box with several pebbles on it, and stones stuck to the side. There was also a large, red button. (to Steg) Hang on. Those are diamonds. And sapphires. And rubies.

STEG: Actually, I call them special-shiny-clear-stones, special-shiny-bluey-stones, and, um—

DAD: Well, it was very lucky for me that you turned up when you did and rescued me. I need to get home in order to make sure my children get milk for their breakfast. (shows him the milk) Although I expect that one hundred and fifty million years ago you called it ‘wet-white-drinky-stuff. Can you take me home?

STEG: Yes and no. Yes, I would love to take you home. Nothing would make me happier. No, I cannot take you home. My Time Machine is being temperamental. I have pressed that button many times but nothing happens.

DAD: Button? Don’t you mean ‘big-red-flat-pressy-thing’?

STEG: I most certainly do not. It is a button. I named it after my Aunt Button.

DAD: Can I press it? (to the kids) I pressed the button. The sun shot around the sky, and the balloon began to rock and lurch and zoom around like an angry fly. I held on to the ropes as hard as I could. Fortunately, I was still keeping tight hold of the milk in my right hand.

SISTER: Are there any ponies in this? I thought there would be ponies by now.

DAD: (ad libbing like crazy to somehow incorporate ponies) The machine stopped. We were hanging in the air above a grassy plain. Below me, on a number of brightly colored ponies were gathered.

PONY: You must be the man with the milk. We have heard about you, in our tales.

SISTER: I’m so glad there were ponies.

DAD: The milk! My children are breakfastless . . . (to the kids) And with that, Professor Steg pressed the red button with his heavily armored tail. There was a ZOOM, a TWORP, and a THANG, and we were hurtling through the cosmic void --FLOATING above a landscape of ominous towers and castles. It was not a friendly place. Bats flew across the sky in huge flocks. There was a loud FLUT!, and where the bats had been, several pallid people were now standing. The man in front had a very bald head. THEY ALL HAD SHARP TEETH.

VAMPIRE: Ve are wumpires. Vot is this? Who are you? Answer us, or ve vill wiwisect you.

STEG: I am Professor Steg. We are on an important mission. My assistant is trying to get home to the future for breakfast.”

DAD: At the word BREAKFAST all the wumpires looked very excited.

VAMPIRE: Ve have not had our breakfast. Ve normally have vigglyvorms, vith orange juice on them. Orange juice makes vorms ewen vigglier. Like vandering spaghetti. But if ve cannot eat vorms ve vill eat assistant, or ewen roast professor.

DAD: One of the wumpires took out a fork and looked me up and down in a hungry sort of way. The professor tinkered with the jewels and the string and the buttons.

STEG: I think I’ve got it properly fine-tuned, now. This next press should bring you back to your own time, place, and breakfast.

DAD: I pressed the red button. The hole in space opened again. And [we and] the milk came rocketing through. There was an ear-popping noise and I was floating, in a balloon basket. I could see our house. I could see the bicycles in the back garden. I could see the rabbit hutch.

ME: Does that mean that there is a Stegosaurus in a hot air balloon outside?

DAD: There is not. For reasons that will become apparent

SISTER: (wistfully) I think that there should have been some nice wumpires . . . Nice, handsome, misunderstood wumpires.”

DAD: There was a familiar sort of a thumm-thumm noise, and before I had a chance to press the red button [again], we were deposited, balloon and all, on the enormous metal deck of a flying saucer, with a number of very grumpy-looking green globby people staring at us with too many eyes. They did not look pleased.

ALIEN: HaHA! You thought you had escaped us! And you were wrong! Now, you must sign the planet over to us so that we can remodel it. We will take out all the trees and put in plastic flamingoes. Also, we are going to replace the clouds with scented candles. We have been tracking your movements through time and space. Now, see what happens when I press this grundledorfer

(points to a button on the spaceship control panel).

DAD: It’s called a button.

ALIEN: Nonsense. We named it after our brood-aunt, Nessie Grundledorfer. (pushes the button)

DAD: There was a CRACKLE. There was a FIZZ. Standing around us, in attitudes of anger and irritation, were several pirates and some wumpires.

PIRATE QUEEN: Prepare to be keelhauled, you scurvy dogs.

VAMPIRE: Ve vants those willains and warmints wiolently vound up.

DAD: The aliens looked at each other. One of them pressed the grundledorfer. The wumpires and pirates were gone. It was at that moment that a voice louder than anything I have ever heard said

POLICE: GALACTIC POLICE. DO NOT MOVE.

DAD: There were red and blue flashing lights and about half a dozen uniformed dinosaurs, holding unmistakably large and extremely serious weapons. They pointed their weapons at the green globby aliens.

POLICE: You are charged with breaking into people’s planets and redecorating them. And then with running away and doing it again somewhere else, over and over.

You have committed crimes against the inhabitants of eighteen planets, and crimes against good taste. DADThe Tyrannosaurus handcuffed all the green globby people together with something that looked a lot more like pink string-in-a-can than it looked like handcuffs, which was a good thing because they probably didn’t have hands and they definitely didn’t have wrists. The last I saw of any of them, the whole inside of the saucer was fading into light so bright I had to close my eyes and look away. And then I was standing at the back door of our house, none the worse for wear. So I came in. And here I am . . .

ME: That was what my dad said. I looked around the kitchen. At the calendar on the wall with the hot air balloons on it. At my dinosaur models and my sister’s ponies, at my sister’s vampire books.

SISTER: You know we don’t believe any of this.

ME: Especially not how you saved the world from being remodeled. Or the pirates. Not. Any. Of. It.

DAD: (shrugging) Suit yourselves. But it was all true. And I can prove it. Here’s the MILK!
```

---

## IC-2025: The Frog Prince Continued

- Title: The Frog Prince Continued
- Author (byline): Jon Scieszka
- Work: Not specified
- Publisher: Viking Juvenile
- Publication date as stated: May 1991
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, PRINCESS, PRINCE, WITCH 1, WITCH, WITCH 2, WITCH 3, FAIRY GODMOTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1042
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jon Scieszka:
ISBN: 978-0670834211
Publisher: Viking Juvenile
Date (Month/Year): May 1991
```

### Introduction (context only: never use it for content warnings)

```text
And they lived happily ever after . . .This is where most fairy tales end. The prince and princess marry and ride off into the sunset to begin their new life together as husband and wife, a life full of promise, romance, and above all, love. But no one has ever told us how this is supposed to happen, or why it succeeds if it does. In The Frog Prince Continued by Jon Scieszka, the truth behind happily ever after is revealed -- warts and all. (CROAK)

The Frog Prince Continued by John Scieszka
```

### Performance text (classify this)

```text
NARRATOR: The Princess kissed the frog, he turned into a prince and they lived happily ever after. Well, let’s just say they lived sort of happily for a long time. Okay, so they weren’t so happy. In fact, they were miserable.

PRINCESS: Stop sticking your tongue out like that.

PRINCE: How come you never want to go down to the pond anymore?

NARRATOR: The Prince and Princess were so unhappy. They didn’t know what to do.

PRINCESS: I would prefer that you not hop around on the furniture. And it might be nice if you got out of the castle once in a while to slay a dragon or giant or whatever.

NARRATOR: The Prince didn’t feel like going out and slaying anything. He just felt like running away. But then he reread his book. And it said right there at the end of his story: “They lived happily ever after. The End.” So he stayed in the castle and drove the Princess crazy. Then one day, the Princess threw a perfectly awful fit.

PRINCESS: First you keep me awake all night with your horrible, croaking snore. Now I find a lily pad in your pocket. I can’t believe I actually kissed your slimy frog lips. Sometimes I think we could both be better off if you were still a frog.

NARRATOR: That’s when the idea hit him. The Prince thought . . .

PRINCE: Still a frog . . .Yes! That’s it!

NARRATOR: And he ran off into the forest, looking for a witch who could turn him back into a frog. The Prince hadn’t gone far when he ran into just the person he was looking for.

PRINCE: Miss Witch, Miss Witch. Excuse me, Miss Witch. I wonder if you could help me?

WITCH 1: Say, you’re not looking for a princess to kiss are you?

PRINCE: Oh, no. I’ve already been kissed. I’m the Frog Prince. Actually, I was hoping you could turn me back into a Frog.

WITCH: Are you sure you’re not looking for a beautiful sleeping princess to kiss and wake up?

PRINCE: No, no -- I’m the Frog Prince.

WITCH: That’s funny. You don’t look like a frog. Well, no matter. If you’re a prince, you’re a prince. And I’ll have to cast a nasty spell on you. I can’t have any princes waking up Sleeping Beauty before the hundred years are up.

NARRATOR: The Prince didn’t stick around to see which nasty spell the witch had in mind. He ran deeper into the forest until he came to a tiny cottage where he saw another lady who might help him.

PRINCE: Miss Witch, Miss Witch. Excuse me, Miss Witch. I wonder if you could help me. I’m a prince and---“

WITCH 2: Eh? What did you say? Prince?

PRINCE: No, I mean, yes. I mean, no, I’m not the prince looking for Sleeping Beauty. But, yes, I’m the Frog Prince. And I’m looking for a member of your profession who can turn me back into a frog so I can live happily ever after.

WITCH: Frog Prince, you say? That’s funny. I thought frogs were little green guys with webbed feet. Well, no matter: If you’re a prince, you’re a prince. And I can’t have any princes rescuing Snow White. Here- eat the rest of this apple.

NARRATOR: The Prince, who knew his fairy tales (and knew a poisoned apple when he saw one), didn’t even stay to say, “No Thank you.” He turned and ran deeper into the forest. Soon he came to a strange-looking house with a witch outside.

PRINCE: Ahem. Miss Witch, Miss Witch. Excuse me, Miss Witch. I wonder if you could help me? I’m the Frog-

WITCH 3: If you’re a frog, I’m the King of France.

PRINCE: No, I’m not a frog. I’m the Frog Prince. But I need a witch to turn me back into a frog so I can live happily ever after, can you do it?”

WITCH: (eyeing the Prince and licking her lips) Why, of course, dearie. Come right in. Maybe I can fit you in for lunch.

NARRATOR: The Prince stopped on the slightly gummy steps. Something about this house seemed very familiar. He broke off a corner of the windowsill and tasted it. Gingerbread.

PRINCE: I hope you don’t mind my asking, Miss Witch. But do you happen to know any children by the name of Hansel of Gretel?

WITCH: Why yes, Prince darling, I do. I’m expecting them for dinner.

NARRATOR: The Prince who, as we said before, knew his fairy tales, ran as fast as he could deeper into the forest. Soon he was completely lost. He saw someone standing next to a tree. The Prince walked up to her, hoping she wasn’t a witch, for he’d quite had his fill of witches.

PRINCE: Madam. I am the Frog Prince. Could you help me?”

FAIRY GODMOTHER: Gosh, do you need it. You are the worst-looking frog I’ve ever seen.

PRINCE: I am not a frog. I am the Frog Prince and I need someone to turn me back into a frog so I can live happily ever after.

FAIRY GODMOTHER: Well, I’m on my way to see a girl in the village about going to a ball, but I suppose I could give it a try. I’ve never done frogs before, you know.

NARRATOR: And with that the Fairy Godmother waved her magic wand and turned the Prince into a beautiful carriage. The Prince couldn’t believe his rotten luck. The sun went down. The forest got spookier. And the Prince became more and more frightened.

PRINCE: Oh, what an idiot I’ve been. I could be sitting at home with the Princess, living happily ever after. But instead, I’m stuck here in the middle of this stupid forest, turned into a stupid carriage. Now I’ll probably just rot and fall apart and live unhappily ever after.

NARRATOR: The Prince thought these terrible, frightening kinds of thoughts (and a few worse- too awful to tell), until far away in the village the clock struck midnight. The carriage instantly turned back into his former Prince self and ran by the light of the moon until he was safe inside his own castle.

PRINCESS: Where have you been? I’ve been worried sick. You’re seven hours late. Your dinner is cold. Your clothes are a mess.

PRINCE: The Prince looked at the Princess who had believed him when no one else in the world had, the Princess who had actually kissed his slimy frog lips. The Princess who loved him.

NARRATOR: The Prince kissed the Princess. They both turned into frogs. And they hopped off happily ever after. (CROAK)
```

---

## IC-2026: Garbage Scan

- Title: Garbage Scan
- Author (byline): Dave Barry
- Work: Dave Barry Talks Back, Pg 158-162
- Publisher: Three Rivers Press
- Publication date as stated: May 1992
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: SPEAKER
- Teaser before the introduction: Yes
- Spoken words (computed): 577
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Barry
Book: Dave Barry Talks Back, Pg 158-162
ISBN: 978-0517588680
Publisher: Three Rivers Press
Date (Month/Year): May 1992
```

### Introduction (context only: never use it for content warnings)

```text
Channel-surfing enables the listener to escape the incessant pressures of political advertising, commercials, talk radio, news reports, radio evangelists and of course, the dreaded CLASSICAL MUSIC channels.

Let’s face it . . . we don’t want to hear any of those things on the way to work. We want REAL music . . . the kind that makes you long for a convertible and a hundred miles of open road.

Unfortunately, for those of us without I-Tunes, Sirius XM or, for you more mature audience members, CDs

(ARGGGHHHH) . . . we are left with only one option in our quest for Rock and Roll. . . the Garbage Scan by Dave Barry.
```

### Performance text (classify this)

```text
SPEAKER: (Pg 158-162) Monday morning. Bad traffic. Let's just turn on the radio here, see if we can get some good tunes, crank it up. Maybe they'll play some early Stones. Yeah. Maybe they . . .

-POWER ON- ". . . just reached the end of 14 classic hits in a row, and we'll be right back after we . . ."

-SCAN- ". . . send Bill Doberman to Congress. Because Bill Doberman agrees with us. Bill Doberman. It's a name we can trust. Bill Doberman. It's a name we can remem-ber. Let's write it down. Bill . . ."

-SCAN- ". . . just heard 19 uninterrupted classic hits, and now for this. . ."

-SCAN- ". . . terrible traffic backup caused by the. . ."

-SCAN- . . . EVIL that cometh down and DWELLETH amongst them, and it DID CAUSETH their eyeballs to ooze a new substance, and it WAS a greenish color, but they DID not fear, for they kneweth that the. . ."

-SCAN- "(spoken as rapidly as possible) . . . followingisbasedonan500yearleaseanddoesnot-includetaxtagsinsuranceoranactualcarwegetyourhousea ndyourchildrenandyour-kidneys. . ."

-SCAN- "NINE THOUSAND DOLLARS!!! BUD LOOTER CHEVROLET OPEL ISUZU FORD RENAULT JEEP CHRYSLER TOYOTA STUDEBAKER TUCKER HONDA WANTS TO GIVE YOU, FOR NO GOOD REASON. . ."

-SCAN- ". . . Bill Doberman. He'll work for you. He'll fight for you. If people are rude to you, Bill Doberman will kill them. Bill Doberman . , ."

-SCAN- ". . . enjoyed those 54 classic hits in a row, and now let's pause while, . ."

-SCAN- ". . . insects DID swarm upon them and DID eateth their children, but they WERE NOT afraid, for they trustedeth in the. . ."

-SCAN-
". . . listening audience. Hello?"
"Hello?"
"Go ahead."
”Steve?"

"This is Steve, Go ahead."
"Am I on?"
"Yes. Go ahead."
"Is this Steve?"

-SCAN- "This is Bill Doberman, and I say convicted rapists have no business serving on the Supreme Court. That's why, as your congressman, I'll make sure that. . . "

-SCAN- ". . . a large quantity of nuclear waste has been spilled on the interstate, and police are trying to. . ."

-SCAN- ". . . GIVE YOU SEVENTEEN THOUSAND DOLLARS IN TRADE FOR ANYTHING!!! IT DOESN'T EVEN HAVE TO BE A CAR!!! BRING US A ROAD KILL!!! WE DON'T CARE!!! BRING US A CANTALOUPE-SIZED GOB OF EAR WAX!!! BRING US. . .”

-SCAN- ". . . huge creatures that WERE like winged snakes EXCEPT they had great big suckers, which DID cometh and pulleth their limbs FROM their sockets liketh this, 'Pop,' but they WERE not afraid, nay they WERE joyous, for they had. . ."

-SCAN- ". . . just heard 317 uninterrupted classic hits, and now.. ."

-SCAN- "Bill Doberman will shrink your swollen membranes. Bill Doberman has. . ."

-SCAN- ". . . glowing bodies strewn all over the road, and motorists are going to need.”

-SCAN- ". . . FORTY THOUSAND DOLLARS!!! WE'LL JUST GIVE IT TO YOU!!! FOR NO REASON!!! WE HAVE A BRAIN DISORDER!!! LATE AT NIGHT, SOMETIMES WE SEE THESE GIANT GRUBS WITH FACES LIKE KITTY CARLISLE, AND WE HEAR THESE VOICES SAYING. . ."

-SCAN-
"Steve?"
"Yes."
"Steve?"
"Yes."
"Steve?"

-SCAN- "Yes, and their eyeballs DID explode like party favors, but they WERE NOT sorrowful, for they kneweth. . ."

-SCAN- Bill Doberman. Him good. Him heap strong. Him your father. Him. . ."

-SCAN- ". . . finished playing 3,814 consecutive classic hits with no commercial interruptions dating back to 1978, and now. . ."

-SCAN- ". . . the radiation cloud is spreading rapidly, and we have unconfirmed reports that. . ."

-SCAN- ". . . liquefied brain parts did dribbleth OUT from their nostrils, but they WERE not alarmed, for they were.. ."

-SCAN- ". . . getting sleepy. Very sleepy. When you hear the words 'Bill Doberman,' you will . . ."

-POWER OFF- SPEAKER: OK, never mind. I'll just drive. Listen to people honk. Maybe hum a little bit. Maybe even, if nobody's looking, do a little singing. (Quietly) I can't get nooooooo Sa-tis-FAC-shun . . .*
```

---

## IC-2027: Garden Wars

- Title: Garden Wars
- Author (byline): W. Bruce Cameron
- Work: Not specified
- Publisher: Rocky Mountain News
- Publication date as stated: 2003
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 750
- Already set (do not supply): none

### Source block (context only)

```text
Author: W. Bruce Cameron
ISBN: Syndicated Columnist:
Publisher: Rocky Mountain News
Date (Month/Year): 2003
```

### Introduction (context only: never use it for content warnings)

```text
THEME FROM THE VEGGIE TALES:
```

### Performance text (classify this)

```text
SING . . . . . If you like to talk to tomatoes

If a squash can make you smile

If you like to waltz with potatoes

Up and down the produce aisle...

Have we got a show for you!

VeggieTales, VeggieTales, VeggieTales,

VeggieTales . . . . Ok . . . . not really. I mean VeggieTales are OK, but not for a mature high school forensics performance. Instead . . . I’ll stay with the same theme, but instead of Veggie Tales, I present to you (in a loud echoing voice) GARDEN WARS by W. Bruce Cameron . . . .

Copyright 2003 W. Bruce Cameron — Please do not remove the copyright from this essay

It's harvest time, that bountiful season when amateur gardeners such as myself can finally say, "how the heck am I going to get rid of all these vegetables?"

I've got zucchini growing thick as Popeye's forearms out there, bloating past prime because after the zucchini tacos and the zucchini flambé and the zucchini pancakes and the zucchini fondue, no one can even look at another one of the darn things without experiencing squash-induced food disorder. Tomato plants sag like bellhops carrying Ivana Trump's luggage to her room. Wicked peppers drip toward the ground, and potatoes tunnel all over the yard like prairie dogs. I'm overrun.

My children react to their vegetable-enriched meals by making projectile gagging sounds and attempting to foist spoonfuls of zucchini casserole on the dog, who for the first time in her canine life has stopped begging at the table. "I'm a carnivore," my son declares. "I'm not eating anything but meat."

"Meat! Meat!" my children chant.

My neighbor Fred deserves some of the blame-it was he who showed up at my door with a wheelbarrow full of horse manure last spring. "Guess who I've just been talking to?" he trumpeted.

I eyed the foul-smelling cargo. "Our congressman?" I speculated.

"The guy who manages the stables. We can have all the manure we want!" Fred cried gleefully.

"Fred, even with none, I already have all the manure I want," I replied.

Fred explained it was for our gardens, and proceeded to show me how to "work it into the soil." Since I have an aversion to anything with the word "work" in it, I sat in a hammock and watched him, calling out encouragement until I fell asleep.

So now, with my garden going berserk, I load up a grocery bag and head over to Fred's house. "Hey Fred!"

I call when he opens the door to my knock. "I brought you summer squash, some peas, and lots of tomatoes!"

He peers at me. "I already have more than I can eat."

"I really don't care, buddy. I'm your neighbor and I'm sharing the vegetables of my labor. You have to take it."

Fred slams the door.

Okay, no problem. I simply go to his garden and place my excess crops around his own prolific plants. What's a few more onions? He'll hardly notice!

The next day the coward sends his WIFE to my house with some zucchini bread, a case of canned tomatoes, and a host of other thinly-disguised garden delivery systems. I retaliate immediately.

"You can't put vegetables in my mailbox," he complains when he phones. "That's against federal law."

"No it isn't, I put stamps on them," I retort.

"I'm bringing over some cucumber cheesecake," he threatens.

"You do and I'm calling the cops!" I storm.

The next day, I call HIM. "What's with all the stuff in my car?"

"I left you vegetable medley a la grand,'" he explains.

"What? It's a bunch of dirty vegetables in paper bags," I rage.

"Medley a la sack," he amends.

My attempts to retaliate that night by delivering him "salsa verde a la not yet made into salsa" are thwarted. "That BB gun HURT, you jerk," I seethe over the phone. "How did you know I was up by your chimney, anyway?"

"Night vision goggles," he boasts. "Plus, we knew something was going on when the tomatoes started to roll out of the fireplace."

Night vision goggles! See how deranged some people can be? Why would anyone go to such ridiculous lengths over a few vegetables?

Anyone know where I can get a catapult?

So I've had to keep all the outside lights on around my house, in case Fred and his high-tech weaponry are making a sneak attack. I know he's up to something, because he's mad at me for my last salvo. But hey, all I did was SEND the Fed-ex!

HE signed for it.
```

---

## IC-2028: Geek Love

- Title: Geek Love
- Author (byline): Katherine Dunn
- Work: Not specified
- Publisher: Warner Books
- Publication date as stated: Aug 1993
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1845
- Already set (do not supply): none

### Source block (context only)

```text
Author: Katherine Dunn
ISBN: 978-0446391306
Publisher: Warner Books
Date (Month/Year): Aug 1993
```

### Introduction (context only: never use it for content warnings)

```text
Enter the world of the carnival freaks . . . . I’m Olympia Binewski, and this is the story of my family. All of us children were precious to our parents. . . In fact, Mama used to say: "What greater gift could you offer your children than an inherent ability to earn a living just by being themselves?" My family’s story is a raw, insight into the human condition, a glimpse of tormented people who live on the fringe. I’m proud to be a product of Geek Love by Katherine Dunn.
```

### Performance text (classify this)

```text
"WHEN YOUR MAMA WAS the geek, my dreamlets," Papa would say, "she made the nipping off of noggins such a crystal mystery that the hens themselves yearned toward her, waltzing around her, hypnotized with longing. 'Spread your lips, sweet Lil,' they'd cluck, 'and show us your choppers!' "

This same Crystal Lil, our star-haired mama, sitting snug on the built-in sofa that was Arty's bed at night, would chuckle at the sewing in her lap and shake her head. "Don't piffle to the children, Al. Those hens ran like whiteheads." Nights on the road this would be, between shows and towns in some campground or pull-off, with the other vans and trucks and trailers of Binewski's Carnival Fabulon ranged up around us, safe in our portable village.

After supper, sitting with full bellies in the lamp glow, we Binewskis were supposed to read and study. But if it rained the story mood would sneak up on Papa. The hiss and tick on the metal of our big living van distracted him from his papers. Rain on a show night was catastrophe. Rain on the road meant talk, which, for Papa, was pure pleasure.

"Your Mama fluttered around like a dainty bird, and when she caught those ugly squawking hens you couldn't believe she'd actually do anything. When she went right ahead and geeked 'em that whole larruping crowd went bonzo wild. There never was such a snap and twist of the wrist, such a vampire flick of the jaws over a neck or such", champagne approach to the blood. She'd shake her star-white hair and the bitten-off chicken head would skew off into the corner while she dug her rosy little fingernails in and lifted the flopping, jittering carcass like a golden goblet, and sipped! Absolutely sipped at the wriggling guts! She was magnificent, a princess, a Cleopatra, an elfin queen! That was your mama in the geek pit.

"People swarmed her act. We built more bleachers, moved her into the biggest top we had, eleven hundred capacity, and it was always jammed." Papa would half frown, looking down at his hands, quieted suddenly. Feeling the story mood evaporate, one of us children would coax, "What made you quit, Mama?"

She would sigh and look up from under her spun-glass eyebrows at Papa and then turn to where we were huddled on the floor in a heap and say softly,

"I had always dreamed of flying. The Antifermos, the Italian trapeze clan, joined the show in Abilene and I begged them to teach me." Then she wasn't talking to us anymore but to Papa. "And, Al, you know you would never have got up the nerve to ask for my hand if I hadn't fallen and got so bunged up. Where would we be now if I hadn't?"

Papa nodded, "Yes, yes, and I made you walk again just fine, didn't I?" But his face went flat and smileless and his eyes went to the poster on the sliding door to their bedroom. It was old silvered paper, expensive, with the lone lush figure of Mama in spangles and smile, high-stepping with arms thrown up so her fingers, in red elbow-length gloves, touched the starry letters arching "CRYSTAL LIL" above her.

My father's name was Aloysius Binewski. He was raised in a traveling carnival owned by his father and called "Binewski's Fabulon." Papa was twenty-four years old when Grandpa died and the carnival fell into his hands. Al carefully bolted the silver urn containing his father's ashes to the hood of the generator truck that powered the midway. The old man had wandered with the show for so long that his dust would have been miserable left behind in some stationary vault.

My mother, Lillian Hinchcliff, was a water-cool aristocrat from the fastidious side of Boston's Beacon Hill, who had abandoned her heritage and joined the carnival to become an aerialist. Nineteen is late to learn to fly and Lillian fell, smashing her elegant nose and her collarbones. She lost her nerve but not her lust for sawdust and honky-tonk lights. It was this passion that made her an eager partner in Al's scheme. She was willing to chip in on any effort to renew public interest in the show. Then, too, the idea of inherited security was ingrained from her childhood. As she often said, "What greater gift could you offer your children than an inherent ability to earn a living just by being themselves?"

The resourceful pair began experimenting with illicit and prescription drugs, insecticides, and eventually radioisotopes. My mother developed a complex dependency on various drugs during this process, but she didn't mind. Relying on Papa's ingenuity to keep her supplied, Lily seemed to view her addiction as a minor by-product of their creative collaboration.

Their firstborn was my brother Arturo, usually known as Aqua Boy. His hands and feet were in the form of flippers that sprouted directly from his torso without intervening arms or legs. He was taught to swim in infancy and was displayed nude in a big clear-sided tank like an aquarium. His favorite trick at the ages of three and four was to put his face close to the glass, bulging his eyes out at the audience, opening and closing his mouth like a river bass, and then to tum his back and paddle off, revealing the turd trailing from his muscular little buttocks. Al and Lill laughed about it later, but at the time it caused them great consternation as well as the nuisance of sterilizing the tank more often than usual. As the years passed, Arty donned trunks and became more sophisticated, but it's been said, with some truth, that his attitude never really changed.

My sisters, Electra and Iphigenia, were born when Arturo was two years old and starting to haul in crowds. The girls were Siamese twins with perfect upper bodies joined at the waist and sharing one set of hips and legs. They usually sat and walked and slept with their long arms around each other. They were, however, able to face directly forward by allowing the shoulder of one to overlap the other. They were always beautiful, slim, and huge-eyed. They studied the piano and began performing piano duets at an early age. Their compositions for four hands were thought by some to have revolutionized the twelve-tone scale.

I was born three years after my sisters. My father spared no expense in these experiments. My mother had been liberally dosed with cocaine, amphetamines, and arsenic during her ovulation and throughout her pregnancy with me. It was a disappointment when I emerged with such commonplace deformities. My albinism is the regular pink-eyed variety and my hump, though pronounced, is not remarkable in size or shape as humps go. My situation was far too humdrum to be marketable on the same scale as my brother's and sisters'. Still, my parents noted that I had a strong voice and decided I might be an appropriate shill and talker for the business. A bald albino hunchback seemed the right enticement toward the esoteric talents of the rest of the family. The dwarfism, which was very apparent by my third birthday, came as a pleasant surprise to the patient pair and increased my value. From the beginning I slept in the built-in cupboard beneath the sink in the family living van, and had a collection of exotic sunglasses to shield my sensitive eyes

Despite the expensive radium treatments incorporated in his design, my younger brother, Fortunato, had a close call in being born to apparent nor-malcy. That drab state so depressed my enterprising parents that they immediately prepared to abandon him on the doorstep of a closed service station as we passed through Green River, Wyoming, late one night. My father had actually parked the van for a quick getaway and had stepped down to help my mother deposit the baby in the cardboard box on some safe part of the pavement. At that precise moment the two-week-old baby stared vaguely at my mother and in a matter of seconds revealed himself as not a failure at all, but in fact my parents' masterwork. It was lucky, so they named him Fortunato. For one reason and another we always called him Chick.

"Papa," said Iphy. "Yes," said Elly. They were behind his big chair, four arms sliding to tangle his neck, two faces framed in smooth black hair peering at him from either side.

"What are you up to, girlies?" He would laugh and put his magazine down.

"Tell us how you thought of us," they demanded.

I leaned on his knee and looked into his good heavy face. "Please, Papa," I begged, "tell us the Rose Garden."

He would puff and tease and refuse and we would coax. Finally Arty would be sitting in his lap with Papa's arms around him and Chick would be in Lily's lap, and I would lean against Lily's shoulder while Elly and Iphy sat cross-legged on the floor with their four arms behind them like Gothic struts supporting their hunched shoulders, and Al would laugh and tell the story.

"It was in Oregon, up in Portland, which they call the Rose City, though I never got in gear to do anything about it until a year or so later when we were stuck in Fort Lauderdale."

He had been restless one day, troubled by business boondoggles. He drove up into a park on a hillside and got out for a walk. ''You could see for miles from up there. And there was a big rose garden with arbors and trellises and fountains. The paths were brick and wound in and out." He sat on a step leading from one terrace to another and stared listlessly at the experimental roses. "It was a test garden, and the colors were. . . designed. Striped and layered. One color inside the petal and another color outside.

"I was mad at Maribelle. She was a pinhead who'd been with your mother and me for a long while. She was trying to hold me up for a raise I couldn't afford." The roses started him thinking, how the oddity of them was beautiful and how that oddity was contrived to give them value. "It just struck me-clear and complete all at once – no long figuring about it.” He realized that children could be designed. “And I though to myself, no that would be a rose garden worthy of a man’s interest!”

We children would smile and hug him and he would grin around at us and send the twins for a pot of cocoa from the drink wagon and me for a bag of popcorn because the red-haired girls would just throw it out when they finished closing the concession anyway. And we would all be cozy in the warm booth of the van, eating popcorn and drinking cocoa and feeling like Papa's roses.
```

---

## IC-2029: George Carlin’s Guide to Dining Out

- Title: George Carlin’s Guide to Dining Out
- Author (byline): George Carlin
- Work: Brain Droppings, Pgs 8-13
- Publisher: Hyperion Press
- Publication date as stated: May 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, GUY, CUSTOMER, WORKER, WAITER
- Teaser before the introduction: Yes
- Spoken words (computed): 1282
- Already set (do not supply): none

### Source block (context only)

```text
Author: George Carlin
Book: Brain Droppings, Pgs 8-13
ISBN: 978-0786863136
Publisher: Hyperion Press
Date (Month/Year): May 1997
```

### Introduction (context only: never use it for content warnings)

```text
Let’s face it. The American public is in LOVE with eating out. Some studies have shown the average American eats out 4 to 5 times a week. How many other “pleasurable” activities does the average adult engage in 4 to 5 times a week?

Food is IMPORTANT but enjoying yourself during the dining experience is also important. In the true nature of fun, I offer you George Carlin’s Guide to Dining Out (may he rest in peace)
```

### Performance text (classify this)

```text
NARRATOR: Are you a fan of restaurant chains? I’m not. Every now and then I get a Waffle House attack, and I have to get something scattered and smothered, but I don’t make a habit of it. After all, Applebee’s slogan of Eatin’ Good in the Neighborhood takes on a whole new meaning when you think about the fact that they have 2,000 locations. Then of course there is Olive Garden whose food is about as Italian as Taco Bell is Mexican. And last but not least, there is my beloved IHOP, where you can be convinced that pancakes with dripping strawberry syrup and whipped cream is a healthy dinner any day of the week!

(Excerpted from Restaurant Menus Recreated to be Honest by Diana Adams https://bitrebels.com/entertainment/restaurant-menus-recreated-to-be-honest-humor/ )

NARRATOR: (Pg 8-13) There are certain clues that tell you how much a restaurant will cost. If the word cuisine appears in the advertising, it will be expensive. If they use the word food, it will be moderately priced. However, if the sign says eats, even though you'll save some money on food, your medical bills may be quite high.

I don't like trendy food. When I hear, "sauteed boneless panda groin," I know I'm in the wrong place. There's such a thing as pretentious food. Puree of woodchuck, marinated bat nipples, weasel chops, porcupine cacciatore. Or fried eagle. A guy said to me recently,

GUY: C'mon, we'll go to Baxter's, they have really great fried eagle."

NARRATOR: I'm thinkin' to myself, "Do I really wanna know this guy?" However, if you are going to dine with pretentious people, here are some items you can order that are sure to impress (each said with a different affectation): • gorilla fondue, • filet of hyena, • jackal tartare, • rack of prairie dog, • free-range mole en brochette, • wolf noodle soup, • loin of chipmunk, • koala flambe, and • wombat souvlaki Then, at the other end of the spectrum, there is the decidedly non-trendy restaurant, where the special sometimes is simply "meat." Big sign in the window: "Today's special: Meat."

CUSTOMER: I'll have the meat.

WORKER: Would you like sauce with that?

CUSTOMER: What kind of sauce would that be?

WORKER: That would be meat sauce.

NARRATOR: It's similar to a fish sandwich. Have you ever seen these places that feature "fish sandwiches"? I always think, "Well, that's kind of general." I mean, I wouldn't order something called a "meat sandwich," would you?" At least not without a couple of follow-up questions:

CUSTOMER: Does anyone know where this meat came from? . . . Are any of the waitresses missing?

NARRATOR: I think when you eat out you should have a little fun; it's good for digestion. Simple things. After the waiter recites a long list of specials, ask him if they serve cow feet. But act really interested in the specials. When he says,

WAITER: Today we have goat-cheese terrine with arugula juice, sauteed cod with capers and baby vegetables, coastal shrimp cooked in spiced carrot juice, roast free-range chicken with ginger and chickpea fries, and duck breast in truffle juice.

NARRATOR: Act like you're completely involved. Say,

CUSTOMER: The cod. What is the cod sauteed in?

WAITER: A blend of canola and tomato oils.

CUSTOMER: (No hurry here.) Ahhh, yes! (pointing thoughtfully at the waiter) I'll have the grilled cheese sandwich.

NARRATOR: Even some low-end places are pretentious. The menu can't merely say "cheeseburger." They have to get wordy. So, go along with them. When you order your food use their language. But you must look right at the waiter; no fair reading from the menu. Look him in the eye and say . . .

CUSTOMER: I'll have the succulent, fresh-ground, government-inspected, choice, all-beef, six-ounce patty on your own award-winning sesame-seed bun, topped with a generous slice of Wisconsin's finest Grade-A cheddar cheese made from only premium milk and poured from large, galvanized steel cans, having originally been extracted from a big, fat, smelly, champion blue-ribbon cow with a brain disease.

NARRATOR: Continue that style with other items: Instead of asking for a glass of water, say you'd like a . . .

CUSTOMER: cylindrical, machine-blown, clear drinking vessel filled with nature's own colorless, odorless, extra-wet, liquid water.

NARRATOR: Have fun. Be difficult. Order unusual things: a chopped corn sandwich. Rye potato chips. Filet of bone with diced peas. Peanut butter and jellyfish. Ask for a glass of skim water. Insist on fried milk. Chocolate orange juice. Order a grilled gorgonzola cheese sandwich on whole-wheat ladyfingers. Then top the whole thing off with a bowl of food coloring and a large glass of saturated fat.

Issue special instructions. Ask for the French toast, medium rare. Get a pizza with no toppings, hold the crust. Tell 'em you want eggs: "Fry the whites and poach the yolks." Order a basket of poppy seed rolls and tell them to scrape off the seeds and put them in a separate bowl and heat them to 200 degrees. Keep them busy.

Tell your waiter you want to make a substitution: "Instead of my napkin, I'll have the lobster tails." See what he says. Ask him if the garnish is free. If it is, tell him all you're having is a large plate of garnish. If they have a salad bar, ask how many times you can go back. If they say as many times as you like, ask for a lawn bag. Come back the next day with a small truck. Tell them you weren't quite finished eating the night before. You're actually within your legal rights, because, technically, no one is ever finished eating.

Ask him if the chef would mind preparing a dish that's not on the menu. Then describe something simple but unusual. Like half a coconut filled with egg whites. When the waiter comes back and says,

WAITER: Yes, the chef said he will be delighted to make that for you . . .

NARRATOR: Tell him, "Well, never mind, I don't like that anymore.” When the food arrives, change your mind. Say. . .

CUSTOMER: I've changed my mind, waiter. Instead of the roast suckling pig, I believe I'll have a half order of Kellogg's Product 19.

NARRATOR: And always, when the food arrives, send something back. It's considered very sophisticated. But make sure you use colorful language. Tell him . . .

CUSTOMER: Waiter, this veal tastes like the inside front panel of Ferdinand Magellan's shorts. And I'm referring to the first voyage.

NARRATOR: Show him you're a man of new ideas. When he comes with the pepper mill . . . Actually, the pepper mill can be a source of great fun. Keep the waiter going on the pepper mill for a long time. Disturbingly long. Until everyone in the restaurant is really uncomfortable. Then, when your food and silverware are completely covered with a thin layer of ground pepper, say . . .

CUSTOMER: Okay, stop! That's perfect!

NARRATOR: Then, a few minutes later, call the waiter over and tell him . . .

CUSTOMER: This food has way too much pepper on it!

NARRATOR: Now that you have your food, the waiter can begin to ask you if everything is all right.

WAITER: Is everything all right?

CUSTOMER: Yes. Thank you. Good-bye!

NARRATOR: Usually, when they ask if everything is all right, tell them the truth. Say . . .

CUSTOMER: Well, I had a problem with the peas. I received 143 peas. Of them, 36 were overcooked, 27 were undercooked, and 18 were not quite the same color as the others.

NARRATOR: Or tell them more than they really want to know.

CUSTOMER: No, everything is not all right. I'm going through a period of upheaval. I have a rogue polyp in my bowel, my wife ran off with a periodontist, and my son has been arrested for defecating in a mall.

NARRATOR: And always fill out the "How did we do?" card. It's very helpful to the owner.

CUSTOMER: (writing on the comment card) Everything was wonderful, except the waiter had some vomit on his shoes and a tiny snot on the end of his nose. It was small, but it was definitely a snot.
```

---

## IC-2030: The Giant’s Tooth

- Title: The Giant’s Tooth
- Author (byline): Bruce Coville
- Work: Odds are Good
- Publisher: Magic Carpet Books
- Publication date as stated: March 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MEAGAN, EDGAR
- Teaser before the introduction: Yes
- Spoken words (computed): 2177
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bruce Coville
Book: Odds are Good
ISBN: 978-0152057169
Publisher: Magic Carpet Books
Date (Month/Year): March 2006
```

### Introduction (context only: never use it for content warnings)

```text
The Giant’s Tooth by Bruce Coville
```

### Performance text (classify this)

```text
EDGAR TWONKY had no intention of getting eaten by a giant the morning he left for Cottleston Fair. Sometimes these things just happen. He was ambling along, humming tunelessly, when an enormous hand swept down from the sky, scooped him up, and deposited him in a mouth the size of a cave. The tongue on which he landed was coarse and soggy, like a bed of rain-soaked ferns. It flung him toward the back of the mouth, where a vast bulb of red flesh dangled above the gaping black hole that would, Edgar presumed, be the last thing he ever saw. With a leap, Edgar grabbed the dangling piece of flesh. It was moist and slick, and far too wide for him to put his arms around. Digging his fingers into the soft surface, he hung on for dear life. "Gunnarrrgh.” said the giant. "Gunnarrrgh.”

Edgar's grip was loosening, and he was expecting to fall into the waiting hole at any second, when he heard a creaky voice call, "Over here! Hurry!" Edgar flung himself forward, landing on the giant's tongue once more. The great pad of flesh rippled alarmingly as the giant tried to swallow him.

MEAGAN: Come on, come on! I can't hold this out here forever. It'll make him sneeze, which will almost certainly kill you! Reaching forward, Edgar grabbed another handful of tongue and pulled himself along the rough surface. He dragged himself hand over hand toward the beckoning torch, when the giant made a last desperate attempt to swallow him. "Gak gak gak.” hacked the giant. Edgar leaped forward, landing within a foot of the torch. A withered hand reached out to him. He grabbed it thankfully and was pulled into the most astonishing room he had ever seen. Well, it wasn't a room, exactly. It was the inside of one of the giant's back teeth. But the flickering light of the torch showed that it had been hollowed out to make an area large enough to hold a table and two chairs and a clutter of items that covered both floor and table: cups, plates, knives, pitchforks, shovels, coils of rope, chunks of wood, and an old wagon wheel, among other things. "Salvage," wheezed a voice behind him. Edgar turned and received yet another surprise. His rescuer was a woman.

MEAGAN: By salvage, I mean the stuff in the room, not you. First time since I've been here that I've actually been able to save someone. Silly things all panic and slide down his gullet before I can do a thing to help them. That was very good, the way you managed to grab on to something. Quick thinking. I like that in a man.

EDGAR: (nervously) Thank you. (looking around) How long have you lived here?

MEAGAN: (shrugging) Can't really say. It's hard to keep track of the time in here. (stroking her hair, sadly) I do know I was young when he took me. Young and pretty, some thought. And my hair was black as a raven's wing. Now come on, ducky. Sit down, sit down. I haven't had a visitor in . . . well, ever, actually. (flipping hair over shoulder) My name is Meagan.

EDGAR: And I'm Edgar. How do you live here, anyway? Where do you get your food?

MEAGAN: (shrugging) I scavenge. Anything that comes along that doesn't go down his gullet. I've dug bits of meat out of his teeth that would feed a family of ten. Edgar shuddered, and decided not to ask what she did for water. He was afraid he already knew the answer. He leaped ahead to the bigger, more important question. "Have you ever tried to get out?"

MEAGAN: (bitterly) What do I look like? Of course I've tried to get out. I tried every way I could think of. Finally, when it became clear I wasn't going to make it, I gave up and accepted my fate. With every flash of light that came when the giant opened his mouth, I took stock of where I was. Many was the hour I spent huddled in this tooth, weeping to myself, wondering what was to become of me. But I never gave up. I drank from pools of spit. I snatched passing food. And when I found my first tool, I began to dig, to make myself a home. Chip, chip, chip, I picked away at this tooth. (pause, chuckles) He didn't like that, I can tell you. Oh, the roars of pain! I thought I would go deaf. (Beat) Did I try to get out? Of course I tried to get out. But in the end, I made myself a home here. Night inside the giant's tooth came in two stages. The first was when the giant himself lay down to rest, which changed the floor into a wall, and the rear wall into the floor. Stage two came when Meagan decided to put out the torch. As he lay in the dark, wrapped in misery, Edward finally did drift into a fitful slumber-only to be jolted back into wakefulness by a deep rumble, something like a cross between a thunderstorm and an avalanche. (Sound of giant snoring, ending in 3 peeps)

EDGAR: (horrified) What was that?

MEAGAN: (groggily) What was what?

(Sound of giant snoring, ending in 3 peeps)

EDGAR: That!

MEAGAN: (snarling) It's just the giant, snoring. Forget it and go back to sleep. He was still wide awake, though completely exhausted, when Meagan lit the torch again. Only a few moments later the giant groaned and lurched to his feet, causing everything that had fallen to the wall the night before to return to the floor.

MEAGAN: I've been thinking, and I've decided that you're going to have to build a home of your own. This place really is too small for the two of us. Odds are good I'd end up killing you. Edgar, who was still determined to think of this as a temporary situation, felt that digging out his own home would be a waste of time and energy.

EDGAR: (snarling whine) Where do you suggest I make this home.

MEAGAN: (snapping) Well, he has nearly thirty more teeth to choose from! However, I'd suggest you stick with the molars. They're roomier. And so, after a breakfast so gray that Edgar decided he didn't really want to know what it consisted of, they left Meagan's home to search for a tooth where he could live. The giant's tongue, pulsating beside them like a pink and fleshy whale, was a constant danger. Even worse, when they first started out they had to dodge into the gap between Meagan's tooth and the next one while the giant poked at their hiding spot with the tip of his tongue, as if he was trying to dislodge an irritating bit of food that had become stuck there. It was a humbling thought for Edgar to realize that "an irritating bit of food" was, in fact, precisely what he had become. The tooth directly next to Meagan's was strong and solid, with no obvious place for Edgar to begin excavating a home. The one next to that, however-the tooth farthest back in the giant's mouth-had a hole twice the size of Edgar's fist. The odor of decay hung rank about it, but Meagan said that would disappear when Edgar had cut away the rot. Before Meagan would let him start to work, she bound them both to the tooth with a combination of ropes and leather straps. Edgar swung the pick and knocked away a chunk of the yellowed enamel. The outraged roar of pain that rose from deep within the giant nearly deafened him. Edgar almost felt sorry for the giant. Then he reminded himself that the only reason the creature was suffering this way was because it had tried to eat him. The outer coating of the tooth was hard but brittle, and broke away fairly easily. After about four feet, the material changed to something dense and yellow, and tougher to work with the pick.

Finally the time came when the excavation in the tooth was big enough for Edgar to take up his home in it. He moved his things-that is, the two or three items Meagan had given him, as well as a pitchfork (the single thing he had managed to snag on his own)-to his new abode. While he continued work on his new dwelling, Meagan taught him how to snatch things from the tide of food and rubble that poured down the giant's throat three times a day. When she "went fishing," as she called it, she first secured a safety rope about her waist, anchoring the other end of the rope to one of the chairs inside her tooth. Normally she pulled things in with the help of a long pole that had a hook on one end. But if something particularly good came rushing past that was too far out on the tongue for her to snag simply by leaning for it, she would fling her whole body onto the surface of the tongue, then use the rope to haul herself back. Once Edgar was truly settled, he began to explore the giant's mouth in search of a way out.

Though he did not tell Meagan this was what he was doing, he suspected she was able to guess. Not that it made any difference. He could find no way of escape. It was like being at the bottom of a well: easy enough to fall in, impossible to climb out. Edgar continued his explorations, until he had at last reached the most distant of the giant's molars. He carried a torch with him, which he lit and waved to Meagan when he reached the far side. When he returned from that trip, he was burning with a new idea.

EDGAR: If we string a rope directly across the center of his mouth, we might have better luck snagging things as they go by.

MEAGAN: Might work. Just how good an idea became clear as the weeks rolled on and they were able to retrieve more and more items. The most unexpected of these items was a young man named Charles, whom Edgar snatched from certain doom by hanging upside down from the rope and reaching out to him.

During Edgar's second year in the giant's mouth, they rescued Farley. Next to be pulled to safety, about six months later, were a pair of sisters, named Babette and Cleo, and their dim-witted brother, Herbert. The time had come to begin building homes in the teeth on the other side of the mouth. Babette and Cleo chose to live together. Herbert took the tooth above them. Before too many more years had passed, a thriving community had risen in the giant's mouth. Edgar was elected mayor of Giant's Mouth Township. They gave him a jeweled scepter, which they had managed to retrieve one afternoon when the giant swallowed a king. (They had tried to save the king, too, of course, but his grip was weak and flabby, and he had not been able to hold on when Herbert reached out to him.) Many was the night Edgar sat in his tooth and looked out the window he had carved on the tongueward side, feeling warm and cozy at the sight of the lights twinkling on the other side of the giant's mouth. In this way, the years rolled on. And then, one afternoon while he was setting a rope, Edgar was suddenly yanked from the giant's mouth. It happened because the giant, who was in a foul mood that day, became particularly irritated by the feeling of things moving in his mouth. Edgar was stringing a rope across the roof of the giant's mouth in order to do some salvage work when the giant reached in and began to scratch at the roof of his mouth. Though the rope was less to him than a silk thread would be to a human, it caught on his fingernail. When he pulled his hand out, one end of the rope came free-and with it, still clinging to the end, came Edgar. As he hurtled out of the giant's mouth, two things caused Edgar to blink. The first was the unexpected brightness of the sun, which he had not seen except at a distance for so many years. The second was the horrifying distance that separated him from the ground. Knowing he could not keep his grip on the saliva-slick rope, Edgar made a desperate leap and landed on the giant's collar. The giant swatted at him, as one would at an annoying insect, but Edgar quickly scrambled under the giant's collar, where he held as still as he could, scarcely breathing. Finally night darkened the sky, bringing with it the stars that he had not seen in so many years. Their beauty made him weep. The giant lay down, and after a time began to snore. Edgar climbed out onto his chest. He stood, staring out at the rising moon, the river on whose water it was reflected, the dark ridge of the distant mountains, and the road that led back to his village. Then he began to climb the giant's shirt-not down, but up-onto the giant's chin, where the stubble grew so thick it was like a grove of small pine trees. Across the loose and pendulous lip Edgar climbed. Then he lowered himself back into the moist cavern of the giant's mouth, where his home and friends lay waiting.
```

---

## IC-2031: Gifted

- Title: Gifted
- Author (byline): Simon Rich
- Work: Spoiled Brats
- Publisher: Back Bay Books
- Publication date as stated: May 2015
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1690
- Already set (do not supply): none

### Source block (context only)

```text
Author: Simon Rich
Book: Spoiled Brats
ISBN: 978-0316368650
Publisher: Back Bay Books
Date (Month/Year): May 2015
```

### Introduction (context only: never use it for content warnings)

```text
It's a natural instinct to want to help your child. After all, that's what parents do: We protect and support our children until they are ready to go out on their own. But these days some parents are defining "protect" and "support" a little differently than usual. And the definition of when kids are ready to be on their own has gotten fuzzy, too.

Compound this social phenomenon with being the parent of a differently-abled child, author Simon Rich and you get a short story rife with hyperbole entitled . . . . Gifted
```

### Performance text (classify this)

```text
When the nurses handed me my son, I couldn’t believe how perfect he was. Ben was so robust, nearly fifty inches tall, including horns and tail. Even the doula was impressed.

“My God,” she said. “My holy God in heaven.”

Alan and I knew instantly that our child was exceptional. He was just so adorable, with his pentagram birthmark and little, grasping claws. His red eyes gleamed with intelligence. When the doctors came in with all their charts, they just confirmed what we already knew. Our child was “one of a kind” and “unlike any creature born of man.”

Alan and I were ecstatic – but also a little bit nervous. Raising a gifted child is a huge responsibility. We vowed then and there that we would do all we could to ensure he achieved his full potential.

The first step was getting him into the right preschool. We figured it would be a breeze, given Ben’s obvious star quality. But, to our great surprise, he struggled. At Trevor Day, a teacher asked him how old he was. Instead of saying “three,” he pinned her to the ceiling with his mind. We were able to get him an interview at Trinity, thanks to a family connection. But when Ben saw the crucifix in the lobby, his eyes turned black and the walls wept blood. Why was Ben behaving this way?

There was only one logical explanation: attention deficit disorder. We took him to a specialist on Park Avenue, and within five minutes our son had his first prescription for Ritalin.

At first Ben wouldn’t take his pills. Padma, our nanny, had to chase him for hours around the apartment, blowing incense in the air to try to scare him down from the ceiling. Within months, though, Ben got used to his medication. He became calmer, more alert, and far less murderous. He was a real joy to be around.

In some ways, Ben still lagged behind most children. He spoke only one word: arrgh. And he was unable to tie his shoes or blink his eyes. We didn’t care, though. Because, by the age of five, he’d finally found an outlet for his gifts. Art!

Ben always had a creative temperament. He could grip crayons by his second birthday (which is very rare), and by the age of six he was drawing every day. His favorite colors were black and red. Sometimes, while composing a sketch, he would become so excited that his crayon would break apart in his claws and he would start to ram his horns against the wall as noxious steam emitted from his ears. If Ben’s art supplies were taken from him, he would respond with so much violence that Padma would have to subdue him, using one of the sleeper holds she’d learned. It didn’t take long for Alan and me to realize we had a true artiste on our hands.

We decided to enroll Ben at Dalton, because of its emphasis on creativity. I wasn’t going to let Ben’s talent go to waste at some cookie-cutter public school where every child is forced into the same dull mold. I wanted him to have a chance to find himself.

Ben’s time at Dalton was not without incident. He’s incredibly unique – every teacher said so. But his creativity could sometimes be a burden. If a subject didn’t ‘grab’ him, he would have trouble focusing – and instead create a game of his own design. For example, in fifth grade, a teacher asked him to calculate the area of a four-by-six-foot rectangle. Instead of multiplying four by six, as a typical child might have done, Ben crab-walked across the ceiling and blinded the teacher with a fire stare. The incident was very traumatic for our son. Alan and I decided it was time to reexamine his treatment.

After consulting with our specialist, we chose to switch Ben from Ritalin to Focalin, which is a slightly stronger medicine. We also hired Han Cho, an astrophysics PhD candidate at Columbia, to tutor Ben five days a week after school.

The sad truth is, our world is just not designed for differently abled children. Many assignments at Dalton require the use of pencils, which Ben cannot hold in his claw. Other projects involve calculators, which Ben considers food, or the use of English, which Ben cannot speak. Enlisting Han allowed Ben to complete his assignments at his own pace and in a way that showcased his distinct gifts.

Ben’s grades soon improved. We were so grateful to Han for unlocking our son’s potential. Once, they were studying vocab by the pool when I heard a loud splashing noise. When I went outside to check on them, Ben was holding Han upside down by the ankles and growling with delight.

“Help!” Han shouted, playing along with Ben’s game. “I’ve lost control! I’ve lost control!”

When Ben turned thirteen, we knew it was time to start thinking about college. We met with a number of counseling firms. They helped us structure a four-year strategy for Ben that would demonstrate his skill set – and we followed the plan to the letter. By the time Ben was a senior, his résumé was absolutely glittering. He’d received five participation gavels from Model UN, been elected tri-captain of the Dalton golf team, and contributed numerous drawings to the school’s Fine Arts Magazine. His GPA was a respectable 1.4, and even though he’d accidentally eaten several sections of his SAT he still managed to notch a 420.

Despite all of Ben’s achievements, he did not seem excited about college. He’d spend hours in his room, playing violent video games. The only time I’d see Ben was late at night, when he’d emerge from his room to raid the fridge for Popsicles. I worked to take advantage of these ‘sightings’ as best I could. But when I tried to engage him in conversations about his future, he replied in typical teenage fashion, with a series of shrugs, grunts, and monosyllables.

“Do you want to go to a big school or a small school?”

“Arrgh.”

“Do you want to be in a city or in the country?”

“Arrgh.”

“Would you prefer lecture classes or seminars?”

“Arrgggh!!!!”

It was exasperating. In the end, we were able to persuade Ben to apply early to Bard. Alan and I had taken him there on a college tour and we were so impressed that we donated several tennis courts to their campus. When Ben was accepted, Alan and I were beside ourselves! But Ben wasn’t as thrilled as you’d expect. Here he was, accepted into his dream school, and his smile was so faint I could barely see his fangs. It was obvious what had happened: Ben had burned out.

We met with Ben’s psychiatrist and decided it would be best for him to take a ‘gap year’. The only question was: where would Ben go? It was difficult to decide. He had his heart set on Transylvania, which I found baffling. (Italy would make more sense, since it has such a grand artistic tradition.) In the end, we compromised. Ben would spend two weeks on his own in Transylvania, as a reward for all his hard work. Then he’d spend six months at a wonderful program I found in Costa Rica that builds eco-friendly houses for the poor.

When Ben returned from his time abroad, he was a changed man. He had a swagger to his step and a confidence I’d never seen before. Part of me wondered if he’d maybe met a girlfriend overseas, but I knew better than to ask. If there’s one thing I’ve learned from my years as a parent, it’s that the mother is always the last to know!

Unfortunately, though, Ben had trouble adjusting to college. He thrived within his major, creating dozens of ‘splatter’ paintings in the Abstract Expressionist tradition. But he had difficulty with his core curriculum courses. Once, during a Spanish midterm, he escaped into the Hudson Valley woods and lived as a beast for several months, taking residence in a cave and eating neighborhood pets to survive. The local authorities were able to subdue him. And, thankfully, they turned him over to the Bard police, so that his outburst could be handled internally by the school. But the event was traumatic for Ben, and I decided it would be best for him to take a semester off. We also got him a prescription for Adderall, which is a slightly stronger medicine than Focalin.

It took nearly seven years, but Ben eventually earned his BA in painting. I’ll never forget how handsome he looked on the podium, with his cute little horns poking out through his mortarboard. No sooner had he snatched his diploma, though, than my heart began to race. All I could think was, What now?

We got him a prescription for Kilmax, which is a slightly stronger medicine than Adderall. Then, on a rainy February morning, I sat down with him to talk about his future. As usual, it was difficult for us to connect.

“Would you like us to rent you your own artist’s studio in Williamsburg?”

“Arrgh.”

The Kilmax, I noticed, had produced several troubling side effects. Ben’s eyes – usually so bright and searing – had dimmed to a pale ocher. His horns were pointed downward and his fur was falling out in clumps. I was telling him about another option – the birthright trip to Israel – when he suddenly held up his claw, cutting me off midsentence.

“No… more.”

I screamed for Alan, and he came running. “Ben spoke!” I cried. We leaned in toward our son, keeping as still as possible. Ben gasped a few times, obviously struggling. Eventually, though, he managed to continue.

“No more… arrrrrgh! Pleeeeeaseeeearrrrrgh! Me… not… sick. Me… arrrrrrrgh! Monster. Let… be… monster. Let be monster.”

My eyes filled with tears. I’d always assumed that Ben would never talk – and now here he was, carrying on a full conversation! If Ben could master language, there was no limit to what he could achieve. I whipped out my iPhone and typed in Han’s number from memory.

It was time to start thinking about law school.
```

---

## IC-2032: The Goblins

- Title: The Goblins
- Author (byline): A.J. Jacobs
- Work: Fractured Fairy Tales
- Publisher: Bantam Books
- Publication date as stated: Nov 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1078
- Already set (do not supply): none

### Source block (context only)

```text
Author: A.J. Jacobs
Book: Fractured Fairy Tales
ISBN: 978-0553099805
Publisher: Bantam Books
Date(Month/Year): Nov 1997
```

### Introduction (context only: never use it for content warnings)

```text
One of the most successful and beloved of Victorian fairy tales, George Macdonald’s The Princess and the Goblin tells the story of young Princess Irene and her friend Curdie, who must outwit the threatening goblins who live in caves beneath her mountain home.

This version of the story by A.J. Jacobs – simply called “The Goblins” modifies the original a bit to fit the format of what the world has come to know as “Fractured Fairy Tales” If you ever watched the Rocky and Bullwinkle show on Saturday mornings as a child, you may remember this one!

The Goblins by A.J. Jacobs
```

### Performance text (classify this)

```text
A long, long, long time ago, a little kingdom sat perched on top of a high mountain. The king of the kingdom was constantly trying to raise money for things he thought the country needed. Like, for instance, another robe for the king.

“That robe-the one with the lion fur around the collar?" the king told his prime minister. "Got to have it. I'll have to levy another tax on the little people."

"But we already have a tax on everything, Your Majesty," said the prime minister. "What can you tax them for?"

"Easy! I'll just tax them for being little people." And so the king levied a tax on all people under four feet six. Problem was, there weren't that many people that little. Matter of fact, only one family in the kingdom was under four feet six. The Goblins. And they didn't like it a bit.

"We may not have height, but we got heart!" father Goblin told the tax collector who banged on his door. "We may not have altitude, but we got attitude. We may not have-"

"All right, I got the point," said the tax collector. "But if you're going to live on this mountain, you gotta pay the tax."

"Well, then," said the goblin, "we won't live on the mountain. We'll live in the mountain."

And with that, the entire Goblin family entered a hole in the side of the mountain and slammed the door shut, vowing to come out only on moonlit nights to try to get the big people. But as we said, that was a long, long, long time ago. After many years passed by, the kingdom entered the era officially known as a long time ago. (We'll skip the era called a long, long time ago.) Anyway, a long time ago, the goblins still lived inside the mountain and still sallied forth to try to get people. Although, it should be said they had never actually gotten a person, and wouldn't really know what to do if they did.

The reason the goblins had never actually got-ten someone was that they had a weakness: poetry. Repeat a couple of lines-something like "One, two, buckle my shoe, three, four, shut the door"-and the goblins were stopped cold. Repeat a couple more lines-for instance, "I should have been a pair of ragged claws scuttling across the floors of silent seas"-and the goblins ran away, screaming.

One day, the new king was teaching his daughter, Irene, the facts of life.

"And remember, the goblins will get you if you don't watch out!"

"Oh, yeah?" said Irene. "Have you ever seen a goblin?"

"Umm, no, but ... "

"Well, how do you know there are even such things as goblins? Is that a goblin?" asked Irene, pointing to a red couch.

"No, but-"

"Is that a goblin?" asked Irene, pointing to a brass candlestick.

"Um, no."

"Is that a goblin?" asked Irene, pointing to a little, four-foot, three-inch man with an evil glint in his eyes.

"Why, yes," said the king. "I believe that is a goblin."

And with that, the goblin began chasing Princess Irene around the castle and out the door and over the moat and into the kingdom.

"l'm gonna get you!" the goblin cackled.

"I don't want to be got! I don't want to be got!" shouted Irene.

Things looked bad for the princess until she bumped into a young miner named Curdy, and he was so struck by the princess's beauty that he was moved to poetry.

"Oh, Princess fair," said Curdy. "Your golden hair. Upon your head. I see it there."

And of course, that stopped the goblin in his tracks, for he just couldn't stand poetry.

"You saved me with your poem," said the grateful princess to the miner. "Are you a handsome prince in disguise?"

"No, I'm just a miner boy," said the ever-modest Curdy. "Although for a lonely miner, I'm quite courageous and have excellent hygiene."

"Oh," said the crestfallen princess. "Couldn't you go somewhere to learn to be a prince?"

"Like where?" asked Curdy. "How 'bout Princeton?"

Oooof. That kind of talk makes the poetry seem appealing. Anyway, little did the princess know that the goblin who had chased her was himself a prince, the Prince of Goblins, and that he was determined to make her his bride. And so a pack of goblins-led by Prince Goblin-burrowed underneath the mountain precisely to the spot where the princess was, and popped up.

Actually, they made a slight miscalculation. They popped up in the middle of a croquet court. Af-ter a hasty retreat and a couple of aspirin (those croquet mallets aren't made of rubber, you know), the goblins tried again. They popped up and grabbed the princess! Well, actually, there was another slight miscalculation. They grabbed the hygienic miner instead.

"You fellows have made a terrible mistake," protested Curdy, as he was dragged into the moun-tain. "l'm Curdy!"

"You sure are, hun!" giggled the prince, not knowing what curdy meant, but thinking it sounded rather appealing.

So Curdy figured he would just recite a poem and make these goblins disappear. But without the princess to inspire him, Curdy couldn't think of a sin-gle rhyme. He could only think of words like orange. And month.

In no time at all, Curdy found himself in a very embarrassing position. Namely, standing next to Prince Goblin, dressed in a bridal gown.

"Do you take this earthling to be your lawful wedded wife?" a four-foot, two-inch minister asked the prince.

"Um, could you give me a second on that one?" requested the prince. "She looks a bit different than I remembered her." The prince decided to take Curdy out into the daylight for a closer look. Out they popped and who should Curdy see just outside the hole, but the princess herself. Finally inspired, Curdy burst into verse.

"What a gladsome fine surprise, to see you with mine eyes," he recited.

The prince winced and cupped his ears.

"I love you more, my lovely princess, than pies of apples or minces."

At this, the prince could stand no more. He let go of Curdy and fled back to the mountain forever. The king was overjoyed to have his daughter back where she belonged.

"See," he said. "I told you the goblins will get you if you don't watch out."

"But you were wrong!" shouted Irene. "It's the love bug that gets you if you don't watch out."

Now that's a happy ending.
```

---

## IC-2033: Good News Versus Bad

- Title: Good News Versus Bad
- Author (byline): Erin Barker
- Work: The Moth
- Publisher: Hachette Books
- Publication date as stated: Sept 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1285
- Already set (do not supply): none

### Source block (context only)

```text
Author: Erin Baker
Book: The Moth
ISBN: 978-1401311117
Publisher: Hachette Books
Date (Month/Year): Sept 2013
```

### Introduction (context only: never use it for content warnings)

```text
Good News Versus Bad by Erin Baker
```

### Performance text (classify this)

```text
(Pg 201-205) When I was about twelve years old, my mom said she wanted to talk to me about something. My mom and I didn’t have a lot of talks. I loved her very much, but she was one of those corporate working moms with the beeper and the pants suit. She yelled important things into phones, and she was away a lot on business.

But she sat me down in the living room, and she told me that she was pregnant. And it was kind of strange the way she said it, almost like she wasn’t that happy about it. It had been eight years since my brother was born, but even I could remember how excited everybody had been—how everyone had ideas for names, how all the grandparents had flown in from out of town, how barely a day went by that we didn’t get some kind of massive delivery of balloons or a giant stuffed animal. But this time there were no balloons. There weren’t even any cards.

But I was still very excited. I had never expected to have another sibling after my little brother, and I was optimistic that this time I'd get one who could throw a baseball. So I told everyone the big news. I told everyone at school, everyone at church, my Girl Scout troop, the next-door neighbors, the kid who mowed our lawn -everybody. And they were all just as excited as I was. Except after a while, I started to notice that when these people would inevitably congratulate my dad on the big news, there would be this sort of whispered exchange, and then that person would say, "Oh my God, I'm so sorry." And I didn't know what that meant until one day when my dad took me out for ice cream.

My dad was my best friend when I was a kid. He was the dad who would read to us every night before bed and would listen very seriously to my thoughts on the Roald Dahl masterpiece James and the Giant Peach. He taught me how to throw a baseball, and at one point really believed he could teach my brother the same. He taught us that Darth Vader had to wear that suit because he had been injured in a car accident, and so my brother and I better always wear our seat belts unless we wanted to end up like him.

Because my dad and I were so close I knew what ice cream meant. Every time my dad has bad news he takes us out for ice cream. It's kind of his M.O. Don't ever go to the Cold Stone Creamery with my dad -just don't do it. Unless you want to find out that Grandpa has cancer, or your dog's been put to sleep, or your nanny's been fired for stealing your mother's jewelry, just don't go.

So we get our ice cream of doom, and my dad takes a deep breath, and he says, "The baby your mother is pregnant with is not mine." And I can see him looking at me trying to see if I understand at twelve years old what he means.

As it just so happened, I had conveniently just learned what sex was in school, when my science teacher forced poor Craig Berken to read it out loud from our biology textbook. I can still remember the exact words, as read in Craig's shaky, giggly voice: The man jiggles his penis inside the woman's vagina.

Yes, jiggles. Even at that age I was like, I really feel like that is not the right word for this context. "Jiggles" is a word that's neither sexy nor scientific, and probably only belongs in a Jell-0 commercial. But you know, it did the trick. I learned what sex was, and I understood exactly what was going on here. I understood what my dad was telling me, and I could tell how hard it was for him to tell me.

And then he says, "Do you know who the father is?" And I realize with sudden clarity that I do know.

"Andy?" I said, and my dad nodded.

Andy was my mom's coworker, this British guy about ten years younger than her, who would take me and my mom and my brother on little trips and buy us expensive presents. He'd even, oddly enough, gone to church with us. I thought he was our friend.

I realized now that I'd been wrong, and that I'd been stupid not to realize it. And as a result, not only had I failed to prevent this disaster (and like every child I truly believed in my heart that I could have, with a well-timed tantrum or the right number of slammed doors), but I'd also made it infinitely worse for the person who deserved it the least, my father. I'd been coming home for months saying things like, "Dad, look at the awesome Lego castle Andy brought us." "Dad, guess what, we taught Andy how to play baseball today," never noticing the tense silence. Not to mention I'd publicly humiliated him by telling everyone about my mother's pregnancy.

I was devastated, and I was no longer excited about the new baby. Shortly after this my parents got divorced, and my mom bought a house down the street from my dad's because the neighborhood didn't already have enough to talk about. One day I went down and there was cake on the table and my mom said, "Andy and I got married today. Do you want a piece of the wedding cake?"

No, I did not want a piece of the cake of lies.

The next time I went down, I was met with an even bigger surprise, this time in the form of a strange pink baby who I was told was my new sister.

"Do you want to hold her?" my mom asked.

No, I did not want to hold her. I didn't want to look at her, at this baby who had broken my father's heart. I loathed this horrible creature, and I decided then that I always would. I made a commitment in that moment to hate this baby for the rest of my life, possibly longer.

There was just one problem ... I don't know if you've ever tried to hate a baby, but it is difficult. Because everything they do is magical. And this was especially true in the case of my sister, Emma, who had a little Pebbles Flintstone ponytail on top of her head. Every night that I was at my mom's house, she would refuse to go to sleep until I came and sang to her.

Soon I found myself bonding with my mom for the first time in a long time over our mutual love for Emma and our mutual hatred of the Teletubbies. Slowly all my anger fell down like dominoes. When I forgave my sister, it was easier to forgive my mom, and when I forgave my mom, it was easier to forgive myself. I'll admit I never quite forgave Andy, but that was okay because it turned out that his stay with us was only temporary anyway. He met another married woman with children and started going to church with them, and presumably started this story all over with someone else.

As for my dad, I never had to ask for his forgiveness. It was always there.

Emma is fourteen years old now, and she's gone from Teletubbies to Twilight. Clearly she has questionable taste-in a few years it'll probably be Dan Brown novels. But despite that, we're great friends, and I love her very much, and I can't regret anything that happened because without it we wouldn't have her. Although she never did learn how to throw a baseball.
```

---

## IC-2034: Good Pupils

- Title: Good Pupils
- Author (byline): Jack Lothian
- Work: If This Goes On
- Publisher: Parvus Press
- Publication date as stated: March 2019
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: DAVID, ME, MR. GARVEY
- Teaser before the introduction: Yes
- Spoken words (computed): 1473
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jack Lothian
Book: If This Goes On
ISBN: 978-0999784211
Publisher: Parvus Press
Date (Month/Year): March 2019
```

### Introduction (context only: never use it for content warnings)

```text
Good Pupils by Jack Lothian
```

### Performance text (classify this)

```text
On Monday, David's desk is still empty. We've gone through the same process that we go through every day: lining up, trudging through the metal detectors, bags on the conveyor belt, random searches that never feel that random. Picking up our collars from the tray at the end, putting them on. Through another set of metal detectors into the room, and then to the desk, and the whole time I didn't want to look to my right, didn't want to see his seat, as if by not looking, it'll somehow break the jinx. David will be slouched there, scowling, like it was a normal Monday. But the seat is empty, because of what happened last week.

David and I grew up on the same street before his father lost his job and they had to relocate to cheaper housing. I'd been best friends with David since we were six, almost ten years now. I couldn't care less where he lived. [He is . . . was] an ally in this world, someone who has your back, no matter what. Our big guilty pleasure: old teen movies. Breakfast Club, Ridgemont High, Heathers, Grease . . . I get they're corny, and the clothes are weird and the music bad, but they've got a strange energy and spirit. In Dead Poet's Society they stand on their desks. My desk has my name printed on it and is bolted to the ground. When Bender tells Mr. Vernon to 'eat his shorts’, it's amazing to see someone talk to a teacher like that, and not end up on their knees as a result, drooling and disoriented.

DAVID: (laughing) These are not good pupils. The problem with David is that he's not really a good pupil either. He's a smart ass, likes to talk back, and even when he's not speaking he's got an array of tuts and snorts he can deploy to signify displeasure at whoever is talking. When we started in Mr. Garvey's class, it was clear that David's prime motivation was to test the limits of our new teacher, day by day, lesson by lesson. He's also smart though, in a way I don't think I could ever be. He looks at equations or math problems, and something in that brain of his just clicks. So when they introduced the collars, I could see his eyes light up. I knew he'd eventually find a way to slip one out from school, take into his garage, and dissect it.

(Pause) It's been three months since I've seen anyone collared. I don't know the exact details of the incident. All I know is what I saw. He was shouting at Mr. Phillips, gesturing, spit flying from his mouth, some argument they'd got into. He picked up a trash can to throw it. At that moment Mr. Phillips gave a verbal command, and the kid just dropped. His body spasmed and shook. Security took him away, and it was a few weeks until he was allowed back. He's okay now. Sits quiet. Does his work. Never asks questions in class, but never disrupts either. Definitely what they call a "good pupil." The collars had been part of our everyday school life for over a year when David finally sneaked one out. He laid it down on the bench and started taking it apart.

He stripped out the metal work, showing me the tiny motherboard, which he said controls both the shock and the voice trigger.

DAVID: Easy enough to smuggle it out of school. Smuggling it back in-that's the challenge! He'd been engaged in an on-going debate with Mr. Garvey for weeks, something to do with amendments and rights. You can tell Mr. Garvey can't stand David. I don't blame him. When David thinks he's right, he gets this tone in his voice, like he pities you for not being able to keep up. Like it's not enough for him to be right, but he's got to humiliate you as well. He reached into his drawer and rummaged around, taking out a pair of scissors.

DAVID: Cut my hair

ME: I’m not a hairdresser, dumbo.

DAVID: I know that, dumbo. That's why I want you to do it. Just chop away. I want Garvey to look at me and think, 'What is wrong with that kid.’ So I hacked off a clump. David smiled as the hair tumbled into his lap.

You could see security giving him odd looks when he came in the next day. This was the day he decided to smuggle the dismantled collar back in, looping it round the handle of his bag, so you could barely notice. His hair was lopsided. He'd ended up shaving one side as well, then stopping before it was complete. It gave the impression of someone who'd staggered out of a medieval asylum. "You look like a freak," I whispered before I filed through the metal detector ahead of him. On that day he sidetracked Garvey into an argument on rights. David said the exercise of your rights cannot infringe on another person's. Garvey leaped on that, and they went round and round, until David pointed out that he was quoting something Garvey had said a few weeks before, so either it still held true, or Garvey didn't know what he's talking about.

MR. GARVEY: You will apologize.

DAVID: (dripping with sarcasm) I’m sorry. I’m sorry that you don’t know what the *** you’re talking about!

David then started recounting the plot of The Breakfast Club as if it was a historical documentary, drawing special attention to the scene where the kids ran free through the halls.

DAVID: Have you ever stopped to think about what that meant, about what all we've sacrificed! David was moving towards the blackboard when Garvey gave the verbal command to activate the collar. David's body jerked. He staggered forward and there was an audible gasp in class. You could tell some people were horrified, and some were secretly excited to see a collar going off. David stumbled forward a few more steps, and his arms flew out, like a marionette with its strings all tangled . . . Then he raised his head and smiled at our teacher.

DAVID: Mr. Garvey? Go eat my shorts. (takes off the modified collar and throws it to the ground) (Pause) There's that scene in the movies where everyone starts spontaneously applauding at once. That's exactly what happened as David walked out of the room. Even the kids who couldn't stand him were banging on their desks, hollering. Mr. Garvey just stood there, staring at us, like we were animals in a zoo, and the bars weren't as solid as he thought. A week passed. David was absent. His parents didn't pick up the phone. My mother sat me down for "a talk." She told me he's a bad influence. She said if I wanted to do well in life, go to a good college and have a career, then I needed to stay away from [people] like that. David returned on Tuesday. His head has been completely shaved. He is pale, and he walks with a slow and deliberate gait. He doesn't look at me. He sits at his desk, a fresh collar on, his hands folded. He copies down notes. He listens when other kids ask questions. He repeats back the phrases that Mr. Garvey tells us to. He never disagrees. He never rolls his eyes at something Garvey says. His eyes are vacant lots, where once there used to be cities on fire. Something inside me breaks.

ME: What's wrong with David, sir?

MR. GARVEY: (turns from the blackboard to answer. Smiles) Nothing.

ME: (louder) What's wrong with David, sir? I know I can keep asking forever, until the school crumbles and falls, and I'll still never get a proper answer from him. I think of those kids in the movies, running in the corridors. Standing on desks. Getting high behind the bleachers. Breaking into the school at night. I think of glorious, wild, untamed youth. I am already out of my seat and running for Mr. Garvey. I think I'm shouting, "What's wrong with David?" but I'm not entirely sure anymore. Mr. Garvey is yelling the command, and pain rips through my neck, yet still my legs are moving, and my hands are out. That's when Mr. Garvey reaches for his gun and pulls the trigger. They tell me I'm lucky. The bullet grazed my skull. (Long pause) They were going to open it up anyway. (Long pause) (with no emotion or affect) I can name all the States. I can tell you that John Hancock put the first signature on the Declaration of Independence. I know that the tallest mountain is McKinley. I can't tell you what that anger feels like though anymore, that helpless rage. I can't watch those movies either. They seem jumbled and strange, like a language I'll never learn. I sit next to David in class. We nod, and we copy down answers, and we listen intently to what the teacher says. We are good pupils, just like they wanted us to be.
```

---

## IC-2035: A Guide to Some of the Lesser Ballets

- Title: A Guide to Some of the Lesser Ballets
- Author (byline): Woody Allen
- Work: The Complete Prose of Woody Allen
- Publisher: Crown Publications
- Publication date as stated: Nov 1991
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1593
- Already set (do not supply): none

### Source block (context only)

```text
Author: Woody Allen
Book: The Complete Prose of Woody Allen
ISBN: 978-0517072295
Publisher: Crown Publications
Date (Month/Year): Nov 1991
```

### Introduction (context only: never use it for content warnings)

```text
WITH OVER THE TOP ENTHUSIASM . . . . (think excitable sports caster)

In a perfect world, ballet commentators (Yes, I said BALLET) could make annual salaries that exceed $1 million, and become household names in the homes of every American . . . SERIOUSLY! Play-by-play commentators would do most of the talking during performance; they’re smooth talkers who are valued for their ability to tell you what’s happening on the stage. Color commentators, on the other hand, provide deeper analysis because they possess experience from having danced or directed with proven success – MIKHEL BARISNAKOV would definitely be a color commentator. Large theatres -- both on the professional and college levels – would have one of each . . . and it would sound something like this: A Guide to Some of the Lesser Ballets by Woody Allen.
```

### Performance text (classify this)

```text
Dmitri

The ballet opens at a carnival. There are refreshments and rides. Many people in gaily colored costumes dance and laugh, to the accompaniment of flutes and woodwinds, while the trombones play in a minor key to suggest that soon the refreshments will run out and everybody will be dead.

Wandering around the fairgrounds is a beautiful girl named Natasha, who is sad because her father has been sent to fight in Khartoum, and there is no war there. Following her is Leonid, a young student, who is too shy to speak to Natasha but places a mixed-green salad on her doorstep every night. Natasha is moved by the gift and wishes she could meet the man who is sending it, particularly since she hates the house dressing and would prefer Roquefort.

The two strangers accidentally meet when Leonid, trying to compose a love note to Natasha, falls out of the Ferris wheel. She helps him up, and the two dance a pas de deux, after which Leonid tries to impress her by rolling his eyes until he has to be carried to the comfort station. Leonid offers profuse apologies and suggests that the two of them stroll to Tent NO.5 and watch a puppet show-an invitation that confirms in Natasha's mind the idea that she is dealing with an idiot.

The puppet show, however, is enchanting, and a large, amusing puppet named Dmitri falls in love with Natasha. She realizes that although he is only sawdust, he has a soul, and when he suggests checking into a hotel as Mr. and Mrs. John Doe, she is excited. The two dance a pas de deux, despite the fact that she just danced a pas de deux and is perspiring like an ox. Natasha confesses her love for Dmitri and swears that the two of them will always be together, even though the man who works his strings will have to sleep on a cot in the parlor.

Leonid, outraged at being thrown over for a puppet, shoots Dmitri, who doesn't die but appears on the roof of the Merchants Bank, drinking haughtily from a bottle of Air Wick. The action becomes confused, and there is much rejoicing when Natasha fractures her skull.

The Sacrifice

A melodic prelude recounts man's relation to the earth and why he always seems to wind up buried in it. The curtain rises on a vast primitive wasteland, not unlike certain parts of New Jersey. Men and women sit in separate groups and then begin to dance, but they have no idea why and soon sit down again. Presently a young male in the prime of life enters and dances a hymn to fire. Suddenly it is discovered he is on fire, and after being put out he slinks off. Now the stage becomes dark, and Man challenges Nature-a stirring encounter during which Nature is bitten on the hip, with the result that for the next six months the temperature never rises above thirteen degrees.

Scene 2 opens, and Spring still has not come, although it is late August and no one is quite sure when to set the clocks ahead. The elders of the tribe meet and decide to propitiate Nature by sacrificing a young girl. A maiden is selected. She is given three hours to report to the outskirts of town, where she is told they are having a weenie roast. When the girl appears that night, she asks where all the frankfurters are. She is ordered by the elders to dance herself to death. She pleads pathetically, telling them that she is not that good a dancer. The villagers insist, and, as the music builds relentlessly, the girl spins in a frenzy, achieving sufficient centrifugal force to hurl her silver fillings across a football field. Everyone rejoices, but too soon, for not only does Spring fail to come but two of the elders get subpoenaed in a mail-fraud charge.

The Spell

The overture begins with the brass in a joyous mood, while underneath, the double basses seem to be warning us, "Don't listen to the brass. What the hell does brass know?" Presently, the curtain rises on Prince Sigmund's palace, magnificent in its splendor and rent-controlled. It is the Prince's twenty-first birthday, but he grows despondent as he opens his gifts because most of them turn out to be pajamas.

One by one, his old friends pay their respects, and he greets them with a handshake or a slap on the back, depending on which way they are facing. He reminisces with his oldest friend, Wolfschmidt, and they vow that if either of them grows bald the other will wear a toupee. The ensemble dances in preparation for the hunt until Sigmund says, "What hunt?" No one is quite sure, but the revelry has gone too far, and when the check comes there is much anger.

Bored with life, Sigmund dances his way down to the shore of the lake, where he stares at his perfect reflection for forty minutes, annoyed at not having brought his shaving equipment. Suddenly he hears the flutter of wings, and a group of wild swans flies across the moon; they take the first right and head back to the Prince. Sigmund is astounded to see that their leader is part swan and part womanunfortunately, divided lengthwise. She enchants Sigmund, who is careful not to make any poultry jokes. The two dance a pas de deux that ends when Sigmund throws his back out. Yvette, the Swan Woman, tells Sigmund that she is under a spell cast by a magician named Von Epps, and that because of her appearance it is nearly impossible to get a bank loan. In an especially difficult solo, she explains, in dance lan-guage, that the only way to lift Von Epps's curse is for her lover to go to secretarial school and learn shorthand. This is odious to Sigmund, but he swears he will. Suddenly Von Epps appears, in the form of yesterday's laundry, and spirits Yvette away with him as the first act ends.

As Act II begins, it is a week later, and the Prince is about to be married to Justine, a woman he had completely forgotten about. Sigmund is torn by ambivalent feelings because he still loves the Swan Woman, but Justine is very beautiful, too, and has no major drawbacks like feathers or a beak. Justine dances seductively around Sigmund, who seems to be debating whether to go through with the marriage or find Yvette and see if the doctors can come up with anything. Cymbals crash and Von Epps, the Magician, enters. Actu-ally, he was not invited to the wedding, but he promises not to eat much. Furious, Sigmund pulls his sword and stabs Von Epps through the heart. This casts a pall on the party, and Sigmund's mother commands the chef to wait a few minutes before bringing out the roast beef

Meanwhile, Wolfschmidt, acting on Sigmund's behalf, has found the missing Yvette-not a difficult task, he explains, "because how many half women, half swans are there hanging around Hamburg?" Despite Justine's imploring, Sigmund rushes off to Yvette. Justine runs after him and kisses him, as the orchestra strikes a minor chord and we realize Sigmund has his leotards on inside out. Yvette weeps, explaining that the only way to lift the spell is for her to die. In one of the most moving and beautiful passages in any ballet, she runs headlong into a brick wall. Sigmund watches her body change from a dead swan to a dead woman and re-alizes how bittersweet life can be, particularly for fowl. Grief-stricken, he decides to join her, and after a delicate dance of mourning he swallows a barbell.

The Predators

This celebrated electronic ballet is perhaps the most dramatic of all modern dances. It begins with an overture of contemporary sounds-street noises, ticking clocks, a dwarf playing "Hora Staccato" on a comb and tissue paper. The curtain then rises on a blank stage. For several minutes, nothing happens; eventually, the curtain falls and there is an intermission.

Act II begins with a hush as some young men dance on, pretending to be insects. The leader is a common housefly, while the others resemble a variety of garden pests. They move sinuously to the dissonant music, in search of an immense buttered roll, which gradually appears in the background. They are about to eat it when they are interrupted by a procession of women who carry a large can of Raid. Panic-stricken, the males try to escape, but they are put into metal cages, with nothing to read. The women dance orgiastically around the cages, preparing to devour the males the minute they can find some soy sauce. As the females prepare to dine, one young girl notices a forlorn male, with drooping antennae. She is drawn to him, and the two dance slowly to French horns as he whispers in her ear, "Don't eat me." The two fall in love, and make elaborate plans for a nuptial flight, but the female changes her mind and devours the male, preferring instead to move in with a roommate.

A Day in the Life of a Doe

Unbearably lovely music is heard as the curtain rises, and we see the woods on a summer afternoon. A fawn dances on and nibbles slowly at some leaves. He drifts lazily through the soft foliage. Soon he starts coughing and drops dead.
```

---

## IC-2036: Halloween

- Title: Halloween
- Author (byline): Jerry Seinfeld
- Work: Not specified
- Publisher: Little, Brown and Company
- Publication date as stated: Sept 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 873
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jerry Seinfeld
ISBN: 978-0316706254
Publisher: Little, Brown and Company
Date (Month/Year): Sept 2002
```

### Introduction (context only: never use it for content warnings)

```text
I’ll trade you ALL my tootsie rolls for 3 of your Snickers! Yup . . . that’s when we first learned to barter! But that’s not all we learned on . . . Halloween by Jerry Seinfeld.
```

### Performance text (classify this)

```text
When you’re a kid you can eat amazing amounts of food. All I ate when I was a kid was candy. Just candy, candy, candy. And the only really clear thought I had as a kid was get candy. Get candy, Get Candy, Get Candy, GET CANDY.

Family, friends, school – they were just obstacles in the way of getting more candy.

So the first time you hear the concept of Halloween when you are a kid, you’re brain can’t even process the idea.

You’re like, “What is this? What did you say? Someone’s giving out candy? Who’s giving out candy? EVERYONE WE KNOW IS JUST GIVING OUT CANDY?”

“I gotta be a part of this. Take me with you! I’ll do anything they want . . . I can wear that. I’ll wear anything I have to wear. I’ll do anything I have to do to get the candy from those fools who are so stupidly giving it away.”

The first couple of years I made my own costumes. Ghost, hobo . . . the worst.

I knew my destiny was to one day get a real Superman Halloween costume from the store. You know the one . . . The cardboard box . . . the cellophane top, mask included in the set . . . OH, BABY!

Remember the rubber band on the back of those masks? That was a quality item. Thinnest gray rubber in the world. It was good for about ten seconds before it snapped out of that cheap little staple they put it in there with.

You go to the first house, “Trick or . . .” SNAP! It broke, I don’t believe it! “Wait up! I got to fix it. You guys, wait up!” Kids don’t want other kids to wait, they want them to wait UP. Would you wait up?

Because when you’re little, your whole life is up. You want to grow up. Everything is up!

“Wait UP!”

“Hold UP!”

“Shut UP!”

“Mom, I’ll clean UP . . .

Just let me stay UP!”

When you’re a parent, it’s just the opposite: Everything is down.

“Just calm down!”

“Slow DOWN!”

“Sit DOWN!”

“Come DOWN here!”

“Put that DOWN!”

“And keep it DOWN in there!

“You’re GROUNDED!”

So the day finally came. I finally convinced my parents to buy me an official Superman Halloween-store costume. I was physically ready. I was mentally prepared. And I absolutely believed when I put this costume on that I would look exactly like the Superman I had come to know on television and in the movies.

Unfortunately, these costumes are not exactly the super fit that you are hoping for. You look more like you are wearing Superman’s pajamas. It’s all loose and flowy. The neckline comes down to about your stomach. You got that flimsy little ribbon string in the back holding it all together.

Plus, my mother makes me wear my winter coat over the costume anyway. I don’t recall Superman wearing a jacket. I read every comic book. I do not remember him ever once flying with a coat on. Not like the one I had – cheap corduroy, phone fur.

So you go out anyway and the mask keeps breaking, the rubber band keeps getting shorter because you need to keep re-tying it. It’s getting tighter and tighter on your face. Now you can’t even see!

You’re trying to breathe through that little hole that gets all sweaty. Whoosh, whoosh. The mask starts slicing into your eyeballs. “I can’t see, I can’t breathe. But let’s keep going. We gotta get the candy!”

About half an hour into trick-or-treating you take that mask off. “Oh, the heck with it!”

Bing-Bong. “Yeah, it’s me, give me the candy. I’m Superman, look at the red pant legs.”

Year after year, I never gave up on trick-or-treating. But I remember those last, few Halloweens.

I was getting a little too old for it . . . I was just kinda going through the motions. Bing-Bong. “Come on lady, let’s go! Halloween, doorbells, candy, let’s pick it up in there.”

They come to the door; they always ask you the same stupid question. “What are you supposed to be?”

“I’m supposed to be done by now. You want to move it along with the 3Musketeers? I got eighteen houses on this block, sweetheart. You hit the bad, we hit the road. That’s the way it works.” Halloween 3-Step Program:

• Step 1: See kid.

• Step 2: Give candy.

• Step 3: Good night.

Sometimes people give you the little white bag, twisted on the top. You know that’s gonna be some crummy candy. “No official Halloween markings on it? I don’t think so.”

“Wait a second, what is this? The orange marshmallow shaped like a big peanut?

“Do me a favor, you keep that one. We’ve got all the doorstops we need already, thank you very much. We’re going for name candy only this year.”

At the end of Halloween I was able to fill a punch bowl so full of candy that the top of it would be curved. It was like a planet. And I would consume the ENTIRE THING that night.

Next morning, I’d wake up, feel fantastic. And that’s when I realized, when you’re a kid you don’t need a costume, you are Superman.
```

---

## IC-2037: The Happiest Man on Earth

- Title: The Happiest Man on Earth
- Author (byline): Albert Maltz
- Work: Heath Anthology of American Literature
- Publisher: Houghton Mifflin College Division
- Publication date as stated: May 2003
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1256
- Already set (do not supply): none

### Source block (context only)

```text
Author: Albert Matlz
Book: Heath Anthology of American Literature
ISBN: 978-0618542406
Publisher: Houghton Mifflin College Division
Date (Month/Year): May 2003
```

### Introduction (context only: never use it for content warnings)

```text
During the Great Depression, millions of people were out of work across the United States. Unable to find another job locally, many unemployed people hit the road, traveling from place to place, hoping to find some work. Children also greatly suffered from malnutrition. Dietary diseases were rampant because food such as milk, fruit, fresh vegetables, and eggs could not be bought with the family’s low income. So what would make a husband and father happy during this difficult time – a job of course – any job – even a dangerous one would make him The Happiest Man on Earth by Albert Matlz
```

### Performance text (classify this)

```text
Jesse felt ready to weep. He had been sitting in the shanty waiting for Tom to appear, grateful for the chance to rest his injured foot, quietly, joyously anticipating the moment when Tom would say “Why, of course, Jesse, you can start whenever you’re ready!”

For two weeks he had been pushing himself, from Kansas City, Missouri to Tulsa, Oklahoma, through nights of rain and a week of scorching sun, without sleep or a decent meal, sustained by the vision of that one moment.

“Yes?” Tom Brackett said suddenly. “What do you want?”

“I guess you don’t recognize me, Tom . . . I’m Jesse Fulton . . . and Ella sends you her love”

Brackett rose and walked over to the counter until they were face to face. He surveyed Fulton incredulously, trying to measure the resemblance to his brother-in-law as he remembered him. But the face was too gaunt, the body to spiny under the baggy clothes. It was like looking at a faded, badly taken photograph and trying to recognize the subject. “Yes, I believe you are . . . but you sure have changed.”

“By God, it’s been five years, ain’t it?” Jessie said resentfully. Then in mingled vehemence and shame, “What if I have changed. Don’t everybody? I ain’t no corpse.”

Brackett knew what was bothering the boy and it filled his heart with pity. The whole thing was appalling. He had never seen anyone who looked more down-and-out. “Well now, listen, tell me things. How’s Ella and the kids?”

“Oh, they’re fine . . . Well, you know, the young one has to wear a brace. He can’t run around, you know. But he’s smart. He draws pictures and he does things, you know.”

“Ella didn’t tell me things were so bad for you, Jesse. Damn it, boy. I can’t help much. I only get thirty-five a week and I’m damn grateful for it?”

“I know you can’t help us with money! But we met a man who works for you! He said you could give me a job!”

Brackett groaned aloud. “You come walking from Kansas City in two weeks so I could give you a job? You don’t want to work in my department. . . . You don’t know what it is.”

“Yes I do . . . Egbert told me all about it, Tom. You send the dynamite trucks out for the oil business. He told me it was risky work, Tom. But I don’t care. Ain’t there any jobs, Tom?”

“Sure there’s jobs. There’s even Egbert’s job if you want it.”

“He quit?”

“He’s dead! On the job, Jesse. Last night if you want to know, Now you listen to me. I’ll tell you a few things that you should have asked before you started out. It ain’t dynamite you drive. They don’t use anything as safe as dynamite in drilling oil wells. It’s nitroglycerin! You just cough loud and it blows! This stuff goes only in special trucks! At night! They can’t go through any city. Don’t you see what that means? Don’t that tell you how dangerous it is?”

“Tom, you can’t scare me. I got my mind fixed on only one thing: Egbert said he was getting a dollar amile. He was making five to six hundred dollars a month for half a month’s work. Can I get the same?

“Sure you can get the same. A dollar a mile. It’s easy. But why to you think the company has to pay so much. It’s easy - - until you run over a stone or get a blowout. We can’t ask Egbert what happened to him. There’s no truck to give any evidence. There’s no corpse. There’s nothing! Do you understand now? That’s what you get for your God damn dollar a mile!”

There was a moment of silence. Jesse sat twisting his long thin hands. His mouth was sagging open, his face was agonized. Then he shut his yes and spoke softly, “Just look at me, Tom. I just can’t live like this any more. I got to be able to walk down the street with my head up.

“You’re crazy . . . Every year there’s one out of five drivers gets kills. That’s the average. What’s worth that?”

“Is my life worth anything now? We’re just starvin’ at home, Tom. They ain’t put us back on relief yet. There ain’t been other jobs for six years.”

Brackett sat down with his shoulders hunched up wearily. He gripped his hands together and sat leaning forward, staring at the floor.

Jesse stood over him, his gaunt face flushed with emotion, almost unpleasant in its look of pleading and bitter humility. “I ain’t done right for Ella, Tom. Ella deserved better. This is the only chance I see in my whole life to do something for her. I’ve just been a failure. “

“Don’t talk nonsense . . . You ain’t a failure. There’s millions of men in the identical situation. It’s just the depression, or the recession, or the God damn New deal, or . . . !” He swore and lapsed into silence.

Jesse’s face turned an unhealthy mottled red. It looked swollen. “Well I don’t care! You want me to keep looking at my little boy’s legs and tell myself if I had a job he wouldn’t be like that? Every time he walks he says to me, ‘I got soft bones from the rickets and you give it to me because you didn’t feed me right.’

Brackett leaped to his feet. “You say you’re thinking about Ella. How’s she going to like it when you get killed? When you take this job, the only thing certain is that sooner or later you get killed.”

Jessie spoke softly, passionately. “I got it all figured out. On six hundred a month look how much I can save. If I last only three months . . . that’s a thousand dollars . . . more! And maybe I’ll last longer. Maybe a couple years. I can fix Ella up for life!”

“Oh, shut up,” Brackett said. “You think you’ll be happy? Every minute, waking and sleeping, you’ll be wondering if tomorrow you’ll be dead. “

Jesse laughed. “I’ll be happy! Don’t you worry, I’ll be so happy, I’ll be singing. Lord God, Tom, I’m going to feel proud of myself for the first time in seven years!”

“Bracket sighed. “oh, God damn it,” he said finally, “all right, I’ll take you on, God help me.” His voice was low, hoarse, infinitely weary. “If you’re ready to drive tonight, you can drive tonight.

Jesse didn’t answer. He couldn’t. Bracket looked up. The tears were running down Jesse’s face. He was swallowing and trying to speak, but only making an absurd, gasping noise. His heart felt so close to bursting that he pressed both hands against it, as though to hold it locked within his breast.

“Come back here at six o’clock.” Bracket said. “Here’s some money. Eat a good meal.” Bracket turned away. “Oh, get out of here . . . I’m busy.”

Jesse went out. The wet film blinded him, but the whole world seemed to have turned golden. He limped slowly, with the blood punding his temples and a wild joy in his heart. “I’m the happiest man in the world,” he whispered to himself. “I’m the happiest man on the whole earth.”

Bracket sat watching till finally Jesse turned the corner of the alley and disappeared. Then he hunched himself over with his head in his hands. His heart was beating painfully like something old and clogged. He listened to it as it beat. He sat in desperate tranquility, gripping his head in his hands.
```

---

## IC-2038: Harry

- Title: Harry
- Author (byline): Rosemary Timperley
- Work: Roald Dahl's Book of Ghost Stories, Pgs 18-37
- Publisher: Farrar, Straus and Giroux
- Publication date as stated: Oct 1983
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MOM, CHRISTINE, JIM, MISS CLEAVER, OLD WOMAN, TEACHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1780
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rosemary Timperley
Book: Roald Dahl's Book of Ghost Stories, Pgs 18-37
ISBN: 978-0374251314
Publisher: Farrar, Straus and Giroux
Date (Month/Year): Oct 1983
```

### Introduction (context only: never use it for content warnings)

```text
Harry by Rosemary Timperley
```

### Performance text (classify this)

```text
MOM: (Pg 18-37) Ordinary things make me afraid. Sunshine. Sharp shadows on grass. White roses. Children with red hair. And the name Harry. Such an ordinary name.

MOM: The first time Christine mentioned the name, I felt a premonition of fear. She was 5 years old, and she was playing alone in the garden, as she often did. I saw her lying on her stomach in the grass, making daisy-chains. The sun on her pale red hair made her skin look very white. Her big blue eyes were wide with concentration. Suddenly she looked towards the bush of white roses and smiled.

CHRISTINE: Yes, I'm Christine . . . With my mummy and daddy (pause) Oh, but they are my mummy and daddy.

MOM: Uneasy, without quite knowing why, I called her, "Chris, come indoors now. It's too hot for you out there.

CHRISTINE: I must go in now. Goodbye.

MOM: Chris, who were you talking to?

CHRISTINE: Harry.

MOM: (to Christine) Who's Harry? (to audience) I couldn't get anything else out of her, so I read to her until bedtime. As she listened, she stared out at the garden. Once she smiled and waved. When Jim, my husband, came home I told him about the mysterious "Harry."

JIM: (laughing) It's not rare for only children to have an imaginary companion. She hasn't any brothers or sisters or friends her own age. So she imagines someone. I don't know what you're worrying about.

MOM: I felt consoled. Until next morning. Again, the sun shone on the small, bright lawn and white roses. Christine was sitting on the grass, cross-legged, staring towards the rose bush, smiling.

CHRISTINE: Hello. I hoped you'd come. How old are you? I'm only five. I'm not a baby! I'm going to school soon and I shall have a new green dress. Do you go to school? . . . What do you do then?

MOM: She was silent for a while, nodding, listening, absorbed. I felt myself going cold as I stood there in the kitchen. "Don't be silly.” I told myself. "Just carry on as if nothing were happening. Don't listen. Don't be a fool." But I called Chris in earlier than usual for her mid-morning milk. (to Christine) Your milk's ready, Chris. Come along.

CHRISTINE: Can Harry come too?

MOM: Who is Harry, darling?

CHRISTINE: Harry's my brother.

MOM: But Chris, you haven't got a brother. Daddy and mummy have only one child, one little girl, that's you.

CHRISTINE: Harry's my brother. He says so.

MOM: I came to dread those long summer days. I longed for the white roses to wither and die. I trembled when I heard Christine's voice prattling away in the garden. One Sunday, when Jim heard her at it, he said . . .

JIM: You know, I'm getting quite attached to young Harry. Wouldn't it be fun if one day we looked out and saw him?

MOM: Don't say that! It's my waking nightmare. Oh, Jim, I can't bear it much longer. Day in, day out, I hear nothing but 'Harry says,' 'Harry thinks,' 'Can Harry come too?' I'm afraid, Jim.

CHRISTINE: (enters) Harry's got red hair. Redder than my hair. And he's nearly as tall as daddy only thinner. He's 14. He says he's tall for his age.

MOM: She looked up as if at someone beside her. For a brief, dreadful second, I saw a shadow alongside her own - a long, thin shadow. Then it was gone. The child in my house was becoming a stranger. For the first time since Jim and I had adopted Chris. I wondered seriously: Who is she? Who were her real parents? Another week passed. It was Harry, Harry all the time. The day before she was to start school, Chris said:

CHRISTINE: Not going to school.

MOM: You're looking forward to it. There'll be lots of other little girls and boys.

CHRISTINE: Harry says he can't come too.

MOM: You won't want Harry at school. He'd feel silly among little boys and girls, a great lad of 14.

CHRISTINE: (crying) I won't go to school without Harry. I want to be with Harry.

MOM: (angrily) Chris, stop this nonsense! Stop it!

CHRISTINE: (eerily quiet and cold) You don't love me. Harry loves me. He says I can go with him.

MOM: She slept with the tear stains still on her face. I went to the window to draw her curtains. Golden shadows in the garden. Then, like a dream, the long thin clear-cut shadow of a boy near the white roses -- a glimmer of red like close red curls on a boy's head. Then there was nothing. (pause) I told Jim about Christine's emotional outburst. (to Jim) Harry doesn't want her to go to school. . .

JIM: (teasingly) Believing in evil spirits at your old age?

MOM: I don't think Harry's evil. He's just a boy. A boy who doesn't exist, except for Christine. And who is Christine?

JIM: (sharply) None of that! When we adopted Chris, she was to be our own child. No probing into the past. Who is Christine indeed! She's our daughter!

MOM: He'd been so fierce about it that I didn't tell him what I planned to do the next day while Chris was at school. I kissed her goodbye at the gate, and I felt quite light-hearted as I walked away, knowing that Chris was safe and I didn't have to worry. I took a bus to the Greythorne Adoption Society. (to secretary) May I see Miss Cleaver? My name is Mrs. James. (to audience) Miss Cleaver, a tall, thin, grey-haired woman came to meet me.

MISS CLEAVER: Mrs James. How nice to see you again. How's Christine?

MOM: She's very well, Miss Cleaver. I'll get straight to the point. I know you don't normally divulge the origin of a child to its adopters and vice versa, but I must know who Christine is.

MISS CLEAVER: Sorry, Mrs James, our rules . . .

MOM: Please let me tell you the whole story, then you'll see I'm not just suffering from curiosity. (to audience) I told her about Harry.

MISS CLEAVER: Mrs. James, I'm going to break my rule. Christine was born in a very poor part of London. There were four in the family, father, mother, son and Christine herself.

MOM: Son?

MISS CLEAVER: Yes. He was 14 when -- when it happened. Let me start at the beginning. The parents hadn't really wanted Christine. The family lived in one room at the top of an old house which should have been condemned. It was difficult when there were only three of them, but with a baby, life became a nightmare. The mother was neurotic, unhappy. After she'd had the baby, she took no interest in it. The brother, however, adored the little girl. He got into trouble for cutting school so he could look after her. The father had a steady job in a warehouse, not much money, but enough to keep them alive. Then he was sick and lost his job. He was laid up in that messy room, ill, worrying, nagged by his wife, irked by the baby's crying and his son's eternal fussing over the child. Suddenly it all proved too much for him.

One morning, a woman in the ground floor room saw something fall past her window and heard a thud. She went out to look. The son was there on the ground. Christine in his arms. The boy's neck was broken. Christine was blue but still breathing faintly.

The woman woke the household, sent for the police and the doctor. They had to break down the door. An overpowering smell of gas greeted them, in spite of the open window.

They found husband and wife dead in bed and a note from the husband saying: 'I can't go on. I am going to kill them all.' The police concluded that he'd sealed up the door and windows and turned on the gas when his family was asleep. But the son must have wakened. All he could do was pluck away the seals from the window, open it, and fling himself out, holding his adored little sister tightly in his arms.

MOM: Miss Cleaver, what was his name? (to audience) She referred to her files and said . . .

MISS CLEAVER: The family's name was Jones and the 14- year-old brother was called Harold.

MOM: Did he have red hair?

MISS CLEAVER: That I don't know, Mrs James. (pause) We don't think of children as having much memory, but there must be images of the past tucked away somewhere. Christine doesn't invent Harry. She remembers him. So clearly that she's almost brought him to life again.

MOM: May I have the address of the house where they lived? [And] I set out to find # 13 Canver Row. The house was filthy and derelict. But there was a tiny garden with one strange glory that none of the other houses possessed - a bush of white roses. They bloomed gloriously.

OLD WOMAN: What are you doing here?

MOM: It was an old woman, peering from the ground floor window. (to woman) I thought the house was empty.

OLD WOMAN: Should be. Been condemned. But they can't get me out. Nowhere else to go. That's where he fell. Among the roses. He still comes back--won't go away until he gets her. Harry Jones. Nice boy he was. Red hair. Loved Christine too much I thought. Go away, will you? This place isn't for you. It's for the dead who aren't dead, and the living who aren't alive.

MOM: (to audience) Mad people are terrifying. One can pity them, but one is still afraid. Then I heard something that chilled my blood. A clock struck three. At three o'clock I was supposed to be at the school gates, waiting for Christine. At last, I caught the right bus and reached the school. I ran across the empty playground. In a classroom, the teacher was gathering her books together. (to teacher, gasping) I've come for Christine.

TEACHER: (frowning) Christine James? Oh, yes, the little redhaired girl. Her brother called for her. It's sweet to see a boy of that age so fond of his baby sister. Has your husband got red hair, like the two children?

MOM: (aghast) What did - her brother say?

TEACHER: He didn't say anything. He just smiled. They'll be home by now, I should think.

MOM: I ran all the way home. (entering the house frantically calling out) Christine, where are you? Chris! (to audience) Even now I hear my own voice screaming through the house. "Harry! Don't take her away!” I rushed into the garden. The roses glared whitely. For a moment, I seemed very near to Christine, although I couldn't see her. Then the roses danced before my eyes and turned red. The world turned red. I fell through to nothingness - to almost death.

For weeks I was in bed. Jim and the police searched for Christine in vain for months. The papers were full of the strange disappearance of the red-haired child -- stories of kidnappings, child murders. Then the sensation died down. Just another unsolved mystery. (pause)

Such ordinary things make me afraid. Sunshine. Sharp shadows on grass. White roses. Children with red hair. And the name, Harry . . . Such an ordinary name!
```

---

## IC-2039: Harry Potter and the Chamber of Secrets

- Title: Harry Potter and the Chamber of Secrets
- Author (byline): J.K. Rowling
- Work: Not specified
- Publisher: Scholastic, Inc
- Publication date as stated: Aug 2000
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: RIDDLE
- Teaser before the introduction: Yes
- Spoken words (computed): 1090
- Already set (do not supply): none

### Source block (context only)

```text
Author: J.K. Rowling
ISBN: 978-0439064873
Publisher: Scholastic, Inc
Date (Month/Year): Aug 2000
```

### Introduction (context only: never use it for content warnings)

```text
Harry Potter defeated the dark Lord Voldemort at the age of only a year. Now he is 12 and is facing his second year at Hogwart’s School of Witchcraft and Wizardry. There have been attacks petrifying students, all over the school. No one knows who’s committing these attacks until Harry Potter uncovers the mystery of The Chamber of Secrets by J.K Rowling.
```

### Performance text (classify this)

```text
RIDDLE: Twice-in your past, in my future-we have

met. And twice I’ve failed to kill you. How

did you survive? Tell me everything. The

longer you talk the longer you stay alive.”

“Tom-Tom Riddle?” Harry stared at him. Tom Riddle had been at Hogwarts 50 years ago, yet here he stood not a day older than 16. “Are you a ghost?”

“A memory preserved in a diary for 50 years.” Riddle pointed toward the floor. Lying open there was the little black diary Harry had found. “I’ve waited a long time for this Harry Potter, for the chance to speak to you.”

“What’s happened to Ginny?”

“Well, that’s an interesting question, and quite a long story. I suppose the real reason Ginny Weasley’s missing is because she opened her heart and spilled all her secrets to an invisible stranger.”

“What are you talking about?”

“The diary, my diary. Little Ginny’s been writing in it for months and months, telling me all her pitiful worries and woes. It’s very boring having to listen to the silly troubles of an eleven-year-old girl. Yet Ginny simply loved me. No one’s ever understood me like you Tom. . . . I’m so glad I’ve got this diary to confide in. . . . It’s like having a friend I can carry around in my pocket. . . . So Ginny poured out her soul, and her soul happened to be exactly what I wanted. . . . I grew stronger and stronger on a diet of her deepest fears, her darkest secrets. I grew powerful. Powerful enough to start feeding Miss Weasley a few of my secrets, to start pouring a little of my soul back into her. . .”

“What d’you mean?”

Ginny Weasley opened the Chamber of Secrets. She daubed threatening messages on the walls. She set the serpent of Slytherin on four mud bloods. Of course she didn’t know what she was doing at first. It was very amusing. I wish you could have seen her new diary entrees . . . far more interesting they became. . . . Dear Tom, I think I’m loosing my memory, There was an attack today and I don’t know where I was. Tom, what am I going to do? I think I’m going mad. . . . It took a very long time for stupid little Ginny to stop trusting her diary, but she finally became suspicious and tried to dispose of it, and that’s where you came in, Harry. Of all the people who could have picked it up, it was you, the very person I was most anxious to meet. . . .”

“And why did you want to meet me?”

“Well you see, Ginny told me all about you, Harry, your whole fascinating history. I knew I must find out more about you, meet you if I could. So I mad you think that great oaf Hagrid opened the chamber. As though Hagrid had the brains or the power! It had taken me five whole years to find the secret entrance to the chamber. “I knew it wouldn’t be safe to open the Chamber again while I was still at school. But I wasn’t going to waste those long years I spent searching for it. I decided to leave behind a diary, preserving my sixteen-year-old self in its pages, so that one day, with luck, I would be able to lead another in my footsteps, and finish Salazar Slytherin’s noble work.”

“Well you haven’t finished it. No one’s died this time.”

“Killing mud bloods doesn’t matter to me anymore. For many months now my new target has been-you. I knew what I must do. I made Ginny write her own farewell on the wall and come down here to wait. She struggled and cried and became very boring. But there isn’t much life left in her. . . . She put too much into the diary, into me. Enough to let me leave its pages at last. . . . I have been waiting for you to appear. I know you would come. I have many questions for you, Harry Potter.”

“Like what?”

“Well, how is it that you- a skinny boy with no extraordinary magical talent-managed to defeat the greatest wizard of all time? How did you escape with nothing but a scar, while Lord Voldemort’s powers were destroyed?”

“Why do you care how I escaped? Voldemort was after your time. . . .”

“Voldemort, is my past present and future, Harry Potter. . . .” He pulled his wand from his pocket and began to trace it through the air, writing three shimmering words: TOM MARVOLO RIDDLE The he waved the wand once and the letters of his name rearranged themselves: I AM LORD VOLDEMORT “You see Harry? I fashioned myself a new name, a name I knew wizards everywhere would one day fear to speak, when I had become the greatest sorcerer in the world!”

Harry’s brain seemed to have jammed. He stared numbly at Riddle, at the orphaned boy who had grown up to murder Harry’s own parents, and so many others.

“To business, Harry. Twice- in your past, in my future-we have met. And twice I’ve failed to kill you.

How did you survive? Tell me everything. The longer you talk, the longer you stay alive.”

Harry was thinking fast, weighing his chances. It looked bad, but if it had to be a fight between him and Riddle, better sooner than later.

“No one knows why you lost your powers when you attacked me. I don’t know myself. But I know why you couldn’t kill me, because my mother died to save me. My common muggle-born mother. She stopped you killing me. And now, you’re a wreck, you’re barely alive. That’s where all your power got you. You’re in hiding, you’re ugly, you’re foul!”

“So, your mother died to save you. Yes, that’s a powerful counter charm. I can see now . . . There’s nothing special about you after all. Now, Harry, I’m going to teach you a lesson. Let’s match the powers of Lord Voldemort, heir of Salazar Slytherin, against famous Harry Potter.”

Then Harry noticed it-the diary. Then without thinking, without considering, as though he meant to do it all along, Harry seized a snake fang off the floor and plunged it straight into the heart of the book. There was a long, dreadful, piercing scream. Ink sputtered out of the diary in torrents, streaming over Harry’s hands, flooding the floor. Riddle was writhing and twisting, screaming and flailing and then- He was gone, and there was silence. Silence except for the steady drip drip of ink still oozing from the diary.
```

---

## IC-2040: Heaven Help Us!

- Title: Heaven Help Us!
- Author (byline): Cedric the Entertainer
- Work: Grown A$$ Man
- Publisher: Ballantine Books
- Publication date as stated: Oct 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2123
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cedric the Entertainer
Book: Grown A$$ Man
ISBN: 0345447786
Publisher: Ballantine Books
Date(Month/Year): Oct 2002
```

### Introduction (context only: never use it for content warnings)

```text
Church was a big part of my growing up. Back then, it seemed like church was so important. It was about community. It was a time when everybody got together. Sunday was the day for the whole family. You'd go home, have dinner together--cousins and uncles would show up and it'd be a nice day, That's how it was in Caruthersville, Missouri, where I lived until age ten. It was the kind of small town where the lady across the street could whip your butt if she saw you doing something wrong and your mama wasn't home. Those were the good old days. Heaven Help Us by Cedric the Entertainer.
```

### Performance text (classify this)

```text
"Cedric, get off that man's grass! You know that man don't want nobody on his grass!" That was Miss Tessie Mae.

"I hate her," I'd say under my breath.

"I heard you!"

And that lady really did hear you even though she was sitting way up on her porch. She would whip your ass and then make sure you got another whipping when your mama got home from work. Those were the good old days.

You can imagine how important Sunday was in a town like that. My grandmother was one of those real religious people who believed the Lord did everything. She was constantly muttering something about the Lord.

"Ooooh, I woke up this morning, and the Lord put on my house shoes, yes he did. Then I was drivin' down the street and the light turned red, but the Lord told me to keep on going."

"No he didn't, Grandma," I said. "The Lord doesn't tell people to break the law."

I'd hear her speech every Sunday morning for years to come. She didn't care what time you got home from partying on Saturday night. She didn't care that you were sound asleep--one of those good, satisfying, deep sleeps. She'd come in and hit you with the speech.

"You can't tell me you've got time to party on Saturday, but you ain't got time for the Lord on Sunday. Get on up and go on in there." And you'd know it was useless to argue.

Then you'd find yourself sitting up at church with your nightclub clothes on, trying to stay awake. And you aren't the only one. Everybody's nodding--except your grandma and mother. They see your head start jerking like a fishing lure, your eyelids dropping, and you know what happens next? You get that pinch.

"Ouch!" Then you look the other way.

"Man, you got a peppermint, a Certs, a lemon drop, or something? I'm trying to tell you, I ain't gonna make it."

But that was back in the day, before Altoids. Because two or more Altoids will freeze your whole head.

Back then, when you're ten, you're still trying to resist. You start thinking about your daddy. He never goes to church. You see him sitting at home, watching television, drinking a beer, scratching himself, having the kind of good old time you wish you could have.

In fact, he'd never look as happy as he did while waving good-bye and talking about praying for him.

"Y'all pray for me now," he'd say. "Go on ahead."

So you'd turn to your grandma. "What about Daddy?"

"What about him?"

"He don't never go to church?"

"Your daddy knows better. But he's decided he'd rather be going to hell."

And you know she's right. You know your daddy's in trouble. You picture yourself arriving at the pearly gates and St. Peter's saying to him, "Hey dawg, remember that Sunday you didn't feel like getting dressed?"

That's when I think, "A little church might be good for me. Let me just run down and get a TiVo so I don't miss the game."

My favorite part about going to church was the change I got from my mother. It was just a few coins. I'd hit the bottom of the basket as I pretended to put the money in while making the basket jingle.

I wanted my mom to think I'd put the money in, though secretly I put it in my pocket. Only me and God knew. Then after church, I'd buy gum and suckers. I was fine until bedtime. Then I'd think, "Am I going to hell now?"

The other big thing to do on Sundays was go to the Dairy Queen, and everyone in church started to think about that around the same time. So about fifteen minutes before church was over, people started whispering to each other.

There'd be light bickering in which you could tell people were saying, "You go."

"No, you go."

"Just get up, I'm right behind you."

"That's right, amen . . . I went first last week!"

Then people made their moves. One person would pretend to cough and finally get up. He'd be followed by another. Next thing you know, everyone's at the Dairy Queen. The preacher, though not finished with his sermon, knew what was going on, and as the last person hurried out, he worked it right into his sermon, saying, "God wants you to . . . order me a Dilly bar."

"Amen," someone would say from the choir. "Make that two."

The Dairy Queen was right next door to the city jail, so often times you had relatives at the window, hollering down, "Hey, kinfolk, throw me up a banana split or a Blizzard or something."

"Naw, that's too messy. How about a Dilly bar?" At least you got some visiting time in from the Dairy Queen.

That's how it was back in the day. But there seems to be less of that now. Society as a whole seems to be going in a totally different direction. Today, it doesn't seem like church and Sundays have the same importance. You have so many religious leaders, so many televangelists, who are as big as rappers. They're just as famous as the celebrities. They live inside their fame. These guys got private jets. They have mansions. They have money. They're living the same lifestyle as the celebrities. They're friends with Will Smith and Chris Tucker. They want them coming to their church--not so much to save them, but to be associated with them.

Church has become trendy. Choirs have record deals. Going to church nowadays is like going to a concert. It's semicool to go. It's star-studded, people looking around to see who's coming. If you're a celebrity, you get to park in a special parking lot and go in a special back door. You're a celebrity, you don't have to do the regular thing.

That's church in L.A. As if God cares that you're a celebrity, like there's going to be some special roped-off section in Heaven.

I go to church and folks got their instant box cameras with them. People wanting a picture and an autograph . . . during services.

"Can you sign this?"

"Uh, that's your Bible, dawg!"

"Yeah, sign right in Matthew, chapter 7 between verses 20 and 21."

I guess all of that has me a little tainted. The regular common folks want autographs. Is that necessary on a day when everyone should be normal? How do you get celebrity status in a church?

There's something about church and the church environment that indicates we all should be equal because we're all looking for the same thing--salvation.

No matter what, you still have to go to church. When you haven't been to church in a while, you start feeling guilty. You start having thoughts, like maybe the end is near, and suddenly you start hearing a deep, authoritative voice.

"You might want to get up in there, dawg."

"Is that you God?"

"I ain't saying. Alls I'm sayin' is you might want to get your behind into My house soon."

"What do you mean, soon?"

"I mean right now. Not now, but right now!"

Then you start promising yourself that you're going, but you don't make it.

"I'm gonna get on up 'n go on in," you say. "That's what I'm gonna do."

But you don't go, and the next week you raise the ante.

"I'm a go in and pray some, that's what I'm gonna do. I'm a iron my clothes on Saturday. That way, I can just hop right up and go on in."

It's easy to spot the brothers who haven't been to church for a long time. They're the ones who don't know what to do. They walk in thinking they're in a club and find themselves in the pulpit.

"Hey, player, these seats taken? These two?" pointing to the choir director's and deacon's seats. "Ah, they're somebody's seats? All right, damn!"

But he stays cool. He tries another seat.

"Hey, dawg, that's where the preacher sits. You can't sit there. That's where the preacher go!"

It's frightening when you do finally go to church after not having been in a long time. First, you might be identified as a visitor, which means you might have to stand up and have words. And that's a lot of pressure at a black church.

You don't know that church language, which is painfully obvious if you've got to follow that lady who's out traveling. She knows the whole little speech and everything. She gets up right in front of you, giving honor to God, looking you right in the eye.

"Pastor, members, and friends. I come to you on behalf of the Greenway Missionary Baptist Church, Greenway, Mississippi, where my reverend, the Honorable Thesselonious Archinkaid Junior the Third says . . ."

The brother behind her starts panicking. He's next. He starts talking to himself.

"I'm in trouble. I don't know none of that shit. What am I supposed to say?! I don't know none of what that woman's saying. All I know is hip-hop language."

Then he just thinks, "What the hell!" because when his turn comes, he stands up in the middle of the church and gives it a try.

"Ummm, ummm, first of all, givin' big ups to God, Reverend, you 'bout it, you 'bout it. Everybody, big ups. And the choir. Y'all real tight. Real tight. That's on everything. Big ups to y'all."

He keeps on rolling until the sister in the pew next to him leans over and whispers, "Sit your ass down."

The other pressure you might have to deal with going to church after a long dry spell is a good sermon. A good sermon puts a lot of damn pressure on you, boy. You're sitting in your seat and the preacher is doing his thing, calling people up. When he gets like that, he'll eventually find you. You'll think he's finished, but then the Lord will remind him you're there.

"Well, I feel it's just one more person in here that wants to come to the Lord," and he's looking directly at you.

A good sermon is dangerous. It gets you thinking. It starts that internal debate the preacher spoke about. You're in your seat going through it, thinking about it, telling yourself, "Damn, I should go on up there to the altar. I should go ahead on. Pastor's right. I should get my life together. Start right now. Today. If only I didn't . . . have that last little bit of weed left at the crib . . . I'm a join next week. That's what I'm gonna do."

Once, I went to an all-white Catholic church, and I noticed that they prayed differently than black folks. It's true. White folks be praying about trees, clean oceans, peace. They don't care what it is, as long as they're in church they're happy to pray.

"Oh Father, thank you for the trees. Thank you for the birds that fly, Father, and the rivers that run. And the streets we drive on. Amen."

Now you know, if you was at the Great Amount Give A Lot Missionary Baptist Church--in other words, a black church--the prayer is going to be totally different. Black folk pray for stuff that they need--like their lottery numbers to come through.

Then there's always that brother who comes out and prays the same way every time, and for the same things, and you know it's going to be long. You've been planning your escape. You saw Heaven, and it looked like the open highway straight to home. Suddenly you're like, "Oh no, not him! Damn, the game's on!"

But that brother don't care about no game. He's got a whole list of praying to do.

"Dear Lord, you gave me government cheese. Yes you did, Father. I was able to make me a grilled cheese sandwich that was burnt around the edges just like I like it. And Father, when my cable got turned off, your kindness let me run cable from next door. Jesus, y'alright, you such a friend to me. In Jesus's name, Amen."

White folks are so orderly and solemn when they take communion. They're full of quiet contemplation. It ain't that way in a black church. There's always that brother sitting up all important, having the communion wine like he was at a club. He knocks one back and says, "Yo, usher, let me get two more of them. Y'all got any snacks? What's up playa, you gonna eat your cracker? Don't shush me, I'm just askin' if you was gonna eat your cracker?! I was just askin' . . . damn!"
```
