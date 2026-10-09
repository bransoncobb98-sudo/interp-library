# Classification request: batch 44 of 53 (40 records, IC-2121 to IC-2160)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-044-reply.json`.

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

## IC-2121: Shoot Me First

- Title: Shoot Me First
- Author (byline): Carol A. Taber
- Work: Not specified
- Publisher: The Family Security Foundation, Inc.
- Publication date as stated: Oct 6, 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 795
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carol A. Taber
ISBN: N/A
Publisher: The Family Security Foundation, Inc.
Date (Month/Year): Oct 6, 2006
NOTE: The original copy of this article was published
only on on-line at The Family Security Foundations
website.
http://www.familysecuritymatters.org/publications/detail/shoot-me-
first
Be sure to check with your local/state requirements for
publication and category requirements before performing.
Each state has their own requirements for any given
category.
Because this article was never presented in a verbal
format, some states may not allow it to be presented as a
DECLAMATION, but may require that it be presented in
the PROSE category.
```

### Introduction (context only: never use it for content warnings)

```text
On October 2, 2006 Charles Carl Roberts entered Georgetown School, a one-room Amish school house in Lancaster County, Pennsylvania and began addressing the pupils, showing them an automatic handgun. In the classroom were 15 male pupils, 10-12 female pupils, one teacher and a number of assistants - older children and adults. He told the boys to leave, along with a pregnant woman and three others with infants. The gunman made the girls line up in front of the blackboard, where he tied their feet using wire or plastic cuffs. He then barricaded the doors with large pieces of wood he had brought with him. The next minutes must have been horrific for the girls as each awaited what was clearly to be their execution day. In the midst of the terror, however came quite voices . . . Shoot Me First by Carol A. Taber.
```

### Performance text (classify this)

```text
We know there is great courage and honor among our military, but many Americans doubt that such splendid traits are in sight anymore among average American citizens. There has been such a rampaging coarsening of American culture and society - delivered to us through a constant stream of lowest-common-denominator, omnipresent media - that one wonders how we can further degrade ourselves from Janet Jackson’s “costume malfunction”, staged for every American kid to witness in the crassly and grossly over-commercialized Super Bowl.

But there are still laudable and honorable traits living in these United States, and great depth of character. I know because I saw them, and read about them, over these past few days.

Even in the face of such evil fury as we witnessed in Amish country, there was dignity, valor and calm, facing death. In 13-year-old Marian Fisher, the oldest of the five Amish girls who were slaughtered in their simple, one room schoolhouse, West Nickel Mines, we know this. Marian stepped forward and said to her murderer, "Shoot me first". Marian’s younger sister, Barbie, then asked Charles Carl Roberts IV to shoot her second. Barbie, among the ten girls who were shot, survived, while Marian did not.

This is the sort of thing for whom our country normally awards such honors as the Congressional Medal of Honor for valor under the frenzy of battle. This is why so many of the Honors are awarded posthumously. Were these gestures any different?

There is still respect in this country, seen in the throngs of people who removed their hats and stood in silence as the funeral processions passed by. Not a word was spoken while the black carriages passed with the solemn mourners inside. This plain black procession of nineteenth-century horse-drawn carriages with simple folk inside was nothing short of a majestic sight for our wearied eyes, already wearied of the hi tech, edgy gloss of our very young twenty-first century.

There is still dignity and kindness among us, evident in the no-fly zones established overhead the funerals, cordoned off to allow the Amish to grieve in private, without the world gawking at their misfortune. To my knowledge, no out-of-control yahoos violated that zone as would be expected under almost any other sort of similar condition.

There were magnanimous and gallant offers made, too, that saved further agony for the Pennsylvania Amish. Mike Gallagher turned over his entire radio show to the immensely strange people from the ultra left wing group who picket funerals (I choose not to identify their group and give them the coverage they crave). He allowed this so that they wouldn’t be heard and seen by the worldwide media in their picketing of the funerals of those angelic little kids, executed gangland style. This group had planned to proclaim that the girls deserved their unspeakably cruel deaths.

There was compassion, seen in the silent candlelight vigils held for the families of those defenseless girls slain by a madman. No riots, no speeches, no t-shirt selling, no proselytizing…just sorrow and sympathy bearing witness to a deep and abiding tragedy in a farm community of innocents.

There was forgiveness, witnessed in the two families – those of the murderer and those of the murdered – recognizing each other’s terrific loss. The Amish folk have invited the murderer’s family to their homes so that they can share their grief together. In fact, many of the Amish have offered forgiveness for the shooter whom some would more easily call the Devil himself. I admit I do.

And so I sit back and contemplate what I have seen. There are many times when I grieve for the loss of the America I knew when I was young. I do not see that wonderful place in our current culture, only among some families who steadfastly adhere to the principles upon which they were raised. But these valiant families exist in a maelstrom of political correctness gone wild, amidst high school graduates who can’t read, among sheer vulgarity blasted into our living rooms daily, and within a depraved sense of what is right and what is wrong that matches nothing we have known before. With this backdrop, it is tough to imagine America’s future resembling anything of what it was meant to be at its founding. With such polar opposite thinking in our country, it remains to be seen which vision will prevail.

In the meantime, there are those of us who can take comfort in the sights and sounds of the Amish country, and in particular, in their response to the evil that went to school that day. This is a spot in our country where valor, dignity, manners, compassion and courage know no bounds, and we are reminded of life as it once was…and let’s hope might still be.
```

---

## IC-2122: Three Sideways Stories from Wayside School

- Title: Three Sideways Stories from Wayside School
- Author (byline): Louis Sachar – adapted by
- Work: Not specified
- Publisher: Harper Trophy
- Publication date as stated: June 1998
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MRS. JEWLS, JOE, NARRATOR, CALVIN, BEBE, LOUIS
- Teaser before the introduction: Yes
- Spoken words (computed): 1514
- Already set (do not supply): none

### Source block (context only)

```text
Author: Louis Sachar – adapted by Aaron Shepard
ISBN: 978-0380731480
Publisher: Harper Trophy
Date (Month/Year): June 1998
```

### Introduction (context only: never use it for content warnings)

```text
This is the story of three of the children in Mrs. Jewls’s class, on the thirtieth story of Wayside School. But before I get to them, there is something you ought to know. Wayside School was accidentally built sideways. It was supposed to be only one story high, with thirty classrooms all in a row. Instead, it is thirty stories high, with one classroom on each story. The builder said he was very sorry.

Three Sideways Stories from Wayside School by Louis Sachar – adapted by Aaron Shepard
```

### Performance text (classify this)

```text
Aaron Shepard

One day, Mrs. Jewls kept Joe in from recess.

MRS. JEWLS: Joe, you are going to have to learn to count.

JOE: But, Mrs. Jewls, I already know how to count. Let me go to recess!

MRS. JEWLS: First count to ten.

JOE: Six, eight, twelve, one, five, two, seven, eleven, three, ten.

MRS. JEWLS: No, Joe, that is wrong.

JOE: No, it isn’t! I counted till I got to ten!

MRS. JEWLS: But you were wrong. I’ll prove it to you.

NARRATOR: She put down five pencils.

MRS. JEWLS: How many pencils do we have here, Joe?

JOE: Four, six, one, nine, five. There are five pencils, Mrs. Jewls.

MRS. JEWLS: That’s wrong.

JOE: How many pencils are there?

MRS. JEWLS: Five.

JOE: That’s what I said! May I go to recess now?

MRS. JEWLS: No. You got the right answer, but you counted the wrong way. You were just lucky. She set down eight potatoes.

MRS. JEWLS: How many potatoes, Joe?

JOE: Seven, five, three, one, two, four, six, eight. There are eight potatoes, Mrs. Jewls.

MRS. JEWLS: No, there are eight.

JOE: But that’s what I said! May I go to recess now?

MRS. JEWLS: No! You got the right answer, but you counted the wrong way again. She put down three books.

MRS. JEWLS: Count the books, Joe.

JOE: A thousand, a million, three. Three, Mrs. Jewls.

MRS. JEWLS: (bewildered) Correct.

JOE: May I go to recess now?

MRS. JEWLS: No.

JOE: May I have a potato?

MRS. JEWLS: No! Listen to me. One, two, three, four, five, six, seven, eight, nine, ten. Now you say it.

JOE: One, two, three, four, five, six, seven, eight, nine, ten.

MRS. JEWLS: Very good! She put down six erasers.

MRS. JEWLS: Now, count the erasers, Joe, just the way I showed you.

JOE: One, two, three, four, five, six, seven, eight, nine, ten. There are ten, Mrs. Jewls.

MRS. JEWLS: No!

JOE: Didn’t I count right?

MRS. JEWLS: Yes, you counted right, but you got the wrong answer.

JOE: This doesn’t make any sense! When I count the wrong way, I get the right answer, and when I count right, I get the wrong answer.

MRS. JEWLS: (turning away and butting her head) Uh . . . uh . . . uh . . . uh . . . uh . . . . (turns back to JOE) How many times did I hit my head against the wall, Joe?

JOE: One, two, three, four, five, six, seven, eight, nine, ten. You hit your head against the wall ten times.

MRS. JEWLS: No!

JOE: Four, six, one, nine, five. You hit your head five times.

MRS. JEWLS: (shaking head, “no” ) Yes, that is right. ***** Bebe was the fastest draw in Mrs. Jewls’s class. She could draw a cat in less than forty-five seconds, a dog in less than thirty, and a flower in less than eight seconds! But of course, Bebe never drew just one dog, or one cat, or one flower. Art was from 12:30 to 1:30. Why, in that time, she could draw fifty cats, a hundred flowers, twenty dogs, and several eggs or watermelons! You see, it took her the same time to draw a watermelon as an egg. Calvin sat next to Bebe. He didn’t think he was very good at art. It took him the whole period just to draw one airplane. So instead, he just helped Bebe. He was Bebe’s assistant. As soon as Bebe would finish one masterpiece, Calvin would take it from her and set down a clean sheet of paper. Whenever her crayon ran low, Calvin was ready with a new crayon. That way, Bebe didn’t have to waste any time. And in return, Bebe would draw five or six airplanes for Calvin. It was 12:30, time for art. Bebe was ready. On her desk was a sheet of yellow construction paper. In her hand was a green crayon. Calvin was ready. He held a stack of paper and a box of crayons.

CALVIN: Ready, Bebe?

BEBE: Ready, Calvin.

MRS. JEWLS: All right, class. Time for art. She had hardly finished her sentence when Bebe had drawn a picture of a leaf. Calvin took it from her and put down another piece of paper.

BEBE: Red! Blue! They were quite a pair! Their teamwork was remarkable. Bebe drew pictures as fast as Calvin could pick up the old paper and set down the new. A fish. An apple. Three cherries— At 1:30, Mrs. Jewls announced,

MRS. JEWLS: Okay, class, art is over. Bebe dropped her crayon and fell over on her desk. Calvin sighed and leaned back in his chair. He could hardly move. They had broken their old record. Bebe had drawn three hundred and seventy-eight pictures! They lay in a pile on Calvin’s desk. Mrs. Jewls walked by.

MRS. JEWLS: Calvin, did you draw all these pictures?

CALVIN: No, Bebe drew them all.

MRS. JEWLS: Well then, what did you draw?

CALVIN: I didn’t draw anything.

MRS. JEWLS: Why not? Don’t you like art?

CALVIN: I love art. That’s why I didn’t draw anything.

MRS. JEWLS: I don’t understand.

CALVIN: It would have taken me the whole period just to draw one picture. And Bebe would only have been able to draw a hundred pictures. But with the two of us working together, she was able to draw three hundred and seventy-eight pictures! That’s a lot more art.

MRS. JEWLS: No, no! That isn’t how you measure art. It isn’t how many pictures you have, but how good the pictures are. Why, a person could spend their whole life drawing just one picture of a cat. In that time, I’m sure Bebe could draw a million cats.

BEBE: Two million.

MRS. JEWLS: But if that one picture is better than each of Bebe’s two million, then that person has produced more art than Bebe. Bebe looked like she was going to cry. She picked up all the pictures from Calvin’s desk and threw them in the garbage. Then she ran from the room, down all the stairs, and out onto the playground. Louis, the nice yard teacher, spotted her.

LOUIS: Where are you going, Bebe?

BEBE: I’m going home to draw a picture of a cat.

LOUIS: Will you bring it to school and show it to me tomorrow?

BEBE: Tomorrow? By tomorrow I doubt I’ll be finished with even one whisker. (rushes off) *****

MRS. JEWLS: Calvin, I want you to take this note to Miss Zarves for me.

CALVIN: Miss Zarves?

MRS. JEWLS: Yes, Miss Zarves. You know where she is, don’t you?

CALVIN: Yes. She’s on the nineteenth story.

MRS. JEWLS: That’s right, Calvin. Take it to her. Well, what are you waiting for?

CALVIN: She’s on the nineteenth story.

MRS. JEWLS: Yes, we have already established that fact.

CALVIN: The nineteenth story.

MRS. JEWLS: Yes, Calvin, the nineteenth story. Now take it to her before I lose my patience!

CALVIN: But, Mrs. Jewls—

MRS. JEWLS: NOW, Calvin!

CALVIN: Yes, ma’am! Calvin walked out of the classroom and stood outside the door. He didn’t know where to go. As you know, when the builder built Wayside School, he accidentally built it sideways. But he also forgot to build the nineteenth story. He built the eighteenth and the twentieth, but no nineteenth. He said he was very sorry. There was also no Miss Zarves. Miss Zarves taught the class on the nineteenth story. Since there was no nineteenth story, there was no Miss Zarves. And besides that, as if Calvin didn’t have enough problems, there was no note. Mrs. Jewls had never given Calvin the note.

CALVIN: (sarcastically) Boy, this is just great! I’m supposed to take a note that I don’t have, to a teacher who doesn’t exist, and who teaches on a story that was never built! He didn’t know what to do. He walked down to the eighteenth story, then back up to the twentieth, then back down to the eighteenth, and back up again to the twentieth. There was no nineteenth story. There had never been a nineteenth story. There would never BE a nineteenth story. Calvin walked down to the administration office on the first story. He decided to put the note in Miss Zarves’s mailbox. But there wasn’t one of those, either. That didn’t bother Calvin too much, though, since he didn’t have a note. He looked out the window and saw Louis, the yard teacher, shooting baskets.

CALVIN: Louis will know what to do. Hey, Louis!

LOUIS: Hi, Calvin. Do you want to play a game?

CALVIN: I don’t have time. I have to deliver a note to Miss Zarves up on the nineteenth story.

LOUIS: Then what are you doing all the way down here?

CALVIN: There is no nineteenth story.

LOUIS: Then where is Miss Zarves?

CALVIN: There is no Miss Zarves.

LOUIS: What are you going to do with the note?

CALVIN: There is no note.

LOUIS: I understand.

CALVIN: That’s good, because I sure don’t.

LOUIS: It’s very simple. You are not supposed to take no notes to no teachers. You already haven’t done it!

CALVIN: I’ll just have to tell Mrs. Jewls that I couldn’t deliver the note.

LOUIS: That’s good. The truth is always best. Besides, I don’t think I understand what I said, either! Calvin walked back up the thirty flights of stairs to Mrs. Jewls’s class.

MRS. JEWLS: Thank you very much, Calvin. That was a very important note, and I’m glad I was able to count on you.

CALVIN: Yes, but you see—

MRS. JEWLS: The note was very important. I told Miss Zarves not to meet me for lunch.

CALVIN: Don’t worry . . . She won’t! So now you know about Wayside School. Some people say these stories are strange and silly. That is probably true. But when the children at Wayside School heard stories about us, they thought we were strange and silly. And that’s for sure!
```

---

## IC-2123: Six to Eight Black Men

- Title: Six to Eight Black Men
- Author (byline): David Sedaris
- Work: Dress Your Family in Corduroy and Denim
- Publisher: Back Bay Books
- Publication date as stated: May 2005
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1401
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Sedaris
Book: Dress Your Family in Corduroy and Denim
ISBN: 978-0316010795
Publisher: Back Bay Books
Date (Month/Year): May 2005
```

### Introduction (context only: never use it for content warnings)

```text
Six to Eight Black Men by David Sedaris . . . . A heartwarming tale of Christmas in a foreign land where, if you've been naughty, Saint Nick and his friends give you a whuppin'.
```

### Performance text (classify this)

```text
I've never been much for guidebooks, so when trying to get my bearings in a strange city, I normally start by asking the cabdriver or hotel clerk some silly question regarding the latest census figures. I say silly because I don't really care how many people live in Olympia, Washington, or Columbus, Ohio. They're nice enough places, but the numbers mean nothing to me. My second question might have to do with average annual rainfall, which, again, doesn't tell me anything about the people who have chosen to call this place home. "When do you open your Christmas presents?" is another good conversation starter as it explains a lot about national character.

People who traditionally open gifts on Christmas Eve seem a bit more pious and family oriented than those who wait until Christmas morning. They go to mass, open presents, eat a late meal, return to church the following morning, and devote the rest of the day to eating another big meal. Gifts are generally reserved for children, and the parents tend not to go overboard. It's nothing I'd want for myself, but I suppose it's fine for those who prefer food and family to things of real value.

In France and Germany, gifts are exchanged on Christmas Eve, while in Holland the children receive presents on December 5, in celebration of Saint Nicholas Day. It sounded sort of quaint until I spoke to a man named Oscar, who filled me in on a few of the details as we walked from my hotel to the Amsterdam train station.

Unlike the jolly, obese American Santa, Saint Nicholas is painfully thin and dresses not unlike the pope, topping his robes with a tall hat resembling an embroidered tea cozy. The outfit, I was told, is a carryover from his former career, when he served as a bishop in Turkey.

One doesn't want to be too much of a cultural chauvinist, but this seemed completely wrong to me. For starters, Santa didn't use to do anything. He's not retired, and, more important, he has nothing to do with Turkey. The climate's all wrong, and people wouldn't appreciate him. When asked how he got from Turkey to the North Pole, Oscar told me with complete conviction that Saint Nicholas currently resides in Spain, which again is simply not true. While he could probably live wherever he wanted, Santa chose the North Pole specifically because it is harsh and isolated. No one can spy on him, and he doesn't have to worry about people coming to the door. Anyone can come to the door in Spain, and in that outfit, he'd most certainly be recognized. On top of that, aside from a few pleasantries, Santa doesn't speak Spanish. He knows enough to get by, but he's not fluent, and he certainly doesn't eat tapas.

While our Santa flies on a sled, Saint Nicholas arrives by boat and then transfers to a white horse. The event is televised, and great crowds gather at the waterfront to greet him. I'm not sure if there's a set date, but he generally docks in late November and spends a few weeks hanging out and asking people what they want.

"Is it just him alone?" I asked. "Or does he come with backup?"

Oscar's English was close to perfect, but he seemed thrown by a term normally reserved for police reinforcement.

"Helpers," I said. "Does he have any elves?"

Maybe I'm just overly sensitive, but I couldn't help but feel personally insulted when Oscar denounced the very idea as grotesque and unrealistic. "Elves," he said. "They're just so silly."

The words silly and unrealistic were redefined when I learned that Saint Nicholas travels with what was consistently described as "six to eight black men." I asked several Dutch people to narrow it down, but none of them could give me an exact number. It was always "six to eight," which seems strange, seeing as they've had hundreds of years to get a decent count.

The six to eight black men were characterized as personal slaves until the mid-fifties, when the political climate changed and it was decided that instead of being slaves they were just good friends. I think history has proven that something usually comes between slavery and friendship, a period of time marked not by cookies and quiet times beside the fire but by bloodshed and mutual hostility. They have such violence in Holland, but rather than duking it out among themselves, Santa and his former slaves decided to take it out on the public. In the early years, if a child was naughty, Saint Nicholas and the six to eight black men would beat him with what Oscar described as "the small branch of a tree."

"A switch?"

"Yes," he said. "That's it. They'd kick him and beat him with a switch. Then, if the youngster was really bad, they'd put him in a sack and take him back to Spain."

"Saint Nicholas would kick you?"

"Well, not anymore," Oscar said. "Now he just pretends to kick you."

"And the six to eight black men?"

"Them, too."

He considered this to be progressive, but in a way I think it's almost more perverse than the original punishment. "I'm going to hurt you, but not really." How many times have we fallen for that line? The fake slap invariably makes contact, adding the elements of shock and betrayal to what had previously been plain, old-fashioned fear. What kind of Santa spends his time pretending to kick people before stuffing them into a canvas sack? Then, of course, you've got the six to eight former slaves who could potentially go off at any moment. This, I think, is the greatest difference between us and the Dutch. While a certain segment of our population might be perfectly happy with the arrangement, if you told the average white American that six to eight nameless black men would be sneaking into his house in the middle of the night, he would barricade the doors and arm himself with whatever he could get his hands on.

"Six to eight, did you say?"

In the years before central heating, Dutch children would leave their shoes by the fireplace, the promise being that unless they planned to beat you, kick you, or stuff you into a sack, Saint Nicholas and the six to eight black men would fill your clogs with presents. Aside from the threats of violence and kidnapping, it's not much different from hanging your stockings from the mantel. Now that so few people have a working fireplace, Dutch children are instructed to leave their shoes beside the radiator, furnace, or space heater. Saint Nicholas and the six to eight black men arrive on horses, which jump from the yard onto the roof. At this point, I guess, they either jump back down and use the door, or they stay put and vaporize through the pipes and electrical wires. Oscar wasn't too clear about the particulars, but, really, who can blame him? We have the same problem with our Santa. He's supposed to use the chimney, but if you don't have one, he still manages to come through. It's best not to think about it too hard.

While eight flying reindeer are a hard pill to swallow, our Christmas story remains relatively simple. Santa lives with his wife in a remote polar village and spends one night a year traveling around the world. If you're bad, he leaves you coal. If you're good and live in America, he'll give you just about anything you want. We tell our children to be good and send them off to bed, where they lie awake, anticipating their great bounty. A Dutch parent has a decidedly hairier story to relate, telling his children, "Listen, you might want to pack a few of your things together before you go to bed. The former bishop from Turkey will be coming along with six to eight black men. They might put some candy in your shoes, they might stuff you in a sack and take you to Spain, or they might just pretend to kick you. We don't know for sure, but we want you to be prepared."

This is the reward for living in Holland. As a child you get to hear this story, and as an adult you get to turn around and repeat it.
```

---

## IC-2124: Sleeping Ugly

- Title: Sleeping Ugly
- Author (byline): Jane Yolen
- Work: Not specified
- Publisher: Puffin Books
- Publication date as stated: April 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MISERELLA, FAIRY, JANE, JOJO
- Teaser before the introduction: No
- Spoken words (computed): 1114
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jane Yolen
ISBN: 978-0698115606
Publisher: Puffin Books
Date (Month/Year): April 1997
```

### Introduction (context only: never use it for content warnings)

```text
Princess Aurora . . . kind, elegant, carefree and beautiful – But she’s not in this story. She’s in the story of Sleeping Beauty. This story is about Princess Miserella . . . beautiful, spiteful, hateful and a consummate liar. Sleeping Ugly by Jane Yolen.
```

### Performance text (classify this)

```text
Princess Miserella was a beautiful princess if you counted her eyes and nose and mouth and all the way down to her toes. But inside, where it was hard to see, she was the meanest, wickedest and most worthless princess around. She liked stepping on dogs. She kicked kittens. She threw pies at the cook’s face. And she never, not even once, said “thank you” or “please.” And besides, she told lies! In the very same kingdom, in the middle of the woods, lived a poor orphan named Plain Jane.

She certainly was! Her hair was short and turned down. Her nose was long and turned up. And even if they had been the other way around, she would not have been a great beauty. But she loved animals, and she was always kind to strange old ladies. One day Princess Miserella rode out of the house in a huff. A huff is not a kind of carriage. It’s a kind of temper tantrum – her usual kind. She rode and rode looking beautiful, as always even with her hair in tangles. She rode right into the middle of the woods and was soon lost. She got off her horse and slapped it sharply for losing the way. The horse said nothing but ran right back home. It had known the way back all the time but was not about to tell Miserella. So there was the princess lost in the dark wood. It made her look even prettier. Suddenly Princess Miserella tripped over a little old lady under a tree asleep. Now, little old ladies who sleep under trees deep in a dark wood are almost always fairies in disguise. Miserella guessed who the little old lady was, but she did not care.

MISERELLA: (kicking the old lady) Get up and take me home!

So the old lady got to her feet very slowly. She took Miserella by the hand. She only used her thumb and second finger. Fairies know quite a bit about that type of princess.

They walked and walked even deeper into the woods There they found a little house. It was Plain Jane’s house. It was dreary. The floors sank, the walls stank and the roof leaked – even on sunny days. But Jane made the best of it. She planted roses around the door and little animals and birds made their home with her.

MISERELLA: (sniffing disdainfully) This is not my home!

FAIRY: Nor mine.

They walked in without knocking and there was Jane.

JANE: It is mine.

MISERELLA: (looking Jane over; up and down) Take me home! And as a reward, I will make you my maid.

FAIRY: (whispered) Some reward! (aloud) If you could take both of us home, I could squeeze probably a wish or two.

MISERELLA: (to the Fairy) Make it three and I’ll get us home.

Plain Jane smiled. The birds began to sing.

JANE: My home is your home.

FAIRY: I like your manners. And for that good thought, I'll give the three wishes to you.

Princess Miserella was not pleased. She stamped her foot.

FAIRY: (taking a wand from her pocket) Do that again, and I'll turn your foot into stone.

Just to be mean, Miserella stamped her foot again. It turned to stone.

JANE: (sighs a loud sigh) Well, my first wish is that you change her foot back.

FAIRY: (Making a face) I like your manners, but not your taste. Still, a wish is a wish. (She waves her wand)

MISERELLA: (shaking her foot which was no longer made of stone, she told a lie, like always) I guess my foot fell asleep for a moment. Besides, that was a stupid way to waste a wish.

FAIRY: (angrily) Do not call someone stupid, unless you have been properly introduced, or are a member of their family! Miserella hated to be told what to do.

MISERELLA: Stupid, Stupid, Stupid!

FAIRY: Say "stupid" again (holds up her wand, ready for action) and I'll make toads come out of your mouth!

MISERELLA: Stu . . . pid! (mimes a toad coming from her mouth)

JANE: (Jane knelt down and picked up the toad petting it gently) Ahhhhh, cute! And I do like toads, but…

FAIRY: But?

Miserella did not open her mouth. Toads were among her least favorite animals.

JANE: But, my second wish is that you get rid of the mouth toads.

FAIRY: (mumbling) She's lucky it wasn't mouth elephants. (She waves the wand again)

MISERELLA: (Miserella opened her mouth slowly. Nothing came out but her tongue which she pointed at the fairy.) I definitely have had enough. I want to go home! (she grabs Plain Jane’s arm)

FAIRY: Gently . . . Gently . . . If you're not gentle with magic, none of us will go anywhere.

MISERELLA: You can go where you want, but there is only one place I want to go.

FAIRY: (Angry, she waves her wand and shouts) To sleep!

She waved her wand so hard, she hit the wall of Jane’s house. The wall broke. The wand broke. The spell broke. And before Jane could make her third wish. . . all three of them were asleep.

It was one of those famous hundred-year naps that need a prince and a kiss to end them. So they slept and slept and slept. They slept through three and a half wars, six new kings, and the invention of the sewing machine. The cottage was deep in the woods so very few princes passed by. And none of the ones who did even tried the door. At the end of 100-years a prince named JoJo, who was the youngest son of a youngest son, and so had no gold, or jewels, or property to speak of came into the woods He stepped into the cottage over the broken wall. He saw three women asleep with spider webs holding them to the floor. One of them was a beautiful princess. Being the kind of young man who read fairy tales, JoJo knew just what to do. But Jojo had never kissed anyone before, except his mother, which didn’t count and his father, who had a beard. JoJo thought he should practice before he tried kissing the princess. So he puckered up his lips and kissed the old fairy on the nose. (JoJo smiles and nods his head) It was quite pleasant. She smelled slightly of cinnamon. He moved on to Jane. He puckered up his lips and kissed her on the [cheek].

JOJO: Delightful! (Sniffs) Wildflowers! Just then the fairy and Plain Jane woke up. Prince Jojo's kisses had worked! The fairy picked up the pieces of her wand. Jane looked at the prince.

JANE: (touching her cheek and looking longingly at the prince, she whispers to herself) I wish he loved me.

FAIRY: Good wish! (she waves the two pieces of her broken wand gently) The prince looked at Miserella, who was having a bad dream and enjoying it. (Miserella snorts, bats her arms about and frowns). Even frowning she was beautiful. But Jojo knew that kind of princess.

JOJO: Pretty on the outside, but ugly within.

He remembered the smell of wildflowers and turned back to Jane.

JOJO: I love you. What's your name?

So they lived happily ever after in Jane's cottage. The prince fixed the roof and the wall and built a house next door for the old fairy. They used the sleeping princess as a conversation piece when friends came to visit. Or sometimes they stood her up, still fast asleep, in the hallway and let her hold coats and hats. But they never let anyone kiss her awake. Not even their children, who numbered 3.

The moral of the story? Let sleeping princesses lie . . . or lying princess sleep; whichever seems wisest!
```

---

## IC-2125: Snow White & the Seven Microaggressions

- Title: Snow White & the Seven Microaggressions
- Author (byline): Laura Lane and Ellen Haun
- Work: Cinderella and the Glass Ceiling, Pgs 22-31
- Publisher: Seal Press
- Publication date as stated: Mar 2020
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, EVIL QUEEN, MAGIC MIRROR, MARK, BOB
- Teaser before the introduction: Yes
- Spoken words (computed): 1434
- Already set (do not supply): none

### Source block (context only)

```text
Author: Laura Lane and Ellen Haun
Book: Cinderella and the Glass Ceiling, Pgs 22-31
ISBN: 978-1580059060
Publisher: Seal Press
Date (Month/Year): Mar 2020
```

### Introduction (context only: never use it for content warnings)

```text
Snow White is a classic fairy tale. But in this modernized twist, the Evil Queen isn’t just obsessed with beauty -- she’s also completely clueless about how damaging her choice of words can be. The Magic Mirror, part therapist and part DEI consultant, tries to teach her about pronouns and microaggressions, not to mention the inappropriateness of targeting her opponents. And with a touch of fairy-tale chaos, we begin to understand how language, power, and self-awareness collide.

In the words of Desmond Tutu "Language is very powerful. [It]does not just describe reality. [It]creates the reality it describes."

Snow White & the Seven Microaggressions by Laura Lane and Ellen Haun
```

### Performance text (classify this)

```text
NARRATOR: (Pg 22 – 31) Once upon a time . . . there lived a vain, evil, and verbally abusive queen, who was the stepmother to a teenager named Snow White. Stepmothers tend to get a bad rap in fairy tales, but this one was truly evil. The Queen was concerned Snow White would one day grow to be more beautiful than herself. Not to psychoanalyze the Evil Queen, but there were clearly some deep-seated issues happening for her to feel so insecure. Every morning the Evil Queen would look into her Magic Mirror and say:

EVIL QUEEN: Mirror, Mirror, on the wall, who is the fairest of them all?

MAGIC MIRROR: Beauty is a subjective social construct, the use of the word ‘fair’ is problematic because it means both ‘white’ and ‘beautiful,’ and I terribly hate casting judgment on appearances. But all that aside, you, my Queen, are the fairest of them all.

NARRATOR: While the Queen was busy talking to mirrors, Snow White was out living large after moving into a crazy-cute cottage with seven dude roommates who were rarely home. Initially there was a big problem when they left their dishes in the sink and assumed Snow White would deal with the mess. But Snow White put a quick kibosh on that sitch by making a chore chart . . . One day, per usual, the Queen asked:

EVIL QUEEN: Mirror, Mirror, on the wall, who is the fairest of them all?

NARRATOR: But before answering, the Mirror decided to pay the Evil Queen a compliment.

MAGIC MIRROR: You know, I’ve been meaning to tell you that your use of the gender neutral pronoun ‘them’ in your question is quite excellent and inclusive. For an Evil Queen, it’s very impressive.

EVIL QUEEN: Thank you. Snow White explained to me that they identify as nonbinary and prefer the pronouns ‘they’ and ‘them.’ They aren’t a maiden, like I thought. So, I say ‘them’ to make sure you include Snow White when I ask who is fairest in the kingdom. Because I’ll murder hims, hers, xems, zes, hirs, theys, thems. Really anyone who is hotter than me.

MAGIC MIRROR: You are doing an excellent job of respecting Snow White’s—

EVIL QUEEN: (snapping) Answer my question!

MAGIC MIRROR: Like I always say before I answer this question, beauty is a subjective —

EVIL QUEEN: Blah blah blah, answer the question.

MAGIC MIRROR: According to industrialized western white beauty standards, it’s no longer you, my Queen. Snow White is the fairest of them all.

EVIL QUEEN: (shouting, she takes off her tiara and throws it) Dammit! Now I have to kill her.

MAGIC MIRROR: Hold up. You mean you have to kill them. You were doing so well.

EVIL QUEEN: I’m too upset to think about language right now! It’s been a huge hassle for me to have to remember every time I’m around her. Them. Whatever!

MAGIC MIRROR: No. It’s not whatever. It’s really important to Snow White, which is why they had a long conversation with you about it.

EVIL QUEEN: It’s grammatically incorrect anyway.

MAGIC MIRROR: Not anymore . . . Language evolves.

EVIL QUEEN: Okay, fine. I want to kill them because they are more fair than me. Is that better?

MAGIC MIRROR: In terms of pronouns, yes. In terms of content, absolutely not. Baby steps.

EVIL QUEEN: Great, let’s discuss their murder.

MAGIC MIRROR: Can we focus on one problematic thing at a time? We’ll get to why murder is bad later. But since we’re on the topic of respectful language, I’ve been meaning to address something. You see, you have a tendency to commit something called microaggressions on a daily basis. With a lot of people. It’s a problem.

EVIL QUEEN: Micro-what?

MAGIC MIRROR: Microaggressions. They are subtle insults made to marginalized people or mirrors. They are typically delivered in everyday interactions by well intentioned people, so imagine how bad they are delivered by an Evil Queen.

EVIL QUEEN: I do not do that. Ask my henchman! Hey, Mark, come over here! Tell the Mirror how nice I am.

NARRATOR: The henchman, who lost a leg in a sword fight years ago, came over in his wheelchair.

EVIL QUEEN: (laughing) You better slow down or you’re going to get a speeding ticket in that thing!

MAGIC MIRROR: That, right there, was a microaggression. It’s ableism.

EVIL QUEEN: Oh, come on! That’s how we joke together. He likes it.

MARK: (nervously) Um, actually, your Royal Highness, ma’am, Evil Queen. I don’t think it’s funny. It makes me feel defined by my disability. I’ve just been too scared of you to say anything. You throw things.

EVIL QUEEN: You’re just being lazy. You could totally walk and use that peg leg if you wanted to. Also, your shirt is ugly.

NARRATOR: There was a long silence in the room. The Magic Mirror blinked at the Evil Queen.

EVIL QUEEN: Okay, fine. I was being mean. But that time it was on purpose. Mark, you are dismissed.

(calling after him as he exits) And bring me Bob, my second henchman. Let’s get his opinion on whether I’m doing microaggressions or not. And in the future, you have no reason to be scared of me!

NARRATOR: Mark did as he was told. A few moments later, the Queen’s second henchman, Bob, walked in.

EVIL QUEEN: Hi, Bob. Two things. First, I want you to behead Mark. Second, this Mirror thinks I’m committing microaggressions, so I need you to tell it how nice I am.

BOB: Yes, Evil Queen. You are so nice.

EVIL QUEEN: See, Mirror, I am so nice. Also, can we take a moment to compliment Bob on how great his English is. Where are you from again, Bob?

BOB: I’m from this kingdom, ma’am.

EVIL QUEEN: No, like, where are you from-from? Originally.

MAGIC MIRROR: (interrupting) Okay! That’s enough. Those were a bunch of microaggressions, back to back! It might seem trivial to you, but when you told Bob his English was good, you implied that he is an outsider in this kingdom, which is a hidden insult. This creates a hostile work environment for Bob. Even more hostile than working for an Evil Queen.

EVIL QUEEN: It was a compliment! Bob doesn’t look like he’s from here.

MAGIC MIRROR: (shouting) Microaggression alert!

BOB: (sheepishly, looking at the ground) That hurts my feelings.

EVIL QUEEN: But, Bob, you can admit you’re highly sensitive, right? I doubt the other foreign-looking henchman would feel the way you do.

