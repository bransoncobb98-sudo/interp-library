# Classification request: batch 55 of 63 (40 records, IC-2161 to IC-2200)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-055-reply.json`.

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

## IC-2161: What, of this Goldfish, Would you Wish?

- Title: What, of this Goldfish, Would you Wish?
- Author (byline): Etgar Keret
- Work: Suddenly, A Knock on the Door
- Publisher: Farrar, Straus and Giroux
- Publication date as stated: March 2012
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1913
- Already set (do not supply): none

### Source block (context only)

```text
Author: Etgar Keret
Book: Suddenly, A Knock on the Door
ISBN: 978-0374533335
Publisher: Farrar, Straus and Giroux
Date (Month/Year): March 2012
```

### Introduction (context only: never use it for content warnings)

```text
What, of this Goldfish, Would you Wish? By Etgar Keret
```

### Performance text (classify this)

```text
Yonatan had a brilliant idea for a documentary. He’d knock on doors. Just him. No camera crew, no nonsense. Just Yonatan, on his own, a small camera in hand, asking, “If you found a talking goldfish that granted you three wishes, what would you wish for?”

Folks would give their answers, and Yoni would edit them down and make clips of the more surprising responses. Before every set of answers, you’d see the person standing stock-still in the entrance to his house. Onto this shot he’d superimpose the subject’s name, family situation, monthly income, and maybe even the party he’d voted for in the last election. All that, combined with the three wishes, and maybe he’d end up with a poignant piece of social commentary, a testament to the massive rift between our dreams and the often compromised reality in which we live.

It was genius, Yoni was sure. And, if not, at least it was cheap. All he needed was a door to knock on and a heart beating on the other side. With a little decent footage, he was sure he’d be able to sell it to Channel 8 or Discovery in a flash, either as a film or as a bunch of vignettes, little cinematic corners, each with that singular soul standing in a doorway, followed by three killer wishes, precious, every one.

Even better, maybe he’d cash out, package it with a slogan and sell it to a bank or cellular phone company. Maybe tag it with something like “Different dreams, different wishes, one bank.” Or “The bank that makes dreams come true.”

No prep, no plotting, natural as can be, Yoni grabbed his camera and went out knocking on doors. In the first neighborhood he went to, the kindly folk that took part generally requested the foreseeable things: health, money, bigger apartments, either to shave off a couple of years or a couple of pounds. But there were also powerful moments. One drawn, wizened old lady asked simply for a child. A Holocaust survivor with a number on his arm asked very slowly, in a quiet voice—as if he’d been waiting for Yoni to come, as if it wasn’t an exercise at all—he’d been wondering (if this fish didn’t mind), would it be possible for all the Nazis left living in the world to be held accountable for their crimes? A cocky, broad-shouldered lady-killer put out his cigarette and, as if the camera wasn’t there, wished he were a girl. “Just for a night,” he added, holding a single finger right up to the lens.

And these were wishes from just one short block in one small, sleepy suburb of Tel Aviv. Yonatan could hardly imagine what people were dreaming of in the development towns and the collectives along the northern border, in the West Bank settlements and Arab villages, the immigrant absorption centers full of broken trailers and tired people left to broil out in the desert sun.

Yonatan knew that if the project was going to have any weight, he’d have to get to everyone, to the unemployed, to the ultra-religious, to the Arabs and Ethiopians and American expats. He began to plan a shooting schedule for the coming days. Maybe somewhere, some beleaguered Arab man would stand in his doorway and, looking through Yonatan and his camera, looking out into nothingness, just pause for a minute, nod his head, and wish for peace—that would be something to see.

********************

Sergei Goralick doesn’t much like strangers banging on his door. Especially when those strangers are asking him questions. In Russia, when Sergei was young, it happened plenty. The KGB felt right at home knocking on his door. His father had been a Zionist, which was pretty much an invitation for them to drop by any old time.

[Then] one day some kid with a ring in his ear, comes knocking. Hard like that— rapping at his door. Just the way Sergei doesn’t like. And he says, this kid, that he has some questions he wants to put on the TV.

Sergei tells the boy, tells him in what he thinks is a straightforward manner, that he doesn’t want it. Not interested. Sergei gives the camera a shove, to help make it clear. But the earring boy is stubborn. He says all kinds of things, fast things. And it’s hard for Sergei to follow; his Hebrew isn’t so good.

The boy slows down, tells Sergei he has a strong face, a nice face, and that he simply has to have him for this movie picture. The kid is slippery, and somehow between saying no and pushing the door closed, Sergei finds that the kid is in his house. He’s already making his movie, running his camera without any permission, and from behind the camera he’s still telling Sergei about his face, that it’s full of feeling, that it’s tender. Suddenly the kid spots Sergei’s goldfish flitting around in its big glass jar in his kitchen.

The kid with the earring starts screaming, “Goldfish, goldfish,” he’s so excited. And this, this really pressures Sergei, who tells the kid, it’s nothing, just a regular goldfish, stop filming it. Just a goldfish, Sergei tells him, just something he found flapping around in the net, a deep-sea goldfish. But the boy isn’t listening. He’s still filming and getting closer and saying something about talking and fish and a magic wish.

Sergei doesn’t like this, doesn’t like that the boy is almost at it, already reaching for the jar. In this instant Sergei understands the boy didn’t come for television, what he came for, specifically, is to snatch Sergei’s fish, to steal it away. Before the mind of Sergei Goralick really understands what it is his body has done, he seems to have taken the burner off the stove and hit the boy in the head. The boy falls. The camera falls with him. The camera breaks open on the floor, along with the boy’s skull. There’s a lot of blood coming out of the head, and Sergei really doesn’t know what to do.

That is, he knows exactly what to do, but it really would complicate things. Because if he takes this kid to the hospital, people are going to ask what happened, and it would take things in a direction Sergei doesn’t want to go.

“No reason to take him to the hospital anyway,” says the goldfish, in Russian. “That one’s already dead.”

“He can’t be dead,” Sergei says, with a moan. “I barely touched him. It’s only a burner. Only a little thing.” Sergei holds it up to the fish, taps it against his own skull to prove it. “It’s not even that hard.”

“Maybe not,” says the fish. “But, apparently, it’s harder than that kid’s head.”

“He wanted to take you from me,” Sergei says, almost crying.

“Nonsense,” the fish says. “He was only here to make a little something for TV.”

“But he said …”

“He said,” says the fish, interrupting, “exactly what he was doing. But you didn’t get it. Honestly, your Hebrew, it’s terrible.”

“Yours is better?” Sergei says. “Yours is so great?”

“Yes. Mine’s supergreat,” the goldfish says, sounding impatient. ‘‘I’m a magic fish. I’m fluent in everything,” All the while the puddle of blood from the earring kid’s head is getting bigger and bigger and Sergei is on his toes, up against the kitchen wall, desperate not to step in it, not to get blood on his feet.

“You do have one wish left,” the fish reminds Sergei. He says it easy like that, as if Sergei doesn’t know—as if either of them ever loses count.

“No,” Sergei says. He’s shaking his head from side to side. “I can’t,” he says. “I’ve been saving it. Saving it for something.”

“For what?” the fish says.

But Sergei won’t answer.

That first wish, Sergei used up when they discovered a cancer in his sister. A lung cancer, the kind you don’t get better from. The fish undid it in an instant—the words barely out of Sergei’s mouth. The second wish Sergei used up five years ago, on Sveta’s boy. The kid was still small then, barely three, but the doctors already knew something in her son’s head wasn’t right. He was going to grow big but not in the brain. Three was about as smart as he’d get. Sveta cried to Sergei in bed all night. Sergei walked home along the beach when the sun came up, and he called to the fish, asked the goldfish to fix it as soon as he’d crossed through the door. He never told Sveta. And a few months later she left him for some cop, a Moroccan with a shiny Honda. In his heart, Sergei kept telling himself it wasn’t for Sveta that he’d done it, that he’d wished his wish purely for the boy. In his mind, he was less sure, and all kinds of thoughts about other things he could have done with that wish continued to gnaw at him, half driving him mad. The third wish, Sergei hadn’t yet wished for.

“I can restore him,” says the goldfish. “I can bring him back to life.”

“No one’s asking,” Sergei says.

“I can bring him back to the moment before,” the goldfish says. “To before he knocks on your door. I can put him back to right there. I can do it. All you need to do is ask.”

“To wish my wish,” Sergei says. “My last.”

The fish swishes his fish tail back and forth in the water, the way he does, Sergei knows, when he’s truly excited. The goldfish can already taste freedom. Sergei can see it on him.

After the last wish, Sergei won’t have a choice. He’ll have to let the goldfish go. His magic goldfish. His friend.

“Fixable,” Sergei says. “I’ll just mop up the blood. A good sponge and it’ll be like it never was.”

That tail just goes back and forth, the fish’s head steady.

Sergei takes a deep breath. He steps out into the middle of the kitchen, out into the puddle. “When I’m fishing, while it’s dark and the world’s asleep,” he says, half to himself and half to the fish, “I’ll tie the kid to a rock and dump him in the sea. Not a chance, not in a million years, will anyone ever find him.”

“You killed him, Sergei,” the goldfish says. “You murdered someone—but you’re not a murderer.” The goldfish stops swishing his tail. “If, on this, you won’t waste a wish, then tell me, Sergei, what is it good for?”

*******************

It was in Bethlehem that Yonatan found his Arab, a handsome man who used his first wish for peace. His name was Munir; he was fat with a big white mustache. Super-photogenic. It was moving, the way he said it. Perfect, the way in which Munir wished his wish. Yoni knew even as he was filming that this guy would be his promo for sure.

Either him or that Russian. The one that looked straight into the camera and said, if he ever found a talking goldfish he wouldn’t ask of it a single thing. He’d just stick it on a shelf in a big glass jar and talk to him all day, it didn’t matter about what. Maybe sports, maybe politics, whatever a goldfish was interested in chatting about.

Anything, the Russian said, not to be alone.
```

---

## IC-2162: The Wish

- Title: The Wish
- Author (byline): Roald Dahl
- Work: Skin and Other Stories
- Publisher: Puffin Books
- Publication date as stated: Jan 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1467
- Already set (do not supply): none

### Source block (context only)

```text
Author: Roald Dahl
Book: Skin and Other Stories
ISBN: 978-0141310343
Publisher: Puffin Books
Date (Month/Year): Jan 2002
```

### Introduction (context only: never use it for content warnings)

```text
Do children today still have the time and initiative to fight pretend dragons, have an imaginary friend, or dress up as a fairy tale princess? Or is plain old imagination fighting a losing battle with iPods, video games, organized sports and T.V. shows? Just what is so important about imagination?

According to Dorothy Singer, professor of psychology at Yale University, children who actively use their imagination reap a host of benefits. Most importantly: Imagination helps school-age children solve problems by helping them think through different outcomes to various situations and role playing ways to cope with difficult or new circumstances.

Roald Dahl brings the imagination of a child to life in The Wish.
```

### Performance text (classify this)

```text
Under the palm of one hand the child became aware of the scab of an old cut on his kneecap. He bent forward to examine it closely. A scab was always a fascinating thing; it presented a special challenge he was never able to resist.

Yes, he thought, I will pick it off, even if it isn't ready, even if the middle of it sticks, even if it hurts like anything.

With a fingernail he began to explore cautiously around the edges of the scab. He got a nail underneath it, and when he raised it, but ever so slightly, it suddenly came off, the whole hard brown scab came off beautifully, leaving an interesting little circle of smooth red skin.

Nice. Very nice indeed. He rubbed the circle and it didn't hurt. He picked up the scab, put it on his thigh and flipped it with a finger so that it flew away and landed on the edge of the carpet, the enormous red and black and yellow carpet that stretched the whole length of the hall from the stairs on which he sat to the front door in the distance. A tremendous carpet. Bigger than the tennis lawn. Much bigger than that. He regarded it gravely, setting his eyes upon it with mild pleasure. He had never really noticed it before, but now, all of a sudden, the colors seemed to brighten mysteriously and spring out at him in a most dazzling way.

You see, he told himself, I know how it is. The red parts of the carpet are red-hot lumps of coal. What I must do is this: I must walk all the way along it to the front door without touching them. If I touch the red I will be burnt. As a matter of fact, I will be burnt up completely. And the black parts of the carpet. . . yes, the black parts are snakes, poisonous snakes, adders mostly, and cobras, thick like tree trunks round the middle, and if I touch one of them, I'll be bitten and I'll die before tea time. And if I get across safely, without being burnt and without being bitten, I will be given a puppy for my birthday tomorrow.

He got to his feet and climbed higher up the stairs to obtain a better view of this vast tapestry of color and death. Was it possible? Was there enough yellow? Yellow was the only color he was allowed to walk on. Could it be done? This was not a journey to be undertaken lightly; the risks were far too great for that. The child's face-a fringe of white gold hair, two large blue eyes, a small pointed chin-peered down anx-iously over the banisters. The yellow was a bit thin in places and there were one or two widish gaps, but it did seem to go all the way along to the other end. For someone who had only yesterday triumphantly traveled the whole length of the brick path from the stables to the summerhouse without touching the cracks, this carpet thing should not be too difficult. Except for the snakes. The mere thought of snakes sent a fine electricity of fear running like pins down the backs of his legs and under the soles of his feet.

He came slowly down the stairs and advanced to the edge of the carpet. He extended one small sandaled foot and placed it cautiously upon a patch of yellow. Then he brought the other foot up, and there was just enough room for him to stand with the two feet together. There! He had started! His bright oval face was curiously intent, a shade whiter perhaps than before, and he was holding his arms out sideways to assist his balance. He took another step, lifting his foot high over a patch of black, aiming carefully with his toe for a narrow channel of yellow on the other side. When he had completed the second step he paused to rest, standing very stiff and still. The narrow channel of yellow ran forward unbroken for at least five yards and he advanced gingerly along it, bit by bit, as though walking a tightrope. Where it finally curled off sideways, he had to take another long stride, this time over a vicious-looking mixture of black and red. Halfway across he began to wobble. He waved his arms around wildly, windmill fashion, to keep his balance, and he got across safely and rested again on the other side. He was quite breathless now, and so tense he stood high on his toes all the time, arms out sideways, fists clenched. He was on a big safe island of yellow. There was lots of room on it, he couldn't possibly fall off, and he stood there resting, hesitating, waiting, wishing he could stay forever on this big safe yellow island. But the fear of not getting the puppy compelled him to go on.

Step by step, he edged further ahead, and between each one he paused to decide exactly where he should put his foot. Once, he had a choice of ways, either to left or right, and he chose the left because al-though it seemed the more difficult, there was not so much black in that direction. The black was what had made him nervous. He glanced quickly over his shoulder to see how far he had come. Nearly halfway. There could be no turning back now. He was in the middle and he couldn't turn back and he couldn't jump off sideways either because it was too far, and when he looked at all the red and all the black that lay ahead of him, he felt that old sudden sickening surge of panic in his chest-like last Easter time, that afternoon when he got lost all alone in the darkest part of Piper's Wood.

He took another step, placing his foot carefully upon the only little piece of yellow within reach, and this time the point of the foot came within a centimeter of some black. It wasn't touching the black, he could see it wasn't touching, he could see the small line of yellow separating the toe of his sandal from the black; but the snake stirred as though sensing his nearness, and raised its head and gazed at the foot with bright beady eyes, watching to see if it was going to touch.

“I’m not touching you! You mustn't bite me! You know I'm not touching you!"

Another snake slid up noiselessly beside the first, raised its head, two heads now, two pairs of eyes staring at the foot, gazing at a little naked place just below the sandal strap where the skin showed through. The child went high up on his toes and stayed there, frozen stiff with terror. It was minutes before he dared to move again.

The next step would have to be a really long one. There was this deep curling river of black that ran clear across the width of the carpet, and he was forced by his position to cross it at its widest part. He thought first of trying to jump it, but decided he couldn't be sure of landing accurately on the narrow band of yellow on the other side. He took a deep breath, lifted one foot, and inch by inch he pushed it out in front of him, far, far out, then down and down until at last the tip of his sandal was across and resting safely on the edge of the yellow. He leaned forward, transferring his weight to his front foot. Then he tried to bring the back foot up as well. He strained and pulled and jerked his body, but the legs were too wide apart and he couldn't make it. He tried to get back again. He couldn't do that either. He was doing the splits and he was properly stuck. He glanced down and saw this deep curling river of black underneath him. Parts of it were stirring now, and uncoiling and beginning to shine with a dreadfully oily glister. He wobbled, waved his arms frantically to keep his balance, but that seemed to make it worse. He was starting to go over. He was going over to the right, quite slowly he was going over, then faster and faster, and at the last moment, instinctively he put out a hand to break the fall and the next thing he saw was this bare hand of his going right into the middle of a great glistening mass of black and he gave one piercing cry as it touched.

Outside in the sunshine, far away behind the house, the mother was looking for her son.
```

---

## IC-2163: The Witches

- Title: The Witches
- Author (byline): Roald Dahl
- Work: Not specified
- Publisher: Puffin Books
- Publication date as stated: June 1998
- Event as filed: Prose
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

## IC-2164: The Witch’s Broom

- Title: The Witch’s Broom
- Author (byline): AJ Jacobs
- Work: Fractured Fairy Tales
- Publisher: Bantam Books
- Publication date as stated: Jan 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1004
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
You can’t deny it . . . she was a master of her craft. And to top it all off, she had the most glorious broom you could imagine. A glorious, clever and somewhat JEALOUS broom . . . The Witch’s Broom by AJ Jacobs
```

### Performance text (classify this)

```text
Once upon a time there was a witch named Grizelka who chalked up a very enviable record when it came to witchery. If you don't believe me, just look at her resumé:

Sleeping Beauty : Cast highly effective spell on young female, putting her in a state of slumber for several decades.

The Frog Prince: Turned member of the royal family into an amphibian. Received wide publicity.

Hansel and Gretel: Successfully enticed two young siblings to a house in the forest using sweet food as bait.

Naturally, when it came time to give out the award for The Best Witch of the Year, Grizelka won. At her acceptance speech to the Academy of Witches, she moved almost everyone to tears.

"I'd like to thank all the little people who made this possible. Like that guy I shrank to fourteen inches tall after he said something about the wart on my nose. And I'd especially like to thank my assistant, also a little person, the gnome named Harry. I'll treasure this gold-plated skull the rest of my unnatural life!"

Well, sir, after winner the Best Witch Award, Grizelka's stock soared high, and as far as she was concerned, every night was like Halloween. One day, a typical day, Harry and Grizelka were busy in her cobweb-filled house, hashing out her schedule.

"Okay," Harry said, glancing at his clipboard. "Tomorrow you're due to fly to London to touch off the Year of the Plague. And then you've got a banquet for the society for the Humane Treatment of Trolls."

"Cancel that till Monday. Tomorrow I've got to lock this lady Rapunzel in a tower and then run over to the--"

Suddenly, the door to the witch's little house creaked open and there stood the most handsome prince in the world.

"Ah, fair lady," said the prince to Grizelka. "Could I trouble you for a flagon of water?"

Such a request wasn't exactly the wisest thing the prince had ever done. In fact, it was tantamount to committing hari-kari.

"Instead of water, try a sip of this!" said mean old Grizelka, handing him a hissing, steaming cup of newts' knees, bat tripe, and other ingredients that would probably not pass FDA inspection, but would turn the prince into a tree stump. Still, witches too have hearts and, at the very last second before the concoction touched the prince's lips, Grizelka's was struck by Cupid's arrow.

"Don't drink that!" she shouted, and knocked it to the floor. The liquid burned a hole three feet deep.

"My word," said the prince, ''it must be carbonated."

With that, he made a courtly bow, and excused himself to go to the well outside to quench his thirst. Grizelka stared wistfully through the window. For the next few days, Grizelka just couldn't concentrate on her witchery.

She sent Snow White a poisoned kumquat instead of a poisoned apple. She turned bats into bunny rabbits. She tried to put people to sleep, but just made them tired and cranky. Finally, she admitted to herself that she was in love--but because she was horribly ugly, even by witchly standards, she knew she could never win the prince. And so she went to the magic mirror--which charged only $100 for fifty minutes--and asked for advice.

"Mirror, mirror on the wall--and don't you dare crack on me--how can I win the prince's love?"

"Why don't you cast a spell on yourself? I'm afraid our time is up. I must go before I crack up myself."

Of course! The mirror was right. If Grizelka changed herself into a beautiful princess, the prince would fall in love with her. For two weeks she worked on the project, stirring a cauldron full of wolfbane, mice wings, and artificial flavors and colors. Finally, it came time for the age-old incantation.

"Over the teeth and through the gums, look out stomach, here it comes!"

She drank it and--POOF!--where the witch once stood, there was an enchanting princess. The next day, the newly beautiful witch went to the royal ball. When she got there, the prince and the king were in the corner, talking.

"Well, my son, how are you enjoying the ball?" asked the king.

"Oh, I'm having a ball, Dad."

"I know that, but how are you enjoying it?"

But before the prince could answer, he spotted the most beautiful maiden he had ever seen.

"You're beautiful, you're lovely, you're engaged...to me!

Am I rushing things?"

Grizelka shook her head. A whirlwind romance ensued. They went to the opera, to the ballet, to beheadings. But there was one little problem. They were never alone. For wherever they went, along came a broom--the broom that Grizelka used to ride on her nightly forays. It would ride in the carriage with them, sit next to them at shows. There was just no escaping her past. The prince began to get a bit suspicious.

"Now, I have nothing against cleaning instruments in general," he said. "I just want to be alone with you."

Desperate, Grizelka decided to shell out another $100 and go to her old mirror on the wall.

"Ah, well, it is all psychological, my dear. You see, that broom over there has a sort of dust complex. Now that you're a princess, it's lonely. It misses its former owner. And it no doubt still thinks you are a witch."

"Well, what can I do?"

"The answer is simple. Get it a gride."

Now, in medieval English, which is what the mirror was speaking, the word gride meant dustpan.

So the witch immediately purchased a small but attractive dustpan and set it beside the lonesome broom in the broom closet. The rest happened naturally.

In the end, when the prince and the princess got married, they had a double wedding with the happy cleaning instrument couple. So, as you can see, not only was there a bride and a groom, but there was also a gride and a broom.
```

---

## IC-2165: Writing is Easy

- Title: Writing is Easy
- Author (byline): Steve Martin
- Work: Pure Drivel
- Publisher: Hyperion
- Publication date as stated: Oct 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1546
- Already set (do not supply): none

### Source block (context only)

```text
Author: Steve Martin
Book: Pure Drivel
ISBN: 978-0786885053
Publisher: Hyperion
Date (Month/Year): Oct 1999
```

### Introduction (context only: never use it for content warnings)

```text
But “Writing is Easy” by Steve Martin
```

### Performance text (classify this)

```text
Writing is one of the most easy, pain-free, and happy ways to pass the time in all the arts. For example, right now I am sitting in my rose garden and typing on my new computer. Each rose represents a story, so I'm never at a loss for what to write. I just look deep into the heart of the rose and read its story and write it down through typing, which I enjoy anyway. I could be typing "kjfiu joewmv jiw" and would enjoy it as much as typing words that actually make sense. I simply relish the movement of my fingers on the keys. Sometimes, it is true, agony visits the head of a writer. At these moments, I stop writing and relax with a coffee at my favorite restaurant, knowing that words can be changed, rethought, fiddled with, and, of course, ultimately denied. Painters don't have that luxury. If they go to a coffee shop, their paint dries into a hard mass.

Location, Location, Location

I would recommend to writers that they live in California, because here they can look up at the blue sky in between those moments of looking into the heart of a rose. I feel sorry for writers--and there are some pretty famous ones--who live in places like South America and Czechoslovakia, where I imagine it gets pretty dreary. These writers are easy to spot. Their books are often depressing and filled with disease and negativity. If you're going to write about disease, I would suggest that California is the place to do it. Dwarfism is never funny, but look at the result when it was dealt with out here in California. Seven happy dwarfs. Can you imagine seven dwarfs in Czechoslovakia? You would get seven melancholic dwarfs at best, seven melancholic dwarfs with no handicapped-parking spaces.

Love in the Time of Cholera: why it's a bad title

I admit that "Love in the time of ..." is a great title, so far. You're reading along, you're happy, it's about love, I like the way the word time comes in there, something nice in the association of love and time, like a new word almost, lovetime: nice, nice feeling. Suddenly, the morbid Cholera appears. I was happy till then. "Love in the Time of the Oozing Sores and Pustules" is probably an earlier, rejected title of this book, written in a rat-infested tree house on an old Smith-Corona. This writer, whoever he is, could have used a couple of weeks in Pacific Daylight Time.

I did a little experiment. I decided to take the following disheartening passage, which was no doubt written in some depressing place, and attempt to rewrite it under the influence of California:

Most people deceive themselves with a pair of faiths: they believe in eternal memory (of people, things, deeds, nations) and in redressibility (of deeds, mistakes, sins, wrongs). Both are false faiths. In reality the opposite is true: everything will be forgotten and nothing will be redressed. (Milan Kundera) Sitting in my garden, as the bees glide from flower to flower, I let the above paragraph filter through my mind. The following new paragraph emerged:

I feel pretty,

Oh so pretty,

I feel pretty and witty and bright.

Kundera was just too wordy. Sometimes the delete key is your greatest friend.

Writer's Block: A Myth

Writer's block is a fancy term made up by whiners so they can have an excuse to drink alcohol. Sure a writer can get stuck for a while, but when that happens to real authors, they simply go out and get an "as told to." The alternative is to hire yourself out as an "as heard from," thus taking all the credit. It is also much easier to write when you have someone to "bounce" with. This is someone to sit in a room with and exchange ideas. It is good if the last name of the person you choose to bounce with is Salinger. I know a certain early-twentieth-century French writer, whose initials were M.P., who could have used a good bounce person. If he had, his title might have been the more correct "Remembering Past Things" instead of the clumsy one he used. The other trick I use when I have a momentary stoppage is virtually foolproof, and I'm happy to pass it along. Go to an already published novel and find a sentence you absolutely adore. Copy it down in your manuscript. Usually that sentence will lead you naturally to another sentence; pretty soon your own ideas will start to flow. If they don't, copy down the next sentence. You can safely use up to three sentences of someone else's work--unless they're friends; then you can use two. The odds of being found out are very slim, and even if you are, there's no jail time.

Creating Memorable Characters

Nothing will make your writing soar more than a memorable character. If there is a memorable character, the reader will keep going back to the book, picking it up, turning it over in his hands, hefting it, and tossing it into the air. Here is an example of the jazzy uplift that vivid characters can offer: Some guys were standing around when in came this guy.

You are now on your way to creating a memorable character. You have set him up as being a guy, and with that come all the reader's ideas of what a guy is. Soon you will liven your character by using an adjective: But this guy was no ordinary guy, he was a red guy.

This character, the red guy, has now popped into the reader's imagination. He is a full-blown person, with hopes and dreams, just like the reader. Especially if the reader is a red guy. Now you might want to give the character a trait. You can inform the reader of the character trait in one of two ways. First, simply say what that trait is--for example, "but this red guy was different from most red guys, this red guy liked frappes." The other is rooted in action--have the red guy walk up to a bar and order a frappe, as in:

"What'll you have, red guy?"

"I'll have a frappe."

Once you have mastered these two concepts, vivid character writing combined with adjectives, you are on your way to becoming the next Shakespeare's brother. And don't forget to copyright any ideas you have that might be original. You don't want to be caught standing by helplessly while your familiar "red guy" steps up to a bar in a frappe commercial.

Writing Dialogue

Many very fine writers are intimidated when they have to write the way people really talk. Actually it's quite easy. Simply lower your IQ by fifty and start typing!

Subject Matter

Because topics are in such short supply, I have provided a few for writers who may be suffering in the darker climes. File some of these away, and look through them during the suicidal winter months:

"Naked Belligerent Panties": This is a good sexy title with a lot of promise.

How about a diet book that suggests your free radicals don't enter ketosis unless your insulin levels have been carbo-charged?

Something about how waves at the beach just keep coming and coming and how amazing it is (I smell a bestseller here).

"Visions of Melancholy from a Fast-Moving Train": Some foreign writer is right now rushing to his keyboard, ready to pound on it like Horowitz. However, this title is a phony string of words with no meaning and would send your poor book to the "Artsy" section of Barnes and Noble, where--guess what--it would languish, be remaindered, and die.

A Word to Avoid

"Dagnabbit" will never get you anywhere with the Booker Prize people. Lose it.

Getting Published I have two observations about publishers:

1. Nowadays, they can be either male or female.

2. They love to be referred to by the appropriate

pronoun. If your publisher is male, refer to him

as "he." If your publisher is female, "she" is

considered more correct. Once you have

established a rapport, "Babe" is also acceptable

for either sex.

Once you have determined your pronoun usage, you are ready to "schmooze" your publisher. Let's say your favorite author is Dante. Call Dante's publisher and say you'd like to invite them both to lunch. If the assistant says something like "But Dante's dead," be sympathetic and say, "Please accept my condolences." Once at lunch, remember never to be moody. Publishers like up, happy writers, although it's impressive to suddenly sweep your arm slowly across the lunch table, dumping all the plates and food onto the floor, while shouting "Sic Semper Tyrannis!"

A Demonstration of Actual Writing It's easy to talk about writing and even easier to do it. Watch:

Call me Ishmael.

It was cold, very cold, here in the mountain town of Kilimanjaroville.

I could hear a bell. It was tolling. I knew exactly for who it was tolling, too. It was tolling for me, Ishmael Twist, a red guy who likes frappe.

