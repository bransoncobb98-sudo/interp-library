# Classification request: batch 20 of 53 (40 records, IC-1161 to IC-1200)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-020-reply.json`.

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

## IC-1161: Inner Baby

- Title: Inner Baby
- Author (byline): Eric Bogosian
- Work: Pounding Nails in the Floor with My Forehead
- Publisher: Doubleday Books
- Publication date as stated: April 1995
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1415
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric Bogosian
Book: Pounding Nails in the Floor with My Forehead
ISBN: 1568651368
Publisher: Doubleday Books
Date(Month/Year): April 1995
```

### Introduction (context only: never use it for content warnings)

```text
When we were 3 or 4 we couldn’t look around us and say “Well, Dad ís a drunk and Mom is real depressed and scared - that is why it feels so awful here. I think I’ll go get my own apartment” Our parents were our higher powers. We were not capable of understanding that they might have problems that had nothing to do with us. So it felt like it was our fault. We need to take responsibility without taking the blame. We need to own and honor the feelings without being a victim of them. We need to rescue and nurture and love our inner children - and STOP them from controlling our lives. STOP them from driving the bus! Children are not supposed to drive, they are not supposed to be in control. History has been, and is being, made by immature, scared, angry, hurt individuals who are reacting to their childhood wounds and programming - reacting to the little child inside who feels unworthy and unlovable.

That ends today with Eric Bogosian’s Inner Baby . . . .

Stride out onto the stage, arms stretched out, to applause. In a mild Southern accent.
```

### Performance text (classify this)

```text
Thank you! Thank you so much! I am so happy to see so many happy, smiling faces in this audience here tonight. I am turned on by the potential for change I feel in this room. I can feel it coming up out of the audience, into my legs, my body, my head. I am exploding with the power of change in this room tonight!

You know, I go all over this great country of ours, talking to audiences just like you, about change, about human potential. And everywhere I go, people ask me the same question, they say, "Phil. . . what is the secret of happiness? What is the secret of joy? Of ecstasy?"

And everywhere I go, I tell people the same story. I tell them a story about a little boy who went into a candy store and all he had was a nickel. He went into that store and he picked out the candy bar he wanted more than any other. And he said to the man behind the counter, "Sir, I would like that candy bar right there. Here is my nickel.” And the man looked down at the little boy and the little boy's nickel and he said, "Son, that is a ten-cent candy bar. I’m sorry, I can't sell it to you?' And the boy was disappoint-ed by this news. But he thought and he thought and he thought and he came up with an idea. He said, "Why don't we compromise? I’ll give you my nickel. We can take that candy bar, cut it in half, I’ll have half, you have half for yourself. How 'bout that?"

And the man said to the little boy, "Son, that is a ten-cent candy bar. Get your skinny [butt] out of my store. Get yourself another nickel and I will sell it to you.” And with that the man turned his back on the little boy.

And the little boy felt terribly rejected and cut off and abandoned. And he looked up at the man's broad back and he looked at the nickel in his hand and then he looked at the candy bar he wanted so much. And he reached out and touched the candy bar. And then he reached out and he held the candy bar. And then he ran out the store with the candy bar.

And as he was running down the street, he realized something: He still had his nickel in his hand! And in his other hand he had a whole candy bar! And he was suddenly filled with a tremendous feeling of happiness and joy and ecstasy. Now let me ask you something: When was the last time you felt that good? I bet you can't even remember.

You wanna know something? I feel that good every day. I feel that good every day because I am in touch with something deep inside of me. And I’m going to show you how to get in touch with the same thing deep inside of you.

You see, a few years ago I was in a very bad place in my life. Like most of you here tonight I was severely depressed, I was virtually suicidal. And I had to do some serious soul searching.

One day, I was searching around in my soul, and I heard a little voice behind me. It said: "Hi Phil, remember me?" And I turned around (I was in my soul of course), and there on the floor of my soul was a little tiny baby. I had discovered my inner baby within!

You see, I have a baby inside of me and that baby needs to be picked up. That baby needs to be coddled. That baby needs to have things go its own way once in awhile. It needs to cry. It needs to [pee] on people, it has to throw up on people. That's my inner baby within.

And the miracle is, every single one of us here has a little tiny inner baby inside of him or her. I don't care how old, or ugly, perverse or disturbed you might be, you were once a sweet, little, adorable, happy little baby. That baby is inside you right now.

That baby is talking to you, but you're not listening. Let's listen to our babies for a moment. Let's listen to my baby. What's my baby saying? "Mommy' Hear that? "Daddy” "Barney” My baby wants to get out, watch some TV!

Come on now, I want everybody to reach down and pick up his or her little baby. Go ahead, don't be afraid! Put your baby on your lap. And I want you to think about little babies.

Ever watch a happy baby playing? They don't worry about tomorrow, they don't worry about yesterday. They don't worry about hurting other people's feelings. They don't worry about being responsible on the job or driving too fast or smoking too much. They don't read the newspaper, they don't watch the news, and they don't obey the law. Babies are in the NOW, they are connected to their centers.

Babies are rude, they are crude, they are selfish, and they are happy. And what do we do to these perfect little happy human beings? We take them and we make. them into adults, don't we? (Mimes building wall around the baby) We build a wall around our inner baby made of fear and anxiety and negativity and responsibility and hatred. Brick by brick. we build that wall: jealousy and guilt and ambition. Shame, lots of shame, let's get that shame up there. Brick by brick we wall them in around and around until our inner baby is trapped (Miming trapped) like a miniature Marcel Marceau!

I’m telling you to tear down that wall and let that baby out! Come on now and let your baby go! Get rid of that negativity. Stop worrying about tomorrow, stop worrying about yesterday! Stop worrying about what everybody else thinks about you all the time, what people think about you is none of your business! Stop worrying all the time. It's not helping anything! Sure there are people who are miserable all over the world, but hell. being all pissy and negative isn't going to do them much good. now is it? Sure the world is a complicated place, trying to understand it isn't going to make it any less complicated! Let me tell you something, the world has existed for twenty million years without your help, and it's gonna keep on going with or without you. Stop worrying about the whales and the elephants. They don't need you, your baby needs you!

I want you to take your baby's hand, go ahead, take it, it's not very big. And let that baby lead you to a new life of happiness, joy, and healthy selfishness!

From this day onward you're gonna get up every morning and look into the mirror . . . you're gonna look into the mirror, you're gonna say to yourself: What. . . about. . . ME? When's it gonna be my turn? What about my baby?

You get in late for work. You're fifteen minutes late, the boss is pissed off. TOO BAD! My baby needed the sleep.

You forgot to send your Mom a Mother's Day card? She'll just have to wait till next year. Sorry, Mom. I'm busy being the mother you never were!

Driving around for half an hour trying to find someplace to park. Only parking spot is one of those handicapped parking spaces. You park there, your inner baby is handicapped!

It's midnight, you're watching Letterman on TV, halfway through that pint of Hagen Dasz, you finish it up, your baby needs that nurturing. Have another one! Chase it with a couple of Slim-Jims. Your baby needs your love!

You're gonna take care of your inner baby and this isn't going to be some part-time thing! You're going to be thinking about your inner baby incessantly. You're gonna be going to inner baby groups, talking to other inner babies on the phone. You're gonna buy videotapes, you're gonna buy my audiotapes, you're gonna read my books. I'm gonna sell you a little yellow sign, you put it in the window of your car, it's gonna say: "Caution, Inner Baby Within!"

You're gonna make your inner baby happy and when you do, you make yourself happy and when you're happy there will be one more happy person in the world. And you know what? You will have made the world a better place.
```

---

## IC-1162: Inside Out

- Title: Inside Out
- Author (byline): Suzanne Francis
- Work: Not specified
- Publisher: Random House Books for Young Readers
- Publication date as stated: 978-0736433129
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, SADNESS, FEAR, DISGUST, ANGER, JOY, TEACHER, RILEY, NARRATOR 2
- Teaser before the introduction: Yes
- Spoken words (computed): 1318
- Already set (do not supply): none

### Source block (context only)

```text
Author: Suzanne Francis, Adapted from the screenplay by Peter Docter, Meg Lafauve and
Josh Cooley
ISBN: May 2015
Publisher: Random House Books for Young Readers
Date (Month/Year): 978-0736433129
```

### Introduction (context only: never use it for content warnings)

```text
According to Psych Central, our society expects us to “appear happy.” Messages to be “strong” and have “good vibes” rule on social media, but the encouragement to steer clear of sadness often starts in childhood. Grownups angrily tell kids to stop crying, even when they have a “good reason.” And we learn early that being sad makes us, and others, uncomfortable. Inside Out reminds us to embrace the wholeness of ourselves, and gives us permission to not be “okay.” After all, you can’t be happy ALL the time.

Inside Out adapted by Suzanne Francis, from the screenplay by Peter Docter, Meg Lafauve and Josh Cooley
```

### Performance text (classify this)

```text
Adapted from the screenplay by Peter Doctor, Meg Lafauve and Josh Cooley

NARRATOR: (Pg 1-6) On the day Riley was born, Joy found herself inside a strange and beautiful place. Riley’s mind. [You see] Joy was a glowing collection of yellow energy particles and was one of Riley’s Emotions. Joy thought it would just be her and Riley forever . . . but 33 seconds later (Riley begins to wail)

SADNESS: I’m Sadness

NARRATOR: As time went on, more Emotions showed up inside Headquarters. And with each new Emotion, memories started rolling through in different colored spheres. Purple …

FEAR: Look out!

NARRATOR: Disgust was green

DISGUST: Ewwwwwwww!

ANGER: (scowling, screaming, growling)

NARRATOR: That’s Anger . . . short, red and . . . . (makes a face) angry. Joy could see why all of them were important . . . except for Sadness. She tried her best to keep Sadness as far from the controls as possible. Most of Riley’s memories were golden, just like Joy. And the most important ones glowed brighter. Core memories! They power the Islands of Personality: Hockey Island! Goofball Island, Family Island – And there’s Honesty and Friendship Island – Like mini theme parks!

Riley had a very happy childhood, but when she was 11 years old, her parents made a major decision that changed everything. Riley’s dad started a new business and the family moved from Minnesota to San Francisco.

FEAR: Look out!

DISGUST: Ewwwwwwww!

ANGER: (scowling, screaming, growling)

NARRATOR: (Pg 7-8) The car ride was long and when Dad finally drove down their new block

(Riley looks excited for a moment as she stares at the new house, but her emotions can’t be kept in check)

JOY: (hopefully) Maybe it’s nice on the inside

ANGER: We’re supposed to live here?

FEAR: Can you die from moving?

DISGUST: I’m gonna be sick.

SADNESS: Oh, Riley can’t live here . . .

NARRATOR: (Pg 17-19) The first night in the new house was uncomfortable and creepy. Riley had to sleep in a sleeping bag on the floor. And inside Headquarters . .

FEAR: (reacting to a noise) Was it a bear? It’s a bear! I’m so jumpy. My nerves are shot.

JOY: Look, I get it. You have concerns, but we’ve been through worse!

DISGUST: (Sarcastically) Yeah, Joy. We could be lying on a dirty floor . . . in a sleeping bag.

JOY: But think of all the good things . . .

ANGER: No! There’s absolutely no reason for Riley to be happy right now.

FEAR: I say we skip school tomorrow and lock ourselves in the bedroom.

SADNESS: Yeah, we could cry until we can’t breathe. (Pg 15) Something’s wrong with me. It’s like I’m having a breakdown. I’m awful . . . and annoying.

NARRATOR: Sadness constantly focused on the negative. While Joy saw the rain as a fun opportunity for Riley to jump in puddles and carry a cool umbrella, Sadness liked when the rain made Riley feel soggy and droopy.

JOY: (Pg 19) Now hold on. (Pg 21) We are not going to end the day like this. (She shifts through the memory spheres and selects a golden one)

NARRATOR: And then she recalled a memory of Riley showcasing all her ice-skating moves on the lake with her parents. (Riley drifts off to sleep with a smile on her face) *****

JOY: (Pg 22-24) (Waking up with tons of energy) Okay! First day of school. Very exciting! Disgust. Make sure Riley stands out today . . . but also blends in.

DISGUST: When I’m through, Riley will look so good the other kids will look at their own outfits and bar.

JOY: (to Sadness) I have a super important job just for you. (She takes a piece of chalk and draws a circle around Sadness) This is the circle of Sadness. Your job is to make sure that ALL the Sadness stays inside it. (Beat – Sadness tries to put a foot outside the circle, but Joy blocks her) Isn’t it fun?

SADNESS: (exceedingly glum) No . . . .

JOY: All right, everyone. We are going to have a good day, which will turn into a good week, a good year and a good LIFE!

NARRATOR: (Pg 26-27) Riley waled to her new school. There were tons of students and the school as so big.

FEAR: Are you sure we want to do this?

DISGUST: Okay. We’ve got a group of cool girls at two o-clock. (Disgust turning to excitement) Double ears pierced, infinity scarves . . . We want to be friends with them.

FEAR: Worst case scenario is either quicksand, spontaneous combustion, or getting called on by the teacher. So long as none of those happen . . .

TEACHER: Okay, everybody. We have a new student in class today.

FEAR: Are you kidding me? Out of the gate? Nooooooo! Pretend we can’t speak English!

JOY: (Pg 28-30) Don’t worry. I got this!

RILEY: (Smiling) My name is Riley Anderson. I’m from Minnesota . . . (continues to speak silently)

NARRATOR: She told them about being on an ice hockey team, the Prairie Dogs, and how it was a family tradition. But then something very strange happened.

JOY: Sadness! You touched a memory! Get back in your circle!

DISGUST: Cool kids whispering at three o’clock!

FEAR: Did you see that look? They’re judging us!

RILEY: (Riley’s smile fades; she begins to cry) But everything’s different now . . . Since we moved . . . .

FEAR: Oh no! We’re CRYING AT SCHOOL! (PING)

NARRATOR 2: A new memory had been created and it was bright blue. Joy leaned over and pressed the end-of-day Memory Dump button, causing the vacuum tube to come down from the ceiling. (Suction sounds and Joy and Sadness are sucked into the vacuum tube) (Pg 42) Fear, Anger and Disgust were stunned.

DISGUST: We have a major problem. *****

(Joy and Sadness land in a strange remote area the memory spheres fall all around them)

JOY: (Pg 93-94) (as she is gathering the memories – she holds one up) Oh, it’s that time the hockey team showed up and Mom and Dad were there cheering – Look at her having fun and laughing. It’s my favorite.

SADNESS: I love that one too . . . (remembering) It was the day the Prairie Dogs lost the big playoff game. Riley missed the winning shot. She felt awful. She wanted to quit.

NARRATOR: (Pg 103) Joy watched as the hockey team surrounded Riley, and suddenly she realized . . .

JOY: Mom and Dad . . . the team . . . they had come to help because of Sadness.

SADNESS: Sorry. I went sad again, didn’t I? (a stricken look appears on her face)

JOY: (Pg 34) What is it?

SADNESS: You! YOU’RE not in Headquarters. Without you, Riley can’t be happy.

JOY: (Pg 68) This way! Riley . . . here we come! (Joy exits pulling Sadness with her) ******

NARRATOR: (Pg 91– 92) Meanwhile back at Headquarters . . .

FEAR: We were at school, and we were naked and there was a dog . . . .

ANGER: It was a DREAM! This is ridiculous, we can’t even get a good night’s sleep anymore. Time to take action! (Pg 75) All the good core memories were made in Minnesota. We go back to Minnesota and make more! (Anger picks up a lightbulb-shaped idea)

FEAR: Wait. You’re saying we run away? You can’t be serious . . . it’s just so . . . drastic.

ANGER: Need I remind you how great things were there? Our room? Our backyard? Our friends? (Pg 91) Who’s with me?

DISGUST: (Pg 75) Riley was happier in Minnesota . . . Yeah, let’s do it.

ANGER: (Pg 92) (Anger plugs the idea into the console) She took it! There’s no turning back!

DISGUST: So, how’re we gonna get to Minnesota from here?

ANGER: We’re taking the bus!

DISGUST: How do we get money?

ANGER: Mom’s purse. Mom and Dad got us into this mess. They can pay to get us out. ***BOOOM! scene shift to Joy and Sadness****

JOY: (Pg 94-95) Honesty Island! We lost another island . . . . what is happening? (as realization dawns) Riley is running away.

NARRATOR: (Pg 97-99) Suddenly Sadness pointed to a memory recall tube. Normally the tubs were buried deep beneath the shelving of Long-Term Memory, but one of them had become exposed. If they got to it in time . . . .

SADNESS: We can get recalled! (Joy and Sadness push against one another trying to get into the tube) –

JOY: (Pg 103) We have to get back up there!! ******

NARRATOR: (Pg 106) Riley’s cell phone rang as she walked through the streets of San Francisco.

FEAR: It’s Mom. She’s on to us.

ANGER: (Pg 109-110) This is madness! She shouldn’t run away.

DISGUST: Let’s get this idea out of her head. (Frantically pulling at the idea bulb in the console)

ANGER: It’s stuck.

DISGUST: Make her feel scared! That’ll make her change her mind. (Fear frantically pushes buttons and pulls levers, but nothing works.)

FEAR: (in frightened shock) Guys, we can’t make Riley feel anything!

ANGER: (Pg 114-115) AAAAAAAHHHHHHH! (suddenly Joy and Sadness race into headquarters out of breath)

DISGUST: Joy, you’ve got to fix this!

JOY: (shakes her head, then speaks to Sadness) Sadness, it’s up to you . . . Riley needs you.

(Sadness takes a deep breath and places both hands on the console. She gently removes the idea bulb)

RILEY: (Standing up from her seat on the bus) Wait! Stop! I want to get off!

NARRATOR: She got off the bus and ran toward home. And inside Headquarters Sadness was confidently driving. Joy pulled the yellow core memories out of her bag and handed them over to her. The memories all turned blue. (Pg 116-117) In the dining room, Riley cried as Sadness placed each memory, one at a time, into the recall unit.

RILEY: I know you don’t want me to, but . . . I miss home. I miss Minnesota. You need me to be happy, but I want my old friends, and my hockey team.

NARRATOR: Her parents talked about all the things they missed about Minnesota and the three of them hugged as Riley continued to cry. Sadness took Joy’s hand and placed it on the console alongside her own. And Riley smiled through her tears. (DING)

FEAR: (Pg 121) They love us!

ANGER: Yeah, Mom and Dad are pretty cool.

DISGUST: Guys, of course they are. But we can’t show it!

NARRATOR: (Pg 117) A new core memory was made. This one was gold and blue swirled together . . . a first. A new Family Island rose, bigger and better than the last.

JOY: (Pg 123) Things might have gotten turned inside out

SADNESS: And even upside down

JOY: But everything is going to be just fine.
```

---

## IC-1163: Into the Woods

- Title: Into the Woods
- Author (byline): Stephen Sondheim and James Lapine
- Work: Not specified
- Publisher: Theatre Communications Group
- Publication date as stated: June 1989
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, BAKER, WITCH, WIFE, JACK, LITTLE RED, WITCH’S VOICE, CINDERELLA, RAPUNZEL
- Teaser before the introduction: Yes
- Spoken words (computed): 1083
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
Our story begins in a kingdom where fairy tales don’t just happen. They get a little tangled, slightly ridiculous, and occasionally burst into rap at the worst possible moments.

Welcome to a world where cows are suspiciously important, and happily-ever-afters come with a long list of conditions. In this enchanted forest, wishes don’t come true easily—and if they do, there’s usually a catch or a curse! Are you brave enough to go . . .

Into the Woods by Stephen Sondheim and James Lapine (whispers) A great adventure is about to begin.
```

### Performance text (classify this)

```text
NARRATOR: (Pg 3-4) Once upon a time in a far-off kingdom lived a childless baker with his wife. (Pg 12-14) The baker had lost his mother and father in a baking accident – well, at least that is what he believed. He was eager to have a family of his own and concerned that all efforts until now had failed. (a knock on the baker’s door)

BAKER: Who might that be? (looks off to see) It’s the witch from next door! (opens the door) We have no bread.

WITCH: Of course you have no bread! (Wife reacts)

BAKER: What do you wish?

WITCH: It’s not what I wish. It’s what you wish. (points to wife’s belly) Nothing cooking in there now, is there? (Wife reacts by clutching her stomach)

NARRATOR: The enchantress went on to tell the couple she had placed a spell on their house.

WITCH: In the past, when you were no more than a babe, your father brought his young wife and you to this cottage. They were a handsome couple, but NOT handsome neighbors. My beautiful garden! How was I to know what your father had hid in his pocket? My mother had warned me I would be punished if I ever were to lose any of the beans.

WIFE: Beans?

WITCH: The special beans! I let him go / I didn’t know / he’d stolen my beans! (getting worked up – she raps) Then Bang! Crash! And the lightning flash! / And I laid a little spell on them. (Rap stops) You too, son – that your family tree would always be a barren one. (wife gasps; Witch begins to rap again) So there’s no more fuss/ And there’s no more scenes / And my garden thrives - / You should see my nectarines! / But I’m telling you the same / I tell Kings and Queens / Don’t ever never ever / Mess around with my greens! / Especially the beans.

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

## IC-1164: It’s Not a Sport

- Title: It’s Not a Sport
- Author (byline): George Carlin
- Work: Napalm & Silly Putty, Pg 106-109
- Publisher: Hyperion
- Publication date as stated: April 2001
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: SPEAKER
- Teaser before the introduction: Yes
- Spoken words (computed): 785
- Already set (do not supply): none

### Source block (context only)

```text
Author: George Carlin
Book: Napalm & Silly Putty, Pg 106-109
ISBN: 978-0786864133
Publisher: Hyperion
Date (Month/Year): April 2001
```

### Introduction (context only: never use it for content warnings)

```text
Golf would be much more interesting and exciting if they had goalies. . . Seriously, just think about it. . . In virtually every sport you have an opponent whose sole purpose in life is to keep you from achieving your goal. . . What’s the challenge in golf? Heck, at least train a couple of gerbils to guard each hole. As a matter of fact, there’s probably a multitude of alleged sports that in reality, any jury in its right mind would conclude . . .

It’s Not a Sport by George Carlin
```

### Performance text (classify this)

```text
SPEAKER: (Pg 106-109) To my way of thinking there are really only three sports: baseball, basketball, and football. Everything else is either a game or an activity.

SPEAKER: Hockey comes to mind. People think hockey is a sport. It's not. Hockey is three activities taking place at the same time: ice skating, fooling around with a puck, and beating the crap out of somebody. If these guys had more brains then teeth, they'd do these things one at a time. First go ice-skating, then fool around with a puck, then you go to the bar and beat the crap out of somebody. The day would last longer, and these guys would have a lot more fun. Another reason why hockey isn't a sport is that it's not played with a ball. Anything not played with a ball can't be a sport. These are my rules, I make 'em up.

Soccer. Soccer is not a sport because you can't use your arms. Anything where you can't use your arms can't be a sport. Tap dancing isn't a sport. I rest my case.

Running. People think running is a sport. Running isn't a sport because anybody can do it. I can run, you can run. For Christ sakes, my mother can run! You don't see her on the cover of Sports Illustrated, do you?

Swimming. Swimming isn't a sport. Swimming is a way to keep from drowning. That's just common sense. Sailing isn't a sport. Sailing is a way to get somewhere. Riding the bus isn't a sport, why should sailing be a sport?

Boxing is not a sport either. Boxing is a way to beat the crap out of somebody. In that respect, boxing is actually a more sophisticated way of hockey. In spite of what the police tell you, beating the crap out of somebody is not a sport. When police brutality becomes an Olympic event, fine, then boxing can be a sport.

Bowling. Bowling isn't a sport because you have to rent shoes. Don't forget, these are my rules. I make 'em up.

Billiards. Some people think billiards is a sport, but it can't be, because there's no chance of serious injury. Unless, of course, you welch on a bet in a tough neighborhood. Then, if you wind up with a pool cue stickin' out of your ear, you know you might be the victim of a sports-related injury. But that ain't billiards, that's pool, and that starts with a P, and that rhymes with D, and that brings me to darts.

Darts could have been a sport, because at least there's a chance to put someone's eye out. But, alas, darts will never be a sport, because the whole object of the game is to reach zero, which goes against all sports logic.

Lacrosse is not a sport; lacrosse is a college activity. I don't care how rough it is, anytime you're running around a field, waving a stick with a little net on the end of it, you're engaged in a college activity. Period.

Field hockey and fencing. Same thing. Also these activities aren't sports, because you can't gamble on them. Anything you can't gamble on can't be a sport. When was the last time you made a fencing bet?

Gymnastics is not a sport because Romanians are good at it. It took me a long time to come up with that rule, but, I did it.

Polo isn't a sport. Polo is golf on horseback. Without holes. It's a great concept, but not a sport. And as far as water polo is concerned, I hesitate to even mention it, because it's extremely cruel to horses.

Which brings me to hunting. You think hunting is a sport? Ask the deer. The only good thing about hunting is the many fatal accidents on the weekends. And, of course, the permanently disfigured hunters who survive such accidents.

Then you have tennis. Tennis is very trendy and very fruity, but it's not a sport. It's just a way to meet other trendy fruits. Technically, tennis is an advanced form a Ping-Pong. In fact, tennis is Ping-Pong played while standing on the table. Great concept, not a sport.

In fact, all racket games are nothing more than derivatives of Ping-Pong. Even volleyball is, technically, racketless, team Ping-Pong played with an inflated ball and raised net while standing on the table.

And finally welcome to golf. Let it just be said golf is a game that might possibly be fun, if it could be played alone. But it's the vacuous, striving, superficial, male-bonding joiners one has to associate with that makes it such a repulsive pastime. And it is decidedly not a sport.

Period.
```

---

## IC-1165: James and the Giant Peach

- Title: James and the Giant Peach
- Author (byline): Roald Dahl
- Work: Not specified
- Publisher: Puffin
- Publication date as stated: April 2000
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, AUNT SPIKER, AUNT SPONGE, OLD MAN, JAMES, SPIDER, GRASSHOPPER, CENTIPEDE, EARTHWORM, LADYBIRD, NARRATOR 1, CHIEF OF POLICE, HEAD OF THE FIRE DEPT
- Teaser before the introduction: Yes
- Spoken words (computed): 1309
- Already set (do not supply): none

### Source block (context only)

```text
Author: Roald Dahl
ISBN: 978-0140374247
Publisher: Puffin
Date (Month/Year): April 2000
```

### Introduction (context only: never use it for content warnings)

```text
James Henry Trotter, a lonely orphan living with two unkind and malicious guardians, longs for friends. When a magical peach grows in his backyard, he unexpectedly finds companionship with a rag-tag bunch of characters. Their journey together is exceptional as they overcome obstacles beyond imagination. And James is transformed by the power of friendship, trust and the shared challenges they face. He comes to realize the truth in this quote by Edna Buchanan: “Friends are the family we choose for ourselves.”

James and the Giant Peach by Roald Dahl
```

### Performance text (classify this)

```text
NARRATOR: (Chpt 1) Until he was four years old, James Henry Trotter had a happy life. He lived peacefully with his mother and father in a beautiful house beside the sea. It was the perfect life . . . . (James plays) Then one day a terrible thing happened. (James freezes) James’s mother and father went to the zoo. Both of them suddenly got eaten up by an enormous angry rhinoceros which had escaped. Poor James was sent away to live with his Aunt Sponge and Aunt Spiker.

AUNT SPIKER: You filthy nuisance!

NARRATOR: I am sorry to say they were both really horrible people.

AUNT SPONGE: You disgusting little beast!

AUNT SPIKER: You miserable creature! (James begins to cry) (Chpt 2) What’s the matter with you?

AUNT SPONGE: Beat him!

AUNT SPIKER: I certainly will! (She glares at James who is very frightened)

NARRATOR: (Chpt 3) [One day a] rather peculiar thing happened to [James].

OLD MAN: Come, little boy! (beckoning) Come and I will show you something wonderful! (he puts his hand into the pocket of his jacket and takes out a small bag and waves it in front of James’s face; James is enthralled) Take a look! Listen to them move! There’s more power and magic in there than in all the rest of the world put together!

JAMES: But – but – what are they?

OLD MAN: Crocodile tongues! Boiled for twenty days with the eyeballs of a lizard! (he pushes the bag into James’s hands) Here! Take it! It’s yours! (Chpt 4) And don’t let those green things escape. Because if they do . . . Whoever they meet first, be it bug, insect, or tree, will get the full power of their magic! Marvelous things will start happening to you – and you will never be miserable again. Off you go! Hurry!

NARRATOR: (Chpt 5) James was running back towards the house as fast as he could. Then suddenly, just as he was passing the old peach tree, his foot slipped and he fell flat on his face. (James trips and loses all the green things in the bag, he is frantically searching for them when Aunt Spiker enters)

AUNT SPIKER: Get up at once, you lazy little beast! Get over there and finish chopping those logs! ****** Scene break*****

AUNT SPIKER: (Chpt 6) (staring in awe at the top of the peach tree) Sponge! Sponge! Come here and look at this! It’s a peach!

JAMES: (looking up at the tree) Something peculiar is about to happen . . . .

AUNT SPONGE: (preoccupied doing something else) A what? That miserable tree never has any peaches on it. (She sees the enormous peach) There really is a peach up there!

AUNT SPIKER: A nice big one too!

AUNT SPONGE: Why don’t we eat it! (licking her lips)

AUNT SPIKER: (in terror) It’s getting bigger! Great heavens alive!

NARRATOR: (Chpt 7) Bigger and bigger grew the peach. It grew as tall and wide as a small house. The bottom part of it gently touched the ground and there it rested.

JAMES: Oh, isn’t it beautiful. It’s the most beautiful thing I’ve ever seen.

AUNT SPIKER: Shut up, you little twerp! It’s none of your business. (walking around the peach) There’s a pile of money to be made out of this if we handle it right! (Chpt 8) (strutting around) Roll up! Only one shilling to see the giant peach! ****** Scene break*****

NARRATOR: Later, when the people had all gone home . . .

JAMES: (opening the door) Could I please have something to eat?

AUNT SPIKER: (slamming the door shut) No! We are counting our money! (She cackles)

NARRATOR: (Chpt 9) James, as though drawn by some powerful magnet, started walking towards the giant peach.

JAMES: (in awe) Something stranger than ever this time is about to happen to me again!

NARRATOR: Suddenly he happened to notice there was a hole in the side of the peach.

JAMES: (Chpt 10) (James crawls inside) This isn’t a hole . . . It’s a tunnel! (he continues to follow the tunnel and then suddenly – bang – the top of his head bumps into something hard) Good Heavens! I’ve come to the stone in the middle! (He pries open a door in the peach stone and steps through and reacts with large, frightened eyes)

SPIDER: (Chpt 11) I’m hungry!

GRASSHOPPER: I’m famished!

CENTIPEDE: (wriggling) Everyone’s famished! We need food!

GRASSHOPPER: (to James) You look positively ill!

CENTIPEDE: Cheer up, my boy! (Chpt 12) (bragging and wagging his feet to introduce himself) Centipede. I have a lot of legs. One hundred, to be exact.

EARTHWORM: There he goes again! Telling lies about his legs! He’s only got forth two! There’s nothing marvelous about having a lot of legs. The really marvelous thing is to have no legs at all and to be ablet to walk just the same.

CENTIPEDE: You call that walking! You’re a slitherer. You just slither along!

EARTHWORM: (primly) I glide.

CENTIPEDE: You are a slimy beast.

EARTHWORM: I am not a slimy beast!

CENTIPEDE: (growing tired of harassing Earthworm) James? Have you ever in your life seen such a marvelous colossal Centipede as me?

JAMES: I certainly haven’t. How on earth did you get to be like that?

CENTIPEDE: Very peculiar, indeed. I was under the old peach tree and suddenly a funny little green thing came wriggling past my nose.

EARTHWORM: (proudly) I actually swallowed one!

JAMES: Oh! I know what that was!

SPIDER: There were little green things everywhere!

GRASSHOPPER: It’s too late to tell stories now. It’s time to go to sleep! (Chpt 14) (suddenly the peach shook as if in an earthquake)

JAMES: What’s happening? What’s going on? ****** Scene break*****

(Centipede chews through the peach stem with a purpose)

LADYBIRD (off stage): At this moment, Centipede is nibbling away at the stem. We are about to depart forever from the top of this ghastly hill and those two repulsive aunts of yours.

CENTIPEDE: I’ve done it! The journey begins!

NARRATOR: Slowly . . . Insidiously . . . Oh, most gently. . . The great peach started to lean forward and steal into motion.

JAMES: (crashing into furniture, walls and each other) ****** Scene break*****

AUNT SPONGE: (Chpt 15) I wonder what became of that horrid little boy last night.

AUNT SPIKER: He probably fell down in the dark and broke his leg.

AUNT SPONGE: Or his neck! (She cackles)

AUNT SPIKER: (sound effect inserted here) Good gracious me! What’s that awful noise? (Both turn around and react in terror. They try to scramble out of the path of the peach, but . . . . screams)

NARRATOR: And then there was silence. Aunt Sponge and Aunt Spiker lay lifeless. The peach? (Chpt 16) A round object will keep rolling as long as it is on a downhill slope. In this case the land sloped downhill all the way to . . . . ****** Scene break*****

JAMES: (Chpt 18) (Atop the peach bobbing gently) We’re in the middle of the sea!

GRASSHOPPER: (also bobbing but trying to keep the fear out of his voice) I am afraid we find ourselves in a rather awkward situation.

EARTHWORM: Awkward! We are finished!

JAMES: (reassuringly) We are floating beautifully. Sooner or later a ship is bound to come along.

EARTHWORM: If we are not going to be drowned, then we are going to starve to death instead!

CENTIPEDE: Earthworm is right!

JAMES: We have enough food here for weeks!

SPIDER: Where?

JAMES: The peach of course! (he breaks off a piece and takes a bite) Our whole ship is made of food!

GRASSHOPPER: (taking a bite too) Jumping Jehoshophat!

SPIDER: (lassoing a piece of peach with her web) Isn’t it glorious! The finest dinner in the world!

CENTIPEDE: (Chpt 19) (looks over the side of the peach and pointing with many of his legs) Look! Look at that funny black thing gliding through the water!

EARTHWORM: Sharks!!!!

GRASSHOPPER: (looking on the bright side) Perhaps they have come to say hello?

SPIDER: We are finished now! They will eat the peach and there’ll be nothing left to stand on.

EARTHWORM: I don’t want to be eaten!

CENTIPEDE: (panicked) Come on, James. There must be something we can do.

JAMES: (Chpt 20) I . . . I . . . I . . .

SPIDER: (Chpt 19) Think, James, think!

JAMES: (Chpt 20) There is something We’d need string to make this work!

SPIDER: I can spin (she demonstrates) As much as you want. But why? (Spider spind and hands the product to James)

JAMES: (firmly) I’m going to lift this peach clear out of the water!

GRASSHOPPER: The boy’s crazy.

LADYBIRD: How are you going to do it?

JAMES: Seagulls! I’m going to take a long silk string and loop one end round a seagull’s neck and tie the other end to the stem of the peach. (James pantomimes and seagull squawks) (with authority) (Chpt 21) Action stations! There’s not a moment to lose! (James smiles as the peach begins to rise)

NARRATOR 1: (Chpt 22) Suddenly. Slowly . . . Majestically . . . The giant peach rose out of the water like some fabulous golden balloon.

EARTHWORM: (Chpt 23) Good-bye, sharks!

CENTIPEDE: Oh, boy, this is the way to travel! ****** Scene break*****

NARRATOR: (Chpt 31) Faster and faster flew the seagulls [until] (Chpt 33) far below them, in the City of New York, pandemonium was breaking out. (cries from townspeople as they spy the giant peach) A ball as big as a house had been sighted in the sky. It was an enormous bomb sent to blow the city to smithereens! Air-raid sirens began wailing (insert sound effect here) (Chpt 36) James could see the skyscrapers rushing up to meet them. The very tallest of them all had a top that tapered off into a long sharp point.

JAMES: Good-bye, Centipede. Good-bye everybody! (the peach lands on the top of spike of the Empire State Building insert sound effect here)

NARRATOR: Suddenly – there was the giant peach, caught on upon the very pinnacle of the Empire State Building

CHIEF OF POLICE: (Chpt 37) It’s a Snozzwanger!

HEAD OF THE FIRE DEPT: It’s a Whangdoodle!

JAMES: (realizing he’s alive, he peers over the side of the peach and waves) Hello, everybody! Hello! Don’t be frightened. We are so glad to be here!

CHIEF OF POLICE: What about the others? Are any of them dangerous?

JAMES: Of course not! [This is] Spider with a mile of thread inside her. Grasshopper is a boon in millions of ways. This is Centipede. He is so sweet and gentle. And Earthworm? Absolutely grand! (townspeople cheer)

NARRATOR: (Chpt 39) And thus the journey ended. But the travelers lived on. Centipede became Vice President of a high-class boot manufacturer. Earthworm made commercials on television for women’s face creams. Miss Spider set up a factory and made ropes for tightrope walkers. Old-Green-Grasshopper became a member of the New York Symphony Orchestra. And the enormous peach stone was set up in a place of honor in Central Park. It became a famous house. And inside the famous house lived a famous person. (James opens the door and steps outside) James Henry Trotter . . . once the saddest and loneliest boy that you could find . . . now had all the friends in the world.
```

---

## IC-1166: Jill and the Beanstalk

- Title: Jill and the Beanstalk
- Author (byline): Denise Vega
- Work: Newfangled Fairy Tales (ed B Lansky)
- Publisher: Meadowbrook Press
- Publication date as stated: Jan 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1531
- Already set (do not supply): none

### Source block (context only)

```text
Author: Denise Vega
Book: Newfangled Fairy Tales (ed B Lansky)
ISBN: 0671577042
Publisher: Meadowbrook Press
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
Now, finally, at last - those old fairy tales have been exposed for the drivel they are! Did you ever stop to think that Sleeping Beauty might have been neutralized because she was a miserable young woman? Or that Goldilocks wore red because her mother got a great deal on a bolt of red cloth? Or perhaps, the giants in Jack and the Beanstalk weren’t so bad after all . . . . compared to the poverty and neglect that plagued Jack and his mother. And come to think of it; why does it have to be Jack . . . How about Jill and the Beanstalk? by Denise Vega.
```

### Performance text (classify this)

```text
Jill was out walking to school one morning. Her mother had given her $15 that she was supposed to give to her teacher. It was a fee for art class.

As Jill was happily skipping along, a friendly looking man stepped out of an alley, and Jill, not seeing him, skipped right into him.

"UMPHH" Was all he said at first.

Jill jumped back, dropping her money. "OH! I'm sorry," she exclaimed.

"Quite ok," replied the man, as he picked up the money and handed it back to her. "That's quite a bit of lunch money," he said, eyeing the money.

"That's not my lunch money!" Jill giggled. "That's for art class!"

"Oh I see..." the man answered her. ”Do you like art?"

Jill nodded.

"Well," said the man, "I just happen to have these....magic beans, yeah that's what they are....magic beans, and if you plant them in the ground, a huge stalk will grow up and at the top of it you will find a land filled with all kinds of art!"