BOB: I don’t want to speak for all nonwhite henchmen. I can’t possibly represent all of their perspectives. I wouldn’t ask you to speak for all Evil Queens.

EVIL QUEEN: Obviously not. I’m special. I’m not like the other ones. . . Okay, I see your point there.

MAGIC MIRROR: We’re making strides. I think you’re learning that microaggressions can be unintentional, yet harmful. They are based on institutional oppression and often committed by those in power. And you are very powerful, my Evil Queen.

EVIL QUEEN: Indeed I am! We’re done here, Bob. Go behead Mark and then meet me by the guillotine. Don’t worry, it’s not for you. Well, maybe it is. It will be a surprise! Just meet me there. (Bob nervously exits) Great. Now I have to kill both of my henchmen. Magic Mirror, who am I going to get to kill Snow White and those stupid seven dwarfs? Or, wait, let me guess, ‘dwarf’ isn’t acceptable now?

MAGIC MIRROR: Actually, sometimes it is. The best thing to do is to ask the person what they’d like to be called. Some people with dwarfism prefer ‘dwarf’ and others prefer ‘little people.’ They’re just people, who don’t need to be defined by their size. In general, use their names and if you have to refer to their small stature, saying a ‘person with dwarfism’ is typically best.

EVIL QUEEN: So, I should say, ‘Mirror, Mirror, on the wall, how should I kill Snow White and the seven men with dwarfism?’

MAGIC MIRROR: Exactly! In terms of language, at least, you’re getting it. At the end of the day, they’re just seven adult men who live in a house together. And let’s be honest, that’s the weird part.

EVIL QUEEN: You know what all this reminds me of? That time I was at the Convention for Evil Leaders and I was the only Evil Queen at the table. The Evil Kings wouldn’t listen to me! I had this great idea about how to steal a cyclops and one of the kings pretended it was his idea. So annoying.

MAGIC MIRROR: Yes! Microaggressions are often committed against women, good and evil.

EVIL QUEEN: I ended up having the cyclops behead all of the Evil Kings.

MAGIC MIRROR: Of course you did, Your Highness. In the future, let’s try to be a little less defensive when someone tells you that you’ve offended them, be constantly vigilant against your own unconscious biases, and remember that murderous henchmen have feelings, too.

EVIL QUEEN: This has given me a lot to think about. However, don’t forget that since Snow White is still the hottest person in the kingdom, we still have to kill them, as well as the seven men with dwarfism, and my henchpeople Mark and Bob, whom I will not define by their disability or racial background. (smiles proudly)

MAGIC MIRROR: (beaming back at her) We’ve done great work here today. Tomorrow, we’ll tackle murder.
```

---

## IC-2126: Son of Rumpelstiltskin

- Title: Son of Rumpelstiltskin
- Author (byline): AJ Jacobs
- Work: Fractured Fairy Tales
- Publisher: Bantam Books, Inc.
- Publication date as stated: Nov 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1584
- Already set (do not supply): none

### Source block (context only)

```text
Author: AJ Jacobs
Book: Fractured Fairy Tales
ISBN: 978-0553099805
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

"It's, uh . . ." The little man took off his hat and scratched his head. "It's, uh . . ." Then a horrible real-ization came to him. He didn't know what his name was!

"Wait here. I'll be right back," he said to the queen. He dashed into the kingdom to see if he could find anybody who could tell him what his name was.

Once a very long time ago, In a forest, there was a tree-which is a nice thing to have in a forest. Now, in this tree there happened to live a funny little man in a green suit with a pointed cap. He lived with his son-also a funny little man in a green suit with a pointed cap.

One day the son walked over to his father's side of the branch with a question he had been wondering about for fifty years. (He hadn't wanted to rush things.)

"How come we've got to live in a tree?" he asked.

"Because we're not ordinary folks, boy," replied the older little man, wagging his wisdom-filled finger. "We're magic."

"Magic?"

"Yup," said the father. "You know how sometimes folks get into trouble and then they meet a funny little man who makes a deal to help 'em out? And he does a little magic and then later on, they write a fairy tale about it?" He pulled a fairy-tale book out of his cap. and pointed to some funny little men. "Funny little men. That's us."

And then, being that it was the son's six hun-dredth birthday, the father told him it was time he go out in the world and make a name for himself.

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

The next morning, the king placed the unfortunate miller's daughter in a dark room in the castle with nothing but a spinning wheel and a stack of straw.

"Now spin that straw to gold-or else!" ordered the king. Thereupon, he thoughtfully gave the girl her privacy by gently closing the door and nailing it shut.

Alone in the room, the miller's daughter sat down and put her chin in her hands. "I don't want to be or elsed"

The funny little man in the green suit with a pointed cap-the one trying to make a name for himself-'- had heard about the young girl's plight, and knew that this was the chance that he had been waiting for. So into the room he hopped.

"Who are you?" exclaimed the girl.

"I'm a funny little man in a green suit."

"You could say that again."

"I'm a funny little man in a-"

"Never mind," said the daughter, who had no time for such shenanigans. After all, she was busy doing nothing. "What do you want'?" she asked.

"I will spin that straw to gold for you if you will give me your first child after you become queen."

"My first child? Why that?"

"Who knows?" The little man shrugged. "Makes the plot better."

Not one to interfere with the plot, the miller's daughter shook hands with the little man. He jumped to the wheel and in no time at "all had spun a room full of bright, shimmering gold. When in the morning the king found everything as he had wished, he was overjoyed. He now had so much money he could be king. That is, if he weren't king already.

They were married, and the miller's daughter be-came queen. She was given a throne right next to her husband, and learned to sit for long periods of time, as kings and queens do.

About two years afterward, a beautiful child was born and the little man appeared in the castle once again.

"Hi! I came for the kid," he said.

The queen jumped back and clutched her child to her chest.

"But you can't have my child! What will you do with him?"

"Dress him in a green suit and make a funny little old man out of him. What else?"

The queen imagined her baby in a little green suit and little pointed cap and began sobbing loudly. In fact, she sobbed so loudly the man decided to give her a second chance.

Pulling his fingers out of his little ears, he said, "I'll tell you what. I'll make a deal. If you can discover what my name is in two days, you can keep the child." The little man paused. "Boy, won't this make a keen fairy tale someday'?"

The queen began pacing the royal nursery and calling to mind all the names that she could think of.

"Are you Henry? Clyde? Newton? George, Mar-maduke, Sidney, Frank?"

"Nah," said the man.

The queen then desperately searched for still other names. She looked in the village white pages, Who's Who Among the Little People, even the gossip column of the Palace Chronicles. The next day she tried again.

"Are you Ming Choi?" she asked. "Or Running Mouse? Cherry Nose? Charlie Brown?"

"No! You've failed," shouted the little man with a mischievous laugh.

"Well, what is your name then'?" challenged the queen, her hands on her hips.

"It's, uh . . ." The little man took off his hat and scratched his head. "It's, uh . . ." Then a horrible real-ization came to him. He didn't know what his name was!

"Wait here. I'll be right back," he said to the queen. He dashed into the kingdom to see if he could find anybody who could tell him what his name was.

"Do you know me'?" he asked the palace garbage collector.

"No. I can't say I do-and with any luck I never will," the garbage man replied, jumping into a garbage can and pulling the lid on top of him.

The little man asked everyone he chanced to meet, from the village moat cleaner to the royal jack hammer operator, but nobody could tell him who he was. Finally, out of desperation, he went to an old wise man who lived in a hole in the ground.

"No, I don't know your name," said the wise man in the hole in the ground. "But I know how you can find out. Get yourself a mailbox. Sooner or later, somebody will send you a letter. Then all you have to do is see what name is on the envelope."

That was it! He was truly a wise man-or at least as wise as anyone can be who chooses to live in a hole in the ground.

In any case, the little man did as he was in-structed. He got a mailbox and waited inside for a delivery, and before long, he did receive a letter. It was from a talk show sidekick who told him he might have already won a million dollars. But that's another fairy tale. The little man just wanted to see what his name was. But when he saw it, he was shocked. It read "Rumpelstiltskin."

"Rumpelstiltskin!" he cried. "What kind of a name is that? I can't go back to the queen and tell her my name is Rumpelstiltskin. I'd be the laughingstock of the kingdom."

And so, the queen and her child lived happily ever after, for she never saw the funny little man in the green suit again. In fact, nobody ever saw the little man again, because he was so ashamed he got out of the magic business and changed his name to Louie Smith.

And we all know there's never been a fairy tale about Louie Smith. That is, until just now.
```

---

## IC-2127: The Speech and A Breakup Technique DON’T

- Title: The Speech and A Breakup Technique DON’T
- Author (byline): Laurie Notaro and Lynn Harris
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Prose
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1513
- Already set (do not supply): none

### Source block (context only)

```text
Author: Laurie Notaro
Book: The Idiot Girls’ Action-Adventure Club
ISBN: 978-0375760914
Publisher: Villard
Date (Month/Year): July 2002
Author: Lynn Harris
Book: Breakup Girl to the Rescue!: A Superhero's Guide
to Love, and Lack Thereof
ISBN: 978-0316091886
Publisher: Little, Brown
Date (Month/Year): 2009
```

### Introduction (context only: never use it for content warnings)

```text
Breakups are the worst. Sometimes they're the worst because you have lost someone that you truly care about and will miss; sometimes they're the worst because you have put all your eggs in one person-size basket and that person-size basket unceremoniously dumps you; sometimes they're the worst because now what am I supposed to do with my time? Regardless of the reasons surrounding a breakup . . . hearing The Speech is never a good thing. The Speech by Laurie Notaro
```

### Performance text (classify this)

```text
The Speech by Laurie Notaro

Relationships suck.

They suck hard.

Sometimes, in the middle of the night, when my bedroom is as black as death, and the sheets on half the bed are as cold as a five-day-old corpse, I think

All ever wanted to be was someone's Old Lady.

I want to be the ball and chain.

I need to be somebody's squeeze.

I float in this for a minute, in this bed that is too big for me, and feel a little bit lonely when all of a sudden the wheezing, flopping noise from my lungs wakes me up and shocks me back into Relationship Reality, and I realize . . .

The empty side of the bed does not fart in its sleep.

The empty side of the bed does not make me look at the turd as big as my leg grounded in the toilet and then ask aloud, "Dude, do you think it will go down in one flush?"

The empty side of the bed does not wrestle me to the floor, pin me, and then straddle me, in order to do the Spit Torture, dripping saliva out of its mouth over my face, then sucking it back up; dribbling it out, then sucking it back up; dribbling it out, then letting it fall right near my mouth.

The empty side of the bed IS NOT, I repeat, IS NOT a MAN.

And for that, I am thankful.

I want a man as nice as my retarded dog, but one that doesn't crap on the floor. I want a man who will only cheat on me a little and who will call me once a week. I want a man who will buy his own drinks and who will hold back my hair when I puke. I want a man who is unconfused regarding his sexual identity. I want a man who has never heard of or practiced the Speech.

I will never find him. He has never been born.

The last time I got my walking papers, it was over the phone. "It" had lasted about five months, the longest-standing Relationship Record I had held in this decade. Well, it wasn't even a "relationship." I called it the "thing." He didn't call it anything. He thought I wanted to get married tomorrow, have seventeen kids, and buy an Isuzu Trooper.. All I really wanted was one phone call per solstice.

Anyway, the conversation was off to a running start when he cleared his throat and said,

"I am not ready and will not be ready to actively get involved with anyone for at least three to five years."

"Why?" I asked. "Are you going to prison?"

"No. What I am saying is that I'm not ready to commit to anything, either way."

"Either way? You mean you can or cannot commit to committing or not committing?" I said, growing suspicious and confused. "Are you giving me 'the Speech'?"

"I think we should concentrate more on the 'Friends' part of our-well, you know."

Suspicions confirmed. I gasped.

"You ARE giving me the Speech! You just gave me the Speech! That was the Speech!" I cried.

So I got the Speech, which automatically drops you to the lowest point in life, it's like throwing the self-esteem balloon on a cactus. You become such a small specimen of existence that you could probably mate with yourself, which would actually be such a terrific advantage.

I guess I took it well. I didn't set anything on fire, practice any voodoo, or listen to sad songs. No, this time I just sat at the bar and drank, sneering and growling at all of the men except my friend Dave.

"How's it going?" he asked.

"Well, I got the Speech today," I said.

"Oh no. Not the Speech," he said. "Did he use the 'F' word?"

I nodded.

"Oh God." Dave sighed. "The 'F' word is low. Low down."

"Yep," I said. "Friends. He said, 'We're just Friends.' "

I don't understand the Speech and how men learned about it. Was it a part of boys' eighth-grade PE class, did the gym teacher make them say it to one another over and over in the showers so they would be good at it?

"Okay, now how does it go?"

"It goes, 'You're a cool girl, and I like hanging out with you, but I'm not ready to make a - um, that big word - commitment to one person, and I think we need to be . . . we need to be . . . ' "

"Man, this is the most important part! The 'F' word, man! The 'F' word!"

"Oh, yeah! You tell the chick you want to be Friends! But you don't mean it, do you?"

"No.”

Or maybe the Speech is some kind of computer chip that gets implanted in every baby boy as soon as he's born.

"There are things running around out there with uteruses, son. You're goingto need this."

Could it be a hormonal gift package with an added feature thing, where women get PMS with estrogen, and men get the Speech with testosterone? I don't understand it.

Maybe it's just my destiny to remain alone, eating single-people food like Soup for One, collecting Precious Moments figurines, and thinking that my dog can talk back to me. Oh, God. With any luck, I'll wind up living in a trailer park as a bitter, celibate [woman] with a heart full of hate. I'd much rather be alone and make myself miserable than give someone else the pleasure.

TRANSITION OK . . . women struggle after a break-up, but so do guys! And they may not have a close friend to confide in . . . so what options do they have? When we had questions about manners in the 1950s, we wrote to Dear Abbey . . . Today when we have questions about relationships, we can write to Breakup Girl! A Breakup Technique DON’T . . . by Lynn Harris

A Breakup Technique DON’T . . .

Dear Breakup Girl,

After three years my girlfriend broke up with me on the phone – and then refused to talk about it because she was late for a movie! When we finally spoke, she said, “I’m going out with someone else now, and there is no chance of us getting back together.” Her new boyfriend, she said, was a “real man” who could provide for her financially and emotionally in a way I could not (he has a $45,000 job and a $35,000 Jeep, and I am a grad student). I e-mailed her to ask for my stuff back – and her new boyfriend responded, saying he was her soul mate and that she never wanted to see or hear from me again. Then she dropped off a box containing every gift I had ever given her, except the stuffed animals, which, her note said, she’d given to charity.

I don’t understand what has happened. I was always kind, caring, and understanding to her, and then she ended the relationship in such a callous manner. How could she continue saying ‘I love you’ till the end, then two days after breaking up with me jump into a new relationship, claiming this person as a soul mate? All I know is that I am really hurt and . . .

Confused ************* Dear Confused,

Does it make you feel at all betrer – in a heaving, hollow sort of way – that your ex has violated just about every breakup rule there is?

1. Phone breakups are not allowed in three-year

relationships.

2. While it doesn’t work to talk your dumpee

through a breakup, you at least owe it to

him/her to talk about it. Time-management

tip: If you’re going to be late for the movies,

dump him/her afterward.

3. No follow-up calls involving the words “new

boyfriend” or “real man” or actual dollar

amounts.

4. Gift return is permitted if deemed a

necessary purging and healing process, but

only with a note saying something like, “I’m

sorry, but it will be easier for me to move on

without these.”

But BG is not in the business of making people feel better by saying, “You’re right, s/he is very, very bad and wrong!” and leaving it at that. So. What happened? It’s possible that she and Mr. Soul Mate were already shagging and she got tired of the complicated scheduling. Or, she wanted a way out – for whatever reason – and happened to see this guy in a Jeep with a big red “Exit” sign over his head.

And sometimes, callous is easier than careful. You behave badly, you don’t have to make the time or effort to deal. You rationalize twistedly: “Well, maybe if I’m a huge troll, s/he’ll be glad to see/let me go.”

All of which hardly makes you feel better right now, but in the long run, it will. So will this: If he really makes $45,000 and spent $35,000 on a Jeep, he has only $10,000 – well, $6,600 after taxes – left for everything else, like food, clothing, and . . . rent. She says he “provides for her”; I say they live in his care.

Love,

Breakup Girl
```

---

## IC-2128: Squids will be Squids

- Title: Squids will be Squids
- Author (byline): Jon Scieszka
- Work: Not specified
- Publisher: Viking Press
- Publication date as stated: Sept 1998
- Event as filed: Prose
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

Deer, Mouse, Rabbit and Squid: Deer, Mouse, Rabbit and Squid sat on the steps trying to decide what to do. "Let's go see a movie," said Deer. "Great," said Mouse. "Great" said Rabbit. "There's nothing good on," said Squid. "Let's play Frisbee in the park," said Mouse. "Great," said Rabbit. "Great," said Deer. "My tentacles are too tired," said Squid. "Let's go shopping," said Rabbit. "Great," said Deer. "Great," said Mouse. "That's so boring," said Squid. "I'm just going to go home,” and she oozed off down the street. "Great," they said. Then they ran off to see a movie, play Frisbee in the park, and go shopping.

MORAL: Squids will be Squids.

Grasshopper Logic: One bright and sunny day, Grasshopper came home from school, dropped his backpack and was just about to run outside to meet his friends. “Where are you going?” his Mom asked. “Out to meet some friends,” said Grasshopper “Do you have any homework due tomorrow?” asked his Mom. “Just one small thing for History. I did the rest in class.” “Okay, “ said Mom Grasshopper, “Be back at six for dinner. Grasshopper hung out with his friends, came home promptly at six, ate his dinner, then took out his History homework. His Mom read the assignment and freaked out. “Rewrite twelve Greek myths as Broadway musicals. Write music for songs. Design and build all sets. Sew original costumes for each production.” “How long have you known about this assignment?” asked Mom Grasshoper, trying not to scream. “I don’t know,” said Grasshopper.

MORAL: There are plenty of things to say to calm a hopping mad Grasshopper Mmom. “I don’t know” is not one of them.

Pigeon Pie: Pigeon was a very good artist. But she had one very annoying habit. Every time she finished a painting she would show it and say, “It’s not very good” just to get someone to say, “Oh no Pigeon. That’s very good.” One day after she chased everyone else away with her annoying habit, she showed her painting to Saber-Toothed Tiger. “Oh, Look at my painting…. It’s not very good.” Saber-Toothed Tiger licked his long saber teeth. “Oh, no, Pigeon. That’s very good. I’m sure it will be perfect roasted, fried, or baked in a pie.” Pigeon was puzzled. She had painted a sad-eyed clown. Then she noticed that Saber-Toothed Tiger wasn’t looking at the painting. But it was too late and the end of this fable is too messy to even tell.

MORAL: Whatever looks like a pigeon and acts like a pigeon usually makes good pigeon pie.

Little Walrus: Little Walrus’s mom told her to always tell the truth. One day the phone rang. Little Walrus was the only walrus home so she answered it: “Hello?” “Hello, Little Walrus” said Whale, “Is your mom home?” No, She’s out having the hair taken off her lip.

MORAL: You should always tell the truth. But if your mom is out having the hair taken off her lip you might want to forget a few of the details.

Straw and Matches: It was the end of summer vacation. Straw had done everything he could think of. He was bored. So he went over to play with someone he had been warned to stay away from. “Let’s play checkers,” said Straw. “Okay, I’m the red ones. I get to move first. I get two moves and you get one,” said Matches “Forget it,” said Straw. “Let’s play ping-pong instead.” “Okay. I get the good paddle. You stand on that side. I get to serve first, and you have to close one eye,” said Matches. “Never mind,” said Straw. “Maybe we should just watch TV.” “Okay. You sit over there on the floor. I’ll sit on the couch. I get the remote and we have to watch my favorite video,” said Matches. “I think I hear my mom calling,” said Straw. “I’d better go.”

MORAL: Don’t play with Matches

Elephant and Flea: As Elephant grew older, he also grew more responsible. One day he and Flea went to see a movie. They liked it so much that they saw it again and completely lost track of time. “Oh no” said Elephant, when he checked his watch. “I was supposed to be home ten minutes ago. Rhinoceros is going to be furious. Do you have a quarter so I can call?” Flea checked his pockets. “Nope. Spent all my money on popcorn.” So Elephant didn’t call. When Elephant finally showed up, at Rhinoceros’s house, he was twenty minutes late, and she was furious. “You could have at least called,” said Rhinoceros

MORAL: Elephants never forget, except sometimes.

Piece of Toast and Fruit Loops: Piece of toast and Fruit Loops sat on the breakfast table arguing over who was loved the most.

“Of course everyone loves toast the most. I’m half of eggs and toast. I’m all the toast in French toast. I am the toast with the most. Who could not love me?” Fruit loops said, “I’m a good source of 11 essential vitamins and mineral containing 20% of the minimum daily requirements of vitamin C, Iron, Thiamin, riboflavin, Niacin, Vitamin B6, folate, vitamin B 12 and Zinc, based on a 2,000 calorie a day diet and a 1 cup serving size not including milk. I also have 1 gram of dietary fiber per serving and 12 grams of sugar, yellow dye #6, blue #1 and #2 and red #40. BHT has been added to preserve freshness.” But while Fruit Loops was rattling off his nutrition facts… Mom had a cup of tea… “Toast… Toast… toast….” (getting cold) Dad drank coffee….. “Fruit loops…. Fruit loops…. Fruit loops…” (getting soggy) Son ate a doughnut “Toast…toast…toast” (getting colder)

Daughter said she’d get a bagel on the way to school. “Fruit loops…fruit loops… fruit loops…” (getting soggier)

MORAL: Breakfast is the most important meal of the day

Hand, Foot and Tongue: One evening at dinner, Hand, Foot and Tongue got into a heated argument over who had the toughest job. “I have the toughest job,” said Hand. “Every day I work from sunup to sundown. I button shirts. I tie shoes. I hold the spoon and fork to feed all of us. I have to be strong enough to punch with a fist, and gentle enough to pat a baby. I definitely have the toughest job.” “No you don’t,” said Foot. “I have the toughest job. Every day I have to carry all of you. And I’m not complaining or anything, but I usually have to do it in the dark – stuck in a smelly sock and laced in a shoe. I have the toughest job.” Then Tongue spoke up. “I am a fleshy muscular organ attached to the floor of the mouth. I help in both speech and taste. I start the process of digestion by moving food into position to get ripped and mashed and crushed and smashed to little bits by the teeth. Then I cover the little food bits with saliva and shape them into slimy blobs of guck that I push down the throat and . . . . “ “That’s sick,” said Hand. “Disgusting,” said Foot.

MORAL: There are some things we don’t talk about at the dinner table.

What fun! I should write some of those myself, you are probably thinking . . . But before you get started, it just occurred to me that you might want to know one more little bit about Aesop.

Aesop used to tell this one fable about a real bossy jerk “Lion” who ruled a city. When the real bossy jerk guy who ruled Aesop’s city heard his fable, he didn’t like it. So he had Aesop thrown off a cliff.

MORAL: If you are planning to write fables, don’t forget to change the people into animals and avoid places with high cliffs.
```

---

## IC-2129: Standard Loneliness Package

- Title: Standard Loneliness Package
- Author (byline): Charles Yu
- Work: Sorry Please Thank You: Stories, Pgs 3-34
- Publisher: Vintage
- Publication date as stated: May 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1757
- Already set (do not supply): none

### Source block (context only)

```text
Author: Charles Yu
Book: Sorry Please Thank You: Stories, Pgs 3-34
ISBN: 978-0307948465
Publisher: Vintage
Date (Month/Year): May 2013
```

### Introduction (context only: never use it for content warnings)

```text
Society hasn’t achieved this level of technological innovation. Not yet. But as musical artist Steven Wilson once said: We are living in dystopia, in a world that is dominated by technology and disconnect, alienation, loneliness and dysfunction. How much longer will it be before our AI assistant notices we are feeling a bit blue and suggests:

(chipper media commercial voice) Don’t feel like having a bad day? Let someone else have it for you!

Standard Loneliness Package by Charles Yu
```

### Performance text (classify this)

```text
NARRATOR: (Pg 3-34) Don’t feel like having a bad day? Let someone else have it for you. That’s a line from one of our commercials. It shows a rich executive sitting and rubbing his temples, making the TV face to communicate the stress of his situation. There are wavy lines on either side of his temples to indicate that the Executive is! really! stressed! Then he places a call to his broker, and in the next scene, the Executive is lying on a beach looking at the bluest ocean I have ever seen.

Root canal is one fifty, give or take, depending on who’s doing it to you. A migraine is two hundred. Death of a cousin is five hundred. Death of a sibling is twelve-fifty. Parents are two thousand a piece, but depending on the situation people will pay all kinds of money, for all kinds of reasons, for bad reasons, or for no reason at all.

Don’t feel like having a bad day? Let me have it for you— me and the other six hundred operators in building D, cubicle block 4. Not that I get the money. The company gets it. What I get is twelve dollars an hour, plus reimbursement for painkillers. Not that they work.

I feel pain for money. Other people’s pain. Physical, emotional, you name it. Pain is an illusion, I know, I know, I know. The shift manager never stops reminding us. Doesn’t help, actually. Doesn’t help when you are on your third broken leg of the day.

NARRATOR: I get to work late and already there are nine tickets in my inbox. I close my eyes, take a deep breath, open the first ticket of the day: I am at a funeral. I am feeling a mixture of things. Grief, mostly, but I also detect some guilt in there. There usually is. I hear crying. I am seeing crying, pretty, white faces. Nice clothes.

Our services aren’t cheap. So the faces are usually pretty, the clothes are usually nice. The people are usually nice, too. Although, I imagine it’s easy to be nice when you are rich and pretty. Even when you’re at a funeral.

There’s a place in Hyderabad that is doing what we’re doing, a little more towards the budget end of things. Precision Living Solutions, it’s called. And of course there are hundreds of emotional engineering firms in Bangalore. Springing up everywhere you look. I read in the paper that a new call center opens every three days.

Okay. Body is going into the ground now. The crying is getting more serious. Here it comes. The one that these people get a lot, near the end of a funeral service. These sad and pretty people. It’s a big feeling. It feels like a huge boot is stepping on my chest. It is hard to breathe. It doesn’t hurt, exactly. It’s not comfortable, but it’s not pain. More like pressure. Deepak, who used to be in the next cubicle, once told me that this feeling is actually the American experience of the Christian God.

I endure a few more minutes and then when the grief and guilt are almost too much and I wonder if I am going to have to hit the safety button, there it is. It’s usually there at the end of a funeral, no matter how awful, no matter how hard I am crying, no matter how much guilt my client has saved up for me to feel . . . You wouldn’t expect it -- I didn’t -- It seems unbelievable, but it’s almost always there, even if it’s just a glimmer. Relief.

Deep always tried to explain to me how it works: The clients, they call their account reps and book the time. And then at the appointed hour, a switch in their implant chip kicks on and starts transferring their consciousness over. Perceptions, sensory data, all of it. It gets downloaded onto our servers and then dumped into our queue, which parcels out the individual jobs to all of us in the cubicle farm.

It’s based on some kind of efficiency algorithm -- our historical performance, our current emotional load. Sensors in our head measure our stress levels to see what we can handle. They seem to have gotten it down to a science --How much a human being can take in a given twelve-hour shift. Grief, embarrassment, humiliation, all different, of course, so they calibrate our schedules, mix it up, the timing and the order, and the end result is you leave work every day at your exact breaking point. Sometimes when I get home, I’m still shaking. I sit on my couch and let it subside. ******

NARRATOR: Death of an aunt is seven hundred. Death of an uncle is six. Kid’s recital is one twenty-five an hour. Church is one-fifty. The only category that we will not quote a price on is death of a child. Death of a child is separately negotiated. Hardly anyone can afford it. And not all operators can handle it. We have to be specially trained to be eligible for those tickets. People go on sick leave, disability. Most people just physically cannot do it. There hasn’t been one booked the whole time I’ve been here. The rumor is that if you do one, you are allowed to take the rest of the month off. ******

NARRATOR: When I get to work the next morning, my first ticket of the day is a death bed. But this isn’t regular death bed. They are pulling the plug on grandpa this morning. I open the ticket. I am holding grandpa’s hand.

He squeezes my hand, one last burst of strength. It hurts. Then his hand goes limp and his arm falls away. I cry, and also, I really cry. Meaning, not just as my client, but I start crying, too. Sometimes it happens. I don’t know why, exactly. Maybe because he was somebody’s grandpa. And he looked like a nice one, a nice man. Maybe something about the way his arm fell against the guard rail on the hospital bed. Maybe because I could sort of tell, when grandpa was looking at his grandson for the last time, looking into his eyes, looking around in there trying to find him, he didn’t find him, he found me instead, and he knew what had happened, and he didn’t even look mad. Just hurt. ****** • I am in a dentist’s chair. • I am quitting my job. This is a popular one. Clients like to avoid the awkwardness of quitting, so they set an appointment, walk into their bosses’ offices and tell them where they can stick this effing job, and right before their boss starts to reply, the switch kicks in and I get yelled at. • I am losing someone to cancer.

NARRATOR: Eleven tickets, including a two-hour adultery confession. To my husband of twenty-six years.

I’m flipped to green. You can be flipped to green, or flipped to red. You can be there or can just feel the feeling.

This is the one improvement they have made that actually benefits us workers. There’s a toggle switch on the headset. Flip it to green and you get a rendering of the client’s visual field. You see what he sees. Flip it to red and you still feel all of the feelings, but you see what you see.

You can do whatever you want, so long as you don’t leave your cubicle. You can just stare at the cube-divider wall, or play computer solitaire, or even chat with neighbors, although that is strongly discouraged. I was hesitant at first, but more and more these days I am usually flipped to red. Except for funerals. Funerals, I like to be there, out of some kind of respect. ******

NARRATOR: I am in a hospice. I have been here before. A regular client. My husband is gone. He died years ago. Today is the tenth anniversary of his death. I have Alzheimer’s, I think. I am holding a pen. I have just written something on a notepad in front of me. I tear off the sheet -- read it to myself. It is a suicide note. A memory of my husband surfaces, like a white-hot August afternoon, resurfacing in the cool water of November. I raise a glass to my mouth, swallow a pill. Catch a glance of my note to the world. The failsafe kicks on, just in time. The system overrides. I close the ticket. • I am at a funeral. • I am in drug rehabilitation. • I am in surgery. • I am bleeding to death. It doesn’t hurt at all. I go home. I rest. I come back and do it again. ******

NARRATOR: When Deep was happy, before it got bad and then worse and then even worse, he loved telling stories. About a week before he cracked up, he told me a story about a guy at Managed Life Solutions, a physical suffering shop across town, who somehow made arrangements with a prominent banker who wanted to kill his wife. The banker was going to do it, but he didn’t want the guilt. Plus, he thought it might help with his alibi if he didn’t have any memory.

Could never happen, I say. There are twenty reasons why that wouldn’t work. It’s just too much.

Too much what? There is no upper bound on cruelty, he said.

The next Monday, I came to work, and they were pulling Deep out the door -- two paramedics, each one with an arm under Deep’s arms, and two security guards trailing behind. I wanted to say something, anything, to make them stop. I knew I would never see him again. But I froze. As they dragged him past me, I tried to make eye contact, but I looked in there, and no one was left.

And then the next day, there it was, in the newspaper. The whole story about the banker. Exactly how Deepak told it to me. There were rumors that he was the one the banker hired; he was living with murderous guilt. Other people gossiped that he had done the death of a child.

I don’t think it was either. I don’t think it was any one thing that did it. There is no upper bound on sadness. There is no lower bound on decency. Deep saw it, he understood it, what was out there, and he let it seep in, and once it was in, it got all the way in, and it will never come out.
```

---

## IC-2130: The Stinky Cheese Man & Other Fairly Stupid Tales

- Title: The Stinky Cheese Man & Other Fairly Stupid Tales
- Author (byline): Jon Scieska
- Work: Not specified
- Publisher: Viking Press
- Publication date as stated: May 2002
- Event as filed: Prose
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

JACK THE NARRATOR: That’s your story? You’ve got to be kidding. That’s not a Fairly Stupid Tale. That’s an Incredibly Stupid Tale. That’s an Unbelievably Stupid Tale. That is the Most Stupid Tale I Ever – awwwwk!”

(Giant grabs Jack; holds him tight in one fist . . . Jack hesitantly begins to tell his story) Once upon a time there was a Giant.

GIANT: (squeezing Jack tightly) TELL ME A BETTER STORY OR I WILL GRIND YOUR BONES TO MAKE MY BREAD. AND WHEN YOUR STORY IS FINISHED, I WILL GRIND YOUR BONES TO MAKE MY BREAD ANYWAY! (an ugly laugh)

JACK THE NARRATOR: (thinking aloud to audience) He’ll kill me if I do. He’ll kill me if I don’t. There’s only one way to get out of this. . . (clears his throat and beings the story) Once upon a time there was a Giant.

GIANT: (squeezing Jack tightly) TELL ME A BETTER STORY OR I WILL GRIND YOUR BONES TO MAKE MY BREAD. AND WHEN YOUR STORY IS FINISHED, I WILL GRIND YOUR BONES TO MAKE MY BREAD ANYWAY! (an ugly laugh)

JACK THE NARRATOR: (thinking aloud to audience) He’ll kill me if I do. He’ll kill me if I don’t. There’s only one way to get out of this. . . (clears his throat and beings the story) Once upon a time there was a Giant.

GIANT: (squeezing Jack tightly) TELL ME A BETTER STORY OR I WILL GRIND YOUR BONES TO MAKE MY BREAD. AND WHEN YOUR STORY IS FINISHED, I WILL GRIND YOUR BONES TO MAKE MY BREAD ANYWAY! (an ugly laugh)

JACK THE NARRATOR: (thinking aloud to audience) He’ll kill me if I do. He’ll kill me if I don’t. There’s only one way to get out of this. . . (clears his throat and beings the story) Once upon a time there was a Giant. . .

(sing softly and fade out to silence) This is the story that doesn’t end . . . it just goes on and on my friends . . . Some people started *listening* not knowing what it was and they’ll continue *listening* forever just because . . . ] The End
```

---

## IC-2131: The Stinky Princess

- Title: The Stinky Princess
- Author (byline): Bruce Coville
- Work: Odder Than Ever
- Publisher: HMH Books for Young Readers
- Publication date as stated: Oct 2000
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1854
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bruce Coville
Book: Odder Than Ever
ISBN: 978-0152024659
Publisher: HMH Books for Young Readers
Date (Month/Year): Oct 2000
```

### Introduction (context only: never use it for content warnings)

```text
Have you ever felt like you just don't quite fit in? Have you ever been told you’re too much of this or not enough of that? There isn’t a single person on the planet that hasn’t felt judged by others at some point in their lives.

Are we good enough, smart enough, pretty enough, skinny enough? Bruce Coville, in his children’s story “The Stinky Princess,” addresses the issues of being judged and self-acceptance.

But it’s not just a children’s story . . . there’s a moral to his story teens and adults need to hear too!
```

### Performance text (classify this)

