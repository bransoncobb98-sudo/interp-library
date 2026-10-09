# Classification request: batch 43 of 53 (40 records, IC-2081 to IC-2120)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-043-reply.json`.

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

## IC-2081: The Math Curse

- Title: The Math Curse
- Author (byline): Jon Scieszka
- Work: Not specified
- Publisher: Viking Children's Books
- Publication date as stated: October 1995
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MRS. FIBONACCI, RUSSELL, MOLLY, SISTER, MOM, DAD, MR. NEWTON
- Teaser before the introduction: No
- Spoken words (computed): 1395
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jon Scieszka
ISBN: 978-0670861941
Publisher: Viking Children's Books
Date (Month/Year): October 1995
```

### Introduction (context only: never use it for content warnings)

```text
Did you ever wake up to one of those days where everything is a problem? You have ten things to do, but only thirty minutes until your bus leaves. Is there enough time? You have three shirts and two pairs of pants. Can you make one good outfit? Then you start to wonder: Why does everything have to be such a problem? Why do two apples always have to be added to five oranges? Why do four kids always have to divide twelve marbles? Why can’t you just keep ten cookies without someone taking three away? Why? Because you’re the victim of . . .

The Math Curse by Jon Scieszka
```

### Performance text (classify this)

```text
NARRATOR: On Monday in math class, Mrs. Fibonacci says

MRS. FIBONACCI: You know, you can think of almost everything as a math problem.

NARRATOR: On Tuesday I start having problems. I wake up at 7:15. It takes me ten minutes to get dressed, fifteen minutes to eat my breakfast, and one minute to brush my teeth. Suddenly, it’s a problem: If my bus leaves at 8:00, will I make it on time? How many minutes in one hour? How many teeth in one mouth?

I’m getting a little worried. Everything seems to be a problem.

I take the milk out for my cereal and wonder: How many quarts in a gallon? How many pints in a quart? How many inches in a foot? How many feet in a yard? How many yards in a neighborhood? How many inches in a pint? How many feet in my shoes?

I don’t even bother to take out the cereal. I don’t want to know how many flakes in a bowl.

Mrs. Fibonacci has obviously put a MATH CURSE on me. Everything I look at or think about has become a math problem.

I TRY to get on the bus without thinking about anything, but there are five kids already on the bus, five kids get on at my stop, five more get on at the next stop, and five MORE get on at the last stop. True or false: What is the bus driver’s name?

Mrs. Fibonacci has this chart of what month everyone’s birthday is in: Which month has the most birthdays? Which month has the fewest? Why doesn’t February have a w? Do you ever look at clouds and think they look like something else?

The whole morning is one problem after another. There are 24 kids in my class. I just know someone is going to bring in cupcakes to share. We sit in four rows with six desks in each row. What if Mrs. Fibonacci rearranges the desks to make six rows? Eight rows? Three rows? Two rows? I count the 24 kids in our class again, this time by two’s.

Jake scratches his paper with one finger. How many fingers are in our class? Casey pulls Eric’s ear. How many ears are in our class? The new girl, Kelly, sticks her tongue out at me. How many tongues in our class? I’m about to really lose it, when the lunch bell rings.

Unfortunately for me, lunch is pizza and apple pie. Each pizza is cut into eight equal slices. Each pie is cut into six equal slices. And you know what that means: fractions. If I want two slices of pizza should I ask for: one-eighth? Two-eighths? Or two slices of pizza? What is another way to say one half of an apple pie? Two-sixths? Three-sixths? Or la moitiẻ d’une tarte aux pommes? Which tastes greater? Half a pizza, or half an apple pie? We haven’t studied fractions yet, so I take twelve carrot sticks three at a time and eat them two at a time.

In the afternoon, every subject is a problem. Social studies is a geography problem. The Mississippi River is about four thousand kilometers long. An M&M is about one centimeter long. There are one hundred centimeters in a meter, and one thousand meters in a kilometer. Estimate how many M&Ms it would take to measure the length of the Mississippi River. Estimate how many M&Ms you would eat if you had to measure the Mississippi River with M&Ms. Bonus: Can you spell Mississippi without any M&Ms?

English is a word problem. If mail plus box equals mailbox: Does lipstick minus stick equal lip? Does tunafish plus tunafish equal fournafish?

Physical education is a sports problem. In 1919, Babe Ruth hit 29 home runs, batted .322, and made $40,000. In 1991, the average major league baseball player hit fifteen home runs, batted .275, and made $840,000. circle the correct answer: Babe Ruth is less than the average modern baseball player, Babe Ruth is greater than the average modern baseball player, or Babe Ruth is equal to the average modern baseball player.

Math is just a total problem. Mrs. Fibonacci says there are many ways to count. She asks us to give some examples.

RUSSELL: (counting on his fingers) 1,2,3,4,5,6,7,8,9,10.

MOLLY: 2,4,6,8,10…

MRS. FIBONACCI: I always count 1,1,2,3,5,8,13. . . But on the planet Tetra, kids have only two fingers on each hand. They count 1,2,3,10. . . And on the planet Binary, kids have only one finger on each hand. They count 1,10 . . .

NARRATOR: Do you think Mrs. Fibonacci has been to the planet Tetra? How would you bowl if you lived on the planet Binary?

We are just about to go home when Rebecca remembers the special birthday cupcakes her mom made. There are 24 kids in the class. Rebecca has 24 cupcakes. So what’s the problem? Rebecca wants Mrs. Fibonacci to have a cupcake, too. Everyone is going crazy trying to figure out what fraction of a cupcake each person will get. I’m the first to figure out the answer. I raise my hand and tell Mrs. Fibonacci I’m allergic to cupcakes. Everyone (24) believes me and gets one (1) cupcake. No one (0) has to figure out fractions.

I stagger out of school. I’m a math zombie now. I have to find something to break this math curse. I decide to try chocolate. My favorite candy bar is usually fifty cents. But guess what? Today it’s on sale for 50% off. I decide to buy licorice instead.

I pull out my money. I have a five-dollar bill, a one-dollar bill, a quarter, and a penny. George Washington is on both the quarter and the one-dollar bill. Abraham Lincoln is on both the penny and the five-dollar bill. So which is true? One Washington equals 25 Lincolns, five Washingtons equal one Lincoln, one Washington equals one hundred Lincolns, or one Lincoln equals twenty Washingtons? Don’t forget to show your work. Extra credit: How do you think Thomas Jefferson feels about all of this?

I am now a raving math lunatic. What if this keeps up for a whole year? How many minutes of math madness would that be?

SISTER: What’s your problem?

NARRATOR: (snarling) 365 days times 24 hours times 60 minutes! (to audience) Dinner brings no relief. While passing the mashed potatoes, Mom says . . .

MOM: What your father says is false.

NARRATOR: Dad helps himself to some potatoes and says,

DAD: What your mother says is true.

NARRATOR: I think about that for a minute. If what Mom says is true, then what Dad says is false. But if what Dad says is false, then what Mom says isn’t true. And if what Mom says isn’t true, then what Dad says isn’t false. But that can’t be true because he says that what Mom says is true, and she says that what he says is false.

Can that be true? I think about that. Then I think about it some more. Then I think I’d better go to bed.

I undo eight buttons plus two shoelaces. I subtract two shoes. I multiply times two socks and divide by three pillows to get five sheep, remainder one, which is all I need to count before I fall asleep.

Then the problems really begin.

I dream I’m trapped in a room with no doors and no windows. The room is covered with a lifetime of problems. I have only one piece of chalk. How do I get out? I’m about to give up and die, when the answer to my problem comes to me. Fractions. I break the chalk in half. Then I put the two halves together. One half plus one half equals one whole. I put the hole on the wall and jump out. I’m free.

I wake up Wednesday morning at 7:15. It takes me ten minutes to get dressed, fifteen minutes to eat my breakfast, and one minute to brush my teeth. My bus leaves at 8:00. What time will I be ready? 7:41. No problem.

I’ve broken the math curse. I can solve any problem. And life is just great until science class, when Mr. Newton says,

MR. NEWTON: You know, you can think of almost everything as a science experiment. . .
```

---

## IC-2082: A Memory Magically Interrupted

- Title: A Memory Magically Interrupted
- Author (byline): Robert LeLeux
- Work: Not specified
- Publisher: The New York Times (Modern Love Column)
- Publication date as stated: March 20, 2009
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1419
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert LeLeux:
ISBN: Newspaper
Publisher: The New York Times (Modern Love Column)
Date (Month/Year): March 20, 2009
Link to full text:
https://www.nytimes.com/2009/03/22/fashion/22love-
1.html
NOTE: The New York Times (On-Line) is a approved
NSDA website
```

### Introduction (context only: never use it for content warnings)

```text
A Memory Magically Interrupted by Robert LeLeux
```

### Performance text (classify this)

```text
“Your grandmother has Alzheimer’s, right?” the doctor asked me, scrawling notes.

I hadn’t expected to discuss my grandmother’s Alzheimer’s with him. I was hoping to hear some explanation as to why, apart from her memory, my grandmother’s overall health seemed so mysteriously improved. Her lupus, for instance, had all but disappeared from her blood work.

“Yes, but ...”

(Interrupting) “Well, there is a theory that people with Alzheimer’s heal themselves of their diseases. Because they forget they have them.”

I glanced across the room at my beautiful grandmother, smiling vaguely in her lipstick-pink trench coat. “But you don’t really believe that?” I asked.

The doctor shrugged with an implicit “Who knows?” which I found irritating. I hadn’t flown all the way from Manhattan to Nashville to discuss fanciful theories. I wanted solid answers about JoAnn’s health, and he’d thrown me with his talk of miracle cures.

But by that evening, after I’d driven my grandparents home, I realized that the real reason this doctor had startled me was that for the first time I’d heard someone confirm my experience of my grandmother’s disease. Alzheimer’s has, in a sense, healed my grandmother, and our family.

Despite my family role of bulldog journalist, responsible for sniffing out facts, I’ve always preferred fairy tales to literal truth. And I wonder if that isn’t a better way (in my family’s case, anyway) to approach Alzheimer’s, a malady that for us has had a decided fairy tale ring to it, one of those stories where a beautiful lady is cast under a wicked spell that makes her lose her whole life — only to get it back again, better than ever, by the closing paragraph.

Five years ago, when JoAnn’s Alzheimer’s was first diagnosed, I couldn’t imagine anything less fair. At the time, I composed a mental list of all the people I knew who could lose their minds without anybody noticing, scores of people whom I’d never heard say one original thing. While my grandmother, on the other hand, always seemed poised with a staggering, stiletto quip.

As a young artist in New York, I’d spent years trying to find my voice. When I did, it was my grandmother’s. To this day, I’ve never liked anything I’ve created that didn’t somehow remind me of her. I was finding my voice just as she was losing hers.

The only certainty about Alzheimer’s is that it’s characterized by uncertainty: There is no definitive test, no definitive diagnosis. But in July several years ago, after undergoing a gruesome but unserious operation, my grandmother began to exhibit signs of the disease. It was as if her anesthesia never lifted. My grandmother grew ever more foggy, sometimes hilariously so.

“The wonderful thing about Alzheimer’s,” she would say, unfurling her arm like Bette Davis, “is that you always live in the moment.” Humor was the way she had coped with every unpleasant thing in her life, from her long estrangement from my mother, her only child, to the onset of a crippling disease.

But while my grandmother was able to laugh at her decline, her husband couldn’t. He didn’t find anything funny about watching her forget their life together. I think all my grandfather ever wanted was to be left alone with his wife — a goal he’d finally accomplished after more than 40 years of marriage.

My grandparents reminded me of the Reagans, one of those couples who are so gaga for each other that there is no room for the kids. It’s nobody’s fault. It’s just that perfect couples rarely have happy families. They have to have children, because they love each other too much not to make something of it. But then, the honeymoon never ends, and who brings their children on a honeymoon? It’s like they always say: two’s company, and three’s an angry kid like Patti Davis, desperate for attention, with a complex about being shoved outside the magic circle.

Except that in our case, Patti Davis was my mother — a Scarlett O’Hara for the silicon age. Between these two genteel Southern ladies, our family became an Old West town: It just wasn’t big enough for both of them.

Which meant that my grandfather, Alfred, adoring JoAnn as he did, not only stopped speaking to his daughter, he even stopped speaking about her, at least with me. Until the day when we were finally forced to accept JoAnn’s Alzheimer’s and its awful progression.

The more JoAnn forgot, the more often Alfred asked me to visit. And at the end of one of these weekends, as my grandfather wound his Buick through the dark hills on the way to the airport, he suddenly blurted, “Sonny, I think it’s time your mother came home for a visit. I think it’s time your mother came home.”

“I’ll make it happen,” I mumbled. Of course, I had no idea how I would make it happen. Fortunately, my mother was newly sober, and I took advantage of that narrow window of Alcoholics Anonymous time before making amends becomes a crashing bore. All that summer, I begged her long distance. I swore that if she would only visit her parents one more time, everything would be different. Finally I played my ace: I asked her to visit them for my birthday in September.

“Damn it,” she screeched. “So now if I don’t go, I’ll be ruining your birthday? Fine. I’ll do it. But prepare yourself for disaster.”

“There won’t be any disaster.”

“Oh, really? Give me one good reason why things will be different this time.”

“Alzheimer’s.”

For my grandfather and me, having to witness JoAnn’s Alzheimer’s had been agonizing — like watching “The Miracle Worker” backward. Every day seemed accompanied by a new limitation. But for my grandmother, the disease had seemed liberating. For the first time in all the years I’d known her, she seemed truly happy.

Imagine: to be freed from your memory, to have every awful thing that ever happened to you wiped away — and not just your past, but your worries about the future, too. Because with no sense of time or memory, past and future cease to exist, along with all sense of loss and regret. Not to mention grudges and hurt feelings, arguments and embarrassments.

And that’s the fantasy, isn’t it? To have your record cleared. To start over again.

There had always been an element of existential fury to my grandmother’s barbed wit. But as her Alzheimer’s advanced, she forgot to be angry. And she seemed healthier, too: her pace quickened, her complexion brightened, her hair thickened. Her transformation was magical and unmistakable.

It was certainly unmistakable to my mother on that bracing September day when my grandparents and I picked her up at the airport. “Look, JoAnn,” Alfred said, “it’s Jessica.”

“Isn’t that funny,” said JoAnn, before embracing my mother. “That’s my daughter’s name, too.”

My mother forced a smile and shot me a wary look that abruptly softened once we got to the Buick and my grandmother reached for her hand. “Tell me all about yourself, darling,” she said. “I want to know everything about you.”

All through my birthday dinner that evening, JoAnn positively doted on her daughter — beaming sweetly and patting her hand. This behavior unsettled my mother. “Who are those people, Robert? And what have they done with my mother? Because believe me, if that nice old lady had been my mother, I’d never have left home.”

During the following week, the starchy blue autumn skies remained clear, and so did the irony. Now that my grandmother had, in a way, disappeared, she was fully present to my mother for perhaps the first time in their relationship. Now that she was all but unreachable, she was finally available. Each evening, as JoAnn scooted close at dinner, my mother found the nearness less nerve-racking.

On the last day, as we were leaving for the airport, JoAnn suddenly grabbed onto the lapels of my mother’s jacket, as if she were about to shake her.

My mother looked rattled, but then JoAnn said: “Thank you for coming, Jessica. I want you to know how much it means to me. I want you to know that I know we’ve never been close. And I know that’s been mostly my fault. I’m not sure how much time I’ve got. But more than anything, I want to have a shot at spending it with you. It’s so important. I mean, after all, Jessica, we’re sisters.”

I groaned, then looked over to see my tough mother crying . . . “Close enough, Mama,” she said.
```

---

## IC-2083: The Metamorphosis of Justin Jones

- Title: The Metamorphosis of Justin Jones
- Author (byline): Bruce Coville
- Work: Odder Than Ever
- Publisher: Graphia
- Publication date as stated: Oct 2000
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2567
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bruce Coville
Book: Odder Than Ever
ISBN: 978-0152024659
Publisher: Graphia
Date (Month/Year): Oct 2000
```

### Introduction (context only: never use it for content warnings)

```text
In The Metamorphosis of Justin Jones by Bruce Coville, a mistreated and unwanted boy makes a difficult choice between eternal untroubled youth and a future filled with untold pain and promise.
```

### Performance text (classify this)

```text
Justin Jones shot out the front door of the house where he lived-not his house, just the place where he was forced to live-and ran until he could no longer hear his uncle's shouts. Even then he didn't feel safe. Sometimes Uncle Rafe's anger was so powerful it propelled the man onto the street after Justin.

He leaned against a tree, panting and gasping for breath. The air burned in his lungs. He pressed his face against the tree, wishing he could melt into its rough bark and be safe.

When he finally opened his eyes again, Justin noticed an odd mist creeping around the base of the tree- Curious, he stepped forward to investigate. As he circled the tree he heard an odd whispering sound and felt a tingle in his skin. The mist covered the street ahead of him-a street he had never seen before.

At the end of the street he saw a strange, old-fashioned looking building. In the window were the words ELIVES MAGIC SUPPLIES. I could sure use a little magic about now, thought Justin. He tried the door. It opened smoothly. Magicians' parapher-nalia was scattered everywhere. Top hats, capes, scarves, big decks of cards, and ornate boxes covered the floor, the walls, the counters. At the back of the shop stretched a long counter with a dragon carved in the front. On top of the counter stood an old-fashioned brass cash register. On top of the cash register sat a stuffed owl.

Justin wandered to one of the counters. On it stood an artillery shell, thick as his wrist. Attached was a tag that said LISTEN.

Remembering the big seashell his mother used to put to his ear so he could "hear the ocean," Justin lifted the empty metal shell and held the hollow end to his ear. He could hear the sound of cannons, explosions, the terrified neighs of horses, the screams of wounded men. He put the shell down. Quickly.

He was about to bolt for the door when the owl he had thought was stuffed uttered a low hoot.

"Peace, Uwila," growled a voice from beyond the beaded curtain. "I'm coming!" A moment later an old man appeared. He was shorter than Justin, with long white hair and dark eyes that seemed to hold strange secrets. The old man looked at Justin for a moment, and something in his eyes grew softer. "What do you need?"

"I don't think I need anything," said Justin uncomfortably. "I just came in to look around."

"No one comes into this store just to look around, Justin. Now what do you need?"

Justin snorted. What did he need? A real home. His mother and father back. He needed- "Never mind," said the old man, interrupting Justin's bitter thoughts. "Let's try this. Have you ever seen a magician?" Justin nodded. "All right, then what's your favorite trick?"

Justin thought back to a time three years ago, back before his parents had had the accident. His dad had taken him to see a magician who did a trick where he locked his assistant in handcuffs, put her in a canvas bag, tied up the bag, put it in a trunk, wrapped chains around the trunk, and handed the keys to a member of the audience. Then he had climbed onto the trunk, lifted a curtain in front of himself, counted to five, and dropped the curtain. Only, when the curtain fell, the assistant was standing there, and the magician was inside the bag. "The metamorphosis!" he said suddenly, as his mind pulled the word from whatever mysterious place such things are kept.

The old man smiled and nodded. "Good choice.

Wait there." The old man disappeared through the beaded curtain-and came back a moment later carrying a small cardboard box. "The instructions are inside. Right now, it's late, and I am tired. Take the side door. It will get you home more quickly."

Justin nodded and hurried out the side door. Je walked home slowly. The later it was when he got there, the greater the chance his uncle would be asleep. Luck was with him; Uncle Rafe lay snoring on the couch, a scattering of empty beer cans on the floor beside him.

Justin tiptoed up the stairs to his room. He set the box on his desk, then used his pocketknife to cut the tape that held it shut. The box contained two items: a small instruction book and a bag that-to Justin's astonishment-shook out to be as large as the canvas sack the magician had used. The fabric was smooth and silky, and the colors shifted and changed as he looked at it..

He opened the instruction booklet. The directions were written by hand, in a strange spidery script. On the first page of the booklet were the following words: WARNING: Do NOT ATTEMPT THIS TRICK UNLESS YOU REALLY MEAN IT. Do NOT EVEN TURN THE PAGE UNLESS YOU ARE SERIOUS.

Justin rolled his eyes ... and turned the page. The directions here were even weirder: To begin the metamorphosis, open the bag and place it on your bed. Being careful not to damage the fabric, climb inside before you go to sleep. Keep your head out! After you have slept in the bag for three nights, you will receive further instructions.

Justin stared at the bag and the booklet for a long time. He was tempted to just stuff them back in the box and take the whole crazy thing back to the old man. Only, he wasn't sure he could find the store again, even if he tried.

He rubbed the whisper-soft fabric between his fingers. It reminded him of his mother's cheek. He climbed inside the bag, feet down, head out, and slept.

Justin slept in the bag for the next two nights, just as the directions said. In his dreams-which grew more vivid and beautiful each night-he flew, soaring far away from his brutal uncle and the house where he had felt such pain and loss.

On the morning of the fourth day, Justin felt as if something must explode inside him, so deep was the restlessness that seized him. Eagerly, fearfully, he turned to the instruction booklet that had come with the silken sack. As he had half expected, he found new writing on the page after the last one he had read-a page that had been blank before. Sometimes a leap of faith is all that's needed. His shoulders itched.

The next morning they were sore and swollen. The morning after that, Justin Jones woke to find that he had wings. Justin had two reactions. Part of him wanted to shout with joy. Another part of him, calmer, more cautious, was nearly sick with fear. He knew Uncle Rafe would not approve.

To his frustration, they hung limp and useless. Late at night, when his uncle was asleep, Justin would flex them, in the desperate hope that they would stretch and fill, somehow find the strength to lift him, to carry him away from this place.

Exactly one week after the first night he had slept in the sack, his wings became too obvious to hide. When he sat down to breakfast that morning, his uncle snapped, "Don't slouch like that. Look how you're hunching your shoulders. Take off your shirt," said his uncle, narrowing his eyes. Slowly, nervously, Justin did as he was told. “Turn around."

Justin obeyed. He heard a sharp intake of breath, then a long silence. Finally his uncle said, "Come here, boy." Turning to face him, Justin shook his head. His uncle scowled. "I said, come here." Justin backed away instead. His uncle lurched from the table, snatching at a knife as he did. Justin turned and ran, pounding up the stairway to the attic. At the top he closed the door behind him and locked it.

A moment later he heard his uncle roaring on the other side of it. For one foolish moment Justin hoped he would be safe here. Then the door shuddered as his uncle threw himself against it. The door splintered into the room. Stepping through, Uncle Rafe roared, "Come here, you little heathen!"

Shaking his head, mute with fear, Justin backed away, moving step-by-step down the length of the attic, until he reached the wall and the small window at the far end. His uncle matched his pace, confident in his control.

Justin knew that once Uncle Rafe had him, the wings would be gone, ripped from his shoulders. Pressing himself against the wall, he groped behind him until he found the window latch. The wings trembled at his shoulders, and he could feel some strange power move out from them. Taking a deep breath, Justin stepped out. He fell, but only for a moment. Suddenly the wings that had hung so limp and useless snapped out from his shoulders, caught the air, slowed his fall.

They stretched to either side of him, strong and glorious. As if by instinct he knew how to move them. And as his uncle cried out in rage and longing behind him, Justin Jones flew, rising swiftly above the house, above the trees, his heart lifting as if it had wings of its own.

Justin flew for a long time, as far from the home of his brutal uncle as he could manage to go. After a time, he saw a cloud ahead of him. It was glowing and beautiful, and without thought, he flew into it. The air within seemed to be alive with light and electricity, and as Justin passed through the cloud he felt a tingle in his skin.

Justin's shoulders were aching. He wasn't sure how much longer he could stay aloft. And then he saw it ahead of him: a small island, maybe two or three miles across, with an inviting-looking beach.

With a sigh of relief, Justin settled to the beach. He threw himself face forward on the sand to rest. Soon he was fast asleep. When Justin opened his eyes, he saw three children squatting in front of him.

"He's awake!" said the smallest.

"I told you he wasn't dead. They never are, no matter how bad they look."

Justin blinked, then glanced back at his shoulders. The wings were still there. Why didn't these strange children say anything about them? "Maybe I should just flyaway," he muttered.

"Oh, you can't do that," said the little girl, "Well, you could. But it wouldn't be smart. Not until you've talked to the old woman."

"So you've seen people with wings before?" asked Justin.

"Silly!" giggled the girl. "We all had wings when we came here. Were you scared when you went through the cloud? I was."

"Come on," said the biggest boy. "The old woman will tell you all. about it." Justin followed the three strange children up the beach and into the forest, a forest so perfect that it almost made him weep. It was filled with tree houses ... and the tree houses were filled with children. Happy children. Laughing children. Children who scrambled along rope bridges, dangled from thick branches, and swung from tree to tree on vines.

"All right. Take me to this old woman, will you please?"

"We can't take you," said the boy. "You'll have to go on your own. We can only show you the way."

Justin walked through the forest, following the path the children had shown him. The path turned a corner, and when he came out from between two trees he found himself at the edge of a large clearing, where there stood a huge, beautiful house.

The door was open. Even so, Justin knocked and called out. No one answered. Folding his wings against his back, he stepped through the door. "Old woman?" he called. "Old woman?"

"Up here!" called a voice. "I've been waiting for you." At last the stairs ended. Before him was a silver door. He put his hand against it, and it swung open.

"Come in," said the old woman. Her hair was white as cloud, her eyes blue as sky. She smiled. "I'm glad you're here. Do you like your wings?"

Justin reached back to touch one. "They're the most wonderful thing that ever happened to me," he said softly. "Who are you?"

She shrugged. "Just an old woman with time on her hands, trying to do a little good. Now listen carefully - The wings will only last for one more day. However, that will be long enough for you to fly home, if you should wish."

Justin snorted. "Why would I want to-"

"Shhh! Before you answer, you must look into my mirror. Then I will explain your choice." Standing, she took his hand and led him across the room. On the far side was a golden door. Behind it, Justin could hear running water. When she opened the door, Justin saw not a room, but a cave. In the center of the cave was a pool.

"Kneel," said the old woman. "Look."

Justin knelt, and peered into the water. He saw his own face -- not a boy, but a man. Yet it was clearly his face. "The man you will become,"

whispered the old woman.

Justin stared at the face. It was not handsome, as he had always hoped he would become. But it was a good face. The eyes were peaceful and calm. The beginning of a smile waited at the corners of the mouth. Laugh lines fanned out from the eyes.

"Come," she said quietly. Justin followed her back to the room. "Now you must choose," she said. "You can stay here. This place is safe and calm and no one will hurt you, ever again." Justin felt his heart lift. "But ... you will stay just as you are. Never change, never grow any older." She sighed. "That's the trade. There's always a trade.”

He looked at her, startled, Justin went to the window.. He stood there a long time, looking, listening. Finally he turned to the old woman. "Can I ask a question? The man I saw in the pool. Me. What does he do?"

The old woman smiled. "He works with children."

Justin smiled, too. "And what about my uncle?

Will things be better with him if I go back?" The old woman shook her head sadly.

Justin blinked. "Then how is it possible I can turn out the way you showed me? How can that be me?"

The old woman smiled again. "Ah, that one is easy. It is because no matter what happens, you will always remember that once upon a time ... you flew.

Justin nodded and turned back to the window. Far below he could hear the children at play. He ached to join them. But then he thought of the others he knew. The ones who never laughed. The ones who still needed wings. "How would I find the way back?"

"Take the side door," said the old woman softly. "It will get you home a little more quickly."

Tucking his wings against his back, Justin stepped through the door. He took a deep breath. Then he flew. Not toward home; Justin Jones had no real home. Flexing his wings, he pointed himself toward tomorrow and flew as hard as he could. .
```

---

## IC-2084: Mick Harte Was Here

- Title: Mick Harte Was Here
- Author (byline): Barbara Park
- Work: Not specified
- Publisher: Scholastic, Inc.
- Publication date as stated: Jan 1995
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR
- Teaser before the introduction: No
- Spoken words (computed): 1069
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barbara Park
ISBN: 978-0590929837
Publisher: Scholastic, Inc.
Date (Month/Year): Jan 1995
```

### Introduction (context only: never use it for content warnings)

```text
When I was a kid, I rode my bike all the time. I rode it all around my block and up and down my street. I rode it with my dad and brother to the local high school where we'd play a makeshift game of bike tag.

Sure, there was the occasional scare. Once I rode into a street without looking and a car had to stop quite short to avoid hitting me. My dad wasn't too thrilled about that, but nothing bad happened and it wasn't as if I was punished.

And not once, NOT ONCE, did I ever wear a bike helmet. At the time, I had some vague sense that I was invincible. Today, I look at that near miss with the car and silently shudder. I shudder, but not quite to the same extent as the speaker in

Mick Harte was Here by Barbara Park
```

### Performance text (classify this)

```text
NARRATOR: I just want to say, right off the bat that this isn’t the kind of story where you meet the main character, and you get to like him real well and then he dies at the end. I hate those kinds of stories. I don’t want to make you cry; I just want to tell you about Mick. But I thought you should know right up front that he’s not here

anymore. I just thought that would be fair to you.

It was a bike accident. It was about as “accidental” as you can get, too. Like Mick wasn’t riding crazy. Or dodging in and out of traffic. And both of his hands were on the handlebars and all like that. His tire just hit a rock. And he skidded into the back of a passing truck. And that was that.

I’m only ten months older than he was. I was “planned.”

Mick was a surprise. He loved it, too. Being a surprise, I mean. He was always teasing my parents about it. Telling them that even before he existed, he could outsmart two chemistry majors with birth control pills.

I remember the first big caper we pulled together, we scratched the letters F-A-R-T in the new driveway that had just been poured next to our house. It was, without a doubt, the funniest thing anyone had ever done in the entire history of the universe. But it’s amazing how a little fart in the driveway can totally lose its humor when your father sees it. He and mom stood us in front of them and made us “solemnly swear” to tell them the “complete and honest truth” about how it got there. Mick swallowed hard, took a big step forward, and told them “a monkey did it.” Then – just to make the story even more believable – Mick said the monkey’s name was Zippy. And the two of us had saved the day by chasing him “all the way back to Africa.”

You know, I’ve heard that sometimes when people you love die, you forget their voices. But I haven’t forgotten Mick’s. Not yet, anyway. I have a weird kind of memory, I think. Like I’ve never once been able to remember my parents’ anniversary in time to buy them a card. But I can still remember the exact conversation I had with Santa Claus when I was in kindergarten. He said, “Ho ho ho.” I said, “Your breath smells.” And he said, “Get down.” It wasn’t much of a chat, but the point is, it happened eight years ago and I still remember it like it was yesterday. I guess that’s why it doesn’t surprise me that I can still remember everything about the day of the accident.

See, Mick said he needed me to ride his bike home because he was going over to this kid Dillon Rigby’s house after school, but I said, “Sorry. I’ve got soccer practice after school. Plus I’ve got a ton of books to carry home tonight.” And he said, “Great, now I have to ride over there all by myself and I don’t even know where the kid lives.” And I said, “Aaah, no big deal. You’ll be fine,” and he said, “Gee, you’re really cool.” Then he just walked away. I didn’t even get to say goodbye.

I’m running sprints at soccer practice when I hear the siren. It bothers me that I’m kind of hypnotized by the sight of an ambulance. I don’t want to be one of those creeps who gawks at accident scenes. But I am, I think. Because as soon as I see the flashing red light appear over the fence, I can’t take my eyes off it. The ambulance is getting closer to the soccer field now. But instead of speeding past, it seems to be slowing down. Then it slows even more and turns the corner in front of the building. My stomach starts to churn.

I don’t like having the ambulance turn there. By now it should be speeding off to someone else’s neighborhood. A neighborhood where I don’t know anyone. Then all of a sudden, the door of the ambulance flies open and my dad comes rushing out and I close my eyes and I just wanted it not to be Mick. My dad puts his arms around me and pulls me close. Then he sort of cradles my head in his hand. Real gentle. Like I might break or something. Then in a voice so faint I could barely hear him – he whispers the words, “Mick’s gone.”

Yesterday was the official one-month anniversary of the accident. I used to think that anniversaries only celebrated happy things. But now I know that they’re just a way of measuring time. I went to soccer practice after school. I didn’t feel much like running though. The weird thing is, after practice was over, I didn’t want to leave the field. All I wanted to do was sit on the sidelines and think about Mick. Right across the field from me, a group of workmen were putting up a new set of bleachers. They were setting them in concrete. So, it was pretty clear they were going to be there for a while . . . but I decided to wait them out. It was almost dark when they finished. I still can’t believe no one stayed behind to guard the new sidewalk they just poured. I mean, you’ve gotta be nuts leaving wet cement unguarded at a junior high school. Especially if there’s an eighth grader sitting across the field who’s been watching you all afternoon. And I was totally calm when I did it. I walked over, bent down, and wrote, “MICK HARTE WAS HERE.” Because he was. And for twelve years and five months, my brother was one of the neatest kids you’ve ever want to meet. And I just wanted to tell you about him, that’s all. I just thought you should know.

CLOSING – AUTHOR’S NOTE

Head injury is the main cause of death in fatal bicycle crashes. Researchers tell us that if all bicyclists wore helmets, as many as one death every day and one head injury every four minutes could be prevented. I urge you, if you do not have your children wear bike helmets, please reconsider your decision. Today. Please. It’s a matter of life or death.
```

---

## IC-2085: Miss Alaineus: A Vocabulary Disaster

- Title: Miss Alaineus: A Vocabulary Disaster
- Author (byline): Debra Frasier
- Work: Not specified
- Publisher: HMH Books for Young Readers
- Publication date as stated: Sept 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1759
- Already set (do not supply): none

### Source block (context only)

```text
Author: Debra Frasier
ISBN: 978-0152060534
Publisher: HMH Books for Young Readers
Date (Month/Year): Sept 2007
```

### Introduction (context only: never use it for content warnings)

```text
Remember vocabulary tests from elementary school? That’s where we learned how to spell FEBRUARY (Feb-RU-ary), Wednesday (WED – NES – DAY) and TARANTULA (TARE – IN – TULA). And where we learned that there is a silent “S” in Island and it is not pronounced IS-LAND. And don’t even get me started on the word spelled A-I-S-L-E. Take a walk down memory lane with me in Debra Frasier’s Miss Alaineus: A Vocabulary Disaster.
```

### Performance text (classify this)

