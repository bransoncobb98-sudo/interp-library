# Classification request: batch 21 of 53 (40 records, IC-1201 to IC-1240)

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

## IC-1201: Son of Rumpelstiltskin

- Title: Son of Rumpelstiltskin
- Author (byline): AJ Jacobs
- Work: Fractured Fairy Tales
- Publisher: Bantam Books, Inc.
- Publication date as stated: Nov 1997
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1579
- Already set (do not supply): none

### Source block (context only)

```text
Author: AJ Jacobs
Book: Fractured Fairy Tales
ISBN: 0553099809
Publisher: Bantam Books, Inc.
Date(Month/Year): Nov 1997
```

### Introduction (context only: never use it for content warnings)

```text
Set against the backdrop of an enchanted forest, this is the timeless story of a magical, though temperamental, little creature named Rumpelstiltskin who longs for recognition and power. He entices a young maiden to pledge to him her firstborn child in exchange for turning straw into gold. And as it true with most fairy tales the story repeats itself throughout generations . . . Son of Rumpelstiltskin by AJ Jacobs.
```

### Performance text (classify this)

```text
"Well, what is your name then'?" challenged the queen, her hands on her hips.

"It's, uh . . ." The little man took off his hat and scratched his head. "It's, uh . . ." Then a horrible realization came to him. He didn't know what his name was!

"Wait here. I'll be right back," he said to the queen. He dashed into the kingdom to see if he could find anybody who could tell him what his name was.

Once a very long time ago, In a forest, there was a tree-which is a nice thing to have in a forest. Now, in this tree there happened to live a funny little man in a green suit with a pointed cap. He lived with his son-also a funny little man in a green suit with a pointed cap.

One day the son walked over to his father's side of the branch with a question he had been wondering about for fifty years. (He hadn't wanted to rush things.)

"How come we've got to live in a tree?" he asked.

"Because we're not ordinary folks, boy," replied the older little man, wagging his wisdom-filled finger. "We're magic."

"Magic?"

"Yup," said the father. "You know how sometimes folks get into trouble and then they meet a funny little man who makes a deal to help 'em out? And he does a little magic and then later on, they write a fairy tale about it?" He pulled a fairy-tale book out of his cap. and pointed to some funny little men. "Funny little men. That's us."

And then, being that it was the son's six hundredth birthday, the father told him it was time he go out in the world and make a name for himself.

"If I do real good," asked the son, "will they write a fairy tale about me?"

"Without a doubt," said the father, who then gave his son a helpful kick on the rear to start him on his way. Off went the son to make a name for himself and, with any luck, sell his life story to a fairy-tale agent for a goodly sum.

In the village nearby, there was a miller who was very poor, but as luck would have it, he had a very beautiful daughter. One day the miller's daughter was carrying a load of flour when who should she bump into but the king himself, out for his daily constitutional. The king was knocked on his royal rear, but before he could gather his thoughts and banish the girl from the kingdom forever, the miller bounded to the rescue.

"This daughter of mine can spin gold out of straw," boasted the miller. He pointed to his lovely flaxen-haired girl.

"Spin gold out of straw?" exclaimed the king, his regal red eyebrows arching. "Bring this girl to my castle tomorrow and if she can do as you say, I shall take her for my bride. Good day."

The king marched off to do royal things, such as sit on his throne and behead people, leaving the father and daughter alone.

"Father, what did you tell him a thing like that for?" cried the daughter.

"So that he’ll marry you and we can live in a palace in comfort and every whim catered to, including dental care," said the miller.

"But I can't spin gold out of straw-you know that!"

"Yeah, I know it. And you know it. But the king doesn't know it! And we sure won't tell him!" The miller laughed loudly at his own wit, leaving the daughter with no choice but to bonk him on the head with a sack of flour.

The next morning, the king placed the unfortunate miller's daughter in a dark room in the castle with nothing but a spinning wheel and a stack of straw. "Now spin that straw to gold-or else!" ordered the king. Thereupon, he thoughtfully gave the girl her privacy by gently closing the door and nailing it shut.

Alone in the room, the miller's daughter sat down and put her chin in her hands. "I don't want to be or elsed"

The funny little man in the green suit with a pointed cap-the one trying to make a name for himself-'had heard about the young girl's plight, and knew that this was the chance that he had been waiting for. So into the room he hopped.

"Who are you?" exclaimed the girl.

"I'm a funny little man in a green suit."

"You could say that again."

"I'm a funny little man in a-"

"Never mind," said the daughter, who had no time for such shenanigans. After all, she was busy doing nothing. "What do you want'?" she asked.

"I will spin that straw to gold for you if you will give me your first child after you become queen."

"My first child? Why that?"

"Who knows?" The little man shrugged. "Makes the plot better."

Not one to interfere with the plot, the miller's daughter shook hands with the little man. He jumped to the wheel and in no time at "all had spun a room full of bright, shimmering gold. When in the morning the king found everything as he had wished, he was overjoyed. He now had so much money he could be king. That is, if he weren't king already.

They were married, and the miller's daughter became queen. She was given a throne right next to her husband, and learned to sit for long periods of time, as kings and queens do.

About two years afterward, a beautiful child was born and the little man appeared in the castle once again.

"Hi! I came for the kid," he said.

The queen jumped back and clutched her child to her chest.

"But you can't have my child! What will you do with him?"

"Dress him in a green suit and make a funny little old man out of him. What else?"

The queen imagined her baby in a little green suit and little pointed cap and began sobbing loudly. In fact, she sobbed so loudly the man decided to give her a second chance.

Pulling his fingers out of his little ears, he said, "I'll tell you what. I'll make a deal. If you can discover what my name is in two days, you can keep the child." The little man paused. "Boy, won't this make a keen fairy tale someday'?"

The queen began pacing the royal nursery and calling to mind all the names that she could think of.

"Are you Henry? Clyde? Newton? George, Marmaduke, Sidney, Frank?"

"Nah," said the man.

The queen then desperately searched for still other names. She looked in the village white pages, Who's Who Among the Little People, even the gossip column of the Palace Chronicles. The next day she tried again.

"Are you Ming Choi?" she asked. "Or Running Mouse? Cherry Nose? Charlie Brown?"

"No! You've failed," shouted the little man with a mischievous laugh.

"Well, what is your name then'?" challenged the queen, her hands on her hips.

"It's, uh . . ." The little man took off his hat and scratched his head. "It's, uh . . ." Then a horrible realization came to him. He didn't know what his name was!

"Wait here. I'll be right back," he said to the queen. He dashed into the kingdom to see if he could find anybody who could tell him what his name was.

"Do you know me'?" he asked the palace garbage collector.

"No. I can't say I do-and with any luck I never will," the garbage man replied, jumping into a garbage can and pulling the lid on top of him.

The little man asked everyone he chanced to meet, from the village moat cleaner to the royal jack hammer operator, but nobody could tell him who he was. Finally, out of desperation, he went to an old wise man who lived in a hole in the ground.

"No, I don't know your name," said the wise man in the hole in the ground. "But I know how you can find out. Get yourself a mailbox. Sooner or later, some-body will send you a letter. Then all you have to do is see what name is on the envelope."

That was it! He was truly a wise man-or at least as wise as anyone can be who chooses to live in a hole in the ground.

In any case, the little man did as he was instructed. He got a mailbox and waited inside for a delivery, and before long, he did receive a letter. It was from a talk show sidekick who told him he might have already won a million dollars. But that's another fairy tale. The little man just wanted to see what his name was. But when he saw it, he was shocked. It read "Rumpelstiltskin."

"Rumpelstiltskin!" he cried. "What kind of a name is that? I can't go back to the queen and tell her my name is Rumpelstiltskin. I'd be the laughingstock of the kingdom."

And so, the queen and her child lived happily ever after, for she never saw the funny little man in the green suit again. In fact, nobody ever saw the little man again, because he was so ashamed he got out of the magic business and changed his name to Louie Smith.

And we all know there's never been a fairy tale about Louie Smith. That is, until just now.
```

---

## IC-1202: The Spot

- Title: The Spot
- Author (byline): Stephen Dietz
- Work: Laugh Lines: Short Comedic Plays
- Publisher: Random House
- Publication date as stated: 2007
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CHUMLEY, WAGNER, NELSON, ROGER, BETSY, GLORIA
- Teaser before the introduction: Yes
- Spoken words (computed): 1237
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephen Dietz
Book: Laugh Lines: Short Comedic Plays
ISBN: 978-0307277138
Publisher: Random House
Date (Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
For more than a century, movie stars, famous athletes and musicians have all lent their star power to support presidential campaigns. Today the influence of celebrity endorsements continues to be a fascinating phenomenon in American politics.

Political endorsements can be a powerful device in swaying public opinion. But let’s face it. It’s gotten a little crazy lately!

In 2012, a cat named Mr. Nuts gained notoriety for predicting the presidential election based on which litter box he chose, although his prediction was based on his owners' preferences and ended up being incorrect.

And to stay with the cat-themed endorsements: In 2020, pop superstar Taylor Swift signed an Instagram post as “Taylor Swift -- Childless Cat Lady” while endorsing Democrat Kamala Harris for president. The remark was a reference to 3-year-old comment made by JD Vance, in which he described Democrats as beholden to “a bunch of childless cat ladies who are miserable at their own lives and the choices that they’ve made and so they want to make the rest of the country miserable, too.”

Stephen Dietz takes a humorous look at political endorsements in The Spot.

A chair and a small side table. On the table, a cup of tea. Surrounding this -- four people, all staring at the chair.
```

### Performance text (classify this)

```text
CHUMLEY: The Communications Director. Well-dressed. Nervous.

WAGNER: Director of "The Spot."

NELSON: The Pollster. Disheveled. Always working at a laptop computer. Often sipping from a diet soda.

ROGER: The Senior Advisor to the Candidate.

BETSY: A young mother.

GLORIA: A production assistant.

CHUMLEY: So, Roger, what we've envisioned -- and Wagner, just jump right on in here if I miss something -- what we envision for "The Spot" is a sort of solid, homespun, no-nonsense, eyes-right-into-the-camera kind of thing

WAGNER: Something that cries out: "Here-we-are-in-her-livingroom-and-she's-gonna-be-straight-with-us-so-help-her-God."

CHUMLEY: The young mother we've found -- and Wagner, correct me if I'm off-base here - - this young mother is really just a perfect choice for

ROGER: She really a mother? She really have kids?

CHUMLEY: Well, as far as-

ROGER: People want in, Chumley. Everyone wants to be in "The Spot." They'll lie through their teeth to be in "The Spot."

WAGNER: She has kids.

ROGER: You've seen 'em? What are their names?

CHUMLEY: Roger, just to be clear, just to be what I like to call crystal: this woman's kids are not in "The Spot." It's just her. No kids in "The Spot." No kids at all.

ROGER: (Immediately, to WAGNER.) What are their names?

WAGNER: Joey and Gretchen.

ROGER: (Immediately, to NELSON.) I want those names polled.

NELSON: Right away, sir. (Begins typing on her/his laptop.)

CHUMLEY: Shall we bring her in and get started? Her name is

ROGER: I don't give a turd in a taco what her name is, WE'RE ON THE CLOCK, GET HER BUTT IN HERE.

WAGNER: (Calls out.) GLORIA- (GLORIA appears-friendly and efficient.)

GLORIA: (To WAGNER.) Yes, what can I do for you?

WAGNER: We're ready for the talent. (GLORIA nods and is gone.)

NELSON: Roger. NELSON: The name Joey polled at 78.

ROGER: Good. What about Gretchen?

NELSON: 31.

ROGER: Toss it out. How 'bout Sally? Run the numbers on Sally.

NELSON: Will do. (Back to her/his laptop.)

ROGER: Sally always packs a punch. (GLORIA enters with BETSY.)

GLORIA: Everyone: this is Betsy Taylor.

CHUMLEY: Betsy, I'd like you to meet Roger. He's the Senior Advisor to the Candidate.

BETSY: (Extends her hand.) A pleasure.

ROGER: (Suddenly.) YOUR HAND? YOU WANT TO OFFER ME YOUR HAND? HOW DARE YOU TRY TO PULL A STUNT LIKE THIS? WHO DO YOU THINK YOU'RE DEALING WITH? (It becomes clear that he is talking into his phone.) THE DAY MY CANDIDATE SHAKES THE HAND OF SOMEONE FROM YOUR PARTY-YOUR TRIBE -- YOUR GANG, YOUR CABAL- IS THE DAY PIGS WILL PLAY HOCKEY IN HELL!!! (He clicks the call off -. Turns pleasantly to BETSY. Extends his hand.) Hi, there. I'm Roger. (Before she can respond.) I'm told you're a mother. Joey and Sally.

BETSY: Gretchen. My daughter-Gretchen.

ROGER: Sorry. It didn't poll.

NELSON: Sally's at 83.

ROGER: Sally polled like a champ. Rhymes with rally-good times ahead! You've got a daughter named Sally. You must be very happy. Mint? (Offers her one.)

CHUMLEY: (Jumping in, nervous.) Okay, let's get you in place, Betsy. (BETSY sits in the chair. WAGNER approaches her.)

WAGNER: Now, the aesthetic I’m working with in "The Spot" might well be called a "post-ironic, reality-infused, Mom-at-home" kind of thing-

CHUMLEY: Something I like to call "honesty." Are you with me?

WAGNER: And you're clear on the text?

CHUMLEY: What I call "the lines."

BETSY: Yes, I am.

WAGNER: Okay, then, people: let's shoot one.

GLORIA: (Calling out.) QUIET ON THE SET. ROLL SOUND.

WAGNER: And ... ACTION. (BETSY looks straight ahead and speaks. Calm. Honest. Very good at this.)

BETSY: Just the other day, my daughter ... (Slight pause.) Sally ... asked me who I was going to vote for. And I told her that there are three things I look for in a candidate: trust, honor, and integrity. (She lifts her tea.) And this year, only one candidate has all of-

ROGER: STOP RIGHT THERE! Set. The teacup. Down. (She does.) What are you doing, Betsy?

Are you trying to kill me? Are you trying to butcher my candidate?

BETSY: (confused.) I'm not sure 1-

ROGER: Do you know the numbers on TEA? They are abysmal. Tell her the numbers on tea, Nelson.

NELSON: (Helpfully.) 17.

ROGER: Seventeen! The TEA is polling at SEVENTEEN and there you are in your little sweater and your little chair and you're LIFTING THE TEA TO YOUR LIPS. Why don't you just MAKE OUT WITH OJ and DANGLE A BABY OVER A BALCONY?

CHUMLEY: Roger, please, we're on a deadline-

ROGER: An election, Betsy -- this quaint little practice of people going out to vote--that is nothing but a symbolic narcotic to placate the populace. (Grandly, to NELSON.) THE REAL VOTES ARE NOT CAST AT THE POLLS-BUT WITH THE POLLSTERS-with great Americans like Nelson here. (NELSON lifts her/his diet soda.) And has the Carefully Polled Public voted for TEA, Betsy? I think not.

ROGER: Tell them, Nelson. Tell them who America wants Betsy to be.

NELSON: Well, in addition to Joey and Sally. You have a husband named Bill and a dog named Buster. (Quickly consults new data on laptop.) Correction! No husband- you're a single mom. You work at Wal-Mart. And your Joey's all grown up

BETSY: He's only nine!

NELSON: Sorry, ma'am: he's a soldier now, gone to rid the world of evil.

ROGER: Atta boy, Joey!

NELSON: And you're not sipping tea

ROGER: I told you!

NELSON: (Overlapping.) No, Betsy, you're sipping a Starbucks extra-hot low-fat double-tall mocha with extra whipped cream!

ROGER: (Buoyantly.) THAT IS THE WOMAN THEY WANT, Betsy-and, hey, don't look at me, I didn't invent her. She is the Love Child of Entitlement and Complacency. She is the PEOPLE'S CHOICE! NOW: LET'S SHOOT HER!

GLORIA: (Calling out) QUIET ON THE SET. ROLL SOUND.

WAGNER: And ... ACTION.

BETSY: (takes her place, about to begin. Then suddenly) I won't do it. I just won't do it.

ROGER: You won't do it? What's that mean?

BETSY: It's not true-it's all a lie.

ROGER: Just what the hell kind of actress are you, anyway?

BETSY: I'm not an actress.

ROGER: Oh, you can say THAT again.

BETSY: (Genuine, with passion.) I'm a wife and a mother. I was chosen for "The Spot" because I really believe in it. I believe in your candidate. I want to give him my vote. When I look into the camera, I am speaking from my heart. (Silence. ROGER turns to CHUMLEY, then WAGNER, then NELSON, as if to say: CAN THIS BE TRUE? ROGER turns back to BETSY. Approaches her slowly.)

ROGER: Take off your sweater.

BETSY: But didn't you hear what I said? I reaIly-

ROGER: Here's the thing about people who speak from their heart: I don't trust' em. Hearts are fickle, Betsy. Hearts change. And when the future of the free world is on the line, I can't be taking a chance on what people believe in their hearts. (Beat. He stares at her hard.) Take. It. Off. (BETSY, staring right at ROGER, takes off her sweater. Underneath, attached with a strap over her shoulder, is a tape recorder.) See there. Hand me the tape recorder. (She does.) Is this another one of your TRICKS?!

BETSY: I'd like a chance to explain-

ROGER: (Overlapping.) ANOTHER WAY TO "SHAKE MY HAND"? SELL US OUT TO THE JACKALS AT JHE NETWORKS? IS THAT WHAT THIS IS?

BETSY: No, not at all- (We realize that once again, he is speaking into his phone.)

ROGER: What did they pay you? (BETSY does not answer.) Fess up, SuperMom. I know how they work. What did it cost them?

BETSY: I didn't want their money. I did it

ROGER: Because of your beliefs, I suppose. What you feel in your heart.

BETSY: Yes.

ROGER: You disgust me. Get her out of here. (CHUMLEY walks BETSY away, as-ROGER’S cell phone rings.) (Instantly, into phone.) Yes? Mr. Candidate, great to hear from you, sir! It's going extremely well-couldn't be better! Yes, we'll send you a rough cut before the day is out. Thank you, sir. Good-bye. (He ends the call. CHUMLEY rushes back in.)

CHUMLEY: (In a panic.) Oh my god, Roger, we are just-I mean, Wagner, correct me if I'm wrong here-but it seems to me that we are now what I like to call completely screwed.

ROGER: (Calmly.) Nelson. ROGER: Run the numbers on "Gloria."

NELSON: Right away. (Back to her/his laptop.)

CHUMLEY: Roger, no- (ROGER turns to GLORIA.)

ROGER: Gloria, do you know the feeling we're going for?

GLORIA: Well, yes, but-

ROGER: And you're clear on the lines?

GLORIA: Yes, but I'm not really a-

ROGER: And do you believe in them, Gloria? Do you believe in them deep in your heart?

(Beat.)

GLORIA: (Simple, direct.) Not at all.

ROGER: THIS ONE's got MOXIE. THIS ONE we can SHOOT.

CHUMLEY: Roger, please

ROGER: (Exultant.) PUT ON THE SWEATER! (WAGNER leads GLORIA to the chair and helps her into the sweater and her microphone, powders her face, etc.) (Firing questions.) Gloria, I want you to finish this sentence: my candidate is . . .

GLORIA: (Firing back, enjoying herself) . . . dumb as a box of hammers.

ROGER: You bet he is! And people like me are. . .

GLORIA: . . . the scum of the earth.

ROGER: You bet we are! Have a mint. (She does.)

NELSON: Gloria is polling at 93-

ROGER: You bet she is! Gloria

WAGNER: QUIET ON THE SET.

ROGER: -rhymes with euphoria!

WAGNER: ROLL SOUND.

ROGER: And ... ACTION!
```

---

## IC-1203: Squids will be Squids

- Title: Squids will be Squids
- Author (byline): Jon Scieszka
- Work: Not specified
- Publisher: Viking Press
- Publication date as stated: Sept 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: MORAL
- Teaser before the introduction: Yes
- Spoken words (computed): 1385
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jon Scieszka
ISBN: 978-0670881352
Publisher: Viking Press
Date (Month/Year): Sept 1998
```

### Introduction (context only: never use it for content warnings)

```text
John Scieszka’s book Squids will be Squids. is a collection of fables that Aesop might have told if he were alive today, sitting in the back of the class day dreaming, goofing around instead of paying attention, because his dog ate his homework and he didn’t have time to run out and buy new paper and do it over again before his bus came to pick him up in the morning.. Enjoy a few of these contemporary fables today and listen for the Moral of each story and remember . . . Sometimes the names are changed to protect the not so innocent. Squids will be Squids by John Scieszka
```

### Performance text (classify this)

```text
Fables have been around for thousands of years. And it’s no wonder, because even thousands of years ago people were bright enough to figure out that you could gossip about anybody as long as you changed their name to something like “Lion” “Mouse” or “Donkey” Aesop is the guy most famous for telling fables. Though he wasn’t the first or the best looking. Most descriptions of Aesop call him, funny shaped or ugly or worse. But you didn’t hear that from me. I think Aesop was one heck of a swell guy.

Deer, Mouse, Rabbit and Squid:
Deer, Mouse, Rabbit and Squid sat on the steps trying to decide what to do.
"Let's go see a movie," said Deer.
"Great," said Mouse. "Great" said Rabbit.
"There's nothing good on," said Squid.
"Let's play Frisbee in the park," said Mouse.
"Great," said Rabbit. "Great," said Deer.
"My tentacles are too tired," said Squid.
"Let's go shopping," said Rabbit.

"Great," said Deer. "Great," said Mouse. "That's so boring," said Squid. "I'm just going to go home,” and she oozed off down the street. "Great," they said. Then they ran off to see a movie, play Frisbee in the park, and go shopping.

MORAL: Squids will be Squids.

Grasshopper Logic:
One bright and sunny day, Grasshopper came home from school, dropped his
backpack and was just about to run outside to meet his friends.
“Where are you going?” his Mom asked.
“Out to meet some friends,” said Grasshopper
“Do you have any homework due tomorrow?” asked his Mom.
“Just one small thing for History. I did the rest in class.”
“Okay, “ said Mom Grasshopper, “Be back at six for dinner.
Grasshopper hung out with his friends, came home promptly at six, ate his dinner,
then took out his History homework.
His Mom read the assignment and freaked out.
“Rewrite twelve Greek myths as Broadway musicals. Write music for songs. Design
and build all sets. Sew original costumes for each production.”
“How long have you known about this assignment?” asked Mom Grasshoper, trying
not to scream.
“I don’t know,” said Grasshopper.

MORAL: There are plenty of things to say to calm a hopping mad Grasshopper Mmom. “I don’t know” is not one of them.

Pigeon Pie: Pigeon was a very good artist. But she had one very annoying habit. Every time she finished a painting she would show it and say, “It’s not very good” just to get someone to say, “Oh no Pigeon. That’s very good.” One day after she chased everyone else away with her annoying habit, she showed her painting to Saber-Toothed Tiger. “Oh, Look at my painting…. It’s not very good.” Saber-Toothed Tiger licked his long saber teeth. “Oh, no, Pigeon. That’s very good. I’m sure it will be perfect roasted, fried, or baked in a pie.” Pigeon was puzzled. She had painted a sad-eyed clown. Then she noticed that Saber-Toothed Tiger wasn’t looking at the painting. But it was too late and the end of this fable is too messy to even tell.

MORAL: Whatever looks like a pigeon and acts like a pigeon usually makes good pigeon pie.

Little Walrus:
Little Walrus’s mom told her to always tell the truth. One day the phone rang.
Little Walrus was the only walrus home so she answered it: “Hello?”
“Hello, Little Walrus” said Whale, “Is your mom home?”
No, She’s out having the hair taken off her lip.

MORAL: You should always tell the truth. But if your mom is out having the hair taken off her lip you might want to forget a few of the details.

Straw and Matches: It was the end of summer vacation. Straw had done everything he could think of. He was bored. So he went over to play with someone he had been warned to stay away from.

“Let’s play checkers,” said Straw.
“Okay, I’m the red ones. I get to move first. I get two moves and you get one,”
said Matches
“Forget it,” said Straw. “Let’s play ping-pong instead.”
“Okay. I get the good paddle. You stand on that side. I get to serve first, and you
have to close one eye,” said Matches.
“Never mind,” said Straw. “Maybe we should just watch TV.”
“Okay. You sit over there on the floor. I’ll sit on the couch. I get the remote and
we have to watch my favorite video,” said Matches.
“I think I hear my mom calling,” said Straw. “I’d better go.”

MORAL: Don’t play with Matches

Elephant and Flea: As Elephant grew older, he also grew more responsible. One day he and Flea went to see a movie. They liked it so much that they saw it again and completely lost track of time. “Oh no” said Elephant, when he checked his watch. “I was supposed to be home ten minutes ago. Rhinoceros is going to be furious. Do you have a quarter so I can call?” Flea checked his pockets. “Nope. Spent all my money on popcorn.” So Elephant didn’t call. When Elephant finally showed up, at Rhinoceros’s house, he was twenty minutes late, and she was furious. “You could have at least called,” said Rhinoceros

MORAL: Elephants never forget, except sometimes.

Piece of Toast and Fruit Loops: Piece of toast and Fruit Loops sat on the breakfast table arguing over who was loved the most.

“Of course everyone loves toast the most. I’m half of eggs and toast. I’m all the
toast in French toast. I am the toast with the most. Who could not love me?”
Fruit loops said, “I’m a good source of 11 essential vitamins and mineral containing
20% of the minimum daily requirements of vitamin C, Iron, Thiamin, riboflavin, Niacin,
Vitamin B6, folate, vitamin B 12 and Zinc, based on a 2,000 calorie a day diet and a 1 cup
serving size not including milk. I also have 1 gram of dietary fiber per serving and 12 grams
of sugar, yellow dye #6, blue #1 and #2 and red #40. BHT has been added to preserve
freshness.”
But while Fruit Loops was rattling off his nutrition facts…
Mom had a cup of tea…
“Toast… Toast… toast….” (getting cold)
Dad drank coffee…..
“Fruit loops…. Fruit loops…. Fruit loops…” (getting soggy)
Son ate a doughnut
“Toast…toast…toast” (getting colder)
Daughter said she’d get a bagel on the way to school.
“Fruit loops…fruit loops… fruit loops…” (getting soggier)

MORAL: Breakfast is the most important meal of the day

Hand, Foot and Tongue: One evening at dinner, Hand, Foot and Tongue got into a heated argument over who had the toughest job. “I have the toughest job,” said Hand. “Every day I work from sunup to sundown. I button shirts. I tie shoes. I hold the spoon and fork to feed all of us. I have to be strong enough to punch with a fist, and gentle enough to pat a baby. I definitely have the toughest job.”

“No you don’t,” said Foot. “I have the toughest job. Every day I have to carry all of you. And I’m not complaining or anything, but I usually have to do it in the dark – stuck in a smelly sock and laced in a shoe. I have the toughest job.” Then Tongue spoke up. “I am a fleshy muscular organ attached to the floor of the mouth. I help in both speech and taste. I start the process of digestion by moving food into position to get ripped and mashed and crushed and smashed to little bits by the teeth. Then I cover the little food bits with saliva and shape them into slimy blobs of guck that I push down the throat and . . . . “ “That’s sick,” said Hand. “Disgusting,” said Foot.

MORAL: There are some things we don’t talk about at the dinner table.

What fun! I should write some of those myself, you are probably thinking . . . But before you get started, it just occurred to me that you might want to know one more little bit about Aesop. Aesop used to tell this one fable about a real bossy jerk “Lion” who ruled a city. When the real bossy jerk guy who ruled Aesop’s city heard his fable, he didn’t like it. So he had Aesop thrown off a cliff.

MORAL: If you are planning to write fables, don’t forget to change the people into animals and avoid places with high cliffs.
```

---

## IC-1204: Stay, Carl, Stay

- Title: Stay, Carl, Stay
- Author (byline): Peter Tolan
- Work: Stay Carl Stay, Best Half Foot Forward and Pillow Talk: Three One-Act Plays Pgs 5-41
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CAROLINE, BRIAN, MARY SUE, CARL, DR. WEISS
- Teaser before the introduction: Yes
- Spoken words (computed): 1533
- Already set (do not supply): none

### Source block (context only)

```text
Author: Peter Tolan
Book: Stay Carl Stay, Best Half Foot Forward and Pillow Talk: Three One-Act Plays
Pgs 5-41
ISBN: 978-0822210771
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
Ladies . . . Would you rather have A Dog or a Boyfriend? Before you decide, let’s consider 4 important factors in any relationship: Jealousy, Friends, Expectations and Love.

Boyfriend: You’re late. Where have you been? Who were you with?

Dog: I’m so glad you’re home! I have no idea how long you’ve been gone. Let’s play!

Boyfriend: No, I don’t want to spend the day with your friends. I don’t like them. Dog: Whoohoo! More people to play with!

Boyfriend: I don’t know what you want from me.

Dog: Sit. Shake, Stay. Got it! What’s next?

Boyfriend: You are so needy. Just assume I love you unless I tell you otherwise.

Dog: I love you! I love you! I love you! Rub my tummy!

Hmmmm . . . That’s some decision! Stay, Carl, Stay by Peter Tolan
```

### Performance text (classify this)

```text
NOTE FROM THE AUTHOR (summarized): (Pg 9) The character of Carl should not move around on all fours. He should exhibit real dog characteristics not cartoonish – scratching, sniffing and other canine behavior should be used judiciously. Too much of it will tip the balance to cartoon. No bad dogs.

NOTE: Transitions by the Narrator are not found in the original script. The actor should step outside the scene to narrate these transitions.

Living/Dining Room of Caroline’s apartment. She is at the table with a plate in front of her. Across the room, Brian concentrates on a newspaper.

CAROLINE: (Pg 11-12) Honey? Are you sure you don't want some pasta? I put in those little shrimps you like . . .

BRIAN: I'm not eating dinner because I get home late, I eat late, and then I have a wad of food sitting in my stomach like a lead balloon. I don't think that's smart healthwise. Or sleepwise. (Beat)

CAROLINE: Do you want to sit with me? You don't have to eat, but could you sit with me while I do?

BRIAN: (Exasperated) Honey, come on . . . I'm going to watch you eat?

CAROLINE: You used to love eating dinner together, remember? (long beat) Brian?. . . Do you still love me?

BRIAN: Don’t be silly. And now we’ll be quiet. (Brian goes back to his paper)

CAROLINE: (Pg 13-14) I'm not saying Brian hasn't been good for me . . .

MARY SUE: He has been good for you. He's brought you out more. The first time we met, you were so shy. Let's be honest. When you met Brian, you were a spineless mess. But now you're a super terrific person . . .

CAROLINE: With a spine. It's like he filled a need, but the need isn't there anymore. . You know what's funny? I used to think Brian was the perfect man.

MARY SUE: (Pg 15) Look, Caroline, sweetheart, you need a professional -- Dr. Weiss. The woman has done wonders for me. Remember all that stuff I was going through with Jeffrey? She gave me some great advice. I needed love, companionship . . . someone I could relate to and connect with. She told me to get a dog.

TRANSITION by NARRATOR: [So that’s just what Caroline did . . . she went to the local animal shelter and found a big, beautiful, muscular dog . . . she named him Carl]

Caroline sits at the table with her dinner again. Brian is pulling on a pair of sweatpants. He carries socks and sneakers and sits on the couch to put them on. Carl sits on the floor staring at Brian.

CAROLINE: (Pg 19-20) Are you mad at me? . . . About the dog.

BRIAN: I don't care. Just as long as he doesn't get into my stuff. (To Carl) Stop staring at me. (To Caroline) Tell Cujo to stop staring at me.

CAROLINE: Are you going out?

BRIAN: We're playing basketball.

CAROLINE: On a Tuesday night? You usually play Friday nights.

BRIAN: Well . . . now we're playing two nights a week.

CAROLINE: Thanks for telling me. It's not just this one thing. You don't talk to me anymore.

BRIAN: (breezily, insincere) I'm sorry. I guess I don't have anything to say. Caroline, you know me. I'm not the kind of guy who indulges in a lot of small talk.

CAROLINE: I'm not talking about small talk. I'm talking about necessary talk. What's happening in your life. What you're feeling.

BRIAN: (with an edge) I think I liked you better when you were too terrified to open your mouth.

CAROLINE: (Stung) God . . . that's mean. Will you stay home tonight so we can talk?

BRIAN: Honey . . . Look. We're both upset. Let's have some time away from each other . . . and then we'll talk when we've both calmed down. Don't wait up. Keep him out of my stuff. (Brian exits, long sad beat)

CAROLINE: (their relationship is loving and special) Hi, Carl. Who's my baby? Who's my baby? Sit. Sit, Carl. You are sitting. Good boy. Want some little shrimp? Does baby want some little shrimp? (Caroline tosses some shrimp to Carl.) Good boy. That's a good boy. ******** Caroline and Carl are playing on the floor. Brian is draped on the couch again reading the paper.

CAROLINE: (Pg 23-25) Sit, Carl. Sit. (Carl sits down, crossing his legs Indian-style.) Good baby. Lie down. Down. Down, Carl. (Carl reclines, propping his head up with one hand.) Good baby!

BRIAN: Hey. Don't call the dog 'baby.' It's weird.

CAROLINE: Jealous?

BRIAN: (heavy sigh) Okay.This is so obvious. You think I've been ignoring you, so you ignore me and spend all your time with the dog. You’ve made your point. I'll try to talk to you more. Okay?

CAROLINE: Can we discuss some of the problems we're having?

BRIAN: I don't see any problems. You're the one who keeps talking about problems. You know, sometimes I think you make this stuff up so you can have something to bitch about.

CAROLINE: Is that right? I just want to talk.

BRIAN: You want to fight. You want me to say something I'll regret later.

CAROLINE: I want you to say anything you feel like saying. A little communication is all I'm asking for.

BRIAN: You want a little communication? Talk to your dog. Goodnight. (Brian stalks into the other room.)

CAROLINE: (To Carl.) Good boy. (Pointing to the other room.) Bad boy. Good boy, Carl. Speak, Carl. Speak. Woof. Woof. Woof.

CARL: Woof.

CAROLINE: My ... CARL: Moof.

CAROLINE: My ... CARL: My ...

CAROLINE: Name ... CARL: Woof.

CAROLINE: No. Name ... CARL: Name

CAROLINE: Is ... CARL: Is ...

CAROLINE: Carl. CARL: Carl.

CAROLINE: My name is Carl. CARL: My name is Carl.

CAROLINE: Good boy! CARL: Thank you.

*********** Caroline and Carl are snuggling on the couch. Brian enters.

BRIAN: (Pg 27) It smells like dog in here. Our apartment smells like a kennel. (Exits)

CARL: (Pg 26-28) (Caroline and Carl look at each other) I’m crazy about you; [but] I can't live like this. . . The petty tirades. The accusations spoken and unspoken.

CAROLINE: I know.

CARL: I don't want this to turn into a situation of it's him or it's me. I wouldn't ask you to make that decision. I wouldn't be so presumptuous.

CAROLINE: Presumptuous? Where'd you get that?

CARL: Last night on the "The MacNeil Lehrer Report."

CAROLINE: I'm so impressed. You're such a good boy.

CARL: You're my snuggle-bunny. (He rubs his head on her arm, then gets back to his conversation.) Now, as I was saying ...

CAROLINE: You want me to ask him to leave? It's something I've been thinking about, yes ... but to actually confront him. I don't think I can do it.

(Brian enters, spraying disinfectant around the room.)

BRIAN: I'm sick of that stinking animal, I'm sick of his hair all over the place. And I'm sick of my girlfriend spending every minute of her free time with a dumb animal. This is it, Caroline. It's me or it's him.

CAROLINE: You think you can put me in that position? Brian, you are so ...

CARL: (Under his breath.) Presumptuous.

CAROLINE: Presumptuous. You don't want to ask me to make that choice.

BRIAN: You bet your ass I do.

CAROLINE: (Pointing to Carl) I choose him.

BRIAN: Yeah. Right. Read my lips. Get rid of the mutt.

CAROLINE: I'm serious. The dog stays . . . and you . . . go.

BRIAN: (Turning to exit.) You're serious. (Stricken and overly dramatic) After everything I've done for you?! You used to be afraid of your own shadow. You wouldn't give an opinion, you wouldn't make a comment . . . because you were afraid of sounding stupid. I nurtured you. I made you feel good about yourself ...

CARL: (dryly) I’d like to thank the academy . . .

BRIAN: I knew this day would come. (He exits.)

TRANSITION by NARRATOR: [So . . . Caroline finally found the strength to stand up to Brian and throw him out. Life with Carl was perfect in every way. He doted on her every word, he listened, really listened. He was responsive, obedient, loving. He was the perfect companion . . . until one day]

CAROLINE: (Pg 33-34) Well?

CARL: What?

CAROLINE: Don't play dumb with me, Carl. You know what. That scene in the park with Mary Sue? You kissed her!

CARL: I licked her face.

CAROLINE: Big difference! You don't have to make out with her in front of me!

CARL: Boy, are you paranoid.

CAROLINE: Oh, please. Don't start throwing around terms you know nothing about. If you don't have anything constructive to say, keep your mouth shut.

CARL: Oh! It's the ghost of Brian past.

CAROLINE: What? That does it. Let me remind you of something, mister. I'm number one in this house and don't you forget it. I'm number one, you're number two.

CARL: You're number one because that's the way I like it, missy. I'm letting you be number one because you're getting your kicks. If I really wanted to, I could have you under the coffee table in the fetal position like that! (Carl sits on the couch and opens a magazine to read)

CAROLINE: Hey! Get down. Get down off that couch this instant! You're not allowed up on the couch and you know it. Get down!

CARL: Do you mind? I'm trying to read something . . .

CAROLINE: Get off the couch! (grabs the magazine from him and goes to hit him with it. There is a brief struggle that ends when Carl takes a nip at her. Dropping the magazine, she massages her injured hand in pain) Ow! You bit me.

CARL: I didn't bite you. I nipped. You were hitting me. I'm sorry, Caroline. I'm sorry.

TRANSITION by NARRATOR: [Well, Caroline realized that the relationship needed some help. After all, it HAD spiraled quickly into a domestic violence situation, so she called the only therapist she knew . . . Dr. Weiss]

DR. WEISS: (Pg 35-36) All right. Why don't you begin, Caroline?

CAROLINE: I don't feel like we're connecting. There was a time when I was everything to him. I remember you used to sit at the dinner table and watch me eat.

DR. WEISS: So what went wrong?

CAROLINE: He bit me.

CARL: It was a nip. She hit me with a magazine.

CAROLINE: He was up on the couch.

CARL: She makes all the rules. . . I'm not saying that Caroline hasn't been wonderful for me. But what she has to give me, I don't think I need anymore.

CAROLINE: What do you need, Carl?

CARL: Freedom. Room to run. I need to be responsible for my own life. With you I'm always going to be the dog in the relationship.

CAROLINE: That's funny. You are a dog!

CARL: And you never let me forget that. (Beat) I have to leave. I've taken a job at a kennel in Pennsylvania.

CAROLINE: Carl . . . you can't.

CARL: (Pg 37) Yes, I can. And I did. (Breaking) Caroline, I'll never forget you. [But] I think this is for the best ... for both of us. Goodbye. (Carl exits. Caroline runs to the door after him)

CAROLINE: Carll No! Stay, Carll Stay! (He is gone) What now? What do I do now? I've been dumped by my dog.
```

---

## IC-1205: The Stinky Cheese Man & Other Fairly Stupid Tales

- Title: The Stinky Cheese Man & Other Fairly Stupid Tales
- Author (byline): Jon Scieska
- Work: Not specified
- Publisher: Viking Press
- Publication date as stated: May 2002
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: JACK THE NARRATOR, TOWNSMAN, LITTLE OLD WOMAN, STINKY CHEESE MAN, LITTLE OLD MAN, COW, LITTLE GIRL, LITTLE BOY, FOX, FROG, PRINCESS, LITTLE RED, WOLF, QUEEN, LITTLE MAN, CINDERELLA, GIANT
- Teaser before the introduction: Yes
- Spoken words (computed): 1782
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jon Scieska
ISBN: 978-0670035694
Publisher: Viking Press
Date (Month/Year): May 2002
```

### Introduction (context only: never use it for content warnings)

```text
A long time ago, people used to tell magical stories of wonder and enchantment. Those stories were called Fairy Tales. What I’ll be presenting today are NOT fairy tales. They are ALMOST Fairy Tales, but not quite.

The Stinky Cheese Man and Other Fairly Stupid Tales by Jon Scieska
```

### Performance text (classify this)

```text
JACK THE NARRATOR: Once upon a time there was a mother duck and a father duck who had seven baby ducklings. Six of them were regular-looking ducklings. The seventh was a really ugly duckling. Everyone used to say,

TOWNSMAN: What a nice-looking bunch of ducklings – all except that one. Boy he’s really ugly.

JACK THE NARRATOR: The really ugly duckling heard these people, but he didn’t care. He knew that one day he would probably grow up to be a swan and be bigger and look better than anything in the pond. . . Well, as it turned out, he was just a really ugly duckling. And he grew up to be just a really ugly duck. [Make the ugliest duck face possible] The End

JACK THE NARRATOR: Once upon a time there was a little old woman and a little old man who lived together in a little old house. They were lonely. So the little old lady decided to make a man out of stinky cheese. She gave him a piece of bacon for a mouth and two olives for eyes and put him in the oven to cook. When she opened the oven to see if he was done, the smell knocked her back.

LITTLE OLD WOMAN: Phew! What is that terrible smell?”

JACK THE NARRATOR: The Stinky Cheese Man hopped (hop) out of the oven and ran out the door calling . . .

STINKY CHEESE MAN: (while running) Run run run as fast as you can. You can’t catch me, I’m the Stinky Cheese Man!

LITTLE OLD MAN: (sniffing the air and making a face) I’m not really very hungry,

LITTLE OLD WOMAN: (holding her nose) I’m not really all that lonely.

JACK THE NARRATOR: So, they didn’t chase the Stinky Cheese Man. The Stinky Cheese Man ran and ran until he met a cow eating grass in a field.

COW: (chewing cud, abruptly stops and speaks with her mouth full) Wow! What’s that awful smell?

STINKY CHEESE MAN: (hands on hips) I’ve run away from a little old lady and a little old man and I can run away from you too, I can. (while running) Run run run as fast as you can. You can’t catch me, I’m the Stinky Cheese Man!

COW: (sniffing the air again) I’ll bet you could give someone two or three stomachaches, I think I’ll just eat weeds. (returns to eating)

JACK THE NARRATOR: So, the cow didn’t chase the Stinky Cheese Man either. The Stinky Cheese Man ran and ran until he met some kids playing outside school.

LITTLE GIRL: (waving her hand in front of her face) Gross. What’s that nasty smell?

STINKY CHEESE MAN: (dancing around the children, maybe even farting in their general direction) I’ve run away from a little old lady, and a little old man, and a cow, and I can run away from you too, I can. (while running) Run run run as fast as you can. You can’t catch me, I’m the Stinky Cheese Man!

LITTLE BOY: (sniffing the air) If we catch him, our teacher will probably make us eat him. Let’s get out of here.

JACK THE NARRATOR: So, the kids didn’t chase the Stinky Cheese Man either. By and by the Stinky Cheese Man came to a river with no bridge.

STINKY CHEESE MAN: How will I ever cross this river? It’s too big to jump, and if I try to swim across I’ll probably fall apart.

JACK THE NARRATOR: Just then the sly fox (who shows up in a lot of stories like these) poked his head out of the bushes.

FOX: Why, just hop on my back and I’ll carry you across, Stinky Cheese Man.

STINKY CHEESE MAN: How do I know you won’t eat me?

FOX: Trust me.

JACK THE NARRATOR: So, the Stinky Cheese Man hoped on the fox’s back. The fox swam to the middle of the river

FOX: (coughing, gagging, sneezing) Oh, man! What is that funky smell?

JACK THE NARRATOR: and the Stinky Cheese Man flew off his back and into the river where he fell apart. The End ******

JACK THE NARRATOR: Once upon a time there was a frog. One day when he was sitting on his lily pad, he saw a beautiful princess sitting by the pond. He hopped (hopping) in the water, swam (swimming) over to her, and poked his head out of the weeds (pokes head up and tongue darts out a couple of times).

FROG: (in a most sad and pathetic voice) Pardon me, O beautiful princess, I wonder if you could help me.

JACK THE NARRATOR: The princess was about to jump up and run, but she felt sorry for the frog with the sad and pathetic voice.

PRINCESS: (hesitantly) What can I do to help you, little frog?

FROG: Well, I’m not really a frog, but a handsome prince who was turned into a frog by a wicked witch’s spell. And the spell can only be broken by the kiss of a beautiful princess.

JACK THE NARRATOR: The princess thought about this for a second (thinking pose), then lifted (lifting) the frog from the pond and kissed him (kisses frog). (Long pause while nothing happens)

FROG: (Laughing and jumping back into the water) I was just kidding!

JACK THE NARRATOR: and the princess wiped (wiping) the frog slime off her lips. The End *******

JACK THE NARRATOR: This next story is even better than the last three. See, it’s about this girl who runs very fast and always wears red running shorts. That’s where her name comes from, get it? So anyway, this girl is running to her granny’s house when she meets a wolf. He tricks her into taking the long way while he takes the shortcut. Now this is the good part because Red runs so fast that she beats the wolf to granny’s house. He knocks on the door (knocks). Red answers it. And guess what she says? (in Little Red Voice) “My, what slow feet you have.” And that’s it. The end. Is that great or what? So sit back, relax and enjoy – “Little Red Running Shorts. . . (Long pause; he gestures for actors to take the stage) And now, like I already said – Little Red Running Shorts!

LITTLE RED: (in a hateful and sarcastic voice) You just told the whole story. We’re not going to tell it again.

JACK THE NARRATOR: You can’t say that. You have to start with ‘Once upon a time’.

WOLF: (also sarcastic and disgusted) No way. You blew it.

JACK THE NARRATOR: (to Little Red and Wolf) But you guys are next. Look at the title (gestures as if there is a large sign behind him) – ‘Little Red Running Shorts.’ That’s you.

LITTLE RED: Let’s go, Wolf. We’re out of here.

JACK THE NARRATOR: Wait. You can’t do this. WAIT! The End *******

JACK THE NARRATOR: Once upon a time there was a Prince. And this Prince’s dad and mom (the King and Queen) somehow got it into their royal heads that no Princess would be good enough for their boy unless she could feel a pea through one hundred mattresses. So it should come as no surprise that the Prince had a very hard time finding a Princess. Every time he met a nice girl, his mom and dad would pile one hundred mattresses on top of a pea and then invite her to sleep over. When the Princess came down for breakfast, the Queen would ask

QUEEN: How did you sleep, dear?

PRINCESS: (politely) Fine, thank you.

JACK THE NARRATOR: And the King would show her the door. Now this went on for three years. And of course nobody ever felt the pea under one hundred mattresses. Then one day the Prince met the girl of his dreams. He decided he better do something out about it. That night, before the Princess went to bed, the Prince slipped his bowling ball under the one hundred mattresses. When the Princess came down for breakfast the next morning, the Queen asked,

QUEEN: How did you sleep, dear?

PRINCESS: This might sound odd, but I think you need another mattress. I felt like I was sleeping on a lump as big as a bowling ball.

JACK THE NARRATOR: The King and Queen were satisfied. The Prince and Princess were married. And everyone lived happily, though maybe not completely honestly, ever after. The End *******

JACK THE NARRATOR: Once upon a time there was a beautiful girl named Cinderella who lived with her wicked stepmother and two ugly stepsisters. These step-relatives were not only wicked and ugly --- they also made Cinderella clean the house every day. One day the local prince announced that he was holding a fabulous ball at his castle. Everyone was invited. The stepmother and stepsisters got all dressed up to go. But, as usual, they made Cinderella clean the house, so she didn’t have time to get ready. After the stepmother and stepsisters left for the ball, Cinderella sat down and began to cry. Just then a little man appeared.

LITTLE MAN: Please don’t cry. I can help you spin straw into gold.

CINDERELLA: I don’t think that will do me much good. I need a fancy dress, glass slippers, and a coach.

LITTLE MAN: Would you like to try to guess my name?

CINDERELLA: No, Not really.

LITTLE MAN: Come on, Do you think it’s Chester? If you don’t have a dress, it doesn’t really matter. . . Oh, just guess a name, any name.

CINDERELLA: I’m not supposed to talk to strangers.

JACK THE NARRATOR: Then she closed the door and left the little man standing outside screaming.

LITTLE MAN: RUMPELSTILTSKIN! RUMPELSTILTSKIN! RUMPELSTILTSKIN!

JACK THE NARRATOR: When the stepmother and stepsisters got home from the ball, Cinderella told them about the strange little man. They still made her clean the house. And meaner still, they changed her name to Cinderumpelstiltskin. The End *******

JACK THE NARRATOR: Now it’s time for the best story – my story. Because once upon a time I traded our last cow for three magic beans and . . . hey, Giant. What are you doing down here? You’re wrecking my whole story.

GIANT: I DON’T LIKE THAT STORY. YOU ALWAYS TRICK ME.

JACK THE NARRATOR: (to Giant) That’s the best part.

GIANT: FEE FI FUM FORY. I HAVE MADE MY OWN STORY.

JACK THE NARRATOR: (to Giant) Great rhyme, Giant. And I’m sure your story is just as good. But there’s no room for it. So why don’t you climb back up the beanstalk. I’ll be up in a few minutes to steal your gold and your singing harp.

GIANT: I’LL GRIND YOUR BONES TO MAKE MY BREAD.

JACK THE NARRATOR: (to Giant) I knew you’d understand.

GIANT: I WILL [TELL] MY STORY NOW . . . The End of the evil Stepmother said, “I’ll HUFF and SNUFF and give you three wishes.” The beast changed into seven dwarves happily ever after, for a spell had been cast by a Wicked Witch once upon a time.

JACK THE NARRATOR: That’s your story? You’ve got to be kidding. That’s not a Fairly Stupid Tale. That’s an Incredibly Stupid Tale. That’s an Unbelievably Stupid Tale. That is the Most Stupid Tale I Ever – awwwwk!” (Giant grabs Jack; holds him tight in one fist . . . Jack hesitantly begins to tell his story) Once upon a time there was a Giant.

GIANT: (squeezing Jack tightly) TELL ME A BETTER STORY OR I WILL GRIND YOUR BONES TO MAKE MY BREAD. AND WHEN YOUR STORY IS FINISHED, I WILL GRIND YOUR BONES TO MAKE MY BREAD ANYWAY! (an ugly laugh)

JACK THE NARRATOR: (thinking aloud to audience) He’ll kill me if I do. He’ll kill me if I don’t. There’s only one way to get out of this. . . (clears his throat and beings the story) Once upon a time there was a Giant.

GIANT: (squeezing Jack tightly) TELL ME A BETTER STORY OR I WILL GRIND YOUR BONES TO MAKE MY BREAD. AND WHEN YOUR STORY IS FINISHED, I WILL GRIND YOUR BONES TO MAKE MY BREAD ANYWAY! (an ugly laugh)

JACK THE NARRATOR: (thinking aloud to audience) He’ll kill me if I do. He’ll kill me if I don’t. There’s only one way to get out of this. . . (clears his throat and beings the story) Once upon a time there was a Giant.

GIANT: (squeezing Jack tightly) TELL ME A BETTER STORY OR I WILL GRIND YOUR BONES TO MAKE MY BREAD. AND WHEN YOUR STORY IS FINISHED, I WILL GRIND YOUR BONES TO MAKE MY BREAD ANYWAY! (an ugly laugh)

JACK THE NARRATOR: (thinking aloud to audience) He’ll kill me if I do. He’ll kill me if I don’t. There’s only one way to get out of this. . . (clears his throat and beings the story) Once upon a time there was a Giant. . .

(sing softly and fade out to silence) This is the story that doesn’t end . . . it just goes on and on my friends . . . Some people started *listening* not knowing what it was and they’ll continue *listening* forever just because . . . ] The End
```

---

## IC-1206: Strange Addictions

- Title: Strange Addictions
- Author (byline): Laurie Allen
- Work: 22 Comedy Ten-Minutes Plays, Pg 94 - 101
- Publisher: Meriwether Publishing
- Publication date as stated: Aug 2019
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CAST OF CHARACTERS, BETH, EARL, MIKE, SUE
- Teaser before the introduction: Yes
- Spoken words (computed): 1316
- Already set (do not supply): none

### Source block (context only)

```text
Author: Laurie Allen
Book: 22 Comedy Ten-Minutes Plays, Pg 94 - 101
ISBN: 978-1566082112
Publisher: Meriwether Publishing
Date (Month/Year): Aug 2019
```

### Introduction (context only: never use it for content warnings)

```text
Reality TV shows premier all the time, and they actually get more shocking as time goes by. One popular show was My Strange Addiction — a show that featured people who were absolutely hooked on things that the rest of us couldn’t even begin to imagine. Whether it be an addition to puppets, balloons or getting plastic surgery, the show became a guilty pleasure for many fans.

I guess I should confess now . . . I have a strange addiction too . . . I’m addicted to forensics/speech competitions. But rather than tell you about it . . . let me show you!

Strange Addictions by Laurie Allen
```

### Performance text (classify this)

```text
CAST OF CHARACTERS: BETH - addiction counselor EARL - collects toenails MIKE - obsessively calls his mom SUE - thinks she is a cat

BETH: (Pg 94 – 101) Welcome. Welcome to Strange Addictions Anonymous. Here, you are free to share your most private and hidden addictions. And please, please be assured that you don't need to fear being misunderstood or judged, because here, we listen and support one another. No matter the addiction. Also, a quick reminder, absolutely no laughter or negative comments.

EARL: What about you? Are you addicted to anything?

BETH: Actually, yes. Thank you for asking. Exercise. Excessive exercise. To the point that it was once controlling my life. [But] I was able to set limits. Thirty minutes a day. Do I ever have stressful times and slip back into the excessive workouts to the point where I want to do jumping jacks for hours on end? Or worse yet, at inappropriate places? Say, a business meeting or a funeral?

MIKE: You did jumping jacks at a funeral?

BETH: (Raises her hand) Guilty. And that's why we're here, to acknowledge that we have a problem and then support and encourage each other as we work through our own issues. So, let's begin. Who would like to go first?

MIKE: (Halfway raises his hand) Mike. I guess I can go.

BETH: So, tell us about your addiction, Mike.

MIKE: (Quiet.) Well, I... I call my mom. (Holds up his phone.) A lot . . . I like to hear her voice. Constantly. It's comforting, soothing, like when I was a baby.

SUE: Well, I call my mom four or five times a day, and that seems like a lot, but I don't think it's strange.

BETH: Mike, could you be more specific about how often you call her?

MIKE: I already told you. A lot. We hang up, and I call her again. And again. And again.

EARL: And she answers?

MIKE: Not always, but most of the time, yes, because if she doesn't I keep calling her. Again and again and again.

EARL: Oh, brother! What a ...

BETH: Now, now! No judging or name calling. We all have issues here that we are dealing with. We're here to help, support, and offer ideas to break these chains that are our addictions.

SUE: I have an idea. Why don't you tell your mom to get a new phone number and not tell you what it is?

EARL: (Laughs.) Yeah! I love that idea!

SUE: Then all you will hear is "We're sorry. You have reached a number that has been disconnected or is no longer in service."

MIKE: But what if I need my mom?

EARL: Then drive to her house and talk to her.

MIKE: She lives three hundred fifty miles away.

BETH: Mike, have you tried putting your phone away and limiting yourself to just one phone call per day?

MIKE: Tried it. It didn't work. (Without thinking, calls his mom. Into phone.) Hello, Mom ... I did. I'm here ... I know, Mom, but I can't do this without you ...

BETH: Mike, can you hang up now, please?

MIKE: I'm talking to my mom! (Talks quieter.) I got into trouble ... Okay, hold on ... (To BETH.) Mom wants to know why I'm in trouble.

BETH: You're not in trouble, Mike. It's just that we need to continue with our meeting, so, if you don't mind, can you call her back later?

MIKE: (Into the phone.) Did you hear that, Mom? ... Yeah. I have to hang up ... Okay. I'll call you back later. Love you. (Hangs up.)

BETH: Mike, can you please hand me your phone? I promise I'll give it back at the end of our session. Okay, who's next?

MIKE: No worries. I'll just put it right here. Out of sight, out of mind. (Places the phone under his chair.)

BETH: Okay, who’s next?

SUE: (Raises her hand.) I guess me. I’m Sue..

BETH: Welcome, Sue. Tell us about your addiction.

SUE: Well, I have thirteen cats. There's Juliet, Bishop, Sophie, Lilly, Tom, Simba, Max, Whiskers, Tango, Iris, Snowball, Sugar, and Blackie.

BETH: Thirteen. Goodness. You must love your little fur babies a lot.

SUE: I do, but that's not the problem. I don't get out much so I... I mean, I mostly stay indoors with my cats. I don't like to leave them, and I... I feel like we're family, you know ... like we're connected ... (Suddenly begins meowing like a cat.) Meow, meow, meow...

EARL: What the heck? (Points.) She thinks she's a cat! (Claps.) That's hilarious!

SUE: Meow, meow, meow ... Do you have any treats? I like treats. Those little square ones are my favorite. You can toss a few on the ground, if you don't have a bowl.

EARL: This is hilarious!

BETH: (Snaps her fingers at EARL.) Stop that! No negative talk!

MIKE: Is it true? You think you're a cat? Hold on! (Takes a small snack out of his pocket and tosses it on the ground.) Here, kitty, kitty, kitty ...

SUE: (Excitedly jumps on the ground and sniffs the snack.) Hey! These aren't the treats I like!

BETH: Sue, perhaps this is the first step for you. Getting out of your house and socializing with uh ... other humans.

SUE: (Rubs against EARL'S leg.) Meow.

EARL: Oh, my gosh! Make her stop! She's rubbing against me like a cat! Look here, lady, I don't like cats! In fact, I'm allergic to them! (Sneezes. SUE hisses.) Did you see that? She hissed at me!

MIKE: (Grabs his phone and dials, unable to control himself. Into the phone.) Mom, it's getting weird in here ... I know it's for strange addictions, but I shouldn't be here! Okay, I'll pay attention ... Love you too. (Hangs up.)

BETH: (To EARL.) Why don't we discuss why you're here? (SUE hisses at EARL.)

EARL: Can you make her stop hissing at me? Okay, well, I'm Earl.

BETH: Tell us about your addiction.

MIKE: Can I call my mom for a second?

BETH: No. Go ahead, Earl.

EARL: Toenails. I collect them. I mean, after I cut them, of course.

MIKE: Weird. I've got to tell my mom about this. (Reaches for his phone.)

BETH: No calls right now. (MIKE FREEZES. It's killing him not to grab the phone.)

EARL: Well, I started doing this when I was seven years old. I thought I'd make a toenail collection. Pretty cool, huh? So, I started putting them in this old tin box. That was twenty years ago. Man! You should see how many I have now! Wish I could sell them on eBay. Think they're worth anything?

BETH: Have you thought about throwing them in the trash?

EARL: That's what my wife said. You sound kind of like my wife. But I said, "Heck no! Do you know how long I've been collecting my toenails?" And you know what she said? "It's either them or me!" So, either I throw them away, or she leaves me!

SUE: (Smiles, purrs, and licks her hands.)

EARL: (Sneezes.) I told you I'm allergic to cats!

MIKE: (Grabs the phone and dials.) Mom, these people are weird with a capital W. (Into the phone.) I don't know. Between the human cat and the toenail collector, I'm starting to freak out.

BETH: So, Earl, what do you love the most? Your old toenails or your wife?

EARL: And that's the question of the day. It's a hard decision for me. I mean, I love my toenail collection. And my friends, at least up to junior high, all thought my collection was cool!

BETH: Seriously? You don't know if you love your wife more than your clipped toenails? (SUE swipes at EARL.) Let's unpack this. Why did you start collecting your toenails?

EARL: Because it was fun! Oh, and I brought some of them - the toenails I've clipped while in therapy. (Pulls out a plastic bag from his pocket.) Want to see?

BETH: No! No! Please, no! I have a better idea. Let's imagine that your wife is here.

EARL: (Sarcastic.) Oh, great.

BETH: Put down the baggie and picture your wife sitting next to you. Now think. Think real hard. Who can you throw your arms around? Who can you kiss? Who makes you feel wonderful on the inside?

EARL: (Grabs the plastic bag and holds it tightly.) I’m keeping my toenails! (Lifts the baggie and kisses it.) I love you! I love you! I love you! (SUE hisses and swipes him again. To SUE.) Stop that! Bad kitty! Bad, bad kitty!

MIKE: (Into the phone.) Mom, this guy in here loves his toenails more than his wife.

BETH: Hang up the phone! Now!

MIKE: Love you! (Hangs up.)

EARL: (Takes off his shoes and socks, then pulls out clippers from his pocket.) Let's just collect some more. Technically, this is group therapy, so they can still go in this bag. (Cuts his toenails.)

MIKE: (Dials.) Mom, I don't like it here. These people are strange. Mom, what are you doing? I miss you.

BETH: (Jumps up.) You people! I just don't know what to say! (Begins doing jumping jacks.) No one is listening to me! How can I help you if you won't listen to me? Do I care? Maybe I only care about myself! About getting into shape. Yes, that's what I care about!

EARL: (Holds up a clipped toenail.) Look at this one!

SUE: (purrs loudly.)

MIKE: (Into the phone.) Mom, I know it's a long drive, but can you come pick me up? I don't think this is working.

BETH: That's it, I'm out of here! (Jogs OFF)

EARL: Man, that is one strange lady!

(LIGHTS FADE to BLACK)
```

---

## IC-1207: Stye of the Eye

- Title: Stye of the Eye
- Author (byline): Christopher Durang
- Work: Durang, Durang
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: May 1997
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, JAKE, MA, DR. MARTINA, AGNES, MTV.
- Teaser before the introduction: Yes
- Spoken words (computed): 2325
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christopher Durang
Book: Durang, Durang
ISBN: 0822214601
Publisher: Dramatists Play Service, Inc.
Date(Month/Year): May 1997
```

### Introduction (context only: never use it for content warnings)

```text
Christopher Durang's "A Stye of the Eye" is theatrical caricature at its best. Those of you familiar with Sam Shepard (all five of you) will appreciate the blatant references to beat-you-over-the-head-with-it symbols, mostly notably from his play A Lie of the Mind. For those of you unfamiliar with Shepard's depictions of the lonesome prairie, untamed masculinity, and incest, the low humor of white trash will keep you entertained for the full twenty-three minutes and nine seconds. With some parody of David Mamet and whoever wrote Agnes of God in there to boot, "A Stye of the Eye" massacres pretentious plays, family values, and a baby lamb. Enjoy.
```

### Performance text (classify this)

```text
CHARACTERS: Jake / Dr. Martina Dysart, a psychiatrist Ma, Jake's mother / Beth, Jake's wife

JAKE: Answer the phone damn it. Answer the phone. [Bangs the phone receiver on the side of the phone, or any other surface.] Come on, come on! [Into receiver.] Hello! Hello!

[Lights up on a different part of the stage. MA is discovered next to a phone, or enters calmly over to the ringing phone. MA is between forty and fifty, and dressed in a sloppy, comfortable print dress. Her hair is not fussed with, just pulled back out of her face. She is a no-nonsense woman, tough, matter-ot-fact, sounds like a Cracker.]

MA: Hello?

JAKE: Hey, Ma?

MA: Who is this?

JAKE: Ma, it's your son.

MA: Who?

JAKE: Your son, ma.

MA: I got two sons. Which one are you?

JAKE: I'm Jake.

MA: Jake?

JAKE: Jake!

MA: You're not the other one? What's his name?

JAKE: Frankie. No, it's not Frankie, Ma. It'sJake.

MA: Jake?

JAKE: Stop saying Jake, or I'm going to come over to your house and punch you in the mouth.

MA: [Her voice warming, friendly.] Oh, now it sounds like Jake. How ar eyou, baby?

JAKE: She's real bad, Ma.

MA: Who, Jake?

JAKE: She's all red and blue and purple.

MA: Who you talkin' about, Jake?

JAKE: I had to hit her. She was dressin' real sexy like, and goin' off to rehearsal.

MA: Who is this you're talkin' about, Jake?

JAKE: It's Beth, Ma. My wife.

MA: Are you married, Jake?

JAKE: Ma, you know I am. You wuz at the wedding.

MA: Why didn't you marry your sister, Jake, she always liked you.

JAKE: That would be incest, Ma.

MA: No, it wouldn't. Incest would be if you married me. If you married your sister, it would be ... sorority.

JAKE: Shut up, Ma. I'm tryin' to tell you I killed Beth.

MA: Who's Beth?

[Note: MA’s lapses in memory are complete. When she says something like "Who~ Beth," she has no recollection whatsoever that she heard the name Beth a few seconds before. So all her questions are asked innocently, trying her best to get information. There is no "what was that thing you said a moment ago" tone to any of her repeating questions. And thus when JAKE seems irritated with her forgetting, she has no idea what is the cause of his frustration. ]

JAKE: She's my wife.

MA: I didn't know you were married.

JAKE: You have the attention span of a gnat. Ma, we've been through this. Beth is my wife, you wuz at the wedding, and I just killed her.

MA: [Suspicious.] Who is this calling me?

JAKE: It's your son, Ma! I just killed my wife.

MA: Well, I never pay attention to the tramps you start up with. She probably asked for it.

JAKE: She was goin' to rehearsal, Ma. She's into actin', Ma, and she's goes off to fuckin' rehearsal, and every day she dresses more slutty like, and I just know that she's doin' it with some fuckin' actor on her lunch break. And I seen her in a play once. She stank. .

MA: [Upset.] Whatcha goin' to plays for, baby? I didn't bring you up to spend your time goin' to plays. You're gonna end up like that Sam Shepard boy down the road. Why don't you settle down and marry your sister?

JAKE: Stop talkin' about incest, Ma. I just killed my wife.

MA: Well, did anyone see you?

JAKE: No.

MA: Well, there, you see. Go get a good night's sleep, and in the morn-ing we'll get you another one. Why don't you marry your sis ... Oh, that's right, you don't like that idea. You're stubborn like your father.

JAKE: I didn't want to kill her, Ma, but she asked for it.

MA: Who you talkin' about, baby?

JAKE: Beth, Beth! How many times do I have to say it!

MA: Thirty-three. I'm getting bored with this conversation, Jake. Is your good brother Frankie there?

JAKE: What?

MA: Put Frankie on.

MA: Frankie, is that you?

JAKE: Wait a minute, Ma.

MA: Did you hear what Jake told me?

JAKE: Hold your horses a minute, Ma. Hey, Frankie! Ma wants to speak to you! Frankie! [Changes personalities, and witches phone hands; sounds more polite and reasoned though still has a temper.] Hey, Mom, how are you?

MA: Oh, Frankie, I love it the way you call me "Mom" and Jake calls me "Ma." It's so differentiating. Frankie, did you hear that Jake killed his wife?

JAKE: He told me, Mom. He's a crazy, spoiled, mixed up kid. Mom, what are we gonna do about Jake?

MA: Who?

JAKE: Jake.

MA: Jake's dead. His wife just killed him.

JAKE: You got it backwards, Ma. I mean "Mom."

MA: You know you and Jake sound so much alike that sometimes I think you're both two different aspects of the same personality. That means I gave birth to a symbol, and me with no college edjacation.

JAKE: I'm not a symbol, Ma. I'm a westerner looking for the big open expanses, but they're gettin' smaller and smaller. There's no place to hope, Ma.

MA: You sound like a symbol. But not some prissy Ivy League-type symbol. My children are virile, masculine symbols who carry guns and beat up women. You all got so much testosterone in you, that you got a native kinda poetry in you, even when you spit. Why don't you go kill a woman like your brother?

JAKE: But what woman is like my brother?

MA: That's not what I meant, stupid. The verb was implied in that sentence, as in "Why don't you go kill a woman like your brother did, " "did" in imaginary bracket signs. And me with no college edjacation. Put Jake back on the line, honey, I'm bored with this conversation. No, never mind, I got an idea. Why don't you go try to find Beth. Maybe she's not dead. Maybe she's only brain damaged, and you can marry her. That might have symbolic value of some sort.

JAKE: But what symbolic value would that have, Ma?

MA: I don't know, I'm not a writer. But if we put some jazz music under it, or some good country sounds, it's bound to mean somethin' to somebody. I gotta go now, Frankie, the cactus is whistHn' on the stove. But you keep an eye on your brother, and if you wanna marry your sister, just let me know. [Hangs up, exits; lights fade on her part of the stage.]

JAKE: Goodbye, Mom. [Switches to JAKE personality; grabs for phone from himself] Hey, I ain't done talkin' to her yet! [Switches back to Frankie, hangs up the phone.] Well, she's done talkin' to you. Why'd you go and kill her, Jake? [Switches to JAKE.] Ma? [Switches to Frankie, annoyed.] No, not Mom. Beth. [Switches to JAKE.] I don't know. She just kept goin' to all them rehearsals and ... well, it irritated me. [Switches to Frankie.] I can understand that. [Switches to JAKE; vehement.] Especially this one play called "Agnes is Odd" or some such thing, all about this flakey nun who killed her baby.

[Lights change. We see the play JAKE is remembering. JAKE plays the role of Dr. Martina Dysart] The sound of Stravinsky-like music, or Carmina Burana. Startling, mysterious, otherworldly.

Enter DR. MARTINA DYSART, in a crisp business suit, smoking three cigarettes, one in her mouth, two in her hands. She takes the one in her mouth out, and addresses the audience. She is intense and concerned, solving a deep mystery.]

DR. MARTINA: The baby was-discovered in a waste basket with the umbilical cord knotted around its neck. The mother was unconscious, next to the body. The mother was a young nun called Sister Agnes, Sister Agnes Dei. During the night she had given birth and then seemingly killed her baby. Then she went out to the convent stables and blinded eight horses with a metal crucifix. That much is fact. But she is also a musical genius along the lines of Wolfgang Amadeus Mozart. Furthermore, my life as a psychiatrist is drab and depressing, and even though I think it unappealing that she killed her baby and blinded the horses, still I envy her passion. You wouldn't see me getting up in the middle of the night to go down to the stables. And furthermore, I'm a lapsed Catholic who wishes I had her faith, and I wish I had a horse, and I ... wish I was a composer. In short, there are many ideas and subtleties to think about here, so stop rattling your programs and let's move on with it. My first meeting with Agnes, I thought she was brain damaged. [Enter SISTER AGNES, the sensitive nun. Dressed perhaps in the strange white nun ~ outfit Amanda Plummer wore in the Broadway version of ''Agnes of God, "which is the same design Sally Field wore in "The Flying Nun" tv series. Or a more conventional nun outfit is okay too.

JAKE’s wife BETH is playing SISTER AGNES. Actress formerly playing “MA” plays the role of BETH”

AGNES: Look, stigmata. [AGNES holds out her palms, which at first glance have gaping red holes in them. A second later one notices that she seems to be holding red rubber things in her palms, with reddish centers to them.]

DR. MARTINA: Nonsense, those are plastic Dr. Spock ears. Look, I'll show you. [D R. MARTINA removes the ''plastic stigmata" and puts the Dr. Spock ears on her ears. She leaves them there for the rest of the scene.] People sell these at Halloween. Do you like Halloween, Agnes?

AGNES: Pooh. Pooh.

DR. MARTINA: Pooh. Winnie the Pooh? Do you like Winnie the Pooh?

AGNES: Pooh. Pooh. Puer. [Last word is pronounced "Pooh-air. '1

DR. MARTINA: Puer. That's Latin for boy. Do you like boys, Agnes?

AGNES: Pooh-ella.

DR. MARTINA: Yes, puella. Latin for girl. Maybe it's Latin you like. Do you like Latin, Agnes? Hie, haec, hoc, and all that.

AGNES: Puer. Puella. Eck, eck, equus! [Momentarily mimes blinding horses, then pulls herself together again.]

DR. MARTINA: Boy, girl, horse. This isn't a very intelligent conversation, Agnes. Don't they make you speak sentences in the convent, Agnes?

AGNES: Agnes Dei.

DR. MARTINA: Yes, that's Latin for Lamb of God. [With a shock of recognition.] Oh my God, your name is Agnes Dei, isn't it? Good grief, I wonder if that means you're some sort of sacrificial lamb to God, and that maybe your giving birth was an immaculate conception, and that the father is God Himselfl!! Good Lord, what a shocking idea, oh my mind is running, let me try to breath deeply for a moment. [Puffs on several of her cigarettes.] Goodness, what dreadful rubbish I was just speaking. Rather like speaking in tongues. Do you like tongues, Agnes?

AGNES: We had tongue sandwiches at that convent, and it made all the Sisters menstruate.

DR. MARTINA: [Pause.] I think. that's rather an obscene remark you've just made, Agnes. Did you mean to be obscene?

AGNES: Children should be obscene. And not furred.

DR. MARTINA: Furred?

AGNES: Furred like a bird.

DR. MARTINA: What is the matter with you exactly? Are you a saint or are you brain damaged?

AGNES: [Sings, lasciviously.]Erotic, erotic, Put your hands all over my body!

DR. MARTINA: I see. Well, if you're going to sing, I think I'll go now. By the way, which member of the convent is it who won't let you watch MTV? [Shudders to herself] What a sharp remark of mine. I'm definitely in the right profession.

AGNES: No do with MTV.:

DR. MARTINA: Of course, it do. Does. That's the kind of song that's sung on

MTV.:

AGNES: Noooooooo. Who sing, Doctor?

DR. MARTINA: I forget. That slutty woman who changes her look all the time, whats-her-name ... oh my God, her name is Madonna, which means "Mother of God!" [AGNES has a screaming fit at this scary coincidence, and falls to the ground rolling around in circles, going "Whoop! Whoop! Whooop!'1

AGNES: Whoop! Whoop! VVhoop! Whoop! Whoop!

[Lights back up on JAKE.]

JAKE: [As JAKE; explaining to Frankie.] It was after that terrible play that I took Beth out in the parking lot and I beat her to a pulp. "Your play was pretentious!" I said, and then I punched her. "You were unconvincing as a nun, and I didn't know whether you were supposed to be crazy or sane," and then I kicked her in the side. "And I don't like the previous play you wuz in, "The Reluctant Debutante," either, and then I took her head and I put it under the tire of the Chevrolet, and I dropped it on her. And that's how I killed her. [Switches to Frankie.] Oh, Jake. The play couldn't have been that bad. [Switches to JAKE.] It was. It was. I fuckin' hated it, man. It made me wanna puke. [Switches to Frankie.] Yeah, but to kill someone. [Switches to JAKE; big baby, teary.] Oh, Frankie, I miss her already. I wish she was alive so we could go on a second honeymoon together. [Switches to Frankie.] I got some land in Florida I could sell ya. [Switches to JAKE.] Oh yeah? [Switches to Frankie.] It's called Glen Gary Glen Ross. [Switches to JAKE.] Oh I don't want to go there. [Switches to Frankie, who now speaks in a fast, staccato rhythm, with a lot of aggressive salesman energy.] Why the fuck not? The place is good. Not great maybe, but what I'm sayin' is, it's good. Not great maybe, but good. That's what I'm sayin'. It may be swamp, it may have bugs, but fuck, Jake, what's perfect? You tell me. No, don't tell me, I'll tell you. It's not great, good. Am I right? Do you understand what I'm sayin'? Should I say it again? What I'm sayin' is, fuck shit piss damn, it ain't half bad. Half good, half bad. You gotta settle. It ain't perfect. Settle. Gatta. You gotta settle. A negotiation. Give and take. You know what I'm sayin'? What I'm sayin' is ... [Switches to JAKE, frustrated and angered by Frankie’s irritating sales pitch.] Shut up! I know what you're saying, you sound life-like, granted, but you repeat yourself and you're monotonous, and you're ... insensitive to my upset about my wife. She is dead, you know. I deserve sympathy. [Switches to Frankie.] Yeah, but you killed her.
```

---

## IC-1208: Sweet Tooth

- Title: Sweet Tooth
- Author (byline): Margi Palatini
- Work: Not specified
- Publisher: Simon and Schuster
- Publication date as stated: Aug 2004
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, SWEET TOOTH, STEWART, MOTHER, DAD, GRANDMOTHER, STUART, MRS. FINNEGAN, CROWD, MOTHER/DAD, SISTER, UMPIRE, BABY TEETH, CANINE TOOTH, WISDOM TOOTH, TOOTH, TOOTH FAIRY
- Teaser before the introduction: Yes
- Spoken words (computed): 1121
- Already set (do not supply): none

### Source block (context only)

```text
Author: Margi Palatini
ISBN: 978-0689851599
Publisher: Simon and Schuster
Date (Month/Year): Aug 2004
```

### Introduction (context only: never use it for content warnings)

```text
Sweet Tooth by Margi Palatini
```

### Performance text (classify this)

```text
NARRATOR: This is Stewart. Your typical, average, everyday kid. Except for one thing.

SWEET TOOTH: Iii oo-er ere.

NARRATOR: Ahh, yes. There it is all right. The molar in the back. You're probably saying, "A tooth? What's the big deal about a tooth?" And ordinarily you would be correct. . . . But that is no ordinary tooth. Uh-uh. This is Stewart's sweet tooth. One nagging, annoying, demanding . . .

SWEET TOOTH: (Loudly) BLAH. BLAH. BLAH. ENOUGH WITH THE YAKKIN'. I NEED A CANDY BAR. NOW-OW!

NARRATOR: . . . very loud, sweet tooth.

.

SWEET TOOTH: "DOES IT HAVE THAT GOOEY STUFF IN THE MIDDLE? 'CAUSE IT'S GOT TO HAVE THAT GOOEY STUFF IN THE MID-DLE!"

STEWART: (Cramming a candy bar into his mouth, chewing loudly and gulping) There. Satisfied?

SWEET TOOTH: AHHHHH . . . SWEET!

NARRATOR: Yes, a tooth that wants what it wants, when it wants it . . . and lets everybody know it. Take, for example, two years ago at cousin Charlotte's wedding . . . Stewart was on his best behavior. His shoes were shined. Bowtie straight. Hands were spotless. Grandfather had just lifted his glass to toast the bride and groom when . . .

SWEET TOOTH: I'm fallin' asleep here! Come on. Move it along, Gramps. Cut the cake. Time to cut the cake. I want the end hunk with all that iiiiii-icing.

MOTHER: (through a gritted smile) I don't know him.

DAD: (under his breath) He doesn't belong to me.

GRANDMOTHER: (muttering) Who is that boy?

NARRATOR: Stewart wiped the pink rose from his lips.

STUART: It's The Sweet Tooth.

NARRATOR: It was not a pretty picture . . . The Tooth was no better behaved in school. Stewart had enough detention slips to wallpaper his room. Why, just two weeks ago in geography class . . .

MRS. FINNEGAN: Who can tell me the capital of North Dakota?”

SWEET TOOTH: (muffled) Jelly beans

NARRATOR: said a muffled voice from the back of the room.

MRS. FINNEGAN: Did you say something, Stewart?

SWEET TOOTH: Licorice.

MRS. FINNEGAN: Stewart, I'm afraid I can't hear your answer.

SWEET TOOTH: Lollipops.

MRS. FINNEGAN: You're going to have to speak up, Stewart.

SWEET TOOTH: Hey! I'm dying here for a couple of CHOCOLATE PEANUT BUTIER CUPS, OKAY?!

NARRATOR: Detention slip number 432.

STEWART: (as he is lead away to the principal’s office) But, I'm telling you, it's not me, It's The Tooth! *******************

NARRATOR: The movies? You don't really want to go there, do you? . . . Not with Stewart, anyway.

SWEET TOOTH: Would somebody pass the yummy yummys, already?!

CROWD: SHHHHHHHHHHHHH!

STEWART: (chewing) Don't look at me . . . It's The Tooth.

NARRATOR: And of course there was the unforgettable "Easter Basket Mishap." Now that was really ugly. That Sunday A.M. the family awoke to find jelly beans littering the living room. Marshmallow chicks were missing. The trail of crumpled yellow foil wrappers led to one person, and one person only.

MOTHER/DAD: (disappointed) Ooooh, Stewart.

SISTER: (whimpering and closing her eyes) I can't look.

STEWART: (moaning and rubbing his belly-aching stomach) Those chocolate bunnies never had a chance . . . It was The Tooth.

SWEET TOOTH: HEY! CAN WE STOP GOING DOWN MEMORY LANE HERE AND OPEN UP THAT BAG OF COOKIES?

STEWART: That's it. I've had enough!

SWEET TOOTH: ENOUGH? I HAVEN'T EVEN HAD ONE.

STEWART: (shouting) No more cookies! No more candy. No more cake. No more nothing!

SWEET TOOTH: That's no more anything. And . . . WHO DO YOU THINK YOU'RE KIDDING, KID? Bring on those chocolate chips!"

NARRATOR: Stewart sighed. What choice did he have? He was a boy with one big Sweet Tooth. He tore open the bag. He grabbed one, then two-three-four cookies. He opened his mouth.

SWEET TOOTH: (shouting) COME TO PAPA!

NARRATOR: Stewart stopped.

SWEET TOOTH: What are you waiting for, kid? Come on. Cookie. Cookie. Cookie. Cookie.

NARRATOR: Stewart dropped the cookies. But . . . . not in his mouth.

STEWART: (determined) It's over, Tooth. I’m cutting you off. Starting right now. It's cold turkey.

SWEET TOOTH: Cold turkey? Yee-ech! I hate cold turkey . . . unless you add a little cranberry sauce,

STEWART: Didn't you hear me, Tooth? I said it's over. From now on there's nothing for you but a . . . a . . . a . . . (large gulp) Healthy diet.

SWEET TOOTH: (wailing) Healthy? Kid, say you don't mean it.

NARRATOR: But Stewart meant it, all right. He meant every word. Yes, it was trying. Yes, it was difficult. Okay, it was darn near impossible. But Stewart stayed strong. For The Tooth it was a different story.

SWEET TOOTH: PEAS? YOU'RE GIVING ME PEAS? LITILE DRY GREEN VEGGIE MARBLES? Broccoli? You're feeding me a shrub? THAT'S NOT GOING TO DO IT. DESSERT! WHERE'S DESSERT? I'm begging you. WHEN DO WE GET TO THE GOOD STUFF?"

STEWART: (putting his hands over his ears) I can't hear you.

NARRATOR: Strong. He stayed strong.

SWEET TOOTH: Just one eensy-teensy CHOCOLATE-COVERED PEANUT before hitting the sack. How about it? . . . A nosh. A nibble. A breath mint. Somethin'!

STEWART: (turning out the light) Forget it.

NARRATOR: Strong. Strong.

SWEET TOOTH: (at breakfast the next morning as Stewart eats his cereal) COME ON. WHADDAYA SAY? ONE SPOONFUL OF SUGAR.

NARRATOR: Stewart shook his head.

SWEET TOOTH: (losing his grip) A DROP OF CHOCOLATE MILK. One measly little crumb-bun crumb.

STEWART: No way.

NARRATOR: Very strong.

SWEET TOOTH: (shouting) HEY, WATCH THAT TOOTHBRUSH! AND KEEP THAT TONGUE OF YOURS ON THE OTHER SIDE OF YOUR MOUTH. TRYIN' TO WIGGLE ME OUT OF HERE, HUH? Well, I'm not going, kid. I'm not going anywhere! Do you hear me? . . . Do you hear me?"

NARRATOR: Stewart brushed. Flossed. Gargled.

SWEET TOOTH: (moaning weakly) U-u-ugh He's not hearing me . . . I'll get you for this, kid.

NARRATOR: Stewart smiled. He was winning. Oh yes, he was winning. Three days passed. The Tooth was quiet. Very quiet. Almost too quiet. But Stewart wasn't thinking "tooth." He was thinking baseball. It was the biggest game of the season. Bottom of the ninth. Stewart was at the plate. Runners were on second and third. Two outs. Two strikes. The crowd was on their feet. The game was on the line. Stewart's team was down by one run. The pitcher went into his windup. There was a hush from the stands. A big fat fastball was heading for the plate. It was all up to Stewart. And then . . .

SWEET TOOTH: BOY, COULD I GO FOR A HUNK OF BUBBLE GUM RIGHT NOW!

NARRATOR: Swing! Swish!

SWEET TOOTH: Heh-heh-heh.

UMPIRE: (yelling) Strike three! Y'er out!

SWEET TOOTH: Gotcha! Now go get me some goodies!

STEWART: (mumbling as he drops the bat) I'll get you goodies.

NARRATOR: Home he marched. Into the kitchen. Straight for the refrigerator. He yanked open the door. Rustled through the vegetable bin. He flung lettuce. He tossed tomatoes. He hurled a head of cauliflower. And then he pulled out . . . .a carrot. That's right. A carrot.

STEWART: (defiantly as he lifts the carrot above his head) It's over for you, Tooth.

SISTER: (wide-eyed) What are you going to do with that?

NARRATOR: Stewart grinned. He opened his mouth wide. Very wide.

SWEET TOOTH: KID! NO! NOT THE CARROT! NOT THE CARROT!"

STEWART: (shouting) Yes. The carrot!

SWEET TOOTH: No, kid, no!

SISTER: (covering her eyes) Am I too young to be watching this?

NARRATOR: Closer. Closer. Closer. And then . . . . CR-CR-CRUNCH.

SWEET TOOTH: Ahhh-ahh-ahhhhh . . . So long, sweet world! . . . What a way to go . . . Done in by an orange veggie.

NARRATOR: Stewart rubbed his jaw. He stared at the carrot . . . (the tooth is in his hand) and The Tooth. It was over.

SISTER: What's going to happen to it?

NARRATOR: Stewart placed the molar under his pillow, then looked at his sister.

STEWART: (smiling) Who knows? That's the tooth fairy's problem now.

**************** [In the Tooth Fairy’s Bag of Teeth] ****************

BABY TEETH: WAH, WAH, WAH!

CANINE TOOTH: WOOF!

WISDOM TOOTH: Please be quiet. I’m trying to read.

TOOTH: Pipe down, wise guy! What does a sweet tooth have to do to get an ice-cream sundae around here? With hot fudge! And throw some sprinkles on it while you’re at it.

TOOTH FAIRY: ROTTEN TEETH!
```

---

## IC-1209: The Tale of Despereaux

- Title: The Tale of Despereaux
- Author (byline): Kate DiCamillo
- Work: Not specified
- Publisher: Candlewick
- Publication date as stated: April 2006
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MOTHER, BROTHER, FATHER, AUNT, UNCLE, DESPEREAUX, PEA, KING, BROTHER MOUSE, LESTER, ANTOINETTE, HM, MOUSE, ROSCURO, QUEEN, COOK, MIG, RAT
- Teaser before the introduction: Yes
- Spoken words (computed): 1760
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kate DiCamillo
ISBN: 978-0763625290
Publisher: Candlewick
Date (Month/Year): April 2006
```

### Introduction (context only: never use it for content warnings)

```text
The Tale of Dexpereaux by Kate DiCamillo
```

### Performance text (classify this)

```text
NARRATOR: This story begins within the walls of a castle, with the birth of a mouse. The only one of his litter to be born alive.

MOTHER: Just the one. It is such the disappointment. I will name this mouse Despereaux, for all the sadness, for the many despairs in this place. Now, where is my mirror?

NARRATOR: The other, older mice children gathered around to stare.

BROTHER: Look, his eyes are open. They shouldn’t be open.

NARRATOR: Despereaux’s eyes should not have been open. But they were.

FATHER: He’ll be dead soon. He can’t live with his eyes open like that.

NARRATOR: But he did live. This is his story.

NARRATOR: Despereaux Tilling lived, but his existence was cause for much speculation in the mouse community.

AUNT: He’s the smallest mouse I’ve ever seen. No mouse has ever been this small.

UNCLE: Those are some big ears he’s got.

AUNT: They are obscenely large.

NARRATOR: Despereaux said nothing in defense of himself. Everything they said was true. And he was sickly. He coughed and sneezed so often that he carried a handkerchief in one paw at all times.

TRANSITION: Despereaux discovered a sound. The sound was music. King Phillip playing his guitar to his daughter, the Princess Pea. Hidden in a hole in the wall the mouse listened.

DESPEREAUX: Oh, it sounds like heaven. It smells like honey.

NARRATOR: Now, Despereaux did adhere to one of the most basic of all mice rules: Do not ever reveal yourself to humans. But…The music made him lose his head, and he was spied by the Princess Pea.

PEA: Oh, look, a mouse.

KING: That my dear Pea, is a bug, not a mouse.

PEA: No, no, it’s a mouse. I think he was listening to the music. Play something Papa.

KING: A king play music for a bug?

PEA: I told you, he’s a mouse.

KING: Oh, well, if it will make you happy, I will play music for a bug.

NARRATOR: Despereaux forgot all his fear. He only wanted to hear the music. The princess smiled at Despereaux, and Despereaux smiled back. The mouse fell in love.

TRANSITION: Despereaux’s brother happened to scurry past the princess’s room. He saw the princess touching the top of his brother’s head.

BROTHER MOUSE: He’s nuts! He’s a goner!

PEA: Papa, I am going to keep this mouse.

KING: A mouse? Mice are rodents. They are related to rats. You know of our own dark history with rats.

PEA: “But, he is not a rat. He’s a mouse.

KING: Put him down. Scat!

PEA: “Please, don’t be mean to him.

DESPEREAUX: My name is Despereaux! I honor you!

KING: Get out! Rodents know nothing of honor.

NARRATOR: Despereaux’s brother went off to tell his father the terrible news of what he had just seen.

LESTER: He simply cannot be my son.

ANTOINETTE: What do you mean he is not your son? That is a ridiculous statement. Why must you always make the ridiculous statements?

LESTER: Sitting at the foot of a human king. Unthinkable!

ANTOINETTE: Oh, so dramatic.

LESTER: I will call a special meeting of the Mouse Council. Together, we will decide what must be done.

ANTOINETTE: Oh, you and this council of the mouse. It is a waste of the time in my opinion.

TRANSITION: The mouse council gathered in a secret hole. The mice listened in horror while Despereaux’s father related the story of what Furlough had seen.

HM: Despereaux Tilling.

NARRATOR: Said the head mouse.

DESPEREAUX: Yes, sir.

HM: We, the members of the Mouse Council have discussed you behavior. We will give you a chance to defend yourself against these rumors of your egregious acts. Did you or did you not sit at the foot of the human king?

DESPEREAUX: I did.

HM: Did you allow the girl human to touch you?

DESPEREAUX: I did, sir. Her name is Pea. But..

HM: Very well. We have no choice. You will die.

NARRATOR: Despereaux marveled at his own bravery. He admired his own defiance. And then, he fainted. Two mice came forward.

MOUSE: We will escort you to the dungeon.

ANTOINETTE: What will happen to him? What will happen to my baby?

MOUSE: The rats will eat him. (Antoinette swoons)

TRANSITION: Together the three mice traveled down. Despereaux was suddenly pushed from behind. It sent Despereaux flying down the stairs into the dungeon.

NARRATOR: As our story continues, we must go backward in time to the birth of a rat, a rat called Roscuro, a rat born in the darkness of the dungeon. Roscuro showed an abnormal interest in illumination. He was always on the lookout for light. His rat soul longed for it. The door to the dungeon was flung open and a brilliant shaft of light cut into the dark of the dungeon.

ROSCURO: Beautiful. I must see more light. I must go upstairs.

TRANSITION: Imagine having spent your life in a dungeon. One day, you step out of the dark and into a world of bright windows and polished floors.

ROSCURO: I will never leave. No, It is here that I belong.

NARRATOR: The rat waltzed from room to room until he found himself at the banquet hall. He looked and saw King Phillip, Queen Rosemary, the Princess Pea, and all the king’s men.

ROSCURO: Oh. Suffering is not the answer. Light is the answer.

NARRATOR: Roscuro flung himself onto the lowest branch of the chandelier. The Princess Pea spotted him.

PEA: A rat is hanging from the chandelier!

ROSCURO: Rat….

NARRATOR: It became clear that it was an extremely distasteful syllable. This revelation hit Roscuro with such a force, that it made him lose his grip on the chandelier. The rat fell. Right into the queen’s bowl of soup.

PEA: See? It is a rat. He is in Mama’s soup!

NARRATOR: In the spirit of honesty, I must utter a difficult and unsavory truth: Rats are not beautiful creatures.

QUEEN: Nneiggghhhiiinnnnkkkkk! There is a rat in my soup!

NARRATOR: The queen was a simple soul and always had done nothing but state the overly obvious. She died as she lived. Soup was outlawed in the Kingdom of Dor.

ROSCURO: I will make the princess suffer for how she looked at me. (SCENE BREAKE)

COOK: This is what you do. You take the tray of food down to the dungeon, wait for the man to eat the food, and then you bring the tray back up. Do you think you can manage that?

NARRATOR: Said Cook.

MIG: Aye, I reckon so.

NARRATOR: Said the serving girl, Mig.

COOK: I’m sure you’ll find a way to bungle it.

NARRATOR: Mig went happily down the twisting stairs.

MIG: I ain’t the Princess Pea / But someday I will be, / The Pea, ha-hee Someday, I will be.

ROSCURO: May I detain you for a moment? (Mig looks around) Down here.

MIG: You’re a rat ain’t you?

ROSCURO: There is no need to panic. How do you do.

MIG: A rat with manners.

ROSCURO: Allow me to introduce myself. I am Roscuro. Am I right in ascertaining that you have aspirations?

MIG: What?

ROSCURO: Aspirations, my dear, are those things that would make a serving girl wish to be a princess.

MIG: A princess is exactly what I want to be.

ROSCURO: May I illustrate for you how we can make your dream a reality?

NARRATOR: Neither noticed as a napkin on the tray moved, nor did they hear the small mouse like noises of outrage that issued from that napkin as Roscuro went on unfolding his diabolical plan. Mig, after her conversation with Roscuro, carried the tray into the kitchen. Despereaux tumbled out of the napkin.

COOK: Kill him!

NARRATOR: Shouted Cook.

MIG: (chop) I missed him. I got the little meecy’s tail, though.

COOK: So? What good will that do us when the rest of him has disappeared into the pantry?

NARRATOR: Despereaux cried for what he had lost. But he also cried because he was happy. He was out of the dungeon just in time to save the Princess Pea from the terrible fate that the rat had planned for her.

TRANSITION: Roscuro put his terrible plan into effect. The serving girl Mig climbed the stairs to the princess‘s room. In her pockets were the rat and a knife.

ROSCURO: Do I need to review with you again our plan?

MIG: I got it straight right here in my head.

ROSCURO: How comforting.

MIG: We go into the princess’s room and I will wake her up and say “you must come with me.” We take her to the deep downs and we gives me some lessons in how to be a princess and when we is all done studding up, I gets to be princess!

NARRATOR: The sun rose and Despereaux awoke. But he awoke too late. The princess was gone. Having heard Roscuro’s plan, Despereaux knew that the princess was hidden in the dungeon. So the small mouse slipped out of the pantry. Desperaux: “I will be the knight in shining armor. It has to be me.

COOK: A mouse! For the first time, I am glad to see a mouse. A mouse is not a king’s man here to punish me for making soup. A mouse. A mouse with a needle tied around his waist. Ho-hee. That is soup you are smelling.

NARRATOR: She took a saucer and spooned some soup into it and set it on the floor. Oh, it was lovely. He drank the soup and when he stepped out of the saucer, his whiskers dripping.

COOK: You must want more.

DESPEREAUX: I don’t have time. I’m on my way to the dungeon to save the princess.

COOK: Well don’t let me stand in your way.

TRANSITION: Despereaux stood at the top of the dungeon.

DESPEREAUX: “Oh my.”

NARRATOR: `But his heart was full of love for the princess and Despereaux felt brave and strong.

RAT: Welcome, welcome. You are armed. How charming. I surrender!

DESPEREAUX: I don’t want to hurt you. I’m… I am on a quest to save the princess.

RAT: How inspiring. What if I told you that I that I could take you directly to her?

DESPEREAUX: But why? You are a. . .

RAT: A rat, yes. Come, come. I will lead you to your princess. I promise. (Scene Break)

DESPEREAUX: Princess! Princess, I have come to save you!

PEA: Despereaux.

NARRATOR: But Roscuro, baring his teeth, blocked the mouse’s way.

MIG: Don’t worry, princess, I will save the meecy. (Chop) Whoopsie

NARRATOR: Roscuro turned to look at where his tail had been and Despereaux drew his needle and placed the sharp tip right where the rat’s heart should be.

DESPEREAUX: Don’t move.

ROSCURO: Ha…what is that smell? There’s something…Soup.

PEA: Roscuro, …would you like some soup.

ROSCURO: Don’t torment me.

PEA: I promise you that if you lead us out of here, I will get Cook to make you some soup.

ROSCURO: Soup?

PEA: Yes. Truly I promise. Let’s go upstairs. Let’s eat some soup.

NARRATOR: Imagine a king and princess, serving girl and a rat, all gathered in a banquet hall. Sitting in the place of honor, is a very small mouse with big ears. Peeking out from behind a curtain, are mice.

ANTOINETTE: He lives, he lives!
```

---

## IC-1210: Thidwick, the Big-Hearted Moose

- Title: Thidwick, the Big-Hearted Moose
- Author (byline): Theo Geisel (aka Dr. Seuss)
- Work: Not specified
- Publisher: Random House
- Publication date as stated: Sept 1948
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, BINGLE BUG, THIDWICK, TREE SPIDER, ZINN-A-ZU BIRD, FRIENDS, HERNAN THE SQUIRREL, WOODPECKER, GUESTS, HUNTER
- Teaser before the introduction: No
- Spoken words (computed): 1269
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theo Geisel (aka Dr. Seuss)
ISBN: 978-0394800868
Publisher: Random House
Date (Month/Year): Sept 1948
```

### Introduction (context only: never use it for content warnings)

```text
What happens when well-meaning, productive types offer a (literal) free ride to those less willing to take responsibility for themselves? Consider the wide expanse of social services offered by American society today: welfare, public education, health services, (insert any variety of other public programs here). When does helping become enabling and when is enough enough?

In 1991, a few weeks before his death, friends asked Seuss if there were anything he might have left unsaid to all the children out there. Seuss replied, “The best slogan I can think of to leave with the kids of the U.S.A. would be ‘We can . . . and we’ve got to . . . do better than this.’

Thidwick, the Big-Hearted Moose by Theo Geisel (aka Dr. Seuss) is definitely more than a children’s story – it is a cautionary tale – for individuals and societies.
```

### Performance text (classify this)

```text
NARRATOR: Up at the Lake Winna-Bango . . . the far northern shore . . . Lives a huge herd of moose, about sixty or more, And they all go around in a big happy bunch, looking for nice, tender moose-moss to munch.

Up at the lake Winna- Bango, one day, they were lunching, Just strolling along and enjoying their munching . . . (For the moose-moss that day was especially fine) . . . When it happened that Thidwick, the last moose in line, saw a Bingle Bug sitting. The bug called out,

BINGLE BUG: Hey! It’s such a long road, and it’s such a hot day, Would you mind if I rode on your horns for a way?

THIDWICK: (Smiling) Of course not! I’m happy my antlers can be of some use. There’s room there to spare, and I’m happy to share! Be my guest and I hope that you’re comfortable there!

NARRATOR: So the Bingle Bug picked out a nice easy seat and the moose went on looking for moose-moss to eat. Well . . . An hour or so later The bug heard a squeak, and he heard the small voice of a Tree-Spider speak.

TREE SPIDER: I say! You’ve got a nice place! That moose seems quite friendly, Has such a nice face . . . If I got on, too, Do you think he would mind. . ?

BINGLE BUG: (laughing) Hop aboard! And I think that you’ll find that moose won’t object. He’s the big-hearted kind!

TREE SPIDER: (with joy and delight) I accept.

NARRATOR: And he started a web horn to the right. While the spider was spinning, he heard a gay song and a fresh little Zinn-a-zu bird came along. He stopped. And he stared. And he chirped

ZINN-A-ZU BIRD: Well! Well! WELL! What a smart place to build! What a great place to dwell! I’ve been living on trees ever since I was born, but here’s something new! Why not live in a horn! If there’s room there for two, then there’s room there for three!

BINGLE BUG: (laughing) There’s plenty of room! And it’s free!

NARRATOR: Thidwick stopped walking. What was all that talking? These guests had caught Thidwick the Moose unawares.

THIDWICK: Hey! What goes on there upstairs?

ZINN-A-ZU BIRD: Just building a nest, sir.

NARRATOR: The Zinn-a-zu said and began yanking hairs out of poor Thidwick’s head. And he plucked out exactly two hundred and four!

ZINN-A-ZU BIRD: Don’t worry, you can always grow more!

NARRATOR: Then he dozed off to sleep in his fine moose hair nest.

THIDWICK: This bird is sort of a pest! But I’m a good sport, so I’ll just let him rest, for a host, above all, must be nice to his guest. Besides, now, it’s getting quite late in the day and surely tomorrow they’ll all go away.

NARRATOR: But, alas! The next morning the sun’s early light brought to Thidwick’s sad eyes a most unwelcome sight…

ZINN-A-ZU BIRD: Meet my wife! I was married last night. And, perhaps by the way, I should mention to you that her uncle is coming to live with us, too. You’re a very fine host so I knew you’d be willing. . .

NARRATOR: Then the uncle, a woodpecker, started in drilling! . . . All Thidwick’s friends shouted

FRIENDS: GET RID OF THOSE PESTS!

THIDWICK: (sobbing) I would, but I can’t. . . . They’re guests!

FRIENDS: Guests indeed! (frowning) If those are your guests, we don’t want you around! You can’t stay with us, ’cause you’re just not our sort!

NARRATOR: And they all turned their backs and walked off with a snort. Now the big friendless moose walked alone and forlorn, with four great big woodpecker holes in his horn.

HERNAN THE SQUIRREL: (whispering) What holes! What holes to hide nuts in! Hmmm! Mind if I tried ’em?

WOODPECKER: They’re yours! Get right inside ’em! This big-hearted moose runs a public hotel! Bring your nuts! Bring your wife! Bring your children as well!”

NARRATOR: So the whole squirrel family all jumped on, pell mell. And the very next thing the poor animal knew, a bobcat and turtle were living there, too! NOW what was the big-hearted moose going to do? Well what would YOU do if it happened to YOU? You couldn’t say “Skat!” ’cause that wouldn’t be right. You couldn’t shout “Scram!” ’cause that isn’t polite. A host has to put up with all kinds of pests, for a host, above all, must be nice to his guests. So you’d try hard to smile, and you’d try to look sweet and you’d go right on looking for moose-moss to eat.

But now it was winter and that wasn’t easy, for moose-moss gets scarce when the weather gets freezy. The food was soon gone on the cold northern shore of Lake Winna-Bango. There just was no more! And all Thidwick’s friends swam away in a bunch to the south of the lake where there’s moose-moss to munch. He watched the herd leaving. And then Thidwick knew he’d starve if he stayed here! He’d have to go, too! He stepped in the water. Then, oh! What a fuss!

GUESTS: (screaming) STOP! You can’t do this to us! These horns are our home and you’ve no right to take our home to the far distant side of the lake!

THIDWICK: (begging) Be fair! (swallowing a lump in this throat)

BINGLE BUG: We’re fair. We’ll decide this by vote. All those in favor of going, say ‘AYE,’ all those in favor of staying say ‘NAY’.

THIDWICK: (shouting) AYE!

GUESTS: (yelling) NAY!

NARRATOR: But when he was done . . He lost ’leven to one.

GUESTS: We win! By a very large score!

NARRATOR: And poor, starving Thidwick climbed back on the shore. Then, do you know what those pests did? They asked in some more! They asked in a fox, who jumped in from the trees, they asked in some mice and they asked in some fleas. They asked a big bear in and then, if you please, came a swarm of three hundred and sixty-two bees! Poor Thidwick sank down, with a groan, to his knees. And then, THEN came something that made his heart freeze.

Bullets came zinging right past Thidwick’s face! Guns were bang-binging all over the place!

HUNTER: Get that moose! Get that moose! Fire again and again and shoot straight one and all! We must get his head for the Harvard club wall!”

NARRATOR: Thidwick took to his heels with that load on his head! With five hundred pounds on his horns, the moose fled! He could have run faster without all those pests, but a host, above all, must be nice to his guests. Up canyon! Off cliff! Over wild rocky trail! With bullets bang-bouncing around him like hail! Up gully! Through gulch! And down slippery sluice, with his hard-hearted guests raced the soft-hearted moose!

Then finally they had him! Because of those pests, he had run out of luck, because of those guests on his horns, he was stuck! He gasped! He felt faint! And the whole world grew fuzzy! Thidwick was finished, completely . . .or WAS he. . ? Finished . . ? Not Thidwick! DECIDEDLY NOT! It’s true, he was in a most terrible spot, But NOW he remembered a thing he’d forgot! A wonderful something that happens each year to the horns of all moose and the horns of all deer. Today was the day, Thidwick happened to know . . . That OLD horns come off so that NEW ones can grow! And he called to the pests on his horns as he threw ’em,

THIDWICK: You wanted my horns; now you’re quite welcome to ’em! Keep ’em! They’re yours! As for ME, I shall take myself to the far distant side of the lake!

NARRATOR: And he swam Winna-Bango and found his old bunch and arrived just in time for a wonderful lunch at the south of the lake, where there’s moose-moss to munch. His old horns today are where you knew they would be. His guests are still on them, all stuffed, as they should be.
```

---

## IC-1211: The Three Co-Dependent Goats Gruff

- Title: The Three Co-Dependent Goats Gruff
- Author (byline): James Finn Garner
- Work: Politically Correct Bedtime Stories
- Publisher: John Wiley and Sons Inc
- Publication date as stated: Apr 1994
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, TROLL, YOUNGEST GOAT, MIDDLE GOAT, OLDEST GOAT
- Teaser before the introduction: No
- Spoken words (computed): 890
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Finn Garner
Book: Politically Correct Bedtime Stories
ISBN: 978-0025427303
Publisher: John Wiley and Sons Inc
Date (Month/Year): Apr 1994
```

### Introduction (context only: never use it for content warnings)

```text
Kids don't get in trouble anymore. They merely hit "social speed bumps." You're not having a bad hair day; you're suffering from "rebellious follicle syndrome." No one's tall anymore. They're "vertically enhanced." You're not shy. You're "conversationally selective." You don't talk a lot. You're just "abundantly verbal." Is it just me or has the whole concept of Political Correctness gone a little too far? Granted, our vocabulary is expanding, but seriously!

James Finn Garner uses the vehicle of widely known fairy tales to make a point regarding political correctness. I offer for your consideration: The Three Co Dependent Goats Gruff by James Finn Garner.
```

### Performance text (classify this)

```text
NARRATOR: Once on a lovely mountainside lived three goats who were related as siblings. Their name was Gruff, and they were a very close family. During the winter months they lived in a lush, green valley, eating grass and doing other things in a naturally goatish manner. When summer came they would travel up the mountainside to where the pasture was sweeter. This way they did not overgraze their valley and kept their ecological footprints as small as possible.

To get to this pasture, the goats had to cross a bridge over a wide chasm. When the first days of summer came, one goat set out to cross the bridge. This goat was the least chronologically accomplished of the siblings and thus had achieved the least superiority in size. When he reached the bridge, he lashed on his safety helmet and grasped the handrail. But as he began to cross, a menacing growl came from beneath the bridge.

Over the railing and onto the bridge leaped a troll – hairy, dirt-accomplished, and odour-enhanced.

TROLL: “Yaaarrrgh! I am the keeper of this bridge, and while goats may have the right to cross it, I’ll eat any that try!”

YOUNGEST GOAT: “But why, Mr. Troll?”

TROLL: “Because I’m a troll, and proud of it. I have a troll’s needs, and those needs include eating goats, so you better respect them or else.”

NARRATOR: The goat was frightened.

YOUNGEST GOAT: “Certainly, sir. If eating me would help you become a more complete troll, nothing would please me more. But I really can’t commit to that course of action without first consulting my siblings. Will you excuse me?”

NARRATOR: And the goat ran back to the valley.

Next, the middle sibling goat came up to the bridge. This goat was more chronologically advanced than the first goat and so enjoyed an advantage in size (although this did not make him a better or more deserving goat). He was about to cross the bridge when the troll stopped him.

TROLL: Nature has made me a troll, and I embrace my trollhood. Would you deny me my right to live the life of a troll as fully and effectively as I can?”

MIDDLE GOAT: “Me? Never!”

TROLL: Then stand still there while I come over and eat you up. And don’t try to run away; I would take that as a personal affront.”

NARRATOR: He began to invade the goat’s caprinal space.

MIDDLE GOAT: “However, I have a very close family, and it would be selfish of me to allow myself to be eaten without asking their opinion. I have respect for their feelings, too. I would hate to think that my absence would cause them any emotional stress, if I hadn’t first . . . “

TROLL: (screaming) “Go then!”

MIDDLE GOAT: I’ll rush back here as soon as we reach a consensus, for it’s not fair to keep you in suspense.”

TROLL: (sighing) “You’re too kind,”

NARRATOR: And the goat ran back to the valley. As his hunger grew, the troll began to feel a real grievance towards the goats. If he didn’t get to eat at least one of them, he was determined to go to the authorities. When the third goat came to the bridge, the troll discovered that he was nearly twice the troll’s size, with large, sharp horns and hard, heavy hooves. The troll felt his physical-intimidation prerogative fading fast. As fear turned his insides into jelly, the troll sank to his knees and pleaded,

TROLL: “Oh, please, please forgive me! I was using you and your goat siblings for my own selfish ends. I don’t know what drove me to it, but I’ve seen the error of my ways.”

NARRATOR: The goat, too, got down on what passed for knees in goats and said,

OLDEST GOAT: “Now, now, you can’t take all the blame for yourself. Our presence and supreme edibility put you in this situation. My siblings and I all feel terrible. Please, you must forgive us.”

NARRATOR: The troll began to sob.

TROLL: “No, no, it’s all my fault. I threatened and bullied you all, just for the sake of my own survival. How selfish I was!”

OLDEST GOAT: “We were the selfish ones. We only wanted to save our own skins, and we totally neglected your needs. Please, eat me now!”

TROLL: “No, you must butt me off this bridge for my insensitivity and selfishness.”

OLDEST GOAT: “I’ll do no such thing, since we all tempted you in the first place. Here, have a chomp. Go ahead.”

TROLL: “I’m telling you, I’m the guilty one here. Now, knock me off this bridge and be quick about it!”

OLDEST GOAT: “Look, no one is going to take away my blame for this, not even you, so eat me before I pop you in the nose.”

TROLL: “Don’t play guiltier-than-thou with me, Hornhead!”

OLDEST GOAT: “Hornhead?” You smelly hairball! I’ll show you guilt!”

NARRATOR: And with that, they wrestled and bit and punched and kicked as each sought to don the mantle of blame.

The other two goats bounded up to the bridge and sized up the fight. Feeling guilty at not accepting enough of the blame, they joined the others in a whirling ball of hair, hooves, horns, and teeth. But the little bridge was not built to carry such weight. It shook and swayed and finally buckled, hurling the troll and the three codependent goats Gruff into the chasm. On their way down, the each felt relieved that they would finally get what they deserved, plus as a bonus, a little extra guilt for the fate of the others.
```

---

## IC-1212: The Three Swine of Most Small Stature

- Title: The Three Swine of Most Small Stature
- Author (byline): Lewy Olfson
- Work: Skits and Short Farces for Young Actors
- Publisher: Boston Plays, Inc.
- Publication date as stated: 1973
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: STAGE MANAGER, NUMBER ONE PIG, NUMBER TWO PIG, NUMBER THREE PIG, WOLF
- Teaser before the introduction: Yes
- Spoken words (computed): 1674
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lewy Olfson
Book: Skits and Short Farces for Young Actors
ISBN: 978-0823801503
Publisher: Boston Plays, Inc.
Date (Month/Year): 1973
```

### Introduction (context only: never use it for content warnings)

```text
By Lewy Olfson
```

### Performance text (classify this)

```text
NOTE: The acting should be highly stylized, with the actors pantomiming most of the action in pseudo-Oriental fashion. STAGE MANAGER bows low to audience

STAGE MANAGER: O most revered audience, welcome to Imperial Theater of the Orient. I, Oriental Stage Manager, beg your humble attention. Wish to have your permission to introduce play. (Wish to introduce play even without your permission, since actors have been rehearsing for a whole week!) Play tells very ancient and honorable legend: legend of the Three Swine of Most Small Stature. Called in translation, “The Three Little Pigs.” Perhaps you have read legend already, in which case. feel free to nap during performance. However, must warn you that legend in English not so beautiful as legend in Chinese. In Chinese is very symbolic… very aesthetic. Also very hard to understand if you don’t speak Chinese! (Gong sounds offstage.) Ah, So! Signal means, “get this show on the road!”(Bows) The Three Swine of Most Small Stature! (He claps his.)

The three Pigs are dancing and skipping about.

STAGE MANAGER: Behold! A woodland glade in ancient China. Notice: only one tree for scenery. One tree suggests entire woodland. Very symbolic. Very aesthetic. (Claps hands. PIGS stop frolicking and stand in line.)Beg to introduce chief characters. (PIGS step forward and bow as their names are called.) Number One Pig. (He bows.) Number Two Pig. (He bows.) Number Three Pig. (He bows.) Play has one other character. We will introduce him later. For one thing, wish to build suspense. For another thing, he takes a long time to get into his costume. (The gong sounds.) Signal! Signal means: “Let play begin!”

NUMBER ONE PIG: Brother pigs, what a happy life we live here in ancient China.

NUMBER TWO PIG: You have spoken wisely, Number One Pig. Ours is a most carefree existence.

NUMBER THREE PIG: Nothing to do but sing and play, all day long.

NUMBER ONE PIG: Yes, fun is good. But when I spoke of pleasure, I meant also the pleasure of work. The pleasure of going to school. The pleasure of meeting challenges and pursuing honest toil.

NUMBER TWO PIG: What a party-pooper you are, Number One Pig! Number Three Pig and I don’t believe in all that work stuff.

NUMBER THREE PIG: Naw, we just want to dance and sing and have a good time all day long.

NUMBER ONE PIG: Foolish, foolish pigs! Listen to me, your elder brother. All play and no work make for great unhappiness!

NUMBER TWO PIG: Says who!

NUMBER ONE PIG: Old saying of Confucius. NUMBER TWO PIG (Disgusted): Ah, you and your high-flown ideas! Just because you went to college, you’re always showing off.

NUMBER THREE PIG: You used to be a regular guy, Number One Pig. But ever since you got your Ph.D. — in Pig Latin — have you been a grouch!

NUMBER ONE PIG: You may scoff at me now, my brothers. But one day you will see I am right. STAGE MANAGER (Rising, addressing audience): Number One Pig wasn’t exaggerating. He knew that summer could not last forever. Behold: Winter! (He hangs a giant snowflake cutout on the tree.) Cold, cold, cold winter — the worst winter in the history of China. Notice: Only one snowflake for scenery. very symbolic. very aesthetic.

NUMBER THREE PIG: Also very cheap.

STAGE MANAGER: Now came the time to work, just as Number One Pig had predicted.

NUMBER ONE PIG: My brothers, it is winter. We can no longer live out of doors. I think it is time to build a pagoda. NUMBER TWO PIG (Sarcastically): It’s really terrific to have a college graduate in the family. It’s been snowing for a month now, and it’s finally dawned on him to build us a house.

NUMBER THREE PIG: I was wondering when you were going to get around to it, Number One Pig. NUMBER ONE PIG (Smugly): But, my brothers, I am not going to build us a house. I am going to build me a house. You must build houses for yourselves.

NUMBER TWO PIG: Big deal. I guess we can build as good a house as you can if we want to.

NUMBER ONE PIG: We shall see. What will you build your house of, Number Three Pig?

NUMBER THREE PIG: I shall build my house of tatami mats. I know where I can get a real buy on some straw tatami mats, imported from Japan.

NUMBER ONE PIG: If I may say so, esteemed, honorable, and revered brother, it’s a stupid idea. I might call it tatami-rot!

NUMBER TWO PIG: Oink!

NUMBER ONE PIG: And what will you build your house of, Number Two Pig?

NUMBER TWO PIG: I shall build my house of chopsticks. I can get second-hand chopsticks free down at the Chinese restaurant.

NUMBER ONE PIG: House of straw! House of sticks! Is terrible architecture. NUMBER TWO PIG (Wagging his finger; brightly): But is symbolic!

NUMBER THREE PIG: (Likewise): Is aesthetic!

NUMBER ONE PIG: (Proudly): I shall build my house of bricks.

NUMBER TWO PIG: Bricks! But bricks cost a fortune!

NUMBER THREE PIG: Where would you get the money?

NUMBER ONE PIG: Have been making regular deposits at the Piggy Bank. You forget: I am college graduate. I really know how to bring home the bacon.

NUMBER TWO PIG: Oink! STAGE MANAGER (Rising): And so, the Three Swine of Most Small Stature set to work to build themselves the best pagodas they could manage. (PIGS pantomime building houses.) Number One Pig built his house of bricks, while Number Two Pig built his of chopsticks and Number Three Pig used tatami. And when the pagodas were finished, how pleased the pigs were. . . Story now becomes complicated. Is late one night. Each pig sits in his own pagoda. No scenery for night. No scenery for pagodas. Audience must use imagination. We blew budget on the snowflake. Suddenly, out of the woods comes dark, mysterious figure. (WON TON WOLFenters and slinks around at back of stage.) Wicked creature. Evil creature. Hush! Plot thickens! (WOLF pretends to knock on door of straw house by stamping his foot on the stage as he raps his hand in the air.)

WOLF: O, most revered Number Three Pig, I beg you to give me admittance to your snug little pagoda.

NUMBER THREE PIG: Who is that knocking on my door?

WOLF: It is I, your humble friend and neighbor Won Ton Wolf. Let me in, let me in!

NUMBER THREE PIG: Not by the hair of my Chinny Chin-Chin. WOLF (Perplexed): What the heck is a Chinny Chin-Chin?

NUMBER THREE PIG: Oh. Is my girlfriend. Her name is Chin-Chin. “Chinny” is her nickname. WOLF (Still perplexed): Well, what on earth does her hair have to do with it?

NUMBER THREE PIG: Her hair is her most beautiful feature. It is what caused me to fall in love with her. (Sings) “I dream of Chinny with the light brown hair. . . .” WOLF (Disgusted): What is this, Chinese amateur night? Let me in, I say!

NUMBER THREE PIG: Never!

WOLF: Then I’ll huff and I’ll puff and I’ll blow your house in!

NUMBER THREE PIG: And then what will you do? WOLF (Laughing wickedly): I’ll turn you into pork chow mein! STAGE MANAGER (As WOLF huffs and puffs): So Wolf huffed. Wolf puffed. Son of Confucius! Wolf blew house in! (NUMBER THREE PIG falls over.) Fortunately, Pig escaped to pagoda of Number Two Pig. (NUMBER THREE PIG runs over to NUMBER TWO PIG.)

NUMBER THREE PIG: Listen, brother, I’m in big trouble. May I spend the night with you?

NUMBER TWO PIG: Of course. But what happened? (WOLF knocks at door of second house.)

NUMBER THREE PIG: Never mind. I think it’s about to happen again.

WOLF: O, most noble and esteemed Number Two Pig, let me in, let me in.
NUMBER TWO PIG (To NUMBER THREE PIG): Who can that be?
NUMBER THREE PIG (Dryly): Well, it ain’t Madame Butterfly.
NUMBER TWO PIG (Dramatically): You mean — ?

NUMBER THREE PIG: (Nodding): Yep. Won Ton Wolf.
NUMBER TWO PIG (To WOLF): You’ve got to be kidding. O most feared and vicious wolf.
Never will I lot you in, not by the hair of my brother’s Chinny Chin-
Chin. (Pause) Aren’t you going to ask me what a Chinny Chin-Chin is?

WOLF: Forget it. Been there. Done that. Are you going to open up or do I go into my huff-and-puff stuff?

NUMBER TWO PIG: What will you do if I let you in?

WOLF: I’ll turn you into Barbecued Spare Ribs with Sesame Soy Sauce. STAGE MANAGER (As WOLF huffs): Again, Wolf huffed. Wolf puffed. Again, success! (NUMBER TWO PIG and NUMBER THREE PIG fall over.) Sky looked as if it was raining chopsticks. Just in nick of time, Number Two Pig and Number Three Pig made it to pagoda of Number One Pig. (They race over to NUMBER ONE PIG.)

NUMBER ONE PIG: O my most honorable brothers, to what do I owe the esteemed pleasure of this unexpected visit?

NUMBER TWO PIG: It’s Won Ton Wolf!

NUMBER THREE PIG: He’s after us! NUMBER ONE PIG (Smugly): Why did you not seek refuge in your own pagodas?

NUMBER THREE PIG: All right, don’t rub it in. That tatami of mine just shriveled to bits. It never pays to buy cheap foreign merchandise.

NUMBER TWO PIG: And my chopsticks weren’t much use, either. You were very clever, Number One Pig, to build your house of bricks. NUMBER ONE PIG (Modestly): Well, to tell the truth, I didn’t get the idea by myself. Read it in a fortune cookie.

NUMBER THREE PIG: Who cares how you got the idea! Will you let us stay with you?

NUMBER ONE PIG: Do you think I’d throw my esteemed brothers into the cold, and keep all this warmth for myself? What do you take me for — a pig?

STAGE MANAGER: So the Three Swine of Most Small Stature waited in their safe brick pagoda for the arrival of their enemy. He was not long in showing up. WOLF (Pretending to knock): O, most esteemed Number One Pig, let me in, let me in. THREE PIGS (In unison, singing): “I dream of Chinny with the light brown hair…” WOLF (Angrily): Oh, you’re pulling that on me, are you? O.K. wise guys, prepare yourselves for some huffing and puffing that’ll blow you all into won ton soup! STAGE MANAGER (As WOLF huffs): Wolf huffed. Wolf puffed. But, lo! Brick pagoda did not give way. Number One Pig had built it too strongly. Pigs were safe! Wolf was outfoxed! WOLF (To STAGE MANAGER): Oh, yeah? Well, there’s more than one way to skin a kumquat. I have a sneaky plan that will get me into that pagoda even if it is made of bricks.

STAGE MANAGER: What’s your plan? WOLF (Triumphantly): I’ll climb up on the roof and drop down the chimney! Just wait’ll I get a ladder. (WOLF exits. Gong is heard. Stage Manager turns to audience.) Stage Manager: O most revered audience, it would be a pleasure to show you outcome of devious plat of Won Ton Wolf. However, is impossible in our humble theater. Not enough money to show roof. Not enough money to show chimney. Not even enough money for symbolic, aesthetic ladder. Besides, actor playing wolf afraid of heights. However, I can tell you how story ended. Number One Pig said:

NUMBER ONE PIG: O, my brothers, after your adventure in the cold, wintry night, I’ll bet you’d like a cup of nice hot Formosa Oolong tea. I will just set a giant cauldron of water — which I just happen to have lying about the house — in the fireplace and let it come to a boil.

NUMBER TWO PIG: You really shouldn’t bother, Number One Pig.

NUMBER THREE PIG: Yes, why go to all that trouble?

NUMBER ONE PIG: Well, you never can tell. Someone may be dropping in.

STAGE MANAGER: And so, clever Number One Pig came up with stratagem that cooked wolf’s goose. But in any case, Wolf would have met sad fate, and story would have had happy ending. For as it is written in ancient, honorable Chinese proverb, “He who drops down Oriental chimney comes down with case of Hong Kong flue.” Get it? Flu? (Bows low. Blackout and quick curtain.)
```

---

## IC-1213: Time Flies

- Title: Time Flies
- Author (byline): David Ives
- Work: Time Flies and Other Short Plays
- Publisher: Grove Press Inc.
- Publication date as stated: March 2001
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: MAY, HORACE, DAVID, HORACE & MAY
- Teaser before the introduction: Yes
- Spoken words (computed): 1233
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Ives
Book: Time Flies and Other Short Plays
ISBN: 978-0802137586
Publisher: Grove Press Inc.
Date(Month/Year): March 2001
```

### Introduction (context only: never use it for content warnings)

```text
Actor: May is the most gorgeous insect on the planet and I’m . . . . I’m with her. Whoo Whoo !

Actress: I have to admit, there’s something about Horace . . . . even though we’ve just met, it seems like we’ve known each other half our lives! He may be THE ONE!

Actor: Can’t seem too eager though . . . courtship is everything . . . but I know she likes me. I can hear it in her Buzzzzzz

Actress: Enough daydreaming . . . It’s getting late . . .

Together: Time Flies by David Ives
```

### Performance text (classify this)

```text
MAY: Well here we are. This is my place.

HORACE: Already? That was fast.

MAY: Swell party, huh.

HORACE: Yeah. Quite a swarm.

MAY: Thank you for flying me home.

HORACE: No. Sure. I'm happy to. Absolutely. My pleasure. I mean-you're very, very, very welcome. Their eyes lock and they near each other as if for a kiss, their wings fluttering a little. Before their jaws can meet HORACE breaks away.

HORACE: Anyway, it was very nice meeting you-I'm sorry, is it April?

MAY: May.

HORACE: May Yes. Later than I thought, huh. They laugh politely.

MAY: That's very funny, Vergil.

HORACE: It's Horace actually.

MAY: I'm sorry. The buzz at that party was so loud.

HORACE: So you're ”May, the mayfly."

MAY: Yeah. Guess my parents didn't have much imagination. May -- mayfly.

HORACE: You don't, ah, live with your parents, do you, May?

MAY: No, my parents died around dawn this morning.

HORACE: Isn't that funny. Mine died around dawn too.

MAY: Maybe it’s fate.

MAY: Do you want a drink?

HORACE: I'd love a drink, actually. . .

MAY: Let me just turn on a couple of fireflies. (May tickles the underside of a couple of TWO-FOOT-LONG FIREFLIES hanging like a chandelier, and the fireflies light up.)

HORACE: Wow. Great pond! I love the lily pad.

MAY: Care for some music? I've got The Beatles, The Byrds, The Crickets. . .

HORACE: I love the Crickets.

MAY: Well so do I . . . (She kicks a large, insect-shaped coffee table, and we hear the buzz of crickets.)

HORACE: (as they boogie to that) So are you going out with any-I mean, are there any other mayflies in the neighborhood?

MAY: No, it's mostly wasps.

HORACE: So, you live here by your, um, all by yourself? Alone?

MAY: All by my lonesome.

HORACE: And will you look at that moon.

MAY: You know that's the first moon I've ever seen?

HORACE: That's the first moon I've ever seen. . . !

MAY: Isn't that funny.

HORACE: When were you born?

MAY: About seven-thirty this morning.

HORACE: So was I! Seven thirty-three!

MAY: Isn't that funny.

HORACE: Or maybe it's fate. They near each other again, as if for a kiss. Bzzzzzzz . .

MAY: Bzzzzzzzzz... I think that moon is having a very emotional effect on me.

HORACE: Me too.

MAY: It must be nature. Bzzzzzzzzzz...

HORACE: Bzzzzzzzzzzzzzzz... They draw their tails very close. Suddenly: A FROG:

(amplified, over loudspeaker) Ribbit, ribbit!

HORACE: &: MAY: The frogs are coming, the frogs are coming! (They "fly" around the stage in a panic. Ad lib:) The frogs are coming, the frogs are coming! (They finally stop, breathless.)

MAY: It's okay. It's okay.

HORACE: Oh my goodness.

MAY: I think he's gone now.

HORACE: Oh my goodness, that scared me.

MAY: That is the only drawback to living here. The frogs.

HORACE: You know, I like frog films and frog literature. I just don't like frogs.

MAY: Do you want to watch some tube?

HORACE: Sure. What's on?

MAY: Let's see. (She checks a TV Guide.) There is . . . "The Love Bug." "M. Butterfly." "The Spider's Stratagem." "Travels With My Ant." "Angels and Insects." "The Fly. . ."

HORACE: Eugh. Too gruesome.

MAY: "Born Yesterday." And "Life on Earth."

HORACE: What's on that?

MAY: "Swamp Life," with Sir David Attenborough.

HORACE: That sounds good. May presses a remote control and DAVID ATTENBOROUGH appears, wearing a safari jacket.

DAVID: Hello, I'm David Attenborough. Welcome to "Swamp Life." You may not believe it, but within this seemingly lifeless puddle, there thrives a teeming world of vibrant life.

HORACE: May, look-isn't that your pond?

MAY: I think that is my pond!

HORACE: He said "puddle."

DAVID: This puddle is only several inches across, but its stagnant water plays host to over fourteen gazillion different species.

MAY: It is my pond!

DAVID: Every species here is engaged in a constant, desperate battle for survival. Feeding-meeting-mating-breeding-dying. And mating. And meeting. And mating. And feeding. And dying. Mating. Mating. Meeting. Breeding. Brooding. Braiding--those that can braid. Feeding. Mating. . .

HORACE: Only one thing on his mind.

MAY: The filth on television these days.

DAVID: Tonight we start off with one of the saddest creatures of this environment.

HORACE: The dung beetle.

MAY: The toad.

DAVID: The lowly mayfly.

HORACE: Did he say "the mayfly "?

MAY: I think he said "the lowly mayfly."

DAVID: Yes. The lowly mayfly. Like these two mayflies, for instance.

HORACE: May - I think that's us!

MAY: Oh my God...

HORACE: &: MAY: We're on television!

HORACE: I don't believe it!

MAY: I can't look at this.

DAVID: As you can see, the lowly mayfly is not one of nature's most attractive creatures.

MAY: At least we don't wear safari jackets.

HORACE: I wish he'd stop saying "lowly mayfly."

MAY: Can I offer you some food? I've got some plankton in the pond. And some very nice gnat.

HORACE: I do love good gnat.

DAVID: The lowly mayfly first appeared some 350 million years ago. . . and is of the order Ephemeroptera, meaning, "living for a single day."

MAY: I did not know that!

HORACE: "Living for a single day." Huh. . .

MAY: (setting out a tray on the coffee table) There you go. There's curried gnat, salted gnat, Scottish smoked gnat. . . gnat with pesto, gnat au naturelle, and Gnat King Cole.

DAVID: Mayflies are a major food source for trout and salmon . . And then there is the giant bullfrog. FROG: (amplified, over loudspeaker) Ribbit, ribbit!

HORACE: &: MAY: The frogs are coming, the frogs are coming! They "fly" around the stage in a panic-and end up 'Flying" right into each other's arms.

HORACE: Well. there.

MAY: Hello.

MAY: (hypnotized by Horace) Funny how we flew right into each other's wings.

HORACE: It is funny.

MAY: Or fate.Bzzzz . . .

HORACE: Bzzzzz . . .

DAVID: As you see, mayflies can be quite affectionate. . . . mutually palpating their proboscises.

HORACE: You know, I've been wanting to palpate your proboscis all evening.

MAY: I think it was larva at first sight.

HORACE & MAY: (rubbing proboscises together) Zzzzzzzzzzzzzzzzzzzzzzzzzzzz

DAVID: Unfortunately for this insect, the mayfly has a life span of only one day-living just long enough to meet, mate, have offspring, and die.

MAY: Did he say "meet, mate, have offspring, and DIE"-?

DAVID: In fact, mayflies born at seven-thirty in the morning will die by the next dawn.

HORACE: &: MAY: We're going to die . . . We're going to die! Mayday, Mayday! We're going to die, we're going to die! Weeping and wailing, they kneel, beat their breasts, cross themselves, and tear their hair.

HORACE: What time is it? What time is it?

MAY: I don't wear a watch. I'm a lowly mayfly!

HORACE: (weeping) Wah-ha-ha-ha! (gasping for breath) Oh my goodness. I think I'm having an asthma attack. Can mayflies have asthma?

MAY: I don't know. Ask Mr. Safari Jacket.

HORACE: Maybe if I put a paper bag over my head. . . Do you have a paper bag?

MAY: I don't have time to look for a paper bag, I'm going to be dead very shortly, all right?

HORACE: (suddenly sober) This explains everything. We were born this morning, we hit puberty in mid-afternoon, our biological clocks went BONG, and here we are. Hot to copulate.

MAY: For the one brief miserable time we get to do it.

HORACE: Yeah.

MAY: Breeding. Dying. Breeding. Dying. So this is the whole purpose of mayflies? To make more mayflies?

HORACE: Does the world need more mayflies?

MAY: We're a major food source for trout and salmon.

HORACE: How nice for the salmon.

MAY: Oh Horace, I had such plans. I had such wonderful plans. I wanted to see Paris. I was just hoping to live till Tuesday.

HORACE: What's a Tuesday?

MAY: The sun's going to be up soon. I'm scared, Horace. I'm so scared.

HORACE: You know, May, we don't have much time, and really, we hardly know each other-but I'm going to say it. I think you're swell. I think you're divine. From your buggy eyes to the thick raspy hair on your legs to the intoxicating scent of your secretions.

MAY: Eeeuw.

HORACE: Eeeuw? No. I say woof. And I say who cares if life is a swamp and we're just a couple of small bugs in a very small pond. I say live, May! I say. . . damn it . . . live!

MAY: But how?

HORACE: Well, I don't honestly know that. . .

MAY: We could fly to Paris!

HORACE: Do we have time to fly to Paris?

MAY: Carpe diem!

HORACE: What is carpe diem?

MAY: It means "bon voyage."

HORACE: And we're outta here! They fly off to Paris as . . . BLACKOUT.
```

---

## IC-1214: Titanic

- Title: Titanic
- Author (byline): Christopher Durang
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, VICTORIA, TEDDY, RICHARD, LIDIA, CAPTAIN, SAILOR, VCTORIA
- Teaser before the introduction: Yes
- Spoken words (computed): 1925
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christopher Durang
ISBN: 978-0822211556
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
Titanic by Christopher Durang takes us into the heart of children’s anger with their parents and parents’ manipulation of their children. We find that laughter is the best surgery, slicing through prejudice and hypocrisy, cutting out dead beliefs and inflamed opinions. This dark comedy, lit by lightning bolts of truth and humor, is among the most illuminating in American drama, by “one of the most explosively funny American dramatists” – Titanic by Christopher Durang
```

### Performance text (classify this)

```text
CHARACTERS:
Victoria Tammurai – Very British, but turns hick when angry
Richard Tammurai – Foreign Accent (pick a funny one that is incongruous)
Teddy Tammurai – Their son who is a regular guy
Lidia/Harriet/Annabella – Very sultry – the Sigourney Weaver type
The Captain – A pirate voice
Higgins, the sailor – Cockney accent (like the Beatles)

VICTORIA: Richard, listen, they’re playing our song (she sings a little.) “Nearer my God to thee, Floating across the sea.” The merry-go-round was playing that tune when I first conceived Teddy. Did you know that, Teddy?

TEDDY: No.

VICTORIA: Of course you didn’t. You were too young. Yes, your father was quite a devil on the merry-go-round.

RICHARD: I still am

VICTORIA: Although you developed a bad case of vertigo the last time we rode the Wild Mouse.

RICHARD: I’ve never ridden the Wild Mouse.

VICTORIA: (a take; change subject) Teddy has very hair legs for a fourteen-year-old. Do you think that’s right, Richard?

RICHARD: Teddy hasn’t been fourteen for years.

VICTORIA: Even so. Teddy, sit up. People will think you’re fourteen years old. Why weren’t we placed at the Captain’s table. Granted the passenger list is impressive, but I think we are still among the crème de la crème. We’re certainly rich enough.

RICHARD: Perhaps the Captain looked into your family background.

VICTORIA: I would not have set one foot upon this boat if I had thought you were going to persist in these endless cruelties. Richard, I want a divorce. As soon as we dock, I am going straight to my solicitor.

RICHARD: Victoria, as far as I am concerned you can go right back to the pig farms of Indiana. Somehow I wish we had never come on the Titanic.

RICHARD: Victoria, there is no point in continuing this domestic purgatory.

VICTORIA: Not purgatory, Richard. Hell.

RICHARD: Have the decency to control your tongue in front of the boy.

TEDDY: You shouldn’t talk about tongue at the table.

RICHARD: Teddy, are you trying to give us difficulty?

VICTORIA: Don’t be harsh with Teddy, Richard, he’s confused. Have you spoken to him about that bad word beginning with “m” yet? He’s that age.

RICHARD: What bad word beginning with “m”? Menstruation?

VICTORIA: No, silly, that’s girls. Masturbation.

TEDDY: Oh, that bad word beginning with “m”. I thought you meant “mother.”

VICTORIA: Give me your leg, Teddy.

TEDDY: You shouldn’t talk about leg at the table.

VICTORIA: This pre-pubescent temper tantrum is to stop this instant. GIVE ME YOUR LEG. (She grabs his leg. Shrieking, Victoria tears off the bottom part of Teddy’s pants legs, making his long pants now short pants. This is a sudden and insane motion and is quite ferocious. Upon completion of her task, Victoria returns to a calm restrained manner.) You are obviously too young for long pants.

TEDDY: Mommy, everyone is staring at us.

RICHARD: Victoria, perhaps we should stay together for the sake of the children.

VICTORIA: Richard, Teddy is not your son.

RICHARD: Victoria, what do you mean?

VICTORIA: Richard, when you married me you looked down on my American ways. You made fun of the pig farm and my mother! One night, after you had ridiculed my boeuf de dordelaise – I went out to our beach and I wept. And on the beach I met a derelict. It was a mad moment, but he is Teddy’s father.

RICHARD: I’m only surprised that Teddy’s father was a derelict on the beach rather than one of your mother’s prize hogs. Victoria, I have something to tell you. Annabella is not your daughter. Harriet Lindsay is Annabella’s mother.

VICTORIA: Nonsense. I remember the placenta.

RICHARD: It was all a trick. Harriet and I did it with mirrors.

VICTORIA: I went through all that labor for nothing!!!??

TEDDY: Please don’t argue.

VICTORIA: Richard, I shall now make one thing clear. THERE NEVER WAS AN ANNABELLA. Harriet Lindsay and I have been having an affair, and she just invented a pregnancy to keep you from getting suspicious. You never even slept with her. We did it all with mirrors and white bread. HAH! I trust you’ll be more careful next time I say something is just marmalade.

RICHARD: (Stands) Victoria, I shall sue you for divorce. Good evening (Exits in a rage)

VICTORIA: You should have thrown your glass of water at your father, Teddy. He insulted your mother.

TEDDY: (Looks in his glass). There’s a guppy in my glass.

VICTORIA: Manners are manners. Oh, look. The Captain is looking our way. Finish your dinner, Teddy. I’m going to the cabin to rest. (She exits. Enter Lidia. Lidia comes to the table.) (SCENE)

LIDIA: I’m the Captain’s daughter Lidia. You’re cute. May I sit down?

TEDDY: Are you at the right table?

LIDIA: It is my task to make the guests feel at ease. Your fly is open. No, leave it open. Better for circulation. My father thinks I’m promiscuous for my age. What do you think?

TEDDY: I don’t know your age.

LIDIA: We were all listening to your parents. DO you think your father really slept with white bread?

TEDDY: (Shrugs) It might be a metaphor.

LIDIA: I used to keep a hedgehog up my dress. (Pause) But my parents made me stop because I kept feeding it in public. I think that’s being fussy. (Pause) I got a funny disease. They thought it was Dutch Elm disease, but it wasn’t. Am I boring you?

TEDDY: No. (Teddy gulps his water, a little afraid. Clutching his throat) Does anything happen to you if you swallow a guppy?

LIDIA: Come to my cabin, Teddy. You can’t stay a virgin forever.

TEDDY: It’s been such a trying day.

LIDIA: Relax. Take your clothes off. I’ll get the rope.

TEDDY: Rope?

LIDIA: Boy, you are a novice. (Smiles, pulls him away. Teddy begins to wail. It segues into a Foghorn sound, then into a creaking door as it opens on the Captain’s quarters).

(SCENE – CAPTAIN”S QUARTERS)

CAPTAIN: Well, here we are, Mrs. Tammurai.

VICTORIA: What a lovely cabin, Captain. Why all this pet food?

CAPTAIN: My daughter has a fondness for animals. How can we make the mood right?

VICTORIA: The usual ways. Soft music. Dim lights. Bread.

CAPTAIN: You’re an unusual woman, Mrs. Tammurai.

VICTORIA: I’ve seen too much of the world. (She sighs. Segue into Foghorn. Sailor is on deck with spy glass. Enter Richard) (SCENE – ON DECK)

RICHARD: Hello, sailor. You look familiar. No, I doubt it could be the same one.

SAILOR: Sir?

RICHARD: Well, this is going to sound silly – but do you go around in drag much?

SAILOR: I’ve never dressed as a woman in my entire life, sir.

RICHARD: Well, I guess you’re not Dicky Miller. I could never tell, of course, unless you dressed up as Queen Victoria. We’d all be sitting round the bar, and in would waltz Dicky with three tiaras on and a tiny poodle stuffed in his bosom. “I am Queen Victoria,” he’d say. We’d all play along. “Sorry, Your Majesty, no women allowed in his club,” we’d say. Dickey would say, “I am not a woman; I am the Queen.” Strange fellow, Dicky. We used to play along with him; we stopped though when one of the poodles smothered to death in Dicky’s bodice. It kind of put an edge on things.

SAILOR: Doesn’t sound like a regular guy to me.

RICHARD: Oh, he was. Give you the blouse off his back, he would.

SAILOR: Are you a member of Parliament, sir?

RICHARD: No. I’m just a poor should looking for friendship on this bitch of an earth out in the middle of this bitch of a sea.

SAILOR: I think I see an iceberg!

RICHARD: Really? Where?

SAILOR: Good God! We’re heading right for it!

RICHARD: Then we’re done for. Sailor, before we go down, I wonder if you’d do me one small favor.

SAILOR: No time for that! I’ve got to find the Captain (He exits. Foghorn segues into Teddy’s moan. Lidia’s cabin. Teddy is bound in bed. Lidia is smoking a cigarette.) (SCENE – Lidia’s Quarters)

TEDDY: I had no idea it would be so awful.

LIDIA: The first is always awful.

TEDDY: Why is it necessary that the man be tied?

LIDIA: So the woman can be safe, dopey.

TEDDY: The hamsters bit me.

LIDIA: You men are always complaining. Just be glad I got rid of the hedgehog. (Squeaking door. Enter the Captain.)

CAPTAIN: Lidia, did you see a woman pass through here?

LIDIA: No I didn’t. What are you up to?

CAPTAIN: I was entertaining in my cabin, but the woman seems to have slipped away. (Squeaking door. Enter the Sailor and Richard.)

SAILOR: Begging pardon, sir, but we’ve sighted an iceberg.

CAPTAIN: I’ ve told you not to bother me in quarters, Higgins. (calling) Mrs. Tammurai!

SAILOR: I’m afraid we’re going to sink. Why will no one listen?

RICHARD: Poor chap.

TEDDY: Daddy!

RICHARD: Teddy! What are you . . . (Sees Lidia) Oh, my Got. Is it you?

LIDIA: Certainly not. I’m the Captain’s daughter, Lidia.

RICHARD: Harriet.

LIDIA: Why did you call me Harriet?

RICHARD: You can’t fool me. What bread or no white bread, I remember harriet Lindsay.

TEDDY: Then this is the mother of my sister Annabella –

RICHARD: Shut up, Teddy. There is no Annabella. (Door creaks. Enter Victoria.)

CAPTAIN: Mrs. Tammurai!

RICHARD: Victoria!

VICTORIA: Richard. The Captain is attempting to violate my bread box.

RICHARD: You can run a whole wheat brothel as far as I’m concerned.

TEDDY: I’m all tied up.

LIDIA: Hello, Victoria.

VICTORIA: Oh, my God. Harriet. You’ve come back.

CAPTAIN: I don’t understand. Who is Harriet?

VICTORIA: She is.

CAPTAIN: But this is my daughter Lidia.

VICTORIA: Certainly I can be expected to recognize my own sister Harriet!

RICHARD: I didn’t realize Harriet was your sister!

VCTORIA: There are many things you don’t realize, Richard.

CAPTAIN: But I don’t understand. What is the meaning of this Lidia?

VICTORIA: This is not Lidia. This is my sister Harriet.

TEDDY: I’m still tied up.

VICTORIA: Teddy. That’s dirty! Big boys don’t sleep with their aunts. Harriet, Teddy is too young to be treated in a carnal manner.

CAPTAIN: I don’t understand. Who is Harriet?

LIDIA: (Triumphant.) I am Harriet Lindsay, sister of Victoria Tammurai.

CAPTAIN: My daughter Lidia was blond. You’re not blond – now that I look. Where is my daughter?

LIDIA: Your daughter Lidia is in locker #2838 in Port Authority Bus Terminal in New York and has been for three years.

RICHARD: I am appalled.

VICTORIA: Don ‘t speak of morals, Richard. I know all about your secret life. Masquerading as royalty, suffocating poodles. Oh, it’s so sordid.

TEDDY: Are you my sister Annabella?

LIDIA: What if I am?

TEDDY: Then there really is an Annabella?

LIDIA: Yes.

TEDDY: And there isn’t a Harriet?

LIDIA: I suppose not.

TEDDY: Why haven’t mommy and daddy recognized you?

LIDIA: Because they’re very bad parents.

VICTORIA: Children, children!

TEDDY: (A true realization) Yes, they are. They’re very bad. Do you think the boat will ever dock and we can get away from them?

LIDIA: The syip isn’t going to dock. It’s going to sink.

VICTORIA: Harriet –

LIDIA: Why did you call me Harriet?

VICTORIA: What?

LIDIA: I thought you had caught on by now. Teddy caught on. I AM YOUR DAUGHTER ANNABELLA.

VICTORIA: What do you mean? There is no Annabella. It was a trick you and I played on Richard.

LIDIA: I’ve tricked you, mother. You never had an affair with your sister Harriet. You had an affair with me. You don’t even have a sister. You’re an only child.

VICTORIA: I was a lonely child. (Slaps her) Don’t you ever play with words that way again. (Teddy slaps Victoria) Teddy! (Richard slaps Teddy) Thank you, Richard. (Lidia slaps Richard. Victoria slaps Lidia. Teddy slaps Victoria and Richard).

SAILOR: Captain, pleas sir! We’re going to ram the iceberg! I’m afraid we’re done for. That berg’s going to rip right through us.

CAPTAIN: Higgins. I heard you the first time. (They exit. Loud crash. Sounds of enormous ripping, water gushing, alarms, etc. Various shipwreck chaos. Then the Captain’s voice comes over the loudspeaker).

CAPTAIN: This is your Captain speaking. Do no panic. We have not hit an iceberg. What you have just heard is a sound effects record. My wife put it on. It is her idea of a little joke. There is no cause for alarm. (Sudden crash. Everyone is thrown to the ground)

CAPTAIN: (On loudspeaker) Would anyone seeing a woman carrying a sound effects record please advise the Captain of this fact as soon as possible? Thank you.

LIDIA: (Hating life) Oh, why won’t we sink, why?

RICHARD: Annabella, please.

VICTORIA: Richard, you called Harriet Annabella. Really, what could you have been thinking of?

RICHARD: Victoria, mistakes happen.

VICTORIA: Well, I suppose they do.

RICHARD: I forgive you with the derelict on the beach, if you forgive me.

VICTORIA: That’s a generous offer, Richard. (Enter the Captain).

CAPTAIN: I’ve just been through a rather harrowing experience. We’ve had to execute my wife. It’s nautical law. You’re not allowed to incite to sinking. We hanged her from the mast.

VICTORIA: Oh, Captain, how difficult for you.

CAPTAIN: Well, the others did it actually. I just blew the whistle. Mrs. Tammurai? Now that my wife is dead, I would like to propose to you.

RICHARD: Perhaps I should leave.

VICTORIA: Richard’s such a gentleman. How did your wife die?

CAPTAIN: I had her executed.

VICTORIA: Oh yes, of course.

CAPTAIN: Nautical law.

VICTORIA: Well, that happens at sea. Sad. Someday I shall face my death, and look back and see my life. And what shall I see? Deceit. Mirrors. White bread. Ah, Captain, you remember the bread. Isn’t love a strange thing? (Thinks) Sometimes, I worry. (laughs) And sometimes, I don’t (serious) Richard, we’re sinking.

RICHARD: Victoria, this is the end. (The end has gurgles and bubbles in his speech, followed by humming the Titanic theme as if sung underwater.)
```

---

## IC-1215: The Triune Tale of Diminutive Swine

- Title: The Triune Tale of Diminutive Swine
- Author (byline): John Branyan
- Work: Not specified
- Publisher: Independently Published
- Publication date as stated: July 2020
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, PIG 1, WOLF, PIG 2, PIG 1 & 2, PIG 3
- Teaser before the introduction: Yes
- Spoken words (computed): 705
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Branyan
ISBN: 979-8664574470
Publisher: Independently Published
Date (Month/Year): July 2020
```

### Introduction (context only: never use it for content warnings)

```text
What if the Three Little Pigs was retold in Shakespearean English? And what if the third pig, just to mix things up a bit, spoke good ol' American English? Wouldn't that be the best fairytale ever? The Triune Tale of Diminutive Swine by John Branyan
```

### Performance text (classify this)

```text
NARRATOR: (in formal Shakespearean English) In time past, though not long ago, there lived pigs. In stature . . . little. In number . . . three. Who being of an age both entitled and inspired to seek their fortune. Did set about to do thusly.

NARRATOR: When they had traveled a distance, pig numbered first spake. . . Saying,

PIG 1: Harken brethren, heed this tempestuous realm. Tarry we long from hearth and home we shall fare, I fear, [snort] not well.

NARRATOR: And so being collectively agreed but individually impelled,
The diminutive swine set about each to erect for himself an abode.
Pig numbered One did construct his house from straw.
Pig numbered Two did likewise.
Though, rather, not from straw, instead from sticks.
Meanwhile, unique in his imaginings, pig numbered Three did erectus his
domicile,
Stalwart and garish, a structure made from brick entirely.

Soon there happened along, as is frequently the scenario in classic tale of protagonist pig, or redhooded child . . . A wolf. Carnivorous nature in full season he called out to the straw ensconced swine. Saying,

WOLF: "Pray thee, little pig, grant me entrance."

NARRATOR: But pig One recalled with sage foreboding that,

PIG 1: He is mad who trusts in the tameness of a belly-pinched wolf.

NARRATOR: And responded immediately,

PIG 1: Nay! It shall not be! Indeed, not by whit or whiskered jowl!

NARRATOR: Prepared for this most expected response, the wolf replied immediately.

WOLF: Then steel thyself little pig. Forthwith shall I endeavor by employing means both huffing and puffing to dismantle yon flaxen fortress.

NARRATOR: Whereupon there issued forth from the wolf an exhale of gale proportions, That quickly rendered straw hovel to dregs and dross and carried aloft piglet and shattered quarters both. Exposed now to claw and fang, piglet One made haste, wolf in pursuit, To the stick festooned sanctum of peccary secondary. Causing pig Two to cry out in dismay,

PIG 2: Well! This knots my knickers! The marshaling of feral wolf to my doorstep is nowhere among those endeavors amenable or congenial.

PIG 1: (Squealing) A thousand pardons, T'would seem the beast's maim-full breath has purged me of home and sound judgment alike!

NARRATOR: The mighty maelstrom of the wolf's exhale splattered second swine's shack and shortened his sanctimonious scolding simultaneously.

PIG 2: (Squealing) Lo! And Behold!
Stand we now amid wooden wreckage tremulous and vulnerable.
With nary a strategy for eschewing the canine devourer looming in deadly
proximity."

PIG 1: (Squealing) Strategy!
While 'tis noble to contemplate tactical particularities,
Pressed as we are with the time restraint forbidding detailed strategical
conversations,
I would urge we RUN!

PIG 1 & 2: Wee wee wee wee wee wee wee!

NARRATOR: Whether by their own fleet-footed competence or the wolf's winless attitude, The diminutive swine arrived at their ultimate kindred neighbor's inexpungeable brick ingress unscathed. Upon the third pig's door with urgent hooves they pounded. Calling out,

PIG 1 & 2: Unbar this entrance and with haste we beseech thee!

NARRATOR: The third pig hailed from the American Colonies. And possessing a vocabulary substantially less robust than his impromptu visitors, replied,

PIG 3: (in “redneck” American) Say what?

PIG 1 & 2: Seek we sanctuary!

NARRATOR: they implored on the verge of hysteria.

PIG 1 & 2: Lest we fall forthwith to the ravenous appetency of yonder approaching carnivore!

NARRATOR: Still confounded by their importunate words, pig Three did render ajar his portal. Whereupon One and Two spilled through and collapsed beyond the threshold, enervated.

PIG 3: So, y'all just wanted to come in? "You could'a said that."

NARRATOR: The sinister hiss of the wolf could once again be heard outside.

WOLF: Pray thee, pigs, grant me entrance.

PIG 1 & 2: The wolf!

PIG 3: Wolf? What'd ya suppose he wants?

PIG 1: He seeks to gain purchase within.

PIG 2: Indeed he would occupy this very alcove were he but afforded the most meager of opportunities."

PIG 3: Right. I'm just gonna go ask him what he wants.

PIG 2: (Squealing) Under no circumstances!

NARRATOR: squealed Two, flinging self bodily against the portal.

PIG 2: There is naught to be gained accosting external opponent. Save our own immediate demise!

PIG 3: What did you say about my Momma?

NARRATOR: House and occupants were again engulfed in a malevolent blast of wolfish
wind.
The foundation shook, the frame rattled.
And lo, to the astonished eyes of piglet and encroaching scoundrel alike,
Stood the third pigs lodging, undaunted.
[Aside] Good news for you pig fans.
Aghast and dismayed, pig Two queried of Three.

PIG 2: How does against such relentless and torrential onslaught this domicile endure?"

NARRATOR: Pig Three, puffed out chest, tapped a hoof to the hearth and responded.

PIG 3: It's American Made.
```

---

## IC-1216: The True Story of the Three Little Pigs

- Title: The True Story of the Three Little Pigs
- Author (byline): Jon Scieszka
- Work: Not specified
- Publisher: Scholastic, Inc.
- Publication date as stated: 1989
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 728
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jon Scieszka
ISBN: 978-0140544510
Publisher: Scholastic, Inc.
Date: 1989
```

### Introduction (context only: never use it for content warnings)

```text
"Everybody knows the story of the Three Little Pigs. Or at least they think they do. But I'll let you in on a little secret. Nobody knows the real story, because nobody has ever heard my side of the story. I'm Alexander T. Wolf. You can call me Al. I don't know how this whole Big Bad Wolf thing got started, but it's all wrong. Maybe it's because of our diet. Hey, it's not my fault wolves eat cute little animals like bunnies and sheep and pigs. That's just the way we are. If cheeseburgers were cute, folks would probably think you were Big and Bad too. But like I was saying, the whole big bad wolf thing is all wrong. The real story is about a sneeze and a cup of sugar.

THIS IS THE REAL STORY. . . . The True Story of the Three Little Pigs by Jon Scieszka
```

### Performance text (classify this)

```text
Way back in Once Upon a Time time, I was making a birthday cake for my dear old granny. I had a terrible sneezing cold. I ran out of sugar. So I walked down the street to ask my neighbor for a cup of sugar. Now this neighbor was a pig. And he wasn't too bright either. He had built his whole house out of straw. Can you believe it? I mean who in his right mind would build a house of straw? So of course the minute I knocked on the door, it fell right in. I didn't want to just walk into someone else's house. So I called, "Little Pig, Little Pig, are you in?" No answer. I was just about to go home without the cup of sugar for my dear old granny's birthday cake.

That's when my nose started to itch. I felt a sneeze coming on. Well I huffed. And I snuffed. And I sneezed a great sneeze.

And you know what? The whole darn straw house fell down. And right in the middle of the pile of straw was the First Little Pig - dead as a doornail. He had been home the whole time. It seemed like a shame to leave a perfectly good ham dinner lying there in the straw. So I ate it up. Think of it as a cheeseburger just lying there. I was feeling a little better.

But I still didn't have my cup of sugar . So I went to the next neighbor's house. This neighbor was the First Little Pig's brother. He was a little smarter, but not much. He has built his house of sticks. I rang the bell on the stick house. Nobody answered. I called, "Mr. Pig, Mr. Pig, are you in?" He yelled back."Go away wolf. You can't come in. I'm shaving the hairs on my shinny chin chin."

I had just grabbed the doorknob when I felt another sneeze coming on. I huffed. And I snuffed. And I tried to cover my mouth, but I sneezed a great sneeze.

And you are not going to believe this, but the guy's house fell down just like his brother's. When the dust cleared, there was the Second Little Pig - dead as a doornail. Wolf's honor. Now you know food will spoil if you just leave it out in the open. So I did the only thing there was to do. I had dinner again. Think of it as a second helping. I was getting awfully full. But my cold was feeling a little better. And I still didn't have that cup of sugarr for my dear old granny's birthday cake. So I went to the next house. This guy was the First and Second Little Pig's brother. He must have been the brains of the family. He had built his house of bricks. I knocked on the brick house. No answer. I called, "Mr Pig, Mr. Pig, are you in?" And do you know what that rude little porker answered? "Get out of here, Wolf. Don't bother me again."

Talk about impolite! He probably had a whole sackful of sugar. And he wouldn't give me even one little cup for my dear sweet old granny's birthday cake. What a pig!

I was just about to go home and maybe make a nice birthday card instead of a cake, when I felt my cold coming on. I huffed And I snuffed. And I sneezed once again.

Then the Third Little Pig yelled, " And your old granny can sit on a pin!" Now I'm usually a pretty calm fellow. But when somebody talks about my granny like that, I go a Little crazy.

When the cops drove up, of course I was trying to break down this Pig's door. And the whole time I was huffing and puffing and sneezing and making a real scene.

The rest as they say is history.

The news reporters found out about the two pigs I had for dinner. They figured a sick guy going to borrow a cup of sugar didn't sound very exciting.

So they jazzed up the story with all of that "Huff and puff and blow your house down"

And they made me the Big Bad Wolf. That's it The real story. I was framed. "

But maybe you could loan me a cup of sugar ?
```

---

## IC-1217: The Twits

- Title: The Twits
- Author (byline): Roald Dahl adapted by David Wood
- Work: Not specified
- Publisher: Puffin Books
- Publication date as stated: February 2007
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: MRS TWIT, MR TWIT, MRS TWIT NARRATES, MRS. TWIT NARRATES, PANTOMIME SEQUENCE
- Teaser before the introduction: No
- Spoken words (computed): 1342
- Already set (do not supply): none

### Source block (context only)

```text
Author: Roald Dahl (adapted by David Wood)
ISBN: 978-0142407936
Publisher: Puffin Books
Date (Month/Year): February 2007
```

### Introduction (context only: never use it for content warnings)

```text
They're shocking! They're smelly! They're silly! They're stupefyingly stupid! Get ready to meet. . . The one and only. . . Thank goodness! The Twits! By Roald Dahl
```

### Performance text (classify this)

```text
MRS TWIT: Mr Twit. . .. . . was a very hairy-faced man. His thick, spiky hair stuck out straight like the bristles of a nailbrush. The stuff even sprouted in revolting tufts out of his nostrils and ear-holes.

MR TWIT: My hairiness makes me look terrifically wise and grand!

MRS TWIT: But in truth he was neither of these things.: Mr Twit was a twit. He was born a twit. And now, at the age of sixty, he's a bigger twit than ever! [MR TWIT looks angrily at MRS TWIT] How often, you may ask, did Mr Twit wash this bristly, nailbrushy face of his? The answer is. . .

MR TWIT: Never! [Proudly] Not even on Sundays!

MRS TWIT: As a result there were always hundreds of bits of old breakfasts. . . and lunches. . . . and suppers. . . sticking to the hairs. [MR TWIT licks eagerly round his face]

MR TWIT: [With delight] Minced chicken livers! [MR TWIT delves in his beard and finds . . .] A piece of maggoty green cheese! [He eats it noisily] A mouldy old cornflake! [MR TWIT finds it and eats it] Or even. . . [Digging it out] . . . the slimy tail of a tinned sardine. [He holds it aloft and MRS TWIT grabs it and eats it with delight]

MRS TWIT: Mmmm. Tasty. [MR TWIT scowls at her]

MR TWIT: You. . . you ugly old hag! [MRS TWIT reacts furiously, making herself look even uglier than usual]

MRS TWIT: Ugly, yes. But not born ugly.

MR TWIT: When she was young, she had quite a pretty face. [MRS TWIT smiles 'prettily'] But she had ugly thoughts every day. . . of every week. . . of every year. And so her face got uglier. . . and uglier. . . and uglier. . . [MRS TWIT demonstrates] SO ugly I can hardly bear to look at it! [MRS TWIT scowls at MR TWIT. Then she hits him with her walking stick] Ow! [He holds his arm up threateningly]

MRS TWIT NARRATES: Mr and Mrs Twit were a very happy couple. But seldom happy at the same time! For what really made them happy was . . . playing nasty tricks on one another!

[MR TWIT tiptoes to MRS TWIT, putting his finger to his lips as if to tell the audience not to say anything. Unseen by MRS TWIT, he snaps off half of her walking stick.

MR TWIT: [Warmly] A glass of beer, my dear?

MRS TWIT: Mmmm. Lovely. [She goes to walk, using her stick, but it is so short she crashes to the floor] [MR TWIT laughs] Aaaah! [She struggles up, forced to stoop because qf the short walking stick] What's happened? [MR TWIT quickly removes his shoes, kneels down into them and shuffles towards her]

MR TWIT: You seem to be growing, my sweet.

MRS TWIT: Growing?

MR TWIT: [Arriving and looking shorter than her] Growing. Take a look at your stick, you old goat, and see how much you've grown in comparison.

MRS TWIT: [Looking at her stick in amazement] Never!

MR TWIT: You always said you wanted me to look up to you! Your wish has been granted.

MRS TWIT: I don't want to grow!

MR TWIT: No?

MRS TWIT: No! Do something!

MR TWIT: Do something? Anything?

MRS TWIT: Anything! Stop me growing!

MR TWIT: Of course, my pet. [MR TWIT stands up, unseen by MRS TWIT, and fetches an enormous joke mallet, which he brings crashing down on her head]

MRS TWIT: Aaah! [MR TWIT laughs and, seen by MRS TWIT, takes the bottom half of her walking stick from off stage and replaces it]

MR TWIT: Just a litle joke, my honey-bunny! [MRS TWIT growls in fury.]

MRS. TWIT NARRATES: Mrs Twit was determined to pay back Mr Twit.

PANTOMIME SEQUENCE:

[MRS TWIT smiles] [MRS TWIT checks that MR TWIT is not looking] [MRS TWIT pretends to remove her eye, revealing the glass eye (marble) and closing her real eye] MR TWIT looks round with a hint if suspicion. MRS TWIT smiles innocently. MR TWIT drinks from his glass. MRS TWIT pretends to drink from hers. Then she pretends to notice something behind MR TWIT. He turns to follow her gaze. Quickly MRS TWIT swaps the two glasses round. MR TWIT turns back, suspicious. MRS TWIT drinks from his glass, he drinks from hers]

MR TWIT: What are you plotting?

MRS TWIT: Me plotting? You're the rotter what plots. But I'm watching you. Oh, yes! I'm watching you like a wombat!

MR TWIT: [Sprqying her with beer as he talks] Oh, do shut up, you old hag. [He drains the glass and suddenly sees the glass eye at the bottom. MR TWIT jumps with shock] Aaaaah! [MRS TWIT cackles with laughter]

MRS TWIT: I told you I was watching you! I've got eyes everywhere, so you'd better be careful! [She retrieves the glass eye .from the glass and holds it towards MR TWIT meaningfully, then replaces it in her eye-socket]

MRS TWIT NARRATES: Today Mr Twit has been trying, with not much success, to train monkeys for the circus he hopes to run. Now it's time for bed.

MRS TWIT: Them blooming monkeys are a waste of space.

MR TWIT: Shut up, fungus face.

MRS TWIT: A load of woolly wallies, that's all they are.

MR TWIT: That's all you know, camel-breath.

MRS TWIT: All I know is, you'll never train them chattering charlies.

MR TWIT: Yes, I will!

MRS TWIT: No, you won't!

MR TWIT: I will!

MRS TWIT: You won't!

MR TWIT: Will!

MRS TWIT: Won't!

MR TWIT: Will!

MRS TWIT: Won't!

MR TWIT: Won't!

MRS TWIT: Will!

MR TWIT: Hah! Gotcha! [He gets out bed]

MRS TWIT: Where are you off to?

MR TWIT: I want a drink.

MRS TWIT: You want a brain.

[She laughs heartily, then dozes off; snoring gently] [MR TWIT starts to drink]

MR TWIT: [Mr Twit was reminded of the time when had suddenly seen the eye staring at him.] . . . Aaaah! [Deciding to pay Mrs. Twit back, MR TWIT reaches into his beard and brings out a large, slimy frog]. Come on, fat froggy, do your slimy, grimy worst! [Smiling in anticipation, he tiptoes over to the bed and slips the frog under the sheet near MRS TWIT's feet] [Pause]

MRS TWIT: [Suddenly] Aaaaaah! [She bounces about]

MR TWIT: What's the matter, light of my life?

MRS TWIT: Help! There's something in the bed!

MR TWIT: I'll bet it's that Giant Skillywiggler!

MRS TWIT: What Skigglewilly? Ah! It's all slimy!

MR TWIT: The Giant Skillywiggler that jumped out of my suitcase when I got home from Africa.

MRS TWIT: Never!

MR TWIT: Yes. I tried to kill it, but it got away. It disappeared under a pile of your knickers!

MRS TWIT: Help! Save me! It's crawling on my feet!

MR TWIT: It's got teeth like screwdrivers.

MRS TWIT: Aaaah!

MR TWIT: It'll bite off your toes!

MRS TWIT: Aaaah!

MR TWIT: And nibble your knees! [The frog jumps up on to MRS TWIT'S face] My nose! My nose! [MR TWIT grabs the frog and holds it up]

MR TWIT: By golly, it is a Giant Skillywiggler!

MRS TWIT: Aaaah! You scrabby old scumbag! You sneaky old snake! You scheming old scallop! You wait! You wait!

MRS TWIT NARRATES: Mrs Twit, as you might expect, did not forget about her husband's Giant Skillywiggler joke. Next day, at lunchtime, she decided to pay him back.

MRS TWIT: [MRS TWIT, goes to the stove. She sings innocently as she picks up the saucepan] La, la, la, la, la, la, laaaa! [Calling] My dearest! Why don't I make us each a nice, mouth watering bowl of spaghetti? Eh?

MR TWIT: Mmm. Yes. Why not, my little dumpling? Good idea. Spaghetti. I like spaghetti. [MRS TWIT puts spaghetti in the saucepan] [Then, unseen by MR TWIT, MRS TWIT takes some squiggly, squirming worms from her pocket and drops them into MR TWIT'S bowl. She brings the bowls to the table]

MRS TWIT: [Sweetly] Your spaghetti, my dreamboat, my dove!

MR TWIT: Mmm. Scrummy. [He picks up his fork and goes to take some spaghetti] Hey, my spaghetti is moving.

MRS TWIT: What's that, my angel-puss?

MR TWIT: It's all squirmy.

MRS TWIT: It's a new kind. It's called Squiggly Spaghetti. It's delicious. Eat it up while it's nice and hot. [MR TWIT starts to tuck in, forking up the spaghetti and shoveling it into his mouth, slurping and leaving a mess on his beard. MRS TWIT watches eagerly]

MR TWIT: [Chewing hard] It's not as good as the ordinary kind. It's too squishy.

MRS TWIT: Oh? I find it very tasty.

MR TWIT: [Swallowing a mouthful] I find it rather bitter. It's got a distinctly bitter flavour. Buy the other kind next time. [But he goes on eating, with the occasional burp] [MRS TWIT can hardly contain her delight. As he finishes his plateful. . .]

MRS TWIT: You want to know why your spaghetti was squirmy and squishy?

MR TWIT: Why?

MRS TWIT: And why it had a nasty bitter taste?

MR TWIT: Why?

MRS TWIT: Because it was worms! [She roars with laughter] Because it was WORMS!
```

---

## IC-1218: UFO Menance

- Title: UFO Menance
- Author (byline): Woody Allen
- Work: Side Effects
- Publisher: Ballantine Books
- Publication date as stated: Nov 1989
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2062
- Already set (do not supply): none

### Source block (context only)

```text
Author: Woody Allen
Book: Side Effects
ISBN: 0345343352
Publisher: Ballantine Books
Date(Month/Year): Nov 1989
```

### Introduction (context only: never use it for content warnings)

```text
The Men In Black - or MIB's as they are sometimes called are a group that supposedly show up to harass or intimidate witnesses of UFO sightings and related phenomena the government does not want the public to know about. They usually make vague or sometimes specific threats to stop witnesses from talking or sharing information. They confiscate any physical proof of UFO related sightings -- such as photos, artifacts, or audio / video recordings. Needless to say, they have perpetuated the controversy surrounding crop circles, alien abductions, Stonehenge and Area 51. I’m (we’re) here today to get to the TRUTH behind the UFO Menance by Woody Allen.
```

### Performance text (classify this)

```text
UFOs are back in the news, and it is high time we took a serious look at this phenomenon. (Actually, the time is ten past eight, so not only are we a few minutes late but I'm hungry.) Up until now, the entire subject of flying saucers has been mostly associated with kooks or oddballs. Frequently, in fact, observers will admit to being a member of both groups. Still, persistent sightings by responsible indi-viduals have caused the Air Force and the scientific community to reexamine a once skeptical attitude, and the sum of two hundred dollars has now been allocated for a comprehensive study of the phenomenon. The question is: Is anything out there? And if so, do they have ray guns?

All UFOs may not prove to be of extraterrestrial origin, but experts do agree that any glowing cigar-shaped aircraft capable of rising straight up at twelve thousand miles per second would require the kind of maintenance and sparkplugs available only on Pluto. If these objects are indeed from another planet, then the civilization that designed them must be millions of years more advanced than our own. Either that or they are very lucky. Professor Leon Speciman postulates a civilization in outer space that is more advanced than ours by approximately fifteen minutes. This, he feels, gives them a great advantage over us, since they needn't rush to get to appointments.

Dr. Brackish Menzies, who works at the Mount Wilson Observatory, or else is under observation at the Mount Wilson Mental Hospital (the letter is not clear), claims that travelers moving at close to the speed of light would require many millions of years to get here, even from the nearest solar system, and, judging from the shows on Broadway, the trip would hardly be worth it. (It is impossible to travel faster than light, and certainly not desirable, as one's hat keeps blowing off.)

Interestingly, according to modern astronomers, space is finite. This is a very comforting thought-particularly for people who can never remember where they have left things. The key factor in thinking about the universe, however, is that it is expanding and will one day break apart and disappear. That is why if the girl in the office down the hall has some good points but perhaps not all the qualities you require it's best to compromise.

The most frequently asked question about the UFOs is: If saucers come from outer space, why have their pilots not attempted to make contact with us, instead of hovering mysteriously over deserted areas? My own theory is that for creatures from another solar system "hovering" may be a socially acceptable mode of relating. It may, indeed, be pleasurable. I myself once hovered over an eighteen-year-old actress for six months and had the best time of my life. It should also be recalled that when we talk of "life" on other planets we are frequently referring to amino acids, which are never very gregarious, even at parties.

Most people tend to think of UFOs as a modern problem, but could they be a phenomenon that man has been aware of for centuries? (To us a century seems quite long, particularly if you are holding an IOU, but by astronomical standards it is over in a second. For that reason, it is always best to carry a toothbrush and be ready to leave on a moment's notice.) Scholars now tell us that the sighting of unidentified flying objects dates as far back as Biblical times. For instance, there is a passage in the Book of Leviticus that reads, "And a great and silver ball appeared over the Assyrian Armies, and in all of Babylonia there was wailing and gnashing of teeth, till the Prophets bade the multitudes get a grip on themselves and shape up."

Was this phenomenon related to one described years later by Parmenides: "Three orange objects did appear suddenly in the heavens and did circle midtown Athens, hovering over the baths and causing several of our wisest philosophers to grab for towels"? And, again, were those "orange objects" similar to what is described in a recently discovered twelfth century Saxon-church manuscript: ''A lauch lauched he; wer richt laith to weet a cork-heild schonne; whilst a red balle lang owre swam aboone. I thank you, ladies and gentlemen"?

This last account was taken by medieval clergy to signify that the world was coming to an end, and there was great disappointment when Monday came and everyone had to go back to work.

Finally, and most convincingly, in 1822 Goethe himself notes a strange celestial phenomenon. "En route home from the Leipzig Anxiety Festival," he wrote, "I was crossing a meadow, when I chanced to look up and saw several fiery red balls suddenly appear in the southern sky. They descended at a great rate of speed and began chasing me. I screamed that I was a genius and consequently could not run very fast, but my words were wasted. I became enraged and shoured imprecations at them, whereupon they flew away frightened. I related this story to Beethoven, not realizing he had already gone deaf, and he smiled and nodded and said, 'Right.'

As a general rule, careful on-the-scene investigations disclose that most "unidentified" flying objects are quite ordinary phenomena, such as weather balloons, meteorites, satellites, and even once a man named Lewis Mandelbaum, who blew off the roof of the World Trade Center. A typical "explained" incident is the one reported by Sir Chester Ramsbottom, on June 5, 1961, in Shropshire: "I was driving along the road at 2:00 A.M. and saw a cigar-shaped object that seemed to be tracking my car. No matter which way I drove, it stayed with me, turning sharply at right angles. It was a fierce, glowing red, and in spite of twisting and turning the car at high speed I could not lose it. I became alarmed and began sweating. I let out a shriek of terror and apparently fainted, but awoke in a hospital, miraculously unharmed." Upon investigation, experts determined that the "cigar-shaped object" was Sir Chester's nose. Naturally, all his evasive actions could not lose it, since it was attached to his face.

Another explained incident began in late April of 1972, with a report from Major General Curtis Memling, of Andrews Air Force Base: "I was walking across a field one night and suddenly I saw a large silver disc in the sky. It flew over me, not fifty feet above my head, and repeatedly described aerodynamic patterns impossible for any normal aircraft. Suddenly it accelerated and shot away at terrific speed."

Investigators became suspicious when they noticed that General Memling could not describe this incident without giggling. He later admitted he had just come from a showing of the film War of the Worlds, at the post movie theatre, and "got a very big kick out of it." Ironically, General Memling reported another UFO sighting in 1976, but it was soon discovered that he, too, had become fixated on Sir Chester Ramsbottom's nose-an occurrence that caused consternation in the Air Force and eventually led to General Memling's court-martial.

If most UFO sightings can be satisfactorily explained, what of those few which cannot? Following are some of the most mystifying examples of "unsolved" encounters, the first reported by a Boston man in May, 1969: "I was walking by the beach with my wife. She's not a very attractive woman. Rather overweight. In fact, I was pulling her on a dolly at the time. Suddenly I looked up and saw a huge white saucer that seemed to be descending at great speed. I guess I panicked, because I dropped the rope on my wife's dolly and began running. The saucer passed directly over my head and I heard an eerie, metallic voice say, 'Call your service.' When I got home, I phoned my answering service and received a message that my brother Ralph had moved and to forward all his mail to Neptune. I never saw him again. My wife suffered a severe breakdown over the incident and now cannot converse without using a hand puppet."

From I. M. Axelbank, of Athens, Georgia, February, 1971: "I am an experienced pilot and was flying my private Cessna from New Mexico to Amarillo, Texas, to bomb some people whose religious persuasion I do not wholly agree with, when I noticed an object flying alongside me. At first I thought it was another plane, until it emitted a green beam of light, forcing my plane to drop eleven thousand feet in four seconds and causing my toupee to snap off my head and tear a two-foot hole in the roof. I repeatedly called for help on my radio, but for some reason could only get the old Mr. Anthony program. The UFO came very close to my plane again and then shot away at blinding speed. By this time I had lost my bearings and was forced to make an emergency landing on the turnpike. I continued the trip in the plane on the ground and only got into trouble when I tried to run a toll booth and broke off my wings."

One of the eeriest accounts occurred in August, 1975, to a man on Montauk Point, in Long Island: "I was in bed at my beach house, but could not sleep because of some fried chicken in the icebox that I felt entitled to. I waited till my wife dropped off, and tiptoed into the kitchen. I remember looking at the clock. It was precisely four-fifteen. I'm quite certain of this, because our kitchen clock has not worked in twenty-one years and is always at that time. I also noticed that our dog, Judas, was acting funny. He was standing up on his hind legs and singing 'I Enjoy Being a Girl.' Suddenly the room turned bright orange. At first, I thought my wife had caught me eating between meals and set fire to the house. Then I looked out the window, where to my amazement I saw a gigantic cigar-shaped aircraft hovering just over the treetops in the yard and emitting an orange glow. I stood transfixed for what must have been several hours, though our clock still read four-fifteen, so it was difficult to tell. Finally, a large, mechanical claw extended from the aircraft and snatched the two pieces of chicken from my hand and quickly retreated. The machine then rose and, accelerating at great speed, vanished into the sky. When I reported the incident to the Air Force, they told me that what I had seen was a flock of birds. When I protested, Colonel Quincy Bascomb personally promised that the Air Force would return the two pieces of chicken. To this day, I have only received one piece."

Finally, an account in January, 1977, by two Louisiana factory workers: "Roy and I was catfishing in the bog. I enjoy the bog, as does Roy. We was not drinking, although we had brought with us a gallon of methyl chloride, which we both favor with either a twist of lemon or a small onion. Anyways, at about midnight we looked up and saw a bright yellow sphere descend into the bog. At first Roy mistook it for a whooping crane and took a shot at it, but I said, 'Roy, that ain't no crane, 'cause it's got no beak.' That's how you can tell a crane. Roy's son Gus has a beak, you know, and thinks he's a crane. Anyways, all of a sudden this door slides open and several creatures emerge. These creatures looked like little portable radios with teeth and short hair. They also had legs, although where the toes usually are they had wheels. The creatures motioned to me to come forward, which I did, and they injected me with a fluid that caused me to smile and act like Bo Peep. They spoke with one another in a strange tongue, which sounded like when you back your car over a fat person. They took me aboard the aircraft and gave me what seemed to be a complete physical examination. I went along with it, as I had not had a checkup in two years. By now they had mastered my own language, but they still made simple mistakes like using 'hermeneutics,' when they meant 'heuristic.' They told me they were from another galaxy and were here to tell the earth that we must learn to live in peace or they will return with special weapons and laminate every first-born male. They said they would get the results of my blood test back in a couple of days and if I didn't hear from them I could go ahead and marry Clair."
```

---

## IC-1219: The Universal Language

- Title: The Universal Language
- Author (byline): David Ives
- Work: All in the Timing: 14 Plays
- Publisher: Vintage Books
- Publication date as stated: Jan 1995
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: DAWN, DON, DON & DAWN
- Teaser before the introduction: Yes
- Spoken words (computed): 1878
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Ives
Book: All in the Timing: 14 Plays
ISBN: 978-0679759287
Publisher: Vintage Books
Date (Month/Year): Jan 1995
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: There are over 5000 languages on earth

ACTRESS: 5000 different ways to say "hello, goodbye, I love you."

ACTOR: If you listen to a two year old develop language, they say the noun and the verb and always in the present tense. A child experiences life in the now. That's all they need to convey the message. We like to flower it up with adjectives and talk about the future and the past but the gist remains the same.

ACTRESS: So now if we boil down the spoken word to simple concepts like a child does, then creating a new universal language that has a small amount of words may be the answer. English may be the starting point for this language but I believe there is one more answer to this question.

ACTOR: We should all learn Unamunda . . .

TOGETHER: The Universal Language by David Ives.
```

### Performance text (classify this)

```text
DAWN: H-h-h-h-hello...? [She steps in quietly.] Hello? Is anyb-b-b-ody here? {No response. She sees the blackboard, reads.] "He. She. It. Arf." [She notices the numbers around the walls, and reads.] "Wen - yu - fre - fal- fynd - iff - heven - waitz." (Noticing the empty chairs, she practices her greeting, as if there were people sitting in them.] Hello, my name is Dawn. It's very nice to meet you. How do you do, my name is Dawn. A pleasure to meet you. Hello. My name is Dawn. [The door at left opens and DON appears.]

DON: Velcro! ["Welcome!"] ,

DAWN: Excuse me?

DON: Velcro! Belljar, Froyling! Harvardyu? ["Welcome. Good day, Miss. How are you?"]

DAWN: H-h-h-how do you d-d-d-do, my n-n-name is [Breaks off) I'm sorry. [She turns to go.)

DON: Oop, oop, oop! Varta, Froyling! Varta! Varta! ["No, no, no! Wait, Miss! Wait!"]

DAWN: I'm v-very sorry to b-b-bother you.

DON: Mock - klahtoo boddam nikto! Ventrica! Ventrica, ventrica Police! ["But - you're not bothering me at all! Enter. Please."]

DAWN: Really - I think I have the wrong place.

DON: Da rrrroongplatz? Oop da-doll! Du doppa da rektplatz! Dameetcha playzeer. Comintern. Police. Plop da chah. ["The wrong place? Not at all! You have the right place. Pleased to meet you. Come in. Please. Have a seat."]

DAWN: Well. J-just for a second.

DON: [Cleaning up papers on the floor.] Squeegie la mezza. ["Excuse the mess"] [He points to the chair.) Zitz?

DAWN: No thank you. [She sits)

DON: Argo. ["So."] Belljar, Froyling. Harvardyu?

DAWN: "Belljar?"

DON: Belljar. Bell. Jar. Belljar!

DAWN: Is that "good day"-?

DON: Ding! ["Yes."] "Bell jar" arf"good day." Epp ["And - "] Harvardyu?

DAWN: Harvard University?

DON: Oop! ["No."] Harvardyu?

DAWN: Howard Hughes?

DON: Oop! Harvardyu?

DAWN: Oh! "How are you."

DON: Bleeny, bleeny! Bonanza bleeny! ["Good, good, very good."]

DAWN: Is this The School of Unamunda?

DON: Hets arf dada Unamunda Kaka-daymee. ["This is the School of Unamunda."] Epp vot kennedy doopferyu? ["And what can I do for you?"]

DAWN: Do you speak English?

DON: "English"...?

DAWN: English.

DON: Ah! Johndeese!

DAWN: Yes. Johndeese.

DON: Johndeese. Squeegie, squeegie. Alaska, iago parladoop johndeese. ["Sorry. Unfortunately, I don't speak English."]

DAWN: No johndeese at all?

DON: One, two, three worlds. "Khello. Goombye. Rice Krispies. Chevrolet." Et cinema, et cinema. Mock - votsdy beesnest, bella Froyling? ["But - what brings you here?"]

DAWN: Well I wanted to be the first. Or among the first. To learn this universal language.

DON: Du arf entra di feersta di feersten. Corngranulations. Ya kooch di anda. [He kisses her hand.] Epp! Voila-dimir da zamplification forum. [produces an application form.]

DAWN: Well I'm not sure I'm ready to apply just yet...

DON: Dy klink, pink dama? ["Your name?"]

DAWN: "Dy klink..."?

DON: Votsdy klink? Vee klinks du?

DAWN: Urn. No nabisco. [As if to say, I don't understand.]

DON: No nabisco. Klinks duMary, klinks duJane, orf Betsy, orf Barbara, orf Tina...? Tessie? Fred?

DAWN: Oh. My name!

DON: Attackly! Mi klink. Echo mi. "Mi klink..."

DAWN: Mi klink.

DON: "Arf." Parla.

DAWN: Mi klink arfDawn di-di-di-Vito.

DON: Dawn di-di-di-Vito! Vot'n harmonika klink doppa du! ["What a melodious name you have!"]

DAWN: Actually, just one d-d- "d."

DON: Ah. Dawn di Vito. Squeegie.

DAWN: I have a s-s-slight s-s

DON: Stutter.

DAWN: Yes.

DON: Tonguestoppard. Problaymen mit da hoover.

DAWN: Da hoover?

DON: ["Mouth."] Da hoover. ["Face, nose, lips."] Da veasle, da nozzle, da volvos, da hoover. Et cinema, et cinema. Mock! Hets arf blizzardo. Hets arf molto blizzardo! ["This is very strange,"]

DAWN: Something's wrong?

DON: Dusa klinks "Dawn." !ago klink "Don." Badabba? ["Understand?"]

DAWN: Urn. No.

DON: Dawn-Don. Don-Dawn.

DAWN: I'm Dawn and you're Don.

DON: Ding. Arf blizzardo, oop?

DAWN: Arfblizzardo, yes.

DON: Neekolas importantay. [Back to the application form.) Argo. Da bin formations. Edge?

DAWN: Twenty-eight.

DON: "Vont-wait." Slacks?

DAWN: Female.

DON: "Vittamin."

DAWN: How do you say "male"?

DON: "Aspirin." Oxipation?

DAWN: I'm a word processor.

DON: "Verboblender..."

DAWN: Is Unamunda very hard to learn?

DON: Eedgy. Egsovereedgy. [He takes a book off a chair.] Da bop.

DAWN: Da bop?

DON: Da bop.

DAWN: Oh. Book.

DON: Da bop. ["The room"] Da rhoomba. ["The walls"] Da valtz. ["The door"] Isadora. ["The chair"] Da chah. ["Two chairs"] Da chah-chah.

DON & DAWN: ["Three chairs"] Da chah-chah-chah!

DON: Braga! Sonia braga! lago trattoria Shakespeare enda Unamunda.

DAWN: You're translating Shakespeare ito Unamunda?

DON: Forsoot! - Nintendo. ["Listen."] "Ah Romeo, Romeo, bilko arfst du Romeo?" [pointing to a rose on the desk.] "Na rosa pollyanna klink voop sent so pink!" Balloontiful, eh?

DAWN: Yes. Bonzo.

DON: Bonanza.

DAWN: Bonanza.

DON: "Mock visp! Vot loomen trip yondra fenstra sheint? Arf den oyster! Epp Juliet arf sonnnng!" Video, Froyling, Unamunda arf da linkwa supreemka di amamor!

DAWN: You know it's strange how much I understand. SO "linkwa" is "language"?

DON: Perzacto. Wen linkwa. [He holds up one finger.] Yew - [Two fingers.]

DAWN: Two

DON: Linkages. Free - [Three fingers.]

DAWN: Three

DON: Linguini.

DAWN: I see. And "is" is - ?

DON: Arf.

DAWN: "Was" is - ?

DON: Wharf.

DAWN: "Had been" - ?

DON: Long wharf.

DAWN: And "will be" - ?

DON: Barf. Arf, wharf, barf. Pasta, prison, furniture dances. ["Past, present, future tenses."]

DAWN: Well, Mr.

DON: Finninneganegan. [- like "Finnegan," slurred. "Finninn-againagain. ]

DAWN: What kind of name is that?

DON: Fininnish.

DAWN: Mr. F-F-F-F

DON: Police! Klink mi "Don."

DAWN: I'd love to learn Unamunda. I mean, if it isn't too expensive.

DON: {perfect English.] Five hundred dollars.

DAWN: Five hundred dollars?

DON: Cash.

DAWN: Five hundred dollars is a lot of money.

DON: Kalamari, Froyling! Kalamari! Da payola arf oopsissima importantay! ["Be calm, be calm! The money isn't important!"]

DAWN: I don't have much money.

DON: Oop doppa bonanza geld. Ya badabba. ["You don't have much money. I understand."]

DAWN: And the thing is, I do have this s-s-slight s-s-s

DON: Stutter. Ya badabba. Joe diMaggio. Mock no seperanto, Froyling! ["That's too bad. But don't despair!"] Porky mit Unamunda - oop tonguestoppard.

DAWN: I wouldn't stutter?

DON: Oop.

DAWN: At all?

DON: Absaloopdiloop.

DAWN: The thing is, just because I'm quiet doesn't mean I have nothing to say. I believe that language is the opposite of loneliness. And if everybody in the world spoke the same language, who would ever be lonely? I just think English isn't my language. Since it only m-makes p people laugh at me. And makes me...

DON: Lornly.

DAWN: Ding. Very lornly. So will you teach me Unamunda? I do have a little money saved up.

DON: Donutsayev deedeena vanya. ["Don't say I didn't warn you."] Dollripe-chus. Boggle da zitzbells. Arf raddly? ["All right. Buckle your seatbelts. Are you ready?"]

DAWN: Yes. I'm raddly.

DON: Raza la tabooli. Kontsentreeren. Lax da hoover, lax da hoover. Epp echo mi. ["Clear your mind. Concentrate. Relax your mouth, relax your mouth. And repeat after me."] (picks up a pointer.) Schtick.

DAWN: Schtick. /DON puts the pointer down, and begins the pronouns.)

DON: {pointing to himself] Ya.

DAWN: Ya.

DON: (points to her.) Du.

DAWN: Du.

DON: (points to "he" on the blackboard.) En.

DAWN: En.

DON: [points to "SHE" on the blackboard.] Dee.

DAWN: Dee.

DON: [points to "IT".] Da.

DAWN: Da.

DON: ["WE."] Wop.

DAWN: Wop.

DON: ["YOU."] Doobly.

DAWN: Doobly.

DON: ["THEY"] Day.

DAWN: Day.

DON: Du badabba?

DAWN: Ya badabba duo

DON: Testicle. ["Test. "]

DAWN: Al dente? ["Already?"]

DON: Shmal testicle. Epp - alIa togandhi. ["Small test. And - all together."]

DAWN: [As he points to "I, YOU, WE, HE, YOU, THEY'} Ya du wop en doobly day.

DON & DAWN: [DON points to her, then "IT. ') Doo da! Doo da!

DAWN: [Sings "Camptown ladies sing this song.'} Ya du wop en doobly day

DON & DAWN: [Sing together} Arf da doo-dah day!

DON: Bleeny, bleeny bonanza bleeny!

DAWN: Reedly-dee?

DON: Indeedly-dee. [Dawn raises her hand.] Quisling?

DAWN: How do you say "how-do-you-say"?

DON: Howardjohnson.

DAWN: Howardjohnson "to have"?

DON: Doppa.

DAWN: SO - {Indicating "he, you, she') En doppa, du doppa, dee doppa.

DON: Ding!

DAWN: [Faster.] En doppa, du doppa, dee doppa.

DON: Ding!

DAWN: [Faster still, swinging it.] En doppa, du doppa, dee doppa. ["They"] Day.

DON: Bleeny con cavyar! Scoop da gwan?

DAWN: Ya scoop if du do.

DON: Dopple scoop! [points left.] Eedon.

DAWN: Eedon.

DON: [pointing right.] Ged.

DAWN: Ged.

DON: [pointing up.] Enro.

DAWN: Enro.

DON: [pointing down.] Rok.

DAWN: Rok.

DON: [Right.] Ged.

DAWN: Ged.

DON: [Up.] Enro.

DAWN: Enro.

DON: [Left.] EeDon.

DAWN: EeDon.

DON: [Down.] Rok.

DAWN: Rok.

DON: Argo...

DON & DAWN: Ged eedon rok enro, ged eedon rok enro! ["Get it on, rock and roll, get it on, rock and roll!]

DAWN: This is fun!

DON: Dinksdu diss is flan? ["You think this is fun?"]

DAWN: Flantastico!

DON: Ives-ing onda kick. [Holds out hand.] Di anda.

DAWN: Di anda.

DON: [palm.] Da palma.

DAWN: Da palma.

DON: [Index finger.] Da vinci.

DAWN: Da vinci.

DON: [Middle finger.] Di niro.

DAWN: Di niro.

DON: [Thumb.] Da bamba.

DAWN: Da bamba

DON: [Leg.] Da jamba.

DAWN: Da jamba.

DON & DAWN: [Doing a two-step.] Da jambo-ree!

DON: Zoopa! Zoopa mit noodel!

DAWN: Minestrone, minestrone! ["Wait a second!"] Howardjohnson "little"?

DON: Diddly.

DAWN: Howardjohnson "big"?

DON: Da-wow.

DAWN: Argo...

DON: Doppa du a diddly anda? ["Do you have a small hand?"]

DAWN: Yago doppa diddly anda, dusa doopa doppa diddlyanda. ["I have a small hand, you don't have a small hand."]

DON: Scoopa du da diddly bop? ["Do you want a little book?"]

DAWN: Oop scoopa diddly bop, iago scoopa bop da-wow! ["I don't want a little book, I want a big book."]

DON & DAWN: Oop scoopa diddly bop, iago scoopa bop da-wow, da-wow, da-wow!

DON: A-plotz, Froyling. A-plotz! ["A-plus."] Wharf das gold for yu? ["Was that good for you?"]

DAWN: Gold formeeka? Das wharf gland! Wharf das gold for yu?

DON: Das wharf da skool da fortnox!

DAWN: GOOMBYE ENGLISH, BELLJAR UNAMUNDA! Oh, sor denly ya sensa socha frill da joy! ["Suddenly I feel such a thrill of joy!"]

DON: Dawn...

DAWN: My slaveyard! [She rushes to embrace him, but he slips aside.]

DON: Police! Froyling di Vito!

DAWN: Du gabriel mi a balloontiful grift, Don. A linkwa. Epp frontier ta deepternity, yago parlo osolomiento Unamunda! ["You gave me a beautiful gift, Don. A language. And from here to eternity I'm going to speak only Unamunda!"] [Suddenly remembering.] Mock... da payola!

DON: Da payola.

DAWN: Da geld. Fordham letsin. ["The money for the lesson."] [Holding out money.] Dots allada geld ya doppda mit mi. Cheer. ["That's all the money I have with me. Here."] Cheer! Melgibson da rest end a morgen. ["I'll give you the rest tomorrow."]

DON: I can't take your money, Dawn.

DAWN: Squeegie...?

DON: I'm sorry, but 1... I c-c-can't take your money.

DAWN: Du parla johncleese?

DON: Actually, yes, I do speak a little johncleese.

DAWN: Mock du parlit parfoom!

DON: I've been practicing a lot. Anyway, 1-1-1-1 don't think I mentioned that the first lesson is free.

DAWN: Votsda mattress? Cheer! Etsyuris! ["What's the matter? Here! It's yours!"]

DON: I can't take it.

DAWN: Porky?

DON: Because it's a fraud.

DAWN: Squeegie?

DON: Unamunda. It's a fraud. It's a con game. A swindle. A parla trick.

DAWN: No crayola. ["I don't believe you."]

DON: Believe it, Dawn! I should know - I invented it! Granted, it's not a very good con, since you're the only person who's ever knocked at that door, and I'm obviously not a very good con man, since I'm refusing to accept your very attractive and generous money, but I can't stand the thought of you walking out there saying "velcro belljar harvardyu" and having people laugh at you. I swear, Dawn, I swear, I didn't want to hurt you. How could I? How could anybody? Your beau-tiful heart... It shines out of you like a beacon. And then there's me. A total fraud. I wish I could lie in any language and say it wasn't so, but... I'm sorry, Dawn. I'm so, so... sorry.

DAWN: Unamunda arf da linkwa looniversahl!

DON: But you and I are the only peepholes in da voooid who speak it!

DAWN: Dolby udders! Dolby udders! ["There'll be others!"]

DON: Who? What others?

DAWN: Don, if you and I can speak this linkwa supreemka, anybody can. Everybody will! This isn't just any language. This isn't just any room! This is the Garden of Eden. And you and I are finding names for a whole new world. I was so...

DON: Happy. I know. So was I.
```

---

## IC-1220: Urinetown – The Musical

- Title: Urinetown – The Musical
- Author (byline): Mark Hollmann and Greg Kotis
- Work: Not specified
- Publisher: Farrar, Straus and Giroux
- Publication date as stated: Feb 2003
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: LOCKSTOCK, LITTLE SALLY, FIPP, CLADWELL, HOPE, PENNY, OLD MAN STRONG, LITTLE BECKY TWO-SHOES, MCQUEEN, BOBBY, THE POOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1768
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mark Holman and Greg Kotis
ISBN: 978-0571211821
Publisher: Farrar, Straus and Giroux
Date (Month/Year): Feb 2003
```

### Introduction (context only: never use it for content warnings)

```text
Welcome to Urinetown -- a place where citizens must pay to pee and anyone daring to question authority mysteriously “disappears.” Sound absurd? Maybe not. In today’s America, where basic human needs like healthcare, housing, and even clean water often come with a price tag, Urinetown feels less like satire and more like a mirror. Beneath its ridiculous premise lies a biting truth: when greed runs the system and justice can be bought, dystopia starts to feel a lot like business as usual. Urinetown – The Musical by Mark Hollmann and Greg Kotis
```

### Performance text (classify this)

```text
Early morning. The poorest, filthiest urinal in town. Above the entrance to the urinal hangs a sign that reads Public Amenity #9. Officer Lockstock enters and addresses the audience directly.

LOCKSTOCK: (Pg 9-10) Well, hello there. And welcome to a town like any town. (motions to sign) As the sign says, it’s a “public amenity,” meaning public toilet. People have been waiting for hours to get in; it’s the only amenity they can afford to get into.

LITTLE SALLY: Say, Officer Lockstock, is this where you tell the audience about the water shortage? The hard times? The drought? A shortage so awful that private toilets eventually became unthinkable?

LOCKSTOCK: Little Sally. You're too young to understand, but nothing can kill a show like too much exposition.

LITTLE SALLY: How about a bad title? That could kill a show pretty good.

LOCKSTOCK: (Pg 11) (ignoring Little Sally) These public bathrooms are controlled by a private company, the Urine Good Company. They keep admission high, so if you're down on your luck, you have to come to a place like this -- one of the poorest, filthiest urinals in town.

LITTLE SALLY: And you can't just go in the bushes either -- there's laws against it. (counting coins in her hand)

LOCKSTOCK: That's right, Little Sally. Harsh laws, too. That's why Little Sally here's counting her pennies.

LITTLE SALLY: I'm very close, Officer. (Pg 14) 496 . . . 497 . . . Only a few pennies away . . .

LOCKSTOCK: (Pg 11) Aren't we all, Little Sally. Aren't we all.

The executive offices of Urine Good Company. Cladwell is meeting with Senator Fipp.

FIPP: (Pg 21) I made my speech! Where's my dough?!

CLADWELL: Oh, there'll be plenty of dough for everyone, Senator, once the new fee hikes breeze through the Legislature.

FIPP: It's a powder keg out there, Cladwell. This time I think it's gonna blow! (exits)

CLADWELL: (Pg 23) (to the audience) Twenty years ago we came to the people of this community with a simple proposition: Look the other way while we run this company the way we see fit, and we will keep the pee off the street and the water in the ground. I made flushing mean “flush at the bank!” (proud beat, the introduces Hope) This here's my daughter Hope Cladwell. One day she may be standing in the shoes you see me wearing today, the shoes I wore when I made that promise those many years ago.

HOPE: (Pg 24) Gosh, I never realized large, monopolizing corporations could be such a force for good in the world. (Pg 27) Gosh, Daddy, why do I feel so conflicted?

CLADWELL: Nonsense. Did I send you to the Most Expensive University in the World to teach you how to feel conflicted, or to learn how to manipulate great masses of people? *****Scene***** Public Amenity #9

PENNY: (Pg 14-16) All right, folks, you know the drill. Form a line and have yer money ready. We'll not be repeating yesterday's fiasco, and that means you, Old Man Strong.

OLD MAN STRONG: C'mon, Penny, I'm good for it.

PENNY: That's what you said last week and I still haven't seen penny one. And it's Ms. Pennywise to you.

OLD MAN STRONG: Now, Ms. Pennywise, we've all had to make special . . . arrangements with people in high places over the years. Why not let this one be ours?

PENNY: Get your head out of the clouds! No one gets in for free.

OLD MAN STRONG: In the name of God, Penny, what difference could it make?

PENNY: The politicians in their wisdom taxed the toilets and made illegal Public urination. [And] I run the only toilet in this part of town, you see. So, if you've got to go, you've got to go through me. Water's worth its weight in gold these days. No more bathrooms like the olden days. It's a privilege to pee.

OLD MAN STRONG: (Pg 18-20) It's no way to live, I tells ya! No way to live! (struggling to hold his bladder, he turns from the audience and urinates on the street)

LITTLE BECKY TWO-SHOES: He's peein' right there on the pavement, he is!

LOCKSTOCK: (enters blowing a police whistle, he sidesteps to avoid the large puddle) Breaking the Public Health Act is an exiling offense, Strong.

LITTLE BECKY TWO-SHOES: (gasps)

OLD MAN STRONG: (zipping up and turning back to audience) What if it is? I feel better now, and that's all I cares about. I did what I thought was necessary! (cuffed off by Lockstock, he yells as he is hustled away) . . . Remember me, boys! Remember me!

PENNY: (Pg 9) (shrugs without sympathy) They carted old So-and-So off to Urinetown! (dusts off her hands and gets back to business) (Pg 14) All right, folks, you know the drill. Form a line and have yer money ready. *****Scene*****

LITTLE SALLY: (Pg 38) What's it like, Officer Lockstock? Urinetown.

LOCKSTOCK: (Pg 9) It’s kind of a mythical place. A bad place. Its power depends on mystery (whispers) (Pg 38) I can't just blurt it out, like, "There is no Urinetown! We just kill people!" *****Scene***** Public Amenity #9 McQueen makes a speech to the poor.

MCQUEEN: (Pg 39) And so with this piece of paper the UGC awards Amenity Number Nine the first of our new and entirely legal fee hikes, which we hope you all will honor and enjoy. Of course, no one knows better than the good people at Urine Good Company how difficult times are, but research into finding the long-term solutions we need is expensive. So, for the time being, our decision is firm and we look forward to going to Rio with our new profits. (Pause) I mean, we look forward to finding lasting solutions . . . and things like that.

BOBBY: (Pg 40) (to Penny) I was up all night thinking about what happened to my father yesterday. About what’s happening to all of us.

PENNY: He broke the law, Bobby Strong. (to the people waiting) All right, folks, you know the drill. We’ll take your fee now. The improved fee, that is.

BOBBY: (Pg 41-42) But what if the law is wrong? What if all this is wrong?! Daily we make them pay their nickels, dimes, and quarters. And we keep filling moneybags with broken lives and dreams, but what's it for? I can't ignore these black, immoral profit-making schemes.

PENNY: The fee is the law, Bobby Strong.

BOBBY: What if there was a new law in town, Ms. Pennywise? A new law that didn't come from any voting process or elected body or process of judicial review, but a brand-new law that came from (he thumps his chest) a heart? (rallying the poor, he turns and shouts) This one’s on the house for everyone! Forever! (Pg 48) Relieve yourself in happiness! (crowd cheers and rushes the public amenity) *****Scene***** The good offices of Urine Good Company.

MCQUEEN: (Pg 44-45) Sorry to interrupt, Mister Cladwell. We've got a little problem. Public Amenity Number Nine, sir, The people there have rioted.

CLADWELL: Rioted?!

LOCKSTOCK: [Led by] a young man by the name of Bobby Strong.

PENNY: They're peeing for free, Caldwell. I tried to stop them.

MCQUEEN: Strictly symbolic, sir. The crowd gathered there is an unthinkably small percentage of the population as a whole.

CLADWELL: (Pg 46) People are animals! (Pg 45) What would you do if the very foundation of your life's work were threatened by the rabble-rousing son of a convicted criminal? We nip this unpleasantness in the bud! (exits in a huff; others follow) *****Scene***** Public Amenity #9

LITTLE BECKY TWO-SHOES: (A police whistle)Police! (The cops enter with CLADWELL)

BOBBY: (Pg 49) Wait! Wait! Please, everyone, remain calm! We've taken control of this amenity, Cladwell! The people here pee for free.

LITTLE SALLY: Officer Lockstock, what's happening?

CLADWELL: That's my amenity, Officers. I want all of these people taken away.

LITTLE SALLY: (to Lockstock) But what about Bobby's dreams?

LOCKSTOCK: (to Sally) Dreams are meant to be crushed. It's nature's way.

PENNY: (Pg 50) The amenity won't take much more of this uprising, Caldwell. Bobby's a sweet boy, but not sweet enough to sweeten that spillage, not by a long shot.

BOBBY: The amenity will take as much as it has to, Ms. Pennywise. The days of deprivation are over for these people.

THE POOR: Hooray!

CLADWELL: The days of deprivation have just begun if this madness continues a moment longer.

BOBBY: Sure, Mister Cladwell, that's what you've been saying for twenty years. And for twenty years we've waited for the long-term solutions that never came. Well, we're done waiting! A new day has dawned today. A day of hope and happiness when the idea of human dignity is more than just a forgotten notion, but a living, breathing reality!

HOPE: (Pg 52) (rushes in to stop the mayhem) Daddy, these people need understanding, not brutality.

CLADWELL: On the contrary, Hope dear, a little brutality is exactly what these people need. (to Bobby) You are wrong, Mister Strong, You and your socialistic throng! If the people pee for free, they'll push the system to the brink! You are wrong! (Pg 55) You've picked a fight you can't win, today, Mister Strong! Your rabble is no match for my men.

LITTLE SALLY: (defiantly) You can punish our bodies, Mister Cladwell, but you can never punish our spirits!

BOBBY: (Pg 59) (grabs Hope as a shield) Keep your men back, Cladwell! We've got your daughter and we're not letting her go!

HOPE: Help me!

BOBBY: Now run, everybody! Run for your lives! RUN!! *****Scene*****

LOCKSTOCK: (Pg 61) The rebel poor under Bobby's leadership kidnapped Hope and used her as a shield to escape due punishment from my ... man. Word has it, they're holed up in some secret hideout somewhere. (sees Little Sally hiding and nabs her) (Pg 65) Where are they hiding, Little Sally?! Tell me and I'll see things go easy on you.

LITTLE SALLY: Easy on me?! You mean like sending me to the nice part of Urinetown?! Save it for one of your other stoolies, Officer Lockstock. My heart's with the rebellion. And besides, the way I see it, I'm already in Urinetown. We all are. Even you. (to audience) What is Urinetown? It's the town wherever people learn to live in fear. So look around -- Urinetown is your town. *****Scene***** In the secret hideout

BOBBY: (Pg 77) I don't blame you for being angry with me, Hope. But your father gave us no choice.

HOPE: They may not have taught me much at the Most Expensive University in the World, but they taught me this much: kidnapping people is wrong.

BOBBY: I didn't mean to drag you into all this, Hope.

LITTLE BECKY TWO-SHOES: (Pg 70-71) String her up. That's the answer. String up the strumpet daughter of the criminal urinal chain owner Cladwell! Hang her as revenge for her father's crimes.

BOBBY: No one's going to be killing anyone around here. Friends, I know you're afraid. But this has got to be about more than just revenge. I made a promise. A promise that from this day forward, no man would be denied his essential humanity due to the condition of his pocketbook. That no man in need would be ignored by another with the means to help him.

LITTLE BECKY TWO-SHOES: All I remember him saying was "Run! Run for your lives! Run!"

BOBBY: (Pg 75) (continuing) Some of us will almost certainly not make it through the revolution alive! Maybe all of us! But fight on we will, for all the decades necessary, to claim freedom for the people of this land!! ****EPILOGUE*****

LOCKSTOCK: (Pg 98) Hope [eventually] took over her father's business, instituting a series of reforms chat opened the public bathrooms to all the people, to pee for free whenever they liked, as much as they liked, for as long as they liked. The UGC was renamed the Bobby Strong Memorial Toilet Authority and was operated as a public trust for the benefit of the public. (Pg 99) Of course, it wasn't long before the water turned silty, brackish, and then disappeared altogether. As cruel as Caldwell B. Cladwell was, his measures effectively regulated water consumption.

LITTLE SALLY: What?? The good guys finally take over and everything starts falling apart?!

LOCKSTOCK: Don’t people want to be told that their way of life is unsustainable?

LITTLE SALLY: (Pg 100) (sings) This is Urinetown! This is Urinetown! *Ugh!* That title’s awful!

LOCKSTOCK: Thank you. And good night!
```

---

## IC-1221: The Vigilant Rabbit

- Title: The Vigilant Rabbit
- Author (byline): David Sedaris
- Work: Squirrel Seeks Chipmunk
- Publisher: Back Bay Books
- Publication date as stated: Oct 2011
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, SPARROW, HAWK, MUSKRAT, BEAVER, RABBIT, SNAKE, MAGPIE, FROG, UNICORN
- Teaser before the introduction: Yes
- Spoken words (computed): 971
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Sedaris
Book: Squirrel Seeks Chipmunk
ISBN: 978-0316038409
Publisher: Back Bay Books
Date (Month/Year): Oct 2011
```

### Introduction (context only: never use it for content warnings)

```text
There’s a huge laundry list of problems on our planet... terrorism, poverty, crime, COVID-19, corruption, immigration, polarized politics, abuse of power . . . This far from comprehensive list goes on. And on. And on. How can we focus on such weighty issues without falling into a pit of despair? By tempering the darkness with a bit of humor. Enter David Sedaris with an interesting take on both immigration and abuse of power.

The Vigilant Rabbit by David Sedaris
```

### Performance text (classify this)

```text
NARRATOR: (Pg 98+) A white-tailed doe was discovered one morning disemboweled on the banks of the stream, and the residents of the forest went crazy with fear

SPARROW: Freaked out!

NARRATOR: A few days later a skunk was found, no more than a gnawed-upon skull attached to a short leash of spine. Personality-wise, he'd been no great shakes. Neither was he particularly good-looking, but still! Then a squirrel disappeared, and it was decided that something had to be done.

NARRATOR: A meeting was convened in the clearing near the big oak, and the hawk, who often flew great distances in search of food, proposed that they build a gate.

HAWK: I've seen one where the humans live, and it seems to work fairly well.

MUSKRAT: (Raising his paw) Work how?

NARRATOR: The hawk explained that once the gate was erected, anyone entering the forest would have to stop and identify himself.

HAWK: It keeps out the riffraff. When bad things happen, that is usually who is responsible – riffraff.

MUSKRAT: (Raising his paw again) And what if this riffraff can't be stopped?

HAWK: Then you sound an alarm. It could be anything, really, just so long as it's loud.

NARRATOR: The building of the gate was left to the beaver, who had a slight problem with the hinges, but eventually got them right. Just to the side of them he hung a gong fashioned from an old NO TRESPASSING sign.

BEAVER: I figured I could hit it with my tail. (Giving it a whack for good measure and it echoes)

RABBIT: (stepping forward) Who elected you to man the gate? Anyone could hit a sheet of rusted metal, even someone without an oversize tail. (he picks up a heavy stick and goes at it, creating a racket as loud as the beaver's) I've also got better hearing! I'm slimmer, I'm faster, and I'm more safety conscious, vigilant, you might say.

BEAVER: Whatever! (and he waddles off)

NARRATOR: On the rabbit's first morning as chief of security, he stopped an approaching snake.

SNAKE: (looking up at Rabbit and laughing until he cries)

RABBIT: Something funny?.

SNAKE: (wiping a tear from his face with his tail) You idiots! What good is a gate without a wall?

RABBIT: What good is a… huh?

SNAKE: It doesn't make any sense. If an animal doesn't want to enter here, what's to stop him from moving down a few dozen yards and crawling in beside the fallen pine?

RABBIT: What's to stop him? (he picks up his heavy stick and bashes the snake's head in)

NARRATOR: Then he kicked some dirt over the body and wrote NO LAUGHING on the NO TRESPASSING sign.

NARRATOR: A short while later a magpie stopped by and pecked at the bits of brain left scattered on the ground in front of the gate.

MAGPIE: (between mouthfuls) Not to nitpick, but what's to prevent someone from entering by air? You and your friends initiate a no-fly zone?

RABBIT: What's to keep you from flying in? (and once again he brings down his heavy stick)

NARRATOR: Then he dug up the snake and hung both it and the dead magpie from the top of his gate. There they could act as visual warnings, proof that he was a force to be reckoned with. When that was done, he added to his sign

RABBIT: (Reads the sign aloud) NO TRESPASSING. NO LAUGHING. AND NO STUPID QUESTIONS EITHER. THIS MEANS YOU.

NARRATOR: It was a hot, windless day, and within an hour blowflies arrived and settled on the faces of the two dead animals. Their buzzing attracted a frog.

FROG: (jumps in from the nearby stream, flicks out his tongue, and dins upon the flies. He then notices the sign.) Seeing as you don't want jokes or questions, I guess I'll phrase this as a comment. In order to enter through your gate I'll have to stop and go through your tiresome rigmarole. That kind of BS doesn't interest me much, so instead I'm going to return to my stream and swim into your third-rate, beetle-infested forest. (He turns to leave)

NARRATOR: And the rabbit, who was nothing if not quick, reached for his heavy stick. Then he hung the frog on his gate and added

RABBIT: (he speaks aloud as he adds to the sign) NO CURSING!

NARRATOR: It wasn't long before an otter came along and went for the crushed frog. Then a badger stopped by, attracted by the smell of the dead otter. As the bodies were heaped upon the gate, it began to tilt. The rabbit propped it up with a fallen branch and then turned his attention to the sign.

RABBIT: (speaks aloud as he modifies the sign) NO DIRTY LOOKS. NO QUESTIONING MY INTEGRITY. NO INSULTING REMARKS ABOUT MY EARS OR MY TEETH.

NARRATOR: He was just wondering how to spell "insolence" when a shadow fell, and he looked up to see a magnificent white unicorn. His silky mane curled about his neck in waves the color of buttercups. Equally brilliant was his horn, which looked to be made of gold. At his approach, the rabbit put down his pencil.

RABBIT: State your name and your business.

UNICORN: I'm a unicorn and I come to bring joy to all the forest creatures.

RABBIT: Not with that horn you don't.

UNICORN: I beg your pardon?

RABBIT: I said, lose the weapon.

UNICORN: The horn is what makes me who I am!

RABBIT: Which is unwelcome. Now do as I say or beat it. (reaching for his stick)

UNICORN: But happiness follows wherever I go! I can make a rainbow just by flicking my tail. If you won't let me through the gate, I'll just jump over it.

NARRATOR: And because he was taller than the rabbit and much more powerful, he did just that.

UNICORN: (Looking back to the gate) Sorry, but you didn't leave me any choice.

RABBIT: We'll see about that. (he spits on the ground)

NARRATOR: The unicorn spent the late afternoon making rainbows for all the woodland creatures. Then he caused the wildflowers to bloom and conjured up some berries for a hungry box turtle. As the sun set over the treetops, he settled upon a bed of fragrant moss and fell into a deep sleep. The following morning, the songbirds woke him.

UNICORN: (The unicorn wakes up, yawns and notices a pile of golden shavings scattered across the moss. Then feels his forehead and realizes that his horn has been chewed off) Who chewed off my horn?

RABBIT: Rules are rules. If I let you trot around with a weapon on your head, I'd have to let everyone do it.

UNICORN: But it had magic powers!

RABBIT: I said, scram!

NARRATOR: The unicorn, just a common everyday horse now, slunk off toward a field of tall grasses. The rabbit watched him go and then turned back to his sign.

RABBIT: Magic powers indeed. I didn't taste anything special. (he spits on the ground again)

NARRATOR: Only this time a diamond came out and landed on the ground beside him. That's what he was staring at when the wolves arrived.
```

---

## IC-1222: Villains, Victims, and Very Big Feelings

- Title: Villains, Victims, and Very Big Feelings
- Author (byline): Rebecca Young
- Work: Famous Fantasy Character Monologs
- Publisher: Meriwether Publishing
- Publication date as stated: Sept 2006
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: THE NOT-SO-WICKED WITCH, DOROTHY THE UNGRATEFUL, ACROPHOBIC SUPER-DUPER MAN, THE LONELY CAPTAIN HOOK, THE DISGRUNTLED TOOTH FAIRY, DISILLUSIONED SANDMAN, THE BIG BAD WOLF
- Teaser before the introduction: Yes
- Spoken words (computed): 1937
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rebecca Young
Book: Famous Fantasy Character Monologs
ISBN: 978-1566081160
Publisher: Meriwether Publishing
Date (Month/Year): Sept 2006
```

### Introduction (context only: never use it for content warnings)

```text
Imagine a world where the famous fantasy characters, villains, and superheroes finally get to interrupt the narrator and say, “Well . . . actually. . .”

As these legendary characters tell their messy, very human sides of the story, the fairy-tale facade collapses, replaced by the disquieting truth that even fictional characters may need some therapy -- and perhaps a little less judgment. The stories we thought we knew unravel into a fast-paced comedy about reputation, responsibility, and the very human need to finally be heard.

Villains, Victims and Very Big Feelings from Famous Fantasy Character Monologs by Rebecca Young
```

### Performance text (classify this)

```text
THE NOT-SO-WICKED WITCH: (Pg 1) You know, you really shouldn't believe everything you hear. It'll get you into trouble every time. With stories, they get retold so much that by the time someone writes them down, there isn't anything but half-truths hidden within them. They become a pack of lies, twisted and turned until nobody could straighten out the real story from what's left. Take me, for instance. I've got a story to tell. I do. But nobody wants to hear it. Instead they listen to Little Miss Good Witch. Somehow she made the whole world believe she's so sweet! Well, just like I'm not so wicked, she's not so good. She's messed up a time or two. Cast a bad spell. Brewed a rotten potion. Just never gets caught. But who you gonna believe? Someone dressed in black? Yeah, right. It's a bum rap! All I ask is that you take time to hear how things really happened. To me and to others. Oh, don't look so shocked. I'm not the only one. There are plenty more like me: Other characters with a story to tell, living lives of twisted truths.

DOROTHY THE UNGRATEFUL: (enters skipping and happy, twists her ankle and the façade drops) (Pg 14) Follow the yellow brick road, my foot! This thing never ends! I've been skipping along for hours, and I think I'm going in circles! Why did I ever get directions from a bunch of munchkins? I should've known from all that giggling that they were up to something!

THE NOT-SO-WICKED WITCH: (Pg 7) Glinda’s the one that turned all of the townspeople into munchkins! And didn't even get in trouble. I turn one little guy into a scarecrow, and all of a sudden I'm wicked.

DOROTHY THE UNGRATEFUL: (Pg 14) There's probably no such thing as a Wizard of Oz or an Emerald City. They just wanted to get me as far away from their little town as possible before that wicked witch came back. Well, it wasn't my fault my house landed on her stupid sister. All I wanted was to go home. Couldn't Glinda just wave that magic wand of hers and send me back to Kansas? "Go to Oz," she said. "The Wizard will help you." What was wrong with her helping me?

THE NOT-SO-WICKED WITCH: (Pg 7) Everyone thinks Little Miss Good Witch is perfect! It makes me want to choke a toad! All pretty in pink like a big puff of cotton candy! Nobody thinks evil could reside in all that fluff! What do they give me to wear? Black, black, and more black! How's a person to look nice in that? And do you know how hot it gets wearing black all summer long? It's no wonder I'm a bit grouchy at times! Of course, she's all smiles and full of cute little songs with her perky little voice! Well, let her wear this get-up for a while and we'll see how she feels! But not Glinda! Oh no! She's the Good Witch! So what does that make me? The Bad One, of course. What a joke!

DOROTHY THE UNGRATEFUL: (Pg 14) After all, I landed my house on their stupid old witch, didn't I? Didn't she owe me something for that? I ask for help and instead I get some lame directions and a pair of glittery red shoes. Now she's got me walking in circles in a pair of shoes that are causing some very un-magical blisters! Oh, Auntie Em! There's no place like home! There's no place like home! (hobbles off)

THE NOT-SO-WICKED WITCH: (Pg 7) It makes me so mad; I've just got to zap someone! (Makes pointing gesture to someone flying through the air) Zap! (Blows off zapping finger) There. Now I do feel a little better. (cackles and exits in pursuit of Dorothy)

ACROPHOBIC SUPER-DUPER MAN: (Pg 99) (dodging the witch’s “ZAP”, he lands in a superhero pose) (in a superhero voice) It's an eagle. It's a jet. (drops the facade) It's ... oh, give me a break.

Everyone knows it's me. But what I bet they don't know is: I absolutely hate flying. It scares me to death.

THE LONELY CAPTAIN HOOK: (Pg 76) (who may or may not be a little tipsy. He steps forward trying to one-up ASDM) Do you know what it's like being stuck out to sea, seeing nothin' but water for ages? It makes my sea legs quite wobbly, I tell you! (staggers a bit) And that ain't from the rum neither! Ha ha! I've been riding that ol' wooden bucket for months. Some days are real exciting, like when we're looting or fighting. Other times are just plain boring. Hanging out with a bunch of sweaty old men who haven't bathed since the last time we saw land!

ACROPHOBIC SUPER-DUPER MAN: (Pg 99) Do you know how far down the ground is from where I fly? A man could get seriously hurt if something went wrong. That's why I close my eyes sometimes, but do you know how many times I've had to dodge a plane? Or a flock of geese? Believe me, those birds aren't so nice when you upset their formation. I can't tell you how many times I've been attacked! One day I'm liable to get pecked to death, right up there in the sky. But what choice do I have?

THE LONELY CAPTAIN HOOK: (Pg 76) I actually look forward to seeing Peter flying around my ship, free as a bird. All dressed in green with that silly pointed hat! Playing tricks on my crew and tangling up my sails! Taunting us. I know you won't believe this, but I actually care about that silly boy named Peter. Without him, my ship would be in shambles! Whenever the crew gets cabin fever and start beating up on each other, here comes Peter, flitting about trying to cause trouble. He thinks he's annoying me, but I have no interest in hurting the little booger. He's the only thing exciting around here!

ACROPHOBIC SUPER-DUPER MAN: (Pg 99) When someone needs me, I have to get there fast. There's no advance warning. No time to hail a cab or hop on the subway! I've thought about getting a car, but people drive like maniacs! I guess, all in all, I'm safer in the air. It's kind of peaceful ... up in the clouds ... (Looks up at sky dreamily)

THE LONELY CAPTAIN HOOK: (Pg 76) Oh look! Here Peter comes now! "I'm gonna get you! You and that pixie bug! By hand or by hook, I'm gonna get you!" (Exits in pursuit of Peter)

ACROPHOBIC SUPER-DUPER MAN: (Pg 99) (after saying a quick prayer, launches into the air) It's an eagle. It's a jet!

THE DISGRUNTLED TOOTH FAIRY: (Pg 10) (and a new flying creature softly descends, yawning) I am so tired! I spent all night flying around, and I'm plumb worn out! Not to mention bruised! Doesn't anyone use a nightlight anymore? I couldn't see a thing, and I must've bumped into a dozen dressers! And for what? No one even cares about me. Used to be, I'd get sweet little notes thanking me for visiting. But those days are long gone.

DISILLUSIONED SANDMAN: (Pg 124) (enters and nods in agreement) [You tell it sister!] (blows a puff of sand into the Tooth Fairy’s face) This job is nothing like I thought it would be. It doesn't have the first thing to do with sand - not the real kind anyway! I pictured sandy beaches. Girls in bikinis. Drinks with fancy umbrellas. Parties and bonfires. The kind of job any guy would dream of having! Ha! You know what? This stupid job has zero to do with any of that. I work in complete darkness - stuck on the stinking third shift! I haven't seen the light of day since I started working. Who ever heard of a Sandman that helps people sleep?

THE DISGRUNTLED TOOTH FAIRY: (Pg 10) [I know!] Nowadays, if I do get a note, it's not to say thanks. Oooh, nooo! It's to tell me exactly how much I'm supposed to pay for a silly little white nub wrapped in bloody toilet paper! And it's not cheap either! (opens a note from a child) A dollar? You've got to be kidding me! Who pays a dollar for a tooth?

DISILLUSIONED SANDMAN: (Pg 124) [Yeah!] Whatever happened to counting sheep or drinking warm milk? Or Tylenol P.M.? What the heck do people need me for?

THE DISGRUNTLED TOOTH FAIRY: (Pg 10) I don't know why I do this night after night. Maybe I should move on. Be a fairy godmother or something. You know, turn pumpkins into coaches! Now, that would be cool! But then I think about all those children going to bed every night, waiting for me. How would they feel if I just didn't show up? Their little hearts would be broken. And what would parents do with all those little teeth? Throw them away? Oh, I couldn't let that happen!

DISILLUSIONED SANDMAN: (Pg 124) What about the hot chicks wanting to nap at the beach? Why can't I help them? How does a guy get promoted to a job like that? I'm stuck on the worst shift. No one - and I mean no one - above the age of fifteen and under the age of forty ever sleeps with a light on. Not even a tiny one. It's pitch black the whole night. And if you get caught flashing - that's code for turning on the light - it's instant termination! I don't know how much more I can take. How can they expect any normal guy to work this way? I got the wrong job!

THE DISGRUNTLED TOOTH FAIRY: (Pg 10) Maybe I just need a nap ... (motions to The Sandman to hit her with the dust again) (Both exit as Little Red stealthily enters) SECRET AGENT LITTLE RED RIDING HOOD: (Pg 31) I'd been following that wolf for weeks trying to pin something on him. I knew without a doubt that he was bad to the core. I just didn't have any proof. The little red riding hood thing was brilliant. He'd never suspect a helpless young girl on her way to see her grandma. Ha! I laugh at the thought of me being helpless! I'm at the top of my karate class! (does a few karate chops in the air) The basket of goodies was just too much to resist. That stupid wolf trailed me all the way up the mountain. Ducking behind trees. Crouching down beside bushes. He wasn't very clever at hiding, I can tell you that.

THE BIG BAD WOLF: (Pg 92) (hand cuffed behind his back) This is all a big mistake! It was a joke! An innocent prank gone wrong. I wasn't going to eat her! I promise! I'm a vegan. I don't even eat anything that's been anywhere near meat. I swear. I wasn't going to harm a hair on her hooded head. But a wolf's got to have some fun, you know? SECRET AGENT LITTLE RED RIDING HOOD: (Pg 31) I didn't think he was ever going to take the lead and beat me there. I had to stop and tie my shoes twice just to give him a head start. Even then, I could hear the pitiful thing puffing like crazy. I was afraid I might have to give him mouth-to-mouth resuscitation and save his life instead of capturing him! But it was all going according to plan. The lady I hired to play my grandma played her part excellently. By the time I got there, she'd let the wolf tie her up and stuff her in the closet, just like I’d told her to.

THE BIG BAD WOLF: (Pg 92) You should've seen her face! (mocking) "Why Grandma, what big teeth you've got!" The girl needs some serious glasses if she really thought I was her grandma. Look at all the fur, man! (lifts arm awkwardly) I mean, if her grandma looks like this, then she's got one freaky grandma! I thought she'd take one look at me and run laughing -- or screaming -- from the room! I never dreamed she'd stick around. SECRET AGENT LITTLE RED RIDING HOOD: (Pg 31) But then it all went down the drain. All that work. All that planning. For nothing. Here comes the big, bad woodsman to save the day. Couldn't he see that I had it all under control? I was going to pound on that wolf's head, I tell you. (karate chops in the air) Had it all planned out. I'd even gotten in a kick or two before the woodsman ruined everything.

THE BIG BAD WOLF: (Pg 92) She practically stuck her head in I my mouth; she was so close to my face! You gotta give me a break, man! I couldn't help but lick her a little! (cowers as an unseen woodsman raises his ax) Whoa! Hold back on the axe, man! Go check the closet! Her old granny's in there. I didn't harm a gray hair on her head! Go on! Go see! (points in one direction and then runs off in the other direction, yelling) Some people just can't take a joke, can they? SECRET AGENT LITTLE RED RIDING HOOD: (Pg 31) Guess the one good thing is I kept my cover. Secret Agent Little Red Riding Hood, at your service. (bows)
```

---

## IC-1223: The Waking of the Prince

- Title: The Waking of the Prince
- Author (byline): William J. Brooke
- Work: A Telling of the Tales: Five Stories
- Publisher: Harpercollins
- Publication date as stated: April 1990
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR 1, NARRATOR 2, PRINCE, PRINCESS, CAPTAIN, KING, IGNISPIRUS
- Teaser before the introduction: Yes
- Spoken words (computed): 1940
- Already set (do not supply): none

### Source block (context only)

```text
Author: William J. Brooke
Book: A Telling of the Tales: Five Stories
ISBN: 978-0060206895
Publisher: Harpercollins
Date (Month/Year): April 1990
```

### Introduction (context only: never use it for content warnings)

```text
Napping Beauty by William J. Brooke
```

### Performance text (classify this)

```text
NARRATOR 1: (Very dramatically) Ducking under a burst of flame, the Prince throws himself forward into a double roll. With the last of his strength, he thrusts the sword into the underbelly of the dragon.

NARRATOR 2: Hold it! What’s wrong with “once upon a time?” That’s how we’ve always done it.

NARRATOR 1: Times have changed. Kids expect a lot of blood and guts. Blame television. (Clears throat and continues) Steam and blood boil forth as the dragon sinks to the ground . . . Are you going to help me tell the story or not?

Scene 1

NARRATOR 2: (sighs, then speaks flatly) When the mists clear, the dragon has crumbled into dust. The forest of thorns melts into the ground.

NARRATOR 1: (dramatically) Then the Prince charges into the castle and bounds up the spiral staircase.

NARRATOR 2: Add trips.

NARRATOR 1: (surprised) He trips?

NARRATOR 2: Yeah. You forgot about the sleeping bodies on the staircase. It’s part of the curse. Everybody falls asleep for 100 years.

NARRATOR 1: Fine. (Continues dramatically) He leaps to his feet again and enters the tower room at the castle top. There, lying on the spinning wheel is a princess.

PRINCE: Ah! There is beauty beyond beauty!

NARRATOR 2: The Prince leans forward and gently kisses her lips.

NARRATOR 1: Color rushes to the curve of her cheeks. Her eyes flutter open.

PRINCE: I am the Prince Valorian. I have fought my way past the forest of thorns and the evil dragon that guarded your castle. I have awakened you from your 100 year old sleep.

PRINCESS: Hold it, bud. Let’s see some Identification.

PRINCE: Identification?

PRINCESS: You don’t look like a prince to me. Your clothes are a mess.

PRINCE: (insulted) I had a little difficulty getting in here, you know.

PRINCESS: You didn’t happen to notice any guards on your way did you? (worried) They should be here. It’s my 21st birthday.

PRINCE: Actually it’s your 121st. You’ve been asleep for 100 years.

PRINCESS: No way! That’s what I’ve been guarding against, a curse or something.

PRINCE: Well you didn’t make it. I saw you sleeping on that wheel.

PRINCESS: You’re wrong. I was only napping.

PRINCE: (Frustrated) This isn’t going at all how I expected. Look, the curse worked out. You slept 100 years. The thorns grew up. I killed the Evil dragon, then ran up here and woke you up. OK?

PRINCESS: Woke me up? How?

PRINCE: (boasting) I kissed you.

NARRATOR 2: Her mouth drops open to a perfect O. She steps closer and looks up at him. She raises a dainty hand up to his face and then . . .

NARRATOR 1: Slaps his face!

PRINCE: What did you do that for?

NARRATOR 2: Yes, what did she do that for?

NARRATOR 1: I told you. Times have changed. Women don’t like being treated as helpless victims.

PRINCESS: Did it ever occur to you that I might not have wanted to be kissed.

NARRATOR 2: Suddenly, there is a clatter on the stairs as 12 panting, puffing guards rush into the room.

CAPTAIN: Your highness, I’m very sorry we were not with you but--

NARRATOR 1: His eyes go round, seeing the spinning wheel.

CAPTAIN: The wheel! Attack!

NARRATOR 2: The guards leap fearlessly at the spinning wheel and wrestle it to the ground.

CAPTAIN: Stay back, your highness, I will protect you!

NARRATOR 1: The guards hurl the wheel out of the window.

PRINCESS: Captain! Tell me, did you or your men see a forest of thorns anywhere? All over the castle, I've heard.

PRINCE: Were all over the castle. They melted when I killed the dragon.

PRINCESS: Captain, arrest this man!

NARRATOR 2: The Captain steps up to the Prince and holds the point of his sword at the Prince's throat.

CAPTAIN: I command you to yield yourself to my sword.

PRINCE: This sword?

NARRATOR 1: The Prince twists the sword away and throws it out the window.

CAPTAIN: Well, that was the one I had in mind.

NARRATOR 2: At once, the 11 guards attack the Prince.

NARRATOR 1: (melodramatically) The Prince slams one guard against the wall and also throws that man's sword out the window. The Prince kicks and grunts as he tosses more swords through the window.

PRINCE: (breathing heavily and with just a touch of sarcasm) I hope the Princess will reconsider her order and offer me better hospitality.

PRINCESS: Perhaps I was a bit hasty. Tell me about yourself. What brings you here?

PRINCE: Adventure. The whole world knows your story - the sleeping beauty in the tower. I wanted to save you. It's what heroes do.

PRINCESS: Save me? From a nap? Ha!

KING: (from the stairwell) I'm coming, my dear! I'm coming!

NARRATOR 2: A flushed face topped with snow-white hair and a golden crown appears above the stairwell.

KING: (panting) Are you.....alright? I would have been here sooner, but it was raining swords in the courtyard.

PRINCE: (bowing) Your majesty.

KING: Who's he?

PRINCESS: Says he's a prince. He broke into the castle, resisted arrest -

PRINCE: (interrupting) slew the dragon, melted into the forest of thorns, and awakened the Princess.

PRINCESS: (indignant) He kissed me!

KING: (to prince) Do you happen to have any form of identification?

PRINCE: What is this identification thing? A man is what he does! Judge me by my deeds, not by my name! Forgive my temper, Your Majesty, but it's been a long day.

NARRATOR 1: The King listens as Prince Valorian retells his story.

KING: Our problem is that there is no proof of what you say. One would certainly think that a 100 year sleep would leave some kind of evidence.

PRINCE: Look, the idea was that the Princess would, well, fall in love with and -

PRINCESS: Fall in love with you! Of all the conceited . . .

PRINCE: And we would marry and -

PRINCESS: Father, are you going to let this ridiculous man . . .

KING: Now, Princess, calm down. (to Prince) You know it's easier to rule a kingdom than a daughter . . . perhaps you could perform a heroic deed.

PRINCE: What sort of deed?

KING: Oh, slaying a dragon would be acceptable.

PRINCE: (shouting) I already slew a dragon

KING: Yes, well, we were all asleep, weren't we? Now, there is a very famous dragon in the kingdom Farflum. Ignispirus Magnus is his name. Bring back his head, and we'll talk about my daughter's hand.

PRINCE: Actually, after the events of the last hour, fighting a dragon will be a pleasant change of company. (He leaves)

PRINCESS: (Enviously) My life is sooo boring. I sit and sew. I wave at people from the balcony. I wish . . . Scene 2

NARRATOR 1: (dramatically) Ducking under a burst of flame, the Prince throws himself forward into a double roll. With the last of his strength, he thrusts his sword

NARRATOR 2: Or rather, what should have been the soft, underbelly of the dragon, but is in fact empty space.

NARRATOR 1: The dragon hovers above the Prince, wings flapping.

IGNISPIRUS: Nice moves.

NARRATOR 2: The ground shakes as a terrible rush of hot air whirls about the Prince. He closes his eyes and tries to think of the Princess in this, his last moment.

NARRATOR 1: But nothing happens. The Prince opens his eyes.

IGNISPIRUS: Excuse me. Heartburn. Sorry. I'm not used to this kind of activity. Not that it wasn't fun. That double roll of yours was impressive.

PRINCE: I killed a dragon with it just recently as a matter of fact.

IGNISPIRUS: Must have been a young one, you don't live long as a dragon without learning to cover your belly.

NARRATOR 1: The Prince reaches the cave entrance, then makes a break for it.

IGNISPIRUS: Wait! Don't go! I was going to make us tea! (time passes and the Prince realizes he left is sword in the dragon’s cave, resignedly he returns)

PRINCE: Ignispirus! Yoo-hoo Iggy!

NARRATOR 1: A burst of flame rolls from the cave. A huge green head with flashing eyes appear.

IGNISPIRUS: Unauthorized nicknames are exceedingly rude!

PRINCE: Sorry, Ah, I’d like to take you up on that cup of tea.

IGNISPIRUS: Why did you leave so abruptly?

PRINCE: I was concerned . . . Well, a little nervous. . . OK. I was frightened out of my wits! You shot fire at me!

IGNISPIRUS: You came in here swinging with a sword.

PRINCE: I’m a hero. I’m supposed to act like that.

IGNISPIRUS: You know, I’m beginning to wonder if you’re a real prince. Do you have any I.D.?

PRINCE: (furiously) I am a real prince! You’re nothing but an oversized bird!

NARRATOR 2: The dragon opens his jaws. The Prince disappears between them.

NARRATOR 1: For a while, the dragon sits there, enjoying the morning sun on his scales and ignores the muffled sounds coming from inside his mouth.

NARRATOR 2: Finally, after what seems as 100 years to the Prince, the dragon opens his jaws and deposits a damp prince on the ground.

PRINCE: Perhaps I should apologize.

IGNISPIRUS: I should think so! Sit there and dry out while I do the talking. There are some things you (sarcastically) heroes need to learn.

PRINCE: (wringing saliva out of his shirt) What things?

IGNISPIRUS: Take this dragon-slaying stuff. No one ever looks at the dragon’s point of view. We’re supposed to capture maidens for instance. But what am I supposed to do with them? They are too small for a decent meal and too ugly for romance. I tried to get some to do a little cave work, but nooooo! They’re too good for that. The only thing maidens are good for is prince bait.

PRINCE: But when the Princes rescue them, don’t the maidens fall madly in love with them?

IGNISPIRUS: See that’s another myth. Love takes time. Just because you can kill a dragon doesn’t mean anyone is going to give a fig.

PRINCE: I found that out. So what do they want?

IGNISPIRUS: Respect. Tenderness. Honesty.

NARRATOR 1: The dragon lowers his head and snorts.

IGNISPIRUS: It’s what we dragons want too. Ah but you didn’t come here to apologize. You came back to steal your sword, didn’t you?

PRINCE: I’m insulted you’d even think that. Talk about being rude.

IGNISPIRUS: Well maybe I was wrong about you. Forgive me. I’m beginning another molt. It makes me cranky.

NARRATOR 2: The dragon scratches behind an ear, dislodges a few scales. They crash to the ground. . . . (and the Prince and the Dragon enter into a lengthy conspiratorial conversation) Scene 3

NARRATOR 1: The King, the Queen and Princess are in the throne room when the Prince enters and hurls down two large green objects.

PRINCE: Having slayed this the terrible Ignispirus Magnus, I claim the Hand of the Princess.

PRINCESS: (pointing at green objects) What are those?

PRINCE: Scales. . . . Scales hewn from the rocklike hide of a terrible dragon.

PRINCESS: Rocklike? Yeah, right. I bet they are rocks.

PRINCE: You don’t believe me?

KING: Why didn’t you bring back the head like we agreed?

PRINCE: Do you have any idea how big a dragons head is? There aren’t any superhighways out here, in case you haven’t noticed.

KING: Well, we still don’t have proof of anything.

PRINCE: (Shouting) Scales! Look at them! Do they prove something?

KING: Captain! Seek out the dragon’s lair. Make sure the dragon is dead. If it isn’t, finish the job.

PRINCE: Don’t bother.

PRINCESS: Aha! So it isn’t dead.

PRINCE: No, just offended. I stood it up for tea. I’m lucky to have escaped with scales and my sword. (winks at audience)

NARRATOR 2: The Princess laughs.

PRINCE: Excuse me, but I’ve got a dragon to apologize to. I was just beginning to learn from him that (to Princess) beautiful maidens may be beautiful on the outside but not necessarily on the inside!

PRINCESS: No one has ever addressed me in such manner!

PRINCE: Yeah, well, have it your way. You weren’t asleep for 100 years. There never was a forest of thorns. I was the one who was sleeping. I failed at being a hero, but not because I didn’t kill the dragon.

NARRATOR 1: He turns his heel.

PRINCESS: Wait!

NARRATOR 2: The Prince gazes at her. She suddenly look sad.

PRINCESS: It isn’t easy being beautiful and sitting in this tower all day.

PRINCE: You want to come with me?

NARRATOR 1: A smile blooms on her face. She jumps and kisses her mother and father good-bye.

NARRATOR 2: The Princess grabs the Prince’s hand, and runs out.

KING: (calling out) By the authority of the divine right, I pronounce you husband and wife! (to himself) Well, she is his problem now.

NARRATOR 1: The end.

NARRATOR 2: The end? Just like that? Whatever happened to “And they lived happily ever after”? It’s the way we’ve always done things.

NARRATOR 1: Do you really think they lived happily ever after?

NARRATOR 2: It’s not impossible. Some people still do.

NARRATOR 1: OK (Clearing voice) As the happy couple rode away, the Princess was heard to say . . .

PRINCESS: So where are we going Val?

PRINCE: To the mountains where dawn awakens! To the land where women spin gold! But first, to a dragon’s cave for tea.

NARRATOR 2: And they lived happily ever after for they made every day an adventure.
```

---

## IC-1224: The Web Files

- Title: The Web Files
- Author (byline): Margie Palatini
- Work: Not specified
- Publisher: Hyperion
- Publication date as stated: May 2001
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: DUCKTECTIVE WEB, ROOSTER, BILL, WEB, HEN, LITTLE BOY BLUE, HORSE, SHEEP, RAT
- Teaser before the introduction: No
- Spoken words (computed): 967
- Already set (do not supply): none

### Source block (context only)

```text
Author: Margie Palatini
ISBN: 978-0786804191
Publisher: Hyperion
Date (Month/Year): May 2001
```

### Introduction (context only: never use it for content warnings)

```text
Vocalizes Opening Theme from Dragnet (1951-1959) *
```

### Performance text (classify this)

```text
Spoken as Ducktective Web: Ladies and Gentlemen, the story you are about to see is true. The names have been changed to protect the innocent. This is the farm. Hundreds of animals. Most of them follow the course as planned. A few of them get lost along the way. When they do, it makes trouble for me. I’m a Ducktective. I carry a badge (flips open badge)

In a normal voice: The Web Files by Margie Palatini

DUCKTECTIVE WEB: My partner, Bill, and I were working the barnyard shift. It was peaceful. Quiet. Then we got the call.

ROOSTER: Cock-a-doodle-doo!

BILL: A lot of squawking going on down in the coop area, Ducktective Web. Looks like fowl play. Report says feathers are flying. Chief says we should check out the chicks.

WEB: Chicks?

BILL: Check.

WEB: Let's fly.

DUM DE DUM DUM

BILL: 6:35A.M. -- The hen's house.

WEB: We knocked on the door. She answered.

HEN: P'awk! P-p-p-awk! P'awk! P'awk! P'awk!

WEB: Just the facts, ma'am. Just the facts.

HEN: I've been robbed! (unruffling her feathers) Robbed, I tell you. Robbed! Robbed! Robbed!

DUCKTECTIVE WEB: So, you're saying that you were robbed, is that right, ma'am? What exactly is missing from the nest, ma'am? Eggs, ma'am? Chicks, ma'am?

HEN: (flapping) P-p-peppers.

WEB: Peppers?

HEN: My perfect purple peppers that were just about ready to be pickled.

WEB: About how many perfect purple almost-pickled peppers would you say were pilfered, pinched, and picked? A bushel?

HEN: (Squawking) P'awk! Pawk! No --- a peck! A peck, I tell you! A whole purple-pepper-pickin' peck!

WEB: Have any idea who would pick a peck of your perfect purple almost-pickled peppers?

HEN: (Clucking) Not a clue.

DUCKTECTIVE WEB: (Turning to Bill with a quack) Round up the usual suspects.

DUM DE DUM DUM

BILL: 9:06 A.M. - Headquarters was hopping.

WEB: (to audience) A miss named Muffet had just been tossed off her tuffet and a gal named Peep was missing some sheep. I noticed that three little kittens had lost their mittens. They began to cry. I wanted to help. I couldn't. I had pickled peppers to worry about. We had Horner in the comer and were trying to make Little Boy Blue quack. (To Little Boy Blue) Okay, Blue Boy. Quit blowing your horn. Time to make hay. Suppose you just tell me where you were this morning.

LITTLE BOY BLUE: (Quivering) I’m innocent, I tell you! Innocent! I was under the haystack. Fast asleep! Honest. Ask anybody.

WEB: Sure. Sure. I've heard that bedtime story before. (To Bill) Got any witnesses?

BILL: (Shaking his head) No. The sheep were in the meadow. Cows were in the com.

WEB: Things looked black for the boy in blue. And then. . . we got another call. *Ring Ring*

BILL: (Answering, he listens with some Uh-huhs, then to Web) There's been some horsin' around reported down near Barn and Pen, Looks like another robbery.

WEB: We put the kid out to pasture.

DUM DE DUM DUM

BILL: 10:43 A.M. - Comer of Barn and Pen

WEB: (to audience) Bill and I talked to the horses. (calling out to the horses) Whoa! Whoa! You there. Like to ask you a few questions if you don't mind, sir.

HORSE: Na-a-a-ay. Not at all.

WEB: What do you know about a peck of unlawfully picked perfect purple almost-pickled peppers?

HORSE: Peppers? Peppers? A peck of purple peppers? Not a thing. But somebody just hightailed it out of here with a tub of my tartest, tasty toMAHtoes!"

WEB: Tomatoes?

HORSE: You say to-MAY-toes . . . I say to-MAH-toes . . . Somebody just hauled the whole thing off!

SHEEP: (Sighing) And find my lettuce while you're at it, too! Somebody just lifted a load of my luscious leafy lettuce not ten minutes ago! This is ba-a-a-d! Really ba-a-a-d!

BILL: (Scratching his head) Peppers? Tomatoes? Lettuce? What do you make out of all of this, Web?

WEB: There was only one thing to make out of all of this. Salad.

DUM DE DUM DUM

BILL: 11:47 A.M. -- The squad room

WEB: My partner and I were still trying to quack the case, but we didn't have any idea whom to I.D.

BILL: Rats!

WEB: That's it! There was only one suspect who was sneaky enough, wily enough, and tricky enough to pick a peck of perfect purple almost-pickled peppers, take a tub of tasty tart tomatoes, and lift a load of luscious leafy lettuce. My partner and I were hot on the tail of . . . That Dirty Rat.

DUM DE DUM DUM

BILL: 12:46 P.M. - A real hole -in-the-wall.

WEB: (Pounding on the door) We know you're holed up in there, you Dirty Rat. Let us in.

RAT: (Opening the door) Eh, what's up, Duck?

WEB: There's been some trouble down on the farm. What do you know about a rash of recent robberies?

RAT: (Innocently) Robberies? Robberies? What makes you think I know anything about a robbery? I'm no cheesy snitch.

WEB: Can it, Ratzo. You've been in nothing but garbage for years.

RAT: (Smirking) Okay. Sure. Sure. Go ahead, flatfoot. Look anywhere you want. But make it quick, Quacker. . . you're interrupting my lunch.

WEB: (looking past him at the Rat’s table) Lunch, eh, Rodent?

RAT: (hissing) Hey, what's going on here? You're not going to pin this rap on me. Where's your evidence, you waddling webfoot? You got nothing on me. Nothing, see? I'm clean! Clean, I tell you. Clean!

WEB: (picking a piece of lettuce from under his chin) Not clean enough, you Dirty Rat. (he smells Rat’s breath) Just as I suspected. Garlic mayo. Book him, Ducko. His salad days are over.

RAT: (Crying, as his hands are cuffed and he is led away) Over? Over? But they can't be over! I haven't even had my dessert!

BILL: (Patting Web on the back) Looks like you quacked another one, Web. But how did you ever figure it was him?

WEB: Just played a hunch. He ate the evidence for lunch . . . and forgot to use his napkin and brush his teeth. He's a dirty rat. He never did have good hygiene.

DUM DE DUM DUM

WEB: The Dirty Rat was tried and convicted on three counts of vegetable vagrancy, offensive bad breath, and not using a napkin to wipe under his chin. He was sent up the river and was sentenced to six months of farm labor with time off for good behavior, better table manners, and clean teeth. CASE CLOSED.

DUM DE DUMDUM DUM DE DUMDUM DUM DUM!
```

---

## IC-1225: The Whole Shebang

- Title: The Whole Shebang
- Author (byline): Rich Orloff
- Work: The Best Short Plays 1994-1995
- Publisher: Hal Leonard Corporation
- Publication date as stated: 1995
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: DEAN, STUDENT, PROF B, PROF A, HARVEY, EDNA
- Teaser before the introduction: Yes
- Spoken words (computed): 1488
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rich Orloff
Book: The Best Short Plays 1994-1995
ISBN: 978-1557832313
Publisher: Hal Leonard Corporation
Date (Month/Year): 1995
```

### Introduction (context only: never use it for content warnings)

```text
What if God was one of us? Just a cute little nerd like . . . you. Or a totally awesome person like . . . YOU. Yeah? In Rich Orloff’s The Whole Shebang we take a playful look at the creation and evaluation of earth, humans, and everything in between.
```

### Performance text (classify this)

```text
Throughout the play, switch out gender references to match the gender of the student actor – The script is written to allow the student to be of either gender.

(The STUDENT enters. He/She carries a globe, a briefcase and some papers, etc. He/she appears very anxious and pressured.)

DEAN: Please relax. This is just an informal review.

STUDENT: You told me my grade depends on this.

DEAN: (Comforting) Try not to think about it. Why don’t we begin with a brief summary of your project?

STUDENT: All right. For my master’s thesis, I elected to devise a self-sustaining and self-evolving, matter based ecosystem in a universe of three dimensions. And so I created the heavens and the earth.

DEAN: Now that you’ve devised this planetary ecosystem, how do you feel about it?

STUDENT: Well, to be honest . . . I think it’s good.

PROF B: Could you be a little more specific?

STUDENT: Certainly. I think the Earth has succeeded in every way I hoped it would. The weather cycle, given its complexity, is quite efficient. All in all, the Earth is fundamentally capable of sustaining itself.

DEAN: I’m most impressed with your creation of water.

PROF A: I must admit, so am I. It may be one of the most efficient liquids any student has designed.

PROF B: I like how when the temperature drops below freezing, you’ve designed it so that water falls as snowflakes instead of ice cubes.

STUDENT: Thanks. That took a lot of work.

DEAN: (Reviewing paper:) Here’s a most impressive statistic: Over 453 zillion snowflakes so far, and only 12 have been alike.

STUDENT: Thanks.

PROF A: By the way, why did you have an ice age?

STUDENT: I . . . I . . . well to be honest, I screwed [messed] up.

DEAN: Well that happens.

PROF A: Can we begin discussing the human being?

STUDENT: I consider the human being to be the crowning achievement of my universe.

PROF A: I have one question regarding the human being. . . Why did you make them so stupid?

STUDENT: I think they’re smart. They’ve created great civilizations. They’ve developed magnificent tools and brilliant works of art. Their awareness of the universe is increasing exponentially.

PROF A: Stop exaggerating. It took them centuries just to come up with the concept of a sandwich.

STUDENT: May I remind you the human being is the sole creature capable of transforming milk into all those other products. Without the human being the Earth would have been a mass of raw material with unrealized potential.

PROF A: Are you saying it’s a better planet because of cheese doodles?

STUDENT: There’s more to the picture than that.

DEAN: Why did you give these creatures domain over the planet?

STUDENT: Well, you see . . . (The Student sighs and checks his watch.) My roommate was supposed to transport a couple of human beings here so I could…It’s very hard to understand them unless you meet them up close. They really are wondrous creatures. (From the hallway we hear voices.)

HARVEY: (Offstage:) What do you mean, “go in there”?! Maybe I don’t want to go in there!

EDNA: (To man) Don’t cause a scene.

HARVEY: This jerk’s causing the scene! Look buddy. I don’t know who you are, but I’ll go in there when I’m good and ready.

(A Man (HARVEY) comes flying into the room as if he was thrown in by someone else. A Woman (EDNA) follows quickly. Both are dressed for bed. They look around, quite bewildered about what’s going on.)

HARVEY: What the –

STUDENT: Oh, good. Just in time. I’m so glad you’re finally here. (The Student pulls up a couple of chairs.) Make yourselves at home.

EDNA: (Frightened) Where are we?

STUDENT: Relax. This won’t take long…Please. (The Humans look at each other and hesitantly sit down.) (To the Professors) I’d like to introduce two typical human beings:

HARVEY: Uh, can I ask a question? . . . Who the hell are you, and why are we here?

STUDENT: Well, since you asked, my roommate teleported through a warp in dimensional barriers, where he realigned your molecules into a pure energetic code. (To the Humans) Don’t worry. This is just what, in our dimension, is the equivalent of one of your universities. These are professors in my department and I’m a student. You’re here as part of my project.

HARVEY: Oh yeah? And what’s your project?

STUDENT: I created the heavens and the earth. (It takes a moment for this to fully sink in on the Humans.)

HARVEY: Wait a second. Are you telling us that you’re –

STUDENT: I am who I am.

EDNA: Sounds like him.

HARVEY: You mean to tell us that, like the entire universe is just like . . . a science fair project?

STUDENT: More or less.

HARVEY: I work my fingers to the bone and all I am is part of some nerd’s science project?!

EDNA: Harvey please (Whispering;) You’ll go to hell.

HARVEY: Eh, I don’t care. With my luck, I could give the Pope CPR and I’d still go to hell.

DEAN: Now then, Harvey and Edna, why don’t you tell us a little about yourselves?

EDNA: Not much to say. We’re just people. Ordinary people.

PROF A: Do the two of you have children?

EDNA: Oh yes. Michael, who’s sixteen and Wendy who’s just about thirteen.

PROF A: What do they excel at? (Harvey and Edna think about this. Nothing comes to mind.)

EDNA: Michael was just made group leader at his drug rehabilitation center.

PROF B: Does Wendy take drugs?

EDNA: Oh, no. Never.

HARVEY: She spends all day in the bathroom, dyeing her hair unnatural colors.

EDNA: (Trying to put things in a good light:) Some of which are very creative.

HARVEY: Yeah, like one day her head’s going to end up in an art gallery.

EDNA: She’s going through a rough time. She still hasn’t gotten over the shock of menstruation.

HARVEY: (To the Student) Not to question your ways or nothing, but couldn’t you think of anything better than puberty?

STUDENT: No, not really. I tried.

EDNA: Harvey, please.

HARVEY: Well, he’s supposed to be all- knowing and all-powerful and he can’t even make their teeth grow in straight. (To the Student:) Do you know how much that cost me?

EDNA: Harvey, please. We’re supposed to be representing the entire human race.

PROF A: I think you’re doing a splendid job.

PROF B: Do you believe that intimacy is important in a relationship?

EDNA: I think intimacy is the keystone of a healthy relationship. I read it in last month’s Cosmo.

PROF A: Harvey and Edna, what would you say has been the best moment of your lives?

EDNA: Oh that’s easy. It was the day Harvey proposed to me. It was the first day of spring, and we were having a picnic in the park. I had made chicken salad sandwiches and potato salad and carrot-raisin salad and macaroni salad – Anyway, so we were having this picnic, and when we finished eating, I wiped Harvey’s mouth with my napkin, and he wiped my mouth with his---

HARVEY: It’s this thing we do.

EDNA: And, and I remember, I remember Harvey looking right in my eyes and saying . . . “Let’s make it legal.” And I thought, this man knows what I want.

PROF B: If I may, I have one final question. Do you think the world is getting better or worse?

HARVEY: Oh, worse.

EDNA: Much worse. Everyone knows that.

PROF A: Then why do you keep living?

HARVEY: Whaddaya mean?

PROF A: Your lives vary in quality from boring to dismal. Your future holds no promise. Why do you keep living? (Harvey and Edna think for a moment, look at each other.)

EDNA: I just dropped ten pounds. I’m not going to die now.

PROF A: And this is why you keep on living?

EDNA: Well, well, we also have to stick around for the kids. After all, if it weren’t for us, who’d be their role models? (The Professors exchange looks with each other.)

HARVEY: (To Edna:) I think you just blew it.

PROF A: I still don’t understand. With your attitudes, why do you two keep living?

HARVEY: Hey, if you’re suggesting I drop dead, forget it. It’d make too many people happy.

EDNA: There are things in life to look forward to, you know. Special things, things that make life worth living.

PROF A: Name three.

EDNA: Well . . . every Thursday the paper has double discount coupons…And on weekends, I get to sleep in late . . . Oh, and about every six months somebody’ll say “thank you” like they really mean it.

PROF A: Don’t you think those are rather trivial things?

HARVEY: I don’t think you guys realize how hard it is being a human being.

STUDENT: You’re missing the point! I didn’t create the human being so that each one would work perfectly. I created the human being so that humanity as a whole would work perfectly.

DEAN: Thank you. We’ve decided your grade. There is much that is commendable about your project, both in Earth’s evolutionary ability and its astonishing variety of beauty. The human being is wondrous and fascinating.

Nevertheless – the human being’s design is tragically flawed. I’m afraid we’re going to have to give you a C plus.

STUDENT: C Plus?!!!

DEAN: I’m sorry. The grade is final.

PROF A: (To the Student:) You want my advice? Next time, don’t design them in your own image. It’s very narcissistic. (Exits)

DEAN: (To the Student:) Now don’t be too hard on yourself. You did your best.

STUDENT: That makes it even more depressing.

DEAN: It’s only a universe. It’ll pass. (Exits.) (The Student starts to clean up.)

EDNA: Sorry if we blew your grade.

STUDENT: It’s my fault. I never should have goofed off on the seventh day.

EDNA: Well, if it means anything, we are glad you created us.

HARVEY: I mean, I think we’re completely messed up; but I’m glad we’re here.

STUDENT: Thanks. I better have you teleported back to Earth.

HARVEY: Oh, yea, well, sure.

EDNA: By the way, if there is such a thing as reincarnation –

HARVEY: Could you bring me back as an Eagle? Just once I’d like to fly real high on my own power, real high, so I could look down and get a clear view of the whole shebang.

STUDENT: That’s a very nice desire Harvey.

HARVEY: Yeah well, I got my moments.

STUDENT: Shall we go? . . . After you.

(Harvey and Edna exit. The Student is about to go, but then he turns around and picks up the globe.<possibly giving it one last spin.>)

STUDENT: (Shrugs to himself:) I think it’s good. (The Student sighs, puts the globe under his arm, and exits. The lights fade.)
```

---

## IC-1226: The Witches

- Title: The Witches
- Author (byline): Roald Dahl
- Work: Not specified
- Publisher: Puffin Books
- Publication date as stated: June 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CHILD, GRANDMOTHER, MOTHER, SISTER, GRANDMA, FATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1427
- Already set (do not supply): none

### Source block (context only)

```text
Author: Roald Dahl
ISBN: 978-0374384579
Publisher: Puffin Books
Date (Month/Year): June 1998
```

### Introduction (context only: never use it for content warnings)

```text
You see, according to Grandmother, a REAL WITCH gets the same pleasure from squelching a child as you get from eating a plateful of strawberries and cream. They plot to do away with one child a week.

(In a witchy voice) “One Child a Week is 52 a year . . . Squish them and squiggle them and make them disappear.”

That is the motto of all witches. And I know this because my Grandma taught me about . . . The Witches by Roald Dahl
```

### Performance text (classify this)

```text
CHILD: (to audience) I had two separate encounters with witches before I was eight years old. From the first I escaped unharmed, but on the second occasion I was not so lucky. The fact that I am still here and able to speak to you is due entirely to my wonderful grandmother.

GRANDMOTHER: (My Grandmother) My darling, you won't last long in this world if you don't know how to spot a witch when you see one. You must remember everything I tell you. After that, all you can do is cross your heart and hope for the best. I have known no less than five children who have simply vanished off the face of this earth, never to be seen again. The witches took them. The first child I knew who disappeared was called Ranghild Hansen. Ranghild was about eight at the time and was playing with her little sister on the lawn. Their mother, who was baking bread in the kitchen, came outside for a breath of air.

MOTHER: Where's Ranghild?

SISTER: She went away with the tall lady in white gloves. She took Ranghild by the hand and led her away.

GRANDMA: No one ever saw Ranghild again.

CHILD: What happened to the other four children?

GRANDMA: The second one was very peculiar. There was a family called Christiansen and they had an old oil-painting in the living-room. There were no people in the painting, just a flock of ducks on a grassy farmyard and a farmhouse in the background. Well, one day their daughter Solveg came home from school eating an apple. She said a nice lady had given it to her on the street. The next morning little Solveg was not in her bed. The parents searched everywhere but they couldn't find her. Then all of a sudden, her father shouted . . .

FATHER: There she is! That's Solveg feeding the ducks!

GRANDMA: He was pointing at the oil-painting. Solveg was standing in the farmyard throwing bread to the ducks. She was just a picture painted on the canvas.

CHILD: Did you ever see that painting, Grandmamma, with the little girl in it?

GRANDMA: Many times. And the peculiar thing was that little Solveg kept changing her position in the picture. One day she would be inside the farmhouse, and you could see her face looking out of the window. Another day she would be far over to the left with a duck in her arms. And what was most odd of all was that as the years went by; she kept growing older. In ten years, the small girl had become a young woman. In thirty years, she was middle-aged. Then all at once, fifty-four years after it all happened, she disappeared from the picture altogether.

CHILD: You mean she died? . . . (gulps and gathers the courage to hear another) What happened to the third one?"

GRANDMA: The third one was little Birgit Svenson. One day she started growing feathers all over her body. Within a month, she had turned into a large white chicken. Her parents kept her for years in a pen in the garden. She even laid eggs.

CHILD: What happened to the fourth child?

GRANDMA: The fourth was a boy called Harald. One morning his skin went all greyish-yellow. Then it became hard and crackly, like the shell of a nut. By evening, the boy had turned to stone. I'll take you to see him if you like. He stands in the hall, a little stone statue. Visitors lean their umbrellas up against him.

CHILD: (to audience) Although I was very young, I was not prepared to believe everything my grandmother told me. And yet she spoke with such conviction and with never a smile on her face or a twinkle in her eye, that I found myself beginning to wonder. (to Grandma) Go on, Grandmamma. You told me there were five.

GRANDMA: Number five was rather an interesting case. A nine-year-old boy called Leif was summer-holidaying with his family on one of those little islands. Young Leif dived into the water and his father noticed that he stayed under an unusually long time. When he came to the surface at last, he wasn't Leif anymore. He was a porpoise.

CHILD: He wasn't! He couldn't have been!

GRANDMA: Absolutely. I knew his mother well. She told me how Leif the Porpoise stayed with them all that afternoon giving his brothers and sisters rides on his back. They had a wonderful time. Then he waved a flipper at them and swam away, never to be seen again.

CHILD: But wasn't there a most tremendous fuss when this happened?

GRANDMA: Not much. You must remember here in Norway we are used to that sort of thing. There are witches everywhere. There's probably one living in our street this very moment. It's time you went to bed.

CHILD: A witch wouldn't come in through my window in the night, would she?

GRANDMA: No, a witch will never do silly things like climbing up drainpipes or breaking into people's houses. (How to Recognize a Witch) But tonight, I am going to tell you how to recognize a witch when you see one.

CHILD: Can you always be sure?

GRANDMA: No, you can't. And that's the trouble. In the first place, a REAL WITCH is certain always to be wearing gloves when you meet her. Do you want to know why . . . because she doesn't have fingernails. Instead of fingernails, she has claws, like a cat, and she wears the gloves to hide them. Mind you, lots of very respectable women wear gloves, so this doesn't help you very much.

CHILD: (with great fear) Mamma used to wear gloves.

GRANDMA: The second thing to remember is that a REAL WITCH is always bald.

CHILD: Bald!

GRANDMA: Bald as a boiled egg

CHILD: (to audience) I was shocked. There was something indecent about a bald woman. (to Grandma with bravado) If she's bald, she'll be easy to spot.

GRANDMA: Not at all, A REAL WITCH always wears a first-class wig. And it is almost impossible to tell a first-class wig from ordinary hair unless you give it a pull to see if it comes off.

CHILD: What other things must I look for to recognize a witch?

GRANDMA: Look for the nose-holes. Witches have larger nose-holes than ordinary people. A REAL WITCH has the most amazing powers of smell. She can actually smell out a child who is standing on the other side of the street on a pitch-black night.

CHILD: She couldn't smell me. I've just had a bath.

GRANDMA: A clean child gives off the most ghastly stench to a witch. The dirtier you are, the less you smell. The smell that drives a witch mad actually comes oozing out of your skin in waves. Stink-waves the witches call them, go floating through the air and hit the witch smack in her nostrils. They send her reeling. When you haven't washed for a week and your skin is all covered with dirt, then the stink-waves cannot come oozing out nearly so strongly.

CHILD: I shall never have a bath again! Tell me what else to look for in a witch.

GRANDMA: The eyes. The eyes of a REAL WITCH are different from yours and mine. Look in the middle of each eye where there is normally a little black dot. If she is a witch, the black dot will keep changing colour, and you will see fire and you will see ice dancing right in the very centre of the coloured dot. It will send shivers running all over your skin.

CHILD: (to audience) My grandmother leant back in her chair and I stared at her, fascinated. She was not smiling. She looked deadly serious. (to Grandma) Are there other things?

GRANDMA: Of course. You don’t seem to understand that witches are not actually women at all. They look like, talk like and are able to act like women. But in fact they are demons in human shape. You can never be sure whether a woman is a witch or not just by looking at her. But if she is wearing the gloves, has the large nose-holes, queer eyes and hair that looks as though it might be a wig -- then you run like mad.

CHILD: Grandmamma, when you were a little girl, did you ever meet a witch?

GRANDMA: I'm not going to tell you. It would frighten you out of your skin and give you bad dreams. Certain things are too horrible to talk about.

CHILD: Does it have something to do with your missing thumb? (to audience) Suddenly, her old, wrinkled lips shut tight as a pair of tongs and the hand which had no thumb on it began to quiver very slightly. She didn't look at me. She didn't speak. She didn't move . . . It must have been something absolutely appalling and gruesome.
```

---

## IC-1227: The Wizard of Oz: The Screenplay

- Title: The Wizard of Oz: The Screenplay
- Author (byline): Noel Langley, Florence Ryerson and Edgar Allan Woolf
- Work: Not specified
- Publisher: OSP Publishing, Inc.
- Publication date as stated: Jan 1994
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: DOROTHY, GLINDA, WITCH, VOICE, SCARECROW, TIN MAN, LAP DISSOLVE TO, LION, OZ'S VOICE
- Teaser before the introduction: No
- Spoken words (computed): 2534
- Already set (do not supply): none

### Source block (context only)

```text
Author: Noel Langley, Florence Ryerson and Edgar Allan Woolf
ISBN: 978-1566933018
Publisher: OSP Publishing, Inc.
Date (Month/Year): Jan 1994
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
Tw

I offer for your viewing pleasure today, my rendition of The Wizard of Oz in less than ten minutes! No, seriously . . . I can do it! I had to leave out a few parts . . . like . . . The munchkins

(all those little buggers do is sing!), the poppy field (who wants to watch us sleep?). . . . the flying monkeys (we can flap, but certainly can’t fly) and I had to cut down the Wizard’s long-winded speech toward the end (let’s face it . . . he talked forever!). So . . . . We start our adventure just after Dorothy and Toto make a crash landing in Oz, compliments of Tornado Alley in Kansas! The Wizard of Oz: The Screenplay by Noel Langley, Florence Ryerson and Edgar Allan Woolf.

DOROTHY: (exits her farmhouse, looking around with an expression of delighted amazement.) Toto, I've a feeling we're not in Kansas anymore ... We must be over the rainbow! Suddenly a large, pink-tinted crystal BUBBLE approaches. The WITCH OF THE NORTH APPEARS from the bubble. (astounded . . . to TOTO) Now I - I know we're not in Kansas.

GLINDA: (comes gracefully forward.) Are you a good witch - or a bad witch? DOROTHY is so sure GLINDA can't be addressing her that she looks around behind her.

DOROTHY: (turning back) Who, me? Why - I'm not a witch at all. I'm Dorothy Gale from Kansas.

GLINDA: (puzzled) Well, I'm a little muddled - the Munchkins called me because a new witch has just dropped a house on the Wicked Witch of the East – and there’s the house – and here you are – and that’s all that’s left of the Wicked Witch of the East. (Glinda points to two ruby slippers attached to the crushed legs of the WW of the E) And so: Are you a good witch or a bad witch?

DOROTHY: Oh, but I’ve already told you, I’m not a witch at all – witches are old and ugly.

GLINDA: (smiling) I am a witch. I’m Glinda, the Witch of the North.

DOROTHY: You are? (curtsies) Oh, I beg your pardon! But I’ve never heard of a beautiful witch before!

GLINDA: Only bad witches are ugly. (there is a terrific EXPLOSION, leaving the WITCH OF THE WEST. DOROTHY Terrified, hugs TOTO close to her. THE WICKED WITCH walks over to the farmhouse to look at the WICKED WITCH OF THE EAST.

DOROTHY: (in alarm and bewilderment) I thought you said she was dead!

GLINDA: That was her sister, the Wicked Witch of the East. This is the wicked Witch of the West. And she's worse than the other one was.

WITCH: (turning to Glinda and Dorothy) Who killed my sister? Who killed the Witch of the East? (to DOROTHY) Was it you?

DOROTHY: (fearfully) No, No! It was an accident - I didn't mean to kill anybody!

GLINDA: (quickly) Aren't you forgetting the ruby slippers?

WITCH: The slippers - yes, the slippers! (She hurries to the house and is just about to snatch up the slippers when they vanish from under her hands and the feet shrivel up under the house.) They're gone! The ruby slippers - what have you done with them? Give them back to me or I'll - (turning back to GLINDA)

GLINDA: It's too late! (She points her wand at DOROTHY's feet) There they are, and there they'll stay!

WITCH: (to both GLINDA and DOROTHY, in a frenzy) Give me back my slippers! I'm the only one that knows how to use them - they're of no use to you!

GLINDA: (to DOROTHY) Keep tight inside of them - their magic must be very powerful, or she wouldn't want them so badly! (laughs) (to WW of W) You have no power here! Be gone before somebody drops a house on you, too!

WITCH: (falling back as she looks up) Very well - I'll bide my time - (to DOROTHY) - but I'll get you, my pretty, and your little dog, too - (with a burst of laughter, she whirls around and vanishes in a burst of smoke and fire and a clap of thunder.

GLINDA: (to DOROTHY) I'm afraid you've made rather a bad enemy of the Wicked Witch of the West. The sooner you get out of Oz altogether, the safer you'll sleep, my dear.

DOROTHY: Oh, I'd give anything to get out of Oz altogether; but which is the way back to Kansas? I can't go the way I came -

GLINDA: No, that's true. The only person who might know would be the great and wonderful Wizard of Oz himself. He lives in the Emerald City. (kisses her on forehead) All you do is follow the Yellow Brick Road. (pointing with wand)

(She steps back, and the large pink-tinted crystal BUBBLE reappears. The bubble slowly rises, carrying GLIDA away) DOROTHY skips down the Yellow Brick Road. She stops as the Yellow Brick Road crosses another one. She looks up and down, puzzled.

DOROTHY: Follow the Yellow Brick Road, follow the Yellow - Now which way do we go?

VOICE: Pardon me. That way is a very nice way. He is hanging awkwardly on the pole, with his arm pointing to the right down the road.

DOROTHY: Who said that? She looks around for the voice. TOTO barks at the SCARECROW. Don't be silly, Toto. Scarecrows don't talk.

SCARECROW: (pointing to the left) It's pleasant down that way too.

DOROTHY: Why, you did say something, didn't you? The SCARECROW shakes his head, then stops and nods it instead. Are you doing that on purpose - or can't you make up your mind?

SCARECROW: That's the trouble. I can't make up my mind. I haven't got a brain - only straw. (showing her)

DOROTHY: How can you talk if you haven't got a brain?

SCARECROW: I don't know. But some people without brains do an awful lot of talking.

DOROTHY: (speculatively) Yes - I guess you're right. (impressed by such a truth) Well, we haven't really met properly, have we? (curtsying) How do you do?

SCARECROW: Oh, I'm not feeling at all well. You see, it's very tedious being stuck up here all day long with a pole up your back.

DOROTHY: Oh, dear! That must be terribly uncomfortable. Well, here - let me help you! (puzzled - as she works) Well, oh, dear - I don't quite see how I can - (bending down the nail) Oh yes!

SCARECROW: (as he slips off to the ground) Ohhh! (As he lands, his coat bursts open, and straw falls out from his abdomen.) Whoops! (laughs) There goes some of me again!

(He stuffs the straw back into is coat. He gets up and stretches himself luxuriously) My! It's good to be free! (He whirls around and promptly falls over a broken fence rail)

DOROTHY: Oh! (screams) Ohhh! Oh!

SCARECROW: (sitting up with a hopeful smile) Did I scare you?

DOROTHY: No, no. I – I just thought you hurt yourself.

SCARECROW: But I didn't scare you . . . ? (dolefully) I didn’t think so. (A crow lights on his shoulder at this moment) Boo! Scat! Boo! (The crow picks a piece of straw and flies off with it.) (To Dorothy) You see, I can't even scare a crow! (almost weeps) Oh, I’m a failure, because I haven’t got a brain.

DOROTHY: Well, what would you do with a brain if you had one?

SCARECROW: Do? Why if I had a brain I could – (goes into his song and amusing dance)
I could while away the hours
Conferrin’ with the flowers
Consultin’ with the rain
Any my head, I’d be scratchin’
While my thoughts were busy hatchin’
If I only had a brain. - Whoa!
At the finish, he falls to the road. DOROTHY picks up some of his straw and rushes over to him
to stuff it back in again.

DOROTHY: Wonderful! (shaking his hand) Why, if our scarecrow back in Kansas could do that, the crows'd be scared to pieces!

SCARECROW: Where's Kansas?

DOROTHY: That's where I live. And I want to get back there so badly, I'm going all the way to Emerald City to get the Wizard of Oz to help me.

SCARECROW: (with a sudden idea) Do you think if I went with you, this Wizard would give me some brains? (pleading) Uh . . . won't you take me with you?

DOROTHY: (warmly) Why, of course, I will!

SCARECROW: (leaping into the air) Hooray! We're off to see a Wizard! (they continue down the Yellow Brick Road, arm in arm) The two continue down the Yellow Brick Road until they come to the TIN MAN'S LITTLE COTTAGE – Dorothy takes a break to gather up some apples and falls on her hands and knees to pick one up. She sees a tin foot just beside it. She raps on it and then looks up, and sees the TIN MAN. She scrambles to her feet, examining him.

DOROTHY: (raps on him) Why, it's a man! A man made out of tin! (she raps on his chest) A creaky, rusty sound comes from the TIN MAN.

TIN MAN: (almost inaudibly) Oil can! Oil can!

DOROTHY: He said oil can! Oil can? Oh! Oh! (finding oil can) Here it is! Where do you want to be oiled first?

TIN MAN: My mouth . . . my mouth! DOROTHY sends a drop or tow by the TIN MAN's mouth (clearing s throat, as his joints squeak) M - m - my, my, my, my, my, my goodness! I can talk again! Oh, oil my arms, please! Oil my elbows! Oh! Oh!

DOROTHY: (she starts working on his arm joints) Here. (Lowering his ax) Goodness! How did you ever get like this?

TIN MAN: Oh, well, 'bout a year ago, I was chopping that tree, when suddenly it began to rain. And right in the middle of a chop, I - I rusted solid. I've been that way ever since. Oh. As he talks, DOROTHY is working his joints.

DOROTHY: Well, you're perfect now.

TIN MAN: Perfect? Oh, bang on my chest if you think I'm perfect. Go ahead - bang on it! DOROTHY raps on his chest, which echoes. It's empty. (He looks around, then lowers his voice as telling a terrible secret.) The tinsmith forgot to give me a heart. All hollow! (He bangs on his chest and knocks himself against a tree stump. Dorothy goes to help him, but he holds her off) (singing)

When a man's an empty kettle
He should be on his mettle
And yet, I’m torn apart
Just because I'm presumin'
That I could be kind-a human
If I only had a heart.
He goes into a dance. Just as he finishes, the TIN MAN’s joints lock, and DOROTHY comes over
to help. The TIN MAN staggers back and lands on a tree stump).

DOROTHY: . . . oh, oh, oh, are you all right?

TIN MAN: I’m afraid I’m a little rusty yet. Oh!

DOROTHY: Oh, dear. That was wonderful! You know, we were just wondering why you couldn’t come with us to the Emerald City to ask the Wizard of Oz for a heart!

TIN MAN: Well, suppose the Wizard wouldn’t give me one when we got there?

DOROTHY: Oh, but he will (in distress) He must! We’ve come such a long way already -

SCARECROW: (offering his arm to DOROTHY) To Oz!

TIN MAN: (offering his arm to her) To Oz!

LAP DISSOLVE TO: LONG SHOT – DARK AND EERIE FOREST The comrades are coming along the Yellow Brick Road. They move forward slowly and stop.

DOROTHY: Oh, I don't like this forest! It's - it's dark and creepy! Do - do you suppose we'll meet any wild animals?

TIN MAN: Mmm – we might. Mostly lions and tigers and bears.

DOROTHY: Oh my! A roar from ahead of them. LONG SHOT - COWARDLY LION in the distance roars. He advances; Dorothy retreats. He leaps in the air and comes down on all fours. He straightens up in a boxer's stance and then waltzes menacingly, doing some very fancy shadow boxing.

LION: (growling) Hah, put 'em up, put 'em up! Which one of ya is first? I'll fight ya both together if ya want. I'll fight ya with one paw tied behind my back. (puts paw behind back) I'll fight ya standin' on one foot! (stands on one foot) I'll fight ya with my eyes closed. (closes his eyes, then opens them - to TIN MAN) Ohhhh - pull in' an ax on me, eh? (to SCARECROW) Sneakin' up on me, eh? Why . . . (growls) CLOSE SHOT - TOTO barking I'll get you anyway, peewee! (qrowls) (TOTO jumps into the bushes with the LION growling after him. DOROTHY grabs TOTO in her arms. She slaps the LION smartly on the nose.)

DOROTHY: Shame on you -

LION: (bawling) What did ya do that for? I didn't bite him -

DOROTHY: No, but you tried to!

LION: (sniffing pathetically) Well, ya didn't have to go and hit me, did ya? (sobbing)

DOROTHY: (severely) My goodness, what a fuss you're making - why, you're nothing but a great big coward!

LION: (to DOROTHY, with great self-pity, playing with his tail) You're right, I am a coward! I haven't any courage at all! I even scare myself.

DOROTHY: Why don't you come along with us? We're on our way to see the Wizard now. I'm sure he could give you some courage -

LION: (still sniffling) Gee, that - that's awfully nice of ya. My life has been simply
unbearable. (emotionally as they walk) It - It's been in me so long, I just gotta tell
ya how I feel. (singing)
If I were King of the Forest,
Not Queen, not Duke, not Prince.
My regal robes of the forest
would be satin, not cotton, not chintz.
I'd commend each thing, be it fish or fowl,
With a woof and a woof, and a royal growl – woof. Dorothy bows

DOROTHY: Your Majesty, if you were King. You wouldn’t be afraid of anything? Supposin’ you met an elephant!

LION: I’d wrap him up in cellophant. How? . . . . Courage! What makes a king out of a slave! . . . Courage! What makes the flag on the mast to wave! . . . Courage! What makes the elephant charge his tusk in the misty mist or the dusky dusk? What makes the muskrat guard his musk? . . . Courage! What have they got that I ain't got?

ALL (DOROTHY): Courage!

LION: You can say that again! Ha, ha - huh? TRANSITION

Blah, blah, blah . . . sleeping in the poppy field . . . blah, blah, blah . . . And then the quartet of adventurers arrive in Oz and are granted an audience with the Wizard.

(Actor 2 plays Oz’s Voice and should be positioned facing the back of the room directly behind Dorothy, who faces judge)

OZ'S VOICE: I am Oz, the Great and Powerful! Who are you? Who are you?

DOROTHY: I - if you please, I am Dorothy, the Small and Meek. We've come to ask you -

OZ'S VOICE: (booming forth and interrupting) SILENCE! The Great and powerful Oz knows why you have come! Tin Man! You dare to come to me for a heart - do you? You clinking, clanking, collection of junk! And you, Scarecrow, have the effrontery to ask for a brain? You billowing bale of bovine fodder! And you, Lion!

(Actor 2 steps out to play the part of the Lion) The LION groans with fear as he is slowly pushed forward. CLOSE ON LION He begins to speak and faints dead away. (Actor 2 resumes position as Wizard)

DOROTHY: DOROTHY straightens up from LION and turns on WIZARD. (angrily) Oh - oh! You ought to be ashamed of yourself! Frightening him like that, when he came to you for help!

OZ'S VOICE: Silence, whippersnapper! The beneficent Oz has every intention of granting your requests! But first you must prove yourselves worthy by performing a very small task. Bring me the broomstick of the Witch of the West! Now go!

TRANSITION

Piece of cake right? Well, the Wicked Witch had the band of Flying Monkeys, see, who captured Dorothy and Toto, shredded the Scarecrow, beat some major dents into the Tin Man and scared the Lion so bad he wet himself. But through sheer perseverance, loyalty and commitment, the friends make their way to the Witch’s castle to rescue Dorothy. Success! Almost . . . on the way out of the fortress, their great escape goes a bit south!

WITCH: (laughing) Well! Ring-around-the-rosy! A pocketful of spears! Thought you'd be pretty foxy, didn't cha? Well, the last to go will see the first three go before her . . She grins and looks up, then lifts her broom to a burning torch on the wall. How about a little fire, Scarecrow! The WITCH thrusts the blazing broom at the SCARECROW. It sets his arm on fire.

SCARECROW: (jumping up and down) Oh! No! No! (DOROTHY screams) Help! I'm burning! I'm burning! I’m burning. Help! Help! Help! Help! (In defense of the SCARECROW, DOROTHY looks around and suddenly sees a bucket of water.).

WITCH: (screaming) Don't touch that water! DOROTHY flings its contents toward the SCARECROW. The water hits her full in the face and puts out the fire. She screams in agony as she shrinks and shrivels.) Ohhh! You cursed brat! Look what you've done! I'm melting! Melting! You destroy(ed) my beautiful wickedness! Ohhhh – ohhhhhh - ohhhh!

DOROTHY: (looking around at the Witch’s minions, the WINKIES) I didn't mean to kill her - really I didn't . . . it's . . . it's just that he was on fire! (to the leader of the WINKIES) The broom! May we have it? (Accepts the broomstick) TRANSITION

And so the band of battle-weary travelers make their way back to the chamber of the Great Oz, who they discover is really a very good man, but a very bad wizard. From a large, black magician’s back, he presents the Scarecrow with a diploma in honor of his brains, a ticking heart-shaped clock for the Tin Man as a symbol of his humanity and he awards the Lion a Triple-Cross Medal for his courage. But for Dorothy . . . who only wants to go home . . .

DOROTHY: (Sadly) I don’t think there’s anything in that black bag for me.

SCARECROW: (pointing) Look! Here's someone who can help you! The WITCH OF THE NORTH’S BUBBLE comes to rest and fades. GLINDA approaches, waving her wand.

DOROTHY: (curtsying) Oh, will you help me? Can you help me?

GLINDA: You don't need to be helped any longer. You've always had the power to go back to Kansas. [You] wouldn't have believed me. [You] had to learn it for [yourself].

TIN MAN: What have you learned, Dorothy?

DOROTHY: (thoughtfully) Well, I . . . I think it's that if I ever go looking for my heart' s desire again, I won't look any further than my own backyard; because if it isn't there, I never really lost it to begin with! (timidly to GLINDA) Is that right?

GLINDA: (nodding and smiling) That's all it is. Now those magic slippers will take you home in two seconds! Are you ready now?

DOROTHY: Yes, I'm ready now.

GLINDA: Then close your eyes and tap your heels together three times . . . . . . and think to yourself, “There’s no place like home; there’s no place like home; there’s no . . . “

DOROTHY: (DOROTHY speaks with her eyes closed while clicking her heels) “ . . . there's no place like home; there's no place like home . . . there's no place like home; there's no place like home . . . “
```

---

## IC-1228: The Wolf Who Cried Boy

- Title: The Wolf Who Cried Boy
- Author (byline): Bob Hartman
- Work: Not specified
- Publisher: Puffin Books
- Publication date as stated: June 2004
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, LITTLE WOLF, FATHER WOLF, MOTHER WOLF, BOY
- Teaser before the introduction: Yes
- Spoken words (computed): 992
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bob Hartman
ISBN: 978-0142401590
Publisher: Puffin Books
Date (Month/Year): June 2004
```

### Introduction (context only: never use it for content warnings)

```text
Poop . . . it looks like fluffy poop! . . . You really can’t blame the little guy! Gross!

But that’s beside the point. You’ve all heard the story of The Boy Who Cried Wolf . . . today I’m here to flip that story on its head. This is the story of . . . . The Wolf Who Cried Boy by Bob Hartman
```

### Performance text (classify this)

```text
NARRATOR: Once upon a time there lived a family of wolves. They stole sheep, ran after rabbits and dined on ducklings and deer. Except for Little Wolf, that is, who never stopped complaining about what his mother prepared each night for dinner.

LITTLE WOLF: (whining) Lamburgers again! I hate Lamburgers! (howling) Minced mole-roles? We had minced mole-roles last night! (whimpering) Chocolate moose? Chocolate moose makes me sick! And besides, it looks just like . . .

FATHER WOLF: (barking) That’s enough!

LITTLE WOLF: Boy! Why can’t we have boy tonight? We never have boy anymore!

FATHER WOLF: (sighing) Well, son, there was a time when a clever wolf could snatch a shepherd boy off a hill or pluck a farm boy out of a field. Why, there was nothing better than a steaming plate of “boy” chops, (Mmmm) a big baked boy-tato (Mmmm) and some “Boys-N-Berry” pie (Mmmmm). But boys are hard to come by these days, in fact, they’re rare. So stop your complaining and finish off that moose.

LITTLE WOLF: (muttering) Yes, father. But suppose . . . suppose I did find a boy someday?

FATHER WOLF: (smiling) You find a boy out there in the woods and your mother and I would be happy catch him and cook him for you. But I wouldn’t get my hopes up if I were you. Like I said, boys are rare.

NARRATOR: So, the next day as Little Wolf made his way home from school, he sniffed the air. (Sniff) Three pig salad? (moaning) I hate three pig salad! And then Little Wolf remembered what his father had told him about catching a boy some day. So he decided to play a little trick and he put off that awful dinner for a while. He ran home just as fast as he could, howling all the way.

LITTLE WOLF: (howling) Boy! Boy! I’ve just seen a boy in the woods! If we hurry, we can catch him!

NARRATOR: Father and Mother Wolf raced out of the cave. They ran through the woods to the top of the hill and all the way down to the creek. They peered into trees and sniffed behind rocks and looked into every hollow log. But they could not find the boy.

FATHER WOLF: (panting) We looked everywhere – everywhere a boy might go, but we just couldn’t find him. Better luck next time, son.

NARRATOR: Little Wolf tried to look disappointed, but it was all he could do to keep from laughing. The joke got even better when his mother announced:

MOTHER WOLF: Oh, no. The three pig salad is ruined. The bricks are limp. The straw is damp and the sticks have all turned, well . . . “sticky.”

FATHER WOLF: Don’t worry, dear. We can make due with snack food tonight.

NARRATOR: And so they crunched on chipmunks and dip and Little Wolf was happy. So happy, in fact, that he decided to try the same trick the very next day.

LITTLE WOLF: It’s the boy! I saw him again. He’s just at the edge of the woods!

NARRATOR: So once again Father and Mother Wolf went racing after the boy. Once again, they came dragging home, their paws empty and once again, their dinner was ruined.

MOTHER WOLF: (sighing) Just look at that Granny Smith Pie. The apples are entirely too mushy.

FATHER WOLF: Yup. And Granny’s gone all crusty and hard.

LITTLE WOLF: (shrugging) Looks like snacks again tonight!

NARRATOR: But the smile on his face made Father Wolf wonder. And then he heard his son a little later on the phone.

LITTLE WOLF: (whispering) That’s right. I didn’t have to eat dinner tonight either. I think I’ll tell them there’s a boy out there tomorrow too!

NARRATOR: Father Wolf upon hearing this went straight to Mother Wolf and they agreed that on the following night they would ignore his silly tricks. So . . . the next day Little Wolf made his way from home from school as usual. He could smell the awful odor of the steaming musk-ratatouille as it floated out of the cave. And he was just about to holler “boy” when the most amazing thing happened. There walking through the woods before him were more boys . . . more boys than he had ever seen. A Boy Scout troup!

LITTLE WOLF; (howling) Boy! B-b-b-boys!

NARRATOR: But no one came running from the cave.

LITTLE WOLF: (howling) Boys! B-b-boys!

NARRATOR: But still no one came, so he ran into the cave shouting:

LITTLE WOLF: There are boys out there! Mom! Dad! Dozens of them. Big ones and little ones; fat ones and skinny ones. Enough to fill our freezer! And Auntie’s freezer too!

NARRATOR: But his mother just shrugged and said:

MOTHER WOLF: That’s very nice, dear. But I already have our supper planned.

NARRATOR: Father Wolf hid his face behind the newspaper. And that’s when one of the boys stuck his head – he actually stuck his head – in the cave. He was the mischievous type. A lot like Little Wolf, in fact. And he’d crept away from his scout pack to have a closer look.

LITTLE WOLF: (shouting) See! There’s one of them now!

NARRATOR: But even though the boy tip-toed right into the cave. Little Wolf couldn’t get anyone to look.

LITTLE WOLF: (howling) There’s a boy on the couch! C- c- c- couch!

MOTHER WOLF: That’s enough now, son.

FATHER WOLF: You’re not fooling us again! We’re onto your little tricks.

LITTLE WOLF: (pleading) But I’m not lying this time. Honest! There really is a boy! Right here in our cave!

NARRATOR: The boy glanced at his watch and then turned to leave.

BOY: [put hands to ears, wiggle fingers, stick out tongue and give Little Wolf a raspberry

(Pbbbtttttt).]

LITTLE WOLF: (begging) Please, look! Look! He’s getting away!

NARRATOR: By the time Father Wolf finally stuck his head above the paper, the boy was gone.

LITTLE WOLF: (crying) You waited too long! He was here a minute ago. All we have to do is run outside. But you won’t.

FATHER WOLF: (growling) We will do no such thing! From now on you’ll eat your dinner without complaining.

MOTHER WOLF: And you will stop fibbing, once and for all. Do you understand, Little Wolf?

LITTLE WOLF: (sighing) Yes.

NARRATOR: So from then on, Little Wolf ate lamburgers and three pig salad and he even grew fond of Granny Smith pie. And he never, ever, cried “boy” again. And that’s why the boys, at least, lived happily ever after.
```

---

## IC-1229: The World According to Toddlers

- Title: The World According to Toddlers
- Author (byline): Shannon Payette Seip and Adrienne Hedger
- Work: Not specified
- Publisher: Andrews McMeel Publishing
- Publication date as stated: 978-1449401207
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, TODDLER, JUDY, CHUCK, MOM, TODDLER 2, KATIE, MAGIC EIGHT BALL
- Teaser before the introduction: Yes
- Spoken words (computed): 847
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shannon Payette Seip and Adrienne Hedger
ISBN: Mar 2011
Publisher: Andrews McMeel Publishing
Date (Month/Year): 978-1449401207
```

### Introduction (context only: never use it for content warnings)

```text
Welcome to the World According to Toddlers. A hilarious, messy (is hit in the face with a spoonful of something; wipes it off) and unpredictable universe.

The best way to navigate the toddler world? Nobody really knows . . . everyone just makes it up as they go along. It’s a world where the human who believes he is the boss of you only comes up to your knee. A world where food must be cut just so. A world where throwing a spectacular tantrum is on the daily “TO DO” list (off-stage scream) Check!

The World According to Toddlers by Shannon Payette Seip and Adrienne Hedger
```

### Performance text (classify this)

```text
NARRATOR: (Pg vii – viii) (cradling an infant in her arms) In the beginning they are babies. Cue the soft music – (sings) Lullaby and goodnight . . . So cuddly. So sweet. Eating enthusiastically. Playing happily. Wearing the outfits you choose. Life is good! Then, around 18 months, the world starts to change. (off-stage shriek– she wrestles with baby as it morphs into a toddler, finally lets it go)

TODDLER: (cross arms and says emphatically) No! No! No! No!

NARRATOR: This is when you realize: Your baby is gone and in its place is a boisterous, opinionated human: Your toddler. NO!

*****A Major Upset*****

NARRATOR: (Pg 8-9) It’s a major upset – a tantrum is brewing. Let’s cut to our commentators, Chuck and Judy, who are live on the scene to give us a play-by-play report

JUDY: Chuck, I sense Toddler is growing dissatisfied.

CHUCK: Well, look at those shoes Mom is asking her to wear. Tennis shoes with Velcro? That’s outrageous!

JUDY: I think we’re about to witness a full-blown tantrum. Let’s watch the technique

TODDLER: (crying interspersed with “No, no, no” and stomping feet)

JUDY: She’s yelling something . . . I can’t quite make it out.

CHUCK: Well, we can hear the word “no” for sure.

JUDY: She’s making a move to throw herself to the ground. Wait . . . she’s holding back on the sobbing while she concentrates on lowering herself to the ground . . . carefully.

CHUCK: The sobbing resumes, Judy! Watch that arm and leg movement. Impressive.

JUDY: Even more powerful than before.

TODDLER: (full-blown tantrum mode – kicking and flailing)

JUDY: Chuck, everything is infuriating to her now. Even air.

CHUCK: She’s punching the air! I would not want to be that air right now. And listen to that scream!

TODDLER: (manages to get one shoe off and throws it viciously)

JUDY: This kid knows her stuff.

CHUCK: Well, she’s had practice, Judy. Plenty of practice. ****** Snack Time *****

NARRATOR: (Pg 21) A juice box chilled at exactly 37 degrees. Hexagonal wheat crackers, arranged in a fan. Green grapes that are perfectly oblong. No, it’s not a superstar’s dressing room requirements: it’s the high-maintenance demands of a toddler. [It’s] (Pg 34-35) Snack Time!

JUDY: Chuck, Toddler wants a banana.

CHUCK: Mom has the banana in hand. He’s watching for a sign that it’s OK to peel.

TODDLER: (raising arms and opening and closing fists rapidly, with a low-pitched whine)

JUDY: There’s the sign!

CHUCK: Peeling is underway. She needs to keep this slow and controlled so she can stop at exactly the right point.

JUDY: Chuck, if she peels even a centimeter too much, that banana is ruined. I think we all remember what happened last week, when she pulled the granola bar wrapper down too far.

CHUCK: And let’s not forget the incident with the string cheese wrapper.

JUDY: What about the time Dad handed Toddler a naked banana? (Gasp!)

CHUCK: I think we’re getting close . . . close.

MOM: (peeling a banana like she’s diffusing a bomb)

CHUCK: She’s stopping!

TODDLER: (stops screaming suddenly, takes the banana and munches on it)

JUDY: Whew! Right at the perfect point! *****The Social Lives of Toddlers*****

NARRATOR: (Pg 41) Peeing in the sandbox. Though this violation might offend an adult during a social gathering, it’s commonly accepted during a toddler’s playdate. No feelings hurt. No friendships destroyed. Let’s take an inside look at how toddlers play, share (yeah, right!) and enjoy the company of others. Come hope in the sandbox! (pointing) Just watch out for that wet spot. (Pg 54) [It’s just your average] playdate at the park! (Pg 94) Don’t forget your blankie, stuffed giraffe, pacifier, snack, pillow, another snack and your favorite socks! (Pg 100) [But] Understand this: You do not need a stroller. Your mom thinks you still need one, but she is dead wrong!

TODDLER: (wandering in, clutching all these items in her arms)

CHUCK: (Pg 54) Whoa! Judy, I think she’s just going to stand next to that tree, holding her treasured toys.

JUDY: Here comes Toddler’s friend to say hi. Here comes another!

TODDLER 2: (Pg 50) Do you want to play with me?

TODDLER: (turns away violently shaking her head)

CHUCK: (Pg 54-55) She’s got a pretty hostile look on her face. That little head is vehemently shaking no.

JUDY: Mom is encouraging Toddler to play.

CHUCK: She can’t be serious, Judy. Doesn’t she know that those kids will just steal Toddler’s best toys?

JUDY: That’s right, Chuck. The point of bringing your toys to the park is to make sure no one else gets them.

TODDLER: (Pg 67) No, no, no, no!

JUDY: This powerful word is appropriate at any time, in any setting . . .

CHUCK: (Pg 55Yes! Her plan is to hold tight and not move for the entire 90-minute playdate.

JUDY: It’s too risky to even play with your things or other kids might want to play too.

CHUCK: All you can do is show up and guard your stuff.

JUDY: Guard it with your life, Chuck. With your life!

TODDLER: (Pg 66) Mommmmmmmy!

JUDY: Hungry, tired, uncomfortable, or bored? Yelling MOMMY is the remedy! ****** Night Night ******

NARRATOR: (Pg 136-137) Dear Katie, Thank you for babysitting for us tonight. Here are some notes about putting Bobby to bed. Best of luck! Bobby needs to be situated at a 30 degree angle to the door with his yellow blanket (light yellow, not dark yellow) covering him just up to his chest – one-half centimeter lower than his armpits. Now sing the ABC song to him.

KATIE: (singing) A, B, C, D, E, F, G . . .

NARRATOR: In a British accent!

KATIE: A, B, C, D, E, F, G . . .

NARRATOR: When ABC concludes, sing “Twinkle Twinkle Little Star” until he falls asleep or until we get home.

KATIE: (singing) Twinkle Twinkle Little Star

NARRATOR: Thank you! We’ll be home VERY late. (evil, giddy laughter)

TODDLER: (Pg 139) [Dear Magic Eight Ball], I don’t want to sleep and I’m tired of crying it out. Should I throw up? (shakes magic eight ball)

MAGIC EIGHT BALL: Crying takes too much energy; it’s more effective and expedient to throw up. Chances are very good that “night-night time” will be all done.

TODDLER: (smiles evilly)

KATIE: (singing) . . . How I wonder where you are (continues singing through Toddler’s mime)

TODDLER: (throws up) (Pg 17) Gotta go potty! (makes a grimacing face) It’s coming out!

(pooping his pants. A contented sigh, then stuttering) (Pg 62) You know wha. . You know wha. . . You know wha . . . (Pg 20) I DO IT! I DO IT!
```

---

## IC-1230: 1-900-Desperate

- Title: 1-900-Desperate
- Author (byline): Christopher Durang
- Work: 27 Short Plays, Pg 165-170
- Publisher: Smith and Kraus
- Publication date as stated: Feb 1996
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: GRETCHEN, VOICE, RECORDED VOICE, SALLY, ZELDA, LITTLE BOY, SCUZZY
- Teaser before the introduction: Yes
- Spoken words (computed): 1009
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christopher Durang
Book: 27 Short Plays, Pg 165-170
ISBN: 978-1880399897
Publisher: Smith and Kraus
Date (Month/Year): Feb 1996
```

### Introduction (context only: never use it for content warnings)

```text
The 1980s . . . An era before cell phones. (looks shocked) I know, right? Cell phones were called telephones and were actually bolted to a wall with a cord connecting the “base” to the “receiver.” Wow!

It was an era before social media, before texting and before on-line dating. Everyone, I’m told, relied on this so-called telephone to communicate. Welcome to the party line! Oh, that’s a group phone call where people went to meet strangers in the mid-1980s. Think of it as a precursor to the internet chat room. But wait . . . there’s more . . . you had to pay by the minute to participate. By the minute!! Let’s face it. Meeting that special someone never gets any easier.

1-900 Desperate by Christopher Durang
```

### Performance text (classify this)

```text
Scene: Gretchen, a woman in her mid-30s, is on the phone.

GRETCHEN: (Pg 165-170) No, mother, I don't have a date tonight. I know it's Saturday night. Yes, I know my sister Rebecca is married and has children. (Listens.) Well, I'm sorry my life makes you unhappy, mother. I'm very happy here alone in my apartment on Saturday. (Listens some more; holds her head.) Mother, please don't say that about me, you make me feel worthless and desperate. No, I don't want you to lie to me. No, I take that back - I do want you to lie to me. Tell me it's fine that I'm alone on Saturday night, and I'm fine. Say that, mother. Say it. (Listens; it's brief) Thank you, mother, it’s very sweet of you to feel that way. Now I have to go put my frozen dinner in the microwave, so let me get off the phone now. Goodnight. (Grouchy.) Yes, I love you too. (Hangs up.) Oh, thank God, I'm off the phone. (Looks around; disoriented) But what should I do now? Oh, I feel desperate.

VOICE: Feeling desperate? Then call 1-900-DESPERATE. That special someone may just be waiting for you.

VOICE: Call 1-900-DESPERATE. That special someone may just be waiting for you.

GRETCHEN: Oh, Lord, now I'm hearing voices. Oh that's right, the TV is on. I'm not crazy. I'm not crazy. I'm just desperate. (Starts to dial.) 1-900-Desperate. (the sound of ringing, then a click and a recorded voice)

RECORDED VOICE: Hello there, singles. You have reached 1-900-Desperate, where you can meet the man or woman of your dreams. The call costs $1.99 a half minute, $3.98 for a full minute. And there is a $25 minimum for 6 minutes and 28 seconds. If you don't want to be charged, hang up now. (beat) Too late. (Gretchen is taken aback. She might have hung up, but it happened too fast) You didn’t hang up immediately, you might as well listen in on the line, we’re going to charge you whatever you do. Enjoy yourself! (another click)

SALLY: (Having heard the click of Gretchen coming on the line. She is overanxious to make a connection with someone) Hello?

GRETCHEN: (Tentative) Hello? Is this 1-900-Desperate?

SALLY: It sure is. Are you a man with a high voice?

GRETCHEN: No, I'm a woman.

SALLY: Damn it. Are there any men on this line? Hello? Any men out there?

ZELDA: (She seems to be on the line for purposes other than meeting people) We’ve got to stop looking to men to give us meaning.

GRETCHEN: I think she’s right. I have meaning even though I’m home alone on Saturday, thinking of renting a video and using the microwave.

ZELDA: You mean to kill yourself?

GRETCHEN: No. To cook.

LITTLE BOY: Hello?

SALLY: Are you a man?

LITTLE BOY: I'm five years old. My name is Billy.

SALLY: I don't care what your name is, shut up.

GRETCHEN: Please, don't be abusive to a child.

LITTLE BOY: (Calls.) I'm not doing anything, mommy. (To the phone.) Bye! (hangs up)

GRETCHEN: I guess I’d hang up too, but . . . I guess I’ve paid for it.

SALLY: Uh huh. Any men out there? Please God.

ZELDA: Women were once warriors. We hunted like Diana, we carved the turkeys at dinner. We must return to those times.

SALLY: Will you shut up?

ZELDA: You need a woman's support group.

SALLY: I need a man. I don't need women yapping at me. (Lights come up on Scuzzy, a kind of sexy 20-year-old with slicked-back hair and a leather jacket.)

SCUZZY: Hey, ladies, how's it hangin'? You ladies feelin' desperate tonight?

SALLY: Oh my God, a man! Hello! Hello!

ZELDA: Not really. I’m reading the diaries of Anais Nin. She was very spiritual.

SCUZZY: Anyone else out there?

GRETCHEN: Yes. Although I can't stay long. I dialed by mistake.

SCUZZY: Ooooo. A happy mistake for me. What's your name, baby?

GRETCHEN: My name is . . . Gretchen.

SALLY: My name is Sally.

SCUZZY: What you look like, Gretchen?

GRETCHEN: Oh . . . I don't know.

SALLY: I look like a model. I have large breasts and a tiny waist and . . . do you like big or small hips?

SCUZZY: Who is this? I'm talkin' to Gretchen. Hey, Gretchen, talk to Scuzzy again.

GRETCHEN: What kind of name is Scuzzy?

SCUZZY: It's my nickname. You got a nickname?

GRETCHEN: Gretchen. Well, it's not a nickname . . . it's a name.

SALLY: Sometimes I *get excited* just walking down the street. That's the kind of passionate person I am.

SCUZZY: Butt out, butt head. I'm talkin' to Gretchen. Gretchen, you still there?

GRETCHEN: Excuse me. I think I'm going to get off now.

SCUZZY: You want me to call you? You know. On your number. We can have a "better talk" that way.

GRETCHEN: Oh, I don't know, I don't feel I know you properly yet.

SCUZZY: What do you want to know?

GRETCHEN: Oh, gosh. What books do you read?

SCUZZY: Books. I read the TV Guide. (Gretchen reacts non-verbally)

LITTLE BOY: I have a little red wagon.

SCUZZY: Who the hell is that?

SALLY: Oh, I give up. I hate you all! (Sally hangs up)

SCUZZY: (re-focuses) What do you look like, Gretchen?

GRETCHEN: Well, let's see. I'm 5'9", I have brown eyes.

SCUZZY: What are your measurements? Heh, heh, heh.

GRETCHEN: Um . . . my measurements are 36-46-77. I look like a large teepee. And I invite men up to my lair and poison them at dinner and serve their bodies to the raccoons outside my house.

SCUZZY: Oooooh, this lady's intriguing!

ZELDA: Good for you, Gretchen. Feed him to the raccoons.

SCUZZY: We got a nut case on the line. Shut up, nut case! Hey, Gretchen, baby, gimme your number.

GRETCHEN: I'm sorry. I don't think we're right for one another. I'm sorry, Scuzzy. I'm sure you're very nice, for someone.

SCUZZY: Damn right I am. (There is a pause.)

LITTLE BOY: I have a little doggie, and a big doggie.

SCUZZY: Any hot chicks on the line?

ZELDA: (With a glint, does a feminine, girlish voice.) I'm here. Who's this?

SCUZZY: My name is Scuzzy.

ZELDA: Oh, I think I'm gonna like you, Scuzzy. Let me call you.

SCUZZY: Okay. My number's 666-0666.

ZELDA: Ooooh, that's a sexy number. I'll call you right up.

SCUZZY: Okay, baby. (Scuzzy hangs up)

ZELDA: (Regular voice.) Good night, Gretchen. I'm gonna make him suffer. For you and for women everywhere. (Zelda hangs up.)

GRETCHEN: Well, calling this line has been a terrific success.

LITTLE BOY: I have a little red wagon.

GRETCHEN: Do you? That's nice.

LITTLE BOY: My mommy and daddy are asleep in front of the television. I'm five.

GRETCHEN: I'm thirty-five. I guess I could consider waiting for you. In fifteen years, you'll be twenty.

LITTLE BOY: I have a boo-boo on my knee and I can tie my shoelaces.

GRETCHEN: That's better than a lot of the men I know

LITTLE BOY: I have two doggies. And one's small, and one's big.

GRETCHEN: Really?

LITTLE BOY: And I have a teddy bear named Fred. And I can count to ten, and some higher numbers too. One, two ...

GRETCHEN: Really. How interesting.

LITTLE BOY: Three, four, five.

GRETCHEN: Uh huh ...

LITTLE BOY: Five. And six. And seven.

GRETCHEN: Uh huh ... (Lights dim on the Little Boy counting and Gretchen going "uh huh" ...)
```

---

## IC-1231: A . . . My Name is Alice

- Title: A . . . My Name is Alice
- Author (byline): Not specified
- Work: Not specified
- Publisher: Concord Theatricals
- Publication date as stated: Nov 2010
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: POETESS, MS. THOMAS, MRS. JOHNSON, WORKMAN, WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1031
- Already set (do not supply): none

### Source block (context only)

```text
Conceived by: Joan Micklin Silver and Julianne Boyd
ISBN: 978-0573681776
Publisher: Concord Theatricals
Date (Month/Year): Nov 2010
```

### Introduction (context only: never use it for content warnings)

```text
With a wry sense of humor, these sketches from A . . . My Name is Alice address the challenges of being a woman. From beatnik poetry (finger snaps), to being a power-mom in the cut-throat professional world, to merely taking a stroll down the street alone -- women must be prepared to handle it all and smile while we’re doing it!

A . . . My Name is Alice conceived by Joan Micklin Silver and Julianne Boyd
```

### Performance text (classify this)

```text
Conceived by Joan Micklin Silver and Julianne Boyd

POETESS: (Pg 19) A poem. From my collection, For Women Only. (she recites, dramatically)
I am a woman Pity Pretty Polly,
A crippled bird. Doesn’t want a cracker.
The ledge is cold, I am a woman.
My wings are clipped. A crippled bird.
He did it. F—flap
He did it. F—flap
I was his pretty Polly. F—flap
Pity Polly.

Welcome to Kindergarten, Mrs. Johnson (Pg 21-24)

MS. THOMAS: Welcome to kindergarten, Mrs. Johnson.

MRS. JOHNSON: How do you do? It’s a pleasure meeting you. Janie has told me so much about you.

MS. THOMAS: It’s a shame you couldn’t make it to last week’s meeting like the other mothers.

MRS. JOHNSON: I’m sorry. I was speaking at a conference in Zurich.

MS. THOMAS: Well, come along. (crosses back to her desk) I’ve been observing Janie very closely. She’s a very bright girl, Mrs. Johnson. She works beyond potential—a model for her peers, exploring at a level that is way beyond her years. And I’m sorry, but it’s getting on my nerves.

MRS. JOHNSON: I’m sorry.

MS. THOMAS: Don’t fidget, Mrs. Johnson. (beat) She’s a difficult girl, Mrs. Johnson. She helps the other children—Lord knows where it will lead. And I’ve learned that when my back is turned, she’s teaching them to read. I’m to say the least dismayed—what does she think this is, third grade? She’s independent, she’s assertive, she’s always self-assured. Now I don’t know where she’s getting that, but it is not to be ignored—and it generally starts at the home. Did you know that Janie is the only child in class with an even reasonable self-image. Now who’s responsible for that?

MRS. JOHNSON: (a bit thrown) I am.

MS. THOMAS: I’m sorry?

MRS. JOHNSON: (louder) I am.

MS. THOMAS: I am what?

MRS. JOHNSON: I am, Ms. Thomas.

MS. THOMAS: Good. Well, how do you expect her to be intimidated by simple authority?

MRS. JOHNSON: Well, I . . .

MS. THOMAS: Now, I’m not saying you’re a bad mother, even though you missed our pageant And the Halloween parade. No, no one’s saying you’re a bad mother, but your cookies at the bake sale, well, they clearly weren’t homemade.

MRS. JOHNSON: (abashed) They were Pepperidge Farm Mint Milanos!

MS. THOMAS: The other mothers baked.

MRS. JOHNSON: I know, but. . . but I hate baking.

MS. THOMAS: Janie was humiliated!

MRS. JOHNSON: She never said a thing to me!

MS. THOMAS: Well, you’re a busy little bee, Mrs. Johnson. Zipping off to Zurich. I hear next week it’s Rome. Is there really any wonder things are suffering at home? (Mrs. Johnson starts to protest) Oh, there’s no need to object. It’s all here in Janie’s artwork—you can see that I’m correct. (She produces a large pig made out of a Clorox bottle and decorated with hearts. She shows it to Mrs. Johnson)

MRS. JOHNSON: It’s a pig! Made out of a Clorox bottle!

MS. THOMAS: Oh, come on, Mrs. Johnson. There are domestic problems written all over this pig. I know what I’m talking about. I’ve taken psychology courses.

MRS. JOHNSON: But . . .

MS. THOMAS: If you have something to say, you raise your hand! Now, no one wants to be a --

(she waits for Mrs. Johnson to respond)

MRS. JOHNSON: Bad mother.

MS. THOMAS: And I think we can do better if we just make up our minds, ‘cause we all know what happens to a— (she again waits for Mrs. Johnson to respond)

MRS. JOHNSON: Bad mother!

MS. THOMAS: And there’s every indication that this suits your situation. Here’s my evaluation—take it home and have it signed!

MRS. JOHNSON: (fighting back tears) Uh-huh.

MS. THOMAS: Did you know we have these parent-teacher conferences every Monday at four o’clock.

MRS. JOHNSON: (shaking head) Uh-uh.

MS. THOMAS: Well, I hope I’ll be seeing you again very soon.

MRS. JOHNSON: Ye-yes, Ms. Thomas.

MS. THOMAS: That’ll be all . . . (Mrs. Johnson flees for the door) No running in the halls! ******

POETESS: (she continues the 2nd stanza of her poem, dramatically)
I am a woman. “Won’t somebody talk
A neglected plant. to me?”
Hanging by the window I am a woman.
Waiting to be watered. A neglected plant.
He did it. D—droop
He did it. D—droop
I was his philodendron D—droop
Calling out,

***** Hot Lunch (Pg 44-45)

(A workman leans on a bit of construction debris, he’s on lunch break and is ogling imaginary girls that walk by)

WORKMAN: Wowee . . . beautiful, baby, beautiful . . . Hey, don’t ignore me, honey; you’re not that pretty . . . (a woman enters and crosses past him) Wowie, look at them gazoombas! I’d like to show you a taste of heaven, honey bunny.

WOMAN: (very polite) Excuse me, would you repeat what you just said to me?

WORKMAN: (startled) Huh? Oh sure. I said I’d like to show you a taste of heaven, honey bunny.

WOMAN: What else? You said something before that I couldn’t quite make out.

WORKMAN: (getting annoyed) I don’t know. I said you got a great pair of legs or something. I forget.

WOMAN: (matter of fact) No, no, I don’t think you said legs . . . It was something more like daroombas?

WORKMAN: Hey, lady, walk on by, will ya? I’m eating my lunch.

WOMAN: Yes, and I’m very sorry to disturb you, but try to remember what you said. It’s very important to me . . . Now, it sounded like . . .

WORKMAN: (very softly) Gazoombas.

WOMAN: Sorry, I didn’t get that.

WORKMAN: Gazoombas! Now will you please leave me alone? I’m on my lunch break.

WOMAN: I know, I know, I’m infringing on your time and I apologize for it, but what are gazoombas?

WORKMAN: Aw, just a word. A made-up word. No big deal. Look, I’m sorry, okay? I said gazoombas, so what? Since when was it a crime to give a compliment?

WOMAN: Yes, yes, I understand the motivation. It’s just the word, gazoombas. I’d never heard it before. What exactly does gazoombas refer to?

WORKMAN: (embarrassed) You know. (indicates up) Up there. (She looks up) Your chest, lady.

WOMAN: (relieved) Oh, thank goodness. I kind of thought that’s what you meant, but I wasn’t quite sure.

WORKMAN: Well, that’s what I meant, okay? No offense. (He begins to pack up)

WOMAN: Of course not . . . so, you like my gazoombas?

WORKMAN: Hey, cool it, will you? I work here!

WOMAN: Sorry, I just wanted to know if you really appreciated my mammaries.

WORKMAN: Lady, would you excuse me? I gotta get back on the job. (he tries to go past her and she stops him)

WOMAN: Of course, how stupid of me. But before you go, I’d like you to see my gazoombas.

(with her back to the audience . . . )

WORKMAN: Lady, lady, cover yourself! What are you doing?

WOMAN: I thought if I showed you my gazoombas, you’d show me your wogabongo.

WORKMAN: My what?

WOMAN: You know . . . wogabongo!!!

WORKMAN: You’re wacko lady!

WOMAN: Why am I a wacko? You like my gazoombas, I like your wogabongo. I just want that taste of heaven you promised me. Why, with my gazoombas and your wogabongo, we could make great shtahpoonko.

WORKMAN: (calling to an unseen coworker) Hey, Joe! Help! Help! Call the cops! I got a nut-case down here! Help!

WOMAN: (She dusts off her hands, thoroughly pleased with herself) *****

POETESS: (Pg 46) (she finishes her poem, dramatically)
I am a woman. That weekend he took her skiing in Aspen—
A dying swan. That’s when he did it.
Dancing, dancing, dancing. A love bullet
My toe shoes torn. Straight through my feathered gazoombas.
My tutu, too. I am a woman.
He did it. A dying swan.
He did it. Ach-ch
(And he knows who he is.) Ach-ch
Ach-ch
```

---

## IC-1232: Airmail to the Moon

- Title: Airmail to the Moon
- Author (byline): Tom Birdseye
- Work: Not specified
- Publisher: Holiday House
- Publication date as stated: March 1989
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ORA MAE, MAMA, DADAW, BO DEAN, KELSEY ANN
- Teaser before the introduction: Yes
- Spoken words (computed): 1179
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tom Birdseye
ISBN: 978-0823407545
Publisher: Holiday House
Date (Month/Year): March 1989
```

### Introduction (context only: never use it for content warnings)

```text
Losing a tooth is an exciting and memorable part of childhood. It brings thoughts of the magical Tooth Fairy who exchanges money for teeth.

The Tooth Fairy made her first known appearance on September 27, 1908 in an article by the Chicago Daily Tribune . . . and parents under the guise of fairies have been forking out money ever since! Thanks, Chicago!!

Hold on to your wallets, parents: As of 2021, Tooth Fairy payouts have hit an all-time high. According to Delta Dental, the average cash payout for a tooth today is nearly 5 dollars! My biggest haul was a quarter!

In this tale, Ora Mae Cotton’s faith in the tooth fairy is shaken and she is bound and determined to investigate her stolen 1st tooth.

Airmail to the Moon by Tom Birdseye
```

### Performance text (classify this)

```text
ORA MAE: (with a deep southern accent) My name is Ora Mae Cotton of Crabapple Orchard, and last night somebody stole my tooth. I’d been down at the creek catching crawdads when it started tingling – kind of like if you missed your toast and peanut butter and bit your teeth really hard instead. That was three weeks ago. I was popcorn-in-the-pan excited, for sure that tooth was gonna fall out any second. But Dadaw (that’s what I call my daddy) always says not to milk the cow when she’s asleep (which is Crabapple Orchard talk for not blabbing to everybody about something before you’re sure of what you’re blabbing about). So I didn’t tell a soul.

ORA MAE: Then last Monday, while fetching the mail at the county road, I stuck my tongue out at my pesky neighbor, Merrietta Bean, and gave her a big raspberry like this – PPLLUBB! The vibration from my tongue flapping against my teeth popped that chomper of mine as loose as a goose on ice skates. So I told the world about my first tooth coming out . . . whether they wanted to hear or not.

By Thursday that tooth was so wobbly it was just hanging on by one root and a flap of skin. I could push it all the way out between my lips with my tongue and help Mama slop the hogs at the same time. Then Friday, right after my big brother Bo Dean and my little sister Kelsey Ann got into a fight at the dinner table over whether Arlene Peterson’s pigs really kneel and pray before they eat, that loose tooth of mine fell right out of my mouth – plop – and landed smack in the middle of my spaghetti.

MAMA: Be sure and put that tooth under [your] pillow. That way the tooth fairy [will] come get it and give [you] some money.

ORA MAE: Money! Shout howdy. Mama didn’t say how much. But I figured it had to be at least a thousand dollars, or maybe even a hundred dollars. I was so excited that I hurried to bed as quick as a dropped cat just so I could dream about all the things I was going to buy. But like I said, somebody stole my tooth. So I guess I dreamed all night for nothing. First thing this morning when I discovered the crime. I ran lickety-split to find Mama. She was in the root cellar, up to her elbows in rutabagas. (To Mama, yelling) Mama! Is the tooth fairy a crook like ol’ Hester Jenkins that stole the parking meter from in front of the county courthouse?

MAMA: Why no, Oreo. The tooth fairy is as honest as flowers in the spring.

ORA MAE: That’s what I thought. (fuming) Well, then somebody besides the tooth fairy stole my tooth. Somebody so crooked they screw their socks on every morning. And when I catch ‘em, I’m gonna open up a can of gotcha and send ‘em airmail to the moon!

MAMA: Oreo, I don’t think anybody would steal your tooth. Maybe the tooth fairy is putting it on a string with other teeth to make a beautiful necklace. That’s what I’ve heard she does. She probably forgot to leave you some money and will remember tonight.

ORA MAE: (To audience) That didn’t seem likely to me. What good is a tooth fairy that forgets?

MAMA: Why don’t you go ask your daddy. Maybe he knows something we don’t.

ORA MAE: (To audience) Aha! He’s a real thinker, my Dadaw is. Why, he even sells watermelons to the grocery store. He knows mighty near everything.

DADAW: (Singing and shaving with a straight razor)

ORA MAE: I heard Dadaw before I spied him. He was out by the tire swing shaving and singing at the same time (which is mighty dangerous if you ask me). Half his face was shaving cream. The other half was “as smooth as a baby’s belly,” as he liked to say. (To Dadaw) Dadaw! Some crook stole my tooth. And when I catch ‘em, I’m gonna open up a can of gotcha and send ‘em airmail to the moon!”

DADAW: Oreo, I don’t think anybody would steal your tooth. Maybe the tooth fairy has it and is grinding it up in a big machine. That tooth dust might come out as money. Then the tooth fairy could us it to buy you some real estate. Like one of them condominiums at Miami Beach.

ORA MAE: (To audience) What would I do with a condominium at Miami Beach? (To Dadaw, shouting) Tooth dust? But Dadaw! Somebody stole my tooth!

DADAW: (rubbing his chin and nodding) Why don’t you go ask your brother. He usually knows more than he tells.

ORA MAE: Aha! My brother Bo Dean is as ornery as a bull in a beehive. And he lost two teeth last week when he fell out of the hayloft. I’ll bet he stole my tooth and glued it straight into his mouth. I’m gonna get that boy! And when I do, I’m gonna open up a can of gotcha and send him airmail to the moon!

BO DEAN: (calmly, as he sneaks up on a frog or snake to catch) I didn’t steal your tooth, Oreo. What would I want with girl teeth, anyway? They don’t fit boys.

ORA MAE: (to audience) I hadn’t thought of that.

BO DEAN: Are you sure you didn’t just give it to the tooth fairy, no money down?

ORA MAE: (yelling) Why would I do such a thing?! That’s stupid!

BO DEAN: (Shhhs Ora Mae) The tooth fairy saves teeth to give to babies, right, Oreo?

ORA MAE: (whispering) Not according to Mama or Dadaw, she don’t.

BO DEAN: (Still pre-occupied with his hunt) Well, according to me, Bo Dean Cotton, she does. That’s so they can chew on rocks and shoes and stuff. (whispering as he makes a grab for the reptile) Where do you think Kelsey Ann got her teeth when she was little?

ORA MAE: (to audience) Aha! Maybe Bo Dean has a point. Kelsey Ann is as ornery as Bo Dean plus ten. She had to be the one that stole my tooth! I’ll get that little diddle-do! And when I do, I’m gonna open up a can of gotcha and send her airmail to the moon! (she races off to find Kelsey Ann) Kelsey Ann Cotton! Give me my tooth. I know you stole it!

KELSEY ANN: (in the middle of a tea party) Pig feathers. I’m as sweet as roses in the snow. The tooth fairy steals teeth, not me. She makes them into doorknobs. Didn’t you know that Oreo?

ORA MAE: Not according to Mama, Dadaw, or Bo Dean she doesn’t. You took it!

KELSEY ANN: She does too, ‘cause I didn’t.

ORA MAE: Does not, you did!

KELSEY ANN: Does too, I didn’t.

ORA MAE: Does not, you did!

KELSEY ANN: (giggling) I’ll bet you threw it away, Oreo. It’s probably in the bottom of the garbage can stuck in the middle of a blob of leftover spaghetti. That’s how forgetful you are. That tooth will never be a doorknob.

ORA MAE: (to audience) That did it! I was so mad I was ready to scream. Nobody really knew what the tooth fairy was up to. And nobody was the lop-eared rascal that stole my tooth. I was just about to pop my cork clean out of Crabapple Orchard. But instead, I just stood there looking at my sister, and . . . (Ora Mae starts crying – loud and wailing) Somebody stole my tooth . . . and when I catch ‘em I’m gonna open up a can of gotcha and send ‘em airmail to the moon. (She sticks her hands down deep in her pockets and a shocked expression comes over her face. She stops crying) My name is Ora Mae Cotton of Crabapple Orchard. And right now I feel like a possum up a plum tree. I’m as embarrassed as a zebra without stripes. (sheepishly and she hold out her hand) You see, there’s this little hard thing in the bottom of my pants pocket. It’s right where I left it. (beat) I wonder if the tooth fairy ever sends motor-mouth kids like me airmail to the moon?
```

---

## IC-1233: Alice’s Adventures in Wonderland

- Title: Alice’s Adventures in Wonderland
- Author (byline): Lewis Carroll
- Work: Not specified
- Publisher: Dover Publications
- Publication date as stated: May 1993
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ALICE, WHITE RABBIT, DOOR #1, DOOR #2, DOOR #3, SMALL DOOR, BOTTLE, NARRATOR, CATERPILLAR, CHAPTER VI, CHESHIRE CAT, CHAPTER VII, HATTER, MARCH HARE, CHAPTER VIII, CARD #5, QUEEN, VOICE IN THE DISTANCE, CHAPTER XI, CHAPTER XII, KING
- Teaser before the introduction: Yes
- Spoken words (computed): 1030
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lewis Carroll
ISBN: 978-0486275437
Publisher: Dover Publications
Date (Month/Year): May 1993
```

### Introduction (context only: never use it for content warnings)

```text
In 1865 a novel was written that would change the face of children’s literature. In fact, Alice in Wonderland’s themes and characters are so bizarre that in the 1960’s rumors began to surface that Lewis Carroll wrote the book under the influence of drugs. It’s a tempting theory – after all the story has Alice eating ‘magic’ mushrooms and meeting hookah smoking caterpillars. Reference to this seminal work appear in modern day films like The Matrix: "You take the blue pill . . . The story ends, you wake up in your bed and believe whatever you want to believe. You take the red pill . . . You stay in Wonderland, and I show you how deep the rabbit hole goes."

Alice in Wonderland by Lewis Carroll . . . No pills or mushrooms required.
```

### Performance text (classify this)

```text
Chapter I: Down the Rabbit-Hole Alice is reading a book, flipping through the pages rapidly and is bored. (Actor simulates the passing of time by pantomiming the movements of a clock with sound effects)

ALICE: (Sighs heavily as she closes the book) What is the use of a book without pictures or conversations! (Suddenly a white rabbit catches her attention)

WHITE RABBIT: Oh, dear! Oh, dear! I shall be too late!” (he takes a watch out of his pocket, looks at it and hurries on. Alice follows.) Oh my ears and whiskers, how late it’s getting! [Rabbit Hole!] (He jumps down the hole and Alice follows. As she lands, the rabbit is no longer in sight. She finds herself in a hall with a serious of doors. She tries each door)

DOOR #1: Locked

DOOR #2: Locked

DOOR #3: Locked

ALICE: [Oh, look] a tiny golden key. (Picks it up) It might belong to one of the doors!

DOOR #1: Too small

DOOR #2: [Nope]

DOOR #3: (Simply laughs)

ALICE: Either the locks [are] too large, or the key [is] too small.

SMALL DOOR: (representing a small door – makes some type of sound to get Alice’s attention)

ALICE: A little door! (She tries the little key in the lock and it fits!) [Oh, look] the loveliest garden you ever saw. Bright flowers . . . fountains! (She tries to fit her head in the doorway, but she’s much too big) Oh, how I wish I could shut up like a telescope! I think I could, if I only knew how to begin.

BOTTLE: Drink Me!

ALICE: [Well, I’m certainly] not going to do that in a hurry. I’ll look first and see whether it’s marked “Poison” or not. (Alice examines the bottle)

BOTTLE: Drink Me! (Alice shrugs her shoulders and took a sip)

ALICE: What a curious feeling! (Alice shrinks down to 10-inches high, quickly tries the key in the lock. It works and she swings open the door)

NARRATOR: Wonderland! (As Alice steps through the doorway, trumpets blare to herald her arrival)

ALICE: Curiouser and curiouser!

Chapter V: Advice from a Caterpillar

ALICE: [What a] large mushroom . . . Caterpillar!

CATERPILLAR: (taking a hookah from its mouth) Who are you?

ALICE: I – I hardly know, sir, just at the present – at least I know who I was when I got up this morning, but I think I must have changed several times since then.

CATERPILLAR: What do you mean? Explain yourself!

ALICE: I can’t explain myself, I’m afraid, sir, because I’m not myself, you see?

CATERPILLAR: I don’t see!

ALICE: (losing her temper) I’m afraid I can’t put it more clearly – Being so many different sizes in a day is very confusing!

CATERPILLAR: Keep your temper! . . . So you think you’re changed, do you? What size do you want to be?

ALICE: Well, I should like to be a little larger, sir – three inches is such a wretched height to be.

CATERPILLAR: One side of the mushroom will make you grow taller, and the other side will make you grow shorter. (He disappears in a puff of smoke)

ALICE: (Alice stretches her arms round the mushroom as far as they will go and breaks off a bit with each hand) And now . . . which is which . . . (she takes a bite of one of the pieces and begins to grow) [Ahhh. . .] Back to my right size! The next thing is to get into that beautiful garden! (Alice walks for a bit and comes to a small house)

CHAPTER VI: Pig and Pepper

ALICE: Cheshire Cat! Would you tell me please, which way I ought to walk from here?

CHESHIRE CAT: That depends a good deal on where you want to get to. In that direction (waiving its right paw round) lives a Hatter: and in that direction (waving the other paw) lives a March Hare. Visit either you like: they’re both mad.

ALICE: But I don’t want to go among mad people.

CHESHIRE CAT: Oh, you can’t help that. We’re all mad here. I’m mad. You’re mad.

ALICE: How do you know I’m mad?

CHESHIRE CAT: You must be or you wouldn’t have come here. . . Do you play croquet with the Queen today?

ALICE: I should like it very much, but I haven’t been invited y et.

CHESHIRE CAT: You’ll see me there! (and he vanishes)

ALICE: [Well], I’ve seen hatters before. The March Hare will be much the most interesting and perhaps as this is May it won’t be raving mad – at least not so mad as it was in March.

(Hatter enters. He pours himself some tea, and follows Alice for a few seconds, establishing character, and then speaks)

CHAPTER VII: A Mad Tea-Party

HATTER: No room!

MARCH HARE: No room!

ALICE: There’s plenty of room! It’s laid for a great many more than three!

HATTER: Your hair wants cutting.

ALICE: (taken by surprise) You should learn not to make personal remarks. It’s very rude.

HATTER: Why is a raven like a writing-desk?

ALICE: I’m glad [you’ve] begun asking riddles! I believe I can guess that.

MARCH HARE: Do you mean that you think you can find out the answer to it? You should say what you mean.

ALICE: I do – at least – at least I mean what I say – that’s the same thing, you know.

HATTER: Not the same thing a bit! Why, you might just as well say that ‘I see what I eat’ is the same thing as ‘I eat what I see!’ . . . (He looks at his watch uneasily, shaking it every now and then and holding it to his ear.) What day of the month is it?

ALICE: The fourth.

HATTER: (sighs) Two days wrong! (begins trying to reset his watch)

ALICE: (grabbing his wrist to look at the watch) What a funny watch! It tells the day of the month, and doesn’t tell what o’clock it is?

HATTER: (pulling his arm back, offended) Why should it? Does your watch tell you what year it is?

ALICE: Of course not, but that’s because it stays the same year for such a long time together.

HATTER: (Continues with his tea) Which is just the case with mine. . . Have you guessed the riddle yet?

ALICE: No, I give it up. What’s the answer?

HATTER: I haven’t the slightest idea. (he laughs)

ALICE: (wearily) I think you might do something better with the time than wasting it in asking riddles that have no answers.

HATTER: If you knew Time as well as I do, you wouldn’t talk about wasting IT. It’s HIM. I dare say you never even spoke to Time!

ALICE: Perhaps not, but I know I have to beat time when I learn music.

HATTER: Ah! That accounts for it. He won’t stand beating! . . . (Alice stammers for a response)

MARCH HARE: Take some more tea!

ALICE: I’ve had nothing yet, so I can’t take more.

HATTER: You mean, you can’t take less. It’s very easy to take more than nothing.

ALICE: (disgruntled) Nobody asked your opinion.

HATTER: Who’s making personal remarks now? I want a clean cup. Let’s all move one place on!

ALICE: Really, now if you ask me . . . I don’t think –

HATTER: Then you shouldn’t talk!

ALICE: (Extremely offended) [This is] the stupidest tea-party I ever was at in all my life!”

(trumpets blare)

CHAPTER VIII: The Queen’s Croquet-Ground

CARD #5: The Queen! The Queen! (Alice straightens her dress)

QUEEN: Who is this? What’s your name child?

ALICE: My name is Alice, so please your Majesty.

QUEEN: (looks her up and down and then makes a decision) Off with her head! Off . . .

ALICE: Nonsense!

QUEEN: Can you play croquet?

ALICE: Well . . .yes . . .

QUEEN: Well, come on then! Get to your places! (she grabs a croquet mallet and ball and tosses the ball to Alice)

ALICE: [This is] a flamingo and the croquet-balls [are] hedgehogs!

QUEEN: Off with her head! (the Queen stalks away)

ALICE: (to herself) They’re dreadfully fond of beheading people here. (then she notices the arrival of the Cheshire Cat) It’s the Cheshire Cat – now I shall have somebody to talk to.

CHESHIRE CAT: How do you like the Queen?

ALICE: Not at all! She’s so extremely . . . (The Queen comes up behind her, listening – Alice notices) . . . likely to win, that it’s hardly worthwhile finishing the game.

VOICE IN THE DISTANCE: The trial’s beginning! (Scene changes to the Court of Justice)

CHAPTER XI: Who Stole the Tarts?

WHITE RABBIT: (blows three blasts on his trumpet) Silence in the court! (unrolls a parchment scroll and reads) The Queen of Hearts, she made some tarts, All on a summer day: The Knave of Hearts, he stole those tarts, And took them quite away! . . . . Alice!

CHAPTER XII: Alice’s Evidence

ALICE: (Complete surprised) Here!

KING: What do you know about this business?

ALICE: Nothing.

KING: Nothing whatever?

ALICE: Nothing whatever.

KING: That’s very important. . . Unimportant! That proves his guilt!

ALICE: It proves nothing of the sort!

KING: Let the jury consider their verdict.

QUEEN: No, no! Sentence first – verdict afterwards

ALICE: Stuff and nonsense! The idea of having the sentence first!

QUEEN: Hold your tongue!

ALICE: I won’t (stomping her foot)

QUEEN: Off with her head!

ALICE: (Looking around the courtroom) Who cares for you? You’re nothing but a pack of cards!

(transition back to the scene that begins this cutting, with Alice having fallen asleep over her book -- Actor simulates the passing of time by pantomiming the movements of a clock with sound effects as Alice slowly wakes up) Oh . . . Oh . . . I’ve had such a curious dream!

WHITE RABBIT: Alice! (Alice’s face reacts in shock)
```

---

## IC-1234: The Amazing Bone

- Title: The Amazing Bone
- Author (byline): William Steig
- Work: Not specified
- Publisher: Square Fish
- Publication date as stated: July 2011
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, PEARL, BONE, MOTHER, ROBBER 1, ROBBER 2, FOX, FATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1341
- Already set (do not supply): none

### Source block (context only)

```text
Author: William Steig
ISBN: 978-0312564216
Publisher: Square Fish
Date (Month/Year): July 2011
```

### Introduction (context only: never use it for content warnings)

```text
The Amazing Bone by William Steig
```

### Performance text (classify this)

```text
NARRATOR: It was a brilliant day, and instead of going straight home from school, Pearl dawdled. She watched the grownups in town at their grownup work, things she might someday be doing. She saw the street cleaners sweeping the streets and she looked in at the bakery on Parsnip Lane and saw the bakers taking hot loaves of pumpernickel out of the oven and powdering crullers with sugar dust. On Cobble Road she stopped at Maltby’s barn and stood gawking as the old gafers pitched their ringing horseshoes and spat tobacco juice. Later she sat on the ground in the forest between school and home, and spring was so bright and beautiful, the warm air touched her so tenderly, she could almost feel herself changing into a flower. Her light dress felt like petals.

PEARL: I love everything.

BONE: So do I.

PEARL: (straightening up and looking around) Where are you?

BONE: Look down. I’m the bone in the violets near the tree by the rock on your right.

PEARL: (following the directions and searching near the tree. She finds the BONE and speaks in awe) You talk?

BONE: In any language. Habla espanol? Rezumiesh popolsk? Sprechen sie Deutsch? And I can imitate any sound there is: (sounds of a trumpet calling soldiers to arms. Then wind blowing, then like pattering rain. Then snoring, then sneezing)

PEARL: (couldn’t believe what she was hearing.) You’re a bone. How come you can sneeze?

BONE: I don’t know. I didn’t make the world.

PEARL: May I take you home with me, wonderful bone?

BONE: You certainly may. I’ve been alone a long time. A year ago, come August, I fell out of a witch’s basket. I could have yelled after her as she walked on, but I didn’t want to be her bone any longer. She ate snails cooked in garlic at every meal and was always complaining about her rheumatism and asking nosy questions. I’d be happier with someone young and lively like you.

NARRATOR: Pearl picked the bone up and gently put it in her purse. She left the purse open, so they could continue their talk, and started home, forgetting her schoolbooks on the grass. She was eager to show this bone to her parents, and she could guess what would happen when she did. She would tell about the talking bone, her mother would say

MOTHER: You’re only imagining it

NARRATOR: Her father would agree, and then the bone would flabbergast them both by talking. The spring green sparkled in the spring light. Tree toads were trilling.

PEARL: It’s the kind of wonderful day, when wonderful things happen – like my finding you.

BONE: Like my finding you! (And it began to whistle a walking tune)

NARRATOR: That made the going very pleasant. But not for long. Who should rush out from in back of a boulder and spoil everything but three highway robbers with pistols and daggers. Pearl couldn’t tell what breed of animal they were, because they wore cloaks and Halloween masks, but they were fierce and spoke in chilling voices.

ROBBER 1: Hand over the purse!

NARRATOR: Pearl would have gladly surrendered the purse, just to be rid of them, but not with the bone in it.

PEARL: You can’t have my purse.

ROBBER 2: What’s in it? (pointing his gun at Pearl’s head.)

BONE: (growling) I’m in it! (And it began to hiss like a snake and roar like a lion.)

NARRATOR: The robbers didn’t wait around to hear the rest, in case there was any more. They fled so fast you couldn’t tell which way they’d gone. It made Pearl laugh. The bone, too. They continued on their way, joking about what had just happened and chatting about this and that. But it wasn’t long before a fox stepped forth from behind a tree and barred their path. He wore a sprig of lilac in his lapel, he carried a cane, and he was grinning so the whole world could see his sharp white teeth.

FOX: Hold everything! (Pearl froze.) You’re exactly what I’ve been longing for -- young, plump, and tender. You will be my main course at dinner tonight. (he seized Pearl in a tight embrace.)

BONE: (screaming) Unhand her, you villain, or I’ll bite your ears off!

FOX: (surprised) Who is that speaking?

BONE: A ravenous crocodile who dotes on fresh fox chops, that’s who!

NARRATOR: The wily fox was not as easily duped as the robbers. He saw no dangerous crocodile. He peered into Pearl’s purse, where the sounds seemed to be coming from, and pulled out the bone.

FOX: (holding up the bone) As I live and flourish! A talking bone. I’ve always wanted to own something of this sort. (And he put the bone in his pocket)

BONE: (roaring and ranting)

NARRATOR: Pushing Pearl along, the fox set out for his hideaway. Pearl’s sobs were so pitiful the fox couldn’t help feeling a little sorry for her, but he was determined she would be his dinner.

PEARL: (sobbing, whimpering and pitiful) Please, Mr. Fox, may I have my bone back, at least until I have to die?”

FOX: Oh, all right. (disgusted with himself for being so soft-hearted, he handed her the bone, which she put back in her purse.)

BONE: You must let this beautiful young creature go on living. Have you no shame, sir!

FOX: (laughing) Why should I be ashamed? I can’t help being the way I am. I didn’t make the world.

BONE: You coward! You worm, you odoriferous wretch!

FOX: (snarling) Shut up, or I’ll eat you. It would be amusing to gnaw on a bone that talks . . . and screams with pain.

NARRATOR: The bone kept quiet the rest of the way, and so did Pearl. When they arrived at the fox’s hideaway, he shoved Pearl, with her bone, into an empty room and locked the door. Pearl sat on the floor and stared at the walls.

BONE: (whispering) I know how you feel.

PEARL: (also whispering) I’m only just beginning to live. I don’t want it to end.

BONE: I know.

PEARL: Isn’t there something we can do?

BONE: I wish I could think of something, but I can’t. I feel miserable.

PEARL: (hearing some sounds from the kitchen) What’s that?

BONE: (whispering) He’s sharpening a knife.

PEARL: (sobbing quietly) Oh, my goodness! And what’s that?

BONE: Sounds like wood being put into a stove.

PEARL: I hope it won’t all take too long

NARRATOR: She could smell vinegar and oil. The fox was preparing a salad to go with his meal.

PEARL: (Pearl hugged the bone to her breast.) Bone, say something to comfort me.

BONE: You are very dear to me.

PEARL: Oh, how dear you are to me!

NARRATOR: She could hear a key in the lock and was unable to get another word out of her throat or turn her eyes toward the door.

BONE: (whispered) Be brave.

NARRATOR: Pearl could only tremble. She was dragged into the kitchen, where she could see flames in the open stove.

FOX: (sighing) I regret having to do this to you. It’s nothing personal.

BONE: “Yibbam!”

FOX: (standing stock-still) What was that?

BONE: Yibbam sibibble! Jibrakken sibibble digray!

NARRATOR: And something quite unexpected took place. The fox grew several inches shorter.

BONE: Alabam chinook beboppit gebozzle!

NARRATOR: Miraculously the fox was the size of rabbit. No one could believe what was happening, not Pearl, not the fox, not even the bone, whose words were making it happen.

BONE: Adoonis ishgoolak keebokkin yibapp!

NARRATOR: The fox, clothes and all, was not the size of a mouse.

BONE: Scrabboonit!

NARRATOR: And the mouse – that is, the minuscule fox – scurried away and into a hole.

PEARL: (exclaiming) I didn’t know you could do magic!

BONE: Neither did I.

PEARL: Well, what made you say those words?

BONE: I wish I knew. They just came to me, I had to say them. I must have picked them up somehow, hanging around with that witch.

PEARL: You’re an amazing bone, and this is a day I won’t ever forget!

NARRATOR: It was dark when they reached Pearl’s house. The moment the door swung open she was in her mother’s arms, and right after that in her father’s.

MOTHER: Where on earth have you been?

FATHER: We were frazzled with worry.

PEARL: (holding up the bone) This bone can talk!

NARRATOR: And just as she had expected, her mother said,

MOTHER: A talking bone? Why, Pearl, it’s only your imagination.

NARRATOR: And her father said something similar. And also as Pearl had expected, the bone astonished them both by remarking,

BONE: You have an exceptional daughter.

NARRATOR: Before her parents had a chance to get over their shock, Pearl began telling the story of her day’s adventure, and the bone helped out. It was all too much for Pearl’s parents. Until they got used to it. The bone stayed on and became part of the family. It was given an honored place in a silver tray on the mantelpiece. Pearl always took it to bed when she retired, and the two chatterboxes whispered together until late in the night. Sometimes the bone put Pearl to sleep by singing, (sing a lullaby here) or by imitating soft harp music. Anyone who happened to be alone in the house always had the bone to converse with. And they all had music whenever they wanted it, and sometimes even when they didn’t.
```

---

## IC-1235: Amy’s Answering Machine: Messages from Mom

- Title: Amy’s Answering Machine: Messages from Mom
- Author (byline): Amy Borkowsky
- Work: Not specified
- Publisher: Atria Books
- Publication date as stated: April 2001
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: AMY, AMY’S MOM, NEWS REPORTER, GANG MEMBER, GANG MEMBER 2, ANDREW, HOSPITAL WORKER, DAIRY BOARD, WOMAN, WOMAN 2
- Teaser before the introduction: Yes
- Spoken words (computed): 1352
- Already set (do not supply): none

### Source block (context only)

```text
Author: Amy Borkowsky
ISBN: 978-0743422284
Publisher: Atria Books
Date (Month/Year): April 2001
```

### Introduction (context only: never use it for content warnings)

```text
Does your mother call you in a panic whenever there's a storm warning for your area? Does she act as though it's her duty to alert you to every health story on the news? Have you ever been briefly out of touch with your mother only to find she's phoned everyone short of the National Guard to track you down – Or, just maybe, are you that mother? Take comfort in knowing you're not alone! This is Amy’s Answering Machine: Messages from Mom by Amy Borkowsky
```

### Performance text (classify this)

```text
(Note: Amy’s mom peppers her words with Jewish phrases – See glossary at the end of this selection)

AMY: (Pg 14) I have a radio that gives weather forecasts every few minutes, and a TV with a channel devoted entirely to the weather. So why does my mother always feel compelled to call me up with a weather report?

AMY’S MOM: (BEEP) Amila?

AMY: (Pg 9) You may wonder why my mother calls me “Amila” (pronounced AY-muh-luh) when my name is actually Amy. The answer is that, as a classic Jewish mother, my mom follows the tradition of adding an “ila” to my name as a term of endearment. And here and there, my mother uses some other Yiddish phrases.

AMY’S MOM: (Pg 14-15) Amila? I hope you’re on your way home. I just heard on the weather, there’s a big storm headed for New York and they’re expecting four to six inches in the city, with accumulations of up to a foot in the outlying areas. So if I were you. I wouldn’t go shlepping to any outlying areas. On the weather map, all over New York, they had snowflakes the size of bagels. So if you have to go out, make sure you bundle up. And wrap a scarf around your face to protect it, ‘cause y’know, there was that man who climbed Mount Everest and lost his entire nose. Okay, honey? I love you. Bye.

AMY: Somehow I just don’t see anywhere I would shlep to as being quite parallel to climbing Mt. Everest.

NEWS REPORTER: Our guest today is Amila Borkowsky, the first woman ever to reach the summit of Macy’s department store. So, Amila, what was it like up there?

AMY: Words just can’t describe it. The view of Linens and Housewares was breathtaking.

NEWS REPORTER: Now the question everyone want to know is, what did you buy?

AMY: Nothing. By the time I got there, they didn’t have the one item I really needed.

NEWS REPORTER: What was that?

AMY: A new nose! *******

AMY’S MOM: (Pg 29-30) (BEEP) Amila? I don’t think you went to bed yet, but maybe you’re in the tub. I wanted to know if you happened to catch the story on the new squirting scam. Apparently, the way it works is, you’ll be walking along the street, and some guy or maybe a woman will squirt you from behind with a bottle of ketchup. Then someone else who’s in cahoots with that person will say, “Excuse me, Miss, but there’s some ketchup on your sweater.” And then, just as you go to wipe it, they grab your bag and that’s the end of that. So if somebody tries to point out any ketchup on you, you can just say something like, “I’m well aware of the ketchup – in fact it matches my pants that have a big blob of relish.” Then as they’re looking down at your pants, you can make a quick qetaway. All right, I hope you’re doing good, and I’ll talk to you tomorrow. Bye-bye.

AMY: In a world where innocent people are being randomly attacked with guns, knives, and AIDS-filled syringes, I find it hard to lose even a millisecond of sleep worrying that someone’s going to come after me with a bottle of ketchup. *******

AMY’S MOM: (Pg 57) (BEEP) Hi, Amila. It’s me. Y’know the red terry robe you wore when I came to visit – it’s like a ruby red with a belt? Do you still wear that or did you throw it out? I just wanna tell you that if you take out the garbage or run to the mailbox, you may wanna put on something else, because my friend Eileen’s grandson said that red is a gang color. Okay, Sweetie-pie? Talk to you later.

AMY: Now what are the odds that two violent street gangs are going to decide to have it out on the twelfth floor of a Murry Hill doorman building, at the exact moment that I’m carrying out a bag of trash, totally oblivious to the Crips and the Bloods lining the hallway? They’ll be yelling . . .

GANG MEMBER: Don’t go after Julio – he’s not the leader!

GANG MEMBER 2: It’s . . . it’s the Jewish girl in the bathrobe! *******

AMY: (Pg 72-74) The TV! It only feeds my mother’s already obsessive concern over my safety.

AMY’S MOM: (BEEP) Yeah, hello, Amila. They just said on TV, “It’s ten p.m., do you know where your children are? And I’m thinking, I don’t know, so I figured I’d call you, mamascheinz. You must be in the bathroom or something. Give me a buzz when you’re don, okay? All right, bye-bye. (Amy, sleeping soundly, snores)(BEEP) Amila? It’s five to eleven and I know you have work tomorrow. I’m getting ga little worried. Call me when you get the message.

AMY: This message was followed by FOUR separate messages from my friends, Michael, Sherry, Alison and Leslie, each saying that my mother had called them looking for me!

ANDREW: (BEEP) Hi, Amy. Yeah, it’s Andrew. I just got a call from your mom about ten minutes ago, and she wanted to know if you were spending the night at my house. I told her we broke up four years ago.

HOSPITAL WORKER: (BEEP) Hello, Miss Borkowsky? I’m calling from NYU Hospital. Someone called here claiming to be your mother and wanting to know if you’d been admitted.

AMY: So where was I, you ask? In my own bed. Sound asleep. I’d conked out early and had just turned my ringer off. When I work up the next morning, I was sooooo mad. I could only imagine who she would have called next . . . (Ring Ring)

DAIRY BOARD: Good morning, National Dairy Board.

AMY’S MOM: Uh, yes, I’d like to find out how I can get my child’s picture on a milk carton.

DAIRY BOARD: How long has the child been missing?

AMY’S MOM: A very long time. I’d say well over ninety minutes.

DAIRY BOARD: Okay, Ma’am, is this a boy or a girl?

AMY’S MOM: It’s a girl – my Amila.

DAIRY BOARD: And what was she wearing when she disappeared?

AMY’S MOM: Let’s see . . . she probably had on a silk blouse with maybe a dark blazer, a matching skirt, and a pair of pumps.

DAIRY BOARD: Was she playing dress up?

AMY’S MOM: No. But she mentioned today she had to go see a new client.

DAIRY BOARD: Ma’am, how old is your Amila?

AMY’S MOM: Thirty-four and three quarters

*******

AMY: (Pg 97-98) People are always debating whether it’s harmful for kids to watch too much TV, but I think the bigger problem is what happens when your parents watch too much TV!

AMY’S MOM: (BEEP) Amila? I just talked to you. Where’d you go? Anyway, I was watching the news and they had a story about the Hell’s Angels motorcycle club. They flashed a shot of a big bear of a guy from Greenwich Village who was covered in tattoos, and on the back of his motorcycle was a very pretty girl. Was that you? She had your hair, and she was wearing a green blouse that looked like the one that I gave you for Chanuka. You know how I feel about motorcycles!

AMY: (Sarcastically) I did understand her confusion. There are so few women in Manhattan with brown, wavy hair that, really, who wouldn’t assume it was me? I’m constantly getting comments . . .

WOMAN: Excuse me, but I was just noticing how completely unique your hair is. What color would you call that?

AMY: Brown.

WOMAN: Can you write that down? I want to ask my colorist about it.

*******

AMY: (Pg 8) I love my mother, but . . . I know my mother means well, but . . . (Pg 84) Halloween . . . REALLY? I outgrew Halloween when I was around twelve!

AMY’S MOM: (BEEP) (in her best scary voice) Boooooo, Amila. Booooooo. Okay, don’t get scared. It’s just me, honey. Tomorrow’s Halloween, and I just want to warn you to throw out anything that looks suspicious in your trick-or-treat bag. Like if you should happen to find a hole in a candy bar, it could mean that someone stuck it with a hypodermic needle, all right? Happy Halloween!

AMY: How could she even imagine me trick-or-treating at this age?

AMY’S MOM: (Pg 74) Thirty-four and three quarters (Pg 84-85) (Knock, knock, knock)

WOMAN 2: Who’s there?

AMY: Trick or treat!

WOMAN 2: My goodness! What a wonderful costume! Can you wait just a minute?

AMY: Actually, I’m not wearing a cos . .

WOMAN 2: Staaaaanley! Bring the camera! There’s a little girl dressed as Jerry’s friend Elaine! She has the hair and everything! It’s amazing. She even looks like she’s in her thirties!

AMY: That’s because . . .

WOMAN: Your mommy must’ve spent quite some time making your costume!

*******

AMY: (Pg 11) So . . . If your own mother drives you crazy, I hope you now know . . . You are not alone!

AMY’S MOM: (BEEP) (Pg 26) Amila . . . it’s me again!
```

---

## IC-1236: Are You There, God? It’s Me, Margaret

- Title: Are You There, God? It’s Me, Margaret
- Author (byline): Judy Blume
- Work: Not specified
- Publisher: Atheneum Books for Young Readers
- Publication date as stated: April 2014
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: MARGARET, NANCY, MR. BENEDICT, MOM, JANIE, VOICE FROM MOVIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1481
- Already set (do not supply): none

### Source block (context only)

```text
Author: Judy Blume
ISBN: 978-1481409933
Publisher: Atheneum Books for Young Readers
Date (Month/Year): April 2014
```

### Introduction (context only: never use it for content warnings)

```text
Adolescence! When we reminisce about that time in our childhood, it usually brings up the feelings of awkwardness, problems, and just longing for acceptance. Margaret is no exception. She has the same big (or shall we say small) problems as any other 12-year-old, and finds herself sharing and pleading with the Almighty in . . .

Are You There, God? It’s Me, Margaret by Judy Blume
```

### Performance text (classify this)

```text
MARGARET: (Pg 1) Are you there, God? It’s me, Margaret. We’re moving today. I’m so scared, God. I’ve never lived anywhere but here. Suppose I hate my new school? Suppose everybody there hates me? Please help me, God. Don’t let New Jersey be too horrible. Thank you.

MARGARET: (Pg 16) My parents don’t know I actually talk to God. I mean, if I told them, they’d think I was some kind of religious fanatic or something, so I keep it very private. I can talk to him without moving my lips if I have to. My mother says God is a nice idea. He belongs to everybody. (Pg 1-2) [Anyway], I was really surprised when I came home from camp and found out our New York apartment had been rented to another family and that we owned a house in Farbrook, New Jersey. First of all, I never even heard of Farbrook. And second of all, I’m not usually left out of important family decisions. (Pg 4) We hadn’t been in the house more than an hour when the doorbell rang. I answered. It was this girl in a bathing suit.

NANCY: Hi. I’m Nancy Wheeler. The real estate agent sent out a sheet on you. So I know you’re Margaret and you’re in the sixth grade. So am I.

MARGARET: She was taller than me and had bouncy hair. The kind I’m hoping to grow. Her nose turned up so much I could look right into her nostrils.

NANCY: (Pg 9) Do you always wear your hair like that? (Pg 7) Oh, you’re still flat.

MARGARET: Not exactly. I’m small boned, is all.

NANCY: I’m growing already. (sticking out her chest) In a few years, I’m going to look like one of those girls from Playboy.

MARGARET: Well, I didn’t think so, but I didn’t say anything.

NANCY: (Pg 14-16) Oh, listen, Margaret. I want you to join my secret club.

MARGARET: What kind of a secret club?

NANCY: I’ll tell you when school starts.

MARGARET: Later, when I was getting ready for bed, I walked into a closet, thinking it was the bathroom. Would I ever get used to living in this house? Are you there, God? It’s me, Margaret. I met a girl today. Her name’s Nancy. Don’t you think it’s time for me to start growing, God? If you could arrange it, I’d be very glad. Thank you. (Pg 28) On Thursday morning, I got up early, but I had trouble eating. My mother said it was natural for me to feel uneasy on the first day of school. (Pg 29-30) By the time I got to Room Eighteen of the Delano Elementary School, everybody else was busy talking and laughing about summer vacations and new hair styles and all that. The class quieted down in a big hurry when a man walked into the room and wrote a name on the blackboard, Miles J. Benedict Jr.

MR. BENEDICT: That’s me (pointing to the name) I’m your new teacher.

MARGARET: (Pg 33) At two-thirty, Nancy slipped me a note. It said” “Secret club meets today after school my house!” I went to change before going to Nancy’s. (Pg 34) The others were already there. Janie Loomis, Gretchen Potter, and Nancy. (Pg 38) Nancy reminded us that nobody in school was to know anything about our secret club; we all had to solemnly swear. Then we all had to think up a rule. Nancy’s rule was we all had to wear bras. I felt my cheeks turn red. I wondered if the others wore them already. I didn’t think Janie did because she looked down at the floor after Nancy said it. Gretchen’s rule was the first one to get her period had to tell the others all about it. My rule was [that] we meet on a certain day each week.

(Pg 41-42) All through supper I thought about how I was going to tell my mother I wanted to wear a bra. I wondered why she hadn’t ever asked if I wanted one, since she knew so much about being a girl. When my mother came to kiss me goodnight, I said it.

MARGARET: (blurts) I WANT TO WEAR A BRA!

MOM: (pauses, sighs) Well, if you really want to, we’ll have to go shopping on Saturday, okay?

MARGARET: [Boy], was I glad that was over! Are you there, God? It’s me, Margaret. I just told my mother I want a bra. Please help me grow, God. You know where. I want to be like everyone else. (Pg 45-46) First thing on Saturday morning, my mother told my father we were going shopping. [At] the shopping center, we went to the ladies’ lingerie department where my mother told the saleslady we wanted to see a bra for me. The sales lady took one look and told my mother we’d be better off in the teen department where they had bras in very small sizes. My mother thanked the lady and I almost died! (Pg 52-53) [At our next secret club meeting] . . .

NANCY: Well, let’s get to it. We all feel each other’s back so make sure we’re wearing our bras.

JANIE: I got a Gro-Bra

MARGARET: Me too

NANCY: Not me. Mine’s a thirty-two double A. If you ever want to get out of those baby bras, you have to exercise. Like this. (making a fist, and bending her arm at the elbow, she moved them back and forth, sticking her chest way out)I must - I must - I must increase my bust.

MARGARET: We copied her movements and chanted with her.

(Pg 57) Are you there, God? It’s me, Margaret. I just did an exercise to help me grow. Have you thought about it, God? About my growing, I mean. Of course, if you don’t think I’m ready, I’ll understand. Thank you. (Pg 110-112) During the second week in January, Mr. Benedict announced that the sixth-grade girls were going to see a movie on Friday afternoon. The sixth-grade boys were not going to see the movie. Nancy passed me a note. It said: Here we go - the big deal sex (or replace with “reproduction”) movie.

On Friday morning, there was a lot of giggling. Finally at two o’clock, the girls lined up and went to the auditorium. We took up the first three rows of seats. Then the lights went out and we saw the movie.

VOICE FROM MOVIE: Remember, it’s menstroo-ation.

MARGARET: Gretchen, who was next to me, gave me a kick and I kicked Nancy on the other side. We held our hands over our mouths so we wouldn’t laugh. The film told us about the ovaries and how we would soon become women and all that. For days after that whenever I looked at Gretchen, Janie or Nancy we’d pretend to be saying menstrooation. We laughed a lot. One week later, Gretchen got it. (to Mom) (Pg 115) How old were you, Mom, when you got it?

MOM: Uh . . . I think I was fourteen.

MARGARET: Fuorteen! That’s crazy! I’m not waiting until I’m fourteen. (Pg 116) [It wasn’t long after that, that] Nancy and her family went to Washington over Lincoln’s birthday weekend. I got a postcard from her before she got back. It only had three words on it - I GOT IT!!!! There was something wrong with me. I just knew it. Are you there, God? It’s me, Margaret. Life is getting worse every day. I’m going to be the only one who doesn’t get it. Why can’t you help me? Please… let me be like everybody else! (Pg 154) [I decided] I was never going to talk to God again. What did he want from me anyway? I was through with him. (Pg 126-127) On March eighth, I was twelve years old. The first thing I did was sniff under my arms, the way my mother does. Nothing! I didn’t smell a thing. Still, now that I was twelve, I decided I’d better use deodorant, just in case. In school, Mr. Benedict shook my hand and wished me a lot of good luck in the coming year. He also led the class in singing “Happy Birthday” to me. (Pg 155-157) [That afternoon] I asked my mother to drive me downtown to meet Janie for a movie. We were twenty minutes early, so we went into the drugstore on the corner to look around. Mostly we liked to inspect the sanitary napkin display. (to Janie) Let’s buy a box, just in case. (to audience) I took a box of Teenage Softies off the shelf and walked to the check-out counter. Max took my money and presented me with [a] brown bag. That was all there was to it. You’d think he sold that kind of stuff every day of the week. (Pg 158) When I got home I went to my room with my purchase. I sat down on my bed staring at the box of Teenage Softies. I hoped God was watching. Let him see I could get along fine without him! (Pg 169-170) [That night] I had to go to the bathroom. Then, I looked down and I couldn’t believe it. (yelling) MOOOOOM - hey - MOM - come quick! I got IT! (Pg 171) I had to call Nancy and Gretchen and Janie right away. How about that! Now I am growing for sure. Now I am almost a woman! Are you still there, God? It’s me, Margaret. I know you’re there, God. I know you wouldn’t have missed this for anything! Thanks an awful lot!
```

---

## IC-1237: Audition

- Title: Audition
- Author (byline): Jane Martin
- Work: Talking With
- Publisher: Samuel French, Inc.
- Publication date as stated: April 1983
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS
- Teaser before the introduction: Yes
- Spoken words (computed): 828
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jane Martin
Book: Talking With
ISBN: 978-0573630217
Publisher: Samuel French, Inc.
Date (Month/Year): April 1983
```

### Introduction (context only: never use it for content warnings)

```text
In the early stages of her career, when Barbra Streisand was an unknown and hadn’t yet become world-famous, she went to an audition very visibly chewing a large wad of gum. Called to the stage, she chomped on the gum, started to sing a few notes, then stopped and with an abashed and very charming smile she took the chunk of gum out of her mouth and stuck it under a stool seat. Then she sang her songs.

Later, after all auditions were completed and performers had left, a curious director went to the stool and looked at the underside. No chewing gum. Streisand had faked the whole thing.

Why? “The girl who was chewing gum” stood out from all the others. You have to smile and shake your head at that...and remember her forever thereafter.

That may or may not be a true story . . . but it is true that auditions involve many things, including mind games and cunning strategy. No, these “tricks” won’t replace careful preparation and talent, but in a highly competitive world, one seeks whatever advantages one can devise.

Audition by Jane Martin
```

### Performance text (classify this)

```text
An actress in her late twenties runs up on the stage. She is nervous. She shields her eyes against the light. She is dressed in a slightly bizarre and trendy style. She carries in her arms a cat on a leash.

ACTRESS: Hi. Hey Hi. Wow. All Right. Nice place. Nice, uh, nice theatre. Good vibes. Yowsa me yessiree. Toy boat, toy boat, toy boat, toy boat. Now . . . let’s see here. For my . . . can you hear me? Can you? No? Yes? You are out there, right? (She puts the cat on the floor, her foot on the leash) O.K., so we’re all here. Well, I mean, you’re there and I’m here but we’re all. . . forget it.

Let’s see. . . Audition, RAH! Get that part! O.K., my name is. . . s***, I forgot my name. Right. This. . . this would be construed as craziness. My name is. . . I did, I forgot my name. . . my stage name. . . see I decided to use my new stage name for this audition. . . for uh, for luck, it was. . . it was very. . . look what d’you care right? My human, world name is Mary Titfer.

Titfer. You got it? Goodo! O.K., can you hear me? All the way back? Loud and clear Captain Marvel? A-O.K.!

. . . Now, one more introduction and we’re under way. The uh, the small person on my leash is my cat ‘Tat.’ My cat, ‘Tat.’ Get it? (Points to herself) Titfer (Points to cat) Tat. Right, you got it. Hey, we’re waking up here. We’re demonstrating consciousness. O.K., O.K., now you. . . the imperial you. . . have a part. I, Titfer, need a part. We are thus in tune. Synchronicity. Sooooooo, it’s audition city!

Now I’ve got two pieces for you today, and here’s the surprise, I’ve got one classical piece. . . late greats, and I’ve got one contemporary piece. . . dispatches from the front. Good. For my classical piece I will take off all my clothes . . . ‘Crude Rube Protrudes Dubious Boobies.’ Beep-Beep. O.K., O.K., but all kidding and joshing aside I will take them off. Now, why is this classical? Surely, you jest. The body, the body is classical. . . it goes all the way back. . . and all the way front. Har, har. It starts the art, the body does. But there’s no argument there, eh? Naturally not. O.K., O.K., now in the great tradition of auditions you may stop me at anytime. You can stop me one second after I start. But, BUT. . . and here is the stinger. . .

(She takes a hammer out of her purse, and a nail) Bear with me. O.K.? Little hyped-up. A simple task and I’ll be back with you. (She nails the cat’s leash to the floor) There. Tat the cat, that’s that. Nice kitty. Where were we? Toy boat, toy boat, toy boat, toy boat. O.K., stop me at any time. Right, O.K. Just yell. ‘Thank you Miss Tifter.’ Firm but courteous and zaparoonie. . .I stop. I nip the strip. But when I stop my classical piece, I shift immediately into my contemporary piece, which is. . . full attention now. Beating the cat’s head in with the hammer!

Yipes! Holy Mackeral! ‘Is this broad kidding?’ Welllll, I wouldn’t want to spoil it for you but I don’t think she’s kidding. So, dear listeners, that’s the full menu. . . that’s all she wrote. But the tickle in the tushy are the options.

Option A . . . we will let this poor, desperate and deluded girl debase herself. . . and I would, will, be debased. . . mortified. . . I mean. . . no clothes. . . here? In front of strangers? Crummy, yucky, hateful! Or. . .

Option B. . . we can yell out ‘Thank you Miss Tifter’ and watch her clonk the kitty. . . and remember, Miss Tifter is fast. It will happen in a flash. . . kittyplasm . . . and haven’t we, you, ‘fess up now’ actually killed little puss? Responsibility!

Or Option C, the second-to-last option, we could give Mary Titfer the crummy, undemanding, twelve-line, two-scene part, which, let me assure you, any mildly competent average workday actress could do while standing on her head humming, ‘You can take this job and shove it’. . . backwards.

O.K., last option. . . now this is just too tawdry but we are nothing if not thorough. We could give her the part now, and then when she splits, she and the furry hostage, we could take it away from her on the basis that she needs. . . shhh, psychiatric attention. But if you did that. . . if you did that, Mary Tifter would find you and Jacobean revenge, kill the feline, and, perhaps -- disturbing thought -- herself in a particularly garish and oriental manner RIGHT IN FRONT OF YOU. Now she might not have nerve but on the other hand we don’t know. We just don’t know.

O.K., O.K. We’re ready to go in the wooden O. We’re out of the exposition and into the meat of the matter. Denouement. Everybody has their work cut out for them. The dialectic. You have a part. I want a part. We have serious business here. Right? Right. I will begin my classical piece. Watch me closely, both my hands are connected to my arms (She begins to unbutton her blouse as the lights fade out)
```

---

## IC-1238: Beauty Queens

- Title: Beauty Queens
- Author (byline): Libba Bray
- Work: Not specified
- Publisher: Scholastic Paperbacks
- Publication date as stated: June 2012
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MARY LOU, ADINA, TAYLOR, GIRL #1, MISS NEW MEXICO, TIARA, BRITTANI, NICOLE, MISS MONTANA, PETRA, BOSS, AGENT
- Teaser before the introduction: Yes
- Spoken words (computed): 1359
- Already set (do not supply): none

### Source block (context only)

```text
Author: Libba Bray
ISBN: 978-0439895989
Publisher: Scholastic Paperbacks
Date (Month/Year): June 2012
```

### Introduction (context only: never use it for content warnings)

```text
The fifty contestants in the Miss Teen Dream Pageant thought this was going to be a fun trip to the beach, where they could parade in their state-appropriate costumes and compete in front of the cameras. But sadly, their airplane had another idea, crashing on a desert island and leaving the survivors stranded with little food, little water, and practically no eyeliner. What's a beauty queen to do? Continue to practice for the talent portion of the program - or wrestle snakes to the ground? Welcome to the heart of non-exfoliated darkness.

Beauty Queens by Libba Bray
```

### Performance text (classify this)

```text
CAST LIST Tiara / Miss Mississippi
Narrator Brittani / Miss Alabama
Mary Lou / Miss Nebraska Nicole / Miss Colorado
Adina / Miss New Hampshire Miss Montana (no lines)
Taylor / Miss Texas Petra
Girl #1 Boss
Miss New Mexico Agent

NARRATOR: This [story] begins with a plane crash. According to the U.S. Department of Unnecessary Statistics, your chances of dying in a plane crash are one in half a million. Whereas your chances of losing your bathing suit bottoms to a strong tide are two to one. So, all in all, it’s safer to fly than to go to the beach.

As I said, this [story] begins with a plane crash. But there are survivors. They are all beauty queen contestants. They are all such nice, happy, shining, patriotic girls who happen to have interests in baton twirling, sign language, AIDS prevention in the animal population, feminine firearms, interpretive dance, and sequins.

The flight is on its way to a remote tropical paradise where the girls will compete against one another for the title of Miss Teen Dream. And so our tale begins with a sudden fall from blue skies, with screams and prayers . . .

And a camera crew bravely recording every bit of the turbulence and drama: What a lucky break for their show! Ratings will skyrocket!

Through the windows, they can see the strange, verdant land taking shape, growing bigger as they descend. It’s beautiful. They will land safely, no matter the sudden near-vertical descent. They’re sure of it. After all, these are can-do girls from a nation built upon dreams. (Chapter 1)

MARY LOU: Are you all right?

ADINA: Am I dead? (Looks up at Mary Lou standing over her as she lies on the ground) Are you dead?

MARY LOU: No. I’m Miss Nebraska, Mary Lou Novak.

ADINA: Adina Greenberg. Miss New Hampshire.

TAYLOR: (with strong Texas accent). All right, Miss Teen Dreamers! Yoo-hoo! I’m wigglin’ my fingers for y’all’s attention. I’m Taylor Rene Krystal Hawkins, and I’m Miss Teen Dream Texas, the state where dreams are bigger and better. I’m a senior at George Walker Bush High School and I hope to pursue a career as a motivational speaker. (Polite automatic applause from the other girls)

GIRL #1: I want to pursue a career in the exciting world of weight-management broadcast journalism. And help kids not have cancer and stuff.

TAYLOR: Okay, Miss Teen Dreamers, I know we’re all real flustered and everything. But we’re alive. (loud groan from another girl)

GIRL #1: Oh my gosh! Miss Delaware just died!

MISS NEW MEXICO: My head kinda hurts. (Girls gasp…half of an airline serving tray is sticking out of Miss New Mexico’s forehead, forming a canopy over her eyes.). What is it? (She checks to make sure her bra straps aren’t showing.)

TAYLOR: Any of y’all have first-aid training? (Tiara and Brittani’s hands shoot up). Names?

TIARA: I’m Tiara with an A.

BRITTANI: I’m Brittani with an I. I got my Scouting Badge in First Aid.

TIARA: Ohmigosh, me, too! You’re so nice. If it’s not me, I hope you win.

BRITTANI: No, I hope YOU win! (Chapter 2)

ADINA: What we need is a team leader.

TAYLOR: (tosses hair) Judges ready? Hi, y’all. I am Taylor Rene Krystal Hawkins, Miss Texas.

(standing in perfect three-quarters stance, arms at her sides) I have been class president three years in a row, homecoming queen, a National Merit Scholar, and a member of the National Honor Society, and I am a proud, card-carrying member of FAF – Femmes and Firearms. When we get rescued and get to Paradise Cove, America’s gonna be wantin’ to see a pageant. And I do not intend to let them down. So. Starting tomorrow, we’ll be back to working on our dance numbers and our walking, talent, swimsuit, and evening gown presentations, just like nothing ever happened. Thank you.

(Roar of applause)

ADINA: Um, not to be rude or anything, but usually you put it to a vote.

TAYLOR: What are your leadership qualifications?

ADINA: Hello. I am Adina Greenberg, Miss New Hampshire, and I would like to be your team leader. Point A: We need to think realistically. It could be weeks before we’re rescued. I submit that our goal should be survival. We need to find food and potable water. I think we should find some kind of shelter; a cave or something.

TIARA: What if there’s, like, a creature living in the cave? Seriously, I saw this show once where these people were stranded on an island and there were these people who were sort of crazy-slash-bad and there was this polar bear creature running around.

ADINA: (Interrupting) In conclusion, I am great at organizing a team and making things happen. In short, I would make an excellent team leader. Thank you.

TAYLOR: All righty, then. Let’s put it to a vote! All y’all who want to vote for me, Taylor Rene Krystal Hawkins of the Lone Star State, raise your hands. Looks like I’m the winner. (Chapter 4) Teen Dream Misses! My daddy is a general, and I know what he’d say if he were here: (points to jungle) There might be more of us in there. We need to organize a search party. A Miss Teen Dream Recon Machine. (Chapter 2)

*********

NARRATOR: Two teams were organized and, after much debate, names were chosen: The Sparkle Ponies would stay on the beach, tend to the wounded, and try to salvage whatever they could from the wreckage. The Lost Girls would soldier into the jungle in the hopes of finding survivors. (Chapter 2)

The Lost Girls set off down the beach. Taylor led the way. Adina, Petra, Mary Lou and Tiara followed. The jungle gave way to a small clearing. Enormous totems rose next to the trees. With their angry mouths, jagged teeth, and blood-red, pupilless eyes, they were clearly meant to frighten.

*********

MARY LOU: Holy moly . . . You think there might be cannibals here? (They hear something from the jungle)

TAYLOR: Grab whatever you can. Follow my lead. (Taylor holds up 3 fingers, counting down to 1) Now! (Girls launch sticks and rocks at the jungle. Hiss of pain from jungle) Lost Girls, hold your fire.

NARRATOR: A willowy girl stepped out into the open, moaning. Her skin was the same deep brown as the carved figures.

TAYLOR: I’ll try to communicate. (Speaks slowly) Hello! We need help. Is your village close?

NICOLE: My village is Denver. And I think it’s a long way from here. I’m Nicole Ade. Miss Colorado.

TIARA: We have a Colorado where we’re from, too! (swivels hips, spreads arms wide, brings hands together prayer-style and bows) Kipa aloha.

NICOLE: I speak English. I’m American. Did you learn those moves from Barbie’s Hawaiian Vacation DVD?

TIARA: Ohmigosh, yes! Do your people have that, too?

TAYLOR: We’re trying to find survivors. Did you see anybody else out here?

NICOLE: Just a lot of dead chaperones and camera crew. I’m glad to see you.

MARY LOU: What do we do now?

TAYLOR: We should get back and let the others know. It’s just us. We’re the only survivors. We’re on our own. (Chapter 3) ***********(Back on the beach)*************

TAYLOR: All right, Miss Teen Dreamers. Miss Montana? Is that the way a Miss Teen Dream sits, all slutty like that with her hoo-hoo showing?

MISS MONTANA: (Knocks her knees together and yanks down the hem of her skirt)

TAYLOR: Thank you. I’ve got a little bit of bad news: Everybody else is dead. (Gasp from the crowd) (claps) Teen Dreamers! We need to focus like it’s the final interview round and the questions are all about anorexia and current events. Now, I know y’all are upset. This is just plain awful. But God doesn’t make mistakes. Is this a setback, Teen Dreamers?

MISS NEW MEXICO: (Points to tray in her forehead) What about this?

PETRA: You know what would be cute on you? Bangs? So 1960s chic. You’d hardly notice the, um, the… addition.

MARY LOU: Love bangs!

PETRA: Miss Florida was the only one who had bangs and she’s de – um, she’s no longer participating in the pageant system. So you’d really stand out.

MISS NEW MEXICO: Stand out? Stand out! I have a freaking tray stuck in my forehead!

TAYLOR: Miss New Mexico, let’s not get all down in the bummer basement where the creepy things live. There are people in heathen China who don’t even have airline trays. WE have a lot to be grateful for. This is an opportunity for growth and the establishment of your personal brand. Everybody loves a survivor and a Miss Teen Dream contestant. When you put those two together, you have a lot of big endorsement opportunities when we get back. Let’s find a place to camp and look for firewood. Tonight, we’ll keep watch in shifts. (Chapter 4)

NARRATOR: CLASSIFIED. ISLAND. 22:00 Hours . . . Sheltered by the dark, the agent watched the girls sleeping on the beach and shook his head. This was not good, not at all. (Picks up phone and dials) *********

BOSS: This better be good.

AGENT: We’ve got a problem.

BOSS: Agent Jones, in six weeks, Operation Peacock is a go. Nothing can interfere. Nothing. A rescue mission to the island will mean attention. We don’t want attention.

AGENT: I understand. What about the girls?

BOSS: Six weeks is a long time, Agent. And it’s a hostile island. They’ll be lucky to last two days. The official word is that there were no survivors. Operation Peacock goes on as scheduled. (Chapter 5)
```

---

## IC-1239: Bernice Buttman, Model Citizen

- Title: Bernice Buttman, Model Citizen
- Author (byline): Niki Lenz
- Work: Not specified
- Publisher: Random House Books for Young Readers
- Publication date as stated: Mar 2019
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: BERNICE, OLIVER, OLVIER, MOMMA, GINA, MS. KNIGHTLEY, MR. NEWTON, IMOGENE, FRANCIE, PRINCIPAL JENKINS, STUDENT, STUDENTS
- Teaser before the introduction: Yes
- Spoken words (computed): 1763
- Already set (do not supply): none

### Source block (context only)

```text
Author: Niki Lenz
ISBN: 978-1524770419
Publisher: Random House Books for Young Readers
Date (Month/Year): Mar 2019
```

### Introduction (context only: never use it for content warnings)

```text
When you're a Buttman, the label "bully" comes with the territory, and Bernice lives up to her name. But life as a bully is lonely and if there's one thing Bernice really wants, it's a friend. After her mom skedaddles and leaves her in a new town with her aunt (a real live nun!), Bernice tries to mend her ways and start over. But it's hard to be kind when no one shows you kindness, so a few pranks may still be up her sleeve as she works on becoming . . .

Bernice Buttman, Model Citizen by Niki Lenz
```

### Performance text (classify this)

```text
BERNICE: (Chapter 1) Here are things that I, Bernice Buttman, was awesome at. One: burping the alphabet. Two: blowing up stuff with firecrackers. Three: wearing the teachers and puny kids of Oak Grove Elementary into nubs. I was less great at knowing what to do with myself at recess.

I sat on top of the monkey bars, feeling like a booger on a cheese ball . . . out of place and unwelcome. Kids whirled all around me, talking to their buddies and playing games, but nobody came within arm’s length of me.

BERNICE: There was only one kid who I didn’t want to clobber: (dreamily) Oliver Stratts. He was real smart and smelled like laundry detergent. I wanted him to be my friend. It was time to put my plan in action -- my feet marched me over to the group of snotnosed fifth graders. The kids went quiet. I grabbed one of Oliver’s skinny arms and twisted it behind his back. (he squeals) (in a sweet voice) Come with me. I’ve got a present for you.

(to audience) I found the pile of dog doo I’d spotted earlier, and I pushed Oliver’s face right up next to it. (to Oliver) How would you feel about me and you being friends, Oliver?

OLIVER: (squirming to get away and avoid the poo) No way!

BERNICE: He tried to squirm out from under me, but I outweighed him by about a million pounds. All I had to do was lean forward a smidge, and his nose would touch poo.

OLIVER: (squeaking through gritted teeth) Oh, gosh! Oh, man. Let me up, Bernice!

BERNICE: I’ll be glad to. When you say you’ll be my friend.

OLIVER: (whining) Okay, okay, fine.

BERNICE: (to audience) I stood slowly and gave Oliver’s backside one tiny kick, sending him sprawling only one beardsecond away from the pile of dookie. (A beard-second is the average length a beard grows in one second. Google it.)

OLVIER: (running away) You need Jesus, Buttman! You’re the meanest girl I know!

BERNICE: Too bad for you, ’cause I’m your new best friend!

MOMMA: (at the schoolyard fence) Bernice! Bernice Buttman, get your raggedy behind over here right this minute!

BERNICE: (reluctantly going to the fence) What are you doing here? (to audience) Momma was wearing pajama pants and slippers, even though it was eleven o’clock.

MOMMA: Imma need my money back.

BERNICE: (scowling) What money?

MOMMA: The money I gave you this morning for your lunch.

BERNICE: But I need that money to eat! (to audience) All the kids were staring and pointing and laughing.

GINA: Did you see how many chins that woman had? I’ll betcha Bernice will look just like her when she’s grown.

OLIVER: I heard they steal toilet paper from the gas station bathroom.

BERNICE: Not him! The rest of the kids could talk, but not my best friend!

MOMMA: (throwing her hands in the air, frustrated) Figure something out. Now cough up the cash. I gotta put gas in the car and get to my tattoo appointment.

BERNICE: (Chapter 7) I drifted through the following days like a Twinkie wrapper blowing through a parking lot. I tried to avoid Momma as much as possible, [but] she caught me Saturday morning.

MOMMA: I need to talk to you, Bernice.

BERNICE: I was only 11 years old, but when someone tells you they need to talk, it’s never about how they wanna shower you with candy.

MOMMA: I’ve decided I need to make a move. For my career.

BERNICE: (puzzled she thinks aloud) Career?

MOMMA: There’s these open auditions in Los Angeles. This could be my big break!

BERNICE: (excited) We’re movin’! To California? Hotdang! Swimming pools, movie stars!

MOMMA: No, Bernice. Your brothers will stay here. They can take care of themselves. But you require some supervision. (crosses her arms in a no-nonsense way) You’re gonna go live at Aunt Josephine’s.

BERNICE: (to audience) My face must have gone as white as a sun-bleached dishrag. (to Momma) Wait. . . isn’t she a nun? ***** Scene – At the Library*****

BERNICE: (to audience) She tried to tell me it would be temporary. As soon as her and Lloyd got jobs on a TV show, they’d come back for me. I laid my face down on the table and squeezed my eyes shut. One traitor tear managed to squeeze out.

MS. KNIGHTLEY: Bernice? What on earth is the matter?

BERNICE: Ms. Knightley, *our librarian*, was the closest thing I had to a friend. She always seemed happy to see me, and she didn’t think of me as “one of those awful Buttmans.” (to Ms. Knightley, wailing) My momma is giving me away. To live with my aunt in a dumb small town. And she’s a nun! (beat) She can’t make me! I’ll figure out a way to stay!

MS. KNIGHTLEY: But what if you didn’t stay here. What if you did go live in a new town with new people? (pause) Bernice, I know you may not believe what I’m about to say, but this might be the best thing that’s ever happened to you. (smiling softly) Going to live in a new place is starting over. It’s like a clean slate. Sometimes it’s the people around us who help us figure out who we are.

BERNICE: (crossing arms dejectedly) I already knew who I was. Bernice Buttman. Cheese ball eater. Kindergarten money stealer. School terrorizer. Mini-version of my momma. (sadly) But was that who I had to be? Who I wanted to be? What if Ms. Knightley was right -- A new beginning. A new adventure. ***** Scene – At her new school – Halfway Primary School*****

BERNICE: (Chapter 10) I’m so nervous I don’t know whether to scratch my watch or wind my butt. (Chapter 9) I kept telling myself things could be different in Halfway. No one knew me, or my family. I’d never threatened to push anyone’s nose in dog doo here or stolen any milk money. (pause, knocks on the classroom door and steps inside) The first person I saw when I walked into Mr. Newton’s 5th-grade class was Mr. Newton himself.

MR. NEWTON: Bernice Buttman?

BERNICE: (to audience as an aside) Shoot. Permanent file. So much for forging a new identity.

IMOGENE: (eagerly raising her hand) Mr. Newton? Excuse me, Mr. Newton? Would you like me to show Bernice Buttman around?

BERNICE: (rolling her eyes) I managed to stay mostly invisible for the first part of the day. [But] before I knew it, the lunch bell rang.

IMOGENE: (with too much enthusiasm) I can’t wait to show you all around, Bernice. I promise to do whatever it takes to make you feel welcome here. (with fake surprise and batting her eyelashes) Oh, Principal Jenkins, I didn’t see you there.

FRANCIE: (Chapter 13) (whispering to Bernice) She’d bring muffin baskets to his house once a week if she thought it would help her get the Principal’s Citizenship Award.

BERNICE: What’s the Principal’s Citizenship Award?

FRANCIE: It’s this award they give out to one fifth-grade kid each year. If you win you get a thousand dollars and a trip to Jefferson City to meet the governor.

BERNICE: Bernice Buttman was not the kind of girl who won citizenship awards. I was the kind of girl who kicked those prizewinners in the shins. [But then] A lightbulb turned on in my brain. I knew exactly what to do. (to Principal Jenkins, matching Imogene’s fakeness) Mr. Jenkins? (offering her hand to shake) I live at St. Drogo’s with the nuns . . .

PRINCIPAL JENKINS: Yes. Sister Marie Francis says you’ve been quite the blessing to them. And how wonderful that you’ve taken an interest in helping the poor.

BERNICE: I consider myself a global citizen, sir. Always looking out for others. (Jenkins moves on)

IMOGENE: (indignant, and not so nice now) If you’re talking about getting the Principal’s Citizenship Award, you can forget it. I’ve been volunteering after school to prove to everyone how good a citizen I am. Living with nuns doesn’t make you good.

BERNICE: (sweetly) I don’t care if I win any dumb awards. But it sure would make me happy if you didn’t. (Imogene stomps off) (to audience) Maybe I could treat this whole “being nice” thing like it was a part I’d been assigned. Like acting. Yeah. Be nice. It was harder than it sounded.

(Chapter 19) It was the Monday after Thanksgiving break when the idea hit me. (rubbing her hands together and cackling) I sat at my computer and typed a professionally worded letter of congratulations, sealed it in a long white envelope. I got to class early and placed the letter on Imogene’s desk before anyone else arrived.

IMOGENE: (notices the envelope, opens it and smiles as she reads, her hand shoots into the air) I have an announcement! It’s really exciting! (walks to the front of the room, beaming)

BERNICE: (to audience) She had rays of sunbeams shining out her nostrils, I tell you what.

IMOGENE: Everyone, I just received confirmation that I’ve been chosen for the Principal’s Citizenship Award. (squeals) It says . . . and I quote: “Imogene Franklin is the most model student at Halfway Primary. She expresses her love of the community by constantly sucking up to teachers and having her father write bit checks to charity.”

(her smile sags)

STUDENT: Sounds about right! (laughing)

IMOGENE: (continues reading with some confusion) “The recipient of this special award will get to run extra laps in PE for the rest of the school year.” That doesn’t seem right.

MR. NEWTON: Take this letter to the principal immediately so [he] can verify its validity

STUDENTS: (giggling)

BERNICE: (gleefully) You could see the wheels turning in Imogene’s brain as she walked to the classroom door. She paused with her hand on the knob and turned slowly, glaring at me. She was mad enough to eat barbed wire and poop nails. I should’ve been happy . . . I mean, Imogene had thought so much of herself . . . And she had announced it to the whole class and everyone had laughed at her. Added bonus. But it didn’t matter if you were squashing people or writing them fake awards, eventually you got caught and you had to pay the price for bullying. (Chapter 23) I should’ve known Momma would show up (beat) . . . at church! ******Scene******

MOMMA: Bernice! Honey, let’s get out of here. I’m gonna take you out for some fried chicken.

BERNICE: (horrified) What’re you doin’?

MOMMA: Look at you, living like a woman of the cloth. Do they got you praying ten times a day and shining up their crucifixes?

BERNICE: (embarrassed, she speaks to the congregation) Everything’s a joke to her.

MOMMA: I’ve come to fetch you. California didn’t work out for me.

BERNICE: (Chapter 18) What would Ms. Knightley tell me to do?

MS. KNIGHTLEY: (Chapter 7) (echos) Going to live in a new place is starting over. It’s like a clean slate. Sometimes it’s the people around us who help us figure out who we are.

BERNICE: (with conviction) [I am not a] Kindergarten money stealer. School terrorizer. Mini-version of my momma. (Chapter 25) When you are raised to only think about yourself and getting what you want, you don’t turn out to be a very nice person. (beat) (Chapter 26) There were a lot of good things about living in Halfway. ******Scene – a few week after Momma leaves*****

BERNICE: (Chapter 28) The town square was busy, even for a Saturday afternoon, and when I rounded the corner I saw a herd of small kids running around the courthouse lawn. Only one voice attempted to calm the chaos.

IMOGENE: Everyone, sit down. Sit down now! We need to start our program.

BERNICE: Did you start your own day care or something?

IMOGENE: This is a day camp I organize. I watch the children so their parents can shop. The Halfway Chamber of Commerce said it was the best service project ever. It shows what a good citizen I am.

BERNICE: I thought you already got that award.

IMOGENE: (glaring) Can you leave now, so I can get them to come back to the grass.

BERNICE: (to audience) My eyes narrowed at the scrunched-up set of Imogene’s shoulders, and something inside me went mushy. (to Imogene) I have a better idea. How ’bout I stay and help you? (to audience with pride) I spent the afternoon helping the citizens of Halfway. And I didn’t expect anything in return. (strikes a super-hero pose) Bernice Buttman – Model Citizen!
```

---

## IC-1240: Blown Sideways Through Life

- Title: Blown Sideways Through Life
- Author (byline): Claudia Shear
- Work: Not specified
- Publisher: Dell Publishing Company, Inc
- Publication date as stated: April 1996
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CLAUDIA, MANAGER, PIERRE, BARBARA, ANOTHER WAITER
- Teaser before the introduction: Yes
- Spoken words (computed): 1295
- Already set (do not supply): none

### Source block (context only)

```text
Author: Claudia Shear
ISBN: 978-0385313155
Publisher: Dell Publishing Company, Inc
Date (Month/Year): April 1996
```

### Introduction (context only: never use it for content warnings)

```text
If life were a stable career path, Claudia Shear didn’t just miss the memo; she used it to light a cigarette on her way out of yet another job. Ricocheting between gigs like a human pinball, she hustles through it all with a world-class eye-roll and absolutely no illusion of job security.

And then . . . she found waitressing. The glamorous arena where “May I take your order, madam?” really means “Please don’t emotionally unravel over the soup of the day.”

It’s a chaotic parade of low-wage survival jobs where dignity is optional, sanity is negotiable, and every shift feels like a social experiment. But don’t worry, customers -- Claudia’s got a few tips to help you behave like a decent human while the waiters and waitresses talk about you behind your back.

Blown Sideways Through Life by Claudia Shear
```

### Performance text (classify this)

```text
CLAUDIA: (Pg 1-4) It's 3 o'clock and I'm sitting on a bench putting on a pair of cop shoes . . . It's Wednesday at 11 A.M. and I'm pulling on thick janitor's gloves and picking up a bucket. . . It's 4:15 in the morning and I'm trying to take a nap in a bathroom on Wall Street by balancing my head on the toilet-paper roll. . . I fasten on a phone headset. . . .

And then I carry up cases of beer, tubs of chicken, stacks of documents, flats of eggs, trays
of lipsticks. I set up the computer, the desk, the stock. I read the documents, chop the
onions, wash the walls, wash the dishes, answer the phone, answer the phone, answer the
phone. (answering phones)
• "Good afternoon, Battle, Fowler, Jaffin and Kheel. . . "
• "Good morning, Shakespeare Festival. . ."
• "Buona sera, Le Madri. . . "
• “Medical Center Patient Information, what room, please?"
And they tell me . . . (various boss voices)
• "Chill on the conversation."
• "Be nice to the customers!"
• "Put your book away! No reading allowed!"
• "Here's a club in case they come to rob the restaurant when I'm not here."
• "Remember to always give your name."
• "Never give your name!"
And then, later, I hear, (various boss voices)
• "Uh, there's been complaints about your attitude."
• "You were heard whistling in the elevator. . . "
• ". . . singing in the dining room . . ."
• "You talk too much . . ."

• "Your laugh is too loud. . . "
• "No standing around! Look busy!"
And my personal favorite: "I don't have to give you a reason. It's my restaurant!"
And finally: (various boss voices)
• "Listen, we're going to have to let you go. . . "
• "Oh, this is your last shift."
• "Well, it's my way or the highway."
• "You're fired!"
And every time I just say, (with growing frustration) "All right, all right, all right."

CLAUDIA: (Pg 5-6) I'm from Brooklyn. Enthralled by the incredible glamour of the bad kid, I tried to keep up, running from cop cars with the friends I carefully chose -- girls like Janine Morelli, who was mean and punched me like a boy -- or hanging out in a park on Avenue P. Oh, God, did I want "in." In with Kathleen and Debby and Ronnie, skinny girls in shiny fabrics who bit their nails and painted them anyway.

We were tough. We "hung out." [But] I was a prime target. God knows how they knew I was different. I smoked and cursed and fought and stuffed my bra with tissues. But the part of me that still believed in Narnia and cried for Black Beauty must have somehow given me away.

(Pg 8) Back in my basement in Brooklyn I read books that ranged from The Divine Comedy to Book-of-the-Month Club selections of the late 1950s. I read anything I could get my hands on. A misfit in Flatbush, I wanted out so badly, I wanted to fit in so much:

(Pg 10-11) Inside my head there was romance: running through the Highlands with Alan Breck, Crusoe on a desert island, atop a magic mountain, astride a horse with wings. I wanted adventure. A cottage in the woods with the enchanted sword. The search for the Holy Grail. The trials of the hero. All for the quest! Inside my head I was suffering and striving in great feats of strength and ennobling tests of character. This was the plan of my life, the concept perfectly framed.

But what actually was my life?

At last count I've had 65 jobs, and some of them of unusually short duration, the briefest being at a restaurant called Bar Lui: Got hired. Went to work. Drank an iced coffee. Made a few phone calls. After about 10 minutes the manager interrupted me.

MANAGER: Um, we have very specific policies regarding personal calls. . .

CLAUDIA: (to manager) Oh, please! You must be kidding. (to audience) So I got my coat, got my keys, my token, my ticket, my passport, my cash card, and I hit the road, Jack. Out the door on a subway, a train, a plane, a bus. Walking to an address, a comer, a park, a bar, life can spin on a dime. (beat)

(Pg 31) Waitering. What a way to make a living. It's prison, voluntary incarceration, as we line up in the kitchen at 3 P.M. for the "family meal," pushing our trays along, food dumped on our plate at each station. One of the waiters jokingly asks for "a breast, please, Warden!" and the line of guys in white shirts and ties, order books in breast pockets, shout with laughter. I am the only woman.

(Pg 32-33) Aspiring actors work alongside people who are supporting families alongside dedicated party animals who love the hours and the cash. Unusual people waiter. My friend Bill, a young actor, worked in a French restaurant. One night, while waiting at the bar, he overheard Barbara, the bartender, ask one of the other waiters, a French guy named Pierre, to get her some milk from the kitchen for a cocktail.

PIERRE: (with a panicked expression) Oh, Please. No!

BARBARA: What? I'm swamped. Just get me some milk!

PIERRE: (shaking his head) I am so sorry, Barbara, but I really cannot. (backing away)

BARBARA: Will someone please tell me what is going on?

ANOTHER WAITER: Well, Pierre, he has a problem. He is scared of milk. He cannot touch milk. It makes him afraid to be near it.

BARBARA: (laughing) Scared of milk?

ANOTHER WAITER: It is serious. He truly has fear of milk ... and carrots.

CLAUDIA: (Pg 35 - 37) Out on the floor it's the front lines, it's a war, and the waiters are caught between two flanks -- customer and management. Comrades-in-arms, we share a look across a table, shield each other from the manager as we surreptitiously pry a broken cork out of a wine bottle. We are in this together. We lean against a wall and engage in "waiter conversation": two people side by side but never looking at each other, mouths hardly moving, eyes scanning the room for the lift of a beckoning hand. You are expendable, the smallest slip can lead to the freefall of unemployment. Survival is all.

Tips for Waiters 1. Wear cop shoes. As a waiter your entire consciousness is centered in your feet. Cop shoes are strong, cheap, and give you a certain clomping authority. 3. Get retractable pens. You'll lose the top to any other kind, get Rorschach stains on your uniform shirt, and your manager will force you to buy a new one. 4. Get the best busboy. Bribe him if you must. 5. Avoid the VIP tables. Waiting on Warren Beatty is far more trouble than it's worth. At first it's kind of a thrill, but then it's just another table that wants more water and bread, wants to hear the "specials" again, only worse, because the manager is breathing down your neck, dying for an excuse to meet a star. Tips for Customers 1. Never touch the waiter. Even if you think you are being nice, that you have a great rapport, think how shocking it would be if the waiter touched you. 2. Don't ask personal questions. I've been asked questions by customers that even my mother wouldn't ask me. 3. Order dinner without commentary. We aren't interested if you like chicken, hate carrots, never eat white flour. Simply tell us what you want. 4. Finish chewing before you talk to the waiter. We'll wait. Really. 5. Don't snap your fingers. 6. Don't call the busperson "Pedro" or "Ahmed" or "Consuelo." Or any other name you think might be his or hers because of nationality. 7. Don't mention the tip. As in "Listen, take good care of us and you'll get a really good tip." 8. Don't complain to the manager. Restaurants are tough places, so know that if you complain, it means the subject of your criticism will be fired. FIRED. Out the door.

(Pg 4) (various boss voices)
• "Listen, we're going to have to let you go. . . "
• "Oh, this is your last shift."
• "Well, it's my way or the highway."
• "You're fired!"

CLAUDIA: (with growing frustration) "All right, all right, all right."
```