```text
ONCE THERE WAS a princess named Violet who didn't smell very good.

It had nothing to do with either her birth or her upbringing. In fact, she had started out smelling just fine. She smelled of clear mountain streams a moment before the rain comes, and of lilacs.

Violet found her own smell boring, and often declared that there must be many far more interesting scents in the world . . . .

[And then] Bindlepod the goblin came to visit. Bindlepod's skin was the color of rotting toadstools. His bare feet slapped on the stone floors of the castle like dirty dishrags. But the most distressing thing about him was his smell.

While nobody could say exactly what it was Bindlepod smelled of, everybody agreed that it was distinctly unpleasant. Everybody, that is, except the princess. She thought Bindlepod smelled quite interesting.

One day, the princess was walking in the castle garden when she spotted Bindlepod's frog. It was wearing its saddle, as if Bindlepod had just re-turned from a ride. A little farther on she spotted the goblin himself. He was perched on the stone wall, gnawing a raw fish.

Violet climbed onto the wall and took a seat next to Bindlepod. "What's it like in Goblinland?" she asked.

Bindlepod shrugged. "Nice enough, if you're a goblin. We call it Nilbog, by the way, not Goblinland. That's rude. It would be like calling your kingdom Peopleland. "

"Is Nilbog smelly?"

Bindlepod closed his eyes and seemed to be remembering something. "Yes," he said at last, with just a hint of a smile. "Very."

"Let's go there," said the princess.

"You," said the goblin, "are walking trouble, a danger zone with feet."

"Does that mean no?" asked Violet.

"It means never in a million years!" Then he hopped down from the wall and whistled for his frog [for his trip home]. Late in the morning, Bindlepod's frog stopped in the middle of the road and said, "I am not taking another hop until you get that princess out of the saddlebag."

"What are you talking about?" cried Bindlepod in alarm.

"The princess," said the frog patiently. "She's in the saddlebag, and I'm getting tired of carrying her."

"Why didn't you say something before now?" asked Bindlepod, torn between exasperation and despair.

"She bribed me," said the frog. "With june bugs. You know I can't resist june bugs."

The shape of the saddlebag was distinctly suspicious. So Bindlepod unstrapped it from the frog, loosened the top, and turned it over. Out tumbled the princess.

Bindlepod sighed. "What are you doing here?"

"Going to Nilbog," said Princess Violet, picking herself up from the road and brushing the dust from her backside.

"You most certainly are not," said Bindlepod.

"Well, if it's not Nilbog, it will be somewhere else," she said. "I'm not going back, and you can't make me."

"She's got a point," put in the frog. "Even if you took her back, they probably wouldn't let her in on account of ... well, you know."

"I know," said Bindlepod. "The smell. You've been in my saddlebag for three hours already. Your parents may have put up with goblin smell on me, but they certainly aren't going to accept it on their daughter."

"Well, I'll just wash," said Princess Violet indignantly.

"Goblin smell doesn't come off with mere soap and water," said Bindlepod.

"What does it take?" asked the princess, indignation turning to alarm.

"A dip in Fire Lake, if I remember correctly," said the frog.

"Good grief!" cried Bindlepod. "We can't expect her to do that! There's no telling how she might come out. We're turning back. Even if the princess's parents don't let her in, we have to let them know what's happened. If we don't, they're going to assume I stole her, and before you know it we'll be at war.”

They had traveled only about a third of the way back to the castle when they found the king coming in their direction.

"Hail, King Vitril!" said Bindlepod. "I have your daughter," gesturing to where Violet was perched atop the frog. "I was just bringing her home."

Violet raced to her father's side. But when the king dismounted to embrace her, he made a terrible face. "Euuuw!" he cried. "You stink of goblin!" And, indeed, the princess-who had once smelled of apple blossoms and spiced muffins-now had a distinctly strange odor about her. The king looked at his daughter sadly. "I can't take you home like this. What do you think your mother would say if she got a whiff of you now? The smell would break her heart." He turned toward Bindlepod. "As she chose to go with you, I leave her to you." With that he bade his daughter farewell then climbed onto his horse and rode for home.

The astonished princess stood in the road, blinking back tears as she watched her father gallop away. It is, after all, one thing to run away from home. It is another thing entirely to run away and discover that they don't want you back. She sighed and turned her face toward Nilbog.

Narrow stone bridges took them across dark chasms. Winding passages with many tunnels branching to the sides carried them deeper into the earth. And at last they arrived at the entrance to Nilbog.

An enormously fat creature who looked something like a goblin, though not entirely, was leaning against one side of the entrance, cleaning his navel with a sharpened bone. When he saw them coming, he opened his yellow eyes a little wider but made no movement.

"Come here . . . Not you, Princess! Just Bindle-pod." Bending forward-not easy, given his enormous bulk-he began to sniff. Sniff. Sniff sniff. He frowned in disgust. "Whooie!" he cried. "You stink, Bindlepod! You smell of quiet rooms and cramped hearts, tiny minds and tiny places. You smell small and nasty."

Hearing this, the princess grew nervous. "Does that mean he's not going to let us in?" she whispered to the frog in a quivering voice.

"If I sent you away, then I would have a tiny little mind, too, wouldn't I? You may enter. Just don't be surprised if people are not particularly happy to smell you."

Their reception at the court of the goblin king was no more encouraging than Violet's last interview with her father had been. The goblin king - a huge creature with leering eyes, fantastical warts in several colors, and a tongue as long as his arm - was sympathetic, but disturbed. "I am glad to have you back, Bindlepod," he said. "And your young lady friend is welcome to stay as well, of course. But really ... " With that, his voice trailed off, and his eyes rolled around, as if he was searching for exactly the right word.

The goblin queen, looked up and said, "Your father is troubled, son, on account of the princess's smell."

"Son?" asked Violet in surprise. "You didn't tell me you were the prince of Nilbog!" Bindlepod shrugged. "And what's wrong with my smell, anyway?" continued Violet indignantly.

"You do smell of goblin," said the king wearily. "But you also smell of the world above. We will give you shelter, of course. But I fear my people will not be jolly in your presence."

Time proved the king to be correct. Though everyone in Nilbog was polite to Violet and Bindlepod, no one seemed terribly comfortable in the presence of either of them. The result was that Violet and Bindlepod spent more and more time alone together. Bindlepod and Violet fell in love.

"I can't say we were made for each other," said Bindlepod. "Even so," he continued, "I am glad we found each other."

"And why weren't we made for each other?" she asked, reaching up to pat his sallow cheek.

"Well, my stinky little sweetie, our smells are, to say the least, incompatible."

As the weeks wore on, Violet began to realize that Bindlepod was right. Though they were utterly happy in each other's company, the other goblins were most uneasy with their relationship. She decided to seek help and learned the whereabouts of the wisest of goblins, an incredibly ugly female of astonishing age. Her name was Flegmire, and she lived in a cave at the edge of Nilbog.

Standing at the front of the cave, Violet called, "May I enter, o Wisest of the Wise?"

"Yeah, yeah, come on in," replied a gravelly voice. Flegmire sat on the floor playing with a col-lection of colored rocks. The ancient gobliness held up her hands, cried, "Wait! Wait!" and then farted with such violence that it raised her several inches off the floor.

The smell caused Violet to gasp in shock. Flegmire, however, sighed in contentment and said, "Well, now that I can think again, tell me what it is you want."

Eyes watering, the princess explained her difficulty.

Flegmire hooked a curved green fingernail over her enormous lower lip. "You can't think of anything yourself? No hints you've had along the way?"

She swallowed nervously. "Well, Bindlepod's frog did mention something about ... Fire Lake."

Flegmire spread her arms as if the whole thing had been the essence of simplicity. "Well, there you go! If you already knew about that, why did you come here to bother me?”

That night Violet put on her riding clothes, then slipped out the door, intending to saddle up the frog and ride to Fire Lake. But she hadn't gone more than ten paces from her door when Bindlepod stepped from behind an enormous mushroom and said, "Going somewhere, my darling?"

Violet jumped and gasped. "What are you doing here?" she cried.

If you are going to do this thing, then so am I,” said Bindlepod. "There's no point in only one of us taking the risk. If we're going to change, we might as well change together."

In a few hours they were standing at the edge of Fire Lake. The blazing waves hissed and crackled as they rolled against the shore. Bindlepod took Violet in his arms. He held her close, burying his nose in her neck.

"You know," he murmured, "I like the way you smell."

"And I like the way you smell," she replied.

"Then what are you going to do this for?" cried the frog. "Are you out of your minds? What do you care what the others think? It's none of their business! You love each other the way you are. Who are you going to change for?"

*********

Princess Violet and Prince Bindlepod never did step into Fire Lake. What they did do was build a home for themselves in a giant oak tree halfway between the gates of her father's kingdom and the entrance to Nilbog. Part of the home was in the branches, and part beneath the roots. It smelled of sky and leaves, of stone and soil, and they loved it nearly as much as they loved each other.

Though they never went back to either kingdom, their home was always open to anyone who cared to visit, and who would take them as they were.
```

---

## IC-2132: A Story About a Bomb

- Title: A Story About a Bomb
- Author (byline): Jonathan Tel
- Work: Arafat's Elephant: Stories
- Publisher: Counterpoint
- Publication date as stated: Feb 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1840
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jonathan Tel
Book: Arafat's Elephant: Stories
ISBN: 978-1582431833
Publisher: Counterpoint
Date (Month/Year): Feb 2002
```

### Introduction (context only: never use it for content warnings)

```text
A story about a bomb is not a bomb. However artfully constructed the plot, however incendiary the theme, although the topic may be volatile and the implications explosive, however dangerous the sentiments may be – a story will not in fact abolish itself in a blinding flash, scattering shrapnel within a radius of forty meters and shredding passersby. Despite our best efforts. A Story About a Bomb by Jonathan Tel
```

### Performance text (classify this)

```text
Several years ago I browsed through an anthology of Palestinian literature. There was one story that struck me as remarkable at the time; and that has stayed with me since, burning in my memory. Its title was The Red Button.

It concerned a Hamas terrorist (or freedom fighter, if you prefer) who was on the point of blowing himself up, along with as many Israelis as possible. He was shifting from leg to leg in Jerusalem, near where the new city meets the old, across from Jaffa Gate, on the wrong side of the highway.

It was eight o’clock in the morning on the hottest Friday in August. He had come from a refugee camp in Gaza, and had spent the previous night praying with some comrades near Bethlehem. He had just been dropped off by Toyota. He was wearing a long padded overcoat, buttoned up, to conceal the bands of dynamite around his abdomen. He was sweating and shivering. His instructions were to cross the road (looking carefully to right and to left first; it wouldn’t do to be knocked down by a speeding vehicle before he had a chance to press the button on the detonator) to the bus stop on the far side. With any luck, there would e many Israelis waiting there. He would simply have to stand among them, mutter Allahu Akbar, and the next thing he knew he would be marching into Paradise, a pair of dark-eyed houris eager to kiss his bleeding wounds. In reality, of course, it was not as simple as all that.

Every bone in his body ached. (He had had to crouch on the back floor of the Toyota, concealed under a carpet, for what had seemed like generations.) He smelled his own sweat. The bus stop in question was within view. He could see would-be passengers waiting there, more or less patiently. Women, children, old men, also about ten soldiers, perhaps on weekend leave. The ideal target. Yet he had to wait. The traffic was atrocious. He stepped into the road – and a great red Coca Cola truck went roaring past. A Subaru blurted its horn at him. A police car swept by. He hobbled back to the safety of the curb. Finally the road was empty. On the far side, a Number 23 was halted at the stop . . . By the time he arrived there, the bus had departed, taking all the Israelis with it. If he reached into his pocket and jabbed down on the button now, he would explode nobody but himself. He could have wept with frustration.

He kept the vision of Paradise clear in front of him. As it is written: “ . . . that Allah may know those who believe, and take martyrs from among you . . . “ Two houris would come dancing toward him. They would cloak him in the precious hulla robe. They would say, “May Allah put dust on the face of those who put dust on your face!” . . . An acrid aroma; a clammy feeling around the groin. He had got beyond the trembling stage. He was on an exalted level of anguish. Now the twitching was intense, as if he were being banged like a saltcellar on a humid day.

Now at last the future seemed revealed. Now a fresh selection of Israelis had appeared at the stop. Now there was a hiatus in the traffic – no vehicles to delay him, no bus to carry away his victims. And then, just as he was about to scurry across the expanse of asphalt, to leap forward into his destiny, to switch on the detonator . . .

A middle-aged couple approached the terrorist. They stood beside the curb, blocking his way. The man had thin sandy hair whirled over a bald spot. He was wearing baggy green shorts. An oversize map was sprouting from his shirt pocket. He was waving his yellow Holyland Tours baseball cap to attract the terrorist’s attention. The woman, blonde, had on an identical cap; she was also in shorts, blue ones, matching her varicose veins. The two of them were addressing him in what he reasonably believed to be English

Since he evidently did not understand, the tourists resorted to sign language. The man was holding up a camera – it was suspended from a strap around his neck – he was hoisting it free. The woman was pointing to it. Much dumbshow ensured, involving grasping and lifting the Olympus, gesturing at elements of it (automatic focus; you just have to aim the thing and shoot), peering through the viewfinder, and going cheese . . . (And all the while, Hativat Yerushalayim remaind free of traffic, the ignorant Israelis were unmoving – how simple and easy to blow them and himself up, the exemplary conclusion – if only those damn foreigners would just get out of his way!)

But what could he do? If he tried to escape from them, let alone grapple with them, he would only draw attention to himself. The Israelis would just run off, or one of them might draw a gun and kill him before he’d be able to complete his mission. No, the only hope was to go through with what the foreigners wanted, and then they would leave him in peace.

The tourists posed on the curbside. The husband put his arm around his wife’s shoulder. They smiled as if they were genuinely happy. As if purely to be in Jerusalem was to be blessed. The terrorist stepped back, arranging their faces within the rectangle of the viewfinder. He motioned the couple with his left hand, to lean their heads closer together; to step a little this way – so he could catch them with Jaffa Gate behind, for extra picturesqueness . . . Somehow, miraculously, as he squinted through the viewfinder, all his quavering and uncertainties had ceased. He was aware of nothing except this instant. As for the tourists, they would look at the snapshot and remember their trip to the Holy Land for the rest of their lives . . . Ah, perfect now. The tip of an index finger pressed down on a red button – and the story ended.

Of course my summary of the story doesn’t capture the magic of the original. How could it? The author, Ahmed Fishawi took great pains to bring us inside the mind and body of the central character. What exactly was the author, this Mr. Fishawi, trying to say? Was he drawing an analogy between terrorist and tourist? Furthermore, as the years have gone by, I have come to wonder: Perhaps the author was too good a writer. He has taken us too much inside the mind of a terrorist. If we are brought to – more than understand – to sympathize with the terrorist, then are we not, in some sense, colluding with him?

The other day I was at a party in Tel Aviv. As usual in Israel, the guests were arguing about politics. I did yearn for meatier conversation . . . . [when] I noticed a man standing by himself to one side, saying nothing. I introduced myself. “What do you think of all this? I asked him.

“What do they know? The only Arabs they ever see are the guys who pick up their garbage. Believe you me, 99% of the Palestinians support Hamas – whether they admit it or not. The only way we’ll have peace is if the Arabs know there’s a gun pointing at their head.”

“That’s an interesting point of view,” An then, I alluded to The Red Button.

“I know that piece. Yes, I . . . I know it very well. As a matter of fact – I am Ahmed Fishawi. And by the way, don’t keep calling it ‘fiction’. Fiction schmiction! The Red Button is true, every word of it. The events describe took place on the morning of August 8th 1999. I know because I was there. Do you want to know what actually happened? I was there. I was leaning against a lamppost. On the other side of the terrorist, a couple of lovers were kissing . . . So the terrorist pressed the red button on the camera . . . At that moment – when we knew for sure he wouldn’t have a free hand to operate the detonator – I came running up from behind and I slammed into his back. The ‘lovers’ seized his arms between them. And the male ‘tourist’ put on the handcuffs while the female ‘tourist’ kicked him. I’m in counter-terrorism – Shimshon Unit. Have you heard of us? We’d been following the poor *guy* ever since he left Gaza. We eliminated his entire cell. I almost killed myself! And everybody else too! See, when I ran into him, somehow the detonator started up. By a miracle it didn’t set the bomb off. So all that happened was that the *terrorist* got third degree burns on his belly and I screwed up my arm.”

He rolled up his right sleeve. Just above the wrist, a patch of skin was distorted, thickly ridged—as if the flesh had melted like wax and refrozen.

“So then we took him back to HQ. We put him in the medical unit for a while – Intensive Care – until we knew he wasn’t going to die on us, and he was out of pain. Then we could torture him. Don’t look so shocked. We call it torture but it’s not what you think of as torture; it’s the gentle art of persuasion. We use the official methods—making him sit in one position for hours, in a child-size chair – shaking him till he rattles. It’s toughies like me who stop the Arabs from blowing up the kindergartens! Of course we didn’t have to torture him, hardly at all. Not in his case. He knew he’d be spending years in an Israeli prison, instead of partying with houris in Paradise. He didn’t want to be alive. We stood beside the hospital bed, and we shouted at him. SO he told us the names and addresses. Everything we wanted to know. Who his commander was, the location of his safe house. And then we locked him up, and that was the end of that.

“I think you underestimate yourself,” I said. “you say you’re not a fiction writer – and maybe the outline of your story is based on truth – but how on earth did you get inside the man’s head? Those interior monologues. I can’t believe this is your first story!”

“I asked the *guy* to help me. That’s how I know. Not too bad a fellow, the terrorist, once you get to be friends with him. I played the nice guy. I said, if you tell me every little thing that went through your head, I’ll let you read the Quran, and I’ll give you the cutest little prayer mat to keep you company . . . And then when he’d told me everything he could think of, I used the other method to job his memory.”

“What other method?” I said.

I literally felt the hairs stand up on my neck – a sensation I’d only ever read about in books, that I’d always supposed to be fictional.

“The usual. What a man like you would call background research. I wend town to his cell and I tied a blanket soaked in *urine* over his head. Then I patted him in the kidneys with the butt of my rifle . . . It took 72 hours before he broke. He answered all my questions. I don’t need to tell you what he said. Every little detail, and more besides. His childhood. His grandmother. His uncle. His religious beliefs. What he felt and what he smelled. And it was worth it. A chance in a lifetime. The Red Button’s a great story. You told me so yourself. . . “
```

---

## IC-2133: Summer Reading is Killing Me

- Title: Summer Reading is Killing Me
- Author (byline): Jon Scieszka
- Work: Not specified
- Publisher: June 2000
- Publication date as stated: Puffin Books
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: FRED, SAM, JOE, RED QUEEN, DEVIL, FRANKENSTEIN, THE DEVIL, TEDDY, ANNA, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1567
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jon Scieszka
ISBN: 978-0141308203
Publisher: June 2000
Date (Month/Year): Puffin Books
```

### Introduction (context only: never use it for content warnings)

```text
Summer Reading is Killing Me by Jon Scieszka
```

### Performance text (classify this)

```text
(Pg 6-7) This is going to be impossible to explain. But I think I know what happened. My life has not been the same since my uncle Joe gave me THE BOOK -- a book like no book I’ve ever read before or since. It’s a time-warping book. I know. I know. You’re saying to yourself . . . . “What’s with this guy? He probably still believes in the Easter Bunny and the Tooth Fairy.” I didn’t really believe it myself. Then Sam and Fred and I opened THE BOOK. We have been chased by a woolly mammoth, turned into mummies and nearly suffocated by one very nasty-smelling giant. (Beat) And once we go to another time, the only way to get back to our time is to find THE BOOK in that time . . . So anyway, there we were – sitting in my room the very first day of summer vacation . . . We were trying to be careful. We really were!

FRED: (Pg 8-9) No more classes, no more books. No more teachers’ dirty looks!

SAM: (pointing to a book on the bookshelf) Can we please promise not to open THE BOOK and get sucked into some time-travel trouble like we always do?

FRED: I’m with you. We don’t have to open any books!

SAM: Well, now that you mention books . . . I was thinking we might get an early start on this list.

FRED: Summer reading list? Are you crazy. This is vacation.

SAM: (Reading aloud from the list) Each student must read four books during the summer and fill out the attached study guide for two of them. The list has Hatchet, The Phantom Tollbooth, The Hoboken Chicken Emergency . . .

(Pg 10-12) Fred did a half-twist flip off the bed and took Sam’s list. He stuck it in a book from my shelf, shoved the book back and jumped back onto the bed.

JOE: (stares, aghast at the bookshelf) Forget it you guys! You don’t have to decide!

SAM: What do you mean we don’t have to decide?

JOE: (pointing to the bookshelf) We have about three seconds before this green mist leaking off my bookshelf decides for us! All three of us stared at the wisps of green mist swirling out of the thin blue book with silver designs.

FRED: Aww no . . . How did that happen? I didn’t do nothing.

SAM: Anything. You didn’t do anything except put our summer reading list inside THE BOOK! Then the familiar green mist washed over us. And we were flung through time and space to who knows when or where. *****

FRED: (Pg 16) (looking around cautiously) We can’t be in a book. That only happens in movies. There is no way I am going to spend my summer vacation in a book.

SAM: This is very weird, but quite possibly true. What if story characters are real? What if they have a life we just don’t know about.

JOE: (Pg 20-21) Oh no . . We are in huge trouble. If this means what I think it means, all of the characters from every book on the summer reading list are mixed up here. And none of them are in their books where they’re supposed to be. The librarian is going to kill us.

SAM: What if the Red Queen says, “Off with Ramona’s head!?”

JOE: What if the Twits mess up Wayside School?

SAM: What if the Tripods take over the Little House on the Prairie? We have to get everyone back in the right book!

JOE: (Pg 22-23) We have to get back THE BOOK and take the summer reading list out of it before anything happens! . . . . THE LIBRARY!

(Pg 25-27) We took off. We passed old houses, an alley, a street lined with shops and in just a few minutes we were at the corner of the park. Just then we heard a wild yelling and the sound of stomping footsteps behind us. Dracula was dragging Winnie-the Pooh in a headlock. Mr. Twit was breaking Harold’s purple crayon. Twenty different bad guys from twenty different books were chasing, hauling and pushing all kinds of characters up the steps of a big old brick building.

FRED: (Pg 28) (Reading the sign on the building) Hoboken Public Library!

SAM: The one building in Hoboken that we need to get into is packed with every bad guy from every book ever written! (The boys sneak into the library) (Pg 33) (in a whisper) I see it, but I don’t believe it. That’s Mrs. Twit tying up Marry Poppins and Encyclopedia Brown.

JOE: That’s Frankenstein holding Pippi Longstocking

FRED: They even got Mother Goose.

RED QUEEN: (Pg 34-35) Off with their heads!

CHARACTER FROM LORD OF THE FLIES: Kill the pig! Cut his throat! Bash him in!

JOE: I don’t know what’s going on here, but it doesn’t look good. Let’s sneak up those stairs and start looking for THE BOOK – quick! And it probably would have been a good plan. But we were only halfway up the stairs when we heard a voice that could only be talking to us . . .

DEVIL: You three boys. What book are you from? Come here now!

FRED: Is that who I think it is?

JOE: Do you know any other red guy with two horns and a pointed tail? (to the Devil) (Pg 38) We’re the Time Warp Trio!

DEVIL: (Looking at his list) I have no Time Warp Trio!

RED QUEEN: (Pg 38) Off with their heads!

SAM: We’re probably not under Time Warp Trio because we’re actually a series . . .

FRANKENSTEIN: (Groaning and making a move toward them) Series . . . bad!

THE DEVIL: (Pg 39-40) (Stroking his beard) Maybe you can make this easier on all of us. What we are doing here is separating the good characters from the bad characters. The bad characters stay here and take over any story they like . . . And the good characters go there . . . to be crushed by those huge stacks of books and wiped out of stories forever! So . . . are you good characters . . . or bad characters? (Pg 42-43) Then the door with LIBRARIAN written on the glass slammed open with a bang.

TEDDY: What is going on out here?!

FRED: A . . . . a . . . teddy bear?

TEDDY: (Pg 44) That’s Mr. Bear to you, kid! (The boys try to hold in their laughter) This is exactly what I’m talking about. Just because I’m a teddy bear, I get no respect. Everyone thinks I’m soft and huggable and stupid! What exactly is the holdup here? Why isn’t everyone being crushed?

DEVIL: (Pg 45-50) We were . . .uh . . I was just . . . checking in these three characters.

TEDDY: Characters? Hah! They aren’t characters from a book. These are three kids. In fact, they are just the kind of readers I get no respect from – wise-guy boys! Throw them in the crusher now!

(Frankenstein lumbers to do his bidding)

JOE: (Screaming) Now just one minute! Look, Mr. Teddy – I mean Mr. Bear. It is true that we are not the biggest fan of teddy bear books . . . but crushing all of the good characters from every other book is not going to solve anything. (trying to sound very adult and reasonable) Just look how dumb these books sound without their main characters.

SAM: There are giant holes in every story. (he picks up a book and reads) “Run run run as fast as you can. You can’t catch me, I’m the blankety blank?”

JOE: (grabbing another book) The Hoboken Chicken Emergency is just The Emergency

FRED: (picking up a third book) Sylvester and the Magic Pebble is And the Magic Pebble.

TEDDY: Aww, that is so sweet. You are worried about all the poor little books. Well, don’t worry. The new titles of those books will be The Teddy Bear Emergency, Teddy Bear and the Magic Pebble and The Teddy Bear Man! (Raises his arms and laughing a crazy villain laugh at the ceiling) Frankenstein in Wonderland . . . Green Eggs and Dracula.

FRANKENSTEIN AND THE RED QUEEN: (Cheering) Ted-dy! Ted-dy! Ted-dy!

TEDDY: (Pg 58-59) Crush those boys now!

FRED: We’ll never make it to the door. Quick. Up these stairs! We charged up the steps two at a time. Captain Ahab, the Devil and a red-golden dragon climbed after us. We reached the top landing, blocked by the stack of books that had been meant to crush us.

JOE: (To the boys) Get back here and push! (They give a massive shove.

SAM: (Pg 60-61) Nice shot!

TEDDY: You are making me angry! We couldn’t hold out for much longer. I looked around for a way to escape. Stairs blocked. Window too high to reach. That’s when I saw our salvation! A thin blue book covered with silver stars and moons. A folded list stuck out of the middle. THE BOOK!

TEDDY: (Pg 62-64) I will squash you! I will flatten you like the bugs you are! No one ruins my plans. I will be the most famous character in every story!

FRED: Give me some cover . . . Fred jumped the handrail and slid down, launched a perfect flip over the Devil’s horns and rocketed up toward THE BOOK. Now I don’t know if everything really slowed down like it always does in those kung-fu movies. But it sure looked like it to me. Fred bobbled THE BOOK, pulled the summer reading list out and then fell into a pileup of Teddy Bear, Devil, and the Red Queen. We thought Fred was history. Then I saw the wisp of pale green smoke rising from the pile of characters. A whirling tornado of pale green mist sucked up every character and book inside and outside the Hoboken Public Library . . . and we were gone. (Pg 65) Fred landed on top of my desk, surrounded by the pileup of books that had been blown off my shelves. In one hand he held THE BOOK. IN the other hand he held the summer reading list. I looked at the pile of books and had a terrible thought. Fred and I attacked the books, flipping through all of them looking for . . .

JOE: Here’s the Hoboken Chicken. She made it back into her book.

FRED: The Twits are both here

JOE: (Pg 67-69) Mary Poppins, Charlotte, Frog and Toad – everybody’s back! (the boys laugh in relief)

ANNA: Ahem! (the boys freeze) Ahem! It was my little sister Anna, standing in the doorway.

ANNA: I don’t really want to know what you are doing. I just wanted to ask you if you have any ribbon I can use for my . . .

Anna held out her stuffed toy. And before the words “teddy Bear” were even out of her mouth, the three of us dove into my closet

TOGETHER: (Cowering in fear) NOoooooooo!
```

---

## IC-2134: Sweet Tooth

- Title: Sweet Tooth
- Author (byline): Margi Palatini
- Work: Not specified
- Publisher: Simon and Schuster
- Publication date as stated: Aug 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: SWEET TOOTH, STEWART, MOTHER, DAD, GRANDMOTHER, STUART, MRS. FINNEGAN, NARRATOR, CROWD, MOTHER/DAD, SISTER, UMPIRE, BABY TEETH, CANINE TOOTH, WISDOM TOOTH, TOOTH FAIRY
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
This is Stewart. Your typical, average, everyday kid. Except for one thing.

SWEET TOOTH: Iii oo-er ere. Ahh, yes. There it is all right. The molar in the back. You're probably saying, "A tooth? What's the big deal about a tooth?" And ordinarily you would be correct. . . . But that is no ordinary tooth. Uh-uh. This is Stewart's sweet tooth. One nagging, annoying, demanding . . .

SWEET TOOTH: (Loudly) BLAH. BLAH. BLAH.
ENOUGH WITH THE YAKKIN'. I NEED A
CANDY BAR. NOW-OW!
. . . very loud, sweet tooth.

SWEET TOOTH: "DOES IT HAVE THAT GOOEY STUFF IN THE MIDDLE? 'CAUSE IT'S GOT TO HAVE THAT GOOEY STUFF IN THE MID-DLE!"

STEWART: (Cramming a candy bar into his mouth, chewing loudly and gulping) There. Satisfied?

SWEET TOOTH: AHHHHH . . . SWEET! Yes, a tooth that wants what it wants, when it wants it . . . and lets everybody know it. Take, for example, two years ago at cousin Charlotte's wedding . . . Stewart was on his best behavior. His shoes were shined. Bowtie straight. Hands were spotless. Grandfather had just lifted his glass to toast the bride and groom when . . .

SWEET TOOTH: I'm fallin' asleep here! Come on. Move it along, Gramps. Cut the cake. Time to cut the cake. I want the end hunk with all that iiiiii-icing.

MOTHER: (through a gritted smile) I don't know him.

DAD: (under his breath) He doesn't belong to me.

GRANDMOTHER: (muttering) Who is that boy? Stewart wiped the pink rose from his lips.

STUART: It's The Sweet Tooth. It was not a pretty picture . . . The Tooth was no better behaved in school. Stewart had enough detention slips to wallpaper his room. Why, just two weeks ago in geography class . . .

MRS. FINNEGAN: Who can tell me the capital of North Dakota?”

SWEET TOOTH: (muffled) Jelly beans

NARRATOR: said a muffled voice from the back of the room.

MRS. FINNEGAN: Did you say something, Stewart?

SWEET TOOTH: Licorice.

MRS. FINNEGAN: Stewart, I'm afraid I can't hear your answer.

SWEET TOOTH: Lollipops.

MRS. FINNEGAN: You're going to have to speak up, Stewart.

SWEET TOOTH: Hey! I'm dying here for a couple of CHOCOLATE PEANUT BUTIER CUPS, OKAY?!

Detention slip number 432.

STEWART: (as he is lead away to the principal’s office) But, I'm telling you, it's not me, It's The Tooth! ******************* The movies? You don't really want to go there, do you? . . . Not with Stewart, anyway.

SWEET TOOTH: Would somebody pass the yummy yummys, already?!

CROWD: SHHHHHHHHHHHHH!

STEWART: (chewing) Don't look at me . . . It's The Tooth. And of course there was the unforgettable "Easter Basket Mishap." Now that was really ugly. That Sunday A.M. the family awoke to find jelly beans littering the living room. Marshmallow chicks were missing. The trail of crumpled yellow foil wrappers led to one person, and one person only.

MOTHER/DAD: (disappointed) Ooooh, Stewart.

SISTER: (whimpering and closing her eyes) I can't look.

STEWART: (moaning and rubbing his belly-aching stomach) Those chocolate bunnies never had a chance . . . It was The Tooth.

SWEET TOOTH: HEY! CAN WE STOP GOING DOWN MEMORY LANE HERE AND OPEN UP THAT BAG OF COOKIES?

STEWART: That's it. I've had enough!

SWEET TOOTH: ENOUGH? I HAVEN'T EVEN HAD ONE.

STEWART: (shouting) No more cookies! No more candy. No more cake. No more nothing!

SWEET TOOTH: That's no more anything. And . . . WHO DO YOU THINK YOU'RE KIDDING, KID? Bring on those chocolate chips!" Stewart sighed. What choice did he have? He was a boy with one big Sweet Tooth. He tore open the bag. He grabbed one, then two-three-four cookies. He opened his mouth.

SWEET TOOTH: (shouting) COME TO PAPA! Stewart stopped.

SWEET TOOTH: What are you waiting for, kid? Come on. Cookie. Cookie. Cookie. Cookie. Stewart dropped the cookies. But . . . . not in his mouth.

STEWART: (determined) It's over, Tooth. I’m cutting you off. Starting right now. It's cold turkey.

SWEET TOOTH: Cold turkey? Yee-ech! I hate cold turkey . . . unless you add a little cranberry sauce,

STEWART: Didn't you hear me, Tooth? I said it's over. From now on there's nothing for you but a . . . a . . . a . . . (large gulp) Healthy diet.

SWEET TOOTH: (wailing) Healthy? Kid, say you don't mean it. But Stewart meant it, all right. He meant every word. Yes, it was trying. Yes, it was difficult. Okay, it was darn near impossible. But Stewart stayed strong. For The Tooth it was a different story.

SWEET TOOTH: PEAS? YOU'RE GIVING ME PEAS? LITILE DRY GREEN VEGGIE MARBLES? Broccoli? You're feeding me a shrub? THAT'S NOT GOING TO DO IT. DESSERT! WHERE'S DESSERT? I'm begging you. WHEN DO WE GET TO THE GOOD STUFF?"

STEWART: (putting his hands over his ears) I can't hear you. Strong. He stayed strong.

SWEET TOOTH: Just one eensy-teensy CHOCOLATE- COVERED PEANUT before hitting the sack. How about it? . . . A nosh. A nibble. A breath mint. Somethin'!

STEWART: (turning out the light) Forget it. Strong. Strong.

SWEET TOOTH: (at breakfast the next morning as Stewart eats his cereal) COME ON. WHADDAYA SAY? ONE SPOONFUL OF SUGAR. Stewart shook his head.

SWEET TOOTH: (losing his grip) A DROP OF CHOCOLATE MILK. One measly little crumb-bun crumb.

STEWART: No way. Very strong.

SWEET TOOTH: (shouting) HEY, WATCH THAT TOOTHBRUSH! AND KEEP THAT TONGUE OF YOURS ON THE OTHER SIDE OF YOUR MOUTH. TRYIN' TO WIGGLE ME OUT OF HERE, HUH? Well, I'm not going, kid. I'm not going anywhere! Do you hear me? . . . Do you hear me?" Stewart brushed. Flossed. Gargled.

SWEET TOOTH: (moaning weakly) U-u-ugh He's not hearing me . . . I'll get you for this, kid. Stewart smiled. He was winning. Oh yes, he was winning. Three days passed. The Tooth was quiet. Very quiet. Almost too quiet. But Stewart wasn't thinking "tooth." He was thinking baseball. It was the biggest game of the season. Bottom of the ninth. Stewart was at the plate. Runners were on second and third. Two outs. Two strikes. The crowd was on their feet. The game was on the line. Stewart's team was down by one run. The pitcher went into his windup. There was a hush from the stands. A big fat fastball was heading for the plate. It was all up to Stewart. And then . . .

SWEET TOOTH: BOY, COULD I GO FOR A HUNK OF BUBBLE GUM RIGHT NOW! Swing! Swish!

SWEET TOOTH: Heh-heh-heh.

UMPIRE: (yelling) Strike three! Y'er out!

SWEET TOOTH: Gotcha! Now go get me some goodies!

STEWART: (mumbling as he drops the bat) I'll get you goodies. Home he marched. Into the kitchen. Straight for the refrigerator. He yanked open the door. Rustled through the vegetable bin. He flung lettuce. He tossed tomatoes. He hurled a head of cauliflower. And then he pulled out . . . .a carrot. That's right. A carrot.

STEWART: (defiantly as he lifts the carrot above his head) It's over for you, Tooth.

SISTER: (wide-eyed) What are you going to do with that? Stewart grinned. He opened his mouth wide. Very wide.

SWEET TOOTH: KID! NO! NOT THE CARROT! NOT THE CARROT!"

STEWART: (shouting) Yes. The carrot!

SWEET TOOTH: No, kid, no!

SISTER: (covering her eyes) Am I too young to be watching this? Closer. Closer. Closer. And then . . . . CR-CR-CRUNCH.

SWEET TOOTH: Ahhh-ahh-ahhhhh . . . So long, sweet world! . . . What a way to go . . . Done in by an orange veggie. Stewart rubbed his jaw. He stared at the carrot . . . (the tooth is in his hand) and The Tooth. It was over.

SISTER: What's going to happen to it? Stewart placed the molar under his pillow, then looked at his sister.

STEWART: (smiling) Who knows? That's the tooth fairy's problem now.

***** [In the Tooth Fairy’s Bag of Teeth] ****

BABY TEETH: WAH, WAH, WAH!

CANINE TOOTH: WOOF!

WISDOM TOOTH: Please be quiet. I’m trying to read.

SWEET TOOTH: Pipe down, wise guy! What does a sweet tooth have to do to get an ice-cream sundae around here? With hot fudge! And throw some sprinkles on it while you’re at it.