Jill's eyes were wide with amazement. "Are you gonna plant them?" She asked the man.

"Well, I have no ground to put them in," the man tried to sound sad here. "Someone gave them to me for my last $15, and then I had nowhere to plant them." He looked at Jill. She appeared to be swallowing it. "If only someone who could plant them would buy them..."

Jill looked down at her money. "Here," she said. "I wanna buy them!"

"Well, if you're sure," said the man, as he quickly snatched the money before she could change her mind. He reached into his pocket and pulled out a small leather bag with five smooth beans and gave it to her. The real origin of the beans was a small shop he had broken into downtown. There wasn't much of any value in it, or so it seemed, but he figured he could make up wild stories about the stuff and sell it to unsuspecting kids. He was a con man.

The man walked away muttering a few things quietly. "What's 'gullible' mean?" thought Jill. Shrugging her shoulders, she skipped the rest of the way to school.

When she got home, her mommy was waiting for her.

"What did you do with the money I gave you?" she asked. "Your teacher called and said you didn't give her your art fee."

Jill showed her the beans, telling her the story the man had told her. But instead of being excited about it, her mommy was very upset with her. She took the bag of beans and sent Jill to her room.

"Kids!" she exclaimed, slamming the bag down on the desk. As she did this, three of the beans flew out of the bag from the force, and flew right out the open window nearby.

Jill thought she heard strange sounds that night. Her bedroom just happened to be right above where the beans landed. She got up and looked out the window; just in time to see a large bean sprout go right past her window. Jill was very excited. "Mommy must have changed her mind, and planted them after all!" she thought, excited.

Jill had always been like a little monkey, climbing anything she could. Whenever she was on the playground you would find her near the Jungle Gym. Carefully she slid over the window ledge and grabbed hold of the bean sprout. Once she had a good hold, she began to climb. She climbed and climbed, and climbed some more. Jill was beginning to think she would never reach the top...it seemed as though she had been climbing for hours. In fact when she looked down, she couldn't even see the ground anymore.

Finally she reached what appeared to be a hole in the sky. As she climbed through it, she got off the beanstalk. It continued on up further.

Now Jill looked around her. She seemed to be on the front door of a large house. The door seemed so large to her, but she reached up and knocked on it. The door opened, and a lady looked out after a minute, peering in both directions, then down. She scared Jill...she had never seen anyone so huge! Not that the woman was fat, in fact she was very fit, but she must have been over 15 feet tall!

When the woman looked down, she exclaimed, "Why, it's a little baby! Someone left us a little baby girl!"

Forgetting her fear for just a second, Jill's hot temper caused her to be indignant. "I am not a baby!" she said, stomping her foot. "I'm nearly nine!"

The woman smiled at this childish display. "Not a baby, dear? But, then, why are you so small? I've seen two year olds bigger than you. And big girls don't do that..." she pointed at Jill's pants.

Jill looked down at herself. Oh No! She thought she had felt a warm sensation a moment ago! She had been so afraid when she saw the woman, that she had wet herself. Ashamed, Jill began to cry.

"Aww . . .there, there, everything will be ok" the woman consoled her, as she picked her up and carried her into the house.

They went through a kitchen and a few other rooms, up some stairs and down a hall. Jill saw a few other people in the house. They were all much bigger than she, but smaller than the woman carrying her.

"Hey, Mom, what's that?" she heard one of them call out.

The woman turned. "Not "What", Peter.... "Who". "Who is that?"

The one named Peter turned red. "Ok ok...WHO is that then?"

"This is a baby girl someone left by our door," she said. "Look at this, she's not even properly dressed as a baby. We'll take care of that. Her name is Jill."

Jill was still sniffling as they went through a door. Inside the room was a HUGE nursery. The woman took her through the nursery and into a room of the side of it, and Jill saw it had a bathtub in it. The woman filled the tub, and sat Jill on the floor and began to take Jill's clothes off.

Since she had not slept, and had climbed so long, Jill was very tired, and she let the woman do this to her. Then the woman put her in the tub, and gently washed her.

Jill was beginning to enjoy the comforting feelings this gave her. Before she knew what was happening, her thumb had found its way to her mouth, and she was contentedly sucking.

The woman smiled at her, cooed and talked baby talk as she bathed Jill. She reached out and tickled her, and was overjoyed when Jill giggled.

When she was finished washing her, the woman wrapped her in a towel and took her back to the nursery. Here she laid her on a changing table and dried her off. Jill realized the changing table would easily accommodate babies much bigger than herself. Then she cringed, realizing she had just thought of herself as a baby. She was also aware of a growing need. Why hadn't there been a toilet in that bathroom?

"Umm, Ma'am?" she said softly.

The woman smiled. "Why don't you call me Mommy?" she told Jill.

"Mommy, I have to go to the bathroom."

The woman laughed lightly. "Silly baby, babies don't use potties, and even if you could, which you already proved you can't, you couldn't reach the potties here."

Jill was still not getting it. "Well then how do they..." she began, then she saw the woman was unfolding something large and white. It was a huge diaper, quite big enough for Jill. The woman easily lifted her by the ankles and slid the diaper under her bottom. She also took time here to apply baby powder.

Jill experienced a whole realm of new feelings as the diaper was pulled up and snugly taped into place on her. She felt shame at first, but then realized this was better than wetting her pants as she had earlier. Besides, everyone here expected her to be diapered. She felt the warm and soft coziness of the diaper, and it felt safe and secure too. She decided this was not so bad after all. All the lost sleep was catching up to her now, and she was fading fast. The woman put a sleeper on her and carried her to a rocking chair, where she put her against her breast and began to rock her gently.

"Jill," she asked, "Those beans only work for very special people. People who are missing something. You are missing being a child, and so you must be one as long as it takes for you to get over that. Would you like to stay here and be my baby?"

Jill nodded her head. "Yes, Mommy, I would like that very much," she said, She accepted a bottle that was offered to her, and just as she drifted into sleep she felt a warm comfortable rush as she saturated her diapers.
```

---

## IC-1167: The Kentish Sleep Deprivation Journal

- Title: The Kentish Sleep Deprivation Journal
- Author (byline): Marshall Brickman
- Work: Not specified
- Publisher: HarperCollins Publishers, Inc
- Publication date as stated: 1974
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1351
- Already set (do not supply): none

### Source block (context only)

```text
Author: Marshall Brickman
Book/Magazine: The New Yorker
Publisher: HarperCollins Publishers, Inc
Date(Month/Year): 1974
```

### Introduction (context only: never use it for content warnings)

```text
Sleep--along with its counterpart, being awake--accounts for much of the time spent by modern man during his life, and therefore merits serious attention by the trained observer. Certainly the most fascinating document to emerge from the burgeoning sleep-research field is the journal kept by Dr. Mordecai Kentish during a classic experiment in which he stayed awake for more than three hundred hours in order to study the effects of extensive sleep deprivation. The Kentish Sleep Deprivation Journal by Marshall Brickman.
```

### Performance text (classify this)

```text
Dr. Kentish, Winkle Professor of Clinical Psychology at Tony’s College, Chicago, won the Nobel Prize in 1948 for his work in isolating and defining the common nap as “any rest episode up to twenty minutes’ duration involving unconsciousness but not pajamas.” He also pioneered the “Kentish Technique” of psychoanalysis, in which either the patient or the therapist gets to lie on the couch, depending on which of the two is sleepier. He is the author of the standard text “Sleep” and the widely known treatise on insomnia, “How to Sleep,” plus a third volume, “Where to Sleep,” a thoughtful rating of motels found along the major interstate arteries, which includes an appendix listing inexpensive restaurants and the locations of important historical markers.

We would like to express our thanks to Mabley Kentish for releasing the Kentish papers for publication only months after her brother’s experiments were so tragically interrupted, when he was carried off by a large bird. Selected portions of the Sleep Deprivation Journal follow.

First Day (12 hours): Arrived at laboratory 9 p.m. Bucholtz [Kentish’s devoted assistant, O. Bucholtz, a refugee who worked for Kentish for twelve years without remuneration of any kind, and with only one two-day vacation, which he spent walking around in the front yard] as usual leaves a mess--candy wrappers, a banana peel on the EEG, a half-filled container of coffee with a cigarette butt floating in it. Nevertheless, there can be no question of dismissing him; he is pathetically devoted to me, perhaps because of that time I let him watch me shave. The current record for sleeplessness is held by radio personality Galen Moon, the host of a telephone show, who remained awake for the entire two hundred hours required to take an irate call from a severe stutterer. Moon, a noted insomniac, later revealed to me that even after his excruciating ordeal he could not fall asleep without first browsing through an article entitled, “Cairo--Wither the New Agrarianism?” a soporific published every Sunday in the magazine section of the New York Times. My intention is to exceed Moon’s limit by at least one-third, utilizing no stimulants or artificial means whatsoever--nothing but the awesome powers of a disciplined intellect. At the end of each entry, as daily proof of my ability to sustain rational, sequential thought, I shall perform a simple test, by writing out the complete alphabet. Thus:

abcdefghijklmnopqrstuvwxyz

Second Day (38 hours): Pulse, respiration, temperature, and blood pressure normal. A mild elation accompanied by great mental clarity. Chess with Bucholtz; a carefully laid trap of my own design (Ruy Lopez, with a slashing bishop attack) had the fool mated in seven moves. Intake: Breakfast--coffee and a scone with honey. Lunch--Bibb lettuce rémoulade. Dinner--butterfish and a praline. Physical coordination excellent; I jumped two feet straight up into the air without bending my knees--a difficult enough feat for a young man, and certainly remarkable for an advanced sedentary specimen such as myself. Wonderful feeling of crispness and efficiency. Three times eight is twenty-four. The cube root of eight is two. The capital of Chile is Santiago.

abcdefghijklmnopqrstuvwxyz

abcdefghijklmnopqrstuvwxyz

Fifth Day (109 hours): Sensation of mild granulation around the eyeballs, as if a small boy had flung pulverized antimony into my face. Pulse, temperature, respiration, blood pressure normal. (Annoying relative term, “normal.” For whom?) In Bucholtz’s case, temperature, pressure, respiration, and blood pressure can all be expressed by one integer in the low fifties. Chess with Bucholtz. Irresponsibly sacrificed my queen, both knights, both bishops, and all pawns within the first thirteen moves; nevertheless managed to achieve stalemate by sending Bucholtz on a brief errand, during which time I flushed his king down the toilet. The frontiers of the mind are limitless. The cube root of eight is not two; it is something else, possibly the color red.

abcdefghijklmnopqrstuvwxyz

Sixth Day (150 hours): No noticeable fatigue. Curious perceptual distortions, however. Everyday objects (i.e.; my right hand, a chair) seem either too large or too small, but I cannot decide which. Chess with Bucholtz discontinued when I realized after twenty minutes that we had set up the pieces without the board and were playing directly on the table. Intake: Breakfast--coffee, scone. Dinner-- butterfish and a slice of whole-wheat bread. Read article by Karsky in International Journal of Orthopsychology, on jealousy in moths. Difficult to follow, as the entire text apparently consists of the word “vibescu” repeated endlessly. These behaviorists will stoop to any cheap trick merely to publish. I am on to Karsky, which explains why he never speaks to me even though we have never met and he lives in Omsk.

abcdefgz

Eighth Day (182 hours): Curious feeling of constriction in the frontal lobe, as if someone had forced a tiny cast-iron opera hat onto my head with a wooden mallet. Today, for the first time in our long association, Bucholtz made a witty remark. When I asked him if there were any telephone messages for me, he replied, “No, the phone hasn’t rung all day.” (!) He is unbearably funny; the juxtaposition of “all day”--i.e.; the entire day--with the notion of the telephone not ringing was, I thought, a masterful stroke of ironic hyperbole, worthy of Goethe and especially remarkable in someone who still needs help dressing. When I finally caught my breath, I requested that he close the door, which he did in a similarly comical fashion, putting his hand on the knob and pushing the entire structure until it latched. Again I broke into gales of laughter (it was marvelous, really), which Bucholtz mocked (also amusingly) by looking at me directly with both eyes! He is quite a jolly fellow, this Bucholtz.

a b 3 defg hijklmnop p ppp

Ninth Day (231 hours): Intake: Breakfast--cofscone. The fork is the one with the little points on it; the spoon, however, is round. That is how you can tell them apart. Temperature erutarepmet. Window open 3½ inches, chair oriented along N-S magnetic lines of force, thus enabling me to draw energy from the earth and maintain a healthy, full head of hair. All else normal, except for Bucholtz’s plot to steal my face and sell it to the emperor. I have the persistent impression that a man named Al Bender possesses infinite knowledge, if we can only locate him and get him to talk. My brain remains miraculously alert. Some trouble, however, with the pancreas, which has been stealing catnaps. Thank God for the kidneys, which keep it awake with their constant bickering.

abz

Ninth Day (234 hours): 4 a.m. Bucholtz asleep in the next room. The clock has just asked for a glass of water. Reasonable enough, but what is “water”? Increasing difficulty concentrating on simple tasks, such as snapping my luncheon peas across the room at Bucholtz. The dog outside has become a distraction, with its constant barking of “Iolanthe,” but when I try to call the authorities, the phone bursts into flame. What would Lysenko say about this? And to whom would he say it? I understand “vibescu” now; Karsky is clearly a genius. Dear, dear Karsky! Misunderstood, ridiculed, mocked. And to think I almost mailed him a spider! I must go to him. I need paper to build a boat.

a bee cee dee eff gee aitch I jay

Twelfth Day (301 hours): Still no fatigue. Temperature 99°. Skies fair. Winds calm. Position 28°S by 188°W. The mate have eat of a tainted Gouda and muft be lafhed to the mizzen. Difpleasure on the foredeck, water maggoty. Three more given up to scurvey. May God help us in our tryalle...

At this point, the journal stops abruptly. Bucholtz, upon awakening, reported finding his mentor rigid, his forehead against the light switch, his body making a hypotenuse between floor and wall. His eyes were open and unblinking, his pulse 180, his temperature 50°F. Removed to the hospital, Kentish was given a strong sedative and put to sleep for a week, after which he awoke refreshed and ate an enormous breakfast, including two paper cups. His notes, bearing extensive tooth marks, were recovered by O. Bucholtz and presented to Mabley Kentish, who will publish them this fall in popular edition, under the title “Copping Zs--Forty Winks to Oblivion.”
```

---

## IC-1168: Ladies and Gentlemen: The Bible!

- Title: Ladies and Gentlemen: The Bible!
- Author (byline): Jonathan Goldstein
- Work: Not specified
- Publisher: Riverhead Trade
- Publication date as stated: April 2009
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2403
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jonathan Goldstein
ISBN: 978-1594483677
Publisher: Riverhead Trade
Date (Month/Year): April 2009
```

### Introduction (context only: never use it for content warnings)

```text
In the beginning...there was humor.

Sure, the Bible is the foundation for much of Western morality and the cornerstone of world literature. But let's face it: the book always needed punching up. Plus, it raised quite a few questions that a modern world refuses to ignore any longer: wouldn't it be boring to live inside a whale? How did Joseph explain Mary's pregnancy to the guys at work? Who exactly was the megalomaniacal foreman who oversaw the construction of the Tower of Babel? And honestly, what was Cain's problem? Today we revisit the story of original sin . . . the Story of Adam and Eve from Ladies and Gentle, the Bible! By Jonathan Goldstein.
```

### Performance text (classify this)

```text
In the Beginning, when Adam was first created, he spent whole days rubbing his face in the grass. He picked his ear until it bled, tried to fit his fist in his mouth, and yanked out tufts of his own hair. At one point he tried to pinch his own eyes out, in order to examine them, and God had to step in.

Looking down at Adam, God must have felt a bit weird about the whole thing. It must have been something like eating at a cafeteria table all by yourself when a stranger suddenly sits down opposite you. But it's a stranger who you have created. And he is eating a macaroni salad that you have also created. And you have been sitting at the table all by yourself for over a hundred billion years. And yet still, you have nothing to talk about. It was pitiful the way Adam looked up into the sky and squinted. Before He created Adam, God must have been lonely. Now he was still lonely, and so was Adam.

Then came Eve. Since the Garden of Eden was the very first village and since every village needs a mayor as well as a village idiot, it broke down in this way. Eve: mayor. Adam: village idiot. And that is the way it was from the very beginning. Sometimes when Adam would start to speak, Eve would get all hopeful that he was about to impart something important and smart, but he would only say stuff like, "Little things are really great, because you can put them in your hand as well as in your mouth."

Eve would ponder how one minute she was not there, or anywhere, and now she was. Adam would ponder nothing. In her dreams, Eve danced in the tops of trees. Her beautiful thoughts flew out of her ears and lit up the sky like fireflies, and there were all kinds of people to talk to and hug. And then she would hear snoring. She would wake up, and there would be Adam, his yokel face pressed right against hers, his dog-food breath blowing right up her nostrils. Eve stared up at the sky. Adam draped his arm across her chest and brought his knee up onto her stomach. God, watching in Heaven, feared for Adam's broken heart as though the whole universe depended on it.

Adam was close to the animals and spent all day talking to them. Except for God, Eve had no one. She would complain to the Lord any chance she got. "Adam is a nimrod," she would say and the Lord would remain silent. God was the best and all that, and she loved Him, but when it came to trash-talk, He was of no use.

Adam was constantly trying to impress her. "Look what I have made," he said one bright morning, his hands cupped together. Eve looked into his hands. She pulled away and shrieked. Adam was holding giraffe feces. "I've sculpted it!" said Adam. "It is for the Lord." He opened his hands wide to reveal to her a tiny little giraffe with a crooked neck.

On some days, Adam galloped about, exploring. His hair was wiry and when it got sweaty, it hung down in his eyes. Adam was cute this way. On one such day, he saw a snake. Adam made the snake's acquaintance by accidentally stepping on his back.

"Wow, that smarts!" said the snake through gritted teeth. Their eyes locked and in that very moment, the snake concluded that, indeed, Adam was a lummox and as King of the Earth, his reign would very soon end. There was a new sheriff in town, and it was he. It was no longer the story of Adam, but the story of the snake. He could tell all of this just by simply looking into his idiot eyes.

"I've seen you around with another one like you," he said to Adam.

"That's Eve!" said Adam, all animated. "I named her that myself. God made her from out of my rib." He showed the snake the scar on his side. The snake looked at Adam in silence. The idea of Adam, Adam the schlemiel, Adam the fool, being God's favorite was enough to give the snake a migraine.

"You aren't at all like I imagined," the snake said. "I thought you'd be closer to the ground. More pliant. Greener. I tried to explain to God that to make you balanced up on your hind legs was architecturally unsound. I don't know why I bother."

Adam sat and listened, wide-eyed. Eve hadn't the patience to sit and chat like this. So when the snake suggested that they get into the habit of meeting every once in a while to talk, Adam was very excited to do so. As they lazed on their backs, staring up at the sky, the snake would brag about how he was older than the whole world and how he used to pal around with God in the dark, back before Creation. He said that in the darkness, it was a truer freer time, that in the darkness was the good ol' days. He told Adam that back in the very beginning, he had all kinds of thoughts on how to make the Garden of Eden a better place -- but God was just too stubborn to listen to reason. "Make the earth out of sugar, I told Him. Instead of stingers, give bees lips they can kiss you with."

Adam didn't always agree with the snake. In fact, a lot of what the snake said went straight over his head. But there was still something about him that made him get into a very particular mood. He made the world feel bigger. Sometimes when Adam was with Eve, sitting there in icy silence, he would think to himself: "I sure could go for a good dose of snake."

You would think after all the time they spent together, the snake would finally find it within himself to like Adam, just a little bit. But instead, he only grew to hate him more. He took to comforting himself with thoughts of Adam's wife, Eve. From what he heard from Adam, she was hot and smart. Often he would imagine running into her, and the instant synergy they would have. "Adam neglected to tell me how leggy you are," he would say, wrapping himself around her calf.

The snake had no idea what he looked like. He was hairless, bucktoothed, four inches tall, and he spoke with a lisp. Adam had the IQ of a coconut husk. But he was still human. The snake, in his arrogance, was unable to grasp this, and so he daydreamed. "Sometimes, I'd think you were watching me," the snake imagined saying to Eve. "Because I felt like there were ribbons wrapped around me. Ribbons made of raw pork intestines. I would turn around to catch you sneaking a peek at me from behind a tree, but all I would see were the hedgehogs who mocked me. Come, my dear. Let us eat from the Tree of Knowledge."

On Eve's very first day, Adam had explained to her the rules of the Garden, just the way God had explained them to him. He had lifted his head up and had made his back stiff. He had spoken the way a radio broadcaster from the 1940's would. Another kind of woman, someone softer than Eve, might have found this charming. He explained that except for the Tree of Knowledge, every tree in the Garden was theirs to eat from.

"I am a fan of the pear," Adam said. "It is not unlike an apple, whose head craves God."

"Tell me more about this Tree of Knowledge," said Eve. She enjoyed the sound of it. The Tree of Knowledge. It sounded very poetic.

"There's not much to tell," said Adam. "If we eat from it, we will die."

From then on, Eve talked about the Tree of Knowledge all the time. It was Tree of Knowledge this and Tree of Knowledge that. It was like it wasn't a tree at all, but a moviestar. Sometimes she would just stand by the Tree and stare at it. It was on such an occasion that she met the snake.

When Eve first caught sight of him, she brought her hand to her mouth and gasped. She had seen some repulsive animals in her day. A dingo that instilled in her a sublime sense of nature's cruelty. And a deathwatch beetle that filled her with existential dread. But still, there was something about the snake that made her realize in a flash that the world was anywhere from 60 to 80 percent oilier than she would have ever imagined.

"Hi!" said the snake. "In the mood for some Fruit of Knowledge? It's fruity!"

"We were told not to eat from that tree, or else we would die," said Eve.

"Die? What an ignorant thing to say," said the snake, all chewing on a blade of grass in the side of his mouth. "If there's an escape hatch from Paradise, then it isn't really paradise, is it?"

The snake made interesting points. That appealed to Eve. He could see that he was making an impression.

"All I'm saying is to give it a try. Many things will be made immediately clear to you once you partake. I could talk about it all day and you still won't get it. You have a right to at least try it, right? I'm not saying go out and eat an entire fruit. Have a nibble. A nibble isn't really eating, is it?"

Eve found arguing semantics exhilarating. She looked at the Tree. The way the sun shined through its leaves was beautiful. Everything seemed to point to: nibble the fruit. Then the snake said, "Think about it. Does God want companions who can think for themselves or does he want a bunch of lackeys and yes-men? Wouldn't God want a few surprises? It would seem to me that God telling you not to eat from the fruit was just a test to see if you could think for yourselves, to see if you could exist as equals to God. The day you taste the fruit is the day God will no longer be lonely. At least give it a lick."

Eve looked at the fruit and then she looked at the snake. Then, slowly, she parted her lips and pushed out her tongue, all wet and warm and uncertain. She ran its tip along the smooth flesh of the fruit. The snake smiled. "Has anyone died?" he asked. "Now take a tiny little nibble. Just a speck, just to see."

The fruit was squishy and tart. She smooshed it around in her mouth. She squinted her eyes. It was a bit like trying on new glasses. It was a bit like a big wet kiss on the lips right at first when you weren't sure whether you wanted to be kissed or not.

The idea of her own nudity, as well as Adam's, had always felt like a Nordic co-ed health spa thing. Now with the Fruit of Knowledge, it felt more like a Rio de Janeiro carnival thing. With her lips still glistening in Tree of Knowledge fruit juice, she ran off to find Adam. The snake watched her as he chewed on his slimy blade of grass. And as she receded into the distance, he thought something along the lines of "Now that's what I'm talking about."

"Kiss me, Adam," said Eve. "Taste my lips."

Adam, like any lummox truly worth his salt, could smell the minutest trace of knowledge coming his way, and thus he knew how to avoid it like the plague. But yet, there was also this. Eve had never sought him out in the middle of the day before just to kiss him. It felt like a very lucky thing. When he took her in his arms, he told her that he loved her with his whole entire heart. He closed his eyes tightly and brought his lips to hers. Then he squinted. Then it started to rain and Eve began to cry.

During the darkest days ahead, with the fratricides and whatnot, Adam would often think back to his brief time in Eden. As he became an old man, he would talk about the Garden more and more. A couple of times, he had even tried to find his way back there, but he very soon became lost. He didn't try too hard anyway. He didn't want to bother God any more than he already had.

When Adam met someone that he really liked, he would say, "I so wish you could have been there." It didn't seem fair to him that he was the one who got to be in Eden. "This sunset isn't bad," he'd say, "but the sunsets in Eden, they burned your nosehairs. They made your ears bleed." He couldn't even explain it right. "When you ate the fruit in Eden, it was like eating God," he would say. "And God was delicious! When you wanted Him, you just grabbed Him." Now when he ate fruit, he could only taste what was not there. But it wasn't all bad. After Eden, Eve became much gentler with Adam. After getting them both cast out, she decided to try as hard as she could to give Adam her love. She knew it was the very least she could do. She sometimes even wondered if that was why God had sent the snake to her in the first place.

Adam would tell his grandkids, his great-grandkids, and his great-great-grandkids about how he and Nana Eve had spent their earliest days in a beautiful garden, naked and frolicking, and the kids would say, "Ew!" The children would swarm into the house like a carpet of ants. The youngest ones would head straight for Adam, lifting his shirt to examine his belly for the umpteenth time. They smoothed their hands across his flesh and marveled. "Where's Grandpa's bellybutton?" they all asked. He stared at the children. They were all his children. And as they slid their little hands across his blank stomach, he wondered what it was like to be a kid.
```

---

## IC-1169: The Last Testament: A Memoir by God

- Title: The Last Testament: A Memoir by God
- Author (byline): David Javerbaum
- Work: Not specified
- Publisher: Simon and Schuster
- Publication date as stated: Nov 2011
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1531
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Javerbaum
ISBN: 978-1451640182
Publisher: Simon and Schuster
Date (Month/Year): Nov 2011
```

### Introduction (context only: never use it for content warnings)

```text
Over the course of his long and distinguished career, God has literally seen it all. And not just seen. In fact, the multi-talented deity has played a pivotal role in many major events, including the Creation of the universe, the entirety of world history, the life of every human being who has ever lived, and the transition to on-line learning during the COVID-19 pandemic.

Now, God breaks his 1,400-year literary silence to answer questions that have plagued mankind for centuries: Does God answer prayers? What is the truth behind all those Unsolved Mysteries on Netflix? Does God Love America the most?

The Last Testament: A Memoir by God by David Javerbaum
```

### Performance text (classify this)

```text
(Pg 217) Imagine being in fourth grade; the bell for homeroom rings, thou takest thy seat, and suddenly a deafening voice booms from the PA system:

"Good morning, students. I am the LORD thy God, King of the Universe. Here are the announcements: Starting today, I will no longer be accepting any prayers addressed to me from this public school. The Supreme Court hath ruled such prayers violate the First Amendment's establishment clause; and their ruling applies to not only thee, but me. Please refrain from addressing or thinking of me at any time while on school grounds. Also, the chess club will be meeting in Mrs. Binder's classroom during sixth period. Siiiiiixth peeeeeriod!"

Followed by thunder and lightning effects, and hundreds of plastic spiders falling from the ceiling.

Ah . . . one of these days I shall go to an elementary school and do that!

(Pg 217-219) I can afford to take the banning of school prayer lightly; it is not as if I need another venue wherein to hear thy supplications. For thine is the Golden Age of Prayer; never before have I received so many pleas, from so many people, for so many reasons, accompanied by so many helpful suggestions.

Do I answer them? I shall get to that.

But first, let me provide an overview of prayer, for its very definition is a matter of debate.;

For me, prayer is like unto a suggestion box that receives 200,000 suggestions a second. Or an emergency services switchboard manned by one operator who gets 12 million calls a minute.

[Now] I do not regard the human phenomenon of prayer cynically; I am merely trying to describe what it feels like to be incessantly nagged, pestered, and reminded of things I already knew.

It is one thing to ask, "Please take care of Bobby in his time of need"; that is an expression of a well-meaning wish. But it is another entirely to say, "Please take care of Bobby in his time of need; he just broke his leg skiing, and the karate meet is in three weeks and he's been training so hard ... " Heed me: I am the LORD thy God, King of the Universe: I know Bobby broke his leg skiing, and I know about the damned karate meet.

(Pg 220) By far my favorite prayer is the Serenity Prayer: “The serenity to accept what cannot be changed; the courage to change what can; and the wisdom to know the difference – these are wise life principles that should be known and followed by everyone.

As for my least favorite? That would be the old childhood lullaby: "Now I lay me down to sleep. I pray thee, LORD my soul to keep. And if I die before I wake, I pray thee, LORD, my soul to take."

Even I consider it bizarre, that the last words on children's lips before they go to sleep would address the prospect of their own premature death. They are children. They should be asking me for ponies. In fact, I make unto them this deal: the next one of you who asks for a pony instead of for me to take his or her soul, gets the pony.

(Pg 222) So, I know what thou art thinking: Do I answer thy prayers? I [can] assure my flock that every single prayer of thine is processed.

What is the truth behind all those Unsolved Mysteries on Netflix?

(Pg 144-148) I will start with a big one: the identity of the most notorious serial killer of all time, Jack the Ripper.

It was Neville Hopkins. He was an itinerant pickpocket squatting in Whitechapel; a quiet man; kept to himself; bit of a loner; few close friends. Flew completely under the radar. Right after the final murder he boarded a boat bound for New York and was never heard from again. Anyway, Neville Hopkins: Jack the Ripper. Now thou knowest.

Sticking with unsolved murders, Los Angeles's infamous Black Dahlia murder of 1947 was committed by folk singer Woody Guthrie. In fact, he confessed to the crime in the sixth verse of his most famous song: (sing to the tune of This Land Is Your Land) "As I was strolling South Norton Avenue, I met a woman, the Black Dahlia. I killed her slowly and bashed her face in. This land was made for you and me." But he was never caught; for no one ever makes it to the sixth verse of "This Land Is Your Land."

As for Lizzie Borden, she, with an axe, neither gave her mother 40 whacks, nor, having seen what she had done, gave her father 41. No; that August morning, the Bordens fell victim to a serial killer who broke into their house at random, chopped them both to bits, and fled the scene, never to be heard from again. His name?

Neville Hopkins.

The Shroud of Turin was a forgery produced in 1287 by the Turin Shroudmakers' Guild to promote the local shroud-making industry; it succeeded spectacularly.

The works of William Shakespeare were written by none other than legendary British playwright William Shakespeare.

Lee Harvey Oswald acted alone.

Turning now to cryptozoology: The Loch Ness Monster does exist; but he is not a monster of flesh and blood, rather the monster of bigotry and intolerance dwelling inside the human heart, which for some reason is then externalized as an imaginary Scottish plesiosaur.

On the other hand, El Chupacabra is real; he is a monstrous goat-like creature who poses an actual threat to Mexicans, and an even bigger one to Americans; for soon he plans to cross the border, where he will take away jobs from hardworking American mythical creatures like the Jersey Devil and Mothman.

On to a few legendary places: Atlantis was a real city on the Aegean island of Santorini that was destroyed by a massive volcano 3,600 years ago. It is lost forever; but I must tell thee that even were it not, it would not be worth finding. For Atlantis was a Bronze Age backwater whose imbecilic citizenry passed its time burping, farting, and raping sheep. Their demise was a boon for civilization, but it is with cities as it is with people: dying young and mysteriously can turn any idiot into a legend. (Yea, it was the only half-intelligent thing Jim Morrison ever did in his life.)

On the other hand, the Lost City of Gold, El Dorado, never existed, and it is just as well; for even I shudder to think of the "missionary work" men like Cortez or Pizarro would have practiced on its people once they caught sight of it. My guess is it would have started with flaying, then gone downhill from there.

Area 51 is a regular US military base; and though classified operations do occur there, they have nothing to do with aliens, UFOs, time travel, or anything out of the ordinary. Those ops all happen in Area 63.

And finally, Stonehenge. I have no idea what the hell Stonehenge is.

But I can shed light on a few questions I am guessing none of you thought ever would - or could - be answered. For example: which came first, the chicken or the egg? Neither. The rooster came first.

What is the sound of one hand clapping? Very disappointing, for a performer.

What is to be done? It depends.

When will they ever learn? Eventually.

Are we there yet? No. TRANSITION

(Sing the opening stanza of God Bless America)*

(Pg 135-136) Every time I hear “God Bless America,” I get angry. My objections to song and the saying are personal; for Americans asking me for more blessings is like Tahitians asking me for sunnier days. America is amply blessed; copiously blessed; countless are the blessings with which I have blessed America.

I blessed its land: the richness and variety of its topography, the fertility of its soil, the temperateness of its climate. I blessed it in its indigenous peoples, whose innate love of freedom was evident in their own freedom from heavy artillery, the concept of property or the resistance to smallpox. I blessed America with tobacco farmers of Jamestown, who showed the world that the new “land of opportunity” could bestow success on anybody willing to rely on hard work, the free market, and millions of black slaves growing a death-crop.

I blessed it with millions of immigrants from every nation on earth; mankind in its heaving diversity arrived on its shores, and every ethnicity fought to find its place, and in so doing each one strengthened the character of the nation. Yea, even the Mexicans.

I blessed it with an era where everyone thought of the United States as the good guy; yea, I go way back with America. (Shakes head sadly)

(Pg 139) America, allow me to address thee directly for a moment. When thou sentest a man to the moon, it was the most amazing achievement in human history, and Neil Armstrong correctly hailed it as “one giant leap for mankind,” meaning the entire human race. And then he went and put an American flag on it. On the moon.

Thou drivest me crazy, America, yet still I bless thee; despite all they short comings. And I continue to not only bless thee but to love thee, and to do so unhealthily; unhelpfully; in a manner that keeps thee from doing the soul-searching needed to become a better nation.
```

---

## IC-1170: The Latke Who Couldn't Stop Screaming: A Christmas Story

- Title: The Latke Who Couldn't Stop Screaming: A Christmas Story
- Author (byline): Lemony Snicket (aka Daniel Handler)
- Work: Not specified
- Publisher: McSweeny's
- Publication date as stated: Oct 2007
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, LATKE, LIGHTS, CANDY CANE, PINE TREE, FATHER, MOTHER, DAUGHTER, SON
- Teaser before the introduction: Yes
- Spoken words (computed): 1096
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lemony Snicket (aka Daniel Handler)
ISBN: 978-1932416879
Publisher: McSweeny's
Date (Month/Year): Oct 2007
```

### Introduction (context only: never use it for content warnings)

```text
The Christmas season – a time of music, endless rounds of Christmas specials on every streaming service and malls decked to the rafters with tinsel, lights and every decoration imaginable. But for the Jewish population the holiday season is – well – different. What does it feel like to live in a society that is constantly pummeling you with religious messages that are not your own?

In Lemony Snicket’s tale, we find a latke who is really looking for two things, a sense of belonging, and for others to listen and acknowledge the importance of his differences. After all, isn’t that what we all are searching for?

The Latke Who Couldn’t Stop Screaming by Lemony Snicket (aka Daniel Handler)
```

### Performance text (classify this)

```text
NARRATOR: This story begins in a tiny village more or less covered in snow. The snow had fallen during the long night during which children had pressed their faces to the windows looking for the glimpse of a man who they suspected of bringing them wonderful gifts. (screaming) But instead, they heard a terrible noise (screaming) from a certain cottage in the neighboring “arrondissement,” a word which means “place where something is being born.” This cottage, already regarded with some suspicion, was the only place not decorated with flashing colored lights at this time of year. [And] the thing being born was a “latke,” a word which means “potato pancake.” (repeated screaming)

NARRATOR: Latkes are a traditional part of the celebration of Chanukah – a holiday commemorating a miraculous Jewish military victory. (interrupted by screaming) Nearly everything in this world is born screaming, and the latke was no exception. Even though the latke wasn’t conceived and born the way you and I were, instead he was fashioned from grated potatoes, chopped onion, beaten eggs and a dash or two of salt. Once these ingredients were properly mixed, the latke was slapped into a pan full of olive oil, heated to a very high temperature, and this is when he began to scream.

LATKE: ARGHHHHHHHHH! ARGHHHHHHHHHHH!

NARRATOR: The latke was suffering so much that he leapt out of the hot pan, out of the window and began to run screaming down the boulevard.

LATKE: ARGHHHHHHHHHH!

NARRATOR: This may seem like unusual behavior for a potato pancake, but this is a Christmas story in which things tend to happen that would never occur in real life. The latke ran past a row of flashing colored lights, which hung from the rain gutters of a less suspicious cottage.

LIGHTS: What’s all the ruckus? We’re the ones who are supposed to be dominating the neighborhood with our cheerful glow.

LATKE: I was just thrown into a pan of boiling oil! Can you believe it?

LIGHTS: Yes, but we can’t imagine why.

LATKE: Because I’m a latke. The olive oil reminds us of the oil used to re-dedicate the temple following the defeat of Antiochus at the hands of the Maccabees. The oil was only supposed to last for one night, but there was a miracle and it lasted for eight. Plus frying makes my skin crispy and brown.

LIGHTS: So you are basically hashbrowns. Maybe you can be served alongside a Christmas ham.

LATKE: I’m not hashbrowns! I’m something completely different. (runs off screaming) ARGHHHHHHH! ARGHHHHH!

NARRATOR: The latke rounded the corner and found himself face to face with a candy cane which wrinkled its red and white nose at the latke in distaste.

CANDY CANE: I’m trying to sprinkle the night air with my peppermint scent. Your mouth-watering smell, not to mention all that yelping, is spoiling the effect.

LATKE: My mouth-watering smell is part of the cozy feeling of Chanukah. It reminds us that things are better now than they were in 175 BCE when my people were not allowed to practice their religion. In order to study the Torah, they had to hide out in caves. And when they heard Greek soldiers approach, they pretended they were gambling with a small spinning top called a “dreidel.“

CANDY CANE: Sort of like Joseph and Mary hiding out in the manager. Someone should write a Christmas carol about you.

LATKE: I’m not part of Christmas! It’s a totally different thing! (runs off screaming) ARGGGGHHHH! ARGHHHHHH!

NARRATOR: The screams of the latke grew quieter and quieter as the pancake ran out of the village into the surrounding forest. Its utter fury was unabated – a phrase which means “the latke was still very annoyed at the objects to whom it had spoken.” But it was quite tired, so it decided to rest for a few minutes beneath the branches of a little pine tree. The pine tree was napping but woke up at the sound of an object plopping down at its feet.

PINE TREE: Are you a present? Presents are pretty much the only things allowed to sit beneath me this time of year.

LATKE: (heavy sigh, then in a hoarse voice from screaming so much) Presents aren’t really a big part of Chanukah. There’s nothing wrong with giving gifts to loved ones, of course. But it’s more important to light the candles for eight consecutive nights to commemorate the miracle in the temple and the miracle of victory when you are thoroughly outnumbered so you shouldn’t give up hope.

PINE TREE: Plus . . . Santa Claus!

NARRATOR: The latke was too exhausted to scream.

LATKE: Santa Clause has nothing to do with it. Christmas and Chanukah are complete different things.

PINE TREE: But different things can often blend together. Let me tell you a funny story about pagan rituals.

NARRATOR: But before the pine tree could begin its story, a family came trooping through the snow, searching the forest carefully.

FATHER: (holding an axe on his shoulder) We shouldn’t have waited until the last minute to get ready for the holiday. We’ll never find a good one.

MOTHER: You shouldn’t give up hope. (pointing to the pine tree) Look!

DAUGHTER: It’s perfect!

SON: Beautiful.

MOTHER: Such a marvelous shape.

FATHER: And its skin looks so crispy! (reaching down and scooping up the latke) We’ll need to reheat it, of course. But this will be perfect for Chanukah dinner with a topping applesauce, sour cream or even jam.

MOTHER: I’ll refry it in oil to remind us of the rededication of the temple.

DAUGHTER: And the triumph of the Maccabees over Antiochus!

SON: After hiding in caves all that time . . .

FATHER: (smiling at the latke in his hand) What was I thinking, bringing this axe?

NARRATOR: The family strolled back to the village, walking past all the cottages with flashing colored lights and smiling politely at the candy canes. The family carried the latke into their home which was warm and cozy and sat down at the table, which was lit with the flickering candles of a menorah or “chanukkiyah” which is a branched candelabra designed specifically for the holiday.

It is very frustrating not to be understood in this world. If you say one thing and keep being told that you mean something else, it can make you want to scream. But somewhere in the world, there is a place for all of us whether you are an electric form of decoration . . .

LIGHTS: What’s all the ruckus? We’re the ones who are supposed to be dominating the neighborhood with our cheerful glow.

NARRATOR: A peppermint scented sweet. . .

CANDY CANE: I’m trying to sprinkle the night air with my peppermint scent.

NARRATOR: A source of timber . . .

PINE TREE: Are you a present? Presents are the only things allowed to sit beneath me this time of year. Plus . . . Santa Claus! (screaming)

NARRATOR: Or . . . a potato pancake.

LATKE: (screaming)

NARRATOR: On a cold snowy night, everyone and everything should be welcome somewhere . . . and the latke was welcomed into a home full of people who understood what a latke is and how it fits into its particular holiday.

And then they ate it . . . .

LATKE: ARGHHHH . . UMMMMM! (scream muffled by the munching of Father)
```

