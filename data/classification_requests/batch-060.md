# Classification request: batch 60 of 63 (40 records, IC-2361 to IC-2400)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-060-reply.json`.

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

## IC-2361: The Acorn People

- Title: The Acorn People
- Author (byline): Ron Jones
- Work: Not specified
- Publisher: Laurel Leaf
- Publication date as stated: June 1996
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NURSE, SPIDER, BENNY, AARON, MARTIN, THOMAS
- Teaser before the introduction: Yes
- Spoken words (computed): 1637
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ron Jones
ISBN: 978-0440227021
Publisher: Laurel Leaf
Date (Month/Year): June 1996
```

### Introduction (context only: never use it for content warnings)

```text
Ron expected that his time as a counselor at Camp Wiggin would be filled with sunny days spent hiking, swimming, and boating. But when he arrives on day one, his illusions are quickly shattered. But everything changes once Ron gets to know his group -- kids who call themselves the Acorn People. The campers teach him that, inside, they are the same as any average kid, and with encouragement, determination, and friendship, nothing is impossible.

The Acorn People by Ron Jones
```

### Performance text (classify this)

```text
(Pg 1) Children spilled from cars and buses. The woods and paths of Camp Wiggin were accustomed to troops of running feet and the noise of children at play. With these wheelchair children there was only silence. It was as if the woods themselves were watching the unfolding of chairs and the lifting of bodies. All life seemed to stop. In procession, the parents wheeled their children toward awaiting counselors. I was a counselor. Like everyone around me, I didn't know what to say.

(Pg 1-3) What do you say to a parade of children who move toward you only by the energy of their parents' insistence? Who move toward you with swollen heads of gargantuan proportion. With birth scars that have left the eyes without sight or the body without arms and legs. Children who seem drained of expression. Crumpled and stuffed into wheelchairs. Covered with blankets, to ward off not the cold, but the vision of disfigurement. The camp nurse had given us a one-day orientation about handicapped children.

NURSE: Most will not live past their teen years. It is nature’s way. She described the hydrocephalic children with heads that looked like melons about to burst. And the disease of multiple sclerosis, which ate away at the muscles, leaving the body without energy or movement. The children who had mongoloid faces and a distant stare. And finally the children who entered life without vision or a hand or perhaps a face. (beat) There were two counselors for each cabin of five children. I shared counseling duties with Dominic Cavelli from New York. He was after a career working with handicapped children. (Pg 4) [But it was] the thought of playing with kids, swimming all day, and taking long hikes had drawn me to this place. My illusions were quickly washed away. I wasn't about to frolic with these children. We would be lucky if we could even take a few steps together. (beat) (Pg 9-10) The first of our kids was Benny. Polio had taken his legs but not his gall or heart. Most kids have a "thing" they do. Something special. For Benny it was speed. With a crash helmet pulled tightly over his head, he hunched forward in his wheelchair like a dirt-track driver in a stock car. (Pg 10-11) Spider was another kid in our cabin. It was a funny name because Spider didn't have any legs or arms. He had stumps that stuck out from his short frame like broken branches out of a tree. Like Benny, Spider was alert and perceptive. You could tell by his eyes. Spider's eyes held everything. And what his eyes couldn't hold, his mouth tried to trap. Spider loved to talk. (Pg 11-12) Far less active and alert than Benny or Spider was Thomas Stewart. He had muscular sclerosis, the cruelest ailment of all. Thomas must have been sixteen. It was hard to tell. Benny and Spider looked and acted like the eight- and ten-year-olds they were. But Thomas weighed about 35 pounds. Picking him up was like holding a collapsible tent. Thomas’ mouth was always pinched tight, as if to hold.in some final scream. He watched the world about him but gave nothing to it. Unwilling to move unless moved. Pensive, patient, and dying. (Pg 12) Martin was the most able-bodied child in our group. Like other blind children in camp, he had a constant smile and seemed in perpetual motion. Sitting still, he would rock forward and back. Even standing, he swayed rhythmically. He was about fourteen, with bright red hair that stuck out in every direction. (Pg 13) Aaron Gerwalski was the fifth kid under our charge. Aaron didn't have a bladder. A large, bag was attached to his intestines. Strapped to his leg, it collected urine that had to be emptied every hour. This condition was terrible for anyone, but for a teenager it must have been overwhelming. The smell repelled any gesture of friendship. It stalled and interrupted any conversation before it could begin. (beat)

(Pg 14-15) Our first day we were assigned to the craft area. I rounded up Benny, got Martin to work with Spider and gave the quiet Thomas Stewart and Aaron each a private workspace. I busied myself with a nut necklace. An act of frustration that symbolized how I felt. Crazy to be here. Absolutely crazy. Spider asked what the necklace was for. . . "I feel a little weird being here, so I've made myself a necklace of nuts."

SPIDER: So do we. We're all a little nutty here!

BENNY: You might call us the nut people. Yeah, that's a good name for us.

SPIDER: Can we make a necklace like yours? Benny raced about collecting every nut in sight. And soon we all had this crazy nut necklace in common.

SPIDER: (Pg 16) We’re the Acorn People! (Pg 22) And the Acorn People were on the move . . . (Pg 25-26) The following day we [went] to the pool. [It] was being used by a group of girls! Participants in this first ever "integrated swim" were self-conscious and then flirtatious. The boys worried about their hair. My God, I had to comb their hair before they would venture out to poolside. [But] soon, the sun and water worked their magic. Children -- no, young adults -- no, children were playing games. Even Thomas Stewart, the most distant of all -- I caught him smiling for the first time when he oh so slightly nudged a girl. (Pg 27-28) There was a great deal of speculation as to who had a crush on whom. There was a new excitement in the air. Leaving the pool area, I noticed that a blind girl named Mary was wearing an acorn necklace. The question of how she got the necklace slid from my mind until Aaron complained.

AARON: I've lost my necklace . . . hey, can we stop so I can make another?

BENNY: Couldn't be you gave it to Mary ... could it? Aaron looked slightly sick and then relieved as Mar-tin saved the day with an idea.

MARTIN: Let's make a bunch of necklaces, OK?

BENNY: Yeah, we can give them to our girlfriends. We set about making acorn necklaces by the gross. By the end of the afternoon, there wasn't an acorn anywhere in sight. Not one. Throughout the days that followed they gave them to everyone. The entire camp - - kids, counselors, and even Mrs. Nelson, the nurse became Acorn Society members. (Pg 29) The giving of the necklaces drew the camp together and gave us all a feeling of confidence and a penchant for adventure. One particular adventure I shall never forget was the mountain. (Beat) One evening the normal recorded taps and Boy Scout pledge were followed by an announcement that special merit badges would be awarded to all those completing the climb to Lookout Mountain.

BENNY: If the Boy Scouts can climb that mountain, can we? (Pg 30) In the morning we made plans. Maps in the camp office gave the trail markings and location of the mountain. It was a six-mile hike round trip. We had no idea of the terrain. We took a bag of apples, some carrots, raisins and canteens of water. Dominic led the way pushing Spider. Next came Benny, wheeling himself, followed by Martin pushing Aaron. I took up the rear pushing Thomas Stewart. (Beat) Each curve in the trail presented an obstacle; (Pg 31-32) but when the trail started upward, we had to turn around and pull the chairs from behind. (Pg 34) Our movement was reduced to pull, stop. Pull, stop. Pull. Perspiring and heaving for breath, Benny had to stop. He didn't say a word. Just stopped pushing. His chair slowly slid to a halt against Martin. Like a train being derailed we twisted to a halt.

SPIDER: (Pg 35) (dramatically sprinkling water from his canteen on the hillside) I hereby name this place Benny's Landing and claim this place and all its riches for the Acorn Society. (beat) (Pg 36) Well, what are you waiting for, Aaron? Break out the food! Here we were, sitting in the middle of a forest with wheelchairs that had until now known only city streets and "convenience ramps." (Beat) (Pg 62-63) Later that night camp filled with the chorus of Cum Ba Yah. We were at peace with the world. And what a marvel -Thomas singing faintly for the first time.

THOMAS: (singing) Someone’s singing, Lord, Cum Ba Ya Why can't life be like this? Human beings in all their magnificence, working to find that moment of pride. The feeling of belonging not just to oneself but to the entire universe. (Beat)

Camp days fled by. "How many days left?" was a constant question. The kids seemed to withdraw gradually but perceptibly into cocoons. Thomas stopped talking. Many children displayed symptoms of illness that marked their first few days at camp. Bedwetting returned. Kids on special diets who had been eating regular meals requested their pills again. (Pg 78) [Then it was the final day of camp]. Now a silent exchange was taking place again. Children were being passed from counselor back to parent. Benny rolled slowly by himself from our presence. Spider was passed from arm to arm. Martin walked holding my hand. He was leading. Thomas Stewart had to be carried. His eyes were a little older and sadder. Aaron wanted to push himself to show his parents his strength. [These were] the members of the Acorn Society -- -- racers, [swimmers], mountain climbers, observers, [and above all children] And they were dying.

NURSE: (Pg 2) Most will not live past their teen years. It is nature’s way. (long beat) (Pg 80) Thomas and Aaron died one year after summer camp. Spider was killed by a car the following year. Martin died in a car accident four years later. Benny was the last child to leave this [world]. Of all the children he was the only one to have a funeral. At the final service Benny's mother gave me a white envelope. Inside was a crumpled acorn necklace. She said he gave them to everyone he met. (beat)

SPIDER: (Pg 35) I hereby name this place Benny's Landing, and claim this place and all its riches for the Acorn Society . . .
```

---

## IC-2362: Admiral of the Swiss Navy

- Title: Admiral of the Swiss Navy
- Author (byline): Sam Lipsyte
- Work: Venus Drive: Stories
- Publisher: Picador
- Publication date as stated: March 2010
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, STEVE-IVAN, VAN WORT, MR. MARV, FATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1537
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sam Lipsyte
Book: Venus Drive: Stories
ISBN: 978-0312429607
Publisher: Picador
Date (Month/Year): March 2010
```

### Introduction (context only: never use it for content warnings)

```text
S ummer break – A time to relax from the rigors of school and re-connect with nature. For many students this may mean summer camp. Fresh air, new friends, and new social dynamics. For self-assured teens, this may be true and the experience will create memories and friendships that will last a lifetime. But for others, the ones that find themselves to be the “Odd Camper Out” – the experience can be a traumatic ordeal.

There is a fine line between “boys will be boys” and toxic bullying. And sometimes that line becomes a matter of life or death. You see, no matter what people say . . . the victim NEVER brings it on himself.

The Admiral of the Swiss Navy by Sam Lipsyte
```

### Performance text (classify this)

```text
NARRATOR: I can’t remember the name of the camp. It was somewhere near a lake near Canada. That summer some of us used to go smoke cigarettes behind the Port-O-Sans. Mr. Marv caught us one time, wanted to make a point.

Mr. Marv wore swim togs and parted his hair like a magician. They said he was a teacher of history in the winter somewhere. That summer, though, he was just Mr. Marv, blitzed at the bonfire, babbling on about the time he was a kid and sneaked into a ball game.

He was going to send us packing, which I guess is not a big deal looking back, but at the time it was seen as a stain. Plus, to have your dad drive up in that sad kind of station wagon. What I did was give Mr. Marv some of the names he needed. I gave him the names of boys you’ve never heard of but who were known saboteurs of good camp citizenship. I’m not sorry I did it, either. If I saw those boys today, I’d say, “You brought it on yourselves.”

NARRATOR: Van Wort was the fat kid who put our camp all over the local news that summer, and if you were watching TV back then, you might have caught my debut. I was the one standing in the dining hall saying, “He brought it on himself.”

I don’t think I believed that, even then, but I guess I wanted to say something memorable, something beyond my years. I could have said what a terrible tragedy it all was, but Mr. Marv seemed to be in charge of that part.

***************

NARRATOR: I slept next to Van Wort. I listened to the air whistle in and out of his fat chest. He said he had a chronic bronchial. He said it like a lie he made up a long time ago.

I watched them come to him night after night, boys with their mosquito sprays, their shampoos, tennis rackets and combs, warm water in toothbrush cups. Van Wort was fat and his name was Van Wort. With that combination, why would you pack your kid off to camp? Let him play with ladybugs in the safety of his own lawn.

The counselor tortured Van Wort, too. He was just a mean kid with more years on him, more muscles. His name was Steve, or maybe Ivan. Steve-Ivan called Van Wort Van Wort Hog. Or Fat S***, for short. He was the one who told us to piss in Van Wort’s canteen. It was the best canteen in the bunk, brand new, fuzzy wool, a cavalry sleeve. We took turns pissing in it and dipping it down in the Port-O-San hole. We left it under his short-sheeted bed.

When he found it, his eyes went dark, his great arms started wibbling, wobbling on his knees. The canteen, he told us, was a gift from his dead father.

STEVE-IVAN: It’s just a joke you fat s***. We’re your friends.

VAN WORT: (wanting to believe) Really?

STEVE-IVAN: Sure. Just don’t be a Van Wort Hog and run crying to Mr. Marv.

NARRATOR: Van Wort stopped crying and he didn’t run but he went to see Mr. Marv. Steve-Ivan was somebody’s cousin near Canada, though. The whole thing blew, as they say, over. ***************

NARRATOR: We did a camp-wide Capture-the-Flag. I wasn’t in Van Wort’s unit, but I can tell you things got pretty hairy out there. What happened to this one girl in the beet field was a shame. We never did know what the rules were, or which kids were still living or dead. My unit just marauded around. We laid waste to Mr. Marv’s azaleas and tied a boy to the tetherball pole. Then we lucked into view of the flag, this dinky fluorescent thing, planted on a hill. We flew up along a ridge near the tennis courts. Van Wort appeared out of nowhere with a croquet mallet in his hands. Some of us batted the mallet away and beat Van Wort to the dirt. I led the rest of them. I didn’t want to know what they were doing to Van Wort [because] . . . victory equaled a sack of candy bars, to be divided evenly among all living members of our unit.

Van Wort spent the night in the infirmary, though a boy who was there for a spider bite said there were no visible marks.

***************

NARRATOR: We played Freeze-Please every breakfast, lunch, and dinner. Steve-Ivan would say “Freeze, Please” while we were eating and we’d all go stone-cold statue. Whoever moved first was Admiral of the Swiss Navy, which meant you had to scrape and stack the dishes, bus them over to the kitchen. The Swiss have no navy, but who knew that then?

We called Van Wort the Commodore because he couldn’t hold still. I think it was unfair, really, because it wasn’t so much him as his fat that was moving, if that makes any sense at all. Study a fat kid hard and it might.

STEVE-IVAN: Well, it looks like another lucky day for the Hog.

NARRATOR: “I’ll help him,” I said. Everyone gawked, as though I’d been struck with sudden bolts of lightning, but it was just this feeling I had, that Van Wort was getting a bad break. He wasn’t so off. He wasn’t even weird. It wasn’t like he wrote bird poems or wore the wrong kind of underwear.

VAN WORT: Why are you doing this?

NARRATOR: Just because.

VAN WORT: I don’t care what you do to me. If it’s a trick, it’s a trick.

NARRATOR: We were quiet and stacked for a while. (to Van Wort) So, who killed your dad?”

VAN WORT: Nobody killed him. He dropped dead. I saw it. He went blue and had a bubble on his mouth.. ***************

NARRATOR: Each night they came to his bed where he lay wheezing. It wasn’t even foot powder and Indian burns anymore. They wanted to hurt him, to make him bleed. They taped him down to the bed frame, went at it with tweezers and pocketknives. They got his sock bunched up for a ball gag. They pinched off pieces of him with nail clippers and tiny sewing shears from kits their mothers had packed.

I’d get up and walk to the other end of the bunk until they were done. In the morning I’d help him clean up, wipe down the blood until it was just dark nicks. We talked about everything except what they did to him.

He told me he had given the eulogy at his father’s funeral, that it was easy, he’d just used an essay he’d written for school and substituted “my father” for “our founding fathers.”

I started to admire Van Wort. But then I’d hate him for being so weak. He’d given up even the shrieking and they rarely bothered to gag him anymore. (to Van Wort) Why don’t you fight back?.

VAN WORT: What’s the point?

NARRATOR: The point is you show them you’re not a *wussy.* Then they leave you alone.

VAN WORT: Will you help me?

NARRATOR: No. That would be wrong.

VAN WORT: Why?

NARRATOR: It’s complicated. ***************

NARRATOR: Then it was the last day of camp. We packed all our stuff in duffels. Tomorrow we would strip our beds and get into our family wagons, wave.

At our last lunch Steve-Ivan said that Van Wort and I would be voted camp love-birds at the camp banquet that night. (to Steve-Ivan) Vote us whatever you want.

We had to stack without even a Freeze-Please and Van Wort wouldn’t look at me. (to Van Wort) What’s wrong with you?

VAN WORT: I’m done with this.

NARRATOR: I took that to mean that he was going to do something, make himself the last of the brave. What he meant, though, was that he was truly done.

***************

NARRATOR: Van Wort took a canoe out to the middle of the lake. We were doing free swim and we heard him call to us, watched him drink from a big plastic jug and just sort of bend over, roll off the bow into the lake. You’d figure drowning would be hard going to begin with, but picture it with your guts burning off from a stolen jug of kitchen lye. Steve-Ivan dove in to save him but Van Wort was too fat. We watched them bob together in the middle of the lake. Then Steve-Ivan was bobbing up and down alone. He swam back weeping, or maybe it was the water.

They got Van Wort’s body out with a special boat. They had him in a strap swinging off the gunwale. His swim trunks trailed out from his feet and you could see all the night wounds on him.

MR. MARV: Self-mutilation. Interesting.

NARRATOR: The news trucks drove up that afternoon. Van Wort’s father appeared, too. He was a skinny man in a sun hat. He stood on the shoreline shouting at no one in particular. I walked up to him. (To VW’s Father) I was his friend.

FATHER: Were you his Judas, too? (slaps narrator across the face, then immediately regrets it) I didn’t mean that. I know you were his friend. Bobby wrote me about you.

NARRATOR: (long pause) I had long forgotten Van Wort was also a Bobby, if I ever knew. . . . I was his friend, [and] I was the one standing in the dining hall saying, “He brought it on himself.” . . . . his friend.
```

---

## IC-2363: Adventure Dog

- Title: Adventure Dog
- Author (byline): Dave Barry
- Work: Dave Barry’s Greatest Hits, Pg 208
- Publisher: Ballantine Books
- Publication date as stated: June 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ADVENTURE DOG, MASTER, DOOR, THEME SONG SINGER
- Teaser before the introduction: No
- Spoken words (computed): 626
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Barry
Book: Dave Barry’s Greatest Hits, Pg 208
ISBN: 978-0345419996
Publisher: Ballantine Books
Date (Month/Year): June 1997
```

### Introduction (context only: never use it for content warnings)

```text
(Sing) Adventure dog, Adventure doooooooggg,/ Kinda big, kinda strong, / Stupid as a log.

VOICE OVER: It’s a Bird . . . It’s a Plane . . . It’s ADVENTURE DOG! Able to shed on all types of furniture, finds even his own poo edible . . . Arch nemesis of the evil MAILMAN . . .

Reality Television really has gone too far! Adventure Dog by Dave Barry
```

### Performance text (classify this)

```text
(Pg 208+) I have this idea for a new television series. It would be a realistic action show, patterned after the true life experiences of my dog, Earnest. The name of the show would be "Adventure Dog." The theme song would go: (Sing) Adventure dog, Adventure doooooooggg / Kinda big, kinda strong / Stupid as a log.

Each episode would be about an exciting true adventure that happened to Earnest. For example, here's the script for an episode entitled: "Adventure Dog Wakes Up and Goes Outside": It is 6:17 a.m. Adventure Dog is sleeping in the hall. Suddenly she hears a sound. Her head snaps up. Somebody is up! Time to swing into action! Adventure Dog races down the hall and, skidding on all four paws, turns into the bathroom, where, to her total shock, she finds: The Master! Whom she has not seen since LAST NIGHT! YAYYYYYY!!

ADVENTURE DOG: Bark!

MASTER: DOWN, dammit! Now Adventure Dog bounds to the front door, in case the Master is going to take her outside. It is a slim chance. He has only taken her outside for the past 2,637 consecutive mornings. But just in case, Adventure Dog is ready.

ADVENTURE DOG: Bark! Can it be? Yes! This is unbelievable! The Master is coming to the door! Looks like Adventure Dog is going outside! YAAAYYY!

MASTER: DOWN, dammit! Now the Master has opened the door approximately one inch. Adventure Dog realizes that, at this rate, it may take the Master a full three-tenths of a second to open the door all the way. This is bad. He needs help. Adventure Dog alertly puts her nose in the crack and applies 600,000 pounds of force to the door.

MASTER: HEY!

DOOR: WHAM! And now Adventure Dog is through the door, looking left, looking right, her finely homed senses absorbing every detail of the environment, every nuance and subtlety, looking for . . . Holy Smoke! There it is! The YARD! Right in the exact same place it was yesterday! This is turning out to be an UNBELIEVABLE adventure!

ADVENTURE DOG: Bark! Adventure Dog is vaguely troubled. Some primitive version of a thought is rattling around inside her tiny cranium, like a BB in a tuna fish can. For she senses that there is some reason why the Master has let her outside. There is something he wants Adventure Dog to do. But what on Earth could it be? Before Adventure Dog can think of an answer, she detects . . . is this possible? Yes! It's a SMELL! Yikes! Full Red Alert!

ADVENTURE DOG: Sniff sniff sniff.

MASTER: Come on Earnest.

ADVENTURE DOG: Sniff sniff sniff sniff sniff sniff sniff sniff. No question about it. The evidence is clear. This is a smell, all right. And what's more, it's the smell of -- this is so incredible -- DOG WEEWEE! Right here in the yard!

MASTER: EARNEST!

ADVENTURE DOG: Sniff sniff sniff sniff sniff. Adventure Dog is getting the germ of an idea. At first is seems farfetched, but the more she thinks about it, the more she thinks, hey, why not! The idea is -- get ready -- Adventure Dog is going to MAKE WEEWEE! Right now! Outside! It's crazy, but it just might work!

MASTER: Good GIRL. What was that? It was a sound! Definitely. A sound coming from over there. Yes! No question about it. This is unbelievable! It's the MASTER out here in the yard! YAAAYY!

MASTER: DOWN, dammit!

THEME SONG SINGER: Adventure Dog, Adventure Dooooooggg . . .

ADVENTURE DOG: BARK!

MASTER: DOWN! Bear in mind that this is only one episode. There are many other possibilities: "Adventure Dog Gets Fed," "Adventure Dog Goes for a Ride in the Car and Sees Another Dog and Barks Real Loud for the Next 116 Miles," etc. It would be the kind of family-oriented show your kids could watch, because there would be extremely little sex, thanks to an earlier episode, "Adventure Dog Has an Operation."
```

---

## IC-2364: The Alumni Interview

- Title: The Alumni Interview
- Author (byline): David Levinthal
- Work: Sixteen: Stories about That Sweet and Bitter Birthday
- Publisher: Random House
- Publication date as stated: 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: IAN, THOM, MR. WRIGHT
- Teaser before the introduction: Yes
- Spoken words (computed): 1657
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Levinthal
Book: Sixteen: Stories about That Sweet and Bitter
Birthday
ISBN: 978-1400052707
Publisher: Random House
Date (Month/Year): 2004
```

### Introduction (context only: never use it for content warnings)

```text
It's difficult to deal with homophobic strangers, but it can be even more difficult dealing with relatives who reject homosexuality. These "loved ones" should love you no matter what and not judge you based on your sexual preferences. That's the way it should be . . . but not always.

Thom and Ian are in a loving relationship; and even though most of their friends know they are gay, Thom hasn’t found the strength to come out to his stoic, judgmental father. Can Ian keep their secret during a college interview with Thom’s father?

The Alumni Interview by David Levinthal
```

### Performance text (classify this)

```text
IAN: It is never easy to have a college interview with your closeted boyfriend's father. Would I have applied to this university if I had known that of all the alumni in the greater metropolitan area, it would choose Mr. Wright to find me worthy or unworthy? Maybe. But maybe not. Thom took it worse than I did. [He] couldn't believe I wanted to go to a place that had helped spawn the person his father had become.

IAN: Thom answered the door. We'd agreed on this beforehand. I didn't want to be in his house without seeing him. I wanted to know he was there.

It is a strange thing to meet your boyfriend's father when the father doesn't know you're his son's boyfriend-or even that his son has a boyfriend. It puts you at an advantage-you know more than he does-and also puts you at a disadvantage. The things you know aren't things you can let him know.

THOM: Dad, this is Ian.

MR. WRIGHT: Have a seat, Ian. Thank you, Thom.

IAN: I turned to Mr. Wright. I can do this, I thought. Then: And even if I can't, I have to. Mr. Wright had clearly done the alumni interview thing a hundred times before. As if reciting a message beamed in from central campus, he talked about how this interview was not supposed to be a formal one; it was all about getting to know me, and me getting to know the college where he had spent some of the best years of his life. He had a few questions to ask, and he was sure that I had many questions to ask as well.

In truth, I had already visited the campus twice and knew people who went there. I didn't have a single question to ask. Or, more accurately, the questions I wanted to ask didn't have anything to do with the university in question. • Thom says you've never in all his life hugged him. Why is that? • What can I do to make you see how wonderful he is? • Don't you know how wrong it is when you wave a twenty dollar bill in front of your son and tell him that when he gets a girlfriend, you'll be happy to pay for the first date? And then I'd add: My father isn't like you at all. So don't tell me it's normal parent behavior.

I am not by nature an angry person. But as this man kept saying he wanted to get to know me, I wanted to throw that phrase right back at him. How could he possibly get to know me when he didn't want to know his son?

MR. WRIGHT: Have you taken economics?

IAN: No.

MR. WRIGHT: (harrumphing) Why not?

IAN: I explained that our school offered only one economics class, and I had a conflict. A complete lie, but how would he know?

Judgmental. I considered the word judgmental. The mental state of always judging. His tone. I knew he wasn't singling me out. I knew this was probably the way he always was.

There were times I had gotten mad at Thom. Argument mad. Cutting-comment mad. Because his inability to be open made me a little closed. I didn't want to be a conditional boyfriend. I didn't want to be anybody's secret. As much as I said I understood, I never entirely understood.

Can't you just tell them? After they became the excuse for why we couldn't go out on Saturday. After they became the reason he pulled his hand away from mine as we were walking through town-what if they drove by? But then I'd feel bad, feel wrong. Because I knew this was not the way he wanted it to be. That even though we were sixteen, we were still that one leap away from independence. We were still caught on the dependence side, staring over the divide. Now, bearing the brunt of his father's disapproval, I understood. Not all of it. But a little more.

MR. WRIGHT: (expousing) ... too many of you students dillydally. You spend your time on such expendable things. Like Thom. You know Thom, right? No focus. He has no focus. He wouldn't be right for this university. You show more promise. But I have to say, you need to make sure you don't spend time on expendable things ... "

IAN: And suddenly I was sick of it. I looked to the door and saw something. A shadow in the keyhole. And I knew. Thom had never left. He was on the outside of the door, holding his breath for me. Trying to keep quiet. Stay quiet, because his father was around.

MR. WRIGHT: (condescendingly) What are your interests?

IAN: Your son in my room.

MR. WRIGHT: Excuse me?

IAN: The sun and the moon . . . Astronomy.

MR. WRIGHT: (pleased) I didn't know kids liked astronomy anymore. When I was a child, we all had telescopes. Now you just have telephones and televisions instead."

IAN: (nodding emphatically) You couldn't be more right, sir. A telescope is a fine instrument. And there's something about the stars ... (dramatic pause) Well, there's something about the stars that makes you realize both the smallness and the enormity of everything, isn't there?

MR. WRIGHT: Yes, yes, absolutely.

IAN: (to audience) Thom had first told me this as we lay on our backs on a golf course outside of town, too late for the twilight, but early enough to catch the rise of the moon, the pinprick arrival of the stars. His words were like a grasping. Now here was his father, agreeing with him, through me.

I looked to the keyhole, to Thom's shadow there. Knowing he was near. Speaking to him in this code. Saying to his father what I've said to him. (to Mr. Wright) Sometimes I wish we could open ourselves up to each other as much as we do to the sky. To the smallness and the enormity.

MR. WRIGHT: (looking at his notes) I see . . . (frowning) What is the GSA?

IAN: It had now gone from uncomfortable to downright fierce. I tried to imagine him coming to one of our Gay-Straight Alliance meetings. I tried to imagine that if I told him what it was, he would understand. I tried to think of a way to avoid his shiver of revulsion, his dismissive disdain.

Thom had tried to signal him once. I'd placed a pink triangle pin on his bag after a meeting, and he didn't take it off when he got home. Instead, he put the bag in a spot where it could be seen. But it didn't work. Mr. Wright brushed past it. He didn't notice or didn't say. When all Thom wanted was for him to notice without being told.

(to Mr. Wright as sincerely as possible) GSA stands for God Smiles Always, sir.

MR. WRIGHT: I didn't know the high school had one of those. How did it start?

IAN: (earnestly) Because of the school musical. A lot of the kids in the musical wanted to start it. It was Jesus Christ Superstar, sir. I think we were all moved by how much of a superstar Jesus was. It made us want to work to make God smile.

MR. WRIGHT: (irritated) And the school is okay with this?

IAN: Yes, sir. It's all about bringing people together.

MR. WRIGHT: (looking at Ian’s transcript) It says here you were on the dance committee for the GSA?

IAN: (nodding) I was one of the coordinators. We wanted to create a wholesome atmosphere for our fellow students. We only played Christian dance music. It's like Christian rock music, only the beat is a little faster. The lyrics are mostly the same."

MR. WRIGHT: Did Thom go to that dance?

IAN: Yes, sir. I believe I saw him there. (aside to audience) In fact, he was my date.

MR. WRIGHT: It also says you were involved in something called the Pride March?

IAN: Yes. We dress up as a pride of lions and we march. It's a school-spirit thing. Our mascot is a lion.

MR. WRIGHT: (not amused) Do you march in costume?

IAN: Yes. But we don't wear the heads of costumes. We're proud to be wearing them. We want people to know who we are.

MR. WRIGHT: (looking again at Ian’s paperwork) It says the Pride March is tied to Coming Out Day.

IAN: (to audience) Damn. The transcript might as well have been written in lavender ink. (to Mr. Wright with a fake laugh) Oh, that. It's another school-spirit thing. First day of the football season, someone dresses up as a lion and comes out from under the bleachers onto the field. If we see its shadow, we know the season will be a long one. If not, we know it's pretty much over before it's begun. The whole school gets really into it.

MR. WRIGHT: (slowly and deliberately) I know what's going on here. And I don't like it one bit.

IAN: I'm sorry, sir, but ...

MR. WRIGHT: (voice rapidly rising in agitation) I will not be ridiculed in my own house. That you should have the presumption to apply to my alma mater and then to sit there and mock me. I know what you are, and I will not stand for it here.

IAN: (to audience) I wish I could say that I hurled a response right back at him. But mostly, I was stunned. To have such a blast directed at me. To be yelled at. I couldn't move. I couldn't figure out what to say. Then the door opened and Thom said

THOM: (assertively) Stop it. Stop it right now! If you say one more word, I'm going to scream. I don't give a s***what you say to me, but you leave Ian out of it, okay? You're being a total a**hole, and that's not okay.

IAN: Mr. Wright started to yell. But it was empty yelling. Desperate yelling. And while he yelled, Thom came over to me and took my hand. I stood up and together we faced his father. And his father fell silent. And his father began to cry. As if the world had ended. I could feel Thom shaking, the tremors of that world exploding. As we stood there. As we watched. As we broke free from limbo.

I wanted to say, All you need to know about me is that I love your son. And if you get to know your son, you will know what that means. But the words were no longer mine to say.
```

---

## IC-2365: Am I Blue?

- Title: Am I Blue?
- Author (byline): Bruce Coville
- Work: Am I Blue? Coming Out from the Silence, Pg 1-18
- Publisher: Harper Trophy
- Publication date as stated: May 1995
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: VINCENT, BUTCH, MELVIN
- Teaser before the introduction: Yes
- Spoken words (computed): 1468
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bruce Coville
Book: Am I Blue? Coming Out from the Silence, Pg 1-18
ISBN: 978-0064405874
Publisher: Harper Trophy
Date (Month/Year): May 1995
```

### Introduction (context only: never use it for content warnings)

```text
Am I Blue? by Bruce Coville
```

### Performance text (classify this)

```text
VINCENT: (Pg 1-18) It started the day Butch Carrigan decided I was interested in *him.*

BUTCH: (snarling) You little fruit. I’ll teach you to look at me!

VINCENT: A moment or two later he had given me my lesson. I was still lying face down in the puddle into which Butch had slammed me as the culminating exercise of my learning experience when I heard a clear voice exclaim . . .

MELVIN: Oh, my dear! That was nasty. Are you all right, Vince?

VINCENT: (suspiciously) Who are you?

MELVIN: Your fairy godfather -- Melvin. Come on, stand up and let’s see if we can’t do something with you. (helping Vincent to his feet)

VINCENT: Are you making fun of me?

MELVIN: Moi? (arching his eyebrows and laying a hand on his chest) Listen, honey, I have nothing but sympathy for you. I had to deal with my share of troglodytes when I was your age, and I know it’s no fun. I’m here to help. You know, like in ‘Cinderella’? Do you want your three wishes or not, Vincent? (he stalks off)

VINCENT: (catching up, embarrassed) Do you have to walk like that?

MELVIN: Like what?

VINCENT: (blushing) You know . . . So swishy.

MELVIN: Honey, I gave my life to be able to walk like this. Don’t you dare try to stop me now. (proudly) I walk and talk the way I do because I’m not going to let anyone else define me.

VINCENT: (to audience) We went to a little cafe on Morton Street called Pete’s and found a table where we could talk in private. I kept trying to figure out what this was really about—-Candid Camera, an elaborate practical joke, that kind of thing. (To Melvin as he takes a sip of coffee; he’s shocked that it changed from plain coffee to Swiss double mocha; they both continue to sip during the conversation)

Okay, if you’re real, then tell me how come I never heard of fairy godfathers before.

MELVIN: Because I’m the first. It was pretty much expected that I would just opt to be an angel; tracking system, you know. But I said I didn’t want to be anyone’s guardian angel, I wanted to be a fairy godfather. (rolls his eyes) Let me tell you, that caused a hullabaloo! But I said people had been calling me a fairy all my life, and now that I was dead, that was what I wanted to be. You’re my first case.

VINCENT: (nervously) Does that mean I’m gay? (to audience) I didn’t mention that I had been trying to figure out the same thing myself for about a year now.

MELVIN: You may be, you may not. The point is, you’re getting picked on because people think you are—which is why I’ve been sent to work with you. Gay-bashing is a special issue for me. It’s how I met my maker, so to speak. I was walking down the street last year, minding my own business, when three bruisers dragged me into an alley, shouting, ‘We’ll teach you!’ They never did explain exactly what it was they were going to teach me. Last thing I remember was coming face to face with a tire iron. Next thing I knew, I was knocking at the Pearly Gates. (a silent moment, then Melvin shrugs)

VINCENT: (stunned) You’re taking this awfully casually.

MELVIN: Honey, I did a lot of screaming and shouting while it was happening. Afterwards too, for that matter. Didn’t do me a bit of good—I was still dead. Once you’ve been on the other side for a while, you get a little more zen about this kind of thing. Why don’t we just concentrate on your case for the time being?

VINCENT: Okay, do I really get three wishes?

MELVIN: Sure do. Well, two, now -- You used up the first one on that coffee.

VINCENT: I didn’t tell you to change it into Swiss double mocha!

MELVIN: You didn’t have to. You wished for it.

VINCENT: (muttering) I’m glad I didn’t wish I was dead!

MELVIN: Oh! Getting personal, are we? (glances around the room, then winks at a student)

VINCENT: (hissing) Will you stop that!

MELVIN: What’s the matter? (waves his hand) I guarantee you he wasn’t offended. He’s one of the gang.

VINCENT: What gang? (Melvin purses his lips and raises his eyebrows) How can you tell something like that just from looking at him?

MELVIN: Gaydar -- Automatic sensing systems that lets you spot people of similar persuasion. A lot of gay guys have it to some degree or other. If it was more reliable, it would life easier on us. If a guy asks a girl for a date, about the worst that can happen is that she laughs at him. If he asks another guy, he might get his face pounded in.

VINCENT: (sadly) It must be lonely.

MELVIN: (sharply) It doesn’t have to be. If gay people could just openly identify ourselves, there would be plenty of people you could ask for advice. Everybody knows gay people; they just think they don’t. Do you know the great gay fantasy? (Vincent shakes his head) Imagine what it would be like if every gay person in the country turned blue for a day. All the straights would have to stop imagining that they didn’t know any gay people. They’d have to face the fact that there are gay cops and gay farmers, gay teachers and gay soldiers, gay parents and gay kids. The hiding would finally have to stop. (beat) How would you like to have the sight? You might find it interesting.

VINCENT: (suspiciously) Does this count as a wish?

MELVIN: No, it’s education. Comes under a different category. Close your eyes. (Martin waves his hands with a flourish) Okay, open up and see what the world is really like.

VINCENT: (opens his eyes and gasps) (to audience) About a third of the people in the café were blue. Some were bright blue, some were deep blue, some just had bluish tint. (to Martin in a whisper) Are you telling all those people are gay?

MELVIN: To some degree or other.

VINCENT: But so many of them?

MELVIN: Well, this isn’t a typical place. The theater crowd hangs around in here. (waves his hand grandly) Groups like that tend to have a higher percentage of gay people, because we’re naturally artistic. (frowning) Of course, some bozos take a fact like that and decide that everyone doing theater is gay. Remember, two thirds of the people you’re seeing aren’t blue.

VINCENT: What about all the different shades?

MELVIN: It’s an indicator of degree. The lighter ones are less committed—or maybe like you, trying to make up their minds. Come on, let’s go for a walk.

VINCENT: (to audience) It was like seeing the world through new eyes. Most of the people looked just the same as always, of course. But Mr. Alwain, the guy who ran the grocery store, looked like a giant blueberry—which surprised me, because he was married and had three kids. On the other hand, Ms. Thorndyke, the librarian, who everyone knew was a lesbian, didn’t have a trace of blue on her.

MELVIN: Can’t tell without the spell. Straights are helpless at it. They’re always assuming someone is or isn’t for all the wrongs reasons.

VINCENT: (beat – to audience) All right, I suppose you’re wondering about me—as in, was I blue? The answer is, slightly. When I asked Melvin to explain, he said,

MELVIN: “The Magic Eight Ball says, ‘Signs Are Mixed.’” In other words, you are one confused puppy. That’s the way it is sometimes. You’ll figure it out after a while. (Melvin disappears)

VINCENT: (to audience) Watching the news that night was a riot. My favorite network anchor was the shade of a spring sky. So was the congressman he interviewed, who happened to be a notorious Republican homophobe. (beat) I couldn’t forget his hypocritical words: “the great crime of homosexuality” and “the gay threat to American youth.” I was brushing my teeth when I figured out what I wanted to do. . . it would probably mean another beating from Butch Carrigan. Yet if I did it, nothing would ever be the same. (whispering) Melvin?

MELVIN: At your service! Ooooh, what a tacky bathroom.

VINCENT: I want to make my second wish. . . . Gay fantasy coast to coast.

MELVIN: (a beat then he smiles) How’s midnight for a starting point?

VINCENT: Twenty-four hours should do the trick, don’t you think?

MELVIN: (rubs his hands, chuckles and disappears)

VINCENT: (to audience) I went to bed, but not to sleep. I kept thinking about what it would mean when the rest of the world could see what I could see today. I turned on the radio. It was about twelve thirty when, thanks to the wonders of modern communication, it had become obvious that people were turning blue from coast to coast. It didn’t take much longer for people to start figuring out what the blue stood for. The reaction ranged from panic to hysterical denial to dancing in the streets. National Public Radio quickly summoned a panel of experts to discuss what was going to happen when people had to go to work the next day . . . or school! Which was when I got my next idea. (shouting) Melvin!

MELVIN: You rang?

VINCENT: I just figured out my third wish. (taking a deep breath) I want you to turn Butch Carrigan blue.

MELVIN: (eyes wide) Vincent, I like the way you think. I’ll be back in a flash. (he disappears and pops back in grinning) You’ve still got one wish left, kiddo. (chuckling) Butch Carrigan was already blue as a summer sky when I got there. (he disappears)

VINCENT: (beat, then to audience) So . . . if I caused you any trouble with Blueday, I’m sorry. But not much. Because things are never going to be the same now that it happened. Never. And my third wish? I’ve decided to save it for when I really need it—maybe when I meet the girl of my dreams. Or Prince Charming. Whichever.
```

---

## IC-2366: Ambush

- Title: Ambush
- Author (byline): Tim O’Brien
- Work: The Things They Carried
- Publisher: Broadway
- Publication date as stated: Dec 1998
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 977
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tim O’Brien
Book: The Things They Carried
ISBN: 978-0767902892
Publisher: Broadway
Date (Month/Year): Dec 1998
```

### Introduction (context only: never use it for content warnings)

```text
A number of studies have focused on war zone psychology and understanding post-traumatic stress disorder. Even without the full-blown traits of PTSD, soldiers can suffer from what they call "moral injuries" – psychological wounds from having done something, or failed to stop something, that violates their moral code. You see, a moral injury tortures the conscience.

A war incident still haunts the narrator of this selection. Sometimes he can forgive himself, sometimes not.

Ambush by Tim O’Brien from The Things They Carried
```

### Performance text (classify this)

```text
When she was nine, my daughter Kathleen asked if I had ever killed anyone. She knew about the war; she knew I’d been a soldier. “You keep writing war stories,” she said, “so I guess you must’ve killed somebody.” It was a difficult moment, but I did what seemed right, which was to say, “Of course not,” and then to take her onto my lap and hold her for a while. Someday, I hope, she’ll ask again. But here I want to pretend she’s a grown-up. I want to tell her exactly what happened, or what I remember happening . . .

He was a short, slender young man of about twenty. I was afraid of him – afraid of something – and as he passed me on the trail I threw a grenade that exploded at his feet and killed him.

Or to go back: Shortly after midnight we moved into the ambush site outside My Khe. The whole platoon was there, spread out in the dense brush along the trail, and for five hours nothing at all happened. We were working in two-man teams – one man on guard while the other slept, switching off every two hours – and I remember it was still dark when Kiowa shook me awake for the final watch.

The night was foggy and hot. For the first few moments I felt lost, not sure about directions, groping for my helmet and weapon. I reached out and found three grenades and lined them up in front of me; the pins had already been straightened for quick throwing. And then for maybe half an hour I kneeled there and waited. Very gradually, in tiny slivers, dawn began to break through the fog; and from my position in the brush I could see ten or fifteen meters up the trail. The mosquitoes were fierce. I remember slapping them, wondering if I should wake up Kiowa and ask for some repellent, then thinking it was a bad idea, then looking up and seeing the young man come out of the fog.

He wore black clothing and rubber sandals and a gray ammunition belt. His shoulders were slightly stooped, his head cocked to the side as if listening for something. He seemed at ease. He carried his weapon in one hand, muzzle down, moving without any hurry up the center of the trail. There was no sound at all – none that I can remember. In a way, it seemed, he was part of the morning fog, or my own imagination, but there was also the reality of what was happening in my stomach.

I had already pulled the pin on a grenade. I had come up to a crouch. It was entirely automatic. I did not hate the young man; I did not see him as the enemy; I did not ponder issues of morality or politics or military duty. I crouched and kept my head low. I tried to swallow whatever was rising from my stomach, which tasted like lemonade, something fruity and sour. I was terrified.

here were no thoughts about killing. The grenade was to make him go away – just evaporate – and I leaned back and felt my mind go empty and then felt it fill up again. I had already thrown the grenade before telling myself to throw it. The brush was thick and I had to lob it high, not aiming, and I remember the grenade seeming to freeze above me for an instant, as if a camera had clicked, and I remember ducking down and holding my breath and seeing little wisps of fog rise from the earth. The grenade bounced once and rolled across the trail. I did not hear it, but there must’ve been a sound, because the young man dropped his weapon and began to run, just two or three quick steps, then he hesitated, swiveling to his right, and he glanced down at the grenade and tried to cover his head but never did. It occurred to me then that he was about to die. I wanted to warn him.

The grenade made a popping noise – not soft but not loud either – not what I’d expected – and there was a puff of dust and smoke – a small white puff – and the young man seemed to jerk upward as if pulled by invisible wires. He fell on his back. His rubber sandals had been blown off. There was no wind. He lay at the center of the trail, his right leg bent beneath him, his one eye shut, his other eye a huge star-shaped hole.

It was not a matter of live or die. There was no real peril. Almost certainly the young man would have passed by. And it will always be that way.

Later, I remember, Kiowa tried to tell me that the man would’ve died anyway. He told me that it was a good kill, that I was a soldier, and this was a war, that I should shape up and stop staring and ask myself what the dead man would’ve done if things were reversed.

None of it mattered. The words seemed far too complicated. All I could do was gape at the fact of the young man’s body.

Even now I haven’t finished sorting it out. Sometimes I forgive myself, other times I don’t. In the ordinary hours of life I try not to dwell on it, but now and then, when I’m reading a newspaper or just sitting alone in a room, I’ll look up and see the young man coming out of the morning fog. I’ll watch him walk toward me, his shoulders slightly stooped, his head cocked to the side, and he’ll pass within a few yards of me and suddenly smile at some secret thought and then continue up the trail to where it bends back into the fog.
```

---

## IC-2367: Angela’s Ashes

- Title: Angela’s Ashes
- Author (byline): Frank McCourt
- Work: Not specified
- Publisher: Scribner
- Publication date as stated: May 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: FRANK, PRIEST, GRANDMOTHER, GRANDMA, GRANDMOTER, MOTHER, MIKEY
- Teaser before the introduction: Yes
- Spoken words (computed): 1366
- Already set (do not supply): none

### Source block (context only)

```text
Author: Frank McCourt
ISBN: 978-0684842677
Publisher: Scribner
Date (Month/Year): May 1999
```

### Introduction (context only: never use it for content warnings)

```text
Crossed-eyed Mikey Molloy is eleven years old. He knows about the female body and “Dirty Things in General.” Mikey tells Frank a story of Irish mythology about the great Cuchulain’s wife, Emer, who was the “champion woman pisser of Ireland.” Uh – oh – And thus begins the story of Frank McCourt’s first confession and communion.

Angela’s Ashes by Frank McCourt.
```

### Performance text (classify this)

```text
FRANK: It’s my turn. The confession box is dark and there’s a big crucifix hanging over my head. I can hear a boy mumbling his confession on the other side. I wonder if there’s any use trying to talk to the Angel on the Seventh Step. I know he’s not supposed to be hanging around confession boxes but I feel the light in my head and the voice is telling me, Fear not. The panel slides back before my face . . . (to Priest) Bless me, Father, for I have sinned. This is my First Confession.

PRIEST: Yes, my child, and what sins have you committed?

FRANK: I told a lie. I hit my brother. I took a penny from my mother’s purse. I said a curse. . . I, I listened to a story about Cuchulain and Emer.

PRIEST: Surely that’s not a sin, my child. After all we are assured by certain writers that Cuchulain turned Catholic in his last moments.

FRANK: ‘Tis about Emer, Father, and how she married him.

(whispering) She won him in a pissing contest. (to audience) There is heavy breathing. The priest has his hand over his mouth and he’s making choking sounds and talking to himself, Mother o’ God.

PRIEST: (trying to control is laughter) Who, who told you that story, my child?

FRANK: Mikey Molloy. He read it in a book, Father.

PRIEST: For your penance say three Hail Mary’s, and three Our Fathers.

FRANK: Father, was that the worst sin? Am I the worst of all the boys, Father?

PRIEST: No, you have a long way to go. God bless you, my child.

FRANK: First Communion Day is the happiest day of your life because of The Collection and James Cagney at the Lyric Cinema. The night before I was so excited, I couldn’t sleep till dawn. I’d still be sleeping if my grandmother hadn’t come banging at the door.

GRANDMOTHER: (knocking at the door) Get up! Get up! Get that child outa the bed! Happiest day of his life an’ him snorin’.

FRANK: I ran to the kitchen. I took off [my] shirt and she pushed me into a tin tub of icy cold water. They dressed me in my black velvet First Communion suit with the white frilly shirt, the short pants, the white stockings, the black patent leather shoes.

GRANDMOTHER: Come here till I comb your hair. Look at that mop, it won’t lie down. (she spits on his head to control the hair) You didn’t get that hair from my side of the family. That’s that North of Ireland hair you got from your father. That’s the kind of hair you see on Presbyterians. If your mother had married a proper decent Limerickman you wouldn’t have this standing up, North of Ireland, Presbyterian hair. (she spits on his head again)

FRANK: Grandma, will you please stop spitting on my head.

GRANDMA: If you have something to say, shut up. A little spit won’t kill you. Come on, we’ll be late for the Mass.

FRANK: We ran to the church. My mother panted along behind with Michael in her arms. We arrived at the church just in time to see the last of the boys leaving the altar rail where the priest stood with the chalice and the host. (Priest assumes glaring stance) (Frank opens his mouth to receive communion and speaks with his mouth full) Then he placed on my tongue the wafer, the body and blood of Jesus. At last, at last!

(look of surprise as the wafter sticks) It stuck! I had God glued to the roof of my mouth! I could hear the master’s voice:

PRIEST: Don’t let the host touch your teeth for if you bite God in two you’ll roast in hell for eternity.

FRANK: I tried to get God down with my tongue (tries to dislodge the wafer)

PRIEST: (hissing) Stop that clucking and get back to your seat.

FRANK: God was good. He melted and I swallowed Him and now, at last, I was a member of the True Church, an official sinner.

When the Mass ended, there they were at the door of the church, my mother and my grandmother. They each hugged me and told me it was the happiest day of my life. They cried all over my head and after my grandmother’s contribution that morning my head was a swamp. (to Mom) Mam, can I go now and make The Collection?

GRANDMOTER: No. You’re not making no collection till you’ve had a proper First Communion breakfast at my house. Come on.

FRANK: We followed her. She banged pots and rattled pans and complained that the whole world expected her to be at their beck and call. I ate the egg, I ate the sausage, and when I reached for more sugar for my tea . . .

GRANDMOTHER: (slapping his hand) Go aisy with that sugar. Is it a millionaire you think I am? An American?

Is it bedecked in glitterin’ jewelry you think I am? Smothered in fancy furs?

FRANK: The food churned in my stomach. I gagged. I ran to her backyard and (he throws up). Out she came.

GRANDMOTHER: Look at what he did. Thrun up his First Communion breakfast. Thrun up the body and blood of Jesus. I have God in me backyard. What am I goin’ to do? (thinking) I’ll take him to the Jesuits!

FRANK: She dragged me through the streets of Limerick. She told the neighbors and passing strangers about God in her backyard. She pushed me into the confession box. (to the Priest) In the name of the Father, the Son, the Holy Ghost. Bless me, Father, for I have sinned. It’s a day since my last confession.

PRIEST: A day? And what sins have you committed in a day, my child?

FRANK: I overslept. I nearly missed my First Communion. My grandmother said I have standing up, North of Ireland, Presbyterian hair. I threw up my First Communion breakfast. Now Grandma says she has God in her backyard and what should she do?

PRIEST: (struggling to control his laughter) Ah … ah … tell your grandmother to wash God away with a little water and for your penance say one Hail Mary and one Our Father. God bless you, my child.

FRANK: Grandma and Mam were waiting close to the confession box.

GRANDMOTHER: Were you telling jokes to that priest in the confession box? (gives him a slap on the back of the head) If ’tis a thing I ever find out you were telling jokes to Jesuits I’ll tear the bloody kidneys outa you. Now what did he say about God in me backyard?

FRANK: He said wash Him away with a little water, Grandma.

GRANDMOTHER: (thinking) Holy water or ordinary water?

FRANK: He didn’t say, Grandma.

GRANDMOTHER: Well, go back and ask him. (pushing him back into the confessional)

FRANK: Bless me, Father, for I have sinned, it’s a minute since my last confession.

PRIEST: A minute! What is it now?

FRANK: (embarrassed) My grandma says, Holy water or ordinary water?

PRIEST: Ordinary water, and tell your grandmother not to be bothering me again.

FRANK: (exiting the confessional) Ordinary water, Grandma, and he said don’t be bothering him again.

GRANDMOTHER: Don’t be bothering him again! That bloody ignorant bogtrotter!

FRANK: Can I go now and make The Collection? I want to see James Cagney.

GRANDMOTHER: You can forget about The Collection and James Cagney because you’re not a proper Catholic the way you left God on the ground. Come on, go home.

MOTHER: Wait a minute. That’s my son. That’s my son on his First Communion Day. He’s going to see James Cagney.

GRANDMOTHER: (throwing her hands up) Take him then to James Cagney and see if that will save his Presbyterian North of Ireland American soul. Go ahead. (she exits in disgust)

FRANK: We met Mikey Molloy on Barrington Street. He asked if I was going to the Lyric and I said I was trying.

MIKEY: Trying? You don’t have money? That’s all right. I’ll get you in. I’ll create a diversion.

FRANK: What’s a diversion?

MIKEY: I have the money to go and when I get in, I’ll pretend to have the fit and the ticket man will be out of his mind and you can slip in when I let out the big scream. (demonstrates the scream) I’ll be watching the door and when I see you in, I’ll have a miraculous recovery. That’s a diversion. That’s what I do to get my brothers in all the time.

MOTHER: Oh, I don’t know about that, Mikey. Wouldn’t that be a sin and surely you wouldn’t want Frank to commit a sin on his First Communion Day.

FRANK: Mikey said if there was a sin it would be on his soul, and he wasn’t a proper Catholic anyway so it didn’t matter. He let out his scream and I slipped in. The ticket man was so worried over Mikey he never noticed! (triumphant grin that turns to horror as he realizes he has sinned again. He arrives at church the next day and enters the confessional)

(to the Priest) In the name of the Father, the Son, the Holy Ghost. Bless me, Father, for I have sinned. It’s a day since my last confession.
```

---

## IC-2368: Animals

- Title: Animals
- Author (byline): Simon Rich
- Work: Spoiled Brats, Pg 1-18
- Publisher: Little, Brown and Company
- Publication date as stated: Oct 2014
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: PRINCESS JASMINE, HAILEY, MS. HUDSON, SIMON, ALYSSA, PRINCIPAL DAVENPORT, SIMON’S MOTHER, CARLOS, GIRL 1, GIRL 2, GIRL 3
- Teaser before the introduction: Yes
- Spoken words (computed): 1427
- Already set (do not supply): none

### Source block (context only)

```text
Author: Simon Rich
Book: Spoiled Brats, Pg 1-18
ISBN: 978-0316368629
Publisher: Little, Brown and Company
Date (Month/Year): Oct 2014
```

### Introduction (context only: never use it for content warnings)

```text
By the time Simon Rich graduated from Harvard he had a two-book deal from Random House. He also spent four years writing for Saturday Night Live (the youngest writer SNL ever hired) and about two years at Pixar and is now at work on a film and a television series. His stories are eccentric, universally hilarious and often built on an unusual premise, or told from a surprising angle. This tale takes a looks at a typical week in a 2nd grade classroom of a elite private school . . . but the twist? Our narrator is a widowed hamster named . . . (wait for it) PRINCESS JASMINE!

Animals by Simon Rich
```

### Performance text (classify this)

```text
PRINCESS JASMINE: (Pg 1-18) They buried my wife in a shoebox in Central Park. I like to imagine that the service was respectful, that her body was treated with a modicum of dignity. But of course, I’ll never know. I wasn’t invited to her funeral. Instead, the guests of honor were the students of homeroom 2K . . . Her killers.

Hailey, I noticed, was crying. The irony. It was her responsibility to refill our water bottle last week. Instead, she spent all her free time with Alyssa, practicing a clapping game called “Miss Mary Mack.”

HAILEY: (with enthusiasm) Miss Mary Mack, Mack, Mack! All dressed in black, black, black!

PRINCESS JASMINE: It was that inane chant that provided the score to my wife’s final moments. . . Pocahontas was her name.

PRINCESS JASMINE: My name is Princess Jasmine. I am a male, so this name is humiliating, but I’m aware that my situation could be worse. The other homeroom, 2R, has a guinea pig named Homer Simpson and an elderly turtle named New Kids on the Block.

Pocahontas left me with three sons, and it’s for their sake alone that I keep up my struggle. Their names are Big Mac, Whopper, and Mr. T.

It’s morning now. The square of sunlight on the blackboard grows and grows. Soon the gremlins will run in howling, hopped up on Pop-Tarts and primed for violence. It turns out this school is a private one, an “elite” institution for the children of millionaires. I can hear the nannies muscling their way through the lobby, dragging their little terrors toward my family. The bell clangs harshly. The nightmare has begun.

Monday

MS. HUDSON: What time is it?

SIMON: Jobs time!

PRINCESS JASMINE: My fur bristles as Ms. Hudson takes out the Jobs Board. This laminated poster, with its seventeen colorful squares, rules my family’s existence. It determines everything: whether we feast or starve, live or die. I rub my paws impatiently while Ms. Hudson assigns the week’s tasks. . . Pencil organizer . . . . Table Wipers . . . Eventually, she gets to the one job that matters.

MS. HUDSON: Hamster feeder is…

PRINCESS JASMINE: I scan the room. There are still some good candidates left. Maybe we’ll get lucky and end up with Caitlin? Last time she gave us double portions. It’s while I’m enjoying this fantasy that Ms. Hudson clears her throat and—with one little word—sentences my family to death.

MS. HUDSON: …Simon.

PRINCESS JASMINE: My eyes widen with horror.

SIMON: (shouting) Hamster feeder? Whatchu talkin’ ’bout Willis!

PRINCESS JASMINE: The other children laugh hysterically. My God, I think. This is it. This is how it ends.

PRINCESS JASMINE: 11:25 am . . . I sigh with relief as Simon finally walks over to our cage. He doesn’t feed us, though, or replenish our water. Instead, he picks me up by my tail, which is connected directly to my spine. He swings me through the air drops me back into my cage. My sons poke their heads through the newspaper. They look around confusedly, then stare at me in dismay. They’re used to receiving food at this hour, but I have none to give. Simon has forgotten to do his one basic task. Our long, slow death march has started.

Tuesday

PRINCESS JASMINE: I awake to the sound of screeching laughter. Sophie and Alyssa have made a dress out of pink construction paper and taped it to my sleeping body.

ALYSSA: You’re a pretty girl, Princess Jasmine! A pretty, pretty girl!

PRINCESS JASMINE: I try to remove the costume, but the tape is double-sided and my paws are too weak to detach it. I must wear this “dress” indefinitely, in the presence of my own sons. I avoid their eyes, and they avoid mine. Whatever dignity I had is long gone. I can feel myself on the verge of becoming insane.

When the final school bell rings. Carlos, the janitor walks from table to table, cleaning up after the beasts. The Jobs Board is a total farce, I think, as he sponges up their filth. Kristen and Sophie are table wipers in name only. At the end of the day, every job on the board belongs to Carlos. When Carlos sees us, he curses under his breath. I avert my eyes with shame. Our cage is full of feces. I know we’re not responsible for the condition of our prison, but it’s hard not to feel mortified. I look on with pity as the janitor collects our soiled newspaper. He refills our water bottle, and, for the first time in days, I allow myself to feel hope. Before he can find our feedbag, though, Principal Davenport has run into the room.

PRINCIPAL DAVENPORT: Carlos, there you are! A kindergartener [soiled] himself in dance. Would you please take care of it?

PRINCESS JASMINE: Carlos forces another smile and reaches for his mop. Wednesday

PRINCESS JASMINE: The water tastes so rich it brings tears to my eyes. As I drink it, I can feel it coursing through my body, giving my parched veins life. I look over at my sons, asleep in their clean cage, their wet little noses twitching with contentment. Carlos has saved our lives. But for how long?

Mercifully, the children are gone this morning. They’ve been given a break from their arduous studies to enjoy a “field day” at Randall’s Island. The classroom is blissfully quiet until lunchtime, when the hobgoblins return. Their red faces are streaked with grime and sweat. The smell is almost unendurable. Every child has somehow won an athletic trophy.

SIMON: (Raising his golden prize over his head, he shouts) Boom shaka laka!

PRINCESS JASMINE: When he walks by my cage, I peak at the engraving on his trophy. “Participation,” it reads. I wonder if Simon is aware that his trophy has no meaning, that all he participated in was a mass delusion?

MS. HUDSON: Great job, everybody. That was some great teamwork today. Don’t forget to do your jobs!

PRINCESS JASMINE: Simon doesn’t even look in our direction. This makes three straight days without food. It’s official: we are going to starve to death. Thursday

PRINCESS JASMINE: As the sun rises on another hellish day, I gather my sons around me. I’ve rehearsed my speech all night, but it’s still hard to utter it. Eventually, with painful effort, I manage to force the terrible words through my lips. “If Simon forgets to feed us one more time… I want the three of you to eat my body.” Mr. T breaks down and weeps. But Big Mac and Whopper merely nod. They know it’s the only solution we have left.

I can hear Simon’s voice before he even enters the classroom, as piercing and abrasive as a siren.

SIMON: Whatchu talkin’ ’bout Willis! (As he presses his face against the bars of the hamster cage, he chants again and again) Whatchu talkin’ ’bout! Whatchu talkin’ ’bout! Whatchu talkin’ ’bout!

PRINCESS JASMINE: His noxious Dorito breath engulfs me and I can feel the fury mounting in my chest. I think of the sound of my son weeping and the look my wife gave me as she drew her final breath. I have only a little strength left. But it’s enough to rise up and sink my teeth into the monster’s flesh. Friday

PRINCESS JASMINE: Our cage has been moved to the principal’s office,

PRINCIPAL DAVENPORT: Words can’t express how sorry I am! Safety is our top priority—I’m as appalled as you are that something like this could occur at our school.

SIMON’S MOTHER: He had to get three stitches! The plastic surgeons say that the scar could be visible for months!

PRINCESS JASMINE: I roll my eyes as Simon’s mother starts to cry.

SIMON’S MOTHER: He’s just a little boy. And you let him be exposed to wild animals! I’m considering pressing charges. My lawyer says I have a real case. Simon had to take a rabies test, and when the nurse pricked his thumb, he cried and cried. The doctor said he’d never seen a boy cry like that.

PRINCESS JASMINE: I smile proudly, thinking of this scene. [Then] Simon’s mother turns toward our cage, her eyes narrowing with rage.

SIMON’S MOTHER: I want those animals out of the classroom . . . I want them destroyed.

PRINCIPAL DAVENPORT: (clearing his throat) Of course.

(He picks up a phone and calls for a janitor)

PRINCESS JASMINE: Carlos arrives within seconds, mop in hand . . . . I can smell the Dumpster before I see it, an overflowing bin of putrid trash. My nose twitches painfully as I process all the stenches: decomposing Dunkaroos and mold-encrusted Pop-Tarts; rancid, soggy Lunchables and spoiled Nesquik. The monsters have accumulated so much waste this week, and now we’re to be added to the pile.

CARLOS: (whispering) Sorry, little guys. (He scans the alley to make sure no children are watching, then tucks the cage under his arm and runs) Saturday

PRINCESS JASMINE: I awake to the sight of three girl humans, gobbling pancakes and chatting rapidly.

GIRL 1: What do we name the babies?

GIRL 2: Snap, Crackle, and Pop!

GIRL 3: The mommy should be Mrs. Fluffy, or Mrs. Furry, or…

CARLOS: (interrupting) It’s not a mommy. It’s a daddy. And we’re going to call him Hercules.

GIRL 1: (laughing) Hercules! Why?

CARLOS: (Crouching down and looking into Hercules’ eyes) Because he’s tough. And strong. And he works long hours, even though it’s a living nightmare. (There is a sense he is talking about himself too)

GIRL 2: (looking around nervously, she whispers) O.K. We’ll call him Hercules.
```

---

## IC-2369: Araby

- Title: Araby
- Author (byline): James Joyce
- Work: Dubliners
- Publisher: Wordsworth Editions
- Publication date as stated: 1993
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1596
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Joyce
Book: Dubliners
ISBN: 978-1853260483
Publisher: Wordsworth Editions
Date (Month/Year): 1993
```

### Introduction (context only: never use it for content warnings)

```text
Come with me to Araby . . . the Islamic lands of North Africa, the Near East, and the Middle East . . . Symbols of decadence, exotic delights, escapism, and a luxurious sensuality. Let’s face it the lure of escape beckons to all of us from time to time. For the protagonist of James Joyce’s Araby, however, the reality of Araby is a rather tawdry shadow of his dreams. Anticipation of the unknown faces the stark reality of existence in

Araby by James Joyce.
```

### Performance text (classify this)

```text
North Richmond Street, being blind, was a quiet street except at the hour when the Christian Brothers' School set the boys free. An uninhabited house of two storeys stood at the blind end, detached from its neighbours in a square ground. The other houses of the street, conscious of decent lives within them, gazed at one another with brown imperturbable faces.

The former tenant of our house, a priest, had died in the back drawing-room. Air, musty from having been long enclosed, hung in all the rooms, and the waste room behind the kitchen was littered with old useless papers. The wild garden behind the house contained a central apple-tree and a few straggling bushes, under one of which I found the late tenant's rusty bicycle-pump.

When the short days of winter came, dusk fell before we had well eaten our dinners. When we met in the street the houses had grown sombre. The space of sky above us was the colour of ever-changing violet and towards it the lamps of the street lifted their feeble lanterns. The cold air stung us and we played till our bodies glowed. Our shouts echoed in the silent street. The career of our play brought us through the dark muddy lanes behind the houses, where we ran the gauntlet of the rough tribes from the cottages, to the back doors of the dark dripping gardens where odours arose from the ashpits, to the dark odorous stables where a coachman smoothed and combed the horse or shook music from the buckled harness. When we returned to the street, light from the kitchen windows had filled the areas. If my uncle was seen turning the corner, we hid in the shadow until we had seen him safely housed. Or if Mangan's sister came out on the doorstep to call her brother in to his tea, we watched her from our shadow peer up and down the street. We waited to see whether she would remain or go in and, if she remained, we left our shadow and walked up to Mangan's steps resignedly. She was waiting for us, her figure defined by the light from the half-opened door. Her dress swung as she moved her body, and the soft rope of her hair tossed from side to side.

Every morning I lay on the floor in the front parlour watching her door. When she came out on the doorstep my heart leaped. I ran to the hall, seized my books and followed her. I kept her brown figure always in my eye and, when we came near the point at which our ways diverged, I quickened my pace and passed her. This happened morning after morning. I had never spoken to her, except for a few casual words, and yet her name was like a summons to all my foolish blood.

I imagined that I bore my chalice safely through a throng of foes. Her name sprang to my lips at moments in strange prayers and praises which I myself did not understand. My eyes were often full of tears (I could not tell why) and at times a flood from my heart seemed to pour itself out into my bosom. I thought little of the future. I did not know whether I would ever speak to her or not or, if I spoke to her, how I could tell her of my confused adoration. But my body was like a harp and her words and gestures were like fingers running upon the wires.

At last she spoke to me. When she addressed the first words to me, I was so confused that I did not know what to answer. She asked me was I going to Araby. I forgot whether I answered yes or no. It would be a splendid bazaar; she said she would love to go.

`And why can't you?' I asked.

While she spoke she turned a silver bracelet round and round her wrist. She could not go, she said, because there would be a retreat that week in her convent. Her brother and two other boys were fighting for their caps, and I was alone at the railings. She held one of the spikes, bowing her head towards me. The light from the lamp opposite our door caught the white curve of her neck, lit up her hair that rested there and, falling, lit up the hand upon the railing. It fell over one side of her dress and caught the white border of a petticoat, just visible as she stood at ease.

`If I go,' I said, `I will bring you something.'

What innumerable follies laid waste my waking and sleeping thoughts after that evening! I wished to annihilate the tedious intervening days. I chafed against the work of school. At night in my bedroom and by day in the classroom her image came between me and the page I strove to read. The syllables of the word Araby were called to me through the silence in which my soul luxuriated and cast an Eastern enchantment over me. I asked for leave to go to the bazaar on Saturday night.

On Saturday morning I reminded my uncle that I wished to go to the bazaar in the evening. He was fussing at the hallstand, looking for the hat-brush, and answered me curtly: `Yes, boy, I know.'

When I came home to dinner my uncle had not yet been home. Still it was early. I sat staring at the clock for some time and, when its ticking began to irritate me, I left the room. I mounted the staircase and gained the upper part of the house. The high, cold, empty, gloomy rooms liberated me and I went from room to room singing. From the front window I saw my companions playing below in the street. Their cries reached me weakened and indistinct and, leaning my forehead against the cool glass, I looked over at the dark house where she lived. I may have stood there for an hour, seeing nothing but the brown-clad figure cast by my imagination, touched discreetly by the lamplight at the curved neck, at the hand upon the railings and at the border below the dress.

When she had gone I began to walk up and down the room, clenching my fists. My aunt said: “I'm afraid you may put off your bazaar for this night of Our Lord.”

At nine o'clock I heard my uncle's latchkey in the hall door. I heard him talking to himself and heard the hallstand rocking when it had received the weight of his overcoat. I could interpret these signs. When he was midway through his dinner I asked him to give me the money to go to the bazaar. He had forgotten.

`The people are in bed and after their first sleep now,' he said.

I did not smile. My aunt said to him energetically: “Can't you give him the money and let him go? You've kept him late enough as it is.”

I held a florin tightly in my hand as I strode down Buckingham Street towards the station. The sight of the streets thronged with buyers and glaring with gas recalled to me the purpose of my journey. I took my seat in a third-class carriage of a deserted train. After an intolerable delay the train moved out of the station slowly. It crept onward among ruinous houses and over the twinkling river. At Westland Row Station a crowd of people pressed to the carriage doors; but the porters moved them back, saying that it was a special train for the bazaar. I remained alone in the bare carriage. In a few minutes the train drew up beside an improvised wooden platform. I passed out on to the road and saw by the lighted dial of a clock that it was ten minutes to ten. In front of me was a large building which displayed the magical name.

I could not find any sixpenny entrance and, fearing that the bazaar would be closed, I passed in quickly through a turnstile, handing a shilling to a weary-looking man. I found myself in a big hall girded at half its height by a gallery. Nearly all the stalls were closed, and the greater part of the hall was in darkness. I recognized a silence like that which pervades a church after a service. I walked into the centre of the bazaar timidly.

Remembering with difficulty why I had come, I went over to one of the stalls and examined porcelain vases and flowered tea-sets. At the door of the stall a young lady was talking and laughing with two young gentlemen. I remarked their English accents and listened vaguely to their conversation.

Observing me, the young lady came over and asked me did I wish to buy anything. The tone of her voice was not encouraging; she seemed to have spoken to me out of a sense of duty. I looked humbly at the great jars that stood like eastern guards at either side of the dark entrance to the stall and murmured: `No, thank you.'

I allowed the two pennies to fall against the sixpence in my pocket. I heard a voice call from one end of the gallery that the light was out. The upper part of the hall was now completely dark.

Gazing up into the darkness I saw myself as a creature driven and derided by vanity; and my eyes burned with anguish and anger.
```

---

## IC-2370: Army Issue Elf

- Title: Army Issue Elf
- Author (byline): Paul Feig
- Work: Kick Me: Adventures in Adolescence, Pgs 9+
- Publisher: Three Rivers Press
- Publication date as stated: Sept 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: PAUL, MOM, FATHER, NARRATOR, BRIAN, MIKE, MISS CONNER, MICHELLE
- Teaser before the introduction: Yes
- Spoken words (computed): 1611
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul Feig
Book: Kick Me: Adventures in Adolescence, Pgs 9+
ISBN: 978-0609809433
Publisher: Three Rivers Press
Date (Month/Year): Sept 2002
```

### Introduction (context only: never use it for content warnings)

```text
Dear Mr. and Mrs. Feig: The 1st grade classes will be performing in a Christmas play on Thursday, December 19th at 3:00 pm. Please mark this date in your calendars. Your child has an important part in the program, so please make sure he has his elf costume ready and with him for the production. Thank you . . . Miss Conner.

And so the saga of the Army Issue Elf by Paul Feig begins.
```

### Performance text (classify this)

```text
PAUL: (Pg 9 +) I was selected to play the lead elf in my school's Christmas pageant when I was in the first grade. The only reason I got the part was because my voice was louder and better suited to be heard in a cavernous gymnasium than any other kid in my class. I don't really remember the specifics of my recruitment into the world of theater. I just remember that one day I came home and told my mother I needed an elf costume.

MOM: An elf costume? Hmmm . . .

PAUL: She and I had seen plenty of TV shows and commercials with elves in them. We'd watched the perennially creepy Rudolph the Red-Nosed Reindeer on TV together at Christmas time enough for her to know what one of Santa's miniature helpers wore. When my father came home that night, my mother informed him of my wardrobe needs.

FATHER: (annoyed) An elf? How are we supposed to do that?

NARRATOR: [Now], my father owned an army surplus store called Ark Surplus. If a kid's father could own any kind of business, an army-surplus store is about as good as it gets, falling short only of a toy company or a roller-coaster factory. As a first grader who was simply trying to get an elf costume for the Christmas pageant, I knew exactly where that costume was going to be pieced together.

FATHER: (sighing)"All right. I'll take him down to the store this weekend and we'll figure something out.

PAUL: A few days later, we went into Ark Surplus and started scouring the aisles for anything that was vaguely elflike.

FATHER: What kind of pants do elves wear? (poking through a shelf)

MOM: I think they wear shorts.

PAUL: Yeah! They wear shorts with suspenders. (to audience) I don't know why my parents didn't try to find a book that had a picture of an elf in it that they could have used for reference. But my parents felt they could pull an elf costume out of all this former soldier gear. And I had no choice but to trust them. We came home that afternoon with a bag full of army issued goods. The search for elf shorts resulted in my father's grabbing a pair of olive drab (or "O.D.") green U.S. government boxer shorts and two black nylon straps. These straps were usually used to lash down an ammunition box but were now going to serve as my merry suspenders. The question of footwear had stumped all three of us, and so a long pair of O.D. green socks and a lengthy piece of foam rubber had been harvested in the hopes of approximating an elf shoe.

FATHER: (with determination) Okay, let's get to work.

PAUL: He and my mother went about constructing my elf outfit. I put on a white button-up shirt from my closet and stepped into the army boxers, which my mother then hoisted up, practically lifting me off the ground and giving me an army-issue wedgie. My father took the black nylon straps and taped the ends inside the front and back of the boxers, creating a suspender-like effect.

FATHER: What the hell do elves' feet look like anyway?

PAUL: They have shoes that curl up.

MOM: (as if that were absurd) I think it's their feet that curl up.

PAUL: My father thought for a second, then grabbed a knife and went to work on the piece of foam rubber. He cut two large banana-shaped curls that were almost a foot long and then stuffed one inside the toe of each sock. I pulled the socks on and stood up. My feet now looked like two dark green pontoons. Instead of curling upward, they gently rose at about a fifteen-degree angle. In addition, my feet were now each about twenty-four inches long.

FATHER: (nodding his approval) Those look like elf feet to me!

PAUL: My mother pulled the watch cap down onto my head and then she and my father stepped back to inspect me.

MOM: (excitedly) I know what's missing! (she exits)

FATHER: (insulted by the casting) Why are you playing an elf anyway?

PAUL: I don't know . . . I guess they think I look like one. (to audience) Before my father's disapproval could scar me for life, my mother ran back in with some cotton balls and a bottle of Elmer's glue and proceeded to put glue on three cotton balls. She took two of them and put one on the toe of each sock. Then she took the third cotton ball and stuck it on top of my hat.

MOM: Now he looks like an elf.

PAUL: My parents stared at me. Several seconds passed. All of a sudden . . . (Mom breaks out in laughter and Dad too) and soon my parents were sitting on the floor, helpless with hysterics. I knew tomorrow would not be a good day. I headed off to school the next morning with my costume in a paper grocery bag. Since I had been blessed with a loud voice and good speaking skills, I was to portray the skeptical elf, for whom the pageant was being held. My character apparently had problems deciphering what the true spirit of Christmas was and it was up to everyone else in the show to convince me that Christmas wasn't just about presents and food. Which was ironic because to every single one of us in that elementary school, presents and food were exactly what Christmas was all about. (to Brian) What's your elf costume look like?

BRIAN: (shrugging) I don't know. It's pretty stupid.

PAUL: I started polling the other kids in the class. They all seemed to think that their costumes were not really very elflike. I started to take heart. Maybe my costume wasn't so bad. True, I looked a little more combat-ready than any elf I'd ever seen but, maybe I was going to be okay. After lunch, our teacher, Miss Connor, informed us it was time to change into our costumes and get ready for the pageant. Out of every bag, my peers produced gaily colored costumes. Bright reds and greens and crisp clean whites made the room glow. And everyone had shoes that looked like they came from a Hollywood studio costume department. These were the most realistic-looking elf costumes I had ever seen, better than the ones worn by the teenagers who worked at the mall and dragged you over to Santa to have your picture taken. And it was in this atmosphere that I pulled out my United States military elf attire.

BRIAN: (in disgust) What color is that?

PAUL: (defensively) It's O.D. green. (disdainfully) O. D. stands for olive drab.

MIKE: Elves aren't that color. You're gonna look like a booger.

PAUL: I put on my outfit and became the focal point of the room.

BRIAN: What's wrong with your feet?!

PAUL: They're elf feet. They're supposed to be big.

BRIAN: Elves' feet aren't big. Their shoes are big.

PAUL: No they're not. It's their feet. They're big and curly. My mom said so.

BRIAN: Well, your mom is wrong.

PAUL: (to audience) Miss Connor came back into the room and looked us all over.

MISS CONNER: Very nice. You all look wonderful. (then she sees our narrator) Oh . . . my!

MIKE: He doesn't look like an elf, does he, Miss Con-nor?

MISS CONNER: I don't know. I think he looks exactly like the kind of elf who would have doubts about Christmas.

PAUL: Miss Connor was now the love of my life! [She] brought us out into the hallway, where the girls were waiting. When [they] spotted me, they stared in disbelief. (to the girls, haughtily) I'm an elf who doesn't know the meaning of Christmas. I'm supposed to look this way!

MICHELLE: You look like a booger that doesn't know the meaning of Christmas. (laughing)

PAUL: It got a huge laugh from both the girls and the guys. One thing's for certain in grade school-a booger joke will always land well with your au-dience.

MISS CONNER: (remembering) Oh, shoot. I was supposed to tell Mr. Kavich's class to come down to the gym in five minutes. Paul, run down to their room and tell them, would you?

PAUL: My heart sank. It was the last thing I wanted to do. Mr. Kavich's class was sixth grade. Even though I knew they were soon to see me in the pageant festooned in my government-surplus elf gear, there was something about their seeing me out of context that I knew spelled trouble.

MISS CONNER: Hurry up. If we forget, we won't have any upperclassmen in the audience. (smiling)

PAUL: (looking like a love-sick puppy) Having crushes on teachers is the surest way of relinquishing any and all power over your dignity when you're a kid. I smiled at her and ran off to deliver my message. I slid up in front of Mr. Kavich's classroom door. I could hear him lecturing behind it. Feeling very cool to be seconds away from entering a sixth-grade classroom as a lowly first grader, I opened the door and stepped inside. That was as far as I got. (laughter from everyone) As I stood there, watching both the students and Mr. Kavich become helpless with laughter, I pondered whether this was the kind of joy and goodwill I, as an elf, was supposed to be bringing to the world. I was definitely taking one for Santa's team. The pageant was a blur to me. There are unsettling home movies from the event. Behind me in a sloppy line are my fellow elves, fidgeting and shifting their weight and picking their noses and engaging in general unprofessional stagecraft. (proudly) I, on the other hand, had overcome the handicap of my costume, the mockery of my peers and schoolmates, the stifled laughter of every teacher and parent in the audience, and I discovered the true meaning of Christmas. I had learned that it was about more than just clothes and presents and decorations. And [I] hadn't done it for them, not for [myself], and, no, not even for Santa. No, the skeptical surplus elf had done it all for one thing and one thing only . . . The United States Army. (salute)
```

---

## IC-2371: Arnie the Doughnut

- Title: Arnie the Doughnut
- Author (byline): Lori Keller
- Work: Not specified
- Publisher: Square Fish
- Publication date as stated: May 2016
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, ARNIE, BAKER, DONUT 1, WAITER, ICER, WORKER, CINNAMON TWIST, CHOCOLATE ZEBRA, SQUARE, POWDERED, LONG JOHN, BEAR CLAW, APPLE FRITTER, MR. BING, FRENCH CRUELLER
- Teaser before the introduction: Yes
- Spoken words (computed): 1027
- Already set (do not supply): none

### Source block (context only)

```text
Author: Laurie Keller
ISBN: 978-1250079473
Publisher: Square Fish
Date (Month/Year): May 2016
```

### Introduction (context only: never use it for content warnings)

```text
Arnie is colorful, covered in sprinkles, and full of personality! He thinks life at the bakery is pretty sweet -- until he finds out that doughnuts aren’t adopted, they’re eaten. Yikes! But once the sprinkles have settled, Arnie’s determined to prove he’s more than just breakfast . . . he’s best friend material!

Arnie the Doughnut by Lori Keller
```

### Performance text (classify this)

```text
NARRATOR: Arnie turned out to be just the kind of doughnut he’d hoped he’d be – chocolate-covered with bright-colored candy sprinkles.

ARNIE: Look at all my sprinkles – there must be a million of them!

BAKER: (stage whispers to audience) Actually, there are only 135, but I’m not going to spoil it for him.

NARRATOR: He was made very early in the morning at the Downtown Bakery, “Home of the Best Doughnuts A- Round!”

DONUT 1: (with a wiggly hula motion) “A-Round?” Get it?

NARRATOR: Arnie was proud to be one of the best. He knew that people all over town made special trips to his bakery to buy doughnuts of their very own. As Arnie sat on the tray, which had just been placed in the doughnut case, he took a moment to reflect on the amazing things that had happened to him that morning. 1 -- Cut into ring [in the] Ringy-Dingy Doughnut-making Thingy.

ARNIE: (as if going down a slide) Wheeeeee!

NARRATOR: 2 – Deep fried

ARNIE: (doing the back stroke, swimming) I’m soaking in boiling grease, but I love it!

NARRATOR: 3 – Cooled

WAITER: (serving Arnie) Your drink, sir!

ARNIE: (taking a long sip through a straw) Thank you!

NARRATOR: 4 – Iced

ICER: (as if in a salon/stylist) Who’s that handsome doughnut?

ARNIE: (admiring himself) That’s me!

NARRATOR: 5 – Sprinkled

WORKER: (reading sign and putting on goggles) CAUTION—Sprinkle Area. Must wear safety goggles!

NARRATOR: 6 – Named

ARNIE: (assuming a rap persona) Whatever I’m named, I’m going to go by Cool Iced-D.

NARRATOR: Arnie looked around and saw all sorts of doughnuts sitting nearby.

CINNAMON TWIST: (with an accent) Cinnamon Twist!

CHOCOLATE ZEBRA: (with another accent) Chocolate Zebra

SQUARE: (in a nerdy persona) Square

POWDERED: (another persona using a powder puff) Powdered.

LONG JOHN: (a pirate accent) [Yo, ho ho!] Long John

BEAR CLAW: (with a growling roar, and swipe of claws) Bear claw!

NARRATOR: He tried to strike up a conversation with an apple fritter on the next tray over, but she didn’t seem to want to talk.

APPLE FRITTER: (giving him the cold shoulder) Humffff!

ARNIE: It is rather early. Maybe she’s not a morning doughnut.

NARRATOR: It was 6 am and the baker had just hung the OPEN sign in the window. Arnie was fascinated as he watched customers stream into the bakery. One by one, doughnuts were chosen, placed in paper bags and whisked away with their new owners. Some went by the dozen in giant boxes.

ARNIE: (waving merrily) Goodbye! Have a great trip! (to audience) This is so exciting! I wonder who will choose me?

NARRATOR: Just then, Arnie looked up and saw a man pointing right at him!

ARNIE: (honored and excited) Moi? (he’s lifted off the tray)

NARRATOR: Before he could say another word, he was pulled from the tray and placed in a paper bag of his very own.

SQUARE: Good-bye, Arnie!

CINNAMON TWIST: We’ll miss you!

BAKER: (to customer) Thank you, Mr. Bing. Have a nice day!

APPLE FRITTER: (with tears) I should have talked to him while I had the chance.

NARRATOR: The ride to Mr. Bing’s apartment was a little bumpy.

ARNIE: (tossed around) Whoa! Whooooaaa! (trying his hardest to push the bag open) Why does he keep me in this bag?

NARRATOR: Finally, the car came to a stop and they were home.

MR. BING: (carefully removes Arnie from his paper bag and places him on a plate)

ARNIE: (wriggling around to see the plate) What a handsome plate! I’m not crazy about the design. I prefer a more modern look.

MR. BING: (lifts Arnie from the plate, humming in anticipation)

ARNIE: Isn’t that cute? (closing his eyes and smiling) He wants to hold me!

MR. BING: (opens his mouth wide)

ARNIE: (opens eyes and screams) What are you doing?!

(stretching arms and legs as wide as possible to prevent being eaten)

MR. BING: (shocked, he drops Arnie back on the plate) I was going to . . . eat you.

ARNIE: EAT ME?!! (sprinkles flying everywhere) Why would you do a thing like that? Do you make a habit of eating all your houseguests?!

MR. BING: No . . . of course not. [But] you’re a doughnut. That’s what doughnuts are for – to eat.

ARNIE: (aghast) Do you mean to tell me you’ve done this before?

MR. BING: (sheepishly) Yes . . . I eat a doughnut every day.

NARRATOR: (to audience, frightened) I’d better get out of here before he tries to eat me again! (then angry) My friends have probably all been eaten! (thinks for a moment) I must put a stop to this right away! I’ll call the bakery and warn the others.

NARRATOR: Arnie knew there was no time to waste and he needed to be very sneaky in order to keep his plan from Mr. Bing.

ARNIE: (to Mr. Bing in his sweetest voice) Excuse me, sir, I don’t believe we’ve been properly introduced. My name is Arnie. (offers hand to shake after licking off a few sprinkles)

MR. BING: (still trying to figure out what’s going on, he stammers) Um. . . hello . . . I’m Mr. Bing. It’s nice to eat, I mean, meet you.

ARNIE: (slyly and extra politely) Mr. Bing, would you be a dear and allow me to use your telephone? (Mr. Bing hands Arnie his phone and Arnie quickly dials – phone rings)

BAKER: (answering) Downtown Bakery. . .

ARNIE: (ominous music as Arnie interrupts, whispering frantically) Mr. Bakerman! This is Arnie the doughnut. I was bought about 20 minutes ago by a man who goes by the name Mr. Bing!

BAKER: Yes, Arnie, what can I do for you?

ARNIE: I don’t want to alarm you, but that man tried to eat me! And not only that – he claims to have eaten 100s of us! I’m going to make a run for it, but I wanted to warn you so if you see him coming into the bakery again, you can stop him!

BAKER: (unconcerned) That’s why I make doughnuts – for people to eat.

ARNIE: (gasps) Are the other doughnuts aware of this arrangement?

BAKER: (yells to other doughnuts) Do you doughnuts know you’re going to be eaten?

LONG JOHN: (pirate accent) We know!

FRENCH CRUELLER: (with French accent) We’re delicious! I don’t blame them.

ARNIE: (crushed, the phone drops from his hand)

NARRATOR: Arnie forgot all about his plan to escape.

ARNIE: (collapses onto the plate, looks up at Mr. Bing and mutters resignedly) All right then, let’s get this over with. Go ahead and eat me.

MR. BING: I wouldn’t feel right about it now. (Arnie sighs in relief) But! Since I’m not going to eat you. I’ll have to figure out something. I paid good money for you. I don’t want to be wasteful.

ARNIE: (spinning and whirling) Do you need a ballroom dance partner?

MR. BING: I don’t dance . . . I could use you as a pincushion.

ARNIE: (wincing) Ohhh, too painful! (thinking) Would you like me to entertain you at parties? (singing) “Doughnut make my brown eyes blue”

MR. BING: I don’t like throwing parties. (thinking) I need a new bowling ball. . . (picks up Arnie and rolls him along the floor)

ARNIE: (woozy) I could be your chauffeur, or I’d make a great body guard. (assumes a fighting stance)

MR. BING: You can’t see over the steering wheel . . . [and] Who would you protect me from . . . a cookie?

NARRATOR: They were both completely out of ideas.

MR. BING: I’m sorry, Arnie, but it’s clear that we can’t agree on anything for you to do around here. (beat) I think it would be best if you found another home.

ARNIE: (sadly, wiping tears from his eyes with the napkin) Is it all right if I keep this napkin to pack up all my loose sprinkles? (blows nose then gathers sprinkles) I guess doughnuts really are only good for eating, aren’t they?

(he leaves dejectedly)

NARRATOR: He walked past the mailboxes and the apartment manager’s office. But when Arnie reached the “NO DOGS ALLOWED” sign at the end of the driveway, Mr. Bing suddenly came up with a new idea.

MR. BING: (running after him) Arnie! Wait up! (out of breath) I can’t believe I didn’t think of this earlier!

(excited) I’ve always wanted a dog, but could never have one. There’s no sign that says “NO DOUGHNUTS ALLOWED” (Arnie perks up) Would you like to take walks and play fetch?

ARNIE: You bet I would!

MR. BING: Can you do trick, like rolling over?

ARNIE: Rolling over? Look at me – I was made for rolling over!

MR. BING: Arnie . . . will you be my doughnut-dog?

ARNIE: *Arf! Arf! Arf!* (panting and jumping around)

NARRATOR: From that moment on, Arnie and Mr. Bing were inseparable.

ARNIE: *Arf! Arf!* (shakes like a dog, then picks up flying sprinkles)
```

---

## IC-2372: Ass Burger

- Title: Ass Burger
- Author (byline): Augusten Burroughs
- Work: Magical Thinking: True Stories (pg 171-180)
- Publisher: Oct 2004
- Publication date as stated: St. Martin's Press
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, JOHN, MOM
- Teaser before the introduction: No
- Spoken words (computed): 1432
- Already set (do not supply): none

### Source block (context only)

```text
Author: Augusten Burroughs
Book: Magical Thinking: True Stories (pg 171-180)
ISBN: 978-0312315948
Publisher: Oct 2004
Date (Month/Year): St. Martin's Press
```

### Introduction (context only: never use it for content warnings)

```text
People with Asperger's Syndrome are often described as having social skills deficits, a reluctance to listen, difficulty understanding social give and take, and other core characteristics. So let’s see . . . based on these “symptoms” – Abraham Lincoln, Albert Einstein, Emily Dickinson and Beethoven would have been suffering from this syndrome. Why is it that people who function outside what society has determined is “normal” must have a diagnosis, a mental disorder . . . a syndrome? Can’t people just be appreciated for the unique individuals they are?

In Ass Burger by Augusten Burroughs, acceptance is a given, the diagnosis is merely “secondary information.”
```

### Performance text (classify this)

```text
NARRATOR: (Pg 171 – 180) The summer my big brother, John, turned fifteen, he read the Encyclopedia Britannica from A to Z. As he finished each volume, he would leave it on my bed, so that I could do likewise. But I did not do likewise. What little factual information I absorbed in my life was gleaned from lectures the Professor gave to Gilligan. . . He simply could not comprehend this.

JOHN: You didn’t read any of them?

NARRATOR: I looked at some of the pictures . . . Those transparent pages with naked people and their insides, that was neat.

JOHN: Well, that’s just unacceptable. I mean, you’re reading at a third-grade level. Don’t you find that alarming?

NARRATOR: Considering I was in the third grade, no, I didn’t. And from this moment on my brother treated me as not just his younger brother, but his “borderline retarded” younger brother. In fact, this is exactly how he introduced me to his friends:

JOHN: This is my younger brother. You can just ignore him; he’s basically retarded. Our mother smoked while she was pregnant with him, and I guess there was brain damage.

NARRATOR: But to me, it was my brother who seemed retarded. Either that or a genius, I couldn’t decide. All I knew for sure was that he was a peculiar creature. While he could not fathom a younger brother who did not share his fascination with quantum mechanics, I likewise could not comprehend that my brother didn’t own a single pair of platform shoes. As far as I was concerned, he was in training to become a creepy gas station attendant, while I was going to be a star. . . So what, exactly, was he? On the one hand, my brother knew how to create something called a circuit board, which, when attached with wires to a series of strobe lights and placed next to our sleeping mother, provided a shocking amount of fun. Instead of a baseball glove, my brother had an oscilloscope on his dresser. And if you asked him, “Are platinum records really made of platinum?” you would get a thirty-minute discourse on the periodic table, including the half-life of each element. But on the other hand, my brother seemed like somebody best confined to a basement. Not only was he gruff and abrupt, but he spoke in a deadly monotone at all times. He never made eye contact. And he took no pride in his appearance, seeing nothing wrong with wearing pants that had been too short for years. When my parents had guests, my brother often asked shockingly rude questions:

JOHN: Didn’t you have an abortion last year?

MOM: (shrieking) John, that is absolutely none of your business. How dare you ask such a question!

JOHN: (grunting, then snorting) Well, I thought you said she had an abortion. One of your friends did. I thought it was this ‘Nancy’ character.

NARRATOR: Thankfully, my brother spent much of his time alone in his room, the walls of which were covered with images of trains: steam engines, cabooses, sometimes close-ups of the wheels themselves. Quite different from the walls of my room, which were decorated with pages torn from Tiger Beat. Occasionally, we would do “activities” together. Once, we took an old pair of his jeans and an old shirt and stuffed them with bed sheets. Next we stapled the seams to create a “body.” My brother then led me down a path a few miles from our house, and we tied a rope around the body and slung it up over one of the rails of the power-line scaffolding. Later at home my brother phoned the local police and informed them that there had been a ritual hanging in the neighborhood. As sirens streamed down our little dirt road my brother smirked and chuckled.

JOHN: That should occupy them for a while.

NARRATOR: My brother moved out of the house when he was seventeen and began living with a rock band. He wasn’t interested in playing an instrument; he was interested in building the various electronic components. Word spread about a grubby, clever kid who was good with electronics. And this is how it happened that my strange and aloof brother built the rocket-shooting, fire-spitting, exploding guitars for the band Kiss. His name began to appear in magazines next to the word “brilliant.” Other kids say “My big brother can beat you up.” I was able to say “My big brother is a genius like Einstein.” It’s twenty-five years later, and my brother’s rock-band days are over. He owns a very successful car dealership and service center where he sells previously owned Range Rovers, Rolls Royces, and other staggeringly expensive cars.. He is married now, and he has a son. We speak on the phone each day because he calls me on the way to work in the morning.

My brother never asks how I am or what I’m feeling. He simply begins speaking, as though we have already been on the phone for an hour. Often, he begins mid-thought.

JOHN: So the kid, he’s not very happy with me - I told him about Santa Claus. . . . I said, ‘You know kid, Santa can’t earn a living working just one day a year.’ And then I told him how on the off-season, Santa works at Europort in Rotterdam, unloading container ships. Only he got fired for drinking on the job, and now he’s depressed, so there might not even be a Christmas this year. (laughs)

NARRATOR: I smile at how awful he is to his ten-year-old son, who already takes his father with a grain of salt. (to John) That’s horrible. You shouldn’t tell him things like that.

JOHN: (laughing) Oh, and I went to a psychologist, and she said I have Asperger’s syndrome.

NARRATOR: What?

JOHN: She said I’ve had it my whole life, and it explains why people think I’m weird.

NARRATOR: Wait a minute, what? Why did you see a psychologist? What is this thing called again? (to audience) He tells me the name again and spells it (because I thought it was “Ass-Burger”) and then says, “I gotta run.” And he is gone. I go online to read about this condition, which my brother suddenly has, which sounds like a sandwich made from donkey flesh. Asperger’s syndrome was named for Hans Asperger, a Viennese physician who published a paper in 1944 describing autistic-like behavior in several young boys. But it wasn’t until 1994 that Asperger’s syndrome was added to the DSM IV, and only in the past few years has AS been recognized by professionals and parents. So for fifty years, these kids were driving their families insane, undiagnosed, and wanting to chase trains in the car. And now, suddenly, Asperger’s syndrome is chic. Bill Gates is said to have Asperger’s. It is also suspected that the condition afflicted Albert Einstein. It is associated with geniuses, and this is why Manhattan parents are often secretly thrilled to have their bratty, brainy, introverted children diagnosed with this condition. It is the first trendy thing ever to occur in the atmosphere surrounding my brother. People with Asperger’s tend to be obsessed with trains and cars. My brother’s first word was “car.” He owns a car dealership that fixes high-end automobiles. And all his life his walls (and now office) have been hung with pictures of trains. Check. People with Asperger’s tend to have “fanciful vocabularies.” Immediately, I know exactly what this means. When my brother’s dog is happy, he describes it as “tail up.”

JOHN: Yup. Dog-o is tail up ninety percent of the time.

NARRATOR: He also speaks of Fire Lizards. These, he claims, are employed in shops by glass artisans. They sleep on the floor in the work area, and then the glass blower steps on the Fire Lizard’s tail, and it exhales fire, which the artist uses to melt and shape the glass. The more I read about this condition, the more I read about my brother, an individual unlike anybody I have ever met before. Clearly, not only does my brother have Asperger’s syndrome, he is the poster boy for it. A lack of interest in other people. Avoidance of eye-to-eye contact. A lack of social skills. Check, check, check. It was a list. But when you combine the elements on the list, the result is a person most kindly described as “extremely eccentric.” A weight has been lifted. It’s not all my fault. I’m not retarded. Or slow. It’s him. It’s always been him. And nobody knew it. My next emotion is one of protection. I will now beat the *crap* out of anybody who is mean to my big, lumbering brother with his unusual, one-in-a-trillion brain.
```

---

## IC-2373: The Attack

- Title: The Attack
- Author (byline): Yasmina Khadra
- Work: Not specified
- Publisher: Nan A. Talese.
- Publication date as stated: May 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1415
- Already set (do not supply): none

### Source block (context only)

```text
Author: Yasmina Khadra
ISBN: 978-0385517485
Publisher: Nan A. Talese.
Date (Month/Year): May 2006
```

### Introduction (context only: never use it for content warnings)

```text
The mind of a religious terrorist is difficult for a Western person to comprehend. What could lead a person to cause his or her own violent death is a question that is frequently raised. It is contrary to every human emotion that we have. Yet, we know there are hundreds of Islamic fundamentalists who are willing to kill and be killed for Allah. All over the world, in Kenya, Algeria, Indonesia, Egypt, Iran, France, South America and America, terrorists have attacked and murdered those they felt were a threat to their religious aims. No one has been spared. "The Attack" by Yasmina Khadra portrays the individual reality of terrorism and its incalculable spiritual costs.
```

### Performance text (classify this)

```text
I don't remember hearing an explosion. A hissing sound, maybe, like tearing fabric, but I'm not certain. My attention was distracted by that quasi-divinity and the host of devoted followers surrounding him as his bodyguards tried to clear a passage to his waiting automobile. "Let us pass, please. Please move out of the way." The faithful elbowed one another, hoping to get a better look at the sheikh or touch a part of his "kamis." From time to time, the revered old man turned to greet an acquaintance or thank a disciple. The eyes in his ascetic's face glinted like the blade of a scimitar.

I was being crushed by the enraptured throng and tried in vain to break free. The sheikh plunged into his vehicle, waving with one hand from behind the bulletproof glass while his two bodyguards took their places on either side of him. And then...but there's nothing more. Something resembling a lightning bolt streaks across the sky and bursts like a giant flare in the middle of the roadway; the shock wave strikes me full force; the crowd whose frenzy held me captive disintegrates. In a fraction of a second, the sky collapses, and the street, fraught with the fervor of the multitude a moment ago, turns upside down. The body of a man, or perhaps a boy, hurtles across my vertiginous sight like a dark flash. What's going on? A surge of dust and fire envelops me, flinging me into the air with a thousand other projectiles. I have a vague sensation of being reduced to shreds, of dissolving in the blast's hot breath...

A few yards--or light-years--away, the sheikh's automobile is ablaze. Hungry tentacles enclose it, spreading abroad a dreadful odor of cremation. The roar of the flames must be terrifying; I can't hear it. I've been struck deaf, ravished away from the noises of the town. I hear nothing, I feel nothing; I hover, I only hover. I hover for an eternity before plunging back to earth, stunned, undone, but curiously lucid, my eyes wide open on the horror that has just descended on the town from out of the sky. In the instant when I touch the ground, everything freezes: the flames rising above the destroyed vehicle, the flying projectiles, the smoke, the chaos, the smells, time....Only a heavenly voice, floating over the fathomless silence of death, is singing "One of these days, we'll go back home." It's not exactly a voice; it's more like a rustling, a filigree of sound....My head bounces off something....

A child cries: "Mama!" The call is weak, but distinct and pure. It comes from far away, from some calm elsewhere....The flames devouring the sheikh's car refuse to budge; the projectiles won't fall....My hand gropes among the gravel. I believe I've been hurt. I try to move my legs, to lift my head; not one of my muscles obeys me....

"Mama," the child cries...."I'm over here, Amin...." And there she is, Mama, emerging from behind a curtain of smoke. She advances through the suspended debris, amid petrified gestures, past mouths opened upon the abyss. For a moment, because of her milk white veil and her tormented look, I take her for the Virgin. My mother was always like this, radiant and sad at the same time, like a candle.

When she placed her hand on my burning forehead, she took away all my fever and all my cares....And now "she's here;" her magic powers are still intact. A shudder runs through me from my feet to my head, setting everything free and unleashing delirium. The flames start their macabre movement again, the exploded fragments resume their trajectories, and panic comes flooding back in....

A man in rags, with blackened face and arms, tries to approach the blazing automobile. Although he's gravely wounded, some reserve of stubbornness moves him to try to help the sheikh, no matter what the cost. Every time he puts his hand on the door of the car, a jet of flames drives him back. Inside the blasted vehicle, the trapped bodies are burning. Two blood-covered specters approach from the other side and try to force open the rear door. I see them screaming orders or crying out in pain, but I don't hear them. Not far from where I'm lying, an old man stares at me stupidly; he doesn't seem to realize his guts are exposed to the air and his blood is streaming toward the crater in the street. A wounded man with an enormous smoking stain on his back is crawling across the rubble. He passes quite close to me, groaning and panic-stricken, and gives up the ghost a little farther on, his eyes wide open, as if he's still denying that such a thing could happen to him, to "him." The two specters finally break the windshield and dive into the automobile.

Other survivors come to their aid. With their bare hands, they pull apart the flaming vehicle, break the windows, tear off the doors, and succeed in extracting the sheikh's body. A dozen arms lift him up, carry him away from the inferno, and lay him down on the sidewalk, while a flurry of other hands strives to beat the fire out of his clothes. A deep, intense tingling makes its presence felt in my hip. My trousers have almost disappeared; only a few strips of scorched cloth cover me here and there. Against my side, grotesque and horrible, my leg is lying, still connected to my thigh by a thin ribbon of flesh. Suddenly, all my strength deserts me. I have the sensation that my fibers are separating from one another, already decomposing....

At last, I hear something, the wailing of an ambulance, and little by little, the noises of the street return, break over me like waves, stun me. Someone bends over my body, gives it a summary examination with his stethoscope, and goes away. I see him stoop before a heap of charred flesh, take its pulse, and then make a sign to some stretcher-bearers. A man comes to me, picks up my wrist, and lets it fall again...."This one's a goner. We can't do anything for him." I'd like to hold him back and force him to reconsider his assessment, but my arm mutinies, refusing to obey me.

The child starts crying out again: "Mama...." I look for my mother amid the chaos...and discover only orchards, stretching as far as I can see...Grandfather's orchards...the orchards of the patriarch...a land of orange trees, where every day was summer...and a dreaming boy on the crest of a hill. The sky is a limpid blue. Everywhere, the orange trees are holding out their arms to one another. The child is twelve years old, with a porcelain heart. At his age, there's so much to love at first sight, and simply because his trust runs as deep as his joy, he thinks of devouring the moon like a fruit, convinced that he need only reach out his hand to gather up the happiness of all the world....And there, before my eyes, despite the tragedy that has just ruined forever My memory of that distant day, despite the bodies of the dying scattered in the street and the flames that have now completely overwhelmed the sheikh's automobile, the boy bounds to his feet, his arms spread like a kestrel's wings, and goes running across the fields, where every tree is enchanted....

Tears furrow my cheeks...."Whoever told you a man mustn't cry doesn't know what it means to he a man," my father declared when he came upon me, weeping and distraught, in the patriarch's funeral chamber. "There's no shame in crying, my boy. Tears are the noblest things we have." Since I refused to release Grandfather's hand, my father knelt before me and took me in his arms. "There's no use staying here," he said. "The dead are dead, they're over, they've served their time. As for the living, they're ghosts, too; they're just early for their appointment...."

Two bearers pick me up and put me on a stretcher. An ambulance backs up to us, its rear doors wide open. Arms pull me inside and practically throw me among some other corpses. In my final throes, I hear myself sob.... "God, if this is some horrible nightmare, let me wake up, and soon...."
```

---

## IC-2374: Attack of the Cartoon Animal Heads

- Title: Attack of the Cartoon Animal Heads
- Author (byline): Dave Barry
- Work: Dave Barry Talks Back, Pg 66-69
- Publisher: Crown Reprint
- Publication date as stated: May 1992
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: SALESMAN, NARRATOR, COUNTRY FELLA, ROBBY, ERIK, EXECUTIVE, JOHNSON
- Teaser before the introduction: No
- Spoken words (computed): 928
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Barry
Book: Dave Barry Talks Back, Pg 66-69
ISBN: 978-0517588680
Publisher: Crown Reprint
Date (Month/Year): May 1992
```

### Introduction (context only: never use it for content warnings)

```text
IN THE VOICE OF A REALLY BAD, ANNOYING
```

### Performance text (classify this)

```text
SALESMAN: Experience an Orlando resort getaway within this Downtown Disney hotel that ascends above the rest. Soaring 27 stories above the world's favorite destination, Buena Vista Palace Hotel & Spa in the WALT DISNEY WORLD® Resort raises the bar for exceptional quality and service in this sunny locale. Feel the magic the moment you arrive at our exclusive Walt Disney World hotel. Take a refreshing dip in one of three outdoor pools. Schedule a soothing treatment at our full-service Spa and Salon. Experience the thrill of world-famous Downtown Disney, with its vibrant shops, delicious restaurants, and exhilarating nightlife. For work or play, delight in our exclusive amenities, stunning accommodations, and alluring setting . . . Oh, and don’t forget to bring your kids to tonight’s entertainment, arrive early for the Attack of the Cartoon Animal Heads by Dave Barry!

NARRATOR: (Pg 66-69) It’s a Sunday evening, and we’re driving home from Orlando, where we have taken our son, Robby, and his friend, Erik, for a special birthday weekend of fantasy and fun and hurling money at random around the Official Walt “You will Have Fun” Disney Magical World of Theme Kingdoms and Resort Complex. We’re taking what the American Automobile Association has designated as the “scenic route” back to Miami, through south-central Florida, a region that used to cater primarily to frogs but that has in recent years sprouted dozens of “adult” (which we used to call “retired person”) communities with names like Belle Harbour, Vista Manour, Downes Estates, and Centre West II, consisting of what we used to call “trailers,” and later we called “mobile homes,” and still later we called “manufactured houses.” I don’t know what we call them now. Probably something like “countrie townehome villas,” as in . . .

COUNTRY FELLA: Hey, Ed! Lester’s cow knocked over your countrie townehome villa again!

NARRATOR: We’ve been driving for three, maybe eight hours. In the backseat, the boys have finished writing on their forearms with Official Walt Disney World souvenir felt-tipped markers and are now passing the time with a little game they have invented with the soaring childhood imaginations: spitting on each other.

ROBBY: (spitting) Ptooo!

ERIK: (spitting) Ptooo!

ROBBY: (spitting) Ptooo!

NARRATOR: This little game of saliva tennis is clearly audible in the front seat, but Beth and I, the Parental Authority Figures, say nothing. We are both thinking the same thing: At least they are taking turns. That is how low we have sunk on this car trip. We frankly would not mind if they were back there shooting a high-powered rifle out the window, as long as they shared it. But, of course, they wouldn’t.

ROBBY: (shouting) No fair! Erik got three shots and I only got two but he won’t give me back the rifle!

ERIK: But Robby hit the farmer and I didn’t hit anybody!

ROBBY: You did too! You hit the policeman!

ERIK: Only his hat!

NARRATOR: And finally one of us Authority Figures would whirl around and snap,

BETH (MOM): If you can’t share the rifle, we’re going to take it away and . . . and then NOBODY WILL BE ABLE TO SHOOT ANYBODY.

NARRATOR: We always get irritable like this when we return to harsh reality after a couple of days in Walt “You Are Having Some Fun Now, Yes?” Disney Resort and World and Compound, a place where your dreams really do come true, if you dream about having people wearing enormous cartoon-animal heads come around to your restaurant table and act whimsical and refuse to go away until you laugh with delight. This happens to you constantly at Disney World. I think it’s part of a corporate discipline program for Disney executives.

EXECUTIVE: Johnson, your department is over budget again. You know what that means.

JOHNSON: No! Please!

EXECUTIVE: Yes! Into the Goofy suit!

NARRATOR: We saw a lot of Goofy. Every time we sat down to eat, there he would be, acting whimsical. It got so that Robby and Erik, busily playing with their action figures, hardly even noticed him. (with mouth full, to the boys) Look, boys! Here comes Goofy! Again!

(to audience) Robby, not even looking up, would thrust one of his figures toward Erik and say:

ROBBY: This guy sends out a laser beam that can MELT YOUR EYEBALLS.

ERIK: Oh, yeah? Well this guy makes a noise like, mmmmmmPAAAAAH!, that goes through your ears and EXPLODES YOUR WHOLE HEAD.

NARRATOR: Meanwhile, right behind them, encased in a heavy costume, this poor person, probably the executive vice president for group sales, would be writhing around, trying desperately to fulfill the boys’ innocent childhood fantasies. Finally, we grown-ups would have to let him off the hook. “Ha, ha, Goofy!” we would say, speaking directly into the saltshaker, which is where we figured the microphone had been hidden by the Walt Disney Would Whimsy Police. “You sure are causing us to laugh with delight!” Don’t get me wrong. I like Disney World. The rest rooms are clean enough for neurosurgery, and the employees say things like, “Howdy, folks!” and actually seem to mean it. You wonder: Where do they get these people? My guess: 1952. I think old Walt realized, way back then, that there would eventually be a shortage of cheerful people, so he put all the residents of south-western Nebraska into a giant freezer with a huge picture of Jiminy Cricket on the outside, and the corporation has been thawing them out as needed ever since. Whatever the secret is, it works, and I urge you all to visit Disney World several dozen times. Afterward, I recommend that you drive down to Miami on the “scenic route,” although if you notice two boys, ages 6 and 7, standing on the side of the road spitting at each other, my advice is not to pick them up.
```

---

## IC-2375: Autopsy Room Four

- Title: Autopsy Room Four
- Author (byline): Stephen King
- Work: Everything's Eventual: 14 Dark Tales (Pg 19)
- Publisher: Scribner
- Publication date as stated: March 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: HOWARD, ORDERLY, PATHOLOGIST, PETER, AMBULANCE DRIVER
- Teaser before the introduction: Yes
- Spoken words (computed): 1714
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephen King
Book: Everything's Eventual: 14 Dark Tales (Pg 19)
ISBN: 978-0743235150
Publisher: Scribner
Date (Month/Year): March 2002
Watch Alfred Hitchcock’s “Breakdown” here
https://the.hitchcock.zone/wiki/Alfred_Hitchcock_Presents
_-_Breakdown
```

### Introduction (context only: never use it for content warnings)

```text
Alfred Hitchcock was a master of mystery and suspense. In 1955 he launched a television episode to rival The Twilight Zone. The plot of Breakdown went something like this: William Callew, a hard-nosed and hard-hearted businessman who holds in contempt such human failings as sentiment, pity, and tears. While racing to keep an appointment in New York, Callew is involved in a spectacular car accident. Awakening, he finds that he is completely paralyzed, unable to move or speak -- though we hear his every thought on the soundtrack. Everyone who comes across Callew assumes that he is dead, including the police and the coroner...and as the episode draws to its conclusion, the horrified Callew is being wheeled into the autopsy room of the morgue!

But that could never happen in real life – or could it? Autopsy Room Four by Stephen King.
```

### Performance text (classify this)

```text
HOWARD: (Pg 19-44) It’s so dark that for a while, I think I’m still unconscious. Then, slowly, it comes to me that unconscious people don’t have a sensation of movement through the dark, accompanied by a faint, rhythmic sound that can only be a squeaky wheel. And I can feel contact from the top of my head to the balls of my heels. This is not unconsciousness, and there is something too… too rational about the sensations from it to be a dream. Then what is it? What’s happening to me? The squeaky wheel quits its stupid rhythm and I stop moving. What’s going on here? I yell, but the yell is only in my head. My lips don’t move. I can feel them, but I can’t move them.

HOWARD: I’m grabbed, shoulders and calves, and lifted. I’m swung through the air in an envelope of blackness- Hey, don’t drop me, I’ve got a bad back! I try to say, and again, there’s no movement of the lips or teeth. What if I’m dead? What if this is what death is like? It fits. The dark, the rubbery smell. Nowadays I am Howard the Conqueror, stockbroker extraordinaire, terror of Derry Municipal Country Club, frequent habitué of what is known at golf courses all over the world as the Nineteenth Hole, but in ’71 I was part of a Medical Assistance Team in the Mekong Delta, a scared kid who sometimes woke up wet-eyed from dreams of the family dog, and all at once I know this feel, this smell. Dear God, I’m in a body bag.

ORDERLY: Want to sign this, doc? Remember to bear down hard-it’s three copies.

HOWARD: Sound of a pen, scraping away on paper. I imagine the owner of the first voice holding out a clipboard to the doctor. Oh dear Jesus let me not be dead! I try to scream, and nothing comes out. I’m breathing though… aren’t I? I mean, I can’t feel myself doing it, but my lungs seem okay, they’re not throbbing or yelling for air the way they do when you’ve swum too far underwater, so I must be okay, right? There’s a harsh ripping sound and all at once I am in white light; it is blinding, like the sun breaking through a scrim of clouds on a winter day. I try to squint my eyes shut against it, but nothing happens. My eyelids are like blinds on broken rollers. A face bends over me, blocking off part of my glare. Help me! But I can only look up into his dark blue eyes with my frozen dead man’s stare. If I’m still alive, how come he hasn’t seen my pupil’s contract when the light hit them? But I know the answer to that… or I think I do. They didn’t contract. That’s why the glare from the fluorescents is so painful. Soft shoes squeaking on tile, and suddenly that sound is replaced by the sound of my driver, beating the bush for my ball. I hate fourteen, supposedly there’s poison ivy, and with all this underbrush, there could easily be. And then something bit me, didn’t it? Yes, I’m almost sure it did. On the left calf, just above the top of my sock. A red-hot darning needle of pain, perfectly concentrated at first, then spreading… …Then darkness. Until the gurney, zipped up snug inside a body bag. I want to think it was some kind of snake, but maybe that’s only because I was thinking about them while I hunted for my ball. It could have been an insect, I only recall the single line of pain, and after all, what does it matter? What matters here is that I’m alive and they don’t know it. The clank is followed by a sound that scares me badly: steel instruments clicking together. They are off to the left of me, and although I can’t see them, I know what they’re getting ready to do: the autopsy. They are getting ready to cut into me. They intend to remove [my] heart and see if it blew a piston. My leg! I scream inside my head. Look at my left leg! That’s the trouble, not my heart! The scissors have long, sharp blades, very sharp blades, and fat slides into the but like butter. Then, snip, up through the bundle of nerves at the solar plexus and into the beef jerky weave of muscle and tendons above it. Then into the sternum. When the blades come together this time, they do so with a heavy crunch as the bone parts and the rib cage pops apart. They’re going to do it. I have to make some kind of noise or movement, or they’re really going to do it. If blood flows or jets up from the first punch of scissors they’ll know something’s wrong, but by then it will be too late. I concentrate everything on my chest. I push, or try to… and something happens. A sound! I make a sound! It’s mostly inside my closed mouth, but I can also hear and feel it in my nose- a low hum. I am lifted. Then I am laid flat again and my shirt is gone. I’m now naked to the waist. It’s cold in the room. Look at my chest! I scream. You must see it rise and fall, no matter how shallow my respiration is! You’re an expert, for Christ’s sake!

PATHOLOGIST: Do you want to handle temp and gross examination?

PETER: Hey, as long as you’ll cover for me if…

PATHOLOGIST: Sure. Got to get your feet wet sometime, Peter. And if you really need me to, I’ll roll the tape back.

PETER: You can do that?

HOWARD: Surely they won’t really cut me up will they? Pete is no veteran, but he has had some training; surely he’ll see the marks of whatever bit me while I was looking for my ball in the rough, and then they’ll at least suspect. They’ll have to suspect.

PETER: Ready, doctor.

HOWARD: Somewhere, tape is rolling. The autopsy procedure has begun.

PETER: Subject is a white Caucasian, age forty-four. His name is Howard Randolph Cottrell, residence is 1566 Laurel Crest Lane. Cause of death may be a heart attack. No neck injury apparent, no rigor. No wounds visible on the back or buttocks, although there’s an old scar on the upper right thigh that looks like some sort of wound, shrapnel, perhaps. It’s an ugly one. (taking the body temperature) 94.2. Gee, that ain’t too shabby. This guy could almost be alive.

PATHOLOGIST: They found him in the rough. At a guess, he had a heart attack while he was looking for his ball. Keep going, Peter, you’re doing fine.

PETER: (continuing the external exam) There are mosquito bites on the left calf that look infected.

HOWARD: I focus all my will and effort on closing my eyes while he’s looking down onto my face, and cannot produce even a tic. All I wanted was eighteen holes of golf on a Saturday afternoon, and instead I turned into Snow White with hair on my chest. And I can’t stop wondering what it’s going to feel like when those poultry shears go sliding into my midsection.

PETER: I am commencing the autopsy at 5:49 P.M. Saturday, August 20th, 1994.

HOWARD: He lifts my lips, looks at my teeth like a man thinking about buying a horse, then pulls my jaw down.

PETER: Good color and no petechiae on the cheeks… man this guy really could still be alive!

PATHOLOGIST: (laughing) Doesn’t he wish.

HOWARD: This time it’s cancer I wish on them, some kind that is inoperable and lasts a long time. (Burp) He looks at me, eyes widening, mouth dropped a little, and again I try desperately to hum, knowing he won’t hear it but thinking that maybe, along with the burp, he’ll finally be ready to see what’s right in front of him…

PATHOLOGIST: (chuckling) Excuse yourself, Howie.

HOWARD: Now I’m trying to stick out my tongue. Just that simple kid’s gesture of impudence, but it would be enough… and it seems to me I can feel a faint prickling sensation deep within my lips, the feeling you get when you’re finally starting to come out of a heavy dose of Novocain. And I can feel a twitch? No, wishful thinking, just… Yes! Yes! But a twitch is all, and the second time I try, nothing happens. Pete turns the scissors at an angle so the light runs down the blade, and for the first time I’m certain, really certain that this mad charade is going to go all the way through the end. The director isn’t going to freeze the frame. The ref isn’t going to stop the fight in the tenth round. Petie boy’s going to slide those scissors into my gut while I lie here helpless, and then he’s going to open me up like a mail order package. No! I howl, my voice reverberating off the dark walls of my skull but emerging from my mouth not at all. No please no! I try to make the humming noise and discover a horrid thing: now I can’t even to that. I’m too scared. Fright has locked down my vocal cords. I can only stare. He slowly brings them out. I see them… then they’re gone from my field of vision. A long moment later, I feel a steel nestle again my naked upper belly.

PETER: Are you sure you don’t…

PATHOLOGIST: Do you want to make this your field or not, Peter?

HOWARD: The door bursts open. Pete cries out in surprise.

AMBULANCE DRIVER: (frantically) Don’t cut him up! Don’t cut him up, there was a snake in his golf bag and it bit Mike knocking him flat! He’s gonna be okay, I guess, but he can hardly talk! Little brown snake, I never saw one like it in my life, it went under the loadin’ bay, it’s under there now, but that’s not the important part! I think… holy shit doc, watcha tryin’ to do? Stoke him back to life?”

HOWARD: [The pathologist] looks around, dazed, at first not sure of what he’s talking about. And as she screams, screams and snatches the shears out of Pete’s limp gloved hand… I find myself thinking again of that old Alfred Hitchcock TV show. Poor old Joseph Cotton, I think. He only got to cry.
```

---

## IC-2376: Baby Einstein

- Title: Baby Einstein
- Author (byline): David Sedaris
- Work: Dress Your Family In Corduroy and Denim
- Publisher: Little, Brown and Company
- Publication date as stated: June 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2115
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Sedaris
Book: Dress Your Family In Corduroy and Denim
ISBN: 978-0316143462
Publisher: Little, Brown and Company
Date (Month/Year): June 2004
```

### Introduction (context only: never use it for content warnings)

```text
The birth of a baby brings a family and their issues back together in a way nothing else can. Sedaris presents multiple generations of his family as a powerful force both pulling their children towards the family’s collective aspirations and pushing them in the opposite direction. The Sedaris family vies against each other, and the other grandparents, for influence in the life of their youngest sibling’s unborn child in David Sedaris’s Baby Einstein.
```

### Performance text (classify this)

```text
My MOTHER AND I WERE on the beach, rubbing oil into each other's backs and guessing who in the family would be the first to have children. "I think it will be Lisa," I said. This was in the early 1970S. Lisa was maybe fourteen years old and while she wasn't necessarily maternal, she did do things ac-cording to their order. Getting married was what came after graduating from college, and having a baby was what came after getting married. "Mark my

words," I said, "by the age of twenty-six Lisa will have children." It felt very prophetic, but my mother

dismissed it. "No," she said. "Gretchen will be the first." She squinted toward her second daughter, who stood on the shore, pitching meat scraps to a flock of gulls. "It's written on her hips. It will be Gretchen, then Lisa, then Tiffany." I did not include my brother in the baby

prophecy, because every time I saw him he was destroying something, not by accident but willfully, gleefully. He'd dismember his baby, with every intention of putting it back together, but then something would come up - a karate movie, the chance to eat two dozen tacos - and the reconstruction would be forgotten about. Neither my mother nor I could have imagined

that the boy smashing bottles on the path to our cottage would be the first and only one in the family to have a child. By the time it happened, she would be long gone and my sisters, my father, and I would have to bear the shock alone. "It happened so fast!" we would say to one another, speaking as if Paul was like us and preceded every action with ten years of discussion. But he's not like us, and to hear him tell it, the debate ended, and shortly after getting married, he called me to announce that Kathy was pregnant. "Since when?" I asked. Paul held the phone away from his mouth and yelled into the other room. "Mama, what time is it?" "You're calling her 'Mama'?" He yelled for her again, and I told him that if it was four 0'clock in Paris, it was ten A.M. in Raleigh. "So how long has she been pregnant?" He figured it had been about nine hours. And Kathy had become Mama, which would eventually change to Big Mama, and later, for no particular reason, Mama D. After hanging up, he went to the store and bought a nursing chair, a changing table, and a bib reading I LOVE MY DADDY. I thought of those children you sometimes see at demonstrations. ANOTHER TODDLER FOR PEACE, their T-shirts read, or, my favorite, I'M so GLAD MY MOMMY DIDN'T ABORT ME. "Shouldn't you wait until the baby can talk and say that kind of thing for itself?" I asked. "Or maybe at least hold out until it has a real neck. What are you doing buying bibs?" The next time he called he was at the counter of a toy store charging a set of Baby Einstein videos. "I don't care if it's a boy or a girl, but this little kid is going to have brains." "Well, it's sure not going to get them from his parents," I said. "Kathy hasn't even gone to the doctor and already you've got videos?" “crib, too, and I'll tell you what, this stuff is expensive." "Well, so is calling France on a cell phone at eleven o'clock on a Wednesday morning," I said, though again, I don't know who I thought I was talking to. My brother can't survive unless he's breathing into a telephone. If you're an enemy, he'll call only once a day, but if you're a family member and on relatively good speaking terms, you're guaranteed to hear from him once every eight hours or so. There's the money he spends calling us, and then there's the money my sisters and I spend calling one another to talk about how much our brother calls us. Like everyone else in the family, I kept a list of possible names and called every so often to offer them up: Dusty, Ginger, Kaneesha - all of them rejected. The contractors and carpenters my brother works with suggested names as well, most of them inspired by the pending war or the image of America as a tarnished but still shining beacon. Liberty was popular, as was Glory, the slightly Italian-sounding Vendetta, and Kick Saddam's Butt. Which, as my father pointed out, didn't leave much room for a middle name. All of his suggestions were Greek and were offered with a complete disregard of the inevitable taunting they would inspire. "You can't enter the third grade with a name like Hercules," Lisa told him. Then there was the pressure of naming the child after one of its grandparents. Lou and Sharon were options, but there was also Kathy's family to consider. "Oh, right," my sister Amy said. "Them." The Wilsons were nice people, but we saw them as interlopers, potential threats standing between us and what we'd come to think of as the Sedaris baby. "Don't Kathy's parents already have a grandchild?" I asked, speaking as if a grandchild were like a Social Security number or a spinal column - something you needed only one of. We decided they were greedy and capable of anything, yet when the time came to compete, we completely dropped the ball. Their team was out in full force when the baby was born, while we were represented by only Lisa and our father. Kathy was in labor for fifteen hours before the doctors decided to perform a cesarean. They named her Madelyn, which was shortened to Maddy by the time she reached the incubator. I was in a hotel in Portland, Oregon, at the time and received the news from my brother, who called from the recovery room. His voice was soft and melodic, not much more than a whisper. "Mama's got some tubes sticking out of her, but it ain't no big thing," he said. "She's lying back, little Maddy's just as happy as she can be." This was the new, gentler Paul: same vocabulary, but the tone was sweeter and seasoned with a sense of wonder. The cesarean had been unpleasant, but after bemoaning the months wasted in Lamaze class, he grew reflective. "Some is cut loose and others come out on their own self, but take heed, brother: having a baby is a miracle." "Did you just say, 'Take heed'?" I asked.

Kathy returned home later that week, but there were problems. Her legs were swollen. She couldn't breathe. An ambulance carried her to the emergency room, where they drained thirty pounds of fluid from her body: Kathy could not have any more children. "Her heart's too weak,” Paul said “but can you believe that?" His new voice temporarily disappeared. "Breaking bad on Mama D when she's on tap and already scared half to death?” His mind was on these things: his sick wife, the baby he was caring for on his own, and the second, hoped-for child he knew now they could never have. I flew to Raleigh two weeks after the baby was born. Madelyn was asleep when we arrived, and Paul, my father, and I gathered around the crib to adore her in soft voices. One of them suggested that she resembled my mother, but to me she just looked like a baby, not the cute kind you see on diaper commercials but the raw, wrinkled kind that resemble bitter old men. When my father left, Paul heated up a serving of formula. The baby woke up, and Kathy settled her onto the sofa, where the four of us watched videos taken in the hospital. That my brother had not filmed the actual cesarean led me to believe that someone had expressly forbidden it, perhaps for legal or sanitary reasons. There was a blank spot between the arrival of the doctor and the purple-faced baby wailing like an urgent call at the end of her umbilical cord. As if to make up for the missing seven minutes, the recovery-room footage goes on forever. Kathy drinks from a plastic cup of water. A nurse wanders in to change the bandages. Sometimes my sister-in-law held the camera, and we saw Paul in his cutoff shorts and promotional T-shirt, a baseball cap turned backward on his head. The two of them had watched this video dozens of times, but still they sat enraptured. "Here's where that nurse's aide comes in," Kathy said. Paul turned off the volume and as the woman stuck her head through the door he lip-synched her voice. "Look like evabody in here asleep." "Do it again," Kathy said. "Look like evabody in here asleep." "Again." "Look like evabody in here asleep." He held Madelyn up to the TV screen and she gave a little, two-syllable cry that sounded to Paul like "whoopee!" but I interpreted as something closer to "help meeeee." People who have nothing to prove offer practical baby gifts: sturdy cotton rompers made to withstand the cycle of vomit and regular washing. People who are competing for the titles of best-loved aunts and uncles - people like my sisters and me - send satin pants and delicate hand-crafted sweaters accompanied by notes reading "P.S. The fur collar is detachable." The baby is photographed in each new outfit, and I receive pictures almost daily. In them my brother and his wife look not like parents but like backwoods kidnappers, secretly guarding the heiress to a substantial cashmere fortune. Between the still cameras and the video cameras, Madelyn's every move is documented and presented as "Baby's First ... " Baby's First Beach Trip doubled as Baby's First Hurricane. Supported by her mother, she looks past the bent sea oats and out toward the blackening sky, her face creased in an expression of wisdom and concern never seen on either of her parents. The Fourth of July, Halloween, Thanksgiving: these are just days to her, but Paul and Kathy, their logic par-alyzed by love, insist that their daughter is cognizant and as excited as they are. On Baby's First Day of Winter Madelyn sat before a video of A Christmas Carol, then watched as, in imitation of a Victorian gentleman, my brother applied a pair of muttonchop sideburns. This was accomplished not with a disguise kit, but simply, using two strips of raw bacon that ran along his jawline and remained in place for minutes at a time through the miracle of fat against human flesh. Then Paul got out the ladder and taped Christmas lights to the front of his house. They too were short-term, collapsing into the bushes moments after the picture was taken. The baby, of course, already knew what she would be getting. Gifts were presented the moment my brother returned from the store. Baby's First Pop-Up Book. Baby's First Talking Doll… My sister-in-law's condition calls for her to sleep through the night, so when Madelyn wakes at two and three and five A.M., it is Paul's job to feed her or change her, or carry her around the house, begging her to lighten up. There's no point in going to bed, so he kicks his pillow from room to room and collapses on the floor in front of her crib or the swinging chair that sits in the dining room. When the last of my sisters has hit the sack, he dials me up and holds the receiver to his daughter's mouth. For month I listened to her cry long-distance, but then she got a little older and learned how to laugh and coo and sigh in that satisfied baby way that makes me understand how some could bring a child into this lousy world of ours. "She'll turn on him sooner or later," my father says. 'Just you wait. In a couple of years Madelyn won't want anything to do with him." I look into the future and see my brother's face, impossibly middle-aged. His daughter has rejected all of his values, and stands now on the dais of a major university, the valedictorian preparing to deliver her commencement speech. What will she think when her dad stands in the aisle, releasing a hog call and raising his T-shirt to reveal the jiggling message painted upon his bare stomach? Will she turn away, as my father predicts, or might she remember all the nights she awoke to discover him: this slob, this lump, this silly drooling toy asleep at her feet.
```

---

## IC-2377: Bad Dog

- Title: Bad Dog
- Author (byline): Steve Martin
- Work: Pure Drivel
- Publisher: Hyperion Press
- Publication date as stated: Oct 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1050
- Already set (do not supply): none

### Source block (context only)

```text
Author: Steve Martin
Book: Pure Drivel
ISBN: 978-0786885053
Publisher: Hyperion Press
Date (Month/Year): Oct 1999
```

### Introduction (context only: never use it for content warnings)

```text
Dogs are descended from wild wolves, and a dog's perception of the world is based on his ancestral genes just like our perceptions are based upon our genes. For example, if you let your dog do as he pleases no matter how socially unacceptable his behavior, you perceive that you are showing your dog love and being good to him, but that is not what the dog perceives. The dog takes your lack of control of him as a sign that you are weak. He believes that he has attained alpha dog status in his pack and as the alpha dog, he IS the boss.

Then you wonder why he won't obey you. HA! He thinks that you should obey HIM because he is obviously in charge. Obedience training is not cruelty. Obedience training and teaching your dog how to behave himself Just remember that dogs perceive the world in a different way than you do, and it is up to you to see the world from the dog's point of view before you descend with a rolled up newspaper chanting “Bad Dog” by Steve Martin.
```

### Performance text (classify this)

```text
“You’re a bad dog, a very bad dog!” shouts Dr. Fogel.

I’ll show you what a bad dog is, thinks Jasper, padding down the hallway to his dog bowl, where he can think.

Sulking next to his dish, Jasper tries to sort everything out. The FedEx man is supposed to be barked at, dammit. When he is outside the gate, he is outside the threshold of recognition. As he nears, he comes inside the threshold of recognition. Of course I’m going to bark at him, even if I know who he is. The plumber is even lower than the FedEx man. I’m just saying, Watch out, he’s got a wrench. Is that so terrible?

The cat slinks buy. Jasper thinks the one epithet he could never say: Fraidy.

In the next room, Dr. Fogel is on the phone. “Well, I need that package today, doggone it.” Jasper shudders. I hate it when he uses that word. Does he know how it hurts me? Does he know what he’s saying? Why can’t he day Goddammit, like everyone else? Goddammit is a decent, benign swear word, no matter how you look at it. Even backward, it’s . . . it’s. . . oh my dog!

The doorbell rings. Jasper’s up and running to the front door, barking. Master and dog arrive at the same time. “Quiet, Jasper! Quiet!” says Dr. Fogel, but Jasper can’t keep quiet. The door opens. It’s the FedEx man.

Oops, thinks Jasper. He immediately puts his nose between the deliveryman’s legs. They love this; this will be my salvation, he calculates.

But from above he hears, “Bad dog! Bad, bad dog.”

What? Bad dog? Jasper keeps on the happy face but is killed inside. He watches the exchange of signature and receipt then follows Him, hoping for a pat or a word of understanding or just anything. It does not come.

Jasper dips into his bowl of water, hiding his big sad eyes. This is a major, major problem, he thinks. That night, lying on his sawdust-filled bed, Jasper realizes that there’s something in his brain telling him to distinguish between the Federal Express man, who must be barked at in all circumstances, and Granny Fogel, for whom he demonstrates his admiration by rolling over and showing his genitals. But how can I stop myself from doing what I want to do – nay, what I must do? This urge is so strong, based on so many factors, so many subtle discernments. He decides that he lacks some key piece of information, some general rule of understanding that would put him on the clear path. He resolves to search for that knowledge by taking a trip around the world. For Jasper, the world is defined by a five-foot fence that surrounds his yard, the house, and all its contents.

The next morning, Jasper is out early. He sidles along the fence, hugging the wall, nose lowered into the grass. After an hour, he realizes that what he’s doing is pointless, except for the pure fun of it all. He hangs around the kitchen for a while, doing the big-eyes thing, but get nothing. Unrewarded, he moves to his bed for a snooze. Jasper puts his nose next to his last saved biscuit and nuzzles it. He thinks, Questing is hard, and he rolls over on his back, sticks his legs in the air, and falls asleep.

Falling hard into a dream, Jasper imagines himself paddling through the air in a vast gallery of paintings. Although he’s never actually been to a museum, he once guided himself accidentally through London’s Tate Gallery Internet site (the letters T-A-T- E are all left-handers on a keyboard, and one lucky paw slap sent Jasper spiraling into cyberspace). Now, in his dream, he is able to whirl and twist in the air, viewing the pictures up close and reading their museum labels. His dream, swirling up from his simple unconscious, changes each painter’s bio: “Johann Fuseli, Swiss painter and former dog.” “Giovanni Battista Tiepolo, Italian painter and former dog.” Jasper sees that these artists have transformed the canine within themselves into wonderful works of art.

The doorbell jars Jasper out of his sleep. Consciousness takes over, and the beautiful dream fades back into his thin cortex. Rising, he looks through a series of windows, from the bedroom to the kitchen, and beyond the kitchen to the street. He sees the white rectangle of the FedEx truck. Impulsively, he runs toward the front door.

Charging down the hall, he can feel the bark welling up inside him. He is like a boxer with a coiled left hook about to be thrown, like the clapper of an alarm, already in motion toward its bell. He knows what he is facing: the cold censure of his master, balanced by the deliciously frightened face of the FedEx man. The bark churns deep within him. He feels it in his belly, moving up through his lungs. His body chemistry pumps him forward like a jockey’s whip, and he turns the corner to the foyer. There in gleaming white is the target, handing over the trim FedEx box to Jasper’s beloved and vulnerable master. As he slows, the fleshy part of his paws struggling against the hardwood floor, Jasper’s locomotion compresses his energy, forcing the bark into his throat. With his master looking on, he opens his mouth; the bark now lies just behind his tongue. As it rolls over the damp, spongy, pink surface, the miracle that is Art rises from his shallow unconscious and transforms the sound waves, curving the pointy spikes of the highs and rounding the crevices of the jagged lows. Jasper looks up at his master, and out comes, in a lovely baritone:

We’re having a heat wave

A tropical heat wave . . .

Now there is not a sound. A performer’s eon passes: the time between the final note of the aria and the whooshing, enveloping applause of the audience. Finally, into the silent ethereal mist that swarms in Jasper’s head, comes his master’s voice: “Good boy – you’re a good, good boy.”

Jasper turns, feeling the euphoric relief of an adrenaline shutdown. He moves away from the door. The cat walks by. There but for grace of God go I, thinks Jasper. He walks into the kitchen, laps some water, looks back at the startled tableau by the front door, and goes outside to lie in the sun.
```

---

## IC-2378: Barrel Fever

- Title: Barrel Fever
- Author (byline): David Sedaris
- Work: Barrel Fever: Stories and Essays, Pgs 126-150
- Publisher: Back Bay Books
- Publication date as stated: June 1995
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ADOLPH, MOTHER, FAITH, HOPE, JOY, TRUDY
- Teaser before the introduction: Yes
- Spoken words (computed): 1934
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Sedaris
Book: Barrel Fever: Stories and Essays, Pgs 126-150
ISBN: 978-0316779425
Publisher: Back Bay Books
Date (Month/Year): June 1995
```

### Introduction (context only: never use it for content warnings)

```text
In Adolph’s world, family bonding looks a lot like emotional dodgeball—everyone lobbing sarcasm, guilt, and questionable gifts at each other just to see who flinches first. His mother, a woman powered almost entirely by complaints and cafeteria Jell-O, turns her hospital room into a full-volume comedy special, starring herself and co-starring anyone unlucky enough to wander in. Mom . . . the gift that keeps on giving – may she rest in . . . well, never mind.

Barrel Fever by David Sedaris
```

### Performance text (classify this)

```text
ADOLPH: (Pg 126-150) My mother was in the hospital, recovering from surgery to remove cancerous lymph nodes. The cancer was nothing compared to the punishment she endured from her roommate, Mrs. Gails. The woman never said a word but watched television constantly at top volume.

MOTHER: (loudly, fidgeting with a bracelet on her wrist) You got any questions about the grazing habits of the North American bull moose? I complained to the nurses about the volume but all they do is point to their ears and whisper that she’s got a hearing problem. If she’s got such a hearing problem then why are they whispering about her? She can hear the food cart from down the hall. (perks up and rubs her hands together) I want that woman dead. (changing the subject) Did I tell you that your sister Charity called me? I hardly recognized her voice because it’s been, what, three years since she’s phoned me. It seems she lost her job at the suicide hot line and is looking to borrow some money. I said, “Hold on just a few seconds, darling. It’s a bit difficult to reach my purse with this IV in my arm.”

MOTHER: (on the phone) Did I tell you what your sister Hope sent me for my birthday? A poncho. Who does she think I am that I might want a poncho? I’ve written her back saying I’m sure it will come in very handy the next time I mount my burro for the three-day journey over the mountains to the neighboring village. I’ve thrown it into the garage-sale box along with the pepper grinder Joy sent me. The thing is two feet long, black and shiny – what do I need with a thing like that? It doesn’t take a psychiatrist to recognize the pepper grinder for what it truly is. I bet she spent weeks knocking that one around with her therapist. But that’s Joy for you, thinking she can impress people with the money she makes ‘consulting.’ That’s what she calls herself now, a consultant, as if that means anything. Anyone who answers questions can call themselves a consultant. A telephone operator is a consultant, a palm reader: they’re all consultants. I thought I’d seen it all but then Faith sent me a subscription to that trade paper she’s working for. She calls it a magazine. Why would anyone subscribe to a magazine devoted to adobe? Is this a big trend? I’ve got a house made of bricks but who wants to read about it every month? Adobe? She circled her name on the first page where she’s listed as ‘Features Editor.’ When people ask what she’s up to I always tell them she’s a secretary – it sounds better. So then, a week after my birthday I got a call from your sister Charity . . .

ADOLPH: Faith, Hope, Joy, Charity, and me, Adolph. See, she just couldn’t help herself. *****

ADOLPH: On the afternoon of my last visit, my mother handed me a check for forty thousand dollars and warned me to cash it fast. Mrs. Gails’s television was blaring a rerun of a vile situation comedy in which a pleasant-looking, vapid teenaged boy acts as the game-keeper of four terminally precocious children.

MOTHER: Leave. (pointing to the door) And on your way out I want you to shut off her television. It’ll take the nurses a good twenty minutes to turn it back on. Give me the gift of peace. It’s worth the forty thousand dollars, believe me.

ADOLPH: As I left the room she offered to double the money if I smothered Mrs. Gails.

MOTHER: Use the pillow . . . The pillow. *****

ADOLPH: [And then she died] Three days after the memorial service we met with her lawyer, an energetic woman with very long fingernails painted to resemble American flags. She informed us that my mother’s house, car, and personal possessions were to be sold at their current market value. That money would be added to her life insurance, pension plan, and bank holdings and, according to her will, would be donated to her specified charitable organization, The National Rifle Association.

After the initial shock had worn off, my sisters found themselves [with] plenty more to talk about. I didn’t mention the money (the 40 thousand dollars) . . . like my mother, I may be mean but I’m not stupid.

Shortly after my mother died, my sisters and I found ourselves rummaging through a cabinet of papers marked “POISON,” and it was there, tucked between the pages of a well-worn copy of Mein Kampf, that I discovered fifteen years’ worth of her annual New Year’s resolutions. She took up the practice the same year she bought her first rifle. Every Christmas afternoon, after placing the artificial tree back into its box, she would grow reflective.

MOTHER: Was it wrong of me to spit on that Jehovah’s Witness girl? Tell me the truth here. I need a second opinion.

ADOLPH: On New Year’s Eve she would sit with her notes and a coffee cup of champagne, glancing at her watch and tapping a pencil against the legs of her chair. She would write something on an index card and, moments later, shake her head and erase it. The process was repeated until she wore a hole through the card and was forced to start fresh on another. The next morning I would ask, “So, what was on your list, Mom?”

MOTHER: Smother those homely teenagers who call themselves my children is at the top.

ADOLPH: I always got a great kick out of my mother, but my sisters, for one reason or another, failed to get the joke. They have grown to be humorless and clinically sensitive: the sorts of people who overuse the words “rage” and “empowerment” and constantly ask, “What do you really mean by that?” While I would often call and visit our mother, they kept their distance, limiting their postal or telephone contact to the holidays.

Following her death my sisters were horrified to discover, sealed in boxes, every gift they had given her.

FAITH: How could she not want a first edition by M. Scott Peck?

HOPE: I made these wind chimes with my own two hands. Didn’t that count for anything?

JOY: What did she have against pepper grinders?

ADOLPH: Aside from a few stiff wallets fashioned in summer camp, there was nothing of mine in those boxes as, at an early age, I discovered that postage stamps, cartons of cigarettes, light bulbs, and mail-order steaks are the gifts that keep giving.

“How could she possibly be so cruel?” my sisters asked, coming upon the unmailed notes and letters stored in the “POISON” file.

JOY: (holding a draft of her graduation card) I am not the ‘missing link,’ I am not, I am not. I am not ‘God’s gift to fraternity beer baths,’ I am not, I am not, I am not.

ADOLPH: Charity and Faith gathered round and the three of them embraced in a circle of healing. There were letters to me, but in all honesty it really didn’t bother me too much. We all entertain hateful thoughts every now and then. My mother hadn’t mailed those letters; she simply left them to be discovered after her death. Hey, at least she was thinking about us.

The most shocking discovery in the box marked “POISON” were not her letters, but the stack of New Year’s resolutions she’d spent so long composing. Each of the fifteen cards was dated in the left-hand corner and, in her slanted, childlike writing, each one read the same: “Be good.” It shook me up as, in the three years that I myself have been making such lists, mine say the same thing, relatively. I have taken to softening my approach as a safeguard against failure. The last one reads: “Try to think about maybe being good.” “Try” and “maybe” give me the confidence I need in order to maintain the casual approach best suited to my ever-changing circumstances.

[So here I was looking] at my telephone and [telling] myself that I would (wait) until someone called, at which point I would answer and redirect my life. Whoever they were and whatever they wanted, I would take it as a sign. (beat) The phone didn’t ring until sometime around ten in the evening. It was a woman’s voice and she started in immediately saying. . .

TRUDY: All right now, I realize you probably don’t remember who I am, do you? It’s me, Trudy Chase. I used to be Trudy Cousins. Chase is my married name even though I’m no longer married if that makes any sense! Anyway, I read the obituary on your mother. I know it’s been a while but I just wanted to tell you that I’m very sorry to hear about it.

ADOLPH: I didn’t know how to respond.

TRUDY: You really don’t remember me, do you? It’s me, crazy Trudy who used to sit beside you in Mr. Pope’s senior English class. Remember me? I was the crazy one. I was the one who wrote ‘Don’t follow me – I’m lost too’ on the back of her graduation gown. It’s me, crazy Trudy.

ADOLPH: (to audience) Suddenly I remembered her perfectly. Even at eighteen she struck me as hopeless. (to Trudy) So, Trudy, what’s going on?

TRUDY: Oh, you know me. I’m just as crazy as ever. No, I take that back – I’m probably crazier if you can believe that!

ADOLPH: (to audience) Trudy went on to tell me that she’s lived in Manhattan for three months, having been transferred from the home office in Piedmont. She chuckled, adding that the people here think she’s just about the craziest person they’ve ever met. She’s so crazy that she planned an office party for Lincoln’s birthday and petitioned her boss to free the slaves in the accounting department. And she even wore a tall hat and a fake beard! The members of her tenant’s association thought she should be committed after she hosted the last meeting . . . by candlelight! (to Trudy) Ha, ha. That sounds pretty scary.

TRUDY: Nothing scares me. That’s how crazy I am.

ADOLPH: Nothing?

TRUDY: Not a damned thing. Nada. Othing-nay.

ADOLPH: The very idea that, out of nowhere, a member of my 1975 graduating class would call me and speak pig Latin created a mixed sense of repulsion and endless possibilities.

Trudy spoke of her involvement in any number of organizations. She is, for example, volunteering to walk the dogs of recent stroke victims.

TRUDY: I usually walk with a woman named Marcie, and, Jesus, if you think I’m crazy, you should meet her! We call ourselves the Poop Troop, and next week we’re getting our uniforms. You should join us sometime.

ADOLPH: I pictured myself wearing an “I brake for hydrants” T-shirt and a baseball cap decorated with a synthetic stool.

On top of everything else Trudy also finds the time to play on her company volleyball team, iron for her crazy arthritic neighbor, and teach underprivileged children to make fudge. She didn’t say it in a boastful way. She wasn’t looking for a medal or trying to make me feel selfish. She invited me over to her apartment for a get-together, but I bowed out, claiming I had a business meeting to attend.

TRUDY: Well, if your meetings are half as crazy as mine you’re going to need all the luck you can get,” she said.

ADOLPH: She asked if she could call me after my meeting and I told her to hold a moment as I had another call coming in. She’s been holding for fifteen minutes now and I still can’t make up my mind. I look over at my mother’s card on the refrigerator. BE GOOD. But she never specified: Be good to whom? If I’m good to Trudy Chase, I’ll tell her never to call me again. If I’m good to myself, I’ll wind up making fudge and walking the dogs of stroke victims. Which is worse?
```

---

## IC-2379: Baseball, Boys and Bad Words

- Title: Baseball, Boys and Bad Words
- Author (byline): Andy Andrews
- Work: Not specified
- Publisher: Thomas Nelson
- Publication date as stated: June 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ANDY, MR. SIMPSON, PHILLIP, INTERVIEWER, CHARLES RAYMOND, STEVE, KEVIN, LEE
- Teaser before the introduction: Yes
- Spoken words (computed): 1521
- Already set (do not supply): none

### Source block (context only)

```text
Author: Andy Andrews
ISBN: 978-1404183728
Publisher: Thomas Nelson
Date (Month/Year): June 2013
```

### Introduction (context only: never use it for content warnings)

```text
In 1938, a man named Carl Stotz had the idea for an organized baseball league for the boys in his hometown of Williamsport, Pennsylvania. From those humble beginnings, Little League has become the world’s largest organized youth sports program, creating new opportunities for girls to play baseball and softball, expanding play for teenage players, and initiating new programs to bring baseball and softball to children with physical and intellectual challenges.

In 1970, eleven-year-old Andy Andrews and a group of friends began a Little League season they would never forget. All the usual ingredients were there—well-worn gloves, freshly cut grass, and new uniforms. But the addition of a coach who was “new to the area” made this season truly unforgettable.

Baseball, Boys and Bad Words by Andy Andrews
```

### Performance text (classify this)

```text
ANDY: In a town without a movie theater or fast-food restaurant, life is divided into three distinct seasons: football, basketball, and baseball. Time itself revolves around children, their practices, and games. Most kids played all three sports, but at 11 I didn't weigh enough to play football and measurements for basketball had me at a lofty 4’5”. It was baseball for me and had been for several years.

One could easily pick out the kids from last year's team: Lee Peyton, Steve Krotzer, Phillip Wilson, Charles Raymond Floyd, and, of course, me. We all had on last year's hats. They were off-white with a dark-blue bill and a big “FNB" on the front. We knew that First National Bank, our sponsor, would be giving everyone new hats, but in the meantime, we wanted to be sure that our new coach could tell the veterans from the rookies.

ANDY: None of us had met our new coach. His name was Mr. Simpson. He was, we were told, "new to the area." "New to the area," was a hint that this person was "from the North." Living in the southern part of Alabama, the phrase brought visions of Vikings and pillaging to my mind. I had been told more than once that these people could be nice, but they were different -- articulated with a pause and with eyebrows raised.

Mr. Simpson parked his station wagon and gathered the equipment from the back. We watched him from the backstop as if he were some wild animal at the zoo. We noticed a boy with him -- red hair and more freckles than I had seen on any human since my Aunt Nancy Jane! The boy, we figured, was the coach's son since Mr. Simpson also had red hair and more than his share of freckles.

MR. SIMPSON: Hi, boys. My name is Hankin Simpson, and I'm your new coach. This is my son, Hankin Jr. Boys, I'm new to the area, but I'm sure that it's going to be a great season. Okay? Okay! Now, before we begin to practice, take a rap!

ANDY: We shuffled our feet and looked at each other. What did he want us to do? Take a what? A rap? What was a rap? Hankin Jr. had begun to trot around the field, and figuring that he knew what he was doing, we trotted after him.

PHILLIP: (with an air of superiority) "Rap” is a Northern word. It means “to run.”

ANDY: I wasn't sure whether to believe him or not. Phillip Wilson was what 5-year-olds called a storyteller, what we called a fibber, and what adults called a liar. He could look you right in the eye, tell you a fib, and be so convincing that you never doubted a word he said.

Back at home plate, out of breath from running a rap, we gathered around Mr. Simpson, quite sure that he would now assign positions. We veterans, a virtual sea of FNBs, silently pleading with the man not to look at one of us and say, "Right field."

Since time began, all Little Leaguers have had a fear of right field. In the glamour department, right field ranks dead last. Most batters are right-handed and hit the ball to left field; therefore, a coach who wants to avoid long losing streaks will put his weakest player in "right."

I'd had my brush with this humiliation two years earlier as the weak link for Henley's Hardware Store (green hat, white H). I couldn't catch, but I wasn't stupid. A permanent residence in right field was an embarrassment -- a curse. I was certain that I had been branded for the rest of my life. I could imagine myself as a grown-up going to a job interview and being told:

INTERVIEWER: (with disdain) We're sorry, but there's just no place for you at NASA. We see on your record that you played right field.

MR. SIMPSON: Boys, we're going to be winners this year. I'm excited about this team. Don't worry if you're new to the game. On my team everyone gets to pray."

ANDY: Excuse me? Did he say "pray.”

MR. SIMPSON: I know this is just practice, but I want you to pray your hearts out!

ANDY: This team is in trouble. Either someone had told our new leader that we lost 17 of 23 games last year, or he took one look at us and decided that we were a bunch of rejects. Mr. Simpson had settled on prayer as our only hope.

We practiced hard that first day: dove for grounders, swung for the fence, and generally showed as much hustle as we could muster. We didn't seem to be a vastly improved team from the year before. I blew a sure double play, our new pitcher was throwing the ball over the backstop, and Charles Raymond got hit in the head by a pop fly and cried.

It was at the end of practice, during the compulsory pep talk, when everything became crystal clear.

MR. SIMPSON: There is one thing about this game you can count on. If you don't rearn to watch the basebarr hit the basebarr grove, you wirr never be an excerrent basebarr prayer.

ANDY: We suddenly understood. A rap? Pray hard? He had wanted us to take a lap! He had wanted us to play hard! From the depths of a pep talk to which no one was listening -- like a bolt from the blue -- those weird words all came together and made sense. Coach Simpson could not say his Ls! We could scarcely contain our collective excitement. To a group of 11-year-old boys, nothing beats having a human target at which to laugh. Double the fun if the boys are able to mimic the target, and triple if the unfortunate target happens to be an adult! (characters speak mockingly with uncontrollable laughter during the following section)

CHARLES RAYMOND: I'm a basebarr prayer.

STEVE: No, you ain't. You're a right fierder!

KEVIN: Take a rap! Take a rap!

PHILLIP: Did you hear him call me Phirrip?

LEE: Coach Simpson? I rike him. I rearry do!

ANDY: To this day, Phillip Wilson is "Phirrip" to everyone who played on that team. And no one has forgotten the game that Lee Peyton rounded third, headed for home, and fell down laughing before he got there, because Coach Simpson really did yell, Sride, Ree! Sride! (long beat)

If I had to choose one time during that season to carry with me for the rest of my life, it would be the day Steve Krotzer got kicked off the team. Maybe kicked off is too harsh. Actually, he was transferred to another team, the Sand Dollar Shoes, because the league found out that Steve's family was living in another district. Steve had played with us for four years. He was our friend and a darn good first baseman. We didn't want him to leave. But that last day did arrive. When practice was over, Coach Simpson gathered us around the pitcher's mound.

MR. SIMPSON: Boys, this is a sad day. We're going to miss Steve. He's a fine barr prayer and a fine young man.

ANDY: Steve was close to tears. We were too.

MR. SIMPSON: I don't understand the inner workings of the system. But I do know one thing . . . and rook at me when I say this because it is important. I want every one of you to know that this was not Steve's faurt. (stifled giggling)

ANDY: Did he say what we thought he said? Surely not.

MR. SIMPSON: This was not Steve's faurt.

ANDY: Yes, he did most definitely, absolutely say what we thought he said! Oh sure, we knew what he meant; we'd been unconsciously translating Simpsonisms all year. He was telling us that it wasn't Steve's fault . . . but that wasn't what we were hearing! Of all the words in the world guaranteed to make 11-year-old boys laugh, only one of them is all by itself at the top of the list. And our coach -- an adult -- was saying that word over and over.

MR. SIMPSON: So don't pin the faurt on any one person, because it is just not their faurt!

ANDY: (silent giggling, to the point of tears) I am not exaggerating when I say that we were literally crying. Coach Simpson became concerned. He sounded desperate as he tried to comfort us, but the more he explained that it wasn't our "faurt," the more out of hand things became. (long beat with a smile brought on by the memory)

I haven't seen Coach Simpson in years. Kevin Perkins and Steve Krotzer were in my wedding. Lee Peyton went to medical school and returned to practice in our town. Charles Raymond Floyd was a late bloomer. He was a center fielder in college and played three years of minor league ball. I've totally lost track of Phillip Wilson. The last I heard, he was a used car salesman and perpetually campaigning for mayor in a small town in Louisiana.

I still remember us all as we were that summer. I can close my eyes and hear the explosions of laughter as we react to something that was, to us, the funniest thing in the world.

MR. SIMPSON: I want every one of you to know that this was not Steve's faurt.

ANDY: And I feel a little sad when I think that when we were eleven years old, we may have laughed harder than we ever would again.
```

---

## IC-2380: A Baseball for Dad

- Title: A Baseball for Dad
- Author (byline): Patrick Thomson
- Work: Chicken Soup for the Baseball Fan’s Soul
- Publisher: Health Communications, Inc.
- Publication date as stated: Oct 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1328
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patrick Thomson
Book: Chicken Soup for the Baseball Fan’s Soul
ISBN: 978-1558749658
Publisher: Health Communications, Inc.
Date (Month/Year): Oct 2001
```

### Introduction (context only: never use it for content warnings)

```text
I think THE most important lesson my father ever taught me is a baseball lesson which really is a metaphor for life. “A walk is as good as a hit.” This couldn’t be more true – it doesn’t matter how you get on base, as long as you get on base. Your own statistics are not as important as the team’s. Think of others and not just yourself. Do not be stubborn – be creative. Dad, I heard you loud and clear when I was 6, and I still hear you loud and clear today. No matter what, we will always have baseball. So, thank you Dad…you ARE the reason for my love of baseball. And thank you baseball…you are ONE of the reasons why my father and I had the relationship we did. A Baseball for Dad by Patrick Thomson
```

### Performance text (classify this)

```text
Many hot summers ago, when I was in elementary school in California, I fell in love with an idea, a game, a dream. I fell madly in love with baseball.

I soaked in baseball. I threw, hit, ran, read, felt baseball. I would throw without a ball, hit home runs in my head, be a hero, be a bum. I loved it all.

For a while, baseball was bigger than even my dad. I saw that he had a hero. How could my hero have a hero?

My dad’s hero was Stan the Man. Stan Musial from Donora, Pennsylvania, who played for the St. Louis Cardinals. At the time, St. Louis was the closet major-league team to Los Angeles. All major-league players were heroes in my eyes, but Dad told me that Stan was the greatest of his time.

There were others who could hit the ball harder, run faster, field better or even put on a better show than Stan the Man. But Dad said that Stan was special.

God had given Stan the tools and he used them well. But that was only a small portion of what made him great. He was all the things that my father valued. He was the embodiment of al that life stood for.

I wanted to be like Dad and I felt that Dad wanted to be like Stan Musial. I knew I couldn’t go wrong trying to fit into those shoes.

This particular summer was special because my dad and I were going to the place where my father grew up – St. Louis. Just the two of us. It was hot and humid in what seemed like a foreign land where the people were pale and talked slightly off English.

In California, everything was new. In St. Louis, everything was old. Only the people were young.

Our mission was to meet Stan the Man. I almost didn’t believe it. There was a part of me that didn’t really think that these idols were real people. To me, they only came to life as legend, like Paul Bunyan or Robin Hood. But the closer I came to the meeting, the more obvious it was that Mr. Musial was a real man. Newspapers said so, all my relatives said so, and most important, Dad reassured me.

Through some good fortune, I got a ball autographed by Musial. An injured rookie was at the hospital where my grandmother worked. She told him my story and he got Stan’s autograph on the ball. The ball was living proof that Stan was for real.

That night, the Cardinals were playing the Brooklyn Dodgers and we went. I held onto my ball so tightly that I elicited an inquiry from the guy next to me.

“New ball?” he asked.

“Yep, with an autograph,” I teased him.

“Who?” he prodded.

“The Man, “ I bragged.

“No.”

“Yes.”

“I don’t believe you.”

“Here,” I handed him the ball.

“Wow! I’ll give you $20 for it right now!” Twenty dollars to a ten-year-old boy in 1955 was a pot of gold.

“Nope, let me have it back,” I demanded.

“You’ve got a dream in the form of a baseball,” he said. “Take good care of it!

I shoved it deep into my pocket and resolved that the ball was the most important thing in my life.

The next day was the big day. We would be meeting the Man. As Dad and I walked up the walk to the door, I was in a state of shock. “He’ll be here,” Dad said, knocking.

Sure enough, the door swung open, and there stood Stan the Man in his robe and slippers. My dad introduced himself then me to Stan, and explained that the ball he had signed earlier was for me.

He was just as I had imagined him: sincere, kind, strong. He looked at me in a way that only a few adults look at kids, and we knew that we had a common bond— baseball.

He inquired about my baseball playing. I bragged. Next to Stan, I felt that is was necessary. I thought that I was some great baseball player. He understood.

Getting back to Los Angeles couldn’t happen fast enough. When I told everyone about my experience in St. Louis with Stan Musial, nobody believed me. Such a reality didn’t exist, my friends insisted. I knew that it had happened, though, and that the ball, the meeting, the feeling would always be mine. The older I became, the less I revealed my treasure.

The seasons paraded by. Teams won, players go traded. There were retirements, rookies, home runs, other kids and other idols. My father died. As in life, he wished to carry on in death. His last request was that in his casket there be a deck of cards, a bottle of Jack Daniel’s and, most important, a baseball. He knew that, wherever he was going, he ought not be ill equipped.

On the day he was buried, the whisky and the cards were ready. The last item was a baseball. I decided it should be my twenty-year-old autographed treasure.

Since my father had been responsible for me meeting Stan Musial, I felt it most appropriate that it should be with my dad. I would miss it, but it belonged with him. Some people thought that it was a sacrifice. I did my best to assure them that it was not. The ball was where it belonged.

Spring trainings, long hot Julys and thousands of extra innings later, my sister, Kathie, asked me to stand in for Dad at her wedding. I was flattered. I was honored to give my sister away, to stand in the shoes of my dad.

On the eve of my sister’s big day, we went to an elegant French Restaurant for the rehearsal dinner. As the evening went on, the impact of the occasion seemed to build to an emotional crescendo. The speeches were many. I became aware that something special was happening.

My sister is an airline stewardess and had flown with the Los Angeles Dodgers for part of the 1984 season. After dinner, she thanked my younger brother for his participation in her wedding by giving him a baseball autographed by all of the Dodgers and dedicated to him by Tommy Lasorda.

I was next for a gift.

She told all of us about flying with Lasorda, about how, on the way to spring training, she had told him the story of my Stan Musial baseball.

She said she’d had a difficult time completing the story, stopping again and again to recapture her composure. She said she had been amazed to learn that Tommy Lasorda knew exactly what she meant.

“I’ll get that baseball back for you,” he told her.

Later during the flight, Lasorda told my sister that he, too, had had a magical relationship with his father, and that when his father had been laid to rest, a baseball accompanied him.\

Lasorda told my sister that his life in baseball, his success in baseball and his love of baseball, had all come from his father.

Being a friend of Stan Musial, Lasorda called and told him the story of the baseball. Musial responded with a new autographed baseball and sent it to Lasorda. The ball was then mailed to my sister.

I looked up to see her holding the ball. “I got you another one,” she said, throwing it to me.

I was a child again, coming home. I heard the distant crack of bat on ball and the roar of a crowd. I heard that man sitting next to me in St. Louis in 1955. “New ball?” he asked.

“Yep, with an autograph,” I teased him.

“Who? He prodded.

“The Man,” I bragged.

“No.”

“Yes.”

And then: “You’ve got a dream in the form of a baseball,” he said. “Take good care of it!”

And so I will.
```

---

## IC-2381: Beelzebub is Weeping

- Title: Beelzebub is Weeping
- Author (byline): Robert Haag
- Work: Not specified
- Publisher: VN Productions
- Publication date as stated: Sept/Oct 2000
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1511
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Haag
Book/Magazine: Vision? Nary! Magazine
http://vision-nary.com/
ISBN: N/A (independently published)
Publisher: VN Productions
Date(Month/Year): Sept/Oct 2000
NFL CAUTIONARY NOTE
• Vision? Nary! Magazine published by VN
Productions was originally both a 24 page hard-
copy printed magazine and an e-zine.
• It was printed in hard-copy form quarterly and
the e-zine updated after each hard-copy
magazine was distributed.
• The editor of the magazine is David Raffin, and
subscriptions were sold for $8.00 for 4 issues.
• It does appear that VN Productions was the
personal business of Mr. Raffin and no ASIN
or ISBN number was issued for this
publication.
• At some point, Mr. Raffin decided to stop
printing the hard copy version of this magazine
and convert to a completely digital distribution
format.
• To obtain a copy of this issue in it’s hard-copy
form, contact David Raffin at david@vision-
nary.com – The charge for this issue is $2.00
and must be paid via PayPal.
```

### Introduction (context only: never use it for content warnings)

```text
This is the story of how I came to dwell in the region of space and time known as Hell; did that rhyme? Oh well, it doesn't matter. My name is... or more specifically was- William Michael Smith Jr. People tended to call me Billy as not to confuse me with my father- him being William Michael Smith Sr. in case you hadn't guessed. Anyway, as I said I'm in Hell. Oh don't worry; I'm not selling or buying anything, I just wanted to tell you how I got here. I figured it would help pass the time (of course time is fairly irrelevant in Eternity, but do me a favor and humor me). Beelzebub is Weeping by Robert Haag
```

### Performance text (classify this)

```text
Just to allay another fear you may be having: No, I'm not going to be one of those lost souls who claim that they don't belong Here. Very few people are more deserving of this fate than I am. The list of things I did to get here is as long as your arm. If I went into the details I'm sure that I'd probably lose your interest and that's not why I'm here.

This is the story of the very first atrocity that I'd ever committed. I was twelve years old and it involved the one and only Santa Claus...

It was about a week before Christmas, my aunt and uncle were staying with us for the Holidays and had brought my cousins with them.

Katie was eleven, I can still remember when I was about six and she and I did the old "you show me yours and I'll show you mine" game, afterwards she went running through the house informing the family about the intimate details of my genitals. She wasn't allowed to come back for about a year.

Jim was nine, he was okay, except that he had this habit of humming the theme song to "The A-Team," after about an hour just about anyone would be driven to do bodily harm to the kid. Heck, one time dad had to restrain grandma when she tried to push him down a flight of stairs.

On my side of the family there was my older brother Joey, I think he was a little jealous about me being named after dad and not him. I guess he figured that since he was the first born he should be the "Junior" of the family.

Anyway, he was sixteen and felt that since he was the only teenager of the group that he was too important for the rest of us. He spent most of his time sitting in a corner listening to his headphones.

The youngest member of the family was five year old Ricky. Out of all of us, he was the only one who still believed in Santa Claus. The rest of us just considered him to be some myth made up by business executives as an excuse to sell toys to the mass markets.

Strangely enough it turned out that Ricky was right. Santa did exist; unfortunately for Santa, I existed too.

It was 11:30 or so on Christmas Eve when it all started. Katie and I were up watching television in the front room when we heard a loud noise that seemed to be coming from the roof.

"Strange," said Katie. "It almost sounds like the hooves of twelve tiny reindeer pulling along a toy-laden sled."

I looked at her for a moment and then said, "Oh, shut the hell up! It's probably just a burglar or ax murderer or something."

"Cool!" She said, "do you think we should wake up our parents?"

"Nah, they'll just think that we're making it up. Let's go get Joey."

Now, Joey never liked people coming into his room; he said that it was an invasion of his privacy. Of course that never stopped me.

We ran up to Joey's room and barged in, it was apparent that he was in the midst of a, let us say, enjoyable dream. We could tell by the pup tent in his sheets. Not to go into the gory details but suffice it to say that he wasn't too thrilled with being woken up.

It took us a couple of minutes to convince him that we weren't making the story up, and he agreed to go down with us to check the noises out.

On our way downstairs both Ricky and Jim came out of their room to see what was going on. After we told them Ricky said, "Oh boy! Santa Claus!"

None of us were in the mood to contradict him. When we got down to the fireplace we could here the noise of someone trying to climb down the damn thing.

"I bet it's a crook," said Joey, "He's trying to make us think he's Santa Claus."

"Let's teach him a lesson," said Katie. "We need to show this bastard what happens to people who attempt to degrade cherished childhood icons!"

"Oh, shut the hell up!" I said.

We quickly spread out and hid behind furniture. Within a couple of moments we caught our first glimpse of our intruder.

This guy was good. He was decked out in the whole traditional Santa garb: red coat, white trim, beard, the whole nine yards.

Once he was completely out of the chimney he proceeded to look around as if casing the joint; from the looks of the bag he was carrying it was apparent that he'd hit a few other places along the way.

The phony Santa's eyes came to rest on the Christmas tree, he smiled and nodded and the made his way towards the presents.

He didn't get two steps before Katie whacked him in the back of the legs with the fireplace poker.

"Holy Shit!" he yelled as he went crashing to the floor.

"Get Him!" I yelled. Within mere moments everyone was out from behind their hiding places kicking, punching, and biting the guy. Well everyone, that is, but Ricky.

"Stop! Don't hurt him, He's just here to give us presents!!!" Ricky yelled.

"Oh get off it Ricky, this isn't really Santa Claus! Santa Claus doesn't really exist!!" I yelled.

"Yes I do!" screamed the fat guy.

"Oh shut the hell up!" I said and then kicked him in the teeth.

"If you are Santa, then what's my name?" asked Jim.

"Uh, well...you see I don't know every child by name anymore. I used to, but with the recent population explosion of the last century it's just downright impossible to keep track." He said.

"You mean you don't know my name?" asked Ricky in a cracking voice that I recognized as his "I'm about to burst out crying" voice.

"Uh, well, you see...I...uh..." the Santa wannabe stammered.

"Oh shut the hell up!" screamed Ricky as he kicked the old fart in the teeth.

He then looked at me and said, "Katie was right. let's teach this son-of-a-bitch a lesson!"

I was so proud, I thought that I was going to cry. I won't bore you with the unsettling details, but over a three hour period we taped his mouth shut, stripped him naked, bound his arms and legs, and then proceeded to go to work.

Ricky took to whapping the fat man's genitalia with the fireplace poker, the whole time muttering under his breath.

Katie and I were enjoying ourselves by pulling out "Santa's" toe nails with a pair of pliers that was freshly liberated from under the tree: my gift to Dad.

Jim was sticking small pieces of wood underneath the old man's fingernails.

Joey just sat back and taped the whole thing with a video camera that he'd found in the bag the guy was carrying.

Oddly enough, during the whole torture process neither my parents, or Katie's, were awoken my the moans of intense pain that our victim was making. Heavy sleepers I guess.

Well, after a while the novelty of the whole thing began to wear off and we weren't exactly sure what to do with him. Ricky suggested several times over that we burn him alive (never mess with a kids beliefs).

Luckily we didn't have to make any decisions, because at that time an elf came scurrying down the chimney. At first we thought that it was one of the fat guy's accomplices, but on close examination we were convinced that the pointed ears he was sporting were, in fact, real.

I must say that we were all a little embarrassed about the situation, but the elf quickly put our concerns to rest.

"This happens about once a year, it started in the 1960's. We keep telling the big guy that it's time to retire, but he keeps on trying. This might be the last straw for him. You kid's worked him over real good," he said with an evil little smile.

It took a while, but Santa was airlifted out on a special medical sled. He kept referring to us as "those little bastards." The elves told us that that was what he usually called them.

Anyway, once they were gone we all went off to bed. When we woke up later on in the morning our parents were confused about the way we were acting.

"If you guys don't shape up, there's a chance that Santa might pass you kids over next Christmas," said my dad.

"Oh, I got a feeling he'll be doing that anyway," said Ricky with a smile.

Well, that's my story. I know that doesn't completely explain what I'm doing down Here, but it's a start. I might get to the rest at some later date.

I'm afraid that I have to go now, it's my turn to give Satan his foot massage.
```

---

## IC-2382: A Bell for Shorty

- Title: A Bell for Shorty
- Author (byline): Jim May
- Work: The Farm on Nippersink Creek
- Publisher: August House
- Publication date as stated: March 1995
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1749
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jim May
Book: The Farm on Nippersink Creek
ISBN: 978-0874833393
Publisher: August House
Date (Month/Year): March 1995
```

### Introduction (context only: never use it for content warnings)

```text
Jim May was born in Spring Grove, Illinois. Raised in this small German-Catholic farming community, his stories resonate with the rural voices of the Illinois prairie. His relatives spent time “visiting” and telling stories as an integral part of daily life–a means of weaving the social fabric of the community.

As an Emmy award-winning storyteller and author, he seeks to reestablish storytelling as an art form, ideal not only for entertainment and education, but also for the grounding and healing that is needed in complex, modern times.

This story pays tribute to the most influential man in his life – his father “Shorty.” A Bell for Shorty by Jim May
```

### Performance text (classify this)

```text
(Pg 189) My father's nickname was Shorty. He wasn't particularly short, but he was the second son born to a farm family of twelve children, and when his oldest brother, my uncle Ben, gave him the nickname, it stuck. As I grew up, it never occurred to me that his nickname had anything to do with his height. It was simply what most people called my father. Our family called him Dad.

My father was fifty-one years old when I was born.

The best thing about being the youngest was the year I had my father all to myself. I was five years old, and there was no kindergarten at the one-room school I would attend the following fall. My oldest sister was married and my other two sisters were in high school. My brother was working construction, and my mother assembled typewriters at a factory in Woodstock. Each day, after an enormous farm breakfast of bacon, sausage, fried potatoes, eggs, pancakes, and German coffeecake, everyone scattered to their destinations in town, leaving Dad and me, the oldest and the youngest, at home to be the real farmers.

I went along to work in the fields, too. I remember sitting with Dad high up on the iron seat of the old tractor, the big seat with the holes drilled in it for the rainwater to drain through. There was plenty of room for both of us on that wide, flat, piece of iron. I sat half in his lap, surrounded by his arms as he held the steering wheel. Sometimes I'd grab the wheel and "help" him steer.

In those days, even though I was five years old, I never thought of myself as being "babysat." I was the official "hooker-upper" on the place, and could drive a tractor, in a manner of speaking. In late summer the corn stood tall in the fields but was still green and juicy. We'd hook up a hay wagon to the tractor. I'd lift the wagon tongue (most were four-wheeled in those days, so there was no weight on the tongue) while Dad backed the tractor toward me. When the coupling hole in the tractor's drawbar matched the hole in the wagon tongue, I'd drop a pin through both holes, joining the wagon and tractor. I was proud of this contribution because I knew that it would have been nearly impossible for my dad to do that job alone. Next we'd pull the wagon down to the cornfield, cut and load some corn, and feed it to the cows when they came up to the barn for milking.

My job was to "drive" the tractor while Dad cut the corn. Once we reached the cornfield, he'd put the tractor in first gear and hold the clutch pedal to the floor. Then I'd put my small work shoe on top of his heavy work boot, and while the tractor continued to run he would slowly slide his foot out from under mine. I could feel the tension of the clutch pedal rising against my foot and as I pushed back with all my weight, the pedal would slowly depress again. At that moment I took control of the big machine.

I was pleased that I had saved him a lot of time and effort walking back and forth to the wagon and climbing on and off the tractor to move it closer to his work. He was nearly sixty years old and farming three hundred acres by himself; even then I was aware of his age and how hard he worked.

There were times when I couldn't go along with him, times when I had to stay alone back at the house. There was the time that I rang the bell.

I watched Dad milk and feed the cows, helped him hook up the corn planter, and looked on as he filled first the canisters that held the fertilizer and then the ones that contained the corn seed itself. When he was finished and had tightened the last wing nut on the last bolt, he looked at me, thought for a moment, and said as he turned toward the tractor, "You'll have to stay home today."

I didn't understand why. It seemed like a horrible injustice. Looking back, I think he may have been afraid to have me sitting with him on the tractor seat that day. There was a lot of moving around when you planted corn. We used an ancient two-row planter that had been converted from horse-drawn to mechanical. A man sitting on the tractor had to reach around and back to put the planter in gear by hand. The marker arms had to be lifted and dropped again at the end of every pass so that each row of corn was properly spaced for future cultivating and harvesting. With all that movement, a small boy could easily be bumped and fall under the tractor wheel. Farming is dangerous work. Every farmer knew a friend or relative who had lost a hand or an arm to a machine. Local accounts of some child crushed under the wheel of a tractor or truck served as moral lessons and cautionary tales.

Before he got on the tractor. Dad turned to me and said, "I know you'll be alone, so if there's trouble, ring the bell."

A rusty, cinnamon-colored bell hung from a wooden frame on the roof of a storage shed we called the shanty. The shanty was attached to the house. I had never heard the bell.

"It's not for fun or foolishness, but if there's trouble, ring the bell. I'll hear it in the field and come back in on the tractor."

He left for the field. I watched the tractor roll down the lane, getting smaller and smaller. Finally it was out of sight. I didn't like being there alone. I was afraid someone might come down the driveway. It wasn't just strangers that scared me. I was just plain shy, frightened even of neighbors.

The time was passing ever so slowly, so I thought I'd go into the shanty to play.

When my eyes had adjusted to the darkness, I saw our dog, Bootsie, asleep in a dirt hole. Curled up next to her was a snake. This snake looked threatening, and I had overheard some talk about rattlesnakes on neighbors' farms. Recalling my father's words, I thought to myself. This could be trouble. I looked up at the bell. I liked the idea of ringing it. I liked the idea of Dad coming in early from the field. I knew he'd be coming in for the noon meal, which we called dinner, but it was still mid-morning and I didn't want to wait. I looked at the snake again and it seemed to have gotten bigger, with a more sinister look on its face. I thought. This is trouble enough.

I grabbed the old hemp rope and gave it a pull that literally lifted my feet off the ground. When the side of the rusty bell hit the clapper, it sent a low, rich toll out over the fields. I liked the sound so much that I gave it another pull.

When the toll had drifted away, I heard something else: the engine of my father's tractor. He had heard the bell and was coming in from the field.

When I saw his tractor belching smoke and coming into the yard at full speed, I knew that he was worried about me and I thought, Maybe I am in trouble!

The tractor braked, coming to a stop right in front of me. He turned the engine off and it got real quiet, the kind of stillness only noticed after it has been preceded by a loud noise. "What's the trouble?" he asked, still seated on the tractor.

"There's a snake over there by Bootsie!" I replied, pointing to the shanty. He climbed down off the tractor and walked quickly to the old building, taking big steps. I followed behind him, running. It turned out to be a garter snake, about eight inches long and disappointingly harmless. He let go with a big sigh like he was relieved that I was safe and sound. Then he got mad.

"I've got a lot of planting to do today. I can't be coming back in unless it's more trouble than that!" He turned toward the house, walking past me, muttering. That was the last he said about the incident and I never rang the bell again.

The following year, on the first of March, we auctioned the farming business and moved to town. Dad said it was because of the price of milk and the recession. I think the work was getting too hard for him.

He got a job working in a milk machine factory in town. It must have been hard on him working inside after all those years of farming, but he never said too much about it. The second spring in town, he was laid off from the factory and was hired to work on a Lipizzan horse farm. This was a blessing because he loved horses.

One day while I was at school, he was leading a big stallion across a hayfield to a new barn when the big horse bolted. The stud horse threw its head, jerking on the leather lead that Dad was holding. I remember him saying, "If I would have let go, I would have been all right." Instead he'd held on and fought the horse. Maybe he'd remembered his younger days, cowboying those raw, young draft horses that he had trained to behave and work at a farmer's side. But Dad was old now, and the strain was too much. He had a heart attack and died a short time later. I was sixteen.

In the years that followed, there were times in my life when there was trouble, and I ached to pull on the rope, but I didn't have a bell to ring and he didn't have a tractor to drive in from the field.

This story has been silent for years, like the old bell. But now when I tell it, it feels to me like I'm pulling on the rope. And if you hear that bell, or maybe a bell of your own, then I know I've rung it. Shorty May taught me to listen to the land and to its people, and sometimes while searching my memories, I can hear the tractor coming, too.
```

---

## IC-2383: Big Fish: A Novel of Mythical Proportions

- Title: Big Fish: A Novel of Mythical Proportions
- Author (byline): Daniel Wallace
- Work: Not specified
- Publisher: Penguin Publishers
- Publication date as stated: Nov 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: DAD, DR. BENNETT, SON
- Teaser before the introduction: Yes
- Spoken words (computed): 2408
- Already set (do not supply): none

### Source block (context only)

```text
Author: Daniel Wallace
ISBN: 978-0140282771
Publisher: Penguin Publishers
Date (Month/Year): Nov 1999
```

### Introduction (context only: never use it for content warnings)

```text
In Big Fish, William Bloom has never really known his father, a charming, globe-trotting salesman with a joke for every occasion. Now Edward Bloom, dying, comes home to Alabama, and his son hopes for a connection, before he dies. This selection is the final chapter in Edward Bloom’s mythical life. “Mythical” I say because William has created a life for his father from his own imagination – a life of mythical proportions. Is the story of Edward’s death true, though difficult to believe, or is it the final chapter of a life so incredible that one MUST believe? I’ll leave that to you to decide.

My Father’s Death: Take 4 from Big Fish by Daniel Wallace.
```

### Performance text (classify this)

```text
(My Father's Death: Take 4) One of our last car trips, near the end of my father's life as a man, we stopped by a river. After a couple of minutes my father took off his shoes and his socks and placed his feet in the clear-running water. Then he closed his eyes and smiled.

DAD: This reminds me . . . . And then he stopped and thought some more. I guessed he was thinking of some joke to tell, because he always had some joke to tell. Or he might tell me a story that would celebrate his adventurous and heroic life. Does it remind him of the duck in the hardware store? The horse in the bar? The boy who was knee-high to a grasshopper? Did it remind him of the dinosaur egg he found one day, then lost, or the country he once ruled for the better part of a week?

DAD: This reminds me of when I was a boy.

I looked at this old man, my old man with his old white feet in this clear-running stream, and I thought of him suddenly, and simply, as a boy. I'd never done that before. And these images--the now and then of my father-- converged, and at that moment he turned into a weird creature, wild, concurrently young and old, dying and newborn . . My father became a myth.

My father was dying. Sheltered inside an oxygen tent at Jefferson Memorial Hospital, his small, emaciated body seemed bleak and translucent, a kind of ghost already.

The doctors were all very grave, even hopeless. Dr. Bennett, our old family doctor, synthesized the details of ongoing reports; he would give us the Big Picture. Dr. Bennett had an old, tired face. The rings beneath his eyes were like dark brown ruts in a road. He had been our doctor for years. But he was a good doctor, and we trusted him.

DR. BENNETT: Mr. Bloom may not make it out of this one. There are a couple of things we want to try—we’re not giving up, not by a long shot. But I’ve seen this sort of thing before. It’s sad, I—I’ve known Edward Bloom for a quarter of a century. I don’t feel like his doctor anymore. I feel like a friend, you know? A friend who wishes he could do something. But without the machines . . . ” (Shakes head sadly) I turned and wandered away while he continued to talk to my mother. I went to my father’s room and sat in the chair beside his bed. I sat there and waited—for what I don’t know—and stared at those marvelous machines. This wasn’t life, of course. This was life support. This was what the medical world had fashioned to take the place of Purgatory. I could see how many breaths he was taking by looking at a monitor. I could see what his frenetic heart was up to. And there were a couple of wavy lines and numbers I wasn’t sure about at all, but I kept an eye on them as well. In fact, after a while it was the machines I was looking at, not my father at all. They had become him. They were telling me his story. Which reminds me of this joke. I’ll always remember his jokes, but this one especially I will remember. It’s a family heirloom. It’s one I tell myself still, out loud and alone, the way he told it to me, I say, There’s this man. There’s this man, and he’s a poor man but he needs a new suit. This man needs a new suit, but he can’t afford to buy one, he can’t afford to buy one until he passes a store where there’s this suit on sale, and it’s priced just right, this beautiful dark blue suit with pinstripes—and so he buys it. Just like that he buys it and wears it right out of the store with a matching tie and everything, but the joke here is— and I guess I should’ve mentioned this earlier—the joke is it doesn’t fit. This suit doesn’t fit him at all. It’s simply way too big. But it’s his suit, right? It’s his suit. So to make it look good he has to place an elbow against his side like this, and his other arm out sort of like this, and he has to walk without moving one of his legs so that the cuffs will appear even, this tiny man in this huge suit—which, as I said, he walks out wearing, walks out into the street wearing. And he thinks to himself, What a nice suit I have! and walks with his arms just so—my father would make his arms just so— and dragging one leg behind with this smile on his face like an idiot because of this great buy he’s just made—a suit! on sale!—when he passes two old women on the avenue there. They watch him pass, and one of them shakes her head and says to the other, “What a poor, poor man!” And the other woman says, “Yes—but what a nice suit!” Which is the end of this joke. But I can’t tell it like my father did. I can’t drag my leg the way he did it, and so even though this is the funniest joke I have ever heard in my life, I don’t laugh. I can’t. Even when the lady says “Yes—but what a nice suit!” I’m not laughing. I’m not laughing at all. I’m doing the other thing. I suppose this is what roused him, brought him back to the world for a bit, thinking that if there was anytime I needed a joke, now was the time. God, he really cracked me up.

DAD: Some water. Get me some water. Some water, he says! Oh and it’s his voice all right, it’s his voice, deep and booming, caring and gentle. And I get him some water, and he calls me over, to his bed, his only son, me, his only child, and he pats a place on the edge of the bed where I’m to sit, right? So I sit. There’s no time for hellos and how are yous and we both know it. And he says, after taking a sip of water from the little plastic cup, “Son,” he says, “I’m worried.” And he says it in this real shaky voice so I know, don’t ask me how but I know that, machines or not, this will be the last time I ever see him alive. Tomorrow, he’ll be dead.

SON: What is it you’re worried about, Dad? The hereafter?

DAD: No, dummy. I’m worried about you. You’re an idiot. You couldn’t get yourself arrested without me along to help. But I don’t take it personal: he’s trying to be funny. He’s trying to be funny and this is the best he can do! Now I know he’s a goner.

SON: Don’t worry about me, Dad. I’ll be okay. I’ll be fine.

DAD: I’m a father, I can’t help it. A father worries. I am a father and as a father I’ve tried to teach you a thing or two. I really did try. Maybe I wasn’t around so much, but when I was, I tried to teach. So what I want to know is—you think I did a good job? (Beat) Wait! Don’t answer that!

(trying to smile, but it doesn’t quite work) Oh, go on, then. Just tell me before I die. Tell me what it is I’ve taught you. Tell me everything it is I’ve taught you about life so I can go ahead and die and so I won’t have to worry so much. Just . . . just go ahead and say it. I look into his gray-blue dying eyes. We’re staring at each other, showing each other our last looks, the faces we’ll take with us into eternity, and I’m thinking how I wish I knew him better, how I wish we’d had a life together, wishing my father wasn’t such a complete and utter mystery to me, and I say, “There’s this man,” I say. “There’s this man, and he’s a poor man, but he needs a suit, and—” And he smiled. Then he cast his gaze around the room, and he winked at me. He winked!

DAD: (in a hoarse whisper) Let’s get out of here.

SON: Out of here? Dad, you’re in no condition . . .

DAD: There’s a fold-up wheelchair in the bathroom. Wrap a blanket around me. As soon as we get off this hall, we’ll be in the clear. But we don’t have much time. Hurry, son! I did as he asked, I don’t know why. I wrapped him with a pale brown blanket, covering his head like a monk’s habit. I lifted him, with a disturbing ease, from his bed and into the chair. I had no gotten no stronger in the last few months, but he had become considerably smaller. I opened the door to his room and peeked out into the hallway. I saw Mom at the nurse’s desk with Dr. Bennett, wiping her eyes with a tissue and nodding. I pushed my father in the opposite direction. I dared not even look behind me to see if they had spied us. I just pushed him fast, hoping for the best, and when we came to a corner went around it. Only then did I allow myself a backward view. Nobody. So far, so good.

SON: (Breathlessly) So. Where are we going?”

DAD: The elevators. The elevator to the lobby to wherever you parked your car. Take me there. Now. We don’t have much time.

The elevator came and I pushed him on. The door closed behind us, and when they opened again I wheeled him out of there with a daredevil’s panache, past a host of doctors in green and white, past nurses holding charts giving me sidelong glances. Everybody in the lobby paused and stared at us, knowing this wasn’t right somehow, but by then I was traveling at such speed that no one had the time to think to stop us. They simply looked at us as though they had seen something odd—and they had, too, odder than they knew. And then we were gone.

DAD: Good job. Still need to hurry, though, Will. I need some water. I need some water bad.

SON: I have some in the car -- A thermos full.

DAD: (laughing) More than that.
When we got to the car I lifted him out of the
wheelchair and placed him in the front seat. I folded the
wheelchair and threw it in the back.

DAD: We won’t be needing that. (laughing) Not where we’re going. But he didn’t tell me where we were going, not at first. I simply drove away from everything I knew: the hospital, his old office, home.

DAD: That water, William?” It was beside me on the seat. I opened the top and passed it to him. One shaky, scaly hand appeared from beneath the folds and took it from me. But instead of drinking it, he poured it all over himself. The blanket was soaked.

DAD: Ahh . . . That’s the ticket. Still, he didn’t take the blanket off.

DAD: Go north on Highway 1. There’s a place there. There’s a river. A place by the river. I took the car down a series of streets, through the city and the surrounding suburbs, where the sun was rising over the roofs and treetops, until finally we broke into the deep, green, beautiful country.

SON: How far now?

DAD: Just a couple more miles, I think. I hope. I don’t feel so good.

SON: What’s there? But for an answer all I got was a shivering inside the damp blanket, and a gurgling, groaning sound, as if he were in deep pain.

SON: Are you okay?

DAD: Been better. I feel like that guy . . . Who walks into the bar with a frog on his head, with a bird on his shoulder, with a kangaroo at his side and the bartender says, “Hey, we don’t get that many kangaroos in here,” and the kangaroo says, “Yeah, and at these prices you’re not likely to get many more!” And then he said, suddenly almost yelling,

DAD: Here! And I pulled off the road. There was your old oak tree with the roots spreading out through the dark and mossy soil. And there was your river, running clear the way you didn’t think rivers ran anymore, moving fast around stones the size of a small car, making little rapids, running as clear as the air, as blue as the sky, as white as a cloud. I don’t know how he saw it from beneath the blanket. “Carry me,” he said, or so it sounded, his voice so weak now I was doing my share of interpreting as I listened. He said, Carry me and You don’t know how I appreciate what you’re doing and When you see your mother, tell her—tell her I said good-bye. And so I carried him out of the car and down the mossy bank to the river and stood there before it, holding my father in my arms. And I knew what I was supposed to do then but I couldn’t do it. I just stood there, holding his body shrouded in a blanket on the banks of this river, until he told me, You might want to look away now and then Please, and all of a sudden my arms were full of the most fantastic life, frenetic, impossible to hold on to even if I’d wanted to, and I wanted to. But then all I was holding was the blanket, because my father had jumped into the river. And that’s when I discovered that my father hadn’t been dying after all. He was just changing, transforming himself into something new and different to carry his life forward in. All this time, my father was becoming a fish. I saw him dart this way and that, a silvery, brilliant, shining life, and disappear into the darkness of the deep water where the big fish go, and I haven’t seen him since— though others have. Already I’ve heard stories, of lives saved and wishes granted, of children carried for miles on his back, of anglers mischievously dumped from their vessels and emptied into various oceans and streams from Beaufort to Hyannis by the biggest fish they’ve ever seen, and they tell their stories to anybody who will listen. But no one believes them. No one believes a word.
```

---

## IC-2384: The Big Woods

- Title: The Big Woods
- Author (byline): Patrick F. McManus
- Work: How I Got This Way
- Publisher: Henry Holt & Company
- Publication date as stated: Oct 1995
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2285
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patrick F. McManus
Book: How I Got This Way
ISBN: 978-0805034813
Publisher: Henry Holt & Company
Date (Month/Year): Oct 1995
```

### Introduction (context only: never use it for content warnings)

```text
The Big Woods by Patrick F. McManus
```

### Performance text (classify this)

```text
Crazy Eddie Muldoon and I had hit a dead spot in an otherwise interesting summer, mostly because Eddie’s parents had confined him to his own yard for two weeks. This was shortly after Eddie’s father, Mr. Muldoon, had fallen into a pit we had dug for the purpose of trapping wild animals, which we intended to tame and then train to do tricks. Eddie had even found an old chair and made a whip out of a stick and a length of clothesline. Those were the main things you needed to train wild animals, a chair and a whip. Eddie planned to charge people to see the animals perform. It was a good idea and probably would have made Eddie and me some money, but then Eddie’s father fell in the pit and ruined everything. Mr. Muldoon wasn’t hurt one bit, and neither was the skunk, the only wild animal in the trap at the time, not counting Mr. Muldoon. From all the fuss, a person would have thought we had dug the trap just for Eddie’s father. It was the wild animal trap that got Eddie confined to his yard. After the first week, I was allowed in to play with him, and it was a good thing, too. Eddie was about ready to go yard-crazy.

“How’s it going?” I asked

“Terrible,” he said. “The guards are real mean to me, particularly the one that smells like skunk.”

“What do they feed you?”

“Just bread and water. But I’ve set some snares around the yard to see if I can catch something for supper. Look, a wild pig!” He pointed to a Muldoon chicken approaching one of his snares. The chicken stepped into the snare and pecked at some crumbs Eddie had left on the ground, then wandered off without tripping the snare. Eddie was furious. He took great pride in his snares, even though he had never caught anything with one of them. “Stupid chicken!” he yelled.

About then one of the guards appeared at the door and said lunch was ready. Eddie and I went in. The guard had placed bowls of soup and a platter of ham sandwiches and a pitcher of lemonade on the table. “Usually, it’s just bread and water,” Eddie explained as we washed our hands. “The guard didn’t want the outside would to know how mean they are to me.”

“Go tell your father lunch is ready,” the guard said to Eddie.

Eddie sniffed the air. “he’s coming now,”

And at that moment Mr. Muldoon stepped on the porch and opened the screen door. He looked at me. “Aha, the other wild-animal tamer,” he growled.

“Now, Herbert,” Mrs. Muldoon said. “Don’t get all fussed up again. The boys just let their imaginations run away from them from time to time.”

“Only kidding,” Mr. Muldoon said. “But it wouldn’t hurt if they penned up their imaginations for the rest of the summer. Eddie must get his imagination from your side of the family. I’ve never imagined anything in my life. Boys have got to learn to live in the real world.

Take life like it is, and no complaints. You ever hear me complain? Never!”

“That’s good, Herbert, because I have a little job for you. I need some dewberries for jam, and I want you to take the boys out in the woods and pick me a couple of gallons.”

Mr. Muldoon started to complain.

“Hooray!” Eddie and I shouted in unison. “You mean the Big Woods, Ma?” Eddie cried.

Mr. Muldoon went on complaining.

“Yes, dear, the Big Woods.”

Mr. Muldoon complained even more fiercely. It was hard to believe this was his first time, he did it so well.

“Great!” Eddie yelled. “Maybe we’ll even get lost out in the Big Woods and have to build snares to survive. Pat and I will go get the berry buckets out of the garage.”

As soon as Mr. Muldoon had finished his lunch, Eddie and I raced across the highway toward the Big Woods, with Mr. Muldoon plodding along behind. Mrs.

Muldoon stood in the doorway and watched our departure. “You keep a close eye on the boys, Herbert,” she called after us. “It would be easy for them to wander off and get lost.”

Mr. Muldoon chortled evily.

Eddie and I had named the Big Woods ourselves. There were lots of little woods around that we were allowed to play in, but the Big Woods went on forever. They spread out across the valley, over the foothills, and then climbed the mountains. I was a little concerned about getting lost in the Big Woods, because I didn’t have that much faith in Eddie’s snares as a means of providing sustenance.

Eddie and I raced along a trail overgrown with ferns taller than ourselves. “Hold up, you rascals!” Mr. Muldoon shouted. “I ain’t wearing tennis shoes, like you. Even if a bear was chasin’ me, all I could do is walk a little faster.” Eddie’s father actually grinned at us. He seemed to be enjoying the hike through the woods, even in his big old clod-hopper boots. They probably weighed five pounds each.

Eddie and I enjoyed the hike, too. The woods were cool and moist and full of a thousand shades of green, with thick blankets of moss covering long-dead fallen trees. Shafts of sunlight slanted through the towering firs and pines and cedars, making bright green blotches in the shadowy woods. Out there in the shadows, perhaps even watching us, were deer and elk and cougars and bears and --!

“Bear!” screamed Crazy Eddie. He pointed into the woods. And there it was! Eight feet tall, mean red eyes glaring from its black hairy head, the fanged mouth twisted back in a horrible snarl!

For a brief moment, Mr. Muldoon seemed almost as startled as I. “That’s only a black stump, Eddie,” he explained crossly. He picked his hat up off the trail and put it back on his head. “What did I tell you about that imagination of yours! Stop letting it run wild!”

I couldn’t believe Eddie had actually mistaken the stump for a bear, and told him so. Anyone could see it was just a stupid old black stump.

The woods became less enjoyable after our encounter with the stump. “It could have been a bear,” Eddie said. Both he and I now looked for other signs of bear in the shadows. We dropped back and followed close behind Mr. Muldoon, who from time to time turned his head casually to peer off to the left and then to the right, probably to check for landmarks. The woods had grown darker and were full of rustling and cracking and creaking sounds we hadn’t noticed before.

“How come your mom just doesn’t make raspberry jam?” I said to Eddie. “Raspberry jam is good.”

“I don’t know,” Eddie said nervously. “I think raspberry jam would be plenty good enough, don’t you, Pa?”

“We come to pic dewberries and we are going to pick dewberries,” Mr. Muldoon grumbled. “Bears or no bears.”

A few minutes later, the woods thinned and faded away tree by tree, and all at once we were in a big bright clearing, larger than the Muldoons’ cow pasture. Dewberry vines were everywhere, climbing over ancient brush piles and gray stumps, the vines heavy with black juicy fruit.

“Wow!” Crazy Eddie said. “Look at all the dewberries! Did you know this clearing was here, Pa?”

“Of course I knew it was here,” Mr. Muldoon said, smiling. “Did you think I was leading you on a wild-goose chase?”

We went to picking dewberries with a frenzy, stopping only occasionally to gobble handfuls of the sweet, juicy fruit. Eddie and I both exchanged the opinion that dewberries made much better jam than raspberry. As we exhausted each trove of berries, we moved deeper into the clearing, or buckets growing ever heavier. Then Eddie and I spotted a pile of stones black with berries. We raced each other to get to it first. The pile of stones turned out to be the remains of a fireplace. Hidden beneath the grass was the stone foundation of a cabin.

Some distance off were the remains of another fireplace. And beyond that another. And sill another. Gray, weathered boards and cedar shakes were scattered about on the ground. Near one of the cabin sites was a patch of wild roses and a gnarled fruit tree.

“Hey, Pa,” Eddie called out. “Somebody used to live here. This was once a little town.”

Mr. Muldoon straightened up from a tangle of berry vines and rubbed his back. “Yeah,” he said. “A long time ago. You guys got your buckets full yet?”

“Just about,” Eddie said.

The sun slid down behind the great dark mass of the Big Woods. A cool breeze stirred the tall dry grass of the clearing.

Mr. Muldoon walked over to look at the fireplace.

“What do you suppose happened to the people who lived here?” Eddie asked him.

“Oh, they probably moved away,” Mr. Muldoon said.

“Why would they do that?” Eddie said.

“How should I know?” Mr. Muldoon said.

A lone raven flew over, silent except for the rustle of its wings.

“Maybe they were all murdered,” Eddie said. “Some bandits came along and murdered them.”

They weren’t murdered,” Mr. Muldoon said. “They moved away.”

A board clattered to the ground on the far side of the clearing. We stared in the direction of the sound. Nothing there. We stared in the direction of the sound. Nothing there. The breeze sighed through the tall grass, as though whispering to us of some dreadful mystery of long ago.

“The murdered people are probably buried under those roses,” Eddie said. I looked at the patch of wild roses. It seemed likely. Otherwise, what would wild roses be doing out in the middle of a clearing?

“There are probably ghosts here, don’t you think, Pa?” Eddie said. “The ghosts of the poor murdered people.”

“Eddie,” Mr. Muldoon said. “There’s no such thing as ghosts. There you go again, letting your imagination – what’s that?”

“What’s what, Pa?”

“Nothing. Just the wind I guess.”

“Could have been a ghost,” Eddie said. “What did it sound like, Pa?”

Mr. Muldoon didn’t reply. He seemed absorbed in thought, possibly reassessing his opinion about the existence of ghosts.

“Gosh,” I said. “Maybe I’d better be heading home.”

“Me too,” Eddie said. It’s probably about the time the ghosts come out. I bet they wander around the clearing out here talking to each other after dark, just like they did before they were murdered.”

“Eddie . . . “ Mr. Muldoon said, stroking the hair on the back of his neck.

A rock tumbled from the fireplace chimney. All three of us jumped. Mr. Muldoon picked his hat up off the ground and slapped it back on his head.

“Yeah,” I said. “I’d better head on home.” I turned and sauntered toward the entrance of the trail through the Big Woods. I could hear the grass whispering all around me. I sauntered faster. Eddie passed me at a quick walk. I started to trot to keep up. Eddie broke into a run. I ran past him. Eddie passed me. I had the distinct feeling something was after us. Now Eddie and I were flying down the trail, running harder and harder, cold sweat streaming out behind. I could hear things gaining on us, an eerie angry rumbling coming closer and closer. We sailed over logs across the trail without even touching them, logs so big Mr. Muldoon had to boost us over them on the way into the dreadful clearing. Eddie slipped and fell, and I leaped over him without even breaking stride and kept going. It was each man for himself now. Eddie shot past me a second later. And at last we burst out of the woods and slid to a stop in the ditch by the highway. The drivers of the cars going by glanced out at us, little realizing they were looking at two boys who had just made a desperate escape from an unknown number of irate ghosts.

“I sure hope the ghosts didn’t get Pa,” Eddie gasped.

“Me too,” I said.

“Whewee!” Mr. Muldoon said.

Eddie and I whirled around. We thought he’d still be back in the clearing. I couldn’t help but stare down at his big old clodhopper boots, to make sure he was still wearing them. He was. They seemed to be giving off steam, but that may have just been my imagination.

Mr. Muldoon sucked in a draft of air, as he glanced back up the trail behind us. “Well, that was invigorating. Gasp! So, you boys thought you could – gasp – race the old man home, did you? Wheweee! I guess I showed you I could – choke- hold my own with a couple of kids even after a late start”

We crossed the highway into Eddie’s yard, with Mr. Muldoon stopping to rest every few feet. He seemed a little shaky. “Yep, that was – gasp—quie a race,” he said. “I probably would have beaten the two of you, if I hadn’t been worried about spilling my bucket of berries. Look here—gasp—I didn’t lose a single ber--!

And then Mr. Muldoon slammed facedown on the ground, sending the berries spraying from his bucket.

“Pa!” Eddie cried out. “Are you all right? What’s the matter, Pa? Your heart? Is it your heart?”

Eddie’s father rolled over on his back and propped himself up on his elbows. All three of us looked down at his foot. One of Eddie’s snares had finally caught something.
```

---

## IC-2385: Biscuits of Glory

- Title: Biscuits of Glory
- Author (byline): Bruce Coville
- Work: Odder than Ever
- Publisher: Graphia
- Publication date as stated: Oct 2000
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: BENJIE, ELVIRA, DAN, REV. ZEPHYR
- Teaser before the introduction: Yes
- Spoken words (computed): 1405
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bruce Coville
Book: Odder than Ever
ISBN: 978-0152024659
Publisher: Graphia
Date (Month/Year): Oct 2000
```

### Introduction (context only: never use it for content warnings)

```text
When Benjie Perkins meets the ghost of Elvira Thistledown he learns the strange story behind why she haunts his kitchen -- and what he must do to free her from her curse. Biscuits of Glory by Bruce Coville
```

### Performance text (classify this)

```text
BENJIE: (Pg 20-28) I am haunted by biscuits -- Elvira Thistledown's biscuits, to be more precise. But I don't have any regrets. If I had it to do over again, I would still eat one, if only to free that poor woman from her curse. I'd do it even knowing how it was going to affect the rest of my life.

ELVIRA: (singing softly, sweetly and sadly, almost like a hymn) Biscuits, biscuits of glory, This is my story, Biscuits of glory . . .

BENJIE: I was ten when it happened. We had just moved into a new house. Well, new to us; it was really a very old one.

On our third night in the house, I heard a clatter in the kitchen. Now all old houses have their noises, their own personal creaks and groans. But something about this particular noise didn't sound right to me. So I grabbed my baseball bat and headed for the stairs. Trying not to wake my parents, I tiptoed along the hall, past the peeling wallpaper, past the bathroom, on to the head of the stairs. I paused and listened. Something was definitely moving in the kitchen. I could hear scrapes and thumps, soft and gentle. I was about to go wake my parents when I heard something else -- something totally unexpected. I heard a woman singing. I leaned forward and closed my eyes, straining to hear.

ELVIRA: (singing softly, sweetly and sadly, almost like a hymn) Biscuits, biscuits of glory, This is my story, Biscuits of glory . . .

BENJIE: By now the hair was standing up on the back of my neck. Yet somehow I didn't think anyone who sounded so sad and sweet could hurt me.

ELVIRA: Biscuits, biscuits of glory.

BENJIE: Pushing lightly on the kitchen door, I swung it open just a crack. When I peeked through, I let out a little squeak of fright. There was no one in sight, not a person to be seen. What I did see was a bag of flour, which wouldn't have been that unusual, except for the fact that this bag was floating through the air. The bag of flour opened, seemingly by itself. A measuring cup drifted into the air, then dipped into the flour bag. As the cup came out of the bag, a little thrill ran down my spine. Suddenly I could see the hand that was holding it -- covered with flour!

ELVIRA: Biscuits, biscuits of glory . . . (her voice catches as she chokes back a sob)

BENJIE: I couldn't help myself. Stepping through the door into the kitchen . . . "What is it? What's wrong?"

The flour-covered hand jerked sideways, knocking over the container of baking powder.

ELVIRA: (startled and frightened) Who are you?

BENJIE: I'm Benjie Perkins. I live here. Who are you?

ELVIRA: (whispering) Elvira Thistledown. I died here.

BENJIE: What are you doing?

ELVIRA: Making biscuits. (sets the baking powder upright) I make biscuits every Saturday night. Saturday at midnight. It's my curse. (she continues to work) I always loved to make biscuits. My mother taught me when I was only seven years old.

BENJIE: I hate to interrupt, but is it possible for you to become visible? I might feel less nervous if you did.

ELVIRA: Well, it's not easy. But you seem like a nice boy. Just a minute and I'll see what I can do.

BENJIE: Soon a milky light began to glow in front of me. It started out kind of blobby, but after a minute or two it condensed into the form of a woman. She was younger and prettier than I had expected. .

ELVIRA: Better? (she returns to her work) It was vanity did me in. I was so proud of my biscuits that I just couldn't stand it when that awful Dan McCarty moved into town and started bragging that he made the best biscuits in the state.

DAN: Why, my biscuits are lighter than dandelion fluff. Apt to float away on the first stiff breeze.

ELVIRA: After a while his proud talk got to me, and I chal-lenged him to a contest -- A biscuit bake-off. Both of us to make biscuits, results to be judged by Reverend Zephyr of the Baptist Church.

BENJIE: Did you win? (to audience) She was busy working on her biscuits, so she didn't answer right away. She had turned the dough out onto the counter and was kneading it lightly

ELVIRA: I lost. I lost, and that was the beginning of my downfall. I became obsessed with biscuits. I swore I would make a better biscuit than Dan McCarty or die trying. (she finishes kneading and begins to cut the dough into rounds) We began to have a weekly contest, Dan and I. Every Sunday morning we'd take our biscuits to church, and after the service Reverend Zephyr would try them out. He'd measure them. He'd weigh them. Finally he'd taste them, first plain, then with butter, then with honey. And every Sunday he'd turn to me and say,

REV. ZEPHYR: I'm sorry, Elvira, but Dan's biscuits are just lighter and fluffier than yours.

ELVIRA: (Popping the tray into the oven) I was like a madwoman. (she gradually become more scary) I worked day and night, night and day, trying every combination I could think of to make my biscuits lighter, fluffier, more wonderful than any that had ever been made. I wanted biscuits that would float out of the oven and melt in your mouth. I wanted biscuits that would make the angels weep with envy. (whispering) The key is in the baking powder. (her eyes wild)

BENJIE: I was beginning to be frightened again. I wondered if she really was crazy - and if she was, just what a crazy ghost might do.

ELVIRA: One Sunday I was sure I had it; I came to church with a basket of biscuits that were like a stack of tiny featherbeds. But after the judging, Reverend Zephyr shook his head sadly and said,

REV. ZEPHYR: Sorry, Elvira.

ELVIRA: By the next Saturday night I was wild, desperate, half insane. In a fit of desperation, I dumped an entire can of baking powder into my dough.

BENJIE: What happened?

ELVIRA: The oven door blew off and killed me on the spot. And ever since, I've been doomed to bake a batch of biscuits every Saturday at midnight, as punishment for my pride. What's worse, I finally know the secret. Learned it on the other side. These biscuits are the lightest, fluffiest ever made, Benjie. But no one has ever tasted them, and I can't rest until someone does.

BENJIE: How come no one has ever tasted them?

ELVIRA: (near tears) How can they? My biscuits of glory are so light and fluffy they float right out of the oven and disappear through the ceiling. If I could leave them on the counter overnight, someone might have tried them by now. But they're always gone before anyone gets a chance.

BENJIE: These biscuits of yours-they wouldn't hurt someone who ate them, would they?

ELVIRA: Of course not! These are biscuits of glory. One bite and you'll never be the same.

BENJIE: What if I grabbed one as it came out of the oven?

ELVIRA: You'd burn your hand.

BENJIE: Wait here! (to audience) I scurried up the stairs and rummaged through my room until I found what I was looking for. I went down the stairs two at a time, hoping to make it to the kitchen before Elvira's biscuits came out of the oven. She was standing by the big old oven as I slipped through the swinging door.

ELVIRA: What's that?

BENJIE: My catcher's mitt. Are the biscuits ready?

ELVIRA: To perfection! (she opens the oven door)

BENJIE: Out floated a dozen of the most perfect biscuits I had ever seen-light, golden brown, high and fluffy, crusty around the edges. (he reaches out with the mitt and snags a biscuit)

ELVIRA: Careful, they're hot!

BENJIE: (Ignoring her warning, he takes the biscuit from the glove) Ow! (he loses his grip and the biscuit heads toward the ceiling. He scrambles to snag another one) I was more careful this time, cupping the glove over it and holding it tenderly while it cooled. I could feel the heat, but the leather protected me. Finally I thought it was safe to try a bite. (Elvira watches with wide eyes and he takes the biscuit from his glove and lifts it to his lips) It was astonishing, the most incredible biscuit I have ever tasted! (he begins to float off the ground) Suddenly I realized something even more astonishing: I was floating! I had lifted right off the counter and was hovering in midair. I worried about getting down, but as I chewed and swallowed, I drifted gently to the floor. (to Elvira) What an amazing biscuit. I feel like I've died and gone to heaven!

ELVIRA: So do EyeeeeeeeI! (Elvira floats through the roof and disappears)

BENJIE: . . . . as if she were being snatched into the sky. That was the last I ever saw of Elvira Thistledown. Her biscuits, however, haunt me still. It's not just the memory of their taste, though I have never again tasted anything so fine. It's the effect of the darned things. See, whenever I get too happy, or too excited, or begin thinking about those biscuits too much, I start to float. It gets a little embarrassing sometimes. I'll tell you this, though. Unlike some people, I'm not afraid of what happens after you die. I know what I'll find waiting on the other side . . . (Sings) Biscuits. Biscuits of glory.
```

---

## IC-2386: The Boogeyman

- Title: The Boogeyman
- Author (byline): Stephen King
- Work: Night Shift
- Publisher: Signet Books
- Publication date as stated: Dec 1994
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1766
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephen King
Book: Night Shift
ISBN: 978-0451170118
Publisher: Signet Books
Date (Month/Year): Dec 1994
```

### Introduction (context only: never use it for content warnings)

```text
The man: Lester Billings from Waterbury, Connecticut. According to the history taken from Nurse Vickers, he is twenty-eight, employed by an industrial firm in New York, divorced, and the father of three children. All deceased. This is Lester’s story (AKA The Boogeyman by Stephen King).
```

### Performance text (classify this)

```text
I came to you because I want to tell my story, I can't go to a priest because I’m not Catholic. I can't go to a lawyer because I haven't done anything to consult a lawyer about. All I did was kill my kids. One at a time. Killed them all. Denny in 1967. Shirl in 1971. And Andy this year. I want to tell you about it.

I married Rita in 1965-I was twenty-one and she was eighteen. She was pregnant. That was Denny. I had to leave college and get a job, but I didn't mind. I loved both of them. We were very happy.

Rita got pregnant just a little while after Denny was born, and Shirl came along in December of 1966. Andy came in the summer of 1969. Denny was already dead by then. Andy was an accident. That's what Rita said. She said sometimes that birth-control stuff doesn't work. I think that it was more than an accident. Children tie a man down, you know. Women like that, especially when the man is brighter than they. It doesn't matter, though. I loved him anyway

The boogeyman killed them all. Just came out of the closet and killed them. You think I’m crazy. It's written all over you. But I don't care. All I want to do is tell you and then get lost.

It started when Denny was almost two and Shirl was just an infant. He started crying when Rita put him to bed. We had a two-bedroom place, see. Shirl slept in a crib in our room. At first I thought he was crying because he didn't have a bottle to take to bed anymore.

Rita said don't make an issue of it, let it go, let him have it and he'll drop it on his own. But that's the way kids start off bad. You get permissive with them, spoil them. Then they break your heart. Get some girl knocked up, you know, or start shooting dope. Or they get to be sissies. Can you imagine waking up some morning and finding your kid-your son-is a sissy?

After a while, though, when he didn't stop, I started putting him to bed myself. And if he didn't stop crying I’d give him a whack. Then Rita said he was saying 'light' over and over again. Well I don't know. Kids that little, how can you tell what they’re saying. Only a mother can tell.

Rita wanted to put in a nightlight. One of those wall-plug things with Mickey Mouse or Huckleberry Hound or something on it. I wouldn't let her. If a kid doesn't get over being afraid of the dark when he's little, he never gets over it. Anyway, he died the summer after Shirl was born. I put him to bed that night and he started to cry right off. I heard what he said that time. He pointed right at the closet when he said it. 'Boogeyman," the kid says. 'Boogeyman, Daddy.'

I turned off the light and went into our room and asked Rita why she wanted to teach the kid a word like that. I was tempted to slap her around a little, but I didn't. She said she never taught him to say that.

That was a bad summer for me, see. The only job I could get was loading Pepsi-Cola trucks in a warehouse, and I was tired all the time. Shirl would wake up and cry every night and Rita would pick her up and sniffle. I tell you, sometimes I felt like throwing them both out a window. Christ, kids drive you crazy sometimes. You could kill them.

Well, the kid woke me at three in the morning, right on schedule. I went to the bathroom, only a quarter awake, you know, and Rita asked me if I’d check on Denny. I told her to do it herself and went back to bed. I was almost asleep when she started to scream.

I got up and went in. The kid was dead on his back. Just as white as flour except for where the blood had . . . had sunk. Back of the legs, the head. His eyes were open. That was the worst, you know. Wide open and glassy, like the eyes you see on a moosehead some guy put over his mantel. Like pictures you see of those gook kids over in Nam. But an American kid shouldn't look like that. Dead on his back. Wearing diapers and rubber pants because he'd been wetting himself again the last couple of weeks. Awful, I loved that kid.

Rita was screaming her head off. She tried to pick Denny up and rock him, but I wouldn't let her. The cops don't like you to touch any of the evidence. I know that-

The closet door was open. Not much. Just a crack. But I knew I left it shut, see.

We moved Shirl into Denny's old room a month after the funeral. Rita fought it tooth and nail, but I had the last word.

It hurt me, of course it did. Jesus, I loved having the kid in with us. But you can't get overprotective. You make a kid a cripple that way. Life goes on. Shirl went right into Denny's crib. We sent the old mattress to the dump, though. I didn't want my girl to get any germs. So a year goes by. And one night when I'm putting Shirl into her crib she starts to yowl and scream and cry. 'Boogeyman, Daddy, boogeyman, boogeyman!” That threw a jump into me. It was just like Denny. And I started to remember about that closet door, open just a crack when we found him.

The boogeyman got her, too. A month later. But something happened before that. I heard a noise in there one night. And then she screamed. I opened the door real quick-the hall light was on-and . . . she was sitting up in the crib crying and . . . something moved. Back in the shadows, by the closet.

When she died I found her, see. And she was black. All black. She swallowed her own tongue and she was staring at me. Her eyes, they looked like those eyes you see on stuffed animals, all shiny and awful, like five marbles, and they were saying it got me, Daddy, you let it get me, you killed me, you helped it kill me . . .

Rita still loved me. Oh, she was sort of colorless the first four or five months after - dragged around the house, didn't sing, didn't watch the TV, didn't laugh. I knew she'd get over it. When they're that little, you don't get so attached to them. After a while you have to go to the bureau drawer and loot at a picture to even remember exactly what they looked like.

So what's next? She's knitting little things, singing in the shower, and eating pickles like crazy. Sitting on my lap and saying things about how it must have been God's will. The baby came at the end of the year after Shirl's death. That's right. A boy. She named it Andrew Lester Billings. I didn't want anything to do with it, at least at first. My motto was she screwed up, so let her take care of it. I know how that sounds but you have to remember that I'd been through a lot.

But I warmed up to him, you know it? He was the only one of the litter that looked like me, for one thing. Denny looked like his mother, and Shirl didn't look like anybody. But Andy was the spitting image of me.

That next year was the best one for us. I’d give every finger on my right hand to have it back again. But this last year wasn't so good. Something about the house changed. I started keeping my boots in the hall because I didn't like to open the closet door anymore. I kept thinking: Well, what if it's in there? All crouched down and ready to spring the second I open the door?

Andy died in February. Rita wasn't there. She got a call from her father. Her mother had been in a car crash the day after New Year's and wasn't expected to live. She took a bus back that night. It was all right when Rita was there, but when she was gone, it started to get bolder.

You'd wake up at three in the morning and loot into the dark and at first you'd say, 'It's only the clock.' But underneath it you could hear something moving in a stealthy way. But not too stealthy, because it wanted you to hear it. And you'd close your eyes, knowing that hearing it was bad, but if you saw it.

And always you'd be afraid that the noises might stop for a little while and then there would be a laugh right over your face and a breath of air like stale cabbage on your face and then hands on your throat.

The kid was sleeping in the room with me. I didn't want to move him. I was afraid to, after Denny and Shirl. But with Rita gone, I moved him. I knew it would go for him, see. Because he was weaker. And it did. That very first night he screamed in the middle of the night and finally, when I got up the courage to go in, he was standing up in bed and screaming. 'The boogeyman, Daddy. . . boogeyman . . . wanna go wif Daddy, go wif Daddy.”

"But I couldn't,", "I couldn't. And an hour later there was a scream. An awful, gurgling scream. And I knew how much I loved him because I ran in, I didn't even turn on the light, I ran, ran, ran, oh, Jesus God Mary, it had him; it was shaking him, and I heard . . . I heard it when Andy's neck broke."

When it was over, I called the police. He was lying on the floor and staring at me. Accusing me. A tiny bit of blood had run out of one ear. Only a drop, really. And the closet door was open-but just a crack."

I lied to the police, see? Told them the kid must have tried to get out of his crib in the night and . . . they swallowed it. Course they did. That's just what it looked like. Accidental. like the others. But Rita knew. Rita . . . finally . . . knew. . .
```

---

## IC-2387: Bottleman

- Title: Bottleman
- Author (byline): Eric Bogosian
- Work: Sex, Drugs, Rock & Roll
- Publisher: Theatre Communications Group
- Publication date as stated: 1996
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1109
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric Bogosian
Book: Sex, Drugs, Rock & Roll
ISBN: 978-1559361248
Publisher: Theatre Communications Group
Date (Month/Year): 1996
```

### Introduction (context only: never use it for content warnings)

```text
This past Monday, 36,782 homeless people spent the night in a New York City shelter; the number who slept on the street is impossible to ascertain. Homeless men and women are part of an expanding, often faceless community. When we come in contact with a homeless person, we may feel repulsed, annoyed, even angered as we avert our eyes and think, "Why don't they do something to help themselves?" or "If I look them in the eye, that'll just encourage them to ask me for money" or "They choose to be homeless." Frequently, it is our lack of understanding about the complexities of homelessness that fuels our prejudices and fears about homeless people. Somehow, that gives us "permission" to act less compassionately towards a homeless person — who is, after all, a human being just like us. I’d like to introduce you to Bottleman by Eric Bogosian

(A man talks quickly, nervously, rarely looking at the audience. He constantly hitches his pants and pats his hair. His over cheerful manner covers his fear. He’s making conversation with an imaginary listener. He begins by talking to the wall.)
```

### Performance text (classify this)

```text
NOTE: This cutting met the requirements for

PROSE by the National Speech and Debate

Association in 2008. Rules governing the PROSE

category have changed over time and this selection

no longer meets the requirements for PROSE by

the NSDA as it is a monologue from a play.

State rules governing PROSE vary from state to

state, so please verify your state’s current rules

before competing with this selection in the PROSE

category.

I don’t like to complain. I’m not a complaining kind of guy, I’m a happy kind of guy – runs in my family, happiness. Never been sick in my life. Not one day. Unless you count broken bones, which I don’t. But I like to stay positive. Stay on the sunny side of the street. You give me a pack of cigarettes, egg salad sandwich, cup of coffee, a newspaper, someplace to sit down, and I’m happy – I’m happy.

I don’t even need the cigarettes, I should quit anyway. It’s a dirty habit. Unhealthy. Expensive. Of course you can always find cigarettes. People always have cigarettes – they’ll give ‘em to you. Food’s another subject altogether. People aren’t exactly walking around with an egg salad sandwich in their pocket – unless they’re crazy! And you figure, egg salad sandwich’s gonna run you maybe seventy-eighty bottles. I’m findin’ maybe fifty bottles a day – you’re talking a short-fall of about twenty bottles. . . or cans . . . bottles or cans, it doesn’t make much difference.

Back in the old days, I used to weigh a lot more than I do now. Used to be on a diet all the time. Always trying to lose weight. I don’t have that problem anymore. I’m on the egg salad sandwich diet now. One egg salad sandwich every two days . . . you lose weight like crazy. The fat just flies off . . . and it stays off. I’m gonna patent it. Get a copyright and put an ad in the newspaper. Make a little money.

See, newspapers – newspapers, you can get. You can always find a newspaper, people just leave ‘em around. And I read ‘em. I wanna know about the world.

It’s important to stay informed. I read about a train in Japan goes three hundred miles an hour, gets you there in no time. They got hotels for cockroaches now, hotels for mice. I stay away from hotels. Too much money – who’s got that kinda money? Then bucks a night, forget it. You figure that’s two hundred bottles – bottles or cans – and that’s not in my budget.

But it’s not a problem. You can always find someplace – there’s always someplace to stay. You wedge yourself in someplace. The real problem is the concrete. The stone. They make everything out of rocks and cement! Too hard. Whatever happened to wood? Used to be all the buildings were made out of wood. Used to make benches outa wood. But no more. Because they make wood outa trees, and trees, they don’t got them no more.

I saw this tree . . . there was this tree, beautiful tree . . . they dug a hole and put it in the sidewalk. Every day I come to say hello. And this guy was backing up his truck. The truck was making that beep sound – beep-beep-beep-beep—right over the tree, That was it for the tree. That was it. What are you gonna do? It’s just in the nature of a tree that if you run ‘em over they die. They’re not like people – they can’t take the abuse.

Take a tree, replace it was a metal pole, then there’s no problem. Truck hits the pole, that’s it, But you lose the leaves. You lose the leaves and the twigs. You lose the wood. Wood is good.

Dogs like wood. I know – I used to have a dog. Walked him every day. I used to say (miming walking the dog): “Come on! Come on! . . . Who takes care of you? Who takes care of you? I take care of you. Who’s gonna take care of me in my old age? Who’s gonna take care of me?” That’s what I used to ask him . . .

He ran away. But that’s okay – they gotta eat too, the little ones. Everybody’s gotta eat, sooner or later. It’s human nature. It’s human nature. I like to eat. I like to eat. Kind of a habit of mine, food. (He holds an imaginary sandwich before his face)

Nice egg salad sandwich. Cup a coffee . . . Cream. Sugar.

I’m cutting down on the coffee. I don’t drink much coffee these days. Sixty cents a cup. Where did they come up with that figure, that’s the question I want to ask. Should be ten cents! But they got ya, see, they got ya. ‘Cause they got the beans. They got the beans. You got no choice. They got a cartel. This OPEC.

But I don’t need coffee. I don’t need the coffee. People drink coffee to stay awake – I don’t need to stay awake. I’m awake, I’m awake. When I’m asleep I’m awake. You gotta keep your eyes open when you’re sleeping, ‘cause you find a place to lie down and you don’t keep your eyes open and a guy comes back with a baseball bat and that’s it – bang, bang, you’re dead!

No more coffee, no more cigarettes – that’s it!

See, these guys on the street, they like to fight. I don’t got that luxury. I’m on my second set of teeth, I’m missing a kneecap, I can’t hear in one ear. I’m like the bionic man without the hardware. I’m no Cassius Clay. I’m no Cassius Clay. (Pause) But I stay on the sunny side of the street. I stay on the sunny side of the street. A guy once told me, “Life is like a half a glass of water . . . half a glass of water . . . “ (He loses his train of thought; his hand is shaking, holding the imaginary glass)

You got a half a glass a water . . . “And . . . uh . . . you should drink the water,” that’s what he said. . .

(Sheepish – he didn’t get the saying right – he turns away, then laughs at himself.)

No, that isn’t what he said . . . He said . . . he said . . . “Half a glass of water is better than no water at all!” That’s it. “Half a glass of water is better than no water . . . “ (Full of energy again)

I look at it this way – I could be living in Ethiopia. Those poor people got it terrible. They got nothing to eat. Starving all the time. They just sit in the sand all day long . . . It’s too sunny, too many flies . . . it’s not for me. It’s not my bag. I prefer it here . . . it’s better here. (Lost in thought, convincing himself)

It’s good here, it’s good. It’s good. Thank God! (Pause. He’s just standing, staring at the ground. He snaps out of it – sunny, cheerful again, he addresses the audience.)

Well, I gotta get going, got to get to work. You know what they say: “The early bird catches the can!”

Or bottles . . . bottles or cans, it don’t make no difference . . . It don’t make no difference at all . . . .
```

---

## IC-2388: The Boy in the Striped Pajamas

- Title: The Boy in the Striped Pajamas
- Author (byline): John Boyne
- Work: Not specified
- Publisher: David Fickling Books
- Publication date as stated: Oct 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: SHMUEL, BRUNO, SCHMUEL, BURNO, BRUO
- Teaser before the introduction: Yes
- Spoken words (computed): 1723
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Boyne
ISBN: 978-0385751537
Publisher: David Fickling Books
Date (Month/Year): Oct 2007
```

### Introduction (context only: never use it for content warnings)

```text
This is the story of an event seared into the fabric of history. It is a fable told through the voice of a child . . . but it is not for children. The year is 1943. Bruno is 9-years-old and is quite unaware of a place called Auschwitz and the fate of the Jews where were sent there. All he knows is that his father is a soldier. Shmeul is also 9, but lives on the other side of the fence. They form a friendship that crosses dangerous boundaries and can only end in tragedy. And somehow, events are all the more tragic when narrated by those who do not understand. The Boy in the Striped Pajamas by John Boyne
```

### Performance text (classify this)

```text
SHMUEL: (Pg 126) All I know is this. Before we came here I lived with my mother and father and my brother Josef in a small flat above the store where Papa makes his watches. Every morning while we went to school, Papa mended the watches that people brought to him and made new ones too.

SHMUEL: (Pg 126-128) And then one day things started to change. I came home from school and my mother was making armbands for us and drawing a star on each one. Like this (Draws a Star of David in the air). And every time we left the house, she told us we had to wear one of these armbands.

BRUNO: My father wears one too . . . on his uniform. It’s very nice. It’s bright red with a black-and-white design on it. (Draws a swastika in the air)

SCHMUEL: Yes, but they’re different, aren’t they?

BRUNO: No one’s ever given me an armband.

SHMUEL: But I never asked to wear one.

BRUNO: All the same, I think I’d quite like one. I don’t know which one I’d prefer though, your one or Father’s.

SCHMUEL: We wore the armbands for a few months, and then things changed again. I came home one day and Mama said we couldn’t live in our house anymore.

BRUNO: That happened to me too! The Fury came for dinner, you see, and the next thing I knew we moved here. And I hate it here. Did he come to your house and do the same thing?

SCHMUEL: No, but when we were told we couldn’t live in our house, we had to move to a different part of Cracow, where the soldiers built a big wall and my mother and father and my brother and I all had to live in one room.

BRUNO: All of you? In one room?

SCHMUEL: And not just us. There was another family there and the mother and father were always fighting with each other and one of the sons was bigger than me and he hit me even when I did nothing wrong.

BRUNO: You can’t have all lived in the one room. That doesn’t make any sense.

SCHMUEL: All of us. Eleven in total. (Pg 129-132) Then one day the soldiers all came with huge trucks and everyone was told to leave the houses. Lots of people didn’t want to and they hid, but in the end I think they caught everyone. And the trucks took us to a train and a train . . . . and the train was horrible.

There were too many of us in the carriages for one thing. And there was no air to breathe. And it smelled awful.

BRUNO: That’s because you all crowded onto one train. When we came here, there was another one on the side of the platform but no one seemed to see it. That was the one we got. You should have got on it too.

SCHMUEL: I don’t think we would have been allowed. We weren’t able to get out of our carriage.

BRUNO: The doors are at the end.

SCHMUEL: There weren’t any doors.

BRUNO: Of course there were door. They’re at the end. Just past the buffet section.

SCHMUEL: There weren’t any doors. If there had been, we would all have got off. When the train finally stopped, we were in a very cold place and we all had to walk here.

BRUNO: We had a car

SCHMUEL: And Mama was taken away from us, and Papa and Josef and I were put into the huts over there and that’s where we’ve been ever since.

BRUNO: Are there many other boys over there?

SCHMUEL: Hundreds.

BRUNO: Hundreds? That’s not fair at all. There’s no one to play with on this side of the fence. Not a single person.

SCHMUEL: We don’t play. . . . . You don’t have any food on you, do you?

BRUNO: Afraid not . . . perhaps you can come to dinner with us one evening.

SCHMUEL: Perhaps

BRUNO: Or I could come to you. Perhaps I could come and meet your friends.

SCHMUEL: You’re on the wrong side of the fence though.

BRUNO: I could crawl under. (Reaches down and lifts the wire fence off the ground)

SCHMUEL: I have to go back.

BRUNO: Some other afternoon then.

SCHMUEL: I’m not supposed to be here. If they catch me, I’ll be in trouble.

BRUNO: (Pg 133) I’ll come back tomorrow. (Pg 161) For several weeks the rain was on and off and on and off and Bruno and Schmuel did not see as much of each other as they would have liked.

BRUNO: (Pg 194-196) I thought you weren’t coming any more. I came yesterday and the day before and you weren’t here.

SCHMUEL: I’m sorry. Something happened. . . . Papa. We can’t find him.

BRUNO: Can’t find him? That’s very odd. You mean he’s lost?

SCHMUEL: I suppose so. He was here on Monday and then he went on work duty with some other men and none of them have come back.

BRUNO: And hasn’t he written you a letter? Or left a note to say when he’ll be coming back?

SCHMUEL: No.

BRUNO: How odd. Have you looked for him?

SCHMUEL: Of course I have.

BRUNO: And there was no sign?

SCHMUEL: None.

BRUNO: Well, that’s very strange. But I think there must be a simple explanation. I could ask Father if you wanted.

SCHMUEL: I don’t think that would be a good idea.

BRUNO: Why not? Father is very knowledgeable about life on that side of the fence.

SCHMUEL: I don’t think the soldiers like us. Well, I know they don’t like us. They hate us.

BRUNO: I’m sure they don’t hate you.

SCHMUEL: They do, but that’s all right because I hate them too. I hate them!

BRUNO: You don’t hate Father, do you? (Long pause) Anyway, I have something to tell you too. I’m going back to Berlin. We’re leaving on Saturday.

SCHMUEL: But for how long?

BRUNO: I think it’s forever. Mother doesn’t like it at Out-With (Bruno’s pronunciation of Auschwitz) – she says it’s no place to bring up children – so Father is staying here to work because the Fury has big things in mind for him, but the rest of us are going home.

SCHMUEL: So I won’t see you again?

BURNO: Well, someday, yes. You could come on a holiday to Berlin. You can’t stay here forever after all. Can you?

SCHMUEL: I suppose not. I won’t have anyone to talk to anymore when you’re gone.

BRUNO: (Pg 197-199) I wish we’d got to play together. Just once. Just to remember. We’ve been talking to each other for more than a year and we never got to play once. All this time I’ve been watching where you live from my bedroom window and I’ve never even seen for myself what it’s like

SCHMUEL: You wouldn’t like it. Yours is much nicer.

BRUNO: I’d still like to have seen it.

SCHMUEL: (putting his hand under the fence and lifting a little) Well? Why don’t you then?

BRUNO: But if I was caught I’d be in trouble.

SCHMUEL: That’s true. I suppose I’ll see you tomorrow to say goodbye then.

BRUNO: Unless . . . . Don’t you remember that you said I looked like you? Since I had my head shaved? Well, if that’s the case and if I had a pair of striped pyjamas too, then I could come over on a visit and no one would be any the wiser.

SCHMUEL: Would you do it? You could help me look for Papa.

BRUNO: Why not. The only problem is getting a spare pair of striped pyjamas.

SCHMUEL: That’s all right. There’s a hut where they keep them. I can get some in my size and bring them with me. Then you can change and we can look for Papa.

BRUNO: Wonderful. Then it’s a plan! [The next day, the two boys meet for the last time.] (Pg 202-203) Schmuel lifted the bottom of the fence off the ground and handed a pair of striped pyjama bottoms, a striped pyjama top and a striped cloth cap exactly like the one he was wearing, underneath to Bruno.

BRUNO: Well, turn round. I don’t want you watching me. (Schmuel turns and Bruno changes clothes) When was this last washed?

SCHMUEL: I don’t know if it’s ever been washed.

(Bruno finishes changing)

BRUNO: (Pg 204) There, you can turn back now. (They wander into the camp) If it wasn’t for the fact that Bruno was nowhere near as skinny as the boys on [this] side of the fence, and not quite so pale either, it would have been difficult to tell them apart. It was almost as if they were all exactly the same really.

BRUNO: (Pg 205) I’m pretending to be a person from the other side of the fence.

SCHMUEL: A Jew, you mean.

BRUNO: Yes, that’s right. (Pg 208) Everywhere [Bruno] looked, all he could see was two different types of people: either happy, laughing, shouting soldiers in their uniforms or unhappy, crying people in their striped pajamas, most of whom seemed to be staring into space as if they were actually asleep.

BRUNO: I don’t think I like it here.

SCHMUEL: Neither do I. (Pg 209-210) The two boys spent an hour and a half searching the camp. They weren’t sure exactly what they were looking for, but they didn’t find anything at all that might give them a clue to Shmuel’s papa’s disappearance, and it started to get darker.

BRUNO: I’m sorry, Shmuel. I’m sorry we didn’t find [anything]. I think I ought to go home now. Will you walk back to the fence with me? (Actor playing Schmuel steps behind Bruno and whistles loudly – the whistle is the sound of the solders getting ready to order people on a march). What’s happening? What’s going on?

SCHMUEL: It happens sometimes. They make people go on marches.

BRUNO: Marches! I can’t go on a march. I have to be home in time for dinner. It’s roast beef tonight.

SCHMUEL: Sshhh! Don’t say anything or they get angry.

BRUNO: (Pg 211-213) Does the marching go on for long?

SCHMUEL: I don’t think so. I never see the people after they’ve gone on a march. But I wouldn’t imagine it does.

BRUNO: That’s it. I’m going to catch a cold out here. I have to go home. But as he said this, his feet brought him up a set of steps and into a long room that was surprisingly warm and must have been very securely built because no rain was getting in anywhere. In fact it felt completely airtight.

BRUO: Well, that’s something. I expect we’ll have to wait here till [the rain] eases off and then I’ll get to go home. I’m sorry we didn’t find your Papa. [And] I’m sorry we didn’t really get to play, but when you come to Berlin, that’s what we’ll do. You’re my best friend, Schmuel. My best friend for life!

At that moment there was a loud gasp from all the marchers who had filled the room. The door at the front was suddenly closed and a loud metallic sound rang through from the outside. And then the room went very dark and somehow despite the chaos that followed, Bruno found that he was holding Schmuel’s hand in his own and nothing in the world would have persuaded him to let it go.
```

---

## IC-2389: Breaking and Entering

- Title: Breaking and Entering
- Author (byline): Sherman Alexie
- Work: War Dances
- Publisher: Grove Press
- Publication date as stated: Aug 2010
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ELDER’S MOTHER, GEORGE
- Teaser before the introduction: Yes
- Spoken words (computed): 1501
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sherman Alexie
Book: War Dances
ISBN: 978-0802144898
Publisher: Grove Press
Date (Month/Year): Aug 2010
```

### Introduction (context only: never use it for content warnings)

```text
Life is made up of an infinite amount of choices. Some inconsequential; others life-changing. In fact, Graham Brown once said, “Life is about choices. Some we regret, some we are proud of. Some that will haunt us forever.”

Choices are not always black or white . . . or are they? In Breaking and Entering, Sherman Alexie explores how choices are impacted by ethnic identity, power, privilege and race.
```

### Performance text (classify this)

```text
(Pg 5-17) When I was first learning how to construct a scene, my professor said to me, “You don’t have to show people using a door to walk into a room. If people are already in the room, the audience will understand that they didn’t just materialize. The audience understands that a door has been used – the eyes and mind will make the connection – so you can just skip the door.

“Skip the door” is a good piece of advice that I’ve applied to my entire life. Omit all unnecessary information. So in telling you this story, in constructing its scenes, I will attempt to omit all unnecessary information. But oddly enough, in order to skip the door, I am forced to begin with a door: the front door to my home in Seattle, Washington. Once year ago there was a knock on that door.

I work at home, but I did not rise from my chair to answer. Bang, bang, bang, bang! It had to be a Jehovah’s Witness or a Mormon . . . or a magazine sales kid. Trust me, nobody interesting or vital has ever knocked on a front door at three in the afternoon. So I ignored the knocking and kept at my work. And, sure enough, my potential guest stopped the noise and went away.

But then, a few moments later, I heard a window shatter in my basement – shards of glass dropping onto a hardwood floor. And then one hears – feels – the epic thump of two feet landing on that same floor. Somebody – the same person who had knocked on my front door to ascertain if anybody was home, had just broken and entered my life.

Looking back, I suppose I should have just run away. I could have . . . the front door into the street, the back door onto the patio, the side door into the alley, or even the door into the garage . . . and made my escape.

But here’s the salt of the thing: I believe I was making my way toward the front door – after all the front door was the only place where I could be positive that my intruder was not waiting. But in order to get to the front door, I had to walk past the basement door. And as I walked past the basement door, I spotted the baseball bat. It belonged to my ten-year-old son. A Little League bat, so it was comically small.

Yes, I am a father. And a husband. That is information you need to now. My wife had taken our son to visit her mother and father. So, to be truthful, I was in no sense being forced to defend my family. And I’d never been the kind of man to defend his property. In fact, I’d often laughed at news footage of silly men armed with garden hoses as they tried to defend their homes from wildfires. I always figured those men would die, go to hell, and spend the rest of eternity having squirt-gun fights with demons.

So with all that information in mind, why did I grab my son’s baseball bat and open the basement door? Why? Trust me, I’ve spent many long nights asking myself those questions. There are no easy answers. There are many who believe I was fully within my rights to head down those stairs and confront my intruder. There are laws that define – that frankly encourage – the art of self-defense.

In the end, I think I wasn’t defending anything at all. Did I walk down those stairs because I was curious? Because a question has been asked (Who owned the feet that landed on my basement floor?) and I wanted to discover the answer?

So, slowly I made my way down the stairs and through the dark hallway into our family room and saw a teenaged burglar. I stood still and silent. Standing with his back to me, obsessed with the task – the crime – at hand, he hadn’t yet realized that I was in the room with him.

Let me get something straight. Up until that point I hadn’t made ay guesses as to the identity of my intruder. I mean, yes, I live in a black neighborhood – and I’m not black. There had been news of local burglaries by black teenagers, but I swear none of that entered my mind. I didn’t think, there’s a black teenager stealing from me. I only remember being afraid.

“Get out of here!” I screamed. “You ******!”

The black kid was so startled that he staggered and nearly fell before he caught his balance and ran for the broken window. I could have – would have – let him make his escape, but he stopped and turned back toward me. Why did he do that? He was young and scared and made an irrational decision. He searched for a door. The door behind me. He paused, weighed his options, and sprinted toward me. I could have made the decision step aside. But I didn’t. As that kid ran toward me, I swung the bat at the black teenager’s head. When it made full contact with the kid’s temple, he dropped to the floor and did not move.

He was dead. I had killed him. I fell to my knees, dropped my head onto his chest and wept.

I don’t remember much about the next few hours, but I called 911, and led the police to the body.

“Did he have a gun or knife?”

“I don’t know. No. Well, I didn’t see one. He ran at me. He was going to run me over.”

“And that’s when you hit him with the bat?”

“It’s my son’s bat. It’s so small. I can’t believe it’s strong enough to – is he really dead?”

His name was Elder Briggs, a sixteen-year-old kid, backup point guard for the basketball team at Garfield High School. A good kid. No criminal record. So why had this good kid broken into my house? Why?

The investigation was quick but thorough. I was not charged with any crime. It was self-defense. But then nothing is ever clear, is it? I was legally innocent, but was I morally innocent? Shortly after the police exonerated me, Elder’s family organized a protest. I watched the live coverage of the event:

ELDER’S MOTHER: “The police don’t care about my son because he’s black. Just another black boy killed by a white man. And none of these white men care.”

As she continued to rant about my whiteness – all of them, protesters, reporters – were unaware of one crucial piece of information: I am not a white man.

When I heard Althea Riggs misidentify my race – I picked up my cell phone and dialed the news station. [They] put me on live, and my voice played over images of Althea Riggs weeping and wailing at God:

GEORGE: I am watching the coverage of the protest, and I insist on a correction. I am not a white man. I am a member of the Spokane Tribe of Indians.

How could I have been such an idiot? How could I have been so goddamn callous and self-centered . . . I was pissed, mostly at myself for failing to walk away from a dangerous situation. But I was also pissed at Althea and Elder Briggs. Yes, the kid was a decent athlete; yes, the kid was a decent student; yes, the kid was a decent person. BUT . . . he had broken into my house.

And his mother instead of explaining why her good and decent son had broken and entered a stranger’s house, committing a felony, had instead decided to blame me and accuse me of being yet another white man who was always looking to maim another black kid – had already maimed generations of black kids – when in fact I was a reservation Indian who had been plenty maimed myself by generations of white men.

So, Althea, do you want to get into a pain contest? Do you want to participate in the Genocidal Olympics? Whose tragic history has more breadth and depth?

And oh, my God, it was a Little League baseball bat! It weighed less than three pounds. I could have hit one hundred men in the head and not done anything more than given them a headache. But on that one day, I took a swing – a stupid, one-handed, unlucky cut – and killed a kid, a son, a young man who was making a bad decision but who maybe had brains and heart and soul enough to stop making bad decisions.

Oh, Jesus, I murdered somebody’s potential. It was self-defense, but it was still murder. I confess: I am a killer. (Long pause)

How does one survive these revelations? One just lives. Or rather, one just finally walks out of his basement and realizes that the story is over. It’s old news. There are new villains and heroes -- criminals and victims to be defined, examined and tossed aside by the media. Life is infinitesimal and incremental and inconsequential. Elder Briggs and I were suddenly and equally unimportant.
```

---

## IC-2390: Breaking the Ice and You’ve Got to Be Kidding

- Title: Breaking the Ice and You’ve Got to Be Kidding
- Author (byline): Dave Barry
- Work: Dave Barry is NOT Making This Up
- Publisher: Ballantine Books
- Publication date as stated: Feb 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: JUDY, ME, WOODLAND CREATURES
- Teaser before the introduction: No
- Spoken words (computed): 1851
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Barry
Book: Dave Barry is NOT Making This Up
ISBN: 978-0345440648
Publisher: Ballantine Books
Date (Month/Year): Feb 2001
```

### Introduction (context only: never use it for content warnings)

```text
Dave Barry was born in Armonk, New York, in 1947 and has been steadily growing older ever since without ever actually reaching maturity. He attended public schools, where he distinguished himself by not getting in nearly as much trouble as he would have if the authorities had been aware of everything. He is proud to have been elected Class Clown by the Pleasantville High School class of 1965. For 25 years Dave Barry was a syndicated humor columnist whose work appeared in more than 500 newspapers in the United States and abroad. In 1988 he won the Pulitzer Prize for Commentary. Many people are still trying to figure out how this happened. For your viewing pleasure today, I’ve compiled two of his commentaries based on responses to readers’ letters. Breaking the Ice and You’ve Got to be Kidding by Dave Barry
```

### Performance text (classify this)

```text
Breaking the Ice

As a mature adult, I feel an obligation to help the younger generation, just as the mother fish guards her unhatched eggs, keeping her lonely vigil day after day, never leaving her post, not even to go to the bathroom, until her tiny babies emerge and she is able, at last, to eat them. “She may be your mom, but she’s still a fish” is a wisdom nugget that I would pass along to any fish eggs *who are listening in* But today I want to talk about dating. This subject was raised in a letter to me from a young person named Eric Nott, who writes: I have got a big problem There’s this girl in my English class who is really good-looking. However, I don’t think she knows I exist. I want to ask her out, but I’m afraid she will say no, and I will be the freak of the week. What should I do? Eric, you have sent your question to the right mature adult, because as a young person I spent a lot of time thinking about this very problem. Starting in about eighth grade, my time was divided as follows: Academic Pursuits: 2 percent. Zits: 16 percent. Trying to Figure Out How to Ask Girls Out: 82 percent. The most sensible way to ask a girl out is to walk directly up to her on foot and say, “So, you want to go out? Or what?” I never did this. I knew, as Eric Knott knows, that there was always the possibility that the girl would say no, thereby leaving me with no viable option but to leave Harold C. Crittenden Junior High School forever and go into the woods and become a bark-eating hermit whose only companions would be the gentle and understanding woodland creatures. “Hey, ZITFACE!” the woodland creatures would shriek in cute little Chip ‘n’ Dale voices while raining acorns down upon my head. “You wanna DATE? HAHAHAHAHAHAHA.” So the first rule of dating is: Never risk direct contact with the girl in question. Your role model should be the nuclear submarine, gliding silently beneath the ocean surface, tracking an enemy target that does not even begin to suspect that the submarine would like to date it. I spent the vast majority of 1960 keeping a girl named Judy under surveillance, maintaining a minimum distance of 50 lockers to avoid the danger that I might somehow get into a conversation with her, which could have led to disaster:

JUDY: Hi.

ME: Hi.

JUDY: Just in case you have ever thought about having a date with me, the answer is no.

WOODLAND CREATURES: HAHAHAHAHAHA. The only problem with the nuclear-submarine technique is that it’s difficult to get a date with a girl who has never, technically, been asked. This is why you need Phil Grant. Phil was a friend of mine who had the ability to talk to girls. It was a mysterious superhuman power he had, comparable to X-ray vision. So, after several thousand house of intense discussion and planning with me, Phil approached a girl he know named Nancy, who approached a girl named Sandy, who was a direct personal friend of Judy’s and who passed the word back to Phil via Nancy that Judy would be willing to go on a date with me. This procedure protected me from direct humiliation, similar to the way President Reagan was protected from direct involvement in the Iran-contra scandal by a complex White House chain of command that at one point, investigators now believe, included his horse. Thus it was that, finally, Judy and I went on an actual date, to see a movie in White Plains, New York. If I were to sum up the romantic ambience of this date in four words, those words would be: “My mother was driving.” This made for an extremely quiet drive, because my mother, realizing that her presence was hideously embarrassing, had to pretend she wasn’t there. If it had been legal, I think she would have got out and sprinted alongside the car, steering through the window. Judy and I, sitting in the backseat about 75 feet apart, were also silent, unable to communicate without the assistance of Phil, Nancy, and Sandy. After what seemed like several years we got to the movie theater, where my mother went off to sit in the Parents and Lepers Section. The movie was called North to Alaska, but I can tell you nothing else about it because I spent the whole time wondering whether it would be necessary to amputate my right arm, which was not getting any blood flow as a result of being perched for two hours like a petrified snake on the back of Judy’s seat exactly one molecule away from physical contact. So it was definitely a fun first date, featuring all the relaxed spontaneity of a real-estate closing, and in later years I did regain some feeling in my arm. My point, Eric Knott, is that the key to successful dating is self-confidence. I bet that good-looking girl in your English class would LOVE to go out with you. But YOU have to make the first move. So just do it! Pick up that phone! Call Phil Grant. TRANSITION But Mr. Barry’s “Dear Abby” columns helped a much wider audience than hormonal teen-agers, he also responded to their confused and often disgruntled parents with equally insightful commentary like, You’ve Got to be Kidding!

You’ve Got to Be Kidding Today’s scary topic for parents is: What Your Children Do When You’re Not Home. I have here a letter from Buffalo, New York, from working mom Judy Price, concerning her 14-year-old son, David, “Who should certainly know better, because the school keeps telling me he is a genius, but I have not seen signs of this in our normal, everyday life.” Judy states that one day when she came home from work, David met her outside and said: “Hi, Mom, Are you going in?” (This is a bad sign, parents.) Judy says she considered replying, “No, I thought I’d just stay here in the car all night and pull away for work in the morning” That actually would have been a wise idea. Instead, she went inside, where she found a large black circle burned into the middle of her kitchen counter. “DAVID,” she screamed. “WHAT WERE YOU COOKING?” The soft, timid reply came back: “A baseball,.” “A baseball,” Judy writes. “Of course. What else could it be? How could I forget to tell my children never to cook a baseball? It’s my fault, really.” It turns out that according to David’s best friend’s cousin – and if you can’t believe HIM, who CAN you believe? – you can hit a baseball three times as far if you really heat it up first. So David did this, and naturally he put the red-hot pan down directly onto the countertop, probably because there was no rare antique furniture available. For the record: David claims that the heated baseball did, in fact, go farther. But this does NOT mean that *any young people listening* should try this foolish and dangerous experiment at home. Use a friend’s home. No, seriously, you young people should never heat a baseball without proper adult supervision, just as you should never – and I say this from personal experience – attempt to make a rumba box. A rumba box is an obscure musical instrument that consists of a wooden box with metal strips attached to it in such a way that when you pluck them, the box resonates with a pleasant rhythmic sound. The only time I ever saw a rumba box was in 1964, when a friend of my parents named Walter Karl played one at a gathering at our house, and it sounded great. Mr. Karl explained that the metal strips were actually pieces of the spring from an old-fashioned wind-up phonograph. This gave my best frined, Lanny Watts, an idea. Lanny was always having ideas. For example, one day he got tired of walking to the end of his driveway to get the mail, so he had the idea of hanging the mailbox from a rope-and-pully system strung up the driveway to his porch, where he hooked it up to a washing-machine motor. When the mailman came, Lanny simply plugged in the motor, and whoosh, the mailbox fell down. The amount of time Lanny spent unsuccessfully trying to get this labor-saving device to work was equivalent to approximately 5,000 trips to get the actual mail, but that is the price of convenience. So anyway, when Lanny heard Mr. Karl explain the rumba box, he realized two things: 1. His parents had an old-fashioned wind-up phonograph they hardly ever used. 2. They both worked out of the home. So Lanny and I decided to make our own rumba box. Our plan, as I recall it, was to take the phonograph apart, snip off a bit of the spring, then put the phonograph back together, and nobody would be the wiser. This plan worked perfectly until we removed the metal box that held the phonograph spring; this box turned out to be very hard to open. “Why would they make it so strong?” we asked ourselves. Finally, recalling the lessons we had learned about mechanical advantage in high-school physics class, we decided to hit the box with a sledge hammer. Do you remember the climactic scene in the movie Raiders of the Lost Ark, when the Nazis open up the Ark of the Covenant and out surges a terrifying horde of evil fury, and the Nazis’ heads melt like chocolate bunnies in a microwave? Well, that’s similar to what happened when Larry sledge-hammered the spring box. It turns out that the reason the box is so strong is that there is a really powerful, tightly wound, extremely irritable spring in there, and when you let it out, it just goes berserk, writhing and snarling and thrashing violently all over the room, seeking to gain revenge on all the people who have cranked it over the years.

Lanny and I fled the room until the spring calmed down. When we returned, we found phonograph parts spread all over the room, mixed in with approximately 2.4 miles of spring. We realized we’d have to modify our Project Goal slightly, from making a rumba box to being in an entirely new continent when Lanny’s mom got home. Actually, Mrs. Watts went fairly easy on us, just as Judy Price seems to have been good-humored about her son’s heating the baseball. Moms are usually pretty good that way. But sometimes I wonder. You know how guys are always complaining that they used to have a baseball-card collection that would be worth a fortune today if they still had it, but their moms threw it out? And the guys always say, “mom just didn’t know any better.” Well, I wonder if the moms knew exactly what they were doing. Getting Even.
```

---

## IC-2391: A Brief Moment in the Life of Angus Bethune

- Title: A Brief Moment in the Life of Angus Bethune
- Author (byline): Chris Crutcher
- Work: Prejudice: Stories about Hate, Ignorance . . .
- Publisher: Hyperion Press
- Publication date as stated: Sept 1998
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2578
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chris Crutcher
Book: Prejudice: Stories about Hate, Ignorance . . .
ISBN: 978-0786813100
Publisher: Hyperion Press
Date (Month/Year): Sept 1998
```

### Introduction (context only: never use it for content warnings)

```text
According to the U.S. Department of Education, approximately 160,000 students a day stay home from school because they are afraid of being bullied. That's over 3 million a month. And the highest percentage of bullying is directed toward overweight students. Options: avoid the situation, or learn to take daily verbal and sometimes physical abuse. But if your name is Angus and you have two sets of gay parents . . . that’s only the beginning. A Brief Moment in the Life of Angus Bethune by Chris Crutcher
```

### Performance text (classify this)

```text
While farsighted parents of other infants my age were pre-enrolling their kids four years ahead into elite preschools, my dad was hounding the World Wrestling Federation to hold a spot for me sometime in the early 1990s. I mean, my mom had to go to the husky section of Safeway to buy me Pampers. I’m a big kid. And they named me Angus. God!

Sometimes, when I stand back and take a good look, I think my parents are ambassadors from hell. Two of them, at least, the biological ones, the big ones. Four parents are what I have altogether, not unlike a whole lot of other kids. But quite unlike a whole lot of other kids, there ain’t a hetero among ‘em. My dad’s divorced and remarried, and my mom’s divorced and remarried, so my mathematical account of my family suggests simply another confused teenager from a broken home. But my dads aren’t married to my moms. They’re married to each other. Same with my moms.

That frightening little off-season trade took place prior to – though not much prior to – my birth, so until I began collecting expert feedback from friends at school, somewhere along about fourth grade, I perceived my situation as relatively normal.

No, what really hacks me off is that when people the size of my parents decide to reproduce, they usually dig a pit and crawl down in there together for several days. Really, I’m surprised someone in this family doesn’t have a trunk. Or a blowhole. I swear my gestation period was three years and seven months.

“Angus is a cow,” I said to my mother when she got home from her job at Westhead Trucking firm. “You guys named me after a cow.”

“Your father’s uncle was named Angus,” she said.

“So my father’s uncle was named after a cow, too,” I said. “What did he think of that?”

“Actually,” Mom said, “I think he was kind of proud. Angus was quite a farmer, you know.”

“Jesus help me,” I said, and went to my room.

As Angus, the fat kid with perverted parents, I’ve had my share of adjustment problems, though it isn’t as bad as it sounds. I am incredibly quick for a fat kid, and I have world-class reflexes. Plus you don’t have to dig too deep in our ancestral remains to find an IQ safely into three digits, so grades come pretty easy to me. But I’d sure be willing to go into the winter trade meetings and swap reflexes, biceps, and brain cells, lock, stock, and barrel, for a little physical beauty.

Which brings me to tonight. Tonight is a big night, and I don’t want the blubbery bogeyman or the phantoms of sexual perversity, who usually pop up to point me out for public mockery, mucking it up for me. I want normal. I want socially acceptable. See, I was elected Senior Winter Ball King, which means for about one minute I’ll be featured gliding across the floor beneath the crimson and gold crepe paper streamers at lake Michigan High School with Melissa Lefevre, the girl of my dreams – and only my dreams – who was elected Senior Winter Ball Queen. For that minute we’ll be out there alone. Alone with Melissa Lefevre.

I mean, it’s a joke, I know that. I just don’t know whose. It’s a hell of a good one, though, because someone had to coax a plurality of more than five hundred seniors to forgo casting their ballots for any of a number of bona fide Adonises to write in the name of a cow. At first I tried to turn it down, but Granddad let me know right quick I’d draw a lot more attention if I made a fuss than if I acted as if I were the logical choice – indeed, the only choice – and went right along.

Granddad is the man who taught me to be a dignified fat kid. “Always remember these words, and live by ‘em,” he said after my third suspension from kindergarten for fighting. “Screw ‘em. Anybody doesn’t like the way you look, screw ‘em.”

And that’s just what I’ve done. Sometimes I’ve screwed ‘em by punching them in the nose, and sometimes by walking away. And sometimes by joining them – you know, laughing at myself. That’s the one that works best. So you see, slowly but surely I’m getting all this under control. I don’t mind that my detractors will wonder aloud tonight whether it is Melissa or I who is the Winter Ball Queen, a playful reference to my folks’ quirky preferences, and I don’t mind that I’ll likely hear, “Why do they just swim up on the beach like that?” at least three times. What I mind is that during those few seconds when Melissa and I have the floor to ourselves, all those kids, will be watching me dance. Now, I’ve chronicled the majority of my maladies here, but none remotely approaches my altogether bankrupt sense of rhythm. When it comes to clapping his hands or stomping his feet to the beat, Angus Bethune is completely, absolutely, and, most of all, irreversibly brain dead.

I’ve known about the dance for three weeks now. I even know the name of the song, though I don’t recognize it, and I went out and spent hard-earned money on dance lessons, [But] I’ve been planning for Melissa Lefevre for a long time. I fell in love with her in kindergarten, when she dared a kid named Alex Immergluck to stick his tongue on a car bumper in minus-thirty-five-degree weather for calling her a “big, fat, snot-nosed deadbeat.” Being a fat kid, I was interested in all the creative retaliatory methods I could get to store in the old computer for later use, and when I saw the patch of Alex’s tongue stuck tight to the bumper as he screamed down the street, holding his bleeding mouth, I knew I was in the company of genius.

The bottom line, though, [is] I would never have the opportunity for any conversation with Melissa other than one in my head. Until tonight. Tonight I’ll have to talk to her. If I don’t, she’ll have only my dancing by which to remember me, which is like Mrs. Fudd remembering Elmer for his hair. It’d be a damn shame. All I really want is my moment with her. All I want is my moment.

So now I stand at the door to the gym. Heads turn as I move through the door. I see Melissa on the dance floor with her boyfriend – a real jerk in my book, Rick Sanford – and my heart bursts against the walls of my chest, like in Alien. I order it back. A sophomore server leaves a glass of punch on the table, and I sip it slowly through the next song, after which the lead singer announces that the “royal couple” and their court are due behind the stage curtain in five minutes. Tributaries of perspiration join at my rib cage to form a raging torrent of sweat rushing toward my shoes as I silently hyperventilate, listening for my grandfather’s voice, telling me to screw ‘em, telling me once again I can do anything I want. I want my moment.

I want to run. What am I doing here? What was I thinking of? Suddenly I’d give up my moment in a heartbeat for the right to disappear. What a fool, even to think…

They stand before me. [Rick and Melissa] Melissa smiles. She says, “Hi.” I smile and nod, any words far, far from my throat. Melissa says, “Why don’t we go on up?” and she takes my arm, leaving Rick’s hanging limply at his side.

“Yeah,” he says, “why don’t you go on up? You right on up behind that curtain with my girl, snowball king.”

Melissa drops my arm and grips his elbow. “Shut up,” she whispers between her clenched teeth. “I’m warning you, Rick. Shut up.”

Rick tears his arm away. “Enjoy yourself,” he says to me, ignoring her. “Your campaign cost me a lot of money, probably close to two bucks a pound.” He looks me up and down as couples at the nearest tables turn to stare. The heat of humiliation floods up through my collar, and I fear the worst will follow. I fear I’ll cry.

Melissa takes my arm again and says, “Let’s go.” We move two steps toward the stage, and Rick says loud, “Got your rubber gloves, honey?”

“What do you mean by that?” I ask quietly, knowing full well what he means by that.

“I wasn’t talking to you, bigfoot,” Rick says, looking past me to his girl. “I’m asking if my sweetie’s got her rubber gloves.”

Melissa says, “I hate you, Rick. I really do.”

Rick ignores her. “Bigfoot comes from a high-risk home,” he says. “Best wear your rubber gloves, honey, in case he has a cut.”

In that instant I sweep his feet with mine, and he lands hard on the floor. He moves to get up, but I’m over him, crowding. When he tries to push himself up, I kick his hands out, following his next movements like a cow dog, mirroring him perfectly, trapping him there on the floor. No chaperone is in view, so it isn’t totally out of hand yet. When he sees he can’t rise, I kneel, sweat pouring off my forehead like rain. Softly, very softly, I say, “You may not like how my parents live. But they’ve been together since 1971 – monogamous as the day is long. That’s a low-risk group, Rick. The only person at high risk right now is you.”

He looks into my eyes, and he knows I mean it, knows I’m past caring about my embarrassment. “Okay, man,” he says, raising his hands in surrender. “Just having a little fun.”

I’m apologizing to Melissa all the way up the backstage stairs, but she’s not having any. “You should have stomped on his throat,” she says, and I involuntarily visualize Alex Immergluck clutching at his bleeding mouth in the freezing cold next to the car bumper. “If you ever get another chance, I’ll pay you money.”

At the side door to the stage I say, “Speaking of embarrassment, there’s something you need to know.” She waits. “I can’t dance.”

Melissa smiles. She says. “We’ll survive.”

I say, “Yeah, well, I didn’t say I can’t dance well. I said I can’t dance. Good people have been badly hurt trying to dance with me.” We take our places. The darkness of the stage and the silence are excruciating. The curtains part as the trumpets blare. I gaze out into the spotlights, smiling like a giant. The introduction of last year’s king and queen begins, and they move toward us from stage left and right to relinquish their crowns to us. It all would be unbelievably ridiculous even if they weren’t crowning King Angus the Fat. Without moving her lips, Melissa says, “I picked a slow song. We don’t have to move much. Dance close to me. When you feel me lean, you lean. Whatever you do, don’t listen to the music. It’ll just mess you up. Trust me. My brother’s like you. Just follow.”

A part of me stays to concentrate, but another part goes to heaven. In my wildest dreams I could never have imagined Melissa Lefevre being nice to me in my moment, would never have dared imagine holding her tight without feeling pushy and ugly and way out of line. Feeling greedy now, I want my moment to last.

“Angus? “Do you ever get tired of who you are?”

I pull back a second, but it’s like Lois Lane releasing Superman’s hand twenty thousand feet in the air. She falls. I pull close again. “Do you know who you’re talking to?”

I feel her smile. “Yeah,” she says, “I thought so. I know it’s not the same, but it’s not always so great looking the way I do, either. I pay, too.” She’s right. I think it’s not the same.

“Want to know something about me?” she asks. “I’m bulimic. Do you know what that is?”

I smile. “I’m a fat kid with faggot parents who’s been in therapy on and off for eighteen years,” I say. “Yes, I know what that is. It means when you eat too much, you chuck it up so you don’t turn out to look like me.”

“Close enough for discussion purposes. Don’t worry, I’m in therapy for it,” she says, noticing my concern. “A lot of pretty girls are.”

“Actually,” I say, “I even tried it once, but when I stuck my finger down my throat, I was still hungry and I almost ate my arm.”

Melissa laughs and holds me tighter. “You’re the only person I’ve ever told except for the people in my therapy group; I just wanted you to know things aren’t always as they appear. Would you do me a favor?”

“If it doesn’t involve more than giving up my life,” I say, feeling wonderful because Melissa isn’t a goddess anymore and because that doesn’t change a thing about the way I feel about her.

“Would you leave with me? I like how you stood up for your family. It must be hard. Defending them all the time, I mean.”

“Compared to me, a boy named Sue had it made,” I say.

The music ends; all dancers stop and clap politely. “I want to dance one more,” Melissa says. “A fast one.”

“I’ll wait over by the table.”

“No. I want to dance it with you.”

“You don’t understand,” I say. “When I dance to the beat of rock and roll, decent folks across this great land quake in their boots.”

She holds my hand tightly. “Listen. Do what you did when you wouldn’t let Rick up. Don’t listen to the music; just follow me the way you followed him.”

I try to protest; but the band breaks into “Bad Moon Rising,” and the dance floor erupts. I back away as she comes at me, mirroring her every move, top to bottom. A crowd gathers and I’m trapped inside a cheering circle, actually performing the unheard of: I’m Angus Bethune, Fat Man Extraordinaire, dancing in the limelight with Melissa Lefevre, stepping outside the oppressive prison of my body to fly to the beat of Credence Clearwater Revival.

When the drummer bangs the last beat, the circle erupts in celebration, and I take a long, low bow. Melissa is clapping wildly.

Rick yells at the door as I help Melissa into her coat. “You practiced with this tub of lard! You guys were getting together dancing. You set me up.” He turns to me. “I ought to take you out, fat boy,” he says, but his unimaginative description can’t touch my glory.

I put up a finger and wag it side to side in front of his nose. “You know the difference between you and me, Sanford?”

He says, “There are a lot of differences between us, lardo. You couldn’t count the differences between us.”

“That’s probably true,” I say, closing my fist under his nose. “But the one that matters right now is that I can make you ugly.”

He stares silently at my fist.

I say, “Don’t even think it. Next to dancing, that’s my strong suit.”
```

---

## IC-2392: The Burn Journals

- Title: The Burn Journals
- Author (byline): Brent Runyon
- Work: Not specified
- Publisher: Vintage
- Publication date as stated: Oct 2005
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2353
- Already set (do not supply): none

### Source block (context only)

```text
Author: Brent Runyon
ISBN: 978-1400096428
Publisher: Vintage
Date (Month/Year): Oct 2005
```

### Introduction (context only: never use it for content warnings)

```text
One February day in 1991, Runyon came home from eighth grade, had a snack, soaked his full-length bathrobe in gasoline, and set himself on fire. He intended to kill himself. But Brent was not successful . . . instead he survived to suffer the pain of burns to 85 percent of his body. What made a smart, popular, funny, loving boy try to take his own life? Depression, a chemical imbalance? I don’t have the answers and neither does Brent Runyon, but the following excerpts from The Burn Journals tries to explain what happened before, during and after the horrendous “accident.”
```

### Performance text (classify this)

```text
When we moved here, the first thing they did was start testing me to see how smart I was. I didn’t even have time to make any friends before they put me in this program for smart kids called GT, which stands for Gifted and Talented. I started calling it Goobers and Twerps because all of the kids that were in it were real dorks. None of the cool kids were in it. None. Well, one, if you count me. I started begging my parents to let me out of the program because it was so stupid. I kept begging and begging, and then, finally, this year, they let me out of GT, and for some reason I started doing really badly. Now I’m getting F’s in a couple of classes.

I’m awake, listening to the radio, and Mom is yelling at me to get out of bed. I don’t want to get out of bed. I don’t want to go to school. Maybe I should play sick, but I’ve done that too many times this year already.

I run the whole thing back in my head. I did so many things wrong, I can’t even believe it. I shouldn’t have taken the matches from Adam. I shouldn’t have set the whole pack on fire. I shouldn’t have thrown them into that locker. And I really shouldn’t have put that lock on the locker.

When I walk into gym, Mr. Huff is standing in the back of the locker room, right next to the locker that was on fire. He says, “Okay, boys, settle down. Some arsonist among you purposefully set a shirt on fire. Boys, whoever did this is in an enormous amount of trouble. Charges will be pressed. He’ll be expelled. So whoever did it, or if you know who did it, come see me in my office before the end of the period.” His eyes lock with mine on the last word and I feel a cold sickness all over my body, but somehow I manage to keep my eyes from showing that I know he knows it’s me.

What am I going to do? What am I going to do? . . . I’m going to kill myself.

I think about that movie we saw in English class, about the guy who’s standing on the bridge waiting to get hung. As soon as the rope snaps his head back, he’s dead.

I wonder why all the ways I’ve tried to kill myself haven’t worked. I mean, I’ve tried hanging. I used to have a noose tied to my closet pole. I’d go in there and slip the thing over my head and let my weight go. But every time I started to lose consciousness, I’d just stand up.

I tried to take pills. One afternoon, I took twenty Advil, but that just made me sleepy.

And all the times I tried to cut my wrists, I could never cut deep enough. I took my knife from its hiding place between the mattress and the box spring and held it against my wrist. I sliced as fast as I could and bit my lip from the pain. I hung my arm between the two twin beds pushed together from when my brother used to share the room with me and let it bleed. I was surprised when I work up in the morning. I had to find a Band-Aid big enough to cover the wound and told my parents I’d scratched my wrist on a locker.

That’s the thing – your body tries to keep you alive no matter what you do. I’ve got to think of a way to kill myself that I can’t turn back from.

When seventh period is finally over, I run to my locker and put all my books inside. I won’t need them anymore. Laura walks with me down D hall. She says, “Hey, I heard you set that fire in gym class.”

“Yeah.”

“What are you going to do?”

“I’m going to set myself on fire.” She stops at her locker and I keep walking.

On the bus ride home, I sit by myself. I lean my head against the cold glass window and try not to think about all the stupid things I’ve done, all the bad things I’ve done, and all the pain I’ve caused everyone.

My brother is playing basketball outside the house when I get home. I rebound the ball for him and throw it back. I tell him the whole story, about what I did and what they’re going to do to me. I don’t tell him what I’m going to do to myself.

When I’m done talking, he says, “That sucks,” and I go inside the house. I don’t have to write a note anymore. Craig knows everything.

I walk out to the shed to get the gas can. I bring it inside to the bathroom at the top of the stairs because that’s the room with the most locks. I go back downstairs and get the matches from the kitchen.

I take off all my clothes and put on the pair of red boxers that my mom bought for me at the mall last weekend. I bring my bathrobe into the shower and I pour the gasoline all over it. The gas can is only about a quarter full, but it seems like enough.

I step into the bathtub and I put the bathrobe over my shoulders. It’s wet and heavy, but there’s something kind of comforting about the smell, like going on a long car trip. I hold the box of matches out in front of me in my left hand.

I take out a strike-anywhere match and hold it against the box.

Should I do it? . . . Yes. Do it.

I strike the match, but it doesn’t light. Try again.

I light the match. Nothing happens. I bring it closer to my wrist and then it goes up, all over me, eating through me everywhere. I can’t breathe. I’m screaming, “Craig! Craig!”

I fall down. I’m going to die. I’m going to find out what death is like. I’m going to know. But nothing’s happening.

This hurts too much. I need to stop it. I need to get up. I stand. I don’t know how I stand, but I do, and I turn on the shower. I’m breathing water and smoke. I unlock the door and open it. My hand is all black. I walk out. There’s Craig with Rusty, or dog, next to him. They have the same expression on their faces.

Craig yells something and runs downstairs. I think he’s calling 911. I’m following him. He hands me the phone and runs off. There’s a woman on the phone asking me questions. I try to tell her what’s happened, but my voice sounds choked and brittle. There’s something wrong with my voice.

The woman on the phone says the fire trucks and ambulances are on their way. Somehow she knows my address. Craig is gone now, gone to get Mom, and Rusty is hiding somewhere. Smoke is coming from the bathroom upstairs and I can see that the whole room has turned black. I look down and see my flesh is charred and flaking and the boxer shorts are burnt into my skin

The woman on the phone says everything is going to be all right, and I believe her. She keeps asking me if I’m still on fire and I say, “I don’t think so.”

I’m walking around the kitchen, waiting for the ambulance to come. I can see my reflection in the microwave. Where’s my hair? Where did my hair go? Is that my face?

We used to put marshmallows in the microwave. We used to watch them get bigger and bigger and then shrink down . “Oh god, just tell them to get here, just tell them to get here, okay? I’m so sorry. I’m so sorry.”

I can hear the sirens in the distance now . . . Then the firemen are here. They’re putting me on a plastic sheet. They say I’m going to be okay. One of them puts something over my face. That feels good. That feels so good. The cold air feels so good going into my lungs

What are they talking about? What are they saying? They’re giving me a shot They say it’s going to make the pain go away. Make the pain go away.

I’m looking at the faces of all the men who are gathered around me. Their eyes are so blue and so clear.

I turn my head and see Craig in the front hall. He’s yelling and punching the walls. He’s angry

And my mom is here, and she’s smiling and saying she loves me, and her eyes, which are green like my eyes, are the most beautiful things I’ve ever seen.

I don’t want to die anymore. I hope Craig can love me again.

**************

I’ve been [at the burn center] for exactly one month.

Mom sits by my bedside and I can tell that she wants to talk about the fire and everything about it. So I start by trying to say why I was so sad, and how I thought that the principal was going to expel me and how I didn’t want them to be mad at me because they both wanted me to be so smart and I’m sorry I couldn’t be what you wanted. And she says, “You are everything we wanted.” And we both cry together.

“Mom, no one’s ever going to love me, are they?”

But mom puts her hand on my fingertips and whispers, “Brent, listen to me, honey, you are so smart and so kind. You will fall in love, and someone will fall in love with you. I promise.”

It makes me feel better to hear her say that, but I can tell that she’s not really sure. It’ll be okay, I tell myself, I can live in the basement when I get older so people don’t have to look at me. I’m crying and crying. I want her to go away and leave me alone.

**************

People here like to talk to me about Pain Management. They ask me to rate my pain on a scale of one to ten. One being the least painful and ten being the most. I don’t think they have a number for some of the pain I’m going through. I don’t think they even have a number.

I keep thinking about it. I was in the bathroom and I had the gas can and the matches and I sat on the toilet. That’s when I should’ve realized how stupid I was being. That’s when I should’ve stopped it.

But I stood in the bathroom and put the bathrobe on, and it was wet and heavy, and I could have taken it off and gone back outside to play basketball with Carig and said, You won’t believe what I almost did. And he would’ve known what to do. He would’ve gotten me help and made that Mom and Dad weren’t made at me. I should’ve done that.

I wish, I wish, I wish, I wish, I wish I’d stopped. But I didn’t.

********************

Mom is here and she looks like she’s ready to talk. If I just say it, then maybe I’ll be able to stop feeling so bad inside. I’ll say, Hey Mom, guess who tried to kill themselves a bunch of other times besides the one you know about? That’s right, me. Hey, Mom, remember the Band-Aids on my wrist? Well, I didn’t really scrape it on my locker. I cut it with a knife that I kept under my bed. . . . And you know the furnace in the basement, I thought about pouring gasoline in there and blowing up the whole house . . . And you know how I got the book on how to make knots? It was so I could tie a noose and hang myself from the closet pole.

I can’t say any of this. So I say, “Mom . . . when I . . . . when I tried . . . to hurt myself before . . . that wasn’t the first time that I tried to do something like that.”

She doesn’t look surprised, but she’s starting to cry. She puts her hand on top of mine. I know, honey. I figured it wasn’t the first time. I’m sorry I didn’t know you were so sad.” She’s crying hard now, and I’m crying too.

“I know. I’m sorry, Mom.”

“Brenny?” she says. “About a week before your accident . . . .

An accidental house fire. Right. Okay. Okay. We can say that. We don’t have to tell anyone what really happened. An accidental house fire.

“. . . . we got into a fright at the dinner table and you stormed up to your room, and I remember, I said, “Where are you going?” and you said, I think I heard you say, “I’m going to set myself on fire.”

I think about it. “I don’t think I said that. I mean, I might have, but I didn’t mean it.”

She can hardly get the words out, she’s crying so hard. “But if you ever get that sad again, you have to promise to tell someone so they can help you . . . And know that we love you so much and we don’t ever want to lose you.”

********************

It’s been nine months and I still don’t know why I did it. I was so sad. I wanted to be funny and cool and I wanted everyone to love me, but I still don’t know why I did it. [Once I was home] we never mentioned my suicide attempt or my time in the hospital – my parents still call it an accident. To them, the entire thing was a mystery they’d given up on solving.

But as I talked to more people, I realized that the only thing unique about my story is the rather unfortunate and dramatic way in which I tried to kill myself. Other than that, I’m just another guy with a history of depression, which is somehow very comforting to me . . .
```

---

## IC-2393: The Button

- Title: The Button
- Author (byline): Robert Newman
- Work: Not specified
- Publisher: Originally Published by Wetmore Declamation Bureau (no longer in business)
- Publication date as stated: 1949
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: JOE, DR. TREVOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1146
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Newman
ISBN: 978-1600451157
Publisher: Originally Published by Wetmore
Declamation Bureau (no longer in business)
Date (Month/Year): 1949
```

### Introduction (context only: never use it for content warnings)

```text
In the choking blackness of solitary confinement, Joe Ransom teeters on the brink of madness. A single match, a drifting spider, a worthless white button become his last defenses against the terror. He devises a simple game to protect his sanity. Will the game work or will the button prove to be his downfall?

The Button by Robert Newman
```

### Performance text (classify this)

```text
The scene is a solitary confinement cell in a large American prison. It is a stone-walled room about six feet square and in it, a hard cot, no other object of any kind. The room is in absolute darkness. On the cot sits a prisoner, Joe Ransom, about forty years of age. He is in solitary after a prison riot in which another convict has been murdered. His head in his hands, he sits and rocks from side to side on the cot; the springs creak with every move. Suddenly he stops swaying, lifts his head and listens. Far away an iron door opens.

JOE: Warden! Warden! I knew you’d come. Warden, listen -- listen to me. Listen, Warden, you gotta take me out of here. You gotta, see? I’m goin’ nuts. I can’t stand it, Warden, I’m goin’ nuts!

Look, look, Warden, I’ll tell you what I’ll do, see. I’ll confess. Get me a pencil and paper and for a little light and I’ll write out a confession. Then you can take me out and hang me. I’ll confess see –Warden! (shouts) Warden, are you listenin’? I tell you I killed him. I killed him. I KILLED HIM!

JOE: All right. All right. I’ll be calm, see -- Calm an’ quite, so’s you’ll know I mean what I’m sayin’. Listen: I, Joe Ransom killed my cellmate, Mike Malari. I did it. An’ I’ll tell you why, Warden. It was his eyes. He used to sit there starin’ at me. The guards wouldn’t put me in another cell. They just laughed, Warden. Thought it was funny, they did, him starin’ at me like that. Five years, Warden, five years I stood it. Five years I stood those eyes. Then I killed him. That night when hell broke loose in the block an’ everybody was fightin’ back and forth in the corridor, I killed him. It was him or me, Warden, him or me -- So I squeezed his throat, ‘till I knew he wouldn’t stare at me no more. There, Warden, I confessed. Now hang me -- do anything to me -- only take me out of this hole. I’m afraid, Warden, I’m afraid of bein’ alone in this dark -- I start seein’ things -- I start seein’ Mike’s eyes again!

(shouts)

Warden! Take me out! Open this door! Take me out! Take me out! Take me out! (pause, silence, then almost timidly) Warden!

Gone! He’s gone! He’s gone and left me here! In the dark. Pitch dark. Ssssh! What’s that! Something movin’! Up there. Up there in the corner. Mike! No, no, it can’t be Mike, or you could see his eyes. Take it easy now. The match. . . the one match you saved. Don’t tremble! So, light it! (strikes the match and then reacts) A spider! It’s a spider! He’s weaving a web. He’s weaving a web to catch flies! You fool, spider, you fool! There’s no flies here. There’s nothin’ here except me. Me! Why don’t you catch me in your web, spider? Why don’t you catch me? I’ll sit down and watch you. You’re weaving, spider, back and forth, back and forth, back and forth. (mesmerized) Look, I can do that too. Back and forth, back and forth, back and forth, back and forth, back and forth, back and forth, the spider and I, back forth . . .

Stop it! Stop it, you hear Joe Ransom. You’ll go nuts that way! Nuts, crazy, mad! Stop it!

What are you going to do? What are you going to do?

What was that? I heard something. I heard something drop. What was it? A button! A button came off my jacket. Here it is. Little button. White button. What do I want it for? What good can it do me? I’ll throw it away. (tosses the button) Throw it away like I threw my life away.

Now it’s gone. Gone like my life. Like everything. (beat) No, its not gone. It’s still here. Here in this cell some place. I heard it. I heard it. I heard it drop. I threw it away like my life, like everything, but it’s still here, here in the cell!

(determined) I’ve got to find it. I’ve got to find it, you hear? It means something! Now where is it? Where? I heard it hit the wall and then the floor. Is it under . . . (looks under the cot) Here it is! Here it is, the little button. I found it. It means something. I know. It’s a game! I play the game and it keeps me from thinkin’. It makes me tired and then I can sleep. Sleep! And not see Mike’s eyes. This is it! I’m saved! Saved! Play it again. Close your eyes.

Now throw! This side. It went over there. No! Further to the left. There it is. This is it! This’ll save me! I was a sucker to shoot off my mouth to the Warden like that. Well, it wasn’t in writing, that was one good thing! I’ll have to get hold of a mouthpiece right away, there must be something . . . (long beat) Insanity! That’s it. Pull the nut act! Boy, oh boy, oh boy, I’m saved!

The button! The button, you fool! Throw the button. Play that game! Throw! Over here. No. over further. That was near the other side. Near the door. No. Here? No. Where? Where? Oh, here it is! What would happen if I couldn’t find it? What would happen in a little stone cell? Where could it get lost? Play! Throw the button!

That was near the bed. No nearer the middle – there! But if it did get lost? Stop it! It can’t get lost! Play the game. Play and forget! Shut your eyes. Put your arm back and throw!

(he slowly descends into madness) Throw? I threw. I threw the button. I threw the button, but I didn’t hear it hit. I threw and it didn’t hit. I didn’t hear it hit anything. All I can hear is my heart beating, beating, beating. Pounding -- pounding in my ears.

I threw the button and now it’s gone. It didn’t hit the walls, the floor, anything. I threw and it disappeared. It’s gone! Gone! Where is it? What happened? I threw and it’s, its gone! Something grabbed it! Something . . .

(terrified) Mike! Mike! Stop staring! Stop staring at me! Mike! Don’t! Don’t, Mike! Don’t touch me, Mike!

******

DR. TREVOR: (on the phone) Hello, hello. Yes, operator, get me the Warden’s office. Hello, Warden? This is Dr.Trevor. (beat) Yes, I’m down in the solitary confinement wing. (beat) Yes. Yes, I examined him. (beat) No. I had him sent away. (beat) Yes.

Completely, hopelessly mad. (beat) No, not a chance. His mind’s gone. (beat) What caused it? Hard to say, sudden terrific shock or an emotional blow. Solitary confinement is a strain on the best of them. (beat) No, that’s all. Oh, yes, one thing, very curious. I looked around the cell after he was taken away, there was a spider web in one corner. (beat) Yes, I said spider’s web. And in the spider’s web was a button - a little white button. Odd, isn’t it.
```

---

## IC-2394: Not specified

- Title: Not specified
- Author (byline): the Dawn’s Early Light
- Work: Not specified
- Publisher: Ahmadiyya Movement In Islam
- Publication date as stated: Jun 2009
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1491
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ahmad Nurudddin
ISBN: 978-1882494255
Publisher: Ahmadiyya Movement In Islam
Date (Month/Year): Jun 2009
```

### Introduction (context only: never use it for content warnings)

```text
Black, white, and Latino—Americans from every race and religion are increasingly accepting and converting to Islam. Why, you ask? Aren’t the radical extremists who are terrorizing our world a part of the Islamic faith? The answer is yes, but just like any religion, there are fanatics who go overboard. Look at Fred Phelps, and the intolerant image he presents of Christianity -- Is that what Christianity is? No more than the acts of terrorists define the religion of Islam. And at a time when our nation is seeing a rise in intolerant behavior, crossing every cultural line, whether based on race, religion or sexual orientation, Islam teaches tolerance, justice and honor, and promotes patience, modesty and balance. By the Dawn's Early Light, presents forty engaging autobiographical essays by American converts to Islam, and helps to explain why. This is the story of Noel Durham (also known as Ahmad Nuruddin).
```

### Performance text (classify this)

```text
By Ahmad Nuruddin

I was born Noel Durham in Philadelphia, Pennsylvania in 1972. Along with two brothers, Joseph and Nathaniel, and sister, Marie, I was raised in a pseudo-Christian household. We were raised to believe in God and know right from wrong, but I cannot say we were involved with religion more than that.

Our grandparents were practicing Baptists and when my siblings and I visited them we would attend church regularly. My mother was a housewife, tending to her children's upbringing primarily, while my stepfather worked for a pipe supply company.

I went to public school and I still remember my mother stressing the importance of education throughout my childhood. As a family we did not have many means - luxuries were sacrificed in order for all of us to excel in education. It is a tribute to my mother that all of us did, despite the inner-city environment, obtain good grades and stay out of trouble.

I was also a good athlete, playing basketball and football when I was younger. In high school, I replaced basketball with wrestling but still kept playing football. I played both offensive and defensive tackle for the football team and became the captain during my senior year at Abraham Lincoln High School. I also wrestled as a heavyweight, which is the 225 pound-plus weight class. Our team won the citywide championship every year from my sophomore year onwards, and my personal record was 30-3.

During my junior year of high school, my elder brother Joseph came home from college during a holiday and said he is a Muslim and does not eat pork. At the time, it was a 'thing' in Philadelphia, kind of fashionable you can say, to give up pork to try to purify oneself. This was my first real contact with Islam.

While my family members were not antagonistic, they were a bit curious as to why this sudden change had come about in Joseph. I also had a cousin, Rashid, who was the same age as me and identified with the teachings of the Nation of Islam.

One time, Rashid gave me a Muslim head cap as a gift and I wore it the entire day because I liked the look. Surprisingly enough, throughout the entire day people would pass when I was walking on the street and say, "Assalaamu alaykum." This may not be a big deal to some folks, but those who are familiar the hustle-bustle lifestyle of any major American city know people just don't stop to say hello. When I found out that these people were wishing peace upon me simply because they assumed I was a Muslim, a small attraction began to develop for Islam.

After graduating from high school I enrolled at Indiana University (IU) in Pennsylvania, the same college my brother Joseph had attended. I continued to pray to God in times of trial or joy. This belief in God is due in part to the training my grandparents instilled in me. I would visit the church near campus sometimes and experienced more of what I had seen while at home - singing and dancing, but no real guidance on personal development and refinement.

By the Grace of God, despite some hard times, I earned my Bachelor's in Marketing in 1990.

When I returned home to start work, I found Islam was even more popular in Philadelphia. Muslim men, however, had become known for committing crimes and being abusive towards women. I remembered that when I was a child I had dream in which I had been in a car accident; it seemed as though I was hovering above the scene, and after the accident, I sat down in the median. The dream was strange as I had never been in an accident. I don't know why I recalled that dream following college. Anyways, one night my brother Joseph and I decided to visit our alma mater and on the way back, the car went out of control and violently flipped off the highway. Alhamdolillah, Joseph and I survived with only a few minor bumps and bruises.

A few months later I spotted an exact replica of the car that we were in during the accident. The car had a personalized license plate that said "B Ready." I found this very peculiar and feverishly prayed for God to show me the truth.

I began studying Islam and the Holy Qur'an. I noticed that if I had problem, I would open the Qur'an and eventually arrive on something that addressed the problem. Before I had finished half the Qur'an, I knew it was a living book from God. Eventually, I completed the entire English translation. I prayed, "If this is the truth, God, please guide me and allow me to fully understand and implement its teachings."

Thereafter I started to discuss my impressions of the Quran with friends. I also visited a few mosques but was disappointed at the lack of love and brotherhood the Muslims showed me simply because I was not a Muslim, at the time. One day, after a game of basketball with my cousin Rashid and some of his friends, three of the brothers asked if we would like to visit the mosque to offer prayers and eat. I did not know that these three brothers, Idrees Mahmood, Daud Mahmood, and Usman Abdul Karim, were Ahmadi Muslims at the time.

After we had offered prayers and eaten, we began a discussion on Islam and I was very impressed that they took an interest in my education of Islam. The first question they asked was whether I knew how to perform prayers in Arabic. As I did not, they began teaching me the entire prayer. I actually learned Surah Al-Fatihah that very day. Over a three-month span, I learned the fundamentals of Islam, the true story of Jesus Christ, and who the Promised Messiah and his successors were. I also became firmly grounded in the life of Prophet Muhammad. In fact, the first book I finished was Life of Muhammad by Mirza Bashiruddin Mahmood Ahmad, the Second Khalifa.

The pictures of the Promised Messiah and his successors had a profound impact on me. I was amazed that I was given that chance to actually see the face of a prophet of God as well as that of his noble successors. I knew this place, the Nasir Mosque, was the place to learn about Islam.

About a month after my first visit, in 1997, I joined the Ahmadiyya Muslim Community, under the watchful and loving eye of Imam Mubasher Ahmad. At that time, many brothers helped me pick out a new name. I wanted some connection to the Promised Messiah, so I chose "Ahmad," the "one who praises," as my first name. Learning that the Promised Messiah wished all of his followers to be like his First Khalifa, Hakim Nuruddin, I chose "Nuruddin," "light of the faith," as my last name.

I was very impressed with the fact that these brothers, despite being American, could recite the Qur'an in fluid and beautiful Arabic, and it made me want to be at par with them. At that time, an elder brother, Rashid, came to the mosque weekly to hold an Arabic class. Within three months time, Alhamdolillah, I became fluent in the recitation of the Qur'an in Arabic. The first chapter I then memorized was Surah al- Ikhlas.

While the demographic of Nasir Mosque was seventy percent Pakistani and thirty percent African- American, 100% of the brothers were honorable and honest people. I was enamored with the atmosphere as there was no backbiting or foul language, and all the brothers were highly educated and sincere. In particular, there was a brother named Munir Hamid, who I still recall was a striking figure because of his character and mannerisms.

Initiation into the Ahmadiyya Muslim Community has made me a much more refined and spiritually awakened human being. In both my walk and talk, those around me, especially my family, have seen a marked difference. I feel as though entering into this Community is akin to finding a fountain after wandering through a desert for one's entire life. There is no way I can leave this fountain now. I am 100% confident that I am following the correct teachings of the Qur'an and Prophet Muhammad.

Our youth group, Khuddamul Ahmadiyya, is a beautiful organization that allows the youth to quickly mature into men - becoming educated in both religious and secular studies. Many of our Khuddam are honorable young men who take education seriously and I feel it is very rare to be amongst such young people who are not engaged in the nonsense so many others most unfortunately fall victim to.

By the grace of Allah, in 2002, 1 married a woman who had converted to the Ahmadiyya Muslim Community one year prior. Allah has blessed us with three beautiful daughters.
```

---

## IC-2395: Call Me Charlie

- Title: Call Me Charlie
- Author (byline): Josh Bond
- Work: The Moth Presents: All These Wonders, Pg 119-125
- Publisher: Crown
- Publication date as stated: Mar 2017
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1335
- Already set (do not supply): none

### Source block (context only)

```text
Author: Josh Bond
Book: The Moth Presents: All These Wonders,
Pg 119-125
ISBN: 978-1101904404
Publisher: Crown
Date (Month/Year): Mar 2017
```

### Introduction (context only: never use it for content warnings)

```text
For well over a decade, Charlie Gasko, better known as James “Whitey” Bulger was America’s most wanted gangster—the FBI’s biggest domestic target, second in priority only to Osama bin Laden. As a leader of Boston’s Winter Hill Gang, Bulger was wanted by the Bureau on 19 charges of murder, as well as for numerous other offenses including racketeering, extortion and narcotics distribution. And yet, for 16 years—from just before Christmas 1994 until June 23, 2011—he remained at large. The main reason Bulger was able to first evade capture was that he had a man on the inside: FBI agent John Connolly. Connolly tipped Bulger off to a secret grand jury indictment, allowing the mobster to flee before his arrest.

Call Me Charlie by Josh Bond
```

### Performance text (classify this)

```text
I managed a hotel and an apartment building in Santa Monica for about seven years. I lived in the apartment building and had an office in the hotel across the street. You meet a lot of interesting people when you manage an apartment building. For example, there was a retired couple who lived in the apartment next to mine -- the Gaskos. The first time I met the husband, I was in my apartment playing guitar and trying to write a song. There's a knock on the door, and I open it to find a seventy-year-old man holding a black case. He tells me that he heard me playing music, and he thought I could use this black Stetson cowboy hat. Really nice gesture. I thank him, and he says his name is Charlie.

So fast-forward five years. I'm taking a nap on my couch. At 2:00 p.m. the phone rings, and my co-worker is at the hotel with the FBI. Before I know it, I’m on the phone with an FBI agent says, "I need to talk to you about a tenant in your apartment building. Come here now."

So, I get to my office and have a seat, and there's a large man wearing a Hawaiian shirt and jeans. He closes the door, throws a manila folder down on the desk, opens it and points to a sheet of paper. Across the top is "WANTED and, underneath, a photo of a man and a woman, with names.

He asks if these people live in the apartment next to mine. The woman is my neighbor, Carol Gasko. And while I've never heard the name "Catherine Greig," the name "James J. 'Whitey' Bulger" is very familiar. I had heard this name many times when I was in college at Boston University. But I didn't really know anything about him. He was a Jimmy Hoffa type guy to me, like, "Oh, this guy's missing, he's never gonna be found." It was almost like a joke.

So, I'm standing there, and the FBI agent says, "What do you think?"

"What does my face tell you?"

So, he gets on his radio, and while this is happening, it is almost like in a movie after an explosion where the sound just disappears. You don't know what's going on, and you don't know what's about to happen.

This is an old man who bought me a bike light one time because he was worried about me riding at night without one. And now I'm discovering he's a notorious fugitive?!

Hawaiian Shirt says, "Look, this guy's pretty high on the most-wanted list. We could use your help apprehending him. We can't just go to his apartment. We have to make sure he's in there. If it's just her, it doesn't really work for us. So why don't you go knock on the door and see if he's there?"

In the previous months, Carol had been telling people in the building, "Charlie has dementia, he has heart problems." They'd put notes on their door during the day that said, "Don't knock on the door." I knew from talking to him over the years that he slept during the day.

I explain this to the agent, and without skipping a beat he says, "Well, what are you doing tonight?" I realize I'm going to be with these guys until they have him in cuffs.

Then things really kick in. They place an agent at a window in the hotel that has a good view of the Gaskos' balcony. Then the agent wants to go to my apartment. I take him through a back alley and some side streets, so we aren't walking in front of the apartment building in clear view of Charlie and Carol. We're stopping at cars, and he's talking on the radio, and there are agents everywhere!

Hawaiian Shirt says, "They just closed their blinds. Did you tip 'em off?"

"I've been with you the whole time, no, of course not."

We get to my apartment, and I draw them a floor plan of the Gaskos' place. We're throwing ideas back and forth about how to get this guy out of his apartment.

My living room wall shares a wall with Charlie's bedroom, so I'm like, "Uh, you know this guy can hear everything we're saying? Like, he's repeated conversations I've had with my friends, asking me why we don't curse or fight as much as he and his friends did in his younger days."

We go into my bedroom, and we come up with an idea. We're going to break into his storage locker in the garage. We go down to the garage, and the FBI agent goes to get his car; he has some bolt cutters in there.

I'm suddenly pumped up. I'm involved in something. It's like a movie. I'm almost having fun at this point. The adrenaline is helping me forget about my relationship to these people. I mean, this is the same man who bought me a Christmas present every year.

Once the lock is broken, we go back to my apartment, and the agent's telling me, "Okay, this is what's gonna happen. I'm gonna go down, get everything set, I'm gonna call you, and you knock on his door and bring him down."

And I'm like, "No, I'm going to go to the hotel, I'm going to call him, tell him to meet me there. Then you guys take care of your business."

I'm in my office, and I'm thinking about this guy, my neighbor, who looked after an old woman on the first floor. Who one year, when I didn't write a thank you note for a Christmas present he gave me, gave me a box of stationery.

I'm thinking, What did this guy actually DO?

So I go to Wikipedia, and I'm reading about murders and extortion and gambling. I get to the bottom, and in one of his last public sightings with one of his Mafia buddies there's a quote from him: "When I go down, I'm going out with guns blazing."

I start to rethink my involvement in the day's events. Conveniently, my phone rings, and it's the FBI: "Make the call."

I start to waver: "Look, man, I just read something about this guy. . . and I don't know about this."

He says, "No, no, no, he'll never know, he'll never know." Which is obviously not true.

But . . . I call the Gaskos from the hotel, and there is no answer. I am so happy that they didn't answer the phone. I call the agent back, and I say, "Hey, man, sorry, they didn't answer. Going to have to do something else."

He says, "Are you sure you don't want to knock on the door?"

And I'm like, "Look, man, what if he comes to the door with a gun?"

He says, "Just be like, 'Hey, man, what's going on?' "

I'm thinking to myself, Uh, he will shoot me before I finish that one statement.

But while this is going on, Carol calls back. I explain to her that the storage unit's been broken into. I can either call the police, or Charlie can meet me in the garage and we'll look at it.

She says, "He'll be down in five minutes."

Hang up, call the FBI. "He's on his way.” ***** Looks through curtains at the chaos*****

[The take-down didn’t take long] As soon as I open the door, it's like a slow-motion shot of Suburbans and vans and FBI agents everywhere. And my neighbor, Charlie Gasko, standing there in cuffs, surrounded by agents, laughing and telling stories. He almost looks relieved. I see Carol standing a few feet away in cuffs. And the magnitude of everything that has happened starts to sink in. I helped the FBI arrest the most wanted man in the country.

New neighbors eventually moved in, and they seemed like nice people. But what do I know?
```

---

## IC-2396: The Cask of Amontillado

- Title: The Cask of Amontillado
- Author (byline): Edgar Allan Poe
- Work: 18 Best Stories
- Publisher: Dell Publishing Company, Inc
- Publication date as stated: Feb 1981
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1804
- Already set (do not supply): none

### Source block (context only)

```text
Author: Edgar Allen Poe
Book: 18 Best Stories
ISBN: 978-0440322276
Publisher: Dell Publishing Company, Inc
Date (Month/Year): Feb 1981
```

### Introduction (context only: never use it for content warnings)

```text
The thousand injuries of Fortunato I had borne as I best could but when he ventured upon insult I vowed revenge you who so well know the nature of my soul will not suppose however that gave utterance to a threat at length I would be avenged this was a point definitely settled but the very definitiveness with which it was resolved precluded the idea of risk I must not only punish but punish with impunity a wrong is un-redressed when retribution overtakes its redresser it is equally un-redressed when the avenger fails to make himself felt as such to him who has done the wrong. The Cask of Amontillado by Edgar Allan Poe
```

### Performance text (classify this)

```text
It must be understood that neither by word nor deed had I given Fortunato cause to doubt my good will I continued as was my in to smile in his face and he did not perceive that my to smile now was at the thought of his immolation He had a weak point this Fortunato although in other regards he was a man to be respected and even feared he prided himself on his connoisseurship in wine few Italians have the true virtuoso spirit for the most part their enthusiasm is adopted to suit the time and opportunity to practice imposture upon the British and Austrian millionaires in painting and gemmary Fortunato like his countrymen was a quack but in the matter of old wines he was sincere in this respect I did not differ from him materially I was skillful in the Italian vintages myself, and bought largely whenever I could It was about dusk one evening during the supreme madness of the carnival season that I encountered my friend he accosted me with excessive warmth for he had been drinking much the man wore motley he had on a tight-fitting party-striped dress and his head was surmounted by the conical cap and bells I was so pleased to see him that I thought I should never have done wringing his hand I said to him "my dear Fortunato you are luckily met how remarkably well you are looking today but I have received a pipe of what passes for Amontillado and I have my doubts"

"How?" said he "Amontillado a pipe? Impossible and in the middle of the carnival" "I have my doubts" I replied "and I was silly enough to pay the full Amontillado price without consulting you in the matter you were not to be found and I was fearful of losing a bargain" "Come let us go" "Whither?" "To your vaults" "My friend no” "Let us go nevertheless the cold is merely nothing” Thus speaking Fortunato possessed himself of my arm and putting on a mask of black silk and drawing a roquelaire closely about my person I suffered him to hurry me to my palazzo. I took from their sconces two flambeaux and giving one to Fortunato bowed him through several suites of rooms to the archway that led into the vaults we came at length to the foot of the descent and stood together upon the damp ground of the catacombs of the Montresors The gait of my friend was unsteady and the bells upon his cap jingled as he strode "The pipe" he said "It is farther on" said I "but observe the white web-work which gleams from these walls” He turned towards me and looked into my eves with two filmy orbs that distilled the rheum of intoxication "Nitre?" he asked at length "Nitre" I replied. "How long have you had that cough?" "Ugh ugh ugh ugh ugh " My poor friend found it impossible to reply for many minutes "It is nothing" he said, at last "Come" I said with decision "we will go back your health is precious you are rich respected admired beloved you are happy as once I was you are a man to be missed for me it is no matter we will go back you will be ill and I cannot be responsible Besides there is Luchresi " "Enough" he said "the cough's a mere nothing it will not kill me I shall not die of a cough" "True, true" I replied "and indeed I had no intention of alarming you unnecessarily but you should use all proper caution a draught of this Medoc will defend us from the damps Here I knocked off the neck of a bottle which I drew from a long row of its fellows that lay upon the mould “Drink" I said presenting him the wine. He raised it to his lips with a leer he paused and nodded to me familiarly while his bells jingled "I drink" he said "to the buried that repose around us" "And I to your long life” He again took my arm and we proceeded "These vaults" he said, "are extensive" "The Montresors" I replied "were a great and numerous family" "I forget your arms" "A huge human foot d'or in a field azure the foot crushes a serpent rampant whose fangs are imbedded in the heel" "And the motto?" "Nemo me impune lacessit" "Good" he said. The wine sparkled in his eyes and the bells jingled as my own fancy grew warm with the Medoc we had passed through long walls of piled skeletons with casks and puncheons intermingling into the inmost recesses of the catacombs I paused again and this time I made bold to seize Fortunato by an arm above the elbow. "The nitre!" I said "see it increases It hangs like moss upon the vaults we are below the river's bed the drops of moisture trickle among the bones come we will go back ere it is too late your cough " "It is nothing" he said "let us go on but first another draught of the Medoc" I broke and reached him a flagon of De Grave he emptied it at a breath his eyes flashed with a fierce light he laughed and threw the bottle upwards with a gesticulation I did not understand. I looked at him in surprise he repeated the movement a grotesque one "You do not comprehend?" he said "Not I" I replied "Then you are not of the brotherhood" "How?" "You are not of the masons" "Yes, yes" I said; "yes, yes" "You? Impossible a mason?"

"A mason" I replied. "A sign" he said "a sign" "It is this" I answered producing from beneath the folds of my roquelaire a trowel "You jest" he exclaimed recoiling a few paces "But let us proceed to the Amontillado." "Be it so" I said replacing the tool beneath the cloak and again offering him my arm he leaned upon it heavily we continued our route in search of the Amontillado we passed through a range of low arches descended passed on and descending again arrived at a deep crypt in which the foulness of the air caused our flambeaux rather to glow than flame at the most remote end of the crypt there appeared another less spacious its walls had been lined with human remains, piled to the vault overhead, in the fashion of the great catacombs of Paris three sides of this interior crypt were still ornamented in this manner from the fourth side the bones had been thrown down and lay promiscuously upon the earth forming at one point a mound of some size within the wall thus exposed by the displacing of the bones we perceived a still interior crypt or recess in depth about four feet in width three in height six or seven it seemed to have been constructed for no especial use within itself but formed merely the interval between two of the colossal supports of the roof of the catacombs and was backed by one of their circumscribing walls of solid granite it was in vain that Fortunato uplifting his dull torch endeavored to pry into the depth of the recess its termination the feeble light did not enable us to see. "Proceed" I said "herein is the Amontillado as for Luchresi” "He is an ignoramus" interrupted my friend as he stepped unsteadily forward while I followed immediately at his heels in niche and finding an instant he had reached the extremity of the niche and finding his progress arrested by the rock stood stupidly bewildered a moment more and I had fettered him to the granite in its surface were two iron staples distant from each other about two feet horizontally from one of these depended a short chain from the other a padlock Throwing the links about his waist it was but the work of a few seconds to secure it he was too much astounded to resist withdrawing the key I stepped back from the recesses As I said these words I busied myself among the pile of bones of which I have before spoken throwing them aside I soon uncovered a quantity of building stone and mortar with these materials and with the aid of my trowel I began vigorously to wall up the entrance of the niche a succession of loud and shrill screams bursting suddenly from the throat of the chained form seemed to thrust me violently back for a brief moment I hesitated I trembled unsheathing my rapier I began to grope with it about the recess but the thought of an instant reassured me I placed my hand upon the solid fabric of the catacombs and felt satisfied I re-approached the wall I replied to the yells of him who clamored I re-echoed I aided I surpassed them in volume and in strength I did this and the clamorer grew still It was now midnight and my task was drawing to a close I had completed the eighth the ninth and the tenth tier I had finished a portion of the last and the eleventh there remained but a single stone to be fitted and plastered in I struggled with its weight I placed it partially in its destined position but now there came from out the niche a low laugh that erected the hairs upon my head it was succeeded by a sad voice which I had difficulty in recognizing as that of the noble Fortunato The voice said "Ha ha ha he he he a very good joke indeed an excellent jest we will have many a rich laugh about it at the palazzo he he he over our wine he he he" "The Amontillado" I said "He he he he he he yes the Amontillado but is it not getting late? Will not they be awaiting us at the palazzo the Lady Fortunato and the rest let us be gone" "Yes" I said "let us be gone" "For the love of God Montresor" "Yes" I said "for the love of God” But to these words I hearkened in vain for a reply I grew impatient I called aloud "Fortunato"

No answer I called again “Fortunato" No answer still. I thrust a torch through the remaining aperture and let it fall within. There came forth in return only a jingling of the bells my heart grew sick it was the dampness of the catacombs that made it so. I hastened to make an end of my labour I forced the last stone into its position I plastered it up against the new masonry I re-erected the old rampart of bones for the half of a century no mortal has disturbed them
```

---

## IC-2397: A Child Called It

- Title: A Child Called It
- Author (byline): Dave Pelzer
- Work: Not specified
- Publisher: Health Communications, Inc.
- Publication date as stated: Oct 1995
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: DAVID, MOTHER, FATHER, MOTEHR
- Teaser before the introduction: Yes
- Spoken words (computed): 1451
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Pelzer
ISBN: 978-1558743663
Publisher: Health Communications, Inc.
Date (Month/Year): Oct 1995
```

### Introduction (context only: never use it for content warnings)

```text
From the outside looking in, you might’ve believed the Dave Pelzer had the perfect life – but four teachers who happened to be paying attention in the 1970s realized that was not the case at all. On paper, the Pelzer home seemed picture-perfect. But there were secrets at home. You see, when Dave’s mother drank, she morphed into something quite horrific. And unfortunately for Dave, he became her primary target. But in the 1970s, Child Protective Services did not exist, and our society didn’t want to know that there were parents out there actually hurting their children.

A Child Called It by Dave Pelzer
```

### Performance text (classify this)

```text
DAVID: (Pg 15) [Once upon a time] My family was the Brady Bunch of the 1960’s. My two brothers and I were blessed with the perfect parents. Our every whim was fulfilled with love and care.

My mother, Catherine, was a woman who glowed with love for her children. (Pg 16) One day, she took us to Chinatown in San Francisco. As we drove around the area, Mom told us about the culture and history of the Chinese people. When we returned, she decorated the dining room with Chinese lanterns, she dressed in a kimono and served what seemed to us as a very exotic meal. At the end of dinner Mom gave us fortune cookies and read the captions for us. I felt that the cookie’s message would lead me to my destiny -- “Love and honor thy mother, for she is the fruit that gives thou life.”

(Pg 18) [And Christmas!] Before dawn, Mom would creep into our room and wake us, whispering, “Santa came!”

DAVID: (Pg 21-22) [As I got older] My relationship with Mom drastically changed. As a small child, I probably had a voice that carried farther than others. I also had the unfortunate luck of getting caught at mischief, even though my brothers and I were often committing the same “crime.” In the beginning, I was put in a corner of our bedroom. When she yelled at us, her voice changed from nurturing mother to the wicked witch.

Soon, the sound of Mother’s voice began to send tremors down my spine.

When Mother decided that the “corner treatment” was no longer effective, I graduated to the “mirror treatment.” Mother would grab me and smash my head against the mirror, smearing my tear-streaked face on the slick, reflective glass. Then she would order me to say over and over again, “I’m a bad boy! I’m a bad boy! I’m a bad boy!”

(Pg 27-28) When I came home from school one day Mother told me that she had often driven to school to watch my brothers and me play during our lunch period recess. Mother claimed that she had seen me that very day playing on the grass, which was absolutely forbidden by her rules. I quickly answered that I never played on the grass. I knew Mother had somehow made a mistake. My reward for observing Mother’s rules and telling the truth was a hard punch in the face. Mother then reached over and turned on the gas burners to the kitchen stove. She sneered at me,

MOTHER: You’ve made my life a living hell! Now it’s time I showed you what hell is like.

DAVID: Gripping my arm, Mother held it in the orange-blue flame. As hard as I fought, I could not force Mother to let go of my arm. Finally, I fell to the floor, on my hands and knees, and tried to blow cool air on my arm. Mother ordered me to climb up onto the stove and lie on the flames so she could watch me burn. I refused, crying and pleading. I had to buy time.

(Pg 29) Finally, I heard the front door fly open. It was my brother Ron. My heart surged with relief. For a moment in time, Mother froze. I seized that instant to race to the garage. I had beaten her. That day I vowed to myself that I would never again give [her] the satisfaction of hearing me beg her to stop.

(Pg 30-31) The summer after the burn incident, school became my only hope of escape. By then, Mother would “forget” to feed me. On a good day, I was allowed leftover cereal portions from my brothers, but only if I performed chores before going to school. I started stealing food at school. (Pg 39-40) My idea was to rip off frozen lunches from the school cafeteria. Alone in the restroom, I swallowed frozen hot dogs and tater tots so fast I almost choked myself in the process. I returned to the classroom, feeling proud I had fed myself. I had fed myself!

That afternoon, Mother changed my mind. She dragged me into the bathroom and slugged me in the stomach so hard that I bent over. She rammed her finger into my mouth as if she wanted to pull my stomach up through my throat. I knew what was going to happen next. I closed my eyes as chunks of red meat spilled into the toilet. “I thought so. Your father’s going to hear about this!” Mother ordered me to scoop the partially digested food out of the toilet and put it in a bowl. Mother was gathering evidence. (Pg 41) That evening Mother and Father stormed into the kitchen.

MOTHER: So, you think the boy is through stealing food, do you?

DAVID: I could tell he was getting more and more tired of the constant “What the boy had done now” routine. Staring at me, Father shook his head in disapproval and stammered,

FATHER: Well, if you would just let The Boy have something to eat.

MOTEHR: EAT? You want the boy to eat? Well, the boy is going to EAT! He can eat this!

DAVID: I sat on a chair and picked the clumps of hot dogs out of the bowl with my hand. Globs of thick saliva slipped through my fingers, as I dropped it in my mouth. As I tried to swallow, I began to whimper. I turned to Father. He nodded for me to continue. I felt a hand clamp on the back of my neck.

MOTHER: Chew it! Eat it all!

DAVID: (Pg 42) Father turned away to avoid my pain. And at that moment, I hated Mother to no end, but I hated Father even more. He stood like a statue while his son ate something even a dog wouldn’t touch.

(Pg 50-54) The summer of 1971 – my morale dwindled. Food was little more than a fantasy. I rarely received breakfast and never lunch. As for dinner, I averaged about one every three days. During dinner, I sat at the bottom of the stairs listening to the sounds of “the family” eating. Suddenly [I heard] Mother’s snarling voice.

MOTHER: Get up here!

DAVID: I had begun clearing the dishes from the dining room table, praying that tonight I would get something, anything, to soothe my hunger.

MOTHER: You have 20 minutes! One minute, one second more, and you go hungry again! Is that understood?” Look at me when I’m talking to you!

DAVID: As I looked at her, Mother snatched a carving knife from the countertop and . . .

MOTHER: If you don’t finish on time, I’m going to kill you!

DAVID: Her words had no effect on me. She had said the same thing over and over again for almost a week now. But something looked wrong. Very wrong! I strained my eyes to focus on Mother. Her whole body began to weave back and forth. I thought she was going to fall. I imagined that the old drunk was going to fall flat on her face. Out of the corner of my eye I saw a blurred object fly from her hand. A sharp pain erupted from just above my stomach. I tried to remain standing, but my legs gave out, and my world turned black.

It took my Mother nearly half an hour to dress my wound. There was no remorse in her eyes. I thought that, at the very least, she would try to comfort me. Looking at me with no emotion, Mother stood up, washed her hands and told me I now had 30 minutes to finish the dishes.

From the kitchen I could hear Father flipping through his newspaper. I made my way into the living room. Sitting on the far end of the couch was my hero. I knew he would take care of Mother and drive me to the hospital. “Mo . . . Mo . . . Mother stabbed me. She told me if I didn’t do the dishes on time . . she’d kill me.”

FATHER: (Long pause - coldly) Well . . . you better go back in there and do the dishes. Damn it boy, we don’t need to do anything that might make her more upset! I don’t need that tonight . . . Go!

DAVID: I stood before Father in total shock. He didn’t even look at me.

(Pg 95-97) (As an adult) As a child living in a dark world, I feared for my life and thought I was alone. As an adult, I know now that I was not alone. There were thousands of other abused children. Some victims stay quietly locked in their shells. They look the other way, believing that by not acknowledging their past it will go away. This is my story. And I believe if society is to come to grips with the problem of child abuse, it must be exposed. Childhood should be carefree, playing in the sun; not living a nightmare in the darkness of the soul.
```

---

## IC-2398: Christmas Hatchet

- Title: Christmas Hatchet
- Author (byline): Patrick F. McManus
- Work: Never Sniff a Gift Fish
- Publisher: Owl Books
- Publication date as stated: Sept 1984
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1947
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patrick F. McManus
Book: Never Sniff a Gift Fish
ISBN: 978-0805000313
Publisher: Owl Books
Date (Month/Year): Sept 1984
```

### Introduction (context only: never use it for content warnings)

```text
Christmas Hatchet by Patrick F. McManus
```

### Performance text (classify this)

```text
The best evidence I've been able to come up with that the human race is increasing in intelligence is that parents no longer give their kids hatchets for Christmas.

When I was a boy the hatchet was a Christmas gift commonly bestowed upon male children. In an attempt to cover up their lapse of sanity, parents would tell their offspring, "Now don't chop anything." By the time this warning was out of mouths, the kid would have already whacked two branches off the Christmas tree and be adding a second set of notches to one of his new Lincoln logs.

It was not that the kid harbored a gene compelling him to be destructive. The problem was with the hatchet, which had a will of its own. As soon as the kid activated it by grasping the handle, the hatchet took charge of his mental processes and pretty much ran the show from then on.

Shortly after Christmas the kid would be making frequent trips to the woodshed with his father, and not to chop wood either.

"The hatchet did it!" the kid would yell as he was being dragged toward the woodshed by his shirt collar. I was just walking through the gate and my hatchet leaped out and chopped the post!"

Some kids were gullible enough to try the old George Washington cherry tree ploy. "I did it with my own little hatchet," they would confess.

"I know," their father would say. "Now haul your rear end out to the woodshed!"

The moral most of my friends and I drew from the cherry tree story wasn't that George Washington was so honest but that his father was a bit slow. This showed that even a kid with a dumb father could grow up to be President.

The average length of time a kid was allowed to remain in possession of his hatchet was forty-eight hours. By then the hatchet would have produced approximately sixty bushels of wood chips, eight hundred hack marks, and a bad case of hysteria for the kid's mother. The youngster would be unceremoniously stripped of his hatchet, even as its blade fell hungrily on a clothesline post or utility pole, and be told that he could have it back when he was "older" by which was meant age twenty-seven.

Kids now probably wouldn't understand the appeal hatchets held for youngsters of my generation. If a kid today received a hatchet for Christmas, he would ask, "Where do you put the batteries?" He would have no inkling of the romance of the hatchet and what it symbolized to boys of an earlier time, presumably all the way back to George Washington.

In the time and place of my childhood, woodcraft still loomed large in the scheme of a man's life. A man sawed and split firewood for the home, of course, but more important, he could take care of himself in the woods. He could build log cabins and lean-tos and foot-bridges, chop up a log to feed a campfire, fell poles to pitch a tent on or to hoist up a deer or to make a stretcher to haul out of the woods the person who wasn't that good with his ax.

One of the best things you could say about a man back then was that he was a good woodsman. Being good woodsman seemed to erase a lot of other character flaws.

"Shorty may have some faults," one man might say, "but I'll tell you this-he's a good woodsman!"

"Yep," someone else would observe. "Shorty is a fine woodsman, all right. If he made it to the mountains, I reckon it'll take the posse a month to root him out."

The ax was the primary tool of the woodsman. If he wished, a woodsman could go off into the woods with an ax and provide heat and shelter for himself and live a life of freedom and independence and dignity and not be at anyone's beck and call or have to comb his hair or take baths. Not that I recall anyone ever fleeing to the woods, not even Shorty, who was nabbed sitting on a barstool at Beaky's Tavern, still a long way from the mountains. But it was the idea! If you were good with an ax and a gun, of course, and a knife, you could always fall back to the mountains. What it was all about, underneath, was the potential for freedom, not the jived-up freedom of patriotic speeches but real freedom, one-to-one-ratio freedom, where man plucks his living directly from Nature. Of course, sometimes Nature plucks back, but that's not part of this dream, this vision, as symbolized by the Christmas hatchet.

I first realized I needed a hatchet when I was five years old and my mother read me stories about the pioneers chopping out little clearings in the great forests of the land. Ah, I thought, how satisfying it would be to chop out a clearing, to chop anything, for that matter. My campaign for a hatchet began immediately and achieved fruition on my eighth Christmas. Although I wasn't allowed to touch any of the presents before Christmas Eve, I had spotted one package that bore the general shape of a hatchet. Still, I couldn't be sure, because my mother was a clever and deceptive woman, once wrapping a new pair of long johns to look like an electric train. Was she pulling a fast one on me this time or had she truly lost her senses and bought me a hatchet?

It turned out to be a hatchet, a little red job with a hefty handle and a cutting edge dull as a licorice stick. Even as I unwrapped it, I could feel all the thousands of little chops throbbing about inside, pleading to be turned loose on the world.

"Now don't chop anything," my mother said.

Within minutes, I had honed a razor edge onto the hatchet and was overcome with a terrible compulsion to chop. Forty-eight hours later, the hatchet was wrenched from my grasp and hidden away, presumably to be returned to me sometime after I had children of my own.

A few days after Christmas I learned that my friend Crazy Eddie Muldoon, who lived on the farm next to ours, had also received a Christmas hatchet.

"Where is it?" I asked. "Let's go chop something."

"Uh, I got it put away," Crazy Eddie said. "Let's use yours."

"Uh, I loaned mine to my cousin for a while," I replied. "He said, 'You don't have a hatchet I can borrow, do you?' and I said, 'Sure."'

"Sure," said Crazy Eddie, who was only crazy part of the time.

As good luck would have it, an epidemic of permissiveness swept the county the following summer and both Eddie and I regained possession of our respective hatchets. There were still plenty of chops left in the hatchets and the two of us wandered off down to our woodlot in search of a suitable recipient. A large tamarack soared up uselessly on the edge of the woodlot, and Crazy Eddie said maybe it would be a good idea if we built an empty space in the sky where it was standing. As it happened, I had long nourished desire to yell "Timberrrrrr! " at the very moment I sent a mammoth of the forest crashing to the ground.

"Your folks can use it for firewood," Crazy Eddie said, in an attempt to explain his motive for felling the tamarack. But I knew he too yearned to hear the thunder of a great tree dashed to earth; he, as much as I, was into chopping for the pure aesthetics of the thing.

We spent all day chopping away at the tamarack, with Eddie on one side, me on the other, our hatchets sounding like slow but determined woodpeckers. At noon

I went home for lunch.

"What are you boys up to?" my mother asked, with no great show of interest.

"Chopping down a big tree."

"That's nice," Mom said. "Don't fight."

After lunch, Crazy Eddie and I were back at the tree again, chipping out a huge U-shaped gouge all the way around its circumference. We were both exhausted, sweating, standing in chips up to our knees, but we could see now it was possible to accomplish the task we had set for ourselves. The tree began to moan and creak ominously as the hatchets bit into its heartwood. By late afternoon the huge tamarack stood precariously balanced on a gnawed core of wood slightly thicker than a hatchet handle.

Neither Crazy Eddie nor I had the slightest clue as to the direction in which the tree might fall, which heightened our anticipation with the added element of suspense. We took turns charging up to the tree, whacking out a quick chip, and then dashing back to relative safety.

Suddenly we heard it: the faint, soft sigh that signaled the tree's unconditional surrender to our Christmas hatchets. A silence fell upon the land. High above us the boughs of the tamarack rustled. Crazy Eddie and I shivered happily. We had accomplished something momentous!

Crrrrrraaa ... went the tree, beginning a slow tilt. We were now able to determine the direction of its fall, which wasn't particularly good. Eddie's father, a short while before, had built a fence between our woodlot and theirs and now, even though I had not yet studied plane geometry, I was able to calculate with considerable accuracy that the tree would neatly intersect the fence at right angles.

"You better yell 'timber,"' Crazy Eddie said, his voice trembling.

"Timmmm . . . " I started to cry. Then we heard another cry. It was that of Eddie's father, who had come down to the woodlot to call him to supper.

"Eddieeeee!" his father called. "Crazy Eddieee! It's time for supperrrrr!"

Cr-r-r-r-a-a-a-a-A-A-A-A-ACK! went the tree.

"Eddieee!" went Eddie's father. "EddieeEEEEEE!" The monstrous tamarack smote the earth with a thunderous roar, rising above which was the twanging hum of barbwire. Fence posts shot into the air fifty yards away. Eddie's father shot into the air fifty feet away.

"Bleeping bleep of a bleep! screamed Eddie's father, introducing me to that quaint expression for the first time.

There is an old saying that cutting firewood warms you twice: once when you chop it and once when you burn it. Well, chopping down that tamarack warmed Eddie and me three times, and one of those warnings was a good deal hotter than when the wood burned.

I learned a good many things from felling that tamarack with my Christmas hatchet, perhaps the most interesting of which is that a barbwire fence is regarded by its builder as merely a barbwire fence until a tree falls on it. Afterward it is looked back upon as a priceless work of art, surpassed in beauty and grandeur only by the Taj Mahal.

My Christmas hatchet disappeared immediately after the great tree-felling but surfaced again a few years later when I was old enough to conduct my own camping trips. Much to my surprise, I discovered the hatchet was almost useless for cutting wood. It was as if Excalibur had been reduced to a putty knife.

The very next Christmas, I gave my little cousin Delbert the hatchet as a present.

"Wow!" he said. A real hatchet of my own! Thanks a lot!"

"You're welcome!" I shouted after him as he raced away, homing in on a stand of shrubs in his backyard. "But don't chop anything!"
```

---

## IC-2399: The Christmas Truce

- Title: The Christmas Truce
- Author (byline): Aaron Shepard
- Work: Not specified
- Publisher: Skyhook Press
- Publication date as stated: Nov 2016
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1356
- Already set (do not supply): none

### Source block (context only)

```text
Author: Aaron Shephard
ISBN: 978-1620355053
Publisher: Skyhook Press
Date (Month/Year): Nov 2016
```

### Introduction (context only: never use it for content warnings)

```text
The Christmas Truce of 1914 is one of the most extraordinary incidents of World War I and perhaps of all military history. It has endured as an archetypal image of peace.

On a Christmas Eve during World War I, British and German soldiers lay down their weapons to celebrate the holiday together. The truce covered as much as two-thirds of the British-German front, with thousands of soldiers taking part. Perhaps most remarkably, it grew out of no single initiative but sprang up in each location spontaneously. This fictional letter is drawn from first-hand accounts of soldiers found in their historic letters and diaries – One night of peace in a world of war.

The Christmas Truce: A True Story of World War I by Aaron Shepard
```

### Performance text (classify this)

```text
Christmas Day, 1914. My dear sister Janet,

It is 2:00 in the morning and most of our men are asleep in their dugouts—yet I could not sleep myself before writing to you of the wonderful events of Christmas Eve. In truth, what happened seems almost like a fairy tale, and if I hadn’t been through it myself, I would scarce believe it. Just imagine: While you and the family sang carols before the fire there in London, I did the same with enemy soldiers here on the battlefields of France!

There has been little fighting of late. The first battles of the war left so many dead that both sides have held back until replacements could come from home. We have mostly stayed in our trenches and waited. But what a terrible waiting it has been! Knowing that any moment an artillery shell might land and explode beside us. And in daylight not daring to lift our heads above ground, for fear of a sniper’s bullet.

The rain has fallen almost daily. Of course, it collects right in our trenches, where we must bail it out with pots and pans. And with the rain has come mud—a good foot or more. One new recruit got his feet stuck in it, and then his hands too when he tried to get out—just like in that American story of the tar baby!

Through all this, we couldn’t help feeling curious about the German soldiers across the way. They faced the same dangers we did and slogged about in the same muck. Their first trench was only fifty yards from ours. Between us lay No Man’s Land, bordered on both sides by barbed wire— yet they were close enough we sometimes heard their voices.

Just yesterday morning, we had our first good freeze. Cold as we were, we welcomed it, because at least the mud froze solid. Everything was tinged white with frost, while a bright sun shone over all. Perfect Christmas weather. And as darkness fell on Christmas Eve, the shooting stopped entirely. Our first complete silence in months! We hoped it might promise a peaceful holiday, but we didn’t count on it. We’d been told the Germans might attack.

I went to the dugout to rest, and lying on my cot, I must have drifted asleep. All at once my friend John was shaking me awake, saying, “Come and see! See what the Germans are doing!” I grabbed my rifle, stumbled out into the trench, and stuck my head cautiously above the sandbags.

I never hope to see a stranger and more lovely sight. Clusters of tiny lights were shining all along the German line, left and right as far as the eye could see.

“What is it?” I asked in bewilderment, and John answered, “Christmas trees!” The Germans had placed Christmas trees in front of their trenches, lit by candle or lantern like beacons of good will. And then we heard their voices raised in song.

Stille nacht, heilige nacht . . . This carol may not yet be familiar to us in Britain, but John knew it and translated: “Silent night, holy night.” I’ve never heard one lovelier—or more meaningful, in that quiet, clear night.

When the song finished, the men in our trenches applauded. Yes, British soldiers applauding Germans! Then one of our own men started singing, and we all joined in.

The first Noel, the angel did say . . . In truth, we sounded not nearly as good as the Germans, with their fine harmonies. But they responded with enthusiastic applause of their own and then began another.

O Tannenbaum, o Tannenbaum . . . Then we replied.

O come all ye faithful . . . But this time they joined in. British and German harmonizing across No Man’s Land! I would have thought nothing could be more amazing—but what came next was more so.

“English, come over!” we heard one of them shout. “You no shoot, we no shoot.” There in the trenches, we looked at each other in bewilderment. Then one of us shouted jokingly, “You come over here.” To our astonishment, we saw two figures rise from the trench, climb over their barbed wire, and advance unprotected across No Man’s Land. One of them called, “Send officer to talk.”

I saw one of our men lift his rifle to the ready, and no doubt others did the same—but our captain called out, “Hold your fire.” Then he climbed out and went to meet the Germans halfway. We heard them talking, and a few minutes later, the captain came back with a German cigar in his mouth!

“We’ve agreed there will be no shooting before midnight tomorrow,” he announced. “But sentries are to remain on duty, and the rest of you, stay alert.”

And in minutes, there we were in No Man’s Land, over a hundred soldiers and officers of each side, shaking hands with men we’d been trying to kill just hours earlier! Before long a bonfire was built, and around it we mingled—British khaki and German grey. I must say, the Germans were the better dressed, with fresh uniforms for the holiday.

Only a couple of our men knew German, but more of the Germans knew English. I asked one of them why that was.

“Because many have worked in England!” he said. He told me he had a girlfriend in London and that the war had interrupted their plans for marriage. I said, “Don’t worry. We’ll have you beat by Easter, then you can come back and marry the girl.”

Another German had been a porter at Victoria Station. He showed me a picture of his family back in Munich. His eldest sister was so lovely, I told him I should like to meet her someday. He beamed and said he would like that very much and gave me his family’s address.

Even those who could not converse could still exchange gifts—Our tea for their coffee, our corned beef for their sausage. Badges and buttons from uniforms changed owners, and one of our lads walked off with the infamous spiked helmet! Newspapers too changed hands, and the Germans howled with laughter at ours. They assured us that France was finished and Russia nearly beaten too. We told them that was nonsense, and one of them said, “Well, you believe your newspapers and we’ll believe ours.”

Clearly they are lied to—yet after meeting these men, I wonder how truthful our own newspapers have been. These are not the “savage barbarians” we’ve read so much about. They are men with homes and families, hopes and fears, principles and, yes, love of country. In other words, men like ourselves. Why are we led to believe otherwise?

As it grew late, a few more songs were traded around the fire, and then we parted with promises to meet again tomorrow, and even some talk of a football match. I was just starting back to the trenches when an older German clutched my arm. “My God,” he said, “why cannot we have peace and all go home?”

I told him gently, “That you must ask your emperor.”

He looked at me then, searchingly. “Perhaps, my friend. But also we must ask our hearts.”

And so, dear sister, tell me, has there ever been such a Christmas Eve in all history? And what does it all mean, this impossible befriending of enemies?

For the fighting here, it means regrettably little. Decent fellows those soldiers may be, but they follow orders and we do the same. Besides, we are here to stop their army and send it home, and never could we shirk that duty.

Still, one cannot help imagine what would happen if the spirit shown here were caught by the nations of the world. Of course, disputes must always arise. But what if our leaders were to offer well wishes in place of warnings?

Songs in place of slurs? Presents in place of reprisals? Would not all war end at once?

All nations say they want peace. Yet on this Christmas morning, I wonder if we want it quite enough.

Your loving brother, Tom
```

---

## IC-2400: The Color of Water

- Title: The Color of Water
- Author (byline): James McBride
- Work: Not specified
- Publisher: Riverhead Books
- Publication date as stated: Feb 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: JAMES, RICHIE, MOMMY, DAUGHTER
- Teaser before the introduction: Yes
- Spoken words (computed): 2044
- Already set (do not supply): none

### Source block (context only)

```text
Author: James McBride
ISBN: 978-1594481925
Publisher: Riverhead Books
Date (Month/Year): Feb 2006
```

### Introduction (context only: never use it for content warnings)

```text
It took James McBride 14 years to unearth his mother’s remarkable story – the daughter of an Orthodox Jewish rabbi who married a black man in 1942. In this excerpt, James examines her life, his own childhood in Brooklyn’s housing projects, and the force of his mother’s love. The Color of Water: A Black Man’s Tribute to His White Mother by James McBride
```

### Performance text (classify this)

```text
As a boy, I never knew where my mother was from – where she was born, who her parents were. When I asked she’d say, “God made me.” When I asked if she was white, she’d say, “I’m light-skinned,” and change the subject. She raised 12 black children and sent us all to college and in most cases graduate school. Her children became doctors, professors, chemists, teachers - yet none of us even knew her maiden name until we were grown.

Answering questions about her personal history did not jibe with Mommy’s view of parenting twelve curious, wild, brown-skinned children. She issued orders and her rule was law. Since she refused to divulge details about herself or her past, and because my stepfather was largely unavailable to deal with questions about himself or Ma, what I learned of Mommy’s past I learned from my siblings. We traded information on Mommy the way people trade baseball cards, offering bits and pieces fraught with gossip, nonsense, wisdom, and sometimes just plain foolishness. “What does it matter to you?” my older brother Richie scoffed. “You’re adopted anyway.”

JAMES: “You’re lying.”

RICHIE: “You’ll see when Mommy takes you back to your real mother next week. Why do you think she’s been so nice to you all week?” Suddenly, it occurred to me that Mommy had been nice to me all week. But wasn’t she nice to me all the time? I couldn’t remember, partly because within my confused 8-year-old reasoning was a growing fear that maybe Richie was right.

Mommy, after all, did not really look like me. In fact, she didn’t look like Richie, or David – or any of her children for that matter. We were all clearly black, of various shades of brown, some light brown, some medium brown, some very light-skinned. And all of us had curly hair. Mommy was, by her own definition, “light-skinned,” a statement which I had initially accepted as fact but at some point later decided was not true. There was something inside me that told me. It was in my blood, you might say. Yet Mommy refused to acknowledge her whiteness. Why she did so was not clear, but even my teachers seemed to know she was white and I wasn’t. On open school nights, the question most often asked by my schoolteachers was, “Is James adopted?” which always prompted an outraged response from Mommy.

JAMES: “If I’m adopted, you’re adopted too.”

RICHIE: “Nope. Just you, and you’re going back to your real mother in jail.”

JAMES: “I’ll run away first.”

RICHIE: “You can’t do that. Mommy will get in trouble if you do that. You don’t want to see Ma get in trouble, do you?

JAMES: (Panic setting in) “But I don’t want to go to my real mother. I want to stay here with Ma. . . “

RICHIE: “You gotta go. I’m sorry, man.” This went on until I was in tears. I remember pacing about nervously all day while Richie, knowing he had ruined my life, cackled himself to sleep. That night I law wide awake in bed waiting for Mommy to get home from work at 2 a.m.

MOMMY: (laughing) “You’re not adopted.”

JAMES: “So you’re my real mother?”

MOMMY: “Of course I am.” (big kiss) “You want some coffee cake?” Enough said . . . In 1966, when I was 9, black power had permeated every element of my neighborhood in St. Albans, Queens. Malcolm X had been killed the year before and had grown larger in death than in life. Afros were in style. The Black Panthers were a force. Congas played at night on the streets.

But there was a part of me that feared black power very deeply for the obvious reason. I thought black power would be the end of my mother. I had swallowed the white man’s fear of the Negro, as we were called back then, whole. It began with a sober white newsman on our black-and-white television set introducing a news clip showing a Black Panther rally led by one of those black militant leaders, screaming to hundreds and hundreds of angry African-American students, “Black power! Black power! Black power!” while the crowd roared. I thought to myself, these people will kill Mommy. Mommy, on the other hand, seemed unconcerned. Her motto was,

MOMMY: “If it doesn’t involve your going to school or church, I could care less about it and my answer is no whatever it is.” She insisted on absolute privacy, excellent school grades, and trusted no outsiders of either race. But even if she had any interest in black power, she had no time to talk about it. She worked the swing shift at Chase Manhattan Bank as a typist, leaving home at 3 p.m. and returning around 2 a.m., so she had little time for games. On his end, my father, Andrew McBride, a Baptist minister, had his doubts about the world accepting his mixed family. He always made sure his kids never got into trouble, was concerned about money, and trusted the providence of the Holy Father to do the rest. After he died and Mommy remarried, my stepfather, Hunter Jordan, seemed to pick up where my father left off, insistent on education and church. On her end, Mommy had no model for raising us other than the experience of her own Orthodox Jewish family which represented the best and worst of the immigrant mentality: hard work, no nonsense, quest for excellence, and a deep belief in God and education. They believed that money without knowledge was worthless, that education tempered with religion was the way to climb out of poverty in America, and over the years they were proved right. Yet conflict was a part of our lives. Mommy’s contradictions crashed and slammed against one another like bumper cars at Coney Island. White folks, she felt, were implicitly evil toward blacks, yet she forced us to go to white schools to get the best education. Blacks could be trusted more, but anything involving blacks was probably slightly substandard. She couldn’t stand racists of either color and had great distaste for bourgeois blacks who sought to emulate rich whites by putting on airs and “doing silly things like covering their couches with plastic and holding teacups with their pinkies out.”

MOMMY: (hissing) “What fools!” When Malcolm X talked about “the white devil” Mommy simply felt those references didn’t apply to her. She viewed the civil rights achievements of black Americans with pride, as if they were her own. And she herself occasionally talked about “the white man” in the third person, as if she had nothing to do with him, and in fact she didn’t, since most of her friends and social circle were black women from church.

MOMMY: “What’s the matter with these white folks?” (reading the newspaper) “They’re fighting over this man’s money now that he’s dead. None of them wanted him when he was alive, and now look at them. Forget it, honey. (she’s talking to the newspaper) Your husband’s dead, okay? He’s dead – poop! You had your chance. Is money gonna bring him back? No!” Then she’d turn to us and deliver the invariable lecture: “

MOMMY: “You don’t need money. What’s money if your mind is empty! Educate your mind! Is this world crazy or am I the crazy one? It’s probably me.” Indeed it probably was – at least, I thought so. I knew of no other white woman who would board the subway in Manhattan at one o’clock every morning and fall asleep till she got to her stop in Queens 45 minutes later. Her lack of fear for her safety – particularly among blacks, where she often stuck out like a sore thumb and seemed an easy target for muggers – had me stumped. As a grown man, I understand now, understand how her Christian principles and trust in God kept her going through all her life’s battles, but as a boy, my faith was not that strong. Mommy once took me to Harlem. When we got off the bus, two black men came up behind us and one of them grabbed Mommy’s purse. It seemed that the only white person for miles was my own mother. The incident confirmed my fears that Mommy was always in danger. Mommy loved God. She went to church each and every Sunday, the only white person in sight, butchering the lovely hymns with a singing voice that sounded like a cross between a cold engine trying to crank on an October morning and a whining Maytag washer. My siblings and I would muffle our laughter as Mommy dug into hymns with verve and gusto:

MOMMY: “Leaning. . . .oh, leannnning . . . safe and secure on the ---“ * Up, up, and away she went, her shrill voice climbing higher and higher. Even as a boy I knew God was all-powerful because of Mommy’s utter deference to Him, and also because she would occasionally do something in church that I never saw her do at home or anywhere else: at some point in the service, usually when the congregation was singing one of her favorite songs, like “What a Friend We Have in Jesus,” she would bow down her head and weep. It was the only time I ever saw her cry. I asked her one afternoon after service . . .

JAMES: “Why do you cry in church?”

MOMMY: “Because God makes me happy.”

JAMES: “Then why cry?”

MOMMY: “I’m crying ‘cause I’m happy. Anything wrong with that?” But there was something wrong, because happy people did not seem to cry like she did. Mommy’s tears seemed to come from somewhere else, a place far away, a place inside her that she never let any of us children visit, and even as a boy I felt there was pain behind them. I thought it was because she wanted to be black like everyone else in church, because maybe God liked black people better, and one afternoon on the way home from church I asked her whether God was black or white.

MOMMY: (a deep sigh) “Oh boy. . . God’s not black. He’s not white. He’s a spirit.”

JAMES: “Does he like black or white people better?”

MOMMY: “He loves all people. He’s a spirit.”

JAMES: “What color is God’s spirit?”

MOMMY: “It doesn’t have a color. God is the color of water. Water doesn’t have a color.” There are probably a hundred reasons why Mommy should have stayed on the Jewish side, instead of taking New Jersey Transit and the F train to go to a Christian church in Brooklyn, but I'm glad she came over to the African-American side. She married two extraordinary men and raised twelve very creative and talented children who became doctors, professors, chemists, and teachers. Like any family we have problems, but we have always been close. Through marriage and adoptions, the original dozen has expanded into dozens and dozens more-wives, husbands, children, grandchildren, cousins, nieces, nephews-ranging from dark-skinned to light-skinned; from black kinky hair to blond hair and blue eyes. In running from her past, Mommy has created her own nation. I have met hundreds of mothers – African American, Jewish, European, Arab, Latino, African, Muslim, Christian, Hindu, Buddhist – and all of them understand that family love, a mother’s love gives us grace, courage, and power beyond measure. One afternoon, a few years ago, my African American daughter, who was about eight years old asked me:

DAUGHTER: “Daddy, if Grandma is your mother, how come she doesn’t look like me or you?” I gave her the only answer I could:

JAMES: “I don’t know. But she loves us, and that’s the most important thing.” I all the important ways, my family’s story is not unique. It plays out across the world, on every continent, in every nation, city, town and village every day. Family love: It is firm footing, something to cling to in a frightened world that seems to spin out of control with war, turmoil, terrorism and uncertainty. It is our highest calling and our greatest nobility. So if you see a woman driving in Trenton with her blinkers on, look out. Back off. Give her some space. She could go left, she could go right. She could go up into Heaven clear out of sight! But no matter which way she goes, she’s not likely going your way. And if she is, don’t bother her with any questions about it, or you’ll get an earful of God.
```
