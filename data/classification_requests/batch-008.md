# Classification request: batch 8 of 63 (40 records, IC-0281 to IC-0320)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-008-reply.json`.

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

## IC-0281: This is Where it Ends

- Title: This is Where it Ends
- Author (byline): Marieke Nijkamp
- Work: Not specified
- Publisher: Sourcebooks Fire
- Publication date as stated: Jan 2016
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: PRINCIPAL TRENTON, AUTUMN, FATHER, TYLER
- Teaser before the introduction: Yes
- Spoken words (computed): 1379
- Already set (do not supply): none

### Source block (context only)

```text
Author: Marieke Nijkamp
ISBN: 978-1492622468
Publisher: Sourcebooks Fire
Date (Month/Year): Jan 2016
```

### Introduction (context only: never use it for content warnings)

```text
This is Where It Ends by Marieke Nijkamp.
```

### Performance text (classify this)

```text
PRINCIPAL TRENTON: (at a podium addressing the entire school body on the 1st day of 2nd Semester) (Pg 5) Here at Opportunity, we pride ourselves on shaping the doctors, lawyers, and politicians of tomorrow. And it’s the choices you make now that will determine your future.

AUTUMN: (Pg 5-6) My brother would tell me that Principal Trenton’s words are truer than I think; that it’s up to me to make my future the best it can be. For me, college is the only way out of this misery, and Dad sure as hell isn’t going to pay my ride. Not to study dance.

FATHER: Look what happened to your mother. . .

AUTUMN: As if I haven’t counted the days, hours, minutes since Mom’s accident.

FATHER: Dance took everything from her. No daughter of mine is going into that business. Not if I can stop it.

AUTUMN: So he tries to stop me—every day. And with Mom gone, there’s no one to stop him. Not from drinking. Not from hitting me. There’s no one to keep our family from falling apart.

PRINCIPAL TRENTON: (Pg 4) . . . it’s all a matter of the decisions you make, today and every day. Your behavior reflects not only on yourself but also on your parents, your family, and your school.

AUTUMN: (Pg 30) A set of doors to my left opens. blond locks under a black knit cap. That’s the first thing I notice—the unruly hair that frames a too-familiar face. [NOTE: Attributed to another student, Sylv, in the novel] (Pg 42) Tyler. My brother.

TYLER: (Pg 30) (with a handgun pointed at her head, he calls out in a sing-song voice) Principal Trenton, I have a question. (he fires)

AUTUMN: (Pg 35) The stage is a mess of people congregating around Principal Trenton—Mr. Jameson, everyone’s favorite English teacher, tries to stem the blood flow, except she’s hit in the head, and it’s not blood but brains. [NOTE: Attributed to another student, Sylv, in the novel]

TYLER: (Pg 60) I have no issue with most of you, so I’d rather you don’t force me to waste my bullets.

AUTUMN: (Pg 34) The room is swept up in panic. Screams echo in my ears. Teachers standing near the doors try to approach Tyler, but he picks them off methodically, like everyone who gets too close. (Pg 37) I hear gasps and cries and screams. There’s death, there’s dying, and there’s blood everywhere. [NOTE: Attributed to another student, Sylv, in the novel]

TYLER: (he struts to the stage) (Pg 71-72) I liked it here once. Opportunity High. Opportunity. It sounds so hopeful. I wanted to fit in here. Instead, I lost everything. All of you with your perfect lives. Do you know what losing feels like? Do you care?

AUTUMN: (Pg 57-58) Fear and survival are two sides of the same coin. Dad taught me that. These last two years, he proved it again and again and again. Terror is our strongest force because we’re only afraid when we have something to lose. (Pg 73) I don’t know what Ty wants, but if they try to stop him, this’ll only get worse.

TYLER: If you cooperate, some of you might go home today. All you have to do is listen carefully. No screaming, no running, no phones. Today, you’ll all listen.

AUTUMN: (Pg 42) My brother, who cared for my bruises when Dad couldn’t contain his grief. Who helped me dance. Once, he caught Dad’s belt on his bare arm to stop it from coming down on me. Afterward, Tyler cracked a joke and tousled my hair. He is the only real family I have. It can’t be him.

TYLER: (Pg 87-88) (smiling and grandiose) Now then. Good. To survive, you must know who your friends are. You must know who you can trust. And you must know how to stop caring.

AUTUMN: His smile was just like Dad’s—cold. A couple nights ago, Ty stood by while Dad showed me that the love he once had for dance, for me, died along with Mom. Yesterday, Ty laughed through his tears. When he tended my bruises, he told me there was nothing that made him happier than to see me dance. It reminded him of when Mom was alive and we’d go see her performances. He said that even though he’d never felt the extremes of Dad’s anger, he’d already lost so much. We both had. I wanted to believe him. He’s my brother.

TYLER: (Pg 89) Lesson one: don’t get attached and you won’t get hurt. (He fires)

AUTUMN: Without a second glance, without so much as a blink, he pulls the trigger and shoots Mr. Jameson.

TYLER: (Pg 102) Do you know what it feels like to lose everything you hold dear? Your family? Your girlfriend? For your entire town to turn against you too? I’m reclaiming Opportunity. Your lives are mine. And you will pay attention. (tapping the barrel of the gun against his chin he speaks softly while pacing back and forth) (Pg 104) I thought my family at least cared about me. But you corrupted them. You left nothing for me (beat) Wouldn’t you agree, Autumn? (silence) (Pg 107) (in a singsong voice) Would it help if I gave you an incentive to make the right decision?

AUTUMN: He jumps off the stage and paces in front of the students like he’s deciding who to pick for his basketball team in PE. (Pg 109-110) He leans over and drags a girl by her baseball jersey over the row of seats. She’s young—a sophomore maybe. Too young to die. The auditorium may be big enough to hold a thousand students, but it’s too small to hide just one.

TYLER: (Pg 113-114) (he calls out) It’s easy, Autumn. Come out or I’ll pick off the entire school.

(gunshots punctuate each word) Just. Like. This.

AUTUMN: (to audience) (Pg 124-125) Every time I blink, I see Nyah’s face being torn apart by a bullet. If anyone can get through to him, it’s me. I have to try . . . (to Tyler) Tyler. (clears her throat and speaks louder) Tyler. I’m here. (to audience) (Pg 136) I’m staring at a stranger. This is not the same person who showed me the abandoned shed where I could dance in secret. This isn’t the same person who bought me pointe shoes. He may look and sound like Tyler, but this is not the same person.

TYLER: (Pg 134) (sarcastically) Do you expect me to shout at you from across the room? Did your mother not raise you better than that?

AUTUMN: (Pg 136) When I reach the stage, the full horror hits me. The bodies of half a dozen teachers lie up there. (to Tyler) Why, Tyler?

TYLER: (Pg 137) (grabbing a fistful of Autumn’s hair and pulling her on stage – his gaze devoid of humanity) You think you are so special, don’t you? Do you even care about anyone anymore? Or do you only care about yourself? (He holds the gun to her face)

AUTUMN: Please don’t. (whispers) I love you. (Pg 146-147) You’re my brother. You’re my best friend. You’re everything to me. What happened to us, Ty? I lost as much as you did. But you made me believe fulfilling Mom’s dream—my dream—was still possible.

TYLER: (blinks) Believe in your dream?

AUTUMN: To get out of here.

TYLER: (begins to laugh, louder and louder) I wanted to be your excuse to stay home. But you pushed me away. (Pg 148) You told me there was nothing keeping you here. Not even me. (the laughing turns to sobbing) It’s your fault. (gestures grandly) All of this, is your fault. (he fires again into the crowd)

AUTUMN: (Pg 153) I know it’s my fault. (softly) Not a day goes by when I don’t miss Mom. I wish I could go back and redo that day. But I can’t. I can’t. I can only keep doing what she wanted me to do, and she wanted me to dance, Ty.

TYLER: (Pg 161) (seething) I hate you. You never cared about me. You never cared about any of us. You only ever cared about dance.

AUTUMN: (wincing) I want to contradict him, but I can’t. Dance is beauty. Dance is compassion, honesty. The only way I’ve ever known how to share my feelings is through dance.

TYLER: (points the gun again at Autumn) So dance. You wanted a stage? Take it!

AUTUMN: (assumes 5th position and begins to dance with trembling hands and tears pouring down her face) (to the audience) (Pg 175) They say your life flashes in front of your eyes right before you die. As I wait for Ty to pull the trigger, no memories overtake me. No last wishes or if-onlys. (she can’t dance anymore, and crumples) When Dad was at his worst, he’d call me every name he could think of and wouldn’t stop until he felt like he’d won. Ty is worse. His eyes are wild and unrecognizable.

TYLER: (shaking his head) I thought you understood the loneliness and the loss. I thought that was why you wanted to get out—to fight back. To win. (facing the auditorium, he punctuates each word with a gunshot) (Pg 182) I. Will. Not. Let. You. Go.

AUTUMN: (grabbing his arm, she steps between him and the students in the auditorium) (Pg 260) You won’t kill me. We’re family. That must count for something. (he brushes Autumn aside roughly, takes aim and fires at her) (Autumn drops to the ground -- long beat) (to audience) (Pg 270) When Ty pointed the gun at me, he broke me. I didn’t need to die for him to kill me. He simply lowered his gun and pulled the trigger. And his bullet tore my knee to shreds.

TYLER: (with a complete lack of emotion) (Pg 260) Our family was everything to me once. (he puts the gun to his own temple) I just don’t want to be alone anymore . . . (he fires) (long beat)

AUTUMN: (to audience – she composes herself and speaks slowly) (Pg 280) We are not better because we survived. We are not brighter or more deserving. We are not stronger. But we are here. We are here, and this day will never leave us. [NOTE: Attributed to another student, Fareed, in the novel]
```

---

## IC-0282: This Property is Condemned

- Title: This Property is Condemned
- Author (byline): Tennessee Williams
- Work: Twenty-Seven Wagons Full of Cotton and Other Short Plays
- Publisher: New Directions Publishing
- Publication date as stated: 1992
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: WILLIE
- Teaser before the introduction: Yes
- Spoken words (computed): 971
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tennessee Williams
Book: Twenty-Seven Wagons Full of Cotton and Other Short Plays
ISBN: 0811212157
Publisher: New Directions Publishing
Date(Month/Year): 1992
```

### Introduction (context only: never use it for content warnings)

```text
The Setting: Mississippi - A nowhere town with train tracks running through it. A boarding house right next to the train tracks, which now has a big sign outside saying: THIS PROPERTY IS CONDEMNED. I’d tell you more . . . but let’s face it. Willie, our main character, is a remarkable apparition – thin as a beanpole and dressed in outrageous cast-off finery. She wears a long blue velvet party dress with a filthy cream lace collar and sparkling rhinestone beads. On her feet are battered silver kid slippers with large ornamental buckles. Her wrists and her fingers are resplendent with dimestore jewelry. She has applied rouge to her childish face in artless crimson daubs and her lips are made up in a preposterous Cupids bow. She is about thirteen and there is something childlike and innocent in her appearance despite the makeup. It’s her story . . . I’ll let her tell it! This Property is Condemned by Tennessee Williams.
```

### Performance text (classify this)

```text
Willie is advancing precariously along the railroad track, balancing herself with both arms outstretched, one clutching an extraordinarily dilapidated doll with a frowsy blond wig. She laughs frequently and wildly and with a sort of precocious, tragic abandon.

WILLIE: Don’t talk to me till I fall off. [She proceed dizzily] Take my – crazy doll-will you? [Tosses doll toward audience] I don’t wanta – break her when – I fall! I don’t think I can – stay on much – longer. I’m practically - off – right now! No, don’t touch me. It’s no fair helping. You’ve got to do it – all – by yourself! God, I’m wobbling! I don’t know what’s made me so nervous! You see that watertank way back yonder? That’s where I – started – from! This is the furthest – I ever gone – without once – falling off. I mean it will be – if I can manage to stick on – to the next – telephone – pole! Oh Here I go! [She becomes completely unbalanced and rolls down the bank.]

WILLIE: Skinned my knee a little. [Spits on her knee and rubs it in] Glad I didn’t put my silk stockings on. The principal damage was done to my bracelet, I guess. I knocked out one of the diamonds. Where did it go?

[Give up looking for the “diamond” – notices audience again] My name’s Willie. I was expected to be a boy but I wasn’t. They had one girl already. Alva. She was my sister. [Looks up at the sky] It looks like everything has been swept off with a broom. Don’t it? The sky is perfectly white. It’s white as a clean piece of paper. But there isn’t a wind. It’s up too high for us to feel it. It’s way, way up in the attic sweeping the dust off the furniture up there!

I bet you’re wonderin’ why I ain’t at school. I quituated. Two years ago this winter. Grade Five A with Miss Preston. They started teaching algebra an’ I didn’t give a damn what X stood for so I quit. ‘Sides . . . what a girl needs to get along is social training. I learned all of that from my sister Alva. She had a wonderful popularity with the railroad men.

Mama actually run off with a brakeman on the C & E. After that everything went to pieces [A train whistles far off] You hear that whistle? That’s the Cannonball Express. The fastest thing on wheels between St. Louis, New Awleuns an’ Memphis. My old man got to drinking. Disappeared. I guess I ought to refer his case to the Bureau of Missing Persons. The same as he done with mama when she disappeared.

Then there was me and Alva. Till Alva’s lungs got affected. Oh, it – wasn’t like death in the movies. When somebody dies in the movies they play violins. But they didn’t for Alva. Naw. Not even a victrola. They said it didn’t agree with the hospital regulations. She was always singin’ around the house. Throwing enormous parties. This was her favorite number. [She closes her eyes and stretches out her arms in the simulated rapture of the professional blues singer. Her voice is extraordinarily high and pure with a precocious emotional timbre] You’re the only star In my blue hea-ven And you’re shining just For me! This is her clothes I got on. Inherited from her. Everything Alva’s is mine. (BEAT)

The principal at my old school used to say there must’ve been something wrong with my home atmosphere because of the fact that we took in railroad men an’ some of ‘em slept with my sister. She was The Main Attraction. The house is sure empty now. I still live there by myself. I’m not supposed to be but I am. The property is condemned but there’s nothing wrong with it. Some county investigator come snooping around yesterday. I recognized her by the shape of her hat. It wasn’t exactly what I would call stylish-looking. It looked like something she took off the lid of the stove. Alva knew lots about style. She had ambitions to be a designer for big wholesale firms in Chicago. She used to submit her pictures. It never worked out. You’re the only star In my blue hea-ven . . . .

[Notices her shoes] The freight sup’rintendent has bought me a pair of kid slippers. Patent. The same as the old ones of Alva’s I’m going to dances at Moon Lake Casino. All night I’ll be dancing an’ come home drunk in the morning! We’ll have serenades with all kinds of musical instruments. [excitedly] And the sky will be white like this. White – as a clean – piece of paper . . . . I’ll draw – pictures on it! Pictures of me dancing! In a pair of patent kid shoes! Yeh! Yeh! An’ they’ll play my favorite music! The same as Alva’s You’re the only STAR -- In my blue HEA-VEN . . . .

I’ll – wear a corsage! Flowers to pin on your dress at a formal affair! Rose-buds! Violets! And lilies-of-the-valley! When you come home it’s withere but you stick ‘em in a bowl of water to freshen ‘em up. That’s what Alva done. [She pauses, and in the silence the train whistles.] The Cannonball Express . . . (BEAT)

I’m going to live for a long, long time like my sister. An’ when my lungs get affected I’m going to die like she did – maybe not like in the movies, with violins playing – but with my pearl earrings on an’ my solid gold beads from Memphis . . . The sky sure is white. White as a clean piece of paper.

I’m going back now. To the watertank. An’ start all over again. Maybe
I’ll break some kind of continuous record. Alva did once. At a dance
marathon in Mobile. Across the state line. Alabama.
You’re the only star
In my blue heaven - (pause)
An’ you’re shining just –
For me!
```

---

## IC-0283: Through a Window

- Title: Through a Window
- Author (byline): Angela Johnson
- Work: On the Fringe
- Publisher: Penguin Group
- Publication date as stated: March 2003
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NIA
- Teaser before the introduction: Yes
- Spoken words (computed): 1729
- Already set (do not supply): none

### Source block (context only)

```text
Author: Angela Johnson
Book: On the Fringe
ISBN: 978-0142500262
Publisher: Penguin Group
Date (Month/Year): March 2003
```

### Introduction (context only: never use it for content warnings)

```text
Sometimes we think we know someone because we see him or her almost every day. Then something happens to make us realize we didn’t know that person at all. The death of a best friend is different than the death of a parent or spouse; there are no sympathy cards that quite fit the bill. There's no term for this loss and folks expect an abbreviated mourning period and offer a different, lighter brand of sympathy. It’s almost like you are living your life as a spectator . . . just watching . . . Through a Window by Angela Johnson
```

### Performance text (classify this)

```text
NIA: I don’t believe in God. Not right now. Not at this minute. But . . . When they cut Nick Gorden down from the upper stairwell outside the chem lab, a storm had just come up over the lake. You know the kind: lightning, rain, and wind that rips the roofs off buildings.

They were gentle when they took Nick away. The paramedics put him on the stretcher like he was a baby. I didn’t see the rest, the cops and all. I only watched through a second-floor window as they took my best friend away from me and here and this place . . . forever . . .

NIA: I tell my therapist that there had to be a storm the day Nick died. Something cataclysmic and ugly had to happen. If the sun had been shining, afterward maybe I would have cried and thought about how Nick just missed a day at the park. But as it happened, nature stepped in again. Somebody had to cry for Nick. The sky and his mother did that day. My eyes stayed dry.

It’s all about Nick. All of it. The therapy, the dreams, the way I can’t cry . . . Nick’s favorite song was the old Sly & the Family Stone tune called "Everybody Is a Star." He sang it all the time. (sing lines from the song here – See links to song and lyrics at the end of this selection) Wrote and tagged buildings everywhere with it, but in the end he didn’t believe it, I guess. It was the song Nick’s uncle was singing right before he died in Vietnam. Nick’s mom got all her brother’s belongings - clothes, records, dog tags - from one of the guys in his platoon.

It used to drive me crazy listening to those old records with scratches and jumps in them, but Nick said the scratches were in his head - he knew every one of them and they were like old friends. I never told Nick those records bothered me. Now I wished I had, ‘cause at least it would have been one more conversation we had had.

I used to be envious of Nick, ‘cause he was the person that everybody said hello to in the halls. He always smiled and seemed to sail along halls that had nothing but fear in them (to me, at least). In class pictures he always smiled. In his family pictures he always smiled. I overheard his mom on the phone once call him sweet and good-natured.

But I found out something about Nick a week before he died that got me all turned around, and I’d known Nick since first grade. We had been each other’s one and only friend since he’d followed me under the monkey bars after I stolen Josh Neil’s lunch. Nick had crawled under and sat behind me while I munched. He stared at me until I gave him a Fruit Roll-Up to go away. He ate it, kept staring, and stayed.

The next day the same thing, only this time I’d taken pudding out of Heather Longchamp’s backpack ‘cause she’d sat on me in front of the whole first grade. Plus she always had butterscotch. We finally got caught a week later. My mom dragged me out of the office mumbling that I was already a criminal.

Nick told the principal he’d taken the lunches and I said I’d taken them. Okay, we were tight; so why didn’t I understand that even though Nick was somebody people smiled at and waved to, nobody knew anything about him? Sometimes they couldn’t even remember his name. Nick said it. He was the invisible man.

The week before they took him out on a stretcher with his face covered, Mr. Miles (in civics class) couldn’t remember his name or that he had even been in that class. I think Nick could have taken that if Heather (no longer eating pudding--- a definite anorexic) hadn’t started laughing that he’d been going to school for years and nobody ever knew his name.

I wanted to hit her. Break those skinny, skinny cheerleader arms and that big-toothed smile she only used to torture people. Everybody laughed but me and Mr. Miles, who just looked confused and a little sorry he’d opened his mouth. Nick was even laughing. I spent the rest of the day with a stomachache, not able to look Nick in the eye. Later that night he laughed that invisible people had to have a sense of humor. I didn’t think that was funny.

I wasn’t invisible myself. I was just visible enough to be let out of conversation purposely - just visible enough to be picked on for my bad skin, nonexistent fashion sense, and biggest crime of all: I was smarter than anyone in my class and I had the nerve to be female.

(Long beat)

I went over to Nick’s house after the police and [everyone] had gone back to their lives. At first I was going to knock on the door, but then I couldn’t face Miss Gorden. Her eyes would be puffy, her face tired and sad, her body drooping. I climbed into the open hall window on the side of the house. It’s the way me and Nick came in most of the time anyway.

I could hear Miss Gorden crying two rooms down. She sounded like a little kid. I almost started crying too. That would have been a good thing. That would have helped. But instead, I just ducked into Nick’s room.

His baseball and Greenpeace posters jumped out at me and stabbed me in the heart. I used to listen to guys at school talking basketball as Nick’s eyes glowed. I’d think: This time he’s going to say something, talk about what happened in some game somewhere. But he never did, and none of the group ever asked. I curled up on the bed and in a minute was asleep. When I woke up a few hours later, the sun was going down and Miss Gorden must have come in and taken Nick’s favorite blanket off his chair and covered me in it. I put it over my head and inhaled Nick, then crawled out the way I came in and walked the street-lit sidewalks.

At breakfast yesterday my dad said, "Do you want to go to another school?" I bit down hard on my apple without looking at him, then slurped my orange juice so that I couldn’t hear him if he asked me again. He asked again. So I grabbed a piece of toast and hoped it was as loud as the apple had been. He shook his head and looked at my mom, who was looking again for signs that I was so depressed I’d go the way Nick had. Finally, though, they started picking up the breakfast dishes and left me alone. I’d have to get used to alone.

I stood beside Miss Gorden when they put her son in the ground. I fought the urge to scream when the casket was lowered. I should have screamed. There were eight people there: Miss Gorden, my parents and me, the school principal, and three people that I’ve never seen before. Again, I wanted to scream. Nobody from school came. Not one classmate. Not even to get out of those halls from hell. Everyone cried but me.

When the service ended, Miss Gorden turned on the [CD] she’d told me to bring. She sat next to Nick’s grave and smiled as "Everyone Is A Star" echoed through the cemetery. And all I could think as I got into my mom’s minivan was that Nick probably wouldn’t even be mad that the last time he heard his song it was on a CD.

For a week, the halls and classes got quite when I walked through them. It was like I was carrying a plague that would only infect others if they talked around you. They all just stayed away.

The second week, though, it started. The questions: Why? And why there? Did I expect it? Did he talk about it? I would swallow what I wanted to say and never answer. Did they want me to put in a paragraph or less (while looking appropriately sad) how someone I loved more than anyone on the planet had lived his life, then ended it? Especially to people who couldn’t give a damn whether he lived or died before. Had most of the pack creatures ever held a single conversation with Nick? Had any of the ones who ask me "How come?" been in a group who had screamed out "Do it!" as Nick was about to let go of the rafters and swing like a rag doll in front of them? I lasted three days in school.

Nick had been happy his whole life. He’d never had a bad day, I thought. He never seemed miserable or lonely, ‘cause he had me. I thought he never minded that he was invisible. I’d always believed he never wanted to be like them, having basketball conversations and talking about what they did the night before. I guess that I was wrong about it all.

Wrong that he never minded that they thought he was a sad case ‘cause his best friend was a girl with bad skin who couldn’t form a social sentence. Wrong that it didn’t make him sad the person he identified with most was a boy who’d died thirteen years before he was born, fighting a war that shouldn’t have been. At thirteen when Nick found out about reincarnation, he decided his uncle had come back to the world as him. He really believed it. Believed it in his soul. Believed it more than anything he’d ever thought in his whole life, even believed it more than the thing about him being invisible.

[Now] I watch the world through a window of [a] Psychiatric Clinic for Adolescents, and the world only comes in and bothers me when I want it to. I’ve decided that it’s not such a bad thing to be invisible. The thing that you have to be careful of, the thing that Nick never learned, is that you can’t want to be anything else. You can’t want to have more people who care. You have to be invisible on your own all by yourself. You can’t even have a friend like me who loves you and thinks you’re better than anything else.

(sing lines from “Everybody is a Star” here – See links to song and lyrics at the end of this selection)

Nick got it wrong. Everybody isn’t a star. . . maybe in a better world they could be. They could be. They really could be . . .
```

---

## IC-0284: The Thumbprint of Mukhtar Mai

- Title: The Thumbprint of Mukhtar Mai
- Author (byline): Susan Yankowitz - based on conversations with Mukhtar Mai
- Work: Seven (Pg 117)
- Publisher: Dramatists Play Service
- Publication date as stated: Oct 2009
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MUKHTAR
- Teaser before the introduction: Yes
- Spoken words (computed): 1988
- Already set (do not supply): none

### Source block (context only)

```text
Author: Susan Yankowitz
Book: Seven (Pg 117)
ISBN: 978-0822223511
Publisher: Dramatists Play Service
Date (Month/Year): Oct 2009
```

### Introduction (context only: never use it for content warnings)

```text
The Thumbprint of Mukhtar Mai by Susan.Yankowitz, based on conversations with Mukhtar Mai.
```

### Performance text (classify this)

```text
MUKHTAR: My great-aunt had the honor of naming all the children in my family because she had none of her own. She called me Mukhtar, which means "powerful" or "self-respecting" and that always was strange for me, because I am very thin, and in my culture, a thin person is considered weak. My village is Meerwala in the southern part of Pakistan, one of the poorest areas in the Punjab. We are from the Gujars, a peasant tribe of low caste. I lived with my mother, father, four sisters, and two brothers. Like other girls, I played with dolls, climbed trees, and swam in the canal.

My village had no school, and no one in my family could read or write. I learned the same things my mother had learned, and her mother before her: how to do housework, fetch water from the pump, put the younger children to bed. I did not know that in other places, not so far away, girls were being educated. I was not unhappy because I did not realize I had been taught nothing about the world.

(Pause as she visibly thinks; then change of tone.) No, no, I WAS taught something . . . all girls were; I was taught silence, I was taught fear. I was taught that some people are high up and some are low down - and that my caste, my family, were at the bottom. I was taught to hide my face and bow my head, to say "yes," "yes," even when I felt "no" in my heart, to obey my parents, and stay away from boys.

MUKHTAR: [When] I was twenty-eight years old, some men of the Mastoi tribe come to our home and say that my twelve-year-old brother, Shakur, has committed zina with a girl from their clan and must go to jail. This crime they put on Shakur means rape or sex before marriage, and by the laws of Sharia it is punished by death. We are sure this is false. But what can we do? The Mastoi are a higher caste than we are, they are landowners, so whatever they say is law.

The men of the jirga, our village council, meet to discuss the situation, and finally we are told that I, Mukhtar, must ask forgiveness for my brother. If this will satisfy them, if this will free my brother from their hands, I am happy to do it. (Gets Quran, begins her walk.)

It is twilight when I begin walking toward the farm of the Mastois, holding my prayer book to my breast. I am not afraid. I have done no harm to anyone. With my father and uncle, I travel the dirt road and enter the Mastoi compound. The clan chief, Faiz Mohammad, and four other men are standing there with rifles.

(Kneeling.) I spread my shawl on the ground to show submission and silently recite a prayer: Praise be to God, Lord of the Universe, Thee only do we worship and of thee only do we ask help ... (raises her head and speaks clearly) If my brother has offended you, I ask pardon for his action and beg you to set him free.

Faiz shouts to his kinsmen: "There she is. Do what you want with her." Four men pull me by my hair and arms and drag me into a dark room. I am thrown onto a dirt floor ... a stable. The only animals there ... the only beasts! ... are those men. For more than an hour, I am raped by men of the Mastoi tribe. My father and uncle could do nothing for me. Men with shotguns force them to wait outside. They must have known what was happening, but they had no power.

Every woman, from the time she is a little girl, walks in terror of what happened to me. By the time we are eight years old, ten years old, we know that a man can grab us whenever he pleases and take us to some evil place where he will push us down ...

break into our bodies ... destroy our childhoods and our futures.

When the men are finished with me, I am thrown outside. My uncle and father help me to my feet and support me to walk home, past hundreds of townspeople. No one says a word as I pass by; they all lower their eyes or stare at me with disgust. Now I am unclean and dishonored - in the eyes of the tribal elders, my family, and the villagers.

For the next few days no one talks to me about the thing that happened, and I say nothing. In my country, women do not share such disgrace with others. People will spit on me, on my parents and sisters ... I can spare everyone that misery by killing myself, I think; it might even be a relief for them ... (Growing agitated.) In Pakistan, staying alive is seen as more cowardly and shameful than the rape itself. I understood that the shame was not mine, but, I felt ashamed. I knew I should go on living but I felt so miserable that I wanted to die. But if I didn't die, what would I do with my life?

One idea kept pushing away the others: I could try to help the women of my country. Yes, maybe that was possible ... Because I knew that what happened to me was not God's will. Nowhere does the Quran approve of violence against women! So why do men act in such ways? Because women in Pakistan have no value and cannot bring their attackers to justice? Because we are too weak to fight back?

(Calming) So this is how I was thinking when I learned that my rape was not just an evil plot of the Mastois but had been ordered -- ordered! by the most honored men in my village, the tribal elders - (Increasingly furious.) The tribal council had declared that I should be gang-raped as punishment. An "honor revenge”, they call it! How could they reach such a terrible decision? How?!

So l see I have no choice. I must stand up alone for myself. My mind was made up. I was ready to speak out. (Again she begins to walk.) Eight days after the rape, I travel the many miles to the police station in Jatoi. My father could have tried to stop me but no, he walks steadily beside me.

The policeman is sitting at his desk when I enter. He says, “We already know what happened. See?" and shoves a piece of paper at me. Words are written on it, but I do not know what they mean. How can I deny his report or defend myself? "Sign here and we will fill in the particulars."

My face burns red, I am so embarrassed that I do not know how to write my name. But he just laughs. "Use your thumbprint, like the other women. And he presses my thumb on an inkpad, then onto the bottom of the blank page. I have no idea what statement will appear above that signature.

This is when I realize why we must have knowledge. If you are educated, you can understand what is happening and fight for your rights. But when you are illiterate, you are like a dumb animal, so how can you stop the terrible things that fall down on you?

And the next morning, what a racket wakes me up! The dog is barking, chickens are squawking in the yard, reporters call out for me, women's groups, civil rights groups from all over the world ... ! The Pakistan Human Rights Commission has demanded a full investigation, and the press is supporting my lawsuit. Everyone wants to hear my story, because this is the first time that tribal elders in Punjab province have authorized a gang rape and the first time a woman is taking her case to court.

And from these strangers I learn about other violence. In Lahore, a woman asking divorce from a husband who beats her was murdered in her lawyer's office. A teen-aged girl's nose was cut off to punish her for holding hands with a boy from a neighboring tribe. Acid was thrown in the face of another girl who refused to marry an old man chosen by her family. In a village near Sukkur, three brothers burned their sister-in-law alive because they claimed she had been unfaithful. And always, always, it is a matter of honor! No one seems to find it strange that in all our history, only women and never a man have been punished for a so-called crime of honor!

And so I take my rapists to court, even though I hear they are laughing at the whole thing; but they do not laugh when the verdict is announced. The four rapists are condemned to death. I am told to report to a local office where I am given a check for half a million rupees - about eight thousand dollars - by a government minister - a woman!

"I don't need money. I need a school. A school for girls. We are so ignorant, we know nothing of the world. Girls must learn how to sign their names with a pen instead of a thumb. They must learn to read, to write, to know their rights as citizens. Help me. Help me to build a school." She says it is fine to use the money any way I choose. And so begins my new passion, my mission in life.

I hire a teacher and set up the school in a field of wheat and cotton. I start with only three, but every day more little girls turn up with their notebooks and pencils. They learn the usual subjects. But we also teach them that women are equal with men. All of us are human beings and we all must be treated with respect in society. And we read to them what the founding father of my country, Mohammad Ali Jinnah, said in 1944: "No nation can rise to the heights of glory unless its women are standing side by side with the men. It is a crime against humanity that our women are shut up within the four walls of the houses like prisoners."

Me, I don't cry anymore. And each morning when I rise, I thank God for the rewards of living. l have now opened three schools in Punjab province and they are for boys as well as girls, because boys too must learn that under Islam, under the law, women have the same rights they do. And in Meerwala, where I almost killed myself, I have built a real schoolhouse, with a library and six classrooms. The children come from many tribes, from low and high castes girls from the Gujars and even boys from the Mastois! We teach more than two hundred and sixty boys and four hundred girls.

And I am one of those girls. I was the first student in my own school, and now I am in the fifth grade. I will keep on studying but already I have learned this: Never, never will I need to use my thumb to sign my name. I am Mukhtar. Powerful. Self-respecting. Mukhtar!

CONCLUSION In Pakistan today, women are still in peril. In international news . . . On July 21, 2021, 27-year-old Noor Muqaddam was brutally tortured and beheaded in the nation’s capital – her crime, refusing to marry her murderer, Zahir Jaffer. The courts have yet to decide on the merits of the case.

And yet Pakistan is ranked only 6th on the scale of most dangerous countries for women. How can this be? The Human Rights Commission of Pakistan recorded 430 cases of honor killings in 2020 and during the first 4 months of this year, in Punjab alone, police have registered 53 cases of gang rape.

Education is a start, but Pakistan remains a culture that de-humanizes the female gender. And as long as this is so . . . Pakistan will continue to fail its women.
```

---

## IC-0285: The Towel Lady

- Title: The Towel Lady
- Author (byline): Janet S. Tiger
- Work: The Scenebook for Actors: Great Monologs and Dialogs from Contemporary and Classical Theatre, Pg 45-48
- Publisher: Meriwether Publishing
- Publication date as stated: June 1990
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: THE TOWEL LADY
- Teaser before the introduction: Yes
- Spoken words (computed): 683
- Already set (do not supply): none

### Source block (context only)

```text
Author: Janet S. Tiger
Book: The Scenebook for Actors: Great Monologs and Dialogs from Contemporary
and Classical Theatre, Pg 45-48
ISBN: 0916260658
Publisher: Meriwether Publishing
Date (Month/Year): June 1990
```

### Introduction (context only: never use it for content warnings)

```text
How do you know if you are better off staying married or getting a divorce? Sometimes a marriage is worth saving and sometimes it isn't. Sometimes people keep trying to make sense out of something that doesn't make sense or can't be solved. If you throw in the towel, you stop trying because you have found that you won't succeed. More than 50% of marriages in the United States today end with one or both partners throwing in the proverbial towel. The most common conclusion is divorce; but, of course, there are always other alternatives . . .

The Towel Lady by Janet S. Tiger
```

### Performance text (classify this)

```text
A woman comes onto the stage with a basket of laundry, which she puts down heavily. Then she takes a towel from the basket, and she stops, turning to the audience, holding the towel in a kind reverie.

THE TOWEL LADY: (Pg 45-48) You know, a new towel is a wonderful thing. Come on, you ladies all know what I’m talking about! Now, I can understand why the men are muttering to themselves, because no man can appreciate a good towel. But you ladies know what I’m saying is true! Only another woman knows what I’m talkin’ about. (She holds out the towel to illustrate)

Isn’t it beautiful when it’s brand new? It’s so soft and good smellin’. It has a youthful way about it, kinda sassy, but innocent. You men are sittin’ there wonderin’ why the hell you came to listen to some old woman talk about the laundry, but if you listened for once in your lives, maybe you’d learn something.

See this towel? I just bought it today. It ain’t never been touched by any hands ‘cept mind. Well, maybe somebody touched it in the store first, but since I didn’t see it and it didn’t leave no mark, it don’t matter. (beat)(Examining edges) It’s perfect. I never buy those “seconds” with their funny lines down the middle and the frayed bottoms. They don’t last as long. I buy one hunnert per cent thick cotton Cannon towels made for J C Penney. The thirsty ones. (beat)

Men never did understand towels. And that’s because they treat their towels just like they treat their women. Here’s this beautiful towel which I’ll put carefully onta my towel rack. And I’ll be real sure that my hands are washed clean when I use it, so’s all that gets on it is water. (beat)

(She turns ornery) But a man’ll come in from working on some greasy car for three hours and he’ll. . . he’ll (She can barely bring herself to say the words) . . . he’ll take those greasy, filthy hands and put them onto that clean, pure towel.. and. . . and that towel will never be the same! No matter how I wash that towel with soap, that dirt gets right down into the fibers. And if I bleach that towel, all the newness comes right out with the grease!

And once that towel is besmirched, I dunno, it’s downhill from there. But even though that towel isn’t pure no more, it lasts and lasts, and that man puts more and more greasy dirt onto it, and I bleach more ‘n more of the life outa it (beat) But just like a woman, it keeps doing what it has to do. Not complainin’, just sittin’ there. Until one day there’s a hole in it. Not a big one, mind ya, but it’s there. When you point it out to them, they just say, (She imitates a man’s voice) So what? Lotsa good use in it. . .

(Back to herself) But you can’t put it out fer company no more. Naw, it gets put to the back of the closet, to be used for wipin’ babies and cleanin’ up after the dog. (beat) And then one day, (She shudders to think about it) you go to get the towel to wipe up some jam that spilled onta the carpet, and it’s gone.. You can’t find it nowhere. You take all the other towels out, but there ain’t hide nor hair of it.

So you ask him (Sweetly). Honey did you see that towel, the one with the pretty yeller flowers on it? And he says, (Imitates man’s voice) You mean that old faded thing with holes in it. (Back to herself) And that’s when you know the truth. You go out to the garage, and there ya see it, hanging on a nail, just like Jesus. And it’s just not mildly stained anymore, it’s COVERED with disgusting marks that you don’t even want to know what the origins were. And you look at that poor, faithful towel, and it’s enough to make your heart just bleed! (beat)

(She’s quiet now and holds the towel like a baby.) And so you go inside to your husband’s desk, and you take his thirty-eight, and you shoot him right through the heart. (A pause to let this sink in, then she is cheerful again.) (Beat) And then you wait for the police to come and get you. (Put down towel carefully, reverently. We hear a distant voice, calling from offstage. She listens, then responds to the voice.)

I’ll be there in just a minute, Officer Williams. I just have one more thing to hang out. (She takes the last shirt out of the basket and hangs it up. It has a hole in it surrounded by a big red stain. She turns to the audience and smiles, then takes the basket and walks offstage.)
```

---

## IC-0286: Train Story

- Title: Train Story
- Author (byline): Adam Rapp
- Work: The Best American Short Plays 2000-2001
- Publisher: Applause Theatre Books
- Publication date as stated: 2002
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: WOMAN, GIRL
- Teaser before the introduction: No
- Spoken words (computed): 1034
- Already set (do not supply): none

### Source block (context only)

```text
Author: Adam Rapp
Book: The Best American Short Plays 2000-2001
ISBN: 1557834806
Publisher: Applause Theatre Books
Date (Month/Year): 2002
```

### Introduction (context only: never use it for content warnings)

```text
On a cross-country train trip, an upper-middle class woman makes a strange connection with a pregnant teenager. Lori is an editor, and she is working on a particularly tiresome manuscript when Exley barges into her train car looking for drugs. Exley is about three months pregnant, and she is mad as all get-out that her boyfriend Morris hasn’t met her on the train like he promised. Exley is obviously drunk, and the other passengers are afraid of her. When no one produces drugs for Exley, she pulls out a nail file that she calls a knife to threaten the passengers, and someone calls the conducter. The conductor knocks Exley to the floor of the train, and then handcuffs her to the seat across the aisle from Lori. The Train Story by Adam Rapp begins.
```

### Performance text (classify this)

```text
WOMAN: The girl’s nose is bleeding. I offer her my silk scarf. It’s an expensive scaf, Hermes I think, but I don’t mind. After all, it’s the holiday season. She takes it ans stares at it appraisingly. For a moment I think she might stuff it in her pocket, but she balls it up and presses it into her face. I say, It’s silk but don’t worry about it. Are you okay?

GIRL: Three hours I waited for him. Three hours!

WOMAN: Who were you waiting for?

GIRL: Morris

WOMAN: Is that your boyfriend?

GIRL: Yeah

WOMAN: Is he the . . .

GIRL: The what?

WOMAN: Well, the father (no response . . . My name is Lori . . .. Lori Lansky

GIRL: Cool . . . Exley . . . . Yo, Lori Lansky, you got any pain relief?

WOMAN: I have aspirin. I reach into my purse and remove a small bottle of aspirin. I unscrew the top and hand her a few. While she’s swallowing them, I realize that it’s not her nose that’s bleeding. Are you oaky?

GIRL: Why?

WOMAN: Well, it looks like you’re losing some blood. We are quite. I mind my business. Out the window, the black fields have turned white. Somewhere along the way it has started to snow. Silently. Invisibly. The sun has fallen so fast it’s as if the earth has slid on its axis. I look over and notice that Exley’s lap is completely red now. Absurdly so. Like something from a horror movie.

GIRL: Yeah, go ahead and judge me lady. WOMAN; I say, I’m not judging you. I am thinking, Don’t judge her, Lori. Don’t you dare judge her.

GIRL: You think god’s gonna get me, don’t you, Lori?

WOMAN: I wasn’t thinking that at all.

GIRL: Yes you was. I can tell. Like he really give a dam. He too busy helpin’ all the rich people.

WOMAN: I don’t think God operates like that.

GIRL: Operates. Oh, he a surgeon now?

WOMAN: I don’t think he discriminates according to economic stature. He’d be too dependent on the IRS. I think he exercises far mor subtlety . . . I’m not judging you, Exley. She looks at me with a kind of hunger. The way animals beg for food with their eyes. With this look I realize that she’s much younger than I thought. Her skin is too fragile. Her cheeks too soft. She may be fifteen, sixteen. For some reason, I ask her if she believes in God. Do you believe in God, Exley?

GIRL: Not really. I mean, when I used to see Jesus in those Easter movies I thought he was cool. Like how he walked on water and whatnot. There was this one where he turned all this bred into tropical fish. That was pretty dope . . . Why, do you?

WOMAN: I don’t know.

GIRL: What do you believe in, credit cards? Fancy clothes catalogs?

WOMAN: I believe in luck, I guess.

GIRL: That’s prolly why you don’t fly. Luck

WOMAN: It’s true. I have this fear that things would go bad for me on a plane. That I’d lose myself somehow.

GIRL: That how I feel about trains. I kept tellin’ Morris we shoulda drove. He just bought a ’99 BMW.

WOMAN: Is Morris the father?

GIRL: I think so.

WOMAN: Where were you two planning on going?

GIRL: I don’t know. Somewhere west. Like the ocean maybe. Swim with the starfish. Chill with the electric eels. He said he had a partner out there. On some beach with an Italian name.

WOMAN: Venice Beach. Well, wherever you wind up, I wish you luck, Exley.

She doesn’t respond. It’s as if I’ve stung her. Sure, an overly educated, more fortunate white woman in designer clothes can just throw Luck around. It’s a mild luxury like potpourri or expensive soap.

When the conductor re-enters I tell him how Exley may be hemorrhaging from her uterus and he calls the paramedics on his walkie-talkie. She is staring out the window as if there is something in the barren fields that will pardon her. As if there is a fairy tale about poor white girls that has yet to be written.

We lock eyes for a moment. Bravely. Somehow longingly. I never used to believe that strangers shared these kind of moments. In real life these exchanges are simply anecdotes. It’s never about yearning or frailty or pure, wordless human contact.

By the time the train stops in Indiana Exley has lost consciousness. There is an enormous volume of blood pooling in her lap When the doors open there are policemen. There are station managers. There are paramedics as silent as aliens. Far too many men to move the body of a small, lifeless girl.

I tell one of the paramedic that I think it’s a botched abortion. I give him the number of where I’m staying and ask him to call me. To let me know if she makes it through.

A few weeks after I get back to New York I start to feel sick in the mornings. I think I must have gotten a bug from traveling. Something from the other coast. Three weeks later I miss my period. I buy an over-the-counter pregnancy test. It turns out positive.

I’m two months along now. My appetite has changes. I have told no one. Not even the father. I often think of Exley. That paramedic never called me. I don’t recall what she did or said so much as her will. How it burned through her skin. That lost white orchid. Did she make it through? Did someone find her at the hospital? A priest? A policeman? Is she wandering the snow-swept highways of Indiana? There are certain hors of the night when I wake to the sound of a train. It roars right through my apartment. At times it feels as if it will life me out of bed. All that earsplitting thunder and then silence. A quiet that can’t be captured in prose or likened to certain kinds of weather. A calm that defies even thought. Just the purest absence of noise.

Perhaps souls have the ability to leap from womb to womb?

I am alone, Exley. I am very much alone in a city that at time makes people feel old and used. But I am somehow lucky. Even during the darkest hour I manage to always pull through . . .
```

---

## IC-0287: Twist

- Title: Twist
- Author (byline): Cora Sorenson
- Work: Fast Horse Plays - Round 6, Pgs 23-31
- Publisher: Create Space Independent Publishing
- Publication date as stated: May 2015
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SAMANTHA, MRS. B, RICKY
- Teaser before the introduction: Yes
- Spoken words (computed): 1953
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cora Sorenson
Book: Fast Horse Plays - Round 6, Pgs 23-31
ISBN: 978-1512244120
Publisher: Create Space Independent Publishing
Date (Month/Year): May 2015
```

### Introduction (context only: never use it for content warnings)

```text
Twist by Cora Sorenson
```

### Performance text (classify this)

```text
Samantha, 17 or 18, is intelligent, well-spoken and charming. The short vignettes are reenacted with the single performer embodying the persona of the other characters.

SAMANTHA: (Pg 23-31) (singing) * I never meant 2 cause you any sorrow. I never meant 2 cause you any pain. I only wanted 2 see u laughing in the purple rain. I only wanted 2 see u baby in the purple rain.

Every good story ends with a twist. Well, at least in my opinion they do. Who wants to read a novel where you spend so many hundred pages getting to know the characters, actually end up caring about them and then . . . Bam! They just end up doing what people would do in real life. Or you shell out nine bucks for a movie and by the time the two hours is up, somehow, magically, everything works out perfectly. Boy meets girl. Girl gets pissed off at boy. Boy goes to extraordinary means to get girl back. Girl forgives boy and they ride off into the sunset. Sure. People in real life do what we expect them to do. Always. We escape into entertainment hoping something different will happen. So, that's why I decided I'd make sure my story would have a twist at the end. Maybe I've ruined the surprise by announcing it upfront; but, sometimes, for things to make sense, you have to start at the end of the story.

SAMANTHA: There's a zillion different places where the story could start. I mean, I could go back to how my parents met at their Ivy League schools, fell madly in love (supposedly), made all sorts of money in the professions of medicine and law and then decided to have me. But I’m not going to start with that. I'm going to start with Fluffy, Mrs. Butterbutt and Samantha. Fluffy was my loyal hamster when I was five. Mrs. Butterbutt was my kindergarten teacher. And, in case, you haven't figured it out, I’m Samantha. So, anyway, I adored Fluffy and I hated Mrs. Butterbutt. Fluffy was always there to listen to all of my problems and comfort me -- everything anyone could ever want in a hamster. Mrs. Butterbutt, on the other hand, was an old cow who appeared to exist only to make my life a living hell. For example: (re-enactment – age 5)

SAMANTHA: The other girls are being mean to me again, Mrs. B.

MRS. B: You have to kill them with kindness, Samantha, dear.

SAMANTHA: I have to kill Andrea and Melissa?

MRS. B: No, no, no, dear. You have to be nice to them, even when they're mean to you.

SAMANTHA: Even when they call me ogre, giant girl or redwood tree?

MRS. B: Yes, dear, even then.

SAMANTHA: But Mrs. B didn't have to spend day in and day out with Andrea and Melissa. Mrs. B didn't have to walk around being twice as big as all the other little girls. You don't get called "redwood tree" for nothing. She pretended to be a nice old lady, but really she was meaner than the witch from Hansel and Gretel. And no, the twist isn't that I baked Mrs. B in an oven.

So, back to Fluffy. One day I come home from kindergarten hell to find Fluffy with four feet in the air. Traumatizing, let me tell you. Mom and dad explained how Fluffy was very old for a hamster and had gone to hamster heaven. I got all that, I was a bright kid. But the thing was, why hadn't Mrs. Butterbutt gone to kindergarten teacher/wicked witch heaven? Cuz she was really old. Really, really old.

So, the years passed like the middle pages of a long novel. The ones you only skim through and don't really read because you're trying to get to the end . . . to the twist. And we get to the part of the narrative where I'm in high school. Some time in high school, I think girls make a decision. They either decide they are going to devote every moment of their time to obtaining that holiest of holies - a boyfriend - or they are just going to resign themselves to never having one. I decided that having a group of friends (some of whom happened to be reasonably cute boys) was good enough for me. Until the spring of my 11th grade year when Ricky asked me if I would go to the junior prom with him. Sort of like this:

RICKY: Sam, would you go to junior prom with me?

SAMANTHA: Pardon?

RICKY: You know, the event where everybody gets dressed up, dances, eats and sneaks out to go drinking afterwards?

SAMANTHA: yeah. Umm, as friends, you mean?

RICKY: Samantha! As my date!

SAMANTHA: Okay, cut. I'm a big girl, but not an idiot. Sorry to disappoint, but I did not go through any low-self esteem crap, self-loathing, etc, etc. I just said yes. Ricky is about an inch shorter than me, varsity swimmer, and, umm . . . Has these blue eyes. I'm trying to think of some poetic description . . . They're just these clear, blue reflections . . . Like you can see yourself there when you look into them.

So we went to prom. And then we started doing this thing that all my friends had been doing for awhile. Teenagers in the wild call it "dating." For a while, I was really suspicious. Like, this was going to turn out just like one of those movies where the girl gets to date the gorgeous guy for a while only to find out she's the victim of some bet. But, the more Ricky said to me, the less suspicious I was. So, we went to the lake together and swam.

RICKY: I like your smile.

SAMANTHA: He took me to a comedy show and actually paid.

RICKY: I love your laugh. Don't ever stop laughing.

SAMANTHA: We ate Lebanese food and he gave me a ring he'd made in metal shop.

RICKY: I was waiting for you, Samantha.

SAMANTHA: We laid out on a blanket, drank apple cider from the same thermos and he kissed me.

RICKY: I think I'm falling in love with you, Sam.

SAMANTHA: I always thought "love" was the worst cliche of any novel, of any stupid teen movie. But maybe we think a lot of things are stupid until we understand what they are. I probably sound like a big giant cliche with extra cheese right now, and I don't even care. My heart started to feel. And I fell in love with Ricky. My parents were overjoyed. Parents never see the flaws in their kids, not ever, so I guess they couldn't understand why I hadn't been snatched up earlier.

About a year after the prom, Ricky and I were going to spend the weekend at my parent's lake house. We were excited, ya know, graduation was only a couple of months away. On Saturday afternoon, though, I had to drive back to town to study for my calc final with some friends. Ricky decided to stay ... He was going to swim, study, whatever. I thought I'd be gone ‘til the evening, but Deidre had a headache and we cut studying short. I drove back, and, you know, I didn't think anything of the car outside the house . . . Not anything . . . Just figured he'd invited someone over. I walked in the front door, and Ricky was there with Kristy, a cheerleader, and, uh, their clothes were off, strewn across the floor. . . uh . . . I didn't say anything, really. Ricky's eyes, though, his blue glacier eyes, met mine and he said things. His mouth moved and sounds fell out, like lines from a movie, like . . .

RICKY: Samantha, what are you doing back? I, uh, I didn't. I didn't mean to. I, uh . . .

SAMANTHA: And I don't think I said anything back, really. I was dizzy and my heart was pounding . . . just pounding. And then I heard a car starting, wheels going over gravel and then Ricky and . . . that girl . . . were gone. I sat there for a while, very quiet, and then I went home.

I waited three days. Didn't see him. He wasn't at school. And then I called him. What you may not be aware of is that more than 3/4 of intimate relationships survive when one person cheats. I just needed . . . wanted to talk to him. And, the thing you need to understand, is that he wouldn't talk to me. And that was what started the shattering. Seeing him there, with Kristy hurt. But him not being willing to talk, to work this out -- it made me feel like my body was breaking apart. I tried to explain to him that we could work this out, but he wasn't listening ... He just kept saying

RICKY: Goodnight, Samantha. . .

SAMANTHA: Over and over. And then he hung up. (singing) I never wanted to be your weekend lover. I only wanted 2 be some kind of friend. I could never steal u from another. It's such a shame our friendship had 2 end. I only wanted 2 see u underneath the purple rain . . .

So this catches us up to right this very instant. With me standing on the deck of my parent's lake house. No, this isn't the part of the story where you start to feel sorry for the girl who was made fun of her whole childhood only to get dumped by the first boy she really loved. Don't you dare feel sorry for me. If you do, you're missing the point altogether and you won't get the twist.

All he had to do was talk to me. That's all. And he wouldn't. If this was a movie, I would eventually get over it. Or, in some fantasy, he and I might even get back together. But this isn't those things. This is my life.

Ricky is inside now -- Just a few steps away. After all these times of me asking to talk, he finally agreed. Said he would give me an hour tonight. But the time is up. The chance is over. Like a chemical reaction that's expired. No talking tonight. . . no.

I think I told you that my father was a physician, right? I think I did. You may not be aware, but there's a drug called "Vionox"- a drug that paralyzes the body but keeps the person alert. I lifted some from the hospital, and Ricky is inside there now, experiencing the effects. He's lying very still, his blue eyes wide open but he can't move.

I didn't want to struggle with him. I'm a big girl, after all, but he's strong. (picks up a bat, or sledgehammer from the deck, swings it) What you may not be aware of is that the human skull and the brain can sustain between four and six direct hits with a heavy blunt object before it gives up . . . expires. (beat) I am not a tragic heroine. I refuse. I will never be made fun of again, by the girls in kindergarten, by Mrs. Butterbutt, by Ricky - the boy who has no heart. (beat) Every action has a consequence. In a book or a movie, I would get over all of this . . . But I decided my story would have a twist. Did you see it coming? They say there's only so many plot lines, you know. (beat)

Afterwards, maybe I’ll call the police. Or my mother. She's an attorney, remember? She's always told me, "It's not about whether or not someone did something bad, just whether or not they have a lot of money. Justice is very expensive."

Maybe I'll say he tried to rape me or attacked me first. I'll decide something. (beat) I have to go now. I have to tell Ricky goodnight. (sings as she exits) "Honey, I know times r changin'. It's time we all reach out 4 somethin' new that means u 2. U say u want a leader But u can't seem 2 make up your mind. I think u better close it and let me guide u 2 the purple rain."
```

---

## IC-0288: Two Rooms

- Title: Two Rooms
- Author (byline): Lee Blessing
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Dec 1990
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: LAINIE, ELLEN, WALKER, LANIE, MICHAEL
- Teaser before the introduction: Yes
- Spoken words (computed): 1610
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lee Blessing
ISBN: 978-0822211839
Publisher: Dramatists Play Service
Date (Month/Year): Dec 1990
```

### Introduction (context only: never use it for content warnings)

```text
*According to the James Foley Foundation and recent White House Statements from President Joe Biden regarding American hostages in Gaza, as of January 14, 2024, nearly 70 U.S. nationals are known to be held hostage or wrongfully detained in at least 15 countries. (update as needed) Over 90% of these cases are wrongful detentions that interfere with U.S. foreign policy and national security. Of those hostages, six have been held for over 10 years.

Written in 1990, this selection deals with a subject still very much in the minds of contemporary society – the taking of innocent hostages by political terrorists, the agony of the detainees and the helpless fury of those who are left behind – loved ones impatient for something to be done and officials who have a larger political agenda in mind.

Two Rooms by Lee Blessing
```

### Performance text (classify this)

```text
LAINIE: (Pg 16) (an empty room, she is clearly seeing a different time and place) A hotel in Beirut near where we lived was destroyed in some shelling a couple of months before . . . before he was taken. (beat) (Pg 8-9) I’m talking to myself. All last night, taking the furniture out of this room, I was talking to myself. For the last year, what else have I been doing? Talking to everyone in power – which is, of course, the definition of talking to yourself. The Arabs wouldn’t help me, but at least they’d resect the pain. In Washington, I was the pain. (beat) (Pg 10) The government’s coming today. [Someone] attached to me. My case.

ELLEN: (Pg 12-13) The most important thing to remember is that we're not speaking of a country of terrorists here. We're barely speaking of a country at all. We're speaking of factions. Some friendly to Iran, some to Syria, some to Israel, some to us. They're all fighting for power. For all we know your husband -

LAINIE: Michael.

ELLEN: Michael may be liberated by a faction that favors us. The crucial thing – is knowing that hope is a real and present possibility.

LAINIE: What are the chances?

ELLEN: There are pictures. We have pictures of Michael. Taken just a month ago. Pictures of him alive.

WALKER: He had the s*** beat out of him. He was barely recognizable. It’s our Middle East policy that’s keeping your husband hostage. Nothing else.

ELLEN: (Pg 11) What have we been talking about for the last year, Lanie? It’s absurd for you to talk to newspapers. We have no way of knowing what public statements by hostage relatives may do. No way at all. It could make it harder for us to secure a safe return.

LAINIE: (Pg 13) When will my husband be released?

ELLEN: Lainie – this government is using every ethical means to bring your husband back to you. (Pg 14) There are however acts of God, for example, over which no government has power.

LAINIE: You think this is an act of God?

WALKER: (Pg 13) This government wouldn’t care if your husband died. Because then he’s not a problem anymore. Have you ever wondered why other governments can get their hostages out and we can’t?

ELLEN: They pay ransom.

WALKER: And it works!

ELLEN: Either he goes – right now – or I do. (beat) Lainie? (a glimpse of irritation crossing her face. She exits)

WALKER: (Pg 19) You understand what’s really going on.

LAINIE: What’s really going on?

WALKER: What’s really going on is that they’ll let him die. They’ve already made the value judgment. To this administration, it’s more effective to use his captivity – and even his death – to push a bunch of policy points, than it is to get him back.

LANIE: You really think that?

WALKER: I know it. So do you. The day he’s reported dead, they’ll be all over TV, pointing the finger at every terrorist in the Middle East, saying, “These are barbarians. Don’t try to understand them, just let us do what we must.” And we’ll let them.

LAINIE: What do you think I should do?

WALKER: Speak out. Do interviews. Go on TV if you have to. (beat) (Pg 20) Care about your husband. LAINIE. I do!

WALKER: [Then] do something!

LAINIE: I am! (beat) You know what will get him back? Nothing. Whatever took Michael, whatever will bring him back is a power so incomprehensible we’ll never understand it. And all the running around screaming about injustice won’t change a thing. All we can do – all anyone can do – is take pictures of mourning widows. Write stories about mourning widows. Become fascinated with widows of men who aren’t even dead yet. But nothing – nothing – will make a difference.

WALKER: Lainie, I’m only . . .

LAINIE: Get out! *****

MICHAEL: (blindfolded and in handcuffs) War isn’t a tear in the fabric of things, it is the fabric. Americans fight all the time – lots of wars. But always far away. We haven’t had to fight for the soil we stand on in a century. We’ve forgotten that level of sacrifice. These people haven’t. Everyone in this country -- Christian, Palestinian, Israeli – everyone is fighting for the ground itself. They stand here or nowhere. It’s easy for them to kill. Lanie, don’t you see? We’re not different from these people, we’ve just forgotten. *****

ELLEN: (Pg 28-29) What does it mean to be an American? Well, here it means - for most of us – “to be comfortable." Elsewhere in the world it means to be punished for the crime of having been born here and not there. Enormous numbers of people all over the world hating Americans. Willing to kill even the most innocent of us. To imprison us without trial. For years. Why? They watch our television, you know. See our films, wear our clothes, drive our cars, listen to our music. They learn in our universities. What do they learn? That they have been born in a part of the world which has no power. [And so their] only reality is to reject and destroy what they can of the Western world. *****

LAINIE: (Pg 31- 33) How’s the crisis coming?

ELLEN: You should know. You’re doing enough to intensify it.

LAINIE: That’s not what I’m doing.

ELLEN: It isn’t? Let me remind you of your phone call to me yesterday . . . (mimics Lanie’s words, perfectly) “Walker says I should go on TV. I think he may be right. Maybe this is a real opportunity to put pressure on people.”

LAINIE: I didn’t mean you.

ELLEN: Of course you meant me. You meant the State Department.

LAINIE: All right, so I did mean you. So what?

ELLEN: Lainie, we have a lot of Americans trapped with some exceedingly dangerous terrorists in a very cramped charter terminal in Crete. If you start jumping onto TV screens now, God knows what effect it will have.

LAINIE: Can’t we just wait them out? Can’t we . . . ?

ELLEN: This group likes to die for what they believe in. They’re not like a bunch of bank robbers. When terrorists take a group as large as this, everyone understand it’s a short-term project.

LAINIE: Project? Is that how you see it? What’s Michael – a long-term project?

ELLEN: Sadly, in a sense, yes.

LAINIE: Because he wasn’t lucky enough to be abducted in an airport? With a bunch of other people?

ELLEN: If you go public, if you make demands, you’ll only increase the danger for everyone involved. And frankly, no matter what you do, we won’t ask for Michael’s release. It’s not his time.

LAINIE: His time? *****

MICHAEL: (Pg 35) LAINIE!! LAINIE!! (beat, he removes his blindfold and looks around fearfully, then relaxes slightly) They moved me again. They have a box they put me in – the shape of a coffin and it’s soundproof. The first time they put the box in the back of a van with a bad exhaust system. I was unconscious when they took me out. (beat) Sometimes I don’t know. I don’t absolutely know whether I’m alive or dead. *****

WALKER: (Pg 36-37) We did it! We got the message out! We put those bastards on the spot. They’re going to have to ask for everybody – I know it! You were fantastic! Everybody in America felt for you. Was I right or what? The cameramen were tearing up.

LAINIE: They were not.

WALKER: I saw tears. Men who’ve seen every disgusting, pitiful atrocity that ever happened. But they cried tonight. For Michael. For you.

LAINIE: No one has to cry for me.

WALKER: They do. That’s the point. That’s the power. Every once in a while, enormous numbers of people become ready to hear something. And if you’ve got what they’re ready to hear, then you’re a very powerful person. You have to use it.

LAINIE: Is that all this has been? You’ve just been waiting for me to . . . blossom into some kind of spokesperson for you?

WALKER: Not for me . . . For Michael. How do you think you’re going to get him back? ESP? You going to pray he’ll show up? He won’t You’ll get him back when you make this government uncomfortable enough to lean on somebody – that’s it.

LAINIE: I don’t feel like celebrating. For all I know, I haven’t done anything more than risk the lives of innocent people tonight.

WALKER: Look . . . I’ve waited a year for a story . . .

LAINIE: Michael’s waiting. Not you. Not me. Michael! (softly, near tears) (Pg 38-39) I can’t see him anymore. I can’t remember what he looks like. *****

MICHAEL: Sometimes I wake up and realize that months have gone by. (beat) Time is change. That’s all it is. When there’s no change. When there’s no change . . . Yesterday one of my guards told me I’d been here three years. (beat) I didn’t know what he meant. (beat) (Pg 44-45) Some clothes were thrown on me and I was hustled into the back seat of a car by three men. They drove me to a quiet neighborhood and shoved me into a building. I was taken down, still blindfolded, to a small, cramped room that smelled like . . . clay, and I was . . . (pantomimes the execution gunshot) (long beat) *****

ELLEN: (Pg 45-46) When I worked in the Defense Department, I told them their men were heroes. I said, “He died of bad luck.” No bad planning at the top, not tactical mistakes of his commanders. Bad luck. Lainie gets the truth. We miscalculated. We valued Michael’s life below a chance to make an international point. We increased the danger for all the hostages. We chose to (Pg 41-42) intercept a terrorist. Not a Shi’ite, not even Lebanese. But an Arab, and . . . we killed him. It was the judgment of the Department that Michael and the others would not be overly . . . endangered. (Pg 46) We miscalculated.

LAINIE: Thank you.

ELLEN: (turns with surprise) Lainie, I . . . I wasn’t ---

LAINIE: (angry) Going to say it like that? I’m glad you did. Is that all your business?

ELLEN: Allow me to take this opportunity to convey the deep sympathy of the Secretary of State and the President.

LAINIE: Go to hell. (long beat) (Pg 47) (with heavy sarcasm turning to intense sadness) No, I think you and the government did your best. I think everyone did his best. Michael, Walker, you, the Shi’ites – even the ones that killed Michael. Probably everyone has done his best. That’s what frightens me. That’s why I don’t know if I’ll ever be able to walk out of this room anymore. Into what? A world filled with people doing their best.

ELLEN: I wish I could take your pain away.

LAINIE: I wish you could remember it.
```

---

## IC-0289: Ungrateful

- Title: Ungrateful
- Author (byline): Linda Eisenstein
- Work: The Best Women’s Stage Monologues of 1997
- Publisher: Smith & Kraus
- Publication date as stated: Dec 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MEG
- Teaser before the introduction: No
- Spoken words (computed): 1047
- Already set (do not supply): none

### Source block (context only)

```text
Author: Linda Eisenstein
Book: The Best Women’s Stage Monologues of 1997
ISSN: 1575251388
Publisher: Smith & Kraus
Date (Month/Year): Dec 1998
```

### Introduction (context only: never use it for content warnings)

```text
“No ma, I don’t want any green beans.” (mimicking) “There are children starving in Africa that would love the chance to eat those beans.” Ungrateful. “I’ve been standing all day and my legs are killing me!” (mimicking)“You know, some people don’t even have legs to stand on.” Ungrateful. “Can’t you drive me? It’s such a long walk.” (mimicking) “Back in my day we had to walk five miles to school, uphill both ways!” Ungrateful. We’re a bunch of ungrateful people living in an ungrateful time. Let’s put things in perspective. Ungrateful by Linda Eisenstein
```

### Performance text (classify this)

```text
MEG: SO there I am after the show, cooling my heels in the Playhouse Square* lobby (Note: insert the name of your big-buck commercial theatre here: the one that would present the touring production of "Cats".) for what seems like hours, because as usual Dana was late AGAIN! And I'm waiting, and waiting, and waiting for the damn car to show up, and there's no sight of Dana, of course, and I've called the apartment twice and gotten the answering machine twice, and I figure she's probably in some book store browsing around without a care in the world, or having a second cup of Cafe Latte blabbing away with somebody, losing track of time while I'm just standing here looking stupid. And so I think about maybe getting a cab, and I look in my wallet and discover I don't have enough money for one, and I'm getting more and more steamed, and more and more freaked out, until I can't even pay attention to the book I brought for this very purpose, because all I do is look up every ten seconds wishing the goddamn car and goddamn Dana would GET here, already, and soon all I'm doing is pacing up and down. Until now it finally IS a whole hour that I've been waiting, and they actually make me switch lobbies, and they're starting to run the big industrial-sized vacuum cleaner and there's nobody there but me and the security guard and he wants to go home. And the frustration is starting to turn into panic and I'm muttering to myself, on the verge of hysteria, swearing I'm going to kill Dana the moment the car pulls up, that is, if she's not already dead from a traffic accident. . .

And THEN it starts to rain. And I totally lose it, man, I'm standing there staring out the glass doors, wracking sobs are pouring out of me, I'm actually sobbing with rage and loss and the sense of abandonment, feeling like a total fucking orphan of the storm, okay? And you know what happens then? A homeless guy walks by. (Pause.) Outside. In the rain. A homeless guy walks by. And boom, two words light up my mind like a sudden flash of lightning, and I hear a voice. And it says: "Ungrateful girl." It's my grandmother's voice. Not an angry voice, I don't ever remember her being angry. She'd just get this tone of regret, shaking her head, like you just didn't understand something. (A sigh.) "Ungrateful girl." And it's like a sword in my heart.

You know, I don't mean to be ungrateful. Really. I don't. It's not the way I was raised. "Be grateful for small favors." Grandma used to say stuff like that all the time. When you'd complain about some injury, like a teacher was nasty, or your feet hurt, she'd shrug and say" some people don't have any legs." Or, "people are starving in Armenia," she'd say, as she filled your plate with food you didn't want. Well, they're starving in Armenia again, Grandma. And in Bosnia, and Chechnya, and a bunch of other places I can barely pronounce, but they all sound like places my grandmother could have been from. I could be from there. I could be living in one of those places now, starving and ducking bombs, if my grandmother hadn't gotten the hell out. Gotten out when she was still an ungrateful girl herself. A servant girl, who refused to listen to some priest's sermon about her duty. A hungry servant girl, who stole meat from her master's dog.

I figure that must be why we're all so ungrateful, so restless here. America is bubbling over with the gene-pool of the people who wouldn't sit still. We're all the children and grandchildren and great grandchildren of the ones who refused to sit and take whatever was dished out. So we're all congenitally ungrateful, you and I. We sit in our houses surrounded by riches and privilege and every convenience and advantage, bitching and moaning our heads off. Ungrateful, ungrateful.

Some places we would be illegal. Things I do, things I take for granted every day, could get me thrown in jail somewhere else. Tortured. Even killed. Did you see the pictures of those Iranian women, the ones who wouldn't wear the veil? With the black sacks over their heads, right before the trapdoor sank under their feet? That could be me. Or you. And I'm still fucking ungrateful, and so are you, I can see it in your eyes. And why not? I don't think I should have to rejoice just because I'm not locked up. Why shouldn't freedom be the norm? Am I supposed to feel good because I only get dirty looks instead of a boot in the back or a truncheon to the head? Not hardly. Not hardly.

But it got to me, man. When I was standing there, watching that guy walk by in the rain. And I thought, maybe this life-this life in which I feel like I'm suffering so much, this life where I cry and cry-this one's the reward. It's time off for good behavior, man. Maybe in the last bunch of lives, they really got me burned me as a witch, or shot me and left me in a ditch with the other corpses, or left me starving in some rat-hole for the jailers to rape. This life? This one's the reward. The one where they don't gouge my eyes out. The one where all I get is the occasional sneer, and a stack of unpaid bills, and a lover that leaves me standing alone in the lobby for an hour after some fluffy Broadway touring show, where the ticket cost more than some-body's Third World paycheck.

Oh, Jesus. I'm supposed to be standing here feeling grateful. Grateful for only being marginalized and misunderstood and ignored now and then. Hey, that's a piece of cake, babe. That's ice cream and butterflies and a walk in the park. And then this car finally pulls up in the rain, fenders rattling-and there's Dana, with that look, you know, that guilty" I really screwed up, go ahead and walk on my face with your hobnailed boots" hunched-over LOOK-and all I could think of was-Oh, babe. Oh, babe. We don't know how lucky we are.
```

---

## IC-0290: The Very First Dating Video of Rose Ritz from I Love You, You're Perfect, Now Change

- Title: The Very First Dating Video of Rose Ritz from I Love You, You're Perfect, Now Change
- Author (byline): Joe di Pietro
- Work: Not specified
- Publisher: Hal Leonard Corporation
- Publication date as stated: Jan 2000
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ROSE
- Teaser before the introduction: No
- Spoken words (computed): 641
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joe di Pietro
Book. I Love You, You're Perfect, Now Change
ISBN: 978-0634009334
Publisher: Hal Leonard Corporation
Date (Month/Year): Jan 2000
```

### Introduction (context only: never use it for content warnings)

```text
On line dating – It’s the latest thing . . . Look at a few photos, read a profile and then send an e-mail . . . or maybe just a “wink” – What could be easier??? But the problem with traditional photo-based dating services is that photos — even those that come from Facebook — are often outdated and misleading. A video, on the other hand, is not only a more accurate representation of a potential suitor's attractiveness, but a chance to show off personality and creativity — you know, the REAL YOU. That’s a good thing, right? The Very First Dating Video of Rose Ritz from I love You, You’re Perfect, Now Change by Joe di Pietro.
```

### Performance text (classify this)

```text
ROSE: Hello. I'm Rose Carboni. No! Ritz! Rose Ritz! That's it. Rose Ritz. Yes. Carboni was my husband's name. But he's dead. Whoops! Actually, he's not really dead, we're divorced. I just prefer to think of him as dead, cheers me right up.

(does something embarrassing on camera and then realizes it) Oh my gosh, did I just do that?! Here I am, making my very first dating video -- that's right, this is the very first dating video of Rose Ritz! -- and I'm already telling all you potential -- Mr. Video Men-Of-My-Dreams out there-telling all you Video Men that I'm divorced. Good move, Rosie!

But yes, I'm divorced. I love you forever -- not! Divorced, divorced, divorced! But actually, can we not even talk about my divorce. My divorce was like -- like open heart surgery without anesthesia. My insides were just ripped out, my guts on the floor, and no one bothered to sedate me!

Well, wasn't that attractive of me to share with you. Okay. I bet my phone is ringing off the hook already!

Now about myself -- well, I've just had to re-enter the workforce as a telemarketer. Basically I call people up, try to sell them something and they hang up on me. It's very fulfilling.

Oh, and I just enrolled in a magic class at the high school adult school. It was either magic or a step aerobics class, and quite frankly, magic seemed less exhausting. And to be even more frank, I thought it'd be a more likely place to meet men. Unfortunately, the class consists entirely of divorced women, all hoping to meet men. Yes, seven divorced women learning how to pull a coin from a child's ear, while next door twenty-five single men do step aerobics. Well, at least I'm back in the game!

Oh, I almost forgot -- I've got children! Well isn't that attractive. So Mr. Video Man, I hope you don't hate children.

Though I do. Oh, I don't hate my children, of course! I hate the concept of having to raise children all by yourself after your dead husband walks out on your fortieth birthday! Oh my God! I just told you he left me, not visa versa! DAMAGED GOODS ALERT! Why would her dead husband dump her and run off with an older woman? That's right, he had a mid-life crisis and he didn't even have the decency to leave me for someone young and pretty and firm! He left me for a size eighteen with a grandchild and a bad hip! So now you're really wondering what is wrong with Rose Ritz!

Well you know what? I don't care, Mr. Video Man! 'Cause I've stayed up many a late night with nothing to comfort me except my thirty-two inch television and sent away for all those tapes from all those late-night infomercial things -- Tony Robbins, Richard Simmons, all those nuts who think they're psychic -- and now I believe in myself! Stop the insanity! Deal a meal! I'm okay!

And now, after fifteen years of waking up next to the same balding lump of deadwood, Rose Ritz is ready and in control and had to stop the car three times to throw up on the way to this humiliating video dating session just on the thousand-to-one chance that maybe she'll meet a decent guy so she doesn't have to be alone for the rest of her life 'cause her dead husband left her for a limping grandmother!

(A beat) No warning. "I love someone more." Then he just left. And then it just stopped. My life. For three days, I laid in bed, and just stopped.

And somehow, here I am -- on the six month anniversary of the collapse of my life -- I got myself here -- to make the very first dating video of Rose Ritz. So choose me. Mr. Video Man. Please.
```

---

## IC-0291: Voices from Chernobyl

- Title: Voices from Chernobyl
- Author (byline): Svetlana Alexievich
- Work: Not specified
- Publisher: Dalkey Archive Press
- Publication date as stated: April 2005
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: LYUDMILLA, DOCTOR, NADEZHDA, LARISA Z
- Teaser before the introduction: Yes
- Spoken words (computed): 1725
- Already set (do not supply): none

### Source block (context only)

```text
Author: Svetlana Alexievich
ISBN: 978-1564784018
Publisher: Dalkey Archive Press
Date (Month/Year): April 2005
```

### Introduction (context only: never use it for content warnings)

```text
April 26, 1986 -- fourteen days after the worst nuclear accident in history, Lyudmilla Ignatenka lost her husband. Reactor #4 at the Chernobyl Nuclear Power Plant in what is now northern Ukraine exploded and burned. Scientists estimate the zone around the former plant will not be habitable for up to 20,000 years.

According to the official, internationally recognized death toll, just 31 people died as an immediate result of Chernobyl, these were the first responders. But over 600,000 people suffered from radiation poisoning that continues to impact generation after generation. Imagine being a mother and knowing that your children or future children are at risk.

Voices from Cherynobyl collected from interviews by Svetlana Alexievich in 1996.

Nadezhda Petrovna Vygovskaya -- mother
```

### Performance text (classify this)

```text
Lyudmilla -- wife of fireman, Vasily Ignatenko

LYUDMILLA: (Pg 5-6) We lived in the dormitory of the fire station where he worked. One night I heard a noise. I looked out the window. Everything was radiant. The whole sky. “Close the window and go back to sleep,” he said. “There’s a fire at the reactor. I’ll be back soon.”

They went off just as they were, in their shirt sleeves. No one told them. They had been called for a fire, that was it. Four o’clock. Five. Six. Seven o’clock. I was told he was in the hospital. The police had already encircled it, shouting “The ambulances are radioactive, stay away!”

[When] I saw him. He was all swollen and puffed up. You could barely see his eyes. Many of the doctors and nurses in that hospital would get sick themselves and die. But we didn’t know that then. (Pg 7) The doctors kept telling us they’d been poisoned by gas. Not one said anything about radiation. No one talked bout the radiation.

DOCTOR: (Pg 9) All right, listen: his central nervous system is completely compromised. And if you start crying, I’ll kick you out. No hugging or kissing. Don’t even get near him.

LYUDMILLA: (Pg 12) It was a hospital for people with serious radiation poisoning. For fourteen days . . (Pg 11) Will they live? Live. (Pg 12) In fourteen days, a person dies. [She is silent] (Pg 11-12) He started to change – every day I met a brand-new person. The burns started to come to the surface. At first there were little lesions, and then they grew. I came off in layers – as white film . . . the color of his face . . . his body . . . blue . . . red . . . gray-brown. The only thing that saved me was it happened so fast; there wasn’t any time to think, there wasn’t any time to cry.

(Pg 17) They photographed him. Naked. One thin sheet on top of him. I changed that sheet every day, and every evening it was covered in blood. I pick him up, and there are pieces of his skin on my hand. They photographed him. For science, they said.

NADEZHDA: (Pg 155-157) It happened late Friday night. My husband says, "There's some sort of fire at the nuclear plant. They're saying we are not to turn off the radio." I forgot to say that we lived in Pripyat, near the reactor. I can still see the bright-crimson glow. [But] this wasn't any ordinary fire, it was shining. It was pretty.

That evening everyone spilled out onto their balconies. We were on the ninth floor, so we had a great view. People brought their kids out, picked them up, said, "Look! Remember!" And the people who worked at the reactor. . . They stood in the black dust, talking, breathing, wondering at it.

People came from all around on their cars and their bikes to have a look. We didn't know that death could be so beautiful. My throat tickled, and tears came to my eyes.

In the morning I woke up and I remember feeling something isn't right, something has changed forever. At eight there were already military people on the streets in gas masks. When we saw them on the streets, we didn't grow frightened -- on the contrary, it calmed us down. Since the army has come to our aid, everything will be fine. We didn't understand then that the peaceful atom could kill, that man is helpless before the laws of physics. All day on the radio they were telling people to prepare for an evacuation. We settled in Mogilev and our son started school, he came back the very first day in tears. They put him next to a girl who said she didn't want to sit with him, he was radioactive. Our son was in the fourth grade, and he was the only one from Chernobyl in the class. The other kids were afraid of him, they called him "Shiny." His childhood had ended so early.

Larisa Z -- mother

LARISA Z: (Pg 85-88) My little daughter-she's different. She's not like the others. When she was born, she wasn't a baby, she was a little sack, sewed up everywhere, not a single opening, just the eyes. The medical card says: "Girl, born with multiple complex patholo-gies: aplasia of the anus, aplasia of the vagina, aplasia of the left kidney." That's how it sounds in medical talk, but more simply: no pee-pee, no butt, one kidney.

On the second day I watched her get operated on, on the second day of her life. She opened her eyes and smiled, and I thought that she was about to start crying. But, God, she smiled! The ones like her don't live, they die right away. But she didn't die, because I loved her.

In four years she's had four operations. She's the only child in Belarus to have survived being born with such complex pathologies. I love her so much. [Stops] I won't be able to give birth again. I wouldn't dare. I came back from the maternity ward, my husband would start kissing me, [and] I would lie there and tremble: we can't, it's a sin, I'm scared. I heard the doctors talking: "That girl was born in a suit of armor. If we showed it on television not a single mother would give birth." That was about our daughter. How are we supposed to love each other after that?

I went to church and told the minister. He said I needed to pray for my sins. But no one in my family has ever killed anyone. What am I guilty of? First they wanted to evacuate our village, and then they crossed it off their lists -- the government didn't have enough money. And right around then I fell in love. I got married. I didn't know that we weren't allowed to love here. Many years ago, my grandmother read in the Bible that there will be a time when everything is thriving, everything blossoming and fruitful, and there will be many fish in the rivers and animals in the forest, but man won't be able to use any of it. And he won't be able to propagate himself in his likeness, to continue his line. I listened to the old prophecies like they were scary fairy tales. I didn't believe them.

My daughter . . . She's four years old and she can sing, dance, she knows poetry by heart. Her mental development is normal, she isn't any different from the other kids, only her games are different. She doesn't play "store," or "school" she plays "hospital." She gives her dolls shots, takes their temperature, puts them on [an] IV. If a doll dies, she covers it with a white sheet.

We've been living in the hospital with her for four years, we can't leave her there alone, and she doesn't even know that you're supposed to live at home. When we go home for a month or two, she asks me, "When are we going back to the hospital?" That's where her friends are, that's where they're growing up.

After the last operation her urinary functioning completely broke down, and they were unable to insert a catheter. They'll need more operations for that. They've advised us to seek medical help abroad. Where are we going to get tens of thousands of dollars if my husband makes 120 dollars a month?

One professor told us quietly: "With her pathologies, your child is of great interest to science. You should write to hospitals in other countries. They should be interested." So I write. [Tries not to cry.] I write that every half hour we have to squeeze out her urine manually through artificial openings. Where else in the world is there a child who has to have her urine squeezed out of her every half hour? And how much longer can it go on? No one knows the effect of small doses of radiation on a child. Take my girl, even if it's to experiment. I don't want her to die. I'm all right with her becoming a lab rabbit, just as long as she lives. [Cries.] I've written dozens of letters. Oh, God!

She doesn't understand yet, but someday she'll ask us: why isn't she like everyone else? Why can't she love a man? Why can't she have babies? I wanted to get papers so that she'd know, when she grew up, it wasn't our fault, my husband and I. It wasn't our love that was at fault. [Tries again not to cry.]

I fought for four years with the doctors. I knocked on the doors of important people. It took me four years to finally get a paper from the doctors that confirmed the connection between ionized radiation and her terrible condition. They refused me for four years, they kept telling me: "Your child is a victim of a congenital handicap." What congenital handicap? She's a victim of Chernobyl!

I studied my family tree. Nothing like this has ever happened in our family. Everyone lived until they were eighty or ninety. My grandfather lived until he was 94. The doctors said: "We have instructions. We are supposed to call incidences of this type general sicknesses. In twenty or thirty years, when we have a database about Chernobyl, we'll begin connecting these to ionized radiation. But for the moment science doesn't know enough about it." But I can't wait twenty or thirty years. I wanted to sue them. Sue the government. They called me crazy, laughed at me. [Beat] There were children like these in ancient Greece, too. One bureaucrat yelled at me: "You want Chernobyl privileges! Chernobyl victim funds!" How I didn't lose consciousness in his office, I'll never know.

[Breaks down. Cries.] This girl is growing up -- she's still a girl -- even our neighbors don't know. I'll put a dress on her, and a handkerchief, and they say, "Your Katya is so pretty." Meanwhile I give pregnant women the strangest looks. I have all these mixed feelings: surprise and horror, jealousy and joy, even this feeling of vengeance.

(Pg 126) We’re often silent. We’re afraid to talk about it. We don’t know how. [On April 26, 1986] the world was split in two: there’s us the Cherynobylites, and then there’s you, the others. (Pg 133) They’ve written dozens of books. Fat volumes, with commentaries. But the event is still beyond any philosophical description. (Pg 187) It’s not just the land that’s contaminated, but our minds.
```

---

## IC-0292: Walking with RJ

- Title: Walking with RJ
- Author (byline): Stephanie Peirolo
- Work: The Moth Presents All These Wonders, Pgs 82-88
- Publisher: Crown
- Publication date as stated: Mar 2017
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: STEPHANIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1577
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephanie Peirolo
Book: The Moth Presents All These Wonders, Pgs 82-88
ISBN: 978-1101904404
Publisher: Crown
Date (Month/Year): Mar 2017
```

### Introduction (context only: never use it for content warnings)

```text
No mother should have to choose between saving her child’s life and navigating the maze of health insurance coverage. But that’s exactly what Stephanie Peirolo faced when her son RJ suffered a traumatic brain injury. She thought the hardest part would be watching RJ fight for his life not fighting a system that puts profits before people.

Health insurance “coverage” quickly vanished behind automated phone lines and unreadable policies. And when Stephanie is fired from her job for taking too much time off, what little insurance safety net was in place disappeared too. While her son struggled to hold up his head, and relearn basic things like swallowing and speaking, Stephanie Peirolo discovered that our healthcare system doesn’t break only the sick. It breaks the families who love them, too.

Walking with RJ by Stephanie Peirolo
```

### Performance text (classify this)

```text
STEPHANIE: (Pgs 82-88) I was 23 years old when I had my first child. I was in labor for three days before my son, RJ, was born. So when I first laid eyes on him, I felt nothing but exhaustion. I said, “This is it?” It wasn’t until about an hour later, when I woke up and he was in my arms, wrapped up, that I felt it -- that rush of maternal love, that primal adoration. And I thought, This is it. This is how the species survives.

I had another child, a daughter, Emma. And soon after Emma was born, their father and I divorced. He moved to Europe, and I raised the kids by myself.

Fast-forward. We’re living in Seattle. The kids are in high school and doing great. They get straight A’s. The only thing RJ gets in trouble for is wearing his hair long. He goes to Catholic school and you’re supposed to have your hair above your collar. But RJ plays the drums, he’s in theater, so he wears his hair long.

In the fall of his junior year, he’s cast as the lead in the school play. He’s going to be Atticus Finch in To Kill a Mockingbird, so he has to get his hair cut. And I remember him walking out of the barbershop. He had a crew cut, and he was six feet tall and impossibly handsome. He had this kind of shy smile, and I thought, This is the man he is becoming.

STEPHANIE: In January of his junior year, a cop showed up at our door, and he said, “Are you RJ’s mom?” I said yes. He said, “There’s been an accident.” I said, “Is he dead?” And he said, “Not yet, but we have to get to the hospital right away.” So the cop drove me to Harborview, which is not the closest hospital to our house, but it is the one with a trauma center. We went in the back way, where the ambulance bays are. Someone was hosing blood out of the back of an ambulance, all of this blood, and I remember thinking, That’s my son’s.

It took a couple of hours for me to find out what had happened. RJ had been driving to his best friend’s. He had his seat belt on. He didn’t have drugs or alcohol in his system, and he was hit from the side in a blind intersection. He sustained a traumatic brain injury (or TBI), and he had broken his pelvis. At the time I didn’t understand the gravity of a TBI.

I was the vice president of an advertising agency. They had just changed their insurance plan. Keep in mind, it’s the first week of January. So I didn’t have a list of my benefits. What I have is an insurance card with a phone number on the back. So while RJ’s in the ICU, I call the phone number, and the voice on the other end of the phone told me, “ICU is covered, intensive brain-injury rehab is covered, skilled nursing facility . . .” And they list off all these great benefits. And I remember thinking, Thank God I don’t have to worry about insurance.

When RJ was discharged from the ICU, he was transferred to the rehab facility, and shortly after, they called me and said, “Your insurance company called and said RJ’s benefits are up on Friday.” I said, “No, no, no, no, he’s got many more benefits,” but of course I just had a voice on the other end of the phone.

So I went over there, and said, “Where am I supposed to take him? He’s in a coma.” They said, “Well, there’s always foster care.” (shocked pause) So Emma and I took RJ home. We made a hospital room in his bedroom. He had PEG tube in his stomach, and that’s how we pumped in nutrition. They taught us how to do physical therapy. Emma was 15, and she said, “Mom, I will help you take care of RJ in any way I can, as long as it doesn’t involve the Speedo zone.” So when he needed to be changed, because of course he was in diapers, she would bring me a bucket of warm water and washcloths and I would clean him up.

Coming out of a coma is nothing like what you see in the movies. It’s a long, slow, painstaking process. It took RJ months to learn how to hold up his head. We put him in his wheelchair, and his friends would come by every day after school.

Months had passed, and I still couldn’t get the Summary Plan Description. I kept calling [the insurance company]. But I realized this not a bureaucratic mix-up, this is intentional and this is illegal. This is a violation of a law called ERISA - the Employee Retirement Income Security Act of 1974. So I called an ERISA lawyer and told him the situation, and he said, “I can help you, but you’re going to have to give me a retainer of $30,000.” I said, “Let me be clear. I’m a single parent. I have paid to set up a hospital room in my house. I pay a nurse to sit with my son, so that I stay employed so I can keep this insurance. I don’t have $30,000.” And he said, “I’m sorry; I can’t help you.”

At this point, I was completely exhausted and I was very concerned about getting fired because I’d taken so much time off. So, I applied for and was granted FMLA leave. The Family Medical Leave Act says you can take 12 weeks of unpaid leave to care for a sick family member and they have to keep your job for you. Shortly into my FMLA leave, I was fired. These things are illegal, but you can’t call the police on a corporation. And I couldn’t afford an attorney.

When RJ turned 18, he was able to go on Medicaid, and I made the decision to put him in a nursing home. I found a facility that specialized in patients with TBIs. All their patients were on Medicaid, so they didn’t have much money. But they took really good care of RJ, and he continued to make slow progress. He could do thumbs-up for yes, thumbs-down for no. We were visiting him, and Emma was teasing him, and he flipped her off. I got really excited ‘cause that’s like some manual dexterity happening there, right? And then he turned to me and he put his hand down because, brain injury notwithstanding, he was not about to flip off his mother.

Before RJ’s accident, I had to drag him to Mass on Sundays, but after the accident, he loved to go to church.I’d say, “Do you want to go to Mass today?” He’d put his thumbs up. He learned how to put money in the collection plate again. And when he learned how to swallow – because apparently swallowing is incredibly complex; that took like a year to come back -- he could take Communion, and you could see it provided him so much solace.

In August of 2005, RJ got very sick, and we thought it was the flu. He still had his PEG tube in his stomach, and it had fallen out. That happens, and when it falls out, you put it back in. You’re supposed to X-ray to make sure you have it in the right place. Well, this facility couldn’t afford an X-ray machine, so they guessed and they guessed wrong.

His food had been going into his abdominal cavity and he had sepsis. At the hospital, the surgeon took me aside and said, “I can operate on RJ, and I might save his life, but he’s going to go back into a deep coma, and he will never come out. Or you can let him go. You have to decide.”

So I went down the hall and called his father, who was still in Europe, and I said, “What should I do?” He said, “You’re caring for him; it’s your choice.”

So I went into RJ’s room. [He] was completely aware of what was happening, and he was afraid. His eyes were open really wide. And I said, “Honey, you’re very sick, and they can’t fix you. So you’re gonna go to God -- you’re gonna go to God, but my dad is there, and he’s gonna come and find you, and I will be there soon.” (long beat as she struggles to compose herself)

It took RJ three days to die. (another long silence)

[Today], RJ would be 27 years old. Why didn’t you keep him at home? If you had made more money, you could’ve put him in a private nursing home, then he never would’ve died.

The world is so diminished without him, like there’s been a total eclipse of the sun. Only I’m the only one who can see it. (beat) I wonder if RJ’s existence is part of a larger narrative arc. If maybe this slice in time was how RJ had to work out his destiny, and maybe my job was to walk with him. (beat) Between RJ’s accident and his death, he was only able to say a handful of words. And the word he said most was “Mom.” And there are times now where I feel RJ. I feel that he is. And in those moments, I know it’s his turn . . . for his love to carry me.
```

---

## IC-0293: Wealthy Lady

- Title: Wealthy Lady
- Author (byline): Joyce Carol Oates
- Work: I Stand Before You Naked
- Publisher: Samuel French, Inc.
- Publication date as stated: Nov 1991
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: LADY
- Teaser before the introduction: No
- Spoken words (computed): 628
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joyce Carol Oates
Book: I Stand Before You Naked
ISBN: 978-0573622489
Publisher: Samuel French, Inc.
Date (Month/Year): Nov 1991
```

### Introduction (context only: never use it for content warnings)

```text
The morning routine for you or me usually consists of a shower, a toothbrush and a bowl of cereal. But for a society matron, it consists of writing checks – POWDER BLUE CHECKS – to various charitable organizations. However, this particular matron should be more concerned with her sanity than with her charity.

Let me show you what life is really like for this Wealthy Lady. . . and maybe, just maybe you won’t wish for riches anymore. From I Stand Before You Naked by Joyce Carol Oates
```

### Performance text (classify this)

```text
LADY: (Graciously) I am performing the
rituals
of the body I woke up in
sweet smiles writing
checks
I am the lady of the house

this house you've gazed at
from the outside Yes
some of you have wondered
what it looks like
on the outside
Well -- it is nice! (Pause)

Yes I am the lady of the house
this is my boudoir
I am doing what I do best
I am writing writing
POWDER BLUE CHECKS

(Pause, as SHE writes, tears check out from book, etc.)

I am "prolific" I am much admired
I am happy to be so much admired
as I smile smile
writing writing
checks FLUTTER BLUE
on! In all directions!

(As if in a sudden breeze, checks flutter to floor.)

I am performing the rituals
oh! they're sac-red!
of the body I woke up in
I know my place
on this third-planet-from-the-sun
HEAPING RICHES LIKE GOD'S GRACE
into an emaciated face in a photograph --
Cambodian refugee no it's
is it? -- Ethiopian?
SAVE THE ORPHANS FUND
SAVE THE SYMPHONY FUND
SAVE THE REDWOODS FUND

I am smiling upon you all I'm in a good
mood this morning
I slept well last night and I'll sleep well
tonight
smiling upon the FRIENDS OF THE
MENTALLY HANDICAPPED
smiling upon the FRIENDS OF THE
ENDANGERED YAK
smiling upon the FRIENDS OF THE
ENDANGERED FETUS
I have many adventures with my checkbook
I SMILE UPON ALL RACES COLORS AND
CREEDS

(Sudden change of mood; yawns) An -- I'm a bit bored my poor hand is exhausted

(Rises from table, moves a bit stealthily) Now I'll leaf through the portfolio he keeps locked away

(LADY opens safe)

I'll finger these sacred papers the quarterly dividend statements the money manager's reports investments property interest oh! I suppose it's all in order, I wouldn't know and --

(LADY has small pistol in palm of hand)

-- and here! --
which he keeps in the safe thinks I don't know
about
I WILL HIDE IT IN MY CLOTHES

(LADY paces about the room, fantasizing, excited)

I will cancel the FRIENDS OF THE ART
INSTITUTE luncheon
I will attend today's Sotheby's auction
the Van Dusen estate poor Hendrik
there is a Goya up for bidding or is it a
Rembrandt!
Andrew Wyeth Van Gogh Jasper James
oh!
one or another!
I will bid gaily and drunkenly and when
I have bought everything when
the gallery officers approach me
then I will --

(Brandishes pistol)

No I will buy what remains of the Hinklemann
estate
and the old Quaker cemetery north of town
I WILL TURN IT INTO A LUSH LOVELY
MEADOW
I want sheep grazing rail fences inner-city
children
I want languorous mists that linger
cow-bells and vespers and shepherds with staves
Lombardy poplars for the balmy evening breeze
if the sheep get too filthy
if the children vandalize the monuments
IF ONE OF THEM APPROACHES ME --

(Brandishes pistol)

At the country club buffet I will toss food onto
the floor
I will shake the champagne bottles FIZZLE
SPRAY ALL OVER
I will gaze upon my lifelong friends without
recognition
I will mutilate the ladies' fur coats
When I am approached when they say Won't
you come with us
I will smile smile smile and

(Brandishes pistol)

No -- I will park the Mercedes by a warehouse
in my Gucci crocodile pumps I will go stumbling
through dark alleys
when I turn my ankle when I whimper
when one of them approaches
oh! I will run I will be terrified I will pant like a
doe!
when one of them touches me
I will --

(Brandishes pistol)

YOU THOUGHT I WAS A DEFENSELESS WHITE LADY DIDN'T YOU...!

(Abrupt change of mood, returns to table and pen, etc.)

Oh some other time
my migraine is
I'll cancel the luncheon though
I almost forgot the FRIENDS OF GAELIC
they depend upon me
the FRIENDS OF THE GRAPE PICKERS the
FRIENDS OF THE BLIND
oh! already it's afternoon
the day will flutter by safely

POWDER BLUE SMILES ON ALL SIDES
but --
I am crossing off my list
the COMMITTEE FOR THE PRESERVATION
OF ST. TIMOTHY'S ABBEY
for it is chaired by a swine
who chews
celery
noisily
```

---

## IC-0294: Weapons

- Title: Weapons
- Author (byline): Mary Krell-Oishi
- Work: Perspectives: Relevant Scenes for Teens
- Publisher: Merriwether Publishing, Ltd
- Publication date as stated: March 1997
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SHERYL
- Teaser before the introduction: Yes
- Spoken words (computed): 1968
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mary Krell-Oishi
Book: Perspectives: Relevant Scenes for Teens
ISBN: 1566080304
Publisher: Merriwether Publishing, Ltd
Date(Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
Tens of billions of dollars are spent each year by women worldwide on makeup and other cosmetic products. Why? Women have discovered that beauty is power. When a woman improves her appearance, an amazing thing happens. People begin to pay attention to her, listen to her, seek her company, ask her opinion. She becomes more confident. As her confidence grows, so does the respect she receives – at work, at home, everywhere. Lipstick, blush and mascara become tools for some and for some . . . Weapons by Mary Krell-Oishi
```

### Performance text (classify this)

```text
(SHERYL is getting ready for MIKE's party and during her conversation does her hair and makeup.)

SHERYL: I call these my weapons. This blush is one of those kinds that has two tones of peachy rose for accenting the cheekbones. I've got the kind of coloring that if I go with peachy I look jaundiced, and if I go with rose I look like some kind of cheap tart, so if I mix the two I get just the right amount of fresh and natural non-make-uppy look. Natural fiber blush brush, too. No polyester here! Eye liner in two shades, brown and dark brown. You don't want black because it's way too harsh. But if you go with light brown you might as well not wear any at all, so what's the point? And you have to use the pencil because the liquid stuff smears and wiggles. But don't put it on too thick, because if you do it defeats the purpose of enlarging the eye. Start at the middle of the eye and go outward. It's a matter of practice, that's all. And don't forget about mascara, thick lash, of course. But you have to be careful with the mascara because if you get the cheap stuff it gets all clumpy and makes you look like Tammy Faye, may God forbid. I spend a lot of money on mascara because my eyes are my best feature and you can't cheat on the lashes. The rest of this stuff I get at the dollar counter at the Pic and Save. To be honest, it's all pretty much the same. Except the mascara. It's important to remember the difference. I get mine at Nordstrom's. I know it's extravagant, but think about it. So I spend an extra two or three dollars and I have the satisfaction of knowing that my eyes will look great. It's sort of like a little insurance policy. I hope you're paying attention.

SHERYL: The lips are important, too. Very important, especially on a night like tonight. You want to have color, but you don't want it to make a mess if you get together with someone. I usually go with a strawberry gloss. You don't want to get the kind in a pot that you put on with your fingers because then you get all icky and where do you wipe your hands and it's always a mess. Nope. You get this stuff at the Pic and Save, right at the counter, and you can't go wrong. It comes in this handy little tube that fits perfectly in your pocket. Not only that, it's soft and flexible, so if you are wearing something that doesn't have pockets, you can stick it in your bra, which is an asset, because then it stays warm and goes on easier. And always wear a bra. Trust me, you'll regret it later if you don't. Look at all those women from the sixties and seventies who didn't. Sag city. Pitiful.

Mike's party tonight is supposed to be a very big deal, so I want to look good. Everyone will be there. We've all been waiting a long time for a party like this, our last party before we all graduate. His parents are gone, but it won't be rowdy because we're not the kind of kids to be stupid. We have respect for Mike's home and his parents' faith in him. So, it won't be like Chuck's party was where the whole football team came and drank and proceeded to act like fools and tear up the house.

That was awful, really awful. Of course, look at Chuck. He's like a walking advertisement for teenage evil. He was right in the middle of all that, encouraging it. And when his parents got home and saw that disaster, they didn't do anything about it. Just called in some professional house cleaners, had the carpets replaced and repaired the guest toilet in the downstairs bathroom. I don't know what happens to teenage guys when they get too much beer in them. It must be some sort of testosterone thing that I just don't understand. But at Mike's it will be a lot better. Yeah, everyone is invited. Well, I mean, everyone knows about this party, but that doesn't mean it will be some big blowout. Just a lot of nice people mingling and stuff. There will be a few people there that I really want to see, and some that I really want to see me. That's why I need my weapons. And that's why I'm taking my time putting this stuff on. I want to look beautiful, but not made up, see? Which reminds me, never ever wear face makeup, like powder or pancake or any of that. You only wear face makeup when you are on stage or you're old and have a lot of wrinkles to hide, like when you're thirty.

You want to look natural, kissable. The last thing a guy wants to see is your face melting off onto his shirt. A real turn off, trust me. Anyway, I figure this is going to be about the last high school party I go to. I've been going to high school parties since I was in junior high. That's five years of high school parties. (It's kind of weird to think that some of the guys I got together with when I was a freshman are now graduating from college. Hmmm.) Anyway, I want to look really good for this last party. So I hope you don't mind if I finish getting ready while I talk. I have all this worked out to a science. See, if I just follow a simple plan of attack I can be fully made up and looking pretty damn good in just about eleven minutes. Not bad! I know some girls take all day to get ready. Pathetic. There's so much more to do in life than primp, you know? But some people, I guess, just find it necessary to spend all day in front of a mirror doing something that shouldn't take more than a couple minutes.

Do you like this outfit? I do, even though it's jeans. I know some girls don't like to wear jeans. Heather won't even wear pants. "Girls wear dresses, boys wear pants," that's what she always says. But I'm perfectly comfortable in a good pair of nice-fittingjeans. And jeans are a good thing to wear, a good basic. You can look like a slob in jeans, but take those very same jeans, put on a nice button-down shirt and a blazer, and if you're feeling really funky, a thin tie and tuck those jeans into some black boots and you look very good. Want to look classy?

Same outfit, add a pair of earrings and put your hair up and, voila', you are right off the cover of YM magazine. Never, though, wear heels with jeans. Hello, tramp! if you do. Trust me on this one.

A lot of people are going to be at this party tonight. It should be pretty fun. But since this is my last appearance at a high school party, I want to make an impression that will last. God, I hate to think I'd turn into one of those losers that keep going to high school parties after they graduate. I'm counting on the fact that Nick Carloti will be there. In fact, I bet you solid money that Nick will be there. He graduated, what, four years ago? I remember, and God this is embarrassing to admit, but I remember being so impressed with myself for macking with him when he was a senior and I was a freshman. I thought he was the beginning and end of the world. Now, it's just humiliating to think about it. I mean, look at him. He's been out of school for four years and he's doing exactly the same thing he did when he was in high school. A lot of talk about all the things he's going to do, but never any action to get him there. It's sad, really.

Nick, however, is one of the reasons I want to look especially good tonight. Boy, did he use me four years ago. Took advantage of my innocent nature. I'm not saying we did anything more than mac, because we didn't. I was young and stupid, but not a fool. What he did was play with my feelings, lead me into thinking that there was going to be a real relationship there. God, I was dumb. I mean, really, what would a popular senior like Nick see in a little freshman like me? Dh, he'd tell me how he loved me and there was no one else. And, yeah, I knew in my brain he was lying, but in my heart I wanted to believe it. First love, you know? Even some of the senior girls took me aside and told me what a cheating worm he was and what he was doing. But would I listen? No siree, not me. I told them that that's how he used to be, but I would change him. Dumb, huh? But I learned a really good lesson, you know. I learned that people are who they are and they are not going to change. You either love someone for who they are or move on. I can thank Nick for that. He was a good learning experience. He was fun, but he was ajerk and didn't really care about anyone but himself. I learned that that's not the kind of person I want in my life. A good lesson to learn early, rather than waiting until you're in your twenties and marrying an idiot hoping he'll turn into a decent person. 'Cause they won't. But the nasty little vindictive side of me wants Nick to see that the little girl whose mind he messed with is now a grown woman.

Here's my plan. I am going to walk into that party looking so fine that all heads will turn. See, this is the perfect outfit to wear, too. Casual enough to look like I just threw something together, but smart enough to look stylish and stunning. And I'll tell you, jogging five miles every day does wonders for the fit of your jeans! So, I will sashay right up to Nick, give him a big hug and ask how he's doing. He, of course, will tell me about how things are just about coming together for him. How he's going to start going on auditions for agents or he's thinking about getting back into singing. You know, the same old same old he's always talking about. Of course, he won't ask me about what I'm doing, but I'll work the conversation around to me eventually. OK, look at me. Hair, makeup, outfit. I look great, right? My weapons are all in place. I'm looking pretty devastating if I do say so myself. But! Here's the atomic bomb that I am going to drop on him. You ready?! I just found out today that I got accepted to Yale! Ha! Yale! And I got a couple of scholarships that will cover most of the costs. And I did it all with my own talents, determination and brains. I'm going to Yale!

My point here is this: Nick and I had the same four years. What has he done? Not much. Stagnated, works as a waiter in the same place he did four years ago. Talked a good game, but never got off the bench to play it. But in those same four years I worked hard and it paid off. It paid off big. That's the main weapon I have. Me! So, yeah, I do the makeup, hair and clothes thing. But I have a future that includes more than just looking good. Everything I do is up to me. And that, my young friend, is the best weapon of all.
```

---

## IC-0295: When I Was a Little Girl and My Mother Didn’t Want Me

- Title: When I Was a Little Girl and My Mother Didn’t Want Me
- Author (byline): Joyce Carol Oates
- Work: The Best American Short Plays 2001-2002
- Publisher: Applause Books
- Publication date as stated: Aug 2007
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 871
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joyce Carol Oates
Book: The Best American Short Plays 2001-2002
ISBN: 978-1557837042
Publisher: Applause Books
Date (Month/Year): Aug 2007
```

### Introduction (context only: never use it for content warnings)

```text
Sometimes children are not able to live with their parents, possibly due to a parent's death, incarceration, abuse or neglect, poverty, mental illness, substance abuse, or unwillingness to raise a child. During these times relatives often step in to care for these children. In 1999, According to the National Survey of America's Families, 2.3 million children, or 90 percent of children not living with parents, lived with a relative. The solution seems to be a valid and preferable one for our society – after all . . . these children do remain with family rather than being placed in foster care with complete strangers. However, being separated from on’es parents regardless of the reason or manner of solution can have profound long-term effects on the child. In this selection by Joyce Carol Oats a woman nearing the end of her life reflects back on her childhood . . . When I was a Little Girl and My Mother Didn’t Want Me.

[Lights up. An elderly woman speaks. Her voice alternates between urgency and bemusement; emotion and reflection.]
```

### Performance text (classify this)

```text
My father was killed and I never knew why.
Then, I was given away. By my mother.
I was so little.. .six months.
There were too many of us, nine of us, my mother gave me away. When I was old enough to
know...I cried a lot.
My father was killed and I never knew why.
No one would tell me.
Now there's no one I can ask.
"Why? Why?"
It happened in a fight, in a tavern, he was only forty-four
years old.
My father I never Knew. Forty-four! Now, he could be my son. I wasn't always an.. .old
woman. Eighty-one.
I was a girl for so long. I was a little girl for so long.
I was six months old when my father died.
And there were too many of us to feed, and my mother. . . gave me away.
There were nine children. I was the baby.
I was born late, I was the baby.
My mother gave me to her sister Lena who didn't have children. This was in 1918.
This was in the Black Rock section of Buffalo, the waterfront on the Niagara River.
Germans, Poles, Hungarians.. .immigrants.
We were Hungarians. We were called "Hunkies."
I don't know why people hated us...
[WOMAN pauses; decides not to explore this.]
Uncle John and Aunt Lena were my "parents."
We moved to a farm far away in the country.
And my real mother and my brothers and sisters moved to a farm a few miles away.
Uncle John and Aunt Lena were good to me.
I don't know if I loved them...I think I loved them. I think...
I think they loved me.
They wanted children but couldn't have them so it was right, I think, that my mother gave
me to them...
[Pause.]
It was a, a good thing, it was a.. .necessary thing.
I would learn one day that it happened often.
In immigrant families in those days.
In poor immigrant families.

My father was killed and I never knew why.
They said he was a bad drinker, he got drunk and was always in fights.
The Hungarians were the worst, they said-the drinking, and the fighting.
They said he was so handsome, my father.
My mother Elizabeth was so pretty.
Curly hair like mine.
They said he had a temper "like the devil."
In the tavern there was a fight, and he died.
A man took up a poker and beat my father to death.
I never knew why, I never knew who it had been.
Yet this was how my life was decided.
There is the moment of conception-you don't know.
There is the moment of birth-you don't know.
There is the moment your life is decided-you don't know.
Yet you say, "This is my life."
You say, "This is me."
[WOMAN regards herself in wonder like a stroke victim regaining some of her
awareness. ]
When I was a little girl and my mother didn't want me I hid away to cry.
I felt so bad and I felt so ashamed.
When I was old enough I would walk to the other farm.
There was a bridge over the Tonawanda Creek a few miles away. They didn't really want to
see me I guess.
My name was Carolina, but they didn't call me that.
I don't remember if there was a name they called me.
They weren't very nice to me I guess.

They didn't want me, I guess I was a reminder of.. .something. Elizabeth, my mother, never
learned English.
She spoke Hungarian all her life.
She never learned to read. She never learned to drive a car.
My Aunt Lena never learned to drive, so the sisters didn't see much of each other.
They lived only a few miles apart, and were the only sisters of their family in America, but
they didn't see much of each other. That was how women were in the old days.
She was a short, plump woman.
Curly brown hair like mine.
People would say, "You look just like your momma!"
Then they would be surprised, I'd start to cry.
My mother scolded me in Hungarian
"Go away, go home where you belong. You have a home.
Your home is not here."
I loved my big brothers and sisters.
There was Leslie, he was the oldest.
He took over when my father died.
There was Mary, I didn't get to know real well.
They were born in Budapest.
There was Steve, who'd been kicked and trampled by a horse. His brain was injured, he
would never leave home.
There was Elsie who was my "big sister."
There was Frank who was my "big brother."
There was Johnny.. .and Edith...
There was George, I wasn't too close with George.
There was Joseph, I wasn't too close with.
[Pause.]

They are all dead now.
I loved them, but...
I am the only one remaining.
Sometimes I think: The soul is just a burning match!
It burns a while and then...
And then that's all.
It's a long time ago now, but I remember hiding away to cry. When I was a little girl and
my mother didn't want me.
```

---

## IC-0296: White Oleander

- Title: White Oleander
- Author (byline): Janet Fitch
- Work: Not specified
- Publisher: Tichenor Bay Books
- Publication date as stated: May 2000
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2283
- Already set (do not supply): none

### Source block (context only)

```text
Author: Janet Fitch
ISBN: 0316284955
Publisher: Tichenor Bay Books
Date (Month/Year): May 2000
```

### Introduction (context only: never use it for content warnings)

```text
And so they went, against Astrid’s better judgment, to visit the woman who genetically had the right to claim Astrid as daughter. After all, Astrid couldn’t protect her foster mother, Claire, forever, could she? White Oleander by Janet Fitch
```

### Performance text (classify this)

```text
Dear Claire,

Yes, I think it would be marvelous if you’d visit. It’s been so long since I’ve seen Astrid, I don’t know if I’d recognize her – and I’m always delighted to meet my loyal readers. I will put you on my visitors list – you’ve never been convicted of a felony, have you? Just teasing.

Your Friend,

Ingrid

It was February, a gray morning so overcast we couldn’t see the Hollywood Hills from our yard. We were going to visit my mother. Claire had set it up. The idea of this meeting was almost too much to bear. I could only lose. My mother could hurt her. Or she could win her over. I didn’t know which was worse. Claire was mine, someone who loved me. Why did my mother have to get in the middle? But, that was my mother, she always had to be the center of attention, everything had to be about her.

I looked in the mirror, imagining what my mother would think of me now. The scars on my face were just the start. I’d been through a few things since then. I wouldn’t know how to be with her now, I was too big to hide in her silence. And now I had Claire to worry about.

I had second thoughts about my clothes too, a long skirt and Doc Martens, thick socks, a crocheted sweater with a lace collar from Fred Segal, where all trendy young Hollywood shopped. My mother was going to hate it. But I had nothing to change into, all my clothes were like that now.

We drove east for an hour. It had been more than two years since I’d last come this way, a very different girl in pink shoes. We drove back along the same blacktop road to the CIW, the steam stack and the water tower, the guard tower that marked the edge of the prison. We parked in the visitors lot.

Claire took a deep breath. “This doesn’t look so bad.” We sat at a picnic table under the blue overhang. I watched the gate where my mother would come in. Claire shivered. She was trying to be brave. “Why are they staring at us like that?

It was cold, but now I was sweating, waiting for my mother. Who knew, maybe they would become friends. Maybe my mother wasn’t playing a game, or not to ugly a one. I saw my mother, waiting while the CO opened the gate. Her hair was long again, forming a pale scarf across the front of her blue dress, she was as nervous as I was. So beautiful. She always surprised me with her beauty. Even when she had just been away for a night, I’d see her and catch my breath. She was thinner than the last time I’d seen her, all the excess flesh had been burned away. Her eyes had become even brighter, I could feel them from the gate. She was very upright, muscular, and tan. She strode up, smiling, but I felt uncertainty in her hands. We looked into each other’s eyes, and I was astonished to find that we were the same height. Her eyes were searching within me, trying to find something to recognize. They made me suddenly shy, embarrassed of my fancy clothes, even of Claire. I was ashamed of the idea that I could escape her, even of wanting to. “Welcome to Valhalla,” she said, shaking Claire’s hand. I tried to imagine how my mother must be feeling right then, meeting the woman I’d been living with, a woman I liked so much I hadn’t written anything about her. Now my mother could see how beautiful she was, how sensitive, the child’s mouth, the heart-shaped face, the delicacy of her neck, her freshly cut hair. Claire smiled with relief that my mother had made the first move. She didn’t understand the nature of poisons.

She looked older than the last time I saw her, lines etching into her tanned face, around the eyes and thin mouth. I winced at her old-fashioned, actressy diction. I could imagine my mother mocking her later to her cellblock sisters. But I couldn’t protect Claire now. It was too late. I saw that the perennial hint of irony in the corners of my mother’s lips had now been etched into a permanent line, the tattoo of a gesture.

“My daughter says you’re an actress.” She wore no sweater in the cold grayness of the morning. The fog suited her, I smelled the sea on her although we were hundred miles from any ocean.

Claire twisted her wedding ring, it was loose on her thin fingers. “To tell you the truth, my career’s a disaster. I blotched my last job so badly, I’ll probably never work again.” Why did she always had to tell the truth? I should have told her, certain people should always be lied to. My mother instinctively felt for the crack in Claire’s personal history, like a rock climber in fog sensing fingerholds in a cliff face. “Nervous?” she said kindly. Claire leaned closer to my mother, eager to share confidences. “It was a nightmare,” she said, and began to describe the awful day.

Overhead the clouds roiled and clotted, like dysentery, and I felt sick. Claire was afraid of so many things, she only went thigh-deep into the ocean because she was afraid of being swept under. So why couldn’t she feel the undertow? My mother’s smile, so kind-looking. They treat actors so badly,” my mother said. “I’ve had it.” “No more. Dragging myself to auditions, just to have them look at me for two seconds and decide I’m too ethnic for orange juice, too classic for TV moms.” “That’s why Astrid and I get along. Scorpio and Pisces understand one another.” My mother didn’t like that we understood each other, Claire and I, could tell by the way she was pulling my hair. “Astrid and I never understood each other. Aquarius and Scorpio. She’s so secretive, haven’t you found that? I never knew what she was thinking.” “We just adore her,” Claire said, and for a moment I saw her my mother saw her. Actressy, naïve, ridiculous. No, I wanted to say stop, don’t judge her based on this. “She’s doing wonderfully well, she’s on the honor roll this year. We’re trying to keep that old grade point average up.” I was mortified and I didn’t want to be. When would my mother have worked with me, hour after hour, to raise the old grade point average?

“Does he have to travel a good deal, your husband? What’s his name again? Ron?” “He’s always gone,” Claire admitted. “He wasn’t even home for Christmas.” “It must be lonely for you,” my mother said. Sadly. So sympathetic. I wished I could get up and run away, but I would never leave Claire here alone with her. “It used to be,” Claire said. “But now I have Astrid.” I was such a traitor. I had betrayed my master. She knew why I’d kept Claire in the background. Because I loved her, and she loved me. Because I had the family I should have had all this time, the family my mother never thought was important, could never give me. “Astrid, do you mind letting us talk for a moment alone? Some grown-up things.” I looked from her to my foster mother. Claire smiled. “Go ahead. Just for a minute.” Like I was a kid who had to be encouraged to get into the sandbox. She didn’t know how long a minute could be, what might happen in a minute.

I got up reluctantly and went over to the fence closest to the road, ran my fingertips over the bark of a tree. I watched them, leaning toward each other over the table. My mother was talking without stopping, low, reasonable, I’d seen her hypnotize a cat this way. Claire was upset. I didn’t care what my mother’s game was. Her time was up. We were leaving, she was staying. She couldn’t screw this up for me, no matter what she said. They both looked up as I rejoined them. My mother glared at me, then veiled it with a smile. “You just remember what I told you.” “I’ll meet you in the car,” she said.

My mother and I watched her go. “What did you tell her?” “ I hear she’s having trouble with her husband.” She smiled sensually, “It’s not you, is it? I know you have an attraction to older men.” “No, it’s not me.” She couldn’t play with me the way she played with Claire. “You stay out of it.” I could see it startled her to have me oppose her. It angered her that I felt I could, but she was controlled, I could see her switch gears. “I have to do what I can for my new friend.” “Just leave her alone.” “Oh, but it’s fun,” my mother said. “Don’t screw it up for me.” “What could I do? I’m a poor prisoner. A little bird with a broken wing.” “If you love me, you’ll help me.” “Help you, darling? I’d rather see you in the worst kind of foster hell than with a woman like that.” She grabbed my wrist, forcing me to look at her. Now she was dead serious. “What are you going to learn from a woman like that?” “How to pine artistically? She stood and kissed me on the cheek, embraced me lightly. “All I can say is, keep you bags packed.” “I think I did well with you mom, don’t you?” “You did,” I told her, gazing out the window so I wouldn’t have to lie to her face. “She really liked you.” A tear rolled down her cheek,” What did she said to you?” “She said that I was right about Ron. That he was having an affair. I knew it anyway, she just confirmed it.” “How would she know,” I said. “For God’s sake, Claire, she just met you.” “All the signs are there,” she sniffled. “I just didn’t want to see them.” Claire was supposed to go to an audition. She had told Ron she would, but she had me call in and say she was sick. Ron was supposed to be home on Friday, but something came up. His trips home were handholds for her, so she could swing from one square on the calendar to the next. When he said he was going to come home and didn’t, she swung forward and grasped thin air, fell. I intercepted a letter from prison from my mother to Claire. In it, my mother advised a love potion to put in his food, but everything in the formula she sent looked poisonous to me. I wanted to hold her close, but something was pushing her away. I didn’t think I could save her anymore. “Claire, you know he’ll be back. He loves you, don’t worry.” I didn’t care if he came back or not. I heard the squeak of the bedsprings as she turned over, the effort it took to get up, stumble the three steps to the door. She tumbled with the lock. I opened the door and she fell back into bed, still wearing that red bathrobe. “I’m so cold,” she mumbled. “Come in with me.” I got in, clothes and all. She put her cold feel on mine, her head on my shoulder. “Stay with me, promise. Don’t leave.” I held her cold hands, rested my head against hers as she fell asleep. Claire was still sleeping when I woke up. I got up, careful not to disturb her, and went out to the kitchen. After a while, I checked on Claire. She was still asleep. The room was dark gray, no morning light penetrated the French doors covered with blinds. She had one hand flung across the top of the pillow. Her mouth was open, but she wasn’t snoring now. “Claire?” I put my face right to hers. She smelled of sherry and something metallic. She didn’t move. I put my hand on her shoulder, shook her gently. “Claire?” She didn’t do anything. I couldn’t hear her breathing. I shook her again. “Claire, wake up.” I yelled at her, hoping she would open her eyes. It was impossible. “Claire.” I screamed into her sleeping face. Nothing. I searched the bedside table, the floor. On the far side, I found the pills on the floor, along with the empty sherry bottle. The pill bottle was open, the pills spilled out, small pink tablets. Butalan, the label said. For Insomnia. Do Not Take With Alcohol. The sounds I was making were no long screams. I knocked the bedside light off the nightstand. I pulled the magnet box from under the bed and threw it across the room. I took her silver-backed hairbrush and threw it overhead like a baseball into the round mirror. I took the phone off the receiver against the headboard until it came apart in my hands, leaving dents in the soft pine. I lay my head on her chest where there was no heartbeat. She was so pale. Cold. Maybe she hadn’t meant to. She would have written a note, explaining everything two or five ways. Maybe all she wanted was to sleep. The house was still. I heard the tick of the clock on the bedside table. A car drove past in the street. Fresh air came through the windows. She lay with her mouth open on the flowered pillow in her red bathrobe in the brightness of the morning.
```

---

## IC-0297: Whiteout

- Title: Whiteout
- Author (byline): Jocelyn Beard
- Work: The Best Women’s Stage Monologues of 1997
- Publisher: Smith & Krauss
- Publication date as stated: 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: REBECCA
- Teaser before the introduction: No
- Spoken words (computed): 1560
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jocelyn Beard
Book: The Best Women’s Stage Monologues of 1997
ISBN: 978-1575251387
Publisher: Smith & Krauss
Date (Month/Year): 1998
```

### Introduction (context only: never use it for content warnings)

```text
Racism is the product of judgment and pride intertwined. The experiences of yesterday determine the judgments of today, and the judgments of today determine the pride of tomorrow. Racism is learned not invented. Racism breeds from suffering. Those who suffer are racist – those who impose suffering are racist. Rebecca explains her pride, her judgments and her suffering in “Whiteout” by Jocelyn Beard.
```

### Performance text (classify this)

```text
REBECCA: I will not sit in this house. The fact that the soles of my shoes have to touch your floors is bad enough... Let me tell you something about me, Miss Creek. Let me tell you something that might help you to understand me, since that's your job. Let me tell you about my Great-grandmother. My Great-grandmother was a slave, Miss Creek. Her name was Effie. (beat) Don't you "oh" me, you...you...Peckerwood piece of white trash! We are all descended from slaves, you ignorant girl. My great-grandmother was a slave. Her name was Effie. She was kept on several plantations outside of Richmond, on the James River. Seems she wasn't much of a worker, but she was smart. Smart enough to keep herself out of the fields and out of the Boss's bed. Smart enough to head north when the war was over and Negroes were free to finally get paid to be slaves. Great-grandmother Effie made her way first to Philadelphia, where she worked for several years in the household of an umbrella tycoon. Can you imagine making your fortune making umbrellas? That's white luck for you. Anyway, there was smart, clever Great-grandmother Effie cooking up a storm for the umbrella tycoon in Philadelphia when, as her own personal luck would have it, one of the umbrella tycoon's houseguests fell in love with her Liquor Pudding...

In the south, Miss Creek, African American cooks labored to concoct countless dishes irresistible to white men... most of them so high in fat that coronary units should be on stand-by whenever they're served. Call it a sweet revenge. Liquor pudding was Effie's specialty, and a rich politician from New York City by the name of Benjamin Morse fell in love with it. He offered Effie three times what the umbrella tycoon was paying her to come and cook for him in New York and she said, "Yes, Boss. That do sound good to me." She was quite lucky. Great-grandmother Effie grew famous in New York for her unusual culinary skills and for her beauty. In fact, Morse's youngest son, Ezekial, had ardently courted Effie since her arrival. She eventually bore him three sons and three times that in scandal.

Fortunately, the younger Morse was a responsible white boy, and he set Effie up in a little house in Cold Spring, right on the Hudson River, where he continued to visit even after his marriage to a Connecticut heiress. My grandfather, Thomas Morse, grew up with his mother and brothers in that little house on the river and they wanted for nothing. Thomas was able to go to college, and then had the audacity to start his own law practice in Poughkeepsie, New York, in 1922. He married the daughter of one of his first clients, a man by the name of Euclid Strange who owned an apple orchard deeded to him by a grateful former employer. My grandmother, Tabitha Strange had grown up on that apple orchard, up in the Hudson Highlands. Grandma Tabby bore Effie six beautiful grandchildren: Euclid, Thomas, Nathan, Philip, Marie and my mother, Willa. Uncle Euclid and Nathan went into law with Grandfather, as did my mother. By the time I was born, Morse, Morse and Wooley was one of the biggest firms in the valley. A black law firm. It was a freak of nature. Both my parents were attorneys. I grew up in a small town named Red Hook that was as white as white can be. We were as white as white can be. Our neighbors were white, our friends were white, we spoke like whites, we ate like whites, we were white. I went to a private girl's school with a bunch of other white girls and then on to Harvard and Harvard Law. On the day I was graduated I received a rare and unexpected summons from Cold Spring. I was to present myself to Great-grandmother Effie without delay. I'd only met her a handful of times in my life and truth be told, she had always terrified me. But I was young, fancied myself white and had a J.D.L from Harvard in my pocket, so I drove down to Cold Spring as requested. I'd never been to the house, nor had anyone prepared me for it. The “me” that you seem to think you know was last seen standing in that driveway on that hot June day.

From the driveway, you followed a path through thick forsythia and hydrangea trees to a clearing where Effie's house had stood since a Dutch farmer had built it in the early eighteenth century. As I stood there, staring the house...or what had become of it...I didn't think of Holland, I thought of Senegal. Effie had used the years to transform that little Dutch colonial into her memory of the hut in which her mother had been born in Senegal. She'd done it all by herself. She'd even replaced the slate roof with sweet-smelling thatch. I must tell you, Miss Creek, that it quite took my breath away. It was like a memory of a dream. I found her in an herb garden on the other side of the house. She was singing...in Senegalese, dressed in a batik robe of the brightest blues I'd ever seen. Her hair was white, and piled on her head in braids. She must have smelled me, standing there behind her, for she stopped singing and slowly turned around. Her face was ancient, but somehow, still beautiful. In fact, the most startling thing about her, I remember, was that she stood erect; as if life and all its burdens had no claim on her. As if she'd never been a slave. She eyed me up and down, and then she did something I never would have expected.

She laughed, oh good lord how she laughed! She took one look at me in my white clothes with my straightened hair and the look of white concern on my face and she just laughed. She walked with a cane that she didn't seem to need, and she poked it at me and said: "Look at you, child. All dressed up and no place to go." Well, I wasted no time informing her that I did in fact have many places to go...but she cut me off with another poke of her cane and said, "You listen to me, girl child. I got no time to be listening to no pretend white girl, so you just listen to me. By this time next year I'll be dead. My bones be crushed and ground to paste the earth. Now, I been carrying something...carrying it with me all the way from Virginia, and it's heavy, girl child, too heavy for me to take with me to the grave. I got to give it to someone to carry to the next one...and you're the one who has to take it. You. Only you." She reached inside her gown, and pulled out a long necklace. I remember her hands...like little brown spiders...running up and down the necklace as they undoubtedly had every day for seventy years. "This is what I got to give to you, girl child," she said, "but I'm going to keep it on just a little while longer while I introduce you to them."

(As she slowly pulls the necklace out of her own dress.) It was long, white pearls held together by black and white strands... (She holds up the first "pearl," which is actually a human tooth, as Effie.) "This be Rummy. The Boss man done whipped him dead. Whipped him so bad that the blood spray all over his Nile green frock coat that little Bess done took more'n a month to sew. Rummy die screamin'. (The next "pearl. ") This be Old Paw. The Boss Man done whipped him dead. Old Paw my father's brother. Old Paw keep me from the men on the boat over. Old Paw die screamin'. (The next "pearl. ") This be Ben. The Boss Man done whipped him dead. Ben and me was in love. I had Ben's baby in me but the Boss Man punched it out. Ben die screamin'. (The next "pearl. ") This be Fifi. The Boss Man done whipped her dead. Fifi was my mama. She held me close in the boat over and not even let go on the block. Fifi slap Boss Man when he take my baby. Fifi die screamin'.”

These are the teeth and the hair of my family. This is all I have. This pitiful ossuary. This is all I have to prove who and what I am. I don't have someone's wedding gown, passed down through generations...I don't have corsages, carefully preserved in plastic...I don't have scrapbooks or photos...all I have are these, yanked from the skulls of my forbears... these, and a great recipe for Liquor Pudding. Great-grandmother Effie gave me a powerful gift that day in her garden, Miss Creek; she gave me the gift of a secret identity. She gave me my destiny. On that day I was made a racist, Miss Creek. Just as you have been made a racist. What you need to know...what isn't in my FBI profile, is that my racist agenda is no less savage than yours.

That is why I cannot and why I will not touch a single thing in this particular house. Do I make myself clear?
```

---

## IC-0298: Who’s Afraid of Virginia Woolf?

- Title: Who’s Afraid of Virginia Woolf?
- Author (byline): Edward Albee
- Work: Not specified
- Publisher: Signet Books
- Publication date as stated: Aug 1988
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MARTHA, GEORGE
- Teaser before the introduction: Yes
- Spoken words (computed): 1950
- Already set (do not supply): none

### Source block (context only)

```text
Author: Edward Albee:
ISBN: 978-0451158710
Publisher: Signet Books
Date (Month/Year): Aug 1988
```

### Introduction (context only: never use it for content warnings)

```text
Who's Afraid of Virginia Woolf? explores a marriage steeped in manipulation and emotional abuse. George and Martha’s innocent banter quickly pivots to a bitter and venomous exchange, especially when the topic of their thinly veiled psychological warfare turns to their son. As the truth is revealed, the painful illusions that sustain a toxic relationship are finally exposed. Can they – can anyone – survive a life built on deception?

Who’s Afraid of Virginia Woolf by Edward Albee
```

### Performance text (classify this)

```text
MARTHA: (Pg 15-16) Poor Georgie-Porgie, put-upon pie! [as he sulks] Awww. . . what are you doing? Are you sulking? Hunh? Let me see. . . are you sulking? Is that what you're doing?

GEORGE: [very quietly] Never mind, Martha. . .

MARTHA: AWWWWWWWWWW! [no reaction] Hey! [no reaction] HEY! [GEORGE looks at her, put-upon - she sings to the tune of *Who’s Afraid of the Big Bad Wolf] "Who's afraid of Virginia Woolf, Virginia Woolf, Virginia Woolf. . . Ha, ha, ha, Hal” [no reaction] What's the matter . . . didn't you think that was funny? Hunh?

GEORGE: [patiently] It was very funny; yes. (Pg 18) Just don't start in on the bit about the kid, that's all.

MARTHA: (Pg 16) [after a moment's consideration] You make me puke! (Pg 19) [threatening] He's mine as much as he is yours. I'll talk about him if I want to.

GEORGE: I'd advise against it, Martha.

MARTHA: SCREW you!

MARTHA: (Pg 49) [to audience] George’s biggest problem about . . . ha, ha, ha, HA! . . . about our son, is that deep down in the private-most pit of his gut, he’s not completely sure it’s his own kid.

GEORGE: [deeply serious] My God, you're a wicked woman. [to audience] Martha’s lying. [MARTHA laughs] the one thing in this whole sinking world that I am sure of is my partnership in the . . . creation of our . . . son. (Pg 55-56) I warn you, Martha, it's going to make me angry.

MARTHA: [laughing at him] Oh, it is, is it?

GEORGE: [very quietly] I warn you. [turns his back to her]

MARTHA: You getting angry, baby? Hunh? (Pg 75) [to audience] When our son was just a little boy he used to . . .

GEORGE: Don’t, Martha . . .

MARTHA: . . . he used to throw up all the time, because of George

GEORGE: I said, don’t! The real reason [spits out the words] our son . . . used to throw up all the time was that he couldn’t stand you fiddling at him all the time, with your liquor breath on him.

MARTHA: Yeah? And I suppose that’s why he ran away from home twice in one month, too. [to audience] Six times in one year!

GEORGE: [to audience, matter-of-factly] Our son ran away all the time because Martha here used to corner him. He used to run up to me when I’d get home and say, “Mama’s always coming at me.” That’s what he’d say.

MARTHA: Liar! (Pg 79) [threateningly] You son of a . . .

GEORGE: [quietly] (Pg 95) Be careful, Martha . . . I’ll rip you to pieces. (Pg 120) SNAP!

MARTHA: [a little afraid] Truth or illusion, George. Doesn’t it matter to you . . . at all?

GEORGE: Now; we got one more game to play. And it’s called bringing up baby.

MARTHA: (Pg 121-123) [pleading] No more games.

GEORGE: [quietly triumphant] One more, Martha. One more game.

MARTHA: [almost in tears] No more games . . . please. It’s games I don’t want. No more games.

GEORGE: Aw, sure you do, Martha . . . original game-girl and all, ‘course you do.

MARTHA: [tenderly; moves to touch him] Please, George, no more games; I . . .

GEORGE: [slapping her moving hand with vehemence] Don’t you touch me! [grabbing her hair, pulling her head back] Now, you listen to me, Martha; you’ve had quite a night for yourself, and you can’t just cut it off whenever you’ve got enough blood in your mouth. I want you on your feet and slugging, sweetheart, because I’m going to knock you around, and I want you up for it. [releases her and pushes her away]

MARTHA: All right, George. What do you want?

GEORGE: An equal battle, baby; that’s all. I want you mad

MARTHA: I’m MAD!!

GEORGE: Good -- we’re going to play this one to the death.

MARTHA: Yours!

GEORGE: [calmly] You’d be surprised . . . (Pg 125) [to audience] Now, take our son . . .

MARTHA: George . . .

GEORGE: [too kindly] Yes, Martha?

MARTHA: Just what are you doing?

GEORGE: Why love, I was talking about our son.

MARTHA: Don’t

GEORGE: [to audience] Isn’t Martha something? Here we are, on the eve of our boy’s homecoming, the eve of his twenty-first birthday, the eve of his majority . . . and Martha says don’t talk about him. But I want to, Martha! It’s very important we talk about him.

MARTHA: Just . . . don’t

GEORGE: (Pg 126) Well, now; let’s see. He’s a nice kid, really, in spite of his home life; I mean, most kids’d grow up neurotic, what with Martha here carrying on the way she does: trying to break the bathroom door down to wash him in the tub when he’s sixteen, because it’s her baby-poo.

MARTHA: That’s enough!

GEORGE: Well, do you want to take over?

MARTHA: ALL RIGHT! [by rote; a kind of almost-tearful recitation] Our son. You want our son? You’ll have it.

GEORGE: You want a drink, Martha?

MARTHA: (Pg 127-128) [from far away] What, George?

GEORGE: Your recitation, please . . . “Our son . . . “

MARTHA: Our son. Our son was born in September, a night not unlike tonight. . . twenty . . . one . . . years ago. It was an easy birth . . .

GEORGE: Oh, Martha; no. You labored . . . how you labored.

MARTHA: It was an easy birth . . . once it had been . . . accepted, relaxed into.

GEORGE: Ah . . . yes. Better.

MARTHA: I was young, and he was a healthy child, a red, bawling child . . .

GEORGE: [to audience] Martha thinks she saw him at delivery . . .

MARTHA: . . . with a full head of black hair which later, later, became blond as the sun, our son.

GEORGE: He was a healthy child.

MARTHA: And I had wanted a child. . . oh, I had wanted a child.

GEORGE: [prodding her] A son? A daughter?

MARTHA: A child! [quieter] A child. And I had my child.

GEORGE: Our child.

MARTHA: [with great sadness] Our child. And we raised him . . . [laughs, briefly, bitterly] yes, we did; we raised him . . .

GEORGE: With teddy bears and an antique bassinet from Austria . . . and no nurse.

MARTHA: . . . with teddy bears and a pale blue bed with cane at the headboard, cane which he wore through . . . finally . . . with his little hands . . . in his . . . sleep . . .

GEORGE: . . . nightmares . . . [soft chuckle, head-shaking in disbelief]

MARTHA: . . . sleep . . . He was a restless child . . . and animal crackers, and the bow and arrow he kept under his bed. . .

GEORGE: Why? Why, Martha?

MARTHA: . . . for fear . . . for fear of . . .

GEORGE: For fear. Just that: for fear.

MARTHA: (Pg 129-132) [vaguely waving him off; going on] And as he grew . . . he walked between us . . . [spreads her hands]. . . a hand out to each of us for what we could offer by way of support, affection, teaching, even love . . . and these hands, still, to hold us off a bit, for mutual protection, to protect us all from George’s . . . . weakness . . . and my greater strength . . . to protect himself . . . and us. So wise. Of course, this state, this perfection . . . couldn’t last. Not with George . . . not with George around.

GEORGE: [to audience] There; you see? I knew she’d shift.

MARTHA: A drowning man takes down those nearest. George tried, but, oh, God, how I fought him.

GEORGE: [a satisfied laugh]Ahhhhhhh. How did I try, Martha? How did I try?

MARTHA: How did you . . . what? No! No . . . he grew . . . our son grew . . . up; he is grown up; he is away at school, college. He is fine, everything is fine.

GEORGE: [mocking] Oh, come on Martha! You can’t cut a story off like that, sweetheart. You started to say something . . . now you say it!

MARTHA: No!

GEORGE: Well, I will. [to audience] You see, Martha stops just when the going gets good. Now, Martha here, is a misunderstood little girl; she really is. She has a tiny problem with liquors – she can’t get enough . . .

MARTHA: [without energy] No more, George.

GEORGE: . . . and on top of all that she has a son who fought her every inch of the way, who didn’t want to be turned into a weapon against his father, who didn’t want to be used as a goddamn club whenever Martha didn’t get things like she wanted them!

MARTHA: [rising to it] Lies! Lies !!

GEORGE: Lies? All right. A son who would not disown his father, who came to him for advice, for information, for love that wasn’t mixed with sickness – and you know what I mean, Martha! – who could not tolerate the slashing, braying residue that called itself his MOTHER. MOTHER? HAH!!

MARTHA: [cold] A son who was so ashamed of his father he asked me once if it – possibly – wasn’t true, as he had heard, from some cruel boys, maybe, that he was not our child; who could not tolerate the shabby failure his father had become . . .

GEORGE: Lies!

MARTHA: Lies? Who would not bring his girlfriends to the house . . .

GEORGE: . . . in shame of his mother . . .

MARTHA: . . . of his father! A son who spends his summers away from his family on any pretext because he can’t stand the shadow of a man flickering around the edges of a house . . .

GEORGE: . . . who spends his summers away because there isn’t room for him in a house full of empty bottles, lies, and strange men . . .

MARTHA: Liar!! The one thing I’ve tried to carry unscathed through the sewer of this marriage, through the derision and the laughter . . . through one failure after another; the one person I have tried to protect, to raise above the mire of this vile crushing marriage; the one light in all this hopeless darkness . . . our son.

GEORGE: (Pg 133-134) Ho-ho! Got a little surprise for you, baby. I’M RUNNING THIS SHOW! Sweetheart, I’m afraid I’ve got some bad news for you . . . for us, of course. Some rather sad news.

MARTHA: [afraid, suspicious] What is this?

GEORGE: [oh, so patiently] Well, Martha, while you were out of the room, I don’t know where, hell, you must have been somewhere [little laugh] the doorbell rang . . . It’s hard to tell you, Martha . . .

MARTHA: [a strange throaty voice] Tell me.

GEORGE: It was good old Western Union. A telegram for us. Martha . . . I can hardly bring myself to say it . . . [sighing heavily] (Pg 135-136) Martha . . . I’m afraid our boy isn’t coming home for his birthday.

MARTHA: Of course he is. I say he is!

GEORGE: Martha [long pause] our son is . . . dead. [silence] He was . . . killed late in the afternoon . . . [silence -- a tiny chuckle] on a country road, with his learner’s permit in his pocket, he swerved, to avoid a porcupine, and drove straight into a . . .

MARTHA: [rigid fury] YOU . . . CAN’T . . . DO . . . THAT!

GEORGE: . . . large tree. [quietly, dispassionately] I thought you should know.

MARTHA: [quivering with rage and loss] NO! NO! YOU CANNOT DO THAT! YOU CAN’T DECIDE THAT! I WILL NOT LET YOU DECIDE THESE THINGS!

GEORGE: We’ll have to leave around noon. There are matters of identification, naturally, and arrangements to be made.

MARTHA: YOU CAN’T DO THIS!

GEORGE: [right in Martha’s face] You don’t seem to understand, Martha; I haven’t done anything. Now, pull yourself together. Our son is DEAD! We got a telegram; there was a car accident and he’s dead. POUF! Just like that! Now, how do you like it?

MARTHA: [a howl which weakens into a moan] Noooooooooo. [pathetic] No; no, he is not dead; he is not dead. You can’t kill him! You can’t have him die!

GEORGE: [sarcastically] That’s right, Martha; I’m not God. I don’t have the power over life and death, do I? There was a telegram.

MARTHA: Show it to me! Show me the telegram!

GEORGE: [with a straight face] I ate it. (Pg 137-138) [with disgust] You know the rules, Martha! For Christ’s Sake, you know the rules!

MARTHA: He is our child! GEORGE: And I have killed him!

MARTHA: No! GEORGE: Yes!

MARTHA: [great sadness and loss] You have no right . . . you have no right at all . . .

GEORGE: [tenderly] I have the right, Martha. We never spoke of it; that’s all. I could kill him any time I wanted to. You broke our rule. You mentioned him to someone else.

MARTHA: [crying] I forget! I want to mention him . . . but I . . . hold on . . . I hold on . . . Oh, George, you’ve pushed it over the edge. You didn’t have to . . . kill him. (Pg 75) [to audience] When our son was just a little boy he used to . . .

GEORGE: (Pg 138) [softly] It will be dawn soon. I think the party’s over. Martha . . . time for bed.

MARTHA: You didn’t have to have him die, George.

GEORGE: (Pg 139-140) It was time. [long silence] It will be better.

MARTHA: Just . . . us?

GEORGE: Yes. Are you all right?

MARTHA: Yes . . . No.

GEORGE: [puts his hand gently on her shoulder; she puts her head back and he sings to her, very softly] Who’s afraid of Virginia Woolf, Virginia Woolf, Virginia Woolf

MARTHA: I am George . . . I am.
```

---

## IC-0299: Wintergirls

- Title: Wintergirls
- Author (byline): Laurie Halse Anderson
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: LIA
- Teaser before the introduction: Yes
- Spoken words (computed): 1161
- Already set (do not supply): none

### Source block (context only)

```text
(none)
```

### Introduction (context only: never use it for content warnings)

```text
The danger of habit. When you train yourself to do something over and over again, how do you break the rigorous training you’ve set up for yourself? In the following selection, Lia has spiraled into not eating. Counting calories, competing with her best friend to be the thinnest, Lia is caught and monitored by family, but nothing is enough to stop her from returning to old habits. What does it take to make a change? To turn toward recovery?

Wintergirls by Laurie Halse Anderson.
```

### Performance text (classify this)

```text
LIA: (Pg 7) . . . When I was a real girl, with two parents and one house, breakfast was granola topped with fresh strawberries, always eaten while reading a book propped up on the fruit bowl.

(Pg 5) “Why don’t you have one of those muffins?” [My stepmom, Jennifer, asks.] “I bought oranges yesterday, or you could have toast or frozen waffles.”

Because I can’t let myself want them because I don’t need a muffin (410), I don’t want an orange (75) or toast (87), and waffles (180) make me gag.

(Pg 7) No. I can’t go there. I won’t think. I won’t look.

I won’t pollute my insides with Bluberridazzlepops or muffins or scritchscratchy shards of toast, either. Yesterday’s dirt and mistakes have moved through me. I am shiny and pink inside, clean. Empty is good. Empty is strong.

LIA: (Pg 27) The first time . . . (Pg 9) Mom and Dad rushed in, side by side for a change, happy that I was not dead. A nurse handed my chart to my mother. She read through it and explained the disaster to my father and then they fought, a mudslide of an argument that spewed across the antiseptic sheets and out into the hall. I was stressed/overscheduled/manic/no -- depressed/no -- in need of attention/no -- in need of discipline/in need of rest/in need/your fault/your fault/fault/fault. They branded their war on this tiny skin-bag of a girl.

Phone calls were made. My parents force-marched me into New Seasons . . .

They locked me up and dripped sugar water into my empty veins . . . (Pg 27) The first time they admitted me, this body weighed 093.00 pounds.

(Pg 28) I was a good girl because I didn’t poke holes in my skin, or write depressing poetry, and I ate and ate. They stuffed me like a pink little piggy ready for market. I bit, chewed, swallowed day after day and lied, lied, lied. (Who wants to recover? It took me years to get that tiny. I wasn’t sick; I was strong.) But staying strong would keep me locked up. The only way out was to shove in food until I waddled.

Four weeks later, the gates opened. Mom drove me home and we pretended none of it ever happened, except for the meal plans and the rules and the appointments and the scales and the hurricane of my mother’s disappointment.

(Pg 46) The doctors told Dad to buy a Blubber-O-Meter 3000, a bathroom scale with a giant dial that was easy to read. Jennifer had to do the dirty work, weighing me in my tattered yellow robe to make sure I stayed fat. For the first couple of months, she measured my sins every morning and called in the results to my doctor once a week. The ugly numbers made me cry.

Everyday weighing became every-other-day weighing became every-Tuesday weighing because none of us wanted to do it in the first place . . .

(Pg 189) Adrenaline kicks in when you’re starving. That’s what nobody understands. Except for being hungry and cold, most of the time I feel like I can do anything. It gives me superhuman powers of smell and hearing. I can see what people are thinking, stay two steps ahead of them.

(Pg 145) I’m hungry I need to eat.
I hate eating.
I need to eat.
I hate eating.
I need to eat.
I love not-eating.
(Pg 161) Why? You want to know why?

Go to school to jump through hoops, sit up and beg, and roll over on command. Listen to the whispers that curl into your head at night, calling you ugly and fat and stupid and bitch and whore and worst of all “a disappointment.” Puke and starve and cut and drink because you don’t want to feel any of this. Puke and starve and cut and drink because you need an anesthetic and it works. For a while. But then the anesthetic turns into poison and by then it’s too late because you are mainlining it now, straight from your soul. It is rotting you and you can’t stop. Look in a mirror and find a ghost. Hear every heart-beat scream that everysinglething is wrong with you. “Why?” is the wrong question. Ask “Why not?” (Pg 46-47) I change into the yellow robe in my bedroom and make sure the quarters I sewed into the pockets aren’t making them droop. When I get to the bathroom, Jennifer is fixing her eyeliner in the mirror. I step on the scales. 107.00 fake pounds.

(Pg 220) Alone . . . I strip, to weigh my faults and measure my sins . . . (Pg 52-53) as I step on the scale, I open my eyes. 099.00 pounds. I am officially standing on Goal Number One.

Goal Number Two is 095.00, the perfect point of balance. At 095.00, I am pure. Light enough to walk with my head up, meaty enough to fool everyone.

At 090.00, I soar. That’s Goal Number Three.

(Pg 220) 089.00.

I could say I’m excited, but that would be a lie. The number doesn’t matter. If I got down to 070.00, I’d want 065.00. If I weighed 010.00, I wouldn’t be happy until I got down to 005.00. The only number that would ever be enough is 0. Zero pounds, zero life, size zero, double-zero, zero point.

(Pg 8) I [drive], windows down, music cranked, flying to the SATs.

Did I eat breakfast? Of course not. Did I eat dinner the night before, or lunch, or anything?

The car in front of [me] brake[s] as the traffic light turn[s] yellow, then red. My edges blur. The car in front disappear[s]. The steering wheel, the dashboard, vanish.

(Pg 271) The light beyond my eyes flashflashflashes with a hundred futures for me. Doctor. Ship’s captain. Forest ranger. Librarian. Beloved of that man of that woman or those children or those people who voted for me or who painted my picture. Poet. Acrobat. Engineer. Friend. Guardian. Avenging whirlwind. A million futures - not all pretty, not all long, but all of them mine.

(Pg 8) When I w[a]ke up, the emt-person and a cop [are] frowning. My blood pressure that of a cold snake. My heart [is] tired. My lungs [need] a nap.

(Pg 266) Two days later, (Pg 274-276) my third visit to New Seasons is the longest one yet, a marathon, not a sprint to the exit. No games this time. No midnight exercise parties in the shower for me. No dumping my food in the plants or sticking it in my underwear or bribing an attendant to lie about my intake.

The concept of eating is scary. I put all of the bites in my mouth and try not to count. It’s hard. Food is life. I exhale, take another breath. Food is life. And that’s the problem. When you’re alive, people can hurt you. It’s easier to lock everybody out. But it’s a lie.

Food is life. I have no idea how much I weigh. This scares me to death, but I’m working on it. I am beginning to measure myself in strength, not pounds. Sometimes in smiles.

I am learning how to taste everything.
```

---

## IC-0300: Within the Ghostly Mansion’s Labyrinth

- Title: Within the Ghostly Mansion’s Labyrinth
- Author (byline): Don Nigro
- Work: Glamorgan and Other Plays
- Publisher: Samuel French, Inc.
- Publication date as stated: 1966
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MRS WINCHESTER
- Teaser before the introduction: Yes
- Spoken words (computed): 1211
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dan Nigro
Book: Glamorgan and Other Plays
ISBN: 978-0573695919
Publisher: Samuel French, Inc.
Date (Month/Year): 1966
```

### Introduction (context only: never use it for content warnings)

```text
The Winchester Mystery House is a well-known California mansion that was under construction continuously for 38 years, and is reported to be haunted. It once was the personal residence of Sarah Winchester, the widow of gun magnate William Wirt Winchester, but is now a tourist attraction. Under Winchester's day-to-day guidance, its "from-the-ground-up" construction proceeded around-the-clock, without interruption, from 1884 until her death on September 5, 1922, at which time work immediately ceased. The cost for such constant building has been estimated at about US $5.5 million According to popular belief, Winchester thought the house was haunted by the ghosts of individuals killed by Winchester rifles, and that only continuous construction would appease them. It is located at 525 South Winchester Blvd. in San Jose, California. In Within the Ghostly Mansion’s Labyrinth by Don Nigro we hear the Sarah Winchester’s story directly.
```

### Performance text (classify this)

```text
MRS. WINCHESTER, a well dressed old woman, speaks from within her dark, strange house in the year 1919.

MRS WINCHESTER: There are one hundred sixty rooms in my house. It has turrets and gables, spire and peaks, gingerbread and gargoyles, wildly sloping roofs, rooms with thirteen windows, chandeliers with thirteen lights, thirteen bathrooms, staircases with thirteen steps. One staircase has forty-four steps, but it’s only ten feet high – teeny tiny little steps the cat likes very much. Stairways that lead to nowhere, upside down stairways, elevators that skip all but one floor, doors that open onto sudden, terrible drops, dead ends, secret passages, labyrinth within labyrinth. It is all because of the ghosts you see.

MRS WINCHESTER: It all began that terrible year they took my husband and my only child and buried them in the ground. My despair was like drowning in the ocean. And then, in desperation, and without much hope, I went to a séance, to try and speak to my lost ones, and the medium told me that the spirit of my dead husband was standing right beside me, holding a skeleton key, the key to a house that did no yet exist. The medium said my husband had a task which only I could do for him. He was the heir, you see, to the Winchester rifle fortune. His ghost said I must build a great house of the spirits of all those who over the years had been killed by Winchester rifles. And thus was born the great mission of my life. I sold my house in New Haven and headed west, certain that my husband’s ghost would tell me where to stop and build the ghostly mansion. And here, in the Santa Clara valley, I came upon a half-constructed house almost hidden in the trees, and the spirits began shrieking in my head, singing opera, banging on pots and pans, doing somersaults and cartwheels, bouncing on giant springs, playing the accordion and clog dancing, so I thought, well, this must be the place. So I bought the half-done house

When I spoke to the builder about my plans to construct a home for the ghosts of dead rifle victims, the idiot began to treat me as if I was a crazy woman. But it didn’t matter.

A person with enough money can always find a carpenter for any project. So I spent the next thirty odd years building – adding on, tearing down at times, but mostly building rooms and floors and wings and steeples onto the house. I follow the bidding of the spirit world in this, and the spirits are impatient, so I must be as well. The spirits tell me, and I build.

Often I hold banquet for my ghostly friends. Thirteen places are set, for myself and the ghosts. Once I had a presentiment that a terrible flood would soon engulf the universe, so I had an ark built in the back yard, and lived in it for six years, but finally I grew tired of the animal smell and began to wonder if the ghosts had not been playing a malicious trick on me. So I moved back into the house.

I am very particular about whom I allow in this house. I wouldn’t let the blowhard Teddy Roosevelt in the door. All that bully this and bully that and up San Juan Hill. Goodness. What a silly man. And I didn’t like his mustache, either. I did invite Houdini once. He was charming, I thought, but the ghosts took a powerful dislike to him, and kept dropping dead mice from the chandelier into his soup. I took him to a far part of the house and ditched him for a lark, through a secret passage in the lavatory. I never saw him again, but I presume he must have found his way out, eventually, as somebody named Houdini is still running around out there, getting shot out of cannons or something, isn’t he?

In the Blue Room, which is a small chamber with no windows, I hold my séances. At midnight a bell rings and I enter in a long gown, decorated with occult symbology. O one but myself and the ghosts is allowed in this room. Here the spirits whisper secrets to me. Often of late I cannot sleep, and wander the house at night, spirits trailing along after me like yapping, slightly crazed puppies. I play a game sometimes of moving about the house in the dark until I’m lost. But I am never lost, and always lost. It is a dangerous game, considering the odd geography of the house, but all games are dangerous.

I will tell you a secret. In the old days, I rejected the primitive idea that the spirits of the dead were anything to fear. I knew they were my friends. I had built a lovely house for them, gaping gunshot wounds and all. But now that I have spent the better part of my life surrounded by the dead, I must tell you, I have learned to fear them. Oh, many seem harmless enough, too much wrapped up in their own grief to hurt anybody. But others, there are others – darker things.

Sometimes I think perhaps they are trying to murder me. I have heard of a man named Pendragon who constructed a similar house in the early part of the last century in Ohio somewhere, but his house was less cleverly designed than mine, and one night ghosts caught up with him and killed him.

I wonder perhaps if in fact I have not constructed this place, this strange eccentric labyrinth, not to please and amuse the ghosts but to confuse and preoccupy them so they can’t get to me. I hide from them, sleeping in different rooms each night, an sometimes under the stairways, or on the roof, but the spirits always seem to sniff me out.

In the year nineteen hundred and six there was a horrible shaking and rumbling all over the house. I was thrown violently out of my bed and onto the chamber pot, and I was convinced that the ghosts had finally come to destroy me. The servants tell me it was just some earthquake in San Francisco. A likely story. But soon I think the spirits will corner me in some dead-ended corridor and then rip out my throat and leave me gaping, and the servants, who believe I’m mad, will find me in the center of a bloody finger-painting in the morning.

I do not wish to alarm you. I do not wish to be morbid. But the truth is, I think the dead do not love us. No. The dead hate and fear us. They resent us. They resent our suit of living flesh, and our capacity to create, and no matter how complex the construction of your labyrinth, sooner or later they will come upon us, we turn a corner and come face to face, a hideous, rotting, face, as in the mirror, and they reach out their skeleton fingers towards us and we are lost. We are utterly, hopelessly, eternally lost, and in our loneliness and our despair we wander the dark and twisted labyrinth of hell forever.
```

---

## IC-0301: The Woman Who Walked Into Doors

- Title: The Woman Who Walked Into Doors
- Author (byline): Roddy Doyle
- Work: Not specified
- Publisher: Penguin Books
- Publication date as stated: Jan 1997
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: PAULA, CHARLO, LEANNE, NICOLA
- Teaser before the introduction: Yes
- Spoken words (computed): 2335
- Already set (do not supply): none

### Source block (context only)

```text
Author: Roddy Doyle
ISBN: 978-0140255126
Publisher: Penguin Books
Date (Month/Year): Jan 1997
```

### Introduction (context only: never use it for content warnings)

```text
In Ireland, the euphemism "she walked into a door" is so loaded with grim implications of domestic abuse that it is usually whispered, not spoken. According to Women’s Aid of Ireland, one third of women never relate their experiences to anyone and simply try to survive – as well as to protect their children in many instances – as best they can on their own. – Many people ask . . . Why don’t they just leave? And in Paula Spencer’s story, perhaps we can understand exactly that. Why?? The Woman Who Walked into Doors by Roddy Doyle
```

### Performance text (classify this)

```text
*NOTE: Roddy Doyle is an Irish author and this would be the perfect piece to try out your Irish dialect.

PAULA: My name is Paula Spencer. I am thirty-nine years old. I was married for eighteen years. My husband left me. I threw him out. His name was Charles Spencer; everybody called him Charlo.

THE FIRST TIME IT HAPPENED . . . . . .

PAULA: He lost his temper. And he hit me. It was as simple as that. He sent me flying across the kitchen. I hit the sink and fell. I felt nothing, only shock. And a spinning in my head. I knew nothing for a while, where I was, who was with me, how come I was on the floor. Then I saw his feet, then his legs, making a triangle with the floor. He seemed way up over me. Miles up. I had to bend back to see him. Then he came down to meet me.

CHARLO: Y'alright?

PAULA: His eyes were going all over my face, every inch and corner. Looking, searching. Looking for marks, looking for blood. He was worried. His face was full of worry and love. He was scared.

CHARLO: You fell, he said.

PAULA: I didn't - I wouldn't do what he wanted, he was in his moods, I was being smart, he hated me being pregnant, I wasn't his little Paula any more - and he drew his fist back and he hit me. He wanted to hurt me. And he did. OR . . . . I'd been too near him; he hadn't realised. He'd only been warning me. He didn't know his own strength. He had things on his mind. Anything. It wouldn't happen again. It had been a mistake. We'd laugh about it later. Remember the time. We did laugh about it later. That night. And the time after that. And the time after that. Many other nights. Until I couldn't laugh any more. I wouldn't let myself. Nothing came out when I opened my mouth. Only pain.

Someone once told me that we never remember pain. Once it's gone it's gone. A nurse. She told me just before the doctor put my arm back in its socket. She was being nice. She'd seen me before. -I fell down the stairs again, I told her. No questions asked. What about the burn on my hand? The missing hair? The teeth? I waited to be asked. Ask me. Ask me. Ask me. I'd tell her. I'd tell them everything. Look at the burn. Ask me about it. Ask. . . . No.

The doctor never looked at me. He studied parts of me but he never saw all of me. He never looked at my eyes. Drink, he said to himself. I could see his nose moving, taking in the smell, deciding. I am an alcoholic. I've never admitted it to anyone. I've never done anything about it; I've never tried to stop. I think I could if I really wanted to, if I was ready. I've always liked a drink. I don't remember when I stopped liking it and started needing it. It crept up on me, I suppose.

Being hit by Charlo the first time knocked everything else out of me. One day I was Mrs Paula Spencer, a young wife and soon to be a mother, soon moving into a new house, in a new place, making my husband's dinner, timing it so it would be just ready for when he came in from work. Then I was on the floor and that was the end of my life. The future stopped rolling in front of me. Everything stopped.

I keep blaming myself. After all the years and the broken bones and teeth and torture I still keep on blaming myself. I can't help it. What if? What if? He wouldn't have hit me if I hadn't . . . none of the other fists and belts would have followed if I hadn't. . . He hit me, he hit his children, he hit other people - and I keep blaming myself. For provoking him. For not loving him enough; for not showing it. Did you fall down the stairs, Paula? Did you walk into a door, Paula? What made him do that, Paula? What made you do that, Paula? Did you say something to him, Paula? No. No. No! I'm innocent. I'm innocent. I'm innocent. He. Hit. Me. Ask me. Ask me. Ask me. Here goes.

Broken nose. Loose teeth. Cracked ribs. Broken finger. Black eyes. I don't know how many; I once had two at the same time, one fading, the other new. Shoulders, elbows, knees, wrists. Stitches in my mouth. Stitches on my chin. A ruptured eardrum. Burns. Cigarettes on my arms and legs. Thumped me, kicked me, pushed me, burned me. He butted me with his head. He held me still and butted me; I couldn't believe it. He dragged me around the house by my clothes and by my hair. He kicked me up and he kicked me down the stairs. Bruised me, scalded me, threatened me. For seventeen years. Hit me, thumped me, raped me. Seventeen years. He threw me into the garden. He threw me out of the attic. Fists, boots, knee, head. Bread knife, saucepan, brush. He tore out clumps of my hair. Cigarettes, lighter, ashtray. He set fire to my clothes. He locked me out and he locked me in. He hurt me and hurt me and hurt me. He killed parts of me. He killed most of me. He killed all of me. Bruised, burnt and broken. Bewitched, bothered and bewildered. Sev-enteen years of it. He never gave up. Months went by and nothing happened, but it was always there - the promise of it.

For seventeen years. There wasn't one minute when I wasn't afraid, when I wasn't waiting. Waiting for him to go, waiting for him to come. Waiting for the fist, waiting for the smile. I was brainwashed and brain-dead, a zombie for hours, afraid to think, afraid to stop, completely alone. I sat at home and waited. I mopped up my own blood. I lost all my friends, and most of my teeth. He gave me a choice, left or right; I chose left and he broke the little finger on my left hand. Because I scorched one of his shirts. Because his egg was too hard. Because the toilet seat was wet. Because because because. He demolished me. He destroyed me. And I never stopped loving him. I adored him when he stopped. I was grateful, so grateful, I'd have done anything for him. I loved him. And he loved me.

He was everything and I was nothing. I provoked him. I was stupid. I forgot. I needed him. I was hopeless, useless, good for nothing. I lived through years of my life thinking that they were the most important things about me, the only real things. I couldn't cope, I couldn't earn, I needed him. I needed him to show me the way; I needed him to punish me.

(FLASHBACK TO MEMORY)

LEANNE: -Don't hit my mammy!

PAULA: Leanne's voice. She is twelve [now – she was younger then . . . 5 or 6?] She always cheers me up. She's intelligent and creative and good at math. Leanne's arms around my leg, clinging to me. As he went around me. And I turned to keep facing him. Trying to keep Leanne behind me. -It's alright, love. To Leanne. Patting her head. Her face pushed into me. Looking at her father. Looking at his fists. At his face. Not being able to see her. My hand on her head. -It's okay. Having to keep my eyes on Charlo. Pleading with him, holding him back. Feeling Leanne's shivering. Keeping him back. Making sure I faced him. Making sure I didn't let her become a shield. Her heart beating. Keeping my eyes on Charlo's eyes.

CHARLO: -Where'd you get that?

PAULA: -What?

CHARLO: -The eye.

PAULA: It was a test. I was thumping inside. He was playing with me. There was only one right answer. -I walked into the door.

CHARLO: -Is that right? Looks sore.

PAULA: -It's not too bad. He was messing with me, playing. Like a cat with an injured bird. Keeping me in my place. Pretending he didn't remember. I could never fight back. When he wasn't hitting me he was reminding me that he could. He was reminding me and getting me ready. Like the cat playing with the bird, letting it live a bit longer before he killed it. He put one of his fingers on the bruise. I made sure I stayed absolutely still.

CHARLO: -You must have walked right into it, did you?

PAULA: -Yeah; I wasn't looking.

CHARLO: -Which door?

PAULA: -Bedroom.

CHARLO: -Were you drinking?

PAULA: -No. Just careless.

CHARLO: -Yeah.

PAULA: Every day. I think about it every minute. Why did he do it? No real answers come back, no big Aha. He loved me. I know it. But if he loved me, why did he hit me? Why did he hit me so hard and so often? The questions are never answered. They always torment me. And his love becomes a cruel thing, like a smile on a Nazi's face. You don't hit the people you love. You might, once or twice - it's only human. But not the way he did it, again and again. You don't pull back their fingers till they snap. You don't wake them in the morning with a kick in the stomach. You don't hold their face over the chip pan and threaten to dump their head into the boiling fat. You don't beat them in front of their children. That's not love. You can't love someone one minute, then beat them, and then love them again once the blood has been washed off.

I never gave up. I always got up off the floor. I got between them and him. I made ends meet. I never gave up. I'm here. I picked myself up. I washed the blood off my face. I put on the kettle.

I came close. I wanted to die. I lay on the floor and felt death under it. It was warm and I wanted it. I never wanted to get up. I was broken; I wanted to melt. I didn't know who I was. All I knew was the pain. But I got up. I always got up. I had children. I had a husband. I limped around the rooms, tucking the children up in their beds. I hung out the washing with a broken finger. I drank gin. I made sandwiches for their lunches; thin slivers of ham around the edges to hide the nothing in the middle. I hid. I hid the pain, the bruises and the poverty.

I could never get past the door. There were too many things. Things I didn't have. Money, somewhere to go. Too many things. The kids. The schools. People seeing me. All of them stopped me. It was all black out there. -Where would you be without me? he said. I couldn't go. He'd come after me and kill me. And the kids. He said he'd never let me take them. I wasn't fit to look after them; I was an alcoholic and too stupid. He wouldn't let it happen; they'd be better off dead. He looked at me. He meant it. He smashed me against the door before I could open it. He hit my face off it. I waited for the glass to smash into me.

CHARLO: -I'll kill you; I'll kill you!

PAULA: I could never go. I always stopped at the door. But when I saw him looking that way at Nicola, She is eighteen . . . when I saw his eyes. It wasn't the way men look at women - I could nearly have understood that. It was almost natural, something to be careful about. But it was sheer hate. It was clear in his face. He wanted to ruin her, to kill her. His own daughter. Because he could. There was evil in him. I wasn't going to pretend any more. Things were falling apart and it didn't matter. I looked at Nicola.. She looked at me. Yes, her face said; you're right, it's happening. She looked embarrassed and guilty. What did I do? her face said. I'm sorry. Help.

He started humming. The noise disgusted me. I grabbed the frying pan. He was looking straight at Nicola; he was going to make her get out of his way, rub against her. I could always tell when Charlo was about to move; his shoulders told you. They went before his legs. I hit him on the side of the head with the pan.

I knew I was angry now. I took aim this time. He tried to get up. I hit him on top of the head. I could have killed him; it didn't matter. He collapsed properly. I'd done something. - I saw him, I said. -Looking. Nicola nodded. She shut the fridge door.

NICOLA: -Is he dead?

PAULA: -I hope so, I said. His head moved; I had to start again.

NICOLA: -Kill him

PAULA: -No, I said. -There's no need. She couldn't believe me. She thought I was being completely thick.

NICOLA: -He'll kill you now.

PAULA: -No, he won't, I said.

NICOLA: -He will.

PAULA: I escorted him off the premises. Out the gate he went. He got away from me, down the path, away from us. Drenched and bloody and stooped over like a travelling rat. -Go away! He stood there. At the gate. The blood was still running out of his head, down into one of his eyes. The door behind me slammed. It was Nicola. -Go away, will yeh! Go away! And he did. I couldn't believe it. He did what I'd told him to. He walked away. His head still down. He said nothing at all. -Jesus- -He's gone.

NICOLA: -What now?

PAULA: -God knows, I said. -But one thing's for certain. He's not coming back in here again. Her face said it: she'd heard it before. -He's not, I said. It was a great feeling for a while. I'd done something good.
```

---

## IC-0302: The Women of Lockerbie

- Title: The Women of Lockerbie
- Author (byline): Deborah Breevort
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: ): 2005
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BILL, MADELINE, CHORAL DIALOGUE, WOMAN 1, WOMAN 2, OLIVE
- Teaser before the introduction: Yes
- Spoken words (computed): 1420
- Already set (do not supply): none

### Source block (context only)

```text
Author: Deborah Breevort
ISBN: 978-0822220794
Publisher: Dramatists Play Service
Date (Month/Year): ): 2005
```

### Introduction (context only: never use it for content warnings)

```text
When Pan Am Flight 103 exploded over Lockerbie, Scotland on December 21, 1988, it was carrying 35 Syracuse University students home from a semester spent studying abroad. The explosion, caused by a terrorist bombing, resulted in the deaths of everyone on board and 11 people of the town of Lockerbie. It was the largest terrorist attack in the history of the UK.

In this fictious account, a mother from New Jersey travels to Lockerbie, looking for her son’s remains. This is her story . . . The Women of Lockerbie by Deborah Brevort.

NOTE: THE WOMEN OF LOCKERBIE is loosely inspired by a true story, although the

characters and situations in the play are purely fictional. Written in the structure of a

Greek tragedy, it is a poetic drama. Although lines in this cutting are attributed to

various characters, the final product may sound amazingly like a monologue.
```

### Performance text (classify this)

```text
BILL: (Pg 65) [Adam’s] body was never found. He’s still out here somewhere.

MADELINE: (PG 22-23) I can feel him. If only I could find him! If only I could find some part of him. A bone. The bone from his chin. I would know it if I saw it! He had such a strong... firm.. chin...And what I would give to talk to him. Even if it was only to say "Pick up your socks!" If only I could find him... (PG 24) there's got to be something of him somewhere!

MADELINE: (PG 29-30) I was in the kitchen baking a pie for Adam. a pumpkin pie, to welcome him home. The TV was on. I listen to it when I'm cooking. I sprinkle flour on the counter and roll out the pie dough. I roll it once in each direction, like this... (she rolls) the way my mother taught me. And then, Ted Koppel comes on the air. I know immediately that something is wrong. He said:

BILL: "We interrupt this program..."

MADELINE: I thought, oh, dear, something awful has happened. What a shame. And so close to Christmas. I grab more flour and sprinkle it. I roll the crust. I hear...

BILL: "Pam Am 103 was last seen in a fireball over Scotland."

MADELINE: I double over into the kitchen counter. My face presses into the pie dough. I cannot stand up. I grope the counter for something to hold on to. I reach for the handle on the refrigerator -- pull myself up. And there in front of me is a note held by a magnet that says "Adam. 7PM. JFK. Pam Am 103." (She sinks to the ground, overcome with grief) I live in New Jersey! I have two cars in the driveway! This was not supposed to happen to me!

CHORAL DIALOGUE: Multiple women speak to the audience (Pg 32-33)

WOMAN 1: You think the worst can't happen.

WOMAN 2: You think that it won't.

WOMAN 1: But then, one day, it does.

OLIVE: The poor soul on television is suddenly you. Death is a guest whose visit is short. When it comes to your house it never stays

WOMAN 1: But, grief...

OLIVE: Grief is a guest who stays too long. Its visit turns from days,

WOMAN 2: into weeks,

WOMAN 1: into months,

OLIVE: into years.

WOMAN 2: It takes over your house and will not leave. Wherever you go it follows.

WOMAN 1: Whatever you do it watches.

OLIVE: It hovers behind you, looking over your shoulder so you cannot forget that it's there. (Pg 26-27) Grief needs to talk

BILL: She goes over and over the moment I heard the news. Over and over the moment of his death. I’ve stopped listening. I can’t take it anymore.

MADELINE: (PG 28) It's all right if you think I'm crazy, because I am. I roam the hills looking for my son's body. Only a crazy person would do that....

OLIVE: . . . or a mother.

MADELINE: I'm not a mother anymore... (PG 40-42) I never should have let him study in London. He was too young. Much too young to go so far away from home. I should have made him wait for a year. I should have been more firm. And why did I choose Pan Am over Delta? There were two boxes on the application form! Why didn't I...check the box for Delta? (pause) And I should have let him stay an extra day with his friends! But I said, "No, I want you home for Christmas. I want you home for the party. You need to hang the Christmas lights for your father." (pause) Oh God... (pause) And why did I plan the party for Friday? I should have planned it for Saturday! If I had planned the party for Saturday he wouldn't have been on that plane. He never would have died. He could have flown on Delta! - I could have said "Yes, you can come home whenever you want!" I should have hung the Christmas lights! I could have gotten on that ladder myself!

CHORAL DIALOGUE: Multiple women speak to the audience (PG 42-44)

OLIVE: Our lives are made of choices. Hundreds of little choices that determine our fate, each with a consequence we cannot see.

WOMAN 1: You check the box for Delta and your son lives.

WOMAN 2: You check the box for Pam Am and he dies.

WOMAN 1: Choices,

WOMAN 2: such little choices...

WOMAN 1: Sometimes I wonder if the choices you make are yours at all...

WOMAN 2: Or if they're made by something else Something greater, like God.

WOMAN 1: Sometimes it seems that these things are fated,

WOMAN 2: meant to happen.

MADELINE: (PG 46-47) I was a good mother! And a good wife! And a good neighbor! I made cookies for the bake sale! I gave money to the swim team! I remembered birthdays! When someone got sick, I made chicken soup! And this is how I'm repaid?

BILL: It’s not fair. Life’s. Not. Fair. At some point you have to accept that. You have to move on.

MADELINE: Move on? To what? What is there to move on to?

BILL: (PG 48 – 50) I had to return his Christmas presents back to the mall. Do you know what that was like? What do you say to the sales clerk? What do you say to the 16-year old school girl standing behind the counter at JC Penney's who smiles at you and asks "Why are you returning the sweater?" What do you say to someone so young and innocent? "This was for my son, but he died?" "He was blown to bits by a bomb?" What do you say to the pretty young girl with red and green ribbons in her hair? (pause) I just said... "My son doesn't need it anymore". And then I breathe a sigh of relief because I think I've gotten through it. But I haven't. Oh no! It doesn't stop there. I go to the next store, to return the Nikes. And to the next store to return the pajamas. And the next store to return the bathrobe and the blue jeans and the bike helmet. (pause) I go to six stores before the day is through. I have that same conversation in every single place. (pulling out a wallet to examine the pictures)

MADELINE: (PG 82-84) Adam? How quickly you passed... One moment here. The next moment there. Living, dead. Living, dead. Dead. Dead, dead, dead. What is it like to be dead? What was it like when you crossed the line and passed to the other side? Where you drinking a coke? Taking a nap? Or were you talking...? Having a nice conversation with the woman right beside you? Mrs. Corcoran. Yes, Doris Corcoran. She was a teacher from Syracuse University. Were you talking about London? Christmas? College? Changing your major to math? And what... did you "do" the moment it happened...? Did you grab Mrs. Corcoran's hand? Close your eyes and pray? Or did it happen too fast for any of that? Adam... What happened next? What did you do? Where did you go? You must have gone somewhere... (grief turns to a growing anger that builds to a crescendo)

(PG 44-45) If I ever meet his killers I will inflict on them the measure of pain they have brought to me. They should suffer! Pain is a gentle word to describe what I would do to them if I ever got the chance! I want justice! I won’t find peace until there is justice. Those men killed [my] son! They killed 270 people! They destroyed our lives!

CHORAL DIALOGUE: Multiple women speak to the audience (PG 51-52)

WOMAN 1: There's an order in the world. An order behind the chaos and the violence.

WOMAN 2: And there's a purpose. If the sun never set, we would find no beauty in the sunrise.

WOMAN 1: If the night was full of light, we would not see the stars.

OLIVE: And if hatred never pierced our hearts, we would not know the power of love.

WOMAN 1: They are given to us so we learn and grow. You have to trust in this. Trust.

OLIVE: And believe that behind the suffering of the world, there is a purpose to everything.

BILL: (PG 52-53) I want to believe that. I want nothing more than to believe that this happened for a reason. But I can't. I just...can't. To believe that would mean that Adam died just so that I could learn and grow. And that's not true. There is no lesson so important that it was worth the price of his life. To believe that would mean that I am at the center of the universe and that all things happen for my benefit. And they don't. The events of the world... the horrors... just happen. And they happen for no reason. The only thing you can do is accept that and carry on the best you can. Just accept the suffering that comes to you and find some way to keep going. (PG 86) Why do [you/I] hold on to [your/my] grief so hard?

MADELINE: It's the only thing I have left to hold on to!
```

---

## IC-0303: WWJD

- Title: WWJD
- Author (byline): Will Weaver
- Work: On the Fringe: Stories
- Publisher: Dial
- Publication date as stated: April 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SUZANNE, GROUP, CROWD MEMBER, EDDIE, MONITOR, PRINCIPAL, NURSE, COUNSELOR
- Teaser before the introduction: Yes
- Spoken words (computed): 2148
- Already set (do not supply): none

### Source block (context only)

```text
Author: Will Weaver
Book: On the Fringe: Stories
ISBN: 978-0142500262
Publisher: Dial
Date (Month/Year): April 2001
```

### Introduction (context only: never use it for content warnings)

```text
Being a transfer student is difficult enough, but Suzanne also carries other burdens into her new high school. When counseling and drug therapy don't help, Suzanne's religious beliefs give her strength. However, her major tormentor, Eddie Halvorsen, won't give up. WWJD by Will Weaver.
```

### Performance text (classify this)

```text
SUZANNE: LIKE JESUS, I am surrounded by sin. Every morning on my way to school I walk past rough boys with shaved heads and girls with pierced faces. They stand inches off the high school property line and smoke cigarettes. When I appear, they whoop and swear and throw their trash at me. Every morning I am their amusement. Their victim. I could easily avoid my tormentors by taking a different path from my aunt's house. But I try to live by one rule: WWJD. What would Jesus do? And the answer is clear. Jesus never took the easy way out. He never avoided the sinners, the lost, the lonely, the hurting. Rather, He went among them.

SUZANNE: Today I carry a black plastic garbage bag. My antagonists do not see me immediately-two of them are wrestling in the snow. The rest are laughing and egging them on. I tighten my long orange scarf around my throat, and quietly I ease behind them. I begin to pick up their trash.

GROUP: (chanting) Hey look, it's Weird Suzy! Weird Suzy, Weird Suzy!

SUZANNE: Sticks and stones. Their name-calling does not bother me. After all, my real name is Suzanne. I am a sixteen-year-old sophomore at River Forks High School in central Wisconsin, and the year is 2001. But I don't feel like this is my school, Wisconsin my state, or these times my times. . .

This morning a can of Mountain Dew clatters at my feet. Yellow spray splashes my clothes, spatters my face.

CROWD MEMBER: Good hit, Eddie!

SUZANNE: I look up to my main tormentor, Eddie Halvorsen.

EDDIE: Hey, pick up my can, Weird Suzy.

SUZANNE: I bend down to get it. I place it carefully in my garbage bag.

EDDIE: This too, freak.

SUZANNE: From between his thumb and middle finger he flips his cigarette directly at me. I'm not quick enough to avoid it, but would not have anyway. The cigarette stings my cheek like a bee. Sparks fly as the butt falls at my feet. I touch my cheek; gray ash comes off on my finger tip. I draw my ashy finger slowly across my forehead, then bend to pick up the dead butt. The parking lot monitor, an off-duty security guard, trots across the street. He comes first to me.

MONITOR: Are you all right, miss? You could have put her eye out. (catching Eddie by the arm)

EDDIE: (shrugging) I was just getting rid of my butt. Can't help it if she got in the way.

MONITOR: If this were on school property, you'd be gone-for good.

EDDIE: But it ain't. It's public property. I got my rights, now shove off and stop bothering me.

SUZANNE: Then the first hour bell rings. My tormenters look at one another, then swear loudly. Burping and cursing, they throw down their trash, then trudge onto school property. I wait for them to leave. My cheek stings a little but I keep working with my garbage bag.

PRINCIPAL: Suzanne-come along now.

SUZANNE: I look up. It's the assistant principal, Ms. Kaufman. She takes my garbage bag in one hand and my arm in the other. She reminds me of my real mother, who is in prison. I have not told anyone in River Forks about this. She has leaned in to stare at my cheek.

PRINCIPAL: You'd better drop by the nurse's office and get your face looked at. There's a little blister on your cheek.

SUZANNE: Eddie. (touching the burned spot)

PRINCIPAL: The parking lot monitor told me. Would you like to fill out a harassment report?

SUZANNE: (thinking) WWJD? (to principal) No.

PRINCIPAL: I really encourage you to do so. Eddie is out of control these days. You would be helping him.

SUZANNE: (murmuring) A change of heart must come from the inside. (to audience) Ms. Jones, the nurse, puts ointment on my face. She tries to wipe clean the ash mark but I lean away. (to nurse) I consider it a religious symbol. Like the mark Catholics wear on Ash Wednesday.

NURSE: Suzanne, today is Monday.

SUZANNE: Her eyes flicker down the rest of me. At my hair. At my clothes, which I get from the Salvation Army. At my sandals, which I made myself in shop class from tire rubber, leather straps, and buckles. At my long orange scarf, which I wear everywhere. Her eyes return to my hair.

NURSE: Are you keeping up your hygiene, Suzanne? Good personal hygiene is important-particularly for girls. (smiling and winking) Let me give you some samples of shampoo and deodorant.

SUZANNE: Next I go to the counselor's office.

COUNSELOR: Who's next? Why, it's Suzanne! Come on in!

SUZANNE: A hearty greeting is requisite for all counselors. That and positive body language. He glances at a memo on his desk.

COUNSELOR: I understand that you had an encounter with Eddie Halvorsen this morning.

SUZANNE: (to counselor) Nothing serious. I have no complaint against Eddie. I think he's going through tough times right now. Jesus is trying to speak to him.

COUNSELOR: (pursing his lips) He burned your cheek. I can see the mark from here.

SUZANNE: And I've forgiven him."

COUNSELOR: Suzanne, we've talked about this ... forgiveness thing. I know you're a very religious person. You read the Bible every day.

SUZANNE: Yes. Though mainly in the New Testament. I find the Old Testament too centered upon retribution, revenge. Jesus believed not in punishment but in forgiveness. In turning the other cheek.

COUNSELOR: (quickly) Yes, of course, Suzanne. But my point, one we've talked about before, is that this is the twenty-first century. These are different times than when Jesus lived. And we must live in them. We must inhabit our own times, so to speak. (clears throat) While Jesus provided us wonderful lessons, it is, may I say, perhaps unrealistic to try and live His example every minute of our day.

SUZANNE: (silence while Suzanne thinks, then) But isn't that why we go to church? Why we read the Bible? To live more like Jesus? There are no limits to forgiveness. (to audience) My day goes all right. What I'm looking forward to is my last class of the day, woodworking. I've always liked to make things, plus I don't mind being surrounded by boys (I'm the only girl). It is among boys that I can do the most good. At 2:00 P.M. I go to woodworking. Eddie Halvorsen is there, along with the other "woodies." as they call themselves. He glares at me. I begin work on my wooden swan. The neck of my black walnut swan curves up gracefully. I've been working on her all term, and she's really getting beautiful. Even Mr. Patterson complimented me on her. He let me do a project different from the boys, most of whom are making gun cabinets. But I love my swan. When I work on her, she reminds me that there is hope for Eddie. For all of us . . . After school, on my way home, it is snowing. I walk with my head down and my scarf wrapped around my face. It never snowed in California . . . Suddenly someone blocks the sidewalk.

EDDIE: Weird Suzy!

SUZANNE: (blinking) Hello, Eddie. (to audience) For a moment he scares me. But I remember that Jesus must have been afraid many times. Suddenly Eddie whoops and snakes out his arm; he grabs my orange scarf and strips it from my neck. I blink against the falling snow and look at him. WWJD? I set down my book bag, take off my coat, hold it out to him. (to Eddie) Take my coat too. (to audience) He stops, stares. Then he grabs my coat, throws it in the snow. (to Eddie) My hat too. (to audience) I take off my beret, hand it to him. He throws it in the snow. He laughs. I peel off my sweater-I have on only a T-shirt underneath and it is suddenly very chilly-and I hand it to him. After a moment's hesitation, he takes it. He swallows as he stares at me. I am shivering in the February air. Suddenly he flings my sweater in my face so hard I stumble back.

EDDIE: (voice cracking) What in hell is the matter with you?

SUZANNE: When I look up again, he is disappearing in the snow. . . The next morning I walk to school the usual way. Eddie's gang spots me, as usual. But this morning Eddie will not look at me. He stands with his back to me, his hands jammed in his pockets. I can feel his anger. His hard heart. Light snow is falling again and has whitened his cap and shoulders. For a moment he looks like a pillar of salt. . . In shop class Eddie's dark eyes follow me as I go to my locker, unlock it, carefully take out my swan lamp. I go to my station and begin work. Working on my swan makes me forget everything, even my mother.

EDDIE: What the hell's that supposed to be, anyway?

SUZANNE: I turn. He grabs at my swan. I jerk it away from him and cradle it in my arms. Eddie laughs. I feel my face flush. I shouldn't have jerked my swan away from Eddie. It's not something Jesus would have done. Slowly I hold it out so that he can see it-but not touch it. (to Eddie) It's a swan.

EDDIE: Looks like a damned crow to me.

SUZANNE: (to Eddie) It's not finished . . . Like all of us. (to audience) He stares at me. I see the hate in his eyes.

EDDIE: You should have stayed in California, you freak.

SUZANNE: After he leaves I turn back to my swan but my hands are shaky. For one brief moment I understand what Jesus felt like when He knew that He was the One. The Chosen One. "Take this cup," I murmur to my swan. "Choose someone else to help Eddie." But she is silent. . . I do not see Eddie after school, which today is all right by me. I take a walk down by the river. I often come down here to pray. Today I pray for my mother that she will not forget me-and especially for Eddie Halvorsen. . . Near school the next morning Eddie calls out to me.

EDDIE: Hey, Suzy! How's it going?

SUZANNE: I stare. His voice is almost cheerful. None of his friends throw anything at me. They are all smiling. I do not quite understand this, but not everything Jesus does is understandable. I smile a little, nod and pass by. . . In shop class I go straight to my locker. I can't wait to get started. But my padlock, broken, falls into my hands. I stare at it, then at my little metal door. Its hinges are bent. Slowly I pull open the door. My swan falls out in pieces. She clatters to the floor like a spilled puzzle that cannot ever be put right. I can't help myself: I drop to my knees, clutch the pieces, and begin to wail. I hear myself calling for my mother. . . . I leave school late. I have been in the nurse's office. Finally she lets me go home. I head down by the river, when I am aware of footsteps.

EDDIE: Hey, Weird Suzy. What happened to your crow?

SUZANNE: I stop. (to Eddie) It was a swan. A black swan. (to audience) I hunch under my scarf and keep walking.

EDDIE: So where you going now, Weird Suzy?

SUZANNE: Down by the river.

EDDIE: Gonna drown yourself? (laughing, then whispers) Maybe today's the day. If not now, when, Weird Suzy?

SUZANNE: To get away, I head down the bank, past a "Danger -Thin Ice!" sign.

EDDIE: That's right. Good girl! SUZANNE He follows me down the bank. I step onto the ice. I walk out several yards, toward the middle of the river where there is a dark, steaming, open patch. I think of Jesus when He walked on water. It was all a matter of faith. I move a couple of steps closer to the black water. Then I turn and face Eddie, who remains on the white shore. (to Eddie) Are you coming? Don't be afraid. (to audience) He laughs but there is something thin and reedy and strangled in his throat. (to Eddie) You can do it. (beckoning him forward) Come out to where I am. It's all a matter of not being afraid. (to audience) He takes several more steps-and suddenly there is a sound under his feet like foil ripping. Eddie's arms flap, like a bird taking off, as his legs and trunk disappear through the ice. He screams. I wonder if my black swan screamed when its head was cut off. Suddenly, Eddie is hanging on to the ice by his elbows. Most of his body is underwater.

EDDIE: Help! Help me!

SUZANNE: A car stops on the parkway; the driver quickly lifts a cell phone to his face.

EDDIE: (screaming) Save me. Someone! Suzy! Please! Save me!

SUZANNE: I watch him. I think of my swan. My butchered black swan. I think, What would Jesus do? Possibly I could save Eddie, though he seems to have a grip on the ice. I have my long orange scarf. It would be enough to throw to him. It would be something for him to hold on to until help arrives. But I understand that not even Jesus could save everyone. I sit down on the ice just out of Eddie's reach. I must think about what to do. After all, I am only human.
```

---

## IC-0304: The Yellow Wallpaper

- Title: The Yellow Wallpaper
- Author (byline): Paul Kuritz
- Work: The Best American Short Plays 2001-2002
- Publisher: Applause Books
- Publication date as stated: Aug 2007
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SHE, JOHN
- Teaser before the introduction: Yes
- Spoken words (computed): 3400
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul Kuritz
Book: The Best American Short Plays 2001-2002
ISBN: 1557837058
Publisher: Applause Books
Date(Month/Year): Aug 2007
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
(adapted from the short story by Charlotte Perkins Gilman)

[Light finds her in her room, JOHN has just exited. Bed in upper right corner, chair and writing desk upper left, exit upper left. SHE notices the audience and begins to talk about her house.]

SHE: Ancestral halls...A colonial mansion, An hereditary estate. [Aside.] I would say a haunted house, and reach the height of romantic felicity-but that would be asking too much of fate! Still! There is something queer about it. Else, why should it be let so cheaply? And why have stood so long "untenanted"? John laughs at me. But one expects that in marriage. John is practical in the extreme. He has no patience with faith [lifting her Bible], an intense horror of superstition, and he scoffs openly at any talk of things not to be felt and seen and put down in figures. John is a physician. And perhaps, perhaps that is one reason I do not "get well" faster. You see: He does not believe I am sick! So what can I do? If a physician of high standing, and one's own husband, assures friends and relatives that there is really nothing the matter with me but "temporary nervous depression-a slight hysterical tendency." What can I do?

The Yellow Wallpaper by Paul Kuritz; adapted from the short story by Charlotte Perkins Gilman

SHE: [Looking at photo in a frame on wall by bed.] My brother is also a physician. Also of high standing. And he says the same thing. [Picking up pill containers and lines them up on the floor.] So I take phosphates. Phosphites, Tonics, and journeys, and air, and exercise, and am absolutely forbidden to "work" until I am well again. Personally, I disagree with their ideas. Personally, I believe that work, excitement and change, would do me good. But what can I do? [Picking up and looking through papers, laying them one by one behind the row of pill and tonic containers.] I did write for a while in spite of them. But it exhausts. Having to be so sly about it. I sometimes fancy that in my condition if I had less opposition and more society and stimulus-but John says

JOHN: The very worst thing you can do is to think about your condition.

SHE: I get angry with John sometimes. I never used to be so sensitive. I think it is due to this nervous condition. But John says

JOHN: If you feel so, you will neglect proper self-control.

SHE: So I control myself. And that makes me very tired. I don't like this room a bit. I wanted one downstairs that opened on the piazza and had roses all over the window, and such pretty old-fashioned chintz hangings! But John would not hear of it.

JOHN: There was only one window and not room for two beds, and no near room for me if I took another.

SHE: He is very careful and loving. He hardly lets me stir without special direction. I have a schedule prescription for each hour in the day. He takes care of me. So I feel ungrateful not to value it more.

JOHN: We came here solely on your account. You are to have perfect rest and all the air you can get. Your exercise depends on your strength, my dear. And your food somewhat on your appetite. But air you can absorb all the time.

SHE: So we took this-the nursery at the top of the house. It is a big, airy room, the whole floor nearly. It was nursery first and then playroom and gymnasium: the windows are barred for little children, and there are rings and things in the walls. The paint and paper look as if a boys' school had used it. It is stripped off in great patches all around the head of my bed, about as far as I can reach, and in a great place on the other side of the room low down. I never saw a worse paper. No wonder the children hated it! I'd hate it myself if I had to live in this room long.

SHE: John is away all day, and even some nights when his cases are serious. I am glad my case is not serious! But these nervous troubles are dreadfully depressing. John does not know how much I suffer. He knows there is no reason to suffer. And that satisfies him. Of course it is only nervousness. But it weighs on me not to do my duty in any way! I meant to be such a help to John-a real rest and comfort. And here I am a burden. Already! Nobody believes what an effort it is to do what little I can: - to dress and entertain, and order things. It is fortunate Mary is so good with the baby. Such a dear baby! And yet I cannot be with him. It makes me too nervous. I suppose John never was nervous. He laughs at me about this wallpaper! At first he meant to repaper the room, but afterwards he said

JOHN: You are letting it get the better of you. Nothing is worse for a nervous patient than to give way to such fancies. After the wallpaper was changed it would be the heavy bedstead, and then the barred windows, and then that gate at the head of the stairs, and so on. You know the place is doing you good. And really, dear, I don't care to renovate the house just for three months.

SHE: He is right about the beds and windows and things. It is an airy and comfortable room. And, of course, I would not want to make him uncomfortable just for a whim. I'm really getting quite fond of this big room. All but this horrid paper.

SHE: If I were only well enough to write a little it would relieve the press of ideas and rest me. But I get pretty tired when I try. It is so discouraging not to have any advice and companionship.

JOHN: When you get really well, we will ask Cousin Henry and Julia down for along visit.

But I would as soon put fireworks in your pillow-case as to let you have those stimulating people about now.

SHE: I wish I could get well faster. [Turns back.] But I must not think about that. This paper looks to me as if it knew what a vicious influence it had! [Seeing as if for the first time, a major discovery. Perhaps SHE begins to project onto the paper the feelings for JOHN she can't or won't admit.] There is a recurrent spot where the pattern looks like a broken neck. And two bulbous eyes stare at you upside down. The impertinence of it! And the everlastingness! Up and down and sideways they crawl. And those absurd, unblinking eyes are everywhere. [Discovers a particular wallpaper seam for the first time and inspects it.] There is one place where tow breadths don't match. The eyes go all up and down the line, one a little higher than the other. I never saw so much expression in an inanimate thing before. [Backs away from it toward bed.] [Lies on the bed.] I used to lie awake as a child and get more entertainment and terror out of blank walls and plain furniture than most children could find in a toy store. I remember what a kindly wink the knobs of our big, old bureau used to have. There [notices her writing chair] was one chair that always seemed like a strong friend. I used to feel that if any of the other things looked too fierce I could always hop into that chair and be safe. [SHE does so.] [Pause. ] [SHE notices the paper beside her.] This wallpaper, as I said before, is torn off in spots. It sticks closer than a brother. [Noticing the floor for the first time.] The floor is scratched [Walking and examining each thing SHE notices empathetically.] and gouged and splintered. [Looking at the ceiling.] The plaster is dug out here and there. [At her bed.] And this great heavy bed looks as if it had been through the wars. But I don't mind it a bit-only the paper. [Noticing the wallpaper, as if discovering something very important about it for the first time.] This wallpaper has a kind of sub-pattern in a different shade, a particularly irritating one. You can only see it in certain lights. [Gets candle, lights it, and uses it to examine the wallpaper more closely.] And not clearly then. But in the places where it isn't faded and where the sun is just so l can see a strange, provoking, formless sort of figure. It seems to skulk about behind that silly and conspicuous front design.

SHE: Fighting back tears] I cry at nothing. And cry most of the time. Of course I don't when John is here or anybody else. But when I am alone.... And I am alone a good deal just now. John is kept in town very often by "serious cases." And Jennie is good and lets me alone when I want her to. [Trying to talk herself into believing it to be true.] I'm getting really fond of the room in spite of the wallpaper. Perhaps because of the wallpaper. It dwells in my mind so! I lie here on this great immovable bed-it is nailed down, I believe-and follow that pattern about by the hour. It is as good as gymnastics. I start at the bottom, down in the corner over there where it has not been touched, and I determine for the thousandth time to follow that pointless pattern to some sort of a conclusion. But, on the other hand, they connect diagonally. And the sprawling outlines run off in great slanting waves of optic horror. The whole thing goes horizontally, too. At least it seems so. It makes me tired to follow it.

SHE: Dear John! He loves me very dearly. He hates to have me sick. I tried to have a real earnest reasonable talk with him the other day: Let me go and visit Cousin Henry and Julia.

JOHN: You aren't able to go. Nor able to stand it after you got there.

SHE: I did not make a very good case for myself. I was crying before I finished. It is getting to be a great effort to think straight. Just this "nervous weakness" I suppose. And dear John gathers me up in his arms. And just lays me on the bed, and sits by me, and reads to me till it tires my head.

JOHN: You are my darling and my comfort and all I have. You must take care of yourself. For my sake. And keep well. No one but you can help you out of this. Use your will and self-control. Don't let any silly fancies run away with you.

SHE: There are things in this paper that nobody knows but me. Or ever will. Behind the outside pattern the dim shapes get clearer every day. It is always the same shape, only very numerous. And it is like-a woman, stooping down and creeping about behind that pattern. I don't like it a bit. I wonder... I think... I wish John would take me away from here! It is so hard to talk to John about my case. He is so wise, he loves me so... But I tried it last night. It was moonlight. The moon shines in all around. I hate to see it sometimes, it creeps so slowly. John was asleep and I hated to wake him. So I kept still and watched the moonlight on that undulating wallpaper till I felt creepy. [Sees the figure shaking the paper for the first time.] The faint figure behind seems to be shaking the pattern. As if she wants to get out. I got up softly and went to feel and see if the paper did move. And when I came back-John was awake.

JOHN: What is it, little girl? Don't go walking about like that. You'll get cold.

SHE: I really am not gaining here. I want you to take me away.

JOHN: Why, darling, our lease will be up in three weeks. I can't see how to leave before. The repairs are not done at home. I cannot possibly leave town just now. Of course if you were in any danger, I could and would. But you really are better, dear, whether you can see it or not. I am a doctor, dear, and I know. You are gaining flesh and color. Your appetite is better. I feel really much better about you.

SHE: I don't weigh a bit more, nor even as much. My appetite may be better in the evening when you are here, but it is worse in the morning when you are away!

JOHN: Really, dear, you are better!

SHE: Better in body perhaps [JOHN sits up straight and looks at her with a stern, reproachful look.]

JOHN: My darling, I beg of you, for my sake and for our child's sake, as well as for your own, never, even for one instant, let that idea enter your mind! There is nothing as dangerous, as fascinating, to a temperament like yours.

SHE: There is one marked peculiarity about this paper. A thing nobody seems to notice but myself. It changes as the light changes. The outside pattern, and the woman behind it, is as plain as can be. I didn't realize for a long time what the thing was that showed behind, that dim sub-pattern. But now I am quite sure. It is a woman. By daylight she is subdued, quiet. It is so puzzling. The fact is [SHE starts to say it, hesitates, but this time succeeds.] I am getting a little afraid of John. He seems very queer sometimes.. It must be the paper! I have watched John when he did not know I was looking. I've caught him several times looking at the paper! [Vows.] But nobody will find it out but me! [Lights fade and up.]

SHE: Life is very much more exciting now than it used to be. You see I have something more to expect, to look forward to, to watch. I really do eat better. And am more quiet than I was. I don't sleep much at night. I watch developments. There is something else about that paper-the smell! I noticed it the moment we came into the room. But with so much air and sun it was not bad. And whether the windows are open or not, the smell is here. It creeps all over the house. It gets into my hair. Such a peculiar odor, too! It is not bad-at first, and very gentle, but quite the subtlest, most enduring odor I ever met. It used to disturb me at first. I thought of burning the house. But now I am used to it. The only thing I can think of that it is like is the color of the paper! A yellow smell. There is a very funny mark on this wall, low down, near the mop-board. A streak that runs round the room. It goes behind every piece of furniture. Except the bed. A long, straight, even smooch. As if it had been rubbed over and over. I wonder how it was done. Who did it. What they did it for. Round and round and round and round and round and round... [Dizzy, falls into the bed.]

SHE: I discovered something. I found out. The front pattern moves! The woman behind shakes it! Sometimes I see many women behind. Sometimes only one. She crawls around fast, and her crawling shakes it all over. She is all the time trying to climb through. But nobody could climb through that pattern-it strangles so.

SHE: I think she leaves in the daytime! I've seen her! I can see her out of every one of my windows! It is the same woman. [Looking at one window.] I see her in that long shaded lane, creeping up and down. [Looking at the other window.] I see her in those dark grape arbors, creeping all around the garden. [Back at the first window.] I see her on that long road under thee trees, creeping along. I don't blame her a bit. I always lock the door when I creep. I don't do it at night. John would suspect something. And John is so queer now. I don't want to irritate him. I wish he would take another room! Besides, I don't want anybody else to get that woman but myself! [Lights fade and up.]

SHE: I have found out another funny thing. But I won't tell you this time! I can't trust you with too much. There are only two more days to get this paper off. John is beginning to notice. I don't like the look in his eyes. John knows I don't sleep very well at night. He asks me all sorts of questions, too, and pretends to be very loving and kind. As if I can't see through him! [Lights fade and up.]

SHE: Hurrah! This is the last day. John is staying in town overnight, and won't be out until this evening. Last evening, as soon as it was moonlight, that poor thing began to crawl and shake the pattern. I got up and ran to help her. I pulled, she shook. I shook, she pulled. Before morning we had peeled off yards of this paper. [SHE reveals a bucket of yellow strips of paper.] And when the sun came that awful pattern began to laugh at me [Laughs at the paper in the bucket.] I will finish you to-day! We are going away to-morrow. Jennie was amazed, but I told her merrily that I did it out of pure spite. She laughed and said she wouldn't mind doing it herself. [To the bucket of paper.] But nobody touches you but me! Not alive, anyway. She tried to get me out of the room. [Lies down on bed.] But I said that I believed I would lie down again and sleep all I could; and not to wake me even for dinner. I would call when I woke. Now she's gone. The servants are gone. The things are gone. And there is nothing left. But I must get to work. I have locked the door and thrown the key down into the front path. I don't want to go out, and I don't want anybody to come in. Till John comes. I want to astonish him. [SHE takes rope with noose from a secret place] I've got a rope that even Jennie did not find. If this woman does get out, and tries to get away, I can tie her! I am getting angry enough to do something desperate. To jump out of the window would be admirable exercise, but the bars are too strong even to try. Besides I wouldn't do it. Of course not. "People don't do such things!" I don't even like to look out of the windows-there are so many of those creeping women, and they creep so fast. I wonder if they all come out of you as I did? [Ties end of rope to bed leg and puts noose around her neck.] But I am securely fastened now. You won't get me out in the road there! I suppose I shall have to get back behind the pattern tonight. That is hard! It is so pleasant to be out in this great room and creep around as I please! I don't want to go outside. [Sits on floor.] I won't. [Hears something we can't hear.] Why there's John at the door! Calling and pounding! Now he's crying for an axe. It would be a shame to break down that beautiful door! "John dear, the key is down by the front steps." [Listens again.] That silenced him for a few moments.

JOHN: Open the door, my darling.

SHE: I can't. The key is down by the front door. [SHE repeats it again, several times, very gently and slowly.]

JOHN: What is the matter? For God's sake, what are you doing!

SHE: I'll just keep on creeping. I've got out at last. In spite of you. And I've pulled off most of the paper. So you can't put me back in!
```

---

## IC-0305: The Acorn People

- Title: The Acorn People
- Author (byline): Ron Jones
- Work: Not specified
- Publisher: Laurel Leaf
- Publication date as stated: June 1996
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: RON, NURSE, SPIDER, BENNY, AARON, MARTIN, THOMAS
- Teaser before the introduction: Yes
- Spoken words (computed): 1638
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
RON: (Pg 1) Children spilled from cars and buses. The woods and paths of Camp Wiggin were accustomed to troops of running feet and the noise of children at play. With these wheelchair children there was only silence. It was as if the woods themselves were watching the unfolding of chairs and the lifting of bodies. All life seemed to stop. In procession, the parents wheeled their children toward awaiting counselors. I was a counselor. Like everyone around me, I didn't know what to say.

RON: (Pg 1-3) What do you say to a parade of children who move toward you only by the energy of their parents' insistence? Who move toward you with swollen heads of gargantuan proportion. With birth scars that have left the eyes without sight or the body without arms and legs. Children who seem drained of expression. Crumpled and stuffed into wheelchairs. Covered with blankets, to ward off not the cold, but the vision of disfigurement. . . The camp nurse had given us a one-day orientation about handicapped children.

NURSE: Most will not live past their teen years. It is nature’s way.

RON: She described the hydrocephalic children with heads that looked like melons about to burst. And the disease of multiple sclerosis, which ate away at the muscles, leaving the body without energy or movement. The children who had mongoloid faces and a distant stare. And finally the children who entered life without vision or a hand or perhaps a face. (beat)

There were two counselors for each cabin of five children. I shared counseling duties with Dominic Cavelli from New York. He was after a career working with handicapped children. (Pg 4) [But it was] the thought of playing with kids, swimming all day, and taking long hikes had drawn me to this place. My illusions were quickly washed away. I wasn't about to frolic with these children. We would be lucky if we could even take a few steps together. (beat)

(Pg 9-10) The first of our kids was Benny. Polio had taken his legs but not his gall or heart. Most kids have a "thing" they do. Something special. For Benny it was speed. With a crash helmet pulled tightly over his head, he hunched forward in his wheel-chair like a dirt-track driver in a stock car.

(Pg 10-11) Spider was another kid in our cabin. It was a funny name because Spider didn't have any legs or arms. He had stumps that stuck out from his short frame like broken branches out of a tree. Like Benny, Spider was alert and perceptive. You could tell by his eyes. Spider's eyes held everything. And what his eyes couldn't hold, his mouth tried to trap. Spider loved to talk.

(Pg 11-12) Far less active and alert than Benny or Spider was Thomas Stewart. He had muscular sclerosis, the cruelest ailment of all. Thomas must have been sixteen. It was hard to tell. Benny and Spider looked and acted like the eight- and ten-year-olds they were. But Thomas weighed about 35 pounds. Picking him up was like holding a collapsible tent. Thomas’ mouth was always pinched tight, as if to hold.in some final scream. He watched the world about him but gave nothing to it. Un-willing to move unless moved. Pensive, patient, and dying.

(Pg 12) Martin was the most able-bodied child in our group. Like other blind children in camp, he had a constant smile and seemed in perpetual motion. Sitting still, he would rock forward and back. Even standing, he swayed rhythmically. He was about fourteen, with bright red hair that stuck out in every direction.

(Pg 13) Aaron Gerwalski was the fifth kid under our charge. Aaron didn't have a bladder. A large, bag was attached to his intestines. Strapped to his leg, it collected urine that had to be emptied every hour. This condition was terrible for anyone, but for a teenager it must have been overwhelming. The smell repelled any gesture of friendship. It stalled and interrupted any conversation before it could begin.

(beat)

(Pg 14-15) Our first day we were assigned to the craft area. I rounded up Benny, got Martin to work with Spider and gave the quiet Thomas Stewart and Aaron each a private workspace. I busied myself with a nut necklace. An act of frustration that symbolized how I felt. Crazy to be here. Absolutely crazy. Spider asked what the necklace was for. . . "I feel a little weird being here, so I've made myself a necklace of nuts."

SPIDER: So do we. We're all a little nutty here!

BENNY: You might call us the nut people. Yeah, that's a good name for us.

SPIDER: Can we make a necklace like yours?

RON: Benny raced about collecting every nut in sight. And soon we all had this crazy nut necklace in common.

SPIDER: (Pg 16) We’re the Acorn People!

RON: (Pg 22) And the Acorn People were on the move . . . (Pg 25-26) The following day we [went] to the pool. [It] was being used by a group of girls! Participants in this first - ever "integrated swim" were self-conscious and then flirtatious. The boys worried about their hair. My God, I had to comb their hair before they would venture out to poolside. [But] soon, the sun and water worked their magic. Children -- no, young adults -- no, children were playing games. Even Thomas Stewart, the most distant of all -- I caught him smiling for the first time when he oh so slightly nudged a girl. (Pg 27-28) There was a great deal of speculation as to who had a crush on whom.

There was a new excitement in the air. Leaving the pool area, I noticed that a blind girl named Mary was wearing an acorn necklace. The question of how she got the necklace slid from my mind until Aaron complained.

AARON: I've lost my necklace . . . hey, can we stop so I can make another?

BENNY: Couldn't be you gave it to Mary ... could it?

RON: Aaron looked slightly sick and then relieved as Martin saved the day with an idea.

MARTIN: Let's make a bunch of necklaces, OK?

BENNY: Yeah, we can give them to our girlfriends.

RON: We set about making acorn necklaces by the gross. By the end of the afternoon, there wasn't an acorn anywhere in sight. Not one. Throughout the days that followed they gave them to everyone. The entire camp -- kids, counselors, and even Mrs. Nelson, the nurse became Acorn Society members. (Pg 29) The giving of the necklaces drew the camp together and gave us all a feeling of confidence and a penchant for adventure. One particular adventure I shall never forget was the mountain. (Beat)

One evening the normal recorded taps and Boy Scout pledge were followed by an announcement that special merit badges would be awarded to all those completing the climb to Lookout Mountain.

BENNY: If the Boy Scouts can climb that mountain, can we?

RON: (Pg 30) In the morning we made plans. Maps in the camp office gave the trail markings and location of the mountain. It was a six-mile hike round trip. We had no idea of the terrain. We took a bag of apples, some carrots, raisins and canteens of water. Dominic led the way pushing Spider. Next came Benny, wheeling himself, followed by Martin pushing Aaron. I took up the rear pushing Thomas Stewart.

(Beat) Each curve in the trail presented an obstacle; but (Pg 31-32) when the trail started upward, we had to turn around and pull the chairs from behind. (Pg 34) Our movement was reduced to pull, stop. Pull, stop. Pull. Perspiring and heaving for breath, Benny had to stop. He didn't say a word. Just stopped pushing. His chair slowly slid to a halt against Martin. Like a train being derailed we twisted to a halt.

SPIDER: (Pg 35) (dramatically sprinkling water from his canteen on the hillside) I hereby name this place Benny's Landing and claim this place and all its riches for the Acorn Society. (beat) (Pg 36) Well, what are you waiting for, Aaron? Break out the food!

RON: Here we were, sitting in the middle of a forest with wheelchairs that had until now known only city streets and "convenience ramps." (Beat) (Pg 62-63) Later that night camp filled with the chorus of Cum Ba Yah. We were at peace with the world. And what a marvel -Thomas singing faintly for the first time.

THOMAS: (singing) Someone’s singing, Lord, Cum Ba Ya

RON: Why can't life be like this? Human beings in all their magnificence, working to find that moment of pride. The feeling of belonging not just to oneself but to the entire universe. (Beat)

Camp days fled by. "How many days left?" was a constant question. The kids seemed to withdraw gradually but perceptibly into cocoons. Thomas stopped talking. Many children displayed symptoms of illness that marked their first few days at camp. Bedwetting returned. Kids on special diets who had been eating regular meals requested their pills again.

(Pg 78) [Then it was the final day of camp]. Now a silent exchange was taking place again. Children were being passed from counselor back to parent. Benny rolled slowly by himself from our presence. Spider was passed from arm to arm. Martin walked holding my hand. He was leading. Thomas Stewart had to be carried. His eyes were a little older and sadder. Aaron wanted to push himself to show his parents his strength. (beat) [These were] the members of the Acorn Society -- -- racers, [swimmers], mountain climbers, observers, [and above all children] And they were dying.

NURSE: (Pg 2) Most will not live past their teen years. It is nature’s way. (long beat)

RON: (Pg 80) Thomas and Aaron died one year after summer camp. Spider was killed by a car the following year. Martin died in a car accident four years later. Benny was the last child to leave this [world]. Of all the children he was the only one to have a funeral. At the final service Benny's mother gave me a white envelope. Inside was a crumpled acorn necklace. She said he gave them to everyone he met. (beat)

SPIDER: (Pg 35) I hereby name this place Benny's Landing, and claim this place and all its riches for the Acorn Society . . .
```

---

## IC-0306: Alien Boy

- Title: Alien Boy
- Author (byline): Will Scheffer
- Work: The Best American Short Plays 2001-2002
- Publisher: Applause Theatre Book Publishers
- Publication date as stated: July 2007
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ALIEN BOY, VOICEOVER
- Teaser before the introduction: Yes
- Spoken words (computed): 2138
- Already set (do not supply): none

### Source block (context only)

```text
Author: Will Scheffer
Book: The Best American Short Plays 2001-2002
ISBN: 978-1557837042
Publisher: Applause Theatre Book Publishers
Date(Month/Year): July 2007
```

### Introduction (context only: never use it for content warnings)

```text
Alien Boy by Will Sheffer
```

### Performance text (classify this)

```text
ALIEN BOY: Today I am thirteen. I don't want to be thirteen. I have always yearned to be older than my years. Therefore I have been described as a precocious child. I drink coffee. I smoke cigarettes. I use the words: masturbatory, ennui, and existential-liberally in conversation. But today I am thirteen. I am wearing my sailor suit. I come down here often in my sailor suit, to the Howard Johnson's in Bloomfield, New Jersey, and I wait. I wait for a man to come and take me away, away from this childhood that I do not belong in. A blonde man who is muscular and bold, I have seen him on TV. He will teach me how to be athletic and brave. He will give structure and meaning to my life. He will hold me in the dark. Just we two. I wait and wait. But he never seems to come.

ALIEN BOY: I was supposed to be Bar Mitzvahed today. But I told my mother I wouldn't go. I told her I had decided I didn't want to be Jewish anymore. My mother was distraught.

"You can't just decide you don't want to be Jewish anymore," she said. I told her again, "I don't want to be Jewish." "Why don't you want to be Jewish?" she asked me.

“In the street, children throw pennies at me, they call me Jew Bagel, in an age when it is possible for us to choose our own destiny, I have decided I don't want to go through life with the particular disadvantage of being a Jew. I want to be Blonde and Handsome like the men on TV. I want to drive a Volkswagen."

"Over my dead body, you'll drive a Volkswagen. This wouldn't be happening
if your father were alive."
"He's not alive," I said, "he's dead!"
My mother took a Valium and locked herself in her bedroom.

My father was a Jew.He came to America during World War Two. He was-an Alien. He left behind his mother, sister, his first wife, and a son. They died at Auschwitz. I have here their names, as listed by the Red Cross. Rebecca, Betsy, Rachel, and the son, Wolf, who was shoveled into an oven on the day of his thirteenth birthday in 1943. [He burns the names of his relatives with flash paper.]

I never got along with my father. He spoke with a heavy foreign accent. He was thin and pale and European, not at all like the men on TV. One day I was walking around the house in my mother's high heels and my father caught me. He slapped me and told me: "I never want you to walk in high heels again. Soon you will be thirteen, you will be Bar Mitzvahed, soon you will be a man."

"I don't want to be a man," I told him. "You're a man, I wish you were dead."

The next year he died of lung cancer. Now I wear my mother's high heels whenever she's not home. [He puts on high heels and twirls while humming West Side Story.]

I turn up the music from West Side Story and I twirl my baton. [When the lyrics reach: "I feel pretty, and witty, and gay"... The music stops with a screech and horror music fades in.]

Last night after my mother had cooked me a Swanson's frozen TV dinner, I was reading Everything You Always Wanted to Know About Sex but Were Afraid to Ask by David Rueben, M.D., and I quote:

VOICEOVER: "Male Homosexuality is a condition in which men have a driving emotional and sexual interest in other men. Because of the anatomical and physiological limitations involved, there are some formidable obstacles to overcome. In the process they often transform themselves into part-time women. They don women's clothes, wear makeup, adopt feminine mannerisms, and occasionally even try to rearrange their bodies along feminine lines."

ALIEN BOY: I don't want to be a homosexual. Until last night I didn't know I was one. I knew I was different, but I didn't think there was a name for it. I knew I liked to wear my mother's slip. I knew I liked to wrestle with my friend Nicky Sabatini, and I knew I didn't mind losing. I knew I liked to rub against the sofa watching Monty Hall on Let's Make a Deal and the cowboys on Bonanza. But then I read this:

VOICEOVER: "Some of the more routine items that find their way into the gastrointestinal systems of homosexuals via the exit are pens, pencils, lipsticks, combs, pop bottles, ladies' electric shavers, and enough other items to stock a small department store."

ALIEN BOY: That night I have a disturbing dream. Outside my window I see strange lights. A spaceship lands and a robot man descends from its steps and comes into my bedroom, He is very blonde and looks like my GI Joe doll and the devastatingly handsome Nazis I have seen in war films. He comes to my bed and takes me on his lap. He looks very cold like metal but when he touches me his skin is hot. He holds me in his hot arms. He says that: "You must tell me that you love me." I look into his blonde eyes. I start to form the words I love you. "I... Love..." I wake up screaming. [Sound: a horror' movie scream.]

It's two in the morning. I creep into the kitchen and go for the Yellow Pages. I look under the letter P. I find the names of all psychiatrists in Bloomfield. Both of them. Dr. Kaplan and Dr. Casey. I choose Dr. Casey, because he sounds more attractive. I write him a brief letter:

"Dear Dr. Casey: I think I am a homosexual. I have no money. I cannot tell my mother. Please help me. I want to be cured."

I find a stamp in my mother's pocketbook. For the rest of the night I dream of my doctor. The one who will save me. The man I've been waiting for.

The next day while carrying my tuba, I mail the letter to my doctor. The boys at school have stopped calling me Jewboy and have begun to call me pussy and faggot. I now dress in work boots and flannel shirts to disguise myself. Anxious weeks pass as daily, I run home after school to check the mailbox. Every night I stay awake until 4, praying to the God I do not believe in to save me from my sordid fate. Then one day a letter arrives addressed to me. [ALIEN BOY clutches the letter to his chest and opens it, his heart pounding.]

He will see me one week from today in his office. I am filled with excruciating anticipation. The week passes quickly, and on the day of our assignation I run from school to the bus that will take me to my hero. I have dressed in my argyle shirt and socks, corduroy bell-bottoms and platform shoes, tempting derogatory slurs from the boys in gym class, but I don't care, I am reckless with expectation.

I arrive at the address of Dr. Casey's office. I ring the bell and am buzzed into a small waiting room. "I'm here to see Dr. Casey," I say to the secretary with a hint of pride. As she knocks suspiciously on the doctor's door I look around his office. I am disappointed to find other people here. The secretary returns and ushers me into Dr. Casey's office. Suddenly, as I am face to face with the man who knows my secret, I realize why I have felt vaguely disoriented since arriving. Dr. Casey is a black person, like his secretary and the people in the waiting room. I am momentarily unable to process this information, as I have never seen a black doctor on TV. But the look of kindness in his handsome face reassures me. I imagine my small white face pressed against his strong black chest. The secretary leaves and the doctor asks me a few questions. "Why do you think you're a homosexual?"

"Because I like men," I tell him.
"What do you want to do with them?"
"I don't know-just be with them," I offer, searching for the correct
answers.

Dr. Casey seems satisfied with my answers and then rises from behind his desk. "I'd like to help you," he says. "But you understand I can't possibly treat you without the permission of your mother." He hands me the phone. "I'm afraid you'll have to call her and tell her where you are."

I dial my mother's phone number at work, unable to look him in the eyes. "Hello Mom?" "I'm at a doctor's office." "No, nothing's wrong." I hand the phone to Dr. Casey. "I think you should come down and pick your son up," he says. "313 Franklin Street." He hangs up the phone. "I'm sorry," he says. I look into Dr. Casey's eyes. [Pause] "I... You... Nigger!" [Sound: a horror movie scream.] [The BOY puts his hands over his ears. A beat.]

My mother collects me at Dr. Casey's office and she tells him: "What he's lacking is a male role model." Dr. Casey agrees and offers to treat me, but my mother nervously replies that, "There is a Dr. Kaplan in town, who I think would be a more appropriate choice for us." We walk briskly to the car. We sit in front of Dr. Casey's office in silence. My mother lights a cigarette. "Why didn't you tell me about this...problem?"

"There is no problem, I feel better already."
"Really, I think it's just a passing phase you're going through."
"Yes, I feel it passing already as we speak."
"What would you like for dinner?"
"Can we go to McDonald's?"
"Yes, I think that's a wonderful idea."

And that's the last we talk about it. Years pass.

I look at myself in the mirror as I prepare to meet my mother in New Jersey. After thirty years I must admit my boyish good looks and full head of hair have not diminished. I look remarkably like my dead father. An irony I am not unaware of.

I take the bus from New York City to my mother's small apartment. We see each other often, my mother and myself. We share an easy intimacy. As easy as either of us is capable. We even talk about my boyfriends.

Tonight my mother's taking me to dinner at McDonald's. Close and within walking distance, it is most convenient now that she doesn't drive anymore. I haven't been to a McDonald's in years, but it's the same as I remember it. It's different; but it hasn't really changed. It's like Cher.

My mother and I eat Big Macs and talk about current events. My mother is ecstatic about the passing of the "Gay Marriage Bill" in Vermont. She looks forward to the day I settle down with someone. She wants me to have the kind of love she had with my father. To not be lonely.

"Are you lonely?" I ask her. "No, no. I have so many friends," she says. "Why didn't you ever remarry?" "After your father, there was nobody else for me. You know that."

"Do you miss him?" she asks.
"Yes," I answer. "I miss him very much."
She delicately chews on a French fry. "I miss him too." She takes a gulp of
Diet Sprite. McDonald's seems to be making her nostalgic.

"But I wish I had done a better job, with you.. .after. . .," she says. "You know, I still feel bad about when you went to see that psychiatrist, what was his name?" "Dr. Casey," I answer. "I should never have made him call me." "Oh, Ma," I say, "You're confused. He made ME call YOU. He was a bad psychiatrist. He betrayed my trust."

And then it all comes out: "No." "I never told you this, but I opened that letter you got from Dr. Casey, you know saying he would see you. I made him have you call me from his office. I told him I'd sue him if he didn't. I was so desperate to know why you contacted him. I didn't know what else to do."

And suddenly it feels like I am falling. As if the room around me is falling away: "Darling." "I'm sorry." "Please forgive me." "I love you." "It's O.K.," I say. I stare at my hot apple pie. "You did the best you could." I start to form the words I love you. "I...love..." Inside myself I hear the roar of wind and the sound of combustion. "I love you, Ma. I forgive you. I love you. Of course, I love you."
```

---

## IC-0307: All the Stars Burned Black for Dumbo

- Title: All the Stars Burned Black for Dumbo
- Author (byline): Jared Botticelli
- Work: Fast Horse Plays: Round 3, Pgs 3-9
- Publisher: Fast Horse Drama
- Publication date as stated: Aug 2012
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1571
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jared Botticelli
Book: Fast Horse Plays: Round 3, Pgs 3-9
ISBN: 978-0615694894
Publisher: Fast Horse Drama
Date (Month/Year): Aug 2012
```

### Introduction (context only: never use it for content warnings)

```text
In life, choices are inevitable. Although they start small – the monkey bars or the swings – as we age, we are presented with monumental choices that have the power to shape the course of our everyday lives. For it is not the stars that hold our destiny, but ourselves. Every choice comes with a consequence and those consequences can be uplifting or devastating. Your stars may burn brightly or they may burn black.

All the Stars Burned Black for Dumbo by Jared Botticelli
```

### Performance text (classify this)

```text
A MAN sits alone on a park bench. For a moment, he observes the crowd around him and then, haltingly, speaks to an unknown bystander (the judge)

MAN: (Pg 3-9) This is a nice park, don't you think? Always kids here with their parents, when the weather's good. Playing on the monkey-bars, asking for just five more minutes of pushes on the swings. I like this park. It's good to just [be] here and watch the kids and their parents being happy.

Hey, you got a minute? Well, probably more like five minutes.

MAN: My wife's name is Brittney. B. I usually just call her B. Sometimes, when you know someone so well, you can just say it with one little letter. B. She just graduated from, um, teacher's college. Incredible. Long, dark hair, amazing smile. She makes a killer cappuccino. Yeah. I didn't want her to work while she was in school, but, uh, bills, you know? You gotta do what you gotta do.

We've been married almost three years. I knew her all the way through high school, and, uh, she helped me with my chemistry, my physics- B's the only reason I actually passed Calculus, with a C minus, but I passed. So we knew each other and we were friends but I never thought I was good enough, you know? We started seeing each other after we graduated and I guess she saw something in me that I, uh, didn't see. Still don't. B just does everything for the right reasons . . . Her star just burns bright because it does, you know?

She's just. . . I just love her.

. . . You know how sometimes you make one crappy decision, just one, right? And then everything after that, well, it just sort of builds on itself and gets bigger and bigger? Well, I, uh, that is, a couple of months ago - 9 weeks? ten maybe, it's sort of jumbled up now . . . it was a Friday and one of those crap days at work. I'd screwed up and I wasn't sure exactly how I was going to fix it, you know? And a few of the people from the office were going to go out. B was done with class already and didn't work that night so I called her to tell her I was going to pick her up, and uh, she tells me that she didn't go to her last class, that her stomach was kind of upset and she didn't feel too good. And then she tells me she really wants some tomato juice, and asks if I can pick some up for her, right? And I just thought that was the kookiest thing, right? She tells me she's okay, though, and that I should just go ahead and go. And she says, "I love you, Dumbo" and she hangs up. And, uh, normally I wouldn't go anywhere after work without B, but it's been a lousy day, and B suggested it, so I decide to go. You would've done the same thing, right? Right. . .

So, we go to that place off of 3rd and Alder -- they had live music on Fridays. And it was me and three of the other guys and uh, Debbie, this new girl they'd hired as a receptionist. I was only going to stay for a drink or two, but we all started to play this game of trying to guess what song the band was playing . . . uh . . . what's that song . . . Losing My Religion . . . "That's me in the corner, that's me in the spotlight, losing my religion . . . *" I notice this girl, Debbie, she's putting her hand on my leg under the table. I don't think a whole lot about it, right? But the hour hand is moving on the clock and then out of nowhere it's last call and everybody's talking about going home and it turns out Debbie lives on B's and my side of town, so, I offer to drive her, no problem. (Long beat)

So, I get to Debbie's house and she says I should really come in for coffee before I go home. And I think, I probably shouldn't, but, B's for sure sleeping at this point, so, I. . . uh . . . I do. I go in, and this girl, Debbie, she, uh, she doesn't make any coffee. (long guilty pause) I'm sure you get the idea. (long beat) It was around, I don't know, four in the morning. Debbie is sleeping but I get up and I throw up, two or three times and then I look in the mirror, but I don't recognize the person that I see there. No. That guy's not me. I don't know him. The guy that's me is the guy that lives in a small house with one large cat named Marbles and has a wife who he loves more than he thought was humanly possible. Not the ... uh ... thing I saw in that mirror in that apartment that night. I didn't know him. I still don't.

So . . . uh . . . I go out to my car. And I'm not doing so good. I'm driving and the lights are all whizzing past me and I'm trying hard to breathe but it's like there's a heavy granite block sitting on my chest. And it only takes me a few minutes to get home, because, uh, B and I, we don't live very far away. (long beat) I realize right off that there's something wrong. And the something that's wrong is that B's car isn't in the driveway. It's not here. And so, of course, the first thing that I'm thinking, [is] that B was there at the bar, watching, listening when I was singing: “losing my religion . . .*" and she saw that girl, that Debbie, get in my car and saw me drive her back to her apartment. [That] somehow, B was watching through a window or something when I, uh. . . stopped being myself with Debby. Turned into that something else. The other guy that I don't know.

So, walking up to our door, I'm thinking, B hates me now, she knows and she hates me. I push the door open. I turn on all the lights in the house, cuz I need to get rid of the darkness, ya know? And there's this note on the refrigerator, a note in B's little perfect handwriting: "I hope you're having a good time. I felt a little better, so I went out to get the tomato juice - just wanted you to know in case you get back before I do. I love you, Dumbo. -B."

I wait. I go outside on the porch, and I wait. And I look up and I see all of the stars in the night sky, and I wonder why they look like they do. I mean, they go on and on forever and I start to wonder how they can just burn and burn like that. It's like, uh, 3:45 in the morning and B isn't home. And so of course I'm thinking, she knows. I feel like my brain is trying to squeeze itself out of my head and I don't know what to do so I wait. And it's 4:00. And it's

4:13. And it's 4:24. And it's 4:46. And it's 4:58.

And then it's 5:04. I'll always remember that. 5:04. Because at 5:04, the phone rings, and I'm thinking, gee whiz, thank goodness, B just got a flat tire or went over to see her sister and she's calling to say she's spending the night there.

(Answering the phone) "Hello" (realizes it's not B).

This voice on the other end of the line is asking me, "Are you Britney Johnson's husband"

"Yes, I am, what's going on?"

And the voice on the other end of the line is telling me, "Sir, I'm very sorry to have to inform you of this . . .”

And I guess I'm hearing this guy's voice coming through the line, but it sounds like someone dead is talking to me. I can't really listen because I have to go down to the police station . . . (at the station) I have to show my ID and then go down this elevator and it sort of feels like I'm going straight down to hell or something. I come into this room with lots of silver metal and watch while this guy pulls out this drawer, and uh, he pulls back a sheet and uh . . . huh. . . on that big cold silver drawer thing is my B . . . my Britney . . . the girl who helped me pass Calculus and named me Dumbo . . . and uh . . . made me worth something . . . she's lying there and she's all messed up . . . real bad . . . (breaks down, cradles ‘B’s body and screams)

It's time to go home now . . . we have to go home . . . I am so f***** sorry! We just need to go home. (his voice gets softer and softer as the realization sets in – To audience) But, uh, we couldn't go home together. We couldn't. (Long beat)

I don't really look into mirrors anymore because, uh, I don't recognize myself. Or, I guess, the myself that I used to be. (long beat) Sometimes we make a really crappy decision and then everything ends up being all our fault. You know what I mean, right? We go to some bar some Friday night and we start sing, "That's me in the corner, that's me in the spotlight*" and then suddenly we're in some apartment with some girl and we go home only to find that our life, our light, our everything, was hit by a drunk driver on her way out for tomato juice. Tomato juice I was supposed to buy.
```

---

## IC-0308: Anger Box

- Title: Anger Box
- Author (byline): Jeff Goode
- Work: Anger Box: A Monologue Collection, Pgs 4-8
- Publisher: Original Works Publishing
- Publication date as stated: Sept 2013
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SPEAKER
- Teaser before the introduction: Yes
- Spoken words (computed): 1820
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jeff Goode
Book: Anger Box: A Monologue Collection, Pgs 4-8
ISBN: 978-1934962794
Publisher: Original Works Publishing
Date (Month/Year): Sept 2013
```

### Introduction (context only: never use it for content warnings)

```text
The Anger Box by Jeff Goode
```

### Performance text (classify this)

```text
SPEAKER: (Pgs 4-8) I'm only telling you this because I don't have to. So, off the record, just between you and me: . . . There's this guy.

And he works at the gas station on the corner of Aloe and Pennsylvania. (And, frankly, I think he owns the station, but he's too cheap to hire any help, so half the time you drive by, he's the only one there. So what does that tell you?)

So, anyway, so last week somebody kills this guy. Like a drive-by. Cuz at first they thought it was a robbery, but no money was taken. And now all a sudden they're calling it a hate crime.

So my question is: Is it still a hate crime if it was self-defense?

SPEAKER: I mean, what if this guy was just a total a**hole? Does that make it a hate crime? I mean, that's every murder, really, right? You gotta hate someone pretty bad if you're gonna kill them. I mean, it's hardly ever that someone gets murdered because people really, really like them. Why does it have to be a special category?

I mean, like this guy that got killed. Nobody liked him. I mean, if hate is your motive. Everybody had a reason to kill him. I coulda been the one to kill him if that's all it takes. In fact, I would say that I had more reason than most.

And I know you're thinking, "There's never a reason to kill anybody." But that's just so closed-minded. You don't know what he was like, this guy. I mean, this guy. . . No disrespect, but just between you and me. Thank God. Okay? Good riddance. There I said it.

And I know how that makes me look, but sometimes you gotta just stand up for your rights and say, I don't care what anybody thinks, that's just how it is. And if you disagree, I'm sorry, but you don't know.

Because that's the thing -- you'll have people from all over, from New York, or San Francisco, writin' about. . . I don't know. Intolerance. Or, I don't know, profiling. Because of how something looks on the surface, but do they even take the time to come down here and find out, or research or even ask somebody? Do they ask anybody? I mean, ask me, I'll tell you.

Cuz things aren't always how they look, is all I'm saying. And I stand by that. You can't just go judging people by how they behave.

Like, for example, this guy who got shot. Fine upstanding business owner, member of the community, right? But where did he get the money to own a business? Two years in this country, five years, I dunno, whatever. Doing what? Driving a cab, probably. Five years maybe, tops. Hasn't even learned the language and then - boom - owns his own business. Like I'm buying that.

I've been 15 years on my job and I don't own [nothin’]. I'm still paying for my truck. And now it's impounded so I can't even use it. So I'm paying $150 a month for nothing.

And this guy! Little station. Great location. Major intersection. Eight pumps. Not just four. Four on each side. All self-service so he doesn't even have to get off his [butt]. Just sit in his little booth and take my money.

So everywhere I go, that's what I think: More money for him. 25 miles to the gallon, I get. So every 25 miles - more money for him. I haul a load of trash out to the dump. Money in his pocket. Go to a ball game. Money in his pocket. Everything I do. Who's gettin' rich? Achmar McYahoo.

I could run a gas station. And I - check it out - would have full service. Check your oil. Windshield. Tires? No problem: tires. At self-service prices. (taps his head) American ingenuity.

But that's the thing. Being an American don't count in this country.

"Sorry, we need collateral. We need, I don't know, credit reports." And, "oh, what's this I see? You owe American Express $1000 dollars?"

No! My girlfriend owes American Express a thousand dollars because that's her engagement ring that she charged. That I let her pick out, because nothing can be perfect for her. So you go ahead, honey, you just pick the one you like, because that's the kind of guy I am. And then when I find out it's a thousand dollars . . . Do you know how long it takes me to make a thousand dollars?

It doesn't matter. It doesn't matter if you know. She knows how long it takes. And when I try to discuss it with her, can she be reasonable? No, that would be too much to ask.

So "I'm sorry we cannot authorize your loan."

You know why they have armed guards at a bank? Exactly for that. So they can say that to your face and they got somebody around to pull you off 'em before you're completely finished.

But this Egyptian . . . Let me ask you one question: What kind of collateral does he have? What kind of credit history does he have? I'll tell you what - none. I'll tell you what he's got. The Mafia. That's how they do it. This Middle Eastern Hindu Palestinian OPEC crap. Where they all stick together, because why? Because they all wear turbans? Because they all have brown skin? My cousin Bobby almost married a Mexican chick, so don't talk to me about racism.

I'll tell you what it is. It's all this fundamentalist Buddhist crap where Allah teaches them that we're the Great Satan because we like Freedom and Equality and because we think women look hot in a bikini instead of all those veils and baggy robes so you can't tell if they're fat or not.

Cuz you know that's what this is all about. Because when Mohamed gets back to the hotel room on his wedding night and finally gets his virgin bride unwrapped out of all her tarps and it turns out she's a pig. . . Yeah! he wants to blow up some Americans. I would, too.

So when they got a problem, instead of just changing it in their Bible like we do and problem solved, they have to go: Okay, now everyone else has to suffer, too. So they do this "we all have to stick together" thing and get rid of Israel - like that's their problem. So the Arabs support the Palestinians. And the Libyans help the Albanians. And Iraq and Iran and Yemen.

And that would be fine if they all wanted to stay over there and be Islamic in Mecca. Which seems like the obvious thing if you ask me.

But what happens is one of them comes over here. And he wants to open a gas station. So he can sell their oil over here. And he doesn't even know the language. So is the guy at the bank going to approve that? No, because the guy could just say, "I didn't know what I was signing." Or "It's against the Koran to pay interest" or some [crap], so he can't go to a bank.

But it doesn't matter because they just get some sheik to go in with him on it because he's making a profit on the oil anyway, so it's all gravy for him. So they can have as many gas stations or 7-11s as they want at pure profit until they take over that way.

But you don't have to believe me.

I shouldn't even be saying this because: Religion and politics, you know what they say. And this is both. So never mind. It's a free country, right? So what if an honest American can't make an honest living and gets arraigned on assault charges while this [idiot] is charging almost 2 dollars a gallon and won't even wipe your windshield.

And he gives you this look every time you walk in.

Because you know what it is, really? This is the thing: We have something in this country called "innocent until proven guilty" I just want to say that up front. Innocent until proven guilty.

Because what it is, really - This guy thinks I did something to his daughter. And I don't even want to get into this he said/she said because that doesn't even matter.

That's not the point, because the point is. . . Whatever happened. Whatever he thinks happened. He doesn't know.

I know he doesn't know, because how is he going to find out? She's not gonna say nothing. They can't even look a woman in the eye without a veil on. You think she's gonna tell him how her date went?

So, every time I go in there, he looks at me like he knows I'm guilty of something which I know for a fact he don't know. But that's how he looks at me anyway. But where's the proof? Where's the presumption of innocence? For all he knows it could be that it turns out it was consensual. Did he ever think of that? That maybe there's a reason she didn't go to the police. That maybe there's a reason she doesn't talk to him about it. Like maybe in this country it's none of his business if she wants to go to a party and doesn't feel like telling him every little detail of what goes on in her private life.

So she makes [stuff] up.

Did it ever occur to him that whatever that little b*** told him - if she even told him anything at all - which I don't think she did - isn't exactly the whole truth?

So now every time I go in there I have to feel like I'm on trial for something when I'm there to give him money! That's the thing that pisses me off. I'm the customer. He's getting rich off me. You'd think there'd be some kind of common courtesy to smile at least while he's raking me over the coals with every gallon. I didn't ask to be out of gas. But he makes me feel like the Inquisition every time I walk in.

Listen, if you don't like it, don't open a store. Go back to driving a cab so you can decide who you pick up and who you don't based on the color of their skin, or what part of town you think they live in that you don't go to.

But if you're gonna open a business in my part of town, then you're gonna get people like me comin' in, because this is a free country. And if you don't like it, you’re free to leave it and go back to wherever it is you’re from that everybody else is just like you so you can discriminate against your own kind.

But don't come in here with your bombs and your racism and your centuries-old quarrels that nobody understands and blame innocent people because you don't have nice stuff in your own country. Because that's where somebody ends up dead.

So don't ask me, but that's what I think happened.
```

---

## IC-0309: Angry Alan

- Title: Angry Alan
- Author (byline): Penelope Skinner
- Work: Angry Alan & F**ked: Two Plays, Pgs 9-42
- Publisher: Oberon Books
- Publication date as stated: Oct 2018
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ROGER
- Teaser before the introduction: Yes
- Spoken words (computed): 2268
- Already set (do not supply): none

### Source block (context only)

```text
Author: Penelope Skinner
Book: Angry Alan & F**ked: Two Plays, Pgs 9-42
ISBN: 978-1786826176
Publisher: Oberon Books
Date (Month/Year): Oct 2018
```

### Introduction (context only: never use it for content warnings)

```text
Roger never questioned what it meant to be a man. At least not until the world began to shift. Once, masculinity felt simple: a job, a family, a son who looked up to him. But when everything he thought was solid begins slipping through his fingers, he relies on Angry Alan for help.

The rules have changed: women are speaking out, roles are reversing, and Roger can’t find where he fits anymore. Being a man must mean something! It’s only when his son begins to question his own gender identity that Roger’s confusion turns into something else entirely.

Angry Alan by Penelope Skinner
```

### Performance text (classify this)

```text
ROGER: (Pgs 9-13; Where it Begins) Things are what I would consider to be normal. Not the old normal. The old normal is long gone. On a Monday morning Roger-from-before would be getting in his fancy car and heading into the office. But what you're looking at here is Roger-Now. And Roger-Now is the assistant store manager in the Walnut Creek Safeway and he doesn’t work Mondays – instead I end up watching a video which is kind of amazing. Then I click on a link undeneath to the man who uploaded it. He calls himself Angry Alan -- a pioneer of The Men's Rights Movement. Have you heard of that? Apparently it's a natural evolution from the women's movement because basically, in a nutshell, feminism was so successful. We're now living in a 'Gynocentric Society' and now -- now it's like Beyonce says: Who runs the world? Women. And because of this, ordinary men are beginning to suffer. And Alan doesn't just say these things: he backs it up with evidence. Statistics. Data. He's got his own website and his own Youtube Channel

ROGER: (Pgs 9-13; Where it Begins) I keep on reading and watching videos and at a certain point I find myself up on my feet and something incredible happens. (Roger is in a state of rapture) My red pill moment! for the first time in a really long time I feel like someone is speaking to me in a language which I completely understand.

(Pgs 14-16, Fish Tacos) They don't teach Men's Rights at the Community College by the way only Women’s Studies -- like how bad things 'still are' for women? [How] about how men are raised to value women's feelings over our own. How we're taught early on that our only worth as human beings lies in being financial providers.

(Pg 17-18, A Son!) I take the red pill. And I learn about how the entire legal system and the structure of the family courts are rigged to favor women. And mothers. And meanwhile men like me, fathers who love their kids, are getting exploited. (shows photo of his son) This is Joe. People say he looks like me. (beat) He's born and Suzanne gets post-natal depression which I don't know if anyone here has ever experienced that but it was extremely challenging for me. And next thing I know we're getting divorced and then I lose my job and Suzanne got custody. I don't see Joe except on weekends or holidays. I've paid her all this alimony. And in return I've been alienated from Joe through absolutely no fault of my own.

(Pg 19-21, #MeToo) You women need to think about what it is you actually want. Because Alan says the Modern American Woman wants it all her own way: she wants her own career and she wants a rich guy to treat her like a princess. She wants you to respect her intellectually then she invites her girlfriends over to watch Love Island. You can't have both now. Can you? Alan says Modern American Men are getting more and more confused. And we're taking more and more of the blame when you women don't get what you want.

(Pg 22-23, Impulse Buy) Alan’s helped fund a home for men who are victims of domestic violence. Or. . .or. . . or survivors of male genital mutilation. I go onto Angry Alan dot com and I click, and I click, and I pay and I'm going to [his] conference in Cincinnati. I get my tent out of the garage. Book a spot at a KOA campground and I feel this kind of exhilaration. Like I'm changing. You know? I'm becoming someone new.

(Pg 24-26, Two Dozen Eggs) Alan points out how unfair it is that in an emergency like on a sinking ship the rule is you have to save women and children first. He says this is because men's lives are considered to be innately less valuable. Are we men disposable, he asks? Are we less worthy of saving for some reason? If a ship was sinking who would you rather save? A stranger or your own son? Your own father? See when you take the red pill you start to question all the things you've just taken for granted your whole life.

Alan says 70% of the people who kill themselves in America are men because we're raised not to show our feelings. See? All we hear about is how much women suffer and meanwhile guys like me for example -- my wife walks out on me and takes my kid. And you know what? I haven't cried in front of another human being since I was 8 years old.

Then I lose everything I've worked for: AT&T and that day in Bill Jefferson's office when he told me they were letting me go. The look on his face. This look like sorry man. It's just one of those things. I should just go get my gun I thought. Because there's not much use for me now. A middle-aged guy starting all over again in this market? People want 23-year-olds fresh out of college or even 18-year-olds who were smart enough not to go! But guys like me? 20 years’ experience at AT&T means diddly squat apparently . . . (beat, change of topic)

(Pg 30-31, The Orange Lamp) The good news is Joe's coming camping. (elated and proud of himself) That was my brilliant idea. I bring Joe out to Cincinnati on Saturday night. He can stay in the tent with me. I still get to go to the whole first day of the conference, then on Sunday morning we can go for a hike maybe do a little shooting or fishing and we can get back to the hotel in time for Alan's keynote speech. Pretty inspiring for Joe don't you think? To hear Alan speak in person. I wish I'd had that kind of opportunity when I was 14 that's for damn sure.

(Pgs 32-34, Cincinnati) So I get here on Friday night and pitch my tent at the KOA. I'm extremely nervous and I wake up at dawn and I get to the hotel bright and early.

(scribbles his name on a name badge and pins it on his chest) The whole scene is very upbeat and quite exciting and I start to feel somewhat like my old self again, you know? It's kinda like when I used to go to conferences back in the day with AT&T: the sound of men laughing and talking and we're all here for a common purpose. And because of that purpose we matter. You know?

(claps, whistles and claps again as an unseen speaker steps up to present) With every speaker that gets up on that podium I start to feel more and more optimistic that we could one day live in a world where all of this injustice that has been affecting me -- maybe one day we could live in a world without it

One of the speakers, he's talking about false rape allegations -- and he makes one joke -- it gets a laugh so big they have to turn his mic up because we're just so pumped with the frikkin freedom of it all. You don't realize until you get here; you don't realize how oppressive the Gynocentric Society is. You get used to living your life feeling bad about who you are -- feeling guilty, feeling anxious in case you do or say something which, once upon a time would've been totally fine, but is suddenly completely unacceptable for reasons you are unable to comprehend and living your life in terror that if you put one foot out of line you will be viciously and violently attacked on the internet and feminist lynch mobs will trash your reputation. And that's no way to live. That's no life at all. Is it? Misunderstood and completely frikkin powerless. (beat, shakes it off)

(Pgs 35-57, Honey Badger) The most important thing is I'm here and I'm having a great time. And I've got my son coming up to see me and we're going to get to know each other again and things are good, you know, things are -- really when you think about it things are just about perfect. (a long pause)

(Pgs 38-42, Precipice) I have a son. His name is Joe. (beat) I'm sorry I'm all over the place. I've missed a bit. I need to start before . . . It's morning and we're in the woods early and it's a beautiful day. I've got the gear in a duffel bag and the gun on a strap on my shoulder and Joe's got his little backpack and he's carrying the lunch and the water and the birds are singing and we hike for a good couple of hours and eventually we get to a clearing and we sit down to drink some water and I can tell he's about to come out with it but when he does . . .

I say: What does your mom say about all this? And he says: She's getting used to it. Slowly. Why didn't she tell me? I say. And he says: Because I asked her not to. Because I wanted to tell you myself. In person. Even though it was really hard, Dad. I've been feeling sick for days. Are you mad at me?

I say: No. I'm mad at your mother. Clearly this is because of that school she sent you to. And he says: It's got nothing to do with school, Dad. I've been feeling this way for ages. And I say ages? My god, you haven't even been alive for ages, Joseph. What about football? Hockey? What about that girl from your drama club? I thought you had a crush on her. And he says Dad: I'm not gay. I'm just saying I don't identify as a male. And I say I literally don't even know what that means. You got a d***don't you? So, you are a male. And he says it depends on your definition. And I say no it doesn't. It's a biological reality. And he says I knew you'd say that. And he opens up his pack and takes out this book and reads me part of it:

Both women's and trans liberation have presented me with two important tasks. One: to join the fight to strip away the discriminatory and oppressive values attached to masculinity and femininity. Two: to defend gender freedom -- the right of each individual to express their gender in any way they choose, including the right to change their sex, whether female, male, or any point on the spectrum between.

Do you have any idea what any of that means? Because I sure as hell don't. And I look at him and I go: Joe. And he says: Katie. And I say: I'm sorry but, no. I have a son. His name is Joe. And he doesn't say anything. (long silence)

And [then] he goes: Dad, I'm not interested in surgical intervention. But I do want to wear dresses and make up and high heels and I want to challenge the notions of gender that exist in mainstream society. And I say: Well surely you can just identify as a girl without wearing a dress son. And he says: I just want to be able to choose! Why do we have to be boxed in by these narrow definitions of what is or is not a man? (beat) You're ashamed of me.

And I say: This is not a game ok, son? This could affect your whole future. People find out about this? What about when you want to try and get a job? And he says: Please, Dad! I need you to accept me! I'm not asking for permission. And I say: Well maybe that's the problem here. You know? Because who's gonna pay for these dresses? Huh? Who pays for every damn thing you own? Huh? I do! I pay for the clothes on your back and the food on your table and that means I have a right to be involved!

And suddenly as I'm saying this everything starts crashing in: all the injustice. All the things I've read and seen. How unfair it all is and how helpless I feel and how angry I am because of all the things I've had taken away from me - my job, my basic human rights and now my own son?

And I can hear Alan's voice loud in my head saying: Roger how much more can you take? (slowly takes the gun from his shoulder and points it at Joe while he speaks) And that's when I just let go. (with growing intensity and anger) I am so sick of this shit. I'm sick of you disrespecting me and your mother scrounging off me and I'm sick of everyone blaming me and I'm sick of people thinking they can walk all over me. Do you know what it cost me to raise you? Do you have any idea what I've sacrificed for your sake? Do you?

And for some reason he's got his hands up in the air and his eyes are wide and fearful and l realize I've grabbed the gun from off my shoulder. I didn't mean to but I'm pointing it at him. I'm standing here pointing the gun at Joe and his eyes are wide with something like terror but he doesn't say anything he's just standing there shaking and I say: I think I need to take a walk, ok?

And I put the gun down carefully. I place the gun on the ground and I back away and I leave him there. . . (long beat) I walk and I keep walking until I can't walk any more. I stop on the edge of the rocks over a wide valley and I wonder what's going to become of us. Because this can't be the future can it? Everyone just changing the rules. I can't just decide one day not to be a man, can I? I'm a man. I'm a man. And deep down I know that's what my son is too. Course he is. He's a man. He's a man. I'm a man –

(the sound of a single gunshot echoes from below) What was that? Did you hear that? Sounded like . . . (realization dawns on Roger. He stays very still, horrified. He struggles for breath and breaks down crying)
```

---

## IC-0310: Aryan Birth

- Title: Aryan Birth
- Author (byline): Elizabeth Page
- Work: The Best American Short Plays 1992-1993
- Publisher: Hal Leonard Corporation
- Publication date as stated: Nov 1993
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DAVID
- Teaser before the introduction: Yes
- Spoken words (computed): 2798
- Already set (do not supply): none

### Source block (context only)

```text
Author: Elizabeth Page MN State Qualifier
Book: The Best American Short Plays 1992-1993
ISBN: 978-1557831675
Publisher: Hal Leonard Corporation
Date (Month/Year): Nov 1993
```

### Introduction (context only: never use it for content warnings)

```text
Aryan Birth by Elizabeth Page
```

### Performance text (classify this)

```text
DAVID: You can't help who your parents are, right? I mean even if you buy the Hindu thing-that the soul is out there looking to get reborn. Waiting for, say, two child abusers to get pregnant. Not that I'm blaming the kids on the wrong end of a cigarette, I'm not. And not that I'm blaming her parents. Necessarily. Y'see that's the thing about the Hindu trip-if the soul wants to come back, you're stuck. This is your life. Too bad if you don't like it. So why blame her, right? She's stuck. "Fraulein Mueller, in ziss lifetime you vill vork on your anger, if you please. And you vill take it out on David Cohen. You'll know him. He's a nice boy viss a bullseye on his heart." Is there anything worse than whining? Besides, if you pick your parents, you damn sure pick your lover. So we're both to blame.

DAVID: The first thing I saw was her soul. Scene: I'm in the islands, in a temple, meditating. The sun's coming up-you can hear it, the wind picks up, the trees start to move, the birds sing. I open my eyes ... She's so deep in the meditation it's like she isn't there. I can't even make out her face. Just this hum-energy. Hummm ... She hummed me in and that was it. Yeah, she was beautiful. We chose each other. We couldn't help it. I knew it wasn't going anywhere, I was going home – New York. She was going back to Austria. I went home. And she came with me.

The only problem-actually there were two problems. Th. visa and the TV. The visa meant she had to leave the country Soon. Actually I guess it's tied in-borders, nationalism, the World War II thing. I live in this country, she lives in that country. And in this country we hate that country. Which is where the TV comes in. We were in the apartment a lot so the TV was on. "Nazis und communists. Nazis und communists. Das ist all you people know." . You make the bad guy a Nazi, you don't even have to give him a character, just put him in a uniform. Or her. Where we got into trouble was when I'd try to defend the programming-which meant, of course, defending the obsession in this country with Nazis. Because I'd have to get into, y'know, what they did. And then she'd get all defensive and think I was attacking her family. And I'd get all defensive and say that her family would have gassed my family.. I don't know what I expected. I guess, well, remorse. Not that she did anything but y'know, sort of collective remorse. I mean I could understand why she was defensive. If my father were a Nazi ... When I saw her meditating I didn't pick up that her father was a Nazi. It didn't occur to me, all right? They were all Nazis. It was a political party. People were starving, there weren't any jobs, it was politics. They lived in the mountains, her father'd never even seen a Jew. So fine, I wasn't shtupping her father. He used to beat her. And lock her in a closet. Now this was interesting. She didn't think there was anything particularly wrong with that. Not that she enjoyed it, she hated him. But that's how kids were brought up there. If they misbehaved, they were hit. Or locked up. Do you read the Times? The New York Times? Did you see that article on the op-ed page, This psychiatrist gets this hunch-he's been travelling around Europe, noticing how kids in different countries are different, play differently, and he gets this hunch. This is in the early 70s [He takes a newspaper article out of his pocket.] I carry this around. It makes me feel like less of a jerk. Okay ... "The result was that the Danish and Italian adults committed no acts of aggression against children as compared with 73 aggressive acts by German adults against children. The German children committed 258 acts of aggression against other children, as compared with 48 aggressive acts by Italian children and 20 by Danish children. The tentative moral of the story is that Germans mistreat their children more often than Danish or Italian adults, and that the children take it out on other children. One would suppose that aggressive children grow up into aggressive adults - adults whom I don't trust ... " It goes on. Anyway. Now obviously the point is not that the Fascists had troubled childhoods and we should like overturn Nuremburg. But he used to beat her up. And that does something to a person. I mean you can understand how they might not be as sensitive maybe as they could be. People like that need a lot of love. So I've got this wounded bird. And she doesn't even know she's wounded. She thinks she's this invincible Rhine maiden Brunhilde, running around the world, having an affair with a Jewish man. She doesn't even realize she should be terrified. Okay so she decides she wants to go to this peace conference being held at another ashram up in Canada. A lot of people she knows are gonna be there. This is, what, '87, before the wall came down and I'm thinking, okay, maybe we can break through some of the denial going on here. An international peace conference has to deal with Fascism. Doesn't it?

So we go. You ever been on the Freedom Trail? You follow the yellow brick road around Boston from one old thing to another? Anyway we're driving and we hit Boston-and she's heard of it-so I take her on the Freedom Trail.. "Images of the Holocaust." Don't ask. There it was, these floor to ceiling blow-ups of emaciatedskeletal-children, mounds of corpses. You've seen 'em. She's very quiet. I ask her if she wants to leave-she's always dismissed this stuff before-but she says no and so we walk through the exhibit. It was pretty good. I've seen more gruesome stuff-y'know the documentation of some of the medical-and I use the term loosely-experiments. Where they filled women's wombs with cement, froze people alive. In the name of science. But they had a jar full of hair, piles of baby shoes, memos describing transport and "disinfection" and of course the photographs. One of our main arguments was about the nature of the camps. Really of the "final solution" itself. She claimed it was wartime and that the camps were prisoner of war camps. I know, but I'm telling you, she actually believed that. I found that out in Boston. Until that day she'd say, okay, there were maybe individual sadists who got carried away, that the Japanese had camps, that the Brazilians slaughter their Indians. I kept screaming about the decision coming from the top, that it was planned, that it started in someone's heart and mind, that it wasn't just separate, impulsive acts of sadism, that the act of deciding to annihilate a people-that's what made it such an abomination. More patriotic ... and more Jewish. We leave the exhibit. She says, "They don't teach this in the schools. Our parents don't talk about it. It is taboo. Verboten." She's quiet the rest of the day.

I changed her. Whatever you can say about what happened, she was changed. Okay so we get to this peace conference. I don't know what I expected. I guess ... "Us and Them." Y'know, what you get when you take the bus to Washington to do a march. Placards, cameras, people with hangers on their heads screaming at people with pictures of butchered fetuses. A "we shall overcome" kinda thing. Well this was all "Us". I mean it makes sense that none of "Them" are gonna pack a sleeping bag and catch a cab to the mountains so "Us" could have a target. But it was weird. It was like whatta you do when the enemy isn't there. There was an article in Vanity Fair awhile back about how the children of the Nazi superstars are getting together for group therapy. This blew my mind-having been through every kind of therapy, self-help, analysis, primal scream, tonka bats-you name it. I'd practically written the article in my head before I paged back to where it started-middle-aged Nazi kinder holding hands and sobbing. Let me just read you this one little bit. [He takes the article out of his pocket.] This is Martin Borman, Jr., about age 14, who's been taken for tea with his little sister at Frau Pothast's-Himmler's mistress. Okay, they've had chocolates, a little turn around the garden, now it's time for a special treat. She takes the kids up to the attic. "When she opened the door and we flocked in, we didn't understand at first what the objects in that room were-until she explained, quite scientifically, you know. Tables, and chairs, made of parts of human bodies. There was a chair ... The seat was a human pelvis, the legs human legs-on human feet. And then she picked up one of a stack of copies of Mein Kampf-all I could think of was that my father had told me not to bother to read it, as it had been outdated by events. She showed us the cover, made of human skin, and explained that the Dachau prisoners who produced it used the Ruckenhaut-the skin of the back-to make it." [DAVID takes several long breaths and then looks around the audience for a moment.] Be glad it hurts. That's the point. It should hurt. It must hurt. Borman, Jr.- who after all was showing up for therapy, I mean, he's at least acknowledging there's a problem-Borman Jr.'s described as relating this incident with a "toneless voice." He later says that to call the people who did this swine is an insult to swine but other than getting red in the face, that's it. Am I the only crier here? No. Something's missing-maybe it was never there or maybe they bred it out of them but that inclination to pity, compassion, emotional identification, tears ... Anyway, I'm having a wonderful time in the mountains ... enjoying simultaneous translations of scintillating speeches by obscure Nato attaches, taking Kirlian photographs of my chakras and learning how to manipulate my aura so as to create a peaceful personality, grading an airstrip behind the tents and meditating nightly so as to attract peaceful extraterrestrials, learning everyone's rising sign, eating soggy samosas, smiling and chanting in the rain. Let me tell you, peace is hard work. And Maria? She might as well be in Berlin. She won't connect. And I'm not making her. Hey, I've read as many self help books as the next American. If the fraulein needs her space, fine. I know Boston wigged her out. I saw something and she's scrambling for cover. So let her scramble, we're going home. We took a train back from Montreal. She wasn't feeling well and slept against me for an hour. You remember the dumbest things, y'know. The way that felt, the weight of her head against my shoulder. Like a baby's head, heavy. We get back to New York and I don't know. Maybe it was being around a lot of people at the ashram but suddenly the silence in the apartment was sonic. I mean I could hear her breathing. And since she wasn't doing much talking, I started reading her breaths. A short one-she just thought of something. She's holding her breath-she knows I'm listening. A long one-how long till I get out of here. Fine. I go see my sister for a couple of days. She wants space, I'll give her some space. Sixteen hours and she wants me to come back. Anyway I go home-she's still not feeling good. She's pregnant. Oh and she's Austrian and the clock's ticking, she's got, what, a couple weeks and her visa runs out which means if I even want to talk to her without paying Ma Bell we have to get married. So. Jews don't have reincarnation. Not that they don't take the long view but you only get one chance with them. Hindus get all the second chances they want only they don't enjoy them. Basically Vishnu says okay, you want it, you got it-the punchline being that someday you'll realize you don't need it and then you get the door prize-bliss divine. But until then, you're coming back. Which puts a certain spin on parenthood. I mean your kid isn't new-he's coming back. Which makes it less intimidating-you're just one in a long line of fathers-and more intimidating-why me? What does this kid need? What are we going to teach each other? I was really curious. I was ready. She wasn't. She hadn't found herself yet. Couldn't I understand that she needed to do that? Didn't I realize ...

I'm not a right-to-lifer, okay? I mean I let it happen. But that doesn't mean I have to be happy about it. This wasn't just a tablespoon of cells to me, okay? This was her, this was our relationship, this was me, my son, my daughter, my genes, my history. [He taks a deep breath. He's rattled. He starts searching in his pockets ... ] They kept correspondence ... [He finds a Xerox, spreads it out. Touching it seems to steady him. He reads ... ] "To the Central Construction Office of the SS and Police, Auschwitz. Subject: Crematoria Two and Three for the camp. We acknowledge receipt of your order for five triple furnaces, including two electric elevators for raising the corpses and one emergency elevator ... " It's that cleaning up thing, y'know? [Singing.] "The party's over ... " You think I'm sick? They were competing for these gigs. [He searches his pockets ... ] And the competition suggested ... [He finds another Xerox] ... what... "For putting the bodies into the furnaces, we suggest simply a metal fork moving on cylinders. For transporting the corpses ... " [He trails off. He's rattled and takes a deep breath, speaks quite calmly ... ] Look, I'm glad I live where it's legal. But you have to admit it's not like filling a tooth or getting a mole cut off. I mean if you choose to "not continue" a life for the sake of your own life, you pay the price. Life is expensive. But Maria, she was impervious. She'd made the decision and that was it. Who cares. At first I thought she was just reacting to me, y'know because I was really upset. So, y'know, she'd be cool. But no. It wasn't that. And it wasn't just that she was selfish although I think she is. It really honestly didn't mean anything to her. And I don't mean me or the relationship. She claimed she still cared about me, wanted the relationship. But the baby-it might as well have been a hangnail.

And that scared me. She called it "the procedure"-I thought she didn't like the word abortion but to her that's what it was. A "procedure". [In a German accent.] "For putting ze bodies into ze furnace, ve suggest simply a metal fork moving on cylinders." As soon as she made her decision she started drinking again-I mean she's not an alcoholic but y'know pregnant women aren't supposed to drink. And she started having wine with dinner again. And I thought of that poor kid being drowned in Beaujolais. Even if it was gonna die in a couple of days. She said I was sentimental. And I called her a fascist bitch. And that was the end of that. Ever since the wall came down, the Berlin Wall, I've been having a dream. I hear knocking at the window and I turn to see what it is-a branch maybe. But it's a little child, a little girl, hanging out there in the darkness, knocking on the window, wanting to come in. I know what I'm about to say is not spiritual. But I feel like I was allowed to experience something. She was cold. Maybe I'm sentimental but she was ruthless. Without Ruth. Who, if you remember the story, was a very compassionate woman. Maria had no compassion and I don't think any of them do. That was always my trouble thinking about the holocaust. I could never imagine how a human being could do that to another human being. But now I can. And maybe that makes me a racist and just as bad as they are but I don't trust them. And I never will.
```

---

## IC-0311: As Is

- Title: As Is
- Author (byline): William M. Hoffman
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Oct 1985
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SAUL, RICH, DOCTOR 1, DOCTOR 2, TV ANNOUNCER, CHET, BROTHER, PARTNER, PWA, ROBOT, HOSPICE WORKER
- Teaser before the introduction: Yes
- Spoken words (computed): 1723
- Already set (do not supply): none

### Source block (context only)

```text
Author: William M. Hoffman
ISBN: 978-0822200734
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Oct 1985
```

### Introduction (context only: never use it for content warnings)

```text
In 1981, the first cases of AIDS were reported. According to the CDC, by December 31, 2000 nearly 450,000 people in the United States had died. See . . . In the 1980’s AIDS was poorly understood by the general public. It was a disease stigmatized as an illness impacting primarily the gay community and there was no known treatment. This selection follows two gay men in the early 1980s dealing not only with the AIDS epidemic but also with the fear that swept through our society at the time. As Is by William M. Hoffman.
```

### Performance text (classify this)

```text
1st MAN: (Pg 30) The first time I heard about AIDS was in the Paradise Garage, a disco I used to go to. I won a raffle, the proceeds of which went to help people with this strange new disease. I didn’t even know what it was. 2nd MAN: I thought AIDS was like Legionnaires ’ Disease, or Toxic Shock Syndrome, or Sickle-cell Anemia, Alzheimer’s Disease – one of those rare diseases you read about in the papers.

SAUL: (Pg 16-17) I visited Teddy today at St. Vincent’s. It’s very depressing . . . He’s lying there in bed, out of it. He doesn’t even know you’re there. (Pause) Jimmy died, as you must have heard. I went out to San Francisco to be with him the last few weeks. He was in a coma for a month. Everybody wanted to pull the plug, but they were afraid of legal complications. I held his hand. He couldn’t talk, but I could see his eyelids flutter. I swear he knew I was with him. (Pause) I haven’t slept well for weeks. Every morning I examine my body for swellings, marks. I’m terrified of every pimple, every rash. If I cough I think of Teddy. I wish he would die. He is dead. He might as well be. Why can’t he die? (Beat) Say something, damn it.

RICH: I have it.

DOCTOR 1: We call it a “Pre-AIDS Condition”

DOCTOR 2: “AIDS-related Complex”

SAUL: I don’t think that’s funny.

RICH: That’s the bad news. The good news is that I have only the swollen glands . . . and I’ve lost some weight. (Pg 18-19) I tire easily. My temperature goes up and down.

SAUL: Doctors make mistakes all the time. Remember when they told my niece she had skin cancer? It turned out to be dry skin.

TV ANNOUNCER: (Pg 20) The simple fact is, that we know very little about Acquired Immune Deficiency Syndrome. Its victims may live a normal life span, or they may have only a few weeks. Fortunately, so far this tragic disease has mainly been confined to the high-risk groups and has rarely affected people like you and me. When will science conquer this dreaded plague? We don’t know. We simply don’t know . .

SAUL: You’re my friend. You’ll stay with me till you feel better.

RICH: (Pg 21) Aren’t you afraid I’ll infect you? Paper plates, Lysol, face masks – no. I’d prefer to live alone, thank you. . . Besides, if I live with you, where am I going to bring my tricks?

SAUL: You pick up people?

RICH: (Sarcastically) I lurk in dark corners where they can’t see my lumps. I’m like a shark or a barracuda, and I snap them up and infect them.

SAUL: How can you joke about this?

RICH: I don’t care. I’m going to die! I’ll take as many as I can with me. And I’ve pissed in the Croton Reservoir. I’m going to infect the whole city! Wheee!

SAUL: (PG 22) Give me a straight answer. Do you still pick up people?

RICH: Maybe I ought to wear a sign around my neck and ring a bell. “AIDS. I’ve got AIDS, stand clear!” Would that make you happy? Or maybe I should dig a hole in the ground, douse myself with kerosene, and have a final cigarette. No muss, no fuss. Is that what you want?

SAUL: Forgive me for not trusting you. It’s just that I’m frightened of it.

RICH: How do you think I feel? My lover leaves me;

CHET: (Pg 18) If you don’t mind, I’ll sleep on the couch tonight. You’ve been sweating a lot. (Pg 19) I know I’m being paranoid. (Rich reaches out to Chet) (Pg 20) Don’t touch me!

RICH: (Pg 22) My family won’t let me near them;

BROTHER: (Pg 18) I’m not in the habit of kissing my brother. I touched him on the back when I arrived and when I left. (Pg 19) Christ, I didn’t even use the bathroom.

RICH: (Pg 22) I lose my business;

PARTNER: (Pg 18) Rich and I started [this catering] business about a year ago. But now word got out that Rich has this disease. I tried to explain: he doesn’t touch the food; I do all the cooking. But they won’t listen. I can understand what he’s going through. Myself, I’ve been wrestling with cancer for a while.

RICH: (Pg 22) I can’t pay my rent. How do you think I feel?

SAUL: You’ll stay here with me. You have nowhere to go. You’ve got to stay with me. (Pause) You were kidding about picking up people.

RICH: (PG 31) Just until I feel better. . . (Pg 32) One thing. I’m embarrassed. I’m just about broke. The doctors. Tests.

SAUL: We’ll get by. You’ll see.

RICH: I’ll keep track of every cent you spend on me. You’ll get it all back when I can work. I swear. . . . Saul, I’m frightened. (Saul takes him in his arms)

SAUL: We’ll be okay. We’ll be okay.

*********** CUT TO AIDS SUPPORT GROUP (PWA=Person with AIDS) **********

PWA: (Pg 37-38) I was part of a team trying to teach robots how to use language. (He moves and talks like a robot) “I’m Harris, your android model 3135X. I can vacuum the floors, cook cheeseburgers, play the piano.” It’s much harder to teach robots to understand. (Instructing a backward robot) Joke?

ROBOT: Noun: a clash of values or levels of reality, producing laughter. Example: Have you heard about the disease attacking Jewish American princesses? It’s called MAIDS. You die if you don’t get it. Ha. Ha.

PWA: My co-workers asked me to leave. They were afraid of contracting AIDS through the air, or by my looking at them. You see, they are scientists. My last act before I left was programming one final robot. (He behaves like a robot again) “Good morning. This is Jack – (He suddenly becomes a flamboyantly gay robot) but you can call me Jackie – your fabulous new android model 1069. If you wish to use me – and I love being used – press one of those cunning little buttons on my pecs. Go on, press one – (He switches from a campy tone to an almost angry, accusatory one) or are you afraid of me too?” That was my stab at immortality.

RICH: I’m not sure I have it anymore. I feel like somehow I’m being disloyal to the group. (but) I’m getting better, I know it. I just have these lumps, which for some reason won’t go away. I feel great. I feel the disease disappearing in me. Only a tiny percentage of those with the swollen glands come down with the rest. If I really thought that I was coming down with it . . . we all have options. . . .

TRANSITION But Rich was not getting better. The disease progressed rapidly and soon, Saul was visiting Rich in the hospital as they tried desperately to combat the symptoms ravaging his body. Rich began to contemplate his options.

RICH: (Pg 47) Saul, I want you to do something for me. Will you do something for me? Now listen. I want you to go out of here and go to the doctor and tell him you aren’t sleeping so hot

SAUL: I’m sleeping okay.

RICH: Sh! Now listen: you tell him you want something to make you sleep and Valium doesn’t work on you, but a friend once gave you some Seconal –

SAUL: No! I won’t do it!

RICH: (Pressuring Saul relentlessly) I tried hoarding the pills here, but every night the nurse stays to watch me swallow them down.

SAUL: I can’t do that. I won’t listen.

RICH: If you love me, you’ll help me. I have something that’s eating me up. I don’t want to go on. I’m scared to go on.

SAUL: Don’t do this to me! I can’t handle it. . . I swear, don’t do this –

RICH: Don’t you see, it’s the only way. Just get the pills. Just have them around. You’ll get used to the idea. And when the lesions spread above my neck so that I don’t look the same, you’ll want me to have them. (Pg 52) What’ so hot about living when you’re covered with lesions and you’re coming down with a new infection every day? . . . . If it gets too bad, I want to be able to quietly disappear.

SAUL: I won’t argue the logic of it. I can’t do what you want me do.

RICH: I just want them around. You keep them for me – just in case.

SAUL: I won’t

RICH: Then I’ll get them myself. (Tries to get up, but is shaky) (Pg 53) Where’re my clothes? (Takes a few steps)

SAUL: Get back in bed! (Tries to help steady Rich)

RICH: I want to get out of here! (Fighting Saul) This place is a death machine! (He collapses on the floor)

SAUL: (sits beside him) You idiot . . . I want you to understand something. It’s important. Listen. (Pg 54) Don’t you see, I just don’t have the right to take your life. Maybe I’m being selfish, but I want you here. (Pg 52) Let me help you live!

RICH: My future isn’t exactly promising. (Pg 48-49) I have Kaposi’s sarcoma, a hitherto rare form of skin cancer. It’s spreading. I have just begun chemotherapy. It nauseates me. I expect my hair will fall out. I also have a fungal infection of the throat called candidiasis, or thrush. My life expectancy is . . . I have a greater chance of winning the lottery.

SAUL: (Pg 54) I’ll take you as is.

RICH: But what happens when it gets worse? It’s gonna get worse.

SAUL: I’ll be here for you no matter what happens. I promise.

RICH: Shit. You’re so goddamned noble.

SAUL: How do you want me to be?

RICH: I can’t afford to be noble. The only thing holding me together is rage. It’s not fair! Why me?

SAUL: Why not you? Maybe it’s me next. No one knows.

RICH: I reserve the right to put an end to all this shit.

SAUL: All right, but if you kill yourself they won’t bury you in hallowed ground and you’ll got to hell with all us Jews.

RICH: I bet they have a separate AIDS section in the cemetery so I don’t infect the other corpses. (Beat. Then suddenly he speaks fiercely) Do you promise to stick with me no matter what happens?

SAUL: I do.

RICH: Do you? (He searches Saul’s face for the answer) I need you. (Long silence. Rich exits scene as Hospice worker steps forward to address the audience) **********

HOSPICE WORKER: (Pg 56-57) I have a new AIDS patient, Richard. He still has a lot of denial about his condition. Which is normal. I think most of us would go crazy if we had to face our own deaths squarely. Rich will be out of the hospital again in a week or so. For a while. He’s a fighter . . . The angry phase is just about over and the bargaining phase is beginning. If he behaves like a good little boy, God will do what Rich tells Him to do . . . I certainly hope that God does.

CLOSING In the US today; research, education and treatment options have converted AIDS from a certain death sentence to a condition that can be managed. According to the Kaiser Family Foundation . . . over 1.2 million people in the US today are LIVING with HIV/AIDS. We have a long way to go . . . Minority populations and rural areas of the US are still more profoundly affected than the rest of the county. But progress is being made. The panic of the 1980’s has ended and today, people are being more readily accepted AS IS.
```

---

## IC-0312: Assassins

- Title: Assassins
- Author (byline): Stephen Sondheim and John Weidman
- Work: Not specified
- Publisher: Theatre Communications Group
- Publication date as stated: Sept 1991
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BOOTH, HEROLD, VOICE FROM OUTSIDE BARN, RADIO ANNOUNCER, OSWALD
- Teaser before the introduction: Yes
- Spoken words (computed): 1926
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephen Sondheim and John Weidman
ISBN: 978-1559360388
Publisher: Theatre Communications Group
Date (Month/Year): Sept 1991
```

### Introduction (context only: never use it for content warnings)

```text
To paraphrase the words of author Blake Crouch: What if time is an illusion, a construct made of human memory? What if there’s no such thing as the past, the present or the future? What if It’s all happening now? What if John Wilkes Booth could come face to face with Lee Harvey Oswald, two men forever tied to the assassinations of American presidents. Booth, full of self-righteous conviction:(as Booth) Sic semper tyrannis! And Oswald, who many Americans still
```

### Performance text (classify this)

```text
(Pg 15) A tobacco barn in rural Virginia – middle of the night. Booth sits huddled on the floor, drinking from a brandy bottle and reading through a pile of newspapers.

BOOTH: (Pg 17-19) Damn! (takes a tattered diary out of his pocket and starts to write. The door bangs open and *David Herold rushes in)

HEROLD: They're coming! They'll be here any minute! (begins frantically gathering their things. Booth throws down his pen; his hand is trembling)

BOOTH: I need your help. I've got to write this and I can't hold the pen!

HEROLD: Johnny, they've found us! We've got to get out of here!

BOOTH: Not till I finish this. Have you seen these papers?! Do you know what they're calling me?! A common cutthroat! A hired assassin! This one says I'm mad!

HEROLD: We must have been mad to think we could kill the President and get away with it!

BOOTH: We did get away with it! He was a bloody tyrant and we brought him down! And I will not have history think I did it for a bag of gold or in some kind of rabid fit!

HEROLD: Johnny, we have to go --

BOOTH: No! I have to make my case. Take it down. (Booth holds out the diary and the pen and dictates as Herold writes) An indictment. Of the former President of the United States, Abraham Lincoln, who is herein charged with the following High Crimes and Misdemeanors- One: That you did ruthlessly provoke a war between the States which cost some six hundred thousand of my countrymen their lives. Two: That you did silence your critics in the North by hurling them into prison without benefit of charge or trial. Three-

VOICE FROM OUTSIDE BARN: Booth! I have fifty soldiers out here, Booth! Give yourselves up or we'll set fire to the barn!

HEROLD: Don't shoot! I'm coming out! (throws down the diary and rushes out the door)

BOOTH: No! (to audience) I have given up my life for one act, you understand? Do not let history rob me of its meaning. Pass on the truth! Please . . . (to soldiers outside the barn)

Hunt me down, smear my name, say I did it for the fame . . . What I did was kill the man who killed my country!

believe did not act alone:(as Oswald) “My definition of democracy: The right to be in a minority and not be suppressed.” What would Booth say to Oswald in the minutes leading up to . . . (voice of radio announcer) Breaking News: Shots fired from the Texas School Book Depository. (normal voice) Is history a twisted game of chance or one inevitable destiny where those who feel abandoned and disenfranchised are no longer bound to the compacts of civilized society – they simply find a gun. Assassins by Stephen Sondheim and John Weidman

(Pg 90 – 95) A storeroom on the sixth floor of the Texas School Book Depository in Dallas, Texas. Lee Harvey Oswald sits on a carton reading a handwritten note. On the floor beside him are a lunch pail and a long package wrapped in a blanket. An announcer comes on the radio

RADIO ANNOUNCER: That was the Blue Ridge Boys and "Heartache Serenade." And now we take you live to KTEX reporter Harry- Oswald turns off the radio as he re-reads the note. He opens the lunch pail, takes out a gun and puts it to his head. Whistling off stage. Oswald spins around. John Wilkes Booth steps onstage.

BOOTH: Oh! I'm sorry. I was just browsing. Please, carry on . . . (notices the gun. Oswald shoves it back in the lunch pail. Booth indicates a wall clock) Is that the right time? Yes? (taking out a pocket watch) I don't know what's the matter with this thing. Excuse me for a moment.

(crosses to the radio and turns it on)

RADIO ANNOUNCER: -- speaking to you from Love Field, where the President's plane has just touched down and is taxiing toward us. We understand the President intends to speak briefly at the airport before proceeding into Dallas, where- (Oswald turns it off )

BOOTH: (picks up the note, reads) Dearest Marina. Today I end my life so that your life can begin. Last night you said that I oppressed you . . .

OSWALD: (Oswald snatches the note) F*** you.

BOOTH: We seem to have gotten off on the wrong foot here. (Oswald grabs lunch pail) You're not going, are you? (Oswald heads for the door) Don't leave now. Come on, I didn't mean to . . . Alik. (Oswald stops)

OSWALD: What did you call me?

BOOTH: Alik. You used to like that nickname. Back in Minsk. Marina said Lee sounded Chinese, so she called you Alik. Of course I don't have to call you Alik. I just thought . . .

OSWALD: How do you know what Marina called me?

BOOTH: I know lots about you, Lee. Let's see. . . (rattling it off like a resume) Born, New Orleans, October 18, 1939. Father, Robert, died before your birth. Crazy mother, Marguerite. Dropped out of school at seventeen. Joined the Marines. Court-martialed twice. Defected to the Soviet Union, October, 1959. Defected back, June, 1962. Married, Marina Nikolaevna. Two children, June and Rachel. Current employment, stock boy, Texas School Book Depository, Dallas, Texas . . . Oh. And this morning, depressed over your estrangement from a wife who views you as a dismal and pathetic failure, you rose before dawn, kissed your sleeping children, put your last hundred dollars and your wedding ring into a cup which Marina's mother gave you for a wedding present, and came here to kill yourself . . .

OSWALD: Who are you?

BOOTH: I'm your friend, Lee.

OSWALD: I don't have any friends. (beat) Show me your badge.

BOOTH: My what?

OSWALD: You bastards think you're so smart. I know my rights. You try to interrogate me at my place of business I can sue you for harassment.

BOOTH: Ah! You think I'm with the FBI!

OSWALD: I have a right to see your badge.

BOOTH: (opens his coat, holds out his arms) Search me, Lee. You think I've got a badge. Come on, search me. (Oswald starts to frisk him. Booth grins) The FBI. You really love those morons, don't you? Hell, why wouldn't you? No one else cares if you live or die, those guys can't get enough of you. "How was your day, Lee? Sell any secrets to the Soviets? Sabotage any defense plants? Kick off your shoes and tell us all about it!"

OSWALD: (shoving him away) F*** you, whoever you are!

BOOTH: (smiles) I'm sorry, Lee. It's just so sad . . . I mean, it's all you ever wanted, isn't it? Someone who wants to hear about your day. Someone – anyone -- Your mother. Mother Russia. The Marines. Your wife Marina . . . (shakes his head) Attention must be paid.

OSWALD: What's that mean?

BOOTH: It's from a play. About a salesman. A man very much like you, Lee. independent, proud, a decent man who tries and tries but never gets a break. So, he does something dumb. When he realizes his whole life has been a failure built on lies, he kills himself. And when he's dead, his wife stands at his grave and says attention must be paid. She has to beg the world to pay attention to this poor, misguided nobody . . . I'm an actor, Lee; a good one. But Willy Loman is a part that I could never play. And I don't think that you should play it either.

OSWALD: (beat) I don't know what you're talking about.

BOOTH: What do you want, Lee?

OSWALD: You know so much, why don't you tell me?

BOOTH: You want what everybody wants. To be appreciated. To be valued. You want someone to love you, Lee. Right? . . . Isn't that it? . . . Lee?

OSWALD: Yes.

BOOTH: [Well], forget it. It's never going to happen. It's a fantasy. You've got to give it up.

OSWALD: I'm going to kill myself! Don't you think I've given it up?!

BOOTH: No. I think you're going to kill yourself because you think that's how to get it. "When I'm dead, then they'll be sorry! When I'm dead they'll know how much they loved me!" When you close your eyes you probably see the funeral, don't you, Lee? A gentle rain is falling. Everybody has umbrellas-

OSWALD: Shut up!

BOOTH: There's Marina, weeping quietly. Your sobbing children clutching at her skirt. Your mom, your dad. Every boss who ever fired you . . . I'm sorry, Lee. It's just so childish. It's so dumb.

OSWALD: You think it's dumb?! If I shouldn't kill myself what should I do?! Go home?! Beg her to take me back?! Plead with her?! Beat her up?!

BOOTH: You tried all that. It doesn't work.

OSWALD: I know it doesn't work! So tell me what I should do!

BOOTH: You should kill the President of the United States.

OSWALD: What?

BOOTH: He's coming into town to make a speech. His plane landed at the airport 15 minutes ago. His motorcade is going to go right past this window. When it does, you shoot him.

OSWALD: You're nuts. I didn't come here to shoot the President.

BOOTH: He didn't come here to get shot. . . All your life you've been a victim, Lee. A victim of indifference and neglect. Of your mother's scorn, your wife's contempt, of Soviet stupidity, American injustice. You've finally had enough, so how are you planning to get even?

OSWALD: I'm not a murderer.

BOOTH: Who said you were?

OSWALD: You just said I should kill the President . . .

BOOTH: Lee, when you kill a President, it isn't murder. Murder is a tawdry little crime; it's born of greed, or lust, or liquor. Adulterers and shopkeepers get murdered. But when a President gets killed, when Julius Caesar got killed . . . he was assassinated. And the man who did it

(lets the sentence hang, unfinished)

OSWALD: Brutus.

BOOTH: Ah! You know his name. Brutus assassinated Caesar 2000 years ago, and here's a high school drop-out with a dollar twenty-five an hour job in Dallas, Texas who knows who he was. And they say fame is fleeting . . . (smiles; Oswald stares at him. beat)

OSWALD: This is stupid. Up here on the sixth floor, what would I do? Throw schoolbooks at him?

BOOTH: What's in the package that you brought to work? (indicating package wrapped in blanket) What's in it?

OSWALD: Curtain rods.

BOOTH: (picking up the package) You sure?

OSWALD: Sure I'm sure. Marina wanted me to take them to the . . . (Booth tosses the package to Oswald; Oswald catches it, looks surprised. He folds back the blanket, revealing a high-powered rifle)

BOOTH: That's a Mannlicher-Carcano. 6.5 millimeter. Stopping range, nine hundred yards. The sight's already been adjusted.

OSWALD: Who are you?

BOOTH: My name is John Wilkes Booth.

OSWALD: John Wilkes Booth shot Abraham Lincoln.

BOOTH: (quietly, smiling) Attention has been paid . . . All your life you've wanted to be part of something, Lee. You're finally going to get your wish. (Oswald drops the rifle and turns to leave, Booth blocks his exit) (Pg 97) OK, OK . . . Lee, I'm sorry. I know things are happening kind of fast here. But you can't leave now. You have a responsibility here, Lee.

OSWALD: To who? To you? I'm responsible to me and no one else!

BOOTH: Not anymore, Lee. Fifty years from now they'll still be arguing about the grassy knoll, the mafia, some Cuban crouched behind a stockade fence, but right here, right now -- this is the real conspiracy. And you're a part of it.

OSWALD: Get out of my way.

BOOTH: (holding his ground) You have to do this. Now. You won't get another chance.

OSWALD: So what? I'll do something else. I'll shoot my wife. I'll shoot my kids. I won't shoot anyone! Who cares?!

BOOTH: (Exploding) I care, you stupid fool! Sorry. I'm sorry . . . (Pg 98) Take a look, Lee. (indicating scene outside) You know what that is? That's America. The Land Where Any Kid Can Grow Up to Be President. But in here (taps Lee’s chest), this is America, too. . . "The mass of men lead lives of quiet desperation." An American said that. And he was right. But let me tell you something. There are no lives of quiet desperation here. Desperation, yes.

But quiet? Not today. Today we're going to make a joyful noise. You're the one that's going to sum it all up and blow it all wide open. Why, after you . . . (pauses) (Pg 99) I've seen the future, Lee. And you are it. (snaps his fingers; the radio comes on)

RADIO ANNOUNCER: -- and now the motorcade is turning into Elm Street. There's someone holding up a banner, "All the Way with JFK." The President is smiling and waving as his car heads for Dealy Plaza where it will swing past the Texas Book Depository - (Booth snaps his fingers again; the radio goes off. He opens the window, picks up the gun and holds it out)

OSWALD: People will hate me.

BOOTH: They'll hate you with a passion, Lee. Imagine people having passionate feelings about Lee Harvey Oswald . . .

OSWALD: (reaches for the gun, hesitates, then drops his hand)

BOOTH: (Pg 101) All you have to do is move your little finger -- you can close the New York Stock Exchange. You have the power of Pandora's Box, Lee. Open it . . . (holds out the gun. Oswald takes it.) I envy you . . . (Oswald turns and crouches at the window) (Pg 102) All you have to do is squeeze your finger. Squeeze your finger . . . You can change the wor -- Oswald fires. Booth exits. Oswald turns. Where did he go? Oswals lurches to his feet, grabs his lunch pail and exits. A beat, then Booth returns. He picks up Oswald's suicide note, takes matches from his pocket and burns it.)
```

---

## IC-0313: At a Loss

- Title: At a Loss
- Author (byline): Dan Savage
- Work: American Savage: Insights, Slights, and Fights on Faith, Sex, Love, and Politics - Sections of "At A Loss" first appeared as “Our Man of Perpetual Sorrow” on the radio show “This American Life” May 1, 2009.
- Publisher: Penguin
- Publication date as stated: 2013
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1738
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dan Savage
Book: American Savage: Insights, Slights, and Fights on Faith, Sex, Love, and Politics -
Sections of "At A Loss" first appeared as “Our Man of Perpetual Sorrow” on the radio show
“This American Life” May 1, 2009.
ISBN: 978-1101624227
Publisher: Penguin
Date (Month/Year): 2013
```

### Introduction (context only: never use it for content warnings)

```text
At a Loss by Dan Savage.
```

### Performance text (classify this)

```text
The strangest thing about returning to the scene of the crime is that so many involve somebody returning to a place he really doesn't want to go. Someplace that he dislikes, or disagrees with, or wished he'd never been in the first place. But then the person finds that he can't help himself, he goes back. The crime scene in this story is a Catholic church. And yes, I went to Catholic grade schools. And yes, I was an altar boy. But no, the crime is not what you're assuming. No Catholic school children were harmed during the production of this story. So you can relax.

I am no longer a practicing Catholic. If I had to apply a religious label to myself, it would be “agnostatheist, an awkward hybrid of agnostic and atheist. I don’t believe in a higher power, but I do cross myself on airplanes. I once blew up at a friend who thought he was being funny when he inverted one of the crucifixes in my “ironic” collection of Catholic kitsch. And when I take the Lord's name in vain - when I mutter “Jesus Christ” through clenched teeth as my lead-footed husband passes someone going ninety miles an hour -- I am seeking the protection of a higher power.

But I go right back to not believing once my plane safely lands or once Jesus or Joseph Smith or Xenu safely delivers us back to the right-hand lane. Which makes me a hypocrite and an ingrate, I suppose, but not quite an atheist or a believer. Not quite.

I wasn’t supposed to turn out this way. I went to the same Catholic grade school my mother and grandmother did. I was baptized as an infant; I had my first communion at age seven; I was confirmed at age thirteen.

But even at age seven, I was having trouble reconciling this “loving father in heaven” with this “eternal damnation” thing the nuns were constantly threatening us with. But the fatal blow was the realization that I was gay. This realization came at roughly the same time I entered a Catholic high school for boys who were thinking about becoming priests. It was a bit like realizing you're an alcoholic on your first day working at the Budweiser bottling plant.

Despite all those years of Catholic schooling, my first reaction to the realization that I was gay wasn’t, “Looks like I’m going to find out what that eternal damnation thing is all about.” Instead I thought, “What the church says about homosexuality – that can’t be right. They must be wrong.” This intuitive sense that the Church was wrong about homosexuality - - this unshakable conviction that the Church was wrong about me – led me to wonder what else the Church might be wrong about. Virgin births, maybe? Resurrection? Masturbation? It didn’t take long to arrive at the biggest doubt of all: The existence of God.

I transferred to a public high school and stopped going to church – except for the odd family wedding, baptism or funeral. (And they are all odd, aren’t they?) For most of my adult live I was likelier to walk into a Planned Parenthood clinic for a Pap smear than to walk into a church.

Then my mother died.

A virus can lay dormant in your body for so long that you can forget you were ever infected. Then something happens that weakens your immune system and the virus seizes its opportunity. For more than two decades the Catholicism I'd contracted at Saint Ignatius had lain dormant, manifesting itself only on airplanes and in passing lanes. But the immunity I'd long enjoyed was weakened by my mother's death. Because after that sunny, awful day in Tucson, Arizona, when my mother’s life ended, I started slipping into Catholic churches. Not for weddings or funerals, but on totally random days of non-holy, non-obligation. Tuesday afternoons, Friday mornings. And I wasn’t just going to church. I was going out of my way to go to church.

Saint James Cathedral in downtown Seattle looks like a Catholic church should – Acres of stained glass, rows of marble columns, crowds of plaster saints. Saint James is open for “private contemplation “ several days a week. The church was usually empty, aside from one or two volunteers straightening up the hymnals and the offering envelopes in the backs of the pews. I think they were really there to keep an eye on the homeless people that sometimes come in to get out of the rain. Every once in a while a priest would hurry through, taking care to avoid making eye contact with me or any of the other bums.

When my mother used to call with bad news-- a relative I hadn't seen in years diagnosed with cancer, an old friend with a desperately ill grandchild-- she would always say, "I know you don't pray, Daniel. Just keep them in your thoughts." My mom knew that thoughts were the best I could do. And for months after my mother’s death, sitting in the pews at Saint James Cathedral, I stared at a marble statue of the Virgin Mother, trying to keep my mother in my thoughts.

By her own estimation my mother was a good Catholic. She believed that Jesus was her savior and that He died for her sins; she believed in the Resurrection, the Virgin Birth, The Trinity, the Sacraments. My mother also believed that sex was sacred, and that people, particularly people with children, should be married. To each other. But she didn't believe that being a good Catholic meant blind obedience. You could say that my mother was a good American Catholic. She believed that women should be priests. And that priests, male or female, should be allowed to marry. And after four pregnancies in four years, my mother concluded that birth control was not a sin.

My mother prayed that the leaders of her church would come around during her lifetime. Unfortunately, the Church, under the last two popes, moved further away from her. Whenever the current pope, “Benny”, as she called him, or the previous pope, “JP2”, condemned birth control, attacked gay people, or insisted that women could never be ordained as priests, my mother would call me, sigh audibly, and say, “It's like they're trying to make Lutherans of us all.”

But she refused to leave the church. It was her church, too, she insisted, just as much as it was Benny's, or JP2's. The little voice in her head said the same thing the little voice in mine did: “That can't be right, they must be wrong.” But that voice, a voice that destroyed my faith, somehow strengthened hers. [She] took it hard when I told her I was gay. Her first impulse was to call a priest. Father Tom, whose last name I won’t disclose for reasons that will become clear in a moment, rushed over. Sitting on the front porch, my mother broke down in tears and told Father Tom why she was so upset: “Danny says he’s gay.”

Father Tom put his hand on my mother’s knee and said, “So am I.”

My mother came around on the my-son-is-gay issue pretty fast. And she came out swinging. A rainbow bumper sticker on her car, a PFLAG membership, and an ultimatum delivered to the entire extended family: I was still her son; and anyone who had a problem with me had a much bigger problem with her.

The Catholic Church still has a problem with me.

One of the cards in the back of the pews at Saint James, tucked in with the hymnals, is addressed to non-practicing Catholics. "WELCOME BACK" it reads in large letters across the top.

Are you a Catholic who's been away from the church?

Welcome back classes are designed to help you return to the

sacraments and regular church attendance. A return to the sacraments. I sometimes fantasize about “returning” to the sacraments, particularly the sacrament of confession. “Forgive me father, for I have sinned. It's been twenty-nine years since my last confession. I hope you packed a lunch.”

I want there to be heaven. And I want my mother to be looking down on me. Though, and I say this both as a gay man and a professional sex advice columnist, not all the time. There are things a mother has a right not to know – and I did my best to keep those things from her while she was alive. My mother’s death, somehow and unexpectedly, drew me back to church. I was tempted. I am tempted. I wouldn't have wasted so much time sitting in Saint James in the months after my mother’s death if I weren’t. My husband would not have found a "WELCOME BACK" card in the back pocket of my jeans if I weren’t tempted.

But when I feel tempted, when I feel like, maybe, I could go through the motions, maybe I could return to the sacraments, maybe I could take what comfort I could from the Church and its rituals, the pope goes to Africa and says that condoms spread AIDS, or an archbishop in Brazil excommunicates a Catholic mother for getting her nine-year-old daughter a life-saving abortion, but not the Catholic man who raped and impregnated that woman’s nine-year-old daughter.

Or I contemplate how the church views me and the two people I love most in the world, my husband of eighteen years and our fifteen-year-old son, and I think, no, I can't even go through the motions.

The Church doesn’t want me back – not as I am. Every other week there’s a story in the news about a Catholic grade school expelling a child who has gay parents. When it comes to homosexuality, church leaders are growing ever more, er, rigid. The Church condemns homosexuality as “intrinsically and gravely disordered.” So long as we insist on coming out, so long as we insist on living and loving openly, our “sin” is visible to the naked eye. And Church leaders can’t see past our homosexuality; they can barely see our humanity.

[And yet I still] want there to be heaven. And I want my mother to be looking down on me. [And I still] sit in the pews at Saint James Cathedral, staring at a marble statue of the Virgin Mother, trying to keep my mother in my thoughts.
```

---

## IC-0314: Beauty Mark

- Title: Beauty Mark
- Author (byline): Craig Shafer
- Work: Fast Horse Plays, Round 6, Pg 33-39
- Publisher: Create Space Independent Publishing
- Publication date as stated: May 2015
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: THE BOY
- Teaser before the introduction: Yes
- Spoken words (computed): 1625
- Already set (do not supply): none

### Source block (context only)

```text
Author: Craig Shafer
Book: Fast Horse Plays, Round 6, Pg 33-39
ISBN: 978-1512244120
Publisher: Create Space Independent Publishing
Date (Month/Year): May 2015
```

### Introduction (context only: never use it for content warnings)

```text
Cassidy Creech was only 13 when he considered suicide. He feared a world where no one would want anything to do with him – even his church-going parents, whom he worried wouldn’t accept him for being gay. This feeling was already a reality in class, where he was relentlessly bullied at his small-town school despite not having gone public with his sexuality.* Six out of 10 students reported feeling unsafe and ostracized in school because of their sexual orientation, according to a 2019 study from the Gay, Lesbian and Straight Education Network. And now with an unprecedented number of anti-LGBTQ policies introduced and implemented across our nation, the status of LGBTQ students is even more perilous.

No one should be afraid to go to school in America . . . But they are.

Beauty Mark by Craig Shafer
```

### Performance text (classify this)

```text
The Boy is an unnamed speaker somewhere between sixteen and almost adulthood.

THE BOY: (Pg 33-39) When I was getting ready, I went through all the things she could possibly say when I told her. No, seriously -- I did. Best case scenario included things like, "I already knew, but thanks for telling me," and "That explains why you're so fabulous." Worse case scenario include disowning, verbal abuse, beheading -- I'm kidding.

I mean, I thought maybe it would just fall somewhere in the middle, you know? Something like, "I really wanted grandkids," but I already had a response to that. "No you didn't. Who are you kidding? You hate kids."

So, I told her. I did. As my sixteenth birthday present to myself. .. "Mom, I'm gay." And umm, she just sat there. So, of course, I thought about all the great advice I'd gotten from whenyoufirstcomeouttoyourparents.com and they said that sometimes it takes a little while to process and that "gently reinforcing" the message can be very helpful. So I did. "Mom, I'm gay. Like, completely gay."

And I leaned forward like to hug her or whatever and she just pulled back, wrapping her arms around herself - like she might catch it or something. And I tried to make a joke, but she didn't laugh at all. And, umm, out of all the responses I'd gone through, this was the one that I hadn't thought about. Nothing. Just nothing. She looked at me for the longest time and then she just walked away.

THE BOY: So, here's the thing, the secret they don't really tell you. Not a whole lot changes after you "come out." I mean, I don't know, maybe I was expecting like exploding rainbow starbursts to suddenly surround me or, a really hot guy on a unicorn to show up on my doorstep and take me out for pizza. But those things don't happen, and life just keeps being boring and doesn't change a whole lot at all.

I kept getting this telemarketer call on my phone, from, like, New York, and I know this is dumb, but I fantasized that it was Ellen -- you know, Ellen, from, like Ellen the show? inviting me to appear on her show, right? Because she brings kids on her show all the time that are special. And so, umm, I would go on the show and I would kiss Ellen dramatically on both cheeks and then announce, "Ellen, I'm gay." And she would smile, of course, and then ask me some questions. "Are you famous?" No. "Do you sing?" No. "Play any unique or unusual musical instruments?" Sorry, no. "Mathematical genius?" No. "Reaching here, but born with extra fingers on both hands?" Just ten.

So, moral of the story? No. Not special. Just gay. And just living in this hellhole out in the middle of nowhere without very many friends, no boyfriend in sight, not much of anything, you know?

Okay, but here's the thing. I came out to my mom, right? raging success, and then I came out at school, with the help of whenyoufirstcomeouttoeveryoneatschool.com of course, and, umm, it's not that I became, well, popular, but, mum, I guess I became, I dunno, "notorious?" Like, people were talking about me, and I thought, well, at least people are noticing me, right? It's better to be the "gay kid" then just nothing at all, right? Right?

So, I decided to start a GSA at school -- that's a gay-straight alliance, if you don't know -- at school. Basically it's where gay kids and straight kids come together and they talk about gay stuff and straight stuff and, mum, well, they, I dunno, they "ally." I don't really know they're supposed to do, but it seemed like a good idea, okay? So, I wore a snappy bow tie to the first meeting, but, unfortunately, the turnout was somewhat limited. The turnout was two. Myself and the 70-year-old Home-Ec teacher who was forced to be the advisor because she wasn't advisor-ing any other clubs. And she umm, offered me home-baked cookies -- do I look like I need cookies? I need a boyfriend! and umm, she asked me if maybe it was "just a phase?"

And so I asked her if being a b**** was "just a phase" for her, and mum, the principal told me that that was probably pretty inappropriate and that Mrs. Nightengale- Marbletooth wasn't going to be the advisor for the GSA anymore. And I told him that the GSA only had one member anyway, and to just drop it.

Okay, but, anyway, here's the thing: being "notorious" means that people kind of start talking to you. They do. And, I mean, some of the time I wasn't sure if it was the good kind of talking, or if they were just talking to me because I was, like, the freak of the week or whatever, but I mean . . . I wanted to be noticed, I guess. I just didn't want to be nothing anymore, you know? I mean . . . I dunno.

So, umm, I get invited to this party, right? And, I mean, it isn't just a party, it's "A PARTY” the kind that somebody like me doesn't get invited to ever, right? But I'm not going to question fate, I mean, obviously, I was just meant to go, right? And it's a few of the football players -- the Varsity football players -- and they're telling me that they're totally cool with me and whatever and that I've got to come to the party, and so, of course, I go . . . right?

And so, I get there, and I'm thinking, this is how it is to be somebody, you know? This is how it is to be a cool kid. And kids are saying, "that's him, that's the gay kid," and I'm thinking, whatever, right? It's okay. . . And so I'm drinking, just a little. . . okay, maybe more than a little, but whatever. . . and we're at this house - some rich kid's house, and a few of the guys, the bros, right? - they're all, you know, with me, and I'm thinking that this is awesome, right? And they're saying we're gonna go out to the field down from the house and I'm thinking this is really awesome, right? And so I go . . .

And it's dark and whatever and I'm stumbling around like a fool, but we're all walking together and I'm just trying to think straight -- well, not straight, but you know what I mean, but, really I'm just thinking that these guys do like me and that everything is going to be okay, and then. . . Well . . .

And then, one of them, out of nowhere, really, he hits me across the back of my head with a baseball bat and calls me a faggot.

And you know what's so weird? It felt like it took, I dunno, hours and hours to fall to the ground, you know? It musta only been a few seconds but it felt so long. And I was just thinking that it was some kind of dream or something, right? Like maybe a musical and we were all just pretending or that it was an episode of Ellen and she was gonna just pop up out of nowhere and tell everybody how special I was . . . but, umm. . . she didn't. Nobody did.

No. They were on top of me. And ripping at my clothes. And the blows just came one after another. And I think maybe I thought – wow - my body is kinda strong or maybe I'm dead. . . and umm. . . here's the thing -- I felt the blood -- my blood -- like in my eyes and my mouth, and one of the boys, he's just making this awful loud noise and at first I can't even figure out what it is, but I turn my head to look at him and then I get it. He's Woody the Woodpecker -- you know the laugh, right? And that's what he's doing. He's laughing at me.

And I hear glass breaking and that boy, Woody, he's right on top of me and he's holding a broken beer bottle and even before the glass touches my face- I know. Do you know how that feels? Not the cutting, I mean. No. But the knowing. That hurts more. Knowing that it's going to happen and there's nothing you can do. You know the weirdest thing, though? That's not what I'm gonna remember, no. What I'm gonna remember is the grass. How soft and warm and nice the grass was up against my face while those boys were on top of me. That's what I'm gonna remember. Things are funny.

Okay, so, umm. . . I know what you're thinking. You think I don't know, but I know what you're thinking. You're thinking -- what did I think was going to happen? Going with those boys to that party? Well, I didn't think anything. I just wanted something to be okay, and, I'm sorry, but everybody says "we've come so far -- gay kids are fine at school now." Well, we haven't come so far here, now, have we? We haven't come very far at all.

I didn't die though. I am invincible. Not really, but if I was a superhomo I mean, a superhero that would be kind of an awesome thing to say, you know? I'm gonna be okay. I mean, my body's gonna be okay, I guess. This? (He gestures to a large scar on his face) Well, yeah, that's not gonna go away. But, umm, Marilyn Monroe, she had a mole, right? And umm, I have this. . . it's my trade-mark -- my beauty mark, right? It's unforgettable.

Anyway, my mom, she was there when I woke up. She, well, we talked. But umm. . . yeah, it doesn't matter. She does her best, you know?
```

---

## IC-0315: Bent

- Title: Bent
- Author (byline): Martin Sherman
- Work: Not specified
- Publisher: Applause Theatre Books
- Publication date as stated: May 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: RUDY, MAX, OFFICER, HORST, CAPTAIN
- Teaser before the introduction: Yes
- Spoken words (computed): 2356
- Already set (do not supply): none

### Source block (context only)

```text
Author: Martin Sherman
ISBN: 978-1557833365
Publisher: Applause Theatre Books
Date (Month/Year): May 1998
```

### Introduction (context only: never use it for content warnings)

```text
In Bent, Martin Sherman tells a Holocaust story that no one had ever told before – The story of the persecution of homosexuals -- the lowest of the low in the concentration camp pecking order. The wearers of the Pink Triangle. Written in 1979, the struggle of Max to accept himself, to learn to love in the most unlikely of places, still carries meaning today.

Bent by Martin Sherman

RUDY screams again as stage is set for next scene [Scream during transition to Character of Horst] MAX moves, as if to get up. [The man wearing the pink triangle (HORST) moves toward MAX. He touches him.] HORST: (Pg 42-43) Don't. [He removes his hand from MAX and looks straight ahead. The

GUARD walks through the circle of light.] Don't move. You can't help him. Silence. The

GUARD walks through the circle of light.]
```

### Performance text (classify this)

```text
CUTTING NOTES are in RED; STAGE DIRECTIONS from the PLAY are in BLUE. [RUDY and MAX crouched on the ground] A prisoner transport train. A GUARD walks through the circle of light. He carries a rifle. [RUDY and MAX watch as GUARD crosses – actors should coordinate eye moment to give the illusion there is a GUARD] Silence.

RUDY: (Pg 40-41) Where do you think they're taking us? [Silence. The other prisoners look away The GUARD walks through the circle of light. Silence.] [To the PRISONER next to him] Did you have a trial? [The PRISONER doesn't answer.]

MAX: Rudy . . . I . . . . [Silence]. RUDY and MAX look at each other. They are both terrified. RUDY starts to extend his hand, then withdraws it. A scream is heard-off, beyond the circle. [Characters respond physically to the sound] RUDY and MAX look at each other, then turn away. Silence. Max assumes the role of OFFICER and walks through the circle of light. Silence. Another scream. [Rudy responds physically to the sound] Silence. The OFFICER looks at the prisoners one by one. He stops at RUDY.]

OFFICER: Glasses. [Silence.] Give me your glasses. [RUDY hands the OFFICER his glasses. The OFFICER examines them.] Horn-rimmed. Intelligensia.

RUDY: What?

OFFICER: [Smiles.] Stand up. [Pulls RUDY up.] Step on your glasses. [RUDY stands-petrified.] Step on them. [RUDY steps on the glasses.] Take him.

RUDY: Max! [RUDY looks at MAX. The OFFICER pushes RUDY off-out of the circle. The OFFICER smiles.]

OFFICER: Glasses. [He kicks the glasses away]. Exits . . . MAX resumes his original role MAX stares ahead. A scream is heard-off, beyond the circle. RUDY'S scream. MAX stiffens. Silence. RUDY screams again.

MAX: This isn't happening. Where are they taking us?

HORST: It's happening. Dachau. I've been through transport before. They took me to Cologne for a propaganda film. Pink triangle in good health. Now it's back to Dachau.

MAX: Pink triangle? What's that?

HORST: Queer. If you're queer, that's what you wear. If you're a Jew, a yellow star. Political-a red triangle. Criminal-green. Pink's the lowest. [He looks straight ahead].

MAX: This isn't happening. [Silence.] This can't be happening. [Silence.]

HORST: Listen to me. If you survive the train, you stand a chance. Here's where they break you. You can do nothing for your friend. Nothing. If you try to help him, they will kill you. If you try to care for his wounds, they will kill you. If you even see -- see what they do to him, hear -- hear what they do to him -- they will kill you. If you want to stay alive, he cannot exist. *****SCENE: At the prisoner camp, Dachau***** [A tight little corner at the end of the barracks. HORST crawls in and sits huddled with his bowl. He drinks the soup. MAX enters, crawling in next to HORST. He carries a bowl. He wears the prison uniform. On it is a yellow star.]

MAX: (Pg 50-57) Hi. [HORST looks at him; says nothing; MAX holds up his bowl.] Here.

HORST: Leave me alone.

MAX: I got extra. Some vegetables. Here. [Drops vegetables from his bowl into HORSTS]

HORST: Thanks. [They eat in silence. HORST stares at MAX'S uniform.] Yellow star? Jew?

MAX: Oh. Yeah.

HORST: I wouldn't have figured it. [Silence.] I'm sorry about your friend.

MAX: Who?

HORST: Your friend.

MAX: Oh. [Silence.] [Points to HORST'S pink triangle.] How'd you get the pink?

HORST: I signed a petition. . . for Magnus Hirschfeld.

MAX: Oh yeah. I remember him. Berlin. He wanted to. . .

HORST: Make queers legal. Looked like he would, too, for a while. It was quite a movement. Then the Nazis came in. Well. I was a nurse. They said a queer couldn't be a nurse. Suppose I had to touch a patient's penis! God forbid. They said rather than be a nurse, I should be a prisoner. A more suitable occupation. That's how I got my pink triangle. How'd you get the yellow star?

MAX: I'm Jewish.

HORST: You're not Jewish, you're a queer. [Silence.]

MAX: I didn't want one. You told me it was the lowest. So I didn't want one. I worked a deal.

HORST: A deal? With the Gestapo? You're full of shit. [Silence.]

MAX: I'm going to work a lot of deals. They can't keep us here forever. Sooner or later they'll release us. I'm only under protective custody, that's what they told me. I'm going to stay alive.

HORST: I don't doubt it. Thanks for the vegetables. [Starts to crawl away.]

MAX: Where are you going?

HORST: To sleep. We get up at four in the morning. I'm on stone detail.

MAX: Don't go. . . I'm not Jewish.

HORST: Then why are you wearing that?

MAX: You told me pink was the lowest.

HORST: It is, but only because the other prisoners hate us so much.

MAX: I got meat in my soup. You didn't. . . . You didn't think I'd make it, did you? Off the train?

HORST: I wasn't sure.

MAX: I'm going to stay alive. Because of you. You told me how.

HORST: Yes. [Pause.] I did. [Pause.] You should be wearing a pink triangle.

MAX: I made a deal. They said if I . . . I could prove . . .

HORST: What? [Silence.]

MAX: They took me. . . into that room. . . on the train. And they said. . . prove that you're not. . .

HORST: Prove that you're not what?

MAX: Queer.

HORST: How?

MAX: They said, if you. . . Made love.

HORST: Who was she?

MAX: Maybe . . . maybe only thirteen . . . she was dead. Just. Just dead, minutes [MAX indicates a gun at the temple] They said prove that you're. . . and I did. . . lots of them, watching. . . laughing. . . He's a bit bent, they said, he can't . . . but I did . . . I wanted . . .

HORST: To stay alive.

MAX: She was like an angel . . . to save my life . . . [Silence.] And I said, I'm not queer. And they laughed. And I said, give me a yellow star. And they said, sure, make him a Jew. He's not bent. And they laughed. But. . . I. . . got. . . my. . . star.

HORST: Yes. [Reaches out, touches MAX'S face.]

MAX: Don't do that! [Pulls away.] You mustn't do that. For your own sake. You mustn't touch me. I'm a rotten person. *****Scene: Max uses his “deals” to get Horst moved to rock detail*****

MAX: (Pg 63-65) You see those. . . You take one rock at a time. And move it over there. And then when the entire pile is over there, you take one rock at a time, and move it back.

HORST: [Looks at MAX. Silence.] And move it back? We move the rocks from there to there, and then back from there to there? Why?

MAX: Start moving. He's watching. [MAX continues to move rocks. HORST does the same. They do so in different rhythms, at times passing each other.] It's supposed to drive us crazy. It makes no sense. It serves no purpose. I figured it out. They do it to drive us crazy.

HORST: They probably know what they're doing.

MAX: But it doesn't work. I figured it out. It's the best job to have. That's why I got you here.

HORST: What? [Puts down his rock.]

MAX: Don't stop. Keep moving. [HORST picks up the rock and moves it.] A couple more things. That fence. It's electric. Don't touch it. You fry. And over there-that pit.

HORST: Oh yes. It smells awful.

MAX: Bodies. Sometimes we have to throw them in.

HORST: Oh. Well, it will break the routine. (Pg 68-71) Where do the bodies come from?

MAX: The fence. The hat trick. Sometimes a guard throws a prisoner's hat against the fence. He orders him to get the hat. If he doesn't get the hat, the guard will shoot him. If he does get the hat, he'll be electrocuted.

HORST: I'm really going to like it here. Thanks a lot.

MAX: I'm really doing you a favor.

HORST: Some favor! You just want someone to talk to so you won't go crazy. And I'm the only one who knows your secret.

MAX: What secret?

HORST: That you're a pink triangle.

MAX: No. I'm a Jew now.

HORST: You are not. It's a lie.

MAX: It's a smart lie. I thought you'd be grateful.

HORST: I'm not grateful. I liked cutting stones. This is insane. Twelve hours of this a day? I'll be nuts in a week.

MAX: You haven't figured out this camp, that's all. You don't know what's good for you. This is the best job to have.

HORST: Moving rocks back and forth for no reason. Next to a pit with dead bodies and a fence that can burn you to dust. The best job to have? [They both move their rocks. A long silence.]

MAX: I thought you'd be grateful. *****Scene: Same work detail . . . months later*****

HORST: (Pg 86) I'm going crazy. [Silence.] I'm going crazy. [Silence.] I'm going crazy. I dream about rocks. I close my eyes and I'm moving rocks. Rocks never end. Never end. [Silence.] I'm going crazy.

MAX: Think of something else.

HORST: I can't think. I've been up all night. Didn't you hear? Our barracks had to stand outside all night. We stood at attention all night long . . . Punishment.

MAX: What for?

HORST: Someone in our barracks killed himself.

MAX: A moslem?

HORST: (Pg 74) No. That's what they call a dead person who walks. You know, one of those guys who won't eat anymore, won't talk anymore, just wanders around waiting to really die. (Pg 86-93) It doesn't mean anything if a moslem kills himself, but if a person who's still a person commits suicide, well . . . it's a kind of defiance, isn't it? They hate that -- it's an act of free will.

MAX: I'm sorry.

HORST: Sure. Yellow star is sorry. [Silence.] I'm going crazy.

MAX: O.K. O.K. You're going crazy. I'm sorry. It's my fault.

HORST: What do you mean your fault?

MAX: For bringing you here. Because you make me feel so guilty. And you should. This job is the worst. I figured it wrong. I'm sorry.

HORST: You should be with us, where you belong.

MAX: No. But you shouldn't be here.

HORST: I want to be here.

MAX: Why?

HORST: Because. Because I love rocks. [Pause.] Because I love you. [Silence.] I do. I love you. When I'm not dreaming about rocks, I'm dreaming about you. For the past six weeks, I've dreamed about you. It helps me get up. It helps me make sure my bed is perfectly made so I'm not punished. It helps me eat the stinking food. It helps me put up with the constant fights in the barracks. Knowing I'll see you. At least out of the corner of my eyes. In passing. It's a reason to live. So I'm glad I'm here. [MAX is at one pile of rocks, moving them into symmetrical piles.]

HORST: What are you doing?

MAX: Arranging these neatly. We've gotten sloppy. They can beat you for it. [Silence.] Don't love me.

HORST: It's my secret. And I have a signal. No one knows it. When I rub my left eyebrow at you, like this ... [Rubs his left eyebrow.] ... it means I love you. Bet you didn't know that. I can even do it in front of the guards. No one knows. It's my secret. [Starts to cough.] It's cold.

MAX: Don't love me. I don't want anybody to love me. I can't love anybody back.

HORST: Who's asking you to?

MAX: Queers aren't meant to love. I know. They don't want us to. You know who loved me? [That boy . . . on the train. ] I don't remember his name. But I killed him. See -- queers aren't meant to love. I'll kill you too. Hate me. That's better. Hate me. Don't love me. [MAX finishes arranging the rocks. He returns to moving the rocks. Silence. HORST starts to cough again. Slips. Drops the rock and falls to the ground.]

MAX: Horst! [Puts down his rock.]

HORST: Shit. [MAX starts toward him.] Don’t move! He's watching. The guard. If you help me, they'll kill you. Get back to your rock. Do you hear me, get back! [MAX returns, picks up his rock, but stands looking at HORST; HORST is coughing] Move! [MAX moves the rock.] Don't ever help me. [Pulls himself up.] I'm up. It's O.K. [Picks up his rock.]Never notice. Never watch. I love you. But I won't help you if you fall. Don't you dare help me. We save ourselves. Do you understand? Do you?

MAX: Yes. I understand.

HORST: Promise me. Come on. Promise me. We save ourselves.

MAX: (Pg 96-97) You're losing weight. You need medicine.

HORST: It doesn't matter.

MAX: You're turning into a moslem. I'm scared. *****Scene: Same work yard ***** [MAX assumes the role of CAPTAIN as HORST resumes moving rocks.] The CAPTAIN watches HORST. He paces up and down. HORST moves the rocks. The CAPTAIN paces. HORST coughs. He catches himself and tries to stifle it.]

CAPTAIN: (Pg 112-117) Ah. [HORST stops the cough.] You. Pervert.

HORST: [Stiffens, stands still.] Yes sir?

CAPTAIN: Are you ill?

HORST: No sir.

CAPTAIN: You have a cough. I heard you cough. You're not well.

HORST: I am, sir.

CAPTAIN: Put down that rock.

HORST: Yes sir. [Puts down the rock.]

CAPTAIN: Good. Now take off your hat.[A long pause.]

HORST: My hat, sir?

CAPTAIN: Yes. Your hat. [HORST removes his hat]

CAPTAIN: Throw your hat away. [HORST flings his hat on the ground.] Not there. Pick it up.

HORST: Yes sir. [Picks up his hat.]

CAPTAIN: Throw it on the fence. The fence. [HORST starts to cough.] That's all right. We'll wait. [The cough subsides.] Are you better?

HORST: Yes sir.

CAPTAIN: Nasty cough. On the fence. Now.

HORST: On the fence. Yes sir. [HORST throws his hat on the fence. The fence sparks.]

CAPTAIN: Get your hat. [The CAPTAIN points his rifle at HORST.]

HORST: [Is silent for a moment. Turns to the CAPTAIN] Yes sir.

[HORST turns left, takes his hand and rubs his left eyebrow. He turns and stares at the CAPTAIN. The CAPTAIN waits. HORST turns toward the fence. He starts to walk very slowly to his hat. He almost reaches the fence, when, suddenly- He turns and rushes at the CAPTAIN. He screams in fury. The CAPTAIN shoots HORST. He falls, dead. Silence.] *****SCENE: Max and Horst’s dead body*****

MAX stares at HORST. Silence. MAX opens his mouth to cry out. He can't. Silence. MAX walks to HORST'S body.

MAX: (Pg 119-120) Nol [He looks up-off-at the GUARD, then back at HORST. Silence.] You don't have to worry about the rocks. I'll do yours, too. I'll move twice as many each day. I'll do yours, too. You don't have to worry about them. [Silence.] You know what? [Silence.] Horst? [Silence.] You know what? [Silence.] I think I love you. [Silence.] Shh! Don't tell anyone. I love you. [Silence.] What's wrong with that? [He starts to cry.]
```

---

## IC-0316: Betrayer, Judas Iscariot

- Title: Betrayer, Judas Iscariot
- Author (byline): Richard Exley
- Work: Witness the Passion
- Publisher: White Stone Books
- Publication date as stated: 2004
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1777
- Already set (do not supply): none

### Source block (context only)

```text
Author: Richard Exley
Book: Witness the Passion
ISBN: 159379021X
Publisher: White Stone Books
Date(Month/Year): 2004
```

### Introduction (context only: never use it for content warnings)

```text
Who knows what makes a man like Judas do what he did. Of this we can be certain, he did not follow Jesus in order to betray him. Like the other disciples he left everything-family, friends, career-to serve Him. Along the way something happened, some little thing most likely, that poisoned his soul and made him susceptible to Satan's snare.

He came to Jesus with high expectations and when his expectations were not realized his disappointment soon turned to disillusionment. His bitterness of soul caused him to make a pact with the devil. "Then Satan entered Judas, called Iscariot, one of the Twelve. And Judas went to the chief priests and the officers of the temple guard and discussed with them how he might betray Jesus.

From the mind and soul of the Betrayer, Judas Iscariot by Richard Exley.
```

### Performance text (classify this)

```text
Having delivered Jesus into the hands of the chief priests as per our agreement, I now watch as the temple guards bind his hands and prepare to lead him away. I should have a sense of triumph, or at least some feeling of accomplishment, but I don't. Instead I feel strangely empty. Not guilty, just unfulfilled.

Against my will my mind returns to an earlier time when hope was as bright as the summer sun. In those days I believed Jesus could do anything. He had a way of speaking unlike anyone I had ever heard. When he talked about the Father, or the kingdom, my heart fairly leaped within me. He made it all seem so immediate, so real. There were even moments when I could almost believe that he was the chosen One.

For all his gifts, Jesus was incredibly naive. A politically astute person would have built on his popularity and seized the moment. But not Jesus! There were several times, especially during the early months of his ministry, when the masses were determined to make him a king. What did he do? He went into hiding, disappearing for weeks at a time. We tried to reason with him, but to no avail.

With an effort I dismiss all thoughts of what might have been. It is too late for that and I will not torment myself with idle speculation now. I have made my decision, cast my lot with the elders and chief priests. Let others judge me if they will, I know I did the only sensible thing under the circumstances, difficult though it was.

A surly guard now prods Jesus with the butt of his spear and we move out. Leaving Gethsemane we enter Jerusalem. As we wind our way through the dark streets, one of the temple guards positions himself at my shoulder. "What's he really like?" he asks, nodding his head in the direction of Jesus. Being in no mood for small talk I ignore him, hoping he will go away. Unfortunately, he seems oblivious to my reticence, and after awhile he tries again. "I've heard rumors about miracles and such like," he says. "What do you know about that?"

"Little enough," I say. Though if the truth be known the miracles of Jesus are too numerous to be numbered. His disappointment is plain enough, but I am not about to get into this. The memories are still too fresh, and capable of invoking the very feelings from which I have tried so hard to distance myself. Talking about it can serve no good purpose.

There are no lanterns or torches, and an order is given to maintain absolute silence. According to the captain, it is imperative we attract no attention as we make our way toward the house of the high priest. All of this secrecy can only mean one thing-they intend to try Jesus tonight. Although secret trials are strictly forbidden by our law, it now seems obvious that this is exactly what Caiaphas has in mind. It makes sense. Who knows what might happen if the multitudes were to awaken in the morning and find Jesus in the hands of the elders and the chief priests. But, if the trial is finished before daybreak and Jesus is already in the custody of the Romans, the Sanhedrin will have little or nothing to fear.

Arriving at the house of the high priest, Jesus is immediately taken into a large semicircular room where the Sanhedrin is already in session. A movement in the dark catches my eye, and I watch as John moves toward the outer door of the courtyard. Furtively he glances over his shoulder before opening the door. A large man emerges from the shadows beyond the wall and quickly steps inside. For an instant he is framed in the light. With a start I realize that it is Simon Peter. What is he doing here? Surely he can't be crazy enough to try to rescue Jesus. Such an attempt would be ludicrous. Still, I cannot help thinking it is just the kind of thing Peter might attempt. One thing is certain, I dare not show my face while he is around.

Moving deeper into the shadows I turn my attention back to the ecclesiastical trial. In dismay I watch as our carefully laid plans seem to unravel before my eyes. Witness after witness is heard, yet the Sanhedrin can find no evidence with which to condemn Jesus. Finally Caiaphas takes matters into his own hands. Rising from his elevated seat he addresses Jesus in his most judicial manner. "I charge you under oath by the living God: Tell us if you are the Christ, the Son of God."

Instantly the atmosphere in the room changes. The weariness and frustration of the long night give way to a sudden tension. Around the room the elders and chief priests lean forward. They sense Jesus himself may provide the condemning evidence they have not been able to produce. Caiaphas remains standing, towering over Jesus, willing him to incriminate himself. Only Jesus seems unmoved by the drama of the moment. Yet he too is different, energized somehow. It is a transformation I have seen before. I saw it first when he commanded the storm to cease, and again when he raised the widow's son from the dead. Still, I have never sensed such transcendent authority, not even when he commanded Lazarus to come forth.

"Yes, it is as you say," Jesus replies, his voice clear and distinct. "But I say to all of you: In the future you will see the Son of Man sitting at the right hand of the Mighty One and coming on the clouds of heaven."

In an instant the high priest gnashes his teeth and tears his robe, nearly beside himself with self-righteous rage. "He has spoken blasphemy!" he screams. "Why do we need any more witnesses?"

With one voice the Sanhedrin answers, "He is worthy of death!" Suddenly the hatred and jealousy they have harbored these many months erupt. Rushing forward, they deposit huge wads of foul spittle full in his face. Others strike him with their fists, screaming, "Prophesy to us, Christ. Who hit you?" My reaction is different. It is not blasphemy I have heard, but prophetic revelation, and now the magnitude of what I have done hits me for the first time. It is not an impostor I have delivered into the hands of the religious authorities, but the Messiah. I have betrayed the chosen One of God!

In stunned disbelief I watch from the shadows as the guards bind Jesus and prepare to deliver him to Pontius Pilate. Although his beard is stiff with spittle and his face bruised and bleeding, there is about him sense of dignity that dwarfs his accusers.

"Wait!" I scream leaping to my feet and rushing toward the high priest. For just a moment Our eyes meet. In his there is a flicker of recognition, then he turns away in disgust. In that instant I see my condemnation written in his face. He has played me for a fool. Now that I am of no further use to him, I am of no more value than a leper in the streets, or a gentile.

"Wait!" I scream again, trying to force my way through the temple guards who block my way. Reaching inside my garment I grab the bag of silver coins and thrust it toward the priests. "Take these," I plead. "Let Jesus go. He has done nothing worthy of death." Ignoring the coins, they restrain me as Jesus is led away. When finally I am released I rush desperately from priest to priest begging, "Help me for I have sinned. I have betrayed innocent blood." It is no use. They will not hear me. My desperate pleas full on deaf ears.

Finally one of them says with a sneer, "What is that to us? That's your responsibility." His words are like a dagger plunged into my heart. Grabbing the silver coins, I hurl them at their feet before rushing into the street. Now the awful weight of my treachery descends upon me afresh and I stagger beneath the burden of my sin. It isn't just what I did-unspeakable though it was-but what I am. To my everlasting shame I discover that the deed and I are one!

I am driven to flee, to run away, but where can I go? The thing I cannot escape, the thing I cannot bear, is myself So this is hell, I think, to live forever with what I have done. Stumbling through the streets the words of Jesus return to haunt me. "The Son of Man will go just as it has been written about him. But woe to that man who betrays the Son of Man. It would be better for him if he had not been born."

I curse the day of my birth. I curse the day I heard the name of Jesus. I curse the high priest and the Roman governor. I curse my own life. In absolute despair I scream, "I am damned! I am damned!" After a long time I find myself on the side of a steep hill overlooking a deep ravine. A rope is in my hand and on one end I have fashioned a hangman's noose. In a trancelike state, I loop the other end over a branch, being careful to place it as far out as I can reach. When it is securely tied I drop the noose over my head and draw it tight around my neck. Closing my eyes I try to remember my mother's face but I cannot. Instead his eyes stare at me, not in anger, but with a wounded love. The way he looked at me when I kissed him in Gethsemane. That's what I cannot bear. Not his anger, but his love. Even now he seems to be calling to me.

I am sobbing now. Weeping like a motherless child, but it is no use. Tears cannot save me. It is too late. Too late. Regardless of what others may think, I know I did not consciously choose to become what I am. It was a subtle process and who can say what small act opened the door to the evil within? But once that door was open, it was impossible to close it again and now I must pay for what I have done.

With all my strength I scream, "I have sinned. I have betrayed the innocent blood of my Lord." Then I leap . . .
```

---

## IC-0317: Big Fish: A Novel of Mythical Proportions

- Title: Big Fish: A Novel of Mythical Proportions
- Author (byline): Daniel Wallace
- Work: Not specified
- Publisher: Penguin Publishers
- Publication date as stated: Nov 1999
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: WILLIAM, DAD, DR. BENNETT
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
WILLIAM: (My Father's Death: Take 4) One of our last car trips, near the end of my father's life as a man, we stopped by a river. After a couple of minutes my father took off his shoes and his socks and placed his feet in the clear-running water. Then he closed his eyes and smiled.

DAD: This reminds me . . . .

WILLIAM: And then he stopped and thought some more. I guessed he was thinking of some joke to tell, because he always had some joke to tell. Or he might tell me a story that would celebrate his adventurous and heroic life. Does it remind him of the duck in the hardware store? The horse in the bar? The boy who was knee-high to a grasshopper? Did it remind him of the dinosaur egg he found one day, then lost, or the country he once ruled for the better part of a week?

DAD: This reminds me of when I was a boy.

WILLIAM: I looked at this old man, my old man with his old white feet in this clear-running stream, and I thought of him suddenly, and simply, as a boy. I'd never done that before. And these images--the now and then of my father--converged, and at that moment he turned into a weird creature, wild, concurrently young and old, dying and newborn . . . My father became a myth.

WILLIAM: My father was dying. Sheltered inside an oxygen tent at Jefferson Memorial Hospital, his small, emaciated body seemed bleak and translucent, a kind of ghost already. The doctors were all very grave, even hopeless. Dr. Bennett, our old family doctor, synthesized the details of ongoing reports; he would give us the Big Picture. Dr. Bennett had an old, tired face. The rings beneath his eyes were like dark brown ruts in a road. He had been our doctor for years. But he was a good doctor, and we trusted him.

DR. BENNETT: Mr. Bloom may not make it out of this one. There are a couple of things we want to try—we’re not giving up, not by a long shot. But I’ve seen this sort of thing before. It’s sad, I—I’ve known Edward Bloom for a quarter of a century. I don’t feel like his doctor anymore. I feel like a friend, you know? A friend who wishes he could do something. But without the machines . . . ” (Shakes head sadly)

WILLIAM: I turned and wandered away while he continued to talk to my mother. I went to my father’s room and sat in the chair beside his bed. I sat there and waited—for what I don’t know—and stared at those marvelous machines. This wasn’t life, of course. This was life support. This was what the medical world had fashioned to take the place of Purgatory. I could see how many breaths he was taking by looking at a monitor. I could see what his frenetic heart was up to. And there were a couple of wavy lines and numbers I wasn’t sure about at all, but I kept an eye on them as well. In fact, after a while it was the machines I was looking at, not my father at all. They had become him. They were telling me his story.

Which reminds me of this joke. I’ll always remember his jokes, but this one especially I will remember. It’s a family heirloom. It’s one I tell myself still, out loud and alone, the way he told it to me, I say, There’s this man. There’s this man, and he’s a poor man but he needs a new suit. This man needs a new suit, but he can’t afford to buy one, he can’t afford to buy one until he passes a store where there’s this suit on sale, and it’s priced just right, this beautiful dark blue suit with pinstripes—and so he buys it. Just like that he buys it and wears it right out of the store with a matching tie and everything, but the joke here is—and I guess I should’ve mentioned this earlier—the joke is it doesn’t fit. This suit doesn’t fit him at all. It’s simply way too big. But it’s his suit, right? It’s his suit. So to make it look good he has to place an elbow against his side like this, and his other arm out sort of like this, and he has to walk without moving one of his legs so that the cuffs will appear even, this tiny man in this huge suit—which, as I said, he walks out wearing, walks out into the street wearing. And he thinks to himself, What a nice suit I have! and walks with his arms just so—my father would make his arms just so—and dragging one leg behind with this smile on his face like an idiot because of this great buy he’s just made—a suit! on sale!—when he passes two old women on the avenue there. They watch him pass, and one of them shakes her head and says to the other, “What a poor, poor man!” And the other woman says, “Yes—but what a nice suit!” Which is the end of this joke.

But I can’t tell it like my father did. I can’t drag my leg the way he did it, and so even though this is the funniest joke I have ever heard in my life, I don’t laugh. I can’t. Even when the lady says “Yes—but what a nice suit!” I’m not laughing. I’m not laughing at all. I’m doing the other thing.

I suppose this is what roused him, brought him back to the world for a bit, thinking that if there was anytime I needed a joke, now was the time. God, he really cracked me up.

DAD: Some water. Get me some water.

WILLIAM: Some water, he says! Oh and it’s his voice all right, it’s his voice, deep and booming, caring and gentle. And I get him some water, and he calls me over, to his bed, his only son, me, his only child, and he pats a place on the edge of the bed where I’m to sit, right? So I sit. There’s no time for hellos and how are yous and we both know it. And he says, after taking a sip of water from the little plastic cup, “Son,” he says, “I’m worried.” And he says it in this real shaky voice so I know, don’t ask me how but I know that, machines or not, this will be the last time I ever see him alive. Tomorrow, he’ll be dead.

WILLIAM: What is it you’re worried about, Dad? The hereafter?

DAD: No, dummy. I’m worried about you. You’re an idiot. You couldn’t get yourself arrested without me along to help.

WILLIAM: But I don’t take it personal: he’s trying to be funny. He’s trying to be funny and this is the best he can do! Now I know he’s a goner. (to Dad) Don’t worry about me, Dad. I’ll be okay. I’ll be fine.

DAD: I’m a father, I can’t help it. A father worries. I am a father and as a father I’ve tried to teach you a thing or two. I really did try. Maybe I wasn’t around so much, but when I was, I tried to teach. So what I want to know is—you think I did a good job? (Beat) Wait! Don’t answer that! (trying to smile, but it doesn’t quite work) Oh, go on, then. Just tell me before I die. Tell me what it is I’ve taught you. Tell me everything it is I’ve taught you about life so I can go ahead and die and so I won’t have to worry so much. Just . . . just go ahead and say it.

WILLIAM: I look into his gray-blue dying eyes. We’re staring at each other, showing each other our last looks, the faces we’ll take with us into eternity, and I’m thinking how I wish I knew him better, how I wish we’d had a life together, wishing my father wasn’t such a complete and utter mystery to me, and I say, “There’s this man,” I say. “There’s this man, and he’s a poor man, but he needs a suit, and—” And he smiled. Then he cast his gaze around the room, and he winked at me. He winked!

DAD: (in a hoarse whisper) Let’s get out of here.

WILLIAM: Out of here? Dad, you’re in no condition . . .

DAD: There’s a fold-up wheelchair in the bathroom. Wrap a blanket around me. As soon as we get off this hall, we’ll be in the clear. But we don’t have much time. Hurry, son!

WILLIAM: I did as he asked, I don’t know why. I wrapped him with a pale brown blanket, covering his head like a monk’s habit. I lifted him, with a disturbing ease, from his bed and into the chair. I had no gotten no stronger in the last few months, but he had become considerably smaller.

I opened the door to his room and peeked out into the hallway. I saw Mom at the nurse’s desk with Dr. Bennett, wiping her eyes with a tissue and nodding. I pushed my father in the opposite direction. I dared not even look behind me to see if they had spied us. I just pushed him fast, hoping for the best, and when we came to a corner went around it. Only then did I allow myself a backward view. Nobody. So far, so good.

WILLIAM: (Breathlessly) So. Where are we going?”

DAD: The elevators. The elevator to the lobby to wherever you parked your car. Take me there. Now. We don’t have much time.

WILLIAM: The elevator came and I pushed him on. The door closed behind us, and when they opened again I wheeled him out of there with a daredevil’s panache, past a host of doctors in green and white, past nurses holding charts giving me sidelong glances. Everybody in the lobby paused and stared at us, knowing this wasn’t right somehow, but by then I was traveling at such speed that no one had the time to think to stop us. They simply looked at us as though they had seen something odd—and they had, too, odder than they knew. And then we were gone.

DAD: Good job. Still need to hurry, though, Will. I need some water. I need some water bad.

WILLIAM: I have some in the car -- A thermos full.

DAD: (laughing) More than that.

WILLIAM: When we got to the car I lifted him out of the wheelchair and placed him in the front seat. I folded the wheelchair and threw it in the back.

DAD: We won’t be needing that. (laughing) Not where we’re going.

WILLIAM: But he didn’t tell me where we were going, not at first. I simply drove away from everything I knew: the hospital, his old office, home.

DAD: That water, William?”

WILLIAM: It was beside me on the seat. I opened the top and passed it to him. One shaky, scaly hand appeared from beneath the folds and took it from me. But instead of drinking it, he poured it all over himself. The blanket was soaked.

DAD: Ahh . . . That’s the ticket.

WILLIAM: Still, he didn’t take the blanket off.

DAD: Go north on Highway 1. There’s a place there. There’s a river. A place by the river.

WILLIAM: I took the car down a series of streets, through the city and the surrounding suburbs, where the sun was rising over the roofs and treetops, until finally we broke into the deep, green, beautiful country. (To Dad) How far now?

DAD: Just a couple more miles, I think. I hope. I don’t feel so good.

WILLIAM: What’s there? (To audience) But for an answer all I got was a shivering inside the damp blanket, and a gurgling, groaning sound, as if he were in deep pain. (To Dad) Are you okay?

DAD: Been better. I feel like that guy . . .

WILLIAM: Who walks into the bar with a frog on his head, with a bird on his shoulder, with a kangaroo at his side and the bartender says, “Hey, we don’t get that many kangaroos in here,” and the kangaroo says, “Yeah, and at these prices you’re not likely to get many more!” And then he said, suddenly almost yelling,

DAD: Here!

WILLIAM: And I pulled off the road. There was your old oak tree with the roots spreading out through the dark and mossy soil. And there was your river, running clear the way you didn’t think rivers ran anymore, moving fast around stones the size of a small car, making little rapids, running as clear as the air, as blue as the sky, as white as a cloud. I don’t know how he saw it from beneath the blanket.

“Carry me,” he said, or so it sounded, his voice so weak now I was doing my share of interpreting as I listened. He said, Carry me and You don’t know how I appreciate what you’re doing and When you see your mother, tell her—tell her I said good-bye. And so I carried him out of the car and down the mossy bank to the river and stood there before it, holding my father in my arms. And I knew what I was supposed to do then but I couldn’t do it. I just stood there, holding his body shrouded in a blanket on the banks of this river, until he told me, You might want to look away now and then Please, and all of a sudden my arms were full of the most fantastic life, frenetic, impossible to hold on to even if I’d wanted to, and I wanted to. But then all I was holding was the blanket, because my father had jumped into the river. And that’s when I discovered that my father hadn’t been dying after all. He was just changing, transforming himself into something new and different to carry his life forward in.

All this time, my father was becoming a fish.

I saw him dart this way and that, a silvery, brilliant, shining life, and disappear into the darkness of the deep water where the big fish go, and I haven’t seen him since—though others have. Already I’ve heard stories, of lives saved and wishes granted, of children carried for miles on his back, of anglers mischievously dumped from their vessels and emptied into various oceans and streams from Beaufort to Hyannis by the biggest fish they’ve ever seen, and they tell their stories to anybody who will listen.

But no one believes them. No one believes a word.
```

---

## IC-0318: Big Mac, Strawberry Shake and Large Fries

- Title: Big Mac, Strawberry Shake and Large Fries
- Author (byline): Jared Botticelli
- Work: Fast Horse Plays, Round 5, Pg 3-9
- Publisher: Create Space Independent Publishing
- Publication date as stated: July 2013
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1721
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jared Botticelli
Book: Fast Horse Plays, Round 5, Pg 3-9
ISBN: 978-1491283189
Publisher: Create Space Independent Publishing
Date (Month/Year): July 2013
```

### Introduction (context only: never use it for content warnings)

```text
* In 2023 over 550 anti-LGBTQ bills have been introduced into state houses across the county; more than 80 have been passed into law. Record-breaking. And against this backdrop of discriminatory legislation, attacks on the LGBTQ community are on the rise. Hate-filled rhetoric from our politicians and on social media leads to real world violence. 2022 saw the highest number of anti-LGBTQ hate crimes reported to date and the number are not yet in for 2023.

Welcome to a hate crime – or as Apollo likes to call it “The Night of the Incident.”

Big Mac, Strawberry Shake and Large Fries by Jared Botticelli
```

### Performance text (classify this)

```text
NOTE: Contains triggering labels used against the LGBTQ Community Apollo, a young man, somewhere between 17 and manhood, picks up a cup and takes a long drink through a straw. He looks with appreciation at the cup and then puts it down.

Strawberry shakes rock my world. No kidding. Right now, I can't really think of anything that makes me happier than a friggin' Micky D's strawberry shake. My boys always gave me crap about ordering strawberry, but ya know what, Real Men drink Strawberry. I kid ya not. Apollo picks up his Big Mac and pulls the paper back. He takes a bite. Add in one of these beauties, and, well, you've died and gone to Big Mac heaven. He eats the last bite of his burger, crumples the paper into a ball and tosses it. He calls out to someone other than the audience before him. 'K, I'm done. I'M DONE.

Uh, so it's kinda funny, but that's what I had that night. You know, "The Night of the Incident," as everybody and their mother likes to call it. Okay, hold up. Hold up. I need to give some history here. Get you guys up to speed with all of this.

Was me, Peach and Slideshow that night. Three of us boys, We'd just been out driving in my Mustang. Cherry Red. My Mom and Pops bought it for me for graduation. Only had it for coupla months. So, anyway, we're out driving around, went to McDonalds, and umm, Peach used his fake ID to score us some beer at 711 and we drive down to that park in Midtown. Ya know, Triangle Park. The cops don't usually go through there at night, so that's where we'd go to drink or whatever. So, that night, we're sitting on the wall, drinkin, talking about going away in the fall, right?

We'd been there awhile when we see this dude walkin down the sidewalk across the street. We could see him, ya know, plain as day with the streetlights and what-not. And Peach and Slideshow, they start laughing, right? They start bustin up because he looks like. . . he looks like he's queer, ya know? Like he's gay. Tight jeans like a chick would wear, muscle tee, whatever. We knew he was walking home from the gay bars, right? Cuz there like two or three blocks down from the park or whatever. And umm, we start yelling crap across the street to him. Stupid stuff, ya know. "Hey homo," "Why don't you come over here and show us what you're good for?" -- Just teasin', right? And then, umm, somebody yells, "Faggot" and this guy, he turns and he yells back, "S**** you." And see, the thing is, that's what started all this. If he'd just kept walkin', none of this woulda ever happened . . . but, he yelled back.

And then, umm, all of a sudden we're not sittin' on the wall anymore, somehow we're across the street, right where the dude was walkin'. And somehow, Slideshow has the bat from the back of my 'Stang, and that guy, that gay dude, is down on the cement, and his arms and legs are goin' all crazy, like an octopus or something, just swinging around, and Slideshow, he's holdin' that bat just like when we were in high-school. And then, Slide is swinging the bat and he connects, but he's not hittin' a ball, he's hittin' this dude, and he swings and hits; swings and hits; swings and hits and the guy is making these sounds like a wild animal, cryin' out, growling, begging, screamin', all this stuff all at once.

And, uh, then Peach takes the bat and he swings too, and he hits this dude, like a buncha times. Then we're all just kinda standin there, ya know? And uh, Peach, he says to me, "Do it, man, you gotta do it. Just like a pinata. Just like a pinata, man."

And, uh, see the thing is, I wasn't gonna hit him at all, ya know? He was busted up bad already, and, uh, I thought we should just split, right? So, I'm just standin' there, not doing anything, and Slideshow says, "What's the deal, Apollo? You wanna kiss the queer and make him better? What are ya, queer, Apollo?"

I'm not, of course, and my boys they know that, but I got so pissed off that I took the bat, my bat, and I'm looking at this guy on the ground and he's bleedin real bad, but he can still talk, can still yap, ya know? And he looks up at me and he just says one thing, jus' one. He says, "Tell my Mom I love her," and I swung the bat and when it connected it was like hittin' something soft, but then there was this cracking and I'm swinging and swinging and then, I dunno, I hear Peach say, "Dude, that's enough man, we gotta split. The queer might have AIDS. . . we gotta go get this off." And I realize there's all this blood. So much blood. Like the three of us are in a horror movie or somethin. So we split. And we left that guy on the sidewalk.

The dude's name was John Smith. And, guess what, he was a gay guy. Had a boyfriend or life partner or whatever they call it. He was 25. He died in the ambulance on the way to the hospital.

And, uh, by morning it's all over the papers and on the news. And Peach, he doesn't even last a day before he squeals to the cops. So I get arrested and that's when everything starts goin' really bonkers, ya know? And my Mom and Pops they get this team of lawyers, and they come every day and ask me questions about everything. Stuff that doesn't have anything to do with "The Night of the Incident." I have to answer questions about my family and Peach and Sideshow and whether I've ever had a girlfriend (negatory on that front -- never found one that met my standards, ya know?) and they just keep askin' all of these questions, and then the trial starts. And, I guess, to tell ya the truth, that's where I get a little sketchy on everything. It just went on forever.

I started to see it like a circus. Like I was six again or somethin' and I'm at the circus with my pops. And the lawyers are all lions growling at each other, and all the people that came and talked about blood types and stains and splatters are just clowns and some of them have happy faces and some of them have sad faces, and the judge, this old bald guy with big glasses, he's the ringleader, ya know? Directing all of them. It's like I could smell the popcorn and hear that music, the circus music, just playing on a loop over and over again. My lawyers did good though, they did, they tried to help me, tried to say it was Peach who beat the dude last and that it wasn't my bat and they used words I didn't even know, like "Narcissistic Personality" and "Internalized Homophobia" and, uh, the thing is though, I did it. I did. His blood was on my clothes, in my 'Stang, everybody knew I did it. And so, one day we're at the circus, the trial, and this District Attorney, she's grillin' me, askin' me the same dumb questions over and over again, • "How many times did you strike Mr. Smith with the baseball bat?" • "Did you intend for Mr. Smith to die?" • "Did you mean to strike Mr. Smith in the head?"

And the circus music is just like drillin' a hole in my head and I’m feelin' like I'm gonna puke and I just see red, all this red blood all over everywhere and I put my head down and then I just said it. I just lost it. I did.

(Yelling) "I killed him, okay? I knew I was gonna kill him when we went over there. I beat his head in with a bat, okay? I killed him." (long silence)

I don't even know why. I just did. It was like I was the one bleedin' all over before I yelled and then afterwards, everything was quiet. And I look out across the circus and I see my Mom, ya know? And she's just mouthing "I love you" over and over again. It was over pretty quick after that.

I had to meet with all kinds of shrinks to make sure I wasn’t crazy. . . and well, they decided I wasn’t. I’m not an expert on life or anything, but I guess shit just happens sometimes. Anything coulda changed that night. I coulda gotten food poisoning from my Big Mac or we could agon to see Slideshow’s girl, or I coulda told Peach . . . whatever. Ya know what I mean, right? It coulda turned out way different is my point. But it didn’t. I’m not a bad kid, I just did something screwed up.

Someone from outside the audience addresses Apollo and he responds to them.

Huh? It's almost time. Gotcha. I gotta finish my fries first. I always leave my fries 'til last. Cuz they burn my tongue when they're hot.

I told Mom I was gonna be really brave about all this. But uh, right now . . . I . . . umm, I don't wanna sound like a Marna's boy or anything, but when I was a little kid Mom used to sing this song to me, the mountain song, ya know, (singing) "She'll be coming 'round the mountain when she comes, she'll be pulling six white horses when she comes. . . and so, I'm just gonna kinda sing that all the way through, all the way, ya know?

I really love my Mom. I won't be able to see her through that mirror thing, but I know she's gonna be there . . . Hey, if you guys see her or whatever, you let her know that it wasn't her fault.

They say the gas chamber is like you're drowning -- like you're goin' out to sea and ya never come back. They say you gotta breathe in deep, real deep, ya know? So that's what I'm gonna do. I don't wanna drown. So I'm gonna breathe in deep . . . real deep. I'm gonna let the sea take me home. Apollo responds again to an unseen voice. Okay, okay. Jeez. I just got a fry or two left. Yup. I gotcha.

(singing) She'll he coming 'round the mountain when she comes She'll be comin' round the mountain when she comes. . .
```

---

## IC-0319: Blackout

- Title: Blackout
- Author (byline): Gary Lennon
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 1997
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JACK
- Teaser before the introduction: Yes
- Spoken words (computed): 1528
- Already set (do not supply): none

### Source block (context only)

```text
Author: Gary Lennon
ISBN: 978-0573662362
Publisher: Samuel French, Inc.
Date (Month/Year): 1997
```

### Introduction (context only: never use it for content warnings)

```text
Overcoming an addiction to alcohol can be a long and bumpy road. At times, it may even feel impossible. But it’s not. If you’re ready to stop drinking and willing to get the support you need, you can recover—no matter how bad the addiction or how powerless you feel. You don’t have to wait until you hit rock bottom; you can make a change at any time. Blackout by Gary Lennon takes us into the world of Alcoholics Anonymous as Jack, the leader of this particular group, shares his story.

Blackout by Gary Lennon.
```

### Performance text (classify this)

```text
JACK: Hi, my name is Jack and I’m an alcoholic. (pause) Thank you. It’s funny I haven’t been in this room for a long time. I haven’t done this in awhile. I forget where to begin. Uh…I’m so nervous. It’s hard to believe I’m celebrating my seventh year of sobriety. It seems like just yesterday I was a drunk. I guess I’m still a drunk, but a dry drunk. I never thought I had a problem with alcohol.

JACK: People were always telling me that they thought I had a drinking problem. But being Irish, I thought they were crazy. I wasn’t going to give in to that. Being a drunk. I was going to defy the tyranny of fact. One of my friends said, “I think you’re an alcoholic.” I said, “no, not me.” I thought an alcoholic was a bum, one of those guys sleeping in the streets. I was too young to be an alcoholic. I thought you at least had to be 40. Was I surprised when I hit bottom, and I woke up in the morning with somebody else’s clothes on, and I didn’t know how I got there. I thought an alcoholic had to drink everyday of his life. I just drank every other day.

My life has been so good since I’m sober. I’ll start at the beginning for the newcomers. My advice is to stay with the program. It works. If I could stop drinking, anybody could. I know that everybody says that, but it’s true. I took my first drink when I was twelve, and it seems like I never stopped. My brother got me drunk the first time. It was beer. Then it was Boone’s Farm Apple Wine. I learned about sex through Boones Farm. In P.S. 111 on a ledge. It never seemed to get better than that. I was shy. The wine loosened me up. You know what I mean.

My father was an alcoholic. He died of it. So, this is a serious disease. He died drunk. He died drunk with his face down in a puddle. He could have lived if he wanted to. If he was sober. But he was drunk. He died when I was little. And all I remember is that I hated him. I can hardly remember his face, you know, but I remember his smell. It was Jack Daniels. Me and my brothers took right after him. I don’t think he meant the things he did. I don’t think that he wanted me to hate him, but he could have at least told me he loved me once. No matter how drunk he was.

Both of my parents died before I was thirteen. I figured that was a good enough reason. When my mom died, I remember the night when they told me. I went out and got really drunk with my friend in the pack on 12th avenue and 51st street. We drank. I thought that if I drank so much, it would put me asleep, so that when I woke up, it wouldn’t be real. She wouldn’t be gone. I remember the next night I went down to the park again by myself. I brought a case with me. I drank, and there was a really bright star over the Chrysler Building, and it was watching me. I felt it. I knew it was her, and I said to it, “I don’t wanna be like him,” I promised. I don’t want to be like him. I drank to be numb. Numb so I wouldn’t feel the loss of them or feel the anger. The anger at someone or something for taking them away, because I didn’t have a dad to teach me to play baseball, or teach me to fish, or teach me to be a man. I may have hated him, but I wanted him around. At least he was mine. (pause)

I used to have a bottle of scotch in my locker. I thought I was cool. I was kicked out twice. But they kept taking me back because my grades were so good. I was smart. I was a functioning alcoholic. I don’t know how it worked. After high school, I got jobs, but I didn’t keep any because they would get in the way of my career of drinking. They were good paying jobs too. I should have a lot of money saved, or a nice apartment, or something. I don’t know where the money went. I guess I took a lot of cabs.

Relationships were a joke. Alcoholics don’t have relationships. They hold hostages. It’s like, “You love me, don’t you? You want to suffer with me, don’t you?” I was married for four months, but it was a joke. I was drinking so much at the time that I was crazy. I was seeing this girl for six months, and she started to really drive me out of my mind. As you know, alcoholics are terrified of being alone. So, I was going to jump out the window or marry her. So, I married her. I was stubborn. I never made love to anyone sober. I couldn’t I always had to be drunk. I just couldn’t have sex sober. So quiet. It was too scary. It was too intimate. Just you and that one other person.

My very last time being drunk was a blackout. That’s when you don’t remember what you do. It was a gin martini binge. Drinking did crazy things to me. I woke up in this afghan covered bed. I didn’t know where I was or how I got there. I felt this strange sensation my body was going through. I couldn’t life my head. I looked to the side of me, and I saw this night table. On it was a clock. I was trying to make out the time when I saw this clear glass filled with water and something pink floating in it. I looked closer. It was someone’s false teeth. Pink and white. And then I heard this . . . “I met you last night at the Blarney Stone next to McDonald’s on 56th and 8th Avenue.” That night I went back to AA.

What I guess I’m really trying to say is that I’m grateful. I’m grateful for this room, and I’m grateful to be sober. When I first walked into this room seven years ago, I had a pint of Jack Daniels in my pocket and about a dollar fifty, and I was in ragged old clothes, and I smelled just like my father. I came in and I sat in the back. I was scared. I didn’t talk to anybody. I couldn’t raise my hand to say my name. I thought all of you were crazy and derelicts and you all smoked so much. I thought, “Great. All these people are getting sober, and they’ll die of lung cancer.” All of you were saying such personal things. I was intimidated by your honest. I said, “This place isn’t for me.” But I came back the next day and the next. I didn’t have anywhere else to go. And the day after that and I kept coming back for 90 days. I came to a meeting every day, and the most important thing was I didn’t drink. I didn’t have to try and change my life in one day. I could do it one day at a time. I didn’t say a word to any of you people, and you all shared your lives with me, telling your stories, and I thank you, because that’s what kept me sober. Your stories. Just listening. You all loved me unconditionally, and you didn’t even know me. You were all selfless. It’s taken me 24 years to find the definition of the word’s integrity, honesty, friendship, and love, and I’ve learned them through you. I love all of you, even the ones I don’t know. You all gave me the love that I was looking for. And now, you know what? Every night at seven o’clock, I look out my window and I look up at that same star over the Chrysler Building, and I’m not drinking.

You know what the best part of being sober is? It’s being able to go out with someone at night and being able to see them the next day without being humiliated about what you did or said the night before. The most important thing being sober has done for me is helping me know who I am! Who Jack is! When I was drinking, I didn’t know who I was. I had spent all those years developing into a drunk person who didn’t know himself. Who I didn’t like. When I got sober, I asked myself, “Who are you? What makes you tick? How do you feel about that?” It’s hard to be honest with yourself sometimes. So many people go around not knowing who they really are. They’re afraid to ask. The answers might scare them. It’s hard to take that extra moment to take a long look in the mirror and confront yourself. Do it! It’s worth it.
```

---

## IC-0320: A Bone Close to My Brain

- Title: A Bone Close to My Brain
- Author (byline): Dan Dietz
- Work: Humana Festival 2004 Complete Plays, Pgs 16-23
- Publisher: Smith & Kraus
- Publication date as stated: April 2005
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MAN
- Teaser before the introduction: Yes
- Spoken words (computed): 978
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dan Dietz
Book: Humana Festival 2004 Complete Plays, Pgs 16-23
ISBN: 978-1575253855
Publisher: Smith & Kraus
Date (Month/Year): April 2005
```

### Introduction (context only: never use it for content warnings)

```text
What are the limits of brotherly love? And what do they have to do with the 32 bones huddling tight inside your mouth? Through sparse dialogue and childlike illustrations, a man describes his relationship with his younger brother -- who is both brilliant and mentally ill -- and the heartbreaking decision he has to make.

A Bone Close to My Brain by Dan Dietz
```

### Performance text (classify this)

```text
A MAN stands beside an easel; he uncaps a marker and draws a big tooth on the paper.

MAN: (Pg 16-23) today my brother is a dentist
he knows all about these little bones
huddling tight inside your mouth
incisors, bicuspids, wisdoms way in the back
he knows them all
their shapes and contours
their uses and misuses
the damage they can reasonably take
from impact or decay
my brother is a dentist today

i don't mean he just got certified
i don't mean he opened a practice
i mean that today my brother is a dentist
just like yesterday he was a radiologist
and last month he was a reporter for the new york times
only two things about him stay the same
day in, day out
his address, this tidy little house in new jersey
which we've shared for the nine years
since our parents passed away
and the fact that i am his big brother
no matter what else he erases and remakes
inside his mind
these two facts sit solid and bonehard
within his head

MAN: he can't feed himself
he doesn't grasp the need to fuel his body
he can't bathe himself
left on his own, he'll either starve or stink himself to death
he doesn't live in his skin, his stomach, his fingernails
he lives here
in the bulbous gray organ
just above and behind
the roof of his mouth
that's his house

(MAN draws a roof and windows on the tooth, maybe even a chimney with smoke)

the rest of him
skin, stomach, fingernails
is like a yard (draws a yard by the house)
a yard that needs a full-time, round the dock landscaper
to keep from going to hell
that's me
i tend him
he trusts me
anyone else comes near the yard
(skin, stomach, fingernails)
he screams, hits, bites
gets arrested, gets bailed out, forgets, etc.
but not me
he would never hurt me

except for today
today he will hurt me
in about ten minutes
he will walk in here
lay me down on this chair
and tear out of my head
a single, white, completely healthy
tooth (flips to a new sheet, draws a new tooth)
and i will let him

i can't get used to the way teeth look
strange
spiny
like they belong on the outside
of some prehistoric fish
not sprouting from my face
maybe i should smile more
but i was always that way
even as a kid
i can't find one picture of me
smiling showing my teeth
always just a twist of the lips
to indicate a grin
gerald always smiled with teeth
he's smiling right now
in the kitchen, sterilizing his instruments
which consist of a penlight
and a pair of pliers

he's brilliant
he learns this stuff in just hours
pores over textbooks
random ones i pick up
from the public library
to keep his house (draws a roof on the tooth, draws a yard)
occupied (draws a happy stick figure waving from the house)

he dives into the volumes
(the only medication he'll accept)
and the next time i see him
he's completely reborn
he's memorized it all
he's a dentist
(radiologist, reporter)
and he can't remember a day
when he wasn't a dentist
(radiologist, reporter)

he was reading tolstoy at age eight
studying fractals at eleven
those huge numbers
blooming out infinite all over the place
numbers that want to be pictures
he called them

what does a number do if it wants to be a picture

he grew into adolescence
his head devouring everything
like his eyes were mouths
awards, acclaim
the "g" word tossed about
(and i don't mean "gerald")
by people important enough to believe
he was slated to graduate high school
before his sixteenth birthday

then mom and dad died
when our house
got broken into (draws a hole on the house and an arrow pointing into the hole)
attempted robbery
became
attempted rape
became

i was away at college
i didn't have to come downstairs
didn't have to try to stop it
try to save
but gerald
he was fifteen
the same age as the boy
they caught and convicted
after finding his skin cells
beneath my mother's

i moved back home
took a break from school
gerald however refused to take a break
so close to graduation
less than a year
but the things he started saying
and doing

it was like his mind had twisted
to indicate a person (points to the person waving from the house)
a person
that wants to be a picture
and he'll erase and try again
until he gets the picture
right

he's beautiful at night
he sits in his room
soft light
pages blurring by

he was expelled
for tearing open a substitute's blouse
he insisted she was in danger
her beat was irregular
he could hear it across the room
he had to press his stethoscope
to her bare chest to be sure

silly tragic moments are always so f***ing silly

like this one today

(flips to a new sheet, draws a new tooth)
today my little brother
will remove my tooth
which he is convinced
upon examination with his penlight
is rife with decay

(draws holes on the tooth) little holes in a bone close to my brain

he will administer anesthetic
a rag steeped in ether
(which he got from god knows where)
and pluck out my tooth
("pluck" is probably not
the right word)
and smile
believing
he has saved me from danger
i will give him this belief
today
and tomorrow
i will take him to a place
where they will administer
a more sophisticated anesthetic
one which will
maybe
combined with other treatments
over the course of years
help

tomorrow i will turn him over to people who will break into his house

(draws a roof on the tooth, a yard, arrows pointing into the holes in the tooth)
and do their best
as he flails and screams
to clean the damn thing up

i will leave him there i will erase him and

because i can't i

you wake up one day
and the decay
i can't find myself
in this picture

i will leave him there
and return here (turns to a fresh blank page)
to my house
and gerald
i know
will hold onto my tooth
forever
a bone close to my brain
perhaps it will reside
beneath his pillow
as he sleeps
giving him dreams
of his big brother
crying "don't hate me"

don't hate me

and perhaps
somewhere in the back of my mouth
i will feel the head
of my little brother shift
in the night
every night
after
tonight.
```
