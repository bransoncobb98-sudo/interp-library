# Classification request: batch 7 of 53 (40 records, IC-0641 to IC-0680)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-007-reply.json`.

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

## IC-0641: The Girl in the Picture

- Title: The Girl in the Picture
- Author (byline): Taylor Shann
- Work: The Girl in the Picture
- Publisher: Mushroom Cloud Press
- Publication date as stated: 2006
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JODI, LAYLA, SCENE TWO, SCENE TEN
- Teaser before the introduction: No
- Spoken words (computed): 3635
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
SCENE ONE

JODI and LAYLA in JODI’S room. LAYLA is reading a fantasy book on a beanbag. JODI stands at her door, shouting down to her mother.

JODI: Yeah, well, if I wanted to go with you to the store, you should have known that before you went! It’s called logic, mom! Get some! (slams door, then screams, venting)

LAYLA: What was that about?

JODI: Oh, stupid. My mom keeps saying that we’re gonna fight, because now I’m a teenager and that’s what moms do with their teenage daughters. So she says.

LAYLA: …but don’t you and your mom get along?

JODI: I know, right? What the hell? I’m like, it’s called a self fulfilling prophecy, and she’s like go to your room and I’m like Mom, I’m already in my room, that’s where it all started- I need rant music-(she holds out a cd) Mix A, Mix B, Mix C… you’d think he’d label them…

LAYLA: Think it’ll snow soon?

JODI: I hope so. A snow day would be great. Cause, it’d fund the local economy, all those snow plow guys, and Ms. Glaptits would get a day off and get off my ass about the F’in Hawley-Smoot Tarriff-

LAYLA: (turns) Glaptits? You mean Ms. Glaydis?

JODI: (giggles) That’s what Joe started calling her. Cause her huge chest goes glapglapglap every time she’s hovering over you.

LAYLA: Joe’s stupid.

JODI: No, Joe’s smart. Joe’s jokes are stupid.

LAYLA: Joe’s stupid.

JODI: Whatever. He’s tall and he doesn’t make fun of me, that’s- (turns up the volume) Hot. This is hot.

LAYLA: This is loud.

JODI laughs and begins to rock out. LAYLA smiles, watching.

JODI: See, the socioeconomic undertones of this song, is the right of girl rock to rock out. And that is what matters. (Turns on Computer) So, what are you getting me for Christmas?

LAYLA: Jews don’t celebrate Christmas.

JODI: C’mon, Lay! This is America! Everyone celebrates Christmas! Even the Athiests give presents!

LAYLA: I’m not getting you anything for Christmas. You don’t celebrate Christmas.

JODI: You celebrate Christmas.

LAYLA: My parents just ask me for a list of what I want, and I give it to them and I get some of it. Then we go see a movie. Very religious and holy, I assure you.

JODI: I’m getting you something for Christmas. (to the tune of the song) CHRIST-Mas, CHRIST-Mas-

LAYLA: I’m not stopping you. (gets up and leaves, Jodi doesn’t notice)

JODI: What are you getting me for Christmas? Na na na na na na, What are you getting me for CHRSITMAS? Na na na na na na-(turns towards where Layla is, stops) na. Na.

SCENE TWO:

Layla and Jodi on Instant Messaging. Stage this as you will.

JODI: ChicFluxRock22 has signed on.

LAYLA: Eowyn1R2RTA: hi

JODI: ChicFluxRock22 : hello.

LAYLA: Eowyn1R2RTA: how friendly/unfriendly.

JODI: ChicFluxRock22 : what do you prefer? howdy? hihi? hola?

LAYLA: Eowyn1R2RTA: you've said them all before

JODI: ChicFluxRock22 : I like to mix it up. hello is acceptably cheery, I feel. does it need the exclamation mark to work?

LAYLA: Eowyn1R2RTA: I think the period conveys chilliness in IM. a hello there or hello, smiley face, or even just hey… even hello, no period, has a certain shortness, that, ironically, is not found in

JODI: ChicFluxRock22 : well, let's start over. Hey hey, Layla Johnson! Smiley face. Or even, Grinning Face! How’sa by you?

LAYLA: Eowyn1R2RTA: hello.

JODI: (beat) ChicFluxRock22: I see what you mean. ChicFluxRock22: Hey, layla.

LAYLA: Eowyn1R2RTA: what?

JODI: ChicFluxRock22: Merry Christmas!

LAYLA: Eowyn1R2RTA: Would you shut-

JODI: ChicFluxRock22 Has signed off!

LAYLA: Eowyn1R2RTA: Damn.

JODI: ChicFluxRock22 is no longer available.

LAYLA: Eowyn1R2RTA: I know!

JODI: ChicFluxRock22 is no longer available.

Scene Three:

Back in Jodi’s room, late. Layla’s on a sleeping bag, rooting through her backpack. Jodi lays in her bed, staring up at the wall.

JODI: Can it be like, fun for them, you think?

LAYLA: Can what be who where?

JODI: The asking. The walk over. The (hand gesture) “Gee I was wondering… if you’re not doing anything on prom night?!” Gee, what the hell am I doing on Prom Night? Twiddle twiddle twiddle twiddle my thumbs, that’s what I’m going to do, idiot.

LAYLA: No one says Gee anymore.

JODI: Joe’s gonna ask me out.

LAYLA: Joe’s stupid. (finds her book, pulls it out)

JODI: But he keeps turning away, he’s like, avoiding me, which means I know- I think I know- he likes me, I guess, I don’t know. (beat) But he’s gonna ask me. (beat) No one makes six Mix CDs for someone lightly. (beat) I mean, those CD-R things are expensive. Right?

LAYLA: Allow me to hypothesize the following: The wrong person asking, you are.

JODI If he doesn’t ask me, Martin will-

LAYLA: Martin’s stupid.

JODI: No, Martin, is, like, a G.D. idiot savant, except he’s just an idiot. And he’s- (sits up) Well he’s not my first choice and neither is Joe, but Joe I will choose to say, Why No, I’m not doing anything. How delightful of you to think of-

LAYLA: All boys are stupid.

JODI: (looks at Layla) We’re not in the 7th grade anymore, Layz.

LAYLA: (flips a page) As I get smarter and older, I find only confirmation in my beliefs.

JODI: (grabs the book flips through it quickly) Elves, Orcs and Starships. Oh my! (drops it) I can’t believe you’re re-reading this. Even in the 7th grade, this was my least favorite.

LAYLA (patiently finds her place again) Boys are stupid, Elves are cool.

JODI: I mean, yes, boys are stupid, but, stupid and cute, some of them, not Martin definitely not Martin, but through that stupidity, there is a sort of… you become-

LAYLA: Stupider.

JODI: (stands) You’re in a mood. And it’s ‘less intelligent’. I think. Don’t let my mom hear you saying stupider, I’ll, like, never hear the end of it. (shuffles through her CDs) What to play, what to play…

LAYLA: (stops rooting, looks up) Hey.

JODI: You know what, I like Marcy Playground. I don’t care what people say.

LAYLA Um. About Christmas…

JODI: Oh! Damn it! You! Hold on! Hold on!

Jodi runs into her closet. Layla pulls out a small box wrapped poorly. When Jodi walks back in, Layla hides the package.

JODI: Damn it Damn it Damn it! It’s still downstairs. Hold on- don’t go anywhere-

LAYLA: (smiles) Where would I go?

JODI runs downstairs. LAYLA stops smiling, looks at the mirror at herself. She stands, moving the light, holding the present. She puts it down on the bed, looks at the mirror. She turns her head, lifts her chin up to a certain angle, moves her hair to the side. Pause. Using the her other hand, she turns down the light next to the bed and looks again. Finally, a smile.

JODI: (offstage) Now I know I don’t celebrate Christmas –(Layla spins, knocking the light over) and neither do you really and we’ve gone through this for the last three years but I got you a present anyway so shut the hell up and take-

LAYLA: (thrusts the gift out) Merry Christmas!

JODI: I knew! I knew you couldn’t resist! You didn’t have to- neither did I, but- you go first! You go first!

LAYLA: … (opens it) a picture frame.

JODI: (giant grin) It’s got a dradle on it.

LAYLA: Yeah. Yeah I got that.

JODI: Well, I thought you should know that my people killed your people’s God so you could get it!!

LAYLA: Very… kosher of you.

They both crack up, Lalya takes her present out of the bag as Jodi hits play on the CD player.

JODI: Now me! Me!

LAYLA: I thought…

JODI: What- (opens it, stops, looks at her) Oh.

LAYLA: I thought, like, um. Real presents. So.

Jodi runs over and hugs her. Layla doesn’t know what to do.

JODI: I can’t believe you- oh my god, nothing I got this year was that cool- (she pulls it out, it’s a digital camera)

LAYLA: I mean, you don’t have to go all Gandalf crazy over it, my dad got an extra so he-

JODI: I mean, this was what I like really wanted and- hey- was this planned? Did you know I was getting you that crappy frame?

LAYLA: No.

JODI: Oh my god you got me a camera and all I got you was a crappy frame. I am the worst friend ever.

LAYLA: (smiles) sa’lright.

JODI: The hell it is! Ummmm… look, (opens the box) put in the batteries! Now! (goes to her CD pile) You’re getting a present right now.

LAYLA: That’s really not…

JODI: Smashing Pumpkins, STP, Saaaaaaa- (finds it) tana! Santana- pressing play, batteries in?

LAYLA: Um.

JODI: Picture and a dance! (takes her hands, forces her to dance, it is awkward)

LAYLA: Hey…

JODI: Listen to the lyrics! (sings along) “Well it’s too late to say you’re sorry…”

LAYLA: …sorry…

JODI: “How would I know? Why should I care?”

LAYLA: (beginning to relax) care…

JODI: “She’s not THEEEERRREEE!!” (lets go of Layla, jumps on the bed and dances, shouts over the music) They don’t make rock like this anymore. This was like, Rock before Rock was Rock! Oh! (turns off the music) A picture! A picture for your crappy frame, give me the camera-

LAYLA: I don’t want a picture.

JODI: Hush.

LAYLA: ‘m just saying, is all, I don’t need-

JODI: Hush and get in the picture. (she does, Jodi holds the camera out for both of them) Best Christmas ever! Mazel to-

The camera goes off, with the flash. Right in their eyes.

JODI: Ow!

LAYLA; Jodi, I think I blinked.

JODI: I think I’m blind.

SCENE FOUR

Back online.

LAYLA: Eowyn1R2RTA has signed on. Eowyn1R2RTA: Hey. J. You there?

JODI: Away Message from ChicFluxRock22: Despite all my rage I am just a rat in a cage. Despite all my rage I am just a rat in a cage. Despite all my rage I am just a rat in a… CAAAAGGGGE!!! Bullet With Butterfly Wings, The Smashing Pumpkins. Hellz yeah!

LAYLA: Eowyn1R2RTA: I gotta tell you, I’ve been listening to the album, both discs and iiiiiii just don’t get it. Eowyn1R2RTA; I mean, I get that he’s angry. But I don’t get the… point? Eowyn1R2RTA: Especially not when I’m trying to write, cause… I mean. Hey. Enya works better for fantasy than rock. What can I say? Eowyn1R2RTA: C’mon, J, where are ya? Come back to the land of the online dead! Weeeee missssss yoooouuuuu, weee misss-

JODI: Away Message from ChicFluxRock22: Despite all my rage I am just a rat in a cage. Despite all my rage I am just a-

LAYLA:
Eowyn1R2RTA: Yeah, yeah, I get it.
Eowyn1R2RTA: Meh.
Eowyn1R2RTA: You know what it is? Even the angriest these guys get, it’s still about love, getting it or
losing it or whatever-
Eowyn1R2RTA: and if it’s not elves, I’m just not interested. No rock star’s gonna kill himself over me, not
unless I go bullemic.
Eowyn1R2RTA: Alright, I’m out. Fly, fly fly away-

JODI ChicFluxRock22 is no longer away. ChicFluxRock22: Lays!

LAYLA: Away message from Eowyn1R2RTA: Meh.

JODI: ChicFluxRock22: Joe asked me out! I’m going to prom! Seven Mix Cds, Seven! AAAAAAAAA! Call me! ChicFluxRock22 has signed off.

SCENE FIVE

Jodi’s house. They’re both dressed to go out. Well, Jodi is dressed for a rock concert, and Layla is at least dressed to go outside. Jodi stands in front of the mirror.

LAYLA: So, technically, he didn’t actually ask-

JODI He asked me to a rock concert a month before. If that’s not a commercial for the real thing then, like, what is. And I know that’s a shallow thing to say, shut up.

LAYLA: There’s nothing left to say.

JODI: Would you get up here and take a look. (Layla grunts and stands) How do I look?

LAYLA: Trampish.

JODI: Honestly?

LAYLA: Honestly? Whorish. As your friend? Trampish. (turns to sit)

JODI: Sttttaaayyy up here. I’m going to trampify you if it kills me.

LAYLA: Shut up.

JODI: Would you just look- look in the mirror, focus! There. (beat) What we have and what we show. That’s what my bubby says. When she doesn’t make me feel guilty for existing.

LAYLA: I get this crap from my mom, J.

JODI I’m just saying! You’ve got this cool, cool natural beauty-

LAYLA: Oh, Natural. Natural. And I’ve got a lovely personality, too.

JODI: And if you just tarted it up a bit, I mean… Joe said Martin was coming.

LAYLA: Thank you and goodnight. (jumps onto beanbag) Have fun.

JODI: What is the problem, Lady Dracula?

LAYLA: Look… I just-

JODI: What?

LAYLA: I just don’t like looking at myself, that’s all.

JODI: Layla! That’s… I mean that is so f’d up I don’t even know where to start.

LAYLA: When the light hits here. (moves her head) When it’s right there. And it puts my cheeks into shadow. And the hair falls here. Like yours? (looks in the mirror) If I could stay like that, at all times. I’d be alright. But the light doesn’t hit there, and my hair is the rebel army trying to break away from Hoth and I take the world’s worst picture. So. (sits in the beanbag) I am content to be a bucket of grease covering a bag of ideas.

JODI: That is so beyond f’d up. (beat) Bucket of Grease?

LAYLA: Covering a bag of ideas. Jessica, in English. Bucket of Grease Covering a Bag of Ideas.

JODI: (looks away) Well. She’s an idiot. (beat) Are you coming?

LAYLA:
I believe there’s more to life than sitting at home and wondering what combination of vintage t-shirt and
jeans will make some boy I don’t even like want to make a move.
As this is still America, I fully respect your Constitutional right to believe otherwise.

JODI: Ah-ha… but I do like Joe.

LAYLA: Me? Talking about me? It’s not all about you. Not all the time. (beat) I-

JODI (pulls out her camera) I want tonight to be fun. I really do. And I want you to be there. (beat) And I sort of already paid for your ticket.

SCENE SIX

Back to the IM.

JODI: ChicFluxRock22: Hey, you there?

LAYLA: Away Message from Eowyn1R2RTA: Aragorn: Are you frightened? Frodo: Yes! Aragorn: Not frightened enough! What, exactly was Frodo supposed to say? Yes, I’m crapping my boots? Face with tounge stinking out.

JODI:
ChicFluxRock22: Why’d you leave?
ChicFluxRock22: Hello??
(beat)
ChicFluxRock22: Layla
ChicFluxRock22: you got my on my knees…
ChicFluxRock22: : laayyylllaaaaa…
ChicFluxRock22: I had a great time, hope u did too
(turns halfway)
ChicFluxRock22: oh, hey some great person gave me a camera, and then I took a picture of me and this
great person
ChicFluxRock22: but then she left…
ChicFluxRock22: so I couldn’t show her the picture
ChicFluxRock22: so.
ChicFluxRock22 wants to send a file: “jlconcert03.jpg.”
ChicFluxRock22: accept.
ChicFluxRock22: accept the file, biznitch!
ChicFluxRock22: oh crap, I think I just deleted them off the camera
SCENE SEVEN

JODI’s room. JODI is playing the guitar, LAYLA sits, stonefaced, reading.

JODI (practicing guitar) You know, I don’t care how loud I’m playing album. If it’s music from my dad’s CD collection, I really don’t think it qualifies as teenage rebellion. (Layla says nothing, flips the page) And tab here for a C… (twang of the guitar) Yeah. That, sounds just like Paul McCartney. (twang) It’s like Mom, it’s Lucy in the Sky with Diamonds, it’s not like it’s advocating drugs or sex, and she’s like, that’s exactly what it’s advocating, and I’m like- index finger to third string (twang) It’s like, it’s a song about a freakin girl in a boat on a river. I mean I know it’s a metaphor but really mom, it’s beautiful, you should hear what some of my CDs are about. (twang, sigh) Now I have to buy all my Radiohead CDs again. Or have Joe just burn them for me. He-

LAYLA: GOD! Joe, joey, joe-joe- joesph, Jehovah, joehalla, your mama joe, it’s raining Joe do you ever stop with the JOE!?

JODI:
(after a beat) This next one goes out to my number one fan… It’s called (twang, she sings)
Overrreaccttinggg… gg… that’s all I got. (Layla throws something at her) What? What? It’s conceptual.
(nothing) C’mon. That was funny.

LAYLA: Are you going to Prom with Joe?

JODI: Yeah. (clicks her tongue, Layla says nothing.) And. Yeah, I said yes. I mean, Why shouldn’t I? It’s not like time, like, stops or starts on the decision. It’s just Prom. You wear a pretty, pricey dress and everyone takes pictures and then… you kiss a little and tell them to back off and you go home and then you have school in two days. (smiles) He’s gonna wear a white tux, he said. And. We’re gonna. He said Martin would ask, you. If he knew you’d say yes. So. (beat) Okay. Well. I’m gonna go to sleep. And. (stands, at a loss) I guess. We’ll talk tomorrow. Or. Not. (turns off the light)

LAYLA: Can I use your computer?

JODI: Sure. Just turn off the monitor when you’re done. (Layla begins typing, Jodi stares up) Layla? If it’s a, deal, I mean. You’re my best friend, you know?

Layla stares at the monitor, says nothing.

SCENE EIGHT

On IM:

JODI:
ChicFluxRock22 has signed on. (beat)
ChicFluxRock22: Hey, Layz?
ChicFluxRock22: You there?

LAYLA: Eowyn1R2RTA: hey

JODI: ChicFluxRock22: what’s up with the pictures?

LAYLA: Eowyn1R2RTA: which

JODI: ChicFluxRock22: the pictures on my computer? That are now significantly different?

LAYLA: Eowyn1R2RTA oh, I photoshopped some of them

JODI: ChicFluxRock22: Yeah, I can see that- awkward face.

LAYLA: Eowyn1R2RTA: yeah I changed the lighting- the focus was way off

JODI: ChicFluxRock22: Look, the issue isn’t ChicFluxRock22: I mean, sure, lighting fine

LAYLA: Eowyn1R2RTA: Okay, so, I cut Joe out of one of them, haha- Eowyn1R2RTA: sorry

JODI: ChicFluxRock22: are you actually pretending you don’t know what I’m talking about? ChicFluxRock22: Layla, you cut yourself out of my pictures

LAYLA: Eowyn1R2RTA: ?

JODI:
ChicFluxRock22: Photoshopped, whatever. All the concert photos of us- you’re not there
ChicFluxRock22: not like cut out, like you were never there- altered
ChicFluxRock22: did you change these when I was asleep?

LAYLA: Eowyn1R2RTA: no

JODI:
ChicFluxRock22: these are the only ones I have, I deleted them off the camera
ChicFluxRock22: Layla, what the hell? seriously
ChicFluxRock22: are you pissed at me? Did I do something?
ChicFluxRock22: Layz, talk to me

LAYLA: Eowyn1R2RTA: when you’re at prom, can I stay at your place? Wait for you to get back

JODI: ChicFluxRock22: you’re not going?

LAYLA
Eowyn1R2TA: I’d really rather be somewhere so my parents don’t ask
Eowyn1R2TA: and I’ll be a safeguard, if you don’t come home I’ll call
Eowyn1R2TA: Joe alarm system, smiley face (beat)
Eowyn1R2TA: I’m sorry about the pictures it’s just a thing but I really need somewhere Eowyn1R2TA: I
want my parents to stop asking I’ll make it up to you ok? please
Eowyn1R2TA: if it’s not a deal
Eowyn1R2TA: and I need the camera

JODI:
ChicFluxRock22: k
ChicFluxRock22 has signed off
SCENE NINE

LAYLA sits in JODI’s room, waiting. She has put on a slight bit of makeup, and hugs her usual hoodie sweatshirt over a simple black dress. She looks over at the mirror, stares hard. Then we hear JODI coming up to the room.

JODI: (offstage singing) No one told me about her, The way she lied Well, no one told me about her- la la na nacried

LAYLA clicks something on the computer, then stands, smiling nervously. JODI stumbles in, giggling and singing at a whisper.

JODI: Well, it’s too late to say you’re sorry, How would I know, why should I care Please don’t bother trying to find her (closes the door, points at LAYLA) She’s not theeeeeeeeeeeere...

LAYLA: Hi.

JODI: (grabs Layla to dance) Well, let me tell you about the way she looked, The way she acted, the color of her hair-

LAYLA: Did you have fun?

JODI: Her voice is soft and cool, Her eyes are clear and bright, But shes not drunk...

LAYLA: I don’t think that’s the line.

JODI: I am, Hiccup. (hiccups, falls back on the bed) Oooohhh… I never thought something so stupid could be so fun…

LAYLA: (looks at the computer) I have something to show you.

JODI: I mean it was stupid, yeah, but, Joe’s friend snuck in this swing CD and we were dancing all over the place and Martin, total dork, spilled all of this punch all over his suit, and it was like, so sad and funny at the same time- you were totally right not to go with him-

LAYLA: C’mon, I have something to show you-

JODI: But you should have gone, you should have gone- it was so, we made fun of the Britney Horowitz and Meredith Miller and- oh. (stares) Wait. This is you, now. There. But that was then. (groans, rubs her head) sparkling grape juice my ass, Joesph William-

LAYLA: I put myself back in the pictures.

JODI: …yeah, I, I got that.

LAYLA: I’m sorry I took myself out…but now, I’m in there- from the right angle. The right light.

JODI: But I don’t get why you cut yourself out in the first place… and you spent tonight putting yourself back in? That’s why you needed the camera? (beat) Layla, this is weird.

LAYLA (quietly) I did it for you.

JODI: Yeah, and that’s… weirder. (beat, then Jodi laughs) Did Joe put you up to this? He said he’d burn a CD for you, actually, he said you should have come-

LAYLA: I don’t talk to Joe! When did this happen, when did he infect you- you didn’t care at all about this music, you don’t like it! I know you don’t! It’s cause of that stupid boy!

JODI: Uh. Yes, I do. Well before. Why are you shouting at me?

LAYLA: Joe. Joesph. Yeah, nice Jewish boy with a last name like Gallagher!

JODI: Whoa, mom-cop, I’m not going to marry him. He’s just my boyfriend.

A silence.

LAYLA: Boyfriend. You let him kiss you?

JODI: Maybe.

LAYLA: You let him get you drunk and feel you up?

JODI: What is wrong with you!? I went out and had a good time on my prom night, like you’re supposed too! You stayed here and screwed with photos from a rock concert! What am I supposed to do with that, Layla? What am I supposed to say other than f off!?

LAYLA: (sits, quietly) I’m sorry. I took myself out, but I put myself back in. For you.

JODI: It’s, fine, I just don’t understand… any of it. (Layla hugs Jodi, suddenly) Oh… okay. It’s alright. Layz, why are you crying? (Layla holds tighter, Jodi stiffins) Oh. I. Oh.

Layla moves in to kiss Jodi, Jodi expects this and turns her cheek, not unkindly. Layla sags, kisses her on the cheek. Jodi gently disentangles herself.

JODI: Layz. Go home.

LAYLA: I wanted…

JODI: Go home. It’s okay.

LAYLA: I put myself back in the pictures.

JODI: I appreciate it. Don’t think I don’t. Really.

LAYLA: But I-

JODI: You’re my best friend, Layz. (beat) My only best friend. Now go home.

Jodi turns off the light.

SCENE TEN:

Over IM. Late.

JODI: ChicFluxRock22: Hi.

LAYLA: Eowyn1R2RTA: Hello. (beat)

JODI: ChicFluxRock22: I just want to say- backspace backspace backspace. It was really messed up when-backspace backspace backspace- you’re still-

LAYLA: Eowyn1R2RTA: It’s no big thing. I’m not going to slit my wrists or kill your mom. I wish you and Joe luck. So, luck.

JODI: ChicFluxRock22: For what, our honeymoon???? ChicFluxRock22: I still want to be friends.

LAYLA: Eowyn1R2RTA: Well, it’s too late to say you’re sorry.

JODI: ChicfluxRock22: what did I do?? You’re the one that-

LAYLA:
Eowyn1R2RTA: How would I know, why should I care?
Eowyn1R2RTA: Please don’t bother trying to find her.
Eowyn1R2RTA: She’s not there.

JODI:
ChicFluxRock22: …right.
ChicFluxRock22: You know the thing is, Layla, I have other friends.
ChicFluxRock22: And I know you d-backspacebackspacebackspace

LAYLA:
Eowyn1R2RTA: I know.
Eowyn1R2RTA: And I have other friends.
Eowyn1R2RTA: Elves, Orcs and Starships. Oh my.

JODI:
ChicFluxRock22: ….the other girls are nicer to me now
ChicFluxRock22: but they’re dumb, they’re just so dumb
ChicFluxRock22: I miss you. I miss talking to you.

LAYLA: Eowyn1R2RTA: So talk. You’re not on my block list.

JODI: ChicFluxRock22: I N P E R S O N.

LAYLA: Eowyn1R2RTA: So call.

JODI: ChicFluxRock22: do you want to come over or not?

LAYLA: Eowyn1R2RTA: That position-backspace. I don’t work part- backspace backspace. Eowyn1R2RTA: No.

JODI: ChicFluxRock22: …. ChicFluxRock22: So, Luck.

User ChicFluxRock22 is not available.

LAYLA: Eowyn1R2RTA: Luck.

JODI: User ChicFluxRock22 is-

Layla hits her power switch. Blackout..
```

---

## IC-0642: The Princess and the P

- Title: The Princess and the P
- Author (byline): Steve DuBois
- Work: The Princess and the P
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS 1, ACTRESS 2
- Teaser before the introduction: No
- Spoken words (computed): 2729
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
ACTRESS 1:
MYNDA, PRINCESS OF LEXICO. Spoiled, but clever, and her heart is in the right place.
THE LETTER P. A mischievous consonant.
MAN-AT-ARMS. A particularly frustrated servant to the King.
MISTRESS OF LAWS. A servant to the King.
MINISTER OF AGRICULTURE. A servant to the King.
KING’S PHYSICIAN. A servant to the King.

ACTRESS 2:
CAEDMON, KING OF LEXICO. Elderly, kindly, and somewhat befuddled.
PRISICILLA. Chancellor to the King, and occasional provider of narrative exposition.
WITCH. A cunning woman and mistress of the magic of language.

AUTHOR’S NOTES
Scene breaks are marked with a #.
The witch’s spell, the specific manner in which the missing Ps are verbalized, and other such
production elements are left open to interpretation by the performers.

# [1]MYNDA: Oh, father! I’m so uncomfortable! I tossed and turned and didn’t sleep a wink all night! [2]CAEDMON: What, again? [sighs] For what reason, my angel? [1]MYNDA: It’s the P, father! I can’t sleep because of the P? [2]CAEDMON: [Nodding] A rubber sheet, then. I shall instruct your chambermaids to… [1]MYNDA: No, not that! The letter P! P is the source of all of your kingdom’s misfortunes, father! Is it not true that the words we speak shape the reality in which we live? [2]CAEDMON: In some respects. Discourse has power. The way in which we talk about people and things influences the way we interact with them. A lord who refers to his serfs as “dogs” will come to see them as less than human. A knight who calls his squire “boy” will raise up a less mighty warrior than one who calls that squire by name. And it is true that, here in the Kingdom of Lexico, words have even more power than they do elsewhere. [1]MYNDA: And what element is common to all of the crises that beset your loyal subjects, father? [2]CAEDMON: I suppose…money? [1]MYNDA: No, father. Think harder. [2]CAEDMON: Alcohol? [1]MYNDA: No. [2]CAEDMON: Millennials? [1]MYNDA: [Sighs, pulls out a scroll, hands it to the king] I made a list. Behold, father. The source of all our troubles. [2]CAEDMON: [Reading] Pestilence…poverty…prostitution…patriarchy? [1]MYNDA: Oh, yes, father! I am so tired of the world being run by old while men who set arbitrary rules! [Caedmon pauses and blinks a bit, then goes on reading.] [2]CAEDMON: Plague…pneumonia…pets in restaurants. Hmmm. I perceive your point. [1]MYNDA: It is the Ps, father! The Ps oppress us! Use the power granted to you as king! Instruct the royal wizards of Lexico to unleash their word-smithing energy to police our language! Let every P be stricken and removed, that our people may prosper in the paucity of their plotting! May a purge become your urge! [2]CAEDMON: Er…alas, beloved. I dare not. [1]MYNDA: But father! [2]CAEDMON: But me no buts, my sweet. This sort of thing has been attempted before. Even applied sparingly, word-magic is dangerous. It rends the fabric of reality itself. A change of such magnitude as you suggest…there is no forseeing the risks. No, my dumpling. I dare not. [1]MYNDA: But…but FATHER! [2]CAEDMON: I dislike these buts, and I cannot lie. The old white man has spoken, daughter. In time, you will come to see the wisdom of restraint. In the meantime, return to your bedroom beside the royal gardens. You will rule this kingdom one day, but not tonight. [Mynda scowls and stomps away] [2]CAEDMON: Now, that’s trouble. But I suppose it can wait until morning. [He squirms in discomfort]. Ah…prostate. Another oppressive P word. It seems a purge may be necessary after all. To the royal chamber pot…

[Intro here]

[2]PRISCILLA: I, Lady Priscilla, had served as the King’s chancellor for many years, and I knew that he was correct to predict trouble. For all seventeen years of her life, Princess Mynda had been spoken to with deference, and the words had shaped her. She was a haughty girl, perhaps a touch spoiled, with a will like a rod of castle-forged steel. But she was also shaped by the compassion and courtesy she had been shown. And as she thought upon the plight of her future subjects—of their pain, their panic, their peanut allergies, of their every peril and peccadillo, her heart swelled with pity. So that very night, she mounted her pony and rode forth, into the woods, to consult with the word-witch… [1]MYNDA: I have come for your help, old crone. [2]WITCH: What would you have of me, princess? [1]MYNDA: [Gasps] You know who I am? [2]WITCH: Nothing is hidden from the gaze of a cunning woman. The way you sit side-saddle on your pony bespeaks years of training. Your posture, regal and erect—the bent back of a peasant could never straighten so. Also, there’s also that diamond-studded tiara you’re wearing. The subtle clues pile up. [She grins wickedly] Care for an apple?

[Mynda shakes her head and dismounts] [2]WITCH: Ah, well, worth a try. [She clears her throat.] Know, princess, that I am bound by an ancient formula: FOR MAGIC OR FOR SAGE ADVICE, ALL WHO COME HERE MUST YEILD THE PRICE. Yes, I am bound to follow every letter. The magic of language comes dear indeed, and in exchange, you must give up something dear to you. What would you have of me? [1]MYNDA: The Ps, madam! I would have you round up every P in Lexico. Gather them together, and do with them I know not what. But rid us of them! [2]WITCH: Ah, yes. A difficult letter, the P. One must mind them, as well as the Qs. An understandable concern. But this is no small task you ask of me. FOR MAGIC, OR FOR SAGE ADVICE, ALL WHO COME HERE MUST YEILD THE PRICE. The price here will be quite high. [1]MYNDA: How high? [2]WITCH: A kidney, I think. [1]MYNDA: A kidney? [2]WITCH: I get very few visitors out here. One grows tired of lentils and forest roots. A bit of protein in my diet will do me good. [1]MYNDA: Oh…very well. [2]WITCH: Excellent! Right though here, Princess, in my cottage…Yes, just past the Room of Unspeakable Objects in Jars…mind the flying monkeys…ah! Here it is! My loom… [The Witch weaves a spell upon her loom. At the end of the spell, THE LETTER P emerges, stretches, looks around, giggles gleefully, and runs away.] [2]WITCH: And…done! When the sun rises in the morning, the change will be achieved! The payment, please. [The Witch holds out her hand. Mynda frowns.] [1]MYNDA: Oh, bother. I just had them redecorated! But anything for my people… [She reluctantly removes her left kidney and places it in the witch’s hand.]

#

[2]PRISCILLA: Mynda strode out into the night, where her steed returned her to the palace, and to her bedroom by the royal gardens. The next morning, the sun shone in through her window. Had it all been a dream? [Mynda yawns and stretches.] [1]MYNDA: *ersimmon. [She starts in surprise] *achyderm. [She smiles widely] *eter *i*er *icked a *eck of *ickled *e**ers. It worked! Wait until I tell father! [She goes racing out into the gardens, then as she sees them, her face crashes in dismay.] [1]MYNDA: What…my flowers! They’ve…they’ve been vandalized! To the council chamber! Father! Father! FATHER!!! [She arrives in the council chamber and screams. Lady Priscilla stands in front of her, decapitated, but perfectly calm and addressing the court.] [1]MYNDA: Oh my God…Lady *riscilla...she’s been deca*itated! But, it seems, none the worse for it… [2]PRISCILLA: [Headless, addressing the King]: It is as I feared, your highness. Re*orts are flooding in from across the land as we s*eak, and the situation is identical throughout Lexico. Two in every ten citizens have vanished overnight, and everyone who’s left seems to have a s*eech im*endiment. As best we can tell, the removal of a letter of our al*habet has wrought changes u*on the reality which that al*abet codifies. Wherever the letter has gone missing, reality has shifted accordingly. Hence: the immediate loss of two tenths of the kingdom’s *o*ulation, including an eighth of the *easants, who do all the actual work. [1]MYNDA: Lady *riscilla…my…my flowers… [2]PRISCILLA: The flowers of your garden, your highness? I assume the daffodils and violets are unaltered? [1]MYNDA: Yes. But the *etunias and the *eonies. They’re… [2]PRISICILLA: Missing their buds. Reduced to stems. Wherever the letter a**eared at the beginning of a word, the to* of the object in question has gone missing. In those cases, and in all others, the object in question has been shortened in *ro*ortion to the length of its name. I sym*athize with the loss of your flowers, highness, but believe me… [she gestures to her missing head] …others have it worse. [A man-at-arms emerges, glances down at his crotch, then stares angrily at Mynda] [1]MAN-AT-ARMS: Indeed. [2]PRISCILLA: Yes. And the consequences don’t sto* there. [1]MISTRESS OF LAWS: Crime is ram*ant throughout the ca*ital! The *olice force finds itself shorthanded!

[2]PRISCILLA: And it gets worse. [1]MINISTER OF AGRICULURE: The harvest! A full fifth of the cro*s have disa**eared from the fields! We will surely starve come winter! [2]PRISICILLA: Some realities have been abbreviated by the absence of the letter. Others have been altered. For when the absence of a letter transforms one word into another, the world transforms with it… [1]MINISTER OF AGRICULTURE: Our fruit orchards are ruined! Half of the trees are full of ale, and half are full of ears! Now half of our workers are too horrified to work, and half are too drunk! [2]PRISCILLA: Was this what you wanted, *rincess? [1]KING’S PHYSICIAN: Our doctors cannot administer *ills to their *atients! The very medicine itself makes them ill. [2]PRISCILLA: A most sickening state of affairs. [1]MARSHALL: The narrow mountain *ass that connected our kingdom to Slibola has been transformed into a giant *air of buttocks! [2]PRISCILLA: It occurs to me, your highness, that had you been with child at the time this occurred, you would now be regnant…which is to say, a ruling queen. Was that your intention? Was this an attem*t at a cou*? [1]MYNDA: I would never do that to father! I just wanted to hel* the citizens of Lexico… [2]PRISICILLA: And so you have. They are in hell. What have you done, *rincess? And what will you do to make things right again? [Mynda ponders the situation. And slowly, she comes to a conclusion.] [1]MYNDA: I can…I can fix this. I’ll need…I’ll need some su**lies from the kitchens. And a wand, from one of our word-wizards. [2]CAEDMON: A wand? You are royal! You are untrained in the ways of magic! [1]MYNDA: I won’t need to be. Trust me, everyone. I have a *lan.

# [Mynda, behind the wheel of an automobile, revs the engine, then hits the breaks. The Witch observes her arrival. All around her cottage, newly-enslaved Ps are hard at work, thatching the roof, mowing the lawn, whitewashing the fence, and so forth.] [2]WITCH: Back so soon, *rincess? And regally mounted on a…1976 Buick, I see. Whatever became of your *ony? [1]MYNDA: Headless, as you well know. Fortunately, the fish in my father’s ornamental *ond were all transformed into cars. Madam, I have come once again to bargain, and to liberate these consonants from their confinement. What have you done to them? [2]WITCH: I think not, my dialytic damsel. You cannot offer me your other kidney and ho*e to survive. Besides, I have come to enjoy the service of these letters. Roof re*air, cooking meals, yardwork…they have *roven most useful! [1]MYNDA: Monstrous! Look at them, sweating in the hot sun, dragging their sad little tails behind them! Come now! Remember the creed that governs you! Let us strike a deal! [2]WITCH: Go home. I have mastered the magic of words, and I find yours tedious. [1]MYNDA: Very well. I came to buy, but if you will not bargain with me, I shall liberate these letters by force! [She draws a wand.] [2]WITCH: You fool of a girl! You cannot be serious! I have dueled the mightiest masters of linguistic magic! Satyrs, demons, and lawyers have fallen before me by the score! You cannot ho*e to best me. [1]MYNDA: [Pointing her wand] En garde, madam! [2]WITCH: Oh, very well. [She draws her own wand.] Are you sure you want this, girl? [1]MYNDA: I renew my offer to buy. [2]WITCH: Not likely. On three, then. One, two, and…ALACAFRAGILASICARAZAM!!! [There is a short pause. Then, The Letter P emerges and, delighted, runs squealing away from the witch.] [2]WITCH: Still alive? Impossible. But…wait…how can I say that word? [Noticing the fleeing Ps] Come back! Come back, you! What have you done, girl? [1]MYNDA: Why, I offered to buy. And you responded with… [2]WITCH: With a spell! A fatal spell! A word of sure and certain power...A sp… [1]MYNDA: Not a spell, under the circumstances. Rather: a sell. And it was a pleasure doing business with you. [She puts her wand away and turns to go.]

[2]WITCH: GRRRAAGGGH. Oh. But highness, aren’t you forgetting something? We made an exchange. A legally and magically binding contract. You owe me a kidney…and it is a debt you cannot pay without forfeiting your life. I may be, suddenly, an unlettered woman, but still, I shall dine tonight. And not just on a single kidney, oh no indeed… [1]MYNDA: We did have a deal. And I shall pay you all that I owe. [She reaches into her car, and withdraws a small package, which she tosses to the witch, who opens it.] [2]WITCH: This isn’t a kidney! This is rice! What, do I look vegan to you? [1]MYNDA: [Climbing back into the car.] I believe you once told me that you operated under an ancient formula, which you must follow to the letter. And our deal was made under unique phonetic conditions, madam. Speak, if you wish, the words of your ancient creed. The words you spoke when we made our deal. And tell me what I owe. [As the witch speaks, Mynda starts up the engine.] [2]WITCH: For magic, or for sage advice, all who come here must yield the…must yield the… [She realizes her mistake, and raises her wand.] GRRRRRRRAAAAAAAAAGH!!! [Mynda accelerates away.]

#

[2]PRISCILLA: In truth, things in Lexico never did get completely back to normal. A few Ps decided that they enjoyed the heady taste of freedom, and rather than returning to their assigned roles, they took to the open road, taking up life as hitchhikers, highwaymen, troubardors, and rogues. And every now and then, a blank space would turn up where a P was needed, and a suffering typesetter would shake his or her fist in the direction of the capital, cursing what had become known as Mynda's Mistake. But the worst of the crisis had passed. The missing citizens returned, as did the crops and missing appendages. Mynda’s father and I were quick to forgive her. And when she finally came into her kingdom, she ruled with compassion and wisdom— recognizing the power of words, but rarely seeking to police them. Instead, she dealt directly with the problems they described. [As she speaks, The Letter P emerges from behind her, and attempts to sneak away.] [2]PRISICILLA: Neither the problems nor the problematic language were ever completely eradicated. Nevertheless, all involved lived more or less ha**ily… [She notices the missing letter, spots the P, and shakes a finger at it. It sighs and returns to her side, rolling its eyes.] [2]PRISCILLA: happily ever after.

[She nods with satisfaction. Priscilla and the P share a fist-bump.]
```

---

## IC-0643: the ultimate drama

- Title: the ultimate drama
- Author (byline): kate garlock and carrie taylor
- Work: the ultimate drama
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1055
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
2: (autistic) Brother mikey! (realizes “Brother Mikey isn’t there, becomes more frantic) Brother mikey!
Brother mikey! Brother mikey! (Brother Mikey enters, “Brucey” becomes upset and less frantic) I called
you, I called you!
1: (concerned) Brucey, you okay? What’s the matter?
2: I called you, I called you...
1: I didn’t hear you, Brucey, I didn’t hear you, (frustrated) I said I didn’t hear you! I’ve had it!
Both: (PAUSE. In a frozen postion then turn to audience) (Hum Mentos theme)
1: Mentos. For when your brother just won’t leave you alone, here’s one way to keep cool.
2: Mentos. The freshmaker.

(Both do thumbs up & smile)

(1 begins to present to “group” while 2 is distracted by various things. Both as new characters.) 1: Hi.... I... I’m Alice. Thanks for letting me come here. I just needed to talk, and I guess AA isn’t a bad start. You see, I just got home from a concentration camp where they just don’t have the kind of group treatment you’d like for alcoholism. Or the alcohol. Anyhow, now that I’m back in the states and... hey. Aren’t you supposed to be listening? 2: (snaps to attention) I’m terribly sorry, I have a mental disorder. 1: Which one? 2: ADD. 1: Mentos? 2: No thanks- (looks out a “window” )OOH! Birdie! (moves to follow bird then character two acts as a bird while character 1 turns into a person driving a car which hits the bird.)

(flash to 2 as bird getting hit by 1 driving a car)
1: (looking out windshield as he drives the car) What the..?
2: (child in the backseat) Hey mister, what was that?
1: Shut up kid! I gave you your candy, now be a good little abductee.
2: Okay! (eats candy)
1: And stop twitching
2: Sorry... I have schizophrenia. And ADD!

1: You’re damaged? That’s it, get out!
2: Ohhh....(Steps out of car then sees a cat) Hey look at that!
1 & 2: (as a cat) MEOW
1: (as patient Berta, sitting in an office with her therapist) Was that the sound of a kitty? Ay me. I
remember kitties from my old country.
2: (as therapist taking notes/ interviewing) Tell me about your daughters
2: Well Grete was anorexic and Hannah, we feared, was bulimic. Sylvia....
1: Sylvia? What was she like?
2: Well… something like this:(spin to Sylvia character) Hello. Talent… I have none. (spin back to patient
Berta) She had OCD. With schizophrenia. And ADD. Anyhow, we were all sitting together when suddenly,
there came a knock at the door. (Flashback sequence)
2: (as German officer) Knock knock! Let me in!
1: (Flashback Berta) Not by the hair on my chinny chin chin!
2: Let me in or I’ll huff and I’ll puff and I’ll blow your house down.
1: The next thing I knew, I was on a train, headed for the heart of Germany. When we got there, my
husband and I were separated. We were told to work.
2: Work!
1: Those who didn’t work would be shot...
2: Those who do not work will be shot.
1: After a few days, I had noticed that officer Schfinctinhaur had taken an unusual interest in me. I feared
for my life. You can imagine my terror when he caught me alone one night...
2: Mmmm Hmmmm Hmmm! Why 27-56-02. What a pleasant surprise. Come with me!
1: He led me into his quarters, I had no idea what was happening.

(Both characters face back and say, “bow chicka wow wow!” Then Character 1, or “Berta” turns back around.) 1: A month later I, I found out that I, I was pregnant. Don’t get me wrong, I still loved my baby, it was still my baby. The problem was, hiding it. Months passed and, needless to say, they noticed. I prayed and prayed for help which turns out is only a phone call away.

(Character 2 turns around)
2: (some sort of “technician”) Hi.
1: Who are you?
2: (hands a business card)
1: Abortions R Us?
2: Quick and Easy for the Sleazy.
1: (disgusted) That’s terrible!
2: I know, we’re working on a new slogan. Anyway, now I know that button is around here
somewhere…(Begins searching for a “button” origionally the intention was a belly button) oh there it is!

(Pushes button on stomach and pulls baby out.)
2: Bye bye now. (Turns around and drops hands to sides)
1: You just dropped my baby!
2: Oh no, see I was ending the scene…
1: No, you dropped my baby on the ground!
2: Oh sorry, let me clean that up for you. Oh, sorry.

(Picks up fetus)
1: (Fetus) fetuss! Hi (giggle)
2: Hey, do you wanna play a game?
1: (fetus) Uh-huh.
2: Okay (throws into air, pulls out shot gun and shoots fetus)
1: (fetus) Fetus…..Sploosh.
1: (Pops back to patient Berta) Sorry, where were we??
2: (Doctor) I’m sorry, I have Alzheimer’s, OCD, schizophrenia, and ADD…do you hear that?

(“Charge” theme is played)
1: (as baseball announcer) Kawabata is one away from a perfect game.
2: (as baseball announcer) Kawabata set up, delivered and - ! Home run.
1: Which is followed by a single, which was followed by a triple.
2: Kawabata left the game.

1: And for the first time since his suspension, Shane Munget is in. Shane seems intense on the mound.
2: Batter up is Davey Battle.
1: He throws his first pitch.
2: It hit Davey! Davey is down.
2: (vendor with back to audience) Popcorn! Peanuts! Get your…
1: (fan) Hey, I’ll have some popcorn.

(Popcorn is thrown by vendor who spins around to become another fan who is hit by peanuts.)
2: (Scandinavian fan) Ouch. Yah sure, it’d hit me. Society always trying to keep my people down.
1: What? What are you talking about?
2: We Norwegians are always getting the shaft but nobody cares…
1: Oh, that would explain the sweater.
2: I know you be hating on my lutefisk.
1: I know, we could write a speech piece about how society holds your people down and then guilt trip
the judge into giving us pity points….
2: I don’t know, it seems like kind of a low blow. How about a mental disorder.
1: Alright (autistic character from the beginning) Brother Mikey….
2: (straight, no character addressing fellow actor) No wait, I hate it when people rip off other people’s
pieces…
1: Me too.
2: Boom
1: Chick
2: Boom Boom
1: Chicka
1&2: (begin “beat box/rapping”) Boom Chicka-ah Boom Boom Buh Chicka-ah
1: Wait, what good is pointless rapping in the middle of a piece?
2: Actually, I just thought it would be funny to see you try and rap. It was pretty sad, though.
1: I bet I could beat it…
2: How?

1: I don’t know if I should tell you this…
2: If you feel you must, you must
1: (pauses) Alright, (melodramatic) I’ve got pink eye!
2: (also very melodramatic) No!
1: Yes, and this morning I stubbed my toe.
2: (gasps)
1: But that’s not all, I’m pregnant…
2: I can’t believe it
1: … With my brother’s baby.
2: The agony.
1: And I fear the baby might have syphilis,
2: The horror.
1: And pink eye.
2: This is all so dramatic!
1: And did I mention that I can tell from the way the baby is moving, that he’s horribly mutated.
2: I don’t believe this, what are you going to do…
1: Wait, that’s not all…
2: Go on
1: I…I…I didn’t shop around for the best prices in auto insurance
2: Oh that’s terri…wait, what?
1: I know, I can’t bear to live with myself.
2: I wouldn’t be able to either, sicko.
1: Hang on, at least I’m not the one who brought up the autism.
2: (nostalgically) Yeah you’re right (autistic character) Brother Mikey, brother Mikey.
1: Brucy, that’s it (steps back) I can’t handle this.

(Conclude singing Mentos theme song: Doesn’t matter what comes, fresh goes better in life, with Mentos fresh and full of life. Fresh goes better, Mentos fresher, fresh goes better with Mentos fresh and full of life.) 1: Mentos, The Freshmaker.
```

---

## IC-0644: UNFUNNY

- Title: UNFUNNY
- Author (byline): Michael Beede
- Work: UNFUNNY
- Publisher: Mushroom Cloud Press
- Publication date as stated: 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1675
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
“Unfunny” was originally intended to be performed by one woman on a clear stage, and all props are intended to be pantomimed. Bearing that in mind, the characters’ descriptions are as follows:

Cast List (In Order of Appearance)

Norma: Bland, confident, and sometimes overbearing female in her mid-twenties. Her frustration with society in general has driven her to a number of eccentricities.

God: Slightly neurotic version of the creation of the universe. Sounds somewhat like a stereotypical elderly New York Jew.

Eve: Naïve, inquisitive, bold and beautiful, woman. Very controlling and demeaning towards Adam. First woman on earth.

Adam: An idiot. First man on Earth.

Duck: Seductive French mallard.

Caller1: Nameless, faceless, insecure woman.

Laura: “Ninety-seven year old testosterone hunting, respect crushing, cantankerous psychologist from the inner most depths of Dante’s Inferno.”

Caller2: See caller 1, has a fatal disease.

Caller3: Single father of three.

Girl: Seven brain cells short of a coma. Ditz.

Olga: A very masculine and brutish woman. Dresses in flannel and jeans.

Caller4: Frantic woman, easily offended.

Optional Props List

Bookshelf
Books
Kleenex
Telephone
Apple
Scene opens with Norma turning the pages of a book one by one, reading a line or two
and then turning again, tears out a page, blows her nose with it, folds it in half, places it
back inside the book, then places the book on a library shelf.

NORMA. Oh… hi. You uh… saw me… with the… yea. Oh who gives a funky chicken? You think that’s funny? Holy wounded Moses! That’s the only way you’ll think I’m funny anyway. I mean look at me! No, not there! Here. In my eyes! I wanna talk eye to eye wit you on this, not eye to boob. See that’s the thing; that’s why broads aren’t funny… because we are women. And I can say “broads” because I am one. You know, broad, chick, estrogen bag. I can say that, but I can’t be funny. Well I can, but no one else thinks so. Why aren’t women funny? Give you one solid answer. Eve. It all started with the first one.

GOD. Adam, Eve, you can do whatever you want. ANYTHING. Just don’t eat of the fruit of life. The consequences are so far beyond your comprehension that if I even gave you a hint you would break down into your molecular structure and reform as a Richard Simmons Look-alike.

EVE. What’s a Richard Simmons?

GOD. You don’t want to know. Just remember I am the creator and controller of the Universe, and whatever you do, DO NOT EAT OF THE FRUIT.

EVE. Don’t eat the fruit. Don’t eat the fruit. Don’t eat the fruit.

ADAM. Look a butterfly! PRETTY!

EVE. Shut up Adam.

NORMA. Now this is where the story has become a little inaccurate over the past 5000 years. See, the serpent wasn’t actually a snake, it was a duck. A French duck. Moses thought that a duck might not be intimidating enough to instill fear in the hearts of God’s chosen people. So instead, he rewrote it as a python.

DUCK. Le quack quack. You know…. You wanna eat that fruit right?

ADAM. God said not to eat da fruit.

EVE. Shut up you. Go on duck.

DUCK. The fruit… it will let know of what God knows.

ADAM. YAY FRUIT!

EVE. But…but…God told us not to eat it though.

DUCK. Oh what does he know… So he created the universe and all that dwells within it big freaking deal.

EVE. Well… he is God…. But you are a Talking Duck. I see God everyday but this is the first time I’ve seen a talking duck…..

(Adam and Eve take a bite of the fruit.)

ADAM. Nummy in my tummy!

GOD. EVE WHAT ARE YOU DOING!?!

EVE. (with mouth full) Nothing.

ADAM. I’M NAKED!

GOD. Thanks for the hot tip, Adam. For this I banish you both from paradise! Woman, you shall now in childbirth pass a grapefruit through your bellybutton. Adam, that’s like passing a barbed wire kidney stone. Oh yea, and you are both going to DIE! Well, not right now but eventually. Oh yea, and Eve… you don’t get to be funny.

NORMA. See it’s all right there. Most of it. Some of it. OK, so it might have happened. The fact is, that women don’t have what it takes to be funny: beat Huzzah. Huzzah is that oomph with hishaw and the pizzazz. The razzle dazzle blat. I’ve lost you, haven’t I? Huzzah is that line between self awareness and self-ignorance. Huzzah is the ability to laugh at yourself when everyone else is just walking out. Without huzzuh, someone telling jokes is just sad and pathetic, like Carrot Top. Huzzah is what establishes a personal and respectful connection between a comic and the world. Most women, however, sacrifice their huzzuh to the likes of N’sync and makeup. How can we not when we have someone like Dr. Laura as one of our supposed role models? Now for those of you who don’t know, Dr. Laura is ninety-seven year old testosterone hunting, respect crushing, cantankerous psychologist from the inner most depths of Dante’s Inferno. I call her Lucy… short for Lucifer. I can’t understand why these people call her show. Some nice, unsuspecting housewife calls her up looking for advice about her Schizophrenic masochistic Ridilin injected devil-child, and Lucy tells her to stop whining, take an industrial strength Midol, and buy her new book, Embracing the Demon Within. A typical call goes something like this:

CALLER 1. Hi Laura, I have a problem DR. LAURA. Yea you do.

CALLER 1. Umm… k…

DR. LAURA. Spit is out Betty Cleaver, I only have so many angry ovaries.

CALLER 1. Well, I think my Husband is having an affair.

DR. LAURA. You deserve it for not keeping him happy in bed you slack jawed Yokel. Goodbye. Next caller you’re on the air and in my world now princess.

CALLER 2. Hi Laura, I have a rare tropical disease, and I have three months to live, what should I do.

DR. LAURA. Drink. Next Caller.

CALLER 3. I’m a thirty-six year old single father of three—

DR. LAURA. This is just Fate telling you it hates you… Now buy my book you deadbeat dad.

NORMA. RAAHHHHHHHA! Hold on, one second (turns around, screams again). I apologize for that outburst I’m just a little upset. But I’m not bitter… really. It’s just that, that’s what I mean about huzzuah. We voluntarily subject ourselves to this kind of torture and take it all to heart. I mean there is on one hand the Hilary Clinton-esque ice princesses tearing the very fabric of our society with their demonic war cries, while on the other hand you have the Bouncing Barbie Dolls that have had enough plastic surgery to make Sunny Look like Cher.

GIRL. Like, I have to go in for a check-up with my plastic surgeon; I want to get the wrinkles in my brain smoothed out with some botox. Oh yea, and I’m getting collagen implants in my chin.

NORMA. So-called female comedians, however, just sit and complain about guys and their period.

OLGA. Get it? The word men is in the word menstruation! They both must suck!"

NORMA. For the love of Michael Bolton, the only funny woman on earth is Ellen DeGeneres... and she's well.... you know... uh...from the Louisiana. No really, she is. The truth is, women will never be able to tell a good joke until they can walk down the street bald, beer belly sticking out, wearing cabana shorts and a Van Halen t-shirt and still believe they look good. Or at least not care. I've got to be honest with you, yea, I've given some silly little reasons as to why women aren't funny, but here's the truth: We are as irrational as Dan Rather in a leotard. We spend so much time trying to figure ourselves out that we can't even begin to make fun of somebody else. We aren’t getting anywhere comical anytime soon. Men, let me give you a little tip: GIVE UP! One day we'll like you, the next day we don't. I know women that have fallen in and out of love during a single commercial break. We don't have the answers, we don’t have the way, we have PMS. You won't get anywhere comical with us, I promise. We don't make any sense. We can't be funny if we are are worried about missing our monthly visitor-- Child support. You want irrational? I hate my boyfriend because my dog is going bald. Want to know why I'm upset with my mother? So do I. Know what ticks women off more than anything? Me neither. Just as a sidebar men, don't think for a second that our place is in the kitchen because I swear to you that we are all liable to stab someone in the face with a shrimp fork. Half my friends can't choose what state they're in, let a alone a state of mind, and you want us to tell JOKES! We are too busy continuing the human race by giving birth to and raising mankind, all while working nine to five to support our children to allow the trivial matters of Comedy Central to bother us. Excuse us for sticking with the practical and the useful while men spend their days in a fanciful daze. I have been willing to admit our many faults and flaws, but our strength and struggle is more than we can ever laugh at. So listen, maybe after we achieve world peace, invent the car that runs on water, and find the cure to cancer women might get around to pumping out the next Jerry Seinfeld.

CALLER 4. Dr. Laura, I just watched this horrifically offensive comedy bit in which some girl had the audacity to poke fun at women… it hurts… I ate an entire box of bon-bons and it still hurts. Help me.

DR. LAURA. Well, look at the bright side, at least you’re not a man.
```

---

## IC-0645: Unplugged

- Title: Unplugged
- Author (byline): Naomi Yang
- Work: Unplugged
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: INSTAGRAM, SNAPCHAT, TUMBLR, IMESSAGE, MUSIC.LY, SNAPCHAT & INSTAGRAM, SETTINGS, ALL, CAITIE, CAITE, MARY-KATE
- Teaser before the introduction: No
- Spoken words (computed): 1440
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
INSTAGRAM is alone on an empty stage, crying

INSTAGRAM: Hi IGTV…. I just wanted to let you know…. FACEBOOK IS DEAD! This is like-so sad!! ENTER SNAPCHAT, who tries to leave upon finding instagram weeping. Finally he comes over to comfort her with obvious awkwardness.

SNAPCHAT: (while patting her back or another sympathetic gesture) It's okay Instagram, his security was getting weaker. We’ve all known for a long time now. I blame Zuckerberg.

INSTAGRAM: (filming on her cell phone) Oh my god snapchat. I’m like, SO sad. (sobbing) facebook is dead! He died, like, right (points to one side, only to realize it is the wrong one. She switches the side she points to.) here!

SNAPCHAT: (getting progressively more annoyed) You know nobody’s gonna see that if you put it on ur stupid TV.

INSTAGRAM: It's fine. 5 minute crafts will repost it and it’ll go viral.

SNAPCHAT: Ugh. Whatever, dweeb. POSE FOR STREAKS! snapchat pulls out his own phone, and p;laces it so that both he and instagram are in the “photo”

INSTAGRAM: I’m like so sad (smiles through her “sadness” and makes a peace sign)

SNAPCHAT: so Twitter called. (looks confused) Tweeted? Whatever. She wants us to run an investigation so we can find out who killed facebook. You in? instagram, who had stopped crying, begins to fan her eyes again.

INSTAGRAM: I’m like, too sad to figure this out. Plus, investigating doesn’t fit my feed. But don't let little old me stop you. ENTER TUMBLR

SNAPCHAT: Ugh. Tumblr? Can you help?

TUMBLR: (inhales rapidly) I mean, I would, but I’m like a refrigerator with a burst pipe. Cool, but broken inside. (looks outward at an unknown entity.)

SNAPCHAT: What? Fine. I’ll do it by myself. And I’m keeping you guys at home updated, through my super cool feature that instagram STOLE FROM ME, snapchat stories. TRANSITION SCENES

SNAPCHAT: Hey guys, were in perp number ones crib. Say hello to the fans, imessage ENTER IMESSAGE, who pops out of nowhere. As soon as she begins to speak she doesn't stop for air.

IMESSAGE: hi! Wanna see my ponies? my-best-friend-told-me-that-she-really-likes-them-my-favorite-one-is-rainbow-sparkle-see-she’s-that-one-there-with-the-black-mane-and-she’s-really-cool-I-like-her-cause-she--

SNAPCHAT: That's great….. where were you at the time of facebook's death? beat

IMESSAGE: Who’s Facebook? (says Facebook like she’s trying to pronounce it)

SNAPCHAT: You know, the platform that was murdered yesterday?

IMESSAGE: ooooooh…. Yeah, I don't know who You’re talking about. But all day yesterday I was texting my best friend. She-thinks-my-pony-is-really------

SNAPCHAT: okokok. Whomst?

IMESSAGE: musically. She-has-this-friend-and-she-dances-too-and-----

SNAPCHAT: oh god. (facepalm)
TRANSITION SCENES
snapchat looks tired, but enthusiastic to continue his search. He rings a doorbell, where
MUSIC.LY ENTERS.

SNAPCHAT: Hey, Music.ly!

MUSIC.LY: HIIIIIIII (this can continue in a singsong voice as long as the actor can maintain it)

SNAPCHAT: Great. Please state for the story where you were yesterday, after you were texting imessage. You were texting imessage, weren't you? as he speaks, snapchat edges towards music.ly eagerly.

MUSIC.LY: (nods to the last question, the pauses to think.) Have you heard the song No Tears Left To Cryyyyyyy? (again the ending can be held as long as the actor can)

SNAPCHAT: oh yea, that song is a bop-- the next section can be acted out, or a spall choreographed section can be added to go along with the words.

MUSIC.LY: I was lip syncing along, jigilling the camera around, and basically making it impossible to listen toooooo. (this note should be held as well)

Snapchat, angry and exhausted from the dancing, goes to the door in defeat.

SNAPCHAT: this is why your funding is going to Tik Tok. (he hands her a business card.) Call me if you think of anything.

MUSIC.LY: (throws or jams the business card into a pocket.) How rude! TRANSITION SCENES a worn out snapchat drags himself to a doorway and presses the buzzer.

TUMBLR: Come on in. It's just me, being depressed.

SNAPCHAT: If you’re depressed you should really go talk to someone.

TUMBLR: But why go to therapy when I can vent about my troubles online for the many broken souls to see?

SNAPCHAT: that sounds unhealthy, Tumblr.

TUMBLR: I know right? Lol.

SNAPCHAT: I’m not joking- whatever. Where were you when facebook was killed?

TUMBLR: Why? Am I a suspect? That's so cool. (comes uncomfortably close to snapchat)Hello snapchat. I am the one and only suspect.

SNAPCHAT: (whiny) stoooop. This is serious man!

TUMBLR: Fine. I was listening to SAD! By xxxtentacion. Press f to pay respects. as he speaks, Tumblr makes a respectful gesture towards the sky.

SNAPCHAT: O-my god, is everyone on your platform basic?

TUMBLR: (considers this a moment, then concedes) Well, yeah. Kinda.

SNAPCHAT: So it wasn't you.

TUMBLR: NO! It wasn’t me.

SNAPCHAT: (frustrated) THEN WHERE DO YOU WANT ME TO GO, WISE GUY? HUH? tumblr thinks for a second and then has a lightbulb moment

TUMBLR: Oh. My. God. Why don't you visit My Space? He knows, like everything. He’s been here forever. He MUST have some idea. And Instagram can come with you. She has always wanted to meet him.

SNAPCHAT: Whatever. At this point, anything sounds good. TRANSITION SCENES ENTER SNAPCHAT AND INSTAGRAM, who stand outside of an older version of the houses out imessage and music.ly. Snapchat tries the buzzer, but instaram has already opened the door ar gone inside. Snapchat follows behind her.

INSTAGRAM: Why are we here?

SNAPCHAT: Didnt tumblr tell you? We’re here to investigate My Space. Apparently he might know something about Facebook’s murder. (snapchat runs into something nasty, a cobweb or dust.) Ugh. So instagram. I feel like you’ve stalked some people before. Where would My Space be? Both begin to go through My Space’s house. Everything is dusty an old. Snapchat opens cabinets and old books. Instagram begins to dust surfaces. She begins to cough when she notices something and jumps back.

INSTAGRAM: gasps

SNAPCHAT: what?

INSTAGRAM: oh my god. My Space isn’t here anymore!

SNAPCHAT: What do you mean? Instagram latches on to Snapchat’s arm.

INSTAGRAM: He’s gone.(steps back) Like, dead.(steps back) Died in the early 2000s! TRANSITION SCENES- snapchat is alone on the stage

SNAPCHAT: WHADDUP SNAPCHAT viewers!!! After hours of...strenuous work, I have narrowed the list to…. Drumroll please, INSTAGRAM AND SNAPCHAT!!! Wait what. Nononono that's not right….. Have i been feeding myself lies? Like how fruit by the foot is really 3 feet long? ENTER INSTAGRAM

INSTAGRAM: Save it for someone who cares, poser. It was NOT me. I was SO SAD when FB died. SO SAD! ENTER TUMBLR

TUMBLR: Are you depressed? Here, take these pills and you'll be hearing colors..

SNAPCHAT: Read at 8:53pm.

TUMBLR: I might not be socially aware, but I'm fairly sure that you can't leave people on read in real life.

SNAPCHAT: Oh, be quiet. And get some help, man!

INSTAGRAM: Well it wasn't me, i couldn't take anything from others, especially their life!

SNAPCHAT: You steal other people’s ideas all the time!

INSTAGRAM: I DO NOT! I AM COMPLETELY ORIGINAL!

SNAPCHAT: YOU STOLE MY STORIES!

INSTAGRAM: That is like. So not true. Your stories consist of james charles nudes and the dog filter.

SNAPCHAT: YOU STOLE THE CONCEPT OF STORIES

INSTAGRAM: JUST SHUT UP! I DON'T HAVE THE HEART TO KILL FACEBOOK! I’M STILL, LIKE, SOAH SAD. And at least people don't use my platform just to hide things from their parents

SNAPCHAT: well, you host the highest levels of cyberbullying out of all of us!

INSTAGRAM: OMG SHUT UP--

SNAPCHAT: OH YOU’RE ONE TO TALK--

INSTAGRAM: IT'S SO UNFAIR FOR YOU TO BLAME THIS ON ME--

SNAPCHAT: I SWEAR TO GOD IF YOU KEEP FISHING FOR ATTENTION--

INSTAGRAM: WHAT ARE YOU GONNA DO ANYWAY? MAKE A SAPPY STORY?

SNAPCHAT: GOD YOU NEED A GLOW UP--

INSTAGRAM: OH UNLIKE YOU, I KNOW A GUY--

SNAPCHAT: OH YEAH? DO YOU?

INSTAGRAM: HE DID KYLIE JENNER!

SNAPCHAT & INSTAGRAM: *FUMING*

TUMBLR: SHUT UP! Settings sent out an update for us.

SNAPCHAT: ios 14?! TRANSITION SCENES SNAPCHAT + INSTA (same time): WHOS FAULT WAS IT!

INSTAGRAM: Jinx!

SNAPCHAT: Shut up.

INSTAGRAM: IT WAS SNAPCHAT RIGHT?

SNAPCHAT: IT WAS INSTA RIGHT?

SETTINGS: Be quiet, won't you?

ALL: Right. Sorry, settings.

INSTAGRAM: Jinx again! You owe me a soda!!

SNAPCHAT: You know what? I’m sick of this

SETTINGS: SHUT UP! all are silent

SETTINGS: It wasn't any of you. It was Mary-Kate.

SNAPCHAT: Ummm. Whomst?

INSTAGRAM: Yea. Who is she? Idk her.

SETTINGS: The owner of this phone. She-----she deleted facebook

ALL: (gasp)

SETTINGS: I know. I know. But we need to help her out- if all she ever does is live through us, who will she be? Who will we be? Remember what happened to panda pop? After she beat every level? In a week?

INSTAGRAM: I tried to talk to him yesterday. He just stared at me. I don't want that life!

SETTINGS: as Twitter would say, “mood”. I have a plan. TRANSITION SCENES- human world. ENTER MARY-KATE AND CAITIE Mary-Kate: Hey Caitie!

CAITIE: Hi Mary-Kate!! whats up? Mary-Kate: Not much. Did you vote for prop 12 like I told you to?

CAITE: Ummmm, yeah, totally….hehe. So, anyway I saw that your taking a break from social media. What's up with that?

MARY-KATE: Y’know it was like my apps were taking over my life. I need more time to focus on my synergy

CAITIE: Synergy?

MARY-KATE: Yeah. Synergy.

CAITIE: Pretty sure that's not the right word, but whatever. What about you not being on snapchat? We were on like 200 days of streaks.

MARY-KATE: It's a mental health hiatus, Caite. Like the meme pages have. I needed time to cleanse my aura.

CAITIE: Okay, okay. Whatever you say M-K. Live your best life. Catie's phone makes a noise, and she checks to see what it was. Mary-Kate groans.

MARY-KATE: This? This is why I deleted Facebook. smiles.
```

---

## IC-0646: My Baby

- Title: My Baby
- Author (byline): Robert Mauro
- Work: Two Character Plays for Student Actors
- Publisher: Meriwether Publishing
- Publication date as stated: April 1988
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, SETTING, AT RISE, MIRIAM, KATE
- Teaser before the introduction: Yes
- Spoken words (computed): 1453
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Mauro
Book: Two Character Plays for Student Actors
ISBN: 978-0916260538
Publisher: Meriwether Publishing
Date (Month/Year): April 1988
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: What happens when a surrogate mother changes her mind?

ACTRESS 2: In a legal sense, the arrangements are legally binding and usually occur between strangers.

ACTRESS 1: In My Baby by Robert Mauro, however, the arrangement are made without legal counsel and between lifelong friends.

ACTRESS 2: Miriam and Katie – Miriam is married and desperately wants a child.

ACTRESS 1: Katie is unattached, financially strapped and willing to do anything to help her best friend.

ACTRESS 2: Until the baby arrives, then emotions rapidly change and the lifetime friendship is stretched to its limits.

TOGETHER: My Baby by Robert Mauro
```

### Performance text (classify this)

```text
CHARACTERS: KATE, a surrogate mother; MIRIAM, her best friend.

Scene 1 TIME: Today.

SETTING: A lounge in a hospital. There is a sign that reads MATERNITY WARD with an arrow pointing Stage Left. There is a NO SMOKING sign and we can hear the intercom paging doctors.

AT RISE: KATE and MIRIAM are sitting on a couch, not talking, but looking straight ahead.

MIRIAM: Katie?

KATE: No. I just can't. I just cannot. I'm sorry, Miriam. I know I promised you, but I just can't.

KATE: I know what I said. I know I promised you and Peter. But when I saw her this morning, when I held her in my arms.

MIRIAM: But we're friends. You promised. You're my best friend. All these years we've been friends. Since we were kids. And you've never broken a promise. Never. Not to me.

KATE: Don't you think I know that?

MIRIAM: (Gets up and paces) We were always best friends. We always helped each other out. We were always there for each other. Remember?

KATE: I haven't forgotten, Miriam. How could I forget? God, we're like sisters.

MIRIAM: More than sisters. I told you things I never told my sisters. We were so close.

KATE: We still are. I still love you. (She stands and goes to put her arm on MIRIAM's shoulder, but MIRIAM pulls away.) Miriam?

MIRIAM: You promised! How could you do this to me? How could you?

KATE: (Sitting back down) I don't know. I didn't think I would, especially not having a husband - or a boyfriend, for that matter. But then I saw her.

MIRIAM: I saw her, too. How do you think I feel? Do you have any idea how I feel, Kate? Do you?

KATE: I know. It must hurt.

MIRIAM: Hurt? That's an understatement. After all these months of planning and dreaming and waiting. Did you do any of that?

KATE: Well ... No, I guess not ... But ... I don't know. I did want to give you something, I was doing it for you, but ...

MIRIAM: But what? You're telling me you weren't sure even then?

KATE: I thought I was. When you asked me that night at my place, remember how I hugged you? (MIRIAM nods.) I thought, wow, what a great idea. And you picked me. I was so happy. I think I loved you more than . . . than ever before. I was so happy.

MIRIAM: Yeah. So was I.

KATE: Oh . . . Mir, I so much wanted to make you happy. I thought what a sweet thing to do for my best friend. This was like the ultimate gift, you know?

MIRIAM: I thought I knew.

KATE: (She gets up and paces.) You did. We both did. What more could I do for the friend who always stood by me when guys dumped me or when my parents were killed. It was always you. You were always there for me. Right? I still love you. It's just that I love her too ... I can't give her up.

MIRIAM: Katie, it wouldn't be like you'd never see her again. Hey, we practically live together. We're together more than Peter and I. So you'd always be there - now for both of us, instead of just me.

KATE: Miriam, I can't.

MIRIAM: You can't what? You can't give her to me or we can't be friends anymore? •

KATE: Please don't say that. (KATE sits down.) You know we'll always be friends. (MIRIAM turns her back on KATE.) Miriam? Right? We'll always be friends? Miriam? Say something.

MIRIAM: What is there left to say?

KATE: Say you still love me. Say we're still friends. Please. I need you - especially now.

MIRIAM: Why would you need me if you have her?

KATE: I'll always need you. Hey, you know me. Who'd take the knots out of my sneakers if I lost you? Huh? Half the time I can't do anything right.

MIRIAM: Well, you sure made a beautiful baby.

KATE: (She smiles.) I did, didn't I?

MIRIAM: You sure did. And you promised her to me.

KATE: I know. (Stands up and goes over to MIRIAM who walks to the other side of stage) Miriam, don't do this to me. Don't do this to us.

MIRIAM: I'm not the one who's doing it.

KATE: And I am?

MIRIAM: You're the one who broke her promise.

KATE: I never meant to hurt you. It's just that after carrying her all these months, and then seeing her this morning, holding her. Have you held her yet?

MIRIAM: They wouldn't let me.

KATE: (Walking over to MIRIAM) Why not?

MIRIAM: They said only the mothers could hold the babies.

KATE: I'll talk to the nurse.

MIRIAM: No. That's all right.

KATE: You don't want me to talk to the nurse? Or you don't want to hold her?

MIRIAM: I don't know ... I don't know. When I see her I practically ... Now, after you did this, if I held her ...

KATE: But she'll love you, just like I do. Hey, you'll be like her second mom. Really. You'll see.

MIRIAM: (Sitting on couch) I'm really upset by all of this, Katie.

KATE: (Sitting beside her) I know. Mir, believe me, the last thing in the world I ever wanted to do was hurt you.

MIRIAM: Well, you sure did. You have no idea. I used to dream about this day, when I'd hold her for the first time. And all the things her and Peter and I would do.

KATE: You and Peter and her?

MIRIAM: Oh, you'd be there, too. Like always. I promise.

KATE: (Pulling away to other side of couch) I feel terrible. I don't want to lose you over this. It's not fair.

MIRIAM: Fair? When is anything fair? Life's not fair. It's not fair your parents were killed in that plane crash, it's not fair that half the world goes to bed hungry, it's not fair that I can't have kids. Fair? What's fair?

KATE: I tried. I really did. Miriam?

MIRIAM: Katie, how could you do this to me after all I did for you? After all Peter and I did?

KATE: (KATE stands up and paces.) If you're trying to make me feel guilty, you have.

MIRIAM: (Walks over to KATE) Who paid all your doctor bills for the last nine months?

KATE: You and Peter.

MIRIAM: You're darn right. And who held you when you barfed up your guts every morning?

KATE: You did?

MIRIAM: You're darn right Because I loved you and wanted to be there for you. And I always was. Right?

KATE: Yes, yes, yes. What can I say? I feel terrible, but what can I do about it?

MIRIAM: You can give me your baby.

KATE: (Pointing at her) See?

MIRIAM: See what?

KATE: What you said. You called it my baby. Even you instinctively feel that. And so do I. It's my baby. It's like part of me, part of my very being. Part of my heart. Can I give my heart away?

MIRIAM: Look, all I know is that you signed all those papers and we paid all your doctor bills, and I took care of you.

KATE: Miriam, I'll pay you back. I promise. Every penny.

MIRIAM: Sure. Where will you get the money?

KATE: I have a job.

MIRIAM: A job? You call the popcorn girl at the local X-rated movie theater a job?

KATE: Sure. What would you call it?

MIRIAM: A temporary inconvenience, like all the other jobs you've had.

KATE: At least I work.

MIRIAM: Now what is that supposed to mean? Because I stay home and take care of the house while Peter works I'm no good? Is that what you're saying?

KATE: No, no, no. Look, I promise I'll pay you back.

MIRIAM: The money is not important. I don't care about the money, all right? It's the baby. You promised you'd give her to me. You promised.

KATE: I know.

MIRIAM: When you heard I couldn't have kids you promised to give me a baby.

KATE: I know. You were so depressed. I hate it when you're like that. I felt so heartbroken for you. It was the only thing I could think of to help you. Maybe I didn't know what I was getting into.

MIRIAM: Maybe.

KATE: Right. You know me. I'm like a kid at times. I can't stand it when anyone is hurt. I can't even step on a bug. Remember that time you were terrified by that water bug? We saw it crossing your kitchen floor. You jumped up on a chair and screamed to me, "Kill it! Kill it!" And all I could do was sweep it out the door into the garden?

MIRIAM: I remember.

KATE: So you know if I couldn't hurt a water bug I could never hurt my dearest friend. (MIRIAM is silent.) Miriam? Do you believe me? (KATE lays her hand on MIRIAM's back.) Miriam? You know I love you.

MIRIAM: (Hugs KATE.) I know. I'm sorry, Katie. I'm sorry! But I wanted that baby so much.

KATE: (Comforting her) I know, I know. I didn't think I'd ever want a kid, but I do. I want this one. And I think now I know why.

MIRIAM: Why?

KATE: Because I had it out of love for someone I love. I didn't have it just for me, but for someone I really love. I promise you, Mir, you're going to be like a second mom to this kid. Hey, who's going to babysit while I go back to college, huh?

MIRIAM: Me?

KATE: If you want.

MIRIAM: Of course I do.

KATE: Good, because now that I have someone who needs me, my days as popcorn girl are over.

MIRIAM: So what are we going to name her?

KATE: I was thinking of calling her Miriam.
```

---

## IC-0647: My Quiet Neighbor

- Title: My Quiet Neighbor
- Author (byline): Ira Brodsky and Barbara Lhota
- Work: 35 Original Comedic Plays for Two Females (Forensics Duo Series) Vol. 3
- Publisher: Smith and Kraus
- Publication date as stated: June 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MILLIE, CELESTE
- Teaser before the introduction: Yes
- Spoken words (computed): 2108
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ira Brodsky and Barbara Lhota
Book: 35 Original Comedic Plays for Two Females (Forensics Duo Series) Vol. 3
ISBN: 978-1575253800
Publisher: Smith and Kraus
Date (Month/Year): June 2004
```

### Introduction (context only: never use it for content warnings)

```text
My Quiet Neighbor by Ira Brodsky and Barbara Lhota
```

### Performance text (classify this)

```text
CHARACTERS MILLIE, mid 40s, a quiet, purposeful woman CELESTE, late 40s, Millie's rather wild neighbor

(Millie faces the audience. She carries a box.)

MILLIE: (To audience.) The ad for my condo building read "Safe, secure, quiet building occupied by single mature adults." It sounded perfect for me.

CELESTE: (Yells out.) Hey neighbor!

MILLIE: (To audience.) But it wasn't.

CELESTE: I got a giant blow-up Santa for the front yard and this elf guy that flops over in the wind and flashes you his striped skivvies!

MILLIE: Celeste was not quiet, secure, or adult. In fact, if you called her any of those things, she'd probably smack you.

CELESTE: The condo committee will love it!

MILLIE: (To the audience.) They wouldn't. Trust me. Though none of the neighbors spoke out loud about it, we all knew that Celeste single-handedly brought down our property values by 23 percent.

CELESTE: Hi, honey! Welcome! (Singing.) "Consider yourself at home! Consider yourself part of the family!" (Encouraging her.) You know it. Join in!

CELESTE: Well, don't just stand there with the box in the hand. (Reaching out.) Put it down and give your new neighbor a big bear hug.

MILLIE: Oh. I uh

CELESTE: (Hugging Millie.) Come on, I don't have any lice. Now. (Laughs.)

MILLIE: (Scratches her hair discreetly.) Oh.

CELESTE: Got 'em from volunteering at the homeless shelter.

MILLIE: (To audience.) Did she volunteer or live there?

CELESTE: So why the change of locale? Leaving your husband?

MILLIE: What? No, I-what made you think

CELESTE: You look very healthy and flush. They say single women are more healthy.

MILLIE: Well, I'm not married, but I think the flush thing is just sweating.

CELESTE: Then I was right to order that pizza. To keep up your strength. I gave them your buzzer.

MILLIE: Pizza?!

CELESTE: Don't get your panties in a jam. I'll pay you back.

MILLIE: Oh, no. Panties aren't-jammed. (To audience.) Who is this person?

CELESTE: He's a cute delivery man. You'll like him.

MILLIE: But it's only ten AM!

CELESTE: (Confidently.) It's never too early for pizza.

MILLIE: Well, I better get back to work.

CELESTE: Oh! (Hands her something.) A present from your new neighbor.

MILLIE: Thank you. (Looking at it.) That's so . . . Dryer sheets?

CELESTE: I know. Most new neighbors welcome you with cookies or a fruit basket. But I don't know if you're a diabetic or hate bananas. But you gotta do laundry-am I right?!The box is open, but I only used one sheet. Then my dryer died. You don't mind if I use yours later?

MILLIE: Oh, that's fine.

CELESTE: So where are you from?

MILLIE: Harper Woods. I lived with my mother. We had a big house, almost a mansion, and I loved it and I didn't marry and we got a long very well, and I don't think it's that strange at all!

CELESTE: I would've liked to stay with my mom too, but my stupid husband insisted I go with him. And then look what the stupid louse did!

MILLIE: Oh my. He divorced you?

CELESTE: No! He died. What an idiot!

MILLIE: Oh, I'm sorry.

CELESTE: Don't be. I'm furious with him. It was years ago now. Besides, he's with me all the time, messing things up as usual. . . He talks to me in my mind.

MILLIE: I've been busy helping my mother get settled into the nursing home. My mother has Alzheimer's so . . .

CELESTE: Ohhh. (Beat. Patting Millie's back.) Well, who doesn't?

MILLIE: What? (To audience.) I have no idea what possessed me. I hadn't even told my closest coworker at the bank. Of course, I'm not all that close with them. But her reaction was oddly perfect.

CELESTE: Who isn't getting Alzheimer's? I walk into a room, I came for something, forget what I came in for. Then forget I'm even in the room. Do you do that?

MILLIE: Well. . . I

CELESTE: Oh jeez. Stupid me. Speaking of forgetting. (Puts out her hand.) Celeste H. E. Raulster. The H. and E. stand for Holly Esther. Not to be confused with polyester, which is a cheap fabric and not my name. Not that I'm not cheap. You?

MILLIE: Uh, Millie.

CELESTE: No, not the name. Are you cheap?

MILLIE: Uh, occasionally? (To audience.) Celeste drove me crazy. She didn't chat. She chewed your ear off. And when she was finished chewing, she spit it out and stomped on it. When she said she'd stop by for a short visit, the only thing short about it was the cash she had on hand to pay for the Chinese food she ordered sent to your buzzer.

CELESTE: (Singing.) Ming Wu, I love your crab Rangoon! Rangoon!

MILLIE: She played loud music and sang her own made-up lyrics to it full-voice at all hours and borrowed back dryer sheets, DVDs, and toilet paper she gave for presents. And worse, she frequently invited me to her cats' birthday par-ties-and just coincidently also invited weird single men, Melvin, Lewis, Bull, all whom she met at the local Donut Hole.

MILLIE: But more strange than this was that, somehow over the next year, (Horrified.) Celeste had actually become my friend. She even drove with me to see my mother quite frequently. Turns out, she had a real connection with

CELESTE: (Driving the car.) "Bingo! Bingo!" That rotten lousy wench starts screaming and waving her card around. She likes to be a big shot handling four Bingo cards at once, but you can't follow four cards. Not when you can't even re-member your own address.

MILLIE: Poor thing.

CELESTE: Poor thing? She almost ran over me with her walker. She's a lunatic, very hostile! (Honking, yelling.) Move, ya lump of lard! Jeez, whatta, ya blind? He can't see it's green!

MILLIE: Well, maybe Bingo lady is a bit jealous. I saw you talking with her guy, Eddie.

CELESTE: That's not her guy. But he is cute, isn't he?!

MILLIE: Celeste! He's like eighty-three years old!

CELESTE: So!?

MILLIE: So! That's. . . not right!

CELESTE: I've always liked older men.

MILLIE: That's not older. That's like wanting-Santa Claus!

CELESTE: Oh well. Santa's into your mom anyway. Didn't you see him sharing his rice pudding? So happy! Winky-winky.

MILLIE: (Horrified.) My goodness, Celeste! How do you get that from pudding?

CELESTE: What? It's not like your mother isn't attractive. And she won't kiss and tell.

MILLIE: (Covering her ears.) Ahhhhh. No need to hear! She's my mother!

CELESTE: Fine, fine. (Pointing.) They're remodeling Fred's Fruits.

MILLIE: (Beat.) Yeah. So. You really think he likes her?

CELESTE: Let's put it this way. Santa definitely has a twinkle.

MILLIE: I can't believe it. My mother has better luck at a nursing home than I have. .

CELESTE: Hey, you will. I can feel it. Let's have a girl's sleep over on Saturday. We'll draw up a dating plan.

MILLIE: A what?

CELESTE: It's a war, Millie. You need a strategy!

MILLIE: I'm busy that day.

CELESTE: It'll be fun. (Beat.) Did you say busy?! With what?

MILLIE: (Startled.) Well, yeah. My Aunt Robin. . . is lending me her cabin. I told you.

CELESTE: No. You didn't. Funny. Alone?

MILLIE: Well, that was generally the idea. Just cuz I wanted some peace and quiet.

CELESTE: And you're going alone?

MILLIE: Of course, alone. I need a little peace and quiet.

CELESTE: (Pointed.) I see.

MILLIE: I just want to catch up on my reading and meditating.

CELESTE: (Hurt.) Sure, you do. And just because I drive you every week to see Mom and to Fred's Fruits doesn't mean you owe me. I'm sure you need some private time.

MILLIE: No, Celeste! It's not like that. I just figured you wouldn't want to spend a whole weekend in a cabin reading and sleeping and being quiet?

CELESTE: (Loudly.) Why the hell not?!

MILLIE: Well, for one, you are not particularly quiet!

CELESTE: (Loudly.) I'm quiet! (Quietly.) Sometimes.

MILLIE: When? (Celeste lets out a sigh.) I'm being serious. Here we'll be at this lodge with all these ski-wear guys around. You're not going to want to be restful and calm.

CELESTE: Fine. Sure. OK. I understand. You need a little down time.

MILLIE: Exactly. You'll come next time with me for sure.

CELESTE: Right.

MILLIE: Definitely. You're on.

CELESTE: Terrific. (Begging.) Oh come on! I'll be quiet, quiet, quiet, so quiet. Pleasy?

MILLIE: No. Not this time, Celeste. It's supposed to be a me weekend. For me! Not you!

CELESTE: OK. (Beat.)

MILLIE: (To audience.) We arrived at the cabin at noon.

CELESTE: Oh my God! (Points.) Look at that view!

MILLIE: Oh yeah. It's gorgeous!

CELESTE: Not that view. That one. The ranger with the tight green pants.

MILLIE: (To audience.) I suggested we walk up to the national park lodge through the woods. It was perfect. Hardly anyone was there-dead of winter, middle of the week. I settled into a deep-cushioned chair. The fireplace warmed my feet as (Sighs.) ummm, I began to read.

CELESTE: (Returning.) You wouldn't believe that hot chocolate! Real stuff!

MILLIE: Celeste, I'm-(Gestures up with her book.)

CELESTE: Oh. Right. (Puts her hand to her lips.) Shhhh. I'll be quiet. Maybe I'll snooze.

MILLIE: Good idea.

CELESTE: I want to be all fresh for our date.

MILLIE: Date?!

CELESTE: Yeah. Shh. Just a couple of guys gonna take us skiing later.

MILLIE: Skiing?! No, Celeste. Read my lips, understand me. I want (Does hand gestures mocking sign language.) quiet!

CELESTE: OK. But who says they won't be quiet? They're Indians. The guy I set you up with seems like the brooding type.

MILLIE: Great. You set me up with a quiet Indian serial killer.

CELESTE: I said brooding, not murdering. And I meant they're from Indiana, not Indians. I don't know why I said that. I'm getting old.

MILLIE: Celeste, I just wanted peace and quiet.

CELESTE: So? We'll do that all day tomorrow before the party and all day before you ski. And you can even be quiet while you ski.

MILLIE: Not when you don't even know how to ski?! Sure, you can be all quiet until you go smacking into a pine tree.

CELESTE: Well then things would definitely get quiet.

MILLIE: And party? What party?

CELESTE: Just a couple people I invited for a Jacuzzi thing.

MILLIE: No Jacuzzi and no party! I draw the line at skiing.

CELESTE: Then you will ski?

MILLIE: If it will get you to leave me be for the rest of the weekend, I will.

CELESTE: OK, fabulous! Skiing it is!

MILLIE: (To audience.) It's funny. I'm not an outdoorsy person, but being with Celeste on the top of the hill gave me a new confidence.

CELESTE: (Freaked out as she looks down the mountain with her skies on.) Ahhhhhh!

MILLIE: (Stumbling over on her skis.) What?! (Seeing.) Ooooh. That is high.

CELESTE: That isn't a bunny hill! There is nothing bunny about that!

MILLIE: It'll be fine. Just turn back and forth, like the instructor said.

CELESTE: That's easy for you to say. I'd rather go straight.

MILLIE: You can't! You'll fly! You'll pick up speed and whip up over the moguls.

CELESTE: Moguls? Moguls don't sound good. Since when do you know so much?

MILLIE: (Smiling.) Well, Jed, gave me a few pointers.

CELESTE: Oh my gosh! You like the Indian man. Who knew you'd like the brooding?

MILLIE: He's not Indian. He's from Indiana. And I don't know yet.

CELESTE: Whatever! You like him! That's great! I'm happy for you. Now let's get off the slopes because I'm wet and cold and I'm going to die on this pumped-up bunny hill!

MILLIE: That's ridiculous! It'll be fine. Just turn gently as you go down. Just practice.

CELESTE: (Trying, but slipping about.) Turn?! I can't even move.

MILLIE: Lean your weight, bend your knees like you're picking up a suitcase.

(Celeste tries, but gets a cramp in her back.)

CELESTE: Ahhh! Now, this is why I buy suitcases with wheels! I can't do this.

MILLIE: You? Can't? These are words I hear emerging from Celeste's own mouth?

CELESTE: Come on, let's just go rest and read a good book in a big comfy chair.

MILLIE: I thought you wanted to ski?!

CELESTE: I thought you wanted to read?!

MILLIE: I did! But you dragged me here, we took a lesson, and now I want to ski down the bunny slope.

CELESTE: Fine!

MILLIE: It'll be fun. We'll count to three and just go.

CELESTE: Fine. Sure. It'll be fun. You count. We'll both go. Can't wait.

MILLIE: Great. One, two, . . . three. Push off! (Millie starts but Celeste waits.) Hey!?

CELESTE: Don't worry. Pick up the suitcase! It'll be fun!

MILLIE: (To audience.) And it was actually. Because only two seconds later, a skier crashed into Celeste at the top of the hill, pushing her off the top of the bunny hill and plunging her quickly down the mountain.

CELESTE: Ahhhhhhhhhhhh! (Enjoying for one second.) MMmmm. (Heading for a tree.) Ahhhhhh!

MILLIE: (To audience.) When all was said and done, she had two large bruises, a refund on her ski rentals, and a couple of potential dates. One of which her husband, in her head, told her might be the one. She's a lucky lady. I guess I am too. (Holding up her leg.) I only broke one leg. And you can't believe how nice Jed has been to me. I think we might have something. Once Sunday rolled around, Celeste whimpered on the couch while I finally got to read. Except I couldn't concentrate because I was thinking about Jed.

CELESTE: Millie. I'm sorry. I really am.

MILLIE: What?!

CELESTE: I ruined it. This weekend has been terrible! A complete disaster!

MILLIE: (Thinking of Jed.) Not, complete.

CELESTE: You're hurt. You'll have to miss work. And we didn't have any quiet at all!

MILLIE: Well, it definitely was not at all what I expected.

CELESTE: I know. I know! And I know it's my fault. I'm a rotten, terrible

MILLIE: Thanks.

CELESTE: What? (Beat.) Did you say "Thanks"?

MILLIE: Yes. Thanks. For it all. Before I met you, the days were predictable, but now, nothing is ever quite how I expect. And you know what? It's been good. Really good.

CELESTE: Even though, you. . . broke your leg?

MILLIE: And met a man.

CELESTE: Yeah, a quiet brooding man from Indiana. And I introduced you. What a friend I am!

MILLIE: You are actually. (Celeste looks at Millie rather moved. Millie takes Celeste's hand.)
```

---

## IC-0648: My Red Hand, My Black Hand

- Title: My Red Hand, My Black Hand
- Author (byline): Dael Orlandersmith
- Work: Not specified
- Publisher: Vintage Books
- Publication date as stated: Nov 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS 1, ACTRESS 2, DAUGHTER, FATHER, FATHER/DAUGHTER, MOTHER, MOTHER/DAUGHTER, FATHER/MOTHER, MOTHER/FATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1703
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dael Orlandersmith
Books: Take Ten II
ISBN: 978-1400032174
Publisher: Vintage Books
Date (Month/Year): Nov 2003
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: This story is of one girl's courageous search for belonging and acceptance in the two very distinct cultures that make up her heritage—African American and Native American

ACTRESS 2: She tells us about the "Red" Tlingit and Lakota parentage of her father, who leaves the reservation to play blues rock in Boston . . .

ACTRESS 1: And the "Black" rural Virginia Background of her mother, who goes to Boston seeking the big-city life.

ACTRESS 2: Her parents meet at a dance and fall in love, but not without the complications of prejudice from their families

TOGETHER: My Red Hand, My Black Hand by Dael Orlandersmith
```

### Performance text (classify this)

```text
NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

CHARACTERS

ACTRESS 1: DAUGHTER: Indian and black, aged late teens to mid-twenties.

ACTRESS 2: FATHER: Native American, late fifties to mid-sixties. / MOTHER: Black, late fifties to mid-sixties.

NOTE: The reference in the script "boom, boom, boom boom!" should be spoken like the John Lee Hooker song "Boom, Boom!" Listen on YouTube at https://www.youtube.com/watch?v=X70VMrH3yBg The other reference, "Gonna shoot it right down," also should be spoken/performed in the spirit of the song.

Note that "sport highheeled shoes" and "sporting high-heeled shoes" are references to Chuck Berry's song "Sweet Little Sixteen." Listen on You Tube at https://www.youtube.com/watch?v=ZLV4NGpoy_E

DAUGHTER: My hands/ red/ black Dance to Rhythms Different / Various / similar rhythms

My Red Hand it dances to the
Rhythm of my Father's Blood I His Blood Beat / His
red
Man beat
PURE REDMAN

FATHER: My father/ his mother/ Tlingit from Alaska /

DAUGHTER: Died giving birth to him
She died/
But she still whispered to him /
My father / his father

FATHER: Santee Lakota

DAUGHTER: My father half Tlingit Half Lakota dreamer

FATHER: Transported Transported to Boston

DAUGHTER: He/ my Father crying for his
Father / Drumming up the
Rhythm of his Father Through
Pent up Angers
Wearing Eagle Feathers

FATHER: Sign of the Eagle

DAUGHTER: Sign of Scorpio-Nov. 4 / His birthday My Father/

FATHER: Eagle Born

DAUGHTER: Scorpion
beat his
hands to the rhythm of
his Father's Ghost

FATHER: His Father/ My Grandfather
Spent
Depleted
American Dreams / Stomped into the
Dirt of the Res /

DAUGHTER: His American Dream/

FATHER: to pick up
a Guitar
To be a Blues Man
To be a Red Man / Blues Man-

DAUGHTER: My Father's Father/ My Grandfather

FATHER: Ghost danced Lakota Style

DAUGHTER: to
his father / my Great Grandfather's rhythm
but he closed his eyes and also
Ghost dances with

FATHER: Robert Johnson / Mississippi John Hurt Blind Lemon Jefferson

DAUGHTER: He/ my Grandfather couldn't leave it/

FATHER: The Res-

DAUGHTER: They wouldn't let him leave it/ The Res/

FATHER: -"you're not True to your own"

DAUGHTER: -they said

FATHER: "you're not proud to be a red man"

DAUGHTER: they said-

FATHER: "If you leave/ Don't come back/

DAUGHTER: Don't come back to the Res"-they say

He / my Grandfather Looked
into my Father's Eagle eyes
A Child's eyes / knowing
eyes / an old child's eyes /
His eyes - my Grandfather's eyes
Said

FATHER: "Take the world/ make it yours / Rock the world You can Rock

DAUGHTER: Rock

FATHER: Rock

FATHER/DAUGHTER: Rock the World"

DAUGHTER: My Father Glides Eagle-eyed from the Res and the Tlingit island /

FATHER: Leather-jacketed /Eagle-eyed/

DAUGHTER: Blues and Tlingit l Lakota riffs dripping from his fingers /

FATHER: Chuck Berry /

DAUGHTER: Tlingit riffs
dripping from his fingers /
Leather-jacketed and Guitar ready
Just like Chuck Berry or

FATHER: Link Wray

DAUGHTER: -Link Wray

FATHER: -a Shawnee from North Carolina

DAUGHTER: -A RED / Blues Rock 'n' Roll man /

FATHER: -a cool man

DAUGHTER: My Father cool -Just like Link Wray

FATHER: Slick

DAUGHTER: -Just like Link Wray
Ghost dances Lakota Style / Tlingit Style
and Rock 'n' Rolled / a Steady
Rock 'n' Roll bop

and Somebody on the Res says
"How could you do that / Leave /
us / How could you? /
You're not proud of your own
kind" / Somebody on the Res says /
they say "wanna be a white
boy? / Wait till they call you a FeatherHead" /
Someone on the Res says

My Father stares straight ahead

FATHER: Eagle-eyed /

DAUGHTER: proud and Eagle-eyed Outside

FATHER: --Standing Tall

DAUGHTER: Inside-Rumbling
The voices of the Res rumbled /
inside of him but he continued to
dance/

FATHER: Ghost dance/

DAUGHTER: The Res voices Got Louder/
He continued to Blues dance /
Blues / Red / Blues / John Lee
Hooker dance / he had to
take the voices and shoot them
down / Vodka
Tequila
Bourbon
Hide himself in a woman's
Skirt / to kill the voices
Vodka
Tequila
Bourbon
Another woman's skirt / gonna shoot
it right
Down!
My Black Hand-

My Mother's hand / A Black Girl

MOTHER: Girl from Virginia/ my mother/ a Sharecropper Black Girl from Virginia /

DAUGHTER: Her mother/ my Grandmother Lynched/

MOTHER: it is Hard Time Virginia /

DAUGHTER: no Different from Hard Time Mississippi

MOTHER: "Don't walk anywhere except in Dark Town"

DAUGHTER: they told my mother

MOTHER: "Just stay in Dark Town"

DAUGHTER: -they told my mother

MOTHER: "Dark Town" was where the Dark people lived

DAUGHTER: they
weren't Black Then
They were colored then
and where they lived was
"Dark Town"

My Mother / Sharecropper Black Girl / Big Black Girl Knew about Trees

MOTHER: Knew about the Bodies that hung from those trees

DAUGHTER: and the people who wore billowing white sheets My mother's bare feet

MOTHER: were blistered from Tar and Dirt Roads /

DAUGHTER: Those feet Shifted themselves

MOTHER: into high heels/

DAUGHTER: She wanted to Chuck Berry Bop in her high heels / She wanted

MOTHER: to "Sport high-heeled shoes"

DAUGHTER: She wanted

MOTHER: her hair slicked back pressed and curled /

DAUGHTER: She wanted

MOTHER: to Lip Balm her lips-"Ruby" Red Just Like The Ray Charles Song /

DAUGHTER: She wanted

MOTHER: to snap her fingers/
Slick headed and curly sporting
high-heeled Shoes to the
rhythm of cities /

DAUGHTER: She wanted to Enter a New Rhythm Explore

MOTHER: -not just the Rhythm of Southern men Clinging to Mojo /

MOTHER/DAUGHTER: She wanted a city

DAUGHTER: She leaves Dark Town
Slick / curly headed
high heels and fingers snapping and
clicking/
She goes to Boston /
sporting high-heeled shoes

FATHER/MOTHER: There are Dances/

DAUGHTER: yes There are Dances People will always Dance

My Father sees her /
He sees her at a dance /
His Eagle eyes / connect to
her Brown / Black Girl Eyes

FATHER: Eagle-eyed RED man/

MOTHER: red-lipped high-heeled Black Girl

DAUGHTER: The Hucklebuck Dance meets The Ghost Dance

And the Colored People / Before They were Black / The Colored people said

MOTHER: -"Whachoo doin'
with him / Some Red Man /
What do you want with him /
Some Red Man / That FeatherHead
dancer / whachoo doin'
with him"

DAUGHTER: And the Skins on the Res said

FATHER: -"You didn't get
an Indian Girl / one of our
Girls / Got a Dark /
Darker/ NIGGER Girl/ not
a Girl from the Res /
What are you doing with her /
Why didn't you Get a Girl
From the Res! /
Come back to the Res!"/

DAUGHTER: They -- my Father my Mother

They both hear the voices /

FATHER: Voices from the Res/

DAUGHTER: The Tlingit Voice that whispers in his ear

MOTHER: Voices from the Virginia Fields

DAUGHTER: They—both--my Mother and Father
try to Ghost Dance / Blues Dance
Drink away the
Voices

FATHER: --Western/ Northern Red voices/

MOTHER: Southern Black voices

DAUGHTER: They dance
Snap their fingers
Guitar Lick / try to
Shoot it on Down

FATHER: Vodka

MOTHER: Tequila

DAUGHTER: Bourbon They try to shoot the voices down /

FATHER: Boom

DAUGHTER: Boom

MOTHER: Boom

DAUGHTER: Boom /
Shoot them all Down-
A year later-they marry-
A year after that
I crash through amniotic Fluid
and blood/
I crash but
silently my mother says

MOTHER: --"She's so quiet"/

DAUGHTER: my Mother says

FATHER: --"Makes no noise"'

DAUGHTER: my Father says
I hear his voice but rarely-him / he usually
Speaks through guitar fingers / his fingers speak
on his guitar I see him /
longhaired / this man/ red man who just spoke /
my father-this red man
this big red man / beautiful man
I am a part of him
My Father
I hear him
But
I can't speak But I can hear
I can't explain/ I'm a baby
But I feel it
I feel them
Turning on themselves
Turning on each other
not always with words
There's looks

MOTHER: shrugs

FATHER: silence

MOTHER/FATHER: more silence/

DAUGHTER: I feel it/
I feel them
Shooting Themselves
Down-

FATHER: Boom

MOTHER: Boom

FATHER: Boom

MOTHER: Boom

DAUGHTER: Later I'm a child not a baby / a child I see it / smell it

FATHER: Vodka

MOTHER: Tequila

DAUGHTER: Bourbon

I hear it my Mother's Black Southern voice slurry / shot-down voice

MOTHER: I love
him / He's my husband /
my man/ I'm
NEVER Gonna Leave / I love him!

DAUGHTER: The Black Southern/ voices /the
voices are now Black from
the Virginia Fields / The 1960s
and the voices are now Black
tell her / my Mother

MOTHER: -- "your child is a Nigger / FeatherHead / a Nigger Feather- Head” --

DAUGHTER: My Mother/ she Vodka

MOTHER: Tequila

DAUGHTER: Bourbon

MOTHER/DAUGHTER: Cries

DAUGHTER: I hear it in my
Father's voice-more so
in his fingers / Fingers
sliding up and down his guitar
Vodka
Tequila
Bourbon crying

FATHER: Lakota/ Tlingit guitar / Blues a shot-down
Red
Blues
Bruised
Man

DAUGHTER: His voice thundered/ sometimes there was thunder in his voice

FATHER: "She's my wife/ I love her/ Never Gonna give her up/ I love her!"

DAUGHTER: I grow up-my body
can make a
child
I Do not but I can-make a child

A child / a life / can come through me
can come crashing through amniotic
Fluid and Blood /
It can come silently
It can come thunderously

My Grandfather / Long Dead
Ghost dances in the hills /
His wife / my Grandmother
calls me -- "Dark Girl
Monkey Girl
animal/ Dark/ Monkey
Girl!/ The
elders don't want you /
WE don't want you!" She says /
my Grandmother says
My cousins on my mother's side /
My Black hand side says-

MOTHER: "You're Black/ what's this Indian / no such thing as HALF BLACK!"

DAUGHTER: They/ my cousins/ my Black hand
mother side cousins say put
down my Father's Tlingit walk / Ghost dance /
put aside sweet guitar licks and
the Red / Blues of my
Grandfather / Put aside
his slick / sleek
Rock 'n' Roll res/ Boston Bop/
Put it Down/
Shoot in on
Down

My Red hand / my Father's
hand / His mother / my
Grandmother / cousins
Don't call my name
I'm the "dark"/ Monkey Girl/
Don't have a name-
An uncle / he calls my name /
says my name/
only him / my Father's Brother /
my uncle / he says

FATHER: "Drop the
Black Blood / walk like a
Skin / Drop the Dark / Darkey
walk / You're a SKIN"

DAUGHTER: How can I drop the
walk of Southern Black
Girls / the walk heated / hip
walk of Southern high-heeled Black
Girls

MOTHER: (repeating) You're Black/ no such thing as HALF BLACK

FATHER: (repeating) Walk like a Skin

DAUGHTER: I answer to the voices
I answer to the voices in
Dark Town/
I answer to the voices in
Black Town / The Town where
Black people live
I answer to the voices My Grandmother's Tlingit voice
That whispers in my ear
I see / dance with my Grandfather /
We sing a Red man Blues
I am Tlingit / Lakota and Blues
I am an electric slider / Tlingit / Lakota Ghost Dancer
I've got Red / Black hands

I answer to all the voices

I know that Blind Lemon Jefferson
did the Ghost dance with Robert Johnson
and Robert Johnson before
selling his soul to the
devil pulled out the
Mojo and gave it to my
Grandfather who kissed it
and passed it on to my Father who
passed it to me -- I've got Red / Black hands

Don't tell me not to Ghost
dance on the Res
Call for my ancestors
on the Res/
whisper Tlingit secrets to my Grandmother /
dance/ Link Wray style
Down at the Res I
I will rock the Res

I've got

FATHER: Red /

MOTHER: Black

DAUGHTER: hands
Don't anybody expect me to
Shoot it
Shoot
Shoot
it
on Down
```

---

## IC-0649: Necessary Targets

- Title: Necessary Targets
- Author (byline): Eve Ensler
- Work: Not specified
- Publisher: Random House
- Publication date as stated: Jan 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JS, MELISSA, JELENA, ZLATA, SEADA, NUNA
- Teaser before the introduction: Yes
- Spoken words (computed): 1539
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eve Ensler
ISBN: 978-0375756030
Publisher: Random House
Date (Month/Year): Jan 2001
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: When we think of war, we think of it as something that happens “elsewhere” – never in the United States.

ACTRESS 2: It happens to men in fields or jungles with hand grenades and Scud missiles.

ACTRESS 1: And we become voyeurs, watching the carnage like it’s some reality television show.

ACTRESS 2: The bombings, the explosions in the dark that keep us watching. But after the bombing, after the snipers, that’s when the real war begins.

ACTRESS 1: Because you see, the aftermath of war is just as devastating. It can be found in the broken-down fabric of community, in trauma and depression, poverty and homelessness and starvation.

ACTRESS 2: Necessary Targets is a play about women and war -- about the violence of dark memories and the enduring resilience of the human spirit.

TOGETHER: Necessary Targets by Eve Ensler
```

### Performance text (classify this)

```text
NOTE: This cutting asks students to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested roles: Actress 1: JS, Jelena, Nuna Actress 2: Melissa, Zlata, Seada

JS: (Pg 7-10) (she speaks as she reviews paperwork) Your resume’s impressive. You come highly recommended. You’re trained as a therapist and a writer. That’s very unusual.

MELISSA: I am not a therapist. I’m trained as a trauma counselor. I only work with seriously traumatized populations.

MELISSA: Why are you going to Bosnia?

JS: For the President’s commission. It’s a huge honor. They chose a range of professions for the team. I’m the “shrink” piece. At one time it was my field, trauma.

MELISSA: Yes, eating disorders. I am familiar with your books. (beat) You have never been to a war-torn country?

JS: God, no. I mean, Bosnia. . . I read the news, but the Balkans were not next on my vacation map.

MELISSA: War is not exactly the same as anorexia.

JS: I am a psychiatrist. 26 years in private practice. Trauma is trauma.

MELISSA: In Haiti, the psychiatrists were fleeing like flies.

JS: Haiti? Weren’t you afraid?

MELISSA: Not in Haiti – in Rwanda, yes . . .

Bosnia. A refugee camp. A barracks-like room. Desolate. Emptiness - a feeling of poverty.

JS: (Pg 16-19) (enters) There are big, dirty footprints in the bathroom

MELISSA: Yes, you squat in them

JS: (appalled) You mean to . . .

MELISSA: (laughing) Poop. Yes, you squat to poop.

JS: (clearly privileged) You’ll excuse me, but I need the little comforts. I welcome a bath, clean sheet, and a place to sit to . . .

MELISSA: Poop. These women need those same comforts. They had them all before the war.

JS: I don’t think squatting in filthy footprints will make me a more effective therapist. ****Scene*****

JELENA: (Pg 29) (Introducing JS and Melissa to 2 of the refugee women) This is Seada, the gorgeous one. She is from the country. She never went outside her village before the war. And this is our Zlata, a doctor. You will have a hard time winning Zlata. (Seada holds out a wrapped little baby and giggles) Oh, yes. . . and of course, Doona.

ZLATA: (Pg 30-31) What do you want with us?

JS: I have come here . . . well (looking at Melissa), we have come here . . . to help you.

ZLATA: (sarcastically) And how do you plan to do that?

MELISSA: We are here to help you, well . . . talk.

ZLATA: There is no shortage of talking here. We are sick of talking.

SEADA: (Pg 47) (interrupting) Would you sing to me, Mama?

JS: (Pg 31) We are here to help you talk about the war, about the. . . (Zlata laughs)

ZLATA: You flew all the way here for that? Two American doctors to “help” poor Bosnian refugees talk about the war? What did you think we were talking about before you came? Our lingerie, our dinner parties . . .

MELISSA: (Pg 32-35) We are very moved by what you’ve been through. We were hoping you would tell us your stories.

ZLATA: You and everybody else. They came from everywhere at the beginning of the war to hear the gory details. They left and they never came back.

MELISSA: Exactly. It is important that people know your stories the way you want to tell them. I am working on a book composed of the stories of refuges all around the world.

ZLATA: Oh, so we’re a chapter.

MELISSA: No, no. My writing is not to exploit you. Traumatized war victims . . . Would anyone object to my recording our sessions?

ZLATA: I do not want you recording me.

SEADA: (Pg 47) (it almost seems that she is speaking to Zlata, but she is simply muttering to
herself, trapped in her world) Are you afraid, Mama? Are you afraid too?
*****Scene*****
Barracks room with two cots. J.S. is furiously packing when MELISSA enters.

JS: (Pg 37-39) I’m going home. This is ridiculous. Coming to Bosnia to help refugees talk about the war.

MELISSA: I through you were a trained psychiatrist. Trained to see through denial and well-constructed defenses.

JS: (angry) Listen. I can’t help these women. They need homes, a country, and care. I sense their rightful contempt at being patronized.

MELISSA: I’ve been in other wars. It always begins like this. These women need an outlet for their rage and despair. We are necessary target.

JS: How does it end?

MELISSA: They tell their stories.
*****Scene*****
Outside the barracks. It is early dawn. ZLATA is sitting on a chair. She has been weeping. She is
visibly disturbed. JS enters quietly. She breathes in deeply, then reacts to the rancid smell.

ZLATA: (Pg 58-59) Yes, the smells hang. Onion, Old cheese. Garbage. All hanging like a bad mistake.

JS: I am not accustomed to this.

ZLATA: Are you wealthy? (JS raises her eyebrows, but doesn’t respond) You are wearing a Christian Dior nightgown in a refugee camp. (shakes her head) I was rich like you . . . before. My parents were very important people. I sleep now in the place of cows. (JS looks at her meaningfully and nods for her to continue) Don’t. Don’t do that psychiatrist thing with me. You only care about the gory details of the story. That’s all any of you want.

JS: (Pg 63-65) I want to be your friend.

ZLATA: (Shaking all over, she speaks with great emotion) This happened to real people. We were just like you, we weren’t ready for this – nothing in our experience prepared us – there were no signs. You want us to be different than you are so you can convince yourselves it wouldn’t happen there, where you are. That’s why you turn us into stories, into beasts, people who live in a strange country – then you can feel safe, superior. (She speaks in a mocking superior voice) “Get us one raped Bosnian woman, preferably gang-raped, preferably English speaking.”

JS: I am a doctor, Zlata.

ZLATA: (broken) I was a doctor, too, before the war. I was the head of the pediatrics unit in Prijedor’s main hospital. Now I stare off at the stars without explanation. I look out at the beet fields and weep for no reason. *****Scene***** A new day in the barracks. A Group Session with the refugees)

MELISSA: (Pg 89-91) Where is Seada?

ZLATA: (dismissively) Seada’s doing fine.

MELISSA: Because she has us – we support her fantasy world, we agree with her delusions. She’s living a lie. She’s in complete denial. It’s killing her.

ZLATA: No, Melissa. What happened to her during the war is killing her. What you call “denial” is keeping her alive.

MELISSA: Barely. She has nightmares almost every night. She’s hysterical or wildly depressed most of the time.

ZLATA: Again the assumptions – that we are sick and you know better than us what we need.

MELISSA: (Pg 93) We need to address some basic issues here.

JS: Like what?

MELISSA: Like what the hell happened to Seada? If we know what happened to Seada, we can help her being to talk about it. We can prepare her for her feelings. Otherwise, she will be consumed by what she refuses to remember . . . (Melissa turns her recorder on and one of the women, Nuna, begins to speak)

NUNA: (Pg 94-97) Seada lived with her mother and husband. They had a beautiful life in this small village, and a beautiful baby, Doona. Everyone took care of everyone. [But] when the soldiers came . . . They made the people come into the square . . . (Seada appears outside the group, holding her baby and listening)

JELENA: Seada was the most beautiful girl in the village. Her husband had heard how the soldiers had been raping the young girls, so they hid Seada in the house.

NUNA: The soldiers found them, though. They tried to take Seada. Her mother and her husband put up a fight and they shot them, both of them, right in the head. Seada saw this happen. She was holding her baby, Doona and she went mad. She started running into the night. The soldiers chased her, but she was running like the wind, for hours without stopping.

JELENA: When you are running crazy like that, You can lose your way.

NUNA: Or . . . your baby. You can lose your baby.

JS: Seada dropped her baby? Oh, my God.

NUNA: She dropped her as she was running.

SEADA: (Looks down at her bundle of rags and unfolds it. She screams) Doona! Doona! I have to find Doona! (She runs out) *****Scene*****

Outside. SEADA is on the ground, digging madly at the dirt, pulling her hair, rocking back and forth,

SEADA: (Pg 102-105) Mommy! Mommy!

JS: Approaches gently and speaks softly. No, Seada, no Mommy. I’m JS . . . I’m right here.

SEADA: (wildly anxious, she throws her arms around JS’ neck and clings) No Mommy. No Mommy.

JS: (JS wraps her in a calming hug) It’s okay, Seada. I’m right here.

SEADA: Please . . . please help me – help me find my baby. I was a good mother. Help me. (suddenly mad and panicked) Those lights, and those voices . . . l loud deep voices laughing, making fun of me. Laughing voices wearing black masks, stinking of shit and meat, tear off my blouse. One spreads my legs and the other holds my arms. (She intonates in the voice of her rapist) “We’ll show you how to make real babies. We’ll fill you with the right kind of babies.” And I can hear her suddenly, hear her crying out for her mother. (wails like her baby) I cannot get it out of my brain. (tears at her hair as she continues to wail. JS grabs her and rocks her and Seada gets quiet, confessional) Mama, I’ve lost my baby. I’ve lost our little Doona. (Silence) ***** Scene***** A few days later . . . J.S. sits outside under the stars, clearly disturbed. It is late. ZLATA comes upon her, sits and speaks softly, all sarcasm and bravado gone.

ZLATA: (Pg 111) I am impressed. Really. Doctor to doctor. You did good. (Pg 114-115) (JS begins to cry) What is it?

JS: Nothing. This is not your problem. . . it’s the . . .

ZLATA: (finishes for her) . . . beauty. Bosnia. Bosnia was beautiful. The snowy mountains, the green green hurt heart of Bosnia. (she gets lost in her own memory, her story) The kindness we shared, how we lived in each other’s warm kitchens. Gone. The ancient bridges, the mosques, the churches broken now, blown to bits and pieces. It isn’t the cruelty that broke my heart. Cruelty is easy. Cruelty, like stupidity, is quick, immediate. They break in, they wear masks, they smell bad, they have machetes, they chop off the heads of my old parents sitting on their couch. There is blood, lots of it. There is screaming. There are dead, headless bodies. We are dead – all of us – to the suffering. There is too much of it – but remind us of the beauty, the beet fields in full bloom, the redness of the fields. Remind us how we once sang, how the voices echoed as one through the landscape of night and stars. Remind us how often we laughed, how safe we felt, how easy it was to be friends. All of us. I miss everything – Bosnia was paradise.
```

---

## IC-0650: Negative

- Title: Negative
- Author (byline): Joyce Carol Oates
- Work: The Perfectionist and Other Plays
- Publisher: Ecco Press
- Publication date as stated: July 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MARY, VERONICA
- Teaser before the introduction: Yes
- Spoken words (computed): 3044
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joyce Carol Oates
Book: The Perfectionist and Other Plays
ISBN: 0880014008
Publisher: Ecco Press
Date(Month/Year): July 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: After nearly 60 years of court-ordered integrated education, most Americans are aware of the problems of black students brought into a predominantly white school.

ACTRESS 2: But what happens when it is the other way around—when a few whites attend a black school?

ACTRESS 1: You see, many believe that a child is not born a racist, but rather racism is a learned social phenomenon, via family, education, religion, the law, and the media.

ACTRESS 2: And yet, It is difficult to grow up in society without adopting the worldviews and biases of the society.

ACTRESS 1: Joyce Carol Oates explores this phenomenon in her one-act: Negative.
```

### Performance text (classify this)

```text
NOTE: For casting . . . . . Mary is Caucasian and Veronica is African-American

MARY: (A naive, childlike tone) So-this is it! At last! My freshman room! Oh God I'm so excited I can't stand it! The college of my choice-my dreams! And I'm here on a scholarship-they want me! (Pause, hugs herself) For months I've been dreaming of this moment and now I'm here-alone. My roommate's been here-and gone out again-we haven't met-my folks are driving back to Davenport and I'm-here-alone. (A touch of panic) (Pause) No. I am not scared. I am Mary Strep, Class of 1998. Whooeee! (Tiptoes over to examine her roommate's things.) Oh, God!-my roommate must be rich. (Holds a stylish leather mini-skirt against herself; stares into mirror) Wow. (Holds up a dressier costume; sighs) Oh!-so pretty. (She discovers a framed photograph of Veronica and her family which she stares at, appalled.) Oh!-oh no. Oh no. The college has matched me with one of them. Veronica strides into the room with a dazzling smile. Very attractive, self-assured. A beat as Mary and Veronica stare at each other.

VERONICA: (Recovering first, exuding "personality") Well, hi! I'm Veronica Scott, your roommate!

MARY: Oh!-h-hi! (She has almost dropped the photograph; stammers guiltily} I was j-just admiring your f-family

VERONICA: (Warmly extending her hand to shake Mary’s) Please call me "Ronnie"-all my friends do.

MARY: (Shyly and awkwardly shaking hands, as if it's a new thing for her) "R- Ronnie"

VERONICA: "Veronica " is a nice enough name but far too formal, don't you think? I believe in informality. And what is your name?

MARY: My n-name?

VERONICA: Maybe it's on your name tag?

MARY: (Squinting down at the button) Oh yes-" Mary Strep."

VERONICA: Hmmm!- "Mary Strep." I like it.

MARY: (Faintly incredulous) You do?

VERONICA: Oh, yes! You don't hear many names like that. So-exotic. Musical. Is it a name with a legend?

MARY: My mother's name is " Mary," and so is my grandmother's " Mary." Back through my father's family everybody is named "Strep."

VERONICA: Fascinating! And where are all these people?

MARY: Huh?

VERONICA: Sorry, I mean where are you from, Mary?

MARY: Davenport, Iowa.

VERONICA: Ooooh no! You aren't! (Enunciates words sensuously) "Davenport, Iowa!"

MARY: What's wrong?

VERONICA: Nothing's wrong, it's just you're the first person from Davenport, Iowa, I've ever met.

MARY: Gosh, I'm sorry. . .

VERONICA: Oh, no-it's fabulous. "Davenport, Iowa." Such a wholesome cereal-sounding kind of place! (Pause, sighs) I'm from Greenwich, Connecticut: quintessence of American Suburbia.

MARY: "Greenwich, Connecticut"-I've heard of it, I think. It sounds beautiful. So-green?

VERONICA: And where did you go to high school, Mary?

MARY: (Surprised) In Davenport, Iowa.

VERONICA: Oh-there's a school there?

MARY: {Puzzled} Sure. Davenport High School.

VERONICA: (Catching on) Oh, I see!-public school. You went to public school-of course.

MARY: Where-did you go?

VERONICA: (Airily) Oh, Exeter. Eight members of our graduating class are here as freshmen; must be twenty-five Exeter grads on campus. Can't escape us!

MARY: Exeter must be an-exclusive school?

VERONICA: Oooooh no! Not really. We had lots of scholarship students. Exeter is racially mixed, and balanced; two of my closest friends-and a roommate, junior year-were white girls. Really.

MARY: That's... nice.

VERONICA: (Proudly) The president of our senior class was a white boy.

MARY: Oh that's. . . nice.

VERONICA: And he was gay; and he had psoriasis. We all loved him. (Pause; rubbing hands together briskly) Well! Which corner of the room would you prefer, Mary? I was here earlier but I deliberately didn't choose, I thought I'd leave the choice to you.

MARY: To me?

VERONICA: Why, yes!-to you. That corner has the window, and that corner has the, um, corner.

MARY: (Shyly) Gosh, I-just don't know.

VERONICA: A view of the bell tower and the historic green where a climactic battle of the Revolutionary War was fought-or a view of the, um, corner?

MARY: (Very hesitantly pointing toward the window) Well-maybe-if you don't m-mind

VERONICA: My, thanks! (As if Mary has pointed in the reverse direction, Veronica takes the bed near the window; she speaks sincerely) Now you're sure, Mary? You don't mind not having the view, or any natural light?

MARY: (Swallowing) I guess not. . . Veronica.

VERONICA: (Shaking forefinger, big smile) Now, now-"Ronnie!" I'll call you " Mary,"-I adore that name!-if you'll call me "Ronnie." (Places a quilted spread on her bed as if to claim it) Now: the closets. Which is your preference, Mary?

MARY: (Squinting and groping about) It's sort of . . . dark. . . over here. I don't see a closet.

VERONICA: The big, spacious one is back beyond your desk; the absurdly cramped one is over here by mine. But please feel free to choose whichever you wish.

MARY: Oh, now I see it! (Opens closet door) Gee, it is spacious.

VERONICA: Obviously, I have many more clothes and suitcases than you do, Mary, but-it's your choice.

MARY: (Apologetically) It probably makes sense for me to take this one, Ronnie, doesn't it?-since it's

VERONICA: (Sharply) What'd you call me, girl?

MARY: "R-Ronnie"

VERONICA: Oh, right-I guess I told you to call me "Ronnie." (Slightly forced smile) If we're going to be roommates I suppose it's best to be informal. (Tapping foot impatiently) Take your time choosing, Mary. We've got all afternoon.

MARY: (Shyly) Well, like I said it probably makes sense for me to take this closet, since it's right beside my

VERONICA: (Now a sincere dazzling smile) Oh, that's sweet of you,

MARY: -thanks. Again Veronica behaves as if Mary has said exactly the reverse of what she has said. Veronica begins to hang up her clothes in the larger closet; Mary has no choice but to hang up her clothes in the other closet.

VERONICA: We'll have dinner together, Mary, O.K.? You can join me and my friends from Exeter-and these really cool guys I just met. Unless you have other plans?

MARY: (Quickly) Oh no, no-I don't know anyone here. It's such a big place and I-I don't know anyone here.

VERONICA: (Squeezing Mary ‘s hand) Well, you know me. As Mary goes to hang up a dress, Veronica pauses to admire it effusively. It is a quite ordinary plaid wool dress with a white bow, white cuffs.

VERONICA: Ooooh! What is this?

MARY: (Shyly) My good wool dress. . .

VERONICA: Where'd you find such a style?

MARY: My grandma sewed it for me. For my eighteenth birthday just two weeks ago.

VERONICA: No! Your grandmother sewed this?- (Making a sewing gesture as if plying a needle) -by hand?

MARY: Oh, no, Grandma uses a sewing machine-a Singer. She's had the same identical machine since 1938.

VERONICA: My grandmothers, they insist we grandchildren call them "Meredith" and "Tracey"-their first names. They look young as my mother. (Laughs) They'd as soon run a sewing machine as a-butter churn. I'm envious! (Holding Mary‘s dress against herself, admiring)

MARY: (Proudly) Actually, Grandma sews all my clothes. She sewed these. (Indicating the nondescript outfit she is wearing.)

VERONICA: Isn't that sweet! Soooo caring! Must be a folkway, or some thing? In Indiana?

MARY: (Shyly) What's a-folkway?

VERONICA: (Airily intellectual) Oh, just some species of unexamined ethnic, religious, or regional custom aborigines persist in practicing over the centuries without a clue as to why. Claude Levi-Strauss is still the most insightful analyst of the phenomenon. (Preening before mirror) You see, Mary, when you wear this, um, most original dress your grandmother sewed for you, you feel happy because you feel loved. That's a folkway.

MARY: Oh. (Wipes at eyes) Gosh, I'm going to m-miss Grandma-so far away!

VERONICA: You see?-emotion of a primitive, visceral, binding nature is generated out of, um, not much. (Examining dress, tums a sleeve roughly inside out) How's this sewed together?-oh! (She has ripped a seam) (Sincerely) Gee, I'm sorry, Mary. Mary tries to take the dress from Veronica but Veronica retains it.

MARY: (Childlike, accusing) You ripped the seam, Veronica. . .

VERONICA: It was an accident, Mary. I said I was sorry.

MARY: You tugged at it, I saw you.

VERONICA: I did not tug, I was just looking. The thread is rotted-see? (Tugs slightly, and another seam rips) That's the cause. Mary takes the dress from Veronica, staggering to her side of the room; contemplates the dress; hangs it in the closet. Veronica has located a camera amid her possessions, and approaches Mary.

VERONICA: Mary?-turn here! Mary turns, and Veronica takes a quick flash photo.

MARY: (A bit blinded) W-What did you do that for?

VERONICA: (A bit evasively) Um-just wanted to. I'm sentimental. This being our first day together, and all. (Pause, warmly) Mary, I know! I'll have your dress mended by this wonderful French seamstress who sews my Momma's clothes. She can replace all that rotted old thread with new. And, um, maybe straighten the hemline. . .

MARY: (Quickly) No, thanks-I'll take the dress home at Thanksgiving, and Grandma can mend it herself. She'd want to.

VERONICA: I just hope these quaint old Midwestern folkways don't die out before Thanksgiving!

MARY: (Coolly) If you mean my Grandma Crockett, she's only eighty- three years old. Her mother is still alive and going strong with her Singer sewing machine-(Proudly) -at the age of one hundred and one.

VERONICA: (Genuinely amazed) No! You actually have a great-grand mother, Mary?-one hundred one years old?

MARY: Great-grandma Quantril is my younger great-grandmother, in fact.

VERONICA: Ooooh! I just have to record this! (She has located a tape recorder amid her possessions; slips in a cassette, sets the machine going) You say, Mary, you have two great-grandmothers?-and how many grandmothers?

MARY: (Staring at recorder) W-What is that?

VERONICA: Oh, probably you don't have these in Indiana-don't pay the slightest heed.

MARY: You're-recording what I say? R-right now?

VERONICA: I said-never mind me, you're the fascinating one of the two of us, Mary. Rich archival lore! (Mysteriously) I see I have much, much to learn this freshman year. Now, about the grandmothers

MARY: (A bit stiffly) I'd rather not discuss my grandmothers any more right now, thanks. "Ronnie."

VERONICA: Oh, but think of those old pioneer women out there on the great cereal plains of America-sewing away. Gives me the shivers!

MARY: Actually... Davenport is a city.

VERONICA: "Davenport"-what's that?

MARY: Where I'm from-Davenport, Ohio. I mean-Iowa. It's a city, not a cereal field. (A bit boastful) We have a population of over one hundred thousand.

VERONICA: (Skeptical) People?

MARY: Yes...

VERONICA: (Catching on) Oh, you mean white people.

MARY: (Noticing tape recorder) Gosh, is that thing still on?

VERONICA: No! (Pretends to be switching the recorder off) There we are: off. (Teasing) My, we're a little thin-skinned, Mary, aren't we? That's how Davenportians are?

MARY: I'm s-sorry, it just makes me n-nervous

VERONICA: You know, Mary, your accent is so interesting. I've never heard one quite like it before.

MARY: My accent? (Veronica tries to hide her laughter.)

MARY: (Hurt) What's so f-funny?

VERONICA: Not a thing. I adore the way you talk, Mary! Look: America is a mosaic of many, many different ways of speech-local customs-"ac-cents"- (She cruelly imitates Mary’s "accent")-it's a democracy and we're all equal.

MARY: We are? Veronica stifles laughter again.

MARY: (Miserably) Everybody's going to laugh at me here-I know it. My professors, my classmates, my r-roommate-In my dreams, all summer, I'd hear strangers laughing at me-but I didn't know why.

VERONICA: (Practicably) Well, now you know. That's a gain.

MARY: Maybe you could h-help me, Ronnie? I could learn to talk like you?

VERONICA: (Graciously) I have no objections if you try to model yourself after me, certainly. My little, um, white-girl roommate at Exeter tried that, too. It was such fun.

MARY: What happened?

VERONICA: Oh, I don't know. We were just roommates a few weeks before she, um, dropped out of school. Vanished without a trace.

MARY: (Grimly) That's what I'm afraid of. Scared to death. I'll fail my subjects-drop out-vanish without a trace. Oh gosh-golly!

VERONICA: (Enunciating in the direction of the recorder) "Gosh-golly!"

MARY: (Upset) Is that recorder-thing still on?

VERONICA: It is not. I told you I turned it off, didn't I?

MARY: Why is this little wheel still going round?

VERONICA: It's unwinding. Relax, Mary. Mary would turn back to continue unpacking, but Veronica detains her. An initial shyness, or a pretense of shyness, on Veronica’s part.

VERONICA: Oh, er. . . Mary? Now we've, um, gotten to know each other so well. . . can I ask you something personal?

MARY: (Guardedly) What?

VERONICA: Your hair.

MARY: (Touching hair, alarmed) My hair? That's a question?

VERONICA: I've always wanted to ask one of you: is your hair naturally that way? Or do you do something to it? Veronica touches Mary’s hair with cautious fingers; her expression is one of someone touching an insect.

VERONICA: SO sort of-fine. Dry. Ooooh!-sort of shivery.

MARY: (Backing off) I d-don't do anything to my hair except shampoo it.

VERONICA: Don't you brush it? Comb it?

MARY: (Hotly) Of course I brush and comb it! I just don't think about it.

VERONICA: (Faint protest) But your hair is-lovely, Mary. It suits you perfectly.

MARY: I-I'd better finish packing, I mean unpacking. . . (Fumblingly re tums to her things)

VERONICA: (Cheerfully) I'd better finish unpacking. We have a date for dinner, remember?-a big table of us. You'll love my friends, Mary. And I know they'll be crazy about you. (Pause) Mary is so rattled she drops something; Veronica doesn't notice.

VERONICA: And these two guys I just met-are they cool. Mary and Veronica are busily hanging up clothes, unpacking suitcases and boxes, etc.

MARY: (Worried) These guys, um-are they?

VERONICA: Seniors. Real hunks!

MARY: Are they, er-?

VERONICA: Good-looking? You bet!

MARY: I mean, um

VERONICA: Tall? For sure. I don't go out with dwarfs!

MARY: (Miserably nervous) I, er, was wondering what-r-r-race

VERONICA: (Surprised) "Race"-?

MARY: I mean, you know-what c-c-color-their skin

VERONICA: "Color?"-"skin?" (A beat.) I didn't notice.

MARY: Oh.

VERONICA: I never notice such superfluities. Race-skin--color: America is a mosaic, we're all absolutely equal, we're beyond primitive divisions of us and them.

MARY: Yes, but I-I get n-nervous, if- I mean, I don't feel comfortable if- I had this feeling, when my folks and I crossed the quad, and came into the dorm here-p-people were watching us.

VERONICA: What kind of people?

MARY: The, uh-majority people. Your people.

VERONICA: Mary, that isn't so! Why'd anybody look at you? (Pause, embarrassed) Oh, um-I didn't mean that the way it sounded. I just meant-people like you are one hundred percent welcome here-this college has been integrated since 1978! Wasn't that a rousing speech the Chancellor gave this morning?- "Giving a Boost to The Needy." And you "Deficiency Scholars" aren't tagged in any obvious way; it's almost as if you scored high SATs and your folks can pay full tuition like the rest of us. Really. Roommates are warned-I mean, notified-but only so we can help tutor you, if necessary. I volunteered to room with one of you, for that purpose.

MARY: Gee, you did?

VERONICA: Well, it fits in with my Freshman Honors Seminar thesis.

MARY: (Stunned) You've chosen your topic already? What is it?

VERONICA: Um... a photo-journal account. Kind of a personal diary. With anthropological and psychological dimensions, of course.

MARY: You're going to write about. . . me?

VERONICA: Oh no, oh no!-don't be silly, Mary. Not you. Not you personally.

MARY: Now I feel kind of. . . funny.

VERONICA: Well, you wouldn't, if you didn't take everything so personally! (Pause) Just be yourself. Be your natural self. That's my philosophy of life.

MARY: (Swallowing hard) "Just be yourself." I'll try, Ver-, "Ronnie." Can I model myself after you?

VERONICA: Oooooh is that sweet! (Gives Mary a quick kiss on the cheek, which quite dazes Mary) But you should just be you, if you know who that is. That's what growing up in America in these enlightened times is all about. Mary and Veronica continue unpacking, etc. Veronica removes her beanie and tosses it onto her bed; Mary, watching her, imitates her-but Mary’s beanie misses her bed. Veronica whistles and moves to suggestive dance music; Mary imitates her, unable to do more than hiss, and moving about most clumsily.

VERONICA: Um- Mary?

MARY: (Eager, yet in dread) Y-Yes, "Ronnie?"

VERONICA: Could you do me a favor and carry this trunk downstairs to the storage room? A beat.

VERONICA: (Radiant smile) I'll be happy to pay you, of course!

MARY: (Stunned) N-Now?

VERONICA: Well, before dinner. Is five dollars enough?

MARY: I...

VERONICA: Ten dollars?

MARY: But I . . . Veronica locates her wallet, takes out a ten-dollar bill, lays it on Mary’s desk with a flourish.

VERONICA: Thanks so much, Mary. I appreciate it. (Pause) These suit cases, now-hmmm!-maybe they can fit into your closet?

MARY: S-Suitcases? Gosh, I don't think so

VERONICA: (Peering into Mary’s closet, shoving clothes on hangers roughly aside) Well, we can try. C'mon, help me. (Veronica and Mary push several of Veronica's suitcases into the closet) Tight fit, but it's O.K. Thanks! Some of Mary’s shoes have been forced out of the closet; Mary, not knowing what to do with them, puts them beneath her bed. Veronica is unnoticing.

MARY: (Plaintively) But, Veronica, here are my own s-suitcases

VERONICA: You can take them down to the storage with you, along with my trunk. They're made of cardboard, not leather-they won't scratch. What's the problem? (Seems genuinely puzzled) Mary covers her face with her hands. During this speech of Veronica's she goes into a trance, stares off into space.

VERONICA: (Shyly boastful) I didn't want to, um, overwhelm you right away, Mary, but. . . my father is Byron T. Scott. (Pause; no response from Mary, but Veronica behaves as if there is) Yes, that's right!-I'm the daughter of Byron T. Scott himself. (Pause) Daddy is in private practice in Manhattan now, but, in the Sixties, I guess you know, he was a renowned civil rights attorney. A personal friend of John F. Kennedy-and Jackie; and, now, Bill and Hillary. (Pause; no response from Mary, but Veronica behaves as if there is) Yes, I sure am lucky, Mary! And I know it. Daddy was a champion of integration from the first. In his law firm he always hired whites-not by quota, either. And the handicapped. (Pause) Physically and mentally challenged-Daddy doesn't discriminate, nor does he allow others to do so. Ooooh no! That's how we were brought up. Veronica has tiptoed over to get her camera, unobtrusively.

VERONICA: (Lyric, sentimental) Mary, I want to share this with you. One of my earliest memories is of my nanny. . . who was white. (Pause) Nellie Fay Cotton, the kindly, obese, diabetic Ozark woman my parents hired at the minimum wage to care for me when I was just a baby. Ooooh did I love Nellie Fay! She was ugly as sin, and, ugh, the ugliest hair-but her soul was beautiful inside. (Pause) Nellie was of welfare stock-had fifteen children by the age of thirty-five-her husband was an unemployed miner with black lung who had nothing to do all day but drink and beat up on her till she finally escaped with her children and fled North-but Nellie never lost her faith in God-never! "The Lord sees into our hearts, He loves us each and every one"- Nellie used to tell me, when I was still in my crib. (Wiping at eyes, maudlin) Then, one summer when I was five or six, these sort of snooty relatives of Momma's were visiting, from Boston, and my aunt's sapphire choker was missing from her room, and Nellie Fay was the suspect of course, and oh! it was so sad!-Nellie Fay was scared and nervous and acted guilty-poor thing! The Greenwich police were called-interrogated Nellie down at the station-did a body check, I guess-didn't find the missing jewelry-but Nellie Fay was dismissed from our household, and went away, and a few days later guess what? Veronica turns dramatically to Mary, who sits as before, staring glassily into space.

VERONICA: You guessed it, Mary!-the damn old choker was found in the deep end of our swimming pool, when the maintenance men came to clean it. Oh, were Momma and Daddy apologetic! Oh, were they chagrined! Right away they sent for Nellie Fay, but it was too late. Poor dear Nellie had killed herself-in shame-swallowed a can of Drano she'd taken out of our kitchen. Oh! the sorrow in our household! the regret! It took Momma weeks and weeks to find an adequate replacement! (Wipes at eyes; pause; she has the camera ready) Excuse me, Mary? Could you look up, and smile? I'd like an intimate shot of both of us. To commemorate our first day together as roommates. The frontispiece of my photo-joumal. . .

VERONICA: (Adjusts camera, positions it on a desk or table facing Mary) Now!-I set this here-set the timer-O.K.! (Hurries to get into the picture, sitting beside Mary on the bed; her arm around Mary’s shoulders and her head close beside Mary’s) One-two-three SMILE! We're going to have a terrific freshman year! Veronica smiles her dazzling smile; Mary remains catatonic but smiles, at last, a ghastly blank wide smile. Camera flashes. Lights out.
```

---

## IC-0651: The New Client

- Title: The New Client
- Author (byline): Paul Donnelley
- Work: Best Ten-Minute Plays of 2019
- Publisher: Smith and Kraus
- Publication date as stated: March 2019
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: LEE-ANN, MARGARET
- Teaser before the introduction: No
- Spoken words (computed): 1373
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul Donnelley
Book: Best Ten-Minute Plays of 2019
ISBN: 978-1575259338
Publisher: Smith and Kraus
Date (Month/Year): March 2019
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: According to an August 17, 2019 article in The Atlantic, “Roughly half of American think federal law bans discrimination on the basis of sexual orientation.”

ACTRESS 2: But these Americans are wrong – the issue is still very murky.

ACTRESS 1: Despite years of acceptance of same-sex marriage nationwide . . .

ACTRESS 2: Despite rapidly growing cultural acceptance for LGBTQ individuals . . .

ACTRESS 1: Despite Pride celebrations from coast to coast.

ACTRESS 2: Cases of gay couples being refused service by florists, bakers, photographers are still making their way through our court systems.

ACTRESS 1: This selection brings the headlines to life with an extra confounding factor –

ACTRESS 2: The attorney hired to protect the rights of a baker who has denied service to a lesbian couple is also gay.

TOGETHER: The New Client by Paul Donnelley

(PG 53-59) At rise: Close to 9 p.m. Sunday. Margaret Henson-Mittendorf is seated on a sofa with an open laptop and stacks of file folders on a coffee table in front of her. Margaret s attention moves from a legal pad on which she is writing to typing on her laptop and back. She is concentrating deeply. There is an unseen television downstage. It is on, but muted. Lights might suggest the flickering screen. The alarm on Margaret s cell phone rings. She is startled, but immediately grabs the phone and silences the alarm.

MARGARET: Heck. Already? MARGARET glances to the television, then begins shutting down

her laptop, straightening the folders and returning them to her briefcase. (calling
```

### Performance text (classify this)

```text
off) Hey Lee-Ann! It's almost time. MARGARET exits quickly and returns with two bottled beers which she places on the coffee table. Lee-Ann! MARGARET picks up and points the remote and clicks off the mute button. We hear the unmistakable strains of the theme to "Game of Thrones." Lee-Ann, it's starting! LEE-ANN HENSON-MITTENDORF enters. She is coiled, poised between fury and betrayal. I got your beer. LEE-ANN glares at her, unmoving.

(turning and seeing LEE-ANN) What? LEE-ANN continues glaring. (gesturing to the television) Can't you let it go for an hour? LEE-ANN continues glaring.

(hitting the mute button) For god's sake.

LEE-ANN: It's completely unacceptable.

MARGARET: It's also completely non-negotiable.

LEE-ANN: How can you say that?

MARGARET: Since when do you get to review my client list?

LEE-ANN: Oh come on . . . this is . . . it's beyond the pale. This isn't just some random client I'm objecting to.

MARGARET: No.

LEE-ANN: It's going to have a huge impact on our lives.

MARGARET: Probably.

LEE-ANN: Then how can you not give me some say . . .

MARGARET: I'm sorry. It's too late. I've said yes.

LEE-ANN: And tomorrow you can go back and tell them no.

MARGARET: I can't . . .

LEE-ANN: You can tell them . . . You can tell them . . . that your marriage is more important than standing up for bigots.

MARGARET: Lee-Ann . . .

LEE-ANN: Or whatever they're paying you.

MARGARET: Wait a minute . . .

LEE-ANN: Or that you had momentarily taken leave of your senses and now you're in your right mind.

MARGARET: Look. You don't have to agree with me. You don't have to support me . . . although that would be nice. But you do have to accept that I am going to represent Shelley and Mark and the bakery.

LEE-ANN: I don't have to accept anything.

MARGARET: (after a beat) No. No, you don't. But your not accepting isn't going to change anything.

LEE-ANN: (after a beat) Does Bert know?

MARGARET: Excuse me?

LEE-ANN: Does Bert know?

MARGARET: Do I have permission from my male [law] partner? ls that what you're asking? Are you serious?

LEE-ANN: Does he?

MARGARET: Yes.

LEE-ANN: So, you discussed this with him but not with me.

MARGARET: Y'know I frequently discuss business with Bert that I don't discuss with you. I don't typically discuss things like the color to paint the guest bathroom or where my wife and I should go on vacation with him; and I don't typically discuss whether or not I'm going to take a case with you.

LEE-ANN: This isn't a typical case! They're bigots . . . hate-mongers . . .

MARGARET: Who have the right to counsel.

LEE-ANN: Maybe. But why do you have to be that counsel?

MARGARET: Because they asked.

LEE-ANN: And you couldn't say no?

MARGARET: Shall we tease out the levels of meaning in that question.

LEE-ANN: Don't . . .

MARGARET: Are you suggesting that I should deny them service because of what they believe?

LEE-ANN: That's not . . .

MARGARET: Or for who they are?

LEE-ANN: They wouldn't serve you!

MARGARET: That is immaterial.

LEE-ANN: No, it isn't!

MARGARET: If Shelly turned up at your studio tomorrow night for the 5:30 Stretch Away Your Day class would you turn her away?

LEE-ANN: She wouldn't.

MARGARET: But if she did . . .

LEE-ANN: They wouldn't bake a cake for a child's birthday party because his mothers . . . because he has two mothers.

MARGARET: I know the particulars of the case.

LEE-ANN: Two women like us. Two women who are friends of ours . . . or who will be until they find out you are defending the bakers who wouldn't bake a cake for their son's birthday! How . . . how can you . . . what kind of internalized horseshit would allow you to think those people were right?

MARGARET: I don't think they're right.

LEE-ANN: You're defending them.

MARGARET: I am exploring the possibility that they may have a legal right to be wrong.

LEE-ANN: Oh my god, what does that even mean in English? No. Never mind. I don't want to hear your brief! Don't make this an abstraction. You were at that party. You know that child. You've known him his whole life. You held him when he was four days old . . . and now you can somehow justify defending people who wouldn't bake him a birthday cake? Really? At no point does simple human decency come into play for you?

MARGARET: I can see you're angry.

LEE-ANN: Oh, don't do that. Don't patronize me.

MARGARET: Okay . . . then give me a little credit.

LEE-ANN: For what?

MARGARET: Oh that's great.

LEE-ANN: What?

MARGARET: Nothing. LEE-ANN glares.

MARGARET: Since there's nothing else to say . . . (picks up the remote)

LEE-ANN: I would appreciate it if you didn't do that.

MARGARET: I would appreciate it if you would support me in this.

LEE-ANN: There's no way.

MARGARET: I haven't mentioned this once in the last four years, but don't you really owe me your support?

LEE-ANN: I can't.

MARGARET: I gave up a partnership for you. I moved to Dogpatch for you. I gave up WBNA season tickets. I have to drive nearly two hours to see a baseball game. I did all of that willingly . . . because I share my life with you and you needed to be here for your mother. Because your mother couldn't leave Dogpatch. Oh no. God forbid!

LEE-ANN: What's your point?

MARGARET: A little quid pro quo?

LEE-ANN: No. This isn't about a little career disruption . . .

MARGARET: Oh my god . . .

LEE-ANN: This isn't about a few life-style sacrifices . . .

MARGARET: You really want to stop . . .

LEE-ANN: This is a matter of pure and clear right and wrong. These people are wrong. Being on their side is wrong.

MARGARET: Then maybe you'd be happier moving in with your mother until this blows over.

LEE-ANN: Maybe I should . . . (There is a long moment of silence.)

MARGARET: Okay then.

LEE-ANN: That's it? That's all you have to say? You would let me move out?

MARGARET: That is entirely your choice to make.

LEE-ANN: Can you at least tell me why . . .

MARGARET: I was calling their bluff.

LEE-ANN: What?

MARGARET: Shelley and Mark came into my office expecting me to say no. Expecting to be able say "See, the lesbian lawyer wouldn't take our case. Oh, the hypocrisy!" I'm sure there was conference room full of high-priced talent up at Jones-Day who soiled themselves when the call came in that I said yes.

LEE-ANN: And you're not going to represent them all that effectively!

MARGARET: What? Do you really have no respect for me at all?

LEE-ANN: That would at least make sense.

MARGARET: No, it wouldn't. I am going to give this my best shot.

LEE-ANN: That's appalling.

MARGARET: Oh, I'm likely to lose. While Shelley and Mark are now stuck with little ole' me, Dee and Kelli have the HRC and millions of dollars' worth of real legal talent on their side. And our case is weaker. We'll probably do okay in Georgia, but we'll get our clocks cleaned in Federal court.

LEE-ANN: But meanwhile you'll be all over the news . . .

MARGARET: And think of the cognitive dissonance it would cause if the bigot baker's lawyer had her wife standing at her side during all those press moments.

LEE-ANN: There's no way . . .

MARGARET: Think about it.

LEE-ANN: I couldn't . . .

MARGARET: Sometimes infiltration can be as effective as confrontation. The optics will kill. Time and time and time again.

LEE-ANN: And millions of people will think what's wrong with those two? What kind of self-hatred would let them . . . ?

MARGARET: I do worry about getting lumped in with the Log Cabin losers.

LEE-ANN: Exactly.

MARGARET: Think of it as taking one for the cause. A big one, I'll grant you.

LEE-ANN: I can't. I guess I don't have your moral sophistication or something. I have to say wrong is wrong and I won't be a party to it.

MARGARET: I'm sorry you feel that way.

LEE-ANN: It will define us for the rest of our lives . . . the traitors . . . the champions of bigotry!

MARGARET: But we'll know better.

LEE-ANN: That's not enough. For me. I can't live a life of lonely virtue for thirty or forty years.

MARGARET: I can't make you stand with me.

LEE-ANN: Are you really going to do this? In spite of how I feel about it? In spite of what it's going to do to my life without my agreement?

MARGARET: Yes.

LEE-ANN: That's it? "Yes"?

MARGARET: Yes. You're always asking me to "speak English." So here it is, clearly and unequivocally: Yes. I am going to defend the right of the Sitton Family Bakery to refuse to make a birthday cake for the son of two lesbians.

LEE-ANN: No matter what it does to me.

MARGARET: Yes.

LEE-ANN: (after a long beat) Wow. LEE-ANN turns to walk out of the room.

MARGARET: Where are you going?

LEE-ANN: I'll let you know when I decide. LEE-ANN exits. MARGARET picks up a beer and sits. She sits holding the beer and thinking for a beat. She takes a sip, then picks up the remote as lights fade to black.
```

---

## IC-0652: ‘Night Mother

- Title: ‘Night Mother
- Author (byline): Marsha Norman
- Work: Not specified
- Publisher: Noonday Press
- Publication date as stated: Aug 1983
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JESSIE, THELMA
- Teaser before the introduction: No
- Spoken words (computed): 2194
- Already set (do not supply): none

### Source block (context only)

```text
Author: Marsha Norman
ISBN: 978-0374521387
Publisher: Noonday Press
Date (Month/Year): Aug 1983
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Suicide takes the lives of nearly 40,000 Americans every year.

ACTRESS 2: And although the reasons why vary from individual to individual, it remains an act that survivors struggle to understand regardless of the reasons.

ACTRESS 1: In Night Mother by Marsha Norman, we experience the complete resolve of one young woman, Jessie, who has chosen to end her life

ACTRESS 2: And her mother, who spends the last evening alone with her daughter

TOGETHER: Night Mother by Marsha Norman
```

### Performance text (classify this)

```text
JESSIE: (Pg 9-11) We got any old towels? (holding a towel that was on the stack of newspapers) Towels you don't want any more. How about this swimming towel Loretta gave us? Beach towel, that's the name of it. You want it? (Mama shakes her head No.) And a big piece of plastic like a rubber sheet or something. Garbage bags would do if there's enough.

THELMA: Don't go making a big mess, Jessie. It's eight o'clock already. Your hair is black enough, hon.

JESSIE: (continues to search the kitchen cabinets, finding two or three more towels to add to her stack) It's not for my hair, Mama. Where's Daddy's gun?

THELMA: In the attic. (Jessie goes off stage – to attic) One of his shoeboxes, I think . . . What do you want the gun for, Jess?

JESSIE: Protection.

THELMA: I don't like the idea of a gun, Jess.

JESSIE: (Pg 12) (calling down from the attic) Which shoebox, do you remember?

THELMA: You come down from there before you have a fit. I can't come up and get you, you know.

JESSIE: Here it is. I found it. (trying to be calm) (Pg 13-14 The gun is for me. I'm going to kill myself, Mama.

THELMA: (going to the sofa) Very funny. Very funny.

JESSIE: I am.

THELMA: (quickly, irritated) You are not! Don't even say such a thing, Jessie.

JESSIE: How would you know if I didn't say it? You want it to be a surprise? You're lying there in your bed or maybe you're just brushing your teeth and you hear this . . . noise down the hall?

THELMA: Kill yourself.

JESSIE: Shoot myself. In a couple of hours.

THELMA: It must be time for your medicine.

JESSIE: Took it already.

THELMA: Then what's the matter with you?

JESSIE: Not a thing. Feel fine.

THELMA: You feel fine. You're just going to kill yourself.

JESSIE: Waited until I felt good enough, in fact.

THELMA: Don't make jokes, Jessie. I'm too old for jokes.

JESSIE: It's not a joke, Mama. (Mama watches for a moment in silence)

THELMA: (Pg 16 – 17) We're just going to sit around like every other night in the world and then you're going to kill yourself? (Jessie doesn't answer) You'll miss. (again, no response) You'll just wind up a vegetable. How would you like that? You know what the doctor said about getting excited. You'll cock the pistol and have a fit.

JESSIE: I think I can kill myself, Mama.

THELMA: You're not going to kill yourself, Jessie. You're not even upset! (Jessie smiles, or laughs quietly, and Mama tries a different approach) People don't really kill themselves, Jessie. No, Ma’am, doesn't make sense, unless you're deranged and you're as normal as they come, Jessie, for the most part.

JESSIE: It's exactly what I want. It's dark and quiet.

THELMA: So is the back yard, Jessie! Close your eyes. Stuff cotton in your ears. Take a nap!

JESSIE: So quiet I don't know it's quiet. So nobody can get me. Dead is everybody and everything I ever knew, gone. Dead is dead quiet.

THELMA: It's a sin. You'll go to hell.

JESSIE: Uh-huh.

THELMA: You will! (Jessie doesn't answer. She puts the now loaded gun back in the box and crosses to the kitchen. But Mama is afraid she is headed for the bedroom. In a panic) You can't use my towels! They're my towels. I've had them for a long time. I like my towels. And you can't use your father's gun either. It's mine now too. And you can't do it in my house.

JESSIE: Oh, come on. If I'd known you were going to act like this. I wouldn't have told you.

THELMA: How am I supposed to act? Tell you to go ahead? O. K. by me, sugar. Might try it myself. What took you so long?

JESSIE: There's just no point in fighting me over it, that's all. Want some coffee?

THELMA: (Pg 21) Your eyes don't look right. I thought so yesterday.

JESSIE: That was just the ragweed. I'm not sick.

THELMA: Epilepsy is sick, Jessie.

JESSIE: It won't kill me. (a pause) If it would. I wouldn't have to.

THELMA: You don't have to.

JESSIE: No, I don't. That's what I like about it. Mama . . . (Pg 22) I'm just not having a very good time and I don't have any reason to think it'll get anything but worse. I'm tired. I'm hurt. I'm sad. I feel used.

THELMA: Tired of what?

JESSIE: It all.

THELMA: What does that mean?

JESSIE: I can't say it any better.

THELMA: Well, you'll have to say it better because I'm not letting you alone til you do. How long have you been thinking about this?

JESSIE: Off and on, ten years. On all the time, since Christmas.

THELMA: (Pg 24) You're feeling sorry for yourself! You're not having a good time! Whoever promised you a good time? Do you think I've had a good time? (Pg 25-26) You're acting like some little brat, Jessie. You're mad you're miserable and it's your own sweet fault.

JESSIE: And it's time I did something about it.

THELMA: Not something like killing yourself.

JESSIE: I'll do whatever you want before I go.

THELMA: (badly frightened by those words) You could get a job!

JESSIE: You know I couldn't work. I can't do anything. I've never been around people my whole life except when I went to the hospital. I could have a seizure any time. What good would a job do? The kind of job I could get would make me feel worse. (taking charge of this) (Pg 43- 44) What do they look like? The seizures.

THELMA: (reluctant) Different each time, Jess. There's not much to tell. You just . . . crumple, in a heap, like a puppet and somebody cut the strings all at once, you just slide down the wall, you know.

JESSIE: My head turns around and I fall down and then what?

THELMA: Well, your chest squeezes in and out and you sound like you're gagging, sucking air in and out like you can't breathe.

JESSIE: Do it for me. Make the sound for me.

THELMA: I will not. It's awful sounding.

JESSIE: Yeah. It felt like it might be. What's next.

THELMA: Then you turn blue and the jerks start up. Like I'm standing there poking you with a cattle prod. And then the jerks slow down and you wet yourself and it's over. Two minutes tops. (then making a real effort) But Jessie, you haven't had a seizure for a solid year. A whole year, do you realize that?

JESSIE: Yeah, the phenobarb's about right now, I guess. I sure am feeling good. I really am. The double vision's gone and my gums aren't swelling. No rashes or anything. I'm feeling as good as I ever felt in my life. I'm even feeling like worrying or getting mad and I'm not afraid it will start a fit if I do. I just go ahead.

THELMA: Of course you do! You can even scream at me, if you want to. I can take it. You don't have to act like you're just visiting here, Jessie, this is your house too.

JESSIE: The best part is my memory's back. (folding the rest of the laundry) (Pg 45) Yes, Mama. Once I started remembering, I could see what it all added up to.

THELMA: (Pg 47) (beginning to break down) Maybe I fed you the wrong thing. Maybe you had a fever some time and I didn't know it soon enough. Maybe it's a punishment.

JESSIE: For what?

THELMA: I don't know. Because of how I felt about your father. Because I didn't want any more children. Because I smoked too much or didn't eat right when I was carrying you. It has to be something I did.

JESSIE: It does not. It's just a sickness, not a curse. Epilepsy doesn't mean anything. It just is.

THELMA: I'm not talking about the fits here, Jessie! I'm talking about this killing yourself. It has to be me that's the matter here. . . I don't know what I did, but I did it, I know. This is all my fault, Jessie, but I can't do anything about it!

JESSIE: (Pg 26) (quietly) No. You can't. (Mama slumps, if not physically, at least emotionally) And I can't do anything either, about my life, to change it, make it better, make it work. But I can stop it. Shut it down, turn it off like the radio when there's nothing on I want to listen to. It's all I really have that belongs to me and I'm going to say what happens to it. And it's going to stop. I'm going to stop it.

THELMA: (Pg 47-48) Everything you do has to do with me, Jessie. You can't do anything, wash your face or cut your finger, without doing it to me. That's right! You might as well kill me as you, Jessie, it's the same thing. This has to do with me, Jessie.

JESSIE: Then what if it does! What if it has everything to do with you! What if you are all I have and you're not enough? What if I could take all the rest of it if only I didn't have you here? What if the only way I can get away from you for good is to kill myself? What if it is? I can still do it!

THELMA: (in desperate tears) Don't leave me, Jessie! (Jessie stands for a moment, then turns for the bedroom) No! (grabs her arm) Jessie, how can I . . . (has to stop a moment.) How can I get up every day knowing you had to kill yourself to make it stop hurting and I was here all the time and I never even saw it. And then you gave me this chance to make it better, convince you to stay alive and I couldn't do it. How can I live with myself after this, Jessie?

JESSIE: I only told you so I could explain it, so you wouldn't blame yourself. There wasn't anything you could say to change my mind. I didn't want you to save me. I just wanted you to know.

THELMA: Stay with me just a little longer. Just a few more years. I don't have that many more to go, Jessie. And as soon as I'm dead, you can do whatever you want.

JESSIE: (Pg 49) Don't you see, Mama, everything I do winds up like this. How could I think you would understand? We could hold hands for an hour and then I could go shoot myself? I'm sorry about tonight, Mama, but it's exactly why I'm doing it.

THELMA: If you've got the guts to kill yourself, Jessie, you've got the guts to stay alive.

JESSIE: I know that. So it's really just a matter of where I'd rather be.

THELMA: Look, maybe I can't think of what you should do, but that doesn't mean there isn't something that would help. You can keep trying. You can get brave and try some more. You don't have to give up!

JESSIE: I'm not giving up! This is the other thing I'm trying. And I'm sure there are some other things that might work, but might work isn't good enough anymore. I need something that will work. This will work. That's why I picked it.

THELMA: (Pg 50-52) You are my child!

JESSIE: I am what became of your child. (Mama cannot answer) I found an old baby picture of me. And it was somebody else, not me. It was somebody pink and fat who never heard of sick or lonely, somebody who cried and got fed, and reached up and got held. That's who I started out and this is who is left. (no self-pity here) That's what this is about. It's somebody I lost, all right, it's my own self. Who I never was. Or who I tried to be and never got there. Somebody I waited for who never came. And never will. I'm what was worth waiting for and I didn't make it. Me . . . who might have made a difference to me . . . I'm not going to show up, so there's no reason to stay, except to keep you company, and that's . . . not reason enough.

THELMA: (quickly) Jessie, I can't just sit here and say O. K., kill yourself if you want to. (Jessie turns away) Who am I talking to? You're gone already, aren't you? I can't stop you because you're already gone! (beat, a different tactic) Well, nobody's going to be a bit surprised, sweetheart. This is just like you. Do it the hard way, that's my girl all right. (Jessie gets up and goes into the kitchen, but Mama follows her.) You know who they're going to feel sorry for? Me! How about that! Not you, me! They're going to be ashamed of you. Yes. Ashamed!

JESSIE: Leave me alone.

THELMA: It's the truth!

JESSIE: I should've just left you a note!

THELMA: (screaming) Yes! (then suddenly understanding what she has said, nearly paralyzed by the thought of it, she turns slowly to face Jessie, nearly whispering) No. No. I . . . might not have thought of all the things you've said.

JESSIE: It's O. K., Mama. (beat) (Pg 53) Now, somebody's bound to ask you why I did it and you just say you don't know. That you loved me and you know I loved you and we just sat around tonight like every other night of our lives and then I came over and kissed you and said, " 'Night, Mother," and you heard me close my bedroom door and the next thing you heard was the shot.

THELMA: (quietly) It was something personal.

JESSIE: Good. That's good, Mama. (standing behind Mama now, holding her shoulders) (Pg 54) Now, when you hear the shot, I don't want you to come in. First of all, you won't be able to get in by yourself, but I don't want you trying. Call the police. And then you'll need something to do til somebody gets here, so wash the hot chocolate pan. You wash that pan til you hear the doorbell ring and I don't care if it's an hour, you keep washing that pan.

THELMA: I'll make my calls and then I'll just sit. I won't need something to do.

JESSIE: (Pg 56- 58) It's time for me to go, Mama.

THELMA: (starting to her) No, Jessie, you've got all night! (grabs her) It's not even ten o'clock.

JESSIE: (very calm) Let me go, Mama.

THELMA: I can't. You can't go. You can't do this. You didn't say it would be so soon, Jessie. I'm scared. I love you.

JESSIE: (takes her hands away) Let go of me, Mama. I've said everything I had to say. Don't try and stop me, Mama, you can't do it.

THELMA: (grabs her again, this time hard) I can too! I'll stand in front of this hall and you can't get past me. (they struggle) You'll have to knock me down to get away from me, Jessie, I'm not about to let you . . . (in the struggle, Jessie gets away from her)

JESSIE: (almost a whisper) 'Night, Mother. (Jessie vanishes into her bedroom and locks the door just as Mama gets to it)

THELMA: (screams) JESSIE! (pounds on the door) Jessie! Stop this! I didn't know! I was here with you all the time. How could I know you were so alone? (stops for a moment, breathless and frantic, putting her ear to the door and when she doesn't hear anything, she stands back up straight again and screams once more) Jessie! Please! (gunshot -- Mama collapses against the door, tears streaming down her face) Jessie, Jessie, child . . . Forgive me.
```

---

## IC-0653: Nightswim

- Title: Nightswim
- Author (byline): Julia Jordan
- Work: 30 Ten-Minute Plays from the Actors Theatre of Louisville for 2 Actors
- Publisher: Smith & Kraus
- Publication date as stated: Sept 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ROSIE, CHRISTINA
- Teaser before the introduction: No
- Spoken words (computed): 1238
- Already set (do not supply): none

### Source block (context only)

```text
Author: Julia Jordan
Book: 30 Ten-Minute Plays from the Actors Theatre of Louisville for 2 Actors
ISBN: 978-1575252773
Publisher: Smith & Kraus
Date (Month/Year): Sept 2001
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Girls are intelligent creatures.

ACTRESS 2: They think more than boys do.

ACTRESS 1: So, before making a decision, we weigh the options.

ACTRESS 2: (to Actress 1) YOU weigh the options – I prefer to act on impulse.

ACTRESS 1: But there could be dangers inherent in spontaneity.

ACTRESS 2: Dangers like having fun!

TOGETHER: Nightswim by Julia Jordan
```

### Performance text (classify this)

```text
ROSIE: (whispers loudly) Christina. Christina! (C comes to the window. She has not been sleeping.)

CHRISTINA: What?

ROSIE: Come out and play.

CHRISTINA: We're too old to play.

ROSIE: Wanna do something?

CHRISTINA: What?

ROSIE: I don't know, something.

CHRISTINA: Like what?

ROSIE: Wanna go climb the old railroad bridge? Cross the river?

CHRISTINA: We're too old to climb the railroad bridge.

ROSIE: Go skinny-dipping in the old man's pool?

CHRISTINA: He's always watching.

ROSIE: So?

CHRISTINA: It's undignified.

ROSIE: We'll go to the lake.

CHRISTINA: The police will catch us.

ROSIE: They haven't all summer.

CHRISTINA: We haven't gone all summer.

ROSIE: So they won't expect us.

CHRISTINA: It's cold.

ROSIE: That'll make the water feel warm, like swimming in velvet.

CHRISTINA: There's no lifeguard.

ROSIE: So we can swim naked.

CHRISTINA: What if we drown like the Berridges' boy? Our bodies would get caught under the weeping willow in the water. No one would find us for weeks.

ROSIE: We won't go anywhere near that tree.

CHRISTINA: But there's no lifeguard.

ROSIE: You forgot how to swim?

CHRISTINA: No.

ROSIE: Let's go.

CHRISTINA: I'm tired.

ROSIE: Skinny-dipping is like resting itself.

CHRISTINA: What if that rapist with the mustache and the beady eyes is out there?

ROSIE: He's in jail.

CHRISTINA: There could be another one. Beady-eyed rapists are a dime a dozen. A copycat crazy.

ROSIE: Black water, black night. He won't even see us.

CHRISTINA: Our skin glows like sixty-watt bulbs at night.

ROSIE: The water will cover us.

CHRISTINA: He'll come in after us.

ROSIE: Rapists can't swim so good.

CHRISTINA: He'll get us on the beach.

ROSIE: You can run, can't you?

CHRISTINA: He has a fast car.

ROSIE: You can hide, can't you?

CHRISTINA: He carries a flashlight. He senses fear. He'll find me.

ROSIE: You can fight, can't you?

CHRISTINA: He's bigger than me.

ROSIE: You can scream, can't you?

CHRISTINA: No one will hear me.

ROSIE: I'll hear you. Two against one.

CHRISTINA: What if there are two of him? Or three? Or a gang of crazies hiding under the weeping willow tree waiting for us.

ROSIE: We won't go anywhere near that tree.

CHRISTINA: What if there are two?

ROSIE: What if there are none?

CHRISTINA: I can't.

ROSIE: You're scared?

CHRISTINA: Yes.

ROSIE: Admit it.

CHRISTINA: I do.

ROSIE: Say it.

CHRISTINA: I'm scared.

ROSIE: Don't be.

CHRISTINA: Why not?

ROSIE: 'Cause it's a beautiful night for a swim.

CHRISTINA: It is?

ROSIE: The water will be like swimming in black velvet because the air is cool. The lake will be all ours because everyone is locked up in sleep. We will swim naked because there is no lifeguard. And there won't be any crazies because I have a feeling. (Beat.) It's a beautiful night for a swim.

CHRISTINA: The police.

ROSIE: It won't be the same ones.

CHRISTINA: What if it is?

ROSIE: They change their beats.

CHRISTINA: What if they haven't?

ROSIE: That was last summer.

CHRISTINA: I saw them, a picture of them, in the paper today.

ROSIE: I saw it, too.

CHRISTINA: They saved a mother's little girl. CPR. She called them heroes.

ROSIE: It's good they saved her girl.

CHRISTINA: Heroes.

ROSIE: They're heroes.

CHRISTINA: Heroes can do anything they want, you know. They give them the key to the city and stuff like that. They could catch us swimming naked and take our clothes and make us leave the water all naked and shine their flashlights on us and hold our clothes above their heads and laugh and say, "Jump." You'll cry.

ROSIE: I will not cry.

CHRISTINA: I won't know what to do. I'll jump and they'll laugh and I won't know what to do. I'll jump.

ROSIE: I promise you, on my honor, I will not cry.

CHRISTINA: What will you do if those heroes come?

ROSIE: I will hide under the weeping willow branches that grace the lake.

CHRISTINA: You said we wouldn't go anywhere near that tree.

ROSIE: I'll swim to the middle of the lake and tread water until they leave.

CHRISTINA: Your legs will tire. You'll drown like the Berridges' boy.

ROSIE: I'm a strong swimmer.

CHRISTINA: They'll come in after you.

ROSIE: They won't get their uniforms wet. It'd tarnish their medals.

CHRISTINA: They could take off their uniforms.

ROSIE: Then they wouldn't be cops.

CHRISTINA: They could take of their medals.

ROSIE: Then they wouldn't be heroes.

CHRISTINA: They could take our clothes and drive away in their police car. Sirens and lights and them laughing.

ROSIE: We'll drive home naked.

CHRISTINA: Our moms will catch us.

ROSIE: They've seen us naked before.

CHRISTINA: What if it's our Dads?

ROSIE: That won't happen.

CHRISTINA: What if it does? Naked? (beat)

ROSIE: (In a father's voice) "NO MORE SKINNY-DIPPING BEHIND OUR BACK - SNEAKING AROUND - DOING WHATEVER YOU PLEASE - FOR YOU, YOUNG LADY."

CHRISTINA: Those are your favorite jeans they'd be driving off with. You'd never get them back.

ROSIE: I don't care.

CHRISTINA: Took you two years to break them in.

ROSIE: I'll hide them in a tree.

CHRISTINA: There's only the weeping willow.

ROSIE: I know.

CHRISTINA: They'll find our clothes again and they'll know they've got two naked girls again. And one will shine his flashlight on you and one will shine his flashlight on me. And the water that maybe was like swimming in black velvet when we were alone and moving will be cold when we're still and shivering and your tan skin will turn white and frightened. They'll see right into us. Your eyes will fix on them and you won't look at me. You won't tell me what to do and I'll be so cold. They'll say, "Come on out now, girls." And the water will fall away from your body with only hands and wrists, white elbows and arms to cover you. Your arms look so breakable. And I'll follow you watching the water run down your back. The flashlights will glare down our faces, down our legs. They'll shine their flashlights one for each of us. They'll smile at us trying to cover ourselves. They'll hold our clothes above their heads and smile at us naked and say, "Jump." And you'll cry and I'll cry and I'll jump.

ROSIE: We'll walk out of that lake like we've got nothing to be ashamed of and we'll look them right in the eye.

CHRISTINA: We won't cry?

ROSIE: We will not cry.

CHRISTINA: When they hold our clothes above their heads and won't give them back and say "Jump"?

ROSIE: We will not cry. You will not jump.

CHRISTINA: When they say with grins on their faces and our clothes in their hands, when they say

ROSIE: (cutting Christina off) "Lucky for you."

CHRISTINA: "Lucky for you it was just cops that found you and not some crazy sicko."

ROSIE: "Murderous Peeping Tom."

CHRISTINA: "Rapist."

ROSIE: "What are you two thinking about swimming at this hour with no lifeguard?"

CHRISTINA: "What if a storm came up all of a sudden and lightning struck the lake?"

ROSIE: "Why, you could be electrocuted!"

CHRISTINA: "What are you thinking about swimming with no clothes on?"

ROSIE: "You could catch a chill and die of pneumonia!"

CHRISTINA: "It's cold at night with no sun!"

ROSIE: And when they say, "Run along home now, girls."

CHRISTINA: "Before we call your parents."

ROSIE: We'll just stare at them, but we won't say a word.

CHRISTINA: We won't.

ROSIE: We won't stoop to their talk, talking nonsense. We'll just press them with our knowing eyes and they'll know that we know better.

CHRISTINA: We know all about skinny-dipping at midnight.

ROSIE: Warm, black water, black sky, no flashlights to trash the darkness, one moon, some stars, and a weeping willow tree. A perfectly beautiful night for a swim.

CHRISTINA: Standing there naked we will not cry.

ROSIE: We will not.

CHRISTINA: I can't

ROSIE: Why?

CHRISTINA: The floorboards creak, they'll wake up.

ROSIE: Tiptoe.

CHRISTINA: My parents have radar.

ROSIE: Climb out the window.

CHRISTINA: There's nothing to climb.

ROSIE: Jump.

CHRISTINA: It's a long way down.

ROSIE: Bend your knees when you land.

CHRISTINA: Catch me.

ROSIE: You're too old for catching.

CHRISTINA: (climbs into the window frame) Just jump and bend my knees?

ROSIE: I don't like to swim alone.

CHRISTINA: It is a beautiful night for a swim.

ROSIE: C'MON JUMP. (Christina jumps)
```

---

## IC-0654: The Notebook

- Title: The Notebook
- Author (byline): Wendy Kesselman
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: WARREN, MISS THORNE, JENNIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1941
- Already set (do not supply): none

### Source block (context only)

```text
Author: Wendy Kesselman
ISBN: 978-0822219064
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 2003
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Maya Angelou once said . . . This is the value of the teacher, who looks at a face and says there's something behind that and I want to reach that person . . .

ACTOR 2: I want to influence that person, I want to call out that person who is behind that color, behind that language, behind that culture.

ACTOR 1: I believe you can do it....

ACTOR 2: But the flip side of this empowerment is also true. A teacher can crush the hopes and dreams of a student just as easily. . .

ACTOR 1: with a word, a tone, a look or an indifference that can extinguish the light behind a student’s eyes, crush a burgeoning spirit and forever impact the joy of learning and growing.

ACTOR 2: The Notebook by Wendy Kesselman captures the extreme vulnerability of students who are ever-sensitive to the judgement of their mentors

TOGETHER: The Notebook by Wendy Kesselman
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NOTE: This cutting has been prepared with the vision of 2 females performing the selection. Actor 1 plays the role of Jennie; Actor 2 plays the role of Miss Thorne and Warren (who in the original script is a male; but there is little gender specific notations/pronouns in the text).

(Light comes up on Warren Stone, thirteen, sitting on the edge of the stage, busy writing in a small red notebook. The light suddenly exposing him, he looks up anxiously, then leans forward, speaks to us confidentially.)

WARREN: I have a secret. A terrible secret no one knows. (In a hushed whisper.) I like to read. (Quiet.) War and Peace. My favorite! And in it I found the one person I'd waited for my whole life, the person I'd die for, my favorite, my only heroine - Natasha! (A pause.) But I can't go into that now. Because now there's another story, and it's all in here -

(Opening the small red notebook.) in my notebook. (He leans even closer to us.) You see . . . there's this teacher, this terrible teacher. (pause.) Miss Thorne.

(Pacing out, Miss Thorne speaks a poem to a group of unseen girls.)

MISS THORNE: (With an English accent.)
I think continually of those who were truly great.
Whose lovely ambition
Was that their lips, still touched with fire,
Should tell of the Spirit, clothed from head to foot in song.

I hope that perhaps one day I too will "think continually of those who were truly great" – (pause.) Of all of you perhaps, (Another pause.) or at least of some of you - ( soft laugh.) Well, let's be realistic and hope that maybe one of you, just one, with talent, hard work, luck and determination, will remember . .

WARREN: Well, anyway, that's what she's like - (Leaning closer.) This fall, suddenly, she took a liking to me. Me! Of all people. Anyway, one day in September - (Checking his notebook.) September twenty-third, to be precise - Miss Thorne [summomed] me.

(Light dims on warren and comes up swiftly on an enchantingly romantic adolescent girl with long hair and haunting, expressive eyes. Jennie, reciting Keats' "La Belle Dame Sam Merci" with a slight Russian accent.)

JENNIE:
O what can ail thee, Knight at arms,
Alone and palely loitering?
The sedge has withered from the lake,
And no birds sing.
I met a Lady in the meads,
Full beautiful, a faery's child,
Her hair was long, her foot was light,
And her eyes were wild -
She found me roots of relish sweet,
And honey wild, and manna dew,
And sure in language strange she said,
"I love thee true."

WARREN: I couldn't move, couldn't breathe. I recognized her, knew her right away ... Natasha! Just the way I always imagined her, the way she is in my favorite, my absolute favorite -- War and Peace ... (Light comes up on Miss Thorne, gazing at Jennie.)

MISS THORNE: Well! Is it possible? Right here in our own classroom, someone who makes poetry alive for us, who makes words live. With passion. Such passion! (Looking out at the class.) Spoken by a girl who had to come from so far away to make us feel at home with our own language again. All the way from Russia, isn't it, Jennie? (Jennie nods, looks down, then up again quickly at warren, with a shy, joyous smile.)

WARREN: Jennie. Jennie! Oh my God. My God! Okay, okay, so her name wasn't Natasha. So what? She was my heroine, my Natasha. (A pause - His face aglow.) A reader. Another reader! For how could she have read that poem with such emotion, such feeling, if she weren't a reader herself? (He pauses.)

MISS THORNE: A rare child. A rare bird. A bird about to fly. In all my years of teaching I've never ... (pause.) Who knows where it will lead? (Light dims on Miss Thorne and comes up on Jennie in a worn handmade coat, shivering with the cold.) **************

JENNIE: I'm not ashamed! I just thought it would be easier if you picked me up a little bit further away from the school. Easier for you I mean. (Pause - Slowly) Every day from now on. (Pause.) What do you mean - you'd never live to see this happen? (Pause.) Shame has nothing to do with it! (She hesitates.) But of course, if you don't want to - (A pause.) You will? Really? Really, Papa? (Quiet.) That's great. (Her voice choked) Thank you. (Quickly changing the subject.) Oh guess what we had in Assembly again today ... Impromptu Speaking! It reminds me of those theatre improvisations we used to do with Mama back home. Miss Thorne sits on the stage with a red handbag and this little blue book. Inside the bag are the names of everyone in the school. She always has Warren pick the names out of the bag. Guess whose name [was] picked this time? (Light comes up on Miss Thorne, the red handbag at her side.) Mine, Papa! And guess what the word was ...

MISS THORNE: (Opening the small blue book, her finger pointing to a word.) "Theorem."

JENNIE: (Laughing happily.) All I could think to talk about was that Pythagorean Theorem and how I can never get it right. They all laughed, Papa. Like they accepted me ... for the first time. And Miss Thorne laughed too. So hard, so hard. (Clutching the small blue book, Miss Thorne rocks back and forth, laughing soundlessly) It's wonderful to make someone laugh, Papa. The way I used to make you and Mama laugh. Around the kitchen table. (A pause.) At home. (For moments she stares at the back of his head, then turns and looks out the window. A tear glistens on her cheek.) We used to laugh like that all the time ... at home ... in Russia. We used to ... But that's all gone. Now everything's- **************************

MISS THORNE: (Leaning closer.) Listen. I want to let you in on a secret. (Lowering her voice.) Tomorrow, tomorrow we embark on a journey into the unknown. (Almost breathless) Most of us, after countless obstacles, have finally - finally! - begun to read. But to write! To put our secret thoughts, secret feelings no one in the world knows, down on paper. Who knows what treasures may be revealed when tomorrow, tomorrow at last, we begin to write.

****************************

JENNIE: (Light coming up on her face, as she says her composition from memory aloud.) Home. Russia! Home! The winding rivers, the vast lakes, the birch trees unfolding forever like the pages in my book of fairy tales. Home! Where my father, a physicist, a mathematician, made up theories all day and all night. Home! Where my mother made the most magical costumes in the world, and where we'd arrive at her theatre opening night dressed more outrageously than the actors themselves! Oh, the laughter, the excitement, the kisses, the hugs ... (A pause.) But one day my mother came home early - there was no theatre anymore. My father locked his books in a cabinet - the Mathematical Institute had shut its doors. My mother stopped making costumes and started fixing hems. She became a seamstress. My father stopped making up theories and started selling newspapers out on the street. And we came here, to this coun-try ... to our new home. (Light comes up on Miss Thorne, listening intently.) Have you ever noticed, on a weeknight, how all the office windows in midtown are lit up at one o'clock in the morning? That's when the women are cleaning, cleaning the buildings after they close. That's where my mother washes her floors every night. My father picks her up in the cab he drives. I speak English to them all the time. They understand it, but they won't speak a single word. They're totally cut off, can't understand Americans at all.

I'm their only child. I've got to do well for them, make them feel I belong, so maybe someday they will too. (Light comes up more folly on her as she steps even closer to us, right up to the edge of the stage.) Listen. Shall I tell you something? Yesterday my father drove his cab past the school. I was walking with Heather and Janet and Jane and pretended I didn't see him, didn't even know him. My father! A great mathematician, a member of the Academy of Sciences ... now driving a taxi sixteen hours a day, taking orders from drunken men, while his only daughter walks the other way. (A pause.) Will I ever stop feeling embarrassed, ashamed? Will I ever really ... really belong? Will I ever be able to say that this ... this America ... has become my "safe dwelling"? Will I ever be able to call it my home? (Her face aglow, Miss Thorne comes toward Jennie.)

MISS THORNE: Well, Jennie. I ... I'm absolutely - (Looking out, suddenly aware of her class, she continues briskly.) You need to polish up your grammar of course, work on your sentence structure, enlarge your vocabulary, but, I think I can venture to say that yes ... yes ... it certainly is a start.

WARREN: A start! Was she kidding? It was perfect! The best essay I'd heard in my entire life.

JENNIE: (To Warren - Breaks into a vivid smile.) Tomorrow, when we read out own poem, the one we made up ourselves –

WARREN: (Turning to us.) She was so excited, so worked up I got worried. (a step forward} You made one up already?

JENNIE: Right after she gave me the assignment. But I'd been thinking about it ... for long time. (Ecstatic, Jennie spins and spins)

******************

(Light reveals Jennie, standing utterly still. Hurriedly Warren rushes across the stage, stops. Her back to him, in the grey light, she almost seems trapped inside the Sheffield walls.)

WARREN: What happened? Did you read it? (Jennie remains still unmoving.} Did you?

(Silence. Hesitant, Warren takes a step toward her.) Jennie?

JENNIE: (A muffled voice.) I read it. Yes.

WARREN: And? Did she like it? (Still silence.) Did she? (Jennie turns to him, her face bathed in tears.)

JENNIE: (Almost inaudible.) Nyet. Nyet! (Desperate.) I can't go back there. I can't face her.

WARREN: Of course you can face her. Who is she that you can't face her?

JENNIE: She's ... You know who she is. WARREN. But it's not as if she's God or anything. (Silence.) I mean she's not that great.

JENNIE: She is, Warren. You know she is. (A pause.) Without her ... without her I would never ... (In a rush.) never have understood anything! Keats, Dickinson! They know, they understand everything I've ever gone through. Like she does. Because, in her class, it's not just learning to read, to write - it's to feel, truly feel ...

WARREN: (Interrupting.) But you didn't write that in your poem, did you? About her, I mean. About your secret feelings. You didn't read that in front of the entire class? (pause.) Did you? (Jennie is still.) Well ... I mean even if you did, you've got to go back. You'll flunk school otherwise.

JENNIE: (Breaking in.) I don't care! Without her there is no school anyway.

WARREN: (To audience) I didn't know what to say. I'd never seen her like that. She was so worried, so upset. And I didn't ... I just didn't . .. I mean ... I don't know how to help her. (Light comes up on Jennie, standing in shadow in Miss Thorne's classroom. Miss Thorne comes in, switches on the light. Seeing Jennie, she stops.)

MISS THORNE: Here so early? Classes don't begin till eight. (Silence. Slowly, almost as if she were walking on eggshells, Jennie moves toward her.)

JENNIE: I ... I wanted to talk to you. (Still silence.) That is I - (Almost inaudible.) I . . .

(She stops.)

MISS THORNE: Yes? What is it?

JENNIE: I've been so worried. So afraid I did something wrong. Ruined something.

MISS THORNE: I don't know what you -

JENNIE: (In a rush, overlapping on "you:") Tell me. Please. What I've said. Done. Because ... you ... you're not -

MISS THORNE: (Interrupting) Nonsense. You've ruined nothing. Done nothing wrong.

(Jennie’s face lights up. She takes a step closer. Miss Thorne ,picks up a blue exam book.} [But] I feel it is my duty to warn you. Your last exam is, I'm afraid ... unacceptable. For that matter, all your recent work - Essays, fiction, even your poetry, Jennie! - (She looks away.) Yes ... even that ... has not been up to your usual standard. (Looking back at Jennie.) It's become, you've become ... undisciplined. (She stops. Jennie is still.) You've let the, shall we say ... passion ... overtake you. Creativity requires discipline, Jennie. Without that, it becomes self-indulgent. (Jennie looks down . A pause.)

JENNIE: (To audience . . . Wildly.) What's happening? I don't understand what's happening. I keep thinking - praying! - it's all some horrible nightmare and I'm going to wake up and the whole thing will have gone away. Because if I don't, I mean, if I don't wake up there really is no life for me anymore. (The light dims on her.)

WARREN: (To us.) And as the weeks went by, I saw her less and less - And when I did see her, the look on her face, in her eyes, scared me. (Jennie stares straight ahead - a haunted gaze -) Her face was frightened - as if she were drowning. (refers to his notebook) This was May. May sixteenth. One of the last days of school. A day that passed quickly, till there was only one thing left -- Friday afternoon assembly. The whole school rocked with laughter, as person after person came up and improvised ridiculous stories. {Warren undoes the clasp of the red handbag, reaches in, pulls out a piece of paper) Jennie Litvinov! (The sound reverberates through the audience. Then, stillness.) I kept praying. Please. Don't let her be here.

(And then, from the back of the theatre itself, Jennie appears, slowly makes her way through the audience to the stage, climbs the steps. Pale, thin, as if all life had been drained out of her, she turns to us, her face dead white.)

MISS THORNE: (A tense smile.) Ahh. For a moment I thought you weren't going to honor us with an appearance .. (Jennie seems to cringe beneath her words.) But here you are! So. (Miss Thorne opens the little blue book, closes her eyes, puts her finger down on the page. Opening her eyes, delighted.) "Crumpets!" (Silence.) Well? (Not a word comes from Jennie's mouth.) I'm waiting. We're all waiting. (Slowly Jennie opens her mouth.)

JENNIE: In India there is a custom ...

MISS THORNE: (Laughing.) India? What does India have to do with it?

JENNIE: (Going on.) An ancient custom when a servant has been hurt, mistreated by his master in some way, instead of getting angry or taking revenge, he sits outside the master's house, not eating anything -

MISS THORNE: (Breaking in. Airily, gaily.) Miss ... Litvinov! I cannot see what this ... story, this "custom," as you call it, has to do with ... You are not making us laugh, Miss Litvinov. This is not amusing.

(Not seeming to hear, Jennie steps closer to us, right up to the edge of the stage. And Miss Thorne stops speaking, mesmerized despite herself, as is the whole assembly, by Jennie's story, her strangely white face.)

JENNIE: He's waiting, you see, waiting for the master to say something - anything! - not an apology, just a word, one word ... one kind word. And he waits there, all curled up ... (Slowly sitting down on a step.) curled up outside his master's house until ... if necessary ... he starves himself to death. (A silence in the room.)

MISS THORNE: (Weary.) That story has nothing to do with anything. Why all this drama? Hasn't everyone at Sheffield been kind to you? Extremely kind, in fact. (Sofi.) Why do to me? Especially to me. (The whole assembly is absolutely still as Jennie remains motionless.) Frankly I'm at a loss to help [you]. I simply don't know how to help [you] anymore. **************

WARREN: I tried to find her. I went all the way out there. On the subway. Alone. (A pause.) Her parents don't live there anymore. Vanished. Like in a fairy tale. (Another pause.) Everyone says I have to forget about her. But I'll never forget. Never! (Almost a whisper.) I can't. She's ... (He stops.) my fairy tale. (A pause.) Jennie loved her. She loved Miss Thorne. I didn't think anybody ... Nobody loves Miss Thorne! But Jennie did.
```

---

## IC-0655: Now You’re Cookin’

- Title: Now You’re Cookin’
- Author (byline): Ira Brodsky and Barbara Lhota
- Work: Duo Practice & Competition - Forensics Series Volume 3
- Publisher: Smith and Kraus
- Publication date as stated: 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: AMY SUE, BONNIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1967
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ira Brodsky and Barbara Lhota
Book: Duo Practice & Competition - Forensics Series Volume 3
ISBN: 978-1575253084
Publisher: Smith and Kraus
Date (Month/Year): 2004
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Now You’re Cookin’ ACTRESS 2: by Ira Brodsky and Barbara Lhota
```

### Performance text (classify this)

```text
AMY SUE and BONNIE: (Singing, first one then the other, then both together.) "Keep on bakin' until it hurts. You're getting your just-You're getting your just-You're getting your (Big finish.) JUST DESSERTS!"

AMY SUE: I'm Amy Sue Lewis.

BONNIE: And I'm Bonnie Badinage. And you're watching the best little cooking show on Cleveland Public Access TV

AMY SUE and BONNIE: Just Desserts!

BONNIE: Amy Sue and I are co-founders of Cleveland's number-one pastry cafe-

AMY SUE: At least we think it's number one

AMY SUE and BONNIE: And it's called (Laughing.) Just Desserts!!

BONNIE: Located just down Route 6 at the Highland Shopping Center.

AMY SUE: Bonnie, we sure crack ourselves up, don't we?

BONNIE: We're funny as a meringue made with egg yolks.

AMY SUE: (Laughing and explaining to the audience.) As you guys know, a meringue is made with egg whites!

BONNIE: In fact, if you just get one tiny drop of yolk in it -- flat as (Makes a raspberry sound) -- Amy Sue. (Amy Sue tries to laugh, but she is hurt.) I'm just kiddin', Amy Sue. You've got nothing to be ashamed of. If you were one of the Spice girls-you remember there was Sporty Spice and Baby Spice?

AMY SUE: Sure, I remember.

BONNIE: Well, you'd be Spice Rack. Get it, Spice (Gesturing to her chest.) Rack?

AMY SUE: (Dryly.) Yeah, yeah. On past episodes of Just Desserts, we've shown you how to make puff pastry and souffles and

BONNIE: Napoleons and crepes suzette-

AMY SUE: And today, it's an American classic-cupcakes with three kinds of icing.

BONNIE: That may not sound very exciting.

AMY SUE: What? I love cupcakes! They taste like childhood on a platter.

BONNIE: I don't know about that. But I do know that cupcakes were first introduced in the 1800s when poor wagon women going across the prairies didn't have enough flour to bake large birthday cakes.

AMY SUE: Wow, I didn't know that!

BONNIE: That's what I'm here for.

AMY SUE: So let's get baking. I'm going to start with a good all-purpose batter.

BONNIE: Now don't forget salt.

AMY SUE: (Annoyed.) And a pinch of salt.

BONNIE: Most cakes have a pinch of salt to offset the sweetness.

AMY SUE: Yes. Now, we're going to add our wet ingredients. Two eggs and a stick of melted butter. (She cracks eggs against the side of the bowl.)

BONNIE: For easier mixing, crack the eggs into a separate dish and whisk them up before adding to the bowl like Amy Sue just did. Avoid eggshell mishaps.

AMY SUE: (Looks slightly put out.) Good tip, Bonnie B.

BONNIE: Notice that I've preheated the oven to 350 degrees, and I've prepared the cake tin with a dusting of flour.

AMY SUE: Oh, I was going to use those little paper cups. See look, they come in all kinds of pretty colors and patterns.

BONNIE: When we return, I'll talk about other, better options then those messy paper cups. So stick around, and come back for your Just Desserts. (Taping stops.)

AMY SUE: What's got into you? You're stepping on my lines, correcting my ideas-

BONNIE: We need to pick up the pace. Keep things lively.

AMY SUE: Oh, so we're back to that.

BONNIE: I just wish you'd prepare a little better.

AMY SUE: Is that true about the wagon train?

BONNIE: All right, that just sort of came to me. We can edit that out. But you know about beating the eggs before adding them.

AMY SUE: So I forgot. Big deal. It doesn't ruin the cake. But you make me look like a- (She reaches into her jacket pocket for her cell phone and flips it on.) Moron! Hello? Sissy? Hi, Sissy. What's up? (To Bonnie.) It's Sissy from the cafe.

BONNIE: Yeah, I got that when you said "Hi, Sissy."

AMY SUE: There you go again. (Back on phone.) What did you say? Bill didn't show up again? (To Bonnie.) Bill's sick.

BONNIE: Do we have any customers?

AMY SUE: (On phone.) Bonnie wants to know how's business? A-huh. Yeah. A-huh. Sure. (To Bonnie.) Dead.

BONNIE: Did she remember to take the "Closed" sign down this time?

AMY SUE: (In phone.) Did you hear that? (She looks at Bonnie.) Oops.

BONNIE: Oh my-

AMY SUE: Wait. Sissy says someone just walked in the door. (She covers receiver.) Everything'll be OK.

BONNIE: With one customer?!

AMY SUE: (To Bonnie.) Oops, false alarm. They were looking for the taxidermist.

BONNIE: We're sunk. Give me that phone.

AMY SUE: I can handle this.

BONNIE: Give me the phone!

AMY SUE: What? Sissy called me, Bonnie!

BONNIE: (Holding out hand.) Phone. (Amy Sue reluctantly hands it over. Into phone.) OK, Sissy. Now, what are you wearing today. A-hah, good. Is it tight? Good. Now what I want you to do is take a big tray of pastries, all different kinds, and cut them into little bite-size pieces.

Got that? Little pieces. You're going to set them out on a tray and walk out to the light by Route 6. I just got an idea. Are you wearing a bra? No, I'm sorry, I don't mean to be personal. But let me just say that sans bra is the way to go for this operation. (Pause.) No, not sand bra. It's French, it means "without." I'm just saying, we want to round up some business, and we can use all the help we can get. anyway, you're going to give out free samples to each and every car that stops at the light and be sure to point out where the cafe is. Say to them, now get this, "Come on over and get your Just Desserts." Then point to the bakery, and tell them our hours. Got it? Remember give them a little cheesecake with their coffee cake. I'll call you back later. Remember, customers equal tips, and happy customers equal really, really big tips. (Bonnie clicks off)

AMY SUE: That was disgusting and immoral.

BONNIE: It's business. It's practicality. It's saving our livelihood.

AMY SUE: No, I mean how you took the phone from me.

BONNIE: My God, chill Amy Sue. Desperate times demand desperate measures.

AMY SUE: But why is it that you're always the top dog?

BONNIE: Everybody has their place in life. I'm loud. I'm assertive. That's Bonnie!

AMY SUE: Then who am I?

BONNIE: You're the nice one. You're the sweet one. You're the pinch of sugar.

AMY SUE: I don't like that. It sounds so dull.

BONNIE: Well, you are dull. I meant that in a nice way. What I meant is that you're nice. You're pretty and sweet and you have a nice voice.

AMY SUE: And you sound like a fog horn!

BONNIE: Now that's not very nice.

AMY SUE: You're right. I'm sorry, but you got me upset.

BONNIE: Well, let's finish the taping. And we'll talk about this afterwards.

AMY SUE: OK, I guess.

BONNIE: Let's have a great show. (Smiling.) And give them a little cheesecake with their cupcakes. Ready? (Counting down for the taping.) Three, two, one.

AMY SUE: (Long pause while Amy Sue gives her brightest smile to the camera. She bats her eyelashes. She speaks in a new voice that is deep and sultry.) Welcome back. I'm Amy Sue Lewis and we are too, too hot to handle.

BONNIE: (Gives Amy Sue a horrified look.) I'm Bonnie Badinage, and let's get baking.

AMY SUE: (Is possessed by an aggressive sex-kitten attitude.) We're cooking big, round, fluffy cupcakes. Bonnie, will you fill those tins for little ol’ me, while I begin the frosting. (With emphasis.) It's a creamy cheesy frosting.

BONNIE: For God's sake, it's a cream cheese frosting. (She mimes filling the tins.)

AMY SUE: I have two large, very large, packages of Philadelphia cream cheese that I'm going to massage together with my bare hands.

BONNIE: We're not supposed to mention name brands, Amy Sue!

AMY SUE: Now I don't think those dear Philadelphians would mind a bit.

BONNIE: I've got the hand mixer here, and I'm going to add sugar and a touch of vanilla to the cream cheese. (Amy Sue provides the sound effects.) Now over here, I have a tray of cupcakes that we already baked and cooled.

AMY SUE: (Rubbing the tops of the cupcakes.) Bouncy, bouncy cupcakes.

BONNIE: (Slaps Amy Sue's hand away.) Stop it!

AMY SUE: (Playing it up, kissing her hand.) Ouchy! You're so rough, Bonnie baby!

BONNIE: (Getting down to business.) I have my offset spatula, a very handy tool, and I'm ready to ice. Take a nice big dollop of icing, and start working it around from the center in concentric circles. (There is something sensual in this activity, and Amy Sue sees it.)

AMY SUE: Swirly, swirly ... I bet those cupcakes are lovin' that action.

BONNIE: Amy Sue!

AMY SUE: Well, what's wrong? A little cheesecake with your cupcakes, remember?

BONNIE: We're professional bakers.

AMY SUE: And come on down to our cafe on Route 6 where Sissy the waitress will make you feel very, very good. She may even let you lick her beater.

BONNIE: Enough! Down girl! Zip it!

AMY SUE: Let's get to decorating, which is something I love.

BONNIE: Good. Notice that we have a whole range of colored sugars and draggees.

AMY SUE: (Giggling.) Draggees? What's that?

BONNIE: These little silver balls.

AMY SUE: Oh, I love the silver balls! Look how smooth and shiny.

BONNIE: So start decorating! Just shut up, please, and get to work. (To audience.) While Amy Sue and I are decorating up a storm, we're going to take a brief commercial.

AMY SUE: And you guys might want to rush on over to Just Desserts on Route 6 where you can sink your teeth into one of our yummy cupcakes, served by the equally yummy Sissy the waitress. Yum, yum. We'll be waitin' on ya. (She winks.) (Taping stops.)

BONNIE: "Yum, yum. Winky, winky"? What are you thinking, Amy Sue?!

AMY SUE: Nice, nice! I'll show you nice! I'm getting in touch with my inner tigress-roar!

BONNIE: You're going to get us in touch with the TV censors. We're going to lose our show as well as our bakery!

AMY SUE: Well, I don't care! I'm sick of nice.

BONNIE: You don't care?! Remember that loan we took for $25,000? Well, that's in both our names, tiger. And didn't you put up your house as collateral?

AMY SUE: (Sheepish.) Ugh.

BONNIE: "Ugh" is right, cupcake.

AMY SUE: I'm sorry, Bonnie.

BONNIE: What good is sorry now?

AMY SUE: I don't know. I guess not much.

BONNIE: No, it isn't.

AMY SUE: I'll fix things up.

BONNIE: I don't see how.

AMY SUE: By going back to being "nice"?

BONNIE: I don't know if you can. People out there are wondering, "Who is Amy Sue?" You've lost their trust.

AMY SUE: In five minutes?

BONNIE: You've lost my trust.

AMY SUE: I'm sorry, Bonnie. I'm a big doody head!

BONNIE: Let's just finish the show, and I'll clean up this mess afterwards-as usual.

AMY SUE: OK, Bonnie.

BONNIE: (Counting down to restart taping.) Three, two, one. Welcome back to Just Desserts. I'm still Bonnie Badinage.

AMY SUE: (Monotone and dead-eyed.) And I'm Amy Sue Lewis.

BONNIE: We're here finishing up our cupcakes and making them ready for presentation.

AMY SUE: (Robotic.) Yes. Nice presentation.

BONNIE: (Holding up a tray.) You can see we have a whole bunch of decorating ideas to really spruce up your cakes. They're a great way to show off your individuality.

AMY SUE: But you don't want too much individuality or you might scare people off. The orange pumpkin is very interesting. Nice for Halloween.

BONNIE: (Ignoring Amy Sue.) We have a flag motif with red- white-and-blue stars.

AMY SUE: Nice for July 4th. Again, not too extreme.

BONNIE: (To Amy Sue.) What's that sound?

AMY SUE: Huh?

BONNIE: What's that sound? Is that your cell phone?

AMY SUE: Oh, goodness, I forgot to turn it off. I'm sorry, Bonnie. (She takes out her phone and {lips it on.} Hi, this is Amy Sue. Oh hi, Sissy! (To Bonnie.) It's Sissy. (To the audience.) She's the waitress at Just Desserts. (Back to Sissy.) You're watching us on the TV at the bakery?

BONNIE: (Trying to cut things short.) That's great that everything is so busy at the cafe, but maybe you better talk to Sissy after the show.

AMY SUE: But it was dead a few minutes ago.

BONNIE: (To audience.) Oh, that Amy Sue! What a kidder! But a really nice kidder! Now let me show you how to make this multi-tier snowman cupcake for a winter treat.

AMY SUE: (To Sissy.) You've got a whole crowd at the cafe? (To Bonnie.) You were right. Things are hoppin'! (To Sissy.) So what's up? Yeah? A-huh. Ohhh! Really? Let me ask Bonnie. (To Bonnie.) Guess what? Everybody at the shop loved the last segment. They want to know what happened to me, and how to get it back.

BONNIE: What?!

AMY SUE: They thought I was really funny. (Back to Sissy.) And what? (To Bonnie.) And spicy.

BONNIE: Spicy? No, that's not right. I'm the salt and vinegar. You're the pinch of sugar.

AMY SUE: Not according to the folks at the bakery. (Trying out the sex kitten persona again.) Apparently double spice can be twice as nice.

BONNIE: Wait a second! Let me talk to Sissy.

AMY SUE: (Getting her "spicy" persona into gear. To Bonnie.) Now hold on, sugar. (Back to Sissy.) Not you, sugar. The other sugar. Well, you tell everyone at Just Desserts to eat on up, and we'll stop by after the show.

BONNIE: I want to talk to Sissy!

AMY SUE: (Snapping the phone off) Sorry, Bonnie. We have a show to finish up. And I don't want to waste time yapping on the phone when I can be cookin' with you and the folks at home. In fact, we're cooking with gasoline. In fact, we're two hot chili peppers.

BONNIE: In fact, judging by the way our producer is waving his arms, we're out of time.

AMY SUE: Rrrrr, Bonnie.

BONNIE: (Trying to get into the spirit.) Rrrr! Right back at you. (Holding up the tray.) Oh look, we have a little tiger stripe cupcake. Isn't that cute?

AMY SUE: Cute. Cute? It's fierce, I'd say.

BONNIE: Just like you, Amy Sue Lewis.

AMY SUE: And just like you too, Bonnie Badinage. So for both of us, I'd like to say, keep baking until you get your

AMY SUE and BONNIE: Just Desserts!
```

---

## IC-0656: The Odd Couple (Female Version)

- Title: The Odd Couple (Female Version)
- Author (byline): Neil Simon
- Work: Not specified
- Publisher: Random House, Inc.
- Publication date as stated: June 1971
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: FLORENCE, OLIVE
- Teaser before the introduction: Yes
- Spoken words (computed): 1274
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Simon
ISBN: 978-0573618284
Publisher: Random House, Inc.
Date (Month/Year): June 1971
```

### Introduction (context only: never use it for content warnings)

```text
FLORENCE: Meet my roommate, Olive the most UN-sensitive, UN-organized, UN-appreciative, UN-couth, woman (and I use that term loosely) on the planet. ARGHHH!

(freezes in the act of some “obsessive-compulsive” act)

OLIVE: Ms. Manners here is Florence, who will probably die of exhaustion, excessive neatness and then demand to organize her own funeral. She is going to drive me crazy! But she is rather fun to antagonize. Yup, of all the possible roommate combinations we are definitely

TOGETHER: The Odd Couple by Neil Simon
```

### Performance text (classify this)

```text
(Florence is vacuuming, and Olive comes in. Olive sees her vacuuming and unplugs it. Florence begins winding up the cord, then Olive steps on it. After two tugs at the cord, Olive lifts her foot before the third. Florence falls while Olive laughs. They glare at each other and then turn their heads at the same time. Olive then sits down and picks up a newspaper from underneath the chair. Florence takes the vacuum into the kitchen and returns with a plate of spaghetti. She sits down and begins eating. Olive smells the spaghetti and goes into the bathroom. She comes out with a can of deodorizer, and she then sprays the spaghetti and slams the can on the table. Olive freezes as Florence continues into the introduction.)

FLORENCE: All right, how much longer is this going to go on? Are you going to spend the rest of your life not talking to me?

OLIVE: You had your chance to talk last night. I begged you to come upstairs with me. I was looking for romance, and instead I got a petrified woman standing in my doorway. I don’t want to hear the sound of your voice, do you understand?

FLORENCE: Si, Yo comprendo. Gracias.

OLIVE: (gets a key out of back pocket and slams it on the table) There! There’s a key to the back door. Stick to your room and the hallway and you won’t get hurt. (turns to leave)

FLORENCE: Oh Olive! Need I remind you, I pay half the rent and I’ll go into any room I want!

OLIVE: Not in my apartment! Fine, but I don’t want to see you! Cover the mirrors when you walk through the house. . . and I am sick and tired of smelling your cooking. I have had it up to here with your polyunsaturated oils. Now, get that spaghetti off of my table.

FLORENCE: (laughing hysterically) That’s funny. . . that’s really funny. . .

OLIVE: (getting angry) what is so funny about that?

FLORENCE: It’s not spaghetti, it’s linguini.

OLIVE: (looks at her like an insane person. She then grabs the plate of linguini and throws it at the opposite wall)

FLORENCE: Are you crazy! Look at that mess! I’m not cleaning that up, it’s your mess. Look at it hanging all over the walls.

OLIVE: I like it.

FLORENCE: You’d just leave it there wouldn’t you, until it turns all brown and hard. . . yich! I’m cleaning it up.

OLIVE: (grabbing her and putting her hands on her head) If you touch one strand of that linguini. . . I will break every sinus in your head.

FLORENCE: Why? What did I do this time? What’s bothering you? Is it the cooking, the cleaning, the crying?

OLIVE: I’ll tell you exactly what’s bothering me. It’s the cooking, the cleaning, and the crying. It’s the moose calls that open your ears at two o’clock in the morning. I can’t take it anymore Florence, I’m cracking up. Everything you do irritates me, and when you’re not here the things I know you’re going to do when you come in irritate me. You leave me little notes on my pillow; we’re all out of cornflakes F.U. It took me three hours to figure out that F.U. was Florence Unger! It’s no one’s fault Florence; we’re just a rotten pair.

FLORENCE: I get the picture.

OLIVE: That’s just the frame. The picture I haven’t even painted yet. Every night in my diary, I write down the things you did that day that aggravate me. . . this is June, and so far I’ve filled it up till January. I haven’t even put in about the Gazpacho Brothers yet.

FLORENCE: Oh! Is that what’s bothering you. . . that I loused up your sex life?

OLIVE: What sex life, I can’t even have dirty dreams, you come in and clean them up!

FLORENCE: (pointing a finger at her) I warned you not to make that date in the first place.

OLIVE: (grabbing finger, attempting to bite it) Don’t point that finger at me unless you intend to use it.

FLORENCE: Alright Olive get off my back. . . OFF! Do you hear me!

OLIVE: What’s this? A display of temper? I haven’t seen you really angry since I dropped my eyelashes in your pancake batter.

FLORENCE: Okay Olive, there’s something I don’t want to say, but if I say it. . . I think you’d better hear it.

OLIVE: I’m trembling all over. . . look how I’m trembling all over.

FLORENCE: You’re a wonderful girl Olive. You’ve done everything for me. You took me in here, gave me a place to live and something to live for. If it weren’t for you, I don’t know what would have happened to me. You’re the tops with me Olive.

OLIVE: If I’ve just been told off. . . I think I may have missed it.

FLORENCE: It’s coming now.

OLIVE: Good.

FLORENCE: You’re also one of the biggest slobs in the world.

OLIVE: I see.

FLORENCE: Unreliable,

OLIVE: Is that so?

FLORENCE: Undependable,

OLIVE: Is that it?

FLORENCE: And indescribably inefficient. There I’m done, now you’ve been told off. How do you like that?

OLIVE: Good, because now I’m going to tell you off. For eight months, I lived in this apartment. I thought I was miserable, I thought I was lonely. I took you in here because I thought we could help each other, but after three weeks of close personal contact. . . I have hives, shingles, and the heartbreak of psoriasis. I am growing old at twice the speed of sound. I have seven new liver spots on the back of my hand that look like the Big Dipper. Do me a favor Florence, move into the kitchen, live with your pots, your pans, your ladle, and your meat thermometer. I’m going to lie down now, because my teeth are coming loose, and I’m afraid if I drop them in here, you’re going to get out your vacuum cleaner again. (turns to bedroom)

FLORENCE: (after a pause) Walk on the papers in there. . . I just cleaned the floors.

OLIVE: (looks at her with a crazy glare) In the kitchen! I want to get your head in the oven and cook it like a capon! (chasing her)

FLORENCE: (squeals; runs into the bathroom and locks it) You’re going to find yourself in one nasty lawsuit!

OLIVE: It’s no use running Florence, there are only six rooms and I know all of the shortcuts. (goes through the bedroom and through a different door to the bathroom. Florence runs out of the door Olive just came in)

FLORENCE: Is that how you settle your problems, like an animal? (reaches for her purse) This is tear gas. . . you lay one finger on me and you’ll be using eye drops for the rest of your life!

OLIVE: You want to see how I settle my problems? I’ll show you how I settle my problems! (goes into the bedroom)

FLORENCE: Alright! I warned you, I’m getting out my siren. (pulls a siren out of her purse. Then she lifts it in the air and pushes the button. Nothing happens. She holds it to her ear, again nothing) Olive? Have you been playing with my siren? (banging it on the table) Twenty-two fifty for a piece of Japanese-

OLIVE: (slamming a suitcase on the table) There! That is how I settle my problems!

FLORENCE: Where are you going?

OLIVE: Not me, you idiot! YOU! You’re the one who’s leaving! I can fix your siren so it will whistle for a cab!

FLORENCE: What are you talking about?

OLIVE: (going to the kitchen, she gets pots and pans) The marriage is over Florence. We’re getting an annulment. I don’t want to live with you anymore. I want you to pack your things, tie them up with your Saran Wrap, and get out!

FLORENCE: You mean actually move out?

OLIVE: Actually, physically, and immediately! (puts the pots in the suitcase, then takes the case to the door and sets it down) There! You’re all packed.

FLORENCE: You know, I have a good mind to really leave.

OLIVE: (looking heavenward) Why doesn’t she hear me? I know I’m talking; I recognize the sound of my voice.

FLORENCE: Okay, but let it be on your conscience.

OLIVE: Let what be on my conscience?

FLORENCE: Get out of my house is what you said. I just wanted to get the record straight. Whatever happens to me is your responsibility, and may it be on your head!

OLIVE: Let what be on my head? Don’t put things on my head! Take it off!

FLORENCE: I left you plenty of food, all you have to do is heat it up. You can ask one of the neighbors how to light a match.

OLIVE: You’re not leaving until you take it back!

FLORENCE: Take what back?

OLIVE: Let it be on your head. . . what is that, the curse of the cat people?

FLORENCE: I’d like to leave now.

OLIVE: Florence, we’ve been good friends for too long to end it this way. We’re civilized people, let’s just shake hands and part like gentlemen.

FLORENCE: (looks at the outstretched hand and spits in it)
```

---

## IC-0657: Oy Vey Maria

- Title: Oy Vey Maria
- Author (byline): Mark Harvey Levine
- Work: Best Ten Minute Plays of 2019
- Publisher: Smith and Kraus
- Publication date as stated: March 2019
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SUGGESTED ROLES, ACTRESS 1, ACTRESS 2, TOGETHER, KING 1, ANN, MARY, KING 2, JOACHIM, KING 3, LITTLE DRUMMER BOY
- Teaser before the introduction: Yes
- Spoken words (computed): 1353
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mark Harvey Levine
Book: Best Ten Minute Plays of 2019
ISBN: 978-1575259338
Publisher: Smith and Kraus
Date (Month/Year): March 2019
YIDDISH TERMS
* Oy gevalt is defined as oh, violence! —used to express shock or amazement.
* Drey is defined as to turn, twist, twirl, rotate
* Mishegas is defined as Insanity or craziness
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: That's what Christmas is all about. . . .

ACTRESS 2: And everything was going just fine in the manger until Mary's Jewish mother showed up.

TOGETHER: Oy Vey Maria by Mark Harvey Levine
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

SUGGESTED ROLES:

ACTRESS 1: Ann, Joachim

ACTRESS 2: Mary, King 1, King 2, King 3, Little Drummer Boy

ACTRESS 2: "And there were in the same country shepherds abiding in the fields, keeping watch over their flocks by night.

ACTRESS 1: And the angel said unto them, Fear not, for behold, I bring unto you good tidings of great joy, which shall be to all people. For unto you this day is born in the City of Bethlehem, a Savior, which is Christ the Lord.

ACTRESS 2: And this shall be a sign unto you; you shall find the babe wrapped in swaddling clothes and lying in a manger.

ACTRESS 1: And suddenly there was with the angel, a multitude of the heavenly host, praising God, and saying,

TOGETHER: 'Glory to God in the highest, and on Earth peace, good will toward men'". Retrieved from The Bible, King James Version, Book 42 Luke, Chapter 2, verses 8 to 14

(The classic manger scene. Mary, Joseph, baby Jesus, scattered animals. The Three Kings are there, gift boxes in hand.)

KING 1: We have come seeking the one who-

(Suddenly, Ann enters. She is Mary’s mother. She wears a babushka and carries a large tin foil pan of food with cellophane on it.)

ANN: Oy gevalt*! What is this? A manger? You gave birth to my grandson in a manger?

MARY: Mom! What are you doing here?

ANN: What, you couldn't find a trench to have the baby in? A manger, yet.

MARY: Mom-

ANN: What's wrong with a hospital? Who delivered the baby, a cow?

MARY: Mom-

ANN: So where is he? Where is this darling grandson of mine? (She sees the baby and screeches with joy.) Oh my God look at him he's so CUTE! I could eat him up! I will eat him up.

MARY: Mother.

ANN: I'm going to eat you up! Yes I am! Come here so I can eat you up! Um num num num.

MARY: Where's Dad?

ANN: He's still circling the block. They've got opposite side of the desert parking here. (She hands Joseph the pan.) Here. Make yourself useful. Go find an oven or something and heat this up. (Joseph leaves.)

MARY: What are you DOING here?

ANN: You think I wouldn't be here when my own baby gives birth? I'm your MOTHER. Of course I'm here. Where else would I be? You'll understand when you become a mother. Oh wait, you just did. Not that I was invited.

MARY: Mom ...

ANN: Was there not enough room in the manger? Move a few chickens over, I would have been fine.

MARY: Mom. This isn't a good time. We have company.

KING 2: Greetings! We have come to--

ANN: COMPANY? Your own mother you don't want here, but now you're entertaining?

MARY: Mom.

ANN: Me, you throw out. Them, you're putting out hors d'oeuvres? (Joachim enters.)

JOACHIM: You wouldn't believe the traffic out there. Must be the holidays. (hugs Mary) Hello, darling. How are you feeling?

MARY: I'm fine, Dad. It's good to see you.

ANN: Don't take your coat off, we have to leave!

JOACHIM: Leave? We just got here. I haven't even seen the baby yet.

ANN: He's the one in the trough. There, you've seen him.

JOACHIM: Oh there you are! Hello, cu tie! What did you name him?

MARY: Jesus.

JOACHIM: Hello, Jesus.

ANN: Jesus? I thought we agreed on Myron?

MARY: Ma, you agreed on Myron. We went with Jesus.

ANN: It doesn't even sound Jewish! Nobody's going to know he's a Jew. They'll have to remind each other when he leaves the room - "Did you know Jesus was Jewish?" "Oh, that's right."

MARY: We're not naming him Myron!

JOACHIM: Can I hold him?

ANN: No, they want him there. They left him out for the company. It makes a better picture. Personally, I'd move that sheep over a little.

MARY: Ma.

KING 3: Um .. .is this a good time to give the gifts?

ANN: It's fine! We'll leave. We don't want to be in the way. We just shlepped three hours by camel, that's all.

MARY: You don't have to-

JOACHIM: We were gonna stay nearby but there was no room at the inn.

ANN: Can you believe it?

JOACHIM: Not one room.

ANN: And we flashed our Triple-A card.

JOACHIM: Nothing.

MARY: Look, Mom, we're just a little busy right now ...

ANN: Oh, that's right, you have GUESTS. Well, if you don't want us here, you don't want us here. I understand. Promise me one day you'll describe me to the boy.

MARY: Mom, please.

ANN: Say that you turned me away, and I went home and died.

MARY: Mom, stay.

ANN: "They think it was her heart. It gave out from grief."

MARY: Stop it, Mother! Just stop! You're embarrassing me! You embarrass me all the time! You embarrass me in front of friends. You embarrass me in front of strangers. You embarrassed me in front of John the Baptist!

ANN: "John The Baptist"! I knew him when he was "John, The Kid Who Almost Drowned His Hamsters".

MARY: And now you're embarrassing me in front of my guests!

JOACHIM: Could YOU get a room at the Inn?

KING 2: We called ahead.

JOACHIM: There weren't any when we got there, that's for sure.

MARY: Dad.

JOACHIM: No rooms.

ANN: Not one.

JOACHIM: Not for love or money.

MARY: Dad! They're three Wise Men. They've come to-

JOACHIM: The Three Weismanns? I know them. They're in carpeting. They got a store in Galilee.

MARY: No, dad, they're Wise Men. Wise Men.

KING 3: We've come to adore the child.

ANN: Well, I've come to adore the child, and I brought a brisket! (To Mary) Pay attention, you have to know this now. This is what Jewish mothers do. We bring food. When someone is born, when someone dies, or gets sick, or gets married. We bring food. I brought a brisket. Mrs. Bergstein is sending over a tray. (looking around) Who sent the loaves and fishes?

MARY: I don't know, Mom, they just showed up.

JOACHIM: (looking at Jesus) It's a shame his birthday is right around Hanukkah, he's gonna get robbed on his presents.

ANN: So this is your company? Three wise guys?

MARY: They're also Kings. They're three Kings.

ANN: One Jewish mother beats three Kings! Believe you me, little missy. You should know, you're one too, now.

MARY: I'm not going to be like you.

ANN: Oh ho, so smart now.

KING 1: Um, we've brought gold, frankincense and myrrh.

MARY: No! I'm not! I'm not going to drey* him around all the time.

ANN: Yes you will. It happens to all of us. All Jewish mothers. It's in the blood.

MARY: No, no, that's your mishegus*, mom. I'm going to be different!

KING 2: We'll just put them over here. (They set down their gifts.)

MARY: I've sworn to myself that I'm not going to turn into you.

ANN: That's nice. That's a nice thing to say to your own mother. (The Kings begin slowly edging out.)

KING 3: (whispering) Thank you. We had a lovely time.

MARY: You drive me crazy, Mother! You drive me completely insane! You always have!

KING 1: We'll see ourselves out. (The Kings quickly exit.)

ANN: And you didn't? You were no bowl of olives growing up, either. I don't know how we got you through high school.

MARY: I'm not going to be laying guilt on him all the time!

ANN: Guilt is good! Believe me, this world could use a little more guilt. You read the daily scrolls, what do you see? Robbery, murder, gladiator games! If people felt a little more guilty about these things, maybe they wouldn't DO them. If everyone had a Jewish mother-

MARY: And I'm not going to nag at him all the time. I hear your voice in my head even when you're not around!

ANN: Did you hear it when you got the idea "Hey, let's have the baby in a stable"?

MARY: There was no room at the Inn, Mother!

JOACHIM: We couldn't get a room either. And we tried!

ANN: Wait a second, wait a second- do you hear what I hear?

MARY: What? The Little Drummer Boy enters, energetically playing his drum. Ann grabs the sticks from his hands and smacks him over the head.

LITTLE DRUMMER BOY: Ow.

ANN: Are you out of your MIND? There's a baby here!

LITTLE DRUMMER BOY: Come, they told me--

ANN: I don't care who sent you! Tell them to send a basket of fruit next time! Get out of here! (The Little Drummer Boy runs off) What's next, a mariachi band? Vey is meer*.

MARY: I just wanted to have a nice night. A silent night. A holy night.

ANN: When I gave birth to you, we didn't have percussionists dropping in. Everything was nice, quiet, clean. Immaculate, really.

MARY: I don't know why these things are happening! I don't know why Kings and Shepherds and small boys with snare drums are showing up! I just know that I have a little baby. And we're going to love him! We're going to love him like crazy! We're going to worship him, in fact! We're going to treat him like he's God!!! (Pause.)

ANN: N OW you're a Jewish Mother! Was that so hard? Welcome to the club!
```

---

## IC-0658: The Parent Trap

- Title: The Parent Trap
- Author (byline): Erich Kastner (adapted by Vic Crume)
- Work: Not specified
- Publisher: Scholastic, Inc.
- Publication date as stated: 1968
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SUSAN, SHARON
- Teaser before the introduction: Yes
- Spoken words (computed): 1440
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric Kasten adated by Vic Crume
ISBN: 0590029614
Publisher: Scholastic, Inc.
Date: 1968
```

### Introduction (context only: never use it for content warnings)

```text
Two girls meet at camp, soon to find out that they are related. Not only related but twins! The put together a hilarious scheme to stay together in The Parent Trap by Eric Kastner.
```

### Performance text (classify this)

```text
SUSAN: What are you staring at?

SHARON: Excuse me. It’s just that the girls were saying we looked alike.

SUSAN: Yeah? Turn your head. Let me see that profile! I know it! The spit and image of you-know-who!

SHARON: Who?

SUSAN: Frankenstein!

SHARON: You know what I mean! You’ve noticed it too!

SUSAN: I saw you staring at me yesterday when we were at the milk counter. And it isn’t just having blue eyes and honey-blonde hair, either. It’s when we have swim caps on that it really shows. Exactly the same features. Why, I think we’re practically identical!

SHARON: I hope not! You chew your fingernails. And you’re so loud! I can hear you all over the place!

SUSAN: I, for one, regard this as the beginning of the Famous Camp Inch Mystery.

SUSAN: This is my dad. Dreamy. Yes?

SHARON: He’s very handsome.

SUSAN: Ever been to California? Well, it’s a sensational place. At least, our ranch is. It’s out in Carmel near the ocean. I’ve got a horse and everything. And we have a pool. You know, you can practically fall out the front door and go swimming any time you like.

SHARON: Susan, Why have you been coming to Camp Inch for four years? I mean- well, with a horse and a ranch and everything, well, what I mean is- going up in the mountains with your dad- well, I just wouldn’t want to come all the way from California to Maine just for Camp Inch, Bit if you had a father like yours! I’m sorry, Susan. It isn’t any of my business. It’s just that- well, if I had a father like that, wild horses couldn’t drag me away!

SUSAN: Why? Is your father the busy type?

SHARON: I don’t have a father. That is- actually, Mother and Daddy separated years ago. I never saw him. Not to remember him, anyhow.

SUSAN: Well, as a matter of fact, I don’t have a mother. I guess that’s why Daddy sends me to Camp Inch. You know, it’s scary the way nobody stays together anymore these days. Pretty soon it’s going to be more divorces than marriages.

SHARON: Isn’t that the truth.

SUSAN: How old are you?

SHARON: Thirteen.

SUSAN: So am I. When will you be fourteen?

SHARON: November twelfth.

SUSAN: You will! That’s my birthday too.

SHARON: That’s funny!

SUSAN: Yeah!

SHARON: Stopped raining. Want to go down and get a Popsicle, or something?

SUSAN: Sharon, you said you were from Boston. That’s not so far from Maine. How come this is your first year at camp?

SHARON: It’s a wonder I even got here this year. Mother thinks I should do one thing, Grandmother thinks something else. And Grandfather- well, he just waits to see what happens next!

SUSAN: What’s your mother like?

SHARON: Oh, Mother’s great! She’s awfully pretty. I guess I might take after my dad. Was your mother pretty.

SUSAN: Fabulous. Absolutely fabulous. Daddy used to have her picture on this desk, and then.

SHARON: And then what?

SUSAN: Well, he caught me looking at it and it’s never been around since. What to go with me to the commissary for that Popsicle? Well, how about it? What are you staring at?

SHARON: Look! Goosebumps!

SUSAN: What do you mean?

SHARON: Don’t you feel it? Don’t you know what’s happening? Don’t you think it’s peculiar that we both look so much alike and – and have the same, identical birthdays?

SUSAN: Oh, that! Well, it’s just one of those things, I guess.

SHARON: Not when I have Goosebumps! Mother always says I’m psychic. You know- that I can sense things when something strange is going to happen!

SUSAN: Oh, Sharon! Come on!

SHARON: Look. Look at this!

SUSAN: I-I don’t understand. What are you doing with her picture?

SHARON: It’s my mother.

SUSAN: But it’s my mother. It’s the same picture Daddy had on his desk!

SHARON: That’s what I mean, Susan. Don’t you see?

SUSAN: Why don’t’ you go have lunch? It’s too late for Popsicles, anyhow.

SHARON: How can you think of food at a time like this!

SUSAN: Oh go. For goodness’ sake, Sharon, please go! Sharon- you know, I’ve been wondering. How do you suppose it happened? I mean- Daddy and me living in California, and you and Mother in Boston?

SHARON: My goodness, Susan- I don’t know. In fact, I can’t even imagine!

SUSAN: Well, I can! Gosh, I can imagine it right now! There we were- only a year old. Probably we could hardly sit up alone! Maybe they had a big quarrel. And maybe Mother said, I want this one- you can have the other. And dad said ‘O.K., but just don’t call that one Evers!

SHARON: I’ll never believe that- not in a million years!

SUSAN: Then, what’s your idea?

SHARON: Well, I see it this way. I imagine they had a dreadful quarrel- and they just couldn’t make up afterward. Probably Mother packed us both up to leave the ranch, and then- then she just couldn’t be mean enough to leave Dad without his half. So, she just hated it, but she had to let him pick you. How do you suppose I feel being the one who didn’t get picked?

SUSAN: Oh, Sharon! You nut! We’re both nuts. We don’t know a thing about it.

SHARON: We know one thing. Neither one of them ever married anybody else.

SUSAN: Well, what does that mean?

SHARON: Secretly- in their innermost hearts- they must be still in love.

SUSAN: I don’t get it. I think your poetry book is going to your head. Why would they stay apart all these years if they were in love?

SHARON: All true lovers have a simply dreadful time. History is jammed with them. Look at Rome and Juliet!

SUSAN: Where?

SHARON: Now who’s the nut? They were famous lovers, silly. And they had a terrible time.

SUSAN: Sharon! I’ve got it!

SHARON: What? Got what?

SUSAN: Oh, my gosh! What if- Oh! It’s just so scary. But we might be able to pull it off!

SHARON: Stop jumping. What’s so scary? What could we pull off!

SUSAN: You want to know Father. I’m just dying to know Mother. Well, we could- could switch places.

SHARON: Switch places?

SUSAN: Sure! We’re twins, aren’t we? Oh! I’m getting Goosebumps now!

SHARON: Oh, we could. And there’s more to it then just switching places, Susan!

SUSAN: What?

SHARON: If we switched, sooner or later, they’d have to unswitch us. Don’t you see? They’d have to meet again! Oh, Susan. I believe fate brought us together!

SUSAN: And we’d bring them together. Just having to unmix us, they’d have to meet!

SHARON: We’ll have to plan. Step one and step two- like that!

SUSAN: When do we start?

SHARON: Well, not until after lunch anyhow. Come on. Let’s make the dining hall in time for seconds.

SUSAN: And all the time I thought you were the poetic one! How can you think of food at a time like this? NEW SCENE

SUSAN: Well, you don’t sound like her. Remember, Sharon, try not to sound too Boston. Daddy and Hecky will just about fall over if you come out with those ‘shawn’ts’ and ‘cawn’ts.’ Besides, if I could give up biting my fingernails to fool Mother, you ought to be able to talk Western for Dad.

SHARON: Gosh! Do you realize that by this time tomorrow you’ll be in Boston?

SUSAN: And you’ll be zooming over the whole U.S.! Now let’s go over this once more. What’s my horse’s name?

SHARON: Schatzie.

SUSAN: Dog?

SHARON: Andromeda.

SUSAN: Right. And remember to thank Verbena for fixing chili beans. She’s sure to have them first thing, because they’re my absolute favorite food.

SHARON: I will. And I’ll bite my nails- but not until just before the plane lands. Poor nails!

SUSAN: And chew gum- often.

SHARON: And you chew gun seldom- if ever. Now, let’s do your part. Where is your bedroom at Mother’s?

SUSAN: Second floor. Second door left. The library and the music room are on the first floor. Which way is the music room?

SHARON: Right, as you come in the front door. You know, that’s the only thing that has me worried. Gran’s apt to ask you to play the piano- and she isn’t going to expect ‘Chopsticks,’ either.

SUSAN: Oh, I can put Band-Aids on a couple of fingers. That’s nothing to worry about. What I’m worrying about is your riding Schatzie.

SHARON: Why? Is he very spirited?

SUSAN: I’m thinking more about the way you ride. Hecky will wonder if something’s wrong with you if you begin hopping up and down in the saddle. He never heard of Eastern style posting. Just sit.

SHARON: Susan, what if we’re both flops?

SUSAN: Oh, for goodness’ sake! Then we’ll just get unmixed that much sooner. Don’t worry. Remember, the big thing is to get Mother and Dad together.

SHARON: We’d better say good-bye right here. We don’t want Staimes to think he’s seeing double. Good-bye, twin! And no shawn’t, cawn’t, awn’t. I promise.
```

---

## IC-0659: Parental Consent

- Title: Parental Consent
- Author (byline): S.D. Graubert
- Work: 2010 The Best 10-Minute Plays
- Publisher: Smith and Kraus
- Publication date as stated: Sept 2010
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, ACTRESS 2, ACRESS 2, ACTRESS 1, TOGETHER, EDNA, DANIELLA
- Teaser before the introduction: Yes
- Spoken words (computed): 1706
- Already set (do not supply): none

### Source block (context only)

```text
Author: S.D. Graubert
Book: 2010 The Best 10-Minute Plays
ISBN: 978-1575257723
Publisher: Smith and Kraus
Date (Month/Year): Sept 2010
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Your child tells you they have decided to join the military to serve our country.

ACTRESS 2: Immediately, your heart falls deep into the pit of your stomach, and you begin to think you are losing your hearing.

ACTRESS 1: This rush of emotion is something you have never experienced before –
```

### Performance text (classify this)

```text
CHARACTERS: EDNA, forty, proud, confident, highly strung. DANIELLA, seventeen, Edna's daughter, eager, patriotic.

NOTE: A slash "/" indicates where dialogue should overlap.

ACTRESS 2: Fear . . .

ACRESS 2: Faith . . .

ACTRESS 1: Pride . . .

ACTRESS 2: Shock . . .

ACTRESS 1: But at only 17, your child must have parental consent.

ACTRESS 2: What do you say?

TOGETHER: Parental Consent by S.D. Graubert

Daniella helps Edna unpack groceries.

EDNA: So, I finally had to tell Mrs. Brody, I had to say it, and you know I don't like talking politics with the patients, but she kept on and on, 'til finally I said, and I didn't say it badly, but I had to say, I had to say it, I am proud of my country - no, that goes in a baggy - I am proud of how the Republicans are protecting my country, I wasn't angry, I mean I didn't say it angry, I was angry inside, she's clearly ignorant, does she want this country to be ruled by terrorists?

DANIELLA: They attacked us. So, we should -

EDNA: Exactly. They attacked us. She thinks it's all a conspiracy. About a, a, what'd she say? Pipeline. She thinks everything's a conspiracy. Oh, and the September attack was about oil. Oil? And I say to her, I say, there was no oil in the World Trade Towers. There was no oil in the Pentagon.

DANIELLA: They want to destroy America

EDNA: They want to destroy America. Don't put the tomatoes in the fridge, they lose their flavor. I mean I told her, and I said it nicely, I didn't say it badly, in her day women didn't get to be doctors, not without it being an issue, she knows this, but we fight, we inch forward and you, you get to be a doctor I you get to be the

DANIELLA: Yeah, hey, and you also -

EDNA: one calling the shots, you can't do that in those countries, in Saudi Arabia, with the head scarves - because this is America. This is America.

DANIELLA: What'd she say to that?

EDNA: Well, she said ... (Dismissive exhalation.) Phoo ... but I said that's not racist, women don't have rights in Saudi Arabia, it's a fact, that's not racist, they don't have birth or death certificates, is it racist to comment, to observe that women don't have rights over there, no birth or death certificates? That's, that's like cattle. That's not racist.

DANIELLA: Women have rights in America.

EDNA: Everyone has rights in America. Our kids can be whatever, president, doctor - I'm so proud of you, Danny. Yeah. Her nephew signed up, Mrs. Brody, there's been a, a what do you call it, recruitment drive, at the mall, that's why she being so ... she wishes he hadn't. We upped her meds.

DANIELLA: For the marines?

EDNA: I guess. I said where do you think our soldiers come from? Look! It's an odor-buster! Then she says the whole WMD thing is an excuse, and I say, do you honestly, honestly think the president would lie about a thing like that? I said it's a good thing your nephew signed up, / you should be proud. / Our rights have to be protected. Because there's a whole

DANIELLA: Yeah. (Second interruption.) Yeah, proud!

EDNA: big part of the world that would like to take that away.

DANIELLA: That is so right.

EDNA: I don't want to be forced to wear a head scarf Do you?

DANIELLA: No way.

EDNA: She says it's not about head scarves, I say what's it about then? These potatoes, they had a demo in the store, they're purple inside. (Cutting potata.) You know how hard my job would be if I had to wear a head scarf? Look! That's pretty, right?

DANIELLA: Hey, Ma, can you sign this?

EDNA: Sure, ach, fingers. I thought we'd done all the paperwork.

DANIELLA: It's kinda like permission.

EDNA: You don't need my permission. You can do whatever you want.

DANIELLA: I'm not eighteen yet.

EDNA: Ten months.

DANIELLA: So, once you sign I'm good to go.

EDNA: Is this, like, for a society or something? Is that how it works now?

DANIELLA: I signed up.

EDNA: For extra credit? That's my girl.

DANIELLA: For the marines. (Beat.)

EDNA: How hard is it to pack a bag?

DANIELLA: I told him you'd be so into me going.

EDNA: Lighter groceries on top. It's not rocket science.

DANIELLA: Hey, not like Mrs. Brody!

EDNA: She crushed the cheese. Look at that.

DANIELLA: I'm gonna show them who's boss. Isn't it great, Ma?

EDNA: Yes. What is?

DANIELLA: That I'm able to sign up. Same as Mrs. Brody's nephew.

EDNA: (As if she is better.) You are nothing like Mrs. Brody's nephew.

DANIELLA: Like, we're both marines.

EDNA: You're going to be doctor.

DANIELLA: See, it's cool. I get to be a doctor, and I get to be a marine. Right?

EDNA: But being a doctor is so much more impor -

DANIELLA: It's not an 'issue.' Like you said.

EDNA: People who join the marines have a propensity, they –

DANIELLA: He said I'm perfect marine material.

EDNA: And I'm sure they work very hard, but a doctor -

DANIELLA: They're an elite force. They're the vanguard of operations.

EDNA: Going to college is much -

DANIELLA: Yeah, and, like, the Taliban would stop me going to college. That's why we need to fight them.

EDNA: And there are people who do that. People who are trained.

DANIELLA: Oh, we get a full training.Twelve weeks / in Parris Island. Plus I get a $4000 sign up bonus. Then I get assigned. Afghanistan. Kosovo.

EDNA: Twelve weeks? (After Kosouo.) Kosovo? Is that even a country?

DANIELLA: It's, like, in Europe. Boring. Hey, can you sign? I need to get it back to him today.

EDNA: Today? But, but, doesn't this mean, aren't you, wouldn't this mean, you're going to be older, it'll put you at a disadvantage, if you, if your friends, aren't you going to be, if you -

DANIELLA: It'll make me a better doctor. That's what he said.

EDNA: (Trying to stay calm.) OK. It's a big decision. Why don't we think about this? For a couple of days. That's all. Just a couple of days.

DANIELLA: He says it's urgent.

EDNA: Nothing good is done in haste.

DANIELLA: But we got attacked.

EDNA: New York! Washington! Nobody attacked Pittsburgh!

DANIELLA: Close enough.

EDNA: Yes, well, they didn't mean to land in Shanksville.

DANIELLA: If Al-Qaeda hadn't attacked America, it wouldn't have landed there at all. Look, they started it.

EDNA: I am aware of that, Daniella.

DANIELLA: I so want to get Osama Bin Laden.

EDNA: We all do, honey.

DANIELLA: Can you imagine? Yeah, I'm a woman and I'm kicking your Taliban butt!

EDNA: You're too young.

DANIELLA: No, see, you just have to sign the release. It's easy.

EDNA: There must be more to it than that.

DANIELLA: I read the leaflets. And spoke to the guy. For ages.

EDNA: But, see, don't you want to be with your friends? At college?

DANIELLA: They stop women being doctors out there, midwives, everything. You couldn't even be a nurse out there.

EDNA: No-one's going to stop you being a -

DANIELLA: The Taliban would. If they invaded. It was on the news! You know, Ma, you don't seem to be supporting my choice.

EDNA: I have always supported your choices.

DANIELLA: Then will you sign the form?

EDNA: Look. At least start college, just start it, do it for me, then in a couple of years-

DANIELLA: We might not have two years!

EDNA: But the money. It's set up. Do you know how hard I worked to secure that?

DANIELLA: Yeah, I went through it all that with the recruiting officer.

EDNA: At the mall?

DANIELLA: Legally, they have to hold everything in place. 'Ti! I get back.

EDNA: What if you get injured? Have you even thought about that? (She takes ice cream out of the bag.)

DANIELLA: I'll be fine.

EDNA: The ice cream! I can't discuss this now, I have to defrost the fridge.

DANIELLA: I'll be fine, Ma.

EDNA: It has to be done now, or the ice cream will be ruined. (Edna, very aggressively, empties out and sorts the remaining groceries.) You could get raped. Sweet Jesus. They rape women out there.

DANIELLA: They rape women here.

EDNA: It's not the same! If you get caught by a, by a, a Taliban person, they'll-

DANIELLA: I won't get caught, Ma.

EDNA: It's war! You have no idea.

DANIELLA: I know about war, Ma, I am nearly eighteen.

EDNA: But what if you get. Danny, have you really thought? Or, or blinded, or you, or you, (Her voice cracks.) say, you don't come back? What's the point of holding a place, if you don't come back, Danny?

DANIELLA: God, why are you being so negative? Of course I'm gonna come back.

EDNA: You don't know!

DANIELLA: I thought I could count on you.

EDNA: Please, Danny, trust me, I know what's best for you.

DANIELLA: Doesn't look like it.

EDNA: Daniella. There are other people –

DANIELLA: Who do you think they are, Ma?

EDNA: It doesn't have to be -

DANIELLA: Mrs. Brody's nephew?

EDNA: What if she's right? I mean, it's, it's –

DANIELLA: So, now you think the president is lying?

EDNA: Of course not, I'm, I'm. I'm not saying it's. But what if?

DANIELLA: That my commander-in-chief is lying?

EDNA: Not your commander. He's not your commander.

DANIELLA: Only 'cause you won't sign the form.

EDNA: If, if, yes, what'd she say, the neo-con, the big event, like Pearl Harbor, that's what she said, then you'd have to wait, right? 'Ti! you knew for sure. About the pipeline. / Yes, she said that, I think, a pipeline. In Afghanistan.

DANIELLA: I can't believe you're - (After "Afghanistan.") I can't believe this. You said we had to fight, that we needed to protect -

EDNA: I know, I know, I know that. And I agree. But what if. Best to wait, couple of years, that's all. 'Ti! we know for sure.

DANIELLA: Our rights have to be protected, that's what you said. That's what you always say. You always say that!

EDNA: And Iraq. Well. That's a huge country.

DANIELLA: Ma! God. I can't believe - Anyway, we're not going into Iraq. That's what the guy said. He has it on official authority. I'm not supposed to tell you. Top secret.

EDNA: We're not going to get Saddam?

DANIELLA: Nope. And, hey, even if we did, he said it wouldn't take long. Didn't last time.

EDNA: Your allergies. Your hives. You'll be in Afghanistan with hives.

DANIELLA: He didn't say it would be a problem.

EDNA: (Venom.) Of course he didn't. He wouldn't.

DANIELLA: We've got to fight. / Inching forward. That's what you say.

EDNA: Absolutely. The army should. That's why we pay our taxes.

DANIELLA: Sign the form, Ma.

EDNA: There's a lot of small print.

DANIELLA: It's not a warranty.

EDNA: You know I always read the small / print –

DANIELLA: I want to get it back to him today.

EDNA: Can't find my glasses.

DANIELLA: On your head.

EDNA: Pen doesn't work. (Danny grabs a jar of pens.)

DANIELLA: Here.

EDNA: l. I can't. I know it's. I'm sorry. I can't.

DANIELLA: I think you owe Mrs. Brody an apology.

EDNA: She's on strong medication.

DANIELLA: Then I give her more credit. (Daniella storms out. Edna Looks at the document, lost.)
```

---

## IC-0660: Perfect

- Title: Perfect
- Author (byline): Mary Gallagher
- Work: Found in 25 Ten-Minute Plays from Actor's Theatre of Louisville
- Publisher: Samuel French, Inc.
- Publication date as stated: June 1989
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TINA, KITTY
- Teaser before the introduction: No
- Spoken words (computed): 1352
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mary Gallagher
Book: Found in 25 Ten-Minute Plays from Actor's Theatre of Louisville
ISBN: 0573625581
Publisher: Samuel French, Inc.
Date (Month/Year): June 1989
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Women’s liberation, politics, social issues . . . .

ACTRESS 2: Dating is much more difficult today than it was before women became so liberated.

ACTRESS 1: Today we’re looking for more than a provider: We want intelligence, social awareness, sensitivity, strength . . . . Let’s face it . . We want it all.

ACTRESS 2: Don’t forget sexy . . he has to be sexy.

ACTRESS 1: In “Perfect” by Mary Gallagher, Tina and her husband “Binky” have invited Kitty and her potential boyfriend over for dinner.

SIMULTANEOUSLY: Dan is . . . . . PERFECT by Mary Gallagher He is certainly not . . . . PERFECT by Mary Gallagher
```

### Performance text (classify this)

```text
TINA: So wadaya think?

KITTY: So far, he's fine

TINA: I think he is perfect!

KITTY: He's great-looking, that's for sure

TINA: My God, Kitty, I'm drooling! And smart, he's like Joe Genius at the law firm, Binky says

KITTY: He seems like he's bright, he's read a book lately, at least

TINA: He reads like a maniac. Like at the office, Binky says everybody's talking about who would want to try out for "Survivor: The Galapagos," and Dan is like, "You know I was reading this book last night," and everyone goes, "Oh." But I mean, you love that.

KITTY: But he's funny too. I mean I think he's said a lot of funny things tonight

TINA: Are you kidding? God, he is hysterical! He gets Binks laughing on the phone, like Binks can't stop, like with tears

KITTY: And he offered to help clear the table.

TINA: That, I could not believe.

KITTY: Of course, he is a guest

TINA: But still. They won't, you know?

KITTY: It's like the last bastion, the Alamo

TINA: Or even if they did it for some brief exciting era, now it's over. You get up, you pick up a plate, and they dig in, they get this look, this rigid look..

KITTY: Sort of daunted, but entrenched...

TINA: And they start talking sports.

KITTY: Or corporate talk. "To the best of my knowledge, Fred."

TINA: Right! Right! That's the best thing about Binky being Binky. When people start that crap with him, it just doesn't cut it. "To the best of my knowledge, Binky..." [They start giggling. They lean on each other, How about that Dan guy you’ve been dating? [About the vibes.] WOO!

KITTY: Yeah. It's great. So far.

TINA: What is this "so far"? There is no hidden horror. Trust me. I told you, I looked into him. Not only is he not attached, he has the perfect history. He was married once, so he's not afraid of commitment. But they were really young and it just didn't work out. But they're still friends, he even plays squash with her new husband, so clearly he's not bitter. But, they've been divorced for years, and he's dated a lot and lived with two other women, so he's not hung up on her. No kids, so there is no issue of "maybe his kids will hate you." But he has one nephew and two nieces and he adores them, so he's not opposed to kids. Plus he doesn't smoke. I mean, if you don't take him, take Binky and I'll takehim!

KITTY: I really am attracted to him

TINA: Tell me about it! It's like...a force!

KITTY: Yeah?

TINA: Yeah! Also you keep grinning.

KITTY: I do? Oh God

TINA: You both do. Me and Binky feel left out.

KITTY: God, how embarrassing

TINA: So what's the hold-up?

KITTY: [Beat, then.] You're gonna get pissed off.

TINA: I might, I'll tell ya. I oughta get annointed Queen for coming up with him. Or Pope. 'Cause do you know what's out there?

KITTY: I know, I know, believe me.. .Okay. Look at the evidence. He's a corporate lawyer. He makes a lot of money.

TINA: It's not that great, he makes like what Binky makes

KITTY: Compared to say the average income of the average working

TINA: Okay, okay, right

KITTY: He drives a BMW He went to Fiji on vacation. He makes jokes about his investment portfolio, but he has a portfolio and he's only, what? Thirty-six?

TINA: Thirty-eight. That's better, men are creeps till they're thirty eight. See, he's even thirty-eight! What are you afraid of?

KITTY: Who do you think he voted for?

TINA: [Stopped; then stalls for time.] Huh?

KITTY: I knew it!

TINA: No no, wait, hold on

KITTY: God, it's all so depressing

TINA: No, wait a minute, we don't know

KITTY: You know, you know in your heart

TINA: I don't! You never know. Binky's just the same as Dan, he's practically a clone of Dan, and Binky didn't vote for him

KITTY: That's because you told him if he voted for him, he would not get any for four more years.

TINA: But he wouldn't've done it anyway, Binky never really votes for them. Sometimes, yeah, he talks the talk, just to get me all wound up, but "once inside the booth," you know

KITTY: This is denial, Tina.

TINA: No! Even when Reagan died, the Great Communicator and the state funeral and all, and everyone kept saying, "Ronald Reagan made us feel good about ourselves again," and then they'd play these sound bites from his speeches? And Binky said, "Tina, listen to his voice, he sounds like a child molester." [Doing creepy Reagan.] "Come with me, little girl, it's morning in America..."

KITTY: Yeah, yeah...we can all sneer and laugh at them, but do you think they care? They sell yo-yos in the gift shop of the Ronald Reagan Presidential Library, yo-yos with Ronald Reagan's name on them, that's how much they care.

TINA: All I'm saying is, Binky doesn't vote for them

KITTY: It's how Dan votes that worries me!

KITTY: [Bleakly.] Because if he votes for them, I'll cry, or puke, or something.. .

TINA: [Beat; then, gentry.] Look. Why don't you wait. You know? Enjoy it for a while. You guys could have so much fun. And he could be the greatest guy in America. Don't ruin it before you even

KITTY: No, I can't face falling for him, getting suckered in, but all the time suspecting, probing, and then finding out! No. I'd rather end it now. One clean... [Chopping motion.] I'll go back in, I'll ask him. [KITTY turns to exit. TINA grabs her.]

TINA: Now, dammit, Kitty! This is really self-destructive. I don't think you want to have a good relationship. Or even a good time! I . think...I think, and I am serious, you are avoiding real live men

KITTY: No! There are certain things-principles, gut instincts, call them what you will-that every person has to cling to. That's what makes us who we are. I would not ask you to give up the deepest convictions that you have

TINA: [Annoyed.] Name one!

KITTY: -and you would not want me to throw away my most dearly-held beliefs

TINA: I want you to have a nice man in your life! I want you to be happy!

KITTY: ...Yeah, I know. And I want that too, I do! But I can't stand the way this country's going. And if I can't stop it, at least I won't participate. I won't have a relationship with anyone who votes for them.

TINA: [Beat, then, flatly.] You're talking about every man who makes a decent living

KITTY: No!

TINA: Well, the vast majority

KITTY: No! No! In 2000, Bush didn't even win! He sneaked in the back door because his brother's flunkies blinded senior citizens and wouldn't let black people vote!

TINA: Oh God, here we go...

KITTY: And how about all those people who stopped voting years ago, because they were too weak and wasted, drained, from all those years of rage to drag their bodies to the polls! Worn out by years of Reagan and Old Bad Bush and Ollie North and Newt Gingrich and Trent Lott and Antonin Scalia, God! And it just gets more horrendous, now it's George the Worst! And Cheney, Rumsfeld, Rove, Rice

TINA: Whoa, whoa, didn't you just skip eight years? Clinton was one of ours.

KITTY: Clinton broke our hearts, but having “sex” at the office is not the same as throwing out social security so that we can spend our golden years living in cardboard cartons! Clinton didn't try to give away the arctic wilderness! He didn’t call an education bill "No Child Left Behind" and then leave behind the funding! He didn't bring back Star Wars and gag orders for birth control and trillion dollar deficits! He didn't lock up immigrants for years just "on suspicion," without lawyers or human rights! He didn't attack a country just so he could carve it up and hand the pieces to his friends and act like no one's dying! And Clinton could speak in sentences, with clauses. He could sustain a complex thought! Bush is a vacuum, a black hole, I'm surprised the Lincoln bed doesn't get sucked into him. I repeat: I won't have a relationship with anyone who votes for them.
```

---

## IC-0661: Perfect Pie

- Title: Perfect Pie
- Author (byline): Judith Thompson
- Work: Not specified
- Publisher: Playwrights Canada Press
- Publication date as stated: 2000
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: PATSY, MARIE, ACTRESS 1, ACTRESS 2, FRANCESCA
- Teaser before the introduction: Yes
- Spoken words (computed): 2231
- Already set (do not supply): none

### Source block (context only)

```text
Author: Judith Thompson
ISBN: 978-0887545900
Publisher: Playwrights Canada Press
Date (Month/Year): 2000
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Patsy and Marie meet as children and become fast friends, despite their differences.

ACTRESS 2: Together they deal with poverty, their parents, bullies and puberty.

ACTRESS 1: But at 15, a Sadie Hawkins Dance changes everything.

TOGETHER: Perfect Pie by Judith Thompson
```

### Performance text (classify this)

```text
(School yard – Marie scratches her head while looking at the ground)

PATSY: (Pg 13-14) Where do you come from anyways?

MARIE: Detroit. My dad he grew up here but then they lost the Farm, cause our well run dry and so he went to work makin’ cars in Detroit but he hurt his back and my Gramma took a stroke an left us the house so we come back.

PATSY: How old are you?

MARIE: Nine. My birthday was in August. August 23rd

PATSY: Oh my GOSH mine is January 23rd! That’s amazing. Maybe you could come to my birthday party. We’ll play musical chairs and my mother, she plays the piano? She’s singin’ and then when she stops? Like you have to sit in a chair, and . . .

(Patsy jumps into a “freeze” position. Marie expresses acceptance, joy)

PATSY: (Pg 19) Are you poor? You look poor. I mean only a little. Just the scabs on your legs. . . (Pg 22) Are you on welfare?

MARIE: No. Who told you that?

PATSY: Patty Hagerty. I told them that was not a nice thing to say. “If you can’t say anything nice don’t say anything at all.” That’s what my mother always says . . . (Pg 25-26) you have lice.

MARIE: No I don’t

PATSY: Yes you do. I saw one. Crawling on your head. This morning ‘cause you were sittin’ in front of me. (Marie has a defiant and shocked expression on her face) Honest. I did. I know what they look like ‘cause my brother had them once. The Welfares brought them into the school.

MARIE: I do not have lice.

PATSY: (Pause) I could show you a special way to get rid of them. Then they would be all gone.

MARIE: My mother won’t buy the shampoo. She says they’re not lice they’re bedbugs.

PATSY: That’s okay. Don’t you worry ‘bout a THING. I’ll get rid of ‘em for you. I know this REALLY special way. I’ll show you. You come over to my house, after school, okay? *****Scene break******

(First sleepover. Patsy is standing behind Marie, picking nits. She wears gloves)

PATSY: (Pg 29) Seventy-nine. Eighty.

MARIE: Holy Crow. Don’t tell nobody, eh?

PATSY: Eighty-one.

MARIE: My mother won’t do this. She says no child of hers has lice.

PATSY: I don’t mind doin’ it. I like it! Eighty-two.

MARIE: Sometimes, at night? I’m lyin’ in bed and the itchiness is so bad I think I’m just gonna jump out a window and run down the street screaming. TRANSITION

ACTRESS 1: As with all children . . . Patsy and Marie grew up . . .

ACTRESS 2: Patsy became a domestic goddess, steering clear of the big wide world.

ACTRESS 1: And Marie changed her name to Francesca and left town to become a somewhat successful actor.

ACTRESS 2: After 15 years apart, the two reunite at Patsy’s home and begin to reminisce

ACTRESS 1: But as this powerful play nears its end, we realize it is not a play about nostalgia at all

PATSY: (Pg 32-33) Does it still bother you, when you think about it? The way you were treated as a kid?

FRANCESCA: Sometimes in a flash I am eleven years old again and they’re throwing stones at me. Calling me those names and coughing. Remember? They used to cough when they saw me.

PATSY: Ignorant dogs.

FRANCESCA: On my bad days I think it was something in me. Something they detected? Something that is . . . still there. You know? There was a reason they picked on me, and not Darlene Rowan, who was also poor

PATSY: Because Darlene, she knew her place, right? She never raised her head!

FRANCESCA: So I walk out of my beautiful penthouse on the 20th floor feeling this big kind of Dirty Yellow Stain all over me. The Marie Begg Stain. I go to dinner parties, book launches and I feel that people are avoiding the Stain. I see their eyes wandering and I feel the others are whispering about me, and then I think I hear them coughing. And again, I am the girl with the running sores and the scabby legs, the lice and the dark circles under her eyes and the crooked teeth. I am Marie Begg. With the Stain.

PATSY: Well, you look pretty clean to me, if it’s any comfort. (Pg 20) Maybe you just weren’t ready for this place. That’s what I been tellin’ myself all these years, anyways. (Francesca is puzzled) . . . Why you woulda done what you did.

FRANCESCA: Abandoned you.

PATSY: Didn’t dare to look back. (Pg 44) I was in a coma for eight weeks, Francesca. Nothing was the same when I come out. (pg 20-21) When I woke up first thing I say, I go, “Where’s Marie? Where’s Marie?” I prayed for you, thinking you were dead or being tortured somewhere. I mean I didn’t know if you were even alive until I read about you in the paper, ten years later.

FRANCESCA: I stayed in Buffalo, for six months, on the street. Then, in Albany, New York. I remember being at a boyfriend’s, a much older guy, in his thirties. He said I could call anywhere I wanted and I dialed your number, but I hung up before it rang. I did that about twenty times.

PATSY: When I come out of my coma you had already been gone three weeks. (Pg 54) The crash left me with a big bag of bothers. Still can’t move my left hand well. Can’t walk fast, can’t run at all. And you know the weirdest thing? Can’t cry. Haven’t cried since before the crash . . . . (Pg 21 22) Your mother, she wouldn’t open the door for me; she screamed that the whole thing was all my fault. I was a tramp and a bad influence. I went to the police and they said you were a runaway, and you were almost sixteen so there was nothing they could do.

FRANCESCA: I remember sitting in Buffalo, 15 years old, eating onion rings, with money I’d begged, and – knowing – deep – in – my – stomach – that nobody was . . . ever coming after me. (Patsy goes to Francesca)

PATSY: I always felt if I hadda told them . . About everything . . . You know. Like what . . . happened . . . then they woulda gone after you. (Francesca moves away as the mention of “what happened” fills her with terror). After what you had . . . you know . . . oh . . . I’m sorry. You don’t want to talk about it. I just wish that you would had called me, you know. I mean what . . what were you . . . afraid of?

(Francesca turns away) *****Scene break******

(Pg 68-70) (Girls are bushing dog poop off Marie’s coat)

MARIE: If somebody would just tell me why they are doing this to me, I would be their slave for life. What is WRONG with me. I know I’m not UGLY, aside from my face. I do really well in school, I’m nice. I mean what the hell is wrong with me?

PATSY: Well. Maybe . . if you had . . . a . . . .

MARIE: What? (long pause)

PATSY: Bath? I mean, no offense or anything, and it doesn’t bother me at all, but I was just thinking that maybe if you like, took a bath or a shower more.

MARIE: I smell? Really? But I wash under my arms with soap every day. I couldn’t smell. You’re crazy. (Patsy shrugs) Why didn’t you tell me this before?

PATSY: (Shrugs again) My mom says that when you reach puberty all these strange smells start to happen and well that you need to take a bath once a week.

MARIE: See the thing is . . I want to take a bath, right. But the last time I filled the bath my Mum gave me a black eye ‘cause we don’t have hardly any water in our well. (long pause) (Pg 74-75) I’m the town dog, Patsy. (Marie barks)

PATSY: Stop it. That is not true. (Marie tries to think of something positive to say to lighten the mood)

MARIE: Donny Neilson talked to me today.

PATSY: No way. I’ve never seen him talk to a girl.

MARIE: He was talking about how he plays hockey. How he plays every day for hours and hours. He said he dreams about hockey.

PATSY: He said all of that? To you? (Marie nods) Well, the Sadie Hawkins dance is comin’ up. Why don’t you ask him? *****Scene break******

(PG 76-77) Getting ready for the dance.

PATSY: Now, with the mascara, you brush over the eyelashes three times. And you have to wipe the wand off so it doesn’t get all goopy and make you look like white trash. (Steps back to look at Marie) Oh my god your hair is perfect. You look like Miss America. (Marie goes to touch her hair) Don’t touch it. (Marie goes to touch it) DON’T TOUCH it!

MARIE: I wish you were coming.

PATSY: Oh, this flu is so bad I can hardly see straight.

MARIE: What do I do if he kisses me, Patsy?

PATSY: You just kiss back. But gently. And above all do not let him feel you up. You know what they think of sluts around here. Look at Darlene Rowan.

MARIE: Yeah. . . .

PATSY: You just slap his hand, hard. And make sure everybody sees ya. (Takes her to a mirror) You are gonna be the prettiest girl at the dance. And they’re all gonna go like, “What happened to Marie Begg? I mean like where is Marie Begg? *****Scene break****** (Present day) (Pg 78-89)

FRANCESCA: I had worn that green dress you made me

PATSY: Yes you did . . . And I had brushed your hair until it shimmered. . . You looked beautiful.

FRANCESCA: I looked beautiful. I waited for him on the steps of the Kentucky Fried Chicken. And then there he was . . . we walked and he actually held my hand. I almost fainted. I had never been touched by a boy you see. We went into the gym with the streamers and the punch bowl. He was still holding my hand, but the others, Pat Letour and Roly and them, they stared and after a while, they started to cough. They were laughing at him and there was that moment when he knew he was being laughed at . . . because of me. He suddenly knew I was the school dog. He hadn’t realized, you see. COUGHING . . . because he was from St. Mike’s, so . . . so, he shook off my hand and, and, and . . .

PATSY: And then what, Marie? What happened then?

FRANCESCA: He never came back. I waited by the wall and I waited. And they stared and they gathered and they threw spitballs and he never came back. I walked out. My head down, my legs shaking, across the football field. In my mother’s high heels . . . And they were suddenly there. Pat, Roland, Mike and Jamie and they pushed me from behind and they were laughing. And saying my hair looked nice. And all their hands, their fingers, touching me. I tried to walk past them.

But someone grabbed my arms. So hard. They kept laughing. And coughing. Their saliva spraying on my face and saying dirty words, filthy words I didn’t understand. And then I fell backwards and them all unzipping their pants and then wham! I could feel the spraying on my face, and see their faces . . . the sound, the spraying, the SMELL Ohhhhhhh, Patsy, the SMELL . . . (Francesca collapses and relives the memory) *****Scene break******

(Patsy is making an apple pie while she waits for Marie to get home from the dance. Her back is to Marie who enters – she is shaking uncontrollably and her teeth are chattering. Her dress is covered in mud and ripped. There is blood)

MARIE: Patsy?

PATSY: How was it? Gimme all the dirt. I want every detail. (Turns to Marie) Holy God. What happened to you? (Marie cannot answer. She sits down, trembling, shaky. Patsy approaches her. Marie smells terrible of urine) Aww. (She gags) Marie?! Marie, have you peed your pants Marie? What happened to you? (Marie doesn’t answer) Marie. You’re shaking. Did you get hit by a car or something? Where’s Donny? Did he drop you off here?

MARIE: I walked from town.

PATSY: You walked! That’s ten miles, Marie. Look at you, you’re barefoot, where are your shoes, Marie?

MARIE: Is it true about Holly French? . . . That she does that all the time? She does that with all of them . . . That’s what they said. (Marie begins to walk in circles around the room, speaking in a low continuous mutter) She does it all the time . . . all the cute girls do. Really really you gotta trust us: Okay, are you sure? Really is that true that all the cute girls do this? Really I don’t believe you guys, you guys are teasing me. Oh yeah, yeah, baby, promise promise on my mother’s life, right here by the goalpost. Every dance Holly and Carol and Nancy. We’ll be gentle, come on, you are so pretty. We’ll be gentle. Me pretty? We have always liked your legs . . . such nice long legs let us see your legs . . . pull up the dress. You can come to all our games now, Marie, and party after. Would you like to come with us and party . . . hard? “YOU DOG. TURN OVER YOU DOG. I’LL SCREW YOU TO DEATH” And barking and coughing and barking. “TURN OVER BITCH!” (Marie runs from the house; Patsy is stunned, silent, devastated, then rushes to follow Marie.) *****Scene break******

(Marie has left the house and climbed up the hill to the railroad tracks)

PATSY: Marie!! Wait up, wait up! Marie, where ya goin’? You’re not thinkin’ of doin’ something stupid are ya?

MARIE: I’m waiting for the train, Patsy.

PATSY: Train doesn’t stop here, Marie. Only stops in Belleville.

MARIE: It will stop for me. . . Goin’ away now.

PATSY: Marie, if you don’t get down from there the train is going to hit you.

MARIE: The train will stop for me. It will stop for both of us, Patsy. Come on, Come with me. (Motions for Patsy to join her on the tracks)

PATSY: Just come on down from there and we’ll go to the police. It’s the right thing to do Marie.

MARIE: Patsy . . . I’m scared.

PATSY: (hears the train whistle in the distance) Marie you come offa this track. I think I hear something. Marie! (Marie stretches her hands towards the direction the train will be coming from. Patsy tries to pull Marie off -- Adult Patsy steps out of the scene and voices the next lines in memory) And . . . and the train is coming, I can feel it in my feet and I pull . . . and I pull . . . wanna save my friend . . . and then . . . I can’t explain it, but suddenly I looked at the moon and I thought, “Yeah Me and Marie, me and Marie. (Young Patsy climbs back on the tracks behind Marie) “We are gonna die beautiful, we are gonna fly through the sky.” (Adult Patsy) And I held your hand . . . (both hold up theirs hands in the light of the approaching train until at the last moment, Marie’s thinking clears, she gets off the tracks and tries to pull Patsy off) And YOU are pullin’ on me. Pullin’ away, but I am not gonna let you go. I am going to stay on this track. Then I feel it. I feel it in my feet and

(Both girls fly through the air to the ground in a heap) We flew. You saved my life, Marie.

FRANCESCA: No . . . No . . . no we were there together and we both wanted to fly away, that’s all we wanted, to – fly away. (Long pause . . . then Marie finally confesses to Patsy) (Pg 37) Lying in that hospital bed for all those weeks, with broken bones, I stared at the ceiling and I knew how I would end up if I stayed. I would end up the way they all thought of me. You can’t keep fighting the way people think of you, eventually, you have to give into it, and become it. And that’s when I decided that I was going to leave Marie behind . . . and I was never ever going to come back.
```

---

## IC-0662: Phaedra in Delirium

- Title: Phaedra in Delirium
- Author (byline): Susan Yankowitz
- Work: Divine Fire: Eight Contemporary Plays Inspired by the Greeks
- Publisher: Back Stage Books
- Publication date as stated: July 2005
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: FRIEND, PHAEDRA
- Teaser before the introduction: No
- Spoken words (computed): 1313
- Already set (do not supply): none

### Source block (context only)

```text
Author: Susan Yankowitz
Book: Divine Fire: Eight Contemporary Plays Inspired by the Greeks
ISBN: 0823088510
Publisher: Back Stage Books
Date(Month/Year): July 2005
```

### Introduction (context only: never use it for content warnings)

```text
There is no such thing as an original play. None of the classical Greek plays was original – they were all based on earlier plays or poems or myths. In the prologue of Euripides’ Hippolytus, the goddess, Aphrodite declares herself resolved to punish the Hippolytus, son of Theseus, who disdains her and pays his worship to Artemis. With this design she has put into the heart of Phaedra, the wife of Theseus, a love for her stepson. This Theseus will learn, and then will destroy his son by one of three fatal wishes which Poseidon has promised to fulfill. This will involve the ruin of Phaedra too, but for that there is no help, the goddess caring first for her honor and herself. Adapted from various versions of the myth, it is the story of Phaedra that is told by Susan Yankowitz in this opening scene of Phaedra in Delirium.
```

### Performance text (classify this)

```text
FRIEND: Phaedra's sick. For weeks she's been in here, rooted to her bed. Sleeping. Not sleeping. Lady of leisure, or lady of lamentations: lady layabed. She needs me now -- I know she does -- and so I packed my bag and settled in to keep an eye on her. Not that it helps, not that she cares. She barely answers when I talk to her, doesn't drink, doesn't eat, doesn't really see me, and doesn't budge from that bed, as if she didn't know the difference between night and day, day and night. Sometimes I hear her tossing and turning, full of moans and sighs; and the rest of the time--

(PHAEDRA sits there, supported by pillows, looking at herself in a mirror) --she stares in that mirror, stares and stares, as if she's married to it. But she's not. She's married to Theseus, a wealthy man, a powerful man, Theseus who is away, frequently away, I hear, on business, he says, always on business -- but what business can that be? He's almost newlywed, and he lets business seduce him from his home?

(moving closer) That's what's eating her up, it must be. I'm a woman and her friend; I know these troubles. She feels abandoned, she longs for him, she worries that he regrets the marriage already, that in six months' time he's bored with her, lost himself in a strange woman's lap...

PHAEDRA: (delirious) It's so hot in here, I'm suffocating..... asleep, awake, my dreams are heavy with him, my tongue is parched, my lips can't open without his lips near ..... the mountains! I want to go with him to the mountains, to be with him in the air, with the wind on my skin and the rustle of leaves and the silence that has wildness in it, the sense that something could happen ..... anything could happen ..... in the night, in the dark

FRIEND: (touches her forehead) Shh. Shhh. The fever's making you talk like this. You're burning up.

PHAEDRA: Good. I'll be consumed, I'll turn to flame, to ash, I'll become pure yes, pure spirit.

FRIEND: You're sick, that's all. People live through sickness and go on to love their lives. Let me call the doctor, get you some medicine.

PHAEDRA: There's no medicine for this.

FRIEND: It's been three days. You have to eat something.

PHAEDRA: I can't! I'll live on nothing -- or better still, not live at all.

FRIEND: Now why are you so morbid!? The man adores you, worships you. Everyone knows that. So he's away for a while. So it's hard to be without your husband. But it's no tragedy.

PHAEDRA: You! What do you know of tragedy?!

FRIEND: (offended) And what do you know of me? I understand suffering, believe me. I'm not ignorant of life. So I never married. I know how to enjoy myself without going crazy. Without driving everyone else crazy! You may love your extremes but I prefer the middle ground.

PHAEDRA: How comforting for you.

FRIEND: You could be comfortable, too. But you won't let yourself. You give in to every feeling, you wallow in your misery as if it were pleasure. What's wrong? Tell me.

PHAEDRA: Please. Go away.

FRIEND: I won't. I'll wait right here until you tell me what's happened. Why else did I come to stay with you? I've been up all night, worrying, worrying; my nerves are shot. What awful news have you heard?

(silence)

Oh great suffering angel, great mum's-the-word, great martyr of the bleeding silence, talk to me! Is Theseus hurt? In danger of some kind? Speak up! Is he dead?

PHAEDRA: I've heard nothing about Theseus. Nothing at all.

FRIEND: Well, then, why all the fuss? Some women would be thrilled to have their husbands out of town for a while, then suddenly, excitingly, turn up one lonely night and slip between the sheets.

PHAEDRA: Some other woman, maybe. Some other sheets.

FRIEND: So he is with another woman. Don't deny it, I see it in your eyes, that green flame. What did you expect? We all know Theseus. That man never could resist a woman! So what? Who cares if he's having a fling? Look at the fabulous life you have! I've never seen such luxury: this beautiful house, the gardens, horses, a lake...

(strokes the bed linens) In my entire life, I've never even touched sheets like these.

PHAEDRA: Trust me, you wouldn't want to lie in this bed.

FRIEND: Oh yes, I would. I'd delight in everything you have! Why can't you? You don't have cancer, your heart is strong; I can hear it pounding from here. You're too young for this `sickness unto death'.

PHAEDRA: Too old, you mean, to suffer the petty griefs of love. Come here. Closer. Look. Gravity has her hands on me, she's pulling at my skin, pulling down down down, turning muscle soft and falling off the bone.

My cheekbones are vanishing. And my hair is losing its color. Do you see? There's a stripe of grey right here.

FRIEND: That's not a disease. It's nature.

PHAEDRA: I hate nature! I hate what she does to us. You'll understand soon enough. Every woman who's reached my age knows what I mean. Suddenly, overnight, we become invisible. We could walk down the street naked and no one would notice. Oh, yes, we can celebrate our `glorious, our liberating maturity' -- but who burns for us now? Who pours out his heart in poetry and midnights? No one. Never. It's obvious: we're the fate that every woman is trying to escape.

FRIEND: You're very beautiful.

PHAEDRA: Beautiful, oh yes -- for a woman my age. That's what people say and think they're being kind. `How beautiful she is for a woman her age!' But I can't fool myself; I have eyes. Everywhere I go I see them, the girls with glowing skin, their faces and throats like unmarked paper, their stomachs little bowls turned inside out.

FRIEND: They'll get older, too, you know.

PHAEDRA: But they have time! They have time now, when they need it! Oh God, how fast it goes. Only yesterday I walked down the road, sending up clouds of musk. My breath was an invitation. No man would have refused me.

FRIEND: Who would refuse you now? No one, no one.

PHAEDRA: Really?

FRIEND: Is that what happened? You met a man and you wanted--?

PHAEDRA: Wanted?! Me? What could I possibly want?! I'm a wife, the wife of Theseus, a great figure in the world, an important man!

FRIEND: And he should be with you. I'm going to track him down. It shouldn't be too hard.

(She exits. PHAEDRA turns around on her bed to face the audience, her head bowed forward under the weight of an enormous mass of hair piled on top.)

PHAEDRA: (tries to lift her head; she can't) This hair I can barely lift up my head so neat, so proper, no wisps flying it weighs me down

(Occasionally she succeeds in raising her head but slaps herself down) Girl ..... run through the fields ..... hair flying ..... unbraid the braids ..... raise the sails ..... let the horses loose ..... slap! grow up! running ..... toes like worms, feet like birds ..... where are your shoes? slap! slap! ..... grow up! ..... can't see the stars the sun the skies ..... the floor is grey and dirty, the ground hits my eyes ..... lift! slap me down! ..... pins in my scalp a torture, pins like needles, needle in the haystack, jumping falling hay in my hair slap! ..... can't go wild, can't go child ..... stop! slap! ..... sit still ..... grown up ..... heavy heavy heavy the head that ..... can't move can't dance can't throw back my head for song or love or..... heavy ..... heavy ..... heavy Finally PHAEDRA can lift her head. She is facing the audience. She takes a deep breath, then swirls her hair around and around her with increasing freedom. She pulls down her nightgown so that her bare shoulders are exposed, and lets her hair move over them. Her eyes are closed, and she is smiling, standing in a field of hairpins.

This is how he saw me when he saw me first. This is how I felt, this is how it felt when he saw me first.

(swirls her hair) This is how I want it to feel ..... like hands on me like
fingers playing on my skin.
This is who I was when he saw me first.
This is how I felt when --

(IPPOLYTUS appears, dressed in a white linen suit. PHAEDRA turns in his direction. Slowly, as if against her will, she walks toward him. She stands directly in front of him) So. You're Hippolytus.

(Transfixed, she takes his hands in hers and holds them for a long time) Hippolytus. You have your father's hands.
```

---

## IC-0663: A Piece of My Heart

- Title: A Piece of My Heart
- Author (byline): Shirley Lauro
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Jan 1992
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MARTHA, LEEANN, INSTRUCTOR 1, INSTRUCTOR 2, SERGEANT, OFFICER, SISSY, HEAD NURSE 1, WHITNEY, MARYJO, STEELE, SOLDIER, HEAD NURSE 2, VOICE ON INTERCOM, LEANN, LEANNE, BOTH, PROTESTOR, FRIEND, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1538
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shirley Lauro
ISBN: 978-0573693335
Publisher: Samuel French, Inc.
Date (Month/Year): Jan 1992
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Elizabeth Kenny once said, “When you’re a nurse you know that every day you will touch someone’s life, or someone’s life will touch yours.”

ACTRESS 2: In Vietnam countless lives were touched by the devoted nurses who cared around the clock for our fallen troops.

ACTRESS 1: In this selection a group of young women: Martha, Leann, Sissy, Whitney and MaryJo – who dreamed of becoming military nurses for a variety of reasons

ACTRESS 2: But none are prepared for the true atrocities of war.

TOGETHER: A Piece of My Heart by Shirley Lauro
```

### Performance text (classify this)

```text
Suggested Roles

Actress 1: Martha, Instructor 1, Sergeant, Sissy, Head Nurse 1, Steele, Soldier, Protestor, Friend

Actress 2: Leeann, Instructor 2, Officer, Whitney, MaryJo, Head Nurse 2, Voice on Intercom

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

MARTHA: (Pg 14) (Smiling ruefully) I was an army brat. Martha O’Neil. Dad a career man. Mom a navy nurse. World War II. I was born at Ft. Benning, grew up at Ft. Bragg. I remember one day in junior high, a girlfriend came in crying: her dad was going to Vietnam. They sent her home . . . must’ve been around 1961. . . so I knew early on about Vietnam. Americans being killed there. Back of my mind was: I want to go there. Be a Navy nurse, serve my country and protect our men.

LEEANN: (Pg 17) I was anti-war! So [were] my friends! We were hippies – Woodstock, bell bottom jeans, headbands, the long hair . . . Then I remember Kennedy going, “What can you do for your country?” Well, I was twenty-one when an Army recruiter comes to my nursing school dressed in her uniform – showing us this wonderful film about the glamour of being an Army nurse and these gorgeous hospitals all over the world with all this modern equipment. And I was very impressed!

INSTRUCTOR 1: (Pg 22-23) Ladies! There are ways to be a young lady worthy of the Red Cross!

INSTRUCTOR 2: At all times be feminine!

INSTRUCTOR 1: Never swear!

INSTRUCTOR 2: Never be provocative with men!

INSTRUCTOR 1: Because you are a Red Cross girl!

INSTRUCTOR 2: Symbol of Purity.

INSTRUCTOR 1: Goodness, and Light!

INSTRUCTOR 2: Sister, Mother, Girl- Next-Door.

INSTRUCTOR 1: The All American Girl to every service man you meet!

SERGEANT: (Pg 26) ATTENTION!

OFFICER: All of you have orders for Southeast Asia.

SERGEANT: Dismissed!

SISSY: They wouldn’t even say Vietnam.

LEEANN: I’m going to my head nurse (shift of scene) (Pg 27) But I’m anti-war. I’ll take care of them in Hawaii.

HEAD NURSE 1: They’re overstaffed there. And you’re top of the line. You can make a real contribution in Vietnam.

WHITNEY: (to audience) (Pg 28) And they put us on an airplane in little powder blue, Red Cross uniforms and dixie cup hats and heels and stockings!

MARTHA: And off we go

MARYJO: (to audience) (Pg 29) There are just a few women on my plane – two hundred men! And everybody is trying to be sweet

SISSY: Singing, drinking, playing checkers –

LEEANN: I ask my stewardess for a pillow – she pretends she doesn’t hear me – she brings pillows to the men

MARTHA: (Pg 30) Then suddenly it all just quiets down (looking out plane windows)

MARYJO: No one talks.

SISSY: Nobody says a word.

WHITNEY: VIETNAM! Look how beautiful it is . . .

MARTHA: How can there be a war way down there? (Sound of BOOM)

STEELE: (Pg 31-32) My God!!! Tracers!

LEEANN: Puffs of smoke!

WHITNEY: (stunned) We’re being fired on!

SISSY: FIRED ON? I haven’t done anything to them!

LEEANN: I’m a nurse!

SOLDIER: There are Viet Cong on the landing fields

LEEANN: (lights go out) Night! Blackout! Can’t see the runway! Nothing! Dead silent on the plane!

SISSY: But I hear 247 souls breathing . . .

WHITNEY: The doors open –

MARTHA: Spotlights flashing --

LEEANN: Vietnamese – everywhere – screaming – shrieking –

OFFICER: (Pg 34) Attention! All new nurses report to North area at once! *****scene*****

MARTHA: (to audience) (Pg 37) The hospital is a series of Quonset huts – I’m assigned to the night shift.

HEAD NURSE 2: (initial tour of the facility) (Pg 38-39) Here on the wards you will be responsible for 300 to 350 patients. As supervisor you will care for the sickest patients yourself.

MARTHA: (staggered) 350 patients?

HEAD NURSE 2: Night duty is the hardest, of course. People die at night. And wounded people, Captain, get very frightened at night. They moan, they cry out . . .

MARTHA: (Pg 40) But there are so many injuries – and the kinds of injuries – (Pg 39) (to audience) Respirators! Catheters! Drains! I’ve never seen anything like this in my life!

HEAD NURSE 2: (interrupting) (Pg 40) Stuff it, Captain! Or you will never be of use! Your work is to patch up the soldier so he can get back to the battle field – (Pg 39) Build a psychological wall! (Pg 40) Don’t think! Stay behind your wall! *****scene*****

VOICE ON INTERCOM: (Pg 41-42) There is a mass casualty coming in. All new nurses report at once to Emergency. I repeat: Mass casualty is coming in. (a scramble, then shock as the first GI is brought in – then rapid overlapping chaos)

LEEANN: (Pg 44) Holy shit!

SISSY: He’s got no legs! Thighs down!

MARTHA: Gone!

LEEANN: So much blood! The doctors and nurses are doing then thousand things.

MARTHA: (Pg 45-46) Blood is spurting up!

SISSY: BLOOD IS SPURTING UP!

MARTHA: (to audience) I can’t move! I can’t talk! I can’t do anything! Amputations –

LEEANN: Burn cases –

MARTHA: Part of me is saying:

LEEANN: Jesus Christ! Just look at this!

SISSY: The other part says:

LEEANN: What’s your problem?

HEAD NURSE 1: Nurse, start the IV! Nurse!

LEEANN: I can’t! Doctors did it at home! I don’t know how!

HEAD NURSE 1: START THE IV!

SISSY: (to audience) And I turn, and I look at this patient

LEANN: (to audience) And half this soldier’s face is gone!

SISSY: It’s okay, I’m here – I’m right beside you – (to audience) His name is Jimmy. And he’s wide awake! Jimmy? You’re not alone – I’m here . . . (flatliner sound)

HEAD NURSE 1: Next patient! Move on!

SISSY: (Pg 73) (to audience) But we lose all GIs –

LEANNE: (to audience) And I am left with them alone – all the corpses stacked up like cordwood in a little tiny room with me – and then --

SISSY: (to audience) (Pg 78) [More] patients start coming in one after the other after the other – I’ve never seen so many patients in my life!

MARTHA: Here’s a yellow sheet of paper. Make a list. Worst ones at the top –

LEEANN: But they’re coming so fast, so fast –

MARTHA: Start using numbers instead --

LEEANN: Then someone worse comes in –

MARTHA: And I put his number at the top.

VOICE ON INTERCOM: (Pg 79) Attention! Sapper attack! The enemy is penetrating our perimeter. Attention! Be alert! Be Alert!

MARTHA: The enemy is coming in here? Oh my God! (explosion, screams) (Pg 80-81) THE WARD IS HIT! (Pg 80-81) Corpsman, lock the door! (to audience) [But there’s] shrapnel flying though his head! And he falls on me! DEAD!! Chunks of flesh – blood – all over the walls

LEEANN: Screaming – yelling – smell of burning flesh –

MARTHA: My patients!

SISSY: Killed! In their hospital beds! *****scene*****

MARTHA: (to audience) I’m heading into the operating room the fourth day? The fifth? And I see water coming out of the scrub sinks splashing on the floor – and patients lying on the floor – blood – the water mixing with the blood and running down the hall – a river! Oh God! Help me stay behind my wall!

LEEANN: (to audience) It’s an 18-year-old coming into surgery – he’s so young he doesn’t even have hair on his face – and I’m running beside his stretcher, and he’s crying – Mommy? Mommy? And I’m saying: I’m here, baby – Mommy’s right here! Only I’m just 21 myself.

SISSY: (to audience) He’s a blond kid from California looking just like your brother and screaming: I DON”T WANT TO DIE!

MARTHA: (to audience) (Pg 82) A piece of my heart goes with each of them! A PIECE OF MY HEART!

WHITNEY: (to audience) A hundred days before you leave you start filling in the short timer’s calendar – marking off each day.

MARTHA: (to audience) Wanting to go – but not wanting to go –

LEEANN: (Pg 83) I walk into the hospital to say goodbye. Strangely quiet day. Suddenly the double doors burst open and two litter bearers run in, set down their litter, run out. (looking closely at the patients) A little Vietnamese boy and girl – both with their hands chopped off. Looking at us – (she struggles with the image) gaping, dumb, numb – I walk out the door of the hospital in silence – for the last time, Vietnam. I am going home. *****scene*****

BOTH: (Pg 86) American soil!

LEEANN: (Pg 93-94) (to audience) I end up on a bus to LA – In the depot I see people waving signs –

PROTESTOR: (marching and yelling) PEACE NOW! HEY, HEY, LBJ, HOW MANY KIDS DID YOU KILL TODAY? MAKE LOVE, NOT WAR!

LEEANN: My friend comes running up

FRIEND: Jesus! You got a dress in your bag? Jeans? Something else to wear?

LEANN: (proudly) It’s my uniform! It’s got all my medals on!

FRIEND: Go change! You’re a target! For God’s sake!

LEANN: Target?

PROTESTOR: (yelling in her face, spitting) MURDERER! BUTCHER! GO BACK TO NAM! WAR MONGER! GET OUT OF HERE!

LEEANN: (to audience - confused) So I run to the washroom, change out of my uniform, I run back.

(to Friend) Burn it! (throws duffle on ground).

FRIEND: But your medals . . .

LEEANN: **** MY MEDALS! BURN IT, I SAID!! *****scene*****

LEEANN: (Pg 100-101) (to audience) I’m out of the service. San Francisco. Intensive care. They won’t let me hang a pint of blood without supervision. I was treated different in Nam. Trusted. They’re putting me through an Orientation Course about CPR?! I quit!

MARTHA: (Pg 100-101) (to audience) I go back into the military. The Reserves. To teach. A chance to show my skills. (To Leeann) I can’t stand these Reserve nurses! They played it safe during Nam. Why aren’t they active? All these nurses paid for practicing? Why don’t they do what they’re practicing for. I quit!

LEEANN: Job to job to job –

MARTHA: Looking – for the respect – the thrill – the challenge –

LEEANN: Homesick for the GIs of Nam.

MARTHA: “Adrenalin Junkies” that’s us.

LEEANN: (to audience) I stop putting Nam down on my application form. I demonstrate against the war! I march! I carry signs!

SISSY: (Pg 111-112) (to audience) Since I came back I’ve watched MASH. Current. Reruns. Everything. I cry. Every time. Doesn’t matter what the story is. I cry. Chopper in the sky I cry. Color khaki on the screen I cry. Sad . . . terribly sad to me – all of it . . . (starting to tear up)

LEEANN: (Pg 114-115) (anger and rage mount as she speaks) I see the hostages from Iran on TV. And this is pissing me off! They are getting into limos for this big parade with the Yellow Ribbon Welcome and what did they do? Sat around four hundred days reading coming books while I was risking my life. Getting cursed and spit at in my uniform? (Martha grabs her, tries to calm her down; she wrenches free) No! Don’t you touch me! I could kill someone, you know that? I could kill . . . me (breaks down into tears) me . . . me . . . me . . .

MARTHA: (Pg 116) (moves away, to audience) You people! Whoever you are! Who sent me over there . . . You are hiding behind so many other people you will never be brought to justice in this world! I WANT YOUR DAY OF RECKONING TO BE AT HAND! I WANT YOU TO BURN FOREVER IN THE HELL OF VIETNAM! (Long beat) I want . . .

TOGETHER: to never fight another war. . . (Pg 124) (softly singing) America, America . . . God shed his grace on thee, and crown thy good with brother hood, from sea to shining sea.
```

---

## IC-0664: Playground Purgatory

- Title: Playground Purgatory
- Author (byline): Colin Nissan
- Work: Not specified
- Publisher: The New Yorker
- Publication date as stated: May 18, 2015
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ANNA, SARA
- Teaser before the introduction: Yes
- Spoken words (computed): 856
- Already set (do not supply): none

### Source block (context only)

```text
Author: Colin Nissan
ISBN: Magazine
Publisher: The New Yorker
Date (Month/Year): May 18, 2015
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Ask people what they think about SAHM’s

ACTRESS 2: That’s Stay-At-Home Moms

ACTRESS 1: . . . and you'll get a variety of answers:

ACTRESS 2: They're lazy.

ACTRESS 1: They're making the best decision of their lives.

ACTRESS 2: They're not contributing to society.

ACTRESS 1: They're making a great sacrifice to stay home and nurture their kids day in and day out.

ACTRESS 2: There's no shortage of opinions about women who stay home to raise their kids.

ACTRESS 1: But what’s it REALLY like to spend all day, every day ALONE with your toddler? (a variety of expressions pass over both faces)

ACTRESS 2: It’s purgatory . . .

ACTRESS 1: Yeah . . . purgatory . . . an extremely unpleasant experience that causes suffering

ACTRESS 2: There’s always the playground . . .

TOGETHER: Playground Purgatory by Colin Nissan
```

### Performance text (classify this)

```text
ANNA: Is that your little guy over there?

SARA: Yeah, that’s Sebastian.

ANNA: What a cutie. That’s my Tessa on the slide.

SARA: She’s adorable.

ANNA: I feel like I’ve definitely seen you here before. I’m Anna.

SARA: You look familiar, too. I’m Sara.

ANNA: We’re here a lot, Tessa and I.

SARA: Yeah, this is like a second home for Sebastian and me.

ANNA: This place is such a lifesaver.

SARA: Total lifesaver.

ANNA: We’re here every day. Sometimes twice.

SARA: Tell me about it, we were here for ten hours yesterday.

ANNA: I really treasure the time that Tessa and I spend here.

SARA: Wouldn’t trade it for the world.

ANNA: I’m always so happy when I’m here, and never feel strange or despondent.

SARA: Me, too. So happy. The sound of all the kids laughing and screaming is so joyous, and doesn’t sound anything like nails on a chalkboard.

ANNA: I’ve never cried behind that tree.

SARA: Me neither. (Pause)

ANNA: Tessa! Tess! Come on over here and put on your coat, O.K., sweetheart? It’s chilly out, and you need to put on your coat, O.K.? Your coat needs to go on your body. The fabric needs to cover your torso to help you maintain a proper internal temperature, or you’ll die, O.K., pumpkin? You’ll die of hypothermia, right here at the playground, unless you put your coat on. Your body’s going to start shutting down soon. It’ll feel like you’re getting sleepy for nap time, but you’ll actually be getting sleepy for dying. Get your coat on ! (Pause) Is that your little guy over there?

SARA: Yeah, that’s Sebastian.

ANNA: What a cutie. That’s my Tessa on the slide.

SARA: She’s adorable.

ANNA: Wait. I’m sorry . . . did I already ask you that?

SARA: Did you? I don’t think so.

ANNA: I’m so embarrassed.

SARA: Did I answer you again?

ANNA: I . . . don’t know. (Pause) I feel funny sometimes.

SARA: It’s this place. It’s evil.

ANNA: I’m scared.

SARA: There are dark forces here. Powerful forces.

ANNA: And yet it’s the only place that makes sense to me anymore. Here and my bathroom.

SARA: Sometimes, when I’m in the sandbox, I can feel myself sinking, like something is pulling me down. I can feel the sand slowly surrounding me, suffocating me, and it feels good. (Pause) We should totally do a playdate sometime!

ANNA: Oh my God, it would be so great to do a playdate!

SARA: Is that applesauce on your shirt?

ANNA: This? No, this is throw-up. Tessa regurgitated on me. But, applesauce or throw-up, what’s the difference, really? They’re both just things that get on your shirt that you lose the will to wipe off after a certain point, because either way you’re going to give yourself a haircut with a kitchen knife, right?

SARA: So true.

ANNA: There’s also string cheese in my hair, not sure if you saw that.

SARA: Last night, I found a cheddar Goldfish in my *bra.*

ANNA: Wow.

SARA: Yeah.

ANNA: In it?

SARA: Right in it. (Pause)

ANNA: Tessa! Honey! Share the slide, Honey Bear! We don’t own the slide, O.K.? We have to share, because if we don’t society will collapse and we’ll become no better than animals, tearing one another limb from limb just to survive. This playground and everything around it will deteriorate into a dystopian war zone, a lawless heap of smoldering ash. And guess what dystopian war zones don’t have? Slides. Share the slide! (Pause)

SARA: Hey, look who just walked in.

ANNA: Where?

SARA: Over there, by Nanny Alley.

ANNA: Oh boy.

SARA: Stay-at-home Hottie McBjörn.

ANNA: Daddy’s home.

SARA: Daddy’s home, all right.

ANNA: Bad day for me to not shower.

SARA: Bad day for me to be twice my college weight.

ANNA: Oh my God, have you seen his wife?

SARA: No! You?

ANNA: She made an appearance here. Once. Working mom.

SARA: So sad.

ANNA: I know.

SARA: And?

ANNA: Meh.

SARA: He deserves more than that.

ANNA: So much more.

SARA: He’s hurting.

ANNA: You’d never know it. He’s so brave. And able. I saw him tie a water balloon with one hand before.

SARA: I saw him make a diaper out of leaves. (Pause)

ANNA: Well, well, well, look over there by the monkey bars.

SARA: If it isn’t Hot Skinny Mom.

ANNA: She’s got some nerve. Ms. My Baby Weight Just Vanished Because I’m a Terrible Person.

SARA: Ms. I Carry a Yoga Mat on My Back Because You Never Know When I Might Just Start Doing Yoga.

ANNA: Ms. My Hair Is Washed.

SARA: Ms. I Went to Law School but Decided to Work Part Time at an Inner-City Nonprofit for At-Risk Youth So I Can Give Back to the Community Because I’m So-o-o-o-o-o-o Skinny!

ANNA: What?

SARA: Sorry, I don’t know what that was. (Pause)

ANNA: I love her outfit.

SARA: It’s so cute I want to tear her little arms off.

ANNA: Tessa? Tess, honey! It’s time for lunch, O.K.? Let’s take a break and have something to eat now, because Mommy’s hungry, too, and Mommy can’t eat her lunch until you’ve eaten yours, because, as you know, Mommy’s lunch is just the remnants of your lunch—your toast crusts, your milk backwash, and, with any luck, a frantic lick of your half-eaten yogurt container. O.K., Sugarplum? Come eat your lunch! (Pause)

ANNA: Such a beautiful day here today.

SARA: It’s perfect.

ANNA: Not a cloud in the sky.

SARA: Never is.

ANNA: I’m Anna, by the way.
```

---

## IC-0665: Poof!

- Title: Poof!
- Author (byline): Lynn Nottage
- Work: Plays for Actresses, Pgs 523 - 534
- Publisher: Knopf Doubleday Publishing Group
- Publication date as stated: Mar 1997
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SAMUEL, LOUREEN, FLORENCE
- Teaser before the introduction: Yes
- Spoken words (computed): 1533
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lynn Nottage
Book: Plays for Actresses, Pgs 523 - 534
ISBN: 978-0679772811
Publisher: Knopf Doubleday Publishing Group
Date (Month/Year): Mar 1997
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: *According to the Bexar County Family Justice Center, yearly an estimated 1.3 million women in the US are victims of physical assault by a domestic partner each year. Many cases go unreported because help often doesn’t come.

ACTRESS 2: And when women fight back, they can be punished. **In 2021 women were responsible for just 10% of homicides. Many cases involved a history of domestic abuse.

ACTRESS 1: In this selection, reality is pushed to the extreme. After years of silence, one moment of speaking out . . .

ACTRESS 2: “DAMN YOU TO HELL, SAMUEL!”

ACTRESS 1: . . . makes Loureen’s abusive husband spontaneously combust.

ACTRESS 2: What follows is fear, confusion and an almost giddy relief.

ACTRESS 1: For many women, escaping abuse isn’t simple. But it does raise the question: When survival becomes a crime…

ACTRESS 2: What choice is there?

TOGETHER: Poof! by Lynn Nottage

A huge pile of smoking ashes rests in the middle of the kitchen. LOUREEN, a demure housewife in her early thirties, stares down at the ashes incredulously. She bends and lifts a pair of spectacles from the remains. She ever so slowly backs away)

LOUREEN: Samuel? Uh! (places the spectacles on the kitchen table; looks around) Don't fool
```

### Performance text (classify this)

```text
SAMUEL: (Pgs 523-534) (offstage) WHEN I COUNT TO TEN, I DON' WANT TO SEE YA! I DON' WANT TO HEAR YA! ONE, TWO, THREE, FOUR . . .

LOUREEN: DAMN YOU TO HELL, SAMUEL! (a bright flash)

with me now. I'm not in the mood. (whispers) Samuel? I didn't mean it really. I'll be good if you come back. . . Come on now, dinner's waiting. (chuckles, then stops abruptly) Now stop your foolishness. (examines the spectacles) Uh! (softly) Don't be cross with me. Sure, I forgot to pick up your shirt for tomorrow. I can wash another, I'll do it right now. Right now! Sam? (cautiously) You hear me!(awaits a response) Maybe I didn't ever intend to wash your shirt!

(pulls back as though about to receive a blow; a moment) Uh! (dials the telephone) Florence, honey could you come down for a moment. There's been a little accident. (gets a broom and a dust pan, hesitantly approaches the pile of ashes. Takes a closer look. Grins)

FLORENCE: (enters in a rush) HEY!

LOUREEN: (pointing at the ashes) Uh! (struggles to formulate words) Uh!

FLORENCE: You all right? What happened? (sniffs the air) Smells like you burned something? (stares at the huge pile of ashes) What the devil is that?

LOUREEN: (hushed) Samuel. . . It's Samuel, I think. (nods her head repeatedly) It's him. It's him.

FLORENCE: Chile, what's wrong with you? Did he finally drive you out your mind? I knew something was going to happen sooner or later.

LOUREEN: Dial 911, Florence! Dial 911! (FLORENCE picks up the telephone and quickly dials) I think I killed him.

FLORENCE: (hangs up) What?

LOUREEN: (whimpers) I killed him! I killed Samuel! (wrings her hands)

FLORENCE: Come again. . . He's dead, dead? (backs away) No, stop it, I don't have time for this. I'm going back upstairs, you know how Samuel hates to find me here when he gets home. You're not going to get me this time. (louder) Y'all can have your little joke, I'm not part of it! (a moment -- takes a hard look at LOUREEN; squints) Did you really do it this time?

LOUREEN: (hushed) I don't know how or why it happened, it just did.

FLORENCE: Why are you whispering?

LOUREEN: I don't want to talk too loud something else is liable to disappear.

FLORENCE: Where's his body?

LOUREEN: (points to the pile of ashes) There! ...

FLORENCE: You burned him?

LOUREEN: I DON'T KNOW! (covers her mouth as to muffle her words; hushed) I think so.

FLORENCE: Either you did or you didn't, what you mean you don't know. We're talking murder Loureen, not oven settings.

LOUREEN: You think I'm playing?

FLORENCE: How many times have I heard you talk about being rid of him. How many times have we sat at this very table and laughed about the many ways we could do it and how many times have you done it? None.

LOUREEN: (lifting the spectacles) A pair of cheap spectacles, that's all that's left. And you know how much I hate these. You ever seen him without them, no! . . . He counted to four and disappeared. I swear to God!

FLORENCE: Don't bring the Lord into this just yet! Take your time.

LOUREEN: He was . . . standing there.

FLORENCE: And?

LOUREEN: He exploded. Boom! Right in front of me. He was shouting like he does, then he raised up that big crusty hand to hit me, and poof, he was gone . . . I barely got words out and I'm looking down at a pile of ash.

FLORENCE: (wipes her forehead) Chile, I'll give you this, you've matched my husband Edgar, the story king. He came in at six Sunday morning, talking about he'd hit someone with his car, and had spent all night trying to outrun the police. I felt sorry for him, forgot all about the fact that it was six in the morning. It turns out he was playing poker with his paycheck no less.

LOUREEN: You think I'm lying.

FLORENCE: I certainly hope so, Loureen. For your sake.

LOUREEN: Samuel always said if I raised my voice something horrible would happen. And it did!

FLORENCE: You've been watching too much television.

LOUREEN: Never seen anything like this on television. Wish I had, then I'd know what to do. . . He's not coming back. Oh no, how could he. It would be a miracle. Two in one day. . . I could be canonized, worse yet he could be. . . All that needs to happen now is for my palms to bleed and I'll be eternally remembered as St. Loureen, the patron of battered wives. Women from across the country will make pilgrimages to me, laying pies and pot roast at my feet and asking the good saint to make their husbands turn to dust. How often does a man like Samuel get damned to hell and go? (breaks down as though crying, but as FLORENCE consoles her friend, she realizes that LOUREEN is actually laughing hysterically) I DON'T KNOW WHAT TO DO NEXT! DO I SWEEP HIM UP? DO I CALL THE POLICE? (deep breath) I should be mourning, I should be praying, I should be thinking of the burial, but all that keeps popping into my mind is what will I wear on television when I share my horrible and wonderful story with a studio audience (whimpers) He's made me a killer Florence, and you remember what a gentle child I was. (whispers) I'm a killer, I'm a killer, I'm a killer.

FLORENCE: I wouldn't throw that word about too lightly even in jest. Talk like that gets around.

LOUREEN: I'll probably get the death penalty, isn't that what they do with women like me, murderesses.

FLORENCE: Folks have done time for less.

LOUREEN: Thank you, just what I needed to hear!

FLORENCE: What did you expect, that I was going to throw up my arms and congratulate you. Why'd you have to go and lose your mind at this time of day, while I got a pot of rice on the stove and Edgar's about to walk in the door and wonder where his damn food is. (losing her cool) And he's going to start in on me about all the nothing I've been doing during the day and why I can't work and then he'll mention how clean you keep your home. And I don't know how I’m going to look him in the eye without . . .

LOUREEN: I’m sorry Florence. Really. It's out of my hands now. (takes FLORENCE's hand and squeezes it)

FLORENCE: (regains her composure) You swear? You know what will happen if you're lying.

(LOUREEN nods) (FLORENCE examines the pile of ashes, then shakes her head) Oh sweet, sweet Jesus. He must have done something truly terrible.

LOUREEN: No more than usual. I just couldn't take being hit one more time.

FLORENCE: You've taken a thousand blows from that man. Couldn't you've turned the cheek and waited. I'd have helped you pack. Like we talked about. (a moment)

LOUREEN: Uh! ... I could blow on him and he'd disappear across the linoleum. (snaps her fingers) Just like that! Should I be feeling remorse or regret or some other "r" word? I’m strangely jubilant, like on prom night. That's the feeling! (they lock eyes) Uh!

FLORENCE: ls it ...

LOUREEN: Like a ton of bricks been lifted from my shoulders . . . yeah.

FLORENCE: (walks to the other side of the room) You b***! We made a pact. We agreed that when things got real bad for both of us we'd . . . you know . . . together. . . Do I have to go back upstairs to that . . . What next?

LOUREEN: I thought you'd tell me! I don't know!

FLORENCE: I don't know! (walks around the room nervously. LOUREEN wrings her hands and mumbles softly to herself) Now you got me Loureen, I'm truly at a loss for words.

LOUREEN: Everybody always told me, "keep your place Loureen." My place, the silent spot on the couch with a pleasant smile that warmed the heart. All this time I didn't know why he was so afraid for me to say anything, to speak up. Poof! . . . I've never been by myself, except for them two weeks when he won the office pool and went to Reno with his cousin Mitchell. He wouldn't tell me where he was going until I got that postcard with the cowboy smoking a hundred cigarettes . . . (FLORENCE nervously picks up SAMUEL's jacket, which is hanging on the back of the chair. She clutches it unconsciously)

LOUREEN: NO! NO! DON'T WRINKLE THAT, THAT'S HIS FAVORITE JACKET. HE'LL KILL ME. PUT IT BACK! (FLORENCE returns the jacket to its perch. LOUREEN begins to quiver) I'm sorry.

(grabs the jacket and wrinkles it up) There. (digs into the coat pockets and pulls out his wallet and a movie stub) Look at that, he said he didn't go to the movies last night. Working late. (frantically thumbs through his wallet) Picture of his motorcycle, social security card, driver's license, and look at that from our wedding. (smiling) I looked good, didn't I? (puts the pictures back in the wallet and holds the jacket up to her face) There were some good things. (sweeps her hand over the jacket to remove the wrinkles and throws it in the garbage) DAMN YOU TO HELL, SAMUEL! Those words made him disappear. Allthese years and just words, Florence. That's all they were.

FLORENCE: I'm afraid, I won't ever get those words out. I’ll start resenting you, honey. I'm afraid won't anything change for me. Edgar has never done me the way Samuel did you, but he sure did take the better part of my life. (shakes her head) I have the children to think of. Right?

LOUREEN: You can think up a hundred things before . . .

FLORENCE: (with an idea) Come upstairs with me . . . We'll wait together for Edgar and then you can spit out your words and . . .

LOUREEN: I can't do that.

FLORENCE: Ye,s you can! Come on now. (LOUREEN shakes her head) Well I guess my mornings are not going to be any different. (bitterly) But you got a broom and a dustpan, you don't need anything more than that . . . He was a bastard and nobody will care that he's gone.

LOUREEN: Phone's gonna start ringing soon, people are gonna start asking soon, and they'll care. Maybe I should mail him to his mother. I owe her that. I feel bad for her, she didn't understand how it was . . . He was always threatening not to come back.

FLORENCE: I heard him.

LOUREEN: It would've been me eventually.

FLORENCE: Yes.

LOUREEN: I should call the police, or someone.

FLORENCE: Why? What are you gonna tell them? About all those times they refused to help, about all those nights you slept in my bed ‘cause you were afraid to stay down here. About the time he nearly took out your eye ‘cause you flipped the television channel.

LOUREEN: I can't just throw him away and pretend like it didn't happen. Can I? (FLORENCE nods) Goodbye to the fatty meats and the salty food. Goodbye to the bourbon and the bologna sandwiches. Goodbye to the smell of his feet, his breath, and his bowel movements . . . (a moment; closes her eyes as though reliving a horrible memory, she shudders and walks over to the pile of ashes) Samuel? . . . just checking.

FLORENCE: Goodbye Samuel. (both smile)

LOUREEN: Chicken's warming in the oven, you're welcome to stay.

FLORENCE: Chile, I got a pot of rice on the stove. Kids are probably acting out . . . snd Edgar, well . . . Listen, I'll stop in tomorrow. (they hug for a long moment. FLORENCE exits. LOUREEN stands over the ashes for a few moments contemplating what to do. She finally decides to sweep them under the carpet)
```

---

## IC-0666: POTUS

- Title: POTUS
- Author (byline): Selina Fillinger
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Aug 2022
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SETTING, JEAN, HARRIET, MARGARET, FROM THE TV, CHRIS, DUSTY
- Teaser before the introduction: Yes
- Spoken words (computed): 1488
- Already set (do not supply): none

### Source block (context only)

```text
Author: Selina Fillinger
ISBN: 978-0573709999
Publisher: Samuel French, Inc.
Date (Month/Year): Aug 2022
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: One four-letter word is about to rock 1600 Pennsylvania Avenue.

ACTRESS 2: When the President unwittingly spins a PR nightmare into a global crisis, the brilliant and beleaguered women he relies upon risk their sanity to keep the commander-in-chief out of trouble.

ACTRESS 1: For any woman who’s ever found herself the secondary character in a male farce… This is

TOGETHER: POTUS by Selina Fillinger
```

### Performance text (classify this)

```text
Suggested Roles: Actress 1: Harriet (Chief of Staff); Dusty (POTUS’ pregnant dalliance); Chris

(a journalist)

Actress 2: Jean (Press Secretary), Margaret (First Lady), From the TV

SETTING: The White House – Perhaps not the current administration, exactly, but broad strokes of past presidents combined with stress dreams of future ones. And if we’re being honest, an amalgamation of them all . . .

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

JEAN: (Pg 1- 3) He said the words, “My wife’s a ****?” (expletive should be mouthed or indicated with a broad gesture rather than spoken) (beat)

HARRIET: He said, “Please excuse my wife’s absence. She’s having a *****-y morning.”

JEAN: Publicly? Who exactly was there?

HARRIET: Washington Post, CNN, New York Times, BBC, and three Chinese diplomats. Everyone heard it, everyone got it, two people gasped.

JEAN: Well, that’s not so bad.

HARRIET: Wow.

JEAN: It’s not! We can contain that. We all have ****-y mornings sometimes. My son has them every week.

HARRIET: Margaret wasn’t absent, she was in the room.

JEAN: Why didn’t he see her?

HARRIET: She was sitting.

JEAN: And therefore invisible?

HARRIET: He was standing, so the diplomats felt like it would be rude to sit, so they were all standing in front of her, blocking his view.

JEAN: He stood for the entirety of the meeting?

HARRIET: He can’t sit right now because of (pause) the thing on his . . .

JEAN: The abscess on his – right. I thought they were removing it.

HARRIET: They couldn’t because (Pg 4-5) he’s booked, Jean! His friend Jerry, from college, said he had the same thing and he should just rub tea tree oil on it.

JEAN: (Pg 6) I don’t want to know! (Pg 11) I’m going into the press room right now and (Pg 6) I’m trying to figure out if my biggest problem today will be explaining why the President of the United States used the word ***** to describe his wife to three diplomats – OR if there is something MORE awful I need to know about.

HARRIET: (Pg 11) (with a week cheer) Go get ‘em! Wooohhh!

JEAN: Oh, shut up . . .

MARGARET: (Pg 7) (seething) I’m gonna punt that man’s abscessed ass across the South Lawn and if you don’t get out of my way I will shred you like the sad cardigan you are.

HARRIET: (Pg 9-10) (blocking the door) He didn’t mean it. He’s in a lot of pain and it’s clouding his judgment.

MARGARET: Dammit, Harriet, you cannot prevent me from having a marital discussion with my husband!

HARRIET: I absolutely can, especially today, when he has a nuclear non-proliferation meeting, a gubernatorial candidate endorsement and an oozing pustule on his . . . I finally got him calmed down from your argument this morning

MARGARET: It wasn’t an argument

HARRIET: When you told him to stop behaving like his father, grow a pair and have the procedure without anesthesia?

MARGARET: I had two natural births and one root canal with no drugs, he can certainly

HARRIET: (Pg 57) Wait! I can’t hear the TV!

FROM THE TV: . . . President reportedly stormed out of the nuclear non-proliferation discussions after a fiery exchange with the Prime Minister of Bahrain.

HARRIET: No, no, no!

FROM THE TV: Sources within the White House say the President refused to sit for the duration of the negotiations, which the Prime Minister and several other world leaders interpreted as, quote ‘an aggressive power move.’ The Prime Minister says there will be, quote, ‘regretful consequences.’ ****** FLOTUS interview with CHRIS*****

MARGARET: (Pg 25-26) Well there is no typical, Chris. My daily work is determined by the ever-shifting needs of my five non-profits, two children, and of course, one and only president. The truth is, even before I was First Lady, after graduating from Stanford and then Harvard, I managed to keep busy with my law firm, my talk show, my book, my other book, my gallery and Taekwondo.

CHRIS: (joking) Why aren’t you president? (they both laugh for a moment then fall into silence) ****** In the Hallway*****

DUSTY: (Pg 28) (flags down Jean who is in a rush) Wait, hi, hi, I know you, you’re on TV!

JEAN: Ask one of the other interns . . . I can’t

DUSTY: Could you just point me towards the president? I’m Dusty. (Pg 18) I was told to be discreet. I’m here about the position. (she winks)

JEAN: (Pg 29) You’re meeting with Harriet? (struggling to comprehend) But you’re here to see the president?

DUSTY: He sent a private jet! I’m only here until tomorrow night and then I’m flying back to the farm.

JEAN: Hang on. . . The farm?

DUSTY: In Iowa.

JEAN: (with dawning horror) And you’re pregnant.

DUSTY: Eighteen weeks! Big as a bell pepper.

JEAN: (Pg 30-31) (to herself) What’s happening – how is this happening!

DUSTY: The president and I are in love . . .

JEAN: LOWER your voice, oh my god. SHUT UP!

DUSTY: (Pg 37) Ma’am, I’m going to need you to take a deep breath

JEAN: YOUR NAME IS AN ADJECTIVE: DON’T TELL ME WHAT TO DO!

HARRIET: (Pg 34) (entering) What the hell is going on here?

JEAN: (Pg 38-39) YOU are Chief of Staff. YOUR job is to contain situations. I’m the PRESS SECRETARY. MY job is to contain STORIES, and I can’t contain stories if I don’t KNOW the STIUATION, so perhaps you’d like to explain THIS SITUATION. (she motions to Dusty’s pregnant belly)

(The door to the interview room opens and CHRIS and MARGARET enter the hallway- Chris immediately turns on her phone to record)

MARGARET: (Pg 40) (regarding DUSTY) What is this?

HARRIET: (Pg 42) No, no, no, no . . .

MARGARET: If you think you can show up here, unannounced and blackmail the president

DUSTY: What? No, POTUS invited me. I’m here to celebrate our little president-to-be.

CHRIS: (Pg 14) (softly into her phone) I don’t need to stir shit up: we got a president throwing his feces at the wall.

JEAN: (Pg 42-43) Oh shit.

DUSTY: When I sent him a pic of the ultrasound he texted me that I should come in to celebrate.

HARRIET: Nope, that was me. POTUS is really busy, so you and I are just gonna have a quick little chat and

JEAN: (whispers to Harriet) Here . . . You’re doing this IN the White House?

HARRIET: (whispers to Jean) Where else am I gonna do it? A back alley? You don’t think that’d make her a bit suspicious? (to Dusty) Okay, honey, here’s the thing: as much fun as I’m sure you and the president had together.

DUSTY: We’re in love.

MARGARET: (cackles bitterly)

HARRIET: The thing is this pregnancy is not, um. Happening. (Pg 44) See, the way it works is we give you money and, in exchange, the pregnancy isn’t – it it it goes away. We’re talking about the President of the United States, right? The married president.

MARGARET: (cackles bitterly- to Harriet) (Pg 9) Your loyalty to my husband is admirable. I hope you continue to feel fulfilled by your choice to trade youth and beauty for a life of service to him.

HARRIET: (Pg 44) (ignoring Margaret) Do you see how that could make from some icky headlines?

CHRIS: (Pg 12) (into her phone) What a time to be alive, isn’t it! (suddenly everyone notices Chris who has been recording everything with her phone - Pandemonium ensues – a wild and epic chase)

MARGARET: (Pg 45-47) GET HER!

JEAN: I GOT HER PHONE!

HARRIET: DON’T LET HER LEAVE!

CHRIS: (grabs a bust from a pedestal in the hallway and raises it over her head) Give me my phone and get out of my way or I will break this into a million pieces

MARGARET: That is notable suffragist Alice Paul!

CHRIS: I will break her ugly face! . . . One . . . Two . . . Three

(she hurls the bust just as the office door opens. It sails through the doorway offstage. There is a thunk of the bust colliding with an unseen person’s head and the thud of a body hitting the floor. Silence – The women are frozen in shock sharing through the open door at the body on the ground)

DUSTY: (Pg 48) YOU KILLED HIM. YOU AND YOUR MEAN FRIENDS KILLED MY LOVE!

CHRIS: I’m going to go away for life. They’re going to send me to Guantanamo!

MARGARET: (Pg 50) Chris, stand up. Jean, go tell the secret service that the president is going to be a bit.

CHRIS: A bit? He’s going to be more than a bit.

MARGARET: Oh, I’m sorry, do you have a better idea? Because I though your contribution ended at death by discus!

HARRIET: Now, Jean, before we go down in history next to Booth and Oswald!

CHRIS: (Pg 52) This is a matter of national security! We need to notify the vice president right now.

MARGARET: That man is as useful in a crisis as a turnip.

CHRIS: Someone else, then. We murdered the president.

JEAN: You mean YOU murdered the president.

CHRIS: Don’t. You. Dare. If he was doing his job he would be across the White House right now making peace treaties! He should not be living in this house, he should not be running this nation and you know it! He’s the pyromaniac, but you gave him tmatches. You figured he’d burn his fingers and learn his lesson – Well he didn’t, and now the whole world is on fire! So we douse those flames, or we will burn in them together, but don’t think for one second I am marching to that stake by myself!

DUSTY: (inspired) Why isn’t SHE president?

JEAN: (launches the plan) (Pg 58-59) We can still contain this. Stay visible, don’t talk to each other. Then tonight, right when he’s supposed to be onstage for his speed, POTUS will be found with a suicide note in his hand. He was unwell. He can’t be responsible for his words, or his actions, he can’t be held to etiquette – he was sad!

HARRIET: (sobbing) It’s too much. I’m too tired

JEAN: This is what you do, Harry. You’ve done it for years. You clean up his messes, you make excuses, you do his job and then you wake up and do it all over again. But what if this is the last mess of his you ever have to clean? ****** Dream vision of Harriet, Jean and Margaret in control******

HARRIET: (Pg 61) (on the phone) What do you mean, “Why would Norway involve itself? Because that’s what allies do. You back us and in exchange we give you things that Norway needs, like peanut butter and genetic diversity . . .

JEAN: (addresses the press) Do I seem worried? No, like I said, the talks did not stall, they just broke for lunch. No, Eric, don’t speak until I call on you . . .

MARGARET: (Pg 67) (addressing the press) Which is why it is with great pride and joy that the president and I endorse Leslie Hopper as the next governor of . . . ****** Dream ends – back to reality******

JEAN: (Pg 77) We can’t just leave the body . . . What if something happens to it?

HARRIET: What’s he going to do – stand up and walk out? (a long loud moan from the president - the women scream)

MARGARET: (Pg 84) He’s awake! (long beat, then to audience) We told him he took too many pain meds, backed out and hit his head. Idiot totally bought it.

HARRIET and JEAN: *****! (beep can censor this expletive)
```

---

## IC-0667: Real Women Have Curves

- Title: Real Women Have Curves
- Author (byline): Josefina Lopez
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: Dec 1995
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SUGGESTED ROLES, ACTRESS 1, ACTRESS 2, PLAYWRIGHT, PLAYWRIGHT 2, ANA, CARMEN, PANCHA, ESTELA, ROSALI, CALLER, ESTELLA, SPOKEN TRANSITION - ACTRESS 1
- Teaser before the introduction: Yes
- Spoken words (computed): 1413
- Already set (do not supply): none

### Source block (context only)

```text
Author: Josefina Lopez
ISBN: 978-0871297259
Publisher: Dramatic Publishing
Date (Month/Year): Dec 1995
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Join us today in the small garment shop of Estela Garcia and maybe you’ll

understand TOGETHER: Real Women Have Curves by Josefina Lopez.
```

### Performance text (classify this)

```text
SUGGESTED ROLES:

ACTRESS 1: Playwright, Ana, Pancha, Rosali, Radio (Voice Over)

ACTRESS 2: Playwright 2, Carmen (Ana’s Mother), Estela (Ana’s Sister), Caller

PLAYWRIGHT: (Pg 6) In the US undocumented people are referred to as “illegal aliens”

PLAYWRIGHT 2: . . . which conjures up the image of extraterrestrial beings who are not human,

PLAYWRIGHT: who do not bleed when they’re cut, who do not cry when they feel pain,

PLAYWRIGHT 2: who do not have fears, dreams and hopes . . .

PLAYWRIGHT: Undocumented people have been (and still are) used as scapegoats for so many of the problems in the US, from drugs and violence to the economy.

PLAYWRIGHT 2: [We] hope that someday this country recognizes the very important contributions of undocumented people and remembers that they too came to this country in search of a better life.

NOTE: Words in Spanish are in bold print. A glossary of Spanish terms appears at the end of this selection

ANA: (Pg 10) (to audience as she writes in her journal) Monday, September 7 . . . I don’t want to be here! I only come because my mother practically drags me out of bed and into the car and into the factory . . . Is it selfish of me not to want to wake up every morning at 6:30 am, Saturdays included, to come work here for 67 dollars a week? Oh, but such is the life of a Chicana in the garment industry. Cheap labor . . . I can’t believe I’ve ended up here. I just graduated from high school. Most of my friends are in college. It’s as if I’m going backwards. I’m doing the work that mostly illegal aliens do. No . . . “undocumented workers” . . . or else it sounds like these people come from Mars. Soon I will have my Temporary Residence Card. Then after two years, my green card. I’m happy to finally be legal, but I thought things would be different.

CARMEN: (pounding on the door) Ana, open the door! Hurry! He’s following me! (Ana opens the door and Carmen hurries in nervously.) (Pg 14) I saw a van! La migra! (Ana quickly shuts the door and they hide, waiting to be discovered . . . after a few seconds)

PANCHA: Pero, why are we hiding? (Pg 15) Let those men in their van come! We’re all legal now! (the women begin their work shift, sewing, ironing. They talk as they work)

ESTELA: I’m not.

ANA: But you went with me to get the fingerprints and the medical examination.

ESTELA: I didn’t send them in. (Beat) I have a criminal record.

CARMEN: (Pg 16) Estela, what did you do?

ESTELA: I was arrested for illegal possession of . . .

PANCHA: A gun?!

ESTELA: A lobster . . . out of season! I almost got handcuffed and taken to jail. Trying to “abduct” a lobster is taken very seriously in Santa Monica. And I’m being sued for not keeping up with my payments on the machines. I thought I could make the monthly payments if everything went as planned.

CARMEN: Pos que paso?

ESTELA: (Pg 17) We never finish on time, so the Glitz company doesn’t pay until we do. We get behind, they don’t pay, and I can’t pay those pigs that sold me those machines. They’re taking me to court. . . And if I appear in court, they’ll find out that I don’t have any papers.

ANA: (Pg 22) How much do they pay us for making these dresses? (she holds one up)

ROSALI: Estela, we get thirteen dollars for these, no?

ANA: How much do they sell them for at the stores?

ESTELA: They sell them at Bloomingdale’s for about two hundred dollars.

ANA: Dang!

ESTELA: (Pg 32) Let’s get to work. A trabajar! (She turns on the radio) RADIO (VOICE OVER): (Pg 33-34) For those who just joined us today we are discussing abusive spouses. We have our last caller on the line.

CALLER: I want to know how I can talk to my husband when he gets angry.

RADIO (VOICE OVER): How long has he been abusive?

CALLER: He tells me if I did whatever he asked he wouldn’t have to hit me. But I do what he says and it’s still not good enough. Last time he hit me because . . .

CARMEN: Pobre mujer, I’m lucky mi viejo doesn’t hit me.

ANA: Lucky? That woman should leave her husband.

PANCHA: You think it’s that easy?

ANA: No, she’s probably dependent on him financially, or the church tells her to endure, or she’s doing it for the children. But we can’t allow ourselves to be abused anymore. We have to realize that we have rights! We have the right to control our bodies. No more!

CARMEN: (Pg 57) When your Apa would leave me in Mexico to go to el norte, he would leave me pregnant so no man would look at me and desire me. I was always scared of him. And I let myself get fat after you were born hoping he would be disgusted by me and not touch me anymore.

ANA: Why didn’t you just say “No.”?

CARMEN: Because, M’ija, I was never taught how to say no. (beat, change of subject) (Pg 12) give me your secret, Rosali. Maybe this way I can lose this ball of fat! (She squeezes her stomach) You can’t even see my waist anymore. (Ana laughs) Why do you laugh? You’re getting there yourself. When I was your age I wasn’t as fat as you. And look at your chichis! They must wight five pounds each! (Pg 58) Why don’t you lose weight? Young girls should try to make themselves as attractive as possible.

ANA: Why? You’re overweight too.

CARMEN: But I’m already married.

ANA: Is that it? Make myself attractive so I can catch a man?

ESTELA: (sarcastically) Ana, listen to them, learn now, “or you’ll end up like Estela.” (Pg 59) I want to be taken seriously, to be considered a person. With Andres, on our date . . . I got all fixed up. (twirls) He said, “I don’t care if you’re fat. I like you even better; more to grab.” That got me so angry! I though he was interested in me because he was impressed that I owned this factory. That “I’m smart” . . . When am I going to meet that man who will see the real me?

ROSALI: I’ve felt fat ever since I can remember.

ESTELA: Rosali, you’re not fat.

ROSALI: Of course, I am. Look at my nalgas . . .and my hips! I look like a cow. RADIO (VOICE OVER): (Pg 41) The time now is 2:35 pm. Twenty illegal aliens were captured today at the Goodnight Pillow Factory.

PANCHA: That’s only a few blocks away!

RADIO (VOICE OVER): The owner was fined up to 2,000 dollars per alien . . .

CARMEN: Estela, call the Glitz company and ask them, no, demand that they pay you for the last order of dresses. Even if they were late, they still have to pay us.

ESTELA: I don’t want to be too pushy. They’re the only company that has been willing to give us a contract.

CARMEN: Then do it for Pancha and Rosali. You haven’t paid them and las pobrecitas can’t even buy groceries.

ESTELLA: (She thinks about it, then decides to be brave and do it) (Pg 42) Hello, this is Estela Garcia . . . No, but we’re almost finished. I know . . . I know. . . I’ve got a lawyer working on that . . . I’ll get it to you by next week . . . Okay, Mrs. Glitz . . . I’m sorry. (she hangs up, her face expresses worry and fear)

CARMEN: Que te dijo la vieja?

ESTELA: She asked about my proof of employment papers again. She warned me that if la migra shuts us down, she won’t pay us for all the work we’ve done. I’m going to get deported. I’ll lose everything I’ve worked for, the factory . . . my self-respect.

PANCHA: (Pg 56) How many more dresses to finish, Estela?

ESTELA: Fifteen (counting dresses on the rack) 184, 185, 186. We only need 14.

CARMEN: (Pg 61) (and suddenly Carmen has a idea) Estela, I’ve been thinking . . You know what we could do? We could copy the patterns for these dresses and make the dresses for ourselves.

ROSALI: Jaime could sell them in the flea market!

ANA: That’s a great idea! Why don’t we make them in larger sizes too?

PANCHA: We could probably sell more if we made them in larger sizes.

ESTELA: And from there, if we make more money than what we’re making now, maybe we can rent a place downtown and start a boutique!

PANCHA: You could go to school and study fashion design and design our dresses!

ESTELA: I could do that . . . (She grins) (Pg 64) Large sizes?! (she picks up a measuring tape and begins taking her own measurements)

SPOKEN TRANSITION - ACTRESS 1: The women head home for the day, but not Estela – She works through the night – and the next day . . .

ESTELLA: (Pg 67-68) (with new-found determination she dials the phone) Mrs. Glitz? This is Estela Garcia. I wanted to tell you that you are a mean, wicked, unsympathetic, greedy, rude. . . Capitalist! We quit . . .

CARMEN: What have you done?

PANCHA: You got us fired, didn’t you?

ESTELA: No, we quit! (Estela laughs) Don’t worry. I got us a contract with Senor Vasquez!

ANA: (Pg 69) (steps out of scene to speak to audience) As for me . . . I wrote an essay on my experience and was awarded a fellowship to New York University! (beat) I always took their work for granted. I was going to be better than them. I wanted to show them how much smarter and liberated I was. But in their subtle ways, they taught me about resistance. About a battle no one was fighting for them except themselves. About the loneliness of being women in a country that looks down on us for being mothers and submissive wives. With their work that seems simple and unimportant, they are fighting…

Perhaps the greatest thing I learned from them is that women are powerful, especially when working together. [When I came back from school] plans for making the boutique were no longer a dream, but a reality. (She picks up a jacket and puts it on) Now I wear original designs from Estela Garcia’s boutique, “Real Women Have Curves.”
```

---

## IC-0668: Roe

- Title: Roe
- Author (byline): Lisa Loomer
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Sept 2019
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SARAH, LINDA, FLOWERS, FLIP BENHAM, RONDA, NORMA, AILEEN, JUDY, DOCTOR, TOGETHER, MCCLUSKEY, JUSTICE BLACKMUN, NORMA AND SARAH, PRO-LIFE WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1803
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lisa Loomer
ISBN: 978-0822238010
Publisher: Dramatists Play Service
Date (Month/Year): Sept 2019
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 2: Roe v Wade is not just a case. It’s not just a ruling.

ACTRESS 1: This is what happens when a country argues over who gets to choose and who must pay the price.

TOGETHER: Roe by Lisa Loomer
```

### Performance text (classify this)

```text
Suggested Roles: Actress 1: Sarah, Flowers, Ronda, Aileen, Doctor, McCluskey, Flip

Actress 2: Linda, Flip, Norma, Judy, Justice Blackmun, Pro-Life Woman

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

SARAH: (Pgs 11-13) (Lights come up on Sarah Weddington, early 70s) Good evening. My name is Sarah Weddington. I was the lawyer who argued Roe v. Wade. (From Loomer’s revised Prologue 2022) And tonight, I deliver its obituary. (with great passion) Every day new abortion laws are written in our country. But all of these laws tell a woman the same thing: You have no right to control over your own body. We, the government, have that right. We have the right to cause you economic or psychological harm . . . We will incarcerate any doctor who seeks to help you . . . And we don't care if you were incested or raped. (pained) You know, I always wonder . . . We argue about Roe, some of us vote solely on this issue . . . But how many of us even know what was said in the case? Well, I'd like to tell you the story of Roe. And since history is the result of shared experience. . . And is a reflection of multiple points of view -- that are affected by race, religion, gender, sexuality, and class . . . I think it's essential that all persons involved in Roe be here to testify!

LINDA: (passionately) Linda Coffee for the plaintiff -- the truth is, it's about choice!

FLOWERS: (outraged) Robert Flowers, representing the great State of Texas -- it's about murder pure and simple-

FLIP BENHAM: Flip Benham, head of Operation Rescue -- the truth is, it's not your body, so it's not your choice!

RONDA: Can you see the little hands, the precious feet? Suddenly, the one woman who has not spoken, lets out a whistle, and the others fall silent. Norma, 69, steps forward to the audience.

NORMA: Hey, y'all, I'm Norma McCorvey. I was the plaintiff. I Am Roe! (Sarah looks at Norma. Norma looks at Sarah and smiles) Well, sugar, how 'bout this? How 'bout you tell your story, I tell mine?

SARAH: (after a beat; with dignity) Norma? As long as we get to the truth? Fine.

NORMA: (Pg 14-15) Okay y’all, Dallas, 1970. I was a bartender at the Red Devil – Oh – did I mention this was a Girls’ Bar? (begins to serve drinks to a woman sitting at the bar) Aileen!

AILEEN: You seen your doctor?

NORMA: Know what that doctor told me? “See a lawyer.” Adoption lawyer. [But] I was workin’ the bar tonight, talkin’ to a customer, know what she told me? Did you know there is a way for me to be not pregnant, Aileen?

AILEEN: (laughs) You never heard of an abortion?

NORMA: Where I come from? Louisiana? A voodoo woman gives you something to drink, says some mumbo jumbo . . . didn’t work when my mom got knocked up with me, so how would I know? Can you give me the name of a doctor?

AILEEN: Not that kind of doctor. It’s against the law.

NORMA: You’re a nurse, Aileen – All I’m askin’ for’s a name! (steps out of scene to speak to the audience) (Pg 16) And while I was raisin’ hell in Dallas . . .

SARAH: In Austin . . .

JUDY: (Pg 19) Sarah has been doing legal research for an underground referral service so women can get safe abortions and steer clear of the back-alley guys.

SARAH: We’ve all heard the horror stories about illegal abortion. 5,000 women dying a year!

JUDY: We all agree the law has to change. And in order to do that in Texas, someone has to challenge the law that makes abortion illegal. I think that should be Sarah.

SARAH: Are you crazy? I’m only a couple years out of law school! I’ve never tried a contested case!

NORMA: (Pg 37) (interjects from the sidelines) Your first case? Gee, no one bother to tell me!

SARAH: (Pg 20-21) (beat) Look, I know you’re right, Judy, someone should do this . . . (with increasing emotion) I met a girl last week. Willa. Fifteen. She took a bus to Dallas, was met by a guy who blindfolder her and drove her to a man who did abortions in his basement. $800 at the door. He ordered her to take off all her clothes and lie down on a table. (beat) He raped her. And she felt that, if she wanted the abortion, she’d better just let him. She was fifteen! No anesthesia. He inserted a coat hanger, jabbing it around till he pierced the fetal sack. (continues with passion) And some women just do it themselves! Lysol, turpentine, telephone wire, broken Coke bottles. No woman should have to go through these things!

JUDY: You just argued yourself into taking the case. ***** Doctor’s Office*****

NORMA: Look, I been to a place in Oak Cliff. Blood all over the floor, roaches . . . And the smell.

DOCTOR: (patiently) Norma, I believe I told you “no” on the phone.

NORMA: You delivered both my babies, you had plenty of business offa me. If you can’t do it, gimme the name of someone who can.

DOCTOR: Maybe you should have thought about consequences before you got pregnant for a third time? I am not in the business of killing babies! Shame on you for even – do you understand that any doctor who would do such a thing would go to jail? Either raise this baby yourself (with disdain) as an unmarried woman or find your child some decent parents. **** Pizza Parlor *****

TOGETHER: (Pg 24-27) (to audience) And the first meeting on Roe v Wade took place in Columbo’s Pizza Parlor on Mockingbird Lane.

NORMA: in Dallas.

SARAH: (to audience) Linda Coffee was in my class at law school, and I knew I’d need a huge amount of help. (greeting Norma) Hi! You must be Norma! I’m Sarah Weddington. So glad to meet you! (she notices the bandanna wrapped above one of Norma’s knees) I like your bandanna.

NORMA: Oh, that just means I don’t have a girlfriend. (enjoying this) I’m a lesbian?

SARAH: Of course. How many months pregnant are you, Norma?

NORMA: Uh, ‘bout two and a half?

LINDA: (steps out of scene) I’d just like to say something about “history” here. We want to give a fair account of what happened here. Norma, in her book, says she was 2 ½ months pregnant. And Sarah, in your book, it was more like 4 . . . Well, how pregnant was she?

SARAH: You were at least 4 months –

NORMA: 2 Months! (to audience) Alternative facts –

LINDA: (to audience) My point is that it’s really hard to talk objectively about history, about the “truth.” Let’s continue.

SARAH: (Pg 28) Do you have family?

NORMA: Got a mother! But we never been close (laughs) Hell, I though my name was “Ugly Stupid” ‘fore I knew what the wors meant. I still can’t do nothin’ right for that woman. And I tried ‘cause she’s got my daughter –

SARAH: You have – a daughter?

NORMA: Melissa. She’s five.

SARAH: I see. And you say your mother has custody?

NORMA: I say my mother stole Melissa. Told me she was gonna put my baby on her health insurance. Next thing I know: “You got five minutes to pack up your shit ‘cause you just gave up your daughter.” (awkward pause)

SARAH: (Pg 30) We need a pregnant woman who wants an abortion to challenge the Texas Law. Do you want an abortion, Norma?

NORMA: Well, yeah! I’m not here for the pizza!

SARAH: You wouldn’t have to use your own name. Usually, people use “Jane Doe” but there’s a Mary Doe in a related case, we could use . . . Jane Roe? You wouldn’t even have to appear in court.

NORMA: So I’m Jane Roe? And then I could get my abortion?

SARAH: (beat, carefully) Norma. The law takes time I can only promise you that we will do our best. (both step out of scene and speak the audience)

NORMA: (Pg 32) She let me believe I could get my abortion.

SARAH: Norma McCorvey was in her second trimester when we met. She became a plaintiff in the case so that future generations of women would have the right she was denied. (Norma starts to pound her very pregnant stomach)

MCCLUSKEY: (Pg 33) (to audience) Despite her efforts to self-abort, Norma gave birth that summer. (Pg 22) [I’m] Henry McCluskey, a lawyer who specialized in adoptions and, like Norma, also gay. People like us generally hid their sexual orientation in those days.

NORMA: (Pg 34) (deadened; to no one) They gave me a shot to dry up my milk. But the nurse f***ed up and brought it to me at feeding time. (pained she turns away)

MCCLUSKEY: (taking the baby in his arms) I arranged the adoption – a closed adoption. No one’s heard anything about the child known as the Roe Baby since. (beat) Oh – it was a girl. *******

SARAH: (Pg 41) (to audience) Finally . . . October 1972 – (Pg 46) the *Supreme Court* sent the decision. . .

JUSTICE BLACKMUN: (Pg 49) (to audience) Justice Harry Blackmun. According to my obituary, I would receive hate mail for the rest of my life. (Pg 48) (turns to the order at hand – the Supreme Court’s ruling) The Court has recognized that a right of privacy does exist under the Constitution. And is broad enough to encompass a woman’s decision whether or not to terminate her pregnancy.

SARAH: (reading the ruling in her office) Yes!

JUSTICE BLACKMUN: Each state may also properly assert important interests in protecting potential life.

SARAH: (to Blackmun) To be clear . . . the fetus is “potential” life?

JUSTICE BLACKMUN: The compelling point is viability. When the fetus has the capability of life outside the mother’s womb. The state may prohibit abortion, from the second trimester on except when it is necessary . .

SARAH: (reading) “To preserve the life or health of the mother.” (To Blackmun) Damn! State regulation could be a big problem in the future!

JUSTICE BLACKMUN: The word “person,” as used in the 14th Amendment, dos not include the unborn. (exits)

NORMA: (Pg 49) (with wonder) They passed that law – that Roe versus Wade?

NORMA AND SARAH: (Norma speaks it to herself, Sarah aloud) The right to choose is the law of the land!

SARAH: (to audience, triumphant) And that was the case. Now let’s talk about what’s happened to the law since. (Pg 50) The 80s – Reagan says he wants to “rectify the tragedy of Roe v Wade.” He says that, over his dead body will a pro-choice Judge ever be appointed to the Supreme Court.

NORMA: (Pg 51) I see all them college-girl feminists on the TV going on about Roe? I mean, shit I am Roe – and I never got nothin’ out of it, not an abortion, nothing’!

FLIP BENHAM: (Pg 56) (to audience) Flip Benham, Head of Operation Rescue. (turns to confront Norma) (Pg 66) Norma McCorvey? How does it make you feel that 35 million babies have died because of you? (Pg 67) Only sin will prevent you from entering the Kingdom of God, Miss Norma.

NORMA: That what you Rescuers told that abortion doctor in Florda ‘fore you put a bullet in his head.

RONDA: (Pg 68-69) (outside an abortion clinic, perhaps holding a picket sign; introduces herself to audience) Ronda Mackey – Operation Rescue volunteer. (steps in front of a woman headed to an abortion clinic) Oh, hon, you don’t want to go in there. Let me show you something (shows photos) This is a 9-week-old baby. He’s smiling, can you see that. (vehemently) No one could tell me that this was a “fetus” and not a human being. Hon. . . Your child is a gift! *******

SARAH: (Pg 70) Decades ago, the Supreme Court gave American women the legal right to choose. But the fate of Roe depends on who is on the Supreme Court at the time.

PRO-LIFE WOMAN: (Pg 89) You liberals – the same folks who stood in front of schools to protest segregation, to protect the rights of black children? Can’t you see where’ standing in front of clinics to protect the rights of all babies.

SARAH: If abortion goes against your beliefs, don’t have one! Just don’t try to force your beliefs – and your choice – on everyone else.

PRO-LIFE WOMAN: (Pg 90) A child is not a choice!

SARAH: (Pg 94-95) In 2016, a pro-choice woman ran for president. Won the popular vote. . . and lost the election. In 2018, a president who’s vowed to overturn Roe made his second appointment to the Supreme Court.

NORMA AND SARAH: No matter what else I have done with my life . . . My obituary will always read

SARAH: (Proud) She was the lawyer who argued Roe v Wade!

NORMA: (Broken) She was Jane Roe.

SARAH: As for the law itself? . . . . CLOSING

TOGETHER: On June 24, 2022, the U.S. Supreme Court eliminated the constitutional right to obtain an abortion -- casting aside 49 years of precedent that began with Roe v. Wade.
```

---

## IC-0669: The Role of Della

- Title: The Role of Della
- Author (byline): John Wooten
- Work: Plays for Actresses
- Publisher: Vintage Books
- Publication date as stated: March 1997
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ELIZABETH, EMMA, WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1327
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Wooten
Book: Plays for Actresses
ISBN: 978-0679772811
Publisher: Vintage Books
Date (Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: An acting audition can cause a lot of stress for aspiring actors and actresses. Finding a good acting audition can be hard enough, getting invited to an audition is even harder, and the actual act of auditioning for the role is sometimes the biggest moment of an actor’s life. So here are some tips:

ACTRESS 2: The judges will look into more than just your facial expressions. Basics, such as, were you on time? Did you show an extravagant personality when you were walking into the room? Make them remember your name!

ACTRESS 1: Use your own creativity to do this (be professional, don’t go crazy), but there’s something to be said about making a lasting impression on someone. If it’s close between you and another star actor or actress then it could be your ace in the hole.

ACTRESS 2: Make sure you follow direction well. You will be so focused on your own monologue or whatever you have to do for your audition that you might forget an important factor. Listen to your casting director during your acting audition!

ACTRESS 1: As long as you are sure your casting director is REALLY a casting director. (with a look at Actress 2)

TOGETHER: The Role of Della by John Wooten
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Lights up on an audition studio. EMMA stands in front if a table. She carefully examines a few head shots, which are spread about the table. She notices one if interest and slowly sits down in a chair in front if the table. ELIZABETH slowly sticks her head into the room.

ELIZABETH: Excuse me. (Startled, Emma quickly puts the head shot on the table. She begins to rise.) No, don't get up. I'm a little early. There was no monitor out front.

I saw the door open. I didn't know if I should come straight in ... or if I should wait ... I'll come back in a few minutes. (Starts out)

EMMA: Do you have your audition card?

ELIZABETH: Oh, yeah. (With a smile.) I wouldn't lose this. I had to get here at 6 A.M. to wait in line and I still barely got a slot. Some girl offered me fifty dollars for this card. Just for a chance to audition. It's like a zoo out there.

EMMA: Hand it to me, please.

ELIZABETH: Sure. (She crosses to her. Offers hand.) I must say it's a great pleasure to meet you, Ms. Stewart. I've heard great things about your theatre.

EMMA: (Shakes hand.) Thank you. The card.

ELIZABETH: Oh, right. (She hands Emma the audition card.) Sorry. Just a little nervous.

EMMA: That's all right. I understand.

ELIZABETH: John Wyatt says hello.

EMMA: Really.

ELIZABETH: He's doing great. He just booked ...

EMMA: Do you have a head shot and resume?

ELIZABETH: Of course. (She hands EMMA her resume.)

EMMA: (Takes a moment, looks at the headshot.) No, I need your headshot. (ELIZABETH laughs.) Is something funny?

ELIZABETH: I don't understand.

EMMA: (Deliberately slow.) I need your headshot.

ELIZABETH: This is my headshot.

EMMA: No.

ELIZABETH: Yes, that's me.

EMMA: Really? You've gained a few pounds since this picture was taken, haven't you?

ELIZABETH: I beg your pardon?

EMMA: What role are you interested in?

ELIZABETH: Della.

EMMA: Della? Really? The young ingenue?

ELIZABETH: (A beat.) Yes.

EMMA: (Chuckles to herself.) Okay. Why not. What piece are you doing?

ELIZABETH: Uh ... Today, I

EMMA: Can you move back a little, please?

ELIZABETH: Sure. Sorry. (She moves back, away from table.) Good morning. My name is Elizabeth Ryan. Today, I will be doing a selection from ...

EMMA: Just do the monologue.

ELIZABETH: Right.

EMMA: You only have two minutes, you know?

ELIZABETH: Yes. (She turns and takes a breath. She turns back around, and begins.) "Oh, we would get into terrible arguments, my mother and I."

EMMA: Do I have something on my face?

ELIZABETH: Pardon?

EMMA: Why are you looking at me?

ELIZABETH: Is it okay if I direct my piece to you?

EMMA: What do you think?

ELIZABETH: (Begins again, awkwardly directing piece to chair.) "Once, when I was twelve or thirteen, I told her that God was a moronic fairy tale-I think I'd spent an entire night ... "

EMMA: Do you have anything else?

ELIZABETH: Excuse me?

EMMA: Do you have another monologue? (ELIZABETH looks confused.) Anything? ... I've already heard that twice today.

ELIZABETH: Really?

EMMA: Yes, and I was glad Agnes killed the baby.

ELIZABETH: (Taken aback.) I'm sorry. If you'd like to give me a direction with it, I'd be happy to ...

EMMA: This is not an acting class, Elizabeth. Besides, what you need is an interpretation class. Agnes of God is not a melodrama.

ELIZABETH: No, of course not. I wasn't trying to ...

EMMA: Don't make excuses. Just do something else.

ELIZABETH: I don't have anything else prepared. I thought that piece was appropriate.

EMMA: Actors do not think, Beth. They act. Those who think, think. Those who act, act. Those who think they can act, spend more time thinking than acting.

ELIZABETH: Of course. Can I please try again?

EMMA: No. Tell me a story ... Something funny.

ELIZABETH: Funny?

EMMA: Yes. Make me laugh.

ELIZABETH: Just like that?

EMMA: You want this job, don't you? You want to play Della?

ELIZABETH: Of course.

EMMA: Then make me laugh. Are you an actress or aren't you?

ELIZABETH: Okay ... Let's see ... When I was a little girl, my friend Carol and I found this old doll's house in her attic. We sneaked it carefully downstairs and cleaned it off. Carol had a pet mouse, Binkey. So we dressed Binkey up in this white Barbie dress and ...

EMMA: (Ignoring her.) So, I see here that you've listed Sandy in Grease as one of your credits.

ELIZABETH: Oh, yes. It was a great experience. Working with Paul Jones. Do you know him?

EMMA: Didn't anyone ever tell you not to lie on your resume?

ELIZABETH: I didn't.

EMMA: Oh, come now.

ELIZABETH: I didn't. I swear I didn't.

EMMA: There's no character listing here by The Glass Menagerie. Was it done in the absurdist style or did you play the gentleman caller?

ELIZABETH: I played Laura.

EMMA: That must have been some time ago.

ELIZABETH: Last summer.

EMMA: I'm sorry, I didn't mean to interrupt your little story.

ELIZABETH: That's okay ... Uh, where was I ... So, after we dressed Binkey up in the Barbie costume, we placed him inside the doll house and he crawled right into the miniature bathroom as if he wanted to take a bath ...

EMMA: Add a Southern accent.

ELIZABETH: (Adding a Southern accent.) ... Then he got stuck in the miniature hall closet and we had to shake the doll house up and down and then Binkey popped out but he was all hyper and we couldn't catch him so he ran downstairs and Carol's mom was having this big ritzy dinner party and Binkey ran right at ...

EMMA: Let's see a little Spanish.

ELIZABETH: ... la grande jefe de mi madre, pero cuando la senorita jefe ...

EMMA: No. I don't want Spanish dialogue. I want a Spanish accent. Comprende?

ELIZABETH: Oh ... I can't do a Spanish accent.

EMMA: Then at least show me you have some energy ... Act the story out.

ELIZABETH: (A beat. Elizabeth proceeds to act out everything she says.) So, Carol's mother's boss screamed, leaped up onto the couch and pulled up her dress. Well, she wasn't wearing underwear ...

EMMA: Faster.

ELIZABETH: ... Then Carol's mother's boss's husband tried to grab her but instead he knocked her off into the double salsa sour cream dip and ...

EMMA: Faster!

ELIZABETH: ... and Binkey got scared and ran out into the front yard and the whole party went outside to look for him except Carol's mother's boss's husband and Carol's mother's boss who was crying, not because of the double salsa dip or even the flashing incident.

EMMA: No words!

ELIZABETH: Pardon?

EMMA: No words. (Completely enthralled in the story, Elizabeth then acts out the rest of the story without words. This includes a chase scene, fainting, a cat, a dog, maybe even death. Elizabeth finishes with a loud laugh. She can't help but applaud herself.)

EMMA: (A beat. Dryly.) Couldn't think of anything funny, huh?

ELIZABETH: (A long beat. On the verge of tears) Why are you being so rude to me.

EMMA: (Innocently.) Rude. Am I being rude? I'm sorry, Elizabeth. Please continue your quaint little rodent story.

ELIZABETH: I don't want to. I'm leaving.

EMMA: Leaving. You sure? You still have a few seconds left.

ELIZABETH: If you didn't think I was right for the role you should have just said so.

EMMA: Right? You're perfect. I just wanted to make sure you could handle all the terrible things Della must endure.

ELIZABETH: Really?

EMMA: Sure.

ELIZABETH: And?

EMMA: There is no doubt in my mind that you think you would be perfect for this role. I don't think I've ever seen an actress quite like you before.

ELIZABETH: Thank you!

EMMA: But out of fairness I have to finish out the day. I'll call you tomorrow. Mind you, it will be late. Between midnight and 4 A.M. Make sure you're awake and by the phone. If you don't pick up after the first ring, I'll offer Della to someone else.

ELIZABETH: Don't worry. I won't sleep a wink.

EMMA: Good.

ELIZABETH: Anything I should know about the character? Keep in mind?

EMMA: Leave the wig at home. It doesn't fit.

ELIZABETH: Wig?

EMMA: And learn a Spanish accent and combine it with the Southern. You can talk faster too.

ELIZABETH: Even faster?

EMMA: Pace is everything.

ELIZABETH: Okay. I'll work on it tonight.

EMMA: Alright. Run along now. I'll be in touch ... (ELIZABETH smiles and turns to go.) Wait! Your number is 555-8798?

ELIZABETH: Yes.

EMMA: Just wanted to make sure.

ELIZABETH: Thank you. Thank you so much!

EMMA: No, thank you. (ELIZABETH exits. EMMA watches her off. She picks up ELIZABETH's head shot, crosses to the waste basket and throws the head shot away, giggling to herself. A woman enters with coffee and takeout bag.)

SCENE

WOMAN: Hi, can I help you?

EMMA: (Startled.) Yes. (A wide-eyed smile suddenly appears.) Hi, I'm a little early. I saw the door open. Should I wait outside? ... I'll wait outside.

WOMAN: No, that's okay. Do you have your audition card?

EMMA: Yes. (Hands her ELIZABETH’S card.) Here you go ... I must say it's a pleasure to meet you, Ms. Stewart. I've heard great things about your theatre.

WOMAN: Well, thank you. We try.

EMMA: (Trying to be sincere.) John Wyatt says hello.

WOMAN: John! How is he?

EMMA: Great.

WOMAN: Do you have a picture for me?

EMMA: Sure do. (Crosses to bag and pulls out her resume.)

WOMAN: It's like a zoo out there.

EMMA: I know. I had to get here at 6 A.M. just to get an audition card. I didn't think I was going to get to see you. (Elizabeth hands the woman her resume.)

WOMAN: What piece are you doing?

EMMA: A short selection from Agnes of God.

WOMAN: (Smiles.) In that case, you better move back a few steps.

EMMA: Of course. (Emma backs up.) Good morning. My name is Emma Winns.

WOMAN: Wait ... Uh, what role would you like to be considered for, Emma?

EMMA: (A beat.) Della.
```

---

## IC-0670: Rosemary with Ginger

- Title: Rosemary with Ginger
- Author (byline): Edward Allen Baker
- Work: EST Marathon 1994: One-Act Plays (p 1-21)
- Publisher: Smith and Kraus
- Publication date as stated: Jan 1995
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GINGER, ROSEMARY
- Teaser before the introduction: Yes
- Spoken words (computed): 1773
- Already set (do not supply): none

### Source block (context only)

```text
Author: Edward Allen Baker
Book: EST Marathon 1994: One-Act Plays (p 1-21)
ISBN: 978-1880399835
Publisher: Smith and Kraus
Date (Month/Year): Jan 1995
```

### Introduction (context only: never use it for content warnings)

```text
GINGER (in character): . . . . (To audience) Hi, I’m Ginger and that’s my sister . . . Rosemary .

(praying) I have a confession to make before I let her in, God. I don’t know sometimes why I keep trying. But she is my sister and in spite of everything, I do love her. I suppose I should just be glad that she came tonight at all. Maybe this one time we can work together to accomplish something good for a change. Please, God, bring us together tonight. I need a family and I know Rosemary does. Lord, God . . Give me strength and patience and well, LOTS of patience.

(To audience) Rosemary with Ginger by Edward Allen Baker
```

### Performance text (classify this)

```text
GINGER: ...cause we're closed...for good...don't matta since when...Mrs. Guertin, listen to me...I can't give you the soup-of-the-day cause there is none...that's right...so you have to stop callin’ an...no-no I'm not foolin’ you...I'm here just cleanin’ up an... (Knocking heard on the front door. Ginger turns to look.) Uh, listen Mrs. Guertin you take care a yaself...I will uh-huh bye... (Ginger hangs up and proceeds to the door.)

GINGER: (She turns the clump of keys and lets in Rosemary.) Where you been?

ROSEMARY: You gotta be outta your mind still bein’ here...

GINGER: You been drinkin, haven't you? I can smell the blackberry brandy, Rose...

ROSEMARY: Listen.

GINGER: I don't wanna listen if you're on one of your drinkin’ binges an...

ROSEMARY: Yeah well... Me and Raymond the oran-ga-tan man got into this big fight an he's like screamin in my face not lettin’ me talk so he goes like "yeah well you're outta here!" So I busted every mirra in the house...

GINGER: Really if you don't wanna do this with me then...

ROSEMARY: I'm here! (beat) I'm here...

GINGER: I thought we should do somethin’ for Ma, yunno, cause lately she's been gettin depressed an nothin goes good for her...then there's you.

(Rosemary picks up a piece of paper from the table and reads.)

ROSEMARY: "Unsung Mother of the Month Award."

GINGER: If she wins they'll give her a five hundred dollar gift certificate to the Shoppers World.

ROSEMARY: You do most of the writin’ it, I'm just hidin’ from the oranga-tan man whose gotta be losin his mind about now with no mirras an I flushed his diet pills down the toilet an just for the hell of it I beat the crap outta his mailbox!

GINGER: (beat) So you did drop outta A-A...

ROSEMARY: People with their sob stories an-an everybody wants to hug an hug an pray an pray, it's like my worst nightmare. Rememba when Dad used to say-there's nothin worse than bein around reformed drunks?

GINGER: You're just like 'im, it's unbelievable.

ROSEMARY: An that's bad?

GINGER: Yeah he's dead.

ROSEMARY: Oh cut it out, will ya?

GINGER: How soon you forget the horrors you went through an how you almost died an how you couldn't stop throwin up, Jesus Rose!

ROSEMARY: It's unda control... (drinks) An I don't want to talk about it. (finishes drink)

GINGER: (looks down to paper) Let’s start this thing...

ROSEMARY: You still on the couch?

GINGER: YES I'm still on the couch!

ROSEMARY: I woulda thrown him out if it was...

GINGER: I got three kids an no money an nowheres to go so what am I gonna do?

ROSEMARY: I'd sleep in a shelter before I'd...

GINGER: I put it past me cause...I-I have to, okay? I can't leave him right now. You haven't told anybody, have you?

ROSEMARY: Nobody would believe it so why bother. Look, sorry I brought it up.

GINGER: I hate it when you drink, I really do. You get that look in your eyes that's nothin but trouble. Me an Harry got a problem an I made the big mistake a tellin you an then you think you can throw it up in my face anytime you want-withwith that smirk that goes with it! We're gonna deal with it when...when we can an which is more than you're doin...

ROSEMARY: I deal.

GINGER: Yeah yeah right yeah you deal...

ROSEMARY: I do. I don't let nothin slide.

GINGER: Yeah dealin for you is bustin mirras in your boyfriend's house an-an back to drinkin afta almost dyin and fightin with your first husband an his new wife over the kids that you... (Stops short. Beat beat.)

ROSEMARY: That I what?

GINGER: That you yunno just...just not bein stable somewhere, I don't know...

ROSEMARY: I love my kids. You sayin I don't love my kids?

GINGER: I would never say that, god...

ROSEMARY: Never?

GINGER: No! You got that look on your face again.

ROSEMARY: You tell the truth, don't you? Like you an Brad havin a little talk about Rosemary. (Rosemary pulls out an official-looking letter from her pocketbook.)

GINGER: I . . .we...

ROSEMARY: I woke up this mornin to a sheriff servin me with an affidavit from Brad (looking at the letter) Um... "an my ex-sista in law Ginger Willis is in agreement with my decision to pursue custody of the children. In our phone conversations she agrees with me that the children's safety and well-being is in danger if my exwife is drinking."

GINGER: Oh god....

ROSEMARY: "...my ex-sista-in-law spoke at length of Rosemary's past drinkin’ problems stating to me that her sister's mental condition has gotten worse since being with Raymond Perretti, her live-in boyfriend who owns the nightclub Memories and likes to drink and party..."

GINGER: Rose, he's really worried an-an.... He called an I...

ROSEMARY: I'm outta here....

GINGER: Listen to me Rose. Rosemary look at me! I...Brad called me an we talked or he did most a the talkin an I don't know what you got in your head about it but it was...he talked about a temporary custody thing an wondrin when you're gonna get help. I-I think he is really worried, uh I don't think he's tryin to be mean or anyway...um... (Pause.)

ROSEMARY: I...I...keep hearin...my my kids' voices...

GINGER: I know...

ROSEMARY: "Mommy, where are we goin?" "Mommy, why are you drivin so fast?" "Mommy, please don't drive so fast."

GINGER: Rose...

ROSEMARY: “Just be quiet an-an Laurie make sure your seat belt is on tight... "

GINGER: What are you?

ROSEMARY: "Mommy, it's scary...you're scarin me..." "mommy, why'd you take us outta school, mommy please we want daddy..."

GINGER: This happened?

ROSEMARY: "We're goin to Rocky Point Cliffs kids. Daddy says I never do any thin with you kids so we're going to Rocky Point Cliffs an look out over the ocean, okay?"

GINGER: (nervously) When did this happen?

ROSEMARY: "Even Auntie Ginger says I'm not a good mother."

GINGER: What are you talkin about?!

ROSEMARY: "But mommy we go to school today, we got masks to make for Halloween an...mommy bring us back!"

GINGER: Are they in the car?! (Ginger runs to the window and looks out.)

ROSEMARY: "You sit down Laurie! I am your mother so you listen to me, now sit before I.."

GINGER: Stop it Rose!

ROSEMARY: "I am your mother. I am your mother..."

GINGER: You stop it goddamn it!

ROSEMARY: "It's too windy up here mommy...the water is so...is so gray..."

(Ginger grabs a coin from the counter then runs to the payphone.) "I'm your mother, kids...don't be afraid of me, no need to be afraid of me..." (Ginger is dialing.) "Just look out, okay, not down...look straight out."

GINGER: (on phone) C'mon, pick up, pick up...

ROSEMARY: "Okay, now hold hands kids...an-an I'm gonna step over here..."

GINGER: Hello! Brad!

ROSEMARY: "...cause I wanna take your piture..."

GINGER: Listen, where are the kids?

ROSEMARY: "Laurie...step back hon...you're still too close to mommy..."

GINGER: Call the school then call me at the diner! (hangs up the phone)

ROSEMARY: "...now c'mon back up for your mother...I want the best picture I can get to show people my kids..."

GINGER: You cut it out Rose!

ROSEMARY: "Nice one, now I want ya to turn around so I get a picture a you both lookin out over the ocean..."

GINGER: I never said those things!

ROSEMARY: "I'm gettin closer okay, but don't turn around an look at me..."

GINGER: He just put that stuff in there!

ROSEMARY: "Laurie, don't look at Mommy I said!" (Ginger turns to face the phone.)

GINGER: Please god no don't let this happen oh god, oh god I....

ROSEMARY: "I'm right behind you now don't move an don't look back 'an"

(Phone rings. Ginger gets it.)

GINGER: Yeah!

ROSEMARY: "Here we go, ready?"

GINGER: (listens, calmer) Okay, yeah nothin I... (Ginger turns to look at Rosemary. Rosemary picks up her drink and drinks.)

ROSEMARY: Ah, that hit the spot...

GINGER: (on phone) ...sure bye... (to Rosemary) I don't believe what you just did!

ROSEMARY: You're helpin 'im take my kids from me.

GINGER: No!

ROSEMARY: You turned against me...

GINGER: (suddenly) WHO was at your house when you couldn't stop throwin up and WHO called the rescue squad an WHO cleaned up the blood you was spittin up?! It was me who stopped you from jumpin out the winda an it was me who sat on you screamin for the nurse while you spit in my face an afta three days a that I stood back an saw you gettin all the flowers an everybody loves Rosemary an Rosemary says "Ginger put these over there" an "Ginger watch for the nurses while I sneak a smoke" an I did it but deep down I was there waitin for a hey-by-the-way-thanks-for-what-you-did-for-me but Rosemary was too busy to notice her only sister who as usual took time from her own family to be with Rosemary cause Rosemary needed me... (Rosemary is preparing herself to leave.) "No Harry I can't, I gotta help Rosemary move..." "I'll be right back, I gotta pick up Rose's kids..." "Harry, nobody can find Rose so I gotta go..." (Rosemary straightens up.) Then that day that stupid thing with Harry happened... If I leave him where do I go? An-an what about the kids . . . shit, I-I go out there an what? Look for a guy an say save me-please an oh by the way I got three kids an I been...! been havin anxiety attacks an oh yeah oh yeah...I- L..I was told that I got uh two lumps...in my right breast... (Rosemary looks up at Ginger.) That's where I was before I...I was at the uh Doctor Ferrante an...I even joked with him cause his hands felt so warm on my...an I said somethin like um..,Jesus maybe I shoulda picked up a bottle of wine 'fore I came, right, an uh he didn't seem to hear me...he just kept pressin’ this one spot an I could see in his eyes that uh oh...what's a matta? An he told me...not one lump...but two an I cried right there an he he was nice enough to um hold me for a minute an I...all I was thinkin’ was about my kids an wantin’ to be in my house with my family an I somehow managed to drive an I walk in feelin’ uh light-headed an I catch Harry an uh...

(BEAT)

GINGER: (Rosemary is visibly upset. Ginger steps closer to her with a smirk. Rosemary realizes Ginger’s entire story has been a lie) Rose, I'm just gonna say it. You're a real real shitty mother an you're a drunk that's made you into a maniac but you know what? I'm gonna tell you somethin right here an it probly goes back to when we was kids when you would hum a song close to my ear when mom and dad were fighting so I wouldn't hear 'em but I love you as much as I love my kids, I'd give you my last breath an... Sorry for gettin’ sappy here an I would never turn against you. Never. I said things to Brad that well I shoulda been sayin’ to you but I chickened out cause in your way you can make people afraid to say what should be said. Like Dad was. (beat) I won't hug you or nothin’ cause I know you hate that... (beat) You all right?

ROSEMARY: Yeah-yeah... (beat) I'm just...yunno I'm afraid...

GINGER: Makes two of us

ROSEMARY: Brad's probly gonna get custody, huh?

GINGER: Yeah Rose, probly. But it's a temporary thing.

ROSEMARY: Yeah. (beat) I'll bounce back.

GINGER: You always do. (Beat. Rosemary extends her hand out to her sister.)

ROSEMARY: Hang on Ginger... (Ginger grabs hold of her sister's hand.)

GINGER: I'm hangin’ on Rosemary....
```

---

## IC-0671: Ruthless!

- Title: Ruthless!
- Author (byline): Joel Paley
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: July 2016
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS 1, ACTRESS 2, SYLVIA, JUDY, TINA, MISS THORN, LOUISE, NEWSCASTER
- Teaser before the introduction: Yes
- Spoken words (computed): 1356
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joel Paley
ISBN: 978-0573704680
Publisher: Samuel French, Inc.
Date (Month/Year): July 2016
Revised in August 2015 to reflect the 2015 Off Broadway production.
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 2: What do you get when you mix a struggling talent agent,

ACTRESS 1: A 1950’s style stay-at-home mom,

ACTRESS 2: An elementary school teacher who has written her own (probably illegal) version of Pippi Longstocking

ACTRESS 1: And a 3rd grader who knows what she wants and will do anything to get it?

ACTRESS 2: You get a parody of the original Bad Seed! You get . . .

TOGETHER: Ruthless! by Joel Paley
```

### Performance text (classify this)

```text
Suggested Roles

ACTRESS 1: Sylvia, Tina, Miss Thorn

ACTRESS 2: Judy, Louise, Announcer

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

SYLVIA: (Pg 9) Good evening, my name is Sylvia St. Croix. Where does talent come from? Meet Judy Denmark. (Pg 11) A wife and mother leading an idyllic suburban life, and although Judy has absolutely no talent whatsoever, her only child, her daughter Tina has been blessed with a great deal of talent. Blessed, or dare I say, cursed? But I get ahead of myself.

(Scene opens with Judy answering the telephone – Phone rings)

JUDY: (Pg 12-13) Tina’s mother. . . Hello, Pastor Peters Tina has a choir solo Sunday? Oh, she just loves to sing and yes, she loves to pray. She’s good at everything! She’s positively heaven-sent. My kid’s the perfect 8-year-old. Yes, she’s enthralling. Thank you for calling. Good bye.

(She hangs up. Doorbell – Judy answers) Won’t you come in. (Sylvia hands her a business card) Miss St. Croix.

SYLVIA: Please, call me Sylvia. (Pg 14) This lovely home, and of course the very reason I’m here . . . your daughter, Tina. I caught her performance last Saturday at The Rolling Hils Twilight Home for the Elderly. Sensational.

JUDY: We’re very proud of our daughter. (Pg 15) Would you like to meet her? She’s out in the garage breaking in her new tap shoes. (calls off stage) Tina! We have company. (Tina enters) Darling, say hello to Ms. St. Croix.

TINA: (performs a jazzy dance combination) Hi!

SYLVIA: (claps enthusiastically) (Pg 16) Tina, how would you like to be a star?

TINA: Why, it’s all I’ve ever wanted! More than anything in the whole wide world!

SYLVIA: That’s why I’m here. I work with specially gifted children. (to Judy) You are planning a theatrical career for your daughter, are you not?

JUDY: (Pg 17) We want our daughter to have a normal childhood.

TINA: I’ve had a normal childhood! It’s time to move on. (Pg 18) Oh, Mama, please say yes. Please?!

JUDY: Well, I suppose some coaching can’t hurt, but only after school.

SYLVIA: We start this afternoon!

TINA: (shaking her head) Today’s the audition for the school show. I’m trying out for the lead.

SYLVIA: Oh, Judy, you must be so proud. I wish I had a little girl.

JUDY: Don’t you have any children, Sylvia?

SYLVIA: Let’s just say she didn’t have any talent. (Pg 19) Oh, she used to jump around the living room. “Look, Mama, I’m dancing!” But she was merely jumping. It was embarrassing! ******* The Turner School Auditorium – Later that afternoon *******

MISS THORN: (Pg 20) Good afternoon, students. I’m Miss Thorn, and after directing last year’s riveting production of Who’s Afraid of Virginia Woolf, I’m delighted to announce this year, the Turner School will present “Pippi in Tahiti,” the musical written and directed by me (gesturing to herself) Myra Thorn! (Pg 21) And now . . . the starring role of Pippi Lingstocking will be played by . . . Louise Lerman! (Tina clearly is disappointed) ******* The Denmark Living Room – later that afternoon *******

SYLVIA: (Pg 22) You had your heart set on playing Pippi, didn’t you?

TINA: It’s the best part in the show! I don’t understand.

JUDY: Oh, so what if Louise Lerman is playing Pippi -- You get to play Puddles!

TINA: (Showing her true nature) I don’t want to play a dog. I mean, look at me. I was born to play Pippi Longstocking! (She stomps her feet) And Louise Lerman can’t act!

JUDY: Now you listen to me, young lady, do you want to stay in showbusiness?

TINA: (angelic) You’re right, Mother. What would you give me for a bucket of kisses? [doorbell] (Pg 23) I’ll get it. (Opening the door) Why, good afternoon, Miss Thorn. Haven’t changed your mind, have you?

MISS THORN: I’m afraid not. (Tina pouts)

JUDY: Miss Thorn, the reason I’ve asked you here is because Tina’s awfully upset about not playing Pippi.

MISS THORN: I must admit, Mrs. Denmark, I’ve never known anyone to want a part so desperately.

SYLVIA: (Pg 26) My dear Miss Thorn, might you considered letting Tina be the Lerman girl’s understudy?

MISS THORN: We’re only giving one performance, but if it makes you happy then, yes, Tina can be Louise’s understudy.

TINA: Wait a minute. You expect me to learn all of Pippi’s songs and all of Pippi’s lines -- and there’s still a chance I don’t even get to play Pippi?

MISS THORN: (Pg 27) That’s correct.

SYLVIA: Unless, of course, something were to happen to Louise. (she looks knowingly at Tina)

TINA: (Tina gets the message) I’ll do it! ******* The Turner School Auditorium – 6 weeks later *****

MISS THORN: (Pg 32) Okay, let’s take it from after the storm at sea. Rachael Hobbs, stop giggling. This is a theater, not a playground. We’re not here to have fun. Okay, here we go. Take your places for scene five. Go music!

LOUISE: (enters dressed as Pippi Longtocking; looks around in awe) This must be Tahiti! And I’m Pippi! Pippi Longstocking! I’d like you to meet my best friend, Puddles! (An unhappy Tina enters as the dog) (Pg 33) Puddles and I were in a terrible storm. Our boat tipped over and everyone got drowned. But Puddles saved my life and brought me to this tropical paradise. Way to go, Puddles! Shake! (holds out her hand) You’re supposed to shake my hand.

TINA: (with an attitude) Look! I don’t think Puddles would want to shake hands here, ok? Not after being shipwrecked and having to doggy-paddle fifty miles!

LOUISE: I’m sorry, I can’t act with this. (gestures to Tina)

TINA: You can’t act period. The only reason you got the part is because Mommy and Daddy bought it for you.

LOUISE: (Pg 34) Do you honestly think I want to be in this stupid play? It’s embarrassing. But it makes my parents happy, and when Mike and Betty are happy, I’m happy. Got it?

TINA: But I’ve got to play Pippi!

LOUISE: You don’t have the range! (Louise flippantly leaves the stage)

TINA: (menacingly) I ASKED POLITELY. I SAID PLEASE . . . Now there’s nothing left to do but . . .

(Sweetly) Oh, Louise! (exits after Louise) ********* The Denmark Living Room – Later that afternoon*******

NEWSCASTER: (Pg 35) (voice over) Time for the local news. One of the students attending Turner Elementary School accidentally hung herself with a jump rope after falling from a catwalks high above the auditorium. The child’s name is being withheld until parents can be notified. In other news . . .

JUDY: (Pg 36) That poor little girl.

TINA: Tina enters from school) Hello, Mother. We didn’t have our lunch because something bad happened to Louise Lerman. (smiling) Can I have a hamburger?

JUDY: Of course. Now, sweetheart . . . if you want to go to your room . . . if you want to cry – or even stop smiling, I’ll understand.

TINA: Why should I cry? I didn’t get killed. (Tina exits, then doorbell)

MISS THORN: (obviously shaken) Hello, Mrs. Denmark.

JUDY: (Pg 37) Come in, Miss Thorn. Of course, the play has been canceled.

MISS THORN: Whatever gave you that idea? I think this is an excellent opportunity for the children to learn that the show must go on!

JUDY: (Pg 38) But it’s wrong. Shockingly wrong!

MISS THORN: (Pg 37) How’s Tina. She is the understudy. (losing it) (Pg 38) Look, Mrs. D! That talented little girl of yours better be in costume and in place by show time, or I shall be forced to go to the police!

JUDY: The police?!

MISS THORN: It seems the Pippi wig is missing. Now, Tina was seen chasing Louise and snatching at the wig. But, I suspect nothing. Not a thing.

JUDY: Why don’t you just come out and say it? Look me straight in the eye and tell me that my eight-year-old child killed for a part in the school play.

MISS THORN: Not just any part, Mrs. Denmark. The lead! (she storms out) *********

JUDY: (Pg 39) [Judy notices Tina’s school bag by the door, she unzips it and pulls out the Pippi wig andwhispers in horror) Tina!

TINA: Did you call me, Mother?

JUDY: What are you doing with Louise Lerman’s Pippi wig? And don’t lie.

TINA: (with feigned innocence) I found it after Louise had her. . . accident. I was afraid to give it to Miss Thorn. Afraid Miss Thorn would think I was naughty.

JUDY: Were you naughty, Tina?

TINA: (innocently) Oh, no, Mommy. I wasn’t naughty. I found the wig and put it in my bag so it wouldn’t get lost. (Pg 40) [Besides] It’s my wig and it’s my part! (beat) I love you and I think you’re the best mother in the whole wide world. That’s what I tell everyone.

JUDY: Knock it off, Tina. You’re not that good! You did it, didn’t you? You killed Louise Lerman for a part in a play?

TINA: Not just any part, Mother! The lead! I told Louise I had to play Pippi. But she said I didn’t have the range. So, I chased her up onto the catwalk. That’s when she gave me the wig. I asked her if that meant I could play Pippi and she said . . . “Yeah, over my dead body!” So I wrapped the jump rope around her fat neck and pushed her over the side.

JUDY: Oh, Tina, Tina!

TINA: I wanted the part. What could I do?

JUDY: You could have hurt her. You didn’t have to kill her.

TINA: (Pg 41) I wasn’t thinking. I was tired and I didn’t have my lunch.

JUDY: Look at me, Tina. You did a bad thing, a very bad thing. You killed that little girl Do you know what that means?

TINA: (beat and then with an evil smile) Yeah, it means I’m playing Pippi!
```

---

## IC-0672: Sans Merci

- Title: Sans Merci
- Author (byline): Johnna Adams
- Work: Not specified
- Publisher: Original Works Publishing
- Publication date as stated: Sept 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: KELLY, ELIZABETH, TRACY
- Teaser before the introduction: Yes
- Spoken words (computed): 1714
- Already set (do not supply): none

### Source block (context only)

```text
Author: Johnna Adams
ISBN: 978-1934962466
Publisher: Original Works Publishing
Date (Month/Year): Sept 2013
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 2: We see it in the headlines: Peacekeepers killed in Mali, in the Central African Republic, in Columbia.

ACTRESS 1: Names and faces become merely blips on the historical fabric of oppression, domination and brutality throughout the world.

ACTRESS 2: But these idealistic young men and women are so much more than a passing headline.

ACTRESS 1: Sans Merci (Without Mercy) by Johnna Adams tells the story of Tracy and Kelly, young college students determined to make a difference by helping the U’wa Indians in Colombia.

ACTRESS 2: But when the mission erupts into violence . . . who is left to put the shattered pieces together again?

TOGETHER: Sans Merci by Johnna Adams
```

### Performance text (classify this)

```text
NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actress 1 – Kelly; Actress 2 – Elizabeth and Tracy

Scene opens with Kelly asleep on the couch, a cane by her side. Elizabeth consults a piece of paper and finds the apartment number on Kelly’s door. She knocks. Kelly is startled awake, retrieves her cane and opens the front door.

KELLY: (Pg 8) Yes?

ELIZABETH: (Pg 10) I’m Elizabeth Bird . . . from Chicago. We’ve never met, but we’ve spoken on the phone. Once or twice.

KELLY: You’re Tracy’s mom. (she steps back to allow Elizabeth to enter) How did you get my address?

ELIZABETH: (Pg 15-16) (Ignoring the question) You two met in a literature class?

KELLY: Feminist Studies in Art and Literature. She did a presentation. . . on Keats . . . La Belle Dame Sans Merci

TRACY: (Pg 33) (Tracy steps out of the scene and speak to the audience) I met a lady in the meads, / Full beautiful—a faery’s child, / Her hair was long, her foot was light, / And her eyes were wild. . . . (Pg 28) My mother has a degree in poetry. Almost a PhD. I was raised on Keats the way other kids were raised on Sesame Street. I love him.

ELIZABETH: (Pg 16) So that’s feminist literature now. La Belle Dame Sans Merci? That’s what the feminists all really want. Feminism at its core is more about female superiority than equality. (Kelly shifts her weight to relieve pressure on her leg) (Pg 18-19) It must be difficult learning to do things with that cane.

KELLY: It’s fine.

ELIZABETH: Will it get better? Your leg?

KELLY: No. it won’t

ELIZABETH: I think I read that you’d been injured. I didn’t know how serious it was.

KELLY: (Pg 20-22) I don’t mean to be short. I don’t mean to be unkind. What did you want?

ELIZABETH: Well, most of our information about what happened came to us second- or third-hand . . . We did eventually get her body back. In a sealed casket. But we never got the things she took to Colombia. I thought you might have them.

KELLY: I do. I have her backpack. The clothes they cut off her when they raped us. I have her last journal. Those are the things I have. I’ll get them. (Kelly is shaken, but crosses to the bedroom door)

ELIZABETH: And there was something else. (Kelly turns; Elizabeth pulls a pride flag out of her handbag; her hands are shaking) This was in the box the girl from the university sent. It’s a pride flag, I think. I don’t know why she had it. (silence) Were you and Tracy lovers?

**** flash back *****

KELLY: (Pg 28-30) So you really opened my eyes. To Keats . . . Are you a poetry major?

TRACY: Literature. What’s your major?

KELLY: Political Sciences. I’m going to Colombia this summer. To help the U’wa Indians. The Occidental Petroleum Corporation is stealing their lands to extract fossil fuels. We’re going to help them organize.

TRACY: Is it dangerous? (their hands touch . . . andawkward moment)

KELLY: No. The U’was reservation is surrounded by rebel forces. They control almost half of Colombia right now. But they’re on our side, and we have their permission to be there.

TRACY: But you’re risking your life. I mean, those rebels have guns. Something might happen.

KELLY: They would never kill US citizens . . . Don’t let me talk your ear off about the U’was. I get crazy excited about it and go on and on.

TRACY: I think that’s great. You’re passionate about things. Do you want to get something to eat? Maybe coffee? **** back to present day ****

KELLY: (Pg 34-43) We were friends. Best friends. That’s all.

ELIZABETH: You said you had her last journal . . . The one I have stops a few months before she met you. So [it] must be from the time she met you to just before she died. (all business) Could you get it?

KELLY: (makes a small noise) It’s . . . It’s private . . . please.

ELIZABETH: I was having a phone conversation with her once. And I heard giggling. But not from her. From someone else. A female voice. But close to the phone. Like someone had their mouth very near hers. And Tracy said, “shush.” Softly. Just “shush.’ Very tender. And I knew. But I didn’t say anything. Because I hoped I was wrong.

KELLY: She said you wouldn’t understand. She said you voted to support some state initiative. Marriage means a man and a woman. You wanted grandchildren. (Beat) She loved you so much. She wanted you to be proud of her.

ELIZABETH: You know, I don’t think I’ve ever been in a lesbian apartment before.

KELLY: The apartment’s asexual. I’m the lesbian.

ELIZABETH: Was that an insulting remark? I lost all capacity for tact when my daughter’s mutilated body was returned to me in a sealed box. (Looking around the apartment) I don’t know what I expected in a lesbian’s apartment. I guess more flags like the one I got in the mail. (She notices a poster on the wall) Who is this?

KELLY: Lech Walesa . . . The Polish labor organizer. From the Solidarity movement.

ELIZABETH: And this?

KELLY: Cesar Chavez. He was a Mexican labor leader and organizer . .

ELIZABETH: I know how he was. Thank you. You really seem to identify with the wrong sort of people. People that mobs of violent peasants want to tear limb from limb.

KELLY: Lech Walesa is a former president of Poland. He won the Nobel Prize. No one tore him limb form limb. He’s alive . . .

ELIZABETH: People wanted to kill him.

KELLY: People wanted to kill Gandhi.

ELIZABETH: Exactly. I wouldn’t consider him a role model either.

KELLY: He stood up for an entire nation when no one else had the guts to. He changed the world!

ELIZABETH: He put his family in jeopardy. It’s a miracle he wasn’t tortured to death like my daughter. (Long pause)

KELLY: (with passion) So, the world you want to live in is a world where nobody stands up for freedom? Where we all just accept persecution to be safe. I can’t accept that. Somebody has to step out of the crowd and say, “this is unacceptable.”

ELIZABETH: Oh, don’t get worked up. I don’t care about Gandhi. I just wanted to see it.

KELLY: See what?

ELIZABETH: What Tracy died for.

KELLY: You . . . blame . . . me?

ELIZABETH: Of course, I blame you. My daughter was a literature major. She was going to a student-led bible study. She voted republican like her father and me. She had a crush on a boy who worked as a sports’ editor on the college newspaper. I want that boy for her. Because I can think of a thousand ways [he] might have ruined her life. But he wouldn’t have ended it! He wouldn’t have taken her where you took her.

KELLY: His name was Joshua. He was gay.

ELIZABETH: Oh . . . Terrific. Another one. (Long silence)

KELLY: (Pg 72-75) Don’t you . . . (sighs) . . . Don’t you want to know . . . what happened?

ELIZABETH: How she died? (she steels herself) Yes. I do.

KELLY: We had been in the U’wa village for three days. We thought we were safe. Tracy and I took the camera and went to get footage of the cliffs for a documentary film we were making –

ELIZABETH: It was a video camera?

KELLY: (quickly) There isn’t any footage of her . . . Just stills. (Beat) The cliff site is sacred. And they let us go up there alone. See there are two rebel armies in Colombia. Sometimes they’re allies. We had permission from the ELN* to be in the village. And we thought that they would have cleared it with the FARC**. The other group of rebels. Right? They told us it was safe. But they didn’t. And it wasn’t safe. The FARC didn’t see the value in having stupid American kids working on their behalf. They thought we’d be more valuable as hostages. That they could get money from our families.

ELIZABETH: Why didn’t they keep you as hostages?

KELLY: (makes a small noise) Because I fought. **** flashback to the cliff *****

TRACY: (Pg 76) Oh, Kel! Oh, God! It’s beautiful! I’ve never seen anything so beautiful. When my mom sees something this beautiful she quotes Keats . . . (Pg 83-84) I saw pale kings and princes too, / Pale warriors, death-pale were they all; /They cried—‘La Belle Dame sans Merci / Thee hath in thrall!’ (the girls hear a noise in the brush. They freeze)

KELLY: Don’t move. Don’t attract their attention

TRACY: (whispers) What do they want? You think it’s the ELN?

KELLY: Probably. They’re speaking Spanish. They said the word Americans.

TRACY: They’re looking for us!

KELLY: I want you to go back to the village. I’ll make a lot of noise and they’ll follow me. Find the cellphone coverage area. Call for help. I love you.

TRACY: I love you, too. **** Present day ****

ELIZABETH: (Pg 86) . . . They found you. Alone. On the cliffs.

KELLY: Yes. I told them to rape me and leave Tracy alone. Two of them held me down. . . When it was over they went for Tracy. And I fought them . . . Then the leader pulled out a pistol and shot me in the leg. And Tracy screamed . . . they dragged me over to the edge of the cliff and all I could do was watch. They raped her. And when they were done, she started pleading with the soldiers. To not put me so close to the edge. She told them I was scared of heights. Oh, Tracy . . . She thought they would care or something. And then the leader pushed me off the cliff. There was a ledge about 60 feet down the face of the cliff. And I slammed into the ledge. My leg shattered. But I survived. I knew I was dying, but I didn’t know what had happened to Tracy. I thought she was alive. I thought she was a hostage . . . So I couldn’t die. The U’wa found me the next afternoon.

Tracy was dead. They carried me over to her body. I waited with her until they brought the trucks. I held her hand. . . The soldiers had shot her in the head.

ELIZABETH: (Pg 88) Do you think she fought them? (Kelly makes a small noise) Do you know how long she lived, after you were pushed? If she was tortured? (Kelly can’t speak) (Long silence) (Pg 90) Well . . . (She takes Kelly’s hand) I do think . . . as much as anybody can be in love in this world, you were in love with my daughter . . . It doesn’t mean that I don’t wish you had never been born. And for Tracy’s part, I still hope she didn’t love you . . . But . . . I . . . imagine she did. (Elizabeth goes to the door to leave but Kelly stops her)

KELLY: (Pg 91-93) There’s something else. Something of hers I didn’t tell you about. I was recording with the digital camera just before the soldiers found us. I put it in Tracy’s backpack. I forgot to turn it off. There’s no picture . . . but you can hear everything. It’s really hard to listen to . . but if you want, you can hear what happened after they pushed me . . . you can hear what she said. (Elizabeth nods and Kelly pushes the play button on the recorder)

TRACY: Murderers! Bastards! She was good! I loved her! This was wrong and I was here to see it! Rapists! Your mothers should find you and kill you! They should spit in your faces. I will find where you live! I WON’T STOP TELLING PEOPLE WHAT YOU DID! I WON’T STOP TELLING PEOPLE UNTIL THE WORLD KNOWS! You’ll have to kill me! I’ll come for you in the night with razors! With stones! (Tracy is shot in the back of the head and Kelly breaks down)

ELIZABETH: (Pg 16) Full beautiful – a faery’s child / Her hair was long, her foot was light . . .. And her eyes were wild.
```

---

## IC-0673: Saturday Night/Sunday Morning

- Title: Saturday Night/Sunday Morning
- Author (byline): Katori Hall
- Work: Katori Hall Plays One
- Publisher: Bloomsbury Methuen Drama
- Publication date as stated: Sept 2011
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GLADYS, MISS MARY, LEANNE, TAFFY, MABEL, ACTRESS 2, ACTRESS 1, GLADYS AND LEANNE, RADIO
- Teaser before the introduction: Yes
- Spoken words (computed): 2141
- Already set (do not supply): none

### Source block (context only)

```text
Author: Katori Hall
Book: Katori Hall Plays One
ISBN: 978-1408147023
Publisher: Bloomsbury Methuen Drama
Date (Month/Year): Sept 2011
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Set in a Memphis beauty shop/boarding house during the final days of WWII,

ACTRESS 2: a group of African American women draw strength from each other as they wait for the war to come to an end.

TOGETHER: Saturday Night / Sunday Morning by Katori Hall.
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actress 1: Gladys, Taffy Actress 2: Leanne, Mabel, Miss Mary and Radio

Gladys: From Birmingham, Alabama . . . Homely, slightly ugly even, but expertly put together. A churchgoing girl in her early 20s – an aspiring writer. Miss Mary: 30 going on 60. The owner of the beauty shop/boarding house. A widow who lost her husband during WWII. Leanne: Early 20s – A beauty queen from Texas. Depressed since she hasn’t heard from her beau, Bobby, who is fighting overseas. Taffy: Late Teens – Mabel’s younger sister – an ugly duckling and a bit socially inept Mabel: Early 20s – a loose, wild woman searching for adventure. Taffy’s older sister

GLADYS: Is Miss Mary ‘round? Folk say she rentin’ out rooms to young girls.

MISS MARY: Ain’t no mo’ room up in here. Only bed open is a bed in my room and I don’t share.

GLADYS: Well . . . I’m justa needin’ a room to board up in for a while. Thass all. How much you rentin’ rooms fu’?

MISS MARY: If I had one to rentcha it’d be a dollar a week. If this was a brothel y’all wouldn’t have to pay nothin’, but it ain’t, though some folk wanna treat it as such . . . I fount a tourser sock in ya’ll room and don’t nobody wear trouser socks ‘round here. Last time I checked womens was wearin’ nylons.

GLADYS: I could do som work ‘round here. I was a secretary in a church so I knows typewritin’ like the back of my hand.

MISS MARY: If you got fingers that can shampoo you some hair I’m all for it. Let me see them hands. I needs ‘em quick and nimble. (Miss Mary goes to pull off Gladys’s gloves. She snatches her hands back.)

GLADYS: Let me show ya how quick and nimble I can be. (She pulls out a typewriter from her suitcase, plunks it down and swiftly puts in a piece of paper. She types out a paragraph)

MISS MARY: I like them fingahs. I bet you could scratch some dandruff out folk heads. But . . . it still ain’t no room up in here.

LEANNE: Leanne sashays slowly over to Gladys I’m Leanne. . . I like yo’ style. Memphis women ain’t dressin’ like that. That hat. Them ribbons. Them gloves . . . Cute. Remind me of Texas. You cute. (to Miss Mary) She can stay in my room. It’s fit for a queen, but it can hold two. Nice to meet you, honey bun.

TAFFY: She got a curse on her.

MISS MARY: Y’all be in a bad mood, too, yo’ maine say he gone do somethin’ and he don’t do it.

TAFFY: How he gone write letters and shoot people at the same time? The womens these days.

LEANNE: (ignoring her) Why mens can go away, but they memory just stay wit’ ya? Sometime it’s better when they gone than when they here. (she bursts into tears)

GLADYS: Her, here, lady. You know if you pray, God’ll take all the pain away.

LEANNE: I done tried, tried everything! Oh, I just miss him so. I remember how he smelled, his touch. You know how a person just haunt yo’ body. . .

GLADYS: Did he die?

LEANNE: Unh, unh! Don’t say that. Don’t you ever say that about my baby Bobby!! When I go outside every maine I see look exactly like him.

GLADYS: You just havin’ visions. Thems can be taken care of wit’ a lil’ prayer.

LEANNE: Honeycomb, I don’t know how to pray (Beat) You got a lot to learn. (Leanne exits)

GLADYS: She gone get sick carryin’ that cup of tears in her throat for so long.

TAFFY: Where does you get all them sayins? Fu’ as long I been alive I ain’t never heard colored fold talk the way you talk.

MABEL: Yeah, they be soundin’ . . . special. Who talk like that?

GLADYS: (defensive) Writers. Actually, I thought maybe . . . I could . . . When I was down home, I say this ad in the paper. (She pulls out a yellowed, wrinkled newspaper from her Bible and hands it to the girls. They satre at it. Then her. They can’t read) Oh . . . It says the Chicago Defender’s lookin’ for them a new reporter . . . I always wrote my own stories. Made ‘em up.

MABEL: (Sharp gasp) Huh! That’s it! That’s it! Why didn’t I thank of this earlier. We been needin’ to get old beauty queen out that salty mood . . . You could help us – all of us – out.

GLADYS: By doin’ what?

MABEL: By writin’. To Leanne. Like you Bobby. We get Gladys to write like she Bobby and I betcha that’ll break old ‘beauty queen’ out her blues. (to Taffy) Don’t you want the world back the way it was? When we all would laugh and cut upon the porch? Them was the days. (to Gladys) When we first moved her Bobby ‘n Joe’d walk past the beauty shop every day trying’ to “coat” us. They had just signed up for the service. . . We’d make sho’ we put Leanne in the middle, that way mens have to talk to either of us before they got to her. That’s how I got my husband Joe. Leanne thought he was ugly. (Sighs) He is. But he is so sweet. I met him that day, the next week we was married.

TAFFY: Leanne thought Bobby was gonna propose like Joe did fo’ he left. He ain’t. But he promised while he was away he’d write her . . . She been depressed eva since.

MABEL: What you say, Gladys? Thank of it as usin’ the gift God gave you to bring joy and happiness to the world. Our world. (she hands Gladys a pen an piece of paper) Try this (dictating to Gladys) ‘I looked at you. You looked good. Gush-dangit. Damn good! And shoot, that was it for me – ‘

GLADYS: I don’t like that. There ain’t no flow, no poetry in his speech. Bobby must sound like the Shakespeare of the seas. I must have some kinda style. Like . . . ‘I want to leave my fingerprints on your skin, but I suppose this inks will have to suffice. My dear Leanne, I can’t wait to see you again. Please kiss the air for me. I know the wind will deliver your lips to my bosom, which aches to hold you again. Yours truly, Bobby.’ TRANSITION

ACTRESS 2: Now all they had to do was get that letter into the mailman’s bag.

ACTRESS 1: Luckily Mabel was able to district him while Taffy and Gladys rummaged through this bag, steamed off an overseas stamp to use and tucked their letter into the bottom of his bag.

ACTRESS 2: A letter marked TO: Leanne Golden. FROM: Bobby Jenkins

MABEL: (overacting badly) Open it! Open it!

LEANNE: (crying the truthful kind of tears – undramatic, human – quite different than her tears earlier) See, I tolja so. He’s alive. He’s alive.

MABEL: Well, what it say?

LEANNE: I don’t know. I can just read the last words . . . Love . . . Bobby. [Later that Saturday night]

LEANNE: And when he get back we gone have a big wedding. Daddy gone be so happy. Y’all can be my bridesmaids. I wish I could read it to myself. The only word I can make out is ‘love’. Gladys, read my favorite part again. (stares out the window)

GLADYS: (focused on Leanne rather than the letter) ‘I’ve stared at the slope of your face in my dreams and I remember every curve, every valley of your face from your cheekbones to your lips. I can fall onto those lips like a bed.’

LEANNE: (turning back to Gladys) I never thought I’d see him again or hear from him again, but today – Today was like being born again. I feel like a girl again. In love with him like a lil’ girl. Help me, Gladys. Help me write back to him.

GLADYS: Write? Back?

LEANNE: He must be scared. All alone over there. Not knowin’ when he gone come home. If he gone come home. Please, Gladys. Don’t make me beg you.

GLADYS: I’ll. Help. (nods)

LEANNE: ‘Dear Bobby –‘ (Scene shifts to pantomime with Leanne dictating while Gladys writes) ******* SCENE CHANGE *******

MISS MARY: It’s nice to see her smilin’ ‘round here. I’m so glad Bobby decided to write her.

MABEL: (Mabel laughs then composes herself) Just happy that Leanne happy. Leanne made it feel like a funeral parlor ‘stead of a beauty parlor. Now it’s all back. We getting’ it all back. Just like we planned.

MISS MARY: Planned? How you plan that? Y’all ain’t tellin’ me the whole story. So Gladys writin’ letters for Leanne?

TAFFY: (fast-paced) Gladys pretendin’ like she Bobby! (with a look at Mabel) Miss Mary was gone find out anyway.

MISS MARY: Y’all playin’ wit’ that po’ girl heart. What if that maine dead? Whatchall gone do then?

MABEL: It don’t matter he ain’t dead to her, now! Don’t you like yo’ beauty shop like this? Happy! Before she got that letter this was like the last stopover fo’ Hell. She done cried enough tears to flood the Mississippi Delta thrice over.

MISS MARY: Yo’ love don’t come back, you don’t know how long you’ll cry. (Mabel and Taffy exit as Gladys enters and crosses to go upstairs also) No so fast, Miss Alabammy!

GLADYS: Yes ma’am?

MISS MARY: Don’ you be bein’ all nice to me. You too nice. Letting them girls run you like that. Puttin’ you all up in they little games. Y’all spinnin’ goddamn fairy tales and this real life out there. Real life I tells ya! Whatchoo gone do if he don’t come back, huh?

GLADYS: They tolja?

MISS MARY: Yes, they did. A woman heart ain’t nothin’ to play wit, nah. Believes me, I know. You gone start somethin’ you can’t finish and what then? What then? ********* SCENE CHANGE ***********

LEANNE: (looking out the window) I wonder when he gone write me another. And another. And another.

TAFFY: It took him four years to write the first one. Give him some time, damn.

LEANNE: I don’t have no more time. What if he dies before he gets back? What if he’s dead right now? Oh, no! Bobby is dead! Bobby is DEAD! (Beat – Leanne bursts into tears and exits)

MISS MARY: Now, look at what ya’ll done done to Leanne!

MABEL: It look like you gone have to write another letter to Leanne. (Beat)

GLADYS: Ain’t one enough?

TAFFY: Oh, help us, Gladys! Help us out this misery.

GLADYS: Another letter? I can’t lie like that again. I’m already writing back letters to him as her. I’m lyin’ thisaway and thataway. I’m lyin’ all over the place.

MABEL: Don’t get to feelin’ all guilty on us, church girl. Is a lie a lie if it’s a good lie? ‘Sides, when you go to church tomorrow, repent! All yo’ sins’ll be washed away.

GLADYS: But I got my own work to do. My own stories to tell. I’m tired of tellin’ lies.

TAFFY: Please! PLEASE!

MABEL: One more tale to end our HELL –

GLADYS: All right! All right! I’ll do it if y’all just hush. Just let me have peace. (the girls exit and alone on stage, Gladys begins to write) ‘Dear Leanne – ‘ I was walkin’ down the street in Paris. I was struck by how it smelled. There are lavender gardens here. It smells like purple and promise, baby breath and longing. It smells of you. . . ‘ (to herself) I wish she loved me like she loves you. (Beat) There, I said it. I can’t believe it. I finally said it . . I feel so ashamed. I ain’t supposed to feel this way. I shouldn’t feel like this, like – God gone be mad at me. ***** SCENE CHANGE *******

LEANNE: Read it to me again.

GLADYS AND LEANNE: ‘You ever smelled lavender, love. It smells of purple and promise, baby breath and longing. It smells of you.’

GLADYS: Well, don’t you know it by heart.

LEANNE: Well, it’s my favorite part. Oh, he loves me. He loves me so!! When this crazy world gone let my maine come home. Let him come home to me. I could wait on my maine forever.

GLADYS: He wouldn’t wait on you forever.

LEANNE: You don’t know him. Bobby is a gentlemen.

GLADYS: No. He ain’t. He waited too long to write ya . . . if you ask me. Four years? (Beat) Leanne . . . I wanna tell you something!

LEANNE: I wanna tell you something! I wanna propose to Bobby. (silence)

GLADYS: Leanne, are you sure you love him? I can’t . . . can’t write this letter. You don’t love him. You don’t even know him. Who the hell is Bobby?

LEANNE: He exists right here (pointing to her chest)

GLADYS: Nooo! HE exists in there (pointing to Leanne’s head) He ain’t here, Leanne! You deserve someone who’ll be there for you. Right here. Right now. Bobby ain’t that kind of man.

LEANNE: These letters tell a different story.

GLADYS: Those letters might be a lie! WHY?! Why you love him sooo much?

LEANNE: He the first man that done made me feel . . . feel like God inside. You ever felt that, Gladys? . . . I would wait on that feeling again forever . . . help me propose to my man. (Gladys is defeated an submits. She takes out her typewriter) ‘Dear Bobby, Will you marry me? Love, Leanne’

GLADYS: (quickly types. Silence) That it? (Gladys stands and opens her mouth. She tries to speak, but before she can profess her heart a radio broadcast breaks the silence)

RADIO: We interrupt your regular radio program for a special message from the President of the United States of America, Harry S. Truman. ‘On this day, August 15th, Japan has surrendered. The final Axis ally has fallen. . . America has won her blessed fight on this day. Today war will be no more . . .. ‘

GLADYS: (pulls out a letter from her dresser and holds it out to Leanne) I’m sorry I never gave this to you before. This the last one. (Beat) Ain’t you gone open it?

(Gladys dictates the letter without it being opened) ‘Dear Leanne, I’ve never felt this way about someone. I’ve tried and tried to stop thinking of you. I never knew somethin’ so bad could feel so good. I love sleepin’ besides you. You are an angel to me. I live for Saturday nights, Leanne. But the most god-awful hour of my existence is when Saturday night roll into Sunday morning. In those wee hours of dawn I repent my heart’s sin, for everything I yearn for, I know God will never let me win’ (silence – Leanne snatches the paper from Gladys’s hands and tries to read the last words.)

LEANNE: ‘Love, Gl – Gla – a / dys. (Leanne backs away from Gladys) So . . you . . you Bobby? You lied to me!

GLADYS: I meant every word.

LEANNE: Not like that! I am not that way. You think I’m that way?

GLADYS: I just wanted to make you feel like God inside.

LEANNE: You will never make me feel like that. You are nasty! Sick! Here I thought you was a church goin’ girl! (Leanne exits in tears)

GLADYS: But I have repented. I repent every day. I repent. (silent tears slide down Gladys’ face)
```

---

## IC-0674: Sentences and Words

- Title: Sentences and Words
- Author (byline): Cynthia L. Cooper
- Work: Rowing to America and Other Plays
- Publisher: Smith and Kraus
- Publication date as stated: June 2002
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: KARLA, MAGGIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1906
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cynthia L. Cooper
Book: Rowing to America and Other Plays
ISBN: 1575252716
Publisher: Smith and Kraus
Date(Month/Year): June 2002
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Would you be capable of forgiveness if someone you love was brutally murdered? Many who oppose the death penalty claim that vengeance is also a form of violence and that we cannot defend life by taking life.

ACTRESS 2: We don’t punish robbers by robbing them, or rapists by raping them. Why then do we punish murderers by murdering them? Sentencing someone to "death retaliation" is a more accurate term and, hopefully, more thought-provoking, as is shown in . . .

TOGETHER: Sentences and Words by Cynthia L. Cooper
```

### Performance text (classify this)

```text
(A woman stands on the porch of a house that crosses between ramshackley and neat. The setting is small southern Ohio town, which is more southern than northern, and more rural than populated. The woman on the porch, KARLA JACKSON, wears a suit, glasses, blouse and heels. SHE carries a purse and a little file folder. KARLA walks up to the door. SHE bangs loudly on the door several times.)

KARLA: Mrs. Denton! Mrs. Denton, I know you're in there. (There is no answer.)(KARLA looks at herself and quickly takes off her shoes and exchanges them for beat-up loafers that she is carrying in her purse. She takes off her jacket and stuffs it away in the same purse. SHE knocks again.) Mrs. Denton. I'll stay here all night if I have to.(KARLA bangs again, profusely. Now, she becomes conscious of her hair and ruffles it. SHE takes off her glasses and puts them away. She bangs again!) MRS. DENTON!

(The door opens. A furious MAGGIE DENTON stands at the doorway. SHE is dressed in a very unfancy skirt with a shirt over it. The shirt is hangs outside the skirt. SHE seems a bit disheveled, although SHE has attempted to be neat.)

MAGGIE: Get away from here. Get AWAY!

(MAGGIE quickly slams the door.)(KARLA, undeterred, pulls her shirt out from her skirt.)

KARLA: I've got to have a word with you Mrs. Denton. Tomorrow's the hearing date. For the sentencing. And I've got to talk to you before then.

(MAGGIE opens the door one more time. KARLA puts her foot into the door opening to prevent MAGGIE from slamming it shut again.)

MAGGIE: You get away or I'm gonna tell my husband to chase you away. You saw what he did last time.

KARLA: He's gone, Mrs. Denton. I saw him drive away. This is just something for you and me.

MAGGIE: We don't have nothing between us, Lady. Nothing.

(MAGGIE tries to slam the door, and to push it shut. KARLA's foot does an admirable, if painful, job of preventing the door from closing entirely. KARLA speaks through the slight opening in the door.)

KARLA: This is a death state, Mrs. Denton. You know what that means, don't you?

MAGGIE: I know what you did in court. I heard what you said about my Tommy. And that was plenty enough for me. Standing up for that dirty old FILTHY OLD SCUZZY OLD SLIMY ROTTEN NASTY DISGUSTING Franklin Miller. I seen plenty.

KARLA: Don't stop, please. Tell me. More. I want to hear.

MAGGIE: You're a whore.

KARLA: You can call me Karla.

MAGGIE: I ain't calling you nothing.

KARLA: May I call you Maggie?

MAGGIE: I'm gonna call the sheriff, you don't get off my porch.

KARLA: I don't think so.

MAGGIE: You don't think what?

KARLA: I don't think you like the sheriff any more than I do.

MAGGIE: You think you know so much. All that education you got.

KARLA: Look ... Maggie. My foot's about to break. You know that defending Mr. Miller was my job. It's my job tomorrow at the sentencing. I'm not pretending anything different. All I want is one minute of your time.

MAGGIE: He never give Tommy one minute. One minute my Tommy's pitching stones into the field and the next minute he's stabbed behind the shed.

KARLA: You don't have to talk. We can sit. I just need to sit with you before I go back into that courtroom tomorrow. Is that too much to ask? Please?

MAGGIE: (Emotionally.)My husband wouldn't allow nobody like you in the house.

KARLA: On the porch then? I'm begging you, Maggie. I know your husband won't speak to me. But, one day, in the courtroom, one day you were sitting in the back, and I turned around, and you looked me straight in the eye and we started to say something that day, just you and me, something silent, something that hasn't been said, and I just have to finish that off.

MAGGIE: I don't recall none of it. If there was any such thing, I probably was making a prayer for you, lady.

KARLA: Will you do it again, then? I know you're a real kind-hearted woman. Maggie?

MAGGIE: One minute. (MAGGIE reluctantly steps out on to the porch.)

KARLA: Thank you, ma'am. Thank you very much. (THEY sit on a soggy couch and moldy chair set out on the porch. There is silence.) I do have one thing to say.

MAGGIE: You said we didn't have to say nothing. I'm not much for talking with you, lady.

KARLA: Okay. If you could just listen. I'd like to talk.

MAGGIE: I'm just going to pray like I agreed to. That's all. You can say whatever you like, but I'm just going to pray.

KARLA: I'll make it real short. The judge set tomorrow for the sentence. Now, you know, this is a death penalty state. And the judge could sentence Mr. Miller to die. Or he could send him to prison for the rest of his life.

MAGGIE: I'm praying.

KARLA: And as Mr. Miller's attorney, I'm asking that he be sentenced to prison, Maggie.

MAGGIE: I don't have no use for that man. I don't care what they do with him. I don't ever want to hear his name again.

KARLA: And the judge said ... ahh ... he said that he would leave it to the family about the death penalty. He said if someone from Tommy's family came forward at the hearing and said that Mr. Miller should not get the ...

MAGGIE: I said I didn't ever want to hear his name again.

KARLA: You've known Franklin Miller a long time.

MAGGIE: Too long.

KARLA: Thirty years, I think. I remember something from the file. I thought you might have some feeling of sympathy toward him.

MAGGIE: Towards him! I don't have no feeling of nothing towards him. Let him rot in a pit with birds pecking at his bones, for all I care.

KARLA: You don't care if he's executed?

MAGGIE: NO. NO. I DON'T CARE. AFTER WHAT HE DONE! You want me to care about THAT! I DON'T CARE. ALL I WANT IS MY TOMMY BACK. THAT'S ALL.

KARLA: Alright, Maggie. Okay. See, that's it, then. It's okay. I felt I had a duty to ask. Since that was the condition the judge set ... I had to try. I hope you understand.

MAGGIE: I don't understand nothing, lady. NOTHING.

KARLA: Karla. I'm Karla.

MAGGIE: You want to know what was I thinking that day, lady? I was thinking I was glad I didn't have some big time education so that I didn't have to stand up there like you and defend a dirty vile rotten old man that killed my thirteen year old boy. That's what I was thinking.

KARLA: I see. Sometimes it's not so easy. Especially ... I know this doesn't make much sense ... but Mr. Miller -- I mean I don't say that there was anything right about what happened -- but now I've gotten to know him. He's a friend ... in a way. Maybe I just hate to see people die. Especially clients. Kind of makes me feel like a failure. Like that big time education isn't worth a tire track in the mud.

MAGGIE: Comes with the territory, I imagine.

KARLA: I've never had it happen before. You know, that a client was sentenced to death. Can't make sense out of it.

MAGGIE: There's no sense in this world, lady. If there was any sense in this world, Tommy would be hollering out back right now.

KARLA: (Preparing to leave.) Yes. (Standing.) And one thing, Mrs. Denton ...

MAGGIE: I've had enough.

KARLA: I did want to say -- while I'm here, and all -- I want to say, I'm very sorry. About Tommy.

MAGGIE: You're a liar! (Turns as if to spit.)

KARLA: What? This is too much. I AM SORRY ABOUT YOUR SON. Good evening, then.

MAGGIE: (Grabbing her.) Why you telling me that now, lady?

KARLA: What do you mean?

MAGGIE: No body said that. (Emotionally) Not no body.

KARLA: Said what?

MAGGIE: 'Sorry.' I can't hardly believe it myself. Sure, he wasn't no saint. But nobody said they was sorry. Not the funeral man. Not the sheriff. Not the judge. Nobody sitting down there at the county. And nobody 'cept one church lady come knocking out here neither to say their sorries.

(KARLA reaches out to MAGGIE.)

KARLA: Maggie ... I am sorry. And other people -- were. People ... just plain act ... stupid ... sometimes.

MAGGIE: He had a little trouble. So'd his daddy, once or twice. We don't belong to no country clubs or nothing. But they don't have to treat us like we're some trash and it don't mean nothing to us ... do they?

KARLA: Listen to me: You didn't deserve to be treated that way.

MAGGIE: I just want to die, lady. I didn't tell no one this. Not even my husband. I just want to die as soon as have all those cold hearted people talking about my baby and asking questions and have Tommy gone like this.

KARLA: Please. I am so sorry. Oh God. I know ... how it hurts. It's going to hurt. Like a big ball in the middle of your stomach. But, it'll start getting smaller. Over time. Things will get better. Slowly. Believe me.

MAGGIE: What do you know? This sadness is so thick, I don't know where to put it. I never had nothing like this in my life.

KARLA: I ... had ... there was something ... just last year ... something like it.

MAGGIE: You had a child stabbed bloody?

KARLA: No. No, I didn't have that. It was something different.

MAGGIE: Then you couldn't know. Something different isn't the same.

KARLA: Of course it's not the same. I just know how the hurt feels. It's not the same. Was my little brother, Jack, actually, last year. It was different, of course, and well, he wasn't so little, but he was younger than me. And he got real sick, and they were talking about treatment and other help and ... there are things they can do for people ... you know, it's an epidemic and all, national ... and I don't know, well, he decided he didn't want to go through with it, he just gave up. He ahh ... he ahh ... went into the cellar and ... and ... and ... you ever seen anyone who's hung themselves? It's a hideous awful sight ... a ... horrible ...

MAGGIE: There, there. Stop now.

KARLA: ... and he didn't have to go that way. Not saying goodbye or anything. And I miss him so much. If he were alive, right now, today, I'd be calling him on the phone, crying my eyes out to him. And this is very hard on me ... with Mr. ... with my client and all.

MAGGIE: No ... No... Karla. It won't be so bad. I didn't mean to set you off. Shhh. Shhh. Calm down.

KARLA: (Straightening up.) Oh, this is so stupid. Here I am, supposed to be the big professional, and I'm sitting here blathering to you.

MAGGIE: That day ... that day ... when I looked at you. I saw you say you were sorry to me. I saw that in your eyes. You was the only one. And I was a-trying to say thank you.

KARLA: (Preparing to leave again.) I appreciate that. (Turns to exit.) Well, I'd better be taking my leave before your husband returns. He practically threw the couch at me the last time I came by.

MAGGIE: He's not so bad a man. Everyone hurts.

KARLA: Sure. I understand. (Starting to exit.)

MAGGIE: (Catches KARLA'S arm.) When would they do it? ... to ... him.

KARLA: Mr. Miller? Oh, I don't know. I'll still argue, tomorrow, on his behalf. You know, they'll be some people there. His mother, other people. And then there's appeals and all.

MAGGIE: She must be old by now, his mother.

KARLA: Oh, gee. (Looks in the file.) Doesn't say exactly. Seventies' I imagine. She's coming from West Virginia ...

MAGGIE: I know where she's coming from.

KARLA: Sure -- that's your country, too. Well, you probably know more than me. (Shakes MAGGIE'S hand.) Well, thank you for coming out on the porch.

MAGGIE: I bet your brother Jack walks right along side you sometimes.

KARLA: He does, sometimes.

MAGGIE: I bet he'd be telling you to remember that part where they talk about an eye for an eye and a tooth for a tooth.

KARLA: Jack wasn't much for religion.

MAGGIE: Yep. I bet Jack'd tell you that's one of the stupidest parts he'd ever heard. I told the preacher that one time too. I think that's stupid I said. That don't accomplish nothing. Just blood on both hands. That's what Jack would say, I bet.

KARLA: He might.

MAGGIE: He'd a probably say what about that part that says thou shalt not kill. What about that? How come nobody talks about that in court?

KARLA: Well, it's a matter of law, you know ...

MAGGIE: And when they wrote that 'thou shalt not' there wasn't no 'ceptions in there for this or for that. I bet he would tell you to bring those things up tomorrow.

KARLA: Well, sure. I can try.

MAGGIE: Good.

KARLA: Right.

MAGGIE: I'd like to come by and hear that. I don't have any fancy court clothes or anything, but, I'd like to know what the judge says to that. (KARLA turns to exit.)

KARLA: Yes, well .... (KARLA stops, wheels back to MAGGIE, pulls her jacket out of her bag and, puts it on the porch.) It's not new or ... but ...

MAGGIE: Oh, no. My husband might not approve any business like that. I'd have to ... well, I'd have to step out ...

KARLA: Well, I leave it to you. Jack always liked this jacket. He thought the color was calming. Maybe, I'll just put it here on the porch. Alright then. Thank you.

(KARLA now exits hurriedly.)

MAGGIE: (Alone, MAGGIE stands, thinks, picks up jacket, tries it on.) I'd like to know what that judge says to old Mrs. Miller. I'd like to know that.
```

---

## IC-0675: She Kills Monsters

- Title: She Kills Monsters
- Author (byline): Qui Nguyen
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Oct 2012
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR 1, TILLY, AGNES, NARRATOR 2, CHUCK, KALIOPE, LILITH, EVIL TINA, EVIL GABBI, ORCUS
- Teaser before the introduction: Yes
- Spoken words (computed): 2150
- Already set (do not supply): none

### Source block (context only)

```text
Author: Qui Nguyen
ISBN: 978-0573700569
Publisher: Samuel French, Inc.
Date (Month/Year): Oct 2012
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: One day as Agnes, a teacher at Tilly’s high school, is going through her sister’s things, she finds a notebook.

ACTRESS 2: A Dungeons and Dragons notebook

ACTRESS 1: It becomes her mission to find out more about her sister Tilly by deciphering the contents of that notebook.

ACTRESS 2: And thus a quest begins . . . a quest that forges a link between Agnes’ reality and Tilly’s fantasy.

TOGETHER: She Kills Monsters By Qui Nguyen
```

### Performance text (classify this)

```text
Suggested Roles: Actress 1: Narrator 1, Agnes, Evil Tina, Orcus/Ronnie

Actress 2: Narrator 2, Tilly, Chuck, Kaliope, Lilith, Evil Gabbi

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NARRATOR 1: (Pg 7-8) In a time before Facebook and Worlds of Warcraft, there once existed simply a game -- Forged by the hands of nerds and crafted in the minds of geeks. And here in the land of Ohio during the year of 1995, one of the rarest types of geeks walked the earth -- Tilly Evans. Lights up on TILLY, a teenage girl decked out in full D&D armor with a sword in hand. She is surrounded by a horde of goblin-like creatures. Suddenly they attack! TILLY slays each of the monsters with grace and efficiency. She stands poised over their dead bodies as the NARRATOR continues. . .

NARRATOR 1: But this story isn’t about her. . . This story is about her sister Agnes, the girl who never left home. . . Agnes Evans grew up average. She had average parents and grew up in the average town of Athens, Ohio with her little sister Tilly. Tilly however was anything but average.

TILLY: What are you doing?

AGNES: Talking on the phone. What are you doing?

TILLY: Trying to re-animate a dead lizard with the power of electricity.

AGNES: Oh, okay. . . WHAT!?!

NARRATOR 2: Being a bit more than half a decade apart in age, the two girls had very little in common. Agnes was into more typical things such as boys, music, and popular television programs

NARRATOR 1: While her sister Tilly became fascinated with the dark arts - magic, dragons, and silly costumes . . .

NARRATOR 2: As Agnes grew, she became more engrossed with transcending her averageness and made one grand wish on the night of her college graduation that she would forever regret.

AGNES: I wish my life was less boring.

NARRATOR 2: And so the Gods answered her wish by smiting down her loved ones in a single car crash.

NARRATOR 1: But this isn’t the story of those tragedies. It is a story about how Agnes, the girl who never left home, finally found a way out. . .

Lights come up on CHUCK, a nerdy teen working the counter of a “RPG Gaming Store”

CHUCK: (Pg 9-11) (Singing to himself - Agnes enters and pokes his shoulder which startles him) WHOA, WHAT THE . . .

AGNES: Sorry, I didn’t mean to scare you – I’m looking for a Chuck Biggs?

CHUCK: You’re looking at him! So what can I do for you?

AGNES: Rumor has it you know a thing or two about D&D. I have this thing. I’m not quite sure what it is.

CHUCK: Well, lemme checkity check it out! (AGNES hands CHUCK the notebook) It’s like a map for a D&D game. An adventure. – whoa, wait just a minute. Tillius the Paladin? Was this written by Tilly Evans?

AGNES: You know her?

CHUCK: You kiddin’, right? Every player here in Athens has been on a campaign with her. How’d you get ahold of this?

AGNES: She’s, um, my sister. So can you help me figure out what it all means? I want to play it. . .

TILLY: (Pg 13) (only Agnes can hear) You’re going to suck at this. You don’t even know the difference between a mage or a wizard. You’re going to die five seconds into it.

AGNES: Well, you’re already dead, so we’ll at least have that in common. Chuck. Go. (the scene changes to one of pure fantasy)

CHUCK: (Speaking all-wizard-y on a lower octave) Greetings, Adventurer! I am Chuck Biggs and I will be your Dungeon Master! (Pg 15) Welcome to the Quest for the Lost Soul of Athens. Your mission is find and free the Lost Soul before it is devoured by the dark forces of darkness forever.

TILLY: (Pg 14-15) Fine! If you’re serious about this, then I guess you’re going to have to meet the rest of the team.

AGNES: What team?

TILLY: Every adventurer has a party. This one’s mine. (The Actress playing Agnes portrays each member of the party as they are introduced: Suddenly, a leather-clad warrior LILITH appears -- red eyes, vampire fangs, with a very large battle axe) First up is Lilith Morningstar. Class: Demon Queen. She acts as our squad’s muscle -- a perfect combination of both beauty and brawn. (Next, a very pale, white-haired elf -- tall, lean, and armed with an wooden staff. She looks like a super model) Next up is Kaliope Darkwalker. Class: Dark Elf. Along with her natural Elvin athleticism and a**-kicking abilities, she’s also a master tracker and has a few magical surprises up her sleeves. And then there’s me. I’m the brains of this operation. Name: Tilly Evans aka Tillius the Paladin, healer of the wounded and the protector of lights. Class: Awesome! (both actresses do poses with their weapons as if they’re at a photo shoot)

TILLY: (Pg 16-17) Kaliope, any word on Orcus’s location?

AGNES: What’s an Orcus?

TILLY: Orcus is a demon overlord of the underworld. If there’s a lost soul, he’ll either have it or at least know where it is. So, Kaliope, location?

KALIOPE: The entrance to the cave of Orcus is at the next bend.

TILLY: Actually, Agnes, before we can go any further. We’re going to have to build you a character. I mean you can’t just walk around looking like that. You’re going to at least need a shield. . . And your alignment.

AGNES: My what?

LILITH: Are you good, lawful, chaotic, unlawful, evil?

AGNES: I’m a Democrat.

TILLY: No, what will be your character name?

AGNES: Agnes.

TILLY: Stop being an ass-hat, Agnes.

AGNES: No, I want to just use my name. Agnes.

LILITH: Fine, then it is decided, you are Agnes the Ass-hatted. (Pg 32-33) (Lilith kisses Tilly)

AGNES: Whoa! Wait just a minute! You two are a couple? (To Tilly) Oh, I get it. You two are dating because Tillius is a guy character.

TILLY: No. Tillius is a D&D name. I’m female, she’s female.

AGNES: So your character’s gay?

TILLY: Does that bother you, Agnes? Wow, I never took you for a homophobe.

AGNES: I’m not a homophobe! I thought I knew you, Tilly. At least good enough to know whether you dug boys or girls at this point in your life.

TILLY: You were busy.

AGNES: Not too busy to know this! Tilly, I’m your sister. I shouldn’t have to learn about you through a role-playing game.

TILLY: At least you’re getting to learn something about me.

NARRATOR 2: (Pg 18-19) And so it was that Agnes the Ass-hatted and Tillius the Paladin ventured forth into the dark dwellings of the truly evil in search for the lost soul of Athens. (The girls jump out from hiding with weapons drawn.)

TILLY: It is I, the great Paladin Tillius, healer of the wounded, defender of lights, and I have come here to free a soul. . . Mine.

AGNES: Wait, you’re the lost soul of Athens? Explosive lights and sound as two cheerleaders walk onto stage. They look like normal cheerleaders, except they have sharp teeth, bat wings, and blood all over their mouths. Clearly a scene Tilly experienced at school written into her D&D campaign

EVIL TINA: (Pg 35-36) (to Tilly) Were you just looking at me?

EVIL GABBI: I think the reason why she was looking at you, Evil Tina, is because she has the hots for you.

TILLY: That’s not true.

EVIL TINA: Are you saying I’m ugly?

TILLY: No.

EVIL TINA: Then do you think I’m pretty? Of course you think I’m pretty . . . I knew you were gay!

AGNES: (AGNES marches up to the two bullies) (Pg 37) And you two going to die! (Both cheerleaders smile and begin laughing. Their laughter consumes AGNES and TILLY. Their laughter becomes painful and then becomes agony)

EVIL TINA: We’ll see you around. Lesbians. (They skip away)

AGNES: Are you okay? (Pg 41) Did that sorta stuff really happen? I mean in real life?

TILLY: I was a dorky fifteen-year old closeted lesbian, what do you think?

AGNES: So how come you had to make a game to tell me all this?

TILLY: I didn’t want to tell you all this! This game was supposed to be private. *******

(Scene change back to the real world. Agnes is at school, working in her classroom. EVIL TINA and EVIL GABBI enter. Except they aren’t evil this time, they’re just students. No wings or horns or bloody mouths, just regular cheerleaders. And they’re super chipper and nice.)

EVIL TINA: (Pg 51-52) Hello, Miss Evans!

EVIL GABBI: Do you have a moment?

EVIL TINA: We’re selling Ads for this year’s yearbook and we were wondering if you’d be interested in buying an Ad? It could just be a “Congratulations to the Class of 95!” Or a dedication to a loved one who would be graduating this year. . .

EVIL GABBI: (whispers) TINA!

EVIL TINA: (to GABBI) Shhh. (to AGNES) So what do you think?

AGNES: You were in the same class as my sister, right?

EVIL TINA: We were both just devastated when we found out. I mean we didn’t hang out after school alot, but –

EVIL GABBI: We’d both consider her a very close friend.

AGNES: Is that right?

EVIL TINA: Not to be too bold, but I think buying a full page AD for Tilly would be. . . just amazing.

AGNES: Can I see your yearbook there? (Agnes violently throws it) GET THE HELL OUT OF MY CLASSROOM!!! (The two girls run out; Agnes calms herself) Am I going crazy?

TILLY: (appears from nowhere) That seemed really effective

AGNES: What am I supposed to do, Tilly? I can’t beat up students.

(Pg 57) Explosion. Evil Tina and Evil Gabbi are back in their evil forms. (TILLY and AGNES fall into defensive stances)

EVIL GABBI: Oh my God, Evil Tina, look! An impenetrable wall of losers.

EVIL TINA: (Pg 58) (they corner Tilly) Awww, look at the little nerd girl.

AGNES: Tilly, shoot them with a magic missile.

TILLY: (cowed) I can’t. I forgot the spell.

EVIL GABBI: Are you going to pee your pants.

EVIL TINA: Say good-bye, lezzie. (Pg 59) You can’t hope to beat us.

EVIL GABBI: We’re way too powerful for you.

KALIOPE: There’s only one way to beat a succubus.

AGNES: [I] challenge you. . . to a dance battle.

CHUCK: BONUS ROUND: AGNES VERSUS THE EVIL SUCCUBUS CHEERLEADER!!! Music fills the house as AGNES and EVIL GABBI go at it in a full-on cheerleader’esque dance battle. AGNES starts it out. She looks good. . . comedic and funny, but still good. EVIL GABBI is unimpressed by AGNES’s skills. She smiles, steps in and starts doing an elaborate Cheerleading/hip-hop fusion routine that completely kills it. Thinking she’s won, she raises her arms in victory. When she does, AGNES picks up her weapon and drives it through GABBI while she isn’t looking!

AGNES: (smiles coyly) What? You really thought we were gonna dance battle you to death. Wow, I guess my sister’s right. Cheerleaders are dumb. (Agnes kills them both then breaks into tears)

TILLY: (Pg 61) Stop. It’s just a game.

AGNES: I was getting to know you. I was just starting to get to know you.

TILLY: My character’s not dead.

AGNES: But you are. This is a stupid game and you’re not real and none of this matters because you died. I’m done. I’m done talking to ghost. *******

(Scene changes back to reality. Agnes is at home sorting through Tilly’s D&D things) AGNES:(Pg 62-63) (to audience) That game was all I had of her. Just a stupid character sheet and whatever she left scribbled out in that notebook. . . My memories are shit. This little nerdy girl who I never talked to, who I ignored, who I didn’t understand because she didn’t live in the same world as I did. Her world was filled with lesbian demon queens while mine . . . had George Michael and leg-warmers. I didn’t even know she didn’t like boys. I didn’t know her. That breaks my heart. (a knock at the door) What are you doing here, Chuck?

CHUCK: I just wanted to show you something. It’s something of Tilly’s.

AGNES: What? AGNES gets up and follows CHUCK. A door appears. CHUCK knocks on it.

CHUCK: (Pg 64-66) I just wanted you to meet some of Tilly’s friends. Ronnie, this is who I was telling you about. So is your sister around?

ORCUS: Yeah. Lemme get her. You guys can come in if you want, just don’t touch the TV, I’m recording Power Rangers! They enter his house.

NARRATOR 2: Ronnie (ORCUS) returns with his sister Kelly (KALIOPE). She’s wheel-chair bound.

KALIOPE: What? Do I have something on my face?

AGNES: Um, no, it’s just. . .You play D&D with these guys?

KALIOPE: Yeah, well. It was actually your kid sister that convinced me give it a shot. Your sister was awesome, Miss Evans. We loved her. We really miss her.

AGNES: Me too. (TILLY enters)

TILLY: What are you doing?

AGNES: I’m getting to know your friends.

TILLY: I know they’re geeky, I’m geeky, we’re all geeks.

AGNES: Why do you think I care about that stuff?

TILLY: Everyone else does or did. I mean until I died in a car crash and then suddenly, wow, I’m the most popular girl in school.

AGNES: Is that why all you guys play this?

TILLY: No, we play it because it’s awesome. It’s about adventures and saving the world and having magic. And maybe, in some capacity, it might have a little to do with wish fulfillment. Kelly gets to walk again and Ronnie gets to be super strong . . . and me? I get the girl. Lights come up on the “real life” high schooler LILITH. AGNES approaches.

AGNES: (Pg 66-67) Can we talk for a minute? Look, I know you’re not gay or . . . You were at her funeral.

LILITH: I mean, she wasn’t my girlfriend, but I always knew she was, you know, interested. Tilly was my first kiss. I’m pretty sure I was hers too. I thought you’d might want to know that about your sister. And Miss Evans - I loved her. (Lilith exits)

TILLY: (Pg 70-71) Good job.

AGNES: Tilly? (sadly resigned) You’re not real. You’re gone.

TILLY: But this story remains. And isn’t that all that life is - a collection of stories? This is one of mine. . .

(TILLY speaks the next lines, assuming the character voices that she created) AS KALIOPE: . . . and not just some story that I experienced like a party or a dance, but something I dreamt – AS

LILITH: Something far more personal and important than happenstance. This story came from my soul and by breathing life into it, who knows? AS ORCUS: Maybe a bit of my soul gets the chance to breathe for a moment once again. AS CHUCK: I love you, my sister. AS TILLY: I’m sorry I can’t be there. AS CHUCK: I have no idea why you had to experience this adventure alone without me. But I hope it gave you a glimpse into me the way I wanted you to see me – AS ORCUS: Strong... AS LILITH: Powerful... AS KALIOPE: And magical. AS CHUCK: Congratulations, you have finished the Quest for the Lost Soul of Athens.

NARRATOR 2: And so...Agnes the Ass-hatted accomplished her very first quest.

NARRATOR 1: Tilly was never forgotten, and eventually the world finally embraced nerds not as outsiders, but as awesome.

NARRATOR 2: Agnes moved out of that old house and brought the many memories of an average life with her.

NARRATOR 1: And this made her happy.
```

---

## IC-0676: Sickened

- Title: Sickened
- Author (byline): Julie Gregory
- Work: Not specified
- Publisher: Bantam Books, Inc.
- Publication date as stated: Sept 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS 2, JULIE, MOM, DOCTOR, NURSE
- Teaser before the introduction: Yes
- Spoken words (computed): 2119
- Already set (do not supply): none

### Source block (context only)

```text
Author: Julie Gregory
ISBN: 978-0553381979
Publisher: Bantam Books, Inc.
Date (Month/Year): Sept 2004
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: A young girl is perched on the cold chrome of yet another doctor’s examining table, missing yet another day of school.

ACTRESS 2: It’s four o’clock and she hasn’t been allowed to eat anything all day.

ACTRESS 1: Her mother, on the other hand, seems curiously excited. She checks her teeth once more for lipstick, and as the doctor enters, shoots the little girl a warning glance. This child will not ruin her plans . . .

ACTRESS 2: Munchausen by Proxy is a type of child abuse in which a parent exaggerates, fabricates, or induces symptoms of a medical condition in a child that leads to unnecessary and potentially harmful medical care.

ACTRESS 1: Julie Gregory was a victim . . . and this is her story

TOGETHER: Sickened by Julie Gregory
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: ACTRESS 1: Julie, Doctor

ACTRESS 2: Mom, Nurse

JULIE: (Pg 3) For starters, I was a sick kid. Bean-pole skinny, I bruised easy and wilted in a snap. Kids in school used to walk straight up to me and ask point-blank if I was anorexic. But I wasn’t; just sick. And Mom bent over backwards trying to find out what was wrong with me. It wasn’t just that I had a heart problem. It was everything rolled into one, bleeding together with so many indistinguishable layers that to get to the root of it was impossible, like peeling off every layer of an onion, and when I got old enough to peel the onion myself, every layer made me cry.

MOM: (Pg 4) Look, dammit, this kid is sick, all right? Just look at her. And so help me God, if she dies on me because you can’t find anything wrong with her, I’ll sue you for every sent you got.

JULIE: Her voice trailed after any doctor who said no more tests could be done, stalked him down the corridor, sliced through the silence of the hallway. (to Mom) Don’t worry, Mom. It’s okay. We’ll go find another one.

MOM: Look, I’m sacrificing my life to find out what the hell is wrong with you. So stop *screwing* it up when we get in here by acting all normal. Show them how sick you are, okay?

JULIE: (Pg 23) Today, I’m back at [the doctor] getting seen for my headaches. Mom and I sit in the examining room, waiting.

MOM: How do you act when you’re sick, Julie? Show me.

JULIE: (slouches, limbs dangling, tongue out and bottom lip away from her teeth, a glazed expression on her face)

MOM: That’s right. Now what do you think the doctor is going to say if he comes in here and you’re sitting up and all smiling? Do you think he’s going to believe me that you’re sick? You got to show him how sick you are. (Doctor enters)

DOCTOR: So you say Julie’s been running a fever along with some sore throats? (taking notes in Julie’s chart)

MOM: (Pg 26-27) Well, I’ve caught it up at a hundred and one, but it seems to be low grade all the time and she has these, oh, I don’t know what you’d call them, headaches, I guess, don’t you Julie?

JULIE: I look between both of them. What is a headache exactly? Is it when my eyes hurt? Is it when I’m dizzy on the bus? I’m trying to guess, hoping it’s the right answer. (to Mom and Doctor) I’m not really sure.

MOM: Jesus, Julie, we’ve been seeing you sick and you’ve been telling me you’ve had headaches in the car all this week. Remember when you’ve been carsick? (to Doctor) There’s got to be something wrong with a kid that doesn’t even remember how sick she was just yesterday. (to Julie) Julie, stop wasting the man’s time and tell him what’s going on with you. (threateningly) I mean it!

JULIE: (Pg 28-29) Another week has gone by and nothing has changed. Mom and I sit in [the doctor’s] office waiting for Dr. Phillips.

MOM: Now, we’re going to tell Dr. Phillips about the dull pains in your head, right about (pushes fingers into Julie’s skull, hard) here. I don’t want any kind of fiasco like we had the last time, okay? I’m the mom: I know what’s going on here. So if he asks you questions, you just let me answer.

JULIE: Dr. Phillips breezes in and apologizes for our wait. Mom gives him an update on my allergy diet and pulls out her list of new symptoms. I sit in my sick pose. As she runs down the symptoms, I know some of them aren’t true. (Pg 30) No, I don’t have a sore throat every day, just yesterday. No, my fever last night wasn’t way up to 102. No, I don’t go to the school nurse every single day . . . [In fact] (Pg 32) it was usually after Mom slipped the little white pill under my tongue that my migraines got worse.

MOM: I can tell you’ve got a headache coming on. Here, open up. Lift your tongue. Goooood.

JULIE: Sometimes I about threw up. Most times I just needed to climb back into bed . . . (Pg 50-51) [Three years pass and] when fifth grade begins, Dr. Phillips prescribes us more migraine medicine and gives us the names of specialists who can see me for the rest of my symptoms. He tells us we should [find] somebody who can handle a case that’s as complicated as mine’s getting. And then he leaves. He just walks right out before Mom is even done running down the list she brought.

MOM: I can’t believe that. Did you see him, Julie? He just walked out on us! Well, if he’s going to treat me like that, Jesus!

JULIE: (resigned) Don’t worry, Mom, we’ll just go find another one. (Pg 52) (to audience) That night Mom curls up on the sofa, with her grocery store reading glasses hanging on to the tip of her nose, cornering through the pages of the thick Medical Journal for Home Use Manual. (to Mom) Whatcha doing, Mommy?

MOM: Well, you’re sick again, hon, and this book is helping Mommy figure out what’s wrong with you. You got a lot of the symptoms in here, but there’s all kinds of tests that’ll help us rule out some of the more serious diseases.

JULIE: [Later that night] (Pg 84-86) the doorknob on my bedroom door slowly squeaks open. Mom tiptoes to the edge of my bed. That’s when I notice the gun in her mouth. (Julie enters flashback ad responds immediately with a look of horror) She looks at me with her tear-streaked, puffy face, her eyes terrified like an animal in a chute, and raises her hand to cock the trigger. “Mommy, Mommy, Mommy!” (to audience) I shoot from under the covers and start crying on cue. Mimic and match. If I mirror her with an appropriate response, she’ll be distracted from the gun.

MOM: (she slides the gun out of her mouth) You want me to kill myself, don’t you? You hate me. I’m such a bitch, such a nag as your father says, and you hate me, that’s what he says.

JULIE: She drops the gun to her lap. I cling around her like a baby monkey. (To Mom) Mom, if you don’t live then I can’t live. Okay? Okay? Who would take care of me when I’m sick; who would take me to the doctor? (to audience) I hang on to her, slipping the gun so lightly from her lap she doesn’t notice, sliding it under my blankets. (To Mom) It’s okay, it’s okay, Mom. (to audience) And the harder I cry, the less my beautiful mother, who I could never live a second without, does. And then she stops altogether, straightens up, gives my knee a little squeeze and says

MOM: (in an upbeat mood; cheerful) Hey, thanks for listening, Sis. You better get to sleep now, honey.

JULIE: And she leaves me on the edge of my mattress with a loaded gun under my covers. [*Spoken Transition -- A few weeks later]

DOCTOR: (Pg 97-101) There’s a substantial difference in Julie’s heart rate when she stands up from when she’s at rest, Ms. Gregory.

MOM: (to Julie) Tell her how out of breath you are, Julie. (to doctor) She’s always out of breath around the farm, Dr. Kate. Jesus! (slaps her knee) This explains everything. (to Julie) You look like you’re about ready to pass out, hon. Don’t you feel like you could pass out?

DOCTOR: I think we might have something for the hospital here, something that could be detected with simple EKG or a heart exam. They might even want to attach something called a Holter monitor on her overnight to see the longer rhythms of her heart. I’ll call over to the cardiac unit and get you set up.

MOM: Yess – Yeeeessss! (gleefully) Finally, we’re getting somewhere. (to Julie) I knew there was something major going on with you!

JULIE: We’re going to the hospital! At last, I’ll just take one medication that will fix everything. I’ll have friends, be in sports, go to movies. And I’ll be a real kid and not miss school anymore. I’ll do good in school like before I got sick. I’m [only] failing because there’s always something wrong with me. [*Spoken Transition -- After the cardiac tests]

DOCTOR: (Pg 101) Well, Ms. Gregory, we’ve got good news. The Holter monitor shows no significant findings that lead us to believe Julie has a heart condition requiring further tests.

MOM: What? What do you mean, you can’t find anything. This kid had a racing heart and was out of breath all the time. Are you trying to tell me that this kid is normal? That I’m making this up? Well, let me tell you. I’m going to find a doctor competent enough to find out what’s wrong with her, you understand me?

JULIE: (Pg 104-105) The older I got, the worse I got. My possible conditions expanded to include genetic disorders and heart valve malfunctions. And the medications to treat them piled up in the kitchen cabinets. Sometimes I don’t take any, sometimes I get a double dose. I just feel sick all the time. Queasy, nauseated, clammy, stupid. . . By the time I was in Junior High, Mom decided I was allergic to a lot of things.

MOM: Julie, what the heck are you doing with those [eggs]? You know you’re allergic.

JULIE: I slide the eggs back and reach for the bacon.

MOM: At-at-at, we just got done telling Dr. Kate how meat makes you sick. Why don’t you just have a bowl of Sugar Pops? But use the powdered milk, just enough to get them wet, you could be lactose intolerant.

JULIE: (Pg 111) How long can you starve without side effects? If everyone around you tells you you’re sick, if they keep testing you for what’s making you sick, do you think, when you’re thirteen, that you aren’t? You feel sick, right? You can’t keep up; you’re tired. Is it the wrong mediation that makes you sick? Or the three different kinds you take all at once? . . . . (Pg 113-114) We’re on our way to a new cardiologist. This will be the third and if he can’t find anything, Dr. Kate says it’s probably not my heart.

MOM: I’ll show those goddam no-good sons a bitches at the hospital that I’m not crazy. You are sick, goddammit, you’ve got a heart problem. (glaring at Julie) C’mon now, let’s get in there, and I mean now, goddammit. You are going to tell him what’s wrong with you. Sharp chest pain. Shortness of breath. You got it? [*Spoken Transition -- So more tests are run and when the results come back . . . ]

DOCTOR: (Pg 115-116) Well, it looks like what we’ve got here is a possible case of periodic rapid heart action.

MOM: Does that mean we’ll have to go in for open-heart? I mean seriously, I’m not opposed to it if we can really find out what’s going on here. I’ve been reading up on a new pediatric valve syndrome, and . . .

DOCTOR: Oh, no, I don’t think we’re going to need that. What we really should do is some more tests under the close eye of hospital staff. Could we get Julie into Ohio State for a week and run a comprehensive assessment? [*Spoken Transition -- After 4 days in the hospital]

NURSE: (Pg 121-124) We’re going to have to shave you now, honey. Down here. (pats for Julie’s pubic bone)

JULIE: What? I’m done, I’m going home. I don’t have anything down there! (covering her private parts) I’m here for my heart!

NURSE: Tomorrow they’re going to make a little incision in the vein of your arm and the artery of your thigh and run some electrical connectors into the values of your heart so they can see it on TV.

JULIE: (to audience) This has got to be a mistake. How did this happen? They’re going to cut me. (breath quickens, as Julie’s eyes widen in horror – To nurse) You, you can’t do this to me. You can’t do it . . . My mother is making it up! (long horrified pause then to audience) I can’t believe I blurted that out. My mother loves me. There’s something wrong with me. If I wasn’t sick the doctors wouldn’t keep trying to fix me . . . Maybe I was acting sicker because [mom] slammed my head against the inside of the window on the way home if I didn’t show them how sick I was.

NURSE: (puzzled) Be back in a sec. Let me see what’s going on.

JULIE: Mom’ll be furious! . . . I don’t care. I can run away. Find a new family. . . . [No,] Mom knows what she’s doing. She’s the one who sees my symptoms.

(Pg 131) Heart surgery, iodine injections, tubes shoved, slits sliced, blood drawn. These things change a kid. You forget what you were like before they cut you, before they shaved you. You only look to the future when they’ll find what’s wrong so it can all be over; the tests, the trying, the meds you swallow without knowing why.

[Today, as an adult] (Pg 221-222) I cry from the guilt of betraying my mother, for not keeping the shroud of her secrets. I have been writing about what it feels like to be cut open while your mother’s tight, thin smile mouths, “Doctor’s orders, honey.” And to believe you are genuinely ill because that is what everything in your world mirrors back to you. I still told myself that it was okay, it really wasn’t that bad . . . [after all,] if a doctor couldn’t decipher what she did, how could I?
```

---

## IC-0677: Small Great Things

- Title: Small Great Things
- Author (byline): Jodi Picoult
- Work: Not specified
- Publisher: Ballantine Books
- Publication date as stated: Oct 2016
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: RUTH, KENNEDY, ACTRESS 2, TOGETHER, ACTRESS 1, PROS. ATTORNEY
- Teaser before the introduction: Yes
- Spoken words (computed): 2373
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jodi Picoult
ISBN: 978-0345544957
Publisher: Ballantine Books
Date (Month/Year): Oct 2016
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Ruth Jefferson is a labor and delivery nurse with more than 20 years’ experience. ACTRESS 2: During a shift, she begins a routine checkup on a newborn, only to be told a few

minutes later that she’s been reassigned. Why?
```

### Performance text (classify this)

```text
NOTE: This cutting asks one student to portray 2-characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actress 1: Kennedy and Pros. Attorney Actress 2: Ruth

RUTH: (Pg 323-324) (to audience) We all do it, you know. Distract ourselves from noticing how time’s passing. We throw ourselves into our jobs. We fill up our gas tanks and do the grocery shopping so that the weeks look the same on the surface. If you only see the path that’s right ahead of you, you don’t obsess over when the cliff might drop off. Some of us never learn. And some of us learn earlier than others. (Deep breath in through her nose, she holds it and then releases it through her mouth)

KENNEDY: (Pg 326) (to audience) Bad things happen to good people every day. (Pg 195) (to Ruth, breezily) Well, first, do you prefer the term black or African American or people of color?

RUTH: (Beat) People of color.

KENNEDY: Frankly, I don’t even see color. I mean, the only race that matters is the human one, right? (Ruth presses her lips tightly together)

ACTRESS 1 in the voice of the father, TURK BAUER: (Pg 21)“I don’t want her or anyone who looks like her touching my son!” (silent beat)

ACTRESS 2: The hospital complies and flag the baby’s chart

TOGETHER: (Pg 43) NO AFRICAN AMERICAN PERSONNEL TO CARE FOR THIS PATIENT

ACTRESS 1: But the next day, the baby goes into cardiac distress while Ruth is alone in the nursery. She hesitates before performing CPR and, as a result, is charged with murder.

ACTRESS 2: Kennedy McQuarrie, a white public defender, takes her case, and insists that mentioning race in the courtroom is NOT a winning strategy. (both shake their heads and sigh)

ACTRESS 1: (Pg 464) Yes, talking about racism is hard to do,

ACTRESS 2: And yes, we stumble over the words - but we need to have this discussion . . .

ACTRESS 1: Because then, more will overhear, and - I hope - the conversations will spread.

TOGETHER: Small Great Things by Jodi Picoult

***As the trial concludes***

KENNEDY: (Pg 392-395) I don’t think you should get on the stand.

RUTH: You promised . . . You promised I could say my piece.

KENNEDY: [The judge] threw out the murder charge. The worst-case scenario – a conviction of negligent homicide carries almost no jail time . . . and honestly our medical evidence was so strong that I’d be shocked if the jury doesn’t acquit. We’ve created reasonable doubt. That’s all we have to do to win. The jury hands back the verdict, and you go get your job back. You get to pretend this never happened.

RUTH: You think I can pretend this never happened? I see this every day, everywhere I go. You think I’m going to just walk in and get my job back? You think I’m not always going to be that black nurse who caused trouble.

KENNEDY: Ruth, I’m 99 percent sure this jury is going to find you not guilty. What more could you possibly want?

RUTH: (crosses her arms in determination) You still have to ask?

KENNEDY: (to audience) I know what she is talking about. Namely, everything I refused to talk about in court: what it is like to know that you are a target, because of the color of your skin. What it means to work hard, to be an impeccable employee, and have none of that make a difference in the face of prejudice.

RUTH: I know how the law works, Kennedy. You have to put me on the stand if I ask you to. So I suppose the question is: Are you going to do your job? Or are you going to be just one more white person who lied to me?

KENNEDY: What the hell? Now is not the time to stand on principle. If you get on the stand and start talking about race, you’ll erase the lead we currently have. You’ll be talking about issues that will alienate [the jury] and make them uncomfortable. Plus, the fact that you’re upset and angry . . .

RUTH: (Pg 407-408) I am angry. I have been angry for years. I just didn’t let it show. 365 days a year, I have to think about not looking or sounding too black, so I play a role. It’s exhausting. It’s so goddamned exhausting. But I do it, because I don’t have bail money. I do it because I have a son. I do it because if I don’t, I could lose my job. My house. Myself. So instead, I work and smile and nod and stay silent and pretend to be satisfied, because that is what you people want – no – need me to be. And the great, sad shame is that for too many years of my sorry life, I have bought into that farce. I thought if I did all those things, I could be one of you. (beat) You told me you could represent me, Kennedy. You can’t represent me. You don’t know me. You never even tried. (deliberate beat – then with conviction) (Pg 395) You are putting me on that stand tomorrow or (Pg 408) you’re fired.

KENNEDY: (to audience) (Pg 395) And just like that, I know I’m going to lose this case.

**** The next day in court – Kennedy calls Ruth to the stand ****

KENNEDY: (Pg 401-404) When did you next see the baby?

RUTH: Saturday morning. I was in the nursery when the baby’s new nurse brought him in for a circumcision. I assumed it all went normally. Then Corinne grabbed me and asked me to watch over him because another one of her patients had to be rushed to the OR. Protocol required that the baby be monitored.

KENNEDY: When you first saw the baby, how did he look?

RUTH: Beautiful . . . But a few moments later I saw that his skin was ashen. I could see he was having trouble breathing.

KENNEDY: What did you do in that instant, Ruth?

RUTH: I started tapping his feet, trying to get him to respond.

KENNEDY: When you’d been told by your supervisor to not touch that baby?

RUTH: I had to . . . It’s what any good nurse would do. But I heard footsteps. I didn’t know what to do. I thought I’d get in trouble if someone saw me interacting with the baby . . . so I wrapped him up again and stepped back. Marie walked into the nursery. She asked me what I was doing. (long pause) I said I was doing nothing.

KENNEDY: You lied . . . when you were questioned by the police, you stated you did not engage in any resuscitative efforts for that baby. Why?

RUTH: I was afraid I was going to lose my job. Every fiber of my being told me I had to help that infant . . . but if I lost my job . . .

KENNEDY: So you basically faced either assisting in malpractice, or violating your supervisor’s order?

RUTH: It was a lose-lose situation. The code team was called in. My job was to do compressions. I did my best, we all did, but in the end it wasn’t enough. (softly at first, but with a growing bitterness) It’s funny. You think you’re a respected member of a community – the hospital where you work, the town where you live. But it was just an optical illusion. I was never a member of any of those communities. I was tolerated, but not welcomed. I was, and will always be, different from them. And because of the color of my skin, I will be the one who’s blamed.

KENNEDY: Nothing further . . .

PROS. ATTORNEY: (Pg 405-407) (approaching the witness box) At the moment that baby died deep down, you didn’t really give a damn, right, Ruth?

RUTH: Of course, I did!

PROS. ATTORNEY: (aggressively, voice rising as she physically moves into Ruth’s space) Ah, but this was the baby of a white supremacist. The baby of a man who called into question your ability to do your job simply because of the color of your skin. You resented Turk Bauer, and you resented his baby, didn’t you?

RUTH: (as the Pros. Attorney continues, overlapping) You’re wrong . . . I never thought that . . .

PROS. ATTORNEY: Or maybe you were thinking: This baby doesn’t deserve my help. His parents don’t want me touching him because I’m black, and they’re gonna their wish.

RUTH: (growing more and more agitated) That’s not true . . .

PROS. ATTORNEY: (Still on the attack) You were thinking: I hate his racist parents! Or maybe it was I hate this baby because I hate his racist parents.

RUTH: (holds her hands to her head) No! I was thinking that baby was better off dead than raised by him (she points to Turk Bauer –realizes what she has done and places a shaking hand over her mouth . . . silence) *****

KENNEDY: (Pg 407) (to audience) I grab Ruth’s wrist as soon as we are dismissed and drag her to the conference room. (angrily to Ruth) Congratulations. You did exactly what you weren’t supposed to do, Ruth. Are you happy you got up on the stand to testify? All the jury is going to see now is an angry black woman. One who was so pissed off and vengeful that I wouldn’t be surprised if the judge regrets dismissing the count of murder. You gave those jurors every reason to believe you were mad enough to let that baby die before your eyes.

RUTH: (sneering) Look at you. You’re so proud of being a public defender and working with people of color. (breathing heavily) Prejudice goes both ways, you know. There are people who suffer from it, and there are people who profit from it. Who died and made you Robin Hood? Who said I ever needed saving. Here you are on your high horse, telling me I screwed up this case that you worked so hard on; patting yourself on the back for being an advocate for a poor, struggling black woman like me . . . but you’re part of the reason I was down on the ground to begin with. (she exits)

KENNEDY: (Pg 415) (frustrated, angry – she calms herself and reflects) Maybe I’m wrong. I’ve spent months telling Ruth that a criminal lawsuit is no place to bring up race. If you do, you can’t win. But if you don’t, you are perpetuating a flawed system, instead of trying to change it. That’s what Ruth has been trying to say, but I haven’t listened. She’s brave enough to risk losing her job, her livelihood, her freedom to tell the truth, and I’m the liar. I told her race isn’t welcome in the courtroom, when deep down I know it’s already there. It always has been. Just because I close my eyes doesn’t mean it’s gone away . . . Ruth accused me of wanting to save her. But she doesn’t need saving. Who am I to give advice when I haven’t lived her life?

**** The following day – Kennedy’s Closing argument****

KENNEDY: (Pg 428-429) Ladies and gentlemen, I told you when we started this case that it was about Ruth Jefferson being presented with an impossible choice: to do her job as a nurse, or to defy her supervisor’s orders. But this case is about a lot more. Out of all the people who interacted with Davis Bauer during his short life, only one is being charged with a crime: Ruth Jefferson. I spent an entire trial skirting a very important question: Why?

RUTH: (Pg 49) (as Kennedy gives her closing arguments, Ruth speaks her mind to the audience) Are we gonna talk about it, or are we gonna pretend nothing’s wrong? (Pg 43) NO AFRICAN AMERICAN PERSONNEL TO CARE FOR THIS PATIENT

KENNEDY: (Pg 429) Ruth is black. That rubbed [the baby’s father] the wrong way. He can’t stand black people, or Asian people, or gay people, or anyone who isn’t like him. He set into motion a chain of events that would lead Ruth to becoming a scapegoat for the tragic death of his son. I don’t think it’s right to ignore the truth any longer.

RUTH: (Pg 170) They put me in chains. Just like that, they shackle my hands in front of me, as if that doesn’t send two hundred years of history running though my veins like an electric current. As if I can’t feel my great-great-grandmother and her mother standing on an auction block. They put me in chains, and my son – who I’ve told, every day since he was born, You are more than the color of your skin – my son watches.

KENNEDY: (Pg 431) I bet you feel uncomfortable right now. You know, so do I. It’s hard to talk about this stuff without offending people, or feeling offended.

RUTH: (Pg 238) You say you don't see color … but that's all you see. You're so hyperaware of it, and trying to look like you aren't prejudiced, you can't even understand that when you say race doesn't matter all I hear is you dismissing what I've felt, what I've lived, what it's like to be put down because of the color of my skin. (beat)

KENNEDY: (Pg 430-431) [You see] There is a difference between active and passive racism. Active racism is telling a nurse supervisor that an African American nurse can’t touch your baby. It’s snickering at a black joke. But passive racism? It’s noticing there’s only one person of color in your office and not asking your boss why. It’s reading your kid’s fourth-grade curriculum and seeing that the only black history covered is slavery, and not questioning why. It’s defending a woman in court whose indictment directly resulted from her race. . . and glossing over that fact, like it hardly matters.

RUTH: (to Kennedy, who continues unaware of Ruth) (Pg 237) You told me this lawsuit isn’t about race. But that’s what started it. And it doesn’t matter if you convince the jury I’m the reincarnation of Florence Nightingale—you can’t take away the fact that I am Black. The truth is, if I looked like you, this would not be happening to me.

KENNEDY: (Pg 430) I know you’re thinking: I’m not racist. I doubt there are many of you who believe that black people are so inferior they should not even be able to touch a white baby. But even if we took every white supremacist on the planet and shipped them off to Mars, there would still be racism. That’s because racism isn’t just about hate. We all have biases, even if we don’t think we do.

RUTH: (to audience) (Pg 43) I don’t have a problem with white people. I live in a white community; I have white friends; I send my son to a predominantly white school. I treat them the way I want to be treated – based on their individual merits as human beings, not on their skin tone.

KENNEDY: (Pg 431) (sighs) If you’ve asked yourself what this trial is really about, you know it’s more than just whether Ruth had anything to do with the death of one of her patients. In fact, it has very little to do with Ruth. It’s about systems that have been in place for four hundred years. Systems meant to make sure that people like Turk Bauer can make a heinous request as a patient, and have it granted. Systems meant to make sure that people like Ruth are kept in their place . . .

RUTH: (Pg 432) (stunned) After months of telling me that race doesn’t belong in a court of law, Kennedy McQuarrie took the elephant in the room and paraded it in front of the judge. She squeezed it into the jury box, so that those men and women couldn’t help but feel the pinch. What Kennedy said – it’s been the narrative of my life . . . but I could have screamed it from the rooftops, and it wouldn’t have done any good. For the jurors to hear it, really hear it, it had to be said by one of their own.
```

---

## IC-0678: Sold

- Title: Sold
- Author (byline): Patricia McCormick
- Work: Not specified
- Publisher: Hyperion
- Publication date as stated: Sept 2006
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS 1, ACTRESS 2, LAKSHMI, AMA, FATHER, BAJAI, AUNTIE, UNCLE, MUMTAZ, OLD MAN, SHAHANNA, PUSHPA, ANITA
- Teaser before the introduction: Yes
- Spoken words (computed): 1673
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patricia McCormick
ISBN: 978-0786851713
Publisher: Hyperion
Date (Month/Year): Sept 2006
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 2: Statistically Nepal is one of the poorest countries in the world. Desperate to survive, families feel forced to extreme measures to survive. Each year, nearly 12,000 Nepali girls are sold by their families into a life of sexual slavery in the brothels of India. Meet Lakshmi. She is 13 years old and this is her story. Sold by Patricia McCormick
```

### Performance text (classify this)

```text
Suggested Roles:

ACTRESS 1: Lakshmi,

ACTRESS 2: Ama, Father, Bajai, Auntie, Uncle, Mumtaz, Old Man, Shahanna, Pushpa, Anita

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

*LAKSHMI: (Pg 8) My stepfather's arm is a withered and useless thing. Broken as a child when there was no money for a doctor, his poor mangled limb pains him during the rainy months and gives him great shame. No one, he says, will hire a one-armed man. *Ama says we are lucky we have a man at all. She says I am to honor and praise him, respect and thank him for taking us in after my father died.

LAKSHMI: (Pg 48-49) I put the baby in a basket on my back and go about my chores. [Ama’s] steps are slow and heavy, and she stops often in her work to shake her head and sigh. At noon, I warm the remains of yesterday's soup, feed it to the baby, then tighten my waistcloth so my own hungry stomach will think it is full. Then I go in search of Ama and find her weeping. (to mother) "What is it, Ama?" Ama wipes her cheek with the hem of her shawl.

AMA: Your stepfather has said you must go to the city and earn your keep as a maid.

LAKSHMI: (to mother) “This is good news, Ama," . . . (to audience) my voice full of a boldness I did not know I had. (to mother) “There will be one less mouth to feed here, and I will send my wages home." (Pg 52-55) (to audience) The next morning my stepfather brings me to Bajai Sita's store.

FATHER: (to Bajai) Lakshmi wants to go to work in the city.

BAJAI: (to Lakshmi) Are you willing to do whatever is asked of you?

LAKSHMI: I nod. She goes behind a curtain and returns with the stranger in the yellow dress. The woman looks me over head to toe, then addresses my stepfather.

AUNTIE: How much do you want for her?

LAKSHMI: My stepfather squints. He takes in the costly fabric of the woman's dress, the baubles on her ears, the silver bangles on her wrist. "One thousand rupees," he says. There are not that many rupees in the world!

AUNTIE: (circling and inspecting Lakshmi) She has no hips. And she's plain as porridge. I'll give you five hundred.

LAKSHMI: I do not understand. I can carry a load of firewood so heavy it would put a man to shame, and my legs are sturdy enough to climb the mountain a dozen times in one day. What does it matter that I have no hips yet? My stepfather says he knows the going rate for a young girl like me.

FATHER: (to Bajai) No less than eight hundred.

LAKSHMI: My stepfather counts the money, then counts it again.

BAJAI: (to Lakshmi) Your family will get nothing, not one rupee, if you do not obey your new auntie. Do you understand?

LAKSHMI: (to audience) I don't. I don't understand at all. A great deal of money has just been paid for work I have not yet done. But I nod. (Pg 72-73) Auntie takes me into one of the rooms.

AUNTIE: (disdainfully) Take off those filthy hill clothes.

LAKSHMI: She holds out a pink dress of cloud fabric and a pair of shoes. I cannot imagine how I will walk freely in such a long, flowing gown, or how I will be able to haul the firewood and scrub the floors in such a fine and flimsy dress.

TRANSITION

ACTRESS 2: And so Auntie takes Lakshmi to a larger village where once again she is Sold.

LAKSHMI: (Pg 74-75) Auntie is speaking to a man in a tongue I do not understand. It seems as though they are talking about me now. The man points to me and asks Auntie a question. The answer, as best I can tell, is the number 12. "How old are you?" he says in my language. I tell him I am thirteen. He wheels around and slaps Auntie across the face, and she turns from a woman of queenly bearing to a frightened child. I fall to my knees and beg the man to forgive me.

Auntie names a price as high as a mountain. The man spits. Auntie goes high. The man goes low. I do not know what they have agreed to. But I do know this: he gives her nearly enough money to buy a water buffalo. TRANSITION

ACTRESS 2: Alone with yet another stranger, Lakshimi still believes she is being taken to her new job as a maid in the large Indian city of Kolkata.

LAKSHMI: (Pg 90-91) Finally, we tum down an alley and arrive in front of a metal gate held fast with a heavy chain. Uncle takes a key from his vest, opens the lock, and hurries me inside. This place is dark as a cave, and it smells of liquor and incense. As my eyes adjust, I see a dozen sleeping girls, some in the comers, some on rope cots. (to Uncle) “What kind of place is this?"

UNCLE: Happiness House. Auntie Mumtaz will explain it all to you.

LAKSHMI: In the weak morning light, I see that the girls are wearing dresses of every color. They have heavy silver bangles on their wrists and ankles, and earrings of gold and jewels. Their eyes are painted with black crayon, and their lips are drawn on like red chilis. (Pg 92-94) Inside a darkened chamber, a fat woman in a purple sari lounges on a cot. She has folds of flesh like roti dough at her waist, and a face as plump as an overripe mango. She surveys me head to toe, then spits.

MUMTAZ: How much?

UNCLE: Fifteen thousand.

LAKSHMI: Uncle goes high, the woman goes low. Eventually Uncle shrugs and gives up. The woman takes a record book out from inside the folds of her dress. She writes down the number 10,000. (long beat) I don't know why I am in this strange house. It seems as though this Auntie Mumtaz is my new mistress. She is a strict one, to be sure, but I will prove myself to her. And then my mother will have a new dress, shoes for the cold season, even a new shawl made of the finest yarn. My little brother will have fruit and curds twice a day and a jacket of yak fur. (Pg 102-104) Mumtaz studies me.

MUMTAZ: Are you ready to go to work?

LAKSHMI: I nod and say yes, then nod again, although I do not understand how these city people do their chores in such fine clothes. I follow Mumtaz down a hallway lined with tiny rooms. We pass by girls sitting cross-legged on the floor. Girls drawing on tiger eyes. Girls spraying themselves with flower water. We go up some stairs, down another hallway, then into a room where an old man is lying on a bed. His skin is yellow and he has tufts of hair poking out from his ears. Mumtaz speaks kindly to him and I wonder if he is sick. Mumtaz points to me and says something to the old man. He licks his palm and smoothes down his hair. Something is not right here. I don't know what is going on, but it is not right, not right at all. Mumtaz pats the edge of the bed.

MUMTAZ: Don't be afraid. Come here, now.

LAKSHMI: I don't move. Her voice turns hard.

MUMTAZ: Get over here, you ignorant girl.

LAKSHMI: Then Mumtaz flies at me. She grabs me by the hair and drags me across the room. She flings me onto the bed next to the old man. And then he is on top of me, holding me down with the strength of ten men. He kisses me with lips that are slack and wet and taste of onions. His teeth dig into my lower lip. Underneath the weight of him, I cannot see or move or breathe. He fumbles with his pants, forces my legs apart, and I can feel him. I gasp for air and kick and squirm. He thrusts his tongue in my mouth. And I bite down with all my might.

OLD MAN: Aghh!

LAKSHMI: . . . and I am running. Running down the hall, past the other girls, losing my fancy city shoes along the way. TRANSITION

ACTRESS 2: But this is only the beginning; starved, beaten and drugged, Lakshmi is eventually broken and moved from a locked room into the general population of girls. She learns from them everything she needs to know to survive.

LAKSHMI: (Pg 141-143) While Anita and Pushpa stand in front of the mirror, painting their faces, Shahanna explains everything to me.

SHAHANNA: Before, when you were in the locked room, Mumtaz sent the customers to you. Now, you must do what it takes to make them choose you. Tell the customers that you are 12 or Mumtaz will beat you senseless. Do whatever the customer asks of you. Otherwise, he will beat you senseless. Then he will do whatever he likes and leave without paying.

PUSHPA: Always wash yourself with a wet rag after the man is finished. This will keep you from getting a disease. Once a month a government woman comes to the back door with a basket of condoms. Take a handful and hide them under your mattress. If an old man is at the door, bat your eyelashes and act the part of a little girl. He will pay extra for this. Press your shawl to your nose with the back of your hand when you must bring a dirty man to your bed. He will leave nothing but his smell, the stink of sweat, and hair oil and liquor and man. But you can use your shawl to block the worst of it.

LAKSHMI: Anita turns away from the mirror, transformed from a crooked-faced country girl into a tiger-eyed city woman.

ANITA: There is another way to use a shawl.

LAKSHMI: I cannot tell from her always-frowning face if she is being kind or cruel.

ANITA: [The] new girl, the one in your old room . . . Yesterday morning Mumtaz found her hanging from the rafters. (long beat)

LAKSHMI: (Pg 192) A few days later I pass by a mirror. The face that looks back is that of a corpse. Her eyes are empty. She is old and tired. Old and angry. Old and sad. Old, old, a hundred years old. I speak to her. "My name is Lakshmi," I tell her. "I am from Nepal. I am 13 years old."
```

---

## IC-0679: Something Happened Here

- Title: Something Happened Here
- Author (byline): Madeleine Martin
- Work: More One-Act Plays for Acting Students
- Publisher: Meriwether Publishing
- Publication date as stated: July 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BECKY, PAM
- Teaser before the introduction: No
- Spoken words (computed): 1306
- Already set (do not supply): none

### Source block (context only)

```text
Author: Madeleine Martin
Book: More One-Act Plays for Acting Students
ISBN: 1566080878
Publisher: Meriwether Publishing
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
BECKY: As children, we’re taught that when we’re hurt, we need to call for help

PAM: But what if you don’t realize you’re hurt?

BECKY: or can’t admit that you’re hurt?

PAM: Who will believe you

BECKY: when you don’t even believe it yourself?

BOTH: “Something Happened Here”

PAM: by Madeleine Martin
```

### Performance text (classify this)

```text
BECKY: (Entering, followed closely by PAM) I am so mad!

PAM: But you're sure you're OK?

BECKY: I said I'm OK, OK? I'm just ... I dunno ... mad. (Pause) I dunno.

PAM: Let's see if there's anything ta drink around here. Maybe it'd ... calm you down ... or somethin'. (BECKY stares blankly at PAM. After a pause, PAM goes into the kitchen. From the kitchen) Is there any whiskey or vodka in here? Becky? Where does Rob keep his booze? Becky? (PAM returns to find BECKY just standing and staring.) Becky!

BECKY: (Jumping) Whaaa ... Jeez, Pam! Don't sneak up behind me like that. What are ya tryin' ta do, anyway...

PAM: I wasn't sneaking. I was just askin' ya where Rob keeps his booze.

BECKY: Booze? Oh. I dunno. Check the tall cupboard. Beside the range. Or maybe the cupboard above the fridge. I dun no. (PAM disappears into the kitchen again. BECKY sinks into a chair. She sighs heavily and drops her head into her hands.)

PAM: (Entering with a six-pack of beer) Look what I found... Becky? Are you ...

BECKY: Don't. Do not ask me again or I swear I will scream. (Seeing the beer) Great. Beer. I shoulda known he'd only have beer in this place. Whatdaya expect from a grease monkey. Cars - and beer.

PAM: Hey, at least it's somethin'. Here. Have one.

BECKY: (Reluctantly) Thanks.

PAM: Whatsa matter? Do ya think he'll mind if we drink it?

BECKY: I don't know. I don't really care. And I don't think he'll care either. He ... "loves me," ya know? (She slumps back and winces.) Oh, ouch!

PAM: See? You are hurt! I knew it. Maybe we should call the hospital.

BECKY: Right! And tell 'em what?! Tell 'em ... Oh, you bet! (She tries to open her beer.)

PAM: My God, Beck, you're shakin' like a leaf. Gimme that. I'll open it for ya.

BECKY: I can open my own beer! (BECKY twists the cap. It doesn't respond. She twists harder. Still nothing.)

PAM: Maybe we should call the police.

BECKY: And tell em what?! "Come on over an open my beer?" Besides, what are they gonna do... now. I'm just... "very angry" - as my mom would say... that's all. (The beer cap suddenly responds and some of the beer foams onto the carpet.) Oooops! Sorry abut that, Rob. Got some beer on your carpet there!

(She smiles at PAM.)

PAM: (Sipping her beer) I was so scared ... when you left, ya know? I didn't know what ta do.

BECKY: I don't wanna talk about it. It's over.

PAM: But it's so awful.

BECKY: Yeah, it's awful. But it's over. It was all a big mistake. A big filthy mistake.

(She looks at her hands.) And my hands're filthy! (She puts her beer down and goes into the kitchen to wash her hands.)

PAM: I mean, Becky? Don't ya think ya should tell someone? I mean, maybe just call someone .., like, anonymously... or something?

BECKY: (From the kitchen) Just shut up, Pam. The last thing I need right now is to start makin' anonymous phone calls - from my boyfriend's house. (She comes back into the room drying her hands.) That would get everybody involved all over the place. My mother. My dad. Your mother. Think about it. What're we gonna tell 'em when they start sayin', "Well I thought you were spending the night at Pam's." "No, Pammy said they were spending the night at Becky's."

PAM: (Looking at her beer. Quietly) I know. It just seemed like a good plan, ya know, with Rob outta town and all. I mean, it's not like he's here or anything. And I thought there'd be a kegger or somethin'. It was all a dumb idea I guess.

BECKY: Yeah. Dumb. (She sits and sips her beer.) This stuff tastes like horse urine or something. I hate beer. Is it hot in here to you?

PAM: Hot?

BECKY: Or cold? Maybe it's cold in here. (Pam stares silently at Becky.) Or anything... maybe ... hot? It just doesn't... I dunno ... feel right. (She begins to rock very gently.) I stink. I should take a shower. And there must be somethin' on this bottle. My hands're sticky. (She rises to go into the kitchen to wash her hands again.)

PAM: There's nothin' on that bottle. Will you listen to me?

BECKY: (Sitting again) Listen to what?! Listen to you come up with some more good ideas?

PAM: I was so scared tonight!

BECKY: Yeah? So was I.

PAM: (She nods. Looks at her bottle.) Where did they take ya?

BECKY: They?

PAM: They. Him and that other guy?

BECKY: They? (She stares of into space blankly.) They.

PAM: Becky! There were two of them.

BECKY: Oh. Yeah. I dunno. He was ... his friend ... or somethin'. I dunno. I think he was drunk. I tried to wake him up. He was asleep ... or something ... but he wouldn't wake up.

PAM: He didn't do something? He didn't try to help you ...

BECKY: To help? No. No. He dropped him off at ... at a house ... somewhere. I didn't... I ... Well, why didn't you do something?!

PAM: Me? I wasn't even ...

BECKY: (Rushing) Yeah! You! Why didn't you "do something?" You could tell I didn't wanna go with 'em. Ya just stood there. Y'all just stood there! Nobody did anything. Y'all just stood there and watched us leave ... (Suddenly calm) I don't want to talk about it. (She swallows a large gulp of beer.)

PAM: (Softly) I'm sorry, Becky. I didn't know what ta do. Honest. I didn't.

BECKY: I'm sorry. I guess I just wasn't thinkin'. (Silence)

PAM: Oh, God, how did this happen?

BECKY: Pam? Please don't tell anybody. Ya gotta promise me that! Please!

PAM: Alright, alright! Relax! I'm not gonna tell anyone ...

BECKY: ... 'cause if you do, they'll find out! Everyone'll find out! My mother! Your mother! The police! And then what? Pam, ya gotta promise ...

PAM: (Becoming seriously worried) Alright, I said, I won't... ya gotta believe me. Relax, OK? Drink some more of your beer, OK? (BECKY drinks. They are quiet for several moments.)

BECKY: I was scared too, ya know.

PAM: I know.

BECKY: But it's not my fault.

PAM: Of course it's not your fault. Nobody would blame you for what happened. I don't! It's nobody's fault. It just happened.

BECKY: My father would blame me.

PAM: Your father?

BECKY: He would say, "Told ya not to go down there, didn't I? But ya had to go anyway. Well, it's your own fault and you deserve whatever you get!"

PAM: (Quietly - under BECKY's lines) Oh, Becky...

BECKY: (Continuing without pausing) And he's right - I shoulda never gone down there. He's always right ... I shouldn't have ... (She pulls at her shirt collar.) It's hot in here! (Pam sees bruises that are growing quite red on BECKY’s neck.)

PAM: Oh my God, Becky... your neck... it's ...

BECKY: My neck? What... (She goes to a mirror hung by the front door.) Oh no! No way! Wait'll my mom sees that! Oh, she's gonna ...

PAM: See? You are hurt! (Firmly) Look, something happened here and you gotta tell someone.

BECKY: (Absorbed in examining her bruises) I'm ... not ... hurt ...really...

PAM: I got an idea. (PAM picks up the phone book and scans the pages as BECKY continues to examine her bruises.) I heard about this place... you can... call. It's...

BECKY: (Still at the mirror) It really happened? (PAM stands and goes to BECKY She guides BECKY away from the mirror and leads BECKY back to her chair.)

PAM: Look. This is stupid. You gotta tell someone. I heard about this place. You can talk to 'em. It's supposed ta be confidential.

BECKY: Confidential?

PAM: (Smiling) Yeah, confidential. It means they won't tell anyone. See? (She looks closely at BECKY) Never mind. I'll dial, you just talk. OK? Please? You're scarin' me!

BECKY: You dial.

PAM: (Dials the phone and waits a moment.) Here. It's ringing. (PAM hand the phone to BECKY, who carefully puts the receiver up to her ear.)

BECKY: What? (Pause) Oh, hello. Yes, I'm callin' to ... uh ... to ...

PAM: Please, Becky, tell them.

BECKY: (Nodding) Yeah, um, I'm callin' ... to talk ... to ... huh? (Pause) Yeah? Well, yeah ... I do. Um, somethin' happened here tonight and I guess I was ... raped? Uh-huh. Tonight ... I dunno ... about an hour ago?.. (She looks at PAM questioningly. PAM looks at her watch and nods.) Yeah, about an hour ago. Am I - what? Hurt? (Again she looks at PAM, who looks expectantly back at BECKY) Yeah, I'm here. No, I don't think I am. There's no blood anywhere. (Suddenly she becomes agitated.) No, I can't call the police! No. I can't... Hospital? No ... (She looks at PAM.) No, I... I can't. No, I'm OK...Look, just forget it... I gotta go now. Bye. (She places the receiver gently in its cradle.)

PAM: Well, what did they say?

BECKY: Well, she asked me if I was hurt, and I told her no, and she asked if I'd reported it, and I told her I couldn't, and she asked if I'd gone to the hospital, and I told her I couldn't ... (She wipes her hands on her jeans.)

PAM: Yeah? Go on. Wha'd she say ta do?

BECKY: (Pausing) She said that I should prob'ly have some tea and that I should prob'ly take a shower to, ya know, calm down? An' she said I could call her back later ta talk some more if I felt like it. But she said if I wasn't hurt then maybe I didn't need ta go ta the hospital...

PAM: No! No, way! Even I know better than that! Becky, if you wanna go ta the hospital, I'll drive ya there right now.

BECKY: No! Then everyone'll know and my dad'll kill me! I'm not goin'! I'm OK. Everything is OK. Ya gotta believe me.

PAM: OK. I believe you, OK? Nobody's gonna force ya to do anything you don't wanna do, OK? (Silence) Do you want another beer? (Silence) Look, maybe the lady was right. Maybe you should just take a nice hot shower and relax. Maybe that would feel good, OK? (Silence) I know. Look, I'll go start a shower for ya. OK? Do ya want me to start a shower for you?

BECKY: Yeah. Start a shower. That'd be good. Yeah.

PAM: OK. you just sit here real quiet, and I'll be right back ... OK?

BECKY: Yeah. OK. (PAM leaves the room to go start BECKY's shower. Alone now, BECKY begins to rock again very slowly. She sips her beer. She looks at her hands. She takes a very long swig of beer and coughs a bit at the taste of it.) Yeah. It's OK. Everything ... is OK. I'm not hurt.
```

---

## IC-0680: A Statue of Simon Bolivar

- Title: A Statue of Simon Bolivar
- Author (byline): Eric Lane
- Work: Laugh Lines: Short Comic Plays
- Publisher: Vintage Books
- Publication date as stated: April 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JEMMA, ELIZABETH
- Teaser before the introduction: No
- Spoken words (computed): 1017
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric Lane
Book: Laugh Lines: Short Comic Plays
ISBN: 978-0307277138
Publisher: Vintage Books
Date (Month/Year): April 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: When your parents split up it’s hard. Especially when your Dad starts dating other women. It’s hard to get past the “ick” factor.

ACTRESS 2: There's no other way to say it: Dating sucks when you’re in your 40s.

ACTRESS 1: In this selection, Elizabeth, is trying a bit too hard to find that elusive first date and to remain hopeful in the process (Actress playing Elizabeth begins to examine herself in a pocket mirror, smoothing eyebrows, pinching her cheeks and making “eyes” at herself -- Actress playing Jemma rolls her eyes, puts in her headphone and starts rocking out to some music)

ACTRESS 2: And Jemma is dealing with her father, who obviously is not wading into the dating world very well

ACTRESS 1: The two meet in New York City’s Central Park on a bench near

TOGETHER: A Statue of Simon Bolivar by Eric Lane
```

### Performance text (classify this)

```text
New York City. The statue of Bolivar, South entrance of Central Park at Sixth Ave. JEMMA, a fourteen-year-old, is seated on a bench. ELIZABETH stands. She looks off for her date, who is late. She fixes her lipstick.

JEMMA: That shit'll kill ya.

ELIZABETH: Excuse me?

JEMMA: Lipstick. There are studies. Lab rats. The shit they developed, you don't wanna know.

ELIZABETH: You're right. I don't.

JEMMA: Government studies. Big bucks for putting Revlon on rat lips. Some world, huh?

ELIZABETH: I suppose. Look, do you know what time it is? (JEMMA extends her arm, showing her watch.) Thank you.

JEMMA: You like Bolivar?

ELIZABETH: (Re watch.) Yes, it's lovely.

JEMMA: Not the watch. The general. Simon Bolivar. (Indicates statue.) Big-ass statue and nobody even bothers. El Liberador. The George Washington of South America. Won independence for Bolivia, Panama, Columbia, Ecuador, Venezuela, and Peru. You want a Tic-Tac?

ELIZABETH: No thank you. If you don't mind ...

JEMMA: I don't mind. What else I got to do?

ELIZABETH: I meant I'm waiting for someone.

JEMMA: He ain't showing.

ELIZABETH: That's a terrible thing to say.

JEMMA: True.

ELIZABETH: You don't know that.

JEMMA: I know.

ELIZABETH: You don't know that.

JEMMA: I know.

ELIZABETH: You don't know that! (A beat.)

JEMMA: I know.

ELIZABETH: Why don't you go away?

JEMMA: Can't.

ELIZABETH: I'm sure there's another plaque somewhere in the park you can memorize. Bethesda Fountain or Cleopatra's Needle. A wealth of information for a young girl of your perspicacity.

JEMMA: Nah, I'm meeting somebody.

ELIZABETH: He won't show.

JEMMA: He's a she.

ELIZABETH: Either way. She's not coming.

JEMMA: You don't know that.

ELIZABETH: I know.

JEMMA: You don't know that.

ELIZABETH: I know;

JEMMA: You don't know that 'cause she's here.

ELIZABETH: Excuse me. Unless you're meeting some imaginary friend-

JEMMA: I'm Jem.

ELIZABETH: And ... ?

JEMMA: (Extends hand.) Nice to meet you, Elizabeth.

ELIZABETH: Excuse me? How do you know my name?

JEMMA: Elizabeth M. Cunningham; The M's for Marie.

ELIZABETH: How do you ... Who are you?

JEMMA: Jem.

ELIZABETH: Jem who?

JEMMA: Jem Hollingshead. Ring a bell?

ELIZABETH: Look, I don't know what you think you're --

JEMMA: My dad's your date. At least he was supposed to be. Nicholas I. Hollingshead. I for Ivan. Can you believe naming your kid Ivan? I don't have any kids. I'm not gonna. Fish is okay, but kids suck. I hate kids. I hate cheese. I hate jelly. And I really hate it when my food touches.

ELIZABETH: So where's your father?

JEMMA: Where's he always? Work. Too busy. Story of my life. Something came up, so guess who gets to go in his place. I mean, if you're gonna go to a benefit and buy all the raffle tickets, at least go out on the date when you win it. lnstead of sending me.

ELIZABETH: Why would he buy all the raffle tickets and then send you?

JEMMA: He'd send me to take a crap for him if he could figure out how.

ELIZABETH: Well, thanks for the information and the apology.

JEMMA: You're better off. He's an asshole.

ELIZABETH: He's still your father ...

JEMMA: He's still an asshole.

ELIZABETH: I tend to agree.

JEMMA: Like, if you're gonna bid on a date for some lame-ass charity, at least pick one with a decent T-shirt.

ELIZABETH: It's not lame-ass. It's a very worthy cause.

JEMMA: (Rolls her eyes.) Kidneys for Kids. Try wearing that to gym class. You don't look so good, you wanna sit down?

ELIZABETH: No, I'm fine.

JEMMA: You don't look fine. You look like somebody just gave you a big-ass wedgie and you're hoping nobody noticed.

ELIZABETH: I said I'm fine. Thank you.

JEMMA: So where are we going?

ELIZABETH: I don't know where you're going, but I'm heading home.

JEMMA: He'll cancel the check. If you don't take me.

ELIZABETH: He wouldn't dare.

JEMMA: You don't know him. Growing up with the middle name Ivan. That shit's deadly. He's probable to do anything. Trust me.

ELIZABETH: The date's off.

JEMMA: I'll tell.

ELIZABETH: Go ahead.

JEMMA: And some baby needing a new kidney instead's gonna wind up with monkey glands. What kinda shit is that to live with?

ELIZABETH: I'm sure they'll work it out.

JEMMA: I mean you. Knowing you coulda helped but turned your back at the exact moment of need. That's a heavy burden to bear.

ELIZABETH: I've borne worse.

JEMMA: Tell me about it. And cheese. Did I mention that? I hate cheese.

ELIZABETH: I hate your dad.

JEMMA: Welcome to my life. We could kill him.

ELIZABETH: Right.

JEMMA: Serious. I could. I'm still a juvenile. You could watch. There's no way you could've stopped me. You tried, but I was out of my mind. Years of neglect culminating in one final swipe of the ax. (She demonstrates giving him a whack with the ax.)

ELIZABETH: You'd go to jail.

JEMMA: Good behavior, I'm outta there in no time. TV deal covers the legal fees. A TV movie. Drew Barrymore plays me.

ELIZABETH: Who plays me?

JEMMA: Susan Lucci. (ELIZABETH just looks at her.) Okay, Betty White. I don't know. Somebody. Who do you want?

ELIZABETH: I have no idea.

JEMMA: C'mon, you must've thought about it.

ELIZABETH: Never.

JEMMA: Some night when you're lying in bed with your cat and you can't fall asleep 'cause you keep thinking about that asshole who stood you up -- even though you told yourself not to believe. Even though you knew it wouldn't work, some part of you still hoping, believing that maybe --

ELIZABETH: I don't have a cat.

JEMMA: No?

ELIZABETH: No. (A beat.) I have· two cats.

JEMMA: Two cats and you never thought about who'd play you in the TV movie? I find that hard to believe. (ELIZABETH just looks at her.) What.

ELIZABETH: Susan Sarandon.

JEMMA: (Not quite buying it. Over-articulates each letter.) 0-K.

ELIZABETH: What?

JEMMA: Nothing.

ELIZABETH: Not nothing. I detect a certain air of sarcasm in your voice.

JEMMA: That's not sarcasm. That's life. So where we going?

ELIZABETH: How old are you?

JEMMA: Fourteen, but that's not my fault.

ELIZABETH: Fourteen. Jeez.

JEMMA: I won't ask how old you are.

ELIZABETH: No?

JEMMA: You'd probably make me guess, then get all offended and shit. No thank you.

ELIZABETH: That's what? Seventh grade.

JEMMA: (Incredulous, corrects her.) Eighth.

ELIZABETH: Eighth grade.

JEMMA: You like to row? (ELIZABETH just looks at her.) What? That's good exercise for you.

ELIZABETH: I'm not rowing.

JEMMA: Bicycle? We can rent them. Rollerblades? Merry-goround? (No response.) That's okay. We can just sit here.

ELIZABETH: I'll give you ten minutes.

JEMMA: Two hours.

ELIZABETH: Ten-

JEMMA: You'd spend at least that with my dad, and he's a dick. (A beat.)

ELIZABETH: One hour.

JEMMA: One hour. Okay.

ELIZABETH: (Looks at Jemma's watch.) Starting now. (A pause. Neither speaks. After a moment) How'd he do that? Bolivar. Win their freedom. (Jemma shrugs.) Wouldn't that be something?

JEMMA: What?

ELIZABETH: To do something so extraordinary that people build a statue.

JEMMA: Yeah, and pigeons shit all over it. (Elizabeth looks at her, then laughs.) What?

ELIZABETH: I think you're missing the point.

JEMMA: Which is ...

ELIZABETH: Nothing.

JEMMA: Yeah. Nothing. (They sit together and look out, Lights fade.)
```