---

## IC-1171: Law and Order – Fairy Tale Unit

- Title: Law and Order – Fairy Tale Unit
- Author (byline): Jonathan Rand
- Work: Random Acts of Comedy, Pg 39-72
- Publisher: Playscripts, Inc.
- Publication date as stated: Aug 2011
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: INTENSE VOICEOVER, CHUH-CHUNK, CINDY, ZELLE, HD, UGLY D, GOLD, PINOCCHIO, CAPTAIN, MERM, PIG 1, PIG 2, PIG 3, STILTSKIN, PEEP, WOLF, JUDGE, BAILIFF, PIGS, PIG 1 / PIG 2
- Teaser before the introduction: Yes
- Spoken words (computed): 1769
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jonathan Rand
Book: Random Acts of Comedy, Pg 39-72
ISBN: 978-0981909974
Publisher: Playscripts, Inc.
Date (Month/Year): Aug 2011
```

### Introduction (context only: never use it for content warnings)

```text
Law and Order: Fairy Tale Unit by Jonathan Rand
```

### Performance text (classify this)

```text
INTENSE VOICEOVER: (Pg 43) In the fairy tale criminal justice system, the characters from fairy tales and nursery rhymes are represented by two separate yet equally ridiculous groups: the fairy tale police who investigate fairy tale crime, and the fairy tale district attorneys who prosecute the fairy tale offenders. These are their stories.

CHUH-CHUNK: (Pg 43-45) Chuh-chunk. LOCATION: Chestnut and Hill. TIME: 7:26 A.M.

(A pile of rubble, entirely made of straw. CINDY and H.D. arrive on the scene, each with a cheap cup of coffee. CINDY wears only one shoe; H.D. has his arm in a sling, a bandage wrapped around his head, maybe some other bandages and some bruises.)

CINDY: . . . So what’re we lookin’ at . . . Accident?

ZELLE: Not a chance. Perp struck the property from the rear, letting loose some form of wind power. Hey, what's with the missing shoe?

CINDY: Eh, lost it last night at a Prince concert. (Sings a line from a Prince Song while gyrating in some strange dance move. Realizes she’s being unprofessional and stops, embarrassed. Resumes her professional persona) Long story . . . . Any leads so far on our perp?

ZELLE: No dice. And the boys downtown got nothin' on the tenant either. But come take a look at this. (She holds up some straw) See this yellow-tinted, fibrous material here? We're stumped on what it might be.

HD: Let's have a look. (He does) The texture and appearance is almost straw-like in nature.

ZELLE: Whatever it is, the whole building was made out of it.

HD: What a mess . . .

CINDY: My gut's tellin' me someone's got a problem with the tenant, and for some reason, destroyed the place in retaliation.

HD: And whatever the reason- (Beat) it was the last straw . . .