```text
None of this would have happened if it wasn’t for Forest. Forest is not a thicket of trees. Forest is a boy. A sick boy. A boy sneezing and coughing all over my desk and pencils.

I caught Forest’s cold and had to stay home from school on Tuesday. Tuesday is Vocabulary Day at Webster School. Follow my advice: Never get sick on Vocabulary Day.

On Tuesday afternoon I called my best friend, Starr who is not a luminous celestial object seen as a point of light in the sky, but a very smart girl who listens perfectly on Vocabulary Day. She was late for baseball practice, so she spelled the first fourteen vocabulary words as fast as she could.

I had to scribble them quickly because her mom was calling her to the car.

“The last one’s ‘Miss Alaineus’!” Starr yelled. “I gotta go. I hope you feel better tomorrow, Sage.” And she hung up the phone with a crash.

1 dinosaur, 2. snake, 3. museum, 4. reptile, 5.

constrictor, 6. herpetologist, 7. fossil, 8.

carnivore, 9. herbivore, 10. nest, 11. species, 12.

theory, 13. hypothesis, 14. category, 15. Miss

Alaineus.

I didn’t feel much better on Wednesday, so my mom called Mrs. Page, who is not a single side of a printed sheet of paper usually found bound in a book. She’s my teacher, and actually Mrs. Page is a good name for her because she reads to us every day. My mom told her yes, I had my math problems and vocabulary words, and yes, I would get better soon.

Every week Mrs. Page gives us a list of words with a theme, like Story Writing or Musical Performance or Electricity. We’re supposed to look up each word in the dictionary, but sometimes I already know the words, so I try to make the definitions sound like I looked them up.

By Thursday afternoon my head felt like it was stuffed with cotton and my throat felt swollen shut. I finished defining my vocabulary words while propped up in bed with a box of tissues on one side and a gigantic red dictionary on the other. It’s hard to look up words in a huge book while you’re in bed blowing your nose, so I made my own dictionary language for as many of them as I could.

13 hypothesis: what you guess will happen in your science experiment

14 category: a bunch of things that are alike

15 Miss Alaineus:

The last word seemed a little odd to me because I couldn’t figure out what she had to do with snakes or categories or theories. Mrs. Page rarely gives us people’s names on our vocabulary lists, but we have had a few that turned into words, like Louis Pasteur for pasteurization and George Washington for Washington, D.C., so I decided she must have been included for a reason.

You should know that for years I had wondered who Miss Alaineus was. When I was little I figured out that she had something to do with the kitchen, because the Miss Alaineus drawer held the spoons too big to fit anywhere else, the sharp corn holders shaped like tiny cobs, and the spaghetti spork, that weird cross between a spoon and a fork that perfectly lifts slippery spaghetti out of the bowl. I thought maybe she was an ancestor: an ancient relative long dead, who left us all these odd things in the drawer.

Then just last year my mom and I were at the grocery store and it all fell into place. We were in one of those Very Big Hurries when she said, “You go get some of that long Italian bread and two sticks of butter. I’ll get Miss Alaineus’ things and meet you here at the cash register.”

I found the bread and butter, and my mom came back with spaghetti sauce, a can of Parmesan cheese, a can of corn and a big green box of spaghetti with a beautiful woman on the front. She was drawn so that her hair tumbled perfectly across the box and ended in a little plastic window, making the spaghetti look just like the ends of the strands of her hair.

There she was – Miss Alaineus.

So, propped up on pillows in my bed, with a tissue in one hand and a pencil in the other, I wrote:

15 Miss Alaineus: the woman on green spaghetti boxes whose hair is the color of uncooked pasta and turns into spaghetti at the ends

And then I fell asleep.

I finally got better over the weekend and felt great on Monday. I turned in my homework to Mrs. Page and sat down at my desk, glad to be back at school with my friends. I was even glad to see Forest at our morning circle meeting.

“First, I want to remind you of the Tenth Annual Vocabulary Parade on Friday,” said Mrs. Page. “I hope you are all working on your word costumes. Second, please remember to bring your bus money and permission slips for our science museum field trip tomorrow. And third, instead of our usual Monday test, we are going to have a Vocabulary Bee today.

“Everyone line up here by the chalkboard, and I’ll choose a word from our list. After I pronounce the word, please spell and define it. If you are correct, go to the end of the line. If you miss the word, please sit down at your desk and look it up in the dictionary. Write the word five times and define it once.”

Starr was the first with museum: “M-U-S-E- U=M: a building for exhibiting objects about art or history or science” she said, and went to the back of the line.

Cliff, not a high, steep face of rock, but one very tall boy, answered to the word dinosaur: “D-I-N-O- S-A-U-R: a prehistoric, extinct reptile, often huge,” and he went to the back of the line.

I was tenth, and when Mrs. Page called out my word, I spelled: “Capital M-I-S-S, capital A-L-A-I- N-E-U-S,” and added, “the woman on green spaghetti boxes whose hair is the color of uncooked pasta and turns into spaghetti at the ends.”

There was a moment of silence in the room. I smiled at Mrs. Page. She waited to see if I would add anything else, and when I didn’t, she grinned. Not smiled – grinned: to draw back the lips and bare the teeth, as in a very wide smile – and the entire class burst into one huge giggling, laughing, falling-down mass of kids. Forest was doubled over. Starr, my best friend, was laughing so hard tears came to her eyes. By now, even Mrs. Page was laughing.

Pride goeth before a fall. I was Sage: one who shows wisdom, experience, judgment. Why were they laughing? “Wise-girl-with-words” my dad always called me. What had I said? I was beginning to turn red. Red: The color of embarrassment.

Finally the room quieted. Mrs. Page opened her dictionary and wrote on the chalkboard:

Miscellaneous: adj. 1) consisting of various kinds or qualities 2) a collection of unrelated objects

My jaw dropped as I looked at the spelling. My eyes bulged as I read the definition. I didn’t bother to tell anyone about my mom and the spaghetti spork and the grocery store. Humbled: aware of my shortcomings, modest, meek, I dragged back to my seat and wrote miscellaneous five times and defined it once. And that’s when I remembered I had even drawn a picture of the spaghetti box for extra credit. I was devastated: wasted, ravaged. Ruined: destroyed. Finished: brought to an end.

They called me Miss Alaineus for the rest of the day. Sometimes a person couldn’t even get the words out before bending over with laughter. The day took a week to end. When I got off the bus I slumped home – devastated, ruined, finished.

I told my mom the whole story, from the kitchen drawer to the grocery store to the Vocabulary Bee.

Even my own mother laughed a little at the part about the drawing for extra credit, but at least she stopped fast and said, “You know what I always say . . . There’s gold in every mistake.”

Gold? A bright yellow precious metal or great value?

Mistake? Something done, said, or thought in the wrong way?

“Impossible,” I told her. Impossible: not capable of happening.

I couldn’t believe I ever had to go back to school. But the next day we went to the science museum, and everyone forgot all about Miss Alaineus at the snake exhibit and the dinosaur bone lab. Then the guide said, “The field of bone archaeology has been influenced by a wide and unusual array of miscellaneous discoveries around the world.” The class burst out laughing, and the guide was pleased with herself for entertaining us so easily. And I knew: to apprehend with certainty that my mistake was still alive and well, and nothing like gold.

After school I lay on my bed and stared at the wall. How could I have been so stupid?

My mom came in and said it was time to work on my costume for the Vocabulary Parade. We had finished the cape for Capable, but I still needed to make the lettering down the back.

“Mom,” I said, “I could only be a mistake this year. Miss Stake.”

Suddenly I sat up. I looked at my mom. She looked at me. I smiled. She smiled.

“Sweetheart,” she said, “let’s take another look at that cape.”

It took the most courage I’ve ever had to walk out on that stage as Miss Alaineus, Queen of All Miscellaneous Things. But when Mr. Bell read my word and definition, everyone applauded and laughed wildly: in a manner lacking all restraint, and I grinned at my mom across the auditorium.

Forest came right after me. When he bowed, his Precipitation watering-can hat rained on Mr. Bell’s new suit, and the entire audience gasped, then cheered when Mr. Bell smiled at his soggy clothes.

To my astonishment: great shock and amazement, I won a gold trophy for the Most Original Use of a Word in the Tenth Annual Vocabulary Parade.

So this time Mom was right. There was good in this mistake. . And next year I think I’m going to be . . . Miss Sterious, Investigator of All Things Mysterious.
```

---

## IC-2086: The Missing Piece

- Title: The Missing Piece
- Author (byline): Shel Silverstein
- Work: Not specified
- Publisher: HarperCollins Publishers, Inc
- Publication date as stated: May 1976
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 558
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shel Silverstein
ISBN: 978-0060256715
Publisher: HarperCollins Publishers, Inc
Date (Month/Year): May 1976
```

### Introduction (context only: never use it for content warnings)

```text
A truly unique and multi-faceted artist, Shel Silverstein was a renowned poet, playwright, illustrator, screenwriter, and songwriter. Best known for his immensely popular children’s books including The Giving Tree, Falling Up, and The Missing Piece, Silverstein has delighted millions of readers around the world, becoming one of the most popular and best-loved children's authors of all time.

In The Missing Piece, Silverstein concocts a marvelous tale with a powerful message: “Nno one should try to find all the answers, no one should hope to fill all the hopes in themselves, because a person without a search, loose ends, internal conflicts and external goals becomes too smooth to enjoy life." Never stop searching for The Missing Piece by Shel Silverstein.
```

### Performance text (classify this)

```text
It was missing a piece.
And it was not happy.
So it set off in search of its missing piece.
And as it rolled it sang this song-

"Oh I'm lookin' for my missin' piece

I'm lookin' for my missin' piece

Hi-dee-ho, here I go,

Lookin' for my missin' piece."
Sometimes it baked in the sun
but then the cool rain would come down.
And sometimes it was frozen by the snow
but then the sun would come and warm it again.
And because it was missing a piece it could not very
fast so it would stop to talk to a worm
or smell a flower
and sometimes it would pass a beetle
and sometimes the beetle would pass it
and this was the best time of all.
And on it went, over oceans

"On I'm lookin' for my missin' piece

Over land and over seas

So grease my knees and fleece my bees

I'm lookin' for my missin' piece."
through swamps and jungles
up mountains
and down mountains
Until one day, lo and behold!

"I've found my missin' piece," it sang,

"I've found my missin' piece

So grease my knees and fleece my bees

I've found my..."
"Wait a minute," said the piece.
"Before you go greasing your knees
and fleecing your bees..."
I am not your missing piece. I am nobody's piece.
I am my own piece.
And even if I was somebody's missing piece
I don't think I'd be yours!"
"Oh," it said sadly,
"I'm sorry to have bothered you."
And rolled on.
It found another piece
but this one was too small.
And this one was too big
this one too sharp
and this one too square.
One time it seemed to have found the perfect piece

but it didn't hold it tightly enough

and lost it.

Another time it held too tightly

and broke.

So on and on it rolled,

having adventures

falling into holes

and bumping into stone walls.

And one day it came upon another piece that seemed to be just right.

"Hi," it said.

"Hi," said the piece.

"Are you anybody else's missing piece?"

"Not that I know of."

"Well, maybe you want to be your own piece?"

"I can be someone's and still be mine."

"Well, maybe you don't want to be mine."

"Maybe I do."

"Maybe we won't fit...."

"Well..."

"Hummm?"

"Ummmm!"
It fit!
It fit perfectly!
At last! At last!
And away it rolled
and because it was now complete,
it rolled faster and faster.
Faster than it had ever rolled before!
So fast that it could not stop to talk to a worm
or smell a flower
too fast for a butterfly to land.
But it could sing its happy song,
at last it could sing "I've found my missing piece."
And it began to sing-

"I've frown my nizzin' geez

Uf vroun my mitzin' brees

So krease ny meas

An bleez ny drees

Uf frown..." Oh my, now that it was complete it could not sing at all. "Aha," it thought.

"So that's how it is!"

So it stopped rolling...

and it set the piece down gently,

and slowly rolled away

and as it rolled it softly sang-

"Oh I'm lookin' for my missin' piece

I'm lookin' for my missin' piece

Hi-dee-ho, here I go,

Lookin' for my missin' piece."
```

---

## IC-2087: A Monster Calls

- Title: A Monster Calls
- Author (byline): Patrick Ness
- Work: Not specified
- Publisher: Candlewick
- Publication date as stated: March 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1178
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patrick Ness
ISBN: 978-0763660659
Publisher: Candlewick
Date (Month/Year): March 2013
```

### Introduction (context only: never use it for content warnings)

```text
Elizabeth Kubler Ross created a pathway to grief with her five stages: Denial, Anger, Bargaining, Depression, Acceptance. These stages are meant to allow grief to be understood, and the sufferer to let go. When Conor O’Malley finds out his mother is dying of cancer, he lives in denial and pent-up anger.

No one talks about her death -- not her, not his grandmother, not his father, and not him. Not until he is forced to face the inevitable and deal with his grief. This grief takes the form of a monster. A monster who forces him to face the truth and guides him to acceptance.

A Monster Calls, by Patrick Ness
```

### Performance text (classify this)

```text
(Pg 1-2) The monster showed up just after midnight. As they do. Conor was awake when it came. He’d had a nightmare. Well, not a nightmare. The nightmare. The one he’d been having a lot lately. The one with the darkness and the wind and the screaming.

He’d told no one about the nightmare. Not his mum, obviously, but no one else either. What happened in the nightmare was something no one else ever needed to know.

The nightmare was slipping from him, but there was something he couldn’t put his finger on, something different . . . He listened, but all he could hear was the quiet house around him. Nothing.

And then something. Something he realized was the thing that had woken him. Someone was calling his name . . . Conor.

(Pg 4) Conor.

“What?” Conor said, his heart thumping, suddenly impatient for whatever was going to happen.

A cloud moved in front of the moon, and then passed, and the moon shone again. On a yew tree. Which now stood firmly in the middle of his backyard. And here was the monster. (Pg 136) The yew is a healing tree. It is the form I choose most to walk in.

(Pg 30) “What do you want from me?”

(Pg 36) You will tell me the truth.

“The truth?”

Not just any truth. Your truth. You know that your truth, the one that you hide, Conor O’Malley, is the thing you are most afraid of. For this is why you called me.

Conor grew even more confused. “Called you? I didn’t call you—

(Pg 137) If your mother can be healed, then the yew tree will do it.

(Pg 141) “What’s going to happen with my mum? You said you were a tree of healing. Well, I need you to heal!”

(Pg 172) Conor O’Malley, I did not come to hear her, I came to heal you.

“Me? I don’t need healing. My mum’s the one who’s...”

But he couldn’t say it. Even now he couldn’t say it. Even though he’d known it all along. Of course he did, no matter how much he’d wanted to believe it wasn’t true, he knew. But still, he couldn’t say it. Couldn’t say she was--

It is time, for [your truth].

The mist surrounded them again. And once more, [he] was in the middle of the nightmare . . .

(Pg 174-175) He recognized the clearing he was in, bordered on three sides by a dark forest; the fourth side, a cliff, flying off into further blackness.

And on the cliff’s edge, his mum.

“Mum!” Conor yelled, feeling too heavy to stand. “You have to get out of here!”

“I’m fine, darling”, she said, “There’s nothing to worry about.” She turned back to the cliff’s edge, as if she’d heard something.

“No,” Conor whispered to himself. He pulled himself forward some more, but she was too far, too far to reach in time, and he felt so heavy--

There was a low sound from below the cliff. A rumbling, booming noise.

Conor knew. It was too late. The real monster was coming. (Pg 178-181) Because with a roar, a cloud of burning darkness lifted two giant fists over the cliff top. They hovered in the air, over his mum as she tried to scramble back. But she was too weak, much too weak-

At last, Conor could run. With a shout, he broke across the clearing, running so fast he nearly toppled over, and he threw himself toward her as the dark fists pulled her over the edge. And his hands caught hers.

“Help me, Conor! Don’t let go!” his mum yelled.

“I won’t! I promise!’

The nightmare monster pulled harder, its fists straining around his mother’s body. And she began to slip from Conor’s grasp.

“No!” he called.

His mum screamed in terror. “Please, Conor! Hold on to me!”

[But even as she said this, her hands] were slipping from his grasp, and she was getting heavier and heavier; the nightmare monster pulling harder and harder. He fell forward onto his chest from the weight of her. She screamed again.

“Please!” Conor whispered to himself. “Please!”

“NO!” Conor screamed. And his mother fell.

And here, he heard the yew tree say, is the truth of Conor O’Malley. (Pg 185-189) You let her go.

“I didn’t let her go! She fell!” Conor shouted.

You must tell the truth or you will never leave this nightmare. You will be trapped here alone for the rest of your life.

“I don’t know what you mean!” Conor yelled desperately trying to fight the monster’s urging.

You do know, it said, low and threatening.

And there was a sudden quiet. Because yes, Conor knew. The truth. The real truth from the nightmare.

“Please don’t make me, please don’t make me say it.”

You let her go. You could have held on for longer, but you loosened your grip. You wanted her her to go.

“NO!”

You must speak the truth, Conor O’Malley. Say it. You must.

“I can’t.”

You let her go. Why? Tell me WHY! Before it’s too late!

A moan started in his throat, a moan that rose into a cry and then a loud wordless yell and he opened his mouth. And he spoke the truth.

“I can’t stand it anymore!” He cried out. “I can’t stand knowing that she’ll go! I just want it to be over! I want it to be finished! I’ve known forever that she wasn’t going to make it. And I started to think how much I wanted it to be over. How I couldn’t stand the waiting anymore. I couldn’t stand how alone it made me feel.”

He began to cry now, more than he thought he’d ever done. More than when he found out his mum was ill.

(Pg 203) He wanted to ask the monster what was going to happen then, but he didn’t dare.

Because he knew.

[And then they were in his mother’s hospital room] (Pg 202) The monster’s hands gently but firmly guided him toward [her]. (Pg 203-205) Conor looked down at [her], and he took his mother’s hand.

She opened her eyes, briefly, catching him there. Then she closed them again.

But she’d seen him. And he knew it was here. He knew there really was no going back. That it was going to happen. And he knew he was going to get through it. And an at last, he spoke the final and total truth . . .

“I don’t want you to go,” He said, the tears dropping from his eyes slowly at first, then spilling like a river.

“I know my love,” His mother said in her heavy voice. “I know.”

He could feel the monster, holding him up and letting him stand there.

“I don’t want you to go,” he said again.

And that was all he needed to say. He leaned forward on her bed and put his arms around her. Holding her. He knew it would come. The moment she would slip from his grasp, no matter how tightly he held on.

But not this moment, the monster whispered, still close. Not just yet.

Conor held tightly onto to his mother. And by doing so, he could finally let her go.
```

---

## IC-2088: The Most Mature Thing I’ve Ever Seen