[Author's note: I am now stuck. I walk over to a rose and look into its heart.] That's right, Ishmael Twist.

Finally, I can't overstress the importance of having a powerful closing sentence.
```

---

## IC-2166: Yertle the Turtle

- Title: Yertle the Turtle
- Author (byline): Theodor Geisel (aka Dr. Suess)
- Work: Not specified
- Publisher: Tandem Library
- Publication date as stated: Nov 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 960
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theodor Geisel (Dr. Seuss)
ISBN: 978-0007173143
Publisher: Tandem Library
Date(Month/Year): Nov 2001
```

### Introduction (context only: never use it for content warnings)

```text
Although many people are unaware of the political basis for many of Geisel’s children’s books, the story of Yertle the Turtle closely parallels the story of Adolf Hitler during World War II. In fact, the original design of Yertle the Turtle had a moustache (before Dr. Seuss removed it, not wanting the symbolism to be too blatantly obvious). Hitler was the despotic ruler of Germany, before he decided to expand the country's wealth by means of force. Yertle the Turtle used turtles as his stepping stones to power, Adolf Hitler used the people of Germany, Italy, and the USSR as his. Welcome to the parable of Yertle the Turtle by Theodor Geisel (Dr Suess). He’s not just for children anymore . . . .
```

### Performance text (classify this)

```text
On the far-away island of Sala-ma-Sond, Yertle the Turtle was king of the pond. A nice little pond. It was clean. It was neat. The water was warm. There was plenty to eat. The turtles had everything turtles might need. And they were all happy. Quite happy indeed.

They were... until Yertle, the king of them all, Decided the kingdom he ruled was too small.

"I'm ruler," said Yertle, "of all that I see. But I don't see enough. That's the trouble with me. With this stone for a throne, I look down on my pond But I cannot look down on the places beyond. This throne that I sit on is too, too low down. It ought to be higher!" he said with a frown. "If I could sit high, how much greater I'd be! What a king! I'd be ruler of all that I see!"

So Yertle, the Turtle King, lifted his hand And Yertle, the Turtle King, gave a command. He ordered nine turtles to swim to his stone And, using these turtles, he built a new throne. He made each turtle stand on another one's back And he piled them all up in a nine-turtle stack. And then Yertle climbed up. He sat down on the pile. What a wonderful view! He could see 'most a mile! "All mine!" Yertle cried. "Oh, the things I now rule! I'm the king of a cow! And I'm the king of a mule!

I'm the king of a house! And, what's more, beyond that
I'm the king of a blueberry bush and a cat!
I'm Yertle the Turtle! Oh, marvelous me!
For I am the ruler of all that I see!"

And all through the morning, he sat up there high Saying over and over, "A great king am I!" Until 'long about noon. Then he heard a faint sigh. "What's that?" snapped the king And he looked down the stack. And he saw, at the bottom, a turtle named Mack. Just a part of his throne. And this plain little turtle Looked up and he said, "Beg your pardon, King Yertle. I've pains in my back and my shoulders and knees. How long must we stand here, Your Majesty, please?" "SILENCE!" the King of the Turtles barked back. "I'm king, and you're only a turtle named Mack." "You stay in your place while I sit here and rule. I'm the king of a cow! And I'm the king of a mule! I'm the king of a house! And a bush! And a cat! But that isn't all. I'll do better than that!

My throne shall be higher!" his royal voice thundered, "So pile up more turtles! I want 'bout two hundred!" "Turtles! More turtles!" he bellowed and brayed. And the turtles 'way down in the pond were afraid. They trembled. They shook. But they came. They obeyed. From all over the pond, they came swimming by dozens. Whole families of turtles, with uncles and cousins. And all of them stepped on the head of poor Mack. One after another, they climbed up the stack. Then Yertle the Turtle was perched up so high, He could see fourty miles from his throne in the sky! "Hooray!" shouted Yertle. "I'm the king of the trees! I'm king of the birds! And I'm king of the bees! I'm king of the butterflies! King of the air! Ah, me! What a throne! What a wonderful chair! I'm Yertle the Turtle! Oh, marvelous me! For I am the ruler of all that I see!"

Then again, from below, in the great heavy stack, Came a groan from that plain little turtle named Mack. "Your Majesty, please... I don't like to complain, But down here below, we are feeling great pain. I know, up on top you are seeing great sights, But down here at the bottom we, too, should have rights. We turtles can't stand it. Our shells will all crack! Besides, we need food. We are starving!" groaned Mack.

"You hush up your mouth!" howled the mighty King Yertle. "You've no right to talk to the world's highest turtle. I rule from the clouds! Over land! Over sea! There's nothing, no, NOTHING, that's higher than me!"

But, while he was shouting, he saw with suprise
That the moon of the evening was starting to rise
Up over his head in the darkening skies.
"What's THAT?" snorted Yertle. "Say, what IS that
thing
That dares to be higher than Yertle the King?
I shall not allow it! I'll go higher still!

I'll build my throne higher! I can and I will! I'll call some more turtles. I'll stack 'em to heaven! I need 'bout five thousand, six hundred and seven!"

But, as Yertle, the Turtle King, lifted his hand
And started to order and give the command,
That plain little turtle below in the stack,
That plain little turtle whose name was just Mack,
Decided he'd taken enough. And he had.
And that plain little lad got a bit mad.
And that plain little Mack did a plain little thing.
He burped!
And his burp shook the throne of the king!

And Yertle the Turtle, the king of the trees, The king of the air and the birds and the bees, The king of a house and a cow and a mule... Well, that was the end of the Turtle King's rule! For Yertle, the King of all Sala-ma-Sond, Fell off his high throne and fell Plunk! in the pond!

And tosay the great Yertle, that Marvelous he,
Is King of the Mud. That is all he can see.
And the turtles, of course... all the turtles are free
As turtles and, maybe, all creatures should be.
```

---

## IC-2167: You Know What, Teacher?

- Title: You Know What, Teacher?
- Author (byline): Zenna Henderson
- Work: Holding Wonder
- Publisher: Avon Books
- Publication date as stated: Jan 1971
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1765
- Already set (do not supply): none

### Source block (context only)

```text
Author: Zenna Henderson
Book: Holding Wonder
ISBN: 978-0380440818
Publisher: Avon Books
Date (Month/Year): Jan 1971
* Cutting compliments of Gregg Moeller of Wisner, NE
```

### Introduction (context only: never use it for content warnings)

```text
Linnet is a shy first-grader who brings to school all the news from home. But in time she reveals a tragic secret to Miss Peterson, her teacher, the only person she trusts, in “You Know What, Teacher” by Zenna Henderson.
```

### Performance text (classify this)

```text
Miss Peterson looked resignedly around the school yard. The children swept ceaselessly from one side of the playground to the other, running madly, sometimes being jet planes, sometimes cowboys, but mostly just running. For the fourth time [she] looked at her watch. Two minutes less of noon recess than the last time she had looked.

“You know what, Teacher?” Linnet’s soft little voice spoke at her elbow. “You know what my mother thinks?”

“What does your mother think?”

“My mother thinks my daddy is running around with another woman.”

Rain swept the closed windows with a rustly, papery sound. Miss Peterson tapped her desk bell and blessed the slight lull that followed. Rainy days were gruesome when you had to keep the children in.

“You know what, teacher?” Linnet’s voice was soft by her shoulder.

“W-H-A-T. That’s what!” laughed Miss Peterson, hugging Linnet’s fragile body against her. Linnet considered for a moment and then smiled.

“I mean, you know what happened at our house last night?”

“No, what?”

“My mother and my daddy had a big fight. Not a hitting fight—a holler fight.”

“Oh?” Miss Peterson [was] still holding Linnet in the circle of her arm.

“Yes. I listened. Daddy said Mother spent too much money and Mother said she spent it for food and rent and not on women and she got so mad she wouldn’t sleep in the bedroom. She slept all night on the couch. I took her one of my blankets. It was cold.”

“That was nice of you,” said Miss Peterson. “Parents!” she thought in exasperation. “Selfish, thoughtless, self-centered . . . !

For the next few months, the state of affairs at Linnet’s house could have been charted as exactly as the temperatures. When she came hollow-eyed to school to fall asleep with a crayon clutched in one hand, it was either that Daddy had come home and they’d gone to the Drive-In to celebrate, or Daddy had gone away again after a long holler fight the night before.

“You know what, teacher?” [Linnet asked one morning after a story about a bus driver]. “Last night we rode on the bus a long ways!”

“My! You must have had fun!”

“We went to find Daddy . . . Mother cried . . . All the way home. ”

“Oh, that’s too bad.” Miss Peterson’s heart turned over at the desolation on Linnet’s face.

“She didn’t cry until we left the motel. You know what, teacher? The lady at the motel got mixed up. She told Mother that Daddy wasn’t there but that Mrs.

Luhrs was. How could she be Mrs. Luhr when Mother is Mrs. Luhrs? She wasn’t in the cabin.”

“Well . . . ” said Miss. Peterson.

“When we got on the bus, the money went ding ding in the box just like in our song!” said Linnet.

It makes me so mad, I could spit! Why can’t that mother manage to keep something from the child? There’s no reason to drag Linnet through the nasty mess. I’m kind of worried. I met Mrs. Luhrs at a PTA meeting several weeks ago. She looks – well, unstable – the mousey-looking kind that gives you a feeling of smoldering dynamite—if dynamite can smolder. Poor Linnet.

Several weeks later, Linnet leaned against Miss Peterson’s desk and asked, “How much more until lunch, teacher? I’m hungry.”

“Not very long, Linnet. What’s the matter, didn’t you eat a good breakfast this morning?

“I didn’t eat any breakfast. I got up too late. I almost missed the bus.”

“You better tell your mother to get you up earlier!”

“She didn’t wake up either. The doctor gave her some sleeping stuff so she won’t cry at night, and she didn’t hear the alarm clock. She said one morning without breakfast wouldn’t hurt me. But I’m hungry.”

Then, about a week later, Linnet came to school resplendent in a brand-new dress, carrying a huge box of crayons. ”Even a gold, and a silver and a white one, teacher!” She was jiggling around excitedly, her newly set curls bobbing with an animation they hadn’t shown in months.

“You know what, teacher? Daddy came home last night! I woke up and I heard him tell Mother he was through with that double-crossing b**** and he’d never go away again!”

It lasted a month. Then Linnet crept around in the schoolroom, not even caring when Henry took her white crayon and chewed it into a crumbled mess. Three trembling fingers crept up to cover a trembling mouth.

She forgot simple words she had known for months, and she cried before trying new ones.

One day the reading group laughed over the story of Spot dragging the covers off Sally to wake her up. They all had wide-eyed stories to tell about how hard they were to wake up or how incredibly early they woke up by themselves.

“You know what, teacher? That’s just like Daddy and Mother this morning,” said Linnet softly. “They didn’t get out of bed, so I fixed my own breakfast and got ready for school, all by myself.

“My, you’re getting to be a big girl, aren’t you?”

“Yes. I went into their bedroom [and] I pulled the covers up for Mother because her shoulders were cold. Her nightgown hasn’t got any sleeves,”

When Linnet brought up the smudged, straggly writing paper that had replaced her former neat and legible ones, Miss Peterson wondered why this morning, when Daddy was home, Linnet’s work hadn’t improved.

“You know what, teacher? Last night Mother promised she wouldn’t cry any more, not ever again. And she said Daddy won’t ever go away again.”

“Isn’t that fine? Now you can have lots of fun together, can’t you!”

Linnet turned her head away. “Daddy doesn’t like me anymore.”

“Oh, surely he does—all daddies love their little girls.”

“My daddy doesn’t. Mother let me take him a cup of coffee last night while she was doing the dishes. He drank it and said, “Hell, even the coffee around here is enough to turn your stomach. Beat it, brat” And he pushed me and I dropped the empty cup and it broke.

“But if he isn’t going away any more – “

“Mother told me that.” Linnet’s eyes were full of unchildlike wisdom. “She told me lots of times before. But she didn’t hear Daddy swear.”

“Well, it will be nice if your mother doesn’t cry anymore.”

“Yes. When she cries, I cry too.”

Miss Peterson watched Linnet go back to her table and start her fun-paper. Poor cherub, she thought.

“Do you suppose I ought to do something about it?” she asked Miss Estes in the cafeteria.

“Do what? Call the sheriff because a father swore at his child and called her a brat?”

“You know it’s more than that. An unwholesome home environment.”

“What would you do? Take her away from them? In that case you’d have to take half the kids in the nation away from their parents. Nope, as long as she’s fed and clothed and carries no visible scars, you can’t invoke the law.”

[Later that day], after the buses had gone, Miss Peterson saw a lonely figure sitting by the swings.

“Hi, teacher! Mother told me not to come home on the bus today. She said someone would come after me.” Linnet was opening and shutting a little blue-and-white box.

“What’s that?” asked Miss Peterson.

“It’s empty. Mother got this at the drugstore yesterday. It had medicine in it then. It was Mother’s sleeping stuff.” Linnet snapped the box shut again. “You know what, teacher? She put an awful lot of sugar in Daddy’s coffee before I took it to him, and he doesn’t like very much sugar. Maybe that’s why he got mad last night.”

“Where did you get this box, Linnet?”

“It was on Mother’s dresser, by her coffee cup. When I went in this morning to see if they were awake, I found it. It was empty.”

Miss Peterson sat eyeing the box for a long minute. Of course it couldn’t be. Children so often exaggerate and draw mistaken conclusions. But . . .

“Let’s play something while you’re waiting. Let’s play What Comes Next. You know, like we do with the picture stories in our workbooks.”

“Okay, Teacher!” Linnet’s eyes lighted with pleasure

“Now, last night, your mother poured your Daddy’s coffee. What Comes Next?”

“Oh, you missed a What Comes Next!” Linnet laughed. “[First] Mother put a lot of the sleeping stuff in Daddy’s cup. She said Daddy was getting restless. Then she poured the coffee.”

“Then you took it to your Daddy?”

“Uh-uh! First I had to get Mother a hankie because she was crying. Then I took it to Daddy.”

“And then your daddy drank it. What Comes Next?”

“I don’t know.”

“You said you dropped the cup . . . “

“Yes . . . I dropped the cup when Daddy got mad and pushed me.” The two sat in silence a while . . .

“When it got dark, you got ready for bed and your mother and daddy said good night.”

“Not Daddy. He went to bed before I did last night. He yawned and yawned and went to bed. And then I went to bed and Mother woke me up [this morning] and told me she wouldn’t ever cry again and that Daddy wouldn’t ever leave her again. And then . . . and then . . . Oh, teacher. You know what? She gave me a note to give to you! She put it in my shoe so I wouldn’t lose it.“

She pulled off the scuffed little oxford and fished inside it. Finally she came up with two grimy pieces of paper.

Miss Petersen sat in the swaying s wing and she wished with all her heart that she didn’t have to read the note:

Please don’t let Linnet ride the bus home. Call AR 2-9276 when school is over. Ask them to keep her for a day or two until her grandmother comes. Thank you.

Linnell Luhrs

“What does it say, teacher?”

“It says for you not to go home on the bus. You’re to wait.”

She looked down at the cramped, close-written line that slanted sharply below the signature.

God forgive me. I couldn’t let him go away again.

“Well,” said Miss Peterson. “I have to go to the office and make a phone call. You say here and play. Remember, don’t move away from here.”

“You know what, teacher?”

“No, what?

“It’s kinda lonesome here, all alone . . . “

“Yes it is, dear,” said Miss Peterson, blinking against the sting in her eyes. “It is kinda lonesome, all alone.”
```

---

## IC-2168: Your Father Has the Hay Fever

- Title: Your Father Has the Hay Fever
- Author (byline): R. Anthony Powell
- Work: I Thought My Father Was God
- Publisher: Picador
- Publication date as stated: Sept 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1878
- Already set (do not supply): none

### Source block (context only)

```text
Author: R. Anthony Powell
Book: I Thought My Father Was God
ISBN: 978-0312421007
Publisher: Picador
Date (Month/Year): Sept 2002
```

### Introduction (context only: never use it for content warnings)

```text
Your Father Has the Hay Fever by R. Anthony Powell
```

### Performance text (classify this)

```text
My father is obsessed with his nose, slave to it. In his mind, he believes God created the nose as a joke around the office and forgot all about it in the rush to finish up the universe before Sunday, His day off. My father and God have a lot in common: God has the fate of all existence on his shoulders, Dad has hay fever. Dad figures it comes out about even. "He doesn't want hay fever. Believe me."

Not a moment goes by that our household is not preoccupied with Dad's nose. How could it possibly be otherwise? It's like some kind of malicious presence that lives with us. Any little diversion we plan—an afternoon drive to the Dairy Queen, a game of Monopoly after supper—Dad's nose vetoes. And those we do manage to get underway while Old Faithful slumbers are invariably aborted when it awakens, like a cross wasp pinned to my father's face. We cut the picnic short or leave the movie in the middle and go home to follow Dad around the house, in search of his inhaler or nasal spray, like five ghouls patrolling their rooms, Dad leading the way with the litany, "My nose, my nose, my nose," like that is the object of our search. Anyone looking in the window would be a fool not to call the authorities.

He stands at the bathroom lavatory, both nostrils clogged beyond sanity. His arsenal is set out before him: nasal spray, nasal drops, nasal plugs, nasal cream, Vicks Vap-O-Rub, camphor oil, olive oil, motor oil, 3-in-1, Liquid-Plumr, Drano, blasting caps. He has developed combinations requiring EPA approval, industrial permits, evacuation of the neighborhood. I stand at the door and watch as he mixes his snake-oils, administers them, then waits for the miracle, absolutely still, like he's listening for faraway hoofbeats, the cavalry, coming to save him from his own nose. Invariably, the bugle never sounds, the army never arrives.

"My nose." Sometimes it's a statement of resignation. Lying on the couch with his handkerchief on his belly, handy you know, he groans, "My nose." Other times, it's a declaration of war, especially when he is trying to do something which requires concentration, like repair the lawn mower. He squats beside the machine, threading a screw the size of a flea, his eyes watering, face crimson and swollen. Suddenly, with no more warning than would accompany an alien invasion, he slings the screwdriver across the yard, leaps to his feet, digging in his hip pocket for his handkerchief like it's a scorpion stinging his butt. He blows. He lifts his countenance to the heavens. He bellows, "My nose!"

I am six years old, Dad is trying to get the chain back on my bicycle. I am such a delinquent for allowing it to come off in the first place. Dad grumbles. I see a drop of clear liquid descend from his nostril and hang there like a pendant an aborigine might wear. I silently retreat a few steps. He sniffs, wipes with his sleeve, sniffs again, grumbles a curse to the creator of such an inanely-designed apparatus as the human nose. He blinks his eyes rapid-fire, yanks on the chain a couple more times for show. And then the nose is in control. Dad roars like a wounded grizzly, snatches the bike over his head and heaves it down the driveway. Out comes the scorpion. He blows. Birds take flight, small mammals urge their young deeper into their burrows, folks all over town look at their watches and wonder why the noon siren's blowing at ten-twenty-five. The blast echoes off the watertower to accompany his anguished cry. "My NOSE!!!"

My mother talks to her doctor about it. She misunderstands him and tells everyone, "Jerry has a deviant septum." she brings home brochures, puts them in his lunchbox. Like he needs reminding.

It is the summer of my ninth year, we are vacationing in Florida. Mom wants to visit Cypress Gardens. Dad is reluctant. "What about my hay fever?" Mom opens her purse: inside is enough Contac and Triaminic to fill a beanbag chair. Interstate transport violations and border seizures flood my mind. I picture the five of us—me, Mom, Dad, and my little brother and sister—assuming the position along the side of the highway, traffic slowing to a crawl, the contents of Mom's purse strewn on the ground, photographers taking pictures of the stash.

We go on to Cypress Gardens. Before we have parked the car, Dad is well on his way to being inducted into the hay fever hall of fame. "My nose."

Mom breaks out the medicine. "Here, take these." She even has one of those plastic collapsible cups and a thermos full of orange juice. She really wants to see Cypress Gardens. "They won't help," Dad says, gulping them anyway. They don't.

I remember it as a day of wrath and embarrassment. Dad's nose was in total control of our itinerary. Mom and us kids wanted to see the ski show, Dad's nose wanted to go home. We wanted to eat lunch in the picnic area beneath the weeping willow trees, Dad's nose threw a fit and asked us if we were all out of our minds.

I walk the winding paths, head down in shame, as Dad heckles the groundskeepers.

"Keep it up. Kill us all! You probably never had to use a vaporizer in your life!" He approaches total strangers and asks if they have a pocketknife on them. "My nose!" he wails, to the strangers' complete horror. "Remove my nose from my face! Just lop her right off. I'm dying here. Put me outta my misery."

Getting to Florida in the first place was almost as much fun as being there. I never got much sleep the night before the big trip, I was too excited by the prospect of sixteen hours in the Buick—counting cows, breathing on my little brother and sister, peeing in a paper cup. "Your father won't stop unless he sees a Stuckey's," Mom says, nudging me out of bed at four AM, the departure time which Dad—in what must be a little preview of senilities to come—has decreed. "Do you have to go to the bathroom?" I shake my head and yawn. "Go anyway," Mom says. "There's not a Stuckey's until Chattanooga." Chattanooga is seven hours down the road.

When Dad dies, they're going to put his bladder in the Ripley's Believe It Or Not! museum. Ron Powell, of Benton, Kentucky, had a bladder so durable, he whizzed only once in his entire life...at a Stuckey's outside Chattanooga, Tennessee. Believe It Or Not! I stand over the toilet, swaying, still half asleep, and manage to wake my bladder for one feeble squirt, after which it turns over and refuses to budge till morning (when, no doubt, we will be at the precise mean distance between home and Stuckey's of Chattanooga).

Dad is sitting in the idling Buick, reading the map by the dome light. Mom is still ironing clothes. She has told us—my brother, sister, and me—to gather up any toys or books we want to take. We take that as a cue to start dismantling the swing set. We each begin to fill a pillowcase like an evacuation has been ordered. When Dad sees us staggering to the car with our freight, he vetoes the entire operation, and we collapse to the ground, hysterical. Tantrums, threats, charlie horses, tears, bloodied noses, spankings, groundings, compromises. We haven't even backed down the driveway.

Dad always packed the car like it was a spacecraft carrying delicate, expensive experiments and NASA would be inspecting for wasted space. He loaded each item according to size, weight, tensile strength, and so forth, which was all well and good except Mom prepared these items for packing in no particular order whatsoever. An ironing board might follow a bag of baloney sandwiches, a pair of shoes might precede a steamer trunk. How many launches were aborted at T-minus two seconds because Dad's internal computers had detected a suitcase had shifted half a micron when he slammed the trunk lid? How many vacations did we take?

1974. I'm eleven. My brother's eight, my sister six. It's after five-thirty. We've been sitting in the car for forty-five minutes when Dad slings his door open to rearrange our cargo for the third time. Mom grabs his arm and tells him that if he doesn't get on the road that second she's going to rip up the traveller's checks. Dad gapes at her a moment then slams his door, stomps the accelerator, and backs over the three-foot dogwood tree he nursed all winter. He doesn't even get out to survey the carnage, so fearsome is his fury, so plump and red are his cheeks. Twenty miles down the road he pulls over and unloads everything onto the shoulder of the interstate. There we sit with our tennis shoes and toiletries, floats and flip-flops in a ring around the car for the world to see, semi-tractor trailers blowing past like sudden angry storms, Samaritans slowing and signaling—Need a hand?—and Dad waving them on with a scowl.

We spent the night forty-five minutes from our doorstep. In the motel, my sister, my brother, and I sit on the edge of the bed. Dad gives us the bad news: "This room cost me fifty-six dollars. You can just forget about going to Disneyworld." The three of us, normally about as compatible as first-graders and flamethrowers, pull together for the common cause.

Dad! Not Disneyworld! Let's skip St, Augustine, instead. Cut back on souvenirs. Hey, I know! Us kids won't beg for anything the whole trip! Dad isn't buying it, so we resort to the only truly effective weapon in our arsenal—we pout. We fight over the TV, stop up the commode, open the camera and ruin the film, knock the nightstand off the wall, break the door on the ice machine, and, on the way to the pool—where I believe Dad is taking us only so we can drown each other—we top off the evening by dropping the car keys in the crack between the elevator and the hall floor where they clink and jingle for a horrifying amount of time before falling out of earshot somewhere in the catacombs below Howard Johnson's. Dad roars, sends us squalling back to the room, dragging our HoJo towels behind us—"I don't even wanna catch you watching TV!"—and stomps off to find the manager. Mom can't quiet us, we're inconsolable, grief-stricken. "You said we could swiiiiim. You saaaiiid!!"

That night, Dad's nose tried to call a family meeting. He never could sleep in a motel. "Is it my imagination or is there enough dust in here to put in an acre of soybeans?" But the rest of us were sleeping like stones; we'd been up since four AM the night before and had put in a good day of insubordination to boot. Even Mom rolled over and told him to take a pill. Dad would just have to deal with his nose alone this time. We were on vacation.
```

---

## IC-2169: 1,000-Year-Old Ghosts

- Title: 1,000-Year-Old Ghosts
- Author (byline): Laura Chow Reeve
- Work: PEN America Best Debut Short Stories 2017
- Publisher: Catapult
- Publication date as stated: Aug 2017
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: KATIE, POPO, MOM, GUNG GUNG, POPO’S MEMORY
- Teaser before the introduction: Yes
- Spoken words (computed): 1504
- Already set (do not supply): none

### Source block (context only)

```text
Author: Laura Chow Reeve
Book: PEN America Best Debut Short Stories 2017
ISBN: 978-1936787685
Publisher: Catapult
Date (Month/Year): Aug 2017
```

### Introduction (context only: never use it for content warnings)

```text
Forgetting is often the only way to survive, and it's almost inevitable due to the transitory/refugee nature of so many of our histories. But it has its price. 1,000-Year-Old Ghosts by Laura Chow Reeve is a beautiful, magical story about 3 generations of women wrestling with their painful memories. It highlights how many immigrants and those descended from them wrestle with the paradox of both wanting to hold on to the experiences that have made them and wanting to forget the pain that these memories have caused.

1,000-Year-Old Ghosts by Laura Chow Reeve
```

### Performance text (classify this)

```text
KATIE: Popo taught me to pickle memories when I was thirteen. It’s just like cucumbers, radishes, cabbage. I learned to cut them into even squares. Memories cut like apples; the knife slides through their protective skin with a crisp snap. I packed them in jars filled with salt, sugar, vinegar, and water. Adding herbs and spices can distort, make them harder to swallow.

POPO: It’s a family secret. It allows you to forget.

KATIE: Forget what?

POPO: Anything. Forgetting does not come easily to the women in our family. We have our jars.

KATIE: What are we trying to forget, Popo?

POPO: So many questions. Chop this into smaller pieces.

KATIE: We started with minor moments: (1) When I dropped my underwear on the floor of the changing room after swim practice at school and Abigail Kincaid picked it up and showed the whole class. (2) The time I tugged on a strange woman’s skirt in a Costco checkout line because I thought, for a second, that she was my mother. (3) A recurring nightmare of being alone in an abandoned building with no way to get out. After the lids were tightened . . .

POPO: How do you feel?

MOM: Ma, why are you teaching her that?

KATIE: It was a grey Sunday morning. It had been a bad week and I didn’t want to remember any of it.

POPO: Because you won’t.

KATIE: Do you have your own jars, Mom?

MOM: No.

KATIE: Like Popo, my mother was good at shutting down conversations. There were so many times that she felt far away. My arms could never quite reach her.

POPO: That’s not true, Anne. We made you one or two when you were younger. You remember that.

KATIE: Mom wasn’t looking at either of us. She was still holding a paper napkin she had used at breakfast. She was trying to smooth out the creases with her fingers. She opened her mouth to say something, but hesitated.

MOM: (with tears in her eyes) I’m sick of this. How come you decide what all of us remember or forget? You know what, Ma? I remember everything.

KATIE: My mother went through my room to find and display my jars on the kitchen counter. They confronted me when I got home from school, my mother and my jars.

MOM: I know Popo thinks this is best, but memories are important even when they are painful. I’m concerned about you. Both of you.

KATIE: I’m fine, Mom. Popo is fine.

MOM: She’s not fine. I know she thinks she can control these things, but she can’t. Her short-term memory is getting worse. She forgets where she puts things, she doesn’t show up to appointments, she can’t even tell me what she had for breakfast some days. Popo isn’t fine.

KATIE: As I got older, I filled my jars with the things I had been holding onto. It was a feeling larger than relief -- a space to put myself away. (1) I chose to forget the white woman at the grocery store who told me I was prettier because I wasn’t full Chinese. “You’re so lucky,” she said. (2) I chose to forget how my mother looked after the spindled cancer cells settled into her body. (3) I chose to forget the woman on the bus who spoke to me in Cantonese, and how I did not know how to respond. I searched for words that someone should have taught me, and I couldn’t find them anywhere. (Beat) Popo never warned me not to let it become a habit, a practice, a daily ritual. Mom wasn’t around to count my jars, display them, remind me of things I had already forgotten, witness my slow dissolve. My jars overflowed and spilled onto my hands until they stung. (Beat) [PoPo] drank a glass of saltwater every night before her evening prayers. When I asked why, she said it was a leftover habit from when my Gung Gung (grandfather) would travel.

POPO: He died on his way back to China. Did you know that?

KATIE: You told me.

POPO: I just wanted to make sure you didn’t forget. (Katie opens one of PoPo’s jars)

POPO’s MEMORY: He is dying but refuses to die in America.

GUNG GUNG: I am going home. I cannot be buried here.

POPO: You are leaving me here. What am I supposed to do without you? What about Anne?

GUNG GUNG: What does it matter? I am dying either way. You don’t want my ghost to haunt you. It’s better for both of us if I go. To guarantee that she is not haunted by her dead husband, she stuffs most of what she has of him into thirty-seven glass jars. She only leaves enough to tell her future grandchildren (1) his name, (2) his occupation, (3) where he was born, (4) where he died.

KATIE: Popo? What do you put in your jars?

POPO: I don’t remember. That is their purpose.

KATIE: But aren’t there things you wish you hadn’t forgotten? I asked. She looked at me for a long time before she answered. (Katie opens one of PoPo’s jars)

POPO’S MEMORY: She never asks him about futures where he does not come back. She prays that he returns to her. He travels back and forth between their apartment in San Francisco and Southern China. It is rare to have a husband whose body tastes like the Pacific Ocean. It is rare to have a husband made mostly of salt.

POPO’s MEMORY: The street outside their apartment is loud the way city streets tend to be. It drifts in through the open windows of their front room, and she lets it fill up the space he left behind. When he comes home, he shuts the windows and says he is tired of loud noises. He tells her how the ocean roars and the wind cracks. He tells her he has been looking forward to the silence of home.

POPO: (softly) No. Sometimes I think there are not enough jars in this city for me to fill. Anne, grab me the measuring cups.

KATIE: Popo. I’m Katie. Anne was my mother. (to audience) Her eyebrows furrowed. The symptoms my mother had witnessed in Popo years before had only gotten worse. She was shriveling. (to PoPo) Please stop. This is making you sick. (to audience) She continued to measure and chop; she licked her index finger, dipped it into a bowl of salt in front of her, and then popped it back in her mouth to taste.

POPO: I’m close.

KATIE: Close to what? What else could you have to forget?

(long silence)

POPO: I love you, but I wish I remembered how to say it the other way. (she begins to cry) There was a way I used to say it. I don’t remember the words. I used to say it to someone. Do you remember?

KATIE: No, Popo. I don’t. (to audience) She finished dissolving seven years after mom died. By the end, her slow pickling process had picked up speed. Everything I loved became smaller and smaller until she started to break apart in my hands. My memory was shaky. Most of the water in my body was salt. I no longer had difficulty forgetting; it came easily with or without a jar. Remembering was harder. (Beat) As I packed up her home, I looked for all the places that Popo had put herself to rest. I went through all of her drawers, her closets. I took every lid off of every box. Jars were hidden everywhere. She was right. There hadn’t been enough jars in the city to hold everything she needed to put down. (Katie opens one of PoPo’s jars)

POPO’s MEMORY: She is less lonely now that she has Anne. She has something to hold onto when she walks through Chinatown. She used to think that she would float away with nothing solid to hold her down. Now she walks with purpose. She teaches Anne how to say apple and block in English. She does not talk to her in Cantonese. When she does not know the word she is looking for in English she says nothing.

(Katie opens another of PoPo’s jars)

POPO’s MEMORY: Every time he comes back, he feels more foreign. He says “néih hóu ma,” (some snow today) but she responds in English.

GUNG GUNG: One day Anne’s children will not know how to speak our language.

POPO: Maybe that will be for the best. They will stop longing for things they cannot have. There will be no reason to leave. Not everyone can live in between things. Not everyone can survive being split into two. There are fish that die in saltwater.

KATIE: I pulled on the [next] lid, but my hands kept slipping. I was too weak or the jar was too strong or whatever was inside didn’t want to be taken back. I threw it against the wall. The glass shattered, the liquid dripped to the floor, the memory clung to the paint. Its smell surprised me— orange peels and baby powder. Popo was holding my mother’s head in her lap, pushing her hair back with her hands, cooing to her softly. One by one, I opened the rest of them. Sometimes they smelled rancid, like death. These were ones of her travels from China, her first few years living in San Francisco, my mother’s sickness and funeral. Many of them smelled like the ocean, like Gung Gung’s seawater breath, like the smells that made up her heartbreak. The ones of me smelled like vanilla yogurt and strawberries . . .
```

---

## IC-2170: 1944

- Title: 1944
- Author (byline): Ellen Gilchrist
- Work: Ellen Gilchrist: Collected Stories, Pg 58-62
- Publisher: Back Bay Books
- Publication date as stated: Dec 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: PIANO TEACHER, MOTHER, FATHER, DORIS, RHODA, RHONDA
- Teaser before the introduction: Yes
- Spoken words (computed): 1249
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ellen Gilchrist
Book: Ellen Gilchrist: Collected Stories, Pg 58-62
ISBN: 978-0316193658
Publisher: Back Bay Books
Date (Month/Year): Dec 2001
```

### Introduction (context only: never use it for content warnings)

```text
Every combatant nation had musicians willing to contribute what they could to the war effort. In the United States, everyone from Frank Sinatra to Leopold Stokowski gave War Bonds concerts and made recordings exclusively for the armed forces. Jazz leader Glenn Miller lost his life en route to play for troops overseas, and cornetist Jimmy McPartland landed on D-Day with the U.S. infantry. The music of the war effort was equally as inspirational to the families of the troops left behind. Come with me to a local pub and you’ll see how a young girl and an older woman escape the tragedy of the war for a moment and revel in the power of music during this time of turmoil.

1944 by Ellen Gilchrist
```

### Performance text (classify this)

```text
(Pg 58-62) When I was eight years old, I had a piano made of nine martini glasses. I could have had a real piano if I had been able to pay the terrible price, been able to put up with piano lessons, but the old German spy who taught piano in the small town of Seymour, Indiana, was jealous of my talent.

PIANO TEACHER: (in a guttural accent, rapping the speaker’s knuckles with a stick) Stop it! Stop it! Stop it! Stopping this crazy business. Can’t you ever listen? Can’t you sit still a minute? Can’t you settle down? God knows I tried to settle down. But the mere sight of the magnificent black upright, the feel of the piano stool against my bottom, the cold ivory touch of the keys would send me into paroxysms of musical bliss, and I would throw back my head and begin to pound out melodies in two octaves.

PIANO TEACHER: Stop it! This is no music, this crazy banging business. Stop on my piano. Stop before I call your momma!

I remember the day I quit for good. I got up from the piano stool, slammed the cover down on the keys, told her my father would have her arrested, and stalked out of the house without my hat and gloves. It was a cold November day, and I walked home with gray skies all around me, shivering and brokenhearted, certain the secret lives of musical instruments were closed to me forever.

So music might have disappeared from my life. With my formal training at this sorry end, I might have had to content myself with tap and ballet and public speaking, but a muse looked down from heaven and took pity on me. She arrived in the form of a glamorous war widow, was waiting for me at the bar when I walked into the officers’ club with my parents that Saturday night. There she sat, wearing black taffeta, smoking long white cigarettes, sipping her third very dry martini.

MOTHER: Isn’t that Doris Treadway at the bar? I can’t believe she’s going out in public.

FATHER: What would you like her to do, stay home and go crazy?

MOTHER: (whispering) Well, after all. It’s only been a month. “Do you know that lady?” I asked, wondering if she was a movie star. She looked exactly like a movie star.

MOTHER: She works for your daddy, Honey. Her husband got killed in the Philippines.

FATHER: Go talk to her. Go cheer her up. Go tell her who you are.

As soon as we ordered dinner I did just that. I walked across the room and took up the stool beside her at the bar. I breathed deeply of her cool perfume, listening to the rustling of her sleeves as she took a long, sophisticated drag on her Camel.

DORIS: (smiling) So you are Dudley’s daughter. I squirmed with delight beneath her approving gaze, enchanted by the dark timbre of her voice, the marvelous fuchsia of her lips and fingertips, the brooding glamor of her widowhood.

RHODA: I’m Rhoda. The baby-sitter quit so they brought me with them.

DORIS: Would you like a drink? Could I persuade you to join me?

RHODA: Sure. Sure I’ll join you. She conferred with the bartender and waved to my parents who were watching us from across the room.

DORIS: Well, Rhoda. I’ve been hearing about you from your father.

RHODA: (worried) What did you hear?

DORIS: Well, the best thing I heard was that you locked yourself in a bathroom for six hours to keep from eating fruit cocktail.

RHODA: I hate fruit cocktail. It makes me sick. I wouldn’t eat fruit cocktail for all the tea in China. “I couldn’t agree with you more,” she said, picking up her stirrer and tapping it on her martini glass.

DORIS: I think people who hate fruit cocktail should always stick together. The stirrer made a lovely sound against the glass. The bartender returned, bringing a wineglass full of bright pink liquid.

DORIS: Taste it, go ahead. He made it just for you. I picked up the glass in two fingers and brought it delicately to my lips as I had seen her do.

RHODA: It’s wonderful. What’s in it?

DORIS: Something special. It’s called a Shirley Temple. So little girls can pretend they’re drinking. She laughed out loud and began to tap the glass stirrer against the line of empty glasses in front of her.

RHODA: Why doesn’t he move the empty glasses?

DORIS: Because I’m playing them. Listen.

She tapped out a little tune. “Now, listen to this,” she said, adding small amounts of water to the glasses. She tapped them again with the stirrer, calling out the notes in a very high, very clear soprano voice.

DORIS: Do, Re, Me, Fa, So, . . . (calling out) Bartender! Bring us more glasses. In a minute she had arranged a keyboard with nine perfect notes.

DORIS: (moving glasses in front of Rhoda) Here, you play it.

RHODA: What should I play? I don’t know any music.

DORIS: Of course, you know music. Everyone knows music. Play anything you like. Play whatever comes into your head. I began to hit the glasses with the stirrer, gingerly at first, then with more abandon. Soon I had something going that sounded marvelous.

DORIS: Is that by any chance the “Air Corps Hymn”* you’re playing?

RHODA: Well . . . yes it is. How could you tell? She began to sing along with me, singing the words in her perfect voice as I beat upon the glasses.

DORIS: (singing) *Off we go, into the wild blue yonder, climbing high into the sky, dum, dum, dum. Down we dive spouting a flame from under, off with one hell-of-a-roar, roar, roar… People crowded around our end of the bar, listening to us, applauding. We finished with the air corps and started right in on the army.

RHONDA: **(singing) Over hill, over dale, as we hit the dusty trail, and those caissons go marching along, dum, dum dum . . . In and out, hear them shout, counter march and right about, and those caissons go rolling along. For it’s hie, hie, hee, in the field artill-a-reeeeee. . . A man near me began playing the bass on a brandy glass. Another man drummed on the bar with a pair of ashtrays. Doris broke into “Begin the Beguine.”

DORIS: *** When they begin the beguine, it brings back a night of tropical splendor. It brings back the sound of music to te-en-de-rr. It brings back a memorreeeeeee ever green. A woman in a green dress began dancing, swaying to our rhythm. My martini glasses shone in the light from the bar. As I struck them one by one the notes floated around me like bright translucent boats. This was music! Not the stale order of the book and the metronome, not the stick and the German. Music was this wildness rising from the dark taffeta of Doris’s dress. This praise, this brilliance. The soft delicious light, the smell of perfume and gin, the perfection of our artistry almost overwhelmed me, but I played bravely on. Every now and then I would look up and see Doris smiling at me while she sang. Doris and I were one. And that too was the secret of music. I do not know how long we played. Perhaps we played until my dinner was served. Perhaps we played for hours. Perhaps we are playing still.

RHONDA: Oh, just let them begin the beguine, let them plaaaay . . . Let the fire that was once a flame remain an ember. Let it burn like the long-lost desire I only remember. When they begin, when they begin, when they begi-i-i-i-i-i-in the begui-i-i-i-ine. . .
```

---

## IC-2171: After the Wink

- Title: After the Wink
- Author (byline): Carolyn Steele Agosta
- Work: After the Wink and Other Stories
- Publisher: Carolyn Steel Agosta
- Publication date as stated: Dec 2011
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1793
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carolyn Steele Agosta
Book: After the Wink and Other Stories
ISBN: 978-0982956120
Publisher: Carolyn Steel Agosta
Date (Month/Year): Dec 2011
```

### Introduction (context only: never use it for content warnings)

```text
You know, sometimes a wink is really just a nervous tic, a sudden twitch of muscles contracted in error by a misguided neuron, an accident of synapses gone awry. The muscles keep twitching until something clicks over and they smooth out, like a skip in an old 45 rpm record, and everything goes back to normal. After the Wink by Carolyn Steel Agosta.
```

### Performance text (classify this)

```text
(Pg 1-7) It starts out so harmlessly. I don't really mean anything by it, I'm just in one of those moods. I mean, when you're 42 years old and have 3 kids and a husband and responsibilities, who figures on finding excitement, too? Other than bad excitement, like when you have to hit the brakes hard and all your blood vessels get a quick yee-ha.

It's true, I've been noticing men a lot lately. Their arms, particularly. Don't ask me why, but I've suddenly become fascinated with men's arms. Forearms, lightly furred, with those lines of tendons and the swell of muscle below the elbow that women just don't have. And men's hands, square and capable. I see them everywhere. In restaurants, at gas stations, in the middle of the aisle at the freakin' K-Mart, for god's sake. It's embarrassing to know I'm lusting in Lawn & Garden.

It's not just the young men either, mind you. I've been noticing older men, too. Men in their 40's and 50's, men who maybe think no woman is looking at them that way anymore. Mostly I like the ones who still have plenty of hair and rugged looking faces, who look like they still get some, you know? Ponytails too, on older men, catch my attention. Here's a guy who thinks young, I figure. I could be wrong. Maybe he's just a guy who hates going to the barber.

Anyway, I'm sitting there at the coffee shop, I'm reading a book by Robin Hemley and it makes me laugh out loud. I look around to see if anyone notices and there's a man smiling at me. He's good-looking too. He's sitting at one of the tables, reading a magazine, and it's not just any magazine, not about motorcycles or computers or entertainers, it's the New Yorker. The guy's literate, for crying in the sink.

I give him a little smile. Going back to my reading, I shift in my seat, cross my legs, straighten my back a little. Knockers up, my aunt used to say. I rest my chin on my hand, arching my neck a little. That's body language for "I'm interested". Or something like that. A customer near the front makes a huge mess by dropping her coffee, the tray clattering to the floor. I take a quick glance at Mr. Attractive and he's looking at me. So I smile. And then, God help me, I wink.

Now it's just a little wink, just an acknowledgement that he's there and I'm there and we both see the humor of the situation and that, perhaps, we're somehow both a little more in the know than the average joker and already have this little connection, but that's all it is. I swear. But it's enough.

Because next thing I know, he's picking up his coffee and his New Yorker and he's coming over to me, doing that little raised eyebrow thing to ask if he can join me and I'm nodding, nodding, thinking I don't quite believe this. He asks me about my book and I ask him about his magazine and I mention, modestly, that I'm a writer and he mentions, modestly, that he's a musician, and even though we're really a bookkeeper and a systems analyst, we understand that we're not defined by our paying jobs. I tell him my name and he tells me his and it's one of those names I always admired. He has a little bit of curly black/grey/white hair coming out of the collar of his shirt. His eyes crinkle at the corners and his forearms flex as he leans forward on his elbows to talk to me in low tones that require that I lean forward too. I smile to show my dimples and hope that I don't have coffee breath and we keep talking. About books and music and the theatre. About the way that parking is getting impossible in this town and how traffic is ridiculous. He mentions that he lives near South Park and I mention that I'm over by the university and pretty soon our coffee is cold and it's somehow gotten to be an hour later.

It's really time for me to leave and he walks me to my car, which thank heavens is decently clean, with no McDonald's Happy Meal figures on the front seat. He mentions that he's going to the poetry slam next Friday because his friend is playing flute for some poet and I mention that I've never been to a poetry slam and he says I should try it. So I say maybe I will and I drive away with my hands perspiring on the steering wheel.

I have no complaints about my husband, that has to be understood. He's loving and thoughtful and sexy and he picks up his socks and puts down the toilet seat. But on Friday night I'm at the damn poetry slam, trying to look like I'm enjoying it but really keeping an eye out for Mr. Handsome only I don't see him and feel like a fool and I'm just getting ready to leave (I mean it, I'm only giving it five more minutes) when he walks in. And he winks at me.

The place is crowded and noisy, people are talking to each other and completely ignoring the woman in purple tights and purple hair who is bellowing some poem about spaghetti, and when he takes my elbow and leads me away to a quieter corner, a little thrill runs right up my arm. He asks if I want to get out of there and I nod and suddenly my knees are way too loose and I'm afraid that if I walk, they'll bend backwards, the wrong way, which would not be attractive at all.

I manage to pull myself together and we get in our cars and I follow him to a bar, which is quiet and low-lit and has a nice band playing oldies. We talk and dance and his arms go around my waist, which has mostly been used to apron strings and babies' monkey legs and my husband's arms. Which are also nicely hairy and brown and have those good flexy muscles. Which I'm trying not to think about just like I'm trying not to mention that both Mr. Gorgeous and I are wearing wedding rings. Because we are, and we're not kidding ourselves that this is anything but an exercise in visibility.

You see, it seems to me that after 40, you become invisible. Oh, you're still there and people see you but they don't really SEE you. They see this person whose daughter is now an adult and whose mother is now a child and who's supposed to hold everything together. A person who couldn't possibly have desires and doubts and unfulfilled longings. A person who is still, improbably, perhaps imperceptibly, a person.

I take a good look at Mr. Still-Has-It and I can see that he still loves rock'n'roll and still would look good behind the wheel of a Corvette and still has a bit of anxiety about how he looks to a younger woman. Which I am, to him. So I smile and flirt and he flirts back and it feel real good. We dance and I think about how strange it is to be in the arms of someone else, another man, a man who is a bit taller and bulkier than my husband, with a different voice and different lips and different eyes. It feels so weird, and then it feels even weirder when he kisses me, which he does, right there in the middle of the dance floor. I haven't kissed another man on the lips in over 20 years and now his mouth is on mine, and it's different, a different touch and taste and style. More than that, it's real, I'm really here and I'm doing this thing.

I start to shake, start to vibrate like a tuning fork, until he probably thinks he's such a good kisser. I'm just shaking with fear because I realize that I'm thinking about a lot more than kissing and that scares the hell out of me. He laughs a little, softly, in a pleased sort of way, and I blush all the way to my fingernails, and we go back to the table. He's looking at me and I think, yes, look at me. I'm not ready to be old, to have all my fun behind me. I want to shimmy when I dance, and wiggle when I walk. I want a man to look at me and get a little yee-ha of his own.

Then I begin to think that maybe this is why people cheat in the first place. To have this warm glow that comes from someone else's eyes. To remember who they are and not to be the person that everyone thinks they are and, a little bit, not to be the person they know they are.

I look at him too. I see a man who's just as scared as I am of becoming invisible. Or being seen as past it, on the far side of manhood, as being old. So I reach across the table and take his hand (good hands, wide and blunt-fingered, the hands of a man who can fix things). I stroke his wrist and tell him without saying it that he's still pretty sexy-looking and makes my mouth water. I think about all the things I've never done and all the things I'll never be, and I wonder if it's too late.

A rush goes through me, starting with my lips, making them feel warm and full, and I think, damn, what a hell of a time for my first hot flash. But it's not a hot flash. It's the realization that I'm not going to do a thing. Because among all those things I wanted to do with my life, this wasn't on the list.

I give Mr. It-Might-Have-Been a quick kiss on the cheek. I'll have daydreams for a while about him, play with thoughts that should send me to confession, and keep the memory of his kiss for those days when I can't jump-start my own desires. I drive home and sit for a moment in the car, looking up at the light in the bedroom window.

You know, sometimes a wink is really just a nervous tic, a sudden twitch of muscles contracted in error by a misguided neuron, an accident of synapses gone awry. The muscles keep twitching until something clicks over and they smooth out, like a skip in an old 45 rpm record, and everything goes back to normal. The way it should be, I guess. The way it is. The way the music plays best.
```

---

## IC-2172: Aimee

- Title: Aimee
- Author (byline): Mary Beth Miller
- Work: Not specified
- Publisher: Dutton
- Publication date as stated: May 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ZOE, AIMEE
- Teaser before the introduction: Yes
- Spoken words (computed): 1688
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mary Beth Miller
ISBN: 978-0525468943
Publisher: Dutton
Date (Month/Year): May 2002
```

### Introduction (context only: never use it for content warnings)

```text
Aimee by Mary Beth Miller
```

### Performance text (classify this)

```text
ZOE: I don’t know if I can [talk] about what happened and come out whole – alive. I don’t know if I can look back. Besides, if I tell it, who will listen? No one believes us – the kids, that is. They all think we have it so great and that this is the best times of our lives. When people tell me that, I want to puke. If this is the best time of my life and I’m going to spend the rest of my life looking back at this, then I should just end it all right now. (long beat) Oh, Aimee, I didn’t mean that. . . I’ll start with the way it was. . .

ZOE: She stared out the window and blew a long trail of smoke that floated from her lips to her hair, then spread into the air, thin curls of smoke heading for the crack in the window. (to Aimee) Is it worse lately?

AIMEE: What?

ZOE: You know

AIMEE: Say it.

ZOE: (to audience) I froze, unable to speak and stared at her. Even then I couldn’t say the important things. I couldn’t face ugly truths. Aimee had never really been explicit about what happened in her house. She dropped hints, but she never said outright what was going on. She and her stepmother didn’t get along, that I knew. In front of people, her stepmother was as nice as sugar, but I had always known she abused Aimee. But now, as I looked at Aimee’s eyes – her cheeks – her shaking hands, I wondered if I knew anything.

AIMEE: What do you want to know? The details?

ZOE: No, Aimee. I thought she knocked you around. Hit you, stuff like that.

AIMEE: Yeah, she does if I don’t do what she says.

ZOE: Does she say mean things?

AIMEE: Don’t all parents?

ZOE: Aimee, don’t you want to talk about it?

AIMEE: You know what I want to talk about? I want to talk about my cat. And you know what? No one wants to talk about her. ‘She’s just a cat.’ ‘You can get another one.’ No one says ‘Wow! You and that cat go back a long way. She remembers what it was like before, when your real mother lived with you, when your dad didn’t walk around with blinders on, when you knew you were safe in your own bed. She slept with you night after night . . . soothing you even when your parents fought. And when your mother left? When she ran off? Did your cat try to tell you that everything would be okay? Did she act like nothing bad had happened? Tell me that!

ZOE: (to audience) She stopped, her shrill voice echoing. She looked at me for a long time before she fell against me and cried. I rubbed my hands up and down her back. She rocked with me a while, then she stiffened.

AIMEE: (stiffening) Don’t touch me.

ZOE: Her voice came from some inner place I had never glimpsed. (to Aimee) What does she do to you, Aimee. Tell me. (to audience) She needed to say it. Her eyes were hollow, empty of feeling. There was something dead inside her, something cold and frozen that never felt the heat of anything. She hid it most of the time. But it was the only thing in her eyes when I asked my question.

AIMEE: Nothing that unusual. Lots of girls do it. It helps them when they get married.

ZOE: (to audience) She sounded strange, so far away – not in distance, but in time. She sounded young, childlike. Images I’d never dreamed of tumbled from her lips, of her stepmother and her . . . “games.” “Games” she called it when Aimee was young, then “preparation.” Now she used threats – that she’d tell Aimee’s dad about it, that she’d touch her brother like that. Threats Aimee knew were real. Because Aimee had seen her destroy her family, had seen her drive her mother away across the county, had seen her steal her brother’s affection from her, had made Aimee into a problem child for her father. And all the while her stepmother remained an icon of her church, her community her family.

No one would believe Aimee. Not a soul. Things like that don’t happen. Things like that never happen, especially in families like theirs. There was no physical proof. There wouldn’t be semen to test for. Was there any way to test for female stuff? Secretions? Probably, but that would mean telling, and Aimee’s empty face told me that she wasn’t going to do that. (to Aimee) So what do we do?

AIMEE: What I’ve been trying to do all along. Die.

ZOE: (to audience) My mind always stops when I remember her simple response . . . “Die.” It’s too hard to face. I didn’t have the energy for this, not tonight, not ever. I pulled the spread off the other bed and covered her up. “Sleep,” I said. I turned off the light and lay down on the empty bed. Her breathing slowed, then became inaudible. She fell asleep. I climbed under the covers of my bed and allowed myself to sleep . . . . .

I woke to see Aimee creeping back into the room.

AIMEE: I’m scared. I’m scared . . .

ZOE: Everything will be fine.

AIMEE: I don’t think I could have come this far without you as my friend. Will you stay with me tonight? One last time?

ZOE: (to audience) Something inside me jerked awake, something I had let sleep – warning lights, sirens, bells, everything started clambering in my jittery mind. (to Aimee) What do you mean, Aimee? One last time?

AIMEE: I need to end it, and I can’t. Not without your help. Not without you here. It’s so dark and scary doing it alone.

ZOE: No, Aimee. Not that. You’re my best friend. I can’t live without you. I’ll help you live . . . not here . . . if that’s what you want. I’ll support you any way I can. Tell them I’ve seen her come for you. Tell them I’ve seen her beat you. Tell everyone about what happened until they believe it, but I need you alive. Aimee, your dad will be home tomorrow, and we’re going to tell him what’s going on. You won’t have to tell him, I will. I’ll support you one hundred percent.

AIMEE: Then support me how I want you to support me. I can’t do it your way. I’m tired. Tired of everything . . . I have to sleep. But you have to stay with me so I can do this.

ZOE: No, I will not help you kill yourself. (to audience) I still didn’t at that point have much of a clue about what exactly she was talking about. Did she mean help her slice her wrists? Hold her hand while she did? Watch her die? I’d check the bathroom for razors now. (to Aimee) I’m going to the bathroom.

AIMEE: Bring me the bottle on the sink . . . I want to take something.

ZOE: (to audience) My mouth went dry. Drier than when she had asked me to help her die . . . (to Aimee) What bottle?

AIMEE: Bottle on the sink. Very important. Stepmother should never leave sleeping pills out with kids in the house. Never. (Aimee laughs, a deep gagging laugh)

ZOE: (to audience) I raced for the bathroom. I thought I just needed to hide the bottle, that she hadn’t taken anything or done anything. The mirror over the sinks had been shattered. Mixed with the mirror’s shards were pieces of the drinking glass – she must have thrown it at the mirror. I also saw fragments of what appears to be family photo albums. Every picture of her stepmother had been cut into tiny fragments. There were no pictures of Aimee anywhere. But the bottle was there. I was almost unaware of my tears as I picked it up . . . There was no rattle of pills. (calls out) Aimee! (to audience) She had already taken the pills. I felt devoid of hope. (calls out) Aimee! (to audience) . . . I need to get to Aimee. I needed to get help.

(calls out) Aimee! (to audience) She wasn’t answering. She was lying face down on the bed. Her back rose, fell, rose, fell, but slowly . . . too slowly. I rolled her over and came face to face with despair. A long trail of vomit slithered down the side of the bed. I had planned on making her throw up, but she already had. It was the only thing I knew to do that would slow things down and get some of the drugs out of her system. (to Aimee) Oh God! Oh God! . . . Aimee! How much of this stuff did you take? Answer me! Answer me! (to audience) But she didn’t. She couldn’t. (to Aimee’s lifeless body) Damn you! Damn you for this! (to audience) I raised her head, tried to support her with my shoulder while I cradled her from behind. I tried to make her vomit again. That’s when her bladder let go. Later, I learned that this is a normal part of death when someone takes sleeping pills.

I was screaming, shrieking, moaning. I thought someone would hear me. Some jogger, somebody walking a dog. I couldn’t see the clock. Couldn’t let go of Aimee. She was gurgling now, and I thought I should lay her down. My screams weren’t even making Aimee twitch. I screamed on and on, and eventually, when Aimee’s eyes were fixed and dilated, when she was cold and blue and filthy and beginning to stiffen up in my arms, someone heard. There was a pounding on the door, but I would have had to let go of Aimee to let them in. And I couldn’t. I just kept screaming, incoherent rages against God and county, and everyone in between . . . (in anguish) She’s dead. She’s dead. Aimee’s dead. (to audience) I quit screaming. I waited. I slipped away. I stopped thinking, stopped reacting like a human being. I became still, cold, dead inside. I still feel that way most of the time. . . .

I can’t say mad at Aimee. I want to, but I can’t. She was, is, my friend, and he needed far more than I could give her. I couldn’t or wouldn’t understand what she needed – so maybe’s she’s wherever she is now, screaming silent screams of anger back at me because I didn’t help her . . . But I was scared . . . scared of every sad and angry word she said. It terrified me to imagine her in a coffin and dead and not on the other end of the phone when I needed to talk. So I didn’t think it could happen.

Friends don’t commit suicide. They don’t die.
```

---

## IC-2173: Airmail to the Moon

- Title: Airmail to the Moon
- Author (byline): Tom Birdseye
- Work: Not specified
- Publisher: Holiday House
- Publication date as stated: March 1989
- Event as filed: Prose
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

ORA MAE: Then last Monday, while fetching the mail at the county road, I stuck my tongue out at my pesky neighbor, Merrietta Bean, and gave her a big raspberry like this – PPLLUBB! The vibration from my tongue flapping against my teeth popped that chomper of mine as loose as a goose on ice skates. So I told the world about my first tooth coming out . . . whether they wanted to hear or not. By Thursday that tooth was so wobbly it was just hanging on by one root and a flap of skin. I could push it all the way out between my lips with my tongue and help Mama slop the hogs at the same time.

Then Friday, right after my big brother Bo Dean and my little sister Kelsey Ann got into a fight at the dinner table over whether Arlene Peterson’s pigs really kneel and pray before they eat, that loose tooth of mine fell right out of my mouth – plop – and landed smack in the middle of my spaghetti.

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

ORA MAE: (to audience) That did it! I was so mad I was ready to scream. Nobody really knew what the tooth fairy was up to. And nobody was the lop-eared rascal that stole my tooth. I was just about to pop my cork clean out of Crabapple Orchard. But instead, I just stood there looking at my sister, and . . . (Ora Mae starts crying – loud and wailing) Somebody stole my tooth . . . and when I catch ‘em I’m gonna open up a can of gotcha and send ‘em airmail to the moon. (She sticks her hands down deep in her pockets and a shocked expression comes over her face. She stops crying) My name is Ora Mae Cotton of Crabapple Orchard. And right now I feel like a possum up a plum tree. I’m as embarrassed as a zebra without stripes.

(sheepishly and she hold out her hand) You see, there’s this little hard thing in the bottom of my pants pocket. It’s right where I left it. (beat) I wonder if the tooth fairy ever sends motor-mouth kids like me airmail to the moon?
```

---

## IC-2174: All I Know About Animal Behavior I Learned in Loehmann’s Dressing Room

- Title: All I Know About Animal Behavior I Learned in Loehmann’s Dressing Room
- Author (byline): Erma Bombeck
- Work: Not specified
- Publisher: Harper Collins
- Publication date as stated: Oct 1995
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, HUSBAND, WOMAN, MAN, INSTRUCTOR, WOMAN 2
- Teaser before the introduction: No
- Spoken words (computed): 975
- Already set (do not supply): none

### Source block (context only)

```text
Author: Erma Bombeck
ISBN: 978-0060177881
Publisher: Harper Collins
Date (Month/Year): Oct 1995
```

### Introduction (context only: never use it for content warnings)

```text
Men and women are very different models of the same species . . . How do I know this? Well, my time is limited, so let’s narrow it down to one prime example: Directions.

Observation #1: Women cannot use a map without turning the map to correspond to the direction that they are heading.

Observation #2: Men will not stop to ask for directions: they’d rather drive for 50 miles in the wrong direction than appear to not know where they are going.

And keep in mind this is from the female perspective!!

All I Know About Animal Behavior I Learned in Loehmann’s Dressing Room by Erma Bombeck
```

### Performance text (classify this)

```text
NARRATOR: (Chapter 3) I have just come up with a wonderful solution to end all wars. Let men give directions on how to get there. There is no species on the face of this earth that prides itself more on how to get around than men. Yet most of them are lost their entire lifetimes. They just won’t admit it.

I can always tell when my husband is lost. He starts to dispense guilt.

HUSBAND: Are you sure you read the route number right?

NARRATOR: And as we’re knee-deep in farm animals staring in our windows,

HUSBAND: Did AAA say anything about a detour?

NARRATOR: If you really want to set a man off, tell him to stop and ask someone where you are.

HUSBAND: Why should I do that?

NARRATOR: Because we are lost.

HUSBAND: I am not lost. I just made a wrong turn.

NARRATOR: Same thing. We have passed this gas station three times.

HUSBAND: That’s a good thing. At least it’s familiar.

NARRATOR: To stop and ask someone for directions is to compromise his masculinity.

Despite the fact that men don’t have a clue where they are most of the time, they insist on giving directions to women…a process better known as death by instruction.

I am standing at the door with my car keys in my hand.

HUSBAND: Do you know where you’re going?

NARRATOR: Yes

HUSBAND: I thought not (putting down his paper). You go west on Silver Street for two blocks and then turn north until you reach the highway. At the freeway, go east and . . .

NARRATOR: Now that drives me crazy! He knows I don’t speak compass. Unless you’re talking about the Civil War, north and south have no meaning to me. North is always opposite my right hand and south my left, no matter which way I’m standing. The same with miles. I walked a mile once and it was the longest hour and a half I ever spent, so forget miles. (to husband, begging) Tell me right or left.

HUSBAND: (patiently) I have tried giving you directions in left and right.

NARRATOR: And?

HUSBAND: You have still gotten lost. Let me draw you a map.

NARRATOR: Oh Lord, forget it. Just tell me when I get to the end of the street, which way do I turn?

HUSBAND: North . . . rather right. Then turn right again and if you are blinded by the sun you are going in the wrong direction.

NARRATOR: I always thought the sun came up in the east.

HUSBAND: Not at 4:30 in the afternoon.

NARRATOR: Why do you always try to confuse me? I think you do that to make yourself feel important.

HUSBAND: Why can’t you have a little patience?

NARRATOR: At my age, patience is not a virtue…it’s a luxury. (beat) Wherever lost women gather…at service stations, in obscure corn fields, and on exit ramps . . . we talk about this thing men have about giving directions. One woman told an unbelievable story one day about being lost. She stopped at a service station.

WOMAN: I am trying to find where my son’s baseball team is practicing. I’m looking for Prindle’s Field.

MAN: Prindle’s field is about three miles west of Dake’s Corners off the Hans Expressway using the Mill Road exit. (Strokes chin) You go by two stop signs, make a right at the overhead, and there’s a church on the corner that used to be Presbyterian but was bought out by the Methodists. You take a jog in the road and follow through to a dead end, then turn left and you’ll see a little filling station called Fred’s.

WOMAN: That’s the name of this station. (looking up at sign) Where’s Prindle’s Field?

MAN: That’s what I’m getting around to telling you. You’re there. It’s behind the station.

NARRATOR: The male species has a superiority complex about driving. I wish I had a dime for every joke about woman drivers I’ve been assaulted with. They relish telling about the woman in driving school who consistently flunked her test because she couldn’t be sure which was her right hand and which was her left. Years later she met her old driving instructor.

INSTRUCTOR: So have you ever figured it out?

WOMAN 2: Certainly. I drive every day now. (holding up both hands). Ruby ring, right and diamond ring, left.

NARRATOR: Women have their jokes on men who drive. My favorite is: If a man and a woman jumped off a building at the same time, who would reach the ground first? Answer? The woman. The man would get lost.

Douglass Corrigan never asked for directions. He just announced to a crowd of reporters and cameras in 1938 that he was headed for California, hopped into his monoplane, and to the horror of the people on the ground, made a wide circle and ended up in Dublin, Ireland.

Roy Riegels never asked. He was the USC center who was pitted against Georgia in the Rose Bowl game in 1929. When a Georgia player fumbled, Riegels came up with the ball and started a dash to the goal line. Unfortunately, it was the wrong one. His own man finally stopped him on the three-yard line.

And while we’re talking heroes, Christopher Columbus wasn’t all that swift. Turn the guy around in the Bahamas a couple of times and he couldn’t find America if it was on fire.

You can say what you want about women’s lack of direction, but it was a man who was found by police officer recently, sitting in his car alongside Interstate 8 where it stops at Ocean Beach in San Diego. He had a map in his lap and perplexed look on his face. The motorist told the officer he had come from New Mexico and was looking for Arizona. He said he must have missed it.

I don’t care what they say about animals having great sonar powers and whales showing up in the Baja every year. How do we know they want to go to Mexico? For all we know, they year headed for Hawaii, but the male was too proud to ask directions.
```

---

## IC-2175: All the Bright Places

- Title: All the Bright Places
- Author (byline): Jennifer Niven
- Work: Not specified
- Publisher: Knopf Books for Young Readers
- Publication date as stated: Jan 2015
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: VIOLET, KATE FINCH, MRS. FINCH
- Teaser before the introduction: Yes
- Spoken words (computed): 1219
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jennifer Niven
ISBN: 978-0385755887
Publisher: Knopf Books for Young Readers
Date (Month/Year): Jan 2015
```

### Introduction (context only: never use it for content warnings)

```text
Every 40 seconds someone in the world commits suicide. Every 40 seconds someone is left behind to cope with the loss. And while those left behind often feel they could have -- should have -- done more; a mental illness left untreated, can be all-consuming and create a darkness from which there is no escape.

Theodore Finch experiences extreme highs and unbearable lows. But as he begins to descend into the darkness of bipolar disorder, Violet can’t pull him from the quicksand.

All the Bright Places by Jennifer Niven
```

### Performance text (classify this)

```text
VIOLET: (Pg 316-318) The first text comes in on Thursday. The thing is, they were all perfect days. As soon as I read it, I call Finch, but he’s already turned the phone off and I go to voicemail. Instead of leaving a message, I text him back: We’re all so worried. I’m worried. My boyfriend is a missing person. Please call me. Hours later, I hear from him again: Not missing at all. Found. I write immediately: Where are you? This time he doesn’t answer. Two days later, Finch writes: I am on the highest branch. The next morning: We are written in paint. The next afternoon: The glow of Ultraviolet. The day after that: A lake. A prayer. It’s so lovely to be lovely in Private.

And then everything goes quiet.

VIOLET: (Pg 326-328) On Sunday morning, around ten thirty, Kate Finch shows up at our door. She looks as if she hasn’t slept in weeks.

KATE FINCH: Do you have any idea where Theo might be?

VIOLET: I don’t hear from him anymore.

KATE FINCH: (nodding) Okay. Okay. It’s just that he’s been checking in every Saturday with Mom or me. I mean, every Saturday. We didn’t hear from him yesterday, and then this morning we get this weird email.

VIOLET: She hands me a piece of paper. It’s the email sent at 9:43 a.m (reading aloud) I’m remembering the time we went to Indianapolis to eat at that pizza place, the one with the organ that came up and out of the floor. Kate must have been eleven, I was ten, Decca was a baby. Mom was there. Dad too. When the organ started playing--so loud the tables shook-- the light show started. Remember? It was like the aurora borealis. But what stays with me most is all of you. We were happy. We were good. Each and every one of us. The happy times went away for awhile, but they’re coming back. Mom, forty-one’s not old. Decca, sometimes there’s beauty in tough words--it’s all in how you read them. Kate, be careful with your own heart and remember that you’re better than some guy. You’re one of the best there is. You all are.

(handing back the e-mail – to Kate) I haven’t [heard from him]. I’m sorry. (to audience) I promise to let her know if by some miracle he gets in touch with me, and then she goes away, and I shut the door. I lean against it because for some reason I feel the need to catch my breath.

I go upstairs and turn on the computer and sign onto Facebook. There’s a new message as of 9:47 a.m. The words are written in The Waves: “If that blue could stay forever; if that hole could remain forever; if this moment could stay forever...I feel myself shining in the dark...I am arrayed. I am prepared. This is the momentary pause; the dark moment. The fiddlers have lifted their bows...This is my calling. This is my world. All is decided and ready...I am rooted but I flow. ‘Come,’ I say, ‘come’.”

I write the only thing I can think of: “Stay,” I say, “stay”.

Something is wrong. I pick up the phone to call Kate and realize I don’t have her number, so I drive to Finch’s house. Kate, Decca and Mrs. Finch are there. When she sees me, Mrs. Finch starts to cry.

(Pg 333) The words are written in The Waves, he wrote on Facebook at 9:47 a.m. The water could be the Bloomington Empire Quarry or the Seven Pillars, but I have a pretty good idea where he might be. (to Mrs. Finch) I think he’s gone back to one of the places we wandered, one of the places with water. I can give you directions and tell you exactly where to look for him. (to audience) She turns to me and lays her hand on my arm and squeezes hard.

MRS. FINCH: (pleading) I hate to ask you, but can you go? I’m just so---worried, and---I don’t think I could---I mean, in case something were to---or if he were. (crying) I just really need you to bring him home.

VIOLET: (Pg 334-335) I call my parents to tell them I’ll be home in a while. I drive faster than I normally do, and I remember the way without looking at the map. I am scarily, eerily calm. “If that blue could stay forever; if that hole could remain forever.” There was nothing to make him last.

(Pg 335-336) His clothes on the bank [of Blue Hole] are folded neatly and stacked. I kneel beside the stack of clothes and lay my hand on them as if by doing so I can learn where he is and how long ago he came. The clothes are warm from the sun. (Pg 336-337)

(whispering) Marco. (louder) Marco.

At some point, I know: he’s gone. He’s not somewhere. He’s nowhere. But as I dial 9-1-1, I think: He’s not nowhere. He’s not dead. He just found that other world.

(Pg 352-353) That evening, I torture myself by reading our Facebook messages, going back to the very beginning. And even though he’ll never read it, I open our notebook and start to write.

Letter to Someone Who Committed Suicide By Violet Markey

Where are you? And why did you go? I guess I’ll never know this. Was it because I tried to help? Because I didn’t answer when you threw rocks at my window? What if I had answered? What would you have said to me? Would I have been able to talk you into staying or talk you out of doing what you did? Or would that have happened anyway?

Do you know my life is forever changed now? I used to think that was true because you came in and showed me Indiana, and in doing that, forced me out of my room and into the world. Even when we weren’t wandering, even from the floor of your closet, you showed the world to me. I didn’t know that my life forever changing would be because you loved me and then left, and in such a final way. I’ll never forgive you for leaving me. I just wish you could forgive me. You saved my life. Why couldn’t I save yours?

(Pg 374-375) Something pokes out of the [journal] --a white envelope. I turn the page and someone has written the words, “Then you will shine among them like stars in the sky.” I pick up the envelope, and there is my name: “Ultraviolet Remarkey-able.” Am I ready to hear what he thought of me? To hear how I let him down? My hands are shaking as I open the envelope. I begin to read:

You make me happy. Whenever you’re around I’m safe inside your smile. You make me handsome. Whenever I feel my nose just seems a bit too round. You make me special and God knows I’ve longed to be that kind of guy to have around. You make me love you, And that could be the greatest thing my heart was ever fit to do . . .

I read and reread them until I know the words by heart. (long pause) (Pg 361) I loved Theodore Finch. He went away and I wish he hadn’t, and I can never bring him back, and it hurts, but I like thinking about him. If I think about him, he won’t be completely gone.
```

---

## IC-2176: The Almost Moon

- Title: The Almost Moon
- Author (byline): Anne Sebold
- Work: Not specified
- Publisher: Little, Brown and Company
- Publication date as stated: October 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: HELEN, CLAIR
- Teaser before the introduction: Yes
- Spoken words (computed): 1821
- Already set (do not supply): none

### Source block (context only)

```text
Author: Anne Sebold
ISBN: 978-0742117013
Publisher: Little, Brown and Company
Date (Month/Year): October 2007
```

### Introduction (context only: never use it for content warnings)

```text
Helen Knightly, a middle-aged Philadelphia divorcee, has sacrificed her marriage and family to care for her vicious, mentally unbalanced mother, Clair. Sebold explores the complex ties between mothers and daughters, the meaning of devotion, and the often too-thin line between love and hate.

The Almost Moon by Anne Sebold
```

### Performance text (classify this)

```text
HELEN: When all is said and done, killing my mother came easily. Dementia, as it descends, has a way of revealing the core of the person affected by it. My mother’s core was rotten like the brackish water at the bottom of a weeks-old vase of flowers. She had been beautiful when my father met her and still capable of love when I became their late-in-life child, but by the time she gazed up at me that day, none of this mattered.

HELEN: It was a cool October morning. When I arrived, my mother was sitting upright in her wing chair, wrapped in a mohair shawl, and mumbling to herself. (to Clair) Mother.

CLAIR: (looking up and smiling) Bitch.

HELEN: The thing about dementia is that sometimes you feel like the afflicted person has a trip wire to the truth, as if they can see beneath the skin you hide in. (to Clair) Mother, it’s Helen.

CLAIR: (rudely) I know who you are!

HELEN: My mother looked at me. It was a horrible bottomless look. She pouted first, her lower lip jutting out and then quivering. She was going to cry. I left the room and walked to the kitchen. Whenever I came, I found good reason to spend many of the hours I was supposed to be with my mother in every room of the house but the one in which she sat. I heard the low moan begin that I’d been hearing all my life. It was a moan the notes of which were orchestrated to elicit pity. My father had always been the one to run to her. After his death, it fell to me. For more than twenty years, with greater or lesser diligence, I had been attending to her, rushing over when she called saying her heart would burst, or taking her on increasing rounds of doctors’ visits as she aged.

Late in the afternoon of that day, I was in the screened-in back porch, sweeping out the straw mat. I had left the door open a crack so that I could hear her. Then into the cloud of dust that surrounded me came an unmistakable odor. My mother had needed to go to the bathroom but couldn’t get up. I dropped the broom and ran to my mother. She had not, as I may have momentarily hoped, died and suffered the resultant loosening of bowels. Instead, she sat in her chair, having soiled herself.

CLAIR: Number two!

HELEN: The smell had filled the room within seconds. I walked back to the porch twice to take in huge drafts of dusty air and could think of nothing else but presenting my mother in the way she would have wanted to be seen. I knew I was going to have to call the ambulance. I knew, as I had for some time, that my mother was heading out of this life.

(to Clair) Mom, I’m going to help you clean up, and then we’re going to make some calls. (to audience) Certain as I said it that she did not recognize the name or the daughter who said it.

I knelt down in front of her and looked up into her face. I hated her more than I’d ever hated anyone. Still, I reached up, as if I were finally allowed to touch a precious thing, and ran my fingers down her long silver braid. (whispering) Mom. (to audience) I said it because I knew it would be still in the air. No reverberations, no response.

But the wetness was making her unhappy. Like a snail trapped in sunlight, say — anxious to get away from an element that caused pain. I went from kneeling to half bending over. I placed my shoulders against her shoulders, careful not to put any weight on her. I leaned in like a football player on a tackle and then lifted up. She was both lighter and heavier than I’d expected.

I got her to standing with ease, but once she was upright, she collapsed in my arms. It was all I could do not to drop her, bringing both of us to the ground. As I adapted to the balance of holding her full weight, I could not help but think of my father, how year after year he carried the burden of her, apologized to the neighbors, dried her copious tears, and how this body had folded into his over and over again like so much batter until the two of them became one.

I felt like weeping myself then. I dragged my mother, with her trying, I could feel, to help, over to the staircase leading up to her bath. I questioned my sanity. How, I wondered, did I think this feat was possible? I panted on the carpeted steps but did not give up. I was determined to clean my mother and to dress her in fresh clothes before I called the ambulance.

My mother began to snore. Her head tilted back over my shoulder so that I could see her ancient, mottled face and neck. I looked at her cheekbones, as sharp as they had always been — almost painful now in her cadaverous flesh. Who will love me? I thought, and then banished this question by looking out at the birch leaves in the fading sunlight.

I twisted out from under her, and she moaned like a collapsing bag of air. I sat by her body on the stairs. I had to get out of there, and I thought, suddenly, of the bathtub among the rocking horses in the shed. I left my mother dozing and turned and ran up the stairs, darting into her cluttered bedroom for blankets, and the pink powder room for towels. I noticed the hush in the upstairs hallway and looked at the pictures on the walls, pictures that would soon be gone. I imagined the dark squares they would leave behind them where no sun had reached for years, and the echoes that would resound from the curtain-less storm windows and the thick plaster-and-brick walls. I began to sing. I sang nonsense.

Cat-food commercials and childhood songs, the latter a habit that had been handed down from my mother, a way to stave off the onset of nerves. The need for noise overwhelmed me, but as I headed down the stairs, I grew quiet again. I saw that my mother had slumped down and lay on the floor, her body on the old wine-red Persian rug.

(to Claire) No, Mother, no. (to audience) Realizing that it was more useless than talking to a dog. A dog cocked her head. A dog gave you a soulful look. Why like this? I stood over her body with my arms full of blankets and towels, and I began to weep. I placed the towels on the bottom stair and took my grandfather’s red-and-black Hudson Bay blanket, spreading it out on the floor beside her. Then, so the wool would not scratch, I put a white Mexican wedding blanket down on top of that.

I bent down and put my arms up under my mother’s armpits. Her eyes snapped open.

CLAIR: What on earth are you doing?

HELEN: I blinked. I kept my arms tense. Would she ever be powerless?

CLAIR: (Screaming) Daniel! Daniel!

HELEN: Dad’s not here, Mom. (to audience) She looked up at me, her face dimmed and then reignited again, like a match flaring in the dark. To be that close to her. To be holding on to her and to see her brain open up like that, its scrambled insides, it was all I could do to keep to my task. I placed her body in the blankets and made an open-ended package with her talking head sticking out. Then I rested the towels on top of her chest and breathed slowly, counting to ten before I spoke. (to Clair) We are going on a sleigh ride. (to audience) And in my fists, I balled up the two free ends of the blanket, partially lifting her body off the floor. I heaved her over the carpet of the dining room, in through the kitchen, and out the side door.

CLAIR: Toot! Toot! . . . Toot! Toot!

HELEN: And then she grew silent and stared at the outside like a child in front of flickering Christmas lights. I wanted to ask her: When was the last time you went into your backyard? When was the last time you smelled a flower or trimmed a shrub or just sat in the rusted white iron lawn chair?

Grief was coming heavily now. Something about being outside, being in the fresh air, away from the acrid scent of her and the mothball smell of the closed-up house. My mother lay in her blanketed cocoon on the small, raised side porch, which thankfully was at least partially shielded from the next-door neighbors by vine-covered latticework.

I touched her treasured braid again. Some years ago her hair had passed out of its wiry stage and become soft. It had always been her crowning glory..

Outside, with the air rushing over her, the fecal scent dissipated, and I could think realistically again. I would not make it to the shed. What had I thought? The damage of dragging her down the three steps, of trying to heave her off the porch. And what would I fill the ancient bathtub with? Cold water from the backyard hose? What had I been thinking?

(to Clair) This is it, Mom. This is as far as we go. (to audience) She did not smile or say “bitch” or wail some final lament. I like to think that by that time she was busy taking in the scent of her garden, feeling the late-afternoon sun on her face, and that somehow in the moments that had elapsed since she’d last spoken, she’d forgotten she’d ever had a child and that, for so many years now, she’d had to pretend she loved it.

I wish I could say that she made it easy on me. That she pointedly listed all the sins she had committed during her long life. She was eighty-eight. The lines on her face were now the cross-hatchings of fine old porcelain. Her eyes were closed. Her breathing ragged.

There is no excuse to give, I know, so here is what I did: I took the towels with which I had meant to bathe her, and not thinking that near the latticework or by the back fence there might stand a witness, I smashed these downy towels into my mother’s face. Once begun, I did not stop.

She struggled, her blue-veined hands, with the rings she feared would be stolen if she ever took them off, grabbed at my arms. I pushed down harder. The towels shifted, and I saw her eyes. I held the towels for a long time, staring right at her, until I felt the tip of her nose snap and saw the muscles of her body go suddenly slack and knew that she had died.
```

---

## IC-2177: Amanda and the Wounded Birds

- Title: Amanda and the Wounded Birds
- Author (byline): Colby Rodowsky
- Work: Visions: 19 Short Stories by Outstanding Writers for Young Adults, Pg 78-86
- Publisher: Delacorte Press
- Publication date as stated: Oct 1987
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: AMANDA, MOM, MR. BURNSIDE, RECEPTIONIST, EMMA HART
- Teaser before the introduction: Yes
- Spoken words (computed): 1319
- Already set (do not supply): none

### Source block (context only)

```text
Author: Colby Rodowsky
Book: Visions: 19 Short Stories by Outstanding Writers
for Young Adults, Pg 78-86
ISBN: 978-0385295888
Publisher: Delacorte Press
Date (Month/Year): Oct 1987
```

### Introduction (context only: never use it for content warnings)

```text
Many daughters of emotionally absent mothers spend their entire childhood trying to win their mom's love and approval instead of focusing on themselves. As a result, they grow up not knowing who they are, what they want from life, or even what they enjoy doing. They might feel empty, alone, and aimless, which often leads to anxiety or depression. Can Amanda break through to her mom and have the courage to ask for what she needs, or will her mom’s focus forever be tied to her patients rather than her daughter?

Amanda and the Wounded Birds by Colby Rodowsky.
```

### Performance text (classify this)

```text
AMANDA: (Pg 78-86) It's not that my mother doesn't understand, because she does. In fact, she understands so well, that half the time she goes around with a glazed look in her eyes and forgets to get her hair cut and that we're almost out of toilet paper. She makes her living understanding. You see, my mother is Emma Hart, a psychotherapist, which means that she tries to help people, who call in to her on the radio, find ways of dealing with their problems.

AMANDA: I never will forget that first show. I mean, there was my mother's voice coming out of our kitchen radio, sounding slightly frantic and giving those first callers more than they bargained for. It wasn’t long before people opened by saying, "I didn't think I'd ever get through to you." After only a month on the air the Emma Hart Show went from one hour to two.

Mom really cared about the people who telephoned her, and almost from the beginning she was calling them her "wounded birds." Not on the air, of course, and never to anyone but me.

MOM: I hope my wounded bird with the abusive husband will get herself into counseling. The wounded bird with those children who walk all over her had better learn to assert herself before it's too late.

AMANDA: And I learned not to joke around: once I referred to one of her callers as a fractured canary and almost started World War III. Mom was busier than she had ever been before, what with traveling and lecturing and doing guest shows from other cities. Sometimes I felt that life was nothing but a revolving door. Mom going out while I was coming in. I know there are some kids who would've thought I was lucky, but the thing about my mother is that she's okay ... And I wanted to see more of her. Besides that, I needed to talk to her. I don't know why, but all of a sudden it seemed that things were piling up around me. No major crises, you understand. • My friend Terri has a secret crush on my boyfriend Josh. If she does, it would be a disaster, because how could we really be friends anymore? But then again how could Terri and I not be friends? • Then there's Miss Spellman, my English teacher, who has this really atrocious breath and is forever leaning into people as she reads poetry in class. Imagine somebody breathing garbage fumes on you as she recites - Emily Dickinson If something doesn't happen soon I may never like poetry again. • And . . . I was coming out of gym on my way to study hall when Mr. Burnside, the guidance counselor, stopped me and started asking me what my career goals were and had I decided what I wanted to major in in-college. What I said, only politer, was that how did I know what I wanted to major in when I didn't even know where I wanted to go to college? Mr. Burnside got a wild look in his eyes and started opening and closing his mouth so that all I could see was a shiny strand of spit running between his top and bottom teeth while he lectured me on how I was going about this whole college thing the wrong way. He said I should come into the guidance office and let him feed me into the computer - well, not me exactly, but stuff like my grades, extra-curricular activities, and whether or not I needed financial aid

MR. BURNSIDE: And what does your mother say? You'll certainly have it easier than anybody else in your class - living with Dr. Emma Hart. (chuckling) She'll get right to the Hart of it. Anybody else'd have to call her on the telephone.

AMANDA: Anybody else'd have to call her on the telephone . . . Why not? Why not? And pretty soon why not? changed to when? I practiced in the shower making my voice huskier than usual and just a little breathless, hoping that it would sound sincere. Once I'd made up my mind to call Dr. Emma Hart, I began to feel like a wounded bird myself, and I was suddenly awfully glad that she cared about them the way she did. (on the phone) I put the call in just before eleven on the Monday morning of spring vacation. I heard my voice, as if it were coming from somewhere far away, giving my name as Claire ... it's my middle name, and outlining my problem. And all of a sudden, I was talking to my own mother and telling her how I couldn't talk to my mother. . . Dr. Hart let me go on for a while and then she broke in and said that it was important for me to know that my concerns were as real as anybody else's. What I had to do was be really up-front with her and let her know how I felt. Then she suggested that I make a date with my mother for lunch so that I could tell her (Mom) exactly what I'd told her (Dr. Emma Hart). The only trouble was that as soon as Mom got home that day, I knew it wasn't going to work. She was sort of coming unglued. It had been a bad day.

MOM: Thank heavens you've got it all together.

AMANDA: Talk about guilt. Right away I knew I was going to break rule number one: I wasn't going to be able to be up-front. I couldn't take what was already one rotten week for Mom and dump my problems, which seemed to be getting bigger by the minute, on her. I felt like I was going to explode. By Friday I knew I needed another talk with Dr. Hart.

RECEPTIONIST: Hold on. Dr. Hart will be with you soon.

AMANDA: And there was Dr. Emma Hart again. And suddenly there I was. unloading about how what she had suggested wasn't going to work.

EMMA HART: Why not? Did you try?

AMANDA: Yes - no. (to audience) Then I was going on again all about Miss Spellnan, the guidance counselor; and how maybe my best friend had a thing for my boyfriend. I said that my mother was swamped, preoccupied, distracted. And then it happened. (to Emma Hart) The thing about my mother is that she has all these wounded birds who have really important problems, and they take all the time she has. (to audience) A silence ballooned up between us and was so loud I couldn't hear anything else. When Mom finally spoke, her voice sounded choked, as if she had swallowed a gumball.

EMMA HART: We've been talking to Claire this morning, who is really Amanda. And one of the things we talk a lot about on this show is saying what you have to say even if that's not always easy. Are you still there, Amanda? (strangled affirmation from Amanda) If I know Amanda, she would rather have run away, or hung up, but instead she did something harder. She hung on. Amanda is my daughter, and it seems we have some things to talk about, so what I’m going to do is to ask my assistant to make a reservation for lunch at the Terrace Garden. If you hurry, Amanda, I'll meet you at 1:30. So we can talk.

AMANDA: And we did: about Miss Spellman, and Terri, and how it's okay not to know now what I want to do with the rest of my life. We talked about saving the whales, and our two weeks at the shore this summer, and how someday we're going to Ireland. About books and movies and the time in fourth grade when I got the chicken pox and Mom caught them from me. And we talked about how we had missed talking to each other and what we could do about it. We sat there all afternoon, until the light streaking in the windows changed from yellow to a deep, burning gold and the busboys started setting the tables for dinner.
```

---

## IC-2178: Amy’s Answering Machine: Messages from Mom

- Title: Amy’s Answering Machine: Messages from Mom
- Author (byline): Amy Borkowsky
- Work: Not specified
- Publisher: Atria Books
- Publication date as stated: April 2001
- Event as filed: Prose
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
Does your mother call you in a panic whenever there's a storm warning for your area? Does she act as though it's her duty to alert you to every health story on the news? Have you ever been briefly out of touch with your mother only to find she's phoned everyone short of the National Guard to track you down – Or, just maybe, are you that mother? Take comfort in knowing you're not alone! This is

Amy’s Answering Machine: Messages from Mom by Amy Borkowsky
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

AMY’S MOM: Thirty-four and three quarters *******

AMY: (Pg 97-98) People are always debating whether it’s harmful for kids to watch too much TV, but I think the bigger problem is what happens when your parents watch too much TV!

AMY’S MOM: (BEEP) Amila? I just talked to you. Where’d you go? Anyway, I was watching the news and they had a story about the Hell’s Angels motorcycle club. They flashed a shot of a big bear of a guy from Greenwich Village who was covered in tattoos, and on the back of his motorcycle was a very pretty girl. Was that you? She had your hair, and she was wearing a green blouse that looked like the one that I gave you for Chanuka. You know how I feel about motorcycles!

AMY: (Sarcastically) I did understand her confusion. There are so few women in Manhattan with brown, wavy hair that, really, who wouldn’t assume it was me? I’m constantly getting comments . . .

WOMAN: Excuse me, but I was just noticing how completely unique your hair is. What color would you call that?

AMY: Brown.

WOMAN: Can you write that down? I want to ask my colorist about it. *******

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

WOMAN: Your mommy must’ve spent quite some time making your costume! *******

AMY: (Pg 11) So . . . If your own mother drives you crazy, I hope you now know . . . You are not alone!

AMY’S MOM: (BEEP) (Pg 26) Amila . . . it’s me again!
```

---

## IC-2179: The Anatomy of Wolves

- Title: The Anatomy of Wolves
- Author (byline): Danielle Wood
- Work: Rosie Little’s Cautionary Tales for Girls; Pg 111
- Publisher: MacAdam Cage
- Publication date as stated: Aug 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ROSIE, HIM, MOTHER, COUNSELOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1541
- Already set (do not supply): none

### Source block (context only)

```text
Author: Danielle Wood
Book: Rosie Little’s Cautionary Tales for Girls; Pg 111
ISBN: 978-1596922525
Publisher: MacAdam Cage
Date (Month/Year): Aug 2007
```

### Introduction (context only: never use it for content warnings)

```text
In this modern take of Little Red Riding Hood, Rosie doesn’t realize she’s stepped off the safe path. She thinks she’s just interviewing some quirky actor in a yellow ballgown, trading jokes and enjoying the kind of banter that feels fun and harmless. But little by little, it becomes clear he is anything but harmless. Rosie’s getting cozy with a wolf, the kind who hides in charm and costume instead of fur.

It’s easy to miss the danger when the wolf smiles, walks on two legs, and makes you feel chosen.

The Anatomy of Wolves by Danielle Wood
```

### Performance text (classify this)

```text
ROSIE: (Pg 111+) The wolf has legs . . . And these were the parts of him that I saw first. I was standing at the bottom of a backstage staircase and he was at the top, his shins sticking out from beneath a taffeta ballgown in an alarming shade of yellow.

HIM: You must be Reporter Rosie.

ROSIE: Is now a good time?

HIM: Rehearsals start again at two. We could do it over lunch, if you like.

ROSIE: (flirtatiously) Only if you leave that dress on. And promise not to say “eclectic” [or] I shall be forced to write evil things about your play. (waving her notebook) (to audience) At least, I think that is what we said. I was 22, just beginning at the metropolitan daily newspaper and almost certainly in love.

ROSIE: I walked with him to the theatre and, at the stage door, when we pulled ourselves apart: ‘Good luck,’ I said just before I remembered this was not the thing to say at all. Whistling backstage, the naming of the Scottish play, the wishing of good luck: all these things are forbidden in the theatre. Instead of ‘good luck’, one might say ‘break a leg.’ But there is another alternative to ‘good luck’; one that I have recently learned, and one that would — in hindsight at least — have been eerily apt. In bocca al lupo. Into the mouth of the wolf -- an Italian phrase that is meant to bestow luck and instill courage.

Only weeks later, we moved in together, renting a small flat behind a pizza shop.

The wolf has claws. But I didn’t see them for quite a long time. There were too many diversions. . . Often, he did the housework as Jesus, wrapped in a white sheet and singing Sunday school hymns over the top of the howling vacuum cleaner. Once, when I was sick with a cold, he borrowed a nurse’s outfit from the theatre’s costume shop, and ministered to me in a lispy falsetto until I laughed myself better. For the winter solstice we took blankets and candles to the local cemetery and read vampire stories to each other while the concrete cold of the graves seeped into our bones. More and more often, though, we stayed home at night on the weekends and watched old movies. . . We folded into each other like a pair of socks.

I remember the night of his birthday in colors. There was the beetle-green glitter eyelids of Cleopatra -- one of the girls from the theatre, and the peacock silk shirt of a guy salty-white hair. There was the red of my tartan skirt and the swirls and layers of bright liquor that were poured into shot glasses as we competed to drink more. The music was loud and silly, but with an irresistible dance beat. I was heady, giggly, and then, suddenly, alone.

‘Oh yeah,’ said the Cleopatra girl. ‘He went home.’

Cross and confused, I walked the few blocks to our flat without a coat, the cold of the night bringing a kind of sobriety. When I got there, he was sitting in the dark. The light I switched on was bright and I saw that he had been crying. The rims of his eyes were reddened. His irises a malignant green, his lips and cheeks pale and slack. But I was not sensible enough to be afraid. He shouted and accused.

HIM: Why didn’t you just *sleep with* him?

ROSIE: Who? You’re not making any sense! (to audience) He stood over me, but I did not back down. Nor did I see it coming. It was too far beyond my experience, too far outside my expectations. His fist felt huge against my small face.

On the couch, I couldn’t sleep. In our bed, he could. When the morning came, on his way out the door, he kissed my cheek softly. He came home with treats, and to begin with I was like a child who would not be enticed. I shook my head to chocolates in the shape of ladybirds wrapped in shiny red foil and to a tiny iridescent fish in a plastic bag of water. I cried and said no to striped socks with toes in them and to a jar full of tiny rubber dinosaurs that were purple, orange and yellow.

But I caved in when he ran me a bath and filled it with bubbles. I let him put a cotton pad soaked in witch-hazel over my bruised and swollen eye, and read to me -- doing all the voices and accents, too -- which made me cry. The tears were a drug whose effect felt like love.

The morning after the night on which he hit me for the second time, he looked at my face and then he put his head in my lap and cried. I stroked and soothed him, pushing my fingers into his beautiful hair. The grazed skin on the inside of my mouth felt like raw steak. I could still taste blood.

I had arrived late home from work to find the flat in darkness. He was crouched in the corner whimpering

HIM: I thought you’d left me.

ROSIE: I crouched down beside him, held out the back of my hand as if to a wounded dog. (to him) Hey, I was just at work. I’m sorry, I should have called.

HIM: (slightly louder) You’ll leave me. One of these days you’ll leave me, I know you will.

ROSIE: I won’t. I won’t. I won’t ever leave you.

HIM: (snarling) Don’t LIE! (strikes her with his fist)

ROSIE: Later that week, my bruises under the cover of the older women’s makeup, we sat at his parents’ table. We all said amen into our laps and then the house resumed a silence that didn’t feel safe. For all of the time it had taken her to make the gravy, his mother had said nothing. Now she pushed some food onto her fork and brought it halfway to her mouth, then put it down again as if it disgusted her. She looked up at her son with her big and green and sad eyes.

MOTHER: You did do that to her, didn’t you?

HIM: Do what?

MOTHER: I know what it looks like when a man hits a woman. I know exactly what it looks like. And it looks like that. (beat) I can’t. I just can’t!

ROSIE: . . . she said standing up at the table and taking away his still-full plate and mine. She tipped our meat and vegetables into the pedal bin and let the lid fall. She was standing over it, sob-breathing and gulping, as we left the house. In the dark of the driveway, I felt ashamed.

The wolf has teeth. It was true that his top incisors sloped inward a little, making his canines appear quite prominent; but it was not these that bit. It was the clean and white-painted right angle of the edge of our bedroom door. I hammered into it fast, a dervish, whirling. My brow-bone fractured on impact. Skin split and out poured unexpectedly dark blood. It streaked down the white paint as I slid to the floor.

I had gone home, to my parents’ house, for a weekend. but not without fear of what I would find when I returned. This time, it was tequila instead of gin. And this time, my hands were up, quickly, in a flimsy block between my face and his chest. I felt adrenalin gush to my hands and feet as he grabbed me, tightly, and held me by both wrists.

HIM: Why did you even bother to come back? You love them more than you’ve ever loved me.

ROSIE: He pulled me towards him and then pushed. I left his grip in a fast, hard spin, and collected the door with my face.

The wound would heal and, over time, fade into a pale crescent scar. But now it was an ugly gash of puckered skin and knotted twine marking the midpoint of eye sockets stained magenta and purple. My forehead was swollen and misshapen. The fine crack revealed by the X-ray was concealed beneath my swollen forehead, but in the mirror I could see the unmissable sign of ownership. A brand.

I was not allowed to leave the hospital until I had seen the domestic violence counselor.

COUNSELOR: He’ll bash you again.

ROSIE: I argued that I knew how to avoid it now. If I could just keep my mouth shut at the right moment. If I didn’t provoke him when he’d been drinking. She looked at me wearily, and I began to hear myself. After I had been silent for a time, she looked at her watch and said that I could go.

COUNSELOR: You’ll have to have someone pick you up? Must be someone.

ROSIE: There was only one person. But instead, I took a taxi to the home of a friend who wouldn’t scold. In the late morning, washed, and dressed in borrowed clothes, I went back to the apartment. He was sleeping. I sat beside him for a while, on the edge of our bed, watching dream-tremors flit through the muscles under the skin of his face.

The wolf has a heart. And there were times, during the year of my lesson in wolf anatomy, when I was close enough to see it. Just a glimpse of it, beating red and slick inside the dark fur.
```

---

## IC-2180: Answering 911: Life in the Hot Seat

- Title: Answering 911: Life in the Hot Seat
- Author (byline): Caroline Burau
- Work: Not specified
- Publisher: Borealis Books
- Publication date as stated: Sept 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: OPERATOR, STRANGER, GIRL CALLER, STEPFATHER, CALLER, DARIUS, AMBER, JAIME, MAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1969
- Already set (do not supply): none

### Source block (context only)

```text
Author: Caroline Burau
ISBN: 978-0873516020
Publisher: Borealis Books
Date (Month/Year): Sept 2007
```

### Introduction (context only: never use it for content warnings)

```text
Answering 911: Life in the Hot Seat by Caroline Burau
```

### Performance text (classify this)

```text
OPERATOR: (Pg 4) Every day that I sit down at a console in the 911 center, I tell myself that today could be the day. Today could be the day that I take a call that will change me forever. It could be the day that a bell gets rung that I can never un-ring. Some-one could die in my ear today and take a piece of me with him. Someone could tell me something unimaginable, and I'll have to imagine it.

STRANGER: (Pg 5) You're a 911 operator? Wow! I bet you've got some stories!

OPERATOR: I get that a lot. The most interesting stories are also the saddest. And you only think you want to hear them until I tell them to you. They are the stories where mothers and fathers fail their children. They are the stories where friends and lovers do awful things to hurt each other because of drugs or alcohol, or worse, for no real reason at all.

Or they are the fascinating ways that some people lose their grip on reality. Interesting? Yeah, but not amusing. . . (Pg 6) The night Dori Swanson died, I cried.

OPERATOR: (Pg 7) 911?

GIRL CALLER: My mom just killed . . . shot herself. Oh my God.

OPERATOR: Where's the gun?

GIRL CALLER: It's in her hand.

OPERATOR: Is she still alive?

GIRL CALLER: I don't think so. Oh God! No. She's dead.

OPERATOR: How old are you?

GIRL CALLER: I'm twelve.

OPERATOR: I would never trade places with the cops that had to go out to Dori Swanson's trailer that night. I would never say that I have a harder job than the medics who had to treat her dead body while her three kids wailed and screamed outside. I would never want to be the police chaplain who had to try to comfort them. But I will say this: At least they had a minute or two to get ready. Then I talk to her stepfather, who is neither upset nor hysterical. (to stepfather) Is she breathing?

STEPFATHER: I'm not in the room with her. I don't want to be blamed for anything.

OPERATOR: Then, with me still on the line, Dad's cell phone rings. He sets me down and answers it. To whomever is on the line, he says,

STEPFATHER: Dori shot herself . . . Yeah. Yeah, no s*** . . . I gotta go. Bye."

OPERATOR: (Pg 8-10) There are many people in the world just like this man. I never knew that until I took this job. The tough part, the longer you do this job, is remembering that most people aren't like him. For the next four minutes, I try to convince Dad to keep his three children out of the room where their mother lies dying (or already dead). Despite my efforts, all I hear are screams overlapping screams; I am no more in control of this scene than I am of the moon in the sky. At last, the cops and medics arrive, call a Code 4 (meaning okay, for now), and just like that, I'm disconnected from 874 Langer Drive. It's like I've been dangling twenty feet in the air, then somebody cuts my cord, and I'm bracing for the fall. That's the moment I first notice that my body is on fire. My hands and face are burning. My head is thick. I think, Who does that? Who blows their brains out in front of their kids? This is ridiculous.

Later, the shift is over and I think of what it must be like at Dori Swanson's house. I envision a cramped mobile home, maybe one of those single-wide jobs with the rotting wooden siding and the redwood deck. I see the kids' bikes that never got put away for the winter, now partially snow-covered. Outside of the fact that she lived in a trailer, I really don't know any of this. But I took the call; I'm involved. So I put myself there. I imagine it as it must have been, so I can grieve it, then maybe let it go.

Inside, I see the dirt-soaked beige carpet and the second-hand furniture; the TV that's always on. I see the overflowing ashtrays, and the filth, and the empty box of wine the chaplain later told me she drank that day. I see kids' drawings taped onto the refrigerator. I see five lives that will never be the same. Six. I see the bedroom where Dori killed herself, just briefly, but I don't stay there long. I wonder if what the cops saw at the scene is more or less horrifying than the image in my head. I never met Dori Swanson, but I wish she had found something worth living for in that trailer. *********

OPERATOR: (Pg 198) 911?

CALLER: (female screaming hysterically) He’s hitting me! He’s hitting me and he won’t leave me alone!

OPERATOR: (Pg 146) 911?

CALLER: (male out of breath) Everybody thinks I hit my girlfriend and they called the cops and I ran because I was scared, but I didn’t hit her.

OPERATOR: (Pg 202-203) Someday, I’m going to move out of this town. I can’t even take a walk anymore without passing ten house that I’ve sent police to for come medical or domestic or other. Or maybe, someday, I’ll quit. . . [but] vow to hang on a little while longer. I like helping people.

*********

OPERATOR: (Pg 53-55) 911?

DARIUS: I want someone to come arrest my mom. She's doing drugs.

OPERATOR: She's doing drugs right now?

DARIUS: Yeah, she locked herself in the bathroom and she's smoking crack. She does it all the time.

OPERATOR: What's your name? How old are you?

DARIUS: Darius . . . Fourteen

OPERATOR: Okay, we have a couple squads on the way, but I want you to stay on the phone with me so I know you're okay 'til they get there. Does she have any weapons?

DARIUS: No . . . (to Mom in the bathroom) Mom, I told you I's going to call! I don't want you to get high anymore!

OPERATOR: Is she mad at you for calling?

DARIUS: Yeah. But I'm tired of this stuff.

OPERATOR: Of course you are. You're very brave for calling. Is she going to fight the cops, do you think?

DARIUS: I don't know. She's different when she's smoking crack. Are they going to hurt her?

OPERATOR: (to audience) I've been trained never to make promises on behalf of the officers. If she fights, they might throw her on the floor, kneel on her back, and cuff her. Is it going to hurt? Probably. I hope she doesn't fight. If she gets hurt, will Darius ever call us again, even if he needs us? (to Darius) I don't think so, Darius. (to audience) I wish I could hug the kid. He trusted me with his mom. **********

OPERATOR: (Pg 143) 911?

CALLER: (whispering) There’s someone at the back door trying to get into my house

OPERATOR: (Pg 129) 911?

CALLER: (older lady) I want someone to come out here and look at what my neighbor is doing to me. She waits for me to leave, then she comes in and pees in my laundry basket. She thinks I don’t know it’s her. But I know. **********

OPERATOR: (Pg 58-59) 911?

CALLER: Yeah, we want to make a report for our son. He says he was molested by a guy from our church, and the guy has admitted to it already.

OPERATOR: How old is your son?

CALLER: He's six.

OPERATOR: Does the suspect know you're calling police?

CALLER: Yes, he's here with us.

OPERATOR: (to audience) The guy is a drifter, sixty-seven years old. We run his criminal history. He has seven prior arrests and convictions for molesting children in all different parts of the country. "Penetration" is the word used to say that he has had sex with boys. "Contributing to the delinquency of" means that he gave them drugs or alcohol. "Failure to comply" means he never went to his court-ordered sex-offender treatment. Some of his victims are adults now. He is almost begging to be thrown back into prison. Maybe it's the only way he knows how to be saved from hurting children. Maybe he needs the roof over his head. **********

OPERATOR: (Pg 56) 911?

AMBER: (calm and blasé) My name is Amber Gillis. My husband was using a table saw and cut two of his fingers off. We’ve got the fingers right here.

OPERATOR: (Pg 9) 911?

CALLER: (elderly man) My neighbor’s clarinet is keeping me up. It’s 8:30 PM, for God’s sake! **********

OPERATOR: (Pg 136 -138) Nine . . . (to audience) The phone disconnects before I can say all three numbers. When I call back, a young woman answers. She is out of breath, and there is a baby wailing in the background. (to caller) This is the sheriff's department. Is everything okay?

JAIME: Um, I just wanted him to leave, that's all.

OPERATOR: What happened?

JAIME: He hit me in the head and slammed me up against the wall.

OPERATOR: Is he still there? Why did you hang up?

JAIME: He's still here, but he took the phone away from me when I tried to call.

OPERATOR: (to audience) As I listen, the two lovers argue back and forth about whether he really hit her. Then it turns quiet, except for the baby. (to Jaime) Jamie? Jamie, what's going on?

JAIME: (to man, begging) Don't!

MAN: I'm going to do it. It's time for me to die.

OPERATOR: Jamie, what does he have? (thinking aloud) A gun? A knife? A bomb? What? (to audience) The baby wails and begins to sound out of breath. I've never taken care of an infant for any length of time. I wonder what she needs and wish I could give it to her. Is she hungry? Is she scared? Shouldn't Mom go and hold her now? After about one minute of this, I begin to realize what Jamie does not: That dips*** isn't going to kill himself. He just wants her to think that he will. To guys like him, women are necessary for survival. She is a roof over his head and a bed and a body to curl up with at night. He will be as sorry and as suicidal as he needs to be to make sure that he still has her waiting when he pleads guilty to disorderly conduct in front of a disinterested judge, then gets released from jail. So he keeps it up.

Later I learn he was holding a knife to his throat. Must have seen that in a movie or something. Judging by the way she is eating his little act with a spoon, I assume he had no trouble going right back to Jamie's apartment the next day. That's what guys like him live on, women who buy their stupid crap. I would love to get him on the phone and tell him to go ahead and do it. I know he won't. But I'd love to say, "Go ahead and do it, worm. You don't have the guts."

He's a sh***head. I can't change it. And she's making her choices. I can't change her. I only have her for these few minutes to do anything to help. He's a big boy and she's a big girl. But when I hang up on Jamie and the cops call a Code 4, one in custody, it's not the man's raspy voice or Jamie's pleas that ring in my ears. It's the baby's cries.

(Pg 142) I remind myself frequently: Most people don’t treat each other that way. Sometimes I imagine what their live would be like . . . Maybe my female caller later moved back to her mom’s house and enrolled in school. Maybe the male got court-ordered into alcohol treatment and it changed his life. It could happen. Growth happens all the time. Good things happen. It’s just that nobody calls 911 to tell us about it.

(long beat) (Pg 181) There is a God, but He can’t be blamed for all the times that people hurt people. I believe that God loves his children, but He can only do so much for them and to them without stepping on their free will. I pray to God very often to work through me. (long beat) . . . [like I said before] (Pg 5) The most interesting stories are also the saddest. And you only think you want to hear them until I tell them to you. . . stories where mothers and fathers fail their children. Stories where friends and lovers do awful things to hurt each other because of drugs or alcohol, or worse, for no real reason at all. (long beat and a call comes in; wearily) 911?
```

---

## IC-2181: The Anything Box

- Title: The Anything Box
- Author (byline): Zenna Henderson
- Work: Modern Fiction about School Teaching (ed Blanchard),
- Publisher: Allyn and Bacon, Date (Month/Year) Nov. 1995
- Publication date as stated: Not specified
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: DAVE, TEACHER, SUE-LYNN
- Teaser before the introduction: Yes
- Spoken words (computed): 830
- Already set (do not supply): none

### Source block (context only)

```text
Author: Zenna Henderson
Book: Modern Fiction about School Teaching (ed
Blanchard),
ISBN: 978-0205152506
Publisher: Allyn and Bacon,
Date (Month/Year) Nov. 1995
```

### Introduction (context only: never use it for content warnings)

```text
It began as a game, a way of getting attention, but soon it became so much more. It became her very existence. You see, circumstances beyond her control tore her world apart. Her Anything Box became her way of connecting to the past, of re-living a happier, safer time. It became her comfort, her sanity. Disappear with me into Sue-Lynn's Anything Box by Zenna Henderson.
```

### Performance text (classify this)

```text
DAVE: (angrily) Teacher? She looks!

TEACHER: Who looks?

DAVE: Sue-Lynn. She looks and looks.

TEACHER: At you?

DAVE: "She looks at her desk and tells lies. She says she can see.

TEACHER: Can see what?

DAVE: Anything It's her anything box! She can see anything she wants too.

TEACHER: I suppose it was about the second week of school that I noticed Sue-Lynn particularly. She had finished her paper-far ahead of the others as usual-and was sitting at her table, She had her thumbs touching in front of her on the table and her fingers curving as though they held something between them. She was looking completely absorbed. Her face was relaxed and happy.

I saw that she spent most of her free time staring at the table between her hands. She hurried through papers and then lost herself in looking. Several times after that I wandered to the back of the room. She saw or felt me coming, and her hand disposed of the evidence. Only once I thought I caught a glimmer of something, I started to wonder about Sue-Lynn. I watched her on the playground. That only confused me more.

Each time before she joined the rush to our door, her hand would sketch a gesture to her pocket. I began to worry about Sue-Lynn. Maybe this was a disturbance that was more fundamental than the usual run-of-the-mill that I had met up with. Maybe a child can smile a soft, contended smile and still have little maggots of madness flourishing somewhere inside. Maybe she does have an Anything Box. Maybe she is looking at something precious. Who am I to say no to anything like that?

What could you see in an anything box? Heart’s desire? I felt my own heart lurch just a little the next time Sue-Lynn’s hands curved. If it was her anything box, I wouldn’t be able to see my heart’s desire in it. Or would I? Then I felt a small presence at my elbow and turned to meet Sue-Lynn’s wide eyes.

SUE-LYNN: (whispering) Teacher? You see my box teacher? It’s my Anything Box!

TEACHER: (To Sue-Lynn) Oh my, may I hold it? (to audience) I took the squareness from her carefully. My tenderness showing in my fingers and face. And I received weight and substance and actuality. (She looks inside and in awe, describes what she sees) I was running barefoot through the whispering grass. My heart outstripping my flying feet and melted with a rush of delight into warmness as his arms- (to Sue- Lynn) It’s beautiful. It’s wonderful, Sue-Lynn. Where did you get it?

SUE-LYNN: It’s mine!

TEACHER: A night or so later when I leaned over my noon-drenched windowsill. I remembered the Anything Box. Could I make one for myself? Could I square off this aching waiting, this outreach, this silent cry inside me and make it into an Anything Box? I freed my hands and brought them together framing a part of the horizon’s darkness. I stared into the empty square until my eyes watered.

Sue-Lynn came to school sleepy-eyed and quiet. She didn’t finish any of her work and feel asleep during rest time. The next day Sue-Lynn burst into tears and slapped Dave!

Sue-Lynn! I gathered Dave up and took Sue-Lynn’s hand. In the shocked silence of the room, we stumbled over to the Isolation Bench. Seating herself, she leaned her head into the corner and sobbed quietly.

(to Dave) What did you do?

DAVE: I only said robber daughter. It said so in the paper. My mama said her daddy’s a robber.

TEACHER: I kept my eyes on Sue-Lynn for the next half hour as I busied myself with the class. Her sobs soon stopped and I knew she was taking comfort in her Anything Box.

That afternoon I looked up from my reading group, to catch Sue-Lynn’s frightened eyes. She looked down at her empty hands. Then she darted to the Isolation corner and reached under the chair. She went back to her seat slowly. For the first time, She-Lynn had to go get the Anything Box.

She sank into her Anything Box at every opportunity. And always, if she had put it away somewhere, she had to go back for it. She roused more and more reluctantly from these waking dreams, and there finally came a day where I had to shake her to waken her.

And before our horrified eyes, she toppled sideways off the chair; lay limp on the green tile, one hand still around something. I pried her fingers loose. I carried her down to the nurse’s room and she opened her eyes. Her hands jerked protestingly in mine.

(to Sue-Lynn) Your Anything Box is just for fun! You mustn’t think it’s real. It’s only play.

SUE-LYNN: (crying) No! No! (she frantically looks for her Anything Box) Where is it? Give it back to me, teacher! Where did you put it?

TEACHER: There is no Anything Box. It’s just imagination. It doesn’t exist.

SUE-LYNN: It does! And I almost got in… into my Anything Box. My daddy’s there… My daddy’s there… I want my daddy.
```

---

## IC-2182: The Apology

- Title: The Apology
- Author (byline): Eve Ensler
- Work: Not specified
- Publisher: Bloomsbury Publishing
- Publication date as stated: May 2019
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: EVIE, FATHER, MOTHER, EVE
- Teaser before the introduction: Yes
- Spoken words (computed): 2039
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eve Ensler
ISBN: 978-1635574388
Publisher: Bloomsbury Publishing
Date (Month/Year): May 2019
```

### Introduction (context only: never use it for content warnings)

```text
Like millions of women, Eve Ensler has been waiting much of her lifetime for an apology. Abused by her father, Eve has struggled her whole life from this betrayal, longing for an honest reckoning from a man who is long dead. After years of work as an anti-violence activist, she decided she would wait no longer; an apology could be imagined, by her, for her, to her. The Apology, written by Eve from her father's point of view in the words she longed to hear, attempts to transform the abuse she suffered with unflinching truthfulness, compassion, and an expansive vision for the future.
```

### Performance text (classify this)

```text
EVIE: (Prologue) I am done waiting. My father is long dead. He will never say the words to me. He will not make the apology. So it must be imagined. For it is in our imagination that we can dream across boundaries, deepen the narrative, and design alternative outcomes. This is my attempt to endow my father with the will and the words of apology so that I can finally be free.

FATHER: (Pg 1) Dear Evie, (Pg 34-35) It began simply, easily embedded in the ordinary. We had a game. I would close my eyes and ask, "Where has my Evie gone? Where is she hiding?" You would squeal with delight and shout

EVIE: I’m here, Daddy. I'm right here.

FATHER: My eyes still closed, I'd say, "Oh where oh where has my sweetie pie gone? Why does she not love me anymore?"

EVIE: (crying) Daddy, open your eyes. Open your eyes!

FATHER: And when I felt it had gone on too long, I would open my eyes with great surprise and delight. "Oh, there she is! There's my sweetie pie. But I am not sure she still loves her daddy!" And you, holding on to my face, looking into my eyes, would kiss me over and over on my cheeks and forehead.

EVIE: I love you, Daddy, I love you, Daddy.

FATHER: I would hold you then and lift you and spin you. "Yes, I think you do love your daddy. You do. You are your daddy's precious little girl." And you would laugh and shriek with relief and delight.

(Pg 41-42) My obsession with you erased all else. The family grew to despise you for it. In that sense I set you up to be hated. And that would come to be part of what destroyed you. They couldn't blame me. I was the husband. I was the father. They needed me. So they blamed you. You were the reason they were deprived. You were the reason it all went wrong. You stole my heart. You banished them to darkness. Your name was Eve and you brought the fall onto the family. You were five.

(Pg 43-45) Much to my chagrin, your mother arranged a vacation for her and me. I suspect she did this to get me out of the house away from you.

When we returned, I opened the door and waited for you to run to me and rush into my arms as you always did. You were nowhere around. I found you upstairs playing with your brother. I entered the room. You hardly looked up.

MOTHER: Evie, don't you want to greet your father?

FATHER: You walked over in a perfunctory way, sighed as if annoyed by the obligation to perform this rite, and barely kissed my cheek. Then you turned and without even the slightest smile or glance you went back to your game. My heart sank. This isn't my girl. What has happened to make you like this? (To Evie, trying to conceal his feelings) Evie, you can do better than that for your daddy.

EVIE: I'm busy now, Daddy.

FATHER: Slap in face. Door shut. Heart ripped apart. How dare you think you have the power to cut me off when I am your father?

You were a sweetie pie, Evie, but also a fierce and defiant child. I could no longer trust you to remain faithful to me. I had to exert control. (Pg 54-55) I withdrew my love from you. I never gave it back. I lived to hurt you after that. To hurt you for your unconcealable hurt. Thus began the reign of punishment, violence, and terror.

I vividly remember the night it began. You were standing in the den and you had just turned ten. You were slouched and had on a dirty T-shirt that I had asked you repeatedly not to wear. You were asking if you could spend the night at your girlfriend Judy's house. I said no. Perhaps because there was nothing about you I liked anymore and I wasn't about to reward you with anything.

EVIE: (with attitude) Why? Judy only lives up the street, I don't have school. We made a plan.

FATHER: Impertinent child. How dare you question my authority. My rage was boiling, my face on fire. Then you turned your face into the most disrespectful smirk, a disdainful smile refusing and mocking my command.

And Shadow Man instantaneously leapt up and with all his might he smashed his hand across your insub-ordinate face. Your whole body went flying across the room until it crashed against the wall and you dropped like a flimsy rag doll to the floor. And through your tears and shock, you smiled the sickest smile. War had been declared.

(Pg 56) Telling you this, I am filled with horror and regret, feeling for the first time how you must have felt. The shock. The disbelief. The utter loneliness. To be exiled, to have been made to believe you were everything and then in one violent blow erased to nothing. How could you, at ten years old, possibly handle this? Who could you turn to for help when I had turned all against you?

(Pg 72-75) I beat a child half my size. I battered a little girl. I used my hands, my fist, and belts as whips. I called you every terrible name. My intention was to humiliate and extinguish. My tactics knew no bounds.

Horrifying incidents replaying over and over on one punishing, unrelenting loop for fifteen years. Pieces of events, which cut rapidly scene to scene.

. . . Pizza parlor. Classless joint. Family dinner. Sit up straight, Eve. Sit still. I say something You immediately disagree. Stupid, girl. Boom. Fist lands in the center of your stupid face. Blood spurting from your nose. You displaying your face for the entire room. Embarrassing me. Outside I grab your arm hard. Drag you through the parking lot. I throw you in the car. Whimpering in back seat . . .

. . . Shaken awake out of deep sleep. Your mother rattled and alarmed. Get up, Arthur. Get up. Eve smoking in her bed. Whore. Slut. Grab you. Beat you. Smash you. Drag you down the stairs. Throw you outside. In the dark, in the cold, in your underwear. Now you'll live as a whore on the front lawn for all the world to see. Slammed, locked the door. Left you there . . .

. . . I catch you sneaking and whispering on the phone. No phone calls allowed. (To Evie) Hang up this phone, Eve. Get up here now. You will not go back to school. You will not be a cheerleader. We are sending you to reform school and you will sleep in the basement from now on with the dog. (return to narration) I drag you down the stairs and push you into the cellar. I've instructed the family to act as if you've died. No one is allowed to acknowledge or speak to you or they will be punished. You are driven mad. You leave . . .

(Pg 80-81) You became a wild hippie. You stopped wearing a bra, grew armpit hair, and looked a disgrace. Everything you did was a slap in my face. And I knew violence was no longer a deterrent. Even when I grounded you and refused to let you out of the house, you would defy me by sneaking out in the middle of the night. You were reckless in the car. You were willing yourself to crash, to be caught, to be arrested, to be obliterated. Your grades and performance in school were assuring you would not go to college or have any future. You stopped eating and were frighteningly thin. You were hyper and you never stopped moving your leg. You were intolerant and disagreeable. There was nothing that could pull you back in.

At eighteen you were in a madly spinning downward spiral, on your way to some irreversible tragedy or possibly death. I blamed this on your willfulness and badness. I blamed and shamed and hurt you more. I never for one moment tried to prevent you from falling.

How did you breathe, Eve? How did you survive?

(Pg 87-89) No plea of your mother's touched my heart. It didn't matter how far you fell, how close to ruin or poverty or death. It didn't matter how much you craved my acknowledgment and support. I invalidated you on every count. And to this day, I don't know how you did it, but after one year at some third-rate women's college, you turned your academic life around and were able to transfer to a prestigious school. Perhaps it was finally being away from me. Perhaps it was the raging impetus to prove me wrong. When you came home on a break, you were filled with a new brashness and fire. You were discovering your interests and your talents. You declared at dinner you were going to be an artist, a writer. You were not going to take sciences or math, as I had strongly advised. Your arrogance and sureness enraged me. (I see now, again, it was jealousy.) Who were you at nineteen to think you had any idea what you wanted or what you needed to study? I said you would take classes to prepare you to be a lawyer or an accountant. I said if I am paying for it, you will take classes that prepare you for a realistic future.

EVE: No, I will not take those classes. I am getting straight A’s now. I will get a scholarship. You can keep your money.

FATHER: Boom! I pulled the chair out from underneath you and lifted it to crash it on your head. And to my shock, you lunged at me.

EVE: (lifting her fists) You don't have to support my classes or my dreams, but if you ever touch me again, I will leave this house forever. I promise you.

FATHER: My God, you were willing to die for this? I knew then I had to develop more effective and ruthless strategies to delegitimize this fantasy and bring you down. Battle on.

You were accepted early into the top graduate drama school in the country. You came home on a rare visit to share your excitement and enlist my support. It was a huge deal that you had been accepted.

EVE: Daddy, it is everything!

FATHER: And looking back, Eve, it probably was. (To Evie) I told you years ago, if you wanted to go this route you would go it on your own.

EVE: But I can't get a scholarship if you have money.

FATHER: That's your problem, Eve. You made your choice. It's up to you to figure it out. (return to narration) Right there I thwarted your foolish dream. Or at least that's what I hoped and thought. (Pg 93) Your mother could not understand this.

MOTHER: Why would you spend all that money on Eve's college education and then undermine her consistently?

FATHER: It made no sense. But there was a fiendish logic. The more independent you became, the more successful, the less control I had of you. I needed to disable you.

(Pg 94) You almost drank yourself to death, putting yourself in constant danger, secretly dreaming that someone would take you out, stop the pain, undo the curse. And I watched and let it happen. You lost your voice, your purpose, and your way. I never stepped in to help you. In your deepest economic distress, I never offered you a penny.

(Pg 95-96) Here's the horrid truth, Eve. It gave me pleasure to watch you grovel without money, respect, or a future. It amused me to see you fall from such willful heights chasing an impractical and grandiose future you had independently designed. What business did you have imagining you could be a writer or an artist when I had spent my best years as a high-end ice cream salesman to pay your bills?

I had become a person who derived pleasure from your suffering. As you fell, Eve, I could feel better about myself. You were no longer a threat to my ego or worth. You had betrayed and disobeyed me. You were a failure. (long pause)

(Pg 112) Eve, Let me say these words: I am sorry. I am sorry. Let me get it right this time. Let me risk fragility. Let me be still. Let me not occupy or oppress. Let me not conquer or destroy. Let me be the father. Let me be the father who mirrors your kindheartedness back to you. Eve, I free you from the covenant. I revoke the lie. I lift the curse . . . Your Father
```

---

## IC-2183: Are You There, God? It’s Me, Margaret

- Title: Are You There, God? It’s Me, Margaret
- Author (byline): Judy Blume
- Work: Not specified
- Publisher: Atheneum Books for Young Readers
- Publication date as stated: April 2014
- Event as filed: Prose
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

Are You There, God? It’s Me, Margaret by Judy Blume.
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

MARGARET: Fourteen! That’s crazy! I’m not waiting until I’m fourteen. (Pg 116) [It wasn’t long after that, that] Nancy and her family went to Washington over Lincoln’s birthday weekend. I got a postcard from her before she got back.

It only had three words on it - I GOT IT!!!! There was something wrong with me. I just knew it. Are you there, God? It’s me, Margaret. Life is getting worse every day. I’m going to be the only one who doesn’t get it. Why can’t you help me? Please… let me be like everybody else! (Pg 154) [I decided] I was never going to talk to God again. What did he want from me anyway? I was through with him. (Pg 126-127) On March eighth, I was twelve years old. The first thing I did was sniff under my arms, the way my mother does. Nothing! I didn’t smell a thing. Still, now that I was twelve, I decided I’d better use deodorant, just in case. In school, Mr. Benedict shook my hand and wished me a lot of good luck in the coming year. He also led the class in singing “Happy Birthday” to me. (Pg 155-157) [That afternoon] I asked my mother to drive me downtown to meet Janie for a movie. We were twenty minutes early, so we went into the drugstore on the corner to look around. Mostly we liked to inspect the sanitary napkin display. (to Janie) Let’s buy a box, just in case. (to audience) I took a box of Teenage Softies off the shelf and walked to the check-out counter. Max took my money and presented me with [a] brown bag. That was all there was to it. You’d think he sold that kind of stuff every day of the week. (Pg 158) When I got home I went to my room with my purchase. I sat down on my bed staring at the box of Teenage Softies. I hoped God was watching. Let him see I could get along fine without him! (Pg 169-170) [That night] I had to go to the bathroom. Then, I looked down and I couldn’t believe it. (yelling) MOOOOOM - hey - MOM - come quick! I got IT! (Pg 171) I had to call Nancy and Gretchen and Janie right away. How about that! Now I am growing for sure. Now I am almost a woman! Are you still there, God? It’s me, Margaret. I know you’re there, God. I know you wouldn’t have missed this for anything! Thanks an awful lot!
```

---

## IC-2184: Bald in the Land of Big Hair

- Title: Bald in the Land of Big Hair
- Author (byline): Joni Rogers
- Work: Not specified
- Publisher: HarperCollins Publishers, Inc
- Publication date as stated: Feb 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: JONI, DR. RO, MALACHI
- Teaser before the introduction: Yes
- Spoken words (computed): 1478
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joni Rogers
ISBN: 978-0060955267
Publisher: HarperCollins Publishers, Inc
Date (Month/Year): Feb 2002
```

### Introduction (context only: never use it for content warnings)

```text
Being a parent while living with cancer is physically and emotionally exhausting. You do everything you can to protect your child from the pretend monsters under the bed and the real monsters lurking in the world. Yet, here at your doorstep is the most real and feared monster of them all, Cancer, and you have no choice but to let it in.

Bald in the Land of Big Hair by Joni Rodgers
```

### Performance text (classify this)

```text
JONI: (Pg 1) When tomorrow was still a given and ignorance was still bliss, I was floating along like a paper sailboat on a lazy river, too caught up in my life to know that I was dying. But the day you're diagnosed with cancer, you stop dying and start surviving. You stop living and start staying alive.

JONI: (Pg 42-47) Dr. Ro made a concise explanation of the diagnosis: diffuse large-cell lymphoma, a high-grade, swiftly spreading cancer. (To Dr. Ro) So what does this mean? Does this mean . . . am I dying? (to audience) But Dr. Ro was reluctant to place a statistical probability on my survival, dodging the question with cautionary statements like . . .

DR. RO: This is a very serious situation. It is important that we move ahead quickly.

JONI: (to audience) Chemotherapy, she said, had proved successful in such cases, and she was ordering six to eight cycles, for starters. (To Dr. Ro) No, I don't want chemotherapy. I want to investigate my alternatives.

DR. RO: (bluntly) Your alternatives are chemotherapy or death. You have very good chance of getting remission with chemotherapy.

JONI: But I read in this book-it said chemotherapy is like removing a wart with a blowtorch.

DR. RO: That's not an appropriate comparison. A wart doesn't kill you.

JONI: (to audience) Her eyes never wavered from mine, and they held not a trace of apology, sympathy, or doubt. She laid out the gruesome possibilities in clinical nomenclature, couching blunt realities like "barfing" and "agony" in palatable terms like "nausea" and "discomfort." This was the first time I heard the word alopecia.

DR. RO: The loss of one's hair.

JONI: (to audience) The word that starts with B and rhymes with "appalled." (To Dr. Ro) It doesn't matter. That's the least of my worries. ******

JONI: (Pg 109) When I was diagnosed with cancer, Malachi [my son] was a savvy second grader. He was old enough to know facts, but young enough to struggle with implications and smart enough that there was no keeping the truth from him. He accepted with a silent nod each time we explained a new side effect or defined a new clinical term, and I would hear him at night, whispering in the dark.

MALACHI: Are you going to die, Mom?

JONI: (to Malachi) I’m trying not to. I promise I’ll do everything possible to stay here with you as long as I can. (to audience) Later, when I wasn’t too sure, I started adding something about how he was a part of me and I was part of him because he grew right out of my own body, so no matter what, I would always be with him.

(Pg 112-113) A child's life is made up of fragile combinations. The irresistible upward motion of precariously stacked building blocks. The intricate logic of a Tinker Toy Ferris wheel. The smooth symbiosis of peanut butter and jelly.

MALACHI: Mom . . .

JONI: I awoke to the feeling of a small hand patting on my cheek, but it took me a moment to open my eyes. (to Malachi) Sweetie, please. Mommy doesn't feel good. Just turn to the Disney channel, okay?

MALACHI: But I'm hungry.

JONI: Can you make yourself a PB and J?

MALACHI: No, you have to make it.

JONI: Sweetie, could you just give it a try? C'mon. Be my big boy.

MALACHI: Why can't you get up and make it? It'll just take a minute. Then you can lay down again.

JONI: All right. (to audience) I sat up on the couch and dragged my feet to the floor. A wave of nausea and dizziness engulfed me, and I rested my head forward in my hands. (to Malachi) Malachi, I can't. I'm sorry, sweetie, you're going to have to do it yourself.

MALACHI: (whining) Nooooo (pause, thinking) I don't feel good. I'm sick. You have to, Mom! You have to do it.

JONI: You're not too sick, Malachi, you're just too lazy. Now would you please . . . oh . . . Lord . . . (to audience) I struggled up from the couch and lurched toward the bathroom.

MALACHI: (groaning) Are you going to throw up again?

JONI: I closed the door behind me. In a little while, I heard the sound of the refrigerator door. Then the silverware drawer. Then a chair scraping across the kitchen floor. ******

JONI: (Pg 119-123) When I woke up the next day, Malachi wouldn't speak to me. I tried to jolly him through the first half of the morning, then let him avoid me until lunchtime. (to Malachi) Hey, Ike. Can I make you a PB and J?

MALACHI: I'm not hungry.

JONI: Oh, c'mon. I'll put more peanut butter on it. Way more. It'll be nice and messy.

MALACHI: Why don't you go lay down if you're so sick.

JONI: Well, thanks for your concern, Dr. Snidely, but I'm feeling better today. (to audience) Cringing at the cranky sound of that, I deliberately softened my tone and laid my hand on his head. (to Malachi) That was kind of rough yesterday, I know. But Dr. Ro said it's normal to be kind of rough the first few days after chemo, and then it gets better. (Kneeling to be on eye level) It gets better, right?

MALACHI: (Softly then gaining strength as he is overcome with anger and sadness) You're not sick! You're just lazy! You don't play -- you don't read books -- you just lay around on the couch all day! You don't want to go to the park or do art projects or science experiments like we always-"

JONI: Malachi, I still want to do those things, but some days it's too hard for me. (Pause) Ike, life is full of stuff we have a tough time understanding . . .

MALACHI: (Mimicking in a jeering falsetto) Life is full of stuff we have a tough time understanding.

JONI: Hey! (Grabbing his arm and jerking him close – she speaks harshly right in his face) I'm sorry this is hard for you, and someday you can tell your analyst how horrible it was having me for a mother, but in the meantime, I will not allow you to speak to me this way, do you understand?

MALACHI: (Pulling away) I think you like having cancer! I wish I had cancer!

JONI: (She slaps him hard, across the face) Don't you ever, ever say that again! (immediately appalled, she covers her face with her hands and cries)

MALACHI: (racing away to his room) I wish you would just die! (slamming the door to his room) I hate you!

JONI: But I hated myself more. After five minutes, a glass of water, and a few deep breaths (take calming breaths), I followed him down the hall. (knocking gently on the door) Ike? Hey, can I come in? (no answer, after a moment she opens the door and steps inside) All right. First, I'm sorry I hit you. That was wrong, wrong, wrong, and I'm sorry. (silence) Malachi, I know you don't wish you had cancer. And I know you don't hate me. And I know that you know none of those other things you said are true. You're just mad because I'm sick, and that's -- it's just . . .

MALACHI: (eyes filled with tears and voice quivering) Mom, I don't want you to -- I don't wish -

JONI: I know. But I wouldn't blame you if you did. Because a few times lately . . . I've wished it myself. I've wished I would just die, Ike. There are times it seems like that would be easier. (to audience) He closed his eyes and shook his head, fighting not to cry. He tried to turn his face toward his pillow, but I pulled him onto my lap. (to Malachi) Malachi, I don't blame you for being mad at me. Everything's out of whack right now, and it seems like it's all my fault. But I really think I'm going to start getting better soon. And if I do die, it won't be because you wished it. Just the opposite. Every day I go on like this -- well, it's hard, Ike. And I don't know if I would have had the courage to do it if it wasn't for you. You make me want to stay alive. You're so full of surprises. I just have to stay around and see how you turn out. ******

JONI: (Pg 127) Trying to be an effective parent when physical and emotional reserves are depleted. The uncertainty and the painful truths that must be told. A child's grief and anger and fear. Though I couldn't see it at the time, Malachi's experience mirrored mine, emotion for emotion, challenge for challenge. He climbed his private mountain and came down changed, just as I did. Both of us discovered reservoirs of unexpected strength, but each of us left a little of our innocence behind.

(Pg 250-251) Someone sent me a little wooden plaque that said, "Adversity is a blessing." But I disagree. The overcoming of adversity is a blessing. Adversity is not a blessing. Adversity just sucks.

"Cancer is the definition of who I am now," said one survivor in a magazine article I read a while back. But if cancer is what we are, and all our efforts are bent toward killing cancer, then what's to become of us?

Cancer is not what I am. It's not a gift or a curse. It's not a blessing in disguise (unless that is one dang good disguise!). It's not the scourge of God, not the Red Badge of Courage, nor is it a purely clinical phenomenon. Personally, I like Malachi's definition: "Cancer is what happens when your cells decide to go funky." We are who we are, regardless of a few funky cells, and surviving cancer is the same as emerging from any of life's refining fires.

I'm still wondering if and when I'll ever "get over it." After all this time, cancer can still reach out and grab me with insidious tentacles of survivor's guilt, fears of reoccurrence, and self-pitying fantasies of what might have been had the beast passed me by.
```

---

## IC-2185: Batting a Thousand (From Fat Girls and Lawn Chairs)

- Title: Batting a Thousand (From Fat Girls and Lawn Chairs)
- Author (byline): Cheryl Peck
- Work: Fat Girls and Lawn Chairs
- Publisher: Warner Books
- Publication date as stated: Jan 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1241
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cheryl Peck
Book: Fat Girls and Lawn Chairs
ISBN: 978-0446692298
Publisher: Warner Books
Date (Month/Year): Jan 2004
```

### Introduction (context only: never use it for content warnings)

```text
It isn't easy being a bat. With Dracula, a few cases of rabies, their pointy teeth, and the fact that they hang upside down to sleep, bats inspire fear in many people. Forget all those stories about bats being blind, becoming entangled in hair, and transmitting diseases to humans and animals. Myths about bats abound, but the facts about these animals are actually far more interesting. For example, did you know that a single little brown bat can catch more than 1,000 mosquitoes in just one hour. Or that North America's common little brown bat has the world's longest lifespan for a mammal of its size, sometimes living more than 32 years. Of course expanding your knowledge base about bats becomes much less important when you find one inside your house! Batting a Thousand from Fat Girls and Lawn Chairs by Cheryl Peck.
```

### Performance text (classify this)

```text
I was sitting at the keyboard and Babycakes was sitting on my shoulder, half-asleep (both the cat and the shoulder) when an utterly silent shadow rippled across the room. I thought, There's a bird in this room.

Something was amiss, I could tell by the repetitive lashing of my left ear by the cat's tail.

A large bird, I reflected, reviewing my memory, black and swooping-probably a rogue turkey vulture.

But I sat at my keyboard and the cat sat on my shoulder, and for the longest time nothing happened.

It's all your imagination, I reproved myself. Perhaps it was merely a giant moth. And at that exact moment, an utterly silent shadow swooped across the room. The cat bolted off my shoulder, taking along small bits of my skin, and huddled down on the floor where he made himself into a small gold rug with big accusing gold eyes, which he trained on me, as if to say, What have you done now? Circling my light like a drunken glider was a bat. I know very little about bats now and I knew even less then. This bat was small and brown. (This observation is unusually precise. Experts in batology would have called it a small brown bat. I did not know this, at the time.)

When I stood up, the circle the bat was flying around my light became more elliptical, as if something large and horrifying had wandered into its radar. I looked around, but I never did see what it was. I spoke to the bat. I said, "Go away."

I walked over to the window, raised the screen, and posed, not altogether unlike Vanna White. "Here would be a good place to go," I directed. The bat switched the tilt of his ellipse from one side of the room to the other. Beyond that I could see no real change in his behavior. He swept past me once, dangerously close to my hair, which I interpreted as an act of aggression.

I may have shrieked. (Once. It was one of those girl-instinct things that some times gets the better of me.)

I went back to the other side of the room, beside the keyboard, and waited.

The bat stopped circling. He had thrown up some subsonic invisibility ray to disguise his whereabouts. I looked expectantly at the cat. The cat looked disgusted and bathed a wild hair. I thought to myself, leave the screen open, close the computer room door and go to bed--when you wake up in the morning, the bat will be gone. Or, thirty thousand of his closest friends will be partying in the computer room. There will be stale beer and com nuts all over the keyboard, small drunken aviators will be hanging upside down from the curtain rods . . . Bats are good, my conscience lectured me, don't do anything to hurt this innocent little bat.

So I closed the screen, closed the door and snuck myself and the cat out of the computer room and went to bed.

In the morning the bat did seem to have vacated the premises.

The following night I was sitting at the keyboard with a sleeping cat on my sleeping shoulder when an utterly silent shadow rippled across the room.

The cat lunged off my shoulder, taking most of my right arm with him, and hid under the desk. "That's it," I said, "I'm done-get out of my house." And I went for the tennis racket. (We will take a moment from our narrative to allow all of my personal friends to finish turning to one another and murmuring, "Cheryl Peck owns a tennis racket?" I do. I stole it from the Wee One because I could see no reason why my little sister should own a tennis racket when I didn't. I don't play tennis, but then again, I might. Besides, she quit playing right after that.) My plan was simple, but well organized: I would swing the tennis racket, knocking the bat out of the air into a small trash can I held in the other hand. I would then slam the tennis racket over the top of the can, constructing a makeshift jail long enough to carry my prisoner downstairs and outside to freedom, where he would gratefully flyaway. The cat at my heels was just insurance. Somewhat wimpy insurance, judging from the cowering crouch, but I assured myself that once the bat had stopped, it would look to the cat like what it looked to me-a flying mouse. The cat has never been out of the house and mice have never been in the house, but I trusted fervently that instincts would burst into play at the appropriate moment. I swung my tennis racket. I caught a solid draft of sheer air, nearly knocking myself off balance, while the bat circled around and swooped just over my head. I waited, muscles tensed for action, instincts honed, my heart pounding with the lust to kill: I swung again, nearly decapitated the cat, drove my own knee forcefully into the trash can as I stumbled forward, and I cursed myself for every tennis lesson I never took. On the third swing I knocked the bat out of the air onto the ground, where it twitched twice, attached itself to the grid of my tennis racket and began crawling up the handle. Swiftly, possibly shrieking (for only the second time in my life), I scraped the offending creature into the trash can, where it hung upside down, still glued to the racket. All three of us thundered down the stairs to the front door where a passionate discussion ensued concerning who can go outside and who cannot. In the meantime, the bat was shaking his battered little head and beginning to stir. The cat would not give up: he would go outside and oversee the release of the bat, or no one would go outside. He glued his back to the door, his paws spread, nailed against the door like a tiny hairy Jesus figure. I explained that if he had been a proper cat, he would have caught the bat, eaten it and I would never have had to deal with the situation at all. He spoke to me about the lure of the wild life, the faint perfume of wanton females in the wind, the sheer testosterone of hunting and killing his own food.

I set the trash can on the floor, its inmate twitching erratically against its mesh caging.

"Okay, so perhaps not," huffed the cat. He flicked his tail at me and stalked with great dignity into the kitchen. I carried the bat outside and released him. Or, at least I tried. I waved him toward freedom.

The bat remained glued to the tennis racket. I waited for the scent of freedom to call him. He wrapped his wings around his head and pretended to be dead. To the bat I said, "Give me back my tennis racket." For, having used this racket to play one game of tennis in the thirteen years it had hung in my basement stairway, I was loath to leave it outside, unattended, in the wind and the weather to warp and perhaps be destroyed.

"Get off, get off," I wailed, and began dancing the hopping whines of the terminally mature.

The cat poked his head through the curtains to see what I was up to, and then went away. I scraped the bat off my tennis racket against the stone flower box on my front porch not unlike the way one would remove peanut butter from a knife blade.

"Die there, then," I tossed as my parting shot.

The bat, batted and bewildered, cat-threatened and smashed and trashed-and, very likely, hungry-gathered his tiny bat wings up, shook them off, staggered a few steps down the flower box, then gathered himself together and flew unsteadily off into the sunset.

I suspect he warned his friends. Fear the mighty [dyke: replace with chick] that lives in that house, he told them all. That woman has a shriek that will foul up your radar for days.
```

---

## IC-2186: Beauty: When the Other Dancer is the Self

- Title: Beauty: When the Other Dancer is the Self
- Author (byline): Alice Walker
- Work: 75 Thematic Readings
- Publisher: McGraw-Hill
- Publication date as stated: Sept 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ALICE, BROTHER, DOCTOR, JIMMY
- Teaser before the introduction: Yes
- Spoken words (computed): 1411
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alice Walker
Book: 75 Thematic Readings
ISBN: 978-0072469318
Publisher: McGraw-Hill
Date (Month/Year): Sept 2002
```

### Introduction (context only: never use it for content warnings)

```text
The Prettiest . . . What does that mean? Physical features? Big eyes, glossy hair, high cheek bones? Rarely do you hear someone defining beauty as generosity, courage, kindness, and sense of humor.” At the age of two, Alice Walker, knew that physical beauty was definitely a selling-point. And she reveled in the role of being the “prettiest.” But how do you cope when a sudden accident renders you disfigured and you aren’t pretty anymore? Can you find the beauty within? Beauty: When the Other Dancer is the Self by Alice Walker.
```

### Performance text (classify this)

```text
NOTE: Speaker is an African-American woman

It is a bright summer day in 1947. My father, a fat, funny man with beautiful eyes, is trying to decide which of his eight children he will take with him to the county fair. I am two-and-a-half years old. I want to go everywhere my daddy goes. I am excited at the prospect of riding in a car. Someone has told me fairs are fun. That there is room in the car for only three of us doesn't faze me at all. Whirling happily, showing off my biscuit-polished patent-leather shoes and lavender socks, tossing my head in a way that makes my ribbons bounce, I stand, hands on hips, before my father.

ALICE: (With assurance) Take me, Daddy. I'm the prettiest!

Later, it does not surprise me to find myself sharing the back seat with the other lucky ones. At home that night I tell the unlucky ones all I can remember about the merry-go-round, the man who eats live chickens, and the teddy bears, until they say: that's enough, baby Alice. Shut up now, and go to sleep.

It is Easter Sunday, 1950. I am six years old and have learned one of the longest Easter speeches to be heard that day. When I rise to give my speech I do so on a great wave of love and pride and expectation. People in the church stop rustling. They seem to hold their breath. I can tell they admire my dress, but it is my spirit, bordering on sassiness, they secretly applaud. "That girl's a little mess," they whisper to each other, pleased. Naturally I say my speech without stammer or pause, unlike those who stutter, stammer, or, worst of all, forget. This is before the word "beautiful" exists in people's vocabulary, but "Oh, isn't she the cutest thing!" frequently floats my way.

It was great fun being cute. But then, one day, it ended.

I am eight years old and a tomboy. I have a cowboy hat, cowboy hoots, checkered shirt and pants, all red. My playmates are my brothers, two and four years older than I. We chase each other for hours rustling cattle, being outlaws, delivering damsels from distress. Then my parents decide to buy my brothers guns. These are not "real" guns. They shoot BBs. Because I am a girl, I do not get a gun. Instantly I am relegated to the position of Indian.

One day while I am standing on top of our makeshift "garage" --pieces of tin nailed across some poles-- holding my bow and arrow and looking out toward the fields, I feel an incredible blow in my right eye. I look down just in time to see my brother lower his gun.

BROTHER: If you tell, we will get a whipping. You don't want that to happen, do you? Here is a piece of wire, say you stepped on one end of it and the other flew up and hit you.

Confronted by our parents we stick to the lie agreed upon. First there is intense fever, Then there are chills: A week after the "accident" they take me to see a doctor.

DOCTOR: (Looking into the damaged eye and shaking his head) Why did you wait so long to come? Eyes are sympathetic. If one is blind, the other will likely become blind too.

This comment of the doctor's terrifies me. But it is really how I look that bothers me most. Where the BB pellet struck there is a glob of whitish scar tissue, a hideous cataract, on my eye. Now when I stare at people--a favorite pastime, up to now--they will stare back. Not at the "cute" little girl, but at her scar. For six years I do not stare at anyone, because I do not raise my head.

I am eight, and, for the first time, doing poorly in school, where I have been something of a whiz since I was four.

I am twelve. I abuse my eye. I rant and rave at it, in front of the mirror. I plead with it to clear up before morning. I tell it I hate and despise it. I do not pray for sight. I pray for beauty.

I am fourteen and baby-sitting for my brother Bill, who lives in Boston. He is my favorite. Understanding my feelings of shame and ugliness he and his wife take me to a local hospital, where the "glob" is removed. There is still a small bluish crater where the scar tissue was, but the ugly white stuff is gone. Almost immediately I become a different person from the girl who does not raise her head. Or so I think.

Now that I've raised my head I win the boyfriend of my dreams. Now that I've raised my head I have plenty of friends. Now that I've raised my head classwork comes from my lips as faultlessly as Easter speeches did, and I leave high school as valedictorian, most popular student, and queen, hardly believing my luck.

Ironically, the girl who was voted most beautiful in our class (and was) was later shot twice through the chest by a male companion, using a "real" gun, while she was pregnant. But that's another story in itself. Or is it?

It is now thirty years since the "accident." [And] I remember:

I am talking to my brother Jimmy, asking if he remembers anything unusual about the day I was shot. He does not know I consider that day the last time my father, with his sweet home remedy of cool lily leaves, chose me, and that I suffered and raged inside because of this.

JIMMY: Well, all I remember is standing by the side of the highway with Daddy, trying to flag down a car. A white man stopped, but when Daddy said he needed somebody to take his little girl to the doctor, he drove off.

I remember:

[Being] in the desert for the first time. I am so overwhelmed by its beauty, I confront for the first time, consciously, the meaning of the doctor's words years ago: "Eyes are sympathetic. If one is blind, the other will likely become blind too." I realize I have dashed about the world madly, looking at this, looking at that, storing up images against the fading of the light. But I might have missed seeing the desert! The shock of that possibility--and gratitude for over twenty-five years of sight--sends me literally to my knees.

But mostly, I remember this: I am twenty-seven, and my baby daughter is almost three. Since the birth I have worried about her discovery that her mother's eyes are different from other people's. Will she be embarrassed? I think. What will she say? Every day she watches a television program called Big Blue Marble. It begins with a picture of the earth as it appears from the moon. It is bluish, a little battered-looking, but full of light, with whitish clouds swirling around it. One day when I am putting Rebecca down for her nap, she suddenly focuses on my eye. Something inside me cringes, gets ready to try to protect myself. All children are cruel about physical differences, I know from experience. I assume Rebecca will be the same.

But no-o-o-o. She studies my face. She even holds my face maternally between her dimpled little hands. Then, looking every bit as serious and lawyerlike as her father, she says gently, but with great interest: "Mommy, where did you get that world in your eye?"

For the most part, the pain left then. Crying and laughing I ran to the bathroom, while Rebecca mumbled and sang herself to sleep. Yes indeed, I realized, looking into the mirror. There was a world in my eye. And I saw that it was possible to love it: that in fact, for all it had taught me of shame and anger and inner vision, I did love it. Even to see it drifting out of orbit in boredom, or rolling up out of fatigue, not to mention floating back at attention in excitement, deeply suitable to my personality, and even characteristic of me.

That night I dream I am dancing. As I dance, whirling and joyous, happier than I've ever been in my life, another bright-faced dancer joins me. The other dancer has obviously come through all right, as I have done. She is beautiful, whole, and free . . . And she is also me.
```

---

## IC-2187: Beauty and the Beast: Keeping Abreast of Sibling Rivalry

- Title: Beauty and the Beast: Keeping Abreast of Sibling Rivalry
- Author (byline): Leslie Marinelli
- Work: You Have Lipstick on Your Teeth (Pgs 5-10)
- Publisher: CreateSpace Independent Publishing
- Publication date as stated: Aug 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: LESLIE, STEPMOM, FATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1325
- Already set (do not supply): none

### Source block (context only)

```text
Author: Leslie Marinelli
Book: You Have Lipstick on Your Teeth (Pgs 5-10)
ISBN: 978-1490963419
Publisher: CreateSpace Independent Publishing
Date (Month/Year): Aug 2013
```

### Introduction (context only: never use it for content warnings)

```text
Welcome to this slightly lopsided tale of two lifelong companions: a bold, beautiful overachiever and her moody younger sister clawing her way to catch-up.

But *‘There’s no need to fear, Underdog is here!’ (sing part of the theme) You see, even in the most dysfunctional families, balance can still be found . . . eventually.

Beauty and the Beast: Keeping Abreast of Sibling Rivalry by Leslie Marinelli
```

### Performance text (classify this)

```text
LESLIE: (Pgs 5-10) I know it’s wrong, but I can’t help it. I have a favorite. I’ve read numerous books about siblings and birth order. All the experts agree that favoritism causes irreparable harm. And yet, no matter how hard I try to be fair and impartial, there is one I simply like better . . . She’s prettier than her sister. There, I said it. She’s also older, so we’ve had more time together to bond. Truth be told, she’s simply near and dearer to my heart – and not just in terms of proximity. She’s my left breast, and she’s spectacular!

LESLIE: Our family dynamic has always been a bit dysfunctional. My breast started to develop when I was 11-years-old. And no, that’s not a *mistake*. I said breast . . . as in one. My left breast, “Mutt,” began to bud a full year before “Jeff” on the right joined the puberty party in my Benetton sweater. And I’ll never forget it, because my best friend’s big sister Kelly told EVERYONE about my Lone Ranger. (Not unrelated: Kelly totally had it coming when we put that Nair in her shampoo.)

That was 1981. We were all singing about “Bette Davis Eyes,” but I knew in my heart I would never be “Jessie’s Girl” or experience “Endless Love” with only one hooter in my holster. A man with a “Slow Hand” sounded like a real catch according to The Pointer Sisters, but a girl with a slow breast? Not so much.

My chest ached constantly that summer . . . but mostly from sadness over my parents’ recent divorce and having to spend July and August in the face-melting heat of Phoenix, Arizona, away from my mom, dog, and friends back east.

So when I noticed a lump on the left side of my chest that July, I had no idea what to make of it. The only thing I new about boobs was that they came in pairs. This thing must have been a spider bite, or a hula-hoop injury, or a really low-hanging goiter.

But when the soreness persisted, I decided to take matters into my own hands. Every time I went into the bathroom, I would frantically perform 2-3 sets of the “I must, I must, I must increase my bust” move . . . but only with my right arm. Maybe I could give my lagging right breast a jump start and it could catch up with the other one before I went back to school.

Naturally my dad and stepmom were very curious why I was spending so much time grunting in the powder room that summer.

STEPMOM: (knocking on the bathroom door) Honey, are you OK in there? You sound like you’re in pain. Are you eating enough fruit?

FATHER: You know, when I was a kid, my Bubbie would line us all up on Sunday nights and make each of us swallow a spoonful of cod liver oil.

LESLIE: “I’m fine,” I’d grunt between reps. “I’ll be out in a minute.” I’d emerge moments later – sweaty, breathless, right bicep bulging . . .

“Oh! Of course!” They nodded. There was only one other reason a kid that age would spend so much time behind a locked bathroom door. After that, they gave me a wide berth . . . and told me to wash my hands a lot. Next thing I knew, my stepmom bought me a copy of Our Bodies, Ourselves. I missed my mom.

My fascinating new book kept me busy though, as did exercising my right arm multiple times a day. By the end of the summer, I could properly diagnose 12 different venereal diseases and lift a car off a toddler with my left arm tied behind by back.

Surprisingly, having half an upper body like Lou Ferrigno did not nudge my other breast into existence. I returned home to Pittsburgh that August with a heavy heart and a rogue breast bud camouflaged by a “Wouldn’t you like to be a Pepper too?” t-shirt

I disguised my embarrassing deformity to the best of my 6th grade ability. Luckily for me, ruffled prairie blouses and denim vests were all the rage in the early ‘80s, so it really wasn’t that hard to hid from most people . . . excepts for that b**** Kelly with the chemical burns on her scalp.

About a year later, my right breast arrived on the scene, but she was definitely the ugly stepsister to my first-born favorite – just the slightest big smaller, and never quite as ample – with a lazy eye and a limp, if I’m being honest. To this day, sometimes I catch a glimpse of her and fully expect to hear her quoting Igor from Young Frankenstein: “What hump?”

By the time I got to high school, “Mutt and Jeff” had become more like “Marcia and Jan Brady.” Sure, the were both flaxen-haired adolescent beauties, but we all know who got asked out on more dates.

Speaking of which, the first time I ever let a boy get to second base, it came as no surprise that he spent a lot more time hanging out with Marcia than Jan. I told her the lemon juice and the Afro wig were a bad idea. “Just be yourself, Jan! You’ll make friends one day.”

Fortunately, things pretty much evened out with the girls once I went away to college and embraced an all-carb lifestyle. I still couldn’t technically call them “the twins,” unless they were fraternal, born over a year apart, and fathered by two different baby-daddies. But over time “Marcia and Jan” matured. Or maybe I matured. Actually I was probably just to busy playing beer pong and dancing in fraternities to notice or care. Either way, my 1.5 breasts and I learned to live together in relative harmony.

The three of us sure had some good times together in the 1990s. We frolicked on the topless beaches of Spain, cleanses our pores in the mud baths of Mexico, skinny dipped up and down the Jersy Shore, and even discovered our aptitude for foreign currency with the breast-to-Mardi-Gras-beads exchange rate in New Orleans.

Eventually I settled down and snagged a husband. Sure, he’s legally blind without his contacts, and yes, he’s right-handed, but so what? He’s mine and he loves all of me unconditionally. In fact, he claims he’s never noticed that one of my kumquats wears a back brace and speaks with lisp, but whatever.

Clearly, marital bliss agreed with us, until I became a mother for the first time. When my milk came in, no longer were my breast separate but unequal. They were finally one unified all-you-can-eat-buffet of womanly splendor. At last, their purpose in life would be realized and they would be judged not by their outward appearance, but by the content of their character.

What I didn’t know was how difficult it would be. By the end of our first week together, my saber-toothed baby had managed to completely mangle my right nipple. “Marcia and Jan” morphed into “Beauty and The Beast.” For the next two weeks, I could only nurse my son with my left udder and use a breast pump on the raw right side. “See? Even the baby has a favorite!” I lamented to my mother.

All three of my baby barracudas experienced the same passive-aggressive behavior from my right Milk Dud. And with every new bambino, “The Beast” seemed to grow more hideous and surly . . . just like Jan Brady when she had to start wearing glasses.

My breastfeeding days are long gone, but the sibling rivalry remains. Today, it’s more about endurance – neither wants to get stepped on or mistaken for a genetically modified spaghetti squash. Little sister Jan has been gloating that she’s finally better at something than her alpha-boob big sister Marcia: “The larger they are the harder they fall.

The important thing is that we are a family and we stick together. As different as they are, they’re my girls and I’ll love them until the day I die.
```

---

## IC-2188: Before Fergus

- Title: Before Fergus
- Author (byline): Lynn Ferguson
- Work: The Moth Presents Occasional Magic, Pg 36-45
- Publisher: Crown/Archetype
- Publication date as stated: Mar 2019
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: LYNN
- Teaser before the introduction: Yes
- Spoken words (computed): 1561
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lynn Ferguson
Book: The Moth Presents Occasional Magic, Pg 36-45
ISBN: 978-1101904428
Publisher: Crown/Archetype
Date (Month/Year): Mar 2019
```

### Introduction (context only: never use it for content warnings)

```text
Congratulations! You are expecting a baby! The time has come for the 20-week scan -- when names have been chosen, tummies are swelling and babies are kicking. The 20-week scan -- the opportunity to find out, will our child be a boy or a girl? But the 20-week scan is also called the “anomaly scan.” Its intention is to determine if the baby is developing properly. You see, especially for women who conceive later in life, the risks of chromosomal birth defects exponentially increase.

In this selection, Lynn Ferguson is given a number of choices. Choices that will determine the fate of her family and her unborn child. Choices that, with the overturning of Roe v Wade, are no longer options for women in America. Lynn shares her personal stance on the issue of terminating a pregnancy: “I think it's a matter of choice . . . and I am completely and utterly pro-choice.”

Before Fergus by Lynn Ferguson
```

### Performance text (classify this)

```text
LYNN: I’m Scottish. A friend of mine is Bosnian, and he married a Serbian, and together they had a child. They had to flee their country, because their child -- being of mixed race -- was in danger by just being. They called their son Trim, which means "courage."

My friend said he called his son "Courage" because he felt that as soon as the child was born, he' cl lost all of his own courage, and that anything that he' cl fought for in his previous life had gone, and now he’d fight for nothing but the life of that child.

You know, I've thought about that a lot since I've had my son.

LYNN: I was thirty-seven when I first fell pregnant. Well, I didn't fall pregnant. There wasn't some incident with a sidewalk and a flip-flop. I did stuff. I got pregnant. I was thirty-seven. The discovery wasn't the kind of romantic one you get in black-and-white movies. I had been touring France on the back of a motorcycle with my husband when I started to feel a bit unwell.

Now, a word of advice: if you're feeling sick, don't do it at eighty miles an hour, leather pants on one end, crash helmet on the other, in a country where they eat snails because they can.

I've heard it said that you feel most like a woman when you're pregnant. It's complete rubbish. It's not so. I felt most like a beached whale. It's a completely bizarre thing, because you suddenly find yourself entirely responsible for this other person. And this other person has only got you, and so even though the two of you are together twenty-four hours a day, it's not like you can have a discussion about it.

Before I got pregnant, my greatest fear about getting run down by a car was that I wouldn't be wearing matching underwear. After I got pregnant, the whole idea of getting run over by a car took on a whole different meaning. Never mind the eating for two, it's the thinking for two that wears you out, you know?

There was a lot of difficulty around my pregnancy, because thirty-seven is considered quite an old age to be having your first child. So almost as soon as everybody agreed that I was in the family way, they decided that I should have an amniocentesis. An amniocentesis is an invasive test where they put a needle through the mother's belly and into the amniotic fluid, and it can tell you whether the baby has Down syndrome or not. But there's also a 1- percent risk that it will cause damage to the fetus or the fetus will miscarry.

Now, I'm totally not against risk; I think it's a matter of choice, and I like risk, and I am completely and utterly pro-choice. But there was no way they were going to do it. It wasn't the baby's fault I was thirty-seven. That was entirely on me. So, I was like, No. But every appointment it would come up, and initially I would deal with it that way you do when you don't want to have coffee with someone.

"Oh, the amniocentesis -- we will, we'll do it. I can't do it this week, though. Maybe next week? Oh, no, my mother's coming. No, I can't do that." But as they became more insistent about it, I kind of felt like I had to, too.

So, I was like, "You know, can this test tell me whether this child will be a jerk? Can your test tell me whether this kid is going to be one of those really screamy ones that annoys everybody on airplanes? Because I'm worried about Down syndrome, hands up, but I'm pregnant, and I'm worried about a lot of things. So, thanks very much and everything, but no."

Then came the twenty-week scan. We were told we were having a boy. Woo-hoo! Then the lady scanning the baby said that my son had statistically a very large head. I looked across at my husband for the first time, I swear, noticing his statistically large head. I silently cursed love for being blind.

She told me I was thirty-seven. I knew that.

Then, scanning the baby's head, she said there were choroid plexus cysts all down one side of the baby's brain. Okay. That wasn't something I was expecting. We were told that everything was going to be "fine," in that way where you just know it's not, and we had to wait for a specialist.

The specialist we went to see told us we were having a boy. We knew that. She told me I was thirty-seven. I know. She said the baby had a statistically large head. Then she said that the choroid plexus cysts were a problem. We'd kind of guessed that. And then, scanning the baby again, she said that there was a vessel missing on the umbilical cord.

She said we needed to do the test. But because I had waited so long, they didn't want to do an amnio, they wanted to do something called a cordio, which is pretty much the same as an amnio. They insert a big needle into the womb, and they take a little bit of the umbilical cord, and that can tell them what's going on with the baby. Now, this is an umbilical cord that they have just told me isn't fully functioning.

We didn't even need a discussion for the decision. I was like, "Okay, the Down syndrome thing, it's not exactly what we'd planned, and I know it's going to be difficult, probably -- for us and for him and in ways that I don't even know yet. But actually, per-sonally, I think there are worse things than having Down syndrome, you know? "I mean, having Down syndrome doesn't mean you're a bad person, does it?" So I said no.

But that's when they told me that Down syndrome was off the table and what we were talking about now was Edwards, a syndrome that means the baby will likely die, either in the womb or within the first year of life.

We'd had so many scans, and I'd seen my son. I'd seen his heart, seen the inside of his eyes. I'd seen his hands and his feet, and in fact, during one of the scans, he'd held his hand out to the front of my body as if to say, Will you go away? I'm busy. Do not disturb.

I'd felt my son move inside my body. What did it matter whether he had a disorder or not? And if he was going to die, well, we're all going to die, right? So, we should meet first. He was my son, and he needed me. He was depending on me to make the right decision. So, I said no.

We had no choice but to change hospitals after they offered me a termination at twenty-five weeks. It became really clear that they wanted to win a battle, and I just wanted to see my boy.

At precisely thirty-five weeks and five days, my son decided it was time to be born. My husband drove us to the hospital in our car, neither of us talking about what lay ahead.

The conversation was made up of the same four phrases: "Are you okay?" "Yeah." "You do know I love you?" "Yeah."

The birth process was the true definition of laborious. My husband gave me water and held my hand, and the midwives were brilliant. They were patient and reassuring. It would be okay, they said, everything was really early, but it would be okay.

I have no idea how long labor lasted, but eventually, my son appeared -- shot out, in fact, doing a kind of hand-brake turn on the table as he did so. He was purple in color, and my husband cut the cord. But whereas before there had been noise and bustle and shouting, suddenly there was silence. It was like the whole world had gone underwater.

The door burst open, and people in white coats came in. They bundled my son over onto a metal table, where they hurriedly tried to resuscitate him.

I had failed my son. He was depending on me, and I had failed him, and the whole world was underwater.

Then suddenly he choked, gagged, coughed up something, and started to breathe. The people in the white coats wandered off, and with my husband standing next to me, they handed me my son.

He. Was. Perfect.

"Fine," they said. "He's absolutely fine."

My son looked up at me. He was curious. He was amazing. He looked up at me as if to say, Ooh, that was all a bit of a trial.

"I am so glad you're here," I said.

My son is ten years old now, and he's still perfect (some of the time). And, like his father, he still has a statistically large head.

I haven't seen my Bosnian friend for such a long time, but I often wonder how he's getting on in his self-imposed exile. I called my son Fergus. In Irish it means "the right choice," but it has a different meaning in Scottish. It means "courage,” too.
```

---

## IC-2189: Before Women had Wings

- Title: Before Women had Wings
- Author (byline): Connie May Fowler
- Work: Not specified
- Publisher: Ballantine Books
- Publication date as stated: April 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: BIRD, BILLIE, GLORY, PHOEBE
- Teaser before the introduction: Yes
- Spoken words (computed): 1187
- Already set (do not supply): none

### Source block (context only)

```text
Author: Connie May Fowler
ISBN: 978-0449911440
Publisher: Ballantine Books
Date (Month/Year): April 1997
```

### Introduction (context only: never use it for content warnings)

```text
(Sing)
```

### Performance text (classify this)

```text
BIRD: (Pg 1-3) Back in 1965, on a day so hot that God Almighty should have been writhing with sick-to-the-stomach guilt over driving His children out of the cool green of Eden, my daddy walked into our general store, held a revolver to his head, told my mama, Glory, that he couldn’t take any more and that because of her harsh ways and his many sins he was going to blow his brains out.

*Some bright morning when this life is over
I’ll fly away
To that home on God’s celestial shore
I’ll fly away

I’ll fly away oh glory
I’ll fly away
When I die hallelujah by and by
I’ll fly away

Before Women had Wings by Connie May Fowler

BIRD: I was six years old, and I prayed that my guardian angel, who so far in my life had proven to be an elusive helper, would materialize. Prayerful words welled up inside me, whirled through my head: Please angel, whisk me away. Take me to your house in the clouds, just for a little while, just for today.

BILLIE: (Crying, voice loud and trembly) Glory, I mean it. I’m sick and tired of trying to make it in this godforsaken world. You and the girls will be happier with me gone.

BIRD: Daddy’s voice was loud, trembly. He was crying. I shut my eyes, and on the backs of my eyelids I saw Mama get up from behind the desk and put her arms around Daddy and coo, “Everything is going to be fine. Yes, baby, I love you. Your daughters love you.” If I’d been her, I would have done that. But my daydream did not come true. When I looked again, Mama was still sitting. When she spoke, her words pounded into me: “Jesus, Billy, you’re behaving like a fool.”

Daddy raised the revolver to his temple, and for a split second the gun seemed alive, a blackbird flapping.

BILLIE: I swear to sweet Jesus, you’re gonna be sorry, Glory.

BIRD: Then he slipped the weapon into the waistband of his pants and stormed out the front screen door.

GLORY: (Pg 5) Quit that foolish crying, Bird.

BIRD: I cried because my mama had told me not to. I cried because I didn’t know what else to do. (Pg 12) My true name is Avocet. Avocet Abigail Jackson. But because Mama couldn’t find anyone who thought Avocet was a fine name for a child, she called me Bird. Which is okay by me. She named both her children after birds, her logic being that if were named for something with wings, then maybe then maybe we’d be able to fly above the shit in our lives. (Pg 23) And so it went. And every night my parents fought:

BILLIE: (Pg 22) Listen here, I’m doing the best I can, woman. You know that. But I’m sick and tired of trying to please you. Nothing I do is good enough for you – Nothing!

GLORY: Trying like hell! You son-of-a-bitch, when was the last time you tried anything that turned out right! You’re no good, Billy Jackson, you’re no damn good! (Pg 54) When was the last time you acted like a father to your girls instead of like a useless drunk?

BIRD: (Pg 26) Some nights I would put my pillow over my head, trying to block out the sound of their arguing. And I would pray to Jesus. I would say, “Dear sweet Jesus, give me angel wings so I can fly away from here.” (Pg 50) Then I’d wonder if guardian angels really existed. (Pg 54) Daddy inhaled, swung his arm as if it were a bat. Then his breath crashed across his lips as he backhanded Mama smack in the mouth. A thread of bright red blood trickled down her chin. (Pg 67) [Again and again] I saw everything so clearly and wished I hadn’t. Her face was pummeled into ground beef. Her nose was no longer in the middle of her face. Her black-and-blue eyes were swollen shut. Mama might be dead. Summer crashed to pieces all around my feet.

PHOEBE: (whispering) She’ll be okay.”

BIRD: (Pg 50) [Now] Phoebe, [my sister], and I suffered beatings as frequently as some children were showered with hugs.

GLORY: We’re trying to make decent humans out of you.

BIRD: Mama would explain. And I’d wonder if there were children in the world who, at that very moment, were being doted on by fat grandmamas. Or little girls whose hair was being brushed out of their eyes as their mamas whispered, “You’re such a good child.” My mama, she wasn’t capable of whispering such sweet words. (Pg 72-73) I dug my nails into my wrists, and as the sting pushed back my tears, an awful notion struck me: My family, we needed to get the hell out of this roach-infested shack. If we didn’t we’d continue to be dumb-assed crackers who drink till dawn in a sorry attempt to forget about all the things they will never have, never become. But there’s no forgetting when you’re white trash. (Pg 74-75) Come morning, I slowly floated up through layers of dream-time, feeling a rush of wings against my skin. Mama sat at the kitchen table, her eyes wild and red-rimmed from tears.

GLORY: Come here, Bird, I need to talk to you. . . I don’t know how to say this easy, so I’ll just say it hard. Your daddy was found this morning by the police. And, well, he had such a tough time with life, he couldn’t handle it no more, honey. Bird, your daddy, he’s gone to heaven.

BIRD: (Pg 76) There wasn’t a funeral. We didn’t have any money, and the priest wouldn’t agree to a service because Daddy wasn’t a Catholic and he’d killed himself, so they said, and that was a sin in their church. (Pg 73) Smirks, stares, stolen glances remind you at every turn that you’re not worth squat. So the men, raging drunk, bullshit each other into believing that bruised fists and broken noses will act as charms, paving their way to heaven. And we females – girls and women alike – can’t find enough strength in our battered souls to escape. We cast daddies, husbands into near-respectable village idiots in the stories we spin over clotheslines draped with bleach-scented, bloodstained damp sheets. And after all that, we still aren’t decent. We’re still trapped. (Pg 233-234) My daddy . . . In my mind, I saw his suicide face, him gazing upon the black waters and finding no peace. Tears welled – I squatted and covered my eyes. Goddamn it! A voice filled my head: “Don’t you wish you were dead!” No! No! No! I cried. (Pg 242) I screamed. Screamed so loud I must have woke the dead. But nobody came. What do you do when you beg loud and long for help but there ain’t nobody listening? (Pg 234) I didn’t want to be like my daddy. (Pg 238) Night birds appeared suddenly, flashing past like ghosts. (Pg 243-244) A small flock of birds with long, upturned bills, stilt necks, white feathers edged in black. My, oh my, I knew what they were! How odd, I thought, this night I would find my avocets. Creatures with wings could end up most anywhere. (Pg 26) And I pray[ed] to Jesus. “Dear sweet Jesus, give me wings so I can fly away from here.”
```

---

## IC-2190: The Bell Jar

- Title: The Bell Jar
- Author (byline): Sylvia Plath
- Work: Not specified
- Publisher: Perennial
- Publication date as stated: Dec 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1453
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sylvia Plath
ISBN: 978-0060930189
Publisher: Perennial
Date (Month/Year): Dec 1999
```

### Introduction (context only: never use it for content warnings)

```text
The Bell Jar by Sylvia Plath tells the story of a gifted young woman's mental breakdown beginning during a summer internship as a junior editor at a magazine in New York City in the early 1950s. The real Plath committed suicide in 1963 and left behind this scathingly sad, honest and perfectly-written book, which remains one of the best-told tales of a woman's descent into insanity. In this selection, Esther is engaged in a conversation with Joan, another mentally disturbed young woman who seems to idolize Esther for her suicide attempt.

The Bell Jar by Sylvia Plath
```

### Performance text (classify this)

```text
Joan's room, with its closet and bureau and table and chair and white blanket with the big blue C on it, was a mirror image of my own. It occurred to me that Joan, hearing where I was, had engaged a room at the asylum on pretense, simply as a joke. That would explain why she had told the nurse I was her friend. I had never known Joan, except at a cool distance.

"How did you get here?" I curled up on Joan's bed.

"I read about you," Joan said.

"What?"

"I read about you, and I ran away."

"How do you mean?" I said evenly.

"Well," Joan leaned back in the chintz-flowered asylum armchair, "I had a summer job working for the chapter head of some fraternity, like the Masons, you know, but not the Masons, and I felt terrible. I had these bunions, I could hardly walk -- in the last days I had to wear rubber boots to work, instead of shoes, and you can imagine what that did to my morale . . ."

I thought either Joan must be crazy-wearing rubber boots to work-or she must be trying to see how crazy I was, believing all that. Besides, only old people ever got bunions. I decided to pretend I thought she was crazy, and that I was only humoring her along . . . '

"I always feel lousy without shoes," I said with an ambiguous smile. "Did your feet hurt much?"

"Terribly. And my boss-he'd just separated from his wife, he couldn't come right out and get a divorce, because that wouldn't go with this fraternal order - my boss kept buzzing me in every other minute, and each time I moved my feet hurt like the devil, but the second I'd sit down at my desk again, buzz went the buzzer, and he'd have something else he wanted to get off his chest . . ."

"Why didn't you quit?"

"Oh, I did quit, more or less. I stayed off work on sick leave. I didn't go out. I didn't see anyone. I stowed the telephone in a drawer and never answered it . . .

"Then my doctor sent me to a psychiatrist at this big hospital. I had an appointment for twelve o'clock, and I was in an awful state. Finally, at half past twelve, the receptionist came out and told me the doctor had gone to lunch. She asked me if I wanted to wait, and I said yes."

"Did he come back?" The story sounded rather involved for Joan to have made it up out of whole cloth, but I led her on, to see what would come of it.

"Oh yes. I was going to kill myself, mind you. I said, 'If this doctor doesn't do the trick, that's the end.' Well, the receptionist led me down a long hall, and just as we got to the door, she turned to me and said, 'You don't mind if there are a few students with the doctor, do you?' What could I say? 'Oh no,' I said. I walked in and found nine pairs of eyes fixed on me. Nine! Eighteen separate eyes.

"Now, if that receptionist had told me there were going to be nine people in that room, I'd have walked out on the spot. But there I was, and it was too late to do a thing about it. Well, on this particular day I happened to be wearing a fur coat . . ."

"In August?"

"Oh, it was one of those cold, wet days, and I thought, my first psychiatrist you know. Anyway, this psychiatrist kept eyeing that fur coat the whole time I talked to him; and I could just see what he thought of my asking to pay the students' cut rate instead of the full fee. I could see the dollar signs in his eyes. Well, I told him I don't know whatall -- about the bunions and the telephone in the drawer and how I wanted to kill myself-and then he asked me to wait outside while he discussed my case with the others, and when he called me back in, you know what he said?"

"What?"

"He folded his hands together and looked at me and said, 'Miss Gilling, we have decided that you would benefit by group therapy."

"Group therapy?" I thought I must sound phony as an echo chamber, but Joan didn't pay any notice.

"That's what he said. Can you imagine me wanting to kill myself, and coming round to chat about it with a whole pack of strangers, and most of them no better than myself . . ."

"That's crazy." I was growing involved in spite of myself. "That's not even human."

"That's just what I said. I went straight home and wrote that doctor a letter. I wrote him one beautiful letter about how a man like that had no business setting himself up to help sick people. . ."

"Did you get any answer?"

"I don't know. That was the day I read about you."

"How do you mean?"

"Oh," Joan said, "about how the police thought you were dead and all. I've got a pile of clippings somewhere." She heaved herself up, and I had a strong horsey whiff that made my nostrils prickle. Joan had been a champion horse-jumper at the annual college gymkhana, and I wondered if she had been sleeping in a stable.

Joan rummaged in her open suitcase and came up with a fistful of clippings. "Here, have a look."

The first clipping showed a big, blown-up picture of a girl with black shadowed eyes and black lips spread in a grin. I couldn't imagine where such a tarty picture had been taken until I noticed the Bloomingdale earrings and the Bloomingdale necklace glinting out of it with bright, white highlights, like imitation stars.

SCHOLARSHIP GIRL MISSING.

MOTHER WORRIED.

The article under the picture told how this girl had disappeared from her home on August 17th, wearing a green skirt and a white blouse, and had left a note saying she was taking a long walk. When Miss Greenwood had not returned by midnight, it said, her mother called the town police.

The next clipping showed a picture of my mother and brother and me grouped together in our backyard and smiling. I couldn't think who had taken that picture either, until I saw I was wearing dungarees and white sneakers and remembered that was what I wore in my spinach-picking summer, and how Dodo Conway had dropped by and taken some family snaps of the three of us one hot afternoon.

Mrs. Greenwood asked that this picture be printed in hopes that it will encourage her daughter to return home.

SLEEPING PILLS FEARED MISSING WITH GIRL

A dark, midnight picture of about a dozen moon-faced people in a wood. I thought the people at the end of the row looked queer and unusually short until I realized they were not people, but dogs. Bloodhounds used in search for missing girl. Police Sgt. Bill Hindly says: It doesn't look good.

GIRL FOUND ALIVE!

The last picture showed policemen lifting a long, limp blanket roll with a featureless cabbage head into the back of an ambulance. Then it told how my mother had been down in the cellar, doing the week's laundry, when she heard faint groans coming from a disused hole . . .

I laid the clippings on the white spread of the bed.

"You keep them," Joan said. "You ought to stick them in a scrapbook." I folded the clippings and slipped them in my pocket.

"I read about you," Joan went on. "Not how they found you, but everything up to that, and I put all my money together and took the first plane to New York."

"Why New York?"

"Oh, I thought it would be easier to kill myself in New York."

"What did you do?"

Joan grinned sheepishly and stretched out her hands, palm up. Like a miniature mountain range, large, reddish weals upheaved across the white flesh of her wrists.

"How did you do that?" For the first time it occurred to me Joan and I might have something in common.

"I shoved my fists through my roommate's window."

“My old college roommate. She was working in New York, and I couldn't think of any place else to stay, and besides, I'd hardly any money left, so I went to stay with her. My parents found me there-she'd written them I was acting funny-and my father flew straight down and brought me back."

"But you're all right now." I made it a statement.

Joan considered me with her bright, pebble-gray eyes. "I guess so," she said. "Aren't you?"
```

---

## IC-2191: Betty Ann

- Title: Betty Ann
- Author (byline): Ina Hughs
- Work: Chicken Soup for the Teenage Soul (Pg 36-40)
- Publisher: May 1997
- Publication date as stated: Health Communication, Inc
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: BETTY ANN’S MOTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1265
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ina Hughs
Book: Chicken Soup for the Teenage Soul (Pg 36-40)
ISBN: 978-1558744639
Publisher: May 1997
Date (Month/Year): Health Communication, Inc
```

### Introduction (context only: never use it for content warnings)

```text
13, 33, or 53 . . . if you are female, chances are other girls have bullied you sometime in your lifetime. Girl-bullying is more subtle than the boys who physically bully others. Girl-bullying is a dehumanizing experience that typically uses rumor spreading, name calling, psychological manipulation, character assassination, and social exclusion.

And because bullying among females is seldom physical it is more difficult to identify. However, upon close inspection, girl-to-girl bullying can be found in the halls, locker rooms, girls' bathrooms, lunch tables, the back of classrooms, on cell phones, and across social media.* And the days of “we didn’t know any better”are long gone. Mean Girls, although a comedy starring Lindsay Lohan, are nothing to be laughed at.

Betty Ann by Ina Hughs
```

### Performance text (classify this)

```text
Mistakes. We all make them. Sometimes, if we’re lucky, an eraser will do the trick, and we can rub it across the page, wipe away the dust, and all that’s left of our careless mess is a hardly noticeable smudge. But some mistakes can’t be erased. No matter how old or young we are.

I was in ninth grade the first time I really thought about all this. That year, I learned to diagram sentences on the blackboard, got my learner’s permit, wore my first strapless bra, wrote poetry I never read to my parents – but by far, the toughest lesson I learned was that life doesn’t come with erasers. I couldn’t make something that had happened, not happen. Even imagination is powerless. There are no erasers. I was 14, and I wished then, and I wish now, that I could erase or imagine away what I did, what we all did, to Betty Ann.

She came to our school from Cleveland, Ohio; and to our ninth-grade class in Richmond, Virginia, Cleveland was on another planet.

“Oh, hi! Ohhoooo. . . ” whispered Margie under her breath, as Mrs. Johnson introduced Betty Ann in homeroom that first day. Margie could be real snooty sometimes. Nobody took her too seriously when she got into her rich-kid, old-money mood. She’d entertain us with cruise stories and New York gossip every afternoon as we sat on the front steps after lunch, licking the icing off Oreos and begging quarters for a Dr. Pepper from the drink machine in the gym. Margie would try to impress us, in her high-pitched, bragging voice, with the Vogue models she knew and how they shampooed their hair; that people who ate their whole dinner with their salad fork were not the kind of people her family wanted her to marry into.

Actually, Margie was as insecure and as homely as the rest of us, and her life was about as exciting as the metric system, but we all knew Margie. We all knew everybody. Except Betty Ann. Most of us had been in the same class since kindergarten.

Then came Betty Ann of Cleveland, in her peasant blouses, rolled-down socks, and strange ideas.

If it had been just Margie who dug into Betty Ann, it wouldn’t have turned out the way it did; she probably could have handled that. But we all were in on it.

I guess what started us off was when Betty Ann wrote a better English composition than Susan Henderson. Susan was the writer of the class, and we were very proud of her. Her weekly story was always so good, Miss Moon usually chose it to read aloud to the class every Friday. Susan would sit back in her desk, a pencil stuck behind her ear, looking to all of us just like a promising young literary genius we could say we once knew.

The Friday after Betty Ann arrived on the scene, Susan twirled her pencil, leaned back in her desk, and waited for the best composition of the week to be read. Hers, of course.

Only it wasn’t. It was Betty Ann’s, and it was about a black poet named Langston Hughes and how he had become a spokesman for his people. Susan’s stories were always about horse shows or opening nights.

We’d never heard of Langston Hughes. Besides, this was an all-white private school. Martin Luther King was being nailed by most of the adults we knew. All in all, it was a real bomb to have Betty Ann go on about Langston Hughes’s “Black Nativity” and his description of the “maple-sugar child” and how he thought Carl Sandburg’s poems fall on the page like blood clots of song from the wounds of humanity.

In Susan’s stories, the “telephone jangled” and “the rainbow painted the sky.” Stuff like that. Betty Ann was writing about the civil war in Spain and the black ghettos of Harlem. Langston Hughes was from Cleveland. We might have guessed.

Mrs. Johnson came to the part in Betty Ann’s composition where Langston Hughes writes a poem about how he likes watermelon so much that if he should meet the queen of England, he’d be proud to offer her a piece. That was when Agnes Matherson’s eyes caught mine (or was it the other way around?) and we started imitating the queen of England eating a piece of watermelon. The whole class burst out laughing. The rest of the story was never read, and everybody but Betty Ann had to say after school and clean blackboards. The next day at lunch, Betty Ann found a note under her lettuce saying we were sorry, but the cafeteria was sh’ nuf out of watermelon.

After that, she became the class joke. What she wore, what she said, what she ate somehow always gave one of us an idea for a wisecrack. There was a kind of one-up-manship about getting Betty Ann that had less to do with Betty Ann than with our own jungle mentality. I know that now, but i didn’t think about it then. She became a pawn.

She started getting sick a lot. There’d be whole weeks when she’d miss school, but the Betty Ann stories went on even without her. She came to our school from another planet. She was our little moron, our Polack, our village idiot.

Then one day, Betty Ann and I were assigned a project together. Everyone had selected a partner, and I was out of town at a school swimming meet the day the assignment was given, so I got stuck with Betty Ann. Everyone kidded me, and I laughed with them.

The day before the project was due, I had to go over to her house after school to work on it with her. Her mother fixed a plate of cookies and kept coming into the room to see if I wanted more Coke or anything. She said I was the only one of Betty Ann’s friends who had come over after school, and she was glad to meet me.

The phone rang while I was there, and it was for me. Betty Ann’s mother was in the kitchen when I heard Margie giggling at the other end of the line: “Have you eaten any maple sugar candy or watermelon, kiddo?”

She waited for me to snicker an undercover laugh.

I saw Betty Ann’s mother just standing in the kitchen with her back to me, pretending not to be listening. It was as if she had heard everything. I hung up. I think it was at that moment when i began to see what we had been doing.

BETTY ANN’S MOTHER: “Why don’t you girls like Betty Ann? She likes you. . . ”

Nobody had ever asked me a question before or since that made me feel so stupid.

If kindness could kill, Betty Ann would have been dead in a week. But it was too late. Her parents moved her to another school, then we heard later that she’d had a nervous breakdown. Once, years later when I was home from college, I saw Betty Ann in the doctor’s office. She didn’t even recognize me.

Sticks and stone only break bones. Words can shatter the soul. A little, quiet, picked-on 10-year-old runs away because the kids on the bus laugh at him. A sensitive ninth-grader flips out because a group of self-rising girls decide to throw her to the wolves. We tell ourselves it takes more than that to send someone over the edge. Maybe so, maybe not.

But there are no erasers.
```

---

## IC-2192: Between Shades of Gray

- Title: Between Shades of Gray
- Author (byline): Ruta Sepetys
- Work: Not specified
- Publisher: Speak
- Publication date as stated: April 2012
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: LINA, JONAS, MAMA, OFFICER, ONA, DOCTOR, GUARD
- Teaser before the introduction: Yes
- Spoken words (computed): 1239
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ruta Sepetys
ISBN: 978-0142420591
Publisher: Speak
Date (Month/Year): April 2012
```

### Introduction (context only: never use it for content warnings)

```text
The year was 1941. While Adolf Hitler orchestrated his “Final Solution” against the Jewish population, Joseph Stalin took the opportunity to target “anti-Soviet” elements in the Baltic States where anyone with a prestigious job, regardless of religion, was viewed as a potential threat to Stalin’s power.

Overshadowed by the atrocities of Hitler’s extermination camps, history is eerily quiet regarding Stalin’s Great Purge. More than a million people from Estonia, Latvia and Lithuania were loaded onto cattle cars. The destination: forced labor camps in Siberia.

This is the story of Lina Vilkas, only 15 when Stalin’s Great Purge begins. Can Lina keep her humanity as she navigates . . .

Between Shades of Gray by Ruta Sepetys
```

### Performance text (classify this)

```text
LINA: (Pg 26-27) They were taking Jonas. My beautiful, sweet brother who shooed bugs out of the house instead of stepping on them.

JONAS: Mama! Lina! (he hangs his head and cries)

LINA: Mother grabbed the officer and began speaking in Russian – pure, fluent Russian. The officer jerked Jonas toward him. His body began to vibrate as sobs wracked his shoulders. Mother pulled a bundle of rubles from her pocket. Her hand flew up and ripped the amber pendant from her neck and pressed it into the officer’s hand. He didn’t seem satisfied. Mother pulled a pocket watch from her coat. I knew that watch. It was her fathers’ and had his name engraved on the back. The officer snatched the watch and let go of Jonas. Have you ever wondered what a human life is worth? That morning, my brother’s was worth a pocket watch.

MAMA: (Pg 7) (frantically) Shoes, Jonas, extra socks, a coat! Lina . . . Hurry!

LINA: (Pg 11) The door burst open and three officers entered our house carrying rifles with bayonets. Mother looked in the foyer mirror to put on her hat. The officer slammed her in the shoulder with the butt of his rifle, throwing her face-first into the mirror.

OFFICER: Bourgeois pigs, always wasting time. You won’t need that hat.

MAMA: (flatly without making eye contact) Pardon me.

LINA: Pardon me? These men burst into our home, slam her into the mirror and she asks them to pardon her? Then she reached for it, the long gray coat, and suddenly I understood. She was playing the Soviet officers like a careful hand of cards, not quite sure what might be dealt next. I saw her in my mind, sewing jewelry, papers, silver and other valuables into the coat’s lining.

OFFICER: (Pg 13) Davai! (Hurry!)

LINA: We marched into the intersection of the street toward a truck surrounded by more NKVD* (Pg 14) We were all on the list. I didn’t know what the list was only that we were on it. Apparently so were the other fifteen people sitting inside on their luggage. (Pg 15) I squeezed my eyes shut. The truck stopped in front of the hospital. Waiting. A woman who was also on the list was giving birth to a baby. As soon as the umbilical cord was cut, they would both be thrown into the truck.

ONA: (Pg 20) (Screaming) My baby! Please don’t hurt my baby!

DOCTOR: Please, you cannot take the newborn. It won’t survive! Sir, I beg you. Please!

LINA: The officer turned to the doctor and kicked the heel of his boot into the doctor’s kneecap. They lifted the woman into the truck. The baby was handed up. I held the bundle and instantly felt the warmth of its little body penetrating through my coat. The child let out a soft cry and its tiny fists pummeled the air. Its fight for life had begun. (Pg 21) The child had been alive only minutes but was already considered a criminal by the Soviets. (Pg 23) We arrived at a small train depot in the countryside. A deserted area, surrounded by dark woods. Soviet trucks filled the rail yard, packed with people just like ours. I pictured a rug being lifted and a huge Soviet broom sweeping us under it. (Pg 29) Wooden train cars lined the platform, stretching as far as the eye could see. They were crudely built and dirty, the kind that would haul livestock. Masses of Lithuanians thronged toward them. White knuckles clutching suitcases. People on their knees yrying bags with twine while officers stepped on the contents. (Pg 35) I counted the people – 46 packed in a cage on wheels. Faces spoke to their future. Courage, anger, fear and confusion. Others had already given up. Which was I? (Pg 41) The back of our train car had Russian writing on it. Thieves and prostitutes. Mothers were in that car. Along with a teacher, a librarian, elderly people, and a newborn baby – thieves and prostitutes. (Pg 49) Two Soviets pulled a priest down the platform. His hands were bound and his cassock was dirty. Why a priest? But then . . . why any of us?

MAMA: (Pg 51) Stalin has a plan. The Kremlin will do anything to see it through. He wants Lithuania for the Soviet Union. I imagine he’s doing the same to Latvia, Estonia and Finland.

LINA: (Pg 55) I hated them, the NKVD and the Soviets. I planted a seed of hatred in my heart. It would grow to be a massive tree whose roots would strangle them all. I looked around the train car. No one spoke. How could we stand up for ourselves if everyone cowered in fear and refused to speak? (Pg 62-63) While I devised a plan, the women in the car showed constant concern for the baby, who could not seem to nurse. We rolled for days, stopping in the middle of nowhere. (Pg 50) A guard approached and handed up a bucket of water and a buckry of slop.

GUARD: (Pg 64) One person! Two buckets! Any dead bodies in there?

LINA: Ona was quiet. Her baby was dead.

MAMA: (Pg 71) Ona, dear. Give me the baby.

ONA: (begging) Don’t give her to them. Please!

MAMA: We will not give her to the guards. I promise. We’ll wrap her in something beautiful.

LINA: (Pg 75-76) We tried for three days to sneak Ona’s baby out. The smell of rotting flesh had become unbearable in the hot car. Ona finally agreed to drop the baby down the bathroom hole.

ONA: (whimpering) She’ll be crushed on the tracks. . .

LINA: Mother moved toward Ona. Before she reached her, Miss Grybas snapped the bundle from Ona and threw it down the hole. (gasp) (Pg 82) Ona was only a few years older than me. (Pg 78) Weeks . . . I lost track of how long we had been traveling. I stopped watching for bodies to be hurled from the cars. Every time the train pulled away, we left a litter of corpses in our wake. Would someone bury them, or would they believe they were really thieves and prostitutes? (Pg 80-81) After six weeks and the third day without food, the train stopped. We heard clanking. The guards opened the door and said we would be getting out. Finally. My entire body trembled at the shock of daylight. The NKVD had bayoneted rifles at the ready.

ONA: (Pg 94) (crying and rocking back and forth unconsolably she chants) No, no, no, no!

LINA: (Pg 101) She could not be calmed. The commander saw Ona standing up, sitting down, and pulling her hair. He stepped up and pulled her from the truck.

ONA: (Pg 94) No, no, no, no! (Screaming and clawing at him as if being drug by her hair)

LINA: (Pg 101) She was no match for his height or strength. He threw her to the ground. His eyes narrowed. His jaw tightened . . . (in horror) He pulled out a pistol and shot Ona in the head. (long beat, then with little emotion -- dazed) (Pg 102) Blood, the color of thick red wine. Leg splayed out in an unnatural angle. One of her feet was missing a shoe. Ona’s body got smaller and smaller as we drove away. She lay dead in the dirt, murdered by the NKVD. Somewhere hundreds of miles away, her daughter decomposed in the grass. (long beat, reflective) (Pg 163-164) My art teacher said if you breathed deeply and imagined something, you could be there. I learned to do that. I clung to my rusted dreams during times of silence. At gun point, I fell into every hope and allowed myself to wish from the deepest part of my heart. (Pg 112) What had happened to Ona? Was she in heaven with her daughter? Or was she floating amongst the trains and masses of Lithuanians, searching for her husband? ****** (Pg 3) They took me in my nightgown. Thinking back, the signs were there – family photos burned in the fireplace. Mother sewing her best silver and jewelry into the lining of her coat. Only later did I realize that Mother and Father intended we escape. We did not escape. We were taken . . . June 14, 1941.
```

---

## IC-2193: Big Brother

- Title: Big Brother
- Author (byline): Paula W. Peterson
- Work: Women in the Grove
- Publisher: Beacon Press
- Publication date as stated: April 2005
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: TERRENCE, KEITH, NICKIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1722
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paula W. Peterson
Book: Women in the Grove
ISBN: 978-0807083857
Publisher: Beacon Press
Date (Month/Year): April 2005
```

### Introduction (context only: never use it for content warnings)

```text
Being a single-mother is difficult under the best of circumstances . . . but when you are also dealing with HIV, daily parenting issues can become completely overwhelming. In this selection Big Brother by Paula W. Peterson, Nickie is doing her best to hold it all together and has signed up with the Big Brother program for her son Terrence. Maybe a big brother can provide the stability Terrence needs. Big Brother by Paula W. Peterson.
```

### Performance text (classify this)

```text
My man Eugene been dead about a year and a half by now, and soon this Big Brother gonna come along. I say last thing I want around here is another man. But the social worker say Terrence suffering for lack of male companionship. Although, shoot, when his daddy was alive he didn't have hardly no more male companionship than he have now, and I don't see what difference it going to make in his life.

It true that Terrence sure be acting funny. Most evenings he too wound up to fall asleep, so he come crawl on the couch with me while I watch the news. Terrence - he big for eight year old - with a head packed with stubbornness. He always asking questions.

TERRENCE: Momma, what that lady kill her five kids for? . . . What country that? Israel? Why they screaming and throwing rocks at each other, huh? I don't pay no attention to the TV no more. I just like to have it on 'cause it keep me from thinking too much. I don't get no relief. Just when I fall asleep, he shake my shoulder, hard, and put his big old face right in mine until I wake up and the first thing I see is his eyes, big and brown with those long trembling lashes and he spluttering, "Momma! Momma! I think yo' skin is getting blacker. Wake up!"

The medications I take are changing the pigment in my skin, ain't nothing I can do about it, and it true, sometimes when I look in the mirror I think it look like I been rubbing coal on my face. Terrence worried his momma gonna turn so black she gonna disappear. So he got to keep me conscious at all times to make sure all that blackness don't swallow me up. That child wear me out. He got a way of draining you with all his needs. Ain't it my turn to rest now, I think, ain't I been through enough already? But I know Terrence need more and I can't bring him out of this craziness on my own.. And that another reason why I say, OK, bring that Big Brother on. When I see him I think, uh-oh, what they sending me here. One of them rich white dudes trying to pretend like they's poor. You can just tell. Ain't no way this gonna work out. I bet he no more than twenty year old. Not even that.

KEITH: Hi, I'm Keith. (holding out his hand to shake)

NICKIE: I'm Nickie, and this my boy, Terrence.

TERRENCE: What that say on your shirt?

KEITH: This? This says Tanglewood Music Festival. That's a . . . well, this kind of summer camp for musicians . . . back East. I used to play the piano . . . but that was a long time ago. Like in another kind of life.

TERRENCE: How come you don't play no more?

KEITH: I just gave it up, that's all. It didn't, you know, it didn't have the same kind of meaning, like, that it used to have for me.

TERRENCE: You gonna play again someday?

KEITH: (sadly) Maybe. I don't know . . . Probably not?

NICKIE: Terrence, quit your nosiness.

KEITH: (shaking his head) No, no, that's OK. Hey, Terrence, man, show me your room, OK? I bet you got a great room?

But there are some things I need to get straight with Big Brother right away, so I say,

NICKIE: Excuse me, Keith, could I have a word with you? Now I know you know I'm HIV cause this HIV housing. But I want you to know that my boy Terrence ain't HIV, in case you was wondering. And he don't know nothing about it, neither, so I'd appreciate it if you didn't talk about that with him.

KEITH: That’s cool. (clears throat, nervously) Terrence seems like a great, kid. I think we're gonna get along.

NICKIE: Terrence stubborn. He stubborn and he willful. . He never pay attention to what people say. If he don't do what you tell him, you come talk to me about it . . . How old you be?

KEITH: Nineteen . . . (nervously) Umm-hmm. And how about you, Nickie?

NICKIE: Me? Thirty-one.

KEITH: Thirty-one. That's a great age. I'd like to be in my thirties, cause that's when you have it all together, you know what I mean? This guy crazy, I think. After that Big Brother come once a week, and sometimes he take Terrence places like the zoo and the beach and the big playground in Golden Gate Park with the long slides Terrence like so much. Terrence bragging about him to all his school friends, I know it. Minute he get on that school bus in the morning he just busting with all the stuff he got saved up to tell, and it don't matter who he tell it to, he collar the first kid he sit next to on the bus and pin him down till the ride is over, saying, "You know what me and my Big Brother done yesterday?" One time Big Brother bring over an electric keyboard he borrowed off of someone and teach Terrence how to play his scales. Then he play something for Terrence, something long and slow and soft. I listen in, standing in the hallway. Big Brother can see me, all right, but he don't let on. The music so pretty I have to hold my breath so I won't miss none. And sad. The sadness creep up on me little by little till I just standing there with my throat closed up with grief, tears ready to squeeze out. When he finish, he look up at me quickly, to make sure I'm still there.

KEITH: (proud and excited) I got that in my head. I remembered it. I still remember it, I didn't know that. Then he sneak a glance at me just to see am I proud of him. I can't help thinking, Big Brother, do your momma know where you is? He want someone to put out cookies and milk for him. He looking at me hopefully, but I think to myself, hell, boy, don't you know that I ain't got nothing left over for nobody? That Eugene took it out of me. Took it all out, and then give me something I can't ever get rid of. Men is all children, it don't matter how old they are or how big they are. Unh-uhn. All that business ain't for Nickie no more. One week Big Brother show up too early. He know that Terrence don't come home from school for another hour. I mad at him. I be tired and diseased and I ain't even good looking no more. I got a right to be left alone. I think, why he messing with me, anyhow? Dumb kid.

KEITH: Nickie, can I ask you a question? . . . Are you afraid of dying? . . . OK, OK, I know that's kind of personal, but I just thought I'd ask because you seem to be so strong. I think of you as the kind of person who's made her peace with death. I know you're not up at three in the morning worrying whether if you're in a coma someone's going to mistake you for dead and bury you alive . . .

When I see you, I see someone who's so beyond that. Fear. What this boy babbling about?

NICKIE: Where you get all these crazy ideas? What you worrying about all that bullshit for? You know how to play the piano, why don't you do that. Ain't that enough?

KEITH: What good's playing the piano. . . (looking down at his hands, he continues softly) I got it too, Nickie,

NICKIE: You got what? But then, a second later, I know what he talking about and I feel bad for asking.

KEITH: (leaning back and pinching the bridge of his nose; he shakes his head) This is bad, man. Oh man, this is bad. (still trying to stop crying) Oh God, I got to stop this.

NICKIE: It ain't no death sentence no more. Look at me, I'm still kickin?' Maybe that just the problem, I think, suddenly. It ain't dying, it living that give us such a hard time. I don't know how to do it no more. Everything I once knew about it don't mean nothing now. My heart feel heavy. I can't go on with no pep talk.

NICKIE: Where you from, Keith?

KEITH: (mumbling) Hillsborough . . . Well, I used to be from there. I don't consider that to be home anymore. I mean, my parents made it pretty clear they don't want me to come back. After they found out what was wrong with me my dad told me my mom had a nervous breakdown and that, you know, she couldn't, like, bear to see me. I think my dad's pretty disgusted with me too.

NICKIE: Was you on the down low or something? (to audience) He don't get my meaning. I explain it to him

KEITH: Oh. Well, just a couple of times. It was just a phase I was going through. I have this theory that we're all, like, designed to be attracted to both sexes, but the balance is different in each person. It's really interesting when you think about it . . . But I'm not gay. . . This Big Brother stuff has been great. It's really helped me change my perspective on the whole thing. Playing with Terrence, and meeting you, Nickie - just watching how you are. You're great. I mean, that first day I met you and you were so upfront about having HIV - you just said it. I admire that. I knew you were someone I could talk to about it. Be open. I don't - well, I don't really know anyone else who's positive.

NICKIE: Everybody I know is positive . . . And there ain't nothing to talk about.

After that I know I got things to sort out in my mind. This Big Brother has turned into a situation on my hands. Now I know all I have to do is call the agency and they take him away, it simple. Poor Big Brother so stupid, he don't even begin to know how the world work. Thinking how stupid he be get me to feeling sorry for him, and that ain't good. Also I think, well, Terrence be much happier now that Big Brother around, and that the truth too. He chilled out a lot and he not acting up in school so much. And then I think Big Brother seem happier too, since he begun playing with Terrence. He like teaching Terrence the piano. That one thing in life he do know something about. . . . Who I think I am, acting like I don't need nobody or nothing?
```

---

## IC-2194: A Big Mean Pair of Scissors

- Title: A Big Mean Pair of Scissors
- Author (byline): Quinn Cummings
- Work: Notes from the Underwire
- Publisher: Hatchette Books
- Publication date as stated: July 2009
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2205
- Already set (do not supply): none

### Source block (context only)

```text
Author: Quinn Cummings
Book: Notes from the Underwire
ISBN: 978-1401322861
Publisher: Hatchette Books
Date (Month/Year): July 2009
```

### Introduction (context only: never use it for content warnings)

```text
More than 35 years ago, AIDS was called "The Gay Plague," gay cancer, or GRID (gay-related immune disorder). Sadly, because AIDS was first detected in homosexual males, it was largely dismissed because gay men circa 1980 were viewed as dispensable. The medical community considered this a homosexual disease, neither fashionable nor prestigious, and consequently unworthy of serious attention. They were wrong!

The most recent statistics compiled by the UN in 2015 reports that 36.7 million people worldwide are now living with HIV/AIDS, of these, 1.8 million are under the age of 15. Nearly 22 million people have died of AIDS-related causes since the epidemic began.

A Big Mean Pair of Scissors by Quinn Cummings
```

### Performance text (classify this)

```text
I grew up in the hills above West Hollywood. Every Halloween, my mother and I would make a lonely trek through the neighborhood where, at any given house, my "Trick or Treat!" would produce a man dressed as either Maria Callas * or Marilyn in The Seven Year Itch *. For a long moment, he would stare at me in confusion then say something like, "Everyone, come here and look! It's a child!" At which point more men in festive regalia would crowd the doorway and goggle at me for a bit, apparently having forgotten there was another segment of the population allowed one night a year to wear something ridiculously bright and sparkly out in public without recrimination.

I always liked the men in our neighborhood. I had every intention of growing up to be a gay man in the West Hollywood hills. They had gorgeous clothing, gorgeous houses, gorgeous boyfriends, and gorgeous dogs.

[It was] Not long after I turned fourteen, [that] I saw one of the longer-time residents out walking his dog. I hadn't seen him in many weeks and I was shocked. He had lost twenty pounds at least, and there were coal-black rings under his eyes. Something told me not to ask. He was dead within a month. He was the first person I knew who died of AIDS. I don't remember who the second and third were, because they started going so quickly. I stopped noticing the sound of the ambulance racing up our hill.

AIDS was a big mean pair of scissors in West Hollywood.

I made a decision: I was going to stop AIDS. I was eighteen, I had no medical training and a habit of covering my eyes and squealing when they inserted a fake IV on hospital dramas, but these were incidental details I could overcome. I was going to stop AIDS.

As it turned out, the workers at the front lines of the battle against AIDS didn't fall to their knees and scream "HUZZAH! She's arrived!" when I called AIDS Project Los Angeles. What they said was, "We need help in the office. Can you file?"

I sulked a bit. I can file, but where's the life-saving potential in that? "Anything else?"

I could hear him flipping through pages. "Oh, you're in luck," he finally said, "there's a hotline training class starting this week."

"Hotline?"

"Yeah, we have a national hotline for information and support. It can be anything from finding a local clinic for people to get tested to helping someone who's just gotten a positive test result to . . . everything, really."

I would work the hotline. I would give people valuable information. I would be useful.

I had several weeks of training before they'd let me answer a phone. In a class of several dozen, I was one of three women. I was the youngest trainee by eight years. I brought several sharpened pencils and a notebook with "Hotline" carefully printed across the front. One of these facts made the teacher pick on me from day one.

He was gorgeous-a six-foot-five-inch-tall black man with the effortless grace of an athlete and the humor and affect of a very tall and very tan Bette Midler.. Near the end of every class, he would bring one of us up front to roleplay a hotline call, with him as the caller and the student assuming his or her role as hotline advisor. Of course, being all enthusiasm and no experience, I was summoned to the front of the class four times out of five. I was a golden retriever puppy taking on Chernobyl.

I persevered. After forty hours of class, I had a working knowledge of the major and most of the minor sexual habits of the North American Homo erectus. I had also developed the ability to work needle-cleaning protocol into casual conversation. We, as a class, were ready to serve, but the teacher had one final lesson to impart. He leaned against a chair, crossing his arms and his endless legs, and looked at us deeply. "Four friends of mine and I sat in an apartment and started what has become this organization. I'm the only one left. I don't know why I'm still alive, but I do know why I'm still able to work here. I go to the gym every morning. I put on my Walkman, and I don't talk to anyone, and I don't think about this place. You went through this because you want to help, but don't overdo it. The hotline takes more out of you than you know." He then lectured us on the symptoms of burnout, which I carefully wrote down in my "Hotline" notebook so I could more effectively monitor my classmates in the months to come. I was going to be fine, but I could tell that some of these people weren't going to be able to keep things in proper balance.

My first shift was on a Saturday morning. I sat at a cubicle with a three-inch-thick binder in front of me, which represented the sum total of medical information and support for AIDS patients in the entire United States. An inch of that represented California and another inch New York. The final inch was the other forty-eight states with a page or two for Canada. Within minutes, the phone rang and I answered, "AIDS hotline, how can I help you?" with only the tiniest quaver, all the while thinking Please don't be crying, please don't be crying, please be some-thing I can answer.

A brisk male voice said, "Hi, I need to get tested in Orange County, California." I nearly giggled in delight but checked the impulse, deciding this was not the image I wanted to present. I gave him his testing options, wished him luck, and hung up.

On the weekends, there was a steady stream of "Yeah, I had a teensy bit too much tequila last night, and I never do this, but . . . how long do I have to wait to get tested?"

If I worked a weekday, I'd get calls from suburban moms who had watched a documentary the previous night about how AIDS was about to inundate the heterosexual community, and who had spent the entire night obsessing over their college boyfriend who, in retrospect, might have liked musical theater just a little too much. Telling them how unlikely they were to have been exposed to AIDS in the early seventies at Iowa State would ease their fears, but they'd still want a local test site, which I would gladly provide.

About fifteen percent of the calls were the Misfit Toys. For these people, the hotline served as a form of solace and an unending source of entertainment. Thanks to our 1-800 number, they could pick up a phone and talk endlessly about their deeply held suspicions about how AIDS could be contracted from houseplants, or escalators, or doorknobs. Doorknob Guy was a frequent caller, and getting a new hotline volunteer was like Christmas and his birthday rolled into one. The new volunteer could be coaxed into a forty-five-minute trip down the rabbit hole where AIDS patients had sneezed into their hand-that sneeze carrying a trace of blood-then touched a doorknob and left AIDS viruses writhing and throbbing, waiting for their next victim.

The first time I got him, I spent almost half an hour before hanging up the phone, exhausted and headachy from trying to explain epidemiology to a lunatic, only to hear the phone in the cubicle next to mine ring. The phones rang in order and I just knew it was Doorknob Guy, fat and sassy from our conversation and hungry for a new victim. The volunteer next to me, a seasoned vet of several months, picked up the phone and said, "AIDS hotline, how can I help you?" He listened for a few seconds and then said waggishly, "Sweetie, it depends on what you do with that doorknob," then hung up sharply and turned to me, a pleasant expression on his face.

"And that's how you handle Doorknob Guy," he said with finality.

Not every phone call was productive; some were fairly unpleasant, thanks to the percentage of the population whose own version of Jesus hated us very much and needed us to know that. Nonetheless, each shift generated at least one call where I could tell myself, "I helped him

Within weeks, I'd grown polished and confident. I was a seasoned veteran. Nothing I heard surprised me. I was the one slamming shut Doorknob Guy to the wonder of the newer volunteers. I was never at a loss for words, never judgmental, never shocked. Every week, there were more people wanting to get tested, more people looking for health care after they'd tested positive, and more people calling for the list of mortuaries who would take people who had died of AIDS. In six months, the call volume doubled. I worked the phones, I heard stuff, and I kept it to myself.

There were group stress-reduction sessions for the hotline volunteers--but I never bothered to go. I was helping. I didn't need help.

The call came on a quiet weekday morning. The caller was sobbing so hard it took her a few minutes to collect herself enough to explain what she needed. She wasn't calling for herself. She was calling for a friend, a sorority sister. The entire sorority had gone, en masse, to get tested, and they got their results this morning. Her friend, eighteen and with one sexual partner, had tested positive. My brain raced. Was this a hoax? It didn't matter if it was; I had to treat it seriously either way. But if it was a hoax, this girl needed an agent. My inner lie detector said it was probably legit, the only question being whether this "friend" was, in fact, my caller. I asked what state she was in and when she told me, I nearly burst into tears myself. She was calling from the Southern state with only one page of medical and psychological support in place-actually half a page-and nothing specifically for women. I gave her what I had, and tried to calm her down enough to see this wasn't an immediate death sentence-although.

The call ended. I hung up, and then I stood up. I said to no one in particular, "I'm cutting out early," and I left. I got to the parking lot, sat in my car, and switched the radio off because I couldn't stand the noise. I then switched it back on because the silence was overwhelming. My brain couldn't find anywhere to land. I had started working at APLA (AIDS Project of Los Angeles) so I could help the gay community in which I had grown up and the addicts who weren't capable of shaking an addiction that was going to kill them unless they took care of themselves. This was the first phone call where it occurred to me that the them in the AIDS epidemic might look a lot like me. I couldn't save my neighbors or my fellow human beings, but what kind of an ass was I that it finally broke my heart when the caller looked like the person I saw in the mirror?

I stopped in to see the hotline supervisor and mumbled my complaints. The job wasn't any fun, or I wasn't good at it, and it was because I got this one call. I had been fine until this one stupid call, which made me feel itchy, sad, and really angry. Besides, everyone else kept talking when I was trying to take a call and no one ever made a fresh pot of coffee, which sucked even freshly made, and it would have been fine if I just hadn't gotten this one call. Finished, I slumped farther down in my seat. My mentor sighed deeply.

"How many support meetings did you attend?" he asked. (silence) "So, none. Lost enthusiasm for the job. Irritable. No longer confident in your ability, right? That college girl may have been your last straw, but it's burnout, Quinn. Remember? Take a month off. See if your heart is in it after that. You've been volunteering how long?"

I thought. "Six months." It seemed longer.

I took off a month, and then two. Three months later, I didn't go back. I beat myself up plenty over that. A few more neighbors were sick, a couple had died, and I still didn't go back. I didn't help because I couldn't help. A teenage girl with a notebook full of phone numbers wasn't going to change a damn thing.

CLOSING More than thirty years ago AIDS was terrifying, deadly and spreading fast. Today, although we still haven’t discovered a cure for AIDS, we do have the means to treat those who test positive for HIV, the virus that causes AIDS. A diagnosis of AIDS is no longer a death sentence; people can live long, happy and fulfilling lives with the proper treatment. Who knows . . . in the next 30 years maybe, just maybe, we will find a cure.
```

---

## IC-2195: Blown Sideways Through Life

- Title: Blown Sideways Through Life
- Author (byline): Claudia Shear
- Work: Not specified
- Publisher: Dell Publishing Company, Inc
- Publication date as stated: April 1996
- Event as filed: Prose
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

And then I carry up cases of beer, tubs of chicken, stacks of documents, flats of eggs, trays of lipsticks. I set up the computer, the desk, the stock. I read the documents, chop the onions, wash the walls, wash the dishes, answer the phone, answer the phone, answer the phone.

(answering phones)
• "Good afternoon, Battle, Fowler, Jaffin and Kheel. . . "
• "Good morning, Shakespeare Festival. . ."
• "Buona sera, Le Madri. . . "
• “Medical Center Patient Information, what room,
please?"
And they tell me . . . (various boss voices)
• "Chill on the conversation."
• "Be nice to the customers!"
• "Put your book away! No reading allowed!"
• "Here's a club in case they come to rob the restaurant
when I'm not here."
• "Remember to always give your name."
• "Never give your name!"
And then, later, I hear, (various boss voices)
• "Uh, there's been complaints about your attitude."
• "You were heard whistling in the elevator. . . "
• ". . . singing in the dining room . . ."
• "You talk too much . . ."
• "Your laugh is too loud. . . "
• "No standing around! Look busy!"
And my personal favorite: "I don't have to give you a
reason. It's my restaurant!"
And finally: (various boss voices)
• "Listen, we're going to have to let you go. . . "

• "Oh, this is your last shift."
• "Well, it's my way or the highway."
• "You're fired!"
And every time I just say, (with growing frustration) "All
right, all right, all right."

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

---

## IC-2196: Blues Ain’t Nothin but a Good Woman Feelin Bad

- Title: Blues Ain’t Nothin but a Good Woman Feelin Bad
- Author (byline): Shay Youngblood
- Work: The Big Mama Stories (Pg 61-66)
- Publisher: Firebrand Books
- Publication date as stated: May 1989
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MISS BLUE, NARRATOR, BO WILLIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1359
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shay Youngblood
Book: The Big Mama Stories (Pg 61-66)
ISBN: 978-0932379573
Publisher: Firebrand Books
Date (Month/Year): May 1989
```

### Introduction (context only: never use it for content warnings)

```text
During the 1930s, The Blues was music created by African Americans of the Deep South. It was the music of front porches and ramshackle juke joints that encouraged dancing, drinking and music. It was the music of love and pain.

Musician Wynton Marsalis once said, “Everything comes out in blues music: joy, pain, struggle. Blues is affirmation with absolute elegance. It’s about a man and a woman. So, the pain and the struggle in the blues is that universal pain that comes from having your heart broken.”

And Miss Blue’s heart was broken . . .

The Blues Ain’t Nothin but a Good Woman Feelin Bad by Shay Youngblood
```

### Performance text (classify this)

```text
MISS BLUE: (singing and upbeat) The Blues Ain’t Nothin but a woman wanna see her man . . . (repeat)*

NARRATOR: (Pg 61-66) Miss Blue lived down the block. She useta sit on her front porch watching TV from eight o’clock in the morning till near dark. First thing in the morning she come out her door in a short housedress in summer, or a raggedy wool robe in winter, with pink sponge hair rollers in her short graying hair. She would haul out her lil black-and-white TV and put it on top of the big gray metal garbage can two feet in front of her.

[And] At night I’d hear her singing the blues. [She] used to sing the blues for a living till her heart started failing. She’d lived through three heart attacks. [One day] something set Miss Blue off on the past and she started talking about love and pain. The way she talked, there wasn’t one without the other.

MISS BLUE: I been in love too many times to count. If love was a dollar bill I’d be a millionaire, and if pain was a quarter it’d be triple. All I got now is my memories – some good, some bad. Like June of 1923.

Me and Bo Willie Peeks met in a juke joint I was singing in. I wasn’t no more than twenty-four or twenty-five years old, and he was the first man I really let love me and the first man I truly give my heart and soul to. Now there was plenty mens round. Mens that made me feel like a star. But Bo Willie took my mind. When I met him, he was married and tipping out on his wife. I never figured he'd tip out on me, and that was my downfall. (hums softly as she imagines herself on stage)

He would sit at a table up front. Chills run up and down my spine when I catch his eyes all over me. Wasn’t long before he was waiting for me after the show. One night he come up to me at the bar and he says,

BO WILLIE: Hey sweetmeat, what’s cooking?

MISS BLUE: I didn’t know what he was talking bout. I wasn’t hip then. I was so nervous, sweat start popping off my face.

BO WILLIE: You what’s cooking, sugar pie. Your cooking is fine as wine and you look good enough to eat, mama.

MISS BLUE: That man drowned me with sweet words and kindness. Treat me like a queen. I wasn’t useta that kinda treatment. You see I knowed I was jet black and didn’t have no hips and wasn’t particularly pretty, but he made me feel like I was the most beautiful Black creature breathing air, and I almost believed him. He was the one made me feel like I was somebody special.

Don’t get me wrong, he wasn’t nowhere near perfect. He drank a lil, and he’d be mean to me, call me an ugly baboon, or talk bout my bug eyes. But usually he was good to me. He begged me on his hands and knees to marry him. I didn’t really feel ready, but he kept on bout how good we was together, how much he love me, and how much he could do for me. After awhile love did cloud my eyes up.

Bo Willie got a good-paying job on the railroad and said he was ready to settle down with me. [So] finally I give in and told him I’d marry him. Chile, he was my thunder and honey. He was all I could see, smell, taste, or touch. We made plans to get married the day he got back from a three-week trip up to New York. I was so happy I smiled all the time, and strangers on the street started asking me if I was in love. I couldn’t do nothing but shake my head and grin . . . He called me that first week saying he was lonesome.

BO WILLIE: (teasing) These gals in New York bout to drive me crazy. A man cain’t go to a bar for a drink without em all over me.

MISS BLUE: (also teasing) I hope you tell em you good as married.

BO WILLIE: (laughing) I do, but it don’t matter none to these gals in New York.

MISS BLUE: I wasn’t worried. He was a good man. Told me he was tired of running round and wanted a wife and a settled life, and I was ready to kiss his feets and bear him a house full of children. [So] I went shopping for my wedding dress – a real expensive white woold suit with pearl buttons – and white gloves, shoes, pocketbook, and hat to match.

The day Bo Willie was to arrive at my mama’s house for the wedding, one hour before the preacher and guests was to come, [he] call me and told me he had another gal. His words cut me to the bone. He say he still love me, but he met this woman. He say he didn’t want me to marry him and be miserable. Hmph!

I loved that man so much I told him I didn’t care bout no other woman, I’d take him like he was if only he’d come to the house that minute and say yes before the preacher. He said he was still in New York and didn’t know if he was really ready to settle down. I ask him if I could come where he was so we could talk, and he flat-out refused. Then I got mad, remembering his sweet lies of loving me to the grave.

(with growing anger) Bo Willie, you a no-good lying dog. If you was on fire, I wouldn’t waste my spit on you. I hope you die choking on your own vomit. You have made a hard bed, now lay in it. You gonna be sorry through, you gonna miss me. Everything you touch is gonna turn to s***, dry up like dust and blow on the wind.

I slammed the phone down and cried for two days solid. For a week I didn’t sleep, eat more than a slice of dry bread and a half cup of coffee. Food lumped up in my throat thinking bout him with another woman. I wanted him dead, boiling in his own blood. I wanted him to hurt my hurt.

One night I was walking the streets, going from joint to joint trying to find him, and I saw him. He was by hisself, getting outta a brand new fishtail Cadillac. I rushed over to the car and swung open the door on his side. I know I scared him cause I looked like a haint. My hair was standing up on my head, I hadn’t changed my clothes for three days, and my eyes had murder in em. I snatched him out the car and was quick on him like white on rice. I hadn’t had no food in days but I found the strength to knock him on the ground. Then I got in the car, shifted in reverse, and tried to run him down like the dog he was. He was lucky I smashed into a telephone pole fore I flattened his a**. I just broke his leg and run over his foot.

I got out the car and walked home with my head up. Took a long hot bath and lit a seven-day candle to ask to be released from him and get my mind back. But I left part of me back at that wreck. (beat) Love hurt. I really had something to sing the blues bout then. That same year I made a hit record, my only record, ‘The Blues Ain’t Nothin but a Good Woman Feeling Bad.’ (long beat)

I heard a few months after I wrecked his car that the woman he was with took all his money and left him and he lost his job on the railroad. (pause) You know something, I hope to this day that sorry son-of-a-b**** is still sucking rocks. One good thing done come out of all that though, and that was a song. It was blue but it was a song. A damn good one, too. . . (she begins to sing low and sadly this time) The Blues Ain’t Nothin but a woman wanna see her man . . . (repeat)*
```

---

## IC-2197: Bonobo Momma

- Title: Bonobo Momma
- Author (byline): Joyce Carol Oates
- Work: Sourland: Stories; Pgs 53-66
- Publisher: Ecco
- Publication date as stated: June 2011
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: DAUGHTER, ADELINA
- Teaser before the introduction: Yes
- Spoken words (computed): 1421
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joyce Carol Oates
Book: Sourland: Stories; Pgs 53-66
ISBN: 978-0061996535
Publisher: Ecco
Date (Month/Year): June 2011
```

### Introduction (context only: never use it for content warnings)

```text
Loneliness in its deepest form emerges not when we are alone, but when we stand beside someone we love and still feel invisible. When words are exchanged but understanding never arrives, when affection is offered yet never quite reaches us. This kind of loneliness is built on hope: the hope of being recognized, valued, and truly seen. But yearning for closeness does not guarantee connection, even if those you yearn for are your own parents. That is when you are left completely and profoundly alone.

Bonobo Momma by Joyce Carol Oates
```

### Performance text (classify this)

```text
DAUGHTER: That day, I met my “estranged” mother in the lobby of the Carlisle Hotel on Fifth Avenue, New York City. It was a few weeks following the last in a series of surgeries to correct a congenital malformation in my spine, and one of the first days when I could walk unassisted for any distance and didn’t tire too quickly. This would be the first time I’d seen my mother since Fall Fashion Week nearly two years ago. Since she’d divorced my father when I was eight years old my mother, whose professional name was Adelina, spent most of her time in Paris. At 30 she’d retired from modeling and was now a consultant -- a much more civilized and rewarding occupation than modeling, she said. For the world is “pitiless” to aging women, even former vogue models.

DAUGHTER: As soon as I entered the Carlisle Hotel lobby, I recognized Adelina waiting for me on a velvet settee. On the way to the hotel I’d become anxious that my beautiful mother might wince at the sight of me, as sometimes she’d done in the past, but she was smiling happily at me—joyously—her arms opened for an embrace. I felt a jolt of love for her like a kick in the belly that took my breath away and left me faint-headed. Is that my mother? My—mother? My father too was “famous” in a similar way—he was a painter/sculptor whose work sold in the “high six figures”— famous in contemporary Manhattan art circles but little-known elsewhere.

ADELINA: Darling! Look at you—such a tall girl—

DAUGHTER: When she leaned back to look at me her mouth worked as if she were trying not to cry. Adelina had not been able to visit me in the hospital at the time of my most recent operation though she’d sent cards and gifts to my room at the Hospital for Special Surgery overlooking the East River: flowers, candies, luxurious stuffed animals and books more appropriate for a younger girl.

ADELINA: Your back, darling -- you are all mended? Yet so thin. But you are very pretty. Or would be if – (inspects her daughter’s hair with her hands and is not impressed) A haircut, chérie. This very day! You’re hungry for lunch, I hope (she turns away) Come!

DAUGHTER: Even in my desperation I was wary, hesitant. With my S-shaped spine that had caused me to walk oddly, I had always been shy and uncertain. Other girls my age hoped to be perceived as beautiful -- I was grateful not to be stared at.

We were going to eat in the sumptuous hotel restaurant. Adelina had made a “special reservation.” As the maitre d’ was seating us, it appeared that something was amiss.

ADELINA: No. I don’t like this table.

DAUGHTER: In her throaty aggrieved voice Adelina was telling the maitre d’ that she’d made a reservation for a “quiet” table -- her daughter had had “major surgery” just recently. In a voice heavy with sarcasm . . .

ADELINA: We will go elsewhere, monsieur! Merci beaucoup!

DAUGHTER: In the park, Adelina lit a cigarette and exhaled bluish smoke in luxurious sighs as if only now could she breathe deeply. Her mood was incensed, invigorated. Snugly she linked her arm through mine. I was having trouble keeping pace with her but I managed not to wince in pain for I knew how it would annoy her.

ADELINA: Lift your chin, chérie. Ignore if they stare.

DAUGHTER: I was hoping that she wouldn’t confront anyone. There was a fiery sort of anger in my mother, that was fearful to me, yet fascinating.

Because of her enormously busy professional life that involved frequent travel to Europe, Adelina had relinquished custody of me to my father at the time of their divorce. It had been a “tortured” decision, she’d said. But “for the best, for all.” Now when she questioned me about school, I sensed that she wasn’t really listening. Several times she turned to glare at someone who’d passed us saying sharply . . .

ADELINA: Yes? Is there some problem? My daughter would appreciate not to be stared at. Merci!

DAUGHTER: Truly I did not know if people were watching us -- either my mother or me -- but it would not have surprised me. Adelina dressed like one who expects attention, yet seemed sincere in rebuffing it. As a child with a body that had been deformed until recently, I’d become accustomed to people glancing at me in pity, or children staring at me in curiosity, or revulsion; but now with my repaired spine that allowed me to walk more or less normally, I did not see that I merited much attention.

Inside the Boat House many diners were awaiting tables. We were jostled by strangers in a continuous stream into and out of the dining area.

My mother inquired about my surgery, and about the surgeon; she seemed genuinely interested in my physical therapy sessions and she explained why she hadn’t been able to fly to New York to visit me in the hospital, and hoped that I understood. (I did! Of course.)

ADELINA: My life is not so fixed. Not like your father!

DAUGHTER: My father loved me very much, he said. Still, I saw that he’d begun to lose interest in me once my corkscrew spine had been repaired, and I was released from the hospital: my medical condition had been a problem to be solved, like one of my father’s enormous canvases or sculptures, and once such a problem was solved, his imagination detached from it. I could understand this, of course. I understood that, apart from my physical ailments, I could not be a very interesting subject to any adult.

More than a half-hour had passed, and we were still waiting to be seated for lunch. Abruptly then my mother decided that we were leaving. She pulled me outside with her. Again she snugly linked her arm through mine.

ADELINA: (taking sudden notice) Your shoulder! Your left, you carry it lower than the other. You don’t want to appear hunchbacked. What was he? Quasimodo? A terrible thing for a girl. Here . . .

DAUGHTER: Adelina gripped my wrists and pulled them over my head, to stretch me. I was made to stand on my toes, like a ballerina.

ADELINA: I don’t like how people look at you. With pity, that is a kind of scorn. I hate that!

DAUGHTER: Her mouth was wide, fleshy. Her forehead was low. Her features seemed somehow in the wrong proportions and yet the effect of my mother was a singular kind of beauty, it was not possible to look away from her. My father once painted a series of portraits called Bonobo Momma. Enormous canvases with primitive figures of monkey-like humanoid females. It was possible to see my beautiful mother in these simian figures with their wide fleshy mouths, low brows, My father had paid homage to that, in my mother. Perhaps it was his loathing of her that had allowed him to see her clearly.

I was feeling light-headed. But when Adelina asked me if I was all right, quickly I told her I was fine.

ADELINA: Frankly, darling, you don’t look ‘fine.’ You look sick. Darling, if you could walk straighter. This shoulder . . . try! (shakes her head in disgust)

DAUGHTER: I was trying to explain. As in a dream in which the right words won’t come . . . Her ash-blond hair stirred in the wind, stiffly. At the base of her throat was a delicate hollow I had not seen before. The bizarre thought came to me, I could insert my fingers into this hollow. I could push down, using all of my weight. My mother’s brittle skeleton would shatter.

ADELINA: You shouldn’t have come out today, darling. If you’re not really mended.

DAUGHTER: Briskly Adelina was signaling for another taxi. Her manner was urgent, dramatic. A taxi braked to a stop. Adelina opened the rear door, pushed me inside, leaned into the window to instruct the driver

ADELINA: Please take my daughter home. She’ll tell you the address. She’s just 13, she has had major surgery and needs to get home, right away. Make sure she gets to the actual door, will you? You can wait in the street and watch her. (stooping to kiss her daughter’s cheek) Darling, goodbye! Take a nap when you get home. You look ghastly. I’ll call you. I’m here until Thursday. Au-voir!

DAUGHTER: The taxi sprang forward. On the curb my mother stood blowing kisses after us. In the rear view mirror the driver’s narrowed eyes shifted to my face. Now I was alone. I wiped at my eyes. Through the smudged window beside me flowed a stream of strangers on the sidewalk -- all that I knew in my life that would be permanent, and my own.
```

---

## IC-2198: Brimstone and Marmalade

- Title: Brimstone and Marmalade
- Author (byline): Aaron Corwin
- Work: Not specified
- Publisher: Rector Magazine
- Publication date as stated: Oct 30, 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MOTHER, MATHILDE, FATHER, PRINCIPAL, NANA, SHOP KEEPER, IX’THOR, BECKY, ROBBY
- Teaser before the introduction: Yes
- Spoken words (computed): 1028
- Already set (do not supply): none

### Source block (context only)

```text
Author: Aaron Corwin
On-line Transcript at: https://reactormag.com/brimstone-
and-marmalade-aaron-corwin/
Publisher: Rector Magazine
Date (Month/Year): Oct 30, 2013
```

### Introduction (context only: never use it for content warnings)

```text
When I was little, I desperately wanted a pot-belly pig – But my parents in all of their wisdom gifted me with BURBLES – the goldfish. BURBLES didn’t last very long, and I remember hosting my own little funeral service as we flushed him to his watery resting place.

BURBLES was followed by a succession of other small creatures – 4 more fish, a hamster, and a bunny. At least I wasn’t condemned to own a pet rock!

In this fantasy selection, Mathilde doesn’t get the pony she wants; but a miniature demon named Ix’Thor. Take that, BURBLES.

Brimstone and Marmalade by Aaron Corwin
```

### Performance text (classify this)

```text
NOTE: The humor from this selection comes from the characterization and voice qualities of the characters. Go big and have fun!

NARRATOR: Mathilde didn’t want a demon. She wanted a pony.

MOTHER: Ponies are expensive. How about a nice little demon instead?

MATHILDE: (stamping her foot) I don’t want a demon! Demons are ugly and creepy and they smell bad!

FATHER: We’ll see.

MATHILDE: (to audience) When a grown-up said “we’ll see,” it really meant “never.” Peter Voorhees brought his demon to school. It was scaly and slobbery, not sleek and pretty like a pony. How could anyone think that a demon was better?

NARRATOR: The day before Mathilde’s birthday in September . . .

PRINCIPAL: Mathilde, your parents called. Your grandmother is picking you up.

MATHILDE: Nana’s here for my birthday? Nana always brought presents. (to Nana) Nana!

NANA: Look at you! My little Matty-Patty’s all grown up!

MATHILDE: (giggling) Where are we going?

NANA: You didn’t think I’d come all this way and not bring you a present, did you? The sort of present you’d better pick out for yourself!

NARRATOR: Mathilde could scarcely believe it. After all this waiting, she was finally going to get a pony of her very own. But when the car stopped, it was in front of a store covered in steel plates and the air smelled just a little bit like rotten eggs. It was very dark inside.

MATHILDE: This isn’t a pony store! This is a demon store! I don’t want a demon! I want a pony!

NANA: When I was a girl, we had a Belgian Muncher on the farm. Smart as a whip if you train ‘em right. You know the best thing about demons? They’re great for convincing parents that little girls are responsible enough to take care of a pony. If you prove you can take care of a demon. . . then we can see about that pony. (Nana and Mathilde enter the store)

SHOP KEEPER: Well, hello there! Are you here for a new demon?

NANA: Yes. It’s her birthday.

SHOP KEEPER: (to Mathilde) I see! What sort of demon were you looking for?

MATHILDE: The kind with the pretty eyes and the long, shiny mane!

NANA: (sighing heavily) That’s a pony, dear.

MATHILDE: Well, that’s what I want!

SHOP KEEPER: Oh, I think I have just the one for you. (he pulls out a small glass cage)

NARRATOR: The demon inside didn’t have a long, shiny mane. It didn’t have any hair at all, just a tiny, black hooded robe. Its eyes were two red stars that twinkled in the darkness of its hood like Christmas lights.

SHOP KEEPER: He’s a Miniature Dark Lord.

NANA: (shaking her head) A Dark Lord? I thought they had great big horns!

SHOP KEEPER: Normally. But this poor little guy was born without any. All the other Dark Lords rejected him.

MATHILDE: (feeling a connection with rejection) What’s your name?

IX’THOR: (raising his arms over his head) I AM IX’THOR, MASTER OF THE VENOMOUS PITS OF KARTHOOM! BOW BEFORE YOUR MASTER!

SHOP KEEPER: How about that! He told you his name first thing. He must really like you.

MATHILDE: (pouting) Well, I don’t like him . . . (IX’THOR is deflated, lowers his arms and hangs his head) But I guess he’ll do.

NARRATOR: Mathilde had a hard time sleeping that night. Her thoughts kept drifting toward the pony she would have someday. How long would she have to take care of a stupid demon, anyway?

MATHILDE: (sleeping . . . she snores lightly)

IX’THOR: (pokes MATHILDE on the chin, she swats him away, but he continues to poke)

MATHILDE: (awakens with a start)

IX’THOR: KNEEL BEFOR YOUR MASTER, MORTAL!

MATHILDE: Aaaaaah! Mom! (IX’THOR squeals and quickly hides)

MOTHER: How did he get out of his cage? (looks around the room for the demon)

MATHILDE: (also looking, she sees a dark shape dart under her bed and grabs a flashlight) He’s right here!

(she reaches under the bed and grabs his little body) I’ve got him!

IX’THOR: (slashing has her hand with his claws)

MATHILDE: EEEEEEE! (abruptly drops him, crying) I hate demons! I want a pony!

MOTHER: Oh, sweetie. It’s just a tiny little cut. He was just scared, that’s all. You have to be careful with animals. When they’re scared they lash out. They don’t know any better.

MATHILDE: (belligerently) I don’t want him in my room!

NANA: (clearly disappointed) I’m sorry. I’ll take him back to the store tomorrow.

MATHILDE: (she remembers her pony and backpedals) Wait! I didn’t mean it. He can stay.

MOTHER: This is your last chance. If you say you don’t want him one more time, we’ll give him to someone who does. *****

NARRATOR: [The next day – Mathilde’s Birthday]

MATHILDE: (excited) There was cake! Chocolate with white frosting and candy sprinkles. And presents! A camera and a unicycle and (sadly) eleven different kinds of TOY ponies. (to the kids at the party) I did get another present . . . You want to see him? (she leads them to her bedroom) You have to turn the lights down. (as she dims the lights) He doesn’t like light.

BECKY: It’s not a snake is it?

MATHILDE: Shhh! It’s not a snake. (She lifts the cover from the cage)

IX’THOR: WELCOME TO MY DOMAIN. FOOLS! DID YOU THINK YOU COULD DEFEAT ME?

ROBBY: Wow! That’s cool!

MATHILDE: (with a real smile of pride) He’s a Dark Lord.

ROBBY: Does he do any tricks?

IX’THOR: BOW BEFORE ME!

MATHILDE: You shouldn’t actually bow. That just encourages him.

BECKY: It’s just a demon. What good is a demon who doesn’t even do anything? I bet he bites.

IX’THOR: FOOLISH MORTALS. NOW BEHOLD MY TRUE POWER! (he waves his arms and emits a bust of fire from his hands)

ROBBY: WOW! You said he didn’t do any tricks!

IX’THOR: GIVE ME YOUR SOUL AND I WILL GRANT YOU LIMITLESS POWER.

MATHILDE: Mom says I can’t have limitless power until I’m older. But you can have a grub soul.

NARRATOR: [Mathilde takes out] a small, softly glowing ball, about the size of a pea from the big plastic bag Nana had bought. The bag said things like “Nutritionally Balanced” and “Now with extra innocence for a health glow!”

IX’THOR: EXCELLENT (racing to the side of the cage, he stands with his arms outstretched) IX’THOR ACCEPTS YOUR SACRIFICE. (he devours the pellet) NUM NUM NUM!

*****

NARRATOR: [Soon it was Halloween] A witch came to the house with a black pointy had, a broomstick, green skin and a big, warty nose.

MATHILDE: Nana!

NANA: (in a big witchy voice) Happy Halloween! Eee-hee-he-hee! How’s my little angel?

MATHILDE: I’m not an angel (raises the hood to her robe and speaks in an Ix’Thor voice) I’m a Dark Lord. Bow before me, mortals!

NANA: (feigning fright) Oh, my! I think I felt the earth tremble for a moment.

MATHILDE: (mimicking IX’THOR) Excellent. It is just as I have foretold. (She picks up a traveling crystal ball and holds it up) Ix’thor’s coming with us! He says fear keeps the peasants in line.

NANA: Mathilde . . . you know not everything Ixthor says is a good idea, right?

MATHILDE: (rolling her eyes) Well, duh!

IX’THOR: MWA HA HA! NOTHING CAN STOP US NOW!

MATHILDE: (mimicking IX’THOR) I’ll take my revenge when I rule the world. Mwa ha ha.

(Mathilde starts to walk toward the street, trips and falls forward. The crystal ball holding Ix’Thor launches from her hand and tumbles through the air into the street – there is the sound of squealing brakes and then shattering glass)

MATHILDE: No! (she races to Ix’thor) Ix’thor! Please!

IX’THOR: THIS . . . CANNOT . . . BE. I AM IN . . . VINCIBLE . . . ***** At the demon store *****

NARRATOR: [The family rushes Ix’thor to the demon store, hoping the shop owner can save him]

FATHER: Demons are pretty strong, right? Almost impossible to kill?

SHOP KEEPER: Dark Lords are weaker in direct sunlight. Much weaker. I did all I could.

MATHILDE: (crying)

MOTHER: Oh, sweetie. It wasn’t your fault. There was nothing anyone could have done. (more sobbing from Mathilde) Father and I were talking to Nana. If you still want one . .

MATHILDE: (defiantly) I don’t want a pony! I want Ix’thor. But I can’t have him back, can I?

MOTHER: No, I’m sorry.

MATHILDE: Then . . . can I get a pony with glowing red eyes and crush the skulls of my enemies beneath his flaming hooves?

MOTHER: (laughing) One with glowing eyes!

MATHILDE: (in her best Ix’thor voice) Excellent! It is just as I have foretold . . .
```

---

## IC-2199: Bring-Your-Machete-To- Work Day

- Title: Bring-Your-Machete-To- Work Day
- Author (byline): Sloane Crosley
- Work: I Was Told There’d be Cake
- Publisher: Penguin
- Publication date as stated: 2008
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1349
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sloane Crosley
Book: I Was Told There’d be Cake
ISBN: 978-1101147474
Publisher: Penguin
Date (Month/Year): 2008
```

### Introduction (context only: never use it for content warnings)

```text
If you went to an American public school during the late 1980s or most of the 1990s, and your classroom was fortunate enough to have a monolithic, clicking heap of machinery called an Apple II, you probably remember a game called The Oregon Trail. Usually on Friday afternoons, when our teacher was at her wit’s end from 4 full days with pre-teens, we were allowed to “play” this educational game. And I have to admit . . . in the eyes of visitors, I was fully engaged in a quality learning experience with strong digital content--a happy, motivated learner. WRONG! As much fun as it was, the dozens of hours I spent in class playing The Oregon Trail really only taught me 3 things: I could single-handedly cause the extinction of the buffalo, what diseases people got in the 19th century, and how to write tombstone epitaphs for the dead. All good things to know, but not extremely practical items to put on a resume! PS: I also know how to drown my family in a river and how to die of starvation . . . somewhere in the Midwest . . . .

Bring-Your-Machete-To-Word Day by Sloane Crosley
```

### Performance text (classify this)

```text
In 1990, after our Apple IIE quit, our family purchased a Macintosh Classic. This was a good thing because the IIE was a constant source of confusion for me. For one thing, it took large flexible disks that were not even, despite all tactile evidence to the contrary, marketed as “floppy disks.” The more current model – disks half their size and so hard you could eat off them – held the public title of “floppy.” (Also neither of these options were, in fact, disc-shaped) For another, the monitor would freeze or blink incessantly without telling you what was wrong, like a pet or a baby. I tried to fix it myself once and the Brightness knob shot out and hit me in the eye. As if these crimes weren’t enough to make us love the Macintosh Classic by comparison, our new computer came with three free games. One of them was Oregon Trail. I have no idea what the other two were.

A game of moderately tough choices and rawhide, Oregon Trail wound its way through the late 1980s in a very un-‘80s-like fashion: subtly. Unlike BurgerTime or Tetris, high-speed programs structured around multiple levels, Oregon Trail slowly moved toward a singular goal. Apparently many children learned how to play it at school, which strikes me as just plain illegal.

For me, Oregon Trail was a private affair – something I engaged in after dinner when I was supposed to be doing homework. At the time I was going through a somewhat awkward phase, both the “somewhat” and the “awkward” being total understatements. I had a chin that jut out when I smiled, as if it were trying to escape from my face. And who could blame it? My eyes were too big for my head, my hair too big for my whole body, and my whole body too flat to be noticed by anyone but me. Sadly, as it is for many of us, my awkward phase found me years before I qualified for a driver’s license or even the alarm code to the house. Homebound and date-free, I enjoyed an early teenagehood of drawing in journals, chatting with inanimate animals, prank-calling boys and playing Oregon Trail. Oregon Trail, which provided me with the illusion I was actually going somewhere. Once the game began, I became completely enthralled, pausing only to listen for the pattern of stair squeaks that would indicate a parent was descending.

Oregon Trail was built on a completely unmodern premise. This also distinguished it from its contemporaries – there were no robots, no time machines, no spacemen possible in a world where people ate unrefrigerated animal guts and washed their socks in a bucket. Originally designed by a couple of college students to teach kids about the odors and tribulations of pioneer life, the game starts in nineteenth-century Independence, Missouri, and heads toward the west coast. The screen itself – displaying a khaki stretch of land and a mountain range in the distance – never alters. IT moves from left to right as your tiny wagon heads west, but there are no pop-ups requiring you to select a weapon, no shifts in perspective, no interiors. IT’s like watching some brilliant independent film where there are no cuts and no scene changes, only a wagon and a little thing called destiny. It’s also like watching a lost ant crawl across the kitchen counter.

Though you never see their faces, you can choose your persona – a banker from Boston (likely a metaphor for Reagan), a farmer from Illinois (likely a metaphor for Carter), or a carpenter from Ohio (Jesus?). Each character comes complete with a skill set and a gun (just the one rifle – this was pre-Uzi). For a future vegetarian, I sure shot a lot of venison.

Unlike other games of the day, which had me leaping through traffic, or called me “gumshoe,” Oregon Trail left lots of room for creativity. It seemed ripe for the misuse. Like a precursor to the Sims, you were allowed to name you wagoneers and manipulate their destinies. It didn’t take me long to employ my powers for evil. I would load up the wagon with people I loathed, like my math teachers. Then I would intentionally lose the game, starving her or fording a river with her when I knew she was weak. The program would attempt an intervention, informing me that I had enough buffalo carcass for one day. One more lifeless caribou would make the wagon too heavy, endangering the lives of those inside. Really now? Then how about three more? How about four? Nothing could stop this huntress of the diminutive plains. It was time to level the playing gield between me and the woman who called my differential equations “nonsensical” in front of fifteen other teenagers. Eventually a message would pop up in the middle of the screen, framed in a neat box: MRS. ROSS HAD DIED OF DYSENTERY. This filled me with glee.

I actually began playing the game in 1990, but it still reminds me of the 1980s. For the sake of this Oregon Trail’s influence, you have to ignore the date discrepancy. There’s always a bit of cultural bleed between decades, and the segue from the ‘80s to the ‘90s is infamously fluid. Especially if you were still a child in the early ‘90s and the formative pop cultural markers of your life were four or five years down the road. It’s the same reason Sunday morning movies can seem unquestionably from the ‘80s, but upon closer examination with a digital remote, were made in, like 1992. Thin of slouch socks, of Roxette, of Jennifer Connelly and Elizabeth Shue with full faces. You’re thinking of the ‘90s. Much like the Macintosh Classic itself, the ‘90s took a while to power up. I find that anything culturally significant that happened before ’93 I associate with the decade before it. In fact, Oregon Trail is one of a handful of signposts that middle school existed at all.

Which brings us to now. Here in the new millennium, there are five versions of the game available, including an Amazon Trail and Africa Trail, but none has provided as much milk to the pop culture teat as the original. Now the wagoneers have realistic movements and facial features. Their adventures have become complicate. But at what cost? Would I be able to go on unceremonious killing sprees now as I did then? Perhaps now you can click a button and see the inside of the wagon, pioneer children napping through a shaky afternoon, dreaming under the dangling hides of eight rabbits and a moose. I know I will continue to wonder. I am too fond of my memories of Oregon Trail and not in the market to have them replaced. Also, I no longer own a machine that plays video games so my curiosity cannot be satisfied without a significant financial commitment.

Apparently the game has changed for the better.

It wasn’t long before Oregon Trail was criticized for its complete lack of Native Americans, African Americans, or three-dimensional Americans of any kind. The hunting came under a certain degree of scrutiny as well because apparently guns connote “violence.” Then there was the game’s blatant favoring of rich white males. The banker is by far the best choice for your pixelated proxy. He’s in good health and comes with spare funds, which can be used to buy food in times of famine or the munchies.

Despite this orgy of damning evidence, I still think of Oregon Trails as a great leveler. IF, for example, you were a twelve-year-old girl from Westchester with frizzy hair, a bit plate, and no control over your own life, suddenly you could drown whomever you pleased. Say you have shot four bison, eleven rabbits, and Bambi’s mom. Say your wagon weighs 9,783 pounds and this arduous journey had been most arduous. The banker’s sick. The carpenter’s sick. The butcher, the baker, the algebra-maker. Your fellow pioneers are hanging on by a spool of lax. Your whole life is in flux and all you have is this moment. Are you sure you want to forge the river? Yes. Yes, you are!
```

---

## IC-2200: Burned Alive

- Title: Burned Alive
- Author (byline): Souad
- Work: Not specified
- Publisher: Bantam Books
- Publication date as stated: Aug 2005
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2442
- Already set (do not supply): none

### Source block (context only)

```text
Author: Souad
ISBN: 978-0553816303
Publisher: Bantam Books
Date (Month/Year): Aug 2005
```

### Introduction (context only: never use it for content warnings)

```text
Honor killings. Almost always, the victim is a woman; the killer a male family member. The woman’s offense is invariably refusing to bend to the will of her family. She is a sister who falls in love with a man not of her family’s choosing, She is a daughter who refuses to agree to an arranged marriage, sometimes to a man old enough to be her father. She is a wife who can no longer stay in an abusive marriage and divorces her husband.

According to the Washington Post, it remains a common practice in Pakistan today, with an estimated 1,000 Pakistani women murdered every year. There are few survivors; Souad was one of the “lucky” ones. This is her story. Burned Alive by Souad.
```

### Performance text (classify this)

```text
(Pg 1) I am a girl. A girl must walk fast, head down, as if counting the number of steps she’s taking. She may never stray from her path or look up, for if a man were to catch her eye, the whole village would label her a charmuta. A girl must be married before she can raise her eyes and look straight ahead, or go into a shop, or pluck her eyebrows and wear jewelry. My mother was married at fourteen. If a girl is still unmarried by that age, the village begins to make fun of her.

(Pg 2-3) It is a curse in my village to be born a girl. I have no memory of having played games or having fun as a child. The only freedom a girl can dream about is marriage, leaving your father’s house for your husband’s and not coming back. I dream about it. Ever since I heard that a man spoke to my father about me, I have been consumed by impatience and curiosity. I know [Faiez] lives three or four steps from us. He must have a good job in the city because he never dresses like a laborer. He always wears a suit, carries a briefcase, and has a car. I imagine I am married to him and he’ll come back from work at sunset and I will remove his shoes, and on my knees I will wash his feet as my mother does for my father. I will be a woman who has a husband!

(Pg 5) As I have mentioned, where I come from, being born a girl was a curse. (Pg 20) In my village, if the men had to choose between a girl and a cow, they would choose the cow. My father repeated endlessly how we girls were not good for anything. A cow gives milk and produces calves. What do you do with milk and calves? You sell them and bring the money homme, which means a cow does something for the family. But a girl? What does the family get from her? Nothing.

(Pg 52) Rights do not exist [for women] There are customs. This is the way it is and that is all. If your father points to a corner of the room and tells you to stay in that corner the rest of your life, you won’t move from there until you die. If your father places an olive in a plate and tells you that today that’s all you’ll have to eat, you eat only that olive.

(Pg 48-49) Being married was the most I could hope for in terms of freedom. But even married, a woman risked her life at the least lapse in her conduct. I remember a woman who had four children. One day I heard my mother say that the village was telling stories about her. People thought she was involved with the owner of the store because she went there frequently to buy bread, vegetables and fruit. One day my mother said that her brothers had gone into her house and cut off her head. They left the body on the ground and walked around the village with her head. She also said that when her husband returned from his job he was happy to learn that his wife was dead since she’d been suspected of something with the store owner. This woman had been punished for her violation of the rules, this was normal. I didn’t realize that simple gossip based on the neighbors’ assumptions, or lies even, could turn any woman into a charmuta and lead to her death, for the sake of the honor of the others. IT is what is called a crime of honor, Jamirat el Sharaf, and for the men of my region it is not considered a crime.

(Pg 72-74) Faiez lives in the house opposite ours, on the other side of the road. [He] works in the city [and] is all elegance. The first time I saw him I was lucky. He came out in a suit, with beautiful black-and-tan laced shoes, carrying a briefcase, very black hair, very tanned complexion, a proud bearing. My heart beat loudly in my chest and my legs trembled. And I said to myself: I want this man for my husband. I love him. I want him, I want him . . .

But what to do? How could I plead with him to go and beg my father to conclude the marriage? How could I even speak to him first? A girl does not speak first to a man. She is not even supposed to look directly at him. He is inaccessible. Even if this man wants to marry me, it’s not for him to decide it. It’s my father, always him, and he would kill me if he knew I lingered for a second on the road to draw Faiez’s attention. I decided to do everything I could to meet him in secret and speak to him, at the risk of being beaten or stoned to death. I didn’t want to lose all hope of going away with a man, of getting free of my father’s brutality.

(Pg 76-77) The next morning, I pretend to be chasing a goat in order to pass in front of [Faiez’] house. He smiles at me – I know he’s watching me go off toward the fields with the animals. I can’t go any farther in taking the initiative. Now it’s for him to decide how he will arrange to speak to me in secret. He knows where I go and when . . . the next day Faiez appears in front of me. He has followed me discreetly and says hello to me. I am ashamed and I look down at my feet, I twist the fabric of my dress and pull on the buttons of my jacket. I don’t know what to say.

“Would you like us to get married together? . . . You’re afraid?”

“Yes, I’m afraid. My father is mean. It’s dangerous for you, too. My father could beat both of us.”

(Pg 78-83) I have never been so happy. To be with him, so close, even for a few minutes. For the first time in my life I am someone because I myself decided to do what I want. I am alive. I’m not obeying my father or anyone else. On the contrary, I’m disobeying. My first real meeting with Faiez, in the field of green wheat, give me an idea of who I am. A woman who is determined to become his wife at any price.

“Do you want me to speak to your father about the marriage?” Faiez comes closer to me, very close. I close my eyes, I’m a little afraid. I feel his hand behind my neck and he kissed me on the mouth. “See you tomorrow. Wait for me, but not on the road, it’s too dangerous. Hide here, in the ditch. I’ll meet you after work.”

And the next day, as I watch him approach my hiding place, my heart is trembling. No one in the house suspects my secret meeting. [But] I’m afraid Faiez wants more than a kiss, and at the same time I want it without really knowing what is waiting for me. I’m afraid that if he goes too far and I push him away, he’ll get angry. I also have confidence in him because he knows very well I can’ let myself be touched before marriage. He knows that I’m not a charmuta. And he has promised me marriage. But I’m afraid all the same, all alone in this field. Hidden in the tall grass.

We sit on the ground. He tries to place his hand on my thigh. I don’t let him do it. He gets annoyed. His expression is mean as he looks at me. “Why don’t you want to? Come on!” I’m so afraid he’ll go away, that he’ll look for somebody else. He is my only hope. So I let him do what he wants. He pushes me into the grass. He knows very well what he’s doing. He says nothing, either before or after. He doesn’t ask me why I’m crying, and I don’t even know why I have so many tears. I didn’t want to. I know nothing about love between a man and a woman, no one has taught me anything about it. I don’t dare look at him, I’m ashamed. I didn’t want to make love with him hidden in a ditch, I wanted what all the girls of my village want. To be married, to have a beautiful dress and go to be in his house. He took advantage of my fear, he knew I would give in to keep him. I begged him not to drop me, to arrange the marriage quickly. A girl who is no longer a virgin, this is too serious, it’s all over for her.

“Now go back, change your clothes, and act like nothing happened. Especially don’t cry in the house.”

(Pg 85-87) One morning in the stable I suddenly feel very strange. The odor of the manure makes me dizzy. And later as I prepare the meal, the mutton makes me feel ill. I’m nervous, I want to go to sleep or cry for no reason. Every time Faiez comes out of his house he looks somewhere else, makes no sign to me. It’s been a long time, too long, and I don’t know when I last had my period, or when it should arrive. If I’m pregnant my father is going to smother me in the sheepskin blanket. So I hide, I pretend to be fine, but it becomes more and more difficult. Summer begins. This lie can’t go on for long. I am pregnant and it’s been a month since the last time I saw Faiez. (Pg 88-89) I believed him, I wanted so much to believe him. [But] I was so afraid that I picked up a big stone and struck my stomach with it hoping to make myself bleed and put things right. (PG 93) I have lost hope. It’s over. He’s dropped me. He took advantage of me, it was a fine time for him. Not for me. I’ll never see him again. [and] I can’t ask anyone for help.

(Pg 100-102) The weeks pass. No one questions me, no one wants to know who did this to me, how and why. Even if I accuse Faiez, my father won’t go looking for him to make him marry me. It’s my fault, not his. A man who has taken a girl’s virginity is not guilt, she was willing. And even worse she’s the one who asked for it, who provoked the man because she is a whore without honor. I have no defense. My naivete, my love for him, his promise of marriage, nothing of all that counts for anything. In our culture, a man who has self-respect doesn’t marry the girl he has deflowered. Did he love Me? No. And if I committed a fault, it was believing that I would hold on to him by doing what he wanted.

One evening - a family meeting. I listen behind the wall, terrified. My mother speaks to Hussein, my older sister’s husband: “We can’t ask our son, he won’t be able to do it, he’s too young.”

“I can take care of her. Don’t worry about it. I’ll find a way. You’ll go out. Leave the house, you can’t be there. When you come back, it will be done.”

I hear my sister crying, saying she doesn’t want to hear this and that she wants to go home. I had heard my death sentence with my own ears. Are they really going to do it? Is it just to frighten me? And if they do it, when will it be? How? By cutting off my head? Maybe they’re going to let me have this child and then kill me after. Will they keep the child if it’s a boy?

The next day, I act as though I’ve heard nothing. My mother says to me: “It’s time for you to do the washing, your father and I are going to the city.” I know what is going to happen. They are leaving the house just as they’d told Hussein.

I first go for water from the well at the back of the garden. I arrange the wood for the fire and sit down on a stone while I wait for the water to heat. (PG 105 – 107) Suddenly I hear the door clang. He’s there, my brother-in-law Hussein. “Hi! How goes it? I’m going to take care of you.” That smile – I wasn’t expecting that. “You’ve got a big belly, huh? “ He didn’t say anything more. I kept my head down in shame, a little relieved that he didn’t ask me other questions.

I suddenly felt a cold liquid running over my head and instantly I was on fire. I start to run in the garden, barefoot. I slap my hair, I scream. I feel my dress billow out behind me. . Was my dress on fire too? I know I’m running and I’m on fire and I’m screaming. I must have climbed onto the garden wall to end up in the street. There were women, it seems to me two of them, and they beat on me, I suppose with their scarves. They dragged me to the village fountain and the water hit me suddenly and I screamed in fear. I hear the voices of women wailing over me “The poor thing . . . the poor thing . . “ I’m going to die. That’s good. Maybe I’m already dead. It’s over, finally.

TRANSITION But Souad didn’t die . . . with 3rd degree burns destroying her face and covering most of her body, she survived. And with the help of SURGIR, a Swiss foundation dedicated to working with women who are subjected to criminal traditions, she escaped with her unborn child to tell her story. 30 years after her attempted murder, she explains . . .

(Pg 197) I have met girls who have come from afar, as I did years ago. They are in hiding. A young girl who has no legs: She was attacked by two neighbor men who tied her up and put her in the path of a train. Another whose father and brother tried to murder by stabbing her and throwing her into a garbage bin. Still another whose mother and two brothers threw her out a window. She is paralyzed . . . [But] I have never met any burned women like myself; they haven’t survived. And still I hide, I cannot say my real name, show my face. I can only speak out, it is the only weapon I have.
```
