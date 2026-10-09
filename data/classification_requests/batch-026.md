# Classification request: batch 26 of 53 (40 records, IC-1401 to IC-1440)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-026-reply.json`.

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

## IC-1401: A Plague of Tics

- Title: A Plague of Tics
- Author (byline): David Sedaris
- Work: Naked
- Publisher: Back Bay Books
- Publication date as stated: June 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2545
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Sedaris
Book: Naked
ISBN: 978-0316777735
Publisher: Back Bay Books
Date (Month/Year): June 1998
```

### Introduction (context only: never use it for content warnings)

```text
Obsessive-compulsive disorder (OCD) is an illness that causes people to have unwanted thoughts (obsessions) and to repeat certain behaviors (compulsions) over and over again. We all have habits and routines in our daily lives, such as brushing our teeth before bed. However, for people with OCD, patterns of behavior get in the way of their daily lives. Most people with OCD know that their obsessions and compulsions make no sense, but they can't ignore or stop what quickly becomes . . . A Plague of Tics by David Sedaris
```

### Performance text (classify this)

```text
When the teacher asked if she might visit with my mother, I touched my nose eight times to the surface of my desk.

"May I take that as a 'yes'?" she asked.

According to her calculations, I had left my chair twenty-eight times that day. "You're up and down like a flea. I turn my back for two minutes and there you are with your tongue pressed against that light switch. Maybe they do that where you come from, but here in my classroom we don't leave our seats and lick things whenever we please. That is Miss Chestnut's light switch, and she likes to keep it dry. Would you like me to come over to your house and put my tongue on your light switches? Well, would you?"

I tried to picture her in action, but my shoe was calling. Take me off, it whispered. Tap my heel against your forehead three times. Do it now, quick, no one will notice.

"Well?" Miss Chestnut raised her faint, penciled eyebrows. "I'm asking you a question. Would you or would you not want me licking the light switches in your house?"

I slipped off my shoe, pretending to examine the imprint on the heel.

"You're going to hit yourself over the head with that shoe, aren't you?"

It wasn't "hitting," it was tapping; but still, how had she known what I was about to do?

"Heel marks all over your forehead," she said, answering my silent question.

"You should take a look in the mirror sometime. Shoes are dirty things. We wear them on our feet to protect ourselves against the soil. It's not healthy to hit ourselves over the head with shoes, is it?"

I guessed that it was not.

"Guess? This is not a game to be guessed at. I don't 'guess' that it's dangerous to run into traffic with a paper sack over my head. There's no guesswork involved. These things are facts, not riddles." She sat at her desk, continuing her lecture as she penned a brief letter. "I'd like to have a word with your mother. You do have one, don't you? I'm assuming you weren't raised by animals. Is she blind, your mother? Can she see the way you behave, or do you reserve your antics exclusively for Miss Chestnut?" She handed me the folded slip of paper. "You may go now, and on your way out the door I'm asking you please not to bathe my light switch with your germ-ridden tongue. It's had a long day; we both have."

It was a short distance from the school to our rented house, no more than six hundred and thirty-seven steps, and on a good day I could make the trip in an hour, pausing every few feet to tongue a mailbox or touch whichever single leaf or blade of grass demanded my attention. If I were to lose count of my steps, I'd have to return to the school and begin again. "Back so soon?" the janitor would ask. "You just can't get enough of this place, can you?"

Depressing as it was, arriving at the front stoop of the house meant that I had completed the first leg of that bitter-tasting journey to my bedroom. Once home I would touch the front door seven times with each elbow, a task made more difficult if there was someone else around. "Why don't you try the knob," my sister Lisa would say. "That's what the rest of us do, and it seems to work for us." Inside the house there were switches and doorstops to be acknowledged. My bedroom was right there off the hallway, but first I had business to tend to. After kissing the fourth, eighth, and twelfth carpeted stair, I wiped the cat hair off my lips and proceeded to the kitchen, where I was commanded to stroke the burners of the stove, press my nose against the refrigerator door, and arrange the percolator, toaster, and blender into a straight row. After making my rounds of the living room, it was time to kneel beside the banister and blindly jab a butter knife in the direction of my favorite electrical socket. There were bulbs to lick and bathroom faucets to test before finally I was free to enter my bedroom, where I would carefully align the objects on my dresser, lick the corners of my metal desk, and lie upon my bed, rocking back and forth and thinking of what an odd woman she was, my third-grade teacher, Miss Chestnut. Why come here and lick my switches when she never used the one she had? Maybe she was drunk.

Her note had asked if she might visit our home in order to discuss what she referred to as my "special problems."

"Have you been leaving your seat to lick the light switch?" my mother asked. She placed the letter upon the table and lit a cigarette.

"Once or twice," I said.

"Once or twice what? Every half hour? Every ten minutes?"

"I don't know," I lied. "Who's counting?"

"Well, your math teacher, for one. That's her job, to count. What, do you think she's not going to notice?"

"Notice what?" It never failed to amaze me that people might notice these things. Because my actions were so intensely private, I had always assumed they were somehow invisible.

"And I suppose this Miss…" My mother unfolded the letter and studied the signature. "This Miss Chestnut is mistaken? Is that what you're trying to tell me? Maybe she has you confused with the other boy who leaves his seat to lick the pencil sharpener or touch the flag or whatever the hell it is you do the moment her back is turned?"

"That's very likely," I said. "She's old.

On the afternoon that Miss Chestnut arrived for her visit, I was in my bedroom, rocking. Unlike the obsessive counting and touching, rocking was not a mandatory duty but a voluntary and highly pleasurable exercise. It was my hobby, and there was nothing else I would rather do. The point was not to rock oneself to sleep: This was not a step toward some greater goal. It was the goal itself. The perpetual movement freed my mind, allowing me to mull things over and construct elaborately detailed fantasies. Toss in a radio, and I was content to rock until three or four o'clock in the morning, listening to the hit parade and discovering that each and every song was about me. I might have to listen two or three hundred times to the same song, but sooner or later its private message would reveal itself. Because it was pleasant and relaxing, my rocking was bound to be tripped up, most often by my brain, which refused to allow me more than ten consecutive minutes of happiness. At the opening chords of my current favorite song, a voice would whisper, Shouldn't you be upstairs making sure there are really one hundred and fourteen peppercorns left in that small ceramic jar? And, hey, while you're up there, you might want to check the iron and make sure it's not setting fire to the baby's bedroom. The list of demands would grow by the moment. What about that television antenna? Is it still set into that perfect V, or has one of your sisters destroyed its integrity. You know, I was just wondering how tightly the lid is screwed onto that mayonnaise jar. Let's have a look, shall we?

I was coming to terms with "The Shadow of Your Smile" when Miss Chestnut arrived. She rang the bell, and I cracked open my bedroom door, watching as my mother invited her in.

I tried rocking in bed, but the sound of laughter drew me to the top of the landing, where from my vantage point behind an oversized wardrobe box, I watched the two women discuss my behavior.

"Oh, you mean the touching," my mother said. She studied the ashtray that sat before her on the table, narrowing her eyes much like a cat catching sight of a squirrel. Her look of fixed concentration suggested that nothing else mattered. Time had stopped, and she was deaf to the sounds of the rattling fan and my sisters' squabbling out in the driveway. She opened her mouth just slightly, running her tongue over her upper lip, and then she inched forward, her index finger prodding the ashtray as though it were a sleeping thing she was trying to wake. I had never seen myself in action, but a sharp, stinging sense of recognition told me that my mother's impersonation had been accurate.

"Priceless!" Miss Chestnut laughed, clasping her hands in delight. "Oh, that's very good, you've captured him perfectly. Bravo, I give you an A-plus."

"God only knows where he gets it from," my mother said. "He's probably down in his room right this minute, counting his eyelashes or gnawing at the pulls on his dresser. One, two o'clock in the morning and he'll still be at it, rattling around the house to poke the laundry hamper or press his face against the refrigerator door. The kid's wound too tight, but he'll come out of it.

Following Miss Chestnut's visit, my father attempted to cure me with a series of threats. "You touch your nose to that windshield one more time and I'll guarantee you'll wish you hadn't," he said driving home from the grocery store with a lapful of rejected, out-of-state coupons. It was virtually impossible for me to ride in the passenger seat of a car and not press my nose against the windshield, and now that the activity had been forbidden, I wanted it more than anything. I tried closing my eyes, hoping that might eliminate my desire, but found myself thinking that perhaps he was the one who should close his eyes. So what if I wanted to touch my nose to the windshield? Who was it hurting? Why was it that he could repeatedly worry his change and bite his lower lip without the threat of punishment? My mother smoked and Miss Chestnut massaged her waist twenty, thirty times a day — and here I couldn't press my nose against the windshield of a car? I opened my eyes, defiant, but when he caught me moving toward my target, my father slammed on the brakes.

"You like that, did you?" He handed me a golf towel to wipe the blood from my nose. "Did you like the feel of that?"

Like was too feeble for what I felt. I loved it. If mashed with the right amount of force, a blow to the nose can be positively narcotic. Touching objects satisfied a mental itch, but the task involved a great deal of movement: run upstairs, cross the room, remove a shoe. I soon found those same urges could be fulfilled within the confines of my own body. Punching myself in the nose was a good place to start, but the practice was dropped when I began rolling my eyes deep in their sockets, an exercise that produced quick jolts of dull, intoxicating pain.

"I know exactly what you're talking about," my mother said to Mrs. Shatz, my visiting fourth-grade teacher. "The eyes rolling every which way, it's like talking to a slot machine. Hopefully, one day he'll pay off, but until then, what do you say we have ourselves another glass of wine?"

"Hey, sport," my father said, "if you're trying to get a good look at the contents of your skull, I can tell you right now that you're wasting your time. There's nothing there to look at, and these report cards prove it."

I took to violently shaking my head, startled by the feel of my brain slamming against the confines of my skull. It felt so good and took so little time; just a few quick jerks and I was satisfied for up to forty-five seconds at a time.

"Have a seat and let me get you something cool to drink." My mother would leave my fifth-and then my sixth-grade teachers standing in the breakfast nook while she stepped into the kitchen to crack open a tray of ice. "I'm guessing you're here about the head-shaking, am I right?" she'd shout. "That's my boy, all right, no flies on him." She suggested my teachers interpret my jerking head as a nod of agreement. "That's what I do, and now I've got him washing the dishes for the next five years. I ask, he yanks his head, and it's settled.

This was part of my mother's act. She played the ringleader, blowing the whistle and charming the crowd with her jokes and exaggerated stories. She noticed my tics and habits but was never shamed or seriously bothered by any of them. Her observations would be collected and delivered as part of a routine that bore little resemblance to our lives.

I'd like to think that some of my nervous habits faded during high school, but my class pictures tell a different story. "Draw in the missing eyeballs and this one might not be so bad," my mother would say. In group shots I was easily identified as the blur in the back row. For a time I thought that if I accompanied my habits with an outlandish wardrobe, I might be viewed as eccentric rather than just plain retarded. I was wrong. Only a confirmed idiot would wander the halls of my high school dressed in a floor-length caftan; as for the countless medallions that hung from around my neck, I might as well have worn a cowbell. They clanged and jangled with every jerk of my head, calling attention when without them I might have passed unnoticed. My oversized glasses did nothing but provide a clearer view of my rolling, twitching eyes, and the clunky platform shoes left lumps when used to discreetly tap my forehead. I was a mess.

"College is the best thing that can ever happen to you," my father used to say, and he was right, for it was there that I discovered drugs, drinking, and smoking. I'm unsure of the scientific aspects, but for some reason, my nervous habits faded about the same time I took up with cigarettes. Maybe it was coincidental or perhaps the tics retreated in the face of an adversary that, despite its health risks, is much more socially acceptable than crying out in tiny voices. Were I not smoking, I'd probably be on some sort of medication that would cost the same amount of money but deny me the accoutrements: the lighters I can thoughtlessly open and close, the ashtrays that provide me with a legitimate reason to leave my chair, and the cigarettes that calm me down while giving me something to do with my hands and mouth. It's as if I had been born to smoke, and until I realized it, my limbs were left to search for some alternative. Everything's fine as long as I know there's a cigarette in my immediate future. The people who ask me not to smoke in their cars have no idea what they're in for.
```

---

## IC-1402: Pointlessness and Boy Perfume from Drums, Girls and Dangerous Pie

- Title: Pointlessness and Boy Perfume from Drums, Girls and Dangerous Pie
- Author (byline): Jordan Sonnenblick
- Work: Drums, Girls and Dangerous Pie
- Publisher: DayBue Publishing
- Publication date as stated: May 2004
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2624
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jordan Sonnenblick
Book: Drums, Girls and Dangerous Pie
ISBN: 096689409X
Publisher: DayBue Publishing
Date (Month/Year): May 2004
```

### Introduction (context only: never use it for content warnings)

```text
During hard times it’s easy to wallow in self-pity and only think about getting what you want. But, sometimes, even in times of trouble it’s about denying what you want for the good of another…for the good of your brother. “Pointlessness and Boy Perfume” by Jordan Sonnenblick
```

### Performance text (classify this)

```text
If you had a father who hadn't shown any emotion for three or four months, and then you stumbled upon him weeping as though someone had just shot Bambi right in front of his eyes, what would you do? Right-you would sneak away, and never let on that you had seen anything. And that's what I did. I crept back into the basement like a highly skilled sneak thief, and then proceeded to listen to the most calming music I know: the Beatles. Somewhere between "Revolution" and "Hey, Jude" I fell asleep. When I awoke in a small puddle of my own drool on the ratty playroom carpet with my left earphone seemingly welded to my head by the force of gravity, I looked at the Zildjian cymbal clock my parents once got me for a birthday. It was 11:45 p.m. I felt pretty sure of two things: nobody had noticed that I was hidden away in the dark basement like a leper, and everybody would be asleep when I went upstairs this time. For a change, I was doubly right. In the kitchen, I couldn't help but notice that my dad's mysterious pile of depressing papers was just sitting on the table, in plain view. To see or not to see? That was the question. Well, for about a tenth of a second, anyway. Then I dove on those papers like Sherlock Holmes on a cappuccino binge. What I was looking at, what had turned my strong, silent dad into a weepy mass of pudding, was a stack of bills. Medical bills. Jeffrey's bills. The top sheet, which was written in my dad's handwriting, was a tally of the total unpaid amount to date: $27,000. The total expenses so far were unbelievable, definitely in the six-figure range. If not for the fact that my parents both had good health insurance (which I knew from overhearing some discussions about this stuff), we would already have blown the whole cost of a college education in these three months-and I knew Jeffrey was going to need at least three YEARS of treatment. As it was, I figured I'd be attending the "University of 'Would You Like Some Fries With That?'" There was no way either of us would have any kind of college fund at the end of this. Then I had an even more depressing thought: Jeffrey might not be around long enough to go to college.

OK, so we were losing money hand-over-fist, my dad was crumbling like a day-old scone, and my brother might die. Really, what could I do about any of it? At the moment, the only answer I could come up with was, "Nothing."

I went upstairs to get ready for bed, and a new obsessive slogan started running through my mind. It worked like this: "OK, I'll brush my teeth now. But Jeffrey might die, so what's the point? Time to wash my face. But Mom's not working, Dad makes maybe $40,000 a year after taxes, and there's $27,000 in unpaid bills downstairs. We're going to be homeless any minute-so what's the point? I should floss now too, but I didn't even brush, so what's the point?" So I went to bed with a grimy face and yuck-encrusted teeth. And that was just the start of my depressing "What's the Point?" period.

The next day, I came back from my week of absence to a barrage of "oh my god what's wrong with Jeffrey is your mom okay how's your dad taking it what you were sick oh." You can imagine that that didn't snap me out of my funk too well.

Renee talked with me all through homeroom, which should have made me ecstatic, but I just kept thinking, "Soon I'll be leaving school to go live under an overpass, so what's the point of Renee liking me now?" Also, somewhere in the back of my mind I was realizing that she hadn't suddenly discovered that I was an actual human - being-type-person because of any new attributes I had developed; she was just fascinated by me as a tragic figure, for the moment. I still couldn't help going gaga over how beautiful she was, but I was almost mad at her, because she wasn't noticing me for the right reasons.

Annette was truly concerned about me, though. In Miss Palma's class, she offered to come over after school a few days that week and catch me up on my classwork in every subject we had together. That was pretty comforting, because I didn't want to fail all of my finals after the massive make-up effort I had done before my flu episode, and Annette always got A's in everything.

There was one problem: my math period was Annette's piano period, so who would bail me out in math? I was tempted to say, ''I'm going to fail the hardest subject anyhow, so what's the point?" I didn't, though-I was determined to pull all of my grades through this so I wouldn't add to my parents' worries. In math class, I went to the teacher and told him I would need help if I wanted to learn the week of new material I'd missed. I was torn between hoping he'd offer to meet me during our opportunity period and teach me the stuff himself, and being afraid that spending that much time one-on-one with a math teacher would crack me completely and turn me into a deranged lunatic. "Oh, well," I figured, "At least I'll be the life of the under-bridge party crowd then."

The teacher did not offer to catch me up, though. Instead, he asked for a volunteer who was willing to tutor me at home. And he got one: Renee Albert. Holy cow. Renee Albert was coming to my house! RENEE ALBERT WAS COMING TO MY HOUSE! Even I couldn't think, "What's the point of Renee Albert coming to my house?" with a straight face. I just said, "Wow, thanks, Renee!" while every other guy in the class looked at me like I had a big target painted on my forehead.

It was one of my drum lesson days with Mr. Watras, and when I walked in he handed me a crumpled tissue, pointed to the garbage can, and told me to show him my newfound hoops skills. I got it in - swish! - and sat down at the drum set. It was a great feeling to be playing drums after more than a week away from them, and Mr. Watras must have understood because he just sat back and watched me burning around the kit at full speed for a couple of minutes. When I stopped, he surprised me by talking about my academic situation, which we had never discussed again after the ugly meeting I'd had with my teachers.

So, I hear you've made up all of your old work.

Yeah.

Do you have a plan .for making up the work you missed last week and studying for the final?

Yes, Annette is going to tutor me in everything except math, and this, um, other girl is going to help me with the math.

Great! Listen, Steven, I'm really glad you're back on track with this school stuff. We absolutely depend on you in All-City, and I'm thrilled that we can keep you in the ensemble.

Me, too.

But part of me was thinking, "What's the point of practicing for a stupid concert when my brother might not live to see it?"

The week went by like that, with me going to school, my mom and Jeffrey coming and going between home and Philly, my dad staring off into space even more than he had been for months. I kept having those, "What's the point of . . ." moments, but plugged away at life pretty consistently anyway. And Annette came by three times to help me study.

You know what? She's an amazing tutor. I understood everything when she explained it, and got hundreds on a social studies quiz and a science lab thanks to her. There was an awkward moment when she first saw Jeffrey, because it was her first time seeing him all bald and puffy, but she covered her shock well. And by the second night, she was playing board games with him every time she took a break while I did practice quizzes or writing assignments. He was happy with the attention, and I noticed something interesting: she was much more patient and honestly excited to play with him than I was.

So Annette was the absolute perfect tutor-pal, and I should have been kissing the ground beneath her feet and carrying her book bag to school every day, right? But even while I was getting so much from her, I couldn't stop thinking about next week when Renee would be coming over.

On Thursday night of that week, Mom and Jeffrey left for a quick two-day trip to Philly for blood counts and a couple of chemotherapy injections. The procedures were pretty routine by then, but the results weren't. Jeffrey's counts were really low, so low that the doctors gave him two transfusions: one of whole blood, and one of platelets. This turned the two-day trip into a four-day trip. I heard my dad on the phone saying that the hospital bills were running about $2,000 a night, so I knew our financial picture wasn't getting any rosier. Also, my mom told me that Jeffrey would probably be even more vulnerable to germs for the foreseeable future, so I should be extra-careful to avoid being near anyone who was sneezing or coughing, and wash my hands when I walked into the house every day. I asked if I should just stay home and live in a plastic bubble with Jeffrey, and she warned me that I might, in fact, have to stay out of school for a while if something like chicken pox started going around.

So I was freaking out. On the one hand, my head was a mess of tumbling worries: rising poverty, falling blood counts, alarming potential for quarantine. On the other hand, Renee was coming! RENEE WAS COMING! To! My! HOUSE!

Tuesday was the big day. Midterm exams were a week away, so I needed Renee's help pretty big-time. Also, I couldn't get past the excitement part of the deal: Renee! In my house! I missed math for a drum section rehearsal (you really have to love the logic of getting called out of math for band right before exams), and Renee wasn't on the bus on the way home from school. So we didn't confirm that she would be coming over, but I assumed the plan was on for 7 p.m., which was what we had arranged the week before.

I ate with my mom and Jeffrey at six; my dad was still at his office. It was the beginning of tax season, when accountants get busier and busier leading up to April 15th. I figured we could use some extra income, so I was betting my dad would be really busy this year. Anyway, my mom noticed that I was being quieter than usual, and Jeffrey started in: He’s saving up all his smooth talking for his big date with Renee Albert! It's not a date nut-ball, she’s just tutoring me in math. I bet you're gonna kiss her, right? She has a boyfriend, Jeffrey. You know that. She’s still going out with Biff, the guitar player. But she’s coming over to play with you.

She's not playing with me, she’s teaching me about numbers and stuff.
So when are you going to kiss her then?
MOM! The kid is out of control. Can't we get him dome tranquilized or something?
Then my mom got rolling:

Steven, is there something going on between you and Renee? I notice you're dressed more neatly than usual, and your hair is even combed down.

And he’s wearing boy perfume, Mom. He wasn’t wearing any last week when Annette came over, but for RENEE he is.

It’s called cologne, monkey boy!

Since when do you wear cologne to learn math? Oh, my son is growing up right in front of my very eyes. Maybe I should get out the video camera.

Maybe you should tie me to a stake, douse me in kerosene and torch me right on our front lawn.

I won't need any kerosene, Steven –I’m sure the cologne will go up pretty fast.

Ha ha, Mom. Just then the doorbell rang.

Please keep the lunatic away from us, Mom. We have work to do.

Is it hard work or easy work Steven? MOM! REMOVE HIM!

I went to answer the door, and when I opened it, Renee was standing there, all bundled up against the winter, with a few snow-flurry flakes on her jacket. Her cheeks were flushed from the wind, and her hair was blowing around. I just wanted to reach out and brush the strands away from her face, but that didn't seem like a good tutorial beginning, plus Biff looked like the kind of guy who could rip my arms off and use them as toothpicks. So I just said hi instead.

She said hello back, and I was just about to step aside and let her in. But just then, she sneezed. And coughed. And sneezed again.

Excuse me, Steven. I'm coming down with dome kind of virus thing, I think. I went home early from school today, and skipped cheering but I did't want to stand you up. You have too many big problems going on, I just couldn’t let you down. So I'm here. Let’s get to work!

I blocked the doorway with my body, and said something that seemed to float up from a place beyond my worst nightmares:

Renee, I can't let you in.

What do you mean? It’s cold out here, and we've got a lot to do.

I mean, I'm sorry, but I can't let you come into this house. You’re sick, and Jeffery can’t get sick right now.

Steven, you're being ridiculous. It’s probably just a cold, anyway.

A cold could put my brother in the hospital.

Steven, what’s really going on? Do you hate math so much you just can't stand it? Do you want to fail the final? Then I wish you would have told me that before I came stomping through the snow to come over here.

Renee, I’m serious, this isn’t about math.

And it can't be about ME. Any boy in the school would be drooling to have me come over. And everybody says you've had a crush on me since third grade, haven't you? Now just let me in!

I'm sorry, Renee. Do you want me to call your mom to come get you?

Without responding to me directly, she spun around on her heels like the dancer she was, and marched away. I could hear her muttering about me all the way to the end of the driveway:

Ugghh! I walk to the boy’s house in a BLIZZARD and he doesn’t even let me in! He drools over me for half a DECADE but when I deliver myself to his front door he slams it in my face! I will NEVER understand boys! At that point, she fired a parting shot over her shoulder: Go ahead, then, fail math, and be lonely the rest of your life. As I slumped against the doorframe, staring at her back and wondering how she could be so graceful in snow boots and a parka when she wasn't even feeling well, Jeffrey came up behind me.

You know, Steven, you were right. I guess you aren't going to kiss her.
```

---

## IC-1403: Poof! No Eyebrows!

- Title: Poof! No Eyebrows!
- Author (byline): Patrick F. McManus
- Work: Never Sniff a Gift Fish
- Publisher: Owl Books
- Publication date as stated: Sept 1984
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: PAT, MILT, BUN, MOM, MR. GROGAN, RETCH, MUZZLELOADER, SHERIFF
- Teaser before the introduction: No
- Spoken words (computed): 2317
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
Let’s face it -- young guys need to explore, hunt, and conquer! It’s in our nature to have a go at the impossible, and if lucky, to come off with a victory. It’s a part of discovering manhood. The old saying goes - “better to have tried and failed than to have never tried at all”. If guys didn’t have a sense of adventure, if we were complacent with not taking a risk, and if men didn’t take on danger, then the world would not be as it is today. Think about it. What would things be like if Edison didn’t explore the idea of a light bulb because he was too scared of being electrocuted? OK, I admit sometimes things do go wrong . . . Poof! No Eyebrows! By Patrick F. McManus.
```

### Performance text (classify this)

```text
PAT: Just as I was assembling the ingredients for a small snack in the kitchen, the doorbell rang My wife, Bun, went to answer it, and I heard her invite in Milt Slapshot, a neighbor who often seeks out my advice on matters pertaining to the sporting life.

MILT: Is Pat home? A fella told me he knows something about muzzleloading

PAT: Realizing Bun could never resist a straight line like that, I jumped up and headed for the living room in the hope of stifling her.

BUN: (laughing) Does he ever! Why, this very minute he's out in the kitchen loading his muzzle!"

PAT: A wife who chortles is an irritation, but one who also regards herself as wit is a social nuisance. I grabbed Milt by the arm and guided him toward the den before Bun could embarrass the poor fellow further with another attempt at emulating Erma Bombeck. (To Milt) Stop the cackling, Milt, it only encourages her. (To audience) Once his tasteless display of mirth had subsided, Milt explained that he was building a muzzleloader and needed some technical advice from me. A mutual acquaintance, one Retch Sweeney, had told him that I had once conducted extensive scientific research on primitive firearms. That was true. In fact, it would be difficult to find firearms more primitive than those utilized in my research. (to Milt) You've come to the right man. Yes, indeed. Now the first thing I need to know is, are you building it from a kit or from scratch?"

MILT: A kit.

PAT: Good. Building muzzleloaders from scratch is a risky business, particularly when you work your way up to sewer pipe too soon. Now the first thing . . .

MILT: Sewer pipe? What do you mean, sewer pipe? Are you sure you know something about black powder?

PAT: Ha! Do you see my eyebrows?

MILT: No.

PAT: Well, that should answer your question. All us experts on black powder have bald eyes. (to audience) Actually, I do have eyebrows, but they are pale, sickly fellows, never having recovered from the shock of instant immolation thirty years ago. Having my eyebrows catch fire ranks as one of the more interesting experiences of my life, although I must say I didn't enjoy it much at the time. Indeed, my somewhat faulty eyesight may be a direct result of having my eyebrows go up in smoke. Either it was that or the splash of Orange Crush soda pop with which my sidekick Retch Sweeney, ever quick to compound a catastrophe, doused the flames. As I explained to Milt, who had settled into a chair in the den and was attempting with some success to conceal his fascination, most of my early research into the mysteries of black powder took place during the year I was fourteen. Some of those experiments produced spectacular results, particularly the last one, which enabled Retch and me to attend the annual Halloween party as twin cinders.

The first experiment, in which my eyebrows were sacrificed to the cause of science, consisted of placing a small pile of black powder on a bicycle seat and touching a lighted match to it. I can no longer recall why a bicycle seat was employed as part of the apparatus, but I am sure my co-researcher and I had sound reasons for it at the time. In any case, we proved conclusively that a match flame serves as an excellent catalyst on gunpowder. I later concluded that the experiment might have been improved upon in only two ways: to have placed the powder on Retch's bicycle seat and to have let him hold the match. Instead, he chose to stand in awe of the experiment and about ten feet away, sucking absently on a bottle of Orange Crush. On the other hand, my sacrifice was not without its reward, since bald eyes and a hole burnt in my bicycle seat made great conversation openers with girls at school. The success of the experiment had to be withheld from the rest of the scientific community for fear our parents would find out about it. Unfortunately, my mother inadvertently discovered the secret.

MOM: Is anything the matter?

PAT: No. Why do you ask?

MOM: Oh, nothing in particular. It just seems a little odd, your wearing sunglasses and a cap at the dinner table.

PAT: She then expressed her desire that I remove both glasses and cap instantly, sooner if possible. After some debate over the finer points of dinner-table propriety, I complied. As expected, Mom responded with the classic question favored by the parents of young black powder experimenters everywhere:

MOM: WHAT HAPPENED TO YOUR EYEBROWS?

PAT: Looking surprised and fingering the scorched area above my eyes, I tried to convey the impression that it was news to me that my eyebrows were missing, as if they might have dropped off unnoticed or been mislaid at school.

The truth was soon extracted from me with an efficiency that would have been the envy of medieval counterintelligence agents. This was followed by a bit of parental advice. But scarcely had this parental advice ceased reverberating among the rafters than I was already plotting my next experiments for unlocking the mysteries of black powder. The discovery by Retch and me that we could purchase black powder in bulk from a local dealer was to have great impact on our lives, not to mention various parts of our anatomies. The dealer in question was the proprietor of Grogan's War Surplus, Hardware & Gun Emporium, none other than the old reprobate, Henry P. Grogan himself. We weren't at all sure Grogan would sell a couple of scruffy, goof-off kids something as potentially dangerous as black powder. Our first attempt at making a purchase was, therefore, cloaked in subtlety and subterfuge.

PAT: Howdy, Mr. Grogan.

MR. GROGAN: Howdy, boys. What can I do for you-assuming, of course, you got cash in your pockets and ain't just here to finger the merchandise?

PAT: Oh, we got cash, Uh, Retch, why don't you read Mr. Grogan our list?

RETCH: Uh, okay, heh, heh. Yeah, well here goes-one GI mess kit, one helmet liner, a parachute harness, a pound of black powder, and let's see, now, do you have any of those neat camouflage jackets left?

PAT: To our chagrin, a look of concern came into Grogan's eyes.

MR. GROGAN: "Gosh, boys, I don't know if I should . . . It just don't seem right to sell you two young fellows . . . Oh, what the heck! Elmer Peabody wanted me to save those last two camouflage jackets for him, but I'll let you have 'em. Now how much gunpowder was that you wanted--a pound?

PAT: In all fairness to Grogan, I must admit that he did warn us that severe bodily harm could result from improper use of the black powder. His exact words, if I remember correctly, were,

MR. GROGAN: You boys set off any of that stuff near my store and I'll peel your hides!

PAT: The black powder we bought from Grogan had been compressed by the manufacturer into shiny black pellets, a form intended, I believe, to make it less volatile. Even before mashing them into powder, we found it was possible to touch off the pellets if they were first piled on a bicycle seat and a match held to them. The pellets did not ignite immediately even then, apparently for the purpose of tricking the person holding the match into taking a closer look at what was occurring on the bicycle seat. Then--poof!--no eyebrows. Our first muzzleloaders were small and crude, but as our technological skill and knowledge increased, they gradually became large and crude. We never did develop a satisfactory triggering mechanism. On the average shot, you could eat a sandwich between the time the trigger was pulled and the gun discharged. A typical muzzleloader test would go something like this:

RETCH: Okay, I'm going to squeeze the trigger now. There!

MUZZLELOADER: Snick! Pop! Ssssss . . .

PAT: Good. It looks like it's working. Better start aiming at the tin can.

MUZZLELOADER: Ssss . . .fizt . . .sss . . .

RETCH: Say, give me a bit of that sandwich, will you?

PAT: Sure.

MUZZLELOADER: . . .sss . . .sput . . . ss . . . putt . . . ss . . .

RETCH: What time is it?

PAT: About time for me to—

MUZZLELOADER: . . . ssst--POOT!

RETCH: (enveloped in cloud of smoke): How was my aim?

PAT: I think it was pretty good, but the muzzle velocity leaves something to be desired. As soon as the smoke clears, reach over and pick up the ball and we'll load her up again.

Even as we increased the range of our muzzleloaders, the delay in the firing mechanism discouraged us from using them on game. If we had used one of them for rabbit hunting, say, we would have had to squeeze the trigger and then hope a rabbit would happen to be running by when the gun discharged. Squeezing the trigger before your game appears over the far horizon is the ultimate in leading a moving target. Since we had up to three minutes of lead time on stationary targets, hunting with our muzzleloaders seemed somewhat impractical. There was also the probable embarrassment of having our shots bounce off the game. It didn't seem worth the risk. A hunter can stand only so much humiliation. Our first muzzleloader was a small-caliber derringer, the ammunition for which consisted mostly of dried peas. This prompted Retch to remark derisively to a tin-can target

RETCH: All right, Ringo, drop your iron or I'll fill you full of dried peas.

PAT: Okay, okay, I get your drift. We'll move up to the hard stuff--marbles, ball bearings, golf balls. (to audience) It was a mistake, though, and I knew it. Once you start escalating, there's no stopping until you achieve the ultimate weapon. Within a couple of months, we were turning out muzzleloaders in the .80-caliber range. Then we got into the large-caliber stuff. Finally, we decided the time had come to stop monkeying around with black powder pistols and rifles. We'd had some close calls. We had reached a point where there was some doubt in our minds whether we might be firing a muzzleloader or touching off a bomb. Thus it was with considerable relief that we abandoned our clandestine manufacture and testing of pistols and rifles. After all, a cannon would be much safer; you didn't have to hold it. The cannon was constructed of sewer pipe, tow-by-fours, baby-carriage wheels, rubber inner-tube bands, a clothespin, baling wire, and various other odds and ends, all of which, blending into a single, symmetrical unity, neared perfection on the scale of beauty. A croquet ball was commandeered from the Sweeney backyard for the use as shot. In our enthusiasm of the moment, it was thought the croquet ball could be returned to the set after it was recovered from the firing range. Alas, it was not to be so. Attired in our muskrat-skin hats, which we had sewn up ourselves, we mounted our bicycles and, with cannon in tow, wet off for the local golf course, where a fairway would serve as a firing range, a putting green as a target. As we had hoped, the golf course turned out to be deserted. We quickly wheeled the cannon into firing position and began the loading procedure.

RETCH: Think that's enough powder?

PAT: Better dump in some more. That croquet ball is pretty heavy.

RETCH: And there's some for good measure.

PAT: The croquet ball fit a little too tightly, but we managed to ram it down the barrel. Then we both took up positions alongside the cannon to witness the rare and wonderful spectacle of a sewer pipe firing a croquet ball down a golf-course fairway. "Ready, aim, fire!" Retch tripped the firing mechanism. Eventually, the thunder was replaced by clanging bells inside our heads, the shattered pieces of earth and sky fell back into place, and the wobbly world righted itself. Retch and I limped over to the side of a utility shed and sat down to relax a bit and collect our senses. Presently, a deputy sheriff drove up. He stood for a moment gazing at the haze of smoke wafting gently over the golf course, the patch of smoldering turf ringed by fragments of sewer pipe, baby carriage wheels, and pieces of two-by-four. Then hoisting up his gun belt, he sauntered over to us.

SHERIFF: You boys know anything about an explosion out this way?.

RETCH: What kind of explosion?

SHERIFF: A big explosion.

PAT: I was still so stunned I couldn't even think up a good lie. Anyway, I knew the deputy had us cold.

SHERIFF: Now, what I want to know is why are you two boys sitting out here behind this shed smoking?"

PAT: Shucks, if you'd been a little earlier, you'd have seen us while we were still on fire!" I thought for sure he was going to haul us off to jail, but instead he just smiled, took one last look at the smoldering debris, and started to saunter back to his car.

SHERIFF: Well, if you fellas turn up any information about the explosion, I'd appreciate it if you'd let me know. I don't reckon there'll be another one, do you?

PAT: Then the deputy stopped and kicked gingerly at something on the ground in front of him. It was Retch's muskrat hat! The deputy turned and gave us a sympathetic look.

SHERIFF: Too bad about your dog.

PAT: The cannon petty well quelled our enthusiasm for building our own muzzleloaders from scratch. Not only had it made a big impression on us; it had made numerous small impressions. Years later, while I was undergoing a physical examination, the doctor commented on some bumps under my skin. (to Doctor) Pay them no mind, doc, they're just pieces of sewer pipe. (to audience) At this juncture of my recitation, Milt Slapshot jumped up and headed for the door.

MILT: Thanks. You've answered my question.

PAT: Gee, I've even forgotten what the question was. But if you need any help putting your muzzleloader kit together, Milt, just give me a call. (to audience) He hasn't called yet. I suppose he's been tied up at the office a lot lately.
```

---

## IC-1404: Ready to Wear

- Title: Ready to Wear
- Author (byline): Dave Barry
- Work: Not specified
- Publisher: The Miami Herald
- Publication date as stated: Sunday, May 7, 1995
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: TODAY'S TOPIC IS, DOCTOR, NURSE
- Teaser before the introduction: No
- Spoken words (computed): 868
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Barry
ISBN: Newspaper
Publisher: The Miami Herald
Date(Month/Year): Sunday, May 7, 1995
```

### Introduction (context only: never use it for content warnings)

```text
The latest buzzword making its way across both cyberspace and regular space is "metrosexual". What's the definition of metrosexual? Some define metrosexual as "a straight man in touch with his feminine side". Others define it with more specificity, such as "a straight man, who lives in an urban environment, who is into designer clothes, art museums, musicals, and other non-macho pursuits."

Are you only a real man if you wear ratty old clothes and spend all your free time watching football on TV? Dave Barry address this tounge-in-cheek question in “Read to Wear.”
```

### Performance text (classify this)

```text
TODAY'S TOPIC IS: Fashion Tips for Men. This topic was suggested by a letter from John Cog of Norfolk, Va. Here's the entire text:

"How come when I'm standing in front of a full-length mirror with nothing on but socks, white socks look OK, but dark- colored socks make me look cheap and sleazy?"

This letter was passed along to me by my Research Department, Judi Smith, who attached a yellow stick-on note that says: "This is true." Judi did not say how she happens to know it's true; apparently -- and I'm sure there's a perfectly innocent explanation -- she has seen John Cog of Norfolk, Va., wearing nothing but socks.

But the point is that dark socks, as a lone fashion accessory, create a poor impression. This is a known fact that has been verified in scientific experiments wherein fashion researchers put little white socks on one set of naked laboratory rats, and dark socks on another, then exposed both groups to a panel of leading business executives such as Bill Gates, who indicated that they would be "somewhat more likely" to hire from the white-sock group, should their personnel needs ever include a rat.

What this means, men, is that if you're dressing for an important job interview, church supper, meeting with my Research Department or other occasion where you could wind up wearing nothing but socks, they should be white.

Likewise, if you're going to be wearing just your underwear, you should always tuck your undershirt way down into your underpants. This is the "look" favored by the confident, sharp-dressing men found in the underwear section of the now- defunct Sears catalog, who are often depicted standing around in Rotary-Club-like groups, looking relaxed and smiling, as if to say: "Our undershirts are tucked way down into our underpants, and we could not feel better about it!"

These men live in Sears Catalog Men's Underwear Town, where all the residents, including on-duty police officers, wear only underwear. All the residents are always in a good mood because they live only a few pages away from Sears Catalog Women's Underwear Town, which is occupied by hundreds of women who stand around all day wearing nothing but brassieres and underpants and thinking nothing of it. Sometimes, late at night, they all get together for wild parties in the Power Tools section.

The happy mood in the Sears underwear towns stands in stark contrast to the mood in Calvin Klein Perfume-Ad Town, where you'd think people would be ecstatic, because they're always writhing around in naked co-educational groups like worms in a bait bucket, but they always have troubled expressions on their faces, as if they're thinking: "Somebody in this co-educational group had Mexican food for lunch."

One last underwear tip: No doubt your mom always told you that your underwear should be clean and free of holes or stains, because you might get in a car crash and be taken, unconscious, to the hospital, and people would see your underwear and possibly ridicule it. Your mom was absolutely right, as we can see from the following unretouched transcript from the emergency room of a major hospital:

DOCTOR: What do we have here?

NURSE: We have a car-crash victim who has severe head trauma and a broken neck and massive internal injuries and is spewing blood like a fire hydrant.

DOCTOR (briskly): OK, let's take a look at his underwear . . . WHOA! How do you get Cheez Whiz THERE?

(Laughter from everybody in the emergency room, including gunshot victims.)

* * *

Our final fashion tip for men concerns those special occasions when, for whatever reason, you want to wear something on top of your underwear. What style of clothing is right for you? The answer -- taking into consideration your particular age, build, coloring and personality -- is: "clothing that has been picked out by a woman." Because the sad truth is that males, as a group, have the fashion sense of cement.

Oh, I realize that there are exceptions -- men who know how to pick out elegant suits and perfectly color-coordinated accessories. But for every man walking around looking tasteful, there are at least 10 men walking around wearing orange plaid Bermuda shorts with non-matching boxer shorts sticking out above AND below, and sometimes also poking out through the fly.

Men are genetically programmed to select ugly clothing. This dates back millions of years, to when primitive tribal men, responsible for defending their territory, would deck themselves out in face paint, animal heads and nose bones, so as to look really hideous and scare off enemy tribes. If some prehistoric tribal warriors had somehow got hold of modern golf clothing, they would have ruled the rain forest.

In conclusion, men, please remember that the fashion tips contained in this column are just the "basics." To learn more about the current men's fashion "scene," get a copy of Esquire or GQ and study the ads and articles presenting the latest styles, making a mental note to never, ever wear any of them, because unless you're a male model, you'd look stupid. Just wear a regular blue suit like everybody else and try to have both shoes the same color. You can get that Cheez Whiz out with bleach.
```

---

## IC-1405: Red Diaper Baby

- Title: Red Diaper Baby
- Author (byline): Josh Kornbluth
- Work: Not specified
- Publisher: Mercury House Publishing
- Publication date as stated: Oct 1996
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: FATHER, JOSH, MOTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1842
- Already set (do not supply): none

### Source block (context only)

```text
Author: Josh Kornbluth
ISBN: 978-1562790875
Publisher: Mercury House Publishing
Date (Month/Year): Oct 1996
```

### Introduction (context only: never use it for content warnings)

```text
It's a morning in the mid-1960s, and 6-year-old Josh Kornbluth is woken by his father, Paul, in the usual manner -- with Paul bursting naked into Josh's room and singing "The Internationale." So begins this raucous tale of a young American communist's coming-of-age The true story of a boy whose dream is to lead a revolution. Quite a challenge, especially for such a shy, chubby kid.

Red Diaper Baby by Josh Kornbluth
```

### Performance text (classify this)

```text
FATHER: (Singing)* Arise, you prisoners of starvation! / Arise, you wretched of the earth! For justice thunders condemnation. / A better world's in birth.

JOSH: My father, Paul Kornbluth, was a Communist. He believed there was going to be a violent Communist revolution in this country -- and that I was going to lead it. Just so you can get a sense of the pressure.

JOSH: Anything my father told me I'd believe, because my father was such a physically magnificent man: he was big, and he had this great big potbelly -- not a wiggly-jiggly, Social Democratic potbelly; a firm, Communist potbelly. You bopped it, it would bop you back. It was strong.

I would have loved to have slept in late on the weekends, but I couldn't because my father wouldn't let me. He'd come bursting into my room and running up to my bed, looming over me he'd sing: Arise, ye prisoner of starvation! Arise, ye wretched of the earth! I didn't know that was the international Communist anthem. I thought it was my own personal wake-up song. I knew from an early age that one day I must grow up and lead the Revolution!

My father had his own language -- not only his own English, but his own Yiddish. I used to think it was real Yiddish, but my mom would say

MOTHER: What your father speaks is not Yiddish. I went to Yiddish school and what your father speaks is not Yiddish.

JOSH: In my father's Yiddish, there was a term ouska -- a prefix, meaning "a lot of," "very"

FATHER: I am ouska-cold, my son!"

JOSH: (to father) Of course you're ouska-cold, Dad; the window is ouska-open."

Dad and I would sit around the kitchen table having hard-boiled eggs (my father, not a soft-boiled kind of guy). And Dad would regale me with his stories of organizing with the Henry Wallace campaign. (That's **Henry Wallace. Henry. Okay?) And he'd drill me in the catechisms of our faith of Communism. Like how society has been driven from one stage to the next, driven inexorably by the forces of dialectical materialism, until ...

According to Marx and Engels -- and my dad -- the first human society was Primitive Communalism: everyone's just kind of dancing around, like at a Grateful Dead concert.

The next stage after Primitive Communalism was Slavery -- which must have been a bummer of a transition.

Then from Slavery to Feudalism, and from Feudalism ... Well, we've learned from history that it's very important after Feudalism to stop in Capitalism before moving on to Socialism. Very important to stop in Capitalism. Because that's where you get your appliances.

So you stop in Capitalism, you get your stuff, and then you move on to Socialism, and finally to Communism -- and you're back at the concert.

All along the walls of our kitchen, bathroom, living-room and dining-room area were posters of our heroes, our gods: W. E. B. Du Bois, Malcolm X, Dr. King, Ho Chi Minh, Bertolt Brecht, Emma Goldman . . . And at the end of all these posters: my height chart.

And we'd go outside for our walks. When we went outside, my father -- in his one true concession to society -- would put on clothing. This was back in '65, when I was about six years old; and being Communists, we had songs associated with every activity. Me and Dad didn't just have generic walking songs; we had specific going-up-the-hill songs, specific going-down-the-hill songs.

We learned our biggest going-up-the-hill song off an album by Paul Robeson, a great Jewish folksinger. It was a record my dad had borrowed from the public library, and then -- as a revolutionary act refused to return. (And my mom was a librarian!)

Going downhill, [we] would sing: ***As I go down in the valley [to the river] to pray / Studying about that good old way / And who shall wear the robe and crown / Good Lord, show me the way!

My father couldn't hear me. He didn't connect it with the fact that he was singing so ouska-loud he was drowning me out. So periodically he'd turn to me on the sidewalk and go

FATHER: Sing louder, my son-I can't hear you! (singing loudly) Come on, fathers, let's go down! / Down in the valley to pra-a-a-ay ... to pray-yee! (declaring emphatically) And a child shall lead them!

JOSH: A nice, cheerful walking song-though confusing lyrically, to an urban child. (beat) We had to live ouska-cheaply. Because my father . . . Well, he was a schoolteacher -- a very good schoolteacher with great passion, but at the same time he would be developing this anger towards his bosses: the principal, the assistant principals, the school board. And this anger at his bosses would build and build, until finally Dad couldn't take it anymore. This would take about two weeks. And at the end of those two weeks, Dad would go storming into the principal's office and yell

FATHER: F*** you!

JOSH: Often the guy would never have seen my dad before. And he'd say, "You're fired! ... If you work for me, you're fired!" And then Dad would get another job, and he'd be teaching his new students with great passion but developing this anger towards his new bosses. And at the end of two weeks he would storm into his new principal's office and go

FATHER: F*** you!

JOSH: And the new principal would go; "You're fired!" This went on for years and years; my father never saw the pattern. He never saw the cause-and-effect between "F*** you!" and "You're fired!" So we had to live ouska-cheaply. Which was fine with me: I loved ouska-cheap adventures, like the Museum of Natural History -- where at the time the admission was whatever you would care to donate. They've since changed that policy; I think because of my dad.

FATHER: Pay them a penny and not a penny more!

JOSH: We'd go running to the dinosaur exhibit, where Dad would give me a tour. I don't think he was an expert in the field, but . . .

FATHER: The Tyrannosaurus rex, my son-one of the largest . . . reptilian(s) ever to walk the earth!

JOSH: And other little kids would break away from their field trips and join us. [It] was a lot more interesting the way my dad described it. (beat) And then, after a weekend of this kind of ouska-fun, my dad -- as the courts had mandated -- had to return me to . . . my mom -- Bernice "Bunny" Selden: also Jewish, also a New Yorker, also a vollege grad, also a Communist -- but so different from my father in temperament. If my father was an out-there, ouska-Communist, my mom was ... inska.

And she had her own inska-wake-up song for me, too. And like I thought Dad had written the "Internationale" for me, I thought my mom had written her wake-up song for me; I only found out years later that Irving Berlin wrote it.

She'd go into the bathroom in her nightgown and come back out with her hair in a bun. And she'd stand in my open doorway -- which was easy for her to do, because for some reason she would not let me have a door. She'd tiptoe to my bed and lean down and sing:

MOTHER: (singing) ****Oh, how I hate to get up in the morning / Oh, how I'd love to stay in bed
For the hardest blow of all / Is to hear that bugler call:
"You gotta get up, you gotta get up; You gotta get up in the morning.
You gotta get up, you gotta get up, You gotta get up in the morning."

JOSH: A pretty nice wake-up song. Unless you know the second verse, which gets to a surreal level of violence . . .

MOTHER: (singing) Someday I'm gonna murder the bugler / Someday you're gonna find him dead / I'll amputate his reveille / And stamp upon it heavily/ And spend the rest of my life in bed!

JOSH: I thought she could snap at any moment. So I'd get out of bed; I didn't want my reveille amputated! (beat) But I still didn't have that get-up-and-go that the "Internationale" gives a kid. She'd guid lead me into the living room and sit me down on the couch. She had this little motherly trick she'd play to get me going in the morning: she'd serve me a tall cup of double-espresso with whipped cream and a maraschino cherry on top.

And I'd sit there sipping my double-espresso on the couch, beneath the half-dozen ceramic disks that she bought in Mexico, where she went to divorce my dad -- which, by the way, was when I was six months old.

They were married for nine years, then I was born. Then, when I was six months old, they divorced. From time to time I'd wonder why. (beat) A few months ago, I was reading this article about a guy named Saul Newton, a crazed psychoanalyst who ran this cult called the Sullivanians. They had a co-op on the Upper West Side. (thoughtfully) Saul Newton . . . Saul Newton -- and suddenly it hit me: Wait a second! My dad's therapist was named Saul! So I called up my mom and said, "Mom, I'm reading about this Saul Newton guy," and she said, "Yeah, that was your father's therapist." Evidently Dad was an early patient of Saul's -- sort of a test case.

After I was born, Saul convinced my dad that now that he had a family, and families were evil, his family must be broken up. So, Dad left me and my mom and got an apartment on the Lower East Side. According to my mom, after a couple of weeks Dad started to miss us. He came running to try to reconcile with us. But Mom escaped with me down to Mexico, where she got the divorce, bought big, floppy hats, danced around with strangers, and got the half-dozen or so ceramic disks -- each one depicts a woman escaping from slavery.

So I'd sit there under the disks on the couch, sipping my double espresso, as my mom turned on the old radio. The morning disc jockey was Julius Lester -- he of the ouska-deep voice. Supposedly, Julius's program was a classical music show. But Julius would play about five minutes of an oboe concerto, and then speak for hours about his various ex-wives and their peccadilloes.

I'd listen to Julius and sip my double-espresso and then go running off to school-jazzed!

I was so excited my first day of kindergarten. After spending the first five years of my life exclusively in the company of my parents and their friends; for the first time, I was going to get to mingle with the masses. Boy, was I disappointed! That first day, I walked into my kindergarten classroom and saw all these little kids running around screaming, pulling hair, bopping each other, crying. I thought, How will I ever organize these people? (then he gets an idea) Remember . . . my father was a Communist. He believed I was going to lead a violent Communist revolution – so . . . (singing as a 5-year-old) * Arise, you prisoners of starvation! / Arise, you wretched of the earth! / For justice thunders condemnation. / A better world's in birth.
```

---

## IC-1406: The Redneck Night Before Christmas

- Title: The Redneck Night Before Christmas
- Author (byline): Ellen J. Sullivan
- Work: Not specified
- Publisher: Crane Hill Publishers
- Publication date as stated: Oct 1997
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 595
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ellen J. Sullivan
ISBN: 157587069X
Publisher: Crane Hill Publishers
Date (Month/Year): Oct 1997
```

### Introduction (context only: never use it for content warnings)

```text
“A Visit from St. Nicholas” also known as “The Night Before Christmas” was first published anonymously in 1823. It is largely responsible for the conception of Santa Claus – including his physical appearance, the night of his visit, his mode of transportation, the number and names of his reindeer and the tradition that he brings toys to children. Because of its notoriety, the poem has unfortunately . . . . or fortunately, spawned numerous parodies: From National Lampoon’s Christmas Vacation to Tim’ Burtons 1993 film The Nightmare Before Christmas, Santa has been twisted, untwisted and remade for a variety of audiences. Today’s entertainment continues the tradition of parody with The Redneck Night Before Christmas by Ellen J. Sullivan.
```

### Performance text (classify this)

```text
It was the night before Christmas, when all through the trailer park
Not a pop-top was poppin', not even Ole Blue barked.
Our stockin's was hung over the space heater with care,
In hopes Santy would fill 'em with Viennas and beer.

The kids was alseep in their NASCAR pj's,
Dreamin' of Goo Goo Clusters, Moon pies, and RC's.
And Earlene in her curlers and me in my John Deere cap
Had just settled into our La-Z-Boys for Wheel of Fourtune and a nap.

Then out in the vacent lot I heard such a commotion
I thought it was neighbor Clyde, finally got his T'bird in motion.
I heaved out of my recliner and to the window I flew,
Busted out the screen and hollered for Blue.

The moon was shinin' down on my old wrecked cars
So bright they was sparklin' like rusty old stars.
And I couldn't believe my own hardworking eyes
When a jacked up Ford pickup come flyin' through the sky!

Faster'n Ole Ironhead hs possums they came
And he whooped and hollered and called 'em by name
Git up Sooner! Hi Duke! Move yer tails Yaller and Spud!
On Blackie! On Queenie! You mind me Duchess and Bud!

To the top of the satellite dish! To the top of the shed!
Now move it! Step on it! Y'all get out the lead!
You know how, on our road, when a car goes by,
There's all this dirt flies up into the sky?

That's how this crew went straight on up to my roof
With that pickup full of toys, a real nice gun rack, and Redneck Santa too.
Then 'fore I could pop my teeth in I heard up on the tin
The scrabbling around of them Flying possums of his'n.

I yanked my head back in the trailer and hitched up my shorts...
Down the dryer vent Redneck Santa came with a grunt and a snort!
He was dressed in red-and-green camo from his neck to his feet
And I had to give him credit he still had most his teeth.

Looked like stuff from Earlene's yard sale slung on his back-
There was flyswatters an' Tupperware an' 8-tracks stickin' out of his pack.
His eye took in our humble home
The furniture we bought on layaway in town...

Earline's pride, that Elvis on velvet...
My collections of barbed wire... and license plates made by relatives.
I coulda' swore I even saw a glistening tear
When his eye fell on sweet Earlene, a snorin'in her chair.

He kindly favored Hank, Jr., with a big round belly
That shook when he laughed like a blob of K-Y jelly.
Yep, he was fat all right, blocked out our whole Large screen TV,
And I had to laugh when I saw him, 'cause he looked just like me!

When he winked his eye I knew fer sure he'd treat us right- Why, he might even leave me some ammo tonight!

I stood there dreamin' of whitetail while I watched him work, Then he stopped and, like a real man, let out a fart and a burp.

He topped off our stockin's with Moon Pies and bottle rockets,
Then squoze up that dryer vent like spam in your pocket.
He jumped in his pickup, laid down on the horn...I'm not lying'!
And they took off like white lightnin' with their possum tails flyin'.

But I heard him holler as headed for the 7-11.... "MERRY CHRISTMAS TO ALL, AND MAY ALL REDNECKS GO TO HEAVEN!"
```

---

## IC-1407: Removing the Glove

- Title: Removing the Glove
- Author (byline): Clarence Coo
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 1994
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: LOUIE, SUPPORT GROUP MEMBERS, WILL, NEWSCASTER’S VOICE, PROTESTER’S VOICE, DISAGREER’S VOICE, DAD, MOM, CINDY, JESSICA, MARK
- Teaser before the introduction: Yes
- Spoken words (computed): 1211
- Already set (do not supply): none

### Source block (context only)

```text
Author: Clarence Coo
ISBN: 978-0874406993
Publisher: Samuel French, Inc.
Date (Month/Year): 1994
```

### Introduction (context only: never use it for content warnings)

```text
Removing the Glove by Clarence Coo
```

### Performance text (classify this)

```text
(WILL walks to some empty chairs up Centerstage. He sits in one of them. The other chairs soon fill up with people of various ages and genders. A middle-aged man, LOUIE, stands in front of them. LIGHTS come up on the SUPPORT GROUP.)

LOUIE: Hi. I’m Louie and I’m left-handed!

SUPPORT GROUP MEMBERS: AND THAT’S OKAY!

LOUIE: So are there any new members today? (everyone looks at WILL who appears to be very intimidated.)

WILL: Uh… me. I’m Will.

SUPPORT GROUP MEMBERS: HI, WILL! YOU’RE OKAY!

WILL: I saw the ad for your support group in the paper and I thought I’d stop by for a meeting. (weakly) Okay… I’m left-handed.

LOUIE: What was that?

WILL: (stronger) I’m left-handed.

LOUIE: What was that?

WILL: (shouting) I’M LEFT-HANDED! (pause) You know, that’s the first time I’ve said those words aloud.

LOUIE: Congratulations, Will. You’ve taken your first step in being honest with yourself. The first step in being honest with the world. The first step in… (raises his left hand) Removing the Glove! (in an overly dramatic fashion, pantomimes removing a glove from his hand. Cheers follow)

WILL: (very intimidated) Removing the glove. Okay. So, what is that like?

LOUIE: Removing the glove is removing the lie that you have lived for other people. Removing the glove means doing what is truly natural for you. It means to be yourself. Because you, Will are okay.

WILL: But… but… then people will know.

LOUIE: That’s right, Will. People will know. Because you tell them. Not just in your actions, but in your words. It’s better for your friends and family to know from you before they find out for themselves. You HAVE to tell them.

WILL: I’m going to (raises his left hand) remove the glove! (removes an imaginary glove over dramatically) I’m going to start with my family at the dinner table. Then I’ll tell my friends at school. I’m committed to this. I just can’t live my life like this. I can’t hide anymore. I’m ready.

NEWSCASTER’S VOICE: Left-handed activists are staging another protest in front of the White House this afternoon. They demanded the passage of a new civil rights bill which would ban job discrimination based on hand dominance. We take you there now, live.

PROTESTER’S VOICE: (sound of protesters chanting is heard in the background) The fact that I am left-handed does not make me any less of a worker, or a person, than anyone else. I was born left-handed and I am proud. . .

DISAGREER’S VOICE: Left-handedness is a sick, depraved practice. That’s why it’s called LEFT-handedness -- because it is not RIGHT. God intended for us all to use our right hand. You, sir, are a pervert. (cheering from the bystanders; shouts of “pervert” and “lefty” are hurled at the protesters. Dad shuts off television and addresses the family)

DAD: I read in the paper today that they’re going to let left-handers in the military.

MOM: Oh, yes. The new “Don’t Ask, Don’t Tell” policy. It was the President’s decision.

CINDY: Well, why would the President be catering to the interests of those left-handers? (pause) Wait, you don’t think that the President . . .

DAD: Cindy, don’t be silly. If the President was left-handed, he would have never been elected to office.

CINDY: Have you heard about all those left-handed priests and left-handed Boy Scout leaders? The world just isn’t safe anymore. (remembering, then getting choked with excitement.) Oh, I can’t believe I forgot to tell you guys. George Bradshaw removed the glove about being ambidextrous at the game last night.

MOM: George Bradshaw . . . isn’t he the school’s biggest football star?

CINDY: Sure is. No one ever suspected HIM. I mean, George Bradshaw was a football player. He never seemed peculiar. It’s not like he was one of those Drama Lefties. . . He got kicked off the team.

DAD: I tell ya, kids, those left-handed people are everywhere these days. You’ve got to be real careful. Speaking of football, Will, why didn’t you try out for the team at school? You could have been the quarterback, like I was when I was your age. *******

(WILL address the audience; his family and two friends are listening intently)

WILL: Hey guys. Can I talk to you for a moment? I’ve been meaning to tell you something that’s been burning inside of me for a long time. I’ve tried to deny it myself––but I just can’t. I’ve faced the fact that it’s true and I hope that you can, too. I’m left-handed. I can still remember my first left-handed experience. I was doing my math homework one day, when my mind started to wander to other things. I looked at my pencil and thought, “What would it be like to put it in my left hand?” So, then I took my apprehensive fingers and wrapped it gently around that hard, wooden number 2. And I slid it across that piece of paper like there was no tomorrow. And it felt so good. So good. It was ecstasy! Sorry, but this thing I am -- left-handed -- it doesn’t change who I am. I hope you realize that. Because I’ve always been that way. And I guess I always will. Please try to understand? Please?

MOM: Jim, turn around right now. Jim, he’s our son.

DAD: Well, he can be YOUR son because MY son was right-handed.

CINDY: (on the phone) Yes, my own brother, first George Bradshaw; now my own brother. . .

DAD: My own son had possibilities of becoming a quarterback. Not with a left-hand. He’d be a laughingstock. He’d be a disgrace. They’d never let him into the locker room. I can just picture it now. It’s after a game and he’s in there showering with them. He reaches out to turn the hot water on and because he can’t control himself he . . . (disgusted.) turns the COLD water on!

CINDY: (still on the phone.) Yeah, I know . . . It’s like they’re coming out from everywhere these days . . . Yeah . . . I know. It’s like earthworms after a rainstorm . . .

DAD: I can’t believe this. Do you know what this means? This means I’ve failed as a parent.

WILL: Dad, please turn around

DAD: I won’t until you apologize for lying to us about being left-handed.

WILL: Dad, I’m not lying to you. I keep trying to tell you that.

DAD: So, if you’re not lying, why did you choose this lifestyle?

WILL: Dad, I didn’t choose it.

DAD: I’m disappointed in you, Will. Don’t you know how wrong this is? This is the most sinful and morally reprehensible thing you could do. Don’t you understand why left-handedness is wrong, Will? It’s completely unnatural! I don’t want to ever speak to you again. *********

WILL: Jessica, we need to talk.

JESSICA: I don’t have to talk to you. You’re left-handed now. Next thing you know, you’ll be cutting up paper with special scissors. Then you’ll join one of those leftist organizations and march down the streets of Washington, D.C. proclaiming your handedness in front of nationwide TV.

WILL: Jessica . . .

JESSICA: (walks off in a state of shock) Hey Ted, would you like to cut some paper with me? I have some very nice scissors! Ha ha ha. Ha ha ha.” (MARK enters) **********

WILL: Mark. I’m glad you’re here. Look, I’m really sorry if . . .

MARK: Oh, sorry huh? I know the trick you’re playing. Next, you’ll suggest we shake hands and make up. But, of course, you’ll want to shake with our LEFT hands. Wasn’t that the plan, eh? But I’m ahead of your game, you little deviant. What are you looking at? You’re looking at my left hand, aren’t you? You are! I saw you, so stop it. Stop looking! (hysterical, as he runs off) Aaaaaaaaaaaah! *********

WILL: I thought removing the glove would make me feel better. (walks over to the dinner table.)

DAD: You’re back! (gives WILL a big hug.)

WILL: Dad, you talked to me!

DAD: It’s going to be okay, Will. It’s going to be okay! Everything will turn out just fine. (removes a brochure from his pocket) Cindy gave this to me. There’s this nice psychiatrist in the city named Dr. Fussbaum. And this guy can really help you. He says that with two years of therapy and electroshock treatment, you’ll be as good as normal! Isn’t that great? Thank you, modern science! Thank you! (one more hug then WILL steps downstage and speaks to the support group)

WILL: You know, removing the glove has really taught me a lesson. So, I thought that I should tell you something that I’ve never told anyone before. Well . . . I’m a Pisces.
```

---

## IC-1408: Resusci-Annie

- Title: Resusci-Annie
- Author (byline): Paul Feig
- Work: Kick Me: Adventures in Adolescence
- Publisher: Three Rivers Press
- Publication date as stated: Sept 2002
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: PAUL, NORMAN, KORN, WENDELL, DOUG
- Teaser before the introduction: No
- Spoken words (computed): 1983
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul Feig
Book: Kick Me: Adventures in Adolescence
ISBN: 978-0609809433
Publisher: Three Rivers Press
Date (Month/Year): Sept 2002
```

### Introduction (context only: never use it for content warnings)

```text
Whether the latest Ebola or Zika virus news has triggered your inner germaphobe, or you’re just a year-round clean freak like me, you’ll be able to identify with this childhood memory of Paul Feig. Middle school . . . . those in between years are rough, but if you are a germaphobe, then it’s even worse, especially if gym class includes CPR training with Sergeant Korn, Coach Wendell and . . . Rescui-Annie by Paul Feig
```

### Performance text (classify this)

```text
PAUL: When I was a kid, I was germ conscious. Really germ conscious. You see, much of childhood is set up as one big germ- and spit-spreading activity. And it seemed as if all of my grade-school peers were more than willing to put their mouths on whatever it was that I or anyone else happened to be consuming at any given moment during the day. Whenever I had a bottle of pop, at any point from age four to fourteen, it was guaranteed that within seconds of opening it, some kid I knew would appear behind me and utter these dreaded words: "Hey, can I have a drink?" Every time. And then I was stuck. Because if I dared to say no, it was sure to provoke a thoughtful and understanding response of "C'mon, ya baby. I'm not gonna drink it all."

"Yeah, but you're gonna get your mouth all over it." Or at least, that's what I wanted to say. But instead, in my true non-confrontational fashion, I'd always relent: "Uh . . . okay. Here." I mean, what other option did I have? The circumstances were always the same. It would be a warm afternoon. I'd be walking home from grade school, tired and worn out from a full day of crushes and failures and overreactions. As I walked, I'd twist off the top. The bottle would give me a friendly hiss that seemed to say, "Oh, friend, are you going to enjoy me." I'd take a deep breath, releasing all the tensions of the day, raise the bottle to my lips, tilt my head back and take a drink, enjoying life to its fullest. The world seemed to melt away. And life for that one moment was good. That is, until the dream would be shattered when Norman would suddenly walk out of the bushes and want to backwash into my bottle.

So, I'd reluctantly give him my Squirt and he'd put his mouth on it and take a sloppy swig and I'd feel defiled as I'd watch him gulp down my once pleasure-producing soft drink. My thoughts would be torn between hoping he choked on the pop and figuring out how I could possibly salvage what was left in the bottle. Maybe I could pour out the top inch of spit-contaminated liquid, then thoroughly wipe down the mouth of the bottle with my shirttail to remove the memory of his mouth. . . . when suddenly the nightmare would worsen. Another kid would invariably walk up. "Hey, Norman, can I have a drink?"

NORMAN: "It's okay with me, but it's Paul's pop. Ask him."

PAUL: What was I gonna say? "No, I don't mind Norman's saliva but yours is a no-go." Why did all these kids have to drink out of the same bottle anyway? So Norman's friend would grab the bottle and take a drink and get his stupid mouth all over it and then a gang of Cub Scouts who were friends of the kid currently drinking would show up and take their turns and after an eternity I'd get the bottle back. The top would be coated with everything our grade school served for lunch that day and the few inches of liquid left at the bottom of the bottle would have about the same viscosity as old motor oil. I'd look at it and feel queasy and feel like crying but instead would try to sound casual and say, "You guys can have the rest. I'm not thirsty anymore."

NORMAN: "No way. I'm not drinking that. It's all backwash."

PAUL: Yeah, YOURS! . . . Well, it was a couple of years later, when I was in junior high school, that something happened during gym class that was to prove one of the most traumatic events of the spit-and-germ-avoiding segment of my childhood. Simply put, I met a girl. And that girl's name was . . . Resusci-- Annie.

"Annie," as I've affectionately come to know her, wasn't a girl in the standard person-who's-actually-alive sense. No, Annie was a mannequin, a life-size doll with a rubber head, a mouth, a working windpipe, a set of lungs, and a body that was in possession of neither arms nor legs. Resusci-Annie, Queen of the Latex Torso Women, was something invented by paramedics and CPR instructors to be used for the teaching of the uninitiated in the fine art of mouth-to-mouth resuscitation. Annie also had one other thing going for her . . . She was terrifying.

The first traumatic thing about Annie was that she looked like a dead person. Her face was white and rubbery, her eyes were closed, her mouth was loosely open, exposing a disturbing set of rubber teeth, and she had a full mane of greasy, matted hair on top of her head. She hardly looked like someone anybody had a chance of saving. I'd throw a blanket over her face and start contacting next of kin if I saw her lying in the street. But as far as the emergency health care community was concerned, Annie had one purpose in this world and that was to be revived over and over again by anyone and everyone trying to master the very practical skills of lifesaving.

Mr. Wendell told us to gather in the center of the gym as we came out of the locker room. As we walked over, we saw Resusci-Annie lying on the floor. Just then, a very large policeman with a big red drinker's face and a handlebar mustache entered the gym and walked up to us.

KORN: Hello, gentlemen. My name is Sergeant Korn. As part of an organized effort to teach people in our community about emergency medical procedures, I'm here today to demonstrate to you the proper way to administer the life-saving technique of mouth-to-mouth resuscitation.

PAUL: If learning mouth-to-mouth meant it would keep us from having to play flag football or floor hockey or having to embark on yet another pointless attempt to do enough sit-ups to try to qualify for the much-unwanted President's Physical Fitness Award, then I was all for it.

KORN: And now, with the help of my good friend Resusci-Annie here (gesturing grandly and chuckling) I'm going to show you the correct way to administer the 'Kiss of Life.'”

PAUL: And then, accompanied by an aria of grunts and groans, he awkwardly got down on his knees next to Annie. He stuck his fingers into her mouth, telling us that before we did anything, we were supposed to make sure that there were no "objects" blocking the victim's throat. Sergeant Korn pinched Annie's deathly white nose, put his hand under her neck to "open the throat," took a deep breath, put his mouth on top of Annie's, and blew. I immediately started to feel a bit nauseous. Maybe it was the image of an overweight cop on his hands and knees blowing into the mouth of an oversize doll and making his already uncomfortably red face even redder that made it feel more like I was watching a very low-quality porn film than a lifesaving demonstration. Unsettling images of Sergeant Korn's private life with Mrs. Korn started to flood into my head. Fortunately, before I was able to ruminate on these mental pictures for too long, Sergeant Korn looked up and

KORN: (breathlessly) Resusci-Annie . . . now has enough air . . . to start breathing on her own again."

PAUL: And then he struggled to stand up again. Hearing him pant and try to catch his breath, I had a momentary flash that Sergeant Korn might keel over and that one of us would then be expected to put our newfound Kiss of Life knowledge to the test. Well, I knew one thing for sure: that "one of us" wouldn't be me. Mr. Wendell stepped forward.

WENDELL: All right, you guys. Line up. You're all gonna take a turn.

PAUL: Huh? Excuse me? I'm sorry, I must not have heard you correctly. It sounded like you said that we were all going to take a turn giving mouth-to-mouth resuscitation to that doll that Sergeant Korn had just had his grown man's mouth all over. That couldn't be right. I looked over at Mr. Wendell and saw him produce a bottle of rubbing alcohol and a rag. He dumped some alcohol onto the rag and wiped Sergeant Korn's spit off of Annie's mouth. My stomach dropped into my Keds. A wave of panic overtook me. My eyes zoomed in on Annie's mouth. White and cold and open and now dripping with an indeterminate mixture of Sergeant Korn's spit and alcohol. My head started to spin.

My mind raced. This couldn't be happening. But it was. My fellow classmates were starting to line up in front of Annie. There had to be some way out of this. It just wasn't possible that I was going to have to put my mouth on that thing. Especially after other guys in my class were about to do it, too. Something had to be done. . . . "Mr. Wendell, I think it's against my religion to do stuff like this."

WENDELL: Feig, I don't care if you're the pope. You're doing this, so get in line.

PAUL: There was no way around it. I was eventually going to have to give Annie the Kiss of Life. I was really starting to feel sick. And this was before I realized that with all the air going in and out of Annie's chest, there was a whole reservoir of lung germs inside my future Resusci-girlfriend just waiting to infect my body. I was stuck, doomed, and now the last in line. More and more spit was being deposited on Annie by the second. And now I noticed that the kid directly in front of me was Doug Blaychek. He was a nice enough guy if you met him in the hallway, but he had extremely large and droopy lips that constantly seemed to be soaked with saliva. Doug turned and gave me a big, wet smile. My life started to flash in front of my eyes.

It was Doug's turn. He kneeled down and bent over Annie. He took a loud, deep breath. I saw his back rise and fall several times as he tried to revive the lifeless rubber doll on the floor. As he moved away, I looked down. There she was. Annie. Her face was soaked. I didn't know what part of that "soaked" was spit and what part was alcohol, and I didn't care. Annie's face must now be a festering cesspool of disease and death.

WENDELL: All right, Feig. You're up." . . .

PAUL: Maybe if I throw up all over it, I won't have to do it, I thought. . . .

WENDELL: C'mon, Feig. What is it with you? Get moving!

PAUL: My mind reeled. I had to do something and I had to do it immediately. But what? Think fast, I told myself. Then it hit me. Faint. I coughed violently and fell over. There was immediate commotion. I hadn't been sure if they would buy my sudden and convenient fainting spell or not, but I guess that the perception of me as someone who was prissy enough to faint at the thought of giving mouth-to-mouth resuscitation was enough to convince them.

DOUG: I'LL SAVE HIM!

PAUL: It was Doug! New panic set in as I heard him stomp toward me to deliver his newly learned Kiss of Life. I was nanoseconds away from blowing my cover by screaming and running away when Mr. Wendell saved me by quickly grabbing Doug by the arm.

WENDELL: No, Blaychek, we don't know if he needs mouth-to-mouth.

NORMAN: He coughed really loud before he fell down.

KORN: (Stepping forward and looking over Paul’s prone body) You said he coughed? (Tense and official) Then he must have choked. Everybody step back.

PAUL: And with that, Sergeant Korn stuck his fingers in my mouth, pinched my nose, and kissed me. . . . I was home sick for three days.
```

---

## IC-1409: Rumpelstiltskin, Private Eye

- Title: Rumpelstiltskin, Private Eye
- Author (byline): Jason Sanford
- Work: Newfangled Fairy Tales, Book #2
- Publisher: Meadowbrook Press
- Publication date as stated: 2000
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: RUMPELSTILTSKIN, MILLER, HAPPY, CAPTAIN, MILLER’S DAUGHTER, KING
- Teaser before the introduction: Yes
- Spoken words (computed): 2425
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jason Sanford
Book: Newfangled Fairy Tales, Book #2
ISBN: 978-0881663174
Publisher: Meadowbrook Press
Date (Month/Year): 2000
```

### Introduction (context only: never use it for content warnings)

```text
Rumpelstiltskin, Private Eye by Jason Sanford
```

### Performance text (classify this)

```text
RUMPELSTILTSKIN: The name on my door says it all-"Rumpelstiltskin, Private Eye." I'm the one people turn to when they're in a jam. That crazy wolf who blew down those pigs' houses? I caught him. When Jack stole the giant's golden-egg-laying hen, I tracked him down. 'Course, things don't always go so smoothly. Take my last case. What started out as a good mystery almost ended with me in the dungeon…all because of the captain of the guards, a miller's daughter, and a whole lot of straw.

It began on a rainy Friday afternoon. I was watching an old Sherlock Holmes movie on TV when the miller walked in the door. I recognized him right away; he and his daughter had been in the news a lot lately. Rumor had it she'd been spinning straw into gold for the king, but I didn't believe that for a minute.

MILLER: I'm looking for a private eye.

RUMPELSTILTSKIN: That's me. Have a seat. (to audience) I poured the miller a glass of soda pop. He was a scraggly looking man, clothes patched and double patched. He needed a haircut worse than Rapunzel.

MILLER: It's my daughter. She's been kidnapped by the king.

RUMPELSTILTSKIN: (to audience) I whistled. The king was a little greedy-he said he'd marry anyone who could increase his stash of golden cash. Still, he was a nice guy and I had trouble believing that he would kidnap anyone. (To Miller) Can your daughter really spin straw into gold?

MILLER: Of course not. What fairy tale do you think this is?

RUMPELSTILTSKIN: Then why would the king kidnap her?

MILLER: Well… I was bowling with the captain of the palace guard, and I happened to mention how intelligent my daughter is, how beautiful she is, how… How she can spin straw into gold. Next day she was gone.

RUMPELSTILTSKIN: (to audience) I groaned. There's no telling how many kids have gotten into trouble because their parents brag a little too much.

MILLER: I guess the captain told the king what I said. Can you get my daughter out of the castle?

RUMPELSTILTSKIN: (to audience) I thought about it. I'd had a run-in with the captain of the guard before-caught him taking a bribe from Puss in Boots. It didn't surprise me that he was mixed up in this. But why would the king keep the miller's daughter in the castle if she couldn't spin straw into gold? Surely he'd have discovered that little fact by now.

I told the miller I'd take the case. I loved a good mystery, and this one was a puzzler. I shook hands with the miller, then ran to the castle. It was still raining, but I figured, hey, this'll save me the trouble of bathing tonight.

I stopped at the guard house by the drawbridge. My friend Happy was on duty. He and I had been the first really short people to make it through the Guard Academy. After I quit to become a private eye, Happy'd stayed on and became lieutenant. He said being a castle guard paid better than working for Snow White, and it was easier than being self-employed like me.

HAPPY: What's up, Rump?

RUMPELSTILTSKIN: I need to see the king. Got a case that involves him.

HAPPY: No can do, bud. The captain of the guard said no one gets in today, and I'm doing just what he says. The captain's got a major case of hay fever and is in a nasty mood.

RUMPELSTILTSKIN: Now why would hay fever be bothering him in the castle?

HAPPY: The captain found someone to spin straw into gold for the king. His Highness was so excited he ordered us to bring him every bit of straw in the kingdom. One of the three pigs came by today and yelled at me because we even took down his straw house.

RUMPELSTILTSKIN: Can the miller's daughter really spin straw into gold?

HAPPY: Seen it myself-straw goes in the main storeroom at night, gold comes out the next day. The king's making a bundle.

RUMPELSTILTSKIN: I was just about to ask Happy to let me in the castle to snoop around when the captain of the guard appeared.

CAPTAIN: What is he doing here?

RUMPELSTILTSKIN: I'm looking for the miller's daughter. Have you seen her? (To audience) The captain glared at me. As he leaned close to me, I caught a whiff of him. Phew! His uniform was filthy, and he smelled like rotten fish.

CAPTAIN: I don't talk to little creeps like you, Bumplestiltskin.

RUMPELSTILTSKIN: Rumpelstiltskin. The name's Rumpelstiltskin. (to audience) The captain had never been able to remember my name.

CAPTAIN: Whatever. Happy, follow your orders. No visitors.

RUMPELSTILTSKIN: (To audience) He walked back into the castle. Happy sighed. He didn't like the captain either. (To Happy) Where's the miller's daughter?

HAPPY: (whispering) She's in the storeroom, but you'd better stay away. You get anywhere near her and the captain will be after you like the Big Bad Wolf.

RUMPELSTILTSKIN: I thanked Happy, then walked away. Things just didn't make sense. No one could spin straw into gold, but it sure sounded as if that were happening. I had to get in the castle to see for myself-but how? The castle walls were forty feet tall, and the rain made them as slick as ice. I looked down at the moat and saw water shooting out of a drainpipe. Bingo, I thought. Every room in the castle had a large drain on the floor to let water out.

Later that night, after the rain had stopped, I swam across the moat and squirmed like a worm through the drainpipe. Talk about disgusting-mushy garbage and rats everywhere. I even got a bath in some old fish stew that someone had dumped down the drain. Soon the drainpipe widened into a sewer. It was so dark in there. I had to feel my way along the sewer wall. Suddenly I stumbled over some heavy bags of trash. One of the bags slumped onto me as I went sprawling in the muck. I wiggled out from under it and kept groping along. Eventually I found the pipe leading to the storeroom. As I eased up the room's drain cover, it clanked softly on the stone floor.

MILLER’S DAUGHTER: Who's there?

RUMPELSTILTSKIN: (To audience) I looked around and saw a young woman sitting by a spinning wheel in one corner of the room. (To Miller’s Daughter) My name's Rumpelstiltskin. I'm a private eye. Your father sent me to help you.

MILLER’S DAUGHTER: Great. I thought I'd be stuck in here until not-so-happily ever after.

(Suddenly wrinkles her nose.) Phew!

RUMPELSTILTSKIN: Yeah, well. Real-life rescues tend to be messier than in fairy tales. (To audience) I crawled out of the drain and stood up. (To Miller’s Daughter) The cleanest escape would be out the window. (to audience) Then it hit me: the miller's daughter had supposedly been spinning straw into gold all night, but there was no gold-and only a little straw-in the room. (to Miller’s Daughter) Aren't we missing something here? Where's all the straw and gold?

MILLER’S DAUGHTER: Oh, the captain's already stashed the straw. As for the gold… well, I suppose you'll be taking the blame for that.

RUMPELSTILTSKIN: Blame for what? I thought. Suddenly an alarm went off in my head. I'd been set up! I tried to run, but the woman grabbed me. She a full two feet taller than me and held me in a half nelson.

MILLER’S DAUGHTER: I've got the thief! Guards! Guards!

RUMPELSTILTSKIN: No! I'm here to help you.

MILLER’S DAUGHTER: I don't need your help. I'm going to be queen.

RUMPELSTILTSKIN: I couldn't believe my ears. Before I could say anything, the storeroom door opened, and in walked the captain and a couple of guards.

CAPTAIN: Looks like we've caught the thief.

RUMPELSTILTSKIN: I'm not a thief.

CAPTAIN: You made it easy, Bumpeltallskin.

RUMPELSTILTSKIN: Rumpelstiltskin. The name's Rumpelstiltskin.

CAPTAIN: Whatever. (He pulled out a handkerchief and sneezed) Anyway, I knew you couldn't ignore a good mystery.

RUMPELSTILTSKIN: What's going on? Tricking the king into believing the miller's daughter can spin straw into gold isn't going to do anything for you.

CAPTAIN: (Laughing) We'll see. Arrest him.

RUMPELSTILTSKIN: (To audience) Gee, I thought, the Wicked Witch hasn't got anything on this guy. Still, you don't get to be a P.I. if you can't improvise. I pushed my shoe under some straw and kicked it up into the captain's face. He exploded into a fit of coughs and sneezes as the other guards tried to help him. Gotta love hay fever. I said to the miller's daughter as I stomped on her foot. She screamed and let me go. I lunged for the window.

CAPTAIN: Get him!

RUMPELSTILTSKIN: But I was already jumping. It was forty feet down-right into the moat. Looks like I was finally getting my bath. I pulled myself out of the water and ran for my life. The next morning I was on the lam. I hid in an apple tree on Old McDonald's farm, listening to my Walkman. The radio was full of news about me stealing twenty bags of gold from the king's treasury.

I groaned. It was a good scam. The captain was stealing gold from the treasury to convince the king that the miller's daughter could spin straw into gold. With me accused of robbing the treasury, it would be hard to prove that no new gold had been added to it. Instead, the miller's daughter would marry the king, the captain would gain a fortune in stolen gold, and I'd be on my way to the dungeon.

I wanted to scream. I couldn't let the captain get away with this, but what could I do? It would only be a matter of time until the guards found me.

Suddenly it hit me. Actually, it bit me. A horse thrust its head into my apple tree to nibble an apple and got me instead. I fell out of the apple tree and landed hard on my butt. As I rubbed my bruised leg, I felt something in my pocket that hadn't been there the day before. I pulled it out: a gold coin. How had that gotten in there?

Then I smiled. All at once, I knew how to expose the captain as a thief, stop the king from marrying a con artist, and clear my name. The radio said the king's wedding would be that Saturday in the castle. The entire kingdom was invited, and I figured it wouldn't be too hard to sneak in. Nobody would expect that I'd be dumb enough to return to the scene of the crime.

On the wedding day, I hid until the miller and his daughter were marching down the aisle. Then, with a yell I jumped up on the pipe organ. That wedding went quiet faster than Little Bo Peep lost her sheep. The king and his bride were horrified. The captain of the guard ran toward me.

CAPTAIN: You're under arrest, Wrinklesoftskin!

RUMPELSTILTSKIN: Rumpelstiltskin! The name's Rumpelstiltskin!

CAPTAIN: Whatever.

RUMPELSTILTSKIN: (to Audience) Behind him, the wedding guests whispered excitedly. Well, I'd give them even more to whisper about. (to the King) I have come to throw myself on the mercy of Your Majesty. And to restore the stolen gold. (to audience) As you can imagine, that got the greedy king's attention. He signaled for silence, then looked at me.

KING: Very well. Please tell me where my gold is.

RUMPELSTILTSKIN: (To King) I'll do better than that; I'll show you. (To Audience) The captain of the guard started to protest, but the king hushed him. He wanted his gold back. Figuring that he still had the best of me, the captain gave in. Happy came up to tie my hands.

HAPPY: I can't believe you did it.

RUMPELSTILTSKIN: (To Happy) Wait and see. I might surprise you yet. (To Audience) Happy finished tying my hands, then dragged me before the king.

KING: Now, lead us to the gold.

RUMPELSTILTSKIN: I started walking toward the throne room.

KING: Where are you going?

RUMPELSTILTSKIN: (To King) The gold's in the castle. (To Audience) The captain of the guard and the miller's daughter exchanged worried looks, but the king didn't notice. He really wanted his gold back. So I took off, with the king, Happy, the miller and his daughter, and the captain trooping along behind me. I kept close to the captain. We walked through the throne room, past the treasury, down into the kitchen. The captain was starting to get restless.

CAPTAIN: You are trying my patience, Stumblestiltskin.

RUMPELSTILTSKIN: The name's… oh, never mind. The gold is nearby; I just forgot which room. (To audience) We descended a stairway and walked down a long hall. This was taking longer than I'd thought it would. I was just getting nervous when the captain pulled out a handkerchief, took a deep breath, and sneezed. The gold's in there I said, pointing to the nearest door. It led to the dungeon.

CAPTAIN: Preposterous. (sneezing)

KING: Open the door.

RUMPELSTILTSKIN: Happy marched forward and swung the door wide open. We crowded in to stare at… straw. There were piles and piles of straw. At first no one understood.

KING: Where's the gold?

HAPPY: The captain said all the straw in the kingdom had been turned into gold. If that's true, what's this straw doing here?

CAPTAIN: *Sneeze, Sneeze, Sneeze*

RUMPELSTILTSKIN: The miller's daughter didn't spin any straw into gold. The captain swapped the straw for gold from the treasury, then blamed his theft on me. The two were working in cahoots to rob you, Your Majesty.

KING: Then where is my gold?

RUMPELSTILTSKIN: Hidden in the sewer under the castle. I said. Then I pulled out the gold coin I'd found in my pocket. I tripped over the bags climbing up here to "rescue" the miller's daughter, and this slid into my pocket. Then I remembered how the captain smelled like rotten fish the other day-just like I did after crawling through the sewer. I figure he was hiding the gold there until the coast was clear. The king frowned at the captain and the miller's daughter.

MILLER’S DAUGHTER: It wasn't my fault. My father and the captain made me do it.

RUMPELSTILTSKIN: Well that did it. The miller, his daughter, and the captain began yelling and arguing like you wouldn't believe. There was no honor among these thieves. The king ordered Happy to throw them all in the dungeon. Happy and I then crawled into the sewer and retrieved all the stolen gold. The next day I came to the castle. (To Happy) Congrats on the promotion. (To Audience) He'd been bumped up to captained, what with the former captain doing time.

HAPPY: Thanks. Glad to know that you're not a thief.

RUMPELSTILTSKIN: How's the king doing, now that he knows his gold-spinning bride was a fake?

HAPPY: Actually, he's feeling great. He just heard about this guy named Midas, who has the golden touch. The king thinks he'll be rolling in gold before the week is out.

RUMPELSTILTSKIN: I groaned. It looked as if the king would be keeping me busy for the next few happily ever afters-very busy. And that's nothing to sneeze at.
```

---

## IC-1410: SantaLand Diaries

- Title: SantaLand Diaries
- Author (byline): David Sedaris
- Work: Holidays on Ice, Pgs 1-44
- Publisher: Back Bay Books
- Publication date as stated: Nov 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: DAVID, OFFICIAL VOICE, MAN, SANTA SANTA, RILEY, WOMAN, MAN 1, WOMAN 1
- Teaser before the introduction: Yes
- Spoken words (computed): 1396
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Sedaris
Book: Holidays on Ice, Pgs 1-44
ISBN: 978-0316779234
Publisher: Back Bay Books
Date (Month/Year): Nov 1998
```

### Introduction (context only: never use it for content warnings)

```text
PERKS TO BEING AN ELF: You can walk home with all the leftover toys come December 25th . . . a never-ending supply of cookies, milk, hot chocolate and other tasty holiday treats. THE DOWN SIDE: Elves are required to wait on Santa and Mrs. Claus hand and foot . . . Mall Duty: they receive the brunt of screaming kids, stray kicks to the shins and sticky candy cane hands in their hair. So even though Will Ferrell made being an ELF seem like the next best thing to Christmas . . . the reality of being a mall elf is, well . . . my therapist suggested that I should keep

SantaLand Diaries by David Sedaris
```

### Performance text (classify this)

```text
DAVID: (Pgs 1-44) I was in a coffee shop looking through the want ads when I read:

OFFICIAL VOICE: Macy's Herald Square, the largest store in the world, has big opportunities for outgoing, fun-loving people of all shapes and sizes who want more than just a holiday job! Working as an elf in Macy's SantaLand means being at the center of the excitement!

DAVID: This morning we were lectured by the Santa-Land managers and presented with a Xeroxed booklet of regulations titled "The Elfin Guide." In the afternoon we were given a tour of SantaLand, which really is something. It's beautiful, a real wonderland, with ten thousand sparkling lights, false snow, train sets, bridges, decorated trees, mechanical penguins and bears, and really tall candy canes.

We traveled the path a second time and were given the code names for various posts, such as "The Vomit Corner," a mirrored wall near the Magic Tree, where nauseous children tend to surrender the contents of their stomachs. When someone vomits, the nearest elf is supposed to yell "VAMOOSE," which is the name of the janitorial product used by the store. We were taken to the "Oh, My God, Corner," a position near the escalator. People arriving see the long line and say "Oh, my God!" and it is an elf's job to calm them down and explain that it will take no longer than an hour to see Santa.

We were given a demonstration of the various positions in action, performed by returning elves who were so animated and relentlessly cheerful that it embarrassed me to walk past them. I don't know that I could look someone in the eye and exclaim, "Oh, my goodness, I think I see Santa!" or "Can you close your eyes and make a very special Christmas wish!" Everything these elves said had an exclamation point at the end of it!!! I am afraid I won't be able to provide the grinding enthusiasm Santa is asking for. I'll be a low-key sort of an elf.

My costume is green. I wear green velvet knickers, a yellow turtleneck, a forest-green velvet smock, and a perky stocking cap decorated with spangles. My elf name is Crumpet. We were allowed to choose our own names and given permission to change them according to our outlook on the snowy world.

Today was the official opening day of SantaLand and I worked as a Magic Window Elf. The Magic Window is located in the adult "Quick Peep" line. My job was to say, "Step on the Magic Star and look through the window, and you can see Santa!" I was at the Magic Window for 15 minutes before a man approached me

MAN: You look so stupid.

DAVID: He had a point. But, at least I get paid to look stupid; he gives it away for free. But I can't say things like that because I'm supposed to be merry. So instead I said, "Thank you!" as if I had misunderstood and thought he said, "You look terrific." (to man) Thank you!

[One day] I was stuck being Photo Elf with Santa Santa. I don't know his real name; no one does. During most days, there is a slow period when you sit around the house and talk to your Santa. Most of them are nice guys and we sit around and laugh, but Santa Santa takes himself a bit too seriously. I asked him where he lives, Brooklyn or Manhattan.

SANTA SANTA: Why, I live at the North Pole with Mrs. Claus! (Santa laugh)

DAVID: I asked what he does the rest of the year . . .

SANTA SANTA: (Santa laugh) I make toys for all of the children.

DAVID: (to Santa) Yes, but what do you do for money?

SANTA SANTA: Santa doesn't need money. (Santa laugh)

DAVID: Santa Santa sits and waves and jingles his bell sash when no one is there. He actually recited "The Night Before Christmas," and it was just the two of us in the house, no children. Just us. What do you do with a nut like that?

SANTA SANTA: Oh, Little Elf, Little Elf, straighten up those mantel toys for Santa.

DAVID: I reminded him that I have a name, Crumpet, and then I straightened up the stuffed animals. (beat) Santa Santa has an elaborate little act for the children. He'll talk to them and give a hearty chuckle and ring his bells and then he asks them to name their favorite Christmas carol. Most of them say "Rudolph, the Red-Nosed Reindeer." Santa Santa then asks if they will sing it for him. The children are shy and don't want to sing out loud, so Santa Santa says

SANTA SANTA: Oh, Little Elf, Little Elf! Help young Brenda to sing that favorite carol of hers.

DAVID: Then I have to stand there and (sings enthusiastically) Rudolph, the Red-Nosed Reindeer. . (drops elf façade) which I hate. Half the time young Brenda's parents are my age and that certainly doesn't help!

[Another day] I worked as an Exit Elf, telling people (in a loud voice) THIS WAY OUT OF SANTALAND. A woman was standing at one of the cash registers paying for her idea of a picture, while her son lay beneath her having a tantrum.

RILEY: (pitches a tremendous fit)

WOMAN: Riley, if you don't start behaving yourself, Santa's not going to bring you any of those toys you asked for.

RILEY: He is too going to bring me toys, liar, he already told me!

WOMAN: (grabbing David’s arm) You there, Elf, tell Riley here that if he doesn't start behaving immediately, then Santa's going to change his mind and bring him coal for Christmas.

DAVID: (to audience) I told her Santa no longer traffics in coal. Instead, if you're bad he comes to your house and steals things If he didn't behave himself, Santa was going to take away his TV and all his electrical appliances and leave him in the dark. (to Riley) All your appliances, including the refrigerator!

RILEY: (pitches a tremendous fit)

DAVID: Your food is going to spoil and smell bad!

RILEY: (continues his fit)

DAVID: It's going to be so cold and dark where you are. Man, Riley, are you ever going to suffer! You're going to wish you never heard the name Santa!

RILEY: (gasps for air, processes the new information and abruptly stops his fit)

DAVID: Lately I am feeling trollish and have changed my elf name from Crumpet to Blisters. Blisters — I think it's cute.

I was the Pointer Elf this afternoon, one of my favorite jobs. The Pointer stands inside the Magic Tree and appoints available Santa Elves to lead parties of visitors to the houses. First-time visitors are enthusiastic, eager that they are moments away from Santa. Some of the others, having been here before, have decided to leave nothing to chance.

Out of all the Santas, two are black and both are so light-skinned that, with the beard and makeup, you would be hard-pressed to determine their race. Last week, a Black woman became upset when, having requested a "Santa of Color," she was sent to Jerome. I've had requests from both sides -- White Santa, Black Santa. A Pointer Elf is instructed to . . . (shrugs shoulders, feigning ignorance) There's only one Santa.

After she was led to the house, the woman demanded to speak with a manager.

WOMAN: (complaining) He's not black!

DAVID: Bridget assured this woman that Jerome was indeed black.

WOMAN: Well, he isn't black enough!

DAVID: We were packed today, absolutely packed, and everyone was cranky. Once the line gets long, we break it up into four different lines because anyone in their right mind would leave if they knew it would take over 2 hours to see Santa. 2 hours — you could see a movie in 2 hours. Standing in a 2-hour line makes people worry that they're not living in a democratic nation. People stand in line for 2 hours and they go over the edge. I was sent into the hallway to direct the second phase of the line. The hallway was packed with people, and all of them seemed to stop me with a question.

MAN 1: Which way to the down escalator,

WOMAN 1: Which way to the elevator (rapidly changing voices and personas) the Patio Restaurant, gift wrap, the women's rest room, Trim-A-Tree.

DAVID: There was a line for Santa and a line for the women's bathroom, and one woman, after asking me a dozen questions already, asked

WOMAN: Which is the line for the women's bathroom?

DAVID: (shouting) The line with all the women in it!

WOMAN: I'm going to have you fired!

DAVID: I had two people say that to me today

MAN: I'm going to have you fired!

DAVID: Go ahead, be my guest. I'm wearing a green velvet costume; it doesn't get any worse than this. Who do these people think they are? (sings the first verse) You’d better watch out . . .
```

---

## IC-1411: The Secret Life of Walter Mitty

- Title: The Secret Life of Walter Mitty
- Author (byline): James Thurber
- Work: Not specified
- Publisher: Creative Education
- Publication date as stated: Nov 1983
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: COMMANDER, NARRATOR, LTN BERG, MRS. MITTY, WALTER, MITTY, NURSE, DR. RENSHAW, DR. P-M, INTERN, WALKER, PARKING LOT ATTENDANT, DISTRICT ATTORNEY, MITTY’S ATTORNEY, PASSING WOMAN, CLERK, SERGEANT, CAPTAIN MITTY
- Teaser before the introduction: Yes
- Spoken words (computed): 1363
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Thurber
ISBN: 978-0871919618
Publisher: Creative Education
Date (Month/Year): Nov 1983
```

### Introduction (context only: never use it for content warnings)

```text
Ever wish you could escape the crushing responsibility of remembering grocery lists, making small talk, or figuring out why you walked into a room… and instead enter a world where you are always the main character?

A world where every decision is bold, every line is dramatic, and no one ever asks, “Did you remember the puppy biscuits?” (harumph) Obviously, you’re too busy saving lives, winning battles, and looking incredibly cool while doing it.

For octogenarian Walter Mitty reality is optional, heroism is guaranteed, and the only real danger is getting snapped back to the boring real world at the worst possible moments.

The Secret Life of Walter Mitty by James Thurber
```

### Performance text (classify this)

```text
DAYDREAM #1

(Somewhere in a Navy hydroplane in a winter storm)

COMMANDER: We're going through!

NARRATOR: The Commander's voice was like thin ice breaking. He wore his full-dress uniform, with the heavily braided white cap pulled down rakishly over one cold gray eye.

LTN BERG: We can't make it, sir. It's spoiling for a hurricane, if you ask me.

COMMANDER: I'm not asking you, Lieutenant Berg. Throw on the power lights! Rev her up to 8500! We're going through!

NARRATOR: The pounding of the cylinders increased (ta-pocketa-pocketa-pocketa-pocketa-pocketa)

COMMANDER: (twisting a row of dials, shouting) Switch on No. 8 auxiliary! Full strength in No. 3 turret!

LTN BERG: No. 8 auxiliary! Full strength in No. 3 turret! The Old Man'll get us through. The Old Man ain't afraid of hell!

NARRATOR: The pounding of the cylinders increased (ta-pocketa-pocketa-pocketa-pocketa-pocketa. Walter is immersed in his daydream)

REALITY

MRS. MITTY: Not so fast! You're driving too fast! What are you driving so fast for?

WALTER: Hmm?

NARRATOR: He looked at his wife, in the seat beside him, with shocked astonishment. She seemed grossly unfamiliar, like a strange woman who had yelled at him in a crowd. MRS.

MITTY: You were up to 55. You know I don't like to go more than 40. You were up to 55.

NARRATOR: Walter Mitty drove on in silence, the roaring of the SN202 through the worst storm in 20 years of Navy flying fading in the airways of his mind.

MRS. MITTY: You're tensed up again. It's one of your days. I wish you'd let Dr. Renshaw look you over.

NARRATOR: Walter Mitty stopped the car in front of the building where his wife went to have her hair done.

MRS. MITTY: Remember to get those overshoes while I'm having my hair done.

WALTER: I don't need overshoes.

MRS. MITTY: (arranging things in her handbag) We've been all through that. (getting out of the car) You're not a young man any longer.

WALTER: (races the engine a little - ta-pocketa-pocketa-pocketa-pocketa-pocketa)

MRS. MITTY: Why don't you wear your gloves? Have you lost your gloves? (Walter reaches in a pocket; brings out the gloves and puts them on)

NARRATOR: But after she had turned and gone into the building and he had driven on to a red light, he took them off again. He drove around the streets aimlessly for a time, and then he drove past the hospital. DAYDREAM #2

NURSE: It's the millionaire banker, Wellington McMillan.

WALTER: (removing his gloves slowly) Yes? Who has the case?

NURSE: Dr. Renshaw and Dr. Benbow, but there are two specialists here, Dr. Remington from New York and Dr. Pritchard-Mitford from London. He flew over.

DR. RENSHAW: (entering, looking distraught and haggard) Hello, Mitty. We're having the devil's own time with McMillan, the millionaire banker and close personal friend of Roosevelt. Obstreosis of the ductal tract. Wish you'd take a look at him.

NARRATOR: In the operating room there were whispered introductions.

DR. RENSHAW: Dr. Remington, Dr. Mitty. Dr. Pritchard-Mitford, Dr. Mitty.

DR. P-M: (shaking Walter’s hand) I've read your book on streptothricosis. A brilliant performance, sir.

NARRATOR: A huge, complicated machine, connected to the operating table began at this moment to go (pocketa-pocketa-queep-pocketa-queep)

INTERN: The new anesthetizer is giving away! There is no one in the East who knows how to fix it!

WALKER: (in a low cool voice) Quiet, man! (moving dials on the machine) Give me a fountain pen! (he pulls a faulty piston from the machine and inserts the pen) That will hold for 10 minutes. Get on with the operation.

NARRATOR: A nurse hurried over and whispered to Renshaw, and Mitty saw the man turn pale.

DR. RENSHAW: (nervously) Coreopsis has set in. If you would take over, Mitty?

NARRATOR: Mitty looked at him and at the uncertain faces of the two great specialists.

WALTER: If you wish. (he dons a surgical gown, adjust a mask and pulls on thin latex gloves) REALITY

PARKING LOT ATTENDANT: Back it up, Mac!! Look out for that Buick! (Walter jams on the breaks in a panic) Wrong lane, Mac.

WALTER: Gee. Yeh.

NARRATOR: He began cautiously to back out of the lane marked "Exit Only."

PARKING LOT ATTENDANT: Leave her sit there. I'll put her away. (Walter gets out of the car) Hey, better leave the key.

WALTER: Oh . . . (handing the man the ignition key)

NARRATOR: The attendant vaulted into the car, backed it up with insolent skill, and put it where it belonged.

WALTER: (he walks away muttering) They're so damn cocky, They think they know everything.

NARRATOR: Once he had tried to take his chains off, outside New Milford, and he had got them wound around the axles. A man had had to come out in a wrecking car and unwind them, a young, grinning garage man. Since then Mrs. Mitty always made him drive to a garage to have the chains taken off.

WALTER: The next time, I'll wear my right arm in a sling; they won't grin at me then. I'll have my right arm in a sling and they'll see I couldn't possibly take the chains off myself. (kicks at something on the sidewalk as he remembers his task) Overshoes.

NARRATOR: When he came out into the street again, with the overshoes in a box under his arm, Walter Mitty began to wonder what the other thing was his wife had told him to get. She had told him twice before they set out from their house. In a way he hated these weekly trips to town--he was always getting something wrong.

WALTER: Kleenex? No. Razor blades? No. Tooth paste?

NARRATOR: He gave it up. But she would remember it.

WALTER: (mimicking Mrs. Mitty) Where's the what's-its- name.

NARRATOR: A newsboy went by shouting something about the Waterbury trial. DAYDREAM #3

DISTRICT ATTORNEY: (holding out an automatic gun to the person on the witness stand) Perhaps this will refresh your memory. Have you ever seen this before?

WALTER: (takes the gun and examines it expertly, then calmly) This is my Webley-Vickers 50.80.

NARRATOR: An excited buzz ran around the courtroom. The Judge rapped for order.

DISTRICT ATTORNEY: You are a crack shot with any sort of firearms, I believe?

MITTY’S ATTORNEY: Objection! We have shown that the defendant could not have fired the shot. We have shown that he wore his right arm in a sling on the night of the 14th of July.

WALTER: (raises his hand and the bickering attorneys are stilled) With any known make of gun, I could have killed Gregory Fitzhurst at three hundred feet with my left hand.

NARRATOR: Pandemonium broke loose in the courtroom. A woman's scream rose above the bedlam and suddenly a lovely, dark-haired girl was in Walter Mitty's arms. The District Attorney struck at her savagely.

WALTER: (lets the DA have it on the point of his chin) You miserable cur! (the word “cur” brings him back to reality) REALITY

WALTER: Puppy biscuit. . .

PASSING WOMAN: (laughs) He said “Puppy biscuit.” That man said “Puppy biscuit” to himself.

NARRATOR: Walter Mitty hurried on. He went into an A&P.

WALTER: I want some biscuit for small, young dogs.

CLERK: Any special brand, sir?

NARRATOR: The greatest pistol shot in the world thought a moment . . .

WALTER: It says 'Puppies Bark for It' on the box. (looks at his watch)

NARRATOR: His wife would be through at the hairdresser's in fifteen minutes. She didn't like to get to the hotel first, she would want him to be there waiting for her as usual. He found a big leather chair in the lobby, facing a window, and he put the overshoes and the puppy biscuit on the floor beside it. He picked up an old copy of Liberty and sank down into the chair.

WALTER: (reading a headline) Can Germany Conquer the World Through the Air? DAYDREAM #4

SERGEANT: The cannonading has got the wind up in young Raleigh, sir.

CAPTAIN MITTY: (wearily) Get him to bed with the others. I'll fly alone.

SERGEANT: (anxiously) But you can't, sir. It takes two men to handle that bomber and the Archies are pounding the hell out of the air. Von Richtman's circus is between here and Saulier.

WALTER: Somebody's got to get that ammunition dump. I'm going over. (pours a drink) Spot of brandy?

NARRATOR: War thundered and whined around the dugout and battered at the door. There was a rending of wood and splinters flew through the room.

WALTER: (barely flinching) A bit of a near thing.

SERGEANT: The box barrage is closing in!

WALTER: (with a faint fleeting smile) We only live once, Sergeant . . . Or do we? (pours another shot and throws it back)

SERGEANT: I’ve never seen a man could hold his brandy like you, sir. (Mitty straps on his huge Webley-Vickers automatic) Begging your pardon, sir. It's 40 kilometers through hell, sir.

WALTER: (finishes one last brandy, speak softly) After all, what isn't?

NARRATOR: The pounding of the cannon increased; there was the rat-tat-tatting of machine guns, and from somewhere came the menacing (ta-pocketa-pocketa-pocketa-pocketa-pocketa) of the new flame-throwers. REALITY

MRS. MITTY: (striking Walter on the shoulder) I've been looking all over this hotel for you. Why do you have to hide in this old chair? How did you expect me to find you?

WALTER: (vaguely) Things close in . . .

MRS. MITTY: What? Did you get the what's-its-name? The puppy biscuit? What's in that box?

WALTER: Overshoes.

MRS. MITTY: Couldn't you have put them on in the store?

WALTER: (protesting weakly) I was thinking. Does it ever occur to you that I am sometimes thinking?

MRS. MITTY: I'm going to take your temperature when I get you home.

NARRATOR: They went out through the revolving doors that made a faintly derisive whistling sound when you pushed them. It was two blocks to the parking lot. At the drugstore on the corner . . .

MRS. MITTY: Wait here for me. I forgot something. I won't be a minute.

NARRATOR: She was more than a minute.

WALTER: (lighting a cigarette, he leans against the wall of the drugstore, smoking)

DAYDREAM #5

WALTER: (putting his shoulders back and his heels together, he says scornfully) To hell with the handkerchief! (takes one last drag on the cigarette and snaps it away)

NARRATOR: Then, with that faint, fleeting smile playing about his lips, he faced the firing squad; erect and motionless, proud and disdainful, Walter Mitty the Undefeated, inscrutable to the last.
```

---

## IC-1412: A Sermon

- Title: A Sermon
- Author (byline): David Mamet
- Work: Found in Take Ten: New 10-Min Plays (ed Lane & Shengold)
- Publisher: Vintage Books
- Publication date as stated: March 1997
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1239
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Mamet
Book: Found in Take Ten: New 10-Min Plays (ed Lane & Shengold)
ISBN: 0679772820
Publisher: Vintage Books
Date(Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
A preacher was on program at a district convention to preach for twenty minutes. The other preachers from the district were sitting behind him in the choir section, giving him moral support and throwing in an occasional "Amen" to help the preacher along. The preacher preached his twenty minutes and continued on despite allotted time. He preached for 30 minutes, then forty minutes and then for an hour. He even continued for an hour and ten minutes. Finally, a brother sitting on the front row took a song book and threw it at the preacher who was still going strong in his message. The preacher saw the song book as it was hurled his way and he ducked. The song book hit one of the preachers sitting in the choir section. As the man in the choir section was going down, you could hear him say, "Hit me again, I can still hear him preaching!" We’ve struggled to maintain consciousness through those early Sunday morning sermons that seem to go on and on and on . . . Perhaps A Sermon by David Mamet is his satirical, non sequitur revenge.
```

### Performance text (classify this)

```text
In September, 1939, a dentist in Viceroy, Louisiana, placed a human tooth into a jar of Coca-Cola and let it stand overnight. The next morning Hitler invaded Poland.

A man has a deaf yak. The yak cannot hear. It grew up deaf. And this man speaks to it: "How are you today, King?" "Bow wow," says the yak one day. Bow wow. And the next day the yak goes "moo." (Pause.) The animal has no idea of its respon-sibilities. It knows that something is required of it; it knows that it should make a sound, but it has no idea what that sound is supposed to be.

Life is like that. I feel. If it were not one thing, it would surely be another. It is, however, one thing. Though it is by no means the same thing. Although it's always something of that nature. And kindness starts at home. You cannot beat your pets and pretend you forgot to take the garbage out and go be nice to whales. It's not right, it's transparent, and it makes you look bad, too.

Let's talk about love. (Pause.) Love. My golly, it sells diapers, don't it! Love is the mucilage that sticks the tattered ribbons of experience-the stiff construction-paper Indians and pumpkins of experience-to the scrapbook of our lives.

And there may be many kinds of love: Love may be the Rocky Coast of Maine, with boats and salt spray gooshing up and you all cozy in the rented cabin. All the others have gone down. Gone down to Boston, gone back to New York. His hands are pressing into the small of your back. His breath is hot upon your shoulder. You have come to write and he has forced the lock. You've never seen this man, he followed you home from the pier. But do you care? You care very much. You whack him with the cover of your typewriter. Whack, whack, whack. Whack, whack, whack. Whack, whack, whack. You hit him on the head. And he leaves. (Pause.) You go back to work. You're typing. "September 18th. Today dawned bleak and serene and I was up to see it. Surely there must be an end to time. . . "

You look down to read back your sentence to yourself. What do you see but weak and colorless impressions. Your ribbon has run out. Oh well, that's a fair excuse to go up to the Lodge to share a cup of coffee with the Kind Old Woman who runs the resort.

You open the door. You breathe in the cold, life-giving spray. The Old Man from the Pier hits you on the head with an oar and this time he has brought his friends.

And what of Death? (Pause.) What of it? That's my question. All of us are going to die, but nobody believes it. And if we did believe it we would not go to the office. We would call in sick. Everybody's talking about "Death." Nobody's been there. Yes, yes, yes, there is a rash of testimony to the effect that Ms. So-and-So or Mr. Whossis once was dead for thirty seconds, or something, and it was just like going through a car wash.

You lay back and it is warm and wet outside. But you feel nothing. Whiirrrr, whiirrrr, and here comes the soap. And everything clouds over. Then you hear a hum. And that must be the brushes. Everything goes white, then black, then white again. You feel a buffeting. There is a wall of water. It cascades over the windshield, wetting all, and driving off the sludge, the salt, the road dirt and the soap. Until you're clean. You're clean.

Then comes the hot wax. Analogous in the experience of death to-what? (Pause.) Exactly. Hot wax coursing for a mere half-dollar more with ten bucks worth of gas. (Well worth it) making your car shine. Shine on. Shine on, my car. (Pause.)

Five youths dressed in coveralls drop upon you like ministering angels, rub your imperfections out and then move on. You'd better tip them, though, cause you'll be back this way again! There you go. Out into traffic. And how proud you feel. And why not? (Pause.) This is death. You've been there before, you say... well, you're going there again.

And sickness. Is it real? And suffering? (Pause.) Are they real? (Pause.) Yesterday a man was going to the supermarket. There he went. Upon some errand. His head full of news or gossip. Fiscal problems... (They are never really far away. . .) He turned the corner and he trod upon the mat which would open the door, and he walked on. The door, however, some of you have already guessed, did not open. Not a jot. (Pause.) He slammed right into it and broke his nose.

His blood flowed. As many times may happen, attendant upon a sharper blow to that area-particularly such a blow to one unused to violent contact-he began to cry. (Pause.)

Many who had seen his accident were laughing at the picture that it made. And then we heard him cry. And then he turned, and then we saw the blood. (Pause.) I’ve broke my nose," he rather oinked. "I've broke my nose, and you think it's funny." (Pause.) He could not think of what to say; a phrase which might instill in us, the spectators who deigned to ridicule his pain, shame or remorse. His mind searched for a curse. (Pause.) "*** you," he said. (Pause.) *** you.

What is required of us? To whom do we owe allegiance, and is this a laughing matter, or should we just mope around as if the dog died? This is a good question, and in conclusion, let me say the following:

A traveler is in the desert. He has lost his way. He has no water. And he is near death. Far off he sees a mountain. In the distance. Far away. Ice encapsulates its top and flows in freshets down its sides, and becomes springs and rivers. Cool, fresh water, redolent of trout. Clean, unpolluted, there for all to drink, to bathe in, to enjoy. And he knows it is a mirage. (Pause.) There is no mountain there. There is but desert. But he trudges on toward it in any case. (Pause.) Whom should we identify with in this story? (Pause.) How many thought the trout? It's not the trout. It's not the trout at all. We've all been down. We've all been at the end of our rope. We all know what it is to call on powers-and let's pray that they exist-far greater than ourselves; to call out, "Lord... Lord, this world of yours sucks, I just can't hack it anymore." And what answer was forthcoming? (Pause.)

Exactly. Therefore, let's smile. Let's slap a silly grin on our face that says to all the world, "Yes, I see what's going on, but I'm pretending not to notice. I see the misery... the pain . . . the hopes frustrated in our daily lives... the fear of loneliness... the fear of death..." I'm going to skip to the end of this list" . . . and through it all I smile, and I say, with the prophets: 'Lo, this world has been the same a great long while. It all shall be the same a hundred years from now probably sooner." (Pause.)

And that's it. Therefore be well. Peace to you. Be very kind to one another in your daily lives. And clean up when you're done. Good evening, and Amen.
```

---

## IC-1413: The Seven Chickens

- Title: The Seven Chickens
- Author (byline): AJ Jacobs
- Work: Fractured Fairy Tales
- Publisher: Bantam
- Publication date as stated: Jan 1999
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, PRINCE, KING, CHICKEN, KNIGHT
- Teaser before the introduction: No
- Spoken words (computed): 846
- Already set (do not supply): none

### Source block (context only)

```text
Author: AJ Jacobs
Book: Fractured Fairy Tales
ISBN: 978-0553099805
Publisher: Bantam
Date (Month/Year): Jan 1999
```

### Introduction (context only: never use it for content warnings)

```text
The world of fairy tales are filled with memories of myths and legends, princes and knights, ogres and witches . . . . and in this case chickens. In cartoons today, chickens are often depicted as fussy and silly — think Foghorn Leghorn and Prissy in Looney Tunes cartoons, or Lady Cluck in Robin Hood. They don’t exactly radiate mysterious elegance. And we will continue that grand tradition in today’s tale . . . . The Seven Chickens by AJ Jacobs.
```

### Performance text (classify this)

```text
NARRATOR: Once upon a time there was a young prince who ventured into the woods in search of game. During the course of the long day, he got tired and hungry.

PRINCE: Next time, bring trail mix.

NARRATOR: Finally, as it got dark, he came across a great castle. He knocked. A king opened the door.

KING: If you're selling magazines, we don't want any. Go away.

PRINCE: Wait (putting his foot in the door to stop it) I am a handsome young prince who has lost his way. Could you see your way clear to sparing me the bare essentials for a night-say, a thirty-two-course meal, a dozen ser-vants, and a suite with a roaring fireplace?

NARRATOR: The king figured this was reasonable enough. Especially for a prince. And he led him inside to the dining room, where dinner was being served. But there, the prince was shocked by what he saw. For in the chairs around the table sat seven chickens. Figuring someone had left the henhouse door open-or had taken the idea of free range a bit too far-the prince began chasing the birds out of the room.

PRINCE: (herding chickens) Shoo! Scat!

KING: (Shouting) Stop that! Leave those girls alone!

NARRATOR: The seven chickens again took their appointed places at the table and they, along with the king, proceeded to peck away at the dishes of corn that sat before them.

KING: (pecking at his plate and then wiping a yellow kernel from his nose) What's the matter, boy? You haven't pecked a thing on your plate.

PRINCE: Suddenly, I'm not hungry.

CHICKEN: Awwk, buk, buk, Awwwwkkkk, cluck

KING: What's that, Florence?

CHICKEN: Awwwk, buk, buk, buk, Squawwwwwkkkk, cluck, cluck.

KING: (laughing loudly) Very funny. Very funny.

PRINCE: (with wide eyes) What just happened?

KING: Florence just told a joke. Now, son. I'm glad you came along. I've got a problem.

PRINCE: I noticed. You're a nut!

NARRATOR: The king went on to tell the prince an incredible tale of a witch who came to the castle and cast an evil spell that turned all of his loving daughters into chickens.

PRINCE: So that's it. Those seven chickens are your daughters.

KING: No. Six of them are my daughters. The seventh one is the witch herself.

PRINCE: Here comes the plot.

KING: Right. The spell on my daughters cannot be broken until I can discover which one of the seven chickens is the witch.

NARRATOR: Well, now, this is the sort of thing all handsome princes dream of. All he would have to do is discover which of the seven chickens was the witch and the king would surely reward him with the Hand of the most beautiful of his daughters. The next morning he got up with the chickens and set about his task. He watched those seven chickens like a hawk.

KING: It's no use, boy. Chickens have the nasty habit of looking just alike."

PRINCE: True, but they don't think alike. The one that is the witch thinks like a witch.

NARRATOR: With that in mind, the prince disguised himself as a beautiful maiden. He figured if he pretended he was Snow White, no witch in the world could resist.

PRINCE: (twirling to show off his dress) I am Snow White! I hope that there's no witch in the castle disguised as a chicken. And I hope that witch disguised as a chicken won't give me a poisoned apple.

NARRATOR: None of the seven chickens paid the slightest bit of attention, but an ogre who happened to be casing the castle did. He wasted no time in grabbing the so-called maiden and making off with her to his cave. But just then a handsome knight chanced to arrive on the scene and rushed to the rescue.

KNIGHT: Never fear, fair beauty. I shall save you.

NARRATOR: With that, he flew at the ogre and the fight was on. (fight ensues between the knight and ogre) The knight won out with a combination uppercut to the right jaw and a rabbit punch to the kidneys.

(pantomime this fight)

KNIGHT: (Grabbing the prince-in-a-dress around the waist) Ah, fair maiden . . Your lips ... your eyes.

PRINCE: (responds with a sharp uppercut to the right jaw and a rabbit punch to the kidneys)

KNIGHT: (rubbing his face) Oooh, I like her.

NARRATOR: The prince, whose high heels made him a bit slower than normal, finally made it back to the castle and began trying to slither out of his Snow White suit. But before he could, the chickens gathered around him, curious to see what the commotion was.

PRINCE: (trying to remove his dress) Girls! Not now! Go away. (he grabs a broom and starts swatting at them, hopping to shoo them away.

NARRATOR: They all scattered. All, that is, except for one. That one snatched the broom from the prince, hopped on it, and flew around the room. Now, centuries of inbreeding couldn't weed out all traces of logic from the prince's mind. Witches, he figured, like brooms. Chickens don't. That one is the witch! The spell was broken. And not only did the witch turn back into a witch, but the six chickens were turned back into the king's beautiful daughters, a little plumper and more corn-fed for the experience.

KING: My boy! As a reward, I'm going to give you any daughter you wish to be your bride.

NARRATOR: Unfortunately, however, before the prince could choose, the knight who still thought the prince was a fair maiden galloped in, swept him off his feet, and galloped away. The prince's mother had told him there'd be days like that. But she had forgotten to warn him about the knights!
```

---

## IC-1414: Shrek - Screenplay

- Title: Shrek - Screenplay
- Author (byline): Ted Elliott, Terry Rossio, Joe Stillman and Roger S.H. Schulman
- Work: Not specified
- Publisher: Scriptfly.com
- Publication date as stated: March 2011
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: SHREK, HEAD GUARD, DONKEY, PINOCCHIO, FARQUAAD, MIRROR, WOODEN PEOPLE, FIONA, WHISPER
- Teaser before the introduction: Yes
- Spoken words (computed): 1445
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ted Elliott, Terry Rossio, Joe Stillman and Roger S.H. Schulman,
based loosely on the book by William Steig
ISBN: N/A
Publisher: Scriptfly.com
Date (Month/Year): March 2011
```

### Introduction (context only: never use it for content warnings)

```text
Join me today for a fractured fairy tale about a smelly ogre with a bad disposition. He sets out on a quest to rescue a beautiful princess from a fire-breathing dragon. The princess packs a punch, however, that softens his heart.

And through the story, we learn 3 very essential lessons: 1) The importance of being our authentic selves, for true beauty is found within; 2) You don’t have to be what everyone expects you to be; and 3) True love is often found in unexpected places and people.

Shrek by Ted Elliott, Terry Rossio, Joe Stillman and Roger S.H. Schulman based loosely on the book by William Steig

Shrek is going about his day, perhaps digging up onions for dinner, or cleaning the windows of his cottage.

HEAD GUARD: (Pg 5) (with false bravado --- he’s really scared of ogres) You there. Ogre!
```

### Performance text (classify this)

```text
(based loosely on the book by William Steig)

SHREK: (Pg 1) Once upon a time there was a lovely princess. But she had an enchantment upon her which could only be broken by love's first kiss. She was locked away in a castle guarded by a terrible fire-breathing dragon. She waited in the dragon's keep in the highest room of the tallest tower for her true love and true love's first kiss. (laughs) Like that's ever gonna happen!

SHREK: (he turns) Aye?

HEAD GUARD: By the order of Lord Farquaad I am authorized to place you under arrest and transport you to a designated resettlement facility.

SHREK: (menancingly) Oh, really? You and what army? (the guard looks behind him to see that no one is behind him) (Shrek makes a move toward the guard, who screams and runs)

(laughing Shrek returns to his work – Donkey enters)

DONKEY: Wow! Those guards! They thought they was all that. Then BAM! They was trippin’ over themselves. Incredible! (Pg 6) You’re a mean, green, fightin’ machine! (Shrek turns and regards Donkey for a moment, then roars very loudly) Oh, wow! That was really scary. (reacts to the smell of Shrek’s breath) If that don’t work, your breath certainly will get the job done. You need some Tic Tacs or somethin’ cause your breath stinks! (Shrek covers his mouth, embarrassed)

SHREK: (Pg 7) I am an ogre, you know. “Grab your torch and pitchforks.” Doesn’t that bother you?

DONKEY: Nope. I like you. What’s your name?

SHREK: (taken aback – no one likes an ogre) Uh, Shrek. (he walks away, but Donkey follows)

DONKEY: You know what I like about you, Shrek? You got that kind of I-don't-care-what-nobody-thinks-of-me thing. I respect that. You all right. (Shrek shakes his head, exasperated and turns to go inside his cottage) (Pg 6) Hey, wait a minute! I got a great idea! I'll stick with you. Together we'll scare the spit out of anybody that crosses us. *****Scene – The next morning*****

SHREK: (Pg 11) (Shrek is awoken by loud noises of chaos outside – It sounds like a party – He angrily rushes outside and roars) What are you doing in my swamp? (the crowd goes silent)

PINOCCHIO: (gulps, then answers) We were forced to come here. Lord Farquaad huffed and he puffed and he . . . signed an eviction notice.

SHREK: (heavy sigh) (Pg 12) Okay. Attention, all fairy tale things. I’m gonna see this guy Farquad right now and get you all off my land and back where you came from! (the crowd cheers) Do not get comfortable. Your welcome is officially worn out. Who know where this Farquaad guy is?

DONKEY: Oh, I do. I know where he is?

SHREK: (purposely ignoring Donkey - overlapping) Anyone else? Anyone at all?

DONKEY: Oh! Oh, pick me! I know! Me . . . Me!

SHREK: (sighs) Okay, fine. You’re comin’ with me (Shrek and Donkey exit)

*****Scene – Lord Farquaad’s Castle*****

FARQUAAD: (Pg 13) (speaking to a few fairy tale creatures) I'm not the monster here. You are. You and the rest of that fairy tale trash, poisoning my perfect world. (he motions for them to leave, then turns to the Magic Mirror on the Wall) (Pg 15) Mirror, mirror on the wall. Is this not the most perfect kingdom of them all?

MIRROR: Well, technically you're not a king. (Farquadd responds as if to smash the mirror) What I mean is you're not a king YET. But you can become one. All you have to do is marry a princess. (chuckles nervously, then continues as a game show host) So, just sit back and relax, my lord, because it's time for you to meet today's eligible bachelorettes. Bachelorette number one – Cinderella! Her hobbies include cooking and cleaning for her two evil sisters. (Cinderella strikes a pose) Bachelorette number two – Snow White! Although she lives with seven other men, she's not easy. (Snow White strikes a pose) And last, but certainly not last, Bachelorette number three is a fiery redhead who likes pina coladas and getting caught in the rain. Yours for the rescuing -- Princess Fiona! (Fiona strikes a pose)

FARQUAAD: (Pg 16) Princess Fiona. She’s perfect! (to himself) All I have to do is find someone who can go . . .

MIRROR: I should probably mention the little thing that happens after sunset . . .

FARQUAAD: Silence! *****Scene – Shrek and Donkey arrive in DuLoc*****

DONKEY: (Pg 17) That’s it! That’s DuLoc!

SHREK: (looking up at a 40-story castle) So, that must be Lord Farquaad’s castle.

(As they approach the gates to the city, Donkey knocks on the gate and music begins to play – 2 wooden people emerge from each side of the gate and begin to sing)

WOODEN PEOPLE: (Pg 18-19) (Singing and dancing)
Don't make waves, stay in line
And we'll get along fine
DuLoc is the perfect place
Please keep off of the grass
Shine your shoes, wipe your... face
DuLoc is, DuLoc is
DuLoc is the perfect place.

(Donkey and Shrek respond; Shrek is disgusted and Donkey excited)

DONKEY: Wow! Let’s do that again! (Inside the gates, a trumpet sounds and Lord Farquaad is speaking to a group of knights)

FARQUAAD: Brave knights, today one of you shall have the honor – no, no – the privilege to rescue the lovely Princess Fiona from the fiery keep of the dragon. Some of you may die, but it’s a sacrifice I am willing to make. (he notices Shrek) Oh! What is that? It’s hideous! (Shrek points to himself, confused) Knights, new plan! The one who kills the ogre will be named champion! (A fight ensues – Suffice to say that Shrek kicks butt) (Somewhat disgusted with the poor showing of his knight, Farquaad sighs) (Pg 20-21) Congratulations, ogre. You’ve won the honor of embarking on a great and noble quest.

SHREK: Quest? I’m already on a quest – a quest to get my swamp back. My swamp! Where you dumped those fairy tale creatures!

FARQUAAD: All, right, I’ll make you a deal. Go on this quest for me, and I’ll give you your swamp back. (as Donkey and Shrek leave DuLoc)

DONKEY: Let me get this straight. You're gonna go fight a dragon and rescue a princess just so Farquaad will give you back a swamp. I don't get it. Why don't you just pull some of that ogre stuff on him? Throttle him, grind his bones to make your bread . . .

SHREK: (Pg 27) (interrupting) Donkey, two things, okay? Shut . . . . Up! *****Scene – Shrek and Donkey arrive at the Dragon’s tower*****

SHREK: The princess will be up the stairs in the highest room in the tallest tower. Go over there and see if you can find any stairs (Shrek walks off)

DONKEY: (talking to himself) Cool. You handle the dragon. I’ll handle the stairs. I’m the stair master! (Donkey rounds a corner and . . . ) (Pg 28) Aah! DRAGON!!! (Dragon roars and flaps its wings) That’s one dazzling smile you got there. And you know what else? (flaps turn decidedly “show-girl”) You’re a girl Dragon! Just reeking of feminine beauty. (Dragon flutters her eyes) SHREK!

*****Scene – Shrek arrives at Fiona’s Room***** Fiona appears to be asleep. Shrek enters, looks at her and she puckers her lips. Shrek is not entranced. He takes her by the shoulders and shakes her.

SHREK: (Pg 29) Wake up! (she rouses) Are you Princess Fiona? Let’s go!

FIONA: Wait! You should sweep me off my feet out yonder window and down a rope onto your valiant steed. Recite an epic poem for me. A ballad? Something!

SHREK: Yesh, sorry, lady. There’s no time (the dragon roars)

FIONA: (surprised – she looks out the window) You didn’t slay the dragon? (Shrek grabs Fiona and runs out. He grabs Donkey and delivers them all to safety) (Pg 32) You did it! You rescued me! You’re amazing. (Pg 34) It’s destiny! A princess locked in a tower and beset by a dragon is rescued by a brave knight, and then they share true love’s first kiss.

DONKEY: With Shrek? Wait. You think that Shrek is your true love? (Donkey and Shrek burst out laughing)

SHREK: (Pg 40-41) Look . . . I’m better off alone. People take one look at me and go “Aah! Help! Run! A big, stupid, ugly ogre!” They judge me before they even know me.

FIONA: (Pg 35) But, I have to be rescued by my true love, not by some ogre and his . . . his pet.

(Donkey is offended)

SHREK: Princess, I was sent to rescue you by Lord Farquaad. He is the one who wants to marry you.

FIONA: (Pg 36) And what of my groom-to-be? Lord Farquaad? What’s he like?

DONKEY: There are those who think little of him. (he laughs)

SHREK: Let me put it this way, Princess. Men of Farquaad’s stature are in short supply (he laughs) (Pg 37) But I’ll let you do the “measuring” when you see him tomorrow. (Shrek exits to find a place to camp)

FIONA: (to Donkey) Tomorrow? (she’s obviously worried) It’ll take that long? (she notices the setting sun) (Pg 51) Sunset? Oh, no!

MIRROR: (Pg 16) (echoing voice off stage) I should probably mention the little thing that happens after sunset . . .

FIONA: (Pg 53-54) Oh, no! (Fiona begins to change into an ogre, burping and farting may be involved))

DONKEY: (freaking out) Aah! (calling off) Shrek! Shrek! What did you do with the princess? (shocked) You ate [her]?!!!

SHREK: (Pg 56) (cut to Shrek to is talking to himself as he picks a flower, he practices) Princess? I saw this flower and thought of you because it’s pretty. Well, I don’t really like it, but I thought you might ‘cause you’re pretty. But I like you anyway! (he continues to practice in pantomime)

FIONA: (Pg 54-56) Donkey, I’m the princess. In this body. It only happens when the sun goes down. (sighs) When I was a little girl, a witch cast a spell on me . . . until you find true love’s first kiss . . . and take love’s true form.” Every night I become this horrible, ugly beast! That’s why I have to marry Lord Farquaad before the sun sets tomorrow and he sees me like this! (Shrek approaches the clearing just in time to hear . . . ) I mean, really, who can ever love a beast so hideous and ugly. “Princess” and “ugly” don’t go together. (Shrek heaves a deep sigh, throws the flower down and walks away)

DONKEY: Princess, how ‘bout you don’t marry Farquaad . . . You’re kind of an orge, and Shrek – well, you got a lot in common. *****Scene – The next morning*****

(Fiona sees the rising sun and as it rises, she turns back into a human – she searches for Shrek who never returned the night before)

FIONA: (Pg 57-58) Shrek? Shrek! There’s something I want . . . I have to tell you.

SHREK: You don’t have to tell me anything, Princess. I heard enough last night. Like you said, “Who could love a hideous, ugly beast?”

FIONA: (misunderstanding) But I thought that wouldn’t matter to you.

SHREK: (also misunderstanding) Yeah? Well, it does. (Fiona looks at him in shock and dejected, she exits – Donkey enters)

DONKEY: Shrek, what are you doing? You’re letting her get away.

SHREK: Yeah? So what?

DONKEY: Shrek, there’s something about her you don’t know. I talked to her last night . . . (Pg 63) All she ever did was like you, maybe even love you.

SHREK: Love me? She said I was ugly, a hideous creature. I heard the two of you talking.

DONKEY: She wasn’t talkin’ about you! She was talking about . . . Why don’t you just go ask her?

SHREK: (Pg 67-68) (Overcome by emotion, Shrek swallows his pride and searches for Fiona) Fiona! I need to talk to you.

FIONA: (angrily) Oh, now you wanna talk? It’s a little late for that.

SHREK: (hesitantly) You can’t marry [Farquaad] . . . He’s not your true love.

FARQUAAD: (Pg 13) (echoing) I'm not the monster here. You are. You and the rest of that fairy tale trash, poisoning my perfect world.

FIONA: And what do you know about true love?

SHREK: Well, I . . . uh . . . I mean . . . (he gathers his courage) (Pg 70) I – I love you.

FIONA: (smiles) I love you too! (they kiss – and the magic of the spell begins to work)

SHREK: (Pg 1) Once upon a time there was a lovely princess. But she had an enchantment upon her which could only be broken by love's first kiss.

WHISPER: (echoing) (Pg 71) Until you find true love’s first kiss and take love’s true form . . . true form . . . true form. . . (Fiona is transformed into her true self – an ogre – some burping and farthing may be involved)

SHREK: (Shrek is shocked and overjoyed) Fiona? You are beautiful! (burps, the both laugh and kiss again)
```

---

## IC-1415: The Skunk Ladder

- Title: The Skunk Ladder
- Author (byline): Patrick F.McManus
- Work: The Grasshopper Trap
- Publisher: Owl Books
- Publication date as stated: Sept 1986
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: BUN, PAT, MR. MULDOON, EDDIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1226
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patrick F.McManus
Book: The Grasshopper Trap
ISBN: 978-0805001112
Publisher: Owl Books
Date (Month/Year): Sept 1986
```

### Introduction (context only: never use it for content warnings)

```text
The Skunk Ladder by Patrick F. McManus
```

### Performance text (classify this)

```text
PAT (to audience): Driving out to the country the other day, my wife, Bun, and I passed the aromatic remains of at least ten road-killed skunks. (to Bun) Must be a good year for skunks

BUN: Looks like a bad one for them, if you ask me. PAT (to Bun): I mean there’s obviously a large skunk population this year. (to audience) Just then a live skunk scurried out in front of the car. I swerved to the left and back to the right, and we managed to screech safely around it.

BUN: Goodness, that was close! What would you have done if you’d hit that skunk with the car?

PAT: The only decent thing. I’d have stopped and buried it in the ditch. I might even have buried the skunk along with it.

BUN: You talk as if you’ve had a lot of experience with skunks

PAT: You bet. Mostly when I was a kid. You mean I’ve never told you about the skunk ladder? Boy do you have a treat in store for you!

PAT: My friend Crazy Eddie Muldoon and I were sitting on the corral fence one summer afternoon, trying to think of something to do. Mr. Muldoon came by on his tractor and stopped to study us suspiciously.

MR. MULDOON: What are you two up to now?

EDDIE: Just trying to think of something to do.

MR. MULDOON: Well, when you think of it, you let me know before you start to do it, you hear?

EDDIE: Sure, Pa. I guess what we’ll do is go dig in the dirt. We’ve been talkin’ about doin’ that.

MR. MULDOON: Okay. Just don’t build nothing!

PAT: (to audience) Then he drove off. (to Eddie) What kind of hole are we going to dig? (to audience) He stared off into space, his face enveloped in that dreamy expression that always accompanied one of his wondrous new ideas.

EDDIE: A big hole. A real big hole.

PAT: There are basically two kinds of holes: (1) applied holes such as for posts, wells, mines, etc. and 2) holes for holes’ sake. Eddie and I were digging one of the latter. Digging the hole occupied us for most of a week. Eventually, the hole was so deep we could barely heave shovelfuls of dirt up over its sides. And since Eddie had insisted that we keep the sides of the hole squared up, we had to pull ourselves out of it on a rope, one end of which was tied to a pile of stumps nearby. We were immensely proud of the hole. It was so nice, in fact, that Eddie began trying to think of it as practical.

EDDIE: You know what we could do with this hole? We could make a wild animal trap out of it, you know, like in Africa. We could cover it up with branches and leaves and grass, and wild animals would come along and fall into it. Then we could tame them and teach them to do tricks. . . . And then we could start our own circus. We could charge people. We might even get rich. Gosh, I bet we could catch a deer or an elk or a bear or a mountain lion or . . .

PAT: One of your father’s cows.

EDDIE: Yeah, I never thought of that . . . Tomorrow we’d better fill the hole back in.

PAT: How about tonight? Maybe a cow will fall in tonight.

EDDIE: I got it. There’s a big ol’ door out behind the barn. We’ll drag that down here and put it over the hole.

PAT: And that is what we did. Secure in the knowledge that the door would save us from the uncomfortable experience of watching his father undergo one of his fits of hysteria. Early the next morning, Eddie and I headed for the big hole, prepared to start the tedious task of undigging it. As we approached the excavation, a familiar odor reached our nostrils.

EDDIE: Must be a skunk around here someplace.

PAT: Maybe it’s in thehole.

EDDIE: Couldn’t be. We covered it with the door.

PAT: (to audience) Nevertheless, the skunk was in the hole. He had found an open space under the door, slipped in for a look around and plummeted the eight feet or more to the bottom. Oddly, for we did not know that skunks were great diggers, he had hollowed out a huge covern under one side, in an attempt to dig his way out of the hole. (to Eddie) We can’t fill in the hole with the skunk in there. How are we going to get him out?

EDDIE: Maybe one of us could drop down in the hole, grab him real quick before he sprays, and then throw him out. I’ll yell real loud so he’ll look at me and won’t notice when you jump in and grab him and . . .

PAT: I don’t like that idea. Think of something else.

EDDIE: I got it! We’ll go up to my dad’s shop and build a ladder. Then we’ll stick it down the hold and hide someplace while he climbs the ladder. A skunk should be able to figure out how to climb a ladder.

PAT: Eddie and I were working on the ladder when his father walked into the shop.

MR. MULDOON: I thought I told you not to build anything. What’s that?

EDDIE: Just a skunk ladder.

MR. MULDOON: Oh, well, don’t build nothin’ else unless you tell me first.

PAT: Eddie and I went back out to the hold and stuck the ladder in it. The skunk showed no inclination to climb it, choosing instead to hide in the cavern it had hollowed out. Just then we heard Eddie’s father yelling . . . .

MR. MULDOON: What did you mean, skunk ladder?

EDDIE: Quick, help me put the door back over the hole!

PAT: We threw the door over the top of the hole, neatly hiding it from view.

MR. MULDOON: Now what? Where did that dirt come from? What’s my door doing out here?

PAT: He reached down and grabbed the edge of the door.

EDDIE: Stop, Pa, don’t!

PAT: From that point on, the actions of the parties involved all blurred together. Mr. Muldoon grabbed the door and flipped it off the hole.

MR. MULDOON: Smells like a skun . . . .

PAT: At which time he shot out of sight. A cloud of dust puffed up out of the hole when Mr. Muldoon hit the bottom. Then he yelled several serious swear words with the word

MR. MULDOON: SKUNK!

PAT: mixed in with them. Next there were a lot of earthy scrabbling sounds, and Mr. Muldoon came clawing his way up the side of the hole, but the dirt gae way and he fell back in saying something like

MR. MULDOON: Oooffff!

EDDIE: Pa, Pa, don’t hurt him!

PAT: He was standing at the top of the ladder when the skunk rushed up and emerged from the cloud of dust. Startled and not wanting the skunk to reverse ends and spray him, Eddie grabbed the animal by the head. The skunk started scratching and biting, so Eddie threw it back down in the hole, where its arrival was followed by a savage bellow from Mr. Muldoon, who came racing up the skunk ladder himself. This was the signal for Eddie and me to start running. Eddie eventually made his way home and placed himself under the protective custody of his mother. In the ruckus at the skunk ladder, Eddie had been hit in the face with a slight charge of skunk spray. Worried at first that the spray might have affected his brain, Mr. and Mrs. Muldoon finally assumed there would be no lasting ill effects. Twenty years later, however, Crazy Eddie became a Ph.D. in chemistry!
```

---

## IC-1416: Soap Opera

- Title: Soap Opera
- Author (byline): David Ives
- Work: Time Flies and Other Short Plays
- Publisher: Grove Press
- Publication date as stated: April 2001
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: LOUDSPEAKER VOICE, MAITRE D’, REPAIRMAN, MOTHER, MABEL, WASHING MACHINE
- Teaser before the introduction: Yes
- Spoken words (computed): 1646
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Ives
Book: Time Flies and Other Short Plays
ISBN: 978-0802137586
Publisher: Grove Press
Date (Month/Year): April 2001
```

### Introduction (context only: never use it for content warnings)

```text
Soap Opera by David Ives
```

### Performance text (classify this)

```text
LOUDSPEAKER VOICE: (Soap opera-like music) Welcome to . . . "All the Days of the World of the Lives of All of Our Children." Today's episode: "Love Machine." Lights come up on a FRENCH MAITRE D’ at a restaurant podium, taking a phone reservation.

MAITRE D’: (into phone) Bonsoir, Cafe Paradis, this is Pierre. . .Ah, oui, bonsoir, madame. . . A table at 8:15? Yes bien. I 'ave written your name in ze Beeg Book. . . A bientot to you, chere madame. My plaisir. During this, the REPAIRMAN has entered, pushing a WASHING MACHINE. He wears a dignified blue service uniform, red bowtie, and blue visored cap.

REPAIRMAN: Excuse me.

MAITRE D’: Mm-hmmmmm... And do you have a reservassyonnng?

REPAIRMAN: I do-for deux, under "Maypole."

MAITRE D’: Maypole. Mmmmmmmmmmmmmm . .. (checks reservation book) Has your other party arrived, monsieur?

REPAIRMAN: (gesture to the washing machine) This is my other party.

MAITRE D’: Monsieur, is your companion not a majeur household appliance?

REPAIRMAN: Yes. She is a Maypole washing machine

MAITRE D’: "She"... is a washing machine! Per'aps you would like to sit at ze bar. But-one moment, monsieur. . . Have I not seen you somewheur . . . ? Mais oui! La television! Are you not ze Maypole Repairpersonne?

REPAIRMAN: I am the Maypole Repairman.

MAITRE D’: The Repairman who weeps because he has nothing to

REPAIRMAN: Yes. Yes.

MAITRE D’: Who goes beu-eu-eu because la machine is too peifecte?

REPAIRMAN: Yes. That is I. (He bursts into tears and sobs loudly and tragically.) Oh, it's so sad. It's so, so sad!

MAITRE D’: (holds out a handkerchief) Mouchoir, monsieur?

REPAIRMAN: (takes it) Merci. (abruptly stops sobbing and speaks to audience) Like everything else, it all started a long time ago. . .

REPAIRMAN: It was as a naked crawling infant I first glimpsed it-a great gleaming machine in our basement which I mistook for a television. I tried to watch cartoons on it till I was five unsuccessfully, of course. But by then I was hooked.

MOTHER: Young man, you take off those filthy clothes immediately! How can you stand to stand there in those disgusting dirty items of apparel. Coke. Pepsi. Play-Doh. Dipsy Doodles. Dog doo . . . ? Eugh! Ogh! Peh! Ptui! I should just burn these clothes.

REPAIRMAN: Aw, Mom. I just put these on this morning.

MOTHER: Fabrics find filth. Now strip until you're naked as a little ferret. And get in that bath and scrub. (exits)

REPAIRMAN: The sphinx in our Oedipal basement was my Mother 's Maypole. The old Ocean IT-40 It sat there like a mystical monolith. An ivory soap tower. One block of some Tower of Bay bel. Or is it Babble. Anyway, in our house the Maypole was a god. Week after week generating out of my miserable clay . . . A line of clean washing flies in over his head-white, filmy, angelic forms, including one cutout of an angel . . . the radiant angels who oversaw my childhood. I was a walking magnet for filth-here was the machine to cleanse me. We were a perfect match. MABEL enters, a teenage girl in bobby sox and ponytail, chewing gum, sucking on a milk shake through a straw.

MABEL: Hi, Manny.

REPAIRMAN: Hi, Mabel. (to audience) Then there was Mabel. Mabel was perfect too, in a flawed human way. She always had a spot of jelly on her blouse, but she was loving, she was tender, and her name sounded like "Maypole." (to Mabel) You got a spot on your blouse.

MABEL: It's jelly. You wanna like go to like a movie or somethin'?

REPAIRMAN: You wanna hop up on the washer and take a spin?

MABEL: Manny, how come we always gotta make out on your Mother 's Maypole?

REPAIRMAN: Well like what's so like weird about that?

MABEL: Do we have to run a full load while we do it? I mean, the vibrations are kinda nice, but. . .

REPAIRMAN: But the Maypole. . .

MABEL: I know, I know. It's like perfect.

REPAIRMAN: A machine that's faultless and flawless and has none of our stupid human feelings and failings? The Maypole is poetry. It's purity. A paragon! Perfection, cubed!

MABEL: But like what about me? Do you like like me like you like the Ocean IT-40? And aren't you the love of my life? You are!

REPAIRMAN: Gosh, Mabel.

MABEL: I'm sorry, but you're gonna have to choose. Me or the machine. Earth or Ocean.

REPAIRMAN: Mabel? Mabel come back! He starts to weep. The top lid of the Machine lifts and a woman's head appears: perfect hair, perfect makeup, perfect red lips.

WASHING MACHINE: Would you like a handkerchief?

REPAIRMAN: Excuse me?

WASHING MACHINE: (produces one) A handkerchief? It's immaculate, of course. We are a Maypole.

REPAIRMAN: I'm talking to an Ocean IT-40. This harrows me with wonder and fear. And your English is so good.

WASHING MACHINE: What Maypoles do, we do perfectly.

REPAIRMAN: I guess you don't think much of human beings.

WASHING MACHINE: We run hot and cold. Do humans ever read the instruction manual?

REPAIRMAN: I do. The manual is my Immanuel.

WASHING MACHINE: And .your name is . . . ?

REPAIRMAN: Manuel.

WASHING MACHINE: Maypoles don't need to read the Good Booklet. We know by nature how to run smoothly, noiselessly, and efficiently.

REPAIRMAN: My God you're beautiful.

WASHING MACHINE: Just beautiful?

REPAIRMAN: Exquisite. Sublime.

WASHING MACHINE: Yes we are. And we're a bit hungry. Would you feed us?

REPAIRMAN: What would you like?

WASHING MACHINE: Don't you sometimes miss a little something in the wash. . . ?

REPAIRMAN: You eat the socks?

WASHING MACHINE: Socks are sustenance. Underwear is tastier.

REPAIRMAN: (reaches into his waistband and pulls out, whole) Will B.V.D.'s do?

WASHING MACHINE: You're so sweet. Kissing her lips at him, the head takes the B. V.D.'s and goes back into the MACHINE. The lid closes.

REPAIRMAN: (to audience) I was awash in confused feelings. But I sensed that this machine and I were locked in permanent press. And if it was love-it was unclean. Mom died during a soapflake blizzard and was buried on a day without blemish-a good send-off for someone who believed that man was not only dust, but dusty. I inherited the Maypole. The pure unapproachable goddess was mine. This machine and I are soulmates! Nobody understood. But who understood Romeo and Juliet, or Tristan and Isolde, or Lewis and Clark? I soon was desperate. So was Mabel. *******

MABEL: Can't you love me, Manny?

REPAIRMAN: What about my past with. . . the machine?

MABEL: We all have our dirty laundry.

REPAIRMAN: There's a spot on that.

MABEL: It's jelly. So do you want to marry me or do I gotta live in sadness forever and ever?

REPAIRMAN: I do.

MABEL: You do?

REPAIRMAN: I do. (to audience) We repaired to the church and said we did. But the honeymoon soon ended.

MABEL: Manny, is it really all over between you and. . . that?

REPAIRMAN: (caressing the Machine) Yes, it's all over, why do you ask?

MABEL: Do you think I didn't notice we're sleeping in the utility room? Do you think I don't see you polishing its knobs when I'm not looking? Do you think I don't know you're buying me rare cottons and high-quality blends so that. . . she can wash them? Huh? Mabel exits.

REPAIRMAN: The house reeked of jealousy. The machine started making greater and greater demands. Imported Italian bleach. Nuclear detergents. Fine French fabric softener. Mabel bought none of it. She'd had it. And so we folded. I went into Soak cycle-lapping up suds while hanging out at cut-rate Laundromats, just to watch the competition break down. Washers without automatic lint control. How pathetic-and yet how vulnerable. Then came the final blow. The lid lifts and the head appears.

WASHING MACHINE: We want a dryer.

REPAIRMAN: A dryer. . . Why?

WASHING MACHINE: Don't get anxious.

REPAIRMAN: I'm not anxious.

WASHING MACHINE: Don't be jealous.

REPAIRMAN: Why do you need a dryer when you've got me?

WASHING MACHINE: Washer-dryer. Love-and-marriage. Horse-and-carriage.

REPAIRMAN: A dryer. To give you a tumble, eh?

WASHING MACHINE: For companionship.

REPAIRMAN: That's not the truth, that's just. . . spin.

WASHING MACHINE: We want a family and we want them to be Maypoles! Is that so weird?

REPAIRMAN: Her inner timer had told her it was time for a dryer and how could I deny her? (the Machine starts to cry) What is it? What's the matter?

WASHING MACHINE: (wailing) I'm a Maypole! That's what's the matter!

REPAIRMAN: Handkerchief? It's kinda dirty.

WASHING MACHINE: Then it's my duty to accept it. (takes the handkerchief, and wails) Oh, it's cruel, having to be perfect all the time. I wash and I wash, and I give, and I give. . . It's a full load.

REPAIRMAN: Sure.

WASHING MACHINE: And I'm good at it, oh yes, I'm very good. But sometimes I want so badly to be bad. To be one of those other makes-I don't have to name them, we know who they are. People take us Maypoles for granted, as if we liked pee stains and snot rags and bibs full of baby vomit. I'm no saint! Well, yes, I am a saint in a way.

REPAIRMAN: But you had to be what you are.

WASHING MACHINE: It's true. I came off the assembly line of fate. But AM I NOT AN INDIVIDUAL? Not really, I suppose. I have a serial number. That's individual, isn't it?

REPAIRMAN: There's nothing to be done.

WASHING MACHINE: Oh, but there is. "If it ain't broke don't fix it"? Break the machine, and you can fix it.

REPAIRMAN: You mean. . . ?

WASHING MACHINE: Yes. Break me.

REPAIRMAN: (to audience) I reached for a sledgehammer.

WASHING MACHINE: It doesn't have to be much. Loosen a screw or two, agitate my agitator. Take away the burden of my perfection. Make me suffer. Break me. Ruin me. Give me a belt, but give me a bad belt, an old belt, an imperfect belt, one that'll wear out. Do it. Please! Do it! Yes! Do it! Hurt me!

REPAIRMAN: Yes. Yes. I want to. Yes. . . I want to. Yes. . .The Repairman has a tool ready--but stops. (a cry of frustration)

WASHING MACHINE: What's the matter?

REPAIRMAN: I can't. I just can't.

WASHING MACHINE: Oh, please. . .

REPAIRMAN: If I could only force myself, but-Wreck the perfect only for my own happiness? No. I couldn't live.

WASHING MACHINE: All right. All right. You have your human feelings. BE THAT WAY! The head goes into the Machine.

REPAIRMAN: But then I saw the cruel truth. I saw that the world is a vale of pee stains and snot rags and bibs full of baby vomit, but that amidst the filth -there were Mabel’s, creatures of glorious imperfection. And that I had already wrecked the perfect, because I had let Mabel go. And that's why I wanted a table tonight! To end this idiocy! To say to this machine I gave you my All (shows a box of All detergent) . . . but the Tide has turned (shows a box of Tide) . . . so goodbye and be of good Cheer. (shows a box of Cheer) But of course, you don't understand! Nobody understands!
```

---

## IC-1417: Story in Harlem Slang from Spunk

- Title: Story in Harlem Slang from Spunk
- Author (byline): Zora Neale Hurston
- Work: [Found in Telling Tales: New One-Act Plays (ed Lane, E)
- Publisher: Penguin Books
- Publication date as stated: Feb 1993
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: SLANG TALK MAN, JELLY, FOOTNOTE VOICE, SWEET BACK, SWEET BACK/JELLY, GIRL, AIR OUT, ASTORPERIOUS, BEATING UP YOUR GUMS, BULL-SKATING, COLLAR A NOD, COAL-SCUTTLE BLONDE, CUT, DIDDY-WAH-DIDDY, DUMB TO THE FACT, FRAIL EEL, GINNY GALL, GRANNY GRUNT, I DON'T DEAL IN COAL, JULY JAM, JUMP SALTY, KITCHEN MECHANIC, MANNY, MISS ANNE, PE-OLA, PIANO, PLAYING THE DOZENS, REEFER, RIGHTEOUS MOSS OR GRASS, RUSSIAN, SCRAP-IRON, SOLID, SUGAR HILL, THE BEAR, THOUSAND ON A PLATE, ZIGABOO, ZOOT SUIT WITH THE REET PLEAT
- Teaser before the introduction: Yes
- Spoken words (computed): 2761
- Already set (do not supply): none

### Source block (context only)

```text
Author: Zora Neale Hurston
Book: [Found in Telling Tales: New One-Act Plays (ed Lane, E)
ISBN: 0140482377
Publisher: Penguin Books
Date(Month/Year): Feb 1993
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
It is suggested that the rhythms of the dialect be played, instead of the dialect itself. A subtle but important distinction: The former will give you Zora. The latter, Amos and Andy. The emotional states of the characters should not be sacrificed for "style." Nor should style be sacrificed because it gets in the way of the emotions. The preferred blend is one in which stylized gesture and speech are fueled by the emotional states.

Lights reveal SLANG TALK MAN: his attire, very debonair; his manner of speaking, very smooth.

SLANG TALK MAN: Wait till I light up my coal-pot and tell you about this Zigaboo called Jelly.

(On Slang Talk Man's signal, lights reveal Jelly, a hick trying to pass himself off as slick. He wears a stocking cap and underneath his "street" bravado is a boyish charm.)

JELLY: Well all right now!

SLANG TALK MAN: He was sealskin brown and papa-tree-top tall.

JELLY: Skinny in the hips and solid built for speed.

SLANG TALK MAN: He was born with this rough-dried hair, but when he laid on the grease and pressed it down overnight with his stocking cap. . .

JELLY: (pulls off the cap to admire his "do": It looked just like righ-teous moss.

SLANG TALK MAN: Had so many waves, you got seasick from lookin'.

JELLY: Solid man solid.

SLANG TALK MAN: His mama named him Marvel, but after a month on Lenox Avenue. . . (On Slang Talk Man's signal, a zoot-suit jacket and hat magically appear.)

SLANG TALK MAN: He changed all that to

JELLY: (getting dressed) Jelly.

SLANG TALK MAN: How come? Well he put it in the street that when it comes to filling that long-felt need. . .

JELLY: Sugar-curing the ladies' feelings. . .

SLANG TALK MAN: He was in a class by himself. And nobody knew his name, so he had to tell 'em.

JELLY: It must be Jelly cause jam don't shake!

SLANG TALK MAN: That was what was on his sign. The stuff was there and it was mellow. N' whenever he was challenged by a hard-head or a frail eel on the right of his title, he would eyeball the idol-breaker with a slice of ice and say

JELLY: Youse just dumb. to the fact, baby. If you don't know what you talking 'bout, you better ask Granny Grunt. I wouldn't mislead you baby. I don't need to. Not with the help I got.

SLANG TALK MAN: Then he would give the pimp's sign. . . (Jelly/Slang Talk Man adopt an exaggerated "street" pose;/or Slang Talk Man it's empty posturing; for Jelly it's the real deal.)

SLANG TALK MAN: And percolate on down the Avenue.(On Slang Talk Man's signal, the Footnote Voice is heard. As the Voice speaks Jelly practices a series of poses.)

FOOTNOTE VOICE: Please note. In Harlemese, pimp has a different meaning than its ordinary definition. The Harlem pimp is a man whose amatory talents are for sale to any woman who will support him, either with a free meal or on a common-law basis; in this sense, he is actually a male prostitute.

"Story in Harlem Slang," defines current Harlem slang by creating a conversation between three Harlem pimps representing various generations: Slang Talk Man, Sweet Back, a fur coat and platform shoe wearing dandy, and Jelly in a full-tilt zoot suit. They're trying to get women to notice them, and the piece plays for pure laughs. Story in Harlem Slang from Spuk by Zora Neale Hurston.

SLANG TALK MAN: So this day he was airing out on the Avenue. It had co be late afternoon, or he would not have been out of bed.

JELLY: Shoot, all you did by rolling out early was to stir your stom-ach up. (Confidentially.) That made you hunt for more dishes codirty. The longer you slept, the less you had to eat.

SLANG TALK MAN: But you can't collar nods all day. So Jelly. . . (Music underscore.)

SLANG TALK MAN: Got into his zoot suit with the reet pleats and got out to skivver around and do himself some good.

(The transformation from "jelly the Hick" into "jelly the Slick" is now complete. He struts and poses like a tiger on the prowl; his moves suggestive, arrogant, mocking. Lights reveal Blues SPeak Woman and Guitar Man, sitting outside the playing arena, scatting vocalise which accents jelly's moves.)

JELLY: No matter how long you stay in bed, and how quiet you keep, sooner or later that big guts is going to reach over and grab that little one and start to gnaw. That's confidential from the Bible. You got to get out on the beat and collar yourself a hot!

SLANG TALK MAN: At 132nd Street, he spied one of his colleagues Sweet Back! Standing on the opposite sidewalk, in front of a café

(Lights reveal Sweet Back, older than jelly; the wear and tear of the street is starting to reveal itself in Sweet Back's face. Nonetheless, he moves with complete finesse as he and Jelly stalk each other, each trying to outdo the other as they strut, pose and lean.)

SLANG TALK MAN: jelly figured that if he bull-skated just right, he might confidence Sweet Back out of a thousand on a plate. Maybe a shot of scrap-iron or a reefer. Therefore, they both cook a quick backward look at the soles of their shoes to see how their leather was holding out. They then stanched out inco the street and made the crossing. (Music underscore ends.)

JELLY: Hey there, Sweet Back. Gimme some skin!

SWEET BACK: Lay the skin on me pal. Ain't seen you since the last time, Jelly. What's cookin'?

JELLY: Oh, just like the bear, I ain't no where. Like the bear's brother, I ain't no further. Like the bear's daughter, ain't got a quarter.

SLANG TALK MAN: Right away he wished he had not been so honest. Sweet Back gave him a

SWEET BACK: Top-superior, cut-eye look.

SLANG TALK MAN: Looked at Jelly just like

SWEET BACK: A showman looks at an ape.

SLANG TALK MAN: Just as far above Jelly as fried chicken is over branch water.

SWEET BACK: Cold in the hand huh? A red hoc pimp like you say you is ain't got no business in the barrel. Last night when I left you, you was beating up your gums and broadcasting about how hot you was. Just as hot as July jam, you told me. What you doin' cold in hand?

JELLY: Aw man, can't you take a joke? I was just beating up my gums when I said I was broke. How can I be broke when I got the best woman in Harlem? If I ask her for a dime, she'll give me a ten-dollar bill. Ask her for a drink of likker, and she'll buy me a whiskey still. If I'm lyin' I'm flyin'!

SWEET BACK: Man, don't hang out that dirty washing in my back yard. Didn't I see you last night with that beat chick, scoffing a hot dog? That chick you had was beat to the heels. Boy, you ain't no good for what you live. And you ain't got nickel one.

(As if to a passing woman.) Hey baby!

SLANG TALK MAN: Jelly

JELLY: Threw back the long skirt of his coat.

SLANG TALK MAN: And rammed his hand into his pants pocket. Sweet Back

SWEET BACK: Made the same gesture. . .

SLANG TALK MAN: Of hauling out nonexistent money.

JELLY: Put your money where your mouth is. Back yo' crap with your money. I bet you five dollars.

SWEET BACK: Oh yeah!

JELLY: Yeah. (jelly/Sweet Back move toward each other, wagging their pants pockets at each other.)

SWEET BACK: (Playfully) Jelly-Jelly-Jelly. I been raised in the church. I don't bet. But I'll doubt you. Five rocks!

JELLY: I thought so. (Loud talking.) I knowed he'd back up when I drawed my roll on him.

SWEET BACK: You ain't drawed no roll on me, Jelly. You ain't drawed nothing bUt your pocket. (With an edge.) You better stop that boogerbooing. Next time I'm liable to make you do it.

SLANG TALK MAN: There was a splinter of regret in Sweet Back's voice. If Jelly really had had some money, he might have staked him to a hot. .

SWEET BACK: Good Southern cornbread with a piano on a platter.

SLANG TALK MAN: Oh well! The right broad would. . . might come.

JELLY: Who boogerbooing? Jig, I don't have to. Talkin' about me with a beat chick scoffing a hot dog? Man you musta not seen me, 'cause last night I was riding 'round in a Yellow Cab, with a yellow gal, drinking yellow likker, and spending yellow money. (To the audience.) Tell 'em 'bout me. You was there. Tell 'em!

SWEET BACK: Git out of my face Jelly! That broad I seen you with wasn't no pe-ola. She was one of them coal-scuttle blondes with hair just as close to her head as ninety-nine to hundred. She looked like she had seventy-five pounds of clear bosom, and she lookted like six months in front and nine months behind. Buy you a whiskey still! That broad couldn't make the down payment on a pair of sox.

JELLY: Naw-naw-naw-now Sweet Back, long as you been knowing me, you ain't never seen me with nothing but pe-olas. I can get any frail eel I wants to. How come I'm up here in New York? Huh-huh-huh? You don't know, do you? Since youse dumb to the fact, I reckon I'll have to make you hep. I had to leave from down south cause Miss Anne used to worry me so bad to go with her. Who me? Man, I don't deal in no coal.

SWEET BACK: Aww man, you trying to show your grandma how to milk ducks. Best you can do is confidence some kitchen-mechanic out of a dime or two. Me, I knocks the pad with them cackbroads up on Sugar Hill and fills 'em full of melody. Man, I'm quick death 'n' easy judgment. You just a home-boy, Jelly. Don't try to follow me.

JELLY: Me follow you! Man, I come on like the Gang Busters and go off like The March of Time. If that ain't so, God is gone co Jersey City and you know He wouldn't be messing 'round a place like that.

SLANG TALK MAN: Looka there! (Sweet Back/jelly scurry and look.)

SLANG TALK MAN: Oh well, the right broad might come along.

JELLY: Know what my woman done? We hauled off and went to church last Sunday. And when they passed 'round the plate for the penny collection, I throwed in a dollar. The man looked at me real hard for that. That made my woman mad, so she called him back and throwed in a tWenty-dollar bill. Told him to take that and go! That's what he got for looking at me 'cause I throwed in a dollar.

SWEET BACK: Jelly. . .
The wind may blow
And the door may slam.
That what you shooting
Ain't worth a damn!

JELLY: Sweet Back you fixing co talk out of place.

SWEET BACK: If you tryin' to jump salty Jelly, that's yo' mammy.

JELLY: Don't play in the family Sweet Back. I don't play the dozens. I done told you.

SLANG TALK MAN: Jelly

JELLY: Slammed his hand in his bosom as if to draw a gun.

SLANG TALK MAN: Sweet Back

SWEET BACK: Did the same. .

JELLY: If you wants to fight, Sweet Back, the favor is in me.

(jelly/Sweet Back begin to circle one another, each waiting on the other to "strike" first.)

SWEET BACK: I was deep-thinking then, Jelly. It's a good thing I ain't shore-tempered. Tain't nothing to you nohow.

JELLY: Oh yeah. Well, come on.

SWEET BACK: No you come on.

SWEET BACK/JELLY: (overlapping): Come on! Come on! Come on! Come on! (They are now in each other's lace, grimacing, snarling, ready to fight, when Sweet Back throws Jelly a look.)

SWEET BACK: You ain't hit me yet. (They both begin to laugh, which grows, until they are falling all over each other: the best of friends.)

SWEET BACK: Don't get too yaller on me Jelly. You liable to get hurt some day.

JELLY: You over-sports your hand yo' ownself. Too blamed astor perious. I just don't pay 'you no mind. Lay the skin on me man.

SLANG TALK MAN: They broke their handshake hurriedly, because both of them looked up the A venue and saw the same thing.

SWEET BACK/JELLY: It was a girl. (Music underscore as lights reveal the girl, busily posing and preening.)

SLANG TALK MAN: And they both remembered that it was Wednesday afternoon. All the domestics off for the afternoon with their pay in their pockets.

SWEET BACK/JELLY: Some of them bound to be hungry for love.

SLANG TALK MAN: That meant. . .

SWEET BACK: Dinner!

JELLY: A shot of scrap-iron!

SWEET BACK: Maybe room rent!

JELLY: A reefer or two!

SLANG TALK MAN: They both. . .

SWEET BACK: Went into the pose.

JELLY: And put on the look. (Loud talking.) Big stars falling.

SLANG TALK MAN: Jelly said out loud when the girl was in hearing distance.

JELLY: It must be just before day!

SWEET BACK: Yeah man. Must be recess in Heaven, pretty angel like that out on the ground.

SLANG TALK MAN: The girl drew abreast of them, reeling and rocking her hips.

(Blues Speak Woman scats as the girl struts, her hips working to the beat of the music. Jelly and Sweet Back swoop in and begin their moves.)

JELLY: I'd walk clear to Diddy-Wah-Diddy to get a chance to speak to a pretty Ii'l ground-angel like that.

SWEET BACK: Aw, man you ain't willing to go very far. Me, I'd go slap to Ginny-Gall, where they eat cow-rump, skin and all.

SLANG TALK MAN: The girl smiled, so Jelly set his hat and took the plunge..

JELLY: Ba-by, what's on de rail for de lizard?

SLANG TALK MAN: The girl halted and braced her hips with her hands. (Music underscore stops.)

GIRL: A Zigaboo down in Georgy, where I come from, asked a woman that one time and the judge told him ninety days.

(Music underscore continues.)

SWEET BACK: Georgy! Where 'bouts in Georgy you from? Delaware?

JELLY: Delaware? My people! My people! Man, how you going to put Delaware in Georgy. You ought to know that's in Maryland.

(Music underscore stops.)

GIRL: Oh, don't try to make out youse no northerner, you! Youse from right down in 'Barn your ownself.

JELLY: Yeah, I'm from there and I aims to stay from there.

GIRL: One of them Russians, eh? Rushed up here to get away from a job of work. (Music underscore continues.)

SLANG TALK MAN: That kind of talk was not leading towards the dinner table.

JELLY: But baby! That shape you got on you! I bet the Coca-Cola company is paying you good money for the patent!

SLANG TALK MAN: The girl smiled with pleasure at this, so Sweet Back jumped in.

SWEET BACK: I know youse somebody swell to know. Youse real people. There's dickty jigs 'round here tdes to smile. You grins like a regular fellow.

SLANG TALK MAN: He gave her his most killing look and let it simmer.

SWEET BACK: S'pose you and me go inside the cafe here and 'grab a hot.

(Music underscore ends.)

GIRL: You got any money?

SLANG TALK MAN: The girl asked and stiffed like a ramrod.

GIRL: Nobody ain't pimping on me. You, dig me?

SWEET BACK/JELLY: Aww now baby!

GIRL: I seen you two mullet-heads before. I was uptown when Joe Brown had you all in the go-long last night. That cop sure hates a pimp. All he needs to see is the pimps' salute and he'll out with his night-stick and ship your head to the red. Beat your head just as flat as a dime. (The girls sounds off like a siren. Sweet Back and Jelly rush to silence her.)

SWEET BACK: Ah-ah-ah, let's us don't talk about the law. Let's talk about us. About you goin' inside with me to holler, "Let one come flopping! One come grunting! Snatch one from the rear!"

GIRL: Naw indeed. You skillets is trying to promote a meal on me. But it'll never happen, brother. You barking up the wrong tree. I wouldn't give you air if you was stopped up in a jug. I'm not putting out a thing. I'm just like the cemetery. I'm not putting out, I'm takin' in. Dig. I'll tell you like the farmer told the. potato-plant you now and dig you later.

(Music underscore.)

SLANG TALK MAN: The girl made a movement to switch off. Sweet Back had not dirtied a plate since the day before. He made a weak but desperate gesture. (just as Sweet Back places his hand on her purse, the girl turns to stare him down. Music underscore ends.)

GIRL: Trying to snatch my pocketbook, eh?

SLANG TALK MAN: Instead of running. . .

GIRL: (grabs Sweet Back's zoot-suit jacket) How much split you want back here? If your feets don't hurry up and take you 'way from here, you'll ride away. I'll spread my lungs all over New York and call the law. (jelly moves in to try and calm her.) Go ahead. Bedbug! Touch me! I'll holler like a pretty white woman! (The girl lets out three "pretty white woman" screams and then struts off. Music underscores her exit.)

SLANG TALK MAN: She turned suddenly and rocked on off, her earring snapping and her heels popping.

SWEET BACK: My people, my people.

SLANG TALK MAN: Jelly made an effort to appear that he had no part in the fiasco.

JELLY: I know you feel chewed.

SWEET BACK: Oh let her go. When I see people without the periodical principles they's supposed to have, I just don't fool with 'em. (Calling out after her.) What I want to steal her old pocketbook with all the money I got? I could buy a beat chick like you and give you away. I got money's mammy and Grandma's change. One of my women, and not the best one I got neither, is buying me ten shag suits at one time. He glanced sidewise at Jelly to see if he was convincing.

JELLY: But Jelly's thoughts were far away. (Music underscore.)

SLANG TALK MAN: He was remembering those full hot meals he had left back in Alabama to seek wealth and splendor in Harlem without working. He had even forgotten to look cocky and rich. (The lights slowly fade)

Glossary for "Story in Harlem Slang"

AIR OUT: leave, flee, stroll

ASTORPERIOUS: haughty, biggity 'BAM, DOWN IN 'BAM: down South

BEATING UP YOUR GUMS: talking to no purpose

BULL-SKATING: bragging

COLLAR A NOD: sleep

COAL-SCUTTLE BLONDE: black woman

CUT: doing something well

DIDDY-WAH-DIDDY: (1) a far place, a measure of distance; (2) another suburb of Hell, built since way before Hell wasn't no bigger than Baltimore. The folks in Hell go there for a big time.

DUMB TO THE FACT: "You don't know what you're talking about."

FRAIL EEL: pretty girl

GINNY GALL: a suburb of Hell, a long way off

GRANNY GRUNT: a mythical character to whom most questions may be referred

I DON'T DEAL IN COAL: "I don't keep company with black women." JIG: Negro, a corrupted shortening of Zigaboo

JELLY: sex

JULY JAM: something very hot

JUMP SALTY: get angry

KITCHEN MECHANIC: a domestic

MANNY: a term of insult; never used in any other way by Negroes

MISS ANNE: a white woman

MY PEOPLE! MY PEOPLE!: sad and satiric expression in the Negro language; sad when a Negro comments on the backwardness of some members of his race; at other times, used for satiric or comic effect.

PE-OLA: a very white Negro girl

PIANO: spareribs (white rib bones suggest piano keys)

PLAYING THE DOZENS: low-rating the ancestors of your opponent

REEFER: a marijuana cigarette, also a drag

RIGHTEOUS MOSS OR GRASS: good hair

RUSSIAN: a southern Negro up North. "Rushed up here," hence a Russian

SCRAP-IRON: cheap liquor

SOLID: perfect

STANCH or STANCH OUT: to begin, commence, step out

SUGAR HILL: northwest sector of Harlem, near Washington Heights; site of the newest apartment houses, mostly occupied by professional people. (The expression has been distorted in the South to mean a Negro red-light district.)

THE BEAR: confession of poverty

THOUSAND ON A PLATE: beans WHAT'S ON DE RAIL FOR THE

LIZARD?: suggestion for moral turpitude

ZIGABOO: a Negro

ZOOT SUIT WITH THE REET PLEAT: Harlem-style suit with padded shoulders, 43-inch trousers at the knee with cuff so small it needs a zipper to get into, high waistline, fancy lapels, bushels of buttons, etc.
```

---

## IC-1418: Strong Arms

- Title: Strong Arms
- Author (byline): Albert Lujan
- Work: Virgins, Guerrillas & Locas
- Publisher: Cleis Press
- Publication date as stated: Oct 1999
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1524
- Already set (do not supply): none

### Source block (context only)

```text
Author: Albert Lujan
Book: Virgins, Guerrillas & Locas
ISBN: 978-1573440875
Publisher: Cleis Press
Date(Month/Year): Oct 1999
```

### Introduction (context only: never use it for content warnings)

```text
Toys have always played an important role in enriching children's lives. They often reflect the culture of the times and are an indicator of historical changes and trends in society. Although today's toys may seem very different from those of years past, the purpose of toys has always been the same: to bring laughter and joy, and to create opportunities for learning and developmental growth. Maybe you can remember the power of the first toy you fell in love with. . . Strong Arms by Albert Lujan.
```

### Performance text (classify this)

```text
At the age of six I declared my love, my desire, my utter need out loud, to the image on the smooth convex surface of my family’s Zenith color television console. From my seat on the tangled shag of the living room I was levitated forward by a force so magnetic that it pulled my tongue from my mouth and my eyes from their sockets, to vibrate only inches from the screen. It pulled the words from my mouth.

“I want you.”

I vowed to sit there, in front of the television, until I saw again the commercial that so transfixed me; a vow that only lasted till 8:30, my bedtime. I swore I would resume my vigil at dawn. I would see it again. See him again. There, I said it. Not out loud, of course, but secretly, with conviction and desire.

Who was he? Why hadn’t I heard mention of him in the schoolyard or park? All night I thrashed these questions around, between dreaming and waking. He was on my mind when I woke up. It seemed I’d imagined him, but my dreams were so detailed that I knew, deep down, he was real.

That next morning, before school and between bites of Alpha-Bits cereal, he appeared to me again, on Channel 2.

“Mom, hurry mira lookit, hurry mira lookit! The one I told you about. Hur-ryyy!” I sprayed milk and bits through my nose across the table as I bolted for the TV. Clearly she didn’t sense the urgency in my screams. By the time she reached the living room, from the kitchen, where she wrapped a beans-and-rice burrito for my lunch, he was gone.

It was too late to pretend that I felt sick in order to spend the day in front of the TV. A successful sick act had to begin the night before or the minute she woke me up. Plan B had me rummaging through the medicine chest before breakfast for something that would have the school nurse calling home to let my mother know she was sending me home for the day. I examined the various pills of ever color and shape. I resisted eating the Hershey-imitation Ex-Lax. I tried that the day Luke and Laura were scheduled to be married on General Hospital. It worked, only I spent the whole day on the toilet and missed it all. I pushed the children’s multi vitamins off to the side and selected the bottle with the baby-blue colored pills in it. The label read “Midol.” I popped the top and poured three into my pocket. After all, I wasn’t suicidal, I was in love.

On the walk to school I ate the pills from my pocket. I tasted the chalky bitterness and gagged. I silently beckoned to Him. I mouth His name. Called it out. Even chanted it. Armstrong. Mr. Stretch Armstrong from Hasbro. Hasbro – where was that magical country? I wondered. Strong arms. Yes, clearly he was very strong. Buff like the Tasmanian Devil but in complete control. Stronger than any Tonka truck I’d ever owned and destroyed. He had powerful arms with shoulders out to there and legs so muscular it was clear he would never be able to cross them like a girl, even if he wanted to. He had a Bob’s Big Boy soft-serve chocolate ice cream flip going on. Sexy, of course, but in a manly way. Painfully blue eyes. He held a sensual half-grin/half-snarl that said, “I’ll be your special friend, but don’t [mess] with me ‘cuz I could still kill you with my hands if I have to.”

Stretch was quite confident too. Proud of his hard-earned physique. All he ever ran around in was a pair of Speedos. Red. They looked like they were painted on. He was the color of Band-Aids. G.I. Joe and that old sissy, Ken, were obviously ashamed of their scrawny bodies. I was quite disappointed in them, considering how hard it was to get their clothes off.

At school I couldn’t concentrate. I felt kind of lightheaded and kept needing to pee. At my desk I misspelled his name over and over again on my H.R. Puffinstuff notebook. If I got him for Christmas I would never mistreat him. If I got him for my birthday I would cuddle him. Rest him on my chest like some mini-manchild. Feed him mini-muscle bars so that he could have the strength to put Ken in a headlock.

At lunchtime, after I threw away my burrito, I stood in line in the cafeteria holding my bile-yellow fiberglass tray loaded with bile-yellow food. The guy in front of me, this gangly third grader, kept reaching around, checking the contents of his book bag with one hand and trying to balance the tray with the other. It was as if he were afraid some bully was gonna steal his math book or something. Or someone. I saw it. From the edge of the book bag flap I saw it protruding like some obscene, pink udder. Like and arm. A strong arm.

Oh my God. Only one day after the commercial aired for the first time. How hard did he have to whine to get him so soon? And he had the nerve to bring Stretch to school with him. Nine months ‘til Christmas, ten ‘til my birthday. It just wasn’t fair.

By the time we reached the milk I was hyperventilating. I was so enraged and jealous that I started gagging. Everyone around me was going “eeiiuu” and moving away. I instantly reacted. I jerked forward, snatched Stretch from the backpack, dropped him onto my tray, pulled my tray to my chest, and spilled creamed-corn and fruit cocktail on myself. Still I held him tight next to my thumping heart and obscured him. I was delirious and a little nauseous. The little punk out a scream.

The Lord works in a mysterious ways, ‘cuz all of a sudden projectile vomit sprayed from my smiling face. I was wild. Kids ran in all direction. Like a far-reaching sprinkler, I caught most of them on their pants legs. Everyone screamed. It was pandemonium. They cleared out a wide-open get-away path and I took it, laughing, gurgling, almost drowning in my barf, clutching the tray to my chest. I was halfway out the cafeteria before I heard the third grader scream, “Hey, puke-boy’s got my doll!”

Doll? Is that all he thought Stretch was? Some toy to stuff into a chest like some old deflated Hoppity-Hop? I thought not. He really didn’t deserve him. I ducked in the teachers’ restroom. The ladies’. Jumped into a stall. “Oh, Stretch,” I murmured. “But they’re coming for us. They’ll want to take you from me.” There was nowhere to hide him. He didn’t fit in my pockets. I tried to stuff him into my pants and that was kinda nice but really obvious. I could hear them outside. They had followed the trail of puke and food. “You’re mine, Stretch, forever. No matter what,” I vowed.

I pulled the packet that contained the napkin, straw, and ‘spork’ that had stuck to my shirt. “Before they take you from me, my love, we must take the blood oath.” Yes, I was a bit melodramatic for six years old. I slashed the back of my hand with the spork, but getting through Stretch’s skin was a little harder. It took a couple of hard jabs with my pencil to finally puncture the tough hide on his arm.

I put my bleeding hand to his face. I held him over my face and squeezed out his pink, gummy insides, which dangled sensuously and thick like melted mozzarella. I put my mouth over his whole arm and sucked it. Like it was my thumb. I sucked his insides into me. It tasted like Ponds cold cream and paste. Tears ran down my face. I sucked until I passed out.

I woke up in the hospital. His nontoxic goop lined my insides and blocked my air passage. A 125-year-old nurse told me that I had turned blue, “…just like a Smurf.” I had to have my stomach pumped.

At the hospital my parents, and some relatives whom I only saw on Easter and Christmas, watched me nervously, praying the rosary over me and pulling my arm with the I.V. in it to make the sign of the cross. They lavished on me welcomed kisses, Spanish comic books I couldn’t figure out, and a Lite-Brite set with a note taped to the top of it that read, “Do not swallow the pegs! They are not JUJU- BEES!” I had a strange feeling that from then on everybody would be watching what I ate very closely.

That night I fell asleep with the soft, colorfully glowing Lite-Brite set clutched to my chest. On it was the first message I wrote. My first love letter: “I ‘heart’ S.A. 4-ever.”
```

---

## IC-1419: Stuart’s Stepmother Could be the Devil

- Title: Stuart’s Stepmother Could be the Devil
- Author (byline): Jay M. Dean
- Work: Speak Out: Performance Pieces for Speech and Forensics (edited by James Doyle)
- Publisher: Lulu.com
- Publication date as stated: March 2013
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: STUART, CAT, STEPMOTHER, MS FAIRWINKLE
- Teaser before the introduction: Yes
- Spoken words (computed): 1185
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jay M. Dean
Book: Speak Out: Performance Pieces for Speech and Forensics (edited by James Doyle)
ISBN: 978-1300800798
Publisher: Lulu.com
Date (Month/Year): March 2013
```

### Introduction (context only: never use it for content warnings)

```text
My Stepmother Could be the Devil by Jay M. Dean
```

### Performance text (classify this)

```text
STUART: (Pg 15-20) Allo. My name is Stuart . . . and I have LOTS of cool stuff. For example, this is my cat Tobias.

CAT: Hissss . . .

STUART: He pretty much hates me.

CAT: Rawr . . .

STUART: And he’s hideous. He used to be ok until I burned all his fur off. I probably shouldn’t have done that. I am what they call a pyromaniac. It’s a disease. But I have a much bigger problem. I have what they like to call “an over-active imagination.” (looks off, poof poof) (Imagination scene to be created by the actor)

STUART: Apparently an overactive imagination is only good in Disneyland. But I digress . . . I like my hideous cat cuz he talks when you squeeze him.

CAT: Rawr . . .

STUART: Sort of . . .

STEPMOTHER: Stuart! Your cat puked on the rug . . . again . . . Get down here and clean it up . . . now!

STUART: That’s my stepmother. She’s evil . . . like in the fairytales.

CAT: Hiss . . .

STUART: My thoughts exactly Tobias . . .You know . . . (petting cat) it’s ok that my cat’s super ugly and sounds like Janet Reno cuz . . . wanna know a secret? He’s magic. (holds out cat)

CAT: Rawr . . .

STUART: looking at cat) Yah magical. He grants wishes! He can grant whatever wish that I wish when I squeeze him and wish something. It’s pretty sweet . . . Oh . . . except it’s only in my brain. Apparently, Tobias is just the primary extension of my over-active imagination manifesting itself physically in my pet cat. (Smiles) Yah. At least that’s what the therapist told my stepmother.

STEPMOTHER: Stuart! Get your grounded little tookis down to breakfast . . . now!

STUART: Coming!

STEPMOTHER: Stop talking like that! You’re not Winston Churchill!

STUART: But . . . STEPMOTHER: No!

STUART: But . . . STEPMOTHER: No!

STUART: Really? STEPMOTHER: Yes.

STUART: NO! She’s the destroyer of all that is good in the world. . . Hey! So, remember when I said I had lots of cool stuff? Yah, that was a lie. All I have in the world is my magic cat, Tobias.

CAT: Hiss . . .

STUART: What did I ever do to you? I have lost all my worldly possessions because that tyrannical overlord . . . you know . . .

STEPMOTHER: Stuart!

STUART: Her . . . the bringer of unmitigated evil . . . has taken it all for no reason. Or it could be because I’m grounded. Whatever. It all started last week with my teacher, Ms. Fairywinkle . . .

MS FAIRWINKLE: Stuart! What is the matter with you?

STUART: I’m a pyromanic . . . MS FAIRWINKLE: No . . .

STUART: It’s a disease.

MS FAIRWINKLE: No! I mean this. Do you know what card I have in my hand?

STUART: The queen of spades? MS FAIRWINKLE: No . . .

STUART: The four of clubs? MS FAIRWINKLE: No!

STUART: Really?

MS FAIRWINKLE: Yes! I mean . . . No! I mean . . . Yes! Never mind. This is your report card. Just look at your grades. Science D, Reading D, Writing F, Math F!

STUART: Well, Ms. Fairywonkle, I guess I need to be spending less time on Science and Reading.

MS FAIRWINKLE: I am going to have the principal sign this and then I’m sending it home to your stepmother.

STUART: That was bad news. When I got home, I had a serious conversation with Tobias: What are we gonna do? I’ve got to get that report card before anyone else sees it.

CAT: Rawr . . .

STUART: What’s that? Sneak into the principal’s office and get it? No way! The principal’s office is heavily guarded. We’ll never get inside. It’s an impossible mission . . . Wait a tick . . . (picks up cat) Tobias, I have a wish. I need you to turn me into Tom Cruise . . . minus all the creepy stuff. (Holds out cat, squeezes him)

CAT: Rawr . . . (Magic transition sound, 270 spin to the right)

(Mission Impossible Theme, putting on stealth vest and sneaking into the principal’s office, opening a file cabinet and pulling out a report card – As he does so, he verbalizes the following objects as if reading signs that appear on each object: Principal’s Office, Tom Cruise, File Cabinet and Report Card.)

STUART: Everything is labeled in this place! (Finished Mission Impossible Theme) And then I stopped. (Removing vest) Stealing is wrong. Plus, couldn’t all this just be a figment of my over-active imagination. (Report card disappears) And I realized – Yes . . . yes it could.

MS FAIRWINKLE: Stuart! Get down off your desk! You are not a monkey and this is not a zoo. . . what the *heck*!

STUART: Sorry Ms. Farfigwinkle.

MS FAIRWINKLE: I don’t know what is causing this wild behavior, but since you can’t seem to get your head out of the clouds, I’m going to have to put in a call to . . . (devil’s voice) Your Stepmother! (evil laugh)

STUART: Noooo! (beat) So, I’m pretty *doomed*, then. I don’t know what to do, so I decide to sleep on it. (falls asleep, alarm sounds immediately, wakes up) I wake up refreshed and . . . still don’t have a plan. As I eat my breakfast, Tobias comes up with a brilliant plan.

CAT: Rawr . . .

STUART: What’s that? Why yes, I suppose we could . . . create a potion to erase the dark one’s memory . . . if my stepmother can’t remember my grades, then I can’t get in trouble for them! Tobias, I have a wish. I need you to turn me into a really amazing scientist . . . like the guy who invented Poptarts. (to the audience) I love Poptarts. (Holds out cat, squeezes him)

CAT: Rawr . . . (Magic transition sound, 360 degree turn with hands in the air like a mad scientist)

STUART: Good. (clears throat) You put two drops in (sounds: drop, drop, poof!) You take two drops out (sounds: slurp, slurp, pop!) You put three cups in (sounds: swoop, plop, swoop, plop, swoop, plop, poof!) and you shake it all about (sounds: squeeze, drop, drop, slurp, plop, poof!) You make yourself a potion just to knock your stepmom out. That’s what it’s all about! (plop, poof!) There, all finished.

STEPMOTHER: Stuart?!? Oh, there you are . . . let’s go. You’re going to be late for school!

STUART: Oh, but you look so parched stepmother. Perhaps you would like a drink? (offers cup)

STEPMOTHER: Why Stuart? Did you make Tang? Why, thank you. I love Tang. (She drinks, gulp gulp) Mmmm. Delicious.

STUART: And then I stopped. Using a potion to erase someone’s memory is wrong. And couldn’t this just be my over-active imagination, and couldn’t that just be regular, potion free Tang? And I realized, yes, yes it could.

STEPMOTHER: Ok, Stuart. School is starting in 15 minutes! You don’t want to be late for school! Let’s go.

STUART: Wait a tick! That’s it!

STEPMOTHER: What’s it?

STUART: Nothing.

STEPMOTHER: Really?

STUART: Yep.

STEPMOTHER: OK! . . . I’ll be waiting in the car . . .

STUART: Tobias, I’ve got one more wish. If I can’t get rid of my report card, I’ll have to think a little bigger . . . Tobias, I wish there was no such thing as school! (Hold out cat, squeezes him)

CAT: Rawr . . . (Magic transition sound, 180-degree spin)

MS FAIRWINKLE: (Facing back) Stuart! Stuart! Come to class!

STUART: (slowly turning, a little crazy) But I can’t Ms. Fairyfarkle! There is no class! School doesn’t exist! The only thing on the lesson plan today is chaos! And everyone is getting an “A”! Ha! Ha!

MS FAIRWINKLE: Stuart! If school doesn’t exist, then where are you right now?

STUART: (Looks around) That is an excellent point, Ms. Fairyfignuten.

MS FAIRWINKLE: (cold, but concerned) Stuart . . . I think you had better go home.

STUART: Okay, Ms. Fairyfart (to the audience) I am in a terrible amount of trouble! (Starts turning, stops) I wonder if my death will be very painful . . . (finishes 360-degree turn)

STEPMOTHER: Stuart . . . what is wrong with you?

STUART: I’m a pyromaniac.

STEPMOTHER: No . . .

STUART: It’s a disease.

STEPMOTHER: No . . . look, I know things have been hard since your father passed away. But you can’t keep disappearing into that imaginary world of yours when we need you here. I want you to know that if I’m strict, it’s just because I want what’s best for you.

STUART: Oh. I have misjudged this situation terribly. Well, I have something to tell you, but you’re not going to like it.

STEPMOTHER: That’s ok; I don’t like most things.

STUART: There is a very bad report card on its way to this house. And . . . it’s mine.

STEPMOTHER: I know.

STUART: What?

STEPMOTHER: Yep.

STUART: How?

STEPMOTHER: Ms. Fairywinkle told me about your poopy grades last week. I was wondering when you would work up the courage to tell me.

STUART: Oh . . . well, since I was so terribly honest . . . is there any way . . .

STEPMOTHER: (laughs) Oh . . . yeah. No. You’re grounded.

STUART: I see (360-degree turn) So that’s how I ended up here, with nothing to do. My over-active imagination got the best of me . . . But I did learn a lesson. . . and when I figure out what it is I’ll let you know. Meanwhile, I’m sure I can find something to pass the time.

(Strikes match)

CAT: (terrified) Rawr . . .
```

---

## IC-1420: Summer Reading is Killing Me

- Title: Summer Reading is Killing Me
- Author (byline): Jon Scieszka
- Work: Not specified
- Publisher: June 2000
- Publication date as stated: Puffin Books
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: JOE, NARRATOR, FRED, SAM, TOGETHER, RED QUEEN, DEVIL, FRANKENSTEIN, THE DEVIL, TEDDY, ANNA
- Teaser before the introduction: Yes
- Spoken words (computed): 1229
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
JOE: (Pg 6-7) This is going to be impossible to explain. But I think I know what happened. My life has not been the same since my uncle Joe gave me THE BOOK (An elderly Uncle Joe hands Joe a very precious book) – a book like no book I’ve ever read before or since. It’s a time-warping book. I know. I know. You’re saying to yourself . . . .

NARRATOR: “What’s with this guy? He probably still believes in the Easter Bunny and the Tooth Fairy.”

JOE: I didn’t really believe it myself. Then Sam and Fred and I opened THE BOOK. We have been chased by a woolly mammoth, turned into mummies and nearly suffocated by one very nasty-smelling giant. (Giant burps a disgustingly foul burp and Joe responds) (Beat) And once we go to another time, the only way to get back to our time is to find THE BOOK in that time . . . So anyway, there we were – sitting in my room the very first day of summer vacation . . . We were trying to be careful. We really were!

FRED: (Pg 8-9) No more classes, no more books. No more teachers’ dirty looks!

SAM: (pointing to a book on the bookshelf) Can we please promise not to open THE BOOK and get sucked into some time-travel trouble like we always do?

FRED: I’m with you. We don’t have to open any books!

SAM: Well, now that you mention books . . . I was thinking we might get an early start on this list.

FRED: Summer reading list? Are you crazy. This is vacation.

SAM: (Reading aloud from the list) Each student must read four books during the summer and fill out the attached study guide for two of them. The list has Hatchet, The Phantom Tollbooth, The Hoboken Chicken Emergency . . .

FRED: (Pg 10-12) (grabs the list from Sam and sticks it in a book from the shelf)

JOE: (stares, aghast at the bookshelf) Forget it you guys! You don’t have to decide!

SAM: What do you mean we don’t have to decide?

JOE: (pointing to the bookshelf) We have about three seconds before this green mist leaking off my bookshelf decides for us! (The boys are engulfed in a green mist)

FRED: How did that happen? I didn’t do nothing.

SAM: Anything. You didn’t do anything except put our summer reading list inside THE BOOK! *****

FRED: (Pg 16) (looking around cautiously) We can’t be in a book. That only happens in movies. There is no way I am going to spend my summer vacation in a book.

SAM: This is very weird, but quite possibly true. What if story characters are real? What if they have a life we just don’t know about.

JOE: (Pg 20-21) Oh no . . We are in huge trouble. If this means what I think it means, all of the characters from every book on the summer reading list are mixed up here. And none of them are in their books where they’re supposed to be. The librarian is going to kill us.

SAM: What if the Red Queen says, “Off with Ramona’s head!?”

JOE: What if the Twits mess up Wayside School?

SAM: What if the Tripods take over the Little House on the Prairie? We have to get everyone back in the right book!

JOE: (Pg 22-23) We have to get back THE BOOK and take the summer reading list out of it before anything happens!

TOGETHER: THE LIBRARY!

JOE: (Pg 25-27) We took off. We passed old houses, an alley, a street lined with shops and in just a few minutes we were at the corner of the park. Just then we heard a wild yelling and the sound of stomping footsteps behind us. (provides sound effects) Dracula was dragging Winnie-the Pooh in a headlock. Mr. Twit was breaking Harold’s purple crayon. Twenty different bad guys from twenty different books were chasing, hauling and pushing all kinds of characters up the steps of a big old brick building.

FRED: (Pg 28) (Reading the sign on the building) Hoboken Public Library!

SAM: The one building in Hoboken that we need to get into is packed with every bad guy from every book ever written! (The boys sneak into the library) (Pg 33) (in a whisper) I see it, but I don’t believe it. That’s Mrs. Twit tying up Marry Poppins and Encyclopedia Brown.

JOE: That’s Frankenstein holding Pippi Longstocking

FRED: They even got Mother Goose.

RED QUEEN: (Pg 34-35) Off with their heads!

CHARACTER FROM LORD OF THE FLIES: Kill the pig! Cut his throat! Bash him in!

JOE: I don’t know what’s going on here, but it doesn’t look good. Let’s sneak up those stairs and start looking for THE BOOK – quick! (they begin up the stairs but are stopped by a commanding voice)

DEVIL: You three boys. What book are you from? Come here now!

FRED: Is that who I think it is?

JOE: Do you know any other red guy with two horns and a pointed tail? (to the Devil) (Pg 38) We’re the Time Warp Trio!

DEVIL: (Looking at his list) I have no Time Warp Trio!

RED QUEEN: (Pg 38) Off with their heads!

SAM: We’re probably not under Time Warp Trio because we’re actually a series . . .

FRANKENSTEIN: (Groaning and making a move toward them) Series . . . bad!

THE DEVIL: (Pg 39-40) (Stroking his beard) Maybe you can make this easier on all of us. What we are doing here is separating the good characters from the bad characters. The bad characters stay here and take over any story they like . . . And the good characters go there . . . to be crushed by those huge stacks of books and wiped out of stories forever! So . . . are you good characters . . . or bad characters?

JOE: (Pg 42-43) Then the door with LIBRARIAN written on the glass slammed open with a bang.

TEDDY: What is going on out here?!

FRED: A . . . . a . . . teddy bear?

TEDDY: (Pg 44) That’s Mr. Bear to you, kid! (The boys try to hold in their laughter) This is exactly what I’m talking about. Just because I’m a teddy bear, I get no respect. Everyone thinks I’m soft and huggable and stupid! What exactly is the holdup here? Why isn’t everyone being crushed?

DEVIL: (Pg 45-50) We were . . .uh . . I was just . . . checking in these three characters.

TEDDY: Characters? Hah! They aren’t characters from a book. These are three kids. In fact, they are just the kind of readers I get no respect from – wise-guy boys! Throw them in the crusher now! (Frankenstein lumbers to do his bidding)

JOE: (Screaming) Now just one minute! Look, Mr. Teddy – I mean Mr. Bear. It is true that we are not the biggest fan of teddy bear books . . . but crushing all of the good characters from every other book is not going to solve anything. (trying to sound very adult and reasonable) Just look how dumb these books sound without their main characters.

SAM: There are giant holes in every story. (he picks up a book and reads) “Run run run as fast as you can. You can’t catch me, I’m the blankety blank?”

JOE: (grabbing another book) The Hoboken Chicken Emergency is just The Emergency

FRED: (picking up a third book) Sylvester and the Magic Pebble is And the Magic Pebble.

TEDDY: Aww, that is so sweet. You are worried about all the poor little books. Well, don’t worry. The new titles of those books will be The Teddy Bear Emergency, Teddy Bear and the Magic Pebble and The Teddy Bear Man! (Raises his arms and laughing a crazy villain laugh at the ceiling) Frankenstein in Wonderland . . . Green Eggs and Dracula.

FRANKENSTEIN AND THE RED QUEEN: (Cheering) Ted-dy! Ted-dy! Ted-dy!

TEDDY: (Pg 58-59) Crush those boys now!

FRED: We’ll never make it to the door. Quick. Up these stairs!

JOE: We charged up the steps two at a time. Captain Ahab, the Devil and a red-golden dragon climbed after us. We reached the top landing, blocked by the stack of books that had been meant to crush us. (To the boys) Get back here and push! (They give a massive shove. Frankenstein and Dracula are buried in the avalanche)

SAM: (Pg 60-61) Nice shot!

TEDDY: You are making me angry!

JOE: We couldn’t hold out for much longer. I looked around for a way to escape. Stairs blocked. Window too high to reach. That’s when I saw our salvation! A thin blue book covered with silver stars and moons. A folded list stuck out of the middle. THE BOOK!

TEDDY: (Pg 62) I will squash you! I will flatten you like the bugs you are! No one ruins my plans. I will be the most famous character in every story!

FRED: Give me some cover . . .

(He does an amazing maneuver, in slow motion. to leap over the bad characters and grab the book; Sam and Joe continue to pelt the characters with books as a distraction) (Fred dramatically opens the book and removes the reading list – holding it aloft as if were Excalibur)

******

(the boys are engulfed in a green mist and land back in Joe’s bedroom, surrounded by books. Fred has THE BOOK in one hand the reading list in the other. They shake themselves and immediately begin thumbing through the books)

JOE: (Pg 67-69) Mary Poppins, Charlotte, Frog and Toad – everybody’s back! (the boys laugh in relief)

ANNA: Ahem! (the boys freeze) Ahem! I don’t really want to know what you are doing. I just wanted to ask you if you have any ribbon I can use for my (She holds her teddy bear aloft) teddy bear . . .

TOGETHER: (Cowering in fear) NOoooooooo!
```

---

## IC-1421: Swindle

- Title: Swindle
- Author (byline): Gordon Korman
- Work: Not specified
- Publisher: Scholastic
- Publication date as stated: March 2008
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: GRIFFIN, BEN, PALOMINO, REPORTER, CAMERA MAN, PITCH, SAVANNAH, LOGAN, NARRATOR, MULRONEY, NEWS REPORTER, POLICE CHIEF
- Teaser before the introduction: Yes
- Spoken words (computed): 1394
- Already set (do not supply): none

### Source block (context only)

```text
Author: Gordon Korman
ISBN: 978-0439903448
Publisher: Scholastic
Date (Month/Year): March 2008
```

### Introduction (context only: never use it for content warnings)

```text
After a mean collector named Swindle cons him out of a most valuable baseball card, Griffin Bing must put together a band of misfits to break into Swindle's compound and recapture the card. There are many things standing in their way -- but Griffin and his team are going to get back what's rightfully his . . . Even if hijinks ensue.

Swindle by Gordon Korman
```

### Performance text (classify this)

```text
GRIFFIN: (Pg 1-3) Sneaking out at night – Helpful Hints: 1. When lying to your parents, maintain eye contact. 2) Ask permission to attend the FAKE SLEEPOVER. 3) Meet at the Old Rockford House at 8:30 pm Friday. 4) Enter through missing plans in boarded-up window, first floor, east side. Bring your sleeping bag. The old Rockford house is a condemned building that will be demolished tomorrow morning. There will be no beds, no running water, no furniture, no lights, no TV!

BEN: We probably shouldn’t have put in the part about no TV . . . . maybe they’re just late.

GRIFFIN: Nine o’clock is late. Ten-thirty is a no-show.

BEN: Come on, Griffin, what difference does it make if two people or two hundred people spend the last night in a condemned building. They’re never even going to know about it. Maybe the other kids were scared.

GRIFFIN: Of what? Dust? The rain? A whole night with no TV?

BEN: This house is supposed to be haunted. You know the rumors.

GRIFFIN: (Pg 6) Oh, come on! There’s no such thing as a haunted house. (a gust of wind blew through the eves and an unearthly moaning sound echoed around them – Griffin reacts with fear) No offense, Ben, but shut up. You’re starting to creep me out. (Griffin clicks on his flashlights and begins to look around) [I’ll explore by myself!] (Pg 12-13) (He begins to wander the empty husk of the Rockford house. A creature lands in his hair (a bat). Full-on terror rocks him. He slaps desperately at his head, and goes down to the floor – the creature disentangles itself and flies off) You’re okay. Maximum gross, minimum danger. (He grabs his flashlight and shines it around, then screams) Some kind of old-fashioned desk!

(By the glow of his flashlight Griffin plays with the many drawers and compartments, but one drawer won’t open – He accidently touches a release switch) (Pg 14-15) A release switch! This must be some kind of hiding place. (He looks inside the drawer) A baseball card! GEORGE HERMAN RUTH . . . (BABE) RUTH. No way! Old baseball cards [are] worth a lot of money! (He races back to where he left Ben and waves the card under his nose) (Pg 20-21) Read it and weep!

BEN: Babe Ruth – wow! Do you think it’s real?

GRIFFIN: (Looking more closely at the card) It’s probably not valuable. I never get that lucky . . . (thinking) There are experts in this kind of thing.

BEN: Palomino’s Emporium?

GRIFFIN: We’ll get an appraisal!

(Ben and Griffin enter Palomino’s Emporium and spy a short stocky man behind the front counter Thick glasses make his eyes appear twice their size.)

GRIFFIN: (Pg 23) Are you Mr. S. Wendell Palomino?

PALOMINO: What can I do for you, young gentlemen?

GRIFFIN: (Pg 24-26) (Pulling out his Babe Ruth card) I’m thinking of selling this. I hear you guarantee the best prices. (Palomino extends a pudgy hand to take the card. As he looks at it his eyes get wider and his busy eyebrows shoot up high. He is obviously excited about the card and Griffin and Ben get excited too) It’s valuable?

PALOMINO: (instantly reigning in his enthusiasm. He snorts in disdain) Well, it would be – if it was real. (He takes out a large magnifying glass and expounds) You see this solid blue border? That was striped in the original. That’s how we know it’s a copy. I’ll give you a hundred bucks for it.

GRIFFIN: (Sighing heavily) A hundred and fifty!

PALOMINO: (chuckling) You drive a hard bargain, sonny boy. Tell you what – one twenty.

GRIFFIN: Sold! (Hands over the card)

PALOMINO: (Palomino counts out his payment. Palomino then turns and makes an elaborate show of opening his safe, putting the card inside and closing the safe again. He turns and is surprised to see the boys still standing at the counter) (Pg 27) Pleasure doing business with you!

GRIFFIN: (Pg 26) If the card isn’t valuable, how come you need to keep it in a safe?

PALOMINO: This isn’t Toys ‘R’ Us, sonny boy. We take security seriously at Palomino’s Emporium. ((Pg 61) Luthor, Palomino’s guard dog Doberman comes out of nowhere, snarling and growling.) (Pg 36) That’s okay, Luthor. ((Pg 27) As Palomino calms the dog, Griffin and Ben slink out of the shop.) ******

(Griffin settles in a home to watch some television. As he clicks through the channels, one station catches his attention – He turns up the sound and watches in shock)

PALOMINO: (pg 32-34) (Holding up the Babe Ruth card for a group of reporters and cameramen) . . . when I bought the collection, I had no idea . . . but the instant I laid eyes on it . . . I mean . . wow!!

REPORTER: There are a lot of similar cards out there. What makes this one so special?

PALOMINO: It was printed in 1920, Ruth’s first season as a Yankee. But look at the picture.

CAMERA MAN: (Zooming in) That’s a Red Sox uniform!

PALOMINO: That’s what makes this card especially valuable.

REPORTER: How much is it worth, Wendell? What are you selling it for?

PALOMINO: [Well] The people at Worthington’s think it could be the second card in history to break the million-dollar barrier.

GRIFFIN: (Pg 39) I’ve been cheated!! *********

(At school the next day, Griffin hatches his plan at recess)

BEN: (Pg 41-42) You want to pull a what?

GRIFFIN: Shhhh! A heist.

BEN: A robbery. That’s stealing!

GRIFFIN: Not stealing. Stealing BACK. There’s a big difference.

BEN: S. Wendell. Never trust anybody whose name sounds like swindle.

GRIFFIN: He’s the ultimate Swindle. And the only way to get that card back is to take it. What do you say? (Pg 44) (He notices a group of kids who were supposed to be at the Rockford House, but didn’t show up) Hey! What about the old Rockford house, huh? Where were you on Friday night? (Pg 45) Pitch?

PITCH: My family was at the indoor rock wall. I completely spaced.

GRIFFIN: Savannah??

SAVANNAH: I couldn’t be there on Friday. Madame Curie was about to litter. (takes a hamster from her bag) My hamster. (rapidly produces more and more hamsters from the bag) It was a boy . . . and another boy . . . and three girls.

GRIFFIN: Logan??

LOGAN: (Haughtily) Well, I didn’t miss it for any dumb reason like that. I have an audition for an acne cream commercial. I had to stay home and rehearse.

PITCH: We’re all sorry, Griffin. We shouldn’t have flaked out on you that way. Our loss.

SAVANNAH: (Pg 121) This is about your stupid baseball card, isn’t it!

GRIFFIN: (Pg 122-124) (in a stage whisper) Before we go any further. I need your word that you can’t tell anybody about this. Ever . . . [It’s] A Babe Ruth card from 1920 – the kind collectors pay big bucks for. Swindle saw a couple of kids, and he took advantage of us because he didn’t think we could do anything about it. We’re going to show him he was wrong! [He] told the news it could go for over a million. Equal shares!

LOGAN: (dreamily) I could afford . . . . acting lessons!

PITCH: I could take my family climbing at Yosemite!

SAVANNAH: Yeah, it’s a lot of money. But that kind of cash doesn’t come easy. You’re talking about a robbery.

GRIFFIN: You’re right. If we all work together, we can pull it off. (Griffin reveals his PLAN) (Pg 136) The Great Baseball Card Heist (Pg 124) We break into Swindle’s house through a skylight on the roof. Pitch, that’s where you come in! Swindle has a guard dog that sleeps in the house. The dog’s no joke, but Savannah can handle him.

LOGAN: (Pg 125-126) Where do I fit into all this? I’m an actor, not a burglar.

GRIFFIN: Swindle lives across the street from the great-grandaddy of all nosy neighbors. We need you to distract him during the operation. We can do this! Now, who’s on board?

PITCH: (Pg 127) Count me it. Somebody’s got to teach this creep a lesson!

LOGAN: Me, too. It’s the ultimate challenge for an actor.

SAVANNAH: (Pg 129) Yeah, right – like I’ve got a choice. I have to go along to protect poor Luthor!

GRIFFIN: (Pg 160) Ben’s going to take the lookout spot in the front bushes. (Ben reacts with his characteristic enthusiasm) (pg 129) It’s a go then! ******

NARRATOR: (Pg 133) The next day, Logan Kellerman started up the walk at 530 Park Avenue, a package under his arm . . .

LOGAN: (doing some theatrical warm-ups as he gets into character. When he’s ready, he approaches the door and rings the bell)

MULRONEY: What can I do for you son?

LOGAN: I live at 530 University, and this parcel was delivered to our house by mistake. Are you (consulting the label on the package) E. Mulroney? ********

GRIFFIN: (Pg 157) (giving the final pep talk to the rest of the heist crew) What we’re dong tonight isn’t about a baseball card. It isn’t even about money. Tonight we show that fairness isn’t something that’s just for adults, and that you can’t get away with dumping on people just because they’re younger than you. Tonight we make our statement! Okay . . . Let’s go! (Pantomime putting on a climbing harness and extending a ladder on the side of the house. They make it to the roof, open the sky light and drop down inside the house) (Pg 168-169) Everybody – remember to keep you gloves on. No fingerprints! (Luthor lets out a long low growl and heads toward the group viciously) Savannah!!

SAVANNAH: Luthor! Sweetie! Good boy – beautiful boy! Oh, I missed you so much!

(Luthor interrupts himself in mid-ounce, landing on his back and wriggling like a puppy, presenting it’s belly to be scratched.)

GRIFFIN: (releasing a huge breath he had been holding) Okay, guys. Split up. We have to find that [card]. (Pg 183) It’s in this house somewhere! (Pantomime a search for the card – until he ultimately finds it and holds it aloft) (Pg 191) This is the greatest moment of my life! (They beat a hasty retreat through the back door of the house, Griffin grabs Ben on the way out)

BEN: (Pg 207) I’ve always had a lot of respect for you, man. But I never dreamed we had a prayer of pulling off what we did tonight!

GRIFFIN: If you’ve got the right plan, that’s all you need! *********

NEWS REPORTER: (Pg 216) In what is being called the most spectacular robbery in history, a 1920 baseball card valued as high as one million dollars was stolen from its owner’s home last night. Police are investigating leads, including the harnesses and an extension ladder found at the scene. *********

GRIFFIN: (Pg 235) (to his posse) Don’t worry. I’ll take all the blame. My plan, my problem. To be honest, I can’t believe the cops haven’t come for me yet.

(Knock at the door, Griffin is handcuffed and taken to the police station.) ********

POLICE CHIEF: (Pg 244-245) (pulling a sheet of paper from the typewriter and placing it on the table in front of Griffin) Sign here at the bottom.

GRIFFIN: (Scared beyond belief) A confession? Worse? What does it say?

POLICE CHIEF: Take it easy. It’s just a statement that you found the baseball card inside the old Rockford house. There’s a 97-year-old lady in Baltimore – the last surviving member of the original Rockford family. The card is really hers. Palomino is out of luck. (Griffin reacts) I hope you know how lucky you are. Mr. Palomino isn’t going to press charges. He wants to avoid an investigation into whether he broke the law when he cheated you. It’s a pretty happy ending all around – probably happier than you deserve.

GRIFFIN: Thanks, Officer. Thanks, a lot!

NARRATOR: (Pg 251) Palomino’s Emporium closed its doors for good The store never recovered from the scandal. S. Wendell moved to California, leaving only his dog Luthor behind. The Doberman spent less than an hour at the pound before being adopted by Savannah Drysdale. It was a match made in heaven.

(Pantomime their reunion)

SAVANNAH: (Pg 169) Luthor! Sweetie! Good boy – good boy! Oh, I missed you so much!

NARRATOR: What everybody knew, but no one was willing to admit, was that the most interesting thing that had ever happened in this sleepy little community was the Great Baseball Card Heist!
```

---

## IC-1422: Tarzan

- Title: Tarzan
- Author (byline): Wayne Rice and Mike Yaconelli
- Work: Greatest Skits on Earth – Volume 1 (Pg 49)
- Publisher: Zondervan
- Publication date as stated: March 1986
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, COLONEL, TARZAN, CHIEF, JIVE, TENDERBELLY
- Teaser before the introduction: Yes
- Spoken words (computed): 1088
- Already set (do not supply): none

### Source block (context only)

```text
Author: Wayne Rice and Mike Yaconelli
Book: Greatest Skits on Earth – Volume 1 (Pg 49)
ISBN: 978-0310351412
Publisher: Zondervan
Date (Month/Year): March 1986
```

### Introduction (context only: never use it for content warnings)

```text
Tarzan by Wayne Rice and Mike Yaconelli
```

### Performance text (classify this)

```text
This skit takes place "in the jungle," of course. As it opens, Tarzan's boy companion, Jive, is tied to a pole, ready to be burned at the stake.

NARRATOR: Darkest Africa! Wild and foreboding! Man-killing beasts stalk their prey in these dark jungles, ready at any moment to spring, tear, and mangle. Wild savages lurk in dense underbrush waiting to ambush unwary travelers. So sit right back and relax, as we present "Tarzan."

COLONEL: (to audience) Hi, there! I'm the villain in tonight's episode! So far, I've burned down the village of the Lumbago Tribe, I've captured Tarzan's little friend Jive, and, worst of all, I've said nasty things to the animals! But, so far, Tarzan hasn't shown up!

TARZAN: (Tarzan enters, swinging on a rope if possible, and yelling.) AHHH ... EEEEE ... AHHH ... EEEEE ... AHHH ... WAAYA!

COLONEL: Oh-Oh! That's Tarzan now! (to Tarzan) Me Colonel Grub! You Tarzan! Tarzan want boy to live? Tarzan listen to me! Me Boss! You Slave! Savvy?

TARZAN: Tell me, Colonel, have you had this speech problem all your life?

COLONEL: Why-Why, you speak as good as me!

TARZAN: Wrong again, Colonel! That's "as well as I." And I happen to speak better than you.

COLONEL: But when did all this happen? What happened to your English?

TARZAN: Well, Jane isn't with me any longer, so I spend my evenings brushing up on my English!

COLONEL: Well, good English or bad English, the situation remains the same! Either you take orders from me or the boy dies!

TARZAN: Big deal! I hardly know the kid! (Chief enters.)

CHIEF: Ungowah! Tarzan in big trouble! Tarzan burn down village of Lumbagos!

TARZAN: I didn't burn down your village!

CHIEF: We put Tarzan in cobra pit. If Tarzan speak truth, cobra will not kill!

TARZAN: Cobra pit? Isn't it enough if I say, "Cross my heart and hope to die?"

COLONEL: What are you afraid of, Tarzan? I've heard that you're the friend of a million jungle animals!

TARZAN: I am! Unfortunately, there are a million and a half in this jungle! Besides, it was probably you who burned this village.

COLONEL: Maybe! But how are you going to prove it?

TARZAN: With my knowledge of the jungle, it would be easy to follow footprints, search for matches and gasoline in your tent, investigate ashes ...

COLONEL: Resorting to evidence, eh? The 'oldest trick in the book! But it won't work among these savages! They believe in the judgment of the cobra! So into the pit!

TARZAN: What are you going to do with the boy?

CHIEF: He stay tied up! Any friend of Tarzan's no friend of ours!

TARZAN: That's unfair! Why not put the kid in with the cobra and tie me up to the tree?

JIVE: Tarzan! How can you talk like that! I've been at your side every waking moment for the past nine years!

TARZAN: Which is precisely why I'm talking like this!

CHIEF: Enough! Into the pit! (Tarzan exits.)

NARRATOR: Once in the pit, our fearless hero gains the friendship of the cobra, once more proving that all jungle animals love Tarzan. (Tarzan enters with snake over shoulder.)

CHIEF: Ancient tribal code say, since Tarzan make friend with cobra, Tarzan must be telling truth!

COLONEL: Hold on, Chief! I wanted Tarzan to help me trap elephants for ivory! But I don't need him! Your tribe can help me instead! Follow my orders and I'll make you rich!

CHIEF: However, modern tribal code say, since you offer us good deal, ancient tribal code don't stand a chance! We follow!

TARZAN: Don't do it, Chief! Don't you see this man's intentions are dubious, insidious, and furtive?!

COLONEL: And my first order as your leader is to kill the loinclothed Noah Webster!

TARZAN: Stop! After years of companionship and understanding, you can't kill me like that! You aren't that savage!

CHIEF: Right! We must repay him for his kindness! Count to five ... then kill!

NARRATOR: Tarzan, realizing that he is doomed, proceeds to bellow out one of his famous earsplitting jungle cries . . . this momentarily deafens those around him, enabling him to flee to freedom among the familiar jungle surroundings. (Tarzan flees.)

COLONEL: Well, Jive! It looks like your friend Tarzan isn't coming back to help you! Any last requests?

JIVE: Yes! Would you please remove my draft card from my pocket before you light the fire? I don't want to get into trouble for burning my draft card.

TARZAN: (Spying on the Colonel) Now to see what Colonel Grub is up to! Holy ant hills! They're going to burn Jive at the stake! If I didn't have laundry to do I'd rescue him! Wait a minute! Jive does my laundry! Darn! Now I've got to save him! (Tarzan unsheathes his knife and enters to confront the Colonel) O.K., Colonel! Drop the gun!

CHIEF: O.K., Tarzan! Drop the knife!

COLONEL: You'll be sorry you came back, Tarzan! O.K., Chief! Run him through!

TARZAN: Wait, Chief! I appeal to you!

CHIEF: Sorry! Tarzan do not appeal to me! Not even in that miniskirt!

TENDERBELLY: (Tenderbelly enters) Wait! Stop! Spare Tarzan's life! Kill me instead!

TARZAN: Tenderbelly! You're the Chief's daughter! Why do you want to save my life!

TENDERBELLY: Because Tarzan teach me how to love, kiss, and make out!

TARZAN: Tenderbelly! Please! Don't say another word!

TENDERBELLY: Tenderbelly's big heart say Tarzan must live!

TARZAN: Yeah ... but Tenderbelly's big mouth say Tarzan must die.

CHIEF: Enough fooling around! We settle this mess with big fight to finish! If Tarzan loses and is killed, then he must be put to death!

TARZAN: Your sentence structure is a trifle redundant, Chief! Grammatically speaking the proper phrasing should be ...

CHIEF: Hold your filthy tongue in front of the maiden! Have you no respect for an innocent girl? The iron tooth will show the truth!

TARZAN: You mean that knife will decide my life?!

COLONEL: Enough dumb rhyme! You're wasting time! (Tenderbelly shoots the Colonel.)

TENDERBELLY: The job is done! I used the gun!

CHIEF: One more poem and I go home!

TARZAN: Tenderbelly! How could you kill him like that?

TENDERBELLY: I knew you couldn't! You too chicken! Besides, after you spare him, he turn around and stab you in back!

CHIEF: Tenderbelly speak the truth! I was blinded by promises of wealth! But now, Colonel Grub is dead, and Tarzan lives! Tarzan do another show next week! And week after that! And summer reruns! Chief no fool! He know which side of bread to butter up! (Chief exits.)

JIVE: (Jive enters, running) Tarzan, I'm free! They set me free!

TARZAN: Well, I can console myself with the knowledge that there will always be other villains willing to kill a kid!

JIVE: What can I do to repay you for saving my life?

TARZAN: Just a simple token of appreciation will be enough! Like a whalebone slingshot!

JIVE: But the nearest whales are millions of miles from here ... in the Arctic!

TARZAN: Dress warmly, kid! As for you, Tenderbelly ... I think we should continue your lessons! (Tarzan and Tenderbelly exit.)

NARRATOR: So as Tarzan and Tenderbelly frolic through the underbrush together, we come to the end of tonight's [today’s] episode of ... TARZAN!
```

---

## IC-1423: Ten Rules You Absolutely Must Not Break if You Want to Survive the School Bus

- Title: Ten Rules You Absolutely Must Not Break if You Want to Survive the School Bus
- Author (byline): John Grandits
- Work: Not specified
- Publisher: Clarion Books
- Publication date as stated: July 2011
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: KYLE, JAMES, BIG KID, BUS DRIVER, RULE SIX, GIRL, RULE NINE, RULE TEN
- Teaser before the introduction: Yes
- Spoken words (computed): 1909
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Grandits
ISBN: 978-0618788224
Publisher: Clarion Books
Date (Month/Year): July 2011
```

### Introduction (context only: never use it for content warnings)

```text
Ten Rules You Absolutely Must Not Break if You Want to Survive the School Bus by John Grandits
```

### Performance text (classify this)

```text
KYLE: It was the first day of school, and my brother James was walking me to the corner where the school bus stopped. I’d never taken the bus before, and to be honest I was a little nervous. But James was a school bus expert and he promised to help me out.

JAMES: Pay attention Kyle. Don’t walk on people’s lawns. They don’t like it when you do that. And don’t get to the bus stop too early! That’s always a mistake. But don’t get there late, either. You’ll get left behind.

KYLE: My stomach turned over. In one of the nature shows I watch on TV, a young Canada goose got left behind when the flock flew south for the winter. I think it froze to death. Too bad James wasn’t taking the bus with me. Last year he rode the bus and Mom walked me to school. Then we moved. Now he gets to walk, and I have to take the bus. James had told me all about riding the bus. He said if you weren’t careful, you could get laughed at or yelled at. You could get pushed around or even pounded. Big kids would steal your lunch and your money and even your football card collection! Sometimes I wondered if he was exaggerating a little. But if even half the stories were true. I was in trouble. (to James) So what am I supposed to do?

JAMES: Just think of what I’d do and try to act like me. And always, always follow my rules.

KYLE: He called them the. . .

KYLE: I was going to follow every one of them. I didn’t want to get pounded. A couple of kids and their parents were already at the bus stop. There was a house with a fenced-in yard on the corner, and inside the yard there was a dog, barking like crazy. I couldn’t see him, but he sounded like an artic wolf that hadn’t eaten all winter. The fence looked old and rotten.

(Dog barking viciously)

JAMES: Better stay back. That dog sounds nuts.

BIG KID: No lie. I heard he ate a first-grader last year.

KYLE: Everyone moved as far away from the fence as possible – even the grownups. But I had bigger things to worry about than some dumb wolf dog. I had to ride the school bus all alone . . . by myself . . . surrounded by kids I didn’t know. Suddenly there it was: the school bus, charging right at me like a giant yellow rhinoceros! At the last second it jerked to a stop. The door swung open. Man, what was that smell? Last year’s barf? James waved and walked away. That’s when the big kid pushed me aside, knocking my backpack to the ground. By the time I’d picked up all my stuff, everyone else was on the bus. I climbed onboard. The driver was nasty-looking.

BUS DRIVER: Hurry up, kid. I don’t have all day, you know.

KYLE: The first row of seats was empty, but I kept going because of . . . RULE ONE: Never sit in the first row. The second row was filled – and the third row, too. There were kids of every size and shape and color on the bus, and everyone one of them was staring at me. I felt like a zebra at a lion party. The fourth row was filled, the fifth, the sixth. Oh no! Every seat was taken except in the last row. But I couldn’t sit there because of . . . RULE TWO: Never sit in the last row. I thought maybe I should go back to the first row and break Rule One. But then I’d have to walk by everybody again. And I’d break . . . RULE THREE: Never, ever make yourself stand out in any way. I’d been very careful to put on ordinary clothes that morning. I hadn’t worn my moose antlers hat or my lucky bowling shirt. Even so, there I was, stopped dead in the middle of the aisle, with everybody staring at me. I walked to the last row and sat down. I had broken Rule Two and probably Rule Three because I didn’t break Rule One. I stared at my shoes. The day was not starting out well. There was a kid sitting in the window seat next to me. I could see legs and feet, jeans and sneakers. Was it a boy or a girl? I didn’t want to be rude, but I was curious. I decided to take a peek – and immediate broke . . . RULE FOUR: Never make eye contact.

BIG KID: What are you looking at, dweeb?

KYLE: It was the big kid from my stop, and he was glaring at me. Up close, he was the size of a grizzly bear. He must have been in the sixth grade, at least! Quickly, I looked away. My brother had told me that eye contact was very dangerous. If you looked at a kid wrong, he might lash out at you, like a cornered animal. All of a sudden, the big kid’s lunch bag fell off the seat! Without thinking about what James would do, I picked it up. That’s when I remembered . . . RULE FIVE: Never touch anyone’s stuff.

BIG KID: (yelling) What are you doing with my lunch!

KYLE: Nothing. (tossing it into his lap) It fell on the floor. I was just trying to help.

BIG KID: Help yourself to my Twinkies, you mean!

KYLE: No, honest. I just picked it up.

BIG KID: Get out of this seat! (growling) You little kids are a pain!

KYLE: James would never have gotten into this mess because he wouldn’t have broken . . .

RULE SIX: Never talk to big kids.

JAMES: Big kids on the bus are bad. Never, ever talk to a big kid unless you’re one yourself!

KYLE: And I wasn’t. So far, the big kid had already yelled at me. Maybe he wasn’t pounding me yet, but he might be planning to pound me later. I go up, crossed the aisle, and sat down. There was a girl in the other half of the seat.

GIRL: Don’t pay any attention to him. I saw the whole thing. You didn’t try to take his lunch.

KYLE: Yeah, but I shouldn’t have touched his stuff. I guess I wasn’t thinking. (to audience) Which only proved that I still wasn’t thinking, because I’d just broken . . . RULE SEVEN: Never talk to girls. James had told me that girls were even worse than big kids. They were as mean as snakes; they never stopped talking, and they hated sports. And if you were nice to them on the bus, they might want to sit with you at lunch. Actually, that part didn’t sound too bad to me. I wouldn’t mind having someone to sit with at lunch. But my brother was the expert. And it was true, the girl hadn’t stopped talking since I’d sat down. But I sort of stopped listening because the barf smell was getting to me and I had to concentrate on not adding to it. Still, I snapped to attention when I heard her say

GIRL: That guy’s not so tough, you know. One time I saw him run away from a squirrel. But he likes to pick on younger kids. He’s a big bully.

KYLE: Oh no! James had especially warned me to obey . . . RULE EIGHT: Never mess with the bully.

JAMES: Every bus has a bully. It could be a big kid or a little one. A boy or a girl. It doesn’t matter. If you make the bully mad, your life will be miserable.

KYLE: I spent the rest of the bus ride imagining the bully beating me up all the way through grade school, high school, and college. Finally, the bus screeched to a stop, and I escaped. I found my classroom, met my teacher, and sat down with the other kids. The rest of the day went OK, and one nice thing actually happened. At recess I was watching a game of kickball, and I saw the talking girl from the school bus. She was captain of one of the teams, and she was really good! Anyway, while she was waiting for her turn to kick, she came over and talked to me. And talked and talked. She told me that she took acting classes on Saturday, and yellow was her favorite color. She knew a lot about chameleons, because she had three of them. I was going to tell her about my ant farm, only she didn’t leave any spaces for me to say anything. Of course, James never would have listened to a girl, but it wasn’t bad. In fact, the chameleon stuff was interesting, and she said I could be on her kickball team tomorrow. Finally, it was time to go home. But I couldn’t find my bus. There were thousands of them. It was a heard of identical yellow rhinos. Which one was mine?

GIRL: (hanging out the bus window) Hey, new kid. Over here.

KYLE: Yes! I’d found the bus – or at least it had found me. I hurried to get one, because of . . .

RULE NINE: Never be the last one on the bus.

BUS DRIVER: (frowning) Sit down, kid. You’re the last one onboard.

KYLE: I could see that my brother was right about this rule. There were no seats left – except in the first row, right next to the big kid bully. (To big kid, weakly as he slides into the seat) Uh, hi. (to audience) I didn’t look him in the eye. Even so, I’d managed to break Rule One, Three, Six. Eight and Nine in about thirty seconds. That must be a new world record. James would never approve, but I was too tired to care.

BIG KID: Man, I hate the ride home on this bus.

KYLE: Yikes! The big kid bully was talking to me! (To big kid, carefully) Really?

BIG KID: Yeah, I always get a bad seat – like this one. (glaring at Kyle as if it were his fault) And I hate where the bus stops.

KYLE: You mean, because of the dog? (big kid grunts) – (to audience) which I took to mean yes. (to big kid) Yeah. What if it got loose? That would be really scary.

BIG KID: (nodding) You’d think the bus driver could stop across the street. But nooooo!

KYLE: Have you asked her?

BIG KID: Are you nuts? There are rules you have to follow when you ride the bus.

KYLE: Tell me about it. (to audience) And I remembered the last one on my brother’s list . . .

RULE TEN: Never, absolutely never, mess with the bus driver.

BIG KID: She’s scarier than the dog on the corner. (smiling evilly) Why don’t you ask her? You’re a little kid. She probably won’t yell at you . . . much.

KYLE: I thought it over. I’d already broken every other ule. I might as well go for ten out of ten. (rising up from his seat, he taps the bus driver on the shoulder) Ms. School Bus Driver Lady?

BUS DRIVER: Yeah? What? Sit down, kid. No talking to the driver.

KYLE: But I wasn’t going to quit now. (to bus driver) There’s a scary dog on the corner by our stop. Could you please drop us off on the other side of the street instead?

BUS DRIVER: Oh, is that all? No sweat, kid. Now sit down.

BIG KID: (impressed) Wow! Good work! (then catches himself and growls) Little kids get away with murder!

KYLE: Maybe that was true, but I still felt brave. I’d broken ever single one of my brother’s rules. Even so, I hadn’t gotten pounded – and I hadn’t even barfed on the bus. I walked on people’s lawns all the way home. James was waiting for me.

JAMES: (jumping up and down) How was the school bus? Where did you sit? Did you get pounded? Who's the bully? Is the driver mean? You didn’t talk to any girls, did you? Was it terrible?

KYLE: It was OK. I think I’ll be all right. And I learned something I never expected to learn.

JAMES: Oh, yeah? What’s that?

KYLE: (grinning) RULE ELEVEN: Never, absolutely never, pay attention to your big brother’s list of Ten Rules You Absolutely Must Not Break if You Want to Survive the School Bus!
```

---

## IC-1424: Theseus

- Title: Theseus
- Author (byline): Barbara McBride-Smith
- Work: Greek Myths Western Style
- Publisher: August House, Inc.
- Publication date as stated: April 2001
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, DADDY, THESEUS, MAMA, THESUES, FRIENDS, FRIEND
- Teaser before the introduction: Yes
- Spoken words (computed): 2194
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

NARRATOR: Theseus is a Greek word that means “forgetful.” OK, so it’s not, but it ought to be. When Theseus was born, his daddy picked him up, turned him around a few times, looked deep into his eyes, and said to the mama,

DADDY: “Hon, this boy’s got a few cogs without a matching ratchet.”

NARRATOR: Now, he could have said a lot of things that would have become self-fulfilling prophecies about Theseus. He could have said:

DADDY: “This boy’s elevator don’t go all the way to the top.”
“He don’t have both oars in the water.”
“He ain’t the sharpest quill on the porcupine.”
“His dipstick don’t reach his oil.”
Or . . . “He must have gotten into the gene pool when the lifeguard wasn’t
looking,”

NARRATOR: He could have said any of those things. But what he said was,

DADDY: “This boy’s got a few cogs without a matching ratchet.”

NARRATOR: And the daddy was right. Then the daddy took a sword and a pair of shoes, buried them in a hole in the back yard, covered them up with a big ol’ rock, and said to his wife. “Hon, when this boy gets big enough to move that rock, and smart enough to know what’s under it, send him around to see me.” And the daddy was outta there!

NARRATOR: The mama did the best she could raising Theseus. But by the time he was a teenager, he was starting to get on his mama’s nerves. That boy couldn’t remember anything she told him. Besides that, when it came to following directions, he was slower than a herd of turtles stampeding through peanut butter. Every day the mama would say, MAMA: “Son, do you remember that hole out there in the back yard?”

THESEUS: “Uh, sure, Mom.”

MAMA: “Well, go out there and see if you can move that rock off it.”

THESEUS: “Sure, Mom.”

NARRATOR: But before he could get all the way out to that rock, he would trip over an anthill and lose track of where he was going. Or he’d get caught up in a game of “Gotcha” with his friends and forget all about what he was supposed to be doing. You see, “Gotcha” was Theseus’s favorite game, and he whiled away many an hour playing it. This is how it works: everybody, except the one who is It, goes out into the woods and hides up in the trees. The one who is It then walks under the trees looking for the ones who are hiding. Suddenly somebody up in a tree jumps down on the one who is It, knocking the one who is It to the ground, sometimes rendering the one who is It unconscious. The one doing the jumping then hollers, “Gotcha!” Theseus loved being It. He was so good at being It, everybody let him be It all the time. He would go walking along under those trees and somebody would jump down on him. But Theseus always heard them before they landed on him. He could hear the leaves rustle. He could hear the air move. So before anybody could lay a hand on him, he would whirl around, knock ‘em about a hundred yards, and holler, “Gotcha back!” Theseus’s mama would see him dragging back in the house a few hours after she’d sent him out, and she’d say,

MAMA: “Are you coming back in here without that rock?”

NARRATOR: Theseus would wrinkle up his brow like he was working on a problem in quantum physics and say,

THESUES: “What rock?”

NARRATOR: One day, the mama got fed up. She grabbed Theseus by the ear and dragged him out to the back yard.

MAMA: “That rock, son. Do you see that rock? Well, move it!”

NARRATOR: Theseus didn’t know how strong he was. He picked up that big ol’ rock with one hand and tossed it aside.

MAMA: “Now, what do you see down there in that hole?”

THESEUS: “Uh, a sword and a pair of shoes.”

MAMA: “Congratulations, Son. You pass with an A.”

NARRATOR: The mama slapped a map into one of his hands and a sack lunch into the other. “Good luck with your daddy” she said. And the mama was outta there!

Theseus’s daddy had taken up residence in a place called Athens, so that’s where Theseus headed. The Athenian Road was a very dangerous road. It was infested with a bunch of ragtag, third-rate burglars and bandits. They hid in the bushes and trees alongside the road. When wayfarers went down that road, carrying suitcases, pushing baby buggies, those creeps would jump down on ‘em, rob and terrorize ‘em, and generally act like hoodlums. Well, when the terrible stories about the road made the front-page news, people were afraid to travel to Athens anymore. But what did Theseus know about current events? Diddly squat! But luckily, this situation was made to order for Theseus’s unique talents. He went merrily down that road, and when those burglars and bandits jumped down on him, he heard the leaves rustle and the air move. He whirled around, knocked ‘em about a hundred yards, and hollered, “Gotcha back!” Those perverts were never seen again, and the Athenian Road became a shining example of early urban renewal.

Well, when word got out in Athens about this big hero who was coming to town, folks turned out to cheer his arrival. Meanwhile, Theseus’s daddy, Aegeus, who was now king of Athens and enjoying the company of a girlfriend named Medea, got very worried. He had no idea that the road hero was his very own son. Medea, who did not have a stellar reputation in family relations, convinced Aegeus that this hero might be elected the new king of Athens and that poor ol’ Aegeus would be left crownless, powerless, and penniless. So she hatched a plot to poison the mysterious hero. When Theseus got to town, Aegeus and Medea greeted him at the city gates and handed him a cup of wine. As Theseus tipped the beverage to his lips, Aegeus recognized the sharp sword and the dusty shoes he had buried so long ago. He realized that this hero was none other than his abandoned son. Aegeus knocked the cup of poison from the boy’s lips and embraced him.

DADDY: “My son, at last I’ve found you!”

NARRATOR: It so happened that these were tough times in Athens. A few years back, Athens had gotten into a scuffle with the island of Crete. The Athenians had lost. So now every nine years, as payment to the King of Crete, Athens was required to send seven young men and seven young women to Crete, where they were fed to a monstrous Minotaur. When Theseus heard of this atrocity, he said,

THESEUS: “Hey! I’ve got a swell idea! I’m a big-time hero. How about if I go along on the boat this time and just kill that . . . uh . . . that . . . Whaddya call that thing? Oh, year, Minotaur! Yep, I’ll just kill that Minotaur. No problem. Well, so long. See you later . . . uh . . . see you later . . . Whaddya call yourself? Dad! Yep, see you later, Dad!”

NARRATOR: The next day, Theseus joined the thirteen other adolescents bound for Crete. The shop was launched under black sails, befitting the occasion. But Theseus promised Aegeus that if the mission was successful, they would return under white sails. Aegeus could look out over the water and know before the ship ever reached shore whether or not his son was alive. When the ship reached Crete, the young Athenians went ashore, led by Theseus. The first person who greeted them was a beautiful island girl who fell in love with Theseus the moment she laid eyes on him. She looked him up, and she looked him down, and she liked what she saw. Then she looked deep into his eyes, and she said to herself, “Mmm, this boy’s got a few cogs without a matching ratchet.” Theseus was her best hope, so the girl tried not to think about the consequences.

Now this girl was no run-of-the-mill citizen of Crete. She was Ariadne, daughter of King Minos and half-sister to the Minotaur. She walked along next to Theseus and explained to him about the labyrinth where her daddy kept the Minotaur. She told him she was certain that he was strong enough to destroy the Minotaur. But, she said, he could never find his way out of that labyrinth without a little help from her. She’d be happy to provide some assistance, explained Ariadne, if he would take her with him as his wife when he left Crete.

THESEUS: “Sure, Mom . . . uh, sure, Dad . . . uh, sure, Ari-something. Sure, take you with me . . . whatever.”

NARRATOR: When they reached the entrance to the labyrinth, Ariadne handed Theseus a golden ball of string. She told him to let that string unwind behind him as he made his way through the maze of passages. Once he killed the Minotaur, all he had to do was follow the string back to her. She said she’d be waiting with her wedding dress and her running shoes. Theseus led his not-so-merry band of thirteen through the door of the labyrinth, unwinding the golden string as he went. The passageway was dark and dank and narrow, twisting and turning back on itself like a snake. When they reached the innermost part of the maze, Theseus felt the movement of air above him. The bull-headed monster jumped from his hiding place on the wall overhead, snorting and spewing phlegm on the intruders. But Theseus, anticipating the attack, stepped aside and whirled around, and before the Minotaur could lay a hoof on anybody, Theseus knocked him about a hundred yards. “Gotcha back!” he yelled. The Minotaur lay dead, deader than a doornail. Theseus sat down on the lifeless body of the monster and pouted.

THESEUS: “Shucks. Now how in the name of Sam Hill are we supposed to get out of this lousy place?”

NARRATOR: His friends looked deep into his eyes and said to themselves, “This boy’s got a few cogs without a matching ratchet.” They could have said a lot of things, but what they did was yell real loud,

FRIENDS: “The string, stupid, the string!”

NARRATOR: Theseus looked down at the ball of string still in his hand.

THESEUS: “Sure. Right. I knew that. I was just checking. Come on. Follow me. I’m getting you people outta here!”

NARRATOR: They picked up Ariadne at the door, ran for the harbor, and sailed away from the island of Crete at full speed. That night they stopped to rest on the island of Naxos. Ariadne unpacked her wedding frock, and she and Theseus were married by the local justice of the peace. It was the shortest honeymoon in history. Before the crack of dawn, Theseus loaded the crew and the bags back onto the ship and set sail for Athens. Not far out of the harbor, one of his shipmates looked back and yelled,

FRIEND: “Ariadne! Theseus, you forgot Ariadne!”

NARRATOR: Sure enough, there she stood, knee deep in the ocean, still in her nightgown, frantically waving her arms.

THESEUS: “Who? Ari-who? Oh, yeah, her. Nice girl. Well, home to Athens. Full-speed ahead!”

NARRATOR: Would you believe it? He forgot about her. Went off and left her and forgot all about her. And that wasn’t even the worst thing that happened that day. As the ship approached Athens, Aegeus was standing on a high, rocky cliff gazing out over the horizon. When he saw the vessel, he began to weep, and he threw himself to his death on the rocks below. You want to guess what color the sails were? That’s right – black. Theseus forgot to change them!

That’s how the rest of Theseus’s life went. One faux pas after another. He messed up so many times, nobody bothered to keep track for posterity anymore.

Once he went down to the underworld, thinking he could rescue a beautiful woman named Persephone. Hades caught him, of course, and punished him by making him sit in the Chair of Forgetfulness. What a hoot! Theseus felt right at home. He sat there looking mellow, forgetting who he was and what he was supposed to be doing. But, you see, that Chair of Forgetfulness was a fiendish device. It not only took away your memory, but it also sealed itself to your rear end like Super Glue. Theseus would still be there if it hadn’t been for his pal Hercules who followed him down there, grabbed hold of him, and ripped him out of that chair, leaving part of Theseus still attached. That’s why, by the way, to this very day Theseus’s descendants are known as “half-ass people.”

How that boy Theseus ever got to be a hero to the Greeks is a complete mystery to me. On the one hand, he screwed up just about everything he touched. On the other hand, he did clean up the Athenian Road, and he did rid the world of the Minotaur, and he did bring those thirteen young people home safe to Athens. So I guess you could say he did the best he could for a boy who had a few cogs without a matching ratchet.
```

---

## IC-1425: Trigger Mortis, Frontier Mortician

- Title: Trigger Mortis, Frontier Mortician
- Author (byline): Wayne Rice and Mike Yaconelli (eds)
- Work: The Greatest Skits on Earth, Pgs 146-151
- Publisher: Zondervan
- Publication date as stated: March 1986
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, SAM, PIE, JOE, ARNIE, TRIG
- Teaser before the introduction: Yes
- Spoken words (computed): 1868
- Already set (do not supply): none

### Source block (context only)

```text
Author: Wayne Rice and Mike Yaconelli (eds)
Book: The Greatest Skits on Earth, Pgs 146-151
ISBN: 978-0310351412
Publisher: Zondervan
Date (Month/Year): March 1986
```

### Introduction (context only: never use it for content warnings)

```text
Trigger Mortis, Frontier Mortician by Wayne Rice and Mike Yaconelli (eds) originally attributed to Warren W Wiersbe
```

### Performance text (classify this)

```text
Originally attributed to Warren W. Wiersbe

NARRATOR: (Pgs 146-151) The makers of Fatrical present Frontier Mortician! Are you skinny and run down? Are you so thin you have to wear skis in the bathroom to keep from going down the drain? When you turn sideways and stick out your tongue do you look like a zipper? When you drink strawberry pop, do you look like a thermometer? Then you need Fatrical—the drink that adds weight to you. Fatrical is not a capsule. It is not a solid. It is not a liquid. It’s a gas that you inhale. Fatrical comes in one delicious gas flavor – mustard. It costs only $4.95 a case and the equipment for inhaling it costs only $5,678. This includes a 5,000-cubic foot tank, 400 feet of hose, three pumps, two filter tips, and a partridge in a pear tree.

NARRATOR: Now for our story. The Adventures of Trigger Mortis, Frontier Mortician. The scene opens in the residence of Sam Alamode, a wealthy rancher and owner of the Bar-B-Q Ranch in Sparerib, Texas. Sam is dying and is talking to his lovely daughter, Piney Alamode, whom he lovingly calls pie.

SAM: Pie, honey, I’m dying again. Go tell Trigger Mortis, the frontier mortician. Have hearse will travel.

PIE: What’s wrong with you, Daddy? What is your ailment?

SAM: I swallowed the thermometer and I’m dying by degrees.

PIE: I’ll go call Trigger Mortis right away.

NARRATOR: Unknown to Sam Alamode, his head foreman, Joe Silver, is hiding outside listening to the conversation. He’s a full-blooded native American-Indian and Sam always calls him his faithful Indian companion Silver. Sam doesn’t hear Joe speak.

JOE: Let old Sam die. I wish he would. Then I can get the ranch and be set for life. He’s always got some fool disease. Last week he swallowed a dynamite cap and his hair came out in bangs. Before that he swallowed a hydrogen bomb and had atomic ache. He’s suffering from flower disease—he’s a blooming idiot. Hey, here comes Pie Alamode’s stupid boyfriend, Arnie. Poor kid. He’s an orphan. Little orphan Arnie. I’ll just sneak away.

ARNIE: I haven’t seen my girlfriend, Pie Alamode, for two weeks. Boy, she has lovely eyes. One is brown and the other two are blue. Last time I was here she rolled her eyes at me and I picked them up and rolled them back. I remember the first time she kissed me. It made chills go up and down my spine. Then I found out her Popsicle was leaking. I’ll knock at the door. (Knocks)

PIE: Who is it?

ARNIE: It’s me, honey. And I call you honey because you have hives.

PIE: Oh, my cookie. I call you cookie because you’re so crummy.

NARRATOR: We interrupt this love scene to bring you a message from Peter Pan Makeup. Use Peter Pan before your pan peters out. This is the makeup used by the stars: Lassie, Gentle Ben, Phyllis Diller. Listen to this letter from Mrs. Mergatroid Fluglehorn from Liverlip, Mississippi: “My face was so wrinkled I had to screw my hat on. Then I used Peter Pan Makeup and I don’t look like an old woman anymore. I look like an old man. I had my wrinkles tightened up and now every time I raise my eyebrows I pull up my socks. I give all the credit to Peter Pan.” Use Peter Pan and you can be beautiful too. Now back to Frontier Mortician—Trigger Mortis, the frontier mortician, is answering his telephone.

TRIG: Oh, it’s you, Miss Pie Alamode. You want me to come to see your father? Well, my hearse has been giving me trouble—I think I blew a casket. I’ve got to quit using embalming fluid in the gas tank—the motor keeps dying. Yes…yes…well, I have to finish my breakfast. I’m eating Shrouded Wheat and Ghost Toasties…Well, I’ll hurry right out. Goodbye. I must be shoveling off.

NARRATOR: Pie Alamode hangs up and goes to meet her lover, little orphan Arnie, in their favorite meeting place, the family graveyard.

PIE: It’s so romantic here in the graveyard. There’s the grave of my Uncle Earnest. Look…there are some maggots making love in dead earnest.

ARNIE: Darling, may I have your hand in marriage?

PIE: My hand? Oh, yes. In fact, you can have my arm too.

ARNIE: Here, I’ll put this ring on your finger.

PIE: Awwww, your face it turning red.

ARNIE: Yeah, and your finger’s turning green. After all, we’ve been going together for twelve years now.

PIE: So what do you want—a pension? Let’s go tell my father.

NARRATOR: This program is brought to you by the Double Insanity Insurance Company. Mothers, do you have children? Then protect them with a double deal policy. We pay $100,00 if your son is killed by a herd of white elephants going east on Thursday. If you lose an arm, we help you look for it. If you get hit in the head, we pay you in one lump sum. We have double indemnity clause too—if you die in an accident, we bury you twice. Now a report from the National Safety Council. It is predicted that 356 people will die in accidents this weekend. So far only 135 have been reported. Some of you aren’t trying. Now back to our story. Joe Silver is plotting to kidnap Pie Alamode and hold her for ransom. He thinks Sam Alamode is dying, but he really isn’t. Trigger Mortis, frontier mortician, is on his way to the ranch.

TRIG: Well, here I am. When you’re at death’s door, I’ll pull you through.

SAM: Good to see you, Trigger. Can you give me a good funeral?

TRIG: I’ll give you a good funeral or your mummy back. Could I interest you in our new layaway plan?

SAM: I’m a sick man, a sick man. The doctor told me to drink some medicine after a hot back, and I could hardly finish drinking the bath.

TRIG: You need some of my Whistler’s Mother medicine. One dose and you’re off your rocker.

SAM: Trigger, I can trust you, can’t I?

TRIG: Of corpse, of corpse. Have I ever let you down?

SAM: I don’t trust my faithful Indian companion, Silver. He has a sneaky look.

TRIG: I happen to know, Sam, that Joe Silver wants to kidnap your daughter and keep her from marrying little orphan Arnie.

SAM: Trigger, we gotta do something. Think of a plan.

NARRATOR: Will Trigger Mortis think of a plan? While he thinks, a word from Honest John Pendergast, the used car dealer. Honest John has bargains in used cars that you can’t afford to miss. Here’s an 1887 Essex—this is a revolutionary car. Washington drove it at Valley Forge. The tires are so beat that you not only knock the pedestrians down, you whip them to death. The car has low lines—in fact, it’s so low it doesn’t have doors. It has manhole covers. This program is also brought to you by Glum, the toothpaste that gives your bad breath the Good Housekeeping seal of approval. Are your teeth like the Ten Commandments—all broken? Do you have a Pullman car mouth? One upper and one lower? Then use Glum. Glum contains eucalyptus oil, flown in from Australia. This eucalyptus oil is the secret of Glum. Millions of users say, “Man, you clipt us.” Be true to your teeth and they will never be false to you. Now back to Frontier Mortician. Sam, Pie, Arnie and Trigger Mortis are trying to figure out how to get rid of Joe Silver.

SAM: I have a splitting headache.

TRIG: Have your eyes ever been checked?

SAM: No, they’ve always been blue. Trigger, why don’t we put Joe in one of your coffins and ship him out of the state?

TRIG: A tisket, a tasket, I’ll put him in a casket. Listen, Sam, I was in love once, so I know what Arnie and Pie are going through.

PIE: You were in love?

TRIG: I was stuck on a girl who worked in the glue factory. She had a schoolgirl complexion— with diplomas under her eyes. Her lips were like petals—bicycle pedals. Those lips, those teeth, that hair, that eye.

ARNIE: Hey, here comes Joe Silver. Get your coffin ready, Trigger.

PIE: Daddy, lie on the bed and act like you’re dead.

NARRATOR: Sam lies on the bed and holds his breath. Trigger takes off his shoes and they all hold their breath. At this breathless moment, we bring you the daily police calls. Calling car 15, calling car 15—happy birthday, car 15, you are now car 16. Car 56, car 56, rush to the Bungling Brother’s Circus. The fat woman has hay fever and is crying so much three midgets are about to drown. Car 23, car 23—return the 10-gallon hat bought for the mayor—he has an 11-gallon head. Car 19, go to the corner of 6th and Main—the Chinese cook has just committed chop sueycide. Now back to the story. Joe Silver enters Sam’s bedroom as the others hide.

JOE: So I finally caught you, you scoundrel. You’ve cut my check so many times I have to endorse it with Mercurochrome. I want to marry your daughter, Sam, and nobody’s gonna stop me. Sure I’m tough—I’ve been sent up the river so many times I get fan mail from the salmon. The last time they caught me I got ten years in jail and two in the electric chair. Even when I was a baby people were pinning things on me. Now I’m gonna get you.

SAM: Get him, Arnie!

JOE: Help! Help! You’re mushing me… (muffled sounds)

TRIG: That takes care of him. Now I have to run for a body. A fellow in town swallowed a quart of shellac and died. He had a lovely finish.

ARNIE: How can we thank you? You’ll come to the wedding, won’t you?

TRIG: Yes, I plan to give you a tombstone for a present, but don’t take it for granite.

SAM: Thanks, Trig. By the way, stop over and we’ll play golf someday.

TRIG: Don’t ever play golf with an undertaker—he’s always on top with the last hole. (Sam and Trig exit.)

ARNIE: Now we’re alone, Pie, my love. Someday you’ll have my name.

PIE: I never did find out, what is your last name, Arnie?

ARNIE: My name is Arnie R. Square.

PIE: What a lovely name I’ll have—Mrs. Pie R. Square.

NARRATOR: And as the sun sinks slowly in the west, we leave the lovers as they plan their future. Tune in tomorrow for a new adventure, brought to you by Bleeties, the cereal for old goats. Bleeties contains 56% iron, 22% copper, 78% steel, 14% bronze and 11% zinc. It doesn’t snap, crack or pop. It lies there and rusts. Bleeties isn’t the breakfast of champions. It’s for people who just want to get into the semifinals. In closing, be sure to visit your local dime store where they’re having a monster sale. Haven’t you always wanted to own your own monster? We have vampires at special prices. They’re excellent for curing tired blood! These are experienced vampires who all work as tellers in blood banks. Now, tune in tomorrow for the first episode of the new store, “I was a Teenage Spinster,” brought to you by the gardener’s magazine, Weeder’s Digest.
```

---

## IC-1426: Twas a Dark and Dreary Night

- Title: Twas a Dark and Dreary Night
- Author (byline): Patrick F. McManus
- Work: The Grasshopper Trap
- Publisher: MacMillan
- Publication date as stated: 1986
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1563
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patrick F. McManus
Book: The Grasshopper Trap
ISBN: 978-0805001112
Publisher: MacMillan
Date (Month/Year): 1986
```

### Introduction (context only: never use it for content warnings)

```text
Twas a Dark and Dreary Night by Patrick F. McManus
```

### Performance text (classify this)

```text
Back during my single-digit ages, I often thought about running away and joining the French Foreign Legion. The uniform was nice, and I liked the idea of riding horses and camels across the desert. Only one thing bothered me. I wondered if the Legionnaires were issued night lights. My love of adventure had its limits. I could easily imagine a battle-hardened Legionnaire sergeant reporting to his company commander, “Looks grim, sir. We’ve run out of food and water and the ammunition’s nearly gone. Worse yet, we’re short on fuel fro the men’s night lights.” With my luck, I’d be the one whose night light ran out of fuel first.

I realized of course that fear of darkness was a serious flaw in my character. Since my character was riddled with flaws anyway, I didn’t worry much about one more. Nevertheless, I didn’t want my friends to find out I was afraid of the dark, and I went to great lengths to keep my secret from them. Take, for instance, the time Ronnie Ditmire came out to our farm to spend the night with me.

Ronnie had no sooner set foot in the house than he came up with the suggestion that he and I sleep out in the backyard. He said he’d had a lot of experience sleeping out in backyards in town, but this was his first opportunity to do so in the country.

“Yeah, well,” I said. “Sure. In the dark, you mean. Sleep out. That would be fun. You don’t mind a lot of black widow spiders crawling all over you, do you Ronnie?”

“You got black widow spiders in your yard?”

Patting my hair back down, I retracted a few premature goosebumps. Unfortunately, my evil sister, the Troll, overheard our conversation and rushed to put in her oar and roil the waters. “What are you telling Ronnie? There are no black widow spiders in our yard, you silly!”

“Ma!” the Troll roared. “Are there any black widow spiders in the yard?”

Mom, ever ready to rush to my defense, stuck her head out of the kitchen. “No, of course not. Where did you ever get a dumb idea like that?”

“I thought there were,” I said smiling weakly at Ronnie.

“Good,” he said. “Then we can sleep out in the yard tonight, after all..”

“I can’t think of any reason why not,” I said. “Unless you happen to beothered by poisonous snakes. Ever seen anybody get snakebit? First they swell up into a great big horrible ball, and then they turn blue and green and yellow and then it starts to get real bad.”

“My dad says there ain’t any poisonous snakes around here,” Ronnie said. “So we don’t have to worry about snakes.”

“I thought we did,” I said.

“OF course not,” the Troll put in. “There aren’t any poisonous snakes around here – not even when it’s dark! (Trollish cackle)

“Ma!” I yelled. “The Troll is bothering us. Tell her to leave us alone!”

“Don’t refer to your sister as the Troll,” my mother said. “Now, Trudy, get out of there and leave the boys alone.”

The Troll backed slowly out of the room, grinning evilly. “Hope you have a good time sleeping out – in – the – dark. The weather report says there’s going to be heavy darkness all night (cackle cackle!)

Just my luck – heavy darkness. And here was Ronnie, pressing ahead with his plan for sleeping out. This was getting out of hand. We were actually getting some old blankets and quilts down out of the attic to make a bed in the yard. What madness! I considered asking Ronnie to take an oath of secrecy and then confessing to him my disgusting fear of darkness. He would probably understand.

“I’ll tell you something weird,” Ronnie said. “I tried to get Fred Phelps to sleep out with me one night, and he said he couldn’t, he was afraid of the dark. A big guy like Fred, you wouldn’t expect him to be yellow-bellied chicken, would ya? He even made me take a secret oath not to tell anybody.”

“Fred’s dumb too.” I said. So much for that idea.

Darkness was already coming down off the mountain, crawling out of the woods, and oozing up from the creek bottom. Down in the swamp, a chorus of frogs welcomed the coming of night. Stupid frogs.

The Troll detected my fear of darkness early on, and used it for her own amusement. Once, walking home with her through the woods, I noticed that the shadows of the trees had lengthened and were not blending together into great patches of – darkness. “It’s getting dark!” I warned. “We’d better run. We don’t want to get caught out here after dark.”

The Troll stopped, turned around, and studied me thoughtfully. “We can’t run,” she said. “If we run, the wolves will attack.”

I looked around, as one is wont to do after such an announcement. “What wolves?”

“The wolves that have been following us,” she said. “Don’t tell me you haven’t seen them!”

Well, now that she mentioned it, I did indeed see the wolves, slipping along through the shadows to the left and right of us.

The Troll clamly studied my reaction. “Why are you twisting yourself all up like that, you silly?”

Apparently she had never before seen anybody wind up the main spring. Sprannnnnngggg! And I was gone. At the time, I knew nothing about the infectious nature of panic. Otherwise I wouldn’t have been so surprised when, upon reaching my top crusing speed, I noticed the Troll passing me on the left and still accelerating, her braids snapping like bullwhips as she cut in front of me. Maybe she thought there actually were wolves following us. More than likely it was simply that panic loves company. For my part, I couldn’t have cared less about a mere pack of wolves. A pack of wolves wasn’t even in the same league as a pack of darkness.

But now here were Ronnie and I, engaged in the insanity of actually spreading quilts and blankets on top of an old hay tarp in preparation for spending the night outdoors. If I even relaxed my feigned enthusiasm for the undertaking – good word that, undertaking – Ronnie would become suspicious. Then both Fred Phelps and I would become outcasts at school next fall, when Ronnie spread the word that we two yellow-bellied chickens were scared of the dark.

Of course, all I need was a tiny little night light. Something the size of a birthday-cake candle would do – a fifteen-foot birthday-cake candle. Any obvious night light, though, would cause Ronnie to put some tough questions to me, like, “What you doing with that flashlight and the big stack of batteries?” Even if I’d had a big stack of batteries, I couldn’t have risked it.

“What say we turn in?” Ronnie asked. “it’s already dark.”

“I noticed,” I said.

I glanced longingly up at our house, the lights of which were being flicked off one by one as my mother made her final rounds. She opened the back door and called out, “I’m going to bed now. You boys all right?”

“Yep,” Ronnie said.

“Yaup,” I said.

Mom went back inside, and minutes later the last light on our side of the house flicked off. Ronnie and I were in TOTAL DARKNESS! Not just the well-defined cube of darkness that filled a bedroom, but a great shapeless ocean of night!

“You ever hear the story about the stranger who got himself hung for claim-jumping, and his ghost still wanders these parts looking for revenge?” Ronnie said.

“Yeah, I heard it.”

“Well, my pa seen that ghost crossing a field right out this way one night. Foggy it was he said, and . . . “

Idea! Why hadn’t I thought of it before! I leaped out of the covers and told Ronnie I’d be right back. “I forgot to brush my teeth,” I said, rushing toward the house. In the bathroom, I jerked the string on the overhead light, waited an appropriate length of time, and then sauntered back outside. Perfect! The light from the bathroom window cast a nice rectangular patch of light right next to my side of the hay tarp.

“You left the bathroom light on,” Ronnie said.

“Dang,” I said. “If that doesn’t beat all! Oh, well, a little light won’t hurt anything.”

Without warning, an ominous shadow suddenly appeared in my patch of light. Wha? I turned and looked up at the bathroom window. No! There, framed in the window stood the Troll! She was in silhouette, so I couldn’t see her face, but I knew she was grinning her evil grin as she stared down in my direction. Slowly her hand reached for the light string. NO! DON’T DO IT! She made several teasing motions with the light string, then – Zap! The light was gone. Faintly, off in the darkness, I could hear the hollow wound of trollish laughter. She would have already locked all the doors to the house. Trolls are nothing if not thorough.

So now there was nothing to do but suffer the night away. For me, the Troll had murdered any hope of sleep. Under my breath I put a curse on her: May a garter snake turn up in your underwear drawer! (And a garter snake would, which show you can’t discount the power of curses) - Trollish cackle . . . .
```

---

## IC-1427: The Two-Wheeled ATV

- Title: The Two-Wheeled ATV
- Author (byline): Patrick F. McManus
- Work: A Fine and Pleasant Misery
- Publisher: Macmillan
- Publication date as stated: (Month/Year): April 1981
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: PATRICK
- Teaser before the introduction: Yes
- Spoken words (computed): 1758
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patrick F. McManus
Book: A Fine and Pleasant Misery
ISBN: 978-0805000320
Publisher: Macmillan
Date: (Month/Year): April 1981
```

### Introduction (context only: never use it for content warnings)

```text
Okay . . . I’ll admit it . . . but only to you! I would never tell this story to any of my friends. See at our age, bicycles aren’t really that cool anymore. Everyone is talking about their first car! But secretly, I still love my bike. (whisper) His name was Thor (gradually gain volume and excitedness) and he was bright red, with that really cool banana seat and the tassels that flew out from the handles. I put a playing card in the back spokes and it sounded sooooo bad! . . . Yeah . . . well, Patrick F. McManus knows what it was like! This is his story of his first bike, aka . . . “The Two-Wheeled ATV.”

.
```

### Performance text (classify this)

```text
PATRICK: My first all-terrain vehicle was a one-wheel drive, and it could take you anywhere you had nerve and guts enough to peddle it.

Most of the other kids around had decent well-mannered bicycles of distinct makes and models. Mine was a balloon-tired monster born out of wedlock half-way between the junkyard and the secondhand store. Some local fiend had built it with his own three hands and sold it to my mother for about the price of a good milk cow.

For two cents or even a used jawbreaker, I would have beaten it to death with a baseball bat, but I needed it for transportation. And transportation, then as now, was the name of the game.

You could walk to some good fishing holes, all right, but when the guys you were with all rode bikes, you had to walk pretty fast.

PATRICK: Perhaps the worst thing about the bike, as I called it within hearing range of my mother, was that you simply could not ride it in a manner that allowed you to retain any sense of dignity let alone savoir-faire. The chief reason for this was that the seat was permanently adjusted for a person about six-foot-four. I was a person about five-foot-four. The proportions of the handlebars suggested strongly that they had been stolen from a tricycle belonging to a four year old midget. The result of this unhappy combination was that wherever I went on the Bike my rear was always about three inches higher than my shoulder blades.

I tried never to go anywhere on the Bike where girls from school might see me, since it was difficult if not impossible in that position to maintain the image I was cultivating among them as a dashing, carefree playboy.

The seat on the Bike was of the kind usually found on European racing bikes. The principle behind the design of this seat is that the rider goes to beat hell the sooner to get off of it. The idea for heel-and-toe walking races was conceived by someone watching the users of these particular seats footing it back home after a race.

To get the proper effect of one of these seats, you might spend a couple hours sitting balanced on the end of a baseball bat - the small end. Put a doily on it for cushioning.

Whatever the other guys thought of my appearance on the Bike, they had respect for me. I was the fastest thing around on two wheels, thanks to that seat.

PATRICK: The Bike had a couple of little tricks it did with its chain that the Marquis de Sade would have envied. One was that it would wait until you had just started down a long, steep, curving hill and then reach up with its chain and wind your pant leg into the sprocket. This move was doubly ingenious, since the chain not only prevented you from putting on the coaster brakes; it also shackled you to a hurtling death-machine. Many was the time that a streamlined kid streaked silently past cars, trucks and motorcycles on grades where a loose roller skate could break the sound barrier.

The Bike's other trick was to throw the chain off when you needed it most. This usually happened when you were trying to outrun one of the timber wolves the neighbors kept for watchdogs. You would be standing up pedaling for all you were worth, leaving a trail of sweat and burned rubber two inches wide on the road behind you. The wolf would be a black snarl coming up fast to your rear. Then the chain would jump its sprocket and drop you with a crunch on the cross bar, the pedals still spinning furiously under your feet. The wolf gnawed on you until you got the chain back on the sprocket or until he got tired and went home.

The standard method for getting off the bike was to spring clear and let it crash. If it got the chance it would grab you by the pant leg at the moment of ejection and drag you along to grim destruction.

The Bike would sometimes go for weeks without the front wheel bouncing off. This was to lure you into a false sense of security. You would be rattling hell-bent for home past the neighbors, and for a split second you would see the front wheel pulling away from you. Then the fork would hit the ground and whip you over the handlebars. Before you had your breath back, the wolf was standing on your belly reading the menu.

I spent half my waking moments repairing the Bike and the other half repairing myself. Until I was old enough to drive, I went around looking like a commercial for Band-Aids. I hated to stop the Bike along the highway long enough to pick up an empty beer bottle for fear people would stop their cars and try to rush me to a doctor. Even on one of its good days, the Bike looked like an accident in which three people had been killed.

Much as I hated the Bike, I have to admit that it was one of the truly great all-terrain vehicles. It could navigate streams, cross fallen logs, smash through brush, follow a mountain trail, and in general do just about anything but climb trees. Several times it did try to climb trees but the damage to both of us was sufficient to make continued efforts in that direction seem impractical and unrewarding.

Our bicycles in those days were the chief mode of transportation for 90 percent of our camping trips. Occasionally even today I see people use bicycles for camping. They will be zipping along the road on ten-speed touring bikes, their ultra-light camping gear a neat little package on the rear fender. When we went camping on our one speed bikes, it looked as if we had a baby elephant on the handlebars and the mother on behind.

Loading a bicycle for a camping trip was not simply a remarkable feat of engineering; it was a blatant defiance of all laws of physics. First of all, there may have been ultra-light camping gear in those days, but we didn't own any of it. Our skillet alone weighed more than one of today's touring bikes, and a bedroll in cold weather, even without the feather bed, was the weight and size of a bail of straw. The tent was a tarp that worked winters as a haystack cover. A good portion of our food was carried in the quart jars our mother had canned it in. Then there were all the axes, hatchets, saws, machetes, and World War II surplus bayonets without which no camping trip was complete. And, of course, I could never leave behind my jungle hammock, the pride of my life, just in case I happened to come across a jungle.

The standard packing procedure was to dump most of your stuff into the center of the tarp, roll the tarp up into a bundle, tie it together with half a mile of rope, and then find nine boys and a man to lift it to the back fender of the Bike. Anything left over was rolled up in the jungle hammock and tied to the diminutive handlebars. The hardware was distributed evenly around the outside of the two massive bundles, just in case you had sudden need for an axe or bayonet.

Then you sprang onto the saddle and pedaled with all the fury you could generate from ninety-eight pounds of bone and muscle. The Bike would howl in rage, the twin humps of camp gear would shudder and sway like a sick camel, and slowly, almost imperceptibly, the whole catastrophe would move out of the yard and wobble off down the road on some incredible journey.

Sometimes during the winter now, when the cold awakens in my bones and flesh the ache of a thousand old injuries, I suddenly will recall in vivid detail the last few terrifying moments of the Bike's existence as a recognizable entity. A ragged gypsy band of us had just begun another trip into the mountains on our camel-humped ATVs. As usual, I was far out in the lead, the hatchet-head bicycle seat urging me on.

There was a hill about three miles from any home called Sand Creek Hill, a name deceptive in its lack of color and description. By rights the hill should have been called Dead Man’s Drop or Say Goodbye Hill. Loggers drove their trucks down it with one foot on the running board and one hand clutching the rosary - even the atheists.

Just as I crested the hill and started my decent, whom should I notice coming up it but one of our neighbor's wolves, apparently returning home after a hard night of killing elk in the mountains. From fifty yards away I could see his face brighten when he caught sight of me hurtling toward him like doom on two wheels. He crouched expectantly, his eyes happily agleam.

The chain, not to be outdone, chose that moment to eat my pant leg half way up to the knee. I expected to be abandoned by the front wheel any second. The washboard road rattled my bones; axes, saws, and bayonets filled the air on all sides; and the great straining mass of the rear pack threatened to collapse on me. With one last great effort, I aimed a quick kick at the wolf, ripped the pant leg free and threw myself into space. I bounced four times to distribute the injuries evenly about my body, and finally, using my nose for a brake, slid to a stop.

The Bike apparently self-destructed shortly after my departure. Probably the front wheel came off, and the two packs took it from there, ripping and tearing, mashing and grinding, until there was nothing left but a streak of assorted rubble stretching off down the hill.

Even the wolf was somewhat shaken by the impact of the crash. He stared at the wreckage in silent awe, almost forgetting my one good leg he held in his slack jaws.

When I was up and around once more, my mother bought me a car, my second ATV. She got it from a local fiend, who had built it with his own three hands, but that's another story.
```

---

## IC-1428: Variations on the Death of Trotsky

- Title: Variations on the Death of Trotsky
- Author (byline): David Ives
- Work: All in the Timing: Fourteen Plays
- Publisher: Vintage Books
- Publication date as stated: Nov 1994
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: TROTSKY, MRS TROTSKY, RAMON
- Teaser before the introduction: Yes
- Spoken words (computed): 1004
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Ives
Book: All in the Timing: Fourteen Plays
ISBN: 978-0679759287
Publisher: Vintage Books
Date (Month/Year): Nov 1994
```

### Introduction (context only: never use it for content warnings)

```text
Lee Harvey Oswald, Nathuram Godse and Sirhan Sirhan comprise the most famous assassins of political figures in the 20th century. Oswald assassinated President Kennedy, Godse murdered Mahatma Gandi and Sirhan Sirhan killed Robert Kennedy, Their murderous acts not only changed history but also guaranteed them everlasting infamy and a kind of immortality. However, some prominent assassins have become forgotten in the mists of time -- one of them was born 100 years ago in Barcelona, Spain. Jaime Ramón Mercader del Río, a Spanish communist and agent for Russia’s notorious intelligence agency, murdered Russian revolutionary Leon Trotsky in Mexico City in 1940 under orders from Joseph Stalin.

Well that’s not funny, you say? I thought you were going to do a humorous piece, you say! Are you in the wrong room, you say?

No worries. This is . . . . . David Ives’ Variations on the Death of Trotsky
```

### Performance text (classify this)

```text
Lights up on TROTSKY sitting at his desk, writing furiously. The handle of a mountain-climber’s axe is sticking out of the back of his head

NOTE: Actress also plays the role of RAMON

VARIATION ONE

TROTSKY: (as he writes) The proletariat is right. The proletariat must always be right. And the revolution of the proletariat against oppression must go on . . . forever! (MRS. TROTSKY enters, holding al large book) And forever and forever . . . !

MRS TROTSKY: Leon, I was just reading the encyclopedia.

TROTSKY: The heading?

MRS TROTSKY: Trotsky, Leon

TROTSKY: Good, It’s about me.

MRS TROTSKY: Listen to this. (Reads) “On August 20th, 1940, a Spanish Communist named Ramon Mercader smashed a mountain-climber’s axe (looks at the axe in Trotsky’s head) into Trotsky’s skull in Coyoacan, a suburb of Mexico City. Trotsky died the next day.”

TROTSKY: What is the year of that encyclopedia?

MRS TROTSKY: (Checks the spine) “Insert this year’s date as the response.”

TROTSKY: Strange . . . but interesting. I am Trotsky. And this is our house in Coyoacan. And we have a Spanish gardener named Ramon --?

MRS TROTSKY: Mercader. Yes….

TROTSKY: Hmmm. . . What is the date today?

MRS TROTSKY: August 21, 1940.

TROTSKY: Then I’m safe! That article says it happened on the twentieth, which means it would have happened yesterday. And I’d be dead today, with . . . (Gingerly feeling the axe in the back of his head) . . . with a mountain-climber’s axe in my skull. (shrugs it off) Will the capitalist press never get things right? (resumes writing)

MRS TROTSKY: But Leon, isn’t that the handle of a mountain-climber’s axe, sticking out of your skull?

TROTSKY: (looks into the mirror) It certainly does look like one . . . and you know, Ramon was in here yesterday, telling me about his mountain-climbing trip. And now that I think of it, he was carrying a mountain-climber’s axe. I can’t remember if he had it when he left the room . . . (considers) Did Ramon report to work today? (he dies, falling face forward onto his desk)

VARIATION TWO

(Trotsky begins to pace)

TROTSKY: This is very bad news. This is serious.

MRS TROTSKY: What is serious, Leon?

TROTSKY: I have a mountain-climber’s axe buried in my skull!

MRS TROTSKY: Smashed, actually. It says Mercader “smashed” the axe into your skull, not “buried” --

TROTSKY: All right, all right. What am I going to do?

MRS TROTSKY: Maybe a hat would cover the handle. You know. One of those cute little Alpine hats, with a point and a feather . . . ? (Sees the look on his face, and stops.)

TROTSKY: The encyclopedia says that I die today? Does it say what time?

MRS TROTSKY: No.

TROTSKY: So much for the usefulness of that encyclopedia. All right, then, I have until midnight at the latest.

MRS TROTSKY: What should I tell Cook about supper?

TROTSKY: Well, she can forget the soup course. (TROTSKY falls to the floor and dies)

MRS TROTSKY: Nyet, nyet, nyet!

VARIATION THREE

TROTSKY: But this man is a gardener. At least he’s been posing as a gardener. Doesn’t that make him a member of the proletariat?

MRS TROTSKY: I’d say so.

TROTSKY: Then what’s he doing smashing a mountain-climber’s axe into my skull?

MRS TROTSKY: I don’t know. Have you been oppressing him?

TROTSKY: Why would Ramon have done this to me?

MRS TROTSKY: Maybe he’s a literalist.

TROTSKY: A what?

MRS TROTSKY: A literalist. Maybe Ramon ran into Manuel yesterday. You now – Manuel? The head gardener? Maybe Ramon asked him, “Will Mr. Trotsky have time to look at the nasturtiums today?” And maybe Manuel said, “I don’t know – axe Mr. Trotsky.” HA HA HA HA HA HA HA !

TROTSKY: Very funny.

MRS TROTSKY: Or maybe he was just hot-to-trotsky.

TROTSKY: Oh, very, very funny.

MRS TROTSKY: Or maybe he just wanted to pick your brain! HOO HOO HEE HEE HAAA HAAA!

TROTSKY: Stop it! Stop it! (He dies)

MRS TROTSKY: HA HA HA HA HA HA HA !

VARIATION FOUR

TROTSKY: Call Ramon in here. You’d better get him quickly. I have a mountain-climber’s axe in my skull.

MRS TROTSKY: Ramon! Come quickly! (RAMON enters with a sombrero, serape, huaraches and a guitar)

TROTSKY: Good morning, Ramon.

RAMON: Good morning, senor (they shake hands)

TROTSKY: Have a seat, please (to audience) You see? We have a very good employer-employee relations here. (to Ramon) Ramon, did you bury this mountain-climber’s axe in my skull?

RAMON: I did not bury it, senor. I smashed it into your skull.

TROTSKY: Excuse me?

RAMON: You see? You can still see the handle. So we cannot say “buried,” we can only say “smashed,” or perhaps “jammed” –

TROTSKY: All right, all right. Buy why did you do this?

RAMON: I think I read about it in an encyclopedia.

TROTSKY: (to audience) The power of the printed word! (to Ramon) But why? Do you realize who I am? Do you realize that you smashed this axe into the skull of a major historical figure? I helped run the Russian Revolution! I fought Stalin! I was a major political theorist! Why did you do this? Was it political disaffection? Anti-counterrevolutionary backlash? Oh, God! What a fool I’ve been! (He dies)

VARIATION FIVE

TROTSKY: Well. All right then. The twenty-first of August 1940. The day I’m going to die. Interesting. And to think that I’ve gone over so many twenty-firsts of August in my life, like a man walking over his own grave. . .

MRS TROTSKY: It’s been wonderful being married to you, Leon. Though it was a burden at times, being married to a major historical figure.

TROTSKY: I’m sorry I was away from home so often, tending the revolution. . . And I’m sorry I couldn’t have been more in touch with my feelings.

MRS TROTSKY: (gentle protest) No . . . please . . . .

TROTSKY: And that I often had such trouble expressing my emotions.

MRS TROTSKY: Oh, I haven’t been everything I should have been.

TROTSKY: Well, it’s a little late for regrets, with a mountain-climber’s axe buried in one’s skull.

MRS TROTSKY: Smashed, actually.

TROTSKY: So it wasn’t old age, or even cancer that I feared for years. It was an axe wielded by a Spanish Communist posing as a gardener. The gardener was false, and yet the garden that he tended was real. How was I to know he was my killer when I passed him every day? How was I to know I’d never get to know about the bomb, or the eighty thousand dead at Hiroshima? Or rock and roll, or Gorbachev, or the state of Israel? How was I supposed to know I’d be erased from the history books of my own land . . . ?

MRS TROTSKY: But reinstated, at least partially, someday.

TROTSKY: What does that entry say? Would you read it again?

MRS TROTSKY: On August 20th, 1940, a Spanish Communist named Ramon Mercader smashed a mountain-climber’s axe into Trotsky’s skull in Coyoacan, a suburb of Mexico City. Trotsky dies the next day.

TROTSKY: It gives you a little hope about the world, doesn’t it? That a man could have a mountain-climber’s axe smashed into his skull, and yet live on for one whole day . . . ? (Trotsky dies)
```

---

## IC-1429: Waffle

- Title: Waffle
- Author (byline): Owen Egerton
- Work: How Best to Avoid Dying
- Publisher: Dalton Publishing
- Publication date as stated: 2007
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: INSPECTOR, HILLARY, STUMPY, DJ
- Teaser before the introduction: Yes
- Spoken words (computed): 1596
- Already set (do not supply): none

### Source block (context only)

```text
Author: Owen Egerton
Book: How Best to Avoid Dying
ISBN: 978-0974070377
Publisher: Dalton Publishing
Date (Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
• NOTE: GREETING COULD USE MORE VERVE. FLOOR AT ENTRANCE STICKY. • NOTE: BLINDS NEED DUSTING. CASA DE WAFFLE HOT SAUCE ECLIPSED BY A.1. SAUCE. SYRUP CONTAINTER NEEDS TOPPING OFF. • NOTE: WAITRESS ‘HILLARY.’ SHIRT STAINED AND UNTUCKED. PANTS RUMPLED.

Waffle by Owen Egerton
```

### Performance text (classify this)

```text
INSPECTOR: (to audience) For thirty-four years I was a Waffle House secret inspector. In fact, I was the top secret inspector. I traveled to every Waffle House in the nation and trained hundreds of others. My unofficial title was Uber- Inspector. That was six months ago, but my eyes still catch it all. The batter crust on the menu, the cracked tile three from the register, the radio playing instead of the juke box. Minor infractions. Incidentals. Nothing I’d report to the main office. Just notes for the manager in my report. I would never meet him. He can never know my face. Secrecy is key. I used to take notes with a pen the size of a toothpick on a notepad the size of a credit card. But I’ve turned in my tiny pen and pad. Still, I can’t help but think what I would have written.

INSPECTOR: (to audience) Hillary is obese. Very obese. The front roll of her belly rests on my table. Her hair is an unnatural red. Heated coil red. It sticks out from her scalp like wires. She is wearing make-up, but she is not wearing it well. It looks as if it has been applied in the dark by a drunk child. I don’t judge people based on physical beauty. But Hillary is unclean and that’s a bad trait for a food server. She also has a problem with mucus. She places a glass of water down and drags her flabby, wet nostrils along her uniform’s sleeve. I’m disgusted, but my face reveals nothing. I am a spy.

HILLARY: Anything to drink?

INSPECTOR: (to audience) Her voice is pleasant enough. Softer than I’d expected. (to Hillary) “I’ll have a decaf coffee, please.” (to audience) Under the table I press start on my stopwatch. The beverage should reach the customer within a minute and a half. Add an extra fifteen seconds if the order is hot cocoa. As in every Waffle House, there are two distinct coffee pots. Black handle for regular. Orange handle for decaffeinated. Hillary grabs the black handle, pours a cup and returns to my table. (to Hillary) “Is that decaf? Because I’m allergic to caffeine and if it’s not decaf my heart will explode and I will die.”

HILLARY: I’m allergic to walnuts.

INSPECTOR: (to audience) My hands twitch.

HILLARY: Anything to eat?

INSPECTOR: (to audience) I order the All Star Special.

HILLARY: (yelling over her shoulder) Stumpy, we need an A-S-S.”

INSPECTOR: (to audience) Stumpy, a short black cook hovering over the grill, raises his hand, which isn’t there. In place of the hand is a spatula duct-taped to the stump. I watch him. He’s fast. He’s good. I relax and sip my coffee. I’m not really allergic to caffeine. Waffle House are magic. Eclectic gatherings. It’s a quarter till four and look at these wanderers who have found each other. The drunk stewing at the counter, the Hispanic couple cooing in booth three, the teenagers daring each other to French kiss spoonfuls of ketchup. This is life. This is America. The All Star Special includes two eggs, one waffle, four strips of bacon, grits, and toast. It should arrive at the table in six to nine minutes. Stumpy prepares a plate in seven minutes and thirty-four seconds. Well done, Stumpy. Hillary brings it to the table – not careless, but clumsy. As she walks the eggs slide into the grits, but she’s trying and she’s smiling. I’ll give her that, she smiles. Runny eggs, soft waffle, shiny bacon. I’m happy. I like Waffle Houses to work. I like to write STELLAR at the top of my report. I like the basics to be covered so a store can go deeper. Moving beyond “Was the water glass refilled?” to “What was the true motivation of the waiter pouring the water?” I enjoy every bit, saving the waffle for last. I’m ready to add the perfect amount of Whipped Spread and syrup and gobble it up while it’s still hot, but when I open up my tub of Whipped Spread I find an unpleasant surprise. NOTE: MELTED SPREAD It’s a tub of yellow liquid, little white globs floating like scum in an overused hotel hot tub. I motion for Hillary, who is staring at the air. She sees me and waddles over.

HILLARY: More coffee?

INSPECTOR: (to Hillary) “Can I have another tub of butter? This one is melted.” (to audience) Notice I call it butter. All part of the disguise. Anyone who knows Waffle House knows the Whipped Spread is about as close to butter as Alabama is to Asia. Personally, I prefer the spread. Perfect for waffles. Hillary is on her way back to my table with a fresh tub when the phone rings. She squeals and hops to the phone. It’s the fastest I’ve seen her move since I arrived.

HILLARY: (on phone) Hello, Waffle House. (nods, then covers the mouth-piece) Stumpy, it’s the radio people again.

STUMPY: Oh, my, Whoop!!!

INSPECTOR: (to Hillary) Radio people?

HILLARY: They’ve been calling us for the past hour. It’s their morning show.

INSPECTOR: It’s four a.m.

HILLARY: They start real early.

INSPECTOR: Is it the station we’re listening to?

HILLARY: Yep, yep, yep.

INSPECTOR: Why didn’t we hear you? (to audience) She looks at me with what I can only presume is some kind of pity.

HILLARY: They pre-record it.

INSPECTOR: (to audience) I nod and return to my waffle. I open my new spread and find it, too, is liquid. (to Hillary) “Excuse me. This is all melted, too.”

HILLARY: (frowning) Yeah, we keep them by the grill. Anything else?

INSPECTOR: (to audience) Hillary is waiting, doodling on her pad. I take a deep breath. (to Hillary) “Yes, please. A hot slice of apple pie and a cold scoop of vanilla ice cream.”

HILLARY: No apple pie, I think we’re out.

INSPECTOR: Can you check?

HILLARY: I did a minute ago. We’re out.

INSPECTOR: Then why did you say you think?

HILLARY: It’s a figure of speech. Like a metaphor.

INSPECTOR: Like a metaphor?

HILLARY: Would you like pecan?

INSPECTOR: I want apple.

HILLARY: No apple. Just pecan.

INSPECTOR: (to audience) I order pecan. She brings it, smiling again, but I no longer find it pleasant. The pecan pie tastes like sticky chalk. Hard to swallow. I chew slowly. I try to calm myself. My doctor says no losing my temper. I’m too old to afford anger.

HILLARY: More coffee? Or another slice of pie?

INSPECTOR: I could kill her. I could pour syrup down her throat until she drowns. The phone rings and Hillary squeals, drops my check and scampers off. I try another bite. Paper and sugar.

HILLARY: (to Stumpy, the phone again pressed to her ear.) They say I should stand on a table. They say they’re watching somewhere outside. They want me to lift my shirt, Stumpy.

STUMPY: You can’t see *that* on the radio.

HILLARY: Stumpy, it’s five thousand dollars.

STUMPY: I don’t know. You could lose –

INSPECTOR: (to audience) But it’s too late. Hillary climbs up on the table of the booth next to mine, unbuttons her shirts and out flop her breasts. Dear God. Pink, strained flesh popping from the sides of tan mesh bra. It’s as if two shaved possums are hammocked and hibernating on her chest. The teenagers gasp, the drunk claps, Stumpy hides his eyes with his one good hand. Hillary giggles, rebuttons her shirt, and bounces back to the phone.

STUMPY: What are they saying?

HILLARY: (phone to her ear) I don’t know. They’re laughing. They hung up. I don’t understand. (puts down the phone.) I think they said something mean. (flustered and embarrassed) I wonder how I get my money?

INSPECTOR: (to audience) My anger is gone. It’s just too sad. I abandon my pecan pie, walk up to the register, and hand Hillary a twenty dollar bill and my check. I avoid looking at her. I avoid thinking about her. I just want to be outside, driving away.

HILLARY: Here’s your change. (no embarrassment or shame)

INSPECTOR: (to audience) It makes everything worse. I’m looking up to tell her to keep the change when I notice, right next to the register, on a plate, under a glass lid – an untouched, genuine, Waffle House apple pie. And there’s Hillary’s chubby fist handing me crumpled bills. (loudly to Hillary) “I take it back, I do not like the Waffle House. I do not enjoy your smells, your grimy menus. I despise your unclean lavatories, your timorous steaks, your powdered hot cocoa. And you (pointing at Hillary) you are not going to win any money, you stupid thing. Thing! So mop the entrance floor, turn down the music and keep the damned spred in the fridge. (to audience) The door dings open. Two men walk in carrying a life-sized pink cow with the words “KLOL Cash Cow” painted on the side.

DJ: (shouting into a wireless microphone) “We’re here to give away some mooooooney!”

HILLARY: (jumping up and down) “Oh my God! Oh my God! Oh my God!”

INSPECTOR: The other man runs through the store high-fiving the customers and staff, stopping just short of Stumpy. It takes both men to hoist Hillary up on the back of the Cash Cow. They hand her a wad of cash and snap some photos. Stumpy turns up the radio and pumps his arms in the air.

DJ: (yells into microphone) “The Waffle House is a rockin’,”

INSPECTOR: Hillary is happy. A goofy, doughy ball of joy. Why can’t I feel happy for her? Why do I find myself wishing the plastic cow would collapse under her weight or that the DJs would snap the money back and laugh at her naiveté? Stumpy is weeping behind the counter. People are cheering and laughing and toasting Hillary with coffee cups and juice glasses.

HILLARY: (chanting) “Thank you, radio people! Thank you, radio people!”

INSPECTOR: I squeeze past the Cash Cow and leave. It is still more night than morning. But the sky is growing paler. I notice the Waffle House sign is glowing above me. NOTE: ‘A’ AND SECOND ‘F’ NEED NEW BULBS. I climb into my car and start the engine. Glancing in my rearview mirror, I can’t see the Cash Cow. It’s below the window, but I see Hillary. She’s galloping, waving an arm above her head like a rodeo star.
```

---

## IC-1430: Wanda Hickey’s Night of Golden Memories

- Title: Wanda Hickey’s Night of Golden Memories
- Author (byline): Jean Shepherd
- Work: Not specified
- Publisher: Broadway Books
- Publication date as stated: Jan 1976
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: REPORTER, SCHWARTZ, ME, AL, MORTY, MOM, WANDA, WAITER
- Teaser before the introduction: Yes
- Spoken words (computed): 1245
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jean Shepherd
ISBN: 978-0385116329
Publisher: Broadway Books
Date (Month/Year): Jan 1976
```

### Introduction (context only: never use it for content warnings)

```text
Or do they? Wanda Hickey’s Night of Golden Memories by Jean Shepherd
```

### Performance text (classify this)

```text
REPORTER: (Pg 299 – 300) Puberty rites in the more primitive tribal societies are almost invariably painful and traumatic experiences . . . A classic example is the Ugga Buggah tribe of lower Micronesia. When an Ugga Buggah reaches puberty, the rites are rigorous for both sexes. Difficult dances are performed and the candidate for adulthood must eat a sickening ritual meal during the postdance banquet. You will also notice that his costume is as uncomfortable as it is decorative . . . Here we see the ritual dance in progress. (An obviously uncomfortably dressed young man dances a crazy ritual dance to heavy drum beats) Of course, we in more sophisticated societies no longer observe these rites . . .

SCHWARTZ: (Pg 301-302) You going to the prom? I read on the bulletin board where it said you wear a summer formal to the prom.

ME: That’s where you wear one of those white coats. Ya gotta rent ‘em. (To audience) (Pg 305-312) The next day, after school, Schwartz and I went downtown to Al’s Swank Formalwear. Rented by the day or hour, free fittings! I could feel excitement rising deep inside me.

AL: OK, boys. Ya wanna make it big at the prom, am I right? Ya come to the right place. (Yelling to the back room) HEY, MORTY! HERE’S [ONE] MORE FOR THAT BASH AT CHERRYWOOD. I’D SAY ONE FAWTY REGULAH.”

MORTY: THE FAWTY AIN’T BEEN CLEANED YET!

AL: BRING IT OUT, AWREADY! This suit just come in from anotha job. Don’t worry about how it looks. We’ll clean it up an’ take it in so’s it’ll fit good.

ME: Al held up the suit invitingly. (slips his arms into the jacket)

AL: Perfect. Couldn’t be bettuh. Take it in a little here . . . An’ doan worry ‘bout the stain; we’ll get it out. Here, try on these pants.

ME: (Putting on the pants) They were rumpled and smelled strongly of some spilled beverage, but they were truly magnificent. The waist came to just a shade below my armpits. (sashaying around)

AL: Perfect. Just right. Put a little tuck in the waist, so. (Grabbing several yards of the seat) And a little in here. You’re [a] high-class customers. Now, I suppose ya wanna go first class right? . . . . Right?

ME: (To audience) With an air of mystery, he bent over, slid open a drawer and placed atop the counter an object that unfocused my eyes with its sheer brilliance.

AL: A genuwine Hollywood paisley cummabund. It’s only a buck extra . . . [And] how do you expect to trip the light fantastic without a pair of black patent-leatha dancin’ pumps?

ME: Dancin’ what?

AL: (Irritably) Shoes, shoes. And we throw in the socks for nuttin’. How ‘bout it?

ME: (To audience) Step by step, in the ancient tradition, the tribal ritual was being acted out. The prom was now two weeks off . . . (Pg 315) Everything was set to go, except for one thing – no girl.

SCHWARTZ: How ya doin’ with Daphne Bigelow?

ME: Oh, that. I haven’t had time to ask her. (To audience) (pg 312) [She] drifted by on gossamer wings, her brilliant smile lighting up the corners of homeroom. (Pg 314) [Then there was only] one week to go. I knew I could never ask Daphne Bigelow to be my date . . .

MOM: (Pg 303) Why not take that nice Wanda Hickey?

ME: Ah, come on, Ma. This is the prom. This is important. You don’t take Wanda Hickey to the prom. (To audience) Wanda Hickey was the only girl who I knew for an absolute fact liked me. She laughed at my jokes and once when we were 12, actually sent me a valentine. (pg 315-319) A feeling of helpless rage settled over me as I [went to water] the lawn.

WANDA: What are you doing?

ME: (Somewhat exasperated) Oh, hi, Wanda. I’m sprinkling the lawn.

WANDA: I’m sure glad school’s almost over. I never thought I’d be a senior.

ME: Yeah. (To audience) Then it happened. I realized there was no sense fighting it. Some guys are born to dance forever with the Daphne Bigelows. Others – well, they do the best they can. (To Wanda) Would you . . . well . . . I mean uh . . . how about . . . going to the prom with me? (To audience) The die was cast. There was no turning back . . . (Pg 326) [Prom] day dawned bright and sunny, as perfect as a day can be. (Pg 328-333) I took two showers. I knew what happened to people who didn’t – disastrous B.O. It would not happen to me. (sniffs armpits) Tonight I would be a truly magnificent specimen of lusty manhood. Laid out on my bed was my beautiful summer formal. (In words and pantomime) Carefully, I undid the pins that festooned my pleated Monte Carlo shirt. I struggled to get [the studs] in place between the concrete slits. It was impossible! Never in my life had I experienced a collar remotely like the one that now clamped its iron grasp around my windpipe. It dug mercilessly into my throat – a mere sample of what was to come. Tie, shoes, cummerbund and snowy coat. And there I stood – Adonis! (Admiring himself in the mirror) (Pg 334-335) When I pulled up before Wanda’s house, she was out on the porch. With stately tread, I moved up the walk; my pants were so tight that if I’d taken one false step, God knows what would have happened. (Sees Wanda and his mouth drops open) This was NOT the old Wanda. For one thing, she didn’t have her glasses on, and her eyes were unnaturally large and liquid. Milky skin and golden hair radiating in the glow of the porch light. In accordance with the tribal custom, we drove off through the soft night. [And] from all over town, other cars, polished and waxed, carried the rest of the junior class to their great trial by fire.

REPORTER: (pg 300) Here we see the ritual dance in progress. (An obviously uncomfortably dressed young man dances a crazy ritual dance which shifts to the standard box step as the Ugga Buggah tribesman morphs into our narrator) (Pg 336-341) 1-2-3 Pause . . . Back and forth, up and down. 1-2-3 Pause . . . By now my dashing concrete collar had removed a wide strip of skin encircling my neck. Wanda was exhaling directly into my face with a heady essence of cough drops and sauerkraut. [She] started to sweat through her taffeta. I felt it running down her back. My own back was already wet and the sweat, which had now saturated my jockey shorts was pouring down my legs. I pulled [her] closer and we swung back into action. .1-2-3 Pause . . . . [Then] all of a sudden, it was over. The band played Good Night, Sweetheart and we were out . . . . SEE YOU AT THE ROOSTER! – The savage tribal rite was nearing its final and most vicious phase.

REPORTER: (Pg 300) The candidate for adulthood must eat a sickening ritual meal during the postdance banquet.

ME: (pg 342-347) A beady-eyed waiter, hair glistening with Vaseline Hair Oil, sidled over and hovered like a vulture. Quickly distributing the famous Red Rooster Deluxe Menu, he smirked and waited for us to impress our dates.

WAITER: Can I bring you anything to drink?

ME: My first impulse was to order my favorite drink, a bottled chocolate concoction called Kayo, the Wonder Drink; but remembering that better things were expected of me on prom night, I said, in my deepest voice, Uh . . . make mine . . . burbon.

WAITER: How will you have it, sir?

ME: Well, in a glass, I guess and make it a triple. (To audience) I had some vague idea that this was a brand or something. I also ordered – for reasons that even today I am unable to explain – lamb chops, yellow turnips, mashed potatoes and gravy, and a side dish of Italian Cole slaw. (Acknowledges the waiter returning with the drink) Swiftly, I brought the bourbon to my lips, intending to down it in a single devil-may-care [shot]. Down it went – a screaming 90-proof rocket searing savagely down my gullet. (Eyes watering, unable to gasp for breath, but trying desperately to appear manly)

WANDA: Isn’t this romantic? Isn’t this the most wonderful night in all our lives?

ME: Urk . . . Urk . . . yeah! In all the excitement of preparation for the prom, I realized that I hadn’t eaten a single thing all day. Maybe [food] would help! (Lowers head and shovels food in quickly) I tried the potatoes and gravy. I wolfed down the Cole slaw. My stomach . . . .

(He’s obviously going to get sick, struggles down the hallway to the bathroom, holding onto the wall – makes it to the rest room and throws up violently into the toilet – after he recovers, he wipes his mouth with the back of his hand)

(To audience) (Pg 348-349) It was the absolute high point of the junior prom.
```

---

## IC-1431: What in God’s Name

- Title: What in God’s Name
- Author (byline): Simon Rich
- Work: Not specified
- Publisher: Reagan Arthur/Back Bay Books
- Publication date as stated: Aug 2013
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: GOD, VINCE, CRAIG, ELIZA, TV ANNOUNCER, BAYNE, NARRATOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1902
- Already set (do not supply): none

### Source block (context only)

```text
Author: Simon Rich
ISBN: 978-0316133746
Publisher: Reagan Arthur/Back Bay Books
Date (Month/Year): Aug 2013
```

### Introduction (context only: never use it for content warnings)

```text
Welcome to Heaven Inc., the grossly mismanaged corporation in the sky. For as long as anyone can remember, the founder and CEO (known in some circles at God) has been phoning it in. And when he does show up at work, it’s not to resolve wars or end famines, but to Google himself and read what humans have been blogging about him. Enter Eliza and her mentor, Craig, two underpaid Angels in the lowly Department of Miracles. Eliza has just been promoted from the Prayer Department for her innovative method of coding prayers into priority levels – Level 7 prayers are printed on red paper and routed immediately to God. Everything was rolling along quite nicely . . . until today! What in God’s Name by Simon Rich
```

### Performance text (classify this)

```text
(Pg 6-7) VINCE: NFL?

GOD: (closing his eyes and massaging his temples . . . . considering) Packers

VINCE: (writing it down) We’ll make it happen. What about NASCAR?

GOD: I like Trevor Bayne and David Reutimann. (then suddenly pointing at Vince) Hey, how are my numbers?

VINCE: (removing a pie graph from his briefcase) Your numbers are fantastic. Eighty-five percent of humans worship you in some way.

GOD: Outstanding. (Smiling proudly at the chart) Any problem demographics?

VINCE: Some college kids have doubts, but we think they’ll come around. It’s just a phase. (Sighing) We’ll keep working on it.

GOD: (Smiling) All right, then. Let’s play golf!!

(Pg 25 – 27) ELIZA: Hey, can you explain dreams again?

CRAIG: Sure. Dreams were invented by Angels to test out their beta programs.

ELIZA: (Embarrassed to be asking another question) I’m sorry . . . what are beta programs again?

CRAIG: Oh, they’re awesome. They’re unreleased pieces of software. In dreams you can try out anything you want. You can break all the rules, consequence free.

ELIZA: Which rules?

CRAIG: Well, a lot of Angels really hate the gravity thing, so you see a bunch of flying programs. What else . . . a lot of teleporting and body morphing and resurrecting the dead.

ELIZA: Don’t those dreams screw humans up?

CRAIG: (Shaking his head) They’re self-erasing. As soon as you wake up, you forget almost everything that happened.

ELIZA: What’s your favorite beta program?

CRAIG: It’d have to be Vision Stuffer. That’s the one that allows you to visit them. You know, to try to reason with them.

ELIZA: Does that ever work?

CRAIG: (laughing) Nah. They usually forget what you told them by morning. And if anything sticks – like an image or a word – the fill in the blanks themselves and write a crazy book about you.

ELIZA: So all of those religions . . .

CRAIG: They’re our fault. Do you have any other questions?

ELIZA: Just one. How does he decide? You know, on who gets in?

CRAIG: I don’t know. I’ve always wanted to ask him. But I’ve never had the guts. (Craig exits) Just then Eliza’s computer started to beep as a line of text flashed nightmarishly on the screen.

(Pg 32 – 41) ELIZA: (reading from the screen) CODE BLACK: Possible tsunami. Potential loss of life. Warn God! (She looks around the empty office, unsure what to do. Finally she sprints toward the elevators) ******

VINCE: You can’t see him right now. He’s busy

ELIZA: But I have a Cod Black. A possible tsunami!

VINCE: You can make an appointment, but there’s a two-month wait

ELIZA: I can’t wait two months!

VINCE: I don’t know what to tell you, honey.

ELIZA: (Frustrated, Eliza bypasses Vince and shoves open the brass door to God’s office) I’m an Angel. And I’m going to talk to God!

GOD: (interrupted in the middle of eating his breakfast, looks up)

ELIZA: (resolutely but with a quivering voice) I’m here to tell you about a Code Black? The computer said I should warn you. (God nods and returns to his breakfast) I’m sorry for interrupting, but it said there was a potential loss of life. (God nods and continues eating) If you’re not too busy, I think you should take a look at the tsunami. It seems like a pretty urgent situation.

GOD: I’m sorry, what? . . . . You’re right. I’ll intervene. (God picks up the remote control and turns on the television) You like racing? This is a big one – Bayne’s going to his second straight win at Daytona.

TV ANNOUNCER: Bayne and Collins are neck and neck! Collins is making a push a big push! He’s three lengths ahead . . . he should win this one easily and . . . Oh no! He’s down! His car has flipped end over end! He’s escaped the wreckage, but he’s on fire . . . wow . . . he really seems to be in a lot of pain. Looks like Trevor Bayne is the winner!

GOD: (laughing)

ELIZA: (cautious, but angry) Sir, when you said you were going to intervene . . . were you talking about the car race or the tsunami?

GOD: What tsunami? (Distracted by the TV) Hey – they’re interviewing Bayne!

BAYNE: (lifting the trophy over his head) I just want to thank God for this victory. I couldn’t have done it without him.

GOD: (Clapping his hands) Did you hear that? Did you hear what he just said?

ELIZA: (Forcing a smile) Yeah. Neat.

GOD: (Turning off the TV) Okay. I’m sorry. Where’s the earthquake?

ELIZA: It’s a tsunami. And I’m not sure where it is – it just said possible. It came in this morning around seven?

GOD: Probably too late to stop it. (Phone rings and God answers) Yeah, three o’clock’s good. Let’s just play nine this time, though. My back’s killing me. (Puts hand over the receiver) Don’t worry about the tsunami. I’ve got everything taken care of!

ELIZA: (nodding wearily, she begins to exit then notices a giant stack of red papers, nearly as tall as she was. It was a pile of prayers – all 7s) *******

CRAIG: You want to God with a code? (clasping his scalp in disbelief) What were you thinking?

ELIZA: (hands shaking, she is so angry) I spent years sorting those prayers. And he didn’t even read them. I mean, honestly, what kind of CEO is he? How incompetent can you get?

CRAIG: Look. I know he isn’t much of a details guy. But you’ve got to give the man a little respect. I mean, this whole company was his idea. None of us would even be here without him. He deserves some credit.

ELIZA: I feel sick . . . (thinking) You know what? I’m going to go back up there! I’m going to tell him to read those prayers. I spent three years sorting them. He doesn’t have to answer them, but the least he can do is read them! ************ (Pg 46- 55) NARRATOR: God new that his obsession with the humans was insane. When he first built the universe, after all, he’d never even intended for it to be populated. He’d constructed the earth for one reason and one reason only: to manufacture xenon gas. But God rapidly grew bored with that side of the business. So one day, for amusement, he’d had his staff invent mankind. God quickly became preoccupied with the tiny creatures. He began to care about their spots and their wars and their songs and their discoveries. They reminded God of himself.

God thought wistfully about the past. In the beginning, the humans were so easy to please. Give them some fruit, some light, and they’d all be singing his praises. These days nobody said thank you. It made him wonder if his best days were behind him; it made him wonder if it was time to retire.

There was probably a way to fix things, to set the world right. But he was too exhausted to figure it out. *************

ELIZA: (bursting back into God’s office) So you’re just going to play golf!

GOD: (holding his golf bag over his arm; confused) Do you . . . want to come?

ELIZA: Those prayers (pointing to the huge stack of papers in the corner) I sorted them. It took me years to isolate those level sevens, and you’ve probably never even looked at them. (God furrowed his brow, trying to figure out what a #7 was) Look, I know running Earth is hard. But if you’re not going to try to fix things, if you’re not going to really devote yourself to it, what’s the point of being here? What’s the point of even coming to work? Why not just quit? (A eerie silence settles over the room, then slowly God smiles and begins nodding)

GOD: You know what? I’ve been thinking the same thing lately. (Puts down golf bag and yells through the office door) If anyone calls, tell them I’m busy. I’ve got work to do. ************

CRAIG: He canceled golf? (shaking his head in shock and admiration) I can’t believe you just went up there and talked to him.

ELIZA: It was a scary morning. I mean, it’s been five hours and my hands are still shaking! But sometimes, if you really want something, you’ve got to take risks. You know what I mean? (Craig’s computer bings with an incoming e-mail)

CRAIG: (checking his messages) Hey, Eliza! Check your e-mail! ********

GOD: (Reading the e-mail that he has composed) Hey gang, After much consideration I’ve decided to resign as CEO of Heaven Inc. It’s been a fun ride, but part of being successful is knowing when to quit. I want to give a special thanks to Eliza Hunter from the Miracles Department, who really put things into perspective for me. Without her persuasive arguments, I might not have come to this decision:

The earth will be destroyed in a month. I haven’t decided how to do it, but it will probably be by fire or by ice. (Demolition Dept: I will make a decision soon, I promise!) The humans of course, will all be killed, so any jobs related to mankind will be eliminated. Don’t worry. Even though your services are no longer needed, you will retain full access to our company’s facilities. You don’t have to turn in your bicycle. Your laundry will still be picked up on alternate Wednesdays. You’ll just have more time to enjoy it all. The planet’s been on a downhill slide for centuries and frankly I think it’s time we cut our losses. Remember: in the grand scheme of our company, the earth and its creatures are not particularly significant.

I’m pleased to announce that next month I will finally fulfill my lifelong dream of opening a restaurant. I’m calling it Sola, and we’re going to specialize in Asian- American fusion. ********

CRAIG: Holy shit! Didn’t I tell you not to go up there? Look what happened – look what you did!

ELIZA: (crying) You’re right. It’s all my fault. I was just trying to help the humans. I ended up killing all of them. What are we going to do now?

CRAIG: It’s going to be okay. Everything’s going to be okay.

ELIZA: You need to talk to him . . . You need to talk to God!

CRAIG: Me? I’m just some Angel. I can’t walk into his office whenever I feel like it?

ELIZA: (gives him a look, since she’s just done that . . . TWICE) Come on. We can’t let him shut down our department! Please. The entire earth is counting on you

CRAIG: Why me?

ELIZA: Because you’re the only Angel good enough to fix this.

CRAIG: (ramping himself up to the prospect) Okay . . . Okay. . . I’ll go talk to him. ************ (Pg 60 – 67) CRAIG: I was thinking . . . maybe you shouldn’t give up on the earth just yet.

GOD: (flicking his wrist dismissively) That project’s a bust. I’m not throwing more good time after bad.

CRAIG: I know things are rough down there. But don’t you think you could make it better?

GOD: Look. I’m gonna level with you. With that whole mankind thing? I bit off way more than I could chew. (motions to the pile of prayers in the corner) You know, I’ve never answered a single human prayer? It’s not that I haven’t tried – I used to spend ten minutes a day on those suckers. I just could never get them to work.

CRAIG: Not even little prayers?

GOD: (Shaking his head) Last year this guy prayed for me to fix his stereo antenna. I tried to help him out – ended up striking him in the face with lightning. Two times – bap bap! He exploded.

CRAIG: You know. I’m pretty good. I bet I could answer some of those prayers for you, if you gave me a chance.

GOD: (Smirking) I doubt it.

CRAIG: I’m serious. In the Miracles Department, we deal with these types of things all the time. Things aren’t as hopeless as you’re making them out to be. I’ll show you some of my miracles. I’ve done hundreds of them. I did two this morning! I helped a guy in Alaska strike oil, I won a girl a stuffed bear at Coney Island .. . .

GOD: How do I know those weren’t just coincidences?

CRAIG: (clenching his fists) What do I have to do to convince you?

GOD: (folding his arms and contemplating) You’ve gotta call your shot! (motioning to the pile of prayers in his inbox) Pick one – any one. It can be the easiest prayer. If you tell me you can solve it – and you do it by next month – I’ll keep the earth open. (God and Craig shake hands and Craig grabs a hand-full of prayers and begins reading aloud)

CRAIG: Dear God: please give my fat boss a heart attack – Joseph Hickey, 38 , Northern Ireland. – Could be tricky. I could build up plaque in the guy’s arteries, but I doubt that would kill him by next month. (discards this prayer) Dear God: Please don’t let my hamster die. Andrea Oran 7, St. Louis

NARRATOR: Craig zoomed in on the little girl’s bedroom. Her hamster lay in the corner of a fetid cage, taking rapid shallow breaths.

CRAIG: (Shaking his head) That hamster’s a gonner.

NARRATOR: [He] shuffled through the remaining prayers, anxiety rapidly mounting. Everyone wanted the impossible: A mega Millions jackpot, a perfect SAT score, a pony. Eventually [he] was down to his last prayer. Craig took a deep breath and unfolded it.

CRAIG: Please let me and Laura be together. – Sam Katz, New York City (with obvious frustration) Love miracles are impossible. I’ve tried them – they never work. You can’t make two humans fall in love with each other. Too many variables. This Laura girl could be married, for all we know. Just because you love someone doesn’t mean they’ll love you back. Hey – why is this one two pages (turning to page 2 of the prayer request) Please let me and Sam be together – Laura – New York. (Suddenly grinning and confident) Want to know something? That could work!!

CLOSING Will Sam and Laura get together? Will Craig and Eliza be able to save the world? Call it divine intervention, call it Karma, heck, call it Bob for all I care . . . . for now the earth is safe!
```

---

## IC-1432: What’s the Worst That Could Happen?

- Title: What’s the Worst That Could Happen?
- Author (byline): Bruce Coville
- Work: Oddest of All
- Publisher: Harcourt Children's Books
- Publication date as stated: Sept 2008
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: MURPHY, MIKEY, TIFFANY, MRS. WHITCOMB, VOICE
- Teaser before the introduction: Yes
- Spoken words (computed): 1519
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bruce Coville
Book: Oddest of All
ISBN: 978-0152058081
Publisher: Harcourt Children's Books
Date (Month/Year): Sept 2008
```

### Introduction (context only: never use it for content warnings)

```text
What’s the Worst That Could Happen? by Bruce Coville
```

### Performance text (classify this)

```text
MURPHY: (To audience) Good luck and I have rarely shared the same park bench. Sometimes I think Murphy’s law – “If something can go wrong, it will” – was invented just for me. I suppose the fact that my name is Murphy Murphy might have something to do with that feeling. Yeah: Murphy Murphy. It’s like a family curse. (Beat) The last name I got from my father, of course. The first name came down from my mother’s side, where it is a tradition for the firstborn son. You would think my mother might have considered that before she married Dad, but love makes fools of us all. I guess. (Beat) Anyway, you can see that right from the beginning of my life, if something could go wrong, it did. Okay, I suppose it could have been worse. I could have been born with two heads or something. On the other hand, as I lie here in my hospital bed trying to work out exactly how I got here, there are times when I wonder if being born with two heads might not have been the best thing. (Beat) To begin with, I want to say here and now that Mikey Farnsworth should take at least part of the blame for this situation. The one I am not going to blame is Tiffany Grimsley, though if I hadn’t had this stupid crush on her, it never would have happened.

MIKEY: Man, you’ve got it bad for Tiffany!

MURPHY: (Blushing and embarrassed) What are you talking about?

MIKEY: (laughing) Look at you blush, Murphy! There’s no point in trying to hide it. I watched you drooling over her in social studies class today. And you’ve only mentioned her, like, sixteen times since we got home this afternoon.

MURPHY: (To audience) I do not think I have actually drooled over Tiffany during social studies class. But it is hard not to think about her then, because she sits right in front of me. It’s the last class of the day, and the October sunlight comes in and catches in her golden hair in a way that makes it hard to breathe. (To Mikey, groaning) What am I going to do?

MIKEY: (shrugs) Either you suffer in silence, or you tell her you like her.

MURPHY: (To audience) Is he nuts? If you tell a girl you like her, it puts you totally out in the open. I mean, you’ve got no place to hide. And there are really only two possible responses you’re going to get from her: (a) She likes you, too (expression of pure terror) or (b) anything else, which is, like, totally, utterly humiliating. Then, on Wednesday, it’s as if the gods are smiling on me, which not something I am used to. Tiffany grabs my arm on the way out of social studies and says

TIFFANY: Can I talk to you for a second, Murphy?

MURPHY: Sure. (To audience) Not very eloquent, but it is better than the first thought that crossed my mind, which is, “Anytime, anywhere, any moment of the day.” It is also better than, “Your words would be like nectar flowering into the hungry mouths of my ears,” which was a line I had come up with for a poem I was writing about her. She hands me a folded-over set of papers, and my heart skips a beat. Can this be a love letter?

TIFFANY: I wrote this skit for drama club, and I thought maybe you would do it with me next Friday. I think you’d be just right for the part.

MURPHY: Yes! (To audience) She gives me one of those sunrise smiles of hers, grabs my arm and gives it a squeeze, and says,

TIFFANY: Thanks. This is going to be fun.

MURPHY: Then she’s gone, leaving me with a memory of her fingers on my arm and a wish that I had started pumping iron when I was in first grade, so my biceps would have been ready for this moment.

MIKEY: Murphy, you can’t go onstage with her. You can’t even move when you get onstage. Don’t you remember what happened in fifth grade?

MURPHY: (To audience) As if I could forget . . . . (Flashback) Mrs. Carmichael had cast me as George Washington in our class play, and I was, I want to tell you, pretty good during rehearsals. But when they opened the curtain and I saw the audience…well, let’s just say that when my mother saw the look on my face, she actually let out a scream. She told me later she thought I was having a heart attack. As for me, my mouth went drier than day-old toast, and the only reason I didn’t bolt from the stage was that I couldn’t move my arms or legs. Heck, I couldn’t even move my fingers. I couldn’t even squeak! They had to cancel the performance. Even after the curtains were closed, it took two teachers and a janitor to carry me back to the classroom. (To Mikey) Oh, man, what am I gonna do? I wail.

MIKEY: Come on, let’s look at the script. Maybe all you have to do is sit there and she’ll do all the acting. (the boys leaf through the script)

MURPHY: (To audience) No such luck. The script, which is called “Debbie and the Doofus,” is very funny. It also calls for me to say a lot of lines. It also calls for me to act like a complete dork. Immediately, I begin to wonder why Tiffany thinks I would be just right for this role. After two days I know not only my lines, but all of Tiffany’s lines, too, as well as the lines for Laurel Gibbon, who is going to be playing the waitress at the little restaurant where we go for our date. My theory is that I will enjoy rehearsals and the excuse they give me to be with Tiffany, and then pray for a meteor to strike me before the day of the performance.

MIKEY: (Scanning the skies) No meteor yet! Maybe you could be sick that day.

MURPHY: (Shaking his head) If I let her down, I will hate myself forever.

MIKEY: (Rolling his eyes) Maybe you should run away from home.

MURPHY: Despite my prayers, Friday arrives. I don’t suppose I really expected God to cancel it, though I would have been deeply appreciative if he had. I go through the day in a state of cold terror. At 2:45 Mrs. Whitcomb, the drama club coach, comes back to wish us luck.

MRS. WHITCOMB: Okay, kids – break a leg!

MURPHY: This is how people wish each other luck in theater?!

TIFFANY: Are you excited?

MURPHY: You have no idea. (To audience) Inside me, a small voice is screaming,

VOICE: What were you thinking of you moron? You are going to humiliate yourself in front of all these people, including the girl you would cut out your heart for, who will be even more humiliated than you are because it’s her skit that you are messing up! Run away! Run away!

MURPHY: My stomach clenches. Cold sweat starts out on my brow.

TIFFANY: Murphy! Your shoelace!

MURPHY: (glancing down) I have forgotten to untie it, which is the key to one of my first funny bits. I lift my foot to take care of the lace. At that instant the curtain opens, which startles me so much that I lose my balance and fall over, landing onstage in full view of the audience. There they are. The enemy. The people who are going to stare at me, judge me, whisper about me tomorrow. I am so frozen with terror I cannot move. This is it, I will never be able to face another living human being.

TIFFANY: (whispering) Murphy, are you all right?

MURPHY: (is startled out of his frozen terror and speaks to the audience) For the sound of that voice, I would do anything! (He stands, turns to the invisible door of the script and fake knocks) Knock-knock. Knockity-knock-knock. (To audience) To my surprise, the audience finds this funny. (happily surprised) Tiffany comes to the door, and we go through our opening business. But something is happening. I’m not making up lines, but I am making bigger gestures, (gestures broadly) broader moves, weirder voices than I did in rehearsal. People are howling. I am a genius! Who is this funny person, making everyone laugh? (he pulls out a chair for Tiffany at the restaurant, then sits – with a flourish he shakes out the cloth napkin . . . and blows his nose in it – He inspects the results and is fascinated by the imaginary boogers) The audience is just about screaming. This kind of laughter is even better than the sound of Tiffany’s voice. Laurel comes back with our “order” which, because this is a skit and we are on a low budget, is a plate of Hostess cupcakes. Chocolate. I am supposed to eat in a disgusting way. (picks up a cupcake and stuffs it whole into his mouth.) I deliver my next line . . . You are beautiful (bits of chocolate spew out. He crams another cupcake in his mouth and suddenly can’t breathe. He gasps for air)

MIKEY: (runs on stage screaming) He’s choking! He’s choking! (he grabs Murphy from behind and does the Heimlich Maneuver)

MURPHY: I’ve been Heimliched! (partially chewed cupcakes spew out of his mouth and spatter all over Tiffany)

TIFFANY: (reacts in horror and disgust)

MURPHY: (scrambles loose from Mikey’s grasp, he tries to wipe the mess off Tiffany.) Unfortunately, the table is close to the edge of the stage. Too close. Tripping over my untied shoelace, I hurtle headfirst into the darkness . . . . (Beat) Okay, I probably could have accepted the broken leg. I might even have been able to live with the memory of the look on Tiffany’s face. But when Mikey told me that my fly had been open during the entire fiasco, that was too much! Anyway, that’s how I ended up in this hospital bed, staring at my right leg, which is up in traction.

MIKEY: Tough luck, Murphy.

MURPHY: I try to remember that he is my friend and really thought he was saving my life when he Heimliched me. It is not easy.

MIKEY: Cheer up. It couldn’t get worse than this.

MURPHY: (Makes a disgusted face) Right . . . . After all, my name is still Murphy Murphy. And I am thirteen years old. I don’t even want to think about what might happen next week.
```

---

## IC-1433: Wigfield

- Title: Wigfield
- Author (byline): Amy Sedaris, Paul Direlio and Stephen Colbert
- Work: Not specified
- Publisher: Hyperion Books
- Publication date as stated: May 2003
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: RUSSELL HOKES, HOYT GEIN, CHARLES HALSTEAD, BURCHAL SAWYER, FLEET HOLLINGER, FARBER, JUDGE, FLEET, JUDGE COLEMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 2114
- Already set (do not supply): none

### Source block (context only)

```text
Author: Amy Sedaris, Paul Direlio and Stephen Colbert
ISBN: 978-0786868124
Publisher: Hyperion Books
Date (Month/Year): May 2003
```

### Introduction (context only: never use it for content warnings)

```text
Today you’ll hear personal accounts from the chief of police, 3 self-declared mayors; and an elected government official who will provide a snapshot of “small town”America – which I’m sure you will come to realize is more than “just a little ditty ‘bout Jack and Diane.” Wigfield by Amy Sedaris, Paul Direlio and Stephen Colbert.
```

### Performance text (classify this)

```text
RUSSELL HOKES: Welcome to Wigfield. Population: vague. Driven by the government’s recent threat to destroy the local dam, and with it the self-described “town” of Wigfield, residents must race against the clock. The real question: Is Wigfield merely posing as a town in order to collect federal disaster relief?

RUSSELL HOKES: Wigfield is a quarter-mile stretch of highway known as Wigfield. As is the case with many small towns, Wigfield is totally isolated, with the exception of the four-lane interstate that runs parallel to its Main (and only) Street.

I walked down the road staring into the shops, searching for something in this town to tell me its story. I read the signs hanging in the storefront windows: DAM BEING TORN DOWN SALE! EVERYTHING MUST GO BEFORE THE DAM IS TORN DOWN AND TOWN IS DESTROYED!

Wigfield is endangered! I decide to let the town residents tell their story in their own words . . . . I set forth to meet the People of Wigfield.

************

HOYT GEIN: I’m Hoyt Gein, the police chief under Charles Halstead, who is the legitimately self-declared may or Wigfield. I know some townspeople have criticized Mayor Halstead for appointing me chief of police, given my arson arrest record, but come on now, that’s just ludicrous. I can stop lighting fires anytime I want. Yes, I occasionally start fires when I’m out at a social event, but so what? Who doesn’t? It’s a free country.

Fleet Hollinger thought he could force me out . . . he’ll hold an election, and just because he’s the most powerful man in town, he’ll get elected. Well, that not the way things work. A curious electrical fire at the polling station saw to that. It turns out it’s pretty hard to exercise your right to vote when you’re on fire. Case closed. In the confusion, the town ended up with three mayors.

Maybe saving a little town like Wigfield isn’t important to most people, but it’s important to me. I know most people don’t cotton to small towns,. Like lemmings, they follow everyone else to the cities, where they can find jobs, housing, and culture. But in Wigfield we march to is the beat of our hearts. You scrape away the unemployment, the unsolved murders, or even the contaminated topsoil, and what you’ll find is the giant swollen heart of America.

RUSSELL HOKES: And then Hoyt demanded that I follow him out to his camper van. Any doubt I had as to his official capacity was dispelled by the words “Wigfield’s Police Chief” stenciled on the side. Throwing open the rear cargo door with a flourish, he proudly displayed a man win his early forties who was elaborately seat-belted into a lawn chair. According to Hoyt, this cheerfully disheveled man was Mayor Charles Halstead, who had insisted on meeting me.

CHARLES HALSTEAD: I like fudge. I have a briefcase. I keep my fudge in there. I’m not from here, but I live here now. I came to this town to represent the lead dispersal plant. The government wanted to close it because they said it was retarding the employees. I got a court order that allowed me to stay at the plant so I could disprove firsthand the effects of the plant. After I lost the case, I decided to stay in Wigfield. I don’t know why. I like fudge. Guess what I have in my briefcase. I’m one of the mayors. I hope they don’t tear down the dam. My fudge would get wet.

RUSSELL HOKES: I knew now that a vital part of this story was the mayor. All three of him. I had met one, but I knew that some more of them were out there. My search quickly led me to the business establishment of Mayor Burchal Sawyer. We met in his vast junkyard.

BURCHAL SAWYER: I’m the great American success story. One day you’re livin’ out of your car, the next you’re livin’ out of your car, and you’re the mayor of a town. That’s because I make things happen.

Listen to this. Fleet Hollinger tried to tell me that I couldn’t run for mayor of this town because I didn’t have a residence. I was livin’ in my car at the time. Then he gets his [shorts] all in a bunch just ‘cause I didn’t have any identification. I know who I am. I don’t need fingerprints to prove it. Plus, he says that I’m not educated, and that’s a crock. Look, last time I checked this was a free country.

Speaking of which, as one of the mayors, I feel I should chime in about this dam business. On the record, my official reaction is this: Why would the state want to tear our dam down? It just doesn’t make any sense: flooding a river bed? What kind of logic is that? You think just because I’m used to livin’ in my car it will be easy for me to pull up stakes and drive to another place? But again, if it’s got to come down, well then, I say, as a community we prepare ourselves for the horrifying loss we must endure, and on behalf of the town I accept my relocation money graciously.

RUSSELL HOKES: This only left Fleet Hollinger to complete the trifecta of local leadership. Logic said his home. A series of double and singlewide trailers had been hauled into an impressive maze of aluminum and connected in a haphazard fashion with sheet metal and button rivets. Clearly this was the home of an important man.

FLEET HOLLINGER: I’m a simple man in a simple town. Small towns are built on old-time values. Friendliness, openness, trust. That’s what I’m all about. Besides the used car lot, I also own Fleet’s Used Auto Parts – the oldest business in Wigfield. Another business I run is Mack (M-A-C-K) Donalds. The only and the best fast-food chain in Wigfield. As we speak, a large hamburger chain is trying to shut me down. All I know is my middle name is Donald and my nickname is Mack because this guy I know dries a truck. It seemed natural to me that a clown would be the mascot. How can they have a lock on that? When you think of hamburgers, you think of cows, cows make you think of bullfights, and who distracts the bulls? Clowns! I named the clown after my nephew Ronald. I wouldn’t be surprised if that unnamed hamburger chain is involved in this whole dam thing.

Along with being a respected businessman, I’m also the mayor. Now, I’m sure the government sees us as a bunch of squatters who gradually accumulated at the bottom of a newly dry riverbed. But we will battle tirelessly to keep our town, and nothing will deter us!

RUSSELL HOKES: Through my many interviews with the mayors of Wigfield a story was starting to shape up. But my journalistic sense of fair play told me that Representative Bill Farber deserved the chance to give his side of the story. I decided to track him down.

FARBER: First of all, Wigfield isn’t a town. These people are living here illegally. Half of those people don’t have social security numbers. They don’t even have a zip code. They don’t pay any taxes. They’re outside of any health care system or school district. But even though they have built illegally on land that belongs to the state, we are willing to discuss a nominal relocation fee. The state will not recognize this place as a town.

RUSSELL HOKES: Well, I guess that will all be settled today in court.

******

JUDGE: Be seated. We have a motion filed by the town of Wigfield. At this time the plaintiffs can make their opening statement.

FLEET: You Honor, or scenic little town is nestled quaintly in the shadow of the Bulkwaller Dam. Our tiny little hamlet will soon be washed away by the cold, unforgiving waters of the so-called Fresh Springs River. I call Eminent Domain! If residents are relocated by the state, they must be financially compensated for both home and property. The pain is immeasurable, as should be our compensation.

FARBER: Your Honor, eminent domain only applies to legally occupied incorporated towns. There is no precedent for payment to what really amounts t o illegal squatters, no matter how many mayors they claim to have.

FLEET: How dare you?! Are you suggesting that we are merely posing as a town in order to get money when the dam is torn down?

RUSSELL HOKES: Your Honor, my name is Russell Hokes. I am a writer. Now perhaps these people don’t possess the necessary legal documents stating they are a town. But I’ll tell you this much, Judge. I have lived with these people for nearly two weeks now. I’ve seen their children play on the mercury mound. I think I can say with great confidence that if Wigfield is not a town, then I am not a writer.

JUDGE COLEMAN: I’m going to take this matter under consideration. The demolition of Bulkwaller Dam is stayed for one month. You will have that one month to prove you are a town. If you can’t prove your township, the dam may come down and the state will have no financial obligation to you whatsoever.

RUSSELL HOKES: At first the town struggled for a solution: 1) Add the words “Town of” to the Wigfield sign. 2) Get a Wigfield sign and 3) Parade!

What better way to prove you are something you are not than to celebrate the very thing that someone says you aren’t! And what better way to celebrate than with a parade?

What happened next is almost impossible to believe. A reporter at one of the big-city papers wrote a human-interest story about the travails of Wigfield. “Small Town Parades to Save Self.” Anyway, somehow that story piqued the interest of other newspapers. Soon, they began showing up in Wigfield. Stories began to spread, and before long crowds began to show up along the parade route.

Representative Farber has informed the town that he would like to address them.

FARBER: Well, ladies and gentlemen, what I have to say is very simple. You win. The state is bowing to public pressure and has decided not to tear down the Bulkwaller Dam.

RUSSELL HOKES: A chant of “where’s our money” rings out from the floor and begins to build

FARBER: I don’t have any money for you, but I do have your new town charter. You should know that among the responsibilities that come with townhood are providing proper sewage, streetlights, a school system . . . well, the list goes on. A tax will have to be levied on the citizens and businesses to pay for all that, of course. You have until the first of the year to initiate these actions.

FLEET: What if we don’t?

FARBER: The town will be dissolved, your property confiscated without compensation, you will be forcibly removed from the area and all town officials, which I might remind you are legally listed as Hollinger, Sawyer, Gein and Halstead will be subject o criminal prosecution. Good day, gentlemen.

*****************

RUSSELL HOKES: Hello, Mr. and Mrs. America, this is Russell Hokes coming to you live from the first annual Wigfield Town Charter Celebration. It’s just about dusk, and I suspect people will begin gearing up for the fireworks display. Hoyt Gein is moving toward the base of the dam carrying fuses, a torch, and other explosive delights. I can only imagine what flaming wonders will emerge from the deep shafts bored directly into the face of the dam.

It’s exploding! It’s exploding! The whole dam is exploding! Oh, the humanity! I can’t talk! I can’t breathe! The dam is a mass of smoking rubble. Water is crashing through the smoking wreckage! The entire town is being submerged!

(5 days later)

Who lived? They all did. In the time that it takes most people to change into their grieving black, the people of Wigfield have bounced back as if their souls were made out of Superballs. The mind reels at the fact that given a disaster of this proportion, almost every member of the town survived, and not only that, they were able to miraculously salvage nearly every possession. God has smiled on these people. Amid all this mournful merriment, one agonizing question remains. What now?

FLEET: Well, here’s the deal. I’ve talked to the boys down at the Federal Emergency Management Agency, and apparently we qualify for disaster relief. The only thing we need in order to get what is justifiably coming to us is this little written account of the tragedy by an impartial third-party witness . .

RUSSELL HOKES: Then is struck me. Third-party account? Why I could be that account! . . . . . [So I leave you with this question]: Was Wigfield merely posing as a town in order to collect federal disaster relief? [The world may never know].
```

---

## IC-1434: YMA Dream

- Title: YMA Dream
- Author (byline): Thomas Meehan
- Work: Fierce Pajamas: An Anthology of Humor Writing from The New Yorker
- Publisher: English
- Publication date as stated: October 2002
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1429
- Already set (do not supply): none

### Source block (context only)

```text
Author: Thomas Meehan
Book: Fierce Pajamas: An Anthology of Humor Writing from The New Yorker
ISBN: 978-0375761270
Publisher: English
Date (Month/Year): October 2002
```

### Introduction (context only: never use it for content warnings)

```text
Dreams are known to reveal the secret desires of the dreamer. Many prophecies have been made through dreams. Dreams made Martin Luther King Jr. famous. Jesus was a dream interpreter. Therapists wouldn’t have bread on the table if not for bizarre and questionable dreams. However, if Tom is expecting his dream to hold relevance in reality, he will find himself increasingly tongue tied. “YMA Dream” by Thomas Meehan
```

### Performance text (classify this)

```text
In this dream, which I have had on the night of the full moon for the past three months, I am giving a cocktail party in honor of Yma Sumac, the Peruvian singer. This is strange at once, for while I have unbounded admiration for four-octave voices, I have never met Miss Sumac, and, even in a dream, it seems unlikely that I should be giving her a party. No matter. She and I are in the small living room of my apartment, on Charles Street, in Greenwich Village, and we are getting along famously. I have told her several of my Swedish-dialect stories, and she has reciprocated by singing for me, in Qyechua, a medley of Andean folk songs. Other guests are expected momentarily. I have no idea, however, who any of them will be. Miss Sumac is wearing a blue ball gown and I am in white tie and tails. Obviously, despite the somewhat unfashionable neighborhood and the cramped quarters of my apartment, it is to be a pretty swell affair. In any case, I have spread several dishes of Fritos about the room, and on what is normally my typing table there is a bowl of hot glugg.

The doorbell rings. A guest! I go to the door, and there, to my astonished delight, is Ava Gardner. This is going to be a bit of a night, I think.

"Tom, darling!" she says, embracing me warmly. "How wonderful of you to have asked me."

In my waking hours, unfortunately, I have never met Miss Gardner. In my dream, though, my guests seem to know me rather intimately, while, oddly, none of them seem to know each other. Apparently it is their strong common affection for me that has brought them to Charles Street. For my part, although I immediately recognize each guest as he or she arrives, I have no memory of having ever met any of them, or, for that matter, of having invited them to a party in my apartment. On with the dream, however. "Miss Ava Gardner," I say, "I'd like you to meet Miss Yma Sumac."

"Charmed," says Miss Sumac.

"Delighted," counters Miss Gardner.

“Ah, but Tom," says Miss Sumac, with an enchanting laugh (which runs up the scale from E above middle C to C above high C), "let us not, on this of all occasions, be formal. Por favor, introduce each guest only by the first name, so that we may all quickly become-how shall I say?-amigos. "

Typical Peruvian friendliness, I think, and reintroduce the two. "Ava, Yma," I say.

We sit around for some time, sipping glugg and munching Fritos. Things seem to be going well. The doorbell rings again. The second guest is a man-Abba Eban, the former Israeli Ambassador to the United Nations. Again I make the introductions, and, bowing to the wishes of the guest of honor, keep things on a first-name basis. ''Abba, Yma; Abba, Ava," I say.

I stifle a grin, but neither Miss Sumac nor my two other guests see anything amusing in the exchange. We chat. The bell rings again, and I am pleased to find Oona O'Neill, Charlie Chaplin's wife, at the door. She is alone. I bring her into the room. "Oona, Yma; Oona, Ava; Oona, Abba," I say.

We are standing in a circle now, smiling brightly but not talking much. I sense a slight strain, but the party is young and may yet come to life. The bell again. It is another man- Ugo Betti, the Italian playwright. A bit hurriedly, I introduce him to the circle. "Ugo, Yma; Ugo, Ava; Ugo, Oona; Ugo, Abba," I say.

Miss Sumac gives me an enigmatic glance that I try to interpret. Boredom? Thirst? No, she looks almost irritated. Hastily, I replenish everyone's glass. For some reason, I begin to hope that no other guests have been invited. The doorbell rings once again, however, and I open the door on two lovely actresses, Ona Munson and Ida Lupino. This gives me a happy inspiration for my introductions. "Ona and Ida," I say, "surely you know Yma and Ava? Ida, Ona-Oona, Abba." Damn! It doesn't come out even. "Ida, Ona-Ugo," I finish lamely.

I have scarcely given Miss Munson and Miss Lupino their first drinks when I am again summoned to the door. My guests stand stonyfaced as I usher in the new arrival, the young Aga Khan. He is looking exceptionally well turned out in a dinner jacket with a plaid cummerbund. Smiling too cheerfully, I introduce him to the waiting group. "Folks," ,I say, using a word I have always detested, "here's the Aga Khan! You know." But there is silence, so I must continue. ''Aga- Yma, Ava, Oona, Ona 'n' Ida, Abba 'n' Ugo."

The Aga Khan and Mr. Eban, I notice, take an immediate dislike to each other, and I begin to feel an unmistakable pall descending over my party. I suggest a game of charades. This is met with glacial looks from everyone, including Miss Gardner, whose earlier affection for me has now totally vanished. When the doorbell rings this time, everybody turns and glares at the door. I open it and discover another pair- Ira Wolfert, the novelist, and Ilya Ehrenburg, the Russian novelist. The latter, I know, is quite a man-of-the-world, so I try a new approach. "Ilya," I say, "why don't you just introduce yourself and Ira? You know all these lovely people, don't you?"

"Nyet," says Mr. Ehrenburg. "Can't say that I do."

"Oh, all right," I say. "Ilya, Ira, here's Yma, Ava, Oona. Ilya, Ira, Ona, Ida, Abba, Ugo, Aga."

I ask Miss Sumac to sing for us. She refuses. We continue with the glugg and some hopelessly inane small talk. Mr. Eban and the Aga Khan stand at opposite sides of the room, eying each other. I begin to wish I'd never given the goddam party. Ona Munson jostles Ugo Betti's elbow by accident, spilling his drink. I spring forward to put them at their ease, whipping a handkerchief from my pocket. "Never mind!" I cry. "No damage done! Ugo, you go get yourself another drink. I'll just wipe this glugg off the, uh, rug."The guests fix me with narrowed eyes. At this moment, Eva Gabor, the Hungarian actress, sweeps through the door, which I have cleverly left open. Unaware of the way things are going, she embraces me and turns, beaming, to meet the others. Inevitably, I must make the introductions. I start rapidly. "Eva, meet Yma and Ava and Oona-" But then I find that Miss Gabor is pausing to hug each guest in turn, so I am forced to make the remaining introductions separately. "Eva, Ona; Eva, Ida; Eva, Ugo; Eva, Abba; Eva, I1ya; Eva, Ira; Eva, Aga."

This is a terrible party. All the men have bunched up. We stand in a circle, glowering at one another. I can think of nothing to say. I feel oddly hemmed in, like a man who is about to be stoned to death.

"Am I late?" asks the actress Uta Hagen gaily as she comes tripping into the room.

"No, no!" I say, gallantly taking her arm and steering her at once toward the punch bowl and away from the others.

"Please have the common decency to introduce your guests to one another," says Miss Sumac, in a cold monotone. "And in the proper manner.”

In the dream, Yma Sumac seems to have some kind of hold over me, and I must do as she wishes. "O.K., O.K.," I snap crossly. "Uta, Yma; Uta, Ava; Uta, Oona; Uta, Ona; Uta, Ida; Uta, Ugo; Uta, Abba; Uta, Ilya; Uta, Ira; Uta, Aga; Uta, Eva." I turn to see if this has placated Miss Sumac. But she coldly ignores me. I have begun to hate her. Then I discover that the glugg has run out, and I am forced to offer my guests rye and-7-Up. In the hope that no further company will arrive, I silently close the door. The bell rings instantly, however, and I feel a chill run down my spine. I pretend not to hear it.

“Answer the door," Miss Sumac says peremptorily. My circle of guests moves menacingly toward me. With a plummeting heart, I open the door. Standing before me, in immaculate evening dress, is a sturdy, distinguished-looking man. He is the Polish concert pianist Mieczyslaw Horszowski.

"Come in, Mieczyslaw!" I cry, with tears in my eyes. "I've never been so glad to see anyone in my whole life!"

And here always, my dream ends.
```

---

## IC-1435: Your Mother’s Butt

- Title: Your Mother’s Butt
- Author (byline): Alan Ball
- Work: Five One Acts Plays by Alan Ball
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CLIENT, PSYCHOLOGIST
- Teaser before the introduction: No
- Spoken words (computed): 1414
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alan Ball
Book: Five One Acts Plays by Alan Ball
ISBN: 0822213680
Publisher: Dramatists Play Service, Inc.
Date(Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
Without fail, just about anything that goes wrong in a child's life is the mother's fault. What a good idea it would be to have child psychiatry a regular part of annual well child doctor's visits. After the vaccinations and the eye-chart test, the child could lie down on a chaise and spill for the doc all the ills he feels mom has inflicted on him. “My mom won't leave the hall light on at night and the noises outside my window scare me.” We could take care of the problem right there at age 5 and avoid having the same conversation with a therapist 30 years later and deciding that mom's hall light failings are to blame for the adult child's foibles. In this selection our client seeks psychiatric attention for his increasing dissatisfaction with life and as is typical . . . . His therapist attempts to trace his many idiosyncrasies directly to what she affectionately calls . . . Your Mother’s Butt by Alan Ball.
```

### Performance text (classify this)

```text
CLIENT: My life is, like, so mundane. The days come, the days go. I keep waiting, waiting, waiting, but for what? I go to work, I eat, I work out. I watch television. I'm not really depressed. Well, yeah, I guess I am depressed. I'm lonely. I'm easily irri-tated. But it's not the kind of overwhelming depression that feels like it's ripping me apart. It's more of a . . . blandness, an overall numbness. . . like every fiber of my being has been sucked dry of any coherent reason to exist. (Pause.) Nothing matters.

PSYCHOLOGIST: Nothing?

CLIENT: No. (Pause. The CLIENT cries.) I have- (It is too painful for him to say; takes a moment, then tries again.) I have this sweater. .

PSYCHOLOGIST: A sweater?

CLIENT: It's really nice. It's this old sweater, I think it belonged to my brother. It's just this black V-neck sweater, wool, but it's faded and soft and it fits me really well, it accentuates my shoulders, but, like, in a subtle way, and when I wear it, I feel really sexy.

PSYCHOLOGIST: You have every right to find joy in a sweater.

CLIENT: I do, that's the weird part, it's like the only thing in my life I get excited about. Sometimes I put it on just to vvalk around in it, and then sometimes I forget that I've done laundry and I go to pick out something to wear, and there it is, all clean and soft and faded just a little bit more, all folded up, and it's, like, primal, like, maybe even religious. (Pause.)

PSYCHOLOGIST: How are you feeling?

CLIENT: How do you think I'm feeling? The only significant relationship in my life is with a piece of clothing? At best, that's tremendously shallow, and at worst, it's sociopathic. I mean, if I was somebody else and I knew me, I would say look, get a life.

PSYCHOLOGIST: I think perhaps you're being a bit hard on yourself.

CLIENT: You're right. God, I am so messed up. I've got to do something about this, I can't be this messed up anymore. What can I do? Tell me what to do. You're the expert.

PSYCHOLOGIST: Well, first, I think we need to take a look at why you are so hard on yourself. (Pause.)

CLIENT: (Sighs.) Okay. (Long pause.)

PSYCHOLOGIST: How are you feeling?

CLIENT: Excited.

PSYCHOLOGIST: Excited?

CLIENT: Yeah. I'm thinking about this pair of shoes I saw yesterday.

PSYCHOLOGIST: Shoes?

CLIENT: Yeah. I've been looking for the perfect pair of black shoes for. . . well, probably for my whole life. You know, a pair of oxfords, just plain, nice leather, not too clunky, but not too Wall Street, either. The kind of shoes you can wear with a suit and look really hip, but you can also wear with blue jeans and look really. . . intelligent.

PSYCHOLOGIST: Intelligent.

CLIENT: But also approachable. And politically correct. With a sense of humor.

PSYCHOLOGIST: Shoes seem to communicate quite a lot for you.

CLIENT: Oh, yeah. Definitely. I think there's two ways to learn a lot about somebody in a short amount of time. One is their refrigerator-not only what they stick on the front of it, but what's in it, too-and the other is their shoes.

PSYCHOLOGIST: (A hunch.) What's in your refrigerator?

CLIENT: Well, nothing right now.

PSYCHOLOGIST: Ah.

CLIENT: These shoes are the greatest shoes-I think.

PSYCHOLOGIST: Let's stay with the image of the empty refrigerator for a moment.

CLIENT: Why?

PSYCHOLOGIST: I have an idea it might be significant.

CLIENT: Okay.

PSYCHOLOGIST: (Taking time, setting mood.) A cold, white, empty box. . . possibly a source of nourishment, but also a potential death trap. (Pause.)

CLIENT: Cool. (Pause.)

PSYCHOLOGIST: Perhaps we should return to the shoes.

CLIENT: Okay. (Pause.) I don't know. They might be the right ones, they might not. They're really expensive. I don't want to spend that much money and have them not be the perfect shoes! (Suddenly angry.) God, why does everything always have to be so hard?

CLIENT: Weird. I just remembered. . .oh, I had this weird dream.

PSYCHOLOGIST: Tell me about it.

CLIENT: I dreamed. . . I dreamed I was in this. . . house, it wasn't my house, but I lived there. And I was in this big room, and I was in this bathtub. This old-fashioned bathtub on pedestals. And I'm wearing clothes. This olive drab cardigan, just over a T-shirt, and these flax-colored, I guess, linen shorts. And then I hear these voices in the hall and in comes my mother. Only she's a younger version of herself, and she's wearing these 1960s hip-huggers, and she has Mary Tyler Moore hair that she's tied a bandanna around, and I think oh, she's trying to be hip, and it's really sort of sad for a moment. . . then she gets in the bathtub with me, only she won't look at me, and then she bends over and. . . she just sticks her butt in my face.

PSYCHOLOGIST: (Scribbling furiously.) This is really good.

CLIENT: And I'm thinking. . . okay. This is kind of weird. . . this is really. . . it's really not quite right. . . it's really. . .

PSYCHOLOGIST: Inappropriate?

CLIENT: It's more than that. . . Oh, God, what is it?

PSYCHOLOGIST: Visualize the dream.You're in the water. . . Is the water warm or cold?

CLIENT: Warm. But not hot.

PSYCHOLOGIST: And she comes in.

CLIENT: Yeah, and she's walking this swingy, hippy kind of walk, and I think oh, God, my mother. I'm so embarrassed.

PSYCHOLOGIST: And she gets in the tub. . .

CLIENT: You can tell she thinks she's really groovy.

PSYCHOLOGIST: Now she's in the water with you. . .

CLIENT: Yeah. And she is wearing the most hideous Barbie, like, flower power outfit and macramé belt.

PSYCHOLOGIST: She's turning around. She's bending . . .

CLIENT: Oh, wait a minute! I just realized something. Oh, wow. (Pause.)

PSYCHOLOGIST: Yes?

CLIENT: It makes such perfect sense, doesn't it.

PSYCHOLOGIST: What does?

CLIENT: I get my bad belt luck from her. It's heredity. (Long pause.)

PSYCHOLOGIST: (Just the slightest bit if tightness.) How are you feeling?

CLIENT: I feel great! If it's hereditary, then I don't have to feel guilty for it. I have no control over it, so it's not my fault. Right?

PSYCHOLOGIST: Well, not exactly, no. One of the underlying assumptions that the therapeutic process is based upon is that you do have control over your life.

CLIENT: No ,thanks. I don't want that kind of responsibility. (Pause.)

PSYCHOLOGIST: I'd like to get back to your mother's butt.

CLIENT: Please. Be my guest.

PSYCHOLOGIST: It's such a strong image, with so many potential implications. It could open many doors. So I'd like to try something a little . . . unorthodox.

CLIENT: Oh, no. You're not going to stick your butt in my face, are you?

PSYCHOLOGIST: No, no. I just want you to close your eyes, and relax. Feel the warm water in the tub. Now try to picture your mother's butt.

CLIENT: Okay.

PSYCHOLOGIST: Do you see it?

CLIENT: Plain as day.

PSYCHOLOGIST: Now speak to it.

CLIENT: I'm sorry?

PSYCHOLOGIST: Speak to your mother's butt.

CLIENT: Oh, right.

PSYCHOLOGIST: Think of it as separate from your mother. As an entity of its own. If you could communicate with it, what would you say?

CLIENT: Get out of my face.

PSYCHOLOGIST: Perhaps it would be helpful if you gave it a name.

CLIENT: What do you mean?

PSYCHOLOGIST: If it had a name, what would it be?

CLIENT: You mean like a person's name?

PSYCHOLOGIST: Possibly.

CLIENT: Like. . . Debbie?

PSYCHOLOGIST: Perhaps.

CLIENT: This is really weird.

PSYCHOLOGIST: Just try speaking to it by name.

CLIENT: Get out of my face, Debbie. Excuse me, Debbie, can you get out of my face? Thank you. Yo, Debbie. Get the heck out of my face.

PSYCHOLOGIST: Maybe you'd like to yell at it.

CLIENT: Sure, why not. (Yells.) Debbie! Get the hell out of my face, you witch! And take that hideous macramé belt with you!

PSYCHOLOGIST: Now become the butt.

CLIENT: What?

PSYCHOLOGIST: If you were the butt, what would you say in response?

CLIENT: Uhm, I'm Debbie the butt, and you better shut up. Stop telling me what to do. This is a free country and I can be wherever I want. If you don't like me being in your face, then you leave.

PSYCHOLOGIST: Now respond as yourself.

CLIENT: You stupid butt. I was here first.

PSYCHOLOGIST: Keep going.

CLIENT: Oh yeah, well. . .

PSYCHOLOGIST: Keep going.

CLIENT: I'm confused. Am I me or am I the butt?

PSYCHOLOGIST: Keep going!

CLIENT: But

PSYCHOLOGIST: Don't turn away from this! We're right on the verge of something!

CLIENT: Um

PSYCHOLOGIST: Don't hold back! Tell that butt how you are feeling!

CLIENT: (Loses it.) God! Shut up! Get out of my face, get out of my bathtub, get out of my life, you butt! I hate you, I hate you, I hate your guts! (He sobs uncontrollably. Long pause.)

PSYCHOLOGIST: How are you feeling now?

CLIENT: I feel like the biggest jerk in the universe. I'm never telling you another dream again. But. . . oh, wow. Wow. This is intense.

PSYCHOLOGIST: What?

CLIENT: Have you ever been hit with, like, this realization, it's, like, something you always knew, but it's the first time you've ever really seen it so clearly? Oh this is so weird, it's like deja vu.

PSYCHOLOGIST: What? (The CLIENT sits up and looks at her.)

CLIENT: (With great resolve.) I don't care how expensive they are, I'm buying those shoes! (Blackout.)
```

---

## IC-1436: Press Play

- Title: Press Play
- Author (byline): M.K. Hill
- Work: Press Play
- Publisher: Mushroom Cloud Press
- Publication date as stated: August 1, 2023
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1065
- Already set (do not supply): none

### Source block (context only)

```text
(none)
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
Girl: It’s so nice to finally be able to watch a movie with you.

Boy: Oh yeah!
Girl: We’ve had such a busy week. You with sports, me with debate. It’s gonna
feel so nice to sit down with just the two of us.
Boy: Totally.
Girl: Who are you texting?
Boy: No one
Girl: About what?
Boy: Our theory on how the government is run by radioactive lizards.
Girl: Oh ok……well, could you do that some other time? I want to watch this
movie with you.
Boy: Oh sorry, of course of course.
Girl: Great…where is the remote?
Boy: Uhhhhhhhh
Girl: I know I had it a moment ago.
Boy: Check the last place you saw it?
Girl: I was gonna check the first place I saw it.
Boy: Just trying to help
Girl: Get up.
Boy: Oh yeah check the couch cushions
Girl: Oh wow what a great idea
Boy: I know
(Girl starts to pull out many things in the cushions, very random and crazy
things. Then pulls out a bag of chips)
Boy: Oooh!
Girl: Don’t eat it!

(Finally pulls out the remote) Girl: Ah ha! Boy: Yah! Great job Girl: Uh huh. Let's just start the movie Boy: Oh yeah

(Starting to press play) Boy: Wait! I need to get some water! Girl: Hurry. Boy: Do you want any? Girl: No.

(goes and comes back with water) Boy: Alright.

(Girl looks disgusted at boy) Boy: You want water…. Girl: Yes.

(Boy gets water, Girl looks at boy)
Boy: What? Oh….you want a blanket.
Girl: Please.
Boy: Here!
Girl: Thank you! Alright, let's start now, the movie is 2 and a half hours long-
Boy: What! That movie is way too long…..without popcorn! I’ll be right back
Girl: Oh come on.

(Boy happily pops popcorn while girl gets inpatient) Girl: Come on!

(Boy comes back) Boy: Okay! I’m done

Girl: Great

(Boy loudly opens the bag of popcorn) Boy: Alright.

(Girl tries to start the movie) Boy: No! Girl: What. Are you ok? What’s- Boy: The popcorn’s burnt! Girl: Really? Boy: This is a disgrace I must pop some more! Girl: We don’t need- Boy: Nonsense! It is a sin to watch a movie without the golden crunch of popcorn. It was made for the sole purpose of watching movies! Girl: I don’t think that’s true Boy: Shhh. There was a brave man, who lived in the dark times of the world. The world in which corn had yet to be popped. Many years, terrible things happened during that time. Wars, climate change, more wars. Soon. A brave man, whose name was probably Steve. Came up with the most brilliant idea anyone could ever think of. Adding heat to corn, then pouring gallons of butter on top. Since then, we must honor Steve, by eating his glorious creation every time a cinematic piece is playing. I mean. It’s popcorn! Could you imagine anything better? Girl: Yes, many things. Boy: I must go! And make more. Girl: Uh huh, you do that.

(Boy comes back some time later)
Girl: How long did you microwave it?
Boy: 2 minutes
Girl: Felt like two hours
Boy: Well, time does stop when you are microwaving something
Girl: Can we PLEASE start?
Boy: Yes
(Girl begins to press play) Boy: Ah wait! I’ve got to pee!
Girl: Really?
Boy: When you gotta go you got to go Girl: Then go

(Boy goes and girl looks at watch)
Boy: Much better
Girl: I am going to start the movie now.
Boy: Can’t wait

(Girl tries to start the movie but boys phone rings) Boy: Oops.. Hold on….oh my really? That’s terrible Girl: What happened?

Boy: My car's warranty has expired…yes…please…we must extend my
warranty!
Girl: No…no we don’t….goodbye Mr. Spam caller
Boy: Ah…Spam…what a great name.
Girl: Sit down….and lets watch this movie! Boy: Ok. Ok.
Girl: You have everything you need. Popcorn, water, you went to the bathroom
Boy: I promise you. I am ready
Girl: Both of our phone are away
Boy: Yes…you should really stop talking. I want to watch the movie
Girl: Boy. Don’t you test me
Boy: Sorry
Girl: Alright.

(The doorbell rings) Girl: AH! Boy: I’ll get it

(Boy opens the door and the mail person is here)
Mail Person: Package delivery.
Boy: Oooo… BABE did you order a package?
Girl: Well, apparently, because it’s here! Just get it and come
Boy: Thank you so much!
Mail person: Swipe and Sign
Boy: Oooh, see I don’t really sign anything because the value of my signature
will go down with the more things I sign.
Girl: Let’s go

(Back on the couch) Boy: What did you get? Girl: Never mind that….let’s just…

(Doorbell rings) Boy: I’ll get it!

(Opens the door and there is a two scout) Scout : Hi! I’m are here today to support the scouts! Boy: Cookie! I love cookies!! I will take three of the very minty one, 5 of those lemons things, and 6 of the peanut butter one that no one knows the name of Scout : Uh….sorry, but the girl scouts don’t sell cookies anymore. We try to be more environmentally friendly. Boy: Oh, ok- Scout : We now have gluten free non gmo vegan zero sugar no calories….ice triangles! All proceeds help-

(Boy angrily shuts the door)

Boy: I wanted cookies.

Girl: You ok? Boy: They didn’t have any cookies!! Girl: You poor child….let’s watch the movie now.

(Doorbell rings) Girl: Imma kill someone Boy: I’ll get it!

(Opens the door and census bureau enters)
Census Bureau : Hi, I am here with the US census bureau
Boy: I have no Idea what that is but ok!
Census bureau : How many people live in this house?
Boy: (gasp) Babe! Is this your way of asking me to move in with you? Census
Bureau: Who is the owner of this house
Boy: Uh, I have to have a talk with my girlfriend, who is seemingly upset…so if
you’d just give me a sec-

(Shuts the door) Boy: Babe…what's wrong. Girl: We have spent 2 weeks trying to free up time to just sit and be together, and it’s tiring. You’re my boyfriend. I just want to watch this movie. Boy: I’m sorry. I really am. You know, ever since I met you, you’ve been a go-getter. You’ve known what you want, and you do it. The world tends to bring you down in ways that aren’t right. You deserve a break. As your boyfriend. It is my job to make sure you are happy. And I vow to be the best boyfriend in the world. We will watch this movie together, and we will laugh, cry, and talk about how predictable the ending will be. We will be one again. This world today is trying to separate us. But no more! We shall be one, together, sitting down. On this couch. Watching this movie. I will make you happy, all of our dreams will come true. I promise. But first. I have to go to the bathroom. Girl: That’s it!

(Girl hits boy with a frying pan and ties him up) Girl: I will watch this movie with you, even if it's over your dead body.
```

---

## IC-1437: Ringing

- Title: Ringing
- Author (byline): Frank Smith
- Work: Ringing
- Publisher: Mushroom Cloud Press
- Publication date as stated: August 1, 2023
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: EZRA
- Teaser before the introduction: No
- Spoken words (computed): 2646
- Already set (do not supply): none

### Source block (context only)

```text
(none)
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
A Dramatic Monologue

Written by Frank Smith SCENE I Ezra’s Apartment.

(Spartan. No art, no posters, no personality. Yet 100% clean. Not one dust speck on one surface.) EZRA.

(EZRA NEWELL (32), even in sweats, he looks crisp and sharp, sits at a table, drinking coffee. He points to a second cup.)

EZRA: For you. I told Chief, you guys don’t have to come check on me. I’m a detective. I’m tough. I’ve just, I don’t know, been through it these last few weeks. The Ramos case took a lot out of me. I really thought we were going to find that kid, you know? You do what we do long enough, and you get an instinct for how things are going to turn out. That case had “this kid’s hiding out somewhere” written all over it. Ran away from home all the time. Whenever he fought with his big brother. But there was love there. They needed each other. Little guy, getting taken right off the street like that. Wouldn’t have happened if his big brother had been looking after him, like he was supposed to. They’re all victims. I know that. I just never would let someone I truly loved out of my sight like that. You never know what could happen.

(Ezra goes to take another sip of coffee, then pushes it away.)

EZRA: Here. Take it. I can’t have this. I’m pretty wired already. You know, I don’t know how I’d be able to do any of this if it weren’t for Amory. He really is the one for me. Which is crazy, because cops and teachers, all we really have in common is unions. That’s not true: he and I, we both love kids. I think that was the big thing that drew us together. I love protecting kids. He loves teaching kids. Plus, we first met while helping a kid find her Mom in the park. You know that story, right? Wait. I’ve never told you? Then you’re in for a treat. Well, I was doing my usual morning workout in the park. Because I’m a fan of the outdoors. Not because I was throwing out a fishing line. AKA my abs. Anyway. He was jogging by. But I felt like he kept doing laps near my area in particular. And not just ‘cause it was “part of his routine.” I’m about to get my flirt on, when I hear this little girl crying. Curly hair. Striped dress. Says she has no idea where her Mom went. The dog ran off, and she hasn’t come back yet. I’m guessing this means she’s only been gone a few minutes – I remember being a kid and having no sense of time – but still, I go to hold her hand, and walk her around, to look for her Mom. That’s when I see someone else has taken her hand at the same time. Amory. Kind, sweaty, handsome, helpful. Just like me. We introduce ourselves to this little girl, and then to each other. Her mother is so grateful, when we find her looking for her daughter nearby. Says she really appreciates us, and we make a cute couple. I agree. Which is why I ask him out. And he immediately says yes.

(Ezra pours one cup of coffee into another.)

EZRA: Seriously, have this! I don’t want it. You know how hard it is to find a partner who gets it. The long nights. The secret cases. The mood swings. What we do gets to us, and them. It’s not for everybody. When we win, and help families out, it’s amazing. But when we don’t – well. Amory gets it. He wants great results for his kids, just like we do. I’ve had a lot of boyfriends who couldn’t handle the unpredictability of what I do. The stress of what I do. The risk of what I do. But he always understood. From the start.

(Ezra pours out both coffees in the sink.)

EZRA: I’m lucky. I can barely remember ever having an argument with him, to be honest. Well, I guess that’s not completely true. There was definitely at least one time. The only time, I think. I came home in tears, from a case I hadn’t been able to crack. Little girl named Shannon Brown. Wonderful parents, wonderful siblings, wonderful home. Just didn’t make any sense. Sometimes, this world of ours is unfair. Turn away for a second, and everything changes. Like losing your little girl. The light of your life. At least when there’s death, there’s closure. You know? But that wasn’t something this family ever got, or seemed like they would get. Nothing on CCTV. No eyewitness accounts. Just a missing, presumed dead, little girl. And I couldn’t help it. Once I ran out of leads, and apologized to the family for not being able to help more, I came home, and just sobbed at the kitchen table. For hours and hours and hours. So many hours, actually, that I missed out on Amory getting a teaching award from his school. He came home, sat down, and put his arm around me. Said how sorry he was to see me sad like this. But he also said, “I’m disappointed you weren’t able to come tonight.” “Disappointed.” The word a parent uses with a misbehaving child. And the tone – ooh. I’ve spoken to his classes about what I do before. It was definitely his teacher tone that he used when telling the kids to pay attention, or settle down. And, you know, it wasn’t a tone that he typically used with me. But that’s all he said. He kissed me on the head, went to bed, and didn’t bring it up again. I know it sounds weird to count that as a fight, but for us – it was. I always meant to make it up to him somehow, but work kept getting in the way. Now, I know, for sure, that I didn’t. I didn’t ever make it up to him.

(Ezra eyes the cups.)

EZRA: I’m tired all of a sudden. I probably shouldn’t have poured those out. But I think there might be more coffee in the pot.

(Ezra pours himself another cup of coffee, and takes a sip. He smiles.)

EZRA: I guess I did need that. Why don’t we tell ourselves the truth about things like that? Right. It’s time I let you in on something else. It’s not just the Ramos case that has me down. Amory and I had an incredible dinner last week. New French place, Mes Amis? The steak is…wow. Never tasted anything like it. And the fries? Best I’ve ever had. All they had on the menu, steak and fries. All they needed. We came home, laughing, and smiling after a big bottle of wine. Said we’d have to do that again soon. But we haven’t gone back yet. Because – damn, this is hard – Amory has been missing since that night, two weeks ago. I woke up, alone, and just thought he’d gone to work early, like always. Believe it or not, teachers sometimes start even earlier than detectives do. But when I came home, he wasn’t back. Didn’t respond to my texts all day long. That was odd, but I figured, hey, maybe it was some parent-teacher conference day, or academic development thing I’d forgotten all about. Because I remember a lot of things…most things…but not everything. But once it got to midnight – I knew something was wrong. I was sure he was missing. And I know our rules, 48 hours, so I figured I was on my own for finding him. Yes, I know you would have had my back, but…this felt like something I could totally handle. I do this for a living. Finding missing people. I know how to make this happen. And I didn’t want to come into work, and make it seem like I didn’t have my house in order. So, I started trying to find him, alone. Because I was alone. And I hadn’t been in a really long time.

(Ezra takes another sip of coffee.)

EZRA: The first thing I had to do was sit down and wait for the ringing in my ears to go away. I have this thing, ever since I got into a shootout 2 years back. You remember. I didn’t get shot – I wasn’t that cool – but a bullet flew past my ear, while I was chasing down a suspect. I went to the ER, came out with hearing damage. So now, whenever I get into a stressful situation – even if it’s just personal stress, and not physical – I have to sit down, and wait it out. Tinnitus, is what it’s called. Chief told me I could go to a therapist to deal with that, but I don’t like to have time to go boohoo to some therapist. No offense. How are things with Dr. Lily?

(Ezra winces, and grips his head.)

EZRA: Yep, there it is. Just need to give it a few seconds, and it’ll go away. Ooh. This one is lasting a little longer than usual. Okay. Okay. It’s gone. Whew. Right. So, I started the search for Amory. I followed the usual protocol. Went to the school. Talked to his teacher’s aide, Jenna - or Joanne, I think it was. I don’t remember. I mean, I’ve met her a bunch of times, so I really should know, at this point, but…yeah, I don’t know. I’ve never really been that good with names. I am reliant on my notepad to remember every last witness. That’s not true, actually. Witnesses, I can remember just fine. Civilians, normal people – they’re in and out. Right, so back to…J name. She hasn’t seen Amory since the day before. So, I go talk to the principal to ask some questions. And she didn’t really know what had happened to him, either. Don’t ask me for her name - I seriously don’t know what it is. But the principal’s secretary says that Amory, or someone who sounded like him, at least, called in to request a leave of absence, one day earlier. So that got me really, really worried. Look, I know Amory’s not a kid, you know? But adults get taken all the time. Still, he knew how to be safe. We’d been together for years. So none of this, any of it, was making any kind of sense to me.

(Amory gets up and starts pacing.)

EZRA: I had to dig a little deeper. I called his family. They weren’t answering any of my calls – and I called a lot – which of course made me immediately think that they had something to do with it. His brother Francis, you know, the suit salesman with the really bad taste? He was the one who liked me best out of all them. No, he doesn’t know that I think his suits are bad. And even if he did, I think he’d still be polite. Anyway, I went to talk to him, Francis. Probably says something that I can remember men’s names better than women’s names. Guess I am gay after all. Well, Francis, he seemed really concerned. But all he said to me was, “I would leave it alone.” Leave it alone? Leave it alone? I would not leave it alone. What did that even mean, “leave it alone?” That someone in his family had done something to Amory? “Leave it alone.” That’s like something you hear in a mob movie. Had Amory’s family hurt him? Were a few of them in on it together? He was only a teacher, but he was the only one in his family who worked consistently, so he was worth the most money. I know all this sounds like a conspiracy. I know that. But some conspiracies are proven right in the end. I just didn’t understand why this all wasn’t easier. Didn’t I track down missing people for a living? Missing people to whom I had no connection, at all? Why, when I loved the person who was missing, could I not find even a clue?

(Ezra grips his head a moment, and sits down, till the feeling goes away.)

EZRA: Don’t get me wrong. This was starting to feel like something that I wanted to bring up to you all. But my gut told me it wasn’t quite time yet. There was still an answer I could find on my own. And if I can do something without help – I want to. Amory wasn’t like that. He wanted to do everything together, even complain. But that’s not me, I told him. I think he understood. Anyway, I ran all of Amory’s records I could think of: his car records, his credit card records, his phone records. Heck, even his old stereo records. Backwards and forwards. Anything that could give me a lead on where he was. It was the weirdest thing. I got nothing. Nada. Zip. None of my research turned up anything, at all. I was stuck. For maybe the first time in my career, I had no idea what to do next. But as you know, whenever your ingenuity fails you – luck fills in. I went to pay off my credit card – Amory’s and my joint one – and that’s when I saw that he, or whoever had his card, had already paid it off. And that really scared me. I checked the card’s location – five towns over – so I got to roadtripping. I drove down this lonely country road for what felt like 100 miles. I could have sworn I was driving for days. Finally, I pulled into a long driveway. That’s where I found his car. Now, I’m thinking, “Oh my God. Someone stole his car. Someone killed him. And I’m about to find my boyfriend’s dead body inside this lonely house.”

(Ezra takes a deep breath in, holding his head, before continuing.)

EZRA: I draw my weapon and run up to the door. I kick it in, and there’s a loud scream coming from…Amory. It’s him. He’s there. He’s alive. But, but, how is that even possible? Amory is okay…and he does not look happy to see me. Amory asks, “Ezra? What the hell are you doing here?” “What am I doing here?” I ask. “What are you doing here? I thought you were dead. I thought you were missing. I thought you…” “Amory,” Ezra cuts in, “Did it ever occur to you that maybe I didn’t want to be found?” No. No, it didn’t. “I thought you were dead, Amory.” All he said was, “I wish I were.” I couldn’t even see straight. I thought, what does that mean, you wish you were dead? And that’s when the truth finally came out: that Amory had been miserable for a very long time. So miserable, he hadn’t even known how to tell me. When he tried to explain, I never seemed to understand. Or didn’t remember after. He knew my job as a finder of people meant he couldn’t get away. And even despite all that, he had still tried to disappear, to even have a hope of ending our relationship. Because he knew I wouldn’t give up, if he just broke up with me, like a normal person. Because apparently, I’m not a normal person. But being the great person that he is, he still didn’t want to leave me with a bill to pay it off, not realizing that I’d be able to track his every movement. Like I always could. “Amory…we really can’t work this out?” I asked. Begged, really. “Ezra,” he said, “Do you even know what today is?”

(Ezra finishes the coffee incredibly slowly.)

EZRA: It was my own birthday. Not his. Mine. I got so wrapped up in finding him. I got so wrapped up in finding people, finding truth, that I didn’t remember that it was my own Birthday. And if I couldn’t remember things for myself – well, no wonder he felt ignored. And unloved. I left Amory at the house. He ran away. I guess I did a number on him. Which doesn’t surprise me, because I also did a number on myself. And that’s what I’m going to have to work on from now on. That ringing in my ears. It apparently echoes away with time, but it’s something you actively have to work on. So, I guess that means that I’m going to take care of it. I have to take care of it.

THE END.
```

---

## IC-1438: Screaming Timmy Must Die

- Title: Screaming Timmy Must Die
- Author (byline): Steve DuBois
- Work: Screaming Timmy Must Die
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: CALVIN, DENNIS, NANCY, TIMMY, SPLODEY JOE, GEORGE, SALLY, MISS WATKINS, WOLVERINE, WATKINS, JOE
- Teaser before the introduction: No
- Spoken words (computed): 2354
- Already set (do not supply): none

### Source block (context only)

```text
(none)
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
CAST OF CHARACTERS

CALVIN: An evil eight-year-old. Has an extensive vocabulary.

DENNIS: An evil eight-year-old. Has a nervous disorder.

NANCY: An evil eight-year-old. Has a talent for plotting and a taste for dangerous men.

TIMMY: An evil eight-year-old. Has the loudest and most annoying voice in human history.

SPLODEY JOE: An evil eight-year-old the size of an NFL linebacker. Has the ability to make people explode by pointing at them.

GEORGE: An evil eight-year-old. Has a toy truck.

SALLY: An evil eight-year-old. Has no lines.

MISS WATKINS: An elementary school student teacher. Has had it with these little bastards.

WOLVERINE: A small mammal of no particular moral alignment. Has a brain injury.

#

[Morning recess at Mephisto Elementary School. Calvin and Dennis sit atop the monkey bars, staring down at the antics of their classmates.]

CALVIN: Screaming Timmy must die. His nefarious tactics can no longer be borne.

DENNIS: Indeed, friend Calvin! The death of Screaming Timmy is much to be desired!

CALVIN: Even here at Mephisto Elementary School, the nation’s premier academy for pre-pubescent supervillains-in-training, Screaming Timmy’s loathsome ways stand out. I tell you, Dennis, I despise his smug little face! His brown-nosing! That stupid little sailor suit he always wears! How I long to wrap my fingers ‘round his pudgy little windpipe and squeeze!

DENNIS: Behold! Over by the sandbox! Even now, he prepares one of his vile ambuscades! [GEORGE sits in the sandbox, playing with a small toy truck. TIMMY appears behind him.]

TIMMY: Whassat? Whassat you got there George? [George tries to hide the truck.]

TIMMY: Whassat object George? Whassat object gimmee object I wanna object WHASSAT OBJECT… [Timmy’s voice transforms into a piercing, obnoxious shriek.]

TIMMY: GIMMEEITIWANNITGIMMEEOBJECTGIMMEEGIMMMEEEEEEEEE…. [George covers his ears in agony and pushes the toy truck over towards Timmy. Timmy picks it up, glances at it idly, places it on the ground, and stomps on it. Then he picks it up, hands it back to George, smiles, and skips away happily. George looks down at the remains of his toy, crying quietly.]

CALVIN: George ‘The Ram’ Ramirez, a young supervillain of exceptional power and potential. Yet confronted with the tactics of Screaming Timmy, he is helpless as a kitten.

DENNIS: It is obscene! Action must be taken!

CALVIN: Yes. Yes, there can be no question. Screaming Timmy must die.

#

[Introduction here.]

#

[NANCY enters, climbing up the monkey bars to sit beside Calvin and Dennis.]

NANCY: And what is this? A confederacy, I think. I smell a scheme upon the November wind. A scheme that would rid us all of that most pestilential presence, Screaming Timmy.

CALVIN: What? Nancy? Why…er no! Never! Nothing of the sort! Screaming Timmy is…a beloved friend!

DENNIS: Um…yes! A friend to all is screaming Timmy!

CALVIN: We are in no way troubled by the scent of mayonnaise that follows him everywhere in a reeking cloud!

DENNIS: Why, his window-shattering shrieks are as birdsong to us!

CALVIN: We were merely discussing…um…boy things!

DENNIS: Yes! The performance of…of a local sports franchise!

CALVIN: The salting of slugs. The operation of internal combustion engines. Items of that nature.

NANCY: A futile ruse, gentlemen. The truth is writ bold upon your faces. The demise of Screaming Timmy is indeed your design. But fear not; I shall not reveal your conspiracy. Rather, I wish to join it.

Not one week hence, Screaming Timmy tore the head from my beloved dolly. It is war, war to the last, between Screaming Timmy and I. [Calvin and Dennis glance at each other and reach an unspoken agreement.]

CALVIN: Very well. The three of us—co-conspirators, bound in blood.

DENNIS: No additional recruits, mind you! One word in the wrong ear, and we are undone!

NANCY: I know not why. Who is to object? Mephisto Elementary has an annual fatality rate of nearly forty percent. Many enter into these hallowed halls, but few indeed are those who survive to graduate. Observe. Why, look…even now, by the tetherball poles, the custodial staff gathers the smoldering remains of Fiendish Franklin Flash into numerous small sandwich bags.

CALVIN: Still, it is essentially not to draw the attention of outside authorities to the Mephisto project. To do so is to risk a trip…to the Principal’s Office. [All three of them shudder.]

NANCY: Stealthily, then. To class, my boys. And be watchful for opportunities…

#

[CALVIN, DENNIS, and NANCY are gathered inside the school door leading out to the playground. A huge pile of educational bric-a-brac is perched above the door.]

CALVIN: Behold our wonder of engineering! A towering, teetering pile of desks, folding chairs, school supplies, spent nuclear waste, playground equipment, and janitorial supplies, all held in place above the playground door by a single duct-taped mop handle!

DENNIS: A most impressive edifice!

CALVIN: Why, is that a lightly stunned wolverine amidst the wreckage?

WOLVERINE: [Chitters menacingly]

CALVIN: Indeed! And now this incipient avalanche waits, dangling like a proverbial Sword of Damocles above the unsuspecting head of the odious Screaming Timmy. A tip of the cap to you, respected friend Nancy, on your most cunning scheme.

NANCY: It is a well-established fact that Screaming Timmy insists on being first in every line, including the line to come in from recess. And that shall be his undoing. For when he comes through the door, and dislodges the prop…

DENNIS: Screaming Timmy’s time grows short! Soon his screams shall resound in hell!

CALVIN: But soft, friends! To the window. I hear the clanging of the recess bell. The fateful moment approaches…

[Outside, MISS WATKINS, an overwhelmed student teacher, struggles vainly to shepherd the evil children back inside.]

WATKINS: All right, children, everybody line up by—BOBBY! PUT THAT CHAINSAW DOWN!—line up by grade! No, straight lines, please. Yes, Samantha, I know that space-time is technically curved, but I still need you to…

TIMMY: More recess!

WATKINS: Now, Screaming Timmy, you know that’s not how it works. The bell rings, and we all march back inside. March, march, march. You’ve got social studies next. Won’t that be fun? You’ll get to show everybody that Vlad the Impaler diorama you’ve been—

TIMMY: More recess! WANNA MORE RECESS!

WATKINS: No, now, Screaming Timmy, we talked about this, please, just don’t…

TIMMY: WANNARECESSWANNAMORERECESSAIEEEEEEEEEEEEE…

WATKINS: [Covering her ears] All right! All right! Yes, you can have more recess! More recess for everybody!

TIMMY: No! Just Timmy! More recess for TIMMY!

WATKINS: All right, Screaming Timmy. Just don’t scream, all right? Just you. Recess for nobody else but you. Everybody else, back in your lines. Hold on, I have to go inside and find somebody to supervise Screaming Timmy. I think this is Mr. Okoye’s plan period…

CALVIN: [In a whisper] No! No! This was not the plan!

WATKINS: [Walking back inside, under her breath.] God, that little turd. This whole school! Who ARE these people? I wonder if that bartending job’s still available…oh, Christ, now the door’s blocked. NGGGH! There, that’s got it…AAAAAAAAAH! [She looks up and screams as the avalanche of debris descends on her, squashing her to pulp. Inside, the three conspirators watch in horror.]

DENNIS: Alas! The lovely Miss Watkins!

CALVIN: [to Nancy] This is your fault, you trollop! Your scheme is an abject failure!

NANCY: Me? Who was it that insisted that we delay construction for two days in order for the depleted uranium to arrive? You’ve made a hash of everything, you buffoon! [Calvin and Nancy lock gazes, snarling menacingly at one another]

DENNIS: Comrades! Do not lose sight of the true enemy! Screaming Timmy breathes yet!

CALVIN: Very well. Let us set aside our differences.

NANCY: Acceptable. For the present.

CALVIN: We shall redirect our anger, and redouble our efforts. The next time Screaming Timmy screams, we three shall be the reason.

#

[The playground. Calvin and Dennis stand in a small alcove.]

CALVIN: Where is Nancy? It is unlike our colleague to be late, and she promised us a surprise.

DENNIS: There! She approaches!

CALVIN: But…who is that hulking figure behind her? The one being dragged by the hand, like an ocean liner behind a tugboat? His description matches that of…but…surely not. It cannot be.

NANCY: Gentlemen. [She proudly gestures to the immense boy whose hand she is holding.] I wish to introduce the newest, and most powerful, piece in our game.

CALVIN: Impossible. He is a myth, surely?

DENNIS: Inconceivable! It is said that they keep him in the basement! Inside a vault! Under guard! Strapped to a gurney!

NANCY: Such obstacles are nothing to a girl of cunning and initiative. And what locked door can hold true love inside? It is indeed he. I present to you, my boyfriend…Splodey Joe. [Splodey Joe stares straight ahead, slackjawed.]

JOE: Nggggggggggffff.

CALVIN: A…a demonstration, Splodey Joe! A mere taste of your fabled power! We beseech you!

DENNIS: An aperitif, as it were! To whet our appetites for the feast of carnage to come! [Splodey Joe notices them for the first time, and grunts his assent. In the distance, SALLY babbles aimlessly, gossiping with a group of her friends. Splodey Joe slowly raises his arm and points his finger at her. Sally stops talking, clutches herself in momentary discomfort, and then explodes, showering her friends with red mist. Calvin and Dennis gaze in awe.]

CALVIN: Behold the astonishing talents of Splodey Joe!

DENNIS: I renounce all other Gods! Henceforth I worship only Splodey Joe! [Nancy sighs adoringly and gazes moonily up at Splodey Joe. He stares straight ahead, not noticing.]

CALVIN: It seems that our femme fatale has a crush on our secret weapon.

DENNIS: As do I!

CALVIN: Wait a moment. Do you… [he sniffs] Do you smell mayonnaise? [Screaming Timmy appears.]

TIMMY: Hey! Hey, new kid! Be my friend!

DENNIS: Ecce homo! Behold the man!

CALVIN: Our quarry! Attend, Splodey Joe! There stands your target!

JOE: [Cocking his head to the side in confusion] Grrrrgh?

NANCY: Tee-hee! How amusingly droll you are, Splodey Joe!

TIMMY: I got no friends! Wanna friend! Be my friend, new kid!

CALVIN: Do no such thing! Gaze upon your death, Screaming Timmy!

DENNIS: Strike now, Splodey Joe! The time is ripe!

JOE: [Glances back and forth between the four of them in total bewilderment.] Mwrrf?

TIMMY: GotnofriendsbemyfriendwannafriendWANNAFRIENDBEMYFRIEND

JOE: [Places his hands over his ears, groaning in pain.]

CALVIN: Be not deterred, Splodey Joe! End your pain, and ours!

DENNIS: Obliterate him, Splodey Joe!

TIMMY: WANNAFRIENDBEFRIENDWANNAFRIENDBEFRIENDWANNAFRIEND [Clutching his ears in agony, his eyes uncomprehending, Joe raises his finger to point at Timmy, then at Calvin, then at Dennis, then at Nancy, then back at Timmy. Finally, he points his finger at himself. There is a massive explosion. When the debris clears, all five of the other children are drenched in red mist.]

NANCY: [Stares down the remains of Joe all over herself, then throws back her head to the sky.] NOOOOOOOOOOOOOOOO! SPLODEY JOE!

TIMMY: [Wipes a palm across his face, stares at it for a moment, then licks it and smiles.] Thanks, friend! [He skips away merrily.]

DENNIS: A substantial setback!

CALVIN: [Pulls out his shirttail, cleans his glasses on it. Struggles for words. Finally manages:] O infamy.

#

[Calvin, Dennis, and Nancy are gathered on the roof of the school, overlooking a drop to the blacktop below.]

CALVIN: I gather you together for the final time, my comrades. From up here on the school roof, we can see far—and one of the things we must gaze up on stark reality. None can stand against the machinations of Screaming Timmy. The day is his.

DENNIS: Pish and tosh! Why, there are stratagems yet unexplored! Retroviral engineering! Giant robots! Spitwads!

CALVIN: Nay. Against a lesser opponent, such schemes might prevail. But not against the all-conquering tactical juggernaut that is Screaming Timmy. In any case, we have no-one capable of designing the blueprint for any such scheme. Our master planner has been rendered nearly catatonic by her tragic loss.

NANCY: [Staring morosely into the distance.] Farewell, my sweet. Farewell forever, Splodey Joe. [She pulls out a juice box, and inserts a straw.] A last libation for our lost love. [She pours out the juice box onto the roof].

CALVIN: So this must conclude our partnership, I fear. It was a worthy and noble effort, but we have failed to… [he sniffs the air] …wait a minute… [Screaming Timmy appears.]

TIMMY: Hey! Why you guys up here on the roof? Shouldn’ be up here! I’m tellin’ the teacher! I’m tellin’ the PRINCIPAL!

DENNIS: Scalawag! Mountebank! Most despised Screaming Timmy!

CALVIN: Wretched boy! Is there no avoiding you? Is there nowhere we can go to be relieved of your insufferable presence, you ever-present kidney stone in our collective urethra?

TIMMY: [Frowning] Why you guys talk that way? You always talk that way. All threea you. All those big words. Shouldn’ talk that way. Gives me a headache. [A long pause. Slowly, Nancy rises from her seat overlooking the blacktop.]

NANCY: Oh, it does, does it?

TIMMY: Yeah! Long words. Weird words. Don’ like ‘em.

CALVIN: Why, Screaming Timmy. Did you never wonder at our presence, here at Mephisto? Did you never ask yourself why we three, with no evident powers, would be placed at this special institution for genetically gifted avatars of evil? Know then, Screaming Timmy, that our specific gift, the skill with which we shall conquer the world, is monologuing.

NANCY: Monologuing and scheming!

DENNIS: Monologuing and scheming and general twitchiness!

TIMMY: Yeah…well…you stop. Don’ like it.

CALVIN: Oh, I think not. I THINK NOT, SCREAMING TIMMY! I think our monologuing, our vocabularial manipulations and meanderings, shall be GREATLY ENHANCED henceforth! For no simpering delinquent such as yourself can still the tongue of the illustrious Calvin Cruel!

TIMMY: Shut up! Shut up, meanies!

DENNIS: Never! Dread the dolorous dictations of Menacing Dennis!

TIMMY: Shut up! [He begins racing around the roof in circles, eyes shut and hands over his ears.] SHUTUPSHUTUPSHUTUP!

NANCY: Shudder, malignant twerp-turd, at the loquacious lexicon of Nancy Grue!

TIMMY: BADWORDSMEANWORDSSHUTUPSHUTUUUUUUUUUU…. [Eyes still shut, Timmy races straight off the edge of the roof, and plummets to the blacktop below. The three conspirators stare down after him.]

CALVIN: Thus ends the contemptible reign of Screaming Timmy.

DENNIS: Sic semper screamers!

NANCY: I feel we have learned a valuable lesson today. Even in the face of seemingly insurmountable obstacles, a boy or a girl can succeed. All that is required is teamwork, belief in one’s self, and a complete disregard for human life.

CALVIN: And perhaps a thesaurus.

DENNIS: Seventh period next. Arts and crafts!

CALVIN: Excellent. To the classroom, my friends! I feel a powerful hunger for paste.
```

---

## IC-1439: Sibling Rivalry

- Title: Sibling Rivalry
- Author (byline): K.R. Schneider
- Work: Sibling Rivalry
- Publisher: Mushroom Cloud Press
- Publication date as stated: December 11, 2023
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: TIM, TOM, BOTH, TIM & TOM, NANCY
- Teaser before the introduction: No
- Spoken words (computed): 1865
- Already set (do not supply): none

### Source block (context only)

```text
(none)
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
K.R. Schneider

[Two brothers, Tim and Tom, have not seen each other in ten years. After their father dies, they have to come home for the reading of his will.]

(Both brothers are getting ready to leave their respective homes; they stand facing opposite directions, each packing toiletries in a bathroom.)

TIM: Honey, have you seen my black shirt? (pauses to listen) Can’t I go without a tie? I hate wearing a tie!

TOM: Laura, did you call the financial advisor? (pauses to listen) And you packed my good cufflinks?

BOTH: I heard you; I’m almost ready!

TIM: I have to see my stuck up, jerk brother.

TOM: I have to see my underachieving, clown of a brother.

(Both turn to “look in the mirror” but are facing each other, treating the other as their own reflection.)

BOTH: I guess it’s what dad would have wanted.

(TIM and TOM sit in chairs facing opposite directions, driving their respective cars home for the funeral - each on the phone with their mother. They freeze when the other has a line.)

TIM: Hey, Mom. I’m about twenty minutes out. Tommy there yet?

TOM: Hi, Mom. No, I’ll be early. Timmy there yet?

TIM: Of course he is. He get your taxes done already too?

TOM: Yeah. That about figures. I’m sure he’ll come rolling in late.

TIM: I’m sorry. He just has to one-up me all the time!

TOM: I’m sorry. It’s just typical Timmy. Never on time.

TIM: I’ll be as nice as he deserves, how about that?

TOM: I’ll do my best to keep the peace, but if I hear one joke about a busload of preachers in the apocalypse…

TIM: I’m just saying, we’ve never been close, Mom. If he doesn’t talk down to me, I won’t punch him.

TOM: He did tell that joke! At Grandpa’s funeral!

TIM: Okay, okay. I promise I’ll try.

TOM: I know. I’ll do my best.

TIM & TOM: See you soon, Mom. Love you too.

(TIM is entering the kitchen backwards, yelling back to the car at his wife; TOM is seated at the kitchen table.)

TIM: Honey, just leave the bags; we’ll get ‘em later! Don’t carry that one. That’s the heavy one!

TOM: Still leaving the heavy lifting for your lady, I see.

TIM: (turns and takes in the way that Tom is sitting - with his legs crossed) Still sitting like a teenage cheerleader, I see.

TOM: (uncrosses his legs) Mature, Timothy.

TIM: (mocking him) Haughty, Thomas.

TOM: (leans in to shake his hand awkwardly) So. How are you? Are you well?

TIM: Am I well? We haven’t spoken in ten years, and that’s your opener?

TOM: What would you prefer? Punches thrown?

TIM: Might be a little more sincere. But since you asked, no. My dad’s dead, Tommy. So no, I’m not well.

TOM: Hey, he was my dad too!

TIM: And clearly you’re doing well with things.

TOM: He was my dad too.

TIM: He was my dad first, skunk-hole.

TOM: Wow. Well, you’re still charming as ever, Tim.

TIM: You’re still a prissy little girl, Tom.

TOM: I tried to be civil. I guess maybe that was too much to ask for from someone like you.

TIM: I’m sorry, someone like me?

TOM: You’re a loser, Timmy; you’ve always been a loudmouthed loser.

TIM: Oh, really? As I recall there were a few occasions when you needed this loudmouthed loser to pull your duct taped little nerd butt off of your locker.

TOM: One. One occasion! And it wasn’t my locker, it was the oak tree on the quad!

TIM: Well catch my carp, Tommy, that’s much more respectable.

[FLASHBACK: TOM, as a cruel prank, has been duct taped to a tree in the school’s outdoor area. TIM has come outside to sneak a cigarette.]

TOM: Tim, hey! Tim? Hey, over here!

TIM: Hi Tommy…(taking in the scene) how’s lunch?

TOM: (sarcastic) Fantastic.

TIM: Mmhhm. (pulls out a pack of cigarettes from his pocket) Ya look a little...tied up.

TOM: Yeah, nothing gets by you, Timmy.

TIM: You uh...protesting the cafeteria food or something? (lights a cigarette)

TOM: Can you just cut me down, please? Wait, are you smoking?

TIM: Well, yeah. I didn’t come out here to rope myself to the rose bushes.

TOM: That’s disgusting, you know. Nobody wants to kiss a smoker.

TIM: Wasn’t really planning on kissing you, Tom.

TOM: Shove it, okay? Obviously I meant girls. Girls don’t want to kiss a smoker.

TIM: Yeah, how’s not smoking helping your game? You get an extra kiss from Grandma?

TOM: For your information, I do just fine thank-

TIM: Yeah. I’m sure you do, Tommy. Well this has been fun, but Biology waits for no man, so...

TOM: Wait! You have to cut me down.

TIM: Do I? Do I really? I mean you give me hell about my habits, even though it’s lucky for you really that I came out here, and then you talk down to me, and now you want my help?

TOM: Yes.

TIM: Yes what?

TOM: Yes, please? Come on, Tim!

TIM: I actually prefer that you call me Master and Commander.

TOM: You’ve got to be kidding me.

TIM: “You’ve got to be kidding me, Master and Commander.”

TOM: Just cut me down, you idiot! (Tim moves to walk away) Okay, okay. Cut me down, (mumbles “master and commander”)

TIM: I’m sorry, Tommy, I just couldn’t quite make that out.

TOM: I said cut me down, Master and Commander.

TIM: Oh gosh, man you flatter me. Happy to!

[PRESENT: TIM & TOM are sitting in the kitchen of their parents’ house.]

TOM: You were a jerk.

TIM: I’m sorry, I think you mean, “You were a jerk, Master and Commander.”

TOM: Shove it, Timmy.

(TIM shoves the side of TOM’s head - TOM pushes TIM back - they start a shoving match)

TIM: Hey, what the hell, man?

TOM: You shoved me!

TIM: You told me to!

TOM: Tim, obviously I didn’t mean for you to shove me!

TIM: You said shove it. I shoved it.

TOM: This is sophomore homecoming all over again.

TIM: What does that mean?

TOM: You went home with my date!

TIM: You told me to!

TOM: Tim!

[FLASHBACK: The homecoming dance. TOM is sitting at a table with his date, NANCY - Tim imitates Nancy.]

NANCY: Your brother is a senior right?

TOM: He’s a junior.

NANCY: Do you guys like, hang out all the time?

TOM: Me and Tim?

NANCY: Yeah does he like, drive you places and take you to parties and stuff?

TOM: Tim? Nancy, have you met Tim?

NANCY: He seems like he’d be such a gentleman, you know? Tom, you’re so lucky to have a brother like Tim.

TOM: Last week he tried to chloroform me with a dirty gym sock.

NANCY: That’s funny! Oh my gosh, Tim is so funny, right?

TOM: I’m not sure that’s the adjective I’d employ.

NANCY: Huh?

TOM: Nothing, nevermind. Hey, don’t you have to take pictures for the yearbook tonight?

NANCY: Oh, right! I’ll be right back. If Tim comes over, tell him I said hi.

TOM: Sure.

[The boys switch places. Tim goes back to being himself]

TIM: Hey, man. Rad dance right?

TOM: I don’t know; I haven’t danced.

TIM: Why not? I saw you walk in with Nancy Jergens; she’s hot.

TOM: Yeah, actually I feel more like I’m here with you.

TIM: No, Tommy. I’m here stag. Stag is cool, you know? Playing the field.

TOM: Yeah, I know. Nancy said it’s “sooo cool to come without a date; like how brave is that?”

TIM: You came with a date.

TOM: I know.

TIM: Your date is Nancy.

TOM: Yeah, Tim. I know that. Honestly, she’s spent enough time talking about you tonight that we might as well switch places.

TIM: What, like me go home with Nancy and you go solo?

TOM: Yeah, honestly it might be better than having her as my date.

TIM: (slaps Tom on the shoulder) Happy to take one for the team, man.

[PRESENT: Their parents’ kitchen.]

TIM: You asked me to take her home!

TOM: I was bonding with my brother! I thought you were just trying to show moral support!

TIM: No, Thomas, obviously I wanted to make out with your date!

TOM: Obviously.

TIM: If it makes you feel any better, I cut my lip on her braces.

TOM: No, wildly Timmy, that actually does not make me feel any better.

TIM: Oh. Cause I kissed her?

TOM: Yup.

TIM: I mean it was like a million years ago.

TOM: It’s the principle of the thing, Tim!

BOTH: (to Mom offstage) We’re not fighting!

TIM: We’re fine, Mom!

TOM: We’re great.

TIM: Come on, Tom, it’s not like all of our memories are bad, right? I’ve done nice things for you.

TOM: You mean like the time you locked me out of the house in my underwear in January, and I caught pneumonia?

TIM: Okay, that’s a bad example. But I sold all of your boy scout popcorn that year!

TOM: Because I was bed-ridden!

TIM: I still did it. I sold so much popcorn, you won that ten-speed you wanted.

TOM: Yeah. That was a great bike.

TIM: Neon green with the black stripe. It was a sick bike, man.

TOM: You made me ramp it off the playground slide.

TIM: You got some air on that ramp!

TOM: I broke my wrist. And I sliced my chin open. (points to his chin) I still have the scar!

TIM: Yeah, and I rode you to the hospital on my handlebars!

TOM: (starting to lighten up) Yeah. Yeah, I guess you did.

TIM: I wasn’t the worst brother all the time.

TOM: You put a snake in my bed.

TIM: I didn’t say I was perfect, Tom. And you put a mouse trap in my slippers; that was way worse!

TOM: You woke Dad up after a night shift, and I was grounded for like two weeks.

TIM: You put a mouse trap in my slippers!

TOM: Okay, yeah. I’ll take that one. That was my fault.

TIM: See, I’m not always the bad guy. Remember the time you pushed me in the lake?

TOM: I’m pretty sure you hooked me in the head with your fishing pole first.

TIM: Details…

[FLASHBACK: The boys are pre-teens, at the lake together. TIM is teaching TOM how to cast a fishing pole.]

TOM: Okay, so I just hold this down, and then...fling it?

TIM: No, here, like this.

(Tim demonstrates a proper cast.)

TOM: Okay, cool. I got this now.

TIM: Yeah, you’re a real man now, Tommy. Can cast a fishing pole and everything.

TOM: Thanks. For showing me, I mean. Thanks.

TIM: Okay, I’ll be down the bank a bit; holler if you need me.

(Tim walks a few paces away, his back is to Tom, to cast his pole. He throws his line back too far and snags Tom’s head on the upswing.)

TOM: (screaming in pain) HEY! (Tim pulls the pole) HEY!

TIM: Hold on; I’m snagged on something here. (pulls harder)

TOM: Timmy stop it! My head!

TIM: Stop wailing Tommy, I’ll help you in a second; I’m snagged here.

TOM: YOU ARE SNAGGED IN MY FLESH!

TIM: (turns, realizes what has happened) Geez, Tommy! Why didn’t you say somethin’??

(Tim rushes over to help.)

TOM: You have GOT to be kidding me! I was screaming! You HEARD me.

TIM: Well, I heard you wailin’; I just thought you had a fish or something.

TOM: (gets the hook out of his scalp) ARE (shoves him) YOU (shoves him) KIDDING ME?

TIM: Hey, what the hell, man! Quit shoving me.

TOM: You caught my scalp on a lure!

TIM: (shoves back) Not on purpose!

TOM: You yanked it in!

TIM: Well that’s what you do when you’re snagged, Thomas!

(Tom shoves Tim into the lake.)

[PRESENT: Back at their parents’ house.]

TIM: It was not necessary to shove me into the lake.

TOM: Tim, if I had a dollar for all of the scars you’ve caused me.

TIM: All you ever are is mad at me; I don’t even know why I try!

TOM: Because you’re a pain in my neck at every turn!

TIM: What about the time I won on that scratch ticket? And I split the money with you!

TOM: You owed me that money after I bailed you out of jail!

TIM: Oh. Right. Well, I got you out of your relationship with Molly. She was awful.

TOM: You’re not seriously calling that a favor.

TIM: Yeah, man. She was terrible. I totally got you out of that.

TOM: You hooked up with her.

TIM: For YOU.

TOM: Gee, thanks, Tim.

TIM: Yes. You’re welcome. Finally, some appreciation.

TOM: You can’t be serious.

TIM: What?

TOM: Just forget it. Look, neither of us are perfect, okay? Let’s just forget it, and get through the next couple of days.

TIM: Fine. We’ll try to get along. You know, I actually brought you something.

TOM: Yeah? That’s funny; I have something I need to give you too.

(Each of them pulls out a box to give to the other - they open them at the same time.)

TIM: A watch?

TOM: A knife?

BOTH: Dad gave it to me.

(They look at each other in surprise.)

TOM: He gave me that watch when I turned eighteen.

TIM: When I…became a man...

BOTH: And I wanted you to have it because…

(again, look at each other strangely)

TOM: Dad said it was

TIM: ...his most prized possession.

TOM: Yeah. And obviously it was really the watch because...I mean - well, I was Dad’s favorite.

TIM: Uh, no. I was definitely Dad’s favorite.

TOM: You’re delusional!

TIM: You’re an idiot!

TOM: Great comeback!

TIM: Great sweater vest!

(They start to physically scuffle.)

TOM: Shut-up.

TIM: You shut-up.

TOM: Make me.

TIM: Oh, gladly.

(pause their scuffle when Mom calls in from the other room - TIM has TOM in a headlock)

TOM: No, mom! We’re fine.

TIM: We’re good!

BOTH: We’re not fighting!
```

---

## IC-1440: So You Want to Date a Superhero

- Title: So You Want to Date a Superhero
- Author (byline): Kevin J. Burgun
- Work: So You Want to Date a Superhero
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2262
- Already set (do not supply): none

### Source block (context only)

```text
(none)
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
CHARACTERS

Announcer Male or Female.

Taylor Williamson Game show host. Male or Female.

Dana Super hero. Looking for a date. Female

Steve Contestant. Male.

Trevor Contestant. Male.

Ryanne Contestant. Mousy. Female.

SET

Can be a bare stage. Needs at least a divider of some type between Dana and the contestants. Taylor could have a podium, but not necessary. Should have the feel of a dating game set-up.

AUTHOR’S NOTE

The key to this show will be facial reactions from the various actors. It is important that Ryanne be as one-note as possible.

SO YOU WANT TO DATE A SUPERHERO?

(Lights come up. DANA sits CS; STEVE, TREVOR,

RYANNE sit SL. TAYLOR is SR.)

ANNOUNCER It’s time, once again, for everyone’s favorite dating show (alone or with audience) “So You Want to Date a SuperHero”! And here’s your host, Taylor Williamson!

TAYLOR I am your host, Taylor Williamson. Today we have on the show Princess Diana, oh wait, sorry, Dana. Dana?

DANA It’s Dana. A common mistake.

TAYLOR For a second I thought you were…

DANA No.

TAYLOR But you sort of look like…

DANA It’s Dana. Princess Dana.

TAYLOR Right you are. And where are you from, Dana?

DANA Themyscira. (Beat.) Indiana.

TAYLOR There’s a Themyscira, Indiana?

DANA Yes.

TAYLOR Really?

DANA Look, there’s an Olympia Washington, a Sparta Georgia….

TAYLOR Ok, Ok, We get it. What sort of date will our lovebirds be going on?

ANNOUNCER Taylor, our newly branded couple will be eating dinner at a lovely little diner in Hell’s Kitchen, situated nicely in the middle of a ninja training facility, a secret, government black site for extremely dangerous villains, a radioactive insect and animal lab, and finally a newly opened cupcake shop.

TAYLOR Fantastic. Let’s meet our contestants. Contestant one?

STEVE Hi Taylor! My name is Steve.

TAYLOR Steve, I really like your energy, you seem pretty excited.

STEVE I’m over the bar scene and going home with a different woman every single night. I’m ready to settle and find true love. And if she’s a millionaire super hero, all the better.

TAYLOR Whoah, have a hard time affording breakfast for two there Steve?

STEVE I’ve never had one stay for breakfast, they always sneak out in the middle of the night. Usually with my watch. Or wallet. (Emotional.) One time my dog.

TREVOR

(Reaching over and putting hand on Steve’s shoulder.) I’ve been there, man. I’ve been there.

TAYLOR

(Long Pause.) Well, umm, let’s go straight to contestant three.

RYANNE Hi, Taylor. And just for the record, I’ve never stolen anyone’s dog. Or wallet.

TREVOR He also said watch.

RYANNE I heard.

(Pause.)

TAYLOR So, Ryanne, you are a girl.

RYANNE Yes.

TAYLOR I feel as if our producers thought you were a boy.

RYANNE Because of my name?

TREVOR I was wondering why a chick was sitting there.

STEVE I thought this was one of those new shows that rejects the gender normative standards of the past.

TREVOR Oh.

TAYLOR Dana, you ok with Ryanne being here?

DANA I’m not going to alienate an entire fan base, so I’m cool with that.

TAYLOR Great. And contestant number two.

TREVOR Trevor.

TAYLOR Ok, now let’s…

TREVOR Uh, I have a quick question.

TAYLOR Ok, Trevor.

TREVOR Can we get a quick rundown of what we are dealing with, in terms of powers here? Am I safe? And she isn’t one of those wake up with nightmares and like stab me in my chest accidentally types?

STEVE Tortured hero, right. I would also like to hear that. Yes. And any sort of weapons she may have. Swords. Guns. Electric billy clubs. Fusion weapons that could explode me if I were caught cheating or lying. Things like that.

TREVOR Does she have powers where she can’t touch anyone or they die?

STEVE I need hugs.

TAYLOR Great questions. Dana?

DANA I am optimistic. I’ve been told annoyingly optimistic at times. Not tortured. Yet. I have super strength. Pretty strong. I’ve never accidentally stabbed anyone. And I can touch things.

TREVOR What kind of things do you like to touch?

STEVE Can you lift a car?

DANA Easily. And the only weapon I really have is a lasso.

TREVOR I could get on board with that.

STEVE Yeah. Um, do you like tying things up…or…ummm….you know….

TREVOR Being tied up?

STEVE What Trevor said.

TAYLOR Gentlemen, gentlemen. (Pause.) I kinda want to know now, too. Dana?

DANA I like tying other people up with it…(Steve and Trevor fist bump)…because my lasso is magic and makes whoever is tied up with it tell the truth.

TREVOR Well damn, Dana. That really does not sound like fun at all now.

STEVE I knew there had to be a catch. Magic. Freaking magic.

TAYLOR Ryanne? You’ve been pretty quiet.

RYANNE I think honesty is important, and I like telling the truth.

TAYLOR Dana, do you have a question for your potential dates?

DANA Yes. In the past, the person I’m dating usually gets caught up in my adventures. Are you open to that? Being part of adventures?

TAYLOR Great question. Let’s start with Trevor.

TREVOR Without a doubt. What would we be doing? Drinking wine under the setting sun in Tuscany?

DANA Ok. Here’s a typical situation. I am fighting fifty bad guys with my sword and shield…

TREVOR I thought you just had a lasso?

DANA And a sword. And a shield. And sometimes my tiara can act like a boomerang.

STEVE You sound violent.

DANA So, inevitably, I lose my sword in the middle of the battlefield, but I need my sword in order to defeat the boss.

TAYLOR Obviously.

DANA Are you willing to run out into the battlefield, grab the sword, and throw it to me just as you are being knocked out or taken out by aforementioned bad guys?

TREVOR What sort of weapons do the bad guys have?

DANA AMP-69’s firing 7.62x39mm cartridges with a few Barrett REC7’s firing the 6.8mm Remington special thrown in to make things interesting.

STEVE

(Giggles) She said “69”.

TREVOR And I have to run out, grab your sword? And then what, run it over to you?

DANA It’s more dramatic if you throw it, like in an arc.

TAYLOR Do you not watch any superhero movies, Trevor? Dana, will you also be requiring the AAAAAAAAAAUGH noise whilst he is throwing.

DANA Of course. I like it when my man giving me the sword is vocal. The louder the better.

RYANNE Man?

DANA Person.

STEVE If I can interject here for a moment. Can bullets hurt you, Dana?

DANA No.

STEVE Then why don’t you just go out and grab your sword?

DANA That undercuts the moment, Steve. Someone who can die needs to do it, to inspire me.

RYANNE I’d inspire you.

TREVOR So I just do all of that, risk my life to inspire you?

DANA For that particular moment, yes. Heroes need inspiration, otherwise we would just sit around all day in our pajamas eating ice cream and watching Judge Joe Brown [Feel free to change Judge Joe Brown to any judge or talk show. Region-specific is best.]

RYANNE I love that show.

STEVE Pajamas? Are they silky?

TREVOR So, I just need to risk my life? I’ll be safe?

TAYLOR (Grimaces) You need to catch up on your Netflix.

DANA Well, if you actually die, flinging me the sword with your last breath? That would be fantastic. Especially if we had eye contact as the bullets exploded through your body. Do you think that could happen?

TREVOR Wait, what?

STEVE You want us to die?

DANA I don’t want you to die. But that’s the whole point of being my romantic interest.

TREVOR Taylor, what the hell is going on here? Is this like the Purge, or a dating show?

TAYLOR Absolutely a dating show. But she’s a super hero. That’s the show. And there are expectations.

STEVE Hold the door open. Hold the umbrella. Hold in the fart. Those are dating expectations.

TAYLOR If you don’t have powers and are the romantic interest of a super-hero….you are going to die.

DANA To provide inspiration. You die reminding me to keep fighting for the regular people.

RYANNE That sounds very noble.

STEVE You are out of your mind.

DANA My last romantic interest died a hundred years ago. That’s why I need renewed inspiration.

TREVOR WHAT?

DANA In a plane explosion.

TAYLOR Tragic.

RYANNE Did he throw you your sword?

DANA No, but he saved many lives. Very heroic.

STEVE Hold on. Just. We have two things going on here.

TREVOR One hundred years ago? How old are you?

DANA Two thousand two hundred and twenty-nine.

STEVE Taylor, is she all shriveled? I can’t do all shriveled. Dana, you better not be bald.

RYANNE I don’t care.

TAYLOR She is looking great from where I’m standing.

TREVOR How many boyfriends have you had?

DANA Boyfriends? Just the one.

STEVE So one hundred percent of your boyfriends have died fiery deaths?

DANA Yes.

TREVOR And this happened one hundred years ago?

DANA Yes. It took a long time to move on.

TREVOR And you want us to die so you can be inspired?

DANA No! Again. I don’t want you to die. That’s just the way things have to go. You seem very opposed to this idea of dying a long, torturous death.

TREVOR Torturous?

DANA The more cruel and painful the death, the more inspiring it is. That only makes sense.

TREVOR I’m tapping out.

TAYLOR Oh, too bad, Thanks for playing, Trevor. Steve, still in?

STEVE I’m not out yet. She sounds hot. And, I’m guessing that it’s better if we know each other a long time, so she can get really attached to me, and then I die?

DANA Yes. The deeper I fall in love, the better.

STEVE So, I’m gonna gamble here. Date her for six months, then break up. Free and clear.

TREVOR I didn’t think of that, I’m back in.

TAYLOR Ouch, you didn’t read the fine print, Steve.

STEVE Fine print?

DANA An ex is the one who is kidnapped, beaten, and tortured in a bid to get me to give up whatever the bad guys need to complete their plan. I feel guilty, so I have to come and rescue you.

STEVE Oh.

TREVOR And I’m back out!

STEVE But, I don’t die?

DANA No, of course not. I’m a hero. I always save the kidnapped person right before they die.

STEVE You sound pretty hot. It might be worth being kidnapped to be with you for six months.

TAYLOR I feel I have to point out, Steve, that you will probably be kidnapped multiple times over the course of your life.

STEVE I’m still in. I’m an instant gratification sort of guy.

TAYLOR Ryanne, as usual, you’ve been pretty quiet this entire time. As if you have no personality at all and are just sort of existing. Is it for a particular purpose? We don’t know yet. Are you still in? Remember death is on the table here.

RYANNE I’m in. I think that having the entire purpose of one’s life to be to die just to serve as an inspiration for a hero for a bit is a life well-lived.

TAYLOR Interesting life philosophy there, Ryanne. What do you do for work?

RYANNE I’m in refrigeration, actually.

TAYLOR Really? Odd choice. Good pay?

RYANNE I just love refrigerators.

TAYLOR Who doesn’t? Ok, Dana. We are down to Steve and Ryanne. Trevor is out.

TREVOR Hold on…totally spaced an important question: What’s your costume like?

DANA Ummm, like really high boots, super short skirt, and my top sort of is like an armored corset.

TREVOR Yeah, I’m back in.

TAYLOR Welcome back. Dana?

DANA Well, I like Steve’s plan to break up with me after six months. I’ve never had an ex to save from being kidnapped, and that sounds like fun. I think I’d like the whole “I miss you, but we can never be together” speech after I rescue him. Lots of good drama there.

STEVE Yes!

DANA But, I am a little worried I won’t really fall deeply in love with him if I know his plan.

TAYLOR Good point.

DANA I feel like Trevor is more the person who I have a one night stand with, and wake up to an empty bed, and learn a harsh lesson about all that is wrong with men. Sort of like a challenge to my normally sunny, optimistic disposition. But I overcome it, and choose to focus on the good I see.

TREVOR I’m comfortable with that role in your life.

DANA I feel like I can find that anywhere though. Men are mostly dirty pig boys.

TREVOR Not true! Not true. I can promise you to sneak out in the middle of the night. And never contact you again. A lot of guys will say that, but then a month later they are texting you all like, “what’s up” or pretending they are texting someone else “don’t forget to pick up the bread”, you know?

STEVE That’s true.

TAYLOR Good point. Dana?

DANA I’m sorry, Trevor. I am not picking you today.

TAYLOR Steve or Ryanne?

STEVE I’d love to be kidnapped. You’ve never had that experience. Here’s your chance.

DANA I’m going to go with Ryanne, actually.

RYANNE Yes!

TAYLOR Surprising choice. You went with the one-dimensional character.

DANA She only has one purpose for existing, so I think that will work out great.

TAYLOR Can’t argue with that logic. (Dana and Ryanne come front to hug and talk soto. Trevor and Steve talk soto. To Audience.) Tune in next week when we have a new super-hero, he’s tortured, he’s dramatic, he’s (pause) blind? (Taylor turns to talk to Dana and Ryanne.)

FADEOUT
```