- Title: The Most Mature Thing I’ve Ever Seen
- Author (byline): Chris Blake
- Work: Swimming Against the Current
- Publisher: Pacific Press Publishing
- Publication date as stated: 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 919
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chris Blake
Book: Swimming Against the Current
ISBN: 978-0816321414
Publisher: Pacific Press Publishing
Date (Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
In a recent survey of 40,000 high school students, 50 percent admitted to bullying other students within the past year, and 47 percent said they had been "bullied, teased, or taunted in a way that seriously upset" them. The scary part is that bullying doesn’t have to be physical . . . indirect bullying or social aggression can cause even deeper psychological wounds than physical bullying. And teens are so eager to fit in that this subtle form of bullying spreads like wildfire. In The Most Mature Thing I’ve Ever Seen by Chris Blake . . . one teenager is strong enough to fight the pack mentality and reach out to a student who unwittingly becomes a target of the teen-age pack. The Most Mature Thing I’ve Ever Seen by Chris Blake.
```

### Performance text (classify this)

```text
Every student at Monroe High School knew about it. Nobody did it. Nobody. Lunchtime at Monroe High School was consistent. As soon as the bell that ended the last morning class started ringing, the students swarmed toward their lockers. Then those who didn’t eat in the cafeteria headed with their sack lunches toward the quad. The quad was a large, treeless square of concrete in the center of campus. It was the meeting-and-eating place.

Around the quad the various school cliques assembled. The druggies lined up on the south side. The punkers were next to them. On the east side were the brothers. Next to them were the nerds and brains. The jocks stood on the north side next to the surfers. The rednecks were on the west side. The socialites were in the cafeteria. Everybody knew their place.

This arrangement did create some tension. But all the tension generated on the perimeter of the quad a lunchtime was nothing compared with the inside of the quad.

The inside was no-man’s land.

Nobody at Monroe walked across the middle of the quad. To get from one side to the other, students walked around the quad. Around the people. Around the stares.

Everybody knew it so nobody did it.

Then one day at the beginning of spring, a new student arrived at Monroe. Her name was Lisa. She was unfamiliar to the area; in fact, she was new to the state.

And although Lisa was pleasant enough, she did not quickly attract friends. She was overweight and shy, and the style of her clothes was not . . . right.

She had enrolled at Monroe that morning. All morning she had struggled to find her classes, sometimes arriving late, which was especially embarrassing. The teachers had generally been tolerant, if not cordial. Some were irritated; their classes were already too large, and now this added paperwork before class.

But she had made it through the morning to the lunch bell. Hearing the bell, she signed and entered the crush of students in the hall. She weaved her way to her locker and tried her combination three, four, five times before it banged open. Standing in front of her locker, she decided to carry along with her lunch all of her books for her afternoon classes. She thought she could save herself another trip to her locker by eating lunch on the steps in front of her next class.

So Lisa began the longest walk of her life – the walk across campus toward her next class. Through the hall. Down the steps. Across the lawn. Across the sidewalk. Across the quad.

As Lisa walked, she shifted the heavy books, alternately resting the arm that held her light lunch. She had grabbed too many books – the top book kept slipping off, and she was forced to keep her eye on it in a balancing act as she moved past the people, shifting the books from arm to arm, focusing on the balanced book, shuffling forward, oblivious to her surroundings.

All at once she sensed something: The air was eerily quiet. A nameless dread clutched her. She stopped. She lifted her head.

Hundreds of eyes were staring. Cruel, hateful stares. Pitiless stares. Angry stares. Unfeeling, cold stares. They bore into her.

She froze, dazed, pinned down. Her mind screamed, “No! This can’t be happening!”

What happened next people couldn’t say for sure. Some later said she dropped her book, reached down to pick it up, and lost her balance. Some claimed she tripped. It didn’t matter how it happened.

She slipped to the pavement and laid there, legs splayed, in the center of the quad.

Then the laughter started, like an electric current jolting the perimeter, charged with a nightmarish quality, wrapping itself around and around its victim.

And she lay there.

From every side fingers pointed, and then the taunt began, building in raucous merriment, building in heartless insanity: “You! You! You! YOU!”

And she lay there.

From the edge of the perimeter a figure emerged slowly. He was a tall boy, and he walked rigidly, as though he were measuring each step. He headed straight toward the place where the fingers pointed. As more and more students noticed someone else in the middle, the calls softened, and then they ceased. A hush flickered over the crowd.

The boy walked into the silence. He walked steadily, his eyes fixed on the form lying on the concrete.

By the time he reached the girl, the silence was deafening. The boy simply knelt and picked up the lunch sack and the scattered books, and then he placed his hand under the girl’s arm and looked into her face. And she got up.

The boy steadied her once as they walked across the quad and through the quiet perimeter that parted before them.

The next day at Monroe High School at lunchtime, a curious thing happened. As soon as the bell that ended the last morning class started ringing, the students swarmed toward their lockers. Then those who didn’t eat in the cafeteria headed with the sack lunches across the quad.

From all parts of the campus, different groups of students walked freely across the quad. No one could really explain why it was OK now. Everybody just knew. And if you ever visit Monroe High School, that’s how it is today.

It happened some time ago. I never even knew his name. But what he did, nobody who was there will ever forget.

Nobody.
```

---

## IC-2089: My Father’s Hands

- Title: My Father’s Hands
- Author (byline): Calvin R. Worthington
- Work: Reader’s Digest; Volume 108, No 649, Pg 169
- Publisher: Reader’s Digest
- Publication date as stated: May 1976
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1389
- Already set (do not supply): none

### Source block (context only)

```text
Author: Calvin R. Worthington
Book: Reader’s Digest; Volume 108, No 649, Pg 169
ISSN: 0034-0375
Publisher: Reader’s Digest
Date (Month/Year): May 1976
```

### Introduction (context only: never use it for content warnings)

```text
In the early 1900s, supporting yourself and helping your family took priority over school if you were poor. And if you were poor and had a learning disability; school was simply not a necessity. Learning to read and write? Optional. Today these people are called functionally illiterate. And according to an article by Chloe Haderlie and Allysa Clark, in *2017 approximately 18% of American adults fell into this category.

My Father’s Hands by Calvin R Worthington
```

### Performance text (classify this)

```text
His hands were rough and exceedingly strong. He could gently prune a fruit-tree or firmly wrestle a stubborn mule into harness. He could draw and saw a square with quick accuracy. He had been known to peel his knuckles on a tough jaw. But what I remember most is the special warmth from those hands soaking through my shirt, as he would take me by the shoulder and, squatting beside my ear, point out the glittering swoop of a blue hawk, or a rabbit asleep in its lair. They were good hands that served him well and failed him in only one thing: they never learned to write.

My father was illiterate. The number of illiterates in the country has steadily declined, but if there were only one, I would be saddened, remembering my father and the pain he endured because his hands never learned to write.

When he started school, the remedy for a wrong answer was ten ruler strokes across a stretched palm. For some reason, shapes, figures and recitations just didn’t fall into the right pattern inside his six-year-old tow-head. Maybe he suffered from some type of learning handicap such as dyslexia. His father took him out of school after several months and set him to a man’s job on the farm.

Years later, his wife, educated to the fourth year of primary school, would try to teach him to read. And still later I would grasp his big fist between my small hands and awkwardly help him trace the letters of his name. He submitted to the ordeal, but soon grew restless. Flexing his fingers and kneading his palms, he would eventually declare that he had had enough and would depart for a long, solitary walk.

Finally, one night when he thought no one saw, he slipped away with his son’s second-grade reader and labored over the words, until they became too difficult. He pressed his forehead into the pages and wept. ‘Jesus— Jesus—not even a child’s book?’ Thereafter, no amount of persuading could bring him to sit with pen and paper.

From the farm to road-building and later factory work, his hands served him well. His mind was keen, his will to work unsurpassed. During World War II, he was a pipefitter in a shipyard and installed the complicated guts of mighty fighting ships.

His enthusiasm and efficiency brought an offer to become a foreman — until he was handed the qualification test. His fingers could trace a path across the blueprints while his mind imagined the pipes lacing though the heard of the ship. He could recall every twist and turn of those pipes. But he couldn’t read or write.

It has always been hard for him to stand before a man and make an X mark for his name, but the hardest moment of all was when he placed ‘his mark’ by the name someone else had written for him and saw another man walk away with the deed to his beloved farm. When it was over, he stood before the window and slowly turned the pen he still held in his hands—gazing, unseeing, down the mountainside. I went out to the barn that afternoon and wept for a long, long while.

Eventually, he found a cotton-mill job, and we moved into a millhouse village with a hundred look-alike houses. He never quite adjusted to town life. The blue of his eyes faded; the skin across his cheekbones became a little slack. But his hands kept their strength, and their warmth still soaked through when he would sit me on his lap and ask that I read to him from the Bible. He took great pride in my reading and would listen for hours as I struggled through awkward phrases.

Once he had heard ‘a radio preacher’ relate that the Bible said, ‘The man that doesn’t provide for his family is worse than a thief and an infidel and will never enter the Kingdom of Heaven.’ Often he would ask me to read that part to him, but I was never able to find it. Other times, he would sit at the kitchen table leafing through the pages as though by a miracle he might be able to read the passage should he turn to the right page. Then he would sit staring at the Book, and I knew he was wondering if God was going to refuse him entry into heaven because his hands couldn’t write.

When Mother left once for a weekend to visit her sister, Dad went to the store and returned with food for dinner. After the meal he said he had a surprise for dessert, and went out to the kitchen, where I could hear him opening a can. Then everything was quiet. I went to the doorway and saw him standing before the sink with an open can in his hand. ‘The picture looked just like pears.’ He mumbled. He walked out and sat on the back steps, and I knew he had been embarrassed. The can read ‘Whole White Potatoes’, but the illustration on the label did look a great deal like pears.

I went and sat beside him and asked if he would point out the stars. He knew where the Big Dipper and all the other stars were located, and we talked about how they got there in the first place. He kept that can on a shelf in the woodshed for a long while, and on several occasions I saw him turning it in his hands as if the touch of the words would teach his hands to write.

Years later, when Mom died, I tried to get him to come and live with my family, but he insisted on staying in his small weatherboard house on the edge of town with a few farm animals and a garden plot. His health was failing, and he was in and out of the hospital with several mild heart attacks. Old Doc Green saw him weekly and gave him medication, including nitroglycerin tablets to put under his tongue should he feel an attack coming on.

My last fond memory of Dad was watching as he walked across the brow of a hillside meadow, with those big, warm hands, now gnarled with age, resting on the shoulders of my two children. He stopped to point out them, confidentially, a pond where he and I had swum and fished years before. That night, my family and I flew to a new job and new home, overseas. Three weeks later, he was dead of a heart attack.

I returned alone for the funeral. Doc Green told me how sorry he was. In fact, he was bothered a bit, because he had just written Dad a new nitroglycerin prescription, and the chemist had made it up. Yet the bottle of pills had not been found on Dad’s person. Doc Green felt that a pill might have kept him alive long enough to summon help.

An hour before the chapel service, I found myself standing near the edge of Dad’s garden, where a neighbor had found him. In grief, I stopped to trace my fingers in the earth where a great man had reached the end of life. My hand came to rest on a half-buried brick, which I aimlessly lifted and tossed aside, before noticing underneath it the twisted and battered, yet unbroken, soft plastic bottle that had been beaten into the soft earth.

As I held the bottle of pills, the scene of Dad struggling to remove the cap and in desperation trying to break the bottle with the brick flashed painfully before my eyes. With anguish I knew why those big warm hands had lost in their struggle with death. For there, imprinted on the bottle cap, were the words, ‘Child-Proof Cap—Push Down and Twist to Unlock’. The chemist later confirmed that he had just started using the new safety bottle.

I knew it was not a purely rational act, but I went straight to town and bought a leather-bound pocket dictionary and a gold pen set. I bade Dad goodbye by placing them in those big old hands, once so warm, which had lived so well, but had never learned to write.
```

---

## IC-2090: My Town

- Title: My Town
- Author (byline): Buddy Wakefield
- Work: Live for a Living
- Publisher: Write Bloody Publishing
- Publication date as stated: Oct 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 977
- Already set (do not supply): none

### Source block (context only)

```text
Author: Buddy Wakefield
Book: Live for a Living
ISBN: 978-0978998950
Publisher: Write Bloody Publishing
Date (Month/Year): Oct 2007
```

### Introduction (context only: never use it for content warnings)

```text
The United States is a country that has laws, a constitution and a Bill of Rights which preach freedom, democracy and justice—all of which are words written on paper. The United States is a country that is fueled by the need to be the most powerful and wealthiest nation in the world and is selective when applying its standards of freedom and democracy.

The sad truth is that the United States is a society where one man can spend millions of dollars on a magnificent yet insignificant event and another man must eat from garbage in order to quell his hunger. Is this truly freedom and democracy?

My Town by Buddy Wakefield
```

### Performance text (classify this)

```text
My town is cute
like a bumper sticker
like when Christians sport POWER OF PRIDE bumper
stickers.

What is it you people don’t understand about pride being a deadly sin?

My town is cute like GOD BLESS AMERICA bumper stickers. Judging by our excessive luxuries, those stickers really work. Now if we can just get God to bless the whole world.

Alix Olsen’s bumper sticker reads I LOVE MY
COUNTRY.
I JUST THINK WE SHOULD START SEEING OTHER
PEOPLE.
But my town doesn’t see other people.
We’re just too cute
like the difference between what we say and what we do
like the fact that violence in any form
is sanctioned by the government as criminal or insane
unless they're the ones who commit it.

My town is cute like people who still shop at Wal-Mart and claim to be patriotic. Stop it.

My town is cute in the way we worry about the gays [messin’] up our family values and the sanctity of marriage, yet we still let our children watch television shows like Wife Swap, The Bachelor, Who Wants to Marry a Millionaire, American Idolatry and Fox News.

My town is so cute that - check this out -
once, six years ago,
there were some brown people (boogity boogity),
they attacked two of our tallest buildings
and killed a [bunch] of our innocent citizens,
kinda like we did
in Guatemala, Nicaragua, Panama, El Salvador,
Tanzania, Mozambique, Vietnam, Afghanistan,
Hiroshima, Philippines, Kosovo, Bolivia,
Angola, Argentina, Brazil, Chile, Dresden,
Dominican Republic, Cuba, Haiti, Indonesia,
East Timor, Cambodia, Iraq, (what the [hell]
are we doing in Israel?)
and my cute town pretends we never saw it [or had it]
coming
so in a perpetual attempt to save cute face
we’ve waged a war on terror about as effective as the
war on drugs.
My town is cute when we wage these wars in the name of
God.

As many as 20% of the polar bears on the Northern Ice Cap are hermaphrodites due to PCB’s being dumped into the ocean. You won't hear about that on the news because it's too cute, like a wolf giving birth through its penile canal (True).

My town is cute like a 300lb tumor containing hair and teeth inside of it grown from the body of a 210 pound agoraphobic woman, cute like competitive poetry, the history of Scientology, plastic surgery, and refined sugars, cute like a man swallowing an 8-ball of cocaine then jumping from a 5-story building to escape police, getting up and running away from it all.

Y'all, this this is a true story:

The first time my town saw the sky
it sucker punched us in the throat
left us breathless
said, "I'm gonna keep you awake some nights
without touching you
you'll make it up, the pain,
you always do."

Now my town only buys drowsy formula sky.
Otherwise it gets too big, the sky,
like when we were three
before we realized:

We have balls. The sky does not. Therefore, we have bigger balls than the sky.

Please do not talk to us about being tea-bagged by upside down hot air balloons.

Where rational conversation and big pictures are
concerned
we have no time for getting wrapped up.
We are not presents for your sky.
We are just right.
Far right.
And cut
like 3-year-olds,
like the book about bunny suicides,
cute like Old Yeller just 'fore he got shot in the rabies
(a good actor, that dog).

My town was born way off the mark.
Sometimes we see it coming, the mark,
So we shoot it with spit wads or
precision-guided phallic symbols.

Every time there is talk of war people give me reasons why their town will be bombed first. It's a souped-up sense of self importance, buck-o. Everybody knows my town will be bombed first because once we planned the construction of a nuclear power plant right here in the same fields where our military children now carry out covert orders to keep the word dumb alive.

Christianity has a hard time workin' here,
makes us believe that even when we are alone
someone is watching us and judging us.
Now we're all narcissists.
We have a habit of giving other people's gifts to
ourselves.

But at least our children still get their confidence booster shots, while our fathers perform voice reduction surgery to keep our pleas for help mime-sized while our mothers are bending infinity in half so that our families can continue to talk in circles, while we all burn our tongues when we drink hot cocoa for the same reason everybody here wants to hug the ocean because it's just so much.

My town knows that there is something so big inside of
all of us
we have to suck
just to distract you from being directly overwhelmed by
our real power,
the kind of power that makes you smile.
Everybody knows that smiling is for little girls, the gays
and certain kinds of fish
who are smiling by accident.

The shortcuts my town has taken
have saved us so little time
gotten us so far ahead of ourselves
we have actually fallen behind.
Would have been better off learning to herd turtles
into bomb shelters, on a moment’s notice,
giggling at the fact that we will all now die
and it'll have happened so fast
we will have never been anything
but really cute
like our three-year-olds
who use folding chairs
to beat lambs within inches of their lives.

My town is inches tall.
It's why the sky looks down on us,
wants to tell us something
like grow up
or reach up
or look up and watch me winking
I'm trying to talk to you.

The Earth is travelling at 66,641 mph around the sun. It simultaneously rotates on itself at over 1000 mph. My town? Yeah, it's having some trouble sleeping.
```

---

## IC-2091: Nineteen Minutes

- Title: Nineteen Minutes
- Author (byline): Jodi Piccoult
- Work: Not specified
- Publisher: Washington Square Press
- Publication date as stated: February 2008
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1891
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jodi Picoult
ISBN: 978-0743496735
Publisher: Washington Square Press
Date (Month/Year): February 2008
```

### Introduction (context only: never use it for content warnings)

```text
In nineteen minutes, you can mow the front lawn, color your hair, watch a third of a hockey game. In nineteen minutes, you can bake scones or get a tooth filled by a dentist; you can fold laundry for a family of five . . . In nineteen minutes, you can stop the world, or you can just jump off it. In nineteen minutes, you can get revenge.

Sterling is a small, ordinary New Hampshire town where nothing ever happens -- until the day its complacency is shattered by a shocking act of violence. 17-year-old high school student Peter Houghton has endured years of verbal and physical abuse at the hands of classmates. One final incident of bullying sends Peter over the edge and leads him to commit an act of violence that forever changes the lives of Sterling’s residents.

Nineteen Minutes by Jodi Picoult
```

### Performance text (classify this)

```text
Patrick sat at a red light in his unmarked police car, waiting to turn onto the highway. Beside him, on the passenger seat, was a paper bag with a vial of cocaine inside it. The dealer they'd busted at the high school had admitted it was cocaine, and yet Patrick had to waste half his day taking it to the state lab so that someone in a white coat could tell him what he already knew. He fiddled with the volume button of the dispatch radio just in time to hear the fire department being sent to the high school for an explosion. Probably the boiler; the school was old enough for its internal structure to be falling apart. He tried to remember where the boiler was located in Sterling High and wondered if they'd be lucky enough to come out of that kind of situation without anyone being hurt.

Shots fired...

The light turned green, but Patrick didn't move.

The discharge of a gun in Sterling was rare enough to have him narrow his attention to the voice on the dispatch radio, waiting for an explanation.

At the high school...Sterling High...

Shots fired... At the high school...Sterling High...

The dispatcher's voice was getting faster, more intense. Patrick wheeled the car in a U-turn and started toward the school with his lights flashing. Other voices began to transmit in static bursts: officers stating their positions in town; the on-duty supervisor trying to coordinate manpower and calling for mutual aid from Hanover and Lebanon. Their voices knotted and tangled, blocking one another so that everything and nothing was being said at once.

Signal 1000, the dispatcher said. Signal 1000.

In Patrick's entire career as a detective, he'd only heard that call twice. Once was in Maine, when a deadbeat dad had taken an officer hostage. Once was in Sterling, during a potential bank robbery that turned out to be a false alarm. Signal 1000 meant that everyone, immediately, was to get off the radio and leave it free for dispatch. It meant that what they were dealing with was not routine police business.

It meant life or death.

Chaos was a constellation of students, running out of the school and trampling the injured. A boy holding a handmade sign in an upstairs window that read HELP US. Two girls hugging each other and sobbing. Chaos was blood melting pink on the snow; it was the drip of parents that turned into a stream and then a raging river, screaming out the names of their missing children. Chaos was a TV camera in your face, not enough ambulances, not enough officers, and no plan for how to react when the world as you knew it went to pieces.

Patrick pulled halfway onto the sidewalk and grabbed his bulletproof vest from the back of the car. Already, adrenaline pulsed through him, making the edges of his vision swim and his senses more acute. He found Chief O'Rourke standing with a megaphone in the middle of the melee. "We don't know what we're dealing with yet," the chief said. "SOU's on its way."

Patrick didn't give a damn about the Special Operations Unit. By the time the SWAT team got here, a hundred more shots might be fired; a kid might be killed. He drew his gun. "I'm going in."

"The hell you are. That's not protocol."

"There is no protocol for this," Patrick snapped. "You can fire me later."

As he raced up the steps to the school, he was vaguely aware of two other patrol officers bucking the chief's commands and joining him in the fray. Patrick directed them each down a different hallway, and then he himself pushed through the double doors, past students who were shoving each other in an effort to get outside. Fire alarms blared so loudly that Patrick had to strain to hear the gunshots. He grabbed the coat of a boy streaking past him. "Who is it?" he yelled.

"Who's shooting?"

The kid shook his head, speechless, and wrenched away. Patrick watched him run crazily down the hallway, open the door, burst into a rectangle of sunlight.

Students funneled around him, as if he were a stone in a river. Smoke billowed and burned his eyes. Patrick heard another staccato of gunshots, and had to restrain himself from running toward them blindly. "How many of them?" he cried as a girl ran by.

"I...I don't know..."

The boy beside her turned around and looked at Patrick, torn between offering knowledge and getting the hell out of there. "It's a kid...he's shooting everyone..."

That was enough. Patrick pushed against the tide, a salmon swimming upstream. Homework papers were scattered on the floor; shell casings rolled beneath the heels of his shoes. Ceiling tiles had been shot off, and a fine gray dust coated the broken bodies that lay twisted on the floor. Patrick ignored all of this, going against most of his training -- running past doors that might hide a perp, disregarding rooms that should have been searched -- instead driving forward with his weapon drawn and his heart beating through every inch of his skin. Later, he would remember other sights that he didn't have time to register right away: the heating duct covers that had been pried loose so that students could hide in the crawl space; the shoes left behind by kids who literally ran out of them; the eerie prescience of crime-scene outlines on the floor outside the biology classrooms, where students had been tracing their own bodies on butcher paper for an assignment.

He ran through hallways that seemed to circle in on each other. "Where?" he would bite out every time he passed a fleeing student -- his only tool of navigation. He'd see sprays of blood, and students crumpled on the ground, and he did not let himself look twice. He pounded up the main stairwell, and just as he reached the top, a door cracked open. Patrick whirled, pointing his gun, as a young female teacher fell to her knees with her hands raised. Behind the white oval of her face were twelve others, featureless and frightened. Patrick could smell urine.

He lowered his gun and beckoned her toward the staircase. "Go," he commanded, but he did not stay long enough to see if they did.

Turning a corner, Patrick slipped on blood and heard another gunshot, this one loud enough to ring his ears. He swept into the open double doors of the gymnasium and scanned the handful of sprawled bodies, the basketball cart overturned and the globes resting against the far wall -- but no shooter. He knew, from the overtime detail he'd taken on Friday nights to monitor high school ball games, that he'd reached the far end of Sterling High. Which meant that the shooter was either hiding somewhere here or had doubled back past him when Patrick hadn't noticed...and could even now have cornered him in this gym.

Patrick spun around to the entrance again to see if that was the case, and then heard another shot. He ran to a door that led out from the gym, one he hadn't noticed in his first quick visual sweep of the area. It was a locker room, tiled white on the walls and the floor. He glanced down, saw the fanned spray of blood at his feet, and edged his gun around the corner wall.

Two bodies lay unmoving at one end of the locker room. At the other, closer to Patrick, a slight boy crouched beside a bank of lockers. He wore wire-rimmed glasses, crooked on his thin face. He was shivering hard.

"Are you okay?" Patrick whispered. He did not want to speak out loud and give away his position to the shooter.

The boy only blinked at him.

"Where is he?" Patrick mouthed.

The boy pulled a pistol from beneath his thigh and held it up to his own head.

A new rush of heat surged through Patrick. "Don't fucking move," he shouted, drawing a bead on the boy. "Drop the gun or I will shoot you." Sweat broke out down his back and on his forehead, and he could feel his cupped hands shifting on the butt of the gun as he aimed, determined to lace the kid with bullets if he had to.

Patrick let his forefinger brush gently against the trigger just as the boy opened his fingers wide as a starfish. The pistol fell to the floor, skittering across the tile.

Immediately, he pounced. One of the other officers -- whom Patrick hadn't even noticed following him -- retrieved the boy's weapon. Patrick dropped the kid onto his stomach and cuffed him, pressing his knee hard into the boy's spine. "Are you alone? Who's with you?"

"Just me," the boy ground out.

Patrick's head was spinning and his pulse was a military tattoo, but he could vaguely hear the other officer calling this information in over the radio: "Sterling, we have one in custody; we don't have knowledge of anyone else."

Just as seamlessly as it had started, it was over - - at least as much as something like this could be considered over. Patrick didn't know if there were booby traps or bombs in the school; he didn't know how many casualties there were; he didn't know how many wounded Dartmouth-Hitchcock Medical Center and Alice Peck Day Hospital could take; he didn't know how to go about processing a crime scene this massive. The target had been taken out, but at what irreplaceable cost? Patrick's entire body began to shake, knowing that for so many students and parents and citizens today, he had once again been too late.

He took a few steps and sank down to his knees, mostly because his legs simply gave out from underneath them, and pretended that this was intentional, that he wanted to check out the two bodies at the other end of the room. He was vaguely aware of the shooter being pushed out of the locker room by the other officer, to a waiting cruiser downstairs. He didn't turn to watch the kid go; instead he focused on the body directly in front of him.

A boy, dressed in a hockey jersey. There was a puddle of blood underneath his side, and a gunshot wound through his forehead. Patrick reached out for a baseball cap that had fallen a few feet away, with the words STERLING HOCKEY embroidered across it. He turned the brim around in his hands, an imperfect circle.

The girl lying next to him was facedown, blood spreading from beneath her temple. She was barefoot, and on her toenails was bright pink polish -- just like the stuff Tara had put on Patrick. It made his heart catch. This girl, just like his goddaughter and her brother and a million other kids in this country, had gotten up today and gone to school never imagining she would be in danger. She trusted all the grown-ups and teachers and principals to keep her safe. It was why these schools, post-9/11, had teachers wearing ID all the time and doors locked during the day -- the enemy was always supposed to be an outsider, not the kid who was sitting right next to you.
```

---

## IC-2092: Not Waving But Drowning

- Title: Not Waving But Drowning
- Author (byline): Erin McKean
- Work: Machines of Death
- Publisher: Machines of Death LLC
- Publication date as stated: 2010
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2150
- Already set (do not supply): none

### Source block (context only)

```text
Author: Erin McKean
Book: Machines of Death
ISBN: 978-0446555722
Publisher: Machines of Death LLC
Date(Month/Year): 2010
```

### Introduction (context only: never use it for content warnings)

```text
The poem you just heard is by Stevie Smith and sets the stage for the short story by the same name by Erin McKean. In McKean’s futuristic world, technology has advanced to the point that a simple blood test can tell you just how you are going to die . . .not when, but how. What if your mode of death was Not Waving But Drowning by Erin McKean.
```

### Performance text (classify this)

```text
Nobody heard him, the dead man,
But still he lay moaning:
I was much further out than you thought
And not waving but drowning.

Poor chap, he always loved larking
And now he's dead
It must have been too cold for him his heart gave way,
They said.

Oh, no no no, it was too cold always
(Still the dead one lay moaning)
I was much too far out all my life
And not waving but drowning.

Everyone knows that the fourth day of ninth grade is when you get your results. I mean, that’s the way it happens in our town; other towns do it differently. But here, in our town, all the parents got together and decided that they just couldn’t take knowing before we were at least in high school. Tim K. says it’s because when you’re in ninth grade, your parents find you so annoying that they can actually bear to think about you dying.

The way it works is pretty easy. The first day of ninth grade, in homeroom, the school nurse comes in and takes blood samples. She gives a ten-minute speech about the machine and how it works. (Short answer: nobody knows, but it’s never been wrong.) She tells us that she’s going to die in a fire. She doesn’t even shiver when she tells us that—I guess when you’ve known for years and get up and talk about it every year, it becomes routine.

It’s weird to see other people’s blood. I watch the needle go in, careful not to look away. All the blood, each sample in a little barcoded tube, goes into one of those freaky BIOHAZARD mailers, and the nurse seals it in front of us. Of course it’s all anyone can talk about. Helen wants to die glamorously, like in a terrorist attack. “Do you know how much money your family gets if you die in a terrorist attack?”

Naturally, we all hoot at this—there haven’t been hardly any terrorist attacks at all, since the machine. There are still some every once in a while, in really poor places like India and Russia, where people can’t afford the test, but it’s hard to scare people about terrorism if they know they’re going to die because they stuck a fork in a toaster.

It’s hard to know what to wish for. Old age could be dying in bed, with all of your family around you, just like in a movie, with your daughter holding your hand and a room full of flowers, or it could be horrible Alzheimer’s and being tied to a bed so you don’t wander off, with no one there at all but you don’t care because you can’t remember anyone anyway. Car accident could be instant or it could be paralysis or amputation and infected bedsores that give you that staph they don’t have antibiotics for anymore. Heart failure could be a dramatic heart attack, the fall-down-clutching-your-chest kind, or it could just be you get old, your heart stops. As I said, it’s hard to know.

My mom and dad have the same one. Cancer. They met at a death party in college, where you got paired up with someone who was going to die the same way. They were the only two cancers at the party; by the time the machine came around most cancer was curable. Which sucks for them because they know they’re going to have one of the bad kinds of cancer, like ovarian or pancreatic or brain, the really painful kinds. At least now when you get those kinds of cancer the doctors know you’re going die from it, and they give you lots of painkillers. It used to be that it was hard to get painkillers, my mom told me. When her grandma died of breast cancer she was in lots of pain but the doctors wouldn’t give her drugs in case she got addicted. That’s because nobody knew she was going to die of the cancer. They thought maybe the cancer would go away and then they’d have an old lady addicted to morphine to deal with. That doesn’t happen anymore.

My brother has just “accident,” which freaks him out. It freaked us all out. Usually the machine is pretty specific. Car accident, household accident, whatever kind of accident. Just plain accident is pretty rare. For a while he went through what everyone goes through—the whole avoidy thing. He put grab bars in our shower. He walked to school, instead of riding the bus or his bike or driving.

My grandmas are both dead; one died before the machine, just had an aneurysm. The other grandma, my dad’s mom…she was one of the first ones to use the machine in their town. Her ticket said suicide. My dad said she didn’t tell anyone she was having the test. She just waited for all of them—my dad, his sister, his dad— to leave the house the next day, and then she took two bottles of sleeping pills. They didn’t even know she had them; she got the prescription in another town and had been saving them. She didn’t leave a real note. She just wrote “I’m sorry, I knew it” on her machine report and left it on the table.

My grandpa—her husband—he’s never taken the test. He says that it’s wrong to know, and that the whole human race is going to descend into mediocrity because of it. (He talks like that a lot.) He says that the fear of death, coupled with its unpredictability, is what drives humanity to achieve. He likes to talk about how there haven’t been any real scientific advances since the machine. He says everyone is too busy spending time with their families and enjoying life to do any real work.

I don’t really know too much about other people’s tickets. Most people don’t talk about it. It’s hard to know what to say, when you find out someone’s going to be shot, or hit by a car, or fall from a height. You either find yourself saying “that’s not so bad” or you just talk about something else. It’s kind of rude to ask someone that you don’t know well. And since it’s so vague, sometimes it’s hard to know what to do.

Some people you do know how they’ll die. Like, if they’re famous. Famous people’s tickets always get out. Someone they told will tell the tabloid pages—I’ve heard they pay a lot of money for famous tickets. Politicians have to disclose it. One guy who was running for governor in Tennessee faked his—his really said “shot by a hooker” and he got it to read “stroke.” Of course someone sold that story. Now the politicians have to have their tests taken in public and read right there.

The day you get your results back there aren’t any classes; you just show up for homeroom. They call you in one by one to another room to get your ticket, and then you just go home. Lots of people’s parents take the day off. If they’re really dorky they meet you at school. You can’t really hang around after, although everyone’s texting each other on their phones. Not asking, outright, just “U OK?” Lots of people don’t talk about theirs, and that’s cool. The teachers discourage it, for the most part, and sometimes your parents get mad if you tell somebody.

When they called me I felt a little nervous. Like, everyone knows they’re going to die, but it’s still a wobbly feeling to find out exactly how. My knees felt like they wanted to bend the wrong way, and I almost tripped getting out of my chair. I went into the room and sat down, and the counselor made me go through the whole routine. I had to tell him my social, twice. I had to do the iris-scanner, both eyes. I had to show him the waiver from my parents that allowed him to tell me without them present, and I had to sign a form allowing him to tell me, period, and releasing the test people from liability. Then I had to do the breathalyzer; a couple of years ago kids would show up wasted or high for their tests, so now you can’t get the results unless you’re sober.

Finally he brought out my ticket. It wasn’t in an envelope or anything, it was just the top one in his folder. The folder was black, which I thought was kind of weird. Like, why make the folder black? He was dressed in just regular clothes, tan pants and a blue shirt, no tie or anything, so the black folder just seemed kinda pretentious.

“You have a slightly unusual result,” he said. That wasn’t good. Unusual meant stuff like mauled by a bear, or electric-mixer accident, or choked on a pickle. Stupid stuff. Not dramatic or cool.

“Let me see.” I really didn’t want to wait. He pushed the ticket over to me. In block letters, it said NOT WAVING BUT DROWNING.

The man said, “It’s a line from a poem.” He held his pen like he didn’t know what it was for.

“But it still means I’m drowning, right? It’s not so bad.”

“We’d like you to have the test retaken. It’s unusual to get something like this. Something so…allusive.” I looked at him. He hadn’t done a good job shaving that morning; it looked like he used a real razor and not a depilatory laser. Maybe his ticket said he’d be killed by a laser?

“I don’t know. I like this one. What if it changed to something worse?”

“That doesn’t really happen. They don’t change. Sometimes they get more specific—we think yours would get more specific.”

“I think I’m good with vague, thanks. Vague and poetic is okay with me.”

“Are you sure? You could retake now…” I noticed that he had a test kit, too, next to his chair.

“Nah. I’m okay.” I put my ticket in my bag, careful not to fold it. Some people framed theirs, and kept it somewhere safe, especially if it was a cool one, like “saving a child.” Mine was totally frameable.

“If you change your mind, here’s a number to call.” He beamed a number to my phone from his pen.

“And we’d like your permission to keep a tracer on you, so that our department will be alerted when you die.”

Wow—I was important enough to have a tracer? That was also cool. I couldn’t decide if I’d tell anyone about the ticket, but I could definitely tell people I had a tracer.

“Sure, okay.” He pushed another form to me.

“We have to let you think about this one for twenty-four hours, and your parents have to sign it, too. I have to disclose to you that tracer information is subpoenable, which means that if you are accused of a crime the data from the tracer can be used by the prosecution and the defense. You can drop off the form in homeroom tomorrow.” He stood up, so I got up, too. He shook my hand. “I think you are a remarkable young woman,” he said, like he didn’t say that to everyone. “Please use this knowledge to focus and direct your life, and to live while you can.” Then he recited the machine motto, Dum vivimus vivamus. Although nobody really knows Latin anymore, everyone knows that bit. It means “while we live, let us live.”

My folks were home, and I think they had been crying. It’s hard to think of people you love dying. Like they thought if they didn’t know, I’d live forever or something. My dad gave me a big hug and kind of sniffled, before I even showed him the ticket, which was weird. I didn’t really know what to say about the ticket, so I just pulled it out and showed it to them. “The guy said it was from a poem.” My folks looked a little shocked, but then my mom just googled up the poem on the living room screen. We just stood there and read it, and clicked through to read about the poet. It was by somebody named Stevie Smith. She died of a brain tumor, which was as close as you could get back then to knowing for sure how you were going to die. Not a lot of people survived brain tumors. I kind of liked that she died that way. Not that she died, of course, but that she probably knew.

The fact that it was a line of a poem: cool. The fact that I could get a tracer: cool. Drowning: not so bad. I’d heard it was peaceful. I pulled up the poem again and made it the background on my screen. I think I’ll leave it there for a little while.
```

---

## IC-2093: The Nutcracker

- Title: The Nutcracker
- Author (byline): Not specified
- Work: Not specified
- Publisher: Atheneum
- Publication date as stated: October 1981
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 593
- Already set (do not supply): none

### Source block (context only)

```text
Author: E.T.A. Hoffman
ISBN: 978-0027474701
Publisher: Atheneum
Date (Month/Year): October 1981
```

### Introduction (context only: never use it for content warnings)

```text
At Christmas time my mother always gets out the tree ornaments, something to hang on the door, a village, a nativity set, and The Nutcracker Retold by: E.T.A. Hoffman
```

### Performance text (classify this)

```text
Retold By E.T.A. Hoffman

It is Christmas Eve and glistening snow falls softly on a small town in Germany. Bright silver bells ring out through the frosty air as horse-drawn sleighs are pulled through the streets to the Silberhaus home. Judge Silberhaus, his wife, and their two children, Clara and Fritz, joyfully greet their guests as the scents of pine needles, cinnamon, and clove-studded apples draw the party to the ballroom. Gaily wrapped gifts are admired and then happily exchanged before the magnificent tree, laden with tiny glass ornaments, golden tinsel, and flickering candles.

Suddenly there appears a special guest, Clara’s godfather, Doctor Drosselmeyer. It is rumored that he is not an ordinary doctor and that he possesses strange and mysterious powers. To Fritz, he gives a splendid army of small wooden soldiers. For Clara, there is a special surprise.

Doctor Drosselmeyer reaches deep within the folds of his satin cape and slowly withdraws a finely carved Nutcacker. “Oh, thank you, dear Godfather!” says Clara, gently cradling the doll while lightly stroking its soft curly beard. “Give him to me,” Fritz demands, seeing what an excellent leader the Nutcracker will make for his new soldiers. He grabs the Nutcracker from Clara’s arms, but as the starts across the room, he trips and drops the Nutcracker to the floor. The Nutcracker is broken! Doctor Drosselmeyer picks up the doll and places it carefully in Clara’s arms.

It is growing late and the party draws to a close. “Merry Christmas!” call the guests as they step out into the cold wintry night. Clara and Fritz are tucked into bed and kissed good night. The candles are snuffed, moonlight drifs through the frosted windows, and the house grows still….

…except in Clara’s room. Deep in the shadows, Doctor Drosselmeyer Quietly repairs the broken Nutcracker. When he has finished, he places the doll next to Clara and disappears.

The grandfather clock strikes 12 and awakens Clara. She hears a faint noise and sees her bedroom window slowly open.

Great gray mice pour into Clara’s room, led by a ferocious mouse with seven heads—the Mouse King. Suddenly, the Nutcracker calls in Fritz’s soldiers to lead them into battle.

Bayonets flash and hissing fills the air. Without warning, the Mouse King attacks the Nutcracker form behind. Clara screams and pulls the Mouse King’s lashing tail. As the giant mouse turns toward Clara, the Nutcracker raises his sword and slays the giant mouse.

The Nutcracker turns and faces Clara. He is no longer a doll. He is now a young Prince. He removes a crown from the Mouse King and places it gently on Clara’s head. “You saved my life,” he says, “and I crown you Princess Clara. Come! My kingdom is near.”

The Prince takes Clara’s hand and their journey begins. Sparkling snow falls about them though it is not cold.

They run through glittering ice crystals in the Land of Frost.

Soon they come to gates of sparkling spun sugar. Peppermint sticks line a candy road. The soft breezes of spring are all about them. “Hurry,” says the Prince. “They are waiting.”

At he end of the road stands a glowing castle, made entirely of marzipan. “Welcome,” says the Sugar Plum Fairy. “Your kingdom awaits your return,” trumpets sound and music fills the air, The celebration begins.

Clara and the Prince join hands and dance, and they dance far into the night. And as they dance their final waltz, pink and gold clouds flow about them and the pale sun begins to rise.
```

---

## IC-2094: The October Game

- Title: The October Game
- Author (byline): Ray Bradbury
- Work: Stories of Ray Bradbury, Pg 787-792
- Publisher: Knopf
- Publication date as stated: 1980
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MICH, NARRATOR, MARION, DOCTOR, CHILD, CHILD 2, LOUISE
- Teaser before the introduction: Yes
- Spoken words (computed): 1166
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ray Bradbury
Book: Stories of Ray Bradbury, Pg 787-792
ISBN: 978-0394513355
Publisher: Knopf
Date (Month/Year): 1980
```

### Introduction (context only: never use it for content warnings)

```text
The October Game by Ray Bradbury
```

### Performance text (classify this)

```text
MICH: (Pg 787-792) (Holding up a gun and examining it closely – he shakes his head an places the gun back in a bureau drawer) No, not that way. Louise wouldn’t suffer that way. She would be dead and it would be over and she wouldn’t suffer. It’s very important that this thing have, above all, duration. Duration through imagination. How to prolong the suffering? How, first of all, to bring it about? Well . . .

NARRATOR: He paused long enough to hear the children run by swiftly on the street below, outside this warm two-story house; like so many gray mice the children, like so many leaves. By the sound of the children, you knew the calendar day. By their screams you knew what evening it was. The last day of October, with white bone masks and cut pumpkins and the smell of dropped candle fat. There was a soft running in the hall.

MICH: That’s Marion. My little one. All eight quiet years of her.

NARRATOR: His daughter had been in and out all evening, trying on various masks, asking him which was most terrifying, most horrible. They had both finally decided on the skeleton mask. It was “just awful!” It would “scare the beans” from people! He had never liked October. Ever since he first lay in the autumn leaves before his grandmother’s house many years ago and hear the wind and saw the empty trees. It had made him cry, without a reason. And a little of that sadness returned each year to him. It always went away with spring. But, it was different tonight. There would be no spring. He had been crying quietly all evening. It did not show on his face. It was all hidden somewhere and it wouldn’t stop. There was a mouse-rustle in the hall. Marion appeared in the door, all skeletonous in her disguise.

MARION: How do I Look, Papa?

NARRATOR: From under the mask, blonde hair showed. From the skull sockets small blue eyes smiled. What alchemy had there been in Louise that bleached the dark brown eyes and black hair of a dark man? She had produced a child in her own image, and, to top it, she had somehow fixed the doctor.

DOCTOR: (shaking his head) Sorry, Mr. Wilder, your wife will never have another child. This is the last one.

MICH: And I wanted a boy.

NARRATOR: He almost bent to take hold of Marion now, in her skull mask. He felt pity for her, because she had never had a father’s love, only the crushing love of a loveless mother. But most of all he pitied himself, that he had not made the most of a bad birth, enjoyed his daughter for herself, regardless of her not being dark and a son and like himself. Somewhere he had missed out. Now it was October again. There had been other Octobers and when he thought of the endless months trapped with a woman and child, neither of whom loved him, he had been filled with horror . . . year after year. He simply could not wear this one through. There was an acid walled off in him that slowly had eaten through tissue and bone over the years, and now, tonight, it would reach the wild explosive in him and all would be over!

MICH: (hesitating) What was all this? Where had it gone wrong? Certainly not with the birth of the child alone.

NARRATOR: Why didn’t he just turn, pack a suitcase, and leave? No. Not without hurting Louise as much as she had hurt him. It was simple as that. Divorce wouldn’t hurt her at all. It would simply be an end to numb indecision. If divorce would give her pleasure in any way, he would stay married the rest of his life . . . for damned spite. No, he must hurt her.

MICH: Figure some way, perhaps, to take Marion away from her, legally. Yes! That was it. That would hurt most of all. To take Marion away. (He smiles as disturbing smile and bends to scoop Marion up in his arms) Here we go . . . (he exits with her to the cellar) *****

MICH: (mimes, washing his hands and face and drying them off with a towel)

NARRATOR: [Later that evening] there was a mad ringing of the bell below. There were vast bowls of punch, stringed apples in each door. There was a water tub in the center of the living room, waiting, with a sack of apples nearby, for dunking. There were shouts and hilarity. He walked to the top of the stairs. Louise was below, tall and slender and blonde, laughing down upon the new children.

MICH: (putting on his party mask, he shouts with forced happiness) Hello down there!

CHILD: (shouting and waving) Hi, Mr. Wilder!

NARRATOR: He took the party right out of Louise’s hands. He supervised pin the tail on the donkey, spin the bottle, and musical chairs, amid fits of shouting laughter. Then, all house lights out, he cried . . .

MICH: Hush! Follow me! (tiptoeing toward the cellar)

NARRATOR: The parents commented to each other, nodding at the clever husband, speaking to the lucky wife. How well he got on with children they said.

MICH: (In an ominous whisper) The cellar! The tomb of the witch! (mock shivering he speaks the incantation loudly) Abandon hope all ye who enter here!

NARRATOR: The parents chuckled. Everybody talked at once. Everybody but Marion. The upper house was empty and silent in the candle-shine . . . They sat in a vast circle in the cellar. Twenty squealing children, twelve relatives, with Louise down at the far end. The entire program from here on was to be enacted in the dark.

MICH: Now! Quiet! . . . . The witch is dead, she has been killed, and here is the knife she was killed with.

NARRATOR: He handed over the knife. It was passed from hand to hand around the circle . . .

MICH: (whispering) The witch is dead, and this is her head.

(handing another item to be passed around)

CHILD: (excitedly) Oh, I know this game! He gets some old chicken innards from the ice box and hands them around and says, “These are her innards!” I know how this is played!

CHILD 2: Hush you’ll spoil everything!

MICH: The witch came to harm, and this is her arm!

NARRATOR: The items were passed and passed around the circle. Some children screamed, wouldn’t touch them.

CHILD: Eeeee!

CHILD 2: (giggling) Aw, it’s only chicken insides. Come back, Helen!

MICH: The witch cut apart, and this is her heart.

LOUISE: Marion, don’t be afraid; its only play. (silence) Marion? Are you afraid? (silence)

MICH: She’s all right. She’s not afraid.

NARRATOR: On and on the passing, the screams, the hilarity. The autumn wind signed about the house. And he, the husband, stood at the head of the dark cellar, intoning the words, handing out the items.

LOUISE: Marion? Marion? Marion, answer me, are you afraid? (Silence) Where’s Marion?

CHILD: Maybe she’s upstairs?

LOUISE: Marion, Marion! (panicking) Turn on the lights!

NARRATOR: Everybody quieted. The items stopped passing. The children and adults sat with the witch’s items in their hands.

LOUISE: (gasping) No . . . No . . . Don’t turn on the lights, oh, God! God, don’t turn them on, please. (voice rising to a shriek) Don’t turn on the lights, don’t!

NARRATOR: Nobody moved. Everyone sat in the dark cellar, suspended in the suddenly frozen task of this October game. The wind blew outside, banging the house. The smell of pumpkins and apples filled the room with the smell of the objects in their fingers.

CHILD: I’ll go upstairs and look!

NARRATOR: And he ran upstairs hopefully and out around the house, four time around, calling

CHILD: Marion . . . Marion . . . Marion!

NARRATOR: At last, coming slowly down the stairs into the waiting cellar and saying to the darkness

CHILD: I can’t find her.

NARRATOR: Then . . . some idiot turned on the lights.
```

---

## IC-2095: Of a Pig and a Spider and Bearing the Unbearable

- Title: Of a Pig and a Spider and Bearing the Unbearable
- Author (byline): Barbara Mahany
- Work: Not specified
- Publisher: Pull Up a Chair.org
- Publication date as stated: Sept 20, 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 905
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barbara Mahany
ISBN: On-Line Transcript
https://pullupachair.org/2013/09/20/of-a-pig-and-a-spider-
and-bearing-the-unbearable/
Publisher: Pull Up a Chair.org
Date (Month/Year): Sept 20, 2013
* Link to the article from which these quotes were taken
“The 60th Anniversary of Charlotte’s Web: Charlotte and
the Museum”
https://www.amnh.org/explore/news-blogs/news-posts/e.-
b.-white-s-charlotte-s-web-and-the-museum
```

### Introduction (context only: never use it for content warnings)

```text
Children’s books occupy a privileged space in our psyches. They are what we read for comfort; what we pass on to our own children, or to those we teach; and what we return to or should return to as adults for reasons of nostalgia or rediscovery.

Sadly, there are times in adult life – even my young “almost adult” life when the world seems filled only with anger, division and hatred. It’s a world devoid of heroes and the barrage of negative news reports is just too much to bear. It's in those moments that children's books, for me, do that which nothing else can. They speak of hope. They tell me, through the medium of wizards and lions and talking spiders, that bravery still matters, wit matters, empathy matters, love matters. These things may or may not be true. . . . I hope they are.

Of a Pig and a Spider and Bearing the Unbearable by Barbara Mahany
```

### Performance text (classify this)

```text
Maybe it was all the hours curled up on my patchwork quilt, pretending I had a fever so I could stay home to read instead of going to church. Maybe it was the time travel. Or the slipping quietly into someone else’s heart, someone’s secret hideaway. But the hold that children’s books had on me, has never lifted.

I tiptoe my fingers across the bookshelves and feel the quickening in my heart. There’s Miss Rumphius and her lupine seeds. There’s The Secret Harden and orphaned Mary Lennox slipping into the secret locked garden of her uncle’s great house on the Yorkshire moors. There’s the Little House in the Big Woods, where Laura Ingalls Wilder made me feel the icy morning cold and hunger for prairie porridge. There’s Tasha Tudor, she who launched a thousand dreams and made me see the magic in a single tulip’s petal.

And then there’s Charlotte and her web. And Wilbur who ever breaks my heart and fills it up again.

So, no wonder when the call went out from my sweet boy’s reading teacher for grownups to come to class, to bring along a book that they read and re-read in days gone by, I turned rather swiftly to a spider and a pig and a girl named Fern whose cry for justice never has died down.

“Where’s Papa going with that ax?” said Fern to her mother as they were setting the table for breakfast.

“Out to the hog house,” replied Mrs. Arable. “Some pigs were born last night.”

“I don’t see why he needs an ax,” continued Fern, who was only eight.

“Well,” said her mother, “one of the pigs is a runt. It’s very small and weak, and it will never amount to anything. So your father has decided to do away with it.”

“Do away with it?” shrieked Fern. “You mean kill it? Just because it’s smaller than the others?”

And so, with those four questions, Fern leaped to the top of my hero’s heap.

And as Kate DiCamillo writes in the forward to the 60th edition of E.B. White’s classic, Charlotte’s Web, the crux of its miracle is this: “Within the confines of its pages, something terrible, something unbearable, happens. And yet, we bear this unbearable thing. And in the end, we even rejoice.”

Later, DiCamillo goes on: “It is also E.B. White’s promise to his reader: Things will continue; life will go on. It will be beautiful, astonishing, heartbreaking. And as long as you keep your eyes and heart open to the wonder of it, as long as you love; it will be okay.”

No wonder it is among the holiest of acts to slide a Charlotte’s Web, a Miss Rumphius, a Secret Garden, into the hands of a child, one whose circles are just beginning to expand beyond being fed, and tucked in at night, beyond the reminders to brush teeth, and the taping of bandages across skinned knees.

It is through the pages of a beautifully wrought, deeply inscribed book that a child slaps on her or his first explorer suit, and sets sail across rocky seas, and steps into tangled shadowed woods.

While that child might get lost in the depths of those pages, forget that he’s curled under the covers in his very own bedroom, with his very own baseball trophies lined across the sill, and his very own mama banging pots and pans down in the kitchen, the holy resurrection of reading is that the terrors and the unbearability and the broken hearts belong inside the pages. And in time, that child can shake it off, and tuck the whole heart-stretching exercise back between the covers. Yet go forward, having held on tight through the tug and pull and breath-catching, and be just a squidge more ready to encounter the real-life bumps and hurricanes. Or simply to understand those encountered by fellow travelers.

And isn’t that, in the end, the children’s gospel, and the scripture that carries them to mountain tops and certain shores?

Because I’ve been enchanted all week with a particular spider and a pig, and scribbling madly in the margins, I thought I’d leave you with a few fine [thoughts]. One, from the American Museum of Natural History, that tells the backstage tale of the curator in the museum’s department of insects and spiders on whom E.B. White heavily relied for scientific detail on the Aranea Cavatica, the species of barn spider to which Charlotte belonged.

The publisher, Harper & Brothers, had misgivings about the death of the heroine in what was essentially a children’s book but “on this point [White] refused to budge,” writes Sims in The Story of Charlotte’s Web. “Natural history could not be dodged: Charlotte’s species of spider dies after spinning its egg sac.” *

White’s choice stands the test of time. Charlotte’s Web is as popular and enduringly poignant as when Eudora Welty first described it in her 1952 review. “What the book is about,” Welty wrote, “is friendship on earth, affection and protection, adventure and miracle, life and death, trust and treachery, pleasure and pain, and the passing of time. As a piece of work it is just about perfect, and just about magical in the way it is done.” *

[So as you go forward], be gentle to spiders and runt piglets. And cheer little girls — and boys — who speak out against axes and injustice.
```

---

## IC-2096: The Old Turtle and the Broken Truth

- Title: The Old Turtle and the Broken Truth
- Author (byline): Douglas Wood
- Work: Not specified
- Publisher: Scholastic Press
- Publication date as stated: March 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1191
- Already set (do not supply): none

### Source block (context only)

```text
Author: Douglas Wood
ISBN: 978-0439309080
Publisher: Scholastic Press
Date (Month/Year): March 2007
```

### Introduction (context only: never use it for content warnings)

```text
To all who seek truths and who listen to the language of the breezes . . . . author Douglas Wood expresses a desire for our collective conscience. He gently proposes a world where tranquility is dependent on mutual understanding. A healed world can come from acceptance. The Old Turtle and the Broken Truth by Douglas Wood.
```

### Performance text (classify this)

```text
Inscription: To all who seek truths and who listen to the language of breezes. (And turtles.)

Once, in a beautiful, far away land…where every stone was a teacher and every breeze a language, where every lake was a mirror and every tree a ladder to the stars, into this far and lovely land there fell…a truth.

It streaked down from the stars, trailing a tail as long as the sky. But as it fell, it broke.

One of the pieces blazed off through the night sky, and the other fell to earth, Crow found the fallen piece. It seemed to be a sort of stone. He picked it up.

“This is a lovely truth,” said crow. “I will keep it.” But after he had held it for awhile. “This truth does not feel quite right. A part of it is missing. I will look for a whole one.” He flew off and dropped it to the ground.

Butterfly and Bear discovered the truth, drawn by its sweetness. But each found that it left a bitter taste after all. “There is something missing in this truth.” And they left it alone.

Then a human being found it.

He was walking slowly, listening to breezes, gazing at beauties above and below and all around him, when he found the broken truth. On it was writing, and the writing said: “YOU ARE LOVED.”

The man held it carefully, thinking it was the loveliest thing he had ever seen.

The man took the wonderful truth to his people --- those who lived with him, who spoke as he spoke and dressed as he dressed and whose faces looked like his.

And together they cherished their newfound truth and believed in it.

After a while, the man and his people did not hear the language of breezes and stones anymore, but heard only their truth. And for them, it was enough.

And they called it…The Truth.

The Truth made the people feel good and proud and strong. But soon they also began to feel fear and even anger toward those who were not like themselves.

Time passed, and other people said, “We must have this Great Truth for ourselves, for with it comes happiness and power.”

Many battles were fought, and the broken truth was won and lost, won and lost, over and over again.

The stones and trees suffered. The breezes and waters suffered, and the animals, and the earth….and most of all, the people suffered.

Finally, the animals went to Old Turtle --- ancient and wise as the mountains and seas themselves.

“This truth the people quarrel over,” they said, “It is broken and does not work. Please tell the people.”

“I am sorry,” answered Old Turtle, “but the people will not listen. They are not yet ready.”

And the suffering continued. Until one day…a Little Girl came to find Old Turtle. She had crossed the Mountains of Imagining and the River of Wondering Why, she had found her way through the Forest of Finding Out. And when she had grown tired, she had ridden on the backs of animals or the wings of birds, and they helped her find her way.

When she saw Old Turtle, she could hardly speak.

“Why have you come so far to find me, Little One?” asked Old Turtle. Her voice rumbled like far away thunder, but was soft as the breeze through a caterpillar’s whiskers.

The Little Girl <said>. “Where I live, the earth is sore, and people are suffering. Battles are fought, over and over again. People say it has always been this way and will never change. Can it change, Old Turtle?

Old Turtle spoke. “The world you describe is not the world that has always been, Little One.”

Then Old Turtle told of how the people had found the broken truth, and the suffering it caused.

“It is because it is so close to a great, whole truth that is has such beauty, and that the people love it so,” said Old Turtle. “It is the lost portion of the broken truth that the people need, if the world is to be made whole again.”

Asked the Little Girl. “Can we put the truth back together again?”

“First, my child,” said Old Turtle, “remember that there are truths all around us, and within us. They twinkle in the night sky and bloom upon the earth. They fall upon us every day, silent as the snow and gentle as the rain. The people, clutching their one truth, forget that it is a part of all the small and lovely truths of life.

For a long time then the two friends were quiet, high on their hill in the very center of the world.

Finally, the Little Girl asked one more question. “Old Turtle how will the people learn these things?”

“By listening once more to the languages of breezes, by learning lessons from stones and animals and trees and stars. Even turtles,” she chuckled, “and little girls.

It is time for you to go, to return to your people and tell them what you have learned, and to help them mend their Broken Truth.

“Take this with you,” said Old Turtle, as she placed something in the Little Girl’s hand. “I have saved it for a very long time, for someone just like you.”

The Little Girl looked: It was a kind of stone, a mysterious, beautiful stone. It was lovely to touch, and it made her feel good to hold it.

“Thank you, Old Turtle,” And then she started home.

Once more Crow led the way, and again when the Little Girl grew tired, all her animal friends helped. She sometimes touched the stone Old Turtle had given her to renew her strength. And it took a long time yet almost no time at all…

But it had been a very long journey, and those who take great journeys of the heart are changed.

The people did not recognize her. And when she spoke, they did not understand. She spoke of a world made of small and gentle truths, of all the peoples being one People. But they could not catch her meaning.

Finally, Crow, flew to the place high above the village where the Great Truth was kept. He cawed in his loudest voice. The Little Girl knew what to do. She climbed to the high place herself. She took Old Turtle’s stone from her pocket and…carefully...added the missing piece to the old, broken one.

The fit was perfect.

“YOU ARE LOVED . . . AND SO ARE THEY.”

Some smiled.

And some cried.

And they began to understand.

Time passed and upon the beautiful land the trees climbed like ladders to the stars, the waters shone like mirrors, and the people saw their beauty. A breeze stirred and they heard its music. Tiny truths fell by day and night, and the people found them and kept them in their hearts.

And slowly, as the people met other people different from themselves, they began to see…themselves.

And far away, on a hill in the very center of the world…Old Turtle smiled.
```

---

## IC-2097: One Hot Mess

- Title: One Hot Mess
- Author (byline): Carmen Agra Deedy
- Work: Funny Girl: Funniest Stores Ever, Pgs 43-61
- Publisher: Viking Books for Young Readers
- Publication date as stated: May 2017
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: CARMEN, MAMI, PAPI, RONALD, RONALD’S DAD
- Teaser before the introduction: Yes
- Spoken words (computed): 1590
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carmen Agra Deedy
Book: Funny Girl: Funniest Stores Ever, Pgs 43-61
ISBN: 978-0451477316
Publisher: Viking Books for Young Readers
Date (Month/Year): May 2017
```

### Introduction (context only: never use it for content warnings)

```text
It’s true, every family is crazy in their own special way – and Carmen’s Cuban-American family is chock full of wild and unforgettable traditions. But sometimes, even the weirdest family moments can bring us closer together -- For instance, has anyone in your family ever set a bathtub on fire?

One Hot Mess by Carmen Agra Deedy
```

### Performance text (classify this)

```text
CARMEN: (Pgs 43-61) When you're a kid you think your family is normal. You assume everybody has a family that celebrates New Year's Day with a Jell- O fight on the lawn, or [a mom who] sets a fire in the bathtub on moving day . . . A little background on that last one.

My parents were Cuban refugees. We grew up in a small Southern town where they worked, paid taxes, and went to church. As far as I could tell, they were pretty ordinary people.

Okay, so maybe my mother liked to clean -- a lot. She descended from a long line of Iberian women who believed it their mission to rid the world of dirt and grime. In her defense, my mother's grandmother and sister both died of typhoid fever in 1930’s Havana. This terrible loss marked the beginning of Mami's lifelong campaign against "The Godless Germ." As part of her arsenal, she kept a spray can of Lysol disinfectant tucked in her pocketbook.

MAMI: (spraying Lysol everywhere, speaks with a strong Cuban accent) Danger never takes a holiday and nothing is more dangerous than The Godless Germ!

CARMEN: I never thought any of this odd, until the year I turned nine. It was our fourth move in five years. My dad, Papi, was a steel worker, and money was always tight. We would stay in a place until the rent went up, and then we'd pull up stakes and move into another house usually no more than two or three blocks and a decade older than the last one.

But this time was different. Papi's willingness to work extra hours at the steel mill had earned him a raise, and our family the nicest place we had rented yet. No more crappy old clapboard houses with rusted faucets, warped windowsills, and bathrooms with chipped tiles. No sirree. We were moving into an apartment complex with a flower bed in the parking lot, and a swimming pool.

I remember how excited Marni was when we walked into apartment number eight. It was freshly painted and carpeted, and everything smelled of newness with a capital N. Even our battered furniture looked a little brighter. When Papi arrived with hamburgers from the corner diner, I just knew this day couldn't possibly get any better.

PAPI: I’m going back to the house for the last load.

CARMEN: (to Papi) Wait for me! (to audience) I shoved the last bites of greasy burger into my mouth, pushed the chair away from the table, and headed after him. When I stepped outside, a shaggy-haired kid was bouncing an old tennis ball against the wall next to our apartment.

RONALD: (bouncing the ball) You moving into number eight?

CARMEN: (to audience) I beamed at him what I hoped was my most winning "you-bet-I-am-and-is-today-your-lucky-day-or-WHAT-because-you-get-dibs-on-the-new-kid" smile. (to Ronald) You wanna watch my mom set fire to the bathtub?

(to audience) He just stared at me with luminescent green eyes that reminded me of winter antifreeze. Then, in infinitesimal increments -- like molasses seeping from a broken jar along a cold winter floor, one millimeter at a time -- a smile spread across his face. It kept spreading, until it bunched up his cheeks and reached his eyes. Then, and only then, did he speak.

RONALD: Boy howdy, do I!

CARMEN: Great! Come on! She's almost ready. (to audience) He followed me into the apartment without hesitation. I watched him take in the neat rows of labeled boxes, the cheap Naugahyde recliner, the shiny Formica kitchen table. A perplexed look settled on his face.

RONALD: So, is your mama a pyro? 'Cause this don't look like no pyro's house; you still got plenty of stuff that'll burn.

CARMEN: What's a pie-rou?

RONALD: Somebody who lights stuff on fire so's they can watch it burn.

CARMEN: No! My mom doesn't like to watch the bathtub burn. She likes to watch the germs die.

RONALD: (with a shocked look) She . . . say what?

CARMEN: The look on his face made that hastily eaten burger stir treacherously in my stomach. Until that instant, I'd genuinely believed that everyone's mother did this. A hot, prickly sensation crept its way up my neck. I recognized it for what it was: shame. Burning a bathtub was weird. (to Ronald, stammering) L-I-let me explain.

RONALD: I cain't wait to hear.

CARMEN: (to audience) So I told him. I told him about my mother's dead grandmother and sister back in Cuba. I told him about the spray can of Lysol in her pocketbook. I told him the world was filled with all manner of invisible bugs just waiting to eat out your brains and turn your guts to mush and kill you deader than dead with just an innocent swipe of a doorknob. And when I finished telling, do you know what he did? (beat)

RONALD: (laughing uproariously)

CARMEN: He laughed. He laughed so hard he wheezed. He laughed so long he swallowed his gum and coughed it back up again. And do you know what I did? (punches) I punched him in the arm.

RONALD: (stumbling sideways and laughing harder)Easy, girl. (more laughing) You got a mean right hook there.

MAMI: What is going on here ...?

CARMEN: Mami stood in the doorway and looked from me to this alien child and back again. (to Mami) He's my friend. His name is. . . (whispering to Ronald) What's your name?

RONALD: (to Mami) My name's Ronald, ma'am. Wayne Ronald Harding, but ever'body calls me Ronald.

CARMEN: My mother nodded, as if this was enough information for anybody.

MAMI: (turning to Carmen) I find the matches. The bathtub, she burn in ten minutes.

CARMEN: And I was relieved when she turned on her heel and disappeared down the short hall. (to Ronald) This is kinda crazy, huh?

RONALD: It's better'n crazy. This here's an opportunity. (leans in and whispers) Let's sell tickets!

CARMEN: And that's what we did. Ronald rustled up a half dozen of his friends and told them that, for a quarter, they'd see something worth telling their grandchildren about someday. I stood in front of the door to number eight and explained what was about to happen to the small but eager crowd.

First, I said, my mom would scrub the bathtub with a bristle brush. Then she'd make certain there was nothing flammable in the room. As an added precaution, she'd place a bucket of water on the toilet. Next, she'd screw off the lid of a sixteen-ounce bottle of isopropyl alcohol and cover the tub's surface.

Then, and only then, would she strike the match and toss it in. I'd seen her do it time and again. It was a marvelous sight. Those old ceramic tubs would burst into flames, and just as quickly the fire would burn itself out.

RONALD: (to the crowd of kids) Now, I ask you, ain't that the dangdest thing y'all ever heard? So, who's in?

CARMEN: Kids tripped over one another to hand over their quarters. Mami was visibly startled when she saw me coming down the hall, a mob of children following along behind. (pleading with Mami) Can they watch, too?

MAMI: (shakes her head) Ay, ay, ay!

CARMEN: But then she put aside whatever misgivings she may have had; she had work to do. The Godless Germ waits for no woman, and we had to have baths that night.

MAMI: (to the crowd) Okay, childrens. You no go in bathroom. You stay in door. NO GO IN. Me comprenden?

CARMEN: Whether they understood or not, no one was leaving. No one was breathing. This was a tale, as Ronald had promised, that they would tell their grandchildren.

My mother unscrewed the top of the bottle of alcohol. She moved the bucket of water closer to the tub. She upturned the bottle and drained the contents with great care. She reached into her apron pocket and drew from it a small box of wooden matches -- The crowd pressed forward.

MAMI: Tranquilos!

CARMEN: Again, no one moved. But all eyes watched as she struck the match and tossed it in a perfect flaming arc into the bathtub. The brand-spanking-new FIBERGLASS bathtub. The thing lit up like kerosene-soaked kindling. The plastic melted and warped as the fire spread.

Kids began to shriek as they scattered in a panic for the front door. Only three people held their ground: my mother, who flipped on the bathroom faucet and splashed bucket after bucket onto the flames; me, too terrified to run, or scream, or be of any use to anyone whatsoever; and Ronald. Well. . . Ronald actually disappeared briefly. He returned moments later, followed by a man in a ribbed white T-shirt who was carrying a fire extinguisher.

RONALD’S DAD: (puts out the fire with the extinguisher)

CARMEN: Within seconds the bathroom was a blanket of white foam, giving the room the look of a peaceful, if bizarre, Christmas postcard -- so long as you were unaware of the horror that lay beneath.

RONALD’S DAD: (softly and unflustered) Now, that is one hot mess, ma'am! (beat) I just gotta ask. What in the world made you want to light a tub on fire?

CARMEN: (to Ronald’s Dad) She had to kill The Godless Germ!

RONALD’S DAD: (nodding and chuckling) Well, I reckon that explains it about as well as anything.

CARMEN: None of the apartment kids were allowed to play with me after that day. Heck, they weren't even allowed to pass my door without an escort. Except for Ronald. He showed up the next morning.

RONALD: Hey!

CARMEN: I'm surprised your parents let you talk to me.

RONALD: Ain't got parents; got a dad. You met him. He's a firefighter, down Ladder 11 way. He said to call him if anything else catches fire!

CARMEN: (embarrassed) You're not funny! (to audience) My face felt as hot as melting fiberglass.

RONALD: You know, I had me an uncle once who swore up and down that for every lie I told, Santa Claus would have to eat one of his reindeer.

CARMEN: That's crazy . . .

RONALD: It's only crazy when somebody else's family does it.

CARMEN: And I knew then that Wayne Ronald Harding and I would be friends forever. (beat) Or at least until the rent went up again.
```

---

## IC-2098: A Package for Mrs. Jewls

- Title: A Package for Mrs. Jewls
- Author (byline): Louis Sachar
- Work: Wayside School is Falling Down (Pg 21-31)
- Publisher: HarperCollins
- Publication date as stated: Mar 2019
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, LOUIS, TRUCK DRIVER, MRS. JEWLS, ALLISON, JASON, JENNY, JOHN, CHILDREN, ERIC, TERRENCE, MAURECIA, TODD, JOE
- Teaser before the introduction: Yes
- Spoken words (computed): 857
- Already set (do not supply): none

### Source block (context only)

```text
Author: Louis Sachar
Book: Wayside School is Falling Down (Pg 21-31)
ISBN: 978-0380754847
Publisher: HarperCollins
Date (Month/Year): Mar 2019
```

### Introduction (context only: never use it for content warnings)

```text
A Package for Mrs. Jewls from Wayside School is Falling Down by Louis Sachar
```

### Performance text (classify this)

```text
(Louis enters, shaking his head and frowning at the mess he sees all over the playground)

NARRATOR: The school yard was a mess. There were pencils and pieces of paper everywhere.

LOUIS: (muttering aloud) How’d all this junk get here? Well, I’m not going to pick it up!

NARRATOR: It wasn’t his job to pick up garbage. He was just supposed to pass out the balls during lunch and recess, and also make sure the kids didn’t kill each other.

LOUIS: (heavy sigh and begins to pick up the trash)

NARRATOR: [You see,] he loved all the children at Wayside School. He didn’t want them playing on a dirty playground. As he was picking up the pencils and pieces of paper, a large truck drove into the parking lot.

(DOUBLE HONK . . . DOUBLE HONK)

LOUIS: (running out to the truck – he speaks in a loud whisper) Quiet! Children are trying to learn in there! (he points at the school)

TRUCK DRIVER: (stepping out of the truck) I have a package for somebody named Mrs. Jewls.

LOUIS: I’ll take it.

TRUCK DRIVER: Are you Mrs. Jewls? I have to give it to Mrs. Jewls.

NARRATOR: Louis thought a moment. He didn’t want the man disturbing the children. He knew how much they hated to be interrupted when they were working.

LOUIS: (in a falsetto voice) I’m Mrs. Jewls.

TRUCK DRIVER: But you just said you weren’t Mrs. Jewls,

LOUIS: (still falsetto) I changed my mind.

NARRATOR: The man got the package out of the back of the truck and gave it to Louis.

TRUCK DRIVER: Here you go, Mrs. Jewls.

LOUIS: (taking the package and grunting from the weight) Uhh!

NARRATOR: It was a very heavy package. The word FRAGILE was printed on every side. He had to be careful not to drop it. The package was so big, Louis couldn’t see where he was going. Fortunately, he knew the way to Mrs. Jewls’s class by heart. It was straight up.

Wayside School was thirty stories high, with only one room on each story. Mrs. Jewls’s class was at the very top. It was Louis’s favorite class. He pushed through the door to the school, then started up the stairs. There was no elevator. There were stairs that led down to the basement too, but nobody ever went down there. There were dead rats living in the basement.

LOUIS: (huffing and puffing he makes hilarious faces)

NARRATOR: The box was pressed against Louis’s face, squashing his nose. Even so, when he reached the fifteenth floor, he could smell Miss Mush cooking in the cafeteria. It smelled like she was making mushrooms.

LOUIS: (sniffing loudly he speaks aloud to himself) Maybe on my way back I’ll stop by Miss Mush’s room and get some mushrooms! (he continues up the stairs, groaning and huffing)

NARRATOR: He didn’t want to miss Miss Mush’s mushrooms. They were her specialty. His arms and legs were very sore, but he didn’t want to rest.

LOUIS: (speaking to himself) This package might be important. I have to get it to Mrs. Jewls right away.

NARRATOR: He stepped easily from the eighteenth story to the twentieth. There was no nineteenth story. Miss Zarves taught the class on the nineteenth story. There was no Miss Zarves. At last, he struggled up the final step to the thirtieth story.

LOUIS: (knocks on the door with his head)

NARRATOR: Mrs. Jewls was in the middle of teaching her class about gravity when she heard the knock.

MRS. JEWLS: Come in!

LOUIS: (gasping) I can’t open the door. My hands are full. I have a package for you.

MRS. JEWLS: (to her class) Who wants to open the door for Louis?

NARRATOR: All the children raised their hands. They loved to be interrupted when they were working.

MRS. JEWLS: Oh dear, how shall I choose? (thinking) I have to be fair about this. I know! We’ll have a spelling bee. And the winner will get to open the door.

LOUIS: (knocking his head against the door again and complaining) It’s heavy. And I’m very tired.

MRS. JEWLS: Just a second! Allison, the first word’s for you. Heavy.

ALLISON: Heavy. H-E-A-V-Y. Heavy.

MRS. JEWLS: Very good. Jason, you’re next. Tired.

JASON: Tired. S-L-E-E-P-Y. Tired.

LOUIS: (trying to readjust the package, but not having much luck)

NARRATOR: Louis felt the package slipping from his sweaty fingers. He shifted his weight to get a better grip. The corners of the box dug into the sides of his arms. He felt his hands go numb. Actually, he didn’t feel them go numb.

MRS. JEWLS: Jenny, package.

JENNY: Package. B-O-X. Package.

MRS. JEWLS: Excellent!

NARRATOR: Louis felt like he was going to faint. At last John opened the door.

JOHN: I won the spelling bee, Louis!

LOUIS: (muttering) Very good, John.

JOHN: Aren’t you going to shake my hand?

LOUIS: (shifts the box to one arm, he quickly shakes John’s hand, grabs the box again and staggers into the room) Where do you want it, Mrs. Jewls?

MRS. JEWLS: I don’t know. What is it?

LOUIS: (in obvious distress and losing patience) I don’t know. I’ll have to put it down someplace so you can open it.

MRS. JEWLS: But how can I tell you where to put it until I know what it is? You might put it in the wrong place.

NARRATOR: So Louis held the box as Mrs. Jewls stood on a chair next to him and tore open the top. His legs wobbled beneath him.

MRS. JEWLS: It’s a computer!

CHILDREN: (booing)

LOUIS: What’s the matter? I thought everyone loved computers.

ERIC: We don’t want it, Louis.

TERRENCE: Take it back, Jack.

MAURECIA: Get that piece of junk out of here.

MRS. JEWLS: Now, don’t be that way. The computer will help us learn. It’s a lot quicker than a pencil and paper.

TODD: (complaining) But the quicker we learn, the more work we have to do

MRS. JEWLS: You may set it over there on the counter, Louis.

LOUIS: (sets the computer on the counter and collapses)

MRS. JEWLS: Now watch closely.

NARRATOR: Everyone gathered around the new computer. It had a full-color monitor and two disk drives.

MRS. JEWLS: (huffs and puffs and pushes it out the open window!)

NARRATOR: They all watched it fall and smash against the sidewalk.

LOUIS: (slaps his forehead with a shocked and angry expression)

CHILDREN: (cheer)

MRS. JEWLS: See? That’s gravity.

JOE: Oh, now I get it!

MRS. JEWLS: Thank you, Louis. I’ve been trying to teach them about gravity all morning. We had been using pencils and pieces of paper, but the computer was a lot quicker.

LOUIS: ARGHHHHHH!!
```

---

## IC-2099: The Phantom Tollbooth

- Title: The Phantom Tollbooth
- Author (byline): Norton Juster
- Work: Not specified
- Publisher: Bullseye Books
- Publication date as stated: Oct 1988
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MILO, GATEMAN, MERCHANT 1, MERCHANT 2, MERCHANT 3, MERCHANT 4, PAGE, KING AZAZ, GUEST 1, GUEST 2, GUEST 3, KING AZAS
- Teaser before the introduction: Yes
- Spoken words (computed): 1785
- Already set (do not supply): none

### Source block (context only)

```text
Author: Norton Juster
ISBN: 978-0394820378
Publisher: Bullseye Books
Date (Month/Year): Oct 1988
```

### Introduction (context only: never use it for content warnings)

```text
The Phantom Tollbooth by Norton Juster
```

### Performance text (classify this)

```text
NARRATOR: There was once a boy named Milo who didn't know what to do with himself-not just sometimes, but always. Wherever he was he wished he were somewhere - else, and when he got there he wondered why he'd bothered. Nothing really interested him-least of all the things that should have.

MILO: It seems to me that almost everything is a waste of time, I can't see the point in learning to solve useless problems, or subtracting turnips from turnips, or knowing where Ethiopia is or how to spell February.

NARRATOR: And, since no one bothered to explain otherwise, he regarded the process of seeking knowledge as the greatest waste of time.

MILO: And worst of all, there's nothing for me to do, nowhere I'd care to go, and hardly anything worth seeing.

NARRATOR: And then, to one side of the room, just next to the phonograph, he noticed something he had certainly never seen before. Attached to one side was a bright-blue envelope which said simply:

MILO: FOR MILO, WHO HAS PLENTY OF TIME.

NARRATOR: He opened the envelope, but just to be polite.

MILO: ONE GENUINE TURNPIKE TOLLBOOTH. EASILY ASSEMBLED AT HOME, "What a strange present,"

NARRATOR: He hopped in [to his small electric automobile] and, for lack of anything better to do, drove slowly up to the tollbooth. As he deposited his coin and rolled past he remarked wistfully,

MILO: I do hope this is an interesting game, otherwise the afternoon will be so terribly dull."

NARRATOR: Suddenly he found himself speeding along an unfamiliar country highway, and as he looked back over his shoulder neither the tollbooth nor his room nor even the house was anywhere in sight.

MILO: What a strange thing to have happen, Here I am riding on a road I've never seen, all because of a tollbooth which came from.

NARRATOR: Before long he saw in the distance the towers and flags of a city sparkling in the sunshine, and in a few moments he reached a great wall and stood at the gateway to Dictionopolis.

GATEMAN: A-H-H-H-R-R-E-M-M, This is Dictionopolis, a happy kingdom, advantageously located in the Foothills of Confusion and caressed by gentle breezes from the Sea of Knowledge. Today, by royal proclamation, is market day. Have you come to buy or sell?"

MILO: I beg your pardon?

GATEMAN: Buy or sell, buy or sell, Which is it? You must have come here for some reason.

MILO: Well, I--"

GATEMAN: Come now, if you don't have a reason, you must at least have an explanation or certainly an excuse,"

MILO: (Shakes head)

GATEMAN: Very serious, very serious, You can't get in without a reason. Wait a minute; maybe I have an old one you can use."

NARRATOR: He took a battered suitcase from the gatehouse and began to rummage busily through it, mumbling to himself,

GATEMAN: "No ... no ... no ... this won't do ... no . . . h-m-m-m . . . ah, this is fine,"

NARRATOR: He held up a small medallion on a chain, dusted it off, and engraved on one side were the words "WHY NOT?"

GATEMAN: That's a good reason for almost anything-a bit used, perhaps, but still quite serviceable."

NARRATOR: And with that he placed it around Milo's neck, pushed back the heavy iron gate, bowed low, and motioned him into the city.

MILO: I wonder what the market will be like,

NARRATOR: Thought Milo as they drove through the gate; but before there was time for an answer they had driven into an immense square crowded with long lines of stalls heaped with merchandise and decorated in gay-colored bunting. Overhead a large banner proclaimed, "WELCOME TO THE WORD MARKET" And, from across the square, five very tall, thin gentlemen regally dressed in silks and satins, plumed hats, and buckled shoes rushed up to the car, stopped short, mopped five brows, caught five breaths, unrolled five parchments, and began talking in turn. 5 GENTLEMEN: "Greetings! Salutations! Welcome! Good afternoon! Hello!

NARRATOR: Milo nodded his head, and they went on, reading from their scrolls. 5 GENTLEMEN: By order of Azaz the Unabridged-- King of Dictionopolis-- Monarch of letters-- Emperor of phrases, sentences, and miscellaneous figures of speech- -We offer you the hospitality of our kingdom, Country, Nation, State, Commonwealth, Realm, Empire, Palatinate, Principality"

MILO: Do all those words mean the same thing? 5 GENTLEMEN: Of course. Certainly. Precisely. Exactly. Yes, You see, Dictionopolis is the place where all the words in the world come from. They're grown right here in our orchards. Once a week by royal proclamation the word market is held here in the great square and people come from everywhere to buy the words they need or trade in the words they haven't used. Enjoy yourself in the market,

NARRATOR: Above all the noise and tumult of the crowd could be heard the merchants' voices loudly advertising their products.

MERCHANT 1: "Get your fresh-picked ifs, ands, and buts."

MERCHANT 2: "Hey-yaa, hey-yaa, hey-yaa, nice ripe wheres and whens."

MERCHANT 3: "Juicy, tempting words for sale."

MERCHANT 4: "Step right up, step right up-fancy, best-quality words right here, Step right up-ah, what can I do for you, little boy? How about a nice bagful of pronouns-or maybe you'd like our special assortment of names?"

NARRATOR: Milo had never thought much about words before, but these looked so good that he longed to have some.

MILO: Maybe if I buy some I can learn how to use them,"

NARRATOR: Said Milo eagerly as he began to pick through the words in the stall. Finally he chose three which looked particularly good to him-"quagmire," flabbergast," and "upholstery." He had no idea what they meant, but they looked very grand and elegant.

NARRATOR: And he continued on through the market. [When the five very tall, then gentlemen once again appeared] 5 GENTLEMEN: 'Ah' there you are. here have you been? We've been looking all over for you. The royal banquet is about to begin. Come with us.

NARRATOR: They seemed very agitated and out of breath as Milo walked along with them.

5 GENTLEMEN: Right this way. Follow us. Come along. Step lively. Here we go.

NARRATOR: They shouted, hopping from the wagon and bounding up a broad marble stairway. Everyone seemed quite grumpy about having to wait for lunch, and they were all relieved to see the tardy guests arrive. There was an ear-shattering blast of trumpets, entirely off key, and a page announced to the startled guests:

PAGE: KING AZAZ THE UNABRIDGED.

NARRATOR: The king strode through the door and over to the table and settled his great bulk onto the throne,

KING AZAZ: "Places, everyone. Take your places."

NARRATOR: He was the largest man Milo had ever seen, with a great stomach, large piercing eyes, a gray beard that reached to his waist, and a silver signet ring on the little finger of his left hand. He also wore a small crown and a robe with the letters of the alphabet beautifully embroidered all over it.

KING AZAZ: What have we here?

MILO: If you please, my name is Milo. Thank you very much for inviting me to your banquet, and I think your palace is beautiful. 5 GENTLEMEN: Exquisite, Lovely, Handsome, Pretty, Charming,

KING AZAZ: SILENCE, Now, young man, what can you do to entertain us? Sing songs? Tell stories? Compose sonnets? Juggle plates? Do tumbling tricks? Which is it?"

MILO: I can't do any of those things.

KING AZAZ: What an ordinary little boy, Why, my cabinet members can do all sorts of things. The duke here can make mountains out of molehills. The minister splits hairs. The count makes hay while the sun shines. The earl leaves no stone unturned. And the undersecretary, hangs by a thread. Can't you do anything at all? . . . Time for the speeches, You first,

MILO: Your Majesty, ladies and gentlemen, I would like to take this opportunity to say that in all the- -"

KING AZAZ: That's quite enough, Mustn't talk all day. NEXT!"

GUEST 1: Roast turkey, mashed potatoes, vanilla ice cream,

MILO: What a strange speech,"

NARRATOR: Thought Milo, for he'd heard many in the past and knew that they were supposed to be long and dull.

GUEST 2: Hamburgers, corn on the cob, chocolate pudding.

GUEST 3: Frankfurters, sour pickles, strawberry jam,

NARRATOR: And so down the line it went, with each guest rising briefly, making a short speech, and then resuming his place. When everyone had finished, the waiters reappeared immediately, carrying heavy trays, which they set on the table. Each one contained the exact words spoken by the various guests, and they all began eating immediately with great gusto.

KING AZAZ: Dig in, I can't say that I think much of your choice."

MILO: I didn't know that I was going to have to eat my words.

KING AZAZ: Of course, of course, everyone here does. You should have made a tastier speech."

NARRATOR: Cried the king, clapping his hands three times. As he did so, the waiters rushed back into the room and quickly cleared away the dishes, the silver, the tablecloth, the table, the chairs, the banquet hall, and the palace, leaving them all suddenly standing in the market place.

KING AZAS: Good luck, good luck; do be careful!

NARRATOR: Milo suddenly remembered his home. He wanted very much to go back, He clapped his hands and the little car appeared, polished like new. Milo got in and with one last look, started down the road. In a few minutes he reached the end of his journey deposited his coin and drove through. And almost before realizing it, he was sitting in the middle of his own room again. But where the tollbooth had been, there was not nothing at all. He searched frantically throughout the apartment, but it had vanished just as mysteriously as it had come and in its place was another bright-blue envelope, which was addressed simply:

MILO: "FOR MILO, WHO NOW KNOWS THE WAY."

NARRATOR: He opened it quickly and read:

MILO: Dear Milo, You have now completed your trip, courtesy of the Phantom Tollbooth. We trust that everything has been satisfactory, and hope you understand why we had to come and collect it. You see, there are so many other boys and girls waiting to use it, too. It's true that there are many lands you've still to visit and wonderful things to see (that no one has yet imagined), but we're quite sure that if you really want to, you'll find a way to reach them all by yourself.

NARRATOR: And, in the very room in which he sat, there were books that could take you anywhere, and things to invent, and make, and build, and break, and all the puzzle and excitement of everything he didn't know-music to play, songs to sing, and worlds to imagine and then someday make real. His thoughts darted eagerly about as everything looked new-and worth trying.

MILO: Well, I would like to make another trip,but I really don't know when I'll have the time. There's just so much to do right here.
```

---

## IC-2100: Picnic at Treblinka

- Title: Picnic at Treblinka
- Author (byline): Susan Jane Gilman
- Work: Hypocrite in a Pouffy White Dress, Pgs 203-227
- Publisher: Grand Central Publishing
- Publication date as stated: Jan 2005
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, GIRL, BOY
- Teaser before the introduction: Yes
- Spoken words (computed): 1367
- Already set (do not supply): none

### Source block (context only)

```text
Author: Susan Jane Gilman
Book: Hypocrite in a Pouffy White Dress, Pgs 203-227
ISBN: 978-0446679497
Publisher: Grand Central Publishing
Date (Month/Year): Jan 2005
```

### Introduction (context only: never use it for content warnings)

```text
Like the majority of young Jewish Americans, Susan Jane Gilman attended a public high school, decorated a Christmas tree each holiday season, and rarely attended synagogue or temple. For her, the Holocaust was just a bit of history. She knew of it, yes; but from a very distant and sheltered place.

When Gilman was sent to Poland as a reporter for the Jewish Weekly to write an article about Jewish history and the Holocaust, she was less than thrilled. In her own words: “I don’t mean to be funny. It’s just that the world is patently absurd.”

In Picnic at Treblinka, Gilman tries valiantly to maintain her off-beat, wry sense of humor until the visceral response becomes too much.

Picnic at Treblinka by Sarah Jane Gilman
```

### Performance text (classify this)

```text
NARRATOR: (Pg 203-204) (to audience) To be honest, I don’t know a thing about Judaism. Ever since making my grand debut in the sixth grade Christmas pageant, all I’d ever managed to learn about Judaism was that people could kill you for it for no good reason. What was there for Jews to be proud of? Christians had Christmas and Easter bunnies. Granted, heaven and hell seemed to me like transparent attempts at crowd control. But all we Jews seemed to have was the Holocaust. Christians were visited by angels, Jews by the Gestapo. It was no contest.

NARRATOR: (Pg 216) (to audience) The week's itinerary read like a vacation package designed by Joseph Goebbels. Tuesday: Treblinka concentration camp. Wednesday: Warsaw ghetto. Thursday: Krakow. Friday: Auschwitz and Birkenau concentration camps.

(Pg 219-220) Treblinka was so pristine, it looked more like an art installation than a concentration camp. The entire site had been demolished by the Nazis in the wake of advancing Allied troops, so the only structures now were memorials. Jagged rocks, each engraved with the name of a town whose population had been annihilated, were scattered around the woodsy site like a haphazard graveyard. Seeing it without knowing the historical context, you'd have absolutely no way of divining what had actually happened there. You might think it was another Stonehenge, a miniature Easter Island.

A few kids seemed to be under just this impression: they sat down beside one of the memorials and began passing around chicken salad sandwiches.

(sarcastically to traveling companions) Oh look! What a great place for a picnic. Or, better yet, a fashion shoot. Here! (striking a pose)

(to audience) I [struck] a pose beside a chunk of granite with the name "Bialystok" etched on it. Bialystok had been the town my grandmother had come from; all her relatives had been killed.

(to traveling companions) Get one of me like this!

(tucking an arm seductively behind head) For Grandma . . (bitterly) Why not? Everyone else here seems determined to pretty things up. (to audience) Are you ready for the height of sickness? Check out the souvenir shop. You'll be relieved to know that, at least when I was there, Treblinka sells key rings, change purses, and souvenir bookmarks. (to saleswoman) Hey, do you have any bumper stickers that say 'Honk If You Love the Fuhrer'? (laughing) Look at these . . . (to audience) A rack of postcards with attractive shots of Treblinka on a sunny day. (incredulously) Okay, hands-down, this wins! (to audience) We each bought some, along with airmail stamps. (writing on postcard) 'Dear Mom. Here I am at Treblinka. As you can see, it is very pretty. The people are friendly. I am having lots of fun” *****

NARRATOR: (Pg 221-227) The highlight took place on Friday -- first to Auschwitz. From there -- two kilometers to Birkenau. Concentration camp prisoners often had to walk from the labor camp to their own extermination. The fields around Auschwitz were flooded with hazy sunshine. Forsythia bloomed on the roadsides. [And] the great irony about Auschwitz -- now you had to pay to get in. Near the entrance was a cafeteria/snack bar, followed by an ice cream stand. As I walked up a stony path, a group of teenagers came barreling up the path.

GIRL: (excitement of an amusement park) It's the gate! Quick, you guys, we have to get a picture!

NARRATOR: (looking and gesturing above to the words) "Work Makes You Free" -- The famous entrance to Auschwitz, that mocked prisoners as they staggered to their deaths. "Work Makes You Free." In a moment, four of them were posing beneath it, their arms flung around each other chummily, everyone squirming and giggling. One kid made a peace sign with his fingers.

BOY: (with camera) Okay, at the count of three, smile and say 'cheese."

GIRL: CHEESE!

NARRATOR: I could see them back home: (mimicking) Here's me and Jason at Disneyland. Here we are at the junior prom. Oh, and here we are at Auschwitz! But then, strangely, I found myself almost gleeful. Hitler, had hoped to turn a handful of synagogues into museums documenting "the extinct Jewish race." Instead, his own machinery had been preserved as a tourist attraction, and now here we were -- kids with cartoon T-shirts, cameras, and picnic lunches, posing beneath the defunct infrastructure of genocide, laughing and squeezing together to fit into the frame. Jews weren't just victims; in the end, we were victors, too!

The Third Reich was gone, but all the people they'd tried to exterminate were still here: the gays, the disabled, the Gypsies, and the Jews. Just how triumphant was that?

I rounded a corner onto dirt paths to find former barracks where prisoners had slept packed together like cattle. Upstairs, preserved behind a wall of Plexiglas was an enormous pile of hairbrushes and combs -- a hundred thousand of them, piled nearly to the ceiling --and if you looked closely, you could see a few strands of hair in some of them. More disturbingly, the next room was filled with shoes, all sizes and styles-scuffed leather, buckles, lace-ups, high heels -and tiny children's shoes-thousands of pairs, again piled nearly to the ceiling, an avalanche of footwear, all of them bearing the imprints of their former owners.

Six million. Suddenly I could picture the woman in dark green leather pumps with cracked soles, the man with a tortoiseshell comb tucked in his breast pocket. One hair-brush, one belt buckle, and for the first time, the dead became individually palpable. In the next room were eyeglasses, a big, mangled tumbleweed of wire. I wore eyeglasses.

I don't know how I got out of the barracks, or accidentally stumbled into the gas chambers next door -- a dank, impassive, clinically tiled room -- or was it con-crete? Overhead were big, flat shower heads. Were those fingernail gouges in the walls, or was I imagining things?

The first time I'd heard about the gas chambers was when my friend Ruthie had told me there was a man named Hitler who'd made all the Jews take off their clothes and go into a big group shower where poison gas came out of the pipes instead of water. (as a child to Ruthie) So wait, before the showers, they didn't even let you wear towels? (to audience) Now, here I was, in a gas chamber myself. The room seemed to vibrate with malignancy and pain. I was out of jokes; I was utterly alone.

Adjacent to the showers was a crematorium. The ovens were reddish brick, long and deep, with human-sized spatulas protruding from them. -- there was no mistaking their purpose.

Until that moment, I'd somehow assumed that the Holocaust had been meant for other people -- for real Jews, Jews who actually cared about their religion. Jews who had been weak or naive. Jews who hadn't been nearly as savvy, charming, or modern as my family was. Surely, we would have been spared. Surely, we would have figured out some way to wriggle out of it, to be granted an exemption from a fate reserved for six million others. Surely, the Nazis would at some point have realized that they were making a terrible mistake. Look: We had a Christmas tree! I'd sung in a choir!

At some point, I suppose, all of us in our lives confront some unavoidable, outsized horror. Maybe it's a tumor, or a little brother playing with a gun, or a psychopath in a day care center; but inevitably, a moment comes for all of us when we realize that we cannot beat the devil on this one: we have been targeted for injustice or tragedy. And nothing in school, nothing in daily life really prepares us for this.

At twenty-two years old, I'd remained strangely naive. Now, staring into an oven designed specifically for me -- me in my shoes and eyeglasses -- I was suddenly aware of just how spoiled and ill-equipped I was to cope with the viciousness of the world. What the hell did I know? I was just some ambitious little *jerk* from New York.

I wanted to go home and curl into a feral position in my bedroom. I'd happily forfeit substance and forgo all wisdom if it meant I'd never have to recognize this. I had the urge to rip open my own skin, crawl out of it, and leave it behind as I fled. As if cued, the sky became overcast, and a soft rain began falling as we marched past the ominous watchtowers and under the brick archway of Birkenau, where railway tracks ran, then came, chillingly, to a halt.
```

---

## IC-2101: Short Stories (from The Pillowman)

- Title: Short Stories (from The Pillowman)
- Author (byline): Martin McDonagh
- Work: Not specified
- Publisher: Faber and Faber
- Publication date as stated: Sept 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: CHILD’S VOICE, MOTHER, MOM OR DAD, LITTLE GIRL, PRIEST
- Teaser before the introduction: No
- Spoken words (computed): 2003
- Already set (do not supply): none

### Source block (context only)

```text
Author: Martin McDonagh
ISBN: 978-0571220328
Publisher: Faber and Faber
Date (Month/Year): Sept 2004
```

### Introduction (context only: never use it for content warnings)

```text
Martin McDonagh’s play The Pillowman is about a writer who is interrogated about the gruesome content of his short stories and their similarities to a number of child-murders that are happening in his town. He learns that his older brother, Michal, is also being held and questioned in another cell. Michal, who has the mind of a child. Michal, who our author, Katurian, has raised ever since the death of their parents.

The first short story tells the tale of Katurian and Michal – it is believed to be somewhat autobiographical . . . right up until the end. The Writer and the Writer’s Brother by Martin McDonagh writing as Katurian Katurian,
```

### Performance text (classify this)

```text
PAGE 31 - 35 Once upon a time there was a little boy upon whom his mother and father showered nothing but love, kindness, warmth, all that stuff. He had his own little room in a big house in the middle of a pretty forest. He wanted for nothing: all the toys in the world were his; all the paints, all the books, paper, pens. All the seeds of creativity were implanted in him from an early age and it was writing that became his first love: short stories, fairy tales, little novels, all happy colorful things about bears and piglets and angels and so forth, and some of them were good, some of them were very good. His parents’ experiment had worked. It was the night of his seventh birthday that the nightmares first started. The room next door to his own room had always been kept bolted and padlocked for reasons the boy was never quite sure of but never quite questioned until the low whirring of drills, the scritchety-scratch of bolts being tightened, the dull fizz of unknown things electrical, and the muffled screams of a small gagged child began to emanate through its thick brick walls. On a nightly basis.

CHILD’S VOICE: (to mother) What were all those noises last night, Mama? He’d ask, after each long, desperate, sleepless night, to which his mother would ever reply . . .

MOTHER: Oh, that’s just your wonderful but overactive imagination playing tricks on you.

CHILD’S VOICE: Oh. Do all little boys of my age hear such sounds of abomination nightly?

MOTHER: No, my darling. Only the extraordinarily talented ones.

CHILD’S VOICE: Oh. Cool. And that was that. And the boy kept on writing, and his parents kept encouraging him with the utmost love, but the sounds of the whirrs and screams kept going on . . . and his stories got darker and darker and darker. They got better and better, due to all of the love and encouragement, as is often the case, but they got darker and darker, due to the constant sound of child-torture, as is also often the case. It was on the day of his fourteenth birthday, a day he was waiting to hear the results of a story competition he was short-listed for, that a note slipped out from under the door of the locked room . . . (a note in red writing slips under the door and the speaker picks it up) . . . a note which read: ‘They have loved you and tortured me for seven straight years for no reason other than as an artistic experiment, an artistic experiment which has worked. You don’t write about little green pigs any more, do you?’ The note was signed ‘Your brother’, and the note was written in blood. He axed through the door to find . . . his parents sitting in there, smiling, alone; his father doing some drill noises; his mother doing some muffled screams of a gagged child; they had a little pot of pig’s blood between them, and his father told him to look at the other side of the blood-written note. The boy did, and found out he’d won the fifty-pounds first prize in the short-story competition. They all laughed. The second part of his parents’ experiment was complete. They moved house soon after that and though the nightmare sounds had ended, his stories stayed strange and twisted but good, and he was able to thank his parents for the weirdness they’d put him through, and years later, on the day that his first book was published, he decided to revisit his childhood home for the first time since he’d left. He idled around his old bedroom, and all the toys and paints still littered around there . . . then he went into the room beside it that still had the old dusty drills and padlocks and electrical cord lying around, and he smiled at the insanity of the very idea of it all, but he lost his smile when he came across . . . (He pulls the mattress of to reveal the horrific corpse of a child) the corpse of a fourteen-year-old child that had been left to rot in there, barely a bone of which wasn’t broken or burned, in whose hand there lay a story, scrawled in blood. And the boy read that story, a story that could only have been written under the most sickening of circumstances, and it was the sweetest, gentlest thing he’d ever come across, but what was even worse, it was better than anything he himself had ever written Or ever would (Speaker takes a lighter and sets the story alight). So he burnt the story, and he covered his brother back up, and he never mentioned a word of what he had seen to anybody. Not to his parents, not to his publishers, not to anybody. The final part of his parents’ experiment was over. ‘ *************** Katurian’s story ‘The Writer and the Writer’s Brother’ ended there in a fashionably downbeat mode, without touching upon the equally downbeat but somewhat more self-incriminating details of the truer story, that after he’d read the blood-written note and broken into the next-door room it was, of course . . . his brother he found in there, alive, as such, but brain-damaged beyond repair, and that night, whilst his parents were sleeping, the fourteen-year-old birthday boy held a pillow over his father’s head for a little while . . . and, after waking her a moment just to let her see her dead blue husband, he held a pillow over his mother’s head for a little while too. TRANSITION After the deaths of Katurian and Michal’s parents, Katurian becomes the sole care-giver for his brother Michal, regaling him every night with stories he has written – dark stories. As Martin McDonagh’s play The Pillowman opens, we find out that both brain-damaged Michal and our author, Katurian, have been arrested for the gruesome murders of 2 local children. A third little girl has now been reported missing. Strangely enough, each murdered child was put to death in a manner described in one of Katurian’s short stories: the removal of toes, the swallowing of razor blades.

The third little girl, however, has yet to be found; and as the play progresses, Michal claims responsibility and explains that ‘The Little Jesus’ was the inspiration for her disappearance. The Little Jesus by Martin McDonagh writing as Katurian Katurian

PAGE 67-71 Once upon a time in a land not so very far away there lived a little girl, and although this little girl’s gentle parents hadn’t brought her up very religiously at all, she was quite, quite determined that she was the second coming of the Lord Jesus Christ. Which was somewhat strange for any six-year-old. She’d wear a little beard and would go around in sandals, blessing stuff. She could be forever found walking amongst the poor and the homeless, consoling the drunks and the drug addicts, and generally consorting with the type of person her mummy and daddy didn’t deem suitable for a six-year-old to be consorting with. Each time they would drag her home from some unsavory sort, she would stamp and scream and throw her dollies about, and when her parents would counter that . . .

MOM OR DAD: Jesus never stamped and screamed and threw his dollies about . . . She’d reply . . .

LITTLE GIRL: That was the old Jesus! Get it? Well, one day, the little girl slipped away yet again, and for two horrifying days her parents could find neither hide nor hair of her, until they received a distraught call from a priest they didn’t know saying:

PRIEST: You’d better come down to the church. Your daughter’s here giving us a lot of shit. It was cute at first, but now it’s really getting irritating. Well, her parents didn’t care about all that, they were just relieved that she was alive and well, and they sped downtown to pick her up, but in their haste they careened into an oncoming meat truck, were beheaded and died. The little girl was informed of the news; she cried one single tear, and not a single tear more, as she thought Jesus would’ve done if he’d lost his parents in a vehicular beheading; and she was shipped off by the state to live in a forest with some abusive foster-parents . . . who hadn’t informed the state that they were abusive on the form; who hated religion, who hated Jesus, who hated anybody, in fact, who didn’t hate anybody, and who, as would follow, hated the little girl. She bore their hate with a happy heart and forgave them, but this didn’t seem to work. When she insisted on attending church of a Sunday, they took her sandals away, forcing her to walk there barefoot and alone, over craggy roads of broken glass, yet when she got there, she’d kneel for hours, praying for her Father in Heaven to forgive them, only to get told off for bleeding all over the church. She’d receive a beating for arriving late home, though no time had been set for her arrival; she’d receive a beating for sharing her food with the poor children at school; she’d receive a beating for cheering up the ugly kids; she’d receive a beating for wandering about looking for lepers. Her life was a constant torture, yet she bore it with a smile and it all only made her stronger, till this one day when she met a blind man begging by the roadside. She mixed a little of her spittle in the dust and rubbed it over his eyes. He reported her to the police for rubbing dust and spittle in his eyes, and when her foster-parents got her back from the police station they said to her . . .

MOM OR DAD: So you want to be just like Jesus, do you? And she said . .

LITTLE GIRL: Finally, you get it! Her foster mother embedded in her daughter’s head a crown of thorns made of barbed wire, because she was too lazy to make a proper crown of thorns, while her foster-father whipped her with a cat o’nine tails, and after an hour or two of that, they asked her, when she regained consciousness

MOM OR DAD: Do you still want to be like Jesus? And, through her tears, she said

LITTLE GIRL: Yes, I do.

So they made her carry a heavy wooden cross around the sitting room a hundred times until her legs buckled and her shins broke and she could do nothing but stare at her little legs going the wrong way, and they said to her . . .

MOM OR DAD: Do you still want to be like Jesus? And she almost got sick for a second, but she swallowed it so she wouldn’t look weak and she looked them in the eye and she said . . .

LITTLE GIRL: Yes, I do And then they nailed her hands to the cross and bent her legs back around the right way and nailed her feet to the cross and they stood the cross up against the back wall and left her there while they watched television, and when all the good programs were over, they turned it off and they sharpened a spear and they said to her. MOM OR DAD; Do you still want to be like Jesus? And the little girl swallowed her tears and she took a deep breath and she said

LITTLE GIRL: No, I don’t want to be like Jesus. I am Jesus (Pause) And her parents stuck the spear in her side . . . and they left her there to die, and they went to bed. And in the morning they were quite surprised that she wasn’t dead . . . so they took her down off the cross and they buried her alive in a little coffin with just enough air to live for three days . . . and the last voices she heard were her foster parents above, calling out . .

MOM OR DAD: Well, if you’re Jesus, you’ll rise again in three days, won’t you? And the little girl thought about it for a while, then she smiled to herself and she whispered

LITTLE GIRL: Exactly. Exactly (Pause) And she waited. And she waited. And she waited.

CLOSING I’ll leave you with one question . . . one you must answer for yourself: Who is culpable? Katurian, Michael, their parents, or society? These are the stories from The Pillowman
```

---

## IC-2102: Pinocchio

- Title: Pinocchio
- Author (byline): AJ Jacobs
- Work: Fractured Fairy Tales
- Publisher: Bantam Books
- Publication date as stated: Dec 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 851
- Already set (do not supply): none

### Source block (context only)

```text
Author: AJ Jacobs
Book: Fractured Fairy Tales
ISBN: 978-0553099805
Publisher: Bantam Books
Date(Month/Year): Dec 1997
```

### Introduction (context only: never use it for content warnings)

```text
Walt Disney’s immortal masterpiece Pinocchio has inspired millions to wish upon a star and always “let your conscience be your guide.” On a magical starlit night, a blue fairy brings Geppetto’s beloved marionette Pinocchio to life, beginning a fantastic adventure that will test the puppet’s bravery, loyalty and honesty - virtues he must learn to become a real boy. Despite the warnings of his wise friend, Jimmy Cricket, Pinocchio gets entangled in one humorous predicament after another. In AJ Jacobs parody of this classic, Jimmy Cricket is missing and the only virtue that eludes our hero is that of bravery, and an overwhelming push by Geppetto to make it BIG on TV. Pinocchio by AJ Jacobs.
```

### Performance text (classify this)

```text
Once upon a time in a faraway city lived a kindly old wood-carver named Geppetto. All day long, he sat in his tiny workshop and carved puppets out of wood with his crude jackknife.

"Boy, this whittling sure gets to be a drag," said Geppetto one day. "Looka me. Talking to a pine-top dummy. If only you was a real kid! I could get you a paper route and take it easy for a while."

No sooner had kindly old Geppetto shuffled off to bed than a good fairy mysteriously appeared. The fairy figured that kindly old Geppetto deserved better, and decided to grant him his wish. She tapped the puppet on the head and POOF it sprang to life.

"Ugh," groaned the puppet. "Do l need a cup of joe. Hey, who are you'?"

"I'm the good fairy who just brought you to life," said the fairy.

"Yeah, but looka me! I'm still wood! I want to be a real boy!"

The fairy told the puppet that yes, one day, he could be a real boy. But as always, there was a catch. The puppet had to perform a brave deed. With that, the fairy mysteriously disappeared and the puppet ran to wake Geppetto and tell him the good news;

"Hey, kindly old Geppetto," said the puppet,shaking the wood-carver awake.

"Whatever you sellin' I don't want," grunted Geppetto. .

"No, it's me, the puppet you carved. The good fairy brought me to life."

Geppetto bolted up, clicked his heels, and shouted, "Yabba-dabba-doo!" (Italian for Hooray!) "Oh, I so happy! A talking puppet with no strings? " You're worth a fortune! I'm gonna call you Pinocchio and start my own television show."

"But I don't want to be on television," said the puppet. "I want to do a brave deed and become a real boy."

"You outta your mind, Splinters? Stay wood. Stay wood! You gonna be bigger than Hunch and Juicy."

"That's Punch and Judy," said the puppet. But Geppetto wasn't listening. He was already on the phone with J. Quincy Flogg, the president of the television network, telling him about this hot new act. Flogg loved the concept and, after three dozen focus groups, 22 studies, and 158 meetings, he boldly agreed to give Geppetto a show. It was tentatively titled Pinocchio Doody Show and after some hard bargaining, Geppetto got himself a million dollars and two coffee breaks for each show.

Everybody soon got to work. Pinocchio was sent to a personal trainer to make sure his pine was hard but flexible. He got some high-priced wooden surgery for his nose, which mysteriously grew each time he lied. (Which, in show business, was quite a bit.) And he started shooting a commercial for lemon-scented wood polish-no easy task.

"Take it from the top!" yelled Geppetto, on the commercial's set.

"But kindly old Geppetto," sighed Pinocchio, "I've already done the commercial fifty times."

"Hey, knothead, you know what this is'?" asked Geppetto, holding up a piece of paper.

"It's paper,"

"Atsa right," said Geppetto. "And you know what it's made of?"

"Wood."

"Atsa right again. Now. . . you wanna wind up as a big brown roll in a butcher shop?"

"No, sir," said Pinocchio.

"Okay. Then let's see that soft smile and the hard sell,"

Finally, all was in readiness for the big show. Backstage, Pinocchio sat in his chair, his makeup artist applying a little varnish. The director approached him. "Don't worry, Pinocchio," he said. "If you forget your lines, you can always look at the cue cards."

Pinocchio shrugged his shoulders. He didn't need any cue cards, he said. He knew his part. Now who should overhear this but J. Quincy Flogg, the president of the network. He was stunned. "A TV star not using idiot cards! Why, that's the bravest thing I've ever heard."

It was quite brave. In fact, it was such a brave deed that the mere thought of it instantly turned Pinocchio from a wood puppet into a real boy. But as soon as that happened, the network canceled the show. Geppetto tried to sell his idea to Disney as a nice family movie, but Disney couldn't care less. Geppetto and Pinocchio found themselves penniless and on the street.

Just then, the good fairy appeared again.

"Oh, I love happy endings," she said. "Finally Pinocchio's a real boy and he can be your son and live with you forever."

"You offa your head?" shouted Geppetto. "I want to be lonely. I don't like kids. I'm leaving." Geppetto sulked off to his workshop, where he made hundreds and hundreds of other puppets, hoping that one would come to life again someday, which never happened.

The good fairy comforted the little boy. "Let him go. You see, he isn't your real father at all. That's your real father." She pointed at J. Quincy Flogg, the head of the network.

Pinocchio was overjoyed to find his real father at last, and Flogg was happy too. He was so happy he gave his son a starring role in the nighttime soap opera Faraway Hamlet 90210, even though he had minimal acting skills.
```

---

## IC-2103: The Plane Truth

- Title: The Plane Truth
- Author (byline): Ellen DeGeneres
- Work: Sand in My Bra and Other Misadventures
- Publisher: Traveler's Tale
- Publication date as stated: March 2003
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, FLIGHT ATTENDANT, INVESTIGATOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1181
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ellen DeGeneres
Book: Sand in My Bra and Other Misadventures
ISBN: 978-1885211927
Publisher: Traveler's Tale
Date (Month/Year): March 2003
```

### Introduction (context only: never use it for content warnings)

```text
Many people have a fear of flying. And the Flight Attendant’s spiel before take-off doesn’t inspire a great deal of confidence either!

(Presented in a friendly, flight attendant voice with accompanying gestures) Welcome aboard Flight 245. To operate your seat belt, insert the metal tab into the buckle, and pull tight. It works just like every other seat belt, and if you don’t know how to operate one, you probably shouldn’t be out in public unsupervised.

In the event of a sudden loss of cabin pressure, masks will descend from the ceiling. Stop screaming, grab the mask, and pull it over your face. If you have a small child traveling with you, secure your mask before assisting with theirs. If you are traveling with more than one small child, pick your favorite.

The Plane Truth by Ellen DeGeneres
```

### Performance text (classify this)

```text
NARRATOR: (Pg 28-34) I know that the experts say you’re more likely to get hurt crossing the street than you are flying (these, of course, would be the street-crossing experts), but that doesn’t make me feel any less frightened of flying. If anything, it makes me more afraid of crossing the street. As soon as the light turns green, I run across the street as fast as I can, screaming like a mad *person.* I arrive on the other side out of breath, wheezing, and clutching my stomach.

NARRATOR: I felt edgy the moment I stepped into the aircraft. That could be why I snapped at the woman in front of me. In my defense, she did ask the flight attendant a pretty stupid question:

WOMAN IN 27-B (also a nun): Excuse me, where is seat 27- B?

NARRATOR: I mean, really. But I see now that I overreacted when I screamed at her, “Well, moron you walk in the only direction you can, and it’s the 27th row seat B – next to seat A. All righty?!” That sort of response is probably one of the many reasons why I’m not a flight attendant. It was only when the woman (27- B) turned around to look at me that I saw she was a nun. I guess that sort of hat-like thing she wore on her head should have given me a clue. (beat) I tried to apologize by smiling and giving her a playful punch on the arm to let her know I was joking. Well, either my playful punch carried more of a wallop than I intended or her advanced years made her frailer than she appeared, but the nun shouted out,

WOMAN IN 27-B (also a nun): Owww! (rubbing her arm in pain . . . she rolls up her sleeve)

NARRATOR: . . . you know, that bruise could easily have been there before I hit her. (beat) My good friend Jasmine told me that a good way to combat fear is to chant. So all the way to my seat I was chanting, “I’m going to die, I’m going to die, oh sweet Lord, I’m going to die.” It didn’t work. If anything, I was more petrified when I got to my seat (27-A). Even seeing the familiar face of the nun in 27-B (who seemed to flinch when she saw me) didn’t call me down.

So here I am, sitting in my seat. (taking calming breaths, then reacts violently to a sound) ARGHHH! What was that? We’re going to crash!!! Oh, I wish I hadn’t shouted that out loud. It was just the beverage cart. (to seatmate) “Pardon me, Sister, I am sorry, I . . . . I was frightened. Pray for me.” Now she’s going to turn on that little air thing above her. Maybe I’m paranoid, but I think it takes power away from the plane somehow. “Sister, don’t use that, that’s . . . . Dang! Shut if off! Shut it off!” (beat) The nun just left to find a different seat. Some people are so touchy. I’m sure she didn’t learn that little hand gesture in her convent, either.

I’ve got to relax somehow. Why didn’t I think of this sooner? I’ll recline my seat. Oh, that makes all the difference. That ¾ of an inch between upright and reclined is the difference between agony and ecstasy. I never thought ¾ of an inch could mean so much. When I get home, I’m going to put some gizmo in my chairs so that they go back ¾ of an inch, too. I’d better not get too comfortable in my ¾-of-an-inch recline because toward the end of the flight, the flight attendant is going to say,

FLIGHT ATTENDANT: You’re going to have to put your seat in the upright position for landing.

NARRATOR: They’re so adamant about that every single time, like that’s gonna make a difference. Because if we crash, the investigators are going to say,

INVESTIGATOR: Oh, that’s a shame, her seat was recline ¾ of an inch. When will they learn? What was that – 30,000 feet? She could have made that. Sheesh. If only she’d been upright.

NARRATOR: Being reclined isn’t working. I’m still freaking out. I know what I need. “Oh, flight attendant. Oh ma’am.” (to audience) You have to talk nice to the flight attendants because they all have this attitude. And they can afford to have the attitude, because they have the power – they have the peanuts. They have these six peanuts that we need. Six peanuts. Somebody could offer that to you on the street, and you’d say, “I don’t want that – get that away from me. Six peanuts? No-oh.” Somehow, they’ve done research. They know that the higher we go, the more we need nuts. And we go crazy if we don’t get them. (to Flight Attendant) Miss, I didn’t get my, uh - - my peanuts. And I’d really appreciate it if you game me some. (stuffing peanuts one at a time in her mouth) They’re good, aren’t they? I’ve never been able to get them on the ground either. At least not ones this good! (licking the salt from her fingers)

(panicked) What was that! We’re going to crash! Oops, false alarm. It’s just the food card coming down the aisle. We do get excited about it, don’t we? “Oh, here comes the cart, put down the tray! La la la la. Put down your tray! They’re starting on the other side first. Hurry! Hurry! Those people over there – they’re eating. Those people are eating.”

Any kind of meat that you get – chicken, steak, anything – has grill marks on each side, like somehow we’ll actually believe there’s an open-flame grill in the front of the plane. And salads are always two pieces of dead lettuce and salad dressing that comes in that astronaut package. (package explodes as she tries to open it) As soon as you open it, it’s on your neighbor’s lap. “Could I just dip my lettuce, ma’am? Hm, that’s a lovely skirt.

What is that, silk?” But you know, should that happen, club soda’s gonna get that stain our immediately. That’s the answer to anything you ask up there, I don’t know if you’ve noticed that.

NARRATOR: Excuse me, I have an upset stomach.

FLIGHT ATTENDANT: Club soda, be right back.

NARRATOR: Excuse me, I spilled something.

FLIGHT ATTENDANT: Club soda, be right back.

NARRATOR: Ooh, the wing is on fire!

FLIGHT ATTENDANT: Club soda, be right back.

NARRATOR: I thought the food would make me feel less frightened. But it didn’t. Maybe if I stretch my legs and go to the restroom it will help. You have no concept of time when you’re in there – it’s like a casino: no windows, no clocks. I could be the only one to get up out of my seat to go to the bathroom – everybody else is sound asleep when I go – but after I’ve been in there for what I think is thirty seconds, I open the door and everyone in the plane is lined up, looking at their watches, make me feel like I’ve been in there forever.

And now I’ve got to explain the smell that was in there before I went in there. “Oh! Listen, there’s an odor in there and I didn’t do it. It’s bad. You might want to sprinkle some club soda, if you uh . . .“

I think my only hope of escaping my mind-numbing fear is to sleep; to sleep and perchance to dream. The only trouble is when I fall asleep on a plane, (drifts off while finishing this statement) I always have a nightmare . . . (only to jolt awake screaming) Oh sweet Lord, I’m going to die!
```

---

## IC-2104: Playing with Fire

- Title: Playing with Fire
- Author (byline): Tess Gerritsen
- Work: Not specified
- Publisher: Ballantine Books
- Publication date as stated: Oct 2015
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1432
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tess Gerritsen
ISBN: 978-1101884348
Publisher: Ballantine Books
Date (Month/Year): Oct 2015
For additional historical information regarding The
Holocaust in Italy and the San Sabba Police Camp in
Trieste:
https://encyclopedia.ushmm.org/content/en/article/italy
https://www.holocausthistoricalsociety.org.uk/contents/akti
onreinhardt/sansabba.html
```

### Introduction (context only: never use it for content warnings)

```text
Lorenzo Todesco is a young Jewish violinist in 1940s Italy. Jews had lived in Italy for over two thousand years. In fact, the Italian Jewish community was one of the oldest in Europe. But this is Mussolini’s Italy, and a brutal war is on. And although more than 40,000 Jews survived the Holocaust in Italy, the Todesco family were not among the survivors. For a time, Lorenzo Todesco was one of the lucky ones. Hand-picked for his musical prowess, Lorenzo was forced with five others to play his composition Incendio (The Fire) over and over. In this selection he recounts one horrific day among many, playing his role in the “orchestra of the damned.”

Playing with Fire by Tess Gerritsen
```

### Performance text (classify this)

```text
(Pg 199-200) May 1944 -- Late at night, lying in his bunk, Lorenzo could hear the screams from Cell No. 1. He never knew who was being tortured. He never saw the victims. He only knew that from night to night, the voices of the tormented kept changing. Sometimes a woman’s shrieks, sometimes a man’s. Sometimes a baritone voice would crack into the girlish sobs of a boy still on the threshold of manhood. He had been warned by the Italian Colonel: See nothing. Hear nothing. Say nothing. And you just might survive.

(Pg 185) When you cannot see where you are going, when you do not know your final destination, every hour is its own eternity. (Pg 200-205) Most human beings can learn to endure almost anything, even the cries of the tormented. It was not that their hearts had hardened; it was because they could do nothing about it, and powerlessness leads to its own form of serenity.

Did he dream of the platform where they had all been singled out as musicians and ripped from those they loved? Even now, months later, the wound left by that separation felt as painful to Lorenzo as a fresh amputation. While their families had almost certainly perished, music had kept alive this ensemble of six broken men. Each handpicked by the Italian Colonel. There was Shlomo, the drummer from Milan, who’d been arrested with his family as they’d tried to cross the border into Switzerland. There was Emilio, the second violinist, who’d been dragged from a friend’s farmhouse, a friend who had been summarily executed for hiding a Jew. There was Vittorio, the cellist, arrested in Vincenza, whose hair had magically turned white within weeks of arriving at San Sabba. There was Carlo, the French horn player who had once been fat, and whose loose skin now flopped in pale drapes. And finally there was Aleks, the viola player, a musician so talented he could have found a position with any symphony in the world. Instead here he was, a mere husk of a man who performed with mechanical fingers and empty eyes.

In Cell No. 1, the screams rose to a shriek so piercing that Lorenzo clapped his hands over his ears, desperate to shut out the sound. He pressed them there until the screams faded and all he could hear was the whoosh of his own pulse. When at last he dared to pull his hands away from his ears, he heard the squeal of the cell door and the scrape of the prisoner’s body being dragged out to the courtyard. He knew its final destination.

Three months ago, construction had begun in the building across from their cell block. Though he’d been advised to see nothing, hear nothing, Lorenzo could hardly be blind to all the trucks hauling materials through the gate and into the compound. At first none of the musicians knew what was being built. Lorenzo assumed they were adding another cell block to house the flood of new detainees. Every week, so many men, women and children arrived by train that they were sometimes herded into an open courtyard and spent days shivering and exposed, waiting to be transported north. Yes, a new cell block made sense.

Then he began to hear whispers from the prisoners; they had seen an underground tunnel leading to the chimney stack. No, this was not some new cell block being built. It was something else. One cold morning in April, Lorenzo saw smoke curl from that chimney for the first time. That chimney billowed a singular stench that could not be escaped. It clung to clothes and hair, swirled up throats and noses, and was inhaled into lungs. Both prisoners and guards alike were forced to breathe in the dead.

See nothing. Hear nothing. Say nothing. This is how you survive.

Everyone closed their ears to the screams from Cell No. 1 and to the executioner’s gunshots beyond the walls of the compound. But there was one sound no one could shut out, a sound so horrifying that even the guards would grimace. Some of the executed prisoners delivered to the ovens were not really dead, but merely stunned by what should have been a fatal bullet or blow, and they were thrown into the flames alive.

To drown out the noise of the dying, San Sabba’s little orchestra of the damned was ordered to play music in the courtyard. Since dawn, round after round of gunshots had been booming outside the walls. Now the first truck rolled in, weighed down with the harvest from that morning’s gunfire. “More logs for the fire,” the Italian colonel announced. “Well, what are you waiting for? Begin!”

They did not choose sedate minuets or quiet airs, for the purpose of this music was not to entertain. It was to disguise and distract, and for that they needed music played at maximum volume. The Italian Colonel paced the courtyard as they performed, haranguing his musicians to play louder! Louder!

But it was not loud enough. It could never be loud enough to hide the horrors inside the building with the smokestack.

The first truck pulled away; a second one rolled through the gates, so overloaded that it sagged low on its axles. As it bounced across the courtyard, part of its cargo tumbled out through the open canvas flap and landed with a sickening thud on the stones.

Lorenzo stared down at the man’s caved-in skull, the naked limbs, the wasted flesh. More logs for the fire. Lorenzo’s bow trembled and his notes slid out of tune as his fingers went numb with the horror of what lay at his feet. COLONEL: Play! I order you, play! Forte, forte, forte!

Lorenzo dug his bow harder into the strings and tried to stay focused on his music stand, but the corpse was staring up at him, and Lorenzo could see the eyes were green.

Two soldiers jumped out of the truck to retrieve their lost bit of cargo. One of the soldiers tossed down the stub of the cigarette he’d been smoking, crushed it with his boot, and bent down to grasp the dead man’s ankles. His partner grasped the wrists and together they swung the corpse back into the truck, as casually as if they were tossing a sack of flour. For them, a dead body tumbling from their vehicle was not even worth a pause in their conversation. And why would it be, when there wer so many trucks like their rumbling in, day after day, each with the same terrible cargo? The butcher who hacks and saws away at countless carcasses does not think of sweet-faced lambs; he sees only meat. Just as the soldiers delivering their daily load of corpses saw only fresh fuel for the incinerator.

And through it all, the orchestra kept playing. Through the roar of the truck and the backing of dogs and the staccato of distant gunfire. Through the screams inside the oven. Most important, the screams. They played until those screams at last faded, until the trucks rumbled away empty and foul-smelling smoke billowed from the chimney. They played so they would not have to listen or think or feel, focusing on the music and only the music. Don’t concern yourselves with what’s happening in that building. Just keep your eyes on the notes, your bow on the strings.

(Pg 207) What was earlier a frantic melody has slowed to the ponderous chords of a funeral dirge. (Pg 208) A waltz . . . for the dying. (Pg 207) There is no dramatic flourish at the end, no dazzling final run. There are just three final notes, muted and mournful, which fade into silence. (Pg 215) For thousands of condemned prisoners who were marched to their executions, that waltz – Incendio, (The Fire) was the last music they heard. A waltz to die by.

(Pg 205) And when the day’s ordeal was over, when they were finally given leave to stop playing, they were too exhausted to rise from their chairs. (Pg 200) [You see,] most human beings can learn to endure almost anything, even the cries of the tormented. It was not that their hearts had hardened; it was because they could do nothing about it, and powerlessness leads to its own form of serenity.

(Pg 205) They sat with instruments lowered, heads bowed, until the guards prodded them to their feet. Then back to their cell they marched in silence. Their instruments had already spoken for them, and there was nothing left to say. (long beat)

(Pg 215) In October of 1944, Lorenzo Todesco and his fellow musicians were marched to their own executions. Their bodies were fed to the oven.
```

---

## IC-2105: Pluto Gets the Call

- Title: Pluto Gets the Call
- Author (byline): Adam Rex
- Work: Not specified
- Publisher: Beach Lane Books
- Publication date as stated: Nov 2019
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: PLUTO, STAR, NEPTUNE, URANUS, MOON, SATURN, JUPITER, ASTEROID, COMET, ASTEROID 2, CERES, MARS, EARTH, STAR 2, MERCURY, VENUS, SUN
- Teaser before the introduction: No
- Spoken words (computed): 1319
- Already set (do not supply): none

### Source block (context only)

```text
Author: Adam Rex
ISBN: 978-1534414532
Publisher: Beach Lane Books
Date (Month/Year): Nov 2019
```

### Introduction (context only: never use it for content warnings)

```text
For 76 years, Pluto was the beloved ninth planet in our solar system. No one cared that he/she was the runt of the solar system, with a moon half his/her size. NO one minded that he/she had a tilted, oval-shaped orbit. Pluto was a weirdo, but he/she was our weirdo.

But then one day in 2006, Pluto gets a call from some scientists on Earth, and they have some bad news — he actually isn’t a planet anymore. The International Astronomical Union (or IAU) had redefined the word “plant.” And Pluto no longer fit the bill. As you can imagine, Pluto isn’t too happy with this news, so he sets out on a journey through the solar system to find out why.

Pluto Gets the Call by Adam Rex
```

### Performance text (classify this)

```text
PLUTO: Ooh, someone’s going to call? Are they calling to invoice me to a party? I LOVE parties! (waving broadly) Hi . . . Hi! . . . Over here! Behind the ice and all those other guys. It’s me, Pluto! The ninth planet! It’s great to see you! We don’t get a lot of visitors out here in the Kuiper Belt. It’s this huge ring around the Sun that’s full of frozen stuff. It’s kind of my neighborhood, no big deal. (beat) So, not to brag, but I’m mostly made of nitrogen.

STAR: Ooh, nitrogen! (swoons)

PLUTO: I’m almost as big as Earth’s moon. I’m really cold, and I have a big heart on my belly ‘cause I love being a planet. Hold on a second, that’s my phone. (on the phone) You got Pluto! Oh, what a coincidence – I was just talking to someone from Earth. (to audience) Sorry, I should take this. (back on the phone) Uh-huh . . . Uh-huh . . What?! What do you mean I’m not a planet anymore? Why am I not a planet anymore. I . . . Uh . . . okay. Thank you for calling. (to audience) That was just some scientists from Earth. They say I’m not a planet anymore, no biggie. (getting angry) They asked if I’d like to be known as the solar system’s largest ice dwarf, and I was like, “How’d you like to known as Earth’s . . . meanest . . . jerks, huh? Huh?! (sadness set in) I didn’t really say that. I’m sorry, you were probably hoping to hang out with a real planet. Let me show you around.

(travels to the closest neighbor) Psst, Neptune! Are you awake?

NEPTUNE: (obviously waking up from a nap) Mweh?

PLUTO: This is Neptune. He’s closer to the Sun than me, but he’s still to far away that it takes him 65 years to orbit all the way around! It only takes Earth one year! One year exactly! That’s what a year is, actually.

STAR: AHHHHH! A black hole . . . . Don’t get sucked in!

NEPTUNE: (still groggy) Who are you talking to?

PLUTO: (To Neptune) No one, man, go back to sleep. (To audience) Neptune is pretty icy. (Neptune farts and Pluto reacts) And gassy. I’m not being mean, he just is. His twin is called Uranus – they’re practically the same size.

URANUS: Hey, Pluto!

STAR: Don’t mind Uranus. She always spins on her side! So do her rings!

MOON: When did she get rings? I want rings!

PLUTO: Uranus is icy, too. In fact, she and Neptune are called ice giants, which is . . . (sadly) which is why they want to call me an ice dwarf, I guess.

URANUS: What’s up, Pluto? I know you have a kind of a funky orbit, but I don’t usually see you this close to the Sun.

PLUTO: These Earth scientists say I’m not a planet anymore.

URANUS: WHAT?

PLUTO: Hold on, there’s my phone. Oh, look, it’s the scientists again (rolls eyes)

URANUS: (repositioning herself) Am I back in place?

STAR: Down a little to the left. (Uranus follows directions)

PLUTO: (on the phone) What do YOU want? (with attitude) No, as a matter of fact, I don’t want to be called a “plutoid.” Would you like to be called a “humanoid?” Sheesh! Hanging up! (to Uranus) I gotta go, Uranus.

URANUS: Stay frosty.

PLUTO: Next up are Saturn and Jupiter. They’re gas giants. Again, I am not making these names up.

SATURN: Hi, Pluto!

PLUTO: Hi, yourself! (to audience) Saturn has AMAZING rings!)