TOOTH FAIRY: ROTTEN TEETH!
```

---

## IC-2135: Tain’t So

- Title: Tain’t So
- Author (byline): Langston Hughes
- Work: The Collected Works of Langston Hughes – The Short Stories (Volume 15) edited by R. Baxter Miller, Pgs 209-212
- Publisher: University of Missouri
- Publication date as stated: July 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: LANGSTON, NORTHERN LADY, MISS LUCY, NEGRO WOMAN, MISS JONES
- Teaser before the introduction: Yes
- Spoken words (computed): 1080
- Already set (do not supply): none

### Source block (context only)

```text
Author: Langston Hughes
Book: The Collected Works of Langston Hughes –
The Short Stories (Volume 15) edited by R.
Baxter Miller, Pgs 209-212
ISBN: 978-0826214119
Publisher: University of Missouri
Date (Month/Year): July 2002
```

### Introduction (context only: never use it for content warnings)

```text
Tain’t So by Langston Hughes
```

### Performance text (classify this)

```text
LANGSTON: (Pg 209-212) Miss Lucy Cannon was a right nice old white woman, except that she really did not like colored folks, not even after she come out West to California. She could never get over certain little Southern ways she had, and long as she knowed my Uncle Joe, she never would call him Mister -- nor any other colored man for that matter, not even the minister of the Baptist Church. Miss Lucy Cannon just wouldn't call colored folks Mister nor Missus, no matter who they was.

She was always ailing around, too, and ever so often she would have a fainting spell, like all good Southern white ladies. Looks like the older she got, the more she would be sick and couldn't hardly get around -- that is, until she went to a healer and got cured.

And that is one of the funniest stories Uncle Joe ever told me, how old Miss Cannon got cured of her heart and hip in just one cure at the healer's.

LANGSTON: Seems like for three years or more she could scarcely walk -- even with a cane -- had a terrible bad pain in her right leg from her knee up. And on her left side, her heart was always just about to give out. She was in bad shape, that old Southern lady, to be as spry as she was, always giving teas and dinners and working her colored help to death.

Well, Uncle Joe says, one New Year's Day a friend of hers, a Northern lady who was kinda old and retired also told Miss Cannon . . .

NORTHERN LADY: Darling, you seem to suffer so all the time, and you say you've tried all the doctors, and all kinds of baths and medicines. Why don't you try my way of overcoming? Why don't you try faith?

MISS LUCY: (sipping tea) Faith, honey?

NORTHERN LADY: Yes, my dear, faith! I have one of the best faith-healers in the world. She's a woman, and she heals by power. She lives in Hollywood.

MISS LUCY: Give me her address, and I'll go to see her. How much do her treatments cost?

LANGSTON: Miss Lucy warn't so rich as some folks thought she was.

NORTHERN LADY: Only Ten Dollars, dearest. Ten Dollars a treatment. Go, and you'll come away cured.

LANGSTON: And before she could learn any more about the healer, some other friends came in and interrupted the conversation.

A few days later, however, Miss Lucy took herself all the way from Pasadena to Hollywood, and thought she would go to see the healer, which she did, come Monday morning early. Using her cane and hobbling on her left leg, feeling a bit bad around the heart, and suffering terribly in her mind, she managed to walk slowly but with dignity a half-dozen blocks to the rather humble street to the office and home of the healer.

When she got to the house she was seeking, a large frame dwelling, newly painted, she saw a sign thereon: MISS PAULINE JONES

"So that’s her name," thought Miss Lucy. "Pauline Jones, Miss Jones."

Ring And Enter said a little card above the bell. So Miss Lucy entered. But the first thing that set her back a bit was that nobody received her, so she just sat down to await Miss Jones, the healer who had, she heard, an enormous following in Hollywood. In fact, that's why she had come early, so she wouldn't have to wait long. Now, it was only nine o'clock. The office was open -- but empty. So Miss Lucy simply waited. Ten minutes passed. Fifteen. Twenty. Finally she became all nervous and fluttery. Heart and limb! Pain, pain, pain! Not even a magazine to read.

MISS LUCY: (impatiently) Oh, me! What is this?

(peering at a sign on the wall) Why, I never!

LANGSTON: There was a sign on the wall that read: BELIEVE

MISS LUCY: (looking at her watch) I will wait just ten minutes more.

LANGSTON: But before the ten minutes were up, another woman entered the front door and sat down. To Miss Lucy's horror, she was a colored woman! In fact, a big black colored woman!

Said Miss Lucy to herself . . .

MISS LUCY: (softly) I'll never in the world get used to the North. Now here's a great -- my friend says -- great faith-healer, treating darkies! Why, down in Alabama, a Negro patient wouldn't dare come in here and sit down with white people like this!

LANGSTON: But, womanlike, (and having still five minutes to wait) Miss Lucy couldn't keep her mouth shut that long. She just had to talk, albeit to a Negro, so she began on her favorite subject -- herself.

MISS LUCY: I certainly feel bad this morning.

NEGRO WOMAN: (placidly) Tain't so.

LANGSTON: Which sort of took Miss Lucy back a bit.

MISS LUCY: (lifting her chin indignantly) Indeed, it is so! My heart is just about to give out. My breath is short.

NEGRO WOMAN: (calmly) Tain't so a-tall.

MISS LUCY: (gasping) Why! Such impudence! I tell you it is so! I could hardly get down here this morning.

NEGRO WOMAN: (calmly) Tain't so.

MISS LUCY: Besides my heart, my right hip pains me so I can hardly sit here.

NEGRO WOMAN: I say, tain't so.

MISS LUCY: (screaming) I tell you it is so! Where is the healer? I won't sit here and suffer this -- this impudence. I can't! It'll kill me! It's outrageous!

NEGRO WOMAN: (serenely) Tain't so.

LANGSTON: Whereupon Miss Lucy rose. Her pale face flushed a violent red.

MISS LUCY: (looking around the room) Where is the healer?

NEGRO WOMAN: Right here.

MISS LUCY: What? You're the – why -- you?

NEGRO WOMAN: I'm Miss Jones.

MISS LUCY: Why, I never heard the like. A colored woman as famous as you? Why, you must be lying!

MISS JONES: (calmly) Tain't so.

MISS LUCY: Well, I shan't stay another minute!

MISS JONES: Ten Dollars, then. You've had your treatment, anyhow.

MISS LUCY: Ten Dollars! That's entirely too much!

MISS JONES: Tain't so.

LANGSTON: Angrily Miss Lucy opened her pocketbook, threw a Ten Dollar bill on the table, took a deep breath, and bounced out. She went three blocks up Sunset Boulevard walking like the wind, conversing with herself.

MISS LUCY: (angrily) Tain't so! 'Tain't so! I tell her I'm sick and she says, 'Tain't so!'

LANGSTON: On she went at a rapid gait, stepping like a young girl -- so mad she had forgotten all about her infirmities, even her heart -- when suddenly she cried . . .

MISS LUCY: Lord, have mercy, my cane! For the first time in three years, I'm without a cane!

LANGSTON: Then she realized that her breath was giving her no trouble at all. Neither was her leg. Her temper mellowed. The sunshine was sweet and warm. She felt good.

MISS LUCY: (smiling to herself) Colored folks do have some funny kind of supernatural conjuring powers, I reckon. (her face going grim again) But the impudence of 'em! Soon's they get up North -- calling herself Miss Pauline Jones. The idea! Putting on airs and charging me Ten Dollars for a handful of Tain't so's!

LANGSTON: In her mind she clearly heard . . .

MISS JONES: Tain't so!
```

---

## IC-2136: The Tale of the Three Brothers (Harry Potter & the Deathly Hallows, C. 21)

- Title: The Tale of the Three Brothers (Harry Potter & the Deathly Hallows, C. 21)
- Author (byline): J.K. Rowling
- Work: Harry Potter and the Deathly Hallows
- Publisher: Arthur A. Levine Books
- Publication date as stated: July 2009
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: HARRY, XENO, HERMIONE, RON
- Teaser before the introduction: Yes
- Spoken words (computed): 1786
- Already set (do not supply): none

### Source block (context only)

```text
Author: J.K. Rowling
Book: Harry Potter and the Deathly Hallows
ISBN: 978-0545139700
Publisher: Arthur A. Levine Books
Date (Month/Year): July 2009
```

### Introduction (context only: never use it for content warnings)

```text
It is said that whomever holds all three of the Deathly Hallows will become the Master of Death!

But what does it mean to become the “Master of Death?” – Does it mean that you have complete control over death itself, or that by accepting and not fearing death, you have the ultimate control?

Albus Dumbledore once spoke these words: “The true master does not seek to run away from Death. He accepts that he must die, and understands that there are far, far worse things in the living world than dying.”

And so the legend comes to pass in the final book of the Harry Potter series: Harry Potter and the Death Hallows. This is The Tale of the Three Brothers by J.K. Rowling.
```

### Performance text (classify this)

```text
HARRY: The Deathly Hallows?

XENO: You haven't heard of them? I assume that you are familiar with 'The Tale of the Three Brothers'? . . .I have a copy somewhere . . . He glanced vaguely around the room, at the piles of parchment and books, but Hermione said,

HERMIONE: I've got a copy right here. And she pulled out The Tales of Beedle the Bard from the small, beaded bag.

XENO: Well then, why don't you read it out aloud? Much the best way to make sure we all understand. She opened the book and began to read.

HERMIONE: There were once three brothers who were traveling along a lonely, winding road at twilight – In time, the brothers reached a river too deep to wade through and too dangerous to swim across. However, these brothers were learned in the magical arts, and so they simply waved their wands and made a bridge appear across the treacherous water. They were halfway across it when they found their path blocked by a hooded figure. And Death spoke to them – He was angry that he had been cheated out of the three new victims, for travelers usually drowned in the river. But Death was cunning. He pretended to congratulate the three brothers upon their magic, and said that each had earned a prize for having been clever enough to evade him. So the oldest brother, who was a combative man, asked for a wand more powerful than any in existence: a wand that must always win duels for its owner, a wand worthy of a wizard who had conquered Death! So Death crossed to an elder tree on the banks of the river, fashioned a wand from a branch that hung there, and gave it to the oldest brother. Then the second brother, who was an arrogant man, decided that he wanted to humiliate Death still further, and asked for the power to recall others from Death. So Death picked up a stone from the riverbank and gave it to the second brother, and told him that the stone would have the power to bring back the dead. And then Death asked the third and youngest brother what he would like. The youngest brother was the humblest and also the wisest of the brothers, and he did not trust Death. So he asked for something that would enable him to go forth from that place without being followed by Death. And Death, most unwillingly, handed over his own Cloak of Invisibility. Then Death stood aside and allowed the three brothers to continue on their way, and they did so talking with wonder of the adventure they had had and admiring Death's gifts. In due course the brothers separated, each for his own destination. The first brother traveled on for a week more, and reaching a distant village, sought out a fellow wizard with whom he had a quarrel. Naturally, with the Elder Wand as his weapon, he could not fail to win the duel that followed. Leaving his enemy dead upon the floor the oldest brother proceeded to an inn, where he boasted loudly of the powerful wand he had snatched from Death himself, and of how it made him invincible. That very night, another wizard crept upon the oldest brother as he lay, wine-sodden upon his bed. The thief took the wand and for good measure, slit the oldest brother's throat. And so Death took the first brother for his own. Meanwhile, the second brother journeyed to his own home, where he lived alone. Here he took out the stone that had the power to recall the dead, and turned it thrice in his hand. To his amazement and his delight, the figure of the girl he had once hoped to marry, before her untimely death, appeared at once before him. Yet she was sad and cold, separated from him as by a veil. Though she had returned to the mortal world, she did not truly belong there and suffered. Finally the second brother, driven mad with hopeless longing, killed himself so as to truly join her. And so Death took the second brother from his own. But though Death searched for the third brother for many years, he was never able to find him. It was only when he had attained a great age that the youngest brother finally took off the Cloak of Invisibility and gave it to his son. And then he greeted Death as an old friend, and went with him gladly, and, equals, they departed this life. Hermione closed the book. It was a moment or two before Xeno seemed to realize that she had stopped reading; then he withdrew his gaze from the

window and said:

XENO: Well, there you are. Those are the Deathly Hallows. He picked up a quill from a packed table at his elbow, and pulled a torn piece of parchment from between more books.

XENO: The Elder Wand (drawing a strait vertical line on the parchment) The Resurrection Stone (adding a circle on top of the line). The Cloak of Invisibility

(enclosing both line and circle in a triangle). Together -- the Deathly Hallows.

HERMIONE: But there's no mention of the words 'Deathly Hallows' in the story,

XENO: (smugly) Well, of course not, That is a children's tale, told to amuse rather than to instruct.

Those of us who understand these matters, however, recognize that the ancient story refers to three objects, or Hallows, which, if united, will make the possessor master of Death. There was a short silence in which Xeno glanced out of the window.

RON: When you say 'master of Death'

XENO: (waving his hand) Master. Conqueror. Vanquisher . . . whichever term you prefer.

HERMIONE: (slowly) But then . . . do you mean . . . that you believe these objects – these Hallows – really exist?

XENO: (raising his eyebrows) Well, of course.

HERMIONE: We all know that there are such things as Invisibility Cloaks. They are rare, but they exist. But –"

XENO: Ah, but the Third Hallow is a true Cloak of Invisibility, Miss Granger! I mean to say, it is not a traveling cloak imbued with a Disillusionment Charm, or carrying a Bedazzling Hex, or else woven from Demiguise hair, which will hide one initially but fade with the years until it turns opaque. We are talking about a cloak that really and truly renders the wearer completely invisible, and endures eternally, giving constant and impenetrable concealment, no matter what spells are cast at it. How many cloaks have you ever seen like that, Miss Granger?" Hermione opened her mouth to answer, then closed it again, looking more confused than ever. She, Harry and Ron glanced at one another, and Harry knew that they were all thinking the same thing. It so happened that a cloak exactly like the one Xeno had just described was in the room with them at that very moment.

XENO: Exactly. None of you have ever seen such a thing. The possessor would be immeasurably rich, would he not?

HERMIONE: All right. Say the Cloak existed. . . what about that stone? The thing you call the Resurrection Stone? How can that be real?"

XENO: Prove that is not.

HERMIONE: (Outraged) But that's – I'm sorry, but that's completely ridiculous! How can I possibly prove it doesn't exist? Do you expect me to get hold of – of all the pebbles in the world and test them? I mean, you could claim that anything's real if the only basis for believing in it is that nobody's proved it doesn't exist!"

XENO: Yes, you could. I am glad to see that you are opening your mind a little.

HARRY: So the Elder Wand, you think that exists too?

XENO: Oh, well, in that case there is endless evidence. The Elder Wand is the Hallow that is most easily traced, because of the way in which it passes from hand to hand. The possessor of the wand must capture it from its previous owner, if he is to be truly master of it. Surely you have heard of the way the wand came to Egbert the Egregious, after his slaughter of Emeric the Evil? Of how Godelot died in his own cellar after his son, Hereward, took the wand from him? Of the dreadful Loxias, who took the wand from Baraabas Deverill, whom he had killed? The bloody trail of the Elder Wand is splattered across the pages of Wizarding history.

RON: So where do you think the Elder Wand is now?

XENO: Alas, who knows? History, alas, does not tell us.

HERMIONE: (after a pause) Does the Peverell family have anything to do with the Deathly Hallows?

XENO: (taken aback) You have been misleading me, young woman! I thought you were new to the Hallows Quest! Many believe that the Peverells have everything – everything! – to do with the Hallows! [that] the three brothers in the story were actually the three Peverell brothers, Antioch, Cadmus and Ignotus! That they were the original owners of the Hallows! . . . (takes tray and exits down a spiral staircase, saying) You will stay for dinner? Harry waited until they could hear Xeno moving about in the kitchen downstairs before speaking.

HARRY: (to Hermione) What do you think?

HERMIONE: (wearily) Oh, Harry, it's a pile of utter rubbish. This can't be what the sign really means. This must just be his weird take on it. What a waste of time.

HARRY: (to Ron) You didn't believe it either?

RON: Nah, that story's just one of those things you tell kids to teach them lessons, isn't it? Don't go looking for trouble, don't go pick fights, don't go messing around with stuff that's best left alone! Just keep your head down, mind your own business, and you'll be okay.

HERMIONE: I think you're right, It's just a morality tale, it's obvious which gift is best, which one you'd choose – The three of them spoke at the same time: Hermione said, "the Cloak," Ron said, "the Wand," and Harry said, "the Stone." They looked at each other, half surprised, half amused.

RON: (to Hermoine) You're supposed to say the Cloak, but you wouldn't need to be invisible if you had the wand. An unbeatable wand, Hermione, come on!

HARRY: We've already got an Invisibility Cloak.

HERMIONE: And it's helped us rather a lot, in case you hadn't noticed! Whereas the wand would be bound to attract trouble—

RON: Only if you shouted about it. As long as you kept your trap shut –

HERMIONE: (skeptically) Yes, but could you keep your trap shut? You know the only true thing he said to us was that there have been stories about extra-powerful wands for hundreds of years. The Deathstick, the Wand of Destiny, they crop up under different names through the centuries, usually in the possession of some Dark wizard who’s boasting about them.

HARRY: But how do you know that those wands -- the Deathstick, and the Wand of Destiny -- aren't the same want, surfacing over the centuries under different names?"

RON: What if they're all really the Elder Wand, made by Death? (To Harry) So why would you take the stone?

HARRY: "Well, if you could bring people back, we could have Dumbledore . . . my parents. . . But according to Beedle the Bard, they wouldn't want to come back, would they?
```

---

## IC-2137: Teach Reality, Not Rhetoric

- Title: Teach Reality, Not Rhetoric
- Author (byline): Rod Rose
- Work: Not specified
- Publisher: Tribune Star (Terre Haute, IN)
- Publication date as stated: April 23, 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 840
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rod Rose writes for The Lebanon (Ind.) Reporter.
He may be reached at rod.rose@reporter.net, 117
E. Washington Street, Lebanon, IN 46052, (765)
482-4650
ISBN: Newspaper
Publisher: Tribune Star (Terre Haute, IN)
Date (Month/Year): April 23, 2007
```

### Introduction (context only: never use it for content warnings)

```text
Teach Reality, Not Rhetoric by Rod Rose
```

### Performance text (classify this)

```text
Cho Seung-Hui carried at least 17 magazines for the Glock 19 he used to kill 32 people, and then himself, at Virginia Tech.

Witnesses said he took up to a minute to change magazines.

A rational human being who has chosen to use defend himself with a firearm can be trained to draw and fire two aimed rounds into a target the size of a paper plate 21 feet away in less than 2 seconds.

Do the math.

Ignoring the math — pretending that “gun-free zones” are valid logical defenses against madmen, instead of insane denials of reality — dooms us to hearing about another Cho Seung-Hui. There will be another public massacre, in a school, Amish or public, in a shopping mall, at a fast-food restaurant.

There will be more slaughters unless and until this society admits that evil exists; that irrational individuals walk the streets; that the world is not and never will be perfect.

No guarantees are expressed or implied when we are born. Legislate away, pontificate, twist the facts like rifling in a barrel — we are all going to die, but we can improve the odds we will live longer.

As a human being you are obligated to be aware of your surroundings. “Fend for yourself” is the advertising slogan of knife and tool maker Gerber. Having that ability allows you to fend for others.

The Founding Fathers intended that we inherit a civil society. For many reasons — sociological, political, economic, demographic, theological — we’ve lost it. It’s time for us to take it back.

Knives and firearms are nothing more than tools. They are not, of and in themselves, dangerous. It is only when they are misused that they maim and kill.

Some newspapers, some commentators, some editorial cartoonists, have criticized “the media” — even though they are part of “the media” — for “exploiting” the massacre at Virginia Tech. That they are exploiting the tragedy for their own purposes is, of course, irrelevant.

NBC has been harshly criticized for airing some of Cho Seung-Hui’s incoherent ranting. It serves no purpose, critics say.

Cho offers a lesson if we have the wisdom to recognize the opportunity. Authorities have responsibilities; if they failed in their obligations, the public has both the right and the duty to see that corrections are made and, if appropriate, punishments are administered.

“Let’s not play the blame game,” is another senseless but common reaction.

Why not? The police knew, in 2005, that Cho was a potential threat; a VT professor told NBC’s Matt Lauer she had expressed her concerns to police. They offered to place an officer outside the classroom, but that was legally as far as they could go. Cho had not made a direct threat; without that threat, the police had no authority to do more.

It’s never too early, although it can be too late, to begin assigning blame. Solutions can’t be proposed if the problem is ignored.

If the two police departments have a communications gap, build a bridge.

If the mental health professionals who could have helped Cho but could not because of inadequate funding, then give them more money. If they lack other resources, provide them.

Insisting that the lowest bid is appropriate for every aspect of civilization is reckless, irresponsible, cheap in the derogatory sense, and ultimately suicidal for a rational society.

“If lower taxes are your priority over human life, then we know what sort of person you are,” Garrison Keilor said.

This is a violent society. It’s violent because violence makes money. It’s violent because parents have surrendered their obligations. It’s violent because we are under enormous stress.

And it can be made less violent. It can be healed. But do Americans have the courage and intelligence to accept that cures are sometimes painful?

Until we stop pretending otherwise, there are more Columbines, Virginia Techs and San Ysidro McDonalds in our future.

We have to teach our children — and ourselves — the skills to recognize threats, and the appropriate responses. Sometimes it’s as simple as crossing the street. Sometimes it means running as fast and as hard as we can. Sometimes it means killing someone, then facing the consequences of having assumed the horrendous responsibility of choosing to carry a deadly weapon.

That’s reality. When you send your children to school, do so after having given them the skills to recognize threats. They must know when slipping quietly out of sight is the best choice.

They must also know when they have only two choices: Defending themselves or becoming a corpse.

Sheeple or sheepdog. It’s your choice.

NOTE: Sheeple is a term of disparagement, a

portmanteau created by combining the words

"sheep" and "people"; a reference to herd

mentality. It is often used to denote persons

who acquiesce to authority, and thus undermine

their own human individuality. The implication of

sheeple is that as a collective, people believe

whatever they are told, without processing it to

be sure that it is an accurate representation of

the real world around them. The term is

generally used in a political or religious sense.
```

---

## IC-2138: Tell Me Why You Cry

- Title: Tell Me Why You Cry
- Author (byline): Nicole Rose Patridge
- Work: Chicken Soup for the Teenage Soul II
- Publisher: Scholastic, Inc.
- Publication date as stated: Oct 1998
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1044
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nicole Rose Patridge
Book: Chicken Soup for the Teenage Soul II
ISBN: 978-1558746169
Publisher: Scholastic, Inc.
Date (Month/Year): Oct 1998
```

### Introduction (context only: never use it for content warnings)

```text
You never know how much a younger brother means to you until he is gone. When your brother dies, you lose part of your past and your future as it “should have been” with him, and there’s a hole there, an emptiness that will never again be filled. He isn’t / wasn’t “just” a brother he was a part of you, and you miss him and grieve for him every day and always will. Tell Me Why You Cry by Nicole Rose Patridge
```

### Performance text (classify this)

```text
They say that everyone has a story that will break your heart. My little brother Nicholas has cancer. His hair had fallen out, and he was so weak that it was hard for him to walk. I couldn’t stand to see the pain in his eyes any longer. His childhood memories were not of Christmases, camping trips and toys; his memories were of hospital visits, I.V.s and blood transfusions.

I remember when it first started, when he was only three. At first, it was the way he was getting awful, ugly bruises. We didn’t think anything of it until they started showing up in places they didn’t belong, like in his armpit or on his scalp. Then there were nosebleeds, which were a constant occurrence. My mom would always have to remind us, “Don’t horse around with Nicholas; his nose will start to bleed.”

His form of cancer was acute lymphatic leukemia (ALL), which was very curable. Seventy percent of children with ALL achieve remission within one year, and out of those remissions, 50 percent never relapse. Nicky’s odds were very good.

He started chemotherapy immediately, to stop the cancer form getting any worse. It went well but it was very hard. He was at the hospital Monday, Tuesday and Wednesday receiving treatment, and then he would come home for the rest of the week, sick and completely powerless. He missed pre-school that year, but he was in remission in nine months, and we were all happy.

Life was back to normal for a while, until one day during freshman year. I came home from school to see my parents sitting on the couch, which was odd, because my parents were never home after school. But when I saw the tears, I knew that my worst fear has come true. The cancer was back.

He was five by then and had been in remission for about two years. We all thought he had beaten it, but then they found a cancerous tumor inside his chest. The doctors were not sure how big it was, so they set a surgery date. They were going to make a small incision on his chest and evaluate it that same day.

The day of the surgery, we all woke up early to accompany Nicholas to the hospital. We sat in the stark white waiting room of B-3, the “cancer hall.” I had been there far more than I could handle. In the last two years, I had seen too much of this hall, of cribs occupied by babies whose mothers visit less and less, of children who know they will not make it. The sickening smell of death lines each room, telling past stories of children whose lives were cut short by a silent killer.

We sat and waited for what seemed like eternity. Finally, after four hours Dr. McGuiness, Nicky’s cancer physician specialist, came out of the door marked SURGERY. He was still wearing his operating garb as he motioned for us to follow him, which meant that we needed to talk. As we sat down, fear consumed us.

“Nicholas is out of surgery now, and the medicine will wear off soon,” Dr. McGuiness began. “I’m sorry, though,” he continued. “The tumor has grown too large. It has consumed one entire lung, and it has grown down one side of his heart. There is nothing we can do now.”

As I heard those words, my eyes filled with tears. Those words meant that it was time to stop fighting because we would not win. I looked around and knew I wanted to leave. I wanted to run far, far away, but I knew I couldn’t. It wouldn’t make Nicky live.

The doctor left for ten minutes so we could regain composure. When he returned, he asked where we wanted Nicholas to spend his last days. We said we wanted Nicky home.

The next few months were torture, having to watch Nicky get sicker and weaker. As the tumor grew, his heart stopped pumping regularly and he became short of breath.

The summer went by much quicker that it should have. Nicholas’s health remained steady, although still very fragile. We were even able tot take a trip to Disneyland, Nicky’s One Last Wish. It was so hard, though trying to be happy for him and knowing it was our last vacation together as family.

As the year went by, the bustle and jumble of the holiday season kept us occupied. Halloween was fun and Thanksgiving was delicious. Then, as we started preparing for Christmas, Nicky’s health deteriorated.

One day as everyone was decorating the tree, I went in to see Nicholas. The Christmas lights beautifully illuminated his face and brought out an innocent sparkle we had not seen in a long time. As I came closer, I realized he was crying. I sat down the chair with him and held him in my arms the way I had when he was younger.

“Nicky, tell me why you cry,” I said.

“It’s just not fair,” he blubbered.

“What’s not fair?” I asked.

“Why am I going to die?”

“Well, you know that everyone dies,” I replied, obviously avoiding the subject. I didn’t want him to know either.

“But not like me. Why do I have to die? Why so early?” and then he started to cry. He buried his head in my chest, and I started to cry, too. We sat like that for a long time. A very long, lonesome and scary time. Afterwards there was understanding between us. He was ready, and so was I. We could handle anything now.

In January, he slipped into a coma and we knew we were losing him. One day we sat in his room, holding his hand, because we knew this was going to be his last time with us. Suddenly, certain peacefulness filled the room, and I knew that Nicholas had breathed his last breath.

I looked outside. The freshly fallen snow somehow seemed brighter. I hated myself for it, but I suddenly felt better. All the pain and sorrow of the past few years were gone, and I knew Nicolas was safe. He was no longer scared or hurt, and it was better this way.
```

---

## IC-2139: There Will Come Soft Rains

- Title: There Will Come Soft Rains
- Author (byline): Ray Bradbury
- Work: The Harper Anthology of Fiction
- Publisher: Addison-Wesley Pub Co
- Publication date as stated: Jan 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2223
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ray Bradbury
Book: The Harper Anthology of Fiction
ISBN: 978-0673396341
Publisher: Addison-Wesley Pub Co
Date (Month/Year): Jan 1997
```

### Introduction (context only: never use it for content warnings)

```text
Published in 1920, Sara Teasdale’s poem "There Will Come Soft Rains" envisions an idyllic post-apocalyptic world in which nature continues peacefully, beautifully, and indifferently after the extinction of humankind.

But Ray Bradbury’s future is quite different and much less peaceful. The future is now! Alexa, Siri, and Google Assistants have expanded their abilities and technology reigns supreme. Smart homes cater to our every need . . . until society destroys itself and a radioactive glow fills the skies.

There Will Come Soft Rains by Ray Bradbury
```

### Performance text (classify this)

```text
There will come soft rains and the smell of the

ground, And swallows circling with their shimmering sound;

And frogs in the pools singing at night, And wild plum trees in tremulous white;

Robins will wear their feathery fire, Whistling their whims on a low fence-wire;

And not one will know of the war, not one Will care at last when it is done,

Not one would mind, neither bird nor tree, If mankind perished utterly;

And Spring herself, when she woke at dawn Would scarcely know that we were gone.

In the living room the voice-clock sang, Tick-tock, seven o'clock, time to get up, time to get up, seven o'clock! as if it were afraid that nobody would. The morning house lay empty. The clock ticked on, repeating and repeating its sounds into the emptiness. Seven-nine, breakfast time, seven-nine!

In the kitchen the breakfast stove gave a hissing sigh and ejected from its warm interior eight pieces of perfectly browned toast, eight eggs sunny side up, sixteen slices of bacon, two coffees and two cool glasses of milk.

"Today is August 4, 2026," said a second voice from the kitchen ceiling, "in the city of Allendale, California." It repeated the date three times for memory's sake. "Today is Mr. Featherstone's birthday. Today is the anniversary of Tilita's marriage. Insurance is payable, as are the water, gas, and light bills."

Somewhere in the walls, relays clicked, memory tapes glided under electric eyes.

Eight-one, tick-tock, eight-one o'clock, off to school, off to work, run, run, eight-one! But no doors slammed, no carpets took the soft thread of rubber heels. It was raining outside. The weather box on the front door sang quietly: "Rain, rain, go away; rubbers, raincoats for today…" And the rain tapped on the empty house, echoing.

Outside, the garage chimed and lifted its door to reveal the waiting car. After a long wait the door swung down again.

At eight-thirty the eggs shriveled and the toast was like stone. An aluminum wedge scraped them into the sink, where hot water whirled them down a metal throat which digested and flushed them away to the distant sea. The dirty dishes were dropped into a hot washer and emerged twinkling dry.

Nine-fifteen, sang the clock, time to clean.

Out of warrens in the wall, tiny robot mice darted. The rooms were a crawl with the small cleaning animals, all rubber and metal. They thudded against chairs, whirling their mustached runners, kneading the rug nap, sucking gently at hidden dust. Then, like mysterious invaders, they popped into their burrows. Their pink electric eyes faded. The house was clean.

Ten o'clock. The sun came out from behind the rain. The house stood alone in a city of rubble and ashes. This was the one house left standing. At night the ruined city gave off a radioactive glow which could be seen for miles.

Ten-fifteen. The garden sprinklers whirled up in golden founts, filling the soft morning air with scatterings of brightness. The water pelted windowpanes, running down the charred west side where the house had been burned, evenly free of its white paint. The entire west face of the house was black, save for five places. Here the silhouette in paint of a man mowing a lawn. Here, as in a photograph, a woman bent to pick up flowers. Still farther over, their images burned on wood in one titanic instant, a small boy, hands flung into the air; higher up, the image of a thrown ball, and opposite him, a girl, hands raised to catch a ball which never came down.

The five spots of paint—the man, the woman, the children, the ball—remained. The rest was a thin charcoaled layer.

The gentle sprinkler rain filled the garden with falling light.

Until this day, how well the house had kept its peace. How carefully it had inquired, "Who goes there? What's the password?" and, getting no answer from lonely foxes and whining cats, it had shut up its windows and drawn shades in an old-maidenly preoccupation with self—protection which bordered on mechanical paranoia.

It quivered at each sound, the house did. If a sparrow brushed a window the shade snapped up. The bird, startled, flew off! No, not even a bird must touch the house! The house was an altar with ten thousand attendants, big, small, servicing attending, in choirs. But the gods had gone away, and the ritual of the religion continued senselessly, uselessly.

Twelve noon.

A dog whined, shivering, on the front porch.

The front door recognized the dog voice and opened. The dog, once huge and fleshy, but now gone to bone and covered with sores, moved in and though the house, tracking mud. Behind it whirred angry mice, angry at having to pick up mud, angry at inconvenience.

For not a leaf fragment blew under the door but what the wall flipped open and the copper scrap rats flashed swiftly out. The offending dust, hair, or paper, seized in miniature steel jaws, was raced back to the burrow. There, down the tubes which fed into the cellar, it was dropped into the sighing vent of an incinerator which sat like evil Baal in a dark corner.

The dog ran upstairs, hysterically yelping to each door, at least realizing, as the house realized, that only silence was there.

It sniffed the air and scratched the kitchen door. Behind the door the stove was making pancakes which filled the house with a rich baked odor and the scent of maple syrup.

The dog frothed at the mouth, lying at the door, sniffing, its eyes turned to fire. It ran wildly in circles, biting at its tail, spun in a frenzy, and died. It lay in the parlor for an hour.

Two o'clock, sang a voice.

Delicately sensing decay at last, the regiments of mice hummed out as softly as blown gray leaves in an electrical wind.

Two-fifteen.

The dog was gone.

In the cellar, the incinerator glowed suddenly and a whirl of sparks leaped up the chimney.

Two thirty-five.

Bridge tables sprouted from patio walls. Playing cards fluttered onto pads in a shower of pips. Martinis manifested on an oaken bench with egg-salad sandwiches. Music played.

But the tables were silent and the cards untouched.

At four o'clock the tables folded like butterflies back though the paneled walls.

Four-thirty.

The nursery walls glowed.

Animals took shape: yellow giraffes, blue lions, pink antelopes, lilac panthers cavorting in crystal substance. The walls were glass. They looked upon color and fantasy. Hidden fills clocked though well-oiled sprockets, and the walls lived. The nursery floor was woven to resemble a crisp, cereal meadow. Over this ran aluminum roaches and iron crickets, and in the hot still air butterflies of delicate red tissue wavered among the sharp aroma of animal spoors! There was the sound like a great matted yellow hive of bees within a dark bellows, the lazy bumble of a purring lion. And there was the patter of okapi feet and the murmur of a fresh jungle rain, like other hoofs, falling upon the summer-starched grass. Now the walls dissolved into distances of parched weed, mile on mile, and the warm endless sky. The animals drew away into thorn brakes and water holes. It was the children's hour.

Five o'clock. The bath filled with clear hot water.

Six, seven, eight o'clock. The dinner dishes manipulated like magic tricks, and in the study a click. In the metal stand opposite the hearth where a fire now blazed up warmly, a cigar popped out, half an inch of soft gray ash on it, smoking, waiting.

Nine o'clock. The beds warmed their hidden circuits, for nights were cool here.

Nine-five. A voice spoke from the study ceiling: "Mrs. McClellan, which poem would you like this evening?" The house was silent.

The voice said at last, "Since you express no preference, I shall select a poem at random." Quiet music rose to back the voice. "Sara Teasdale. As I recall, your favorite…"

There will come soft rains and the smell of the

ground, And swallows circling with their shimmering sound;

And frogs in the pools singing at night, And wild plum trees in tremulous white;

Robins will wear their feathery fire, Whistling their whims on a low fence-wire;

And not one will know of the war, not one Will care at last when it is done,

Not one would mind, neither bird nor tree, If mankind perished utterly;

And Spring herself, when she woke at dawn Would scarcely know that we were gone.

The fire burned on the stone hearth and the cigar fell away into a mound of quiet ash in its tray. The empty chairs faced each other between the silent walls, and the music played.

At ten o'clock the house began to die.

The wind blew. A falling tree bough crashed through the kitchen window. Cleaning solvent, bottled, shattered over the stove. The room was ablaze in an instant!

"Fire!" screamed a voice. The house lights flashed, water pumps shot water from the ceilings. But the solvent spread on the linoleum, licking, eating, under the kitchen door., while the voices took it up in chorus: "Fire, fire, fire!"

The house tried to save itself. Doors sprang tightly shut, but the windows were broken by the heat and the wind blew and sucked upon the fire.

The house gave ground as the fire in ten billion angry sparks moved with flaming ease from room to room and then up the stairs. While scurrying water rats squeaked from the walls, pistoled their water, and ran for more. And the wall sprays let down showers of mechanical rain.

But too late. Somewhere, sighing, a pump shrugged to a stop. The quenching rain ceased. The reserve water supply which had filled baths and washed dishes for many quiet days was gone.

The fire crackled up the stairs. It fed upon Picassos and Matisses in the upper halls like delicacies, baking off the oily flesh, tenderly crisping the canvases into black shavings.

Now the fire lay in bed, stood in windows, changed the colors of drapes!

And then, reinforcements. From attic trapdoors, blind robot faces peered down with faucet mouths gushing green chemical.

The fire backed off, as even an elephant must at the sight of a dead snake.

Now there were twenty snakes whipping over the floor, killing the fire with a clear cold venom of green froth.

But the fire was clever. It had sent flame outside the house, up through the attic to the pumps there. An explosion! The attic brain which directed the pumps was shattered into bronze shrapnel on the beams.

The fire rushed back into every closet and felt of the clothes hung there.

The house shuddered, oak bone on bone, its bared skeleton cringing from the heat, its wire, its nerves revealed as if a surgeon had torn the skin off to let the red veins and capillaries quiver in the scalded air. Help, help! Fire! Run, run! Heat snapped mirrors like the first brittle winter ice. And the voices wailed. Fire, fire, run, run, like a tragic nursery rhyme, a dozen voices, high, low, like children dying in a forest alone, alone. And the voices fading as the wires popped their sheathings like hot chestnuts. One, two, three, four, five voices died.

In the nursery the jungle burned. Blue lions roared, purple giraffes bounded off. The panthers ran in circles, changing color, and ten million animals, running before the fire, vanished off toward a distant steaming river . . . Ten more voices died.

In the last instant under the fire avalanche, other choruses, oblivious, could be heard announcing the time, cutting the lawn by remote-control mower, or setting an umbrella frantically out and in, the slamming and opening front door, a thousand things happening, like a clock shop when each clock strikes the hour insanely before or after the other, a scene of maniac confusion, yet unite; singing, screaming, a few last cleaning mice darting bravely out to carry the horrid ashes away! And one voice, with sublime disregard for the situation, read poetry aloud in the fiery study, until all the film spools burned, until all the wires withered and the circuits cracked.

The fire burst the house and let it slam flat down, puffing out skirts of spark and smoke.

In the kitchen, an instant before the rain of fire and timber, the stove could be seen making breakfasts at a psychopathic rate, ten dozen eggs, six loaves of toast, twenty dozen bacon strips, which, eaten by fire, started the stove working again, hysterically hissing!

The crash. The attic smashing into kitchen and parlour. The parlour into cellar, cellar into sub-cellar. Deep freeze, armchair, film tapes, circuits, beds, and all like skeletons thrown in a cluttered mound deep under.

Smoke and silence. A great quantity of smoke.

Dawn showed faintly in the east. Amount the ruins, one wall stood alone. Within the wall, a last voice said, over and over gain and again, even as the sun rose to shine upon the heaped rubble and steam:

Today is August 5, 2026, today is August 5, 2026, today is . . .
```

