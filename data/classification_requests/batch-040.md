# Classification request: batch 40 of 53 (40 records, IC-1961 to IC-2000)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-040-reply.json`.

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

## IC-1961: All Summer in a Day

- Title: All Summer in a Day
- Author (byline): Ray Bradbury
- Work: The Stories of Ray Bradbury
- Publisher: Knopf
- Publication date as stated: 1980
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: CHILD 1, CHILD 2, MARGOT, NARRATOR, CHILD, WILLIAM, TEACHER, CHILD 3
- Teaser before the introduction: Yes
- Spoken words (computed): 880
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ray Bradbury
Book: The Stories of Ray Bradbury
ISBN: 978-0394513355
Publisher: Knopf
Date (Month/Year): 1980
```

### Introduction (context only: never use it for content warnings)

```text
Many of us feel a bit low during the gloom of winter months, but for an estimated one in twenty people, a lack of light causes changes in energy, appetite, mood and sleep patterns — enough to interfere with normal living. Light, the source of life, is at the core of our culture. From romantic candles to the full intensity of holiday sunshine, the power of light to affect our mood and well-being is tacitly accepted by society.

Join me in a future yet uncharted: All Summer in a Day by Ray Bradbury
```

### Performance text (classify this)

```text
CHILD 1: Ready?

CHILD 2: Ready. . . . Now?

CHILD 1: Soon.

MARGOT: Do the scientists really know? Will it happen today, will it?

CHILD 2: Look, look; see for yourself!

NARRATOR: The children pressed to each other like so many roses, so many weeds, intermixed, peering out for a look at the hidden sun. It rained.

CHILD: It’s stopping, it’s stopping! Yes, yes!

NARRATOR: All day yesterday they had read in class about the sun. About how like a lemon it was, and how hot. And they had written small stories or essays or poems about it.

MARGOT: (quietly) I think the sun is a flower, / That blooms for just one hour.

NARRATOR: That was Margot’s poem, read in a quiet voice in the still classroom while the rain was falling outside.

WILLIAM: Aw, you didn’t write that!

MARGOT: I did. . . I did.

NARRATOR: But that was yesterday. Now the rain was slackening, and the children were crushed in the great thick windows.

CHILD: Where’s teacher? She’d better hurry, we’ll miss it!

NARRATOR: They turned on themselves; like a feverish wheel, all tumbling spokes. Margot stood alone. She was a very frail girl who looked as if she had been lost in the rain for years and the rain had washed out the blue from her eyes and the red from her mouth and the yellow from her hair. She was an old photograph dusted from an album, whitened away, and if she spoke at all her voice would be a ghost. Now she stood, separate, staring at the rain and the loud wet world beyond the huge glass.

WILLIAM: What’re you looking at? (Margot said nothing) Speak when you’re spoken to. (giving her a shove)

NARRATOR: He gave her a shove. But she did not move; rather she let herself be moved only by him and nothing else. They edged away from her, they would not look at her. She felt them go away.

The biggest crime of all was that she had come here only five years ago from Earth, and she remembered the sun. And they, they had been on Venus all their lives, and they had been only two years old when last the sun came out and had long since forgotten the color and heat of it and the way it really was. But Margot remembered.

MARGOT: (eyes closed remembering) It’s like a penny.

CHILD 1: No it’s not!

MARGOT: It’s like a fire in the stove.

CHILD 2: You’re lying, you don’t remember!

NARRATOR: There was talk that her father and mother were taking her back to Earth next year; it seemed vital to her that they do so, though it would mean the loss of thousands of dollars to her family. And so, the children hated her for all these reasons of big and little consequence. They hated her pale snow face, her waiting silence, her thinness, and her possible future.

WILLIAM: Get away! (pushing her again) What’re you waiting for?

NARRATOR: Then, for the first time, she turned and looked at him. And what she was waiting for was in her eyes.

WILLIAM: Well, don’t wait around here! You won’t see nothing!

MARGOT: (whispering) Oh, but . . . but this is the day, the scientists predict, they say, they know, the sun . . .

WILLIAM: All a joke! (grabbing her arm) Hey, everyone, let’s put her in a closet before the teacher comes!

NARRATOR: They surged about her, caught her up and bore her, protesting, and then pleading, and then crying, back into a tunnel, a room, a closet, where they slammed and locked the door. They stood looking at the door and saw it tremble from her beating and throwing herself against it. They heard her muffled cries. Then, smiling, they turned and went out and back down the tunnel, just as the teacher arrived.

TEACHER: (glancing at her watch) Ready, children! Are we all here?

WILLIAM: Yes . . .

NARRATOR: The rain slackened still more. They crowded to the huge door. The rain stopped. The sun came out. The children lay out, laughing, on the jungle mattress, and heard it sigh and squeak under them, resilient and alive. They ran among the trees, they slipped and fell, they pushed each other, they played hide-and-seek and tag, but most of all they squinted at the sun until tears ran down their faces, they put their hands up to that yellowness and that amazing blueness and they breathed of the fresh, fresh air and listened and listened to the silence which suspended them in a blessed sea of no sound and no motion. They looked at everything and savored everything. Then, wildly, like animals escaped from their caves, they ran and ran in shouting circles. They ran for an hour and did not stop running. And then - - - In the midst of their running

CHILD 2: (wailing and holding out her open hand) Oh, look, look!

NARRATOR: They came slowly to look at her opened palm. In the center of it, cupped and huge, was a single raindrop. She began to cry, looking at it. They glanced quietly at the sky. A few cold drops fell on their noses and their cheeks and their mouths. The sun faded behind a stir of mist. A wind blew cold around them. They turned and started to walk back toward the underground house, their hands at their sides, their smiles vanishing away.

CHILD 1: Will it be seven more years?

TEACHER: Yes. Seven.

CHILD 3: (remembering) Margot! She’s still in the closet where we locked her.

NARRATOR: They walked over to the closet door slowly and stood by it. Behind the closet door was only silence. They unlocked the door, even more slowly, and let Margot out.
```

---

## IC-1962: Almost Normal

- Title: Almost Normal
- Author (byline): Jason Sheets
- Work: Turning Points, Pgs 159-161
- Publisher: Tichenor Publishing
- Publication date as stated: Jan 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MRS. SIMPKINS, RULE #1, RULE #2, RULE #3, RULE #4
- Teaser before the introduction: Yes
- Spoken words (computed): 956
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jason Sheets
Book: Turning Points, Pgs 159-161
Publisher: Tichenor Publishing
ISBN: 978-0742117013
Date: Jan 2001
```

### Introduction (context only: never use it for content warnings)

```text
Wow. That was really hard to say, and even harder to do. Why? Because it felt wrong. It felt hateful. No one ever uses diabetes or cancer to denigrate another person. You see, having a medical condition does not make someone lesser or sub-human, and having a cognitive condition shouldn’t be any different.

But it wasn’t always so . . . The R-word was once a slang term that could be heard everywhere: on playgrounds, in hallways and locker rooms; in televisions shows, movies and all-over social media.

In fact, it wasn’t until 2010 that our federal government removed the term “mental retardation” from all federal statutes and replaced it with the term “intellectual disability.”

You see, words have power. They can crush a heart or heal it. They can shame a soul or liberate it. They can shatter dreams or energize them.

In this selection, our narrator comes to the realization that his brother Todd is NOT a ‘retard’ . . . He’s Almost Normal by Jason Sheets.
```

### Performance text (classify this)

```text
NARRATOR: (Pg 159-161) When I was in the fourth grade, my friends and l? We knew how to mess around! We would kick little first graders off the teeter-totters or take Becky Phipher's four-square ball. But our favorite game of all was to imitate the kids from Mrs. Johnson's special ed. class. "Act Like a Retard!" we'd call it. Really clever title. But I was good at this game. I was the master. I had the hand gestures down and everything. I could make fun of those retards better than anyone. Jimmy Stinson always said I was the best actor he'd ever met. I said no. I'd just learned it from my brother.

NARRATOR: My brother, Todd, is nine years older than me. I wasn't even born yet when Todd was diagnosed with mild to moderate mental retardation. Which basically means that somehow, some way, he managed to score a 40 on an IQ test he couldn't even read.

It was kind of difficult figuring out who the baby of the family was: me, because of my age, or Todd, because of his mentality. Either way, Todd caused our entire family to be the object of pity from people in town. I remember one teacher, Mrs. Simpkins, who would always say:

MRS. SIMPKINS: It must be rough having a simple-minded brother. Does it bother you much?

NARRATOR: No. Not until people start talking about it. That was the truth. It didn't bother me much. It just meant that there were certain rules around the house:

RULE #1: Don't say anything you don't want repeated. Like once I said, "U2 sucks." Just a general comment. So then he's walking around the house saying, “You hear that? It SUCKS! U2 sucks!” A half-hour later he asks: "What's U2?"

RULE #2: Don't let Todd request songs at church. Last time he did, he wanted everyone to "do the Vogue!"

RULE #3: Never play Uno with Todd. He'll play a red card and say "WILD! Change it to red!"

RULE #4: Never, ever, expect anyone to have any time for you because YOU are normal. YOU don't need attention.

And Todd loved to talk. It didn't matter if anyone else was in the room, he'd keep up both ends of the conversation. Once I saw him just staring at the wall, talking to himself. I said, "This guy is crazy. He really needs professional help!" Then I thought: who am I talking to?

His favorite topic of conversation was whether he was “retarded” or not. I would just tell him that we are all retarded in certain ways. See, retarded means "slow," not "stupid."

But I put up with his ramblings. 24 hours a day; 365 days a year. I wasn't even safe on my birthday. I didn't even have parties anymore. I was getting ready to blow out the candles when Todd walked up and blew them out for me. And not to be selfish, but that was my birthday moment! My wish. . . and I could have used one!

What did my parents do? They hugged him. See, Todd had never blown out a candle before. They brought out the camera and took a picture of him with the cake.

April 11, 1982: The night of my big solo at the spring concert. Mom missed it. She was out in the lobby giving Todd his 8:00 dose of Mellaril. He has to have it at exactly 8:00. So, she missed my solo. Dad saw it and said I was great. Mom took his word for it.

My brother is rather hard to describe. Let's see . . . he likes anything with cops or firemen, so his favorite TV show is "Rescue 911." His favorite movie is "Beverly Hills Cop." His favorite color is red -- fire-engine red.

Number of embarrassing moments he has caused: 447.
Number of shirts he owns: 25.
Number of shirts he wears: 6.
Number he can count to: 19.
Number of dishes he has broken: 38.
Number of times he's said "I love you": 2,714.
Number of times I've told him I love him: 4.

Trips to the mall were the worst. For some reason, Todd saw this as his chance to pick up chicks. I tried to explain to him that "Whew, shake it for my baby!" was not the coolest pick-up line.

One day, we were walking out of Walgreen's when a store clerk stopped us. She said Todd had taken something from their store without paying for it. I explained to her that he couldn't have because Todd does not steal. He may be slow, but he does not steal. She asked if she could search his pockets. I said "Fine, go ahead." Then she pulled out two packs of M&M's and a Twix bar from Todd's coat pocket. I couldn't believe it. I asked him why he did it. He said he was hungry.

I pleaded with the clerk not to call mom and dad, but she did anyway. When they heard, they decided it was time to place Todd in a group home. They said they couldn't control him anymore. But they could have. They just didn't want to.

I'll never forget the look on his face when we dropped him off at that group home forever. I said, "I love you" and he said nothing. He stared at me with those big, blue eyes, tears streaming down his cheek, looking at me like I was some sort of Judas. That was two years ago. Todd still gets to come home on the holidays, and I still visit him every Saturday. Sometimes we talk. Sometimes not. He appears a year older every time I see him. It's the same Todd, but something is missing. Something real. Something good.
```

---

## IC-1963: Among the Bumblebees

- Title: Among the Bumblebees
- Author (byline): Sylvia Plath
- Work: Johnny Panic and the Bible of Dreams, Pgs 320-326
- Publisher: Harper Perennial Modern Classics
- Publication date as stated: Sept 2008
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1553
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sylvia Plath
Book: Johnny Panic and the Bible of Dreams,
Pgs 320-326
ISBN: 978-0061549472
Publisher: Harper Perennial Modern Classics
Date (Month/Year): Sept 2008
```

### Introduction (context only: never use it for content warnings)

```text
The bond between a father and his daughter can be one of the most important relationships in a young girl’s life.

Alice Denway moves through a world that hums with her father’s power. Like the bumblebees he so effortlessly captures and releases, Alice is drawn to him . . . awed by his strength, unknowingly influenced by its grasp.

Alice depends on her father’s strength to show her how to navigate the world. But when the illusion of her father’s invincibility starts to falter, when the steady buzz of control gives way to silence, Alice is left alone and uncertain . . .

Among the Bumblebees by Sylvia Plath
```

### Performance text (classify this)

```text
(Pgs 320-326) In the beginning there was Alice Denway's father, tossing her up in the air until the breath caught in her throat, and catching her and holding her in a huge bear hug. With her ear against his chest, young Alice could hear the thunder of his heart and the pulse of blood in his veins, like the sound of wild horses galloping.

Alice Denway's father had been a giant of a man. In the blue blaze of his eyes was concentrated the color of the whole overhead dome of sky, and when he laughed, it sounded as if all the waves of the ocean were breaking and roaring up the beach together. Alice worshiped her father because he was so powerful, and everybody did what he commanded because he knew best.

There had been that spring evening . . . "Who's my girl?" he asked her fondly, tweaking at a pigtail.

"Alice is!" she cried out, bouncing in her chair. "Can I watch you correct tonight?"

"May," said her father. "Yes, you may, if you are very quiet." He wiped his lips on his napkin, folded it, and tossed it on the table, pushing back his chair.

Alice followed her father into the den and went to sit in one of the big, slippery leather chairs near his desk. She liked to watch him correcting the papers he brought home in his briefcase, fixing the mistakes that people had made. He would go reading along, and then all at once stop, pick up his colored pencil and make little red gashes here and there where the words were wrong.

"Do you know," her father had said once, looking up suddenly from his work, "what will happen tomorrow when I hand these papers back in class? There will be," her father intoned in mock severity, with a black frown, "a weeping and wailing and a gnashing of teeth."

Alice had thought, then, of the great hall at the college where her father stood, high upon a platform. Hundreds of people came to listen to her father talk and tell them wonderful strange things about how the world was made.

She had pictured him standing up there, handing down papers to the people, calling them by name, each one. Like a king, high on a throne, he would call out the names in his thundering voice, and the people would come, trembling and frightened, to take their papers. And then, rising mournfully, there would be the sound of weeping, of wailing, and gnashing of teeth. Alice hoped that she would be there some day when the people were gnashing their teeth; she was sure that it would make a terrible and awe-inspiring noise.

In the summertime, her father did not go to town at all. He would take her to the beach. First Father would go for a swim himself, leaving her on the shore, with the small waves collapsing at her feet and the wet sand sliding up cool between her toes. Alice would stand ankle-deep, watching him admiringly from the edge of the breakers, shielding her eyes against the blinding glare of summer sun that struck silent and brilliant on the surface of the water.

After a while she would call to him, and he would turn and begin swimming shoreward, carving a line of foam behind him with his legs and cleaving the water ahead with the powerful propellers of his arms. He would come to her and lift her onto his back, where she clung, her arms locked about his neck, and go swimming out again. In an ecstasy of terror, she would hold on to him, her soft cheek prickling where she laid her face against the back of his neck, her legs and slender body trailing out behind her, floating, moving effortlessly along in her father's energetic wake.

And gradually, there on her father's back, Alice's fear would leave her, and the water, black and deep beneath her, would seem calm and friendly, obeying the skillful mastery of her father's rhythmic stroke and supporting both of them upon the level waves.

Alice's father feared nothing. Power was good because it was power, and when the summer storms came, with the crackling blue sheet lightning and the ear-splitting thunderclaps, Alice's father would roar with laughter. Alice learned to sing the thunder song with her father: "Thor is angry. Thor is angry. Boom, boom, boom! Boom, boom, boom! We don't care. We don't care. Boom, boom, boom!" And above the resonant resounding baritone of her father's voice, the thunder rumbled harmless as a tame lion.

Sitting on her father's lap in the den, watching the waves at the end of the street whipped to a ragged froth of foam, Alice learned to laugh at the destructive grandeur of the elements. The swollen purple and black clouds broke open with blinding flashes of light, and the thunderclaps made the house shudder to the root of its foundations. But with her father's strong arms around her and the steady reassuring beat of his heart in her ears, Alice believed that he was somehow connected with the miracle of fury beyond the windows, and that through him, she could face the doomsday of the world in perfect safety.

When it was the right time of year, her father took her into the garden and showed her how he could catch bumblebees. That was something no one else's father could do. Her father caught a special kind of bumblebee that he recognized by its shape and held it in his closed fist, putting his hand to her ear. Alice liked to hear the angry, stifled buzzing of the bee, captured in the dark trap of her father's hand, but not stinging, not daring to sting. Then, with a laugh, her father would spread his fingers wide, and the bee would fly out, free, up into the air and away.

One summer, Alice's father did not take her out to catch bees. He lay inside the house on the couch and Mother brought him trays with orange juice in tall glasses. He drank a lot of water, for he was very thirsty all the time.

It went on like that for a long while. At night, after Alice was in bed, she could hear Mother speaking to Father in the next room, and her voice would go along very soft and low for a while, until Father would get cross and raise his voice like thunder.

One day, after a night like this, the doctor came to see Father, and after he had left, Father began to stay in bed - - doctor's orders. There was whispering, now, instead of talking. The doctor wanted the blinds in Father's room kept down because the sunlight was too bright and hurt [his] eyes.

The doctor, bringing his black bag and smiling a foolish bright smile, pulled playfully at Alice's pigtail, but she switched it away from him with a pout and a toss of her head. Father winked at her, but Mother shook her head.

"Be nice, Alice," she begged. "The doctor's here to help Father."

That was not true. Father did not need any help. The doctor was making him stay in bed; he shut out the sun and that was making Father unhappy. Father could tell the plump silly doctor to go out of the house, if he wanted to. Father could slam the door after him and order him never to come back again. But instead, Father let the doctor take a big silver needle out of the black bag and swab a sterile place on Father's arm and stab the needle in.

Father did not wince at all. He let the needle go in and looked at her with his strong blue eyes, silently telling her that really he did not care; he was only humoring Mother and the absurd fat little doctor. Alice felt her eyes fill up with tears of pride. But she blinked back the tears and did not cry. Father did not like anyone to cry.

The next day Alice went to visit her father again. She tiptoed into the room, which smelled sweet and strange with alcohol. Father was asleep, lying motionless on the bed except for the rhythmic rising and falling of the blankets over his chest and the sound of his breathing. In the muted light, his face was the sallow color of candle wax, and the flesh was lean and taut about his mouth.

Alice stood looking down at her father's gaunt face, clenching and unclenching her thin hands by her side and listening to the slow thread of his breathing. Then she leaned over the bed and put her head down on the bedclothes above his chest. From somewhere, very faint and far off, she could hear the weak pulsing of his heart, like the fading throb of a distant drum.

"Father," she said in a small pleading voice. "Father." But he did not hear . . . Lost and betrayed, she slowly turned away and left the room.

That was the last time that Alice Denway saw her father. She did not know then that in all the rest of her life there would be no one to walk with her, like him, proud and arrogant among the bumblebees.
```

---

## IC-1964: And Thy Name Shall Be . . . Something

- Title: And Thy Name Shall Be . . . Something
- Author (byline): Paul Reiser
- Work: Babyhood, Pgs 67-79
- Publisher: Avon
- Publication date as stated: Aug 1998
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1578
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul Reiser
Book: Babyhood, Pgs 67-79
ISBN: 978-0380728725
Publisher: Avon
Date (Month/Year): Aug 1998
```

### Introduction (context only: never use it for content warnings)

```text
And Thy Name Shall Be . . . Something from Babyhood by Paul Reiser
```

### Performance text (classify this)

```text
(Pg 67- 79) Naming your child is a monumental responsibility. You get to tag and identify – for life – a whole new person. Throughout your child’s life, it will come up every hour of every day.

“Name, please.”

“Hi, what’s your name?”

“Sorry, I didn’t catch your name.”

“We just need you to sign your name.”

“Would you put last name first, first name last, middle

initial . . . “

“May I ask who’s calling?

“Name and Social Security number . . .”

And with every usage, that name – the result of hours and hours of debate, and the consideration of an infinite number of variables, uninvited input, and conflicting personal agendas – that name will, for good or bad, represent to the world and its people, for all eternity, your child.

Which is why you don’t want to screw it up.

People screw up their kids’ names all the time. Not on purpose. In fact, usually with the best of intentions. The new parents who want their child to stand out and be recognized, who want more than anything to thrust their child forward from a sea of common and interchangeable surnames, are the ones responsible for kindergartens full of Zebadiahs, Queequegs, and Moons. Lovely and creative names all. Unfortunately, these kids are in for a lifetime of quizzical stares, judgmental smirks, and patronizing displays of phony interest, in response to which they can only say, “Yeah, my parents were into a thing . . . “

The power is extraordinary. The simple combination of letters and sounds you select can result in a life of carefree coolness or decades of expensive therapy.

“Hi, I’m Jake” versus “Hi, I’m . . .Tapioca.”

Not to denigrate the virtues of being unique. It’s just that there’s a fine line between Good Unique and Just Plain Wrong. Good Unique is when you call your child’s name and he’s the only one who comes running. Just Plain Wrong is when they’re running because they’re being chased.

I imagine that part of the reasons there are so many Bobs and Janes year after year is that even parents who want to be creative ultimately chicken out. And understandably. You never know when the name you love today is going to be hideous tomorrow. The Ashleys, Dylans, and Maxes of our children could turn out to be what Hortense, Gertrude, and frankly, Max were when we were growing up. It’s sort of like the jacket you wore in your high school yearbook photo; it may have been cutting-edge that week, but for the rest of your life, you’re “the maroon-plaid-jacket guy with lapels the size of sea flags.”

All I know is that if you name your daughter Trixie or Tina, she’s more likely to sleep in a van with a band from Seattle than the exact same girl named Ruth. Similarly, a boy named Herbert may grow up to play baseball professionally, but not as easily as Dale, Pee Wee, or Scooter. This, of course, is not scientifically documented or anything, but . . . I think I know what I’m talking about.

A lot of people tell you that their kid popped into the world and the name just revealed itself: “He looks like an ‘Elliot.’ Let’s call him ‘Elliot.’”

Come on – nobody seven minutes old looks like “Elliot.” It takes years to look like “Elliot.” If they’re like most newborns, your precious new one will enter this world looking like one of three things: Winston Churchill, Mahatma Gandhi, or a boiled chicken. That’s basically it. (It is possible for a baby to look like Churchill or Gandhi and a boiled chicken, but this usually goes away with time and plenty of fluids.)

In some cultures, they don’t even name their babies right away. They wait until they see how the child develops; see what they do, see how they behave . . . and then name the kid accordingly. Like in Dances with Wolves. If you stand with your fists clenched, you’re called Stands with a Fist. I like that system. It certainly makes it easy to remember people you’ve met.

“How’s that guy doing?”

“What guy?”

“You know . . . what’s-his-name, the guy who’s always yelling at the vegetables . . . “

“Oh, you mean Barks at Salad?”

“Yes, yes, Barks at Salad . . . how’s he doing? . . .” Unfortunately, in our world, kids’ names would be less romantic and poetic. Certainly, less warrior-like. “This is my oldest boy, Falls Off His Tricycle, his friend, Dribbles His Juice, and my beautiful daughter, Allergic to Nuts.”

Some people don’t agonize at all about finding the perfect name. They simply give the kid their name. “He’ll be me, but Me Junior. To be followed by Me the Third, and his son, Me the Fourth.”

Certainly moves things along. Of course, if you’re really pressed for time, do what heavyweight champ George Foreman did - - name all of his kids George Foreman. God bless him, a great fighter, a fine humanitarian – not, apparently, the most creative in the naming department. An entire family named George Foreman. It’s not like they’re of successive generations, overlapping only here and there for a few years . . . No, this is almost half a dozen guys, with the exact same name, all living in the same house.

For others, the task of naming is simplified by family mandates. “The child will be named after his grandfather.” Or, “She will take her mother’s surname, and it shall be as her own . . . And they shall go forth unto themselves, with their beasts and their grains, and into the desert shall they sojourn.” (I’m sorry, I just saw The Ten Commandments on TV and frankly, I enjoy talking like that.)

In our case, we knew we wanted to name our child after my father. We didn’t want to use the exact same name, but something beginning with the same letter. We had plenty of girls’ names we liked, but nothing for a boy. Of course, when our son came out a boy (as almost all sons do) we were stuck. So we decided instead to honor my father’s name by making it our son’s middle name. Middle names are kind of like vice presidents: It’s a fine distinction and certainly an honor, but you’re never not aware that someone else got the real job.

Parents often give middle names just so that later, when they’re yelling at the kid, they can drag it out: “Henry David Thoreau, you come in here this instant!” It gives them something extra to sink their teeth into.

If, however, you assassinate someone, your middle name is all over the place. Once you shoot a famous person, not only do you go to jail and sit alone hungering for a forgiveness that eludes you your whole life, but on top of that, your middle name, whether you like it or not, gets publicly and permanently cemented right between your first and last name. They just run those puppies together like Sonny-and-Cher. There’s no way you can undo something like that.

But because of the potential anonymity enjoyed by middle names, they also represent opportunities for Name Givers to safely store their really creative choices. So when you meet kids named Stanly DiMaggio Miller or Carol Satchmo Smith, you know their parents had healthy doses of not only creative sparks but discretion, too.

The moment you announce your child’s name, people take it in for a moment, digest it, and then say, “Okay, but what are you going to call him?”

“What do you mean, what are we going to call him? His name.”

“No, of course, but what’s the nickname going to be? I mean Franklin is a beautiful name, but what do we call him? Frank? Frankie? Frankle? Frankfurter?”

This was a setback I hadn’t seen coming. After finally landing on a name the two of you like, your family tells you it’s not enough. You have to come up with a menu of officially sanctioned deviations and nicknames, which they’re going to disregard anyway.

“Hello, Snooky . . . Hello, Angel-puss . . . Who’s my sweet Pumpkin?”

They get called a lot of foods, these babies: “Pumpkin,” “Angel Cake,” “Cupcake,” “Honey,” Sweet Pea,” “Puddin’ . . . ” But not all foods. You never hear someone call an infant “Steak.” “Chicken Parmigiana.” “Eggs.”

I think the rule of thumb is, desserts and side dishes are okay -- entrees and appetizers, not okay. The only exceptions that I’m aware of are my Aunt Cutlet and Uncle Bisque, who were actually born with those names but, ironically, were later nicknamed Phyllis and Lloyd.

(Pg 72) So we bought every book out there on baby names, because when you’re not by nature good with decisions, what could be more pleasant than slugging through the list of every name registered in every town on the globe? While it is nice to learn about other peoples, I’m not sure that any one family needs that many choices.

You’re probably going to stay within a given range. Very few people end up deciding, “Okay, so Achmanzlebred if it’s a girl, and if it’s a boy – Scott.”

You do, however, get to learn the etymology and origin of names, which is useful for parents trying to boost the self-esteem of kids stuck with loser names.

“Sweetheart, you know Milton actually means ‘Ferocious Fighter of Freedom’ . . . “

(Pg 74) Of course, some names you can eliminate pretty comfortably.

“Adolf?”

“Out”

“Medusa?”

“Out”

(Pg 67) Yup . . . Naming your child is a monumental

responsibility. You get to tag and identify – for life – a

whole new person. Throughout your child’s life, it will

come up every hour of every day.

“Name, please.”

“Hi, what’s your name?”

That name will, for good or bad, represent to the world and its people, for all eternity, your child -- Which is why you don’t want to screw it up.

Thanks to mom and dad for my name:

(INSERT FULL NAME HERE)
```

---

## IC-1965: And Weep, Like Alexander

- Title: And Weep, Like Alexander
- Author (byline): Neil Gaiman
- Work: Trigger Warning, Pg 303
- Publisher: William Morrow Paperbacks
- Publication date as stated: Oct 2015
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, OBEDIAH, BRIAN, PROF MACKINTOSH, MICHAEL, SALLY, JOCELYN, TWEET, RAY
- Teaser before the introduction: No
- Spoken words (computed): 1205
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Gaiman
Book: Trigger Warning, Pg 303
ISBN: 978-0062330321
Publisher: William Morrow Paperbacks
Date (Month/Year): Oct 2015
```

### Introduction (context only: never use it for content warnings)

```text
Alexander Graham Bell, best known for his invention of the telephone, revolutionized communication as we know it. Let’s face it, he laid the building blocks of smart phone technology. Texting, e-mails, selfies, social media, emojis, games and even television stream to us 24-7 through the current version of the first telephone invented in the 1800s. What would we do without it?

And Weep, Like Alexander by Neil Gaiman
```

### Performance text (classify this)

```text
NARRATOR: (Pg 303+) The little man hurried into the Fountain and ordered a very large whisky.

OBEDIAH: Because . . . I deserve it.

BRIAN: I’m sure you do.

NARRATOR: He looked exhausted, sweaty and rumpled, as if he had not slept in several days. He wore a tie, but it was so loose as to be almost undone. He had greying hair that might once have been ginger. He took a sip of the whisky as if to find out whether or not he liked it, then, satisfied, gulped down half the glass. He stood completely still, for a moment, like a statue.

OBEDIAH: Listen. Can you hear it? - A sort of background whispering white noise that actually becomes whatever song you wish to hear when you sort of half-concentrate upon it?

NARRATOR: (listening) No.

OBEDIAH: Exactly! (pleased with himself) Isn’t it wonderful? Only yesterday, everybody in the Fountain was complaining about the Wispamuzak. Professor Mackintosh here was grumbling about having Queen’s “Bohemian Rhapsody” stuck in his head and how it was now following him across London. Today, it’s gone, as if it had never been. None of you can even remember that it existed. And that is all due to me.

PROF MACKINTOSH: I what? . . . Something about the Queen? . . . Do I know you?

OBEDIAH: We met. But people forget me, alas. It is because of my job.

NARRATOR: He took out his wallet, produced a card, passed it to me: (reads the card aloud) OBEDIAH POLKINGHORN – UNINVENTOR (to Obediah) If you don’t mind my asking, What’s an uninventor?

OBEDIAH: It’s somebody who uninvents things. (raises his empty glass) Ah. Excuse me. Sally, I need another very large whiskey.

NARRATOR: The rest of the crowd there that evening seemed to have decided that the man was both mad and uninteresting. They had returned to their conversations. I, on the other hand, was caught. (to Obediah) So, have you been an uninventor long?’

OBEDIAH: Since I was fairly young. I started uninventing when I was eighteen. Have you never wondered why we do not have jet-packs?

NARRATOR: I had, actually.

MICHAEL: Saw a bit on Tomorrow’s World about them, when I was a lad. Man went up in one. Then he came down. Raymond Burr seemed to think we’d all have them soon enough.

OBEDIAH: Ah, but we don’t, because I uninvented them about twenty years ago. I had to. They were driving everybody mad. I mean, they seemed so attractive, and so cheap, but you just had to have a few thousand bored teenagers strapping them on, zooming all over the place, hovering outside bedroom windows, crashing into the flying cars . . .

SALLY: Hold on. There aren’t any flying cars.

OBEDIAH: True, but only because I uninvented them. You wouldn’t believe the traffic jams they cause. I’d look up and it was just the bottoms of bloody flying cars from horizon to horizon. Some days I couldn’t see the skies at all. People throwing rubbish out of their car windows . . . They were easy to run – ran off gravitosolar power, obviously – but I didn’t realize that they needed to go until I heard a lady talking about them on Radio Four, all “Why Oh Why Didn’t We Stick with Non-Flying Cars?” She had a point. Something needed to be done. I uninvented them. I made a list of inventions the world would be better off without and, one by one, I uninvented them all.

NARRATOR: By now he had started to gather a small audience. I was pleased I had a good seat.

OBEDIAH: It was a lot of work, too. You see, it’s almost impossible not to invent the flying car, as soon as you’ve invented the Lumenbubble. So eventually I had to uninvent them too. And I miss the individual Lumenbubble: a massless portable light source that floated half a metre above your head and went on when you wanted it to. Such a wonderful invention. Still, no use crying over unspilt milk, and you can’t mend an omelette without unbreaking a few eggs.

JOCELYN: You also can’t expect us actually to believe any of this!

BRIAN: Right. I mean, next thing you’ll be telling us that you uninvented the spaceship.

OBEDIAH: But I did. (very pleased with himself) Twice. I had to. You see, the moment we whizz off into space and head out to the planets and beyond, we bump into things that spur so many other inventions. The Polaroid Instant Transporter. That was the worst. And the Mockett Telepathic Translator. That was the worst as well. But as long as it’s nothing worse than a rocket to the moon, I can keep everything under control.

NARRATOR: So, how exactly do you go about uninventing things?

OBEDIAH: It’s hard. It’s all about unpicking probability threads from the fabric of creation. Which is a bit like unpicking a needle from a haystack. But they tend to be long and tangled, like spaghetti. So it’s rather like having to unpick a strand of spaghetti from a haystack. . . I pride myself on doing good. Each day I wake, and, even if I’ve unhappened something that might have been wonderful, I think, Obediah Polkinghorn, the world is a happier place because of something that you’ve uninvented. (he pauses to gaze into his glass) The trouble is with the Wispamuzak gone, that’s it. I’m done. It’s all been uninvented. There are no more horizons left to undiscover, no more mountains left to unclimb.

TWEET: Nuclear power?

OBEDIAH: Before my time. Can’t uninvent things invented before I was born. Otherwise I might uninvent something that would have led to my birth, and then where would we be? (silence) Kneehigh in jet-packs and flying cars, that’s where. Not to mention Morrison’s Martian Emolument. (looking quite grim) Ooh. That stuff was nasty. And a cure for cancer. But frankly, given what it did to the oceans, I’d rather have the cancer. (pause) No. I have uninvented everything that was on my list. (bravely) I shall go home, and weep, like Alexander, because there are no more worlds to unconquer. What is there left to uninvent?

NARRATOR: There was silence in the Fountain. In the silence, Brian’s iPhone rang. His ringtone was the Rutles singing ‘Cheese and Onions’.

BRIAN: Yeah? I’ll call you back.

NARRATOR: It is unfortunate that the pulling out of one phone can have such an effect on other people around. Sometimes I think it’s because we remember when we could smoke in pubs, and that we pull out our phones together as once we pulled out our cigarette packets. But probably it’s because we’re easily bored. Whatever the reason, the phones came out. Crown Baker took a photo of us all, and then Twitpicced it. Jocelyn started to read her text messages. ‘Tweet’ Peston tweeted that he was in the Fountain and had met his first uninventor. Professor Mackintosh checked the test match scores, told us what they were and emailed his brother in Inverness to grumble about them. The phones were out and the conversation was over.

OBEDIAH: What’s that?

RAY: (holding his phone up) It’s the iPhone 5. Crown’s using the Nexus X. That’s the Android system. Phones. Internet. Camera. Music. But it’s the apps. I mean, do you know, there are over a thousand fart sound effect apps on the iPhone alone? You want to hear the unofficial Simpsons Fart App?’

OBEDIAH: No. (offended) I most definitely do not want to. I do not.

NARRATOR: He put down his drink, unfinished. Pulled his tie up. Did up his coat.

OBEDIAH: (speaking to himself) It’s not going to be easy But, for the good of all . . . (he smiles) (to the bar) It’s been marvelous talking to you all! (he whistles as he exits)
```

---

## IC-1966: An Angel in Disguise

- Title: An Angel in Disguise
- Author (byline): TS Arthur
- Work: After a Shadow and Other Stories, Pg 226-243
- Publisher: ReadHowYouWant
- Publication date as stated: June 2012
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MRS. ELLIS, MAN 1, MAN 2, JOE, BLACKSMITH’S WIFE, MAGGIE, MRS. THOMPSON
- Teaser before the introduction: No
- Spoken words (computed): 1559
- Already set (do not supply): none

### Source block (context only)

```text
Author: TS Arthur
Book: After a Shadow and Other Stories, Pg 226-243
ISBN: 978-1425065577
Publisher: ReadHowYouWant
Date (Month/Year): June 2012
```

### Introduction (context only: never use it for content warnings)

```text
What is compassion? By definition it is the feeling that arises when you are confronted with another’s suffering and feel motivated to relieve that suffering. It’s more than sending “thoughts and prayers” – it is action. Today I challenge you to reflect on the power of compassion. You may truly find . . .

An Angel in Disguise by TS Arthur
```

### Performance text (classify this)

```text
NARRATOR: (Pg 226-243) Idleness, vice, and intemperance had done their miserable work, and the dead mother lay cold and still amid her wretched children. This woman had been despised, scoffed at, and angrily denounced by nearly everyone in the village; but now, pity took the place of anger, and sorrow of denunciation. Neighbors went hastily to the old tumble-down hut: some with grave-clothes for a decent interment of the body; and some with food for the half-starving children, three in number. John, the oldest, was a stout lad, able to earn his living with any farmer. Kate was a bright, active girl, out of whom something clever might be made, if in good hands; but poor little Maggie, the youngest, was hopelessly diseased. Two years before, a fall from a window had injured her spine, and she had not been able to leave her bed since. "What is to be done with the children?" After considering the matter, farmer Jones said that he would take John, and do well by him, now that his mother was out of the way; and Mrs. Ellis concluded that it would be charitable to make choice of Katy, even though she was too young to be of much use.

MRS. ELLIS: I could do much better, I know. But as no one seems inclined to take her, I must act from a sense of duty.

NARRATOR: But no one said "I'll take Maggie." Pitying glances were cast on her wan and wasted form. The sad eyes and patient face of the little one touched many hearts. But none opened to take her in. Who wanted a bed-ridden child?

MAN 1: Take her to the poorhouse. Nobody's going to be bothered with her.

MAN 2: The poorhouse is a sad place for a sick and helpless child.

MAN 1: For your child or mine. But for this brat it will prove a blessed change, she will be kept clean, have healthy food, and be doctored, which is more than can be said of her past condition.

NARRATOR: There was reason in that, but still it didn't satisfy. The day following the day of death was made the day of burial. A few neighbors were at the miserable hovel, but none followed dead cart as it bore the unhonored remains to its pauper grave. Hastily others went out, some glancing at Maggie, and some resolutely refraining from a look, until all had gone. She was alone! Just beyond the threshold Joe Thompson paused, and said to the blacksmith's wife, who was hastening off with the rest . . .

JOE: It's a cruel thing to leave her so.

BLACKSMITH’S WIFE: Then take her to the poorhouse: she'll have to go there.

NARRATOR: For a little while the man stood with a puzzled air; then he turned back and went into the hovel again. Maggie with painful effort, had raised herself to an upright position and was sitting on the bed, straining her eyes upon the door out of which all had just departed.

MAGGIE: (with terror in her eyes) O, Mr. Thompson! Don't leave me here all alone!

NARRATOR: Though rough in exterior, Joe Thompson had a heart, and it was very tender in some places. He liked children and was pleased to have them come to his shop.

JOE: (kindly) No, dear. You sha'n't be left here alone.

NARRATOR: Then he wrapped her up in the clean bedclothes which some neighbor had brought; and, lifting her in his strong arms, bore her out into the air and across the field that lay between the hovel and his home. Now, Joe Thompson's wife, who happened to be childless, was not a woman of saintly temper, nor much given to self-denial for others' good, saw him approaching from the window, and with ruffling feathers met him a few paces from the door.

MRS. THOMPSON: (sharply) What have you there?

NARRATOR: Joe, felt the child start and shrink against him. He did not reply, except by a look that was pleading and cautionary, that said, "Wait a moment for explanations, and be gentle." He carried Maggie to the small chamber on the first floor and laid her on a bed. Then, stepping back, he shut the door, and stood face to face with his vinegar-tempered wife.

MRS. THOMPSON: (angry and astonished) You haven't brought home that sick brat!

NARRATOR: Usually Joe Thompson got out of his wife's way or kept rigidly silent when she fired up on any subject; it was with some surprise, therefore, that she now encountered a firmly-set countenance and a resolute pair of eyes.

JOE: (indignantly) Every woman at the funeral turned her eyes steadily from the sick child's face, and when the cart went off with her dead mother, hurried away, and left her alone in that old hut.

MRS. THOMPSON: Where were John and Kate?

JOE: Farmer Jones tossed John into his wagon and drove off. Katie went home with Mrs. Ellis; but nobody wanted the poor sick one. 'Send her to the poorhouse,' was the cry.

MRS. THOMPSON: Why didn't you let her go, then. What did you bring her here?

JOE: She can't walk to the poorhouse. Somebody's arms must carry her, and mine are strong enough for that task. The Guardians must be seen, and a permit obtained . . Tomorrow.

MRS. THOMPSON: Why put it off till tomorrow? Go at once for the permit and get the whole thing off your hands tonight.

JOE: (voice shaking with emotion) Jane, I read the Bible sometimes, and find much said about little children. How the Savior rebuked the disciples who would not receive them; how he took them up in his arms and blessed them; and how he said that 'whosoever gave them even a cup of cold water should not go unrewarded.' Now, it is a small thing for us to keep this poor motherless little one for a single night; to be kind to her for a single night.

NARRATOR: He turned his head away, so that the moisture in his eyes might not be seen. Mrs. Thompson did not answer, but a soft feeling crept into her heart.

JOE: (softly) Look at her kindly, Jane; speak to her kindly. Think of her dead mother, and the loneliness, the pain, the sorrow that must be on all her coming life.

NARRATOR: Mrs. Thompson did not reply, but presently turned towards the little chamber where her husband had deposited Maggie; and, pushing open the door, went quietly in. Joe did not follow; he saw that her state had changed and felt that it would be best to leave her alone with the child. So he went to his shop and worked until dusky evening released him from labor. After washing from his hands and face the dust and soil of work, Joe went to the little bedroom. A pair of large bright eyes looked up at him from the bed; looked at him tenderly, gratefully, pleadingly. How his heart swelled! Joe sat down, and now, for the first time, examining the thin frame carefully under the lamp light, saw that it was an attractive face, and full of a childish sweetness which suffering had not been able to obliterate.

JOE: Your name is Maggie?

MAGGIE: (voice quivering) Yes, sir.

JOE: Have you been sick long? Has the doctor been to see you?

MAGGIE: He used to come.

JOE: But not lately . . . Have you any pain?

MAGGIE: This morning my side ached, and my back hurt when you carried me. But it hasn't ached any since I've been on this soft bed.

JOE: The soft bed feels good.

MAGGIE: (gratitude in her voice) O, yes, sir--so good!

MRS. THOMPSON: (looking into the room) Supper is ready. (feigning indifference) She can wait until we are done; then I will bring her somethings to eat.

NARRATOR: After sitting down to the table, Joe waited for his wife to introduce the subject uppermost in both of their thoughts; but she kept silent for many minutes.

MRS. THOMPSON: (abruptly) What are you going to do with that child?

JOE: (surprised) I thought you understood that she was to go to the poorhouse.

NARRATOR: Mrs. Thompson looked rather strangely at her husband, and then dropped her eyes. The subject was not again referred to during the meal. At its close, Mrs. Thompson toasted a slice of bread, and softened, it with milk and butter; adding to this a cup of tea, she took them into Maggie. The hungry child ate with every sign of pleasure.

MRS. THOMPSON: Is it good?

NARRATOR: The child paused with the cup in her hand and answered with a look of gratitude that awoke to new life old human feelings which had been slumbering in her heart for half a score of years.

NARRATOR: At breakfast-time on the next morning . . .

JOE: [I] must step down and see the Guardians of the Poor about Maggie.

MRS. THOMPSON: (matter-of-factly) We'll keep her a day or two longer; she is so weak and helpless.

JOE: She'll be so much in your way.

MRS. THOMPSON: I sha'n't mind that for a day or two. Poor thing!

NARRATOR: Joe did not see the Guardians of the Poor on that day, on the next. In fact, he never saw them at all on Maggie's account, for in less than a week Mrs. Joe Thompson would as soon leave thought of taking up her own abode in the almshouse as sending Maggie there. What light and blessing did that sick and helpless child bring to the home of Joe Thompson! It had been dark, and cold, and miserable there for a long time just because his wife had nothing to love and care for. [But now] An angel had come into [their] house, disguised as a helpless child, and filled all its dreary chambers with the sunshine of love.
```

---

## IC-1967: Ant Farm: And Other Desperate Situations

- Title: Ant Farm: And Other Desperate Situations
- Author (byline): Simon Rich
- Work: Not specified
- Publisher: Random House Trade Paperbacks
- Publication date as stated: April 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: JUDGE, CRIMINAL, VICTIM, ME, JAKE, UNICEF, SERVANT, TEACHER, TEACHER 2, TEACHER 3, CHILD 1, CHILD 2, MR. BENDER, JONATHAN, SEYMOUR, SETH
- Teaser before the introduction: Yes
- Spoken words (computed): 1723
- Already set (do not supply): none

### Source block (context only)

```text
Author: Simon Rich
ISBN: 978-1400065882
Publisher: Random House Trade Paperbacks
Date (Month/Year): April 2007
```

### Introduction (context only: never use it for content warnings)

```text
Let’s face it . . . no matter how many times teachers and parents tell you that school is preparing you for “real life” . . . School is nothing like real life. But just to prove my point, I’d like to take you for a walk down memory lane, compliments of Simon Rich in this selection –

Ant Farm and Other Desperate Situations
```

### Performance text (classify this)

```text
Announce the title of each “scene” in a broad announcer’s voice IF LIFE WERE LIKE MIDDLE SCHOOL (Pg 25)

JUDGE: In all my years on the bench, I have never seen a more despicable criminal. You robbed, assaulted, and tortured the victim simply for the thrill of it. Do you have anything to say in your defense before I sentence you?

CRIMINAL: Nope.

JUDGE: In that case, I hereby sentence you to forty years in a maximum-security prison. I also sentence the victim to forty years in prison.

VICTIM: Wait-what? That doesn't make any sense! He attacked me!

JUDGE: I don't care who started it.

SECOND GRADE REALIZATION (Pg 7-8)

ME: Jake, come over here for a second. I need to talk to you about something.

JAKE: What's up?

ME: This is going to sound a little crazy. Oh well ... here goes. Do you remember when we were on the school bus last week and Ms. Higgins taught us that new game?

JAKE: You mean the Silent Game? Yeah, I remember. It was pretty cool of her to let us play games on the bus, huh?

ME: Well, yeah, that's what I thought at first. But then I started thinking about it. And now I'm not so sure.

JAKE: What do you mean?

ME: Well, just think about it. The Silent Game isn't actually fun. We don't do anything-we just kind of sit there. And nobody ever wins. It's always a tie.

JAKE: What are you saying?

ME: I don't think it's a real game. I think she just made it up to get us to be quiet.

JAKE: Oh my God. I think you're right.

ME: I can't believe we fell for it. We were silent for almost twenty minutes!

JAKE: We have to tell the class!

ME: What's the point? They'd never believe us.

JAKE: What about all the other games she taught us? The Politeness Game . . . the Respect Game . . . the Clean Up the Tables Game . . .

ME: What about them?

JAKE: Those might be fake too.

ME: Whoa. You just blew my mind.

JAKE: This has got to be the craziest day of my life. A DAY AT UNICEF HEADQUARTERS AS I IMAGINED IT IN THIRD GRADE (Pg 9-10) [UNICEF sits on a throne. He is wearing a cape and holding a scepter. A servant enters on his knees.]

UNICEF: Halloween is fast approaching! Have the third graders been given their little orange boxes?

SERVANT: Yes, your majesty!

UNICEF: Perfect. Did you tell them what the money was for?

SERVANT: No, sir, of course not! We just gave them the boxes and told them to collect for UNICEF. We said it was for "a good cause," but we didn't get any more specific than that.

UNICEF: Ha ha hal Those fools! Soon I will have all the money in the world. For I am UNICEF, evil king of Halloween!

SERVANT: Sir . . . don't you think you've stolen enough from the children? Maybe you should let them keep the money this year?

UNICEF: Never! The children shall toil forever to serve my greed! [UNICEF tears open a little orange box and rubs the coins all over his fat stomach.] Yes! Oh, yes!

SERVANT: Wait-your majesty! Look at this! Our records indicate that there's a kid out there-Simon-who's plan-ning to keep his UNICEF money this year.

UNICEF: What?!? But what about my evil plans? I was going to give that money to the Russians so they could build a bomb!

SERVANT: I guess there's still one hero left in this world.

UNICEF: Noooo! [Runs out of castle, sobbing.]

SERVANT: Thank God Simon is keeping his UNICEF money. I STILL REMEMBER THE DAY I GOT MY FIRST CALCULATOR (Pg 11-12)

TEACHER: All right, children, welcome to fourth grade math. Everybody take a calculator out of the bin.

ME: What are these?

TEACHER: From now on we'll be using calculators.

ME: What do these things do?

TEACHER: Simple operations, like multiplication and divi-sion.

ME: You mean this device just . . . does them? By itself?

TEACHER: Yes. You enter in the problem and press equal.

ME: You . . . you knew about this machine all along, didn't you? This whole time, while we were going through this . . . this charade with the pencils and the line paper and the stupid multiplication tables! . . . I'm sorry for shouting . . . It's just . . . I'm a little blown away.

TEACHER: Okay, everyone, today we're going to go over some word problems.

ME: What the hell else do you have back there? A magical pen that writes book reports by itself? Some kind of automatic social studies worksheet that . . . that fills itself out? What the hell is going on?

TEACHER: If a farmer farms five acres of land a day

ME: So that's it, then. The past three years have been a total farce. All this time I've been thinking, "Well, this is pretty hard and frustrating but I guess these are useful skills to have." Meanwhile, there was a whole bin of these things in your desk. We could have jumped straight to graphing. Unless, of course, there's some kind of graphing calculator!

TEACHER: There is. You get one in ninth grade.

ME: Is this . . . Am I on TV? Is this a prank show? OUR THOUGHTS ARE WITH YOU (Pg 15-17) [Teachers writing a note home to a parent]

TEACHER 2: Dear Mrs. Matthews, I am writing to express my deepest sympathies. I shared your last note with Caleb's classmates and they made a card (which I have enclosed). Ten funerals in three weeks is a lot to ask of any child, let alone a child like Caleb, who has already suffered so many family deaths this month. At first, as humiliating as it is to admit, I thought your son had forged the notes. But denial quickly gave way to grief. I understand he has another funeral to attend on Wednesday and that it will last until Friday. Please let him know that he can take as much time off as he needs.

TEACHER 3: I would volunteer to drop off Caleb's home-work myself, but I understand that your house recently exploded. Of all the tragedies that have befallen your family, this one saddened me the most. For a house to suddenly explode, without warning, destroying a child's backpack and books, is very upsetting, particularly in the midst of your High Voodoo Holidays.

TEACHER 2: I was also deeply saddened to learn that your son had suffered brain damage and could no longer complete his social studies assignments. To be hit with such a misfortune, on top of Tourette's, is a blow to any child's self-esteem.

TEACHER 3: Incidentally, I understand that Caleb has recently taken on some serious community service projects. I totally understand Caleb's devotion to the blind, particularly in light of his own blindness. But I'm worried that his extracurricular activities might interfere with his schoolwork, especially on top of the pressures of his upcoming Voodoo Bar Mitzvah. Of course, it's your decision.

TEACHER 2: I would also like to take this opportunity to congratulate you on your son's recent achievement! To be named an FBI super-spy at such a young age is an amazing accomplishment, particularly for a child who suffers from so many varied forms of brain damage. He hasn't told me much about his mission, but from what I gather it sounds like an incredible opportunity. I'm going to miss his presence in the classroom next year, but it would be selfish of me to stand in his way. Caleb's country needs him more than I do. He belongs in Russia.

TEACHER 3: Rest assured: I haven't told anyone about Caleb's mission, not even the principal. I am honored that Caleb felt he could trust me with top secret information, and I would never betray that trust.

WHAT GOES THROUGH MY MIND WHEN I’M HOME ALONE (Pg 36-27) (From My Mom’s Perspective)

CHILD 1: Hmm, Mom left me home alone. Better go through the medicine cabinet and drink all the medicine for no reason. Wait, what's this? A note telling me not to "drink any medicines"? Thank God! I was about to do that. I was about to drink all the medicines.

CHILD 2: Well, I better use the stove and then not turn it off. That way, I'll burn down the house and kill myself. Wait a minute. There's a note that says I should "turn off the stove after using it." [WOW], that never would have occurred to me! Mom saved my life again, twice in one night.

CHILD 1: Well, better throw things out the window, something I haven't done since I was seven. I'm fifteen years old, but I haven't matured at all. I still need to be reminded constantly about how to get through the day. What? A note? Guess I shouldn't "throw objects out the window" after all. There go my big plans.

CHILD 2: Ah . . . dinnertime. There's a Tupperware container full of pasta in the fridge, but it's cold! How will I ever heat it up? I guess I'll just starve and die because I'm not competent enough to warm pasta. Whoa! A note telling me to put the container in the microwave and press EASY MINUTE! Thanks, note! You saved my life.

CHILD 1: I hope that when my mom comes home she asks me some very specific, humiliating questions about my changing body. SEX ED (Pg 44-45)

MR. BENDER: Okay class, now it's time to read one of your anonymous sex questions out loud. Here's one . . .

JONATHAN: Hey, Seymour, did you write that one? That looks like your handwriting.

SEYMOUR: Mr. Bender! Don't read it!

MR. BENDER: Please, no talking. It's very important that I answer this question. Whoever asked it is obviously incredibly confused about sex. These are not normal concerns. Not even close.

SETH: Hey, I bet that's Seymour's question. It's written in blue ink like all his homework assignments.

SEYMOUR: Oh, no!

MR. BENDER: Okay, let's see ... it's a seven-part question. The first part is about testicles.

SEYMOUR: Oh my God!

MR. BENDER: Quiet, class. We have to be fair to the boy who wrote this, even if we find his sexual desires morally reprehensible.

JONATHAN: Hey, I think that's Seymour's stationery. I can tell because of the watermark.

MR. BENDER: All right. I'm going to read the question now. But I have to warn you: It's pretty hard to take. If you feel like screaming, that's understandable. I'm probably going to do some screaming myself. It's that extreme. (Bell rings.)

SEYMOUR: That's the bell! Class dismissed!

MR. BENDER: Stay in your seats, everyone. If I don't an-swer this student's question, he could permanently damage his body. Okay. . . here it goes. . . [WOW}, I can't read this out loud, it's too humiliating. Can I have a volunteer?

SEYMOUR: I'll read it! . . . Great! Um . . .okay . . . it says . . . What do you do if you are a . . . normal boy . . . with no really weird things.
```

---

## IC-1968: Are We There Yet?

- Title: Are We There Yet?
- Author (byline): Andy Griffiths
- Work: Just Annoying!
- Publisher: Scholastic
- Publication date as stated: Dec 2003
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ANDY, DAD, MUM, BIKE MAN, MAX
- Teaser before the introduction: Yes
- Spoken words (computed): 1971
- Already set (do not supply): none

### Source block (context only)

```text
Author: Andy Griffiths
Book: Just Annoying!
ISBN: 978-0439424714
Publisher: Scholastic
Date (Month/Year): Dec 2003
```

### Introduction (context only: never use it for content warnings)

```text
Parents, everywhere, I get it. You love your children, but getting into a car with them is like a stepping through the gates of hell. Something about a moving vehicle causes them to do and say the most infuriating things, and because you're behind the wheel, you're powerless to stop it.

I remember those long road trips and from a kid standpoint, they really are BORING! But not this one . . . . Are We There Yet? By Andy Griffiths.
```

### Performance text (classify this)

```text
ANDY: Dad?

DAD: Yes?

ANDY: Are we there yet?

DAD: No.

ANDY: Now?

DAD: No.

ANDY: Now?

DAD: For goodness sakes! Will you stop it!

ANDY: Alright. Don’t get your knickers in a knot.

ANDY: We’ve been in the car for two days now. Mum and Dad are at a breaking point. Don’t get me wrong. I don’t want them to get mad at me – it just happens. Like it or not, when you go on a long drive there are times when you just have to stop. And my parents do not like it. But what’s the alternative? Do they want me to starve to death? To wet my pants? To be sick all over the back seat? I think any of these would be a lot more annoying and inconvenient than the few stops it takes to prevent them. I’m actually doing them a favour. Mum and Dad should save their energy for really annoying things. Like the fly that has been buzzing around in the car for the last half hour. It’s driving me mental. I’m going to do us all a big favour. I’m going to get rid of it. I wind the window down. The fly jumps away. It’s hiding, just waiting for me to wind the window back up again. I have to lure it out. I start doing my best fly-call. Bzzzz! Bzzzzzzzz! Bzzzzzzzzzz! Still no fly. Have to do it louder: BZZZZ! BZZZZZZZ! BZZZZZZZZ!

DAD: Andy! I can’t concentrate with you making that stupid noise. Do you want us to have an accident? Do you want us all to be killed?

ANDY: I hate it when Dad asks dumb questions like that. What does he expect me to say? ‘Yes, Dad, I want us to have an accident. I want us all to be killed.’ But I don’t say that. Instead I say: Alright, Dad. Don’t get your knickers in a knot.

DAD: (Exploding) And stop telling me not to get my knickers in a knot!

ANDY: Okay, Don’t get your trousers in a twist. Dad hunches over the steering wheel. His knuckles whiten. Tiny drops of perspiration appear on the back of his neck. He knows he’s been outsmarted once again. It must be frustrating for him having a [child] as clever as me. It must be hard knowing he can never win. The fly lazily cruises in front of my eyes. It’s asking for trouble. Well, it’s come to the right [place]. I once saw a movie where the door of an aeroplane opened mid-air and everybody was sucked out by the vacuum it created. I don’t need a vacuum quite that powerful, but maybe if I open and close the door I’ll be able to create on strong enough to suck the fly out. I squeeze the door handle as carefully and slowly as I can so that it doesn’t make any noise. I swing it open, then shut. Open, shut. Open, shut

DAD: (Screams) What do you think you’re doing?

ANDY: I’m creating a vacuum.. I’m trying to get a fly out of the car.

DAD: (Shouting) Shut the door! And keep it shut! I’m warning you.. If you don’t behave yourself, I’ll stop the car and you can get out and walk. Do you understand?

ANDY: But, Dad

DAD: No buts! Do you understand?

ANDY: Dad’s knuckles are really white now. He’s gripping the steering wheel so hard that his bones are practically breaking through his skin. I hear a buzz. It’s coming from behind me. The vacuum didn’t work. I turn around but I can’t see the fly. Hang on – the noise is coming from outside. I undo my seatbelt and kneel up on the seat to get a better view. There’s this crazy-looking guy riding an old black Harley. He’s go a long red beard, a black bowl-shaped helmet and a pair of old-fashioned plastic riding goggles. They make him look like a fly. And his motorbike sounds like one. Only much louder. Suddenly the fly shoots across the window. Showdown time! I try to cup it in my left hand and hook it out of the window. That’s my plan, anyway. But the fly has other ideas. It skates across the window to the far corner. And then back again. I’m chasing the fly back and forth across the window when I notice that the biker is making hand signals. He thinks I’m waving to him! I wave. He waves back. I wave again. We’re best friends now.

DAD: Stop waving. Sit down and put your seatbelt back on.

ANDY: But he waved first.

DAD: Sit down!

ANDY: Okay, okay, don’t get your knickers in a knot. I give one last wave to Bike-man, but he’s pulling into a service station and doesn’t see me. I feel like I’ve lost my best friend. I notice a movement out of the corner of my eye. I look up. The fly is on the roof. It’s taunting me. It buzzes again. I have to get rid of this fly. And quickly. Before it gets rid of me. I reach up and try to cup it with my hand. It jumps to the left. I try again. It jumps to the right and then heads towards the front, daring me to come after it. I unbuckle my seatbelt and dive into the front seat. I catch the fly in mid-air. (yelling) HOWZAT!

I’m lying with my head in Mum’s lap and my legs all over the steering wheel. Dad slams the brakes on.

DAD: Get out!

ANDY: But it’s not my fault. It was the fly.

DAD: I don’t care whose fault it was. Out!

ANDY: Surely he can’t be serious. I’m sorry, Dad . . . I was just trying to get the fly out of the car . . . in case it caused an accident.

DAD: You’re the only one who is going to cause an accident. Out.

ANDY: Mum? Are you going to let him do this?

MUM: It’s for your own good. You’ve got to learn.

ANDY: I open the door. You’ll be sorry when you come back and find my bones being picked clean by vultures.

DAD: Shut the door. You’re letting the hot air in.

ANDY: There’s no reasoning with him. I get out of the car and shut the door slowly. The wheels of the car spin. I am showered by gravel. I wipe the grit out of my eyes and look for the car. It’s gone. They’ll be back. Any second. Five minutes tops. Just enough to give me a scare. I start walking. Actually, it’s quite nice. Fresh air. Blue sky. Space. No grumpy parents.

Five minutes pass. Another five minutes. And another five minutes. Where are they? I should just lie down and die – that would teach them. The only trouble is that it could take a while because I’m actually feeling pretty healthy. I hear a droning sound in the distance. Ha! I check my watch. It took them fifteen minutes to give in and come back and get me. That’s really going to teach me a lesson I’ll never forget. NOT. But as I listen, I notice the drone has a different quality. Not the putty-putt-putt sound of Dad’s car at all. It’s Bike-man! I jump up and wave. He waves back and pulls up alongside me. He looks even crazier close up. His beard is full of insects. Some of them are still alive.

BIKE MAN: Well, if it isn’t my little mate. What are you doing out here all by yourself?

ANDY: My parents threw me out of the car. They told me I had to walk.

BIKE MAN: Max. (he shakes Andy’s hand) Hop on then.

ANDY: He hands me a helmet. It’s just like the one he’s wearing. My stomach drops as he accelerates up the road. I grab him around the waist. Roaring wind. My whole body shaking and vibrating. I’m freezing. I see Mum and Dad’s car in the distance. (yelling) That’s them! As we pull closer to the car, I signal Max to blow his horn to let them know I’m here. He blasts. I wave. But they don’t stop. If anything they seem to speed up. Max! Go up next to them. I don’t think they realise it’s me. I wave. Hey, Stop! No reaction. I wave both h ands. Dad flicks a nervous glance across at me, but he doesn’t show any sign of recognition. Instead he hunches over the wheel and pulls away from us at high speed. WOW! I never knew the car could go so fast. Max accepts the challenge. He speeds up. We’re back beside them.

MAX: They’re not going to stop! You’re going to have to board ‘em.

ANDY: He’s joking. He’s got to be. Either that or he’s completely insane. He rides right up beside the car and signals for me to stand. I kneel on the seat. I hold on to Max’s shoulders and pull myself up. My legs are shaking. Max edges in as close as he dares. My stomach is churning. I don’t want to do this. I’m too young to die! I can’t do it. Why can’t I stay with you? I’ll be your apprentice.

MAX: (laughing) Highway’s no place for a nice kid like you. Go back. Finish school

ANDY: I’m not nice. I’m really annoying. He has a wild look in his eyes. Maybe staying here is not such a great idea after all. I stand up again. I take a deep breath. I close my eyes. Clench my fists. Goodbye cruel world! The wind picks me up and sends me hurtling sideways. Thump! I land on the car roof. I made it! Dad s tarts swerving all over the road. He’s trying to shake me off. I’ve got to make him realise it’s me. I bang on the roof. Dad swerves harder. If I can just let him see it’s me he’ll slow down. I push myself down in front of the windscreen. Mum and Dad freak. Eyes wide. Mouths open. The car stops. It’s over. Mum and Dad get out. I take off my helmet.

DAD: This is the limit! The absolute limit! What are you trying to do – get yourself killed?

ANDY: More dumb questions. No, I was trying to get back into the car. You threw me out, remember?

DAD: Yes, to teach you a lesson

ANDY: What sort of lesson is that? To abandon me in the middle of nowhere with no food, no drink, no map and no sunscreen.

MUM: We were going to come back.

ANDY: When? On your way home?

DAD: We were about to come back and get you when the bikie started chasing us. I was trying to lead him as far away from you as possible. Some of these characters can be pretty dangerous, you know.

ANDY: I get into the car. I don’t want to hear any more excuses, Dad. You tried to get rid of me. You failed. Let’s go. He starts the engine. He’s feeling bad now. He should be. We pull out onto the road. [Then] I see the fly. It’s sitting right on top of Dad’s head. (quietly) It’s all your fault. I’ve been abandoned Almost missed out on my holiday. Risked my life. It’s all your fault – and you’re going to pay. I sit up close behind dad. I hold my hands just above his head, ready to smash the fly. It jumps. The movement distracts me. I clap Dad over both ears instead. Oops! Dad, I’m sorry – it was a mistake. See, I was trying to . . .

DAD: It’s okay. You don’t have to explain. We all make mistakes.

ANDY: Oh, I get it. Mum and Dad won’t try to put me out of the car again. No matter what I do. They’ve used their biggest threat and it didn’t work. It just made them feel bad. I can do anything now. Anything I want. This might not turn out to be such a boring trip after all. I just have one question . . . Dad . . . . Are we there yet?
```

---

## IC-1969: Around the World in a Bad Mood!

- Title: Around the World in a Bad Mood!
- Author (byline): Renee Foss
- Work: Not specified
- Publisher: Hyperion Press
- Publication date as stated: March 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: FA, WIRT, CAPTAIN, NEW FA, PASSENGER, NEW FLIGHT ATTENDANT
- Teaser before the introduction: Yes
- Spoken words (computed): 1498
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rene Foss
ISBN: 978-0786890118
Publisher: Hyperion Press
Date (Month/Year): March 2002
```

### Introduction (context only: never use it for content warnings)

```text
Around the World in a Bad Mood! Confessions of a Flight Attendant by Rene Foss
```

### Performance text (classify this)

```text
NOTE: Words appearing in [ ] are added as transitional items.

FLIGHT ATTENDANT (FA): Good morning, ladies and gentlemen! In a few moments we'll begin the breakfast service in the main cabin. We have a wide selection of choices for you today. You may have any or all of the following items: Prozac, Zoloft, Viagra, Ecstasy, Ritalin, Cele-brex, or scrambled eggs. Some of these items may cause side effects, such as dry mouth, fatigue, internal bleeding, temporary blindness; and leprosy. Again, your choices include Prozac, Zoloft, Viagra, Ecstasy, Ritalin . . . oh, one moment please. My apologies, ladies and gentlemen, that is the flight attendants' breakfast menu!

(to audience) I am a flight attendant and the world is my oyster. And what an oyster it is! Oversold flights, weather delays, air traffic control delays, center seats, crappy food, air rage - it's so glamorous! Kind of like a Greyhound bus in the sky. This is just a glimpse into my life . . . a story about air travel, flight attendants, and me!

So . . . fasten your seat belts, raise your tray table, and stow your bag . . . The journey is about to begin. Welcome to my nightmare!

*WIRT – What I’m Really Thinking

FA: Welcome aboard, sir, so glad you could join us today. You have seat 4B. Get you a gin and tonic? My pleasure.

WIRT: Pleasure, my a**. I'd rather watch paint dry.

FA: Here you go, sir. Oh, you couldn't find room for your carryon? You're tired of lifting it and you want someone to get it out of your way?

WIRT: And I guess I'm the lucky someone. I cannot believe my good fortune. Jesus, what has he got in here? A dead body? If this six-foot, 200-pound bruiser can't lift it, how does he possibly think I can lift it?

FA: You know, sir, I think this bag is a little big for the overhead. Perhaps I could check it to your final destination?

WIRT: Better yet, perhaps I could check you to your final destination and put the bag in your seat. The bag would probably be a lot more interesting.

FA: Unacceptable, you say?

WIRT: I'll tell you what's unacceptable: your personality! He probably thinks just because he's sitting in first class that he's entitled to be rude to everyone in the world. Well, I'm checking this bag, whether Mr. Congeniality likes it or not. (begins dragging it up the aisle)

FA: Oh, I didn't mean to disturb you . . . Yes, well, it looks like the only available option is to check it. It sort of exceeds the size requirements.

WIRT: A little bit like your ego, pal. Oh boy, he's getting up now. Well, that got him into action! Probably hasn't moved that fast in years. My, my, look at those muscles .... Amazing how he can heave that two-ton bag into the overhead. Just 2 minutes ago he didn't have the strength.

FA: Thanks so much for helping with your bag. I'm glad we didn't have to check it . . . My name?

WIRT: My name . . . what does he want my name for? It's not like we're going to be buddies. In fact, if things work out the way I am hoping we will never see each other again. So why on God's green earth does he need to know my name? He's probably going to write me up. (outraged) I'm just doing my job, risking my chiropractic good health trying to help this brute with his bag. And what do I get? This idiot requesting my name. Maybe I'll just make up a name . . .

FA: Oh no, you don't need to apologize. I'm sure you've had a hard day and having to tow that heavy bag of yours around has got to be tiring. . .

WIRT: I'll give you a hard day ... my day! Five stops between Chicago and Indianapolis, airplanes of people just like this jack***. And I've got to do the same thing tomorrow and the next day, too. What did I ever do to deserve this? God, I hate my life.

FA: Tonight? Well, I'm flattered. . . Oh yes, I'm sure there's a lot of great nightlife, but I really have to get to bed early tonight because I have to wake up at 7:00 A.M. Oh, aren't you funny, you won't take no for an answer . . .

WIRT: Oh, he's funny all right. Funny as a crutch.

FA: . . . . I guess as long as I'm back by a reasonable hour -- why not? I accept, sir. Charlie? OK, Charlie. I'm really looking forward to it.

WIRT: I'm looking forward to it about as much as I'm looking forward to paying my taxes or getting a root canal.

FA: I'll be right back! *******

FA: (to audience) And there you are . . . curled up in a little ball, sucking your thumb, on the verge of uncontrollable sobbing, when the captain makes an announcement:

CAPTAIN: Ladies and gentlemen, I have some bad news: It appears we will be here for at least another hour. Please let us know if there’s anything we can do to make you more comfortable. Thank you.” . . . .

FA: ARGGHHHH!! *********

NEW FA: TESTING, ONE-TWO-THREE . . . hello? Is this thing on? Oh, for Christ's sake OK. Welcome aboard We Apologize for This Inconvenience Airlines, also known as WAFTI. This flight is under the command of Captain Booze, assisted by First Officer Chance, and as we like to say here at WAFTI, if Booze and Chance can't get ya there . . . nothing can!

For your comfort we have four lavatories on this aircraft: one in first class and three in coach. However, only one is working, so pace yourself! The airphones are not working, we have only three pillows and two blankets. We do not have any magazines or newspapers, but we do have the pamphlet How to Deal with Anger in a Positive Non-violent Way. Today we will be passing these pamphlets out in lieu of the meals. We here at WAFTI appreciate your business and we want you to know that we're constantly upping our standards . . . So up yours! Now it is time for the safety demonstration. This informa-tion could save your life so please pay attention! It's time for the 'Safety Demo Shuffle.' (Attendant raps and moves to the beat, the more awkward the better . . . with enthusiasm!) SAFETY DEMO SHUFFLE If you've never traveled by car this is your seat belt, please know where they are. To fasten the belt, just pull till it's tight and don't let go till the end of the flight! This is for safety, especially yours, pay close attention as we point out the doors, please keep in mind this aircraft has eight, they all have slides and we hope they inflate. If we have to get out, there won't be much time, so head for the door and follow in line, should the cabin lose pressure, place this mask on your nose, if the plane's going down, just reach for your toes, if we have a water evacuation, use your tushy cushion for your flotation, pull up and remove, then hold to your chest, dive in the water, and hope for the best! A few more reminders, then off on our way: No smoking, no cell phones, no meals today! Thank you for flying, we're glad to arrive. If you want to get there faster, if you want to get there sooner, if you just want to get there why don't you drive??? We dooooooo!!!!!

*******

FA: Hello, can I get you a beverage?

PASSENGER: Yes, I'll have a can of tomato juice, a bottle of water, and two cups of coffee with cream and sugar.

FA: Are you ordering for the whole row?

PASSENGER: No, just for me . . . I'm kind of thirsty.

FA: Anything else?

PASSENGER: Yeah, now that you mention it, I'll have a can of apple juice for later.

FA: Airline food has been the butt of many jokes over the years. People make fun of its quality, color, taste (or lack thereof), but as soon as you take it away people miss it! People used to complain about the food choices we offered:

PASSENGER: All you have are three choices?! And all of them terrible! My God, what is the world coming to?

FA: Then as we incurred some cutbacks and started giving everyone the same meal, people were downright appalled.

PASSENGER: You mean everyone is getting the chicken? This is horrifying, I can't believe I don't have a choice!

FA: (to passenger) But, you do have a choice: eat or don't. (to audience) Now, as cost-cutting measures continue, we have not only eliminated the choice, but on certain flights we've eliminated the meal service altogether. Airlines are in the transportation business, not the restaurant business! As a passenger you are paying for transport from here to there, not for the bologna sandwich that we throw in your face. When the airline tells you they'll be serving a five-course meal, it means an apple, a granola bar, cheese, crackers, and a mint in a paper bag. . . The last thing I'd like to remind people is that the flight atten-dants, just like waiters, are the last ones to touch your food or beverage before you consume it. Keep this in mind at all times and bon appetit!

NEW FLIGHT ATTENDANT: (end of the flight) We here at WAFTI appreciate your business and we want you to know that we're constantly upping our standards . . . So up yours! Buh bye!
```

---

## IC-1970: Ashes

- Title: Ashes
- Author (byline): David Sedaris
- Work: Naked, Pgs 234-250
- Publisher: Little, Brown and Company
- Publication date as stated: March 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: TO BE SUNG, NARRATOR, MOM, BOB, FATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1780
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Sedaris
Book: Naked, Pgs 234-250
ISBN: 978-0316779494
Publisher: Little, Brown and Company
Date (Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
That’s what it feels like . . . when your mother is diagnosed with terminal cancer . . . like a runaway train. All you want to do is to go back to the way things used to be. The way things were before you knew your mom was going to die soon.

David Sedaris was a young adult when his mother was diagnosed with stage 4 lung cancer. It was the same year that his sister Lisa got married. A beginning and an ending – the conflict of emotions is clear in Ashes by David Sedaris.
```

### Performance text (classify this)

```text
TO BE SUNG: Stop This Train by John Mayer

Don’t know how else to say it, don’t want to see my parents
go
One generation’s length away from fighting life out on my
own
Stop this train, I want to get off and go home again
I can’t take the speed it’s moving in
I know I can’t
But honestly, won’t someone stop this train.
Lyrics by John Mayer

(Check out the melody here https://www.youtube.com/watch?v=5BTzNX5OMN4)

NARRATOR: (Pgs 234-250) After living with her boyfriend, Bob, for close to ten years, my sister Lisa agreed to marry him. They decided the wedding would take place not at a drive-through chapel in Las Vegas but on a mountaintop in western North Carolina.

MOM: That's nice. Now all I need is a pair of navy blue hiking boots to match my new dress and I'll be all set.

NARRATOR: We liked Bob because he was both different and unapologetic.

BOB: (flipping back his waist-length braid) You take a day-old pork chop, stab it with a fork, and soak it in some vinegar and you've got yourself some good eatin'.

NARRATOR: Bob eventually cut his hair and returned to college, for a career in corporate real estate. He was a likable guy; it was the marrying part that got to me. "My sister's wedding" was right up there with "my recent colostomy" in terms of three-word phrases I hoped never to use. (beat) Three weeks before the wedding, my mother called to say she had cancer. She'd gone to a doctor complaining about a ringing in her ear, and the resulting tests revealed a substantial tumor in her lung.

MOM: They tell me it's the size of a lemon. Not a tiny fist or an egg, but a lemon. I think they describe it in terms of fruit so as not to scare you, but come on, who wants a lemon in their lung? They're hoping to catch it before it becomes a peach or a grapefruit, but who knows? I sure as hell don't. Twenty-odd tests and they still haven't figured out what's wrong with my ear. I'm just hoping that whatever it is, it isn't much larger than a grape. This cancer, though, I realize it's my own fault. I'm just sorry your father's still around to remind me of that fact every fifteen goddamned seconds.

NARRATOR: My sister Amy was with me when my mother called. We passed the phone back and forth across my tiny New York kitchen and then spent the rest of the evening lying in bed, trying to convince each other that our mother would get better but never quite believing it. I'd heard of people who had survived cancer, but most of them claimed to get through it with the aid of whole grains and spiritual publications that encouraged them to sit quietly in a lotus position. They envisioned their tumors and tried to reason with them. Our mother was not the type to greet the dawn or cook with oats and barley. She didn't reason, she threatened; and if that didn't work, she chose to ignore the problem. We couldn't picture her joining a support group or trotting through the mall in a warm-up suit. Sixty-two years old and none of us had ever seen her in a pair of slacks. I'm not certain why, but it seemed to me that a person needed a pair of pants in order to defeat cancer. Just as important, they needed a plan. They needed to accept the idea of a new and different future, free of crowded ashtrays and five-gallon jugs of wine and scotch. They needed to believe that such a life might be worth living. I didn't know that I'd be able to embrace such an unrewarding future, but I hoped that she could. My brother, sisters, and I undertook a campaign to bolster her spirits and suggest new and exciting hobbies she might explore once she was cured and back on her feet.

(To Mom) It'll be great. You could, I don't know, maybe you could learn to pilot small planes or volunteer to hold crack babies. There are a lot of things an older person can do with her time rather than smoke and drink.

(to audience) The cancer was too far advanced and she was too weak to survive an operation. The doctor decided to send her home while he devised a plan. The very word sounded hopeful to us, a plan. (excitedly) "The doctor has a plan!"

MOM: Right. He plans to golf on Saturday, sail on Sunday, and ask for my eyes, kidneys, and what's left of my liver on that following Monday. That's his plan.

NARRATOR: We viewed it as a bad sign when she canceled her subscription to People magazine and took to buying her cigarettes in packs rather than cartons. She went through her jewelry box, calling my sisters to ask if they preferred pearls or gems.

MOM: Right now, the rubies are in a brooch shaped like a candy cane, but you can probably get more money if you have them removed and just sell the stones.

NARRATOR: In her own way she had already begun to check out, giving up on the plan before it was even announced. But what about us? I wanted to say. Aren't we reason enough to carry on? I thought of the unrelenting grief we had caused her over the years and answered the question myself.

If she'd had it her way, we would never have known about the cancer. It was our father's idea to tell us, and she had fought it, agreeing only when he threatened to tell us himself. Our mother worried that once we found out, we would treat her differently, delicately. We might feel obliged to compliment her cooking and laugh at all her jokes, thinking always of the tumor she was trying so hard to forget. And that is exactly what we did. The knowledge of her illness forced everything into the spotlight and demanded that it be memorable. We were no longer calling our mother. Now we were picking up the telephone to call our mother with cancer. We realized that any conversation might be our last, and because of that, we wanted to say something important. What could one say that hadn't already been printed on millions of greeting cards and helium balloons? (on the phone with Mom) I love you.

MOM: I am going to pretend I didn't hear that.

NARRATOR: I heard a match strike in the background, the tinkling of ice cubes in a raised glass. And then she hung up. I had never said such a thing to my mother, and if I had it to do over again, I would probably take it back. It was queer to say such a thing to someone unless you were trying to talk them out of money or into bed, our mother had taught that when we were no taller than pony kegs.

We gathered together for the wedding, which took place on a clear, crisp October afternoon. The ceremony was held upon a grassy precipice that afforded magnificent views of the surrounding peaks, their trees resplendent in fiery red and orange. My father wept openly during the ceremony. The rest of us studied his crumpled face and fought hard not to follow his example. What was this emotion? My sister was getting married to a kind and thoughtful man who had seen her through a great many hardships. Standing in a semicircle on top of that mountain, it became clear that while Lisa might take on a different last name, she could never escape the pull of our family. The ceremony inspired a sense of loss directed not at Lisa, but at our mother. We knew, everyone on that mountaintop knew, that she had cancer. That she was going to die. (beat) . Over the years our mother had repeatedly voiced her desire to be cremated. We would drive past a small forest fire or observe the pillars of smoke rising from a neighbor's chimney, and she would crush her cigarette, saying,

MOM: That's what I want, right there. Do whatever you like with the remains; sprinkle them into the ashtrays of a fine hotel, give them to smart-assed children for Christmas, hand them over to the Catholics to rub into their foreheads, just make sure I'm cremated.

FATHER: (groaning) Oh, Sharon . . . You don't know what you want.

NARRATOR: [My father’d] say it as though he himself had been cremated several times in the past but had finally wised up and accepted burial as the only sensible option. [My sisters and I] [spent our time together] trying to imagine a life without our mother. Why couldn't she just stay where she was and not have cancer? That was always our solution, to go back in time. We discussed it the way others spoke of bone marrow transplants and radiation. We discussed it as though it were a viable option. A time machine, that would solve everything. I could almost see its panel of blinking lights, the control board marked with etched renderings of lumbering dinosaurs and ending with Lisa's wedding. We could turn it back and view our mother as a young girl, befriend her then, before her father's drinking turned her wary and suspicious. See her working in the greeting-card section of the drugstore and warn her not to drop out of school. Her lack of education would make her vulnerable, causing her to overuse the phrase

MOM: Well, what do I know? I'm just an idiot, but…

NARRATOR: We could turn it back and see ourselves as babies, our mother stuck out in the country with no driver's license, wondering whom to call should someone swallow another quarter or safety pin. The dial was ours, and she would be at our mercy, just as she had always been, only this time we would pay attention and keep her safe. We hoped that by preparing ourselves for the worst, we might be able to endure the inevitable with some degree of courage or grace. Anything we forecasted was puny compared to the future that awaited us. You can't brace yourself for famine if you've never known hunger; it is foolish even to try. The most you can do is eat up while you still can, stuffing yourself, shoveling it in with both hands and licking clean the plates, recalling every course in vivid detail.

Our mother was back in her room and very much alive, probably watching a detective program on television. Maybe that was her light in the window, her figure stepping out onto the patio to light a cigarette. We told ourselves she probably wanted to be left alone . . . frightened and alone, staring at the tip of her cigarette and envisioning herself, clearly now, in ashes.
```

---

## IC-1971: Atomic Blue Pieces

- Title: Atomic Blue Pieces
- Author (byline): Angela Johnson
- Work: The Color of Absence (Pg 41-48)
- Publisher: Atheneum Books
- Publication date as stated: Jan 2003
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1456
- Already set (do not supply): none

### Source block (context only)

```text
Author: Angela Johnson
Book: The Color of Absence (Pg 41-48)
ISBN: 978-0689856679
Publisher: Atheneum Books
Date (Month/Year): Jan 2003
```

### Introduction (context only: never use it for content warnings)

```text
For years, movies and country music have pointed out the benefits of living in a small town. A strong sense of community; everyone knows everyone and life is lived at a much slower pace. It’s quiet and peaceful and it’s easy to see the appeal for many who are exhausted by the rat race of the bigger cities. But what these idealized benefits hide are the downfalls: 1) Anonymity is a foreign concept, 2)

There is literally nothing to do, 3) Limited career options, which results in higher levels of poverty. For many who were born into small town life, it can often seem like there’s no way out.

Atomic Blue Pieces by Angela Johnson
```

### Performance text (classify this)

```text
NARRATOR: (Pg 41-48) The day my brother Leon left, I broke my leg falling down the steps of an old deserted building that Mama had told me not to go in. I lay there half a day.

Somebody told me once you can't die from pain, even if you want to. You can make your world what you want it to be sometimes. So, there wasn't any pain for me, for a while. No pain. No busted leg. No pain.

If you count between thunderclaps during a storm you'll know whether the storm is coming or going during the next count. Lower number-it's coming at you. Higher number-it's leaving. I can count during a storm.

NARRATOR: The morning before Leon left he shared half his toast with me and most of his bacon. We didn't get bacon that much, either. He'd sat there smiling at me while I picked out of his plate and babbled about nothing. Mama had already told me to be quiet, twice. Leon gave her dirty looks, though, and smiled back at me. I'd run my bare feet underneath the chair. The linoleum was gritty and cold. Leon kept smiling.

I found out that night after I'd gotten back from the emergency room that Leon was gone. I took an Atomic Blue Magic Marker and wrote my brother's name all over my cast. The day my brother Leon left was mostly white light and pain. But it also was atomic blue, bacon, and his face.

Chalky's Trailer Park is wedged up against Route 82 and Cave Man Woods. Everybody who grows up there spends most of their lives listening to people yelling at them to stay off the highway and not go into the swamp woods. That meant until you are sixteen or have a friend who can drive, you're stuck at Chalky's. Even though I'd been stuck, I'd had Leon and Cougar. We hung out in the swamp like all the kids who lived at Chalky's. It was all something else then. Something I could live with.

Didn't they know that they couldn't keep us away from everything that we were looking for? Didn't they know that sooner or later . . . Sooner or later . . .

Maybe Mama knew about sooner or later. Maybe she knew it when she'd go out with her girlfriends at Star Lanes Bowling. Maybe she even knew about sooner or later when she'd sit in the front window of our trailer all night long listening to Sam Cooke records and playing solitaire.

I only remember Mama at these times because of extremes. Extreme cold. Extreme heat. Leon says Mama is intense. And I wondered out loud once if that was the reason our dad left. Leon got mad when he heard me say it. He turned away from me and whispered, "She got intense after he left us."

If I'd known Leon would leave us for good, I would have paid him back the ten dollars I owed him for fronting me movie tickets and nachos last month. I still dream that he'll come back for the money. Ten dollars is a lot of money when you have nothing. Did he have anything? Was he warm and safe? Did he think about us?"

Me and Mama walking around like ghosts at Chalky's. Mama wanting to stay home and go looking for him but knowing she couldn't afford to lose her job. Me waking up in the middle of history class calling out his name. Was he thinking about us?

In the end Leon had to go because no one but me would believe him. And that was funny ‘cause Leon is the most honest person in the world. So honest . . .

Leon has honor and morality that Mama always used to be proud of until it brought the cops and social services to our trailer. Was Leon thinking about us?

He'd play the African drums on the top of Selby's drugstore, well, what used to be Selby's. Leon said he loved to watch everybody from above six stories above. He wanted to play the drums for everybody. He did.

Sweet, faraway drumming all over the town.

Leon would drum on top of Selby's in the morning and just as the sun was going down. He'd drum everybody in Springhill awake and asleep. Sweet, faraway drumming like he was calling to people he never met in a country he'd never been to.

Leon's drumming made me sad. 'Cause I knew. I knew what I didn't want to know. Leon was not one of us. Even the us everybody our age in Springhill would probably become whether we wanted to or not. He wouldn't work at the turkey farm or go to Star Lanes on Friday night. He wouldn't stand along the fence watching high school football and talking about how he could have been.

He'd never put on a pig roast and stand around a bonfire passing a paper bag full of whiskey, like a lot did years after they couldn't run fast anymore and the weather channel was more important to them than the world news.

I know if Leon had stayed in the county and went to football games, the boy who drummed for us would be gone forever. The boy who used to let me sit beside him and draw while he drummed would just vanish in the mist like people did in scary books. The boy who let me draw him drumming in blue as the sun set would disappear. And he did.

Mama cries all the time now, but I don't really think she's crying for Leon. I think she's crying for all the ones who have left her. Not for their sake, but her own.

Leon used to go to day camp with T-Boy James. They learned to swim together. But T-Boy had stuff happen to him. He changed from the kid who used to share his pudding with my brother. He turned nasty and danger-ous. His grandma cried when they dragged him away.

When T-Boy James got out of juvenile it didn't take him long to start messing with everybody that he thought put him there. That was a lot of people 'cause T-Boy did everything but kill before they finally locked him up.

Cougar got on the bus twice in two weeks with a bloody nose. Somebody had broken every window out of the science lab and keyed all the police cars parked by the courthouse. There was other stuff, but the night the block of apartments across from Selby's went up in flames was one of the worst nights of my life.

An old lady didn't make it out. And a couple of hours later men were looking under our trailer and knocking the door in and dragging Leon off.

Mama went and picked Leon up from the police station that night. Both her and the legal aid lawyer she brought with her looked overworked and nervous.

Leon came home sleepy and quiet. He hugged me hard just before he crawled into bed with all his clothes on. I didn't know it then, but I only had a week to be in the company of my brother.

I used to wonder what would happen to me when Leon went away. I used to think that I'd probably miss him so bad, it would hurt. But I thought away meant college or a job in another state, so he'd come back to me and my loneliness . . .

In the end it didn't matter that T-Boy heard Leon drumming on Selby's roof when he poured the first drops of gasoline or that he hid the gas can under our trailer. It doesn't even matter that everybody would have found out the truth about Leon in the end.

It's about pain. T-Boy's pain, Leon's pain, everybody's pain. The pains might never even have had to come together for my brother to leave this town. But he did. He did in broad daylight with a backpack and his drum under one arm. A man saw him get in a semi off Route 44. He said he was smiling when he got in.

I can't believe that though, 'cause I heard Leon on the roof way after that man says he got in the truck. I can still smell the smoke of the gutted building across the street as I climbed the steps to the roof. Sweet drumming. Sweet Leon playing . . . I even thought I heard him as I fell and visions of atomic blue drawings and pain shot through me.

I always count during the pain, now. Two thousand one, two thousand two ... Higher numbers it's coming-lower numbers it's going away.
```

---

## IC-1972: Barrington Bunny

- Title: Barrington Bunny
- Author (byline): Martin Bell
- Work: Way of the Wolf
- Publisher: Ballantine Books
- Publication date as stated: April 1983
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, BARRINGTON, SQUIRREL, BEAVER, WOLF, FIELD MOUSE
- Teaser before the introduction: Yes
- Spoken words (computed): 1462
- Already set (do not supply): none

### Source block (context only)

```text
Author: Martin Bell
Book: Way of the Wolf
ISBN: 978-0345305220
Publisher: Ballantine Books
Date (Month/Year): April 1983
```

### Introduction (context only: never use it for content warnings)

```text
Christmas is a time for telling stories. Some are ancient stories: stories about shepherds and angels and a baby born in a cow's manger. some of them are stories from our childhood - stories of elves and flying reindeer, of snowmen who come to life under the spell of Christmas magic, and of Santa Claus. Still each season brings new stories, stories that capture for us in a new way some of the miracles of the first story. So often the story of Jesus is portrayed as a kind of romantic, sentimental tale. It is forgotten how marvelous and how expensive a gift Christmas really is, that the manger and the cross are made of the same wood; that this small child was sent not just to be a gift, another trinket for us to wear around our necks for a season, but was sent to die for us, to show us what God's love is all about.

Martin Bell, in his story Barrington Bunny, reminds children everywhere of the power of love and sacrifice.
```

### Performance text (classify this)

```text
NARRATOR: (Pgs 1-8) Once upon a time in a large forest there lived a very furry bunny. He had one lop ear, a tiny black nose, and unusually shiny eyes. His name was Barrington. Barrington was not really a very handsome bunny. He was brown and speckled and his ears didn't stand up right. But he could hop, and he was, as I have said, very furry.

[Now] winter is fun for bunnies. After all, it gives them an opportunity to hop in the snow and then turn around to see where they have hopped. So, in a way, winter was fun for Barrington. But in another way winter made Barrington sad. For, you see, winter marked the time where all of the animal families got together in their cozy homes to celebrate Christmas. He could hop, and he was very furry. But as far as Barrington knew, he was the only bunny in the forest.

NARRATOR: When Christmas Eve finally came, Barrington did not feel like going home all by himself. So, he decided he would hop for a while in the clearing at the center of the forest. Hop. Hop. Hippity-hop. Barrington made tracks in the fresh snow. Hop. Hop. Hippity-hop. Then he cocked his head and looked back at the wonderful designs he had made.

BARRINGTON: Bunnies can hop. And they are very warm, too, because of how furry they are.

NARRATOR: But Barrington didn't really know whether or not this was true of all bunnies, since he had never met another bunny

When it got too dark to see the tracks he was making, Barrington made up his mind to go home. On his way, however, he passed a large oak tree. High in the branches there was a great deal of excited chattering going on. Barrington looked up. It was a squirrel family! What a marvelous time they seemed to be having.

BARRINGTON: Hello, up there!

SQUIRREL: Hello, down there!

BARRINGTON: Having a Christmas party?"

SQUIRREL: Oh, yes! It's Christmas Eve. Everybody is having a Christmas party!

BARRINGTON: (softly) May I come to your party?

SQUIRREL: Are you a squirrel?

BARRINGTON: No.

SQUIRREL: What are you, then?

BARRINGTON: A bunny.

SQUIRREL: A bunny? Well, how can you come to the party if you're a bunny? Bunnies can't climb trees.

BARRINGTON: (thoughtfully) That's true. But I can hop and I'm very furry and warm.

SQUIRREL: We're sorry. We don't know anything about hopping and being furry, but we do know that in order to come to our house you have to be able to climb trees.

BARRINGTON: Oh, well. Merry Christmas.

SQUIRREL: Merry Christmas.

NARRATOR: And the unfortunate bunny hopped off toward his tiny house. It was beginning to snow when Barrington reached the river. Near the riverbank was a wonderfully constructed house of sticks and mud. Inside there was singing. (sing, beaver-style)

BARRINGTON: It's the beavers! Maybe they will let me come to their party. (knocks on the door)

BEAVER: Who's out there?

BARRINGTON: Barrington Bunny

NARRATOR: There was a long pause and then a shiny beaver head broke the water.

BEAVER: Hello, Barrington.

BARRINGTON: May I come to your Christmas party?

BEAVER: (thinks for a moment) I suppose so. Do you know how to swim?

BARRINGTON: No, but I can hop and I am very furry and warm.

BEAVER: Sorry, I don't know anything about hopping and being furry, but I do know that in order to come to our house you have to be able to swim.

BARRINGTON: (eyes filling with tears) Oh, well, I suppose that's true. Merry Christmas.

BEAVER: Merry Christmas!

NARRATOR: And he disappeared beneath the surface of the water. Even as furry as he was, Barrington was starting to get cold. And the snow was falling so hard that his tiny, bunny eyes could scarcely see what was ahead of him. He was almost home, however, when he heard the excited squeaking of field mice beneath the ground.

BARRINGTON: It's a party! (blurting out through his tears) Hello, field mice. This is Barrington Bunny. May I come to your party?

NARRATOR: But the wind was howling so loudly and Barrington was sobbing so much that no one heard him. And when there was no response at all, Barrington just sat down in the snow and began to cry with all his might.

BARRINGTON: (sobbing) Bunnies aren't any good to anyone. What good is it to be furry and to be able to hop if you don't have any family on Christmas Eve?

NARRATOR: Barrington cried and cried. When he stopped crying he began to bite on his bunny's foot, but he did not move from where he was sitting in the snow. Suddenly, Barrington was aware he was not alone. He looked up and strained his shiny eyes to see who was there. To his surprise he saw a great silver wolf. The wolf was large and strong and his eyes flashed fire. He was the most beautiful animal Barrington had ever seen.

For a long time the silver wolf didn't say anything at all. He just stood there and looked at Barrington with those terrible eyes. Then slowly and deliberately the wolf spoke.

WOLF: (in a gentle voice) Barrington, why are you sitting in the snow?

BARRINGTON: Because it's Christmas Eve, and I don't have any family, and bunnies aren't any good to anyone.

WOLF: Bunnies are, too, good. Bunnies can hop and they are very warm.

BARRINGTON: (sniffing) What good is that?

WOLF: It is very good indeed because it is a gift that bunnies are given, a free gift with no strings attached. And every gift that is given to anyone is given for a reason. Someday you will see why it is good to hop and to be warm and furry.

BARRINGTON: (moaning) But it's Christmas and I'm all alone. I don't have any family at all.

WOLF: Of course you do. All of the animals in the forest are your family.

NARRATOR: And then the wolf disappeared. He simply wasn't there. Barrington had only blinked his eyes, and when he looked-the wolf was gone.

BARRINGTON: (thoughtfully) All of the animals in the forest are my family. It's good to be a bunny. Bunnies can hop. That's a gift. A gift. A free gift.

NARRATOR: On in the night Barrington worked. First he found the best stick he could. (And that was difficult because of the snow.) Then Hop. Hop. Hippity-hop. To Beaver's house. He left the stick just outside the door. With a note on it that read: "Here is a good stick for your house. It is a gift. A free gift. No strings attached. Signed, a member of your family."

BARRINGTON: It is a good thing that I can hop because the snow is very deep.

NARRATOR: Then Barrington dug and dug. Soon he had gathered together enough dead leaves and grass to make the squirrels' nest warmer. Hop. Hop. Hippity-hop. He laid the grass and leaves just under the large oak tree and attached this message: "A gift. A free gift. From a member of your family."

It was late when Barrington finally started home. And what made things worse was that he knew a blizzard was beginning. Hop. Hop. Hippity-hop. Soon poor Barrington was lost. The wind howled furiously.

BARRINGTON: It certainly is cold. It's a good thing I'm so furry. But if I don't find my way home pretty soon I might freeze!

FIELD MOUSE: Squeak. Squeak. . .

NARRATOR: And then he saw it -- a baby field mouse lost in the snow. And the little mouse was crying.

BARRINGTON: Hello, little mouse. Don't cry. I'll be right there."

NARRATOR: Hippity-hop, and Barrington was beside the tiny mouse.

FIELD MOUSE: (sobbing) I'm lost! I'll never find my way home, and I know I'm going to freeze.

BARRINGTON: You won't freeze. I'm a bunny and bunnies are very furry and warm. You stay right where you are and I'll cover you up.

NARRATOR: Barrington lay on top of the little mouse and hugged him tight. The tiny fellow felt himself surrounded by warm fur. He cried for a while but soon, snug and warm, he fell asleep.

Barrington had only two thoughts that long, cold night.

BARRINGTON: It's good to be a bunny. Bunnies are very furry and warm.

NARRATOR: And then, when he felt the heart of the tiny mouse beating regularly . . .

BARRINGTON: All the animals in the forest are my family.

NARRATOR: Next morning, the field mice found their little boy, asleep in the snow, warm and snug beneath the furry carcass of a dead bunny. Their relief and excitement was so great that they didn't even think to question where the bunny had come from. And as for the beavers and the squirrels, they still wonder which member of their family left the little gift for them that Christmas Eve.

After the field mice had left, Barrington's frozen body simply lay in the snow. There was no sound except that of the howling wind. And no one anywhere in the forest noticed the great silver wolf who came to stand beside that brown, lop-eared carcass. But the wolf did come. And he stood there. Without moving or saying a word. All Christmas Day. Until it was night. And then he disappeared into the forest.
```

---

## IC-1973: Bartholomew and the Oobleck

- Title: Bartholomew and the Oobleck
- Author (byline): Theo Geisel (aka Dr. Seuss)
- Work: Not specified
- Publisher: Random House
- Publication date as stated: Oct 1949
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, KING, BARTHOLOMEW, MAGICIANS, BELL RINGER, TRUMPETER, CAPTAIN
- Teaser before the introduction: Yes
- Spoken words (computed): 1331
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theo Geisel (aka Dr. Seuss)
ISBN: 978-0394800752
Publisher: Random House
Date (Month/Year): Oct 1949
```

### Introduction (context only: never use it for content warnings)

```text
In an age when power is often mistaken for entitlement, this story feels less like a children’s fable and more like a warning etched in green slime. King Derwin’s insistence that even the sky should bend to his will echoes a dangerous change in modern governance -- where leaders test the limits of institutions, sidestep norms, and treat politics as something to command rather than uphold. When a leader begins to see themselves not as a servant of their people but as an all-powerful, untouchable authority, our way of life is doomed. Can the kingdom be saved? Only if ordinary people, institutions, and officials speak plainly and insist, without fear, that no one, however powerful, rules the sky.

Bartholomew and the Oobleck by Theo Geisel (aka Dr. Seuss)
```

### Performance text (classify this)

```text
NARRATOR: They still talk about it in the Kingdom of Didd as The-Year-the-King-got-Angry-with-the-Sky. If it hadn’t been for Bartholomew Cubbins, that King and that Sky would have wrecked that little Kingdom.

KING: (staring up into the sky, muttering and sputtering) Humph! The things that come down from my sky!

NARRATOR: All spring when the rain came down, he growled at that . . . All summer when the sunshine came down, he growled at that. . . All Autumn when the fog came down, he growled at that . . . And that winter when the snow came down, he started shouting!

KING: This snow! This Fog! This Sunshine! This rain! BAHH!

BARTHOLOMEW: (trying to calm him) But, King Derwin, you’ve always had these same four things.

KING: (bellowing) That’s just the trouble! Every year the same four things! I want something NEW to come down!”

BARTHOLOMEW: Something new? That’s impossible, Your Majesty.

KING: Boy, don’t you dare tell me what I can or cannot have! I am King!

BARTHOLOMEW: I know, Sire, you rule all the land. And you rule all the people. But even kings can’t rule the sky.

KING: (flying into a terrible rage) Well, maybe other kings can’t do it, but maybe I’m one king who can! (begins laughing) They can do it for me! Bartholomew Cubbins, call my royal magicians!

BARTHOLOMEW: (shivering) Oh, no, Your Majesty! Don’t call them!

KING: Hold your tongue, Bartholomew Cubbins! You do as I command you.

BARTHOLOMEW: (bowing) Yes, Sire. But, Your Majesty, you may be very sorry.

NARRATOR: He took the King’s secret whistle from its hook. He blew a long, low blast down the King’s stairway. And a moment later he heard them coming!

MAGICIANS: (shuffling and chanting)
Shuffle, duffle, muzzle, muff.
Fista, wista, mista-cuff.
We are men of groans and howls,
Mystic men who eat boiled owls.
Tell us what you wish, oh King.
Our magic can do anything.

KING: I wish to have you make something fall from my skies that no other kingdom has ever had before. What can you do? What will you make?

MAGICIANS: (thinking, blinking) . . . Oobleck.

Won’t look like rain. Won’t look like snow.
Won’t look like fog. That’s all we know.
We just can’t tell you any more.
We’ve never made Oobleck before.

BARTHOLOMEW: (whispering) They’ll do something crazy, Your Majesty! Stop them!

KING: (chuckling) Stop them? Not for a ton of diamonds! Why, I’ll be the mightiest man that ever lived! Tomorrow I’m going to have OOBLECK!

NARRATOR: On the Mystic Mountain Neeka-tave the magicians were working their terrible magic. All night they walked circles round their magic fire . . .

MAGICIANS: (chanting)
Oh, snow and rain are not enough!
Oh, we must make some brand-new stuff!
Burn yellow twigs and burn red rust
And burn a stocking full of dust.
Make magic smoke, green, thick and hot!

(It sure smells dreadful, does it not?)
Go, magic smoke! Go high! Go high!
Go rise into the kingdom’s sky!
Go make the wondrous Oobleck fall!
Oh, bring down Oobleck on us all!

NARRATOR: Dawn was breaking and Bartholomew was still watching at the bedchamber window. There was something strange in the sky! At first it seemed like a little greenish cloud . . . just a wisp of greenish steam. Tiny little greenish specks were shimmering in the air right over his head.

BARTHOLOMEW: (stretching out his hand to catch a speck, the pulls his hand back, frightened. Slams the window shut, shouting) Wake up, Your majesty! Your oobleck! It’s falling!

KING: (springs from his bed) By my royal whiskers, it is! Oh, that beautiful oobleck! And it’s mine! All mine!

BARTHOLOMEW: I don’t like the looks of those blobs, Sire. They’re coming down now as big as greenish peanuts.

KING: (laughing) The bigger the better! Oh, what a day! I’m going to make it a holiday! I want everyone in my kingdom to go out and dance in my glorious oobleck!

BARTHOLOMEW: Do you really think it’s safe, Sire?

KING: (snapping) Stop asking foolish questions! Wake my royal bell ringer. Tell him to ring the great holiday bell! Run!

NARRATOR: Across the sleeping palace, Bartholomew ran. Then up the ladder of the high bell tower.

BARTHOLOMEW: Ring your bell! His majesty proclaims today a holiday!

BELL RINGER: (grabbing the bell rope and yanking – Nothing happens. He yanks harder – still nothing) Heh . . .? What’s wrong with my bell? I’d better take a look outside. (pokes his head out through the little trap door) Merciful gracious! What is THAT? All over my bell like greenish molasses!

BARTHOLOMEW: Not only your bell! Look at that poor robin down there in that tree! She’s stuck to her nest! That oobleck’s like glue!

BELL RINGER: (wringing his hands) Oooh! If that green stuff sticks up robins, it’ll stick up people, too!”

BARTHOLOMEW: Someone’s got to warn the people! Warn ‘em to stay inside their houses! I’ll tell the royal trumpeter! (races off)

NARRATOR: But all the royal trumpeter blew was . . .

TRUMPETER: (blowing on his trumpet: GLUGG!) My horn! One of those green things flew inside it! (tries to blow it out; tries to shake it out, but no success) I’ll pull it out!

BARTHOLOMEW: No! Don’t you touch it!

NARRATOR: [But] The trumpeter’s hand was already in it.

TRUMPETER: (grabs hold of the lump of oobleck; pulls with all his might. The oobleck stretches then snaps back inside the trumpet, yanking his arm back with it) I can’t wiggle a finger! Oh, Bartholomew, what’ll I do?

BARTHOLOMEW: I hate to leave you stuck to your horn. But if you can’t warn the people of the kingdom, I’ve got to find someone who can! (races out)

NARRATOR: Down the stairs raced Bartholomew Cubbins . . . down to the chamber of the Captain of the Guards.

CAPTAIN: (humming in front of his mirror, combing the ends of his moustache)

BARTHOLOMEW: Captain! DO something! Haven’t you seen the dreadful Oobleck?”

CAPTAIN: (nonchalantly laughing) Oh, that stuff. What so dreadful about that? I think it’s rather pretty. That stuff’s harmless. I’ll show you. I’ll eat some. (leans out the window, scooping up some oobleck)

BARTHOLOMEW: Don’t, Captain! DON’T!

NARRATOR: The Captain did! By the time Bartholomew dragged him back inside the room . . .

CAPTAIN: (mouth glued shut with oobleck. Tries to speak, but no words come out)

BARTHOLOMEW: Forgive me for leaving you, Captain . . . (races out) I’ll get the King’s horse! I’ll ride through the country! I’ll warn the people of the kingdom myself!

NARRATOR: He pushed open the door that led to the Royal Stables. The awful oobleck was plumping down as big as greenish footballs now! Too late to warn the people of the kingdom! There were farmers in the fields, getting stuck to hoes and plows. Goats were getting stuck to ducks. Geese were getting stuck to cows. It was piling up, great greenish tons of Oobleck, deeper and deeper on every roof in the land. There was nothing Bartholomew Cubbins could do out there.

BARTHOLOMEW: (shaking his head sadly, he steps back inside)

NARRATOR: But inside, a moment later, it was just as bad as out! With an angry roar, the Oobleck was suddenly hitting the palace harder! The whole palace was springing leaks. It was dripping through the ceilings. It was coming in everywhere . . . even through the keyholes!

BARTHOLOMEW: (gasping) The King!

NARRATOR: Where was the King? He’d forgotten all about him! Bartholomew found him in the throne room. There he sat . . . Old King Derwin, proud and might ruler of the Kingdom of Did, helpless as a baby. His royal crown was stuck to his head. The seat of his royal pants were stuck to his throne. Oobleck was dripping from his royal eyebrows.

KING: Fetch my magicians, Bartholomew! Make them say some magic words to stop the oobleck falling!

BARTHOLOMEW: (shrugging his shoulders) I can’t, Your Majesty. Their cave on Mountain Neeka-tave is buried deep in oobleck.

KING: (groaning) Then I must think of some magic words! Oh, what are those words my magicians say . . . ? Shuffle. . . duffle . . . muzzle . . . muff . . . That’s all I can remember and they don’t do any good! The oobleck keeps on falling harder!”

BARTHOLOMEW: (angry) And it’s going to keep falling until your great palace tumbles down! Don’t waste your time saying foolish magic words. YOU ought to be saying some plain simple words! This is all your fault! Now the least you can do is say, “I’m sorry.”

KING: (belligerent -- no one had ever talked to him like this before) What! ME . . . ME say I’m sorry! Kings never say I’m sorry! And I am the mightiest king in all the world!

BARTHOLOMEW: (not backing down) You may be a mighty king. but you’re sitting in Oobleck up to your chin. And so is everyone else in your land. If you won’t even say you’re sorry, you’re no sort of a king at all! (turns his back to leave)

KING: (great, deep sob, he begins crying) Come back, Bartholomew Cubbins. You’re right! It is all my fault! And I am sorry!

NARRATOR: And the moment the King spoke those words, something happened. . . Maybe there was something magic in those simple words, “I’m sorry.” Maybe there was something magic in those simple words, “It’s all my fault.” Maybe there was, and maybe there wasn’t. But they say that as soon as the old King spoke them, the sun began to shine. They say that all the oobleck just simply, quietly melted away. Then the King proclaimed a new national holiday . . . in honor of the four perfect things that come down from the sky: The rain, the sunshine, the fog and the snow.
```

---

## IC-1974: Beauty and the Beast

- Title: Beauty and the Beast
- Author (byline): AJ Jacobs
- Work: Fractured Fairy Tales, Pgs 103-110
- Publisher: Bantam Books
- Publication date as stated: Jan 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, ROCKY, BULLWINKLE, OLD MAN, DAUGHTER, PRINCE
- Teaser before the introduction: Yes
- Spoken words (computed): 1258
- Already set (do not supply): none

### Source block (context only)

```text
Author: AJ Jacobs
Book: Fractured Fairy Tales, Pgs 103-110
ISBN: 978-0553373738
Publisher: Bantam Books
Date (Month/Year): Jan 1999
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
NARRATOR: (Pg 103-110) Once upon a time there was a magnificent golden castle on a silver cloud high up in the sky, which has nothing to do with anything because our story is about an old woodchopper who lived in a shack, but that's a good way to start a fairy tale.

Long before Politically Correct Bedtime Stories arrived in bookstores, Americans were getting their giggles from Fractured Fairy Tales, those delightfully twisted parables brought to us between the cliffhanger adventures of our favorite cartoon heroes, Rocky & Bullwinkle.

ROCKY: *And now...

BULLWINKLE: Hey Rocky! Watch me pull a rabbit out of my hat!

ROCKY: But that trick never works!

BULLWINKLE: This time for sure! Presto! (something goes terribly wrong—be creative) Well, I'm getting close.

ROCKY: And now it's time for another special feature! A nostalgic retro adventure re-imagined by AJ Jacobs in his collection of Fractured Fairy Tales. -- Beauty and the Beast

NARRATOR: The old man was very happy, but he had a daughter who was very unhappy because . . . well, she was rather plain. Actually, she was really plain. In fact, she had a face like five miles of bad road. Anyway, it was time for her to marry, but because she was so fat and ugly, none of the young men of the kingdom ever came to ask for her hand, or any other part of her body, for that matter. Then one day, the old man decided to cheer her up.

OLD MAN: Child, it is your birthday and I've brought you something to keep you from being so lonely.

DAUGHTER: (wide-eyed) A man?

OLD MAN: Nope. A mule.

NARRATOR: He pointed to a brown, furry, four-legged, grunting beast. Well, a mule wasn't exactly the kind of companion she had in mind, but at least it was somebody to talk to.

DAUGHTER: Hi there, silly beast, I wonder if you were once a handsome prince changed into a mule by a wicked witch. If so, I could break the spell with a kiss. (kisses mule)

NARRATOR: She smacked the mule right on its lips. It was no use. The mule was a mule and had always been a mule.

The next day the old man instructed his daughter to take a bundle of sticks to the village.

DAUGHTER: A bundle of sticks? What for?

OLD MAN: How should I know. But somebody is always carrying a bundle of sticks around in fairy tales. You know that.

NARRATOR: So, the young girl took the bundle of sticks and decided to ride her trusty mule into the village. But something very strange happened. Unknown to her, the moment she climbed onto the mule's back *POOF* she turned into a beautiful maiden. You know the type: blond hair, blue eyes, a figure like she spends her days doing Jazzercise.

Anyway, when she reached the village, (insert whistles and catcalls) she could hardly believe her eyes, for all the young men, instead of laughing and throwing mud at her, bowed, tipped their hats, and made catcalls. She was still trying to figure it out when a handsome young prince rode up to her on a snow-white horse.

PRINCE: Ah, fair ladyl You are truly the most lovely beauty in the land.

DAUGHTER: (batting her eyes) Why, my young prince, are you nuts or sumpthin'?

PRINCE: With your permission, I should like to call upon you tonight. How about when the clock strikes the hour of eightish?

NARRATOR: Flushed with excitement, the girl raced home; but when she arrived and stepped off her mule, *POOF* she immediately returned to her fat little ugly self. That night, promptly at eightish o'clock, the prince, sitting astride his white charger, knocked on the door.

PRINCE: (prepares himself and knocks regally)

DAUGHTER: (opens door and smiles)

NARRATOR: A crooked-toothed smile -- one that made chopped yak liver seem appealing –

DAUGHTER: Hellooooo!

PRINCE: (with a hard to conceal facial reaction) Um . . .

NARRATOR: Said the prince, who at that moment was desiring a bit of Pepto-Bismol, or the medieval equiv-alent.

PRINCE: Is your sister at home?

DAUGHTER: I don't have a sister.

PRINCE: Your aunt then.

DAUGHTER: I don't have an aunt.

PRINCE: (growing more frantic) Your cousin? Your best friend? Your babysitter?

DAUGHTER: What are you talking about? I live here alone with my father.

PRINCE: (makes a break for it)

NARRATOR: Figuring he had found the wrong house, the prince galloped quickly off on his white steed. The poor girl was left standing at the door, brokenhearted and trying to understand what had gone wrong.

The following day, her father again asked her to go into the village. This time to pick up a bundle of sticks.

OLD MAN: (patting her kindly on her head) It'll take your mind off your ugliness.

NARRATOR: No sooner had the girl climbed on the mule's back than *POOF* once again she changed into a beautiful maiden.

On the way to the village, she chanced to pass a clear, still pool of water. Looking into it, she saw her reflection and was shocked to see she was now very beautiful. She jumped off her mule for a close look and *POOF* instantly she changed back into her former ugly self. And then, she suddenly realized what had happened.

DAUGHTER: I get it now!

NARRATOR: She said out loud to no one in particular, as people in fairy tales sometimes do.

DAUGHTER: This is a magic mule. As long as I sit on this beast, I'm a beauty!

NARRATOR: The girl jumped back onto the mule, and *POOF* beautiful again. And the beauty and the beast dashed to find the prince. When he saw her coming, he rode up to her on his gallant steed.

PRINCE: Ah, lovely beauty, I have found you again. Please say you will be mine so that we may be married.

DAUGHTER: Yes, but on one condition: That I remain on my mule at all times.

NARRATOR: Of course, this seemed like a strange request, but the prince agreed.

PRINCE: So be it, my love. And so that we start off on the right foot -- or on the right hoof -- I shall stay on my horse as long as you stay on your mule.

NARRATOR: And thus they were married by a priest, who delivered the sermon on a donkey. As the years went by, the young girl was very happy, although the poor mule did get a bit of a backache. And true to his word, the prince also stayed on his horse. And as any good husband would, he took her dancing every Saturday night at the palace, where they were the most striking couple on the dance floor. Or actually, the most striking quadruple on the dance floor.

One day, as the girl rode in the garden *WOOSH* the wind blew off her bonnet. Not stopping to think, she hopped off her mule to get the hat and *POOF* she immediately turned into an ugly, disgusting hag again.

DAUGHTER: (adjusting her hat she transfroms from beauty to hag)

NARRATOR: Realizing her mistake, she scrambled to get back in the saddle again. But it was too late, for just then the prince rode up.

PRINCE: Pardon me, old hag. Have you seen my wife? Wait a minute, this is her mule!

DAUGHTER: (blushing and gulping) Yes. And I am your wife.

NARRATOR: She began to sadly confess the whole story to her husband, but instead of being angry . . .

PRINCE: (laughing and clapping for joy) Ha, ha, ha, ha. Yahoo! Yippee!

DAUGHTER: I don't get it. Are you happy to find out that I'm really ugly?

PRINCE: No! I'm happy to know that I can finally get off this blasted horse. You see, I'm only a handsome prince when I stay on him.

NARRATOR: And with that, the prince hopped off his horse and *POOF* he changed into one of the ugliest men ever to walk the earth. He was fat and short and bald and full of warts. His face looked like ten miles of bad road.

DAUGHTER: (gleefully) Ugh! You're uglier than me!

PRINCE: (they hug) We were meant for each other! Just think-no more saddle sores!

NARRATOR: And so, the ugly man and the ugly girl were able to live happily ever after.
```

---

## IC-1975: The Believing Child

- Title: The Believing Child
- Author (byline): Zenna Henderson
- Work: Holding Wonder
- Publisher: Avon Books
- Publication date as stated: Jan 1971
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: TEACHER, DISMEY, DONNA, TREESA, BANNIE, HANNERY
- Teaser before the introduction: Yes
- Spoken words (computed): 1490
- Already set (do not supply): none

### Source block (context only)

```text
Author: Zenna Henderson
Book: Holding Wonder
ISBN: 978-0380440818
Publisher: Avon Books
Date (Month/Year): Jan 1971
```

### Introduction (context only: never use it for content warnings)

```text
Jiminy Cricket, side-kick and fictional embodiment of Pinocchio’s conscious tells us, “Anything is possible if you just believe.” In this story, a child takes this quote to a new extreme.

Dismey is a lonely, tormented first grade child of migrant workers, but her teacher discovers she is a believing child— someone who so strongly believes what she is told, that it becomes true.

But what happens when she realizes that she possesses the power of magic, without understanding the consequences? The Believing Child by Zenna Henderson
```

### Performance text (classify this)

```text
(to audience) No one seeing me sitting here could possibly know that a terrible problem is gnawing at me. In fact, I can’t believe it myself. It couldn’t possibly be. And yet I’ve got to solve it. I have LOTS of time—I have until 2:15. What will I do if 2:15 comes and I haven’t got through to Dismey?

(to audience) I welcomed [Dismey] to my first grade classroom. I was used to frightened withdrawn children, terrified by coming into a new school, but nothing [was] quite so drastic as Dismey. No talking, no laughing, no smiles, or even tears. [But she] came slowly to life in the classroom: drawing, painting, number work, reading . . . But all the rest of the classroom activities paled to insignificance as far as Dismey was concerned to the wonder of story time. Dismey believed without reservation in the absolute truth of every story she heard. This [made] her completely vulnerable to Bannie and Michael. One day I found her crying out by the sidewalk. Tears were falling without a sound as she rubbed with trembling desperation at the sidewalk.

TEACHER: What’s the matter Dismey? What are you doing?

DISMEY: (crying) My mamma. I hurt my mama! I stepped on a crack. I didn’t mean to but Bannie pushed me. And now my mama’s back is busted.

TEACHER: Oh, Dismey, honey! ‘Step on a crack and break your mother’s back’ isn’t for true! It’s just a singing thing the children like to say. It isn’t really so. (to audience) We finished the first of the Oz books and were racing delightedly into “The Magic of Oz,” and there it was! Right on page 19! We all looked at it solemnly. We wrote it on the board. We contemplated it with awe. A real live magic word! All we had to do now was to learn how to pronounce [it]. Therein lay the difficulty. We considered the word—PYRZQXGL. We knew all the letters in it, but there were no vowels except “and sometimes Y”. How could you sound out a word with no vowels and no place to divide it into syllables?

TEACHER: We’ll have to be careful even trying to say it, though. Because if you do find the right way to pronounce it, you can—well, here it tells you— ‘. . . transform anyone into a beast, bird or fish, or anything else, and back again, once you knew how to pronounce the mystical word’ . . . You could even change yourself. Wouldn’t it be fun to be a bird for a while? But . . . birds can talk in the Land of Oz . . . can they talk here? (to audience) The solemn consensus was no, except for parakeets and mynah birds.

TEACHER: So, if you changed yourself into a bird, you couldn’t ever change yourself back. So, you better be careful if you learn the way to say it.

DONNA: How DO you say it, Teacher?

TEACHER: I’ve never found out. I’ll have to spell it every time. Maybe someday I’ll learn it, then when it’s Quiet Time, I’ll turn you all into Easter Eggs, and we’ll have a really quiet Quiet Time! (to audience) [I watched as] Dismey bent over a piece of paper, carefully copying [the word] from the board, her mouth moving to the letters. [Later], the clamor and noise finally settled down to the happy hum of Quiet Time, and I sighed and relaxed, taking a quick census of the room. I straightened and checked again.

TEACHER: Where’s Dismey? Does anyone know where Dismey is?

DONNA: She went to the restroom with me . . . She’s afraid to go alone. She thinks a dragon lives down in the furnace room and she’s scared to go by the steps by herself.

TREESA: Maybe she go’d to beeg playgroun’. We don’
s’pose to go to beeg playgroun’.”
(to audience) Then I heard Bannie’s high
embarrassed giggle

TEACHER: Bannie and Michael, come here. Where is Dismey?

BANNIE: We didn’t do nothing. We just put a rock on her shadow! We told her she couldn’t move. (to audience) The playground was empty, [then] I turned the corner of the Old Building, and there she was, straining and struggling, her whole self pulling desperately away from the small rock that lay on her shadow. I saw—or thought I saw - the shadow itself curl up around her knobby, chapped ankles.

TEACHER: Dismey! DISMEY!

DISMEY: Teacher! Oh, teacher . . . (to audience) I had my arms around her, trying to warm her stiff little hands.

TEACHER: But, Dismey, honey, it isn’t so! You could have come back to the room anytime! A rock can’t hold your shadow! It isn’t true!

(to audience) But, I had to move that rock before I could pick her up and carry her back into the room. I believed that I had felt the tug of a tethered shadow. I was out of my depth – completely. Children bounce back amazingly. The next day— that’s today! – started normally enough. Michael and Bannie had the devilish light flickering in their eyes again. Dismey had a small smile that turned up the corners of her mouth a little. Afternoon recess came and went. The tide of children flowed across the floor for story time.

TEACHER: Bannie and Michael, I don’t. . .

(to audience) Then I felt a huge sinking inside of me. My eyes flew to Dismey. She returned my look, the smile still bending her mouth.

TEACHER: Where’s Bannie and Michael?

HANNERY: They tol’ me they wuz go to beeg playgroun’. They alla time sneak up there.

DONNA: Maybe they didn’t hear the bell . . . when you play by the Old Building, sometimes you don’t. (to audience) I looked at Dismey. She looked back. Her small, pointed tongue circled the smile and then disappeared. I looked away, uncomfortable. After the group went back to their seats and became immersed in their work, I called Dismey quietly up to my desk.

TEACHER: Where are Michael and Bannie?

DISMEY: Out on the playground . . .

TEACHER: Why didn’t they come when the bell rang?

DISMEY: (with a little smile) They couldn’t hear the bell ring.

TEACHER: Dismey, why couldn’t they hear the bell?

DISMEY: ‘Cause I changed them . . . I changed them into rocks.

TEACHER: Changed them? Into rocks?

DISMEY: Yes . . . they’re mean. They’re awfully mean. I changed them. (smiling again)

TEACHER: How did you do it? What did you do?

DISMEY: I learned the magic word. I can say it right. You know, the one you read to us. That PYRZQXGL. (to audience) Her voice fluttered and hissed through a sound that raised the hairs on the back of my neck.

TEACHER: And . . . it . . . WORKED!

DISMEY: Why, sure . . . you said it would. It’s a magic word. Mama told me how to say it. She said how come they put words like that in a kids’ book. That’s not a word for kids. But she told me how to say it anyway. See? (to audience) She picked up the stapler from my desk.

DISMEY: Be a baby rabbit — PYRZQXGL! (to audience) And there was a tiny gray bunny nosing inquisitively at my blotter!

DISMEY: Be what you was before . . . PYRZQXGL! (to audience)The bunny started slightly, and the stapler fell over on its side. I picked it up. It felt warm. I dropped it.

TEACHER: But—but . . . where are the boys, Dismey? Do you know?

DISMEY: I guess so. (frowning) I guess I remember

TEACHER: Go get them. Bring them to me. (to audience) She looked at me quietly for a moment, her jaw muscles tensing, then she said, “Okay, teacher.” So I sent her, heaven help me! A she came back and put three little rocks on the corner of my desk.

DISMEY: I guess these is them . . . Two of them are, anyway. I couldn’t remember exactly which ones they was, so I brought an extra one. (to audience) We looked at the rocks.

DISMEY: They’re scared. I turned them into scared rocks.

TEACHER: Do rocks know? Can rocks be scared?

DISMEY: I don’t know . . . but if they can - they are. (to audience) And there they lie—three rocks, roughly the size of marbles - and two of them are Michael and Bannie. And time is running out fast! I can’t say the magic word. Nobody can say the magic word except Dismey. I see only one possible course of action. I’m going to take a page from Dismey’s own book—I’m going to be the believingest teacher there ever was. I believe. I believe that Dismey will mind me – she’ll do as she is told. I believe, I believe, I believe . . .

TEACHER: Dismey, come here, please . . . It’s almost time to go home. Here, take the rocks and go outside by the door. Turn them back into Michael and Bannie again.

DISMEY: I don’t want to. (to audience) It’s NOT refusal! It’s not refusal . . . it’s just a statement . . .

TEACHER: I know you don’t. But the bell will be ringing soon and we don’t want to make them miss the bus.

DISMEY: (angry) But they were awfully mean.

TEACHER: Yes, I know they were, but they’ve been rocks a long time—scared rocks. They know now that you can be mean back at them, so they’ll probably let you alone and not bother you anymore. Go on, take them outside. (to audience) The three rocks click together in her hand. She is going out the door. Now, I am waiting for the doorknob to turn again. I believe, I believe, I believe . . .
```

---

## IC-1976: Beyond Magenta: Transgender Teens Speak Out

- Title: Beyond Magenta: Transgender Teens Speak Out
- Author (byline): Susan Kuklin, Editor
- Work: Not specified
- Publisher: Candlewick
- Publication date as stated: March 2015
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: GIRL 1, GIRL 2, CHRISTINA, SCHOOL COUNSELOR, BEST FRIEND, NARRATOR, MOM, LOUDSPEAKER, PRINCIPAL, THE DEAN, DEAN, BOYS, CHRISTINA’S MOM
- Teaser before the introduction: Yes
- Spoken words (computed): 1151
- Already set (do not supply): none

### Source block (context only)

```text
Author: Susan Kuklin, Editor
ISBN: 978-0763673680
Publisher: Candlewick
Date (Month/Year): March 2015
```

### Introduction (context only: never use it for content warnings)

```text
The Human Rights Foundation has estimated that there are more than 2 million transgendered individuals in the US. We are parents, siblings, and children. We are your coworkers, your neighbors, and your friends -- A diverse community, representing all racial and ethnic backgrounds, as well as all faith traditions.

In 2021, President Biden declared March 31 as the Transgender Day of Visibility. A day to publicly recognize the resilience, strength and joy of not only transgender, but also nonbinary and gender nonconforming people. And it was a step . . .

But we still face severe discrimination, stigma and systemic inequality. In fact, according to The Human Rights Campaign, 2022 is on pace with more state legislation targeting transgender youth than any prior year.

Today, I want to give voice to a beautiful woman, Christina.

This is her story and these are her words as found in Beyond Magenta edited by Susan Kuklin
```

### Performance text (classify this)

```text
NOTE: Speaker is a transgender woman

GIRL 1: (Pg 31-32) (laughing and gesturing) I don’t know what that is.

GIRL 2: Yeah, what is that?

CHRISTINA: Are those girls talking about me? (Christina stares at them)

GIRL 1: Can I help you with something?

CHRISTINA: Yeah, can you stop laughing at me?

GIRL 1: This is a free country; I can laugh at whoever I want. And how do you know I’m laughing at-chu?

CHRISTINA: Because I’m not stupid. I heard you say, “I don’t know what that is.”

GIRL 1: I know you’re a man with that big face.

CHRISTINA: (Pg 33) (to audience) I was trying not to cry, but it was really hurtful because . . . (holding back tears) People can be so nasty, so rude. I didn’t do anything to her. (beat) I’ve been called a man before. That makes me feel less a woman. I start questioning: Do I really pass in society? I don’t want to get emotional. I really, really hate being transgender. It’s a constant struggle. While everyone else my age is saving up for a car, I’m saving up to look possible. (Pg 34) When I go out, I can’t make any mistakes. My hair has to be exactly right. My makeup, my outfit, even my smell must be feminine. (beat) There were days when I would not go to school. My appearance stopped me. I just turned back.

CHRISTINA: (Pg 34) When I was born, I was named Matthew. When I was little, I wanted to be a girl, but I didn’t have a full understanding about it. I knew I was a boy because my mom and my dad told me I was one. (Pg 35) The teasing began in elementary school. They called me a sissy and a faggot. There was this girl in fifth grade. All the boys were crazy about her. She was the it girl. My ideal. I wanted to look like her. I wanted the attention from boys. Her name was Christina. At the time I thought that if I was a girl, my name would be Christina. My mom hates that name.

(Pg 36-37) My mother comes from a Catholic family who always went to church. I really was close to my family, but not anymore. They are just so narrow-minded. Every time I go to my grandmother’s house, they want to pray for me. I really don’t need to be prayed for.

My oldest brother had gone to an all-boys Catholic high school, where he became disciplined and focused. So off I went to Mount Saint Michael Academy, a Catholic high school for boys. I was so nervous. I asked my brother, “How do I act like a man?” He told me I had to walk a certain way, with a little lean, like a gangsta boy. I practiced . . . He taught me how to sit with my legs open. It was the most uncomfortable feeling in the world for me. It looked gross. He told me I had to deepen my voice and talk like a man.

(to other students) Oh, hey, what’s up? My name is Matthew. (to audience) It came off so phony; it just wasn’t me. At all! No one accepted me as a straight boy. Within a week, people started talking. “I think he’s gay.”

(Pg 39-40) I wasn’t really interested in learning. If there was a test, I’d study, but I wasn’t interested in English or history. I was interested in art and fashion. I drew girls a lot. To this day, I draw girls. One of the school counselors said.

SCHOOL COUNSELOR: I want to see your sketchbook . . . your art.

CHRISTINA: I showed her pictures of girl after girl after girl.

SCHOOL COUNSELOR: You know, when people draw, it’s a way of escaping. People draw what they want to be.

CHRISTINA: The moment she said that. I started thinking, Well, yeah, I want to be a girl, but it will never happen. (to counselor) I’d worry about passing. I don’t want people wondering what I am. I don’t want to get hurt. (to audience) But always in the back of my mind, I wished I was a girl. (Pg 41) One day, (Pg 43) I told my best friend that I wanted to become a girl . . .

BEST FRIEND: Don’t do that! God made you a boy for a reason. For a purpose. Why can’t you just be a gay man?

CHRISTINA: Before I educated myself about what being transgender really is, I thought that I must be a gay person. [But] the Google site said, “Sexual orientation has nothing to do with gender identity. There are gay and straight transgenders.” I thought I was gay because I was attracted to men. (beat) Straight men, not gay men.

NARRATOR: (Pg 42) [Finally], the summer before her senior year, Christina stopped worrying about what her mother would think . . .

CHRISTINA: (Pg 45) My senior year was my best and worst year in high school. (Pg 44) My hair grew long pretty fast. I dyed it red and got bangs. (Pg 45) The day before school started, I got my nails done. Pink. My mom completely freaked out.

MOM: You’re going to get in trouble. You’re going to get hurt. Somebody’s going to hurt you, baby.”

CHRISTINA: Mom, I’ll be fine. (to audience) I blew out my hair. I put on my makeup: purple eye shadow, mascara, blush and lipstick. (Pg 46) People just stared at me. I didn’t think I looked like a girl yet, but there was something about people acknowledging me, wondering what I was, that made me happy. (a big, confident smile) (long beat and the smile fades) I quickly became the school’s joke.

LOUDSPEAKER: (Pg 48-49) Send Matthew V to the principal’s office NOW.

PRINCIPAL: You can’t come to school dressed like a woman.

CHRISTINA: I am a woman.

PRINCIPAL: (angrily) You’re a boy! You’re creating this whole circus. Anything that happens to you is your fault because you’re coming to school dressed like a clown!

THE DEAN: (calmer and a little nicer) Look, Matthew, you know you can’t be wearing nails to school. [And] Why do you need to wear so much makeup? My wife doesn’t even wear that much make up.

CHRISTINA: Every girl is different. it’s not in the handbook, so I can do it.

DEAN: We didn’t think we had to address these things because it’s all boys here.

CHRISTINA: (long beat) I think the other students were freaked out because I looked like a girl and I was pressing gender boundaries. There were some instances . . .

BOYS: (Pg 50) You don’t belong here. Go somewhere else. Get out! Faggot!

CHRISTINA: So many people hated me for no reason (beat) (Pg 64) Sometimes I see Matthew in the mirror. Sometimes . . . when I’m lounging around the house with no makeup on or anything, I see him. (Pg 45) Sometimes I feel my mom misses her son. She doesn’t tell me, but she misses her son. (Looks critically in the mirror)

CHRISTINA’S MOM: (Pg 66) (enters) Hold on! Hold on! I have something to say. After all, I’m the one who had the problem with this. [I’m] Christina’s mom. (beat – she hugs Christina) I love my children. I would never throw them out. Some families throw their kids out and they wind up dead. I would never, ever do that.

I told [her] (to Christina) I’m glad that you are proud to be transsexual. But you can’t let people know. . . I had a lot of learning to do. (beat)

Don’t say horrible things to your child. Hug your children. (she hugs Christina) Hug them. I learned through Christina. I listened to my daughter. And I learned by letting her be.
```

---

## IC-1977: The Big Nap

- Title: The Big Nap
- Author (byline): Simon Rich
- Work: New Teeth: Stories, Pgs 29-45
- Publisher: Little, Brown and Company
- Publication date as stated: July 2021
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, DETECTIVE, BABY ANNA, GAGA, MAMA
- Teaser before the introduction: Yes
- Spoken words (computed): 1439
- Already set (do not supply): none

### Source block (context only)

```text
Author: Simon Rich
Book: New Teeth: Stories, Pgs 29-45
ISBN: 978-0316536684
Publisher: Little, Brown and Company
Date (Month/Year): July 2021
```

### Introduction (context only: never use it for content warnings)

```text
The Big Nap by Simon Rich
```

### Performance text (classify this)

```text
NARRATOR: (Pg 29-45) The detective woke up just after dawn. It was a typical morning. His knees were scraped and bruised, his clothes were damp and soiled, and his teeth felt like someone had socked him in the jaw. He reached for the bottle he kept under his pillow and took a sloppy swig. The taste was foul, but it did the trick. Now he could sit up and think. Now he could start to figure out how to somehow face another day.

He stared at his reflection in a mirror. He wasn’t getting any younger. He was two years old, and soon he would be three. Unless he stayed two. He wasn’t sure if you stayed the age you were or if that changed. He wasn’t sure about a lot of things. The only thing he knew was he was tired. Tired of trying to make some sense out of a world gone mad.

NARRATOR: The client was waiting for him in his nursery. He’d seen her around before. She’d come on the scene about a year ago, moving into the white bassinet down the hall. Some people called her Sweetheart. Others called her Pumpkin. But most people knew her by her full name: Baby Anna. She looked innocent enough, with her big wide eyes and Princess Elsa onesie. But her past was murky. The detective had heard that she came from the hospital. But there was also a rumor she’d once lived inside Mommy’s tummy. It didn’t add up. Still, a job was a job.

DETECTIVE: So, what brings you here?

BABY ANNA: It’s Moomoo. She’s missing.

DETECTIVE: Lost toys are small-time. Why should I bust my a** to find some unicorn who’ll probably just turn up under the radiator?

BABY ANNA: Stickers.

DETECTIVE: Are they the fun kind? (Baby Anna holds up a sheet of stickers and he takes a long, slow breath)

NARRATOR: They were fun, all right. He’d never seen so many Batmans in his life. Jumping ones, flying ones, punching ones, kicking ones.

DETECTIVE: That’s a lot of cabbage. Where’d you even get them?

BABY ANNA: I don’t remember. Sometimes things are just in my hand. I don’t remember how I got into this room.

DETECTIVE: I’m on the case, doll.

BABY ANNA: This rug is where I last saw Moomoo.

DETECTIVE: Any chance she ran away?

BABY ANNA: It’s possible, but it’s not like her. She’s always been completely motionless.

DETECTIVE: If Moomoo didn’t run, that means somebody took her. Have you seen any suspicious characters lately?

BABY ANNA: Well, there is an old lady who showed up today out of nowhere and replaced my parents. Gray hair, glasses, smells like yogurt.

DETECTIVE: Sounds like Gaga. I’ve had run-ins with her before. She’s from Florida. You get in an airplane and you watch cartoons, then you wake up in her house and there’s a turkey.

BABY ANNA: If Gaga’s from Florida, what’s she doing here?

DETECTIVE: That’s what I’m gonna find out.

NARRATOR: [But] Gaga was elusive. Sometimes she was lying in the recliner. Sometimes she was inside a phone.

If [he] was going to track her down, his only chance was good old-fashioned shoe leather. He’d been at it for over 10 seconds when he finally caught a break in the case. Gaga picked him up. He decided to tail her. He held on to her neck as she headed for the laundry room. Before long, she was making a phone call.

GAGA: (on the phone as she loads the washer) How’s the air b and b? Listen, what does smart cycle mean?

NARRATOR: Like all grown-ups, Gaga spoke in a secret code designed to keep her operations hidden.

GAGA: Hold on, I’m putting you on speaker . . .

NARRATOR: The detective felt his stomach lurch as a familiar voice rumbled out of Gaga’s phone.

MAMA: We’re driving to the beach. Just google it, okay?

DETECTIVE: There was no mistaking it; the voice belonged to Mama. And that could only mean one thing. This one went all the way to the top. *****

DETECTIVE: (to Baby Anna) I’m off the case! If Mama’s mixed up in this, I don’t want anything to do with it.

BABY ANNA: What’s wrong with Mama? I like Mama.

DETECTIVE: (smirking) We all like Mama. She smells nice. But that doesn’t change the fat she runs this whole town. (whispering) Mama’s the big boss around here. She pulls all the strings. The doctor, the dentist – they’re all on the take. Everybody answers to her.

BABY ANNA: I thought Dada was in charge.

DETECTIVE: Dada’s just a bagman. He’s fat and has a watch, but Mama’s the one calling all the shots. Something’s happening here. Something big and I’m not sticking around to find out what it is.

NARRATOR: He was halfway to his crib when he heard her start to sob. It didn’t take a detective to see the girl was frightened. Her eyes were wide and bleary, and at some point she had pooped big in her pants.

BABY ANNA: Please! You’ve got to help me! You’re the only one who can.

NARRATOR: Why had he gotten mixed up in this crazy case? Was it just for the Batmans? Or was it something else. The screwy kid believed in him. No one ever had before. It was enough to keep him going.

If he wanted to get to the bottom of things, he was going to have to take a risk. He was going to have to go to the TV room. The detective slipped inside and got to work, opening drawers, taking things out and dropping them on the ground. It was an old detective tactic; you touched everything and everything got everywhere. The door burst open. It was Gaga! She grabbed him.

GAGA: How about a nap and some yummy medicine?

NARRATOR: He liked things that were yummy.

DETECTIVE: (Opens mouth for a treat, smiles for a moment, then makes a horrible medicine face)

NARRATOR: The bitter taste of betrayal. It wasn’t the grown-ups’ cruelty that shocked him; it was their cowardice.

DETECTIVE: They never had the guts to do you dirty to your face. They preferred to stab you in the back. They said you could skip vegetables, then snuck them into your mashed potatoes. They said you could have a present, then gave you a potty with a bow on it and told you to poop in it in front of them, as if that were some kind of a gift. And if you asked too many questions, if you go too close to the truth, they did whatever it took to silence you. (holding the bars of his crib as if he were in jail)

NARRATOR: The detective stared at the bars of his crib. The grown-ups had taken away his freedom, his power, and his dignity. But this time the joke was on them. He had nothing left to lose. ******* he makes his escape******

DETECTIVE: (to Baby Anna) Gaga tried to kill me. She drugged me and left me to die inside a crib. She’s capable of anything. Let’s run away together. Get out of this crazy nightmare town.

BABY ANNA: Where would we go?

DETECTIVE: Some place far, far away, where we can make a brand-new start. Maybe the den. . .

BABY ANNA: We’ll never make it! (sudden gasp, and she points)

NARRATOR: Gaga was headed for the stairs, carrying a clear plastic bag.

BABY ANNA: It’s Moomoo. She’s in there! Gaga is taking her somewhere.

DETECTIVE: Looks like she’s headed for the garage. The car’s bedroom, where it sleeps. There’s a big door there that goes up and down . . . A monster!

BABY ANNA: You can’t go down there! You could get eaten!

DETECTIVE: We all get eaten sooner or later, kid.

NARRATOR: The detective climbed down the stairs, [but] Gaga wasn’t alone. Standing beside her were a pair of grim-faced figures, holding suitcases. Mama and Dada had returned!

GAGA: (to Mama) It’s not my fault. Why does the [washing machine] have so many settings?

NARRATOR: Then he spotted Moomoo inside the plastic bag. She’d been murdered! Her horn had been severed and her hooves ripped clean off her body. Her magic wand was bent and her purple cape was singed a gastly black.

Gaga had taken a life and now Mama was back to run the cover-up. The detective watched with disgust as she gestured at Dada, who obediently tossed Moomoo’s corpse into a trash can.

MAMA: (to Gaga) Don’t worry. She’ll never know.

NARRATOR: The grown-ups climbed the stairs. But the detective had to tell Baby Anna what happened. He turned the corner just in time to see Mama take a new unicorn out of a plastic case.

BABY ANNA: (to Detective) Look! Mama found Moomoo!

DETECTIVE: (running to Baby Anna and knocking the unicorn from her hands) That’s not Moomoo. The real Moomoo’s dead. I saw them bury her body! Anna, you can’t trust any of them. They’re all in this together.

NARRATOR: [But] the grown-ups were closing in [on him].

GAGA: (picking up the Detective cooing into his face and pinching his cheek) He’s going through a phase. Sneaking around, getting into everything. He thinks he’s a little detective. (laughing)

NARRATOR: And as their sick coffee breath hit his nose, he felt something snap. Before he could stop himself, he was lunging, arms flailing, legs kicking. He could hear someone screaming in the distance, a piercing high-pitched wail. It took him some time to realize it was his own voice.

MAMA: (to the Detective) How about some yummy medicine?
```

---

## IC-1978: The Big Over Easy

- Title: The Big Over Easy
- Author (byline): Jasper Fforde
- Work: Not specified
- Publisher: Penguin Books
- Publication date as stated: July 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: SPRATT, BRIGGS, DS MARY, MRS. DUMPTY, ANNOUNCER, NURSE, DR. QUATT, SINGH, EXECUTIVE
- Teaser before the introduction: Yes
- Spoken words (computed): 1700
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jasper Fforde
ISBN: 978-0143037231
Publisher: Penguin Books
Date (Month/Year): July 2006
```

### Introduction (context only: never use it for content warnings)

```text
It’s Easter in Reading --- a bad time for eggs. Nursery celebrity Humpty Dumpty is found shattered to death beneath a wall in a shabby area of town. And now it’s up to Detective Jack Spratt and his new partner Mary Mary to solve the case. But Detective Spratt is fresh from a spectacular failure to convict three wily pigs for the murder of a certain wolf -- and the media and tide of public opinion are set squarely against him. Now new trouble is brewing . .

The Big Over Easy by Jasper Fforde.
```

### Performance text (classify this)

```text
SPRATT: (Pg 33) (to audience) The yard was shaped as an oblong, surrounded by a high brick wall with crumbling mortar. At one end, where the dustbins were spilling their rubbish onto the ground, large pieces of eggshell told of a recent an violent death. The victim: Humpty Dumpty – under the jurisdiction of the Nursery Crime Division. (DUM, DUM DUM DUM . . . DUM)

BRIGGS: (Pg 33-35) Looks like he died from injuries sustained falling from a wall. Could be accident, suicide, who knows? He was discovered dead at 0722 this morning.

SPRATT: Anything else I need to know?

BRIGGS: You’re not exactly ‘Mr. Popular’ at the present. There are people who think that spending a quarter of a million pounds on a failed murder conviction for three pigs is not value for money.

SPRATT: I didn’t think justice was meant to have a price tag.

BRIGGS: It’s a public-perception thing, Spratt. Piglets are cute; wolves aren’t. You might as well try and charge the farmer’s wife with cruelty when she cut off the mice’s tails with a carving knife.

SPRATT: I did. (beat) Insufficient evidence.

BRIGGS: So . . . clean up Humpty’s tumble with the minimum of fuss and bother. After that three-pigs debacle, I want it neat, quick and cheap. I want this ex-egg mopped up neat and clean and a report on my desk Wednesday morning. (beckoning DS MARY over) I want you to meet your new Detective Sergeant Mary.

(BRIGGS exits)

DS MARY: (Pg 36) (very contrary to SPRATT) Mary Mary. It’s Mary Mary. That’s my name.

SPRATT: (Pg 42) Detective Inspector Jack Spratt, Nursery Crime Division. (Pg 57-58) (he launches unexcitedly into his usual induction speech as they both examine Humpy’s body) The NCD’s jurisdiction covers all nursery characters. Because we cover well-established situations, patterns begin to emerge. There’s usually a rule of three somewhere, as in beaus, billy goats, blind mice, little pigs. If you come across any stepmothers, they’re usually evil, orphans are ten a penny, and pigs, cats, bears and wolves frequently anthropomorphize.

DS MARY: I wondered why Reading had talking animals.

SPRATT: The Billy Goats Gruff are a blast. I’ll introduce you one day.

DS MARY: No troll?

SPRATT: In the clink. Eight-to-ten-year stretch for threatening behavior. (beginning to brag) (Pg 62-63) Did you hear about the time I saved Hansel and Gretel from being eaten alive by a witch?

DS MARY: No, I’m afraid I didn’t.

SPRATT: Or the time I rescued a hundred children from the Pied Piper of Hamelin? (a shake of the head) Convicted Jill of aggravated assault against Jack?

DS MARY: Nope. (SPRATT sigs heavily) (Pg 37) (MARY rolls her eyes, flips open a notepad, she speaks to the audience) Humpty’s ovoid body had fragmented almost completely. The night’s heavy rain had washed away his liquid center, but there was sill an unmistakably eggy smell.

SPRATT: (to audience) A thin and hairless leg – still with shoe and sock. The biggest piece of shell contained Humpty’s large features. His face was pale white. One of the eyes was open and a crack ran across his face.

DS MARY: The trauma was quite severe. An untrained eye might have dismissed his body as a heap of broken eggshell and a bundle of damp clothing. (Pg 38) How did you know him?

SPRATT: He used to lecture on children’s literature at Reading University. Good company and very funny. (Pg 39) He was fired by the university in 1981 -- made the mistake of having an affair with the dean’s wife, and it didn’t go down too well. (Pg 40) (looking up at the wall)

Humpty had always sat on walls, it was his way.
(returning to business) We should have a word with Mrs.
Dumpty.
***** Mrs. Dumpty’s House*****

MRS. DUMPTY: (Pg 64) He had it coming. Who was it, a jealous husband?

SPRATT: We never said he was murdered, Mrs. Dumpty.

MRS. DUMPTY: (Pg 66-67) We lived together for eighteen years. His philandering got worse. I through it would blow over, small indiscretions that only served to prove he could still charm the ladies. It carried on, grew more and more blatant. (shrugs her shoulders) I changed the locks. Got a divorce.

SPRATT: Did he ever get depressed?

MRS. DUMPTY: (she is visibly moved) Depressed? Are you considering this might be suicide? (then with haughty indifference) He often got depressed. He was an outpatient at St. Cerebellum’s for longer than I had known him. Easter was always bad for him, as you can imagine. Sometime he would wake up at night in a sweat screaming, “Help, Help, Take me off, I’m boiling!” (Pg 112) A recurring nightmare of being boiled alive for exactly three minutes. (Pg 67) (DS MARY laughs and tries to disguise it as a sneeze) I’m sorry, Officer, do you find something funny? (she is done) If you have no other questions . . . (she sees them out)

DS MARY: Think she’s over Dumpty?

SPRATT: Not really. I think she had Secrets. Perhaps not to do with his death, but secrets nonetheless. ****** NEWS BREAK*****

ANNOUNCER: (Pg 107) [This just in . . . ] The Reading genetic industry suffered a severe blow last night when the Quatt Foundation for Genetic Research was closed following its owner’s admission that she conducted morally dubious experiments. The disgraced Dr. Quatt has been permanently banned from funded research and has been shunned by every hospital in the nation, except for St. Cerebellum’s. **** At St. Cerebellum’s Mental Hospital *****

NURSE: (Pg 108) (escorting SPRATT and DS MARY to DR. QUATT’s OFFICE) Dr. Quatt is a brillian woman. Mad as a barrel of skunks, and many people see her as a perverter of all decent virtues . . . but they said the same about Galileo (she laughs) All her work was to alleviate suffering. When they banned her, a dark veil fell over the medical research community. We don’t expect outsiders to truly understand her brilliance.

SPRATT: (Pg 110-112) Dr. Deborah Quatt? We wanted to talk to you about one of your patients – a Mr. Dumpty. You do know that he’s dead.

DR. QUATT: (haughtily and a bit crazy) I was nowhere near him. If you want to try me for malpractice, you’ll have to mount a good case. I’ve plenty of experience defending them, believe you me. (adjusting her tone) Mr. Dumpty? Dead? What a pity. (she looks around, lowers her voice) Did you know that I have successfully grafted a kitten’s head onto a haddock? (back to crazy) It’s not against the law. I just can’t get any funding to do proper research because of damnable outdated moral principles. In the world of cutting-edge genetic research, you can’t make an omelet without breaking eggs.

SPRATT: Which brings us back to Mr. Dumpty. How long had you been his doctor?

DR. QUATT: For five years. I was a psychiatrist before I moved into genetic research . . .

SPRATT: When did you last see him?

DR. QUATT: Six days ago. Easter was a bad time for him, as you can imagine, with all those chocolate eggs being eaten and real ones dyed – he was a virtual prisoner in his own home.

SPRATT: (Pg 113) Thank you, Dr. Quatt. Tell me – and this is just personal curiosity – were you serious when you said you’d grafted a kitten’s head onto a haddock?

DR. QUATT: (crazy returns) Do you want to see?

SPRATT: (Pg 132-133) (his phone rings, he answers, listens, then hangs up) Got a problem with morgues, Mary? [Time to] view some corpses. *****NEWS BREAK*****

ANNOUNCER: [This just in . . .](Pg 92) The incredibly dangerous homicidal maniac known as “The Gingerbreadman” was captured last night. The flour, butter, ginger and sugar psychopath, (Pg 109) with cherry eyes and thin licorice lips, (Pg 92) whose penchant for literally pulling his victims apart, is currently in a secure wing of St. Cerebellum’s (Pg 107) mental hospital, (Pg 92) where he will doubtless remain for the rest of his life. *****

(SPRATT and MARY enter the morgue)

DS MARY: (Pg 133) An ordinary pathologist would have given Humpty the most cursory of glances, but Mrs. Singh was different.

SPRATT: (to SINGH in admiration) So you’ve managed to do what all the king’s men couldn’t.

SINGH: (proudly) One hundred and twenty-six pieces! They say dead men can’t talk, but this one has spoken volumes. Take a look. (She turns Humpty’s reconstructed body over) Look at the damage on the lower back.

SPRATT: (Pg 134) (whispering) Holy s***. He was . . . shot.

SINGH: The discoloration is gunshot residue. Someone came up from the other side of the wall and shot him. By the time the bullet exited, the cracks had already encircled his body and . . . pow! -- Exploded. (beat) (Pg 135) There was one thing that puzzled me, though. (she points to the body) This section of shell, here on his waistline – or neckline, if you prefer. A small hole exactly one-quarter inch in width. Drilled in him – and deliberately too. There was a Band-Aid covering it.

SPRATT: Drug abuse?

SINGH: Possibly. I’ve run the usual tests. I’ll let you know as soon as I have something.

SPRATT: (Pg 137) Humpty didn’t fall, and he didn’t jump. Mary, we should speak to his ex-wife again. (SPRATT and MARY exit)

DS MARY: (Pg 174) (her phone rings) Thanks for calling. We’ll be straight there. (she hangs up) It’s Mrs. Dumpty. There’s been an accident. She’s. . . dead. ***At the offices of Yummy-Time***

EXECUTIVE: (Pg 176-177) (obviously distraught) She’d been a leading light of Yummy-Time since she took over from her father ten years ago. She knew shortbread fingers like the back of her hand. Mr. Aimsworth said he saw her jump into the main dough mixer. (a muffled sob)

SPRATT: I’m going to look at her office. (They enter the office and SPRATT speaks to the audience as he walks to the desk) A picture of her and Humpty in a gilt frame. And there, on the blotter, was a single piece of paper folded once, with [my] name written clearly on the front. (he dons gloves, opens the note and reads it aloud) “DI Spratt – What I did was out of love, not hate. We had been moving towards a reconciliation, until I saw him with a bimbo and my bod boiled. I went to his home and prayed for God to forgive me as I pulled the trigger. – Signed Laura Dumpty”

DS MARY: So she did kill him.

SPRATT: (Pg 178) It seems a bit too perfect. (Spratt’s phone rings, he answers and puts her on speaker)

SINGH: (Pg 363-365) I’ve been trying to reach you all day! I got Humpty’s results back from the Sunny Dale Poultry Labs. Traces of chorioallatonic membrane.

SPRATT: Traces of what?

SINGH: Chorioallatonic membrane. It’s a highly vascularized extra-embryonic membrane that functions as a site for nutrient transport and waste disposal during embryonic development!

SPRATT: Embryonic development? You mean . . .

SINGH: Right. He didn’t die from the gunshot wound or the fall. He hatched.

SPRATT: Humpty Dumpty was pregnant?

SINGH: Pregnant is perhaps the wrong word. He was an egg . . . and eggs, when fertilized, hatch.

DS MARY: Wait a minute, wait a minute. He’s a guy, right? Over sixty-five years of age., so I think we can safely say he was born – laid – whatever – unfertilized. So when was he fertilized?

SINGH: By comparing the volume of his egg, we can safely say . . . about six months ago.

SPRATT: How?

SINGH: The hole I found drilled in his shell. A modified IVF procedure would do the trick.

SPRATT: But it’s still murder. Whatever grew inside him would have been slowly consuming him from within. The question is WHY?

DS MARY: I should imagine the poultry industry might be very interested in a three-ton chicken, sir.

SPRATT: Don’t be ridiculous, Mary. You’d never find an oven big enough. Besides, what misbegotten evil genius would be so cruelly insane as to want to carry out such a bizarre and perverted experiment on a living breathing creature?

DS MARY: Dr. Quatt!

SPRATT: She had the opportunity, the skill, the knowledge. But, more important, the total absence of any ethical standards! Take a couple of officers and go to St. Cerebellum’s to arrest Dr. Quatt. [I’ll] call the Ops room and see if anyone has reported seeing a giant chicken loose in Reading! (DUM, DUM DUM DUM . . . DUM)
```

---

## IC-1979: Bigfoot Walks into Town

- Title: Bigfoot Walks into Town
- Author (byline): Chris Brock
- Work: Thousand Islands Life Magazine, Volume 14, Issue 2
- Publisher: Thousand Island Life.com
- Publication date as stated: February 2019
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MYRON, CLIFFORD, POLICE CHIEF MYERS, PATROLMAN WEST, BIGFOOT, COLLEGE PRESIDENT, PROFESSOR, CROWD, DOG CONTROL OFFICER, MAYOR
- Teaser before the introduction: No
- Spoken words (computed): 934
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chris Brock
Book: Thousand Islands Life Magazine,
Volume 14, Issue 2
ISBN: On-Line Magazine
https://thousandislandslife.com/tag/february-2019/]
Publisher: Thousand Island Life.com
Date (Month/Year): February 2019
```

### Introduction (context only: never use it for content warnings)

```text
For decades, people around the world have been fascinated with the legend of Bigfoot, Sasquatch or whatever you choose to call it. Sightings of a furry, upright biped and reports of beastly footprints have been reported in American from Kentucky to the Pacific Northwest.

Is Bigfoot real? Nope, not going to answer that question. But one thing is for certain. If Bigfoot does exist, he definitely holds the title of Hide and Seek Champion of the World! But seriously . . . what would you do if one day, with no advance warning . . .

Bigfoot Walks into Town by Chris Brock
```

### Performance text (classify this)

```text
NARRATOR: The Bigfoot wandered into Highville one fine summer morning and climbed a large maple tree in the village park. (pantomime Bigfoot gazing over the town with a confused expression) As the sun rose over the village in the foothills of the Adirondacks, Myron Jones, the owner of the Highville Diner, told the regulars who were buzzing about the unusual wildlife development that the creature looked lost. It just sat there in a notch of two big branches, gazing over the village like he (Myron was certain it was a he) was trying to remember where he parked his car.

MYRON: (speaks while he is scrambling eggs as if he is an expert) It’ll find his way home. They always do.

NARRATOR: Clifford Answorth, a regular customer of the diner, disagreed. Between sips of coffee, he said the beast wasn't lost but that it looked dangerous and theorized it was obviously planning an overthrow of the village. He also thought it purposely swam across the St. Lawrence River from Canada and came down the river valley to its current perch proving its insidious craftiness.

CLIFFORD: Just you wait. That thing has friends. You’d better lock your doors tonight.

NARRATOR: The Highville Police Department was dispatched to the scene and set up a command center in the shadow of the tree; and the whole park was shortly surrounded by yellow crime tape.

POLICE CHIEF MYERS: (staring up at the creature) Jeez, I didn’t think Bigfoots were real. (he reacts to a horrible smell)

NARRATOR: The first thing he noticed was the smell, and he recalled reading about a particular odor that was reported with Bigfoot sightings.

PATROLMAN WEST: (takes a sip of coffee and opens his laptop) I think it has something to do with what they eat. (he rapidly types in some keywords to search for information, then reports eagerly) Did you know they eat cows?

POLICE CHIEF MYERS: I don’t care what they eat. Our first problem is getting it down. Maybe if he ate a crow or two, it would be a good thing.

PATROLMAN WEST: I said cows, and we don't know for sure if it's a he.

POLICE CHIEF MYERS: Whatever.

PATROLMAN WEST: (still skimming the laptop article, amazed at the information) And in Canada, Bigfoots are known to ride moose. It's how they migrate.

NARRATOR: Backed up by such expert knowledge, a half dozen officers approached the tree carefully, (pantomime fearful officer approaching the tree) looking up at each step, as if they were certain the Bigfoot was going to jump down onto them, like some sort of airborne Ninja. But fears passed as they got closer and . . . nothing happened.

PATROLMAN WEST: (surprised) He doesn’t seem to be bothered by us.

POLICE CHIEF MYERS: (retrieves his bullhorn and speaks into it, the words coming out seconds apart) DO . . . YOU . . . KNOW . . . WHERE . . . YOU . . . ARE?!

BIGFOOT: (lazily looks down at the officers)

PATROLMAN WEST: (laughing, maybe with a snort) What? You expect him to understand English? And I think he’d know that he’s obviously in a tree.

POLICE CHIEF MYERS: You’re right (embarrassed and befuddled; he thinks for a moment, scratches his head and has a brilliant idea) Call the community college!

NARRATOR: "Call the community college!" was like the village of Highville's Bat Signal. It was reserved only for such special circumstances. Maybe the college had a Bigfoot expert who knew the language! (Disappointed Wah, Wah, Wah) [But] The closest they could find to a Bigfoot language linguist was a part-time anthropology professor who once studied the mating habits of Ugandan ostriches.

POLICE CHIEF MYERS: Close enough!

NARRATOR: Before the professor was dispatched to the scene, the college’s president hastily called a press conference.

COLLEGE PRESIDENT: (grabbing a reporter’s microphone she stares dramatically into the camera) If the county gave us more money, we could afford to staff a Bigfoot expert. [Now] Our county, and perhaps our entire state, is in peril!

NARRATOR: But the anthropology professor, who was flown to the scene via the Highville Fire Department’s helicopter, did have some useful information.

PROFESSOR: (pompously lecturing the police) Yes, this looks like a familiar case. Ostriches often will chase their prey into trees, hoping they will later expire. I suggest you wait it out.

POLICE CHIEF MYERS: (waiting for more expert advice and reacting with intense nonverbal expressions when he realizes that none is forthcoming) [Well,] that was the most useless advice I ever got.

NARRATOR: At noon, the fire department was called in. All were losing patience. It was obvious something had to be done soon, especially when politics entered the picture. The local Democratic Party said the Bigfoot migration to the town was an effect of global warming. Meanwhile, the Republicans, despite obvious evidence to the contrary, declared the creature wasn’t a Bigfoot at all, but rather a well-fed, inquisitive bear.

NARRATOR: The crowd was getting larger, and members of the media were now streaming the event live. Makeshift signs had appeared.

CROWD: (chanting) We Support Bigfoot! Health Care for Sasquatch! Don’t Let a Liberal Bigfoot Loose! Bigfoot for Congress!

BIGFOOT: (observes the chaos below like a casual observer, shaking its head and rolling its eyes, yawning and eventually nodding off to sleep. It is not impressed with the intelligence of the humans below)

NARRATOR: It woke up when a ladder was slowly extended from a fire truck to the tree.

BIGFOOT: (jolted awake; it appears angry. It breaks a stick from the tree and pounds on the ladder with it)

NARRATOR: The sound echoed off nearby buildings.

PATROLMAN WEST: (in wonder) That’s how they communicate! I saw it on the Discovery Channel! I think he’s calling other Bigfoots.

PROFESSOR: (condescendingly) The plural of Bigfoot is Bigfeet.

POLICE CHIEF MYERS: (with false bravado) I don’t care what you call them. Let’s end this now. Bring out the tranquilizer gun.

NARRATOR: Patrolman West radioed back to the station. The one remaining officer there said the tranquilizer gun wasn’t available. Actually, the gun was available, but all the tranquilizer darts had been used up during crowd control at the County Fair.

POLICE CHIEF MYERS: Well, maybe we should just shoot the darn critter with a regular rifle. It’s getting awfully late. And this crowd is getting too wild.

CROWD: (chanting) We Support Bigfoot! Health Care for Sasquatch!

NARRATOR: So, the village’s dog control officer did the duty.

DOG CONTROL OFFICER: (takes aim and fires one shot)

(long beat)

NARRATOR: As the sun set, a nearby roofing crew was available to retrieve the body. The roofers wanted to keep the Bigfoot, stuff it, and use it as a mascot that they could place in front yards at their projects. But Highville Mayor Charlie James consulted with Chief Myers.

MAYOR: I think we should bury it at sea like they did with Bin Laden.

POLICE CHIEF MYERS: Good idea. The last thing we need is a Bigfoot grave acting as an attraction for all sorts of loonies.

NARRATOR: Under the cover of darkness, the Bigfoot was wrapped in a tarp, loaded aboard the ferry that journeyed between Cape Vincent and Wolff Island, weighed down, and dumped overboard. The boat crew thought no one saw the dumping and gave each other high-fives. (beat) But on the shore, eyes peered out from the woods -- no one quite certain if they were of man -- or of beast.
```

---

## IC-1980: The Birds for Christmas

- Title: The Birds for Christmas
- Author (byline): Mark Richard
- Work: Charity
- Publisher: Anchor
- Publication date as stated: Aug 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1863
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mark Richard
Book: Charity
ISBN: 978-0385425704
Publisher: Anchor
Date (Month/Year): Aug 1999
```

### Introduction (context only: never use it for content warnings)

```text
Author Mark Richard grew up in a very poor Virginia family in the racially-divided 1960s. He was born with deformed hips and spent years in and out of the Richmond Crippled Children’s Hospital. In his short story “The Birds for Christmas” he vividly recalls one of the many holidays he spent in the children’s ward. Health care . . . especially “charitable, un-regulated” health care in the 1960’s was quite different from the health care we’ve come to expect today.

The Birds for Christmas by Mark Richard
```

### Performance text (classify this)

```text
We wanted "The Birds" for Christmas. We had seen the commercials for it on the television donated third-hand by the Merchant Seamen's and Sailors' Rest Home, a big black-and-white Zenith of cracked plastic and no knobs, a dime stuck in the channel selector. You could adjust the picture and have no sound, or hi-fi sound and no picture. We just wanted the picture. We wanted to see "The Birds."

The Old Head Nurse said not to get our hopes up. It was a "Late Show" after Lights Out the night before Christmas Eve. She said it would wake the babies and scare the Little Boys down on the far end of the ward. Besides, she said, she didn't think it was the type of movie we should be seeing Christmas week. She said she was certain there would be Rudolph and Frosty on. That would be more appropriate for us to watch on the night before Christmas Eve.

"Frosty," Michael Christian said to me. "I see that a hunrett times. I want to see "The Birds," man. I want to see those birds get all up in them people's hair. That's some real Christmas TV to me."

Michael Christian and I were some of the last Big Boys to be claimed for Christmas. We were certain someone would eventually come for us. We were not frightened yet. There were still some other Big Boys around--the Big Boy who ran away to a gas station every other night, the Human Skeleton who would bite you, and the guy locked away on the sun porch who the Young Doctors were taking apart an arm and a leg at a time.

The Young Doctors told Michael Christian that their Christmas gift to him would be that one day he would be able to do a split onstage like his idol, James Brown. There never seemed to be any doubt in Michael Christian's mind about that. For now, he just wanted to see "The Birds" while he pretended to be James Brown in the Hospital.

Pretending to be James Brown in the Hospital was not without its hazards for Michael Christian; he had to remember to keep his head lifted from his pillow so as not to bedhead his budding Afro. Once, when he was practicing his singing, the nurses rushed to his bed asking him where it hurt.

"I'm warming up "I Feel Good," stupid," said Michael Christian. Then his bed was jerked from the wall and wheeled with great speed, pushed and pulled along by hissing nurses, jarring other bedsteads, Michael Christian's wrists hanging over the safety bedrails like jailhouse-window hands; he was on his way to spend a couple of solitary hours out in the long, dark, and empty hall, him rolling his eyes at me as he sped past, saying, "Aw, man, now I feel BAD!"

Bed wheeling into the hall was one of the few alternatives to corporal punishment the nurses had, most of them being reluctant to spank a child in traction for spitting an orange pip at his neighbor, or to beat a completely burned child for cursing. Bed wheeling into the hall was especially effective at Christmastime, when it carried the possibility of missing Christmas programs. A veteran of several Christmases in the Hospital and well acquainted with the grim Christmas programs, Michael Christian scoffed at the treasures handed out by the church and state charities-- the aging fruit, the surplus ballpoint pens, the occasional batches of recycled toys that didn't work, the games and puzzles with missing pieces. Michael Christian's Christmas Wish was as specific as mine. I wanted a miniature train set with batteries so I could lay out the track to run around on my bed over the covers. Not the big Lionel size or the HO size. I wanted the set you could see in magazines, where they show you the actual size of the railroad engine as being no larger than a walnut.

"You never get that, man," Michael Christian said, and he was right.

James Brown in the Hospital's Christmas Wish was for "The Birds" for Christmas. And, as Michael Christian's friend, I became an accomplice in his desire. In that way, "birds" became a code, the way words can among boys.

"Gimme some BIRDS!" Michael Christian would squawk when the society ladies on their annual Christmas visit asked us what we wanted.

"How about a nice hairbrush?" a society lady said, laying one for white people at the foot of Michael Christian's bed.

"I want a pick," Michael Christian told her.

"A pick? A shovel and a pick? To dig with?" asked the society lady.

"I think he wants a comb for his hair," I said. "For his Afro."

"That's right: a pick," said Michael Christian. "Tell this stupid white *witch* something. Squawk, squawk," he said, flapping his elbows like wings, as the nurses wheeled him out into the hall. "Gimme some BIRDS!" he shouted, and when they asked me, I said to give me some birds, too.

Michael Christian's boldness over the Christmas programs increased when Ben, the night porter, broke the television. Looking back, it may not be fair to say that Ben, the night porter, actually broke the television, but one evening it was soundlessly playing some kiddie Christmas show and Ben was standing near it mopping up a spilt urinal can when the screen and the hope of Michael Christian's getting his Christmas Wish blackened simultaneously. It was a somber Lights Out.

The next night, a priest and some students from the seminary came by. Practice Preachers, Michael Christian said. While one of the students read the Christmas story from the Bible, Michael Christian pretended to peck his own eyes out with pinched fingers. When the story was finished, Michael Christian said, "Now, you say the sheepherding guys was so afraid, right?"

"Sore afraid," said the Practice Preacher. "The shepherds had never seen angels before, and they were sore afraid."

"Naw," said Michael Christian. "I'll tell you what-- they saw these big white things flapping down and they was big birds, man. I know birds, man, I know when you got bird problems, man."

"They were angels," said the young seminary student.

"Naw," said Michael Christian. "They was big white birds, and the sheepherding guys were so afraid the big white birds was swooping down and getting all up in they hair and stuff! Squawk, squawk!" he said, flapping around in his bed.

"Squawk, squawk!" I answered, and two of the Practice Preachers assisted the nurses in wheeling Michael Christian into the hall and me into the linen cupboard.

One night in the week before Christmas, a man named Sammy came to visit. He had been a patient as a child, and his botched cleft-palate and harelip repairs were barely concealed by a weird line of blond mustache. Sammy owned a hauling company now, and he showed up blistering drunk, wearing a ratty Santa suit, and began handing out black-strapped Timex Junior wristwatches. I still have mine, somewhere.

One by one we told Sammy what we wanted for Christmas, even though we were not sure, because of his speech defect, that that was what he was asking. Me, the walnut train; Michael Christian, "The Birds." We answered without enthusiasm, without hope: it was all by rote. By the end of the visit, Sammy was a blubbering sentimental mess, reeking of alcohol and promises. Ben, the night porter, put him out.

It was Christmas Eve week. The boy who kept running away finally ran away for good. Before he left, he snatched the dime from the channel selector on our broken TV. We all saw him do it and we didn't care. We didn't even yell out to the night nurse, so he could get a better head start than usual.

It was Christmas Eve week, and Michael Christian lay listless in his bed. We watched the Big Boy ward empty. Somebody even came for one of the moaners, and the guy out on the sun porch was sent upstairs for a final visit to the Young Doctors so they could finish taking him apart.

On the night before Christmas Eve, Michael Christian and I heard street shoes clicking down the long corridor that led to where we lay. It was after lights out. We watched and waited and waited. It was just Sammy the Santa, except this time he was wearing a pale-blue leisure suit, his hair was oiled back, and his hands, holding a red-wrapped box, were clean.

What we did not want for Christmas were wristwatches. What we did not want for Christmas were bars of soap. We did not want any more candy canes, bookmarks, ballpoint pens, or somebody else's last year's broken toy. For Christmas we did not want plastic crosses, dot books, or fruit baskets. No more handshakes, head pats, or storybook times. It was the night before Christmas Eve, and Michael Christian had not mentioned "The Birds" in days, and I had given up on the walnut train. We did not want any more Christmas Wishes.

Sammy spoke with the night nurse, we heard him plead that it was Christmas, and she said all right, and by her flashlight she brought him to us. In the yellow spread of her weak batteries, we watched Michael Christian unwrap a portable television.

There was nothing to be done except plug the television into the wall. It was Christmas, Sammy coaxed the reluctant night nurse. They put the little TV on a chair and we watched the end of an Andy Williams Christmas Special. We watched the eleven-o'clock news. Then the movie began: "The Birds." It was Christmas, Sammy convinced the night nurse.

The night nurse wheeled her chair away from the chart table and rolled it to the television set. The volume was low, so as not to disturb the damaged babies at the Little Boy end of the ward--babies largely uncollected until after the holidays, if at all. Sammy sat on an empty bed. He patted it. Michael Christian and I watched "The Birds."

During the commercials, the night nurse checked the hall for the supervisor. Sammy helped her turn any infant that cried out. The night nurse let Sammy have some extra pillows. Michael Christian spoke to me only once during a commercial when we were alone, he said, "Those birds messing them people up."

When the movie was over, it was the first hours of Christmas Eve. The night nurse woke Sammy and let him out through the sun porch. She told us to go to sleep, and rolled her chair back to her chart table. In the emptiness you could hear the metal charts click and scratch, her folds of white starch rustle. Through a hole in the pony blanket I had pulled over my head I could see Michael Christian's bed. His precious Afro head was buried deep beneath his pillow.

At the dark end of the ward a baby cried in its sleep and then was still.

It was Christmas Eve, and we were sore afraid.
```

---

## IC-1981: Blimey, Frognal Cockfosters

- Title: Blimey, Frognal Cockfosters
- Author (byline): Dave Barry
- Work: Dave Barry Talks Back
- Publisher: Three Rivers Press
- Publication date as stated: May 1992
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ME, BRITISH PERSON
- Teaser before the introduction: No
- Spoken words (computed): 858
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Barry
Book: Dave Barry Talks Back
ISBN: 978-0517588680
Publisher: Three Rivers Press
Date (Month/Year): May 1992
```

### Introduction (context only: never use it for content warnings)

```text
At 8:50 a.m. on July 7, 2005 three bombs exploded within 50 seconds of each other on three London Underground trains. The bombings led to a severe, day-long disruption of the city's transport and mobile telecommunications infrastructure.

Fifty-six people were killed in the attacks, including the four bombers, and about 700 injured, of whom about 100 required overnight hospital treatment. The incident was the deadliest single act of terrorism in the United Kingdom since Lockerbie (the 1988 bombing of Pan Am Flight 103 which killed 270), and the deadliest bombing in London since the Second World War.

Despite the somber tone of recent events in London, it is possible to look on the lighter side of public transit and in fact the London culture in general. What more can I say but: Blimey, Frognal Cockfosters by Dave Barry.
```

### Performance text (classify this)

```text
Recently my family and I spent a week in London, which is a popular foreign place to visit because they have learned to speak some English over there. Although frankly they have a long way to go. Often, when they get to the crucial part of a sentence, they'll realize that they don't know the correct words, so they'll just make some silly ones up. I had a lot of conversations that sounded like this:

ME: Excuse me. Could you tell us how to get to Buck-ingham Palace?

BRITISH PERSON: Right. You go down this street here, then you nip up the weckershams.

ME: We should nip up the weckershams?

BRITISH PERSON: Right. Then you take your first left, then you just pop 'round the gorn-and-scumbles, and, Jack's a doughnut, there you are!

ME: Jack's a doughnut?

BRITISH PERSON: Right.

Also they have a lot of trouble with pronunciation, because they can't move their jaw muscles, because of malnutrition caused by wisely refusing to eat English food, much of which was designed and manufactured in medieval times during the reign of King Walter the Mildly Disturbed. Remember when you were in junior high school, and sometimes the cafeteria workers would open up a large Army-surplus food can left over from the Spanish-American War and serve you a scary-looking dish with a name like "Tuna Bean Prune Cabbage Omelet Casserole Surprise"?

Well, they still have a lot of food like that over in England, on permanent display in bars, called "pubs," where people drink for hours but nobody ever eats. We saw individual servings of pub food that we recognized from our last visit, in 1978.

Some dishes-no effort is made to conceal this fact,- contain kidneys. We also saw one dish with a sign next to it that said-I swear I am not making this up-"Spotted Dick."

The English are very good at thinking up silly names. Here are some actual stations on the London under-ground: Marylebone, Tooting Broadway, Piccadilly Circus, Cockfosters, Frognal, Goodge Street, Mudchute, Barking, and East Ham. Londoners are apologetic about their underground, which they believe has become filthy and noisy and dangerous, but which is in fact far more civilized than the average American wedding reception.

At the height of rush hour, people on the London underground actually say "excuse me." Imagine what would happen if you tried an insane stunt like that on the New York City subway. The other passengers would take it as a sign of weakness, and there'd be a fight over who got to keep your ears as a trophy.

Our primary cultural activity in London was changing money. We had to do this a lot because the dollar is very weak. Europeans use the dollar primarily to apply shoe polish. So every day we'd go to one of the money-chang-ing places that are all over London, and we'd exchange some dollars for British money, which consists of the "pound" and a wide variety of mutant coins whose sizes and shapes are unrelated to their values, and then we'd look for something to eat that had been invented in this country, such as pizza, and we'd buy three slices for what we later realized was $247.50, and then we'd change some money again. Meanwhile the Japanese tourists were exchanging their money for items such as Westminster Abbey.

In the interest of broadening our ten-year-old son's cultural awareness, we visited some important historic sites, including the Tower of London, the London Dun-geon, and Madame Tussaud's Wax Museum, all of which are devoted to explaining in clinical detail how various historic members of royalty were whacked into small historic pieces. English history consists largely of royal people getting their heads chopped off, which is why members of the royal family now wear protective steel neck inserts, which is why they walk the way they do.

Needless to say, this brand of history was a hit with our son. He especially enjoyed the guided "Jack the Ripper"

tour that we took one dark night with a very intense guide. "Right on this spot is where they found the victim's intestines," she'd say. "And right here is where they found the liver, which is now part of the food display of that pub over there."

Another cultural activity we frequently engaged in was looking the wrong way before attempting to cross streets. The problem is that in America, people drive on the right side of the street, whereas in London, they drive on both sides of the street, using hard-to-see cars about the size of toaster ovens. The best way to handle this, as a tourist, is to remain on one side of the street for your entire visit, and see the other side on another trip.

But I definitely recommend London for anybody who enjoys culture and could stand to lose a few pounds. I learned many things that will be of great value to me, not just personally, but also professionally, and I'm not saying that just to be polite to the English. I'm saying it because of Internal Revenue Service regulations.
```

---

## IC-1982: Blood-Burning Moon

- Title: Blood-Burning Moon
- Author (byline): Jean Toomer
- Work: The Oxford Book of American Short Stories
- Publisher: Oxford University Press
- Publication date as stated: Sept 1994
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2407
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jean Toomer
Book: The Oxford Book of American Short Stories
ISBN: 978-0195092622
Publisher: Oxford University Press
Date (Month/Year): Sept 1994
```

### Introduction (context only: never use it for content warnings)

```text
In the South, during the period 1880 to 1940, there was deep-seated and all-pervading hatred and fear of the Negro which led white mobs to turn to “lynch law” as a means of social control. Lynchings—open public murders of individuals suspected of crime conceived and carried out more or less spontaneously by a mob—seem to have been an American invention. Most of the lynchings were by hanging or shooting, or both. However, many were of a more hideous nature—burning at the stake, maiming, dismemberment, castration, and other brutal methods of physical torture. Lynching therefore was a cruel combination of racism and sadism, which was utilized primarily to sustain the caste system in the South. Many white people believed that Negroes could only be controlled by fear. To them, lynching was seen as the most effective means of control. In Blood-Burning Moon by Jean Toomer
```

### Performance text (classify this)

```text
Up from the skeleton stone walls, up from the rotting floor boards and the solid hand-hewn beams of oak of the pre-war cotton factory, dusk came. Up from the dusk the full moon came. Glowing like a fired pine-knot, it illumined the great door and soft showered the Negro shanties aligned along the single street of factory town. The full moon in the great door was an omen. Negro women improvised songs against its spell.

we see how passions can quickly spiral out of control.

Louisa sang as she came over the crest of the hill from the white folks' kitchen. Her skin was the color of oak leaves on young trees in fall. Bob Stone, younger son of the people she worked for, loved her. By the way the world reckons things, he had won her. By measure of that warm glow which came into her mind at thought of him, he had won her. Tom Burwell, whom the whole town called Big Boy, also loved her. But working in the fields all day, and far away from her, gave him no chance to show it. His black balanced, and pulled against, the white of Stone, when she thought of them.

To meet Bob in the canebrake, as she was going to do an hour or so later, was nothing new. And Tom's proposal which she felt on its way to her could be indefinitely put off. Separately, there was no unusual significance to either one. But for some reason, they jumbled when her eyes gazed vacantly at the rising moon.. Louisa came down into factory town and sank wearily upon the step before her home. The moon was rising towards a thick cloud-bank which soon would hide it.

Red nigger moon. Sinner!

Blood-burning moon. Sinner!

Come out that fact'ry door.

Up from the deep dusk of a cleared spot on the edge of the forest a mellow glow arose and spread fan-wise into the low-hanging heavens. And all around the air was heavy with the scent of boiling cane. A large pile of cane-stalks lay like ribboned shadows upon the ground. A mule, harnessed to a pole, trudged lazily round and round the pivot of the grinder. Beneath a swaying oil lamp, a Negro alternately whipped out at the mule, and fed cane-stalks to the grinder. The scent of cane came from the copper pan and drenched the forest and the hill that sloped to factory town, beneath its fragrance. It drenched the men in circle seated around the stove. Some of them chewed at the white pulp of stalks, but there was no need for them to, if all they wanted was to taste the cane. One tasted it in factory town.

Tom Burwell chewed cane-stalk and laughed with the others till someone mentioned Louisa. Till someone said something about Louisa and Bob Stone, about the silk stockings she must have gotten from him. Blood ran up Tom's neck hotter than the glow that flooded from the stove. He sprang up. Glared at the men and said, "She's my gal." Will Manning laughed. Tom strode over to him. Yanked him up and knocked him to the ground. Several of Manning's friends got up to fight for him. Tom whipped out a long knife and would have cut them to shreds if they hadn’t ducked into the woods. Tom had had enough. He nodded to Old David Georgia and swung down the path to factory town. He forced his mind to fasten on Louisa. Bob Stone. Better not be. He turned into the street and saw Louisa sitting before her home. He went towards her, ambling, touched the brim of a marvelously shaped, spotted, felt hat, said he wanted to say something to her, and then found that he didn’t know what he had to say, or if he did, that he couldn’t say it.

He shoved his big fists in his overalls, grinned, and started to move off.

"Youall want me, Tom?"

"Thats what us wants, sho, Louisa."

"Well, here I am --"

"An here I is, but that aint ahelpin none, all th same."

"You wanted to say something? …"

"I did that, sho. But words is like th spots on dice: no matter how y fumbles em, there's times when they jes wont come. I dunno why. Seems like th love I feels fo yo done stole m tongue. I got it now. Whee! Louisa, honey, I oughtnt tell y, I feel I oughtnt cause yo is young an goes t church an I has had other gals, but Louisa I sho do love y. Lil gal, An next year if ole Stone'll trust me, I'll have a farm. My own. My bales will buy yo what y gets from white folks now. Silk stockings an purple dresses -- course I dont believe what some folks been whisperin as t how y gets them things now. White folks always did do for niggers what they likes. An they jes cant help alikin yo, Louisa. Bob Stone likes y.

Course he does. But not th way folks is awhisperin. Does he, hon?"

"I dont know what you mean, Tom."

"Course y dont. Ise already cut two niggers. Had t hon, t tell em so. Niggers always tryin t make somethin out a nothin. An then besides, white folks aint up t them tricks so much nowadays. Godam better not be. Leastawise not with yo. Cause I wouldnt stand f’ it. Nassur."

"What would you do, Tom?"

"Cut him jes like I cut a nigger."

"No, Tom --"

"I said I would an there aint no mo to it. But that aint th talk f now.

Tom took her hand in his. Against the tough thickness of his own, hers felt soft and small. His huge body slipped down to the step beside her. The full moon sank upward into the deep purple of the cloud-bank. An old woman brought a lighted lamp and hung it on the common well whose bulky shadow squatted in the middle of the road, opposite Tom and Louisa. The old woman lifted the well-lid, took hold the chain, and began drawing up the heavy bucket. As she did so, she sang.

Red nigger moon. Sinner!

Blood-burning moon. Sinner!

Come out that fact'ry door.

Bob Stone sauntered from his veranda out into the gloom of fir trees and magnolias. The clear white of his skin paled, and the flush of his cheeks turned purple. As if to balance this outer change, his mind became consciously a white man's. He passed the house with its huge open hearth which, in the days of slavery, was the plantation cookery. He saw Louisa bent over that hearth. He went in as a master should and took her. Direct, honest, bold. None of this sneaking that he had to go through now. The contrast was repulsive to him. His family had lost ground. Hell no, his family still owned the niggers, practically. Damned if they did, or he wouldn’t have to duck around so. What would they think if they knew?. He was going to see Louisa tonight, She was lovely -- in her way. Nigger way. What way was that? Damned if he knew. Must know. He'd known her long enough to know. Was there something about niggers that you couldn’t know? Listening to them at church didn’t tell you anything. Looking at them didn’t tell you anything. Talking to them didn’t tell you anything -- unless it was gossip, unless they wanted to talk. Of course, about farming, and licker, and craps -- but those weren’t nigger. Nigger was something more. How much more? Something to be afraid of, more? Hell no. Who ever heard of being afraid of a nigger? Tom Burwell. Cartwell had told him that Tom went with Louisa after she reached home. No sir. No nigger had ever been with his girl. He'd like to see one try. Some position for him to be in. Him, Bob Stone, of the old Stone family, in a scrap with a nigger over a nigger girl. She was worth it. Beautiful nigger gal. Why nigger? Why not, just gal? No, it was because she was nigger that he went to her. Sweet … The scent of boiling cane came to him. Then he saw the rich glow of the stove. He heard the voices of the men circled around it. He was about to skirt the clearing when he heard his own name mentioned. He stopped. Quivering. Leaning against a tree, he listened.

"Bad nigger. Yassur, he sho is one bad nigger when he gets started."

"Tom Burwell's been on th gang three times fo cuttin men."

"What y think he's agwine t do t Bob Stone?"

"Dunno yet. He aint found out. When he does -- Baby!"

Bob Stone's ears burned as though he had been holding them over the stove. Sizzling heat welled up within him. His feet felt as if they rested on red-hot coals. They stung him to quick movement. He circled the fringe of the glowing. Not a twig cracked beneath his feet. He reached the path that led to factory town. Plunged furiously down it. Halfway along, a blindness within him veered him aside. He crashed into the bordering canebrake. Cane leaves cut his face and lips. He tasted blood. He threw himself down and dug his fingers in the ground. After a long while, or so it seemed to him, the thought came to him that it must be time to see Louisa. He got to his feet and walked calmly to their meeting place. No Louisa. Tom Burwell had her. Veins in his forehead bulged and distended. Saliva moistened the dried blood on his lips. He bit down on his lips. He tasted blood. Not his own blood; Tom Burwell's blood. Bob drove through the cane and out again upon the road.. Palpitant between the rooster crows, a chill hush settled upon the huddled forms of Tom and Louisa. A figure rushed from the shadow and stood before them. Tom popped to his feet.

"Whats y want?"

"I'm Bob Stone."

"Yassur -- an I'm Tom Burwell. Whats y want?"

Bob lunged at him. Tom side-stepped, caught him by the shoulder, and flung him to the ground. Straddled him.

"Let me up."

"Yassur -- but watch yo doins, Bob Stone."

A few dark figures, drawn by the sound of scuffle, stood about them. Bob sprang to his feet.

"Fight like a man, Tom Burwell, an I'll lick y."

Again he lunged. Tom side-stepped and flung him to the ground. Straddled him.

"Get off me, you godam nigger you."

"Yo sho has started somethin now. Get up."

Tom yanked him up and began hammering at him. Each blow sounded as if it smashed into a precious, irreplaceable soft something. Beneath them, Bob staggered back. He reached in his pocket and whipped out a knife.

"Thats my game, sho."

Blue flash, a steel blade slashed across Bob Stone's throat. He had a sweetish sick feeling. Blood began to flow. Then he felt a sharp twitch of pain. He let his knife drop. He slapped one hand against his neck. He pressed the other on top of his head as if to hold it down. He groaned. He turned, and staggered towards the crest of the hill in the direction of white town. Negroes who had seen the fight slunk into their homes and blew the lamps out. Louisa, dazed, hysterical, refused to go indoors. She slipped, crumbled, her body loosely propped against the woodwork of the well. Tom Burwell leaned against it. He seemed rooted there.

Bob reached Broad Street. White men rushed up to him. He collapsed in their arms.

"Tom Burwell…."

White men like ants upon a forage rushed about. Except for the taut hum of their moving, all was silent. Shotguns, revolvers, rope, kerosene, torches. Two high-powered cars with glaring search-lights. They came together. The taut hum rose to a low roar. Then nothing could be heard but the flop of their feet in the thick dust of the road. The moving body of their silence preceded them over the crest of the hill into factory town. It flattened the Negroes beneath it. It rolled to the wall of the factory, where it stopped. Tom knew that they were coming. He couldn’t move. And then he saw the search-lights of the two cars glaring down on him. A quick shock went through him. He stiffened. He started to run. A yell went up from the mob. Tom wheeled about and faced them. They poured down on him. They swarmed. A large man with dead-white face and flabby cheeks came to him and almost jabbed a gun-barrel through his guts.

"Hands behind y, nigger."

Tom's wrists were bound. The big man shoved him to the well. Burn him over it, and when the woodwork caved in, his body would drop to the bottom. Two deaths for a godam nigger. The mob pushed in. Its pressure, its momentum was too great. Drag him to the factory. Wood and stakes already there. Tom moved in the direction indicated. But they had to drag him. They reached the great door. Too many to get in there. The mob divided and flowed around the walls to either side. The big man shoved him through the door. The mob pressed in from the sides. Taut humming. No words. A stake was sunk into the ground. Rotting floor boards piled around it. Kerosene poured on the rotting floor boards. Tom bound to the stake. His breast was bare. Nails' scratches let little lines of blood trickle down and mat into the hair. His face, his eyes were set and stony. Except for irregular breathing, one would have thought him already dead. Torches were flung onto the pile. A great flare muffled in black smoke shot upward. The mob yelled. The mob was silent. Now Tom could be seen within the flames. Only his head, erect, lean, like a blackened stone. Stench of burning flesh soaked the air. Tom's eyes popped. His head settled downward. The mob yelled. Its yell echoed against the skeleton stone walls and sounded like a hundred yells. Like a hundred mobs yelling.

Red nigger moon. Sinner!

Blood-burning moon. Sinner!

Come out that fact'ry door.
```

---

## IC-1983: The Blundered Buss

- Title: The Blundered Buss
- Author (byline): Patrick F. McManus
- Work: The Good Samaritan Strikes Again
- Publisher: Henry Holt & Company, Inc.
- Publication date as stated: Sept 1993
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1254
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patrick F McManus
Book: The Good Samaritan Strikes Again
ISBN: 978-0805029222
Publisher: Henry Holt & Company, Inc.
Date (Month/Year): Sept 1993
```

### Introduction (context only: never use it for content warnings)

```text
The questions are as old as time: Where do your noses go? Eyes open or closed? Which side should I tilt my head to? Open lips, closed lips? And if you are really nervous you spend time practicing on inanimate objects: Your hand, your little sisters Raggedy Ann Doll, or heaven forbid . . . .The Mirror. All in the vain attempt to make your First Kiss one that will launch fireworks into the sky and cause the angels to break into a rousing chorus of Hallelujah. Unfortunately, the perfect first kiss only happens on take 37 of most movies, and the rest of us are left to suffer through The Blundered Buss by Patrick McManus.
```

### Performance text (classify this)

```text
Having pretty well exhausted my interest in quantum physics, which took the better part of three minutes, I recently turned to a much more fascinating subject for pondering: the firsts of my life, such as first kiss or first fish. Oddly, I haven't been able to extract my first fish from the mists of time, but memory of my first kiss leaped forth with agonizing clarity.

Perhaps what makes my first kiss so memorable is that it was conducted more as a scientific experiment than as an act of adolescent lust. I simply wanted to determine what kissing a girl felt like, nothing more. My interests at the time centered mostly on guns and hunting, and I tried to transfer my knowledge of shooting to the act of kissing, the similarity in these activities being that in each there is a target you're supposed to hit.

The situation was this. My cousin Buck showed up at my house to request a favor of me. Buck was several years older than I and possessed a driver's license along with, and more importantly, a car. He would on occasion interrupt the car's basic purpose as a vehicle for his amorous pursuits and use it to take me hunting and fishing. The car was his main hold on my loyalties, other than brute force. The reason he had singled me out for the favor was that someone-I didn't know who-had started a rumor that I was quite a ladies' man and that most of the girls in my freshman class at Delmore Blight High were absolutely crazy about me. The person who had contrived this mischief had even suggested that I was a great lover. He had even invented numerous fictional anecdotes in support of that reputation. I realized, of course, that the person who had started the rumor was probably a shy and insecure boy totally lacking in experience with the opposite sex, a lad not unlike myself. I could only sympathize with the rumormonger, and saw no reason to cause him embarrassment by denying the rumor, much as I would have liked to when I heard the favor Buck requested.

'Hey, lover boy," he greeted me. "Guess what you’re doing Saturday night."

"Going to a movie," I said. "A Randolph Scott Western. I can't miss it."

"Yeah, you can. Listen, I got a big favor I need to ask you. You know my new girl, Velveeta? Well, her cousin, who's about your age, maybe a little older, is coming to town, and Vel insists that she hang out with us. So I need you for the cousin. I figure I'll take 'em out for Cokes and burgers, and then I'll pick you up on the way out to the gravel pit."

No, not the gravel pit! For years I had lived in terror of one night finding myself lured to that infamous hole. The gravel pit was the local lovers' lane, or in this case, lovers' pit.

Hey, the gravel pit," I yelped. "You don't have to twist my arm to get me to go to the gravel pit!"

"That's better," Buck growled. "If you'd just said so first, I wouldn’t have had to twist it.

Thus it was that the following Saturday night I found myself on the opposite side of a back seat from a girl who looked like a movie star. She had blue eyes and tawny hair and an actual figure, and she was darting glances at me that sophisticated young women reserve only for freshly squashed worms on a wet sidewalk. The small part of my mind unparalyzed by terror deduced that this was going to be a long and harrowing evening at the old gravel pit. I made a mental note to mention to Buck the next day the anguish he had caused me. Then I'd kill him.

Scarcely had we arrived at the gravel pit than Buck and Velveeta began exchanging passionate kisses. I made a quick study of Buck's technique, never before having had the opportunity to observe passionate kisses at close range, so close in fact that the sounds emanating from the front seat reminded me of those made by toothless Old Man Crawford slurping up a bowl of noodles. Never before had I put Old Man Crawford and romance in the same thought, which says something about the stress of the evening. Although I appeared outwardly calm and casual, despite the loss of all feeling in my extremities, my mind had recovered from its paralysis and now ricocheted about the inside of my skull in wild panic. To rein it in, I started to pretend to myself that this girl was merely another quarry to stalk.

I would simply apply the same psychology I used to fend off buck fever, or in this case, doe fever. I was by no means totally opposed to kissing the girl, because I had long wondered what it would be like. It would be interesting to analyze the sensations, coldly and objectively, as a scientist would do with any experiment.

Despite my painful ignorance about all matters related to the opposite sex, I nevertheless realized that it would be uncouth of me to treat a girl as a mere science project. Before attempting to conduct the experiment, I thought I should first get to know something about her as a person, such as her name, for instance. My attempt at engaging her in preliminary casual conversation was not helped by the noodle-slurping sounds emanating from the front seat.

"By the way, what's your name?" I inched across the seat toward her, beginning my stalk. From the front seat: slurp smack slurp slurp smack.

"Opal."

"So, how about them Yankees, Opal? Won three in a row." Inch inch. Slurp smack slurp slurp smack.

"Yeah." Slurp smack ...

"Uh, hot lunches at our school are really terrible. I bet they are at yours, too. You like noodles?" Inch inch. Slurp smack

"Yeah."

As I drew within firing range of her moist scarlet pouting lips, Opal suddenly tilted back her head and closed her eyes. For a moment I thought she had dropped off to sleep, but then realized she had somehow divined my intent, and even approved of it, if only as a means of killing time. Cold sweat gushing from every pore, I took a deep breath and poised myself for the shot, finger tightening on the trigger, so to speak. Then I made a stupid error: I shut my eyes! Blindly I went for the target, only to discover too late that I had miscalculated the trajectory. My dry, puckered, quivering lips closed not on a soft, more or less receptive mouth but on a hard, unyielding protuberance. Startled by the unexpected sensation, I popped open my eyes to reorient myself and discovered I was kissing the bridge of Opal's nose! Cripes! Two wide and indignant blue eyes stared directly into mine from an inch away, rather disconcerting, I must say.

So back to witty conversation. Presently, Opal closed her eyes and tilted back her head once more. As I pondered whether to run the experiment again, with my eyes open, a tiny snore escaped her lips. I knew then that I had no great talent as a lover, or as a witty conversationalist either, for that matter, and in the future would concentrate only on stalking game possessed of either four legs or feathers. Still, a first kiss is a first kiss, even a blundered buss.
```

---

## IC-1984: Boarding: A Shakespearean Tragedy

- Title: Boarding: A Shakespearean Tragedy
- Author (byline): Renee Foss
- Work: Around the World in a Bad Mood!
- Publisher: Hatchette Books
- Publication date as stated: March 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: HEAD FLIGHT ATTENDANT, BOARDING AGENT, MACBETH, MACDUFF, FLIGHT ATTENDANT, HAMLET
- Teaser before the introduction: Yes
- Spoken words (computed): 935
- Already set (do not supply): none

### Source block (context only)

```text
Author: Renee Foss
Book: Around the World in a Bad Mood!
ISBN: 978-0786890118
Publisher: Hatchette Books
Date (Month/Year): March 2002
```

### Introduction (context only: never use it for content warnings)

```text
Boarding: A Shakespearean Tragedy by Renee Foss
```

### Performance text (classify this)

```text
These days it seems that people will almost kill for a first-class seat. I guess it’s because conditions are so deplorable in coach. One day I saw two grown adults get into a fight over the last seat in first class. Apparently the computer had made an error (hard to believe, I know) and there were twelve seats but thirteen passengers. Now, we’re one of the most civilized, technologically advanced nations in the world, but the behavior of these passengers took me back to the fifteenth century. There is only one word to describe it: “barbaric.”

It was a dark and stormy night. There was thunder, lightning, heavy rain, and a full moon. The three flight attendants prepared the galley and checked the meal count, and as they did so they began to chant: “Double, double toil and trouble Fire burn and caldron bubble.”

HEAD FLIGHT ATTENDANT: What does thou serve for those who sup in first class?

2ND FLIGHT ATTENDANT: Filet of rattlesnake in the caldron boil and back. Wool of bat wrapped in a leaf.

3RD FLIGHT ATTENDANT: In other words chicken or beef.

A lightning bolt flashed and heavy thunder rumbled.

BOARDING AGENT: A drum, a drum, the passengers doth come.

The first passenger, let us call him Macbeth, boarded.

MACBETH: (removing cape and hat) How now, you secret, black, and midnight hags! What is ‘t you do?

HEAD FLIGHT ATTENDANT: Hail Macbeth, hail to thee. Here is your seat, you have 1B. The last remaining in first class. Now give me you cape and your boarding pass.

As Mr. Macbeth got situated in his seat, he heard a strange eerie voice that whispered:

“Macbeth, Macbeth, Beware Macduff
Beware the Thane of Crete
Beware Macbeth, she wants your crown
Beware Macbeth, she wants your seat.”

It bothered him that no one else seemed to hear the voice, but he had been working hard and he was tired and things weren’t going so well with Lady Macbeth back at the castle. The stress was probably getting to him. Maybe he just needed to take it easy and relax he decided, but he would mention this to his doctor on his next visit. At that moment, the thirteenth passenger, Ms. Macduff, entered and the flight attendants assumed the position. In unison they chanted:

“Hail, Hail, Hail Macduff We see thy drown, we kiss thy feet.”

MACDUFF: Enough, enough. There is someone in my seat!”

FLIGHT ATTENDANT: May I see your boarding pass?

Ms. Macduff shoved it in her face and sure enough it was the same seat assignment.

FLIGHT ATTENDANT: Ah me, toil and trouble, boil and bubble, when seat assignments here are double!

Meanwhile, the passengers took matters into their own hands – which is always a dangerous thing.

MACDUFF: Pray, kind sir, but you’re in my throne, where I shall rest till dawn. Remove thyself and get thee gone.

MACBETH: (fastening his seat belt with no intention of leaving his seat) I’ll not move, I’ll not fail. Screw my courage to the sticking place, this is my seat and this is my space! (Macduff growls – Macbeth releases his seat belt, stands and brandishes a toenail clipper) Fie, Fie, I am a frequent flier. / I’ll not share this seat with / the likes of you, a common liar.

MACDUFF: (insulted, rummages in her purse for an eyelash curler which she brandishes) What care I how much you fly? / I am in the Regal Club and / Have a private room at every hub.

By now the two of them were standing in the aisle lunging and parrying about the cabin. The flight attendants hid in the galley and the other passengers took cover.

MACBETH: (jumping onto the seat) Ha! I won the stock, I am on the board / When I arrive, they call me Lord.

MACDUFF: Lord of what? Pray do tell. / Lord of this? Me thinks it hell.

You have to admit she had a valid point. However, Macbeth’s adrenaline was racing and he wasn’t about to give into this shrewish hellhound.

MACBETH: (Shouting) Nonetheless, that is my seat and it I shall defend. / You, poor wench, will ride in back with all the common men. (roars like a lion, then issues an evil laugh)

MACDUFF: (collapsing in despair) Ride in coach? I’d rather ride in a boat.

With that a full-fledged battle ensued. Passengers were taking cover, while the flight attendants continued trying to serve drinks. A beer meant for Macbeth fell off the tray onto Ms. Macduff’s brand new Anne Klein suit.

MACBETH: You wench, you fool / You’ve spilled my beer / I’ll write your boss and / Ruin your career.

FLIGHT ATTENDANT: (furiously scrubbing at the stain on Macduff’s suit, she sobs) Out, out damn spot . . .

HEAD FLIGHT ATTENDANT: A little bit of club soda will take that right out, honey.

With that they threw a can of club soda on Ms. Macduff. Before she could react, they hobbled back to the gallery. At that moment Ms. Macduff pulled a curling iron from her carry-on and thrust it into Macbeth’s soft belly.

MACDUFF: (with a chilling laugh) I’ve got you now, size doth not matter.

Macbeth fell from his first-class seat to the floor. And without missing a beat, Ms. Macduff sat down in seat 1B, for which she had battled valiantly and fairly won. Suddenly, just as she began to relax, Mr. Macbeth, in a surprising comeback, pulled out a golf club from under the seat in front of him and wacked Ms. Macduff in the head. He fell backward as Macduff fell forward on top of him.

HEAD FLIGHT ATTENDANT: (emerging from the gallery to begin the clean-up process) Dead, dead, me thinks them dead / Beer has been spilled, body fluid shed. / And yet here lies a seat that is free and / For this chance other beggars outside do / Wait, spewing forth and bitching at the gate. / So bring them in, the next of kin and seal the / Final fate.”

At that moment, during the trumpet fanfare, in sauntered a young man. Mr. Hamlet. He was very well dressed, but looked a bit pre-occupied with his own thoughts.

HAMLET: To be or not to be? That is the question, whether ‘tis . . .

HEAD FLIGHT ATTENDANT: No, no no! Excuse me, Mr. Hamlet? Not 2B . . . 1B . . . right over here.
```

---

## IC-1985: The Book Thief

- Title: The Book Thief
- Author (byline): Markus Zusak
- Work: Not specified
- Publisher: Knopf Books for Young Readers
- Publication date as stated: Sept 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: DEATH, RED
- Teaser before the introduction: Yes
- Spoken words (computed): 1204
- Already set (do not supply): none

### Source block (context only)

```text
Author: Markus Zusak
ISBN: 978-0375842207
Publisher: Knopf Books for Young Readers
Date (Month/Year): Sept 2007
```

### Introduction (context only: never use it for content warnings)

```text
U Krakovianki once stated, “Death is constantly interrupting us – and then the story moves on. The interruptions do not stop the story – it goes on. Some people are no longer a part of the story, but it goes on just the same until death interrupts again: a pattern as old as the world.”

Death is inevitable. We hear about it, witness it, and fearfully wait for it. And though we see it as the enemy, it’s a natural part of life. In this selection, by humanizing death and putting a name and face to the “enemy,” we are shown that nothing is purely black and white. Death personified is just as affected as we are by occurrences that take place in the novel, The Book Thief by Markus Zusak.
```

### Performance text (classify this)

```text
DEATH: (Pg 3) ***HERE IS A SMALL FACT*** You are going to die.

Does this worry you?
I urge you – don’t be afraid.
I’m nothing if not fair.
I am in all truthfulness attempting to be cheerful
about this whole topic, though most people find
themselves hindered in believing me. Please, trust me. I
most definitely can be cheerful. I can be amiable.
Agreeable. Affable. And that’s only the A’s. Just don’t ask
me to be nice. Nice has nothing to do with me.

DEATH: (Pg 4-5) I could introduce myself properly, but it’s not really necessary. You will know me well enough and soon enough, depending on a diverse range of variables. At some point in time, I will be standing over you. Your soul will be in my arms. A color will be perched on my shoulder [and[ I will carry you gently away. The question is, what color will everything be at the moment when I come for you? What will the sky be saying? I try to enjoy every color I see – the whole spectrum. A billion or so flavors, none of them quite the same. My one saving grace is distraction. It helps me cope, considering the length of time I’ve been performing this job. The trouble is, who could ever replace me? The answer, of course, is nobody, which has prompted me to make a conscious, deliberate decision – to make distraction my vacation. Needless to say, I vacation in increments. In colors. (Pg 6) First up is something white. Of the blinding kind. Some of you are most likely thinking that white is not really a color. Well, I’m here to tell you that it is. White is, without question a color, and personally, I don’t think you want to argue with me. Please, be calm, despite that previous threat. I am all bluster – I am not violent. I am not malicious. I am a result. (Pg 9) Next is a signature black, to show the poles of my versatility, if you like. It is the darkest moment before the dawn. Sometimes I arrive too early. I rush, and some people cling longer to life than expected. (Pg 11) For just a moment, despite all of the colors that touch and grapple with what I see in this world, I will often catch an eclipse when a human dies.

I’ve seen millions of them. I’ve seen more eclipses than I care to remember. (Pg 12) The last [color is] red. (Pg 14) When I recollect, I see a long list of colors, but it’s these three that resonate the most. Sometimes I manage to float far above those [colors]. I hang suspended, until a septic truth bleeds toward clarity. That’s when I see them formulate. ***THE COLORS***

RED: WHITE: BLACK.
They fall on top of each other. The scribbled
signature black, onto the blinding global white, onto the
thick soupy red.
(Pg 174-175) I’ve seen so many young men
Over the years who think they’re
Running at other young men.
They are not.
They’re running at me.

(Pg 307-309) I do not carry a sickle or scythe. I only wear a hooded black robe when it’s cold. And I don’t have those skull-like facial features you seem to enjoy pinning on me from a distance. My travels, what I saw in ’42. There’s a reason for me explaining what I saw in that time. There were certainly some rounds to be made that year, from Poland to Russia to Africa and back again. You might argue that I make the rounds no matter what year it is, but sometimes the human race likes to crank things up a little. They increase the production of bodies and their escaping souls. A few bombs usually do the trick. Or some gas chambers, or the chitchat of faraway guns. So many humans. So many colors. And then. There is death. Making [my] way through all of it. On the surface: unflappable, unwavering. Below: unnerved, untied, and undone. In all honesty, I was still getting over Stalin, in Russia. The so-called second revolution – the murder of his own people. Then came Hitler.

They say that war is death’s best friend, but I must offer you a different point of view on that one. To me, war is like the new boss who expects the impossible. He stands over your shoulder repeating one thing, incessantly: “Get it done, get it done.” So you work harder. You get the job done. The boss, however, does not thank you. He asks for more. (Pg 349) I’ll never forget the first day in Auschwitz, the first time in Mauthausen. I picked them up from the bottom of the great cliff, when their escapes fell awfully awry. There were broken bodies and dead, sweet hearts. Still it was better than the gas. Some of them I caught when they were only halfway down. Saved you, I’d think, holding their souls in midair as the rest of their being – their physical shells – plummeted to the earth. All of them were light, like the cases of empty walnuts. (Pg 336) I carried them in my fingers, like suitcases. Or I’d throw them over my shoulder. It was only the children I carried in my arms. (Pg 350) I shiver when I remember – as I try to de-realize it. I blow warm air into my hands, to heat them up.

But it’s hard to keep them warm when the souls still shiver. God. I always say that name when I think of it. God. Twice, I speak it. I say His name in a futile attempt to understand. “But it’s not your job to understand.” That’s me who answers. God never says anything. You think you’re the only one he never answers? “Your job is to…” And I stop listening to me, because I tire me. When I start thinking like that, I become so exhausted, [but] I’m compelled to continue on, because although it’s not true for every person on earth, it’s true for the vast majority – that death waits for no man – and if he does, he doesn’t usually wait very long. Please believe me when I tell you that I picked up each soul as if it were newly born. I even kissed a few weary, poisoned cheeks. I listened to their last, gasping cries. Their vanishing words. I watched their love visions and freed them from their fear.

They were French, they were Jews, and they were you. (Pg 503) So many people chased after me in that time, calling my name, asking me to take them with me. (Pg 543) It has been many years since all of that, but there is still plenty of work to do. I can promise you that the world is a factory. The sun stirs it, the humans rule it. And I remain. I carry them away. (Pg 549) Yes, I have seen a great many things in this world. I attend the greatest disasters and work for the greatest villains. But then there are other moments. There’s a multitude of stories that I allow to distract me as I work, just as the colors do. I pick them up in the unluckiest, unlikeliest places and I make sure to remember them as I go about my work. (Pg 550) ***A LAST NOTE FROM YOUR NARRATOR*** I am haunted by humans.
```

---

## IC-1986: Born of Man and Woman

- Title: Born of Man and Woman
- Author (byline): Richard Matheson
- Work: The Dark Descent
- Publisher: Doubleday
- Publication date as stated: Jan 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1228
- Already set (do not supply): none

### Source block (context only)

```text
Author: Richard Matheson
ISBN: 978-0312862176
Book: The Dark Descent
Publisher: Doubleday
Date (Month/Year): Jan 1997
```

### Introduction (context only: never use it for content warnings)

```text
In the 19th and early 20th centuries the disabled were exploited as a source of entertainment. Freak shows of people with physical or mental abnormalities could be seen at circuses, fairs and carnivals as late as the 1970s. However, the fate of disabled children born before this time was even more horrific. Often they were locked away from society in cages or basements and viewed as little more than animals.

Richard Matheson turns this historic disgrace on its head in his short story Born of Man and Woman. We view a family through the eyes of a young, disabled child . . . .

Is it a child? . . . Or a monster? Born of Man and Woman by Richard Matheson.
```

### Performance text (classify this)

```text
X — This day when it had light mother called me retch. You retch she said. I saw in her eyes the anger. I wonder what it is a retch.

X — This day it had water falling from upstairs. It fell all around. I saw that. The ground of the back I watched from the little window. The ground it sucked up the water like thirsty lips. It drank too much and it got sick and runny brown. I didn’t like it.

Mother is a pretty I know. In my bed place with cold walls around I have a paper things that was behind the furnace. It says on it SCREENSTARS. I see in the pictures faces like of mother and father. Father says they are pretty. Once he said it.

And also mother he said. Mother so pretty and me decent enough. Look at you he said and didnt have the nice face. I touched his arm and said it is alright father. He shook and pulled away where I couldn’t reach.

Today mother let me off the chain a little so I could look out the little window. That’s how l saw the water falling from upstairs.

XX — This day it had goldness in the upstairs. As I know when I looked at it my eyes hurt. After I look at it the cellar is red.

I think this was church. They leave the upstairs. The big machine swallows them and rolls out past and is gone. In the back part is the little mother. She is much small than me. lam I can see out the little window all I like.

In this day when it got dark I had eat my food and some bugs. I hear laughs upstairs. I like to know why there are laughs for. I took the chain from the wall and wrapped it around me. I walked squish to the stairs.

They creak when I walk on them. My legs slip on them because I dont walk on stairs. My feet stick to the wood.

I went up and opened a door. It was a white place. White as white jewels that come from upstairs sometime.

I went in and stood quiet. I hear the laughing some more. I walk to the sound and look through to the people.

More people than I thought was. I thought I should laugh with them.

Mother came out and pushed the door in. It hit me and hurt. I fell back on the smooth floor and chain made noise. I cried. She made a hissing noise into her and put her hand on her mouth. Her eyes got big.

She looked at me. I heard father call. What fell he called. She said a iron board. Come help pick it up she said. He came and said now is that so heavy you need. He saw me and grew big. The anger came in his eyes. He hit me. I spilled some of the drip on the floor from one arm. It was not nice. It made ugly green on the floor.

Father told me to go to the cellar. I had to go. The light it hurt some now in my eyes. It is not so like that in the cellar.

Father tied my legs and arms up. He put me on my bed. Upstairs I heard laughing while I was quiet there looking on a black spider that was swinging down to me. I thought what father said. Oh god he said. And only eight.

XXX — This day father hit in the chain again before it had light. I have to try pull it out again. He said I was bad to come upstairs. He said never do that again or he would beat me hard. That hurts.

I hurt. I slept the day and rested my head against the cold wall. I thought of the white place upstairs.

XXXX — I got the chain from the wall out. Mother was upstairs. I heard little laughs very high. I looked out the window. I saw all little people like the little mother and little fathers too. They are pretty.

They were making nice noise and jumping around the ground. Their legs was moving hard. They are like mother and father. Mother says all right people look like they do.

One of the little fathers saw me. He pointed at the window. I let go and slid down the wall in the dark. I curled up as they would not see. I heard their talks by the window and foots running. Upstairs there was a door hitting. I heard the little mother call upstairs. I heard heavy steps and I rushed in my bed place. I hit the chain in the wall and lay down on my front.

I heard my mother come down. Have you been at the window she said. I heard the anger. Stay away from the window. You have pulled the chain out again.

She took the stick and hit me with it. I didnt cry. I cant do that. But the drip ran all over the bed. She saw it and twisted away and made a noise. Oh mygodmygod she said why have you done this to me? I beard the stick go bounce on the stone floor. She ran upstairs. I slept the day.

XXXXX — This day it had water again. When mother was upstairs I heard the little one come slow down the steps. I hidded myself in the coal bin for mother would have anger if the little mother saw me.

She had a little live thing with her. It walked on the arms and had pointy ears. She said things to it.

It was all right except the live thing smelled me. It ran up the coal and looked down at me. The hairs stood up. In the throat it made an angry noise. I hissed but it jumped on me.

I didnt want to hurt it. I got fear because it bit me harder than the rat does. I hurt and the little mother screamed. I grabbed the live thing tight. It made sounds I never heard. I pushed it all together. It was all lumpy and red on the black coal.

I hid there when mother called. I was afraid of the stick. She left. I crept over the coal with the thing. I hid it under my pillow and rested on it. I put the chain in the wall again.

**********

X — This is another times. Father chained me tight. I hurt because he beat me. This time I hit the stick out of his hands and made noise. He went away and his lace was white. He ran out of my bed place and locked the door.

I am not so glad. All day it is cold in here. The chain comes slow out of the wall. And I have a bad anger with mother and father. I will show them. I will do what I did that once.

I will screech and laugh loud. I will run on the walls. Last I will hang head down by all my legs and laugh and drip green all over until they are sorry they didn't be nice to me.

If they try to beat me again Ill hurt them. I will.

X —
```

---

## IC-1987: Boy Lost and Wendy

- Title: Boy Lost and Wendy
- Author (byline): Nakita Gill
- Work: Fierce Fairy Tales
- Publisher: Hachette Books
- Publication date as stated: Hachette Books
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1013
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nakita Gill
Book: Fierce Fairy Tales
ISBN: 978-0316420747
Publisher: Hachette Books
Date (Month/Year): Hachette Books
```

### Introduction (context only: never use it for content warnings)

```text
Based on J.M. Barrie’s play and novel of the same name, Disney’s animated musical follows a girl and her brothers who are swept into the magical world of Neverland by a boy named Peter Pan.

And, of course, you’ve heard of Captain Hook, Pan’s dreaded enemy. Ferocious and terrible, he terrorizes Peter and his merry band of boys. But exactly how did Captain Hook become Peter’s greatest enemy? And whatever became of Wendy Darling? Nakita Gill in her short prose selections Boy Lost and Wendy provides some possible answers.
```

### Performance text (classify this)

```text
BOY LOST

(Pg 20-24) Picture a sunset in a small port town by the sea. Two teenaged boys sitting on the docks watching the ships as they fly across the water. One reaches out and takes the other's hand. In this brush of skin for skin, a thousand unspoken promises erupt between them, and both are determined to keep them. This is what youth is. The sheer belief that you will be able to keep every promise you made to someone else. That you will be able to love someone into a forever when you do not even understand what forever means.

An evening spent in the headiness of love, they go back to their respective homes. One boy helps his mother with cooking and cleaning and looking after his little sister. His father is a good man, a sailor who brings home with him meagre wages, but a heart full of love and a quicksilver tongue that tells stories of faraway lands to enthral them all. But this boy, despite his blessings, is not happy. He may have been blessed with a loving family, but that faraway look is made of unrest and wanderlust, something about him says fae, changeling, wearing the skin of a boy who was always destined to fly, to leave.

The other boy returns home to a father who drinks and a mother who works so hard that she is never there. He is the unwanted creature in this home, a beating waiting for him at every corner. His father's temper is a beast so powerful that a boy made of paper bones barely held together cannot fight him. He hides in his room. He lives for a boy at sunset, hope made into a human being.

Now picture this. This boy of paper bones alone at the docks the next sunset. And this boy alone on the docks again on a rainy day. And this boy alone on the docks every day after, waiting for someone who promised him forevers he never

intended to keep. This boy becoming a man, a heart wounded so young in youth that it never quite healed right. Imagine him becoming a sailor, searching land after land for a boy he once loved, thinking he was hurt, or stolen, just needing to know what happened to him.

Now see him finally finding out that the boy he loved in his boyhood ran away to a magical land where he never grew up. That without a second glance, he just forgot every promise of forever. Imagine his rage, that ancient pain turning to a terrible anger and escaping from the forgotten attic of his mangled heart. Think of what happens when immense love turns into immense hate. An anger so intense it cannot be controlled. What he would give up to avenge the boy he once was, paper-boned, standing on the docks, broken without a single person to love him, simply all alone. A hand is a small price to pay for a magical ship that will take him to Neverland, a place that lives on a star. Becoming a villain called Captain Hook is a small exchange to show Peter Pan that you cannot throw away love and think you will get away unscarred. ******* WENDY

[And what ever happened to Wendy?] No one talks about what happened to Wendy Darling after they returned from Neverland. No one speaks of Wendy Darling anymore. The truth is, whilst her parents were able to convince her brothers that Neverland never happened, that all children must grow up, that it was all just a dream, Wendy knew better and she vehemently believed.

She believed when her friends made fun of her in boarding school. She wished for the fairies to save her when she went to the headteacher's office and her parents were forced to remove her. She even spoke to Peter after that when she was homeschooled by her governess. As she grew older, the visions of Neverland never quite ceased and she painted and drew pictures showing her wonderful adventures with Peter and the Lost Boys. She didn't realise her parents were slowly growing concerned and wrung their hands about how she would ever find a man to marry, if she still believed in all this nonsense.

Things came to a head when Wendy refused to marry. Soon they grew so worried that they had Wendy placed in an asylum, claiming her hallucinations were so terrible that they needed tending. You would think the story would end there, but Wendy had a powerful faith in herself and in the strength of her own mind and memory.

So from the asylum she began to write stories and paint pictures of Neverland for children, impressing every doctor, soothing the patients to the point that her doctor, a kind-hearted man, began to send her work to publishers. Wendy, slowly but surely, became so adamant and so polite to her doctors that they began to question their own sanity, because she remained so unfalteringly faithful to her story. However, if she had no means of supporting herself, she would never be able to leave

this asylum, and knowing this was going to be her fate, Wendy once again wished upon the fairies.

They had never paid her any mind before, but her fervour made them pay attention. Because they guided her to send her writings and paintings to a publisher who absolutely loved what she was doing. They offered her enough money to leave the asylum, which she could when she turned 21, and support herself; something almost unheard of in their circle of society.

Wendy died a happy old maid, with a dozen books she had written, a stunning library, and a host of friends and nephews and nieces that absolutely loved and thought the world of her.

But this is the reason why no one talks of Wendy Darling anymore. Because the most successful children's books of her time, the adventures in Neverland, were never published under the name of Wendy Darling, but simply under 'Wendy'.
```

---

## IC-1988: Brer Rabbit meets a Tar Baby

- Title: Brer Rabbit meets a Tar Baby
- Author (byline): Joel Chandler Harris
- Work: Classic Tales of Brer Rabbit
- Publisher: Running Press Book Publishers
- Publication date as stated: Feb 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1093
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joel Chandler Harris
Book: Classic Tales of Brer Rabbit
ISBN: 978-0762417124
Publisher: Running Press Book Publishers
Date (Month/Year): Feb 2004
```

### Introduction (context only: never use it for content warnings)

```text
Many have suggested Br'er Rabbit, represents the Black slave who uses his wits to overcome circumstances and to enact revenge on Br’er Fox, representing the White slave-owners. Most children however would tell you, Br’er Rabbit is just an extremely entertain story. But regardless of your age or mentality, the story of Brer Rabbit meets the Tar Baby is an Uncle Remus story not to be forgotten. The Tar Baby by Joel Chandler Harris.
```

### Performance text (classify this)

```text
One day Brer Fox thought of how Brer Rabbit had been cutting up his capers and bouncing around until he'd come to believe that he was the boss of the whole gang. Brer Fox thought of a way to lay some bait for that uppity Brer Rabbit.

He went to work and got some tar and mixed it with some turpentine. He fixed up a contraption that he called a Tar-Baby.

When Brer Fox finished making the Tar Baby, he put a straw hat on her head and sat the little thing in the middle of the road. Brer Fox, he lay off in the bushes to see what would happen.

Well, Brer Fox didn't have to wait long either, 'cause by and by Brer Rabbit came pacing down the road--lippity-clippity, clippity-lippity--just as sassy as a jaybird. Brer Fox, he lay low. Brer Rabbit came prancing along until he saw the Tar-Baby and then he sat back on his hind legs like he was astonished. The Tar-Baby just sat there, she did, and Brer Fox, he lay low.

"Good morning!" says Brer Rabbit, says he. "Nice weather we're having this morning," says he.

Tar-Baby didn't say a word, and Brer Fox, he lay low.

"How are you feeling this morning?" says Brer Rabbit, says he.

Brer Fox, he winked his eye real slow and lay low and the Tar-Baby didn't say a thing.

"What is the matter with you then? Are you deaf?" says Brer Rabbit, says he. "Cause if you are, I can holler louder," says he.

The Tar-Baby stayed still and Brer Fox, he lay low. "You're stuck-up, that's what's wrong with you. You think you're too good to talk to me," says Brer Rabbit, says he. "And I'm going to cure you, that's what I'm going to do," says he.

Brer Fox started to chuckle in his stomach, he did, but Tar-Baby didn't say a word.

"I'm going to teach you how to talk to respectable folks if it's my last act," says Brer Rabbit, says he. "If you don't take off that hat and say howdy, I'm going to bust you wide open," says he.

Tar-Baby stayed still and Brer Fox, he lay low.

Brer Rabbit kept on asking her why she wouldn't talk and the Tar-Baby kept on saying nothing until Brer Rabbit finally drew back his fist, he did, and blip--he hit the Tar-Baby on the jaw. But his fist stuck and he couldn't pull it loose. The tar held him. But Tar-Baby, she stayed still, and Brer Fox, he lay low.

"If you don't let me loose, I'm going to hit you again," says Brer Rabbit, says he, and with that he drew back his other fist and blap--he hit the Tar-Baby with the other hand and that one stuck fast too.

Tar-Baby she stayed still, and Brer Fox, he lay low.

"Turn me loose, before I kick the natural stuffing out of you," says Brer Rabbit, says he, but the Tar-Baby just sat there.

She just held on and then Brer Rabbit jumped her with both his feet. Brer Fox, he lay low. Then Brer Rabbit yelled out that if that Tar-Baby didn't turn him loose, he was going to butt her crank-sided. Then he butted her and his head got stuck.

Brer Box walked out from behind the bushes and strolled over to Brer Rabbit, looking as innocent as a mockingbird.

"Howdy, Brer Rabbit," says Brer Fox, says he. "You look sort of stuck up this morning," says he. And he rolled on the ground and laughed and laughed until he couldn't laugh anymore.

By and by he said, "Well, I expect I got you this time, Brer Rabbit," says he. "Maybe I don't, but I expect I do. You've been around here sassing after me a mighty long time, but now it's the end.

And then you're always getting into something that's none of your business," says Brer Fox, says he. "Who asked you to come and strike up a conversation with this Tar-Baby? And who stuck you up the way you are? Nobody in the round world. You just jammed yourself into that Tar-Baby without waiting for an invitation," says Brer Fox, says he. "There you are and there you'll stay until I fix up a brushpile and fire it up, "cause I'm going to barbecue you today, for sure," says Brer Fox, says he.

Then Brer Rabbit started talking mighty humble. "I don't care what you do with me, Brer Fox, says he, "Just so you don't fling me in that briar patch. Roast me, Brer Fox, says he, "But don't fling me in that briar patch."

"It's so much trouble to kindle a fire," says Brer Fox, says he, "that I expect I'd better hang you," says he.

"Hang me just as high as you please, Brer Fox, says Brer Rabbit, says he, "but for the Lord's sake, don't fling me in that briar patch," says he.

"I don't have any string, " says Brer Fox, says he, "Now I expect I had better drown you, " says he.

"Drown me just as deep as you please, Brer Fox," says Brer Rabbit, says he, "But please do not fling me in that briar patch, " says he.

"There's no water near here," says Brer Fox, says he, "And now I reckon I'd better skin you," says he.

"Skin me Brer Fox," says he. "Snatch out my eyeballs, tear out my ears by the roots," says he, "But please, Brer Fox, don't fling me in that briar patch, " says he.

Of course, Brer Fox wanted to get Brer Rabbit as bad as he could, so he caught him by the behind legs and slung him right in the middle of the briar patch. There was a considerable flutter when Brer Rabbit struck the bushes, and Brer Fox hung around to see what was going to happen.

By and by he heard someone call his name and 'way up on the hill he saw Brer Rabbit sitting cross-legged on a chinquapin log combing the tar pitch out of his hair with a chip. Then Brer Fox knew he had been tricked. Brer Rabbit hollered out, "Born and bred in the briar patch. I was born and bred in the briar patch!" And with that he skipped out just as lively as a cricket in the embers of a fire.
```

---

## IC-1989: Bridge to Terabithia (The Book)

- Title: Bridge to Terabithia (The Book)
- Author (byline): Katherine Paterson
- Work: Not specified
- Publisher: Harper Trophy
- Publication date as stated: June 1987
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: JESSE, NARRATOR, LESLIE, TOGETHER, MAY BELLE, JESSE’S FATHER, LESLIE’S FATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1735
- Already set (do not supply): none

### Source block (context only)

```text
Author: Katherine Paterson
ISBN: 978-0064401845
Publisher: Harper Trophy
Date (Month/Year): June 1987
```

### Introduction (context only: never use it for content warnings)

```text
Jesse Aaron's greatest ambition is to be the fastest runner in the fifth grade. But on the first day of school, a new kid, a girl, boldly crosses over to the boy's side of the playground and outruns everyone. That's not a very promising beginning for a friendship, but Jesse Aarons and Leslie Burke become inseparable. It doesn't matter to Jesse that Leslie dresses funny, or that her family has a lot of money -- but no TV. Leslie has imagination and she is fearless! For Jesse, who is afraid of everything. . . Leslie is everything he wants to be.

Together, they create Terabithia, a magical kingdom in the woods where they reign and the only limits are their imaginations.

Bridge to Terabithia by Katherine Paterson
```

### Performance text (classify this)

```text
JESSE: (Pg 2) I get up early every day to run. I figure if I work at it, I could be the fastest runner in the fifth grade when school opens up. I have to be the fastest. . . not one of the fastest or next to the fastest, but the fastest. The very best. (Pg 20) Watch out Wayne Pettis. . . I’ll get you. You can’t beat me.

NARRATOR: (Pg 5) Wayne Pettis would be in the sixth grade with the rest of the big guys. [But] anybody had a chance to be the fastest runner, and by Miss Bessie, this year it was going to be Jesse Oliver Aarons, Jr.!

LESLIE: (Pg 49-50) Do you know what we need? We need a place. . . just for us. It might be a whole secret country and you and I would be the rulers of it.

JESSE: Ok. . . Where would we have it?

LESLIE: Over there in the woods where nobody would come and mess it up. (getting excited) I know. . . it could be a magic country like Narnia, and the only way you can get in is by swinging across on this enchanted rope. Come on. . . let’s find a place to build our castle stronghold. . . (searching) How about right here?

JESSE: (Pg 51) (nodding vigorously and catching Leslie’s excitement) Sure! This will be a good place to build. . .

NARRATOR: Leslie named their secret land “Terabithia,” and she loaned Jess all of her books about Narnia, so he would know how things went in a magic kingdom.

LESLIE: (Pg 52) You should draw a picture of Terabithia for us to hang in the castle.

JESSE: (gazing in wonder at their surroundings) I can’t . . . I just can’t get the poetry of the trees.

LESLIE: Don’t worry. You will someday!

NARRATOR: He believed her because, there in the shadowy light of the stronghold, everything seemed possible. They owned the world and no enemy could ever defeat them.

JESSE: (Pg 60) I used to think this place was haunted.

LESLIE: Oh, it is. But you don't have to be scared. It's not haunted with evil things.

JESSE: How do you know?

LESLIE: You can just feel it. Listen. (they close their eyes, then Leslie continues solemnly) This is not an ordinary place. Even the rulers of Terabithia come into it only at times of greatest sorrow or of greatest joy. We must strive to keep it sacred. It would not do to disturb the Spirits. *****Scene change *****

LESLIE: (Pg 103) I’ve never been to a church before . . . do you think your parents would let me go with you?

JESSE: You’d hate it. It’s boring (then skeptically) You can’t wear pants

LESLIE: (indignantly) I’ve got some dresses, Jess Aarons!

TOGETHER: (holding a hymn book; they sing a few lines – pick your favorite hymn (Jesse is bored; Leslie is enthralled)

LESLIE: (Pg 107-109) (after church) I’m really glad I came.

(Jess looks at Leslie in unbelief) It was better than a movie!

JESSE: You’re kidding.

LESLIE: No, I’m not. That whole Jesus thing is really interesting isn’t it? All those people wanting to kill him when he hadn’t done anything to hurt them. It’s really kind of a beautiful story – like Aslan.

MAY BELLE: It ain’t beautiful. It’s scary, nailing holes right through somebody’s hand.

JESSE: May Belle’s right. It’s because we’re all vile sinners God made Jesus die.

LESLIE: Do you think that’s true?

JESSE: It’s in the Bible, Leslie.

LESLIE: (looks like she’s going to argue, then shakes her head) It’s crazy isn’t it? You have to believe it, but you hate it. I don’t have to believe it and I think it’s beautiful.

MAY BELLE: You gotta believe the Bible, Leslie.

LESLIE: (a genuine question) Why?

MAY BELLE: (eyes huge) ‘Cause if you don’t believe the Bible, God’ll damn you to hell when you die.

LESLIE: I don’t believe it. (turns to Jesse) I don’t even think you’ve read the Bible.

JESSE: I’ve read most of it. (grinning) S’bout the only book we got around our place.

LESLIE: OK, but I still don’t think God goes around damning people to hell.

MAY BELLE: But Leslie. . . What if you die? What’s going to happen to you? *****Scene change *****

NARRATOR: (Pg 110) On Easter Monday, the rain began in earnest. (Pg 112) When they got to the bank of the creek, they stopped. It was an awesome sight. Like in The Ten Commandments on TV when the water came rushing into the dry path Moses had made and swept all the Egyptians away . . . The creek was a roaring eight-foot-wide sea, sweeping before it great branches and logs swirling them about like Egyptian chariots, the hungry waters sometimes leaping the banks, daring them to try to confine it. (Pg 115-118) For Jess the fear of crossing rose with the height of the creek [but] Leslie never seemed to hesitate.

LESLIE: (playing the role of Queen of Terabithia) Dost know what is in my mind, O King? Methinks some evil being has put a curse on our beloved kingdom.

JESSE: Damn weather bureau.

LESLIE: (not wanting to kid) Let us go into the sacred grove and inquire of the Spirits what this evil might be and how we must combat it. For I perceive that this is no ordinary rain that is falling upon our kingdom. (lifting her arms and face toward the green canopy above) O, Spirits of the grove, we come on behalf of our beloved kingdom which lies even now under the spell of some evil, unknown force. Give us, we beseech thee, wisdom to discern this evil, and power to overcome it.

JESSE: (also raising his arms) Um. Uh. Um. Yes. Please listen, thou Spirits. *****Scene change *****

NARRATOR: (Pg 119) It had seemed to Jess when he went to bed Wednesday night that he could relax, that everything was going to be all right, but he awoke in the middle of the night with the horrible realization that it was still raining. He would have to tell Leslie that he wouldn't go to Terabithia. He was obviously not worthy to be king of Terabithia. It wasn’t so much that he minded telling Leslie that he was afraid to go; it was that he minded being afraid. (Pg 118) He was obviously not worthy to be king of Terabithia. Whoever heard of a king who was scared of tall trees and a little bit of water?

JESSE: (to himself) All I gotta do is say, “Leslie, I don’t wanta go over there today.” Just like that. Easy as Pie.

NARRATOR: (Pg 119) He hardly slept the rest of the night, listening to the horrid rain and knowing that no matter how high the creek came, Leslie would still want to cross it. *****Scene change *****

NARRATOR: (Pg 130) He was all the way into the kitchen before he realized something was wrong.

JESSE’S FATHER: (Pg 131-132) (quietly) I’m real sorry, boy. They found the Burke girl this morning down in the creek.

JESSE: No. Leslie wouldn’t drown. She could swim real good.

JESSE’S FATHER: That old rope you kids been swinging on broke.

JESSE: (shaking his head) No. No! I don’t believe you. You’re lying to me!

MAY BELLE: (echoing) But, Leslie, what if you die?

JESSE: (looking about wildly) No. It’s a lie. Leslie ain’t dead.

JESSE’S FATHER: They think she musta hit her head on something when she fell. I’m really sorry, son. (Jesse begins to cry) (Pg 139) Your mother and I thought we ought to go down to the neighbors and pay respects. (clears his throat) I think it would be fitting for you to come, too. Seeing's you was the one that really knowed the little girl.

JESSE: (talks to Leslie in his mind) You know something weird?

LESLIE: What?

JESSE: I was scared to come to Terabithia this morning.

(angrily) You think it's so great to die and make everyone cry and carry on. Well, it ain't. *****

NARRATOR: (Pg 144-146) He heard his father ask quietly over his head about “the service.”

LESLIE’S FATHER: [We] decided to have the body cremated and are going to take the ashes to the family home in Pennsylvania tomorrow.

NARRATOR: Cremated. Something clicked inside Jess's head. That meant Leslie was gone. Turned to ashes. He would never see her again. Not even dead. Never. How could they dare? Leslie belonged to him. More to him than anyone in the world. No one had even asked him.

JESSE: (anguished, to the audience) I was the only one who really cared for Leslie. But she went and died just when I needed her the most. She went and left me. She went swinging on that rope just to show me that she was no coward.

LESLIE: (laughing) So there, Jess Aarons!

JESSE: (sadly) She tricked me. She made me leave my old self behind and come into her world, and then before I was really at home in it but too late to go back, she left me stranded there -- like an astronaut wandering about the moon. Alone.

NARRATOR: He was never sure just when he left, but he remembered running up the hill to his own house with angry tears streaming down his face. He raced into his bedroom and retrieved the papers and paint that Leslie had given him at Christmastime. He ran out the kitchen door and down to the stream without looking back. Above the crab apple tree, the frayed end of the rope swung gently.

LESLIE: (Pg 60) (echoing) Even the rulers of Terabithia come only at times of greatest sorrow or of greatest joy.

JESSE: (Pg 146-147) (screaming something without words, he flings the papers and paints into the water)

NARRATOR: There was nowhere to go. Nowhere. Ever again.

JESSE’S FATHER: (who had followed Jesse) That was a damn fool thing to do.

JESSE: (crying hard, barely able to breathe) I don’t care! I don’t care! I hate her. I wish I’d never seen her in my whole life.

JESSE’S FATHER: (pulling him close, comforting) There. There. Sssh. . . Hell ain’t it?

JESSE: Do you believe people go to hell, really go to hell, I mean?

JESSE’S FATHER: Lord, boy, don’t be a fool. God ain’t gonna send any little girls to hell.

JESSE: (softly) She wouldn't have been eleven until November. . . *****The next day *****

NARRATOR: (Pg 150) He woke up Saturday morning with a dull headache. (Pg 160) Before Leslie came, he had been a nothing – a stupid, weird little kid trying to act big – trying to hide a whole mob of foolish little fears. It was Leslie who had taken him into Terabithia and turned him into a king. [He felt called to Terabithia] (Pg 151-152) If was still Terabithia . . .

The castle stronghold was dark and damp, but there was no evidence there to suggest that the queen had died. He felt the need to do something fitting. But Leslie was not there to tell him what it was. The anger which had possessed him yesterday flared up again.

JESSE: Leslie, I’m just a dumb dodo and you know it. What am I supposed to do? (his voice catches) Leslie, were you scared? Did you know you were dying? Were you scared like me?

NARRATOR: A picture of Leslie being sucked into the cold water flashed across his brain. (Pg 160-161) She wasn’t there. . . It was up to him to pay back the world in beauty and caring what Leslie had loaned him.

JESSE: (takes a deep breath) Well, you just have to stand up to your fear and not let it squeeze you white. Right, Leslie?

LESLIE: Right.

JESSE: (Pg 152-153) (a sudden idea) A funeral wreath for the queen…

NARRATOR: He sat in the clear space between the bank and the first line of trees and bent a pine bough into a circle, tying it with a piece of wet string from the castle. He picked spring beauties from the forest floor and wove them among the needles.

JESSE: (reverently he kneels and offers up the wreath to the Spirts) Father, into Thy hands I commend her spirit.

NARRATOR: Leslie would have liked those words. They had the ring of the sacred grove - - the grove in Terabithia.
```

---

## IC-1990: The Bridge’s Complaint

- Title: The Bridge’s Complaint
- Author (byline): Jane Yolen
- Work: Twelve Impossible Things Before Breakfast
- Publisher: Houghton Mifflin Harcourt
- Publication date as stated: 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1767
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jane Yolen
Book: Twelve Impossible Things Before Breakfast
ISBN: 978-0152164447
Publisher: Houghton Mifflin Harcourt
Date (Month/Year): 2001
```

### Introduction (context only: never use it for content warnings)

```text
Once upon a time there were three Billy Goats called Gruff. In the winter they lived in a barn in the valley. When spring came they longed to travel up to the mountains to eat the lush, sweet grass. On their way to the mountains the three Billy Goats Gruff had to cross a rushing river. But there was only one bridge across it, made of wooden planks. And underneath there lived a terrible, ugly, one-eyed troll. Nobody was allowed to cross the bridge without the troll’s permission and nobody ever got permission. He always ate them up. . . . In The Bridge’s Complaint by Jane Yolen . . .
```

### Performance text (classify this)

```text
Trit-trot, trit-trot, trit-trot, all day long. You’d think their demned hooves were made of iron. It fair gives me a headache, it does. Back and forth, back and forth. As if the grass were actually greener on one side one day, on the other the next. Goats really are a monstrous race. . . . It makes me long for the days of Troll.

the Bridge finally gets to explain this perilous situation from his . . . or her perspective.

We never were on more than a generic-name basis. He was Troll. I was Bridge. It takes trolls—and bridges, for that matter – a long time to warm up to full introductions. SO I never had a chance to know his first name before he was . . . well . . . gone. But he was a pleasant sort, for a troll. Knew a lot of stories. Troll stories, of course, are full of blood and food, food and blood. But they were good stories, for all that. Told loudly and with great passion. I really do miss them.

Not that I don’t have a few good stories of my own to tell. I mean, I wasn’t always a Goat Bridge. Long before that demned tribe arrived to foul my planking, I was a Bridge of Some Consequence. Mme. D’Aulnoy herself traversed my boards. And her friend Mms. Le Prince du Beaumont. Ah – the sound of wheels rolling. There is a memory to treasure.

Non of this trit-trot, trit-trot business.

But then the dear ladies were gone and the meadows, once pied with colorful flowers, were sold to a goat merchant, M. de Gruff. He pastured his demned beasties on both sides of my river. They sharpened their horns on my railings, pawed deep into the earthen slopes, and ate up every last one of the flowers. The grass in the meadows was gnawed down to nubbins by those voracious creatures. In other words, they made a desert out of an Eden.

Trit-trot, trit-trot, indeed.

So you can imagine how thrilled I was when Troll showed up, pushing his way upstream from the confluence of the great rivers below.

He wasn’t much to look at when he arrived, being young and quite thin. Of course he had the big bran-muffin eyes and the sled-jump nose and the gingko-leaf ears that identify a troll immediately. And when he smiled, there were those moss green teeth, filed to points. But otherwise he was a quite unprepossessing troll.

Trolls are territorial, you know, and when food gets scarce, the young are pushed out by the older, beigger, meaner trolls. Or so my Troll told me, and I have no reason to disbelieve him. He said, “Me dad gave a shove when he got hungry. I had to go. Been on the move awhile.”

That was an understatement. Actually he had been wading through miles of river before he found me unoccupied. He must have thought it paradise when he saw all those goats.

Not that he could have run across the fields after them. It is a well-kept secret that trolls must have one foot in the water at all times. Troll told me this one night when we were trading tales. They call it water-logging. Troll even sang me a song about it that went something like this:

Two feet wet,

None on shore,

You will live

Evermore.

One foot wet,

One foot dry,

You will never

Need to cry.

Two feet dry –

Say good-bye.

Well, trolls are actually better at stories than poems. You want good poetry, you have to hang out with boggles or sprites.

Of course the whole thing is a secret and I only tell you this because there are no longer many trolls about. It is a shame, actually. M. Darwin wrote of this disappearing phenomenon, and I, for one, believe it.

So trolls must wait by a river’s bank for some creature to cross if they want to eat. That’s why trolls and bridges have such an affinity. A bridge means a crossing place, and we are much more stable than fords. Trolls, while not having particularly scientific minds, long ago figured this much out.

So there we were, Troll and I, he dining on M. de Gruff’s billy goats, large and small and in-between. And after each meal, after he had a round of belching and farting – which trolls consider good form – he favored me with a troll tale.

He told me about trolls in love and trolls at war— which to the untutored ear can sound much the same.

He told me a tale about a troll who lived in the waters near Notre-Dame, eating fish and fishermen. But that troll conceived an unlikely passion for the cathedral. He desired to talk to the gargoyles, whom he thought must be cousins of his. He began to waste away with longing for just a single word with his stone kin. So he pulled himself up out of the water and started across the land. After three steps he died, of course. The Parisians used his bones for soup and built a monument where he fell. But he died happy – or so Troll said.

He told me about a troll who had been interviewed by a journalist, and when I asked what paper the piece had appeared in, he giggled, an unlikely sound coming from such a large source. The silly troll, he said, had eaten the man before he wrote the story, not after. We had a good laugh about that!

And then he told me about his mother, about the good times before his father had given him a shove. We cried together. After all, that’s what friends are for.

He was so delighted with my company, he tried to compose a troll song to the beauty of my span, but he got lost in rhymes about tans/fans/bans and never did finish it. But he was a good teller of tales.

And I am the consummate listener.

I must admit that – except for the day Mme. D’Aulony and Mme. Le Prince du Beaumont traded stories sitting on the banks of my stream, their petit picnic spread out on a blanket – I was never happier.

But the sad fact is that trolls are not very smart. Good storytellers, yes. Pleasant companions, quite. Undemanding friends, absolutely. But they lack upstairs what they have elsewhere. Breadth. They are – alas— really quite stupid. They do not have the slightest understanding of diplomatic dissembling. They do not know how to prevaricate—or to put it more succinctly, they cannot tell a lie. Even with my coaching, Troll would not move downstream a ways and take goats from different parts of the river just to fool, them.

“I like it here with you,” he said. “Besides, this is my place.”

And not being a troll myself, I couldn’t shove him off.

So the day came when the goats stopped crossing the bridge because it had become too notably dangerous. For a month not a single one went over my span. And while I was delighted to be rid of that constant, demned trit-trot, trit-trot, it worried me to see my friend grow so thin and wan. It got so one could almost read a book through him. He had not even the energy to tell stories.

So I did what I could. Bridges are not a flighty tribe. We are solid and stolid. We stay put. But we have our wiles for all that. One does not arch over a river for so many years without learning something.

I waited until one rather silly young goat strayed a bit too close to my embankments and I called to him.

“Come here, little goat.”

He looked about cautiously. “are you a troll?”

“A troll? Do I look like a troll?”

“Well, actually you look like a bridge.”

He shook his little nubbined head.

“but you have seen a bridge?”

He giggled. I knew then that I had him.

“So if you have never seen a troll, how do you know they exist?”

“My mother warned me about them.”

I allowed myself a deprecating little laugh. “Mothers! I bet she also warned you about eating tins and paper products and staying out too late at night.”

He nodded.

“I am just a bridge,” I said. “Immobile and proper. And of course, on my other side is . . . “

“A green meadow?” he asked.

“Greener than any you have ever seen,” I said.

That did it. He upped and started over. Trit-trot, trit-trot.

Of course, halfway there, Troll came up and grabbed the fool off and had his first good dinner in a month. Well, good dinner is perhaps an exaggeration. It was only a very little goat. Practically a kid.

If only he had been content with the one. But the next goat I snared for him with my promise of greener pastures was middle sized.

“Let this one go over,” I whispered to Troll, “and you will soon have the entire herd wanting to follow.” Even though I mentally cringed at the idea of so many trits and so many trots, I did not want my friend to die.

But that smacked too much of planning, something trolls have no sense about. And lying, which they know nothing of at all.

“Hungry now!” Troll complained, and ate the middle-sized de Gruff goad right then and there.

So when the big goat followed, with horns as sharp as gaffing hooks and a sly twist of mind, it is no wonder that my dear Troll was taken in.

It was not the fall that killed him, of course. It was when the big billy goat of M. de Gruff lifted him out of the water. Troll was dead long before he hit the ground.

My own fault then, you will say, that I must endure this trit-trot, trit-trot all day long. I do not, myself, accept blame. Life is like a river: forever changing. Sometimes it is at flood stage, and sometimes not.

But if you should hear of another troll who is looking for a home, tell him there is a Bridge of Slight Consequence placed between two green meadows not far from Avignon. Fish abound in the water, and goats gambol on the hills. And if he is not too greedy a troll, he can make a good living here. Besides, he will have an excellent listener to his tales. What troll could resist that?
```

---

## IC-1991: The Celebrated Jumping Frog of Calaveras County

- Title: The Celebrated Jumping Frog of Calaveras County
- Author (byline): Mark Twain
- Work: The Unabridged Mark Twain
- Publisher: Running Press
- Publication date as stated: November 1976
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2657
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mark Twain
Book: The Unabridged Mark Twain
ISBN: 978-0914294535
Publisher: Running Press
Date (Month/Year): November 1976
```

### Introduction (context only: never use it for content warnings)

```text
Mark Twain once wrote, “Let us be thankful for the fools. But for them the rest of us could not succeed.” Though such thoughts are seldom spoken out loud in today’s politically correct America, there is little doubt that the mantra echoes in our thoughts multiple times each day.

This concept was, however, more readily apparent during the early days of Mark Twain’s career, because the “fools” were geographically situated. The East and its inhabitants had a reputation for being civilized, cultured, and advanced. The West, on the other hand, was considered less-educated - - less-refined and as is seen in The Celebrated Jumping Frog of Calaveras County . . . naive and easily duped.
```

### Performance text (classify this)

```text
In compliance with the request of a friend of mine, who wrote me from the East, I called on good-natured, garrulous old Simon Wheeler, and inquired after my friend's friend, Leonidas W. Smiley, as requested to do, and I hereunto append the result. I have a lurking suspicion that Leonidas W. Smiley is a myth; that my friend never knew such a personage; and that he only conjectured that, if I asked old Wheeler about him, it would remind him of his infamous Jim Smiley, and he would go to work and bore me nearly to death with some infernal reminiscence of him as long and tedious as it should be useless to me. If that was the design, it certainly succeeded.

I found Simon Wheeler dozing comfortably by the bar-room stove of the old, dilapidated tavern in the ancient mining camp of Angel's, and I noticed that he was fat and bald-headed, and had an expression of winning gentleness and simplicity upon his tranquil countenance. He roused up and gave me good-day. I told him a friend of mine had commissioned me to make some inquiries about a cherished companion of his boyhood named Leonidas W. Smiley Rev. Leonidas W. Smiley a young minister of the Gospel, who he had heard was at one time a resident of Angel's Camp. I added that, if Mr.

Wheeler could tell me any thing about this Rev. Leonidas W. Smiley, I would feel under many obligations to him. Simon Wheeler backed me into a corner and blockaded me there with his chair, and then sat me down and reeled off the monotonous narrative which follows this paragraph. He never smiled, he never frowned, he never changed his voice from the gentle-flowing key to which he tuned the initial sentence, he never betrayed the slightest suspicion of enthusiasm; but all through the interminable narrative there ran a vein of impressive earnestness and sincerity, which showed me plainly that, so far from his imagining that there was any thing ridiculous or funny about his story, he regarded it as a really important matter, and admired its two heroes as men of transcendent genius in finesse. To me, the spectacle of a man drifting serenely along through such a queer yarn without ever smiling, was exquisitely absurd. As I said before, I asked him to tell me what he knew of Rev. Leonidas W. Smiley, and he replied as follows. I let him go on in his own way, and never interrupted him once: There was a feller here once by the name of Jim Smiley, in the winter of '49 or may be it was the spring of '50 I don't recollect exactly, somehow, though what makes me think it was one or the other is because I remember the big flume wasn't finished when he first came to the camp; but any way, he was the curiosest man about always betting on any thing that turned up you ever see, if he could get any body to bet on the other side; and if he couldn't, he'd change sides. Any way that suited the other man would suit him any way just so's he got a bet, he was satisfied. But still he was lucky, uncommon lucky; he most always come out winner. He was always ready and laying for a chance; there couldn't be no solittry thing mentioned but that feller'd offer to bet on it, and -take any side you please, as I was just telling you. If there was a horse-race, you'd find him flush, or you'd find him busted at the end of it; if there was a dog-fight, he'd bet on it; if there was a cat-fight, he'd bet on it; if there was a chicken-fight, he'd bet on it; why, if there was two birds setting on a fence, he would bet you which one would fly first; or if there was a camp-meeting, he would be there reg'lar, to bet on Parson Walker, which he judged to be the best exhorter about here, and so he was, too, and a good man. If he even seen a straddle-bug start to go anywheres, he would bet you how long it would take him to get wherever he was going to, and if you took him up, he would foller that straddle-bug to Mexico but what he would find out where he was bound for and how long he was on the road. Lots of the boys here has seen that Smiley, and can tell you about him. Why, it never made no difference to him he would bet on any thing the dangdest feller. Parson Walker's wife laid very sick once, for a good while, and it seemed as if they warn's going to save her; but one morning he come in, and Smiley asked how she was, and he said she was considerable better thank the Lord for his inftnit mercy and coming on so smart that, with the blessing of Providence, she'd get well yet; and Smiley, before he thought, says, "Well, I'll risk two- and-a-half that she don't, any way."

Thish-yer Smiley had a mare the boys called her the fifteen- minute nag, but that was only in fun, you know, because, of course, she was faster than that and he used to win money on that horse, for all she was so slow and always had the asthma, or the distemper, or the consumption, or something of that kind. They used to give her two or three hundred yards start, and then pass her under way; but always at the fag-end of the race she'd get excited and desperate- like, and come cavorting and straddling up, and scattering her legs around limber, sometimes in the air, and sometimes out to one side amongst the fences, and kicking up m-o-r-e dust, and raising m-o-r-e racket with her coughing and sneezing and blowing her nose and always fetch up at the stand just about a neck ahead, as near as you could cipher it down.

And he had a little small bull pup, that to look at him you'd think he wan's worth a cent, but to set around and look ornery, and lay for a chance to steal something. But as soon as money was up on him, he was a different dog; his underjaw'd begin to stick out like the fo'castle of a steamboat, and his teeth would uncover, and shine savage like the furnaces. And a dog might tackle him, and bully- rag him, and bite him, and throw him over his shoulder two or three times, and Andrew Jackson which was the name of the pup Andrew Jackson would never let on but what he was satisfied, and hadn't expected nothing else and the bets being doubled and doubled on the other side all the time, till the money was all up; and then all of a sudden he would grab that other dog jest by the j'int of his hind leg and freeze on it not chew, you understand, but only jest grip and hang on till they thronged up the sponge, if it was a year. Smiley always come out winner on that pup, till he harnessed a dog once that didn't have no hind legs, because they'd been sawed off by a circular saw, and when the thing had gone along far enough, and the money was all up, and he come to make a snatch for his pet bolt, he saw in a minute how he'd been imposed on, and how the other dog had him in the door, so to speak, and he 'peered sur- prised, and then he looked sorter discouraged-like, and didn't try no more to win the fight, and so he got shucked out bad. He give Smiley a look, as much as to say his heart was broke, and it was his fault, for putting up a dog that hadn't no hind legs for him to take bolt of, which was his main dependence in a fight, and then he limped off a piece and laid down and died. It was a good pup, was that Andrew Jackson, and would have made a name for hisself if he'd lived, for the stuff was in him, and he had genius I know it, because he hadn't had no opportunities to speak of, and it don't stand to reason that a dog could make such a fight as he could under them circumstances, if he hadn't no talent. It always makes me feel sorry when I think of that last fight of his'n, and the way it turned out.

Well, thish-yer Smiley had rat-tarriers, and chicken cocks, and tom- cats, and all of them kind of things, till you couldn't rest, and you couldn't fetch nothing for him to bet on but he'd match you. He ketched a frog one day, and took him home, and said he cal'klated to edercate him; and so he never done nothing for three months but set in his back yard and learn that frog to jump. And you bet you he did learn him, too. He'd give him a little punch behind, and the next minute you'd see that frog whirling in the air like a doughnut see him turn one summerset, or may be a couple, if he got a good start, and come down flat-footed and all right, like a cat. He got him up so in the matter of catching flies, and kept him in practice so constant, that he'd nail a fly every time as far as he could see him. Smiley said all a frog wanted was education, and he could do most any thing and I believe him. Why, I've seen him set Dan'l Webster down here on this floor Dan'l Webster was the name of the frog and sing out, "Flies, Dan'l, flies!" and quicker'n you could wink, he'd spring straight up, and snake a fly off'n the counter there, and flop down on the floor again as solid as a gob of mud, and fall to scratching the side of his head with his hind foot as indifferent as if he hadn't no idea he'd been doin' any more'n any frog might do. You never see a frog so modest and straightforward as he was, for all he was so gifted. And when it come to fair and square jumping on a dead level, he could get over more ground at one straddle than any animal of his breed you ever see. Jumping on a dead level was his strong suit, you understand; and when it come to that, Smiley would ante up money on him as long as he had a red. Smiley was monstrous proud of his frog, and well he might be, for fellers that had traveled and been everywheres, all said he laid over any frog that ever they see. Well, Smiley kept the beast in a little lattice box, and he used to fetch him down town sometimes and lay for a bet. One day a feller a stranger in the camp, he was come across him with his box, and says:

"What might it be that you've got in the box?"

And Smiley says, sorter indifferent like, "It might be a parrot, or it might be a canary, may be, but it an't it's only just a frog."

And the feller took it, and looked at it careful, and turned it round this way and that, and says, "H'm so 'tis. Well, what's he good for?"

"Well," Smiley says, easy and careless, "He's good enough for one thing, I should judge he can outjump any frog in Calaveras county."

The feller took the box again, and took another long, particular look, and give it back to Smiley, and says, very deliberate, "Well, I don't see no p'ints about that frog that's any better'n any other frog."

"May be you don't," Smiley says. "May be you understand frogs, and may be you don't understand 'em; may be you've had experience, and may be you an't only a amature, as it were. Anyways, I've got my opinion, and I'll risk forty dollars that he can outjump any frog in Calaveras county."

And the feller studied a minute, and then says, kinder sad like, "Well, I'm only a stranger here, and I an't got no frog; but if I had a frog, I'd bet you."

And then Smiley says, "That's all right that's all right if you'll hold my box a minute, I'll go and get you a frog." And so the feller took the box, and put up his forty dollars along with Smiley's, and set down to wait.

So he set there a good while thinking and thinking to hisself, and then he got the frog out and prized his mouth open and took a tea- spoon and filled him full of quail shot filled him pretty near up to his chin and set him on the floor. Smiley he went to the swamp and slopped around in the mud for a long time, and finally he ketched a frog, and fetched him in, and give him to this feller, and says:

"Now, if you're ready, set him alongside of Dan'l, with his fore- paws just even with Dan'l, and I'll give the word." Then he says, "One two three jump!" and him and the feller touched up the frogs from behind, and the new frog hopped off, but Dan'l give a heave, and hysted up his shoulders so like a Frenchman, but it wan's no use he couldn't budge; he was planted as solid as an anvil, and he couldn't no more stir than if he was anchored out. Smiley was a good deal surprised, and he was disgusted too, but he didn't have no idea what the matter was, of course.

The feller took the money and started away; and when he was going out at the door, he sorter jerked his thumb over his shoulders this way at Dan'l, and says again, very deliberate, "Well, I don't see no p'ints about that frog that's any better'n any other frog."

Smiley he stood scratching his head and looking down at Dan'l a long time, and at last he says, "I do wonder what in the nation that frog throw'd off for I wonder if there an't something the matter with him he 'pears to look mighty baggy, somehow." And he ketched Dan'l by the nap of the neck, and lifted him up and says, "Why, blame my cats, if he don't weigh five pound!" and turned him upside down, and he belched out a double handful of shot. And then he see how it was, and he was the maddest man he set the frog down and took out after that feller, but he never ketchd him. And-

[Here Simon Wheeler heard his name called from the front yard, and got up to see what was wanted.] And turning to me as he moved away, he said: "Just set where you are, stranger, and rest easy I an't going to be gone a second."

But, by your leave, I did not think that a continuation of the history of the enterprising vagabond Jim Smiley would be likely to afford me much information concerning the Rev. Leonidas W. Smiley, and so I started away.

At the door I met the sociable Wheeler returning, and he button- holed me and recommenced: "Well, thish-yer Smiley had a yeller one-eyed cow that didn't have no tail, only jest a short stump like a bannanner, and

"Oh! hang Smiley and his afflicted cow!" I muttered, good-naturedly, and bidding the old gentleman good-day, I departed.
```

---

## IC-1992: Charles

- Title: Charles
- Author (byline): Shirley Jackson
- Work: The Lottery and Other Stories (Pg 91)
- Publisher: Farrar, Straus and Giroux
- Publication date as stated: March 2005
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1611
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shirley Jackson
Book: The Lottery and Other Stories (Pg 91)
ISBN: 978-0374529536
Publisher: Farrar, Straus and Giroux
Date (Month/Year): March 2005
```

### Introduction (context only: never use it for content warnings)

```text
Charles by Shirley Jackson
```

### Performance text (classify this)

```text
The day my son Laurie started kindergarten he renounced corduroy overalls with bibs and began wearing blue jeans with a belt; I watched him go off the first morning with the older girl next door, seeing clearly that an era of my life was ended, my sweet-voiced nursery-school tot replaced by a long-trousered, swaggering character who forgot to stop at the corner and wave good-bye to me.

He came home the same way, the front door slamming open, his cap on the floor, and the voice suddenly become raucous shouting, “Isn’t anybody here?”

At lunch he spoke insolently to his father, spilled his baby sister’s milk, and remarked that his teacher said we were not to take the name of the Lord in vain.

“How was school today?” I asked, elaborately casual.

“All right,” he said.

“Did you learn anything?” his father asked.

Laurie regarded his father coldly. “I didn’t learn nothing,” he said.

“Anything,” I said. “Didn’t learn anything”

“The teacher spanked a boy, though,” Laurie said, addressing his bread and butter. “For being fresh,” he added, with his mouth full.

“What did he do?” I asked. “Who was it?”

Laurie thought. “It was Charles,” he said. “He was fresh.

The teacher spanked him and made him stand in a corner. He was awfully fresh.”

“What did he do?” I asked again, but Laurie slid off his chair, took a cookie, and left, while his father was still saying, “See here, young man.”

The next day Laurie remarked at lunch, as soon as he sat down, “Well, Charles was bad again today.” He grinned enormously and said, “Today Charles hit the teacher.”

“Good heavens,” I said, mindful of the Lord’s name, “I suppose he got spanked again?”

“He sure did,” Laurie said. “Look up,” he said to his father.

“What?” his father said, looking up.

“Look down,” Laurie said. “Look at my thumb. Gee, you’re dumb.” He began to laugh insanely.

“Why did Charles hit the teacher?” I asked quickly.

“Because she tried to make him color with red crayons,” Laurie said. “Charles wanted to color with green crayons so he hit the teacher and she spanked him and said nobody play with Charles but everybody did.”

The third day—it was Wednesday of the first week—Charles bounced a see-saw on to the head of a little girl and made her bleed, and the teacher made him stay inside all during recess. Thursday Charles had to stand in a corner during story-time because he kept pounding his feet on the floor. Friday Charles was deprived of blackboard privileges because he threw chalk.

On Saturday I remarked to my husband, “Do you think kindergarten is too unsettling for Laurie? All this toughness, and bad grammar, and this Charles boy sounds like such a bad influence.”

“It’ll be all right,” my husband said reassuringly. “Bound to be people like Charles in the world. Might as well meet them now as later.”

On Monday Laurie came home late, full of news. “Charles,” he shouted as he came up the hill; I was waiting anxiously on the front steps. “Charles,” Laurie yelled all the way up the hill, “Charles was bad again.”

“Come right in,” I said, as soon as he came close enough. “Lunch is waiting.”

“You know what Charles did?” he demanded, following me through the door. “Charles yelled so in school they sent a boy in from first grade to tell the teacher she had to make Charles keep quiet, and so Charles had to stay after school. And so all the children stayed to watch him.”

“What did he do?” I asked.

“He just sat there,” Laurie said, climbing into his chair at the table. “Hi, Pop, y’old dust mop.”

“Charles had to stay after school today,” I told my husband.

“Everyone stayed with him.”

“What does this Charles look like?” my husband asked Laurie. “What’s his other name?”

“He’s bigger than me,” Laurie said. “And he doesn’t have any rubbers and he doesn’t ever wear a jacket.”

Monday night was the first Parent-Teachers meeting, and only the fact that the baby had a cold kept me from going; I wanted passionately to meet Charles’s mother.

On Tuesday Laurie remarked suddenly, “Our teacher had a friend come to see her in school today.”

“Charles’s mother?” my husband and I asked simultaneously.

“Naaah,” Laurie said scornfully. “It was a man who came and made us do exercises, we had to touch our toes. Look.”

He climbed down from his chair and squatted down and touched his toes. “Like this,” he said. He got solemnly back into his chair and said, picking up his fork, “Charles didn’t even do exercises.”

“That’s fine,” I said heartily. “Didn’t Charles want to do exercises?”

“Naaah,” Laurie said. “Charles was so fresh to the teacher’s friend he wasn’t let do exercises.”

“Fresh again?” I said.

“He kicked the teacher’s friend,” Laurie said. “The teacher’s friend told Charles to touch his toes like I just did and Charles kicked him.”

“What are they going to do about Charles, do you suppose?” Laurie’s father asked him.

Laurie shrugged elaborately. “Throw him out of school, I guess,” he said.

Wednesday and Thursday were routine; Charles yelled during story hour and hit a boy in the stomach and made him cry.

On Friday Charles stayed after school again and so did all the other children.

With the third week of kindergarten Charles was an institution in our family; the baby was being a Charles when she cried all afternoon; Laurie did a Charles when he filled his wagon full of mud and pulled it through the kitchen; even my husband, when he caught his elbow in the telephone cord and pulled telephone, ashtray, and a bowl of flowers off the table, said, after the first minute, “Looks like Charles.”

During the third and fourth weeks it looked like a reformation in Charles; Laurie reported grimly at lunch on Thursday of the third week, “Charles was so good today the teacher gave him an apple.”

“What?” I said, and my husband added warily, “You mean Charles?”

“Charles,” Laurie said. “He gave the crayons around and he picked up the books afterward and the teacher said he was her helper.”

“What happened?” I asked incredulously.

“He was her helper, that’s all,” Laurie said, and shrugged.

“Can this be true, about Charles?” I asked my husband that night. “Can something like this happen?”

“Wait and see,” my husband said cynically. “When you’ve got a Charles to deal with, this may mean he’s only plotting.”

He seemed to be wrong. For over a week Charles was the teacher’s helper; each day he handed things out and he picked things up; no one had to stay after school.

“The P.T.A. meeting’s next week again,” I told my husband one evening. “I’m going to find Charles’s mother there.”

“Ask her what happened to Charles,” my husband said. “I’d like to know.”

“I’d like to know myself,” I said.

On Friday of that week things were back to normal. “You know what Charles did today?” Laurie demanded at the lunch table, in a voice slightly awed. “He told a little girl to say a word and she said it and the teacher washed her mouth out with soap and Charles laughed.”

“What word?” his father asked unwisely, and Laurie said,

“I’ll have to whisper it to you, it’s so bad.” He got down off his chair and went around to his father. His father bent his head down and Laurie whispered joyfully. His father’s eyes widened.

“Did Charles tell the little girl to say that?” he asked respectfully.

“She said it twice,” Laurie said. “Charles told her to say it twice.”

“What happened to Charles?” my husband asked.

“Nothing,” Laurie said. “He was passing out the crayons.”

Monday morning Charles abandoned the little girl and said the evil word himself three or four times, getting his mouth washed out with soap each time. He also threw chalk.

My husband came to the door with me that evening as I set out for the P.T.A. meeting. “Invite her over for a cup of tea after the meeting,” he said. “I want to get a look at her.”

“If only she’s there,” I said prayerfully.

“She’ll be there,” my husband said. “I don’t see how they could hold a P.T.A. meeting without Charles’s mother.”

At the meeting I sat restlessly, scanning each comfortable matronly face, trying to determine which one hid the secret of Charles. None of them looked to me haggard enough. No one stood up in the meeting and apologized for the way her son had been acting. No one mentioned Charles.

After the meeting I identified and sought out Laurie’s kindergarten teacher. She had a plate with a cup of tea and a piece of chocolate cake; I had a plate with a cup of tea and a piece of marshmallow cake. We maneuvered up to one another cautiously, and smiled.

“I’ve been so anxious to meet you,” I said. “I’m Laurie’s mother.”

“We’re all so interested in Laurie,” she said.

“Well, he certainly likes kindergarten,” I said. “He talks about it all the time.”

“We had a little trouble adjusting, the first week or so,” she said primly, “but now he’s a fine little helper. With occasional lapses, of course.”

“Laurie usually adjusts very quickly,” I said. “I suppose this time it’s Charles’s influence.”

“Charles?”

“Yes,” I said, laughing, “you must have your hands full in that kindergarten, with Charles.”

“Charles?” she said. “We don’t have any Charles in the kindergarten.”
```

---

## IC-1993: Charlie the Caterpillar

- Title: Charlie the Caterpillar
- Author (byline): Dom DeLuise
- Work: Not specified
- Publisher: Aladdin
- Publication date as stated: April 1993
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, CHARLIE, MONKEY 1, MONKEY 2, RABBIT 1, RABBIT 2, MOUSE 1, MOUSE 2, KATIE
- Teaser before the introduction: Yes
- Spoken words (computed): 846
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dom DeLuise
ISBN: 978-0671796075
Publisher: Aladdin
Date (Month/Year): April 1993
```

### Introduction (context only: never use it for content warnings)

```text
Sticks and stones can break my bones, but words will never hurt me. – Well, the first part is true, but the second part is completely wrong.

When I was in grade school, I had to get glasses . . . then in middle school it was braces and the horrible transition of puberty when your bones grow too fast for you to NOT be clumsy and you get pimples and the braces make you lisp and you get food caught in your teeth that you don’t even know is there and then Grandma Connie sends you the most hideous Christmas sweater, but you have to wear it because it was a gift . . . It happens to everyone, right? And no one, not one single person ever made fun of me . . . Is my nose growing yet? Just what I need!

In Charlie the Caterpillar, we experience the perils of growing up in a society that would rather make fun of you than to build you up.

Charlie the Caterpillar by Dom DeLuise.
```

### Performance text (classify this)

```text
NARRATOR: One day, one bright sunny day, Charlie the Caterpillar was born. (Charlie is born) The world looked very, very big to Charlie because he was very, very small. Charlie soon found out how delicious green things tasted. (Charlie nibbles on a blade of grass) He could hear the wind whistling and the birds singing. (Charlie smiles) He was glad to be alive. Charlie decided to set out and see the world, so he looked to the left, and he looked to the right and then he went straight ahead. Soon Charlie saw two monkeys.

CHARLIE: Hi! What are you doing?

MONKEY 1: We’re playing cards.

CHARLIE: Oh, that sounds like fun. Can I play too?

MONKEY 2: No, you can’t.

CHARLIE: Why not?

MONKEY 1: Because you’re an ugly caterpillar. Now get out of here.

MONKEY 1: (echoing voice) . . . Because you’re an ugly caterpillar . . . .

NARRATOR: Charlie, for the very first time in his young life, felt bad. (Charlie sighs heavily) He would have shrugged his shoulders if he had any. He looked to the left, and he looked to the right and then he went straight ahead. Pretty soon he saw two rabbits hopping around.

CHARLIE: Hi! What are you doing?

RABBIT 1: We’re playing tennis.

CHARLIE: Oh, that looks like fun. Can I play too?

RABBIT 2: No, you can’t.

CHARLIE: Why not?

RABBIT 1: Because you’re an ugly caterpillar, and we don’t play with ugly caterpillars. Now, get out of here.

NARRATOR: Now, for the second time in his young life, Charlie felt bad, very bad. His feelings were hurt.

CHARLIE: (to himself) What is ugly?

NARRATOR: He didn’t feel ugly. He looked to the left, and he looked to the right and then he went straight ahead. Just then, Charlie saw two mice playing miniature golf.

CHARLIE: Hi! What are you doing?

MOUSE 1: We’re playing golf.

CHARLIE: Oh, that really looks like fun. Can I play too?

MOUSE 2: No, you can’t.

CHARLIE: Why not?

MOUSE 1: Because you’re an ugly caterpillar, and we really don’t play with ugly caterpillars. Now, get out of here.

NARRATOR: Charlie, for the third time in his not-so-young life, felt very, very bad. In fact, Charlie started to feel ugly. No one wanted to play with him. So Charlie looked to the left, and he looked to the right and then he started to cry.

CHARLIE: (crying)

NARRATOR: Charlie wanted to be alone. He climbed up a tree and snuggled up to a small branch. (Charlie climbs, he sits shivering) He felt a little cold, so he went like this (Charlie begins spinning a cocoon) and he went like that, and he went like that, and he went like this, and he went like that, and before he knew it, he had spun himself a warm and wonderful cocoon.

CHARLIE: (sadly) Why can’t I have a friend. (exhausted, he drifts off to sleep)

NARRATOR: All of a sudden, snow began to fall and cover everything with white. Winter had come, but Charlie was nice and warm in his comfortable cocoon. Charlie dreamed that he had a best friend, and in his dream they laughed and had fun together. (Charlie laughs in his sleep) After a while, the grass began to grow, the flowers began to bloom and the birds began to have a party in the sky. Spring had come and somehow Charlie knew it was time to wake up. (Charlie yawns and stretches) And then -- oh, my goodness! (Pop, pop – his wings unfurl one at a time; and Charlie is in awe, looking first left then right) He had wings! Beautiful wings! Charlie had become a beautiful butterfly.

(Charlie flutters his wings and flies, laughing) He flew up, up and up. He soared past the birds having a party in the sky. Charlie was flying high when he came upon the monkeys who were still playing cards.

MONKEY 2: (begging) Oh, please come and play with us!

CHARLIE: Why?

MONKEY 1: Because you’re a beautiful butterfly.

CHARLIE: No, thanks. I gotta get outta here! (He zooms away and the monkeys jump back, looking miserable) Serves them right!

NARRATOR: He did a couple of loopy loops and then he came across the rabbits at their tennis game.

RABBIT 2: Oh, please, won’t you come and play with us?

CHARLIE: Why?

RABBIT 1: Because you’re such a beautiful butterfly!

CHARLIE: Not on your life. Now I gotta get outta here! (he flies off, leaving the rabbits looking very down-hearted) Serves them right!

NARRATOR: He didn’t want to play with them because they were quite mean to him when he was a caterpillar. He circled around for a while and then he saw the mice playing miniature golf.

MOUSE 2: (pleading) Please, please, pretty please, do come and play with us.

CHARLIE: Why?

MOUSE 1: Because you’re really such a beautiful butterfly!

CHARLIE: Sorry, not today. I really have better things to do. Now I gotta get outta here! (he soars off, leaving the mice looking pitiful) Serves them right!

NARRATOR: They all wanted to be his friend because he was now a beautiful butterfly. They didn’t know he was Charlie, the ugly caterpillar.

CHARLIE: If they want to be my friends just because of my beautiful wings, they can’t be real friends.

NARRATOR: And just then Charlie heard someone crying. It was Katie the Caterpillar.

KATIE: (crying with gusto)

CHARLIE: Why are you crying?

KATIE: Because no one will play with me. No one wants to be my friend because I’m an ugly caterpillar.

CHARLIE: (winking and smiling) I’ll play with you. I’ll be your friend.

KATIE: You will? Whoopeee!

NARRATOR: And then Charlie took Katie aside and told her all about becoming a butterfly. Charlie showed Katie what she will look like when she’s a butterfly. (they look in the surface of a small lake, Charlie standing behind her so that her reflection would show up like a mirror in the water) And that made Katie feel good. From that day on, Charlie and Katie played cards and tennis and even miniature golf together. (laughing) They had a good time just like in Charlie’s dream. Katie was happy and Charlie was very happy. He had finally found a friend . . . a real friend . . . a best friend.
```

---

## IC-1994: Charlotte’s Web

- Title: Charlotte’s Web
- Author (byline): E. B. White
- Work: Not specified
- Publisher: HarperCollins
- Publication date as stated: April 2012
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1821
- Already set (do not supply): none

### Source block (context only)

```text
Author: E. B. White
ISBN: 978-0061232916
Publisher: HarperCollins
Date (Month/Year): April 2012
```

### Introduction (context only: never use it for content warnings)

```text
Spiders all over America probably don't realize how often their lives have been spared because the person who spies one in the house has read Charlotte's Web. No such reader has ever looked at a young pig without thinking of Wilbur. Surely, we've looked at spider webs hoping to spot some trace of a word in its intricacies. And, while most of us still fail to appreciate rats, we do smile at the gluttonous but ultimately heroic Templeton. I defy anyone to experience this tale without shedding tears over Charlotte's death, the account of which ends with one of the saddest lines in literature "No one was with her when she died." Charlotte’s Web by E. B. White
```

### Performance text (classify this)

```text
(Pg 163-171) Charlotte and Wilbur were alone. The families had gone to look for Fern. Templeton was asleep. Wilbur lay resting after the excitement and strain of the ceremony. His medal still hung from his neck; by looking out of the corner of his eye he could see it.

“Charlotte, why are you so quiet?”

“I like to sit still. I’ve always been rather quiet.”

“Yes, but you seem specially so today. Do you feel all right?”

“A little tired, perhaps. But I feel peaceful. Your success in the ring this morning was, to a small degree, my success. Your future is assured. You will live, secure and safe, Wilbur. Nothing can harm you now. These autumn days will shorten and grow cold. The leaves will shake loose from the trees and fall. Christmas will come, and the snows of winter. You will live to enjoy the beauty of the frozen world, for you mean a great deal to Zuckerman and he will not harm you, ever. Winter will pass, the days will lengthen, the ice will melt in the pasture pond. The song sparrow will return and sing, the frogs will awake, the warm wind will blow again. All these sights and sounds and smells will be yours to enjoy, Wilbur—this lovely world, these precious days…”

Charlotte stopped. A moment later a tear came to Wilbur’s eye. “Oh, Charlotte, to think that when I first met you I thought you were cruel and bloodthirsty! Why did you do all this for me? I don’t deserve it. I’ve never done anything for you.”

“You have been my friend. That in itself is a tremendous thing. I wove my webs for you because I liked you. After all, what’s a life, anyway? We’re born, we live a little while, we die. A spider’s life can’t help being something of a mess, with all this trapping and eating flies. By helping you, perhaps I was trying to lift up my life a trifle. Heaven knows anyone’s life can stand a little of that.”

“Well, I’m no good at making speeches. I haven’t got your gift for words. But you have saved me, Charlotte, and I would gladly give my life for you—I really would.”

“I’m sure you would. And I thank you for your generous sentiments.”

“Charlotte, we’re all going home today. The Fair is almost over. Won’t it be wonderful to be back home in the barn cellar again with the sheep and the geese? Aren’t you anxious to get home?”

For a moment Charlotte said nothing. Then she spoke in a voice so low Wilbur could hardly hear the words. “I will not be going back to the barn,” she said.

Wilbur leapt to his feet. “Not going back? Charlotte, what are you talking about?”

“I’m done for. In a day or two I’ll be dead. I haven’t even the strength enough to climb down into the crate. I doubt if I have enough silk in my spinnerets to lower me to the ground.”

Hearing this, Wilbur threw himself down in an agony of pain and sorrow. Great sobs wracked his body. He heaved and grunted with desolation. “Charlotte, Charlotte! My true friend!”

“Come now, let’s not make a scene. Be quiet, Wilbur. Stop thrashing about!”

“But I can’t stand it, I won’t leave you here alone to die. If you’re going to stay here I shall stay, too.”

“Don’t be ridiculous, You can’t stay here. Zuckerman and Lurvy and John Arable and the others will be back any minute now, and they’ll shove you into that crate and away you’ll go. Besides, it wouldn’t make any sense for you to stay. There would be no one to feed you. The fair Ground will soon be empty and deserted.”

Wilbur was in a panic. He raced round and round the pen. Suddenly he had an idea—he thought of the egg sac and the five hundred and fourteen little spiders that would hatch in the spring. If Charlotte herself was unable to go home to the barn, at least he must take her children along.

Wilbur rushed to the front of his pen. He put his front feet up on the top board and gazed around. In the distance he saw the Arables and the Zuckermans approaching. He knew he would have to act quickly.

“Where’s Templeton?”

“He’s in that corner, under the straw, asleep,”

Wilbur rushed over, pushed his strong snout under the rat, and tossed him into the air.

“Templeton! Pay attention!”

The rat, surprised out of a sound sleep, looked first dazed then disgusted. “What kind of monkeyshine is this? Can’t a rat catch a wink of sleep without being rudely popped in the air?”

“Listen to me! Charlotte is very ill. She only has a short time to live. She cannot accompany us home, because of her condition. Therefore, it is absolutely necessary that I take her egg sac with me. I can’t reach it, and I can’t climb. You are the only one that can get it. There is not a second to be lost. The people are coming—they’ll be here in no time. Please, please, please, Templeton, climb up and get the egg sac.”

The rat yawned. He straightened his whiskers. Then he looked up at the egg sac. “So! It’s old Templeton to the rescue again, is it? Templeton do that, Templeton please run down to the dump and get me a magazine clipping, Templeton please lend me a piece of string so I can spin a web.”

“Oh, hurry! Hurry up, Templeton!”

But the rat was in no hurry. He began imitating Wilbur’s voice. “So, it’s ‘Hurry up, Templeton,’ is it? Ho, ho. And what thanks do I ever get for these services, I would like to know? Never a kind word for old Templeton, only abuse and wisecracks and snide remarks. Never a kind word for a rat.”

“Templeton, if you don’t stop talking and get busy, all will be lost, and I will die of a broken heart. Please climb up!” Templeton lay back in the straw. Lazily he placed his forepaws behind his head and crossed his knees, in an attitude of complete relaxation.

“Die of a broken heart. How touching! My, my! I notice that it’s always me you come to when in trouble. But I’ve never heard of anyone’s heart breaking on my account. Oh, no. Who cares anything about old Templeton?”

“Get up! Stop acting like a spoiled child!”

Templeton grinned and lay still. “Who made trip after trip to the dump? Why, it was old Templeton! Who saved Charlotte’s life by scaring that Arable boy away with a rotten goose egg? Bless my soul, I believe it was old Templeton. Who bit your tail and got you back on your feet this morning after you had fainted in front of the crowd? Old Templeton. Has it occurred to you that I’m sick of running errands and doing favors? What do you think I am, anyway, a rat-of-all-work?

Wilbur was desperate. The people were coming. And the rat was failing him. Suddenly he remembered Templeton’s fondness for food.

“Templeton, I will make you a solemn promise. Get Charlotte’s egg sac for me, and from now on I will let you eat first, when Lurvy slops me. I will let you have your choice of everything in the trough and I won’t touch a thing until you’re through.”

The rat sat up. “You mean that?”

“I promise. I cross my heart.”

“All right, it’s a deal.” He walked to the wall and started to climb. His stomach was still swollen from last night’s gorge. Groaning and complaining, he pulled himself slowly to the ceiling. He crept along till he reached the egg sac. Charlotte moved aside for him. She was dying, but she still had strength enough to move a little. Then Templeton bared his long ugly teeth and began snipping the treads that fastened the sac to the ceiling. Wilbur watched from below.

“Use extreme care! I don’t want a single one of those eggs harmed.”

“Thith thtuff thicks in my mouth. It’th worth than caramel candy.” But Templeton worked away at the job, and managed to cut the sac adrift and carry it to the ground, where he dropped it in front of Wilbur. Wilbur heaved a great sigh of relief.

“Thank you, Templeton. I will never forget this as long as I live.”

“Neither will I. I feel as though I’d eaten a spool of thread. Well, home we go!”

Templeton crept into the crate and buried himself in the straw. He got out of sight just in time. Lurvy and John Arable and Mr. Zuckerman came along at that moment. Wilbur had already decided how he would carry the egg sac—there was only one way possible. He carefully took the little bundle in his mouth and held it there on top of his tongue. He remembered what Charlotte had told him—that the sac was waterproof and strong. It felt funny on his tongue and made him drool a bit. And of course he couldn’t say anything. But as he was being shoved into the crate, he looked up at Charlotte and gave her a wink. She knew he was saying good-bye in the only way he could. And she knew her children were safe.

“Good-bye!” Then she summoned all her strength and waved one of her front legs at him.

She never moved again. Next day, as the Ferris wheel was being taken apart and the race horses were being loaded into vans and the entertainers were packing up their belongings and driving away in their trailers, Charlotte died. The Fair Grounds were soon forlorn. The infield was littered with bottles and trash. Nobody, of the hundreds of people what had visited the Fair, knew that a grey spider had played the most important part of all. No one was with her when she died.

(Pg 183) As time went on, and the months and years came and went, Wilbur was never without friends. Fern did not come regularly to the barn any more. She was growing up, and was careful to avoid childish things, like sitting on a milk stool near a pigpen. But Charlotte’s children and grandchildren and great grandchildren, year after year, lived in the doorway. Each spring there were new little spiders hatching out to take the place of the old. Most of them sailed away, on their balloons. But always two or three stayed and set up housekeeping in the doorway.

(Pg 184) Wilbur never forgot Charlotte. Although he loved her children and grandchildren dearly, none of the new spiders ever quite took her place in his heart. She was in a class by herself. It is not often that someone comes along who is a true friend and a good writer. Charlotte was both.
```

---

## IC-1995: Chicken Little

- Title: Chicken Little
- Author (byline): James Finn Garner
- Work: Correct Bedtime Stories, Pgs 57-62
- Publisher: John Wiley and Sons, Inc.
- Publication date as stated: April 1994
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: CHICKEN LITTLE, NARRATOR, HENNY PENNY, GOOSEY LOOSEY, FOXY LOXY, ALL TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 879
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Finn Garner
Book: Correct Bedtime Stories, Pgs 57-62
ISBN: 978-0025427303
Publisher: John Wiley and Sons, Inc.
Date (Month/Year): April 1994
```

### Introduction (context only: never use it for content warnings)

```text
Ladies and gentlemen, esteemed members of the jury, and anyone who has ever stubbed their toe and briefly considered suing the furniture . . . welcome! Today’s selection is not just a story. It’s a legal drama; a barnyard thriller, if you will.

You may think you know the story of Chicken Little -- the tale of (pardon my alliteration) panic, paranoia, and poultry? But think again! In this version, the sky isn’t just falling…it’s liable. And someone’s getting paid.

When Chicken Little gets bonked on the head, it’s not just a crisis; it’s a lawsuit!

Chicken Little by James Finn Garner
```

### Performance text (classify this)

```text
CHICKEN LITTLE: (Pg 57-62) (happily playing in the road)

NARRATOR: Chicken Little lived on a winding country lane surrounded by tall oak trees. (It should be mentioned here that the name “Little” was a family name, and not a derogatory, size-biased nickname. It was only by sheer coincidence that Chicken Little was also of shorter-than-average height.) One day, Chicken Little was playing in the road when a gust of wind blew through the trees. An acorn was blown loose and hit Chicken Little squarely on the head.

CHICKEN LITTLE: (squawking and spinning in circles)

NARRATOR: Now, while Chicken Little had a small brain in the physical sense, she did use it to the best of her abilities. So when she screamed . . .

CHICKEN LITTLE: The sky is falling, the sky is falling!

NARRATOR: . . . her conclusion was not wrong or stupid or silly, only logically under enhanced. Chicken Little ran down the road until she came to the house of her neighbor, Henny Penny, who was tending her garden. This was a simple task, since she didn’t use any insecticide, herbicide or fertilizer, and also permitted the native nonedible varieties of wildflower (sometimes branded “weeds”) to mingle with her food crops. So, lost amid the foliage, Henny Penny heard Chicken Little’s voice long before she saw her.

CHICKEN LITTLE: The sky is falling! The sky is falling!

HENNY PENNY: (sticking her head out from her garden) Chicken Little! Why are you carrying on so?

CHICKEN LITTLE: I was playing in the road when a huge chunk of the sky fell and landed on my head. See? Here’s the bump to prove it.

HENNY PENNY: There’s just one thing to do.

CHICKEN LITTLE: What’s that?

HENNY PENNY: Sue the b**tards!

CHICKEN LITTLE: (puzzled) Sue for what?

HENNY PENNY: Personal injury, discrimination, intentional infliction of emotional distress, negligent infliction of emotional distress, tortuous interference, the tort of outrage -- you name it, we’ll sue for it.

CHICKEN LITTLE: Good gracious! What will we get for all of that?

HENNY PENNY: We can get payment for pain and suffering, compensatory damages, punitive damages, disability and disfigurement, long-term care, mental anguish, impaired earning power, loss of esteem . . .

CHICKEN LITTLE: (joyfully) Person, oh, person! Who are we going to sue?

HENNY PENNY: Well, I don’t think the sky per se is recognized as a suable entity by the state.

CHICKEN LITTLE: (her diminutive brain working overtime) I guess we should go find a lawyer and learn who is suable.

HENNY PENNY: That’s a good idea. And while we’re there, I can ask whom to sue for these ridiculously bony legs of mine. They’ve caused me nothing but anguish and embarrassment my whole life and I should be compensated somehow for all that.

NARRATOR: So, they ran farther down the road until they came to the house of their neighbor, Goosey Loosey. Goosey Loosey was busy teaching her canine animal companion to eat grass so she could avoid the guilty feelings that came with feeding the dog processed animal carcasses from a can.

CHICKEN LITTLE: The sky is falling! The sky is falling!

HENNY PENNY: Sue the b**tards! Sue the b**tards!

GOOSEY LOOSEY: (leaning over her fence) Land sakes! Why are you two carrying on so?

CHICKEN LITTLE: I was playing in the road and a piece of sky fell on my head.

HENNY PENNY: So we’re going to find a lawyer to tell us whom we can sue both for her injuries and for my bony legs.

GOOSEY LOOSEY: Oh good! Can I come and sue someone for my long, gangly neck? You know, nothing really flatters it, so I am convinced there’s a conspiracy within the fashion industry against long-necked waterfowl.

NARRATOR: So, the three of them ran down the road looking for legal assistance.

CHICKEN LITTLE: The sky is falling! The sky is falling!

HENNY PENNY: Sue the bastards! Sue the bastards!

GOOSEY LOOSEY: Smash the conspiracy! Smash the conspiracy!

NARRATOR: Farther down the road they met Foxy Loxy, who was dressed in a blue suit and carried a briefcase. He held up a paw to halt the entourage.

FOXY LOXY: And what are you three doing out on this lovely day?

ALL TOGETHER: We’re looking for someone to sue!

FOXY LOXY: What are your grievances? Personal
injury? Discrimination? Intentional infliction of
emotional distress? Negligent infliction of emotional
distress? Tortious interference? The tort of outrage?

CHICKEN LITTLE: (excitedly) Oh, yes, yes!

GOOSEY LOOSEY: all that . . .

HENNY PENNY: . . .and more!

FOXY LOXY: Well, then, you’re in luck. My caseload has just eased up, so I will be able to represent you in any and all lawsuits we can manage to bring.

CHICKEN LITTLE: (cheering and flapping her wings) But who are we going to sue?

FOXY LOXY: (without missing a beat) Who aren’t we going to sue? Three hapless victims such as yourselves will be able to find more guilty parties than you can shake a writ at. (deviously) Now, let’s all step into my office so we can discuss this further.

NARRATOR: Foxy Loxy walked over to a small black metal door that was in the side of a small hill nearby.

FOXY LOXY: (trying to lift the latch) Step right this way.

NARRATOR: But the black door wouldn’t open.

FOXY LOXY: (tugging on it with one paw, then with both. It still wouldn’t budge. He yanks and pulls violently, cursing the door, its mental abilities, and its history) Insert random tirade

NARRATOR: Finally, the door swung open, and a huge ball of fire shot out.

FOXY LOXY: (screams and tries to dodge)

NARRATOR: This was really the door to Foxy Loxy’s oven! But unfortunately for him, the ball of fire engulfed his head, burned off every hair and whisker, and left him totally catatonic.

FOXY LOXY: (babbles incoherently)

NARRATOR: Chicken Little, Henny Penny, and Goosey Loosey ran away, thankful that they had not been devoured.

However, the family of Foxy Loxy caught up with them. In addition to suing the manufacturer of the oven door on behalf of Foxy Loxy, the family brought suit against the three barnyard fowl: Chicken Little, Henny Penny and Goosey Loosey, claiming entrapment, reckless endangerment, and fraud. The family sought payment for pain and suffering, compensatory damages, punitive damages, disability and disfigurement, long-term care, mental anguish, impaired earning power, loss of esteem, and the loss of a good dinner.

The three birds later brought a countersuit, and they’ve all been battling in court from that day to this.
```

---

## IC-1996: The Child in the Grave

- Title: The Child in the Grave
- Author (byline): Hans Christian Andersen
- Work: The Complete Hans Christian Andersen Fairy Tales
- Publisher: Gramercy
- Publication date as stated: May 1993
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1769
- Already set (do not supply): none

### Source block (context only)

```text
Author: Hans Christian Andersen
Book: The Complete Hans Christian Andersen Fairy
Tales
ISBN: 978-0517092910
Publisher: Gramercy
Date (Month/Year): May 1993
```

### Introduction (context only: never use it for content warnings)

```text
The Child in the Grave by Hans Christian Andersen
```

### Performance text (classify this)

```text
It was a very sad day, and every heart in the house felt the deepest grief; for the youngest child, a boy of four years old, the joy and hope of his parents, was dead. Two daughters, the elder of whom was going to be confirmed, still remained: they were both good, charming girls; but the lost child always seems the dearest; and when it is youngest, and a son, it makes the trial still more heavy.

The sisters mourned as young hearts can mourn, and were especially grieved at the sight of their parents’ sorrow. The father’s heart was bowed down, but the mother sunk completely under the deep grief. Day and night she had attended to the sick child, nursing and carrying it in her bosom, as a part of herself. She could not realize the fact that the child was dead, and must be laid in a coffin to rest in the ground. She thought God could not take her darling little one from her; and when it did happen notwithstanding her hopes and her belief, and there could be no more doubt on the subject, she said in her feverish agony, “God does not know it. He has hard-hearted ministering spirits on earth, who do according to their own will, and heed not a mother’s prayers.” Thus in her great grief she fell away from her faith in God, and dark thoughts arose in her mind respecting death and a future state. She tried to believe that man was but dust, and that with his life all existence ended. But these doubts were no support to her, nothing on which she could rest, and she sunk into the fathomless depths of despair. In her darkest hours she ceased to weep, and thought not of the young daughters who were still left to her. The tears of her husband fell on her forehead, but she took no notice of him; her thoughts were with her dead child; her whole existence seemed wrapped up in the remembrances of the little one and of every innocent word it had uttered.

The day of the little child’s funeral came. For nights previously the mother had not slept, but in the morning twilight of this day she sunk from weariness into a deep sleep; in the mean time the coffin was carried into a distant room, and there nailed down, that she might not hear the blows of the hammer. When she awoke, and wanted to see her child, the husband, with tears, said, “We have closed the coffin; it was necessary to do so.”

“When God is so hard to me, how can I expect men to be better?” she said with groans and tears.

The coffin was carried to the grave, and the disconsolate mother sat with her young daughters. She looked at them, but she saw them not; for her thoughts were far away from the domestic hearth. She gave herself up to her grief, and it tossed her to and fro, as the sea tosses a ship without compass or rudder. So the day of the funeral passed away, and similar days followed, of dark, wearisome pain. With tearful eyes and mournful glances, the sorrowing daughters and the afflicted husband looked upon her who would not hear their words of comfort; and, indeed, what comforting words could they speak, when they were themselves so full of grief? It seemed as if she would never again know sleep, and yet it would have been her best friend, one who would have strengthened her body and poured peace into her soul. They at last persuaded her to lie down, and then she would lie as still as if she slept.

One night, when her husband listened, as he often did, to her breathing, he quite believed that she had at length found rest and relief in sleep. He folded his arms and prayed, and soon sunk himself into healthful sleep; therefore he did not notice that his wife arose, threw on her clothes, and glided silently from the house, to go where her thoughts constantly lingered—to the grave of her child. She passed through the garden, to a path across a field that led to the churchyard. No one saw her as she walked, nor did she see any one; for her eyes were fixed upon the one object of her wanderings. It was a lovely starlight night in the beginning of September, and the air was mild and still. She entered the churchyard, and stood by the little grave, which looked like a large nosegay of fragrant flowers. She sat down, and bent her head low over the grave, as if she could see her child through the earth that covered him—her little boy, whose smile was so vividly before her, and the gentle expression of whose eyes, even on his sick-bed, she could not forget. How full of meaning that glance had been, as she leaned over him, holding in hers the pale hand which he had no longer strength to raise! As she had sat by his little cot, so now she sat by his grave; and here she could weep freely, and her tears fell upon it.

“Thou wouldst gladly go down and be with thy child,” said a voice quite close to her,—a voice that sounded so deep and clear, that it went to her heart.

She looked up, and by her side stood a man wrapped in a black cloak, with a hood closely drawn over his face; but her keen glance could distinguish the face under the hood. It was stern, yet awakened confidence, and the eyes beamed with youthful radiance.

“Down to my child,” she repeated; and tones of despair and entreaty sounded in the words.

“Darest thou to follow me?” asked the form. “I am Death.”

She bowed her head in token of assent. Then suddenly it appeared as if all the stars were shining with the radiance of the full moon on the many-colored flowers that decked the grave. The earth that covered it was drawn back like a floating drapery. She sunk down, and the spectre covered her with a black cloak; night closed around her, the night of death. She sank deeper than the spade of the sexton could penetrate, till the churchyard became a roof above her. Then the cloak was removed, and she found herself in a large hall, of wide-spreading dimensions, in which there was a subdued light, like twilight, reigning, and in a moment her child appeared before her, smiling, and more beautiful than ever; with a silent cry she pressed him to her heart. A glorious strain of music sounded—now distant, now near. Never had she listened to such tones as these; they came from beyond a large dark curtain which separated the regions of death from the land of eternity.

“My sweet, darling mother,” she heard the child say. It was the well-known, beloved voice; and kiss followed kiss, in boundless delight. Then the child pointed to the dark curtain. “There is nothing so beautiful on earth as it is here. Mother, do you not see them all? Oh, it is happiness indeed.”

But the mother saw nothing of what the child pointed out, only the dark curtain. She looked with earthly eyes, and could not see as the child saw,—he whom God has called to be with Himself. She could hear the sounds of music, but she heard not the words, the Word in which she was to trust.

“I can fly now, mother,” said the child; “I can fly with other happy children into the presence of the Almighty. I would fain fly away now; but if you weep for me as you are weeping now, you may never see me again. And yet I would go so gladly. May I not fly away? And you will come to me soon, will you not, dear mother?”

“Oh, stay, stay!” implored the mother; “only one moment more; only once more, that I may look upon thee, and kiss thee, and press thee to my heart.”

Then she kissed and fondled her child. Suddenly her name was called from above; what could it mean? her name uttered in a plaintive voice.

“Hearest thou?” said the child. “It is my father who calls thee.” And in a few moments deep sighs were heard, as of children weeping. “They are my sisters,” said the child. “Mother, surely you have not forgotten them.”

And then she remembered those she left behind, and a great terror came over her. She looked around her at the dark night. Dim forms flitted by. She seemed to recognize some of them, as they floated through the regions of death towards the dark curtain, where they vanished. Would her husband and her daughters flit past? No; their sighs and lamentations still sounded from above; and she had nearly forgotten them, for the sake of him who was dead.

“Mother, now the bells of heaven are ringing,” said the child; “mother, the sun is going to rise.”

An overpowering light streamed in upon her, the child had vanished, and she was being borne upwards. All around her became cold; she lifted her head, and saw that she was lying in the churchyard, on the grave of her child. The Lord, in a dream, had been a guide to her feet and a light to her spirit. She bowed her knees, and prayed for forgiveness. She had wished to keep back a soul from its immortal flight; she had forgotten her duties towards the living who were left her. And when she had offered this prayer, her heart felt lighter. The sun burst forth, over her head a little bird carolled his song, and the church-bells sounded for the early service. Everything around her seemed holy, and her heart was chastened. She acknowledged the goodness of God, she acknowledged the duties she had to perform, and eagerly she returned home. She bent over her husband, who still slept; her warm, devoted kiss awakened him, and words of heartfelt love fell from the lips of both. Now she was gentle and strong as a wife can be; and from her lips came the words of faith: “Whatever He doeth is right and best.”

Then her husband asked, “From whence hast thou all at once derived such strength and comforting faith?”

And as she kissed him and her children, she said, “It came from God, through my child in the grave.”
```

---

## IC-1997: The Child-Martyr

- Title: The Child-Martyr
- Author (byline): Joyce Carol Oates
- Work: The Fabulous Beasts
- Publisher: Louisiana State University Press
- Publication date as stated: 1975
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1203
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joyce Carol Oates
Book: The Fabulous Beasts
ISBN: 978-0807101537
Publisher: Louisiana State University Press
Date (Month/Year): 1975
```

### Introduction (context only: never use it for content warnings)

```text
The Orthodox Church is filled with accounts of courageous Christians who, throughout the ages, have witnessed their faith—not only in word but, most memorably, in deed. There are accounts of the “Child Martyrs” who take our breath away. We are humbled by these tiny ones who possessed more courage and conviction than most of us are able to relate to. Enter the silence of a Roman Catholic church with me. Surrounding us are the intricate stained-glass depictions of a variety of saints. The one that draws the most attention is that of The Child-Martyr – Can you imagine his thoughts; his perceptions in the stillness. Listen closely and you can almost hear him speak. The Child- Martyr by Joyce Carol Oates.
```

### Performance text (classify this)

```text
Not white-faced, exactly, but sour-cream-colored, a vicious color, so that his eyes-heavily outlined in black-and his insipid mouth -- salmon-rosy -- were exaggerated. The contortions of the mouth were exaggerated too. It must have been a mistake, but the parted lips revealed no teeth, only that absurd leadish black.

In glassy perfection, around him, were an aquatic blue and rosy-beige and a yellow too sullen with browns to represent sunshine, and of course a repetition of the unearthly white of his face. And the black. In the usual winter drizzle all colors looked sullen. But when the Ideal slipped into position behind the Real all went vivid, and for an instant his original martyrdom was evoked in that thrill of ecstatic pain: only the too-thick black panels between the pieces of glass reminded one of earth, of weighty metals.

In the melodrama of an audience's pity (a small audience-usually women, usually old women) the grimace tightened; the slits of eyes seemed to shriek. It had been a habit, a long habit. It must have been a dream in the mind of whoever had put the window together. . . . One morning, however, the Child-Martyr allowed the grimace to twitch only on the right side of his mouth, the left remaining frozen. Did anyone notice. . . ? And one day he allowed the lips' natural desire to scream in church an inch or two of freedom, only two-dimensional, only visual: a nasty grin.

No more than three feet high, the Child-Martyr enjoyed a certain magnification because of an accident in the structure of the building. Located near the back pews, his window faced out on pavement; some of the other windows had become shaded, over the years, by oaks. So he enjoyed more sunshine. And the odor of damp and piety aided him because a child was out of place in this setting, one's sympathies were evoked at once. . . it was like discovering the skeleton of a kitten in an old cellar, with an earthen floor.

Though it was clear from the very first that the Child-Martyr was shifting inside the brute lead outlines, no one dared notice. There was a tradition of tear droplets, a tradition of stigmata, bloodstains and streaks exactly the color of real blood and drying even to the color of real blood. But the Child-Martyr was too young for tradition, or too stunted in his growth-his legs had been hurriedly and clumsily fashioned, tucked out of sight-for this alone he would never forgive the artisan who had pieced him together! He was poised up there, as if ready to spring. Fully awake and yet pretending to be asleep, but not with the grace of a respectful pretense, with a deliberately coarse pretense. . . an insult to his worshipers.

Of course they were not "his" alone; they rotated their worship from day to day, and on special private occasions, on occasions that involved tears and a mute terrible shaking of the head, they went to special windows, often to his. He did not mind sharing them. As time passed he longed to be less attractive, he did not at all mind the days no one prayed to him. . . . But it wasn't until he began to stare rudely at them through his black-edged eyes that he discovered a way of driving some away. Cunning, sly, furious in that sourish-white face, he discovered at the same time a centuries-old delight, slumbering in him.

Ah, the virginal dreamy stupidity of cold glass! He wanted music, he wanted more space. He began to murmur, to groan. A gutteral murmur back in the throat, a mockery of chaste agony. . . a mockery of the chastity that always stared up at him, out of others' eyes. Who are you worshiping. . . ? Is this only a mirror? -He sensed, from the immediate response, the cringing, the bewilderment, the fear, the tics -he sensed, in triumph, in a joy he had not felt since the original martyrdom, that he was correct in that diagnosis. All along he had been a mirror. And now he was coming alive to protest the stupidity of his makers, his worshipers, his importance, his amateurishly assorted features, his own ordeal. That ordeal had been pleasurable, but this, in glass, in the dank cellarish air, this was a lie. -A low gutteral moan. Bestial and intelligent. Groping to become audible. Inquisitive. Am I. . . ? Am I becoming one of you. . . ? Language instead of glass, music instead of mute babyish screams. . . ?

For centuries he, like the others on the side walls, stared slantwise to the altar. . . out of the corner of their souls they envied that position, the fullest whining triumphant martyrdom. . . in gold, in emeralds and diamonds and paste-pale exquisite flesh. . . a halo that shone without fear of being comic. Centuries of envy and silence. Now the Child-Martyr's low chuckle shattered those centuries. Someone was to write incoherently of him, scribbling down words as if to dispel the original chaos: Evidently before the assumption of one's role in his story, evidently before, evidently all the possibilities are in the seed (seeds?), evidently. . . yes but how to . . . how to unhook (unlock?) them without, with, without causing tidal waves and earthquakes, without. . . with full respect for one's ancestors and the Inquisition in the Marketplace. . .. But he ripped all this up. He prayed to the Child-Martyr to be delivered of his own madness. And yet again he found himself writing: ... before the beginning of history itself, before it, before it pieces the shards together. .. But what? What came before? What was it, where did it go, why is it lost, why is it now a nasty gap-mouthed grin? He ripped the pages up, prayed elsewhere with his rosary wrapped so tightly about his knuckles that the flesh showed the marks of the smooth black beads. Am I. . . ? Am I becoming human. . . ? Am I becoming God. . . ?

God awakening in him made him childish and vicious and lopsided in his grinning-naturally he must mock, after such an eternity of fraudulent suffering! Whose fault is it, sneers the Child-Martyr, who invented all this martyrdom? Rolling his eyes back in his head he caught sight one day of the insipid halo floating three or four inches above him, in utter sky-blue virginity, and for an instant he wondered-with the terrible clarity of the child-if, all along, someone had been mocking him anyway. But the instant passed. No, too good to have been true! And the ironies accumulate, the insulting histrionic groans move toward language. -nearly audible?

He has a dread of the immediate future: of whispers that grow to exclamations and public prayers and public adorations, of a new excited worship of that old fraudulent martyrdom. Famous, must he become famous and martyred once again, so that no one will hear the sly innuendos in the moans, no one will smash the mirror and free him? Another possibility, which terrifies him even more, is that they will seize upon the parody and stumble away with it, stunned and giggling with it, and the original pain-so real, so exquisite!-will be totally lost. Still, he writhes into life. Evidently it is his fate.
```

---

## IC-1998: Chomp

- Title: Chomp
- Author (byline): Carl Hiaasen
- Work: Not specified
- Publisher: Yearling
- Publication date as stated: March 2020
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: RAVEN, NARRATOR, DEREK, WAHOO, MICKEY, DIRECTOR, FROM THE TAPE, SECRETARY, SICKLER, CATERER
- Teaser before the introduction: Yes
- Spoken words (computed): 1251
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carl Hiaasen
ISBN: 978-0593177662
Publisher: Yearling
Date (Month/Year): March 2020
```

### Introduction (context only: never use it for content warnings)

```text
Are you a fan of survival-skills TV or wildlife documentaries? Shows like Naked and Afraid and Steve Irwin’s Crocodile Hunter have nothing on this reality TV show - Expedition Survival! Wahoo Cray and his father Mickey, a professional animal wrangler, are hired to manage the wildlife. Filming begins in Mickey’s homemade swamp, where the reckless Badger ignores Mickey’s warnings and ends up atop a thrashing, angry alligator. When the footage turns out better than anyone expects, Badger orders filming moved to the Everglades to put the real back in reality TV.

Chomp by Carl Hiaasen
```

### Performance text (classify this)

```text
RAVEN: (knocks on door, it is opened by Wahoo – freeze frame)

NARRATOR: (Pg 12) [That woman] with a shining stack of red hair is Raven Stark.

RAVEN: (with a strong accent) I’m Derek Badger’s production assistant. I brought your contract. (Pg 14) One thousand a day, plus location fees and animal rentals. (Pg 15) Where are your pythons? Derek wants a beast. (Derek steps in)

NARRATOR: (Pg 11) Derek Badger - the star of Expedition Survival! (Derek fist pumps to the audience) Every week, Derek parachutes into some gnarly wilderness teeming with fierce animals, venomous snakes and disease-carrying insects. Armed with only a Swiss army knife and a straw, he hikes, climbs, crawls, paddles or swims back to civilization. Along the way, he eats bugs, rodents, even worms—the grosser it looks, the happier Derek Badger is to stuff it into his cheeks. (Derek smiles winningly at the audience, then picks a bug leg from his teeth)

DEREK: (Pg 31) (with an obviously fake Australian accent) Take me to your alligator. Chop Chop!

RAVEN: (Pg 16) (whistles) That’s a monster, eh?

WAHOO: Twelve feet

MICKEY: (Pg 33) (proudly) Six hundred and twenty pounds. (Pg 75) Alice is her name.

DEREK: (Pg 32) She’s perfect! (to Raven) (Pg 38-39) But we can’t stage our biggest scene in some nitwit’s backyard.

RAVEN: It looks like a real-life swamp. You’ll be impressed.

DEREK: No, they’ll be impressed when they see me jump that monster gator.

RAVEN: Not happening. The insurance company says no way.

DEREK: They said the same thing about the cobra dance, but I did it anyway.

NARRATOR: They had been shooting Expedition Survival! in Cambodia when Derek decided to play snake charmer with a spitting cobra that had been rented from a local handler. Mr. Na leaped between Derek and the dangerous reptile just as it released a jet of deadly poison. A few drops landed in Mr. Na’s hair, and as a precaution he rushed off to take a shower. Upon returning to the set was dismayed to learn that Derek had chopped up his pet snake with a rusty machete and eaten it in the program’s final scene. *******

NARRATOR: (Pg 43-44) [The next day] Wahoo and his father uncoiled the python, Beulah and laid her out at full length. The script called for Derek to creep up and seize Beulah behind her head, instigating a fake life-or-death struggle.

DIRECTOR: (airhorn blows) Episode 103 – Expedition Survival! Action!

DEREK: (Pg 44-46) (whispering dramatically into a microphone on his shirt collar as he sneaks up on Beulah) “As if the Everglades weren’t dangerous enough, in recent years this tropical river of grass has been invaded by lethal predators from another continent— Burmese pythons! They can swallow a whole deer, a panther and, yes, even a human being. Look! There she is!” (pounces with a triumphant cry and grabs Beulah 2 feet below her head) “I’ve got her! I’ve caught the beast! (grunting and huffing he ‘struggles’ with the docile Beulah – it’s like fluffing a pillow)

DIRECTOR: Cut! Cut!

DEREK: (Pg 47) (lurching to his feet – he slams the python to the ground and confronts Mickey) That’s the worst excuse for a python I ever saw! You call that a snake? Ha! I call it an overstuffed earthworm. (disgusted with this scene, he moves on) What about the gator?

WAHOO: (Pg 52) Showtime!

DIRECTOR: (Pg 44) (airhorn blows) Episode 103 – Expedition Survival! Action!

NARRATOR: (Pg 60) Wahoo and his father peeked over the cameraman’s shoulder. The screen showed a view from the submerged camera. And there was Alice.

MICKEY: She won’t touch him. Not on a full belly.

DEREK: (Pg 58-59) (to crew) No mistakes! (he slips into the pond up to his neck - to camera) “Soon the sun will be setting over the Everglades. I must swim across this deep, murky pond to reach dry ground. Getting across this water is absolutely crucial to my survival but I’ve discovered fresh signs of an extremely large alligator, and I mean HUGE, lurking close by! If that monster were to attack me right now, the only chance I’d have of escaping alive would be to fight back ferociously, desperately, and gouge it in the eyes.”

WAHOO: (Pg 65) She’s coming up! Don’t move!

NARRATOR: (Pg 64) Slowly but surely, Alice was rising from the bottom of the pool.

DEREK: (Alice comes up underneath Derek; suddenly he is straddling her like a tipsy cowboy on a bronco) (Pg 66) Wooo-hooo! (hollering idiotically – he grabs her scales to hold on)

RAVEN: Oh, Lord. (Pg 68) (shrieking) Shoot it! Shoot it! Shoot that thing!

DEREK: (Pg 66) Wooo-hooo!

NARRATOR: (Pg 67) Members of the Crocodilia order of reptiles don’t buck like horses do when shedding an unwanted rider. Instead, they thrash and spin. Derek managed to hang on for three full revolutions before being launched airborne. (watch Derek’s arc through the air -- Splash!) *****later that night*****

DIRECTOR: (Pg 71) I brought something to show you

(holding up a disk) The pond scene. (puts the disk into a DVD player)

RAVEN: Let’s get this over with. (They watch becoming more excited)

FROM THE TAPE: (Pg 66) Wooo-hooo!

DIRECTOR: (Pg 72) Well?

DEREK: That was bloody. . . brilliant! (punches the air jubilantly with both fists) I almost died, didn’t I? That vicious monster almost killed me! (Pg 75-76) The most extraordinary 33 seconds of footage in the history of Expedition Survival! (Pg 86) (dreamily) The rest of the show must all build up to this incredible, heart-stopping moment. We’ll spare no expense!

MICKEY: (Pg 76) But you almost got drowned.

DEREK: Exactly! And the best part is it was real! We’re hiring you to lead us into the Everglades to put finishing touches on this masterpiece!

MICKEY: (disappointed) (Pg 134) All due respect, Mr. Beaver, this ain’t my first rodeo. (Pg 76) You’re gonna fake the rest of it, same as you always do.

RAVEN: In our line of work, it’s known as ‘re-creating’ events for the camera.

DEREK: (Pg 87) No more faking it, mate. (Pg 86) No tame animals. This time we’re going totally raw and wild. (Pg 87) We’re putting the ‘real’ back in ‘reality.’ *****

NARRATOR: (Pg 89) Mickey Cray was surprised to learn that Derek Badger didn’t want any of his captive critters on location.

MICKEY: Seriously. The man almost got killed by the world’s laziest alligator!

RAVEN: (Pg 97-98) We cannot have a repeat of what happened with your alligator. We need Derek in one piece. He’s the whole franchise.

NARRATOR: (Pg 103) But Raven Stark’s request to base the program in Everglades National Park had been rejected. [They] informed Raven that, because of the earlier egg-robbing incident at Yellowstone, Derek Badger had been blackballed from the entire federal park system.

RAVEN: (on the phone) For how long?

SECRETARY: Eternity.

NARRATOR: The crew of Expedition Survival! was using Sickler’s Jungle Outpost and Juice Bar.

SICKLER: (waves to audience, thumbs up) (Pg 95) I just repainted the place!

(PG 40) [a rumpled assistant begins spraying Derek’s arms and legs. Derek cooperates, then closes his eyes and holds his breath as the assistant mists his face]

WAHOO: What is that stuff?

RAVEN: Spray-on tan.

MICKEY: What a poser!

DEREK: (Pg 52-53) So what am I supposed to eat to survive. For the show, I mean.

RAVEN: (applying make-up to Derek) The script calls for bullfrogs and crawdads.

DEREK: (dismissively) What else? I want something truly disgusting.

RAVEN: How about maggots?

CATERER: (Pg 149) (Off stage a piercing scream)

NARRATOR: One of the catering staff was hopping frenetically and pointing at a furry, twitching intruder that lay quivering on the cake platter.

DEREK: (strides over to the table to examine it – he grins) Just as I suspected – a bat! (he licks his lips) Let’s do this! Set up some lights!

DIRECTOR: (Pg 44) (with little enthusiasm) Episode 103 – Expedition Survival! (Pg 133) Action!

DEREK: (Pg 155-157) (to camera) Deep in the Everglades, the swamp is unforgiving and food is scarce. Survival means eating whatever you can get your hands on. But by sheer luck, the violent weather has literally dropped on my platter a tasty morsel that will provide enough nutrition to get me through another brutal day in this tropical wilderness. Look! (dangles the bat by its tail) Unfortunately, the rain has soaked all the tinder, so I can’t make a fire for cooking. That leaves me only one choice. Now, please don’t try this yourself—wild bats can be vicious, and their teeth are needle sharp. Remember, I’m an experienced survivalist. I know how to handle these unpredictable rascals. . . (he tilts his head back and dramatically begins to lower the bat into his mouth)

NARRATOR: (as Derek pantomimes) The bat wasn’t vicious. She simply didn’t want to be eaten. She reacted defensively and without hesitation and chomped down on the first chompable target. (Derek screams) Which happened to be Derek’s plump tongue.

DIRECTOR: (Pg 159) Zoom in for a close-up! Hurry! (but Derek runs, still screaming into the swamp) ****** days later Derek hiding in the swamp*****

DEREK: (Pg 266) (Using his cell phone to film himself – his speech is distorted due to a swollen tongue) My harrowing Everglades adventure is finally drawing to an end, and not a moment too soon. I’m completely out of food, out of water and dangerously weak after being attacked by a rare but deadly vampire bat. Its savage bite left me dazed and delirious, racked with fever. Why, at times I even imagined myself morphing into a real-life vampire!

NARRATOR: (Pg 168) It would be a humongous night for the show’s TV ratings if Derek Badger failed to survive one of his survival expeditions!

RAVEN: (to audience, almost cheerfully) It’s possible the bat had rabies. Derek could be losing his mind.

DEREK: (Pg 115) (desperately paranoid and scared) Time is running out. [When] the sun goes down, the predators come out – alligators, panthers, bears, pythons. (Pg 186) My only hope is that somebody finds me way out here before it’s too late . . .

NARRATOR: [*Turn in next time for the chilling conclusion of] Episode 103 – Expedition Survival!

(*bracketed words have been added as a transitional ending – not in the original novel)
```

---

## IC-1999: Civil Twilight

- Title: Civil Twilight
- Author (byline): Chuck Palahniuk
- Work: Haunted: A Novel
- Publisher: Anchor
- Publication date as stated: April 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1639
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chuck Palahniuk
Book: Haunted: A Novel
ISBN: 978-1400032822
Publisher: Anchor
Date (Month/Year): April 2006
```

### Introduction (context only: never use it for content warnings)

```text
Those who study our enduring fascination with monsters often point out several reasons for the lure of such fantastic beings.

Monsters represent the ultimate “other.” They’re a safe way to pretend that evil is less human than it usually is . . . they reinforce the comforting fantasy that you can instantly tell who’s good and who’s bad. In real life, of course, it’s hardly ever that simple.

And although adults may no longer be afraid of the dark, they are, and should be, afraid of the monsters that often inhabit it . . . Chuck Palahniuk extends the darkness to a period called “civil twilight.” Civil twilight is the period of time between sunset and when the sun is more than six degrees below the horizon. That six degrees equals about half an hour. And it is during this time that the adult monster of this story stalks his or her prey.

Civil Twilight by Chuck Palahniuk.
```

### Performance text (classify this)

```text
It was the summer people quit complaining about the price of gasoline.

On June 24, sunset was at 8:35. Civil twilight ended at 9:07. A woman, walking uphill on the steep stretch of Lewis Street, heard a pounding sound. It was the sound a pile driver might make, a heavy stomping sound every few seconds, getting louder with each stomp, getting closer. Somewhere in the dark between streetlights, something glass broke.. A newspaper box blew over sideways, crashing into the street. The crash came again and the windows blew out of a glass telephone booth only three parked cars away from where she stood and then the lights went out.

The street was dark.. A mailbox, bolted to the curb, it boomed loud as a cannon, then stood shaking, vibrating, dented and leaning to one side. A wooden utility pole shuddered, the cables draped across it rattling against each other, the sparks sprinkling down, bright summer fireworks. Then nothing. Nothing happened. Nothing had gone by in the dark street.

On July 1, people were complaining about the water shortage. They were griping about city budget cuts and all the police getting laid off. Car prowls were on the rise. Spray-paint tagging and armed robbery.

On July 2, they weren’t. On July 2, a woman walking her dog found the body of Lorenzo Curdy, the side of his face caved in. Dead. The moment before he was hit, the man must’ve felt something, maybe the rush of air, because he put his hands up in front of his face. When they found him, both hands were buried, punched so deep in his face his fingernails had dug into his own crushed brain.

On a street, the moment you’re between streetlights, there in the dark you’d hear it. The stomp. You might hear a second sound from closer, somewhere nearby, or, worse, the next victim would be you. People heard it coming, once, twice, closer, and they froze. Or they forced their feet, left, right, left, three or four steps into a close-by doorway. They crouched, cowering next to parked cars. Closer, the next stomp came. It was coming down the street, sounding closer, getting loud and gaining speed. In the pitch-dark it would hit— bam—a bolt of black lightning.

On July 13, sunset at 8:33 with civil twilight over at 9:03, a woman named Angela Davis had just left work at a dry cleaner’s on Center Street when nothing hit her square in the middle of her back, breaking her spine so hard it lifted her out of her shoes.

On July 17, when civil twilight ended at 9:01, a man named Glenn Jacobs stepped off a bus.. What nobody saw, slammed into him so hard his ribcage collapsed. His chest punched in the way you’d crush a wicker basket.

July 25, civil twilight ended at 8:55. Mary Leah Stanek was last seen jogging along Union Street. She stopped to tie one tennis shoe and check her pulse against her wristwatch. Stanek pulled off the baseball cap she wore. She turned it backward and put it back on, tucking her long brown hair up under it. She headed west on Pacific Street, and then she was dead. Her face torn loose from the skull and muscle underneath.

What killed Stanek, was wiped clean of fingerprints. Clotted with blood and hair. They found the murder weapon wedged under a parked car down along 2nd Avenue. It was a bowling ball, the police reported. Those smudged, greasy-black bowling balls, you can buy them at any thrift shop for half a buck..

The police held a press conference. They stood in a parking lot and someone threw a bowling ball down, threw it hard against the concrete. And the ball bounced. It made the sound of a pile driver far away. It bounced high, taller than the man who threw it. It didn’t leave a mark, and if the sidewalk were sloped, the police said, it would keep going, bouncing higher, faster, bouncing downhill in long strides.

The city council pushed for a law to paint all balls bright pink. Or neon yellow, orange, or green, some color you could see flying at your face down a dark side street late at night. To give people just a moment to dodge before—blam—their face is gone. City fathers pushed for a law to make owning black balls a crime.

The bowling ball was a police cover-up, people said. The bowling ball was a red herring. A monster wannabe. The bowling ball was a quick fix to keep everybody calm.

On July 31, the sun was six degrees under the horizon at 8:49. That night, Darryl Earl Fitzhugh was homeless, sleeping on Western Avenue. when his chest was crushed, both his lungs collapsed, and his heart muscle ruptured.

According to one witness, the killer came out of the bay, dragging itself over the lip of the seawall. Another witness saw the monster, dripping ooze, squeezing up from the storm sewer. These same people said the forensic evidence was consistent with a hard backhanded slap from a giant lizard walking on its hind legs. The ribcage collapsed was sure proof the victim was stepped on by some dinosaur throwback. Something dashed past, other people said, something low to the ground, too fast to be an animal. Or it was a maniac run amok with a fifty-pound sledgehammer. One witness said we were being “smote” by God from the Old Testament.

Everyone saw something different. . . . people need a monster they can believe in. A true and horrible enemy. A demon to define themselves against. Otherwise, it’s just us versus us.

See . . . all day long our biggest enemy is other people. It’s people packed around us in traffic. People ahead of us in line at the supermarket. It’s the supermarket checkers who hate us for keeping them so busy. People didn’t want this killer to be another human being. But they wanted people to die. What people wanted was a sacrifice every few days, something to throw in the volcano. Our regular offering to random fate.

Of course, there was a hero. By accident, August 2, sunset at 8:34, a twenty-seven-year-old named Maria Alvarez was leaving a hotel where she worked as the night auditor. She stood on the curb, stopped to light a cigarette when a man pulled her back. That same instant, the monster rushed past. This man had saved her life. The city applauded on television, but in their hearts, they hated him.

What’s important is, the crime rate went down. In times like that, every man is a suspect. Every woman, a potential victim.

Public attention went this same way during the White Chapel Murders of Jack the Ripper. For those hundred days, the murder rate dropped 94 percent. Burglaries dropped by 85 percent. Assault by 70 percent. Nobody wanted to be the next victim of the Ripper. People locked their windows. More important, nobody wanted to be accused of being the killer. People didn’t walk out at night.

During the Atlanta Child Murders, while thirty kids were strangled, tied to trees, and stabbed, beaten, and shot, most of the city lived in security and safety they’d never known.

During the New Orleans Ax Man Murders, the killer wrote the local newspaper, theTimes-Picayune. On the night of March 19, the killer promised to kill no one in a house where he could hear jazz music. That night, New Orleans was roaring with music, and no one was killed.

During these waves of murder, all crime dropped in each city. In a city with a limited police budget a high-profile serial killer is an effective means of behavior modification.

With the shadow of this horrible bogeyman, with it stalking the streets downtown, nobody beefed about the unemployment rate. The water shortage. The traffic. With the angel of death going door to door, people stayed together. They behaved.

How it ended is, one night the monster got a dog. A hairy rag of a little dog on the end of a leash, tied to a parking meter on Porter Street, it stood and barked as the pounding came closer. The closer the sound came, the more the dog barked. A store window webbed into a puzzle of broken glass. A fire hydrant clanked to one side, cracked cast iron, hissing a white curtain of water. The edge of a windowsill explodes in a spray of gravel and concrete dust. One more stomp and the barking stopped.

The monster seemed to disappear after that night. A week went by, and the streets were still empty after dark. A month went by, and the editors found some new horror to put on the front page of the newspaper. A war somewhere else. Some new kind of cancer.

On September 10, sunset was at 8:02. Curtis Hammond was leaving a group-therapy session he attended every week at 257 West Mill Street. He was pulling down the knot of his tie when it happened. He’d just opened his collar button. It was when he’d just turned to look up the street. He smiled at the warm air on his face, shut his eyes, and breathed in through his nose. A month before, everyone in town knew him from the front page of the paper. From the television news. He’d pulled a night auditor away from getting killed by the monster. From getting smote by God. He was the hero we didn’t want.

On September 10, civil twilight was at 8:34, and a moment later, Curtis Hammond turned toward a noise. His tie loose, he squinted into the dark. Smiling, his teeth shining, he said, “Hello?”
```

---

## IC-2000: Clash of the Titanic

- Title: Clash of the Titanic
- Author (byline): Eric D. Snider
- Work: Snide Remarks ASIN: B000REH4ZS (available through Amazon.com)
- Publisher: Eric D. Snider
- Publication date as stated: January 1998
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, KATE WINSLET, KATE’S WEASELLY FIANCE, KATE, LEONARDO DICAPRIO, LEONARDO, WEASELLY FIANCE, AUDIENCE, FIRST MATE, CAPTAIN, ICEBERG
- Teaser before the introduction: Yes
- Spoken words (computed): 900
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric D. Snider
Newspaper: 1st Published in the Brigham Young
University Newspaper, The Daily Universe,
February 9, 1998
Website: Now available at
https://www.ericdsnider.com/snide/clash-of-the-titanic/
Snide Remarks #26
ISBN: N/A
Publisher: Brigham Young University Press / Eric D
Snider.com
Date: February 9, 1998
Also Published in
Author: Eric D. Snider
Book: Snide Remarks
ASIN: B000REH4ZS (available through Amazon.com)
Publisher: Eric D. Snider
Date: January 1998
```

### Introduction (context only: never use it for content warnings)

```text
Clash of the Titanic by Eric D. Snider
```

### Performance text (classify this)

```text
NARRATOR: Many of you have seen the film “Titanic,” which is about a great big boat that sank like a thousand years ago that for some reason everyone is just now getting worked up about. Some of you—I am speaking to the women here—have seen this movie several times. And I would like to know why. You think there’s a chance the movie will end differently if you see it again? Do you think this is a “Choose Your Own Adventure” movie? It’s NOT! No matter how many times you see it, the boat is going to sink, and the same people are going to die. This movie is entirely too long. The actual sinking of the Titanic took only four hours; the movie is easily three times that long. [So] as a public service, [we are] offering this much-shortened screenplay . . .

(Scene 1)

KATE WINSLET: Why, this is a fancy boat, isn't it?

KATE’S WEASELLY FIANCE: Yes, it certainly is. Here is the art you asked for. It is by an artist named "Picasso." I am certain he will amount to nothing.

KATE: Ha ha ha. That is very funny to our audience, because of course Picasso later amounted to quite a bit, after this boat sank.

LEONARDO DICAPRIO: Hello, I'm Leonardo DiCaprio. Perhaps you have seen the many Internet sites dedicated to the worship of me. You are very pretty.

KATE: Thank you. So are you.

LEONARDO: I know. Prettier than you, in fact. I am going to put on my "brooding" face now, to ensure that women will keep coming back again and again to see this movie. Later, my white shirt will be soaking wet.

KATE: While you're doing that, I will concentrate on standing here and looking pretty, to keep the men in the audience interested until the boat sinks and people start dying.

WEASELLY FIANCE: Excuse me. I do not like you, Leonardo, even though you saved my fiancée's life. I am going to sneer at you and treat you like dirt because you're poor, and then I'll probably be physically abusive to my fiancée, and then, just to make sure the audience really hates me, and to make sure my character is entirely one-dimensional, perhaps I'll throw an elderly person into the water.

AUDIENCE: Boo! We hate you! Even though all real people have at least a few admirable qualities, we have not been shown any of yours, and plus, you're trying to come between Leonardo and Kate, and so therefore we hate you! Boo! (Even though technically it is Leonardo who is coming between you and Kate. But Leonardo is handsomer than you, even though he is only 13, so we are on his side. Boo!)

(Scene 2)

LEONARDO: I'm glad we snuck away like this so that you could cheat on your fiancé.

KATE: So am I. Even though I am engaged to him and have made a commitment to marry him, that is no reason why you and I cannot climb into the back seat of a car and steam up the windows together. The fact that I am the heroine of the movie will no doubt help the cattle-like audience forgive me of this, though they would probably be VERY angry indeed if my fiancé were to do the same thing to me.

AUDIENCE: Darn straight, we would! Moo! We mean, Boo!

LEONARDO: I agree. First, I would like to draw you, though, so of course you have to take off all your clothes.

KATE: But can a movie with five minutes of continuous nudity be at all successful in, say, Provo, Utah, where the audiences might not stand for that sort of thing?

LEONARDO: I would be willing to bet that for the first three weeks the film is in release, every single showing at the Wynnsong Theater in Provo will sell out.

NARRATOR: According to Wynnsong manager Matt Palmer, that is exactly what happened.

KATE: All right, then. (sound of clothes hitting the floor)

(Scene 3)

FIRST MATE: Captain, we're about to hit an iceberg!

CAPTAIN: Great, I could use some ice for my drink. (sound of drinking)

ICEBERG: (hits boat)

FIRST MATE: That can't be good.

CAPTAIN: Bottoms up!

AUDIENCE: Huh?

FIRST MATE: That was irony, you fools.

AUDIENCE: Baa! Moo! Where's Leonardo?

(Scene 4)

LEONARDO: I have been informed that this boat is sinking.

KATE: That is terrible.

LEONARDO: Would you like to engage in some more immoral-but-justified behavior?

KATE: Certainly.

AUDIENCE: Boo! Boo!

WEASELLY FIANCE: (aside) I'm getting the raw end of the deal here. (to Leonardo) Listen, Leonardo, to cement my morally-dubious-yet-somehow-less-annoying-than-you personality, I am going to handcuff you to this pipe, here in a room that will soon be filling with water, due to the fact that we are sinking, which I believe has been mentioned previously.

LEONARDO: Why don't you just shoot me?

WEASELLY FIANCE: Because then you wouldn't be able to escape and save Kate from me. Of course, you're going to die anyway --

AUDIENCE: Don't spoil it for us! Booooooo!!

LEONARDO: He's right, though. I am doomed.

AUDIENCE: Aww, look how cute he is when he's doomed!

WEASELLY FIANCE: I hate you people.

(Scene 5) 150-YEAR-OLD-KATE: And that's when Leonardo rescued me from my evil fiancé and helped me float on a board in the water. Of course, if it hadn't been for having to rescue HIM, I could have gotten on an actual lifeboat, and frozen my legs nearly off. Anyway, he's pretty much dead now, and I'm well over a thousand years old, and who's making my supper? I need a bath. Turn down that Enya music, it's making my ears hurt. You kids today, with your loud music. Why, when I was -- hey! Don't you walk away from me, Mr. Snooty-Patootie! I'd turn you over my knee, if I had one. I'll beat you in the head with this huge diamond! Come back here!

(FADE TO BLACK; roll credits; annoying Celine Dion song [Hum theme from Titanic])
```