SATURN: Oh, stop!

PLUTO: They look like solid bands from far away, but really they’re made up of little bits of ice and rock and dust.

SATURN: (embarrassed, but loving it) Oh, stop, stop, stop, STOP! Uh . . . hey, look over there! It’s Jupiter!

JUPITER: (angrily) STOP LOOKING AT ME!

PLUTO: (whispers to audience) He’s a big ball of gas!

JUPITER: YOU’RE A BIG BALL OF GAS!

PLUTO: I’m . . . not, though. I’m little and I have a hard surface you can stand on. But Saturn and Jupiter don’t! If you tried to sand on Jupiter, you’d just fall right through him.

JUPITER: KEEP OFF THE GAS!

SATURN: You know, Jupiter . . . he’s really stormy. That Great Red Spot is a storm! It’s bigger than Earth, and it’s been there for as long as I can remember.

JUPITER: I’M BIGGER THAN ALL YOU PLANETS PUT TOGETHER!

Pluto: Uhhhh, I should go.

SATURN: Bye, Pluto! Call me!

PLUTO: (dodging asteroids and comets) Jeez. There’s a lot of garbage between Jupiter and Mars.

ASTEROID: Oh, nice. It’s Pluto, calling us garbage.

COMET: We’re not “garbage.” We’re bits of rocks called asteroids and comets.

