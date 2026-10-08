# Classification request: batch 21 of 63 (40 records, IC-0801 to IC-0840)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-021-reply.json`.

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

## IC-0801: He’s Just Not That into You

- Title: He’s Just Not That into You
- Author (byline): Greg Behrendt and Liz Tuccillo
- Work: Not specified
- Publisher: Simon Spotlight Entertainment
- Publication date as stated: Sept 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS, ACTOR, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1300
- Already set (do not supply): none

### Source block (context only)

```text
Author: Greg Behrendt and Liz Ruccillo
ISBN: 978-0689874741
Publisher: Simon Spotlight Entertainment
Date (Month/Year): Sept 2004
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: For ages women have come together to analyze the puzzling behavior of men.

ACTOR: “He’s afraid to get hurt again.”

ACTRESS: “Maybe he’s intimidated by me.”

ACTOR: “He just got out of a relationship.”

ACTRESS: But no matter how many excuses for a dead-end relationship you try to make, the truth may be . . .

TOGETHER: He’s Just Not That into You

ACTOR: by Greg Behrendt and Liz Tuccillo
```

### Performance text (classify this)

```text
ACTRESS: (Pg 7) Hey. I know the guy you’re dating. Yeah, I do. He’s that guy that’s so tired from work, so stressed about the project he’s working on.

ACTOR: He’s just been through an awful breakup.

ACTRESS: He has trust issues.

ACTOR: Right now he has to focus on his career.

ACTRESS: He can’t get involved with anyone until he knows what his life is about.

ACTOR: As soon as it all calms down he’ll leave his wife, girlfriend, crappy job.

TOGETHER: God, he’s so complicated.

ACTRESS: He is a man made up entirely of your excuses.

ACTOR: And the minute you stop making excuses for him, he will completely disappear from your life.

ACTRESS: (Pg 23) He’s just not that into you if he’s not calling you – Men know how to use the phone.

ACTOR: Oh, sure, they say they’re busy. They say that they didn’t have even a moment in their insanely busy day to pick up the phone.

ACTRESS: Bulls***. With the advent of cell phone and speed dialing, it is almost impossible not to call you.

ACTOR: Sometimes I call people from my pants pocket when I don’t even mean to.

ACTRESS: (Pg 26-28) Dear Greg: I’m dating this guy who ends conversations saying he’ll call me. Like, “I’ll give you a call tomorrow.” And then he doesn’t. Should I read something into this? – Annie

ACTOR: Dear Call Waiting: Yes, you should read something into it. In fact the very something is . . “He’s just not that into you.” Most guys will say what they think you want to hear rather than nothing at all. Some guys are lying; some guys really mean it. Here’s how you can tell the difference: You know they mean it when they actually do what they said they were going to do. You should be dating a man who’s at least as good as his word.

ACTRESS: (Pg 29-30) Dear Greg: A guy who I’m going out with is totally important and totally busy. Sometimes when he’s working, I don’t hear from him for days and days. Some guys are just really, really busy! - Nikki

ACTOR: Dear Nikki: Really busy is another way to say “just not that into you.” Totally important is another way to say ,” you’re unimportant” To busy and important to ask you out or call you – what a catch. You must be the envy of every women he’s really dating.

ACTRESS: I’m about to make a wild, extreme, and severe relationship rule: The word “busy” is a load of crap and is most often used by a**holes.

ACTOR: The word “busy” is the relationship Weapon of Mass Destruction

ACTRESS: Men are never too busy to get what they want.

ACTOR: (Pg 36) He’s just not that into you if he’s not dating you: Hanging out is not dating!

ACTRESS: (Pg 39-40) Dear Greg: I’ve been dating a guy for six months. We see each other about every two week. I really like him, so I feel like it’s better than nothing. And you never know thing can change at any time. Maybe I should actually feel honored that he’s able to give me as much time as he does – He might actually really like me. – Lydia

ACTOR: Dear Better than Nothing: Really? Is better than nothing what we’re going for now? Have you lost your marbles? Why should you feel honored for getting scraps of his time. In my book, any guy who can wait two weeks to see you is just not that into you.

ACTRESS: (Pg 45) Better than nothing is not good enough for you!

ACTOR: (PG 59) He’s just not that into you if he cheats on you – There’s never going to be a good excuse for cheating.

ACTRESS: Some will argue that you shouldn’t throw away a meaningful relationship just because of one indiscretion.

ACTOR: And in case he tells you that it just “happened,” please remember, cheating doesn’t just “happen.”

ACTRESS: It’s not an accident as in, “Oops, I just slipped and fell.”

ACTOR: He is not only behaving like a man who’s just not that into you, he’s behaving like a man who doesn’t even like you all that much.

ACTRESS: (Pg 61-62) Dear Greg: I had been dating a guy for about two years, and I thought things were going really well. After he came home from a family visit, he told me [cheated on me] He told me I had put on some weight and therefore he wasn’t that attracted to me anymore. I have put on about 20 pounds. Should I break up with him or start going to the gym? -- Beth

ACTOR: Dear Twenty Pounds: I definitely think you should lose 175 pounds – in the form of your loser boyfriend. He just cheated on you and called you fat. Using your weight as an excuse for his cheating is not only mean, but simply not valid. And by the way, how’s he going to react if you grow older and get a few wrinkles? Or wear a color he doesn’t like?

ACTRESS: (Pg 63) NOTE: Pronouns changed from plural to singular. This last guy is good. He’s betrayed his relationship and humiliated his girlfriend. Then he tells her it’s all her fault.

ACTOR: Don’t let any man blame you for their infidelity. Ever!

ACTRESS: (PG 68) There is no excuse for cheating. Let me say it again. There is no excuse for cheating.

ACTOR: (Pg 93) He’s just not that into you if he’s breaking up with you.

ACTRESS: (Pg 98-99) Dear Greg: I have a boyfriend who keeps breaking up with me. He also keeps calling me and begging me to get back together. He’s done this three times now, every six month. I hate it, but I keep taking him back because I love him. He must be really into me if he keeps coming back, right? -- Christina

ACTOR: Dear Yo-Yo Champion: I’ll put money down that the breakup count isn’t over yet. Sadly, this is what that guy is doing during your relationship recess. He’s [looking] around for something better, and when he doesn’t find it, he gets lonely and comes “home. Reset your breakup maximum to one and move one.

ACTRESS: Just remember that the person you are getting back together with is the same person who, not long before, looked you in your beautiful face, took full stock of you and all your qualities, and told you that he was no longer in need of your company.

ACTOR: If aliens haven’t recently abducted your beloved and switched his brain for the brain of a guy who’s really into you,

ACTRESS: please consider the option that the bum maybe just got a little lonely.

ACTOR: (Pg 130) He’s just not that into you if he’s a selfish jerk

ACTRESS: (Pg 134) Dear Greg: I am dating a guy in medical school. He’s overworked, over tired and gets angry easily. He recently screamed at me because I was bothering him when he was in the middle of studying. I know that this is just temporary. And every once in a while he’ll feel bad and apologize and tell me how much pressure he’s under. He wasn’t like this in the beginning and I know the real guy is going to come back. Besides, I always wanted to marry a doctor! – Denise

ACTOR: Dear Old Yeller: I don’t care if he’s studying to become the next Messiah. There is no reason to yell at anyone ever, unless you are screaming

TOGETHER: “LOOK OUT FOR THAT BUS!”

ACTOR: And it’s not temporary. People who yell are people who think they’re entitled to yell. Don’t wait around for Mr. Hyde to turn back into Dr. Jekyll.

ACTRESS: (PG 145) You want to believe that you are better than all the crap you’ve been taking from all these men all these years?

ACTOR: Well you are. (Front cover) You’re a beautiful, smart, funny woman who deserves better. (Pg 148)

ACTRESS: Life is hard enough as it is without choosing someone difficult to share it with. (Front cover)

ACTOR: So . . . The next time you feel the need to start “figuring him out” consider the glorious thought that maybe . . .

TOGETHER: He’s just not that into you

ACTOR: and then go find the one who is.
```

---

## IC-0802: Hooway for Wodney Wat

- Title: Hooway for Wodney Wat
- Author (byline): Helen Lester
- Work: Not specified
- Publisher: Houghton Mifflin Company
- Publication date as stated: May 2002
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 2, TOGETHER, NARRATOR, WODNEY, CLASSMATE 1, CLASSMATE 2, CLASSMATE 3, NARRATOR 2, CAMILLA, MISS FUZZLEWORTH, VARIOIUS CLASSMATES
- Teaser before the introduction: Yes
- Spoken words (computed): 737
- Already set (do not supply): none

### Source block (context only)

```text
Author: Helen Lester
ISBN: 978-0618216123
Publisher: Houghton Mifflin Company
Date (Month/Year): May 2002
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Do kids have to "fit in" by dressing, acting and thinking like everyone else.

ACTOR 2: Let’s hear a resounding NO!

ACTOR 1: Hooway for Wodney Wat by Helen Lester explores the fear we all have about being different and encourages us to embrace our differences as advantages.
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Actor 1: Narrator, Classmate 1, Classmate 2, Classmate 3, Camilla Actor 2: Narrator 2, Wodney, Miss Fuzzleworth

ACTOR 2: Or as Rodney Rat would say “embwace or diffewences”

TOGETHER: Hooway for Wodeny Wat by Helen Letser.

NARRATOR: Poor Wodney.

WODNEY: Wodney Wat.

NARRATOR: His real name was Rodney Rat, but he couldn’t pronounce his r’s. To make matters worse, he was a rodent.

WODNEY: A wodent.

CLASSMATE 1: What’s your name, Wodney?

WODNEY: (whispers) Wodney Wat

CLASSMATE 2: What’s another name for bunny?

WODNEY: (mumbling) Wabbit.

CLASSMATE 3: (winking) And how does a train travel?

WODNEY: (miserabley) A twain twavels on twain twacks.

NARRATOR: All of this teasing day in and day out made Wodney the shyest rodent in his elementary school. His squeak could barely be heard in class.

WODNEY: (squeak)

NARRATOR: He gnawed lunch alone.

WODNEY: (demonstrate a rodent eating lunch)

NARRATOR: And while the other rodents scurried and scooted about at recess, Wodney hid inside his jacket.

WODNEY: (Demonstrate)

NARRATOR 2: Then one day as the rodents were taking turns doing wheelies, a new rodent – a very large rodent – barged into the classroom and announced:

CAMILLA: My name is Camilla Capybara. I’m bigger than any of you. I’m meaner than any of you and I’m smarter than any of you.

NARRATOR 2: And then she added

CAMILLA: So there.

NARRATOR 2: With that she accidentally-on-purpose elbowed an ear, bumped two noses, stepped on three tails, and lay down on a desk.

NARRATOR: Fur prickled in fear through the classroom. She sure was bigger than any of them. She sure looked meaner than any of them. Was she smarter than any of them?

MISS FUZZLEWORTH: What’s 2 + 2?

CAMILLA: (shouting) FOUR!

NARRATOR 2: Without even bothering to raise her paw.

CAMILLA: And furthermore, 4+4 is 8, 8+8 is 6 and 243 + 125 is 368.

NARRATOR 2: Later, when Miss Fuzzleworth asked

MISS FUZZLEWORTH: What’s the capital of . . . .

NARRATOR 2: Camilla interrupted

CAMILLA: New York, Albany, Population 295,594.

NARRATOR 2: And during science, in answer to the question

MISS FUZZLEWORTH: What part of a plant is blow the ground?

NARRATOR 2: Camilla Capybara danced on her desk and sang

CAMILLA: Root! Root! Rooty-toot-toot!

CLASSMATE 1: Yup

NARRATOR 2: thought all the other rodents

CLASSMATE 2: She’s smarter than we are, too.

NARRATOR 2: They felt very, very uncomfortable.

NARRATOR: Every afternoon, just before the final recess, Miss Fuzzleworth drew a name from her hat to see who would be the leader for their favorite game, Simon Says. She scrunched her eyes closed and jiggled the hat.

MISS FUZZLEWORTH: (demonstrate)

NARRATOR: Would it be Hairy Hamster?

NARRATOR 2: Minifeet Mouse?

NARRATOR: Grizzlefriz Guinea Pig?

NARRATOR 2: Could it be big, mean, smart Camilla Capybara?

NARRATOR: Miss Fuzzleworth’s paw reached in and pulled out the name of

MISS FUZZLEWORTH: . . . Wodney Wat!

NARRATOR: The bell rang, there was a wild scurry for the door, and Camilla Capybara was the first on the playground, having trampled the others in her path.

NARRATOR 2: To Wodney she looked especially scary. What would she do when she heard him speak?

NARRATOR: Breathe capybara breath in his face?

WODNEY: (Demonstrate/pantomime)

NARRATOR: Or tie him up in his own tail?

WODNEY: (Demonstrate/pantomime)

NARRATOR: Or even POUNCE on him?

WODNEY: (Demonstrate/pantomime)

NARRATOR: The tiny, trembling leader of the game stood before the eager players, his head well inside his jacket, and squeaked.

WODNEY: Wodney says wap your paws awound your head.”

NARRATOR: He peeked a little peek out of his jacket and saw

CAMILLA: (Demonstrate) WHAP! WHAP! WHAPPITY SLAPPITY WHAP!

NARRATOR 2: Camilla was whapping her paws around her head so hard she became dizzy, gave herself a headache, and had to sit down.

NARRATOR: The other rodents couldn’t help giggling.

WODNEY: Wodney says play Wing Awound the Wosey.

NARRATOR 2: Camilla put out her arms like wings and made an airplane noise

CAMILLA: Nnnnrrrr

NARRATOR 2: But where was the wosey? WHAT was a wosey?

CAMILLA: (Look frantically for a wosey)

NARRATOR 2: By now Wodney’s voice was stronger and his head was entirely out of his jacket.

WODNEY: Wake the leaves!

NARRATOR: Nobody moved.

WODNEY: Wodney says wake the leaves.

NARRATOR: While Hairy, Minifeet, and Grizzlefriz and the others busied themselves raking,

NARRATOR 2: Camilla Capybara grabbed one leaf.

CAMILLA: (yelling) Wake up!

NARRATOR 2: She snatched another

CAMILLA: (yelling) Come on, you. Up, up, up!

NARRATOR 2: And another

CAMILLA: Rise and shine

NARRATOR 2: And another

CAMILLA: BOO!

NARRATOR 2: By now all the other rodents were squealing with laughter

VARIOIUS CLASSMATES: (Squeal with laughter)

NARRATOR: All but Camilla, who frowned.

CAMILLA: Stupid leaves. They won’t wake up!”

NARRATOR 2: And why was everyone laughing at her? Such bullies!

NARRATOR: In a voice so strong he had to hold his own ears, Wodney called

WODNEY: Wodney says go west!

NARRATOR 2: The rodents collapsed in a happy heap for a rest

CAMILLA: Go west.

NARRATOR 2: Feeling very smart that she could tell directions by the sun said

CAMILLA: All right. I shall go west.

NARRATOR 2: And then she added

CAMILLA: So there.

NARRATOR: West she stomped.

NARRATOR 2: Forever.

NARRATOR: She was gone . . . And from that day on the pupils of PS 142 Elementary School for Rodents never teased Wodney again.

NARRATOR 2: He was their hero

TOGETHER: Hooway for Wodney Wat! Whoot! Whoot! Wooty-toot-toot!
```

---

## IC-0803: Horton Hatches the Egg

- Title: Horton Hatches the Egg
- Author (byline): Theo Geisel (aka Dr. Seuss)
- Work: Not specified
- Publisher: Random House
- Publication date as stated: Oct 1940
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR, ACTRESS, ACTRES
- Teaser before the introduction: Yes
- Spoken words (computed): 1529
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theo Geisel (aka Dr. Seuss)
ISBN: 978-0394800776
Publisher: Random House
Date (Month/Year): Oct 1940
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: The scene: a jungle. Meet Mayzie, the bird. She's bored and she's lazy. She's up in

a tree, in her nest, sitting on her egg. TOGETHER: Horton Hatches the Egg by Theo Geisel (aka Dr. Seuss)
```

### Performance text (classify this)

```text
ACTOR: You've met Horton, we're sure, in a story or two. Remember the time he heard him a Who?

ACTRESS: But before he was Who-ing, Horton was here Protecting an egg with the use of his rear.

ACTOR: While the little egg's mother, a birdie called Mayzie, Is up in Palm Beach getting all kinds of crazy.

ACTRESS: It seems like a sweet tale 'bout what love is for. But it might go much deeper, could it be about war?

ACTOR: Or maybe the story's about who has the right To parent a child in a custody fight.

ACTRESS: No matter the moral, it's certainly clear That there's more than just birdies and elephants here.

ACTOR: Sighed Mayzie, a lazy bird hatching an egg:

ACTRESS: “I’m tired and I’m bored
And I’ve kinks in my leg
From sitting, just sitting here day after day.
It’s work! How I hate it!
I’d much rather play!
I’d take a vacation, fly off for a rest
If I could find someone to stay on my nest!
If I could find someone, I’d fly away-free…”

ACTOR: Then Horton, the Elephant, passed by her tree.

ACTRESS: “Hello!”

ACTOR: called the lazy bird, smiling her best,

ACTRESS: “You’ve nothing to do and I do need a rest. Would you like to sit on the egg in my nest?”

ACTOR: The elephant laughed.
“Why, of all silly things!
I haven’t feathers and I haven’t wings.
Me on your egg? Why, that doesn’t make sense…
Your egg is so small, ma’am, and I’m so immense!”

ACTRESS: “Tut, tut,”

ACTOR: answered Mayzie.

ACTRESS: “I know you’re not small
But I’m sure you can do it. No trouble at all.
Just sit on it softly. You’re gentle and kind.
Come, be a good fellow. I know you won’t mind.”

ACTOR: “I can’t,” said the elephant

ACTRESS: “PL-E-E-ASE!” begged the bird.

“I won’t be gone long, sir. I give you my word. I’ll hurry right back. Why, I’ll never be missed….”

ACTOR: “Very well,” said the elephant, “since you insist…
You want a vacation. Go fly off and take it.
I’ll sit on your egg and I’ll try not to break it.
I’ll stay and be faithful. I mean what I say.”

ACTRESS: “Toodle-oo!” sang out Mayzie and fluttered away.

ACTOR: “H-m-m-m..the first thing to do,” murmured Horton,
“Let’s see…
The first thing to do is to prop up this tree
And make it much stronger. That has to be done
Before I get on it. I must weigh a ton.”

ACTRESS: Then carefully,
Tenderly,
Gently he crept
Up the trunk to the nest where the little egg slept.
Then Horton the elephant smiled.

ACTOR: “Now that’s that…”

ACTRESS: And he sat
And he sat
And he sat
And he sat….

ACTOR: And he sat all that day
And he kept the egg warm…
And he sat all that night
Through a terrible storm.

ACTRESS: It poured and it lightninged!

It thundered! It rumbled!

ACTOR: “This isn’t much fun,”

ACTRESS: The poor elephant grumbled.

ACTOR: “I wish she’d come back ‘Cause I’m cold and I’m wet. I hope that that Mayzie bird doesn’t forget.”

ACTRESS: But Mayzie, by this time, was far beyond reach,
Enjoying the sunshine way off in the Palm Beach,
And having such fun, such a wonderful rest,
Decided she’d never go back to her nest!

ACTOR: So Horton kept sitting there, day after day.
And soon it was Autumn. The leaves blew away.
And then came the Winter…the snow and the sleet!
And icicles hung
From his trunk and his feet.

ACTRESS: But Horton kept sitting, and said with a sneeze,

ACTOR: “I’ll stay on this egg and I won’t let it freeze.
I meant what I said
And I said what I meant…
An elephant’s faithful
One hundred per cent!”

ACTRESS: So poor Horton sat there
The whole winter through…
And then came the springtime
With troubles anew!

ACTOR: His friends gathered round And they shouted with glee.

ACTRESS: “Look! Horton the Elephant’s up in a tree!”

ACTOR: They taunted, they teased him, They yelled,

ACTRESS: “How Absurd!” “Old Horton the Elephant Thinks he’s a bird!”

ACTOR: They Laughed the they Laughed, Then they all ran away. And Horton was lonely. He wanted to play

ACTRESS: but he sat on the egg and continued to say

ACTOR: “I meant what I said
And I said what I meant…
An elephant’s faithful
One hundred per cent!
“No matter What happens,
This egg must be tended!”

ACTRESS: But poor Horton’s troubles
Were far, far from ended
For, while Horton sat there
So faithful, so kind,
Three hunters came sneaking
Up softly behind!

ACTOR: He heard the men’s footsteps!
He turned with a start!
Three rifles were aiming
Right strait at his heart!

ACTRESS: Did he run?

ACTOR: He did not!

ACTRESS: HORTON STAYED ON THAT NEST!
He held his head high
And he threw out his chest
And he looked at the hunters
As much as to say:

ACTOR: “Shoot if you must
But I won’t run away!
I meant what I said
And I said what I meant…
An elephant’s faithful
One hundred per cent!”

ACTRESS: But the men didn’t shoot!
Much to Horton’s surprise
They dropped their three guns
And they stared with wide eyes!

ACTOR: “Look!”

ACTRESS: they all shouted,

ACTOR: “Can such a thing be?
An elephant sitting on top of a tree…”
“It’s strange! It’s amazing! It’s wonderful! New!
Don’t shoot him. We’ll catch him. That’s just what we’ll do!
Let’s take him alive. Why, he’s terribly funny!
We’ll sell him back to a circus, for money!”

ACTRESS: And the first thing he knew, they had built a big wagon With ropes on the front for the pullers to drag on.

They dug up his tree and they put it inside, With Horton so sad that he practically cried.

ACTOR: “We’re off!”

ACTRESS: the men shouted.

ACTOR: And off they all went With Horton unhappy, one hundred per cent.

ACTRESS: Up out of the jungle! Up into the sky!
Up over the mountains ten thousand feet high!
Then down, down the mountains
And down to the sea
Went the cart with the elephant,
Egg, nest and tree…

ACTOR: Then out of the wagon
And onto a ship!
Out over the ocean…
And ooh, what a trip!

ACTRESS: Rolling and tossing and splashed with the spray! And Horton said, day after day after day,

ACTOR: “I meant what I said
And I said what I meant…
But oh, am I seasick!
One hundred per cent!”

ACTRESS: After bobbing around for two weeks like a cork, They landed at last in the town of New York.

ACTOR: “All ashore!”

ACTRESS: the men shouted,

ACTOR: And down with a lurch
Went Horton the Elephant
Still on his perch,
Tied onto a board that could just scarcely hold him…

ACTRESS: Bump! Horton landed! And then the men sold him!

ACTOR: Sold to a circus! Then week after week They showed him to people at ten cents a peek. They took him to Boston,

ACTRESS: to Kalamazoo,

ACTOR: Chicago, Weehawken

ACTRESS: and Washington, too;

ACTOR: To Dayton, Ohio; St. Paul, Minnesota;

ACTRESS: To Wichita, Kansas; to Drake, North Dakota.

ACTOR: And everywhere thousands of folks flocked to see And laugh at the elephant up in a tree.

ACTRESS: Poor Horton grew sadder the farther he went, But he said as he sat in the hot noisy tent:

ACTOR: “I meant what I said, and I said what I meant… an elephant’s faithful—one hundred per cent!”

ACTRESS: Then…one day
The circus show happened to reach
A town way down south, not so far from Palm Beach.
And, dawdling along way up high in the sky,
Who (of all people!) should chance to fly by

ACTOR: But that old good-for-nothing bird, runaway Mayzie! Still on vacation and still just as lazy.

And, spying the flags and the tents just below, She sang out,

ACTRESS: “What fun! Why, I’ll go to the show!”

ACTOR: And she swooped from the clouds Through an open tent door…

ACTRESS: “Good gracious!”

ACTOR: gasped Mayzie,

ACTRESS: “I’ve seen you before!”

ACTOR: Poor Horton looked up with his face white as chalk!
He started to speak, but before he could talk…
There rang out the noisiest ear-splitting squeaks
From the egg that he’d sat on for fifty-one weeks!

ACTRESS: A thumping! A Bumping! A wild alive scratching!

ACTOR: “My egg!”

ACTRES: Shouted Horton.

ACTOR: “My egg! Why, it’s hatching!”

ACTRESS: “But it’s Mine!”

ACTOR: screamed the bird, when she heard the egg crack. (the work was all done. Now she wanted it back.)

ACTRESS: “It’s my egg!”

ACTOR: she sputtered.

ACTRESS: “You stole it from me! Get off of my nest and get out of my tree!”

ACTOR: Poor Horton backed down With a sad, heavy heart… But at that very instant, the egg burst apart!

ACTRESS: And out of the pieces of red and white shell, From the egg that he’d sat on so long and so well, Horton the Elephant saw something whizz!

ACTOR: It had Ears And a Tail

ACTRESS: And a trunk just like his!

ACTOR: And the people came shouting,

ACTRESS: “What’s all this about…?”

ACTOR: They looked! And they stared with their eyes popping out! Then they cheered and they cheered and they cheered more and more. They’d never seen anything like it before!

ACTRESS: “My goodness! My gracious!”

ACTOR: they shouted.

ACTRESS: “My Word! It’s something brand new! It’s an elephant-bird!!

ACTOR: And it should be, it should be, it should be like that! Because Horton was faithful! He sat and he sat!

ACTRESS: He meant what he said
And he said what he meant…”
…And they sent him home
Happy,

ACTOR: One hundred per cent!
```

---

## IC-0804: Housing to Share

- Title: Housing to Share
- Author (byline): Barbara Lhota and Janet B. Milstein
- Work: Duo Practice & Competition: Volume 1
- Publisher: Smith & Kraus, Inc.
- Publication date as stated: 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DORRINE, CAL
- Teaser before the introduction: Yes
- Spoken words (computed): 1927
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barbara Lhota and Janet B. Milstein
Book: Duo Practice & Competition: Volume 1
ISBN: 1575253089
Publisher: Smith & Kraus, Inc.
Date (Month/Year): 2003
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: Housing to Share by Barbara Lhota and Janet B. Milstein
```

### Performance text (classify this)

```text
DORRINE: (To audience.) I jotted down a few notes to help you help me, Cheryl. Let's start with age. I'm looking for a female roommate who is approximately twenty-six to thirty-two years

CAL: (To audience.) I got a couple of IDs here that'll say I'm anywhere from twenty-one to twenty-five.

DORRINE: I think new-to-the-city, sociable, but not too sociable. Female. Definitely female.

CAL: Sex? (Grin.) Well, I uh . . . (Realizes.) Oh? You mean like male or female?

DORRINE: Well educated is important.

CAL: Hey, I was gonna finish college, but it was, like, a lot of work.

DORRINE: No excess drinkers, partyers, and definitely not a smoker.

CAL: I'm real picky on that. On smoking. I want my roommate to use an ashtray. Ya really got to, ya know? Because I almost burned my place down once. (Beat.) What? Not recently!

DORRINE: I'm looking for a real professional, making mid-thirties or so.

CAL: Employment? Yeah, I've got a couple jobs.

DORRINE: And I will accept the occasional vegetarian if there are no curry smells that turn my place into an Ethiopian armpit.

CAL: I always cook with loads of garlic and curry. But that's not a good thing to do if you're tired, and hung-over, and without a lid. I found that out.

DORRINE: Also, Cheryl, I prefer no bike messengers, aerobics instructors, dog walkers, or gothic magicians. Don't ask. I don't want to go into it. Oh, and absolutely no actors!

CAL: Yeah, I'm an actor.

DORRINE: Someone who can carryon an intelligent conversation, well-read, and well-traveled.

CAL: Yeah, uh, someone who pays rent is probably good.

DORRINE: I find it's best if they have no car, no pets, and no boyfriend.

CAL: I mean, they don't have to pay it on the first, but it probably would be good if it's like within the first week or so. I mean, believe me, I've been late with rent. Who isn't? (Beat.) Not real late. What are you writing down?

DORRINE: And uses coasters. Can't anyone use a coaster when they're right there and available?

CAL: And not paying rent, that's. . . that's like bad.

DORRINE: Oh. And finally, they should love my cat, Modesty Blaze. (Beat.) Yes, I said no pets. But that's no pets for them. I have an existing pet in our home. So therefore, they should love Modesty if they want to live here.

CAL: Oh, yeah, Cher, and I majorly love cats. I really, really dig 'em.

Scene change: Dorrine and Cal are now in Dorrine's apartment. Dorrinne is interviewing Cal as a potential - and potentially disastrous - roommate.

DORRINE: (Turns to Cal.) Cats?

CAL: (To Dorrine.) Yeah. Cheryl at the agency said you had cats. Where are they?

DORRINE: I think there's been some sort of a mix-up here, Cal. I don't have cats. I have a cat. CAL: Oh. OK. Well, where's the cat then?

DORRINE: Let's wait on that. She not friendly at first anyway. Besides, we've got a problem. CAL: Problem? Is she OK? What are you feeding her these days?

DORRINE: It's not my cat. The problem is that you're not a female. I requested a female.

CAL: Oh gee, well if you're gonna be picky.

DORRINE: I don't know how this happened. Cheryl is wasting our time.

CAL: No. I don't mind that you're a woman. In fact, I like it. And I love your doorbell, Dorrine, and this room. I have a good feeling about the walls. Ya know when that happens, it happens. You can't force these things.

DORRINE: Yes, but this is a real problem for me. You not being a female.

CAL: Well, there was that short period where I liked shaving my legs. I could complain about my weigh periodically, would that help?

DORRINE: (Beat.) I'm gonna go ahead and call Cheryl.

CAL: Now wait. I was kidding. Hold up. I'm a very cool guy. Don't you want to know more about me?

DORRINE: (Beat.) No.

CAL: I love animals. I work at the shelter on Mack.

DORRINE: See. Now that's another thing. I explicitly said that I didn't want a dog walker.

CAL: Dog walker? Who said anything about a dog walker? I'm not a dog walker. I'm an animal caretaker. See? There's a difference. (Beat.) Besides, I thought you wanted someone who liked your cat - who liked animals?

DORRINE: Of course. But I don't want them bringing home fleas and other sick diseases to my little Modesty Blaze.

CAL: Modesty Blaze? What a cool name. I bet she's a little, cutie, scrunchy, sweetie cat.

DORRINE: Oh, yeah, she is. She's a snuggly wuggly baby cat. (Beat.) Now about your wrong job.

CAL: That's just part-time really. And I always wash. I have a real job. I'm an actor.

DORRINE: An actor?! You're an actor?

CAL: Yeah, but I'm not big-headed or anything. I just do a couple of steady gigs as an actor that bring in the cash.

DORRINE: Cash? Actor? Same sentence? Something's wrong.

CAL: Yeah, I play Banana Man and Bob the Bear for a balloon delivery service. I'm considered their best - their top. Can you believe it? Get this. I never even had one acting class. Never. (Beat.) You got a cig on ya?

DORRINE: Oh God, you smoke too?!

CAL: Hey, you too? Cool! But listen, you have to use an ashtray. I'm picky about that.

DORRINE: No, no you misunderstand me. I don't smoke. At all!

CAL: Oh. So why did you say you did? Honesty's the best policy.

DORRINE: I didn't say I did! In fact, I don't allow smoking in my place under any circumstance!

CAL: Ohhh, quit recently, huh? Yeah, I've done that a couple of times. Gets ya cranky. But I can see why you don't like people smokin' here. The walls are so white, no cracks or peeling like my last place. Don't get me wrong. I loved my last place. Really big. Loved my roommate. I woulda stayed there forever if he hadn't shot at me.

DORRINE: (Beat.) Shot at you? With a gun?

CAL: Yeeahh. (Her face is full of fear.) Oh no, it's cool. He didn't mean to or anything. I was just breaking in the window and he mistook me for a burglar. No biggie.

DORRINE: Ya know, it's getting kinda late.

CAL: I forgot my keys. That's why I was breaking in. And he fired - the gun. It woulda been totally cool. 'Cause he didn't hit me, but he did kinda shatter the neighbors' stained glass window, so the neighbor sued. And Robby was kinda weird about me ever after, which is cool because I didn't like the mice there anyway.

DORRINE: Mice?

CAL: Yeah, one night I woke up and one of them was running across my face. That was it. They have diseases, ya know? Yeah, that's exactly why it's good we'll have a cat here.

DORRINE: We'll?

CAL: This is going to be much better. How are the roaches here?

DORRINE: Oh - kayo You are not moving in here. I meanno offense, but - we - there is no we here.

CAL: But I thought Cheryl said we were a match.

DORRINE: I don't care what Cheryl said. Cheryl is an imbecile. Cheryl could die for all I care!

CAL: Wow! That's sona harsh. You having a bad day, huh?

DORRINE: A bad day? Try a bad year. I've gone through three roommates.

CAL: Yeah, me too - totally kicked out! (Beat.) Not that I didn't want to leave.

DORRINE: I haven't been difficult. I haven't. But my therapist thinks that

CAL: Hey, don't worry. Relax. I lived with crazy people before.

DORRINE: I'm not crazy! I'm not saying I'm crazy!

CAL: Yeah, uh-huh, that's what all crazy people say. What drugs are you on?

DORRINE: I . . . uh . . . I - I - can't believe this! All I was saying was that my therapist

CAL: I think therapy's good. So what drugs are you on?

DORRINE: I am not on drugs! I'm on - medication! There's a difference. I'm a nervous person. And nervous people need quiet roommates. I want someone calm and quiet this time.

CAL: Well, I'm quiet. And jeez, the band would only play once or twice a week.

DORRINE: (Beat. Face drops.) The band?

CAL: Oh, didn't Cheryl mention it? We're the Cool Cats. Heard of us?

DORRINE: (Beat.) My therapist has advised me that it's OK that I have some control issues. Some people have control issues and are, therefore, very particular about some things. One of those things, for me, is roommates. And you would not be good.

CAL: Aww, I just saw your little baby peek her little head around the corner. She's long-haired? (He coaxes the kitty from the hiding place. Whispering to the kitty.)

DORRINE: Yes. She is. (She watches. He still coos at the cat.) That's odd. She usually hisses at new people. (Looking. Excited.) Aww, she's looking at you! Look at her little, teeny - (Stops.) Wait a minute. Stop trying to distract me. I was making a point. The point is my therapist says I obviously need control.

CAL: Well, humm, as Dr. Phil says - lost three roomies. How has that been working for you?

DORRINE: Uh, ya know, I don't like you. And beyond that, you are not what I requested. You are not female. You're an actor. You smoke. You're in a band. You were shot at. And small rodents crawl across your face at night.

CAL: Well, is that my fault?!

DORRINE: (Yelling.) My point is that you are not calm!!!! (Breathes heavily to relax.)

CAL: You know what I think? (She shakes her head no.) I think the universe brings certain energies together. Sometimes in a way that doesn't make complete sense to anyone. But these different kinds of energies benefit from bouncing off one another. . . and they blend together to form like this positive . . . blended thing -like those yummy blended frozen fruity drinks that create. . . (Waving arms to think of word.) energy. Don't you think?

DORRINE: No, I think someone messed up at the agency. Maybe they spilled a fruity drink on our applications and they stuck together. That's about the closest this has anything to do with yummy blended frozen fruity drinks. And I refuse to pay that roommate service fee because you are the antithesis of what I asked for!

CAL: The antithesis?! Really? Wow! (Beat.) What does that mean exactly?

DORRINE: The opposite! You're the opposite of what I want!!

CAL: Well, um that's a good thing. You know uh . . . Yin and Yang. Peanut butter and jelly. Fred and Barney. (Looks at her.) Wilma. Fred and Wilma. (Beat.) The point is what's so wrong with me, huh? Besides being an actor, smoker, band person who was shot at? I'm a nice guy, right?

DORRINE: Well. . . well I know for a fact that you wouldn't do a revolving chore wheel with me.

CAL: A what?

DORRINE: A revolving chore wheel. It's color coded? It revolves around revealing certain chores around the apartment. Each person is assigned a different color chore in a month cycle. I know you would refuse.

CAL: (Sincerely interested.) Oh wow! Cool! Very organized. I like it!

DORRINE: (Beat.) You do? It's driven others away. They think it's anal.

CAL: I don't. I love things that are color coded and alphabetical. You think the chore wheel is anal? I had a roommate who organized the cupboard according to food groups. Isn't that completely nuts?

DORRINE: Nuts? Yes, well, I think nuts is a very strong word for that.

CAL: Oh wow, you do that? I love that!

DORRINE: But you just said that was completely

CAL: Shhh. (Puts his fingers over his lips.) Look. (Points to cat.) She's so friendly.

DORRINE: Oh my God. She's never done that with anyone. (Shocked.) Modesty Blaze? Behave yourself.

CAL: I think she likes me, huh?

DORRINE: Well, she certainly seems to like your. . . your muscular leg.

CAL: I didn't say this but I think organizing according to food roups IS sexy in a way.

DORRINE: You do?

CAL: Shhh!

DORRINE: (Whispering.) So you don't really think it's nuts?

CAL: (Whispers.) No, I think it's totally nuts - but in a sexy way. (Looking down.) You're kitty seems to like me, isn't that something?

DORRINE: Yes, I, I noticed that, but, but what about my control issues and your rodent problem?

CAL: So you have control issues? Works for me. I'm all about lack of control. You're so tense, Dorrine. Let me help you. (Massaging her shoulders.)

DORRINE: Mmmmm. (Pointing to her shoulder.) Right there, will ya? (He moves to that spot.) Ooh. Ahh. Mmm. Uh Oooh - that's good.

CAL: You were saying?

DORRINE: (Moving her shoulder up.) What? (Laughs.) Ha, ha, ha. (Beat.) Um, when do you move in?
```

---

## IC-0805: How We Talk in South Boston

- Title: How We Talk in South Boston
- Author (byline): David Lindsay-Abaire
- Work: Laugh Lines
- Publisher: Vintage Books
- Publication date as stated: April 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NORMAN, MARY, MARTY, BARBARA, MARLON, ASIAN MAN, PING, FRANKIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1395
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Lindsay-Abaire
Book: Laugh Lines
ISBN: 978-0307277138
Publisher: Vintage Books
Date (Month/Year): April 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Hate in America is a dreadful, daily constant.

ACTRESS: The dragging death of a black man in Jasper, Texas;

ACTOR: the crucifixion of a gay man in Laramie, Wyo.;

ACTRESS: and post-9.11 hate crimes against hundreds of Arab Americans, Muslim Americans and Sikhs are not "isolated incidents."

ACTOR: They are eruptions of a nation's intolerance.

ACTRESS: Bias is a human condition, and American history is rife with prejudice against groups and individuals because of their race, religion, disability, sexual orientation or other differences.

ACTOR: The issue is not a comic one; however, sometimes over-the-top comedy can spotlight the issues even more effectively than a serious approach.

ACTRESS: May we present David Lindsay-Abaire’s How We Talk in South Boston . . . .

ACTOR: a comic look at an extremely serious issue where everyone faces some degree of intolerance.

(Lights up on a living room [parlor) in a blue-collar home in South Boston. MARY is making a latch-hook rug when her husband NORMAN enters with a car door. His arm is lodged inside it.)
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NORMAN: Muthah-ra-Gawd, look at dis. My ahm's cot in da kah dewah.

MARY: Doan bring dat hunka gahbitch into my pahlah, Naw man. Take it back outside and diddle inda gudda.

NORMAN: I ain't diddlin'. My ahm's cot.

MARY: Get owda heah. Ya ahm's cot? (Calls downstairs.) Hey, Mahdy, ya fathah's ahm's cot in the kah dewah. Cawl da fiah depahtmend. Tell 'em to get ovah heah befoah he gets dubbaya dee-faddy on my latch-hook rug.

NORMAN: Dat's a nice rug yuh makin'.

MARY: Yuh like it? Thea havin' a time down at the VFW Post in Mahch, a bazah, like an ahts and craffs faih, an I dought I could sell my rugs.

NORMAN: Dat's a great idear, Meery. (MARTY enters).

MARTY: Yuh cawlin' me?

MARY: Yeah, wheah da frig whiryah?

MARTY: I coodin' heah ya. I was downsteahs ina cella.

MARY: Dis frickin' chowdah-head got his ahm cot in da kah dewah.

MARTY: How'd he get his ahm cot in the kah dewah?

NORMAN: I was fixin' da windah 'cause it was hahd to open, so I took da dewah apaht and was fiddlin' aroun' and my ahm got cot.

MARTY: Dat's wicket pissa. Whadda looza.

NORMAN: Get me owda heah. I gotta watch da Sox at fowah.

MARTY: I bet yaw cot in duh lockin' mechanism. I'll go get yaw kah keez. (MARTY exits.)

NORMAN: D'jew buy me some beah, Meery? You know Hahvey and Kevin McCahthy ah comin' ova to watch da game.

MARY: Sully's not comin'?

NORMAN: Nah, Sully went to da dawg track with Fitzy an Beah-zo.

MARY: Okay. I went to Stah Mahket on Sadaday inny-ways. I bought beah and a pahty platta foah yis. I can cook up some budded con on da cob. An' I got some sub rolls so you can make spuckies.

NORMAN: D'jew get any tawnic? Cause Hahvey don't drink no mowah.

MARY: Yeah. I got two big bosses a' Pepsi. The three-leetah kind. And a box of hoodsies foah afta.

NORMAN: Aw, we should still have hoodsies left ova from lass Saint Paddy's Day.

MARY: Dose was hahd and freeza burnt. I trew ' em in cia barrel. I didn't get no jimmies dough. You want me to run upta Brigham's?

(BARBARA, their daughter, enters.)

BARBARA: Ma, Dad, I have some wicket good news.

MARY: Bahbra. Ya fathah's ahm's cot in a kah dewah.

BARBARA: Whadda looza! Wanna heah my good news now? (MARTY enters.)

MARTY: I gut da kah keez. (Holds up car keys.)

BARBARA: Ma, Dad, Mahty, I'm gettin' married!

MARY: Oh my gawd, my dodda's gettin' meerried!

NORMAN: You know I got a bum ticka! I'm havin' a hahd attack heah! Gimme a hug!

(Hugs her, but the car door makes it awkward.)

BARBARA: Ahhh! Ya hit me wit da kah dewah, ya looza!

NORMAN: Sorry.

MARY: Wait a minute, Bahbra, who ah ya marion?

BARBARA: His name is Mahlin.

NORMAN: We don't know no Mahlins.

MARY: Shuwah we do. Mahlin Perkins. Da animal guy.

NORMAN: How come we neva herda dis Mahlin ya marion?

BARBARA: 'Cause I was afraid ya wooden likem.

NORMAN: Why wooden we likem?

BARBARA: He likes da Yankees. (There's a long, uncomfortable pause.)

MARTY: Yalove 'em, Bahb?

BARBARA: Moah than my haht can beah.

MARTY: Den I ken accep' 'em, liddle sista.

BARBARA: Danks, Mahty. Ma?

MARY: I neva liked baseball. I do an kayah.

BARBARA: Dad? (NORMAN spits in her face.) Ya spit in my eye, ya looza!

NORMAN: You know about da curse, Bahb?

BARBARA: Yeah, but ya ain't gotta spit at me.

NORMAN: In nine-teen nine-teen, Babe Root was a Red Sox playah, an den Harry Frazee solt 'em to da Yankees, and da rest is history. Eva since den, my team has been cursed. In eighdy yeahs, we hahven won a Whirl Series. Shuwah, deer ah udda teams wit worse reckids, but nobiddy loses in such haht-breakin' ways. An' above all da teams in da leagues, da Yankees have been ah ahch enemies. Damn dat Harry Frazee. And damn all dose Yankees. Fenway Pahk shoulda been da house dat Root built. And now my ony dodda is gonna tell me she's marion a Yankee fan?

BARBARA: But I love' em.

MARY: Da haht is a mysterious oahgan, Nawman. Dat I know.

NORMAN: SO doan I! I know dat too, Meery!

BARBARA: Please, Daddy. . .

NORMAN: Awww, jeez. Alright. But nobiddy mention dat dis kid's a Yankee fan. Especially to Kevin McCahthy.

BARBARA: Oh dank you, Daddy! (Hugs him, but the car door gets in the way.) Ahhhh, dat dawn kah dewah!

MARTY: I gut da kah keez! (Tries to unlock the car door.)

MARLON: (Offstage.) Knock-knock. Anyone home?

BARBARA: In heah, honey! Dat's MaWin. He was pahkin' da kah. Everyone be nice.

(MARLON enters. He's a black man.)

MARLON: Hello. I'm Marlon. I was parking the car by the bar on the far corner.

BARBARA: Dozen he tock funny?(They just stare at him blankly.) I just tolt 'em you was a Yankee fan.

MARLON: Oh, yeah? Sorry, I hope you don't hold it against me. Least I'm not a Mets fan. I was rooting for you guys in '86. Too bad about that Billy Buckner thing. Gimpy little ground ball down the first-base line. Right between Buckner's feet. World Series riding on that simple grounder. You must've been angry as heck. Kinda funny, though, right?

MARY: Yoah black. Yourah black man.

MARLON: Yes, I know.

NORMAN: This is a black man, Bahbra.

BARBARA: Isn't he goahjis?

NORMAN: A black man who likes da Yankees and tinks Bucknuh is funny. (Spits in MARLON's Face.)

MARLON: Eww. He spit at me.

MARY: Calm ya livva, Nawman.

NORMAN: Mahty, goto da stowah and get me a regulah coffee.

MARY: Anna cahtin a milk. Deah's money in my pockabook.

MARTY: I wanna stay.

NORMAN: We gotta talk to ya sistah.

MARTY: I'm gay. Since youah so mad anyways and spittin' on evrybidy, I might as well tell yuhs.

MARLON: I support you, Marty. Be proud of your feelings.'

NORMAN: Not in dis neighbahood, Take it to da liberals ova da River at Hahvahd. Dale tellya to mahch in da parade ahm in ahm.

BARBARA: Daddy. . .

MARY: He do an mean nuttin' by it. He was mugged by a black guy once.

MARTY: A gay black guy?

MARY: Shut up, Mahtty. Ya fathuh's upset.

NORMAN: You kids doe know about history. Dat's ya problem right deah.

BARBARA: I'm marion MaWin whetha yis like it oah not.

NORMAN: Yaw ancestas came ova cuzza da famines in Iyaland in da 1850s. An you tink dose uppity Brahmin wannid 'em heah in Boston? No. Nobidy wannid a buncha imergrents. So we found a liddle slice a land ona watah and made it ahrown. The Irish were discriminated against foh all dose yeahs, an now deah gonna tell us weah racist foah protectin' duh ony place dat's ahrown.

MARLON: I can't understand a word he's saying.

NORMAN: Yuh stay wit yuh own kind. Dat's how God wants it. (An ASIAN MAN enters.)

ASIAN MAN: I couldn't help overhearing the argument. I guess it's okay to come out now.

MARTY: Mom, Dad, this is Ping, my boyfriend. He's been livin' inda basement wit me for tree months.

PING: It's a pleasure to meet you. Arm's caught in the car door, huh?

NORMAN: Whad is goin' on heah? Did I raise yous kids to be freaks? Friggin League a Nations in dis house! Dis ain't Greenwitch Village, Mahty!

MARY: It's dat tollarinse ting they been tocking about on da TV: Duh kids musta been watchin' da TV:

NORMAN: No tollarinse in dis house. Dis is Southie! We doan tolerate nobidy heah! Nobidy! Day all wanna take us ova. Duh fohced buss in' was da first step. Remembuh when Bob Kraft tried to put the Pats Stadium in my backyahd? I don't tink so! We chased his Yiddish butt owda heah! I shoulda known he was no good, trying to move dat Jacksonville game so it wooden conflict wit Yom Kippa, whadeva dat is!

PING: I've never heard someone be so blatantly prejudiced.

BARBARA: Ain't he funny?

NORMAN: I ain't prejudiced!

BARBARA: See what I mean? Daddy, youah hilairy-us!

NORMAN: Don't laugh at me, Bahb!

MARLON: He's almost as funny as Bill Buckner!

NORMAN: Get outta my house!

MARY: You do look funny, Nawman! Ya face all red, ya ahm cot inda kah dewah!

(They're all laughing at him now. He's so angry he can barely speak.)

MARTY: Hey, Dad, live and let live, okay?

MARY: Ah you okay, Nawman?

PING: I'm a doctor. I can help.

NORMAN: I do an need no help! I'm fine da way I am!

MARLON: Get him to my car. We'll drive him to City Hospital.

NORMAN: I doan need yis help. . . I'm fine widout yis. (He crawls to the exit, the car door dragging.)

MARY: Youah bein' very stubbin.

NORMAN: I doan needa tolerate nobidy . . . (He collapses.) Ahhhh . . .(He dies.)

MARY: Muthah-ra-Gawd, he's dead.

BARBARA: My fathah is dead.

MARY: He wasn't really youah fathah anyways. Kids, I'd like you to meet Frankie Grey Hawk. (FRANKIE enters, an older man in full Native American regalia.)

FRANKIE: How. Me smokum peace pipe.

MARY: Isn't he funny? Dat's duh ferse ting he says each mohnin' befoah he sneaks oudda da house. He's sucha joka.

FRANKIE: I'm actually a linguistics professor at Northeastern.

BARBARA: Youah ah fathuh?

MARTY: Dat explains Bahbra's terrible drinkin' problem.

BARBARA: And Mathy's dream to open a gamblin' casino!

FRANKIE: Kids, those are just racial stereotypes perpetuated by the white man to keep us down.
```

---

## IC-0806: Hypneurosis

- Title: Hypneurosis
- Author (byline): Barbara Lhota and Janet B. Milstein
- Work: Duo Practice & Competition: Volume 1
- Publisher: Smith & Kraus, Inc.
- Publication date as stated: 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: EDSON, JANIS
- Teaser before the introduction: Yes
- Spoken words (computed): 1836
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barbara Lhota and Janet B. Milstein
Book: Duo Practice & Competition: Volume 1
ISBN: 1575253089
Publisher: Smith & Kraus, Inc.
Date(Month/Year): 2003
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: When most people think of hypnosis, they think of a hypnotist making people act silly on a stage.

ACTRESS: But really, hypnosis is used in a variety of settings – from emergency rooms to dental offices to outpatient clinics

ACTOR: Hypnosis has been successfully used to reduce phobias, break the smoking habit, and even promote weight loss.

ACTRESS: Which is one of the main reasons I came to the office today. . . . Weight loss and maybe a few other things while I’m under, you know.

ACTOR: It’s the few other things that I’m worried about . . . .

BOTH: Hypneurosis by Barbara Lhota and Janet B. Milstein
```

### Performance text (classify this)

```text
EDSON: Please, have a seat, Miss Colburn.

JANIS: (Sitting.) Janis. Call me Janis.

EDSON: OK, Janis. (Sitting. She looks suspiciously around the room.) Is something wrong?

JANIS: Just checking. You don't record these sessions, do you?

EDSON: Ohhh. Oh, no. What happens in this room is completely confidential. You have nothing to worry about.

JANIS: That's what I'm worried about.

EDSON: Excuse me?

JANIS: I want other people to know what happens in this room. I don't mean the whole world, but perhaps a friend or two.

EDSON: (Not quite sure what to make of this.) Why don't we back up to what has brought you here today, Janis? Start at the beginning.

JANIS: You're not just trying to change the subject?

EDSON: Absolutely not. I'll even make a note. (Writing.) Recording sessions, friends, not the whole world. There. Now what is it, exactly, that has brought you here to see me?

JANIS: Well, I've read that many people have had success losing weight or quitting smoking or curing insomnia through hypnosis.

EDSON: Yes, we do have a high success rate in helping people overcome the problems they have been struggling with or their fears.

JANIS: Good.

EDSON: What exactly are you looking for help with?

JANIS: My life.

EDSON: (Beat.) OK. Could you be a little more specific?

JANIS: Well, I would like some help losing weight.

EDSON: Good. I don't mean that it's good that you're having problems. I mean, good, we're clarifying things. Well, the way I usually work with clients with this type of problem is to

JANIS: I'm not finished.

EDSON: Oh. Excuse me. I didn't mean to cut you off there. Go on.

JANIS: With your hypnosis you can make my mind believe that I really want to lose weight, right?

EDSON: Well. . . You do want to lose weight, don't you?

JANIS: Yes, but wanting hasn't quite done the job by itself now, has it?

EDSON: Well, think of it this way. I can help you to lessen your cravings for fatty foods and

JANIS: Great! That's what I was hoping.

EDSON: Well, good.

JANIS: You see, I was thinking. . . if you can help me lessen my cravings for fatty foods, then you could also do some other helpful things while you're at it.

EDSON: Other helpful things?

JANIS: Yes! I'd like you to hypnotize me into thinking that I hate chocolate with a passion. And all other candy and sweets. And that my favorite food in the world is veggies - especially dark green veggies. And my second favorite food is fruit. All kinds. Oh, yes, and that I despise anything doughy, like bagels or bread or muffins or cake. And ice cream. Oh, yeah, ice cream has got to go. And that I dislike fried foods almost as much as chocolate, but not quite as much. And I was thinking that my third favorite food should probably have some protein, but not fatty protein. I think it should be beans and things that vegetarians eat that keep them alive without wilting.

EDSON: Uh, Miss Colburn

JANIS: Janis. Now, Doctor. . . (Looking around his office, sees his first name on his desk plaque.) Edson Polanski. Oh, Edson. What an unusual name. I like it. So Edson, are you writing this down?

EDSON: No, Janis, I'm positive I won't forget, but you see

JANIS: Silly me! You're a hypnotist. You've probably already stored it all somewhere in your incredible mind. So, moving on. Now, this is very important, Edson. One cannot stay thin by food alone. So, I want you to use your powers to make me believe that my favorite thing in the whole world to do is to work out.

EDSON: Well, I typically - I

JANIS: Any type of exercise will do. Actually, it might be a good idea if you gave me a love of sports, since I've always been terrified of getting hit by balls in softball and volleyball and anything-ball really. I think that goes back to those horrid days in kindergarten, being forced to play dodgeball and being waled with those red, bouncy playground balls for no good reason at all. (She is starting to get upset at the memory of it.) Does it help you hypnotize me faster if you know the reason I'm screwed up?

EDSON: No, no. No. That would be therapy. Which isn't such a bad idea, Janice. You see, I can't help you to like something you don't really like or to do something you don't really want to do.

JANIS: Well, then what good are you? Huh?

EDSON: Well, I - I help people who want to help themselves.

JANIS: SO now you're God, are you? And choosing to refuse my cries for help? Is this because I'm Jewish, Doctor? It's not my fault my parents birthed me and never sent me to Hebrew school.

EDSON: Janis. Stop. (He raises his hand and does a special finger movement. She freezes hut speaks somewhat rohotically.) Can you hear me?

JANIS: Yesss.

EDSON: Good. You are feeling calm. There is nothing to get worked up about. Everything is peaceful. . . serene. You feel happy and relaxed. (He snaps and Janis comes out of the hypnosis.)

JANIS: (Looking around.) This is a beautiful office, Edson. I just realized that now. It is really quite lovely.

EDSON: Thank you.

JANIS: What was I saying? I'm sorry, I think I got distracted by that gorgeous painting on the wall.

EDSON: Oh, why thank you. You were talking about dodgeball.

JANIS: (Her mood dropping.) Ohhh.

EDSON: And I was mentioning therapy as a possible solution.

JANIS: (Dropping more.) Ohhhhh.

EDSON: Have you ever tried therapy, Janis?

JANIS: Yes, once.

EDSON: Once? And what was that like?

JANIS: I talked, he nodded. I talked, he went, "Hmm." I talked, he took notes. And then I wrote him a very large check.

EDSON: Well, part of the process of therapy is to let the patient discover their own solutions.

JANIS: Well, I can do that at home with some chocolate and wine, and keep my very large check.

EDSON: Well. . .

JANIS: Anyway, why are we talking about therapy? I came here to get hypnotized. I did tell you that, right?

EDSON: Oh yes. It was just that you had so many things you wanted to change

JANIS: Hey, look. I expected to write you a very large check to reprogram these things. But if it costs extra for you to reprogram extra things, I'm prepared to write you an extra large check.

EDSON: Well, that's very kind of you, Janis. However, as I was explaining before, I do not reprogram people's minds. Successful hypnosis depends on two key elements: a willingness to change, and a constant belief that a constructive goal will be reached.

JANIS: Well, I'm willing to have you change me, and I firmly believe if you do, the goal will be very constructive. (Beat.) How about two extra large checks?

EDSON: Janis

JANIS: But I also want you to make me never want to pick my teeth, pluck my eyebrows, or pull out my eyelashes. Bad stuff. I read your pamphlet in the waiting room, Edson. It said hypnotized people experience changes in the way they think or behave in response to suggestions. So I'm merely giving you the suggestions that I want you to suggest to me. (Edson sighs.) OK, you win, five. Five extra large checks. .

EDSON: Done!

JANIS: Done?

EDSON: Yes. Done. Finished. Fine. Finito. OK!

JANIS: Ohhh, I knew you had a kind soul!

EDSON: But one thing at a time. And I can't promise full and permanent results. You have to be willing and open.

JANIS: Yes, yes. I am open. I am so open that I think we could do more than one at once. Fix it all in one fell swoop. Oh, and speaking of open, I want to keep the door that way when we do your thing. And I'd like to videotape our session as well.

EDSON: (Startled.) Videotape?

JANIS: Yes. Remember the note you took?

EDSON: (Reading.) Recording sessions, friends, not the whole world.

JANIS: That's the one. You see, I would like to videotape the session with a friend present or just outside the door to make sure everything's safe.

EDSON: (Panicking.) But I don't allow videotaping. In fact, it, it makes me a bit nervous. I'm not really sure why. Look, I can assure you, Janis, my methods are completely harmless.

JANIS: Exactly. You can assure me. But how do I know, since I will be under your spell, Edson? How do I know you won't hypnotize me into stealing or killing people or watching soap operas? See my point?

EDSON: Well, if that were the case, Janis, I would have hypnotized you to do that already. I mean, why wait? I could have you out right now, killing people, stealing their money, and making it home in time for "One Life to Live"!

JANIS: (Laughs.) Oh my God. You're right. Silly me. (Pinches herself.) Oww! I'm still here. Just checking. OK, Edson, I've got about five minutes left before "Oprah." Let's do it!

EDSON: Now?! No, you see I normally schedule clients to come back after the initial consult

JANIS: Normally, schmormally. I'm different. I'm giving you five extra large checks. Let's go.

EDSON: But what about your friend and, and the (Winces.) videotape?

JANIS: I come prepared. Stephanie is outside the door with a camcorder and two mirrors. (Calling off) Roll 'em, Steph!

EDSON: I - this is - videotapes make me nervous. I, I - OK. Relax. Relax.

JANIS: I'm relaxed.

EDSON: Not you, me.

JANIS: Oh, sorry. Didn't mean to interrupt your process. Go ahead.

EDSON: I, I, I want you to watch my fingers. (He starts moving them as before, in a repetitive motion.) Very closely. You are feeling sloppy - er, sleepy. Relaxed and sleepy. When I clap my hands you will be in a state between sleeping and walking - er, waking. (He claps. She looks controlled by him.) Can you hear me, Janis?

JANIS: (Robotically.) Yesss.

EDSON: Good. Now, you are ready. You are feeling open to my suggestions. Urn, uh . . . could we turn off the camera?

JANIS: Nooo.

EDSON: Please? I can't focus.

JANIS: Fiveee extraaa laaarge cheeecks.

EDSON: Right. OK. Urn, yes, Janis, uh, let me think here. . . You love to play dodgeball and get hit with veggies - especially dark green veggies. (Nervous and fumbling.) Uh, well, that's not urn, OK you have a passion for, for, for deepfried. . . chocolate!

JANIS: Mmmmm.

EDSON: (Peeking at the offstage video camera.) No. No. No. From now on you will not pluck your fruit. (Correcting himself.) No!

JANIS: Nooo plucking fruit.

EDSON: No, Janis, that's not. Oh Jeez, urn, urn, OK uh when you pull out your, your checkbook, you will crave softball. (Not completely sure where that came from.)

JANIS: Ahh.

EDSON: Oh my God, urn, urn wilting eyelashes keep vegetarians healthy? No.

Eating doughy food relaxes your teeth. Aah!

JANIS: Doughyyy.

EDSON: Ice cream is what you. . . pick at?

JANIS: Yesss, pick ice cream.

EDSON: No, you despise, urn, what did you. . . oh, yes, you despise working out.

JANIS: Yuckyyy.

EDSON: Oh dear, oh dear, oh - oh! Your third favorite food is eyebrows!

JANIS: Yummyyy.

EDSON: (Disgusted.) Ehh! OK? OK. When I snap my count, you will come on - turn off - wake up. (He snaps his fingers. Her body loosens.) Janis?

JANIS: Yes?

EDSON: Can you please have your friend turn off that video camera? !

JANIS: Oh. (She laughs.) I was just making that up in case you thought you'd try anything funny.

EDSON: Making it up?! Oh, yes, funny. Ha ha. Ha, ha, ha! (Starting to cry.) Ha-ha-ha-ha-ha.

JANIS: (Smiling.) Oh, I have a friend who does that too – cries when she laughs real hard. Ya know, I feel good. Really good. I think this was successful.

EDSON: But you - I - you can't - I, I,

JANIS: Don't worry. I'll keep my promise. You earned your five extra large checks. Let me just grab my checkbook and (Robotically.) Softball!! I must play softball! (Sounding natural again.}You know I have an incredible urge to play softball? (Realizing.) You did it! You did it! I crave softball. Here keep the whole checkbook! You deserve it - I don't care! Cause I just wanna play softball! (Starting to leave.) Come by for dinner, Edson, we'll celebrate. Sauteed eyelashes and we'll pick at ice cream! Bye! (Calling off) Hey, anyone want to play softball?

EDSON: (Sinking.) Oh, dear.
```

---

## IC-0807: I Bring You Flowers

- Title: I Bring You Flowers
- Author (byline): William Lang
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: April 2017
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: FAYE, JIM
- Teaser before the introduction: Yes
- Spoken words (computed): 1471
- Already set (do not supply): none

### Source block (context only)

```text
Author: William Lange
ISBN: 978-0874408331
Publisher: Samuel French, Inc.
Date: April 2017
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: I Bring You Flowers by William Lang
```

### Performance text (classify this)

```text
[FAYE enters pushing a baby carriage. She coos to the baby, tucks it in, & pushes the carriage to the side. After a moment or two JIM enters carrying a newspaper under his arm. As the conversation evolves, we realize the bench is in the courtyard of an institution where the young wife is an inmate and the husband a visitor.]

FAYE: (Pg 5-8) It’s a lovely day for flowers, isn’t it?

JIM: Yes, it is. [both sit down on the bench. JIM opens the paper]

FAYE: Do you mind if I ask you a question?

JIM: No, not at all.

FAYE: If all the flowers in the world were stretched end to end, how long would they be?

JIM: To the moon and back.

FAYE: [with exaggeration] You’re kidding!

JIM: [puts down paper and raises his hand in the scout salute] Scouts honor.

FAYE: If all the flowers in the world were put in one big flower pot, how high would that be?

JIM: Four times the height of the Empire State Building.

FAYE: [with exaggeration] You’re kidding!

JIM: [raising his hand in the scout salute] Scouts honor.

FAYE: If all the flowers in the world were each given, one by one, to a little child to hold and smell . . .

JIM: [walks a few steps away. He cuts FAYE off, with seriousness] No, Faye. No.

FAYE: I said if all the flowers in the world were each given to a little child…

JIM: [interrupting her again] Faye, ask something else.

FAYE: I want to know the answer to that question. [pouts, stamps foot]

JIM: There is no answer to that question. It disappeared.

FAYE: It didn’t!

JIM: It did.

FAYE: Are you sure?

JIM: Yes, I’m sure. [picks up the paper] Would you like to read a part of the paper?

FAYE: No, thank you. I think I’ll enjoy the flowers. [pause] What time is it?

JIM: [looks at watch] Ten to ten.

FAYE: Time is so deceiving. I could stay here forever.

JIM: Ask me another question.

FAYE: [with enthusiasm] How many chinamen are there in Honolulu?

JIM: [with enthusiasm] Half a million and they’re all waiters at Wo Fats. Do you remember that day?

FAYE: [laughing] Could I ever forget it! We went out and had pizza, remember? (Pg 10-12) Remember the ride around Ka'ena point? You were going to show me the island.

JIM: [with good humor] You laughed at me, then, didn’t you?

FAYE: It is not every day that one’s hero gets stuck in the mud and has to be pulled out.

JIM: We could go back to Hawaii.

FAYE: If all the flowers in the world looked alike, would they be beautiful?

JIM: I would bring you flowers every day.

FAYE: Would you?

JIM: Plumeria, orchid—all the flowers I would lay at your feet.

FAYE: Do you love me?

JIM: [takes her hand] Let’s go back to Hawaii. [JIM turns away]

FAYE: (Pg 16) [doubtful] Jim, do you think we could have as much fun now as we did then?

JIM: More. It would be a second honeymoon.

FAYE: (Pg 12-14) Hawaii is gone. It’s over.

JIM: No, it’s not. [FAYE begins to cry] Don’t cry. Don’t cry.

FAYE: If all the flowers in the world were blue, what color would the ocean be?

JIM: No, Faye, don’t! Let’s talk!

FAYE: I’m not ready to talk. Tell me of Hawaii. Tell me of Makaha, of Pats at Punalu’lu.

JIM: No! I want to tell you of the future.

FAYE: [slight pause] Answer me a question then?

JIM: All right.

FAYE: If all the flowers—

JIM: Oh, God! [interrupting; exasperated] I thought . . . [walks away a few steps] what difference does it make.

FAYE: Jim, please understand.

JIM: [turning and coming up to her] All right. I’ll tell you what I understand. This had got to stop. How long can we go on like this, Faye? [grabs FAYES arms, shakes her] How long?

FAYE: Why must you always come back to that? [FAYE pulls away] Why can’t you leave well enough alone?

JIM: Because it’s there! It lives and breathes. [then, diversionary] Let’s go back to Hawaii.

FAYE: (Pg 16+) Who would take care of her? [goes to stroller, adjust blankets]

JIM: No one. [shakes head]

FAYE: No one? Who would take care of my Lela?

JIM: [going to her with intensity] Honey, honey. It’s time to face up to the fact that our Lela is dead and has been for a year.

FAYE: No. My Lela’s taking a nap!

JIM: She’s not taking a nap!

FAYE: How can you be so cruel? When she wakes up, I’ll show her all the flowers. [sings to herself] Rock-a-bye baby on the tree top.

JIM: When was Lela born?

FAYE: You know that.

JIM: You tell me. I forgot.

FAYE: She was born two days before Christmas. She was our present from Santa Claus.

JIM: That’s right. And how many years ago was that?

FAYE: It was . . .

JIM: It was four and a half years. Now tell me, Faye, if Lela was four and a half years old, would she still nap in a baby carriage?

FAYE: If all the flowers in the world had thorns, would people ever pick them?

JIM: Answer me! Would she?

FAYE: If all the flowers . . .

JIM: Lela is dead!

FAYE: (Pg 22) No. You’re wrong, Jim. She’s alive. In the morning she wakes up and calls for me. She has orange juice for breakfast and we talk and she dresses her dolls. It’s true, Jim. [picks the “baby” up from the carriage] Lela.

JIM: [taking the doll from her] This is not Lela! This is a doll. You buy these things in stores, you take them home to your children and they play with them. This is not Lela. This is a doll. A doll! [has an idea, puts the doll back in the carriage, calms himself, then speaks] Do you remember the kid’s pool with the metal frame I had so much trouble putting together?

FAYE: The pool Lela swims in?

JIM: Yes, that’s it. The pool that Lela swims in. It’s still in the garage . . . heavy . . . You needed a PhD in engineering to put it together.

FAYE: (Pg 24-25) Lela loves this pool.

JIM: Why don’t you get her? Maybe she’d like to swim in it.

FAYE: Really?

JIM: Really. Why don’t you get her and sit there by the pool with her while I go get the fire started. [pantomimes starting a fire] Remember how we used to barbeque in Hawaii all the time?

FAYE: Yes.

JIM: When I lit the fire, do you remember what I said to Lela?

FAYE: You said . . .

JIM: I said, watch the big flames. [pantomimes fire going up] Poof! And then Lela got out of the pool to get the ball. Take Lela out of the pool, honey, to get the ball. Go ahead.

FAYE: All right. [she does so; pantomime]

JIM: Then what happened?

FAYE: (Pg 27) Lela got out and went around the side of the house.

JIM: (Pg 26) Did you say anything to her?

FAYE: Yes. I said, don’t go in the road.

JIM: Tell it to her, honey.

FAYE: [calls out to Lela] Don’t go in the road, Lela baby.

JIM: And what did she say?

FAYE: She said I won’t Mommy.

JIM: That’s right. And then what happened.

FAYE: I sat down. I was tired.

JIM: No, you didn’t sit down. What did you do, Faye, honey? Do you remember?

FAYE: (Pg 28-30) I . . . I . . . I heard a sound

JIM: What sound? What was the sound, Faye?

FAYE: It was loud and grating.

JIM: And then . . .?

FAYE: And then we heard nothing and we ran and . . .

JIM: And what happened??

FAYE: [in tears as she remembers] NO! NO! Oh, God NO!

JIM: We picked up our Lela and put her on the table and she didn’t say anything.

FAYE: She wasn’t in the road, Jim, she wasn’t even in the road.

JIM: [tenderly] Faye.

FAYE: Jim, why us? Of all the people in the world, why us?

JIM: I don’t know. [walks away a few steps]

FAYE: Where does that leave us now, Jim?

JIM: It leaves us free to go home.

FAYE: And what then? [said simply] Lela, Lela, Lela.

JIM: Honey, honey. It’s time to face up to the fact that our Lela is dead and has been for a year, and that you have a husband who is alive and breathing and who needs you and wants to take you away from this flower garden and all the memories of Lela and start making some new memories.

FAYE: Lela likes teriyaki.

JIM: Faye, honey, please, don’t start that again. Please

FAYE: Teriyaki and Kool-Aid. She likes orange Kool-Aid with teriyaki. I’ll fix her some.

JIM: Faye. No! Stop it!

FAYE: [pantomiming the action as she speaks] You just open the package like this and pour it into the pitcher. We empty the package in the big pitcher and pour in water and add sugar. Maybe daddy would like some. Give it to Daddy.

JIM: [spoken at the same time as FAYE’s lines] Faye, honey, stop! Stop it. I love you. Stop it, please, oh God, stop it.

FAYE: [picks up the doll and cuddles it; she’s lost in her memory of Lela] Where is Daddy going? Lela, Daddy is going to work. Say bye-bye to daddy. [JIM shakes his head and exits; he doesn’t look back] Lela, look at the pretty flowers. Lela, if all the flowers in the world could speak, what do you think [they’d say]?
```

---

## IC-0808: I Never Saw Another Butterfly

- Title: I Never Saw Another Butterfly
- Author (byline): Celeste Raspanti
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: Dec 1971
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: LOUDSPEAKER, RAJA, IRENA, CHILD I, CHILD II, HONZA
- Teaser before the introduction: Yes
- Spoken words (computed): 1921
- Already set (do not supply): none

### Source block (context only)

```text
Author: Celeste Raspanti
ISBN: 978-0871292766
Publisher: Dramatic Publishing
Date (Month/Year): Dec 1971
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: From 1942 to 1945 over 15,000 Jewish children passed through Terezin, a former military garrison set up as a ghetto.

ACTOR 2: It soon became a station, a stopping-off place, for hundreds of thousands on their way to the gas chambers of Auschwitz.

ACTOR 1: When Terezin was liberated in May, 1945, only about one hundred children were alive to return to what was left of their lives, their homes, and families.

ACTOR 2: This play is an imaginative creation of the plight of one child, Raja Englanderova, developed from documentary materials: poems, diaries, letters, journals, drawings, and pictures.

TOGETHER: I Never Saw Another Butterfly by Celeste Raspanti
```

### Performance text (classify this)

```text
NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Characters: Actor 1 (F): Raja Actor 2 (M): All other parts: Loudspeaker, Child I and II, Irena, Honza

LOUDSPEAKER: Zuzana Winterova, 11 years old—perished at Auschwitz, October 4, 1944. Gabriela Freiova, 10 years old—perished at Auschwitz—May 18, 1944. Frantisek Liana Franklova, 13 years old—perished at Auschwitz, October 19, 1944. Honza—Honza Kosek, 16 years old—perished at Auschwitz, January 21, 1945 . . .

(RAJA, stands downstage facing the audience. She is carrying a school bag and a bundle.)

RAJA: (faces in the direction of the voice, then walks slowly downstage) My name—is Raja. I was born in Prague. Father, Mother, Irena, Honza—they are all gone, and I am alone. But that is not important. Only one thing is important—that I am a Jew, and that I survived Terezin . . . it slept quietly in its green valley under blue skies until…

LOUDSPEAKER: (an arrogant, military voice, interrupting) March 5, 1939. German Wehrmacht enters Prague. December 1, 1939. Jewish children excluded from state elementary schools. June 14, 1940. Auschwitz concentration camp set up. September 27, 1941. Reinhard Heydrich orders mass deportations of Jews and establishes Terezin as a model Jewish ghetto. October 16, 1941. First transports leave Prague for Terezin . . . Among them were children . . .

(IRENA SYNKOVA, one of the first inhabitants of Terezin, stands in the light with her back to the audience. She has taken responsibility for the children in the camp, organized them into groups, planned lessons in a makeshift school for them. She is obsessed with their survival. She notices the child.)

IRENA: What is your name? (RAJA shakes her head and pulls away) I am Irena Synkova. I’m a teacher here in Terezin. You’ll come to school with us, won’t you? (RAJA turns and drops to the floor, covering her face with her hands. IRENA kneels at a distance from her, talking quietly) You are from Prague? I once taught in Prague. It’s a beautiful city. When I first came to Prague, I was about your age. I remember how frightened I was. But after I made some friends, I was happy to live there. Now you are not alone, and you must not be afraid, either. (She reaches for her gently. At the first touch, the child recoils, but does not move away. She allows IRENA to remove her scarf and to take the sack from her clenched fist. She watches Irena’s face) Now that you know my name, you must tell me yours. How can we be friends? I won’t know what to call you.

RAJA: My number---here. (RAJA stretches out her arm and shows a number tattooed on her arm. IRENA begins to look through the pack and finds an identification tag.)

IRENA: (reading the tag) Raja Englanderova. Come, Raja, Raja Englanderova. Let me tell you about our school. There are many children here. We have few books—but we have many songs: every day if you wish, you may paint and draw. Would you like to paint? See, we save all the paper we can find: forms, wrapping paper—And when there’s enough, the children draw and paint.

RAJA: (RAJA finally speaks) My . . . name . . . is . . . Raja . . . (Getting up slowly, RAJA
turns from her past and returns to the lighted area downstage) It was months before
I could say anything but “my name is Raja.” I said it over and over to hear the
sound of my voice—perhaps just to make sure I still knew my name—Raja. Raja,
Raja! It helped me to be sure I was still alive. I was one of them—the children of
Terezin, one who saw everything, the barbed wire fence, the rats, the lice; one
who knew hunger, dirt and smells; one who heard trains arrive and leave,
screaming sirens, and the tread of heavy feet in the dark. I sat in Irena
Synkova’s classroom to write and paint the story of those days.
I never saw another butterfly…
The last, the very last,
So richly, brightly, dazzling yellow.
Perhaps if the sun’s tears sing
Against a white stone…
Such, such a yellow
Is carried lightly ‘way up high.
It went away I’m sure because it
Wished to kiss the world goodbye.
For seven weeks I’ve lived here,
Penned up inside this ghetto
But I have found my people here.
The dandelions call to me,
And the white chestnut candles in the court.
Only I never saw another butterfly.
That butterfly was the last one.

Butterflies don’t live here in the ghetto.

Tuesday, March 16, 1943. Today I went to see my uncle in the Sudeten barracks; there I saw them throw potato peelings, and the people threw themselves on the little piles and fought for them. There is a great deal of tension among the older children. They are going to send transports to the new ghetto—into the unknown. And fifteen hundred children will arrive tonight. They are from Poland.

CHILD I: They look awful. You can’t guess how old they are, they all have old faces and tiny bodies. They are all barelegged and only a very few have shoes. They returned from the reception center with their heads shaved. They have lice. They all have such frightened eyes.

CHILD II: We got used to standing in line at seven o’clock in the morning, at twelve noon and again at seven o’clock in the evening. We got used to sleeping without a bed, to saluting every uniform. We got used to undeserved slaps, blows, and executions. We got used to seeing people die in their own excrement, to seeing piled up coffins full of corpses, to seeing the helpless doctors.

RAJA: Monday, September 6, 1943. (When she speaks, there is an adult bitterness in her voice.) Where did Zdenka go?

IRENA: The transport—to the East . . . To work . . . resettlement . . .

RAJA: (interrupting). Auschwitz. (turning away and sitting wearily, with an old sigh). She will not come back. Jiri told us. And he knows. You die if you go to Auschwitz. It is true. I know. You die, and the ovens and the chimneys—when you die, you burn to ashes… . . .

IRENA: We do not know this is true.

RAJA: I know. And you know, too. Jiri told us; he came from Warsaw. You die if you go to Auschwitz. And no one returns. Every day—the trains go—and no one returns. Jiri was there. He escaped. He told us. How is it that you do not know?

IRENA: (quietly) I’ve heard the same talk—we all have. It can’t be true. Think. Raja, such things can’t be true.

RAJA: (pleading with her, really frightened) Irena—I want to go home—I hate this place— and everything . . . what’s the use of anything if we are going to die? Zdenka— last night we shared our bread and sang together—and now she is gone. And Eva and Miriam and Marianna . . . Gabriela and Zuzana . . .

IRENA: I know . . . I know . . . They were your friends. You loved them. Do not forget the poems, and the songs. Eva, Zuzana and Gabriela—their pictures, see . . .

RAJA: (snatching them away). No. They will burn them, too! (She tries to rip them.)

IRENA: (Retrieving the pictures and holding Raja’s arms). Raja, listen to me. You are no longer a child—this minute, you are no longer a child—and so I tell you . . . (She gently forces RAJA to sit down and, holding her hands, continues.) I have a child— she is nine years old—she was torn away from my arms and thrown from the train by an angered guard. I tried to throw myself after her—but I was dragged back into the car. I wanted to die until I came to Terezin and found thousands of children waiting for me—and then I knew I must not die . . . Do you understand? (RAJA turns away in despair. She rises with a new-found strength and walks downstage.)

RAJA: One by one the transports came. Mother, Father, Aunt Vera—they went . . . Everyone I knew and loved in Prague. There was no one who could remember me before I had come here as a child of twelve . . . (RAJA follows the train with her eyes as it leaves. As her eyes move across the stage she sees HONZA. He turns to her.) You’re Honza Kosek. I heard about you. My name is Raja—Raja Englanderova.

HONZA: My father was beaten and left for dead before my eyes. I saw it. I couldn’t move; I was so afraid. But I didn’t run. I never understood it—until my father dying told me, “You’re a good boy, Honza; you are afraid, but you are not a coward.”

RAJA: (ashamed) I’m sorry . . . (she starts to turn away)

HONZA: Wait . . . I saw you in the field today. Of course I couldn’t say anything. Maybe we could plan a way to meet there—in case . . . there are messages . . . or anything. Raja, I have some flowers for you . . . You know the square in front of the tower . . .

RAJA: The prisoners aren’t allowed there…

HONZA: I know, but they can’t stop us from looking at it. Look, from here . . . see the flowers near the corner -- and the butterflies? Well, I’m giving them to you, and every time you pass . . .

RAJA: I’ll say—they’re mine. Honza gave them to me—all the flowers—and all the butterflies. Thank you, oh, thank you . . .

HONZA: (haltingly) I won’t be here—for a few days…

RAJA: Why? Where are you going? (frightened) Honza, what is it?

HONZA: Nothing. A special detail to build something outside the fortifications. They’re picking the strongest—I’ll be chosen. There’ll be a chance for extra food. (Smiles) Maybe fresh bread.

RAJA: I don’t care about bread…Honza, I’m afraid!

HONZA: Don’t worry—they want the job done—it’s some kind of walled courtyard . . . nothing much can happen . . . Well, I have to go . . .

RAJA: (reluctantly, almost angrily) Good-bye then . . . (They walk together to the edge of the lighted area. HONZA walks into the darkness) Good-bye. I’ll be waiting . . . waiting . . . Please come back.(She sits with her head in her hands) (to audience) (to audience) Good-bye. It was the motto of Terezin. It should have been written over the entrance instead of the lie that greeted newcomers: “Work makes us free.” It was good-bye, not work, that made us free. It was the only thing we knew would never change. Good-bye . . . good-bye . . . good-bye. It freed us all. What was there to fear when you had said good-bye to everyone you ever loved? I’ve been holding my breath for two days . . . waiting . . . waiting . . . I couldn’t think of anything else but Honza!

IRENA: (IRENA calls from a lighted area a distance away) Raja, Raja, it’s all right. A message came through. The boys are back . . . all of them! What would you have done if he had not come back? If weeks and months had passed?

RAJA: Waited . . . and held my breath . . . for tomorrow . . . then waited again.

IRENA: Waiting days are long days, Raja. You would learn to stop thinking of tomorrow and to keep alive today. That’s the secret of waiting—remember that—to keep alive today. Afraid of tomorrow? Then think of today—now. Can you live until tonight? (Raja nods. Intensely) And tomorrow morning . . . do you think you can live till noon? (Raja nods again) And at noon, in the heat and the hunger, the stench and the weariness . . . can you live until night?

RAJA: Yes, yes . . .

IRENA: Then you will survive. Each day you find some reason . . .

RAJA: (aware of Irena’s meaning) As you have done.

IRENA: Yes. Somehow—one of us is sure to survive. One of us must teach the children how to sing again, to write on paper with a pencil, to do sums and draw pictures. So we survive each today . . . (lights down on scene)

RAJA: (walking to the edge of the stage) The singing, the reading, the learning—the poetry and the drawings—that was part of our survival. In spite of the SS guards and the orders against teaching, Irena kept school in the children’s barracks. An older boy was always on guard and at the sight of the SS men he whistled, and teaching turned into children’s games. Games were permitted, but learning was a crime—for Jews. (Lights come up on Irena, ready for transport. She puts a shabby jacket over her shoulders and sits down with a stub of a pencil to write a note. Her voice is heard as she writes.)

IRENA: Raja, Raja Englanderova, you know by now that my number—102866—was called; when you come to school today you will see that I have gone. (She rises and goes to the side where she enacts the following) I have wrapped up the last of the pictures and poems in my shawl. See that these are buried with the rest— somewhere. And remember what they mean to all of us. I have nothing else to give you but this—what you and all the children have made of Terezin—the fields, the flowers, and all the butterflies . . . Good-bye . . . (She places the rolled package tenderly near the letter. She leaves with a last look. The light stays up on this last remembrance of Terezin, then slowly dims to black) (Raja steps out of the darkness into the light.)

RAJA: Irena Synkova, perished at Auschwitz, January 28, 1945 . . . And I have survived. Mother, Father, Zdenka - - Honza. Irena, too, in the end, perished at Auschwitz and I, Raja Englanderova, after the liberation returned to Prague— alone, alone. (A dim light comes up on a group standing upstage huddled in the background. As the lights grow brighter, they turn, each addressing Raja in a quiet voice as if from a great distance.)

CHILD II: For seven weeks I’ve lived in here. Penned up inside this ghetto. But I have found my people here . . .

IRENA: Now you are not alone. And you must not be afraid.

HONZA: I never understood, until my father, dying, told me: “You are a good boy, Honza. You are afraid, but you are not a coward…”

IRENA: Somehow one of us is sure to survive. One of us will teach the children how to sing gain, to write on paper with a pencil, to do sums and to draw…

HONZA: Raja . . . I am with you wherever you are.

IRENA: I have nothing else to give you but this…the fields, the flowers, and all the butterflies . . . (As the voices grow in intensity, Raja turns to view the people who have called to her from the past. She speaks to each…)

RAJA: Mother, Father. I hear you. Honza, I hear and remember…Irena Synkova, I remember. (She picks up the sack and adjusts her coat. She pushes up the sleeve of the coat and looks at a number on her arm, then determinedly, pulls down her sleeve. She faces the audience again.) My name is Raja—I am a Jew; I survived Terezin—not alone, and not afraid. (She walks slowly across the stage. Lights dim to black as music rises.)
```

---

## IC-0809: I Wanna be a Cowboy

- Title: I Wanna be a Cowboy
- Author (byline): Jon Tuttle
- Work: More One-Act Plays for Acting Students
- Publisher: Meriwether Publishing
- Publication date as stated: July 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: WALTON, NELLA
- Teaser before the introduction: No
- Spoken words (computed): 1899
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jon Tuttle
Book: More One-Act Plays for Acting Students
ISBN: 1566080878
Publisher: Meriwether Publishing
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
WALTON: Ya hear all these kids sayin’ “I wanna be an astronaut..

NELLA: or a rock star

WALTON: or a lawyer

NELLA: or a doctor”

WALTON: not me.

BOTH: “I Wanna be a Cowboy”

NELLA: By Jon Tuttle

(NELLA and WALTON occupy seats next to each other. She has the aisle seat: He stares wistfully out the window next to his seat and jingles quarters in his beefy palm. She is staring at him - or with him, out the window, wondering at his deep, blue mood - when the bus suddenly runs over something in the road. He doesn't move or break his stare, but after a moment, he breaks the silence)
```

### Performance text (classify this)

```text
WALTON: ... 'Dilla.

NELLA: ... Escuse me?

WALTON: 'Dilla.

NELLA: ' Dilla?

WALTON: 'Dilla, Ya hit 'em, they explode. Squirt out both ends like a burrita.

NELLA: ... Arma ...dilla?

WALTON: (Still looking out his window) Stupidest critters in Texas. Sit on the road like a idiot an' watch ya comin'. Then the highway department comes along'n paint yella lines right over their stupid backs. (At the indignity of it) Huh. Huh.

(NELLA contemplates the image, and he yanks off a bite of jerky, his head snapping back. Not wanting to lose the conversational momentum, she loads up a sentence and misfires.)

NELLA: ... To where are you goin' to?

WALTON: ... Dallas.

NELLA: ... We are as yet a considerable long distance to go to Dallas ... You cannot see Dallas at this time from where we are ... at.

WALTON: (Turning to her) I know that. Ya think I'm stupid? Ya think I'm some sorta idiot? - Shee! (He yanks off another bite and looks back out his window. Pause. Nella resists, but then bursts into tears. She sputters, like she s trying to swear at herself.)

NELLA: Hep! Kuh! Fut!

WALTON: (Turning again, dumfounded) ... What?

NELLA: Shup! Purt!

WALTON: What?

NELLA: What am I sayin'? I never know! Kufl

WALTON: Ya got some snot on yer chin.

NELLA: (Quickly wiping it) I'm sorry! I'm sorry what I implied! I think it all through! I try to be soooo - (She pants hard, like some Lamaze breathing drill, trying to pull herself together. He doesn't know what to do.)

WALTON: ... Want some jerky?

NELLA: (Composing herself) No, no thank you. I'm sorry. I'm terrible sorry.

WALTON: 'S OK. Ya got some more on yer cheek.

NELLA: Thank you. I'm sorry. (She wipes her cheek, and he turns back to his window. She dries up a bit and tries again, tentatively.) What are... I mean, for what are you looking... for?

WALTON: .., I'm scared.

NELLA: ... Of what are you scared of? (But Walton cannot articulate it. He just shakes his head, stares, jingles and chews. Nella presses on. Indicating his shirt) Are you a student at the Texas University of A&M?

WALTON: Pff. Hell no. Not no more.

NELLA: I am on my way to be a freshman at the Texas Christian University. That's in Fort Worth. That's near Dallas.

WALTON: (Sharply) I know where Fort Worth is. (Her lip quivers, but she fights it, and hangs in.)

NELLA: I am from Clancy, Arkansas. And you?

WALTON: (Out the window: the sum total of all his hopes)... I wanna be a Cowboy.

NELLA: A cowboy. How very fascinatin'.

WALTON: (To himself, mostly) I'm gonna be a Cowboy, too. I am.

NELLA: Like Gene Autry?

WALTON: Like Walt Garrison.

NELLA: I do not believe as I with him am familiar. I don't know him.

WALTON: (Turning to her now) He's my hero. Ever since third grade with Miss Slocum. Got his poster up over my bed. Greatest Cowboy what ever lived. We got the same name almost, too. I'm Walton Dwight Pritchard. He's Walt Garrison. (He yanks off another bite.)

NELLA: How very fascinatin'. Does he sing?

WALTON: (Baffled)... I dunno.

NELLA: Do you have your own horse?

WALTON: ... Uh-uh.

NELLA: Oh, well, they'll prolly let you borrow one.

WALTON: In high school I won a trophy.

NELLA: A trophy. How very fascinatin'. My high school, which is in Clancy, they awarded me a scholarship to go to any good Christian school to which I wanted to go to, in so far as much as it was within a reasonable radius and had academic credentials. (WALTON yanks off a bite.)

WALTON: How come ya talk like that? That the way they talk in Arkansas?

NELLA: (Wells up.) Hep! I'm sorrow! (She starts crying again. Walton is confused again. He looks at his jerky, contemplates offering it again, looks up at her, down at it, back and forth, while she tries to regulate her breathing.) My mamma, she says I got to go to a big school like Texas Christian is, so I can git my social graces on account'a I never know what I'm sayin'. However, I don't wanna go away to college. I just wanna stay at home.

WALTON: Yeah, well, college sucks.

NELLA: When I was a little girl? I wanted to be a cowgirl. On Career Day? At Hazelwood Elementary? I stood up and I said I want to be a cowgirl. But Joey Ray Draper, he said I already was, and then he mooed. By which he meant I was fat.

WALTON: Grade school sucks too.

NELLA: I wanted to wear one a them little cowgirl hats and vests with fringes and all and boots and be like Shirley Jones.

WALTON: Who's she?

NELLA: She was a cowgirl. You know, from "Oklahoma!"? She had pretty blond hair and she wasn't skinny but she-

WALTON: Oh yeah! She was in the poster what they done!

NELLA: I don't know 'bout no poster. That was a long time ago.

WALTON: That's her! Big Ol' blonde right up front. I didn't know she was from Oklahoma, is all. Them cowgirls, my Lord, they sure are a sight, huh?

NELLA: I was too fat, though.

WALTON: And you know them cowboys, they're gettin' some a that. Be fine by me. That's a laugh, huh! (He snorts.) Them cowgirls, that'd be a joke. They wouldn’t even pay me the time a day. Even if I was a cowboy. Even if I was the greatest cowboy since Walt Garrison.

NELLA: How come?

WALTON: 'Cause I'm stupid. (He yanks off a bite, matter a/fact-like.)

NELLA: Y'are?

WALTON: I'm a idiot. Been that way all my life. Least as far as I can remember. Which ain't very.

NELLA: I was fat once.

WALTON: Ask my daddy. He says I'm stupid to think I'm gonna be a cowboy. He says I should stay in Plano an' be a roughnecker like him on the oil field. He even, look here, he even give me these here quarters so's I can call him when I need a ride back home cause I'm too stupid to be a cowboy.

NELLA: You don't seem stupid to me.

WALTON: I don't?

NELLA: Nope. All the kids at Clancy High School? They were stupid. All the kids at Chester A. Arthur Middle School, they were stupid too, and the kids at Hazelwood Elementary? They were really stupid. You ain't stupid compared to alla them.

WALTON: Eh. I can't open my mouth without stickin' my butt in.

NELLA: Well... cowboys don't talk much, do they?

WALTON: That's true, huh.

NELLA: They're famous for their stoic - stois - they don't talk much.

WALTON: All my life, it's all I ever dreamed of. 'Specially Sunday afternoons, when they were on TV.

NELLA: Uh-huh, I watched 'em.

WALTON: Monday nights, too, when they were on. Cowboys were my heroes.

NELLA: Mine too, uh-huh.

WALTON: Really?

NELLA: Cowboys are most people's heroes, I always thought.

WALTON: Eh. Nobody ain't got no respect for 'em no more. Not like in the olden days.

NELLA: Oh, I think they got a pretty firm place in our sociology.

WALTON: Ya think so?

NELLA: Uh-huh. Look at what all the cowboys stand for. Bravery. Integrity. Hard work.

WALTON: America.

NELLA: America. Freedom.

WALTON: They're against drugs, too.

NELLA: And you can't blame them for what happened to the Indians.

WALTON: Ya mean the Redskins?

NELLA: Uh-huh. The cowboys, they didn't represent the umperialism inherent in manyfest destiny. Quite the opposite, I'd say. Wouldn't you say?

WALTON: Yeah, but I hate the Redskins. What the Cowboys need now is to whomp the hell outa them again, at least one a year, like on Thanksgivin', just like the olden days. Wouldn't you say - what you say your name was?

NELLA: Nella. Nella Overholt.

WALTON: I mean, lookit where they are. Broncos run right over 'em now. How often that used ta happen?

NELLA: I didn't know it was that bad.

WALTON: It's pitiful. If they ain't careful, they're gonna wind up like ...the Falcons.

NELLA: You mean endangered?

WALTON: Exactly. Or Buffalo. Who gives a damn, I mean, who really gives a damn 'bout Buffalo any more?

NELLA: I thought they were extinct.

WALTON: They were, fer awhile. Bears, who can say with them. But the Dolphins? Lookit the Dolphins.

NELLA: Getting slaughtered by the thousands.

WALTON: Exactly!

NELLA: Or the California condors.

WALTON: ... I ain't never heard a them.

NELLA: That proves my point.

WALTON: Exactly! And that's how the Cowboys are headed! I can't let that happen. No red-blooded, born and bred son a Texas can! I could help 'em get back to where they was, I swear I could! If I could be a Cowboy... God! Wouldn't people look up to me! Everybody in Plano! Everybody at A&M! Me! Walton Dwight Pritchard! Cowboy! (The verv notion has pulled him to his feet. He takes his hat off and places it solemnly over his heart. NELLA is getting aroused.)

NELLA: (Heating up) Oh, I would! I would!

WALTON: Would ya? Would ya really?

NELLA: I swear to God I would! Specially when you were on your horse!

WALTON: (Baffled again) But ... I ain't got no horse.

NELLA: You gotta believe in yourself, Walter!

WALTON: (Shaking his head sadly) Eh. It ain't so easy, believin' in yourself, when ... when ...

NELLA: When what?

WALTON: (Earnest) Nellie, yer a smart person, I can tell that. Ya know what yer talkin' 'bout. So I need to ask ya a question here. It's kinda personal though, an' I ain't ever asked it to no girl before. So I need ya to answer straight-forward.

NELLA: (Hoping) OK.

WALTON: (Experimentally) Nellie. Do ya think ...

NELLA: ...Yes?

WALTON: Do ya think... see, the thing is ...

NELLA: Yes? Yes?

WALTON: The thing is ... I got a trophy, see. An' I'm strong. Once, when I was at A&M, I hit a Texas Longhorn. Big sucker, open field, dead run. Broke two a his ribs. My Christ, the sound he made when he hit the ground! An' I stood up and waved my fist in the air ... Yeeeow! And I spit on him.

NELLA: (Totally turned on; overpowered) You broke ... the ribs ...of a longhorn?

WALTON: Uh-huh. How's that? Ya think I could be a Cowboy?

NELLA: Sweet Jesus, yes! Yes, I do!

WALTON: Yee-hoo! I knew I could! Daddy said I couldn't! Everybody said I couldn't! But I got somethin' in me, see, what says I can. I got desire. Ya gotta have desire, Nellie!

NELLA: (She’s SO got it.) Oh, I know! I know!

WALTON: If ya got desire, Nellie

NELLA: I know!

WALTON: Ya can survive bein' stupid. Is what I say. But at A&M, they didn't see it that way. They - eh.

NELLA: What? They what?!

WALTON: Listen to me. You don't want to sit here and listen to me ramblin' on like a idiot.

NELLA: Yes, I do! This is the most intelligent conversation I've had since I don't know when!

WALTON: Me neither! At A&M, they kicked me out fer bein' stupid. They didn't say exacly that, but I knew it's what they meant. It's what everybody says. My daddy, he says Plano is the place fer a man like me, cause it's only Plano, and everybody's stupid. But I got desire! It burns in me like battery acid! I wanna be a Cowboy! But there's only one thing, one thing what I'm ascared of

NELLA: (Holding his hand tightly) What's that, Walter? You can tell me!

WALTON: (The horror, the horror) ... I'm ... stupid.

NELLA: Oh, Walter!

WALTON: A thousand Texans can't be wrong! It burns in me day in and night out! An' the girls? They - pff. Pffff. They never even pay me the time a day. Not like you are here.

NELLA: (Some spite here) Most girls are petty and mean and self centered and vain and superficial and ignorant and mean and they only care about one thing.

WALTON: Basketball.

NELLA: Exactly. I hate basketball.

WALTON: Basketball sucks.

NELLA: I hated school altogether.

WALTON: Me too. Sucked. If I hear that word stupid one more time

NELLA: I was fat. All through high school.

WALTON: (Diplomatically)... No.

NELLA: I've lost seven pounds over the summer. Of course, there's still room for improvement.

WALTON: You ain't too fat.

NELLA: Well, no, not no more. Not as fat.

WALTON: You ain't fat at all.

NELLA: Well, I'm

WALTON: No, I've seen fat. Fat's bigger'n what you got there. Fat's all puffy and white an' you can draw yer name in it with yer finger. You ain't fat. .

NELLA: At my high school reunion I'm going to lose forty-eight pounds. I already lost seven.

WALTON: When's that?

NELLA: Ten years. I'll be skinny as a post. And when they ask me who I am, I'll say

WALTON: Say, I'm Shelley Jones. Cowgirl!

NELLA: Maybe so!

WALTON: An when they ask ya to dance, you can laugh in their stupid, ugly faces.

NELLA: Well, I don't know if

WALTON: It'll make 'em feel stupid. I know.

NELLA: (Protests too much.) Well, maybe some of them. Like those idiots who strutted down the hall with their rippling biceps and big shoulders and washboard stomachs and granite thighs and hairy chests and letter jackets and never saw anybody but the cheerleaders. God, I hated them.

WALTON: Cheerleaders are sluts.

NELLA: I mean the basketball players and baseball players and football players and tennis players and wrestlers and golfers and

WALTON: Ya hated ... football players?

NELLA: Are you kidding? They're the worst! I hated them with a passion. I hated them with a burning, smoldering passion! If I had a nickel for every second I spent hating them

WALTON: How come ... ya hated ... football players?

NELLA: (Isn't it obvious?) ... Because ... football players are stupid! They're idiots. I never met a football player who wasn't as stupid as he could be. Wouldn't you say? (Pause)

WALTON: ... Yeah. I guess so. (Pause, WALTON looks out his window and begins to jingle his change again. Then he turns back to NELLA as if to say something, something hard, but sees her there, looking at him expectantly, hopefully So he puts his hat back on and stares out his window. The bus hits something They jostle a bit, and she squeaks again, softly)

NELLA: (Happily, confidently) ... 'Dilla. (She sits smiling at the back of his head.)
```

---

## IC-0810: If I Could Paint the Rain

- Title: If I Could Paint the Rain
- Author (byline): Rosary O’Neill
- Work: 2006: The Best Ten-Minute Plays for Two Actors
- Publisher: Smith and Kraus
- Publication date as stated: 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ROOSTER, MONICA
- Teaser before the introduction: No
- Spoken words (computed): 1019
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rosary O’Neill
Book: 2006: The Best Ten-Minute Plays for Two Actors
ISBN: 978-1575255637
Publisher: Smith and Kraus
Date (Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Rooster Dubonnet is a French artist coming to grips with his last days fighting cancer. The end is near. He knows this.

ACTOR: I just want to be left alone, and not be pestered by a new nurse – Ms. Falcon

ACTRESS: Nurse Falcon isn’t the type to give in. But can she connect with him in time?

TOGETHER: If I Could Paint the Rain by Rosary O’Neill

The dayroom of a Garden District mansion, New Orleans, Louisiana. Rooster Dubonnet, a young man, twenties, dark-haired, gaunt, almost emaciated, lies in bed in silk pajamas. A painter who has pushed himself beyond reasonable limits. He is critically ill from cancer. The disease gives him a distinct nonchalance, the charm of the damned. If he were not so sick and pasty-looking, he could be handsome with strong features, thick hair, and broad shoulders. Even so, there are kindness and nobility in his face.
```

### Performance text (classify this)

```text
ROOSTER: I'm cold. Maybe the rain makes me that way. It's full of emptiness. Cold blue in the morning, bright blue at noon and intense Italianate blue in the late afternoon. The walls soak up the rain. There is vermilion in the shadows, violet in the gray. Like the sound of everything that's there, that I try to paint. When you are inside the rain, there's luminosity. I want images that have the density of rain. Nature does it easily. When you try to copy it, it's gone. Rain's not easily captured. It's the pink lie, the last little thing that crawled out of Pandora's box with all her colors. If I could paint rain the way it is, thick and smelling of oak leaves, I could figure life out.

(Rooster closes his eyes. Monica Falcon, a stunning nurse, twenties, arrives. Delicate features match her gentleness: fine skin, graceful hands, hair that tumbles about her face. She is dressed simply but impeccably and holds a satchel under her arm. She pauses at the doorway, removing her cape and looking about in the house.)

MONICA: Hello, hello ... anyone there? I'm Monica Falcon, the new nurse.

ROOSTER: What? (Calls out.) Ma.

MONICA: (Puts thermometer in his mouth.) Are you in pain?

ROOSTER: No. (He pulls out the thermometer, leans to an intercom)

MONICA: You sounded as if you were in pain.

ROOSTER: (Into the intercom) Ma, pick up.

MONICA: Everyone's gone.

ROOSTER: Unlikely. (Into the intercom) Pick up, I said.

MONICA: The house echoes quiet.

ROOSTER: (Into the intercom) Ma. They sent a woman.

MONICA: You've a wonderful house ...

ROOSTER: (Into the intercom) I asked for a male nurse.

MONICA: It's like a hotel.

ROOSTER: (Into the intercom) You're not my guest. I'm not lying about halfdressed with a woman. (Monica checks about for lights.)

ROOSTER: Don't.

MONICA: Do you live in darkness?

ROOSTER: Best way to survive in the Garden District.

MONICA: (Looks at her feet.) These shoes looked good before I walked through water.

ROOSTER: Click your heels and go back to OZ.

MONICA: We can catch the last rays of the sun.

ROOSTER: You're not staying. (He sits up, reaches for his robe, but is still weak and has to breathe a few moments. She looks out the window. He reaches for the phone.)

MONICA: The light feels good. Cold bracing sunshine, right behind the rain. That'll keep you awake.

ROOSTER: (Into the receiver.) Is this the Parker Agency?

MONICA: I love a bright afternoon sky.

ROOSTER: This is Rooster Dubonnet. I requested a male nurse.

MONICA: (Reaches for the phone.) Give me that.

ROOSTER: (Stretches phone away, panting, talks into it) I'm not paying for this woman.

MONICA: What do you have against women?

ROOSTER: (Into the phone.) I was nice to those rejects you sent. She can't be the only nurse who'll come.

MONICA: (Takes out a blood pressure kit.) I'll take your blood pressure.

ROOSTER: (Into the phone.) You said you had 200 nurses. (Into the phone.) I don't want this woman. (Into the phone.) Tell her to leave.

MONICA: (Takes phone, speaks into it) Everybody's fine. (Hangs up. To Rooster) One, two, three ... up. (Rooster sits up, very weak, wraps his robe limply over his silk pajamas.)

ROOSTER: Stay away. I'm warning you.

MONICA: Let me help you to that chair.

ROOSTER: I'm calling the police. (He reaches for the phone, but she grabs it and puts it in her pocket.)

MONICA: I'll change those sheets. (He stumbles to his feet. He is panting for breath, totters, and grasps onto furniture. He stops for a second. She watches him from the corner o/her eyes and goes to make the bed.)

MONICA: You can do it?

ROOSTER: I can do it. (He presses a hand alarm, which blares. They struggle for the alarm. She pushes it off)

MONICA: What's that? Turn it off.

ROOSTER: Not likely.

MONICA: Give it over.

ROOSTER: No.

MONICA: (Pulls alarm from his fist.) You think you can get rid of me?

ROOSTER: You're the roughest ...

MONICA: My landlord's evicted me.

ROOSTER: Toughest ...

MONICA: Called me at five AM.

ROOSTER: This is not a hotel.

MONICA: I've no friends or relatives here.

ROOSTER: That's the first good news about you.

MONICA: I'd like to help. (He walks, but stumbles. She calls out as he moves cautiously along.) Take my arm!

ROOSTER: I'm not some bag you can carry around.

MONICA: Can you get to that door?

ROOSTER: Uh-huh. If I push myself I can. (He walks carefully. Reaching the door, he rests his head back, then turns and sets off a strobe light siren. She runs over. They struggle for it.)

MONICA: You crazy ...

ROOSTER: You want to hear the sound of a siren ...

MONICA: Out of my way!

ROOSTER: I'm weak, but I can do it.

MONICA: Stop. Nobody's going to bail me out. (She turns the siren off He staggers to a chair and leans over the back, coughing.) Have you had anything to eat? Or drink?

ROOSTER: Not today.

MONICA: (Hands him glass.) Take a few sips.

ROOSTER: No, thanks. Have you ever heard of the nurse who poisons the emperor? This emperor so feared assassination, he only ate ripe figs from a tree.

MONICA: Drink.

ROOSTER: In the night, his nurse injected them with poison.

MONICA: Just ...

ROOSTER: I n the morning, the emperor ate one and died. (He drinks a little, then pours water on a plant. She speaks continuously, overlapping him.)

MONICA: Since you won't let me help you, may I ask you some questions?

ROOSTER: What's that?

MONICA: I'm studying astrology ... on the side.

ROOSTER: It's amateur night in Dixie.

MONICA: I looked you up. You've got a tenth house, Pluto in Leo.

ROOSTER: Fortune-tellers. They're everything I'm running from –

MONICA: Which means you're gifted ...

ROOSTER: (Breathing fast.) The whole spectre of charlatans –

MONICA: At being able to ...

ROOSTER: That haunt artists' history.

MONICA: Translate archetypal energy ...

ROOSTER: I'm three times more likely to die from the flu ...

MONICA: Through the power of the personal image ...

ROOSTER: Than to speak to a student astrologer. Y' all are the psychos of the science profession.

MONICA: Think you can get in that chair?

ROOSTER: Uh-huh. If I'm careful, I can.

MONICA: I know you're a famous artist from a well-to-do family ...

ROOSTER: Why do people pursue me?

MONICA: May I ask you some questions? It would make my job easier.

ROOSTER: You haven't a job with me.

MONICA: You're so ...

ROOSTER: Difficult? Some artists don't do interviews, and thank God they don't do them. I don't want to be the entertainment.

MONICA: And you're not. (Rooster rises with effort, crosses to the birdcage, whistles ”Dixie.”]

ROOSTER: My parrot, Commander Butler, just flew in.

MONICA: Where?

ROOSTER: He died but sometimes he visits. He's my very special house ghost. The two things Butler does best are scream, "Where's the maid?" and whistle, "Dixie." Calling the maid is so passe. (Pause) You think I'm crazy.

MONICA: No. What's your diagnosis?

ROOSTER: I belong to the National Caged Bird Society ...

MONICA: Your symptoms?

ROOSTER: But I couldn't make that bird talk.

MONICA: How long have ...

ROOSTER: Butler's a Southerner from French aristocrats ...

MONICA: You been sick?

ROOSTER: He was bred by a gentleman who kept his plantation up river. One difference between Butler and me. He's dead and I'm alive. But I'll be flying off soon. (Pause) Are you from the South?

MONICA: Delaware.

ROOSTER: Y'all like to eat on paper plates in halls covered with graffiti. What do you have going for you? That's what I want to know.

MONICA: My husband was from Jackson.

ROOSTER: There's a touch of Mississippi in your family? What does Mr. Falcon do without you?

MONICA: My . . .I . . .. Oh Lord . . . . . . . I mustn't let ... Where're my Kleenex? . . . . . . You think I'd be here if I . . . . . . .

ROOSTER: Take my handkerchief. (She does.) Don't start the sadness machine.

MONICA: It happens frequently. I'm so tired, and broke. It's not professional. I don't want to be so emotional. Your bed is ready. (Rain pours around the sides of the room. She removes the thermometer, writes something on her chart. He pulls a sketchpad from behind a seat.)

ROOSTER: I've not stopped painting because I wanted to. This morning I said to myself, I'm going to paint, if my energy holds out ... Soon as it's warm and the sun's shining ...

MONICA: Well? (Rain begins whistling around. He rubs the armrests)

ROOSTER: My energy didn't hold out ... Listen to that rain blowing round outside.

MONICA: It sounds neighborly.

ROOSTER: Coming right through the sun.

MONICA: I love to hear it when I'm inside.

ROOSTER: Oh, but it's cold walking into the rain when you have to. (Begins to shiver.) Look at me shake, will you? The thought of rain and I start to shiver.

MONICA: Try to nap. Would you like another blanket? (He lies back slowly. She covers him.)

ROOSTER: That does feel good.

MONICA: I told you. (He has closed his eyes and gone to sleep. Monica watches over him as the lights are brought down. The lights come up.)
```

---

## IC-0811: I’m Not Stupid

- Title: I’m Not Stupid
- Author (byline): David E Rodriguez
- Work: Telling Tales: New One Act Plays
- Publisher: Penguin
- Publication date as stated: March 1993
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MA, DR. GREEN, BOTH, DR.GREEN
- Teaser before the introduction: Yes
- Spoken words (computed): 1983
- Already set (do not supply): none

### Source block (context only)

```text
Author: David E Rodriguez
Book: Telling Tales: New One Act Plays
ISBN: 978-0140482379
Publisher: Penguin
Date (Month/Year): March 1993
```

### Introduction (context only: never use it for content warnings)

```text
During the Intro, both Characters speak as “Roger,” a mentally disabled young boy:
```

### Performance text (classify this)

```text
MA: These are the words of my son

DR. GREEN: My patient

BOTH: Roger.

MA: I was watching the Little Rascals on TV, they had a clubhouse . . .

DR. GREEN: and I wanted a big clubhouse like the Little Rascals' . . .

MA: I'm not stupid! You need WOOD to build a clubhouse, and there is a lot of wood in the junkyard.

DR. GREEN: I could get wood from the junkyard to make me a little house like the Little Rascals'.

MA: I was going to sleep in it, and Pa too.

DR. GREEN: We were going to sleep in the clubhouse like the Little Rascals.

MA: I went to the junkyard and got a lot of wood. . .

DR. GREEN: I'm not stupid! You need nails, I had a lot of nails. . .

MA: and you need a box, you build it like a big box, but it's turned upside down . . .

DR.GREEN: I'm not stupid! I could make a clubhouse,

MA: you need a hammer for the nails. Pa had a hammer, he had a big hammer.

DR. GREEN: Like this big.

MA: It was in the house. . . and I went into the house to get the big hammer.

DR. GREEN: I asked Ma for Pa's hammer.

MA: She started to cry.

DR. GREEN: She told me Pa wasn't coming back.

MA: I'm not stupid! I know Pa was dead

BOTH: “I’m Not Stupid”

DR.GREEN: By David E Rodriguez

MA: (drunk, but not noticeably so) Dr. Green?

DR. GREEN: Good afternoon, Mrs. Fletcher. Please pardon this intrusion. I tried calling, but your phone is out of order. Your son Roger didn't keep his appointment. Do you know where he is or if he left?

MA: He's at the junkyard.

DR. GREEN: This is most peculiar. All the years I have known him, he has never missed an appointment.

MA: Wait for him here. He'll be right back, and I do have to talk to you.

DR. GREEN: I see. Then I'll wait. (He takes a seat.) So, what is on your mind?

MA: I was thinking about that question you asked me, if I loved Roger. And I've been thinking; I love Roger. It's the kind of love you have for a pet. . . a dog, maybe. You give it a bath, feed it, clean up after it. Don't get me wrong, Dr. Green, did you expect me to love him as a son? How can I? He can't do anything, except eat and sleep, like a dog. I'm not mean. That does not make me mean. Did you ever wonder if a dog loves? I say that people say that dogs love, but that is just because you take care of it. They'll go back to sleep until they're hungry again, and then come back for more. They don't know where the food comes from, as long as it tastes good. They'll eat it, then they'll go back to sleep. . . Roger sleeps a lot. In a way, Roger isn't a person. He's a dog. You give him what he wants, and he stays happy, right? That's right! It's true! So why should I love him as a son, when he's a dog. Don't look at me like that, Dr. Green, you know what I'm saying is true. Why don't you just put away all that mumbo jumbo about a person is a person, and wake up and see that Roger is really a dog, that talks. A talking, walking, big ol' dumb dog, and maybe you could understand what I'm saying. So you can stop looking at me like that! I'm not stupid, I'm smart. Do you think I'm smart? I think I'm smart, this is my opinion. It is my opinion that Roger is a dog. So what? What's so wrong with that? Kill me, for cryin' out loud, but at least I loved him. I kept him happy. No, I mean, I love him and I keep him happy. Sometimes I mix words around, but I'm still smart, and he's still happy. So you see, there's nothing wrong. Roger would even tell you himself, and he will when he comes back, you'll see.

DR. GREEN: I can't believe you just said that. He's your son.

MA: No, he is not. He's no son of mine.

DR. GREEN: No? What is he to you, then?

MA: He's just this stupid, good-for-nothing that took everything I ever lived for!

DR. GREEN: That is not true!

MA: It's true! Since the day he was born I no longer had a husband. Now he's dead because of him.

DR. GREEN: It was a heart attack. Blaming Roger

MA: (interrupting) Henry was strong! He worked day in and day out to pay doctor bills. . . Doctor! He'd come home tired every night. . . . So tired and pale, Dr. Green. How long do you think a man could last doing that without one day his body giving in? I saw it. I told him to stop. I told him to send Roger away so he wouldn't have to work so hard. But no, he loved Roger. That man gave more love to that idiot than he gave me in seventeen years!

DR. GREEN: I see. So what are you going to do now? Make him suffer? Treat him as if he were some kind of animal? What do you want?

MA: I want what I deserve!

DR. GREEN: And what is that? Money?

MA: It isn't about the damn money!

DR. GREEN: Okay. . . . What, then? . . . What? (Pause.)

MA: If you don't like the way I treat him, why don't you have him sent away?

(Pause.)

DR. GREEN: (They overlap for next few lines.) This is all about the money. . .

MA: You're wrong. . .

DR. GREEN: We both know that if Roger is sent away, you'll be awarded his trust money. . .

MA: I want to go on with my life. . .

DR. GREEN: . . . I won't be able to provide services for him; thus I will no longer oversee the account. . .

MA: . . . I deserve some peace. . .

DR. GREEN: . . . making you the beneficiary of your husband's will, isn't that right? What else could it be? (Overlapping ends.)

MA: You don't know everything, you have no idea!

DR. GREEN: Come now, Mrs. Fletcher, you said it yourself, he's not your son. All Roger is, is one big dollar sign.

MA: He's an idiot. He's never going to get married and have kids. He's never going to have a job, much less take care of me when I get old. I'm lonely, even if Roger is around. Maybe. . . maybe I should get a real dog or something, what do you think? I'll bathe it, take it for walks, clean up after it. I have had years of experience. . .

DR. GREEN: You're drunk.

MA: So I'm drunk, what does that have to do with it? I'll still feel the same when I'm sober. I'll still want a dog. . .

DR. GREEN: Mrs. Fletcher, I think we ought to talk about this again, when you sober up. Obviously you're not yourself. Until then, I will look for Roger. If you will excuse me

MA: No, stay here. Roger will come back. He's probably on his way and it's so cold outside.

DR. GREEN: I appreciate your concern, but I think I really ought to

MA: I gave him the hammer.

DR. GREEN: What?

MA: I did. After that, he went rushing out the door to the junkyard.

DR. GREEN: Well, that explains it. It was good of you, you know. You did something.

MA: I know I've been really hard on him for some time. You see, I'm not mean. I think I'm turning over a new leaf. I was just angry over Henry's death, that's all. Now, I'm over it.

DR. GREEN: Really?

MA: You say that as if you don't believe me. I may be drunk now, but this is the last time. I'm going to be a new woman, you'll see.

DR. GREEN: I see. A moment ago Roger was a dog.

MA: Oh, that. Really bad example, wasn't it?

DR. GREEN: I would say so, but

MA: You know, I never knew what the "K" stands for in "Dr. K Green. "

DR. GREEN: Karl.

MA: Karl-that's a nice name. Do you mind if I call you Karl?

DR. GREEN: If you prefer.

MA: I would. I don't know, "Dr. Green" sounds so formal. Don't you agree? So distant, and I would like us to be closer, Karl. Afer all, you'll be treating me.

DR. GREEN: Treating you?

MA: Yes, didn't I tell you? No, I didn't, did I?

DR. GREEN: I don't believe so.

MA: Well, now you know. I've decided to take you up on your offer. I figured some treatment will do me some good.

DR. GREEN: I see.

MA: What's wrong, you don't want to treat me? I know, I'm blowing your mind, right? Oh, don't be surprised, Karl. I was on my bad side for a while like I said before, I'm over that now.

DR. GREEN: Well, then I think that Dr. Green would be more appropriate.

MA: Why?

DR. GREEN: I think it would make our relationship more professional. Now that you are under my care

MA: Oh, don't be such a stiffy? Wanna drink, while you wait? Oh, I forgot, doctors don't drink, right?

DR. GREEN: I don't know about other doctors, I don't.

MA: That's good. I wouldn't want you to either, Karl. Oops, I forgot! I'm sorry.

DR. GREEN: That's all right.

MA: Since you're here, maybe we can have my first session right now.

DR. GREEN: You've been drinking.

MA: Never mind, I'm sobering up already.

DR. GREEN: Really, Mrs. Fletcher.

MA: Call me Margaret, or is that not professional enough?

DR. GREEN: That's quite all right, if you prefer, but as I was saying before

MA: Yes, as you were saying, Dr. Green.

DR. GREEN: I think it would be more appropriate if I asked my secretary to make an appointment.

MA: There you go again, Mr. Stiffy. Do you always have to do things by the book? There's no bending you, is there?

DR. GREEN: I don't know. What do you mean?

MA: You know what I mean. Didn't you do anything wild and crazy when you were young?

DR. GREEN: Like what?

MA: You know, like play a practical joke on your friends, or steal the neighbor's dog? Play a big trick?

DR. GREEN: I have. Not that in particular, but yes, when I was young.

MA: That's what I mean. Come on, loosen up. Let's get a session going here.

DR. GREEN: All right, if you insist.

MA: Great. So what do I do now, lie down?

DR. GREEN: Whatever makes you feel comfortable.

MA: I'm comfortable. What do I do now?

DR. GREEN: Tell me what's on your mind.

MA: Where do I start?

DR. GREEN: Anywhere.

MA: I don't know, I feel funny. Give me a suggestion.

DR. GREEN: All right, why the sudden change in you?

MA: I told you, I'm letting go of the past.

DR. GREEN: Why?

MA: Why not? I can't stay bitter for the rest of my life. Now that Henry is gone, I'm over it. Why don't I start a new life with Roger? Have a chance to be a mother to him? After all, he is my son, isn't he? Forget all that nonsense about him being a dog. I do love him. I guess I've been denying it for so long. . . Well?

DR. GREEN: Well, what?

MA: Aren't you going to say something?

DR. GREEN: Like?

MA: Well, like, I think that you're making a change for the better.

DR. GREEN: I think you're making a change for the better.

MA: You really mean that?

DR. GREEN: Honestly?

MA: Yes.

DR. GREEN: No, I don't believe one word you've said.

MA: What? I can't believe it!

DR. GREEN: I'm a psychiatrist, Mrs. Fletcher. I don't believe in miracles.

MA: But I'm telling the truth! I swear, He's at the junkyard! Who the hell do you think you are, calling me a liar!

DR. GREEN: When did you give him the hammer?

MA: Today! I gave it to him today!

DR. GREEN: What did you make him promise? What did he have to do?

MA: Nothing. Why are you doing this to me! I just wanted him to be happy.

DR. GREEN: How do you know he is at the junkyard?

MA: I took him there myself.

DR. GREEN: Really? Why?

MA: He wanted me to see them build his goddamn clubhouse!

DR. GREEN: Then why isn't he here now? Tell me! Why?

MA: What? What are you accusing me of? Do you think I'd go that far?

DR. GREEN: Go as far as what? GO AS FAR AS WHAT!!! WHAT DID YOU DO TO HIM?

MA: I'm changing, don't you see? I'm not lying! I swear!

DR. GREEN: I'm going to the junkyard.

MA: No!

DR. GREEN: Why not? I'm going, Mrs. Fletcher.

MA: (Clings fiercely to him.) Don't go-please, please don't go! He's there! Believe what I'm saying! He's there!

DR. GREEN: Let go of me! Let go of me!

MA: All right, all right, go then! Go! (DR. GREEN exits.) You think you know everything! Go!
```

---

## IC-0812: Imperfectly Matched

- Title: Imperfectly Matched
- Author (byline): Eric Benson
- Work: Fast Horse Plays, Round 4, Pgs 21-28
- Publisher: Fast Horse Drama
- Publication date as stated: Aug 2012
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: APRIL, ZACK, GRANDMA, EVIL COUNTER WOMAN, GAME SHOW HOST
- Teaser before the introduction: Yes
- Spoken words (computed): 1434
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric Benson
Book: Fast Horse Plays, Round 4, Pgs 21-28
ISBN: 978-0615711379
Publisher: Fast Horse Drama
Date (Month/Year): Aug 2012
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Meet April and Zack . . .

ACTRESS: A chance meeting at a coffee shop – that’s how the best relationships start, isn’t it -- by chance?

ACTOR: (scoffs) By chance is better that on a dating site! When you meet in person you can tell if there’s chemistry right away.

ACTRESS: One little thing, one choice or accident or joke can change our lives forever –

(blissful sigh) Chemistry. . .

ACTOR: But is “chemistry” enough to save a relationship when you are . . .

TOGETHER: Imperfectly Matched by Eric Benson
```

### Performance text (classify this)

```text
Suggested Roles: Actress – April (early 20s), Evil Counter Woman Actor – Zack (early 20s), Grandma, Game Show Host

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

APRIL: (Pg 21-28) Yeah, can I get a large, non-fat iced mocha with three shots? Thanks.

ZACK: (runs into APRIL as she is picking up her drink, spilling it all over her) Oh, crap. Oh, wow. I am so sorry. Jeez. (helping her to clean up without much success)

APRIL: Really, it's okay. Seriously. It's not a big deal.

ZACK: (sort of chuckling) Well, it could be worse. You could have gotten a hot mocha and right now you'd have steaming hot coffee and milk all over you.

APRIL: Yeah, that's hilarious, man. Real funny.

ZACK: Just imagine, second, maybe third-degree burns, all because some doofus. . .

APRIL: Doofus?

ZACK: Yeah, doofus, 'cause some doofus runs into you. I'm sorry, I'm Zack.

APRIL: Charmed, I'm sure . . . April.

ZACK: April, how about I make it up to you by taking you out for a drink on Friday?

APRIL: That's a very nice offer, Zack, but I --

ZACK: Don't drink, I'm sorry. Not coffee, how about a tea date? Iced, of course.

APRIL: No, I --

ZACK: Boyfriend? APRIL: No

ZACK: Husband? APRIL: No

ZACK: Hmm . . . nun? You don't look like a nun.

APRIL: I'm not a nun. I just don't typically go out on dates with clumsy . . . doofuses who spill my mocha all over me. Were you gonna offer me another one?

ZACK: Oh crap, I'm a doofus . . . Can I get another large

APRIL: Non-fat

ZACK: Mocha with three

APRIL: Freeze.

APRIL: (to audience) So, Zack over here turned out to be a real psycho. Unfortunately, I'd given him my number, and even more unfortunately he started calling me in the middle of the night

ZACK: Hello, April, what are you wearing?

APRIL: Ew. (slams down the phone) His favorite was the chicken calls.

ZACK: (Making loud chicken sounds) Hello, April, you make me want to lay an egg.

APRIL: Freak. (slams the phone down again; to audience) He ended up stalking me and showing up at my door in a giant chicken costume. He kidnapped me, took me to KFC and threatened to put me in the fry vat. Claimed it would consummate our love. I testified and he's doing twenty. I'll be in therapy for at least that long. (beat) I'm lying. Zack and I have been together for the last three years. But, he does do that chicken thing sometimes. I had to do the big "meet his family" dinner a couple of months after we started dating.

ZACK: You are totally going to love my family, especially my grandma. And, more importantly, they are going to adore you. Just like I do. (gives her a peck on the cheek)

APRIL: Well, if they're half as strange as you are, Clucker. (to audience) So, Zack's grandma, she, hmm . . . ***** Grandma Scene*****

GRANDMA: How do you like the meatloaf, dear?

APRIL: It's wonderful, thank you.

GRANDMA: You're an awfully skinny girl. You don't have an eating disorder, do you?

APRIL: No, no. . . just a high metabolism.

GRANDMA: Well, I just want the best for our little Pookie-Bottom.

APRIL: Well, yes, Pookie-Bottom is a special boy.

GRANDMA: I'll say he is. April, are you Catholic?

APRIL: Well, ma'am, actually our family is Jewish.

(GRANDMA has just taken a bite of scrumptious meatloaf and begins choking violently. She is wheezing and making all sorts of unpleasant noises. APRIL performs the Heimlich and the offending piece of meatloaf is successfully ejected.)

GRANDMA: Well, at least you don't look Jewish. Have you and Zack talked about remaining chaste before --

APRIL: Freeze. (to audience) You can't hold somebody's family against them. Even if their Grandmother does closely resemble Norman Bates' mother. ****** Present Day******

ZACK: April's family isn't . . . around. I just wanted her to feel like she had a family to be a part of. After all, she's changed my life

APRIL: Zack . . .

ZACK: Don't Zack me. I'm not ashamed to say that you've made me complete. You know that. You laugh at all my stupid jokes. You make sure my head is screwed on every morning . . . 'cause you know I'd forget it at home if you didn't. I never thought I'd meet the perfect girl. . . and then I spilled an Iced Mocha all over her.

APRIL: (to audience) Zack's an artist. He gave me a painting he'd done of me and then . . . took me to France for our first anniversary. If you looked up extravagant in the dictionary, the definition would include his mug shot. I got food poisoning from an evil cream puff and was sick for the last three days. Zack lost his wallet, my wallet, our plane tickets, our passports . . .

ZACK: That's about it.

APRIL: We were on some bargain airline where the evil counter woman didn't seem to speak English. It was an interesting experience. ****** Airport Scene******

ZACK: I lost our tickets, and we don't have our ID's. Our flight is today.

EVIL COUNTER WOMAN: Parlez vous Francais?

ZACK: We're trying to fly home.

EVIL COUNTER WOMAN: Parlez vous Francais?

ZACK: We need to go home. My girlfriend is sick.

EVIL COUNTER WOMAN: Parlez vous Francais?

ZACK: No, I don't speak French. We have a flight to Connecticut.

EVIL COUNTER WOMAN: I am not deaf, Monsieur. I am an evil counter woman. ****** Present Day******

APRIL: (to audience) We ended up spending 23 hours in the airport before we got on our flight.

ZACK: (to audience) That was a great trip.

APRIL: Basically, Zack and I are opposite in every way. I like to stay home.

ZACK: I like to go out.

APRIL: I like having everything organized. I'm kind of a neat freak.

ZACK: Why waste time putting clothes away when you're just going to wear them again?

APRIL: I like to talk things through.

ZACK: I morph into the chicken. (chicken sounds, beat) And so, we're living proof that opposites attract.

APRIL: Or, we're living proof that the less alike you are, the sooner the problems start to rear their ugly little heads.

ZACK: That's an exaggeration, April. C'mon, now . . .

APRIL: (to audience) Sometimes I'd fantasize that we were contestants on a game show called, "Who's the Crappiest Couple?" *****Game Show Scene*****

GAME SHOW HOST: How many times do you and your boyfriend fight per week?

APRIL: Six out of seven days?

GAME SHOW HOST: How do you typically handle disagreements?

APRIL: Well, I try to discuss things with

ZACK: She starts screaming at me

APRIL: I start trying to explain how I'm feeling and . . .

ZACK: Then I usually fall asleep.

GAME SHOW HOST: Another point for Crappy Couple #1! And, finally, when was the last time you . . .

ZACK: Oh, well. . . umm . . .

APRIL: I, uh, hmm . . .

GAME SHOW HOST: We have our winners! Please proceed to the podium to accept the Grand Prize! One full year of free relationship counseling!

APRIL: Freeze. ****** Present Day******

APRIL: (to audience) I actually suggested counseling and Zack, well --

ZACK: I don't want to talk about our problems with anyone

APRIL: Yeah, including me.

ZACK: That's not what I meant, April.

APRIL: It's what you said. (to audience) Things went down-hill from there. It seemed like we were seeing less and less of each other. We were both working or he was asleep when I got home. One night, I was sitting in the dark, at the kitchen table when he got home. *****Break Up Scene*****

ZACK: Why don't you have the lights on?

APRIL: Because I'm thinking.

ZACK: You can only think in the dark now? Are you crying, April?

APRIL: I thought you were coming home tonight. I thought we were going to eat dinner together.

ZACK: I'm sorry. Things got busy at the restaurant. I . . .

APRIL: You could have called. You never call

ZACK: And you always tell me I'm wrong. I just want to make you happy.

APRIL: But you don't. Freeze. (to audience) I asked him to take some of his stuff to his parents’ house that night. We, uh, broke up.

ZACK: (to audience) Separated.

APRIL: (to Zack) Yeah, Zack, separated, permanently. Zack, we can't be together anymore. We aren't good anymore together. I make you miserable, you don't even want to be around me. Zack. . . what are you doing?

ZACK: I'm searching for my heart, April. I've lost it. It's gone somewhere and I don't know how to find it. Do you understand that?

APRIL: I can't fix us.

ZACK: I never asked you to. I just wanted us to be happy. You were happy for a long time.

APRIL: I don't think I ever really was. I thought I could be, but I'm not.

ZACK: Let's just try again . . . please. I love you.

APRIL: I don't love you, Zack. I'm sorry.

ZACK: I don't believe you. I don't think you're this cold.

APRIL: No, if I was cold, I'd let you stay with me . . . pretend that I loved you when I don't. You deserve a lot more than that.

ZACK: I'll never love anyone again, April. Did I show you my new painting?

APRIL: That's a blank canvas, Zack.

ZACK: It's white like the plate after you ate my heart.

APRIL: If I could change this I would, Zack. I don't have a magic wand. I can't love you like that. I hope you can forgive me. I know you're strong enough. I need to go, Zack. Freeze. (to audience) I don't think we can control our hearts. Whether we're falling in love, or out of it. It's just that falling in is the best feeling in the world and falling out hurts. It's funny, but one little thing, one little choice or accident or joke can change our lives forever. *****Flashback Scene*****

APRIL: Yeah, can I get a large, non-fat iced mocha with three shots?

ZACK: Oh, crap. Oh, wow. I'm so sorry, Jeez.

APRIL: Really, it's okay, seriously. It's not a big deal.

ZACK: I'm such a doofus. Well, you have a nice day.

APRIL: Yeah, you too.

ZACK: Bye.

APRIL: Bye.
```

---

## IC-0813: In Your Hat

- Title: In Your Hat
- Author (byline): Ellen Conford
- Work: Shelf Life: Stories by the Book, Pgs 11-21
- Publisher: Simon and Schuster
- Publication date as stated: Aug 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DENNIS, ARIEL, MR. FRAZETTI
- Teaser before the introduction: Yes
- Spoken words (computed): 1311
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ellen Conford
Book: Shelf Life: Stories by the Book, Pgs 11-21
ISBN: 978-0689841804
Publisher: Simon and Schuster
Date (Month/Year): Aug 2003
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: High school is tough enough without being emotionally ambushed by a girl in a pink sweater wielding fake French literature like a weapon.

ACTRESS: This is a tale of love, lies, and literary hoaxes in which Dennis, a chronic underachiever and wannabe Romeo, finally gets noticed by the elusive Ariel Greenbanks.

ACTOR: Armed with nothing but panic, a dubious history of practical jokes, and a suspicious enthusiasm for hat-based tragedies, Dennis learns the hard way that you should never trust a girl who throws out ‘tuberculosis’ and ‘relevant’ in the same conversation.

ACTRESS: Madame de Maupassant by Emile Bovary may be fake news, but Dennis’s humiliation is very, very real.

TOGETHER: In Your Hat by Ellen Conford
```

### Performance text (classify this)

```text
Suggested Roles: ACTOR: Daniel ACTRESS: Ariel and MR. FRAZETTI

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

DENNIS: (Pg 11- 21) I was in the non-silent study area of the library on the last Sunday of midwinter break when Ariel Greenbanks noticed me. (Ariel enters and tosses her hair) I’d been trying to get Ariel to notice me for almost 2 years now, and the results had been grim to none. So, when she paused next to my chair, I seized the opportunity. (to Ariel) Hey, good lookin’. Come here often?

ARIEL: (picking up a couple of books from the table) As a matter of fact, yes. (looking at titles) Joseph Conrad? Jane Austen?

DENNIS: Well, uh . . . (to audience) I hesitated. She was seeing a side of me she’d never seen before, which wasn’t surprising, since I don’t have that side. She liked the Mensa type. But you can’t base a relationship on lies. I couldn’t pretend I was an intellectual giant. (to Ariel) Actually, I’m in kind of a crisis here. An emergency book report.

ARIEL: Oh. When is it due?

DENNIS: (sighing heavily) Tomorrow.

ARIEL: Tomorrow. That is an emergency. Well, which one of these did you read?

DENNIS: I haven’t exactly gotten to the reading stage yet. (to audience) I didn’t want to tell her that I had only gotten to the “which is the shortest book you can find?” stage. (shocked and elated) [But] Ariel Greenbanks, wearing a cute pink sweater, was talking to me! She slid into the chair next to mine and scooped some of the books toward her. She wanted to help me!

ARIEL: All of these are pretty short.

DENNIS: Short was the first requirement – and big print! (disapproving look from Ariel) I mean, because of the crisis. . . It’s not like I don’t like to read.

ARIEL: Maybe you could write about something you’ve already read. What was the last book you liked?

DENNIS: The Sponge People of Cyberia – [but] Mr. Frazetti has this prejudice against science fiction . . .

ARIEL: Have you read anything that isn’t science fiction?

DENNIS: The Microbe Hunters. But I can’t use that one. (to audience) After 4 years of handing in the same book report I’d written in 7th grade, the book report cops had finally caught up with me. Frankly, I don’t think teachers ought to trade information about their students. Isn’t that like a breach of doctor-patient confidentiality? (to Ariel, desperately) What am I going to do?

ARIEL: (smiling sympathetically) You’d better come to my house.

DENNIS: Her house! Alone with Ariel. With her! She and I. Her and me? Whatever. ***Scene change****

ARIEL: (scanning her bookcase) Darn it. I can’t find it. It was perfect. Short, but a minor classic. Mr. Frazetti would have been impressed. It was so great! About the millinery industry in France and this poor little woman who had all her hat designs stolen by an evil corporation. So vivid, so alive! I mean you could feel the hunger and the cold gnawing at you. (deep inhale) You could smell the slop in the Paris streets.

DENNIS: (inhales, with a cough, matching her excitement) I know what you mean!

ARIEL: And it’s so relevant. Even now. You could compare it to how today’s giant corporations swallow ups the little guy. C’est la vie.

DENNIS: (parroting) La vie (to audiene) A brief scowl flash[ed] across her brow. I hoped she hadn’t suddenly remembered the 26 pizzas I’d had delivered to her.

ARIEL: I really shouldn’t do this . . .

DENNIS: (eagerly) What shouldn’t you do? And will you do it??

ARIEL: I could tell you about the book . . .

DENNIS: (to audience) Had she finally realized we were destined to be together. Had she seen beyond the jokes and discovered the tormented soul beneath? The Me who could only express his love behind a mask of comedy?

ARIEL: (flirtatiously) Can you stay awhile? This will take some time . . .

DENNIS: (to audience) I went home with 5 pages of notes and headed for my computer. It wasn’t easy to concentrate with visions of Ariel dancing in my head. Her soft, pink sweater . . . [No!] I was supposed to be thinking of French hats and imagining the crude, clashing noises of the Parisian slums. It really was a good story. This poor French girl marries a real loser who gets drunk a lot and beats her, and finally dies when he gets run over by a thresher in the potato fields where he’s been trying to eke out a living by growing (of course) potatoes!

ARIEL: (takes over the story telling) She goes to Paris to support herself by making hats. It turns out she’s really talented!

DENNIS: Things are looking up for Madam de Maupassant.

ARIEL: Until she meets this high-class society guy. (named Guy, as a matter of fact) Only, he’s down on his luck too and really needs money to pay of his gambling debts.

DENNIS: But Madam de Maupassant doesn’t know any of that! She falls madly in love with him and he asks her to marry him.

ARIEL: But . . . on the day they’re supposed to be married. He disappears, taking all her original hat designs with him.

DENNIS: He sells her designs to (checks his notes) Le Chic Chapeau, a big hat company and runs off to Algeria and is never heard from again.

ARIEL: (dramatically) Madame de Maupassant is heartbroken, gets tuberculosis, and wastes away – a pitiful shadow of her former self.

DENNIS: She doesn’t even have money for a bowl of soup, let alone medicine. Finally, just as she takes her dying breath, there’s a knock at the door. One of her old customers wants her to design all the hats for her daughter’s wedding.

ARIEL: (dramatically) But it’s too late. [She] can barely whisper . . “Entrez” when she gasps (gasps) and dies.

DENNIS: I’m telling you it was a terrific story! I was sniffling a little as I wrote out the plot. (proudly) AND I made a comparison between Madame de Maupassant and the economics of today. How the book was still relevant even though it was written 120 years ago. I printed out my report and was asleep before midnight . . . to dream of Ariel, in pink, trying on hats. Big flowery, poufy, old-fashioned hats!

ARIEL: (with a French accent) But of course I care what you think, Dennis. I want to look pretty for you.

DENNIS: On Monday I handed in my book report and spent the next two days trying to thank Ariel. I wanted to buy her lunch on Tuesday.

ARIEL: (disdainfully, motioning to her tray) I have lunch already.

DENNIS: On Wednesday I asked if she’d go to the library with me. I had an urge to read Madame de Maupassant. Ariel had made it sound so good. Plus, in case Mr. Frazetti asked me any questions about it I’d be ready for him.

ARIEL: (shaking her head) Band practice . . . (flounces off)

DENNIS: On Thursday Mr. Frazetti handed our book reports back. I sat straight and proud at my desk, waiting for my A, picturing the kiss Ariel would give me when I showed her my report. (puckers up at the thought) Usually I was in no hurry to get my assignments back. But today was different!

MR. FRAZETTI: (thrusting the report toward Dennis) Really, Mr. Murphy.

DENNIS: (looking down at his paper) Madam de Maupassant by Emile Bovary . . . F!! Underneath he’d written . . .

MR. FRAZETTI: (indignant) F as in FAKE!! Do you think I’m an idiot??

DENNIS: I couldn’t have been more stunned if I’d been captured by the Sponge People of Cyberia. How could he possibly know that I hadn’t really read the book? How could he know that Ariel had told me the story? Did she get the plot wrong? (leafing through the paper to the last page) At the bottom Mr. Frazetti had written . . .

MR. FRAZETTI: There will be no Makeup for this assignment. You have made up enough already!

DENNIS: (covering his eyes, dramatically) Despair and confusion overwhelmed me. Just as Le Chic Chapeau had overwhelmed Madame de Maupassant. (dramatic pause) I cornered Ariel near the parking lot exit. She was with two other girls who started giggling the moment they saw me. (to Ariel, pulling out his report) Look at this! Look at this!

ARIEL: (innocently) Oh, my. An F. That’s not good.

DENNIS: (livid) Not good? It’s terrible! Why did I get an F?

ARIEL: Well, maybe because I made it up.

DENNIS: Made it up? Made what up? What are you talking about?!

ARIEL: (with a sweet devious smile) The thing is, there really is no such book as Madame de Maupassant. I made it up. The whole story.

DENNIS: (stammering) No such book? But – but – (wailing) but why????

ARIEL: (laughing) It was a joke, Dennis. Just a little joke. (turns to leave)

DENNIS: It’s not funny! Ariel!!!!

ARIEL: (turns and tilts her head) You don’t think so?

DENNIS: (shouting) No! You really got me in trouble!

ARIEL: (hands on her hips, shaking her head) For heaven’s sake, Dennis. (with a French accent) What’s happened to your sense of humor? (exits)

DENNIS: (yelling to Ariel’s back) My great sense of humor AND my legendary reputation for practical jokes! You can’t base a relationship on lies!

ARIEL: C’est la vie!
```

---

## IC-0814: India Pale Ale

- Title: India Pale Ale
- Author (byline): Jaclyn Backhaus
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: 2018
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS, ACTOR 2, BOZ, NARRATOR, DEEPA, IGGY, SUNNY, TIM, VISHAL, NEWS REPORTER
- Teaser before the introduction: Yes
- Spoken words (computed): 1197
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jaclyn Backhaus
ISBN: 978-0822240136
Publisher: Dramatists Play Service
Date (Month/Year): 2018
```

### Introduction (context only: never use it for content warnings)

```text
AS NEWS REPORTER 1: We’re visiting The Sikh Temple of Wisconsin in Oak Creek, where [insert number] years ago, a white supremacist opened fire, killing six worshipers and wounding four others.

AS NEWS REPORTER 2: The attack was declared a hate crime and a terrorist act by the U.S. Department of Justice. The shooting sparked outrage and grief within the Sikh community and led to increased awareness of hate crimes against Sikhs and other minority groups.

AS NEWS REPORTER 1: This community knows how easily fear of immigrants can turn into violence against immigrants, but they refuse to barricade themselves and hide. So, this Sunday, just past the security cameras and the hired guard at the door, anyone is invited to sit and eat for free.

AS NEWS REPORTER 2: This tradition of langar is a cornerstone of Sikh community life. All are still welcome here.

ACTOR 1: Meet the Batras, a Punjabi-Sikh family navigating tradition and modernity. As Boz Batra moves away and Iggy, her younger brother prepares for his wedding – this violent hate crime forces the entire family to confront their past and the uncertainty of their future.

TOGETHER: India Pale Ale by Jaclyn Backhaus
```

### Performance text (classify this)

```text
Suggested Roles:

ACTRESS: Boz, Deepa

ACTOR 2: Narrator, Iggy, Sunny, Tim, Vishal, News Reporter

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

BOZ: (Pgs 9-12) (digging with a small shovel and talking like a pirate) It is oi, yer daughter Boz. I’ve come to share some news. I’m leavin to traverse the seven seas to head west to Wisconsin!

NARRATOR: Meet Boz, she’s 29. She’s a pirate, or at least she talks like one (chuckles)

BOZ: Oi want to open me own bar. Oi embark as Brownbeard, our natty ancestor, did afore me. Mannin the mutiny of that East India Company vessel 200 years ago.

NARRATOR: She digs a hole in the woodsy Wisconsin backyard of her parents’ home – her home still because she is a Good Indian Daughter.

BOZ: (puts her hand up, imagining protest) No no, hush now mum, hush now dad. Don’t afear. My bravery and your love will carry me safely . . . and this . . . a lost item of treasure. (she spots a glint of white in the soil) YEE-AOHHH – Jol’s marble elephant (reaches down and lifts it up) Oim takin Jol with me . . . yaar!

A langar hall – like a cafeteria, but a little sparser.

DEEPA: (Pg 19) (preparing food for the community with Boz and other family members; she speaks her mind to the audience) Boz should be able to do whatever she wants! She’s been saving money; it’s her money. She opens a bar in a college town, she’ll do well. She’s almost 30. She should do what she wants to do.

IGGY: (Pg 23-25) (off stage) Ey boi, engagement day! BOI BOI BOI

DEEPA: (to audience) Ohhhh Iggy! He is crazy in love!

IGGY: (as he enters; Indian boi street style, super amped on life) My girls! So the plan is langar her, then we all go back to the Lovi’s house; do the engagement party tradition thing, then later me and boys are goin out – bachelor party stuff.

DEEPA: Who is driving?

IGGY: Mamma, we take ubers! – Got to get you on that APP LIFE. Bozzy! You on that app life? You on Tinder, Bozzzyyy? Tell mama what Tinder is.

BOZ: Mamma, I’m not on Tinder. Oh my god, Iggy!

IGGY: Sorry, Boz . . . You like swipe to meet hot peeps and swipe to like reject peeps. Peeps do it when they are single and bored.

BOZ: (Pg 26-27) (with a touch of pirate) Look, oi don’t need a man to be happy! (SUNNY enters)

IGGY: Bozzy is a 21st century feminist like Beyonce, Malala, Fiona Apple.

SUNNY: (hugs BOZ) I wouldn’t have it any other way, daughter-mine. Yaar! Today we celebrate! (claps his hands and begins to dance a traditional Punjab folk dance of celebration* with Boz, they hum, sing, clap)

BOZ: (Pg 36) (Boz stops dancing, catches her breath) Dad, I’m not coming to the party tonight. I gotta go. (deep breath, pirate affectation creeps in) (Pg 38) Oim leaving. Oim moving to Madison to open a bar.

SUNNY: Basminder. You’re not serious. You’re going to walk out on your brother’s engagement day? Leave your family? Why?

BOZ: Dad, my future isn’t like up for your review. I’m 30 years old. I’ve been ready to leave for a long time.

SUNNY: (Pg 39) Basminder. We Batras. We don’t leave it’s not what we do.

BOZ: Brownbeard left. Jol left.

SUNNY: Don’t talk about Jol!

BOZ: (to audience) (Pg 41) When Jol, my brother, crossed the sea my family was proud of him. (Pg 54) I was 14. It was like this freak accident; he was there as a tourist. (Pg 41) When he did not come back, we buried his memory under layers of dirt. (Pg 39) (to father) Jol’s coming with me. (pulls the marble elephant from her pocket) I dug him out of the back yard.

SUNNY: But we buried it for a reason . . . as a family.

BOZ: (to Sunny) It was supposed to stay underground, I know. And I’m supposed to stay here but . . . (pause as she calls on the spirit with pirate accent) (Pg 41) Brownbeard, oi call on you, on your bravery. Armed with my trusty talisman (holds up elephant) and my pirate sneer, ahead of me – a world oive never witnessed but in dreams! (scene shifts-- Boz is behind the bar, serving a customer, TIM, a country boy of limited education)

NARRATOR: (Pg 42) Now a year has passed. The bar is real and it is hers . . .

TIM: (Pg 46-53) So how long have you been here?

BOZ: Opened doors here just a couple of weeks ago.

TIM: Yeah, but I mean like how long have you been here.

BOZ: Oh, I moved to Madison last year. I was born in Raymond.

TIM: No way – you seem like you’re from somewhere else.

BOZ: (staying cordial) Born and raised in Wisconsin.

TIM: So, like, your family . . . what are they? Where are they from?

BOZ: (somewhat colder) They were also born in Wisconsin. I’m 2nd generation American.

TIM: (won’t leave it alone) And ethnically, like, what’s your heritage?

BOZ: (with a sigh, but trying to educate) We’re Indian. Religiously? Sikh from the Punjab province of India.

TIM: It’s crazy how illegals, legals, you know, however you get here. It’s like it’s the country to be in, you know? I had this cousin, he met some Indians once and asked them where they were from and he was like “Dots or Feathers?” (explaining) Native American Indians and then like Indians from India. (BOZ stares at him in disbelief) Yeah, I though it was pretty offensive.

BOZ: Yeah.

TIM: (trying to recover - awkwardly) A lot of Indians becoming doctors . . . pretty big melting pot. The entire country, you know, it’s like Hispanics, Black, Asians, you name it. White . . . You name it. Pretty diverse.

BOZ: I mean, I’m used to it because you know, I was born here. (changing the subject) One of my ancestors was a pirate. They called him Brownbeard.

TIM: No s***!

BOZ: He sailed on one of the beer ships between India and the UK. The East India Company were all basically pirates, but the main duty of the ship was to transport beer. That’s where IPA comes from – India Pale Ale.

TIM: Oh, wow. India Pale Ale – India is the “I”

BOZ: The journey was so long they had to add extra hops.

TIM: I love IPA’s because of their hops.

BOZ: Yeah, that’s like what IPAs are.

TIM: I feel a little stupid askin you all about where you’re from; thinking it’s some exotic answer.

BOZ: I get that all the time. Like when you said “what are you” – the phrasing implies that I am not human. I am an object.

TIM: I didn’t mean. . .

BOZ: I’m not implying you said that intentionally, but it’s just . . . problematic. I’ve dealt with people who actually meant it in a hateful way.

TIM: Wow. . . I know a lot a guys who might probably do that stuff.

BOZ: Well, as long as they’re not creepy, bring em on by. We can have a nice little . . .

TIM: (interrupting) Teachable moment?

BOZ: My life is a series of teachable moments. . .

VISHAL: (Pg 55) (bursts into the bar, frantic) Boz! You gotta come home! Your brother told me to find you.

BOZ: Why didn’t he come find me himself?

VISHAL: Because he’s with your dad in the hospital. There was an accident at the gurdwara.** You have to come with me. (breaking down) (Pg 56) A bunch of people were shot at services. My dad got hit in the leg; he’s gonna be okay. But your dad. . . We have to go NOW. (they exit in a rush – long pause, then Boz takes the stage alone)

BOZ: (Pg 67-68) (to audience, with great sadness) A lone man, a white man, a man full of hate. A Saturday at lunchtime; services finish, langar beginning. Three assault rifles. Shot himself when he heard sirens, but not before he shot nine Sikh neighbors. . . my father too.

NEWS REPORTER: [transition not in playscript] The attack was declared a hate crime and a terrorist act by the U.S. Department of Justice.

BOZ: (Pg 81) I’m not going back [to the bar]. Ma needs me. She’s all alone in that house now. (long beat) It takes a long time for us to say anything about anything . . .

NEWS REPORTER: [transition not in playscript] This community knows how easily fear of immigrants can turn into violence against immigrants, but they refuse to barricade themselves and hide.

DEEPA: (Pg 80) (with much emotion) We spend our time forgetting our stories, forgetting language . . . forgetting so they will call us American. And for what? I was born in this country. I’m as American as a deep fried apple pie. [But] it’s easier to forget than to fear being killed. (beat) (Pg 94) It is a distinctly American tradition to let fear forge chasms. But we are you and you are us. What has to change in our society to allow you to love someone whose culture differs from yours -- who shares your patch of land, your earth? What has to change? . . . . What has to change?
```

---

## IC-0815: Indoor/Outdoor

- Title: Indoor/Outdoor
- Author (byline): Kenny Finkle
- Work: Not specified
- Publisher: Broadway Play Publishing
- Publication date as stated: 2006
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SAMANTHA, SHUMAN, MOUSE, OSCAR
- Teaser before the introduction: Yes
- Spoken words (computed): 1825
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kenny Finkle
ISBN: 978-0881453300
Publisher: Broadway Play Publishing
Date (Month/Year): 2006
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: As is true with most cats, Samantha didn’t have an easy childhood.

ACTRESS: She was ripped away from her mother as soon as she was old enough to eat real food and dropped at the animal shelter. (Thunder clap and or ominous music)

ACTOR: Don’t they kill cats at the Animal Shelter. (Thunder clap and or ominous music)

ACTRESS: You get five days. Five days to find your “forever home”. And then . . . . Well, let’s not think about that.

ACTOR: How in the world do you do that when you are 1 of a gazillion stray cats?

TOGETHER: Indoor/Outdoor by Kenny Finkle
```

### Performance text (classify this)

```text
NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

SAMANTHA: (Pg 1) (Lights up on SAMANTHA by herself) (To audience) Hi. My name's Samantha (Just then SHUMAN appears on stage, looking for SAMANTHA.)

SHUMAN: Samantha? SAMANTHA?? (He wanders off.)

SAMANTHA: That's Shuman. I live with him. He's looking for me right now. We'll get to him in a minute. First though, you need to know me. I suppose this is as good a time as any to tell you . . . I'm a cat.

SAMANTHA: (Pg 4) (To audience) The Animal Shelter was totally horrible. Think Amistad meets Schindler's List. I wanted to find true love. But I didn't know how to go about it. How do you find your true love? Especially in an animal shelter where you only have five days to do it. (Pg 6-8) And it was at that exact moment that Shuman fell into my life. (SHUMAN enters.) From across the crowded shelter our eyes met. (He sees SAMANTHA. They look at each other.) BAM! A connection! It knocked us both off our feet! (They both fall backwards.) Then, he got up, walked to my cage, and a second later I was in his arms. He was so warm and strong. And then he put his hand under my chin and started scratching and I, for the first time in my life, started to purr.

SHUMAN: You're purring. Are you happy?

SAMANTHA: Yes very. (To audience) And if I didn't know then that he was my true love. What he said next sealed the deal.

SHUMAN: Hi. I guess you're coming home with me. You're beautiful. Your name is . . .

(He looks deeply into her eyes) Samantha.

SAMANTHA: (To audience) Shuman named me.

SHUMAN: You don't have to be scared anymore, I'll love you like you are supposed to be loved until the day I die.

SAMANTHA: (To audience) And Shuman took me to his home. And became my true love. And it was everything I dreamed it would be. For a while at least . . . (Pg 10-13) Before we go any further, I think that this may be a good time to tell you more [about] Shuman, the man. (We are now in SHUMAN's office; he is working at his computer) Shuman works from home, doing web design. In case you didn't notice, Shuman is very sensitive and cries over almost anything.

SHUMAN: Save. Save! SAVE! SAVE!!!! Why won't you save? I, I, I, I- (He starts crying hysterically).

SAMANTHA: Every morning Shuman gets up and talks to himself in the mirror.

SHUMAN: I am worthy of success. I am worthy of love. I am worthy of hope. I am worthy of dreams. I am worthy of Samantha. I am worthy of this day. Good morning.

SAMANTHA: (To audience) One of Shuman's favorite things to do is put on music really loud and sing and dance to it. Sometimes he even lets me dance with him.

SHUMAN: Everybody dance! (SHUMAN scoops up SAMANTHA and sings and dances to Madness' song Our House.) Our house in the middle of our street. Our house in the middle of our ... Our house ... (To Samantha) Oh Sammy! You are the greatest thing that's ever happened to me!

SAMANTHA: (To audience) And it was at this exact moment that I noticed Shuman had a crumb of food on his upper lip. Shuman noticed me staring at him and he said-

SHUMAN: You're trying to look into my soul aren't you?

SAMANTHA: No . . . I'm not. You have a crumb on your lip and its driving me crazy! (To audience) And for the first time I realized that maybe Shuman didn't always understand me. Just as clarification, I think I should say I speak in Cat. This is what I really sound like. Meow wowo, memeo, meowwww. So I suppose it shouldn't be all that surprising but still, sometimes he'd be so far off the mark it'd be shocking! (Pg 23-24) [Case in point . . . ] one night, I heard a rustling in the kitchen and I had to see what it was. I ran into the kitchen and found a mouse rifling through the cabinets. (A MOUSE appears)

MOUSE: Oh sh**, a cat.

SAMANTHA: (To audience) No one had ever told me about mice before, but somehow I instinctively knew that mice were evil and that I was to rid the house of them. So that's what I attempted to do. All night long. (SAMANTHA chases the MOUSE) Finally, I got the mouse under my paw.

MOUSE: Ow.

SAMANTHA: Shut up. (To audience) And I started toying with it. Like so. (To MOUSE) Should I let you go?

MOUSE: Yes, please, I didn't mean to be here anyway, I must have taken a wrong tum in Albuquerque-

SAMANTHA: (To audience) For those of you that are weak of heart, I'll refrain from illustrating the rest of what happened. For those of you that aren't weak of heart, think Texas Chainsaw Massacre meets Nightmare on Elm Street! However, suffice it to say, eventually I killed it. . . Killing. Chasing. Using my instincts like that. It came so naturally. And it felt so good! I felt like a wild tigress! And I never wanted to feel any different! The whole next day I carried the mouse around in my mouth. I started to walk with more confidence.

(Confident SAMANTHA shows us her more confident walk. Shuman notices she has a mouse in her mouth and tries to take it from her)

SHUMAN: (Pg 25-29) Oh, Sammy, let go. Ew. Oh my god. Ew. Ew. Ew. This is so . . . disgusting.The mouse has to be thrown away.

SAMANTHA: No! The mouse is mine. I killed it. You can't just throw it away. Its mine! MINE! (SHUMAN picks SAMANTHA up. She flails.) No! SHUMAN GET OFF ME! THE MOUSE IS MINE! GIVE ME BACK MY MOUSE! (To audience) But he didn't listen to me and he threw the mouse away. After that I snuck out of bed every night and roamed the house looking for danger or excitement or both. And then one night, while stalking through the kitchen, the very thing I'd been looking for found me. And his name was Oscar the cat. (OSCAR the Cat appears. He is one cool cat.) I first spotted him through the sliding glass door. I was frozen to the spot. I couldn't move. I couldn't breathe.

OSCAR: Hey ... sup sweetheart? I'm Oscar. I'm an alley cat. Moved up here from the city a few years back. You're cool. Do you like living inside? I've never done it. Can't imagine what it’s like. Outside is the only place I've ever lived. Born and bred. If you ever got out here, I'd show you all these cool places. Like there's a little garden just down the road. In the afternoon I lay out there and get sun. Have you ever felt sun on your coat? It's heaven.

SAMANTHA: (To audience) And I started to wonder why hadn't Shuman ever taken me outside? Why was I an indoor cat?

OSCAR: You know where I wish I could take you? The beach. Do you know its only sand and water? Just water and sand. It's like a giant litter box. And sand, oh man, sand is supposed to feel like heaven underneath your paws. Sure during the day people are around but at night, it'd be ours.

SAMANTHA: (To audience) Ours. He said ours. I'd never thought of there being another "ours" besides me and Shuman and then there was Oscar saying "ours" and I couldn't help but think that it sounded right. Like I was really supposed to be with Oscar outside and not with Shuman inside. But I loved Shuman. Or maybe I didn't. I didn't know anymore.

SAMANTHA: (awkwardly flirting) (Pg 34-39) My name's Samantha . . . I killed a mouse once.

OSCAR: Samantha. Sa-man-tha. I like that. You're a beast! You're a goddess! You're a tigress! You're-you're so unbelievable! (Suddenly SHUMAN enters the kitchen and flips on a light.)

SHUMAN: Samantha? Who's this? What's going on? Where'd she come from? You two friends? That's so sweet. Come on, let's go to bed

SAMANTHA: No. I'm not going to bed with you Shuman. I want to stay here. I want to stay with Oscar!

SHUMAN: You want me to pick you up? (SHUMAN picks SAMANTHA up in his arms.)

SAMANTHA: (To audience) And I was so angry at him for picking me up and disturbing me and Oscar that I-well I did something I'd never done before. (SAMANTHA bites SHUMAN' s arm.)

SHUMAN: OW!!!! GOD DAMN IT!!!!!! OW!!!!! (SAMANTH, hissing, jumps out of SHUMAN's arms.) I can't believe you bit me! Bad girl! Bad BAD GIRL! You will not be allowed in bed tonight! You can stay out here and think about what you did! (SHUMAN exits. SAMANTHA turns to OSCAR.)

SAMANTHA: So, where were we?

OSCAR: Look, save your breath. I'm an alley cat, 0K? I know how this goes. So I'm just gonna back away now. Real slow. And then it'll be like I wasn't ever here and it'll all be cool. (He starts to leave.)

SAMANTHA: No! Oscar! I want to bust out of here. I'm going to figure something out. I promise. (To audience). Maybe if I started to act wild around the house, Shuman would get the idea and let me out. So I started doing these really complex and bizarre running patterns all around the living room.

(SAMANTHA does a bizarre running pattern. SHUMAN follows, talking as he runs.)

SHUMAN: Sammy? Sammy! Stop! Hey!

SAMANTHA: I then proceeded to destroy everything I possibly could. (As she continues to run, SAMANTHA starts knocking off plants, books, anything in her way. SHUMAN attempts to pick up the pieces behind her.)

SHUMAN: Stop it Sammy! No! That’s expensive! Whay are you doing this? OK. OK. You win. Just go ahead. I need to sit. I need to sit and . . . breathe. (He sits and breathes to calm himself – he may even be crying a little)

SAMANTHA: [But] I knew I had to take things further if I wanted Shuman to kick me out. Finally one morning while in my litter box, it hit me. If you catch my drift... I decided that the best place to do it would be on his computer. After all he spent so much time there and if I really did it right, he would possibly have to get a whole new computer. Soon enough, Shuman discovered it. (SHUMAN enters and sees the computer.)

SHUMAN: No. Ew. SAMMY!!!!!???

SAMANTHA: (To audience) I went right up to him and stared at him with a look of defiance. (SHUMAN picks up SAMMY roughly by the scruff of the neck)

SHUMAN: I've had it with you. Do you hear me? You've destroyed everything in this house! I'm throwing you out. Out into the forest so you can get attacked and killed and eaten by wild animals. (He sets her down to open the door) So, goodbye! And don't come back asking for food. Because I'm not giving you any. (He starts to open the door)

SAMANTHA: (To audience) [I was] so close. And then . . .

SHUMAN: (Stops, takes a breath to calm himself and turns to audience) (Pg 45) She’s a cat! She’s supposed to be simple. That’s why I got a cat! I wanted simple. I’m good at simple. I’m not good at the other stuff. (sadly to SAMANTHA) (Pg 49) No matter what I do you’re not happy.

SAMANTHA: (Still angry) You never listen to me.

SHUMAN: (Pg 51-53) [But] I feel like I know you. (all of a sudden, Shuman can actually hear what Samantha is saying, and a look of amazement passes over his face)

SAMANTHA: If you did, you wouldn’t have thrown my mouse away.

SHUMAN: Your mouse?

SAMANTHA: Yes my mouse! I killed that!

SHUMAN: I know you killed it. It was going to start smelling so I threw it away. It was dead!

SAMANTHA: I loved that I killed that mouse and if you knew me at all you would have known that. (to audience) He thinks I’m simple! (yelling at SHERMAN) I’m not simple! I’m complicated. (Shuman starts to cry, but SAMANTHA is resolute) Your crying isn’t real. You’re a fake. You have no backbone. You are a miserable lonely person. Let me leave!

SHUMAN: (Pg 60-61) (SHERMAN opens the door slowly) Samantha, if you want to go. . Go. I can’t keep you. I don’t want to fight anymore. (Samantha and Shuman stare at each other.) I just wish I were enough for you. But if I can’t be, then I can’t. (Samantha begins to leave, but then hesitates)

SAMANTHA: (pg 68-69) (to audience) And I realized in that moment that by letting me outside, Shuman had told me that he loved me unconditionally. And I knew then that this was my home. (Meows loudly) And I looked Shuman right in the eyes and I said: Sometimes you won’t get me and sometimes I won’t get you, but I’ll love you. And for a second I wasn’t sure if he understood, but I was home. And it was enough. (Pg 71) And soon after that Shuman installed a new front door that had a flap in it, so I could come and go as I please. (She goes through the door) Yeah, I’m outside! (She goes back though the door) Yeah, I’m inside! . . . . (Pg 76) Maybe life is just this. Just this. This brief moment we have together where we’re inside each other and outside ourselves and we can all just let go.

SHUMAN: Oh, Samantha. I love you.

SAMANTHA: Meow!
```

---

## IC-0816: Into the Woods

- Title: Into the Woods
- Author (byline): Stephen Sondheim and James Lapine
- Work: Not specified
- Publisher: Theatre Communications Group
- Publication date as stated: June 1989
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, BAKER, WITCH, WIFE, ACTOR, JACK, LITTLE RED, WITCH’S VOICE, CINDERELLA, RAPUNZEL
- Teaser before the introduction: Yes
- Spoken words (computed): 1103
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephen Sondheim and James Lapine
ISBN: 978-0930452933
Publisher: Theatre Communications Group
Date (Month/Year): June 1989
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Our story begins in a kingdom where fairy tales don’t just happen.

ACTOR: They get a little tangled, slightly ridiculous, and occasionally burst into rap at the worst possible moments.

ACTRESS: Welcome to a world where cows are suspiciously important, and happily-ever-afters come with a long list of conditions.

ACTOR: In this enchanted forest, wishes don’t come true easily -- and if they do, there’s usually a catch or a curse!

ACTRESS: Are you brave enough to go . . .

TOGETHER: Into the Woods by Stephen Sondheim and James Lapine
```

### Performance text (classify this)

```text
Suggested Roles: Actor: Baker, Witch, Cinderella, Rapunzel

Actress: Narrator, Wife, Jack, Little Red

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NARRATOR: (Pg 3-4) Once upon a time in a far-off kingdom lived a childless baker with his wife. (Pg 12-14) The baker had lost his mother and father in a baking accident – well, at least that is what he believed. He was eager to have a family of his own and concerned that all efforts until now had failed. (a knock on the baker’s door)

BAKER: Who might that be? (looks off to see) It’s the witch from next door! (opens the door) We have no bread.

WITCH: Of course you have no bread! (Wife reacts)

BAKER: What do you wish?

WITCH: It’s not what I wish. It’s what you wish. (points to wife’s belly) Nothing cooking in there now, is there? (Wife reacts by clutching her stomach)

NARRATOR: The enchantress went on to tell the couple she had placed a spell on their house.

WITCH: In the past, when you were no more than a babe, your father brought his young wife and you to this cottage. They were a handsome couple, but NOT handsome neighbors. My beautiful garden! How was I to know what your father had hid in his pocket? My mother had warned me I would be punished if I ever were to lose any of the beans.

WIFE: Beans?

WITCH: The special beans! I let him go / I didn’t know / he’d stolen my beans! (getting worked up – she raps) Then Bang! Crash! And the lightning flash! / And I laid a little spell on them. (Rap stops) You too, son – that your family tree would always be a barren one. (wife gasps; Witch begins to rap again) So there’s no more fuss/ And there’s no more scenes / And my garden thrives - / You should see my nectarines! / But I’m telling you the same / I tell Kings and Queens / Don’t ever never ever / Mess around with my greens! / Especially the beans.

ACTOR: (whispers) A great adventure is about to begin.

WITCH: (Pg 16) You wish to have the curse reversed? I’ll need a certain potion first. Go to the wood and bring me back . . . One: the cow as white as milk, Two: the cape as red as blood, Three: the hair as yellow as corn, Four: the slipper as pure as gold. Bring me these before the chime of midnight in three days’ time, and you shall have, I guarantee, a child as perfect as child can be. Go to the wood! (the witch disappears in a puff of smoke) (The Baker and his wife prepare to leave for the wood. As the Baker dons his father’s old coat, he finds something in the pocket)

BAKER: (Pg 17) Look what I found in Father’s hunting jacket. (holds out his hand)

WIFE: (Looking at his hand) Six beans BAKER: I wonder if they are the–

WIFE: Witches beans? We’ll take them with us! BAKER: No! You are not coming.

(Baker exits, leaving his wife at home)

NARRATOR: (Pg 18) And so the baker, reluctantly, set off to meet the enchantress’s demands.

BAKER: (Pg 27-29) This is ridiculous. I’ll never get that red cape, nor find a golden cow, or a yellow slipper – or was it a golden slipper and a yellow cow? (Wife sneaks up behind him and taps him on the shoulder; he jumps in fear) Oh, no . . . .

WIFE: The cow as white as milk, the cape as red as blood, the hair as yellow as corn, the slipper

BAKER: (cutting her off at any point) What are you doing here?

WIFE: (tries to put a scarf around his neck) You forgot your scarf –

BAKER: (taking the scarf off) You have no business being alone in the woods. Now go home!

WIFE: I wish to help!

BAKER: No! The spell is on my house. WIFE: Our house

BAKER: Only I can lift the spell

WIFE: We must life the spell together. (noticing a young boy with a white cow) A cow as white as . . . Milk!

BAKER: Hello there, young man. What might you be doing with a cow in the middle of the forest?

JACK: (nervous) I was heading toward market [to] sell my cow, sir. No less than five pounds. But I seem to have lost my way.

BAKER: Five pounds! Where am I to get five pounds? (Searches his pockets)

WIFE: And if you can’t fetch that sum? Then what are you to do?

JACK: I hadn’t thought of that . . . I suppose my mother and I will have no food to eat.

BAKER:(holding out his hand to his wife with a few coins and the beans) This is the sum total . . .

WIFE: (loudly) Beans – we musn’t give up our beans!

JACK: Beans in exchange for my cow?

WIFE: Oh, these are no ordinary beans, son. These beans carry magic.

JACK: (excited) Magic? What king of magic? WIFE: (to Baker) Tell him.

BAKER: (nervously) Magic that defies description . . . JACK: How many beans?

BAKER: Six.

WIFE: Five! We can’t part with all of them. (takes one of the beans and puts it in her pocket) Besides, I’d say they’re worth a pound each, at the very least.

BAKER: (hands Jack the beans as wife takes the cow’s lead) Good luck there, young lad. (to Wife) (Pg 31) Take the cow and go home. I will carry this out in my own fashion. (Baker and Wife exit in separate directions) ******* (Another part of the woods) *******

BAKER: (Pg 31-32) (steps into Little Red Riding Hood’s path) Hello there, little one.(aside)[The cape as red as blood] (to Little Red) Where did you get that beautiful cape?

LITTLE RED: My granny made it for me.

BAKER: I would love a red cloak like that.

LITTLE RED: (giggling) You’d look pretty foolish.

BAKER: (grabbing the cape) May I take a look at it?

LITTLE RED: (in a panic) I don’t like to be without my cape. Please give it back! Please!

WITCH’S VOICE: Forget the little girl and get the cape! (Baker tucks the cape under his arm and dashes away)

LITTLE RED: (stands numb for a moment then lets out a bloodcurdling scream) ******* (Another part of the woods) *******

(Cinderella dashes onstage, looking over her shoulder)

WIFE: (Pg 37) Are you all right, miss?

CINDERELLA: (breathless) Yes. I just need to catch my breath.

WIFE: What a beautiful gown! (focusing on her shoes, not the gown) (aside) (Pg 27) The slipper as pure as . . . (Pg 37) (to Cinderella) Were you at the King’s Festival?

CINDERELLA: (preoccupied with the people who are chasing her) Yes. . . What brings you here (notices the cow) and with a cow?

WIFE: Oh, my husband’s somewhere in the woods. (proudly) He’s undoing a spell. (moving to the shoes) Now, the Prince, what was he like?

CINDERELLA: (creeped out) (Pg 39) I must get home! (runs away)

WIFE: Wait! I need your shoes! (begins to chase Cinderella. Cow moos; she changes direction to chase the cow) Hey. Come back here! ******* (Another part of the woods) *******

BAKER: (Pg 40) (looking at his watch) One midnight gone.

WIFE: (Pg 45-46) (coming up behind him; she startles him again) I see you’ve the red cape.

BAKER: Yes. Only two items left to locate.

WIFE: Three.

BAKER: WHAT HAVE YOU DONE WITH THE COW!

WIFE: She ran away. I never reached home. I’ve been looking for her all night.

BAKER: (upset) I should have known better than to have entrusted her to you.

WIFE: She might just as easily have run from you!

BAKER:But she didn’t! WIFE: BUT SHE MIGHT HAVE! BAKER: BUT SHE DIDN’T!

WITCH: (appearing from nowhere) WHO CARES! THE COW IS GONE! GET IT BACK! GET IT BACK!!!!

BAKER: I don’t like that woman. (they exit in opposite directions.) ******* (Another part of the woods) *******

WITCH: (Pg 57) Two midnights gone!

WIFE: (Pg 51) (to herself) I hope there are no witches to encounter

RAPUNZEL: (sings a tune without words)

WIFE: (hears Rapunzel’s singing and sees her glorious hair as she brushes it near the tower window) (Pg 27) The hair as yellow as corn! (Pg 51) (calling up) Rapunzel, Rapunzel? Let your hair down to me.

RAPUNZEL: (Dubious) Is that you, my Prince?

WIFE: (in a deep voice) Yes. (Rapunzel lowers her hair out the tower window)

(Wife yanks her hair three times. Each time Rapunzel’s song is interrupted by the tugging. On the third yank, Rapunzel screams and the hair falls into the Wife’s hands. She runs away)

******* (Another part of the woods) *******

BAKER: (Pg 53) (enters dejectedly leading the cow by a rope, he spies his wife) I thought you were returning home.

WIFE: You’ve the cow! BAKER: Yes. I’ve the cow. We’ve only two of the four.

WIFE: Three. (reveals the hair she was hiding behind her back) Three! (Pg 27) The hair as yellow as corn! (Pg 54) And I almost had the fourth, but she got away.

BAKER: We have one entire day left. Surely, we can locate the slipper by then.

WIFE: (Pg 85) I wish (Suddenly notices a golden slipper on the ground; she squeals in delight) (Pg 65) The slipper! We’ve all four!

WITCH: (appears out of nowhere) (Pg 67) The third midnight is near. You’ve all the objects? (Pg 68) Feed the objects to the cow! You heard me. Feed them to the cow! (the Wife mimes feeding the items to the cow) Now fill this! (hands over a goblet, and the Wife milks the cow and hands the goblet to the Witch who drinks it down)

BAKER: (Pg 69-70) We’ve given you what you wish.

WIFE: Now when can we expect a child?

BAKER: What’s wrong? What’s happening. (the Witch begins to shudder and move away)

WIFE: (suddenly very pregnant) Wait. Where are you going? (the Witch turns around with a flourish. She has been transformed into a beautiful woman)

NARRATOR: The witch, who had been punished with age and ugliness that night when her beans had been stolen and the lightning flashed, was now returned to her former state of youth and beauty.

WITCH: (Pg 73) (raises her arms to put a spell on the Baker and his Wife once again, but only a pathetic puff of smoke comes from her hand. She tries again. No success)

NARRATOR: As is often the way in these tales, in exchange for her youth and beauty, the witch lost her power. (Pg 74) And it came to pass, all that seemed wrong was now right. The kingdoms were filled with. Ever after. (The witch snorts in derision and stomps off).
```

---

## IC-0817: Jabber

- Title: Jabber
- Author (byline): Marcus Youssef
- Work: Not specified
- Publisher: Talonbooks
- Publication date as stated: Dec 2015
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, ACTOR 1/3, FATIMA, MELISSA’S FRIEND, FATHER, ACTOR 2/3, HISTORY TEACHER, JORAH
- Teaser before the introduction: Yes
- Spoken words (computed): 1682
- Already set (do not supply): none

### Source block (context only)

```text
Author: Marcus Youssef
ISBN: 978-0889229501
Publisher: Talonbooks
Date (Month/Year): Dec 2015
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: Jabber by Marcus Youssef.
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actor – Actor 1; Actor 1/3; Melissa’s Friend; Father, and Jorah Actress -- Actor 2; Actor 2/3; History Teacher; and Fatima

ACTOR 1: (Pg 3-5) Hey. I’m (actor name)

ACTOR 2: Hey. I’m (actor name) . . . . Let’s say we’re in a high school.

ACTOR 1: Oh look, we are. Let’s say her name is Fatima.

ACTOR 2: Let’s say Fatima’s only been in ___________ (insert location. Original script designates Canada) for a couple of years.

ACTOR 1: Let’s say the country she’s from is, like nine thousand kilometers away.

ACTOR 2: And there was some kind of war –

ACTOR 1/3: Let’s say her parents just forced her to switch schools and come to this one because of something that happened at her old school . . . . Something bad.

FATIMA: Not bad, just stupid. I was with my friends, Seema and Hama and Lindsay. Lindsay’s a white girl, but she hangs out with us. We call ourselves the jabbers. Cuz of the hijab. Ha ha. When we get to school, there’s like four police cars and a pile of cops. Standing around the wall outside the gym. Staring and pointing and talking into their walkie-talkies. It was just some graffiti.

MELISSA’S FRIEND: (Pg 32) What did the graffiti say?

FATIMA: “All Muslims must die.”

MELISSA’S FRIEND: Eww. That’s so racist.

FATIMA: Yeah. Anyway . . . (Pg 5-7) My parents totally freaked out. They were, like,

FATHER: “You are not safe, you must change schools. It was a threat, Fatima. You must remember: These people are full of hate. I will do whatever necessary to protect you from these animals.”

FATIMA: By forcing me to come here, a subway and two buses from where we live. St. Mary’s. There’s no Seema, or Hama. No jabbers at all. Let’s say today is my first day.

ACTOR 1: Let’s say my name is Jorah

ACTOR 2/3: Let’s say he’s that guy that people are a little afraid of –

ACTOR 1: He did something

ACTOR 2/3: Something bad -- Rumors – Let’s say maybe none of those rumors are true – Or maybe they are.

ACTOR 1: Today he got in trouble.

ACTOR 2: He was in history class – and the teacher was telling them about what happened to Jewish people in World War Two, how the German army put them in gas ovens . . . and the teacher noticed Jorah not listening, so he called him out, in front of everyone.

HISTORY TEACHER: What do you think of that Jorah . . . The Nazis taking people – real, living human beings – and baking them alive in ovens.

JORAH: You mean, like pizza? Little mini dudes, all covered in cheese.

HISTORY TEACHER: Do you even know what you’re saying?

ACTOR 1/3: Let’s say Fatima was in the class and on their way out

ACTOR 2: He stared at her, for a while

ACTOR 1: Because of her scarf.

FATIMA: I know what they’re thinking. Whoa. What’s with the scarf? I bet she has to wear it. I wonder if she’s a terrorist. I bet she’s really, like, timid . . . . any of those things. (to Jorah, challenging) Hi. (to audience) I’m not shy. But it’s also, hijab, it’s part of who I am.

JORAH: (Pg 13-17) You’re new. If you’re planning on blowing up the school, I’m in.

FATIMA: Excuse me?

JORAH: A lot of kids would thank you. You’d be a hero. You know what? I’ll help. I’m ready. Just give me the signal. Nobody’ll suspect me cuz I don’t look like a terrorist.

FATIMA: Like me. (Beat)

JORAH: What’s your name? (Fatima ignores him) Oh, I get it. You don’t want to blow your cover. You’d be a crap terrorist if you told people your real name.

FATIMA: Ha ha. Fatima.

JORAH: Fatima . . Mind if I call you Fat?

FATIMA: No. Mind if I call you a-hole? (Jorah reacts to her use of profanity) You think because I’m Muslim, I can’t swear?

JORAH: A-hole’s not exactly a swear. You got, like some wicked forehead zits? Covering up some major pus bombs? That why you got the head thing?

FATIMA: My scarf? It’s part of my religion.

JORAH: It’s called a Taliban, right?

FATIMA: Taliban? Oh, my God. Now that’s funny. Taliban are the guys who are fighting in Afghanistan. It’s called a hijab.

JORAH: Oh. Do you wear it all the time? . . . In the shower? In bed?

FATIMA: I only have to wear it in public. I don’t wear it at home.

JORAH: Is it to stop you from turning guys on?

FATIMA: Oh, my God. It’s to show humility. Before God.

JORAH: Is it, like, those Taliban guys might think you’re so hot, they’d see your hair and just, like, lose control? I saw this old Chuck Norris movie where they catch a bad, like, Muslim Taliban dude and tie him up and force bacon down his throat. It was pretty funny.

FATIMA: (Pg 18) Huh. I saw this movie once about this dumb white boy who talked about a lot of crap he wasn’t smart enough to understand. Oh hang on, that wasn’t a move. That’s what’s happening right now. . . (Fatima starts to leave) By the way, if you say any more weird, racist, or insulting things to me, I will use my terrorist skills to kick you in the crotch so hard you’ll be down on your knees begging for your life. Just sayin’ (Exiting) See ya. **** (Scene change) – Fatima arrives home*****

FATIMA: (Pg 22-23) (Speaking to her parents on her way to her room) It was fine, thank you. I’m going to my room. Homework. (to audience) We moved three years ago. I was thirteen. You climb on a plane, fly for two days, and you land in the middle of winter. I’d never seen snow in my life. I spent a lot of time on my computer. Convinced them I needed it in my room – for homework. I sped a lot of time on TeenChat. I don’t talk. I just watch. Teenagers. They’re all white. That’s how I learned to speak English. I watch them. Girls, talking to guys. Flirt and smile and make faces. It’s shocking what these girls do. “Oh, my God, what? No! I love you. You can’t tell them.” Is that normal? Not for jabbers . . . **** (Scene change) – Jorah and Fatima video chat*****

FATIMA: (Pg 49-51) Hi

JORAH: Smile. . . . just do it. Please? (She smiles) You look awesome. (Pg 43) I googled how to talk to Muslim girls. It said to tell you I saw your hair, so that means you have to marry me.

FATIMA: (Pg 39) If my parents knew I was even talking to you, they’d kill me. And they’d kill you too. They’d track you down.

JORAH: Seriously?

FATIMA: Oh yeah. They’d go all ISIS on you.

JORAH: Ha ha. You could stand up to them. Tell them it’s different here. You have a right to do what you want. (Pg 41) The whole Muslim thing? It’s kind of super-hot!

FATIMA: (Pg 49-51) I’ve never done this before. Back home I wouldn’t have even thought of it. There would have been no way. But here . . . it’s like everyone can do whatever they want . . . so the weirdest thing happened today? I overheard . . . somebody was talking about your dad.

JORAH: What did they say? Who? (Beat) (Pg 53-55) People think they know. They think they know about him, and me. But they don’t That don’t know anything. (Beat)

FATIMA: You can trust me. (Beat) I’ve never – what we’re doing – this? If my parents found out, I’d be dead. For me to do – even this – with a boy, it’s the most shameful thing they could imagine. And I know you don’t understand, but if I’m going to do that, I need to know who I’m doing it with.

JORAH: You’re not like your parents, right? Me too. I’m different that my dad too.

FATIMA: Tell me. (A long beat)

JORAH: I was in my room, and they were fighting in the kitchen. I looked down the hall. Mom was holding her face, and there was broken stuff on the floor, and he was pacing back and forth. He was crying, and throwing s***, and yelling he was sorry all at the same time. After, people looked at me different. Like I was dangerous. Like they had a reason to be scared. It was all over the news. If you google our name, it’s what comes up. He got three years, with no parole, because they said it wasn’t the first time. That thee was a “pattern of abuse.” Which I guess is true. But, honestly, until I heard the ambulance that day, I hadn’t ever really noticed.

FATIMA: Oh, Jorah. I’m so sorry. Did he ever . . . hurt you?

JORAH: No. I mean, I don’t know. Not really.

FATIMA: (Pg 56-57) Jorah . . I won’t tell anyone . . . trust me. (blows a kiss) I know what it’s like to have people think you’re a freak. To want to be like everybody else. (She starts to remove her hijab, showing more of her hair – This is a very big deal in her culture) . . . I trust you. (blows a kiss) **** (Scene change) – The next day at school *****

JORAH: (Pg 60-63) Hey. I’ve been trying to find you. (Fatima is embarrassed and feeling very guilty – she doesn’t respond or even look at Jorah) I brought you something . . . a surprise . . . You have really pretty hair. Here (handing her a print of a photograph) It’s [a] screenshot.

FATIMA: (panicked) You can’t show this to anybody. I could get in so much trouble.

JORAH: You trust me, remember?

FATIMA: You don’t understand. I shouldn’t have taken off my scarf.

JORAH: Why not? You wanted to. What’s the big deal?

FATIMA: My whole life, that’s what. . . And my family . . . and my religion. What I did is a sin – a sin against God.

JORAH: Showing me your hair?

FATIMA: You don’t understand. We’re too different (Beat)

JORAH: (Angry – taking back the photograph) “The most beautiful girl in the world.” That’s what I wrote on it (ripping it up) There. Now you’re safe. (He stalks off) **** (Scene change)****

ACTOR 1: (Pg 72-75) Let’s say that night Fatima got a text

ACTOR 2: Check Facebook. Now!!!! . . . . it was a new page.

ACTOR 1: “My Muslim ex-girlfriend takes off her hijab”

ACTOR 2/3: Let’s say Jorah had recorded their chats because sometimes he hates how girls treat him – like he’s already done something wrong.

FATIMA: I showed my parents. It was the hardest thing I’ve ever done. I said, “All I did was blow kisses and show him some hair.” I was crying, but I was, like “What’s the big deal? Is that really so bad? Do you know what girls do online?”

ACTOR 2: Sometimes people do things that they regret.

ACTOR 1/3: Let’s say Fatima’s parents freaked out. . .

ACTOR 2: [There was] a Muslim family in another part of the country who murdered their two daughters because they thought they had dishonored their family. . .

ACTOR 1/3: Fatima’s parents surprised her . . .

FATIMA: [The] next day they told me my punishment . . . . No more computer in my room.

ACTOR 1/3: [They] let her go back to her old school and reunite with Seema, Hama and Lindsay.

ACTOR 2: (Forward) Both Fatima and Jorah live under a cloud

ACTOR 1: Because of her religion

ACTOR 2: Because of his past.

ACTOR 1: Both are smothered by assumptions and preconceptions.

ACTOR 2: The tension comes from [the] expectation of irrational violence – and that is exactly [the author’s] point. We’ve been conditioned to expect the worst.

ACTOR 1: (PG 75) There’s almost two billion Muslim people in the world.

ACTOR 2/3: They’re not all the same.

ACTOR 1: [And not every child will follow in the violent footsteps of his father.]
```

---

## IC-0818: Jerry Finnegan’s Sister

- Title: Jerry Finnegan’s Sister
- Author (byline): Jack Neary
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: Aug 1993
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BRIAN, BETH
- Teaser before the introduction: No
- Spoken words (computed): 1131
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jack Neary
ISBN: 978-0871293008
Publisher: Dramatic Publishing
Date (Month/Year): Aug 1993
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Every guy has as specific girl-next-door prototype, but in general, she's the girl whom you always admired from afar and were afraid to approach

ACTRESS: Who me? Cute, kind, unassuming, and honest! Thank you!

(next 2 lines are said concurrently)

ACTOR: So why am I so afraid to even talk to her? I’ve known her . . . . forever

ACTRESS: So why is he so afraid to even talk to me? I’ve known him . . . . forever

ACTOR: It’s because she’s Jerry Finnegan’s Sister

ACTRESS: by Jack Neary.
```

### Performance text (classify this)

```text
BRIAN: Look, you don’t know me. That’s a problem. I’m telling you this story, see, and it’s about me, sort of, but it’s mostly about her. I got up this morning and I said to myself: “Today is the day. Today I will make contact with Jerry Finnegan’s sister come Hell or high water.” There’s she been, next door, for most of my life, and here I was, doing absolutely nothing about it. It was so frustrating. From our very first meeting, when the Finnegans moved next door. I was about seven.

(FLASHBACK)

BETH: Hi!

BRIAN: Who’s that? Aawww. The new kid has a sister? That stinks!

BETH: Hi!

BRIAN: No! I don’t wanna say hi!

BETH: Hi!

BRIAN: I’m not gonna play with you.

BETH: Okay

BRIAN: You can’t make me.

BETH: Okay

BRIAN: My father sweats through two shirts when he jobs.

BETH: My father . . .

BRIAN: And he lets me stand on the hamper and watch him bleed when he shaves.

BETH: My father . . .

BRIAN: And he says if it stinks, it stinks and we should say it stinks!

BETH: MY FATHER EATS LIGHT BULBS AT PARTIES!

(PRESENT – To Audience)

BRIAN: After that I didn’t have anything substantial to say to Beth for a long time. She made me crazy. I guess though that my silence was trying to make a point. Although, mainly, I think I was just trying not to get humiliated.

(FLASHBACK)

BETH: I know you’re setting up in your room, Brian. Know what I’m reading? It’s a book called “Meet Your Body.” It tells you all about every single solitary inch of your body and what you’re supposed to do with each part! How come you talk to Jerry but you won’t talk to me? Is it because I’m a girl and you’re a boy? I’ve met my body. I know the difference! Well . . . want me to tell you how the book turns out?

(PRESENT – To Audience)

BRIAN: We had that book the year before. All I could think about when she yelled up at me that day was Chapter Nine. Then I thought about Beth. Then I thought about Beth and Chapter Nine! Then I threw up. It occurred to me at twelve years old that I was no longer able to retain Beth Finnegan as the object of my pre-adolescent scorn. All I had to do was come up with the right words. But the words got in the way. Actually . . . other thinhs got in the way as well.

(FLASHBACK)

BETH: Boys.

BRIAN: Boys?

BETH: I like boys a lot!

BRIAN: Don’t say that.

BETH: Why not?

BRIAN: Somebody’ll hear you.

BETH: Boys, I hope!

BRIAN: But you can’t just . . . say things like that . . . You have to . . . you know . . . think them and hope the . . . people you’re . . . thinking about . . . think back the same thing.

BETH: OK, what if it’s you? You’re at a party and you bump into a girl you like. And she looks right in your face . . . and she says, “I like boys, a lot!” What do you do?

BRIAN: I . . . I turn the other way.

BETH: A girl looks you in your face and says, “I like boys, a lot!” and you turn the other way? WHAT AM I GONNA DO WITH YOU?!

BRIAN: I DON’T KNOW, WHAT ARE YOU GONNA DO WITH ME?!

BETH: Brian? You are one sick puppy!

(PRESENT – To Audience)

BRIAN: She noticed! Anyway, before I can do anything about it, she turned fourteen. I no longer have the nuns as my allies in keeping the boys away from the girls in the schoolyard. Beth Finnegan, the girl next door, is now fair game to each and every budding hormonal case a Chelmsford High.

(FLASHBACK)

BETH: Stanley Tryscinski asked me out! And he’s sixteen!

BRIAN: So you went.

BETH: On a date!

BRIAN: Did you enjoy yourself?

BETH: Yeah, until he kissed me. That wasn’t so wondrous. But it was memorable.

BRIAN: Oh, Beth. Why did you let Stanley Tryscinski have your first kiss?

BETH: He was there.

(PRESENT – To Audience)

BRIAN: I know what you’re thinking . . . you’re thinking: “There it was, Bozo. That was your chance. All you had to do was find the right words and it would have been your turn.” Every time I came in contact with her, something inside me said, “Brian, this is your life’s work. This woman is your future. Do something about it.” So I tried. In my own way.

(FLASHBACK)

BETH: Are you going to your prom?

BRIAN: I haven’t given it much thought.

BETH: Well, do you have somebody to go with?

BRIAN: (to audience) My entire life flashed before my eyes . . .

BETH: Brian?

BRIAN: (to audience) Thee seconds it took. And that included the good parts.

BETH: Brian . . . why are you looking at me like that?

BRIAN: (to audience) Was I actually going to say it?

BETH: You weren’t going to ask me, were you?

BRIAN: (to audience) Nope. (to Beth) No! Oh, no! Of course not!

BETH: Oh, well, I was just wondering. I’ll go try on the next one.

(PRESENT – To Audience)

BRIAN: Jerry and I both got into UConn on track scholarships. But, as much as I trusted Jerry Finnegan, I could not, for the life of me, tell him how I felt about his sister. Jerry and I kind of parted ways during my junior year. Which was where things stood last night when I got the call from Jerry telling me Beth was getting married. So, all day today I’ve struggled to put the words together in my brain. The words are now there. Now they have to get to her. And I have to do it by phone. I cannot look her in the face and say what I have to say. (Dials phone)

BETH: (on phone) Hello?

BRIAN: Hello.

BETH: Brian?

BRIAN: Hi . . . Jerry called me last night. He said . . . you were going to get . . . married.

BETH: Are you going to congratulate me?

BRIAN: Oh . . . yeah . . .

BETH: There is no guy, Brian.

BRIAN: Who is there then?

BETH: I’m not getting married.

BRIAN: But, Jerry said . . .

BETH: Jerry cares very much about you, Brian. He knows you very well.

BRIAN: Yeah, but . . .

BETH: I think this is it . . . I think your best friend has set you up and I think this is your chance and I think you’d better grab it.

BRIAN: You mean Jerry lied to me?

BETH: To get you to call me, yes.

BRIAN: And, the thought that if I were mad enough I’d finally tell you . . .

BETH: Say it, Brian!

BRIAN: (to audience) This is it. The time has come to ask the question I’ve been avoiding for almost ten years. The hardest question ever asked since the dawn of time. And after the question will come the answer that will seal my fate. Talk about crucial. (to Beth) Will you go out with me sometime?

BETH: Ok. How about tonight?

BRIAN: (pause) No. Now. Meet me in the driveway now!

BETH: Now?

BRIAN: Now!

(SCENE)

BETH: Ok. I’m here. What’s going on, Brian?

BRIAN: Beth, will you go out with me sometime?

BETH: I already said I would.

BRIAN: (Grabs her shoulders) Beth . . . will you go out with me sometime?

BETH: Oh . . . oh, yes, I will.

BRIAN: I did it.

BETH: You asked me to my face.

BRIAN: Yeah. And you answered me to mine. And I’m still here. I’m still Brian.

BETH: Looks that way.

BRIAN: You said yes.

BETH: I said yes.

BRIAN: (to audience) Well, that’s it. You can go home now.
```

---

## IC-0819: Joan

- Title: Joan
- Author (byline): Robert Mauro
- Work: Two-Character Plays for Student Actors
- Publisher: Meriwether Publishing Ltd
- Publication date as stated: March 1988
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JOAN, PRIEST
- Teaser before the introduction: Yes
- Spoken words (computed): 1760
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Mauro
Book: Two-Character Plays for Student Actors
ISBN: 0916260534
Publisher: Meriwether Publishing Ltd
Date (Month/Year): March 1988
```

### Introduction (context only: never use it for content warnings)

```text
PRIEST: History has had its fair share of monumental heroines.

JOAN: From Queen Elizabeth to Hilary Clinton.

PRIEST: Harriet Tubman to Emilia Earhart,

JOAN: Catwoman to Britney Spears.

PRIEST: And of course, who could forget Joan of Arc? (gestures to Joan who curtsies)

JOAN: Why, thank you.

PRIEST: And I get to hear all of this cross-dressing barbecued soldier’s thoughts in

BOTH: “Joan” by ________________

JOAN is sitting in one chair. A long chain runs from the wall to her leg. The PRIEST stands with his back to JOAN. His hands are folded in prayer.
```

### Performance text (classify this)

```text
JOAN: So I am to die tomorrow?

PRIEST: Yes. I fear it has been decided.

JOAN: I should have guessed it would be.

PRIEST: It is God's will.

JOAN: Don't blame it on God. Everybody blames everything on him.

PRIEST: (Turning to face her) Are you saying then it is not God's will?

JOAN: It is more likely the wishes of men.

PRIEST: Who speak for God.

JOAN: Who at least presume to.

PRIEST: (At a loss for words) As you say.

JOAN: (After a pause) Father?

PRIEST: Yes, Joan?

JOAN: Does it hurt to be burned at the stake?

PRIEST: (Turning away from her) Joan, must we talk of that?

JOAN: (She shrugs.) I was just curious. Will I suffer much? Or will I just-

PRIEST: (Turning towards her) Must we talk of this?

JOAN: I was just curious. OK? I've never been burned at the stake before.

PRIEST: Can we speak of more pleasant things?

JOAN: Such as?

PRIEST: The weather.

JOAN: (Laughing) The. . . weather?

PRIEST: It is a lovely day.

JOAN: Yes? Really? (She goes to Stage Left and stands on her tiptoes.) I cannot see out my only window. What month is it?

PRIEST: It is May.

JOAN: (Still stretching, trying to look out the high window) Oh, wait. I can see the sky. It does look quite blue.

PRIEST: A glorious day. You should hear the birds singing.

JOAN: (She stands with her arms folded.) I fear I'll be hearing plenty of doves quite soon. (She shivers.)

PRIEST: Are you cold, Joan? (He goes to give her his cloak.)

JOAN: As death. (He stops and she goes to sit down.) It is damp and cold in here. And there are no birds singing.

PRIEST: I fear not. (He sits on a chair on the other side of the table.) Do you wish to confess your sins?

JOAN: I'd rather talk about the weather.

PRIEST: Ah, yes. Well, it is-

JOAN: (Finishing for him) A glorious day.

PRIEST: Truly.

JOAN: I used to love playing in the leaves when I was a little girl. Every autumn we'd rake them into great piles. Then run across the meadow and jump into them. It was. . . glorious.

PRIEST: Yes.

JOAN: Did you play in the leaves when you were a little child, Father?

PRIEST: (He thinks.) I imagine so. But it was so long ago. Still. . . I imagine I did. I and my brothers and sisters.

JOAN: Were there many?

PRIEST: Leaves?

JOAN: No. Brothers and sisters.

PRIEST: Ah, indeed. Eight.

JOAN: Eight. Really? I have three brothers and one sister.

PRIEST: All soldiers?

JOAN: No.

PRIEST: What are their names?

JOAN: There is Jacquemin, Pierre, Jean and my sister Catherine. Catherine died as a child. What are the names of your brothers and sisters?

PRIEST: There is Jacque, Peter, Christopher, Marie, Jacqueline, Noel, Daniel and myself.

JOAN: A large family is so nice.

PRIEST: Except when we fought over the milk and the bread, as children will.

JOAN: Yes. So where are they now? Are there any more priests in the family?

PRIEST: No. Just me. But my sister Jacqueline is a nun.

JOAN: Ah. Your mother and father must be proud.

PRIEST: I guess.

JOAN: What? They are not?

PRIEST: They seem happier with my brothers who are soldiers.

JOAN: Soldiers? You mean like me? (He nods.) Really?

PRIEST: (He nods.) Yes. (Whispering to her) My mother thinks you are wonderful.

JOAN: God bless all our mothers.

PRIEST: (Blessing himself) Truly.

JOAN: And your father, Father? What does he think?

PRIEST: (He stands and walks to Stage Front and faces audience.) Not so wonderful.

JOAN: I see. Well, I am young. I admit to being unliked.

PRIEST: He says all women should-

JOAN: (Finishing for him) Have eight children, preferably all soldiers?

PRIEST: (Pointing at her) Amazing! How did you guess?

JOAN: When you're nineteen years old and about to be burned at the stake for wearing men's clothes, it isn't difficult.

PRIEST: Yes. Well, I fear you will not go to your final reward unless you confess. And dress as a woman.

JOAN: I dress as the soldier I am.

PRIEST: Then you will not confess?

JOAN: Confess what? That I fought for what I thought was best for my country? That I led my men as best I could for the glory of France and God? I will confess that. But I fear that is not the confession you are looking for.

PRIEST: No.

JOAN: As a result, I fear I will still be burned. Have they decided on a time yet?

PRIEST: (Shrugs) They don't tell me those things. It's just, "Father, go hear the prisoner's confession." Or, "Father, do this." Or, "Father, do that." I'm never told anything about the executions.

JOAN: Have there been many.

PRIEST: You'd be surprised.

JOAN: I sort of doubt that. So they don't tell you much either?

PRIEST: No. All they tell me is to pray. It's not a very demanding career.

JOAN: Well, Father... (Walks over to him, patting him on the back) I'm sure it's not easy listening to the confessions of those who are about to be barbequed. I guess most are pretty upset about the whole thing.

PRIEST: To say the least. It seems these days no one is in a hurry to go to their final reward.

JOAN: Why would they be with such glorious weather?

PRIEST: This is true. Perhaps if it rained a bit more often.

JOAN: Yes, perhaps. But then God does move in mysterious ways.

PRIEST: This is true.

JOAN: Still, rain would at least make it seem all the more apropos.

PRIEST: Perhaps.

JOAN: Nevertheless, I sort of doubt that, too. One is never in a rush for the ax or the stake - rain or shine.

PRIEST: I would imagine so.

JOAN: (She sits.) Take it from one who knows first hand. They are not.

PRIEST: Will you confess then and cleanse your soul of this sin?

JOAN: Can I be honest with you, Father?

PRIEST: Then you will confess?

JOAN: I wasn't talking about confessing. What I meant was I'd like to talk about my feelings about all this.

PRIEST: All what?

JOAN: This. My trial. My sentence. My execution.

PRIEST: Must we be morbid?

JOAN: It's certainly not my choice. (She stands and paces.) But since it has been as they say, thrust upon me, (To his face) I'll be as morbid as I have to be to make my point. OK?

PRIEST: (Backing away a bit) As you wish.

JOAN: (Pacing) As I wish? I wish I were back in that lovely autumn meadow of my childhood jumping into those big piles of leaves. But since that was then and this is now. . . (To his face again) and since I'm about to be barbequed, I'd like to set the record straight. OK?

PRIEST: In the form of a confession?

JOAN: NO! In the form of a protest! A diatribe! A chewing' out! A criticism, if you will.

PRIEST: If you will it.

JOAN: I sure do will it. (Paces as she talks) First off, they are not burning me out of any little problem with me dressing up in men's clothes. What a laugh.

PRIEST: This is no laughing matter.

JOAN: No? Watch me. (She laughs, then seriously) To continue.

PRIEST: Please do.

JOAN: I do please. I am being burned not for being dressed as a man, but for having the courage to act as one. To stand up and fight for what I felt was right, for what was my duty, for what my God would have me do.

PRIEST: You dare assume to know what God thinks?

JOAN: I know a lot of you men who do that and I don't see any of you being barbequed for it. Most of you become saints, if you know what I mean.

PRIEST: I think you assume too much.

JOAN: You might be right. But I know what my heart tells me and is it not through our hearts that God speaks to us? Isn't that what you all say?

PRIEST: Well- you also say God spoke to you in French and not in English.

JOAN: (She laughs ironically) I am French. (She shrugs.) I guess he figured I'd catch on faster if he spoke my language. Is that a sin?

PRIEST: Well

JOAN: Well, well, well. Confess it. It is a sin to you English, who have captured me.

PRIEST: (Whispering) Not to me. I think

JOAN: Unfortunately, it's not important what we little people think, Father.

PRIEST: I have often heard that.

JOAN: So if you ask me why I am being burned tomorrow, I will tell you. Do you ask?

PRIEST: What?

JOAN: Do you want to know the real reason I am going to be barbequed tomorrow?

PRIEST: I have this strange feeling you will tell me whether or not I wish to hear it.

JOAN: Yes. You are right, Father. You know me well.

PRIEST: (Whispering to her) It is an honor. (Louder) Then you will confess?

JOAN: (Whispering) To God I will. (Louder) Is it not your lot in life to hear the final ravings of those of us who are about to be (Still louder) barbequed for reasons of state?

PRIEST: (In a near whisper) We all have our crosses to bear.

JOAN: We do indeed. Or our flames.

PRIEST: And still you won't confess?

JOAN: You want my confession?

PRIEST: It would lighten both our hearts.

JOAN: (She sits in chair.) OK, OK. Here it is. You want to take notes?

PRIEST: That is not necessary. It will be between you, me and God.

JOAN: Yes. And the five guards your king has placed outside my door. I guess they fear the little maid of Orleans more than I thought.

PRIEST: (Whispering to her) They do.

JOAN: I guessed as much.

PRIEST: So . . .

JOAN: So I confess I did dress up as a man. But only because they aren't in the habit of making armor for women these days. Maybe some day, but not in the fifteenth century. Also, I confess I did take up arms. I did slay many in battle. I did wage war. I did all these things. Although we never fought on Sundays.

PRIEST: I have heard.

JOAN: Sunday is God's day and I did all these things for...(She stops and thinks.)

PRIEST: Yes... For whom did you do all these things, Joan?

JOAN: You see. That's the funny thing, Father. I did them for my king, my country and my God. You think I made the right choice?

PRIEST: It is not for me to say.

JOAN: Right. Now everyone is mum. Mum's the word. Let the girl burn. Do not stand up and defend her. Do not be a man. Do not protest too loudly. . . (In his face) Or at all.

PRIEST: I am just a priest.

JOAN: I am just a girl.

PRIEST: As you say.

JOAN: What does it matter what I say? Tomorrow I will be barbequed and my ashes will be scattered to the four winds. And that will be that for little Joan of Domremy, France. Right. Father?

PRIEST: One can never tell. God moves in mysterious ways.

JOAN: As you say.

PRIEST: So is that it?

JOAN: Is that what?

PRIEST: Your confession?

JOAN: If you like.

PRIEST: Joan, it's not for me to decide. It's for you to decide.

JOAN: I prefer to sit and wait. I am cold and tired. I just want to get it over with. I just hope everyone has a good time at the barbeque tomorrow. I know I used to love them. Of course, at those we were usually cooking a pig and not a person, but then I suppose if you were a pig you were not amused.

PRIEST: I would think not.

JOAN: Me, too. They sure squealed a lot. Guess I will too.

PRIEST: Joan!

JOAN: Sorry, sorry. I just keep thinking about those flames. I'll try to think of those great piles of leaves back home in Domremy, or maybe I'll think of the sunshine tomorrow. I have this feeling it's going to be a glorious day.

PRIEST: As you say.

JOAN: Yes. My heart tells me it will be.

PRIEST: (The lights dim out and a spotlight comes up on the PRIEST, who walks up front to stand before the audience.) Then it was all over, the executioner claimed there was nothing left of Joan - nothing at all, except her heart. That, said the executioner, would not burn. (He shrugs.) Who's to believe a demented, probably drunken, executioner? (He smiles, points to himself and whispers to audience.) Me. (Lights dim out as the curtain falls.)
```

---

## IC-0820: Joe Egg

- Title: Joe Egg
- Author (byline): Peter Nichols
- Work: Not specified
- Publisher: Grove Press, Inc
- Publication date as stated: June 1967
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BRI, SHEILA, BR
- Teaser before the introduction: Yes
- Spoken words (computed): 1666
- Already set (do not supply): none

### Source block (context only)

```text
Author: Peter Nichols
ISBN: 978-0802151155
Publisher: Grove Press, Inc
Date (Month/Year): June 1967
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: How do parents come to terms with their daughter's persistent vegetative state?

ACTRESS: At first, it seems that they deal with the situation by laughing about it. However, after nearly 10 years, Bri has given up hope for his daughter and believes that her death would be a release

ACTOR: His wife, Sheila, believes that she will one day recover.

ACTRESS: Bri's humor is indeed his way of dealing with the trauma

ACTOR: But Sheila's laughter is an attempt to keep Bri happy and the marriage together.

ACTRESS: The characters of Bri and Sheila represent opposite sides of the moral argument on such cases:

ACTOR: Do we have the right to decide whether a human being should live or die

ACTRESS: Or is it cruel to artificially prolong a life that consists only of severe fits and constant pain?

TOGETHER: Joe Egg by Peter Nichols
```

### Performance text (classify this)

```text
BRI: Sheila’s got a theory about Joe’s birth. She doesn’t blame the doctors. She blames herself.

SHEILA: I don’t say that. I say it wasn’t entirely the doctors.

BRI: Because she’d slept around

SHEILA: I think it was partly because I’d been promiscuous, yes, and my subconscious was making me shrink or withdraw from motherhood, all right!

BRI: That vicar told us it was the devil’s doing. Why don’t you believe that? It’s about as brilliant.

SHEILA: (shrugs) It comes down in the end to what you believe.

BRI: I’ll tell you what I believe.

SHEILA: I know what you believe.

BRI: (points at audience) They don’t. (To audience) I believe the doctor botched it. There was no other cause. (To Sheila) That specialist said as much, he said it had nothing at all to do with the way you’d lived or whether there was a nut in the family . . . or what kind of [cigarettes] you smoked. . .

SHEILA: He didn’t say the doctor did it either.

BRI: No. You’ve got a good point there. He didn’t mention that, quite true. He didn’t say, “Yes, he’s a shoddy midwife, my colleague, always was, I’ll see he gets struck off the register.” Very true Weakens my argument. That.

SHEILA: Oh, you’re so clever!

BRI: He’d only say for certain that it was a chance in a million it could happen again . . . It’s due to this that Joe lives at home with us.

SHEILA: She’s our daughter.

BRI: (to audience) She was on the way before we married. That feeds the furnace of guilt.

SHEILA: No need to tell them everything. (to audience) But she’s no trouble. It’s Brian. I don’t know which is the greatest baby. Watching somebody as limited as Joe over ten years, I’ve begun to feel she’s only one kind of cripple. Everybody’s damaged in some way. There’s a limit to what we can do. Brian, for instance, he goes so far – and hits the ceiling. Just can’t fly any higher. Then he drops to the floor and we get self-pity again . . . despair.

BRI: (To audience) How long do your labours last? Two, three hours? A day? Dilettantes! (Points a Sheila) Five days!

SHEILA: (To audience) This doctor kept on drugging me. (To Bri) You never thought it was going on too long?

BRI: Yes, but you leave it to them, don’t you? My mum taught me to believe in doctors.

SHEILA: The next I knew, they handed me this hairless yellow baby with forceps-scars all over her scalp. She was gorgeous. . . . But soon I began to notice these funny turns. We took her to our new G.P. (Sheila mimes holding a baby)

BRI: Baby. (Indicates mimed baby). (Points to himself) Doctor. What seems to be the trouble.

SHEILA: I don’t really know. Funny turns. Face-making. Blinking with her eyes, working with her tongue, shaking her head, then going all limp.

BRI: (tickling the baby and talking to it) Funny turns indeed at your age! Saucy beggar. We are not amused.

SHEILA: But what d’you think it is?

BRI: Gas. Have you tried Gripe Water? Let’s see what we can find in here. (Rummages in drawer, finds medicine, reads label). Ah, yes, this’ll put a stop to it.

SHEILA: Doctor – I wish you could see one of these turns.

BRI: Oh, I’ve seen them, dear. Got three of my own. Your first, is it? First baby?

SHEILA: Yes.

BRI: Well, dear, it’s like this. Take it easy, give ’em a chance. (Tickles the baby, looks again at medicine). Let’s see. Three times daily after meals. I’ve got a waiting-room full of people, dear. You try her with this and come back if there’s no improvement in – say – a week. And don’t fret, Bye-bye. . . . . Three days later

SHEILA: (urgently) Doctor –

BRI: Didn’t I say come back in a week? Why so soon?

SHEILA: She’s gone into a coma. She won’t take anything. She hasn’t fed for two days.

BRI: (Looks at baby, listens to it, claps hands by it, finally shakes it like a piggy-bank – goes humming back to the table, mimes dialing) Get me the Children’s Hospital . . . quick!

SHEILA: (turning to audience) I said to Brian, “I’ve got a feeling we shan’t bring her back.” But we did . . . eventually. I stayed in hospital with her for a few weeks, then left her there having tests. A few weeks later they called me to collect Joe from the hospital by which time we’d gathered that she wasn’t ever going to amount to much. But I was determined to know the best we could expect. And the worst. The pediatrician was German. (For this sketch, Bri uses a music-hall German accent)

BRI: Vell, mattam, zis baby off yours has now been soroughly test and ve need ze bets razzer battly so it’s better you take her home. I sink I can promise she von’t be any trouble. Keep her vell sedated you’ll hartly know she’s zere.

SHEILA: But, Doctor – can’t you tell me the results of the tests?

BRI: Vitch ones? Zere vere so many – (slight laugh. Lists on fingers) Electro-encephalopraph, scree-dimensional eggs-ray, blood urine and stool analyses, zis business vis needles in ze fontanelle –

SHEILA: Is that why her hair’s been shaved off?

BRI: Vell of course –

SHEILA: She’d only just begun to grow it. And did the needles make that scar on her head?

BRI: Ach, nein. Zis vos a liddle biopsy to take a sample of her brain tissue.

SHEILA: That’s a relief (She smiles quickly) I thought at first you bored a hole in her skull to let the devil out.

BRI: (Looks interested, confers with his assistant). Sounds gut. Did you try it? (To Sheila) My colleague says ve don’t do zat any more. (Shrugs) Pity! Vell – if you eggscuse me. (Moves to go)

SHEILA: But – Doctor, Doctor – What can she do?

BRI: Do? She can’t do nozzing at all.

SHEILA: Will she ever?

BRI: Mattam, let me try and tell you vot your daughter iss like. Do you know vot I mean ven I say your daughter vos a wegetable?

SHEILA: (Thinks for a moment, gets it, smiles) Yes! You mean “Your daughter was a vegetable.”

BRI: Ach himmel! Stil is, stil iss, always vill be! I have trouble vis Englisch werbs. Zere’s von born every eight hours, you know.

SHEILA: No, I didn’t. Is that true?

BRI: Oh, ja, ja. Not all as bas as zees case, of course –

SHEILA: Isn’t there anything at all we can do?

BR: But jawohl! You must feed her, vosh her nappies, keep her varm. Just like any ozzer mozzer.

SHEILA: But for how long?

BRI: Who can tell? Anysing can happen. You know zat. Diphtheria, pneumonia . . . vooping cough. (Breaks character) So—what happened then? We brought her home.

SHEILA: And the hospital passed the can back to our local G.P. He had to supply phenobarbitone and keep us happy. But the time came when I asked him whose fault it was.

BRI: Which is when he suggested the vicar might call.

SHEILA: Yes. Nice vicar. Sensitive. So concerned and upset at the sight of Joe – the fits were unusually bad that day – so we left her in the cot and had our chat in another room.

BRI: She’s a beautiful child. It’s tragic. Tell me – when you first – knew there was nothing to be done, how did you feel?

SHEILA: Well, of course, you find out gradually, not all at once. But there is a point when you finally accept it. And that’s – (shakes her head) Oh, very nasty. You think “why me?” I don’t know about the other mothers but I kept saying, “Why me, why us?” all day long. Then you get tired of that and you say, “Why not me?”

BRI: Tell me, what was your husband’s reaction to the child?

SHEILA: He used to say, “Think of something worse.” And of course that’s easy. Joe could have grown older and developed into a real person before it happened. Or she could have been a very intelligent spastic without the use of her limbs. Which is worse, I think, than being a kind of living parsnip.

BRI: Quote. You count your blessings . . . and that give you fortitude.

SHEILA: No, but it’s something to do. When you’re up against a – disaster of this kind – an Act of God – (Bri clears his throat) – it’s so numbing you feel you msut make some sense of it –botherwise – you’d –

BRI: Give up hope?

SHEILA: Yes. My husband doesn’t feel the need to make sense of anything. He lives with despair.

BRI: (coming out of character) Did you tell him that?

SHEILA: He says I shouldn’t look for explanations.

BRI: He doesn’t believe in God?

SHEILA: His own kind of God. A manic-depressive – He doesn’t like me praying.

BRI: You’ve been praying?

SHEILA: What else can I do? I look at that flawless little body, those glorious eyes, and I pray for some miracle to – get her started. It seems, if we only knew the key or the combination, we could get her moving. D’you think the story of Sleeping Beauty was about a spastic? (breaks out of sketch) He was a good man, kind and sincere.

BRI: He was, yes.

SHEILA: (to audience) As soon as we were admitted to the free-masonry of spastics parents, we saw she had even less character than the other children. So we began to make them for her.

BRI: Some never really suited.

SHEILA: No. Like the concert pianist dying of t.b.

BRI: I used to like the drunken bag who threw bottles at us if we didn’t fetch her gin and pip-tobacco.

SHEILA: But they were all too active. The facial expression wasn’t right. (Bri freezes – Sheila – to audience) I join in these jokes to please him. IF it helps him live the her, I can’t see the ham, can you? He hasn’t any faith she’s ever going to improve. Where I have, you see . . . I believe, even if she showed improvement, Bri wouldn’t notice. He’s dense about faith – faith isn’t believing in fairy-tales, its being in a receptive state of mind. I’m always on the look-out for some sign . . . . I think while there’s life there’s hope, don’t you? I wish he’d talk more seriously about her. I wonder if he ever imagines what she’d be like if her brain worked. I do.

BRI: Our marriage might have worked as well as most if Joe hadn’t happened. I was too young for it, that’s true, of course. I always will be. But Sheila might just have dragged me screaming into manhood. ‘Stead of which, I was one of the menagerie. She loved me as much as any goldfish or [plant]. So now it was a question of how to tell her I was leaving her. And when I went into it, I saw it wouldn’t only be about Joe, but also about my ambitions . . . . so in the end I better just creep away without a word . . . (Begins hurriedly putting various objects into his pockets, putting on coat, etc) So I’ve shaved and washed and packed a case . . . (Gets case from hall, stands near by) haven’t decided where I’m going yet.

SHEILA: I shall go on up. Will you carry Joe to her room when you come up? She’s such a lump. (Bri nods, Sheila leaves, Bri picks up his case and goes).
```

---

## IC-0821: Jojo Rabbit - Screenplay

- Title: Jojo Rabbit - Screenplay
- Author (byline): Taika Waititi
- Work: Not specified
- Publisher: Fox Searchlight Pictures
- Publication date as stated: Feb 9, 2019
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR, ROSIE, JOJO, VOICE, ADOLF, CAPTAIN K, FINKEL, FRAULEIN RAHM, YORKI, CHRISTOPH, HANS, ACTRESS, ELSA, WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1757
- Already set (do not supply): none

### Source block (context only)

```text
Author: Taika Waititi (based on the book Caging Skies by Christine Leunens)
ISBN: N/A
Publisher: Fox Searchlight Pictures
Date (Month/Year): Feb 9, 2019
Original Script can be ordered from Scriptfly.com
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: By 1936, all “Aryan” children in Germany over the age of six were required to join a Nazi youth group.

ACTOR: At ten, boys were initiated into the Jungvolk (Young People)

ACTRESS: Their sisters joined the Jungmädel (Young Girls).

ACTOR: *Hitler hoped that: “These young people will learn nothing else but how to think German and act German . . . And they will never be free again, not in their whole lives.”

ACTRESS: Indoctrination into a political ideology at such a young age had a profound impact on the children of Germany; one that was quite difficult to overcome as you will see in . . .

ACTOR: Jojo Rabbit – An Anti-Hate Satire

ACTRESS: Based on the book Caging Skies by Christine Leunens

JOJO: (Pg 1-3) (at home, getting dressed. He tightens his belt, pulls up his socks, clicks his heels

together and stops one foot down hard on the floor. At attention, he stares into a full-length
```

### Performance text (classify this)

```text
(based on the book Caging Skies by Christine Leunens)

Suggested Roles: ACTRESS: Rosie, Voice/IF Adolf, Captain K (Klenzendorf), Christoph/Hans, Yorki, Elsa, Woman

ACTOR: Jojo, Finkel, Fraulein Rahm

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Jojo and his mother Rosie are walking near the banks of the river . . . she has a skip in her step; it’s as if she wants to dance, but is trying to control the urge.

ROSIE: (Pg 51) These banks used to be full of lovers. There’d be singing, dancing, romance.

JOJO: There’s no time for romance, we’re at war. (he stumbles)

ROSIE: Surprise, surprise, your shoelaces are undone. Again. (she ties his laces) (Pg 52-53) You’re growing up too fast. A ten-year-old shouldn’t be celebrating war or talking politics. You should be having fun, climbing trees . . .

JOJO: But the Fuhrer says what when we win, it is us young boys who will rule the world.

ROSIE: Pah! The Reich is dying. We’re going to lose this war and then what will you do? All I’m saying is that life is a gift and we must celebrate it, hold on to it. We have to dance (she does a small twirl) to show God we are grateful to be alive. Dancing’s for people who are free. It’s an escape from all this.

JOJO: (petulant) Well I won’t dance!

mirror and takes a deep breath and encourages himself) Jojo Betzler, today you join the ranks of the Jungvolk in a very special training weekend. Today you become a man. (deep breath, nervous) I swear to devote all my energies and my strength to the savior of our country, Adolf Hitler. I am willing and ready to give up my life for him, so help me God. A strange adult figure passes behind him dressed in a Nazi uniform. It feels ghostly and fantastical. We’ll find out who this guy is very soon.

VOICE: (off-stage; comedic German accent) Now, Jojo Betzler, what is your mind?

JOJO: (a military response) A snake mind.

VOICE: (off-stage; comedic German accent) And Jojo Betzler, what is your body?

JOJO: (a military response) A wolf body.

VOICE: (off-stage; comedic German accent) And Jojo Betzler, what is your soul?

JOJO: (a military response) A German soul. (pause) Adolf, I don’t think I can do this. The voice materializes on stage. It is Jojo’s imaginary friend Adolf Hitler. He can only know what Jojo knows, so he’s more of a charming buffoon who floats through life with whimsical abandon.

ADOLF: What?! Of course you can. Sure, you’re a bit scrawny, unpopular and still can’t tie your shoelaces, but you’re the bestest little Nazi I’ve ever met. You’re gonna go out there and have a great time, Ok? Now Heil me man.

JOJO: (with little gusto) Heil Hitler

ADOLF: You can do better than that. Heil Hitler!

JOJO: Heil Hitler!

ADOLF: That’s it! (They start jogging, maybe dancing? on the spot, chanting together)

JOJO and ADOLF: Heil Hitler! Heil Hitler! Heil Hitler! HEIL HITLER! HEIL HITLER! (They scream and Jojo sprints out)

*****Hitlerjugend Camp ******

CAPTAIN K: (Pg 5-6) Welcome to the Hitlerjugend training weekend in which we will make men and women of you all. My name is Captain Klenzendorf - you may call me Captain K.

FINKEL: Captain K! Woo!

CAPTAIN K: This is sub-office Finkel. And Fraulein Rahm (Fraulein Rahm responds in an awkward way; be creative) Over the next two days you little critters will get to experience some of the things that the mighty German Army goes through every day. You have all been issued your Deutsches Jungvolk Daggers. Never be without them. And don’t try to stab each other.

FINKEL: No stabbing!

CAPTAIN K: Today you boys will be involved in such activities as bayonet drills, grenade throwing, gas defense, ambush techniques, war games, firing guns and blowing stuff up. (huge cheers from the boys) The girls will practice important womanly duties such as dressing wounds, making beds, and learning how to get pregnant. (groans of disappointment from the girls) Alright, let’s get to it.

FINKEL: On your feet you little Nazis! Let’s go!
*******(Pg 6-7) Montage scenes of Jojo and his friend Yorki “training”*******
Be creatively funny (calisthenics, war games, knife throwing, etc.)
*******Scene – Academic Traning*******
Jojo sits in a group of boys and girls. Fraulein Rahm is at the head of the class, writing the
children’s responses on the blackboard. One by one the children call out.

JOJO: (Pg 7) Horns! YORKI: Fangs!

FRAULEIN RAHM: Excellent work children. You forgot that the Jew is the offspring of Satan and sucks the blood of Christian children. Now, get your things together kids, it’s time to burn some books! (children cheer)

YORKI: (Pg 9) Jews sound scary, huh?

JOJO: Not to me. If I met one I’d kill it like that. (tries to snap his fingers) Like. . . that. *******Scene*******

CHRISTOPH: (Pg 10-12) There is no room in Hitler’s army for those who lack strength. We want hardened warriors who are prepared to kill. Can you do that? Johannes? Can you kill?

JOJO: (with bravado) Pff, of course. I love killing.

CHRISTOPH: Good. . . (uncovers a cage, takes out a bunny and holds it out towards Jojo) Kill it.

JOJO: Hummm???

CHRISTOPH: Wring its neck. Kill the rabbit.

JOJO: Oh, I’m ok. I might do it later . . .

CHRISTOPH: No later, NOW. Or are you scared?

JOJO: I’m not scared. I’m just allergic to fur and I don’t want itchy hands all weekend.

HANS: (takes the rabbit and shoves it into Jojo’s hands) Both hands around its neck and then one hard twist.

JOJO: (shaking, holds the bunny and looks it in the eye. He gulps, then drops the bunny and tries to shoo it away)

HANS: He’s scared and so are you. You’re as scared as a rabbit. Jojo Rabbit!

CHRISTOPH: Maybe we should snap your neck. (everyone laughs and begins to chant) Jojo Rabbit! Jojo Rabbit! (Jojo runs away) *******Scene – Academic Traning*******

CAPTAIN K: (Pg 36) (lecturing) If you see a Jew, tell the Gestapo and they tell the SS and then they go and kill the Jew. And anyone who helped the Jew. And, because these are very paranoid times, probably some other people just in case. It’s a pretty drawn out process.

JOJO: Even if the Jew hypnotized someone to make them hide the Jew in the first place?

YORKI: (Pg 9) But how would you know if you saw one? They can look just like us.

JOJO: (boastfully) I’d feel it’s head for horns. And they smell like Brussels sprouts.

CAPTAIN K: (Pg 36) Without their funny hats it’s damn near impossible. Someone should write a book on the subject. It’d make everything a lot easier. (This sparks an idea in Jojo’s head, (tries to snap his fingers and gets it on the 2nd try)

TRANSITION

ACTRESS: But Jojo’s patriotism is challenged when he discovers that his mother, a member of the resistance, is harboring a young Jewish girl, Elsa, in their attic.

ACTOR: Faced with a real person, rather than the monster he’s come to expect, his understanding of the world begins to change.

ACTRESS: His training tells him to turn her in to the Gestapo; but if he does, he also puts himself and his mother at risk.

ACTOR: And so, he arrives at a different solution . . . A solution that will force him to confront his allegiance to the Nazis and to question the belief system he has been taught.

Jojo approaches Elsa’s door. He knocks twice. (KNOCK-KNOCK) The door opens and Elsa sits in the doorway.

JOJO: (Pg 37) Ok, here’s the situation. If I tell on you, you’ll be in big trouble and I don’t think you want that. But then you’ll tell on me and my mother and we’ll be in trouble which I don’t want. So I will not cause any trouble for you if you promise to tell me everything about the Jewish race.

ELSA: We’re like you but human. Done.

JOJO: Please take this seriously. I want to know all your secrets. (he takes out a notebook) (Pg 60) I’m writing a book! “Yoohoo Jew“– It’s an expose on Jews (Pg 73) for the Fuhrer.

ELSA: (Pg 37-38) (laughs) Ok. Obviously we are demons who love money, right?

JOJO: (writing it down) Obviously. Everyone knows that.

ELSA: Your mother . . . she’s kind. She treats me like a person.

JOJO: But you’re not. Not a proper person.

ELSA: (looking him up and down) Are you?

JOJO: How dare you, Jew. You are weak like. . . an eyelash. I am born of Aryan ancestry. My blood is the color of a pure red rose and my eyes are blue like sapphires- (suddenly, Elsa has Jojo in a headlock, twisting his arm behind him) Ow ow ow ow ow ow. . .

ELSA: Break free, great Aryan. There are no weak Jews. I am descended from those who wrestle angels and kill giants. We were chosen by God. You were chosen by a pathetic little man who can’t even grow a full moustache. (releases him) The stronger race, huh?

JOJO: (Pg 40) (to audience) This book is going to be harder to write than I thought. (tries another approach - passes a pen and paper to Elsa) (Pg 44) So, I’d like you to draw a picture of where Jews live. A typical hive; where you all sleep, eat, and where the Queen Jew lays the eggs. I need background.

ELSA: You really are an idiot. Where Jews live. Ok. (quickly drawing) (Pg 47) Finished!

JOJO: I said to draw where Jews live. This is just a stupid picture of my head.

ELSA: (pushes her finger into his forehead) That’s where we live. (Pg 54-55) (Jojo sighs) What’s wrong? (beat) You want me to tell you about the Jews? Okay, in the beginning we used to live in caves, deep in the center of the Earth.

JOJO: Wait. (grabs his books and starts writing)

ELSA: Scary places full of strange and wonderful creatures all with one thing in common. . .

JOJO: (nodding, knowingly) Stealing the ends of penises.

ELSA: (laughing) No, you idiot. A love of art. You want the story or not?

JOJO: Continue. But I know it’s true, the penis thing. Rabbis use them for earplugs. (beat) Where are your horns?

ELSA: (thinking quickly) I’m too young. They grow when you turn 21.

JOJO: Ahhhh . . . (writing furiously)

ELSA: So, after many years of developing magic and spells, we slowly moved out of the caves and into the towns. These days we live among normal humans but often we will take over a house and hang from the ceiling when we sleep, like bats. (long beat) (Pg 65-66) You’re not a Nazi.

JOJO: What are you talking about? Of course, I am. I’m massively into swastikas, so I think that’s a pretty good sign right there.

ELSA: You’re not a Nazi, Jojo. You’re a 10-year-old kid who ‘likes’ Swastikas and ‘likes’ dressing up in a funny uniform and wants to be part of a club. But you’re not one of them. (Pg 75) Jews and Nazis are not friends. (this hits Jojo; beat) (Pg 78) The last time I saw my parents was at the station. They were put on a train. I ran. Slowly found my way back to the city. A friend of my father’s hid me. Then another friend, then friends of friends. . . till your mother took me in. (beat) I am still here. But my parents went to a place you don’t come back from.

JOJO: What is the first thing you’ll do when you’re free?

ELSA: Dance. (a large explosion sends Elsa scuttling for the attic as JoJo heads to the window)

JOJO: (Pg 79-80) (calling to the street below) Yorki, what’s going on out there?

YORKI: (off stage) The Russians Jojo, they’re coming. And the Americans from the other way. The whole world is coming! (Pg 81) And Hitler’s dead. He gave up and blew his brains out

JOJO: No. That’s impossible!

YORKI: Turns out he was doing some really bad things behind everyone’s backs. I’m not sure we chose the right side. I’m beginning to wonder if we might be the bad guys. (Pg 82)

(suddenly there’s a huge explosion and the street is engulfed)

JOJO: Yorki!!! Where are you? (music blares an anthem of some sort as American troops enter the city)

WOMAN: (Pg 83) The war is over! America is here! Everyone is free! We’re all going to get Levi jeans! America! Americaaaaaa!

JOJO: (turns back) (Pg 89-90) Get your things together. We’re leaving! (but instead of Elsa he sees his imaginary friend Adolf standing in his way)

ADOLF: Oh, no you’re not. You betrayed me, traitor.

JOJO: You betrayed everyone! I believed in you!

ADOLF: But you stopped believing; and now you’re best friends with that thing in the attic.

JOJO: That thing is a girl.

ADOLF: Fine. But you need me! I’m all you’ve got! You’re a scared little rabbit. You’ll die without me. Forget about that disgusting Jew up there. Come back to me where you belong.

JOJO: No . . . No . . . NO!!!! (he kicks Adolf as hard has he can between the legs – Adolf screams in pain and disappears into oblivion) (Pg 26) (Jojo goes to the CLOSED secret door and knocks twice) KNOCK-KNOCK. Excuse me? Hello? Um, Jew girl in the wall? (beat) Yoohoo, Jew? (beat. The door opens) (Pg 78) What is the first thing you’ll do when you’re free?

(Elsa smiles and the smile spreads to Jojo, then they begin to dance - not for anyone else, just for themselves and each other)
```

---

## IC-0822: The Kentucky Cycle

- Title: The Kentucky Cycle
- Author (byline): Robert Schenkkan
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: STAR, PATRICK
- Teaser before the introduction: Yes
- Spoken words (computed): 1031
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Schenkkan
ISBN: 0822213095
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Sixteen years before, Star was taken captive from her tribe by the brutal Michael Rowen, who severed the tendon in her heel so she couldn't run away. She has since resigned herself to life with the arrogant man.

ACTRESS: Their son, Patrick, has fallen in love with a girl on a neighboring farm, and here asks his mother for help in courting her.

TOGETHER: The Kentucky Cycle by Robert Schenkkan.

(Dusk. The front yard of the Rowen house. The original single room has been expanded. Among other additions is a simple front porch and steps. The house and yard are bare and unadorned, strictly functional. There is a pile of logs on the porch and an old axe. In the yard is a tin tub, partially filled with water. Patrick enters, cradling his rifle and a leather bag containing a pair of dead rabbits. Star limps in, carrying two wooden buckets full of water. She stops and looks at Patrick.)
```

### Performance text (classify this)

```text
Characters: Star (30s) a Cherokee woman kidnapped by Michael Rowen with the express purpose of providing him with an heir, and Patrick (16) their son. Scene: The Rowen homestead in Eastern Kentucky, 1792

STAR: Ostas hindhalid? [Good hunting?]

PATRICK: Couple of rabbits. Here, gimme those, Ma. (He throws his bag on the porch, lays his rifle down and takes the buckets from her. He pours them into the tub.)

STAR: To hi ju? [How are you?]

PATRICK: I'm fine.

STAR: It embarrasses you now to speak the language of your grandfathers?

PATRICK: No. It don't embarrass me. I just don't see the point.

STAR: Not to forget who you are, that is the point.

PATRICK: Not much danger of that around here, is there? (Beat.)

STAR: I'll bring your supper out. Cooler on the porch. (He sits. She goes in, returns with a bowl of food. She picks up the rabbits while he eats.)

PATRICK: Good.

STAR: Took you all day to get these? Losin' your touch.

PATRICK: Didn't take me all... (Before he can finish protesting, Star goes inside with the rabbits. She returns.) Most of the mornin' I sat up on the ridge.

STAR: Oh. Corn gonna plant itself this year?

PATRICK: I finished that piece on the Shilling.

STAR: Uh-huh. What's on the ridge worth a visit?

PATRICK: Nothin'. Just did me some thinkin'.

STAR: Alone? (Beat.)

PATRICK: Mostly.

STAR: I knew when that Talbert girl come sniffin' round here this morn in' you wasn't gonna get a lick of work done.

PATRICK: I planted the damn field!

STAR: Don't curse in front of your ma.

PATRICK: Don't see what you got against the Talberts. From what I hear you're a regular visitor over there. (Beat.)

STAR: What is it you hear?

PATRICK: You doctored her Pa.

STAR: His name is Joseph.

PATRICK: Joseph? Michael know about it?

STAR: What do you think?

PATRICK: I think he hears about it, he'll skin you alive.

STAR: Are you gonna tell him? (Beat.) Folks think I have the Gift for healin' and readin' dreams. Because I'm different. Because I'm Cherokee. Michael laughs, but as long as they pay, he laughs to himself. I think, why should he have all this money? Why not my son? And so, when I can, I see people secretly. Like Joseph.

PATRICK: For me?

STAR: Someday you'll want land of your own. A woman of your own.

PATRICK: Why hide it from me?

STAR: So if Michael finds out, he'll be angry only with me. (Beat. He crosses over and hugs her knees, puts his head in her lap.)

PATRICK: Do yu jiskanoqi. Skidoliga? [I am sorry. Forgive me?] (She kisses him on the top of his head, strokes his hair roughly.)

STAR: I gvkewidina. [It is forgotten.] You want this Ruth Talbert?

PATRICK: Rebecca.

STAR: Whatever. What she wants, you can give her easy enough. You don't have to marry her for that.

PATRICK: She ain't like that.

STAR: I see. Maybe she's smarter than I thought.

PATRICK: I love her.

STAR: You love her. Now. Today, you love her. But tomorrow? Next year? Chuji. Why so much hurry? Why marry her? (Beat.)

PATRICK: If I marry her, maybe her pa'd gimme that piece of bottom land next to ours. (She cuffs him.)

STAR: You are your father's son. Truly.

PATRICK: Not so's he'd notice.

STAR: I never understand this. What you two have is never enough. You work from sunrise to sunset and you can't plow all what you have now, but you want more. More land! Why?

PATRICK: It's the only thing that lasts. (Beat.)

STAR: You live like that, Chuji, you live a lonely life.

PATRICK: Somethin' different.

STAR: Everybody gotta right to some happiness, osta Chuji. You gotta right.

PATRICK: She makes me happy. Rebecca. (Beat.) You help me?

STAR: How?

PATRICK: Talk to him for me. 'Bout us. (She walks to the tub, runs her hand through the water.)

STAR: Michael don't listen to me.

PATRICK: He's comin' back. (She hesitates.)

STAR: You seen him?

PATRICK: This morn in' .

STAR: You sure?

PATRICK: Somebody was movin' thru the gap in a hurry.

STAR: Coulda been anybody.

PATRICK: Who?

STAR: When'lI he get here?

PATRICK: Tonight mebbe. Tomorrow for sure. But tonight I think.(Beat.) You could tell him... tell him that Talbert bottom land'd give us a third agin as much.

STAR: It'd give your pa a third agin as much. (She takes his bowl and starts into the house.)

PATRICK: Same thing. It's all gonna come down to me, innit?

STAR: Is it? (She sits on the porch. Patrick stares at her in confusion.)

PATRICK: What're you talkin' 'bout? STAR: I'm not sayin' nothin'. Said too much already. (Preoccupied, she absentmindedly strokes her injured leg.)

PATRICK: Your leg botherin' you a lot? (She shrugs. Looks off into the woods where Michael is.) Here. Lemme rub it for you. (He sits next to her. She hikes up her skirt and swings her leg into his lap. He begins to knead her scarred calf She leans back against a post, her eyes closed.) What'd you mean about... about the land not comin' to me. I'm his only son.

STAR: Are you?

PATRICK: What d'you mean, "Are you?" -"Is it?" You know somethin' why don't you just say it, 'stead of dancin' around!

STAR: Lower.

PATRICK: What?

STAR: Rub lower. (He does so.) What does Michael do in Louisville?

PATRICK: I don't know.

STAR: Home come?

PATRICK: 'Cause I ain't never been.

STAR: How come?

PATRICK: 'Cause I gotta stay here and take care of things! (Beat.) STAR: He got a woman down there.

PATRICK: How do you know?

STAR: I seen her in a dream.

PATRICK: You seen her?

STAR: Blue eyes, corn-silk hair. She always be crossin' a muddy river in my dreams.

PATRICK: Muddy water? That's death. (She nods.) Mebbe she's dead already.

STAR: Mebbe.

PATRICK: What I care if he got some woman down there? Specially if she's dead. now.

STAR: Mebbe she had him a baby.

PATRICK: He... got him another family down there?

STAR: Why else he always got to go alone? You a growned man, Chuji. With your help, he could pack in twice as much on these trips. You ever knowed Michael to turn his back on a dollar? How come he don't take you?

PATRICK: You seen the baby in your dream?

STAR: Clear as the bottom of the Shillin'.

PATRICK: Boy or girl?

STAR: She give him a son.

PATRICK: A son!

STAR: Where does that leave you?

PATRICK: I'd still be the oldest! It'd all still come to me! That's the law!

STAR: Law? (She laughs.) Michael ever pay a whole lotta mind to the law?

PATRICK: Why wouldn't he let me have my share?

STAR: You know why.

PATRICK: Why!

STAR: 'Cause he hates you.

PATRICK: That's a lie!

STAR: Look me in the face and tell me it is! (He can't.)

PATRICK: Why? Why's he hate me? Nothin' I ever do is right. Never has been. He looks at me like I was some kinda mad dog, gonna tear somethin' precious away from him.

STAR: He's afraid of you.

PATRICK: Afraid?! Hell, Michael Rowen ain't afraid of nothin'!

STAR: Look at yourself, Chuji, look! See yourself as you really are not like that hungry dog he turns you into, the one who whines and licks the hand that beats him. You are bigger than him now. And stronger. He sees you and he feels old. He feels tired. He sees death in you. That's how you scare him, Chuji, and that's why he hates you. Because there is no forgiving that. And that's why he will never give you your rightful share of this land. Your land. Not till you bury him innit! (Beat.) Ask him. You don't believe me? Ask him for your share and see what he says.
```

---

## IC-0823: King Chemo

- Title: King Chemo
- Author (byline): Brian Guehring
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: Oct 2006
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: KEVIN, ICE QUEEN, PUPPET MAN, MELISSA, DOCTOR, MELISSA & DOCTOR, NURSE, AGENT X, AGENT 5, DOCTOR/5, NURSE/X
- Teaser before the introduction: Yes
- Spoken words (computed): 1925
- Already set (do not supply): none

### Source block (context only)

```text
Author: Brian Guehring
ISBN: 978-1583423677
Publisher: Dramatic Publishing
Date (Month/Year): Oct 2006
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: When we were small children, trying to get to sleep, a creaking floorboard was really spooky.

ACTOR: There's a pirate coming up the stairs . . .

ACTRESS: . . . or a monster in the closet,

ACTOR: or more probably a dragon under the bed.

ACTRESS: Adults chuckle at the “pretend” world of children, but really, it’s the "safe" place of pretend that prepares children to accept the world's harsh realities.

ACTOR: Facing reality head-on is scarier than pirates or burglars or crocodiles . . . especially when that reality is cancer and the treatments that go along with the disease.

ACTRESS: Kevin is a 10-year-old with an active imagination who has returned to the hospital for chemotherapy.

ACTOR: His fantasies help him cope and allow him to believe, if only for a short time that leukemia doesn't actually exist but is rather a plot by the "Powers That Be.

TOGETHER: King Chemo by Brian Guehring
```

### Performance text (classify this)

```text
Suggested Roles: Actress – Melissa, Ice Queen, PuppetMan (scene 1), Doctor & Nurse (Scene 3), Agent 5/Doctor (Scene 4), Doctor (Scene 5) Actor - Kevin, Doctor & Nurse (Scene 2), Agent X/ Nurse (Scene 4), Nurse

(Scene 5)

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

(Superhero music fades up)

KEVIN: (in a recorded voice-over). Welcome back to "THE ADVENTURES OF INVINCIBLE BOY, Defender of Youth." When we last left our hero [a normal boy in appearance, but born of superhuman strength, agility, and intelligence], he had just been captured by his evil arch enemy, the Ice Queen (The ICE QUEEN enters wearing an ice-blue villainess costume [slightly resembling pastel-blue hospital scrubs}.) [the famous rising figure skating star who tragically crashed through thin ice transforming her into a villainess with an ice heart] and her devoted lackey, Puppet Man (PUPPET MAN enters wearing a marionette outfit [also remarkably resembling hospital scrubs].)

***** SCENE 1*****

KEVIN: So, we meet again, Ice Queen.

ICE QUEEN: Yes, Invincible Boy, and this time there is no escape. Puppet Man, get our prisoner a glass of ice water. (PUPPET MAN goes to get a glass of water.) I want you to feel welcome in my ice castle. Is it cold enough for you?

KEVIN: You can't freeze me, Ice Witch.

ICE QUEEN: You should really give up that heroism thing. It's so passe. You should join our side.

KEVIN: Join you? To do what?

ICE QUEEN: To eliminate fun, imagination, and everything that brings happiness. To create a world where pain, seriousness, and logic dominate the world.

KEVIN: How do you plan to accomplish this?

ICE QUEEN: By stealing toys, freezing amusement parks, and making boring television. If all else fails . . . we'll kill all the happy people. I could use you, Invincible Boy. Your superhuman strength, agility, and intelligence would help us. What do you say, partners?

KEVIN: Never.

ICE QUEEN: Maybe we can change your mind. Puppet Man, give him "the pill."

KEVIN: I won't take it.

ICE QUEEN: I think you will. (ICE QUEEN opens a drawer and dry ice smoke falls out as she selects a torture device [resembling a stethoscope}. ICE QUEEN places the torture device on KEVIN's back.)

KEVIN: AAAAHHHHH!

ICE QUEEN: So sorry, was that cold for you?

PUPPET MAN: This should answer any more questions you have about the plan of attack.

(PUPPET MAN hands him a pamphlet.)

KEVIN: (reading). "Cold-bloodedness and You: How an Emotionless Existence Increases Longevity." I'll never join you.

ICE QUEEN: Do you think you are strong enough to resist? Puppet Man, begin the ice treatment.

KEVIN: You can never defeat me. I am Invincible Boy, Defender of Youth!

ICE QUEEN: You won't be for much longer. (PUPPET MAN attaches a torture device [somewhat resembling an IV] on KEVIN's arm. KEVIN braces himself for the pain.) This treatment will slowly replace your blood cells with ice crystals. Later we'll replace your bones with icicles and your spinal fluid with ice water. You have four days to either join our side or permanently become Icicle Boy.

KEVIN: I'm strong enough to resist you.

ICE QUEEN: We'll see. For now, sit back and chill, Invincible Boy. We'll be back soon to start with your bones and spinal fluid. ***** SCENE 2*****

(The fantasy music fades. Lights reveal a small hospital room. MELISSA is sitting in her room as NURSE and DOCTOR enter.)

MELISSA: Good morning.

DOCTOR: Good morning, Melissa. Would you like a glass of ice water?

MELISSA: Yes, please. (NURSE goes to get a glass of water.)

DOCTOR: Melissa, we want you to be as comfortable as possible here. Is the room temperature OK?

MELISSA: It's fine. (NURSE hands MELISSA drink.) Thank you.

DOCTOR: We are about to start the treatment, but remember I can't do this alone. I need your help.

MELISSA & DOCTOR: Partners.

NURSE: This is to help you so you won't get nauseated. (Handing MELISSA a pill.)

DOCTOR: Now I'm just going to check your breathing. I'm sorry but this might be cold.

(DOCTOR uses stethoscope to check MELISSA's breathing.)

NURSE: We brought you another pamphlet. (NURSE hands MELISSA a pamphlet.)

MELISSA: "Chemotherapy and You: How a Nutritious Diet Aids Treatment." Thanks . . . So what's going to happen today?

NURSE: You're scheduled for [chemotherapy at] 2:00 this afternoon. We're going to begin your IV now. (NURSE begins hooking up her IV to her infusaport) I'll get Kevin so we can start his tests. (NURSE and DOCTOR exit. MELISSA starts to read pamphlet. KEVIN sneaks into the room and sees MELISSA.) ***** SCENE 3*****

KEVIN: Hey! Don't read that! (KEVIN rushes and takes the pamphlet away from her and starts jumping up and down on the pamphlet.) Don't believe a word in this.

MELISSA: What are you doing?

KEVIN: I'm destroying the evil propaganda from the Ice Queen. She gives it to everyone.

(KEVIN shows MELISSA his pamphlet then rips up the pamphlets.)

MELISSA: You're ripping up pamphlets on nutrition.

KEVIN: You can thank me later. So what brings you here?

MELISSA: Considering this is the cancer floor of a hospital, it's probably a safe bet I have cancer.

KEVIN: You must be a rookie. You see, I've been doing this for over a year now. I'm the king of chemotherapy. If you have any questions, just ask me. I've helped a lot of young kids get through chemotherapy. I fill them in on what's really going on. For instance ... (KEVIN goes to the hall to check for signs of the DOCTOR.) You have to watch out for the "doctor."

MELISSA: Why? She's been very nice to me.

KEVIN: Acting nice to you, but in reality she is pure ... Evil. She won't be able to hide it for much longer if you watch closely.

MELISSA: She's mean to all leukemia patients?

KEVIN: Yes. You see, only the really special kids get leukemia. The few, the proud, the leukemia kids. It's actually a great honor to be chosen for chemo.

MELISSA: Chemotherapy is an honor?

KEVIN: No. Chemo is terrible. The honor is being chosen. It means you were too strong to be broken through the usual means.

MELISSA: Who wants to break us?

KEVIN: (whispering) The Powers That Be. See, there is someone out there trying to control us Earth children. Obviously the entire hospital staff is in on the plan. I'm not sure who's behind it yet, but I think it's the "doctor." My mission is to discover who they really are and save the world's children from their evil plots.

MELISSA: How do the Powers that Be use leukemia?

KEVIN: They're trying chemicals. It won't work though. They can't control this mind.

MELISSA: Kevin, this may be a crazy idea, but have you ever considered the possibility that the chemotherapy is to stop the cancer?

KEVIN: Melissa, Melissa, Melissa. You are so young and naive. I can tell I have a lot to teach you about the real world. I'm not sick. They made this cancer thing up.

MELISSA: They didn't make cancer up.

KEVIN: They did. Ladies and gentlemen of the jury, I'm here to prove that leukemia doesn't exist. I would like to call an "alleged" leukemia patient to the stand. Miss Melissa, do you swear to tell the truth, the whole truth, and nothing but the truth so help you Elvis?

MELISSA: Sure.

KEVIN: Now, Miss Melissa, does your cancer hurt like a broken bone? [or] do you get a fever like you do when you get the flu?

MELISSA: No.

KEVIN: Ah-ha! Why are you still in the hospital, then? (Before MELISSA can answer.) Melissa, can they show you an X-ray and point out the leukemia?

MELISSA: Not an X-ray. But they have tests. They can extract a sample of bone marrow from your hip and determine if you have leukemia. They show you the test results.

KEVIN: Which are what? Photos? Numbers? Charts? Graphs?

MELISSA: They show you the number of cancer cells.

KEVIN: Numbers? Could they make up these numbers?

MELISSA: Well yeah, but. ..

KEVIN: (cutting her off). Ah-ha! Now, ma'am, is leukemia contagious? How did you get it?

MELISSA: They don't know yet how people get leukemia.

KEVIN: Because it doesn't exist? Ladies and gentlemen, I rest my case. (NURSE clears throat. KEVIN hits the floor to hide behind the bed, but his IV is still clearly visible.)

NURSE: Hoarding all the IVs, Melissa? Kevin, you can come out now.

KEVIN: (in a high-pitched voice). He's not here.

NURSE: Kevin, your bone marrow test and spinal tap are scheduled for right now. (DOCTOR enters taking off her gloves.)

DOCTOR: You can't just avoid these procedures, Kevin. Not taking the tests won't change whether you are in remission or not. I know a transplant is a scary idea, but you have to take these tests.

KEVIN: You'll try and give me a transplant no matter what your little experiments say.

DOCTOR: No, if you're in remission, no transplant. Trust me. (her pager goes off). Kevin, I can't argue now. (DOCTOR and NURSE exit.)

KEVIN: (to Melissa) [See] the doctor wants to use me as a guinea pig for her evil experiments.

MELISSA: They aren't experiments. It's treatment to fight the cancer.

KEVIN: Then why are the "doctor" and nurse are always wearing gloves? It's very suspicious.

MELISSA: It's so they don't touch the blood.

KEVIN: Nah, they wear gloves so they won't leave any fingerprints. They don't want to leave any evidence of their experiments. I'll prove it to you. C'mon.. (KEVIN and MELISSA exit.) ***** SCENE 4*****

(The secret agent command post. KEVIN enters a smoky, dark room with file cabinets, large tracking maps, blinking countertops, and sophisticated computers. He gradually gets weaker and dizzier as the scene progresses. KEVIN picks the lock and walks in. Alarm goes off "IN- TRUDER DETECTED." Lasers shoot off and KEVIN ducks many in slow motion. He is slightly injured as he dives out of the way.)

KEVIN: Powers That Be Command Central. There has to be proof of their plot here somewhere. Let's try here first. (KEVIN jimmies the lock on the files and begins looking for his file.) Bingo. (KEVIN hears footsteps and hides as AGENT X enters. He wears a dark trench coat, sunglasses and a large hat. AGENT X walks over to the files.)

AGENT X: The alarm was triggered. Someone has been in here. (AGENT X notices broken lock and searches for file.) Double O 5 won't like this. (A secret code knock is heard at the door.

AGENT X answers with a code knock.) The bald condor flies upside down.

AGENT 5: (off). My mother's hanky is snotty and stanky. (AGENT X opens door and lets AGENT 5 enter. AGENT X checks the hall behind her. AGENT 5 is also wearing a dark trench coat and sunglasses.)

AGENT X: I'm glad I caught you before you left. The target has flown the coop. I just went to his room and he's gone.

AGENT 5: Then track him! Signal his honing device and get him.

AGENT X: I can't. He took it out. It's still in his room.

AGENT 5: He's not plugged into the system? I told you we should have operated to implant it. Why would he take it out?

AGENT X: Maybe he discovered "the truth."

AGENT 5: Impossible. He's a kid. Nobody would believe him. Everyone ignores kids. What proof does he have?

AGENT X: Someone broke into the files and his file is missing. But as long as he can't get into the computer we're fine.

AGENT 5: We have to find him before the whole operation is blown. This is bad timing, we just got clearance for the "procedure."

AGENT X: If the "procedure" worked, we wouldn't have to worry about him again. Ever.

(AGENTS notice Kevin hiding behind a file cabinet and assume the personas of medical personnel)

DOCTOR/5: Kevin! What are you doing here?

KEVIN: I know about the Powers That Be.

DOCTOR/5: Where is your IV, Kevin? You need those antibiotics.

KEVIN: I took your little signal out.

DOCTOR/5: You don't look good. I'm taking you back to your room now. (slowly moves toward KEVIN). This is not time for one of your games. Without your IV, you will be weak, and things will seem out of control.

KEVIN: (escapes and runs to file cabinet, breathing hard). What are you trying to do? You're trying to take our freedom away! How are you doing it? (MELISSA enters from where she has been hiding) Melissa, get out of here!

MELISSA: You don't have to protect me, Kevin. I'm a spy working to expose the conspiracy, too. See the badge? How can I help you?

KEVIN: This is the command center and this is a spy, code name 5. She's in charge of the government plot.

DOCTOR/5: Kevin, I'm a doctor and this is our medical file room.

KEVIN: Stop lying. Tell me what this Procedure really is.

DOCTOR/5: It's a bone marrow transplant. Melissa, tell him I'm not some evil secret agent.

MELISSA: Kevin knows the two of you are secret government agents. What he doesn't know is that you're on our side. That you two are also working to destroy the Powers That Be. Right?

NURSE/X: Exactly, we're all fighting the same enemy, Kevin.

MELISSA: Our enemy isn't human, Kevin.

NURSE/X: Right. It is a strange invisible creature of origins unknown.

DOCTOR/5: I've studied it. I know how it attacks and how to strengthen your defense. I'm not going to take away your weapons to fight the Powers That Be. I'm adding to them.

KEVIN: (after a pause, collapses in exhaustion). OK. ***** SCENE 5*****

(KEVIN's hospital room. KEVIN is in his bed as DOCTOR and NURSE finish checkup.)

DOCTOR: Everything looks good. Your force field is working well and you're still on track to get your new ammunition in a couple of weeks. Very powerful. It can destroy anything.

NURSE: With heat-seeking target-locking capabilities. (NURSE exits with DOCTOR.)

MELISSA: (entering slowly) Hey, stranger! How are you doing?

KEVIN: Look, I was so weak last week because of my blood count. It wasn't me; it was the blood. Anemia. Once I got a new IV bag, I was fine.

MELISSA: I understand. I feel powerless when I have no energy.

KEVIN: (showing his infusaport). Look, I got a port. I'm going to have a bone marrow transplant in a couple of weeks.

MELISSA: Do you think your energy will be back by next week? We should go on an adventure.

KEVIN: I don't know. Where do you want to go? To the exciting library? Or the cemetery?

MELISSA: No, it'll be fun, I promise. And no adventures about death. Listen, I didn't tell you this before because I had to make sure I could trust you. You see, I'm actually a superhero. I only recently discovered my superpowers. I have to fight all types of threats like mutant organisms, bizarre creatures, and monsters. I thought I might need a new sidekick.

KEVIN: Sidekick? Don't think so. I already am a superhero. How about equal partner?

MELISSA: Deal.

KEVIN: I'll try to recruit the doctors and nurses to join us. They can be our sidekicks. They have superpowers, too, just not as strong as ours.

MELISSA: Well, they are adults. (pause) I'll see you next week. (MELISSA starts to leave.) Oh, and Kevin, don't forget to wear your tights.

KEVIN: Tights?

MELISSA: You can't be a superhero without them . . . Boys.
```

---

## IC-0824: Labor Day

- Title: Labor Day
- Author (byline): Milan Stitt
- Work: More One-Act Plays for Acting Students
- Publisher: Meriwether Publishing
- Publication date as stated: July 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DANIEL, THEA'S VOICE, THEA
- Teaser before the introduction: No
- Spoken words (computed): 1124
- Already set (do not supply): none

### Source block (context only)

```text
Author: Milan Stitt
Book: More One-Act Plays for Acting Students
ISBN: 1566080878
Publisher: Meriwether Publishing
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
DANIEL: Have you ever felt like you’re being watched?

THEA: Have you ever stood and just watched someone?

DANIEL: You don’t know who, you don’t know where. But you know they’re watching.

THEA: You watch and you wonder what’s going on in his life.

BOTH: (Overlapping) it feels really / you feel sort of…(together) Strange.

DANIEL: “Labor Day”

THEA: By Milan Stitt
```

### Performance text (classify this)

```text
(The pay phone at the corner begins to ring. DANIEL is uncertain what to do about the ringing. It’s insistent.)

DANIEL: You've got a wrong number. This is a pay phone. (There s no response.) Hello? Can you hear me? (He hangs up, returns to bus stop, looks for a bus to arrive. The phone starts ringing again. He tries to ignore it ... but can't.) Listen, this is a pay phone. (He listens carefully. Is someone on the line?) Is someone there? If you're there, you got a wrong number.

THEA'S VOICE: Maybe not. (Lights come up on THEA, a striking woman. She’s on her 17th floor terrace, looking down at DANIEL through a high-powered telescope.)

DANIEL: What?

THEA: (Very judgmental) You sound OK. (Annoyed, DANIEL hangs up. THEA pushes the redial button on her portable phone. The pay phone rings and rings. Finally, DANIEL can't resist.)

DANIEL: Look. Whoever you are, I'm not interested.

THEA: It's going to be a long time before a bus comes. We could wait together.

DANIEL: Yeah? What are you waiting for?

THEA: The dark. To go to work. Whatever's left.

DANIEL: (About to hang up) Forget it. I don't pay for it. And I wish you'd stop ringing this

THEA: Sex is easy.

DANIEL: Is it?

THEA: Anyone can accomplish that. (Disappointed) I guess I knew you'd think that was it.

DANIEL: What am I supposed to think? Is this what you do here in what-do-ya-call-it?

THEA: Chelsea. (A moment) Understand, we're never going to meet. (A moment) So don't worry, OK? (He looks up the avenue for a bus.) The buses are on holiday schedule.

DANIEL: (Looking up at buildings) You can see me, can't you?

THEA: Does it make you nervous?

DANIEL: (It definitely does!) No. Where are you?

THEA: You'll never know, so you can say whatever you want.

DANIEL: I have nothing to say, lady.

THEA: (Disappointed) Oh, you look like the kind of person who never mind. Must be the distance. That's what I get for trying something different. (She hangs up. The more he thinks about it, the angrier he gets. He stares at phone, daring it to ring He looks up at buildings... points to phone ... waits. It rings. He s surprised ... hesitates ... then grabs it.)

DANIEL: I do have things to say. But not to you! (He hangs up, looks for bus, hut does not return to bus stop. He won't give her the satisfaction of looking up at buildings again. The phone rings. He picks it up. She hangs up. He yells at the building) That's very childish! (He stalks over to the bus stop. The phone rings. He won't answer it. It keeps ringing. He answers it.) I can't stand unanswered phones.

THEA: That's why I selected you.

DANIEL: Selected me?

THEA: It's been a long weekend. The usual mix-up ... and galleys(Corrects herself, lest he be able to identify her.) Some work that was supposed to be delivered never arrived.

DANIEL: Are you a writer?

THEA: Pardon?

DANIEL: Galleys. Aren't those what writers correct?

THEA: Do you want me to be a writer?

DANIEL: I don't care. Whatever.

THEA: (Annoyed) I'm not indiscriminate, you know? (A moment) You're the first one who looked ... worth it.

DANIEL: (A come-on) You like the way I look? (A moment) How long have you been at this?

THEA: Not long. (A moment) My son's starting at one of those generic universities. Ohio or Indiana. The ones with football. Something or other at Urbana.

DANIEL: Illinois.

THEA: I should know, shouldn't I? But once you put information in computers and these automatic dialers you forget it. (A moment) He left Thursday to avoid the traffic. (A moment) The Time's as empty as the city on these long weekends ... except for the sales. And I don't have time to go running around for bargains. I did the crossword for once. Why anyone would think it's amusing to know a five-letter word for an Egyptian goddess totally escapes me. The other excitement was running out of half and half. On the way back from Dagostino's, I copied the number of your phone down there.

DANIEL: Big cities are a bitch. You're pretty lonely, eh?

THEA: No. Realistic, and therefore bored. We're alone from the moment of conception. Except maybe twins ... but they're aberrations. Lonely is only possible if you think something else is possible; it isn't. We live by ourselves, with ourselves until the time runs out.

DANIEL: How often do the buses run here?

THEA: I don't use buses.

DANIEL: Neither do I. But I've seen three cabs all the way up from Center Street. And they were off duty.

THEA: You work in Wall Street?

DANIEL: (Echoing her) Do you want me to? (No response) I flew in yesterday. There's a conference tomorrow. I figured I could use the weekend here to catch up on paperwork.

THEA: Workaholic?

DANIEL: When there's no work, I don't call strangers to avoid an empty life.

THEA: But you're talking. (A moment) Is your life empty? (No response) You can say whatever you want. (No response) In a civilized world, there would be numbers to call for intelligent conversation on holidays.

DANIEL: You can call for sex.

THEA: But not for intellect. Do you call those numbers?

DANIEL: For sex?

THEA: I forgot. You don't have to.

DANIEL: Do you?

THEA: It's curious how in any conversation men turn so quickly to sex.

DANIEL: Faster than women?

THEA: Yes.

DANIEL: Talk. Let's see how long you can avoid it.

THEA: (After a moment) My life is not a vacuum. I don't have to fill it with sexual fantasies. (Sees that he is looking for bus.) And the only reason I happen to have a telescope to watch you being impatient is that I'm fascinated by celestial phenomena.

DANIEL: Voyeurism. Sex.

THEA: If it is, it's not particularly gratifying knowing what turns me on actually existed some billions of years ago and is just reaching me now.

DANIEL: Lacks immediacy?

THEA: Which I think is important to sex. So no, it's not voyeurism.

DANIEL: You're still talking about sex.

THEA: I'm answering your question ... about sex.

DANIEL: (A moment) I've never gotten the message of astronomy.

THEA: Have you looked?

DANIEL: I can't begin to understand it... and the scientists can't understand it. Black holes, time warps, exploding galaxies, why bother?

THEA: But that's the point.

DANIEL: Why add to the frustration?

THEA: Reality isn't frustration.

DANIEL: Must be different in Chelsea than in Stevensville.

THEA: Is that on the East Coast?

DANIEL: No. It's one of those generic places. Near Chicago.

THEA: (A moment) Looking at the stars ... it's addictive.

DANIEL: Addictions are escapes. Not reality.

THEA: No. It's wonderful. The stars ... they keep me in my place. Probably proves God is a man.

DANIEL: Does it?

THEA: What's left to me in an ever expanding universe is this small place. My small problems. Small responsibilities. I am not the center of the universe. I'm reminded that most of what is I cannot control or change. Nor does anyone expect me to. That's important to know. Essential. Therefore, addictive.

DANIEL: I get that when I'm at the lake.

THEA: I see. You limit your philosophical inquiries to two weeks a year.

DANIEL: (Enjoying the exchange) No, anytime I look out a window in my house. The lake never looks quite the same. I limit myself to that which I can touch ... maybe even understand. Outer space to reach inner space seems a convoluted trip to me. If not just an escape. Tranquility is what you do, not what you think. Easy things. Right here. Now. Golf when there's no one but me to leave tracks in the dew. Fishing for hours when you know the fish couldn't possibly be biting. Gathering driftwood that's too interesting to burn. Not talking, not thinking, just being.

THEA: (A moment) I'm not going to invite you up.

DANIEL: Sex, again?

THEA: Is that the only way people can wait together?

DANIEL: At least, it's waiting closer.

THEA: You're very glib, for a man who 'does,' rather than 'thinks.' Why is there always such a distance between what we want to be and what we are? I hoped that distance would diminish with time.

DANIEL: So did I. (A moment) But I'm not coming up. In an over populated world, non-involvement is a social necessity.

THEA: And that suits you? (Focusing telescope) You don't have a wedding ring.

DANIEL: You want me to say I'll come up. So you can say no. That's the game.

THEA: I don't play games. I can't anymore. A belated social retardation has set in. (Looking at sky) There are a couple of stars. It's almost dark enough.

DANIEL: You're that old? You need candlelight? Scarves over the lamps?

THEA: (After a moment) I wish it were as simple as you think.

DANIEL: Isn't it?

THEA: Not anymore. (She hangs up ... immediately regrets it, redials. He watches the phone ring for a moment, then returns to bus stop. The phone stops ringing. The light fades on THEA. He looks for a bus, returns to phone, looks up .., gestures for her to call. Lights come up on THEA who is now looking at the stars through the telescope. She can't see his gesture. Lights slowly fade to black.)
```

---

## IC-0825: Land of the Dead

- Title: Land of the Dead
- Author (byline): Neil LaBute
- Work: Wrecks and Other Plays
- Publisher: Faber and Faber
- Publication date as stated: July 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MAN, WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1293
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil LaBute
Book: Wrecks and Other Plays
ISBN: 978-0865479708
Publisher: Faber and Faber
Date (Month/Year): July 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: It’s early morning – September 11, 2001 – A few hours before the Twin Towers in New York were attacked by Islamist Extremists.

ACTOR: A few hours of “normal” – Well, not quite normal – thought we tried hard to convince ourselves that what we had planned for the day was no big deal

ACTRESS: A few hours before we found ourselves in

TOGETHER: The Land of the Dead by Neil LaBute
```

### Performance text (classify this)

```text
MAN: Wow. What a day I mean, what a day, right?

WOMAN: I'll never forget it .

MAN: You know, because, it's not ... that kinda thing doesn't just come around any ol' time of the week, thank God. Huh? That's one of those dates that gets in your head and stays there. Like, ahh ... ahh ...

Silence. Darkness. Lights up slowly on a MAN and a WOMAN.

WOMAN: I got up around three that morning, I remember that. Very clearly. It was dark out our window and I just couldn't sleep. Maybe three-thirty but no later than that. (Beat.) He was still snoring . . .

MAN: I was out cold. I mean, completely zonked. I'd been out with some of the guys I work with. We'd closed a big deal that afternoon and you gotta take a minute, pound the ol' fists on the chest a bit when something good happens, right? Anyway, I slept great . . .

WOMAN: I go to my purse and begin to count the money again. That's stupid to do, I know, I know that, I must've checked the thing, like, sixty times already. I count it out again. Should be four hundred dollars. In tens . . .

MAN: She made me go out to an ATM that night! She's sitting up when I get in, just after midnight, and she's just staring at me ... says I shouldn't have taken any money from there without telling her - I snagged a few bills out for the bar - and I need to go back out. So I empty my wallet, but it's no good. We’re fifty bucks short. Great. I'm looking at her face and I know not to argue. I just slip my jacket back on and head down to the corner.

WOMAN: I was waiting for him to get that money - I didn't care about his being out that night. Not like it was some big surprise - I just wanted the rest of the cash. I suppose we could've just written a check, but I wanted to pay it, bill by bill, putting it out there on the counter, so I'd remember. So I'd feel it. Feel something.

MAN: Normally I would go with her, no question. Seriously. We'd talked about it and I promised I would and so, yeah, under normal circumstances I totally would've been there. But the boss is all over me this morning, wants to go to breakfast, he's calling my cell by six o'clock - he's so happy with our closing that account - I have to go... anyhow, once I explain it, she completely understands ...

WOMAN: Typical, right? He leaves it up to me ... but what're you gonna do? He'd just sit there, anyway, reading People magazine and checking his watch, so forget it ... at that point we'd decided, we're doing it, might as well just get it done.

MAN: She leaves a little bit before me ... maybe ten minutes ahead. This peck on the cheek and she takes off. Leaves the stupid money on the table! So I'm running downstairs in my bare feet to catch her ... believe that?

WOMAN: He comes barreling down the stairs, yelling out my name. For a second... I thought he wanted to talk, change of heart. I can recall turning around, this huge smile on my face .... then I see the envelope in his hand.

I took the earliest appointment I could ... seven-thirty. I thought that was the best thing, you know, just get it over with. Only have to use up half a personal day that way. (Beat.)

MAN: Breakfast is pretty decent. I have ham on the bone, and some sorta eggs. The boss is droning on and on about production and output . . .

WOMAN: They call my name . .

MAN: Food's good but the guy is driving me nuts, talking loud and this little bit of jelly hanging on his bottom lip as he's yakking away. I mean, hell, I might as well have gone with her to the clinic... least I could've read a magazine or something.

WOMAN: I'm perched on the edge of the table with that kind of crinkly paper under me ... and the nurse is saying something. I remember quite clearly: She said, "I love your hair." Then later, "There'll be some slight discomfort." (Beat.)

MAN: No, I'm pro-choice, I am ... she can choose to keep the kid, or she can choose to keep me. It's entirely up to her! (Laughs.) That's a joke, actually. (Beat.) But seriously, think about it . . . You do it, it happens, it's over. I've heard that it doesn't hurt that much at least no more than a pretty good paper cut. Now, I know, I know, there's a whole "psychological" thing going on, I know that. But come on ... we're still talking about, in essence, a paper cut!

WOMAN: And I don't really feel anything afterward. Nothing ... (Beat.) Someone comes in to check on me, so I get my things together and go up to the front to pay. At the last moment-I mean, I even reached out and snatched back the envelope-I decide to pay by credit card instead, which somehow seems, I don't know, appropriate.

MAN: Besides, we're sending it to a better place, right? Better than this world, anyways ... Or maybe not. Maybe it is wrong, hell, I don't know... Not that I wouldn't've taken care of it. No, seriously! I can see myself buying toys, changing diapers, stuff like that ... (Beat.) Of course, all that's easier to say knowing that the little bundle's safely in some incinerator somewhere. (Beat.) Anyway, I leave her a message on my way to the office ...

WOMAN: I stop on the street and listen to him. And as he speaks, he just casually tosses this in: "I tried phoning you earlier, but I couldn't get through ... "

MAN: I tried a couple times before I ate, I really did ... but she's always switching the power thing off on the side there. Drives me nuts!

WOMAN: He says, "Cause I was gonna say, I mean, if you wanna, we can go ahead and just keep the thing. Up to you." (Beat.) I stand there for a minute, supporting myself against the metal doorjamb. And then I say out loud, "Too late ... it's too late. I already did it ... " And I'm okay, it's ... it's no problem. The only ... I shouldn't even bring this up, but ... (Beat.) I keep hearing that sound. That buzzing, you know, from the ... I'm still aware of it. (Listens.)

MAN: Anyhow, I get upstairs, over to my cubicle, and just kick back for a second. Look out at the city. Up here, in these cloud-capped towers, all your worries and fears and just, you know, bad stuff ... melts into air, into thin air. The sky's clear as anything. All blue. Makes you feel, I dunno ... alive, I guess ... For a moment, the earsplitting sound of Jet aircraft. Deafening. The light over the MAN slowly goes out. The WOMAN removes a cell phone from her purse.

WOMAN: I kept trying his phone after . . . ringing it, just ringing it and hoping that he'd pick up. For a few days, actually ... but he didn't. He never did ... (Beat.) I still have that message he left me, the one about not going through with it, about keeping the ... I play it at night sometimes, when I'm lying there, missing him. Both of them. She presses a button and holds the phone to her ear.

MAN: (off-stage) "Hey, it's me - breakfast was okay, not bad. Anyway, I tried you earlier, but, listen… I was gonna say, I mean, if you wanna, we can go ahead and just keep the thing. Up to you. Or whatever... 'Kay. Buzz me later. Love ya."

WOMAN: It's funny, the stuff you remember. Well, not funny, but, you know. Yeah ... (Listens.) There's that buzzing again - is that my phone, or...? Do you hear that? Do you? Listen ... She checks her cell phone again, then looks around, searching. Silence. Darkness.
```

---

## IC-0826: Ledge

- Title: Ledge
- Author (byline): William Borden
- Work: More One-Act Plays for Acting Students
- Publisher: Meriwether Publishing
- Publication date as stated: July 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TOM, MARY, TOM AND MARY
- Teaser before the introduction: No
- Spoken words (computed): 885
- Already set (do not supply): none

### Source block (context only)

```text
Author: William Borden
Book: More One-Act Plays for Acting Students
ISBN: 1566080878
Publisher: Meriwether Publishing
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
TOM: People are always talking about living life on the edge.

MARY: I don’t think they ever really meant what they said but…

BOTH: I’m a literal thinker.

TOM: And the closest thing to the edge is the…

MARY: “Ledge” by William Borden.
```

### Performance text (classify this)

```text
(Lights come up to reveal MARY standing on the ledge of a building, her back pressed against the building, looking straight ahead, and inching away from an open window. She thinks for a moment. Then she starts to inch back toward the window -just as TOM climbs out of the window onto the ledge.)

TOM: This is my ledge.

MARY: I was here first.

TOM: I suppose you made a reservation.

MARY: If you're going to jump, jump.

TOM: Of course I'm going to jump! (Several beats) You were here first.

MARY: Go ahead.

TOM: You go.

MARY: No, you go.

TOM: You.

MARY: Jump!

TOM: All right. (He adjusts his position. He readjusts.) You're crowding me.

MARY: I'm sorry!

TOM: Could you ... (She edges away, giving him room. She slips. He grabs her.)

MARY: Thanks. (He readies himself He stops.)

TOM: How's it going to look?

MARY: Messy.

TOM: My going first. Who'll pay attention to me, with you still up here, making a spectacle of yourself? They'll just step over me - what's left of me - and they'll be shining spotlights on you and sending reporters out to interview you and I'll be lucky to be a sidebar on the comics page, which is the story of my life. So go on. (She looks down. Cars honk.) You climbed out here. (She gathers her courage.) You made a decision. (She readies herself) You knew there was no reason to put up with it any longer. (She’s ready.) Stop! (She stops.) You jump first, who'll pay any attention to me, up here, a speck on the forty-first floor? You'll get all the attention, as usual.

MARY: As usual?

TOM: You women. You're always getting the attention. With your legs. Your breasts. Your emotions. Get off.

MARY: Off?

TOM: Through the window.

MARY: You're between me and the window.

TOM: There must be another window around the corner.

MARY: I might fall.

TOM: All right then, jump. I'll wait until they've scraped you up and carried you away in a shoebox, then I'll call attention to myself. Go on, go on, get it over with.

MARY: I'll jump when I'm good and ready.

TOM: Jump!

MARY: No! (Tom pulls out a gun and aims it at her.) Shoot. (Tom smiles, puts away the gun.)

TOM: You women think you're so clever, so damned clever! Tom Longmyer, murderer? No, no. You can borrow it, if you like.

MARY: Why would I want your gun?

TOM: You could make sure that way.

MARY: Forty-one stories is sure.

TOM: I was going to use the revolver, but ...

MARY: What?

TOM: I was afraid nobody would notice. A shot, drowned out by the bedlam of the city. Shots all the time! Gang warfare, drug dealers. Buses make a lot of noise, too. You can't hear yourself think.

MARY: I've never heard myself think. I mean, you think very quietly, really. Silently, in fact. Don't you?

TOM: It's just an expression!

MARY: But words should mean something. Don't you think?

TOM: (He pulls the gun again.) Get off my ledge.

MARY: You are so insignificant.

TOM: Don't say that to me.

MARY: Nothing. An absence.

TOM: Don't say that to me!

MARY: Who will miss you? (He begins to cry. She watches him coldly for a moment.) I'm sorry. (He bawls.) I'm sorry! (He wails.) I'm sorry, Tom! (He stops abruptly, smiles.) Give me the gun. (He hands her the gun.)

TOM: Be careful. The safety's on.

MARY: How do you turn it off? (He switches off the safety.)

TOM: In the mouth. Blows the brains right out. The temple - the bullet can ricochet off the inside of your skull, leave you a semiconscious vegetable for the rest of your life. (She aims the revolver at him.) What are you doing?

MARY: You manipulated me.

TOM: You shoot me, they'll send you to the chair.

MARY: I don't care.

TOM: You wouldn't dare.

MARY: Wouldn't I?

TOM: You women

MARY: You men.

TOM: - Always flaunting yourselves

MARY: You're all the same!

TOM: All you want is a love slave!

MARY: Manipulator!

TOM: Show-off! (She pulls the trigger. The hammer clicks. She pulls it several more times.)

TOM: I didn't have the guts.

MARY: You're a zero.

TOM: I'm not worth your pity.

MARY: You're disgusting!

TOM: I'm not even that significant.

MARY: Get off my ledge!

TOM: My ledge!

MARY: Mine!

TOM: Mineminemineminemine!

MARY: You're so juvenile. (She tries to edge around him, to get to the window.)

TOM: What are you doing?

MARY: You've spoiled it.

TOM: Be careful. You might fall.

MARY: Fat lot you care, Tom Longmyer.

TOM: But aren't you going to ...?

MARY: I don't have to put up with you on the day I'm going to die. I can at least have some privacy. Some quality time to myself as I prepare to ... you know. (She can't get around him.) You climb around me.

TOM: You climb around me.

MARY: Come on, I'm getting cold.

TOM: I might fall.

MARY: Climb around me or I'll push you off. (He tries, he loses hisbalance, she pulls him back. They're belly to belly, face to face. He flings himself back to the building, where he was before, between her and the window.) You're just like my father! Cowardly, weak, ineffectual!

TOM: If you're so effectual, be my guest. (He motions her to climb around him.)

MARY: It's too windy.

TOM: You are so effectual. (She flings herself before him, grabbing at the building. He holds her.)

MARY: Let go. (He lets go. She starts to fall. He grabs her. They're both precarious.)

TOM: You hold onto the building, I'll hold onto you. (They do. Several beats) I've never been this close to a woman before. Without kissing her.

MARY: Kiss me and I'll jump and take you with me.

TOM: You had coffee for breakfast.

MARY: Do I have bad breath? I have mints somewhere ... (She reaches for her mints, teeters, he hauls her in, their lips brush.)

TOM: I didn't kiss you! It was an accident! Just a brush ... of lips...hardly noticeable... like me ...

MARY: You should have shaved. Your death day, the least you could have done

TOM: Who's going to tell, me smeared on the boulevard like sauce on a pizza?

MARY: If you took a little pride in yourself...

TOM: ... I wouldn't be here. (Several beats)

MARY: Tom ...

TOM: I don't even know your name.

MARY: Mary. Tom ...

TOM: Mary what?

MARY: Mary Freestone. Tom ... (He kisses her - a long kiss. She kisses him - tenderly, for a long time. They catch their breaths.) You're excited.

TOM: I know.

MARY: Well stop it. (Several beats)

TOM: I can't. (Several beats) Mary?

MARY: What?

TOM: I don't want to die.

MARY: You should have planned ahead a little better.

TOM: Do you?

MARY: I don't care.

TOM: Well, then you should move, so if one of us falls, it's you.

MARY: I mean, I don't care if you die. I care if I die.

TOM: I'm losing my erection.

MARY: That gives us more room.

TOM: Mary? I want you to live, too.

MARY: That's nice. (She succeeds in getting around him. She inches toward the window.)

TOM: Don't leave me! Mary!

MARY: Don't be a crybaby.

TOM: (Crying) I don't want to die.

MARY: Why did you come out here if you don't want to die?!

TOM: I hadn't met you.

MARY: You're trying to manipulate me.

TOM: If that's true, I'll kill myself! (She waits.) You want me to jump, just for a tiny manipulation? (She waits. He starts to jump.)

MARY: Give me your hand.

TOM: You don't think I have the integrity to jump? (He really starts to jump.)

MARY: Just give me your hand. (He clutches her hand. They edge to the window. The window, which is barred, falls shut.)

TOM: What is it?

MARY: The window fell shut.

TOM: Open it.

MARY: It locks automatically. (They look at each other.)

TOM AND MARY: Help!
```

---

## IC-0827: The Legend of Spud Murphy

- Title: The Legend of Spud Murphy
- Author (byline): Eoin Colfer
- Work: Not specified
- Publisher: Miramax Books
- Publication date as stated: Sept 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 2, DAD, WILL, MARTY, MOM, DONNIE, HP, BERT, LITTLE BOY, SPUD MURPHY
- Teaser before the introduction: Yes
- Spoken words (computed): 994
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eion Colfer
ISBN: 978-0786855018
Publisher: Miramax Books
Date (Month/Year): Sept 2004
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: The name Spud Murphy strikes fear into the hearts of children everywhere.

ACTOR 2: Grown-ups think she’s a kindly old librarian, but kids know the truth.

ACTOR 1: They’ve heard all about the gas-powered spud gun she keeps hidden under her desk.

ACTOR 2: Make so much as a sound in Spud’s library, and you could get spudded with soggy potatoes.

ACTOR 2: Laugh out loud, and you may never be seen again.

TOGETHER: The Legend of Spud Murphy by Eoin Colfer
```

### Performance text (classify this)

```text
Suggested Roles: ACTOR 1: Dad, Will, Spud Murphy, HP

ACTOR 2: Marty, Mom, Little Boy, Donnie, Bert

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

(Will and Marty are rough housing, loudly playing pirates or cowboys or superheroes in an improv format until DAD puts a stop to it)

DAD: (Chapter 1) This is a madhouse.

WILL: And he’s the chief lunatic. (pointing at Marty)

MARTY: I’m not the one talking to dolls!

WILL: Action Man is not a doll.

DAD: (through gritted teeth) Quiet! There must be something we can find for you to do during the summer. Something to get you out of the house.

MOM: What about the library? (Will and/or Marty horrified expression)

DAD: Reading! It’s perfect. How can you cause trouble reading a book?

MOM: Yes, of course, it’s educational too.

MARTY: Don’t make us join the library. It’s too dangerous!

DAD: Dangerous? How could a library be dangerous?

MARTY: (whispering) It’s not the library. It’s the librarian.

MOM: Mrs. Murphy? She’s a lovely old lady.

WILL: She’s not a lovely old lady. She hates kids and she used to be a spy in the army. Tracking kids from enemy countries!

MOM: I’ve heard enough. You two are going to the library for the afternoon and that’s it. We’ll make sandwiches.

WILL: (to audience) Sandwiches wouldn’t be much use against Spud Murphy and her gas-powered spud gun. (Chapter 2) Of course our little brothers thought this was hilarious. (Chapter 1) Having one little brother is bad enough but having three? The trouble with little brothers is that they are never blamed for anything. All Donnie, Bert and HP have to do is bat their blue eyes and let their bottom lips wobble a bit and they are forgiven for everything.

DONNIE: (batting his eyes) Nice knowing you!

HP: (with a lisp) Yeth, Nithe knowing you.

BERT: (with a wobbly bottom lip) Can I have your Walkman?

WILL: Do you hear them, Mom? They’re teasing us already!

MOM: Oh, they don’t mean it. My babies!

WILL: Mom gave them a gummi bear each and I thought that my head would pop with the unfairness of it all. (Chapter 2) [Later that day] Mom dropped us at the library on her way downtown.

MOM: Okay, off you go, up the steps. I’ll just stay here to make sure you go inside.

WILL: (growling quietly as the boys exit the car) (to audience) I bet you’re thinking we were a pair of gutless chickens. But that’s because you think libraries are happy colorful places, where the librarians actually like children. That may be what most of them are like, but this one was different.

LITTLE BOY: (running from the library in tears) Don’t go in there! Don’t do it! I was one day late with Five Go to Smuggler’s Top. Just one day. And look what she did to me! (he runs away)

WILL: And just like that, the boy was gone, with only a puddle of tears to prove he had ever been there. We stayed there until Mom came up the steps. We had no choice but to go inside. (The boys enter the library and look around in fear) The library seemed to go on forever. Row after row of wooden bookshelves.

SPUD MURPHY: (behind the desk, she spoke with a voice like two pieces of rusted metal being rubbed together) What do you want? (Will and Marty quake with fear) I said, what do you want? (stamping a book vigorously with an ink stamp)(the boys approach the desk cautiously)

WILL: (to audience) Spud Murphy was big. Taller than my dad, and wider than Mom and my two aunties strapped together. (squeaking) Mom says we have to join the library.

SPUD MURPHY: Name?

WILL: M – M – Mrs. Murphy?

SPUD MURPHY: (Sighing) Not my name, dummy. Your names.

WILL: (shouting like an army cadet) William and Martin Woodman! (to audience) We surrendered our name and our address was next. Now Spud knew where we lived.

SPUD MURPHY: (fills in the library cards) Pink cards (handing them to the boys) Pink means you stay in the Junior section. (she leads them to a small section of the library . . . pointing) That is the Junior Section.

WILL: A single bookshelf with four rows of books. On the ground -- a small patch of carpet.

SPUD MURPHY: Do not set foot off that carpet until you leave. Whatever boyish idea enters your head, ignore it. Stay on the carpet or there will be trouble. (she bends over until her eyes are level with the boys) Is that understood? (she returns to her desk)

MARTY: (in library voices) (Chapter 3) What exactly did she mean? [Does] trouble mean a strict talking-to? Or [does] trouble mean being suspended by your fingernails over a pit of alligators? I need to know how much I can get away with!

WILL: I don’t need to know. I’ll just sit here and pretend to read.

MARTY: No wonder Action Man is your only friend. I am an actual hero type. I am prepared to take risks! (Marty checks to see if Spud can see him) She can’t even see us. We can do whatever we want!

WILL: What are you going to do?

MARTY: I’m going to switch a few books. The best way to mess with a librarian is too put things back in the wrong place. By the time she finds out, we’ll be home watching cartoons. (Marty sneaks off the carpet and begins switching books)

WILL: (to audience) He switched almost every single book in the section. Mysteries with romance, adventure with bird-watching! Suddenly a shadow fell across my brother. (Spud Murphy looms behind Marty) It was Spud.

SPUD MURPHY: I knew it! (Marty squeaks like a kitten) I can always tell a troublemaker. I took one look at you Martin Woodman and I knew you’d be off that carpet before I was back at my desk.

MARTY: I’m sorry, Spu – Mrs. Murphy. I’ll never leave the carpet again.

SPUD MURPHY: Too late for that. Since you’re already off the carpet, you can fix the damage you’ve done, and maybe I won’t tell your mother how you set off the fire alarms.

MARTY: But . . . I didn’t!

SPUD MURPHY: I know you didn’t. And I’m sure your mother will believe that. Unless, of course, you’ve been in trouble before.

WILL: (to audience) He’d met his match. Two hours and fourteen paper cuts later, Mom was outside, waiting in the car. We were almost safe . . .

MARTY: That wasn’t so bad. I’ve had teachers meaner than her! (Marty stops at the exit and turns to make a beeline for Spud’s desk) Excuse me, Mrs. Murphy. You wouldn’t really say I set off the alarms, would you?

SPUD MURPHY: Oh, wouldn’t I? (She opens her desk and speaks sweetly) (Pg 84) Stand in front of my desk. I have something for you. (Chapter 3)

WILL: (Pg 85) Oh no! The gas-powered spud gun!

SPUD MURPHY: You’re going to get what you deserve. Go on, in front of my desk. (Chapter 3) I have a collection of stamps here. One came in last week you might like. It’s in the shape of a pirate flag. A lot of the boys like me to stamp it onto their forearms, like a temporary tattoo. . . But maybe you’re too young.

MARTY: No, I’d love that (already rolling up his sleeve) Wait until the guys at the swimming pool see this!

SPUD MURPHY: Are you sure, Martin? (Spud inks the stamp) This won’t wash off for a couple of weeks.

MARTY: I’m sure. Stamp away.

SPUD MURPHY: (smiling widely) Okay then. Keep still. (she rolls the stamp on Marty forearm)

MARTY: (leaning over to read it, he wails) I LOVE BARBIE!

SPUD MURPHY: Oops. Wrong stamp. Sorry about that. (a glare) One more thing. Any more of your little games and I get nasty. There are worse things in this desk than rubber stamps.

(she brings out her potato shooter and cocks it with a hiss) Enjoy swimming (she laughs as the boys run for the door)
```

---

## IC-0828: The Lemonade Stand

- Title: The Lemonade Stand
- Author (byline): Bryan P. Harnetiaux
- Work: More One-Act Plays for Acting Students, Pg 53-60
- Publisher: Meriwether Publishing
- Publication date as stated: July 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MAN, WOMAN
- Teaser before the introduction: No
- Spoken words (computed): 1047
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bryan P. Harnetiaux
Book: More One-Act Plays for Acting Students, Pg 53-60
ISBN: 978-1566080873
Publisher: Meriwether Publishing
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
MAN: Those who have

WOMAN: and those who have not.

MAN: Those who want

WOMAN: and those who want not.

BOTH: Those who give

MAN: out of wealth.

WOMAN: and out of poverty.

MAN: “Lemonade Stand”

WOMAN: By Bryan P. Harnetiaux
```

### Performance text (classify this)

```text
MAN: (Pg 53-60) (He enters preoccupied with a piece of paper and then discovers the lemonade stand.) Hello. (The WOMAN, sitting behind the stand, smiles.) Hot today, a scorcher.

WOMAN: Yes. It is.

MAN: Unseasonably hot. (Explaining) Unusual for this time of year.

WOMAN: You're right, there. It'll go, sooner or later.

MAN: Yeah. Say, would you know where Oliveras Street is? (Handing her piece of paper) What, twenty one hundred block... There's a house for sale tomorrow; and I wanted to take a look at the property.

WOMAN: No.

MAN: It can't be far. Just a general direction would help.

WOMAN: (Indicates vaguely.) Somewhere over that way. I don't know. Why do you want that property; property like that?

MAN: What?

WOMAN: You wanna buy property around here?

MAN: Yes.

WOMAN: Why?

MAN: Why not? Investment. You gotta find it; it rarely finds you.

WOMAN: Bad investment around here. I wouldn't.

MAN: You wouldn't?

WOMAN: Maybe somebody's trying to take you.

MAN: Maybe. I'll keep an eye out.

WOMAN: Who's selling? The property. Maybe I know them.

MAN: A bank. It's a foreclosure.

WOMAN: Oh.

MAN: Business. What makes the world go round. Selling lemonade, huh?

WOMAN: Yes.

MAN: One of those things that just sells itself.

WOMAN: Yes, it does.

MAN: Boy takes me back. (Wiping face with handkerchief) Benny LaRuso and me. Our secret was mobility. Had our stand built right on top of my Red Rider wagon. We'd cover forty blocks on a hot afternoon. Long time ago. Well, is it any good?

WOMAN: I think so.

MAN: It's the stuff to have when it's thirsty out, that's for sure. This your regular corner?

WOMAN: No. I don't have a regular corner.

MAN: S ome say you need a regular corner to build up clientele, customers. Not necessary. We did just fine. It's the product that counts - and somebody with a need. Gotta have that. You move around, then?

WOMAN: Huh?

MAN: To different locations. You move around?

WOMAN: I did this today. Just today.

MAN: Trying to get movie money, huh?

WOMAN: Yeah. Movie money.

MAN: A little slow today.

WOMAN: It's been pretty busy. Slow right now. (Looking in pitcher) I've only got about one glass left.

MAN: That's good. Very good. (Takes out coin purse.) Well, why don't I take the last glass? Then you'll have it licked.

WOMAN: If you want.

MAN: If I want? (Chuckles.) It'd be kinda fun. It's been a while I since I had any. How much?

WOMAN: Seven thousand.

MAN: (Fishing for change) Pardon?

WOMAN: Seven thousand dollars.

MAN: (Has a good laugh; WOMAN joins in.) No. Really... (Succumbs to laughter again.) That's good. In business, you get the customer laughing, you get the business. So, what's it go for these days?

WOMAN: This goes for seven thousand.

MAN: T hat's ridiculous. Nobody in their right mind is going to pay seven thousand for a glass of lemonade.

WOMAN: Maybe. It's my lemonade.

MAN: (Laughing again, although with a different quality, as he starts to leave) Seven thousand ... (Coming back) Are you trying to make a fool out of me? Seven thousand! (Picks up a jar of pennies and shakes it.) What are these?!

WOMAN: They're pennies.

MAN: I know they're pennies! You got them selling lemonade.

WOMAN: Those were other glasses and other people. You are you, and this is my last glass.

MAN: Ah, you admit you sold it for pennies.

WOMAN: That's all they had.

MAN: So that's it. You see me as some mark who'd pay seven thousand dollars for a lousy glass of lemonade.

WOMAN: It's not lousy. It's exceptional lemonade. This is all that's left. If you want it, buy it.

MAN: For seven thousand dollars. I could buy a house in this neighborhood for that. A carload of lemons wouldn't cost that much. What am I doing here? You're not serious; you can't be serious... (He laughs.) Alright, I'll give you a buck for it - for entertainment value. (Hands her a dollar. She does not take it. Instead she tears a blank sheet of paper out of an old notebook - or perhaps some excess butcher paper off the corner of the stand and hands it to the man.) What's this?

WOMAN: An application.

MAN: What application? It's a blank piece of paper.

WOMAN: Just put all you own on the left side and all you owe on the right. Add it up and turn it in here.

MAN: You want a net worth statement?

WOMAN: If you don't wanna pay my price, you have ta fill it out.

MAN: Why?

WOMAN: To see if you qualify - for the lower price.

MAN: Which is?

WOMAN: Three cents.

MAN: I offered you a dollar.

WOMAN: My price isn't a dollar. It's seven thousand, unless you qualify.

MAN: I have no intention of qualifying, and I am not paying seven thousand.

WOMAN: Good-bye.

MAN: (Starts to say something, but stops.) Good-bye. (Starts to leave.)

WOMAN: Could I have my form back?

MAN: (Returning) Yes, you can have your form back! (Shoves it at her.) What is so special about this lemonade?!

WOMAN: It's my last glass.

MAN: You can make more.

WOMAN: Not like this. There's no more like this.

MAN: You said that. That doesn't tell me anything. What it tastes like, what it's made of, why you wanna charge me seven thousand dollars for it? You want me to spend that kind of money, I don't even know what it tastes like. (WOMAN ladles out a small amount of lemonade and hands MAN the stirring spoon.) What's this cost?

WOMAN: Nothing. (MAN drinks the sample.)

MAN: My God. That's good. That's quite good. Where'd you get this stuff?

WOMAN: I made it myself, from scratch. I told you it was I exceptional.

MAN: Real lemons, right? Big as footballs. Benny and I got ours from the corner market. Big as footballs. He was fun, but couldn't sell anything to save his life. He pulled the wagon, I sold the lemonade. Nice guy, kid. There's something else in this. What is it?

WOMAN: You wanna buy it or not?

MAN: Not at your price. Hey, I'm trying to be fair. I don't have to be here at all.

WOMAN: You were lost and thirsty as I remember. It had nothing to do with bein' fair.

MAN: Where do you get off talking to a customer that way. I'm not robbing you. (Going to his wallet, he sets ten dollars on the counter.) I'll give you ten dollars, that's it. (WOMAN shakes her head.) You need it and you know it.

WOMAN: I close in a couple of minutes.

MAN: I want that lemonade!

WOMAN: That's my price.

MAN: S uch principles. You can't eat principles. You can't sleep under principles. You can't keep warm with principles. (Once again to his wallet, peels off cash and sets it on the counter.) One hundred dollars. I don't know why I'm doing it, but there it is. Go ahead. When's the last time you saw a hundred dollars for a glass of lemonade? When's the last time you saw a hundred dollars? Go on, pick it up. (WOMAN stares at the bills. Slowly, a drool of spit drops from her lips onto the money.) Why you... worthless piece of ... garbage. I tried to help you.

WOMAN: On your terms. At your convenience. For your entertainment. You tried nothing. Nothing.

MAN: Seven-thousand-dollar lemonade. I'm talking to a nut. What looney farm did you escape from? The world doesn't work this way! (During the following, MAN kicks at one of the corners of the lemonade stand for emphasis and it collapses. Seeing this, he is at first startled but then continues to lay it to ruins. During this, WOMAN grabs the pitcher and clutches it.) You don't set up some flimsy stand and ask for the sky. Nobody owes nobody the sky. And you haven't the decency to go crazy somewhere else, away from those of us who are trying like hell to be reasonable! (He stops; the stand is in shambles.) Didn't mean to ...

WOMAN: Yes, I know...

MAN: Take this. For the stand. (He goes to hand her the money. She does not take it, so he sets it down and starts to go.) I'm sorry. (Pause) You ask too much.

WOMAN: You give too little.

MAN: What was in the lemonade?

WOMAN: Tears. (MAN exits as he came. WOMAN then exits in direction of Oliveras Street.)
```

---

## IC-0829: Let’s Pretend this Never Happened

- Title: Let’s Pretend this Never Happened
- Author (byline): Jenny Lawson
- Work: Not specified
- Publisher: Berkley Trade
- Publication date as stated: March 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ME, VICTOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1811
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jenny Lawson
ISBN: 978-0425261019
Publisher: Berkley Trade
Date (Month/Year): March 2013
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Do you know your significant other? I mean, do you really, truly, know who they are as a person?

ACTRESS: For example, when couples get really busy, they can go days without asking any questions beyond logistics-type questions.

ACTOR: They see each other at the end of the day and ask “How was your day?” and they go through what happened.

ACTRESS: They get so wrapped up in the day-to-day – the ‘how are you?’ that they rarely get to the ‘who are you?’

ACTOR: But never fear . . . you can have deep, [air quotes] meaningful ‘who are you’ conversations with your significant other. Just like Jenny and Victor in . . .

ACTRESS: Let’s Pretend this Never Happened

ACTOR: by Jenny Lawson
```

### Performance text (classify this)

```text
Phone Conversation I Had with My Husband After I Got Lost for the Eighty Thousandth Time

ME: (Pg 140-145) Hello?

VICTOR: Where are you?! You’ve been gone an hour.

ME: I’m lost. Don’t yell at me.

VICTOR: You went to get milk, dude. You’ve been to that store a hundred times.

ME: Yes, but not at night. Everything looks all strange and I couldn’t see the signs. And I guess I must’ve taken a wrong street and I’ve been driving aimlessly, hoping for something to look familiar.

VICTOR: How can you get lost every time you leave the house?

ME: I don’t even think I’m in Texas anymore.

VICTOR: [You have got to be kidding me!] —

ME: DON’T YELL AT ME.

VICTOR: I’m not yelling at you. Just turn on the GPS and put in our address.

ME: I left it at home.

VICTOR: WHAT IS WRONG WITH YOU?!

ME: You said you wouldn’t yell at me!

VICTOR: That was before you left the GPS at home. I BOUGHT IT EXPRESSLY BECAUSE OF YOU.

ME: Can’t you just tell me how to get home?

VICTOR: How am I supposed to help you get home, Jenny? I DON’T KNOW WHERE YOU ARE.

ME: Okay . . . there are a lot of trees. And bushes. Or they might be horses. It’s too dark to tell.

VICTOR: Oh, yeah, I know exactly where you are.

ME: Really?

VICTOR: No. You’re someplace where there may or may not be bushes. How is that helpful?

ME: I need to find a street sign.

VICTOR: You NEED to remember to put the GPS in your car.

ME: No. I’m not using it anymore.

VICTOR: Why not?!

ME: It’s trying to kill me.

VICTOR: [stunned silence]

ME: Remember last week when I had to go into town and I got the driving instructions from MapQuest and you made me take the GPS as a backup, but then halfway there the GPS is all, “Turn left now,” and I’m all, “No. MapQuest says to go straight,” and it’s like, “TURN LEFT NOW,” and I’m all, “No way.” and then she’s sighing at me like she’s frustrated and she keeps saying, “Recalculating,” in this really judgy, condescending way, and then she’s all, “TURN LEFT NOW!” And I’m all freaked out, so I turn left exactly like she says and then she’s all, “Recalculating. Recalculating,” and I’m like, “I DID EXACTLY WHAT YOU SAID TO DO. WHAT’S WITH THE TONE?”

VICTOR: You’re not using the GPS because you don’t appreciate the tone of the robot?

ME: No, that’s just the start . . . .

VICTOR: You still haven’t seen a street sign?

ME: Oh. Sorry. I kind of forgot I was driving.

VICTOR: You forgot you were driving while you were driving?

ME: It’s not like I ran into a cow. I just forgot I was looking for signs.

VICTOR: If you ever make it home I’m hiding your car keys.

ME: Anyway, that’s when I came up with what might be the greatest invention in the history of the world.

VICTOR: Street signs. Look for street signs.

ME: Haven’t seen any. Feels like I’m on a highway. Ask me what my great idea is.

VICTOR: No.

ME: GPS for stupid people.

VICTOR: [silence]

ME: I’m totally serious. Because I’m no good with directions, but I’m really good with landmarks, so if you tell me to go north on Main, I’m [lost], but if you say, “Turn at that Burger King that burned down last year,” I totally know what to do, so we should build a GPS system that does that.

VICTOR: [sigh]

ME: And here’s the genius part: We make it able to learn so it adapts to you personally. So, like, if I say, “Huh. There’s a homeless guy,” it’ll put that in its data banks, and then when I want to go somewhere later, instead of just naming random streets it’s all, “You know where that homeless guy was? We’re going there. Turn left at that Sonic you like. Turn right at the burrito place you took Sarah to.

VICTOR: What the [hell]?

ME: Exactly. See, there’d be a learning curve. We’d have to put that in the brochure. Like a disclaimer.

VICTOR: How long do you have to be missing before I can start dating again?

ME: I’m just saying [it] isn’t perfected yet, dude. It’s close, though. OHMYGOD, I TOTALLY KNOW WHERE I AM!

VICTOR: You’re at the burrito place you took Sarah to?

ME: No. I’m at that abandoned building that looks like it’s owned by Branch Davidians.

VICTOR: Huh. The rest of the world calls that “Dallas Street.” So can you get home now?

ME: I think so. Left at that spooky bar that looks like it’s out of Scooby-Doo, left at the place we saw that wild boar that turned out to be a dog, and right at the corner where I threw up that one time. Right?

VICTOR: You make my head hurt.

ME: DUDE, WE ARE GOING TO BE MILLIONAIRES. Hairless Rats: Free for Kids Only

ME: (Pg 282-286) This morning Victor and I stopped into the local gas station for coffee. On the way out we stopped in front of the public bulletin board. [There] were ads like: REGULAR SQUIRRELS—FREE TO GOOD HOME. NOT FOR EATING. RATS AND MICE CHEAP – LOCAL - CAN DELIVER 24 HRS. HAIRLESS RATS FREE FOR KIDS ONLY.

VICTOR: Wow. I don’t think I want to know of the situation you have to be in where you need a rat delivered so desperately that it can’t wait until morning.

ME: Ooh, I would.

VICTOR: Well, of course you would.

ME: Who wouldn’t want to know about an emergency rat situation where the emergency is that you NEED a rat. It’s like the exact opposite of every regular emergency rat situation ever. It sounds fascinating. We should call this guy just to see what his deal is. I bet he has great stories. I mean, who gives hairless rats to children? He’s like the bizarro-world Candy Man.

VICTOR: So call him. Pretend to apply for a free squirrel and see what his story is.

ME: I wonder what the application process is on that? It would be really depressing to get turned down for free squirrels.

VICTOR: True. “I’m sorry. We’re going to have to decline you. Your home isn’t even fit for squirrels.”

ME: Our home is pretty messy, but I think it’s at least fit for squirrels. I’d be like, “But our squirrels seem quite happy.” I’d totally appeal that ruling.

VICTOR: “I’m sorry, but your references didn’t check out.”

ME: “But our references were squirrels.”

VICTOR: “Right. And they’re not happy. Plus, there have been some reports of hate speech.”

ME: “What?”

VICTOR: “Last week you dropped a fork and yelled, ‘Rats.’ Then in January you complained that your computer wasn’t working properly and was acting ‘all squirrelly.’ We have people on the inside, you know.”

ME: “Hang on. Are those people the squirrels who live in my attic? Because they’re all high and they don’t know what they’re saying. Those squirrels are junkies and they are not to be trusted.”

VICTOR: “Ma’am, that was slander. You’ll be contacted by the squirrel civil liberties union for a statement. Plus, you need to stop referring to squirrels as ‘those people.’ Please get [it] together.”

ME: Wow. We sound . . . totally unfit to have squirrels. Now I don’t even want to call the guy, because I’m all nervous about being judged. I don’t even think I could pass the interview. [And] I can’t remember how we got to the point where I’m defending myself against the imaginary accusations of a man who gives hairless rats to neighborhood children, and who apparently trusts the nonexistent squirrel junkies in the attic.

VICTOR: True. I don’t remember ever having these conversations before we moved to the country.

ME: Me either. Also, I just realized that I just went to a gas station in my pajamas to buy coffee. I just became a giant warning sign to others.

VICTOR: What the hell happened to us? Thanks for the Zombies, Jesus -- Car conversation with Victor

ME: (Pg 164-168) Oh my God, did you see the name of that cemetery we just passed? “Resurrection Cemetery.” What a horrible name for a cemetery.

VICTOR: It’s because they believe in the resurrection of believers.

ME: Still. Some things just shouldn’t be resurrected. Just what we need is a bunch of zombies wandering the earth.

VICTOR: That’s not “resurrection.” That’s “reanimation.”

ME: Same difference. Although I guess “Reanimation Cemetery” would sound way more creepy.

VICTOR: It’s not the same difference. Zombies are reanimated, but they don’t have their previous mental capacity. Technically that’s a “zombification.”

ME: Well, if you want to get all technical, then how about vampires?

VICTOR: Um . . . they’re fine?

ME: What I mean is, vampires have their “previous mental capacity,” thus by your logic they are “resurrected.” Might as well name it “Jesus-Is- Bringing-You-Vampires Cemetery.”

VICTOR: No. That’s not the same thing, because when you resurrect someone from the grave they aren’t undead.

ME: No, they are TOTALLY undead. That’s like the very definition of the undead.

VICTOR: No. A vampire is undead. The resurrected aren’t undead.

ME: I think you don’t know what “undead” means.

VICTOR: I THINK YOU DON’T KNOW WHAT “UNDEAD” MEANS!

ME: Oh my God, calm down, Darwin. Don’t get all crazy just ’cause I threw a vampire monkey wrench in your faulty Jesus-zombie logic.

VICTOR: [glower] . . . [Long angry silence]

ME: So, I was talking to the organ donation lady at work the other day and she told me a secret way that you can’t not give away my organs.

VICTOR: You know what? I dare you to make less sense.

ME: Well, I know you’re anti–organ donation, and so I told her I was afraid that you wouldn’t let the doctor take my organs if I died first, but she said if I list my mom as my next of kin on my donor card then they won’t even ask you for your permission.

VICTOR: If you want to throw away all your organs I won’t stop you. Just don’t come complaining to me when I see you in the afterlife and you’re all, “Oh my God, I just peed all over myself because someone else has my bladder.”

ME: Fine. And if you die first I’m totally donating your organs too.

VICTOR: Like hell you are. I may need them.

ME: Why would you need them? YOU’RE DEAD.

VICTOR: What if I become a zombie? Huh, smart-ass? I’d be a pretty [crappy] zombie if they took my eyes out. I’d be biting poles and cats and . . .

ME: So you’re making a decision to not save someone’s life on the off chance that it might be inconvenient if you turn into a less efficient zombie?

VICTOR: It sounds stupid when you say it.

ME: Fine. I’ll just donate the parts that a zombie doesn’t need. Like your skin. Or your brain tissue.

VICTOR: Zombies need brains.

ME: No, zombies eat brains. Obviously you could donate your brain and still be a functional zombie.

VICTOR: Yeah, and then I’ve gotta spend eternity wandering the world as a mindless idiot.

ME: [snort]

VICTOR: Shut up. If zombie-me finds out I’ve got parts missing you will be the very first person I eat.

ME: I wonder if this is the weirdest fight we’ve ever had.

VICTOR: Not. Even. Close.
```

---

## IC-0830: Life Cycles

- Title: Life Cycles
- Author (byline): Joshua Sands
- Work: Turning Points
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JASON, KARA
- Teaser before the introduction: No
- Spoken words (computed): 1284
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joshua Sands
Book: Turning Points
Publisher: Tichenor Publishing
ISBN: 0742117014
Date: 2001
```

### Introduction (context only: never use it for content warnings)

```text
Growth occurs in cycles. The cycle of childhood, of puberty, of adulthood, of parenthood, of midlife, of retirement, of death. The trick to marriage is to find someone whose cycle matches your own. When two people’s life cycles are in sync, they are able to maintain a healthy relationship. When the cycles are out of sync, the relationship is doomed to cycle into failure. A relationship that exemplifies the latter is put on display in “Life Cycles” by Joshua Sands.
```

### Performance text (classify this)

```text
JASON: Honey, I'm home! (A beat) Honey, I'm home! (Another beat) What's for dinner? Well, whatever it is, it smells -

KARA: Jason? Jason is that you?

JASON: Yes, Kara. I'm finally home.

KARA: Jason, it's been three years! Where have you - I mean, what have you - (a beat) Jason, it's so good to see you!

JASON: You're a sight for sore eyes.

KARA: I've missed you terribly.

JASON: I know. I'm sorry.

KARA: Where did you go? Why haven't you called? Jason - what happened?

JASON: I drove around for a while. Tried A.A. Gave up on that. Dried out in a clinic but let's not talk about that right now. Where's my little Allison?

KARA: No, Jason. Let's do talk about that now.

JASON: Kara, let's not deal with the past. Only the present. You and me. And little Allison.

KARA: She's not so little anymore. She starts kindergarten in the fall.

JASON: WOW - time flies...

KARA: For you, maybe.

(to the audience)

KARA: See, Jason was the love of my life. Met in high school. Went to the same college. Married almost the same time we got our diplomas. We had two good years. You know, he drank a little, but don't we all? But I didn't see it as a problem. Then one night he gets a little weird on me:

JASON: Kara, the system's really quite easy.

KARA: Jason, I-

JASON: The receipts go in the blue folder, the income tax forms in the red, stocks in the yellow. Some of the folders you won't need for months. You know, it all goes in cycles.

KARA: What about the horny green folder?

JASON: Miscellaneous forms - remember?

KARA: Jason - I just don't see -

JASON: I just thought you should know a little bit more about the finances.

KARA: But I always have you take care of that.

JASON: Well sure, but you never know.

KARA: Never know what?

JASON: You just never know.

KARA: And those were the last four words I heard him say. He disappeared the next day. Boss called. He'd emptied his desk. Six months later I get a message on the machine:

JASON: Hey, honey damn - I'm talkin' to my wife - wait your turn! I just wanted to tell you that I'm in Detroit drying out. No problem. Just wait for me, OK? OK, bye ...

KARA: So, I waited. Six months. A year. Mom helped take care of the baby. I worked. But soon I gave up. Divorced him via federal express. Soon enough, he became a memory. Some distant dream of a life long since past, back when I believed in fairy tales. But now, he's standing here telling me:

JASON: Kara, let's start over. Let's do it right this time. No alcohol. No secrets. No lies.

KARA: I never lied to you.

JASON: OK, so I'll start over. You just stay the same. You are already perfect that way.

KARA: Jason, do you have any idea what these years have been like? Do you?

JASON: I know it's been rough, but -

KARA: I'm not the same person anymore. I'm not. I've grown up. I stay home on Saturday nights. I drink wine coolers and get tipsy. I even see signs that I'm becoming my mother. I'm not the person you married.

JASON: But you could be. We could be. Give me that chance. I want to be a good husband. And a good father. Give me that chance.

KARA: Jason-

JASON: We did have some good times, didn't we?

KARA: Well sure -

JASON: It wasn't all bad ...

KARA: Well, not before the -

JASON: Then let's try it. One date. We'll go back to Musselman's bistro. We'll order that special -

KARA: The bistro closed two years ago.

JASON: We'll get good food. I promise. Look, I know this is a lot coming at you all at once, but -

KARA: OK. One date. One date. That's all.

JASON: I'll put on a monkey suit if you like ...

KARA: Just pick me up at 6:00 tomorrow. OK?

JASON: Sure, I know you don't like to wait.

KARA: Actually, I've gotten better at it.

(the date)

JASON: SO, then, this guy starts saying "Oh yeah? You and what army? And then my military buddies stand up and I say "This Army". Now they were Marines, but the guy didn't know that ... he about wet his pants. You know I felt like the Fonz ... just snap my fingers and ... "eeeyyy".

KARA: (Laughing) Wow - you certainly have some stories to tell!

JASON: Always did.

KARA: Remember that one time you got up to go to the bathroom in the middle of the night but walked into the wrong room. I caught you, pants down, sitting on the trash can!

JASON: (Laughing) Yeah, that trash can and I bonded, didn't we?

KARA: I'd say so.

JASON: Kara, it's so good to see you.

KARA: I've missed you, too.

JASON: You've made me laugh for the first time in I don't know how long.

KARA: Trust me - I thought I'd forgotten how.

JASON: Ever since the first day, Junior year of high school. I looked at you and said "That babe will be mine."

KARA: You called me a babe?

JASON: It was before I got Pc. You know - back when the world had a sense of humor.

KARA: Sure.

JASON: (A beat) I know I owe you a lot. I can't begin to say how much.

KARA: Jason, please don't ...

JASON: Your eyes sparkle and light up the room. I want that sparkle back.

KARA: Jason - just dinner ... remember?

JASON: I know I'm rushing, but it feels so right. Kara, will you do me the honor of being my wife?

KARA: (A long beat) Wh-What?

JASON: We could do it all over again. We'll do the wedding with the same yellow roses. Allison could be the flower girl. We could go to Monaco for the honeymoon. We could do it all over -

KARA: Jason, wait.

JASON: What?

KARA: Just wait.

JASON: One word is all I'm asking for and I'll take it from there. Just say yes.

KARA: Jason, you LEFT me! You left without a word. One call in three years. No presents for Allison's birthday or Christmas. Nothing. Did you know she got picked on at pre-school? You know why? Because of you! Everyone knew the story.

JASON: Kara, I can't fix that now. I can only--

KARA: Do you know what it's like to go to the supermarket and hear them whispering? Either they thought it was my fault or I was pitied. Do you know how humiliating that was for me? DO YOU?

JASON: Honey, I'm so sorry. I had no clue-

KARA: That's right. You had no fucking clue! So let's get off this marriage idea for one second and you answer me a question. Why'd you go?

JASON: I was drunk.

KARA: Why'd you go?

JASON: Kara, I was just in a bad state of mind

KARA: Why the hell did you go???

JASON: (breaking down) I don't know. I just don't know. I guess I just wanted to be like that magician who could pull out the tablecloth and leave all the table-settings in place. Take me out. Leave you and Allison in place.

KARA: You know it doesn't work that way, I spent three years waiting for you. I love you, Jason, but I can't do it again.

JASON: You wouldn't have to.

KARA: The answer is no. I won't marry you.

JASON: Is that "No, not now" or "No not ever?"

KARA: Jason, it's just plain no.

(to the audience)

KARA: So now a different night haunts me. It's no longer the folders and the finances. It's the magician and the tablecloth. Three months later he called and left a drunken message on the answering machine. Six months later - rehab. And the cycle had begun all over again. But see, if it really is a cycle, then I relive the moment that he came back, wondering if it will happen again:

JASON: Honey, I'm home! (A beat) Honey, I'm home! (Another beat) What's for dinner? Well, whatever it is, it smells –

KARA: Jason? Jason is that you?

JASON: Yes, Kara. I'm finally home.

KARA: Only this time I take the offer. I take the ring. He moves back in. Allison has a father. And the cycle starts all over again.
```

---

## IC-0831: Linda Wertheimer Script

- Title: Linda Wertheimer Script
- Author (byline): Garrison Keillor
- Work: A Prairie Home Companion: The Screenplay
- Publisher: Penguin
- Publication date as stated: May 2006
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TOGETHER, JOHN, LINDA
- Teaser before the introduction: Yes
- Spoken words (computed): 884
- Already set (do not supply): none

### Source block (context only)

```text
Author: Garrison Keillor
Book: A Prairie Home Companion: The Screenplay
ISBN: 978-0143038238
Publisher: Penguin
Date (Month/Year): May 2006
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: The time when news was gathered ONLY by so-called professionals with bulky expensive cameras and microphones,

ACTOR 2: and disseminated via crazy expensive transmitters to the living rooms of American families is waning.

ACTOR 1: Thank goodness!

ACTOR 2: Today we have the internet, where news breaks sometimes even before it happens!

ACTOR 1: But most of your remember what new coverage used to be like.

ACTOR 2: In The Linda Wertheimer Script, Garrison Keillor has some fun with the travails of satellite broadcasting and the technical delays that came with it.

(PAUSE, THEN SIMULTANEOUS)
```

### Performance text (classify this)

```text
TOGETHER: (THROBBING ELECTRONIC NEWS THEME)

JOHN: A NATION IN CRISIS LOOKS INWARD

LINDA: This is Linda Wertheimer, NPR News in Washington, with a special report from the Middle East. With me on the line from the mountain province of Donundestan, from the provincial capital of Rillirillibad, is correspondent John Knotright with a breaking news report that a planeload of terrorists is on its way to the U.S. at this very moment. John? Can you hear me?

JOHN: Yes, I hear you now.

LINDA: Do you hear me now?

LINDA: Sorry, I stepped on you there.

JOHN: I can hear you loud and clear, Linda.

LINDA: It's Linda -- Go ahead, John. Go ahead.

JOHN: Sorry - I'm having a hard time --

LINDA: We have you, John. Go ahead.

JOHN: Having a little trouble with the satellite delay, there.

LINDA: Yes, I understand. There's a delay with the satellite. Go ahead.

JOHN: You want me to go ahead now?

LINDA: Go ahead, John.

(PAUSE, THEN SIMULTANEOUS)

LINDA: We're ready for you, John.

JOHN: This is John Knotwright, from the provincial capital of Rillirillibad ---- I'm sorry, Linda, did you say something?

LINDA: I said we're ready for your report, John.

JOHN: You want me to do that now, Linda?

LINDA: Yes, go ahead. (PAUSE)

JOHN: Standing by here in Rillirillibad. Whenever you're ready, Linda.

LINDA: Can you hear me, John?

(PAUSE)

JOHN: I can hear you, Linda.

LINDA: Good. We'd like your report now, John.

(PAUSE)

JOHN: Just waiting for your cue, Linda.

LINDA: Let's go to John Knotright in Rillirillibad now for this----

JOHN: It's this satellite connection, Linda. There's a delay and ---- I'm sorry, what did you say?

LINDA: John?

(PAUSE)

JOHN: Yes, Linda.

LINDA: I'm being as clear as I possibly can be.

(PAUSE)

JOHN: You're coming in loud and clear, Linda.

LINDA: John, I'm going to turn it over to you now for your report. (PAUSE) Do you read me, John?

JOHN: You want my report now?

(PAUSE, THEN SIMULTANEOUS)

LINDA: John? Listen to me. We're all waiting to hear your (JOHN: I'm right here, Linda.) report from Rillirillibad---- John? John?

JOHN: Sorry I stepped on you there.

LINDA: John, I'm going to stop talking now and when I do I'd like you to start talking (JOHN: And I have this very cheap earpiece I'm trying to hear you on----) and give us your report ---- what did you say?

(PAUSE)

JOHN: Who?

LINDA: John, we're on the air live with about 600 public radio stations, I'd appreciate it if you could focus----okay? (PAUSE) Okay, John? Are you all set?

JOHN: SIMULTANEOUS Ready when you are, Linda.

(PAUSE)

LINDA: John, how about I just ask you some questions? Okay?

(PAUSE)

JOHN: You're going to ask me questions?

LINDA: Yes.

(PAUSE)

JOHN: After my report?

LINDA: No, instead of your report.

JOHN: Questions about what, Linda?

LINDA: About that planeload of terrorists.

(PAUSE)

JOHN: Standing by here in Rillirillibad, Linda----

LINDA: John, tell me: how did you hear this report of terrorists?

JOHN: SIMULTANEOUS Just fire away.

(PAUSE)

LINDA: John, tell me about the terrorists.

JOHN: SIMULTANEOUS Hello? Linda?

(PAUSE)

LINDA: John?

(PAUSE)

JOHN: Yes, Linda.

LINDA: John, please. Shut your mouth and listen and I'll ask you a question and when I do, you answer it. Okay?

(PAUSE)

JOHN: Okay.

LINDA: Are you shutting your mouth now, John?

JOHN: SIMULTANEOUS So you talk and then I talk, right?

LINDA: John, you're there in Donundestan, from the provincial capital of Rillirillibad, right? You have reports of a planeload of terrorists heading for America --- we'd like to know more. Over to you, John.

(PAUSE)

JOHN: What'd you say?

LINDA: I said, Terrorists, you jerk. Tell us about the terrorists! What do you think I said?

(PAUSE)

JOHN: I don't know about terrorists but there's a planeload of tourists heading for the U.S. Is that what you meant?

LINDA: You told us terrorists.

(PAUSE)

JOHN: Tourists. They're from Iowa. Church people, mostly. Methodists, I think. Here on a study tour. Learning about Islam.

(PAUSE)

LINDA: John, how can you be so unbelievably stupid----

JOHN: SIMULTANEOUS You must've misunderstood me.

LINDA: I'm talking now, John. Why would you be so stupid as (JOHN: Sorry, didn't mean to interrupt.) to file a report ---- Shut up! Do you hear me? Shut up while I'm talking. (PAUSE) John, why would you be so stupid as to----(JOHN: It's the satellite delay, Linda.)--- stop interrupting me! Stop it! Or I'll kill you. And I mean it. Don't push me. Just shut your mouth and listen to me. John, why would you be so incredibly incredibly stupid (JOHN: Sorry, I didn't mean to make you so angry) --- John, let me ask you this: may I ask you a question?

(PAUSE)

JOHN: Go ahead, Linda.

LINDA: I'm going to ask you a question now and you're going to answer it, okay?

(PAUSE)

JOHN: I'll try.

LINDA: Good. Let me ask you this---(JOHN: I'll give it my best shot.) John, why would you bother to tell us about a planeload of tourists that's leaving Rillirillibad there in Donundastan? Why? John? We have important breaking news and we waste five minutes on you telling us about---(JOHN: You want me to answer that now, Linda?) --- what's your problem, John?

JOHN: There isn't much going on here, Linda, and I don't speak the language and the food is bad and they have no alcohol, nothing, not even beer, and I'm just sitting in this crummy hotel watching CNN like everybody else, so when I heard about this planeload of tourists----- I got excited. I'm sorry. So shoot me.

(PAUSE)

LINDA: You're in the south of Afghanistan, right, John?

(PAUSE)

JOHN: Right.

LINDA: We sent you there to look around for Osama bin Laden.

(PAUSE)

JOHN: Who?

LINDA: Osama bin Laden.

JOHN: I thought I was supposed to find a rap star by the name of Yo Mama Bin Rotten.

LINDA: You're an idiot, John.

JOHN: And his drummer, Al Kiyada.

LINDA: You're an idiot. Get on the plane with the tourists, John, and go back to Iowa.

(PAUSE)

LINDA: John?

JOHN: You're breaking up a little, Linda.

LINDA: John, get out of my life. Just disappear. Okay? This is Linda Wertheimer from NPR News----

JOHN: Am I done now?

LINDA: ---- in Washington with a special report.

TOGETHER: (THROBBING ELECTRO NEWS THEME).

JOHN: A NATION IN CRISIS LOOKS WITHIN.
```

---

## IC-0832: Lines

- Title: Lines
- Author (byline): Tony Glazer
- Work: The Best Ten-Minute Plays 2012
- Publisher: Smith and Kraus
- Publication date as stated: June 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JONATHAN, PATRICIA
- Teaser before the introduction: Yes
- Spoken words (computed): 969
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tony Glazer
Book: The Best Ten-Minute Plays 2012
ISBN: 978-1575257938
Publisher: Smith and Kraus
Date (Month/Year): June 2013
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Relationships can be difficult under normal circumstances.

ACTRESS: But when the bond is challenged by additional outside forces . . .Cancer . . . infidelity . . .

ACTOR: How in the world does a couple weather the storm?

ACTRESS: Once you’ve crossed the line, can you ever make it back?

ACTOR: And when all you want to do is blame someone, is forgiveness even a possibility?

TOGETHER: Lines by Tony Glazer
```

### Performance text (classify this)

```text
Lights up on a studio apartment. A few boxes litter the floor someone is either coming or going. A woman PATRICIA stands in the center of the apartment while JONATHAN stands in the door jamb with a box cradled in his arms. Silence. Then ...

JONATHAN: That's it. That's everything.

PATRICIA: Last box. (Awkwardness. Then ...) I've called the utility companies.

JONATHAN: Good, that's . . . I called cable and Sunday Times delivery.

PATRICIA: Everyone in the building just took turns stealing our copy anyway.

JONATHAN: Environmentalists.

PATRICIA: At least they recycle. (JONATHAN notices something.)

JONATHAN: Do you want to take the curtains?

PATRICIA: No.

JONATHAN: Really? You spent so much time picking / them-

PATRICIA: (gently interrupting) Let's, let's just leave them for the next tenant.

JONATHAN: Sure.

PATRICIA: I mean, it's nice to come to a place for the first . . . it's nice to come to the new place you're staying in and find curtains already hanging there.

JONATHAN: Yeah.

PATRICIA: That never happens. People almost always take theirs so when you come in and see them hanging up it's more than just one more thing off your list. It makes everything feel more like a . . .

JONATHAN: Home. (Awkwardness. Finally . . . ) I should go.

PATRICIA: I won't be much longer.

JONATHAN: You're set with everything?

PATRICIA: I'm good.

JONATHAN: You don't need any help with / the rest of

PATRICIA: (gently interrupting) No, no. I'm fine. I've got it.

JONATHAN: Okay. Okay, then. (Beat. Then . . . )

PATRICIA: We did try.

JONATHAN: No one could accuse us of not making the effort.

PATRICIA: We ran the gamut.

JONATHAN: We did.

PATRICIA: Self-help books.

JONATHAN: That vacation.

PATRICIA: Couples' therapy.

JONATHAN: I still don't think that guy was licensed.

PATRICIA: You should let that go.

JONATHAN: Neither of our insurance companies would recognize him, Pat.

PATRICIA: That doesn't mean anything, John.

JONATHAN: Plus he kept wanting us to color in books. What licensed therapist asks you to do that?

PATRICIA: Everyone has their own method.

JONATHAN: Only the "unlicensed ones" involve crayons.

PATRICIA: Don't be so judgmental.

JONATHAN: Wasn't that why we were there?

PATRICIA: We were there to reflect-not judge.

JONATHAN: How do you accomplish that without some form of critical thought?

PATRICIA: Critical thought about us not-it doesn't matter.

JONATHAN: No.

PATRICIA: He didn't help anyway.

JONATHAN: He made it worse. Or better. Depending . . . (The two stand just there, until . . . . ) See you around.

PATRICIA: No.

JONATHAN: No, what?

PATRICIA: You won't "see me around." We broke up, John. We just divided up our belongings and are now going our separate ways. You don't "see each other around" after you do something like that.

JONATHAN: It's just an expression.

PATRICIA: Find a better one.

JONATHAN: Okay. Goodbye.

(JONATHAN exits. PATRICIA begins to cry quietly. JONATHAN returns as if to say something. He stands there, looking at her, affected, before walking to her, putting an arm around her. She s startled at first but then, realizing that it s him, relaxes back into her sadness.)

JONATHAN: It's okay.

PATRICIA: It's not.

JONATHAN: I know.

PATRICIA: Then don't say something is "okay" when you know it's not.

JONATHAN: All right. (He continues to hold her. She continues to cry until it becomes awkward again and they separate.)

PATRICIA: I'm fine now.

JONATHAN: Goodbye. (JONATHAN moves towards to the door.)

PATRICIA: I just . . . (JONATHAN turns back.) I don't . . .

JONATHAN: You slept with my brother.

PATRICIA: I know, John. I was there when it happened.

JONATHAN: You couldn't have thought sleeping with him was going to come without any consequences.

PATRICIA: I didn't.

JONATHAN: And yet you did it all the same knowing full well it was going to lead us right to this moment.

PATRICIA: It wasn't that simple.

JONATHAN: He's my brother.

PATRICIA: You're repeating yourself.

JONATHAN: My stupid, back-stabbing, unemployed, selfish and irresponsible brother.

PATRICIA: At least he could look at my scars without flinching. (Almost unconsciously, JONATHAN looks to PATRICIA s chest before looking away.)

JONATHAN: No . . . don't you . . . don't turn that . . . that's not . . .

PATRICIA: Fair? No it isn't. It's not even decent.

JONATHAN: It's not . . . accurate.

PATRICIA: Accurate enough.

JONATHAN: You changed.

PATRICIA: I survived. (Pause. Finally . . . )

JONATHAN: I should really go.

PATRICIA: You can't color inside the lines.

JONATHAN: What's that?

PATRICIA: At the therapist's office. When he asked us to color. I saw you couldn't color inside the lines. When I saw that I knew it wasn't going to work out.

JONATHAN: Is that right?

PATRICIA: I could never be with someone who couldn't do something as basic as color inside the lines. You have a problem with lines.

JONATHAN: And you don't. Not with crossing them, anyway.

PATRICIA: Screw you.

JONATHAN: See you around. (JONATHAN is about to exit again.)

PATRICIA: Coward. (JONATHAN stops himself, this last statement striking a nerve. Finally . . . )

JONATHAN: I was there for you. (PATRICIA does not respond.) By your side. Through everything. All of it . . . the tests, the insurance forms, the surgery, all that . . . poison. I was there. One hundred percent. Until you got well.

PATRICIA: Your point?

JONATHAN: I loved you.

PATRICIA: Isn't that easy to say?

JONATHAN: I still do for what's it's worth.

PATRICIA: Which isn't much.

JONATHAN: Right.

PATRICIA: Because you're a coward.

JONATHAN: We've been through this already. I don't need to hear-

PATRICIA: I'm very blessed, actually.

JONATHAN: Of course you are. You're alive.

PATRICIA: No. I'm blessed about you. (JONATHAN just stares. Then ... ) Somewhere between sleeping with your brother and the coloring books and you never quite being able to look at my chest it finally occurred to me just how amazing it was to actually be able to see you. See who you really are. Startling, really-the clarity of that moment. I owe you. I never would have challenged our situation. We were on a set track, you and I. We were a straight shot to marriage and kids. I never would have got off that track-not on my own. Of course, now that you've stepped off, not only do I know that I never could be with someone this fundamentally bunched over the lines on my chest, I would never want to be. (Beat. Then . . . )

JONATHAN: (sincere) It's not you, Patricia. It's not / that I don't . . .

PATRICIA: (interrupting) We don't have to revisit / this anymore.

JONATHAN: (interrupting) I can't explain it. I'm not proud of it. It just makes me uncomfortable.

PATRICIA: Stop saying "it." It is not "it." I had to listen to you in that pretend therapist's office go on about "it" for months. Well, before you walk out that door, let's make one thing perfectly clear. "It" is "me," John. You don't have a problem with "it"-it's me you can't look at, can't touch, can't love.

JONATHAN: No, you . . . I don't have a problem with you. You're twisting this . . . it's not . . . you.

PATRICIA: Prove it. (Impulsively, and with her back to the audience, PATRICIA begins to open her blouse.)

JONATHAN: What are you . . .

PATRICIA: If that's true you have to prove it. Right now. Before you go, before we never see each other again, make me believe our entire relationship wasn't a lie.

JONATHAN: Patricia . . . don't . . .

PATRICIA: No, Jonathan. If you loved me-still love me, like you say-then you have to see "me." Not "it." Me.

JONATHAN: Please, Pat. I . . .

(PATRICIA has exposed her chest. JONATHAN, after a moment, looks and then, very tentatively, approaches. After a moment, he puts a hand on PATRICIA’ s chest. His hand stays there for a long time until .. ).

Lines.
```

---

## IC-0833: Little Footsteps

- Title: Little Footsteps
- Author (byline): Ted Tally
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BEN, JOANIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1687
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ted Tally
ISBN: 978-0822206767
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Joanie is an insecure aspiring artist.

ACTRESS: Her husband, Ben - a witty but emotionally stunted television promoter.

ACTOR: In this selection, we find them converting a room in their apartment into a nursery . . .

ACTRESS: and coming to the realization that parenthood is no more than . . .

ACTOR: “The Unprepared attempting the Impossible for the sake of the Ungrateful”

TOGETHER: Little Footsteps by Ted Tally
```

### Performance text (classify this)

```text
BEN: (while painting) It's not that I don't like kids. Hey, I do! I'm walking in the park and I see some dad scraping bubblegum off his little girl's shoe - it just tears me up inside. You know what I mean? (Pause) The thing is, though - I like kids in the abstract. But when I have a kid, he won't live in the abstract. He'll live in my apartment. Right here. Which, let's face it, is already crammed with one husband, one wife, and eight years' worth of furniture. So we're not just talking about the cosmic wonder of creation here. We're dealing with a Man-hattan real estate problem.

[Ben and Joanie are painting what used to be their dining room to make a nursery for the new baby] (Sound of a door opening, off and JOANIE’s voice)

JOANIE: (Off) Ben? I'm back! Hi, honey! God, I missed you! (She hurries to him happily, gives him a big hug) (He returns her hug cautiously, and after a moment she separates from him, looking down at his boxer shorts) What are you wearing?

BEN: My underwear. I couldn't find anything to wear! And I didn't want to mess up my good clothes.

JOANIE: (Looking around) You sure haven't done much painting in here. What've you been up to? God, we're so far behind now . . . (Pause. Then, more cheerfully) Well, never mind . . . we'll do it together. (She kisses him. He turns his face, taking the kiss on his cheek) That'll be more fun anyway! (She takes him by the wrists) Feel. Put your hands right here.

BEN: Aw, I've got paint all over-

JOANIE: Never mind! Just feel . . . (She places his palms flat against her belly, holds them there. A long silence while they look at one another. He feels her gently, looks down at her bulk)

BEN: (Quietly, with wonder) It's so solid. So dense.

JOANIE: That's us, Ben. A part of us.

BEN: (Ben kneels, putting his ear against her belly) He's running another marathon. Can you tell? Go, kid, gol There's the finish line! Just one guy left to beatl (He glances up at JOANIE, grins) "Fetus, don't fail me nowl"

JOANIE: Ben. (But she can't help being amused. Partly to hide this, she kneels at her sketch pad. He rises, circles her)

BEN: What's it like in there? . . . I mean, for one thing, we know it's cramped.

JOANIE: Not to her, it's not. You're just projecting.

BEN: It's hot as hell too, and you've got all this water gooshing around. Gooosh . . . gooooossshhh! (He kneels behind her, pushing against her playfully, trying to distract her from her work) So I'm floating in here . . . sort of snorkeling . . . and I've got these spooky sounds coming at me. And I can't get away from them! I'm trapped! Ba-da-BOOM! What was that? Ba-daBOOM! It's Mama's heartbeat, right in my ear! (JOANIE smiles) And-what's that other weird noise? (Softly) Rumblerumblerumble . . . Sounds like it's coming from her tummy . . . . rumblerumblerumbleRUMBLERUMBLE! . . . Oh, my God, I just remembered! (Clutching her) We drank some BEER today! Mama-she's gonna-she's gonna burp! RUN FOR YOUR LIVES! BURRRRRRRRRRUP! (This last is right in her ear. JOANIE falls over, wincing, laughing outright. He laughs too) No wonder we're so cranky when we finally get out of there! We've just spent nine months in the Twilight Zone. (A muffled shout, into her belly) Don't come out! This is a warning! It's weird out here, tool

JOANIE: (Laughing) You'll catch cold, dressed that way. And I need your help out here. (Pushes him away) Go put on some more clothes!

BEN: (A bit irritated) You're not my mother too, you know.

JOANIE: Get out of here! I mean it! (She rises, props her sketchbook out of the way against a wall)

BEN: (He exits through the french doors; but after only a moment sticks his head back in. To the audience) Don't believe a word she says.

JOANIE: GO!! (He exits. grinning. She shakes her head, exasperated) Ben! Ben, Ben, BEN . .

(She takes her smock from the ladder. As she puts it on, she glances at the audience – throughout the rest of this monologue, she is preparing and putting a butterfly stencil on the wall with cans of spray paint)

Our friends ask me why I want another baby when I've already got one. (Pause) Somehow that used to sound funnier . . . What's he been doing in here, anyway - He promised me he'd spend the whole weekend painting the sky. But, as you can see . . . Mr. Responsibility. (She crosses to the wall, up right, where she tapes up her stencil) The irony is, he's gonna make a great father. He really is! . . . I wish you could see him with other people's kids. He'll get down on the floor and hold this serious, top-secret, totally involved conversation with some two-year-old! But, then, if you ask him what on earth they could possibly find to talk about for all that time, he says something like, "Know your enemy." (works for a moment) He works in television, [you know].

(Pause. She pours some paint into an aluminum troy, picks up a pair of brushes)

(BEN reenters through the kitchen door, now wearing ratty jeans and a corduroy shirt over a T-shirt. He is finishing a sandwich, and also sipping a beer)

BEN: (To audience) Lies, lies, a tissue of lies . . . What? What is it?

JOANIE: I guess you'd have to know sooner or later, Ben. I told them . . . you were in TV.

BEN: (Horrified) Oh, God, no. You didn't.

JOANIE: Sorry. Your secret is out.

BEN: (Kneels) Friends, I was young, I was a fool. They said I'd meet Miss Piggy. (To JOANIE, as he rises) Where do you need me?

JOANIE: Take down the other stencils.

BEN: Check. (He sets down his beer and sandwich on the windowsill, then starts pulling down stencils. She has begun painting blue sky on the wall)

BEN: Actually, I'm in television sports promotion. Those little teasers that warn you not to miss next Saturday's flaming tapioca plunge?

JOANIE: They're called "promos."

BEN: Well, that's what I do. I design those promos. For ten seconds a week I'm a genius.

JOANIE: He was a finalist for a Clio Award.

BEN: I lost out to some ex-jock doing a public-service spot on drug abuse. Depressed me so much I got stoned for a week.

JOANIE: (Irritated) Why do you tell them things like that? You know that's not true.

BEN: Okay. Two days. (He crosses to dump his handful of stencils by the pile of paint cans at right center) Joanie's a little paranoid about drugs. She's afraid we did so many of them in college-

JOANIE: You did so many!

BEN: I did so many of them that the baby will be born looking like Flipper. (A brief but vivid impression) "Orkl Ork! Ork! Orkin

JOANIE: (Shocked) That's not funny! Don't even think that! (Furious) You go too far sometimes, you know that? You think you're so hilarious - telling your little dead-baby jokes when our friends come over-

BEN: (To audience) I've never done that!

JOANIE: Oh, uh-huhl (Crossing down toward audience) "How do you make a dead baby float? One scoop of ice cream, and one scoop of dead baby:' How do you think it makes me feel when you say things like that? What if something did happen? You think it's so funny to joke about now, but what if it did?

BEN: (Still trying to lighten the situation, but it fails) "Orkl Ork! Orkl" (Very upset, she pulls her mask over her face to continue painting. Her back to the audience, point-edly ignoring BEN. He looks at the audience helplessly) Okay, but she's overreacting, too. She really is!... (Pause) What if Joanie was right? (Pause) What if one of those jokes did come true? What if something went wrong with the baby? Would I be able to handle it, or would I panic . . . ?

(Fantasy sequence – transition needs some type of ominous sound/music – can be voiced by Joanie before she rises and turns around ominously. She wears green plastic gloves and stares at BEN over the top of her painting mask. She moves forward into his circle of light)

JOANIE: Benjamin?

BEN: (Turns, sees her) Oh, hiya, Dr. Latimer! Did everything come out okay in the delivery room? (She is silent. He chuckles nervously) That's a joke! You know- "baby?" "come out?"

JOANIE: My poor dear Benjamin . . .

BEN: (Growing alarmed) It's Joanie, isn't it? Something's happened to Joanie!

JOANIE: (Pulls mask down sadly) Your wife is fine. I have her under sedation. She-- doesn't know yet.

BEN: Know what? (Pause) You mean-the baby? (She nods) You mean it's . . . ?

JOANIE: Oh no, no, it's alive! (Pause) That is, we definitely feel that it's living.

BEN: Why-why do you say "it?" Is it a boy or a girl?

JOANIE: (Hesitates) Yes! . . . Look, why split hairs? I told you it was alive.

BEN: (Shaking her) WHAT-IS-WRONG-WITH-MYCHILD?!

JOANIE: (frees herself gently) Ben, I'm going to level with you. Your - well, let's call him your son - was born without a body.

BEN: Without a body? Oh my God, that's horrible!

JOANIE: (Sighs) Yes. Yes, it is. I can only suspect that you or Joanie must have experimented at some point with a marijuana cigarette.

BEN: You mean . . . my boy is nothing but a head? That's all there is to him?

JOANIE: I only wish it were that simple, Ben. Your son doesn't even have a head. In fact, he's just an eyeball. I have him right here. (JOANIE takes a glass eyeball out of her pocket. As BEN rises, she hands it to him)

BEN: (Stunned) This is . . . my son?

JOANIE: Careful how you hold him. He blinks.

BEN: (Suddenly shrieking) OH MY GOD, MY SON IS AN EYEBALL! OH MY GOD! WHAT COULD BE WORSE THAN THIS?!

JOANIE: (Whispers) He's blind!

(BEN screams, tossing the eyeball high into the air. JOANIE catches the eye. Laughing insanely, she returns to her former position. BEN clutches his chest and gasps for breath. JOANIE, instantly back in character, turns from her painting)

JOANIE: Ben . . . ? What's the matter?

BEN: (Squeaks) Heart attack! (She rushes to him, but he avoids her and begins jogging frantically in place, turning in little circles)

JOANIE: What are you doing? Hold stilll

BEN: If I stop I'll die! But if I just keep jogging! Then maybe I'll feel like it's just beating fast! Because I'm jogging! And not because I'm having! A heart attack!

JOANIE: (She finally stops his jogging. He stares at her, panting) You're having an anxiety attack! You've had them before, so we both know there's nothing to be afraid of. In a few minutes it'll go away, if you just don't panic. Okay? Focus on me! We're gonna pretend we're in Lamaze class, okay? I want you to take a long, deep breath. (He nods) Are you ready? Breathe . . . innn. Slow and steady . . . that's it, keep going . . . Good, now hold it for a minute. (Pause) Okay, now let that air out, but slowwwly . . . and innn . . . hold it . . . and ouuut. Innnn . . . and ouuut. Slowwwwly!

BEN: (Pause, his breathing has returned to almost normal) I shouldn't have said what I said about Flipper. I'm sorry. (She looks at him for a long moment, sighs. She looks at the walls, then back at BEN)

JOANIE: Do the sun. (She crosses back to the wall, left, picks up her tray and begins painting areas of sky again)

BEN: The sun! Riiiight! Jolly or smiling face of the jolly or sun . . . (Pause) What color?

JOANIE: Well, what color do you think?

BEN: (Shrugs) Depends on how much air pollution.

JOANIE: Try yellow.

BEN: Yellow! Now, there's an idea! See, Joanie knows about stuff like that, 'cause she's got a B.A. in art. (He crawls about in search of yellow paint)

JOANIE: Right now I'm a volunteer assistant at the Met.

BEN: Scared you might finally make some money? (She gives him a look) Joke! It's a joke . . . c'mon! (Both resume working in silence for a moment)

JOANIE: (Changing the subject) Ben and I play this game we call "Tough Questions." You know-sort of a rehearsal. Like, "Daddy, Daddy, why is there death?"

BEN: Or "Mommy, Mommy, what is my thing for?"

JOANIE: Or "How come God makes bag ladies?"

BEN: Or "Who was Leona Helmsley?"

JOANIE: (Laughs) All the real biggies we might have to face someday. Okay, Dad, for fifty points! I come home from school one day, I'm crying buckets-make believe I'm crying-

BEN: Buckets, right-

JOANIE: I'm fifteen years old, I'm incredibly upset. And I say to you, "Daddy, Daddy, I think I'm gay." And you say-?

BEN: Ah! (Pause) Mmm-hmm. (Pause) "I don't suppose there's any chance you mean 'convivial'?"

JOANIE: "Dad-dy! Be serious!"

BEN: Right. Sorry. (Pause) Umm . . . "Have a seat, my child." (He motions for Joanie to sit on one of the paint cans at right center. She is a bit reluctant to stop working, but sits as directed, setting her tray down beside her. He looks at her, smiles, gets no response. Then he tries a fatherly little punch on her shoulder) "Son, listen to me-"

JOANIE: Daughter.

BEN: Daughter? No fair!

JOANIE: (Firmly) Daughter, fifteen. Sobbing.

BEN: Why do I always get the worst ones? (She wails) Okay, okay! (Pause. He paces awkwardly, searching for words. Joanie smiles at us, enjoying the game) "Sweetheart, look - your mother and I - ah, understand what you're going through. Believe me-nobody knows better than we do just how scary and confusing sex can be." (Joanie smacks his leg. He grins) "But hey, this isn't the Dark Ages! After all, we're in the year-" (Pause) What year is it?

JOANIE: Well, if I'm fifteen, that would make it . . .

BEN: Christ. *enter year 15 years from this one*. (Slight pause. They look at each other unhappily) Sweetheart, we just want you to know . . . to know that no matter what choice you may ultimately make as to your, umm, sexual preference - to know that you'll still be our child . . . and your mother and I will still love you very, very much." (Pause) How's that?

JOANIE: Not bad! But what would you really say?

BEN: (Shouts) "Homol Homo! Homo!" 0

(She jumps up, stabbing at him with her paintbrush. He backs away, both of them laughing as he catches the wet blows with his palms. Abruptly he clutches his chest, as if having another of his «heart attacks . . . When she steps toward him anxiously, lowering her paintbrush; he catches her off guard and sweeps her into a hug. They kiss. It is a long embrace, of growing intensity. Finally she becomes self-conscious about the audience. Despite his resistance, she gently but firmly breaks off the kiss. They stand looking out at the audience for a moment, still hugging. Pause. BEN looks at JOANIE)

Parenthood, huh? . . . The Unprepared attempting the Impossible for the sake of the Ungrateful.
```

---

## IC-0834: Little Footsteps

- Title: Little Footsteps
- Author (byline): Ted Tally
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BEN, JOANIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1974
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ted Tally
ISBN: 978-0822206767
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Joanie is an insecure aspiring artist.

ACTRESS: Her husband, Ben - a witty but emotionally stunted television promoter.

ACTOR: In this selection, we find them converting a room in their apartment into a nursery . . .

ACTRESS: a longstanding project that has revealed both Joanie's agonizing self-doubts and Ben's hostility toward her

TOGETHER: Little Footsteps by Ted Tally
```

### Performance text (classify this)

```text
BEN: (while painting) It's not that I don't like kids. Hey, I do! I'm walking in the park and I see some dad scraping bubblegum off his little girl's shoe - it just tears me up inside. You know what I mean? (Pause) The thing is, though - I like kids in the abstract. But when I have a kid, he won't live in the abstract. He'll live in my apartment. Right here. Which, let's face it, is already crammed with one husband, one wife, and eight years' worth of furniture. So we're not just talking about the cosmic wonder of creation here. We're dealing with a Man-hattan real estate problem.

[Ben and Joanie are painting what used to be their dining room to make a nursery for the new baby] (Sound of a door opening, off and JOANIE’s voice)

JOANIE: (Off) Ben? I'm back! Hi, honey! God, I missed you! (She hurries to him happily, gives him a big hug) (He returns her hug cautiously, and after a moment she separates from him, looking down at his boxer shorts) What are you wearing?

BEN: My underwear. I couldn't find anything to wear! And I didn't want to mess up my good clothes.

JOANIE: (Looking around) You sure haven't done much painting in here. What've you been up to? God, we're so far behind now . . . (Pause. Then, more cheerfully) Well, never mind . . . we'll do it together. (She kisses him. He turns his face, taking the kiss on his cheek) That'll be more fun anyway! (She takes him by the wrists) Feel. Put your hands right here.

BEN: Aw, I've got paint all over-

JOANIE: Never mind! Just feel . . . (She places his palms flat against her belly, holds them there. A long silence while they look at one another. He feels her gently, looks down at her bulk)

BEN: (Quietly, with wonder) It's so solid. So dense.

JOANIE: That's us, Ben. A part of us.

BEN: (Ben kneels, putting his ear against her belly) He's running another marathon. Can you tell? Go, kid, gol There's the finish line! Just one guy left to beatl (He glances up at JOANIE, grins) "Fetus, don't fail me nowl"

JOANIE: Ben. (But she can't help being amused. Partly to hide this, she kneels at her sketch pad. He rises, circles her)

BEN: What's it like in there? . . . I mean, for one thing, we know it's cramped.

JOANIE: Not to her, it's not. You're just projecting.

BEN: It's hot as hell too, and you've got all this water gooshing around. Gooosh . . . gooooossshhh! (He kneels behind her, pushing against her playfully, trying to distract her from her work) So I'm floating in here . . . sort of snorkeling . . . and I've got these spooky sounds coming at me. And I can't get away from them! I'm trapped! Ba-da-BOOM! What was that? Ba-daBOOM! It's Mama's heartbeat, right in my ear! (JOANIE smiles) And-what's that other weird noise? (Softly) Rumblerumblerumble . . . Sounds like it's coming from her tummy . . . . rumblerumblerumbleRUMBLERUMBLE! . . . Oh, my God, I just remembered! (Clutching her) We drank some BEER today! Mama-she's gonna-she's gonna burp! RUN FOR YOUR LIVES! BURRRRRRRRRRUP! (This last is right in her ear. JOANIE falls over, wincing, laughing outright. He laughs too) No wonder we're so cranky when we finally get out of there! We've just spent nine months in the Twilight Zone. (A muffled shout, into her belly) Don't come out! This is a warning! It's weird out here, tool

JOANIE: (Laughing) You'll catch cold, dressed that way. And I need your help out here. (Pushes him away) Go put on some more clothes!

BEN: (A bit irritated) You're not my mother too, you know.

JOANIE: Get out of here! I mean it! (She rises, props her sketchbook out of the way against a wall)

BEN: (He exits through the french doors; but after only a moment sticks his head back in. To the audience) Don't believe a word she says.

JOANIE: GO!! (He exits. grinning. She shakes her head, exasperated) Ben! Ben, Ben, BEN . .

(She takes her smock from the ladder. As she puts it on, she glances at the audience – throughout the rest of this monologue, she is preparing and putting a butterfly stencil on the wall with cans of spray paint)

Our friends ask me why I want another baby when I've already got one. (Pause) Somehow that used to sound funnier . . . What's he been doing in here, anyway - He promised me he'd spend the whole weekend painting the sky. But, as you can see . . . Mr. Responsibility. (She crosses to the wall, up right, where she tapes up her stencil) The irony is, he's gonna make a great father. He really is! . . . I wish you could see him with other people's kids. He'll get down on the floor and hold this serious, top-secret, totally involved conversation with some two-year-old! But, then, if you ask him what on earth they could possibly find to talk about for all that time, he says something like, "Know your enemy." (works for a moment) He works in television, [you know]. (A slight pause) Why can't he . . . why can't he just be a little bit happier about this? Or at least pretend he is. I mean, I look at a tree and think, God! what would that look like, the first time you ever saw one? What would a butterfly look like, or a rainbow, if you didn't even know they had names yet? Can't Ben see that something is happening here? Something-finally-important in our lives.

(Pause. She pours some paint into an aluminum troy, picks up a pair of brushes)

(BEN reenters through the kitchen door, now wearing ratty jeans and a corduroy shirt over a T-shirt. He is finishing a sandwich, and also sipping a beer)

BEN: (To audience) Lies, lies, a tissue of lies . . . What? What is it?

JOANIE: I guess you'd have to know sooner or later, Ben. I told them . . . you were in TV.

BEN: (Horrified) Oh, God, no. You didn't.

JOANIE: Sorry. Your secret is out.

BEN: (Kneels) Friends, I was young, I was a fool. They said I'd meet Miss Piggy. (To JOANIE, as he rises) Where do you need me?

JOANIE: Take down the other stencils.

BEN: Check. (He sets down his beer and sandwich on the windowsill, then starts pulling down stencils. She has begun painting blue sky on the wall)

BEN: Actually, I'm in television sports promotion. Those little teasers that warn you not to miss next Saturday's flaming tapioca plunge?

JOANIE: They're called "promos."

BEN: Well, that's what I do. I design those promos. For ten seconds a week I'm a genius.

JOANIE: He was a finalist for a Clio Award.

BEN: I lost out to some ex-jock doing a public-service spot on drug abuse. Depressed me so much I got stoned for a week.

JOANIE: (Irritated) Why do you tell them things like that? You know that's not true.

BEN: Okay. Two days. (He crosses to dump his handful of stencils by the pile of paint cans at right center) Joanie's a little paranoid about drugs. She's afraid we did so many of them in college-

JOANIE: You did so many!

BEN: I did so many of them that the baby will be born looking like Flipper. (A brief but vivid impression) "Orkl Ork! Ork! Orkin

JOANIE: (Shocked) That's not funny! Don't even think that! (Furious) You go too far sometimes, you know that? You think you're so hilarious - telling your stupid little dead-baby jokes when our friends come over-

BEN: (To audience) I've never done that!

JOANIE: Oh, uh-huhl (Crossing down toward audience) "How do you make a dead baby float? One scoop of ice cream, and one scoop of dead baby:' How do you think it makes me feel when you say things like that? What if something did happen? You think it's so funny to joke about now, but what if it did? I know you, you'd freak out! You wouldn't be able to handle it! You'd be out the door like a shot, and leave me stuck with-leave m-me ss-stuck with-(She starts to cry, turns her back angrily. She tries to start painting again)

BEN: (Following) That's just not true! First of all, it's not going to happen. Okay? And second of all, we're in this thing together-one hundred percent. My God, don't you know that I would never, ever desert you because of something bad happening? Even though it's not going to happen. (Touching her shoulders) Don't you know that by now, sweetheart?

JOANIE: (Shaking free) Don't call me sweetheart, either! You only say those things when you're mad at me.

BEN: (Still trying to lighten the situation, but it fails) "Orkl Ork! Orkl" (Very upset, she pulls her mask over her face to continue painting. Her back to the audience, point-edly ignoring BEN. He looks at the audience helplessly) There I go again! (Crossing down center) What is wrong with me? I don't want to hurt her-I don't mean to hurt her-and I hurt her. (Pause) Okay, but she's overreacting, too. She really is! I'm not taking the rap for all of this ... (Pause) What if Joanie was right? (Pause) What if one of those jokes did come true? What if something went wrong with the baby? Would I be able to handle it, or would I panic like she said . . . ?

(Fantasy sequence – transition needs some type of ominous sound/music – can be voiced by Joanie before she rises and turns around ominously. She wears green plastic gloves and stares at BEN over the top of her painting mask. She moves forward into his circle of light)

JOANIE: Benjamin?

BEN: (Turns, sees her) Oh, hiya, Dr. Latimer! Did everything come out okay in the delivery room? (She is silent. He chuckles nervously) That's a joke! You know- "baby?" "come out?"

JOANIE: My poor dear Benjamin . . .

BEN: (Growing alarmed) It's Joanie, isn't it? Something's happened to Joanie!

JOANIE: (Pulls mask down sadly) Your wife is fine. I have her under sedation. She-- doesn't know yet.

BEN: Know what? (Pause) You mean-the baby? (She nods) You mean it's . . . ?

JOANIE: Oh no, no, it's alive! (Pause) That is, we definitely feel that it's living.

BEN: Why-why do you say "it?" Is it a boy or a girl?

JOANIE: (Hesitates) Yes! . . . Look, why split hairs? I told you it was alive.

BEN: (Shaking her) WHAT-IS-WRONG-WITH-MYCHILD?!

JOANIE: (frees herself gently) Ben, I'm going to level with you. Your - well, let's call him your son - was born without a body.

BEN: Without a body? Oh my God, that's horrible!

JOANIE: (Sighs) Yes. Yes, it is. I can only suspect that you or Joanie must have experimented at some point with a marijuana cigarette.

BEN: You mean . . . my boy is nothing but a head? That's all there is to him?

JOANIE: I only wish it were that simple, Ben. Your son doesn't even have a head. In fact, he's just an eyeball. I have him right here. (JOANIE takes a glass eyeball out of her pocket. As BEN rises, she hands it to him)

BEN: (Stunned) This is . . . my son?

JOANIE: Careful how you hold him. He blinks.

BEN: (Suddenly shrieking) OH MY GOD, MY SON IS AN EYEBALL! OH MY GOD! WHAT COULD BE WORSE THAN THIS?!

JOANIE: (Whispers) He's blind!

(BEN screams, tossing the eyeball high into the air. JOANIE catches the eye. Laughing insanely, she returns to her former position. BEN clutches his chest and gasps for breath. JOANIE, instantly back in character, turns from her painting)

JOANIE: Ben . . . ? What's the matter?

BEN: (Squeaks) Heart attack! (She rushes to him, but he avoids her and begins jogging frantically in place, turning in little circles)

JOANIE: What are you doing? Hold stilll

BEN: If I stop I'll die! But if I just keep jogging! Then maybe I'll feel like it's just beating fast! Because I'm jogging! And not because I'm having! A heart attack!

JOANIE: (She finally stops his jogging. He stares at her, panting) You're having an anxiety attack! You've had them before, so we both know there's nothing to be afraid of. In a few minutes it'll go away, if you just don't panic. Okay? Focus on me! We're gonna pretend we're in Lamaze class, okay? I want you to take a long, deep breath. (He nods) Are you ready? Breathe . . . innn. Slow and steady . . . that's it, keep going . . . Good, now hold it for a minute. (Pause) Okay, now let that air out, but slowwwly . . . and innn . . . hold it . . . and ouuut. Innnn . . . and ouuut. Slowwwwly!

BEN: (Pause, his breathing has returned to almost normal) I shouldn't have said what I said about Flipper. I'm sorry. (She looks at him for a long moment, sighs. She looks at the walls, then back at BEN)

JOANIE: Do the sun. (She crosses back to the wall, left, picks up her tray and begins painting areas of sky again)

BEN: The sun! Riiiight! Jolly or smiling face of the jolly or sun . . . (Pause) What color?

JOANIE: Well, what color do you think?

BEN: (Shrugs) Depends on how much air pollution.

JOANIE: Try yellow.

BEN: Yellow! Now, there's an idea! See, Joanie knows about stuff like that, 'cause she's got a B.A. in art. (He crawls about in search of yellow paint)

JOANIE: Right now I'm a volunteer assistant at the Met.

BEN: Scared you might finally make some money? (She gives him a look) Joke! It's a joke . . . c'mon!

JOANIE: They've been very understanding about the pregnancy, and they said this winter, if I want, I can even do some tour-group lectures. (Pause) They like me there, they really do. (BEN crosses upstage, toward the hallway, where more paint cans are piled)

BEN: "A little gal with your talents, my goodness, we're just going to have to put you on salary one of these days."

JOANIE: (Pauses in her work) You've made your point, okay? So just drop it. (Joanie steps out of the scene to speak to the audience. Sadly . . . Quietly) Let's have it, he said. So what if it's a surprise. We're as ready as we'll ever be - he said that. And now, because I was dumb enough to take him at his word, he'll never forgive me. (Pause). . . I've asked myself a hundred times - what if I'm having this baby for all the wrong reasons? What if this is really just some ridiculous attempt to make Ben stop taking me for granted? Or what if I'm only going through with this because I can't keep a job? . . . terrible questions, and I've agonized over them for weeks. (Joanie freezes)

BEN: She's always right, and I'm always wrongl Okay? If you're keeping score, that's all you need to know. (He paces angrily, kicking at the discarded stencils) She's this sweet Earth Mother, so put-upon, and I'm just a spoiled immature selfish *jerk* who only thinks about himself-okay? (Crossing downstage toward audience) Except for one little thing-i-I'm the one who has to get up in the morningl Okay? I'm the one who goes off to work so we might have a little money around here, so we can pay for the kid's twenty-two million dollars a year in college tuition! And she's the one (He turns, gesturing and sees her . . . she enters the scene. He takes a deep breath and plunges on) -She's the one who sits around here doing her little drawings all day, goes off to do her volunteer work, has tea with the girls, for Christ's sake, and then says - (He looks at his watch) -"Oh, what the hell, I got some time to kill, I think I'll have a baby!" So you tell me - (Then, to her) You tell me, who's so selfish around here?

JOANIE: Do you even know how pathetic that sounds?

BEN: I never wanted this kid! Never! And I don't want him now!

JOANIE: Liar! LIAR!

BEN: Every day you get bigger, and we get smaller! Can't you understand? I liked us the way we were!

JOANIE: Ben, you're trying to make me choose between you and the baby, and I can't do that anymore! You can't ask me to!

BEN: What the hell was I supposed to do? Knock you out and drag you to the abortion?

JOANIE: (White, shaken) You don't say that to me! You don't say to me something that can never be taken back!

BEN: (Shouting) A baby! A baby can never be taken back!

JOANIE: Get out of here. Just get out of this apartment . . . (LONG PAUSE)

BEN: (Almost a whisper) Mommy, Mommy . . . what is wrong with Daddy?

JOANIE: He's scared. (Pause) I'm scared too, baby.

BEN: Joanie? We can fix it-?

(Sadly) (She exits through the french doors. After a moment

JOANIE: Not this time, Ben. we hear the front door opening and then closing)

BEN: (Softly) Joanie . . .?
```

---

## IC-0835: Little Red Riding Hood

- Title: Little Red Riding Hood
- Author (byline): Billy Aronson
- Work: The Best American Short Plays 1992-1993
- Publisher: Applause Books
- Publication date as stated: May 2000
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MOTHER, RED, WOLF, HUNTER, GRANDMOTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1680
- Already set (do not supply): none

### Source block (context only)

```text
Author: Billy Aronson
Book: The Best American Short Plays 1992-1993
ISBN: 978-1557831675
Publisher: Applause Books
Date (Month/Year): May 2000
```

### Introduction (context only: never use it for content warnings)

```text
Actress: Little Red Riding Hood . . . . .

Actor: the contemporary version

Together: by Billy Aronson
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Singing Intro from Sam The Sham & The Pharaohs Listen to the Lyrics at the following link: http://www.youtube.com/watch?v=_FA85RO89HA

Owoooooooo!
Who's that I see walkin' in these woods?
Why, it's Little Red Riding Hood.
Hey there Little Red Riding Hood,
You sure are looking good.
You're everything a big bad wolf could want.
Listen to me.
Little Red Riding Hood
I don't think little big girls should
Go walking in these spooky old woods alone.
Owoooooooo!

SCENE 1 LITTLE RED RIDING HOOD and her MOTHER.

MOTHER: This fresh fruit pie should help make Grandmom strong again, don't you think, Red?

RED: Yes, Mother.

MOTHER: Let's add a warm muffin for the woman who made my bed and kissed me goodnight.

RED: Yes, Mother.

MOTHER: Let's stuff the muffin with a stone so she'll choke. That woman said I was worthless, Red.

RED: I understand, Mother.

MOTHER: But she sure could soothe me to sleep with a bedtime story. So lean Grandmom forward and pat her back 'til she coughs up the stone.

RED: Yes, Mother.

MOTHER: Apologize to the woman who gave birth to your Mother. Then smash her head with a chair.

RED: Yes, Mother.

MOTHER: On second thought, it would be a shame to smash Grandmom when she's already suffering so. Let's wait 'til she's feeling better to choke her and smash her. For now just bring her the goodies.

RED: Yes, Mother.

MOTHER: Stay on the open path the whole way, don't wander into the woods.

RED: I won't, Mother.

MOTHER: If a stranger pokes his head out ignore him. Eyes ahead. Face down. What's that ugly frown? We're talking about keeping the stranger at a distance, not disgusting him.

RED: All right, Mother.

MOTHER: What are we saying. You're too young to talk to strangers. Go straight to Grandmom's.

RED: All right, Mother. Bye, Bye! [RED exits.]

MOTHER: I knew one day she'd leave.

SCENE 2 LITTLE RED RIDING HOOD and the BIG BAD WOLF

WOLF: Nice hat. You from around here?

RED: Yeah.

WOLF: It's a pretty area.

RED: Your woods seem nice. You call it woods or wood?

WOLF: Woods, wood, forest ... Don't ask me what a thicket is. Come sit in the shade.

RED: No thanks.

WOLF: I like your basket.

RED: It's my Mom's.

WOLF: Can I see?

RED: I have to get to my Grandmother's.

WOLF: That's your Grandmother? Down at the end of the road, right at the fork?

RED: Left-

WOLF: Yeah, left, 'til you pass the lake

RED: Right before the lake.

WOLF: What's the number on her door .. .?

RED: Four.

WOLF: Right. Sweet woman.

RED: She's been sick.

WOLF: She has seemed kind of unwell.

RED: Does your face sweat a lot?

WOLF: No more than yours.

RED: How far out do your claws come?

WOLF: Tah dah.

RED: Gleaming needles.

WOLF: I keep them clean.

RED: They're so long.

WOLF: Thank you.

RED: I've never seen such big teeth.

WOLF: I've never seen such smooth bare hands. How do you make them glow like that?

RED: I don't know. [RED slaps her ankle.] Mosquito.

WOLF: I'll scratch it for you.

RED: No thanks.

WOLF: It's the least I can do. You wouldn't have been bitten if you hadn't stopped to talk with me. When you scratch yourself you can't fully enjoy the relief. Let me have your leg. Come on. Pull up the cape. Up, I don't want to tear it. Slide down the sock. Relax.

RED: OW. Ee.

WOLF: Now with the teeth.

RED: Ooo-Stop. Someone could see. What would ...

WOLF: You're right. Your face is as red as your hood.

RED: That's the way it goes.

WOLF: SO how about a tour of the woods?

RED: Oh no.

WOLF: You're sure?

RED: I have to get to Grandmom's house.

WOLF: I should be going too. But let me give you some advice. You walk too fast. Take some time to admire all the beautiful flowers along the path. Pick your Grandmother a bouquet. [WOLF goes. RED plucks flowers.]

SCENE 3 The HUNTER sits, is served by the MOTHER.

HUNTER: Where's my slab O’ steak?

MOTHER: Coming dear.

HUNTER: If a hunter doesn't have his slab O’ steak he can't grab his gun and if he can't grab his gun he can't blast the beasts and if he can't blast the beasts how's he gonna market their meats if he can't market their meats there's no way he can house his spouse and if he can't house his spouse then where's he supposed to eat his slab O’ steak, in the gosh darn mud crap slop?

MOTHER: You didn't get one of your arms into your shirt, dear.

HUNTER: Sure you miss a sleeve now and then or sometimes you forget to button a few buttons, but what about the sleeve you did get into the shirt, what about the buttons you did button. I'm sick and tired of people who always focus on the empty sleeve or the unbuttoned button-

MOTHER: Your fly's open.

HUNTER: -or the opened fly, when the fact is if the truth be known when push comes to shove it's the people with the unbuttoned buttons and unsleeved arms who are out there not looking at the lookers who are looking at them but just plain out there being out there. I'm out there.

MOTHER: I know you're out there, dear.

HUNTER: I'm the one who faces the heat and the snow and the dirtand let me tell you it gets dirty-so I can brave the hills and the lakes and the pebbles-which inevitably get in your boots-to grapple with the branches and the ragweed and the pollen-'til I'm sneezin' my head off-

MOTHER: There's grease on your nose and steak on your forehead, and your fork is lodged behind your ear.

HUNTER: What's a drop 0' grease on a hunter's nose for the sake of his home, or a fork in his ear for his family? I love this fork and I love this family and let me tell you something, sister, I may have a slab of greasy beef suspended from my brow but that won't stop me from pumping ten ounces of lead into a fat quadruped at close range because it's a dog eat dog jungle in that forest.

SCENE 4 GRANDMOTHER in her bed.

GRANDMOTHER: Yecch. [Spits.] I'm spitting up my rotten guts. Where's my lousy bowl. Have to crawl to the cupboard on my throbbing knees. Can't open the latch with my cracked-up knuckles. Back to the bed for that worthless ointment. Can't grip the cap in my rotten wrecked-up teeth, where's my busted tweezers. Lousy bowl was right here the whole time. Useless eyes. Yecch. [Spits.] Missed. [A knock at the door.]

GRANDMOTHER: Knock knock yourself.

WOLF: It's Little Red Riding Hood with a snack from Mother.

GRANDMOTHER: Couldn't keep down a snack if I wanted to.

WOLF: There's a pie and a muffin ...

GRANDMOTHER: Leave me alone.

WOLF: and some wine ...

GRANDMOTHER: Get in here. 'Snot locked. [WOLF enters.]

WOLF: Into the closet. I'm here to eat your Granddaughter.

GRANDMOTHER: You discriminate against the aged?

WOLF: I'll eat you later.

GRANDMOTHER: Right now, or I don't budge.

WOLF: Sorry but I'm going to relax now, to get ready for Little Red.

GRANDMOTHER: You could put an end to every ache in my body in an instant and I demand you do it.

WOLF: I'm a wolf, not a charity worker. I'll get to you when I feel like it.

GRANDMOTHER: You'll never eat me, I know it. I'll keep getting more dumb and decrepit 'til there isn't a tooth left in my-ocean? teaspoon? and I can't even get myself up out of the-soldier? celery?-Oh stitch. I'm losing my ability to think of the right word to plant.

WOLF: Old ladies are a pain Okay, I'll eat you if . . . if you hand me your shawl.

GRANDMOTHER: [She hands him her shawl, crawls under the sheets. WOLF crawls under, eats her, emerges in her shawl.]

SCENE 5 RED and the WOLF.

RED: Grandmom?

WOLF: Come on in, honey. Shut the door. Get comfy. [Removes Shawl] Surprise.

RED: Hi.

WOLF: Hi.

RED: How've you been?

WOLF: Thinking about you. How have you been?

RED: Since Grandmom's gone we can have a muffin.

WOLF: I would love a muffin.

RED: Okay.

WOLF: How'd it get smushed?

RED: My Mother put a stone in and took it out again.

WOLF: Why'd she do that? Anyway, it's a delicious muffin.

RED: You looked weird in Grandmom's shawl.

WOLF: Did I surprise you?

RED: Uh, no.

WOLF: I was afraid if you saw me right when you walked in you might run. You seemed so bashful before.

RED: I picked flowers like you said.

WOLF: Very pretty.

RED: When I'm in your stomach will I be alive?

WOLF: You'll be unconscious.

RED: For how long?

WOLF: A few minutes. Then you run out of air. But you won't feel anything at that point.

RED: No one's woken up and couldn't breathe?

WOLF: Not that I know of.

RED: Couldn't you kill me with your teeth on the way in?

WOLF: It's better for me if I swallow you whole. And for you too. Less mess.

RED: Should I get undressed?

WOLF: Just take off your shoes.

RED: How was Grandmom?

WOLF: I prefer kids.

RED: Now I'm scared.

WOLF: Don't be. [He eats her .falls asleep.]

SCENE 6 The HUNTER enters followed by the MOTHER.

MOTHER: She always comes straight home.

HUNTER: Would you pipe the heck down with your pointless panic before you work yourself up-See? There's her basket and her shoes and the Wolf [into a frenzy.] Help! Wolf! Help! Wolf!.

MOTHER: You've got a gun, he doesn't have a gun. And besides he's fast asleep.

HUNTER: Right. I'm in the perfect position to blast the biggest beast in the forest with the flick of a finger.

MOTHER: Let me cut Little Red from his belly first.

HUNTER: The Big Bad Wolf is mine. Oh yes. Oh good. Oh very good. [HUNTER sings, as MOTHER pulls RED and GRANDMOTHER from the WOLF's belly and embraces them.]

HUNTER: C'mon, Wolf. Arise and be blasted. [The HUNTER shoots several times until the entire room is blasted to bits and the stage is filled with smoke.] Got him. Probably.

EPlLOGUE RED pursues the WOLF.

RED: Please eat me again, Mister Wolf. I'll just curl into a little ball and slide right down. Let me in, please please?

WOLF: I can't eat you. I'm dead. So I've really got to be moving on.

RED: Eat me first?

WOLF: No time. Sorry.

RED: It's not fair.

WOLF: Tell me about it.

RED: So what do I do.

WOLF: Live happily ever after, I guess.

RED: Huh.
```

---

## IC-0836: Loose Knit

- Title: Loose Knit
- Author (byline): Theresa Rebeck
- Work: Complete Plays 1989-1998
- Publisher: Smith & Kraus Publishers
- Publication date as stated: March 1999
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: PAULA, MILES
- Teaser before the introduction: Yes
- Spoken words (computed): 1252
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theresa Rebeck
Book: Complete Plays 1989-1998
ISBN: 978-1575251721
Publisher: Smith & Kraus Publishers
Date (Month/Year): March 1999
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: It’s the natural state of existence. Thee has always been and always will be a hierarchy of power . . . Men vs women; white vs black, logical politics vs psychological reasoning . . . The sooner she accepts it the more content she will be . . . Tonight is the night to open her eyes.

ACTRESS: Hmmph! Some say that opposites attract, but on this particular blind date; the attraction quickly fades. Let’s get it over with . . . .

Loose Knit by Theresa Rebeck
```

### Performance text (classify this)

```text
Character: Paula (African American) & Miles (Caucasian): a couple on a blind date, 30s

Setting: A sushi restaurant, the present

PAULA: I've never seen them do that before.

MILES: Excuse me?

PAULA: I've never seen a waiter serve sushi like that. Like an offering. It's quite - remarkable.

MILES: I know. It's a little embarrassing. They call it the Imperial Feast, and the show comes with it. Sort of like those waiters who sing to you in pizza joints.

PAULA: I didn't think you went to pizza joints.

MILES: I don't. I come here. (He starts to serve her.)

PAULA: I hope you don't mind my asking, but don't you find this all a bit. . . overstated?

MILES: Don't you like sushi? I love sushi.

PAULA: That's not what I meant. It's just, most people I know would be uncomfortable with the politics of all this. I mean, I've had a wonderful time tonight; meeting the governor was really exciting, and the opening at the Whitney was nothing short of dazzling. But to tell the truth, I'm beginning to find this all a little unnerving.

MILES: Really? How so?

PAULA: Well. you know, all of it together is so - all right. Your air of patronage, the subservience of everyone in the restaurant, your car - I mean don't you guys read the newspaper? This sort of thing is going out of style.

MILES: Do you really think so?

PAULA: Yes. I do.

MILES: I think you'd be surprised. The imperialistic structures which seem to disturb you so much have stood at the heart of the American culture for centuries. In fact, these structures, and the assumptions they are built upon, are the very things which have made culture possible. In America and throughout the world.

PAULA: Well, that may be, but

MILES: Here, I think you'll appreciate this; it's a combination of abalone, salmon roe and mahi mahi. Only two people in the world know how to make it. It's exquisite, really.

PAULA: Thank you. (He places it on her plate and hands it to her, then makes a note in his notebook. As he interviews her, he continues to make notes.) What are you doing?

MILES: Just making a few notes to myself, that's all. It's a business habit. Annoying but harmless. I picked it up from my father.

PAULA: (Friendly.) Really? What was he like?

MILES: No, no, no. I was warned about this. You're famous for this. No prying about my parents until the second date.

PAULA: You can't blame a girl for trying.

MILES: (Laughing.) I hope you don't mind my saying so, Paula, but this is the first time I've dated a woman of color. I find it quite stimulating.

PAULA: Really?

MILES: Don't you think so?

PAULA: Well, I've dated white men before.

MILES: So the novelty's worn off.

PAULA: I guess.

MILES: (He writes this down.) Do you have many white friends?

PAULA: Yes. Do you?

MILES: Well, it's less of an issue for me, isn't it?

PAULA: You tell me.

MILES: (Laughing.) Therapists. All I meant was, clearly, it's important for blacks to assimilate themselves into the high culture. Which you seem to have accomplished admirably.

PAULA: What?

MILES: An attractive black woman achieves a position of authority in a predominantly white profession? That looks like assimilation to me.

PAULA: Yes, well, just for the record, I'm not particularly interested in being assimilated into the "high" culture.

MILES: You're not?

PAULA: No. Most of my "friends" are black. And, as you may or may not realize, my family is black. You might want to write that down, too.

MILES: Do you see them often?

PAULA: Yes. I do.

MILES: How often?

PAULA: Often enough.

MILES: And your "black friends?" How often do you see them?

PAULA: I don't keep track of how often I - .

MILES: And your white friends? How often do you see them?

PAULA: Often.

MILES: More often than you see your black friends?

PAULA: (Pause, cold.) Maybe.

MILES: That's the beauty of America, isn't it? Social mobility. (He writes this down.)

PAULA: Okay. What's going on here?

MILES: We're trying to get to know each other.

PAULA: Is that what we're doing?

MILES: Don't you want to know me, Paula? Because I find you fascinating.

PAULA: You're pretty fascinating yourself, Miles.

MILES: Thank you. So. You're a psychologist How many patients do you have? (Beat. Cautiously, Paula decides to answer.)

PAULA: They're not patients, they're clients.

MILES: White?

PAULA: Would it make a difference if they were?

MILES: You tell me. You're the one who doesn't want to be assimilated.

PAULA: (Pause.) Yes. Most of them are white.

MILES: Do you like them?

PAULA: What is that supposed to mean?

MILES: It's a simple question.

PAULA: No, it's not

MILES: I was just wondering how it felt to have white people come in and complain to you all the time.

PAULA: It feels just fine.

MILES: I think you're being coy.

PAULA: And I think you're attacking me.

MILES: I'm just trying to get to know you, Paula. And I really am interested in the whole therapeutic enterprise.

PAULA: Then maybe you should try it. I know a couple of people who might be able to help you with this notebook thing.

MILES: (Smiling a little.) I'll think about it. So, how long, on the average, do you work with any given client? One year? Two? Five? Ten?

PAULA: Yes.

MILES: Have they gotten better?

PAULA: Oh, my God. . .

MILES: Is that a delicate question? I'm sorry. I just don't understand why someone would need your services for ten years. I mean, it's a treatment, right? What good is a treatment if it doesn't make you better?

PAULA: (Steely.) Well, Miles, some people have been terribly damaged by life. Their souls have been - wounded, whether by their family, or events, or just the world

MILES: Well, Paula, I'm sure you're good at what you do, but I'm not convinced that talking to you is going to heal my soul or even make me a successful member of society. I've just never understood why anyone thinks that discussing their problems will make them go away.

PAULA: No one thinks that.

MILES: Don't they?

PAULA: No.

MILES: I thought they did.

PAULA: Well, and so what if they do? Sometimes we all need someone to talk to just to - to get a perspective on things. The world's a hard place. Once in a while, even the best of us needs an ear, and a little shot of compassion. Is that so awful?

MILES: But you don't provide compassion. You provide a service.

PAULA: I also provide compassion.

MILES: If you require a person to pay for it, is it still compassion?

PAULA: Why are you attacking me?

MILES: Why do you see this as an attack? On the contrary, I have nothing but admiration for the shrewdness of your whole enterprise. You convince people they're dependent on you for their happiness, then you charge them for that dependency. It's brilliant.

PAULA: That is not what I do!

MILES: Of course not. I'm sorry if I touched a nerve. (He writes.) Have you tried the eel?

PAULA: No.

MILES: You should. (Pause.) Go ahead, try it. (Pause.) Try it. (She reaches for it. He smiles.)

PAULA: All right, Miles. All right. I think we've talked about me quite enough for one evening. I'd like to hear about you. Why don't you tell me what kind of dreams you have?

MILES: You're interested in my dreams?

PAULA: Very.

MILES: (Pause.) All right. (Pause.) There's one I have where I'm in my office above the city, and there's a document in the computer that I can't get out. So I look in my desk for the key to the computer and it looks like a knife, or a letter opener; it's quite sharp, but just as I'm about to put it into the computer a white rat comes along and steals it out of my hand. So I chase her up and down the halls, and then I hear her behind me, so I turn, and hold out my hand, and the knife is in it - the key, I mean - but it's a different rat, a black rat, only now she's covered in blood because I've stabbed her. Because I had the key all along. (Pause.) Actually, I've had that dream several times.

PAULA: Really.

MILES: Do you know what it means?

PAULA: No. No. I have no idea. (She stares at him. Blackout.)
```

---

## IC-0837: Los Vendidos (The Sellouts)

- Title: Los Vendidos (The Sellouts)
- Author (byline): Luis Valdez
- Work: Luis Valdez Early Works (Pg 40-52)
- Publisher: Dec 1990
- Publication date as stated: 978-1558850033
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR, ACTRESS, SANCHO, SECRETARY, FARMWORKER, JOHNNY, REVOLUCIONARIO, MEXICAN-AMERICAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1448
- Already set (do not supply): none

### Source block (context only)

```text
Author: Luis Valdez
Book: Luis Valdez Early Works (Pg 40-52)
ISBN: Arte Publico Press
Publisher: Dec 1990
Date (Month/Year): 978-1558850033
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Any particular type? Ay caramba! ACTRESS: Los Vendidos (The Sellouts) by Luis Valdez
```

### Performance text (classify this)

```text
NOTE: This selection should be performed by students of Mexican descent

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles:

ACTOR: Honest Sancho, Farmworker, Mexican-American

ACTRESS: Secretary, Johnny, Revolucionario

HONEST SANCHO’s Used Mexican Lot and Mexican Curio Shop. Three models are on display in HONEST SANCHO ’s shop. HONEST SANCHO is moving among his models, dusting them off and preparing for another day of business.

SANCHO: (Pg 40-52) Bueno, bueno, mis monos, vamos a ver a quién vendemos ahora, ¿no?

(Well, well, my monkeys, let's see who we sell to now, right?) (To audience.) I’m Honest Sancho and this is my shop. All I need now is a customer. (woman enters) Ay, a customer!

SECRETARY: Good morning, I’m Miss Jimenez from. . .

SANCHO: Ah, una chicana! Welcome, welcome Señorita Jiménez.

SECRETARY: (Anglo pronunciation.) JIM-enez. My name is Miss JIM-enez. Don’t you speak English? What’s wrong with you?

SANCHO: Oh, nothing, Señorita JIM-enez. I’m here to help you.

SECRETARY: That’s better. As I was starting to say, I’m a secretary from the Governor’s office, and we’re looking for a Mexican type for the administration.

SANCHO: Well, you come to the right place, lady. This is Honest Sancho’s Used Mexican Lot, and we got all types here. Any particular type you want?

SANCHO: . . . Any particular type you want?

SECRETARY: Yes, we were looking for somebody suave … debonaire. Dark. But of course, not too dark. Perhaps, beige.

SANCHO: Beige, just the tone.

SECRETARY: One more thing. He must be hard-working.

SANCHO: That could only be one model. Step right over here, lady. This is our standard farmworker model. Take special notice of his 4-ply Goodyear huaraches, made from the rain tire. This wide-brimmed sombrero is an extra added feature; keeps off the sun, rain and dust. And our farmworker model is friendly. Muy amable. Watch. (Snaps his fingers.)

FARMWORKER: (Lifts up head.) Buenos días, señorita. (His head drops.)

SANCHO: But his most attractive feature is that he’s hardworking. Let me show you. (Snaps fingers. FARMWORKER stands.)

FARMWORKER: ¡El jale! (He begins to work.)

SANCHO: As you can see he is cutting grapes. He also picks cotton. (Snaps. FARMWORKER begins to pick cotton.) That’s his slow speed for late in the season. Here’s his fast speed. (Snap. FARMWORKER picks faster.)

SECRETARY: Chihuahua … I mean, goodness, he sure is a hard worker. But is he economical?

SANCHO: Economical? Señorita, you are looking at the Volkswagen of Mexicans. Pennies a day is all it takes. One plate of beans and tortillas will keep him going all day.

SECRETARY: What about storage?

SANCHO: No problem. You know these new farm labor camps? They were designed with our model in mind. Five, six, seven, even ten in one of those shacks will give you no trouble at all. And here’s an added feature: every year at the end of the season, this model goes back to Mexico and doesn’t return, automatically, until next Spring.

SECRETARY: How about that. But tell me, does he speak English?

SANCHO: Bueno … no, pero he has other features …

SECRETARY: No! He just won’t do!

SANCHO: Okay, okay, pues. We have other models.

SECRETARY: I hope so. What we need is something a little more sophisticated. An urban model.

SANCHO: Ah, from the city! Over here in this corner of the shop is exactly what you’re looking for. Introducing our new 1969 JOHNNY PACHUCO model! Streamlined. Built for speed, low-riding, city life. Let me just turn him on. (Snap. JOHNNY walks to stage center with a PACHUCO bounce.)

SECRETARY: What was that?

SANCHO: That, señorita, was the Chicano shuffle.

SECRETARY: Okay, what does he do?

SANCHO: Anything and everything necessary for city life. For instance, survival: he knife fights. (Snaps. JOHNNY pulls out a switchblade and swings at SECRETARY. SECRETARY screams.)

SANCHO: And here’s a feature no city model can be without. He gets arrested, but not without resisting, of course. (Snap.)

JOHNNY: En la madre, la placa. I didn’t do it! I didn’t do it! (JOHNNY turns and stands up against an imaginary wall, legs spread out, arms behind his back.)

SECRETARY: Oh no, we can’t have arrests! We must maintain law and order.

SANCHO: But he’s bilingual. He speaks English! He’s economical. Nickels and dimes. You can keep Johnny running on hamburgers, Taco Bell tacos, Lucky Lager beer . . .

SECRETARY: Mr. Sancho, I don’t think you quite understand what we need. What we need is something that will attract the women voters. Something more traditional.

SANCHO: Ah! (He smiles meaningfully.) Step right over here, señorita. Introducing our standard Revolucionario type. As you can see, he is well-built, sturdy, durable.

SECRETARY: What does he do?

SANCHO: You name it, he does it. He rides horses, stays in the mountains, crosses deserts, plains, rivers, leads revolutions, follows revolutions, kills, can be killed, serves as a martyr, hero, movie star. Listen to this. (Snap.)

REVOLUCIONARIO: (Scream.) ¡Viva Villaaaaa!

SECRETARY: That’s awfully loud.

SANCHO: He has a volume control. (He adjusts volume. Snap.)

REVOLUCIONARIO: (Mousey voice.) Viva Villa.

SANCHO: And even if you didn’t see him in the movies, perhaps you saw him on TV. He makes commercials. (Snap.)

REVOLUCIONARIO: Is there a Frito Bandito in your house?

SECRETARY: Oh yes, I’ve seen that one!

SANCHO: And finally, there is one outstanding feature about this model I know the ladies are going to love: he’s a genuine antique! He was made in Mexico in 1910!

SECRETARY: Made in Mexico? Mr. Sancho, I thought he was an American product. I’m sorry. We can’t buy anything but American made products. We need Mexican models, such as these, but it’s more important that he be American.

SANCHO: Wait a minute! Mexican but American? Mexican but … (A sudden flash.) American! Yeah, I think we’ve got exactly what you want. He just came in today! Give me a minute. (He exits and brings out the MEXICAN-AMERICAN model, a clean-shaven middle class type in a business suit, with glasses.) Introducing our new 1970 Mexican-American! Ta-ra-ra-raaaa!

SECRETARY: (Impressed.) Where have you been hiding this one?

SANCHO: He just came in this morning. Feast your eyes on him! Sturdy U.S. Steel frame, streamlined, modern. As a matter of fact, he is built exactly like our Anglo models, except that he comes in a variety of darker shades: naugahide, leather or leatherette.

SECRETARY: Naugahide.

SANCHO: Well, we’ll just write that down. Yes, señorita, this model represents the apex of American engineering! He is bilingual, college educated, ambitious! He is intelligent, well-mannered, clean. Did I say clean? (Snap. MEXICANAMERICAN raises his arm.) Smell.

SECRETARY: (Smells.) Old Sobaco, my favorite.

SANCHO: (Snap. MEXICAN-AMERICAN turns toward SANCHO.) Eric? (To SECRETARY.) We call him Eric García. (To ERIC.) I want you to meet Miss JIM-enez, Eric.

MEXICAN-AMERICAN: Miss JIM-enez, delighted to make your acquaintance. (kisses her hand.)

SECRETARY: Oh, my, how charming! How about boards, does he function on boards?

SANCHO: You name them, he is on them. Parole boards, draft boards, school boards, taco quality control boards . . .

SECRETARY: Does he function in politics?

SANCHO: Señorita, you are looking at a political machine. Have you ever heard of the WAR ON POVERTY? That’s our model! Not only that, he makes political speeches.

SECRETARY: May I hear one?

SANCHO: With pleasure. (Snap.) Eric, give us a speech.

MEXICAN-AMERICAN: Mr. Congressman, Mr. Chairman, members of the board, honored guests, ladies and gentlemen. (SANCHO and SECRETARY applaud.) Please, please. I come before you as a Mexican-American to tell you about the problems of the Mexican. The problems of the Mexican stem from one thing and one thing only: he’s stupid. He’s uneducated. He needs to stay in school. He needs to be ambitious, foward-looking, harder-working. He needs to think American, American, American! God bless America! God bless America! God bless America! (He goes out of control. SANCHO snaps frantically and the MEXICAN-AMERICAN finally slumps forward, bending at the waist.)

SECRETARY: Oh my, he’s patriotic too! What about upkeep? Is he economical?

SANCHO: Well, no, I won’t lie to you. The Mexican-American costs a little bit more, but you get what you pay for. He’s worth every extra cent. You can keep him running on dry Martinis, Langendorf bread …

SECRETARY: Apple pie?

SANCHO: Only Mom’s. Of course, he’s also programmed to eat Mexican food at ceremonial functions, but I must warn you, an overdose of beans will plug up his exhaust.

SECRETARY: How much do you want for him?

SANCHO: Well, I tell you what I’m gonna do. Today and today only, because you’ve been so sweet, I’m gonna let you drive him off the lot for $15,000.

SECRETARY: Fifteen thousand dollars? For a Mexican!!!!

SANCHO: Mexican? What are you talking about? This is a Mexican-American! You want quality, but you gotta pay for it! This is no cheap run-about. He’s got class!

SECRETARY: Okay, I’ll take him. (Hands Sancho the $$ in cash) The Governor is having a luncheon this afternoon, and we need a brown face in the crowd. How do I drive him?

SANCHO: Just snap your fingers. He’ll do anything you want. (SECRETARY snaps. MEXICAN- AMERICAN steps forward.)

MEXICAN-AMERICAN: ¡Raza querida, vamos levantando armas para liberarnos de estos desgraciados gabachos que nos explotan! (Secretary snaps and model freezes)

SECRETARY: What did he say?

SANCHO: Something about taking up arms, killing people, etc.

SECRETARY: He’s not supposed to say that!

SANCHO: Look, lady, don’t blame me for bugs from the factory. He’s your Mexican-American, you bought him, now drive him off the lot! Try snapping another finger. (SECRETARY snaps. MEXICAN-AMERICAN comes to life again.)

MEXICAN-AMERICAN: ¡Basta! ¡Basta! ¡Viva la raza! ¡Viva la causa! ¡Viva la huelga! ¡Chicano power! (The MEXICAN-AMERICAN turns toward the SECRETARY, who gasps, backs up and runs out of the shop screaming. All freeze. After a few seconds of silence, the JOHNNY PACHUCO moves and stretches. SANCHO stays frozen to his spot.)

JOHNNY: Man, that was a long one, ese. (Others agree with him.)

FARMWORKER: (moves and stretches) How did we do?

JOHNNY: Pretty good, look at all that lana, man! (He goes over to SANCHO and removes the money from his hand. SANCHO stays where he is.) We keep this up, we’re going to be rich.

FARMWORKER: They think we’re machines.

REVOLUCIONARIO: (moves and stretches) Burros.

JOHNNY: Puppets.

MEXICAN-AMERICAN: The only thing I don’t like is how come I always get to play the Mexican- American?

JOHNNY: That’s what you get for finishing high school.

FARMWORKER: How about our wages, ese?

JOHNNY: $3,000 for you, $3,000 for you, $3,000 for you and $3,000 for me. The rest we put back into the business. (Notices Sancho, still frozen) What about our salesman? I think he needs an oil job.

REVOLUCIONARIO: Leave him to me. (REVOLUCIONARIO goes over to SANCHO, removes his hat, lifts him up and throws him over his shoulder. SANCHO hangs loose, lifeless. To audience.) He’s the best model we got! ¡Ajúa!
```

---

## IC-0838: Lures

- Title: Lures
- Author (byline): Jeanette D. Farr
- Work: Ten 10-Minute Plays: Volume II
- Publisher: Black Box Press
- Publication date as stated: July 2008
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MAUREEN, BOB
- Teaser before the introduction: No
- Spoken words (computed): 1618
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jeanette D. Farr
Book: Ten 10-Minute Plays: Volume II
ISBN: 0615240003
Publisher: Black Box Press
Date (Month/Year): July 2008
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Instant messaging on the computer has become the phone for kids today. Children spend hours chatting online with their friends, and sometimes with strangers.

ACTOR 2: A recent study found that one in five children online is approached by a sexual predator, a predator who may try to set up a face-to-face meeting.

ACTOR 1: In Lures by Jeanette D. Farr just such a meeting has been arranged.

ACTOR 2: This time however, the child (a young boy) is actually his mother, Maureen, who takes it upon herself to put a stop to the stalking and abuse of her son.

ACTOR 1: Entrapment? Or a reasonable response to protect children in an unsafe world?

TOGETHER: Lures by Jeanette D. Farr

[Wilderness. A man 30—40 stands in the cold near a lake. He has a tackle box next to him, hands in his pockets. He seems either cold or nervous, we really can’t tell. After a moment, a woman approaches. She is dressed like a mom – in a warm-up suit and tennis shoes. Her hair is in a ponytail – not a neat one by any means. She catches his eye. He starts to leave.]
```

### Performance text (classify this)

```text
MAUREEN: Don’t leave. On my account, I mean. I am supposed to meet someone here.

BOB: I haven’t seen anyone.

MAUREEN: You waiting for someone?

BOB: Yeah… My son. He’s fishing. We’re fishing.

MAUREEN: Oh. A good spot, huh? To fish I mean.

BOB: That’s what they say.

MAUREEN: Catch anything?

BOB: Nah. Too cold, probably.

MAUREEN: Your first time?

BOB: Fishing?

MAUREEN: Here. Fishing here.

BOB: Sure is pretty. You zone out after a while looking at it all. Not much to see anymore, it’s getting dark. Nice chatting, though. So long.

MAUREEN: What about your son?

BOB: What? Oh. I’m sure he went back to the car already.

MAUREEN: The burgundy van, right?

BOB: Do I know you?

MAUREEN: I would think you would’ve gone with him. Your son.

BOB: Do you need some help finding the road?

MAUREEN: I would go places with my son. You just can’t be too careful these days. The people out there.

BOB: I could go back, call someone for you.

MAUREEN: You just don’t strike me as a parent.

BOB: I told you, I’m here with— Fuck it. I’m outta here.

MAUREEN: I used to think we could help you sick fuckers, that somehow pedaphilia was curable.

BOB: Look, lady, I don’t know you – can you let me by?

MAUREEN: Cut the shit! [She threatens him with a baseball bat.] Give me your shoes.

BOB: I told you, my son…

MAUREEN: You do know me. Lilpete4673. Teenspace, right? Well guess what—you thought it was him, this is what you get.

BOB: I’m here fishing—

MAUREEN: Give me your goddamned shoes!

BOB: My son went to pee, he’ll be back, you’ll see.

MAUREEN: What’s his name? Call him.

BOB: I’m sure as hell not going to tell you anything about my son.

MAUREEN: What? You think I’m going to do something? That’s a laugh. Sit down! Admit why you are here. Tell me what you were going to do.

BOB: Why are you doing this?

MAUREEN: I’m trying to get in your sick head. You’re gonna tell me he is your first? Why any human being on the planet would lure innocent children to—

BOB: I was fishing! [She hits him in the back with the baseball bat.]

MAUREEN: You don’t even have a fishing pole.

BOB: You have a bat, but we’re not exactly playing baseball, are we? [She whacks him again. Lower. His knees buckle. He’s down on the ground.] He took it back with him. We had some things to load. He was cold.

MAUREEN: Give me your jacket. (yelling) NOW!

BOB: It’s freez— [HE complies, not sure if he’s going to get whacked again. MAUREEN looks in all pockets.]

MAUREEN: Where is it?

BOB: Where is what?

MAUREEN: What you promised me. Him. What you promised him. A baseball card. Where is it?

BOB: I don’t—

MAUREEN: (reciting) I like to fish, maybe we could meet sometime. I told – He told you he likes baseball.

BOB: Who!?

MAUREEN: My son. Look. You thought you were talking to an eight year old, right? But it was me, instead. Your worst nightmare. A parent. You’re lucky it’s me and not the cops. You know what they do to you in prison. Huh? I’m not that cruel.

BOB: Please, lady. I think you broke a rib. Calm down, would ya?

MAUREEN: You told him you would bring him a vintage Babe Ruth when you met. Where the fuck is it?

BOB: You got the wrong guy, lady. I’m sorry if your son has been downloading porn or something while you’re at PTA or getting your nails done. Feel guilty – fine by me – but don’t you pull a Babe Ruth just because you’re a bad parent and you think something’s going on with me and your son – [She raises the bat and gets ready to swing. He catches it and pulls her down. He puts the large end of the bat to her throat. He has the upper hand now.] What do you think now, huh? How do you like it, huh you crazy bitch?!

MAUREEN: My son was raped with his own baseball bat. [BOB backs off, still holding on to the bat.] (breaking down) You don’t talk about my son. You don’t have any right to even think about my son.

BOB: (Looking at the bat, horrified.) Lady – I’m sorry. You got the wrong guy.

MAUREEN: Pete was only 78 pounds. A grown man versus 78 pounds. He fought like hell to get that monster offa him.

BOB: There was a person here earlier. Shady looking guy. He saw me and my son and left. Probably got spooked. Can’t imagine those types would do anything with people around. [Pause.] You okay?

MAUREEN: (stunned) Oh, god. I’m sorry. Are you okay? [SHE approaches him, reaching out. He’s spooked and pulls away quickly.] I’m not. I’m not myself.

BOB: I’d hate to meet the real you then. [MAUREEN and BOB share a nervous laugh.]

MAUREEN: Humor. My therapist says that laughing is good. A release of chemicals.

BOB: Funny—great. Can you get me a stretcher please?

MAUREEN: Oh, god. Are you really hurt?

BOB: I’m fine. At least I think I am. Just, I don’t think I’m ready to give this back yet. You know my boy has to be about the same age. In the Boy Scouts. That’s why I wasn’t so worried about him, you know? He’s pretty good at finding his way. Likes to be independent. How old is your boy?

MAUREEN: He was eleven when he… It first happened when he was only eight years old. After that was when the real torture began. Once was enough… enough for anyone.

BOB: You should tell someone. I could talk to him, if you want.

MAUREEN: It doesn’t matter anymore.

BOB: Of course it matters. You have to.

MAUREEN: They knew. We did. Still too much for an eleven year old, thinking about girls, and dating. I couldn’t even count the nightmares he had about it. Or the ones he didn’t tell me about. He loved baseball. So he – (can’t bring herself to say it) Most Moms would be pissed at their kid for ending it. I don’t blame him, you know. Figured the best thing for him was to leave this world.

BOB: I’m sorry for your loss.

MAUREEN: Thank you.

BOB: You and your husband must’ve been mad as hell.

MAUREEN: He was overseas serving at the time. Left the anger and me in charge of dealing with it all. Paul became obsessed with e-mails, then websites, then chatrooms. Seems so impersonal to me. But he said it was the best way to make friends.

BOB: I served in the Gulf.

MAUREEN: Oh god. If I knew then…

BOB: Cut yourself some slack. I don’t judge. Can’t compare to what you went through.

MAUREEN: How long did you serve?

BOB: Eight months in the Marine Corps. Kids don’t think of you as much of a hero these days. Not like they used to.

MAUREEN: Pete always thought his father was a hero. We just… we just couldn’t get past it his father and I. Or I couldn’t get past it. We just sort of grew apart after Pete…after he…

BOB: I get it. There are places, you know. To get help.

MAUREEN: Oh, shit. You think I’m going to off myself now, is that it?

BOB: It helps to talk about it, right? I’m just saying that maybe you should think about getting help.

MAUREEN: They already got me on plenty.

BOB: What’s their cocktail for ya? Zoloft?

MAUREEN: Atavan. Sometimes Xanax. Helps me sleep. That’s when it’s the worst.

BOB: Yep. I remember. I’m off it all now. But I don’t know how I would’ve done without it after I came back. Some guys aren’t so lucky. Do worse. Stuff without a prescription.

MAUREEN: My husband wouldn’t talk about what happened there or here. Let it go, he said. Forget it. He didn’t think that back home things were big enough fish to fry.

BOB: Fish. Geez. My son must really be freaked by now. Can I? [BOB points to the shoes.]

MAUREEN: Oh, god. Sure. God. I’m sorry.

BOB: I told him I would watch the sunset and then we’d go. (Putting on shoes) You going to be okay out here?

MAUREEN: You know my Petie, he always hated when I called him Petie, but I told him it didn’t matter ‘cause he was my Petie—he used to like coming here. It’s why I suggested it to the creep in the first place. Figured if I caught him, it might be some sort of tribute.

BOB: I’m sure he’s long gone by now.

MAUREEN: Whether I catch him – or someone like him. I don’t care. I think I’d feel better. Hell, I don’t know. It was my therapist who suggested visiting some of the places he liked to help with the grieving process.

BOB: I hope you find the bastard that e-mailed him…you. Be careful. You could get hurt.

MAUREEN: They’re cowards. Why else would they pick on children? Besides, I think I can defend myself.

BOB: I have no doubt about that. You’re batting a hundred.

MAUREEN: Still sore? What am I thinking? Of course you are.

BOB: I don’t judge. Besides nothing some Aspirin won’t help. From Ativan to Aspirin. Hey, there’s something to look forward to.

MAUREEN: You are kind, you know that? Nobody’s been this kind, really.

BOB: We’re human beings after all. All put here for the same thing, right?

MAUREEN: To fight like hell.

BOB: Hoo-Rah! You do have quite a swing there. You should have your own baseball card…[An awkward laugh. Glad it’s over.]

MAUREEN: Maureen.

BOB: Take care of yourself, Maureen.

MAUREEN: Do the same. [Bob finds the quickest way out of the forest he can. A little smile back on the way out. MAUREEN notices the tacklebox. Thinks for a moment, then…] Hey – Wait a minute – you- [MAUREEN is curious. She contemplates the quiet moment. She opens the tacklebox. There are fishing lures. She breathes a sigh of relief. Fingering the lures, she pulls out a magazine. This one she is not so thrilled about. She pulls out a baseball, and finally a baseball card. She takes her bat and clutches it tightly as lights fade.]
```

---

## IC-0839: The M Word

- Title: The M Word
- Author (byline): Alan Ball
- Work: Five One-Act Plays
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: WOMAN, MAN
- Teaser before the introduction: No
- Spoken words (computed): 1414
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alan Ball
Book: Five One-Act Plays
ISBN: 978-0822213680
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: The thought of quantifying and qualifying your relationship with your husband-or wife-to-be may sound ludicrous.

ACTOR: However, marriage is a formal agreement into which you are both entering. A vow is no different from a contract.

ACTRESS: And this venture is the most adventurous, daring and permanent of all.

ACTOR: By putting it into a business plan, couples are forced to agree upon certain terms and conditions, ways of handling issues and what happens when one does not fulfill his or her obligations.

ACTRESS: In one form or another, these things should be discussed by the time you decide to even discuss . . .

TOGETHER: The M Word by Alan Ball.

A n office. A well-groomed Woman in a business suit sits at her desk, working furiously. Elsewhere in the office is a table or file cabinet on which sits a pitcher of water and two empty glasses. A Man in a business suit appears at the door, carrying a large, official-looking document and a personal notebook. He knocks to get her attention.
```

### Performance text (classify this)

```text
WOMAN: Yes?

MAN: Are you terribly busy? This won't take long. (She puts her work aside and motions him to come in.)

WOMAN: I can give you ten minutes. I have a very important presentation this afternoon.

MAN: Don't worry. I'm catching the three o'clock shuttle to D.C., which means I'll need to be out of here by - (He performs some calculations on his wristwatch.) - one forty-eight at the absolute latest.

WOMAN: I really admire a man who allocates his time efficiently.

MAN: I'll get right to the point. We've been working together for six months, three days, fourteen hours and _ (Checks his watch again.) - twenty-two seconds. During that time, I believe we have grown to enjoy each other's company -

WOMAN: I wouldn't necessarily say enjoy ...

MAN: Really.

WOMAN: It implies a level of passion we have yet to achieve.

MAN: Oh, well, of course. I didn't mean to paint this as an emotional thing.

WOMAN: I'm glad to hear you say that.

MAN: On the contrary, one of the things I value in our relationship is the complete lack of spontaneity, which virtually eliminates any element of surprise. I know in advance how you're going to react, and I'm able to plan my strategies accordingly.

WOMAN: And I can predict your strategies without fail, thus being able to manipulate you effortlessly, without your even knowing it. There is real security in that.

MAN: We have a lot to offer each other.

WOMAN: We keep each other on our toes.

MAN: Shall I mention the M word now?

WOMAN: Oh, no. Much too soon. You'd do better to keep the suspense going for a little while longer.

MAN: I admire your coaching skills. And I am secure enough in my masculinity not to be threatened by your criticism.

WOMAN: I appreciate that. (Pause.)

MAN: I need a woman to take to the Hamptons this summer. You're quite presentable in a bathing suit _

WOMAN: Thank you.

MAN: - and could arouse feelings of jealousy in other men with whom I compete for advancement in my social circle. One question: are you interested in producing offspring?

WOMAN: My biological clock is ticking like mad.

MAN: Have you given any thought as to what qualities you seek in a potential procreative partner?

WOMAN: Any man who is straight, has a steady job and is not a mass murderer looks pretty good. Of course, these are preliminary projections. I would need to conduct a much more extensive study before actually undertaking such a challenging project.

MAN: Understood.

WOMAN: And yourself? What are your feelings on the issue?

MAN: Well, of course I want children.

WOMAN: Why?

MAN: Oh, many reasons. First, they're quite a prestige item these days.

WOMAN: Uh-huh.

MAN: Second, they would greatly reinforce my own and others' notions of my virility.

WOMAN: Uh-huh.

MAN: Third, I have many unresolved issues with my dead father that I could work out with a son of my own.

WOMAN: Uh-huh.

MAN: And fourth, I've always enjoyed pets.

WOMAN: What are your feelings on shared child-rearing duties?

MAN: Ah ... I'm open to the concept. I certainly plan to budget frequent parcels of quality time for the kids, but ... I guess I'm not sure what you mean exactly by shared child-rearing duties. Would you care to elaborate?

WOMAN: Will you agree to a quota system that ensures even distribution of diaper-changing responsibilities? Are you willing to begin networking immediately in order to improve a child's chances of getting into an Ivy League pre-school? Are you willing to undergo sensitivity training yourself in order to become a more nurturing parent and role model, thus alleviating some of the historical burden of which mothers carry a disproportionate share? (Pause.)

MAN: Can I think about that?

WOMAN:Of course, I don't think we have to come to any decision today.

MAN: Great. (Checks his pad) As far as economic considerations go, I am confident that our combined income would be formidable, and we can continue our futile attempt to fill the void in our lives with overpriced material goods.

WOMAN: That's all well and good, but I think that if we work together on this, using a mixture of jurisprudence and selective risk-taking, we should be able to make the leap from upwardly mobile to wealthy before we're forty-five.

MAN: Oh, I plan to become a millionaire before I'm forty.

WOMAN: Really. That doesn't give you much time.

MAN: I'm aware of that.

WOMAN: May I ask what your contingency plans are?

MAN: I'm considering several options, including suicide in the event of not achieving my goal.

WOMAN: An aggressive approach.

MAN: I work best when I'm under pressure.

WOMAN: Hmm. I would be forty myself at that time, still young enough to embark on a new life partnership. Trouble is, most of the men whom I would deem appropriate partners will be just beginning their mid-life crises, and will therefore be interested only in very young women who make them feel less anxiety about their own mortality. On the other hand, I could do a Cher thing, and take as a lover a man half my age, involved in some kind of manual labor. And preferably not too bright. Hmm. I doubt if such a thing would go over well here at work, but ... if you have a good life insurance policy I could stop working altogether. Maybe. Hmm. I'll need to think about this some more.

MAN: Of course.

WOMAN: By the way, have you planned your own mid-life crisis yet?

MAN: Not fully, but I have settled on a basic approach.

WOMAN: Would you mind briefing me on it?

MAN: Not at all. (Flips through pages.) My target age is fifty, give or take a few years. I plan to start small, an expensive foreign sports car, some flashv clothes, a harmless infatuation with a much younger woman, not acted upon

WOMAN: Such restraint. I’m impressed.

MAN: Well, you might want to withhold judgment, because then I thought I would move up to a serious affair of frightening intensity with an emotionally disturbed model or actress, leading to a temporary separation from my wife and family, several humiliating social episodes, some random drunkenness and maybe even a brief drug problem, all culminating in a life-or-death struggle for my very soul.

WOMAN: That's awfully dramatic.

MAN: I believe at that point, having worked as hard as I plan to, I will deserve it.

WOMAN: I could score some major sympathy points, as well as impressing others with my ability to hold up under such a scandal. My dignity index would soar.

MAN: Both men and women will look down upon me but secretly admire my impetuous and adventurous nature. Of course, if everything goes according to plan, I will realize the folly of my ways, and return to you with a new level of maturity, humility and respect for all that you offer me.

WOMAN: I, of course, will have suffered tremendously, and through your guilt will be able to get whatever I want from you until you die.

MAN: Naturally.

WOMAN: It's an attractive scenario ... but I'm worried about the effect it might have on the children.

MAN: Negligible. They should be hopelessly neurotic by that point, anyway.

WOMAN: You think?

MAN: Definitely. After years of private school, under constant pressure to succeed? They will be addicted to overachievement and equipped with completely unrealistic standards and unattainable goals.

WOMAN: Just like us!

MAN: Ulcers before they finish adolescence, you mark my words.

WOMAN: You're certainly optimistic.

MAN: You have to think big.

WOMAN: I must admit, I find your enthusiasm contagious.

MAN: Then shall I bring up the M word?

WOMAN: I think you may proceed.

MAN: Well. I propose that you and I consider getting mar - (He is unable to say it.) Excuse me. I must have something in my throat. (Indicating water.) May I? (He pours himself a glass of water and drinks.) Let's try that again. I propose that you and I get mar - (Again, he is unable to say it.) Excuse me. (He steps aside, and goes through some sort of athletic warm-up ritual.) I am stronger than I've ever been and getting stronger every day. I am stronger than I've ever been and getting stronger every day. I am stronger than I've ever been and getting stronger every day. (Some intense breathing.) I can do this. I am capable of this. I can argue persuasively, I can drive my point home, I can sell anything to anybody. (He takes a deep breath and the faces the Woman, who has resumed working.) I'm ready now.

WOMAN: Oh. (She puts her work down and looks at him.)

MAN: I propose that we get mar - (Again, he is unable to say it.) Damn. (He pours another glass of water and douses his face with it. Blurting.) Would you like to merge? (Pause.)

WOMAN: I would consider it.

MAN: Great. (Handing her the document he entered with.) I've taken the liberty of drawing up a preliminary proposal, outlining some of the things we've talked about. I'd like for you to read it, at your convenience, and then get back to me with your feedback.

WOMAN: May I make notes on this?

MAN: Of course, it's just a draft, and I have several copies. Oh, my god. (Grabs his notebook.) Well, I hate to make a presentation and run, but I should have left thirty seconds ago. I'm really looking forward to hearing your comments on the proposal. May I call you on Monday?

WOMAN: Please do.

MAN: Okay! (He leaves. The Woman waits until he's out of earshot. She then performs a brief, frantic, savage dance of joy before returning to her work.)
```

---

## IC-0840: The Man Who Couldn’t Dance

- Title: The Man Who Couldn’t Dance
- Author (byline): Jason Katims
- Work: Take Ten: New 10-Min Plays (ed Lane & Shengold)
- Publisher: Vintage Books
- Publication date as stated: March 1997
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GAIL, ERIC
- Teaser before the introduction: No
- Spoken words (computed): 2045
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jason Katims
Book: Take Ten: New 10-Min Plays (ed Lane & Shengold)
ISBN: 978-0679772828
Publisher: Vintage Books
Date (Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
Is the inability to dance a reason to end a relationship? Will Gail and Eric discover the truth over Elizabeth's crib? The Man Who Couldn’t Dance by Jason Katims
```

### Performance text (classify this)

```text
The attic of Gail's house in Connecticut. ELIZABETH sleeps in her crib. ERIC and GAIL enter.

GAIL: Not too loud. (They walk to crib. Look in.) Eric, this is Elizabeth.

ERIC: Oh my God. She's really. . . ugly.

GAIL: What?

ERIC: The kid is like a raisin or something.

GAIL: (to ELIZABETH, whispering.) Don't listen to him Elizabeth. He's jealous. (to ERIC.) I've been wanting so much for you to meet her. It's like it would make the whole thing real or something.

ERIC: God. She's a beautiful little raisin, isn't she? It's what was behind door number two.

GAIL: What?

ERIC: I don't know. All night I haven't been able to shake this feeling. It's like I'm visiting the life I could have had. A baby. A house in Connecticut. A subscription to House and Garden.

GAIL: You won't let me outlive that one will you?

ERIC: Come on Gail. House and Garden.

GAIL: I put it in the basket in the bathroom for you, you know. I remember how frightened you used to be of bathrooms without reading material.

ERIC: Don't make me into some sort of like neurotic old boyfriend Gail.

GAIL: Are you going to deny your severe fear of bathrooms?

ERIC: Bathrooms are frightening, horrible places. Cold. Lonely. Sterile. But you should not use that to make me into some kind of little anecdote. Like a chapter of your life that was some little situation comedy. Do not mistake neurotic fears and obsessions for light comedy. Very dangerous, Gail.

GAIL: I don't want to get into a discussion like this now, Eric.

ERIC: What kind of discussion is it, and when would you like to get into it?

GAIL: A discussion about us. And never. They're waiting.

ERIC: They're fine on their own. She's just a date, Gail. A date.

GAIL: It didn't sound like that on the phone. "She's beautiful. She's intelligent. She's not hung up by society's rules." These are your words. I think you should grow up.

ERIC: Why?

GAIL: Why should you grow up? Are you asking me why you should grow up?

ERIC: Yes. I'm interested in hearing about it from someone whothinks she has.

GAIL: That is what people do. They get married. They have kids. They remember their ideals fondly. They try to stick to them in their own way. They donate to public television. They get by.

ERIC: Don't cry, Gail. Please do not cry.

GAIL: Oooh that gets me. What makes you think I'm going to cry?

ERIC: Because you regret your choices. And now you're going to cry.

GAIL: I regret my choices? Fuck you.

ERIC: I'm sorry. I said what I thought. I broke the unwritten rule between us since we broke up. I'm supposed to smile, and talk to you like I'm really interested . . .

GAIL: Oh am I glad that you are not the father of my daughter. I am so happy to not have to worry for her about your inconsistency, your stubbornness, your uncanny ability to make the most politically and philosophically interesting choices leaving yourself and your loved ones in the shit heap. Let's just spend the rest of the night playing Pictionary. All right?

ERIC: This is the fourth time tonight you brought up Pictionary. Are you forcing me to play fucking Pictionary? It's a waste of time. People sit around and solve meaningless little puzzles and form arbitrary alliances for no other reason than to pass time. Well, time is passing well enough for me without games, Gail.

GAIL: It's so goddamn easy for you.

ERIC: What?

GAIL: It's so easy for you not to play Pictionary. You're funny, verbal, provocative. Do you know how intimidated my husband is by you?

ERIC: (Change of tone.) You don't love Fred.

GAIL: What?

ERIC: You don't love Fred.

GAIL: That's it. I demand that you play Pictionary, Eric. I god damn insist.

ERIC: Why did you marry a man you didn't love?

GAIL: I never said I don't love him.

ERIC: Christ, Gail. Tell me you love him. Please.

GAIL: YOU GOT ON THAT FUCKING BOAT. The crucial point. The pinnacle time. The absolute quintessential turning point of our relationship and you're on a fucking boat to fucking Saint John.

ERIC: That has nothing to do with it.

GAIL: It's got everything to do with it.

ERIC: You make it sound like you made some kind of choice between two men. Like it was me or him.

GAIL: It was.

ERIC: It was? Come on Gail. It's a huge world. If it were a choice between me or Fred most women would just fucking shoot themselves.

GAIL: You threw it away.

ERIC: I never threw you away.

GAIL: Not me. It. Everything. Eric you're such an ass hole. Everyone's goddamn guru. Living by your values. True to yourself. The ascetic. The Twentieth Century Philosopher. Eric, I have a question for you. A real question. Why are you working on a farm? Why? It's like I'm supposed to admire you or something. I'm so sick of your untraditional paths. The Farm Boy of Bensonhurst. You're wasting your intelligence. You're wasting your intelligence to pick vegetables. There is nothing to admire about that. It's stupid.

ERIC: You're right. Why work with my hands to produce a reasonably priced source of nourishment for my fellow human beings while I could be getting fat and playing Pictionary.

GAIL: I gained four pounds. Four. Don't you dare say I'm getting fat. And there is nothing wrong with playing Pictionary, you goddamn all-knowing fool.You lost me..

ERIC: I know.

GAIL: It pisses me off. It really pisses me of[ That thing you said about me regretting my choices. At least I made a choice.

ERIC: But you do regret it.

GAIL: I love Fred, Eric. I do love him. Not like I loved you. But we have these things together. This family. This feeling. This sureness.

ERIC: I don't consider your need for structure your strongest trait.

GAIL: Look, Eric, I don't think I can have this conversation with you. I'm sorry things had to happen the way they happened. Let's go downstairs.

ERIC: Right. I'm sorry.

GAIL: You're just being yourself.

ERIC: That's what I'm sorry for. I should say good-bye to Elizabeth. Who knows when I'll see her again. (ERIC walks to the crib. He looks down. In a moment he bends over to her.)

GAIL: Eric! She'll wake up. (But ERIC lifts her into his arms. When he turns back his face is flush with tears.)

GAIL: Eric. What is it? (ERIC cuddles ELIZABETH. He puts his lips to her forehead. He places her gently back in the crib.) What?

ERIC: It's just - It's this thing I need to tell you. I can't dance, Gail.

GAIL: You can't dance. This is why you're crying? Eric, a lot of people can't dance.

ERIC: I don't know why I can't dance. But it's-I can't. I can't make my body move in these ways that the music is demanding that I move. It's just so goddamn embarrassing. The situation. I mean, standing in public around hundreds of people who are displaying their purest, truest selves. I mean, it takes them no more than two drinks and their souls are out there on the dance floor. Their goodness. Their sensuality. They're sharing and loving. I watch that, look at that. But my body fights it. I start to analyze the music. The rhythm. The time signature. I understand the theory of dancing. The idea of spontaneously sharing in this moment that exists now and only now. The give and take with your partner. Two mirrors on a land where gravity holds you to this point and then leaves you free. And that the universe happens right there and then. Like, truth. I understand this intellectually. But Gail, I never have experienced it. I can't dance.

GAIL: How did Elizabeth make you think of that?

ERIC: When we were together. There were all these times when you would arrange for us to be in these places. These parties. And invariably there would be a band, or music playing and invariably people would start dancing.

GAIL: I would arrange this? Like I did this to you?

ERIC: Invariably you would want to dance. And I wouldn't dance with you. I wouldn't dance with you, Gail. And I could see the hurt register on your face. I could see the anger- build within you. I could see that this just wouldn't do for you.

GAIL: Why didn't you just say I can't dance. Why didn't you just tell me?

ERIC: Because it was the dam holding the water. If I let that out. That one thing, everything would follow. I couldn't dance. I couldn't have a normal talk about the weather with a neighbor without getting into a conversation about God, love and eternity. I mean, after all, the weather has these huge connotations. I couldn't act correctly in social situations. I couldn't sacrifice truth for a relationship. I couldn't hold you when you needed to be held because I wanted you to be stronger. Because I wanted to be stronger. I couldn't ask you for the warmth of your touch out of need. I couldn't let myself. I would only ask for your touch out of strength. Out of something that wouldn't become sick and interdependent and symbiotic. I wasn't able to do these things. I don't know, Gail. I mean, you marrying Fred didn't really say anything to me. It was like something in this continuum. This cycle. I mean, it was this thing that happened in my life. The love of my life got married to another man. It didn't seem permanent. But the fact that Elizabeth. . . The fact that this angel. . . this unbelievable gift isn't mine. And will never be mine. This is killing me.

GAIL: Oh my God, Eric. You're human.

ERIC: I'll never have a daughter, Gail.

GAIL: Yes, you will.

ERIC: I'm thirty-seven. I have done nothing but make myself more isolated, unavailable, and unappealing. Believe it or not, it's difficult picking up women with this type of conversation. I work for four dollars an hour, Gail. I never earned a college degree. I can't bring myself to work for someone who is not producing something with some kind of goodness. That rules out ninety-eight percent of job openings. And the other two percent pay approximately four dollars an hour. I am not really going to change. I don't know why this is. People think I make these choices. But you've got to believe me, Gail, I have no control. I can't dance.

GAIL: I never knew you couldn't dance. I always thought it was that you wouldn't dance.

ERIC: Could you hold me?

GAIL: I don't think so, Eric. I mean, I don't think I would be able to let go.

ERIC: Yeah. You're right. (Pause. ERIC wipes his eyes.) Gail, there were these things that you needed. Just to breathe you needed them. And it was so clear that there was no way I was going to provide you with them. And it was this thing that I did. This thing that I did. It wasn't that horrible. You needed to find someone. I felt that you needed me off the continent. Please believe me, Gail. When I got on that boat, I was thinking of you. Not of me.

GAIL: I believe you.

ERIC: Well, this is a sign of times to come. The first time we had a conversation where your eyes stayed dry and mine didn't.

GAIL: I cried.

ERIC: We better get downstairs before Marie tells Fred about her orgy with the British invasion.

GAIL: There was one time you danced with me.

ERIC: I don't remember.

GAIL: On my wedding day.

ERIC: I couldn't have.

GAIL: You did. I remember it clearly. I remember thinking how strange it was to be in this wedding gown. On my wedding day. Dancing with you. And you weren't my groom.

ERIC: Oh yeah. That. I wasn't dancing, Gail. I was walking. I convinced myself that I was walking very slowly and sideways. It was the only way I could do it.

GAIL: Eric, maybe one day . . .

ERIC: Please don't say it.

GAIL: Right.

ERIC: Gail, I cannot stand Marie. I can't stand her. Please, find. something to say to her about me so she won't expect me to sleep with her tonight.

GAIL: I'm sure you'll do just fine on your own.

ERIC: She was just an excuse to see you. I figured, I'd call with this woman in my life. I'd be less of a threat to the home. It was really stupid of me.

GAIL: No. It was human.

ERIC: Thank you for showing me your daughter. She is absolutely the single, greatest thing I've ever looked at in my entire life. (They are about to leave.)

GAIL: Eric. (ERIC turns. GAIL walks up to him slowly. She puts her head into his chest. His arms fold around her.)

GAIL: Eric, you are Fred Astaire. You are Fred Astaire.

ERIC: No, no. Sweetheart. I'm Eric.

GAIL: You are Fred Astaire. Just move the slightest bit. You have nothing to prove to anyone. Just move a little slowly. The slightest bit. Don't worry.

ERIC: We should go down there.

GAIL: In a minute. Just one minute. (GAIL rocks back and forth musically. ERIC makes a slight movement trying to follow her. In a moment, he relaxes. He is dancing.)
```