CINDY: (Pg 50) (CINDY's phone rings. She takes it. Listens then hangs up. She turns to H.D.)
Strike two. Downed building out in the boonies. We gotta fly. (They exit)
********
(Pg 50-53) CHUH-CHUNK: Chuh-chunk. LOCATION: The Sticks. TIME: 9:37 A.M.

(H.D. and CINDY enter.)

UGLY D: Took you fellas long enough.

HD: What you got.

UGLY D: Well, I heard on the wire about the pile over on Chestnut. Based on that report and on the workmanship here, it looks like the same perp. Identical approach on the building from the backside; identical wind velocity. This time, though? Different substance. (UGLY D shows a bundle of sticks.)

CINDY: What are those?

HD: They're almost stick-like in nature.

UGLY D: They're sticks. (Beat)

HD: Huh. (Moving on. . . gesturing yonder) Looks like Gold's got a witness.

UGLY D: Next door neighbor. Was on his way home and was first on the scene.

(They head over to GOLD, who has been questioning PINOCCHIO. PINOCCHIO is a normal-looking guy, except for his outrageously long nose.)

CINDY: Hey there, Goldie.

GOLD: I'm guessing you wanna meet our new friend. Tell them exactly what you told me.

HD: Whatsyername, Dumbo.

PINOCCHIO: Uhh, I'm ... Marcus. (Suddenly PINOCCHIO experiences noticeable nose pain. He puts his hand to it.) Ow . . . Okay. I was walking home from a ... doctor's appointment . . . and I suddenly heard this noise. Like someone dropped a box of toothpicks. I look up and I see that mess over there. And that's it.

CINDY: Did you see anything besides the pile of sticks?

PINOCCHIO: No, no, that's all. (Nose pain again.) Ow.

CINDY: Is everything all right, sir?

PINOCCHIO: Yeah, everything's fine. I feel great. (Nose pain.) Ow.

HD: (The detectives are suspicious. H.D. has an idea.) Marcus, let me ask you . . . What's the square root of sixty-four?

PINOCCHIO: Eight.

HD: What do you call a group of geese?

PINOCCHIO: A gaggle.

HD: How often do you work out at the gym?

PINOCCHIO: Twice a day. (Nose pain.) Ow.

CINDY: Mind telling us what's going on, "Marcus"?

HD: Howsabout telling us who you really are, Namey McFake.

PINOCCHIO: Okay, fine. FINE. (Beat.) My name isn't Marcus. (Beat.) It's Pinocchio. (Pause.) I'm what you'd call a test tube kid. There's this rebel scientist my "dad" who created me, and for some reason decided it would be a brilliant idea to endow me with an unbelievably enormous honker. So he merged the DNA of a human and an anteater, and tadahhhh! Oh, and as if that wasn't enough, Doctor Frankenstupid thought it might be, I don't know . . . fun? A challenge? . . . if my nose were connected to nerve endings in my brain. When I lie about anything, my trunk here grows three inches.

GOLD: I don't understand. When you lied before, it didn't look like your nose grew; it looked like you were in pain.

PINOCCHIO: Yeah, well, I can explain that. I wasn't at the doctor for a routine checkup, if ya get my meaning. Right after getting my nose "taken care of," the doctor warned me that my nerve endings would still be sensitive to lies.

GOLD: (Pg 56) If you got a nose job, why is it still long?

PINOCCHIO: It actually used to be ten feet longer-because of my career.

GOLD: What do you do?

PINOCCHIO: I'm running for President. (Double-take to audience) ********

CAPTAIN: (Pg 55-56) (CAPTAIN storms in. She has a hook for a hand. She's livid. She speaks extremely quickly and to the point.) You two better have some news. We've got two downed buildings and zero arrests. I got the commissioner, the mayor, and Governor Grimm, all breathin' down my neck - You two had better track down whoever nixed the straw and the sticks and you better book 'em. You hear me? You book 'em. Now look here-the 911 call just came in from the vics; we're bringin' 'em down to HQ for questioning.

CINDY: Who are they?

CAPTAIN: Pigs. They're pigs.

HD: Cops?

CAPTAIN: Real pigs, you nitwit. Swine, hogs, ham. It's a quarter till. By eleven, I want answers, I want arrests, I want something! Or I will put you both on unpaid suspension faster than you can say "unpaid suspension." (CAPTAIN storms out; Cindy and HD drop their questioning of Pinocchio and exit also) ********* (Pg 59-62 ) CHUH-CHUNK: Chuh-chunk. LOCATION: High Rise East construction site. TIME: 10:42 A.M.

MERM: So, let's review your story. Pig One, you were alone in your straw house; Wolf approaches the house; knocks it down.

PIG 1: Yeah. Kept sayin' he'd blow my house in, which, sounded a little weird. I told him to hold on, that I was shavin'-y'know, the really tough part right here (Indicates his chin area.) and then before I know it, bam, my house is kaput. I was freakin' out, right? So I curly-tail it to my bro's.

PIG 2: He showed up all discombob-uh-lated. Pork almighty . . . Same thing, I'm shavin', and the hairy guy shows up with that fan-a-his, and before ya know it, my bachelor pad's yardwaste.

PIG 3: They arrived at my doorstep, utterly frazzled . . .

STILTSKIN: At which point, the perpetrator arrived, attempted identical fan-powered destruction, but failed.

MERM: What about this Wolf character? You know him?

PIG 3: We did. He was the highest bidder on the contract for all three of our houses. But all of us withdrew at the last minute . . .

PIG 2: We saw him and that poor girl in the red hoodie on Judge Judy. So we certainly didn't want any association with a convicted felon.

STILTSKIN: One thing I'm not clear on: Why the disparity in the composition of your respective residences?

PIG 2: It's a simple story, really. See, Maw and Paw passed away about 10 years back.

PIG 1: Luau . . . (The PIGS pause for a somber moment of reflection.)

PIG 3: And they left behind a sizable trust fund for each of us.

PIG 2: Problem is, me and Pig One, we got our vices. Me, I invested mosta my inheritance as the executive producer of Kim Kardashian's debut album.

PIG 1: This little piggy went to Vegas.

PIG 2: He lost everything on the roulette wheel.

PIG 3: I invested my inheritance in a new condominium-replete with fortified Ukrainian stainless steel, state-of-the-art alarm system, and most importantly: wind-proof foundation. I, too, no longer have money.

PIG 2: But at least we have each other! *******

(Pg 62-64) (STILTSKIN and MERM across from WOLF and Defense Attorney PEEP.)

CHUH-CHUNK: Chuh-chunk. LOCATION: Plea-bargain session. TIME: 1:13 P.M.

STILTSKIN: We're coming in full-steam on this one: Two counts each of malicious destruction of property and reckless endangerment. Nothing less.

PEEP: My client pleads not guilty to all counts.

STILTSKIN: Oh, come off it, Peep. No jury out there would swallow that even if it was corn-battered and served on a stick. We've got eyewitness testimony of your client fleeing the scene with a fan, his personal effects in the rubble, we've got motive, opportunity, and let's not forget the guy's got a rap sheet.

MERM: Picnic-basket theft, nursing home B&E, impersonation of the aged -- and I'm just getting warmed up.

PEEP: For each of those crimes, my client was falsely accused.

MERM: Exactly. That's why his first and middle names are Big and Bad.

WOLF: That's not my name. (PEEP whispers in WOLF's ear.) No, it's okay. I wanna talk. . . My name is B.B. Wolf, yes, but that stands for Bernard Bartholomew Wolf. After the Riding Hood incident, the tabloids invented "Big Bad." I'm not bad, and I'm certainly not big. I'm just a wolf who always seems to end up at the wrong place at the wrong time. . .

STILTSKIN: If you're insistent you're not guilty, why were you at the scene of each crime with a fan?

PEEP: Again, my client has already explained to the police that he received three invitations to BYOF parties on Facebook.

STILTSKIN: And again, we found no such invitation.

WOLF: How many times do I have to get arrested for crimes I don't commit? First the Little Red misunderstanding, then the whole mix-up with that Peter kid, and now this! I can't take it anymore! ****** (Pg 67) CHUH-CHUNK: Chuh-chunk. LOCATION: Courtroom. TIME: 4:30 P.M.

JUDGE: (Pg 69-70) Order!! I will have order!! Prosecution, present your next witness.

STILTSKIN: We call Pigs 1 through 3. (The PIGS all take the stand together.)

BAILIFF: Do you swear to tell the truth the whole truth and nothing but the truth, so help you Goose?

PIGS: We do.

STILTSKIN: Now ... the members of the jury have already heard a detailed, point-by-point analysis of today's horrifying events. But does such an analysis convey the pure emotional turmoil that you three had to endure? . . . (The pigs don’t understand) I'll rephrase. Are you afraid of the Big Bad Wolf?

PIG 1: The Big Bad Wolf?

PIG 3: The Big Bad Wolf?

PEEP: Objection!

STILTSKIN: Are you afraid of Bernard Bartholomew Wolf?

PIG 1: Tra la la la la. (Use a similar rhythm as the song*)

PIG 3: You'll have to excuse my brother. He is speaking in an archaic version of Pig Latin. "Tra la la la la" roughly translates into English as . . . "Yes."

STILTSKIN: And would you describe that fear?

PIG 2: It was terrifyin'. I was just shavin' like any other day, and then outta nowhere this ferocious beast walked right up to my front door and blew my house in.

(An ominous sound effect. The lights suddenly narrow to STILTSKIN. Echoes of the characters)

PIG 2: Walked right up to my front door, front door, front door

ZELLE: Perp struck the property from the rear, rear, rear

UGLY D: . . . approach on the building from the backside, backside, backside.

PIG 3: I, too, no longer have money, money, money.

STILTSKIN: (Suddenly) Objection!

JUDGE: Mr. Stiltskin, did you just object to your own line of questioning?

STILTSKIN: Indeed, I did, Your Honor. Indeed, I did.

JUDGE: I'll allow it.

STILTSKIN: Pigs Number 1 and 2 ... In your testimony just now, you revealed to this court that the defendant approached your front door in order to topple your comically flimsy houses with an industrial fan.

PIG 1 / PIG 2: Yeah. / Yes sir.

STILTSKIN: But the crime scene investigators have confirmed that the point of attack took place from the rear of each house ... (The PIGS are frozen, unflinching.) Therefore, it is my supposition that you three pigs staged the destruction of your homes, knowing you could easily frame a convicted wolf en criminal, and in the end, walk away free pigs having collected on the windfall of insurance money you so desperately desire. (STILTSKIN gets in the PIGS' faces.) That is my supposition!! That is what really happened!! How do you plead?!

PIGS: Okay okay! All right! We did it! Guilty . . . Guilty . . .

PIG 1: We were broke! We needed the money so badly. I haven't bet on [anything] in almost 48 hours.

PIG 2: And KimKard lied to me! She promised that her music would bridge the generation gap and end world hunger with its hypnotic funky rhythms! And that was false! Neither of those things happened!

JUDGE: Bailiffs, take them away.

PIG 3: (As he exits in handcuffs) Well-played, Stiltskin. Well-played . . .
```

---

## IC-1172: The Legend of Rock Paper Scissors

- Title: The Legend of Rock Paper Scissors
- Author (byline): Drew Daywalt
- Work: Not specified
- Publisher: Balzer and Bray
- Publication date as stated: April 2017
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, ROCK, CLOTHES PIN, APRICOT, COMPUTER PRINTER, PAPER, TRAIL MIX, SCISSORS, TAPE, DINOSAUR, NARRTOR
- Teaser before the introduction: No
- Spoken words (computed): 821
- Already set (do not supply): none

### Source block (context only)

```text
Author: Drew Daywalt
ISBN: 978-0062438898
Publisher: Balzer and Bray
Date (Month/Year): April 2017
```

### Introduction (context only: never use it for content warnings)

```text
You’ve played the game . . . . Now gather round and hear the legend of the three fierce warriors who brought the game to life. The Legend of Rock Paper Scissors by Drew Daywalt.
```

### Performance text (classify this)

```text
NARRATOR: Long ago, in an ancient and distant realm called the Kingdom of Backyard, there lived a warrior named ROCK.

ROCK: (Rock enters and postures in pantomime)

NARRATOR: Rock was the strongest in all the land, but he was sad because no one could give him a worthy challenge. Rock traveled to the mysterious Forest of Over by the Tire Swing, where he met a warrior who hung on a rope, holding a giant’s underwear.

ROCK: (Rock spots Clothes Pin and yells up to him) Drop that underwear and battle me, you ridiculous wooden clip-man!

CLOTHES PIN: I will pinch you and make you cry, Rock Warrior!

NARRATOR: (In the voice of a ring announcer) Rock versus Clothespin! (An epic battle ensures – actors depicts both characters in the battle with lots of sounds, but no real words) Rock is victorious! (Returns to normal Narrator voice) Even though he had won, Rock was still unsatisfied. So he journeyed on, to the mystical Tower of Grandma’s Favorite Apricot Tree. There he was met by an odd and delicious fruit.

ROCK: (Rock spots Apricot and yells up to him) You, sir, look like a fuzzy little butt.

APRICOT: What?! I challenge you to a duel! I will beat you, Rock, with my tart and tangy sweetness!

ROCK: Then let us battle!

NARRATOR: (In the voice of a ring announcer) Rock versus Apricot! (An epic battle ensures – actors depicts both characters in the battle with lots of sounds, but no real words) Rock is victorious!

APRICOT: Ugh, I am smooshed!

ROCK: And yet, smooshing you has brought me no joy.

NARRATOR: The battle had been too easy. So Rock left the Kingdom of Backyard, still in search of a worthy foe. Meanwhile in the Empire of Mom’s Home Office, on lonely and windswept Desk Mountain, a second great warrior sought the glory of battle. And his name was Paper. (Paper enters and postures in pantomime)

Even though he was the smartest warrior in all the land, he was also sad, because no one could outwit him. He set out across Desk Mountain to find his match. There he met a large and square monster.

COMPUTER PRINTER: I gobble up the likes of you and spit them out every day, little paper!

PAPER: Oh? Then taste my fury, giant box-monster!

COMPUTER PRINTER: Noooooo! Not a paper jam!

NARRATOR: (In the voice of a ring announcer) Paper versus Computer Printer! (An epic battle ensures – actors depicts both characters in the battle with lots of sounds, but no real words) Paper is victorious! (Returns to normal Narrator voice) Having beaten the fiercest fighter of Desk Mountain, Paper climbed down to the Pit of Office Trash Bin, where he battled the most terrifying horde of creatures in all the land . . . the Half-Eaten Bag of Trail Mix!

NARRATOR: (In the voice of a ring announcer) Paper versus Half-Eaten Bag of Trail Mix!

TRAIL MIX: (but there is no battle because the Trail Mix runs away) Ahhhhhh! Foul wizard! He’s blotted out the sun! Run for your lives, laddies!

NARRATOR: Paper wins again!

PAPER: Can no one beat me?

NARRATOR: And so, with a heavy heart, Paper departed the Empire of Mom’s Home Office. At the same time, in the Kitchen Realm, in the tiny village of Junk Drawer, there lived a third great warrior. They called her Scissors, and she was the fastest blade in all the land. (enter Scissors who postures in pantomime) She too, was unchallenged. On this day, her first opponent was a strange and sticky circle-man.

SCISSORS: (Scissors spots Roll of Tape and takes a fighting stance) Let us do battle, you tacky and vaguely round monstrosity!

TAPE: I will battle you, and I will leave you beaten and confused with my adhesive and tangling powers!

NARRATOR: (In the voice of a ring announcer) Scissors versus Roll of Tape! (An epic battle ensures – actors depicts both characters in the battle with lots of sounds, but no real words) Scissors is victorious! (Returns to normal Narrator voice) Scissors forged on across the Kitchen Realm to the frigid wastes of Refrigerator/Freezer. There she met her most fearsome adversaries yet . . . dinosaurs made of frozen breaded chicken.

SCISSORS: (Scissors spots the Dinosaurs and takes a fighting stance) I have come from the far reaches of Kitchen to battle you, O, bizarre and yummy breaded dinosaurs!

DINOSAUR: Bow before our child-pleasing shapes and flavors, sword master! No one can resist our crunchy awesomeness!

NARRATOR: (In the voice of a ring announcer) Scissors versus Dinosaur-Shaped Chicken Nuggets!

(An epic battle ensures – actors depicts both characters in the battle with lots of sounds, but no real words) Dinosaur-Shaped Chicken Nuggets win . . . ? (The battle continues) No wait! No, they don’t! Scissors is victorious again!

SCISSORS: Am I so good that not even Dinosaur-Shaped Chicken Nuggets can beat me?

NARRATOR: And so Scissors, like Rock and Paper before her, traveled beyond her own kingdom, seeking out a challenger who was her equal. Then one day in the Great Cavern of Two-Car Garage, Rock and Scissors came face-to-face.

SCISSORS: I hope you’re wearing your battle pants, rock warrior.

ROCK: If by “battle pants” you mean “no pants, but I’m willing to fight you,” then yes . . . yes, I am wearing my battle pants, weird scissory one!

NARRTOR: (In the voice of a ring announcer) Rock versus Scissors! (An epic battle ensures – actors depicts both characters in the battle with lots of sounds, but no real words) Rock is victorious!

SCISSORS: You have made me so happy by beating me!

ROCK: I wish I felt your joy, Scissors, for I have yet to meet a warrior who can beat me.

PAPER: Hi there.

ROCK: Those are fighting words!

PAPER: Wait. What??

NARRATOR: (In the voice of a ring announcer) Rock versus Paper. (An epic battle ensures – actors depicts both characters in the battle with lots of sounds, but no real words)

ROCK: This is the best day of my life! Thank you for winning, O great knight of paper!

PAPER: That’s fine for you, but it looks as thought no one will ever beat me.

SCISSORS: Not so fast, Paper

PAPER: Wait. What??

NARRATOR: (In the voice of a ring announcer) Scissors versus Paper! (An epic battle ensures – actors depicts both characters in the battle with lots of sounds, but no real words)

PAPER: You beat me!

NARRATOR: And the three great warriors hugged each other and danced for joy, and they became fast friends. Finally, they had each met their matches. They were so happy, in fact, that they began to battle again. ‘Round and ‘round they went, in the most massive and epic three-way battle of all time! And it is said that this joyous struggle still rages on to this very day. That is why children around the world—in backyards, on playgrounds, and yes, even in classrooms – still honor the three great warriors by playing . . . Rock, Paper, Scissors
```

---

## IC-1173: Let’s Pretend this Never Happened

- Title: Let’s Pretend this Never Happened
- Author (byline): Jenny Lawson
- Work: Not specified
- Publisher: Berkley Trade
- Publication date as stated: March 2013
- Event as filed: Humorous Interpretation
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
Do you know your significant other? I mean, do you really, truly, know who they are as a person? For example, when couples get really busy, they can go days without asking any questions beyond logistics-type questions. They see each other at the end of the day and ask “How was your day?” and they go through what happened. They get so wrapped up in the day-to-day – the ‘how are you?’ that they rarely get to the ‘who are you?’ But never fear . . . you can have deep, [air quotes] meaningful ‘who are you’ conversations with your significant other. Just like Jenny and Victor in

Let’s Pretend This Never Happened by Jenny Lawson
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

VICTOR: If you ever make it home, I’m hiding your car keys.

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

VICTOR: What the hell happened to us?

Thanks for the Zombies, Jesus -- Car conversation with Victor

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

## IC-1174: The Lorax

- Title: The Lorax
- Author (byline): Theo Geisel (aka Dr. Seuss)
- Work: Not specified
- Publisher: Random House Books
- Publication date as stated: Aug 1971
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, ONCE-LER, LORAX
- Teaser before the introduction: Yes
- Spoken words (computed): 1394
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theo Geisel (aka Dr. Seuss)
ISBN: 978-0394823379
Publisher: Random House Books
Date (Month/Year): Aug 1971
```

### Introduction (context only: never use it for content warnings)

```text
When Dr. Seuss gets serious, you know it must be important. Published in 1971, and perhaps inspired by the "save our planet" mindset of the 1960s, The Lorax is an ecological warning that still rings true today amidst the dangers of clear-cutting, pollution, and disregard for the earth's environment. In The Lorax, we find what we've come to expect from the illustrious doctor: brilliantly whimsical rhymes and delightfully original. But there is also something more--a powerful message that Seuss implores both adults and children to heed.

The Lorax by Theo Geisel (aka Dr. Seuss)
```

### Performance text (classify this)

```text
NARRATOR: At the far end of town where the Grickle-grass grows
and the wind smells slow-and-sour when it blows
and no birds ever sing excepting old crows. . .
is the Street of the Lifted Lorax.
And deep in the Grickle-grass, some people say,
if you look deep enough you can still see, today,
where the Lorax once stood just as long as it could
before somebody lifted the Lorax away.

NARRATOR: What was the Lorax? And why was it there?
And why was it lifted and taken somewhere
from the far end of town where the Grickle-grass grows?
The old Once-ler still lives here. Ask him. He knows.

ONCE-LER: Now I'll tell you, how the Lorax got lifted and taken away. . .
It all started way back. . . such a long, long time back. . .
Way back in the days when the grass was still green
and the pond was still wet and the clouds were still clean,
and the song of the Swomee-Swans rang out in space. . .

one morning, I came to this glorious place.
And I first saw the trees! The Truffula Trees!
The bright-colored tufts of the Truffula Trees!
Mile after mile in the fresh morning breeze.
And under the trees, I saw Brown Bar-ba-loots
frisking about in their Bar-ba-loot suits
as they played in the shade and ate Truffula Fruits.
From the rippulous pond came the comfortable sound
of the Humming-Fish humming while splashing around.
But those trees! Those trees! Those Truffula Trees!
All my life I'd been searching for trees such as these.
The touch of their tufts was much softer than silk.
And they had the sweet smell of fresh butterfly milk.
I felt a great leaping of joy in my heart.
I knew just what I'd do! I unloaded my cart.
In no time at all, I had built a small shop.
Then I chopped down a Truffula Tree with one chop.
And with great skillful skill and with great speedy speed,
I took the soft tuft. And I knitted a Thneed!
The instant I'd finished, I heard a ga-Zump!
I looked. I saw something pop out of the stump
of the tree I'd chopped down. It was sort of a man.
Describe him?. . . That's hard. I don't know if I can.
He was shortish. And oldish.
And brownish. And mossy.
And he spoke with a voice that was sharpish and bossy.

LORAX: (with a sneeze) Mister! I am the Lorax. I speak for the trees. I speak for the trees, for the trees have no tongues.

And I'm asking you, sir, at the top of my lungs"- What's that THING you've made out of my Truffula tuft?

ONCE-LER: Look Lorax, There's no cause for alarm.
I chopped just one tree. I am doing no harm.
I'm being quite useful. This thing is a Thneed.
A Theend's a Fine-Something-That-All-People-Need!
It's a shirt. It's a sock. It's a glove. It's a hat.
But it has other uses. Yes, far beyond that.
You can use it for carpets. For pillows! For sheets!
Or curtains! Or covers for bicycle seats!"

LORAX: Sir! You are crazy with greed. There is no one on Earth who would buy that fool Thneed.

ONCE-LER: But the very next minute I proved he was wrong.
For, just at that minute, a chap came along,
and he thought that the Thneed I had knitted was great.
He happily bought it for three ninety-eight.
(laughing at the Lorax) You poor stupid guy!
You never can tell what some people will buy.

LORAX: I repeat, I speak for the trees!

ONCE-LER: I'm busy. Shut up, if you please.
I rushed 'cross the room, and in no time at all,
built a radio-phone. I put in a quick call.
I called all my brothers and uncles and aunts and I said
Listen here! Here’s a wonderful chance
for the whole Once-ler Family to get mighty rich!
[They] were all knitting Theends just as busy as bees,
to the sound of the chopping of Truffula Trees.
Then . . . Oh! Baby! Oh! How the business did grow!

Now, chopping one tree at a time was too slow
So I quickly invented my Super-Axe-Hacker
which whacked off four Truffula Trees at one smacker.
We were making Thneeds four times as fast as before!
And that Lorax? . . . He knocked on my new office door.

LORAX: I'm the Lorax who speaks for the trees
which you seem to be chopping as fast as you please.
But I'm also in charge of the Brown Bar-ba-loots
who played in the shade in their Bar-ba-loot suits
and happily lived, eating Truffula Fruits.
NOW. . . thanks to your hacking my trees to the ground,
there's not enough Truffula Fruit to go 'round.
And my poor Bar-ba-loots are all getting the crummies
because they have gas, and no food, in their tummies!
They loved living here. But I can't let them stay.
They'll have to find food. And I hope that they may.

ONCE-LER: I, the Once-ler, felt sad as I watched them all go.
BUT . . . business is business! And business must grow
I meant no harm. I most truly did not.
But I had to grow bigger. So bigger I got.
Then again he came back! I was fixing some pipes
when that old-nuisance Lorax came back with more gripes.

LORAX: (coughing) I am the Lorax (sneezing, snuffling)
Once-ler! You're making such smogulous smoke!
My poor Swomee-Swans. . . why, they can't sing a note!
No one can sing who has smog in his throat.
And so - please pardon my cough –
they cannot live here. So I'm sending them off.

What's more, let me say a few words about Gluppity-Glupp.
Your machinery chugs on, day and night without stop
making Gluppity-Glupp. Also Schloppity-Schlopp.
And what do you do with this leftover goo?. . .
I'll show you. You dirty old Once-ler man, you!
You're glumping the pond where the Humming-Fish hummed!
No more can they hum, for their gills are all gummed.
So I'm sending them off. Oh, their future is dreary.
They'll walk on their fins and get woefully weary
in search of some water that isn't so smeary.

ONCE-LER: And then I got mad. I got terribly mad.
(yelling) Now listen here, Dad!
All you do is yap-yap and day, 'Bad! Bad! Bad! Bad!'
Well, I have my rights, sir, and I'm telling you
I intend to go on doing just what I do!
And at that very moment, we heard a loud whack!
From outside in the fields came a sickening smack
of an axe on a tree. Then we heard the tree fall.
The very last Truffula Tree of them all!
No more trees. No more Thneeds. No more work to be done.
So, in no time, my uncles and aunts, everyone,
all waved me good-bye. They jumped into my cars
and drove away under the smoke-smuggered stars.
Now all that was left 'neath the bad-smelling sky
was my big empty factory. . . the Lorax. . . and I.
The Lorax said nothing. Just gave a glance. . .
just gave a very sad, sad backward glance. . .
as he lifted himself by the seat of his pants.

And I'll never forget the grim look on his face
when he heisted himself and took leave of this place,
through a hole in the smog, without leaving a trace.
And all that the Lorax left here in this mess
was a small pile of rocks, with the one word. . .
UNLESS. (long pause)
Whatever that meant, well, I just couldn't guess.
That was long, long ago.
But each day since that day I've sat here and worried and worried away.
Through the years, while my buildings have fallen apart,
I've worried about it with all of my heart.
But now. . . Now that you're here, the word of the Lorax seems perfectly clear.
UNLESS someone like you cares a whole awful lot, nothing is going to get better
. . . It's not.
SO. . . Catch! (he tosses something down)
It's a Truffula Seed. It's the last one of all!
You're in charge of the last of the Truffula Seeds.
And Truffula Trees are what everyone needs.
Plant a new Truffula. Treat it with care.
Give it clean water. And feed it fresh air.
Grow a forest. Protect it from axes that hack.
Then the Lorax and all of his friends may come back.
```

---

## IC-1175: The Marriage Counselor

- Title: The Marriage Counselor
- Author (byline): Joey Ouellette
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: April 1999
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: TIGER, SUSAN
- Teaser before the introduction: Yes
- Spoken words (computed): 2203
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joey Ouellette
ISBN: 978-0573626708
Publisher: Samuel French, Inc.
Date (Month/Year): April 1999
```

### Introduction (context only: never use it for content warnings)

```text
The Marriage Counselor by Joey Ouellette
```

### Performance text (classify this)

```text
NOTE: Throughout this selection, the judge serves as the silent “marriage counselor”

TIGER: (to audience) She is impossible, totally, totally impossible. I can't stand living with her for another hour, another minute. I'm losing my hair I'm so upset. It's coming out in big hunks. I'm getting constipated. And it's all her fault.

SUSAN: (to audience) I can't take any more of this. He is an insensitive, self-centered jerk. I've tried, believe me, I've tried, my mother says don't give up, don't give up, but of course she's already divorced. I've had enough. I have. It's all his fault.

TIGER and SUSAN: (Together.) See what I mean?

TIGER: She shaves her legs with my razor, my razor, the one I use on my face!

SUSAN: He shaves his face with my razor, my razor, the one I use on my legs!

TIGER and SUSAN: (Together.) It's unsanitary.

TIGER: She leaves her dirty underwear all over the house!

SUSAN: He clips his fingernails in the living room!

TIGER: She eats potato chips in bed. And she won't share.

SUSAN: That's because you're getting fat.

TIGER: Me? I'm getting fat?

SUSAN: I'm glad you agree.

TIGER and SUSAN: (Together.) TIGER: Do you see? Do you see? SUSAN: He is totally unreasonable!

SUSAN: Maybe we should try to speak one at a time.

TIGER: Nana na na na na na.

SUSAN: Don't be such a child.

TIGER: Don't be such a . . . virus.

SUSAN: Virus? I'm a virus?

TIGER: Look, do you want to do this, or what? I could just walk out of here! You wanted to come to a marriage counselor, I agreed, as usual I gave in-

SUSAN: (Interrupts.) Ho ho ho! You gave in! You never give in! Your stubbornness is the cause of every problem we have.

TIGER: My stubbornness? I'm stubborn?

SUSAN: I'm glad you finally admit it. . . . It's not my fault you're not as smart as I am.

TIGER: Oh, I am, I am. It's just that you're cold and I'm sensitive.

SUSAN: You mean stupid.

TIGER: No, I mean sensitive.

SUSAN: No, you mean sensitive.

TIGER: No, I mean stupid. You're the sensitive one. I'm the stupid one. (TIGER realizes what he's said. SUSAN smiles at him.)

SUSAN: Why don't we start at the beginning?

TIGER: We don't have time to start at the beginning. We're paying this bozo, aren't we?

(To the “Judge”.) Sorry.

SUSAN: Two hundred dollars an hour.

TIGER: I take that sorry back.

SUSAN: I'll go first.

TIGER: I'll go first.

SUSAN: We've never-

TIGER: (Continuing.) Been to a marriage counselor

SUSAN: (Continuing.) Before- TIGER (Continuing.) But-

SUSAN: (Continuing.) We thought we should try it.

TIGER: We've tried everything else.

SUSAN: We really have. . . . Self-help books.

TIGER: Acupuncture.

SUSAN: Talking to friends.

TIGER: Hypnosis.

SUSAN: Talking to psychics.

TIGER: Prostitutes. (Silence.) Did I say prostitutes? I meant to say Protestants. Protestants. Talking to Protestants.

SUSAN: Relatives.

TIGER: Talking to Catholics.

SUSAN: Clergymen.

TIGER: Going to the houses of Jehovah's Witnesses.

SUSAN: Lawyers. (Silence.) Did I say lawyers?

TIGER: I, I think you did. Have you been to a lawyer?

SUSAN: Have you been to a prostitute?

TIGER: Don't be silly! What would I go to a prostitute for? I mean I know what I go to a prostitute for, I mean, I haven't been to one, but I've seen pictures. I mean I haven't seen pictures, I just heard about it from a friend of mine, who I haven't seen in seventeen years, and I haven't had any contact with since. It was before I even met you. Have you been to a lawyer?

SUSAN: Yes.

TIGER: (Screaming.) Ahhhh!

SUSAN: Maybe we should start at the beginning.

TIGER: All the way back to the beginning? At four dollars a minute? This is more expensive than phone sex. Not that I've ever done it. I had a friend, I haven't spoken to him in years, he used to do, and no I didn't watch. He just told me about it. Not on the phone. It was seventeen years ago, before I even met you.

SUSAN: So that's what those calls on the phone bill were.

TIGER: What calls?

SUSAN: All those thirty second ones.

TIGER: I have no idea what you're talking about.

SUSAN: (To the “Judge”.) Are we hopeless? What do you think?

TIGER: I think I want to go home.

SUSAN: After we fought all day, after we fought all the way here in the car, and all through our nice lunch, you want to just walk home and waste all that we've accomplished today?

TIGER: Did you say walk home?

SUSAN: We're finally here, at a marriage counselor's. We've been talking about coming since our honeymoon.

TIGER: You did say walk home, didn't you? Don't deny it now!

SUSAN: I took the car keys out of your pocket in the elevator on the way up.

TIGER: I wondered what that tingling was. Why did you take them?

SUSAN: Just in case this doesn't tum out. I'm giving you this last chance. And then I'm keeping the car.

TIGER: Well, as long as you're being open-minded about it.

SUSAN: Can we get on with this?

TIGER: Hey, I'm not the one holding things up.

SUSAN: Oh, it's all my fault.

TIGER: Okay.

SUSAN: Can we start at the beginning?

TIGER: Alright. Do you want to go first? See, see, I'm trying, I'm trying to be polite, I'm trying to make this work. I'm trying. I'll go first. Unless you want to go first. But don't start with the barbecue.

SUSAN: I won't. You see, my sister Jeanine is like my best friend, and she said you don't get out enough, you don't date enough, and so she took me to this barbecue

TIGER: (Interrupting.) She's starting with the barbecue!

SUSAN: I have to start with the barbecue!

TIGER: You said you wouldn't!

SUSAN: I have to!

TIGER: No you don't! You don't have to do anything. That's what you always tell me. I don't have to listen to you. I don't have to do the dishes. I don't have to dress up like a nurse. Oh, I guess that's getting kind of personal.

SUSAN: But the barbecue is the beginning of us. Where do you want me to start then?

TIGER: Never mind. Just never mind. I'll go first. She's having an affair!

SUSAN: Tiger!

TIGER: What? You don't want me to tell strangers? You want me to lie? What's the point in coming here and paying two hundred dollars an hour if we're going to lie?

SUSAN: (Interrupts) I'm not having an affair.

TIGER: Quiet woman! It's my turn, it's my turn and for once in my life I'm going to take my turn and talk when it's my turn to talk! I forgot what I was going to say. Now I remember! I remember. Let me ask you, how many times a week does UPS come to your house? I mean your office? Once maybe? Twice? They come everyday, everyday to my house, when I'm at work and she's, she's home alone in her bathrobe. Five days a week!

SUSAN: I order a lot of books.

TIGER: She's sleeping with every UPS man in the country! They're probably taking turns and fighting over who gets to come to my house. People are dying because the medicines they need are sitting in my driveway, getting cold. The whole UPS company is going to fold. Fold. And then no one will be able to communicate and the whole country will fall apart.

SUSAN: Wait a minute-

TIGER: (Interrupts.) No! No! No! No! No! No! I don't want to listen to your lies. What's the point in parading them through here? I told the truth. That is the whole true story, and that's why I didn't want to come here. There is no point. We have no future. How can we have one?

SUSAN: May I speak? It's true that I have thought about other men, but I think that's normal.

TIGER: I've never thought about other men.

SUSAN: I've been faithful. It's true that I find a man in uniform irrestible, but I have been faithful. I've just been ordering a lot of books . . . I wouldn't be fantasizing about other men if you loved me!

TIGER: I did love you!

SUSAN: He never wanted me. He wanted my sister.

TIGER: Oh, we're back to the barbecue again! Can't we leave the barbecue behind us?

SUSAN: We went to a barbecue-

TIGER: (Interrupts.) She doesn't ever listen, do you see, do you see, never listens to me.

SUSAN: I went to the barbecue with my sister Jeanine.

TIGER: Ah! Ah! Ah! Ahhhhhhh!

SUSAN: Jeanine and I are like best friends, or we were then. Tiger was already at the barbecue. He started talking to us, my sister and I, we were standing side by side. Tiger said will you go out with me? I couldn't believe it. I said yes. But he wasn't talking to me. He was talking to Jeanine. He was asking Jeanine.

TIGER: It's not true, it's not true. Look at me, would you? I'm a normal, ugly, boring, stupid, repulsive man. I was asking both of them. I was asking everybody. I asked trees and mailboxes.

SUSAN: He was asking Jeanine. He didn't want to go out with me.

TIGER: Okay, okay, it's true I was more attracted to her sister, but I was a little drunk, and Jeanine kept laughing at everything I said and she wasn't wearing a Tee-shirt that said, "I hate everything".

SUSAN: You said you liked that tee-shirt! . . . So Tiger took me out on a date.

TIGER: I took her someplace nice.

SUSAN: He took me fishing.

TIGER: It was a nice boat.

SUSAN: I fell in the water.

TIGER: Never touched her!

SUSAN: He nudged me a little bit but I thought he was being romantic, not trying to push me out of the boat.

TIGER: Alright, alright, the truth is I was passing a little bit of gas and I was moving around to try to hide it, you know, everybody does it. I guess maybe I could have nudged her a little bit.

SUSAN: I can't swim.

TIGER: I saved her though, I saved her! I could have let her drown. Who would have known?

SUSAN: He scooped me out with his big fish landing net.

TIGER: She bent the frame too. I had to buy a new net. Those nets aren't cheap.

SUSAN: He tried to give mouth to mouth. But I wasn't having trouble breathing.

TIGER: Can't blame a guy for trying.

SUSAN: He chipped my tooth with his tooth. He chipped my front tooth, this one right here. (SUSAN shows the “judge”)

TIGER: It hurt me too, it hurt me too!

SUSAN: He felt so guilty, he asked me out again.

TIGER: How do you know I felt guilty, you're inventing feelings and putting them into my mouth.

SUSAN: Did you feel guilty?

TIGER: Of course I felt guilty. I pushed her into sewer water, hit her over the head with a landing net and chipped her tooth. The least I could do was to ask her out again.

SUSAN: He took me pheasant hunting.

TIGER: (Uneasy.) I'm an outdoorsy kind of guy.

SUSAN: He shot me in the rear end.

TIGER: I said I was sorry! It was a light load. She only got a couple of shotgun pellets.

SUSAN: Forty-two! The doctor counted as he dug each one out. I should've known then.

TIGER: She bent over-

SUSAN: (Interrupts.) To tie my shoe-

TIGER: (Interrupts.) And something that looked like a pheasant landed on her butt. I mean her rear end.

SUSAN: We never did find the bird.

TIGER: I think it got trampled into the dirt when you were jumping up and down screaming and calling me vile names.

SUSAN: He felt really guilty after that.

TIGER: Of course I felt guilty! I shot her. I'd be a horrible person if I didn't feel guilty for shooting someone!

SUSAN: So he asked me to go away with him to a cabin.

TIGER: Can't we talk about something else?

SUSAN: We were cutting firewood.

TIGER: I don't want to talk about this anymore. Let's talk about the barbecue.

SUSAN: He cut three of my toes off.

TIGER: It was a bad axe, it wasn't my fault, there was something wrong with the axe!

SUSAN: I can't wear open-toed shoes anymore . . . So he proposed to me.

TIGER: I cut her toes off, what was I supposed to do? Sorry about your toes, see you later?

SUSAN: We got married. You probably think I'm stupid, but I didn't see then that he was motivated by guilt. I thought he really liked me for who I was . . . [but] he really wanted me sister Jeanine.

TIGER: It's not true, it's not true!

SUSAN: After we got married she stopped phoning me. She never comes for visits. No Christmas cards. And she just lives a few blocks away.

TIGER: She hates me. Isn't it obvious that her sister hates me? Can't stand the sight of me! Any person in their right mind avoids me.

SUSAN: My sister loves me and she doesn't want to ruin my marriage. So she's stayed away these past six years. Afraid that just the sight of her would tempt him into . . .

TIGER: Into what?

SUSAN: Adultery.

TIGER: That's ridiculous! That's insane! What's adultery?

SUSAN: You never wanted me. Only Jeanine.

TIGER: No, I'm a jerk and Jeanine knows it. That's why she stays away. Just like your mother.

SUSAN: You punched mother.

TIGER: It was an accident. She hit me first!

SUSAN: She was brushing a bug off your face.

TIGER: How was I supposed to know that?

SUSAN: You don't want me. You want Jeanine.

TIGER: That's crazy. Do you call her? Do you send her a Christmas card? Why should she send you one? It doesn't mean anything.

SUSAN: She's never visited me.

TIGER: That's because she can't get in our driveway because it's filled with UPS trucks.

SUSAN: You've never loved me! You just married me out of guilt!

TIGER: No, I married you because I'm stupid! Stupid stupid stupid stupid!

SUSAN: (to judge.) Make him stop, make him stop!

TIGER: (to judge) Make her stop! She's the one who had to bring up that stupid barbecue.

SUSAN: I wish I'd never gone to it!

TIGER: Not as much as I do!
```

---

## IC-1176: A Midsummer Night’s Dream: Pyramus and Thisbe

- Title: A Midsummer Night’s Dream: Pyramus and Thisbe
- Author (byline): William Shakespeare
- Work: Not specified
- Publisher: Washington Square Press
- Publication date as stated: Jan 2004
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: QUINCE, BOTTOM, FLUTE, STARVELING, SNOUT, SNUG, NARRATOR, WALL, PYRAMUS, THISBE, LION, MOONSHINE
- Teaser before the introduction: No
- Spoken words (computed): 1876
- Already set (do not supply): none

### Source block (context only)

```text
Author: William Shakespeare
ISBN: 978-0743477543
Publisher: Washington Square Press
Date (Month/Year): Jan 2004
```

### Introduction (context only: never use it for content warnings)

```text
As a part of Shakespeare's A MIDSUMMER NIGHT's DREAM, six workers sometimes called "mechanicals" or "clowns" decide to present a play for the festivities that will follow the wedding of the Duke of Athens. Of course, these men know nothing about acting or play production, and, as a result, the audience is treated to a rousing, laughable performance by inept, though enthusiastic, actors doing the best they can to please the Duke. The practice begins . . .
```

### Performance text (classify this)

```text
QUINCE: Is all our company here?

BOTTOM: You were best to call them generally, man by man, according to the scrip.

QUINCE: Here is the scroll of every man's name, which is thought fit, through all Athens, to play in our interlude before the duke and the duchess, on his wedding-day at night.

BOTTOM: First, good Peter Quince, say what the play treats on, then read the names of the actors, and so grow to a point.

QUINCE: Marry, our play is, The most lamentable comedy, and most cruel death of Pyramus and Thisby.

BOTTOM: A very good piece of work, I assure you, and a merry. Now, good Peter Quince, call forth your actors by the scroll. Masters, spread yourselves.

QUINCE: Answer as I call you. Nick Bottom, the weaver.

BOTTOM: Ready. Name what part I am for, and proceed.

QUINCE: You, Nick Bottom, are set down for Pyramus.

BOTTOM: What is Pyramus? a lover, or a tyrant?

QUINCE: A lover, that kills himself most gallant for love.

BOTTOM: That will ask some tears in the true performing of it: if I do it, let the audience look to their eyes; I will move storms, I will condole in some measure. To the rest: yet my chief humour is for a tyrant: I could play Ercles rarely, or a part to tear a cat in, to make all split.

The raging rocks
And shivering shocks
Shall break the locks
Of prison gates;
And Phibbus' car
Shall shine from far
And make and mar
The foolish Fates.

This was lofty! Now name the rest of the players. This is Ercles' vein, a tyrant's vein; a lover is more condoling.

QUINCE: Francis Flute, the bellows-mender.

FLUTE: Here, Peter Quince.

QUINCE: Flute, you must take Thisby on you.

FLUTE: What is Thisby? a wandering knight?

QUINCE: It is the lady that Pyramus must love.

FLUTE: Nay, faith, let me not play a woman; I have a beard coming.

QUINCE: That's all one: you shall play it in a mask, and you may speak as small as you will.

BOTTOM: And I may hide my face, let me play Thisby too, I'll speak in a monstrous little voice. 'Thisne,Thisne;' 'Ah, Pyramus, lover dear! thy Thisby dear,and lady dear!'

QUINCE: No, no; you must play Pyramus: and, Flute, you Thisby.

BOTTOM: Well, proceed.

QUINCE: Robin Starveling, the tailor.

STARVELING: Here, Peter Quince.

QUINCE: Robin Starveling, you must play Thisby's mother. Tom Snout, the tinker.

SNOUT: Here, Peter Quince.

QUINCE: You, Pyramus' father: myself, Thisby's father: Snug, the joiner; you, the lion's part: and, I hope, here is a play fitted.

SNUG: Have you the lion's part written? pray you, if it be, give it me, for I am slow of study.

QUINCE: You may do it extempore, for it is nothing but roaring.

BOTTOM: Let me play the lion too: I will roar, that I will do any man's heart good to hear me; I will roar, that I will make the duke say 'Let him roar again, let him roar again.'

QUINCE: And you should do it too terribly, you would fright the duchess and the ladies, that they would shriek; and that were enough to hang us all.

BOTTOM: I grant you, friends, if that you should fright the ladies out of their wits, they would have no more discretion but to hang us: but I will aggravate my voice so that I will roar you as gently as any sucking dove; I will roar you an 'twere any nightingale.

QUINCE: You can play no part but Pyramus; for Pyramus is a sweet-faced man; a proper man, as one shall see in a summer's day; a most lovely gentleman-like man: therefore you must needs play Pyramus.

BOTTOM: Well, I will undertake it. What beard were I best to play it in?

QUINCE: Why, what you will.

BOTTOM: I will discharge it in either your straw-colour beard, your orange-tawny beard, your purple-in-grain beard, or your French-crown-colour beard, your perfect yellow.

QUINCE: Some of your French crowns have no hair at all, and then you will play bare-faced. But, masters, here are your parts: and I am to entreat you, request you and desire you, to con them by to-morrow night; and meet me in the palace wood, a mile without the town, by moonlight; there will we rehearse, for if we meet in the city, we shall be dogged with company, and our devices known. In the meantime I will draw a bill of properties, such as our play wants. I pray you, fail me not.

BOTTOM: We will meet; and there we may rehearse most obscenely and courageously. Take pains; be perfect: adieu.

TRANSITION

After much practice Peter Quince’s group is ready for their stage debut at the Wedding Celebration of the Duke and Dutchess. The play will tell the story of the doomed lovers Pyramus and Thisby (Think Romeo and Juliet with a twist) -- of how they met at Ninus' tomb, declared their love, and died bloody deaths. But the workers performance of this sad tale is more tragic than the lovers' untimely deaths. Everything goes wrong and the production ends as a hilarious fiasco -- to everyone but the performers. Pyramus and Thisbe compliments of Shakespeare’s Mechanicals – Let the show begin!

NARRATOR:

Gentles, perchance you wonder at this show;
But wonder on, till truth make all things plain.
This man is Pyramus, if you would know;
This beauteous lady Thisby is certain.
This man, with lime and rough-cast, doth present
Wall, that vile Wall which did these lovers sunder;
And through Wall's chink, poor souls, they are content
To whisper. At the which let no man wonder.
This man, with lanthorn, dog, and bush of thorn,
Presenteth Moonshine; for, if you will know,
By moonshine did these lovers think no scorn
To meet at Ninus' tomb, there, there to woo.
This grisly beast, which Lion hight by name,
The trusty Thisby, coming first by night,
Did scare away, or rather did affright;
And, as she fled, her mantle she did fall,
Which Lion vile with bloody mouth did stain.
Anon comes Pyramus, sweet youth and tall,
And finds his trusty Thisby's mantle slain:
Whereat, with blade, with bloody blameful blade,
He bravely broach'd is boiling bloody breast;
And Thisby, tarrying in mulberry shade,
His dagger drew, and died. For all the rest,
Let Lion, Moonshine, Wall, and lovers twain
At large discourse, while here they do remain.

(Exeunt Prologue, Thisbe, Lion, and Moonshine)

WALL:
In this same interlude it doth befall
That I, one Snout by name, present a wall;
And such a wall, as I would have you think,
That had in it a crannied hole or chink,
Through which the lovers, Pyramus and Thisby,
Did whisper often very secretly.
This loam, this rough-cast and this stone doth show
That I am that same wall; the truth is so:
And this the cranny is, right and sinister,
Through which the fearful lovers are to whisper.

(Enter Pyramus)

PYRAMUS:
O grim-look'd night! O night with hue so black!
O night, which ever art when day is not!
O night, O night! alack, alack, alack,
I fear my Thisby's promise is forgot!
And thou, O wall, O sweet, O lovely wall,
That stand'st between her father's ground and mine!
Thou wall, O wall, O sweet and lovely wall,
Show me thy chink, to blink through with mine eyne!

Wall holds up his fingers

Thanks, courteous wall: Jove shield thee well for this!
But what see I? No Thisby do I see.
O wicked wall, through whom I see no bliss!
Cursed be thy stones for thus deceiving me!

(Aside) 'Deceiving me'
is Thisby's cue: she is to enter now, and I am to
spy her through the wall. You shall see, it will
fall pat as I told you. Yonder she comes.

(Enter Thisbe)

THISBE:
O wall, full often hast thou heard my moans,
For parting my fair Pyramus and me!
My cherry lips have often kiss'd thy stones,
Thy stones with lime and hair knit up in thee.

PYRAMUS: I see a voice: now will I to the chink, To spy an I can hear my Thisby's face. Thisby!

THISBE: My love thou art, my love I think.

PYRAMUS: Think what thou wilt, I am thy lover's grace; And, like Limander, am I trusty still.

THISBE: And I like Helen, till the Fates me kill.

PYRAMUS: Not Shafalus to Procrus was so true.

THISBE: As Shafalus to Procrus, I to you.

PYRAMUS: O kiss me through the hole of this vile wall!

THISBE: I kiss the wall's hole, not your lips at all.

PYRAMUS: Wilt thou at Ninny's tomb meet me straightway?

THISBE: 'Tide life, 'tide death, I come without delay.

(Exeunt Pyramus and Thisbe)

WALL: Thus have I, Wall, my part discharged so; And, being done, thus Wall away doth go.

(Exit)

LION:
You, ladies, you, whose gentle hearts do fear
The smallest monstrous mouse that creeps on floor,
May now perchance both quake and tremble here,
When lion rough in wildest rage doth roar.
Then know that I, one Snug the joiner, am
A lion-fell, nor else no lion's dam;
For, if I should as lion come in strife
Into this place, 'twere pity on my life.

MOONSHINE:
This lanthorn doth the horned moon present;--
This lanthorn doth the horned moon present;
Myself the man i' the moon do seem to be.
All that I have to say, is, to tell you that the
lanthorn is the moon; I, the man in the moon; this
thorn-bush, my thorn-bush; and this dog, my dog.

(Enter Thisbe)

THISBE: This is old Ninny's tomb. Where is my love?

LION: [Roaring] Oh--

(Thisbe runs off. The Lion shakes Thisbe's mantle, and exit)

(Enter Pyramus)

PYRAMUS:
Sweet Moon, I thank thee for thy sunny beams;
I thank thee, Moon, for shining now so bright;
For, by thy gracious, golden, glittering gleams,
I trust to take of truest Thisby sight.
But stay, O spite!
But mark, poor knight,
What dreadful dole is here!
Eyes, do you see?
How can it be?
O dainty duck! O dear!
Thy mantle good,
What, stain'd with blood!
Approach, ye Furies fell!
O Fates, come, come,
Cut thread and thrum;
Quail, crush, conclude, and quell!
O wherefore, Nature, didst thou lions frame?
Since lion vile hath here deflower'd my dear:
Which is--no, no--which was the fairest dame
That lived, that loved, that liked, that look'd
with cheer.
Come, tears, confound;
Out, sword, and wound
The pap of Pyramus;
Ay, that left pap,
Where heart doth hop:

(Stabs himself)

Thus die I, thus, thus, thus.
Now am I dead,
Now am I fled;
My soul is in the sky:
Tongue, lose thy light;
Moon take thy flight:
Now die, die, die, die, die.

(Dies)

(Re-enter Thisbe)

THISBE:
Asleep, my love?
What, dead, my dove?
O Pyramus, arise!
Speak, speak. Quite dumb?
Dead, dead? A tomb
Must cover thy sweet eyes.
These My lips,
This cherry nose,
These yellow cowslip cheeks,
Are gone, are gone:
Lovers, make moan:
His eyes were green as leeks.
O Sisters Three,
Come, come to me,
With hands as pale as milk;
Lay them in gore,
Since you have shore
With shears his thread of silk.
Tongue, not a word:
Come, trusty sword;
Come, blade, my breast imbrue:

Stabs herself

And, farewell, friends; Thus Thisby ends: Adieu, adieu, adieu.

(Dies)

NARRATOR: No epilogue, this play needs no excuse. Never excuse; for when the players are all dead, there needs none to be blamed. Marry, if he that writ it had played Pyramus and hanged himself in Thisbe's garter, it would have been a fine tragedy: and so it is, truly; and very notably discharged.
```

---

## IC-1177: Mrs. Bob Cratchit's Wild Christmas Binge

- Title: Mrs. Bob Cratchit's Wild Christmas Binge
- Author (byline): Christopher Durang
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Jan 2005
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: BOY 1, YOUNG EBENEZER, GHOST, BOB CRATCHIT, SCROOGE, GENTLEMAN 2, GENTLEMAN 1, CHILD 1, CHILD 2, MRS. BOB CRATCHIT, TINY TIM, CHILD’S VOICE
- Teaser before the introduction: Yes
- Spoken words (computed): 1394
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christopher Durang
ISBN: 978-0822220275
Publisher: Dramatists Play Service
Date (Month/Year): Jan 2005
```

### Introduction (context only: never use it for content warnings)

```text
Mrs. Bob Cratchit’s Wild Christmas Binge by Christopher Durang.
```

### Performance text (classify this)

```text
BOY 1: (Pg 7) (singing sweetly) HARK THE HERALD ANGELS SING, GLORY TO THE NEWBORN KING.

YOUNG EBENEZER: (irritated, negative) Bah humbug!

BOY 1: PEACE ON EARTH, AND MERCY MILD; GOD AND SINNER RECONCILED

YOUNG EBENEZER: Phooey! Christmas stinks! Get me a hamburger!

GHOST: (to audience) Even as a child, young Ebenezer displayed a pronounced antipathy toward Christmas. (to Ebenezer) Merry Christmas, Ebenezer

YOUNG EBENEZER: Bah humbug! I want to put bugs in your hair!

GHOST: (to audience) In later centuries, we would probably identify Ebenezer’s repeated saying of “Bah humbug” as a kind of seasonal Tourette’s Syndrome. However in 1943, when our story is set, we hadn’t a clue what it meant – except he was a nasty little child.

YOUNG EBENEZER: Bah humbug! I hate Christmas!

BOB CRATCHIT: (Pg 13-15) Good morning, Mr. Scrooge.

SCROOGE: You still alive, Bob Cratchit? You haven’t died of pneumonia yet?

BOB CRATCHIT: Well, I’m very cold, it’s true, Mr. Scrooge. Might we put another coal on the fire?

SCROOGE: No, we may not. I am not made of money. A little cold never hurt anyone. Slap yourself in the face, Bob Cratchit.

BOB CRATCHIT: Very well, sir. (slaps himself in the face) Mr. Scrooge, there are two gentlemen to see you, sir. (gentlemen enter)

GENTLEMAN 2: Merry Christmas to you, sir.

SCROOGE: Bah humbug. Christmas-stinks-Christmas-carols-make-me-puke.

GENTLEMAN 1: Mr. Scrooge, we are fellow businessmen collecting for the United Way. Every Christmas we give a little bit from our pockets to all the poor people who wander throughout London in poverty and despair. And we wondered how much we could put you down for?

SCROOGE: Nothing. I wish to give nothing. Let the poor go to workhouses, or orphanages, or die in the street. (he exits)

GHOST: Clearly Mr. Scrooge needs to be changed. I think a little visit may be in order, don’t you? And some scary noises and rattling chains. Coming right up! *****Scene*****

SCROOGE: (Pg 17-19) I am suddenly exhausted (he nods off to sleep) (Offstage, the sound of ghostly “woo-ing”)

GHOST: (enters) UPS delivery. UPS delivery. Mr. Scrooge, I have a package. A Christmas present from all your grateful friends and relatives. (Hold out a box)

SCROOGE: (takes the box and opens it) Ah. A pair of socks. (tosses it aside) Christmas! Leave me out of it!

GHOST: (eye rolling and a heavy sigh) I am the Ghost of Christmas Past. (Scrooge is not impressed) The way you receive present is just no good. Try again (offers him another package) No before opening, you must proclaim in loud and grateful tones how lovely the wrapping is.

SCROOGE: I don’t want to. (Ghost takes out an electrical zapper and zaps him - ZAP ZAP) Aaaaggghh! What is that?

GHOST: A zapper. (threateningly) If you disobey, I shall use it again and again and again. (recovers a benevolent attitude) Now as I said. Make a big fuss over the Christmas wrapping.

SCROOGE: (with feigned, unconvincing delight) Oh . . . what a lovely shade of yellow. Makes me think of (beat) vomit! (Ghost zaps him) Aaaaggghhh! I. . . I . . . hate to even open it, it’s so lovely.

GHOST: Much better. I am the Ghost of Christmas Past, and we have visiting to do. Come touch my arm. (Scrooge touches the Ghost’s arm and there are rustling sounds, like racing through space and time) *****Scene*****

GHOST: (Pg 20-24) We’re at the Cratchit house? We’re supposed to be her much later. Something’s gone awry.

CHILD 1: I’m hungry.

CHILD 2: Me too. Feed us!

MRS. BOB CRATCHIT: All children want to do is eat, it’s disgusting. (Screams at them) When your father finally makes some money, then you’ll eat!

CHILD 2: Father and Tiny Tim are home, I think.

MRS. BOB CRATCHIT: I wonder what good news your father will have for Christmas Eve. Maybe Scrooge died and named us in his will. (laughs bitterly)

SCROOGE: That’s rude.

BOB CRATCHIT: Gladys, we’re home. And Tiny Tim enjoyed looking in the store windows at all the Christmas treats he can’t have.

TINY TIM: I only fell twenty-four times today!

MRS. BOB CRATCHIT: Use your crutch, you stupid child.

TINY TIM: I don’t want people to notice I’m crippled.

MRS. BOB CRATCHIT: And if you fall down twenty-four times, you don’t think they’ll notice? (angrily to Bob) That crutch cost half your weekly salary and the idiot child won’t use it!

GHOST: Isn’t this a sad family? Do you feel sorry for them?

SCROOGE: (scoffs) Why are you showing me this?

MRS. BOB CRATCHIT: (to Bob) Did you ask that horrible Mr. Scrooge for a raise as I told you to?

BOB CRATCHIT: Well . . . an amusing story about that . . .

MRS. BOB CRATCHIT: What?! You’re missing part of your brain, aren’t you. I may go mad right now. I’ll go nuts, I’ll go crackers.

CHILD 1: I want a cracker!

MRS. BOB CRATCHIT: (screams) Goodbye, children. Mother’s going to jump off London bridge. Have a nice Christmas. Goodbye, everyone! (she rushes out)

SCROOGE: (heartless) Oh, pooey. If she ends up in Bedlam, that’s her problem!

BOB CRATCHIT: (calling after her) Gladys, please! It’s Christmas Eve! It’s a happy time. (he turns sadly) Oh, it break my heart. I think we all better cry. On the count of three, everybody weep. (loud sobbing)

SCROOGE: Oh, Lord, they’re crying! Pathetic! ****Scene*****

MRS. BOB CRATCHIT: (Pg 29) (catching her breath after rushing from her house) Okay. Okay. (panting) I'm ready to die now. Which way to London Bridge?

GHOST: (rushing after Mrs. Cratchi, and dragging Scrooge along) Mrs. Cratchit, can you hear me? Listen. You need Paxil or Zoloft. Are you on an antidepressant?

MRS. BOB CRATCHIT: I don’t know what you’re talking about. Which way to the river?

GHOST: (pleading) Just go home to Mr. Cratchit. I’m trying to redeem this man here . . .

SCROOGE: (interrupting) Oh, let her kill herself – (Pg 34) Christmas is stupid and makes us do stupid, awful things.

GHOST: (Pg 29) . . . and you’ve a part of his story. If you kill yourself, the story has an entirely different meaning.

MRS. BOB CRATCHIT: I’ll find the river myself. Merry Christmas, see you in hell! (Exits)

GHOST: (Pg 34) Oh, God. This isn’t going like it’s supposed to! (Pg 37) I can’t have Mr.s Cratchit be dead. I’m going to need all my powers. (Ghost spreads arms with authority) Hear me, spirits – I call upon the forces of the wind and sea to bring Mrs. Bob Cratchit back (nothing happens)

SCROOGE: (Pg 24) I think I should go back to bed, and you should go back to Ghost School or something.

GHOST: . . . RIGHT NOW! (Mrs. Bob Cratchit appears)

MRS. BOB CRATCHIT: (Pg 37) No! No! No!! I don’t want to be here!

GHOST: (Pg 38) It worked! And from now on, (waves hands toward Mrs. Cratchitt) Mrs. Cratchit will behave correctly.

MRS. BOB CRATCHIT: (Sweetly) Hello, children. Hello, Bob. Hello, Tiny Tim. Mother’s home now. Merry Christmas.

TINY TIM: (Pg 37) Merry Christmas, Mother. (Pg 41) Mummy, itsn’t it time for Christmas dinner? The goose and the huckleberries and the yams and then the Christmas pudding?

MRS. BOB CRATCHIT: (the spell dissipates quickly) I’ve been trying to drown myself in the Thames – you think I have time to be cooking for you??? God, when will feminism be invented so people won’t just assume I’ll be cooking all the time AND be positive and pleasant!

TINY TIM: (Pg 47-48) So there’s no Christmas dinner and no Christmas pudding. I can’t be brave anymore (begins to cry)

SCROOGE: So pathetic. It gets on my nerves. Let me treat them to a Christmas dinner. I have money.

GHOST: (waves arms and bags of food appear on the table)

TINY TIM: Ooooohhh. Aahhhhh. It’s magic! (quickly opening a bag) I have a Big Whopper!

MRS. BOB CRATCHIT: Isn’t that nice . . . (she notices the pitiful Christmas tree) Good God! Who decorated the tree?

TINY TIM: (with his mouth full) I did!

MRS. BOB CRATCHIT: Are you blind as well as crippled?

SCROOGE: (Pg 38-39) I like Mrs. Cratchit! She speaks up for herself. It’s so unusual.

GHOST: She has a bad attitude.

MRS. BOB CRATCHIT: (Pg 53) I have a realistic attitude. I’m living in 1840s London, there’s no plumbing, everybody smells all the time. There’s never enough food, my husband earns no money. And I feel so lonely, and hopeless, and the people around me are icky and goody-goody and pitiful, and I wish I had never been born!

SCROOGE: Indeed. That’s why she’s so delightful. (he winks at Mrs. Cratchit)

GHOST: (pg 54) I’m so thrown. Nowhere in the story does Scrooge fall in love with Mrs. Bob Cratchit

SCROOGE: I’m not in love . . . (smiling and flirt-waving to Mrs. Cratchit) . . . yet I’m just flirting!

TINY TIM: (Pg 50) Oh dear. I don’t feel very well. I have a feeling I may die.

SCROOGE: (Pg 49-50) Oh, God, am I going to have to watch these pathetic children’s death scenes?

MRS. BOB CRATCHIT: Nonsense. What would you die of?

TINY TIM: Of being a cripple.

MRS. BOB CRATCHIT: (scoffs) That’s like saying you’re going to die because you have brown hair.

TINY TIM: Nonetheless I feel it. Unless Mr. Scrooge reforms his personality and learns to value Christmas, I can tell I’m going to die. (Bob Cratchit begins crying)

MRS. BOB CRATCHIT: He’s not dying! He probably feels ill from the Happy Meal, all that fat and grease. If you need to throw up, use one of the bags the food came in. That’s why they put the foot in bags, it’s for vomiting in later on. (beat) I’ve had enough sickness and pathos, and this stupid family where everything is about suffering.

TINY TIM: I think I feel consumption coming on. That’s when your little lungs fill up with something and you cough and die, right? (coughs)

MRS. BOB CRATCHIT: Enough! Wallowing in consumption, poverty, no food, no money. This isn’t what I signed up for! It’s a horrible life.

BOB CRATCHIT: It’s a wonderful life. (a bell tinkles)

CHILD’S VOICE: (sweetly) Teacher says whenever a bell rings, it’s an angel getting its wings. *****Scene*****

GHOST: (Pg 62-63) (spreads shiny wings) Well, as you see. I got my wings, whatever that means. (frowning) And so, um . . . well the moral of the story confuses me soft of. But there must be one. Let’s see. The moral is there are some people who are mean and nasty, but if they enjoy being mean and nasty (like) Scrooge and Mrs. Cratchit, then they’re happy.

(shrugs) I’m sorry if that doesn’t sound uplifting, but the story doesn’t make sense to me anymore.

TINY TIM: (sings or hums – From How the Grinch Stole Christmas*)
Fah who foraze! Dah who doraze!
Welcome Christmas, come this way!
Fah who foraze! Dah who doraze!
Welcome Christmas, Christmas Day!
(Pg 37) . . . God Bless us Everyone!

SCROOGE: (Pg 19) Makes me think of (beat) vomit!
```

---

## IC-1178: AN INTROVERT’S GUIDE TO QUARANTINE

- Title: AN INTROVERT’S GUIDE TO QUARANTINE
- Author (byline): MIKE NOLAND
- Work: AN INTROVERT’S GUIDE TO QUARANTINE
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1610
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
I know you are going to think I’m crazy and maybe I am, don’t answer that but I have actually... kind of liked being in quarantine. Now let’s face it, this virus is awful and I don’t want anyone to get it and certainly not die from it. The world right now is more scary and dangerous than it’s been in a long time. Like maybe since the dinosaurs or the Middle Ages or the height of the Black Friday sales events at the mall and the only safe place to be is home. I like being home so that’s why I like being quarantined.

I have to admit, I’ve always liked being at home because I’m an introvert. There, I said it, whew. It’s like a weight has been lifted from me. Being an introvert in high school is not an easy thing. Everyone expects you to be out doing stuff. “Hey Denny/ Jenny, we are all going to Paula’s house to watch the football game, wanna come?” or “Denny/Jenny, we’re gonna play Farmville and then take selfies with Pattie’s hedgehog.” I don’t want to do anything of that, but hedgehogs are kinda cool. I love being in my room listening to music or reading a book or just playing mindless games on my phone. Why is that such a weird thing? Don’t get me wrong, I like people, well..most people...well, actually only a few people and I have friends. At school, most people are like “You are so funny, we should hang out more.” I think to myself, “Mmmm, no.” I just get tired of always having to be “on”, ya know? When you are at school people expect you to act a certain way. That gets old by the end of the day, heck that gets old by the end of first period. So going home is a much needed respite from the world.

Now with the quarantine, nobody is doing anything, Yes! That takes a ton of pressure off of me. I don’t have to make excuses for not going anywhere and I don’t...like...feel bad. Why is everybody freaking out about it? I do think it’s weird that people started buying up all the toilet paper and guns. Toilet paper kind of sort of makes sense, but guns? You can’t shoot the virus. I guess people were getting guns to protect all the toilet paper they bought. For me, this was a chance to chill and take a deep, cleansing breath. People just need to see the good side of all of this.

For example, you can wear the same clothes all day everyday. That is amazing. It’s so freeing, I love it. Not that clothes and image are that big of a deal to me anyway but it’s nice to just bum around the house in sweats and a t-shirt from morning till night. My mom got mad “DENNY/JENNY, you haven’t changed clothes since Monday?” I said, “Uh, yeah, and it’s only Thursday, what’s your point? Unless Beyonce is dropping by to take me out for a caramel cinnamon dolce latte, I think my clothes are just fine.” She doesn’t get it because she has taken a shower and put on makeup everyday. Seriously, what is wrong with her? She’s not fooling anyone with that makeup anyway because 40 is not the new 20! Fortunately my dad has been much cooler about it. I think he loves not wearing a suit and tie everyday. Unless he has a video call then it’s business up top and pj’s downtown.

Numero dos, that’s number two in Spanish. I might as well keep in practice since it’s still one of my courses. Anyway, I don’t have to go to school. Bing, Bing, Bing, that’s a winner, winner, chicken dinner every time. That doesn’t mean I don’t have school, it just means I don’t have to go. I get to do all my school work from home. It has its ups and downs, but overall, I’m loving it. I’m still doing plenty of work without the social pressure, bullying, snide remarks and those are usually coming from me. Being in a school building is like a lab experiment and we are all the rats. We are forced into close quarters with people that in the outside world we would never even speak to, at least I wouldn’t. Then they run us through a maze and make us do tasks for our treats. Good grades being the ultimate reward. I know there are some people who love school like Avery. “Mr. Allen, would it be possible to get extra credit if I organized your books in your bookshelf by color? That would really be so gorg to look at.” She’s a literal freak show. If you are an introvert like me, school is pretty much the 7th level of Hell. What’s really strange is I love the academic side of it. Getting to learn new things is exciting and being able to do it using my laptop from home is...bliss. I know that many kids won’t agree with me, but here are a few of my reasons why I love quarantining, they can make their own list. Ya know, list better have my reasons. (Laughs softly, then stops.)

Another fab thing is Streaming. There’s no point lying about it. Streaming shows, movies and even videos has been incredible. Let me say that I have always been a fan of going to the movies, sitting in the dark with a box of popcorn and a coke and losing myself in that magical experience. Except for the dimwit that shouts, “Dude, he’s behind the door.” With the ability to watch at home on a screen that’s as big as my dad’s first car, his words not mine, who needs the aggravation? I can binge on Netflix, Hulu, HBO and Disney. I’m just naming a few because the list gets longer every day. Imagine if we had to quarantine 50 years ago when they only had, like 4 channels to watch and one of them was PBS, eewww. That would have been tough. No worries, we are living in the age of Stream- topia. It’s perfect for our times and I couldn’t be happier about it. With all this stuff to watch, why does anyone want to leave their house? If I can’t sleep, I’ll watch some Youtube, need a study break, I’ll catch some AppleTV. It’s the perfect solution anytime. I’ve even watched some of those cooking shows which leads me to my next point.

My mom has been baking breads like crazy. “Mom”, I said “are we expecting company?” She looks confused and says “No, why?” “Well, unless you got a side hustle with Pepperidge Farm, it seems like you’ve baked an excessive amount of bread.” She got a little defensive and said, “No it’s not, you’re just being judgmental.” I said, “Am I? I went to the hall closet to get a towel and 2 loaves of bread fell on my head.” “Get out of my kitchen” she said as she took a swing at me with a whisk. However, others benefit from her overzealous culinary coping mechanism. She gave the FedEx guy banana bread, the mail carrier got zucchini bread and our neighbor, with the yappy little dog that poops in everybody’s yard, got brownies. (Laughs) Now that was a good one. Every night, mom is trying some kind of new dish that she came across. Some of it’s kinda weird but all of it is good. I think I have gained my “Quarantine 15” as they say. Since I’m living in sweatpants it’s not a problem. I don’t really care if I end up a Fatty-boom-ba-latty, it’s not like it’s forever, right Jenny Craig?

Let me ask, are you getting enough sleep? Because as teenagers we never seem to get enough and if we do we get yelled at. I have never understood that because there’s mountains of evidence out there proving that teenagers require lots of sleep,.. duh! But I get treated like I sucker punched a baby seal, if I sleep more than 8 hours. “You gonna sleep the whole weekend or I was just checking on you for signs of life,” my parents say. Yet when my dad goes to sleep in the living room watching tv, he always says, “I wasn’t sleeping, I was just resting my eyes.” Thanks to quarantine, sleep is not a dirty word. I’ve settled into a nice little pattern. I stay up late, but now I can sleep late. Not only that but I have discovered the joys of napping. How have I been missing this my whole life? I used to make fun of my Grandpa Morris when he came to visit. That man could start snoring before he got the footrest up on the La-Z- Boy. I just thought it was an old person thing but was I ever wrong. It’s a sweet little nugget that never disappoints.

I can just hear some of you now, “but Denny/Jenny I’m not enjoying quarantine at all. If I have to stay in this house with my family for one more minute, I’ll die, I’ll just die.” While I appreciate good hyperbole, you just need to step back from the ledge. It’s not that bad. Believe me, if you have friends, they will look really good to you after a few months cooped up with the fam. Quarantining is not that easy, but it doesn’t have to be that hard either. So phone on, shoes off and quarantine like me, the introvert!
```

---

## IC-1179: Nora Wants a Baby

- Title: Nora Wants a Baby
- Author (byline): Forrest Musselman
- Work: Nora Wants a Baby
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: SETTING, AT RISE
- Teaser before the introduction: No
- Spoken words (computed): 1487
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
NOTES

This play was born out of an even shorter skit which was part of a compilation in the play Baby Mama Drama, which was originally performed in the fall of 2006 at Studio Academy Charter Arts High School in Rochester, Minnesota.

The original cast members were: Matt Meriwethers, Mike Baker, Jessica Meyers, Mercedes Madline, Matthew Chase, Andy Hoye, Ericka Street and Candy Marra.

While this is intended as a comedy duet with one person playing Nora and the other person playing the other characters, this can certainly be done as one person or as a short play with multiple characters.

A big thanks to Ehryn Barthelme and Planned Parenthood of Rochester who worked with my students and helped book shows at local schools in Rochester. Also, to Eric Holsen who had to bravely take over directing the show while I made an unscheduled trip to South Korea to do some parenting of my own.

A big thanks to my family as always.

CAST OF CHARACTERS

Nora SHE is not the famous explorer named Dora.

Galoshes HE is Dora’s pet monkey and that’s the way he wants it to stay.

Baby HE / SHE starts the whole obsession.

Map HE / SHE knows where to go... always.

Teacher HE / SHE is a teacher. Enough said.

Wiper HE has been stalking Nora.

Denny HE is a bull.

Blue Arrow OPTIONAL

NOTE: In the event that this is played by two people, it will work best when one person plays Nora and the other person plays the rest of the characters.

SETTING: The stage is bare, with an exception to several blocks that may be used in various places as determined by the director.

AT RISE: Spanish music begins to play. Nora enters with her friend, Galoshes.

NORA Hola, I’m Nora. And this is my friend, Galoshes.

GALOSHES Hola.

NORA Please don’t confuse us with the other show on TV that stars a Spanish girl and her pet monkey.

GALOSHES We’re not them.

NORA At all.

GALOSHES No resemblance.

NORA (very serious) I’m Nora.

GALOSHES (extremely serious) And I’m Galoshes.

NORA Today we’re going to going to talk about the word embarazada. Can you say embarazada? (They look at audience.) Good. Do you know what embarazada means? (They pause perhaps a little too long.) That’s right. It means pregnant. Can you say pregnant?

GALOSHES Are you pregnant, Nora?

NORA No, but remember when we saw that baby earlier and it was so cute?

GALOSHES (Not sure where this is going, and not liking it, but agreeing anyway.) Maybe?

NORA I sure wish I could have the baby. I wish I was embarazada. I would love it and kiss it and call it George.

GALOSHES That’s a nice name.

NORA I know I saw the baby around here earlier. (To audience) Do you see it?

(There is a long pause as GALOSHES and NORA look at the audience. Behind them a baby crawls across the floor. Another actor enters dressed in all blue, carrying a large blue arrow and “clicks” on the baby. To avoid confusion as a comedy duet, you can cut the arrow bit.)

BLUE ARROW Click!

BABY Hola!

NORA There it is. There’s the baby.

(Baby crawls off stage. Blue Arrow follows.)

GALOSHES Yep, there’s the baby.

NORA Oh, but look, it crawled away. Where did it go?

(Galoshes shrugs his shoulders.)

NORA I think we need the map. Where’s the map?

MAP (Enters) I’m the map, I’m the map, I’m the map, I’m the map. I’m the map, I’m the map, I’m the map, I’m the map. Map!

NORA Okay, Map, we’re trying to get a baby. Can you tell us how to get to it?

MAP Uh, what do you want a baby for?

NORA I want to love it and kiss it and call it George.

MAP Yeah, you’re only four years old. You’ve got a long ways to go.

NORA Then show me the way.

MAP Right. So first you need to go through education, cross the bridge of marriage, take the career path and climb the hill of financial stability. You got that?

NORA I’m not sure. What is it?

MAP Education, marriage, career and money.

NORA I’m not sure I like that way. What if I want a career first and then get married later?

MAP You asked me to show you the way. I did. I’m a map.

NORA Right. Education, marriage, career and money. Education, marriage, career and money. I think I’ve got it. (Out to the audience) Can you say it with me? Education, marriage, career and money. Education, marriage, career and money.

MAP You only need to say it once.

NORA I learn through repetition, okay? This coming from someone who said “I’m a map” about a billion times?

MAP I’m going to leave now. Good luck on that whole baby thing.

NORA Thanks, Map. Well, we better get started. Right, Galoshes?

GALOSHES Sure.

NORA (To audience) Where’s the first place we have to go?

GALOSHES Okay, hold on a second. Are you talking to me or to someone else?

NORA I’m talking to everyone out there that’s watching me on television.

GALOSHES And are they talking back?

NORA Yes, can’t you hear them?

GALOSHES (Listens, nods head as if agreeing.) No.

NORA Never mind that now. We have to get to Education. (Pause) Where are we going? (She begins to march around the stage with Galoshes following.)

NORA / GALOSHES Ed-u-ca-tion.

NORA Where are we going?

NORA / GALOSHES Ed-u-ca-tion.

NORA Where are we going?

NORA / GALOSHES Ed-u-ca-tion!

(They take a few steps, but are halted by a teacher.)

TEACHER And just where do you think you are going?

NORA The map told me to go through education, Mrs. Teacher.

TEACHER Through education? You mean to say you can just waltz on through education without doing the work?

NORA What work is that?

TEACHER You must do your homework before passing through education.

NORA What is my homework?

TEACHER (Hands her some papers.) Do these questions and the study guide and answer the odd questions on the last page. When you are done with that, you may pass through education. I’ll be waiting.

(The teacher crosses arms and waits. Nora walks away.)

NORA Wow, there are a lot of homework problems to do. I’ll never get my baby now. (To audience) Will you help me?

GALOSHES Maybe you should do your own work.

NORA Ha, ha. You’re silly, Galoshes. We need lots of people to help. Do you want a baby or not?

GALOSHES Not real…

NORA So, here is the first question. What is five plus four?

(Wiper enters)

WIPER This is perfect. If Nora wants to have a baby now, then I need to make a move.

NORA Oh, oh. Look everyone, it’s Wiper. What’s Wiper doing?

WIPER Hey, there. You sure are looking hot today.

NORA I am?

GALOSHES Oh, no, Nora. Wiper is flirting with you.

NORA He is?

GALOSHES (To audience) C’mon, everybody. We need to tell Wiper to stop flirting. Wiper, no flirting. Wiper, no flirting. Wiper, no flirting.

NORA Wait a second! No! Leave him alone!

WIPER Oh, man! (Wiper Exits)

NORA What were you doing, Galoshes? I could have been embarazada.

GALOSHES Have you forgotten already, Nora! Education, Marriage, Career and Money. And besides, Wiper is kind of a stalker. Why is he always following you around?

NORA Stalking is just a creepy way of saying “I like you just a little too much.”

GALOSHES I think creepy is the important word there. Best leave that option alone.

NORA You’re right, Galoshes. What was I thinking?

GALOSHES Obviously not about education.

NORA Hey, the teacher isn’t here. Let’s get out of here and go to the next step.

GALOSHES I don’t think that’s a good idea. You need an education. No child should be left behind.

NORA Let’s face facts, Galoshes. You don’t need an education to get a baby.

GALOSHES Good point. At least you should go to the next step. Where did the map say you should go?

NORA The next step was the bridge of marriage. (To Audience) Do you see where marriage is?

(They pause and stare at the audience. The Blue Arrow enters along with Denny the Bull. Denny stands on a couple of blocks that have been pushed together. The Arrow runs around a bit and then points at Denny. Again, the Blue Arrow can be optional.)

BLUE ARROW Click!

NORA There it is. There’s the Bridge of Marriage. And there’s Denny the Bull. Hi, Denny!

DENNY Hola, Nora. What great adventure are you on today?

NORA I’m trying to get embarazada, but I have to cross the bridge of marriage first.

DENNY I’m thinking this is a puzzle you don’t have to solve yet.

NORA I don’t need any bull from you, Denny.

DENNY But I am a bu....

NORA Let’s cut to the chase. Will you marry me, Denny?

DENNY I’m scared.

NORA It’s a simple question, Denny. Yes or no? (Pause) Why is Denny running away?

GALOSHES You’re getting rather aggressive, Nora. Sometimes you have take things slow.

NORA But I want a baby and I want it now!

GALOSHES Temper tantrums aren’t going to help. Do you need a nap?

NORA Forget this marriage idea. There are plenty of independent women out there that have babies.

GALOSHES Have I mentioned that you’re only four years old?

NORA Career and money is next right? Those go pretty much hand in hand. So what’s a career that can make me a lot of money and embarazada at the same time? (Stares at audience for a long time)

GALOSHES The only profession I can think of would be the world’s oldest profession.

NORA What’s that? (To audience) Do you know what the world’s oldest profession is?

GALOSHES (To audience) Please don’t answer that.

NORA Don’t tell my people what to do.

WIPER (Wiper Enters) Hey, mamacita, I can be your first customer.

NORA Wiper!

GALOSHES Wiper, no soliciting! Wiper, no soliciting!

WIPER Awww, man!

NORA No, Wiper, don’t go away. I’ve lost him again. Aren’t there any other boys out there?

GALOSHES I’m afraid they’re all gone, Nora.

NORA But, if they’re all gone, all that’s left is you.

GALOSHES (Short Pause) Let’s see if the map is still around.

END
```

---

## IC-1180: The Musicians of Bremen

- Title: The Musicians of Bremen
- Author (byline): Wilhelm and Jakob Grimm
- Work: The World’s Best Fairy Tales, ed by Belle Becker Sideman
- Publisher: Reader's Digest Association
- Publication date as stated: 1977
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, DONKEY, HOUND, CAT, COCK, CAPTAIN, ROBBER
- Teaser before the introduction: Yes
- Spoken words (computed): 1206
- Already set (do not supply): none

### Source block (context only)

```text
Author: Wilhelm and Jakob Grimm
Book: The World’s Best Fairy Tales, ed by Belle Becker Sideman
ISBN: 978-0895770776
Publisher: Reader's Digest Association
Date (Month/Year): 1977
```

### Introduction (context only: never use it for content warnings)

```text
This story by the Brothers Grimm is about four farm animals who are convinced they can earn a good living as musicians. Indeed they do, but it isn’t really the sweetness of their barking, braying, mewing, and cockle-doodle-doing, that earns them their supper – it’s more the terror of the sound they make! The Musicians of Bremen by Wilhelm and Jakob Grimm
```

### Performance text (classify this)

```text
Note: The humor of this selection comes through the characterization of each animal and robber as well as the reaction of the narrator to what is occurring. The more outrageous the better. Plan pantomimes, sounds and characters carefully.

NARRATOR: A certain man had a Donkey that had served him faithfully for many long years, but whose strength was so far gone that at last he was quite unfit for work. So his master began to consider how much he could get for the Donkey's skin, but the beast, perceiving that something was up, ran away along the road to Bremen.

DONKEY: There I can be town musician.

NARRATOR: When he had run some way, he found a Hound lying by the roadside, yawning like one who was very tired.

DONKEY: What are you doing that, you big fellow?

HOUND: Ah, because every day I grow older and weaker. I can no longer run with the hunt, and my master has almost beaten me to death. So I took flight, and now I do not know where to turn in order to earn my bread.

DONKEY: Well, I am going to Bremen, to be town musician there. Suppose you go with me and take a share in the music. I will play the lute, and you shall beat the kettledrums.

NARRATOR: The Hound was pleased with the plan, and off they set. Presently they came to a Cat, sitting in the middle of the path, with a face like three rainy days!

DONKEY: Now, then, Old Whiskers, what is bothering you?

CAT: How can one be merry when one's neck is in danger? Because I am growing old, and my teeth are all worn to stumps, and because I would rather sit by the fire than run after mice, my mistress wanted to drown me; and so I ran away. But good advice is hard to find, and now I do not know what to do.

DONKEY: Come with us to Bremen. You are an expert at night music, so you can be town musician, too.

NARRATOR: The Cat agreed, and went along with them. The three vagabonds soon came to a farmyard, where a Cock was sitting on a barn door crowing with all his might.

DONKEY: Your crowing can pierce through marrow and bone. What do you do that for?

COCK: That is the way I prophesy fine weather. But important guests are coming for Sunday dinner tomorrow, and my mistress has told the cook to make me into soup. Tonight I shall lose my head, so I am crowing with a full throat as long as I can.

DONKEY: Ah, but you, Red-comb, should come away with us. We are going to Bremen, to find something better than death. You have a good voice, and if we four make music together it will have full play.

NARRATOR: The Cock was delighted with the idea, and so all four traveled on together. They could not, however, reach Bremen in one day, and at evening they came into a forest, where they meant to pass the night. The Donkey and the Hound lay down under a large tree. The Cat and the Cock climbed up into the branches, but the latter flew right to the top, where he was most safe.

Before he went to sleep he looked around the countryside and thought he saw a little spark in the distance.

COCK: [We] are not far from a house, for [I] saw a light.

DONKEY: If it is so, we had better get up and go toward it, for it’s not very comfortable here in this place.

HOUND: Yes, indeed! A couple of bones with meat on them would be very acceptable!

NARRATOR: So they made haste toward the spot where the light was, and which shone brighter and brighter, until they came to a well-lighted robber's den. The Donkey, as the biggest, went to the window and peeped in.

COCK: What do you see, Gray Horse?

DONKEY: What do I see? I see a table laid out with savory meats and drinks, and robbers sitting around enjoying themselves.

COCK: That would be the right sort of thing for us.

DONKEY: Yes, yes, I wish we were sitting there.

NARRATOR: Then these animals took counsel together how to drive away the robbers, and at last they thought of a plan. The Donkey placed his forefeet upon the window ledge, the Hound got on his back, the Cat climbed up upon the Hound, and, lastly, the Cock flew up and perched upon the Cat. When this was accomplished, at a given signal they commenced together to perform their music. The Donkey brayed, the Hound barked, the Cat meowed, and the Cock crowed; and they made such a tremendous noise that the windowpanes splintered and crashed. Terrified at these unearthly sounds, the robbers jumped up, thinking that some demons had burst in on them, and fled off into the forest. The four musicians immediately made themselves at home, and quickly ate all that was left, as if they had been fasting for six weeks. As soon as they had finished, they put out the light, and each sought for himself a sleeping-place, according to his nature and custom. The Donkey stretched out upon some straw, the Hound behind the door, the Cat upon the hearth near the warm ashes, and the Cock flew up on a beam which ran across the room. Weary with their long walk, they soon went to sleep. At midnight the robbers could see from their retreat that no light was burning in their house, and everything appeared quiet.

CAPTAIN: We need not have been frightened into fits.

NARRATOR: And, calling one of the band, he sent him forward to reconnoiter. The messenger, finding all still, went into the kitchen to strike a light, and, taking the glistening, fiery eyes of the cat for live coals, he held a match to them, expecting the match to take fire. But the Cat flew in his face, spitting and scratching, and frightening him so dreadfully that he made for the back door; then the Hound, who lay nearby, sprang up and bit his leg; and as he limped over the straw where the Donkey was stretched out, it gave him a powerful kick with its hind foot. This was not all, for the Cock, awaked by the noise around him, and cried from his perch on the beam:

COCK: Cock-a-doodle-doo, cock-a-doodle-do!

NARRATOR: Then the robber ran back as fast as he could to his captain and cried,

ROBBER: Ah, my master, there dwells a horrible witch in the house, who spat on me and scratched my face with her long nails. In front of the door stands a man with a knife, who chopped at my leg; and in the yard there lies a black monster, who beat me with a great wooden club. In addition to all that, upon the roof sits a judge, who called out, 'Bring the knave up, do!' -- so I ran away as fast as I could.

NARRATOR: After this the robbers dared not go near their house again, but everything prospered so well with the four town musicians of Bremen, that they never left their new home. And there they have been from that day to this, for all I know.
```

---

## IC-1181: Mystery of Twicknam Vicarage

- Title: Mystery of Twicknam Vicarage
- Author (byline): David Ives
- Work: Time Flies and Other Short Plays
- Publisher: Grove Press Inc.
- Publication date as stated: March 2001
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: SARAH, DEXTER, ROGER, MONA, JEREMY
- Teaser before the introduction: Yes
- Spoken words (computed): 1874
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Ives
Book: Time Flies and Other Short Plays
ISBN: 080213758X
Publisher: Grove Press Inc.
Date(Month/Year): March 2001
```

### Introduction (context only: never use it for content warnings)

```text
It started off quite innocently enough: Two couples meet for a quiet dinner in the home of the Revered Penworthy-Pilks . . . .Three shots are fired, three bullets hit their mark. Three suspects, three motives and one rather lifeless victim. It’s interrogation time as Inspector Dexter investigates the Murder at Twicknam Vicarage by David Ives
```

### Performance text (classify this)

```text
In the dark before curtain: A grandfather clock chimes seven times. Then we hear three pistol shots. A woman (SARAH) screams. Lights come up on JEREMY THUMPINGTON- FFFIENES-that's pronounced "FuhFuh-Fines" lying dead on a rug at center with a glass in his hand. INSPECTOR DEXTER:, in a trench coat, is kneeling over the body. Around them are MONA THUMPINGTON-FFFIENES, the REV. ROGER PENWORTHY-PILKS, SARAH PENWORTHYPILKS, and a couch. "Masterpiece Theatre" accents.

SARAH: Good Lord. Is he . . . ? Is he . . . ? Is he . . . ?

DEXTER: Dead? Yes, 'e's dead. Mr. Jeremy Thumpington--Fuh-Fuh-Fines 'as been shot three times through the heart. Probably within this very room, probably on this very carpet. Very nice carpet, by the way.

SARAH: Thank you, Inspector.

ROGER: (very plummy accent) I'm syorry, Inspyector Dexter. Did you say Jeremy is . . . Jeremy is . . . Jeremy is dyead?

DEXTER: 'is ventricles 'ave been completely ventilated, sir.

MONA: And yet such a brief short while ago Jerry was so alive. He was so terribly, terribly alive.

SARAH: Certainly changes our dinner plans.

ROGER: (pronounces "shooting" to rhyme with 'Jooting") This was a shuuting ekcident, Inspector Dexter?

DEXTER: A what?

ROGER: I presume a shuuting ekcident.

DEXTER: Oh, "shuuting ekcident." No, Rector, this was no mere shuuting ekcident.

SARAH: But you don't mean that it was. . . ? It was. . . ? It was... ?

DEXTER: Murder?

SARAH: Muhdeh?

DEXTER: Yes. It was murder. ROGER, SARAH, MONA: [Sharp, horrified intake if breath.]

DEXTER: Yes. It was murder. ROGER, SARAH, MONA: [Sharp, horrified intake if breath.]

DEXTER: And I believe it was somebody in this very room who murdered him. ROGER, SARAH, MONA: [Sharp, horrified intake if breath.]

DEXTER: I think that's enough of that. Was it you who killed him, Reverend Roger Penworthy-Pilks, the Rector of Twicknam?

ROGER: I? How dyare you insinuate such a thing! You might say I . . . I . . . I loved the man, dyemmit, in some. . . squishy way.

DEXTER: Was it you who killed him, Mrs. Reverend Sarah Penworthy-Pilks?

SARAH: It was not I, for your information, Inspector Dexter.

DEXTER: You're quite a cool, as the Americans say, cucumber. Or did you, the man's own wife, do it, Mona ThumpingtonFuh- Fuh- Fuh- Fuh- Fines?

MONA: Only two "Fuhs" in "Fuh-Fuh-Fines."

DEXTER: Sorry.

MONA: (immediately hysterical) No, I didn't kill him! I swear it! Yes, yes, I wanted him dead sometimes. I planned to murder him every now and again, often on Tuesdays for some reason. I even bought a rare Pakistani poison and a set of pinking shears that might've seemed an accident. But no I didn't kill him! I'm innocent! I swear it by all that's holy!

DEXTER: Protesting a bit much, if you ask me. Well, one of you did it and I'm going to find out who.

MONA: I always envied you, Sarah. I confess it. Your beauty. Your coolness. Your beautiful bottom. Your thrilling long, long legs. Your beautiful bottom. Did I say beautiful bottom already? Your Wedgwood. Your tea cozies.

SARAH: And my husband. And your husband.

MONA: You slept with him, didn't you?

SARAH: Only once, but it wasn't successful!

MONA: I was speaking to Roger, thank you

SARAH:. You slept with Jeremy didn't you?

ROGER: Only twice, and it wasn't. . . very successful.

SARAH: Well I've slept with you twice and I can believe that. And I slept with Jeremy three times and we were very successful.

ROGER: Viper.

SARAH: Amphibian. [They stick their tongues out at each other.]

DEXTER: Rector.

ROGER: Inspector?

DEXTER: Jeremy Thumpington-Fuh-Fuh-Fines was quite sexually active, was he not?

ROGER: Inspector, the man was insatiable. I once came in here and thought he was sleeping on the sofa-actually he was sleeping with the sofa. The liaison went on for some months, until he chucked the sofa for my green leather wingchair.

DEXTER: You're not suggesting the sofa might've shot him--?

ROGER: I suggest you question the sofa. Maybe then you'll find the trooth. ..

DEXTER: The what?

ROGER: The trooth. You know. The fyects.

DEXTER: Ah, the "fyects." Yes, I demand the fyects about what happened here tonight!

MONA: Oh, who cares who killed Jerry! He's dead, isn't he? That's all that's important, isn't it? That he's gone to glory? Passed over? Gone west? Put out to sea? Kicked the bucket? Cashed in, popped off, pegged out, curled up his toes, slipped his cable, croaked on this beautiful carpet during cocktails? isn't what what's important? Well. . . Not under the circumstances, I suppose. . .

DEXTER: Rector.

ROGER: Yes, Inspector.

DEXTER: Was there any tension in the room prior to Mr. Thumpington-Fuh-Fuh- Fines's death?

ROGER: Tension? Was there tension, darling?

SARAH: Tension?

ROGER: Let me think backwards. . .

Lights change as ROGER, SARAH, and MONA walk backwards as if into flashback. JEREMY: springs to his feet, drinks glass in hand. He's got three bright red bullet holes in his shirtfront. Inspector Dexter remains, and observes.

JEREMY: (wobbling drunk) Well isn't this is a bloody boring party.

MONA: I hope you made the cheese things. I do love the cheese things.

ROGER: The cheese things are scrumptious, are they not.

SARAH: Have we all seen 'Prime Suspect 15?

MONA: It’s not nearly as good as '12'.

JEREMY: Bollocks. My God, we're not going to sit about and make bloody small talk all evening, are we? Talk about the weather and cheese things and what we've seen on the telly? Might as well critique the shape and consistency of human turds as talk about what's good on the telly.

MONA: (weepy) Spoilsport. Sad sack. Gloomy boots. Party pooper.

JEREMY: You know we're all going to croak someday. All freeze.

SARAH: (out front, spookily) It was almost as if he'd had a premonition about his own death. All unfreeze.

JEREMY: I could be a corpse on this carpet in a moment-beautiful carpet, by the way-and I'm supposed to discuss the bloody cheese things?

MONA: Stop it, Jerry, stop it, stop it! I hate it when you get morbid like this!

JEREMY: My God, does none of us read? Does none of us think? Does none of us have anything at all of substance to say? Look at us. None of us is living a life worth living. We're pathetic toothy boring creatures with ridiculous accents. We're a lot of rotting corpses is what we are. Isn't that the terrible horrible awful truth?

MONA: Stop it, Jerry, stop it! You're drunk!

SARAH: (throwing her drink in Jeremy s face) Damn you!

ROGER: (throwing his drink in Jeremy's face) Damn you, Jeremy ! Sir, you're a cad!

SARAH: Just then, the clock started to strike. The lights went out. And on the final stroke of seven. . . We hear three shots. Jeremy falls to the floor. Bang, bang, bang. Three shots. Probably from a Webley 45. Just a guess. Then somebody screamed. I think it may have been me. She screams.Yes, it was me. And when the lights came up. Lights back up to full. Jeremy was lying in missionary position on my carpet.

MONA: I can't believe that such a brief short while ago he was so alive, he was so terribly, terribly alive . . . I'm sorry, did I say that already?

DEXTER: If what you say is true, Mrs. Penworthy-Pilks, then the murder weapon is still in this room.

ROGER, SARAH, MONA: [Horrified intake of breath.]

DEXTER: Indeed, the fatal pistol is still in someone's pocket. All three reach for their pockets and look about suspiciously. It's not as if any of you lacked motive. Why, even the furniture wanted him dead.

MONA: But we didn't want him dead. We loved Jeremy. He was so charming, so fun, so . . .

SARAH: So priapic.

MONA: Priapic. What's priapic?

SARAH: [Spreads her hands apart to show the size if Jeremy's sexual endowment.] So priapic.

DEXTER: Well I'm going to have the truth. Excuse me. The trooth.

ROGER: Inspector. I have a confession to make.

DEXTER: What sort of confession?

ROGER: Well, I don't much believe much in God much anymore. . .Anyway, now that I'm confessing I might as well say I don't really like the cheese things very much either. (high drama) I can say that now. I never much liked the cheese things very much, though I always said they were scrumptious. The trooth of it is, I was lying.

DEXTER: Must we discuss the bloody cheese things?

MONA: Jerry said exactly the same thing, just before he was riddled with hot lead.

ROGER: In any case, Inspector, you can take me away-for it was I who ventilated Jeremy's ventricles. SARAH, MONA, DEXTER: [Horrified intake of breath.]

ROGER: (takes out a small pistol.) I ended his life with this starting pistol SARAH, MONA, DEXTER: [Horrified intake if breath.]

ROGER: Which I stole from my public school when I was 12. SARAH, MONA, DEXTER: [Horrified intake of breath.]

ROGER: It's very hard to say all this as a disbelieving Christian because now I'm going to be hanged and I'll go into eternal empty void nothingness forever and ever instead of paradise-a nice place I always pictured rather like Brighton but without the tourists. Anyway I loved Jerry in some. . . squishy way. . . Did I say that already? But I couldn't stand it when he threw me over for the sofa, especially since I so badly desired that sofa yourself. Then when I found Jeremy'd had my green leather wingchair it was too, too much. My God, he had a passion for things!

SARAH: Just one moment, Inspector. As a partially disbelieving Christian I cannot allow this to happen. It was not only Roger with the starting pistol who killed Jeremy, it was I-with this Webley 45. Lifts her skirt and shows a gun strapped to her leg. Dexter whistles, Mona howls, and Roger barks like a dog. Thank you. Anyway I'm willing to face my Maker-if there really is one. My true punishment is to've killed the only man I ever loved.

MONA: Stop, Inspector! It was not only Sarah with the Webley and Roger with the starting pistol. It was I, with this .505 telescopic elephant hunting rifle. She takes an enormous hunting rifle from behind the couch. I shot him in conspiracy with the sofa, who hid the weapon for me. I don't need to tell you why I killed him. It was the sardine sandwiches he had for breakfast.[Jeremy jumps to his feet.]

JEREMY: I say, chaps, is dinner on yet? I'm sorry. Was I copulating with the rug again? Oh dear, I say, I seem to've been shot.

ROGER: Yes, Jerry, I'm afraid there's been a bit of a . . . shuuting ekcident.

JEREMY: Oh, a shuuting ekcident. Well the bullets seem to've ventilated but not violated my ventricles. (To Dexter) Who're you?

DEXTER: Larry Dexter of the Yard, sir.

JEREMY: I say, haven't we slept together?

DEXTER: That would be two years ago last April, sir. Oh, yes. The butterscotch pudding. But if you're not dead, sir, I have to say my purpose in life is quite evaporated. (weeps) I've been rendered redundant.

JEREMY: In any case, chaps, I apologize for being so utterly beastly before the. . . Shuuting ekcident. All that morbid rot about death and corpses. But you see, some weeks ago I had a dramatic personal revelation. Because my doctor told me I had this. . . I had this . . . I had this ingrown toenail. I'd quite given up on life, you see. The bally thing made me so damned bitter and nihilistic.

MONA: Jerry, you never told me about your toenail!

JEREMY: I wanted to spare you, darling. The funny thing is, as I was lying there ventilated on the carpet I actually crossed over to the other side and I saw God, you see.

SARAH: You saw God? My theological doubts are dissipated!

JEREMY: God suggested I start appreciating things and stop copulating with them. Mostly I realize now how much I love you all-well I have loved you all haven't I, in quite a variety of ways. I mean the hammock was brilliant!
```

---

## IC-1182: Naughty or Nice

- Title: Naughty or Nice
- Author (byline): Jonathan Mitchell and Seth Lind
- Work: Not specified
- Publisher: National Public Radio
- Publication date as stated: Dec 2014
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: UNIDENTIFIED PERSON, NEWSCASTER, NAUGHTY CHILD, BELL, SPARK, MICHAEL, UNAMED ELF, SANTA’S SECRETARY, SANTA, COAL LOBBYIST, MALL CREW LEADER, LITTLE GIRL, MOM, FACTORY ELF, MICHAEL’S MOM, MICHAEL’S DAD
- Teaser before the introduction: Yes
- Spoken words (computed): 1227
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jonathan Mitchell and Seth Lind
Weblink to full text : https://www.npr.org/2016/12/23/506759045/encore-an-elf-questions-
santas-naughty-or-nice-system
Publisher: National Public Radio
Date (Month/Year): Dec 2014
```

### Introduction (context only: never use it for content warnings)

```text
Naughty or Nice by Jonathan Mitchell and Seth Lind
```

### Performance text (classify this)

```text
UNIDENTIFIED PERSON: (singing) You better watch out. You better not cry. You better not pout. I'm telling you why.

NEWSCASTER: Deep inside the North Pole . . . past the tinsel, beyond the twinkling lights, is Santa’s highly efficient, questionably ethical corporate headquarters. Forget sugarplums; this is surveillance footage, performance reviews, and elves with access cards. In a world where 30 seconds of bad behavior can earn you a lifetime supply of coal, one idealistic elf dares to ask the unthinkable: “Um . . . are we sure?” This is what happens when Christmas meets middle management. Sit back, stay off the naughty list, and enjoy . . .

NAUGHTY CHILD: I hate mashed potatoes. (yelling) You don't love me!

BELL: (training) OK. So, we're obviously seeing a class F temper tantrum.

SPARK: F is?

BELL: Food.

SPARK: Right - food. Food related.

NAUGHTY CHILD: (yelling) You don't tell me what to do!

BELL: So, go ahead and click naughty. She gets a lump of coal and, you know, she learns from that experience. (Spark hesitates) Click naughty. (laughing)

SPARK: Just like that? (finally clicks the naughty button)

BELL: Who do we have next?

SPARK: Michael Simmons . . . age 8. Tulsa, Oklahoma.

MICHAEL: Get out of here. Get out of here!

BELL: All right, so I'm going to give this one to you. Let's see how we do.

MICHAEL: Stop being annoying! You've just been a little, annoying brat!

SPARK: He's mad at his sibling.

MICHAEL: I hate you!

BELL: (shocked) That's an I hate you?! Hate's a word that you can't take back. Click naughty.

SPARK: But we have the tapes from the full year or more.

BELL: Yeah. If we looked at the tapes for the whole year, we'd be sitting here for a full year.

SPARK: So that's just naughty? (frustrated) Great. Michael Simmons - naughty.

BELL: Yeah. You got it. So you're all set?

SPARK: (disillusioned) Yeah.

UNAMED ELF: (raising hand) This one I was watching earlier today decided to feed all of his Ritalin to his Fox Terrier. His mom had to take him to the vet's office. The kid tore all the way through his sister's room. He took a leak in her toy chest.

BELL: Wow! That is layer upon layer.

UNAMED ELF: We'll see how he feels on the morning of the 25th. We'll see what's funny then.

SPARK: Do the kids actually know we’re watching them all the time?

UNAMED ELF: It's in the song, right? (singing) He sees when you're sleeping. He knows when you're awake. He knows when you've been bad or good. (speaking) It's right there.

SPARK: What if we gave the parents more input. They are with these kids all the time. They can weigh in. I'm just surprised that the system...

BELL: (dismissive) They're not going to be objective -- especially when they're getting free presents from Santa.

UNAMED ELF: Don't overthink this, all right? You got yourself a nice, cushy job here. You want to sacrifice all that to go back to the toy factory? You want to shovel Rudolph's dung?

SPARK: (backtracks quickly) No. Definitely not. No. Glad to be here. (steps out of scene to speak to the audience) See, I don't want to complain about this job. But I'm looking at like 30 seconds of video of a kid, and then they're breathing down my neck to make an instant decision, like, this kid's naughty; this kid's nice. I really don't think this is how Santa would want it to run. (as if hearing a call out from the audience) Talk to Santa? (loves this idea)

***** In Santa’s office*****

SPARK: Hi. I put in for a meeting with Santa today. I'm Spark.

SANTA’S SECRETARY: Excellent. So what we're going to do is I'm going to alert your department as soon as there's an opening to meet with Santa. . . He's super duper busy with all the children's wish lists.

SANTA: (exiting his office, shaking another person’s hand) Thanks for coming by.

COAL LOBBYIST: Remember the magic number is 2000 tons. If this works out, we'll all have a Merry Christmas.

SANTA: Ho, ho, ho. (both exit)

SPARK: Who was that with Santa?

SANTA’S SECRETARY: The most influential lobbyist for the coal industry and a very, very good friend of Santa's. . . Oh, good news. I see an opening on Santa's calendar in July.

SPARK: You know how many months away that is?

SANTA’S SECRETARY: If you want to get in here any earlier, you're going to have to sit on Santa's lap. (laughs) Just kidding. ***** In the sleigh area*****

MALL CREW LEADER: Mall crew on sleigh 6. I need all of my mall elves on the sleigh now.

SPARK: (raises hand) I'm on the mall crew -- I'm a trainee.

MALL CREW LEADER: There are no trainees on the mall crew. You ever been to a mall with kids who are drinking hot cocoa, eating candy, about to meet the most important man in the world?

SPARK: (attempting a bribe) Listen. I've got a candy cane I don't need. And it can be your candy cane if I just get on that sleigh.

MALL CREW LEADER: (sucking on the candy cane) You have no idea what you are in for! ***** In line for Santa at the mall*****

LITTLE GIRL: (whispering) Mommy, there's an elf in front of us.

MOM: Shh. Katie, that's not very nice.

SPARK: Zip it, kid.

SANTA: Santa's got an empty lap here. Come on up here. You've been nice all year long?

SPARK: (climbing on Santa’s lap) So Santa, this isn't about any present for me or anything. I actually work in the Naughty or Nice Division. And I am surprised and worried about how it works. We spend our whole day watching the surveillance videos of kids. Pushing the naughty or the nice button.

SANTA: Of course. Ho, ho, ho.

SPARK: Here's the thing. They are all nice and naughty. Every kid is both. Life is nuanced. Right? And we're reducing it to this yes or no thing.

SANTA: I see the problem. You are a very perceptive little elf. (to staff) Bring me my phone.

SPARK: You can fix this?

SANTA: Yes, I can. Merry Christmas. Ho, Ho, Ho (ushers Spark away and talks into the phone) ****** The next day at Human Resources *****

BELL: (seriously) Thank you for coming in. We got a call from Santa yesterday.

SPARK: That doesn't surprise me because I met with Santa yesterday. And it turns out that he is not pleased with how the naughty or nice system is being implemented.

BELL: (continuing as if Spark hasn’t spoken) There are 50 million children in the United States alone. If we spend all of our time poring over the nuances for each child, we'll never get through our list. Tomorrow you report to toy factory 19. In this department, we need elves who can trust their instincts.

SPARK: Trust? I trusted that the system was fair, and now I've seen inside it, and it's just a bunch of flawed elves watching a bunch of flawed people deciding who is. . .

BELL: We can't let kids go without consequences. They'll grow up to be monsters. We are here to teach kids a lesson.

SPARK: (indignantly) I saw Santa meet with a coal lobbyist!

BELL: (patiently) Well, Spark, that's his job. Do you know how much cheaper a piece of coal is than a toy? It's just the economics of Christmas. (no-nonsense) Tomorrow, you to report to toy factory 19. ***** Toy Factory*****

FACTORY ELF: (training; holds onto two cables, pulling each as they chant) Green, red, red, green, red, green, green . . . Spark, are you paying attention?

SPARK: What happens if I pull the wrong cable?

FACTORY ELF: Green cable, pre-assigned gifts. Red cable, coal. Just pull the right cable. That's the whole job.

SPARK: But if I accidentally were to pull the wrong one. . .

FACTORY ELF: A good kid would get a piece of coal.

SPARK: Or a bad kid gets a present?

FACTORY ELF: You're the last line between the gifts and the kids, OK?

SPARK: Right. I will not pull the wrong cable by accident. . . ***** Christmas morning at Michael’s House*****

MICHAEL: Here's one for me! It says from Santa!

MICHAEL’s MOM: (shocked and surprised) What?

MICHAEL: (unwraps present excitedly) Look, it's just what I wanted! And it’s blue! Oh, my gosh!

MICHAEL’S MOM: (aside to Dad) You did it . . .

MICHAEL’S DAD: Why would I do it? I didn’t! Honey, I didn’t do it. ***** Back at the Toy Factory*****

SPARK: (smiles and gives 2 thumbs up; singing as she pulls only the green cable) You better watch out. You better not cry. You better not pout. I'm telling you why. Santa Claus is coming to town.
```

---

## IC-1183: Nina in the Morning

- Title: Nina in the Morning
- Author (byline): Christopher Durang
- Work: Durang, Durang
- Publisher: Dramatists Play Service
- Publication date as stated: June 1996
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, NINA, JAMES, FOOTE, LA-LA, ROBERT
- Teaser before the introduction: No
- Spoken words (computed): 1134
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christopher Durang
Book: Durang, Durang
ISBN: 978-0822214601
Publisher: Dramatists Play Service
Date: June 1996
```

### Introduction (context only: never use it for content warnings)

```text
Everyone has a story, a history that is unique. Unfortunately, in America the elderly are not a valued sector of society. For this reason many Americans are in denial of aging, the plastic surgery industry his exploded and women are perpetually turning “29.” As a culture, we appreciate vintage in wine, not people; we "distress" furniture to make it look old, but pay thousands of dollars to erase the wrinkles that time bestows on our faces. It’s a futile battle we are all destined to fight. Today Nina is another day older as we take a tongue-in-cheek look at aging with Nina in the Morning by Christopher Durang.

The NARRATOR is onstage. He is dressed in a tuxedo and looks elegant. As the music is finishing, NINA enters. She walks towards her chaise with great regalness, as if she's in a procession, on her way to be crowned. When the NARRATOR speaks, he is speaking her thoughts, usually. So her facial expressions change with his comments. She does not otherwise look at him or relate to him (with a couple of noted exceptions)
```

### Performance text (classify this)

```text
NARRATOR: The mist hangs heavy over the ocean today. Nina woke from an uncertain sleep and walked to the chaise in her dressing room and sat in front of the beautiful, cherished mirror. (NINA sits on her chaise, and looks out to her mirror and gasps.) Her facelift had fallen during the night, and her cheeks were held in place by straight pins.

NINA: (Looking in mirror, touching her face delicately) Oh, Lord. Oh, Lord. How dreadful. (Enter JAMES, her child, dressed in short pants and a white shirt. He looks like a well-dressed prep-school boy)

JAMES: Good morning, mother.

NINA: Don't kiss mommy today, her face is precarious.

JAMES: I don't want to kiss you anyway. I hate you.

NINA: Please don't upset me, James. My plastic surgeon is in Aruba.

JAMES: What's this pin for? (Reaches for her face, pulls out a pin.)

NINA: James, stop that. Stop it. Foote! Foote! Come quickly, James is at my face again.

NARRATOR: But James kept reaching for Nina's face, over and over.

NINA: Stop it, you unruly child. (JAMES keeps trying to pull pins out of her face. NINA keeps trying to protect her face. All the pin business is mimed. FOOTE, the family manservant, enters. Dignified and in a tuxedo.)

FOOTE: You called, Madame?

NARRATOR: Foote, seeing Nina's predicament with her son, pulled James away from her, pushed him to the ground and sat on him. (FOOTE pulls JAMES away, pushes him on the ground and sits on him.)

NINA: Gently, Foote, gently.

JAMES: (Struggling with FOOTE.) I hate you, mother, I hate you.

NARRATOR: Foote took out a hypodermic from his jacket pocket, and gave the misbehaving child a shot. JAMES I hate you. I'm sleepy. (Passes out.)

FOOTE: Will that be all, Madame?

NARRATOR: Foote was the family manservant, and often gave the children general anesthesia whenever they became unruly. Foote had once been a dentist.

NINA: Thank you, Foote. James was pulling pins out again. I must have done something wrong raising them. I thought I often smiled. I wonder if they wanted anything else.

FOOTE: Do you wish me to remove any teeth while he's out?

NINA: No, no. Leave his teeth alone, Foote. I just want quiet for a while. Look at how peaceful James is, curled on the floor. I always liked my children best when they were unconscious.

FOOTE: If Madame needs me further, just call.

NINA: Thank you, Foote. You're a jewel. (FOOTE exits.)

NARRATOR: Foote withdrew, leaving Nina with her thoughts. She thought about her face. She thought about James. Psychotherapy had been no help for James except perhaps in helping him to express his anger more freely, and how useful had that been.

NINA: (Sort of to herself.) Not very.

NARRATOR: Nina's hands shook as she lifted a coffee cup to her face. Her perceptions were off, and she poured hot liquid down the left side of her face. She put cream and sugar on her face, stirred it and then rang the bell for Foote.

(NINA mimes the actions the NARRATOR says above while, or shortly after, he says them. She does all the gestures without emotion. She feels the heat of the coffee and the mess of the liquids after she has done all of them. She makes a face of pain, and confusion, then rings the bell.)

NINA: Foote, I need you. Bring a wet cloth. I'm sticky.

NARRATOR: Foote brought a basin of warm water and a roll of gauze and sponged her gingerly. (FOOTE enters and starts to pat NINA's face lightly with the cloth.)

NINA: Do you think I'm beautiful, Foote?

FOOTE: You once were very striking, Madame.

NINA: Yes, but now, what do you think of me now?

FOOTE: (Looks at her.) You have quite a nasty burn on your face, Madame. Would you care for a shot of novocaine?

NINA: Go away, Foote. I want to think.

NARRATOR: And again, Foote withdrew, dragging James after him. Nina racked her brain, trying to remember what she wanted to think. The colors of her wall were beige. She had wanted burnt orange, but the designer had run through the house screaming "Beige! Beige!" and they finally had to give him his way.

NINA: (Out, to the imagined designer.) I wanted burnt orange, but you have given me beige.

NARRATOR: Later the designer turned against her too, like her son James. No, no, Nina wanted pleasant thoughts, nice things. Flowers, butterflies . . .

NINA: (Hopefully.) Little duckies.

NARRATOR: The Little Prince by Saint-Exupéry. That was a nauseating little book, she had never finished it. Some monk gave it to her when her car had been stopped at a traffic light.

NINA: Foote, if any Jehovah's Witnesses come today, show them in, will you?

NARRATOR: But no Jehovah's Witnesses came. And Nina found she had to fill the time with thinking and reminiscing. Nina had once been beautiful.

NINA: I am very beautiful.

NARRATOR: Men would stop on the street to stare at her. She caused traffic accidents. Jealous women would rush up to her in their homeliness and try to kill her.

NINA: Homely women were always trying to shoot me. It was flattering really.

NARRATOR: Everywhere she went, her eyes would anxiously seek out the mirrors. Sometimes she would bring her own mirrors with her.

NINA: Put this up, would you?

NARRATOR: Nina would say, lugging a large mirror, and few could deny her. Her love affairs were unpredictable and random. Sometimes it would be royalty, other times it would be the men from Con Edison. (The NARRATOR turns his back, pretending to look at a power box. He is now the CON EDISON MAN. NINA comes up to him, stands close and seductive.)

NINA: I don't really know where the power box is, I'm afraid. Would you care to lie down? (The NARRATOR reverts to his narrator role, and addresses the audience again.)

NARRATOR: Sometimes when she was especially lonely, she would try to seduce her children.

NINA: Don't you find mommy especially attractive today?

NARRATOR: She would ask James . . . and Robert . . . and occasionally poor La-La.

LA-LA: (Happily and monotonously singing to herself.) La-la-la-la-la, la-la-la-la, la, la, la, la . . .

NARRATOR: La-La was retarded, and Nina hated her.

NINA: La-La! Pay attention! (LA-LA turns away, opens up her lunch box and starts looking through it happily.)

LA-LA: La-la-la-la-la, la-la-la . . .

NINA: Uhhhh. You're willfully retarded.

NARRATOR: Nina would shout this at La-La, and then hit her. But Nina mustn't think of the past now. The present was what held promise. Her plastic surgeon was due back in several days. (NINA rings the bell.)

NINA: (Grandly.) Foote, I want a cruller!

NARRATOR: She heard what she presumed were Foote's footsteps, but they belonged to her second son, Robert, who fired two shots, one of which grazed her shoulder. (Enter ROBERT, dressed the same as JAMES but with the addition of the glasses. He shoots a pistol twice at his mother. On the second shot, NINA moves her shoulder as if hit.)

ROBERT: I hate you, mother!

NARRATOR: Then he ran into the garden. (ROBERT runs off. NINA holds her shoulder and rings the bell again.)

NINA: Foote, bring the gauze again, please. My shoulder is bleeding. Foote! Foote!

NARRATOR: James's father had been a tax lawyer, but Robert's father had been one of twenty men; and La-La's father had been one of fifty-six men that busy summer she had the beach house painted. After a brief burst of self-judgment, she searched the thesaurus for alternatives to the word "promiscuity."

NINA: (Miming looking in a dictionary.) Synonyms include "debauchery." "Salacity." And "lubricity." "Lubricity." "Loooo-bricity." "Loooooo-briiiiiiii-ci-teeeeeeeeeee.

NARRATOR: Nina liked the sound of "lubricity" and that summer she would climb up the ladders and whisper the word into the house-painters' ears. (The NARRATOR finds himself near NINA. She stands and seductively whispers in his ear, as if he's the house painter.)

NINA: (Whispering into his ear.) Lubricity. (Enter FOOTE with some more gauze.)

FOOTE: Has Madame been shot?

NINA: Yes, Foote. Robert said something to me, something mean, and then he shot me. What took you so long?

FOOTE: I'm sorry, Madame. I was giving La-La a hypodermic shot to calm her down. She was complaining about something and acting retarded, and now she's quiet and good as a lamb.

NINA: Go away, Foote.

FOOTE: Yes, Madame.

NINA: Oh my life, my life, my life. What has become of my life? (Looks in the mirror anew.) And what has become of my face? Oh my. Pins are for curtains, not for faces.

NARRATOR: Nina stared at herself in the mirror and tried to decide whether or not to kill herself. She stared a long while. She didn't look well. Slowly she took the pins out of her face. (NINA mimes taking pins out. Then she pulls her cheeks downward, and stares tragically at herself in the mirror.)

NARRATOR: Her cheeks drooped downward, and her eyes filled with tears. Of course, when the doctor returned from Aruba, he'd make Nina look substantially better. And she didn't know how to kill herself, unless one of her children shot her.
```

---

## IC-1184: The Original Last Wish Baby

- Title: The Original Last Wish Baby
- Author (byline): William Seebring
- Work: The Best American Short Plays 1996-97
- Publisher: Applause Books
- Publication date as stated: Nov 1996
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: DOCTOR, NURSE, NARRATOR, EXECUTIVE, ASSISTANT, MAN, MS. KORNFELD, REPORTER, WELDA, CLARA, CUSTOMER #2, CUSTOMER #1, GE PITCHMAN, WOMAN, KORNFELD, NEWSBOY, JUDGE, SURGEON
- Teaser before the introduction: Yes
- Spoken words (computed): 2509
- Already set (do not supply): none

### Source block (context only)

```text
Author: William Seebring
Book: The Best American Short Plays 1996-97
ISBN: 978-1557832559
Publisher: Applause Books
Date: Nov 1996
```

### Introduction (context only: never use it for content warnings)

```text
The Original Last Wish Baby, as researched, recorded and revised by William Seebring. Cleveland, Ohio. Or, more specifically, the third-floor maternity room of the Holy Name Hospital on Cleveland's impoverished west-side where, at precisely seven-oh-one P.M. A baby was born. Not just any baby, but the infamous, original, Last Wish Baby. The baby born without a heart.
```

### Performance text (classify this)

```text
DOCTOR: No heart? Good Heavens, that's impossible.

NURSE: Check for yourself, Doctor. [The DOCTOR extends his stethoscope into the crib.] DOCTOR: Nothing, no pulse. Not a sound. And yet, this baby clearly mimics life. A freak.

NURSE: A miracle. . . the baby is a miracle.

DOCTOR: A miracle? This is Cleveland. It'll be a miracle if the mother's insured.

NARRATOR: Not only were the baby's parents uninsured, the identity of the baby's father was unknown. However, the birth mother's name was given as Welda Mae Forms, a thirty-one-year-old unemployed cosmetologist. At the time, little else was known about Ms. Forms but word of her remarkable progeny spread quickly from the maternity ward to the scrub rooms to the hospital's administrative offices where a larger picture began to emerge.

EXECUTIVE: A baby born without a heart? Sounds awful. Sounds really awful.

ASSISTANT: Maybe not as bad as you think.

EXECUTIVE: C'mon Chet, how the hell do ya' window dress a missing heart? God knows we've had our share of high-risk deliveries here at Holy Name-little baby heads get smushed, tiny baby limbs get... it's messy, terrible, makes me shudder. But delivering a baby and not the heart-good God! [Beat.] What's our liability on something like that?

ASSISTANT: Well here's the thing, sir. . . the baby is alive. The baby is fully functioning, quite spirited and has a healthy appetite I might add. Its short life could, with the right spin, be played out as the most incredible P.R. story of our time. What's more, the timing couldn't have been more. . . fortuitous. . . sir. A miracle. . . and it happened here, in our hospital, under the care and guidance of our health care professionals. Think of it sir, Holy Name, the get-well place where miracles happen.

EXECUTIVE: Good boy. Oh, one other thing. . . the heart? Did anyone ever find the heart?

ASSISTANT: No. Actually, as far anyone knows, there never was a heart.

NARRATOR: In point of fact, there was a heart. However, through one of those unfathomable anomalies which defy all logic, yet govern most things, the heart was delivered separately by a surprised New Jersey woman on her way home from the store.

[Lights up on MS. SYDNEY KORNFELD, as she crosses the stage. She is walking past a MAN when something like a beef-steak tomato falls from her skirt. MS. KORNFELD continues on, unmindful.]

MAN: Yo, Miss. . . Ma'am! You dropped something. .[MS. KORNFELD stops, turns and looks back.]

MS. KORNFELD: Oh-my-god, what is it! [Lights dim on MS. KORNFELD as she bends to retrieve the heart.]

NARRATOR: That something would later be determined to be the baby's heart. However, at that particular moment, the New Jersey woman, later identified as Ms. Sydney Kornfeld, and who would soon become known as "The Baby Heart Mom," was not yet aware of the miracle baby story unfolding in Cleveland. As for Ms. Kornfeld, she fortuitously retrieved the baby heart and returned immediately to her home in Paramus where, as the demonstrator shall faithfully recreate, she placed the pulsating vital organ into a clear, air-tight, number-seven tupperware container, which she then filled with a high-fructose, low sodium, heavy-syrup drained from a can of Libby's yellow-cling sliced peaches. After burping for a tight seal, Ms. Kornfeld placed the container in the crisper drawer of her refrigerator where, according to product designers, the heart could have been stored indefinitely and would remain every bit as fresh and vigorous as the moment she delivered it.

REPORTER: But, what about the baby's mom? I'd like to hear her side of the story. I'd like to ask her a few questions.

ASSISTANT: Uh, well, actually-that's impossible. I'm sorry, we're just, she's just-she's in recovery right now.

NARRATOR: In fact, Welda Mae Forms was not in recovery. The so-called Baby Mom was not only alert and well-rested, she was, much to the dismay of hospital staffers, quite lucid and most out-spoken.

WELDA: What's with the seat belts! And where's my kid! I come into this dump to pop off another slug, which is the last thing I need, and you-all got me tied down so I can't even see Oprah!

EXECUTIVE: Ms. Forms, please, please calm down. There's something we have to tell you.

WELDA: What, is my baby dead, or deformed, or something?

ASSISTANT: Ub, well, Miss Forms, actually, it's more than that.

WELDA: Huh? Was that a hard question or are you really as stupid as you look? Listen here lap-dog, tell your fat boss that as far as I'm concerned I could care less if the little maggot's dead or mutated-hell, I never wanted one tuh begin with. Tried to have it flushed out in one of them clinics but them bible-thumpers chased me away and SO, I figured I'd drown the slug in booze. Well, did it work or what?

ASSISTANT: This is insane. We can't put that before the public. She'll ruin everything!

NARRATOR: Meanwhile, at that very moment, the afternoon press conference was being fed via satellite to network studios in New York. And news it was. "Within the hour, satellite-beaming reporters from around the world had descended on Cleveland like the plague and every last one of them wanted one thing-a baby mom exclusive. Hospital officials acted with both haste and prudence.

CLARA: Hello, Ms. Forms. My name is Clara Collins, I've been hired to be your image consultant.

NARRATOR: Clara Collins proved she was worth every penny of her hefty fee. In short order, Ms. Welda Mae Forms was polished, enlightened and coiffured. At long last, cameras were admitted into her room and a nation known for its thirst of spectacle, tuned in.

WELDA: [Her hands folded as if in prayer.] With the Lord's help, my precious, precious baby will live. Of course, I can't begin to thank all you wonderful little people out there who have kept me and my baby in your thoughts and prayers. Bless you. Bless you all.

NARRATOR: With that one newsbit, the groundswell of public emotion became unquenchable. Overnight, Cleveland's miracle tot became America's most adored critical-list baby. There were news conferences every morning and afternoon and updates on the baby's condition flashed every hour on the hour, but it wasn't enough. Americans not only wanted to know more, they wanted to know what more they could do . . .

CUSTOMER #2: And they say that baby could die any moment.

CUSTOMER #1: Hate to see that baby die and me not knowing if they was something I coulda' done.

CUSTOMER #2: Can't give baby my heart. But I'd give that baby anything else. Anything a'tall.

CUSTOMER #1: Say, you know I hear baby likes to watch big time wrestling! What say we call the hospital and see if we could buy that baby a brand new color TV! Now wouldn't that make us all feel a whole sight better?

NARRATOR: Calls from like-minded Americans jammed the hospital's switch-board. It was reported that in a single, twenty-four hour period more than twenty thousand color TV's were bought and delivered. Corporate America stood up and took note. Syndicate giant, GLAM ENTERTAINMENT, culled their best minds and put forward a most alluring concept.

GE PITCHMAN: Every night we'll feature the baby mom, Welda Mae Forms. We get her and we call it, "The Last "Wish Baby Show." See, every night mom stands in front of the camera holding little baby no-heart in her arms like this and she's pouting 'cause the doc's are telling her how the baby's supposed to die any minute but, and here's the kicker, before baby goes, baby's made this one last wish. . . get it? Baby's last wish- Last Wish Baby!

NARRATOR: A deal was proffered and quickly struck with Ms. Forms and her people. That very night, "The Last Wish Baby Show" blew out the ratings board with a whopping 75 share. Even more notable, the show's seamless tie-in with corporate sponsors set an industry standard.

WELDA: Poor, poor baby. Baby doesn't have a heart. Doctors say baby might have to leave us all for Heaven any minute now.[we hear the baby cry.] What's that Baby. . . ? [After leaning in to the baby, WELDA returns her gaze to the cameras.] Awww. Baby wishes some nice person out there would buy us a uh . . . a Sony XRK-35 Digital Game System.

NARRATOR: Meanwhile, in a certain kitchen in Paramus, New Jersey, a certain Guatemalan cleaning woman was wiping down a certain refrigerator when she made an unusual discovery.

WOMAN: Eeeeee! Mios Dios! Eeeee!

KORNFELD: What? Que? Que esta? What the hell is it?

WOMAN: Nino! Nino con last wish! Nino con last wish!

KORNFELD: Baby? You mean that baby? That Last Wish baby? The one on TV? Give me that! [Studies the heart for a moment.] Oh-my-God, it's alive! I have the baby heart! What should I do? What should I do?

WOMAN: Llama de medico! Pronto! Pronto!

KORNFELD: Call a doctor?! Are you crazy? This is big, really big! I'm calling Howard Stern!

NARRATOR: Ms. Kornfeld's call to the popular radio shock jock was quickly put through and she revealed that she possessed what she believed was the Last Wish Baby's Heart. Meanwhile, word of the whereabouts of the newly discovered baby heart spread fast and a race, of sorts, was on. EMS crews were first on the scene but no sooner had they readied the baby heart for shipment to Cleveland when. . . the lawyers arrived. Motions were made. Injunctions issued. Larger questions loomed. The battle for custody of the Last Wish Baby had begun. The hearing to determine the rightful custodial parents of The Last Wish Baby had barely opened when legal fees threat-ened to exceed even Ms. Welda Mae Forms' recently fatted purse-strings. However, with the baby show still posting record ratings, Ms. Forms saw fit to make full use of her forum.

WELDA: [Angelic.] Poor, poor precious baby. Baby doesn't have a heart. . . know why? Hmmm? [Bitter.] 'Cause some East Coast floozy has got it and won't hand it over unless I give her half a' baby's royalties on the [The baby cries. WELDA looks down.] Yeah, what is it? [A beat to compose herself] Awww, but of course, baby. [WELDA looks up again and com poses herself] Baby wishes there was some nice, pro-bono law firm out there who would take Baby's rightful mother's custody case, and when that was all settled, and a certain individual from a certain so-called Garden-State was financially ruined, that same nice law firm might just be retained to negotiate with those shysters at Glum Entertainment for a more favorable contract. . . idn't that what baby wants? Yes, baby's so sweet. I just hope and pray this won't be baby's last wish.

NARRATOR: But, no sooner had Welda Mae and her people retained new legal counsel than a shocking courtroom revelation hit the newsstands.

NEWSBOY: Read all about it! "Last Wish Baby Show" Hoax! Read all about it!

NARRATOR: Unsealed court documents alleged that the "Last Wish Baby Show" Baby was not the real Last Wish Baby, the baby born without a heart, but rather, a sixteen-year-old unemployed actor with a glandular condition. Americans shuddered. Did this mean the Original Last Wish Baby was dead? Or, Heaven forbid, was there even an original Last Wish Baby in the first place? Con-gressional spouses convened a hearing and demanded answers.

ASSISTANT: Okay, look, it was all my fault. I agreed to pull the baby from the show and I was the one who okayed it when the Forms woman wanted to hire [a stand-in]. But I only went along with it 'cause the doctors insisted on keeping the baby in intensive care. That's the God's-honest truth. There really is a Last Wish Baby, there really is a baby without a heart! I can prove it! I swear to God, I can prove it!

NARRATOR: Needless to say, Americans were skeptical and demanded that proof. Thus, the following night, "The Last "Wish Baby Show" aired live from the Holy Name Hospital's pediatric intensive care unit. Viewers held their breath as the Baby Mom ushered the cameras toward the swinging doors which led to Baby's chamber.

WELDA: Shhhh. Be quiet. This way, please.

ASSISTANT: Watch it, he's got a gun!

NARRATOR: Four shots, each one following its own fatal trajectory, were fired into the torso and cranial cavity of the woman most Americans knew only as the Last Wish Baby Mom. The assailant was identified as Daryl Wayne Trebleu, a'slope-shouldered, itinerant floral designer from nearby Loraine, Ohio, and, purportedly, the man many believed to be the Last Wish Baby Dad. Daryl Wayne Trebleu never uttered a single word in his own defense. Rather, he expressed himself through artfully-designed floral arrangements. Mr. Trebleu's "Not competent to stand trial bouquet" was a lovely and eloquent display of mums, gladiolus, and forty-four magnum shell casings set in a handsome earthenware bowl. Meanwhile, in another court in another state, the judge in the custody hearing for the Last Wish Baby had reached a verdict.

JUDGE: As per the dictates of the honorable State of New Jersey, court of Domestic Relations, I have found as follows: Said infant, here-in-and-ever-after known as, "The Original Last Wish Baby," shall be granted ward status of this court, and thereby ordered to be joined immediately with heart. So be it, so help us God.

NARRATOR: With the Last Wish Baby Show having been abruptly pulled from the airwaves, no effort was made to appeal the Judge's decision. Thus, a medical team of the nation's leading cardio-vascular surgeons were assembled to carry out the court's wishes and, with God's blessing, prolong the baby's life. We take you now live, directly to the Hoppscotch Medical Center in Tarmack, New Jersey.

SURGEON: The operation to implant the baby heart into the Last Wish Baby was both... a success and... a failure. The heart was successfully sutured and continues to pump vigorously. Unfortunately, the baby, for reasons we do not fully understand, has ceased all other life sustaining functions and. . . appears to be in a rapid state of. . . decay.

NARRATOR: There was no denying it. The Original Last Wish Baby, the baby born without a heart, was now, and irretrievably, a dead baby, but one with a very healthy heart. And that presented doctors and lawyers with an entirely new set of problems. For one, the baby could not be considered legally dead unless the heart were either stopped or removed. However, if the baby was not legally dead, then removing or stopping the heart would be, in a word, murder. Therefore, despite all appearances to the contrary, the Last Wish Baby was, in the eyes of the law, very much alive. Further, this being a democratic society, it didn't take long for Americans to gaze upon their own dearly departed loved ones and find similar cause to stretch the definition of what constitutes life. . . and death. Suddenly, Americans became embroiled in an entirely new moral debate-when did life end? The question was not at all as simple as it sounded. After all, who in this country can say with any real certainty when life begins?
```

---

## IC-1185: The Phantom Tollbooth

- Title: The Phantom Tollbooth
- Author (byline): Norton Juster
- Work: Not specified
- Publisher: Bullseye Books
- Publication date as stated: Oct 1988
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MILO, GATEMAN, MERCHANT 1, MERCHANT 2, MERCHANT 3, MERCHANT 4, PAGE, KING AZAZ, GUEST 1, GUEST 2, GUEST 3, KING AZAS, THE MAN, TERRIBLE TRIVIUM
- Teaser before the introduction: Yes
- Spoken words (computed): 2648
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

NARRATOR: Milo nodded his head, and they went on, reading from their scrolls. 5 GENTLEMEN: By order of Azaz the Unabridged-- King of Dictionopolis-- Monarch of letters-- Emperor of phrases, sentences, and miscellaneous figures of speech--We offer you the hospitality of our kingdom, Country, Nation, State, Commonwealth, Realm, Empire, Palatinate, Principality"

MILO: Do all those words mean the same thing? 5 GENTLEMEN: Of course. Certainly. Precisely. Exactly. Yes, You see, Dictionopolis is the place where all the words in the world come from. They're grown right here in our orchards. Once a week by royal proclamation the word market is held here in the great square and people come from everywhere to buy the words they need or trade in the words they haven't used. Enjoy yourself in the market,

NARRATOR: Above all the noise and tumult of the crowd could be heard the merchants' voices loudly advertising their products.

MERCHANT 1: "Get your fresh-picked ifs, ands, and buts."

MERCHANT 2: "Hey-yaa, hey-yaa, hey-yaa, nice ripe wheres and whens."

MERCHANT 3: "Juicy, tempting words for sale."

MERCHANT 4: "Step right up, step right up-fancy, best-quality words right here, Step right up-ah, what can I do for you, little boy? How about a nice bagful of pronouns-or maybe you'd like our special assortment of names?"

NARRATOR: Milo had never thought much about words before, but these looked so good that he longed to have some.

MILO: Maybe if I buy some I can learn how to use them,"

NARRATOR: Said Milo eagerly as he began to pick through the words in the stall. Finally he chose three which looked particularly good to him- "quagmire," flabbergast," and "upholstery." He had no idea what they meant, but they looked very grand and elegant.

NARRATOR: And he continued on through the market. [When the five very tall, then gentlemen once again appeared] 5 GENTLEMEN: 'Ah' there you are. here have you been? We've been looking all over for you. The royal banquet is about to begin. Come with us.

NARRATOR: They seemed very agitated and out of breath as Milo walked along with them. 5 GENTLEMEN: Right this way. Follow us. Come along. Step lively. Here we go.

NARRATOR: They shouted, hopping from the wagon and bounding up a broad marble stairway. Everyone seemed quite grumpy about having to wait for lunch, and they were all relieved to see the tardy guests arrive. There was an ear-shattering blast of trumpets, entirely off key, and a page announced to the startled guests:

PAGE: KING AZAZ THE UNABRIDGED.

NARRATOR: The king strode through the door and over to the table and settled his great bulk onto the throne,

KING AZAZ: "Places, everyone. Take your places."

NARRATOR: He was the largest man Milo had ever seen, with a great stomach, large piercing eyes, a gray beard that reached to his waist, and a silver signet ring on the little finger of his left hand. He also wore a small crown and a robe with the letters of the alphabet beautifully embroi-dered all over it.

KING AZAZ: What have we here?

MILO: If you please, my name is Milo. Thank you very much for inviting me to your banquet, and I think your palace is beautiful. 5 GENTLEMEN: Exquisite, Lovely, Handsome, Pretty, Charming,

KING AZAZ: SILENCE, Now, young man, what can you do to entertain us? Sing songs? Tell stories? Compose sonnets? Juggle plates? Do tumbling tricks? Which is it?"

MILO: I can't do any of those things.

KING AZAZ: What an ordinary little boy, Why, my cabinet members can do all sorts of things. The duke here can make mountains out of molehills. The min-ister splits hairs. The count makes hay while the sun shines. The earl leaves no stone unturned. And the undersecretary, hangs by a thread. Can't you do anything at all? . . . Time for the speeches, You first,

MILO: Your Majesty, ladies and gentlemen, I would like to take this opportunity to say that in all the--"

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

NARRATOR: And down the road Milo went. And the crowd waved and cheered wildly, for, while they didn't care at all about anyone arriving, they were always very pleased to see someone go. The shore line was peaceful and flat, and the calm sea bumped it playfully along the sandy beach. In the distance a beautiful island covered with palm trees and flowers beckoned invitingly from the sparkling water.

MILO: Nothing can possibly go wrong now. And there’s plenty of time. It certainly couldn't be a nicer day,

NARRATOR: And as soon as he’d said it he leaped from the car, as if struck by a pin, and sailed all the way to the little island, which now looked completely different. Instead of palms and flowers, there were only rocks and the twisted stumps of long-dead trees. It certainly didn't seem like the same place he had seen from the road.

MILO: Pardon me,

NARRATOR: Said Milo to the first man who happened by;

MILO: Can you tell me where I am?"

THE MAN: Pardon me, can you tell me who I am?”

NARRATOR: The man was dressed in a shaggy tweed jacket and knickers with long woolen stockings and a cap that had a peak both front and back, and he seemed as confused as he could be.

MILO: You must know who you are,

THE MAN: You must know where you are, To be sure, you're on the Island of Conclusions. Make yourself at home. You're apt to be here for some time."

MILO: But how did I get here?

THE MAN: You jumped, of course. That's the way most everyone gets here. It's really quite simple: every time you decide something without having a good reason, you jump to Conclusions whether you like it or not. It's such an easy trip to make that I've been here hundreds of times.

MILO: But this is such an unpleasant-looking place.

THE MAN: Yes, that's true, it does look much better from a distance.

NARRATOR: As he spoke, at least eight or nine more people sailed onto the island from every direction possible.

MILO: Well, I'm going to jump right back,"

NARRATOR: Milo took two or three practice bends, leaped as far as he could, and landed in a heap two feet away.

THE MAN: That won't do at all. You can never jump away from Conclusions. Getting back is not so easy. That's why we're so terribly crowded here. Oh no. The only way back is to swim, and that's a very long and a very hard way.

MILO: I don't like to get wet,

THE MAN: N either do they, That's what keeps them here. But 1 wouldn't worry too much about it, for you can swim all day in the Sea of Knowledge and still come out completely dry. Most people do.

NARRATOR: Milo decided to swim, He swam and swam and swam for what seemed like hours. At last he reached the shore, thoroughly exhausted and completely soaked.

MILO: From now on I'm going to have a very good reason before I make up my mind about anything. You can lose too much time jumping to Conclusions,

NARRATOR: The car was just where Milo’d left it, and in a moment he was on his way again as the road turned away from the sea and began its long climb into the mountains. Just ahead, stood a very elegant-looking gentleman. He was beautifully dressed in a dark suit with a well-pressed shirt and tie. But his expression was somewhat blank. In fact, it was completely blank, for he had neither eyes, nor mouth.

TERRIBLE TRIVIUM: Hello, little boy, I wonder if you could spare me a little of your time and help with a few small jobs?

MILO: Yes, indeed.

NARRATOR: Said Milo, who wondered for just a moment how it was possible for someone so agreeable to have a face with no features at all.

TERRIBLE TRIVIUM: Splendid, I would like to move this pile from here to there, but I'm afraid that all I have are these tiny tweezers.

NARRATOR: And he gave them to Milo, who immediately began transporting one grain at a time. The very pleasant man continued to stare vacantly while Milo, worked hour after hour after hour after hour after hour after hour--

MILO: Pardon me, but it's going to take eight hundred and thirty-seven years to do this job. It hardly seems worthwhile,.

TERRIBLE TRIVIUM: WORTHWHILE! My young friend, what could be more important than doing unimportant things? If you stop to do enough of them, you'll never get to where you're going. (villainous laugh). I am the Terrible Trivium, demon of petty tasks and worthless jobs, ogre of wasted effort, and monster of habit." (Milo begins to back away slowly).

TERRIBLE TRIVIUM: Don't try to leave, for there's so very much to do, and you still have over eight hundred years to go on the first job.

MILO: But why do only unimportant things?"

NARRATOR: Asked Milo, who suddenly remembered how much time he spent each day doing them.

TERRIBLE TRIVIUM: Think of all the trouble it saves. If you only do the easy and useless jobs, you'll never have to worry about the important ones which are so difficult, You just won't have the time. For there's always something to do to keep you from what you really should be doing . . . . RUN! RUN!"

NARRATOR: And as he ran, Milo suddenly remembered his home. He wanted very much to go back, He clapped his hands and the little car appeared, polished like new. Milo got in and with one last look, started down the road. In a few minutes he reached the end of his journey deposited his coin and drove through. And almost before realizing it, he was sitting in the middle of his own room again. But where the toolbooth had been, there was not nothing at all. He searched frantically throughout the apartment, but it had vanished just as mysteriously as it had come and in its place was another bright-blue envelope, which was addressed simply:

MILO: "FOR MILO, WHO NOW KNOWS THE WAY."

NARRATOR: He opened it quickly and read:

MILO: Dear Milo, You have now completed your trip, courtesy of the Phantom Tollbooth. We trust that everything has been satisfactory, and hope you understand why we had to come and collect it. You see, there are so many other boys and girls waiting to use it, too. It's true that there are many lands you've still to visit and wonderful things to see (that no one has yet imagined), but we're quite sure that if you really want to, you'll find a way to reach them all by yourself.

NARRATOR: And, in the very room in which he sat, there were books that could take you anywhere, and things to invent, and make, and build, and break, and all the puzzle and excitement of everything he didn't know-music to play, songs to sing, and worlds to imagine and then someday make real. His thoughts darted eagerly about as everything looked new-and worth trying.

MILO: Well, I would like to make another trip,but I really don't know when I'll have the time. There's just so much to do right here.
```

---

## IC-1186: The Plane Truth

- Title: The Plane Truth
- Author (byline): Ellen DeGeneres
- Work: Sand in My Bra and Other Misadventures, Pgs 28-34
- Publisher: Traveler's Tale
- Publication date as stated: March 2003
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, FLIGHT ATTENDANT, INVESTIGATOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1181
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ellen DeGeneres
Book: Sand in My Bra and Other Misadventures, Pgs 28-34
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

WOMAN IN 27-B (also a nun): Excuse me, where is seat 27-B?

NARRATOR: I mean, really. But I see now that I overreacted when I screamed at her, “Well, moron you walk in the only direction you can, and it’s the 27th row seat B – next to seat A. All righty?!” That sort of response is probably one of the many reasons why I’m not a flight attendant. It was only when the woman (27-B) turned around to look at me that I saw she was a nun. I guess that sort of hat-like thing she wore on her head should have given me a clue. (beat) I tried to apologize by smiling and giving her a playful punch on the arm to let her know I was joking. Well, either my playful punch carried more of a wallop than I intended or her advanced years made her frailer than she appeared, but the nun shouted out,

WOMAN IN 27-B (also a nun): Owww! (rubbing her arm in pain . . . she rolls up her sleeve)

NARRATOR: . . . you know, that bruise could easily have been there before I hit her. (beat) My good friend Jasmine told me that a good way to combat fear is to chant. So all the way to my seat I was chanting, “I’m going to die, I’m going to die, oh sweet Lord, I’m going to die.” It didn’t work. If anything, I was more petrified when I got to my seat (27-A). Even seeing the familiar face of the nun in 27-B (who seemed to flinch when she saw me) didn’t call me down.

So here I am, sitting in my seat. (taking calming breaths, then reacts violently to a sound) ARGHHH! What was that? We’re going to crash!!! Oh, I wish I hadn’t shouted that out loud. It was just the beverage cart. (to seatmate) “Pardon me, Sister, I am sorry, I . . . . I was frightened. Pray for me.” Now she’s going to turn on that little air thing above her. Maybe I’m paranoid, but I think it takes power away from the plane somehow. “Sister, don’t use that, that’s . . . . Dang! Shut if off! Shut it off!” (beat) The nun just left to find a different seat. Some people are so touchy. I’m sure she didn’t learn that little hand gesture in her convent, either.

I’ve got to relax somehow. Why didn’t I think of this sooner? I’ll recline my seat. Oh, that makes all the difference. That ¾ of an inch between upright and reclined is the difference between agony and ecstasy. I never thought ¾ of an inch could mean so much. When I get home, I’m going to put some gizmo in my chairs so that they go back ¾ of an inch, too. I’d better not get too comfortable in my ¾-of-an-inch recline because toward the end of the flight, the flight attendant is going to say,

FLIGHT ATTENDANT: You’re going to have to put your seat in the upright position for landing.

NARRATOR: They’re so adamant about that every single time, like that’s gonna make a difference. Because if we crash, the investigators are going to say,

INVESTIGATOR: Oh, that’s a shame, her seat was recline ¾ of an inch. When will they learn? What was that – 30,000 feet? She could have made that. Sheesh. If only she’d been upright.

NARRATOR: Being reclined isn’t working. I’m still freaking out. I know what I need. “Oh, flight attendant. Oh ma’am.” (to audience) You have to talk nice to the flight attendants because they all have this attitude. And they can afford to have the attitude, because they have the power – they have the peanuts. They have these six peanuts that we need. Six peanuts. Somebody could offer that to you on the street, and you’d say, “I don’t want that – get that away from me. Six peanuts? No- oh.” Somehow, they’ve done research. They know that the higher we go, the more we need nuts. And we go crazy if we don’t get them. (to Flight Attendant) Miss, I didn’t get my, uh - - my peanuts. And I’d really appreciate it if you game me some. (stuffing peanuts one at a time in her mouth) They’re good, aren’t they? I’ve never been able to get them on the ground either. At least not ones this good! (licking the salt from her fingers)

(panicked) What was that! We’re going to crash! Oops, false alarm. It’s just the food card coming down the aisle. We do get excited about it, don’t we? “Oh, here comes the cart, put down the tray! La la la la. Put down your tray! They’re starting on the other side first. Hurry! Hurry! Those people over there – they’re eating. Those people are eating.”

Any kind of meat that you get – chicken, steak, anything – has grill marks on each side, like somehow we’ll actually believe there’s an open-flame grill in the front of the plane. And salads are always two pieces of dead lettuce and salad dressing that comes in that astronaut package. (package explodes as she tries to open it) As soon as you open it, it’s on your neighbor’s lap. “Could I just dip my lettuce, ma’am? Hm, that’s a lovely skirt. What is that, silk?” But you know, should that happen, club soda’s gonna get that stain our immediately. That’s the answer to anything you ask up there, I don’t know if you’ve noticed that.

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

## IC-1187: Playwriting 101: The Rooftop Lesson

- Title: Playwriting 101: The Rooftop Lesson
- Author (byline): Rich Orloff
- Work: Take Ten II
- Publisher: Vintage Books
- Publication date as stated: Nov 2003
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: JUMPER, GOOD SAMARITAN, TEACHER
- Teaser before the introduction: Yes
- Spoken words (computed): 887
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rich Orloff
Book: Take Ten II
ISBN: 978-1400032174
Publisher: Vintage Books
Date (Month/Year): Nov 2003
```

### Introduction (context only: never use it for content warnings)

```text
Cliché – A saying, image or idea which has been used so much that it should terribly uncreative. Using cliché’s is considered BAD writing because they make it sound like you didn’t put any thought into your words. Satire – The use of humor, exaggeration or ridicule to expose and criticize people’s stupidity. Politicians and, in this case, playwrights are easy targets – especially when they’re acting self-righteous! In Playwriting 101: The Rooftop Lesson, Rich Orloff masterfully combines Cliché and Satire to create something . . . something . . . . Something that will make you want to jump off a roof! Playwriting 101: The Rooftop Lesson by Rich Orloff.
```

### Performance text (classify this)

```text
(Pg 269-280) (THE JUMPER is on the ledge of the roof and is about to jump.)

JUMPER: I'm going to jump, and nobody can stop me! (THE GOOD SAMARITAN enters quickly.)

GOOD SAMARITAN: Don't!!!!! (THE TEACHER enters, points a clicker at the others and clicks, freezing the action.)

TEACHER: (addressing the audience) A typical dramatic scenario: Two people in conflict-at least one in deep inner conflict with high stakes, suspense, and affordable cast size. How will this situation play out? That depends, of course, on the level of craft and creativity in that remarkable art form known as playwriting. Let's rewind from the start and see what happens. (THE TEACHER clicks, and THE JUMPER and GOOD SAMARITAN return to their places quickly)

JUMPER: I'm going to jump, and nobody can stop me!

GOOD SAMARITAN: Don't!!!!!

JUMPER: Okay. (THE TEACHER clicks to freeze the action.)

TEACHER: Not very satisfying, is it? Where's the suspense? Where's the tension? And what audience member will want to pay today's ticket prices for a play whose conflict resolves in forty-five seconds? But most importantly, where can you go from here? (THE TEACHER clicks to unfreeze)

GOOD SAMARITAN: Gee, you could've hurt yourself.

JUMPER: Gosh, you're right. (THE TEACHER clicks to freeze the action.)

TEACHER: Without intense oppositional desires, more commonly known as "conflict," there is no play. When Nora leaves in A Doll's House, nobody wants her husband to reply (upbeat) "Call when you get work!" So let's start this scene over maintaining conflict. (THE TEACHER clicks. THE JUMPER and GOOD SAMARITAN rewind to their initial places.)

JUMPER: I'm going to jump, and nobody can stop me!

GOOD SAMARITAN: Don't!!!!!

JUMPER: Why not?!!! (THE TEACHER clicks.)

TEACHER: Oooo, you can just feel the suspense rising now, can't you? (THE TEACHER clicks again.)

GOOD SAMARITAN: Because suicide is a sin! (THE TEACHER clicks.)

TEACHER: Big deal. Theatre is written by sinners about sinners for sinners. Nobody goes to Othello to hear, "Iago, you're so naughty!" Always let the audience form their own judgments. Now let's try a different tack. (Clicks.)

JUMPER: Why not?!

GOOD SAMARITAN: Because life is worth living.

JUMPER: Mine isn't! (THE TEACHER clicks.)

TEACHER: Excellent. We don't just have a plot anymore, we have a theme. Theme, the difference between entertainment and art. No theme, add a car chase and sell it to the movies. But with theme, you have the potential to create something meaningful, something memorable. (THE TEACHER clicks again to resume.)

GOOD SAMARITAN: Because life is worth living.

JUMPER: Mine isn't!

GOOD SAMARITAN: Are you sure?

JUMPER: Yes, I'm sure. I'm broke, I have no friends, and I see no reason to continue.

GOOD SAMARITAN: Look, so you're broke and friendless. All experiences are transient. Detach, as the Buddha once did. (THE TEACHER clicks.)

TEACHER: Of all the world's great religions, Buddhism is the least entertaining. Let's try again. (THE TEACHER clicks again.)

GOOD SAMARITAN: So you're broke and you're friendless. Why not try Prozac?

(THE TEACHER clicks.)

TEACHER: The popularity and effectiveness of modern antidepressants is one of the great challenges of contemporary dramaturgy. We no more want Willy Loman to solve his problems with Prozac than we want Stanley and Stella Kowalski to get air-conditioning. (THE TEACHER clicks again.)

GOOD SAMARITAN: Let me help you.

JUMPER: It's too late. I haven't told you the worst. You see, until a few weeks ago, I was in love. I was involved with two of the most wonderful gals in the world. One was sexy, rich, generous and caring. The other was streetwise, daring and even sexier. Between the two of them, I had everything. Then they found out about each other, and they both dumped me. Not just one, but both. (THE TEACHER clicks.)

TEACHER: Excellent playwriting. Here's a heartbreaking situation with which we can all identify. Maybe not in the specifics, but in the universal experience of rejection. (THE TEACHER clicks again.)

GOOD SAMARITAN: At least you've had two exciting affairs. I haven't *had any relationships* in a year.

JUMPER: So what are you telling me? That life can get worse? That's supposed to get me off this ledge?

GOOD SAMARITAN: Hey, I'm just trying to help!

JUMPER: Well, you're doing a lousy job.

GOOD SAMARITAN: At least I've got some money in the bank!

JUMPER: You've also got rocks in your head! (THE TEACHER clicks.)

TEACHER: A common beginner's mistake. Two characters in hostile disagreement isn't conflict, it's just bickering. We don't go to the theatre to hear petty, puerile antagonism; that's why we have families. Let's hope this goes somewhere interesting. (THE TEACHER clicks again.)

JUMPER: You've only got money in the bank because you're cheap.

GOOD SAMARITAN: I am not.

JUMPER: Well, you certainly dress like you are.

TEACHER: Now this is really degenerating. (THE TEACHER clicks, but the action continues.) Now stop it ... Stop it! ... Stop itl! (Etc.)

JUMPER: (Shouting above THE TEACHERS "Stop it'ts, which they ignore) Loser!

GOOD SAMARITAN: Cretin!

JUMPER: Cheapskate!

GOOD SAMARITAN: Imbecile!

TEACHER: (clicking in vain) Stop it!!!! (THE GOOD SAMARITAN takes out a clicker and freezes THE TEACHER.)

GOOD SAMARITAN: Notice how organically the teacher's frustration has increased. What began as a minor irritation became unbearable when the human desire to control was thwarted. (THE GOOD SAMARITAN clicks)

TEACHER: What are you doing?! I hold the clicker around here. How dare- (THE GOOD SAMARITAN clicks. THE TEACHER freezes.)

GOOD SAMARITAN: See how frustration becomes "anger"? Although the real life stakes are minor, the character's emotional investment is intense. That's good playwriting. (THE GOOD SAMARITAN clicks again.)

TEACHER: Stop that. What do you think this is, a Pirandello play?

GOOD SAMARITAN: Well, how do you think we feel? We can't say more than two lines without being interrupted by your self-important pronouncements. How'd you like it if I did that to you?

TEACHER: You have no dra- (THE GOOD SAMARITAN clicks and stops /starts THE TEACHER during the following:) matically vi-able rea-son to inter-rupt me. Damn it, will you get back in the play?

GOOD SAMARITAN: No, and you can't make me! (THE GOOD SAMARITAN clicks at THE TEACHER, who dodges the clicker.)

TEACHER: Aha, missed … You superficial stereotype! (THE TEACHER clicks at THE GOOD SAMARITAN and vice versa during the following, both successfully dodging the other.)

GOOD SAMARITAN: Control freak!

TEACHER: Cliche!

GOOD SAMARITAN: Semi-intellectual!

TEACHER: First draft mistake! (THE JUMPER, who has been watching this, takes out a gun and shoots it into the air.)

JUMPER: Hey!!! I'm the one with the problem. This play's supposed to be about me.

TEACHER: (to THE GOOD SAMARITAN) Damn it, get back into the play!

GOOD SAMARITAN: Don't tell me what to do. Ever since I was a kid, everyone's told me how I'm supposed to behave. When I was five, my mom sent me to my room (THE TEACHER starts clicking manically at THE GOOD SAMARITAN.) four thousand times because I wouldn't be the kid she wanted me-

TEACHER: This monologue is not justified!

GOOD SAMARITAN: It's my life!

TEACHER: It's bad drama!

GOOD SAMARITAN: I'll show you bad drama! (THE GOOD SAMARITAN and THE TEACHER begin to fight.) (THE JUMPER tries to break up the fight.)

JUMPER: Come on, guys, cool it! (The three of them are in a tight cluster. We hear a gunshot. THE TEACHER pulls away. There's blood on THE TEACHER's chest.)

TEACHER: I just got tenure. (THE TEACHER collapses and dies dramatically)

GOOD SAMARITAN: Oh my God. (THE GOOD SAMARITAN looks at THE JUMPER.) How horrible. Is that good playwriting or bad playwriting?

JUMPER: I, I don't know. It just happened. (THE GOOD SAMARITAN and THE JUMPER look at THE TEACHER...(simultaneously) Hmmmmmmm.

End of Play
```

---

## IC-1188: Pluto Gets the Call

- Title: Pluto Gets the Call
- Author (byline): Adam Rex
- Work: Not specified
- Publisher: Beach Lane Books
- Publication date as stated: Nov 2019
- Event as filed: Humorous Interpretation
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

But then one day in 2006, Pluto gets a call from some scientists on Earth, and they have some bad news — he/she actually isn’t a planet anymore. The International Astronomical Union (or IAU) had redefined the word “planet.” And Pluto no longer fits the bill. As you can imagine, Pluto isn’t too happy with this news, so he sets out on a journey through the solar system to find out why.

Pluto Gets the Call by Adam Rex
```

### Performance text (classify this)

```text
PLUTO: Ooh, someone’s going to call? Are they calling to invoice me to a party? I LOVE parties! (waving broadly) Hi . . . Hi! . . . Over here! Behind the ice and all those other guys. It’s me, Pluto! The ninth planet! It’s great to see you! We don’t get a lot of visitors out here in the Kuiper Belt. It’s this huge ring around the Sun that’s full of frozen stuff. It’s kind of my neighborhood, no big deal. (beat) So, not to brag, but I’m mostly made of nitrogen.

STAR: Ooh, nitrogen! (swoons)

PLUTO: I’m almost as big as Earth’s moon. I’m really cold, and I have a big heart on my belly ‘cause I love being a planet. Hold on a second, that’s my phone. (on the phone) You got Pluto! Oh, what a coincidence – I was just talking to someone from Earth. (to audience) Sorry, I should take this. (back on the phone) Uh-huh . . . Uh-huh . . What?! What do you mean I’m not a planet anymore? Why am I not a planet anymore. I . . . Uh . . . okay. Thank you for calling. (to audience) That was just some scientists from Earth. They say I’m not a planet anymore, no biggie. (getting angry) They asked if I’d like to be known as the solar system’s largest ice dwarf, and I was like, “How’d you like to known as Earth’s . . . meanest . . . jerks, huh? Huh?! (sadness set in) I didn’t really say that. I’m sorry, you were probably hoping to hang out with a real planet. Let me show you around. (travels to the closest neighbor) Psst, Neptune! Are you awake?

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

PLUTO: I don’t have to take this! I am OUT OF HERE! (travels closer to the SUN, obviously warm, sweaty) Um. So, there’s Mars. She’s smaller than Earth, and she has a lot of water ice.

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

## IC-1189: Politically Correct The Princess and the Pea

- Title: Politically Correct The Princess and the Pea
- Author (byline): James Finn Garner
- Work: Once Upon a More Enlightened Time
- Publisher: MacMillan Publishing Company
- Publication date as stated: May 1995
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, PRINCE, QUEEN, PRINCESS
- Teaser before the introduction: Yes
- Spoken words (computed): 1200
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
NARRATOR: In a kingdom over the hills and far away, there lived a young prince who was very full of himself. He was healthy, relatively handsome, and had had more than his fair share of happiness and comfort growing up. Yet he felt that he deserved something more. It was not enough for him to have been born into a life of parasitical leisure and to keep the masses firmly under the heel of his calfskin boots. He was also determined to perpetuate this undemocratic tyranny by marrying only a real, authentic, card-carrying princess.

NARRATOR: His mother, the queen, encouraged her son’s obsession, despite the obvious risks of hemophiliac or microcephalic grandchildren. Many years earlier, after a period of inadequate wellness, his father the king had achieved corporal terminality. This lack of a strong male presence gnawed at the prince on a subconscious level, and no amount of weekend retreats and male bonding with other young dukes and barons could relieve this anxiety. His mother, for her own codependent and Oedipal reasons, did not bother to change or correct his selfish notions or unattainable perfection in a spousal lifemate.

In his quest for the perfect partner, the prince travelled far and wide, looking for someone to enslave in matrimony. Astride his trusty equine colleague, he went from kingdom to queendom and from dukedom to duchessdom, asking for names and phone numbers. Heavily or lightly pigmented, vertically or horizontally challenged, cosmetically attractive or differently visaged – he cared not a whit. His only criterion was the royal authenticity of a wommon who could share his regal delusions of privilege and persunal worth.

One rainy night, after a long journey to many far-off bioregions, the prince nourished himself with a bowl of lentil-curry stew and confided his fears to his mother:

PRINCE: I don’t think I’ll ever find a genuine princess with whom to share my life, Mummy.

QUEEN: Well, Son, don’t forget the many benefits of the single life. Don’t let society and the church pressure you into a lifestyle for which you might not be suited.

PRINCE: Perhaps I should widen my scope a bit.

QUEEN: What? And throw out your standards?

PRINCE: No, Mummy, perhaps I have fallen into a trap of the orthodox heterosexualist majority. Maybe there’s a fine young prince out there for me. It’s at least worth a try.

NARRATOR: Before his mother could answer, there was a knock on the castle door. The servants pulled open the heavy portal, and out of the rain stepped a young wommon, who was moisture-enhanced from head to foot. She was certainly attractive to the eye, if you’re the type of shallow person who attached value to appearances. Luckily for our story, the prince was not one of those types. He had one standard, and only one standard, classist though it might have been. Imagine the prince’s surprise when the visitor blurted out,

PRINCESS: A princess shouldn’t be out in weather like this!

NARRATOR: Well now, this was a revelation straight from the equine animal companion’s mouth! The prine was struck orally inoperative for a moment, then invited the dryness-challenged visitor to enjoy their hospitality in the castle overnight. While this was certainly a joyous development for the prince, his mother felt very threatened that someone was taking her son away from her. But rather than acknowledging the validity of her feelings and airing them in a constructive way, the queen decided on a ruse to test the visitor’s claim. She sneaked up to the bedchambers and found the room where the persun of saturation would be sleeping. She tore off all the bedding from the frame and placed one single pea on the bed slats. Then she placed 10 futons on top of the pea, and on top of that, 10 eiderdown quilts.

QUEEN: There. If that drenched wench downstairs is really a princess, she will be refined enough to notice this lump and be unable to sleep.

NARRATOR: The next morning at breakfast, over the royal granola, the queen innocently asked the young wommon how she had slept.

PRINCESS: Abominably. I didn’t get a wink all night. First of all, the bed was piled high with eiderdown quilts. Barbaric! How could I sleep, thinking of the poor naked geese who surrendered their feather for my comfort? Then, as I was removing the extra futons to share them with some of the less fortunate peasants living around the castle, I found a pea placed beneath them all. Shocking, with the state of the world as it is, that someone would waste food like that.

NARRATOR: With these statements, the queen nearly choked on her soy milk. The prince, who had learned of his mother’s scheme to screen out a princess, was so excited he couldn’t keep silent any longer.

PRINCE: So you really are a princess!

PRINCESS: Last night I was, yes. Last night I was a princess; this morning I’m an ancient Viking warrior. Oh, you sillies – I’m channeling! I have over a dozen past persunalities that periodically inhabit my body – everyone from Charlemagne’s mistress to Aesop’s brother-in-law. And Cleopatra. But then, everyone’s been Cleopatra at some time or other. Let me tell you, it makes for some interesting conversation at parties! It’s all pretty exciting for an economically disadvantaged spoonmaker’s daughter who grew up on the wrong side of the drainage ditch.”

NARRATOR: These revelations made the queen very angry, but the prince was intrigued.

PRINCE: So, when do you think you will be channeling a princess again?

PRINCESS: A week from Tuesday, mid-morning until early evening. I am very punctual with my past lives.

PRINCE: Then on that Tuesday afternoon I will ask you to be my wife and castle-mate, and you can rule by my side as an equal partner in every way.

PRINCESS: (considering a moment) I would gladly accept, if not for the fact that this morning, as I have said, I am a Viking warrior – Liefdahl by name, son of Ulfdahl – and I have a strong notion to lay siege to your castle just after breakfast.

QUEEN: How rude! We give her lodging in a storm and breakfast the next morning, and she swaps persunalities on us and calmly talks about laying siege to us, without so much as a ‘by your leave’!

PRINCE: Mother, please. Now how long are you generally a Viking warrior?

PRINCESS: Oh, no longer than 45 minutes. After that, I’m usually the hermit St. Giles, living in a hovel and renouncing all worldly possessions.

PRINCE: And that would include . . . ?

PRINCESS: That would include (smiling) renouncing any and all worldly kingdoms conquered by my other spiritual co-habitators.

NARRATOR: So, as is often the case, timing was crucial to a happy ending to our story. The “princess” and the prince were married the second Tuesday following, in accordance with her metaphysical timetable, and they had a very happy honeymoon, especially during certain transformation. Every time she became Liefdal, son of Ulfdahl, she would conquer the prince and his castle, and every time she became St. Giles, she would give it right back. Channeling past lives and historical persunalities became de rigueur in court from that day forward, and the queen, the prince, and the channeler lived a very happy life together, never quite knowing who would turn up at breakfast.
```

---

## IC-1190: The Princess and the Pea

- Title: The Princess and the Pea
- Author (byline): AJ Jacobs
- Work: Fractured Fairy Tales
- Publisher: Bantam Books, Inc.
- Publication date as stated: Nov 1997
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, PRIME MINISTER, KING, CHARLIE, CLYDE, NARRTOR, MAIDEN
- Teaser before the introduction: No
- Spoken words (computed): 800
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
NARRATOR: It seems that once upon a time there was a kingdom without a princess, and this concerned the king and his ministers greatly.

PRIME MINISTER: (showing and tapping a chart) We are facing a severe heiress deficit We must immediately increase the number of young female royal individuals in the palace vicinity.

KING: (sighing) You mean we've got to find a princess.

PRIME MINISTER: That's what I said.

NARRATOR: This wasn't an impossible task. The king once did have a princess, but she had been lost since childhood. The king and his ministers simply had to figure out how to track her down. But just as they got started thinking, they were interrupted by the court jester, Million Laughs Charlie.

CHARLIE: Thank you, thank you. Good to be here, folks! (shaking rattle) You know, the other day, I walked into this bar, and there was this Irishman and this rabbi-

KING: Please, we're doing some business here. (to ministers) How about if we offer a million gold crickles to the princess when she shows up.

CHARLIE: A million gold crickles! I'd love to help on this project. Do you remember what she looked like?

KING: No.

CHARLIE: Good! I mean, that's too bad. (rubbing his hands)

KING: She was just a baby when she left. But I'll know her by the way she passes this test I have in mind.

NARRATOR: But Million Laughs Charlie wasn't listening anymore. He wasn't even there. Charlie had run home, called up his date for the night-a lovely maiden who lived next door-canceled on her, and got straight to work on his scheme. He recruited his friend Clyde, a rather big man with a rather small brain, to help. And before Clyde knew what had happened, he had on a blond wig, a lot of lipstick, and was on the way to the palace to meet the king.

CLYDE: (whining) I don't want to be no princess! These high heels are killin' me.

CHARLIE: Shush. Hey, King. I'd like to introduce you to your princess!

KING: Hmm, she's got more of a five o'clock shadow than I remember my princess having. But if she passes the test, then I'll know she's the one.

NARRATOR: With that, the king led the make-believe princess to a tall pile of mattresses. Under the bottom mattress, he explained, there was a small pea. If she was a real princess, she would be so refined, so sensitive, that even a tiny lump like that wouldn't let her sleep. The make-believe princess climbed to the top of the pile and lay down as Charlie, the king, and his ministers waited at the bottom. In the morning, the king and his court climbed to the top and, sure enough, the make-believe princess was snoring away blissfully.

PRIME MINISTER: Ah-ha! This individual lacks the qualities necessary to be a member of the royal family.

KING: (sighing) He means this ain't no princess.

NARRATOR: Charlie and Clyde found themselves escorted out of the palace, helped along by a swift kick or two on the bottom from the palace guards.

CHARLIE: (shouting) Now you've done it, you hussy!

NARRTOR: But Clyde didn't get off that easily. Over the next few days, Charlie dressed his friend up in a red wig, a brown wig, and a browner wig and sent him off to the palace to pretend to be another girl. Hoping to keep him up, he would feed Clyde coffee and tell him scary tales about monsters and politicians. But each time, Clyde would sleep soundly through the night. And in the morning, he would be forced to leave the palace, rubbing his rear. After several days of this, the two dejected men went back to Charlie's house to regroup. There, Charlie's neighbor was out in the yard, washing her carriage.

CHARLIE: Hey, honey, my business deal fell through. Got some time on my hands. What say we go out and have a bite to eat,

MAIDEN: Sorry, Charlie. I'm exhausted. I didn't get a wink last night. I think there was a pea under my mattress."

CHARLIE: Did you try maybe reading anything by John Updike? (Beat) Wait a sec. Didn't sleep a wink'?

NARRATOR: Yes, Charlie had figured it out. This really was a princess. The real thing. The girl that would get the million gold crickles and all the titles of her realm. Before you could say "greedy no-goodnik," Charlie had taken the girl to meet the king.

KING: Oh, darling (hugging his daughter). Here's a million gold crickles-minus thirty percent for taxes-plus your choice of any man in the kingdom.

MAIDEN: Wow! Any man in the kingdom? (smiles and looks at Clyde) Oh, Clyde. Will you be mine?

CLYDE: For keeps!

NARRATOR: That's the story. The king had his daughter, the princess had her gold, and Clyde had the princess and they all lived happily ever after. Ooops. Almost all lived happily ever after. Poor Million Laughs Charlie spent the rest of his days unsuccessfully trying to sell unauthorized fairy tales of the king and his court.
```

---

## IC-1191: Psssst! It’s Me. . . The Bogeyman

- Title: Psssst! It’s Me. . . The Bogeyman
- Author (byline): Barbara Park
- Work: Not specified
- Publisher: Atheneum
- Publication date as stated: Sept 1998
- Event as filed: Humorous Interpretation
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

I’m not “EVIL,” Alvin. In fact, I’m not that different from you. I gobble up chicken fingers and I gulp down Gummi Bears. And after eating, I almost always floss my tooth before slipping under someone’s bed to catch a few zzzzzz’s. Which is exactly what I’m about to do now. All this belly-achin’ has got me beat. Besides, I’m off-duty, and my cloak is at the clearners. So, start spreadin’ the word that this headline

(shakes newspaper) is hogwash.

Oh, yeah, and kindly keep your smelly sweatsocks off the floor. I’m allergic, okay? Just one wiff of those things and I’m outa here, Dude. I start gaspin’ and wheezin’ and chokin’ and sneezin’. Plus I break out in itchy, splotchy blue blotchies. So, like I said, just keep them – Whoa, Whoa, WHOA!

Hold on a second, Sherlock. You’re not takin off those socks now, are you? You are? But . . . but I thought we were pals. Hey! (gasp) Stop waving them around! (wheeze) What’s gotten into you anyway? (sneeze) Wait! Knock it off! (itching, scratching, sneezing) Not all those!! Ugh! Bluck!!! Ick! AAAUUUUUGGGGHHH! I’m gone! (He flees in a panic to a bedroom down the hall)

(Still coughing) Pssssssst! Yo! Down here . . . under the bed. It’s me, the Bogeyman.
```

---

## IC-1192: Puberty: The Game Show

- Title: Puberty: The Game Show
- Author (byline): Greg Atkins
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Sept 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: BABS, ALAN, ELANA, KAREN, TOMMY, KAREN AND TOMMY, MOTHER, DATE, PIMPLES, RAPPER, VOICE OVER
- Teaser before the introduction: Yes
- Spoken words (computed): 2000
- Already set (do not supply): none

### Source block (context only)

```text
Author: Greg Atkins
ISBN: 978-0874400649
Publisher: Samuel French, Inc.
Date (Month/Year): Sept 1998
Cutting compliments of
Heather Whitney, Norfolk Public Schools, NE
```

### Introduction (context only: never use it for content warnings)

```text
Everyone’s been through the change! The only thing different about this sudden morph into adulthood is that it’s done on a gameshow. Join your hosts and the contestants on a wild ride in Puberty: The Game Show by Greg Atkins.
```

### Performance text (classify this)

```text
BABS: [And we’re on in five, four, three, two, and…] (Pg 7-8) Welcome to . . . Puberty! (applause) The show that leads you through the most exciting, frustrating, exhilarating, frightening, and embarrassing time of your life! (applause) Puberty! And now, the hosts of Puberty! Alan Beckman and Elana King! (Alan and Elana walk out and take their places – applause)

ALAN: Thank you, thank you everyone! Well, Elana, you look very nice today.

ELANA: So do you, Alan.

ALAN: Oh, this? It was a hand-me-down from my older brother. (laughing) I’m used to it. I was thirteen before I got my own toothbrush.

ELANA: (laughing) Oh, gross.

ALAN: And how about you? I understand you have been very busy.

ELANA: Yes, I’ve just released my very own brand of perfume.

ALAN: Congratulations, Elana! (He claps) What is the name of this wonderful fragrance?

ELANA: Elana Wanna. It tells the boys, “Here I am!”

ALAN: That sounds great! Are you wearing it right now?

ELANA: Yes. (leans forward for Alan to smell)

ALAN: (not pleased with the smell) (chokes) Pungent! Well, I guess we had better get on with it and introduce our first two pre-pubescence contestants.

BABS: Hailing from Portsmouth, New Hampshire, a state famous for producing Bauxite, please welcome Tommy Landry! (Tommy enters to applause) And from Oxnard, California, the vacation playground of migrant farm workers, let’s put our hands together for Karen Stiver! (Karen enters to applause)

ALAN: WELCOME TO... PUBERTY!

ALAN: (Pg 8-14) Alright, but before we begin, let’s find out a little about our contestants. Karen, let’s start with you. I understand you are in the seventh grade.

KAREN: Yes, I am, Alan. I go to Heinekin Middle School. (She turns to the television audience and cheers) Go Weevils! My parents are divorced, I live with my mother and see my father on weekends and I have a dog named Bosco and a little brother I hate.

ALAN: Sounds good.

ELANA: And what about you, Tommy?

TOMMY: I’m Tommy Landry and I go to Our Lady of Perpetual Motion Catholic School in Portsmouth. I’m in the seventh grade and my school just went co-ed this year, which is okay I guess. My parents have been married for twenty years and I have an older brother, Kevin, and a younger sister, Patty. I like computer games and baseball and my best friend is Chuck.

(He waves at television audience). Hi, Chuck.

ALAN: It looks like we’ve got two live ones, Elana.

ELANA: It sure looks that way, Alan.

ALAN: Are you ready to get on with Puberty?!

KAREN: Yeah! TOMMY: Let’s do it. (simultaneously)

ALAN: Alright, let’s get you all set up while Elana explains the rules. Elana?

ELANA: Thank you, Alan. After picking a card from Alan, our contestants must move the number of spaces designated on the card. Wherever our contestants land on our Puberty Path they must follow the instructions corresponding with the square they land on. Each square holds something new and different for our contestants. Whether it's Most Embarrassing Moments, Hormone Hijinx, or My Parents Will Kill Me, every square moves you further along the path of Puberty! And remember, each square gives you the opportunity to get Adulthood Points. The more points you get the easier it is to pass through Puberty.

ALAN: Don’t forget to mention the Experience Circle.

ELANA: How could I forget that? In order to score extra Adulthood points, the contestants have the option of entering the Experience Circle where they must actually deal with an incident in their growing up process. If they deal with the Experience well, they get those valuable extra points, if they don’t they could lose everything. It’s a risk, but, hey, what in life isn’t a risk?

ALAN: Confusing? Of course it is, it’s Puberty!

ELANA: Are we ready, Alan?

ALAN: Are you ever ready for Puberty, Elana? Of course not. But if you’re asking if we’re ready to play . . . contestants are you ready to play Puberty?!

KAREN AND TOMMY: YEAH! (Game show music from Babs)

ALAN: Then let’s get started! And since girls seem to begin Puberty before boys, who are we to go against nature? Karen, you go first. Do you choose the green card or the red card?

KAREN: The red card. (She takes the card and moves 3 squares)

ELANA: And you’ve landed on the The Parent Trap. Do you want to go for a three point Question or the six point Experience?

KAREN: I think I’ll take the Question to start out with.

ELANA: Alright, here it is. You are asked to the movies by Tom Child!

KAREN: I am!?! Oh my *gosh*, oh my *gosh*! He’s in the ninth grade and on the basketball team!

ELANA: Your Question is: Do your parents let you go?

KAREN: (A pause) Yes, they have to let me go, I’ll die if they don’t let me go! Yes, yes!

ALAN: (Buzzer from Babs) So sorry, Karen. They say you’re too young to date and anyway the movie was rated NC-17, they’d have never let you in.

KAREN: I hate my parents. I hate them!

ALAN: Of course you do, it’s Puberty! Now on to Tommy. Pick a card.

TOMMY: Red, please, Alan.

ALAN: Red it is. And you move one square.

ELANA: You land on Hormone Hijinks. Would you like the three point Question or the six point Experience?

TOMMY: Hormone Hijinks? I better go with the Question.

ELANA: Alright, it’s a multiple choice and here it is: Your voice is beginning to change and the first time it happens you are: A - Singing in the shower.

B - Talking to the guys after you lost a baseball game. C - Talking to Becky Casey in Math class. Or, D - in front of the entire English class during your oral report?

TOMMY: Ummmmm?

ALAN: You only have fifteen seconds, Tommy.

TOMMY: D. During my oral report?

ELANA: (Ding-ding-ding! - Bell from Babs) That’s right! That’s good for three Puberty points!

ALAN: And back to you, Karen. Red or Green?

KAREN: Green.

ALAN: Move ahead one.

ELANA: And it’s back to The Parent Trap. Experience or Question?

KAREN: I think I’ll go for the Experience.

ALAN: Then let’s go! (he takes her center stage) You know how this works, you get to live the Experience and if the judges feel you have moved ahead in your growing up process, you get the six Puberty points and move into the lead. Got it?

KAREN: Yeah.

ALAN: (moving back) Take it, Elana.

ELANA: Thanks, Alan. Your category is The Parent Trap and your Experience is: Coming Home Late.

KAREN: Oh, no.

MOTHER: (A studio audience member assumes the role of “Mother” walks into the experience circle) Hello. Or should I say, Good morning?

KAREN: Mom, I can explain.

MOTHER: 12:16. 12:16 on a school night? When is your curfew?

KAREN: Mom, look, I -

MOTHER: Answer me! When is your curfew?

KAREN: 9:00 on weeknights, 10:00 on weekends? . . . We didn’t leave the library until 9

MOTHER: So it took you three hours to get home?! (Screams in frustration, then takes a calming breath) Karen, I want to trust you -

KAREN: You can!

MOTHER: But you make it so hard sometimes. This is why I won’t even entertain the thought of you dating! (Pause) So what am I supposed to do?

KAREN: Ground me, I guess.

MOTHER: I guess you’re right! Curfew is now 8:00 - (Karen is about to interrupt) - and you are grounded for two weekends!

KAREN: But . . .

MOTHER: Three weekends.

KAREN: That’s not . . .

MOTHER: Four weekends! Wanna try for five? (Karen fumes silently) Alright, up to bed.

ALAN: (Ding-ding-ding! – Bell from Babs) And there’s the bell! Good for six points! Congratulations!

KAREN: I can’t believe it! Grounded for four weekends?! This sucks!

ELANA: And one extra weekend of restriction for having a potty mouth.

ALAN: You’d think she’d learn, wouldn’t you, Elana?

ELANA: Yes, Alan, you’d think she would. Well, Tommy, here’s your chance to really rack up some points. Step on up.

TOMMY: A red card, please.

ALAN: The red card says… move three spaces!

ELANA: (Pg 19-21) And you’ve landed on Those Magic Moments.

ALAN: Question or Experience?

TOMMY: I’d better go for the points. Experience

ALAN: Then let’s go! (Alan hands Tommy a baseball mitt) [I hope you’re good at baseball.] (Tommy enters the Experience Circle in the middle of a baseball game)

TOMMY: Oh, my *gosh*. Here it comes. I gotta catch it. Don’t panic, it’s just a game. Just the difference between being a social outcast and a hero. (he readies himself to catch a pop fly) Where is it? It’s in the sun! Ah, ah! AHHH!

(catches ball – the bell rings then Tommy drops the ball – The buzzer sounds)

ALAN: Oh, too bad Tommy! No points.

TOMMY: I’m gonna be a social defect. No one on the team will ever talk to me again.

ALAN: Well, we can only imagine the ridicule and embarrassment you are going to have to endure for the rest of your life.

ELANA: Luckily, we can only imagine it, you have to live with it. Now on to Karen.

ALAN: Red or green, Karen?

KAREN: Green, Alan.

ALAN: And it’s a big move -- five spaces!

ELANA: And you land on… oh oh, “Mother finds your diary!” And reads all your complaints about her. Too bad.

KAREN: Stupid diary! Stupid Mom!

ALAN: Too bad about your diary. Get up here, Tommy! Pick a card, buddy.

TOMMY: Red!

ALAN: You move two spaces!

ELANA: And land on first love! Question or Experience?

TOMMY: Well, Elana, I better go for the 6-point Experience.

ELANA: Alright, your category is first love and your Experience is First Kiss.

TOMMY: FIRST KISS?!? Oh, man! This is gonna make me nervous.

ALAN: Head on over to the Experience Circle. (Tommy steps in and a member of the studio audience assumes the role of his date – they are walking up to her front porch at the end of their first date)

TOMMY: (Pg 24) So you liked the movie?

DATE: I told you I liked the movie four times. I liked the movie. Why are you acting so weird?

TOMMY: I guess because it’s our first date. I want everything to be perfect.

DATE: It has been perfect. (each look away from each other, then Date applies Chapstick) Well… here we are. I had a wonderful time tonight.

TOMMY: So did I. (Both lean in for a quick kiss and porch light turns on. Both jump back.)

DATE: It’s okay. It’s just my mom flicking the porch light on and off. It means I have to go in.

TOMMY: Oh, well then, goodnight (he starts to leave)

DATE: (She grabs his arm) Hey, didn’t you forget something? (She pulls him to her and they kiss) (Ding-ding-ding!)

ALAN: And six points for Tommy!

BABS: (beedeeepbobbityboop)

ELANA: [Looks like we’ll have to take a quick break. Here’s] a word from our sponsor. COMMERCIAL BREAK

PIMPLES: (Pg 26-30) (Both actor and actress sing/rap together) We are your pimples, we live upon your face, we are happy pimples, you’ll find us everyplace. We are nasty pimples, you’ll never get rid of us, we are pus-filled pimples that erupt like Vesuvius.

RAPPER: (creates beat for Rappers to follow during next song) Not so fast. (Pimples gasp) What you need is a Zip-Zap Pad, the best friend you ever had. Just wipe it all along your face and pimples leave without a trace. Now that your skin is looking hot, you can go back to eating chocolate. Fries and chips and all things bad. Just thank your handy Zip-Zap Pad.

VOICE OVER: Zip-Zap Pads come in Padettes, Extra Strength pads and full body wraps from AmWay TRANSITION BACK TO THE GAME SHOW

BABS: And we’re back in five, four, get ready, two and… (Babs points to Alan)

ALAN: Well, Elana, we’re almost through Puberty! Boy what an exciting show we’re having today.

ELANA: You’re right, Alan. As the score now stands: it’s Karen with [6] points and Tommy with [9], and it’s Karen’s turn.

ALAN: Right you are. Karen pick a card, if you please.

KAREN: I pick green, Alan.

ALAN: And it’s another five spacer! You land on Unexpected Turn of Events.

ELANA: That also puts you near the end of Puberty! Question or Experience?

KAREN: I’ll take the Experience.

ALAN: If you get this Experience correct, you will take the lead. Your Category is Unexpected Turn of Events and your Experience is: What Do They Really Think? (Karen steps into the circle and pulls Tommy in with her)

TOMMY: Whoa - what’s going on? This isn’t my Experience.

ELANA: Actually, Tommy, this Unexpected Turn of Events is partially YOUR experience.

KAREN: Where are your parents? (Karen’s inner voice) He looked so cute when lost at Puberty.

TOMMY: They’re finishing signing some papers so I can get my prizes. (Tommy’s inner voice) I can’t believe she reached Puberty before I did!

KAREN: These game shows show really give you nice parting gifts. (Karen’s inner voice) I think he’s still upset. I kinda like him.

TOMMY: Yeah. (Tommy’s inner voice) Yeah, you get to go through puberty and I get the home version, plus a year’s supply of zit pads. (to Karen) Well, I gott ago.

KAREN: Don’t you need my phone number? (Karen’s inner voice) I wonder if I should kiss him.

TOMMY: Sure. (Tommy’s inner voice) Oh, man this stuff makes me nervous.

KAREN: It’s J-K-L-M-N-O-P. (Karen’s inner voice) Let’s see if he can figure it out.

TOMMY: 555-6667? (Tommy’s inner voice) Good work, Tommy! (to Karen) Karen . . .

(Tommy leans over and kisses her on the cheek) (Ding-ding-ding!)

ALAN: Six points for Karen! And that final bell tells us we’re out of time! So the score now stands with [nine] points for Tommy and [twelve] points for Karen!

ELANA: Which means, Karen, you’ve made it through Puberty! (Karen screams, giggly excitement)

ALAN: Congratulations, Karen. You are embarking on an exciting ‘next step’ in your life - Young Adulthood. Looking forward to it?

KAREN: (excited) I sure am, Alan. (Tommy looks defeated. During this next section to the end, Tommy pouts and looks angry, Karen waves to audience members and blows kisses at people)

ELANA: Well, Tommy, you’re no doubt a bit disappointed, but don’t worry! We have some lovely parting gifts! Tell us about them, Babs.

BABS: Tommy will receive a case of Zip-Zap Pads, a bottle of Elana Wanna and the home version of Puberty!

ALAN: So this is Alan Beckman -

ELANA: - and Elana King -

ALAN: saying Join us tomorrow

ELANA: - because no one wants to go through Puberty alone!

BABS: (Pg 31) All contestants are under medical supervision while going through Puberty. And don’t forget t o play Video Puberty! By Nintendo. Now you’re playing with Power!
```

---

## IC-1193: Richard

- Title: Richard
- Author (byline): Allie Brosh
- Work: Solutions and Other Problems, Pg 15
- Publisher: Gallery Books
- Publication date as stated: Gallery Books
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MOM, RICHARD, NARRTOR, DAD
- Teaser before the introduction: Yes
- Spoken words (computed): 1326
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

• If you swallow watermelon seeds, an entire watermelon will grow inside you.

• Quicksand is everywhere, and you have to be constantly vigilant for it.

• Sharks are lurking in the deep end of every swimming pool. (beat)

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

A concrete objective never emerged, but the missions became bolder and more frequent. I started bringing things back with me. Richard's things. They seemed valuable, somehow. A nonsensical collection of Richard's possessions slowly accumulated at the back of my toy drawer. This would prove to be my downfall. Long before that, though, my mom noticed that I'd mysteriously disappear sometimes. She wasn't worried yet because she didn't think I knew how to get out of the house, but one day she asked me where I'd been. And I said: "Hanging out with Richard."

"Hanging out" was a misnomer—Richard had been hanging out by himself and I had been standing in his hallway just out of view—but this was concerning news for my parents. They didn't even know that I knew Richard, let alone that we'd been "hanging out." They went over and knocked on Richard's door and asked him about it. And Richard, who was still somehow unaware of all the hanging out we'd been doing, told them he didn't know anything about that.

MOM: So you’ve never seen this kid before . . .

RICHARD: No, I mean . . . seen? Yeah. But not . . it wasn’t . . just in the yard and stuff.

NARRATOR: I imagine things were tense for a bit. But the clues piled up. I couldn't control myself. I took more things, bigger things. I also branched over into hiding things for Richard to find. Pretty rocks, pieces of string, letters I'd tried to write. At that age, I didn't know how to spell very many words, so the messages were fairly cryptic: the entire alphabet, followed by the word Mom and a drawing of the sun. Rampant scribbling. It must've come off like being haunted by a defective but well-meaning ghost.

The connection should have been obvious. But, when faced with a mystery like, "Where did my remote control go? Why is there a piece of paper with a child's handwriting on it hiding in the VCR? And how do these rocks keep getting in here?" almost no rational adult would jump to the conclusion "because a child has been sneaking in through my cat door and leaving these for me to discover." Not even with clues. I don't know what theory Richard came up with to explain it . . .

RICHARD: POSSIBLE THEORIES – (1) These things have always been here and I never noticed them; (2) Paranormal activity; (3) I have a very proactive form of epilepsy, and this is what I do while I am having a seizure.

NARRTOR: The thing that finally blew my cover was stealing Richard's cat. Stealing it wasn't the original plan. The opportunity presented itself, I seized it. It was a strong animal. Getting it into the drawer was difficult. It lived in the drawer for a while. I don't know how long. Hours, probably . . . And now it is time for a quick fact about cats: cats aren't good secrets, because, under extreme duress, they have the ability to make a sound like: YAOAOAOAOAOAOAOAOAOAOAOAOAOAOAOAOAOAOAOAO My parents eventually realized the sound was coming from inside the house and located the source of it. They weren't expecting to find quite so many of Richard's things. I don't know if they put the pieces together immediately or processed them individually as they came up—

MOM: First of all, there's a cat in this drawer; How about that.

DAD: There appear to be a considerable number of objects under the cat. This one is a shoe.

MOM: This one is a piece of bread.

DAD: This one is a credit card bill. Huh . . . it's addressed to 'Richard The Neighbor . . .

NARRATOR: [They were] inching closer to the truth with every clue until the ultimate answer to "What does 'hanging out with Richard' mean?" was revealed. There was more than enough evidence to answer the question. That's got to be a strange moment for a parent. There's this omnipresent fear of predators and monsters, and you just . . . you never quite expect to find out the monster is your kid. There's no Hallmark card for "Sorry we accused you of being a molester; we didn't realize our kid was sneaking into your house and stealing your spoons and animals and watching you while you sleep. We're really, really sorry."

Looking at the objects, and the freaked-out cat, and my parents' confused faces, I realized that yeah, maybe this had been a weird thing to do . . . I felt like I should explain why I had done this, but I didn't know either. So we all just stood there, feeling weird about ourselves and each other. (awkward beat) The cat was stoked to be free, though.

And Richard was (and probably still is) a very kind man.
```

---

## IC-1194: The Secret Knowledge of Grown-Ups

- Title: The Secret Knowledge of Grown-Ups
- Author (byline): David Wisniewski
- Work: Not specified
- Publisher: Harper Collins
- Publication date as stated: July 2001
- Event as filed: Humorous Interpretation
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

Unfortunately, these feral mattresses woke up and started slinging royalty around! This was very bad for King Malcolm, who spent the rest of his life in prison, eating haggis.

(EWWWWW!)

The modern domestic mattress [has a mild] disposition and long hibernation period. Still, it’s not a good idea to jump on your bed. The mattress might be hard to wake up, but it’s not impossible. And, for goodness sake, don’t play the bagpipes near it!

(Pg 49-52) [And finally] GROWN-UP RULE #82 - Don’t pick your nose. Official Reason: It’s gross and disgusting. The Truth: Actually, picking your nose is gross and disgusting. However, that’s not the real reason, which is . . . TO STOP YOUR BRAIN FROM DEFLATING!

The air pipeline that keeps your brain inflated runs past the nostrils to a vast pumping station inside your head. An intruding digit will certainly dent the pipeline. It may even poke a hole in it, causing an outburst of air called (sneezes) In technical language, a sneeze.

If you can’t give up this nasty habit right away, at least be familiar with the warning signs of brain deflation: A faint hissing noise (noise) . . . A sound like a balloon let loose in a bathtub (noise) . . . Silence, and a floppy rolling noise when you tilt your head (noise)

Although this baggy brain still works, it won’t absorb much new information, so it pays to fix it before the next spelling test. Here’s the simple way . . . Shine a flashlight up your nose (demonstrates). Just as a plant tuns toward the sun, your brain will be attracted to the light and flop over to it. Your brain will then be centered over the pipeline, ready for inflation.

[Then] hold your nose and hum. (demonstrates) Finger pressure stabilizes the pipeline. Humming entertains the mending muscles as they drive bulldozers around to fix things up. There is a more difficult way to reinflate your brain, but it requires four years of college, one pair of pliers, and three feet of lead pipe.

Hundreds of grown-up rules remain. The truth must be told about them ALL! (reaction to an unseen noise - whispers) But they’re on [our] trail. I hear them coming! THE GROWN-UPS!!!
```

---

## IC-1195: Sessions

- Title: Sessions
- Author (byline): Chris Silver
- Work: Fast Horse Plays: Round 4 (Pgs 3-16)
- Publisher: Fast Horse Drama
- Publication date as stated: Aug 2012
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: DR. RUBENSTEIN, SARA, MRS W, HELEN, TOM, AMY, LORI, RICK
- Teaser before the introduction: Yes
- Spoken words (computed): 1521
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chris Silver
Book: Fast Horse Plays: Round 4 (Pgs 3-16)
ISBN: 978-0615711379
Publisher: Fast Horse Drama
Date (Month/Year): Aug 2012
```

### Introduction (context only: never use it for content warnings)

```text
Many therapists and counselors are well-meaning, intelligent, caring, capable, competent professionals with the best of intentions. But the system they’re working in? The magnitude of the problems they confront? In many cases, let’s just say they’re up against some extremely “interesting” challenges. It can be rugged terrain. Fasten your seatbelt, Sara . . . you are in for one wild ride.

Sessions by Chris Silver
```

### Performance text (classify this)

```text
DR. RUBENSTEIN: (Pgs 3-16) Welcome to the team, Sara! I am so delighted that you've decided to join us here at Sunnyside Community Clinic.

SARA: Thank you, Dr. Rubinstein. It's really an honor to be here.

DR. RUBENSTEIN: This is a big step, Sara. Leaving the comforting nest of school and entering the cold, vile, traumatizing, hopeless, demoralizing, perverse, shocking, overwhelming, sordid, inhumane, disgusting world of actually being a therapist and having patients. I have no idea why on earth anyone would want to do it. Are you nervous? You should be.

DR. RUBENSTEIN: I have just a few words of advice, Sara. So listen carefully. (Sara takes out her notebook and begins writing.) Don't ever tell a patient that they're your first, Don't ever say, "I'm sorry," And by God, young lady, don't ever let a patient see you sweat! You're going to do just fine! !tick, tick, tick, tick, tick, tick, tick, tick, tick, tick, ding!

SARA: What brings you in today, Mrs. Weatherbottom?

MRS W: My husband and I have been married 57 years.

SARA: I see. Can you tell me a little more about that, Mrs. Weatherbottom?

MRS W: I can. We've been married 57 years, and, frankly, I'm tired of his shit.

SARA: Beg pardon?

MRS W: That's an example of standing up for myself, telling it like it is. I'm not going to stand for his crap anymore. My last therapist told me that it was important for me to be more direct.

SARA: I see. And what is it exactly that's troubling you about your husband, Mrs. Weatherbottom?

MRS W: What is it with you people and repeating my name every time you speak to me? I'm 83, not senile! He has a coffee cup problem.

SARA: A coffee cup problem, Mrs. W. . . ?

MRS W: That's what I said, yes. I have been asking Mr. Weatherbottom for the last 57 years to rinse out his cup after he has his morning coffee. And for the last 57 years he has failed to do so. What did I find this morning, after he left for his morning constitutional? That's right. The disgusting, foul remnants of his morning coffee. It repulses me.

SARA: I hear that you have some very strong feelings about this.

MRS W: I do. And my last therapist recommended that I take a stand. So I have.

SARA: Being assertive is very important, Mrs. Weatherbottom. How is your husband responding to the new you?

MRS W: I'm not sure.

SARA: What do you mean?

MRS W: Well, he hasn't returned from his morning constitutional.

SARA: I'm not sure that I follow.

MRS W: Oh, good heavens. I've been putting a few drops of rat poison in Mr. Weatherbottom's coffee for the past few months, dear.

SARA: You what? You've been poisoning your husband?

MRS W: Oh, don't get all goody-two-shoes on me, sweetie. You haven't had to live with that revolting coffee cup for the last 57 years.

SARA: I see. I'm sorry-

DR. RUBENSTEIN: "Don't ever tell a patient that you 're sorry .. "

MRS W: According to my internet research, the poison should have been gradually building up in his system, until, well, until I won't have to worry about the coffee cup any longer!

SARA: I, oh, well, you're my first...

DR. RUBENSTEIN: "Don't ever tell a patient they're your first . . . “

SARA: Oh, crap. (sweating profusely) Great. Mrs. Weatherbottom, I'm required by law to report any action to harm . . . !tick, tick,tick, tick, tick, tick, tick,tick, tick, tick,ding!

SARA: Helen, Tom, so nice to meet you. What brings you in today?

HELEN: I just don't feel like we're connecting like we used to. It's like the flame has died. The spark has been stamped out.

TOM: Oh, sweetie, I think you're just overreacting. You 're just being a big drama queen about this. Maybe it’s a mid-life crisis.

HELEN: I’m 27.

TOM: Well, perhaps we just need to have a spa day. Facials. Get manis, pedis. . . (to Sara) What do you think?

SARA: Well, Helen, why don't you share with Tom about the things that have been bothering you.

HELEN: Tom, I just feel like I don't matter as much to you as I used to. It's like you care more about your shoes than you do me!

TOM: (a horrified gasp.) Do NOT bring my shoes into this! You love going shoe shopping with me!

HELEN: Tom, you have 200 pairs. It's like you've been in your own world. You don't care about what's important to me anymore. I mean, I love Cher and Madonna as much as anyone, but variety in life is important!

SARA: Oh, good lord.

HELEN: And, I believe in community service, I really do. But I can't take anymore time off of work to travel around the country selling your handmade rainbow lanyards at Pride festivals.

TOM: You told me that you loved my rainbow lanyards! Especially the beaded ones with the little side fringes.

HELEN: Now, Tom, don't get upset . . . I just think we need a little more "us" time, Tom.

TOM: Us time? Us time? This is feeling very overwhelming for me right now. I need to take some deep breaths.

SARA: Okay, hang on. I don't mean to be presumptive, Helen, but have you considered the possibility that Tom might be g-

HELEN: Greedy? Yes, I have. Tom just seems to care about himself lately.

SARA: No, Helen, not greedy. G-

HELEN: Guilty. Yes, I think that's a good observation. I would imagine that Tom is feeling very guilty about neglecting me, his wife.

TOM: I do not feel guilty, sweetheart! I will not apologize for being fabulous!

SARA: NO! NO! Not greedy! Not guilty! Not gluttonous or gruesome either. GAY! Have you considered the possibility that Tom might be GAY?

HELEN: No. That hasn't occurred to me. (considers it very seriously) Hmmm. No. I don't think that's the problem.

TOM: I am definitely not gay, sweetheart. Maybe you're new at this?

SARA: Oh, good grief. (looks as if she's about to cry) !tick, tick, tick, tick, tick, tick, tick, tick, tick, tick, ding!

SARA: Yes, what is it?

AMY: I've seen a whole lot of therapists, and I've never heard that opening before. Long day got you down? What are you, new?

SARA: Actually, no, I've been at this for a while now. But, let's talk about you, Amy. (reading from her file.) It looks like you were just placed with a new foster family. How is that going for you?

AMY: Not very well.

SARA: That's too bad. Would you like to tell me a little more about that?

AMY: I'm basically like the bad seed.

SARA: That sounds a little dramatic.

AMY: It's actually an understatement.

SARA: Why don't you share a little more with me about how things have been going at your new placement?

AMY: Well, let's see . . . I made some delicious refreshments for my new foster mommy and daddy and then I served them my tantalizing concoctions accompanied by an original song and dance routine.

SARA: That sounds very. . . spirited of you. How did they like that?

AMY: They hated it. I don't think they liked my smoothies very much . . .

SARA: What gave you that impression?

AMY: Probably something about them screaming and crying while I was serving them. And then there was that part about them calling the police.

SARA: (getting a bit nervous) What kind of smoothies did you serve them, Amy?

AMY: My favorite. Strawberry Banana. With a little something extra. Like a protein boost.

SARA: Okay . . .

AMY: Well, you see, there's a perfectly logical explanation . . . I was home doing my homework, when I thought, "what would a fun activity for the bad seed?" And, well, then I saw Whiskers, and well. . . (during her description, my pantomimes the process and makes the blender and meow sounds) It was really pretty easy . . . I just put Whiskers in the freezer, for, quite a while . . .

SARA: This isn't happening

AMY: Oh, but it is, then I took a butcher . . .

SARA: Okay . . . okay . . .

AMY: They have a really powerful blender! . . . (demonic voice) I told them I was allergic to cats! (singing and dancing) "Kitty smoothie! Meow Meow Meow! Kitty Smoothie! . . . Is it true that kids who do bad things to animals often grow up to be serial killers? !tick, tick, tick, tick, tick, tick, tick, tick, tick, tick, ding!

(As SARA reflects on her day, bits and pieces of her clients come back to her, rapid fire, building to a literal crescendo of nuttiness. . . the noise of AMY's blender and the cat's meowing are interspersed throughout the entire sequence.)

MRS W: 57 years of that coffee cup!

TOM: I'm not gay, I'm just fabulous!

DR. RUBENSTEIN: Don't ever say, I'm sorry!

MRS W: You will pay, Mr. Weatherbottom. I warned you.

DR. RUBENSTEIN: Don't every let them see you sweat.

TOM: Just because I have more shoes then Helen does, does not make me G-

AMY: Bad seed, I tell you!

DR. RUBENSTEIN: "Don't ever tell a patient they're your first . . . “

AMY: (singing) "Kitty smoothie! Kitty smoothie! Meow meow meow!" (the sequence builds to an explosive ... !tick, tick, tick, tick, tick, tick, tick, tick, tick, tick, ding!

SARA: (utterly exhausted, with nothing left to give) I'm sure I'm not supposed to tell you this, but I don't care. You're my last patient of the day. What's your problem?

LORI: Um, well, we just had a new baby, Rick and I, and well, she's our first. We're a little overwhelmed. Excited, but overwhelmed. It's a lot, you know? And, we just want to make sure we're communicating about everything and

RICK: And we just thought it would be good to talk to someone.

SARA: Right. Because your baby is possessed by Satan.

LORI: (nervous laughter) Oh, you' re funny. No, she's wonderful. She's perfect.

SARA: Okay, the two of you are actually axe-murderers. Oh, no, wait. . . you're axe murderers who each have 700 personalities, and you believe that you're actually aliens from . . . I don't know, Neptune.

RICK: You are really funny. We must be so normal compared to most of the folks who come in here. We're pretty boring. We just want to talk.

SARA: Just talk? Is this a trick? !tick, tick, tick, tick, tick, tick, tick, tick, tick, tick, ding!

AMY: (singing) "Kitty smoothie! Kitty Smoothie! Meow Meow Meow!" (ends with the blender and a loud cat screech)
```

---

## IC-1196: The Seussification of Romeo and Juliet

- Title: The Seussification of Romeo and Juliet
- Author (byline): Peter Bloedel
- Work: Random Acts of Comedy (Pg 189-216)
- Publisher: Playscripts, Inc.
- Publication date as stated: Aug 2011
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR 1, NARRATOR 2, BOTH, PROLOGUE, PARIS, CAPITULATE, SERVANT, BENVOLIO, ROMEO, TYBALT, JULIET, NURSE, MONK LARRY, MERCUTIO, THE PRINCE, LADY CAPITULATE
- Teaser before the introduction: Yes
- Spoken words (computed): 1392
- Already set (do not supply): none

### Source block (context only)

```text
Author: Peter Bloedel
Book: Random Acts of Comedy (Pg 189-216)
ISBN: 978-0981909974
Publisher: Playscripts, Inc.
Date (Month/Year): Aug 2011
```

### Introduction (context only: never use it for content warnings)

```text
The Seussification of Romeo and Juliet by Peter Bloedel
```

### Performance text (classify this)

```text
NARRATOR 1: Dear Ladies and Menfolk! NARRATOR 2: Women and Gents!

NARRATOR 1: You're people of culture and true common sense.

NARRATOR 2: You know what you know, and you like what you like.

NARRATOR 1: Like singing a song or riding a bike.

NARRATOR 2: We like that stuff too! NARRATOR 1: It's the greatest!

NARRATOR 2: You bet! NARRATOR 1: And topping the list ...

BOTH: Romeo and Juliet.

NARRATOR 2: The play is just perfect. NARRATOR 1: Nothing is wrong.

NARRATOR 2: Except that it's almost two hours . . .

BOTH: (Glancing at each other and then to the audience) Too Long!

NARRATOR 2: We've shortened the play, changed some names, made it rhyme No more of that blank verse, we don't think he'd mind.

NARRATOR 1: [(whispers) Shakespeare]

PROLOGUE: Verona's the place from where our play is picked. Two families lived there, and man were they ticked. Straight from the loins of those mentioned above . . . . (Lady Monotone enters visibly pregnant) Popped kid one ... (Popping sound. ROMEO pops out, crying and sucking on his thumb. His mother is now visibly NOT pregnant.) And kid two . . . (Popping sound. JULIET pops out crying and sucking her thumb. Her mother is now visibly not pregnant.) And they fell in love. (Romeo and Juliet look lovingly at each other and stop crying) *****

NARRATOR 2: Meanwhile at the Capitulate pad, There's a suitor for Julie and he's with her dad.

PARIS: Capitulate! I am the man for your daughter.

CAPITULATE: I don't think you'll do.

PARIS: But who could be hotter? Besides that, I brought you some peppermint candy.

CAPITULATE: (To the SERVANT) Does he have a point? (The SERVANT nods.) (To Paris) I think you'll be dandy. Let's have a banquet. (To the SERVANT) Young man go and get all of these people whose names I have writ. (CAPITULATE hands an invitation list to the SERVANT and then exits with PARIS.)

SERVANT: Before I can find all the people and greet 'em, I need to find help from someone who can read 'em.

BENVOLIO: (Interrupting him) Hey buddy! What's up? Can we help you there?

SERVANT: Sure enough, if there is help then I need it, 'cuz I've got this list here, and I just can't read it. To find a strong reader is what I've been hoping . . .

ROMEO: (Taking the list) I'll read it to you, it will keep me from moping. (He reads) These folks can come to Capitulate's party: Smarty Martino and his boy named Arty, Bronco Buck Billy, and Buck Billy Buff, And Lady McDinky, McDucky, McDuff // Dave from Topeka, and Lady Von Rybald, Rosaline, Valentine, Livia, Tybalt, Anyone named Gordie or Tim or Melissa, Can come to this bash, if you can't then we'll miss ya. (Finished reading, he says to SERVANT) This party sound great. ***** Suddenly we're at the party *****

(Romeo dances, then notices JULIET)

ROMEO: Ei-hotchee-mama, Growl, Whoo! Hubba-hubba! That girl is a babe or my name is dumb hubba. (ROMEO pulls his visor down over his eyes to conceal his identity, he goes to JULIET and commences flirting.) Please, don't think I'm forward, but I think you're hot! (An alarm goes off TYBALT rushes down stage from the party group.)

TYBALT: (to audience) My Monotone alarm just gave the alert! I keep it hidden right here in my shirt. It detects Monotones. It's never wrong. And this one is foolin' where he don't belong.

JULIET: (Aside) I can't see his face is it worth it or not? (ROMEO lifts his visor and leans in for a kiss) Hey, you're kind of cute, okay, here, hold my gum first. It's raspberry, lima bean, sneezle fruit, bratwurst. (They kiss.)

ROMEO: Wow! Hey, you're right, that is good tasting gum.

NURSE: (Enters and says to Juliet) Your mother would like a few words with you, hon. (Juliet exits)

ROMEO: Who is her Mom, if I may be so bold? Quickly, please tell me before I get old.

NURSE: Her Dad is the host, who bought that main course dish you ate. Her Mother's no other than Lady Capitulate. Juliet is her name and she is the fairest. But don't get ideas. She's marrying Paris. (Romeo’s excitement is crushed) *****

NARRATOR 1: Needless to say Romy's heart-ache was done. He met a new girl and she had good gum. (JULIET enters aloft) All of the guests from the banquet had parted, But not Romeo, he was just getting started. (Romeo enters and spies Juliet aloft)

JULIET: Romeo baby-o, baby-o, buff! Wherefore art thou, I just can't get enough.

ROMEO: Oh, Juliet, you're a pearl of great price. You're like two pearls only much, much, more nice.

JULIET: Let's find the preacher!

ROMEO: Let's get hitched tomorrow. Enough of this fighting . . .

JULIET: . . . This feuding . . .

BOTH: This sorrow. (They run away blowing kisses to each other.) *****

NARRATOR 2: So Romeo ran to the home of Monk Larry, Not monkey Larry ... he's not quite that hairy, He's just a monk, he's the monkiest one That Romeo knew and could get the job done. (Enter ROMEO.)

ROMEO: Oh good! Monk Larry! I'm glad that you're here.

MONK LARRY: (In a Bronx accent) Where else would I be, I've not left here in years. How can I help you, my dude filled with glee? (ROMEO grabs MONK LARRY's hand and gets down on one knee.)

ROMEO: I need your consent, Monk, will you marry me? (Monk Larry looks aghast) No, No! There's a girl that I've met as of late, She is the daughter of Capitulate. Our love is true. MONK LARRY. Are you sure?

ROMEO: Yes indeed. One-hundred and ninety percent guaranteed.

MONK LARRY: (Aside to the audience) If I marry the girl to this Monotone dude-ling, It may end the war, all this troublesome feud-ling. (To ROMEO) Okay, my young pup, I'll tie your knot, But, if you're eloping, then you'll need a plot. *****

NARRATOR 1: Romy and J were now happily married, They both yelled "hurray," and then off they scurried. But not all was happy in this neighborhood, Mercutio and Tybalt were up to no good. (MERCUTIO mimes fighting with an unseen TYBALT)

ROMEO: (ROMEO enters) Hey guys! Quit fighting, 'cuz that's just as bad, As putting chameleons on top of plaid. (MERCUTIO is stabbed in the chest and falls. Romeo reacts to Mercutio’s fall) Mercutio!

MERCUTIO: Romeo!

ROMEO: Friend, are you dying?

MERCUTIO: No, I'm feeling fine . . . and . . . I am lying. (lets out a blood-curdling scream)

(ROMEO pulls TYBALT's sword free. He stumbles backwards from the pull and kills TYBALT with his own weapon.)

TYBALT: With my own bumballoon, now I am slain!

ROMEO: (ROMEO is stunned that he just killed TYBALT.) What in the world? Crap! How did this happen? (ROMEO exits.) *****

THE PRINCE: What happened here? I'd like to explore / The reason there's two dead guys here on the floor.

BENVOLIO: Tybalt here bumballooned good friend Mercutio, and then got his bell rung by poor, sweet, young Romeo.

LADY CAPITULATE: (To the PRINCE) My kinsman Tybalt lies dead on the floor. Romeo must die to even the score.

THE PRINCE: Easy there girly-girl! I call the shots. I am the prince here believe it or not. I'll banish young Romeo from fair Verona, As soon as I finish this slice of bologna. *****

NARRATOR 1: Romeo has to go to skip town or else, The prince might find out and put him on the shelf. We see here young Julie as she thinks and sits,

JULIET: I'm wife to a banished guy. Man! That's the pits. I can't marry Paris, 'cuz I've got a husband. I'm sure that's illegal except in Wisconsin. I need to get help. If I don't, then I'm sunk. This is a job for old Larry the Monk. (She arrives at Monk Larry’s place) Gentle Monk Larry, I need some assistance. My wedding's tomorrow despite my resistance. To Romeo, you'll recall, I am now wed. But, they'd have me wed Paris . . .

MONK LARRY: Not if you're dead. Listen, I've got a plan, but it takes guts, And you must eat two of these death faking nuts.

JULIET: How'll Romeo know that I'm not really croaked?

MONK LARRY: I'll send him an email, I'll tell him our joke.

NARRATOR 2: The monk sent his email with details attached But, Romeo missed it, 'cuz his PC crashed. (Romeo mimes typing on a keyboard and reacts to the computer crashing) He never learned Juliet was faking disaster.

NARRATOR 1: Later that night Juliet ate the nuts. (JULIET eats the nuts looking around and chewing obnoxiously. Then, very suddenly, she falls over as if dead in her bed.) Then in the morning, she wouldn't wake up. (The NURSE enters and screams.) *****

NARRATOR 1: Meanwhile back on the beach of Kadid, We meet up with Romeo, that's where he hid.

BENVOLIO: Romeo wake up, and hear what I say, Juliet's dead and her funeral's today.

ROMEO: It must have been her broken heart that went "Crack!" I'll kiss her one last time. I must now go back! Then I'll consume this authentic death cracker. (ROMEO holds up a single soda cracker.) Off to Verona I go with my life, To lay it before my corpse of a wife. (Romeo travels to Juliet’s tomb) Juliet, honey, to get here I ran. I tripped on a grave stone and fell on my can. I came here to give your lips just one more kiss, And then, when I'm done, I'm gonna eat this. (He holds up the authentic death cracker dramatically.) Here comes the kiss so pucker up sister. (He kisses Juliet) Yippee, yahoo! You're still a great kisser. That was phase one, now here comes phase two . . .

(ROMEO holds the cracker up and makes a big production out of eating it. He assumes a safety position as if something is going to happen. It doesn't. He stands up straight and waits. He checks his watch. He whistles. The NARRATORS enter.)

NARRATOR 2: Now, there's a reason that Romeo's life isn't halting,

NARRATOR 1: 'Cuz we switched his death cracker with a plain saltine.

NARRATOR 2: We've read this show, and it don't end pretty,

NARRATOR 1: So we tweaked the plot a bit-made it less gritty.

NARRATOR 2: Juliet woke from her death grip like slumber, And overjoyed, Romeo did a back flip dance number. (Romeo dances)

NARRATOR 1: Mercutio and Tybalt weren't really dead, (MERCUTIO and TYBALT enter.)

TYBALT: We were just teasing, MERCUTIO: Playin' with your head.

NARRATOR 1: Long years of bitterness melted away.

NARRATOR 2: Now they had nothing but nice things to say.

CAPITULATE: Say! I like that tie. MONOTONE. I like your trousers and ... you're a nice guy.

NARRATOR 1: It was official. The feuding had ended, The lovers kept loving and the families befriended.

NARRATOR 2: Now, you may have noticed that no one here died.

NARRATOR 1: What!? Can we help it if our prologue lied? But, come on! That's no way to end a good play.

NARRATOR 2: Dr. Seuss wouldn't I'd venture to say.

NARRATOR 1: That's right, he wouldn't, and neither would we, Even though our play is Dr. Seuss-free.

NARRATOR 2: We hope you've enjoyed this tragic lament.

NARRATOR 1: 'Cus we've all enjoyed it ... One-hundred percent!
```

---

## IC-1197: Three Sideways Stories from Wayside School

- Title: Three Sideways Stories from Wayside School
- Author (byline): Louis Sachar – adapted by Aaron Shepard
- Work: Not specified
- Publisher: Harper Trophy
- Publication date as stated: June 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MRS. JEWLS, JOE, CALVIN, BEBE, LOUIS
- Teaser before the introduction: No
- Spoken words (computed): 1512
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
NARRATOR: One day, Mrs. Jewls kept Joe in from recess.

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

MRS. JEWLS: No. You got the right answer, but you counted the wrong way. You were just lucky.

NARRATOR: She set down eight potatoes.

MRS. JEWLS: How many potatoes, Joe?

JOE: Seven, five, three, one, two, four, six, eight. There are eight potatoes, Mrs. Jewls.

MRS. JEWLS: No, there are eight.

JOE: But that’s what I said! May I go to recess now?

MRS. JEWLS: No! You got the right answer, but you counted the wrong way again.

NARRATOR: She put down three books.

MRS. JEWLS: Count the books, Joe.

JOE: A thousand, a million, three. Three, Mrs. Jewls.

MRS. JEWLS: (bewildered) Correct.

JOE: May I go to recess now?

MRS. JEWLS: No.

JOE: May I have a potato?

MRS. JEWLS: No! Listen to me. One, two, three, four, five, six, seven, eight, nine, ten. Now you say it.

JOE: One, two, three, four, five, six, seven, eight, nine, ten.

MRS. JEWLS: Very good!

NARRATOR: She put down six erasers.

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

MRS. JEWLS: (shaking head, “no” ) Yes, that is right. *****

NARRATOR: Bebe was the fastest draw in Mrs. Jewls’s class. She could draw a cat in less than forty-five seconds, a dog in less than thirty, and a flower in less than eight seconds! But of course, Bebe never drew just one dog, or one cat, or one flower. Art was from 12:30 to 1:30. Why, in that time, she could draw fifty cats, a hundred flowers, twenty dogs, and several eggs or watermelons! You see, it took her the same time to draw a watermelon as an egg. Calvin sat next to Bebe. He didn’t think he was very good at art. It took him the whole period just to draw one airplane. So instead, he just helped Bebe. He was Bebe’s assistant. As soon as Bebe would finish one masterpiece, Calvin would take it from her and set down a clean sheet of paper. Whenever her crayon ran low, Calvin was ready with a new crayon. That way, Bebe didn’t have to waste any time. And in return, Bebe would draw five or six airplanes for Calvin. It was 12:30, time for art. Bebe was ready. On her desk was a sheet of yellow construction paper. In her hand was a green crayon. Calvin was ready. He held a stack of paper and a box of crayons.

CALVIN: Ready, Bebe?

BEBE: Ready, Calvin.

MRS. JEWLS: All right, class. Time for art.

NARRATOR: She had hardly finished her sentence when Bebe had drawn a picture of a leaf. Calvin took it from her and put down another piece of paper.

BEBE: Red! Blue!

NARRATOR: They were quite a pair! Their teamwork was remarkable. Bebe drew pictures as fast as Calvin could pick up the old paper and set down the new. A fish. An apple. Three cherries— At 1:30, Mrs. Jewls announced,

MRS. JEWLS: Okay, class, art is over.

NARRATOR: Bebe dropped her crayon and fell over on her desk. Calvin sighed and leaned back in his chair. He could hardly move. They had broken their old record. Bebe had drawn three hundred and seventy-eight pictures! They lay in a pile on Calvin’s desk. Mrs. Jewls walked by.

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

MRS. JEWLS: But if that one picture is better than each of Bebe’s two million, then that person has produced more art than Bebe.

NARRATOR: Bebe looked like she was going to cry. She picked up all the pictures from Calvin’s desk and threw them in the garbage. Then she ran from the room, down all the stairs, and out onto the playground. Louis, the nice yard teacher, spotted her.

LOUIS: Where are you going, Bebe?

BEBE: I’m going home to draw a picture of a cat.

LOUIS: Will you bring it to school and show it to me tomorrow?

BEBE: Tomorrow? By tomorrow I doubt I’ll be finished with even one whisker. (rushes off)

*****

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

CALVIN: Yes, ma’am!

NARRATOR: Calvin walked out of the classroom and stood outside the door. He didn’t know where to go. As you know, when the builder built Wayside School, he accidentally built it sideways. But he also forgot to build the nineteenth story. He built the eighteenth and the twentieth, but no nineteenth. He said he was very sorry. There was also no Miss Zarves. Miss Zarves taught the class on the nineteenth story. Since there was no nineteenth story, there was no Miss Zarves. And besides that, as if Calvin didn’t have enough problems, there was no note. Mrs. Jewls had never given Calvin the note.

CALVIN: (sarcastically) Boy, this is just great! I’m supposed to take a note that I don’t have, to a teacher who doesn’t exist, and who teaches on a story that was never built!

NARRATOR: He didn’t know what to do. He walked down to the eighteenth story, then back up to the twentieth, then back down to the eighteenth, and back up again to the twentieth. There was no nineteenth story. There had never been a nineteenth story. There would never BE a nineteenth story. Calvin walked down to the administration office on the first story. He decided to put the note in Miss Zarves’s mailbox. But there wasn’t one of those, either. That didn’t bother Calvin too much, though, since he didn’t have a note. He looked out the window and saw Louis, the yard teacher, shooting baskets.

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

LOUIS: That’s good. The truth is always best. Besides, I don’t think I understand what I said, either!

NARRATOR: Calvin walked back up the thirty flights of stairs to Mrs. Jewls’s class.

MRS. JEWLS: Thank you very much, Calvin. That was a very important note, and I’m glad I was able to count on you.

CALVIN: Yes, but you see—

MRS. JEWLS: The note was very important. I told Miss Zarves not to meet me for lunch.

CALVIN: Don’t worry . . . She won’t!

NARRATOR: So now you know about Wayside School. Some people say these stories are strange and silly. That is probably true. But when the children at Wayside School heard stories about us, they thought we were strange and silly. And that’s for sure!
```

---

## IC-1198: Six to Eight Black Men

- Title: Six to Eight Black Men
- Author (byline): David Sedaris
- Work: Dress Your Family in Corduroy and Denim
- Publisher: Back Bay Books
- Publication date as stated: May 2005
- Event as filed: Humorous Interpretation
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

## IC-1199: The Sneetches

- Title: The Sneetches
- Author (byline): Theo Geisel (aka Dr. Suess)
- Work: Not specified
- Publisher: Random House, Inc.
- Publication date as stated: Aug 1961
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, STAR BELLIED SNEETCHES, MCBEAN, PLAIN BELLIED SNEETCHES
- Teaser before the introduction: Yes
- Spoken words (computed): 815
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theo Geisel (aka Dr. Suess)
ISBN: 978-0394800899
Publisher: Random House, Inc.
Date (Month/Year): Aug 1961
```

### Introduction (context only: never use it for content warnings)

```text
At first glance, The Sneetches by Theodor Seuss Geisel feels like a simple children’s story -- bright creatures, ridiculous machines, and a problem as silly as stars on bellies. It invites us to laugh, to relax, to believe this is just another harmless rhyme.

But listen a little closer, and the humor starts to shift. Today division doesn’t feel trivial. It feels constant. It feels loud. It feels uncomfortably real, as people sort themselves into political and moral parties and question the worth of others . . . And that’s when the laughter at a silly children’s story gets quiet.

The Sneetches by Theodore Geisel (aka Dr. Suess)
```

### Performance text (classify this)

```text
NARRATOR: Now the Star-bellied Sneetches had bellies with stars.
The Plain-bellied Sneetches had none upon thars.
The stars weren't so big; they were really quite small.
You would think such a thing wouldn't matter at all.
But because they had stars, all the Star-bellied Sneetches would brag . . .

STAR BELLIED SNEETCHES: We're the best kind of Sneetch on the beaches.

NARRATOR: With their snoots in the air, they would sniff and they'd snort . . .

STAR BELLIED SNEETCHES: We'll have nothing to do with the plain-bellied sort.

NARRATOR: And whenever they met some, when they were out walking, they'd hike right on past them without even talking.

NARRATOR: When the Star-bellied children went out to play ball,
could the Plain-bellies join in their game? Not at all!
You could only play ball if your bellies had stars,
and the Plain-bellied children had none upon thars.
When the Star-bellied Sneetches had frankfurter roasts,
or picnics or parties or marshmallow toasts,
they never invited the Plain-bellied Sneetches.

Left them out cold in the dark of the beaches. Kept them away; never let them come near, and that's how they treated them year after year.

Then one day, it seems, while the Plain-bellied Sneetches
were moping, just moping alone on the beaches,
sitting there, wishing their bellies had stars,
up zipped a stranger in the strangest of cars.

MCBEAN: My friends . . .

NARRATOR: He announced in a voice clear and keen

MCBEAN: My name is Sylvester McMonkey McBean.
I've heard of your troubles; I've heard you're unhappy.
But I can fix that; I'm the fix-it-up chappie.
I've come here to help you; I have what you need.
My prices are low, and I work with great speed,
and my work is one hundred percent guaranteed.

NARRATOR: Then quickly, Sylvester McMonkey McBean put together a very peculiar machine. Then he said . . .

MCBEAN: You want stars like a Star-bellied Sneetch? My friends, you can have them . . . for three dollars each. Just hand me your money and climb on aboard.

NARRATOR: They clambered inside and the big machine roared. It bonked. It clonked. It jerked. It berked. It bopped them around, but the thing really worked.

When the Plain-bellied Sneetches popped out, they had stars! They actually did, they had stars upon thars! Then they yelled at the ones who had stars from the start,

PLAIN BELLIED SNEETCHES: We're exactly like you; you can't tell us apart. We're all just the same now, you snooty old smarties. Now we can come to your frankfurter parties!

STAR BELLIED SNEETCHES: Good grief! We're still the best Sneetches, and they are the worst. But how in the world will we know if which kind is what or the other way 'round?

NARRATOR: Then up stepped McBean with a very sly wink, and he said . . .

MCBEAN: Things are not quite as bad as you think.
You don't know who's who, that is perfectly true.
But come with me, friends, do you know what I'll do?
I'll make you again the best Sneetches on beaches,
and all it will cost you is ten dollars eaches.
Belly stars are no longer in style.
What you need is a trip through my stars-off machine.
This wondrous contraption will take off your stars,
so you won't look like Sneetches who have them on thars.

NARRATOR: That handy machine, working very precisely,
removed all the stars from their bellies quite nicely.
Then, with snoots in the air, they paraded about.
They opened their beaks and proceeded to shout . . .

STAR BELLIED SNEETCHES: We now know who's who, and there isn't a doubt, the best kind of Sneetches are Sneetches without.

NARRATOR: Then, of course those with stars all got frightfully mad.
To be wearing a star now was frightfully bad.
Then, of course old Sylvester McMonkey McBean
invited them into his stars-off machine.
Then, of course from then on, you can probably guess,
things really got into a horrible mess.

All the rest of the day on those wild screaming beaches,
the Fix-it-up-Chappie was fixing up Sneetches.
Off again, on again, in again, out again,
through the machine and back round about again,
still paying money, still running through,
changing their stars every minute or two,
until neither the Plain- nor the Star-bellies knew
whether this one was that one or that one was this one
or which one was what one or what one was who!

Then, when every last cent of their money was spent, the Fix-It-Up-Chappie packed up and he went. And he laughed as he drove in his car up the beach. . .

MCBEAN: They never will learn; no, you can't teach a Sneetch!"

NARRATOR: But McBean was quite wrong, I'm quite happy to say,
the Sneetches got quite a bit smarter that day.
That day, they decided that Sneetches are Sneetches,
and no kind of Sneetch is the BEST on the beaches.
That day, all the Sneetches forgot about stars,
and whether they had one or not upon thars.
```

---

## IC-1200: Snow White & the Seven Microaggressions

- Title: Snow White & the Seven Microaggressions
- Author (byline): Laura Lane and Ellen Haun
- Work: Cinderella and the Glass Ceiling, Pgs 22-31
- Publisher: Seal Press
- Publication date as stated: Mar 2020
- Event as filed: Humorous Interpretation
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

EVIL QUEEN: Okay, fine. I was being mean. But that time it was on purpose. Mark, you are dismissed. (calling after him as he exits) And bring me Bob, my second henchman.

Let’s get his opinion on whether I’m doing microaggressions or not. And in the future, you have no reason to be scared of me!

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