ASTEROID: Together we’re called the Asteroid Belt.

PLUTO: Sorry! Gosh, I’m sorry.

ASTEROID: Just because he’s a planet, he thinks he’s better than us!

ASTEROID 2: What about Ceres? He’s pretty big. He orbits around the sun! He’s round like a planet!

CERES: (confronting Pluto) Yeah, that’s right! How come you’re a planet and I’m not?

PLUTO: I’m . . . actually not a planet anymore.

CERES: He’s not a planet anymore? HA! HA! He’s not a planet anymore. (Asteroid, Comet and Ceres laugh and point)

PLUTO: I don’t have to take this! I am OUT OF HERE!

(travels closer to the SUN, obviously warm, sweaty) Um. So, there’s Mars. She’s smaller than Earth, and she has a lot of water ice.

ASTEROID: I don’t see any water ice.

STAR: It’s under her surface. It’s part ice, water, dust, and small rocks.

COMET: That’s exactly what I put in my smoothies!

PLUTO: She’s called the Red Planet because of all the rusty iron on her surface. Hi, Mars!

MARS: (paranoid) I have robots on me.

PLUTO: Yeah?

MARS: Some of them just sit there. Some of them roll around. (Pluto and Mars look at each other incredulously) ROBOTS!! (whispers) The humans sent them here.

