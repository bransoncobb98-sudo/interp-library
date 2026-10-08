# Classification request: batch 24 of 63 (40 records, IC-0921 to IC-0960)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-024-reply.json`.

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

## IC-0921: Superhero

- Title: Superhero
- Author (byline): Mark Harvey Levine
- Work: The Best 10-Minute Plays 2007 – 2 Actors
- Publisher: Smith and Kraus
- Publication date as stated: July 2008
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: RACHEL, LEONARD
- Teaser before the introduction: Yes
- Spoken words (computed): 1443
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mark Harvey Levine
Book: The Best 10-Minute Plays 2007 – 2 Actors
ISBN: 978-1575255897
Publisher: Smith and Kraus
Date (Month/Year): July 2008
```

### Introduction (context only: never use it for content warnings)

```text
Actor: Don't get me angry. You would not like me when I am angry!

Actress: With great power comes great responsibility.

Actor: My spider sense is tingling! Actress: Is it a bird? Is it a plane? No! It's Superman!

Actor: These are sayings from some of the world's favourite superheroes. They are the Incredible Hulk, Spider-Man and the original superhero, Superman!

Actress :Superheroes use their special powers to rescue people in danger or difficult situations. They must have a strong desire to help.

Actor: Superheroes do not usually like to tell many people about their special powers. So, they must be good at keeping a secret. This may mean that they do not have many close friends. So superheroes must be prepared to be lonely at times.

Actress: But here’s the most important component . . . . Have you been ignored, insulted,

Actor: Discarded all your life?

Together: Then you just may be a Superhero by Mark Harvey Levine.
```

### Performance text (classify this)

```text
An apartment; morning. At lights up, Rachel is seen bound to a chair, a gag in her mouth.

RACHEL: (Muffled from the gag.) Help ... help! (There is a loud thump, the sound of somebody running into the door.) Oh, wait, it's locked. (Rachel effortlessly gets out 0/ the chair, unlocks her front door, and returns to the chair, "re-tying" herself) Try it again. (She puts the gag back on her mouth.) (Nothing happens.) (Sighing.) Help, help. (Immediately, Leonard bursts through her door. He is a slight man dressed like a superhero. His costume is obviously, and rather pathetically, homemade.)

LEONARD: (His slogan') I'm here to help!

RACHEL: Thank God you're here.

LEONARD: I picked up your cry for help. Luckily, I was in the hallway taking out my garbage at the time. What happened, citizen?

RACHEL: Ruffians!

LEONARD: (He starts to untie her, not noticing how easy it is.) Ruffians?

RACHEL: They tried to rob me. But they heard you and ran.

LEONARD: They won't get far. (His exit line.) Stay strong, citizen! (He starts to leave.)

RACHEL: Leonard! Don't go!-

LEONARD: I'm not Leonard! Leonard is my friend. He helps me in my exploits.

RACHEL: Oh, sorry, sorry. I forgot. But I have to call you something - you haven't picked out your name yet.

LEONARD: My name has to come from my powers. And I don't know what they are - yet. I know I can't fly. (Obviously there's a story here.)

RACHEL: You'll figure it out.

LEONARD: (Preparing to leave again.) Stay strong, citizen.

LEONARD: (Preparing to leave again.) Stay strong, citizen.

RACHEL: Wait! Help!

LEONARD: What's wrong?

RACHEL: Well, it's just ... urn ... (Indicates pastry box nearby.) I've got all these danishes, and I won't be able to eat' em all. Want one? (She pulls out a chair for bim.)

LEONARD: That's not a-! You- It's- (He's frustrated into speechlessness.)

RACHEL: If you don't eat it, it'll go to waste! Isn't it a crime to waste food?!

LEONARD: Yes, but-

RACHEL: Well, here is a crime you can prevent! Have some breakfast. You want coffee?

LEONARD: I'm on duty!

RACHEL: Superheroes can't sit down and eat a meal?

LEONARD: At this very moment I'm locked in a terrible struggle with Claw Woman.

RACHEL: Claw Woman?!

LEONARD: ... You may know her as Esther Manning, in 316.

RACHEL: Oh yeah! Her. With all the cats.

LEONARD: She's a Grasping Harpy of Evil. Our contest of wills has escalated. Only one of us will survive.

RACHEL: Well, you can't defeat her on an empty stomach. Have you eaten anything yet?

LEONARD: ... I had a bowl of frosted flakes.

RACHEL: You're running around on nothing but cereal?! Now that is a crime. Sit down. I've got apricot.

LEONARD: Apricot My favorite. Resistance . . . weakening . . . Getting . . . hungry Must . . . turn . . . away . . .

RACHEL: Want me to heat' em up?

LEONARD: No! What if evil strikes and I'm sitting here with a mouth full of tangy apricot filling? I have to go. Stay strong! (He goes to leave again.)

RACHEL: Oh wait, help! Sorry, sorry, there's one more thing. If you don't mind.

LEONARD: Now what?

RACHEL: Well ...

LEONARD: Your life had better be in danger.

RACHEL: Well ... urn, I can't get to that bulb up there.

LEONARD: You want me ... to change a lightbulb?!

RACHEL: I thought with your super-height, you could reach it. Sorry.

LEONARD: Rachel, you've got to stop calling me in, unless it's an actual emergency! I'm a superhero!

RACHEL: I know. I'm sorry.

LEONARD: What if sorneone's really in trouble, and I'm here ... fixing your disposal?!

RACHEL: Sorry, sorry.

LEONARD: ... How IS the disposal, by the way?

RACHEL: Oh, it's great! You did a fabulous job with -

LEONARD: All right then. 'Sides, you don't need a superhero, you need the super. Where IS Mr. Crazciek?

RACHEL: He won't come up to this floor since you defeated him in battle.

LEONARD: Right. Now, Rachel. I'm going to change your lightbulb, as a favor, because you're a nice person. (He gets a chair and stands on it.) But then you must never call me again, unless it's an actual life-or-death emergency. Not to change a lightbulb, not to set your VCR, not to buy you the paper. This is it.

RACHEL: (Unreasonably worried about him on the chair.) Oooo, careful ...

LEONARD: I don't run errands - I fight evil!

RACHEL: (The old schoolyard trick, she grabs him and shakes bim.) Saved your life! (She laughs a little too giddily, stays hanging on.)

LEONARD: Rachel ... you wanna let me go?

RACHEL: (Reluctantly lets go of him, overly nervous.) OK! I'm sorry. Please be careful. Please.

LEONARD: This is nothing! I spent all yesterday battling Claw Woman and her Cat Minions. Get me a new bulb.

RACHEL: (As she does so.) How many cats DOES she have?!

LEONARD: I think she has all of them.

RACHEL: (Finding the bulb, unreasonably scared for Leonard.) Yeah, seriously ... Ooo! Careful! Careful!

LEONARD: (She hands him the bulb.) They keep getting on my balcony and attacking my plants. They killed my ficus. I must avenge his death. (Like a comic book:) The bulb! I- I can't reach it!

RACHEL: That's OK, that's OK, just get down, get down!

LEONARD: You think I accept defeat so easily? Ha! (He stacks two or three chairs on top of one another. It looks incredibly precarious. He starts to climb up.)

RACHEL: (Completely panicked.) NO! DON'T! (She restrains him.)

LEONARD: What? What's the matter with you?

RACHEL: You're going to get hurt! Don't!

LEONARD: Rachel, please!

RACHEL: No! No! You're going to fall and break your neck and it'll be my fault! Please! Forget the light! Please!

LEONARD: All right, all right ... calm down! Sheesh!

RACHEL: I'm sorry. It's just - I'm afraid of heights.

LEONARD: You were on the ground.

RACHEL: I'm afraid of heights for other people.

LEONARD: You weren't in danger, Rachel.

RACHEL: I am in danger! We all are! Look at this! (She grabs the neiospaper.) Bus crashes, home-invasion murders, random shootings, breast cancer, bridge collapses, killer bees! Ewgh! (She rips an article out of the paper.) I am in danger! I'm in terrible danger, Leonard!

LEONARD: (Angrily.) I'm not Leonard! Leonard is, like you, afraid of everything! Leonard goes to work alone and comes home alone and sits alone in his apartment and eats his meals over the sink and watches TV until he falls asleep. But not me.

RACHEL: OK-

LEONARD: That's how I found out I was a superhero. I always WAS one, but I didn't know it! Nobody told me! They kept it hidden from me!

RACHEL: OK, OK, shh, shh, relax honey.

LEONARD: (Getting very worked up.) I should have known, though. It was there all the time. How come I always got the parking ticket, the broken shoelace? How come I always arrive JUST as they're flipping over the sign that says "closed"? Why do they imitate my voice at work when they think I'm not around? Why such a large conspiracy to destroy me? There can only be one reason! I'm dangerous to them!

RACHEL: (Afraid.) Yes, you are, honey, you are, you are.

LEONARD: Now, I don't know what my powers are, but I do know that I'm brave! Strong!

Invincible!

RACHEL: That's very-

LEONARD: (Coming at ber.) I'm afraid of nothing!

RACHEL: (Backing into a corner.) I'm a little afraid of you, I'm afraid.

LEONARD: You're afraid of everything! Just like Leonard -

RACHEL: It's true, it's true! I'm a chicken! I'm afraid of bugs, and microwave ovens, and cancer and subways and Rod Stewart and nuclear war –

LEONARD: They did this to you, Rachel! Don't you see? It's just what happened to Leonard. When you were in school, were you the last person picked for the team?

RACHEL: Always.

LEONARD: When you stand at the deli, does the lady behind the counter stare into space like you're not even there?

RACHEL: Yes ...

LEONARD: Have you been ignored, insulted, discarded all your life?

RACHEL: Yes!

LEONARD: Rachel! You're a superhero!

RACHEL: (Laughs nervously.) Oh no no no.

LEONARD: You are, and you don't know it!

RACHEL: Oh, no. Please. Are you kidding me? I'm nobody.

LEONARD: That's what I thought. But you'll know when you put the uniform on. Try it.

RACHEL: Oh, no, no, that's all right, really -

LEONARD: I'm serious. (As in a comic book.) You have no idea the power you'll feel - pure energy coursing through your veins! (Then, as himself) It's really kinda cool!

RACHEL: No, thanks.

LEONARD: Come on.

RACHEL: ... Well, maybe just the cape. (He removes his cape and puts it on her.)

LEONARD: There. How do you feel?

RACHEL: Like a lady in a cape.

LEONARD: You have to have the gloves, too. (He removes his gloves, she puts them on. During this - ) They go with the cape.

RACHEL: And very smartly, too. (He hands her the underwear.) Um ...

LEONARD: I've only worn these on the outside.

RACHEL: S orry, I had to ask. (She puts them over her slacks.)

LEONARD: OK ... now ... the mask.

RACHEL: Is that OK?

LEONARD: I ... I guess so. I mean, if you want to get the whole effect ... (Leonard removes his mask. Rachel smiles at him. Leonard looks expectantly, and she realizes what she's supposed to do.)

RACHEL: My God! Leonard! It's you!

LEONARD: Yes ... It's me. I had to conceal my identity from you, for your own safety. But now well, there are no secrets between superheroes.

RACHEL: Oh, honey, I'm not a superhero.

LEONARD: Aren't you? Put on the mask. (She does. She now has Leonard's costume on, and he is more or less normally dressed.) You sure look like one. Try walking around. (She shuffles around.) No, no! You have to stride forward, with purpose! Fists clenched! Head high! Never turn back! You turn back, you trip over your cape. How do you feel?

RACHEL: Completely ridiculous. Leonard, I don't think I'm cut out to be a superhero . . .

LEONARD: Of course you are ... I can't be wrong about this. I'm never wrong about this.

RACHEL: Leonard, I'm just the lady who lives across the hall from you. If you want, you can come over and have breakfast sometime -

LEONARD: Fine then! Have it your way! And you can spend the rest of your life getting the parking tickets, the leaky faucets, and the dead plants! Because you're a loser! A failure! You SHOULD be picked last for the team! You should be laughed at and passed over and ignored and - (Quite suddenly, Rachel slugs him in the jaw, surprising herself as well as Leonard. He goes down hard.)

RACHEL: OhmiGod!

LEONARD: (From the floor.) ... Nicely done ...

RACHEL: OhmiGod! Are you OK?! I'm so sorry! I don't know why I did that! Are you OK?

LEONARD: (In great pain.) Sure ... No problem ... Don't forget, I'm a superhero. And so are you. Feels good, huh?

RACHEL: I've never hit anyone before!

LEONARD: Well you're ... doing swell, for a beginner.

RACHEL: I can't believe I -

LEONARD: It's the uniform. It's amazing what it does, isn't it?

RACHEL: Yeah, I guess so ...

LEONARD: Congratulations. Today, for the first time, you fought back against the forces of evil!

RACHEL: I did?

LEONARD: Sure. That nasty little voice inside you? I've got one, too. Of course, I also have Claw Woman in 316. (She laughs.)

RACHEL: Leonard, I think you've ... awakened my inner Wonder Woman ... (She climbs up on the chair. She poses, superhero-ly) Hey.

LEONARD: What?

RACHEL: Hey!

LEONARD: What?!

RACHEL: You saved my life ... (Lights fade.)
```

---

## IC-0922: Sure Thing

- Title: Sure Thing
- Author (byline): David Ives
- Work: All in the Timing: Fourteen Plays, Pgs 1-18
- Publisher: Vintage Books
- Publication date as stated: November 1994
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BILL, BETTY
- Teaser before the introduction: No
- Spoken words (computed): 1426
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Ives
Book: All in the Timing: Fourteen Plays, Pgs 1-18
ISBN: 978-0679759287
Publisher: Vintage Books
Date (Month/Year): November 1994
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: It's probably no surprise -- guys are completely clueless when it comes to meeting women. They often resort to horrible canned pick-up lines: “Do you believe in love at first sight.”

ACTRESS: And women are just as awkward when it comes to accepting the sincere interest of a member of the opposite sex. Instead, women become suspicious: Why is he talking to me? What does he want? Do I need my mace?

ACTOR: It’s a wonder anyone gets together at all! Wouldn’t it be great if you had the opportunity to instantly replay all those times when you’ve said the wrong thing?

ACTRESS: If you actually had a second chance to make a good first impression?

TOGETHER: Sure Thing by David Ives
```

### Performance text (classify this)

```text
Betty, reading at the table. An empty chair opposite her. Bill enters. Every time a bell rings, the scene begins at the last awkward moment – a Do-Over.

BILL: (Pgs 1-18) Excuse me. Is this chair taken? BETTY: Excuse me?

BILL: Is this taken? BETTY: Yes it is.

BILL: Oh. Sorry. BETTY: Sure thing. (A bell rings softly)

BILL: Excuse me. Is this chair taken?

BETTY: No, but I'm expecting somebody very shortly.

BILL: Would you mind if I sit here till he or she comes?

BETTY: (glances at her watch) They seem to be pretty late. . .

BILL: You never know who you might be turning down.

BETTY: Sorry. Nice try, though. BILL: Sure thing. (Bell)

BILL: Is this chair taken? BETTY: No, it's not.

BILL: Would you mind if I sit here? BETTY: No. Go ahead.

BILL: Thanks. (He sits. She continues reading) Everyplace else seems to be taken.

BETTY: Mm-hm. BILL: Great place.

BETTY: Mm-hm. BILL: What's the book?

BETTY: I just wanted to read in quiet, if you don't mind.

BILL: No, sure thing. (Bell)

BILL: What's the book? BETTY: The Sound and the Fury.

BILL: Oh. Faulkner. BETTY: Have you read it?

BILL: Not . . . actually. I've sure read about it though. It's supposed to be great.

BETTY: It is great.

BILL: I hear it's great. (Small pause) Waiter? (Bell)

BETTY: Have you read it? BILL: Yeah, I read it in college.

BETTY: Where was college? BILL: I went to Oral Roberts University.

(Bell)

BETTY: Where was college?

BILL: I was lying. I never really went to college. I just like to party. (Bell)

BETTY: Where was college? BILL: Harvard.

BETTY: Do you like Faulkner?

BILL: I love Faulkner. I spent a whole winter reading him once.

BETTY: I've just started.

BILL: I was so excited after ten pages that I went out and bought everything else he wrote. One of the greatest reading experiences of my life. I mean, all that incredible psychological understanding. Page after page of gorgeous prose. His profound grasp of the mystery of time and human existence. The smells of the earth . . . What do you think?

BETTY: I think it's pretty boring. (Bell) BILL: What's the book?

BETTY: The Sound and the Fury. BILL: Oh! Faulkner!

BETTY: Do you like Faulkner? BILL: I love Faulkner.

BETTY: He's incredible.

BILL: I spent a whole winter reading him once.

BETTY: I was so excited after ten pages that I went out and bought everything else he wrote.

BILL: All that incredible psychological understanding.

BETTY: And the prose is so gorgeous.

BILL: And the way he's grasped the mystery of time --

BETTY: -- and human existence. I can't believe I've waited this long to read him.

BILL: You never know. You might not have liked him before.

BETTY: That's true.

BILL: You might not have been ready for him. You have to hit these things at the right moment or it's no good.

BETTY: That's happening to me.

BILL: It's all in the timing. (Small pause) My name's Bill, by the way.

BETTY: I'm Betty. BILL: Hi.

BETTY: Hi. (Small pause)

BILL: Yes, I thought reading Faulkner was . . . a great experience.

BETTY: Yes. (Small pause)

BILL: The Sound and the Fury . . . (Another small pause)

BETTY: Well. Onwards and upwards. (She goes back to her book)

BILL: Waiter ? (Bell)

BILL: My name's Bill, by the way. BETTY: I'm Betty.

BILL: Do you come here a lot? BETTY: Every once in a while. Do you?

BILL: Not much anymore. Not as much as I used to. Before my nervous breakdown. (Bell)

BILL: Do you come here a lot? BETTY: Why are you asking?

BILL: Just interested.

BETTY: Are you really interested, or do you just want to pick me up?

BILL: No, I'm really interested.

BETTY: Why would you be interested in whether I come here a lot?

BILL: Just . . . getting acquainted.

BETTY: Maybe you're only interested for the sake of making small talk long enough to ask me back to your place to listen to some music, only all you really want to do is [you know] which you won't do very well -- after which you'll go into the bathroom and pee very loudly. And then you'll proceed to lie back down beside me and confess that you've got a girlfriend named Stephanie who's away at medical school for a year, and that you've been involved with her -- off and on -- in what you'll call a very "intricate" relationship, for the past seven YEARS. None of which interests me, mister!

BILL: Okay. (Bell)

BILL: Do you come here a lot? BETTY: Every other day I think.

BILL: I come here quite a lot and I don't remember seeing you.

BETTY: I guess we must be on different schedules.

BILL: Amazing how you can live right next door to somebody and never even know it.

BETTY: I know. BILL: City life.

BETTY: It's crazy.

BILL: You weren't waiting for somebody when I came in, were you?

BETTY: Actually, I was.

BILL: Oh. Boyfriend? BETTY: Sort of.

BILL: What's a sort-of boyfriend?

BETTY: My husband.

BILL: Ah-ha. (Bell)

BILL: You weren't waiting for somebody when I came in, were you?

BETTY: No, just reading.

BILL: Sort of a sad occupation for a Friday night, isn't it? Reading here, all by yourself?

BETTY: Do you think so?

BILL: Well sure. I mean, what's a good-looking woman like you doing out alone on a Friday night?

BETTY: Trying to keep away from lines like that.

BILL: No, listen (Bell)

BILL: You weren't waiting for somebody when I came in, were you?

BETTY: No, just reading.

BILL: Sort of a sad occupation for a Friday night, isn't it? Reading here all by yourself?

BETTY: I guess it is, in a way.

BILL: What's a good-looking woman like you doing out alone on a Friday night anyway? No offense, but . . .

BETTY: I just recently ended a relationship.

BILL: I'm sorry (Small pause) Well listen, since reading by yourself is such a sad occupation for a Friday night, would you like to go elsewhere?

BETTY: No . . . BILL: Do something else?

BETTY: No thanks. BILL: I was headed out to the movies.

BETTY: I don't think so.

BILL: Big chance to let Faulkner catch his breath. All those long sentences gets him pretty tired.

BETTY: Thanks anyway. I appreciate the invitation.

BILL: Sure thing. (Bell)

BILL: You weren't waiting for somebody when I came in, were you?

BETTY: No, just reading.

BILL: Sort of a sad occupation for a Friday night, isn't it? Reading here all by yourself?

BETTY: I guess I was trying to think of it as existentially romantic. You know cappuccino, great literature, rainy night . . .

BILL: That only works in Paris. We could hop the late plane to Paris. Get on a Concorde. Find a café . . .

BETTY: I'm a little short of plane fare tonight. BILL: Damn it, so am I.

BETTY: To tell you the truth, I was headed to the movies after I finished this section. Would you like to come along?

BILL: That's a very nice offer but . . .

BETTY: Uh-huh. Girlfriend?

BILL: No, I don't have a girlfriend. Not if you mean the [witch] I dumped last night. (Bell)

BETTY: Girlfriend? BILL: Sort of. Sort of.

BETTY: What's a sort-of girlfriend? BILL: My mother. (Bell)

BILL: I just ended a relationship, actually. BETTY: I'm sorry to hear it.

BILL: This is my first night out alone in a long time. I feel a little bit at sea, to tell you the truth.

BETTY: So you didn't stop to talk because you're a Moonie, or you have some weird political affiliation ?

BILL: Nope. Straight-down-the-ticket Republican. (Bell) Straight-down-the-ticket Democrat. (Bell) Can I tell you something about politics? (Bell) I like to think of myself as a citizen of the universe. (Bell) I'm unaffiliated.

BETTY: That's a relief. So am I.

BILL: I vote my beliefs. BETTY: Labels are not important.

BILL: Labels are not important, exactly. I believe a man is what he is. (Bell) A person is what he is. (Bell) A person is . . . what they are.

BETTY: I think so too.

BILL: So what if I admire Trotsky? (Bell) So what if I once had a total-body liposuction? (Bell) So what if I once spent a year in the Peace Corps? I was acting on my convictions.

BETTY: Sure.

BILL: You can't just hang a sign on a person.

BETTY: Absolutely. I'll bet you're a Scorpio. (Many bells ring) (Simultaneously) BILL: Y'know I was headed to the . . . BETTY: I was thinking about . . .

BILL: I'm sorry. BETTY: No, go ahead.

BILL: I was going to say that I was headed to the movies in a little while, and . . .

BETTY: So was I. BILL: The Woody Allen festival?

BETTY: Just up the street. BILL: Do you like the early ones?

BETTY: I think anybody who doesn't ought to be run off the planet.

BILL: How many times have you seen Bananas? BETTY: Eight times.

BILL: Twelve. So are you still interested? (Long pause)

BETTY: Do you like Entenmann's crumb cake?

BILL: Last night I went out at two in the morning to get one. (Small pause) Did you have an Etch-a-Sketch as a child?

BETTY: Yes! And do you like Brussels sprouts? (Small pause)

BILL: I think they're gross. BETTY: They are gross!

BILL: Do you still believe in marriage despite current sentiments against it?

BETTY: Yes.

BETTY: Three of them.

BETTY: Harvard, Vassar, and Brown.

BETTY: Yes.

BETTY: Yes.

BILL: And children?

BILL: Two girls and a boy.

BILL: And will you love me?

BILL: And cherish me forever?

BILL: Do you still want to go to the movies? BETTY: Sure thing. BILL and BETTY (together): Waiter!
```

---

## IC-0923: Sylvia

- Title: Sylvia
- Author (byline): A.R. Gurney
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Oct 1996
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GREG, SYLVIA, KATE, LESLIE, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1580
- Already set (do not supply): none

### Source block (context only)

```text
Author: A.R. Gurney
ISBN: 978-0822214960
Publisher: Dramatists Play Service
Date (Month/Year): Oct 1996
```

### Introduction (context only: never use it for content warnings)

```text
Sylvia by A.R. Gurney
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actor – Greg and Leslie Actress: Kate and Sylvia

Greg and Kate's apartment. Sylvia comes on, followed by Greg, holding a leash and a newspaper. She is pert and sexy. Her hair is messy and she wears rather scruffy clothes: a baggy sweater, patched jeans, knee pads, and old boots. A small nametag in the shape of a heart hangs around her neck. Greg wears business clothes, but his tie is loose. He watches Sylvia wander inquisitively around the room. She occasionally might take a sniff of something.

GREG: (Pg 4-6) What are you doing, Sylvia? Relax, why don't you?

SYLVIA: I gotta get used to things. (She prowls) I'm worried about where I sleep. Do I sleep on this couch?

GREG: (He gives Sylvia a cuddle) I want you to be on your best behavior. Kate gets home any minute.

SYLVIA: (Sylvia gazes at him adoringly) You saved my life. I never would have survived out there on my own. Someone else might have ignored me. Or shooed me away. Or even turned me in. Not you. You welcomed me with open arms. (Sylvia hears something) Hey!

GREG: What's the matter?

SYLVIA: (Looking off) Hey! Hey! Hey!

SYLVIA: (Pg 6-7) (Looking off) Hey! Hey! Hey!

GREG: What? (He listens) Oh, that. That's just Kate. Home from work.

SYLVIA: (Unable to control herself) Hey! Hey! Hey! Hey!

GREG: No, now quiet, Sylvia! Quiet down!

KATE: Hello! (Kate enters) Am I crazy? I thought l heard a- (Sees Sylvia) Dog.

SYLVIA: (Walking around Kate, looking her over) Hi. I think I like you. Hi. (Gives Kate a tentative kiss)

KATE: (Brushing her off) Stop that. Go away! (to Greg) Greg, what is this?

GREG: I was sitting in the park, and Sylvia jumped right into my lap.

KATE: Back up, please. You were sitting? In the park? When were you sitting in the park?

GREG: This afternoon. I took a break from the office. (Pause. Kate looks at Sylvia.)

KATE: Sylvia? Why Sylvia?

GREG: The name was on her tag. (Showing her) See? "Sylvia." (Sylvia begins to scratch) It fits. I looked it up. It means "She of the woods." (Sylvia is now scratching vigorously)

KATE: She of the woods has fleas.

GREG: I'll deal with that. I'll get her all checked out.

KATE: (Pg 8-9) Sweetheart, I'm exercising a veto. No. N period. O period. Not in New York. Not at this stage of our lives. No. You work all day, I work all day. We go out a lot. There's no need.

GREG: I have a need. And she needs me. We've bonded, Kate.

KATE: Ooo. Ouch. That's an overworked word, Greg.

GREG: I really want her, Kate.

KATE: And I really don't. (Looking at Sylvia) What is she? A mutt?

GREG: I think she may be part poodle.

SYLVIA: (Assuming a saucy position) Mais oui, Monsieur. Ooo la la.

KATE: Is she house-trained?

SYLVIA: (Uneasily) Oh yes. Definitely. Absolutely. No question.

GREG: She was a good girl walking home, weren't you, Sylvia? (talking baby talk) We were a very good girl. 'Twice. Weren't we?

KATE: I may puke, Greg.

SYLVIA: (Pg 10-11) l think you're prejudiced against dogs! (She leaps onto the couch, circles and lays down)

KATE: Off, Sylvia!

SYLVIA: You speaking to me?

KATE: I said off that couch! Right now! (Pulls Sylvia off the couch) And stay off.

SYLVIA: Easy! Take it easy! . . . Jesus!

KATE: This is not going to work. (Pg 12) We'll give you to The Animal Rescue League. Or the Humane Society.

SYLVIA: They suck! Have you ever been there? The rows of cages. They have time limits. If someone doesn't bail you out, within five days, they put you to sleep. They kill you! Listen. It's a tough world out there, lady. I know. I've been there. (Leaps into Greg’s arms.)

GREG: (Pg 13-15) Let me at least try her, Kate. A few days, at least.

KATE: (exasperated) All right. For a few days we will try Sylvia.

SYLVIA: Yippee! Yay!

KATE: I want one thing dear, Greg. She's yours, not mine. I won't feed her, and I won't walk her, and I don't want her jumping onto any of the- (Sees something on the floor) What's that?

(Disgusted) She's pee'd, Greg. (Sylvia is embarrassed)

GREG: She was nervous, Kate. Strange place. Hostile atmosphere. . .

SYLVIA: 'That's it. That was the problem. (Hugging him) I love this man. I adore him.

KATE: Rub her nose in it at least! She's got to learn!

SYLVIA: Hey! Hey! Hey!

GREG: (Putting Sylvia’s leash back on) Tell you what -- We'll go out.

SYLVIA: Did I hear the word "out"? Knew it! Can't wait! Love going out! (Dragging him toward the front hall.) Come on, Greg! ***** Scene *****

GREG: (Pg 18-20) (Off-stage) We're home! I've got a surprise for you. Ta da. (Proudly he presents Sylvia) I had her professionally groomed. (Sylvia comes on with a new hairdo, a bow in her hair, and a corny outfit.)

SYLVIA: Look at me! Look at me! (Shimmying) How do you like them apples?

GREG: They gave her the full treatment: flea dip, nails clipped, ears cleaned, the works. They told me she was crawling with fleas. You were right about that, Katie. But now look at her. Isn't she spectacular? (Sylvia dances around joyously) Don't you want to keep her now?

(Bringing Sylvia to Kate)

SYLVIA: (Holding out her hand to be kissed) Enchant!, Madame.

KATE: Greg, please. (She exits)

SYLVIA: She doesn't like me. ****** Scene ******

KATE: (Pg 27)(to audience) She waits, you know. She literally waits, until I'm out the door, and then she leaps onto that couch. She only listens to Greg. They do everything together. Once I caught them sharing an ice cream cone and . . . (Pg 29) She drinks from the toilet! And lately he's been taking the afternoon off. Every day! He and Sylvia have lunch and go on these long walks. She's destroying our marriage.

GREG: (Pg 30) (Off-stage) Hello!

SYLVIA: (Pg 35-36) (Hears Greg and excitedly enters carrying a woman's shoe) Look what I've got! (Parading it around) Look at this fabulous shoe!

KATE: Drop that, Sylvia! Right now! (she attempts to get the shoe)

GREG: She just wants to play.

SYLVIA: Chase me. Hey! Hey! Hey!

KATE: Time's up. I said I'd try, and I have. I'm putting my foot down, Greg. I am issuing an ultimatum. Give Sylvia away.

GREG: (Ignoring the statement) It's time for her dinner. (To Sylvia) Come on, sweetheart. Time to eat. (As they exit Sylvia makes a rude gesture of some type)

KATE: (Calling after) Sweetheart? Is it sweetheart now? Dammit, Greg! When's the last time you said that to me? *****Scene*****

LESLIE: (Pg 48) I must say, Kate, I find it somewhat difficult to counsel married couples when one of the partners refuses to cooperate. I thought your husband agreed to join us.

KATE: Let's simply assume he's with Sylvia . . .

LESLIE: (Consulting notes) During our last session, you seemed to suggest that he had actually fallen in love with Sylvia.

KATE: He has! Totally! Even when we were first married, he never looked at me the way he looks at Sylvia. (Greg comes in, breathlessly)

LESLIE: (Pg 49-50) Kate, why don't you go in the other room and read a magazine. I'd like to talk to Greg alone. (Kate goes out)

LESLIE: Sit down, Greg. Talk to me . . . Say whatever is on your mind.

GREG: O.K. (Pause) She's not herself lately. Particularly these past few weeks. She resents me.

LESLIE: And why do you suppose she resents you?

GREG: Because I made the decision (pause, he speaks quietly, ashamed) to have her spayed.

LESLIE: Ah . . . You're talking about . . .

TOGETHER: Sylvia.

GREG: She’s got great eyes. Deep, serious eyes. But that doesn't mean she's serious all the time. She laughs. I've actually seen her laugh. And she's got this great little butt. When she sashays down the street, she kind of wiggles it back and forth.

LESLIE: (Pg 52) Greg. I think it's time to move on. May I bring in Kate so we can all sit down together.

GREG: Aren't you forgetting Sylvia? You've seen Kate, you've seen me, don't you think you should see Sylvia?

LESLIE: You want me to hold a session with your dog? *****Scene*****

GREG: (Pg 54-55) (Pause) Sylvia, I have to send you away. It boils down to you or Kate, Sylvia. And I'm choosing Kate. I've found a family for you.

SYLVIA: You're choosing Kate? Is this because she hates me?

GREG: She doesn't hate you, Sylvia. She doesn't like me, Sylvia. When I'm with you.

SYLVIA: I thought there was talk of you and me moving out. Getting a studio apartment right near the park. (Greg shakes his head sadly) (Sylvia, aloof) Tell me about this family you're shipping me off to.

GREG: (with excitement) They're great, Sylvia. I interviewed a number of applicants. (Pg 56-57) They have children. They want to teach you to play Frisbee. They want to take you to Little League games. They'll be much better for you than I could possibly be.

SYLVIA: I hate *children.* They're totally unreliable. They forget to feed you. They play music which hurts your ears. One minute they're showering you with love, then they leave you locked in some car for hours on end- (Throwing herself on him) Oh Greg, don't do this to me! Please! I'll change my ways. I'll stop chewing shoes. I'll bring Kate the New York Times every morning! Just tell me what to do, and I'll do it! Please!

GREG: I promised Kate I'd give you away, Sylvia. I made that promise. To my wife.

SYLVIA: Jesus, you're something, Greg. You really are. You bring me home, you get me all dependent on you, you spay me ... You had me spayed, Greg! Christ, Greg! Don't you feel guilty?

KATE: (From off) Hello! (Sylvia turns away haughtily; Kate sees that Greg is upset) (Pg 58) I know this is hard for you.

GREG: I can't talk about it, Kate. It's too painful at the moment. (He exits)

KATE: (Pg 59-60) (to Sylvia) I wish it could have been otherwise, Sylvia.

SYLVIA: (Long beat – Mimics Kate) "I wish it could have been otherwise." Know what "otherwise" is, Kate? Otherwise is those sad couples sitting in restaurants night after night, eyeing each other, with absolutely nothing to say. That's otherwise, Kate. (pause) "This wise" is the fact that he can never be happy with me unless you like me, too. Which is why he is always foisting me on you. [It’s] called sharing, Kate. Which is what some people sometimes call love. Of course, what do I know? I'm only a dog. (She exits to find Greg)

KATE: (Thinks for a moment) Oh hell. (She goes off determinedly after Greg and Sylvia) *****Scene*****

(all lines are spoken to the audience)

GREG: (Pg 60-61) We never got to the suburbs. l called and said we'd changed our minds.

KATE: I changed my mind.

GREG: Once I came home and found Kate and Sylvia side by side on the couch. Kate was reading The Hidden Life of Dogs, and Sylvia had her head in Kate's lap.

KATE: This is an absolute lie!

GREG: And Sylvia stayed with us for the next eleven years, until we had to put her down. I held her when the vet gave her the shot. She looked at me, gave a little sigh, lay down quietly, and died. (Pause) Kate was waiting for me when I got home, and we both cried.

KATE: That's not true. I did not cry.

GREG: Whatever. Oh, Sylvia's looks changed. I'll show you. (He takes a small photograph out of his wallet) There. That's Sylvia.

KATE: l took that picture the year before she died. (they look at the picture) I'm afraid she looks a little the worse for wear.

GREG: She does not, Kate! She still looks absolutely gorgeous!

(The lights fade on Greg and Kate, very much together, looking at Sylvia's picture.)
```

---

## IC-0924: Test Tube Lives

- Title: Test Tube Lives
- Author (byline): Jason Sheets
- Work: Turning Points: 30 Pieces for Oral Interpretation, Pg 125-130
- Publisher: Tichenor Press
- Publication date as stated: Jan 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SANDY, MICHAEL
- Teaser before the introduction: Yes
- Spoken words (computed): 1097
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jason Sheets
Book: Turning Points: 30 Pieces for Oral Interpretation, Pg 125-130
ISBN: 978-0742117013
Publisher: Tichenor Press
Date (Month/Year): Jan 2001
```

### Introduction (context only: never use it for content warnings)

```text
Test Tube Lives by Jason Sheets
```

### Performance text (classify this)

```text
SANDY: (Pg 125-130) Well, I thought it was fun!

MICHAEL: I don’t care what you say…movies aren’t meant to be over three hours!

SANDY: True. Thanks for being with me tonight. It was really important that I didn’t spend tonight alone. (A beat) You know. One year ago tonight was supposed to be –

MICHAEL: One year ago tonight – your wedding.

SANDY: Yeah. So anyway, thanks. I didn’t want to obsess over it.

MICHAEL: You OK?

SANDY: Yeah. I still know it was the right thing not to get married, but here I am. 35. I always said if I’m 35 and still single I’d run away and be a nun. It’s lonely. I know – you can’t always relate. I mean, you’ve got Nate and you always have someone there.

MICHAEL: It’s nice.

SANDY: Meanwhile, I’m realizing that I’m getting too old to be the “new look” news-anchor. Too old to find a husband. Too old to have a baby.

MICHAEL: 35 isn’t that old. And some things you just have to accept. I’ve accepted I’m not having children, either.

SANDY: Well, you could.

MICHAEL: Sure, I could adopt. We both could –

SANDY: Or we could (pause)

MICHAEL: We could what?

SANDY: Or we could.

MICHAEL: Sandy, are you serious?

SANDY: You always said with your looks and my brains…

MICHAEL: Whoa – the last thing this would needs is a kid looking like me running around! Besides, Nate probably would have problems with the creation of this wonderchild.

SANDY: We wouldn’t have to actually do it. These doctors now –

MICHAEL: OK, fine. But you want me? Me? To be the father?

SANDY: You’re my best friend.

MICHAEL: Yes.

SANDY: We stick together no matter what.

MICHAEL: Yes.

SANDY: You’re gay, so that means no romantic attachment.

MICHAEL: Sure, but –

SANDY: And I know you. You want to be a father, don’t you?

MICHAEL: I never’d really much thought about it.

SANDY: C’mon.

MICHAEL: OK, maybe once.

SANDY: C’mon, I saw you watch Three Men and a Baby

MICHAEL: Yes, and I laughed. You know why? They were awful parents!

SANDY: No, they cared. They just needed a little help. I’m that help. Michael, I’ll raise the child. You can be as little or as big a part of his

MICHAEL: Or her

SANDY: Life.

MICHAEL: Don’t you want love? A husband? All the –

SANDY: I don’t want give up on love, Michael. But there’s no window for love. There is a window for having a child. I only need one. One. A boy. A girl. I don’t care. I have just always wanted to be a mother.

MICHAEL: (long pause) I’ll need to ask Nate.

SANDY: Of course. Will you?

MICHAEL: Yeah, I will. *************************************************************************

SANDY: (on the telephone) So what’d he say?

MICHAEL: Don’t you think I should come over so we can –

SANDY: No. What’d he say???

MICHAEL: He’s cool with it.

SANDY: Really?

MICHAEL: Yeah, he’s cool with it.

SANDY: Are you?

MICHAEL: Sandy, this is big.

SANDY: Are you cool with it?

MICHAEL: Yeah, truthfully I went shopping this morning. How do you feel about pastels?

SANDY: I knew you’d love this! *************************************************************************

MICHAEL: I still think we’re crazy.

SANDY: That’s OK. So do I. (playing cards)

MICHAEL: Nothing like a game of crazy eights to calm the nerves.

SANDY: I know – not much strategy to worry about.

MICHAEL: I feel as if my life is out of control…

SANDY: But it’s a good feeling isn’t it?

MICHAEL: Yeah, it is. I keep imagining what it’ll be like to have a child call me dad”.

SANDY: Never thought it’d happen, did you?

MICHAEL: Truthfully, no. Gay men kind of give up on having it all.

SANDY: But now…

MICHAEL: Now, I’ve got it all. Sandy, I’m so excited.

SANDY: You don’t think we’re warping the child by giving him two fathers and a mother?

MICHAEL: I think in the 1990s most children need three parents. *************************************************************************

SANDY: Wow, I had no clue how expensive this whole process is! A 15% success rate and the time it takes! Let’s just hope your boys are potent!

MICHAEL: Can we refrain from the talk of my boys?

SANDY: Sure, I’m sorry, I just had no idea –

MICHAEL: We went shopping too soon?

SANDY: No – the power of positive thinking, right?

MICHAEL: Right. Wow, and just last week I was thinking of tearing down the basketball hoop.

SANDY: Better leave it up he

MICHAEL: Or she

SANDY: May like it.

MICHAEL: Sure. So where do we begin?

SANDY: We test your boys and your blood – I mean you go in for –

MICHAEL: Don’t worry, I get the drift. *************************************************************************

SANDY: So, why’d you call? I got your message at work. You never call me there. I –

MICHAEL: Have you talked to the doctor?

SANDY: No.

MICHAEL: Sandy, I’ve changed my mind, I can’t do this.

SANDY: What?

MICHAEL: You heard me. I said I can’t do this.

SANDY: What do you mean? Is this your idea of a joke? You give me the OK, go shopping for baby things, go down for testing, put up with me, and then –

MICHAEL: And then nothing. I just can’t, OK? Look, I gotta go.

SANDY: Like hell. You’re going to stay, and Michael, as my friend of 15 years, you’re going to tell me. You’re free to back out, but you sure as hell are going to tell me why.

MICHAEL: What does it matter?

SANDY: Is it Nate.

MICHAEL: No, no of course not. He doesn’t even know I’m here.

SANDY: Is it your job? You know you can still travel –

MICHAEL: Sandy, will you stop?

SANDY: No, I won’t stop. I want a baby. You’d be the greatest father in the world, and I want to know why!

MICHAEL: I can’t.

SANDY: Why?

MICHAEL: I –

SANDY: Why???

MICHAEL: Cause I’ve got AIDS. OK??? My boys are fine, my blood has AIDS. I can’t father your damn kid because they don’t approve of AIDS babies, OK? I can’t father our child because I’m gonna die. I’m gonna…(cries)

SANDY: (pause) My God, Michael, how did this happen?

MICHAEL: I haven’t been with Nate forever.

SANDY: But Michael

MICHAEL: Look, I gotta go. Nate needs a test, I need to tell him. I’m sorry about the baby. I mean I am so sorry.

SANDY: Michael –

MICHAEL: (waves)

SANDY: I’ll call you, OK? ************************************************************************

SANDY: (on phone) Heya, Nate. Is Michael there> Oh, OK. No, he should be at the doctors. Congrats on your test, by the way. Um, I just wanted to see when I could drop off some books. I found some material on AIDS. You know, they’ve really made a lot of breakthroughs…

MICHAEL: Hi, Sandy.

SANDY: I thought you were –

MICHAEL: I’m here. Just not taking calls at the moment.

SANDY: But you’re taking mine.

MICHAEL: Yeah, I’m taking yours. So, what –

SANDY: Michael, I just wanted to call to tell you thank you.

MICHAEL: For what?

SANDY: For making me realize. I’ve spent all this time obsessing over family. Family. Family. Never for once realizing, you and Nate are it. I’ve got a family.

MICHAEL: Thanks Sandy.

SANDY: And now a family member is sick. So it’s my job to cheer you up. May I interest you in a fierce battle of crazy eights?

MICHAEL: Sure can.

SANDY: Good, I’ll be right over.
```

---

## IC-0925: That’s All Folks

- Title: That’s All Folks
- Author (byline): Barbara Lhota and Janet B. Milstein
- Work: Forensics Series, Volume 2
- Publisher: Smith and Kraus
- Publication date as stated: Feb 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: PETER, SHELLY
- Teaser before the introduction: No
- Spoken words (computed): 1419
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barbara Lhota and Janet B. Milstein
Book: Forensics Series, Volume 2
ISBN: 978-1575253084
Publisher: Smith and Kraus
Date (Month/Year): Feb 2003
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Through the years, Peter has been given the daunting challenge of taking care of his autistic younger sister, Shelly, who is two years his junior.

ACTRESS: Shelly is a high-functioning autistic teenager who attends a special program in the local high school.

ACTOR: Peter watches out for Shelly every day. He protects her from other kids, eases her tantrums, and makes sure she makes it to and from school.

ACTRESS: To make life worse, Shelly and Peter's parents have been fighting for weeks now. The word divorce has even come up. Peter knows that Shelly's autism has played a part in the tension.

TOGETHER: That’s All Folks by Barbara Lhota and Janet B. Milstein
```

### Performance text (classify this)

```text
PETER: What are you doing in here?! Get out of here!

SHELLY: I watch Bugs Bunny. Five minutes till "Bugs Bunny and Friends."

PETER: You don't belong in here, Shelly. It's my room.

SHELLY: Next stop Wilson.

PETER: Go downstairs and watch whatever you want.

SHELLY: Doors closing. Doors closing. (Makes a realistic sounding ding.)

PETER: Get out, or I'm going to throw you out!

SHELLY: (Flapping her hands, upset.) T-t-t-that's all folks!

PETER: Come on!

SHELLY: (Waving her hands a bit.) No. Loud. Loud. (Touching ears.) Looooud.

PETER: Yes, I'm being loud, Shelly, but it's my room. I can be as looooud as I want.

SHELLY: (Rocking.) Yeah.

PETER: You don't think I have a right to be loud in my own room?

SHELLY: Yeah. (Beat.) Lawrence is next.

PETER: You don't think I have a right to do anything if it doesn't involve you. Or at least Mom and Dad don't.

SHELLY: Priority seating is intended for the elderly and those with disabilities.

PETER: You embarrass me. Do you hear me?

SHELLY: (Turning in another direction.) Priority seating is intended for the elderly and those with disabilities.

PETER: You looked like an idiot today, ya know? Why can't you be like a normal autistic kid who doesn't like to touch? Do you know how weird that looks to come running at me-hugging me? It's weird. I'm your brother. You don't do that in front of other people.

SHELLY: Your cooperation is appreciated.

PETER: But you don't care. You just keep going on with your own little thing. I know everybody thinks you can't stop, but I know you can.

SHELLY: (More quietly.) Your cooperation is appreciated. Your cooperation is appreciated. Your cooperation is appreciated. Your cooperation is appreciated. Your cooperation

PETER: Stop it!! (Shelly stops. She even briefly looks up at him.)

PETER: I'm sorry, Shelly. I just. . . hate this. I sorta have a thing for that Donna girl, ya know? That new girl. So when you came. . . at me today, well, it scares other kids. I mean, you scare other kids. I was really pissed off even though I know you don't mean to scare anyone. I got really angry. I even had to go to the Y with Josh to blow off some steam. It's like I get angry all the time now. I hate it. I don't think it's fair to be in this position. It's just I told you I'd pick you up from your classroom. Why didn't you wait?

SHELLY: (Quietly.) This is Lawrence.

PETER: I know you were just being you. I'm just tired, and I want my own space tonight. Okay?

SHELLY: Doors closing. Doors closing. (She makes the ding sound.)

PETER: I know you hear me . . . Sooo. Go. Down. Stairs.

SHELLY: Who directed most of the Looney Tune Cartoons?

PETER: I don't want to play trivia. The TV is free down there.

SHELLY: Try again. Who directed most of the Looney Tune cartoons?

PETER: Fine. I'm gonna get Mom then. (Shelly shakes her head furiously and makes a humming noise.)

PETER: What's wrong? (Shelly begins flapping her arms. In between, she starts to bite her hand.}

PETER: (About her biting.) No. No.

SHELLY: (Still biting.) Gone. Gone. T-t-t-that's all folks.

PETER: Stop it! (She lets out a cry and stops biting.)

PETER: Okay, Mom's gone. That's okay. She'll be back. (Shelly lets out another hum noise and plunks into the chair.)

SHELLY: (She folds her legs, leans forward, and rocks herself. She imitates a famous Bugs Bunny cartoon. Blankly, without emotion.) Would you like to shoot me now or wait till you get home?

PETER: It's practically six. Are you sure she's not here?

SHELLY: (Continuing.) Shoot him now. Shoot him now.

PETER: Did something happen?

SHELLY: (Touching her ears.) Loud.

PETER: A fight?

SHELLY: You keep out of this. He doesn't have to shoot you now. He does so have to shoot me now. I demand that you shoot me now.

PETER: Dad and Mom had another fight?

SHELLY: (Quietly singing, mumbling the words to the Bugs Bunny theme song "Overture.") (*see note at the end of the selection) Overture. . . light the lights. This is it. The night of nights. No more rehearsing and nursing a part. . . we know every part by heart.

PETER: He left?

SHELLY: T-t-t that's all folks.

PETER: (Reaching out to her.) Listen. Did he leave?

SHELLY: (Imitating Woody Woodpecker and Porky.) H-h-h-ha ha. H-h-h-ha-ha. T-t-t-that's all folks. T-t-t-that's all folks. H-h-h-ha-ha.

PETER: (As if to say enough already.) Okay! (Beat.) Do you know why?

SHELLY: (Imitating her father.) I am so sick of this! I am so sick of you and everything! It's enough to have to deal with Shelly every day. Everything we do is with autistic kids autistic events. I'm tired of the obsession. I don't want my life based around this! Do you understand this?

PETER: Where's Mom?

SHELLY: I am so sick of this! I am so sick of you and every thing!

PETER: He didn't mean it, Shelly.

SHELLY: (Biting her hand in between, not ever looking at him.) I am so sick of this! I am so sick of you and everything! It's enough to deal with Shelly every day. It's enough to deal with Shelly every day.

PETER: It's not your fault. This is not your fault.

SHELLY: (Does perfect imitation of father's emotion without adding her own.) Do you understand this? Do you understand this? Do you understand this?

PETER: Yes, yes. I understand. I understand how you feel, and he's just using you as an excuse. It's not your fault. Now, where's Mom?

SHELLY: Doors closing. Doors closing. (Making the ding noise.) Doors closing. Doors closing. (Makes the ding noise.) Doors closing. Doors

PETER: She just wants to be left alone then. She'll come out of her room soon. Don't worry.

SHELLY: Closing. (Makes the ding sound.)

PETER: It's not right what he said, Shel. It's not even true.

SHELLY: (Begins singing again quietly, rocking.) Overture. Light the lights.

PETER: They just fight. They can't seem to get along.

SHELLY: (Singing, rocking.) This is it. The night of nights.

PETER: We could try to help them though.

SHELLY: (Singing.) No more rehearsing and nursing a part.

PETER: You could try to get better, Shelly. It would make things easier maybe.

SHELLY: (Singing.) We know every part by heart.

PETER: I know you're in there. I understand you. Look at me. The first step is more eye contact. Look at me. (He steps in front of her and tries to make her look. She turns away.)

SHELLY: (Singing.) Overture.

PETER: I'll work with you every day. I promise.

SHELLY: (Singing.) Light the lights.

PETER: I'm talking to you, Shelly. Tell me how your day was.

SHELLY: (Singing.) This is it. The night of nights.

PETER: I know you're sad. So talk to me directly now. I'm your big brother. Why don't you talk to me?

SHELLY: (Singing.) No more rehearsing and nursing a part.

PETER: You have to talk directly, not through TV stuff any more.

SHELLY: (Singing.) We know every part by heart. Overture

PETER: (He forces her to look at him.} No, no. What's going on with you, Shelly? What's going on? (She pauses, quietly. She avoids his eye contact.)

PETER: (He feels her calm down. She's with him.) That's good. Look at me now. Come on. You can do it. Tell me.

SHELLY: (Pause.) Doors closing. Doors closing. (Makes the ding noise.)

PETER: Come on, at least try. At least try to look at me for once!

SHELLY: Priority seating is intended for the elderly and those with disabilities. Priority seating is intended for the elderly and those with disabilities. Priority seating is intended for the elderly and those with disabilities.

PETER: Don't you see what you've done to us?!

SHELLY: Doors closing. Doors closing. (Makes the ding noise.) Doors closing. Doors closing. (Makes the ding noise.) Door closing. Doors

PETER: (Slapping her hard across the face.) Stop it! (Shelly cries out and throws herself off the chair.)

PETER: Oh God. (Shelly begins biting her arm hard.)

PETER: Oh God. Please, Shelly. I'm sorry. (He moves toward her but she squirms away from him making a whining sound and biting her arm.)

PETER: I didn't mean it. I don't know what I'm doing, Shelly. I'm an idiot. Please stop. Stop hurting yourself. Please.

SHELLY: (She begins banging her hand hard against her head.) Do you want to shoot me now or wait till you get home? (Peter moves down to the floor with her, trying to stop her hand. She fights against it.)

PETER: I didn't mean what I said. Please. . . stop. I'm stupid. I'm just a kid. I say stupid things I don't mean half the time.

SHELLY: (Still biting her hand, mumbling.) Do you want to shoot me now or wait till you get home? Shoot him now. Shoot him now. You keep out of this. He doesn't have to shoot you now. He does so have to shoot me now. I demand that you shoot me now. (She keeps repeating, whispering more.)

PETER: (Trying to hold her hand back away from her teeth.) I know I'm a rotten brother. And I know if I could get through to you, Dad wouldn't be so angry so often. (She pulls her hand away.) Okay. Fine. But whatever happens, we're gonna need each other now more than ever. And it doesn't matter if you keep biting yourself or not, the pain will still be there. So go ahead if you want to. Go ahead. I'm obviously not helping you any. I'm just making things worse. I can't believe I hit you. I'm sorry, Shelly. I'm sorry. (He moves away from her.)

SHELLY: (She stops struggling and curls up in a ball. Very quietly.) It's not your fault. This is not your fault.

PETER: What did you say?

SHELLY: It's not your fault. This is not your fault.

PETER: (Pause.) We communicate-you and I. Probably better than other brothers and sisters. We just connect in a different way I guess, you know?

SHELLY: Yeah.

PETER: It'll be all right. You know? Maybe he'll be back. He'll be back. I'm sure of it.

SHELLY: Yeah.

PETER: If he doesn't, he's pretty stupid. Cause we're pretty good kids.

SHELLY: Yeah. I knew I took that wrong turn in Albuquerque. Should have zigged when I zagged. (Peter smiles.)

PETER: Should we get Mom?

SHELLY: Yeah. (She reaches out her hands to him.) Hug?

PETER: (Beat.) Sure. (They embrace.)

PETER: I love you, kiddo. Don't ever forget that. 'Kay?

SHELLY: (Beat. Nods.) Umm.

PETER: We'll make it through this. Okay?

SHELLY: Yeah.

PETER: But no huggin' me at school, all right? Okay?

SHELLY: Yeah. (She lets go.) Who directed the most Looney Tune Cartoons?

PETER: (Playing along.) Umm. I don't know. Thomas Jefferson?

SHELLY: (Makes bad buzzer noise.) Wrong answer.

PETER: Maybe, humm, let me think. . . Mel Blanc.

SHELLY: Ding! Correct. Ding!

PETER: Come along, Rabbit. Doors opening. Doors opening. Priority seating is intended for Bugs Bunny and his pal Daffy. Ding! (She takes his hand.) Ding. (Thinking a moment before they leave.) Ding. (To her.) He'll be back. He's gotta come back, right?

SHELLY: Ding. (Peter gestures for her to move ahead.)
```

---

## IC-0926: Therac 25

- Title: Therac 25
- Author (byline): Adam Pettle
- Work: Not specified
- Publisher: Scirocco Drama
- Publication date as stated: Sept 2000
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ALAN, MOIRA
- Teaser before the introduction: Yes
- Spoken words (computed): 1606
- Already set (do not supply): none

### Source block (context only)

```text
Author: Adam Pettle 2003 National Qualifier
ISBN: 978-1896239705 2004 National Qualifier
Publisher: Scirocco Drama 2005 National Qualifier
Date (Month/Year): Sept 2000 2007 National Qualifier
2009 National Qualifier
2010 National Qualifier
2014 National Qualifier
NOTE: Here’s a link to Cat Steven’s Moonshadow to help with the signing parts:
https://www.youtube.com/watch?v=hr0rDW5j1KU
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Cancer blossoms like a fleur du mal in the human body.

ACTOR: That's a scary fact of life.

ACTRESS: Less certain -- and far more delicate -- is the love that flowers in a hospital cancer ward in Therac 25.

ACTOR: Alan and Moira, the most unlikely of partners.

ACTRESS: From that first mutual look of interest as they wait for their ongoing therapies . .

ACTOR: They're a couple destined to alternate between tentative offers of comfort and spiky retreat.

TOGETHER: Therac 25 by Adam Pettle
```

### Performance text (classify this)

```text
A waiting room, the Princess Margaret Hospital. Early in the morning. Alan (22) sits in the waiting room. He has a black, bound journal in his lap; he is trying to write. After a beat or two, Moira enters the waiting room. She grabs a Reader’s Digest and sits down in a chair, feigning interest in the magazine. There is a long silence . . .

ALAN: What year is it?

MOIRA: What?

ALAN: The Digest

MOIRA: Oh. (checking the cover) Eighty-four.

ALAN: A fine year. The Summer Games in L.A., the arrival of E.T . . . Christ! That’s ten years ago already . . . . Now why would they want us to read articles from ten years ago? We’re cancer patients, not historians . . . . I’m Alan

MOIRA: Moira

ALAN: So, where’s your . . . ?

MOIRA: On my mind.

ALAN: And what number treatment is this?

MOIRA: Nine.

ALAN: Of?

MOIRA: Twenty-five.

ALAN: Hey! Me too. I’ve got two today.

MOIRA: Yum. . . . Are you trying to pick me up?

ALAN: What?! No, I mean, no! Christ, I’ve never even tried in a bar, I mean I just never know what to say, and in a waiting room at the Princess Margaret I think I’d really be out of my league. (Grabbing his journal) That could be my book: “One Hundred and One Lines to Pick Up a Cancer Patient” (He begins writing the idea down in his journal) (Pause)

MOIRA: “Hey, baby! Want to go for some platinum injections?”

ALAN: (Laughing) “You know, ah, I don’t want to brag, but I’ve got the lowest white blood cell count in this place.”

MOIRA: “I don’t know if anyone has ever told you this, but you’ve got the most scannable skull I have ever . . . “ (OVER THE INTERCOM) Mr. Feldman to Vault Forty-one. Mr. Feldman.

ALAN: That’s me. (Getting his stuff together) What are you doing this afternoon?

MOIRA: I have chemo at eleven-thirty.

ALAN: You’re doing both! Mon Dieu.

MOIRA: Just for another week. Then my cycle is over.

ALAN: Well do you have plans after chemo? Another one for the book.

MOIRA: Vomiting

ALAN: Can I join you?

MOIRA: You are trying to pick me up.

ALAN: I’m just . . . It’s just that I have eight hours in between my two treatment . . . If I go home, I’ll fall asleep in front of Geraldo, if I stay down here, I’ll wander from coffee shop to coffee shop. We could go for coffee in the four-star cafeteria.

MOIRA: Why would you want to go out with me? I’m . . . I’m bald.

ALAN: I’m Jewish.

MOIRA: Imagine what our kids would look like.

ALAN: My grandfather. What do you say?

MOIRA: I’ll meet you in the cafe at twelve-thirty.

ALAN: Great! Have a good . . . Do you say “Have a good chemo?”

MOIRA: No.

(Alan walks out of the room, Moira closes her eyes and puts her face in her hands. Alan re-enters the room.)

ALAN: Did you say twel . . . ?

MOIRA: What?

ALAN: Sorry, I . . . Are you . . . How are you feeling?

MOIRA: Don’t say that.

ALAN: I know – the world’s worst question and yet I ask it; it’s just –

MOIRA: No! It’s not a joke. If you want to know me, you can never ask me that, it’s a rule, you understand?

ALAN: Yes. (Pause) Do you still want to meet me for coffee?

MOIRA: Maybe I’ll be there and maybe I won’t.

(SCENE)

(Alan sits in the cafeteria drinking a tea, anxiously looking to the door. After a few beats Moira enters the cafeteria and approaches Alan’s table, gingerly)

ALAN: You came.

MOIRA: I decided to forgive you.

ALAN: Thanks. How was . . . ?

MOIRA: Don’t ask. (She takes a pill out of her bad and washes it down with her bottled water.) So when was your diagnosis?

ALAN: Late August.

MOIRA: And what was . . . ?

ALAN: Oh, ah . . . a tumor on my thyroid gland which was removed two weeks later, along with eleven cancerous lymph nodes and the nerve attached to my left vocal cord. The tumor was wrapped around the nerve, which was a surprise to me and to Dr Brierly. He spent an hour during my surgery deciding whether to remove the nerve or –

MOIRA: Will you excuse me for a second? (Before the question is answered, she is up and out)

ALAN: (To himself) I think she’s gone to throw up. Is it the chemo, or the smell of the meatloaf? Or me? I wish I could . . . Maybe she wants me to go out there. I can’t. Christ, you know most people pick an early move and a bit afterwards for their first date . . . We are not most people.

MOIRA: (Re-entering the cafeteria) Sorry. What were you saying? We were talking about your surgery.

ALAN: Right. Ah, gone: thyroid, parathyroid, eleven lymph nodes – enough for a soccer team – the nerve attached to vocal cord, gained a . . . a new pair of eyes. You know, I was hopein they would do something about this nose, but . . . not enough OR time, I guess. Cutbacks, you know? Did you have surgery?

MOIRA: No. It’s inoperable. Like your nose. I have a high-grade pineal tumor that resembles meduloblastoma.

ALAN: (Pause) So, what do you want to be when you grow up?

MOIRA: Alive.

ALAN: I . . . I hear there’s good money in that.

MOIRA: I was in my third year of Sociology. I was thinking about social work.

ALAN: You are thinking about social work.

MOIRA: Whatever. Chris . . . my boyfriend . . . is coming to get me at one-thirty. Do you need a lift somewhere?

ALAN: Oh, no thanks, I’ve got my car.

MOIRA: Ooooh, he’s got a car.

ALAN: Yeah, she’s a ’79 Gremlin. It was my high school graduation present.

MOIRA: A Gremlin?

ALAN: Yeah, well, I didn’t do that well in high school. Do you drive?

MOIRA: I do, but not lately. I mean, you know what they say about morphine and driving.

ALAN: Well, you should give me your number. I mean, I’m coming down here every day, I’d be happy to give you a life if you – (She starts writing her phone number down and laughing.) What?

MOIRA: I was just thinking . . . I wonder what’s more distasteful: the chemo, or being driven to it in a Gremlin.

ALAN: Eh! Enough with the car. Here, I’m going to give you mine, too. (He writes down his number, starts to hand it to her, then pulls it back.) Now no crank calls, OK?

MOIRA: I promise

(SCENE)

(A small Greet Orthodox church beside the hospital)

MOIRA: Thanks for bringing me here. I haven’t been in a church in three years.

ALAN: Happy halfway home. Treatment number thirteen, c’est finis!

MOIRA: Why do you do that? . . . That French thing at the end of your sentences. If we were married that would be one of those things that would secretly drive me crazy and eventually force me into an adulterous affair.

ALAN: C’est dommage! I think the way that you stare at my hairline when I’m speaking would have me banging the maid long before you had a chance to .

MOIRA: Banging the maid? Is that what sex is with you? Banging?

ALAN: Do you think this is the place to be discussing this?

MOIRA: No. (Pause) If you’d said I would be nailing the maid, then we’d

ALAN: Oh. Nice. Crucifixion jokes, we are in big trouble.

MOIRA: Oh, you’re right, I shouldn’t mock God, make . . . make jokes about Jesus, I should be grateful for all this great luck I’ve been having . . . I’m sorry, God, please don’t give me locusts or . . . or a brain tumor, or . . .

ALAN: Moira, please –

MOIRA: Excuse me! I’m talking to God. And when I die, please take care of mommy and daddy and my dog Suzie . . .

ALAN: Do you ever wonder why everyone cries when they’re born? I men, not everyone cries when they die, right? At least not on TV.

MOIRA: No, they don’t. I think you’re on to something Nietzsche.

ALAN: I’m not talking about dying tomorrow, it’s a long way off, for both of us, but it is inevitable, and . . . and I think we could talk about it.

MOIRA: I don’t want to talk about it. . . Your top three.

ALAN: What?

MOIRA: Your top three biggest regrets if you die tomorrow, not that it’s going to happen. What are the chances of your cancer recurring, what?! Seventy-five percent it won’t.

ALAN: Yes! And you’ve got a good chance, too. I looked up meduloblastoma, it’s treatable! You’ve got a really good shot at beating this thing!

MOIRA: I think I’m going to throw up. . . No I am going to throw up. (Moira begins to sing Moonshadow to herself. After a beat or two, she begins to vomit)

ALAN: Ah . . . is there anything I can do for you?

MOIRA: Sing Moonshadow . . . Cat Stevens, Moonshadow, sing it.

ALAN: Moira, I . . . I . . . I don’t know it. (Moira puts her hand on Alan’s back; Alan moves away) No, I can’t

MOIRA: Can’t want?

ALAN: Be touched. I’m sorry I . . . I tried to tell you. It’s just that since September, since my surgery, I . . . I have days when I can’t be touched, not by hands, not by drugs, not even a hug from my mother. And I need you to know that it’s not your hands that are making me nauseous, it’s this body . . . How am I supposed to have a relationship? How am I supposed to explain why I’m crying for the ninth night in a row? . . . You know, I don’t even like it when someone holds my hand.

MOIRA: I think I’d better go. (Moira begins walking out, staggering a little. Suddenly she grabs the back of her neck then falls, convulsing in a seizure.)

ALAN: Oh my God! (Lights fade)

(SCENE)

(A hospital room. Moira sits in a hospital bed hooked to an IV. She is staring out the window, Alan enters.

MOIRA: I don’t want you here. I want you to leave. It’s going to be really embarrassing if I have to call Security – for both of us – so I’m asking you once more to leave.

ALAN: I can’t just leave things like this.

MOIRA: Which part of that didn’t you understand? Go away!

ALAN: No – you – just let me apologize, OK, and then I’ll leave.

MOIRA: Oh! I get it! You think this is your fault. This is a guilt visit. You won’t be able to live with yourself thinking you caused the seizure that broke the camel’s back.

ALAN: (simultaneously with “live”) That’s not what I’m saying. I just need to talk to you.

MOIRA: You need to talk to me? What could there possible be to talk about? Now get out and don’t come back.

ALAN: “I’m being followed by a moon shadow, moon shadow, moon shadow. I’m leaping and hopping on a moon shadow, moon shadow, moon shadow . . . “ (He has some trouble remembering the words) “And if I ever lose my eyes, lose my eyes, if I lose. And if I ever lose my eyes, oh way hey hey hey hey hey hey hey hey, I won’t have to see again.”

MOIRA: It’s a joke (near tears) (pause)

ALAN: What’s happening?

MOIRA: I told you that my tumor resembled meduloblastoma, but what makes it different is that it can travel through the spinal fluid to other parts of the brain and . . . mine has.

ALAN: What does that mean?

MOIRA: That I’m going to die.

ALAN: When?

MOIRA: Soon.

ALAN: Is there anything I can do? (Moira shakes her head, but then it slowly turns into a nod. She looks at him, reaches down and touches his nose. Alan does not pull away. Moira runs her hand down his face, and then takes his hand and puts it on her chest.) Moira . . . how are you feeling?

MOIRA: I’m scared.
```

---

## IC-0927: These Shining Lives

- Title: These Shining Lives
- Author (byline): Melanie Marnich
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: June 2010
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DR. DALITSCH, CATHERINE, TOM, MR. REED, CHARLOTTE, VOICE OVER, REPORTER 1, REPORTER 2
- Teaser before the introduction: Yes
- Spoken words (computed): 1502
- Already set (do not supply): none

### Source block (context only)

```text
Author: Melanie Marnich
ISBN: 978-0822224488
Publisher: Dramatists Play Service
Date (Month/Year): June 2010
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: It was the early 1920s and one of the most sought-after jobs for young women in America involved something exciting and brand new:

ACTOR: Radium. Sparkling, glowing, and beautiful, radium was also,

ACTRESS: According to the company

ACTOR: Completely harmless. It would make watch faces glow in the dark.

ACTRESS: And so, an excited Catherine Donahue found her dream job at age 19 and was hired by the Radium Dial Company. It was a marvelous

ACTOR: . . . until it wasn’t. Throughout American history, women have fought for better wages, equal rights and safer working conditions. The Radium girls of the 1920s brought about the first legal case in which an employer was held responsible for the health of its employees.

ACTRESS: In the words of author Audre Lorde . . . [This is] “for those women who do not speak, for those who do not have a voice because . . . we are taught to respect fear more than ourselves. We’ve been taught that silence would save us, but it won’t.”

ACTOR: Based on true events . . . this is

TOGETHER: These Shining Lives by Melanie Marnich
```

### Performance text (classify this)

```text
Suggested Roles: Actress: Catherine and Charlotte Actor: All other roles

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

DR. DALITSCH: (Pg 46) . . . your fractured jaw resulting from a tooth extraction and the subsequent infection in the tooth’s socket, in addition to anemia . . .

CATHERINE: (Pg 9) This isn’t a fairy tale . . .

DR. DALITSCH: (Pg 46) . . . the severe pain in your legs, the hard ridge that has formed along the underside of your jaw . . . is a direct result of . . .

CATHERINE: (Pg 9) It’s not a tragedy . . .

DR. DALITSCH: (Pg 47) Did they warn you? Did they protect you?

CATHERINE: (Pg 9) It’s something else . . . (Pg 10) I’m Catherine Donohue. I live in Ottawa, Illinois. I have two children [and] a husband that I love . . . (Pg 11) And we started like this. ******

(Catherine and Tom at home; she’s getting ready for her first day of work)

TOM: (Pg 11-12) Well, aren’t you the prettiest thing?

CATHERINE: What time is it? I think I’m going to be late.

TOM: You’re fine.

CATHERINE: The time. TOM: Guess.

CATHERINE: To-om.

TOM: Guess wrong, I kiss you. Guess right, you kiss me. Guess.

CATHERINE: 7:15? (He kisses her. Catherine is still trying to get dressed) 7:30? (He kisses her) Quarter of eight . . . Am I getting close?

TOM: (laughing) You were right the first time.

CATHERINE: Be honest. How do I look? (Strikes a pose) Do I look like a girl worth 8 cents a watch? Who knows, maybe I’ll make more than you someday.

TOM: Ouch!

CATHERINE: (Pg 13) I want to know what it feels like to make eight dollars a week. I want to know. Just once. I want to be that person. For a while. (she drops something) I’m nervous, I guess. (she struggles to fix the collar of her dress).

TOM: Come here. (He reaches out and fixes the collar of her dress) There ya go. You know, I look at you every day before I leave. I take a picture of you (mimes taking a photo) I take it with me up there; on the girders and beams . . . Beautiful.

CATHERINE: Tell me I can do this. Tell me I’ll be good enough.

TOM: You can do it. But you won’t be good enough. You’ll be great. (A quick kiss)

(Catherine’s 1st day of work at the Radium Dial Company)

MR. REED: (Pg 14-16) Morning, girls. I’d like you to meet Catherine Donohue.

CATHERINE: Hello.

MR. REED: (as he ushers Catherine to her work station, he addresses another worker) Charlotte? Painting the dials . . . how it’s done.

CHARLOTTE: (demonstrating) Alright. It’s easy. See? You take your little brush here, twirl it between your lips to make a point, then dip it into the powder here. Paying attention?

CATHERINE: (mimicking Charlotte’s actions) Point . . . dip . . . and then you paint. Like this.

(She paints a number, shows Mr. Reed and puts the brush back in between her lips) Why does it shine? (Reacts to the taste) It tastes awful. Is it okay? Getting this stuff in our mouths.

MR. REED: It’s more than okay. [Radium] is medicinal. (Pg 17-18) Think you can do it?

CATHERINE: Oh, I can do it. I’m sure!

CHARLOTTE: She’ll be great, Mr. Reed. (Mr. Reed exits) *******

CATHERINE: (Pg 18) (speaks to the audience) And I was. My twos swooped and dipped. My fives were flawless. And my twelves? (gestures for extraordinary)(Beat) I walked home that night in the dark. Ten years ago, a girl like me couldn’t even vote, let alone make this kind of money. But now? (enters the apartment and removes her coat to greet Tom, who is in the kitchen making dinner) (Pg 23) You beat me home.

TOM: (Pg 18) Your hair! (Catherine touches her hair) It’s shining. Your dress (She touches her dress) Your hands, your eyelashes, your mouth. You glow.

CATHERINE: It’s the dust. From the paint . . . for the watches.

TOM: (Pg 23-24) (Pre-occupied with getting dinner on the table) Your mom just left. The kids didn’t take their nap, so they’re monsters. Hungry monsters. (He sets the table haphazardly) Dinner’s not going to be good . . . I didn’t really know how to. . .

CATHERINE: (Pulling a small box out of her handbag) A little something. To make up for it.

TOM: (Takes the box) For me? Don’t think you can just bribe me with gifts. I’m not that kind of girl. (Opens the box and is wow’d by the gift) Wait. Yeah, I am. (Takes a pocket watch from the box and opens it) Wow. You just bought me off with a pocket watch.

CATHERINE: (Proudly) I painted it. The numbers.

TOM: It’s . . . perfect! *******

CATHERINE: (Pg 32-33) (to audience) When I started, I thought it would only be for a while . . . Six years. (Beat) And like that, time passes. (Long beat) Before we noticed . . .

VOICE OVER: 218,723 watches later . . .
*******
Tom and Catherine’s apartment. Catherine is in the bathroom, washing the radium dust from her
hands and arms. She is in obvious pain as Tom enters

TOM: (Pg 33-35) Katie? I’m home. Helluva day. I drop my lunch off the twenty-second story. I could eat a horse. (Tom enters the bathroom and clicks on the light, Catherine responds negatively, but Tom doesn’t notice) How was work? How many watches you paint today?

(He pats her on the check, again Catherine responds in pain, but Tom doesn’t notice)

CATHERINE: (without any energy to her voice) One seventy-five.

TOM: (continuing in his happy-go-lucky tone) How are the kids? You hungry? You want me to start dinner? You look tired, no offence.

CATHERINE: Tom? Look at me. You see anything different?

TOM: Just my beautiful Katie

CATHERINE: Turn off the light.

TOM: What? Why?

CATHERINE: Just turn it off! (She holds up her hands, showing her palms, then returns to the sink, washing furiously to try to remove the glow)

TOM: It’s just the dust. Like always. It’ll wear off. It’s fine.

CATHERINE: But it’s not just on my skin anymore. It’s in my skin. Tom, it’s in my body. I ache, Tom. My bones. My legs, my back.

TOM: (refusing to see or hear) Maybe this job’s getting too hard for you. Maybe you’re just tired like any working stiff.

CATHERINE: I’m not some little doll, Tom! It’s not too hard for me. There’s something wrong and I don’t know what it is!

TOM: (blows her off) Your hands are dirty! So what? (starts to walk away)

CATHERINE: Don’t you dare walk away from me!

TOM: (losing his temper) Listen, I’m tired too!. If this job’s getting to you, don’t come home and take it out on me, okay?! Every day I’m up there doing the high-wire act, worried that I won’t see you and kids again just because I moved an inch in the wrong direction. I told you the day you started that work is work! So we ache! So we’re tired! That’s what you signed up for, Katie! Remember, you wanted this job. (a beat of quiet)

CATHERINE: I’m telling you. (She experiences a sudden shooting pain in her arm and cries out loud) There’s something wrong with me. And I. Am. Scared.

TOM: (Pg 39-40) Maybe it’s the cold, the damp.

CATHERINE: (Still doubled over in obvious pain) You know what would be great? If you’d actually believe me instead of making excuses. There’s something wrong. It’s not the weather. I’m not working too hard.

TOM: (Finally facing the reality of her pain) Listen. . . I’m sorry. We’ll go see the doctor. Together.

CATHERINE: God, I’m so tired. ******* Mr. Reed’s office at Radium Dial

MR. REED: (Pg 44-45) Ah, Mrs. Donohue. Come in, come in.

CATHERINE: You wanted to see me?

MR. REED: You’re missing too much work, Mrs. Donohue . . . I have to let you go.

CATHERINE: What? No! Only a few days. Not that many. No more, I promise, no more. Just let me –

MR. REED: (cutting her off)This is a good place for girls. For healthy girls. I’m sorry.

CATHERINE: You’re really firing me? For being sick?

MR. REED: I remember the day you started, Katie. You fit right in. And you didn’t rock the boat. I suggest you don’t start now. I’m sorry you got sick. I’m sorry I have to let you go. It’s my job. It’s business, you know.

CATHERINE: No, it’s not. It’s a crime! *******

CATHERINE: (Pg 42) My bones [were] breaking . . . I couldn’t lift my little girl. I could barely cross the room. (Pg 46-47) No doctors in our town would see us. So we had to go to the city. (Scene shifts to the doctor’s office)

DR. DALITSCH: Catherine . . . the fainting spells and destruction of your teeth [is] connected to the malignancy of your hip and necrosis of your jaw (Sees that she doesn’t understand this word) Necrosis means . . . localized death of living tissue. To the best of my knowledge this is a direct result of radium poisoning. (Catherine breaks down into tears)

CATHERINE: (pulling herself together) Tell me . . . is Radium poisoning . . .

DR. DALITSCH: Terminal. *******

CATHERINE: (Pg 50) (alone on stage. The sound of a ticking watch in the background. As she speaks to the audience, she has more and more trouble moving her jaw, we see her physically deteriorate in pain) This is the sound of a mother’s heart breaking. (Long pause) This is the sound of her falling apart. (Long pause) This is the sound of time (beat) running out. (Scene shifts to Catherine and Tom’s apartment)

TOM: This guy, this doctor, he might be wrong. You ever think of that. From now on, all I want you to think about is getting better. I’ll do everything. You just get better. That’s all you have to do, Okay?

CATHERINE: I am going to die. (Long pause) (Pg 62) I’m not afraid of death. Really, I’m not. (Long pause) I’m just afraid of how I’ll get there.

TOM: (Taking her hand, he speaks emotionally) No one on earth can hold a candle to you . . . No one in heaven will come close. *******

CATHERINE: (to audience) (Pg 52-53) Women like me don’t stir up trouble. We play nice and do what we’re told. (With strong conviction) [But] a big part of me wonders what it would feel like to hire the best lawyer I could find and go get / those sons of . . . [So we did] (Pg 56-57) (to audience) Our case went to court. Our story went to press. And the press went to town.

(through each of the reporter’s statements, the audience can see Catherine wither away)

REPORTER 1: A travesty is unfolding just outside of Chicago, where several disgruntled women are accusing a beloved company of foul play . . .

REPORTER 2: . . . allege that Radium Dial knowingly compromised their health, safety and lives.

REPORTER 1: . . . fired for poor performance.

REPORTER 2: . . . Radium Dial is known for paying generous wages to unskilled workers.

REPORTER 1: . . . . in spite of community pressure to step aside.

REPORTER 2: . . . grasping for a payday. ******

CATHERINE: (Pg 65) I won my case six times. The Radium Dial Company appealed six times. After losing all six, the company appealed to the United States Supreme Court . . .

REPORTER 1: (Pg 62) Mrs. Donohue came to the hearing today supported by her husband. Once healthy and alert, she weighted only 71 pounds and could hardly stand alone. . . . ******

TOM: (to audience) (Pg 65) She died 21 days later – [NOTE: This first line is spoken by one of Catherine’s co-workers (Pearl) in the original script – could be presented as a voice over before Tom speaks] (He takes out the pocket watch Catherine gave him, winds it slowly, looks at it for a moment, then speaks) (Pg 64) Do you know they pulled bones out of her body while she was still alive . . . Lifted them right out. (He starts to cry) Could you tell me what I’m going to do with all this goddamn time? (He caresses the watch and puts it back in his pocket.) *****

CATHERINE: (we hear the ticking of a clock, the ticking becomes a heartbeat . . then it stops. Silence, then Catherine speaks) (Pg 10) They say you see a light But you don’t. You see your life flash before your eyes. You see your story. Beginning . .

TOM: (Pg 13) You know, I look at you every day before I leave. I take a picture of you (mimes taking a photo) I take it with me up there; on the girders and beams . . . . Beautiful.

CATHERINE: (Pg 10) and middle . . .

TOM: (Pg 35) (angry) I told you the day you started that work is work! So we ache! So we’re tired! That’s what you signed up for, Katie! Remember, you wanted this job.

CATHERINE: (Pg 10) And the end . . .

TOM: (Pg 50) (Taking her hand, he speaks emotionally) No one on earth can hold a candle to you . . . No one in heaven will come close.

CATHERINE: (Pg 66- 67) And time stood still for just a minute, just for us . . . and we were (beat) shining.
```

---

## IC-0928: This Hurts from Almost, Maine

- Title: This Hurts from Almost, Maine
- Author (byline): John Cariani
- Work: Almost, Maine
- Publisher: Dramatists Play Service
- Publication date as stated: June 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MAN, WOMAN, MARVALYN, STEVE
- Teaser before the introduction: No
- Spoken words (computed): 1618
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Cariani
Book: Almost, Maine
ISBN: 978-0822221562
Publisher: Dramatists Play Service
Date (Month/Year): June 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: There is the love we find or fall into, the love we’re looking for or hoping for or, alternately, trying like hell to avoid.

ACTOR: And there is the love we embrace, the love that dies quickly or slowly, the love we walked away from years earlier – thus, the love that’s stand-in for anything and everything we ever wanted but never was ours.

ACTRESS: As the song on that TV commercial says, love hurts. Even for a young man who can’t feel any pain.

ACTOR: With dark echoes of the Garden of Eden, love enters this man’s life unexpectedly in his apartment laundry room – but at the same moment, so does pain.

TOGETHER: This Hurts from Almost, Maine by John Cariani

Lights come up on a woman finishing up ironing a man's clothes, in the laundry room of Ma Dudley's Boarding House in Almost, Maine. A man is sitting on a bench. The woman starts folding the man's shirt she was ironing, but thinks better of it, and instead, deliberately crumples it, and throws it into her laundry basket. She picks up the iron, wraps the cord around it, preparing to put it away. As she does so, she burns herself on it.

WOMAN: Ow! Dammit! (The man takes note of this and writes "iron" in a homemade book labeled "Things That Can Hurt You." Meanwhile, the woman has exited to return the iron to its proper place. She returns to deal with the ironing board, which also must be returned to its proper place —the same place she just brought the iron. After folding up the ironing board, she turns to exit and accidentally wallops the man in the head with the ironing board, knocking him off the bench he was sitting
```

### Performance text (classify this)

```text
on.) Oh, no! I'm sorry! I'm sorry! Oh ... I didn't see you, are you okay?!?

MAN: (Unfazed.) Yes

WOMAN: No you're not!! I smashed you with the ironing board, I wasn't even looking! Are you hurt?

MAN: No.

WOMAN: Oh, you must be!! I just smashed you! Where did I get you?

MAN: In the head.

WOMAN: In the head!?! Oh, (Going to him.) come here, are you okay?

MAN: Is there any blood?

WOMAN: No.

MAN: Any discoloration?

WOMAN: No.

MAN: Then I'm okay.

WOMAN: Well, I'm gonna go get you some ice.

MAN: No. I can't feel things like that.

WOMAN: Like what?

MAN: Like when I get smashed in the head with an ironing board. I don't get hurt.

WOMAN: What?

MAN: I can't feel pain.

WOMAN: Oh, Jeezum Crow (Say, "JEE-zum CROW"— it's euphemism.), what have I done to you?

MAN: Nothin'—-

WOMAN: You're talkin' loopy, listen to you, goin' on about not being able to feel pain, that's delusional, I've knocked the sense right outta ya!

MAN: No, I'm okay.

WOMAN: Shh! Listen: I was gonna be a nurse, so I know: You're hurt. You just took a good shot right to the head, and that's serious.

MAN: No, it's not serious. I don't think an ironing board could really hurt your head, 'cause, see, (Forcing his "Things That Can Hurt You" book on her.) ironing boards aren't on my list of things that can hurt you,

WOMAN: (Dealing with his book.) What is — ?

MAN: plus, there's no blood or discoloration from where I got hit, so ...

WOMAN: Well, you can be hurt and not be bleeding or bruised —

MAN: And my list is pretty reliable, 'cause my brother Paul is helping me make it, and I can prove it to you: See, I bet if I took this ironing board, like this, and hit you with it, that it wouldn't hurt you (He smashes her in the head with the ironing board.), see?, that didn't hurt.

WOMAN: OW!! (Scrambling to get away from him.)

MAN: Oh!

WOMAN: Ow! What the hell was that?! // Why did you do that?

MAN: Oh! I'm sorry. Did that hurt?

WOMAN: God!

MAN: Oh, it did, didn't it?

WOMAN: Ow!

MAN: Oh, I didn't think it would 'cause, see, ironing boards are not on my list of things that can hurt you, but, gosh, maybe they should be on my list, because —

WOMAN: What are you talkin' about?

MAN: I have a list of things that can hurt you, my brother Paul is helping me make it, and ironing boards aren't on it.

WOMAN: Well, that ironing board hurt me.

MAN: Yeah.

WOMAN: So you should add it to your list.

MAN: Yeah. (Beat. He adds "ironing boards" to his list of "Things That Can Hurt You." He then picks up a book labeled "Things to Be Afraid Of.") Should I be afraid of ironing boards?

WOMAN: Well, if someone swings it at your head and wallops you with it, yes ...

MAN: Well, it's not — I have a list of things to be afraid of, too — and ironing boards are not on this list either.

WOMAN: Well they shouldn't be, really.

MAN: No?

WOMAN: No, you shouldn't be afraid of ironing boards.

MAN: No?

WOMAN: No.

MAN: But they can hurt you.

WOMAN: Yeah.

MAN: So I should be afraid of them.

WOMAN: No.

MAN: So I shouldn't be afraid of them?

WOMAN: Right.

MAN: But they can hurt me.

WOMAN: Well, if they're used the way you used it, yeah.

MAN: Oh-oh-oh! So, they're kind of like the opposite of God!

WOMAN: What?

MAN: Well, ironing boards can hurt me, but I shouldn't be afraid of them, but God, my brother Paul says, God won't hurt me, but I should fear him.

WOMAN: I guess.

MAN: Boy, this is getting very complicated.

WOMAN: What is?

MAN: This business of learning what hurts, what doesn't hurt, what to be afraid of, what not to be afraid of.

WOMAN: Are you sure you're okay? You're just goin' on and on about crazy stuff —

MAN: Oh, yeah, yeah, see, I have congenital analgesia, he thinks. Some // people —

WOMAN: What?

MAN: Congenital analgesia.

WOMAN: Who thinks?

MAN: My brother Paul. Some people call it hereditary sensory neuropathy type four, but ... it just means I can't feel pain. You can hit me if you want to, to see!

WOMAN: No.

MAN: Go ahead. It won't hurt. See? (He hits his head with the book. Composition books work pretty well, because they make a great sound and don't actually hurt!)

WOMAN: OW!

MAN: See? (He hits his head again.)

WOMAN: OW!

MAN: See? (Hits his head again.)

WOMAN: OW!

MAN: Go ahead. (He offers her the book labeled "Things That Can Hurt You"so she can hit him with it.)

WOMAN: No!

MAN: Come on!

WOMAN: No!!

MAN: Come on !

WOMAN: NO!!

MAN: Okay. You don't have to. Most people don't. Hit me. Most people just go away. You can go away, too, if you want to. That's what most people do when I tell them about myself. My brother Paul says I just shouldn't tell people about myself, because I scare them, (Referring to his book labeled "Things to Be Afraid Of" so he can show her.) so I've actually recently put "myself" on my list of things to be afraid of, but — (Her curiosity getting the better of her, the woman comes up from behind the man and wallops him on the back of the head with the book labeled "Things That Can Hurt You. ")

WOMAN: Oh, my gosh! I'm sorry! Oh, my gosh! I just clocked you!

MAN: You hit me! Most people go away, but you hit me!

WOMAN: I had to see [what would happen]! But — are you okay?

MAN: Yeah, I don't feel pain!

WOMAN: ... Don't feel pain, right, of course you're okay! — But — are you sure?

MAN: Well, is there any blood?

WOMAN: No.

MAN: Any discoloration?

WOMAN: No.

MAN: Then I'm okay.

WOMAN: Well, buddy, you can be hurt and not even look like it.

MAN: But —

WOMAN: Trust me. There are things that hurt you that make you bruised and bloody and there are things that hurt you that don't make you bruised and bloody and ... they all hurt. (Beat. Then, giving him back the book labeled "Things That Can Hurt You":) I'm Marvalyn.

MAN: I'm Steve. I live on the third floor. Room Eleven.

MARVALYN: (Deflecting.) I live with my boyfriend, Eric. I love him very much.

STEVE: Yeah. We saw you move in.

MARVALYN: Yeah. Our roof collapsed from all the snow in December. We're just here until we can get our feet back on the ground.

STEVE: Oh. Well, that's good, 'cause that's what Ma Dudley says her boarding house is. A place where people can live until they get their feet back on the ground. My brother Paul says we've been trying to get our feet back on the ground our whole lives.

MARVALYN: Oh.

STEVE: Yeah, it takes some people longer to do that than others.

MARVALYN: Yeah. (Beat.)

STEVE: You guys are loud.

MARVALYN: Huh?

STEVE: You and Eric. You yell and bang. We're right below you.

MARVALYN: Oh. Sorry about that. We're goin' through a rough patch. Happens. Sorry. (Beat. Then, changing the subject:) What is it like?

STEVE: What?

MARVALYN: To not feel pain.

STEVE: I don't know. I don't know what it's like to hurt, so ... I don't know. I don't really feel.

MARVALYN: Is this ... how you were born?

STEVE: Yeah. I don't have fully developed pain sensors. They're immature, my brother Paul says //, and because they're immature —

MARVALYN: How does he know that?

STEVE: Oh, he reads,

MARVALYN: But —

STEVE: and because they're immature, my development as a human being has been retarded, he says,

MARVALYN: But —

STEVE: but he teaches me what hurts, though.

MARVALYN: Why??

STEVE: So I won't ruin myself. I have to know what hurts, so I know when to be afraid. See, my mind can't tell me when to be afraid, 'cause my body doesn't know what being hurt is, so I have to memorize what might hurt.

MARVALYN: Okay...

STEVE: And I have to memorize what to be afraid of. (Showing her, in his book.) Things like bears. And guns and knives. And fire. And fear — I should fear fear itself— and pretty girls ...

MARVALYN: Pretty girls?

STEVE: (He thinks she's pretty.) Yeah.

MARVALYN: Why should you be afraid of pretty girls?

STEVE: Well, 'cause my brother Paul says they can hurt you 'cause they make you love them, and that's something I'm supposed to be afraid of, too — love — but Paul says that I'm really lucky, 'cause I'll probably never have to deal with love, because I have a lot of deficiencies and not very many capacities as a result of the congenital analgesia.

MARVALYN: Wait, what do you mean you're never gonna have to deal with love //, why —

STEVE: 'Cause I'm never gonna know what it feels like, Paul says.

MARVALYN: Well, how does he know that?

STEVE: 'Cause it hurts.

MARVALYN: It shouldn't.

STEVE: And, plus, I have a lot of deficiencies and not very many capacities.

MARVALYN: You know what, a lot of people do. (She kisses him. At first it's just Marvalyn kissing Steve, but, eventually, Steve participates. Then Marvalyn breaks away.) I'm sorry. I'm sorry. I'm so sorry. Are you all right? Are you okay?

STEVE: (Doesn't quite know how to respond. He hasn't learned about this. Then, maybe feeling his lips, and resorting to his usual way of answering this question.) Well ... is there any blood?

MARVALYN: No .

STEVE: Any discoloration?

MARVALYN: No.

STEVE: Then I'm all right. (Is he?)

MARVALYN: Yeah. You are. (Beat.) I'm so sorry I did that. It's just— ... You're just very sweet.

STEVE: (Trying to make sense of what just happened.) But ... you have a boyfriend and you love him very much.

MARVALYN: (She begins gathering her stuff.) Yes I do. And yes I do.

STEVE: And you just kissed me.

MARVALYN: Yes I did.

STEVE: And it's Friday night and you're doing your laundry.

MARVALYN: Yes I am.

STEVE: And people who are in love with each other, they don't kiss other people and do their laundry on Friday nights, I've learned that. People who are in love with each other, they go to The Moose Paddy on Friday nights, or they go dancing together, or they go skating. And they kiss each other. They don't kiss other people — you know what? I don't think that's love, // what you and your boyfriend have —

MARVALYN: (Deflecting, preparing to leave.) I've been down here longer than I said I would be and he doesn't like that.

STEVE: Who?

MARVALYN: My boyfriend.

STEVE: Who you love very much.

MARVALYN: Yes.

STEVE: Even though you kissed me?

MARVALYN: Yes.

STEVE: Wow, I'm going to have to talk to my brother Paul about this —

MARVALYN: No! Don't talk to your brother Paul about this! Tell him to stop teaching you.

STEVE: What?

MARVALYN: Whatever he's teaching you. Tell him to stop. What he's teaching you ... isn't something you wanna know.

STEVE: But I have to learn from him —

MARVALYN: Look: I was gonna be a nurse, so I know: You need to go to a doctor, and not have your brother read whatever it is he reads.

STEVE: But —

MARVALYN: You know what, I gotta go.

STEVE: (Sits down on the bench.) Right. You gotta go. You're—you're leaving. I knew you would. That's what people do.

MARVALYN: No, I just have to — .1 told you, Eric // doesn't like it if—I

STEVE: Your boyfriend?

MARVALYN: Yeah, he doesn't like it if I'm down here longer than f. I said I'd be, and I've been down here longer than I said I'd be —(On this line, Marvalyn picks up the ironing board. Then, as she goes to put it away, she accidentally swings it around and hits Steve in the head, just as she did at the beginning of the scene. Steve gets knocked off the bench.)

STEVE: OW!

MARVALYN: Oh! I'm so sorry!

STEVE: OW!

MARVALYN: I'm so sorry!, are you all right? I can't believe I just did that to you again! \

STEVE: OW!!

MARVALYN: (She goes to help him; stops short.) Wait — : What did you just say?

STEVE: (As he rubs his head, he realizes what he just said. Beat. He looks at Marvalyn, tells her plainly:) Ow. (Music. Marvalyn and Steve just look at each other. Utter uncertainty. This is scary. And wonderful. But mostly a little scary — because who knows what's next. Lights fade.
```

---

## IC-0929: This is Where it Ends

- Title: This is Where it Ends
- Author (byline): Marieke Nijkamp
- Work: Not specified
- Publisher: Sourcebooks Fire
- Publication date as stated: Jan 2016
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: PRINCIPAL TRENTON, AUTUMN, FATHER, TYLER
- Teaser before the introduction: Yes
- Spoken words (computed): 1396
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
ACTRESS: This is Where It Ends by Marieke Nijkamp.
```

### Performance text (classify this)

```text
Suggested Roles:

Actor: Principal Trenton, Father, Tyler Actress: Autumn

(NOTE Principal and Father appear only in the cut-away intro) This selection is primarily a 2-Character cutting.

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

## IC-0930: Thtick ‘Em Up

- Title: Thtick ‘Em Up
- Author (byline): Barbara Lhota and Janet B. Milstein
- Work: VOLUME 1: Forensics Series, Duo Practice & Performance: Thirty-five 8-10 Minute Original Comedic Plays
- Publisher: Smith and Kraus Date (Month/Year) April 2003
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, JANICE, TROY
- Teaser before the introduction: Yes
- Spoken words (computed): 1423
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barbara Lhota and Janet B. Milstein
Book: VOLUME 1: Forensics Series, Duo Practice & Performance: Thirty-five 8-10 Minute
Original Comedic Plays
ISBN: 978-1575253084
Publisher: Smith and Kraus
Date (Month/Year) April 2003
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: Thick Em’ Up by Barbara Lhota and Janet B. Milstein
```

### Performance text (classify this)

```text
CHARACTERS: TROY: mid-20s, a mugger and JANICE: mid-20s, an angry commuter

(Suddenly, Troy jumps out of the alley.)

JANICE: (Screams.) Ahhhhhh!

TROY: Shh, shh, shh!

JANICE: Don't shhh me! What is your problem? You shouldn't jump out of alleys in front of people.

TROY: I'm thorry. I'm thorry. I wasn't thrying to sare you, sare you - (Shaking his head.) scare you!

JANICE: OK. Fine. Apology accepted. (Mumbling to herself) Be patient. Do not blow up. Obviously from the state facility.

TROY: (Following.) Hey, I juth need to athk you thomething.

JANICE: Oh great. Look, I can tell you right now, you will not get my hard-earned cash. What's left of it anyhow. You looking for a handout? Go back to school. (She walks faster.)

TROY: (Running after her, following, whispering.) Give me your furth.

JANICE: (She stops and turns.) What?!

TROY: Give me your furth!

JANICE: My wh - what?!

TROY: Furth! Furth! You hearf me!

JANICE: Well, I may have "hearf" you, but I didn't understand you. Do you understand this? (Pretending to do sign language.) I do not understand furth. (Opening and closing hands toward him.)

TROY: Wewl, you know what I mean!

JANICE: No, I don't! Maybe if you'd take that ski mask off your face, idiot, you could. (Overenunciating.) Enunciate your words and I'd understand.

TROY: Your muh-ey! Your muh-ey!

JANICE: Muh-ey? Yeah. Muh-ey. OK!

TROY: I'm not k-kidding, lady! I want your muh-ey! (Holding out his hand in his pocket.) I have a kun in my focket!

JANICE: (Beat.) Uh-huh. Good for you.

TROY: No! (Points down to his pocket.) A kun, a kun, a gaga - gaaan!

JANICE: Gaaa - Gun? Are you trying to say you have a gun in your focket?!

TROY: Yeth!

JANICE: Are you trying to say. . . (loudly) are you trying to rob me?

TROY: Yeth!

JANICE: (Even louder.) Help! He wants my purse!

TROY: (Putting his finger to his lips.) Shhhhhhhhhhhhhth!!

JANICE: (Calling across the street.) Sir, oh sir, help! (To Troy who doesn't know what to do.) See, he sees me! (Looking across the street.) Heeeelllllp! (Beat.) Where are you going? Can't you see this man is . . . ? (To man across the street.) You suck, you. . . bad man!!!

TROY: You should be sare. I could take you in the alley.

JANICE: And do what?! Take my three dollars and two maxed out credit cards?

TROY: Thwee? Dat's all?

JANICE: Yeah! And a box of feminine hmm-hmms. Which you cannot have! Those things cost an arm and a leg.

TROY: Are you thure you're not wying to me about the thwee bucks?

JANICE: You want to count it, you little defect?

TROY: Defect? Dat's not nithe. I have a kun. You should be sare.

JANICE: (Imitating him, making him sound whiney.) "You should be sare. You should be sare." I'm not sare!

TROY: (Grabbing her arm.) I'll take you in the alley if you keep theaming.

JANICE: I'm not theaming! And I'll cut your head off if you take one more step. How do you like that threat? (Annoyed.) Now, let go of my arm. Let go!

TROY: (He does.) I'm thorry.

JANICE: You should be. (Rubbing it.) That hurt my arm.

TROY: OK. God. But you're juth thapposth to give me your furth. And I'll go. I'll go.

JANICE: You know what, buddy, I'm sorry to disappoint you, but I'm keeping my purse. Hmm-hmms and all. You picked the wrong lady to rob tonight. OK? You know why? I don't care if I die. In fact, I don't think I will. I think it's more likely that you will die!

TROY: I don't have time for thith!

JANICE: Ohhhhhh, well, you may not, but I have time. I have plenty of time. You know why?

TROY: No.

JANICE: Because I was fired today. (Screaming at him.) Fired!

TROY: (Jumping.) You don't haf to theam everything.

JANICE: I'll theam when I want to theam! You see, I don't have control. I'm not "good with authority." I "fly off the handIe." I have "poor anger-management skills." I don't get along with others. (Doing flaky imitation.) "I create a negative climate!"

TROY: (To himself.) I don't know what I'm doing wong.

JANICE: (Sighing.) So I get a little crazy one time and dent the kitchen wall of the Burnstein's with my head? That's why we have extra two by fours. That's why we have cement filler. (Screaming.) That's why we have white paint!

TROY: You dented a wawl with your head?

JANICE: Well, at least I'm not inept like you. You know you're a total disaster at this thing?

TROY: Disathter? What am I doing tho wong?

JANICE: What are you doing right is the question? It was obvious from the beginning that you'd never done this before.

TROY: It wath?

JANICE: Yes, for one, saying you're sorry for jumping out at me didn't help. No offense. But you have to sound a tiny bit confident to get action.

TROY: I did, I did! Didn't I?

JANICE: Are you kidding? And you got to look like you know what you're doing.

TROY: I did.

JANICE: Well, now, don't get insulted!

TROY: I'm not! I juth want to know what I did wong.

JANICE: Well. . . the ski mask is a dead giveaway.

TROY: Wheally?

JANICE: Yeah. Take it off! Nobody wears a ski mask when they rob people anymore. It's just. . . out. Muggers know darn well that cops aren't going after one person who mugs someone for a couple of bucks. They're going after huge gangs - hell, drug dealers, terrorists, CEOs. They don't have time for schmucks like you.

TROY: Yeah?

JANICE: SO the ski mask just makes you look really unprofessional and you're probably all hot under it. It's safe to take it off. Go ahead.

TROY: You think? (She nods.) I do feewl a wittle fainty. (He takes it off)

JANICE: That's better. And this gun threat of yours? Really dangerous. You're lucky I came by. In this neighborhood, somebody else might have taken one look at you and your little "kun in your focket" and pulled out an Uzi and blown your head off. (Doing imitation.)

TROY: (Cringes.) You're whight.

JANICE: And not to get into what I imagine is probably a sore subject there, but you do have a little. . . speech

TROY: I know. . .

JANICE: Well, it's an issue! You can't mug people if they can't understand you.

TROY: Well, it's not dat bad when I'm not nervouth. You underthood me.

JANICE: Eventually. But there was a major communication block with purse, money, and gun in your focket - pocket. You know what I mean? These are important words to communicate during a mugging.

TROY: Yeah, yeah. Twue. But I've been woo king on my wisp thing for yearth now. What am I thuppothed to do?

JANICE: Keep practicing. (Looking at him.) You know you look very familiar now that I look at you. That lisp of yours reminds me of this dweeby kid I had a crush on back in grade school. I used to pick on him so bad because he was a little skinny, short guy, but when we were in gym class he sweat like a pi . . . oh my . . . Troy F-f-franklin?!

TROY: Janithe Afterbirth?!

JANICE: Alberts, Alberts! Oh my God! So how are you?

TROY: Well. . . not so good as you can thee. Actually, I only rethorted to this because of my thon.

JANICE: You have a son?

TROY: Yeth.

JANICE: SO you got married?

TROY: Yeth.

JANICE: (Disappointed.) Oh.

TROY: Yeah, but we're divorth.

JANICE: (Interested.) Oh. (Trying to cover.) Oh, that's too bad.

TROY: Yeah. We got mawied whight out of high school. It was too early. I wanted tho me one with a wittle more sthability. Bethides, I don't wheally think she liked me.

JANICE: How could she not like you? You're so sweet.

TROY: Thank you. Are you mawied?

JANICE: No.

TROY: (Happy to hear this.) Oh. Well, it'th alwayth better to wait. You'll find thomeone.

JANICE: Yeah. If I want him. It's good being single. So what have you been up to job-wise?

TROY: Well, I thudied to be a twavel wep at this little speciality thool and I got a job whight away, and was working as a customer service wep for this small travel agency, booking tickets. Nobody said they couldn't understand me, but then this recession hit.

JANICE: Oh boy, don't you know it. Who wouldn't resort to mugging people?

TROY: It's wheally no excuse though. Really. I just wanted to get a little extra cash to pay for this electronic game little Carl wanted for Chrithmath tho bad. I juth thought if I could peacefully wob one nithe lady who was wobbable and had a wad of cash, I could get him thome stuff.

JANICE: Yeah. Hey, you thought I looked nice? Robbable?

TROY: Yeah. Real nice. Real Robbable.

JANICE: God. Thanks. That's really nice to hear.

TROY: You know, I wheally don't understand this anger management problem this boss says you have. You seem really in control and sane.

JANICE: By the way I'm sorry I threatened to cut your head off earlier.

TROY: Hey, like you said, it happens. I’m Glad I decided to stick you up tonight, even though you didn't understand a word of it.

JANICE: Yeah, well, I'm glad I had you take off your mask.

TROY: Yeah, you too. (She nods.) I mean, I'm glad I took it off too.

JANICE: SO. (Beat.) Dmm . . . Well. . . cool. I'll just see you around?

TROY: Wait. Dh, uh so what are you up to tonight, Janice? I have thome hot chocolate back at home. And a few old ugly plates you could definitely throw.

JANICE: Yeah? Are you asking me to . . .

TROY: Well, maybe, I, I, I'm - if, if, if - but if not

JANICE: You know, I always thought that was so cute.

TROY: Thanks. (Looks down.) (She takes his arm.)
```

---

## IC-0931: Time Flies

- Title: Time Flies
- Author (byline): David Ives
- Work: Time Flies and Other Short Plays
- Publisher: Grove Press Inc.
- Publication date as stated: March 2001
- Event as filed: Duo Interpretation
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
Date (Month/Year): March 2001
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

## IC-0932: Time Share

- Title: Time Share
- Author (byline): Neil LaBute
- Work: Seconds of Pleasure: Stories
- Publisher: Grove Press
- Publication date as stated: Oct 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SHE, HE
- Teaser before the introduction: No
- Spoken words (computed): 1538
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil LaBute
Book: Seconds of Pleasure: Stories
ISBN: 0802117856
Publisher: Grove Press
Date(Month/Year): Oct 2004
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: The facts about marital infidelity are astounding. Polls show that although 90% of married people disapprove of extramarital relationships, statistics from a national survey indicate that 15% of wives and 25% of husbands have experienced an extramarital affair.

ACTOR: Another source, The Monogamy Myth, authored by Peggy Vaughan, approximates that 60% of husbands and 40% of wives will have an affair at some time in their marriage.

ACTRESS: Every day in America, seemingly happily married couples face the very real aftermath that the discovery of marital infidelity can bring to a relationship.

ACTOR: Rationalizations, explanations, grief, anger – Marriage is not the appropriate relationship to propose a . . .

TOGETHER: Time Share by Neil LaBute
```

### Performance text (classify this)

```text
SHE: Say that again.

HE: What, about before?

SHE: Yes, that. Please.

HE: Well, see, we, ummm . . . . the two of us had actually met before.

SHE: Before?

HE: I mean, before we met. From before we, that is you and I, knew one another.

SHE: Really?

HE: Yeah. We went to the same college and . . .

SHE: Oh. So ... you were in school together?

HE: No, no, not together. It was in Kansas, but not overlapping or anything. No, we actually ran into each other in the city one time, during this coed softball game of alumni in Central Park.

SHE: Quaint.

HE: Which is kind of funny . . .

SHE: Why? Why is that funny?

HE: Well, it's, you know . . . Manhattan. And that's where we went to school, too. Manhattan, I mean. In Kansas. Because Kansas State is in. . .

SHE: Yeah, Manhattan. I get it. It's just not that funny.

HE: Right. Anyway, that's where we were, over by the softball fields, and, see, we got talking about stuff, had a couple drinks, you know, and we just hung out a few times or whatever.

SHE: I think they still call it ‘dating,' even in New York.

HE: No it wasn't like a 'thing'! We didn't date or anything, we just . . .

SHE: Slept together.

HE: . . . something like that. Yeah, this one time we did, yes. Do that, I mean. Not sleeping together, though, just some sex stuff. Sort of. But it was nothing . . .

SHE: So that makes it all right, then . . . what I saw.

HE: No, not all right, I'm not saying that, I just mean . . . I dunno, just that there's some background there. A shared background between us.

SHE: Right. I see. I get it. I do. I do get it.

HE: So, it's not like, I mean ... a 'fling' or anything.

SHE: It isn't?

HE: Well, OK, yes, a fling, but ... a fling with qualifiers. With history.

SHE: You didn't tell me, though. About this 'history' of yours, I mean. All this time and you didn't say anything.

HE: No, I didn't do that.

SHE: Why?

HE: I thought that I wouldn't, you know . . .

SHE: Uh-uh, no, I don't know. What? Get caught?

HE: No. B-b-be understood.

SHE: Well, you're right, you wouldn't b-b-be, but that shouldn't stop you from telling me!"

HE: What was I gonna say?

SHE: I don't know, it's not really my moral dilemma, is it?

HE: It's not a . . . OK, yeah, it is, like, a moral thing, but I think we can still . . . "

SHE: Still what? What? I'd love to hear how that sentence ends. Tell me.

HE: . . . work something out? Or . .

SHE: You think we should work it out, do you? Is that what you think?

HE: I think we could try.

SHE: Try what, talking? Just, like, talking, you and me?

HE: We could, yes. That would be . . . If we can't talk about this like adults, then we might as, well . . .

SHE: Adults? Oh, you wanna talk like ad-ults, is that what you'd like?

HE: It's why I came back over here, yes.

SHE: No, you came back over because this is your house, OK, this is your home. Where you live! What'd you think, you could just live in the pool house there, set up a little place for yourselves or something?

HE: No. Of course not. Look, I don't know what you think you saw . . .

SHE: Oh, please, come on . . .

HE: No, seriously, what? We weren't . . .

SHE: Your trunks were down, all right?

HE: They weren't . . . OK, whatever. You know what you know.

SHE: No, not whatever. I saw you, very clearly, your suit around your knees. Your back was toward the door and. . . do you really wanna hear more?

HE: . . no. But . . .we knew each other in New York . . .

SHE: What does that mean?! You keep saying that but it doesn't seem to mean anything. Lots of people know each other in the city, but that doesn't mean they're all doing it. Does it?

HE: No, but, see . . .we went to the same college and we got talking one time, we had a lot to drink and we just . . . it wasn't like this big thing.

SHE: But you didn't tell me.

HE: No.

SHE: They've been moved in there, next door, in their time-share for three weeks. A month maybe. Since Memorial Day . . .

HE: I was going to say something . . .

SHE: But you decided to keep it all to yourself, huh?

HE: No! God, you're so . . .we were both nervous about it. I mean, embarrassed.

SHE: Obviously . . .

HE: We were! When they introduced themselves that first day, out there on the deck, I could hardly look up . . . Jesus, let me at least tell my side of it.

SHE: Please . . . go ahead.

HE: So, you know . . .if you don't take that moment, I mean, that first moment there and tell the truth, then you're stuck. You are.

SHE: And since you didn't tell me out on the porch that day, you just figured this tiny detail was no big thing. I mean, not a real problem for us . . .is that kind of what you're saying?

HE: Sort of . . .

SHE: Huh.

HE: What's that mean?

SHE: Just 'huh,' no other real meaning to it . . ." [Her head cocks a touch now, slightly to one side as she studies him. Glancing at his eyes but then down, to settle at crotch level. Holding this look for quite some time. He shifts from one bare foot to the other.]

HE: What're you doing?

SHE: Nothing. Just imagining . . .

HE: Imagining?

SHE: Imagining what it'd be like for your son to walk into that shed. Looking for, oh, I dunno, some diving sticks or an inner tube or who knows what, and see that. What I saw . . .

HE: What? We knew each other in Manhattan . . .

SHE: Stop saying that!

HE: We were just talking . . .

SHE: Please don't do that! Don't assume I've been nearsighted all these years on top of being an idiot . . . Would you like it, if he saw that?"

HE: No. Of course not. . .

SHE: Well, that's something . . . Because I couldn't really see . . .my eyes hadn't adjusted. I was pretty sure that's what was happening there, with the two of you, but I wasn't completely. Certain, I mean. Because of the dark. But, hey, now I know . . .

HE: Listen, we were just . . .

SHE: Right. Yeah, college, I know . . . The big game and all.

HE: Yep . . . I mean, you're in the city, right? And you run into a bunch of folks from home, you know, men and women out there on the grass having fun, and you just sort of get caught up in the thing . . .few beers . . .I can't really explain it better than that . . .Does that make any sense?

SHE: No, none. But I understand. I understand that it makes sense to you . . . somehow.

HE: It does. I know it sounds wobbly, but . . .S

HE: And since it does, make sense, I mean, you'll need to explain it to them . . .

HE: Who?

SHE: The children.

HE: . . what do you mean?

SHE: You're going to need to sit them down—they're back from swimming in forty minutes—and you'll need to walk them through this as best you can.

HE: No, I can't . . .what?

SHE: My leaving, I mean. You'll need to come up with something for that. Tell them the rest if you want to, but you have to explain where I've gone.

HE: But where are you . . .?

SHE: To the city, I suppose. For the night, anyway. I need to call my sister, and the lawyers, no doubt. I need to handle a few things.

HE: I can't tell them that! I mean, they're only . . .

SHE: What, children?

HE: Yes.

SHE: Children bounce back. They do, that's their lot in life. You explain things and on Saturday we'll get them on a train, back into town, and they'll be out of your hair. Then you can go back over the fence . . .

HE: But I don't want to.

SHE: Then don't.

HE: I want to . . .I mean, I'd like to, I'd really like to see if we could . . .

SHE: What? [She waits for him to finish but he only repeats the previous phrases over and over. Finally, she picks up her bag, tests the weight of it, then moves toward the door.]

HE: Do you want me to carry that down or . . .?

SHE: No, no, it's fine. You've done enough, believe me . . .

HE: I love you guys. I do.

SHE: Well, that's something you can hang on to, isn't it? You can tell the kids that, if it helps . . .tell them I love them, too.

HE: We were just talking . . .we spent time on the same campus, for Chrissakes! SHE Yeah, I caught that part . . .

HE: We did . . .

SHE: I know.

HE: And we had some . . .

SHE: When did you become so pathetic?

HE: . . . I'm not sure.

SHE: Huh.Tell me one thing . . .

HE: Yes?

SHE: What position did he play?

HE: Huh?

SHE: Our neighbor . . .the guy who was . . . When you met him, what position was he playing?

HE: Oh . . . catcher. He was their catcher.

SHE: . . . I see. I get it now . . .The significance of it all.

HE: What do you mean?

SHE: Come on, he's the catcher . . .you don't know anyone, you're lonely, it's New York, this guy's kneeling at your feet, you've got your nice, firm bat there . . . I get it. It's symbolic . .

HE: It . . .it was an experiment, that's all. Just . . . guy stuff. Kind of, like, you know . . .

SHE: No, you're right. It happens. It does. In 'Manhattan,' anyway . .

HE: We were only . . .see, I met him before we, I mean, you and me . . .

SHE: . . . I hope you're very happy." [Before he can say anything else she is gone]

HE: [Alone on stage] It's OK, it is, it's OK, this is gonna be . . .it's all right. Things'll be fine. It's . . . OK, this is all O-K . . ."
```

---

## IC-0933: To the Airport

- Title: To the Airport
- Author (byline): Julianne Bernstein
- Work: More One-Act Plays for Acting Students
- Publisher: Meriwether Publishing Company
- Publication date as stated: July 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: WOMAN'S VOICE, MARCIA, TED
- Teaser before the introduction: No
- Spoken words (computed): 2001
- Already set (do not supply): none

### Source block (context only)

```text
Author: Julianne Bernstein
Book: More One-Act Plays for Acting Students
ISBN: 978-1566080873
Publisher: Meriwether Publishing Company
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
TED: Try therapy.

MARCIA: You shouldn’t have to pay someone to listen to you.

TED: What about friends?

MARCIA: They’re too involved in the situation.

TED: boyfriend?

MARCIA: He IS the situation.

TED: Pick a random person.

MARICA: Like who?

TED: Like a cab driver.

BOTH: “To the Airport”

TED: By Julianne Bernstein
```

### Performance text (classify this)

```text
(TED sits in his taxicab. He is parked and waiting. He beeps the horn, which sounds twice. He pulls out a postcard from his shirt pocket, reads it, smiles and puts it back. He beeps the horn again. He looks at his clipboard. confirms the address, gets out, goes around the cab and looks up. He gets back in the taxicab. He switches from "park" to "drive" when the sound of a large heavy door slamming and a woman 50 voice is heard.)

WOMAN'S VOICE: You bastard! I don't care if you stay and rot! Along with the Chinese take-out you took out last Friday! Don't you follow me! I don't want to see your face! (It is MARCIA. She enters with several large suitcases. She throws them down on the ground and speaks Upstage Right, as if she :s yelling to the sixth floor of a high-rise.) Don't follow me! You hear me?!

(TED honks the horn.)

MARCIA: (To TED) Yeah, yeah. I'm comin'.

TED: If this isn't a good time, I could come back later.

MARCIA: And what am I gonna do with you later? Kennedy Airport. Now!

TED: You sure you wanna get in this cab? In your state of mind? ,

MARCIA: If you're here to make my life miserable, you can take a number. (Pause) Bobby?! Hey, Bobby, do you hear me?!

TED: (Pause) I can't believe he don't hear ya.

MARCIA: (To TED) Shut off that damn engine. Shut it off!

TED: I got the meter goin'.

MARCIA: For what? You're charging me to stand on the curb? Did you hear me? I said shut if off! (He does so.) I'm tired of it! Five years I'm with you, what do I get? No ring. No promise, even. I'm tellin' you. A dishwasher is no real sign of love. No, sir. You can't even say it. "Marriage," Bobby. The word is "marriage." I can see it now. My fortieth birthday. My fiftieth. And still no ring. You'll bring me another sweet, forget-me-not appliance, you will. (Pause) A little gold won't kill you, Bobby. A little gold won't break you!

TED: Excuse me, but

MARCIA: (To TED) What? What?!

TED: Two-thirty-five West 41st? Sixth floor? Is that who you're talkin' to? The sixth floor?

MARCIA: No, I got a special problem with my neck, and I'm talking to the couple in the basement. Come on. The bags. They're growing mold out here. (TED gets out; he loads the baggage in the trunk. MARCIA looking up) And don't call. You better not call. I'm changing my name. The long distance operator'll laugh in your face. "Who?" "Marcia who?" they'll ask. "Who the hell you talkin' about?" "There's no ..." Aha! You thought I'd say it... my name. My new name. Well, forget it! (TED is finished loading the suitcases. He walks up to her and opens her door.) What's this? Limo service? I'll open my own door, thank you. (She gets in and slides to the left. TED is about to shut the door.) I'll shut my own door. Double thank you! (Leaving the door open, he steps around to the front, and gets into the driver seat. MARCIA slides back to the right to shut the door, but instead, gets out again.) I'm shutting this door, Bobby. I got my hand on the handle and I'm closin' it shut! Do you hear me?! (Pause) Do you get what I'm sayin'?!

TED: Lady, I got a life, too, you know!

MARCIA: (Quickly moving into the cab, and "threatening him at gunpoint") Go ahead. Start the meter. I dare you. (Calling out the window) I'm leavin' now, Bobby? Bobby, you hear me? You can start cryin'. Shed those buckets, Bucko! Cry! Cry! Cry! (She slams the door shut, sits still, and listens. After a beat) Turn the key. (Pause) Turn the key, I said. (He does. Sound of the engine is heard.) Hear that, Bobby? (She slides to the middle of the seat.) Go. (Pause) Drive. (He switches gears, checks his mirror and drives.)

TED: Boy, he sure did a number on you. At least he didn't throw you and your Wandering Jew out on the pavement!

MARCIA: What?!

TED: I had a pick-up in Queens just last night. This nice lookin' guy. He had real good skin. Sittin' there with a pillowcase full of clothes and his favorite Wandering Jew wandering all over the street. He didn't know what to do. The roots were torn to pieces - all the leaves were flyin' towards Flatbush.

MARCIA: So? What do you want? A medal for pickin' him up? A prize for doin' your job? All you guys - you want medals, trophies for just gettin' up in the mornin'! (Pause) Just get me out of here. I wanna go - go where no man has gone before.

TED: Yeah? Where's that? You goin' overseas?

MARCIA: Yeah. Overseas. Way overseas.

TED: Yeah? Wow. Can you believe I got no postcards from overseas? Plenty of domestics, but not a single card from overseas.

MARCIA: What the hell are you talkin' about? (He pulls out his card; he hands it to her.) What am I supposed to do with this?

TED: Write me. I'll write you back.

MARCIA: Excuse me?

TED: But I gotta have your address. Your zip code.

MARCIA: That's ridiculous. That's illegal.

TED: Hey, there's no way it'll work without the zip. It'll get lost and chewed up by those U.S. Postal pigs. It's gotta have a zip. You got mine. Now gimme yours. I'll write you.

MARCIA: What? Like a letter?

TED: Or a card if that's your pleasure.

MARCIA: What the hell for?

TED: Hey, it sounds like you could use your own personal Abby.

MARCIA: Who?

TED: Abby. Dear Abby. Come on. What's your zip? Gimme your zip.

MARCIA: You're crazy. I'll give you that. You're a loonie. I'll give you that much. (Pause) Now, be quiet. I got so much stuff tyin' up my brain right now. I wish I were dead. Yeah. Pretend I'm dead. Pretend you're driving a hearse. (Silence. To herself) He don't understand. He don't listen to me. That's the problem. He don't listen. He don't hear. I don't care about gettin' married. I mean, I'd like it and all. But I love him. I tell him that. But he don't believe me. I just want him to believe me. To hear me. (Bitingly) Well?

TED: Well, what?

MARCIA: You hear me? Are you deaf as well?

TED: No. I heard.

MARCIA: Yeah, what'd I say? Tell me what I said.

TED: You said: He don't understand. That, like, he don't listen to you. That that's the problem. That, like, he don't listen. That he don't hear. That you don't care about like gettin' married. You'd like, like it and all, but that you love him. And you tell him that. But like he don't believe you. That you just want him to believe you. To hear you. (Pause) Well?

MARCIA: (Pause) Right. You got it. Word for word. Like you got the back seat bugged.

TED: You know the best thing? Gettin' cards from places I dream about. I mean, I had a pick-up on Times Square 'bout a year ago, and guess where he was from? Guess.

MARCIA: I don't know. Paris?

TED: Kansas. I pick him up in the middle of Times Square, right under the Sony sign. Another real nice guy. Though his skin wasn't as clear. But we got to talkin'. Turns out he came to New York City to be somethin'. I don't know what. He didn't know what. It didn't work out. So we struck up a correspondence, and now I get cards from Kansas. Corn country and all that. I got Kansas all over my kitchen. How about it? All I need is the zip on two-thirty-five West

MARCIA: I'm leavin'. That's not my zip code anymore. I'm leavin'. Get it? I'm leavin'. (Silence)

TED: How come?

MARCIA: I don't know.

TED: Me, neither. I mean here and now. I don't know. But via the U.S. mail, I usually got this figured by now. Now, I'm aware of the rising cost of postage these days; I can't help that - but my advice will always be first-rate.

MARCIA: You know. That's all I ever wanted from him. Was his first-rate effort. I mean, I know he's gettin' old. Me, too. We're not runnin' naked through the living room to get to the Jiffy Pop popcorn anymore. It's just what happens after so many years. And sex is ... well ... it is what it is.

TED: It is?

MARCIA: It is.

TED: Sounds like you're going through maybe a mid-life thing.

MARCIA: Me? Mid-life? What kind of a thing is that to say? That's supposed to help me? Give me direction? A confirmation that I'm having a mid-life thing?

TED: I told you I'm no good in person, face-to-face. One on one. Ah, but on a postcard or sealed up in a letter? Pure gold. Believe me. Really. This one guy was writin' me all the way from Delaware. You know, the valley? He was having a hell of a time with his teenage daughter. She wanted to run away to Soho with her boyfriend and open up a store selling his oil paintings of traffic in Ohio and other suburbs, and her bracelets made out of gum wrappers and little wet rocks.

MARCIA: Wrappers and rocks? What'd you tell the father?

TED: A bunch of stuff. I mean, it was pourin' out of me. Like I was writin' fortune cookies or horoscopes. Like I was talkin' right out of the Ten Commandments.

MARCIA: So? What'd you tell him?

TED: After six pounds of stationery, I tell him to get off his tucas and go to the grand opening of his kid's store. I say to him, "Your own children will show you the way." That's what I wrote. Their little shop's on Bleeker Street, right next to the Lebanese Deli. It's very popular.

MARCIA: But the father. He was against it.

TED: Not after he saw what a good business they were doin'. He sent me a picture of his daughter. Oh, what a doll. A lovely shot of her workin' behind the counter. Dressed real responsible and all. A skirt with a blouse and a bow. Quite a lady, you know? (Silence)

MARCIA: Uh-oh.

TED: What?

MARCIA: Just follow the road. Terminal A.

TED: Yeah. Quick. Gimme your zip code. We'll get a correspondence goin'.

MARCIA: It's no good anymore.

TED: Come on. Just write me and tell me how you're doin'. I'll interpret what I read, and tell you what I think.

MARCIA: No! You're not gettin' my code. It's my code. Mine.

TED: (Pause) You need me to write you.

MARCIA: You don't know what I need.

TED: Yeah, I do.

MARCIA: Then tell me. Tell me. Tell me everything you know and make me see it in a different way. Make me see him in a different way.

TED: Whoa. You just can't order up advice like... like ... it's a pastrami sandwich or something. I need time to think ...time to ...

MARCIA: What? What?

TED: Let me have my card.

MARCIA: But I thought you

TED: I'll give it back. I'll give it right back. (TED takes a pen from his shirt pocket, and the card which MARCIA hands him. He scribbles a note on the back of the card.)

MARCIA: Hey, don't write while you're drivin'.

TED: I've been driving for fifteen years. I can put up a house of cards while I'm driving.

MARCIA: If we have even a little fender bender - you're dead, buddy.

TED: Be quiet. This is it. This is what you been waitin' for.

MARCIA: Just shut up and take the red arrow. No, the blue. Yeah, the blue ...

TED: Hang on.

MARCIA: I got a plane to catch. Let's go.

TED: 'What airline?

MARCIA: I'm not sure.

TED: What's your ticket say? Check your ticket.

MARCIA: Ticket?

TED: You don't have a ticket?

MARCIA: Not yet.

TED: You're expectin' to fly overseas with a ticket you bought ten minutes before?

MARCIA: What's wrong with that?

TED: That's stupid. You know how much you gotta pay?

MARCIA: I got money.

TED: You need a lot if you want a ticket right up front. I mean, unless you buy a year in advance, they'll charge you a thousand dollars just to fly to Detroit.

MARCIA: Nobody's gonna pay that much to go to Detroit.

TED: Hey, if you're stupid enough to fly to Detroit, you deserve to pay that much! (MARCIA starts weeping.) Hey, you're not stupid. I didn't mean it.

MARCIA: I get so tired of talkin' to him about it.

TED: You call that talkin'? You have to yell like that? He wasn't across the country, he was right there.

MARCIA: He was in the other room. In the bathroom. The shower. With his Walkman over his ears. How else am I going to talk to him?

TED: It sounds like he was checkin' out.

MARCIA: I know what he was doin'.

TED: (Looking in the rear-view mirror) Ah, get out of my face.

MARCIA: Hey, all I said was

TED: Not you. I got these Good Humor trucks tailing me.

MARCIA: (Pause) I hate talkin' in the bathroom. It makes me uncomfortable. (He hands her the card. She reads.) After you take a shower with him, go to the kitchen... and pop up some Jiffy Pop. (Pause) Forget the towel. (Silence. Taking a deep breath) There. Follow that road right there.

TED: It takes you right out of the airport.

MARCIA: I know.

TED: You gonna be OK?

MARCIA: I'll see. (Pause) I don't have a card for me.

TED: Yeah, I know. I know.

MARCIA: But I got yours. Thanks. (Pause) 20331. That's my zip. I don't know how long that'll be it. But that's it. That's my zip. 20331. For now, that is.

TED: (Smiling) 20331.
```

---

## IC-0934: Top Floor

- Title: Top Floor
- Author (byline): David Epstein
- Work: 2006: The Best Ten-Minute Plays for Two Actors
- Publisher: Smith and Kraus
- Publication date as stated: November 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GARY, SUSAN
- Teaser before the introduction: No
- Spoken words (computed): 1368
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Epstein
Book: 2006: The Best Ten-Minute Plays for Two Actors
ISBN: 978-1575255637
Publisher: Smith and Kraus
Date (Month/Year): November 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: It's every parent's worst nightmare: after months of waiting, the excitement of decorating the nursery, the hopes and the dreams you held for the new addition to your family ever since the very first positive pregnancy test now you're going home empty handed.

ACTOR: The death of a baby is one of the most devastating experiences that anyone can go through.

ACTRESS: At first, it may seem almost unreal to the mother and father and they may have difficulty accepting the stillbirth. As it sinks in though, they will go through an emotional journey that will affect every aspect of their lives.

ACTOR: In Top Floor by David Epstein Gary and Susan are six months into this emotional journey. The question is whether they will continue to travel together.

TOGETHER: Top Floor by David Epstein

Gary Lane comes through the front door with his wife, Susan. In their late thirties, they are a tall, sophisticated couple with smart clothes and tired faces. Susan shakes out a wet umbrella, takes off her coat, and examines the space. Gary sets down his wife’s luggage and watches her saunter. It is raining.
```

### Performance text (classify this)

```text
GARY: Do you like it?

SUSAN: What have you done?

GARY: You don't like it.

SUSAN: I didn't say that.

GARY: Then what did you say?

SUSAN: Why didn't you tell me?

GARY: I told you.

SUSAN: But you didn't tell me tell me. We have an upstairs now?

GARY: Your idea.

SUSAN: Mine? (He takes the umbrella and puts it away.)

GARY: "We live on the top floor" is what you always used to say. "If we ever make enough we should buy the roof and make this our penthouse suite." Remember?

SUSAN: That was five years ago, Gary.

GARY: (He nods.) Uh, huh.

SUSAN: So on a whim you decided to add a floor to our apartment?

GARY: While you were with your parents I had time to think.

SUSAN: Clearly. (He steps up behind her; perhaps runs a finger through her hair.)

GARY: So much has happened. It was cold this winter. For both of us. Everyone expects so much.

SUSAN: Yes.

GARY: We needed a change so I went ahead and did it. (He kisses the back of her neck. Susan tries to be attentive but is elsewhere.) You don't like it, do you?

SUSAN: I didn't say that. I didn't say anything.

GARY: I know.

SUSAN: I like it, Gary. I just walked in. I'm getting used to it. Of course I like it.

GARY: Are you sure?

SUSAN: Of course I'm sure.

GARY: Because you seem undecided.

SUSAN: I'm not undecided. I like it. (He backs away and admires the room. He then looks to her.)

GARY: (Long pause.) Really?

SUSAN: Gary!

GARY: I'm sorry. This is a big deal for me.

SUSAN: I see that. I can only say I like it so many times. It's bigger. Not so cramped. It really is what we always talked about.

GARY: You're not just saying that?

SUSAN: I'm not just saying it.

GARY: So I can show you around?

SUSAN: I wish you would.

GARY: You're not too tired?

SUSAN: (Warning.) Gary.

GARY: All right. First let me get your shoes. Don't want to mess up the new floor. Everything is a little out of place but is going to look great in time for spring. The view will blow your mind. There were complaints from the neighbors but that was expected.

SUSAN: About our view?

GARY: About sound, drilling, hammering, portable power generators, cranes in the street, workmen, permits. The place was a disaster zone. But it was worth it. Watch this.

(He pulls on the chord to the blinds. As they open, the lighting brings more color to the room. Susan covers her mouth and giggles.)

SUSAN: You can see the whole city from here. Look at that!

GARY: This will be the living room. The TV goes here. Dining room and kitchen are taking over in the old bedroom. Everything else is on the second floor. Office, weight room, walk in closet, laundry room. The master bedroom is right on top of us. Plus two bedrooms in the back. Right now one of them is ... Oh! We also get the roof but that won't be ready until summer. There will be a deck and a grill. We can go up and look around when the rain stops. What else?

SUSAN: What about the room?

GARY: What?

SUSAN: You were about to say, "One of the rooms upstairs." What about it?

GARY: Oh. It's nothing. You hungry?

SUSAN: "Nothing"?

GARY: We can still order from Dynasty Bowl. They deliver until two.

SUSAN: I ate on the plane. You're not going to tell me?

GARY: I'm telling you it's not what you think.

SUSAN: Come on, Gary. You asked me to be excited, didn't you?

GARY: Susan -

SUSAN: And now I am excited and want to know even the most insignificant details. You went out on a limb, you made changes to our home, you –

GARY: (Sharply.) The bedroom still has the crib in it. There I said it. Let's get depressed now, OK? (It is some time before he speaks.) I've ... Had a lot of coffee. I was nervous about you seeing the place. I was nervous about seeing you. I still am. I wanted you to like it. I know we can have different tastes. I didn't do all this to try and make you forget.

SUSAN: You just wish I would.

GARY: No, no. That's not what I'm saying.

SUSAN: Then what?

GARY: Once in a while ... Does it hurt to try? (Susan wraps herself in her arms) Sue? (No response) Have you talked to the museum?

SUSAN: I go back in two weeks.

GARY: I'm sure they miss their curator.

SUSAN: They survived. I don't know if I'm ready. All this time off. You've spoiled me.

GARY: You can take more. (She gives him a look.) You don't have to work.

SUSAN: I have to work.

GARY: I mean in the great scheme of our personal economics, we –

SUSAN: I know what you mean. You've told me a thousand times.

GARY: All right -

SUSAN: What did you think? I'd get back in town and still be broken by this thing? Sit here all day and watch you bull and bear over the phone until the bell rings? Cook meals and do macrame?

GARY: Can you stop?

SUSAN: I love my job and I'm going back.

GARY: I'm not arguing.

SUSAN: Things will be different.

GARY: Yes they will.

SUSAN: I'm not looking forward to the questions, that's all. "Where have you been? When can we see the bundle of joy?" Jesus. You've been through it. You know how awful it is to explain. I guess it's different for the man.

GARY: Why do you always say that?

SUSAN: What?

GARY: How do you know it's different? Maybe things are exactly the same. Maybe the idea of us being from different planets is a bunch of garbage we choose to believe in order to keep us from seeing how similar we really are.

SUSAN: That's real deep, sweetheart.

GARY: I'm serious.

SUSAN: I know.

GARY: What do you want from me? (Exhausted.) Maybe we should get back to trying to forget.

SUSAN: You're right. Let's forget. Novel idea. I think it's high time we forget everything we can as soon as possible.

GARY: I wish you wouldn't do that.

SUSAN: And I wish I could forget as much as you.

GARY: I didn't forget, Susan!

SUSAN: That's right! Because there is no forgetting is there, Gary?! So why bother asking me in the first place?! (They are horrified with their raised voices. Neither knows what to say. Susan weeps softly.)

SUSAN: I'm sorry. For a lot of things. I'm sorry that I'm crazy.

GARY: You're not crazy. You've been through something.

SUSAN: We're educated people. Raised well. We have friends. I just ... I can't stop asking myself, you know - Why us?

GARY: T here is no "why." It just is.

SUSAN: Really?

GARY: Yeah.

SUSAN: Interesting. Because when I look back at how our romance began, you always used to say that, "Everything happens for a reason." But when our baby arrives dead to the world, it's, "There is no why"? (Gives a narrow look.) There are discrepancies in regard to which events in our life you deem as part of our destiny and which you do not. The way we met? Destiny. Our stillborn baby? Not so much.

GARY: I can't believe you.

SUSAN: What?

GARY: What? It's been six months. You chose to rush off to your parents for a half a year. You had all this time to sit on it. To "adjust." Wasn't that the word and the plan?

SUSAN: But?

GARY: But I don't know, Sue, you tell me. I look at you and I listen and I swear I feel like nothing has changed. I feel like you are still in the same state of shock you were the day you left the hospital. Why did you go away if it wasn't going to help? Why force us to go through this alone, if-You've been home ten minutes and you're picking fights?

SUSAN: You're the one who said there was an empty crib upstairs.

GARY: I did, but that isn't exactly how I described it, is it?

SUSAN: What difference does it make how you describe it?

GARY: It makes a big difference! I didn't want to talk about it.

SUSAN: Well, the next time you don't want to talk about something maybe you shouldn't bring it up.

GARY: Jesus. I can't believe we're doing this.

SUSAN: Believe it.

GARY: You've barely scratched the surface of this thing, have you? (For a moment they are looking at each other. He breaks off. )

SUSAN: Tell me something.

GARY: What more do you want me to say? Everything gets me in trouble.

SUSAN: I, for one, am tired of hearing myself speak. Aren't you? (Faint smile.) Besides. You're better at the truth.

GARY: There is a ton of mail. Everyone sent letters of congratulations. (He sets a small stack of cards on the table. He watches her sift through before revealing another stack.) Two weeks later, most of the same people sent condolences.

SUSAN: How weird.

GARY: Twilight Zone. (They sit quietly, staring at the two piles.) You think we can we get through this?

SUSAN: It's not that much mail.

GARY: That's not what I mean.

SUSAN: I know.

GARY: We spent six months apart. We prepared ourselves. We talked about not arguing or blaming each other. We said we'd work together to stay happy.

SUSAN: How we doing?

GARY: I'm asking you.

SUSAN: I don't know, Gar. The idea of working to stay happy seems a bit counterproductive. We're either going to be happy or we're not.

GARY: Well? Are we?

SUSAN: I don't know. (Silence.)

GARY: Do you still love me? (She does not answer. Gary nods with uncertainty then goes through the stack. Susan watches for a long beat before she starts to help.)
```

---

## IC-0935: The Trestle at Pope Lick Creek

- Title: The Trestle at Pope Lick Creek
- Author (byline): Naomi Wallace
- Work: Not specified
- Publisher: Faber and Faber, Inc.
- Publication date as stated: 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DALTON, PACE, TOGETHER, PAGE
- Teaser before the introduction: Yes
- Spoken words (computed): 1310
- Already set (do not supply): none

### Source block (context only)

```text
Author: Naomi Wallace
ISBN: 978-0571210756
Publisher: Faber and Faber, Inc.
Date (Month/Year): 2001
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: It’s 1936 . . . High atop a railroad trestle that spans a bone dry creek, two teenagers (Pace and Dalton) plan to race across the bridge against an oncoming locomotive.

ACTOR: At first their scheme adds excitement to their lives in a small factory town during the Great Depression but . . .

ACTRESS: This isn’t Pace’s first time racing the train . . . . she’s done it before and her partner in crime that time (Brett) didn’t make it

ACTOR: How far would you go to feel alive in a time frame and in a town where everything appears to be dying? Would you be willing to try to outrun the Great Depression?

TOGETHER: The Trestle at Pope Lick Creek by Naomi Wallace
```

### Performance text (classify this)

```text
DALTON: You had a head start!

PACE: Nah. You haven’t got any lungs in that puny chest of yours.

DALTON: So, this is it, huh? (They look above them)

PACE: Yep.

DALTON: It’s not that high up.

PACE: Almost a hundred feet. From the creek up.

DALTON: Some creek. There’s no water: it’s dry.

PACE: Don’t care; can’t swim anyway. What time is it?

DALTON: Coming up to seven.

PACE: She usually comes through at seven ten; but she’s never exact. You can’t trust her. That’s what I like.

DALTON: How many times have you done it?

PACE: Once. And that’s once more than you. It’ll be just you and me. Up there. And you can be sure we’ll check our pants when we’re done and see who’s shit.

DALTON: You know. You don’t talk like a girl should.

PACE: (meaning it) Thanks. Listen. She’s pulling eight cars at seventy tons a piece at eighty five. The engine herself is one hundred and fifty three tons. Just cold, lip-smackin’ steel. Imagine a kiss like that.

DALTON: How to you know what the train weighs?

PACE: I looked it up. The year, the weight, the speed.

DALTON: So, you can read.

PACE: Yeah, well. You and her are coming from opposite sides, right. You’ve got to time it exact ‘cause you need to make it across before she hits the trestle. Just face her and go.

DALTON: So what if you know it’s too close? You go for the side, right?

PACE: There’s no side.

DALTON: So what do you do if you can’t make it across before she starts over? PACE; You make it across – that’s all there is to it. DALTON; But what if you can’t?

PACE: Remember Brett Weaver?

DALTON: That’s different. He was drunk.

PACE: Say it again and I’ll punch you. Brett wasn’t drunk. He was just slow.

DALTON: Well. I’ve decided: I’m not crossing.

PACE: I knew it.

DALTON: Only a drunk or an idiot would play that game. Not me.

PACE: You got the heart of a rabbit – a dead rabbit.

DALTON: No way. I never said for certain. I said maybe. And you said it was safe. You didn’t say anything about there being no safety sides. You said it was a piece of cake.

PACE: It is a piece of cake.

DALTON: Forget it.

PACE: You’re breaking the deal. Pay me a buck right now or else.

DALTON: I said no.

PACE: Then why’d you come up here with me? If you back down, everyone will know.

DALTON: So how close were you that time you crossed?

PACE: I’d say I had ‘bout eight seconds leeway. It will be a snap (snaps fingers)

DALTON: What if you trip?

PACE: You’re going to run the trestle. ‘Cause if you don’t, your life will turn out just like you think it will: quick, dirty and cold. Come on. Let’s go up. Let’s make something happen. (transition, change of positions) *************

PACE: Now repeat after me: We don’t want to die.

DALTON: We don’t want to die.

PACE: Tell you what. We’ll have a practice first. Let’s start here. See, this tie’s marked with a red X. Now, you crouch down like this. But don’t check your feet. You’ll trip if you check your feet. If you start when I tell you to, you’ll have enough time to make it across. Ready?

DALTON: Pace?

PACE: Yeah?

DALTON: My legs are shaking.

PACE: This is practice, Dalton. There’s no train.

DALTON: My legs aren’t so sure.

PACE: On the count of trhee. Come on.

TOGETHER: One . . . two . . . three . . .

DALTON: Wait! (He seems to be looking over an edge)

PAGE: Don’t look. You’ll lose your nerve.

DALTON: It’s a long way down.

PAGE: Why don’t we just walk it? Give me your hand. (She takes his hand and begins to walk.).

DALTON: Gosh, we’re high up.

PACE: Keep your eyes on the other side. We’re almost there. And now you trip.

(Pace trips him so he falls)

DALTON: Hey! What the . . . you tripped me . . .

PACE: It might happen. You might trip. Anything’s possible. We got to be ready for it.

DALTON: But I wouldn’t have tripped! You pushed me.

PACE: Let’s say you look over your shoulder to see how I’m doing and you do. And you can hear her cold, slathering, black, hell of a heart barreling towards the trestle. But you’ve twisted your ankle.

DALTON: Yeah. And I can hardly stand. And the train, she’s just about to cross.

PACE: And then there I am. At your side.

DALTON: No. You’ve got to save your own skin.

PACE: Yeah, but I can’t just leave you there.

DALTON: Yes, you can. I’ll be torn apart.

PACE: So I put my arm around your waist and start to drag you down the tracks with me. We’ve only got fifty feet or so.

DALTON: But the train – so you drop me.

PACE: No!

DALTON: You drop me and run. You run for your life.

PACE: No. I don’t leave you. I . . .

DALTON: You make it across. Just in time. Alone.

PACE: I drag you with me.

DALTON: And as you clear the tracks, you feel the wind as she rushes by you. And then – you hear me scream (he screams – at the same time, Pace screams the following).

PACE: I SAVE YOU! (silence for some moments)

DALTON: And then?

PACE: I’m alive. Alive!

DALTON: As for me, well, I’m dead. But still you have to go back and have a look. To see what’s left. Of course there’s almost nothing left.

PACE: Yeah, there was. There was a lot left.

DALTON: No, just some bits of meat and a running show. That’s all.

PACE: He wasn’t wearing running shoes.

DALTON: And now maybe my Mom will be able to scrounge up some new shoes for the funeral. If she can find my feet.

PACE: Just shut up. You are wrong. That’s not what a train does to you. It doesn’t mush you up. This train. She’s a knife. We had a good start. Me and Brett. We could have made it. ‘Course Brett was faster. I expected to be running behind, but Brett was worried – about me. He turned to look over his shoulder at me and he tripped. I thought he’d just jump up and keep going, so I passed him right by. (beat) I thought Brett was right behind me.

DALTON: You left him on the tracks?

PACE: I thought he was running behind me. I could hear him behind me. He didn’t call out. He didn’t say wait up. I didn’t know. Why didn’t he call out? Not even a sound. Brett just sat there where he’d fallen. And then he stood up. He stood there, looking her straight in the face – almost like it was a dare. Like: Go ahead and hit me. You can’t do that to a train. You can’t dare a train to hit you – cause it will.

DALTON: This is stupid.

PACE: Just stood there like she could pass right through him for all he cared.

DALTON: Let’s get out of here, it’s getting late (tries to take her arm)

PACE: (she pulls away) Let go of me.

DALTON: You’re out of your mind. (climbs back down to the creek bed)

PACE: (calls after him) It’s not how you think it is. The train, she doesn’t mush you up. I walked down the tracks after the train passed. She cut Brett in two.

DALTON: Pace.

PACE: You know what I thought? Blocks. Two blocks and maybe if I could fit the pieces back together again, he’d be . . . whole.

DALTON: Will you shut your mouth. Please.

PACE: We’re going to do it for real.

DALTON: Yeah. (to placate her . . . still climbing down)

PACE: Both of us. Side by side.

DALTON: That’s right. (sarcastic)

PACE: A steady run. (hears the train and starts across the trestle)

DALTON: Where are you going? Pace. Hey, Pace.

PACE: I’m going to make something happen. (she turns her back audience- out of scene)

DALTON: (to audience) She stood on the tracks. I stood below the trestle. She looked small up there . . . But until she started to run, I never thought she’d do it without me. (to Pace) No! Stop. You better stop! (to audience) Pace must’ve slowed down and lost her speed when she was calling to me. She started to run back, but she knew she’d never make it. And then she turned. Even from where I was, I could see she was shaking her head. Back and forth, like she was saying: No. No. No (pause) She didn’t want to die. And then she did something funny. Pace couldn’t even swim, and there was no water in the creek, but she was going to dive.

PACE: Watch me, Dalton (turn)

DALTON: And this time. I watched her (pause) Pace lay beside the trestle. I started to shout at her, but she was dead. (pause) Well, Pace, you made something happen. I have to believe that.
```

---

## IC-0936: The Twits

- Title: The Twits
- Author (byline): Roald Dahl adapted by David Wood
- Work: Not specified
- Publisher: Puffin Books
- Publication date as stated: February 2007
- Event as filed: Duo Interpretation
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
ACTOR 1: They're shocking!

ACTOR 2: They're smelly!

ACTOR 1: They're silly!

ACTOR 2: They're stupefyingly stupid!

ACTOR 1: Get ready to meet. . .

ACTOR 2: The one and only. . .

ACTOR 1: Thank goodness!

TOGETHER: The Twits! By Roald Dahl
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

## IC-0937: Two Rooms

- Title: Two Rooms
- Author (byline): Lee Blessing
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Dec 1990
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: LAINIE, ELLEN, WALKER, LANIE, MICHAEL
- Teaser before the introduction: Yes
- Spoken words (computed): 1620
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
ACTOR 2: *According to the James Foley Foundation and recent White House Statements from President Joe Biden regarding American hostages in Gaza, as of January 14, 2024, nearly 70 U.S. nationals are known to be held hostage or wrongfully detained in at least 15 countries. (update as needed)

ACTOR 1: Over 90% of these cases are wrongful detentions that interfere with U.S. foreign policy and national security.

ACTOR 1: Of those hostages, six have been held for over 10 years.

ACTOR 2: Written in 1990, this selection deals with a subject still very much in the minds of contemporary society – the taking of innocent hostages by political terrorists,

ACTOR 1: the agony of the detainees and the helpless fury of those who are left behind – loved ones impatient for something to be done and officials who have a larger political agenda in mind.

TOGETHER: Two Rooms by Lee Blessing
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actor 1 (Female): Lainie, Michael; Actor 2 (Male): Walker, Ellen

NOTE: Actors will play roles of both genders in this cutting.

LAINIE: (Pg 16) (alone on stage, an empty room, she is clearly seeing a different time and place) A hotel in Beirut near where we lived was destroyed in some shelling a couple of months before . . . before he was taken. (beat) (Pg 8-9) I’m talking to myself. All last night, taking the furniture out of this room, I was talking to myself. For the last year, what else have I been doing? Talking to everyone in power – which is, of course, the definition of talking to yourself. The Arabs wouldn’t help me, but at least they’d resect the pain. In Washington, I was the pain. (beat) (Pg 10) The government’s coming today. [Someone] attached to me. My case.

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

MICHAEL: (blindfolded and in handcuffs, alone on stage) War isn’t a tear in the fabric of things, it is the fabric. Americans fight all the time – lots of wars. But always far away. We haven’t had to fight for the soil we stand on in a century. We’ve forgotten that level of sacrifice. These people haven’t. Everyone in this country -- Christian, Palestinian, Israeli – everyone is fighting for the ground itself. They stand here or nowhere. It’s easy for them to kill. Lanie, don’t you see? We’re not different from these people, we’ve just forgotten. *****

ELLEN: (Pg 28-29) (alone on stage) What does it mean to be an American? Well, here it means - for most of us – “to be comfortable." Elsewhere in the world it means to be punished for the crime of having been born here and not there. Enormous numbers of people all over the world hating Americans. Willing to kill even the most innocent of us. To imprison us without trial. For years. Why? They watch our television, you know. See our films, wear our clothes, drive our cars, listen to our music. They learn in our universities. What do they learn? That they have been born in a part of the world which has no power. [And so their] only reality is to reject and destroy what they can of the Western world. *****

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

MICHAEL: (Pg 35) (alone on stage) LAINIE!! LAINIE!! (beat, he removes his blindfold and looks around fearfully, then relaxes slightly) They moved me again. They have a box they put me in – the shape of a coffin and it’s soundproof. The first time they put the box in the back of a van with a bad exhaust system. I was unconscious when they took me out. (beat) Sometimes I don’t know. I don’t absolutely know whether I’m alive or dead. *****

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

MICHAEL: (alone on stage) Sometimes I wake up and realize that months have gone by. (beat) Time is change. That’s all it is. When there’s no change. When there’s no change . . . Yesterday one of my guards told me I’d been here three years. (beat) I didn’t know what he meant. (beat) (Pg 44-45) Some clothes were thrown on me and I was hustled into the back seat of a car by three men. They drove me to a quiet neighborhood and shoved me into a building. I was taken down, still blindfolded, to a small, cramped room that smelled like . . . clay, and I was . . . (Actor 2 assumes the role of terrorist and pantomimes the execution gunshot from behind Michael) (long beat) *****

ELLEN: (Pg 45-46) (alone on stage) When I worked in the Defense Department, I told them their men were heroes. I said, “He died of bad luck.” (Lainie enters, unseen by Ellen) No bad planning at the top, not tactical mistakes of his commanders. Bad luck. Lainie gets the truth. We miscalculated. We valued Michael’s life below a chance to make an international point. We increased the danger for all the hostages. We chose to (Pg 41-42) intercept a terrorist. Not a Shi’ite, not even Lebanese. But an Arab, and . . . we killed him. It was the judgment of the Department that Michael and the others would not be overly . . . endangered. (Pg 46) We miscalculated.

LAINIE: Thank you. (turns with surprise)

ELLEN: Lainie, I . . . I wasn’t ---

LAINIE: (angry) Going to say it like that? I’m glad you did. Is that all your business?

ELLEN: Allow me to take this opportunity to convey the deep sympathy of the Secretary of State and the President.

LAINIE: Go to hell. (long beat) (Pg 47) (with heavy sarcasm turning to intense sadness) No, I think you and the government did your best. I think everyone did his best. Michael, Walker, you, the Shi’ites – even the ones that killed Michael. Probably everyone has done his best. That’s what frightens me. That’s why I don’t know if I’ll ever be able to walk out of this room anymore. Into what? A world filled with people doing their best.

ELLEN: I wish I could take your pain away.

LAINIE: I wish you could remember it.
```

---

## IC-0938: The Universal Language

- Title: The Universal Language
- Author (byline): David Ives
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DAWN, DON, DON & DAWN
- Teaser before the introduction: Yes
- Spoken words (computed): 1878
- Already set (do not supply): none

### Source block (context only)

```text
(none)
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

## IC-0939: Urinetown – The Musical

- Title: Urinetown – The Musical
- Author (byline): Mark Hollmann and Greg Kotis
- Work: Not specified
- Publisher: Farrar, Straus and Giroux
- Publication date as stated: Feb 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: LOCKSTOCK, LITTLE SALLY, FIPP, CLADWELL, HOPE, PENNY, OLD MAN STRONG, LITTLE BECKY TWO-SHOES, MCQUEEN, BOBBY, THE POOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1788
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
ACTRESS: Welcome to Urinetown -- a place where citizens must pay to pee and anyone daring to question authority mysteriously “disappears.”

ACTOR: Sound absurd? Maybe not. In today’s America, where basic human needs like healthcare, housing, and even clean water often come with a price tag, Urinetown feels less like satire and more like a mirror.

ACTRESS: Beneath its ridiculous premise lies a biting truth: when greed runs the system and justice can be bought, dystopia starts to feel a lot like business as usual.

TOGETHER: Urinetown – The Musical by Mark Hollmann and Greg Kotis
```

### Performance text (classify this)

```text
Suggested Roles: Actor: Lockstock, Cladwell, Old Man Strong, Bobby

Actress: Little Sally, Fipp, Hope, Penny, Little Becky Two-Shoes, McQueen, The Poor

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Early morning. The poorest, filthiest urinal in town. Above the entrance to the urinal hangs a sign that reads Public Amenity #9. Officer Lockstock enters and addresses the audience directly.

LOCKSTOCK: (Pg 9-10) Well, hello there. And welcome to a town like any town. (motions to sign) As the sign says, it’s a “public amenity,” meaning public toilet. People have been waiting for hours to get in; it’s the only amenity they can afford to get into.

LITTLE SALLY: Say, Officer Lockstock, is this where you tell the audience about the water shortage? The hard times? The drought? A shortage so awful that private toilets eventually became unthinkable?

LOCKSTOCK: Little Sally. You're too young to understand, but nothing can kill a show like too much exposition.

LITTLE SALLY: How about a bad title? That could kill a show pretty good.

LOCKSTOCK: (Pg 11) (ignoring Little Sally) These public bathrooms are controlled by a private company, the Urine Good Company. They keep admission high, so if you're down on your luck, you have to come to a place like this -- one of the poorest, filthiest urinals in town.

LITTLE SALLY: And you can't just go in the bushes either -- there's laws against it. (counting coins in her hand)

LOCKSTOCK: That's right. Harsh laws, too. That's why Little Sally here's counting her pennies.

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

CLADWELL: (Pg 46) People are animals! (Pg 45) What would you do if the very foundation of your life's work were threatened by the rabble-rousing son of a convicted criminal? We nip this unpleasantness in the bud! (exits in a huff; others follow)

*****Scene***** Public Amenity #9

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

## IC-0940: The Valentine Fairy

- Title: The Valentine Fairy
- Author (byline): Ernest Thompson
- Work: The Best American Short Plays 1992-1993
- Publisher: Applause Books
- Publication date as stated: July 2000
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: INGRID, RUDYARD
- Teaser before the introduction: No
- Spoken words (computed): 2687
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ernest Thompson
Book: The Best American Short Plays 1992-1993
ISBN: 978-1557831668
Publisher: Applause Books
Date (Month/Year): July 2000
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Meet Ingrid: It’s Valentine's Day and she’s given up on all men and life itself.

ACTRESS: And if my day wasn’t bad enough already, I get home only to find this curious man in red slippers, a leotard and a lacy skirt. What a day!

ACTOR: And after some initial pleasantries, I, The Valentine Fairy, take Ingrid on a journey analyzing her past loves.

ACTOR: Yeah, right like my love life is important! Geesh!

TOGETHER: The Valentine Fairy by Ernest Thompson

SCENE: In a New York apartment, defined mostly by its over-eager effort to conform to too many fashions, sits RUDYARD, a curious man of 40 dressed in a blue leotard and red slippers and white gloves and lacy skirt, and a rumpled red hat and several days' growth of beard. He thumbs through a worn notebook, checks a slide projector at his feet, checks his appearance. INGRID bursts in, raging in a New York accent. 30, hard, lovely, furious, weepy. She throws a box of chocolates on the table, yanks off her coat and boots.

*NOTE: During the slide sequence, Ruyard and/or Ingrid will have to verbally identify the picture on the slide in order to the audience to follow the scene.
```

### Performance text (classify this)

```text
INGRID: Men. Men! Who thought them up anyway? The experiment's over, it didn't work! [She opens a window, climbs up, looking as if she's going to jump.] Misogynist! Misanthrope! Mis ... representer. Mister Potato Head! [She turns away, picks up the box.] Candy. 10 years of Jane Be Like Me Be Like Me, I'm Anorexic Fonda ... [She throws it down, kicks it.] ... half my life on the Somalian Rice Diet and he gives me candy! [She sits by it.] I should eat it, I should eat the candy and weigh a thousand pounds. [Shouting.] Is that what you would like, a female manatee for a girlfriend? [She pokes in the box.] It's a good way to pick out the peanut ones anyway. [She tries one.] I suppose that's supposed to taste good. Oh, God, that tastes good. [She spits it out.] Ecch, puke, Alien! What am I doing? [Squeezing her stomach.] I'm already Roseanne Arnold! I've got Barbara Bush Disease. [She starts to cry.]

RUDYARD: [Singing softly.] You are so beautiful...to me.

INGRID: [She screams.] Acch! Who are you? Don't hurt me!

RUDYARD: I'm the Valentine Fairy.

INGRID: Go away! I'm warning you.... who?

RUDYARD: The Valentine Fairy. [He smiles.]

INGRID: Oh? I'm Princess Di. Haven't seen old Big Ears, have you?

RUDYARD: You're Ingrid Paloma, you're 31 years old and you work for Fat Cat Advertising. And you're lonely and you're blue.

INGRID: You don't know that. You don't know anything about me. Get out of here! Go! I have a gun! I'll get it, I swear to God, and I'll shoot your face off.

RUDYARD: Oh, boy, I wish you wouldn't. It's so not me. You could try one of the Veterans' Day fairies, they love guns.

INGRID: [A new tack.] Look. You just go and I won't tell anybody you were here, I won't report you or anything.

RUDYARD: Well, that's very pleasant of you, but I have a job to do.

INGRID: What job?

RUDYARD: To bring a little love into your heart. To make you believe once again in the power and the glory and the beauty of Ingrid.

INGRID: [Scowling at him.] My mother put you up to this. She's not normal.

RUDYARD: [He smiles, setting up the projector.] I thought about being a Mother's Day fairy, but I wasn't cut out for it. I like to be able to win a few rounds now and then.

INGRID: Excuse me. Do you mind? Was I evicted or is this still my apartment?

What is that?

RUDYARD: This is a slide projector.

INGRID: You're going to show me slides?

RUDYARD: Yes, sorry. All the young guys have gone computer. VCRs, laser discs, all very impressive. But it's not me. Could you get the lights?

INGRID: You're not listening to me. Hello? You know why? Because even though-and I'm not asking questions-you're wearing a tutu, you're still one more major big dumb man.

RUDYARD: Well, aren't you kind? What I really am is in something of a hurry, I don't mean to be rude. This is my night, you know. I don't think you'd sit around arguing with Santa Claus.

INGRID: [Dubious, facetious, but softening.] What's wrong with Cupid? I thought Valentine's was like his ... bailiwick.

RUDYARD: Cupid is a naughty little boy who likes to fly around shooting arrows at people. He's not a professional. We can't go tossing our affections to the first taker with a cute butt and a je ne sais quoi. You could at least show me the courtesy of listening to my presentation. [Calming.] I'm sorry. This is a very stressful night, Valentine's is not what it used to be. [INGRID looks at him warily. She turns off the light and sits.] Thank you. [He puts up the first slide, a heart with the word LOVE.] Love. A Journey Into Your Heart.

INGRID: [She raises her hand, skeptical.] Um. Is this going to be a long journey? Because I do have places to go.

RUDYARD: Let's talk about the three Rs! Rage, Resentment, self-Recrimination. Is that what you want to do, you want to spend my valuable time and the rest of your life in line at a pity party?

INGRID: Huh? No. I don't believe I do, actually.

RUDYARD: All right then. Good. [He puts up a slide-a bird feeding its young.] Let's go back to the beginning, when we were young, let's focus for a moment on what our dear old mother gave us.

INGRID: Worms.

RUDYARD: [He laughs.] Well, that's very funny, Ingrid. [He makes a note.] Humor still functioning. Now. [He changes slides-a middle-aged man.] Dad. Daddy. Papa. Pops. Pete. Petey.

INGRID: Pervert. Where did you get that? You know my old man? What, did you meet him in Bellevue?

RUDYARD: We had a problem with father, did we?

INGRID: [Quietly.] He did not respect me.

RUDYARD: I'm sorry. [He pauses, affected. Puts up a new slide--a man of 25.] And what about this person?

INGRID: That's my husband! Where'd you get that? I'm dead, right? I got hit by a cross town bus when I jumped out of the cab. And you're really an angel. And I'm an atheist.

RUDYARD: Was it moving? The cab.

INGRID: The cab was parked at the red light in front of Papaya King, where my most recent boyfriend-I'm surprised you don't have his picture, too, you're not very up to date ... My most recent boyfriend decided to inform me it was time to reevaluate our relationship. I think that's a very romantic spot, don't you, the Papaya King, to have your heart broken?

RUDYARD: [Making a note.] And now ... he doesn't love you ... any more.

INGRID: He doesn't love me any less. Ha ha. He told me he has so much love it was only fair to share the surplus with girls who don't have any. I think sometimes that's the only language men know, the mixed message. A kiss goodbye and a box of candy. "I just need a little outside *company*, but I'll always love you, fatso."

RUDYARD: You're angry, aren't you? [He makes a note.]

INGRID: No. Is that how it seems?

RUDYARD: Well, you're probably better off without him. Forge your own trail through the wilderness, who needs the abuse?

INGRID: Am I going to get a bill at the end of the 50 minutes? Because you are not the first know-it-all in a skirt to point out the obvious. You're not even the first one in a skirt and beard. I'm sorry. If I hurt your feelings. I didn't mean any harm.

RUDYARD: Doesn't matter. I'm used to it. Being a fairy is not something that immediately commands respect. [He smiles bravely.] But this is not about me and my poor trod upon feelings. This is about Ingrid. What are we going to do about Ingrid?

INGRID: [Affected.] You're very kind, aren't you? That's nice. That's an unusual commodity for a man. Or for anybody for that matter. You're an unusual person. Or whatever you are. Are you really a fairy?

RUDYARD: Yes.

INGRID: What ... what are you doing here?

RUDYARD: Wherever there's a need, that's where we go. If it's an emergency, we stay till the danger passes. We're just like the Marines, except we don't beat up gay people. [He salutes.]

INGRID: And what, I'm an emergency, is that the idea?

RUDYARD: Oh, that's not up to me to say. That's your decision. Anything else we want to say about the candyman or shall we put him where he belongs? [She shakes her head, troubled. He pulls out the slide, drops it in a waste basket. Goes back through, discarding each slide in turn. Puts up the penultimate, a man in denim.] Good enough. What about this character?

Were we going through our lumber jack period?

INGRID: Um. That was Austin. He had a charge account at Ralph Lauren. Bought a lot of outdoor things he never used. Why would someone buy a jet ski in Manhattan? He couldn't handle intimacy.

RUDYARD: [Next slide, a man in black.] This one? Have Gun Will Travel.

INGRID: Zack. Major Tom Waits fan. We listened to an inordinate amount of Tom Waits. He couldn't handle intimacy either.

RUDYARD: [Next, a father type.] Did we put ourselves up for adoption?

INGRID: Mr. Jannislaw, my Human Development teacher at night school. Not a course he was qualified to teach. Also couldn't handle intimacy.

RUDYARD: [Next, a very young man, cute.] Ah ha. Ingrid's revenge.

INGRID: He was 19. Delivers groceries for Gristedes. Hadn't heard of intimacy.

RUDYARD: [Next, a handsome black guy.] Uh oh. This is a picture we should send to Dad.

INGRID: That was Willy. He was OK. He just hated white girls. [Next slide, a gentle-faced man.] He hated all girls, as it turned out. He was standing on the brink of homosexuality and I pushed him over.

RUDYARD: [Next, a beefy jock.] Not this one, too? The gay community's going to nominate you for sainthood.

INGRID: No. That was Rick. He loves girls. Loves to beat the *crap* out of them.

RUDYARD: [Next, a bookworm type.] This person never beat the *crap* out of anybody. I could take this person on.

INGRID: Alden. Very smart boy. Did the Times crossword puzzle on the typewriter. He broke the news to me that I'm stupid. [Next slide, male, 40 and glum.] My boss. No comment. [Next slide, a young guy.) Ronnie, couldn't handle intimacy. [Another slide, another guy.) Couldn't handle intimacy. [Another.) Couldn't handle intimacy. [Another.) Couldn't handle me. [Another.)

Couldn't handle my mother. Him I liked okay. [Another.] He died. Not of AIDS. He died of jumping in front of the IRT Uptown express, I try not to personalize. [Another, a teenager.] That's Chip. Good old Chipper. We loved each other, until I got pregnant. [Another teenager.] Tommy. We couldn't figure out how to get pregnant. [Another teenager.] Morgan. First base. [Another, very young.] Ben. There was no first base. [A ten year old boy.] Oh. Christopher. Sweet little Christopher. First kiss. [Donny Osmond.] Donny. The only boy who never broke my heart. [RUDYARD turns on the lights. INGRID looks, dazed, upset.] That's it? That's my whole resume? That makes the guys in the post office look interesting. What is the point of this? I *mess* up every single relationship I've been in and I should have my license revoked? Is that going to put you in the Fairy Hall of Fame? You're a genius fairy, big deal.

RUDYARD: It's not part of my job description to draw conclusions, sorry. At least you've got something to work with here. Some of my clients think life is a Judith Krantz novel. I would merely point out, once upon a time you loved every one of those boys and men-and woman-and had faith and a very nice ride at 90 miles an hour, till you smashed your face into the hard brick wall of disappointment and almost bled to death. It's time to get back behind the wheel, Ingrid, and go find your innocence again before it's too late ... You know what's going to happen to you, you're going to turn into *an angry* old broad, it's not an attractive image.

INGRID: Well let's not be cheery, I hate that. So what if I'm *angry*? I like being *angry*?, it's something to feel anyway. I hate men, I hate women, I hate myself, I'm starting to look like Elizabeth Taylor in her John Warner phase. I've had a very hard time! OK?

RUDYARD: I'm sorry.

INGRID: You don't know what you're talking about, you're just a fairy.

RUDYARD: Right. [He waits patiently.] I have another slide for you, if you're interested.

INGRID: Oh, we forgot someone? Who is it, Quasimodo? I thought it was character building. [He puts up a slide of a little girl.] Who's that? That's me. That's me. You could at least've found a picture with teeth. That's embarrassing. [But she stares at the picture.]

RUDYARD: You used to love her. Didn't you?

INGRID: [For a moment it looks as if she'll give in to it, but then turns.] Why are you showing me this?

RUDYARD: Because. Because you weren't mad yet. You were filling out all those little wispy Valentines children inexplicably give one another. "I love you, Ingrid." "Your friend forever, Ingrid." Because every time your heart breaks it's harder to put it back together. Because half my clients have died from love, or are dead inside. Because you still have a fighting chance; look at the little girl.

INGRID: Could you turn that off, please? You were on a roll there for a minute, but this is not inspired, I'm telling you. [He keeps the slide up, waiting.] Get away, go on! Leave a person in peace to jump out the window, maybe that's what I'm gonna do. No, first I'm gonna eat the chocolates, then I'm gonna jump out the window. Would you please leave now? I don't need help, thank you just the same. And if I did, I wouldn't be seeking it out from some bad joke in red toe shoes. OK? Go away! This is not a Frank Capra movie. This is the Ingrid Paloma Story and it ain't gonna have a happy ending, I can tell you that right now. Go! [She pushes him.] There's the door. Or are you gonna fly like Tinkerbell? Where's the magic, incidentally? You're a phony, did you know that? [RUDYARD looks as her grimly. He nods, packs up his slide projector, the image of the little girl staying on the wall. He seems darker now, stronger than before.]

RUDYARD: You're right. I'm too old for this. Should've been a Thanksgiving fairy when I had the chance. They've got it made. A few family squabbles and all you can eat. And a little clinical depression, sounds good to me. But I'll tell you this, Ingrid, you're a big fat spoiled brat. Sorry, I didn't mean fat. [Checking his notebook.] I've got a 78 year old woman in the Bronx, and a priest downtown-they're the worst, want love, can't have love, get love anyway, get in trouble-but at least they still have hope. There are plenty of people out there who could use a good fairy. [He glances at the audience.] But you-you be careful. You're only as stupid and worthless as you want to believe. Who cares if all the *men* in the world love you or not, if you don't love yourself, you big baby? Don't you read the Valentines? [He's ready to go.] "If you can dream-and not make dreams your master ... " Ah, forget it. That's Kipling, by the way. [He starts out.] Usually I go in a poof of smoke, but, you know-budget cuts.

INGRID: [Picking up the waste basket.] What about the slides?

RUDYARD: They're your problem, you sort 'em out.

INGRID: What about her? How'd you do that anyway?

RUDYARD: Well, there's got to be a little magic, even in a recession. [He salutes, gives the audience a knowing look, and walks out. INGRID watches him go, anxious.]

INGRID: Well, wait a minute. What if I decide I'm an emergency? [No response, he's gone.] Emergency, emergency! [She starts to cry, drops the waste basket behind a chair, sits.] Everybody hates me, nobody loves me, I'm goin' out and eat chocolates. [She opens the box.] Big fat juicy ones, long yucky buttercreams ... [She cries. Traipses to the window like a child. She climbs up. It looks as if she's going to jump. But she tosses a piece of candy, calling.] Candy for the homeless. Valentines for the loveless. Free Valentines. From Ingrid, with love. [She dumps out the box. Starts to throw it. Steps in, crumpling it. Drags out the waste basket, sits on the floor, drying her eyes. She turns the basket over. Instead of slides, hundreds of Valentines tumble out, covering her lap. She stares in wonder. Picks one up.] "To Ingrid. When you grow up, I'm gonna marry you. Love, Christopher." Well, I'll let you know, Christopher, if that ever transpires. [She tucks the card in her blouse, pulls a pillow off the couch and an afghan and curls up on the bed of Valentines. Too tired to get up, she yanks the lamp cord out of the wall. The room is dark except for the slide. INGRID gazes up at it.] Good night, little girl. [She closes her eyes. Pause.]
```

---

## IC-0941: Variations on the Death of Trotsky

- Title: Variations on the Death of Trotsky
- Author (byline): David Ives
- Work: All in the Timing: Fourteen Plays
- Publisher: Vintage Books
- Publication date as stated: Nov 1994
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TROTSKY, MRS TROTSKY, RAMON
- Teaser before the introduction: Yes
- Spoken words (computed): 1002
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
ACTOR: Lee Harvey Oswald, Nathuram Godse and Sirhan Sirhan comprise the most famous assassins of political figures in the 20th century.

ACTRESS: Oswald assassinated President Kennedy, Godse murdered Mahatma Gandi and Sirhan Sirhan killed Robert Kennedy, Right?

ACTOR: Right. Their murderous acts not only changed history but also guaranteed them everlasting infamy and a kind of immortality.

ACTRESS: However, some prominent assassins have become forgotten in the mists of time -- one of them was born 100 years ago in Barcelona, Spain.

ACTOR: Jaime Ramón Mercader del Río, a Spanish communist and agent for Russia’s notorious intelligence agency, murdered Russian revolutionary Leon Trotsky in Mexico City in 1940 under orders from Joseph Stalin.

ACTRESS: Well that’s not funny – I thought we were going to do a humorous duo! I don’t DO drama! I told you I don’t DO drama!

ACTOR: No worries. This is . . . . .

TOGETHER: David Ives’ Variations on the Death of Trotsky
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Lights up on TROTSKY sitting at his desk, writing furiously. The handle of a mountain-climber’s axe is sticking out of the back of his head

NOTE: Actress also plays the role of RAMON VARIATION ONE

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

## IC-0942: A Very Clean Place

- Title: A Very Clean Place
- Author (byline): Gale Mena and John Peat
- Work: Fast Horse Plays, Round 3, pg 13-24
- Publisher: Fast Horse Drama
- Publication date as stated: Aug 2012
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SAMMY, BENJI
- Teaser before the introduction: Yes
- Spoken words (computed): 1443
- Already set (do not supply): none

### Source block (context only)

```text
Author: Gale Mena and John Peat
Book: Fast Horse Plays, Round 3, pg 13-24
ISBN: 978-0615694894
Publisher: Fast Horse Drama
Date (Month/Year): Aug 2012
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Sammy is just 10 years old, the baby of the family.

ACTOR: But developmentally she and her older brother Benji are not too far apart.

ACTRESS: You see, Benji was born with a genetic disorder.

ACTOR: This is their story.

TOGETHER: A Very Clean Place by Gale Mena and John Peat
```

### Performance text (classify this)

```text
SAMMY: Rock . . . (Benji is moaning slightly, turned from the audience, gent/y rocking back and forth) C'mon Benji, this is the fourth time today you've said you wanted to play . . . C'mon just say . . .

BENJI: Sciss . . . Sciss . . .

SAMMY: No Benji, we've been over this two gazillion times. If the name of the game is Rock, paper, scissors, then what comes next after rock?

BENJI: (turns towards the audience, making his disability apparent) Rock? (Sammy sighs) You hate playing with me, and so I hate you. A lot.

SAMMY: Benji, stop it. I can't do this every day with you. I have to go to school . . .

BENJI: You're leaving me again, you always have to go away, you like everyone else better than me, maybe I should just die because you hate me . . . Just go away. (turns from audience, crying)

SAMMY: No, c'mon don't say that. You know how that makes me feel. (Benji wails) You know what, forget about it. I’m going downstairs, I have to go to school.

BENJI: Sammy?

SAMMY: What?

BENJI: Can we play again? (Benji is turned from the audience, humming and playing a make-believe game)

SAMMY: (to audience) What you have to understand is that Benji is almost seventeen. There's a seven-year difference between us.

BENJI: Sammy's stupid!

SAMMY: Occasionally.

BENJI: And Sam is a boy's name!

SAMMY: And lots of people like to name their dogs Benji, so what's your point?

BENJI: Woof! Woof! Woof!

SAMMY: Anyway, as I was saying Benji was first born. (turns to see if Benji is indeed engrossed in his imagination so she can speak " privately") Mom and Dad were alerted by their obstetrician that Benji was developing with an extra chromosome, which I'm not sure if you're aware but is a clinical sign of possible. . . (lowers voice to a barely audible whisper) Down syndrome. They were given two options, and they chose the one they were supposed to: Benjamin Sylus Szarsky.

BENJI: (turning around, smiling) That's me !! HEY, SAMMY!!!!!!!!!! Is it my turn?

SAMMY: Go ahead.

BENJI: When Sammy was baby, she was stinky and I hated her cuz she was small. But now she is bigger and less stinky. And I don't hate her all the time too much. And I like to go to the very clean place with her. Do you guys like the very clean place?

SAMMY: Benji, they don't know what the very clean place is.

BENJI: Oh, well it is this place, that is very beautiful and very clean. Sammy and I go there a lot.

SAMMY: We live over beyond the ridge, and the creek is just down the hill outside our backyard. I can't remember a time when Benji and I didn't go down there . . .

we catch tadpoles . . .

BENJI: I am a tadpoke! Look! Does his best tad-pole imitation.

SAMMY: Tadpole, Benji. TAD-POLE.

BENJI: I know, dumb-dumb. Tad-poke. Like this.

SAMMY: . . . And race paper boats and stuff like that. It's our favorite place to go.

BENJI: And it's very clean.

SAMMY: He's always said that. So, even though Benji has always been in the classes for special kids at school, it's never been easy for him. (Scene break – Sammy comes to the quiet room at school. Benji it in a corner of the room, hitting himself in the face and head – she stops him.

SAMMY: What happened this time, Benji?

BENJI: Jimmy . . . Jimmy told me all about the big machine that God has.

SAMMY: What? God doesn't have any big machine. Jimmy is just trying to . . .

BENJI: Yes he does. Yes he does! God has a very big machine and all of the people in all of the whole world pop out of [it]. And most of the time the big machine pops out good people who have good bodies and big healthy brains, but then . . . (fades) But then sometimes the machine gets stupid and it pops out stupid people with dumb heads. Like me. I got very mad at Jimmy! I told him that everybody is equal. That everybody is good and . . .

SAMMY: That everybody has a place. That's absolutely right, Benji. Everybody is perfect and . . .

BENJI: Just how they are supposed to be.

SAMMY: (to the audience) Sometimes it's like the tide, ya know? Ebbing in and out. How he can get so angry and out of control, and then, suddenly, he's just so spot-on. Like the wisest person in the world.

BENJI: (singing) Old MacDonald had a farm, eiei, o, and on that farm, he had some . . . poop. . . eieio

SAMMY: (to the audience) Well, you know what I mean. Can I tell you guys a secret. . . ? I promised Benji I wouldn't, but . . . Benji is who he is, all the tough stuff, and all the wonderful stuff, it's like [he] was born with a "handle with care" label stamped on him, but recently he's been nervous and saying he feels sick all the time. There was a day at school . . . (Benji is suddenly under the table, crying. Sammy bends down under the table) Benji we talked about this, what happened?

BENJI: (Out of control, screaming) Nobody wants to play with me here I hate them, and I hate you for not being here with me! And I feel very sick, very, very sick in my tummy and in my big stupid head.

SAMMY: Benji, you gotta calm, down.

BENJI: Go away, You don't want to be with me.

SAMMY: I can't do this.

BENJI: (pauses to consider this) I feel sick Sammy. Really sick.

SAMMY: Is this so you can go home again? You've said you've been feeling sick a lot lately- B, if you don't wanna go to school anymore, then we should talk about it with Mom and Dad . . .

BENJI: Stop! The spinnies are back! (covers his ears)

SAMMY: (standing up, addressing the teacher) I need you to call 911. And then I need you to call my parents. Right now.

BENJI: (to audience) I have a secret that you cannot tell my sister. I am so scared.

(Scene break – Benji’s family is at the hospital)

SAMMY: No one is ever happy at a hospital. It's where you go the get the bad news. The news that no one wants to hear, but when you do hear it, it's like a worm that's getting into your brain, you know, when the Doctor is saying, “It's very difficult for me to tell you folks this, but Benji has developed Leukemia.”

BENJI: What is Leukemia? Is it a special treat?

SAMMY: No, Benj. Leukemia is a word that means, um, it means very sick.

BENJI: Oh, I have been sick before. I will just take a lot of pills and it will go away.

SAMMY: It's not that kind of sickness, Benji. (Scene break)

SAMMY: (to audience) And so, the weeks passed, and . . . the options for Benji got to be fewer. One afternoon, just before he had to go back to the hospital, for the last time, we couldn't find him. But . . . I knew where he had gone. He had gone to the very clean place. (Scene break)

BENJI: (Skipping rocks) Does the creek go all the way to the ocean, Sammy?

SAMMY: (She joins him in skipping rocks) I'm not sure, big brother.

BENJI: That would be so fun to swim all the way to the ocean.

SAMMY: When did you get so good at skipping rocks?

BENJI: I was always better than you. That is because I am a boy and you are a girl and it is a sport. . . I don't want to have the bad sick.

SAMMY: I don't want you to have it either.

BENJI: I didn't understand dead until Aunt Bertha and then she was dead. She looked really creepy in that room. Like a big, fat doll. Aunt Bertha was fat.

SAMMY: Benji! (reconsiders) . . . Yeah, she was.

BENJI: I do not want to look like an ugly or creepy doll when I get dead.

SAMMY: Benji . . .

BENJI: Well, I do not. I already have a bad brain. I do not want to look ugly or creepy too . . . I am not that scared of dead. What I am scared of is not seeing you . . . Is it really dark when you get dead, Sammy?

SAMMY: I don't think so, Benji. I think it's going to be full of light. It will be the most beautiful, clean place you've ever been. With a creek and tadpoles, and a warm ocean.

BENJI: I need to tell you a very big secret, Sammy. Every night since I can remember, which is a very long time, I have prayed to God before I went to sleep that he would go back to the God Machine and make you a brother that wasn't stupid and dumb and got angry. You deserve a good brother. I am very sorry.

SAMMY: Benji, I have a secret too.

BENJI: You do? What is it?

SAMMY: I have a perfect brother. (Benji looks confused) His name is Benji. (he smiles and points to himself)

BENJI: I love you, Sammy. I don't want to go away.

SAMMY: We will always be together, Benji. Always and always. I promise. Maybe not our bodies, but, right here . . . (she places their hands on each other's hearts -- Long pause)

BENJI: I hope you get a boyfriend one day Sammy, before you get really old. And I hope he loves you as much as Dad loves Mom. And then, I hope you have kids that are perfect with big brains, like yours.

SAMMY: And when I do, I'm going to tell them stories about my hero. His name was Benji and he was . . . is, my big brother, and he was the most beautiful and perfect person I ever knew. I'm going to miss you so much, Benji.

BENJI: Please come here every day. This very clean place. Please make paper boats.

(Sammy nods) and catch tad pokes (Sammy nods again, holding back tears) And please remember me when I get dead.

SAMMY: I will. BENJI: Rock . . . SAMMY: Paper . . . BENJI: Scissors . . .
```

---

## IC-0943: A Walk to Remember

- Title: A Walk to Remember
- Author (byline): Nicholas Sparks
- Work: Not specified
- Publisher: Grand Central Publishing
- Publication date as stated: Sept 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: LANDON, JAMIE
- Teaser before the introduction: Yes
- Spoken words (computed): 2218
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nicholas Sparks
ISBN: 978-0446693806
Publisher: Grand Central Publishing
Date (Month/Year): Sept 2004
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS SPEAKS INTRO: In this heart-wrenching story, Landon Carter is shown the depths of the human heart and the joy and pain of living from a most unexpected person . . . Jamie Sullivan.

A Walk to Remember by Nicholas Sparks
```

### Performance text (classify this)

```text
LANDON: (to audience) Now, Jamie was a nice girl. She really was, [but she] wasn’t exactly what I considered attractive. Despite the fact that she was thin, with honey blond hair and soft blue eyes, most of the time she looked sort of . . . . plain. [And] Jamie carried her Bible wherever she went. She would [even] read the Bible during lunch break at school. Despite these strikes, though, the one thing that really drove me crazy about her was the fact that she was always so [dang] cheerful.

LANDON: (to audience) The homecoming dance was coming up, and I still didn’t have a date. So there I was, flipping through the pages in the [yearbook] when I saw Jamie Sullivan’s picture. I closed the yearbook. Jamie Sullivan? [The reverend's] daughter? Absolutely not. I spent the rest of the evening debating the pros and cons, but in the end the choice was obvious. I had to ask Jamie to the dance. I made my way down the streets of Beaufort, reached her front door, took a second to catch my breath, and finally knocked.

(Landon enters scene)

JAMIE: Landon, this is a surprise! Well, I’d invite you in, but my father isn’t home, and he doesn’t allow boys in the house while he’s not around.

LANDON: Oh, that’s okay. We can talk out here, I guess.

JAMIE: So, what did you want to talk to me about?

LANDON: Sure is a beautiful day. Why I’ll bet there’s not a single cloud in the whole sky.

JAMIE: Landon, you didn’t come here to talk about the weather, did you?

LANDON: Not really.

JAMIE: Then why are you here?

LANDON: Well . . . . I wanted to know if you would like to go to the homecoming dance with me.

JAMIE: I’d love to . . . on one condition. You have to promise that you won’t fall in love with me.

LANDON: (to audience) I knew she was kidding by the way she laughed, [so] I smiled and gave her my word. In the two weeks following the homecoming dance, my life pretty much returned to normal. Sunday I was in my room, working on my application to UNC. I was writing one of my essays when the phone rang.

JAMIE: Landon?

LANDON: Oh, hey. What’s going on? Why are you calling me?

JAMIE: I wanted to ask you a favor. I’d like to ask you if you wouldn’t mind playing Tom Thornton in the school play.

LANDON: Can’t someone else do it instead? (to audience) Being seen with her once was bad enough . . . but being seen with her every day? What would my friends say? But I could tell this was really important to her.

JAMIE: I’ve been praying about it, Landon. I’d really like this play to be special this year, not for me, but because of my father. I know how much it will mean to him to see me be the angel, because this play reminds him of my mother . . . Will you think about it?

LANDON: The next day I talked to Miss Garber, went through the audition and got the part. Rehearsals started the next week. I began to stumble through my lines for the next few days, not really even attempting to learn them. I’d crack a joke or two, which everyone laughed at, except for Jamie and Miss Garber. [But] Jamie wasn’t going to let me off that easy.

JAMIE: Do you ever think about the future, Landon? What you want to do with your life?

LANDON: I don’t know yet. I haven’t figured that part out. I’m going to UNC next fall, at least I hope so. I have to get accepted first. How about you? What do you want to do in the future?

JAMIE: I want to get married. And when I do, I want my father to walk me down the aisle and I want everyone I know to be there. I want the church bursting with people. . . . Yes. That’s all I want.

LANDON: Well, you’ll get married someday. You’ll meet some guy and the two of you will hit it off, and he’ll ask you to marry him. And I’m sure that your father will be happy to walk you down the aisle.

JAMIE: (wistfully) I hope so.

LANDON: (to audience) The next night, as I was walking her home we talked about her Bible. (to Jamie) Why do you always carry it with you?

JAMIE: It was my mother’s.

LANDON: Oh . . . . I’m sorry I asked.

JAMIE: It’s okay, Landon. How could you have known. My mother and father were given this Bible for their wedding, but my mom was the one who claimed it first. She read it all the time, especially whenever she was going through a hard time in her life. She had it with her in the hospital when I was born. When my father found out that she had died, he carried the Bible and me out of the hospital at the same time.

LANDON: I’m sorry.

JAMIE: It just gives me a way to . . . to be a part of her. Can you understand that?

LANDON: (to audience) The night of the play was cool and crisp. [My character] Tom Thornton is [is supposed to be] amazed when he first sees the angel [Jamie], which is why he goes around helping her as she shares Christmas with those less fortunate. The first words out of Tom’s mouth are, “You’re beautiful,” and I was supposed to say them as if I meant them from the bottom of my heart. The problem, however, was that I still hadn’t nailed this lie yet. Sure, I said the words, but they didn’t come off to convincingly. I kept trying to imagine someone else as the angel so that I could get it just right. The next thing I knew, the curtain was opening and I was walking past storefronts and looking in windows for the music box my daughter wants for Christmas. My back was turned from where Jamie entered, but I heard the crowd collectively draw a breath as soon as she appeared on stage. I readied myself to turn around, and when I did, I finally saw what it was all about. Her honey-colored hair was handing loosely, with a trace of glitter in [it], sparkling like a crystal halo. It was absolutely amazing to behold. She was smiling slightly, as if she were holding a secret close to her heart. She looked exactly like an angel.

LANDON: (to Jamie) You’re . . . . You’re beautiful (to audience) And I think that everyone in the whole auditorium knew that I actually meant it. To say that the play was a smashing success was to put it mildly. But because of Jamie’s presence, it really became something special . . . . [After the play] Jamie insisted that I go with her to the orphanage on Christmas Eve.

JAMIE: I’m so glad you could come.

LANDON: So am I . . . . I bought you something . . . . A gift, I mean.

JAMIE: You didn’t have to do that.

LANDON: I know, but I wanted to.

JAMIE: I brought you something, too. Please, open it. I want you to have it.

LANDON: (to audience) I already knew what was inside, and I couldn’t believe what she had done. My hands began to tremble. When it was finally free of the paper, I slowly ran my hand over the top of the well-worn leather as tears filled my eyes. Jamie had given me her Bible.

JAMIE: Thank you for doing what you did. It was the best Christmas I’ve ever had.

LANDON: (to audience) She smiled at me and I smiled at her and all I could do was wonder how I’d ever fallen in love with a girl like Jamie Sullivan. I drove Jamie home from the orphanage later that night.

JAMIE: Landon, do you ever think about God? Do you ever wonder why things have to turn out the way they do? I’ve been thinking about it a lot lately. I know the Lord has a plan for us all, but sometimes, I just don’t understand what the message can be. Does that ever happen to you?

LANDON: Well, I don’t think that we’re meant to understand it all the time. I think that sometimes we just have to have faith.

JAMIE: (thoughtfully) Yes, you’re right.

LANDON: I realized that Jamie had been misunderstood her entire life, not only by me, but by everyone. Jamie wasn’t simply the minister’s daughter, someone who read the Bible and did her best to help others. Jamie was also a 17-year-old girl with the same hopes and doubts that I had. At least that’s what I assumed, until she finally told me.

JAMIE: People think I’m strange, don’t they? Do you think I’m strange, too?

LANDON: You’re a wonderful person, Jamie. You’re beautiful, you’re kind, you’re gentle . . . you’re everything that I’d like to be. I love you, Jamie. You’re the best thing that ever happened to me.

JAMIE: (beginning to cry) Please don’t say that. . . Please . . . . I’m sorry. I’m so, so sorry . . . You can’t be in love with me, Landon We can be friends, we can see each other . . . but you can’t love me.

LANDON: Why not?

JAMIE: Because, I’m very sick, Landon. I’m dying.

LANDON: (to audience) She had leukemia; she’d known it since last summer. Time had suddenly stopped and I understood everything. I understood why she’d wanted me to do the play; why she wanted Christmas to be so special. Why she’d given me her Bible. (to Jamie) No, no, there has to be some mistake. Why didn’t you tell me?

JAMIE: I’d made a decision that it would be better if I told no one, and I asked my father to do the same. No one would look me in the eye. If you had only a few months left to live, is that what you would want?

LANDON: (to audience) I was for the first time in my life, completely and utterly at a loss. I’d been in love with her for only 18 days. Those 18 days seemed like my entire life, but now, when I looked at her, all I could do was wonder how many more days there would be. On Monday she didn’t show up for school, and I somehow knew that she’d never walk the hallways again. She was finished with school forever; she would never receive her diploma. I left school early and went to Jamie’s

JAMIE: Hello, Landon, this is a surprise. My father isn’t home right now, but if you’d like to sit on the porch, we can.

LANDON: How can you do this? How can you pretend that nothing is wrong? Aren’t you frightened?

JAMIE: Yes, I’m frightened all the time. [But] when the doctors first told us, they said that I should try to lead as normal a life as possible for as long as I could.

LANDON: There’s nothing normal about this.

JAMIE: I know. . . I know you’re frightened too.

LANDON: I began to pray for a miracle. We started reading the Bible together. On February 14, Valentines Day, Jamie picked out a passage that meant a lot to her. She told me that if she’d ever had the chance, it was the passage she’d wanted read at her wedding.

JAMIE: Love is always patient and kind. It is never jealous. Love is never boastful or conceited. It is never rude or selfish. It does not take offense and is not resentful. Love takes no pleasure in other people’s sins, buts delights in the truth. It is always ready to excuse, to trust, to hope and to endure whatever comes.

LANDON: (to audience) Jamie was the truest essence of that very description. A week later Jamie’s trips to the hospital became more regular, although she insisted that she didn’t want to stay there overnight.

JAMIE: I want to die at home.

LANDON: Since the doctors couldn’t do anything for her, they had no choice but to accept her wishes. (to Jamie) I’ve been thinking about the past few months. Do you have any regrets?

JAMIE: We all have regrets, Landon. But I’ve led a wonderful life.

LANDON: How can you say that? With all that’s happening to you.

JAMIE: I’ve been happy, Landon. I really have. I’ve had a special father who taught me about God. I can look back and know that I couldn’t have tried to help other people any more than I did. I’ve even fallen in love and had someone love me back.

LANDON: Will you do something for me?

JAMIE: I don’t know if I can anymore.

LANDON: Will you marry me? (to audience) Just as she’d wanted, the church was bursting with people as we were married on March 12, 1959. Although Jamie was weak and hadn’t moved from her bed in two weeks, she insisted on walking down the aisle so that her father could give her away.

JAMIE: It’s very important to me, Landon. It’s part of my dream, remember?

LANDON: (to audience) Then Jamie and [her dad] slowly made their way down the aisle, while everyone in the church sat silently in wonder. Halfway down the aisle, Jamie suddenly seemed to tire, and they stopped while she caught her breath. Her eyes closed, and I remember thinking it was the most difficult walk anyone ever had to make. In every way, a walk to remember.

It was, I remember, the most wonderful moment of my life. In front of God and everyone else, I’d promised my love and devotion, in sickness and in health, and I’d never felt so good about anything. It is now forty years later, and I can still remember everything from that day. I still love her, you see, and I’ve never removed my ring. I smile slightly, looking toward the sky, knowing there’s one thing I still haven’t told you: I now believe that miracles can happen.
```

---

## IC-0944: Wash and Dry

- Title: Wash and Dry
- Author (byline): Shel Silverstein
- Work: An Adult Evening with Shel Silverstein
- Publisher: Dramatists Play Service
- Publication date as stated: March 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MARIANNE, GEORGE
- Teaser before the introduction: No
- Spoken words (computed): 2179
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shel Silverstein
Book: An Adult Evening with Shel Silverstein
ISBN: 978-0822218739
Publisher: Dramatists Play Service
Date (Month/Year): March 2003
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Believe it or not, your dirty laundry can be quite revealing.

ACTOR: Not the kind of dirty laundry that makes tabloid headlines — the real stuff, the dirty clothes that lurk in your hamper and seem to grow into piles of mind-boggling dimensions in no time at all.

ACTRESS: When you walk into George's Laundromat be sure to read the sign.

ACTOR: I provide exactly what I say; nothing more nothing less.

ACTRESS: One thing is for sure, this laundry does not clean your clothes...

TOGETHER: Wash and Dry by Shel Silverstein
```

### Performance text (classify this)

```text
Setting: The Laundromat. George sits and waits. Marianne enters with laundry bag.

MARIANNE: (Entering.) Good morning. (She puts bag on counter.)

GEORGE: Good morning.

MARIANNE: It's a beautiful morning - (She rummages in purse for ticket.)

GEORGE: It's in the eye of the beholder. Wash and dry?

MARIANNE: Yes. Thank you. It's a fresh brisk morning. (Still looking for ticket.)

GEORGE: (Weighing.) You know how many fresh brisk mornings there have been in the world? Millions - hundreds of millions - and what good has it done? Five forty-three.

MARIANNE: Well it's cool and crisp and not a cloud in the sky - all you can see are blue skies - (She pays.)

GEORGE: If I can see blue skies it's not a beautiful day - you know what's a beautiful day? When I can't see any skies at all - when those laundry bags are piled so high you can't see the sky at all - that's what I call a beautiful day - (He takes bag.)

MARIANNE: Here's my ticket - I usually lose the ticket. I feel very proud of myself for having it.

GEORGE: (Reading.) Twelve-oh-seven - (She looks around)

MARIANNE: That's it up there, the blue bag.

GEORGE: All the way up there.

MARIANNE: The blue bag with the rope string. It matches this one.

GEORGE: Well?

MARIANNE: Well? It's mine.

GEORGE: Well, nobody's saying it isn't yours. Who's saying it isn't yours?

MARIANNE: Well, may I have it please?

GEORGE: Sure you can have it. It's yours.

MARIANNE: May I have it now - why not now - Well?

GEORGE: Go get it.

MARIANNE: Go get it?

GEORGE: Why not? It's yours, isn't it?

MARIANNE: I should go get it?

GEORGE: Watch your step climbin' up there - don't step on the top rung - it's rickety - I can't be responsible if you step on that top rung.

MARIANNE: Why don't you get it?

GEORGE: Ha-ha. That's a very good question. You want a very good answer - I don't get it because I don't have to get it - I didn't agree to get it - wash and dry - not wash, dry and get.

MARIANNE: Getting it - is - just part of the service - it's expected.

GEORGE: By you.

MARIANNE: By anyone - It's expected that when you pick up your-

GEORGE: Don't expect too much of life - you'll be sorely disillusioned - you're talking to somebody who knows - don't expect a bed of roses.

MARIANNE: A bed of roses? It's just a common courtesy - it's only-

GEORGE: I did not promise wash, dry and courtesy, did I?

MARIANNE: Obviously not.

GEORGE: Well then, I'm not guilty of false advertising, am I? Am I?

MARIANNE: You're really not going to get it.

GEORGE: Wash and dry, period. (He reads newspaper.)

MARIANNE: Well - I'll tell you something - (She begins to climb.) You don't know how to run a business.

GEORGE: You get what you're promised - consider yourself lucky - most of the time we don't even get what we're promised.

MARIANNE: (Pulling laundry down.) Oops.

GEORGE: I warned you about that ladder, didn't I? I warned you loud and clear - I said it's rickety.

MARIANNE: I'll tell you something else. I'm not coming back here anymore.

GEORGE: Never say never - We don't know what we'll do - circumstances - change.

MARIANNE: And ... And if I hadn't paid for this in advance, I wouldn't pay for it now.

GEORGE: Oh, I know that - and that's exactly why I collect in advance - exactly why.

MARIANNE: And you'd better not have shrunk my blue cotton blouse - (She rummages through bag.) I distinctly said - no hot water-

GEORGE: No hot water was used - it's not shrunk.

MARIANNE: It better not be.

GEORGE: I guarantee it.

MARIANNE: (Pulling blouse out.) God.

GEORGE: Well-

MARIANNE: It - it's not even –

GEORGE: I told you.

MARIANNE: It hasn't been - washed - it's still - it's just like it was when I brought it in

GEORGE: No shrinkage - a promise made, a promise fulfilled - but don't get used to that - don't start expecting that in the rest of your beautiful day -

MARIANNE: It's all - they're all - still dirty. These clothes have not been washed. You make me climb up and risk my neck to get my own laundry that you forgot to wash -

GEORGE: I didn't forget. You don't stay in business by forgetting.

MARIANNE: You didn't forget? You just did not -

GEORGE: You get what you contracted for.

MARIANNE: What I contracted for? I contracted for dirty clothes? I brought them in here to be washed and dried - I contracted for -

GEORGE: Watched.

MARIANNE: What?

GEORGE: Watched - not washed. Watch and dry.

MARIANNE: Watched?

GEORGE: George's Watch and Dry. (Sign.) You gotta pay attention - They'll rob you blind. They'll take the gold fillings out of your teeth.

MARIANNE: George's Watch and Dry?

GEORGE: They count on the fact that people don't pay attention - they depend on that.

MARIANNE: I paid five dollars and forty-three cents to have my clothes watched?

GEORGE: And dried.

MARIANNE: But you haven't washed them.

GEORGE: I've watched them. I've been watching them for five days-

MARIANNE: Why would somebody want to have their clothes watched? Why?

GEORGE: Why is a goose not a gander? There's lots of strange people in this town - bizarre people with unusual needs - and desires. I don't ask questions - They want watch and dry, they get watch and dry.

MARIANNE: I did not come here to have my clothes watched. I did not pay five dollars and forty-three cents to have my clothes watched.

GEORGE: And dry.

MARIANNE: Of course they're dry. They've never been wet. I paid to - have my clothes washed - washed.

GEORGE: You should have taken them to a laundromat.

MARIANNE: I thought this was a laundromat. That's why I –

GEORGE: Marianne - Marianne - don't agitate yourself.

MARIANNE: You know my name?

GEORGE: I'm not like some people. I care. I pay attention. Read the small print - if you don't they'll skin you alive - they'll peel you like a grape.

MARIANNE: You're peeling me like a grape - you're charging me-

GEORGE: I'm teaching you - you've got to -

MARIANNE: Teaching me? By charging me five dollars and forty-three cents to watch my clothes? You think that's teaching?

GEORGE: If the lesson was free, you wouldn't learn it.

MARIANNE: I assume you're not giving me my money back.

GEORGE: This is not George's free Watch and Dry –

MARIANNE: Well, I'm going to the police - directly - I'm going to the Better Business Bureau and they are going to be all over you like a rash. I am not one of those people who suffer in silence. I do not get fleeced silently - I'm not a sheep. I get raped and I identify the rapist. I hunt him down and see him prosecuted and punished -

GEORGE: I'm only teaching you what they taught me - I'm passing on the information.

MARIANNE: Information? That people will take your money on a technicality - for watching your laundry - what kind of information is that?

GEORGE: It's real information - all the love thy neighbor do unto others - sisters and brothers stuff - that's all misinformation - you know what they did to me? They guaranteed my color TV - at least I thought they guaranteed it - I assumed - I assumed that was what I was paying three hundred and eighty-five dollars for - and then when the tube blew - then and only then did they inform me that it was not a guarantee - but a warranty - that's when they told me to read the fine print.

MARIANNE: Your color TV has nothing to do with –

GEORGE: That was the beginning of my education - my transmission was another lesson - my electrical wiring was another lesson - and my re-upholstery - and my Blue Cross - oh, they've taught me a lesson or two - That's when I started paying attention - that's when I started passing along the information.

MARIANNE: That's when you started watching clothes.

GEORGE: Yes, as matter of fact.

MARIANNE: For five dollars and forty-three cents.

GEORGE: Two fifty a load - plus tax.

MARIANNE: A load? Of what? What load.

GEORGE: A machine load.

MARIANNE: Which never goes into the machine.

GEORGE: It's a measurement - You've got to pay attention - Because something is a machine load doesn't mean it gets into a machine. Are you beginning to comprehend?

MARIANNE: I comprehend that you have charged me five dollars and forty-three cents to watch - my laundry - and there's not proof that you have even watched it. I am going to the police - I really am -

GEORGE: Go ahead, go to the police - And try to prove I didn't watch your stupid laundry - and I'll tell you something else, sweetheart - of all the laundry I ever watched, yours was the most bizarre -

MARIANNE: Bizarre? My laundry was - ?

GEORGE: Item - chocolate stains on nightgown

MARIANNE: Chocolate stains?

GEORGE: Or hot fudge - Who am I to say? - I'm no goddamn chemist - and butterscotch stains on nightgown, denoting late night-

MARIANNE: You looked through my laundry -

GEORGE: I watched your laundry - you want more proof? Item stains on blouse - denoting early day dieting and late-night loss of willpower - also sloppy eating, I might add.

MARIANNE: Sloppy eating - you're judging my - ?

GEORGE: Item - wine stains on slacks, denoting heavy drinking and possible alcoholism.

MARIANNE: Alcoholi-

GEORGE: Or potential alcoholism - Item - one white capsule - possibly Nembutal - in pocket of -

MARIANNE: Possibly what?

GEORGE: Or it might be an aspirin - How would I know? That's for the boys in the lab to figure out.

MARIANNE: What boys? What lab?

GEORGE: That's for me to know and you to find out. If it turns out to be an aspirin, you have my apology - but if it turns out to be a Nembutal - I'd say cut out the booze - It's a dangerous combination. Item - One pair of pantyhose - one pair - two weeks' laundry - four sets of sheets and pillowcases and only one pair of pantyhose. Leaving owner's personal hygiene in question.

MARIANNE: You - you count my sheets and my –

GEORGE: And upon two of those sheets - a dried white residue - possibly semen - I say possibly - possibly dried rubber cement - possibly semen - possibly indicating a certain sexual promiscuity -

MARIANNE: I can't believe -

GEORGE: Item - blood stains on underwear and white skirt, denoting unusually heavy menstrual flow and possibly due to recent dilation and curettage. (Marianne gasps - sobs, whimpers, stammers') Don't get yourself agitated - learn your lesson - epileptics have to be careful- fill your prescription - (He unfolds it.) Don't leave it in your pocket - stay on your medication - don't get agitated. Don't spend time with men who give you ... problems.

MARIANNE: How would you like your neck broken? Really - my boyfriend - I could tell him what you're - he's a big guy he is - he could just break your little neck - how would you like that?

GEORGE: How would his wife like that? - Your big guy - (Takes shirt.) Eighteen-inch neck, thirty-six sleeve - initials Y.R. - V.R. - Vincent Romo? - Dispatcher control at United? - Eh? - Y.R.? I think we may have the mystery man here.

MARIANNE: Mystery man?

GEORGE: Possibly the donor of said semen - or said rubber cement - possibly the reason for said alcoholism - and said compulsive overeating - possibly - of course, if your father or brother's initials are Y.R - then there's no problem - but that is highly doubtful since your mother's initials are R.D. - unless, of course, she married again, in which case -

MARIANNE: My mother?

GEORGE: (Reading letter.) Mrs. Donovan, 623 Lake Terrace Road, Milwaukee, Wisconsin? You should answer her letters - she would like some news of you - some news - 623 Lake Terrace Road - it sounds like a nice street - they've put in some poplar trees across from the Hanleys' place - but she doesn't think they'll take-

MARIANNE: I know what it says - give it to me - (She grabs the letter.) That's my property.

GEORGE: Hey, it's yours - you've got a right to it - 623 Lake Terrace Road, I think the zip is four-oh-oh-five - but I could look it up

MARIANNE: You could look it up -

GEORGE: If I wanted to - If I chose to - you don't control the postal service, you know - I can write to whom I choose - I don't need a warrant to write to whom I choose - I'm free to –

MARIANNE: You - You cannot do this - You cannot violate a person's life - by prying into their laundry - Listen, my father happens to be a very prominent attorney in Milwaukee - I happen to know something about the law - do you realize what you're perpetrating? Breach of contract - charging me for services not recei-

GEORGE: W-A-T-C-H - clearly stated - W-A-T

MARIANNE: Invasion of privacy - going through my –

GEORGE: Hey, I have to handle - that's part of my

MARIANNE: Slander - accusing me of -

GEORGE: I'm not accusing - this is accusing - Item - small white powdery residue in front of blue wool sweater - possibly cocaine - possibly face powder - I'm not a goddamn criminologist - call' em in and we'll settle the question - Your property? - Hey, it's none of my business, it's your business - Possibly American Airlines might think it's their business - but I –

MARIANNE: Go ahead - tell them - Just try to tell them. Tell them I-

GEORGE: I won't tell 'em, I'll show 'em.

MARIANNE: Show them what? - This - (Grabs it - George shows Polaroids.) You took ... Polaroids ... of my - (Reaches.)

GEORGE: Uh-uh - my property - to substantiate my claim-that I watched - you question whether I really watched - You cast aspersions on my professional integrity - Okay, I got proof - I watch-

MARIANNE: You are a rotten, vicious - perverted –

GEORGE: I pay attention - the police pay attention - I'm trying to teach you to pay attention - watch and dry - watch and dry - read the small print. (Marianne begins to walk out slowly with laundry) Will I be hearing from your father? Your big boyfriend? Will I be seeing you in court? ... Next Tuesday then.

MARIANNE: Next Tuesday - ?

GEORGE: Before four o'clock - I close at four on Tuesday.

MARIANNE: You think I'd ever bring my laundry in here again - to be watched - to be - violation - a breach of contract –

GEORGE: What's legal? What's illegal? (He fingers vial with cocaine sample - Marianne stops.) Okay then - (He takes pencil.) I'll put you down for an eight-pound load on Wednesday - every Wednesday - (Marianne bites her lip and leaves.) You got to read the small print - they'll squeeze you like an orange - Don't think they won't - Don't assume anything - Pay attention, for God's sake -

(He sits back down and opens newspaper. Marianne exits, in shock.) And let's not wait two weeks on the pantyhose - eh?
```

---

## IC-0945: Wedding Duet

- Title: Wedding Duet
- Author (byline): Lauren Wilson
- Work: Laugh Lines: Short Comic Plays
- Publisher: Vintage
- Publication date as stated: April 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BRIDE, GROOM
- Teaser before the introduction: No
- Spoken words (computed): 1503
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lauren Wilson
Book: Laugh Lines: Short Comic Plays
ISBN: 978-0307277138
Publisher: Vintage
Date (Month/Year): April 2007
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: I (state your name) take thee, (state your name), to be my wedded husband/wife

ACTRESS: To have and to hold, from this day forward,

ACTOR: For better, for worse, for richer, for poorer,

ACTRESS: In sickness and in health, to love and to cherish,

TOGETHER: Till death do us part.

ACTRESS: The ceremony ends . . . you may kiss the bride . . . Yadda, Yadda Yadda . . .

ACTOR: And suddenly you're not in wedding fantasyland anymore. You're in a full-out battle over something trivial

TOGETHER: Wedding Duet by Lauren Wilson
```

### Performance text (classify this)

```text
A closed door. Laughter behind it. A key is put into the lock--more laughter. The knob turns and the door opens. The GROOM stands on the threshold, carrying the BRIDE.

BRIDE: Oh my God. This is so perfect! It's so adorable! Look at the little fireplace!

GROOM: Very cute. Here, can I put you down while I get a better grip?

BRIDE: You can't put me down here!

GROOM: Okay, let me just give you a boost then. (He does.) That's better.

BRIDE: Hang on, my veil's pulling.

GROOM: Why don't you just take it off?

BRIDE: I can't take it off yet! I think your foot's on it.

GROOM: It is? (He steps aside.) Look, let's just go in. My arms-

BRIDE: Okay, but wait. The photographer's not here.

GROOM: We don't need a picture of this. Let's just remember it.

BRIDE: You're right. Let's take it all in so we'll never forget this moment. (They do.)

GROOM: Honey?

BRIDE: Wait a minute. Just one more second.

GROOM: My arms- (He drops her on the threshold.)

BRIDE: Oh my God!

GROOM: Are you all right? Did you hit your head?

BRIDE: No, I'm all right. Are you all right?

GROOM: Sure, I'm fine. I just couldn't hold on anymore.

BRIDE: I'm sorry. It was my fault. I shouldn't have made you-

GROOM: No, it was my fault. I should have braced my- (They look at each other and laugh.)

BRIDE: Can you believe this? Who else but us? (More laughter.)

GROOM: Dropping you right on the threshold! (They laugh again. Her laughter turns to crying.) Honey? (She is sobbing hard now. She turns away and faces the door frame.)

GROOM: Sweetheart?

BRIDE: It's just so-- (Sobs more.)

GROOM: Is it the dress? I'm sure your mother can-

BRIDE: It's not the dress! It's the whole thing! The whole disgusting, hideous thing!

GROOM: Which disgusting, hideous thing?

BRIDE: Everything! (He contemplates this. She sobs.) I mean, of course I fall down in the threshold! Of course! I can never do anything right!

GROOM: Now, look. Let's not turn this into a ... you know, okay? So you fell down in the threshold. Big deal!

BRIDE: It is a big deal. It's a symbol!

GROOM: No, it's not. It's just something that happened. And the longer we talk about it ...

BRIDE: But we have to talk about it. If we don't talk about it, I'll just keep feeling bad about it.

GROOM: Okay, let's talk about it. Why don't we go in and make a fire in the little fireplace?

BRIDE: No! We can't just go in there! (He considers this. He sits down beside her, squeezed into the door frame.) I just feel this huge sense of, I don't know . . . doom.

GROOM: Doom.

BRIDE: Like when I woke up this morning. I just had this feeling that I was totally alone. It's not that I didn't want to get married, that's not what I'm saying at all. I wanted to get married. It's just ... Oh, God, I don't know!

GROOM: So are you saying --

BRIDE: And then all those roses. My God! My God!

GROOM: (Waits for more.) You mean-

BRIDE: All I could think about was how much money it cost, and how one day my parents are going to die, and how tomorrow-tomorrow!-the roses are all going to be thrown in the trash somewhere. Or tonight! They're going to be totting in some Dumpster and filling up a landfill and I'm going to have to put my parents in the ground one day and throw dirt on them.

GROOM: I think this is getting kind of ... Blown out of proportion. I mean, if I hadn't dropped you, would we be having to sit here and talk about all this stuff? No, we'd be in there having fun.

BRIDE: You mean you're not having fun?

GROOM: No! Well, I mean, not right this second.

BRIDE: Are you unhappy? I mean, being married. Are you unhappy being married?

GROOM: No! How do I know? We've been married for three and a half hours! (She looks at him, he looks at her. They burst out laughing. The laughter grows, becomes hysterical, then subsides.) Okay? Are we okay now?

BRIDE: I think so. I just had to- Will you carry me across now?

GROOM: Absolutely. Let's do this thing. (They stand and prepare.)

BRIDE: Ready? (She jumps into his arms.) Here we go! (He hesitates.) Honey?

GROOM: Hang on.

BRIDE: What is it? What's wrong? (He puts her down.)

GROOM: It's . . . It's the thing about the symbol. I wish you hadn't said that. I hadn't been thinking that way until then, and now that you said it, it's all I can think about. Suddenly I'm just this groom person and you're just this puffy bride-

BRIDE: Puffy? You said puffy.

GROOM: I was just trying to make. a point, which is that as long as we're talking about the symbol, what does it mean that I'm carrying you, anyway?

BRIDE: I think it means you're going to support me and hold me for the rest of my life. (He looks at her. He considers this. He sits down.) Honey?

GROOM: Just give me a minute. I thought we were just walking through a door.

BRIDE: Maybe it's not a symbol at all.

GROOM: Oh, it's a symbol, all right. It's definitely a symbol.

BRIDE: Well, if you don't want to carry me, why don't you just say so?

GROOM: Why don't I? Well, because ... Because you'll flip out.

BRIDE: No, I won't.

GROOM: All right. I don't want to carry you. (She considers this.)

BRIDE: Would you rather shove me?

GROOM: See, I knew you'd flip out.

BRIDE: I'm not flipping out. I'm joking.

GROOM: And now that you're flipping out it means we're going to spend the next three hours-

BRIDE: But I'm not flipping out! I'm trying to tell you that I'm not flipping out! (A pause.)

GROOM: Look-

BRIDE: Oh, great. Here we go. . . Go on, I'm listening. . .

GROOM: I was going to say, the vein in my temple is starting to throb, and maybe if I just lay down on the bed for a minute-

BRIDE: But you can't lay down on the bed! You can't just ignore it! We have to resolve this!

GROOM: But we're not going to resolve this by standing here and talking!

BRIDE: I can't believe this. You'd actually do that to me? Leave me standing here alone on the threshold?

GROOM: No! No! Just for, like, ten minutes. I'll come get you as soon as my head stops pounding.

BRIDE: (Crying.) And what am I supposed to do in the meantime? Just stand. out here in the hall?

GROOM: I don't know, Maybe some of the guests are still down at the party.

BRIDE: Down at the party! Down at the ... The bride can't go back to the party!

GROOM: Okay, fine. I give up. You don't want to come in, you don't want to go downstairs, you just want to stand here and be miserable for the rest of our lives.

BRIDE: No! No! Not be miserable. Talk it over! Talk it over!

GROOM: Talk what over? We've already talked so long I can't even remember what we're fighting about! I have no idea what we're fighting about! We're not fighting about anything except about how we're fighting!

BRIDE: I can't believe you just said that.

GROOM: Oh, fine, sure. I'm a jerk because I can't remember. All right then, you tell me-what are we fighting about? I bet you can't remember either.

BRIDE: We're fighting because you're not willing to work through conflict.

GROOM: Not willing to! Are you kidding? I've never worked so hard in my life! It's like pulling a train uphill with my teeth! And no, that was not a reference to your weight! (They glare at each other.)

BRIDE: Now you listen to me, buster. We're married now!

GROOM: Oh, yeah, you got that right. You got that perfectly right!

BRIDE: Either you stay here and talk about this with me or ...

GROOM: Or what?

BRIDE: Or I'm leaving!

GROOM: You're leaving.

BRIDE: Yes.

GROOM: Leaving as in leaving to walk around the block, or leaving as in leaving for good!

BRIDE: Well, I don't know. All I know is, I can't be with someone who doesn't know how to work through conflict.

GROOM: (Bride attempts to interrupt multiple times, but Groom just keeps going) Okay. Okay, I get it now. It's all making perfect sense. What you're saying to me, what you're actually saying to me on our wedding night is that if I don't stand here in the threshold of this cheesy country inn until I drop dead from exhaustion in the attempt to find whatever combination of words is going to "resolve the conflict" and make you feel like the world isn't ending, which is not my responsibility, you know, and which I refuse to-

BRIDE: I wanted to get married in Cancun, remember? You were the one who said let's save the money

GROOM: Don't change the subject-

BRIDE: I brought all the brochures home and had the whole thing-

GROOM: I'm not talking about that! I'm talking about the fact that you-

BRIDE: But you told me to find an inn!

GROOM: I didn't mean-

BRIDE: And now all of a sudden--

GROOM: That's not the point! That's not the point! I didn't even want to get married! (A silence. She screams. He tries to stop her, but she won't stop. He slaps her hard across the face. She slaps him back. They wrestle each other in the doorway, trying to kill each other, until they wear themselves out. She lies panting on the ground; he leans exhausted against the frame. He reaches into his mouth and removes a tooth, spits blood onto the floor. He cleans his mouth with his tie.) Are you all right? (She doesn't answer.) I said, are you all right?

BRIDE: No. Don't talk to me. (She pulls herself up the door frame to her feet. One of her ankles hurts.)

GROOM: Here, let me-

BRIDE: Don't touch me. Don't ever touch me again!

GROOM: Fine. (They stand next to each other.)

BRIDE: I think my ankle's broken.

GROOM: Do you want me to look at it?

BRIDE: No . . . . All right. (He kneels and does this. She winces.)

GROOM: Maybe you should get it X-rayed.

BRIDE: I just want to lie down.

GROOM: Here-- (He puts an arm around her. They stand awkwardly like this.) Do you want to lay on the bed?

BRIDE: All right. No. Wait. You really didn't want to get married?

GROOM: Of course, I did. (He smiles at her. She smiles at him.)

BRIDE: Your mouth's bleeding.

GROOM: I know. Let's go in.

BRIDE: Okay. (Pause) Why did you say it, then?

GROOM: Say what?

BRIDE: That you didn't want to get married.

GROOM: I meant at first. When you brought the brochures home. That's all I meant.

BRIDE: Oh, good. When did you change your mind?

GROOM: Jesus Christ! Can we not do this?

BRIDE: Do what?

GROOM: Start fighting again? (He puts his arm around her.) Can you walk?

BRIDE: I think it's broken.

GROOM: Here. (He picks her up in his arms. They look at the room through the doorway. He gives her a boost. Lights down.)
```

---

## IC-0946: Weights and Measures

- Title: Weights and Measures
- Author (byline): Jodi Picoult
- Work: Stories: All-New Tales, eds Neil Gaiman and Al Sarrantonio (Pg 135-149)
- Publisher: William Morrow Paperbacks
- Publication date as stated: June 2011
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TOGETHER, NARRATOR 2, SARAH, ABE, NARRATOR 1, FUNERAL DIRECTOR, PASTOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1256
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jodi Picoult
Book: Stories: All-New Tales, eds Neil Gaiman and Al Sarrantonio (Pg 135-149)
ISBN: 978-0061230936
Publisher: William Morrow Paperbacks
Date (Month/Year): June 2011
```

### Introduction (context only: never use it for content warnings)

```text
Weights and Measures by Jodi Picolt
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actor: Narrator 2; Abe, Pastor

Actress: Narrator 1; Sarah, Funeral Director

TOGETHER: The loudest sound in the world is the absence of a child.

NARRATOR 2: Sarah found herself waiting for it, the moment she opened her eyes in the morning: that satin ribbon of a giggle, or the thump of a jump off the bed—but instead all she heard was the hiss of the coffeemaker that Abe must have preset in the kitchen last night, spitting angrily as it finished its brewing.

SARAH: We have to get up. . . Abe.

ABE: Right.

NARRATOR 1: He pushed off the bed in one motion and closeted himself in the bathroom, where he ran the shower long before he stepped inside, incorrectly assuming the background noise would keep anyone outside from hearing him cry.

NARRATOR 1: The worst day of Abe’s life had not been the one you’d imagine, but the one after that, when he went to choose his daughter’s coffin.

NARRATOR 2: Sarah begged him to go; said she could not sit and talk about what to do with their daughter as if she were a box of outgrown clothing that had to be stored somewhere safe and dry.

NARRATOR 1: The funeral director was a man with a bad comb-over and kind, gray eyes, and his first question to Abe was whether he’d seen his daughter. . . afterward. Abe had --

NARRATOR 2: -- once the doctors and nurses had given up and the tubes had been removed and the crash carts pulled away, he and Sarah were given a moment to say good-bye. Sarah had run out of the hospital room, screaming. (Abe sits down on the edge of the hospital bed and threads his fingers with his daughter’s. He pulls her into his arms and sobs)

NARRATOR 1: She weighed just the tiniest bit less than she had that morning, when he’d carried her through the double doors of the emergency room.

NARRATOR 2: Medical examiners say a person who died lost twenty-one grams of weight—the measure of a human soul.

NARRATOR 1: He realized, though, holding his daughter in his arms, that the scale was all wrong. Loss should have been measured in leagues: the linear time line he would not spend with her as she lost her first tooth,

NARRATOR 2: lost her heart over a boy,

NARRATOR 1: lost the graduation cap she tossed into a silvered sky.

SARAH: It had only been a sore throat. Her fever wasn’t more than 101. That was the criteria— you weren’t supposed to worry about a fever until it spiked past 102.

ABE: Children weren’t supposed to die of strep throat, but then again, you did not have to look far for the shouldn’ts. All over this world there were tsunamis sweeping entire countries out to sea;

SARAH: . . . there were Eskimo women with breast milk full of mercury;

ABE: . . . there were wars being fought that had been started for the wrong reasons.

TOGETHER: All over this world impossible things were happening that never should have. ****Scene****

FUNERAL DIRECTOR: We suggest that you dress your daughter the way she would have wanted. Did she have a favorite party dress, or a pair of overalls she always wore to climb trees? A T-shirt from a favorite vacation?

ABE: There were other questions, and decisions to be made, and finally, (beat) a coffin. [At] the far end of the room three stunted coffins were propped like brave soldiers. [I] picked one painted a glossy white. (Abe keeps staring at it)

NARRATOR 1: It did not seem large enough to hold a girl as full of life as his daughter. It was certainly not large enough to pack inside the turtle shell of grief that he’d armored himself in this past day.

ABE: Which meant, of course, that even after [she] was gone, the sorrow would remain behind. *****Scene*****

NARRATOR 1: The funeral was held at a church neither Abe nor Sarah attended, a service arranged by Sarah’s mother, who in spite of this still managed to believe in God.

PASTOR: (at the pulpit) Try to remember, as we celebrate her short and glorious life, that sadness comes out of love. Sadness is a kind of terrible privilege. Oh, Lord, receive this child of Yours into the arms of Your mercy and into the company of angels.

NARRATOR 2: Ten minutes later, it was over. [Sarah] remained stone still while everyone left.

SARAH: (she walks to the open coffin and forces herself to look at her daughter, she speaks softly) Hey, baby. (she pulls a book out of her purse and begins to read) In a great green room . . . there was a fireplace, and a red balloon, and a picture of . . . (she hesitates)

NARRATOR 2: This was the part where her daughter would have chimed in: the cow jumping over the moon. But now, Sarah had to say the words for her.

SARAH: The cow jumping over the moon.

NARRATOR 2: She read through to the end, going by heart when the tears came so furiously that she could not see the words on the page.

SARAH: (whispering) Goodnight stars. Goodnight air. Goodnight noises everywhere. (she takes a ragged breath and touches her finger to her daughter’s lips) Sleep tight. (long beat) *****Scene*****

NARRATOR 2: A week after their daughter’s death, Sarah could not stop thinking about her. She would pick up a newspaper and feel instead the rubbery band of small socks between her fingers as she folded them over after doing the wash. She’d be in one room and hear the music of her daughter’s voice, the way grammar leaped through her sentences like a frog.

NARRATOR 1: Abe, on the other hand, was starting to lose her. He would close his eyes and try to conjure up his daughter’s face, and he still could, but it was unraveled at the edges a little more each day. He found himself spending hours in her bedroom, inhaling the smell of her strawberry-mango shampoo still trapped in the fibers of the pillowcase, or poring through the books on her shelves and trying to see them through her eyes. *****Scene*****

NARRATOR 2: [So it was not surprising when Sarah] showed up at the church, shuddering as she remembered the hymns that had been played at her daughter’s funeral, steeling herself for the absence of the coffin at the altar. (Sarah knocks on the pastor’s door and as he opens it . . .)

SARAH: Can I ask you something? Why her? . . . I get the whole God thing. But there are millions of seven-year-olds out there. Why did God take mine?

PASTOR: (hesitating) God didn’t take your daughter, Sarah. Illness did.

SARAH: (snorting) Sure. Pass the buck when it’s convenient.

PASTOR: Heaven’s an amazing place. (softly) She’s up there, and she’s looking down on us, right now, you know.

SARAH: My daughter can’t ride a ski lift without hyperventilating. She panics in elevators. She doesn’t even like bunk beds. She’s terrified of heights.

PASTOR: Not anymore.

SARAH: (exploding) How do you know that? How do you know that there’s anything afterward? How do you know it doesn’t just. . . end.

PASTOR: I don’t know. But I can hope. And I truly believe that your daughter is in heaven, and even if she does still get scared, Jesus will be there to keep her safe.

SARAH: She doesn’t know Jesus. She knows me. *****Scene*****

(Sarah is in her daughter’s room, packing away books into boxes – she is all business)

NARRATOR 2: Sarah and Abe did not really speak to each other, not until . . .

ABE: (Enters and sees what Sarah is doing; he is stricken) What are you doing?

SARAH: I can’t move past this knowing it’s all right down the hall.

ABE: No.

SARAH: What do you mean, no?

ABE: (taking books from the box and jamming them back on the shelf) Just because you’re ready to give her up doesn’t mean I am.

SARAH: (whispering) Give her up? (angrily) Is that what you think I’m doing? For God’s sake, Abe, all I want to do is function like a normal human being again.

ABE: But you’re not normal. We’re not normal. (his eyes fill with tears) She died, Sarah. (Sarah winces; long beat) I lost her. Please don’t tell me I’ve lost you too.

NARRATOR 1: She thought about running her hand through his dark curls, but like most moments, it was gone before she remembered to act on it.

SARAH: (hardening in the face of his grief – she retreats) Maybe I need to be alone for a while.

(Sarah exits)

NARRATOR 1: It was as if, in this new world, where the impossible had actually happened, nothing fit anymore: not language, not reason, not even the two of them.

ABE: What? (his voice raw) What did I do wrong? (long silence)

NARRATOR 1: The loudest sound in the world is the absence of a child. (Abe sobs)
```

---

## IC-0947: What I Learned From Grizzly Bears

- Title: What I Learned From Grizzly Bears
- Author (byline): Jessica Lind
- Work: The Best 10-Minute Plays for Two Actors 2006
- Publisher: Smith and Kraus
- Publication date as stated: September 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BERNADETTE, HUSBAND, TIME, A NOTE ABOUT THE PLAY, ACTRESS, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1796
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jessica Lind
Book: The Best 10-Minute Plays for Two Actors 2006
ISBN: 978-1575255637
Publisher: Smith and Kraus
Date (Month/Year): September 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Stillbirth happens more often than we imagine—10 times more often than sudden infant death syndrome, or SIDS, The impact is impossible to measure.

ACTRESS: Fathers, and especially mothers —must figure out how to absorb the vast and sudden sadness, to grieve and, in many instances, to reconcile with a God who has shaken their faith to its core.

ACTOR: Decades ago, stillborn babies were whisked away from their parents to morgues; doctors and nurses pretended nothing happened, mothers were medicated with Valium, parents suffered their sorrow alone.

ACTRESS: It was in the late 1970s and early 1980s that the medical and psychological thinking about stillbirth began to evolve when researchers started studying the impact of a baby’s death and parents began telling their stories.

ACTOR: From silence and detachment came acknowledgment and remembrance. Today
```

### Performance text (classify this)

```text
BERNADETTE: mid-twenties. A biologist with an intense passion for grizzly bears. She is feisty, easily excitable, and a little quirky. She is almost completely oblivious to anything happening around her.

HUSBAND: late twenties. He genuinely loves Bernadette.

TIME: A muddled present

A NOTE ABOUT THE PLAY: Be aware that the events in this play do not occur in real time. With that in mind, please steer clear of overly literal interpretations.

nurses encourage parents to hold the babies.

ACTRESS: Molds of hands and feet are created. Locks of hair are collected. And photographs are taken. Not just the clinical snapshots that nurses have been capturing for years, but striking and sensitive portraits.

TOGETHER: What I Learned from Grizzly Bears by Jennifer Lind

Bernadette stands behind a table, engrossed in a map of Alaska. A faint beeping noise can be heard.

BERNADETTE: I'm mostly interested in studying how a grizzly's diet relates to its behavior. You wouldn't believe how much impact changes in the environment have on a grizzly. The salmon population in Alaska, for example, has been dwindling because of dams and runoff in the rivers which is a huge portion of a grizzly's diet in the summer. And if the salmon are gone, the grizzlies get desperate and when they get desperate they get mean and when they get mean ... Well, you just better watch out that's what. I'm planning on moving to Alaska to study them. I've already mapped out my research strategy, invested in equipment. All I have to do really is buy my ticket. I mean, there are people out there just dying to give me money. You wouldn't believe how easy it is to get a research grant. This is America buddy you better believe it. Is this parsley?

HUSBAND: Cilantro.

BERNADETTE: I bet you wouldn't believe I was valedictorian of my university, would you? I was. Summa cum laude with a double major and thirty extra credits. Then it was on to graduate school. I'm telling you I am getting pumped. I'm finally finished with school and I am blazing. Nothing is stopping me from getting on a plane tomorrow. I'm on my way up! I'm standing on the edge of the diving board, ready to jump and all I have to do is-

HUSBAND: Don't stand on that.

BERNADETTE: What?

HUSBAND: You can't stand on that.

BERNADETTE: Oh, right. Sorry. (She lies down on what is now a table. She's completely oblivious to what's going on around her. The beeping noise is foster now, and more muffled sounding. Husband is feeling her stomach.) There's something fascinating about communicating with animals in their own language. I'm really looking forward to discovering how grizzlies communicate. Oh I've read all the books and all that, but I'm talking about specifics. How does a grizzly sound when she's sad? What do the different pitches and rhythms in their growls mean? What noises do they make when making love? (Sitting up.) I'd imagine it's a kind of "uhh uhhh" kind of grunting. You know like -

HUSBAND: Please lie down.

BERNADETTE: Geez you're bossy. Anyway, these are the things I'm looking forward to.

(The beeping is so loud now she's shouting over it.) I've been applying for all kinds of grants. I have a pretty good chance at getting a research grant through my university. Hey, could you turn that thing down? I can't even hear myself talk. Geez. My research advisor is actually on the board so my chances of getting the grant are really high.

HUSBAND: Congratulations.

BERNADETTE: Well, thanks, but I haven't exactly gotten it yet. But thank you. You're a real sweetie. What did you say your name was?

HUSBAND: It's twins.

BERNADETTE: Twins? What kind of a name is that? (Mounds o/baby stuff, i.e., diapers, stuffed animals, strollers, etc ... pile up on top other. She is being buried. She continues talking through it all, oblivious to what's happening') Anyway, they only give it to alumni and I'm really the only one qualified. Well, there's this one other guy but he's all into beetles and I'm sure if it came down to choosing between beetles and grizzlies, they'd choose grizzlies. I'd feel like a real loser if I chose beetles over grizzlies. No offense to beetles or anything, but really when it comes down to it I'm sure they'd much rather be associated with grizzlies. As opposed to beetles. (Realiz-ing she's buried.) Wow, it's getting stuffy in here. Is anyone else stuffy? Urn, "Twins," is it? You wanna help me out of here? I have no idea how all this stuff got here. Pretty inconvenient though I must say. Hey! I'm buried alive here. A little help please ...

HUSBAND: Don't worry, I'll help you.

BERNADETTE: Great.

HUSBAND: That's what I'm here for, right?

BERNADETTE: I don't know. Is it?

HUSBAND: For better or worse. (He unburies her.)

BERNADETTE: Wow. You're a real nice guy. A real good-looker too. (Seeing his finger.) Crap, you're married. Figures. Oh well. Do you have a brother?

HUSBAND: No. It's just me.

BERNADETTE: Just my luck. Well? ...

HUSBAND: Well what?

BERNADETTE: Who are you?

HUSBAND: I'm your husband.

BERNADETTE: What are you talking about?

HUSBAND: We're married.

BERNADETTE: That's not possible.

HUSBAND: Check your finger. (She does. She's wearing a ring.)

BERNADETTE: Well Happy Birthday, this is news to me.

HUSBAND: Your birthday is in October.

BERNADETTE: How do you know?

HUSBAND: I'm your husband.

BERNADETTE: What else do you know?

HUSBAND: You wear a size eight shoe you wash your hair at night and you hate those little marshmallows that come with instant hot chocolate.

BERNADETTE: What do you do?

HUSBAND: I'm an insurance agent.

BERNADETTE: (Singing.) "Like a good neighbor, State Farm is there."

HUSBAND: I'm with AllState.

BERNADETTE: Super. Do you cook?

HUSBAND: No. You do that.

BERNADETTE: Do you clean?

HUSBAND: You do that too.

BERNADETTE: What do you do around here then? Water the plants?

HUSBAND: I usually sit in that brown recliner and flip channels until I fall asleep Then you wake me up when it's time for bed.

BERNADETTE: Wow. It looks like I've won the husband lottery. You can sleep in that chair for all I care.

HUSBAND: Fine.

BERNADETTE: Fine.

HUSBAND: Fine.

BERNADETTE: Fine. (Pause) Was that our first fight?

HUSBAND: No. We have them all the time.

BERNADETTE: What do we fight about?

HUSBAND: Cooking and cleaning.

BERNADETTE: Well, maybe if you'd do it once in a while we wouldn't fight about it. (Pause.) Did I make it to Alaska?

HUSBAND: No.

BERNADETTE: Why not?

HUSBAND: You fell in love with me.

BERNADETTE: Why did I do that?

HUSBAND: You thought I looked like Tom Cruise.

BERNADETTE: Do you?

HUSBAND: Nope.

BERNADETTE: Well that was dumb. Where do we live?

HUSBAND: At the end of a cul-de-sac. In a beige house with a beige garage.

BERNADETTE: Why so much beige?

HUSBAND: Development regulations.

BERNADETTE: I feel dizzy.

HUSBAND: You just had twins.

BERNADETTE: Is that what that was? Huh. I didn't see that one coming.

HUSBAND: You did beautifully. You are beautiful.

BERNADETTE: What are you, trying to get me in the sack again? Geez.

HUSBAND: We have to wait six weeks.

BERNADETTE: Lucky me.

HUSBAND: You have to heal first. There was some tearing of the–

BERNADETTE: Yuck! Alright? Seriously. No need to elaborate.

HUSBAND: (Pulling out some gum.) Gum?

BERNADETTE: How can you think of gum at a time like this?

HUSBAND: I don't know. I just thought -

BERNADETTE: You know what? You can take your gum and your recliner and your babies and just shove them. Alright? This is nuts. You make me sick.

HUSBAND: (Pulling out some Tums.) Tums?

BERNADETTE: What are you, a Duane Reade or something? What the hell else do you have in there?

HUSBAND: (Emptying his pockets.) A toothpick, thirty-two cents, a movie stub from Must Love Dogs -

BERNADETTE: Ugh. Don't you ever wash your pants?

HUSBAND: (Continuing.) My inhaler, a pacifier, three tropical-flavored Starbursts, and a picture of you and the babies. (He eats a Starburst.)

BERNADETTE: Let me see that. (Looking at picture.) Is this them?

HUSBAND: Uh huh.

BERNADETTE: A boy and a girl?

HUSBAND: (Beaming.) Yeah.

BERNADETTE: They're cute.

HUSBAND: They have your eyes.

BERNADETTE: And your weird chin. (He offers her a Starburst.)

BERNADETTE: No thanks. I hate yellow ones.

HUSBAND: What about red?

BERNADETTE: I'll take a red. (Their hands touch.)

HUSBAND: I've missed you.

BERNADETTE: Don't get all sappy on me just because we're sharing a Starburst.

HUSBAND: Will you come home with me?

BERNADETTE: That's crazy. I don't want to think about it.

HUSBAND: Where will you go?

BERNADETTE: Alaska. I'm going to go study the grizzlies. You wouldn't believe what it's like to see one of them up close. I mean, I've never actually seen one up close, except for in a zoo, but I don't really count that because their personalities have been altered by human intervention. Anyway, I'm going to Alaska to study them. I'll be living in a tent for the summer when the bears are in the peak of their activity. Then when they go into hiberna-tion, I'll be compiling all my data.

HUSBAND: What should I do with the babies?

BERNADETTE: I don't know. Give them to someone who wants them. Maybe someone who can't have babies.

HUSBAND: But I love them. I can't just give them away.

BERNADETTE: Well, maybe you should have thought about it before you knocked me up.

HUSBAND: You wanted them.

BERNADETTE: What? That's impossible. Why would I all of a sudden want a litter of babies? That's ridiculous. Ludicrous! Don't you know me at all? Didn't you just hear what I said? I'm going to Alaska! People don't live in tents with babies while closely observing grizzly bears. It's just not safe.

HUSBAND: I'll go with you. We'll live in an RY.

BERNADETTE: Yeah. Maybe we can live in a van and park it down by the river. No. Absolutely not. You're not in the picture, do you understand? Nowhere in this picture, which I am standing in, alone, by myself, is there room for you and your weird chin and all those babies.

HUSBAND: This comes as quite a shock.

BERNADETTE: Yeah, well ... if you have a heart attack over it at least you're with AllState.

HUSBAND: Won't you miss them?

BERNADETTE: I never wanted them.

HUSBAND: That's not true. You said you were ready for a change. You wanted to make a family. You were excited to start a new life.

BERNADETTE: I said all that?

HUSBAND: You did. And you also said you loved me. You said "Life is perfect with you in it." You said that.

BERNADETTE: Maybe I was doped up on NyQuil.

HUSBAND: You meant it when you said it. Anyway, I don't want you to come home with me if you feel this way. I don't want to invade your personal picture or self-portrait or whatever you call it. Good luck. Good luck with your bears. (He kisses her on the cheek. She kisses him back. It becomes something compelling.)

BERNADETTE: You do kinda look like Tom Cruise .

HUSBAND: It's the chin.

BERNADETTE: So long.

HUSBAND: It's not really so much long as –

BERNADETTE: No, I meant, "So long" as in good-bye.

HUSBAND: Oh. OK. Good-bye Bernadette. I'll miss you.

BERNADETTE: Good-bye. (He exits. Bernadette addresses the audience.) You really have to be careful because mother grizzlies will fight to the death for their cubs, ripping the flesh of any animal, no matter how large, if her cubs are threatened. If prematurely separated, her cubs have little to no chance of survival. They usually die either of starvation or in the jaws of a predator. If they do survive, chances are their ability to properly social-ize has been severely disrupted. The mother will often wander aimlessly for days, sometimes even weeks, in search of her lost cubs. She shows outward signs of depression, her shoulders droop, her walk slows, she no longer looms but kind of shuffles along - wandering aimlessly along. She loses her majestic dignity, her confidence, and sometimes even her will to eat. The bond between a mother bear and her cubs is extraordinary. The affection and gentleness she displays with them is one of nature's gorgeous mysteries. (She looks to where he exited. Lights.)
```

---

## IC-0948: What in God’s Name

- Title: What in God’s Name
- Author (byline): Simon Rich
- Work: Not specified
- Publisher: Reagan Arthur/Back Bay Books
- Publication date as stated: Aug 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS, VINCE, GOD, ELIZA, CRAIG, TV ANNOUNCER, BAYNE, NARRATOR 1, NARRATOR 2
- Teaser before the introduction: Yes
- Spoken words (computed): 1238
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
ACTRESS: Welcome to Heaven Inc., the grossly mismanaged corporation in the sky.

ACTOR: For as long as anyone can remember, the founder and CEO (known in some circles at God) has been phoning it in.

ACTRESS: And when he does show up at work, it’s not to resolve wars or end famines, but to Google himself and read what humans have been blogging about him.

ACTOR: Enter Eliza and her mentor, Craig, two underpaid Angels in the lowly Department of Miracles.

ACTRESS: Eliza has just been promoted from the Prayer Department for her innovative method of coding prayers into priority levels –

ACTOR: Level 7 prayers are printed on red paper and routed immediately to God.

ACTRESS: Everything was rolling along quite nicely . . . until today!

TOGETHER: What in God’s Name by Simon Rich
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: ACTOR: God, Craig, Narrator 1 (Closing)

ACTRESS: Vince, Eliza, Narrator 2, TV Announcer, Bayne

VINCE: (Pg 6-7) NFL?

GOD: (closing his eyes and massaging his temples . . . . considering) Packers

VINCE: (writing it down) We’ll make it happen. What about NASCAR?

GOD: I like Trevor Bayne and David Reutimann. (then suddenly pointing at Vince) Hey, how are my numbers?

VINCE: (removing a pie graph from his briefcase) Your numbers are fantastic. Eighty-five percent of humans worship you in some way.

GOD: Outstanding. (Smiling proudly at the chart) Any problem demographics?

VINCE: Some college kids have doubts, but we think they’ll come around. It’s just a phase. (Sighing) We’ll keep working on it.

GOD: (Smiling) All right, then. Let’s play golf!!

ELIZA: (Pg 25 – 27) Hey, can you explain dreams again?

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

ELIZA: (Pg 32 – 41) (reading from the screen) CODE BLACK: Possible tsunami. Potential loss of life. Warn God! (She looks around the empty office, unsure what to do. Finally she sprints toward the elevators) ******

ELIZA: (Eliza shoves open the brass door to God’s office. GOD interrupted in the middle of eating his breakfast, looks up. Eliza speaks resolutely but with a quivering voice) I’m here to tell you about a Code Black? The computer said I should warn you. (God nods and returns to his breakfast) I’m sorry for interrupting, but it said there was a potential loss of life. (God nods and continues eating) If you’re not too busy, I think you should take a look at the tsunami. It seems like a pretty urgent situation.

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

ELIZA: I feel sick . . . (thinking) You know what? I’m going to go back up there! I’m going to tell him to read those prayers. I spent three years sorting them. He doesn’t have to answer them, but the least he can do is read them! ************

NARRATOR 1: (Pg 46- 55) God knew that his obsession with the humans was insane. When he first built the universe, after all, he’d never even intended for it to be populated. He’d constructed the earth for one reason and one reason only: to manufacture xenon gas. But God rapidly grew bored with that side of the business. So one day, for amusement, he’d had his staff invent mankind.

NARRATOR 2: God quickly became preoccupied with the tiny creatures. He began to care about their spots and their wars and their songs and their discoveries. They reminded God of himself.

NARRATOR 1: God thought wistfully about the past. In the beginning, the humans were so easy to please. Give them some fruit, some light, and they’d all be singing his praises. These days nobody said thank you. It made him wonder if his best days were behind him; it made him wonder if it was time to retire.

NARRATOR 2: There was probably a way to fix things, to set the world right. But he was too exhausted to figure it out. *************

ELIZA: (bursting back into God’s office) So you’re just going to play golf!

GOD: (holding his golf bag over his arm; confused) Do you . . . want to come?

ELIZA: Those prayers (pointing to the huge stack of papers in the corner) I sorted them. It took me years to isolate those level sevens, and you’ve probably never even looked at them. (God furrowed his brow, trying to figure out what a #7 was) Look, I know running Earth is hard. But if you’re not going to try to fix things, if you’re not going to really devote yourself to it, what’s the point of being here? What’s the point of even coming to work? Why not just quit? (A eerie silence settles over the room, then slowly God smiles and begins nodding)

GOD: You know what? I’ve been thinking the same thing lately. (Puts down golf bag and yells through the office door) If anyone calls, tell them I’m busy. I’ve got work to do. ************

CRAIG: He canceled golf? (shaking his head in shock and admiration) I can’t believe you just went up there and talked to him.

ELIZA: It was a scary morning. I mean, it’s been five hours and my hands are still shaking! But sometimes, if you really want something, you’ve got to take risks. You know what I mean? (Craig’s computer bings with an incoming e-mail)

CRAIG: (checking his messages) Hey, Eliza! Check your e-mail! ********

GOD: (Reading the e-mail that he has composed) Hey gang, After much consideration I’ve decided to resign as CEO of Heaven Inc. It’s been a fun ride, but part of being successful is knowing when to quit. I want to give a special thanks to Eliza Hunter from the Miracles Department, who really put things into perspective for me. Without her persuasive arguments, I might not have come to this decision:

The earth will be destroyed in a month. The humans of course, will all be killed, so any jobs related to mankind will be eliminated. The planet’s been on a downhill slide for centuries and frankly I think it’s time we cut our losses.

I’m pleased to announce that next month I will finally fulfill my lifelong dream of opening a restaurant. I’m calling it Sola, and we’re going to specialize in Asian- American fusion. ********

CRAIG: Holy shit! Didn’t I tell you not to go up there? Look what happened – look what you did!

ELIZA: (crying) You’re right. It’s all my fault. I was just trying to help the humans. I ended up killing all of them. What are we going to do now?

CLOSING Will Craig and Eliza be able to save the world? Call it divine intervention, call it Karma, heck, call it Bob for all I care . . . . tune in next time to see if the world is still safe!
```

---

## IC-0949: Wheelchair Blues

- Title: Wheelchair Blues
- Author (byline): James I. Schempp
- Work: More One-Act Plays for Acting Students
- Publisher: Meriwether Publishing Company
- Publication date as stated: July 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BARNEY, CHARLOTTE
- Teaser before the introduction: No
- Spoken words (computed): 1912
- Already set (do not supply): none

### Source block (context only)

```text
Author: James I. Schempp
Book: More One-Act Plays for Acting Students
ISBN: 978-1566080873
Publisher: Meriwether Publishing Company
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
CHARLOTTE: Being looked at is not being seen.

BARNEY: Looking at someone is not seeing them.

CHARLOTTE: Sympathy is not understanding.

BARNEY: Feeling sorry for someone is not helping them.

BOTH: “Wheelchair Blues”

BARNEY: By James I. Schempp

(CHARLOTTE WHEELER enters in a wheelchair, which she stops at Center Stage. BARNEY LUFTER enters. He opens the doors of the auditorium to make sure they are functioning properly; the sound of the concert washes over the stage. He closes the doors and approaches CHARLOTTE.)
```

### Performance text (classify this)

```text
BARNEY: Uh, you're not planning to sit here much longer are you?

CHARLOTTE: How was the concert?

BARNEY: Because that probably won't be a very good place to be in about ... (Checks his watch) ten minutes.

CHARLOTTE: I didn't go to the concert because there is a flight of fourteen steps just inside those doors.

BARNEY: The concert will end then and this place is going to be virtually flooded with thousands of wild-eyed teenagers headed for their cars.

CHARLOTTE: They are very pretty stairs. Made out of New Hampshire granite. Did you know that?

BARNEY: (Nodding his head toward the side of the stage) You want to come over there with me, we can watch it together. From a safe place.

CHARLOTTE: Fourteen granite steps. (Pause) You sure of the ending time?

BARNEY: Hm?

CHARLOTTE: You know for sure when it's gonna end?

BARNEY: To the minute. This whole concert is planned to the split-second. Gotta be. You ever seen the lighting effects they use? They gotta know exactly where someone's gonna be every second. Now let's get you out of here.

CHARLOTTE: I haven't seen the special effects. I'm not allowed to see them.

BARNEY: That's too bad. Really neat stuff. The concert started three minutes late, so the final encore will end in exactly... (Consults his watch again) nine minutes and thirty-five seconds.

CHARLOTTE: That long?

BARNEY: (Moving behind chair to push it) It's a big finish, too. The kids get real hyped up and come crashing out of there like a herd of buffalo. So like I said, you better come out of the way or they'll run right over you. (The chair doesn't move.) You got the brakes on or what?

CHARLOTTE: It's broken.

BARNEY: 'Cause this thing ain't moving.

CHARLOTTE: I said, it's broken. I broke it.

BARNEY: Yeah? Where's it broken? Maybe I can put it back together.

CHARLOTTE: I don't think so. It's in the axle itself.

BARNEY: Bad news. (Trying to make it a joke) Now why'd you go and break your chair in a dangerous place like this? You trying to get yourself killed?

CHARLOTTE: (Quietly) Yes.

BARNEY: (Nervous) Yes? What d'ya mean, yes? You didn't break the chair intentionally, did you?

CHARLOTTE: Yes. I did.

BARNEY: Why the hell did you do a thing like that?

CHARLOTTE: (Her anger welling out of her) Because I want someone to say, "Gee, I wonder what she was doing there, because you know she couldn't get into the concert because there is no way to get a wheelchair into that damned auditorium!"

BARNEY: (Examining the chair) Maybe I can fix this.

CHARLOTTE: (Recovering slightly) Did you hear what I said?

BARNEY: Huh? Sure. How'd this get broken?

CHARLOTTE: It's easy. You just take a wrench and grab that little tab, then turn it with all your might and the axle gets jammed and there's no way to fix it and there's no way to move it.

BARNEY: Jeez, lady! This is serious!

CHARLOTTE: (Slowly and with emphasis) I intentionally disabled my wheelchair. (Lighter, to herself) Hey! How about that! Now it's my wheelchair that's handicapped!

BARNEY: I gotta get some help to take care of this. (The noise of the concert is heard again as BARNEY reaches for his walkie-talkie. CHARLOTTE makes a lunge for it and gets it out of his hand. The effort of this pulls her from her chair and she ends up on the ground. She sits and places the walkie-talkie beneath her.)

CHARLOTTE: I don't want it taken care of, damn you!

BARNEY: (Lunging) Hey, give me that radio!

CHARLOTTE: (Pulling a can of Mace from her book bag) Don't touch me!

BARNEY: OK! OK...

CHARLOTTE: This stuff smells terrible and it hurts worse.

BARNEY: I said, OK!

CHARLOTTE: I'll use it if I have to!

BARNEY: I'm not going to touch you, OK?

CHARLOTTE: Stand over there!

BARNEY: Just take it easy. The last thing we need right now is for me to be blind!

CHARLOTTE: Yeah. One handicap is enough, right?

BARNEY: Huh?

CHARLOTTE: Skip it. Will you please go away!

BARNEY: (At the end of his patience) Look, lady! I don't know what your problem is, but you are sitting in the path of several thousand people who are going to start coming through those doors in six minutes and fifteen seconds, and they aren't going to see you sitting there, and even if they did, I very much doubt that they will give a care and you could get hurt real bad. Now will you just calm down and let me take you to a more convenient place.

CHARLOTTE: I don't want to be taken to a more convenient place! That's the point! Please go away!

BARNEY: No, I will not go away. I have a job to do.

CHARLOTTE: Then do it!

BARNEY: That's what I'm trying to do. What are you, some kind of protesting nut?

CHARLOTTE: I am not a protestor. I am not a nut. I am not a "handicapped person." I am Charlotte Wheeler. And I want to be seen. And I want to be recognized as an individual. And if I can't be seen, then I want to do something to make people aware of me, even if I have to trip them up to do it.

BARNEY: OK! OK. I see you! Now let's move it. I have other things to do, other doors to check.

CHARLOTTE: No you don't.

BARNEY: I don't what?

CHARLOTTE: You don't see me.

BARNEY: Lady, believe me, I see you.

CHARLOTTE: Can you see me riding a merry-go-round? I'm sick of places I can't go and cars I can't drive and pay phones I can't reach and toilets I can't get into and classes I can't take, for God's sake, because I can't get up the stairs to the classroom!

BARNEY: Look, you have to get out of the way. In ... (Looks at his watch) four minutes and thirty seconds, those doors are gonna open and you're gonna get trashed!

CHARLOTTE: Nothing new. It happens every day.

BARNEY: (Pause) So you're upset because you can't ride a merry go-round?

CHARLOTTE: That was just an example.

BARNEY: You're really feeling sorry for yourself, aren't you?

CHARLOTTE: Damned right. No one else will do it for me, so I gotta do it myself. (Pause) Look, I was out at the Crossroads Mall this afternoon, and I ...

BARNEY: You what?

CHARLOTTE: Nothing. This is stupid. Will you please leave?

BARNEY: You want to get trampled by a herd of rock fans?

CHARLOTTE: Smart boy! You finally figured that out, did you?

BARNEY: Why?

CHARLOTTE: Because I can only be overlooked for so long. (Turning on BARNEY) Look. (He averts his eyes.) No, I mean look at me!

BARNEY: If you don't ...

CHARLOTTE: Do you know what happens when I roll down the street? People get out of my way, sometimes they open doors for me, but they're always looking three feet over my head! That's where my face would be if I were standing up. When they bother to notice me at all, they talk to me like I'm an idiot! The world is full of schmucks and I am an invisible person! You don't see me, no one sees me! Tonight, when these people come out of the concert, they are going to trample me. And maybe I'll be hurt. Real bad hurt. (Pause) What's the worst thing that could happen to me?

BARNEY: (Quietly) You could get killed.

CHARLOTTE: That's not necessarily bad.

BARNEY: You could get maimed! You could end up ...

CHARLOTTE: In a wheelchair? (BARNEY has nothing to say. He looks at his watch.)

BARNEY: Two and a half minutes. (Pause) You're going to just sit there?

CHARLOTTE: (Quietly) Yes. (Pause) I can't play hackey-sack! I can't play Frisbee!

BARNEY: "I can't, I can't, I can't!" All you do is whine "I can't!"

CHARLOTTE: I went by the pet store. At the mall. (Pause) There was a real cute little Scotty in the window. (Pause) I had a dog. She died.

BARNEY: Look...

CHARLOTTE: Pets are great, y'know? I mean, they don't care if you're sitting down or standing up. All they want is love, and all they give is love.

(Pause, then going on with increasing intensity) And all you have to do is take them for a walk and keep them on a leash so they won't run off into the traffic, but if the leash slips and she runs off anyway, there's no way you can stop her if you can't run ... (She rushes on with the same intensity.) Have you ever seen me before?

BARNEY: We don't have time for this ...

CHARLOTTE: You're Barney Lufter. You're a junior in college. You are a member of Theta Chi. You work weekends as a security guard and you're studying pre-law. You drive a little red Chevrolet and you park it in the library parking lot. (BARNEY is taken by surprise, and for the first time, he looks directly at CHARLOTTE.)

BARNEY: How'd you know all that?

CHARLOTTE: I see you every day. We pass each other all the time between classes. We even had a class together. Intro to Business Law.

BARNEY: Was that you? I didn't recognize you.

CHARLOTTE: Of course you didn't! Until I sat here I was invisible to you. You ignored me.

BARNEY: I wouldn't exactly say I ignored you.

CHARLOTTE: That's exactly what you did! Three weeks ago ... you probably don't even remember, do you?

BARNEY: Remember what?

CHARLOTTE: Nothing. Nothing! I'm just so ... (Collects herself) I made an extra special effort to get your attention three weeks ago. It was a Thursday afternoon. I usually leave campus on a special bus at one o'clock in the afternoon on Thursdays, but I made arrangements to stay late because you were going to present a report in Dr. Lee's symposium.

BARNEY: (Remembering the event) That's right ...

CHARLOTTE: I went to the seminar room. I waited outside for you. I knew just what I was going to say. I had it all set out, starting from the first word. I wore my best ...When you came up I said "Hi..." You just kept walking by. You didn't even acknowledge my existence! I gave it my best shot, I put all I had into that one word, "Hi..." Everything I am was attached to that one word! If you had just picked it up. If you had just responded! All of me would have come along with it. That was the opening gambit! Of course you don't remember! Of course you didn't hear! I wasn't there! You just walked past me because I didn't exist! You never saw me. That was the first time I ever tried, I mean really tried, to get someone to deal with me on a grown-up, real-person basis. I wanted you to look me in the eyes and treat me like I was something other than a poor idiot child! You could have done so much. But I thought, he's probably thinking about his report. I'll wait until afterwards and try again. So I sat at the back of the room. I hung on every word you said. I gave you all my attention. When you finished, I'm the one who started the applause! You came off the podium and everyone was telling you what a great job you did. When you came past me, you looked right at me. I know you did. I waited until I could see your eyes, and I said it again. "Hi... " And you ignored me again. you looked right at me, but you never saw me!

BARNEY: I don't even remember that.

CHARLOTTE: That's the point. (CHARLOTTE stops, bites her lip and stiffens. She cries in spite of herself and tries to keep BARNEY from seeing it. BARNEY considers, then reaches a decision. He sits down beside her.)

BARNEY: Move over.

CHARLOTTE: Will you please go away! It's too late now!

BARNEY: Nope. You're gonna sit here, I'm gonna sit here.

CHARLOTTE: I don't want you here.

BARNEY: I don't want you here!

CHARLOTTE: Why are you trying to take care of me? I don't want you to take care of me. I'm an adult and I can make my own decisions! Now get the hell out of here.

BARNEY: Sorry. If they walk on you, they're gonna have to walk on me too.

CHARLOTTE: You're screwing everything up!

BARNEY: Life is like that sometimes. You get a nice little plan and someone comes along and messes it up. Someone makes you see something or someone refuses to see something or someone gets converted to your point of view. It's a bitch, but it happens.

CHARLOTTE: Why are you doing this?

BARNEY: I'm sharing the experience with you.

CHARLOTTE: Do you know how dumb that sounds?

BARNEY: Sorry.

CHARLOTTE: You might get hurt.

BARNEY: There's a terrific echo around here.

CHARLOTTE: (After a pause) Look. You can avoid this. You can just get up and walk. Now will you please do it?

BARNEY: What's the matter? Can't you take "yes" for an answer?

CHARLOTTE: I...

BARNEY: You win! I'm noticing you! (BARNEY sits in silence as they consider the situation. CHARLOTTE hands the walkie-talkie back to him.)

CHARLOTTE: Here's your radio.

BARNEY: Thanks.

CHARLOTTE: You want to use it?

BARNEY: Too late now.

CHARLOTTE: (Pause) How much time?

BARNEY: Fifteen seconds.

CHARLOTTE: Are you sure you want to do this?

BARNEY: No. (There is another slight pause. Then BARNEY turns to CHARLOTTE and looks her directly in the eyes as he extends his hand.) Hi.

(CHARLOTTE takes his hand and holds it.)

CHARLOTTE: Hi. (The sound of a large crowd is heard approaching the closed doors of the auditorium. The sound suddenly increases as if the doors have been opened like floodgates. The lights fade to black with the crowd noise reaching a crescendo.)
```

---

## IC-0950: Where Have All the Lightning Bugs Gone?

- Title: Where Have All the Lightning Bugs Gone?
- Author (byline): Louis Catron
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 1971
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GIRL, BOY
- Teaser before the introduction: Yes
- Spoken words (computed): 1377
- Already set (do not supply): none

### Source block (context only)

```text
Author: Louis Catron
ISBN: 978-0573625831
Publisher: Samuel French, Inc.
Date (Month/Year): 1971
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Things were so much simpler when we were kids.

ACTRESS: Making friends was a cinch—recess, lunchtime . . . even riding your bike in your own neighborhood.

ACTOR: As you get older, making new friends isn’t as easy!

ACTRESS: But, since maintaining inter-human connections is important,

ACTOR: And you may someday need people to serve as character witnesses

ACTRESS: This selection may be just the guidance you need!

TOGETHER: Where Have All the Lightning Bugs Gone? By Louis Catron
```

### Performance text (classify this)

```text
A Girl is reading a book, with other books on the ground next to her. Boy enters – embarrassed, shy – he tries to catch her eye. No luck. Finally he gets up his nerve to speak to her. But the girl speak first without looking at him.

GIRL: (Very composed) No, I don’t know what time it is. Yes it is a very good book. No, I don’t have a match. And yes, I am waiting for someone.

BOY: (Amazed) What?

GIRL: (Blasé) My boyfriend, who is six foot six. He plays football for the Jets. He weighs over two hundred pounds and this monster will be here any moment. So good-bye.

BOY: Wow! (In awe) You didn’t even look up. How’d you know I was here?

GIRL: (Still engrossed in the book) I’m psychic.

BOY: I mean, this is open range. No fences. So how come you’ve tried to put up barbed wire, partner?

GIRL: (A bit taken aback) Barbed wire?

BOY: You and me, we’re a-gonna have a shoot-out. (He is a cowboy with clanking spurs, a big sombrero and two heavy guns) Ain’t nobody a-goin’ put up no fence nohow on this here range, pardner. No, sir. It’s noon, see, and I’m a-walkin’ down this dusty road right a-toward you. Now. Be you goin’ draw at me? (He tenses) Make your play.

(He draws, get shot, falls) Ahhhh! (Gasps) Got me. (Crawls toward her) I reckon I’m only the West’s . . . second . . . fastest gun.

GIRL: (Laughs) You got what you deserve, cowboy.

BOY: (Dying) I’m a-goin’ fast. But . . . ‘fore I pass on . . . to that . . . great blue range up yonder . . . tell me: What’s the name . . . of . . . that fast gun critter who shot me cold?

GIRL: Kate.

BOY: (Drops cowboy character; sits up) Kate? (Seriously) Kate. That’s a very attractive name. (He suddenly becomes the cowboy again and sprawls to the ground) All right, Kate. You done me in. No hard feelings. (He dies. Motionless)

GIRL: (Mournfully) He’s dead. And I never knew the poor feller’s name. He’ll have an unmarked stone, up there on Boot Hill.

BOY: (Alive; jumps up to his knees) William.

GIRL: (Contemplates the name) William. Will. Willy. Bill. (Sudden insight) Billy the Kid?

BOY: (Drawling) That’s what some folk call me. (Girls suddenly becomes awkward and goes back to reading her book. She turns her body away from the Boy)

GIRL: Okay. That’s enough. (Not looking at him) I knew you were going to ask me a question. Try to talk with me. Start a conversation so you could pick me up.

BOY: (Earnestly) Yeah? (Boy springs to his feet and become a strong man in the circus, flexing his muscles, posing) (In a circus barker’s manner) Yes, sir, ladies and gentlemen, the Strongest Man alive. Watch him pick up that beautiful girl, using only one hand. Come one, come all. Only one thin dime and he’ll show you amazing feats. (Girl laughs – Boy drops strong man character) Kate’s a nice name. (Trying hard to remember; speaking in a Shakespearean tone) They call you Kate that do speak of you? Bonnie Kate, the prettiest Kate in all Christendom?

GIRL: (Impressed) That’s pretty good.

BOY: But what light? ‘Tis the East, and Kate is the sun. (Dropping Shakespearean voice) No, that doesn’t work so well.

GIRL: Do you know Shakespeare?

BOY: Sure. He runs that little pizza parlor on Eighth.

GIRL: (Not laughing) Ho ho ho.

BOY: Do you?

GIRL: (Loftily) Of course. (Impressed with her own intelligence and lifting the book she is reading) This is about him. . . You’ve got a good approach, I’ll say that for you. And I’ve heard a lot of lines, believe me.

BOY: (Mock outrage) Line?

GIRL: Sure (Generously) It’s good. I usually don’t speak to stranger.

BOY: (More outraged) Well, you’re not psychic after all. All that stuff about time, and a book, and a boyfriend. Huh. You were just putting me on. Listen. I wasn’t going to ask you any of those things. What do you think of that?

GIRL: (Kindly) What were you going to say?

BOY: (Becomes TV announcer; microphone in hand) This is your Man on the Street, friends (Big smile which switches on and off) And here I am, out in the park on this beautiful day, talking to Miss Kate Brown.

GIRL: My name isn’t Brown.

BOY: (Ignoring her) As you know, friends out there in wonderful TV land, each day WXX- TV asks the big jackpot question. If Miss Kate Brown knows the answer, she wins our special prize. How about that, Miss Kate Brown?

GIRL: Matter of fact, my name isn’t Kate, either.

BOY: (Dropping character; sotto voice) That’s okay. My name isn’t William. (TV announcer) Now here it comes, Miss Sally Barrows. Are you ready?

GIRL: (A giggling, simpering Southern belle, using a fan) Oh, Ah do declare, Ah gets so fearful in front of that camera that y’all got over there. Ah just know Ah’ll forget.

BOY: The question is – are you ready? -- it is “What ever happened to all the lightning bugs?” You have fifteen seconds, Miss Sally Barrows of Landogoshen, Alabama.

(begins watching the time)

GIRL: Oh, dear, Oh, dear. What’s the question?

BOY: (Pompously) We just asked it, ma’am.

GIRL: Really, Honey, would y’all ask it just one more time? Ah promise to listen real close, heah?

BOY: (Irritated) Are you trying to cheat? We told you: fifteen seconds. Now you’re trying to cheat for more time.

GIRL: (Big business with eyelashes) Honey, Ah never would cheat you.

BOY: (Dropping character; speaking confidentially) I know you wouldn’t. That’s why I wanted to talk to you. (TV announcer again) Well, friends, it looks like this young lady blew it. Bang! This has been your roving reporter, Anthony Knight. Good bye.

(Boy turns to leave)

GIRL: (No longer the Southern belle; a bit offended) I didn’t think that question was so good. Anyhow, I really didn’t hear it.

BOY: (turning around.) That doesn’t make sense. First you said the question was no good. Then you said you didn’t hear it. (Boy has gotten quite close to the Girl, his lips quite close to hers. He now kisses her. Girl seems to respond for an instant Then . . .)

GIRL: Quit that! (Angry) (Boy moves behind her. He is perfectly still, his back toward her) What made you think you could get away with that? You’ve got nerve. (Girl begins to leave. Boy doesn’t speak. Girl becomes more uncertain. She pauses then decides to stay.) (Gently) Please put out your hand. (Boy stretches his hand out slowly behind him, toward her. Girl stretches out her hand. Their fingers touch. They don’t look at each other). Thank you. Look, I don’t want to leave. I want to stay.

BOY: (Facing her) Why’d you do that?

GIRL: (Embarrassed) It’s so hard to talk to people. Touching hands: that helps.

BOY: (Thinking) Maybe that’s why it gets harder. Talking, I mean. When we get older. Remember how we used to play? When we were kids. It was easier then because we didn’t mind touching each other.

GIRL: We didn’t even think about it. Maybe we’d touch, playing some game, and we never thought about what it might mean. Now though . . .

BOY: It was easier.

GIRL: Things get more complicated when you get older. There’s always that suspicion. You know what I mean. All the pawing, grabbing. . . Did you have fun when you were a kid?

BOY: (Reflectively) We used to do a lot of things that I liked. In the evenings, when it was dark, we’d play flashlight hide and seek.

GIRL: So’d we. There’d be a dozen kids from the neighborhood.

BOY: The streetlights were sort of half-hidden by the trees.

GIRL: (Taking up the narrative) And we’d hide. Behind trees. Or under a hedge. And whoever was IT would try to find us. (Takes Boy’s hand and leads him to a hiding place)

BOY: But IT couldn’t find you and me.

GIRL: Because we’d find a place where we both could hide. Together. (Whisper together in their secret hiding place until Boy breaks away)

BOY: Being a kid wasn’t always fun. Someone was always around. An adult, trying to rush us. (He gets up. He is a menacing night watchman with a thick voice) Awright, youse kids. Watcha doin’, lyin’ on the grass like that?

GIRL: (Young, innocent, frightened) Nothin’. Honest, we were just hidin’ here.

BOY: (The watchman) Hidin’? That ain’t what it looks like to me. Whatcha doin’, you there boy? I seen you around before, ain’t I?

GIRL: (Indignant, but still frightened) You leave him alone!

BOY: (The watchman) Go on, boy. You get outta here. I’ll take little Miss Smartie Pants home myself.

GIRL: I’ll tell my father on you! He’s the mayor of this town, and he’ll fix you! So there!

BOY: (Dropping the watchman character and laughing) You really showed him!

GIRL: (She takes boy’s hand and pulls him back down to the ground then continues as if there had been no interruption) We used to catch lightning bugs. Put them in a glass jar. God’s own moon bugs. Do you come here often?

BOY: Never. You?

GIRL: First time.

BOY: It must be Fate.

GIRL: It was that question about fireflies. That really got me. How did you think up that one?

BOY: (Earnest) I’ve always wondered. There used to be so many. And wrens. Other little birds. And butterflies. The big ones.

GIRL: (Shaking her head) What happened to them?

BOY: (Jumps up to become a professor lecturing) Very well, students. Today’s lecture topic concerns the question of the demise of certain small living things. Specifically, the nocturnal soft-bodied beetle.

GIRL: (Taking notes. Raises hand) Professor? Sir, would you be so kind as to spell that?

BOY: B – U – G.

GIRL: (Gushing) Oh, thank you so much, professor.

BOY: (Straightening tie, brushing hair back) Now. This insect is often called a glow worm. But it isn’t a worm, of course. It is called by some, a glow fly. Or a fire fly. This lightning bug has an organ at the tip of the abdomen which produces a soft light, a glow. (Rocking back and forth) Any questions? (Girl raises hand again) Yes?

GIRL: You said you were going to tell us the rationale behind the mysterious disappearance of this lovely insect.

BOY: (Loosening tie) Since my attention is drawn to a carless oversight on my part, allow me to finish. The salient point is that they’re gone. The roses of our summer die. The glowworms of our youth are killed. And how? (Pause, then assuming a poetic air) What is this that thou hast done to innocence? With freeways and speeding cars, thee assassinated the gentle butterfly and the warm glow worm. (Sadly) They fly no more.

GIRL: (Dropping character) Is that what happened?

BOY: (Dropping character) That’s my theory. I used to have a job in a car wash. The front ends smeared with bugs. Never mosquitoes. And not ugly hornets. (Sadly) Only the beautiful things get killed.

GIRL: (Softly) I know.

BOY: Love get killed, not hate.

GIRL: Yes (moves in closer to Boy and takes his hand)

BOY: Nice people, not the other kind.

GIRL: (Sigh) Only the beautiful.

BOY: And the bad thing is that I don’t know what to do about it. (Girl rests her head on Boy’s shoulder as scene ends)
```

---

## IC-0951: Where It Went (from Almost, Maine)

- Title: Where It Went (from Almost, Maine)
- Author (byline): John Cariani
- Work: Almost, Maine
- Publisher: Dramatists Play Service
- Publication date as stated: June 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: PHIL, MARCI
- Teaser before the introduction: Yes
- Spoken words (computed): 1116
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Cariani
Book: Almost, Maine
ISBN: 978-0822221562
Publisher: Dramatists Play Service
Date (Month/Year): June 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: "He is never there for me when I need him the most."

ACTOR: “She’s angry all the time, but she won’t tell me why.”

ACTRESS: "We're like ships passing in the night, he goes his way and I go mine."

ACTOR: When you feel lonely within your marriage, you don’t feel like you’re part of anything bigger than yourself.

ACTRESS: You feel alone, and there is no “we,” only you and your spouse, completely separate entities.

ACTOR: You may or may not seem to be a happy couple to others,

ACTRESS: and you may or may not be able to keep a united front for the kids.

ACTOR: Either way, when it is just you and your spouse talking to each other, you don’t feel close, connected, secure or safe.

ACTRESS: And it starts so slowly that by the time you realize the marriage is in trouble,

ACTOR: the other shoe has already dropped.

TOGETHER: Where It Went from Almost, Main by John Cariani
```

### Performance text (classify this)

```text
Lights up on Phil and Marci, who have just been ice-skating on Echo Pond in Almost, Maine. They are undoing their skates, putting on their boots/shoes. Phil has hockey skates; Marci has figure skates. Marci has one shoe on, one skate on. (Marci should be wearing a winter shoe – like an L.L. Bean hunting shoe, or a suede-like winter shoe – not a boot.)

“// and >” indicates an overlap of lines

.

PHIL: It still feels like you’re mad.

MARCI: (Undoing her skate.) I’m not mad, / / I just said I wish >

PHIL: But you were, you are, >

MARCI: you’d pay more attention lately.

PHIL: you’re mad.

MARCI: I’m not mad! I was having fun, I thought. I had fun tonight. Did you?

PHIL: Yeah.

MARCI: Good. (Smiles, continues to undo her skates; is puzzled by something. Beat.)

PHIL: (Continuing his defense.) I mean, Chad called me in to the mill. I had to work.

MARCI: (Looking for something.) I’m not mad at you, Phil, you had to work, / / I get it.

PHIL: I did!

MARCI: (Now actively looking for something.) Phil, where’s my shoe?

PHIL: What?

MARCI: Where’s my shoe, I can’t find it.

PHIL: Well, it’s gotta be here . . .

MARCI: Where is it?!? (They look for her shoe. Beat.) Is this you being funny?

PHIL: No.

MARCI: ‘Cause it’s not funny. >

PHIL: I –

MARCI: It’s cold out here!

PHIL: Well, you’re the one that wanted to go skating!

MARCI: Phil!

PHIL: (Angry – a bit of an explosion.) We’ll find it! It’s gotta be here! (Beat.)

MARCI: I’m not mad. I was never mad. (Re-lacing her skate – too cold for stocking feet. Beat.) I was disappointed. But now I’m / / done.

PHIL: Marce! –

MARCI: I had fun tonight! Skating! I thought it would be fun!, >

PHIL: It was . . .

MARCI: forget all the . . . stuff. Get us away from the kids, get us back to where we used to be. We went skating . . . first time you kissed me, on a Friday night just like this one. ‘Member? Right here . . . (She touches Phil in some way – maybe rubs his back.) Echo Pond PHIL: (Subtly/subconsciously shaking off Marci’s touch.) I know where we are, where the heck is your shoe? (Going to look for it.) Maybe it’s – maybe it’s in the car. Did you -- . . . Where’d you put your skates on, out here or in the car? (We hear him open the doors and trunk of the car.)

MARCI: (Dealing with the fact that Phil shrugged her off.) I put them on with you. Right here. (Beat. She looks to the sky for answers.)

PHIL: (Returning.) Well, it’s / / not in the car –

MARCI: (She sees a shooting star.) Oh-oh-oh!!! Shooting star, shooting star! (She closes her eyes, and makes a wish.)

PHIL: Wha -- / / Where, where?!? (He looks for it).

MARCI: (Eyes closed.) Shh!! I’m wishing, I’m wishing!

PHIL: (Keeps looking, and then:) Oh, I missed it.

MARCI: (Just looks at him.) Yeah, you did.

PHIL: What’s that supposed to mean?

MARCI: (Finishes re-lacing her skate, eventually gets up to look for her shoe.) Nothing – it’s just . . . not really all that surprising >

PHIL: What?

MARCI: that you didn’t see it.

PHIL: What?

MARCI: The shooting star.

PHIL: Why?

MARCI: You don’t pay attention, Phil. (Beat.)

PHIL: See, when you say things like that, I feel like you’re still mad.

MARCI: I’m not.

PHIL: Marce –

MARCI: I wasn’t mad. (Frustrated about a lot more than her missing shoe.) WHERE is my shoe?!?! Gosh, maybe it is in the car. (Going offstage, to the car, to look for her other shoe.) I mean, >

PHIL: It’s not in the car . . .

MARCI: I have one shoe on already. (From off.) I know I didn’t put my skates on in the car, ‘cause the shoe I have on was out there. I changed out there, didn’t I? With you? Phil? (Phil doesn’t answer. He is trying to sort out what’s going on with him, his wife. He’s sad. From off:) Phil? I put my shoes right next to yours, after we put our skates on, but it’s not . . . there . . . This is the weirdest thing. (Returning.) It’s not in the car, I mean, I’m not gonna put one skate on in the car, the other one on out here – (Sees how sad Phil is.) What’s wrong?

PHIL: (Covering.) Huh? Oh. I’m . . . making a wish of my own. On a regular one.

MARCI: Oh.

PHIL: Wanna wish on it with me?

MARCI: Yeah. Yeah, that’d be nice. Which one?

PHIL: Umm . . . see Hedgehog Mountain?

MARCI: Uh-huh.

PHIL: Straight up, right above it.

MARCI: The bright one?

PHIL: Yeah.

MARCI: That one?

PHIL: Yeah.

MARCI: Right there?

PHIL: Yeah.

MARCI: Phil . . .

PHIL: Yeah?

MARCI: That’s a planet.

PHIL: What?

MARCI: That’s a planet. You’re wishing on a planet.

PHIL: That’s a -- ?

MARCI: Yeah, >

PHIL: Well, how do you know?

MARCI: and it’s (She sings.) “ . . . when you wish upon a star,” not “ . . . when you wish upon a planet / / or Saturn – “

PHIL: I know, I know! How do you know?

MARCI: Said on the weather, Phil. Saturn’s the brightest object in the sky this month. It’ll be sitting right above Hedgehog Mountain over the next bunch of weeks. They’ve been sayin’ it on the weather all week. And your wish is never gonna come true if you’re wishing on a planet.

PHIL: Well –

MARCI: You gotta pay attention.

PHIL: Why do you keep sayin’ that?

MARCI: What?

PHIL: That I gotta pay attention?

MARCI: ‘Cause you don’t.

PHIL: What are you talkin’ about? –

MARCI: Phil . . . Happy Anniversary. (Beat.)

PHIL: Huh?

MARCI: Happy Anniversary. That’s what I’m talkin’ about. (Beat.)

PHIL: I’m -- . (Can’t quite say he’s sorry. Beat. Then, instead of apologizing:) I knew you were mad.

MARCI: I’m not mad, / / Phil!

PHIL: You’re mad at me, and pretty soon, outta nowhere, it’s gonna get ugly. >

MARCI: Phil, I’m not mad, I’m –

PHIL: I mean, Marce: I’m sorry!! I know I missed some things, but I gotta work! I gotta take a double when Chad needs me at the mill! He’s helpin’ me – us – out, you know, / / offering me the overtime!

MARCI: I know, I know –

PHIL: No, you don’t know: Me workin’ is for us, and the kids, and it’s a lot sometimes, and it messes me up!

MARCI: Phil! I’m not mad about you workin’. You gotta work. I understand that. What I don’t understand is why I’m lonely, Phil. I got a husband and a coupla great kids. And I’m lonely. (Beat.) You just -- . . . you don’t pay attention anymore. You go away. And I don’t know where you go, but you go somewhere where you can’t pay attention and you forget your son’s first hockey game and / / you forget Missy’s birthday and >

PHIL: Hockey equipment costs money!

MARCI: you forget your anniversary! I mean, I brought you here hoping you’d remember about us. But you didn’t. And that makes me so mad I don’t know what to do anymore . . . (Beat.)

PHIL: You lie.

MARCI: What?

PHIL: You lie so bad.

MARCI: What?

PHIL: You’re mad at me. But you don’t tell me – even when I ask you over and over –

MARCI: Because you wouldn’t / / pay attention if I did tell you –

PHIL: No! No! No! Because you don’t know how to tell me what you feel like about me, so I never know where I am, where I stand! Maybe that’s why I go away! So I can know where I am for a second! And you know what, it’s lonely there too where I go. And you sent me there. You went away a long time before I did. And now all’s you do is lie.

MARCI: I don’t lie!

PHIL: (Furious.) Yes you do! You say you’re not mad, but you’re mad! You say you have fun, but you didn’t! You didn’t have fun tonight, did you?

MARCI: No.

PHIL: But you kept sayin’ you did.

MARCI: I didn’t. I didn’t have fun, Phil. I don’t have fun with you anymore. (Beat.) Did you?

PHIL: No. I had a rotten, lousy time. (Beat.)

MARCI: Well, then . . . (Little beat.) what are we doin’? What are we waiting for?

(Beat. And then . . . a shoe that looks exactly like Marci’s other shoe drops from the sky, right between Marci and Phil. Beat. Marci and Phil survey the sky, trying to figure out what just happened. Music. Phil retrieves the shoe and gives it to Marci, who puts it on. Marci gets up. She then takes the car keys out of her pocket, exits, and we hear her start the car and drive away. Phil is alone. A shooting star cuts across the night sky on the field of stars. Phil sees it. Lights fade.
```

---

## IC-0952: The Whole Shebang

- Title: The Whole Shebang
- Author (byline): Rich Orloff
- Work: The Best Short Plays 1994-1995
- Publisher: Hal Leonard Corporation
- Publication date as stated: 1995
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DEAN, STUDENT, PROF B, PROF A, HARVEY, EDNA
- Teaser before the introduction: Yes
- Spoken words (computed): 1500
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
ACTOR 1: What if God was one of us?

ACTOR 2: Just a cute little nerd like . . . you. (says to other actor)

ACTOR 1: Or a totally awesome person like . . . YOU. (says to other actor)

ACTOR 2: Yeah? (Preens for the audience)

ACTOR 1: In Rich Orloff’s The Whole Shebang we take a playful look at the creation

ACTOR 2: And evaluation

ACTOR 1: Of earth, humans, and everything in between.

TOGETHER: The Whole Shebang by Rich Orloff
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Throughout the play, switch out gender references to match the gender of the student actor – The script is written to allow the student to be of either gender.

(The STUDENT enters. He/She carries a globe, a briefcase and some papers, etc. He/she
appears very anxious and pressured.)
Actor 1: Dean, Prof A, Harvey
Actor 2: Student, Prof B, Edna

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

DEAN: Thank you. We’ve decided your grade. There is much that is commendable about your project, both in Earth’s evolutionary ability and its astonishing variety of beauty. The human being is wondrous and fascinating. Nevertheless – the human being’s design is tragically flawed. I’m afraid we’re going to have to give you a C plus.

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

## IC-0953: Who’s Afraid of Virginia Woolf?

- Title: Who’s Afraid of Virginia Woolf?
- Author (byline): Edward Albee
- Work: Not specified
- Publisher: Signet Books
- Publication date as stated: Aug 1988
- Event as filed: Duo Interpretation
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
ACTOR: Who's Afraid of Virginia Woolf? explores a marriage steeped in manipulation and emotional abuse.

ACTRESS: George and Martha’s innocent banter quickly pivots to a bitter and venomous exchange.

ACTOR: Especially when the topic of their thinly veiled psychological warfare turns to their son.

ACTRESS: As the truth is revealed, the painful illusions that sustain a toxic relationship are finally exposed.

ACTOR: Can they – can anyone – survive a life built on deception?

TOGETHER: Who’s Afraid of Virginia Woolf by Edward Albee
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

## IC-0954: Widows and Children First!

- Title: Widows and Children First!
- Author (byline): Harvey Fierstein
- Work: Torch Song Trilogy
- Publisher: Samuel French, Inc.
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ARNOLD, MA
- Teaser before the introduction: No
- Spoken words (computed): 2034
- Already set (do not supply): none

### Source block (context only)

```text
Author: Harvey Fierstein
Book: Torch Song Trilogy
ISBN: 978-0573690105
Publisher: Samuel French, Inc.
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Meet Arnold, the gay son of a Jewish mother who is an expert at avoiding the truth.

ACTOR: Arnold and his partner Allen had plans to adopt a son from the foster care system . . . a teen-age boy named David who social services felt would benefit from have two well-adjusted gay parents, to help him deal with his own homosexuality.

ACTRESS: Unfortunately for everyone, Allen did not live to see the adoption through.

ACTOR: And now Arnold’s mother, still grieving the death of her own husband has arrived for a visit.

ACTRESS: The stage is set for . . .

TOGETHER: Widows and Children First! By Harvey Fierstein
```

### Performance text (classify this)

```text
ARNOLD: [Coming out of kitchen and speaking to David (off-stage)] Did your teacher happen to mention how Oscar Wilde came to be imprisoned? He was in jail for being gay.

MA: [Embarrassed] Arnold, I can't find the oil.

ARNOLD: In a minute, Ma. See, ten years earlier, the Parliament passed a law against homosexuality. And Oscar Wilde had this young lover named . .

MA: Arnold, could you please give me a hand?

ARNOLD: Just a second. His name was Lord Alfred. Now, Lord Alfred's father found out about them and started causing scenes in public; chasin' 'em outta hotels and stuff.

MA: For God's sake, Arnold. Could you change the subject?

ARNOLD: [Annoyed] I'll finish later. [Goes back to kitchen] I wish you wouldn't interfere like that; it's very embarrassing.

MA: Excuse me, but listening to that is very embarrassing.

ARNOLD: I'm sorry you feel that way, but I have a responsibility to his education.

MA: I am sure that the people who put him here did not have that kind of education in mind.

ARNOLD: The people who put him here had exactly that kind of education in mind. And I'll thank you not to interfere.

MA: I am only suggesting that you should consider the huge responsibility you've taken on here.

ARNOLD: You think I'm unaware of it?

MA: Then act like it. You should be setting an example for the boy.

ARNOLD: And I'm not?

MA: Not when you talk like that, you're not. You've got to consider what you say to him for the remaining time. He's at an impressionable age. After all it's only for a few more months.

ARNOLD: What's for a few more months?

MA: He's here on a nine-month program, right? And he's already been here six months, so . . .

ARNOLD: And what do you think happens then?

MA: He leaves.

ARNOLD: David is here on a nine-month program, but after that, if we agree and the Bureau of Child Welfare allows, I will legally adopt David. And believe me, Ma, if I have anything to say about it, he's not leaving. [Ma tries to say something, she is angry, confused, frustrated. She throws down whatever is in her hands and sits on couch. Arnold follows and stands staring at her. Sits next to her. Pause] Is this it? We gonna sit and stare into space?

MA: You want I should do a Bubble Dance? Frankly, Arnold, you've done a lot of crazy things, but this . . . ?

ARNOLD: Adopting David is not a crazy thing. It's a wonderful thing that I'm very proud of.

MA: If you're so proud how come you were too ashamed to tell your mother? Everything else you tell me. You shove your sex-life down my throat like aspirin; every hour on the hour. But six months he's been here and not a word. Why?

ARNOLD: Ma . . . Y'know, you're not the easiest person in the world to talk to.

MA: What did I say? Do I tell you how to run your life? You want to know why you didn't tell me about this? I'll tell you why: Because you knew it was wrong.

ARNOLD: That's not true.

MA: No?

ARNOLD: No! This isn't something I decided to do overnight. We put in our application more than two years ago.

MA: Who "we"?

ARNOLD: Alan and I.

MA: The two of you were going to do this together? Now I've heard everything.

ARNOLD: That's what I love about you; you're so open minded.

MA: Alright. So, Alan's not here. Why's the kid?

ARNOLD: Because with everything else I forgot about the application. Then, one day, the phone rang. It was the foster parent program and they had David for us. I told them what happened to Alan and they said I could probably take David anyway.

MA: And you said, "send him on over."

ARNOLD: Not at first. But then I thought it all through, called them back and said yes . . . On a trial basis.

MA: I'm glad you got a money-back guarantee, but you still haven't told me why you wanted him.

ARNOLD: Because I was tired of widowing. Widow-ing . . . feeling sorry for myself, cursing every time I passed a couple walking hand in hand, watching Tear Jerkers on T.V. knowing they could only cheer me up. Christ, of all the things going down here, I was sure that was the one thing I wouldn't have to explain.

MA: How should I know about Wida-whating? Did you ever say a word to me?

ARNOLD: I didn't think I had to. Christ, it's only been three years since daddy died.

MA: Wait, wait, wait, wait, wait. Are you trying to compare my marriage with you and Alan? [Haughty and incensed] Your father and I were married for thirty-five years, had two children and a wonderful life together. What loss did you have? You fooled around with some boy. You have the nerve to compare that to a marriage of thirty-five years?

ARNOLD: You think it doesn't? Ma, I lost someone that I loved very much . . .

MA: So you felt bad. Maybe you cried a little. But what would you know about what I went through? Thirty-five years I lived with that man. He got sick, I brought him to the hospital and you know what they gave me back? A paper bag with his watch, wallet and wedding ring. How could you possibly know what that felt like. It took me two months until I could sleep in our bed alone, a year to learn to say "I"

instead of "we." And you're going to tell me you were "widowing." How dare you!

ARNOLD: You're right, Ma. How dare I. I couldn't possibly know how it feels to pack someone's clothes in plastic bags and watch the garbage pickers carry them away. Or what it feels like to forget and set his place at the table. How about the food that rots in the refrigerator because you forgot how to shop for one? How dare I? Right, Ma? How dare I?

MA: [Starting over his speech and continuing until her exit] May God strike me dead! Whatever I did to my mother to deserve a child speaking to me this way. The disrespect! I only pray that one day you have a son and that he'll talk to you like this. The way you talk to me.

ARNOLD: [Over her speech] Listen, Ma, you had it easy. You have thirty-five years to remember, I have five. You had it easy, Ma. You lost your husband in a nice clean hospital, I lost mine out there. They killed him there on the street. Twenty-three years old laying dead on the street. Killed by a bunch of kids with baseball bats. [Ma has fled the room. Arnold continues to rant.] Children. Children taught by people like you. 'Cause everybody knows that queers don't matter! Queers don't love! And those that do deserve what they get! [He stops, catches his breath, sits down] [Long pause while Arnold composes himself] . . . . Ma, I'm sorry I lost my temper. Please come out here. We can't talk like this.

MA: [In doorway] You don't want to talk, you want to fight.

ARNOLD: You wanna sit down?

MA: [Wandering over to the couch] I'm sitting. [Warning] And don't holler at me. People say things they don't mean when they holler and you've already said quite enough.

ARNOLD: I won't holler. You just hit a raw nerve. We won't discuss Alan. Only David.

MA: So discuss.

ARNOLD: Why don't you tell me what you already know, and we'll go on from there.

MA: Let me think. He's an orphan . . .

ARNOLD: He's not an orphan. He was a battered child. They took him away from his parents. This is his third foster home. The first brought him back. The second he ran away from. So . . .

MA: Arnold, darling, open your eyes. Don't you see how ridiculous this is? I've been here less than a day, already I've seen you let him miss school, hang out on the street, go out without dinner . . .

ARNOLD: This isn't Little Lord Fauntleroy we're talking about here. If this kid decided I was coming down too hard on him, he'd pack and take off and I'd never get him back again.

MA: So you let him run wild?

ARNOLD: No. But I don't beat him up either. I teach him. I advise him, I try to set an example for him . . .

MA: Some example. Arnold, look, you live the life you want. I don't say a word. This is what you want. But think about the boy. He told me he loves you. He sees you living like this . . . don't you think it's going to affect him?

ARNOLD: Ma, David is gay: the whole purpose of placing him here was for him to grow up with a positive attitude about his homosexuality.

MA: That's it. [Stands] I'm finished.

ARNOLD: You think this is easy for me? Look; my hands are shaking. I've been like this for days knowing you'd be coming and we'd have to talk about this.

MA: Because you knew I'd show you how wrong you are.

ARNOLD: I'm not wrong.

MA: No? Tell me something: How old was your friend Alan when you met him?

ARNOLD: Seventeen.

MA: Seventeen. Seventeen and you were doing God knows what together. Now tell me; how old is this "son" of yours?

ARNOLD: I have no intention of sleeping with him if that's what you're driving at.

MA: I had no intention of having a homosexual for a son. So, look where intentions get you. Arnold, do what you want. You want to live like this? I don't care anymore. You're not going to make me sick like you did your father.

ARNOLD: I made my father sick?

MA: No; he was thrilled to have a fairy for a son! You took a lifetime of dreams and threw them back in his face.

ARNOLD: What lifetime of dreams? He knew I was gay for fourteen years.

MA: What? You think you walk into a room, say, "Hi Dad, I'm queer," and that's that? You think that's what we brought you into the world for? Believe me, if I'd known I wouldn't have bothered. Arnold, you're my son, you're a good person, a sensitive person with a heart, like your father, and I try to love you for that and forget this. But you won't let me. You've got to throw me on the ground and rub my face in it. You haven't spoken a sentence since I got here without the word "Gay" in it.

ARNOLD: Because that's what I am. You want a part in my life? I am not going to edit out the things you don't like! There is nothing I need from anyone except love and respect. And anyone who can't give me those two things has no place in my life. [Breath] You are my mother, and I love you. I do. But if you can't respect me . . . Then you've got no business being here.

MA: You want me to leave? I'm leaving. You want me to fight? I'm too tired. You want me to change? I'm too old and I can't. I can't, I can't, I can't. So you do what you have to do, and I'll do what I have to do and I hope you're satisfied. [Arnold groans] You can't put all the blame on me. It's not fair. Your “friend” Alan . . . How was I supposed to know?

ARNOLD: Why? You would have understood?

MA: Maybe. Maybe not. You can't know for sure. But I flew up for the funeral and you never said a word.

ARNOLD: So you could've done what? Tell me he's better off dead?

MA: Or maybe I could've comforted you. Told you what to expect. You and your "widowing." [She turns to leave, stops, takes a breath. One last try.] You've got an unusual way of looking at things, Arnold Beckoff.

ARNOLD: Runs in the family. Ma, I miss him so much.

MA: Give yourself time, Arnold. It gets better. But, Arnold, it won't ever go away. You can work longer hours, adopt a son, fight with me . . . whatever, it'll still be there. It becomes part of you, like wearing a ring or a pair of glasses. You get used to it and it's good . . . because it makes sure you don't forget. You don't want to forget him, do you?

[Arnold shakes his head] So, it's good. [Pause] I guess that's what I would have said . . . if I'd known.
```

---

## IC-0955: The Wizard of Oz: The Screenplay

- Title: The Wizard of Oz: The Screenplay
- Author (byline): Noel Langley, Florence Ryerson and Edgar Allan Woolf
- Work: Not specified
- Publisher: OSP Publishing, Inc.
- Publication date as stated: Jan 1994
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DOROTHY, GLINDA, WITCH, VOICE, SCARECROW, TIN MAN, LAP DISSOLVE TO, LION, OZ'S VOICE
- Teaser before the introduction: Yes
- Spoken words (computed): 2564
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
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actor 1 – Dorothy Actor 2 – All other characters

Tw

SPOKEN BY ACTOR PLAYING DOROTHY: We offer for your viewing pleasure today, our rendition of The Wizard of Oz in less than ten minutes! No, seriously . . . we can do it! We had to leave out a few parts . . . like . . . The munchkins (all those little buggers do is sing!), the poppy field (who wants to watch us sleep?). . . . the flying monkeys (we can flap, but certainly can’t fly) and we had to cut down the Wizard’s long-winded speech toward the end (let’s face it . . . he talked forever!). So . . . . We start our adventure just after Dorothy and Toto make a crash landing in Oz, compliments of Tornado Alley in Kansas! The Wizard of Oz: The Screenplay by Noel Langley, Florence Ryerson and Edgar Allan Woolf.

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

TIN MAN: Perfect? Oh, bang on my chest if you think I'm perfect. Go ahead - bang on it! DOROTHY raps on his chest, which echoes. It's empty. (He looks around, then lowers his voice as telling a terrible secret.) The tinsmith forgot to give me a heart. All hollow! (He bangs on his chest and knocks himself against a tree stump. Dorothy goes to help him, but he holds her off) (singing) When a man's an empty kettle He should be on his mettle And yet, I’m torn apart Just because I'm presumin' That I could be kind-a human If I only had a heart. He goes into a dance. Just as he finishes, the TIN MAN’s joints lock, and DOROTHY comes over to help. The TIN MAN staggers back and lands on a tree stump).

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

DOROTHY: Your Majesty, if you were King. You wouldn’t be afraid of anything?

Supposin’ you met an elephant!

LION: I’d wrap him up in cellophant. How? . . . . Courage! What makes a king out of a slave! . . . Courage! What makes the flag on the mast to wave! . . . Courage! What makes the elephant charge his tusk in the misty mist or the dusky dusk? What makes the muskrat guard his musk? . . . Courage! What have they got that I ain't got?

ALL (DOROTHY): Courage!

LION: You can say that again! Ha, ha - huh? TRANSITION

SPOKEN BY ACTOR PLAYING DOROTHY: Blah, blah, blah . . . sleeping in the poppy field . . . blah, blah, blah . . . And then the quartet of adventurers arrive in Oz and are granted an audience with the Wizard.

(Actor 2 plays Oz’s Voice and should be positioned facing the back of the room directly behind Dorothy, who faces judge)

OZ'S VOICE: I am Oz, the Great and Powerful! Who are you? Who are you?

DOROTHY: I - if you please, I am Dorothy, the Small and Meek. We've come to ask you -

OZ'S VOICE: (booming forth and interrupting) SILENCE! The Great and powerful Oz knows why you have come! Tin Man! You dare to come to me for a heart - do you? You clinking, clanking, collection of junk! And you, Scarecrow, have the effrontery to ask for a brain? You billowing bale of bovine fodder! And you, Lion!

(Actor 2 steps out to play the part of the Lion) The LION groans with fear as he is slowly pushed forward. CLOSE ON LION He begins to speak and faints dead away. (Actor 2 resumes position as Wizard)

DOROTHY: DOROTHY straightens up from LION and turns on WIZARD. (angrily) Oh - oh! You ought to be ashamed of yourself! Frightening him like that, when he came to you for help!

OZ'S VOICE: Silence, whippersnapper! The beneficent Oz has every intention of granting your requests! But first you must prove yourselves worthy by performing a very small task. Bring me the broomstick of the Witch of the West! Now go! TRANSITION

SPOKEN BY ACTOR PLAYING DOROTHY: Piece of cake right? Well, the Wicked Witch had the band of Flying Monkeys, see, who captured Dorothy and Toto, shredded the Scarecrow, beat some major dents into the Tin Man and scared the Lion so bad he wet himself. But through sheer perseverance, loyalty and commitment, the friends make their way to the Witch’s castle to rescue Dorothy. Success! Almost . . . on the way out of the fortress, their great escape goes a bit south!

WITCH: (laughing) Well! Ring-around-the-rosy! A pocketful of spears! Thought you'd be pretty foxy, didn't cha? Well, the last to go will see the first three go before her . . She grins and looks up, then lifts her broom to a burning torch on the wall. How about a little fire, Scarecrow! The WITCH thrusts the blazing broom at the SCARECROW. It sets his arm on fire.

SCARECROW: (jumping up and down) Oh! No! No! (DOROTHY screams) Help! I'm burning! I'm burning! I’m burning. Help! Help! Help! Help! (In defense of the SCARECROW, DOROTHY looks around and suddenly sees a bucket of water.).

WITCH: (screaming) Don't touch that water! DOROTHY flings its contents toward the SCARECROW. The water hits her full in the face and puts out the fire. She screams in agony as she shrinks and shrivels.) Ohhh! You cursed brat! Look what you've done! I'm melting! Melting! You destroy(ed) my beautiful wickedness! Ohhhh – ohhhhhh - ohhhh!

DOROTHY: (looking around at the Witch’s minions, the WINKIES) I didn't mean to kill her - really I didn't . . . it's . . . it's just that he was on fire! (to the leader of the WINKIES) The broom! May we have it? (Accepts the broomstick)

TRANSITION

SPOKEN BY ACTOR PLAYING DOROTHY: And so the band of battle-weary travelers make their way back to the chamber of the Great Oz, who they discover is really a very good man, but a very bad wizard. From a large, black magician’s back, he presents the Scarecrow with a diploma in honor of his brains, a ticking heart-shaped clock for the Tin Man as a symbol of his humanity and he awards the Lion a Triple-Cross Medal for his courage. But for Dorothy . . . who only wants to go home . . .

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

## IC-0956: Wonder On Paper

- Title: Wonder On Paper
- Author (byline): Mary Hall Surface
- Work: 10 by 10
- Publisher: Dramatic Publishing
- Publication date as stated: 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: RUSSELL, SHELLY
- Teaser before the introduction: No
- Spoken words (computed): 975
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mary Hall Surface
Book: 10 by 10
ISBN: 978-1583422410
Publisher: Dramatic Publishing
Date (Month/Year): 2004
```

### Introduction (context only: never use it for content warnings)

```text
When anything can be looked up at a moment’s notice, does it actually have any meaning? To take it a step further, can a child growing up in a fast-paced technology-based world learn to appreciate beauty? The communication divide between those who attempt to find meaning and beauty and those who don’t take the time is shown in Wonder On Paper by Marry Hall Surface.
```

### Performance text (classify this)

```text
RUSSELL: Shel? (Sees her.) Great. Got the right gallery. Thought I’d taken a wrong turn at the sphinx. What’s up with the litter?

SHELLY: (drawing) I’ll pick it up. What time is it?

RUSSELL: (checking the clock on his cell phone) Three o’clock. Exactly. I had my phone alarm programmed to beep in increasingly smaller intervals, with a mounting sense of urgency.

SHELLY: It can do that?

RUSSELL: Man and machine. We can do anything. Come on, we gotta go!

SHELLY: Can’t.

RUSSELL: We promised Dad in blood we’d taxi back to the hotel by 3:30.

SHELLY: Can’t.

RUSSELL: (rapidly picking up SHELLY’s discarded drawings, shoving them into her backpack) Shelly, if we blow this, our vacation is doomed! They won’t let us out of their sight again!

SHELLY: I can’t leave until I draw “beauty.”

RUSSELL: Do what?

SHELLY: “Beauty.” What is it? I want to draw it.

RUSSELL: It’s summer, Shel. Honors art class is over.

SHELLY: This is for me! I’ve spent all day in this museum filled with gorgeous paintings and sculptures that artists have made for thousands of years-

RUSSELL: So draw one of those. (Checking his clock.) Quickly!

SHELLY: But they’re beautiful things-not beauty itself. That’s what I want to capture!

RUSSELL: OK. We’ll look it up.

SHELLY: What?

RUSSELL: (punching keys on his cell phone) Oxford English Dictionary. On-line. Mobile access. Definition: “Beauty.”

SHELLY: Russel-

RUSSELL: Shelly. I have the information. The Knowledge.

SHELLY: You have a cell phone.

RUSSELL: I have the Holy Grail of access, a golden bowl of answers. But I can sign off-

SHELLY: Wait! What does it say?

RUSSELL: (reading from his Web access) “Beauty: A quality that pleases the mind or sense.” There you go. (SHELLY does not move.) So draw!

SHELLY: How do you draw that: a “quality”?

RUSSELL: You’re an artist, Shel. Figure it our or give it up.

SHELLY: Is that your philosophy of life?

RUSSELL: Excuse me?

SHELLY: Anything you can’t figure out, you just don’t think about?

RUSSELL: Yes. Exactly! (Looking at his phone.) Depleting power bar. Now we really have to go.

SHELLY: Look at this statue.

RUSSELL: Shelly-

SHELLY: I need five minutes. Time me!

RUSSELL: (programming the phone) Deal. Four fifty-nine and counting.

SHELLY: (looking at the statue) Do you see?

RUSSELL: (reading the label) “Egyptian. 2500 B.C. Sandstone. Ra, the sun god.” And?

SHELLY: Whoever carved this wanted to know how the sun rises and sets. So he made a god.

RUSSELL: Who sailed in a golden boat across the sky, until sunset. I know all about him. Then he road down into the underworld, and rose again at sunrise. Sunset. Sunrise. But! Science has subsequently explained the actual patterns of the earth’s rotation. So that’s why this statue is no longer worshiped, but sits in a museum. Can we go now?

SHELLY: But did the artist really believe in Ra or was he trying to do what I’m trying to do?

RUSSELL: I’d call this guy “beast” before I’d call him “beauty.”

SHELLY: Stop joking, Russell! Look at this one. She’s Ra’s daughter, Basket.

RUSSELL: Who were the first people to keep cats as pets? (Before SHELLY can answer.) Egyptians! (Congratulating himself.) Score!

SHELLY: She’s a goddess!

RUSSELL: Who had the power to ensure a bountiful harvest. The Egyptians had gods for everything-the sky, the earth, the river. So did the Greeks, the Romans, the Aztecs. It’s Ancient Cultures 101. Myths. Hello?! To explain why things are the way they are.

SHELLY: But why?

RUSSELL: Why what?

SHELLY: Why do we need to know?

RUSSELL: We’re human. We don’t like not knowing.

SHELLY: But what if we can never know some things, but we wonder about them anyway.

RUSSELL: Wonder equals confusion. I don’t like to be confused.

SHELLY: Mysteries. You like reading mysteries.

RUSSELL: Sure, because you always find out who did it at the end.

SHELLY: So because we’re human we take all the big wonders and urn them into stories that we can understand-turn them into statues that look like us?

RUSSELL: (referring to RA) I know I’ve got a bad haircut but I don’t have falcon head and you don’t have cat ears!

SHELLY: But we’ve got arms and legs. Here’s all he mystery of how the sun rises and sets, of how things grow reduced down to figures we can recognize.

RUSSELL: (looking at the statues, dubiously) Well…

SHELLY: OK, almost recognize. They feel so…small for something so big.

RUSSELL: Shel. The ancient Egyptians just didn’t know what we know today.

SHELLY: What do we know?

RUSSELL: Everything.

SHELLY: Beauty…myster…everything?

RUSSELL: Sure.

SHELLY: (looking at her sketch) This drawing’s not working.

RUSSELL: (deliberately) So let’s go!

SHELLY: (flips another page) Tell me how to do it, Russell.

RUSSELL: Me?! (RUSSELL’s cell phone rings.) Got to answer this.

SHELLY: Answer me!

RUSSELL: Text message. Dad! Oh great!

SHELLY: Stop the clock. (SHELLY grabs the phone and crosses away from him.)

RUSSELL: Careful with the technology!

SHELLY: (punching in keys) “Dad. Trying to figure out the mystery of the universe. Might take us a minute. Back soon.” (Pushing the off key.) Off. Here. (SHELLY tosses the cell phone back to RUSSELL.)

RUSSELL: (catching it) Watch it! You want to break it?

SHELLY: You mean your phone god is not indestructible as well as all-knowing?

RUSSELL: I’d sacrifice small mammals to this thing, OK?

SHELLY: I thought you just said we’d evolved since ancient times.

RUSSELL: You have exactly two minutes before we catch a cab.

SHELLY: But you know everything-

RUSSELL: We made a deal!

SHELLY: Don’t you?

RUSSELL: (reactivating the timer) Go! (SHELLY opens her sketchbook again. RUSSELL looks at the statues.)

SHELLY: Look up God.

RUSSELL: Pardon?

SHELLY: On your phone. Get a definition on-line for God.

RUSSELL: That’s too weird.

SHELLY: I’m trying to draw God now.

RUSSELL: What happened to beauty?

SHELLY: Ask it!

RUSSELL: It’s a cell phone. Not an oracle!

SHELLY: It’s all the wonders of the universe smushed into a little black rectangle, isn’t it? Makes the sun rise and set! Worshiped by many, but none more than my brother.

RUSSELL: Oh! You think I’m like the guy who carved these statues-that I’ve made a god out of a thing.

SHELLY: You’ve made a god out of having the answers! Of being so sure of yourself that you’re afraid! Afraid to wonder about a question that might be too big to answer. Here! (Shoving the sketchbook toward him.) You draw beauty…God…everything!

RUSSELL: (snatching the sketchbook) Fine. And I won’t draw my phone!

(RUSSELL sits to draw.)

SHELLY: You’ll draw yourself. (This lands on RUSSELL. He puts the pencil down.)

RUSSELL: (genuinely) Shelly. I don’t know what to draw.

SHELLY: Honest?

RUSSELL: I don’t know, OK? Maybe it’s…impossible. (SHELLY crosses and sits next to her brother. She looks at the sketchbook.)

SHELLY: You did it.

RUSSELL: What? It’s blank. There’s nothing there.

SHELLY: Or everything’s there.

RUSSELL: (liking that idea) Huh. You think?

SHELLY: I wonder!

RUSSELL: (acknowledging his sister) Yes you do.

SHELLY: (realizing the time) We gotta go! (SHELLY quickly gathers her things. RUSSELL stands, too, but is not rushed.)

RUSSELL: See ya, Ra. Bastet.

SHELLY: (to the statues) Guess you’re beautiful pars of a great big whole. You, too, phone. Full of myster and power. Maybe nothing can capture the whole. Maybe we shouldn’t try.

RUSSELL: Wanna walk back?

SHELLY: Really?

RUSSELL: Sure. Lots to wonder at out there.

SHELLY: Yeah.
```

---

## IC-0957: The World According to Toddlers

- Title: The World According to Toddlers
- Author (byline): Shannon Payette Seip and Adrienne Hedger
- Work: Not specified
- Publisher: Andrews McMeel Publishing
- Publication date as stated: 978-1449401207
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS, ACTOR, NARRATOR 1, NARRATOR 2, TODDLER, TOGETHER, JUDY, CHUCK, MOM, TODDLER 2, KATIE, MAGIC EIGHT BALL
- Teaser before the introduction: Yes
- Spoken words (computed): 874
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
ACTRESS: Welcome to the World According to Toddlers

ACTOR: A hilarious, messy (is hit in the face with a spoonful of something; wipes it off) and unpredictable universe.

ACTRESS: The best way to navigate the toddler world? Nobody really knows . . . everyone just makes it up as they go along.

ACTOR: It’s a world where the human who believes he is the boss of you only comes up to your knee.

ACTRESS: A world where food must be cut just so.

ACTOR: A world where throwing a spectacular tantrum is on the daily “TO DO” list

(off-stage scream by actress) Check!

ACTRESS: The World According to Toddlers

ACTOR: by Shannon Payette Seip and Adrienne Hedger
```

### Performance text (classify this)

```text
Suggested Roles: Actors should take turns announcing the title of each “scene” in a broad announcer’s voice!

ACTRESS: Narrator, Judy, Mom (banana pantomime), Toddler 2, Katie

ACTOR: Narrator 2, Toddler, Chuck

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NARRATOR 1: (Pg vii – viii) (cradling an infant in her arms) In the beginning they are babies

NARRATOR 2: Cue the soft music – (sings) Lullaby and goodnight

NARRATOR 1: So cuddly. So sweet. Eating enthusiastically. Playing happily.

NARRATOR 2: Wearing the outfits you choose. Life is good!

NARRATOR 1: Then, around 18 months, the world starts to change. (off-stage shriek by actor – she wrestles with baby as it morphs into a toddler, finally lets it go)

TODDLER: (cross arms and says emphatically) No! No! No! No!

NARRATOR 1: This is when you realize: Your baby is gone and in its place is a boisterous, opinionated human: Your toddler.

TOGETHER: NO!

*****A Major Upset*****

NARRATOR 2: (Pg 8-9) It’s a major upset – a tantrum is brewing. Let’s cut to our commentators, Chuck and Judy, who are live on the scene to give us a play-by-play report

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

NARRATOR 1: (Pg 21) A juice box chilled at exactly 37 degrees.

NARRATOR 2: Hexagonal wheat crackers, arranged in a fan.

NARRATOR 1: Green grapes that are perfectly oblong.

NARRATOR 2: No, it’s not a superstar’s dressing room requirements: it’s the high-maintenance demands of a toddler.

TOGETHER: (Pg 34-35) Snack Time!

JUDY: Chuck, Toddler wants a banana.

CHUCK: Mom has the banana in hand. He’s watching for a sign that it’s OK to peel.

TODDLER: (raising arms and opening and closing fists rapidly, with a low-pitched whine)

JUDY: There’s the sign!

CHUCK: Peeling is underway. She needs to keep this slow and controlled so she can stop at exactly the right point.

JUDY: Chuck, if she peels even a centimeter too much, that banana is ruined. I think we all remember what happened last week, when she pulled the granola bar wrapper down too far.

CHUCK: And let’s not forget the incident with the string cheese wrapper.

JUDY: What about the time Dad handed Toddler a naked banana?

TOGETHER: (Gasp!)

CHUCK: I think we’re getting close . . . close.

MOM: (peeling a banana like she’s diffusing a bomb)

CHUCK: She’s stopping!

TODDLER: (stops screaming suddenly, takes the banana and munches on it)

JUDY: Whew! Right at the perfect point! *****The Social Lives of Toddlers*****

NARRATOR 1: (Pg 41) Peeing in the sandbox.

NARRATOR 2: Though this violation might offend an adult during a social gathering, it’s commonly accepted during a toddler’s playdate.

NARRATOR 1: No feelings hurt.

NARRATOR 2: No friendships destroyed.

NARRATOR 1: Let’s take an inside look at how toddlers play, share

NARRATOR 2: Yeah, right!

TOGETHER: (laughing)

NARRATOR 1: . . . and enjoy the company of others. Come hope in the sandbox!

NARRATOR 2: (pointing) Just watch out for that wet spot.

NARRATOR 1: (Pg 54) [It’s just your average] playdate at the park!

NARRATOR 2: (Pg 94) Don’t forget your blankie, stuffed giraffe, pacifier, snack, pillow, another snack and your favorite socks!

NARRATOR 1: (Pg 100) Understand this: You do not need a stroller. Your mom thinks you still need one, but she is dead wrong!

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

NARRATOR 1: (Pg 136-137) Dear Katie, Thank you for babysitting for us tonight. Here are some notes about putting Bobby to bed. Best of luck!

NARRATOR 2: Bobby needs to be situated at a 30 degree angle to the door.

NARRATOR 1: With his yellow blanket (light yellow, not dark yellow) covering him just up to his chest – one-half centimeter lower than his armpits.

NARRATOR 2: Now sing the ABC song to him.

KATIE: (singing) A, B, C, D, E, F, G . . .

NARRATOR 2: In a British accent!

KATIE: A, B, C, D, E, F, G . . .

NARRATOR 2: When ABC concludes, sing “Twinkle Twinkle Little Star” until he falls asleep or until we get home.

KATIE: (singing) Twinkle Twinkle Little Star

NARRATOR 2: Thank you! We’ll be home VERY late.

TOGETHER: (evil, giddy laughter)

TODDLER: (Pg 139) [Dear Magic Eight Ball], I don’t want to sleep and I’m tired of crying it out. Should I throw up? (shakes magic eight ball)

MAGIC EIGHT BALL: Crying takes too much energy; it’s more effective and expedient to throw up. Chances are very good that “night-night time” will be all done.

TODDLER: (smiles evilly)

KATIE: (singing) . . . How I wonder where you are (continues singing through Toddler’s mime)

TODDLER: (throws up) (Pg 17) Gotta go potty! (makes a grimacing face) It’s coming out!

(pooping his pants. A contented sigh, then stuttering) (Pg 62) You know wha. . You know wha. . . You know wha . . . (Pg 20) I DO IT! I DO IT!
```

---

## IC-0958: Wrong for Each Other

- Title: Wrong for Each Other
- Author (byline): Norm Foster
- Work: Not specified
- Publisher: Theatre Communications Group
- Publication date as stated: May 1997
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: RUDY, NORAH
- Teaser before the introduction: Yes
- Spoken words (computed): 1563
- Already set (do not supply): none

### Source block (context only)

```text
Author: Norm Foster
ISBN: 978-0887545221
Publisher: Theatre Communications Group
Date (Month/Year): May 1997
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: Wrong for Each Other by Norm Foster
```

### Performance text (classify this)

```text
RUDY: (Pg 11-13) Excuse me? Could I borrow this chair? We’re one short.

NORAH: Sure.

RUDY: Thanks.

NORAH: (Recognizing Rudy) Rudy?

RUDY: (Recognizing Norah) Oh, my God, Norah. Hi. What are you doing here?

NORAH: What am I . . . it’s a restaurant. I was hungry.

RUDY: Right . . . of course . . . so was I. (beat) So, how are you?

NORAH: Good, good . . . Would you like to sit down?

RUDY: Oh, no, I don’t want to intrude.

NORAH: You wouldn’t be intruding.

RUDY: You’re sure you don’t mind. (Rudy removes his coat and sits) Wow, it’s been what, four years?

NORAH: Three years and nine months.

RUDY: Thee years

NORAH: And nine months.

RUDY: (Pg 16) Boy, do you believe this? Running into each other. I mean, a city this size. What are the chances? Talk about your small world. (Norah laughs as if at an inside joke) What?

NORAH: Nothing Flashback scene to Rudy and Norah’s 1st meeting

RUDY: (Pg 17-19) Looking for a plant, huh?

NORAH: Yes.

RUDY: Yeah, I’m looking for one too.

NORAH: Well, you’ve come to the right place. (Rolls eyes . . . and is not interested in Rudy’s “pick-up”)

RUDY: (awkward little laugh) Listen, could you tell me something? I’m not plant-friendly . . . is there a traditional gift plant . . . that you’re supposed to give . . . .

NORAH: Well, as far as I know, there’s no standard gift plant.

RUDY: Ah. I see. Good. Good.

NORAH: (after an awkward pause) I mean, a lot of people send roses, but that’s not a plant. If you send them, they say you sent flowers.

RUDY: Right. They don’t open it up and say “oh, look, long-stemmed PLANTS.”

NORAH: Who’s the plant for?

RUDY: (hesitation) My mother . . . . birthday (Obviously lying) (beat, but not wanting to leave) Are you buying a gift too, or . . .

NORAH: No, just something for my apartment.

RUDY: Oh. You live around here?

NORAH: Yes, I just moved in . . . a couple of blocks up.

RUDY: (with way too much enthusiasm) Get out! I live a couple of blocks up! (Norah responds non-verbally) I probably walked right past your place on the way here. Welcome to the neighborhood. I’m Rudy Sorenson. (holds out his hand)

NORAH: Norah Case (They shake hands)

RUDY: It’s nice to meet you, neighbor. (Rudy makes an awkward exit, then spins back to Norah) (Pg 21-22) Could I call you sometime?

NORAH: Call me?

RUDY: Yah, call you. Maybe we could go out or something.

NORAH: On a date, you mean? (She’s been put on the spot and she doesn’t like it) Well, gee, this is . . . I mean. (bluntly) I don’t know you.

RUDY: Well, that’s why we’re going to go out. So you can get to know me.

NORAH: (Pg 24-25) Well, I don’t usually give my umber out to a man, you know, so soon after meeting him. It makes me feel kind of easy.

RUDY: [Well, what if . . . . what if . . . ] You meet back here next week and give it to me then?

NORAH: No, that’s not necessary.

RUDY: OR . . . (very excited at this idea) how about if you give it to me now and I don’t call you until next week? I mean, I might bet busy with work and not be able to call you soon anyway. (During Rudy’s ramble, Norah takes out a pen and paper, writes her number on it) It might not be until next week or maybe even the week after. In fact, I might not call you at all. I might lose the number. I mean, I’m always losing things.

NORAH: Just take the number! Back to present day – at the restaurant

NORAH: (Pg 26) You called me fifteen minutes later!

RUDY: Well, I happened to be near a phone. Flashback to Rudy and Norah’s 1st Date – The Ballgame

RUDY: (Pg 27-29) (Focused intently on the baseball field and players - yelling) Hey! Hey, moron. Yah, I’m talkin’ to you, ump! You wouldn’t know a strike if you were a postal worker! Where’d ya graduate? The University of Ray Charles? Yer a bum!

(Norah is embarrassed and it’s obvious from the look on her face – Rudy notices and tones it down awkwardly) Umpires. They’re all idiots . . .

NORAH: What, you just yell at people you don’t even know?

RUDY: Sure. (Purchases some peanuts from a vendor and eats one) It’s a ball game. You yell at everybody. The umpires, the players, the guy with the peanuts . . . everybody.

NORAH: (Soaks in this new information, stands determined and then points and yells) You slut!

(She is proud of herself)

RUDY: (embarrassed) Whoa, hey! You don’t call the players sluts.

NORAH: I wasn’t. I was talking to that girl down there in the tube top.

RUDY: (interested) Where? Well . . . . Flashback to scene in which RUDY meets NORAH’s father

NORAH: (Pg 69-71) (Norah and Rudy are washing dishes after the evening) Well, that wasn’t so bad. I didn’t want to tell you this before, but I was worried about having my father and you to dinner together. I though that he might not like you. But it wasn’t like that at all. I think you really impressed him.

RUDY: Norah, he threw a dumpling at me.

NORAH: What?

RUDY: He threw a dumpling at me while you were in the kitchen getting dessert.

NORAH: He did not.

RUDY: He did. Hit me right in the neck. You can still see the gravy (touching his neck and licking his fingers)

NORAH: Rudy, don’t kid around.

RUDY: I’m not kidding. It was like he was saying “Stay away from my daughter, or the next time it’ll be a cabbage roll.” And then he kept right on eating, like nothing happened.

NORAH: Damn it. I thought he did like you. I really did . . . Are you sure you didn’t provoke him? (Rudy looks a little guilty) What did you say!

RUDY: I said . . . . I didn’t think I could live with a woman who snores like you do.

NORAH: Oh, great. That’s great. (Pg 72-73) And you’re wondering why he threw a little food at you?

RUDY: (trying to make light of the situation) It was a joke! Ha, ha!

NORAH: Well, that’s a childish attitude, isn’t it. What if your parents didn’t like me?

RUDY: (Trying to keep the conversation light) Well, they wouldn’t throw groceries. I can’t see my mother saying, (in a fake woman’s voice) “Charlie, I don’t like this girl. Pass the squash.”

NORAH: Well, it’s important that my father like you.

RUDY: All I’m saying, Norah, is that if he doesn’t like me, there’s not a whole lot we can do about it.

NORAH: Well, we’d better find something. He’s the only parent I’ve got.

RUDY: (Pg 74-75) (After a moment’s thought) Let’s get married.

NORAH: Are you crazy!?!

RUDY: You know, I think you’ve missed the magnitude of the moment here. I’m proposing to you.

NORAH: I know you are. Now, cut it out. (She gradually realizes that Rudy is serious)

RUDY: You know, all these years, whenever I’ve pictured myself asking a woman to marry me, that’s not the response I imagined. I though either a buoyant “Yes, I’ll marry you,” or a tentative, “This is all so sudden,” but for some reason, “Are you crazy!” never entered my mind.

NORAH: Well, it is crazy. You want me to marry you because my father threw food at you. That’s dumb.

RUDY: That’s not the reason.

NORAH: Well, why then?

RUDY: Because I love you. (Norah has no response, though she struggles to come up with a reply) (Pg 77) Okay, listen, maybe I’d better go. I think I’ve made a fool of myself here.

NORAH: (Pg 78) It was a sweet thing to say though. The love part? It was sweet.

RUDY: Just don’t say it again, right. (Beat. Norah doesn’t answer) Good-bye, Norah.

(Rudy exits) Back to present day – at the restaurant

NORAH: (Pg 39) We didn’t have very much in common, did we? We should’ve seen that. I mean, I liked classical music, and you didn’t

RUDY: I liked baseball

NORAH: And I didn’t know much about it.

RUDY: And I wanted . . . . (stopping)

NORAH: Children Flashback to the day of Norah’s stillbirth

NORAH: (Pg 79-80) (near tears) Rudy? Rudy?

RUDY: I’m right here, Norah. Right here.

NORAH: Rudy, I want to hold her.

RUDY: Norah, you can’t.

NORAH: Rudy, please. I just want to hold her . . . Where is she?

RUDY: (holding back tears) She’s gone.

NORAH: I want her now! You tell them that. I want her right now! (Norah dissolves into her grief) (Rudy exits in tears) Flash-forward to 2 months after Norah’s stillbirth

RUDY: (Pg 89-91) Norah? (beat) Norah, your breakfast is ready. (Norah is non-responsive) Do you wat to eat?

NORAH: (with little affect or with anger) I don’t know. Maybe later.

RUDY: Maybe you should go into work today.

NORAH: No.

RUDY: Sure, get back into a routine. It’ll be good for you.

NORAH: Rudy, I don’t want to!

RUDY: How long can you do this? You haven’t been out in two months. (beat, softens tone) It’ll be good for you. You’ll feel better. I know you will.

NORAH: I will. (beat) . . . soon.

RUDY: How soon? When?

NORAH: (Pg 92) (Angry) When I feel like it.

RUDY: Norah, you’ve got to get over this. It’s done. Let’s move on . . .

NORAH: It’s not as easy for me, Rudy.

RUDY: You get over it. You have to. Otherwise you go crazy.

NORAH: I didn’t even get to see her. That’s what makes it so bad. I didn’t get to hold her.

RUDY: She was gone, Norah. What good would it have done?

NORAH: She should’ve been held by her mother, that’s all. Just once.

RUDY: (Struggles to compose himself) Look, I’ve go to go. (Beat) I might be late. We’ve got a job later in the afternoon, so we might no get out of there until seven or eight. . . . I’ll see you tonight Back to present day – at the restaurant

NORAH: (Pg 93-94) (beat) Is that when it started?

RUDY: Norah, I don’t want to talk about this.

NORAH: Oh, I see. Extenuating circumstances, is that it?

RUDY: We were going through a tough time and I . . . .

NORAH: What? [You were] what?

RUDY: You looked like you were never gonna come out of your depression. I’d never seen you like that. You were always so strong.

NORAH: (through clenched teeth) I’d just lost a baby!

RUDY: I know.

NORAH: I need time, that’s all.

RUDY: You kept saying that. You just needed time.

NORAH: I needed you too, Rudy, and you went off with somebody else.

RUDY: I . . . I . . . I . .

NORAH: You slept with her!

RUDY: Well, I needed somebody too, Norah. You weren’t the only one.

NORAH: (Pg 102) How dare you? How dare you! I fell in love with you, Rudy. Against my better judgment. And then you made me feel like it was okay to want more . . . Marriage, a family.

RUDY: Norah, it was okay to want more. (Pg 107) You deserve more. (Pg 105) I’m sorry. You’re the one for me and I’m the one for you and we should’ve realized it a long time ago. (Pg 106) I’m gonna win you back, Norah.

NORAH: No, you’re not.

RUDY: (Pg 107) And I’ll never lie to you again, and I’ll never cheat on you again, and we’ll be happier than we ever were.

NORAH: (Pg 104) I don’t know what we can say to change it now, Rudy. I wish I did. I wish we could go back.

RUDY: We don’t have to go back. We’ll just start fresh from here.

NORAH: No. I don’t think it’s that easy. At least it shouldn’t be. (Pg 109) I don’t need this. I really don’t. I’m just starting to get things back to normal in my life. Finally after four years. (Pg 104) Goodbye, Rudy.

RUDY: (Pg 111) (defeated) Hey, who knows? Maybe we’ll bump into each other again . . . sometime.

NORAH: I don’t think so. (Norah starts to exit)

RUDY: Yeah, I guess you’re right. A city this size? What are the chances? (Nora turns, then exits)
```

---

## IC-0959: You Can’t Trust the Male

- Title: You Can’t Trust the Male
- Author (byline): Randy Noojin
- Work: The Best American Short Plays 1991-1992
- Publisher: Applause Books
- Publication date as stated: May 2000
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SCENE, HARVEY, LAURA
- Teaser before the introduction: Yes
- Spoken words (computed): 2282
- Already set (do not supply): none

### Source block (context only)

```text
Author: Randy Noojin
Book: The Best American Short Plays 1991-1992
ISBN: 978-1557831132
Publisher: Applause Books
Date (Month/Year): May 2000
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Some crimes are more serious than others. Most people will agree that stealing candy from a grocery store is less serious than robbing a bank. Most people will agree that robbing a bank is less serious than killing someone. But what about stealing someone’s mail . . . that’s no so bad, right?

ACTRESS: Meet Harvey, a painfully shy young mailman, who falls in love-at-first-sight with . .

ACTOR: Laura, a feisty young Brooklyn woman. He's dying to ask her out, but he doesn't know how to begin and then there never seems to be a perfect time and then he doesn't know what to say and then he doesn't want to bother her and then he just plain chickens out.

ACTRESS: Finally, when a card comes through the mail to Laura canceling the first meeting of a night class she's signed up for, SOMEONE decides not to deliver it and goes to meet her there, knowing that he and she will be the only ones to attend.

ACTOR: It all goes to show . . .

TOGETHER: You Can’t Trust the Male by Randy Noojin
```

### Performance text (classify this)

```text
SCENE: A night class room.
HARVEY KESSEL is a man in his mid-thirties and he's sopping wet.
LAURA SPIVEY enters. She's an attractive woman around Harvey’s age. She has an umbrella,
a big bag, a purse and a Beginning Spanish book. She's wet and late.

HARVEY: Hello.

LAURA: Intro to Spanish, right?

HARVEY: Si.

LAURA: Where is everybody? I thought I was late.

HARVEY: I don't know. I just got here.

LAURA: Are we in the right room?

HARVEY: 36A

LAURA: Well, it's five after. We got the right date? [She checks her registration card.]

HARVEY: Friday the sixth. .I wonder where is everybody. [He goes to the door and looks down the hall.]

LAURA: Yeah, this is ridiculous. There was a lady in the office. I'll go check.

HARVEY: We should give 'em a while longer. We're in the right place at the right time.

LAURA: I'll go make sure.

HARVEY: Oh, you know what? Hold on. Lemme check something.

LAURA: I just checked the schedule.

HARVEY: No, I know. This is not the schedule. I know, I did get that too, but this is something else. I didn't really-oh, yeah, here we go. [He finds a postcard in his jacket pocket.] Oh, no. Intro to Spanish is rescheduled for Tuesdays at eight!?

LAURA: What?

HARVEY: I shoulda read this.

LAURA: Lemme see that. I NEVER GOT THIS! Goddamn it! What next?! How come everything is picking now to happen? [She takes his card to her desk and copies the information.] These are the most incompetent, disorganized, stupid bunch I ever had to deal with in my life.

HARVEY: They probably sent you one, it's gonna come tomorrow.

LAURA: Yeah! Tomorrow! Why don't they call us? Would that be brilliant? A mailbox is a wishin' well in Brooklyn.

HARVEY: Well, something's bound to fall through the cracks occasionally.

LAURA: Thanks. They don't need an occasion to *mess* up in Brooklyn. They need a business day.

HARVEY: Well, this time a year, you know. Christmas cards and parcels pouring in. It's a flood.

LAURA: That's exactly why they should call. Everybody knows you can't trust the mail.

HARVEY: Well, it'll get there eventually, I bet, but you're right.

LAURA: What, is your dad a mailman or something?

HARVEY: No, no.

LAURA: Hold it-

HARVEY: He's a mechanic.

LAURA: Oh, my God, I'm sorry.

HARVEY: What?

LAURA: I thought I'd seen you before.

HARVEY: I doubt it.

LAURA: Oh, God. Aren't you my mailman?

HARVEY: Your mailman?!

LAURA: You look just like my mailman.

HARVEY: You're kidding?

LAURA: 294 Vanderbilt Avenue. Fort Greene.

HARVEY: Well, yeah, that's my route. I thought you looked-yeah, I guess maybe that might be it.

LAURA: I'm sorry.

HARVEY: No, no.

LAURA: I wasn't sayin' it was your fault.

HARVEY: No, I know.

LAURA: I didn't mean it was the mailmen. It's the post office probably.

HARVEY: You don't have to apologize. I know you didn't mean anything by it. It's funny. Ha. Forget it. But, yeah, hey, I'm your mailman! Wow! How are ya? Nice to meet ya. I'm Harvey,Harvey Kessel.

LAURA: Laura Spivey.

HARVEY: So we're both taking a Spanish class, huh?

LAURA: Yeah, weird, huh?

HARVEY: Why are you taking Spanish?

LAURA: I'm goin' to Mexico the end of February.

HARVEY: Really? That's great.

LAURA: Yeah, I love the sound of the language.

HARVEY: [In Spanish.] My dog has no nose. How does he smell? Terrible. (Mi perro no tiene ninguna nariz. ¿Cómo él huele? Terrible)

LAURA: Hey, that's pretty good. What did you say? [He resists.] It was dirty?

HARVEY: No. Just . . . My dog has no nose. How does he smell? Terrible.

LAURA: Oh, ya know what? While I got ya here. Well, ifya think about it, could you shove the mail under the grating, that iron door-?

HARVEY: Sure.

LAURA: But only if it hasn't been rainin'. 'Cause the drain clogs.

HARVEY: Be glad to. No problem.

LAURA: Just if ya think about it. That would be great. The kids upstairs, I think, or somebody's been opening my mail. [She gets ready to go]

HARVEY: Oh, no. What makes you think that?

LAURA: Little rips. You know. It's no big deal, it's mostly just a feelin', but if it's no trouble.

HARVEY: Not at all. . . , what're you-? I don't know-you gotta-? I mean, it's early and it's Friday and everything and there's no class now and everything-I don't know. You gotta be somewhere?

LAURA: Yeah, I gotta meet my boyfriend uptown in a minute. You know.

HARVEY: Oh, okay. I was just wondering. Good night then.

LAURA: Or else I would.

HARVEY: No, that's cool.

LAURA: Maybe some other time.

HARVEY: Okay. You go ahead. See ya Tuesday. [LAURA exits. A short beat. She re-enters.]

LAURA: That was a pretty bad lie, wasn't it?

HARVEY: No, no. It was an okay one. [He's getting ready to go.]

LAURA: I mean, it wasn't even logical. I'm here for a two-hour class and now I all of a sudden gotta meet my boyfriend uptown in a minute? Bad lie.

HARVEY: We say whatever.

LAURA: I just wanna set the record straight. I do not have to be anywhere and I definitely do not have a boyfriend. I'm just-I'm a mess. So, believe me you don't wanna have anything to do with me right now.

HARVEY: What's wrong?

LAURA: Ahhh. I recently discovered I almost moved in with a lying *jerk* from hell.

HARVEY: I'm sorry.

LAURA: Yeah, so I'm in a bad mood. But, thanks though. Some other time.

HARVEY: Fine. That's fine. You let me know.

LAURA: Sorry I lied. . I'm not usually like this. I haven't slept. My brain against my will keeps playin' this dirty movie starring this guy and a beach fulla girls who're prettier than me.

HARVEY: Nobody's prettier than you.

LAURA: Oh, please. I'm a wreck.

HARVEY: You'll be fine. It passes eventually, but the only way out is through.

LAURA: I guess.

HARVEY: Oh, and one other thing. Never keep a Dear John letter. My advice is to burn it immediately if you haven't already. How long were you together?

LAURA: Two years.

LAURA: How did you know it was a letter? I never said I got a Dear John letter. How did you know it was a letter?

HARVEY: What was? No, I was just saying about my Dear John--that I burned it.

LAURA: Plus you got this thing that says there's no class tonight, that I didn't get, and you're my mailman. Have you been reading my mail?

HARVEY: What're you talkin' about? I never read your mail. That's a felony! That's crazy. I was just talkin' to ya.

LAURA: Really?

HARVEY: God, you are so paranoid.

LAURA: I KNOW IT! That's exactly why you gotta tell me the truth now. Am I crazy? It's possible. Have I finally gone crazy? I won't be mad. Just tell me.

HARVEY: You're not crazy. Forgive me. I read Alan's last letter.

LAURA: I KNEW IT!

HARVEY: Can I at least explain?

LAURA: Stay away from me.

HARVEY: Oh, Jesus, don't be scared of me. Please don't think I'm dangerous 'cause I'm not. I'm a chicken. If I wasn't a chicken I could just ask a girl out like everybody else seems to be able to do.

LAURA: What?

HARVEY: I'm sorry. Oh, God, what an idiot. I just--I think you are so beautiful. You weaken my knees sometimes you're so beautiful. I swear to God I could faint from you sometimes if I stopped trying not to. And I been trying to think of a way to say something to you since I got your route. But no way seemed like the perfect way and then there was never really a good time and then I didn't want to bother you and then I didn't know what to say and then I got a fever blister and then--I just plain chickened out. I admit it. I'm scared of you. I am. I mean, you think you're scared--oh, boy, oh, boy, oh, boy. Okay. To make a stupid story short, I read your registration stuff for class. I mean, that's not really personal, really.

LAURA: Yeah, it is!

HARVEY: You're right, but it gave me the idea that--maybe we could meet in the class and I could maybe, I don't know--impress you maybe a little.

LAURA: Impress me?

HARVEY: I took two years of Spanish in high school. So I signed up and that was the plan. But then you started getting the airmails from Alan. And I thought for a while he might just be a friend or something but then he drew the little hearts in the corner that one time--

LAURA: I don't believe this.

HARVEY: So I was gonna cancel the class. I sold my book back. I was gonna do my best to just forget the whole thing, but--I was just-curious, I don't know--what kinda love letters a guy who could be with you would have to write--or something like that, I don't know. But what I read was not exactly a love letter.

LAURA: You read my Dear John letter!

HARVEY: Right, so last week when your postponement thing came, I didn't deliver it and I was gonna finally make myself, no matter what, ask you out tonight. I just-I screwed up. I know it was wrong. Everything I do is wrong, but I can't just not do anything anymore. So I just did something, anything, something, I didn't think and I'm sorry but I gotta be glad 'cause it's better at least than what I been doing which is not a thing. But the last thing in the world I wanted was to add to your troubles and I hope you do whatever it takes to make yourself feel better about this. And turn me down if that's what it'll take.

LAURA: You wanted a date?

HARVEY: Don't worry about me.

LAURA: I'm not worried about you.

HARVEY: I invaded your privacy and there's no excuse for that.

LAURA: There's excuses.

HARVEY: You have every right to be furious and it's not good to keep that in.

LAURA: Will ya shut up about it? I can't turn you in.

HARVEY: I don't understand. [Pause.]

LAURA: Well, see-uh-okay, Alan's a SEAL. In the Navy. So sometimes he goes out on these special maneuvers where there's no--whatever, telecommunications or somethin'. Least that's what he told me, and me, like a moron's been lappin' it up the last two years. Who knows what's really the truth, but when he does this we correspond. So he goes out this time and I wrote him and I'm expecting a letter and I'm gettin' nothin', so I figure my mail must be bein' sent to his place.

HARVEY: Why?

LAURA: I was gonna move in with him next month, so I filled out one a those change of address things, but I figured they might coulda started it too soon. You know how they are over there.

HARVEY: You'd be surprised the job we do, but I know what you mean, go on.

LAURA: So I went to his place to see if my mail's in his box-and it's not-but guess what was? [She produces an opened letter.] A love letter from some woman named Brenda. I could not believe it.

HARVEY: Is that Alan's mail?

LAURA: Oh, shut up. You did it too.

HARVEY: Oh, boy, oh, boy.

LAURA: But what burns me is once I read this, I was gonna break it off wi th him. I was so proud a myself. I didn't wanna talk about it. I didn't wanna fight it out. I wrote this- [She shows him a notebook.] -like, what is it, two-and-a-half pages of “Get lost”. I was waitin' to buy a stamp. But I got his Dear John before I could mail him mine.

HARVEY: Is there anything I can do?

LAURA: Nah, nobody can do anything.

HARVEY: I gotta tell ya, it's about all I can do to keep from kissing you right now. [Beat.]

LAURA: What size shoes do you wear?

HARVEY: I know. I got giant feet.

LAURA: Are you a twelve? [She gets shoes from her bag.]

HARVEY: Eleven-and-a-half, twelve. Depends.

LAURA: Try these on.

HARVEY: What're these?

LAURA: They're good shoes.

HARVEY: You don't want 'em?

LAURA: If they fit you, you can have 'em.

HARVEY: These are great.

LAURA: See if they fit. [He tries them on.]

HARVEY: I really love these. They're great. I don't know what to say. This is so nice of you. They fit perfect. Thank you.

LAURA: You're welcome.

HARVEY: How come you don't-oh, these are Alan's shoes!

LAURA: They were gonna be, but not anymore.

HARVEY: I can't take these.

LAURA: No, please, if you like 'em keep 'em. I was gonna throw them off the D train into the river but we went local.

HARVEY: I can't. What if-you know-what if you guys make up?

LAURA: I wouldn't worry about that. They look good on you.

HARVEY: Well, before you start givin' his stuff away-you should probably read this. [He pulls an airmail letter from his notebook.] This came today. [He holds the airmail letter out to her. She just looks at him.]

LAURA: Ya know, if I were you I'd wonder if maybe I shouldn't be a mailman. This came today?

HARVEY: Came and went. [She looks at it a second then holds it out to him.]

LAURA: Take it back. I don't even wanna hear it. I'm never speakin' to him again. I don't care if he begs on his hands and knees.

HARVEY: He does quite a bit of beggin' in there. [She examines the letter for rips.]

LAURA: What, steam?

HARVEY: The laundromat on your corner. There's an exhaust vent.

LAURA: You are so lucky I had a recent fit of snoopiness.

HARVEY: I realize that. And I'm grateful. But that's the end of it. [She opens letter. Reads..]

LAURA: Oh, sweet God. This is a miracle. [Pause. She's in sweet relief] This is-He wants me back. Oh, God- Oh, my God, I can't believe it! It's a miracle. Harvey! A miracle just happened. Listen, could you do me a big favor?

HARVEY: I know, you want the shoes back.

LAURA: No. I want to send this letter back first class. [She writes on envelope.] Return to sender. Address unknown.

HARVEY: Oh, boy, oh, boy, oh, boy. [Pause.]
```

---

## IC-0960: Youngsters

- Title: Youngsters
- Author (byline): Brian Dykstra
- Work: 2006: The Best Ten-Minute Plays for 2 Actors
- Publisher: Smith and Kraus
- Publication date as stated: 978-1575255637
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GORDON, PAULA
- Teaser before the introduction: No
- Spoken words (computed): 1677
- Already set (do not supply): none

### Source block (context only)

```text
Author: Brian Dykstra
Book: 2006: The Best Ten-Minute Plays for 2 Actors
ISBN: 978-1575255637
Publisher: Smith and Kraus
Date (Month/Year): 978-1575255637
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Dear Abby: I'm a 20-year-old junior in college and I've been talking online with my professor a lot. He started hinting that he was interested in me. One day, after class, we kissed and talked about having sex. He says that I'm mature for my age and that we just had an instant connection. If it wasn't for his obligations (he's married and has kids), he said he would marry me. I'm in love with him now. Still, sometimes I think that maybe he's done this kind of thing before or that he will in the future. Is this a mistake?

ACTOR: Youngsters by Brian Dykstra
```

### Performance text (classify this)

```text
Paula sits, waiting and working on some paperwork. Gordon enters, as if looking for Paula.

GORDON: There you are.

PAULA: You mean here in my office?

GORDON: Right.

PAULA: OK.

GORDON: I've come to a decision.

PAULA: Hold on a minute.

GORDON: I've decided.

PAULA: I hear you, but it seems quick.

GORDON: I know what I'm doing.

PAULA: I'm sure you do, but I want you to think about it some more.

GORDON: I don't need to.

PAULA: "Fools rush in ... "

GORDON: Do you somehow know what I've decided?

PAULA: No.

GORDON: Then how do you know I'm rushing in?

PAULA: Are you?

GORDON: ... Not really the point.

PAULA: You're not going to send it.

GORDON: Yes, I am.

PAULA: Why?

GORDON: He can't do what he's doing. It's wrong.

PAULA: Wrong? OK, but what are you hoping to get out of sending it?

GORDON: I'm hoping to right this wrong.

PAULA: Yes, fine, but is there nothing about this that's between you and Peter, something about evening up some kind of score?

GORDON: What are you suggesting?

PAULA: He's a very popular teacher.

GORDON: I'm not that shallow.

PAULA: She's a very fetching girl.

GORDON: What am I hearing?

PAULA: Is there part of you that feels the need to get even?

GORDON: Let me be clear, nothing about this is about vengeance.

PAULA: Vengeance? See, that's a surprise. The word I would have used was revenge.

GORDON: Is there a substantive difference?

PAULA: Not that I'm aware of. Except for the fact the one you chose is traditionally the domain of The Lord.

GORDON: The Lord? We're talking about The Lord now?

PAULA: In this climate, we'd be fools not to.

GORDON: So, what's your point? Are you making some point with that old, "Vengeance is Mine" is that what you're doing?

PAULA: Yes. "Sayeth The Lord." You have some kind of God complex going on I'm not aware of?

GORDON: So, OK, Revenge, then. But, wait, you know what? The truth is, it's not about revenge or vengeance. No, it's about justice.

PAULA: That's what you say. But we both know it's not entirely about justice.

GORDON: We do?

PAULA: Sure. Because you just now committed to revenge after not wanting to commit to vengeance. If it was really about justice, you wouldn't feel the need to make the distinction.

GORDON: Stop talking like I'm a student in one of your classes.

PAULA: Forgive me. Occupational hazard. As you well know. But, I've been thinking about it too, about you sending that letter; and what I've arrived at, is you are not sending that letter.

GORDON: What if I do send it?

PAULA: Then I'm going to show you just how cold revenge can get.

GORDON: Are you threatening me?

PAULA: Am I threatening you? You mean when I said, "I'm going to show you how cold revenge can get?"

GORDON: Yeah. Is that some kind of threat?

PAULA: I hate that question. That's like walking in on a family member, balled up in a corner, bleeding from her ears, rocking back and forth, crying so hard, her clothes are wet. You go over, concerned, you lean down, put your hand on her shoulder and ask gently, "Are you OK?" But it's a stupid question, isn't it? Of course she's not OK. Any idiot can see she's not OK. So, let me frame in your question for you, "Am I threatening you?"

GORDON: Of course you are.

PAULA: Of course I am. You know how we could tell? It was when I said, "I'm going to show you how cold revenge can get." See, how could that be anything but a threat? I mean, really now, in what context could that possibly be construed as not a threat?

GORDON: So I guess my question is, why are you threatening me?

PAULA: Why do you want to send that letter?

GORDON: It's a fundamental transgression. It's clearly wrong. It's so clearly wrong, it's punishable by dismissal, and there's good reason for that. Teachers sleeping with students, what is she, twenty? If that?

PAULA: Just a poor little lamb.

GORDON: It is clearly a violation of the trust she is required to put in her teacher.

PAULA: That big bad wolf.

GORDON: He's taken advantage of that trust.

PAULA: Blah, blah, blah.

GORDON: He has!

PAULA: So, what?

GORDON: So what? What do you mean, so what? We're watching a girl, a child, get put through the kind of emotional ringer that not only isn't fair to her, it might really be damaging.

PAULA: And, what, it takes a village to raise this child?

GORDON: Why are you being -

PAULA: And you're the self-appointed sheriff of all that is moral in our little village?

GORDON: Why this cavalier? You know I'm right.

PAULA: Why did you let it go on so long? Sheriff. You knew he was seeing this girl socially. It wasn't like they were being all that discreet. Why did you let it go on?

GORDON: I thought it was none of my business.

PAULA: What changed?

GORDON: She's in love with him.

PAULA: And?

GORDON: You see that, right?

PAULA: I do.

GORDON: So, something needs to be done.

PAULA: Not what you propose.

GORDON: Why not?

PAULA: Because if you send that letter, I'm going to hear about it. And when I hear about it, I'm going to compose a remarkably similar letter. But the subject of my letter will be you. I will accuse you, in my letter of having an affair with a student here. But, unlike you, I will sign my name to it and I will stand by it, after I send a copy to your wife.

GORDON: Why would you do that? It's not even true.

PAULA: Will your wife know it isn't true?

GORDON: Yes.

PAULA: How?

GORDON: ... OK, so she won't. Why would you do that?

PAULA: Because she won't know it isn't true. How could she? None of our spouses would. That's the position we're in. All of us. That's how precarious our jobs are. We work with these children, and I take offense at that characterization, children, my ass. These kids don't know what they're doing when they crawl into the sack with a teacher? Please.

GORDON: This one's in over her head.

PAULA: And I feel for the girl. I do. It's sad. So she'll work through her daddy complex, get a better grade than she deserves, and chalk it up to her first tragic affair. If she's lucky, it might even make her a better writer. I've read her work, it couldn't hurt.

GORDON: That's really the way you want to say that?

PAULA: What position would you have me take? You want to make this a thing? There are hundreds of students coming through here every year. You really feel that secure you're not going to meet one down the road who pushes all your buttons?

GORDON: Of course not! You mean have an affair with a student? Of course not!

PAULA: If your letter gets sent, and Pete gets dismissed because of it, you will have demonstrated to these children just how much power they possess. Even if he doesn't get dismissed. These students will realize an anonymous letter accusing a teacher of marital infidelity, or of seducing (or being seduced) by a student throws this administration into a tizzy. You think we won't have to deal with a spate of accusations that might touch any one of us?

GORDON: You're having one, too.

PAULA: Don't be ridiculous.

GORDON: But you've had one?

PAULA: Who hasn't?

GORDON: I haven't.

PAULA: You're young yet, give yourself another semester. And so what? It's the pitiful, worst-kept secret of higher education. Hopefully higher education. And, I'm saying we're all at risk. Even you. Even if you're innocent. The rule exists so that if a student wants to bring charges herself, she (or he) has a viable option. But they have to bring it on themselves. The scrutiny, the questions, the innuendo, the public humiliation of having accused, they have to deal with the fallout themselves.

GORDON: So, the victim gets the blame?

PAULA: Victim? No. Other students need to see it's nothing to trifle with. Your letter outs this kid against her will and other students who are in some post teenage competition for the attention of a part-time adjunct, figure out how to get rid of that competition by sending letters accusing all kinds of things. The whole cachet of sexual harassment has finally, mercifully faded a bit. Let's not revisit it. Let's not turn this girl into the first lem-ming in line.

GORDON: Who are you protecting?

PAULA: You. Obviously. Me. The rest of the faculty. All of us.

GORDON: And this girl?

PAULA: It's a dalliance with a teacher. She's in over her head. Hopefully, she'll drag Peter into some emotional disaster, as well. Hopefully there will be some cost to him for his behavior. Hopefully, when some dark-eyed beauty comes along who reminds you of your first crush, you'll remember how you made room for a fellow teacher a few years back, and hope precedent makes room for you, so some spiteful sculptured prick doesn't put you through the kind of humiliating question & answer -! ... And ... Perhaps, I've said too much. If you do the research, you will find a slight bump in the road of my ivory tower career that lands me at this liberal arts institution at this stage in my life, rather than the slightly more elevated position I had envisioned for myself And, that being the case, let's be honest, these empty-headed children of leisure who kill brain cells with ecstasy and hip-hop while dressing like whores and desperately search for husbands rather than educations, what's the only thing most of them are good for if not the occasional roll in the hay?

GORDON: Are you serious?

PAULA: How could I be? You want revenge, look for it somewhere else.

GORDON: I don't want revenge.

PAULA: Good. That's safer. Cleaner. Don't want revenge. Look what happens to a person when you do.

GORDON: ... This is someone different.

PAULA: And your point.

GORDON: ... What do you have against her?

PAULA: Specifically? I don't know. I suppose I'm aghast she had the bad taste to choose Peter. As for the rest of them: Now that I'm to live out my days at a second-tier educational institution nowhere near a population center that supports world-class culture or art, not enough of these frat boys want me, anymore. That's what I have against her. But, not to worry. I'm sure I'll get over it.

(Gordon lingers a moment. Paula gets back to work. Gordon leaves the room. Paula doesn't even look up. She just continues working.)
```