---

## IC-2140: Theseus

- Title: Theseus
- Author (byline): Barbara McBride-Smith
- Work: Greek Myths Western Style
- Publisher: August House, Inc.
- Publication date as stated: April 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2198
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barbara McBride-Smith
Book: Greek Myths Western Style
ISBN: 978-0874835243
Publisher: August House, Inc.
Date (Month/Year): April 2001
```

### Introduction (context only: never use it for content warnings)

```text
In the original myth, Theseus, a hero of Greek legends, was known for his quick wits. His cleverness made him one of the great monster slayers of Greek mythology. But for Barbara McBride-Smith – Greek mythology is just a bit overwhelming, so she has re-written the myths, added her own special Texas trade-mark and just a bit of humor to make them more palatable. And even though in this version, Theseus may have some mismatched cogs . . . the basis of the myth remains the same . . . Theseus vs the Minotaur!
```

### Performance text (classify this)

```text
NOTE: Best if told with a Texas “twang”

Theseus is a Greek word that means “forgetful.” OK, so it’s not, but it ought to be.

When Theseus was born, his daddy picked him up, turned him around a few times, looked deep into his eyes, and said to the mama, “Hon, this boy’s got a few cogs without a matching ratchet.” Now, he could have said a lot of things that would have become self-fulfilling prophecies about Theseus. He could have said:

“This boy’s elevator don’t go all the way to the top.”

“He don’t have both oars in the water.”

“He ain’t the sharpest quill on the porcupine.”

“His dipstick don’t reach his oil.”

Or . . . “He must have gotten into the gene pool when the lifeguard wasn’t looking,”

He could have said any of those things. But what he said was, “This boy’s got a few cogs without a matching ratchet.” And the daddy was right.

Then the daddy took a sword and a pair of shoes, buried them in a hole in the back yard, covered them up with a big ol’ rock, and said to his wife. “Hon, when this boy gets big enough to move that rock, and smart enough to know what’s under it, send him around to see me.” And the daddy was outta there!

The mama did the best she could raising Theseus. But by the time he was a teenager, he was starting to get on his mama’s nerves. That boy couldn’t remember anything she told him. Besides that, when it came to following directions, he was slower than a herd of turtles stampeding through peanut butter. Every day the mama would say, “Son, do you remember that hole out there in the back yard?”

“Uh, sure, Mom.”

“Well, go out there and see if you can move that rock off it.”

“Sure, Mom.”

But before he could get all the way out to that rock, he would trip over an anthill and lose track of where he was going. Or he’d get caught up in a game of “Gotcha” with his friends and forget all about what he was supposed to be doing.

You see, “Gotcha” was Theseus’s favorite game, and he whiled away many an hour playing it. This is how it works: everybody, except the one who is It, goes out into the woods and hides up in the trees. The one who is It then walks under the trees looking for the ones who are hiding. Suddenly somebody up in a tree jumps down on the one who is It, knocking the one who is It to the ground, sometimes rendering the one who is It unconscious. The one doing the jumping then hollers, “Gotcha!”

Theseus loved being It. He was so good at being It, everybody let him be It all the time. He would go walking along under those trees and somebody would jump down on him. But Theseus always heard them before they landed on him. He could hear the leaves rustle. He could hear the air move. So before anybody could lay a hand on him, he would whirl around, knock ‘em about a hundred yards, and holler, “Gotcha back!”

Theseus’s mama would see him dragging back in the house a few hours after she’d sent him out, and she’d say, “Are you coming back in here without that rock?”

Theseus would wrinkle up his brow like he was working on a problem in quantum physics and say, “What rock?”

One day, the mama got fed up. She grabbed Theseus by the ear and dragged him out to the back yard. “That rock, son. Do you see that rock? Well, move it!”

Theseus didn’t know how strong he was. He picked up that big ol’ rock with one hand and tossed it aside.

“Now, what do you see down there in that hole?” asked his mama.

“Uh, a sword and a pair of shoes.”

“Congratulations, Son. You pass with an A.” The mama slapped a map into one of his hands and a sack lunch into the other. “Good luck with your daddy” she said. And the mama was outta there!

Theseus’s daddy had taken up residence in a place called Athens, so that’s where Theseus headed. The Athenian Road was a very dangerous road. It was infested with a bunch of ragtag, third-rate burglars and bandits. They hid in the bushes and trees alongside the road. When wayfarers went down that road, carrying suitcases, pushing baby buggies, those creeps would jump down on ‘em, rob and terrorize ‘em, and generally act like hoodlums. Well, when the terrible stories about the road made the front-page news, people were afraid to travel to Athens anymore. But what did Theseus know about current events? Diddly squat! But luckily, this situation was made to order for Theseus’s unique talents. He went merrily down that road, and when those burglars and bandits jumped down on him, he heard the leaves rustle and the air move. He whirled around, knocked ‘em about a hundred yards, and hollered, “Gotcha back!” Those perverts were never seen again, and the Athenian Road became a shining example of early urban renewal.

Well, when word got out in Athens about this big hero who was coming to town, folks turned out to cheer his arrival. Meanwhile, Theseus’s daddy, Aegeus, who was now king of Athens and enjoying the company of a girlfriend named Medea, got very worried. He had no idea that the road hero was his very own son. Medea, who did not have a stellar reputation in family relations, convinced Aegeus that this hero might be elected the new king of Athens and that poor ol’ Aegeus would be left crownless, powerless, and penniless. So she hatched a plot to poison the mysterious hero.

When Theseus got to town, Aegeus and Medea greeted him at the city gates and handed him a cup of wine. As Theseus tipped the beverage to his lips, Aegeus recognized the sharp sword and the dusty shoes he had buried so long ago. He realized that this hero was none other than his abandoned son. Aegeus knocked the cup of poison from the boy’s lips and embraced him. “My son, at last I’ve found you!”

It so happened that these were tough times in Athens. A few years back, Athens had gotten into a scuffle with the island of Crete. The Athenians had lost. So now every nine years, as payment to the King of Crete, Athens was required to send seven young men and seven young women to Crete, where they were fed to a monstrous Minotaur. When Theseus heard of this atrocity, he said, “Hey! I’ve got a swell idea! I’m a big-time hero. How about if I go along on the boat this time and just kill that . . . uh . . . that . . . Whaddya call that thing? Oh, year, Minotaur! Yep, I’ll just kill that Minotaur. No problem. Well, so long. See you later . . . uh . . . see you later . . . Whaddya call yourself? Dad! Yep, see you later, Dad!”

The next day, Theseus joined the thirteen other adolescents bound for Crete. The shop was launched under black sails, befitting the occasion. But Theseus promised Aegeus that if the mission was successful, they would return under white sails. Aegeus could look out over the water and know before the ship ever reached shore whether or not his son was alive.

When the ship reached Crete, the young Athenians went ashore, led by Theseus. The first person who greeted them was a beautiful island girl who fell in love with Theseus the moment she laid eyes on him. She looked him up, and she looked him down, and she liked what she saw. Then she looked deep into his eyes, and she said to herself, “Mmm, this boy’s got a few cogs without a matching ratchet.” Theseus was her best hope, so the girl tried not to think about the consequences.

Now this girl was no run-of-the-mill citizen of Crete. She was Ariadne, daughter of King Minos and half-sister to the Minotaur. She walked along next to Theseus and explained to him about the labyrinth where her daddy kept the Minotaur. She told him she was certain that he was strong enough to destroy the Minotaur. But, she said, he could never find his way out of that labyrinth without a little help from her. She’d be happy to provide some assistance, explained Ariadne, if he would take her with him as his wife when he left Crete.

“Sure, Mom . . . uh, sure, Dad . . . uh, sure, Ari-something. Sure, take you with me . . . whatever.”

When they reached the entrance to the labyrinth, Ariadne handed Theseus a golden ball of string. She told him to let that string unwind behind him as he made his way through the maze of passages. Once he killed the Minotaur, all he had to do was follow the string back to her. She said she’d be waiting with her wedding dress and her running shoes.

Theseus led his not-so-merry band of thirteen through the door of the labyrinth, unwinding the golden string as he went. The passageway was dark and dank and narrow, twisting and turning back on itself like a snake. When they reached the innermost part of the maze, Theseus felt the movement of air above him. The bull-headed monster jumped from his hiding place on the wall overhead, snorting and spewing phlegm on the intruders. But Theseus, anticipating the attack, stepped aside and whirled around, and before the Minotaur could lay a hoof on anybody, Theseus knocked him about a hundred yards. “Gotcha back!” he yelled. The Minotaur lay dead, deader than a doornail.

Theseus sat down on the lifeless body of the monster and pouted. “Shucks. Now how in the name of Sam Hill are we supposed to get out of this lousy place?”

His friends looked deep into his eyes and said to themselves, “This boy’s got a few cogs without a matching ratchet.” They could have said a lot of things, but what they did was yell real loud, “The string, stupid, the string!”

Theseus looked down at the ball of string still in his hand. “Sure. Right. I knew that. I was just checking. Come on. Follow me. I’m getting you people outta here!”

They picked up Ariadne at the door, ran for the harbor, and sailed away from the island of Crete at full speed. That night they stopped to rest on the island of Naxos. Ariadne unpacked her wedding frock, and she and Theseus were married by the local justice of the peace. It was the shortest honeymoon in history. Before the crack of dawn, Theseus loaded the crew and the bags back onto the ship and set sail for Athens. Not far out of the harbor, one of his shipmates looked back and yelled, “Ariadne! Theseus, you forgot Ariadne!” Sure enough, there she stood, knee deep in the ocean, still in her nightgown, frantically waving her arms.

“Who?” said Theseus. “Ari-who? Oh, yeah, her. Nice girl. Well, home to Athens. Full-speed ahead!” Would you believe it? He forgot about her. Went off and left her and forgot all about her. And that wasn’t even the worst thing that happened that day.

As the ship approached Athens, Aegeus was standing on a high, rocky cliff gazing out over the horizon. When he saw the vessel, he began to weep, and he threw himself to his death on the rocks below. You want to guess what color the sails were? That’s right – black. Theseus forgot to change them!

That’s how the rest of Theseus’s life went. One faux pas after another. He messed up so many times, nobody bothered to keep track for posterity anymore.

Once he went down to the underworld, thinking he could rescue a beautiful woman named Persephone. Hades caught him, of course, and punished him by making him sit in the Chair of Forgetfulness. What a hoot! Theseus felt right at home. He sat there looking mellow, forgetting who he was and what he was supposed to be doing. But, you see, that Chair of Forgetfulness was a fiendish device. It not only took away your memory, but it also sealed itself to your rear end like Super Glue. Theseus would still be there if it hadn’t been for his pal Hercules who followed him down there, grabbed hold of him, and ripped him out of that chair, leaving part of Theseus still attached. That’s why, by the way, to this very day Theseus’s descendants are known as “half-ass people.”

How that boy Theseus ever got to be a hero to the Greeks is a complete mystery to me. On the one hand, he screwed up just about everything he touched. On the other hand, he did clean up the Athenian Road, and he did rid the world of the Minotaur, and he did bring those thirteen young people home safe to Athens. So I guess you could say he did the best he could for a boy who had a few cogs without a matching ratchet.
```

---

## IC-2141: Thidwick, the Big-Hearted Moose

- Title: Thidwick, the Big-Hearted Moose
- Author (byline): Theo Geisel (aka Dr. Seuss)
- Work: Not specified
- Publisher: Random House
- Publication date as stated: Sept 1948
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1349
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
NOTE: Works by Theo Geisel (aka Dr. Seuss) have been identified as both PROSE and POETRY. Check your tournament rules to determine the category in which this selection should be entered.

Up at the Lake Winna-Bango . . . the far northern shore . . . Lives a huge herd of moose, about sixty or more, And they all go around in a big happy bunch Looking for nice, tender moose-moss to munch.

Up at the lake Winna- Bango, one day, they were lunching, Just strolling along and enjoying their munching . . . (For the moose-moss that day was especially fine) . . . When it happened that Thidwick, the last moose in line, Saw a Bingle Bug sitting. The bug called out, “Hey! It’s such a long road, and it’s such a hot day, Would you mind if I rode on your horns for a way?”

“Of course not!” smiled Thidwick, the Big-Hearted Moose. “I’m happy my antlers can be of some use. There’s room there to spare, and I’m happy to share! Be my guest and I hope that you’re comfortable there!” So the Bingle Bug picked out a nice easy seat and the moose went on looking for moose-moss to eat.

Well . . . An hour or so later The bug heard a squeak, And he heard the small voice. Of a Tree-Spider speak. “I say!” said the spider, “you’ve got a nice place! That moose seems quite friendly, Has such a nice face . . . If I got on, too, Do you think he would mind. . ?”

“Hop aboard!” laughed the bug. “And I think that you’ll find that moose won’t object. He’s the big hearted kind!”

“I accept,” said the spider, with joy and delight.” And he started a web horn to the right.

While the spider was spinning, he heard a gay song and a fresh little Zinn-a- zu bird came along. He stopped. And he stared. And he chirped, “Well! Well! WELL! What a smart place to build! What a great place to dwell! I’ve been living on trees ever since I was born,

But here’s something new! Why not live in a horn! If there’s room there for two, then there’s room there for three!”

“There’s plenty of room!” Laughed the bug. “And it’s free!”

Thidwick stopped walking. What was all that talking? These guests had caught Thidwick the Moose unawares. “Hey!” he called out. “What goes on there upstairs?”

“Just building a nest, sir.” The Zinn-a-zu said, and began yanking hairs out of poor Thidwick’s head. And he plucked out exactly two hundred and four! “Don’t worry,” he laughed. “you can always grow more!”

Then he dozed off to sleep in his fine moose hair nest. “This bird,” murmured Thidwick “is sort of a pest! But I’m a good sport, so I’ll just let him rest, for a host, above all, must be nice to his guest. Besides, now, it’s getting quite late in the day and surely tomorrow they’ll all go away.” But, alas! The next morning the sun’s early light brought to Thidwick’s sad eyes a most unwelcome sight…

“Meet my wife!” said the bird. “I was married last night. “And, perhaps by the way, I should mention to you that her uncle is coming to live with us, too. You’re a very fine host so I knew you’d be willing. . .” Then the uncle, a woodpecker, started in drilling!

All Thidwick’s friends shouted, “GET RID OF THOSE PESTS!” “I would, but I can’t.” sobbed poor Thidwick. “They’re guests!”

“Guests indeed!” his friends answered and all of them frowned. “If those are your guests, we don’t want you around! You can’t stay with us, ’cause you’re just not our sort!” And they all turned their backs and walked off with a snort.

Now the big friendless moose walked alone and forlorn, with four great big woodpecker holes in his horn.

“What holes!” whispered Hernan, a squirrel, who spied ’em. “What holes to hide nuts in! Hmmm! Mind if I tried ’em?”

“They’re yours!” called the woodpecker. “Get right inside ’em! This big hearted moose runs a public hotel! Bring your nuts! Bring your wife! Bring your children as well!” So the whole squirrel family all jumped on, pell mell.

And the very next thing the poor animal knew, a Bobcat and turtle were living there, too! NOW what was the big-hearted moose going to do?

Well what would YOU do if it happened to YOU?

You couldn’t say “Skat!” ’cause that wouldn’t be right. You couldn’t shout “Scram!” ’cause that isn’t polite.

A host has to put up with all kinds of pests, for a host, above all, must be nice to his guests. So you’d try hard to smile, and you’d try to look sweet and you’d go right on looking for moose-moss to eat.

But now it was winter and that wasn’t easy, for moose-moss gets scarce when the weather gets freezy.

The food was soon gone on the cold northern shore of Lake Winna-Bango. There just was no more! And all Thidwick’s friends swam away in a bunch to the south of the lake where there’s moose-moss to munch. He watched the herd leaving. And then Thidwick knew he’d starve if he stayed here! He’d have to go, too!

He stepped in the water. Then, oh! What a fuss!

“STOP!” screamed his guests. “You can’t do this to us! These horns are our home and you’ve no right to take our home to the far distant side of the lake!”

“Be fair!” Thidwick begged, with a lump in his throat.

“We’re fair,” said the bug. “We’ll decide this by vote. All those in favor of going, say ‘AYE,’ all those in favor of staying say ‘NAY’.”

“AYE!” shouted Thidwick, but when he was done . .

“NAY!” they all yelled. He lost ’leven to one.

“We win!” screamed the guests, “by a very large score!” And poor, starving Thidwick climbed back on the shore. Then, do you know what those pests did? They asked in some more! They asked in a fox, who jumped in from the trees, they asked in some mice and they asked in some fleas. They asked a big bear in and then, if you please, came a swarm of three hundred and sixty-two bees!

Poor Thidwick sank down, with a groan, to his knees. And then, THEN came something that made his heart freeze.

Bullets came zinging right past Thidwick’s face! Guns were bang-binging all over the place!

“Get that moose! Get that moose!” Thidwick heard a voice call. “Fire again and again and shoot straight one and all! We must get his head for the Harvard club wall!”

Thidwick took to his heels with that load on his head! With five hundred pounds on his horns, the moose fled! He could have run faster without all those pests, but a host, above all, must be nice to his guests.

Up canyon! Off cliff! Over wild rocky trail! With bullets bang-bouncing around him like hail! Up gully! Through gulch! And down slippery sluice, with his hard-hearted guests raced the soft-hearted moose!

Then finally they had him! Because of those pests, he had run out of luck, because of those guests on his horns, he was stuck!

He gasped! He felt faint! And the whole world grew fuzzy! Thidwick was finished, completely . . .or WAS he. . . ? Finished…? Not Thidwick! DECIDEDLY NOT! It’s true, he was in a most terrible spot, But NOW he remembered a thing he’d forgot! A wonderful something that happens each year to the horns of all moose and the horns of all deer. Today was the day, Thidwick happened to know . . . That OLD horns come off so that NEW ones can grow! And he called to the pests on his horns as he threw ’em, “you wanted my horns; now you’re quite welcome to ’em! Keep ’em! They’re yours! As for ME, I shall take myself to the far distant side of the lake!”

And he swam Winna-Bango and found his old bunch, and arrived just in time for a wonderful lunch at the south of the lake, where there’s moose-moss to munch.

His old horns today are where you knew they would be. His guests are still on them, all stuffed, as they should be.
```

---

## IC-2142: This is How We Live

- Title: This is How We Live
- Author (byline): Ellen DeGeneres
- Work: The Funny Thing Is, Pgs 59-66
- Publisher: Simon and Schuster
- Publication date as stated: Oct 2003
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ELLEN
- Teaser before the introduction: Yes
- Spoken words (computed): 1700
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ellen DeGeneres
Book: The Funny Thing Is, Pgs 59-66
ISBN: 978-0743247610
Publisher: Simon and Schuster
Date (Month/Year): Oct 2003
```

### Introduction (context only: never use it for content warnings)

```text
This is How We Live by Ellen DeGeneres
```

### Performance text (classify this)

```text
ELLEN: (Pg 59-66) Everyone likes to talk about how

advancements in technology will change the way we live

forever. Frankly, I think modern technology is hurting

us. I really do.

If you want to know the truth, I blame the microwave for

most of our problems. Anything that gets food that hot

without fire is from the devil. If you don’t believe me,

put a Hot Pocket in your microwave for three or four

minutes, then pop that thing in your mouth. If that’s not

Hell, my friend, I don’t know what is.

ELLEN: Everyone likes to talk about how advancements in technology will change the way we live forever. Frankly, I think modern technology is hurting us. I really do.

If you want to know the truth, I blame the microwave for most of our problems. Anything that gets food that hot without fire is from the devil. If you don’t believe me, put a Hot Pocket in your microwave for three or four minutes, then pop that thing in your mouth. If that’s not Hell, my friend, I don’t know what it.

Modern life requires hardly any physical activity. We just push a button and stand there. Take the car window. Someone decided that having to crank the window down yourself was too hard. “I don’t want to churn butter, I just want fresh air!” So we got a button to do it.

We’re just so lazy. We used to have breath mints. Now we have breath strips that just dissolve on our tongue. Can we not suck anymore?

Yes, we’re lazy. Yet we also can’t seem to sit still. So we’ve started making things like GO-GURT. That’s yogurt for people on the go. Let me ask you, was there a big mobility problem with yogurt before? How time-consuming was it, really?

“Hello? . . . Oh, hi, Tom . . . I’ve been dying to see that movie . . . Umm, no . . . I just opened up some yogurt . . . Yeah, I’m in for the night . . . No, not even later – it’s the kind with fruit on the bottom. Well, have fun. Thanks anyway.”

Power bars were made for mountain-climbing expeditions and hiking, not really made to be eaten in the car on the way to the mall. Is it really that much faster and more convenient? It takes longer to chew one bit of those things than it takes to make an entire sandwich. I don’t know what they’re made from, but you could insulate a house with that stuff.

There are certain things that they’re coming up with that I just don’t think we need. Top of the list is that moving sidewalk you find in airports. It’s like a little ride in the middle of nowhere, but I don’t know what function it really serves. I mean, it’s fun because it moves, so if you walk while you’re on it you’re almost like the Bionic Woman, just flying past the people trudging beside you on the ground. But you know how hard it is to adjust to walking again once you get off that thing? And what about those people who get on there and just stand? I guess we have to thank God they found the moving sidewalk. Without it, I don’t know how they’d get anywhere.

You’d think with all these innovations that are speeding things up for us and moving us along, people would be early-or at least on time-when they’re going places. But somehow, everybody’s still always late. And people always say the same thing when they finally show up after you’ve been waiting for them. “Oh, sorry. Traffic.”

“Really? How do you think I got here? Helicoptered in? I allow for it.”

[And] What has happened to toilet paper in public bathrooms? It’s not even one-ply anymore, is it? It’s a sheer suggestion of toilet paper. It’s an innuendo. It’s like prosciutto, it’s so thin. And if you’re in a public bathroom and it’s a brand-new roll that hasn’t gotten started yet, just try to find the start of that toilet paper roll. Fist you turn it slowly. You think, surely I’ve gone around once or twice by now. Then you go fast. Maybe the wind will open up the first flap. Then you turn it the other way, thinking maybe you’re going in the wrong direction. And back to the slow again. And then you find it, and it’s glued down. So then you try to pull it apart but only a quarter of an inch separates and the rest stays glued. So you’re pulling and pulling and soon you’ve got a five-foot-long quarter-of-an-inch strip. I don’t want a streamer, I want toilet paper! So now one side is fully intact and you’ve got a groove cut out on the other side. Then you use your finger to try to even it out, but you never get it exactly even, so then you finally just claw at it like a wild animal. “Jesus, I just want toilet paper!”

On the other hand, some things that don’t need to be made easier are being made easier. They’re making these automated toilets that flush entirely on their own schedule. Sometimes they just go off randomly. You’re still sitting down and suddenly it just flushes. “How dare you! I’ll decide when I’m done!” And then other times it won’t go off when you want it to. You sand up and stare at the toilet. Sometimes you have to fake it out. You sit back down . . .stand up! Sit down . . . stand up! Then you try tiptoeing away as if you’re leaving. Nothing works.

Technology has done one beautiful thing for us. It’s called the cell phone. There is now not one place in the world where a cell phone is not going off. And every cell phone now has its own little song. Good thing we got rid of those obnoxious rings, isn’t it?

When you’re on a cell phone, you can’t ever have a full conversation. Usually reception is terrible, and somehow it’s only bad on your side. The person talking to you has no idea that you have bad reception. They’re rambling on and on and you’ve got your finger jammed in your ear. You’re shushing people on the street, ducking behind a Dumpster, putting your head between your knees, just so you can hear about your friend’s new haircut. “What about the bangs? Are they shorter? Are the bangs shorter? THE BANGS!!”

At least if there’s static you have some clue that you may get cut off. There’s nothing worse than when you have crystal-clear reception and you’ve been rambling on for who knows how long, only to find out that the connection cut out who knows how long ago. Then you get paranoid. You’re scared to talk too long ever again. Next time you’re on the phone you become obsessed with checking. “So we were going to go to the cheese shop . . . Hello? Okay . . . And we knew we were having white wine. . . Still there? All right. And I thought, what kind of cheese would go with. . .? Did I lose you? Okay . . . And I like Muenster . . . “

Even if you’re on a regular phone at home, you’ll be interrupted somehow. You’ll be interrupted by call-waiting most likely. Call-waiting was intended as a convenience, but let’s face it – it’s really turned into a mini People’s Choice awards. You find out right away who wins or loses. You’re having a pleasant conversation with someone you think is a good friend, and you hear the click, and you’re confident that they’re going to come back to you. Then they come back and say, “I’ve got to take this other call.” And you know what that means. They just said to the other person, “Let me get rid of this other call.” That’s what you just became: a call to get rid of. Then you learn to trick them the next time, when they say they’ve got to check on the other call. “Hey, when you come back, remind me to tell you something that somebody said about you! . . . Hello?”

Of course, you don’t have to pick up call-waiting. You can get voice mail. Voice mail will pick it up for you. My favorite voice mail is the one where you insert your name into a robotic message, and you end up sounding more like a robot than the robot itself. “Your call has been forwarded to an automatic voice message system. El-len [or insert your name here] is not available.” Is that how I say my name? Like HAL from 2001: A Space Odyssey? “Yeah, I’d like to make reservations for dinner tonight, there’s four of us, and the name is El-len [or insert your name here].”

Phones have gone through such an evolution. Now we have this wireless technology that lets us talk to anybody, anywhere, anytime. Think about how far phones have come. You’ll remember there was a time when there was one phone in the house, when cord was just being invented. There was a shortage of cord back then. Maybe you had a foot or two from the wall to the phone. Back then, when you said you were on the phone, you were on the phone.

Then the kitchen wall phone came along, usually a lovely mustard or an avocado green. It had a ninety-foot-long cord that allowed you to talk all round the house, cleaning tables, wrapping around dogs, so that by the time you hung up the phone, it had become this tangled wire of cord confusion. But what was fun about it was that every once in a while you would hold the phone upside down by the cord and let that thing spin and spin, around and around, till it found its center. Good times.

One surefire sign that things are going the wrong way? Now we have the hands-free phone so you can concentrate on the thing you’re really supposed to be doing. My thought is this: Chances are, if you need both of your hands to do something, your brain should be in on it too!
```

---

## IC-2143: This is Why I’ll Never be an Adult (From Hyperbole and a Half)

- Title: This is Why I’ll Never be an Adult (From Hyperbole and a Half)
- Author (byline): Allie Brosh
- Work: Hyperbole and a Half
- Publisher: Touchstone Books
- Publication date as stated: Oct 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 696
- Already set (do not supply): none

### Source block (context only)

```text
Author: Allie Brosh
Book: Hyperbole and a Half
ISBN: 978-1451666175
Publisher: Touchstone Books
Date (Month/Year): Oct 2013
```

### Introduction (context only: never use it for content warnings)

```text
Grocery shopping ??? My parents' fridge is already stocked. Paying the cell phone bill? I’m on my parents’ plan. Health insurance? Ditto – at least until I’m 26. Growing up?? Optional because, for many of us, it is.

But there will come a time when you are suddenly an adult. You're definitely not ready for it and you feel like you barely got any warning, but there it is – you're an adult. Deal with it. Enter the "real world."