PLUTO: UGH! No offense, but I don’t want to talk about humans right now. (Pluto leaves in a huff) So next is Earth. (raises hand as if “talk to the hand” and looks the other direction in a major snub) It’s where mean scientists live – moving on!

EARTH: Oh, c’mon!

STAR: Look, there’s Earth’s moon! Guess who has the MOST moons.

STAR 2: super excited) Um, Mars! No, Neptune! Wait, Uranus! No, Mercury! Ooh, ooh, it’s Venus! I mean, Saturn! It’s Saturn, isn’t it?

STAR: (exasperated) Jupiter.

STAR 2: Awww, I was going to say that!

STAR: Wow! Pluto has traveled over 3.5 billion miles!

PLUTO: Venus and Mercury are really hot.

MERCURY: You’re not so bad yourself.

PLUTO: Venus is the hottest planet, and she’s hidden behind yellow acid clouds.

VENUS: (ashamed) You’d hide your face too if it was covered in volcanoes.

PLUTO: Mercury’s hot too, but he’s also cold!

MERCURY: (Sings a line from Foreigner) Cold as Ice!

PLUTO: If you were standing on Mercury in the Sun, you’d burn up. But if you stood in the shade, you’d freeze.

VENUS: Hey, Pluto, are you doing okay?

PLUTO: Oh, I’m just kind of down because I’m not a planet anymore.

VENUS: Not a planet? But you’re round.

PLUTO: Yeah.

MERCURY: You orbit the Sun. You don’t orbit another planet like a moon does.

PLUTO: Yeah, but I live in a crowded neighborhood. I guess a real planet’s supposed to sweep all the ice and rocks out of the way.

VENUS: Hey, why don’t you go talk to the boss about this?

PLUTO: Maybe I will!

MERCURY: Yeah, man! Go ask the Sun’s advice – she’s pretty bright. (laughing at his own joke, when no one else laughs, he tries to explain) Did you get what I said? Pretty bright? Because she’s the Sun.

PLUTO: Yeah, no. I got it. (traveling onward)

SUN: Pluto! You’re far from home!

PLUTO: (sadly) Did you hear what happened to me?

SUN: (nodding) Pluto, you were orbiting around me for billions of years before the word “planet” was even invented.

PLUTO: Oh, I know. I just liked feeling special for a while.

SUN: Look out at the solar system, my friend. (gazing out into the distance) Mercury is the smallest.

MERCURY: And, dare I say, the cutest!

SUN: Venus is the hottest.

VENUS: (spinning in circles) And I rotate in the opposite direction as most everyone else.

SUN: Earth has life.

EARTH: (has just taken a bite and speaks with a full mouth) And this yummy sandwich!

SUN: Mars has robots.

MARS: I guess they’re kind of cool.

SUN: Jupiter’s the biggest.

JUPITER: Stop Staring at my red spot. (covers himself)

SUN: Saturn has its rings.

SATURN: (waving with both hands) Yoo-hoo! Hi, Pluto!

SUN: People talk about Uranus for reasons I don’t really want to get into.

URANUS: (turns and begins to bend over, then rethinks it) Aww, shucks, you must mean my charming personality.

SUN: And . . . well, Neptune is Neptune . . .

NEPTUNE: What’s THAT supposed to mean?

SUN: (gearing up for a rousing pep talk) But you, Pluto . . . you’re the planet who doesn’t get to be a planet anymore. And people love you for it. You’re still a planet to everyone who was too short to ride the Ferris wheel. To everyone who’s ever put seven dollars into a claw machine and still didn’t get the hippopotamus they wanted. To all the people picked last for kickball. Do you know that right now, as we speak, those scientists are still arguing about you?

PLUTO: They are?

SUN: You used to be the coldest, littlest planet . . but now you have a big warm place in our hearts.

EARTH: There, there, don’t cry Jupiter

JUPITER: (obviously crying) I’m not crying. I have . . . meteor dust in my eyes!

PLUTO: Thanks, Sun. . . I’d hug you, but . . .

SUN: You’d burn up instantly. It’s cool.
```

---

## IC-2106: Politically Correct Cinderella

- Title: Politically Correct Cinderella
- Author (byline): James Finn Garner
- Work: Once Upon a More Enlightened Time
- Publisher: MacMillan Publishing Company
- Publication date as stated: May 1995
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1166
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Finn Garner
Book: Once Upon a More Enlightened Time
ISBN: 978-0028604190
Publisher: MacMillan Publishing Company
Date (Month/Year): May 1995
```

### Introduction (context only: never use it for content warnings)

```text
Once upon a time, in the windy kingdom of Chicago, there lived a left-of-center, freelance scribe, struggling through the '90s on feeble jests and weak rejoinders. He was basically minding his own business, trying to be progressive and enlightened, diverse and multicultural, even though, as a heterosexual, phallocentric white male, he recognized he was severely challenged, both in terms of pigment and moral clarity.

Then, one day in 1991, he happened upon a didactic little newsletter warning preschool and kindergarten teachers about the ideological perils of such classic fairy tales as Snow White, Rumpelstiltskin and Cinderella.

Inherently sexist the newsletter charged. Full of destructive biases, not to mention disempowered women. If a child admits to enjoying Cinderella, the newsletter advised, it's the teacher's job to embarrass the child. Cinderella the story shouldn't be enjoyed because Cinderella is a ''simp'' who makes no decisions for herself.

That's it, decided James Finn Garner, the left-of-center, scribe. This has gone way too far. Someone's got to stop this silliness now. So here it is . . . the Politically Correct Cinderella by James Finn Garner.
```

### Performance text (classify this)

```text
There once lived a young wommon named Cinderella, whose natural birthmother had died when Cinderella was but a child. A few years after, her father married a widow with two older daughters. Cinderella’s mother-of-step treated her very cruelly, and her sisters-of-step made her work very hard, as if she were their own personal unpaid laborer.

One day an invitation arrived at their house. The prince was celebrating his exploitation of the dispossessed and marginalized peasantry by throwing a fancy dress ball. Cinderella’s sisters-of-step were very excited to be invited to the palace. They began to plan the expensive clothes they would use to alter and enslave their natural body images to emulate an unrealistic standard of feminine beauty. (It was especially unrealistic in their case, as they were differently visage enough to stop a clock.) Her mother-of-step also planned to go to the ball, so Cinderella was working harder than a dog (an appropriate if unfortunately speciesist metaphor).

When the day of the ball arrived, Cinderella helped her mother- and sisters-of-step into their ball gowns. A formidable task: It was like trying to force ten pounds of processed nonhuman animal carcasses into a five-pound skin. Next came immense cosmetic augmentation, which it would be best not to describe at all. As evening fell, her mother- and sisters-of-step left Cinderella at home to finish her housework. Cinderella was sad, but she contented herself with her Holly Near records.

Suddenly there was a flash of light, and in front of Cinderella stood a man dressed in loose-fitting, all-cotton clothes and wearing a wide-brimmed hat. At first Cinderella thought he was a Southern lawyer or a bandleader, but he soon put her straight.

“Hello, Cinderella, I am your fairy godperson, or individual diety proxy, if you prefer. So, you want to go to the ball, eh? And bind yourself in the male concept of beauty? Squeeze into some tight-fitting dress that will cut off your circulation? Jam your feet into high-heeled shoes that will ruin your bone structure? Paint your face with chemicals and make-up that have been tested on nonhuman animals?”

“Oh, yes, definitely!” she said in an instant. Her fairy godperson heaved a great sigh and decided to put off her political education till another day. With his magic, he enveloped her in a beautiful, bright light and whisked her away to the palace.

Many, many carriages were lined up outside the place that night; apparently, no one had ever thought of carpooling. Soon, in a heavy, gilded carriage painfully pulled by a team of horse-slaves, Cinderella arrived. She was dressed in a clinging gown woven of silk stolen from unsuspecting silk-worms. Her hair was festooned with pearls plundered from hard-working, defenseless oysters. And on her feet, dangerous though it may seem, she wore slippers made of finely cut crystal.

Every head in the ballroom turned as Cinderella entered. The men stared at and lusted after this wommon who had captured perfectly their Barbie-doll ideas of feminine desirability. The womyn, trained at an early age to despise their own bodies, looked at Cinderella with envy and spite. Cinderella’s own mother-and sisters-of-step, consumed with jealousy, failed to recognize her.

Cinderella soon caught the robing eye of the prince, who was busy discussing jousting and bear-baiting with his cronies. Upon seeing her, the prince was struck with a fit of not being able to speak as well as the majority of the population. “Here,” he thought, “is a wommon that I could make my princess and impregnate with the progeny of our perfect genes, and thus make myself the envy of every other prince for miles around. And she’s blond, too!”

The prince began to cross the ballroom toward his intended prey. His cronies also began to walk toward Cinderella. So did every other male in the ballroom who was younger than 70 and not serving drinks.

Cinderella was proud of the commotion she was causing. She walked with head high and carried herself like a wommon of eminent social standing. But soon it became clear that the commotion was turning into something ugly, or at least socially dysfunctional.

The prince had made it clear to his friends that he was intent on “possessing”’ the young wommon. But the prince’s resoluteness angered his pals, for they too lusted after her and wanted to own her. The men began to shout and push each other. The prince’s best friend, who was a large if cerebrally constrained duke, stopped him halfway across the dance floor and insisted that he was going to have Cinderella. The prince’s response was a swift kick to the groin, which left the duke temporarily inactive. But the prince was quickly seized by other sex-crazed males, and he disappeared into a pile of human animals.

The woymn were appalled by this vicious display of testosterone, but try as they might, they were unable to separate the combatant. To the other womyn, it seemed that Cinderella was the cause of all the trouble, so they encircled her and began to display very unsisterly hostility. She tried to escape but her impractical glass slippers made it nearly impossible. Fortunately for her, none of the other womyn were shod any better.

The noise grew so loud that no one heard the clock in the tower chime midnight. When the bell rang the twelfth time, Cinderella’s beautiful gown and slippers disappeared, and she was dressed once again in her peasant’s rags. Her mother- and sisters-of-step recognized her now, but kept quiet to avoid embarrassment.

The womyn grew silent at this magical transformation. Freed from the confinements of her gown and slippers, Cinderella sighed and stretched and scratched her ribs. She smiled, closed her eyes and said, “Kill me now if you want, sisters, but at least I’ll die in comfort.”

The womyn around her again grew envious, but this time they took a different approach: Instead of exacting vengeance on her, they stripped off their bodices, corsets, shoes, and every other confining garment. They danced and jumped and screeched in sheer joy, comfortable at last in their shifts and bare feet.

Had the men looked up from their macho dance of destruction, they would have seen many desirable womyn dressed as if for the boudoir. But they never ceased pounding, punching, kicking, and clawing each other until, to the last man, they were dead.

The womyn clucked their tongues but felt no remorse. The palace and realm were theirs now. Their first official act was to dress the men in their discarded dresses and tell the media that the fight arose when someone threatened to expose the cross-dressing tendencies of the prince and his cronies. Their second was to set up a clothing co-op that produced only comfortable, practical clothes for womyn. Then they hung a sign on the castle advertising CinderWear (for that was what the new clothing was called), and through self-determination and clever marketing, the all – even the mother and sisters-of-step – lived happily ever after.
```

---

## IC-2107: Politically Correct The Princess and the Pea

- Title: Politically Correct The Princess and the Pea
- Author (byline): James Finn Garner
- Work: Once Upon a More Enlightened Time
- Publisher: MacMillan Publishing Company
- Publication date as stated: May 1995
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1297
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Finn Garner
Book: Once Upon a More Enlightened Time
ISBN: 978-0028604190
Publisher: MacMillan Publishing Company
Date (Month/Year): May 1995
```

### Introduction (context only: never use it for content warnings)

```text
And so begins the story of the Princess and the Pea . . . You remember the story . . . the one with the moral that goes something like this . . . if you are extremely sensitive and fussy about your own physical comfort, and complain to your host about small imperfections, instead of being tactful and polite; then you are special and deserve to marry a handsome prince and live happily ever after.

Yeah, right . . . . Somehow I cannot imagine the princess from this story living "happily ever after." If she was sensitive enough to be bothered by a pea under a gazillion mattresses, then how in the world would she cope when the honeymoon was over and the prince started leaving the toilet seat up?

Fortunately, James Finn Garner gives us an alternate version . . . a politically correct version of The Princess and the Pea.
```

### Performance text (classify this)

```text
In a kingdom over the hills and far away, there lived a young prince who was very full of himself. He was healthy, relatively handsome, and had had more than his fair share of happiness and comfort growing up. Yet he felt that he deserved something more. IT was not enough for him to have been born into a life of parasitical leisure and to keep the masses firmly under the heel of his calfskin boots. He was also determined to perpetuate this undemocratic tyranny by marrying only a real, authentic, card-carrying princess.

His mother, the queen, encouraged her son’s obsession, despite the obvious risks of hemophiliac or microcephalic grandchildren. Many years earlier, after a period of inadequate wellness, his father the king had achieved corporal terminality. This lack of a strong male presence gnawed at the prince on a subconscious level, and no amount of weekend retreats and male bonding with other young dukes and barons could relieve this anxiety. His mother, for her own codependent and Oedipal reasons, did not bother to change or correct his selfish notions or unattainable perfection in a spousal lifemate.

In his quest for the perfect partner, the prince travelled far and wide, looking for someone to enslave in matrimony. Astride his trusty equine colleague, he went from kingdom to queendom and from dukedom to duchessdom, asking for names and phone numbers. Heavily or lightly pigmented, vertically or horizontally challenged, cosmetically attractive or differently visaged – he cared not a whit. His only criterion was the royal authenticity of a wommon who could share his regal delusions of privilege and persunal worth.

One rainy night, after a long journey to many far-off bioregions, the prince nourished himself with a bowl of lentil-curry stew and confided his fears to his mother: I don’t think I’ll ever find a genuine princess with whom to share my life, Mummy.”

“Well, Son,” the queen reassured him, “don’t forget the many benefits of the single life. Don’t let society and the church pressure you into a lifestyle for which you might not be suited.”

“Perhaps I should widen my scope a bit,” he mused.

“What? And throw out your standards?”

“No, Mummy, perphas I have fallen into a trap of the orthodox heterosexualist majority. Maybe there’s a fine young prince out there for me. It’s at least worth a try.

Before his mother could answer, there was a knock on the castle door. The servants pulled open the heavy portal, and out of the rain stepped a young wommon, who was moisture-enhanced from head to foot. She was certainly attractive to the eye, if you’re the type of shallow person who attached value to appearances. Luckily for our story, the prince was not one of those types. He had one standard, and only one standard, classist though it might have been.

Imagine the prince’s surprise when the visitor blurted out, “A princess shouldn’t be out in weather like this!”

Well now, this was a revelation straight from the equine animal companion’s mouth! The prine was struck orally inoperative for a moment, then invited the dryness-challenged visitor to enjoy their hospitality in the castle overnight.

While this was certainly a joyous development for the prince, his mother felt very threatened that someone was taking her son away from her. But rather than acknowledging the validity of her feelings and airing them in a constructive way, the queen decided on a ruse to test the visitor’s claim.

She sneaked up to the bedchambers and found the room where the persun of saturation would be sleeping. She tore off all the bedding from the frame and placed one single pea on the bed slats. Then she placed 10 futons on top of the pea, and on top of that, 10 eiderdown quilts.

“There,” said the queen. “If that drenched wench downstairs is really a princess, she will be refined enough to notice this lump and be unable to sleep.”

The next morning at breakfast, over the royal granola, the queen innocently asked the young wommon how she had slept.

“Abominably,” she replied. “I didn’t get a wink all night.”

The queen’s eyes grew wide. Had her plan worked too well?

The visitor continued, “First of all, the bed was piled high with eiderdown quilts. Barbaric! How could I sleep, thinking of the poor naked geese who surrendered their feather for my comfort?”

The queen reddened a bit but said nothing.

“Then, as I was removing the extra futons to share them with some of the less fortunate peasants living around the castle, I found a pea placed beneath them all. Shocking, with the state of the world as it is, that someone would waste food like that.”

With these statements, the queen nearly choked on her soy milk. The prince, who had learned of his mother’s scheme to screen out a princess, was so excited he couldn’t keep silent any longer. “So you really are a princess!” he yelped.

“Last night I was, yes,” she replied. The quizzical looks from the prince and queen led the wommon to elaborate: “Last night I was a princess; this morning I’m an ancient Viking warrior. Oh, you sillies – I’m channeling! I have over a dozen past persunalities that periodically inhabit my body – everyone from Charlemagne’s mistress to Aesop’s brother-in-law. And Cleopatra. But then, everyone’s been Cleopatra at some time or other. Let me tell you, it makes for some interesting conversation at parties! It’s all pretty exciting for an economically disadvantaged spoonmaker’s daughter who grew up on the wrong side of the drainage ditch.”

These revelations made the queen very angry, but the prince was intrigued. “So, when do you think you will be channeling a princess again?”

“A week from Tuesday,” she said matter-of-factly, “mid-morning until early evening. I am very punctual with my past lives.”

“Then on that Tuesday afternoon I will ask you to be my wife and castle-mate, and you can rule by my side as an equal partner in every way.”

The wommon considered a moment, then answered: “I would glady accept, if not for the fact that this morning, as I have asaid, I am a Viking warrior – Liefdahl by name, son of Ulfdahl – and I have a strong notion to lay siege to your castle just after breakfast.” She calmly took a sip of coffee and grabbed another muffin.

“How rude!” said the queen with a slap on the table. “We give her lodging in a storm and breakfast the next morning, and she swaps persunalities on us and calmly talks about laying siege to us, without so much as a ‘by your leave’!”

“Mother, please,” said the prince. “Now how long are you generally a Viking warrior?”

“Oh, no longer than 45 minutes.”

“And after that?” he asked.

“After that, I’m usually the hermit St. Giles, living in a hovel and renouncing all worldly possessions.”

“And that would include . . . ?”

“That would include” – the visitor smiled with a dawning awareness – “renouncing any and all worldly kingdoms conquered by my other spiritual co-habitators.”

So, as is often the case, timing was crucial to a happy ending to our story. The “princess” and the prince were married the second Tuesday following, in accordance with her metaphysical timetable, and they had a very happy honeymoon, especially during certain transformation. Every time she became Liefdal, son of Ulfdahl, she would conquer the prince and his castle, and every time she became St. Giles, she would give it right back. Channeling past lives and historical persunalities became de rigueur in court from that day forward, and the queen, the prince, and the channeler lived a very happy life together, never quite knowing who would turn up at breakfast.
```

---

## IC-2108: The Princess and the Pea

- Title: The Princess and the Pea
- Author (byline): AJ Jacobs
- Work: Fractured Fairy Tales
- Publisher: Bantam Books, Inc.
- Publication date as stated: Nov 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 905
- Already set (do not supply): none

### Source block (context only)

```text
Author: AJ Jacobs
Book: Fractured Fairy Tales
ISBN: 978-0553099805
Publisher: Bantam Books, Inc.
Date (Month/Year): Nov 1997
```

### Introduction (context only: never use it for content warnings)

```text
Ugly princes, fibbing fairy godmothers, and knights who prefer clown suits to suits of armor - these clearly aren't your ordinary fairy tales. They are, in fact, Jay Ward's infamous Fractured Fairy Tales, originally introduced within Ward's brilliant Rocky & Bullwinkle Show, on television in the 1960s.

From princesses who take destiny into their own capable hands, to inept witches with broomstick envy, to beauties who happily discover their inner beasts, these tales contain surprisingly modern messages of female empowerment – Unless, of course, you are a Princess named Clyde. The Princess and the Pea as collected and published by AJ Jacobs.
```

### Performance text (classify this)

```text
It seems that once upon a time there was a kingdom without a princess, and this concerned the king and his ministers greatly.

"We are facing a severe heiress deficit," the prime minister told the king, tapping a chart. "We must immediately increase the number of young female royal individuals in the palace vicinity."

"You mean," sighed the king, "we've got to find a princess."

"That's what I said."

This wasn't an impossible task. The king once did have a princess, but she had been lost since childhood. The king and his ministers simply had to figure out how to track her down. But just as they got started thinking, they were interrupted by the court jester, Million Laughs Charlie.

“Thank you, thank you. Good to be here, folks!" said Charlie, shaking his rattle. "You know, the other day, I walked into this bar, and there was this Irishman and this rabbi-"

"Please," said the king, "we're doing some busi-ness here." Then, to his ministers, he said, "How about if we offer a million gold crickles to the princess when she shows up."

"A million gold crickles!" interrupted Charlie again. "I'd love to help on this project. Do you remember what she looked like?"

"No," said the king.

"Good! I mean, that's too bad," said Charlie, rub-bing his hands.

"She was just a baby when she left," said the king. "But I'll know her by the way she passes this test I have in mind."

But Million Laughs Charlie wasn't listening any-more. He wasn't even there. Charlie had run home, called up his date for the night-a lovely maiden who lived next door-canceled on her, and got straight to work on his scheme.

He recruited his friend Clyde, a rather big man with a rather small brain, to help. And before Clyde knew what had happened, he had on a blond wig, a lot of1ipstick, and was on the way to the palace to meet the king.

"I don't want to be no princess!" whined Clyde. "These high heels are killin' me."

"Shush," shushed Charlie, as they arrived at the palace front door. "Hey, King. I'd like to introduce you to your princess!"

"Hmm," said the king. "She's got more of a five o'clock shadow than I remember my princess having. But if she passes the test, then I'll know she's the one."

With that, the king led the make-believe princess to a tall pile of mattresses. Under the bottom mattress, he explained, there was a small pea. If she was a real princess, she would be so refined, so sensitive, that even a tiny lump like that wouldn't let her sleep.

The make-believe princess climbed to the top of the pile and lay down as Charlie, the king, and his min-isters waited at the bottom. In the morning, the king and his court climbed to the top and, sure enough, the make-believe princess was snoring away blissfully.

"Ah-ha!" said the prime minister. This individual lacks the qualities necessary to be a member of the royal family."

"He means," sighed the king, "this ain't no princess."

Charlie and Clyde found themselves escorted out of the palace, helped along by a swift kick or two on the bottom from the palace guards.

"Now you've done it, you hussy!" shouted Million Laughs Charlie. But Clyde didn't get off that easily. Over the next few days, Charlie dressed his friend up in a red wig, a brown wig, and a browner wig and sent him off to the palace to pretend to be another girl. Hoping to keep him up, he would feed Clyde coffee and tell him scary tales about monsters and politicians. But each time, Clyde would sleep soundly through the night. And in the morning, he would be forced to leave the palace, rubbing his rear.

After several days of this, the two dejected men went back to Charlie's house to regroup. There, Char-lie's neighbor was out in the yard, washing her carriage.

"Hey, honey," Charlie said to her. "My business deal fell through. Got some time on my hands. What say we go out and have a bite to eat."

"Sorry, Charlie," said the maiden. "I'm exhausted. I didn't get a wink last night. I think there was a pea under my mattress."

"Did you try maybe reading anything by John Up-dike'?" asked Charlie. "Wait a sec. Didn't sleep a wink?"

Yes, Charlie had figured it out. This really was a princess. The real thing. The girl that would get the million gold crickles and all the titles of her realm. Be-fore you could say "greedy no-goodnik," Charlie had taken the girl to meet the king.

"Oh, darling," said the king, giving his daughter a hug. "Here's a million gold crickles-minus thirty percent for taxes-plus your choice of any man in the kingdom."

"Wow!" said the princess. "Any man in the king-dom'?" She smiled, looking over at her escort-and his friend. "Oh, Clyde. Will you be mine?"

"For keeps!" said Clyde.

That's the story. The king had his daughter, the princess had her gold, and Clyde had the princess and they all lived happily ever after. Ooops. Almost all lived happily ever after. Poor Million Laughs Charlie spent the rest of his days unsuccessfully trying to sell unauthorized fairy tales of the king and his court.
```

---

## IC-2109: Psssst! It’s Me. . . The Bogeyman

- Title: Psssst! It’s Me. . . The Bogeyman
- Author (byline): Barbara Park
- Work: Not specified
- Publisher: Atheneum
- Publication date as stated: Sept 1998
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: BOGEYMAN, THE NATIONAL SQUEALER
- Teaser before the introduction: No
- Spoken words (computed): 857
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barbara Park
ISBN: 978-0689816673
Publisher: Atheneum
Date (Month/Year): Sept 1998
```

### Introduction (context only: never use it for content warnings)

```text
So, I’ve asked a lot of people – people my age, adults, little kids; and I’ve come to realize one thing. I am not alone. Almost everyone, at one time or another, has had an overwhelming fear of 1) the dark or 2) even worse: things IN the dark. Yes, I’m talking about monsters.

It’s bedtime. You go into your room, look around. No monsters in sight. You flip off the light switch, make a mad dash for your bed, pull the covers over your head as quickly as you can, and (big breath in) hold your breath. . . listening intently for any sound. Because you realize there are a few places you may have forgotten to check. The closet??? Under your bed ???

Psssst! It’s Me. . .The Bogeyman by Barbara Park
```

### Performance text (classify this)

```text
BOGEYMAN: Pssssssst! Yo! Down here . . . under the bed. It’s me, the Bogeyman. Yeah, you hear me, Sparkie. It’s the genuine, creepy-crawly, blood-chilling, spine-tingling, can’t-avoid-the-urge-to-grab-your-ankle-when-you’re-climbing-into-the-sack, Bogeyguy. And the news doesn’t get any better, Bud, ‘cause I’m stew-spewin’, gravel chewin’ mad.

Oh, quit your shivering, Skeezicks. It isn’t you who’s got me fuming. Here! Just take a look at this morning’s headline!

THE NATIONAL SQUEALER: EVIL BOGEYMAN BELLOWS BOO – BOY SCOUTS GO BERSERK -- THE BOGEYMAN WILL GET YA IF YA DON’T WATCH OUT!

It’s a lie, I tell you! That lummox isn’t me! I don’t go clomping after campers like some bumbling, stumbling Frankenstein. And even if I did, I’d never stop and pose for pictures. I’d lose my job, Jake.

Check it out . . . It’s all right here on page three of my Official Bogeyman Contract.

OFFICIAL BOGEYMAN CONTRACT

• The bogeyman’s identity must be protected at all costs.

• No one must ever gaze upon your face, or (heaven forbid!) take your picture and then (perish the thought!) print it in the tabloids.

• If any of these calamities should occur, we, the management, regret to inform you that your services as the Bogeyman will no longer be required.

There, see? You’ve gotta help me clear my name! The photo’s a fake. A fib, a fraud!

And here’s another news flash, Filbert: The Bogeyman doesn’t say BOO. Boo’s a baby word, Bubbie. It rhymes with toodle-loo. And Winnie the Pooh. And it comes after peek-a-. And right before hoo. And okay, maybe if you scream it really loud at a football game, it might mean the ref made a bad call. But no matter how you shout it, boo just ain’t scary, Skippy.

Want to know a scary word? I’ll give you five of ‘em: Go . . . get . . . read . . . for . . . bed. Yeah, you know what I’m talking about. Especially if it’s a dark and stormy night, and your pj’s are in your closet, all the way in . . . the . . . back. And oh, dearie me, your lightbulb burned out last night. But you fight your fear and head upstairs.

Then you stop at the top and peer into the pitch-black darkness of your room. You’d have to be insane to go in there. Am I right, Dwight? But suddenly, your dim-witted feet rush you right across your rug, and deposit you slap dab in front of your closet door which swings open all by itself. (sound effect) (Hmmm. That’s odd.)

Still, you gather your courage and reach for the hook. And silly-willy me, I been waitin’ for you, Jack. And I tenderly tickle your arm with my finest fingernail. (scream) And you yell so loud and run so fast, you never even hear me collapse on the closet floor and bust a gut full of giggles. (insane giggles)

News flash number three: I don’t bellow. Why, I rarely even raise my voice. I’m a professional, Peppie. I whisssssper and I murrrmurrr. And I whoooosh and swoooosh and saaail. And, weather permitting, I even waffffft on warm summer winds. Which is why, my little whippersnapper, on that dark, moonless night last August, when dear old Dad left you all alone in your big backyard, looking for the Little Dipper, you heard just the faintest of sounds as I sneaked up behind you on marshmallow feet and fluttered my eyelashes close to your ear.

Th-then th-th-that’s when you s-s-sensed that you (gulp) w-w-weren’t alone, and the hairs on your neck tried to stand up and run as your knockin’, rockin’ legs turned to jiggle-jam-jelly. And seriously, Seymour, don’t you just hate it when that happens?

News Flash number four: The Bogeyman does not “Get ya.” What does that even mean, get ya? If I got ya, what would I do with ya? Where would I put ya? And what would I feed ya? My job is to scare ya. I don’t want to raise ya. So enough already with the get ya garbage.

I’m not “EVIL,” Alvin. In fact, I’m not that different from you. I gobble up chicken fingers and I gulp down Gummi Bears. And after eating, I almost always floss my tooth before slipping under someone’s bed to catch a few zzzzzz’s. Which is exactly what I’m about to do now. All this belly-achin’ has got me beat. Besides, I’m off-duty, and my cloak is at the clearners. So, start spreadin’ the word that this headline (shakes newspaper) is hogwash.

Oh, yeah, and kindly keep your smelly sweatsocks off the floor. I’m allergic, okay? Just one wiff of those things and I’m outa here, Dude. I start gaspin’ and wheezin’ and chokin’ and sneezin’. Plus I break out in itchy, splotchy blue blotchies. So, like I said, just keep them – Whoa, Whoa, WHOA!

Hold on a second, Sherlock. You’re not takin off those socks now, are you? You are? But . . . but I thought we were pals. Hey! (gasp) Stop waving them around! (wheeze) What’s gotten into you anyway? (sneeze) Wait! Knock it off! (itching, scratching, sneezing) Not all those!! Ugh! Bluck!!! Ick! AAAUUUUUGGGGHHH! I’m gone! (He flees in a panic to a bedroom down the hall)

(Still coughing) Pssssssst! Yo! Down here . . . under the bed. It’s me, the Bogeyman.
```

---

## IC-2110: Racism and Fascism

- Title: Racism and Fascism
- Author (byline): Toni Morrison
- Work: The Source of Self-Regard
- Publisher: Knopf
- Publication date as stated: Feb 2019
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 654
- Already set (do not supply): none

### Source block (context only)

```text
Author: Toni Morrison
Book: The Source of Self-Regard
ISBN: 978-0525521037
Publisher: Knopf
Date (Month/Year): Feb 2019
NOTE: Excerpt from Charter Day Speech, "The First
Solution" presented at Howard University, Washington
DC, March 3, 1995.
```

### Introduction (context only: never use it for content warnings)

```text
Most people recognize the following quote: “Those who cannot remember the past are condemned to repeat it.” In fact, history repeating itself is a common warning in all walks of life. Humanity is constantly reminding itself that everyone must learn from their mistakes. Yet, one look at our history proves that this reminder is often ignored or forgotten.

In 1995 Toni Morrison spoke at Howard University in Washington DC with a grim reminder of this prophecy. Now, nearly 25 years later . . . our country is becoming more and more politically divided. We have once again demonized the enemy – “the migrant hoard” – and created holding areas for those who have been vilified – especially the children.

As you listen to Toni Morrison’s speech on Racism and Fascism – ask yourself – has humanity learned from their mistakes or are we racing once again down the same path to a humanitarian crisis?
```

### Performance text (classify this)

```text
Let us be reminded that before there is a final

solution, there must be a first solution, a second one, even a third. The move toward a final solution is not a jump. It takes one step, then another, then another.

Something, perhaps, like this: 1. Construct an internal enemy, as both focus and diversion. 2. Isolate and demonize that enemy by unleashing and protecting the utterance of overt and coded name-calling and verbal abuse. Employ ad hominem attacks as legitimate charges against that enemy. 3. Enlist and create sources and distributors of information who are willing to reinforce the demonizing process because it is profitable, because it grants power, and because it works. 4. Palisade all art forms; monitor, discredit, or expel those that challenge or destabilize processes of demonization and deification. 5. Subvert and malign all representatives of and sympathizers with this constructed enemy. 6. Solicit, from among the enemy, collaborators who agree with and can sanitize the dispossession process. 7. Pathologize the enemy in scholarly and popular mediums; recycle, for example, scientific racism and the myths of racial superiority in ordor to naturalize the pathology 8. Criminalize the enemy. Then prepare, budget for, and rationalize the building of holding arenas for the enemy especially its males and absolutely its children. 9. Reward mindlessness and apathy with monumentalized entertainments and with little pleasures, tiny seductions: a few minutes on television, a few lines in the press; a little pseudo-success; the illusion of power and influence; a little fun, a little style, a little consequence. 10. Maintain, at all costs, silence. In 1995 racism may wear a new dress, buy a new

pair of boots, but neither it nor its succubus twin fascism is new or can make anything new. It can only reproduce the environment that supports its own health: fear, denial, and an atmosphere in which its victims have lost the will to fight.

The forces interested in fascist solutions to

national problems are not to be found in one political party or another, or in one or another wing of any single political party. Democrats have no unsullied his-tory of egalitarianism. Nor are liberals free of domination agendas. Republicans have housed abolitionists and white supremacists. Conservative, moderate, liberal; right, left, hard left, far right; religious, secular, socialist-we must not be blindsided by these Pepsi-Cola, Coca-Cola labels because the genius of fascism is that any political structure can host the virus and virtually any developed country can become a suitable home. Fascism talks ideology, but it is really just marketing-marketing for power. It is recognizable by its need to purge, by the

strategies it uses to purge, and by its terror of truly democratic agendas. It is recognizable by its determination to convert all public services to private entrepreneurship, all nonprofit organizations to profit-making ones-so that the narrow but protective chasm between governance and business disappears.

It changes citizens into taxpayers-so individuals become angry at even the notion of the public good.

It changes neighbors into consumers-so the measure of our value as humans is not our humanity or our compassion or our generosity but what we own. It changes parenting into panicking – so that we vote against the interests of our own children; against their health care, their education, their safety from weapons. And in effecting these changes it produces the perfect capitalist, one who is willing to kill a human being for a product (a pair of sneakers, a jacket, a car) or kill generations for control of products (oil, drugs, fruit, gold). When our fears have all been serialized, our creativity censured, our ideas "marketplaced," our rights sold, our intelligence sloganized, our strength downsized, our privacy auctioned; when the theatricality, the entertainment value, the

marketing of life is complete, we will find ourselves living not in a nation but in a consortium of industries, and wholly unintelligible to ourselves except for what we see as through a screen darkly.
```

---

## IC-2111: Rapunzel

- Title: Rapunzel
- Author (byline): James Finn Garner
- Work: Politically Correct Bedtime Stories: Modern Tales for Our Life and Times (Pg 23-30)
- Publisher: John Wiley and Sons, Inc.
- Publication date as stated: April 1994
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, WITCH, TINKER, PRINCE, RAPUNZEL
- Teaser before the introduction: Yes
- Spoken words (computed): 1200
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Finn Garner
Book: Politically Correct Bedtime Stories: Modern Tales
for Our Life and Times (Pg 23-30)
ISBN: 978-0025427303
Publisher: John Wiley and Sons, Inc.
Date (Month/Year): April 1994
```

### Introduction (context only: never use it for content warnings)

```text
Once upon a time, heavy-set middle-aged men would congregate in their elitist clubs, smoke air-choking cigars, and pitch story ideas to each other. Problem was, these stories, reflected the way in which these men saw their world: that is, the stories were sexist, discriminatory, culturally biased, demeaning to witches, animals, goblins, and fairies everywhere. Enter James Finn Garner and his absurd and politically correct retelling of Rapunzel from Politically Correct Bedtime Stories.
```

### Performance text (classify this)

```text
NARRATOR: (Pg 23-30) There once lived an economically disadvantaged tinker and his wife. His lack of material accomplishment is not meant to imply that all tinkers are economically marginalized, or that if they are, they deserve to be so. This particular individual was a tinker by trade and just happened to be economically disadvantaged.

NARRATOR: The tinker and his wife lived in a little hovel next to the modest estate of a local witch. From their window, they could see the witch's meticulously kept garden, a nauseating attempt to impose human notions of order onto Nature.

The wife of the tinker was pregnant, and as she gazed at the witch's garden, she began to crave some of the lettuce she saw growing there. She begged the tinker to jump the fence and get some for her. The tinker finally submitted, jumped the wall and liberated some of the lettuce. But before he could get back, the witch caught him.

Now, this witch was very kindness-impaired. (This is not meant to imply that all witches are that way. Far from it, her disposition was without doubt due to many factors of her upbringing and socialization, which, unfortunately must be omitted here in the interest of brevity.) . . . The witch was kindness-impaired, and the tinker was extremely frightened. She held him by the scruff of the neck and asked,

WITCH: Where are you going with my lettuce?

NARRATOR: The tinker might have argued with her over the concept of ownership and stated that the lettuce rightfully "belonged" to anyone who was hungry and had nerve enough to take it. Instead, in a degrading spectacle, he pleaded for mercy.

TINKER: It was my wife's fault! She is pregnant and has a craving for some of your lovely lettuce. Please spare me. Although a single-parent household is certainly acceptable, please don't kill me and deprive my child of a stable, two-parent family structure.

NARRATOR: The witch thought for a moment, then let go of the tinker's neck and disappeared without a word. The tinker gratefully went home with the lettuce. A few months later, and after agonizing pain that a man will never really be able to appreciate, the tinker's wife gave birth to a beautiful, healthy pre-wommon. They named the baby Rapunzel, after a type of lettuce.

Not long after this, the witch appeared at their door, demanding that they give her the child in return for the witch's having spared the tinker's life in the garden. What could they do? Their powerless station in life had always left them open to exploitation, and this time they felt they had no alternative. They gave Rapunzel to the witch, who sped away.

The witch took the child deep into the woods and imprisoned her in a tall tower, the symbolism of which should be obvious. There Rapunzel grew to wommonhood. The tower had no door or stairs, but it did boast a single window at the top. The only way for anyone to get to the window was for Rapunzel to let down her long, luxurious hair and climb it to the top, the symbolism of which should also be obvious.

The witch was Rapunzel's only companion. She would stand at the foot of the tower and shout,

WITCH: Rapunzel, Rapunzel, let down your hair, that I might climb your golden stair.

NARRATOR: Rapunzel obediently did as she was told. Thus, for years she let her body be exploited for the transportational needs of another. The witch loved music and taught Rapunzel to sing. They passed many long hours singing together in the tower.

One day a young prince rode near the tower and heard Rapunzel singing. But as he rode closer to find the source of the lovely sound, he spied the witch and hid himself and his equine companion in the trees. He watched as the witch called out to Rapunzel, the hair fell down, and the witch climbed up. Again, he heard the beautiful singing. Later, when the witch finally exited the tower and disappeared in the other direction, the prince came out of the woods and called up:

PRINCE: Rapunzel, Rapunzel, let down your hair, that I might climb your golden stair.

NARRATOR: The hair cascaded from the window, and he climbed up. When the prince saw Rapunzel, her greater-than-average physical attractiveness and her long, luxurious hair led him to think, in a typically look-ist way, that her personality would also be beautiful. (This is not to imply that all princes judge people solely on their appearance, nor to deny this particular prince his right to make such assumptions.)

PRINCE: Oh, beautiful damsel, I heard you singing as I rode by on my horse. Please sing for me again.

NARRATOR: Rapunzel didn't know what to make of this person, since she had never seen a man up close before. He seemed a strange creature – large, hairy in the face, and possessing a strong, musky odor. For reasons she could not explain, Rapunzel found this combination somewhat attractive and opened her mouth to sing.

WITCH: Stop right there!

NARRATOR: The witch had returned!

RAPUNZEL: How. . . how did you get up here?

WITCH: (matter-of-factly) I had an extra set of hair made, in case of emergency. And this certainly looks like one. Listen to me, Prince! I built this tower to keep Rapunzel away from men like you. I taught her to sing, training her voice for years. She'll stay here and sing for no one but me, because I am the only one who truly loves her.

PRINCE: We can talk about your codependency problems later. But first let me hear . . . Rapunzel, is it? . . . let me hear Rapunzel sing.

WITCH: NO! I'm going to throw you from the tower into the thorn-of-color bushes below so that your eyes will be gouged out and you'll wander the countryside cursing your bad luck for the rest of your life!

PRINCE: You may want to reconsider that. I have some friends in the recording industry, you see, who would be very interested in . . . Rapunzel, wasn't it? Different, kind of catchy, I suppose . . .

WITCH: I knew it! You want to take her from me!

PRINCE: No, no, I want you to continue to train her, to nurture her. . . as her manager. Then, when the time is right, say a week or two, you can unleash her talent on the world and we can all rake in the cash.

NARRATOR: The witch paused for a second to think about this, and her demeanor visibly softened. She and the prince began to discuss record contracts and video deals, as well as possible marketing ideas, including life-like Rapunzel dolls with their very own miniature stereo Tune-Towers.

As Rapunzel watched, her suspicions turned into revulsion. For years, her hair had been exploited for the transportational needs of others. Now they wanted to exploit her voice as well.

RAPUNZEL: (sighing) So, rapaciousness does not depend solely on gender.

NARRATOR: Rapunzel edged her way to the window without being seen. She stepped out and climbed down the second set of hair to the prince's waiting horse. She dislodged the hair and took it with her as she rode off leaving the witch and the prince to argue about royalties and percentages in their phallus-shaped tower.

Rapunzel rode to the city and rented a room in a building that had real stairs. She later established the non-profit Foundation for the Free Proliferation of Music and cut off her hair for a fund-raising auction. She sang for free in coffee houses and art galleries for the rest of her days, always refusing to exploit for money other people's desires to hear her sing.
```

---

## IC-2112: Red Card

- Title: Red Card
- Author (byline): S.L. Gilbow
- Work: Brave New Worlds – Dystopian Stories (Pgs 11-22)
- Publisher: Night Shade Books
- Publication date as stated: Dec 2012
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, ANDREWS, BLANCHARD, OFFICER, LINDA, SARAH, MILES, BARRY GILES
- Teaser before the introduction: Yes
- Spoken words (computed): 1139
- Already set (do not supply): none

### Source block (context only)

```text
Author: S.L. Gilbow
Book: Brave New Worlds – Dystopian Stories (Pgs 11-22)
ISBN: 978-1597804547
Publisher: Night Shade Books
Date (Month/Year): Dec 2012
```

### Introduction (context only: never use it for content warnings)

```text
Welcome to the future. In an effort to curb uncontrolled violence and a drastic rise of murder, America has outlawed all weapons. Well, almost all . . .

In this dystopian future, our government has chosen to issue

(at random) special cards. Red cards. Along with each of these cards comes a government issued handgun. The red card holder has a single use permit to kill any one person, at any time, for any reason with full immunity from prosecution.

And Linda Jackson holds a . . . Red Card by S.L. Gilbow
```

### Performance text (classify this)

```text
NARRATOR: (Pg 11-22) Late one April evening, Linda Jackson pulled a revolver from her purse and shot her husband through a large mustard stain in the center of his T-shirt. The official after incident survey concluded that almost all of Merry Valley approved of the shooting. Sixty-four percent of the townspeople even rated her target selection as “excellent.”

ANDREWS: He never seemed to have a good word to say about anybody.

BLANCHARD: Excellent use of a bullet. Most overbearing person I’ve ever met. He deserved what he got.

NARRATOR: Linda knew what to do after shooting Larry. She had read The Enforcement Handbook from cover to cover six times. So, after she shot her husband, Linda returned the revolver to her purse, picked up the telephone and dialed a number from a yellow sticker plastered across the phone.

OFFICER: Merry Valley Police Department.

LINDA: (matter of fact) The Enforcement Handbook says I’m supposed to call you. I’ve just shot someone.

OFFICER: That’s right. Who did you shoot? And how many times?

LINDA: My husband. Once.

OFFICER: I’d recommend you shoot him one more time just to be sure.

NARRATOR: The Enforcement Handbook recommended at least two shots, but the first shot hadn’t been easy, in spite of what the handbook said.

OFFICER: Fine then, but you’ll need to come down to the station to fill out the paperwork.

LINDA: Do I need to call someone to pick him up?

OFFICER: We’ll take care of that. Just come down to the station and don’t forget to bring your red card. And any spare ammunition you didn’t use. We can reissue it with the card.

NARRATOR: Linda hung up, set the phone on the floor, and went to her bedroom. She scanned her closet and finally settled on a lavender dress and a matching pair of high heeled shoes. Linda wasn’t sure who might be at the police station, but crowds had a way of forming, and she wanted to be presentable.

LINDA: Damn it, Larry, I gave you fair warning.

NARRATOR: Linda stepped into the dark night. The porch light on Sarah Hall’s house across the street blazed like a beacon. Sarah gave a friendly wave. Linda liked Sarah and believed Sarah liked her too. She liked her sisterly advice. Often Linda would call Sarah when Larry acted up. As the taxi pulled over, Sarah dashed across the street, opened the taxi door and slid into the back seat; she waved for Linda to join her.

SARAH: (excited) Why did you shoot him?

NARRATOR: Linda wanted to cry. The handbook had mentioned this—Shooter’s Regret. It will pass, the handbook stated, just trust your decision, trust your instincts.

SARAH: When I was young, I used to drive around with my cousin. He would yell at people all the time -- for going too slow, for going too fast, for cutting him off. I wasn’t surprised when he used a red card. The same week he got it, in fact.

LINDA: How’d you know I used a red card?

SARAH: I heard it on the radio. There’s nothing as exciting as one of the cards being used.

NARRATOR: By the time Linda and Sarah arrived at the police station, a small crowd had already gathered.

MILES: (cheering) Way to go! Killed by a librarian with a red card. That’s got to be embarrassing.

BARRY GILES: (reporting with microphone in hand) How did it happen, Mrs. Jackson?

NARRATOR: Officer Hamilton was waiting for Linda. She reached into her purse and pulled out the government-issued revolver and the red card. The card didn’t seem special. It was small, half the size of a postcard, with rounded corners. The one mark on it was an ordinary bar code. Officer Hamilton slid the card under an electronic reader, confirmed its authenticity, and led Linda to a small, secluded room in the back of the station.

LINDA: This is the hard part, isn’t it?

OFFICER: There’s no hard part. It’s all easy. (putting on his glasses. He begins the paperwork) Marital Status?

LINDA: Widowed.

OFFICER: (chuckles) Oh yes, that‘s kind of why we’re here, isn’t it. Why did you execute the enforcement?

LINDA: I think the real question should be why didn’t I do it sooner.

OFFICER: Why didn’t you? You’ve had the red card for almost four years.

LINDA: I didn’t want to use it because then I wouldn‘t have one. Sometimes he would egg me on, dare me to use it.

OFFICER: (shocked) He knew you had a red card? (shrugs) Just answer honestly. You have nothing to worry about. You performed an enforcement while in possession of a valid red card. It’s that simple. These questions are just to help us improve the program.

LINDA: He knew. He’s known for years. Is that alright? Am I in trouble?

OFFICER: Well, some people view it as having an unfair advantage over other citizens. But in this case it doesn’t seem to have made a difference. Had he been drinking?

LINDA: He’d been out messing around. I think I just snapped.

OFFICER: Linda. People with red cards are allowed to snap. It’s their duty to snap. (putting down his pencil and removing his glasses) That wasn’t so bad was it? [But] a word of advice? If you ever get another red card, don’t tell anyone. The program is random and anonymous. That‘s what makes it work.

NARRATOR: Officer Hamilton released Linda. As she walked down the hall to join Sarah in the waiting area, he could hear voices.

MILES: Well, I know what I’ll do if I get the card next.

SARAH: If you get a card, let me know. You tend to live a lot longer if you know who has the cards.

MILES: She shops at my store. Always did like her.

SARAH: Sweetheart, you have to like someone who has a red card. Kind of dangerous not to.

MILES: How would I have known she had a red card?

SARAH: I knew. I’ve known it for years. I’m surprised you all didn’t know. (pausing for effect) Oh, I forgot, you all weren’t sleeping with her husband? (laughing) Well, I guess I won’t have to like her anymore.

NARRATOR: Linda listened for the conversation to continue, but it stalled. Even Sarah was silent. She joined Sarah and the others in the waiting room.

LINDA: Sarah, I’m all done now.

NARRATOR: When the taxi dropped them off at Linda‘s place well after midnight, Sarah had pretty well resolved most of Linda’s problems. She had told her how to improve her career–

SARAH: After all you can‘t stay a librarian your entire life.

NARRATOR: And she had told her how to improve her looks–

SARAH: Those bangs just have to go; they do absolutely nothing for you. Stop moping about. Tomorrow we plan Mr. Jackson’s funeral. Then we bury him, and then you get on with your life. The enforcement program is run so well.

NARRATOR: Even the blood had been cleaned up. All that remained was a small stain, barely noticeable on the other side of the room. Sarah folded onto the couch, pried her shoes off, and clicked through the television channels.

LINDA: Stay for as long you can. I’ll be with you in a moment. After I change.

(she closes the door to her bedroom softly, kicks off her shoes, folds her hands over her face, and quietly in distress – a beat, then she renews her resolve – she reaches for a shoe box, opens it slowly and pulls out a red card and a small revolver. She clears her throat and as she steels herself for what is to come, she calls out to Sarah but this time with a clear double meaning)

Sarah, I’m all done now.
```

---

## IC-2113: The Rematch

- Title: The Rematch
- Author (byline): B.J. Novak
- Work: One More Thing: Stories and Other Stories
- Publisher: Vintage Contemporaries
- Publication date as stated: Feb 2015
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1405
- Already set (do not supply): none

### Source block (context only)

```text
Author: B.J. Novak
Book: One More Thing: Stories and Other Stories
ISBN: 978-0804169783
Publisher: Vintage Contemporaries
Date (Month/Year): Feb 2015
```

### Introduction (context only: never use it for content warnings)

```text
(In the style of a news commentator) THIS JUST IN: The infamous story of the Tortoise and the Hare is a classic tale that most people have heard before. But today we have a follow-up story that you simply do not want to miss! After losing and being utterly humiliated, the Hare has decided to challenge the Tortoise to a rematch. You heard it here first, folks: The Rematch by B.J. Novak
```

### Performance text (classify this)

```text
In the aftermath of an athletic humiliation on an unprecedented scale—a loss to a tortoise in a footrace so staggering that, his tormenters teased, it would not only live on in the record books, but would transcend sport itself, and be taught to children around the world in textbooks and bedtime stories for centuries; that hundreds of years from now, children who had never heard of a “tortoise” would learn that it was basically a fancy type of turtle from hearing about this very race— the hare retreated, understandably, into a substantial period of depression and self-doubt.

The hare gained weight, then lost weight; turned to religion, then another less specific religion. The hare got into yoga; shut himself indoors on a self-imposed program to read all the world’s great novels; then traveled the world; then did some volunteer work. Everything helped a little bit, at first; but nothing really helped. After a while, the hare realized what the simplest part of him had known from the beginning: he was going to have to rematch the tortoise.

“No, ” came the word from the tortoise’s spokesperson. “The tortoise prefers to focus on the future, not relive the past. The tortoise is focused full-time on inspiring a new generation with the lessons of dedication and persistence through his popular speaking tours and his charitable work with the Slow and Steady Foundation.”

The smugness and sanctimony of the tortoise’s response infuriated the hare. “The lessons of dedication and persistence”? Had everyone forgotten that the hare had taken six naps throughout the race (!) -- unequivocally guaranteeing victory to anyone—a horse, a dog, a worm, a leaf, depending on the wind—anyone lucky enough to be matched against the hare at this reckless, perspectiveless, and now-forever-lost peak phase of his career, an offensive period of his own life that he had obsessed about and tried in vain to forgive himself for ever since? How could anyone think the tortoise was relevant to any of this? A minor detail of the race, known to few but obsessives (of which there were still plenty), was that there had been a gnat clinging to the leg of the tortoise throughout the entire contest: was this gnat, too, worthy of being celebrated as a hero, full of counterlogical lessons and nonsensical insight like “Right place, right time takes down talent in its prime”? Or “Hang on to a tortoise’s leg, who knows where it will lead”?

No—the lesson of this story has nothing to do with the tortoise, thought the hare, and everything to do with the hare. How he had let himself become so intoxicated with the aspects of his talent that were rare that he had neglected the much more common aspects of his character that also, it so happened, were more important—things like always doing your best, and never taking success for granted, and keeping enough pride burning inside to fuel your success but not so much to burn it down. Now, the hare knew these things. Now. Now that it was too late.

Or was it? What was that lesson again? Slow and steady?

The hare started running again, every day, even though there was no race planned. He ran a mile every morning, then two, then ten.

Before long, he added an afternoon run to his training routine—a slower one, with a different goal in mind. On this run, he made a point to start a conversation with everyone he came across. “Boy, I sure would love to race that tortoise again someday. You think anyone would want to watch it, though?” Then he would shrug it off and jog along to the next stranger. “Hey, what do you think would happen if I raced that tortoise again? Ya think I’d win this time? Or do you think pride would get the better of me all over again?”

Then he’d shrug and run off again, at a provocatively medium pace.

Slowly, steadily, anticipation built for a tortoise-hare rematch. After a while it became all that anyone could talk about, and eventually, the questions made their way to the tortoise.

“No, ” said the tortoise, but this time his “no” just led to more questions. “No” now, or “no” ever? Would he ever rematch the hare? If so, when, and under what conditions? If not, why? Could he at least say “maybe”?

No, said the tortoise again; never. They kept asking, and he kept saying no, until eventually, everyone gave up and stopped asking. And that’s when the tortoise, sad and dizzy at having all this attention given to him and then taken away, impulsively said, Yes, okay, I bet I can beat this hare again. Yes.

I’m undefeated against the hare, thought the tortoise. Actually, I’m 1–0—I’m undefeated in my entire racing career! How do you win a race? Slow and steady, that’s what they say, right? Well, I invented slow and steady. This is good. This will be good. One time could have been a fluke. Twice, there’ll be no question.

The race was set in ten days’ time. The tortoise set out to replicate what seemed to have worked the first time, which was nothing in particular: simple diet, some walking around. A little of this, a little of that. He didn’t want to overthink it. He was going to mainly just focus on being slow and steady.

The hare trained like no one had ever trained for anything. He ran fifteen miles every morning and fifteen every afternoon. He watched tapes of his old races. He slept eight hours every night, which is practically unheard of for a hare, and he did it all under a wall taped full of the mean, vicious things everyone had said about him in all the years since the legendary race that had ruined his life.

On the day of the race, the tortoise and hare met for the first time in five years at the starting line, and shared a brief, private conversation as their whole world watched.

“Good luck, hare, ” said the tortoise, as casual as ever. “Whoa! You know what’s funny—do that again—huh, from this angle you look like a duck. Now you look like a hare again. Funny. Anyway, good luck, hare!”

“And good luck to you, tortoise, ” whispered the hare, leaning in close. “And just so you know— nobody knows this, and if you tell anyone I said it, I’ll deny it— but I’m not really a hare. I’m a rabbit.”

This wasn’t true—the hare just said it to *mess* with him.

“On your mark, get set, GO!”

There was a loud bang, and the tortoise and hare both took off from the starting line.

Never, in the history of competition—athletic or otherwise, human or otherwise, mythical or otherwise— has anyone ever kicked anyone’s *butt* by the order of magnitude that the hare kicked the *butt* of that tortoise that afternoon.

Within seconds, the hare was in the lead by hundreds of yards. Within minutes, the hare had taken the lead by more than a mile. The tortoise crawled on, slow and steady, but as he became anxious at having lost sight of his competitor and panicked over what he seemed to have done to his legacy, he started speeding up: less slow, less steady. But it hardly mattered. Before long—less than twenty minutes after the seven-mile race had begun —word worked its way back to the beginning of the race that the hare had not only won the contest, and had not only recorded a time that was a personal best, but had also set world records not only for all hares but also for leporids and indeed for all mammals under twenty pounds. When news reached the tortoise, still essentially under the banner of the starting line, he fainted. “Oh, now he’s napping?! Isn’t that rich, ” heckled a nearby goat, drunk on radish wine.

Those who didn’t know the context—who hadn’t heard about the first race —never realized what was so important about this one. “A tortoise raced a hare, and the hare won? Okay.” They didn’t understand the story, so they didn’t repeat it, and it never became known. But those who were there for both contests knew what was so special about what they had witnessed: slow and steady wins the race, till truth and talent claim their place.
```

---

## IC-2114: Richard

- Title: Richard
- Author (byline): Allie Brosh
- Work: Solutions and Other Problems, Pg 15
- Publisher: Gallery Books
- Publication date as stated: Gallery Books
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MOM, RICHARD, NARRTOR, DAD
- Teaser before the introduction: Yes
- Spoken words (computed): 1327
- Already set (do not supply): none

### Source block (context only)

```text
Author: Allie Brosh
Book: Solutions and Other Problems, Pg 15
ISBN: 978-1982156947
Publisher: Gallery Books
Date (Month/Year): Gallery Books
```

### Introduction (context only: never use it for content warnings)

```text
Let's face it: kids are total suckers. When we were young, we believed a lot of crazy things.

• If you swallow watermelon seeds, an entire

watermelon will grow inside you.

• Quicksand is everywhere, and you have to be

constantly vigilant for it.

• Sharks are lurking in the deep end of every

swimming pool. (beat)

• A person lives next to us!

Yup . . . just part of being a kid. As we tried to make sense of the world, our imaginations often got the better of us. But in this selection imagination becomes action – weird, weird action!

Richard by Allie Brosh
```

### Performance text (classify this)

```text
NARRATOR: (Pg 15+) People: Where do they live? Us – Our House; Other People – Remote mystery houses that your mom drives you to.

For the first few years of my life, the only people I knew how to find lived in my house. We had a neighbor, Richard. But Richard was quiet and rarely outside for long, so I didn't know about him. One afternoon, though, Richard went outside. That's how I found out about him. I just saw him. He probably didn't even know. He stood in his driveway for a minute or two and then went back into his house. But I saw him.

It was very exciting. A person lives next to us! A person! He lives right there! And I SAW him! When will he go outside again? What else does he do? Does he know about dad? Who is his friend? Does he like whales? Is his house the same as ours? Carpet – Could be brown like ours but could also be blue! Blue carpet! What if his walls are blue too? What if he has a different couch? Which room does his grandma live in? – Maybe [she] lives in the bathroom . . . Who knows what all the possibilities are!

NARRATOR: Desperate to catch another glimpse of him, I'd lurk near the windows all day just staring at his house. I think I expected it go somewhere. You can't find out there's a person living right next to you and then never get any answers. Maybe if you're 100 and you know everybody, but not if you're 3. Not when it's the first stranger you know how to find. I just wanted to know more. Anything.

And the whole thing could have ended right here folks . . . and NOBODY would get any answers about Richard . . . if it wasn't for the dog door.

My grandma usually supervised me while my parents were at work. “Supervised” - If she hadn't seen me in a while, she'd check to make sure I still had all my fingers, but escaping wasn't a big concern. The doors were locked . . . but the dog door was the weak point in the fortress. I'd sneak out through the dog door and go stare at his house from the edge of our driveway, hoping this would summon him. When it didn't, I'd sneak a little closer. Maybe it'll work if I stand in Richard's driveway . . . or maybe I'll just go over to this little window . . .

I started sneaking out more frequently. I started sneaking out at night. And the fact that I was sneaking seems to suggest I might've been at least partially aware that this type of behavior should be a secret, but I don't think I'd reached that crucial developmental turning point where you're capable of recognizing how creepy you're being.

However, on the night I found the cat door in Richard's garage, even my undeveloped, fish-level brain could sense that a boundary was about to be crossed. A tiny, instinctual trace of doubt—This might be too weird of a thing to do . . . Of course, one of the main features of undeveloped, fish-level brains is poor impulse control, and before I could complete the thought, I was in Richard's living room.

Here I am . . . I did it . . . Wowee!!! I hadn't prepared for this possibility. I'd dreamed of it, sure. But I wasn't expecting it to HAPPEN.

A concrete objective never emerged, but the missions became bolder and more frequent. I started bringing things back with me. Richard's things. They seemed valuable, somehow. A nonsensical collection of Richard's possessions slowly accumulated at the back of my toy drawer. This would prove to be my downfall.

Long before that, though, my mom noticed that I'd mysteriously disappear sometimes. She wasn't worried yet because she didn't think I knew how to get out of the house, but one day she asked me where I'd been. And I said: "Hanging out with Richard."

"Hanging out" was a misnomer—Richard had been hanging out by himself and I had been standing in his hallway just out of view—but this was concerning news for my parents. They didn't even know that I knew Richard, let alone that we'd been "hanging out." They went over and knocked on Richard's door and asked him about it. And Richard, who was still somehow unaware of all the hanging out we'd been doing, told them he didn't know anything about that.

MOM: So you’ve never seen this kid before . . .

RICHARD: No, I mean . . . seen? Yeah. But not . . it wasn’t . . just in the yard and stuff.

NARRATOR: I imagine things were tense for a bit. But the clues piled up. I couldn't control myself. I took more things, bigger things. I also branched over into hiding things for Richard to find. Pretty rocks, pieces of string, letters I'd tried to write. At that age, I didn't know how to spell very many words, so the messages were fairly cryptic: the entire alphabet, followed by the word Mom and a drawing of the sun. Rampant scribbling. It must've come off like being haunted by a defective but well-meaning ghost.

The connection should have been obvious. But, when faced with a mystery like, "Where did my remote control go? Why is there a piece of paper with a child's handwriting on it hiding in the VCR? And how do these rocks keep getting in here?" almost no rational adult would jump to the conclusion "because a child has been sneaking in through my cat door and leaving these for me to discover." Not even with clues. I don't know what theory Richard came up with to explain it . . .

RICHARD: POSSIBLE THEORIES – (1) These things have always been here and I never noticed them; (2) Paranormal activity; (3) I have a very proactive form of epilepsy, and this is what I do while I am having a seizure.

NARRTOR: The thing that finally blew my cover was stealing Richard's cat. Stealing it wasn't the original plan. The opportunity presented itself, I seized it. It was a strong animal. Getting it into the drawer was difficult. It lived in the drawer for a while. I don't know how long. Hours, probably . . . And now it is time for a quick fact about cats: cats aren't good secrets, because, under extreme duress, they have the ability to make a sound like: YAOAOAOAOAOAOAOAOAOAOAOAOAOAOAOAOA OAOAOAO My parents eventually realized the sound was coming from inside the house and located the source of it. They weren't expecting to find quite so many of Richard's things.

I don't know if they put the pieces together immediately or processed them individually as they came up—

MOM: First of all, there's a cat in this drawer; How about that.

DAD: There appear to be a considerable number of objects under the cat. This one is a shoe.

MOM: This one is a piece of bread.

DAD: This one is a credit card bill. Huh . . . it's addressed to 'Richard The Neighbor . . .

NARRATOR: [They were] inching closer to the truth with every clue until the ultimate answer to "What does 'hanging out with Richard' mean?" was revealed. There was more than enough evidence to answer the question. That's got to be a strange moment for a parent. There's this omnipresent fear of predators and monsters, and you just . . . you never quite expect to find out the monster is your kid. There's no Hallmark card for "Sorry we accused you of being a molester; we didn't realize our kid was sneaking into your house and stealing your spoons and animals and watching you while you sleep. We're really, really sorry."

Looking at the objects, and the freaked-out cat, and my parents' confused faces, I realized that yeah, maybe this had been a weird thing to do . . . I felt like I should explain why I had done this, but I didn't know either. So we all just stood there, feeling weird about ourselves and each other. (awkward beat) The cat was stoked to be free, though.

And Richard was (and probably still is) a very kind man.
```

---

## IC-2115: Romeo and Juliet vs. Mrs. Jackson’s Seventh Grade English Class

- Title: Romeo and Juliet vs. Mrs. Jackson’s Seventh Grade English Class
- Author (byline): Ethan Anderson
- Work: May Contain Nuts: A Very Loose Canon of American Humor
- Publisher: Harper Collins
- Publication date as stated: 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 735
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ethan Anderson
Book: May Contain Nuts: A Very Loose Canon of
American Humor
ISBN: 978-0060516260
Publisher: Harper Collins
Date (Month/Year): 2004
```

### Introduction (context only: never use it for content warnings)

```text
Why do they teach Romeo and Juliet in seventh grade? When boys turn 13? When Romeo and Juliet are medieval seventh-graders? When they make love once and kill themselves? What are they thinking? The thoughts of a 7th-grade boy girl studying . . . Romeo and Juliet vs. Mrs. Jackson’s Seventh Grade English Class By Ethan Anderson
```

### Performance text (classify this)

```text
The Average Boy Sitting Behing Suzy Warner in Mrs. Jackson’s Class:

One, Suzy Warner is incredibly hot.
Two, no one is hotter than Suzy Warner.
Three, I’m hungry.
Four, last year I was a kickball superstar.
Five, this year I am a virgin.
Sis, Suzy Warner is incredibly hot.

Seven, there’s a muffled noise coming from the front of
the room.
Eight, the muffled noise is Mrs. Jackson, trying to
teach.
Nine, Mrs. Jackson is incredibly hot..
Ten, Suzy Warner beats Juliet
any century, any day of the week.
Eleven, how hot would Suzy Warner look in the 14th
century?
Twelve, the correct answer is crazy 14th-century hot.
Thirteen, let’s say I’m Romeo
And Suzy Warner not only does it with me,
But then she tells me she wants to do it AGAIN the
next day.
Fourteen, gaphphnuggungh, my brain has imploded.
Fifteen, I didn’t think it was possible to be this hungry.
Sixteen, according to Shakespeare,
The day after I do it with Suzy Warner,
I’m across town lying dead in a crept.
Seventeen, NO WAY that happens in real life, okay?

Because One, if I’m Romeo,
That means I’m not a virgin anymore,
WHICH IS AWESOME.
And because Two, if Suzy Warner’s in bed with me,
No way I’m leaving bed, EVER.
I would never get out of bed.
There is no upside to leaving bed.
Skittles, skateboarding, food and water --
things of the past, my friend.
Let’s assume for some totally unbelievable hypothetical
reason
that I leave Suzy Warner in bed.
Let’s suppose later that day
one of Suzy Warner’s relatives
kills my best friend Mercutio.
On one hand, I hate that dude.
On the other hand,
I know Suzy Warner
WANTS IT AGAIN, FROM ME, TONIGHT.

So let’s review.

Either I avenge my best friend, who is tragically dead.
Or I sleep with Suzy Warner, who is totally hot.
Door number one,
Avenge friend’s death, return to kickball.
Door number two,
SUZY WARNER.
In conclusion, Shakespeare, total idiot.
Class dismissed.
And if I don’t get Cheetos in the next five minutes,
I will pass out and die.

Suzy Warner

One, Mrs. Jackson is my favorite teacher and
Romeo and Juliet is not just a great play
It is also an incredible movie.
Two, in the movie Leonardo DiCaprio played Romeo
And he is an amazing actor.
Three, the only movie I have seen more times than
Romeo and Juliet is Titanic,
Starring Leonardo DiCaprio.
Four, you should be allowed to drink Diet Coke in English
class.
Five, Leonardo DiCaprio is o amazing in Titanic
that I almost forgot the ending every time. I swear.
Six, my other favorite movie
Behind Titanic and Romeo and Juliet
Is The Beach, starring Leonardo DiCaprio.
Seven, I haven’t seen What’s Eating Gilbert Grape yet,
But I want to.
It stars Leonardo DiCaprio and Johnny Depp,
Who is also an amazing actor.
Eight, I could not believe how incredibly much
Johnny Depp loved Winona Ryder
in Edward Scissorhands. They were like unicorns.
Nine, if I were Juliet
That would mean I would be married to Leonardo
DiCaprio.
Ten, if I were married to Leonardo Di Caprio
we would have houses in Hollywood and Europe and
Florida
That my friends could visit any time
And I would have my own successful business
And I would still write in my journal
When Leonardo is out making movies
And I would decorate one of the houses entirely in Kelly
green,
Which is an amazing color.
Eleven, if I were married to Leonardo DiCaprio
And he was Romeo,
And I woke up and I saw that he had killed himself
because he thought I was dead even though I wasn’t,
I would definitely do what Juliet did,
Which is incredibly sad, but I definitely would.
Twelve, I would definitely NOT EVER do what Juliet did
for any boy in my class.
NOT IN A BILLION YEARS.
Thirteen, I know Leonardo is fat now, but I don’t care.
In conclusion, Shakespeare is an amazing writer,
And it makes me sad that there are no boys in my class
Who are anything like Leonardo DiCaprio.

Mrs. Jackson

One, if Suzy Warner calls Romeo “Leonardo” one more time, I will kill her and lose my pension. Two, you should be allowed to drink Diet Coke in English class. And three, what’s that boy behind Suzy thinking? He’s not even in this class.
```

---

## IC-2116: Rosa Parks

- Title: Rosa Parks
- Author (byline): Kai Friese
- Work: Not specified
- Publisher: Demco Media
- Publication date as stated: January, 1990
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1158
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kai Friese
ISBN: 978-0606047852
Publisher: Demco Media
Date (Month/Year): January, 1990
```

### Introduction (context only: never use it for content warnings)

```text
When Rosa Parks refused to give up her seat on a bus, it led to one of the most important chapters in the story of civil rights in America. Parks’ courage led to profound change for African Americans. In 1998 Parks was recognized with the first International Freedom Conductor Award given by the National Underground Railroad Freedom Center. President Bill Clinton awarded Parks the Congressional Gold Medal, the nation's highest civilian honor, in July 1999. This is the story of Rosa Parks by Kai Friese
```

### Performance text (classify this)

```text
It was Thursday, December 1, 1955. The workday was over, and crowds of people boarded the green and white buses that trundled through the streets of Montgomery. Rosa Parks was tired after a full day of stitching and ironing shirts at the Montgomery Fair department store. She thought she was lucky to have gotten one of the last seats in the rear section of the Cleveland Avenue bus that would take her home.

Soon the back of the bus was full, and several people were standing in the rear. The bus rolled on through Court Square, where African Americans had been auctioned off during the days of the Confederacy, and came to a stop in front of the Empire Theater. The next passenger aboard stood in the front of an aisle. He was a white man.

When he noticed that a white person had to stand, the bus driver, James F. Blake, called out to the four black people who were sitting just behind the white section. He said they would have to give up their seats for the new passenger. No one stood up. “You’d better make it light on yourself and let me have those seats,” the driver said threateningly. Three men got up and went to stand at the back of the bus. But Rosa Parks wasn’t about to move. She had been in this situation before, and she had always given up her seat. She had always felt insulted by the experience. “It meant that I didn’t have a right to do anything but get on the bus, give them my fare, and then be pushed around wherever they wanted me,” she said.

By a quirk of fate, the driver of the bus on this December evening was the same James F. Blake who had once before removed the troublesome Rosa Parks from his bus for refusing to enter by the back door. That was a long time ago, in 1943. Rosa Parks didn’t feel like being pushed around again. She told the driver that she wasn’t in the white section and she wasn’t going to move . Blake knew the rules, though. He knew that the white section was wherever the driver said it was. If more white passengers got on the bus, he could stretch the white section to the back of the bus and make all the blacks stand. He shouted to Rosa Parks to move to the back of the bus. She wasn’t impressed. She told him again that she wasn’t moving. Everyone in the bus was silent, wondering what would happen next. Finally Blake told Rosa Parks that he would have her arrested for violating the racial segregation codes. In a firm but quiet voice, she told him that he could do what he wanted to do because she wasn’t moving.

Blake got off the bus and came back with an officer of the Montgomery Police Department. As the officer placed Rosa Parks under arrest, she asked him plainly, “Why do you people push us around?”

With the eyes of all the passengers on him, the officer could only answer in confusion. “I don’t know. I’m just obeying the law,” he said.

Rosa Parks was taken to the police station, where she was booked and fingerprinted. While the policemen were filling out forms, she asked if she could have a drink of water. She was told that the drinking fountain in the station was for whites only. Then a policewoman marched her into a long corridor facing a wall of iron bars. A barred door slid open. She went inside. The door clanged shut, and she was locked in. She was in jail.