It’s called Adulting: (It’s a real word – Adopted into the Dictionary officially in 2014. Adulting: the practice of behaving in a way characteristic of a responsible adult, especially the accomplishment of mundane but necessary tasks. In fact, Amazon has a multitude of “ADULTING” guides for our clueless generation, because guess what they don’t teach you in school? ADULTING!

This is Why I’ll never be an Adult from Hyperbole and a Half by Allie Brosh
```

### Performance text (classify this)

```text
NOTE: Text shown in red is not in the original text and has been added for transition/clarification purposes.

I have repeatedly discovered that it is important for me not to surpass my capacity for responsibility. Over the years, this capacity has grown, but the results of exceeding it have not changed.

Normally, my capacity is exceeded gradually, through the accumulation of simple, daily tasks.

My productivity is directly related to my level of responsibility.

• Stage 1: Taking care of only the very basics

necessary to survival (eating, sleeping, breathing)

– I’m doing pretty well! I can breathe and beat

my heart like a champion!

But a few times a year, I spontaneously decide that I'm ready to be a real adult. I don't know why I decide this; it always ends terribly for me. But I do it anyway.

• Stage 2: A few very minor tasks, like grocery

shopping and brushing my hair. – Look at me go!

I’m actually getting stuff done!

I sit myself down and tell myself how I'm going to start cleaning the house every day and paying my bills on time and replying to emails before my inbox reaches quadruple digits. Schedules are drafted. Day-planners are purchased. I stock up on fancy food because I'm also planning on morphing into a master chef and actually cooking instead of just eating nachos for dinner every night. I prepare for my new life as an adult like some people prepare for the apocalypse.

• Stage 3: One major responsibility, like (feeding

the dog) – I’M SUCCESSFUL!!!!!

The first day or two of my plans usually goes okay.

• Email!

• Go to the bank like an adult

• Grocery Shopping

• Clean all the things!

For a little while, I actually feel grown-up and responsible. I strut around with my head held high, looking the other responsible people in the eye with that knowing glance that says "I understand. I'm responsible now too. Just look at my groceries."

At some point, I start feeling self-congratulatory. This is a mistake.

I begin to feel like I've accomplished my goals. It's like I think that adulthood is something that can be earned like a trophy in one monumental burst of effort and then admired and coveted for the rest of one's life.

(Show trophy) That right there is my ability to be responsible. I won it when I was 25.

• Stage 4: Now there are a few more things –

(paying bills, cleaning the kitchen and bathroom,

going to the bank) – Wait . . . what is this? I have

to go to the bank? What am I, some sort of

wizard?

• Stage 5: Now even a few more – (renewing my

driver’s license, laundry, changing the oil in my

car) – I did three things yesterday! Now I’m

supposed to keep doing things? It’s like the

things never end!

• Stage 6: One more . . . (April 15 – Taxes are due

today! And I’m 26 – I have to find a job with

health insurance) – SYSTEM FAILURE!

What usually ends up happening is that I completely wear myself out. Thinking that I've earned it, I give myself permission to slack off for a while and recover. Since I've exceeded my capacity for responsibility in such a dramatic fashion, I end up needing to take more recovery time than usual. This is when the guilt-spiral starts.

The longer I procrastinate on returning phone calls and emails, the more guilty I feel about it. The guilt I feel causes me to avoid the issue further, which only leads to more guilt and more procrastination. It gets to the point where I don't email someone for fear of reminding them that they emailed me and thus giving them a reason to be disappointed in me.

Then the guilt from my ignored responsibilities grows so large that merely carrying it around with me feels like a huge responsibility. It takes up a sizable portion of my capacity, leaving me almost completely useless for anything other than consuming nachos and surfing the internet like an attention-deficient squirrel.

At some point in this endlessly spiraling disaster, I am forced to throw all of my energy into trying to be an adult again, just to dig myself out of the pit I've fallen into. The problem is that I enter this round of attempted adulthood already burnt out from the last round. I can't not fail. (in an utterly defeated and small, sad voice)

• email

• bank

• grocery shopping

• clean all the things?

It always ends the same way. Slumped and haggard, I contemplate the seemingly endless tasks ahead of me.

Work? . . . .

And then I rebel. No . . . . (re-energized) INTERNET! . . . Forever . . .
```

---

## IC-2144: The Three Co-Dependent Goats Gruff

- Title: The Three Co-Dependent Goats Gruff
- Author (byline): James Finn Garner
- Work: Politically Correct Bedtime Stories
- Publisher: John Wiley and Sons Inc
- Publication date as stated: Apr 1994
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 943
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
Once on a lovely mountainside lived three goats who were related as siblings. Their name was Gruff, and they were a very close family. During the winter months they lived in a lush, green valley, eating grass and doing other things in a naturally goatish manner. When summer came they would travel up the mountainside to where the pasture was sweeter. This way they did not overgraze their valley and kept their ecological footprints as small as possible.

To get to this pasture, the goats had to cross a bridge over a wide chasm. When the first days of summer came, one goat set out to cross the bridge. This goat was the least chronologically accomplished of the siblings and thus had achieved the least superiority in size. When he reached the bridge, he lashed on his safety helmet and grasped the handrail. But as he began to cross, a menacing growl came from beneath the bridge.

Over the railing and onto the bridge leaped a troll – hairy, dirt-accomplished, and odour-enhanced. “Yaaarrrgh!” intoned the troll. “I am the keeper of this bridge, and while goats may have the right to cross it, I’ll eat any that try!”

“But why, Mr. Troll?” bleated the goat.

“Because I’m a troll, and proud of it. I have a troll’s needs, and those needs include eating goats, so you better respect them or else.”

The goat was frightened. “Certainly, sir,” he stammered. “If eating me would help you become a more complete troll, nothing would please me more. But I really can’t commit to that course of action without first consulting my siblings. Will you excuse me?” And the goat ran back to the valley.

Next, the middle sibling goat came up to the bridge. This goat was more chronologically advanced than the first goat and so enjoyed an advantage in size (although this did not make him a better or more deserving goat). He was about to cross the bridge when the troll stopped him.

“Nature has made me a troll,” he said. “and I embrace my trollhood. Would you deny me my right to live the life of a troll as fully and effectively as I can?”

“Me? Never!” exclaimed the goat proudly.

“Then stand still there while I come over and eat you up. And don’t try to run away; I would take that as a personal affront.” He began to invade the goat’s caprinal space.

“However,” blurted the goat. “I have a very close family, and it would be selfish of me to allow myself to be eaten without asking their opinion. I have respect for their feelings, too. I would hate to think that my absence would cause them any emotional stress, if I hadn’t first . . . “

“Go then!” screamed the troll.

“I’ll rush back here as soon as we reach a consensus,” the goat said, “for it’s not fair to keep you in suspense.”

“You’re too kind,” signed the troll, and the goat ran back to the valley. As his hunger grew, the troll began to feel a real grievance towards the goats. If he didn’t get to eat at least one of them, he was determined to go to the authorities.

When the third goat came to the bridge, the troll discovered that he was nearly twice the troll’s size, with large, sharp horns and hard, heavy hooves. The troll felt his physical-intimidation prerogative fading fast. As fear turned his insides into jelly, the troll sank to his knees and pleaded, “Oh, please, please forgive me! I was using you and your goat siblings for my own selfish ends. I don’t know what drove me to it, but I’ve seen the error of my ways.”

The goat, too, got down on what passed for knees in goats and said, “Now, now, you can’t take all the blame for yourself. Our presence and supreme edibility put you in this situation. My siblings and I all feel terrible. Please, you must forgive us.”

The troll began to sob. “No, no, it’s all my fault. I threatened and bullied you all, just for the sake of my own survival. How selfish I was!”

But the goat would have none of this. “we were the selfish ones. We only wanted to save our own skins, and we totally neglected your needs. Please, eat me now!”

“No,” the troll said, “you must butt me off this bridge for my insensitivity and selfishness.”

“I’ll do no such thing,” said the goat, “since we all tempted you in the first place. Here, have a chomp. Go ahead.”

“I’m telling you,” the troll insisted standing up, “I’m the guilty one here. Now, knock me off this bridge and be quick about it!”

“Look,” said the goat, rearing to his full height, “no one is going to take away my blame for this, not even you, so eat me before I pop you in the nose.”

“Don’t play guiltier-than-thou with me, Hornhead!”

“Hornhead?” You smelly hairball! I’ll show you guilt!” And with that, they wrestled and bit and punched and kicked as each sought to don the mantle of blame.

The other two goats bounded up to the bridge and sized up the fight. Feeling guilty at not accepting enough of the blame, they joined the others in a whirling ball of hair, hooves, horns, and teeth. But the little bridge was not built to carry such weight. It shook and swayed and finally buckled, hurling the troll and the three codependent goats Gruff into the chasm. On their way down, the each felt relieved that they would finally get what they deserved, plus as a bonus, a little extra guilt for the fate of the others.
```

---

## IC-2145: To Any Would-Be Terrorists

- Title: To Any Would-Be Terrorists
- Author (byline): Naomi Shihab Nye
- Work: 75 Readings Plus
- Publisher: McGraw Hill
- Publication date as stated: July 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1871
- Already set (do not supply): none

### Source block (context only)

```text
Author: Naomi Shihab Nye
Book: 75 Readings Plus
ISBN: 978-0073125084
Publisher: McGraw Hill
Date (Month/Year): July 2006
```

### Introduction (context only: never use it for content warnings)

```text
Soon after the attacks of September 11, 2001, Naomi Shihab Nye wrote "A Letter to Any Would Be Terrorists." Not knowing what to do with it, she emailed the letter to five friends and wrote, "just send it anywhere." The letter spread, becoming published in anthologies, newspapers as far as Beirut, even, a friend tells her, posted on the wall of a Buddhist temple in San Francisco. This is that letter . .
```

### Performance text (classify this)

```text
To Any Would-Be Terrorists:

I am sorry I have to call you that, but I don't know how else to get your attention. I hate that word. Do you know how hard some of us have worked to get rid of that word, to deny its instant connection to the Middle East? And now look. Look what extra work we have. Not only did your colleagues kill thousands of innocent, international people in those buildings and scar their families forever, they wounded a huge community of people in the Middle East, in the United States and all over the world. If that's what they wanted to do, please know the mission was a terrible success, and you can stop now.

Because I feel a little closer to you than many Americans could possibly feel, or ever want to feel, I insist that you listen to me. Sit down and listen. I know what kinds of foods you like. I would feed them to you if you were right here, because it is very very important that you listen. I am humble in my country's pain and I am furious.

My Palestinian father became a refugee in 1948. He came to the United States as a college student. He is 74 years old now and still homesick. He has planted fig trees. He has invited all the Ethiopians in his neighborhood to fill their little paper sacks with his figs. He has written columns and stories saying the Arabs are not terrorists, he has worked all his life to defy that word. Arabs are businessmen and students and kind neighbors. There is no one like him and there are thousands like him - gentle Arab daddies who make everyone laugh around the dinner table, who have a hard time with headlines, who stand outside in the evenings with their hands in their pockets staring toward the far horizon.

I am sorry if you did not have a father like that. I wish everyone could have a father like that.

My hard-working American mother has spent 50 years trying to convince her fellow teachers and choir mates not to believe stereotypes about the Middle East. She always told them, there is a much larger story. If you knew the story, you would not jump to conclusions from what you see in the news. But now look at the news. What a mess has been made. Sometimes I wish everyone could have parents from different countries or ethnic groups so they would be forced to cross boundaries, to believe in mixtures, every day of their lives. Because this is what the world calls us to do. WAKE UP!

The Palestinian grocer in my Mexican-American neighborhood paints pictures of the Palestinian flag on his empty cartons. He paints trees and rivers. He gives his paintings away. He says, "Don't insult me" when I try to pay him for a lemonade. Arabs have always been famous for their generosity. Remember? My half-Arab brother with an Arabic name looks more like an Arab than many full-blooded Arabs do and he has to fly every week.

My Palestinian cousins in Texas have beautiful brown little boys. Many of them haven't gone to school yet. And now they have this heavy word to carry in their backpacks along with the weight of their papers and books. I repeat, the mission was a terrible success. But it was also a complete, total tragedy and I want you to think about a few things.

1. Many people, thousands of people, perhaps even millions of people, in the United States are very aware of the long unfairness of our country's policies regarding Israel and Palestine. We talk about this all the time. It exhausts us and we keep talking. We write letters to newspapers, to politicians, to each other. We speak out in public even when it is uncomfortable to do so, because that is our responsibility. Many of these people aren't even Arabs. Many happen to be Jews who are equally troubled by the inequity. I promise you this is true. Because I am Arab-American, people always express these views to me and I am amazed how many understand the intricate situation and have strong, caring feelings for Arabs and Palestinians even when they don't have to. Think of them, please: All those people who have been standing up for Arabs when they didn't have to. But as ordinary citizens we don't run the government and don't get to make all our government's policies, which makes us sad sometimes. We believe in the power of the word and we keep using it, even when it seems no one large enough is listening. That is one of the best things about this country: the free power of free words. Maybe we take it for granted too much. Many of the people killed in the World Trade Center probably believed in a free Palestine and were probably talking about it all the time.

But this tragedy could never help the Palestinians. Somehow, miraculously, if other people won't help them more, they are going to have to help themselves. And it will be peace, not violence, that fixes things. You could ask any one of the kids in the Seeds of Peace organization and they would tell you that. Do you ever talk to kids? Please, please, talk to more kids.

2. Have you noticed how many roads there are? Sure you have. You must check out maps and highways and small alternate routes just like anyone else. There is no way everyone on earth could travel on the same road, or believe in exactly the same religion. It would be too crowded, it would be dumb. I don't believe you want us all to be Muslims. My Palestinian grandmother lived to be 106 years old, and did not read or write, but even she was much smarter than that. The only place she ever went beyond Palestine and Jordan was to Mecca, by bus, and she was very proud to be called a Hajji and to wear white clothes afterwards. She worked very hard to get stains out of everyone's dresses -- scrubbing them with a stone. I think she would consider the recent tragedies a terrible stain on her religion and her whole part of the world. She would weep. She was scared of airplanes anyway. She wanted people to worship God in whatever ways they felt comfortable. Just worship. Just remember God in every single day and doing. It didn't matter what they called it. When people asked her how she felt about the peace talks that were happening right before she died, she puffed up like a proud little bird and said, in Arabic, "I never lost my peace inside." To her, Islam was a welcoming religion. After her home in Jerusalem was stolen from her, she lived in a small village that contained a Christian shrine. She felt very tender toward the people who would visit it. A Jewish professor tracked me down a few years ago in Jerusalem to tell me she changed his life after he went to her village to do an oral history project on Arabs. "Don't think she only mattered to you!" he said. "She gave me a whole different reality to imagine - yet it was amazing how close we became. Arabs could never be just a "project" after that."

Did you have a grandmother or two? Mine never wanted people to be pushed around. What did yours want? Reading about Islam since my grandmother died, I note the "tolerance" that was "typical of Islam" even in the old days. The Muslim leader Khalid ibn al-Walid signed a Jerusalem treaty which declared, "in the name of God, you have complete security for your churches which shall not be occupied by the Muslims or destroyed." It is the new millenium in which we should be even smarter than we used to be, right? But I think we have fallen behind.

3. Many Americans do not want to kill any more innocent people anywhere in the world. We are extremely worried about military actions killing innocent people. We didn't like this in Iraq, we never liked it anywhere. We would like no more violence, from us as well as from you. HEAR US! We would like to stop the terrifying wheel of violence, just stop it, right on the road, and find something more creative to do to fix these huge problems we have. Violence is not creative, it is stupid and scary and many of us hate all those terrible movies and TV shows made in our own country that try to pretend otherwise. Don't watch them. Everyone should stop watching them. An appetite for explosive sounds and toppling buildings is not a healthy thing for anyone in any country. The USA should apologize to the whole world for sending this trash out into the air and for paying people to make it.

But here's something good you may not know - one of the best-selling books of poetry in the United States in recent years is the Coleman Barks translation of Rumi, a mystical Sufi poet of the 13th century, and Sufism is Islam and doesn't that make you glad?

Everyone is talking about the suffering that ethnic Americans are going through. Many will no doubt go through more of it, but I would like to thank everyone who has sent me a consolation card. Americans are usually very kind people. Didn't your colleagues find that out during their time living here? It is hard to imagine they missed it. How could they do what they did, knowing that?

4. We will all die soon enough. Why not take the short time we have on this delicate planet and figure out some really interesting things we might do together? I promise you, God would be happier. So many people are always trying to speak for God - I know it is a very dangerous thing to do. I tried my whole life not to do it.

But this one time is an exception. Because there are so many people crying and scarred and confused and complicated and exhausted right now - it is as if we have all had a giant simultaneous break-down. I beg you, as your distant Arab cousin, as your American neighbor, listen to me. Our hearts are broken, as yours may also feel broken in some ways we can't understand, unless you tell us in words. Killing people won't tell us. We can't read that message. Find another way to live. Don't expect others to be like you. Read Rumi. Read Arabic poetry. Poetry humanizes us in a way that news, or even religion, has a harder time doing. A great Arab scholar, Dr. Salma Jayyusi, said, "If we read one another, we won't kill one another." Read American poetry. Plant mint. Find a friend who is so different from you, you can't believe how much you have in common. Love them. Let them love you. Surprise people in gentle ways, as friends do. The rest of us will try harder too. Make our family proud.
```

---

## IC-2146: To Hell with Dying

- Title: To Hell with Dying
- Author (byline): Alice Walker
- Work: Not specified
- Publisher: Voyager Books
- Publication date as stated: Feb 1993
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1673
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alice Walker
ISBN: 978-0152890742
Publisher: Voyager Books
Date (Month/Year): Feb 1993
```

### Introduction (context only: never use it for content warnings)

```text
Our society is more generationally stratified than ever before, making the elderly feel particularly alienated. According to one study from the University of California San Francisco, 43% of seniors report feeling lonely, which comes with a staggering 59% higher risk of declining health and a 45% higher risk of death. In short, the epidemic of loneliness among the elderly isn’t just an emotional travesty, it’s a health hazard.

But love can always defeat loneliness. It can give those who are struggling a reason to live when the feeling of defeat is overpowering. Never underestimate the healing power of love.

To Hell with Dying by Alice Walker
```

### Performance text (classify this)

```text
"To hell with dying," my father would say. "These children want Mr. Sweet!" Mr. Sweet was a diabetic and an alcoholic and a guitar player and lived down the road from us on a neglected cotton farm. "To hell with dying, man," "These children want Mr. Sweet!" At a signal from Father they would come crowding around the bed and throw themselves on the covers, and whoever was the smallest at the time would kiss him all over his wrinkled brown face and tickle him so that he would laugh all down in his stomach, and his mustache, which was long and sort of straggly, would shake like Spanish moss.

Mr. Sweet had been ambitious as a boy, wanted to be a doctor or lawyer or sailor, only to find that black men fare better if they are not. Since he could become none of these things he turned to fishing as his only earnest career and playing the guitar as his only claim to doing anything extraordinarily well.

Mr. Sweet used to call me his princess, and I believed it. He made me feel pretty at five and six, and simply outrageously devastating at the blazing age of eight and a half. When he came to our house with his guitar the whole family would stop whatever they were doing to sit around him and listen to him play. He liked to play "Sweet Georgia Brown," and all sorts of sweet, sad, wonderful songs., Sometimes he would cry and that was an indication that he was about to die again. And so we would all get prepared, for we were sure to be called upon.

I was seven the first time I remember actually participating in one of Mr. Sweet's "revivals" - my parents told me I had participated before; I had been the one chosen to kiss him and tickle him long before I knew the rite of Mr. Sweet's rehabilitation. He had come to our house, it was a few years after his wife's death and he was very sad. He sat on the floor next to me and my older brother, the rest of the children were grown up and lived elsewhere, and he began to play his guitar and cry. When he was leaving, my mother said to us that we'd better sleep light that night for we'd probably have to go over to Mr. Sweet's before daylight. And we did. For soon after we had gone to bed one of the neighbors knocked on our door and called my father and said that Mr. Sweet was sinking fast and if he wanted to get in a word before the crossover, he'd better shake a leg and get over to Mr. Sweet's house. As soon as we heard the cry we got up, my brother and I and my mother and father, and put on our clothes. We hurried out of the house and down the road for we were always afraid that we might someday be too late, and Mr. Sweet would get tired of dallying.

When we got to the house, a very poor shack really, we found the front room full of neighbors and relatives and someone met us at the door and said it was all very sad that old Mr. Sweet Little was about to kick the bucket. My parents were advised not to take my brother and me into the "death room," seeing we were so young and all, but we dashed in without giving his warning a second thought. I was almost in tears, for these deaths upset me fearfully, and the thought of how much depended on me and my brother made me very nervous.

The doctor was bending over the bed and turned back to tell us for at least the tenth time in the history of my family, that, alas, old Mr. Sweet Little was dying and that children had best not see the face of implacable. My father pushed him rather abruptly out of the way saying, as he always did and very loudly for he was saying it to Mr. Sweet, "To hell with dying, man, these children want Mr. Sweet" - which was my cue to throw myself upon the bed and kiss Mr. Sweet under the eyes and around the collar of his nightshirt where he smelled so strongly of all sorts of things, mostly liniment. I was very good at bringing him around, for as soon as I saw that he was struggling to open his eyes I knew he was going to be all right.

Once, though, I got a tremendous scare, for he could not open his eyes and later I learned that he had had a stroke and that one side of his face was stiff and hard to get into motion. When he began to smile, I could tickle him in earnest because I was sure that nothing would get in the way of his laughter.

When we were sure he would listen to us, we would ask him why he was in bed and when he was coming to see us again and could we play his guitar, which more than likely would be leaning against the bed. His eyes would get all misty and he would sometimes cry out loud, but we never let it embarrass us, for he knew that we loved him.

My brother was very generous in all this, he let me do all the revival-ing - he had done it for years before I was born and so he was glad to be able to pass it on to someone new. What he would do while I talked to Mr. Sweet was pretend to play the guitar, in fact he pretended that he was a young version of Mr. Sweet, and it always made Mr. Sweet glad to think that someone wanted to be like him.

We were desperately afraid that he was just going to take off one day and leave us.

It did not occur to us that we were doing anything special; we had not learned that death was final when it did come. We thought nothing of triumphing over it so many times, and in fact became a trifle contemptuous of people who let themselves be carried away. It did not occur to us that if our father had been dying we could not have stopped it, that Mr. Sweet was the only person over whom we had power.

When Mr. Sweet was in his eighties, I was studying in the university many miles from home. By this time, he not only had a mustache but a long flowing snow-white beard, which I combed and braided. He was very peaceful, fragile, gentle, and the only jarring note about him was his old steel guitar, which he still played in the old sad, sweet, down-home blues way.

On Mr. Sweets ninetieth birthday I was finishing my doctorate in Massachusetts. That morning I got a telegram telling me that Mr. Sweet was dying again and could I please drop everything and come home. Of course, I could. My dissertation could wait. Within hours I was speeding along the dusty road to Mr. Sweet's.

The house was more dilapidated than when I was last there, barely a shack, but it was overgrown with yellow roses, which my family had planted many years ago. The air was heavy and sweet and very peaceful. I felt strange walking through the gate and up the old rickety steps. But the strangeness left me as I caught sight of the long white beard flowing down the thin body over the familiar quilt coverlet. Mr. Sweet!

His eyes were closed tight and his hands, crossed over his stomach, were thin and delicate. I looked around at my parents and was surprised to see that my father and mother also looked old and frail. My father, his own hair very gray, leaned over the quietly sleeping old man, who, incidentally, smelled still of wine and tobacco, and said, as he'd done so many times, "To hell with dying, man! My daughter is home to see Mr. Sweet!" I bent down and gently stroked the closed eyes and gradually they began to open. The closed lips twitched a little, then parted in a warm, slightly embarrassed smile. Mr. Sweet could see me and he recognized me and his eyes looked very spry and twinkly for a moment. I put my head down on the pillow next to his and we just looked at each other for a long time. He began to trace my hair line with a thin, smooth finger. I closed my eyes when his finger halted above my ear. His hand stayed cupped around my cheek. When I opened my eyes, sure that I had reached him in time, his were closed.

Even at twenty-four how could I believe that I had failed? That Mr. Sweet was really gone? But when I looked at my parents, I saw that they were holding back tears. They had loved him dearly. He was like a piece of rare and delicate china which was always being saved from breaking and which finally fell. I looked long at the old face, the wrinkled forehead, the hands that still reached out to me. Soon I felt my father pushing something cool into my hands. It was Mr. Sweet's guitar. He had asked them months before to give it to me; he had known that even if I came next time, he would not be able to respond in the old way. He did not want me to feel that my trip had been for nothing.

The old guitar! I plucked the strings (*humming "Sweet Georgia Brown") The magic of Mr. Sweet lingered still in the cold steel box. Through the window I could catch the fragrant delicate scent of tender yellow roses. The man on the high old-fashioned bed with the quilt coverlet and the flowing white beard had been my first love.
```

---

## IC-2147: The Toys of Peace

- Title: The Toys of Peace
- Author (byline): H.H. Monroe (Saki)
- Work: Not specified
- Publisher: Echo Library
- Publication date as stated: March 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1881
- Already set (do not supply): none

### Source block (context only)

```text
Author: H.H. Monroe (Saki)
ISBN: 978-1847020741
Publisher: Echo Library
Date (Month/Year): March 2006
```

### Introduction (context only: never use it for content warnings)

```text
Today's children are constantly invited to play with violence. In fact, many children's toy chests have been transformed into war chests full of action figures, toy guns and swords, war toys, laser guns, and other implements of destruction. At every turn, children are faced with violent arcade games, video games, computer games and virtual-reality games. They see violence on television, in the movies, on video.

Children are not born violent -- research shows that violence is a learned behavior. And it is a behavior that we are teaching to younger and younger children. H.H. Monroe (aka Saki) takes a humorous look at a solution to this problem in The Toys of Peace.
```

### Performance text (classify this)

```text
"Harvey," said Eleanor Bope, handing her brother a cutting from a London morning paper of the 19th of March, "just read this about children's toys, please; it exactly carries out some of our ideas about influence and upbringing."

"In the view of the National Peace Council," ran the extract, "there are grave objections to presenting our boys with regiments of fighting men, batteries of guns, and squadrons of 'Dreadnoughts.' Boys, the Council admits, naturally love fighting and all the panoply of war . . . but that is no reason for encouraging, and perhaps giving permanent form to, their primitive instincts. At the Children's Welfare Exhibition, which opens at Olympia in three weeks' time, the Peace Council will make an alternative suggestion to parents in the shape of an exhibition of 'peace toys.' In front of a specially-painted representation of the Peace Palace at The Hague will be grouped, not miniature soldiers but miniature civilians, not guns but ploughs and the tools of industry . . . It is hoped that manufacturers may take a hint from the exhibit, which will bear fruit in the toy shops."

"The idea is certainly an interesting and very well-meaning one," said Harvey; "whether it would succeed well in practice --"

"We must try," interrupted his sister; "you are coming down to us at Easter, and you always bring the boys some toys, so that will be an excellent opportunity for you to inaugurate the new experiment. Go about in the shops and buy any little toys and models that have special bearing on civilian life in its more peaceful aspects. Of course you must explain the toys to the children and interest them in the new idea. I regret to say that the 'Siege of Adrianople' toy, that their Aunt Susan sent them, didn't need any explanation; they knew all the uniforms and flags, and even the names of the respective commanders, and when I heard them one day using what seemed to be the most objectionable language they said it was Bulgarian words of command; of course it may have been, but at any rate I took the toy away from them. Now I shall expect your Easter gifts to give quite a new impulse and direction to the children's minds; Eric is not eleven yet, and Bertie is only nine-and-a-half, so they are really at a most impressionable age."

"There is primitive instinct to be taken into consideration, you know," said Henry doubtfully, "and hereditary tendencies as well. One of their great-uncles fought in the most intolerant fashion at Inkerman -- he was specially mentioned in dispatches, I believe -- and their great-grandfather smashed all his Whig neighbours' hot houses when the great Reform Bill was passed. Still, as you say, they are at an impressionable age. I will do my best."

On Easter Saturday Harvey Bope unpacked a large, promising-looking red cardboard box under the expectant eyes of his nephews. "Your uncle has brought you the newest thing in toys," Eleanor had said impressively, and youthful anticipation had been anxiously divided between Albanian soldiery and a Somali camel-corps. Eric was hotly in favour of the latter contingency. "There would be Arabs on horseback," he whispered; "the Albanians have got jolly uniforms, and they fight all day long, and all night, too, when there's a moon, but the country's rocky, so they've got no cavalry."

A quantity of crinkly paper shavings was the first thing that met the view when the lid was removed; the most exiting toys always began like that. Harvey pushed back the top layer and drew forth a square, rather featureless building.

"It's a fort!" exclaimed Bertie.

"It isn't, it's the palace of the Mpret of Albania," said Eric, immensely proud of his knowledge of the exotic title; "it's got no windows, you see, so that passers-by can't fire in at the Royal Family."

"It's a municipal dust-bin," said Harvey hurriedly; "you see all the refuse and litter of a town is collected there, instead of lying about and injuring the health of the citizens."

In an awful silence he disinterred a little lead figure of a man in black clothes.

"That," he said, "is a distinguished civilian, John Stuart Mill. He was an authority on political economy."

"Why?" asked Bertie.

"Well, he wanted to be; he thought it was a useful thing to be."

Bertie gave an expressive grunt, which conveyed his opinion that there was no accounting for tastes.

Another square building came out, this time with windows and chimneys.

"A model of the Manchester branch of the Young Women's Christian Association," said Harvey.

"Are there any lions?" asked Eric hopefully. He had been reading Roman history and thought that where you found Christians you might reasonably expect to find a few lions.

"There are no lions," said Harvey. "Here is another civilian, Robert Raikes, the founder of Sunday schools, and here is a model of a municipal wash-house. These little round things are loaves backed in a sanitary bakehouse. That lead figure is a sanitary inspector, this one is a district councillor, and this one is an official of the Local Government Board."

"What does he do?" asked Eric wearily.

"He sees to things connected with his Department," said Harvey. "This box with a slit in it is a ballot-box. Votes are put into it at election times."

"What is put into it at other times?" asked Bertie.

"Nothing. And here are some tools of industry, a wheelbarrow and a hoe, and I think these are meant for hop-poles. This is a model beehive, and that is a ventilator, for ventilating sewers. This seems to be another municipal dust-bin -- no, it is a model of a school of art and public library. This little lead figure is Mrs. Hemans, a poetess, and this is Rowland Hill, who introduced the system of penny postage. This is Sir John Herschel, the eminent astrologer."

"Are we to play with these civilian figures?" asked Eric.

"Of course," said Harvey, "these are toys; they are meant to be played with."

"But how?"

It was rather a poser. "You might make two of them contest a seat in Parliament," said Harvey, "and have an election --"

"With rotten eggs, and free fights, and ever so many broken heads!" exclaimed Eric.

"And noses all bleeding and everybody drunk as can be," echoed Bertie, who had carefully studied one of Hogarth's pictures.

"Nothing of the kind," said Harvey, "nothing in the least like that. Votes will be put in the ballot-box, and the Mayor will count them -- and he will say which has received the most votes, and then the two candidates will thank him for presiding, and each will say that the contest has been conducted throughout in the pleasantest and most straightforward fashion, and they part with expressions of mutual esteem. There's a jolly game for you boys to play. I never had such toys when I was young."

"I don't think we'll play with them just now," said Eric, with an entire absence of the enthusiasm that his uncle had shown; "I think perhaps we ought to do a little of our holiday task. It's history this time; we've got to learn up something about the Bourbon period in France."

"The Bourbon period," said Harvey, with some disapproval in his voice.

"We've got to know something about Louis the Fourteenth," continued Eric; "I've learnt the names of all the principal battles already."

This would never do. "There were, of course, some battles fought during his reign," said Harvey, "but I fancy the accounts of them were much exaggerated; news was very unreliable in those days, and there were practically no war correspondents, so generals and commanders could magnify every little skirmish they engaged in till they reached the proportions of decisive battles. Louis was really famous, now, as a landscape gardener; the way he laid out Versailles was so much admired that it was copied all over Europe."

"Do you know anything about Madame Du Barry?" asked Eric; "didn't she have her head chopped off?"

"She was another great lover of gardening," said Harvey, evasively; "in fact, I believe the well known rose Du Barry was named after her, and now I think you had better play for a little and leave your lessons till later."

Harvey retreated to the library and spent some thirty or forty minutes in wondering whether it would be possible to compile a history, for use in elementary schools, in which there should be no prominent mention of battles, massacres, murderous intrigues, and violent deaths. The York and Lancaster period and the Napoleonic era would, he admitted to himself, present considerable difficulties, and the Thirty Years' War would entail something of a gap if you left it out altogether. Still, it would be something gained if, at a highly impressionable age, children could be got to fix their attention on the invention of calico printing instead of the Spanish Armada or the Battle of Waterloo.

It was time, he thought, to go back to the boys' room, and see how they were getting on with their peace toys. As he stood outside the door he could hear Eric's voice raised in command; Bertie chimed in now and again with a helpful suggestion.

"That is Louis the Fourteenth," Eric was saying, "that one in kneebreeches, that Uncle said invented Sunday schools. It isn't a bit like him, but it'll have to do."

"We'll give him a purple coat from my paintbox by and by," said Bertie.

"Yes, an' red heels. That is Madame de Maintenon, that one he called Mrs. Hemans. She begs Louis not to go on this expedition, but he turns a deaf ear. He takes Marshal Saxe with him, and we must pretend that they have thousands of men with them. The watchword is Qui vive? and the answer is L'etat c'est moi -- that was one of his favourite remarks, you know. They land at Manchester in the dead of the night, and a Jacobite conspirator gives them the keys of the fortress."

Peeping in through the doorway Harvey observed that the municipal dustbin had been pierced with holes to accommodate the muzzles of imaginary cannon, and now represented the principal fortified position in Manchester; John Stuart Mill had been dipped in red ink, and apparently stood for Marshal Saxe.

"Louis orders his troops to surround the Young Women's Christian Association and seize the lot of them. 'Once back at the Louvre and the girls are mine,' he exclaims. We must use Mrs. Hemans again for one of the girls; she says 'Never,' and stabs Marshal Saxe to the heart."

"He bleeds dreadfully," exclaimed Bertie, splashing red ink liberally over the facade of the Association building.

"The soldiers rush in and avenge his death with the utmost savagery. A hundred girls are killed" -- here Bertie emptied the remainder of the red ink over the devoted building --"and the surviving five hundred are dragged off to the French ships. 'I have lost a Marshal,' says Louis, 'but I do not go back empty-handed.'"

Harvey stole away from the room, and sought out his sister.

"Eleanor," he said, "the experiment --"

"Yes?"

"Has failed. We have begun too late."
```

---

## IC-2148: The Triune Tale of Diminutive Swine

- Title: The Triune Tale of Diminutive Swine
- Author (byline): John Branyan
- Work: Not specified
- Publisher: Rockshow Comedy, Inc.
- Publication date as stated: 2012
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 717
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Branyan
ISBN: 978-0985469900
Publisher: Rockshow Comedy, Inc.
Date (Month/Year): 2012
```

### Introduction (context only: never use it for content warnings)

```text
What if the Three Little Pigs was retold in Shakespearean English? And what if the third pig, just to mix things up a bit, spoke good ol' American English? Wouldn't that be the best fairytale ever? The Triune Tale of Diminutive Swine by John Branyan
```

### Performance text (classify this)

```text
In time past, though not long ago, there lived pigs.
In stature . . . little.
In number . . . three.
Who being of an age both entitled and inspired to seek

their fortune. Did set about to do thusly.

When they had traveled a distance, pig numbered first

spake. Saying, "Harken brethren, heed this tempestuous

realm."

"Tarry we long from hearth and home we shall fare, I

fear, [snort] not well." And so being collectively agreed but individually

impelled, The diminutive swine set about each to erect for himself

an abode. Pig numbered One did construct his house from straw. Pig numbered Two did likewise. Though, rather, not from straw, instead from sticks. Meanwhile, unique in his imaginings, pig numbered Three

did erectus his domicile, Stalwart and garish, a structure made from brick

entirely.

Soon there happened along, as is frequently the scenario

in classic tale of protagonist pig, or redhooded child

. . . A wolf. Carnivorous nature in full season he called out to the

straw ensconced swine. Saying, "Pray thee, little pig, grant me entrance."

But pig One recalled with sage foreboding that, "He is mad who trusts in the tameness of a belly-pinched

wolf." And responded immediately, "Nay! It shall not be!" "Indeed, not by whit or whiskered jowl!"

Prepared for this most expected response, the wolf

replied immediately. "Then steel thyself little pig." "Forthwith shall I endeavor by employing means both

huffing and puffing to dismantle yon flaxen

fortress." Whereupon there issued forth from the wolf an exhale

of gale proportions, That quickly rendered straw hovel to dregs and dross

and carried aloft piglet and shattered quarters both.

Exposed now to claw and fang, piglet One made haste,

wolf in pursuit,
To the stick festooned sanctum of peccary secondary.
Causing pig Two to cry out in dismay,
"Well! This knots my knickers!"
"The marshaling of feral wolf to my doorstep is nowhere

among those endeavors amenable or congenial."

"A thousand pardons," squealed One. "T'would seem the beast's maim-full breath has purged

me of home and sound judgment alike!"

The mighty maelstrom of the wolf's exhale splattered

second swine's shack and shortened his

sanctimonious scolding simultaneously. "Lo! And Behold!" squealed Two. "Stand we now amid wooden wreckage tremulous and

vulnerable." "With nary a strategy for eschewing the canine

devourer looming in deadly proximity."

"Strategy!" squealed One. "While 'tis noble to contemplate tactical

particularities,"

"Pressed as we are with the time restraint forbidding

detailed strategical conversations," "I would urge we RUN!"

"Wee wee wee wee wee wee wee!"

Whether by their own fleet-footed competence or the

wolf's winless attitude, The diminutive swine arrived at their ultimate kindred

neighbor's inexpungeable brick ingress unscathed. Upon the third pig's door with urgent hooves they

pounded. Calling out, "Unbar this entrance and with haste we

beseech thee!"

The third pig hailed from the American Colonies. And possessing a vocabulary substantially less robust

than his impromptu visitors, replied, "Say what?"

"Seek we sanctuary!" they implored on the verge of

hysteria. "Lest we fall forthwith to the ravenous appetency of

yonder approaching carnivore!"

Still confounded by their importunate words, pig Three

did render ajar his portal. Whereupon One and Two spilled through and collapsed

beyond the threshold, enervated.

"So, y'all just wanted to come in?" "You could'a said that."

The sinister hiss of the wolf could once again be heard

outside. "Pray thee, pigs, grant me entrance."

"The wolf!" said One and Two.

"Wolf?" said Three. "What'd ya suppose he wants?"

"He seeks to gain purchase within." "Indeed he would occupy this very alcove were he but

afforded the most meager of opportunities."

"Right." "I'm just gonna go ask him what he wants."

"Under no circumstances!" squealed Two, flinging self

bodily against the portal. "There is naught to be gained accosting external

opponent." "Save our own immediate demise!"

"What did you say about my Momma?"

House and occupants were again engulfed in a malevolent

blast of wolfish wind. The foundation shook, the frame rattled. And lo, to the astonished eyes of piglet and encroaching

scoundrel alike, Stood the third pigs lodging, undaunted.

[Aside] Good news for you pig fans.

Aghast and dismayed, pig Two queried of Three. "How does against such relentless and torrential

onslaught this domicile endure?"

Pig Three, puffed out chest, tapped a hoof to the

hearth and responded. "It's American Made."
```

---

## IC-2149: The True Story of the Three Little Pigs

- Title: The True Story of the Three Little Pigs
- Author (byline): Jon Scieszka
- Work: Not specified
- Publisher: Scholastic, Inc.
- Publication date as stated: 1989
- Event as filed: Prose
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
"Everybody knows the story of the Three Little Pigs. Or at least they think they do. But I'll let you in on a little secret. Nobody knows the real story, because nobody has ever heard my side of the story. I'm Alexander T. Wolf. You can call me Al. I don't know how this whole Big Bad Wolf thing got started, but it's all wrong. Maybe it's because of our diet. Hey, it's not my fault wolves eat cute little animals like bunnies and sheep and pigs. That's just the way we are. If cheeseburgers were cute, folks would probably think you were Big and Bad too. But like I was saying, the whole big bad wolf thing is all wrong. The real story is about a sneeze and a cup of sugar. THIS IS THE REAL STORY. . . . The True Story of the Three Little Pigs by Jon Scieszka
```

### Performance text (classify this)

```text
Way back in Once Upon a Time time, I was making a birthday cake for my dear old granny. I had a terrible sneezing cold. I ran out of sugar. So I walked down the street to ask my neighbor for a cup of sugar. Now this neighbor was a pig. And he wasn't too bright either. He had built his whole house out of straw. Can you believe it? I mean who in his right mind would build a house of straw? So of course the minute I knocked on the door, it fell right in. I didn't want to just walk into someone else's house. So I called, "Little Pig, Little Pig, are you in?" No answer. I was just about to go home without the cup of sugar for my dear old granny's birthday cake. That's when my nose started to itch. I felt a sneeze coming on. Well I huffed. And I snuffed. And I sneezed a great sneeze.

And you know what? The whole darn straw house fell down. And right in the middle of the pile of straw was the First Little Pig - dead as a doornail. He had been home the whole time. It seemed like a shame to leave a perfectly good ham dinner lying there in the straw. So I ate it up. Think of it as a cheeseburger just lying there. I was feeling a little better. But I still didn't have my cup of sugar . So I went to the next neighbor's house. This neighbor was the First Little Pig's brother. He was a little smarter, but not much. He has built his house of sticks. I rang the bell on the stick house. Nobody answered. I called, "Mr. Pig, Mr. Pig, are you in?" He yelled back."Go away wolf. You can't come in. I'm shaving the hairs on my shinny chin chin."

I had just grabbed the doorknob when I felt another sneeze coming on. I huffed. And I snuffed. And I tried to cover my mouth, but I sneezed a great sneeze.

And you are not going to believe this, but the guy's house fell down just like his brother's. When the dust cleared, there was the Second Little Pig - dead as a doornail. Wolf's honor. Now you know food will spoil if you just leave it out in the open. So I did the only thing there was to do. I had dinner again. Think of it as a second helping. I was getting awfully full. But my cold was feeling a little better. And I still didn't have that cup of sugarr for my dear old granny's birthday cake. So I went to the next house. This guy was the First and Second Little Pig's brother. He must have been the brains of the family. He had built his house of bricks. I knocked on the brick house. No answer. I called, "Mr Pig, Mr. Pig, are you in?" And do you know what that rude little porker answered? "Get out of here, Wolf. Don't bother me again."

Talk about impolite! He probably had a whole sackful of sugar. And he wouldn't give me even one little cup for my dear sweet old granny's birthday cake. What a pig!

I was just about to go home and maybe make a nice birthday card instead of a cake, when I felt my cold coming on. I huffed And I snuffed. And I sneezed once again.

Then the Third Little Pig yelled, " And your old granny can sit on a pin!" Now I'm usually a pretty calm fellow. But when somebody talks about my granny like that, I go a Little crazy. When the cops drove up, of course I was trying to break down this Pig's door. And the whole time I was huffing and puffing and sneezing and making a real scene.

The rest as they say is history.

The news reporters found out about the two pigs I had for dinner. They figured a sick guy going to borrow a cup of sugar didn't sound very exciting.

So they jazzed up the story with all of that "Huff and puff and blow your house down"

And they made me the Big Bad Wolf. That's it The real story. I was framed. "

But maybe you could loan me a cup of sugar ?
```

---

## IC-2150: Typical Day

- Title: Typical Day
- Author (byline): Jonathan Walton
- Work: Millennium Monologues
- Publisher: Meriwether Publishing
- Publication date as stated: Nov 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 921
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jonathan Walton
Book: Millennium Monologues
ISBN: 978-1566080828
Publisher: Meriwether Publishing
Date (Month/Year): Nov 2002
```

### Introduction (context only: never use it for content warnings)

```text
According to the Death Penalty Information Center, since 1973, 138 people in 26 states have been released from death row with evidence of their innocence.

The imposition of the death penalty is a disgrace to a nation founded on principles of justice, human rights and civil liberties. It is even more appalling when death sentences are handed out to those who are innocent.

As long as the death penalty remains a part of the American “justice” system, innocent people will continue to be sentenced to death. Some will be executed. It is inevitable.

Typical Day by Jonathan Walton
```

### Performance text (classify this)

```text
For eight long years I have sat upon death row and finally the day has come that my curtain is going to close. For 243 months,, I have been locked inside this cell and for 2920 days - my life has been nothing short of hell.

The moment draws near where I will take my last walk (pause) and with the victim’s family I will have my very last talk. As I finish the last bite of this, my last meal, the concept of death I begin to grasp. To a wooden chair my body will be strapped, and a metal cap put upon my head - electricity will be run throughout my entire body until at last, I am dead. Ten pairs of eyes, will stare gape and gawk, quite possibly enjoying the site of my life being lost.

I remember staring into those same eyes, those same frowning faces. The prosecutor shouting insults, back and forth as he paces. I testified in my own defense, “I wasn’t there,” I cried. “I don’t even own a gun, so how in God’s name could I have shot someone?”

Upon the truth I swore and all of the words I said were true but all at once the lawyer turned and said, “Why should they believe you?” The foreman began to rise and he handed down a verdict of guilty. All at once I rose to my feet and at the top of my lungs, I began to scream.

“I don’t belong in prison - get your hands off of me!” I fought as they put cuffs on my hands, and chains on my feet; but it didn’t matter what I did- to prison they carried me. My lawyer filed appeal after appeal, but we could make no one believe.

Awaiting my sentence, I sat within this cement block. I spent many nights crying out to God, “Lord I have done nothing wrong, nothing!” “Please God, don’t leave me here to rot. I don’t think I could take it Lord. No, I know that I could not.” Later that month I received my sentence, the words pierce my heart to this day. The foreman again stood to rise and before he sat, I was condemned to die.

I haven’t seen the stars in eight years, if you could count the drops in the oceans - only then could you begin to count my tears. I am all but forgotten, my family no longer visits me. All I have left are thoughts and memories.

My mother used to cook breakfast on Sunday morning as she sang Amazing Grace, the love of God, shown off her face. As she kneaded the biscuits it would go something like this, (sings verse of Amazing Grace).

My wife, she had the smile of an angel. I swear you could see wings, if you gazed from just the right angle. The birth of my daughter, so small within my arms. I remember the first time she called me Daddy, it filled a void with in my heart. But my third year here, my momma passed away. I missed her funeral, the month of January, that fourth Monday. My wife remarried and my daughter should be thirteen; I am all but forgotten, no more visits to Daddy.

The last bite settles in my stomach and the warden instructs me to rise. I have resolved in my mind that I am going to die. I walk the last one hundred feet, one foot in front of the other - left then right, left then right. The chains clank across the floor, I squint my eyes in the light. I try to turn my wrists but I meet pain - the shackles so tight. I walk into the room, with my head held high. I enter into the witnesses’ midst wearing not a frown nor a smile. The executioner asked for my last words and I look each victim in the eye.

“The state killed me years ago, gave me a number - I no longer had a name. Inmate number 49536, I was not a person, I was a convict. I used to be a man until I came here, now I’m part of an unwanted clan. A group of rejected individuals, clasped in chains and wearing orange suits. This was not the way it was supposed to be! Just as your loved one’s life was stolen, the state, the judge, the jury, - each and every one of you; stole my life from me. I have been raped and beaten, ridiculed and scorned. I looked up to God and cursed the day I was born. My spirit is broken and my heart forever dismayed. My body stands before you, but my mind has passed away.”

The shackles were secure and the metal cap put into place, as the tears began to flow down my troubled face.

“Please Lord, take me quick! I am not worthy of this punishment. You are the only one who can read my heart and you know that I am innocent.” I looked over to the wall and the executioner began to reach for the lever. So before the electricity flowed through my veins, I look up to heaven. “The Lord is my Shepherd, I shall not want. He maketh to lie down in green pastures, He leadeth me beside still waters. He restoreth my soul. He leadeth me on the path of righteousness for his namesake. Yea, though I walk through the valley of the shadow of death; I will fear no evil, for thou art with me. (stops abruptly, body convulses, and dies)
```

---

## IC-2151: UFO Menace

- Title: UFO Menace
- Author (byline): Woody Allen
- Work: Side Effects
- Publisher: Ballantine Books
- Publication date as stated: Nov 1989
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2062
- Already set (do not supply): none

### Source block (context only)

```text
Author: Woody Allen
Book: Side Effects
ISBN: 978-0345343352
Publisher: Ballantine Books
Date (Month/Year): Nov 1989
```

### Introduction (context only: never use it for content warnings)

```text
The Men In Black - or MIB's as they are sometimes called are a group that supposedly show up to harass or intimidate witnesses of UFO sightings and related phenomena the government does not want the public to know about. They usually make vague or sometimes specific threats to stop witnesses from talking or sharing information. They confiscate any physical proof of UFO related sightings -- such as photos, artifacts, or audio / video recordings. Needless to say, they have perpetuated the controversy surrounding crop circles, alien abductions, Stonehenge and Area 51. I’m (we’re) here today to get to the TRUTH behind the UFO Menace by Woody Allen.
```

### Performance text (classify this)

```text
UFOs are back in the news, and it is high time we took a serious look at this phenomenon. (Actually, the time is ten past eight, so not only are we a few minutes late but I'm hungry.) Up until now, the entire subject of flying saucers has been mostly associated with kooks or oddballs. Frequently, in fact, observers will admit to being a member of both groups. Still, persistent sightings by responsible individuals have caused the Air Force and the scientific community to reexamine a once skeptical attitude, and the sum of two hundred dollars has now been allocated for a comprehensive study of the phenomenon. The question is: Is anything out there? And if so, do they have ray guns?

All UFOs may not prove to be of extraterrestrial origin, but experts do agree that any glowing cigar-shaped aircraft capable of rising straight up at twelve thousand miles per second would require the kind of maintenance and sparkplugs available only on Pluto. If these objects are indeed from another planet, then the civilization that designed them must be millions of years more advanced than our own. Either that or they are very lucky. Professor Leon Speciman postulates a civilization in outer space that is more advanced than ours by approximately fifteen minutes. This, he feels, gives them a great advantage over us, since they needn't rush to get to appointments.

Dr. Brackish Menzies, who works at the Mount Wilson Observatory, or else is under observation at the Mount Wilson Mental Hospital (the letter is not clear), claims that travelers moving at close to the speed of light would require many millions of years to get here, even from the nearest solar system, and, judging from the shows on Broadway, the trip would hardly be worth it. (It is impossible to travel faster than light, and certainly not desirable, as one's hat keeps blowing off.)

Interestingly, according to modern astronomers, space is finite. This is a very comforting thought-particularly for people who can never remember where they have left things. The key factor in thinking about the universe, however, is that it is expanding and will one day break apart and disappear. That is why if the girl in the office down the hall has some good points but perhaps not all the qualities you require it's best to compromise.

The most frequently asked question about the UFOs is: If saucers come from outer space, why have their pilots not attempted to make contact with us, instead of hovering mysteriously over deserted areas? My own theory is that for creatures from another solar system "hovering" may be a socially acceptable mode of relating. It may, indeed, be pleasurable. I myself once hovered over an eighteen-year-old actress for six months and had the best time of my life. It should also be recalled that when we talk of "life" on other planets we are frequently referring to amino acids, which are never very gregarious, even at parties.

Most people tend to think of UFOs as a modern problem, but could they be a phenomenon that man has been aware of for centuries? (To us a century seems quite long, particularly if you are holding an IOU, but by astronomical standards it is over in a second. For that reason, it is always best to carry a toothbrush and be ready to leave on a moment's notice.) Scholars now tell us that the sighting of unidentified flying objects dates as far back as Biblical times. For instance, there is a passage in the Book of Leviticus that reads, "And a great and silver ball appeared over the Assyrian Armies, and in all of Babylonia there was wailing and gnashing of teeth, till the Prophets bade the multitudes get a grip on themselves and shape up."

Was this phenomenon related to one described years later by Parmenides: "Three orange objects did appear suddenly in the heavens and did circle midtown Athens, hovering over the baths and causing several of our wisest philosophers to grab for towels"? And, again, were those "orange objects" similar to what is described in a recently discovered twelfth century Saxon-church manuscript: ''A lauch lauched he; wer richt laith to weet a cork-heild schonne; whilst a red balle lang owre swam aboone. I thank you, ladies and gentlemen"?

This last account was taken by medieval clergy to signify that the world was coming to an end, and there was great disappointment when Monday came and everyone had to go back to work.

Finally, and most convincingly, in 1822 Goethe himself notes a strange celestial phenomenon. "En route home from the Leipzig Anxiety Festival," he wrote, "I was crossing a meadow, when I chanced to look up and saw several fiery red balls suddenly appear in the southern sky. They descended at a great rate of speed and began chasing me. I screamed that I was a genius and consequently could not run very fast, but my words were wasted. I became enraged and shouted imprecations at them, whereupon they flew away frightened. I related this story to Beethoven, not real-izing he had already gone deaf, and he smiled and nodded and said, 'Right.'

As a general rule, careful on-the-scene investigations disclose that most "unidentified" flying objects are quite ordinary phenomena, such as weather balloons, meteorites, satellites, and even once a man named Lewis Mandelbaum, who blew off the roof of the World Trade Center. A typical "explained" incident is the one reported by Sir Chester Ramsbottom, on June 5, 1961, in Shropshire: "I was driving along the road at 2:00 A.M. and saw a cigar-shaped object that seemed to be tracking my car. No matter which way I drove, it stayed with me, turning sharply at right angles. It was a fierce, glowing red, and in spite of twisting and turning the car at high speed I could not lose it. I became alarmed and began sweating. I let out a shriek of terror and apparently fainted, but awoke in a hospital, miraculously unharmed." Upon investigation, experts determined that the "cigar-shaped object" was Sir Chester's nose. Naturally, all his evasive actions could not lose it, since it was attached to his face.

Another explained incident began in late April of 1972, with a report from Major General Curtis Memling, of Andrews Air Force Base: "I was walking across a field one night and suddenly I saw a large silver disc in the sky. It flew over me, not fifty feet above my head, and repeatedly described aerodynamic patterns impossible for any normal aircraft. Suddenly it accelerated and shot away at terrific speed."

Investigators became suspicious when they noticed that General Memling could not describe this incident without giggling. He later admitted he had just come from a showing of the film War of the Worlds, at the post movie theatre, and "got a very big kick out of it." Ironically, General Memling reported another UFO sighting in 1976, but it was soon discovered that he, too, had become fixated on Sir Chester Ramsbottom's nose-an occurrence that caused consternation in the Air Force and eventually led to General Memling's court-martial.

If most UFO sightings can be satisfactorily explained, what of those few which cannot? Following are some of the most mystifying examples of "unsolved" encounters, the first reported by a Boston man in May, 1969: "I was walking by the beach with my wife. She's not a very attractive woman. Rather overweight. In fact, I was pulling her on a dolly at the time. Suddenly I looked up and saw a huge white saucer that seemed to be descending at great speed. I guess I panicked, because I dropped the rope on my wife's dolly and began running. The saucer passed directly over my head and I heard an eerie, metallic voice say, 'Call your service.' When I got home, I phoned my answering service and received a message that my brother Ralph had moved and to forward all his mail to Neptune. I never saw him again. My wife suffered a severe breakdown over the incident and now cannot converse without using a hand puppet."

From I. M. Axelbank, of Athens, Georgia, February, 1971: "I am an experienced pilot and was flying my private Cessna from New Mexico to Amarillo, Texas, to bomb some people whose religious persuasion I do not wholly agree with, when I noticed an object flying alongside me. At first I thought it was another plane, until it emitted a green beam of light, forcing my plane to drop eleven thousand feet in four seconds and causing my toupee to snap off my head and tear a two-foot hole in the roof. I repeatedly called for help on my radio, but for some reason could only get the old Mr. Anthony program. The UFO came very close to my plane again and then shot away at blinding speed. By this time I had lost my bearings and was forced to make an emergency landing on the turnpike. I continued the trip in the plane on the ground and only got into trouble when I tried to run a toll booth and broke off my wings."

One of the eeriest accounts occurred in August, 1975, to a man on Montauk Point, in Long Island: "I was in bed at my beach house, but could not sleep because of some fried chicken in the icebox that I felt entitled to. I waited till my wife dropped off, and tiptoed into the kitchen. I remember looking at the clock. It was precisely four-fifteen. I'm quite certain of this, because our kitchen clock has not worked in twenty-one years and is always at that time. I also noticed that our dog, Judas, was acting funny. He was standing up on his hind legs and singing 'I Enjoy Being a Girl.' Suddenly the room turned bright orange. At first, I thought my wife had caught me eating between meals and set fire to the house. Then I looked out the window, where to my amazement I saw a gigantic cigar-shaped aircraft hovering just over the treetops in the yard and emitting an orange glow. I stood transfixed for what must have been several hours, though our clock still read four-fifteen, so it was difficult to tell. Finally, a large, mechanical claw extended from the aircraft and snatched the two pieces of chicken from my hand and quickly retreated. The machine then rose and, accelerating at great speed, vanished into the sky. When I reported the incident to the Air Force, they told me that what I had seen was a flock of birds. When I protested, Colonel Quincy Bascomb personally promised that the Air Force would return the two pieces of chicken. To this day, I have only received one piece."

Finally, an account in January, 1977, by two Louisiana factory workers: "Roy and I was catfishing in the bog. I enjoy the bog, as does Roy. We was not drinking, although we had brought with us a gallon of methyl chloride, which we both favor with either a twist of lemon or a small onion. Anyways, at about midnight we looked up and saw a bright yellow sphere descend into the bog. At first Roy mistook it for a whooping crane and took a shot at it, but I said, 'Roy, that ain't no crane, 'cause it's got no beak.' That's how you can tell a crane. Roy's son Gus has a beak, you know, and thinks he's a crane. Anyways, all of a sudden this door slides open and several creatures emerge. These creatures looked like little portable radios with teeth and short hair. They also had legs, although where the toes usually are they had wheels. The creatures motioned to me to come forward, which I did, and they injected me with a fluid that caused me to smile and act like Bo Peep. They spoke with one another in a strange tongue, which sounded like when you back your car over a fat person. They took me aboard the aircraft and gave me what seemed to be a complete physical examination. I went along with it, as I had not had a checkup in two years. By now they had mastered my own language, but they still made simple mistakes like using 'hermeneutics,' when they meant 'heuristic.' They told me they were from another galaxy and were here to tell the earth that we must learn to live in peace or they will return with special weapons and laminate every first-born male. They said they would get the results of my blood test back in a couple of days and if I didn't hear from them I could go ahead and marry Clair."
```

---

## IC-2152: The Veldt

- Title: The Veldt
- Author (byline): Ray Bradbury
- Work: Not specified
- Publisher: Creative Education
- Publication date as stated: Nov 1987
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2060
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ray Bradbury
ISBN: 978-0886821081
Publisher: Creative Education
Date (Month/Year): Nov 1987
```

### Introduction (context only: never use it for content warnings)

```text
The Veldt by Ray Bradbury
```

### Performance text (classify this)

```text
"George, I wish you'd look at the nursery."

"What's wrong with it?"

"I don't know. I just want you to look at it, is all, or call a psychologist in to look at it."

“What would a psychologist want with a nursery?"

"You know very well what he'd want." His wife paused in the middle of the kitchen and watched the stove busy humming to itself, making supper for four

"It's just that the nursery is different now than it was."

"All right, let's have a look."

They walked down the hall of their soundproofed Happylife Home, which had cost them thirty thousand dollars installed, this house which clothed and fed and rocked them to sleep and played and sang and was good to them. Their approach sensitized a switch somewhere and the nursery light flicked on when they came within ten feet of it. Similarly, behind them, in the halls, lights went on and off as they left them behind, with a soft automaticity.

They stood on the thatched floor of the nursery. It was forty feet across by forty feet long and thirty feet high; it had cost half again as much as the rest of the house. "But nothing's too good for our children," George had said.

The nursery was silent. It was empty as a jungle glade at hot high noon. The walls were blank and two dimensional. Now, as George and Lydia Hadley stood in the center of the room, the walls began to purr and recede into crystalline distance, it seemed, and presently an African veldt appeared, in three dimensions, on all sides, in color reproduced to the final pebble and bit of straw. The ceiling above them became a deep sky with a hot yellow sun.

"You see, there are the lions, far over, that way. Now they're on their way to the water hole. They've just been eating," said Lydia. "I don't know what."

"Some animal." George Hadley put his hand up to shield off the burning light from his squinted eyes. "A zebra or a baby giraffe, maybe."

"Are you sure?" His wife sounded peculiarly tense.

"Did you hear that scream?" she asked.

The lions were coming. And again George Hadley was filled with admiration for the mechanical genius who had conceived this room. A miracle of efficiency selling for an absurdly low price. Every home should have one. Oh, occasionally they frightened you with their clinical accuracy, they startled you, gave you a twinge, but most of the time what fun for everyone, not only your own son and daughter, but for yourself when you felt like a quick jaunt to a foreign land, a quick change of scenery. Well, here it was!

The lions stood looking at George and Lydia Hadley with terrible green-yellow eyes.

"Watch out!" screamed Lydia. The lions came running at them.

Lydia bolted and ran. Instinctively, George sprang after her. Outside, in the hall, with the door slammed he was laughing and she was crying, and they both stood appalled at the other's reaction.

"Walls, Lydia, remember; crystal walls, that's all they are. Oh, they look real, I must admit - Africa in your parlor - but it's all dimensional, super-reactionary, supersensitive color film and mental tape film behind glass screens.

"You've got to tell Wendy and Peter not to read any more on Africa."

"And lock the nursery for a few days until I get my nerves settled."

"You know how difficult Peter is about that. When I punished him a month ago by locking the nursery for even a few hours - the tantrum be threw! And Wendy too. They live for the nursery."

"I don't know - I don't know," she said, blowing her nose, sitting down in a chair that immediately began to rock and comfort her. "Maybe I don't have enough to do. Maybe I have time to think too much. Why don't we shut the whole house off for a few days and take a vacation?"

"But I thought that's why we bought this house, so we wouldn't have to do anything?"

“That's just it. I feel like I don't belong here. The house is wife and mother now, and nursemaid. Can I compete with an African veldt? Can I give a bath and scrub the children as efficiently or quickly as the automatic scrub bath can? I cannot. And it isn't just me. It's you. You've been awfully nervous lately."

At dinner they ate alone, for Wendy and Peter were at a special plastic carnival across town and had televised home to say they'd be late, to go ahead eating. So George Hadley, bemused, sat watching the dining-room table produce warm dishes of food from its mechanical interior.

As for the nursery, thought George Hadley, it won't hurt for the children to be locked out of it awhile. Too much of anything isn't good for anyone. And it was clearly indicated that the children had been spending a little too much time on Africa.

Remarkable how the nursery caught the telepathic emanations of the children's minds and created life to fill their every desire. The children thought lions, and there were lions. The children thought zebras, and there were zebras. Sun - sun. Giraffes - giraffes. Death and death.

Perhaps Lydia was right. Perhaps they needed a little vacation from the fantasy which was growing a bit too real for ten-year-old children. It was all right to exercise one's mind with gymnastic fantasies, but when the lively child mind settled on one pattern... ?

I'm beginning to be sorry we bought that room for the children. If children are neurotic at all, a room like that -"

"It's supposed to help them work off their neuroses in a healthful way."

"I'm starting to wonder."

"We've given the children everything they ever wanted. Is this our reward-secrecy, disobedience?"

"Who was it said, 'Children are carpets, they should be stepped on occasionally'? We've never lifted a hand. They're insufferable - let's admit it. They come and go when they like; they treat us as if we were offspring. They're spoiled and we're spoiled."

"I think I'll have David McClean come tomorrow morning to have a look at Africa."

And although their beds tried very bard, the two adults couldn't be rocked to sleep for another hour. A smell of cats was in the night air.

"Father?" said Peter [the next morning]. "You aren't going to lock up the nursery for good, are you?"

"Matter of fact, we're thinking of turning the whole house off for about a month. Live sort of a carefree one-for-all existence."

"That sounds dreadful! Would I have to tie my own shoes instead of letting the shoe tier do it? And brush my own teeth and comb my hair and give myself a bath? It would be horrid. I didn't like it when you took out the picture painter last month."

"That's because I wanted you to learn to paint all by yourself, son."

"I don't want to do anything but look and listen and smell; what else is there to do?"

Soon Dr. McClean arrived . . .

"Run outside a moment, children," said George Hadley. With the children gone, the two men stood [at the door of the nursery] studying the lions clustered at a distance, eating with great relish whatever it was they had caught.

“This doesn't feel good, This is very bad. My advice to you is to have the whole damn room torn down and your children brought to me every day during the next year for treatment."

"Is it that bad?"

"I'm afraid so. One of the original uses of these nurseries was so that we could study the patterns left on the walls by the child's mind, study at our leisure, and help the child. In this case, however, the room has become a channel toward-destructive thoughts, instead of a release away from them."

“You [have] spoiled your children more than most. And now you're letting them down in some way. What way?"

"I've taken a few machines from the house and threatened them, a month ago, with closing up the nursery unless they did their homework. I did close it for a few days to show I meant business."

"Ah, ha!"

You've let this room and this house replace you and your wife in your children's affections. This room is their mother and father, far more important in their lives than their real parents. And now you come along and want to shut it off. No wonder there's hatred here. You can feel it coming out of the sky. Feel that sun. George, you'll have to change your life. Like too many others, you've built it around creature comforts. Why, you'd starve tomorrow if something went wrong in your kitchen. Turn everything off. Start new. It'll take time. But we'll make good children out of bad in a year, wait and see."

"I don't imagine the room will like being turned off," said the father.

"Nothing ever likes to die - even a room."

They went to the fuse box together and threw the switch that killed the nursery.

The two children were in hysterics. They screamed and pranced and threw things. They yelled and sobbed and swore and jumped at the furniture.

"You can't do that to the nursery, you can't!''

“It's off, and it stays off. And the whole damn house dies as of here and now. The more I see of the mess we've put ourselves in, the more it sickens me. We've been contemplating our mechanical, electronic navels for too long. My God, how we need a breath of honest air!"

And he marched about the house turning off the voice clocks, the stoves, the heaters, the shoe shiners, the shoe lacers, the body scrubbers and swabbers and massagers, and every other machine be could put his hand to.

The house was full of dead bodies, it seemed. It felt like a mechanical cemetery. So silent. None of the humming hidden energy of machines waiting to function at the tap of a button.

"Don't let them do it!" wailed Peter at the ceiling, as if he was talking to the house, the nursery. "Don't let Father kill everything." He turned to his father. "Oh, I hate you!"

"I wish you were dead!"

"We were, for a long while. Now we're going to really start living. Instead of being handled and massaged, we're going to live."

Wendy was still crying and Peter joined her again. "Just a moment, just one moment, just another moment of nursery," they wailed.

"Oh, George," said the wife, "it can't hurt."

"All right - all right, if they'll just shut up. One minute, mind you, and then off forever.

I'm going to dress. You turn the nursery on for a minute, Lydia, just a minute, mind you."

And the three of them went babbling off while he let himself be vacuumed upstairs through the air flue and set about dressing himself. A minute later Lydia appeared.

"I'll be glad when we get away," she sighed.

"Did you leave them in the nursery?"

"I wanted to dress too. Oh, that horrid Africa. What can they see in it?"

"I think we'd better get downstairs before those kids get engrossed with those damned beasts again."

Just then they heard the children calling, "Daddy, Mommy, come quick -quick!"

They went downstairs in the air flue and ran down the hall. The children were nowhere in sight. "Wendy? Peter!"

They ran into the nursery. The veldtland was empty save for the lions waiting, looking at them. The door slammed. "Wendy, Peter!"

"Open the door!" cried George Hadley, trying the knob. "Why, they've locked it from the outside! Peter!" He heard Peter's voice outside, against the door.

"Don't let them switch off the nursery and the house," he was saying.

And then they heard the sounds.

The lions on three sides of them, in the yellow veldt grass, padding through the dry straw, rumbling and roaring in their throats. The lions.

Mr. Hadley looked at his wife and they turned and looked back at the beasts edging slowly forward crouching, tails stiff. Mr. and Mrs. Hadley screamed . .

Now the lions were done feeding. They moved to the water hole to drink, [and outside the nursery door Wendy and Peter smiled.]
```

---

## IC-2153: The Vigilant Rabbit

- Title: The Vigilant Rabbit
- Author (byline): David Sedaris
- Work: Squirrel Seeks Chipmunk
- Publisher: Back Bay Books
- Publication date as stated: Oct 2011
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1268
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
(Pg 98+) A white-tailed doe was discovered one morning disembowelled on the banks of the stream, and the residents of the forest went crazy with fear – "freaked out" was how the sparrow put it. A few days later a skunk was found, no more than a gnawed-upon skull attached to a short leash of spine. Personality-wise, he'd been no great shakes. Neither was he particularly good-looking, but still! Then a squirrel disappeared, and it was decided that something had to be done.

A meeting was convened in the clearing near the big oak, and the hawk, who often flew great distances in search of food, proposed that they build a gate. "I've seen one where the humans live, and it seems to work fairly well."

"Work how?" asked a muskrat.

The hawk explained that once the gate was erected, anyone entering the forest would have to stop and identify himself. "It keeps out the riffraff," he said, adding that when bad things happened, that was usually who was responsible – riffraff.

For the second time that day, the muskrat raised his hand. "And what if this riffraff can't be stopped?"

"Then you sound an alarm," the hawk suggested. "It could be anything, really, just so long as it's loud."

The building of the gate was left to the beaver, who had a slight problem with the hinges, but eventually got them right. Just to the side of them he hung a gong fashioned from an old NO TRESPASSING sign. "I figured I could hit it with my tail," he said, and he gave it a whack for good measure.

When the noise had stopped echoing off the surrounding hills, the rabbit stepped forward. "Who elected you to man the gate?" he asked, adding that anyone could hit a sheet of rusted metal, even someone without an oversize tail. At that he picked up a heavy stick and went at it, creating a racket as loud as the beaver's. "I've also got the better hearing," he boasted. "I'm slimmer, I'm faster, and I'm more safety conscious, vigilant, you might say."

All eyes turned to the beaver, who said simply, "Whatever," and waddled back to his lodge.

On the rabbit's first morning as chief of security, he stopped an approaching snake, who looked up at him and laughed until he cried.

"Something funny?" asked the rabbit.

The snake used his tail to wipe a tear from his face. "You idiots," he said. "What good is a gate without a wall?"

"What good is a… huh?"

"It doesn't make any sense," continued the snake. "If an animal doesn't want to enter here, what's to stop him from moving down a few dozen yards and crawling in beside the fallen pine?"

"What's to stop him?" asked the rabbit, and he picked up his heavy stick and bashed the snake's head in. Then he kicked some dirt over the body and wrote NO LAUGHING on the NO TRESPASSING sign.

A short while later a magpie stopped by and pecked at the bits of brain left scattered on the ground in front of the gate. "Not to nitpick," he said between mouthfuls, "but what's to prevent someone from entering by air? You and your friends initiate a no-fly zone?"

"What's to keep you from flying in?" asked the rabbit, and once again he brought down his heavy stick. Then he dug up the snake and hung both it and the dead magpie from the top of his gate. There they could act as visual warnings, proof that he was a force to be reckoned with. When that was done, he added to his sign, which now read: NO TRESPASSING. NO LAUGHING. AND NO STUPID QUESTIONS EITHER. THIS MEANS YOU.

It was a hot, windless day, and within an hour blowflies arrived and settled on the faces of the two dead animals. Their buzzing attracted a frog, who jumped over from the nearby stream, flicked out his tongue, and dined upon them until he was full. Only then did he read the sign and turn to address the rabbit. "Seeing as you don't want jokes or questions, I guess I'll phrase this as a comment," he said. "In order to enter through your gate I'll have to stop and go through your tiresome rigmarole. That kind of BS doesn't interest me much, so instead I'm going to return to my stream and swim into your third-rate, beetle-infested forest."

He turned to leave, and the rabbit, who was nothing if not quick, reached for his heavy stick. Then he hung the frog on his gate and added NO CURSING to his NO TRESPASSING sign.

It wasn't long before an otter came along and went for the crushed frog. Then a badger stopped by, attracted by the smell of the dead otter. As the bodies were heaped upon the gate, it began to tilt. The rabbit propped it up with a fallen branch and then turned his attention to the sign. NO DIRTY LOOKS, HE WROTE. NO QUESTIONING MY INTEGRITY. NO INSULTING REMARKS ABOUT MY EARS OR MY TEETH. He was just wondering how to spell "insolence" when a shadow fell, and he looked up to see a mag-nificent white unicorn. His silky mane curled about his neck in waves the colour of buttercups. Equally brilliant was his horn, which looked to be made of gold. At his approach, the rabbit put down his pencil. "State your name and your business."

"I'm a unicorn," said the unicorn, "and I come to bring joy to all the forest creatures."

"Not with that horn you don't," said the rabbit.

"I beg your pardon?"

"I said, lose the weapon."

"The horn is what makes me who I am!"

"Which is unwelcome," said the rabbit. "Now do as I say or beat it."

"But happiness follows wherever I go!" the unicorn protested. "I can make a rainbow just by flicking my tail."

The rabbit reached for his stick.

"If you won't let me through the gate, I'll just jump over it," said the unicorn. And because he was taller than the rabbit and much more powerful, he did just that. "Sorry," he said as he headed into the forest, "but you didn't leave me any choice."

"We'll see about that," muttered the rabbit, and he spat on to the blood-soaked ground.

The unicorn spent the late afternoon making rainbows for all the woodland creatures. Then he caused the wildflowers to bloom and conjured up some berries for a hungry box turtle. As the sun set over the treetops, he settled upon a bed of fragrant moss and fell into a deep sleep.

The following morning, the songbirds woke him. The unicorn yawned and was just about to stand when he noticed the pile of golden shavings scattered across the moss. Then he felt his forehead and galloped to the gate piled high with rotting carcasses. "Who chewed off my horn? he wailed.

The rabbit answered calmly that rules were rules. "If I let you trot around with a weapon on your head, I'd have to let everyone do it."

"But it had magic powers!"

"I said, scram," said the rabbit.

The unicorn, just a common everyday horse now, slunk off toward a field of tall grasses. The rabbit watched him go and then turned back to his sign. "Magic powers indeed," he muttered. "I didn't taste anything special." Again he spat, only this time a diamond came out and landed on the ground beside him. That's what he was staring at when the wolves arrived.
```

---

## IC-2154: Villains, Victims, and Very Big Feelings

- Title: Villains, Victims, and Very Big Feelings
- Author (byline): Rebecca Young
- Work: Famous Fantasy Character Monologs
- Publisher: Meriwether Publishing
- Publication date as stated: Sept 2006
- Event as filed: Prose
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

THE NOT-SO-WICKED WITCH: (Pg 7) It makes me so mad; I've just got to zap someone! (Makes pointing gesture to someone flying through the air) Zap! (Blows off zapping finger) There. Now I do feel a little better.

(cackles and exits in pursuit of Dorothy)

ACROPHOBIC SUPER-DUPER MAN: (Pg 99) (dodging the witch’s “ZAP”, he lands in a superhero pose) (in a superhero voice) It's an eagle. It's a jet. (drops the facade) It's ... oh, give me a break.

Everyone knows it's me. But what I bet they don't know is: I absolutely hate flying. It scares me to death.

THE LONELY CAPTAIN HOOK: (Pg 76) (who may or may not be a little tipsy. He steps forward trying to one-up ASDM) Do you know what it's like being stuck out to sea, seeing nothin' but water for ages? It makes my sea legs quite wobbly, I tell you! (staggers a bit) And that ain't from the rum neither! Ha ha! I've been riding that ol' wooden bucket for months. Some days are real exciting, like when we're looting or fighting. Other times are just plain boring. Hanging out with a bunch of sweaty old men who haven't bathed since the last time we saw land!

ACROPHOBIC SUPER-DUPER MAN: (Pg 99) Do you know how far down the ground is from where I fly? A man could get seriously hurt if something went wrong. That's why I close my eyes sometimes, but do you know how many times I've had to dodge a plane? Or a flock of geese? Believe me, those birds aren't so nice when you upset their formation. I can't tell you how many times I've been attacked! One day I'm liable to get pecked to death, right up there in the sky. But what choice do I have?

THE LONELY CAPTAIN HOOK: (Pg 76) I actually look forward to seeing Peter flying around my ship, free as a bird. All dressed in green with that silly pointed hat! Playing tricks on my crew and tangling up my sails! Taunting us. I know you won't believe this, but I actually care about that silly boy named Peter. Without him, my ship would be in shambles! Whenever the crew gets cabin fever and start beating up on each other, here comes Peter, flitting about trying to cause trouble. He thinks he's annoying me, but I have no interest in hurting the little booger. He's the only thing exciting around here!

ACROPHOBIC SUPER-DUPER MAN: (Pg 99) When someone needs me, I have to get there fast. There's no advance warning. No time to hail a cab or hop on the subway! I've thought about getting a car, but people drive like maniacs! I guess, all in all, I'm safer in the air. It's kind of peaceful ... up in the clouds ...

(Looks up at sky dreamily)

THE LONELY CAPTAIN HOOK: (Pg 76) Oh look! Here Peter comes now! "I'm gonna get you! You and that pixie bug! By hand or by hook, I'm gonna get you!" (Exits in pursuit of Peter)

ACROPHOBIC SUPER-DUPER MAN: (Pg 99) (after saying a quick prayer, launches into the air) It's an eagle. It's a jet!

THE DISGRUNTLED TOOTH FAIRY: (Pg 10) (and a new flying creature softly descends, yawning) I am so tired! I spent all night flying around, and I'm plumb worn out! Not to mention bruised! Doesn't anyone use a nightlight anymore? I couldn't see a thing, and I must've bumped into a dozen dressers! And for what? No one even cares about me. Used to be, I'd get sweet little notes thanking me for visiting. But those days are long gone.

DISILLUSIONED SANDMAN: (Pg 124) (enters and nods in agreement) [You tell it sister!] (blows a puff of sand into the Tooth Fairy’s face) This job is nothing like I thought it would be. It doesn't have the first thing to do with sand - not the real kind anyway! I pictured sandy beaches. Girls in bikinis. Drinks with fancy umbrellas. Parties and bonfires. The kind of job any guy would dream of having! Ha! You know what? This stupid job has zero to do with any of that. I work in complete darkness - stuck on the stinking third shift! I haven't seen the light of day since I started working. Who ever heard of a Sandman that helps people sleep?

THE DISGRUNTLED TOOTH FAIRY: (Pg 10) [I know!] Nowadays, if I do get a note, it's not to say thanks. Oooh, nooo! It's to tell me exactly how much I'm supposed to pay for a silly little white nub wrapped in bloody toilet paper! And it's not cheap either! (opens a note from a child) A dollar? You've got to be kidding me! Who pays a dollar for a tooth?

DISILLUSIONED SANDMAN: (Pg 124) [Yeah!] Whatever happened to counting sheep or drinking warm milk? Or Tylenol P.M.? What the heck do people need me for?

THE DISGRUNTLED TOOTH FAIRY: (Pg 10) I don't know why I do this night after night. Maybe I should move on. Be a fairy godmother or something. You know, turn pumpkins into coaches! Now, that would be cool!

But then I think about all those children going to bed every night, waiting for me. How would they feel if I just didn't show up? Their little hearts would be broken. And what would parents do with all those little teeth? Throw them away? Oh, I couldn't let that happen!

DISILLUSIONED SANDMAN: (Pg 124) What about the hot chicks wanting to nap at the beach? Why can't I help them? How does a guy get promoted to a job like that? I'm stuck on the worst shift. No one - and I mean no one - above the age of fifteen and under the age of forty ever sleeps with a light on. Not even a tiny one. It's pitch black the whole night. And if you get caught flashing - that's code for turning on the light - it's instant termination! I don't know how much more I can take. How can they expect any normal guy to work this way? I got the wrong job!

THE DISGRUNTLED TOOTH FAIRY: (Pg 10) Maybe I just need a nap ... (motions to The Sandman to hit her with the dust again) (Both exit as Little Red stealthily enters)

SECRET AGENT LITTLE RED RIDING HOOD: (Pg 31) I'd been following that wolf for weeks trying to pin something on him. I knew without a doubt that he was bad to the core. I just didn't have any proof. The little red riding hood thing was brilliant. He'd never suspect a helpless young girl on her way to see her grandma. Ha! I laugh at the thought of me being helpless! I'm at the top of my karate class! (does a few karate chops in the air) The basket of goodies was just too much to resist. That stupid wolf trailed me all the way up the mountain. Ducking behind trees. Crouching down beside bushes. He wasn't very clever at hiding, I can tell you that.

THE BIG BAD WOLF: (Pg 92) (hand cuffed behind his back) This is all a big mistake! It was a joke! An innocent prank gone wrong. I wasn't going to eat her! I promise! I'm a vegan. I don't even eat anything that's been anywhere near meat. I swear. I wasn't going to harm a hair on her hooded head. But a wolf's got to have some fun, you know? SECRET AGENT LITTLE RED RIDING HOOD: (Pg 31) I didn't think he was ever going to take the lead and beat me there. I had to stop and tie my shoes twice just to give him a head start. Even then, I could hear the pitiful thing puffing like crazy. I was afraid I might have to give him mouth-to-mouth resuscitation and save his life instead of capturing him! But it was all going according to plan. The lady I hired to play my grandma played her part excellently. By the time I got there, she'd let the wolf tie her up and stuff her in the closet, just like I’d told her to.

THE BIG BAD WOLF: (Pg 92) You should've seen her face! (mocking) "Why Grandma, what big teeth you've got!" The girl needs some serious glasses if she really thought I was her grandma. Look at all the fur, man! (lifts arm awkwardly) I mean, if her grandma looks like this, then she's got one freaky grandma! I thought she'd take one look at me and run laughing -- or screaming -- from the room! I never dreamed she'd stick around. SECRET AGENT LITTLE RED RIDING HOOD: (Pg 31) But then it all went down the drain. All that work. All that planning. For nothing. Here comes the big, bad woodsman to save the day. Couldn't he see that I had it all under control? I was going to pound on that wolf's head, I tell you. (karate chops in the air) Had it all planned out. I'd even gotten in a kick or two before the woodsman ruined everything.

THE BIG BAD WOLF: (Pg 92) She practically stuck her head in I my mouth; she was so close to my face! You gotta give me a break, man! I couldn't help but lick her a little! (cowers as an unseen woodsman raises his ax) Whoa! Hold back on the axe, man! Go check the closet! Her old granny's in there. I didn't harm a gray hair on her head! Go on! Go see! (points in one direction and then runs off in the other direction, yelling) Some people just can't take a joke, can they? SECRET AGENT LITTLE RED RIDING HOOD: (Pg 31) Guess the one good thing is I kept my cover. Secret Agent Little Red Riding Hood, at your service. (bows)
```

---

## IC-2155: The Visit

- Title: The Visit
- Author (byline): Ray Bradbury
- Work: We’ll Always Have Paris, Pgs 15-21
- Publisher: William Morrow and Company
- Publication date as stated: Jan 2010
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, BILL, MRS. HADLEY
- Teaser before the introduction: Yes
- Spoken words (computed): 1419
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ray Bradbury
Book: We’ll Always Have Paris, Pgs 15-21
ISBN: 978-0061670145
Publisher: William Morrow and Company
Date (Month/Year): Jan 2010
```

### Introduction (context only: never use it for content warnings)

```text
Pablo Picasso once said, “The meaning of life is to find your gift . . . the purpose of life is to give it away.” In this selection two strangers, bound by grief and hope, come to understand exactly what this means. The Visit by Ray Bradbury
```

### Performance text (classify this)

```text
NARRATOR: (Pg 15-21) She had called and there was to be a visit. At first the young man had been reluctant, had said no, no thanks, he was sorry, he understood, but no.

But then when he heard her silence on the other end of the telephone, no sound at all, but the kind of grief which keeps to itself, he had waited a long while and then said. .

BILL: (on phone) Yes, all right, come over, but, please, don't stay too long. This is a strange situation, and I don't know how to handle it.

NARRATOR: Nor did she. Going to the young man's apartment, she wondered what she would say and how she would react, and what he would say. She was terribly afraid of doing something so emotional that he would have to push her out of the apartment and slam the door. For she didn't know this young man at all. He was a total and complete stranger. They had never met and only yesterday she had found his name at last, after a desperate search through friends at a local hospital. And now, before it was too late, she simply had to visit a totally unknown person for the most peculiar reasons in all her life or, for that matter, in the lives of all mothers in the world since civilization began.

MRS. HADLEY: (handing money to the cabdriver) Please wait.

NARRATOR: She gave the cabdriver a twenty-dollar bill to ensure his being there should she come out sooner than she expected and stood at the entrance to the apartment building for a long moment before she took a deep breath, opened the door, went in, and took the elevator up to the third floor.

She shut her eyes outside his door and took another deep breath and knocked. There was no answer. With sudden panic, she knocked very hard. This time, at last, the door opened. The young man, somewhere between twenty and twenty-four, looked timidly out at her and said

BILL: You're Mrs. Hadley?

MRS. HADLEY: You don't look like him at all. I mean—

NARRATOR: She caught herself and flushed and almost turned to go away.

BILL: You didn't really expect me to, did you?

NARRATOR: He opened the door wider and stepped aside. There was coffee waiting on a small table in the center of the apartment.

MRS. HADLEY: No, no, silly. I didn't know what I was saying.

BILL: Sit down, please. I'm William Robinson. Bill to you, I guess. (picking up the coffee pot) Black or white?

MRS. HADLEY: Black.

BILL: How did you find me? (handing the cup over)

MRS. HADLEY: (hands trembling) I know some people at the hospital. They did some checking.

BILL: They shouldn't have.

MRS. HADLEY: Yes, I know. But I kept at them. You see, I'm going away to live in France for a year, maybe more. This was my last chance to visit my--I mean-- (heartbeats)

NARRATOR: She lapsed into silence and stared into the coffee cup.

BILL: (quietly) So they put two and two together, even though the files were supposed to be locked?

MRS. HADLEY: Yes. It all came together. The night my son died was the same night you were brought into the hospital for a heart transplant. It had to be you. There was no other operation like that that night or that week. I knew that when you left the hospital, my son, his heart anyway (with difficulty) went with you." (heartbeats) (putting down the coffee cup) I don't know why I'm here.

BILL: Yes, you do.

MRS. HADLEY: Not really, I don't. It's all so strange and sad and terrible and at the same time, I don't know, God's gift. Does that make any sense?

BILL: To me it does. I'm alive because of the gift.

NARRATOR: Now it was his turn to fall silent, pour himself coffee, stir it and drink.

BILL: When you leave here, where will you go?

MRS. HADLEY: (uncertainly) Go?

BILL: I mean . . .

NARRATOR: The young man winced with his own lack of ease. The words simply would not come.

BILL: I mean, have you other visits to make? Are there other . . .

MRS. HADLEY: I see.

NARRATOR: The woman nodded several times, took hold of herself with a motion of her body, looking at her hands in her lap, and at last shrugged.

MRS. HADLEY: Yes, there are others. My son, his vision was given to someone in Oregon. There is someone else in Tucson . . .

BILL: You don't have to continue. I shouldn't have asked.

MRS. HADLEY: No, no. It is all so strange, so ridiculous. It is all so new. Just a few years ago, nothing like this could have happened. Now we're in a new time. I don't know whether to laugh or cry. Sometimes I start one and then do the other. I wake up confused. I often wonder if he is confused. But that's even sillier. He is nowhere.

BILL: He is somewhere. He is here. (heartbeats) And I'm alive because he is (places his hand on his heart) here at this very moment.

NARRATOR: The woman's eyes grew very bright, but no tears fell.

MRS. HADLEY: Yes. Thank you for that.

BILL: No, I thank him, and you for allowing me to live.

NARRATOR: The woman jumped up suddenly, as if propelled by an emotion stronger than she knew. She looked around for the perfectly obvious door and seemed not to see it.

BILL: Where are you going? You just got here!

MRS. HADLEY: This is stupid! Embarrassing. I'm putting too much of a burden on you, on myself. I'm going now before it all gets so ludicrous I go mad--

BILL: Stay. Finish your coffee.

NARRATOR: She remained standing but picked up her coffee cup with shaking hands. The soft rattle of the cup was the only sound for a time as she slaked the coffee with some unquenchable thirst. Then she put the empty cup down and said:

MRS. HADLEY: I really must go. I feel faint. I feel I might fall down. I am so embarrassed with myself, with coming here. God bless you, young man, and may you have a long life.

NARRATOR: She started toward the door, but he stood in her way.

BILL: Do what you came to do.

MRS. HADLEY: What, what?

BILL: You know. You know very well. I won't mind it. Do it. (gently) Go on. . .

NARRATOR: And shut his eyes, his hands at his side, waiting. She stared into his face and then at his chest, where under his shirt there seemed the gentlest stirring. (heartbeats) She took one step forward. She turned her head and quietly moved her right ear down and then again down, inch by inch, until it touched the young man's chest. (heartbeats)

She might have cried out but did not. She might have exclaimed something but did not. Her eyes were also shut now, and she was listening. (heartbeats) Her lips moved, saying something, perhaps a name, over and over, almost to the rhythm of the pulse she heard under the shirt, under the flesh, within the body of the patient young man. The heart was beating there. (heartbeats) She listened. The heart beat with a steady and regular sound. (heartbeats)

She listened for a long while. Her breath slowly drained out of her, as color came into her cheeks. She listened. The heartbeat. (heartbeats) Then she raised her head, looked at the young man's face for a final time, and very swiftly touched her lips to his cheek, turned, and hurried across the room, with no thanks, for none was needed. At the door she did not even turn around but opened it and went out and closed the door softly.

The young man waited for a long moment. His right hand came up and slid across his shirt, across his chest to feel what lay underneath. (heartbeats) His eyes were still shut and his face emotionless. Then he turned and sat down without looking where he sat and picked up his coffee cup to finish his coffee. The strong pulse, the great vibration of the life within his chest, traveled along his arm and into the cup and caused it to pulse in a steady rhythm, unending, as he placed it against his lips, and drank the coffee as if it were a medicine, a gift, that would refill the cup again and again through more days than he could possibly guess or see. He drained the cup. Only then did he open his eyes and see that the room was empty.

CONCLUSION

* Over 100,000 people are on the national organ transplant waiting list and every 8 minutes another name is added. It's estimated that more than 17 people die every day in the U.S. because of the lack of donor organs.

Consider becoming an organ donor. It’s a tremendous decision, but as easy as registering at the DMV when you renew your driver’s license. After all, the only thing you take with you when you’re gone is what you choose to leave behind.
```

---

## IC-2156: Waiter from Hell

- Title: Waiter from Hell
- Author (byline): Gene Perret
- Work: Not specified
- Publisher: Inferno Publishing
- Publication date as stated: Feb 1998
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 596
- Already set (do not supply): none

### Source block (context only)

```text
Author: Gene Perret
BOOK: Legends Magazine, No 75
ISBN: Magazine
Publisher: Inferno Publishing
Date (Month/Year): Feb 1998
```

### Introduction (context only: never use it for content warnings)

```text
Remember when eating out was a relaxing experience? Someone else cooked for you, served you and cleaned up after you. All you had to do was chew, swallow and pay. No longer, though. Today you feel like a laboratory rat who has to struggle through a maze every time it wants a chunk of cheese. Waiter from Hell by Gene Perret
```

### Performance text (classify this)

```text
"Good evening," the maitre d' said. "Table for four?"

"Yes, thank you."

"Smoking or non?"

"Nonsmoking."

"Would you prefer to dine indoors or outdoors this evening?"

"I guess indoors would be good."

"Very well, sir," he said. "Would you like to be seated in the main dining room, the enclosed patio or our lovely solarium?"

"Uh, let me see...uh..."

"I can give you a table with a lovely view in our lovely solarium."

"I think the solarium would be lovely," l said. We followed him there.

"Now, would you prefer a view overlooking the golf course, the sunset on the lake or the majestic mountains to the west?"

"Whatever you recommend," I said. Let him make a decision for a change, I thought.

He sat us by a window facing the golf course, the lake or the mountains. I couldn't tell which because it was dark outside.

Then a young man better dressed and better looking than any of us presented himself at our table. "Good evening, my name is Paul, and I'll be your waiter this evening. Would you like a few minutes before I take your order?"

"No," I said. "I'm just a meat-and-potatoes guy, so I'll have the filet mignon and a baked potato."

"Soup or salad?"

"Salad."

"We have a mixed-green salad, hearts of palm or a very fine endive salad with baby shrimp."

"Just a mixed-green salad, okay?"

"Whatever you say, sir. Dressing?"

I didn't want to make another decision. "Whatever you've got will be fine."

"We have creamy Italian, blue cheese, vinaigrette, Thousand Island, honey Dijon, ranch…"

"Just bring me one. Surprise me."

"Creamy Italian is our house specialty. Would that be all right, sir?"

"Yeah." I was curt. I was done with civility.

"And your baked potato..."

I knew what was coming. "I just want the baked potato dry, you understand? I don't want anything on it."

"No butter? No sour cream?"

"No."

"No chives?"

"No! Don't you understand English?" I shouted. "I don't want anything on it. Just bring me a baked potato and a steak."

"Would you prefer the six-, eight or 12-ounce steak, sir?"

"Whatever."

"Would you like that rare, medium rare, medium, medium well or well done? Or, if you prefer, we can butterfly it for you."

"Pauly Boy," I said, "you are really starting to get me steamed."

"Which brings up the vegetables, sir. Would you like steamed broccoli, creamed corn, sautéed zucchini, diced carrots—"

That did it. I threw my napkin to the floor, stood up, put my face right in his arrogant kisser and said,

"How'd you like to settle this outside?"

"Fine with me, sir. Would you prefer the parking lot, the side alley or the street in front of the restaurant?"

"I prefer right here," I said, and sucker-punched him.

He ducked, then countered with a left hook right under my eye. It was the first time all night he hadn't offered me a selection. I collapsed semiconscious into my chair, as someone in authority rushed over and berated Pauly.

I felt my tie being loosened, my collar unbuttoned, hands slapping my face. When I regained my senses, I saw the very concerned maitre d' right in front of my nose. He apologized and offered to buy me a drink, call the paramedics—whatever I wanted.

"No, no," I said. "I'll be all right. Just bring me a glass of water."

"Yes, sir, right away," he said. "Would you prefer imported mineral water, sparkling water or club soda with a wedge of lime?"
```

---

## IC-2157: Wayside School Gets a Little Stranger

- Title: Wayside School Gets a Little Stranger
- Author (byline): Louis Sachar
- Work: Not specified
- Publisher: HarperTrophy
- Publication date as stated: Feb 1996
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1076
- Already set (do not supply): none

### Source block (context only)

```text
Author: Louis Sachar
ISBN: 978-0380723812
Publisher: HarperTrophy
Date (Month/Year): Feb 1996
```

### Introduction (context only: never use it for content warnings)

```text
All the kids from Wayside School had to spend 243 days in horrible schools while Wayside closed to get rid of the cows (Don't ask!). Now the kids are back, but the big surprise is that their favorite and strangest teacher, Mrs. Jewls, is expecting a baby -- one named Cootie Face or Bucket Head--and a substitute teacher is coming . . .

Now, having a substitute teacher can be great for many students. They either give you an easy assignment or let you watch a movie, but then there are the weird subs, who take their job way too seriously, or the downright evil subs who just don’t like children at all. Wendy Norad, the final substitute for Ms. Jewls falls into the last category . . . and this is why!

The back-story of Ms. Norad from Wayside School Gets a Little Stranger by Louis Sachar.
```

### Performance text (classify this)

```text
Wendy had three. Ears, I mean.

She had one ear on each side of her head, just like most people. But she also had a third ear, which lay flat on top of her head.

You couldn’t see it. It was completely covered by her thick, frizzy brown hair.

She was an intelligent and lovely young woman. She was gentle and kind. At least, she used to be. Then she met Xavier and became evil and wicked, but I’ll get to that later.

She lived in a small apartment in the big city. She always kept fresh flowers in the vase on her kitchen table. She didn’t have any friends. She was afraid someone might find out about her ear. She was very embarrassed by it. The one on top of her head, I mean. The other two ears were pretty, as ears go. Actually, the third ear wasn’t ugly. In fact, it looked just like the other two. It was quantity, not quality, that bothered her.

Then she met Xavier. It was at a museum. They happened to be standing next to each other looking at the same painting. The Mona Lisa. A guard stood by to make sure they didn’t touch it. Xavier was very handsome. But he was frightfully shy. He was afraid of women.

“That’s a beautiful painting, isn’t it?” said Wendy.

Xavier blushed. He wanted to speak, but his mouth locked shut with fear. It took all his courage just to nod his head. But Wendy knew he liked her. Because there was something else about her ear I haven’t told you yet. The one on top of her head, I mean. It didn’t hear normal sounds. It heard people’s brains. Wendy was able to listen to Xavier’s secret thoughts. And this is what she heard.

Yes, the painting is very beautiful. But you are more beautiful than the Mona Lisa. I wish somebody would paint your picture. I would buy it and look at it all day. Alas, if only I had the courage to talk to you.

Wendy didn’t usually listen to other people’s thoughts. She thought it was rude, even though the other people didn’t know she was listening. Besides, most people’s thoughts were usually boring. Xavier was getting too nervous standing next to her. He moved on to another painting. Wendy followed him. She listened to the lonely man’s thoughts. They weren’t boring at all. Most of his thoughts were about her, but she also learned a few other things. He liked to read his favorite author was Charles Dickens. He loved animals, especially dogs.

“That painting reminds me of a book,” said Wendy. “A tale of two cities, by Charles Dickens. Have you read it?”

“Yes!” Xavier blurted, a little too loudly. “It’s my favorite book! I’ve read everything Dickens has ever written. Twice. My favorite part is when-“He suddenly stopped, very embarrassed.

“Please go on,” said Wendy.

“No, I don’t want to bother you.” said Xavier.

“You’re not bothering me,” said Wendy. “Charles Dickens is my favorite author. I sometimes read aloud to my dog.”

“You have a dog?” asked Xavier. Wendy nodded. Xavier stared into her dark eyes. “I love dogs.” he said, as his brain said I love you.

Wendy and Xavier spent the afternoon together. He could hardly stop talking. It was like a genie had escaped from a bottle. All the love and emotion that had been buried for so long inside him came pouring out on Wendy. “I don’t even know your name,” he suddenly blurted.

“Wendy Nogard,” said Wendy.

“I’m Xavier Dalton.” said Xavier. They shook hands and made plans to meet again at the museum the following week.

On her way home, Wendy stopped by the library and checked out a tale of two cities. Then she went to the pet store and bought a dog.

A month later. Xavier asked her to marry him. Wendy didn’t know what to say. She loved Xavier. And she knew he loved her. But she still hadn’t told him about her ear. The one on top of her head, I mean. He knew about the other two. He had nibbled on each of them.

“Marriage is a big step.” she said. “I’m afraid we haven’t known each other long enough.

“I’ve known you long enough to know I could never be happy without you.” said Xavier. “Before I met you, Wendy, I was sad and lonely. But I was used to it. Now I can’t imagine living like that again. I don’t know what I’d do without you.” He stroked her hair.

“Well, there’s this one little thing you don’t know about me,” said Wendy. His hand bumped into it. “What’s this thing?” he asked.

“That’s what I was going to tell you about, dear.” said Wendy. Xavier parted her hair and looked at it.

“It’s an ear!” he exclaimed.

“Yes, it is.” said Wendy. “Some people have two ears. I have three. Now that you know, if you still want to marry me, my answer is yes! Yes, sweetheart, yes!”

“I love you,” said Xavier. “That’s all that matters to me.” That was what he said. But this is what he was thinking.

Oh, gross! You’re disgusting! I never want to touch you again! I can’t even stand to look at you! You tricked me, you freak! You monster!

And of course, Wendy heard every word.

He stood up. “I’ll be right back, sweetheart. I bought you diamond earrings as an engagement present. I just need to run back to the jewelry store and buy one more.” He hurried out the door. She never saw him again.

I’m sorry to say this story has a sad ending. Xavier, thanks to Wendy, got over his shyness. He went out with lots of women but broke each one’s heart. He could never love any of them. There was a hole in his heart. He was in love with Wendy Nogard, but he didn’t know it. And so he could never be happy.

Wendy became a bitter and evil person. She was unhappy, and she wanted everyone else to be unhappy too. Whenever she heard someone thinking happy thoughts, she would listen closely and then do and say just the right thing to make the person feel rotten. She hated children the most.

Every time she passed a playground, she heard them laughing and having fun. So she became a substitute teacher.
```

---

## IC-2158: Wear Sunscreen: A Primer for Real Life

- Title: Wear Sunscreen: A Primer for Real Life
- Author (byline): Mary Schmich
- Work: Not specified
- Publisher: Andrews McMeel Publishing
- Publication date as stated: Originally published in the Chicago
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 674
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mary Schmich
ISBN: 978-0836255287
Publisher: Andrews McMeel Publishing
Date (Month/Year): Originally published in the Chicago
Tribune June 1997
```

### Introduction (context only: never use it for content warnings)

```text
Mary Schmich's original column became a cultural phenomenon soon after it appeared. It was posted on Web pages and e-mailed to thousands of people as the text of novelist Kurt Vonnegut's commencement speech at the Massachusetts Institute of Technology. Unfortunately, Vonnegut had not delivered the speech at MIT. But the column went on to attract the notice of Australian movie director Baz Luhrmann. Luhrmann made the column the basis of a novelty song titled Everybody's Free (To Wear Sunscreen) on the album Something for Everybody , released in Australia in late 1997. Today I present this speech to you in it’s original form, a witty and humorous take on the graduation speech we'd all like to make if given the opportunity. Wear Sunscreen by Mary Schmich.
```

### Performance text (classify this)

```text
(adapted by Baz Luhrmann)

Ladies and Gentlemen of the class of '99: Wear sunscreen.

If I could offer you only one tip for the future, sunscreen would be it. The long term benefits of sunscreen have been proved by scientists, whereas the rest of my advice has no basis more reliable than my own meandering experience.

I will dispense this advice now.

Enjoy the power and beauty of your youth; oh never mind; you will not understand the power and beauty of your youth until they've faded. But trust me, in 20 years you’ll look back at photos of yourself and recall in a way you can’t grasp now how much possibility lay before you and how fabulous you really looked. You’re not as fat as you imagine.

Don’t worry about the future; or worry, but know that worrying is as effective as trying to solve an algebra equation by chewing bubblegum. The real troubles in your life are apt to be things that never crossed your worried mind; the kind that blindside you at 4pm on some idle Tuesday.

Do one thing everyday that scares you.

Sing.

Don’t be reckless with other people’s hearts; don’t put up with people who are reckless with yours.

Floss.

Don’t waste your time on jealousy; sometimes you’re ahead; sometimes you’re behind; the race is long, and in the end it’s only with yourself.

Remember the compliments you receive; forget the insults. If you succeed in doing this, tell me how. Keep your old love letters; throw away your old bank statements.

Stretch.

Don’t feel guilty if you don’t know what to do with your life; the most interesting people I know didn’t know at 22 what they wanted to do with their lives; some of the most interesting 40 year olds I know still don’t.

Get plenty of calcium.

Be kind to your knees; you’ll miss them when they’re gone.

Maybe you’ll marry -- maybe you won’t. Maybe you’ll have children -- maybe you won’t. Maybe you’ll divorce at 40 -- maybe you’ll dance the funky chicken on your 75th wedding anniversary. Whatever you do, don’t congratulate yourself too much or berate yourself either -- your choices are half chance; so are everybody else’s.

Enjoy your body; use it every way you can. Don’t be afraid of it, or what other people think of it. It’s the greatest instrument you’ll ever own.

Dance -- even if you have nowhere to do it but in your own living room.

Read the directions, even if you don’t follow them.

Do NOT read beauty magazines; they will only make you feel ugly.

Get to know your parents; you’ll never know when they’ll be gone for good. Be nice to your siblings; they are the best link to your past and the people most likely to stick with you in the future.

Understand that friends come and go, but for the precious few you should hold on. Work hard to bridge the gaps in geography, in lifestyle, because the older you get the more you need the people you knew when you were young.

Live in New York City once, but leave before it makes you hard;

Llve in Northern California once, but leave before it makes you soft.

Travel.

Accept certain inalienable truths: price will rise; politicians will philander; you too will get old, and when you do you’ll fantasize that when you were young prices were reasonable, politicians were noble, and children respected their elders.

Respect your elders.

Don’t expect anyone else to support you. Maybe you have a trust fund; maybe you have a wealthy spouse; but you never know when either one might run out. Don’t mess too much with your hair, or by the time you're 40, it will look 85.

Be careful who advice you buy, but be patient with those who supply it. Advice is a form of nostalgia: dispensing it is a way of fishing the past from the disposal, wiping it off, painting over the ugly parts, and recycling it for more than it’s worth.

But trust me on the sunscreen.
```

---

## IC-2159: The Web Files

- Title: The Web Files
- Author (byline): Margie Palatini
- Work: Not specified
- Publisher: Hyperion
- Publication date as stated: May 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: DUCKTECTIVE WEB, ROOSTER, BILL, WEB, HEN, LITTLE BOY BLUE, HORSE, SHEEP, RAT
- Teaser before the introduction: No
- Spoken words (computed): 959
- Already set (do not supply): none

### Source block (context only)

```text
Author: Margie Palatini
ISBN: 978-0786804191
Publisher: Hyperion
Date (Month/Year): May 2001
2009 National Qualifier
IA State Qualifier
KS State Qualifier
*Thematic Opening for Dragnet 1951-1959
https://www.youtube.com/watch?v=o1hgGchn8p8
```

### Introduction (context only: never use it for content warnings)

```text
Vocalizes Opening Theme from Dragnet (1951-1959) * Spoken as Ducktective Web: Ladies and Gentlemen, the
```

### Performance text (classify this)

```text
story you are about to see is true. The names have been changed to protect the innocent. This is the farm. Hundreds of animals. Most of them follow the course as planned. A few of them get lost along the way. When they do, it makes trouble for me. I’m a Ducktective. I carry a badge (flips open badge)

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

HORSE: You say to-MAY-toes . . . I say to-MAH-toes . . .

Somebody just hauled the whole thing off!

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

WEB: (picking a piece of lettuce from under his chin) Not clean enough, you Dirty Rat. (he smells Rat’s breath)

Just as I suspected. Garlic mayo. Book him, Ducko. His salad days are over.

RAT: (Crying, as his hands are cuffed and he is led away) Over? Over? But they can't be over! I haven't even had my dessert!

BILL: (Patting Web on the back) Looks like you quacked another one, Web. But how did you ever figure it was him?

WEB: Just played a hunch. He ate the evidence for lunch . . . and forgot to use his napkin and brush his teeth. He's a dirty rat. He never did have good hygiene.

DUM DE DUM DUM

WEB: The Dirty Rat was tried and convicted on three counts of vegetable vagrancy, offensive bad breath, and not using a napkin to wipe under his chin. He was sent up the river and was sentenced to six months of farm labor with time off for good behavior, better table manners, and clean teeth. CASE CLOSED.

DUM DE DUMDUM DUM DE DUMDUM DUM DUM!
```

---

## IC-2160: What It Means When a Man Falls From the Sky

- Title: What It Means When a Man Falls From the Sky
- Author (byline): Lesley Arimah Nneka
- Work: Not specified
- Publisher: Riverhead Books
- Publication date as stated: April 2017
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, GRANDDAUGHTER, FATHER, NNEOMA, BOY, GIRL, MAN, KIONI
- Teaser before the introduction: Yes
- Spoken words (computed): 1475
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lesley Arimah Nneka
ISBN: 978-0735211025
Publisher: Riverhead Books
Date (Month/Year): April 2017
```

### Introduction (context only: never use it for content warnings)

```text
Welcome to the future – a world ravaged by climate change and geopolitical conflict. As its inhabitants lament the plight

(or the intrusion) of refugees fleeing turmoil, many take solace in a discovery that is said to have the ability to ease all human pain. Furcal’s Forumla has been discovered and the Mathematicians, though there are few, can calculate a person’s emotional agony and then undo it. A world without pain . . . a world without suffering? It sounds like Heaven.

But. . . some Mathematicians have pushed past their limits with grievous results and are using the Furcal Formula to manipulate the physical world.

What it Means When a Man Falls from the Sky by Lesley Arimah Nneka
```

### Performance text (classify this)

```text
NARRATOR: What does it mean when a man falls from the sky? (Pg 151-174) It means twenty-four-hour news coverage. It means politicians doing damage control; activists egging on protests. It means Francisco Furcal’s granddaughter at a press conference defending her family legacy.

GRANDDAUGHTER: (into a microphone) My grandfather's formula is sound. Math is constant and absolute. Any problems are the fault of those who miscalculate it.

NARRATOR: 2,400 Mathematicians worked the globe and made their living calculating and subtracting emotions, drawing them from living bodies like poison from a wound.

Nneoma was one of 57 registered Mathematicians who specialized in calculating grief, down from 59 last year. Alvin Claspell had committed suicide after, if the stories were to be believed, going mad and trying to eat himself. And Kioni Mutahi has simply disappeared.

This work wasn't for everyone. It wasn’t a profession you chose or aspired to; you could either do it or you couldn’t.

For Nneoma, it started when she was fourteen, in math class. The teacher had showed them a long string of Furcal’s Formula, purchased from the Center like a strain of a virus. To most of the other students, it was an impenetrable series of numbers and symbols, but to Nneoma it was as simple as the alphabet. From then on she could see a person’s sadness as plainly as the clothes he wore. And now, she’d been doing it for so long she could exorcise the deepest of traumas for even the most resistant of patients.

A message dinged on the phone console -- her assistant reminding her of the lecture she was to give at the school. She gathered her papers and rang the car, which pulled up to the glass doors almost immediately. They drove through the wide streets and passed a playground full of sweaty egg-white children. It wasn’t that Nneoma had a problem with the Britons per se, but some of her father had rubbed off on her. At his harshest Father would call them refugees rather than allies

FATHER: They come here with no country of their own and try to take over everything and don’t contribute anything.

NARRATOR: That wasn’t entirely true. When the floods started swallowing the British Isles, they’d reached out to Biafra, a plea for help that was answered. Terms were drawn, equitable exchanges of services contracted. But while one hand reached out for help, the other wielded a knife. Once here, the Britons had insisted on their own lands and their own separate government. A compromise, aided by the British threat to deploy biological weapons, resulted in the Biafra- Britannia Alliance. Shared lands, shared governments, shared grievances. Better a mutually beneficial, if unwanted, alliance than what the Americans had done in Mexico.

When things began to fall apart, the world cracked open by earthquakes and long dormant volcanoes stretched, yawned and bellowed, the churches (mosques, temples) fell, not just the physical buildings shaken to dust by tremors, but the institutions as well. Into the vacuum stepped Francisco Furcal, a Chilean Mathematician who discovered a formula that explained the universe. It, like the universe, was infinite and the idea that the formula had no end and, perhaps, by extension, humanity had no end, was exactly what the world had needed.

Over decades, people began to experiment with this infinite formula, and in the process discovered equations that coincided with the anatomy of the human body, making work like hers possible. Then the rumors started that Furcal’s Formula was wrong.. They were just that, rumors, but then a man fell from the sky.

As they neared the school, they could see a few protesters with gleaming electronic placards. The angry red of angry men. Nneoma greeted the class -- filled with bored faces, most around thirteen or fourteen with few caring or understanding what she did, too untouched by tragedy to understand her necessity. But schools like these, which gathered the best and brightest several nations had to offer, paid the Center handsomely to have people like her speak and it was the easiest money she earned.

NNEOMA: How many of you can look at someone and know that they are sad?

NARRATOR: The whole class raised their hands.

NNEOMA: How many of you can look at a person who is sad, know why they are sad and fix it?

NARRATOR: All hands lowered. She had their attention now…

NNEOMA: Some Mathematicians remove pain, some deal in negative emotions, but we all fix the equation of a person. The bravest (she winked) have tried their head at using the Formula to make the human body defy gravity, for physical endeavors, like flight.

BOY: What you are doing is wrong. My dad says that you shouldn’t be stopping a person from feeling natural hardships. That’s what it means to be human.

NARRATOR: She studied the boy and noted on his wrist his father’s occupation (lawyer), his class (first). People who’d lived easy lives, who’d had moderate but manageable difficulties then dared to compare their meager hardship with unfathomable woes.

NNEOMA: Your father and those people protesting outside have no concept of what real pain is. Their feelings on this matter are invalid. I would never ask a person who hasn’t tasted a dish whether it needs more salt.

GIRL: (raises hand)

NNEOMA: (thinking) Not her, not her!

NARRATOR: She’d been trying to ignore the girl since she walked into the classroom. She didn’t need to look at her wrist to know that the girl was Senegalese and had been affected by the Elimination. It was etched all over her, this sorrow.

GIRL: (with obvious pain in her voice) So you can make it go away?

NNEOMA: Yes, I can. But it is a highly regulated and very expensive process. Most of my clients are heavily subsidized by their governments, but even then. You have to be a citizen.

NARRATOR: The girl lowered her eyes to her lap, fighting tears. The Elimination began after the French had won the trust of their Sengali hosts. The Senegalese newspapers that issued warnings were dismissed as conspiracy rags, rabble-rousers inventing trouble. But then the camps, the raids, and the mysterious illness that wiped out millions. Then the cabinet members murdered in their beds. The girl must have lived through the unthinkable. The weight of her mourning was too much, and Nneoma left the room..She saw the sign for the ladies room and stepped inside.

NNEOMA: (checking the stalls to make sure she is alone, she bends forward taking deep breaths)

NARRATOR: The bathroom door creaked open. Nneoma knew who it was. The girl couldn’t help but to seek her out. Nneoma held out her arms and the girl walked into them. And Nneoma saw the sadness. The girl’s mother shredded by gunfire. Her brother taken in the night by a gang of thugs. Her father falling to the synthesized virus that attacked all the melanin in his skin till his body was an open sore. Hunger so deep she’d swallowed fistfuls of mud. (Beat)

Nneoma worked almost exclusively with parents who’d lost a child, wealthy couples who’d thought death couldn’t touch them, till it did. When the Center partnered with governments to work with their distressed populations, it was Kioni Mutahi who worked with those people full time. Until she disappeared.

NNEOMA: (holding the girl in her arms she absorbs all the pain and suffering, she begins sobbing)

NARRATOR: No one had really been able to explain why one person could take another person’s grief.

Mathematical theories abounded based on how humans were, in the plainest sense, a bulk of atoms held together by positives and negatives, an equation all their own, a type of cellular math. A theologian might call it a miracle, a kiss of grace from God’s own mouth. But in that room, it simply meant that a girl had an unbearable burden and then she did not. (Beat) The ride back home was silent. As she cleared the corner around her compound, she saw a small crowd gathered at her gate. Protesters? she wondered in shock before she registered the familiar faces of her neighbors.

MAN: We called medical right away. She was banging on your gate and screaming.

NARRATOR: The woman wore no shoes and her toes were wounds. How on earth had she been able to bypass city security?

NNEOMA: (recognizing her colleague) Kioni?

KIONI: (frantically she looks about her in fear) Nneoma we have to go, we have to go now.

NARRATOR: Every bare inch of her skin was scratched or bitten or cut in some way. Her usually neat dreadlocks were half missing, her scalp raw and puckered like someone had yanked them out. The smell . . .

NNEOMA: Who did this to you?

NARRATOR: And then she remembered Alvin Claspell and the stories of him trying to eat himself.

KIONI: (sobbing) They just come, and they come and they come.

NARRATOR: How many people had Kioni worked with over the last decade, five thousand? Ten? Ten thousand traumas in her psyche, squeezing past each other, vying for the attention. What would happen if you couldn’t forget, if every emotion from every person whose grief you’d eaten came back? It could happen if something went wrong with the formula millions and millions of permutations down the line. A thousand falling men landing on you. . . The breadth of it was so vast, too vast.
```