Rosa Parks’ decision to challenge her arrest in court led Montgomery’s black community to organize a bus boycott as a show of solidarity.

Rosa Parks woke up on the morning of Monday, December 5, thinking about her trial. As she and her husband got out of bed, they heard the familiar sound of a City Lines bus pulling up to a stop across the road. There was usually a crowd of people waiting for the bus at this time. The Parkses rushed to the window and looked out. Except for the driver, the bus was empty and there was no one getting on either. The bus stood at the stop for more than a minute, puffing exhaust smoke into the cold December air as the puzzled driver waited for passengers. But no one appeared, and the empty bus chugged away.

Rosa Parks was filled with happiness. Her neighbors were actually boycotting the buses. She couldn’t wait to drive to the courthouse so that she could see how the boycott was going in the rest of Montgomery. When Fred Gray arrived to drive her to the trial, she wasn’t disappointed. Rosa Parks had expected some people to stay off the buses. She thought that with luck, maybe even half the usual passengers would stay off. But these buses were just plain empty.

All over the city, empty buses bounced around for everyone to see. There was never more than the usual small group of white passengers in front and sometimes a lonely black passenger in back, wondering what was going on. The streets were filled with black people walking to work.

As Rosa Parks and her lawyer drove up to the courthouse, there was another surprise waiting for them. A crowd of about five hundred blacks had gathered to show their support for her. Mrs. Parks and the lawyer made their way slowly through the cheering crowd into the courthouse. Once they were inside, the trial didn’t take long. Rosa Parks was quickly convicted of breaking the bus segregation laws and fined ten dollars, as well as four dollars for the cost of her trial.

This was the stage at which Claudette Colvin’s trial had ended seven months earlier. Colvin had had little choice but to accept the guilty verdict and pay the fine. This time, however, Fred Gray rose to file an appeal on Rosa Parks’ case. This meant that her case would be taken to a higher court at a later date. Meanwhile Mrs. Parks was free to go.

Outside the courthouse, the crowd was getting restless. Some of them were carrying sawed-off shotguns, and the policemen were beginning to look worried. E. D. Nixon went out to calm them, but nobody could hear him in the din. Voices from the crowd shouted out that they would storm the courthouse if Rosa Parks didn’t come out safely within a few minutes. When she did appear, a great cheer went up again.

After seeing the empty buses that morning, and this large and fearless crowd around her now, Rosa Parks knew that she had made the right decision. Black people were uniting to show the city administration that they were tired of the insults of segregation. Together, they could change Montgomery. They could do some good.
```

---

## IC-2117: Sacrifice

- Title: Sacrifice
- Author (byline): Macey Baggett Wuesthoff
- Work: Not specified
- Publisher: Amber Quill Press
- Publication date as stated: July 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1887
- Already set (do not supply): none

### Source block (context only)

```text
Author: Macey Baggett Wuesthoff
ISBN: 978-0027474701
Publisher: Amber Quill Press
Date(Month/Year): July 2004
```

### Introduction (context only: never use it for content warnings)

```text
This is the story of how the town of Grimshaw sold its soul to the Devil. What happened in Grimshaw could have happened—and still could happen—in virtually any small American town. Yet it happened in Grimshaw perhaps because the town was enduring extreme hardship at the time, which naturally causes weakness in man. Sacrifice by Macey Baggett Wuesthoff
```

### Performance text (classify this)

```text
A deep recession was sweeping the United States. That recession exceptionally devastated small towns like Grimshaw, which offered its peoples few industries and sources of income. The majority of the sparse sources of income in Grimshaw—factories, warehouses, restaurants, cafés, and various mom-and-pop businesses—closed their doors forever, leaving most of Grimshaw unemployed.

A rural town in the Deep South, Grimshaw was able to fall back on farming—until the recession was followed with a drought.

Grimshaw, the smallest town in the affected region, the town with the fewest businesses still open, the town that relied most heavily on farming, was the town that suffered the most. Day after day, farmers lugged buckets of water to their thirsty fields, only to have their crops mock them by withering and browning into premature deaths.

Weeks extended into months. The drought and the recession went on…and on…and on…

With no end in sight to the tribulations, with the businesses gone, the land dying, and money and even food scarce, Grimshaw’s population began to die out along with the economy and crops. Some of those who lived through it moved, a few abandoning their homes and property. Others couldn’t leave due to lack of education, finances, personal strength, or various other inhibitors. Thus, they were stuck in Grimshaw to suffer and await the end of the drought, the recession, or themselves.

The hearts of those left in Grimshaw overflowed with dark, bitter pain. They were starving. They were thirsty. They were weary. They were angry. Most of all, they were desperate.

The most desperate among them was a farmer named John Weekly. Nine years before, when John and his high school sweetheart Gay were seventeen, they had dropped out of school to get married. Over the next seven years, they had three children. Together, the family lived a life that was humble yet full of love and happiness. That love and happiness ended during the latter part of John and Gay’s eighth year of marriage, when Gay died due to complications in childbirth. Gay had given birth to twin boys. That left John the widowed father of five at only twenty-five years old. Just weeks after Gay’s death came the recession, followed by the drought. The factory where John worked closed, and the crops on his farm began to die. As a single parent, John found it harder and harder to care physically and financially for his children.

He had no living relatives to help him, and his friends and neighbors had too many troubles of their own to offer him aid. Like his own old tractor, worn and rusted from too much weather and use, John Weekly’s spirit simply “broke down”—broke down worse than the spirit of anyone else in Grimshaw. That is probably why he was chosen.

It happened on a Friday night, when John was in the modestly furnished bedroom he had shared with Gay. It was late, so John wore his usual sleepwear of a sleeveless undershirt and boxers. He looked at his reflection in the dusty, cracked mirror of the bureau across the room and shook his head. His skin was pale and his body gaunt from lack of nourishment, for he had been eating a little less so his children could have a little more. The hard times he’d been through that year had marked him with worry lines and patches of premature gray in his thinning, brown hair. Appalled by his own reflection, he switched on his bedside lamp and switched off his overhead light, trying not to face the shell of a man he had become.

John slumped onto the bed. On the nightstand to the bed’s right were a folded piece of paper and a framed photo of Gay, smiling and beautiful, taken just before she died. John picked up Gay’s photo and poured over it longingly. God, how he missed her, how he needed her now! In a way, though, he was glad she wasn’t around to suffer through these hard times, to see how they had left him unable to support his own family. He dabbed his eyes with a handkerchief on the nightstand to stop the tears that threatened to seep through his lids.

That was it. Looking at Gay’s photo and thinking about her hurt too much. John put the picture down, picked up the piece of paper, and unfolded it. Printed across the top were the words, “Mortgage Foreclosure, Final Notice.” He shook his head again. So now he’d not only lost his wife, his job, and his crops, he was going to lose his home and land, too. Where would that leave his family?

“Daddy?”

John raised his eyes from the mortgage notice. His oldest daughter, eight-year-old Sarah, who was of age, stood gazing at him from outside the open doorway. Sarah was the only of the five children who had her late mother’s blonde hair and blue eyes, but her facial features were almost identical of John’s. John had once been quite proud of his daughter’s face being so like his own. Now, seeing that similarity hurt him, for Sarah’s countenance had recently taken on the pale, sickly color that he’d just observed in himself.

John asked, “What’re you doing up, hon’?”

“I’m hungry,” Sarah replied. “Everybody is. The twins are crying and pointing at their tummies and saying ‘hun-ry, hun-ry.’ And Gaylette and John Jr. are in my room now, saying they can’t sleep ‘cause their tummies are growling.”

“Oh,” John said distractedly, returning his attention to the mortgage notice. “There’s a loaf of bread in the breadbox.”

“Nuh-uh. That’s gone.”

“Gone?” John echoed.

“Yeah. We ate it all at dinner.”

“Any crackers in the cabinet? Fruit in the fridge? Canned soup or vegetables in the pantry?” Sarah answered each question with a shake of her head.

“There’s nothing in the house to eat.” Her features brightened with an idea. “Hey, let’s get some vegetables out of the garden!”

John shook his head sadly. “There ain’t none. The drought’s killed the whole push of them.”

“Oh.”

An awkward silence followed. Sarah lowered her eyes in the same defeated expression that John had also observed on his own face a minute before. It pained his soul. He tried to say something comforting. “I’ll go into town tomorrow and get a few things. For now, why don’t you have a glass of water, and get one for your brothers and sister too? It’ll make y’all feel full.”

His statement had the opposite effect. Sarah contorted her features and said resentfully, “I already did. We’re still hungry!” Scowling, she pivoted and disappeared from the doorway.

John maintained his composure long enough to put the mortgage notice back on the nightstand, crawl under the covers, and switch off the lamp. But once he flipped over on his side, facing away from the door and the extinguished light, he allowed his tears to flow. He cried for his land, he cried for his children, he cried for his late wife. Mostly, though, he cried for himself.

“John.”
At first, his name was spoken so faintly, so
unexpectedly, that he assumed he had imagined it and
just kept crying.

“John,” it repeated, low and gravelly, with a hissing undertone.

The third time the voice sounded, John knew for sure it was real, because he heard it speak an entire sentence: “I can make it all better, John.”

John’s lids flew open, and he bolted upright in bed. “Who’s there?” he called, groping for switch to his bedside lamp.

The voice came again, now angry. “Don’t turn on that light!”

John dropped his hand but demanded, “Who are you?”

Calm once more, it replied, “I am known by various names. The Prince of Darkness, the Antichrist, Lucifer, Beelzebub, Satan—”

“Aw, what a load of crap!” John sputtered. He reached for the lamp a second time.

The voice became deeper, louder, and more forceful than before. “I said, don’t turn on that light!”

John searched the darkness. His heart began to pound. Just beyond the foot of his bed, in the corner between the bureau and the bedroom door, he saw two red eyes flashed on like lights. They glowed bright as fire. Down the middle of each eye, where a pupil should have been, there was instead a black, snake-like slit.

Now more afraid than he’d ever been in his life, John squeezed his own eyes shut so he could no longer see the bestial ones blazing back at him. He began murmuring, “Oh please, don’t hurt me, please don’t let him hurt me, Jesus—”

“Jesus?” the voice cut him off. It broke into loud, hysterical cackling. “What has He done for you lately?”

“Huh?” Awestruck, John opened his lids.

“Brought you this endless recession? Given you this drought that has killed your crops and those of your friends and neighbors? Stolen your wife and the mother of your children? Left you and your family to starve to death? Fat lot of good He’s been to you.” It paused, and then, seeing that John was listening, repeated, “I can make it all better, John. I can give you back your home, your land, your job. I can make your crops grow once more, and ensure that you and your children never go hungry again. I can make it so that you, your friends— the entire town of Grimshaw—prosper.”

It paused once more. John timidly whispered, “How?”

“Simple. I do something for you; you do something for me. I give you your lives back, and you give life back to me.”

“I don’t understand.”

“You will repay me through sacrifice.”

“Sacrifice? What sort of sacrifice?”

Sacrifices of blood.”

“You mean, like animals or somethin’?”

“Yes, sometimes goats and rams and such,” the voice replied. “Other times, I will require the sacrifice of a child.”

“WHAT?!” John cried. “We’d have to kill children?”

“Heed my words, John,” it replied. “The whole town is perishing. What difference will a few children here and there make if it will save so many others from oblivion?”

John was reaching for the bedside light yet a third time when he realized that, sadly, this sounded like a logical proposition. He hesitated. “Children from where?”

“Children from Grimshaw only, of course. It would be foolish to do otherwise. If you venture outside town for your sacrifices, you will attract more attention and likely get caught.”

John could scarcely believe the grotesque proposition that he was hearing. Nor that he was considering it. As his own stomach began to rumble, though, he heard himself ask, “Which ones? Just any of them?”

“Oh no, not just any.

Those with what some mortals have called ‘angelic features’.” Seeing that John didn’t understand, it added, “Features like those of your daughter Sarah.”

“No,” John began to shake his head. “You can’t mean you expect me to...”

“It would set a good example, a convincing example for the rest, if your own daughter were the first to be given to me.”

John clenched his hands, ready to leap off the bed and pound the demon with his fists. “You ain’t layin’ a finger on my daughter!” “No, I won’t,” it confirmed. “You will. You will sacrifice her to me.”
```

---

## IC-2118: The Scarlet Letter

- Title: The Scarlet Letter
- Author (byline): Nathaniel Hawthorne
- Work: Not specified
- Publisher: Bantam Classics
- Publication date as stated: March 1981
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: WOMAN 1, WOMAN 2, WOMAN 3, WOMAN 4, WOMAN 5, BEADLE
- Teaser before the introduction: Yes
- Spoken words (computed): 1303
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nathaniel Hawthorne
ISBN: 978-0553210095
Publisher: Bantam Classics
Date (Month/Year): March 1981
```

### Introduction (context only: never use it for content warnings)

```text
Set in colonial New England, Hester Prynne has come to Boston ahead of her husband. When she gives birth to a daughter, the time-line just doesn’t match up and it becomes obvious that she has committed adultery. The community’s response – Public Shaming.

We’ve come a long way since then . . . or have we? In an age of cyber-bullying and demagoging politicians, this practice lives on. We still live in a Scarlet Letter Society. Look at the most recent headlines: [insert your own examples here to keep this intro up to date] A President impeached as a result of alleged infidelity; A high-school student attacked for disrespecting a Native American during a protest rally in Washington DC . . . the list goes on. We don’t sew scarlet letters on the clothing of the immoral transgressors anymore. Instead we flash their images around the world from televisions and computer screens.

The Scarlet Letter by Nathaniel Hawthorne.
```

### Performance text (classify this)

```text
The grass-plot before the jail, in Prison Lane, was occupied by a large number of the inhabitants of Boston; all with their eyes intently fastened on the iron-clamped oaken door. It might be that an undutiful child, whom his parents had given over to the civil authority, was to be corrected at the whipping-post. It might be, too, that a witch, was to die upon the gallows. The women appeared to take a peculiar interest in whatever penal infliction might be expected to ensue.

WOMAN 1: Goodwives, I’ll tell ye a piece of my mind. If we women, being of mature age and church-members in good repute, should have the handling this Hester Prynne, what think ye, gossips? If the hussy stood up for judgment before would she come off with such a sentence as the magistrates have awarded? Marry, I trow not!

WOMAN 2: People say that the Reverend Dimmesdale, takes it very grievously to heart that such a scandal should have come upon his congregation.”

WOMAN 3: The magistrates are God-fearing gentlemen, but merciful overmuch—that is a truth. At the very least, they should have put the brand of a hot iron on Hester Prynne’s forehead. Little will she care what they put upon the bodice of her gown! Why, she may cover it with a brooch, or such like, and so walk the streets as brave as ever!

WOMAN 4: (softly) Ah, but, let her cover the mark as she will, the pang of it will be always in her heart.

WOMAN 5: What do we talk of marks and brands, whether on the bodice of her gown, or the flesh of her forehead? This woman has brought shame upon us all, and ought to die. Is there not law for it? Truly there is, both in the Scripture and the statute-book. Then let the magistrates, who have made it of no effect, thank themselves if their own wives and daughters go astray!

The door of the jail being flung open from within, there appeared, the grim and grisly presence of the town-beadle. Stretching forth the official staff in his left hand, he laid his right upon the shoulder of a young woman. On the threshold of the prison-door, she repelled him and stepped into the open air, as if by her own free-will. She bore in her arms a child, a baby of some three months old acquainted only with the gray twilight of a dungeon.

She took the baby on her arm, and, with a burning blush, and yet a haughty smile, and a glance that would not be abashed, looked around at her neighbors. On the breast of her gown, in fine red cloth, surrounded with an elaborate embroidery and fantastic flourishes of gold thread, appeared the letter A. It was so artistically done that it had all the effect of a fitting decoration to the apparel which she wore; a splendor greatly beyond what was allowed by the regulations of the colony.

She had dark and abundant hair, so glossy that it threw off the sunshine with a gleam, and a face which, besides being beautiful, had the impressiveness belonging to deep black eyes. Never had Hester Prynne appeared more lady-like, in the antique interpretation of the term, than as she issued from the prison. Those who had expected to behold her dimmed and obscured by a disastrous cloud, were astonished to perceive how her beauty shone out, and made a halo of the misfortune in which she was enveloped. But the point which drew all eyes, and, as it were, transfigured the wearer, was that SCARLET LETTER, so fantastically embroidered and illuminated upon her bosom. It had the effect of a spell, taking her out of the ordinary relations with humanity, and inclosing her in a sphere by herself.

WOMAN 1: She hath good skill at her needle, that’s certain, but did ever a woman, before this brazen hussy, contrive such a way of showing it! Why, gossips, what is it but to laugh in the faces of our magistrates, and make a pride out of what they meant for a punishment?”

WOMAN 2: It were well if we stripped Madam Hester’s rich gown off her dainty shoulders; and as for the red letter, which she hath stitched so curiously, I’ll bestow a rag of mine own rheumatic flannel, to make a fitter one!

WOMAN 4: (whispering) O, peace, neighbours, peace! Do not let her hear you! Not a stitch in that embroidered letter, but she has felt it in her heart.

BEADLE: (gesturing with his staff) Make way, good people, make way, in the King’s name. Open a passage. Come along, Madam Hester, and show your scarlet letter in the market-place!

A lane was forthwith opened through the crowd of spectators. And Hester Prynne set forth towards the place appointed for her punishment. A crowd of eager and curious schoolboys, understanding little of the matter in hand, except that it gave them a half-holiday, ran before her progress, turning their heads continually to stare into her face, and at the baby in her arms, and at the letter on her breast. As haughty as her demeanor was, she perchance underwent an agony from every footstep of those that thronged to see her, as if her heart had been flung into the street for them all to spurn and trample upon. With almost a serene deportment, Hester Prynne passed through this portion of her ordeal, and came to a sort of scaffold. It stood nearly beneath the eaves of Boston’s earliest church, and appeared to be a fixture there.

In fact, this scaffold constituted a portion of a penal machine – as effectual an agent in the promotion of good citizenship, as ever was the guillotine among the terrorists of France. There can be no outrage, methinks, against our common nature—whatever be the delinquencies of the individual—no outrage more flagrant than to forbid the culprit to hide his face for shame. In Hester Prynne’s instance, her sentence bore, that she should stand a certain time upon the platform. Knowing well her part, she ascended a flight of wooden steps, and was thus displayed to the surrounding multitude, at about the height of a man’s shoulders above the street.

Hester Prynne stood on the scaffold of the pillory, an infant on her arm, and the letter A, in scarlet, fantastically embroidered with gold thread, upon her bosom!

The scene was not without a mixture of awe, such as must always invest the spectacle of guilt and shame in a fellow-creature, before society shall have grown corrupt enough to smile, instead of shuddering, at it.

The Governor, and several of his counsellors, a judge, a general, and the ministers of the town; sat or stood in a balcony of the meeting-house, looking down upon the platform. The crowd was sombre and grave. The unhappy culprit sustained herself as best a woman might, under the heavy weight of a thousand unrelenting eyes, all fastened upon her. It was almost intolerable to be borne. Had a roar of laughter burst from the multitude,—each man, each woman, each little shrill-voiced child, contributing their individual parts,—Hester Prynne might have repaid them all with a bitter and disdainful smile. But, under the leaden infliction which it was her doom to endure, she felt, at moments, as if she must needs shriek out with the full power of her lungs, and cast herself from the scaffold down upon the ground, or else go mad at once.

Could it be true? She clutched the child so fiercely to her breast, that it sent forth a cry; she turned her eyes downward at the scarlet letter, and even touched it with her finger, to assure herself that the infant and the shame were real. Yes!—these were her realities.
```

---

## IC-2119: The Secret Knowledge of Grown-Ups

- Title: The Secret Knowledge of Grown-Ups
- Author (byline): David Wisniewski
- Work: Not specified
- Publisher: Harper Collins
- Publication date as stated: July 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1282
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Wisniewski
ISBN: 978-0064437530
Publisher: Harper Collins
Date (Month/Year): July 2001
```

### Introduction (context only: never use it for content warnings)

```text
The Secret Knowledge of Grown-Ups by David Wisniewski
```

### Performance text (classify this)

```text
NARRATOR: (Pg 8-9) The truth must be told to kids! For too long, for centuries in fact, it’s been covered over, hidden, impossible to find. A conspiracy, an organized silence by generations of grown-ups, has kept the truth from millions of children.

And what is this truth, you ask. Simply this: The reasons grown-ups tell you to do things are not true!

Eat your vegetables, they say. They’re good for you. NONSENSE!

Comb your hair, they say. It keeps it neat. POPPYCOCK!

There are far more sinister, truly macabre reasons for these seemingly innocent requests. Over the last three years, I’ve gathered as much information as I could: crisscrossing the country in clever, impenetrable disguises . . .Breaking into the secret files kept by hundreds of grown-ups . . . Assembling the evidence. And now . . . the truth!

NARRATOR: (Pg 11-15) GROWN-UP RULE #31: Eat Your Vegetables. Official Reason: They’re good for you. The Truth: You don’t eat vegetables because they’re good for you. You eat vegetables to keep them under control!

Millions of years ago, vegetables ruled the earth. Big bunches of broccoli stomped through the jungles, followed by ferocious carrots and savage packs of peas. And what were these terrible vegetables looking for? You guessed it . . .

People! Yes, these were meat-eating vegetables. They terrorized the early humans, attacking without warning. Our ancestors put up with this for centuries, living in drafty caves and getting nasty head colds. But then they discovered sticks and stones.

With these new weapons, humans began to defend themselves. At first, lone hunters would take on a single radish or green bean. Eventually, groups of hunters tackled bigger game, like the saber-toothed asparagus and woolly cucumber. By mixing these vanquished vegetables, primitive chefs invented. . . SALAD!

More important, the discovery of fire allowed humans to cook their leafy foes. This brought the Age of Vegetables to a close. As the human race grew in size and intelligence, vegetables became smaller and dumber, devolving into the pathetic produce of gardens and grocery stores. To prevent vegetables from ever regaining power, grown-ups eat them. They don’t like the flavor any more than you do, but it keeps the little horrors fearful and demoralized. It’s a simple way to protect modern civilization.

Besides, which would you rather do: Eat vegetables or be eaten by vegetables?

(Pg 17-21) [And what about] GROWN-UP RULE #37: Drink Plenty of Milk. Official Reason: It’s good for you. The Truth: Yes, milk is packed with vitamins and protein, but that’s not why parents want you to drink it. The real reason is . . . TO STOP OUR ATOMIC COWS FROM EXPLODING!

Kids have been told that millions of cows produce our country’s milk. That’s not true. At this moment, only five giant cows do all the work. The other are decoys made of plywood and old box springs. One of these colossal cows is Flossie. (MOO!) Eighty feet tall, she provides the daily milk supply for Utah, Nevada, Wyoming, and Colorado. Flossie is kept under tight security at a secret air-force base, right next to the hangar where they stack all the banged-up flying saucers.

Flossie’s size is no accident. In the 1950s, our government was afraid that the Russians would develop the first atomic cow and flood the market with Communist milk. To prevent this, American scientists fed Flossie and her friends radioactive hay. The experiment worked great. But Flossie can’t be turned off. The milk just keeps coming.

[Now], government officials are very happy that all this milk is available. However, there is one crisis the government can’t prepare for: kids NOT drinking milk. If that happened, Flossie would have to hold it (cross legs) Getting bigger and bigger until. . . NUCLEAR MILKDOWN!

Such a catastrophe forever scars the landscape between the Arizona towns of Flagstaff and Winslow. A huge crater is all that remains of Doris, the only atomic cow that ever exploded. When kids felt the ground shake and saw the curdled cloud of dairy products form over the desert back in 1962, they were told that a meteor had hit the local Tastee Freeze.

Now you know better. So drink your milk!

(Pg 37-41) [Which brings us to] GROWN-UP RULE #62: Don’t jump on your bed. (jumping enthusiastically) Official Reasons: You’ll break it. You might get hurt. The Truth: Yes, it’s possible to break your bed if you jump on it. And it’s possible you might bet hurt if you fall off. But you’ll definitely get hurt . . . IF YOU WAKE UP THE MATTRESS!

You see, mattresses aren’t just big lifeless rectangles crammed with stuffing. They are active wooly creatures raised on farms in Scotland. After growing to adulthood, the mattresses start a long period of hibernation. Undisturbed by noise and handling, they are rounded up, sorted by size, and sold to stores. Then they end up in your bedroom, where they snooze peacefully year after year. Unless you jump on them!

Fortunately, today’s mattresses are very difficult to wake up. That wasn’t the case with their hardy ancestors. One night, about 1040 AD, the Scottish King, Malcolm the Upset, wandered the moors, trying to get over eating haggis -- A real humdinger of a national dish -- a pudding made from the heart, lungs and liver of a sheep! No, I am NOT making this up!

Malcolm stumbled upon a wild hibernating mountain mattress, upon which he slept soundly for the first time in many years. He realized that the wild mattress was more comfortable than the boulder he usually slept on. King Malcolm brought the mattress home and began breeding it. Soon he was giving mattresses as gifts to other kinds and queens.

Unfortunately, these feral mattresses woke up and started slinging royalty around! This was very bad for King Malcolm, who spent the rest of his life in prison, eating haggis. (EWWWWW!)

The modern domestic mattress [has a mild] disposition and long hibernation period. Still, it’s not a good idea to jump on your bed. The mattress might be hard to wake up, but it’s not impossible. And, for goodness sake, don’t play the bagpipes near it!

(Pg 49-52) [And finally] GROWN-UP RULE #82 - Don’t pick your nose. Official Reason: It’s gross and disgusting. The Truth: Actually, picking your nose is gross and disgusting. However, that’s not the real reason, which is . . . TO STOP YOUR BRAIN FROM DEFLATING!

The air pipeline that keeps your brain inflated runs past the nostrils to a vast pumping station inside your head. An intruding digit will certainly dent the pipeline. It may even poke a hole in it, causing an outburst of air called (sneezes) In technical language, a sneeze.

If you can’t give up this nasty habit right away, at least be familiar with the warning signs of brain deflation: A faint hissing noise (noise) . . . A sound like a balloon let loose in a bathtub (noise) . . . Silence, and a floppy rolling noise when you tilt your head (noise)

Although this baggy brain still works, it won’t absorb much new information, so it pays to fix it before the next spelling test. Here’s the simple way . . . Shine a flashlight up your nose (demonstrates). Just as a plant tuns toward the sun, your brain will be attracted to the light and flop over to it. Your brain will then be centered over the pipeline, ready for inflation.

[Then] hold your nose and hum. (demonstrates) Finger pressure stabilizes the pipeline. Humming entertains the mending muscles as they drive bulldozers around to fix things up. There is a more difficult way to reinflate your brain, but it requires four years of college, one pair of pliers, and three feet of lead pipe.

Hundreds of grown-up rules remain. The truth must be told about them ALL! (reaction to an unseen noise - whispers) But they’re on [our] trail. I hear them coming! THE GROWN-UPS!!!
```

---

## IC-2120: Seventh Grade

- Title: Seventh Grade
- Author (byline): Gary Soto
- Work: Baseball in April and Other Stories
- Publisher: Harcourt Paperbacks
- Publication date as stated: April 2000
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1903
- Already set (do not supply): none

### Source block (context only)

```text
Author: Gary Soto
Book: Baseball in April and Other Stories
ISBN: 978-0152025670
Date (Month/Year): April 2000
Publisher: Harcourt Paperbacks
```

### Introduction (context only: never use it for content warnings)

```text
Remember what the middle school years were like? An emotional roller coaster: hormone madness and changing bodies; a very shaky self-concept; novel interest in the same or other sex—which is exciting, awkward, confusing—all at the same time; a simultaneous craving for and fear of new freedom … independence from mom and dad. Middle school: the wonder years. Young people wonder, "Will I ever be normal?" Parents wonder, "Will this ever end?" Let’s go back to Seventh Grade with and by Gary Soto
```

### Performance text (classify this)

```text
On the first day of school, Victor stood in line half an hour before he came to a wobbly card table. He was handed a packet of papers and a computer card on which he listed his one elective, French. He already spoke Spanish and English, but he thought some day he might travel to France, where it was cool; not like Fresno, where summer days reached 110 degrees in the shade. There were rivers in Prance, and huge churches, and fair-skinned people everywhere, the way there were brown people all around Victor

Besides, Teresa, a girl he had liked since they were in catechism classes at Saint Theresa’s, was taking French, too. With any luck they would be in the same class.

Teresa is going to be my girl this year, he promised himself as he left the gym full of students in their new fall clothes. She was cute. And good in math, too, Victor thought as he walked down the hall to his homeroom. He ran into his friend, Michael Torres, by the water fountain that never turned off.

They shook hands, raza-style, and jerked their heads at one another in a saludo de vato. “How come you’re making a face?” asked Victor.

“I ain’t making a face, ese. This is my face.” Michael said his face had changed during the summer. He had read a GQ magazine that his older brother had borrowed from the Book Mobile and noticed that the male models all had the same look on their faces. They would stand, one arm around a beautiful woman, and scowl. They would sit at the pool, their rippled stomachs dark with shadow, and scowl. They would sit at dinner tables, cool drinks in their hands, and scowl,

“I think it works,” Michael said. He scowled and let his upper lip quiver. His teeth showed along with the ferocity of his soul. “Belinda Reyes walked by a while ago and looked at me,” he said.

Victor didn’t say anything, though he thought his friend looked pretty strange. They talked about recent movies, baseball, their parents, and the horrors of picking grapes in order to buy their fall clothes. Picking grapes was like living in Siberia, except hot and more boring.

“What classes are you taking?” Michael said, scowling.

“French. How ‘bout you?”

“Spanish. L ain’t so good at it, even if I’m Mexican."

“I’m not either, but I’m better at it than math, that’s for sure.”

A tiny, three-beat bell propelled students to their homerooms. The two friends socked each other in the arm and went their ways, Victor thinking, man, that’s weird. Michael thinks making a face makes him handsome.

On the way to his homeroom, Victor tried a scowl. He felt foolish, until out of the corner of his eye he saw a girl looking at hint Umm, he thought, maybe it does work. He scowled with greater conviction.

In the homeroom, roll was taken, emergency cards were passed out, and they were given a bulletin to take home to their parents. The principal, Mr. Belton, spoke over the crackling loudspeaker, welcoming the students to a new year, new experiences, and new friendships. The students squirmed in their chairs and ignored him, they were anxious to go to first period. Victor sat calmly, thinking of Teresa, who sat two rows away, reading a paperback novel. This would be his lucky year. She was in his homeroom, and would probably be in his English and math classes. And, of course, French.

The bell rang for first period, and the students herded noisily through the door. Only Teresa lingered, talking with the homeroom teacher.

“So you think I should talk to Mrs. Gaines?” she asked the teacher. “She would know about ballet?”

“She would be a good bet,” the teacher said. Then added, “Or the gym teacher, Mrs. Garza."

Victor lingered, keeping his head down and staring at his desk. He wanted to leave when she did so he could bump into her and say something clever.

He watched her on the sly. As she turned to leave, he stood up and hurried to the door, where he managed to catch her eye. She smiled and said, “Hi, Victor."

He smiled back and said, “Yeah, that's me.” His brown face blushed. Why hadn’t he said, “Hi, Teresa,” or "How was your summer?” or something nice.

As Teresa walked down the hall, Victor walked the other way, looking back, admiring how gracefully she walked, one foot in front of the other. So much for being in the same class, he thought. As he trudged to English, he practiced scowling.

In English they reviewed the parts of speech. Mr. Lucas, a portly man, waddled down the aisle, asking, “What is a noun?”

“A person, place, or thing,” said the class in unison.

Yes, now somebody give mean example of a person-- you, Victor Rodriguez.”

"Teresa,” Victor said automatically. Some of the girls giggled. They knew he had a crush on Teresa. He felt himself blushing again.

“Correct,” Mr. Lucas said. “Now provide me with a place.”

Mr. Lucas called on a freckled kid who answered, “Teresa’s house with a kitchen full of big brothers.”

After English, Victor had math, his weakest subject. He sat in the back by the window, hoping that he would not be called on. Victor understood most of the problems, but some of the stuff looked like the teacher made it up as she went along. It was confusing, like the inside of a watch.

After math he had a fifteen-minute break, then social studies, and finally lunch. He bought a tuna casserole with buttered rolls, some fruit cocktail, and milk. He sat with Michael, who practiced scowling between bites,

Girls walked by and looked at him, “See what I mean, Vic?” Michael scowled. "They love it.”

Yeah, I guess so.

They ate slowly, Victor scanning the horizon for a glimpse of Teresa. He didn’t see her. She must have brought lunch, he thought, and is eating outside. Victor scraped his plate and left Michael, who was busy scowling at a girl two tables away.

The small, triangle-shaped campus bustled with students talking about their new classes. Everyone was in a sunny mood. Victor hurried to the bag lunch area, where he sat down and opened his math book. He moved his lips as if he were reading, but his mind was somewhere else. He raised his eyes slowly and looked around. No Teresa.

He lowered his eyes, pretending to study, then looked slowly to the left. No Teresa. He turned a page in the book and stared at some math problems that scared him because he knew he would have to do them eventually. He looked at the right. Still no sign of her. He stretched out lazily in an attempt to disguise his snooping.

Then he saw her. She was sitting with a girlfriend under a plum tree. Victor moved to a table near her and daydreamed about taking her to a movie. When the bell sounded, Teresa looked up, and their eyes met. She smiled sweetly and gathered her books. Her next class was French, same as Victor’s.

They were among the last students to arrive in class, so all the good desks in the back had already been taken. Victor was forced to sit near the front, a few desks away from Teresa, while Mr. Bueller wrote French words on the chalkboard. The bell rang, and Mr. Bueller wiped his hands, turned to the class, and said, “Bonjour.”

“Bonjour,” braved a few students.

“Bonjour” Victor whispered. He wondered if Teresa heard him.

Mr. Bueller said that if the students studied hard, at the end of the year they could go to France and be understood by the populace.

One kid raised his hand and asked, “‘What’s ‘populace’?”

"The people, the people of France.”

Mr. Bueller asked if anyone knew French. Victor raised his hand, wanting to impress Teresa. The teacher beamed and said, “Tres bien. Parlez-vous francais?”

Victor didn’t know what to say. The teacher wet his lips and asked something else in French. The room grew silent. Victor felt all eyes staring at him. He tried to bluff his way out by making noises that sounded French.

“La me vave me con le grandma,” he said uncertainly.

Mr. Bueller, wrinkling his face in curiosity, asked him to speak up.

Great rosebushes of red bloomed on Victor’s cheeks. A river of nervous sweat ran down his palms. He felt awful. Teresa sat a few desks away, no doubt thinking he was a fool. Without looking at Mr. Bueller, Victor mumbled, ‘Frenchie oh wewe gee in September.”

Mr. Bueller asked Victor to repeat what he said.

“Frenchie oh wewe gee in September," Victor repeated.

Mr. Bueller understood that the boy didn’t know French and turned away. He walked to the blackboard and pointed to the words on the board with his steel-edged ruler.

"Le bateau,” he sang.

“Le bateau,” the students repeated.

"Le bateau est sur l’eau,” he sang.

“Le bateau est sur l’eau.”

Victor was too weak from failure to join the class. He stared at the board and wished he had taken Spanish, not French. Better yet, he wished he could start his life over. He had never been so embarrassed. He bit his thumb until he tore off a sliver of skin.

The bell sounded for fifth period, and Victor shot out of the room, avoiding the stares of the other kids, but had to return for his math book. He looked sheepishly at the teacher, who was erasing the board, then widened his eyes in terror at Teresa who stood in front of him. “I didn’t know you knew French,”she said. “That was good.”

Mr. Bueller looked at Victor, and Victor looked back. Oh please, don’t say anything, Victor pleaded with his eyes. I’ll wash your car, mow your lawn, walk your dog-- anything! I'll be your best student, and I’ll clean your erasers after school.

Mr. Bueller shuffled through the papers on his desk, He smiled and hummed as he sat down to work. He remembered his college years when he dated a girlfri0end in borrowed cars. She thought he was rich because each time he picked her up he had a different car. It was fun until he had spent all his money on her and had to write home to his parents because he was broke.

Victor couldn’t stand to look at Teresa. He was sweaty with shame. “Yeah, well, I picked up a few things from movies and books and stuff like that.” They left the class together. Teresa asked him if he would help her with her French.

"Sure, anytime,” Victor said.

“I won’t be bothering you, will I?”

"Oh no, I like being bothered.”

“Bonjour,”Teresa said, leaving him outside her next class. She smiled and pushed wisps of hair from her face.

"Yeah, right, bonjour,” Victor said. He turned and headed to his class. The rosebuds of shame on his face became bouquets of love. Teresa is a great girl, he thought. And Mr. Bueller is a good guy.

He raced to metal shop. After metal shop there was biology, and after biology a long sprint to the public library, where he checked out three French textbooks.

He was going to like seventh grade.
```
