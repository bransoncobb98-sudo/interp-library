# Classification request: batch 15 of 63 (40 records, IC-0561 to IC-0600)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-015-reply.json`.

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

## IC-0561: Beauty Queens

- Title: Beauty Queens
- Author (byline): Libba Bray
- Work: Not specified
- Publisher: Scholastic Paperbacks
- Publication date as stated: June 2012
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR 1, NARRATOR 2, MARY LOU, ADINA, TAYLOR, GIRL #1, MISS NEW MEXICO, TIARA, BRITTANI, NICOLE, MISS MONTANA, PETRA, BOSS, AGENT
- Teaser before the introduction: Yes
- Spoken words (computed): 1366
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
ACTRESS 1: The fifty contestants in the Miss Teen Dream Pageant thought this was going to be a fun trip to the beach,

ACTRESS 2: Where they could parade in their state-appropriate costumes and compete in front of the cameras.

ACTRESS 1: But sadly, their airplane had another idea, crashing on a desert island and leaving the survivors stranded with little food,

ACTRESS 2: Little water,

ACTRESS 1: And practically no eyeliner!

ACTRESS 2: What's a beauty queen to do?

ACTRESS 1: Continue to practice for the talent portion of the program –

ACTRESS 2: Or wrestle snakes to the ground?

ACTRESS 1: Welcome to the heart of non-exfoliated darkness.

TOGETHER: Beauty Queens by Libba Bray
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

SUGGESTED ROLES

Actress 1: Narrator 1, Mary Lou / Miss Nebraska, Taylor / Miss Texas, Tiara / Miss Mississippi, Agent

Actress 2: Narrator 2, Adina / Miss New Hampshire, Girl #1, Miss New Mexico, Brittani / Miss Alabama, Nicole / Miss Colorado, Miss Montana (no lines), Petra, Boss *****

NARRATOR 1: This [story] begins with a plane crash.

NARRATOR 2: According to the U.S. Department of Unnecessary Statistics, your chances of dying in a plane crash are one in half a million. Whereas your chances of losing your bathing suit bottoms to a strong tide are two to one. So, all in all, it’s safer to fly than to go to the beach.

NARRATOR 1: As we said, this [story] begins with a plane crash. But there are survivors. They are all beauty queen contestants.

NARRATOR 2: They are all such nice, happy, shining, patriotic girls who happen to have interests in baton twirling, sign language, AIDS prevention in the animal population, feminine firearms, interpretive dance, and sequins.

NARRATOR 1: The flight is on its way to a remote tropical paradise where the girls will compete against one another for the title of Miss Teen Dream. And so our tale begins with a sudden fall from blue skies, with screams and prayers . . .

NARRATOR 2: . . . and a camera crew bravely recording every bit of the turbulence and drama: What a lucky break for their show! Ratings will skyrocket!

NARRATOR 1: Through the windows, they can see the strange, verdant land taking shape, growing bigger as they descend.

NARRATOR 2: It’s beautiful. They will land safely, no matter the sudden near-vertical descent. They’re sure of it. After all, these are can-do girls from a nation built upon dreams. (Chapter 1)

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

TAYLOR: All righty, then. Let’s put it to a vote! All y’all who want to vote for me, Taylor Rene Krystal Hawkins of the Lone Star State, raise your hands. Looks like I’m the winner. (Chapter 4) Teen Dream Misses! My daddy is a general, and I know what he’d say if he were here: (points to jungle) There might be more of us in there. We need to organize a search party. A Miss Teen Dream Recon Machine. (Chapter 2) *********

NARRATOR 1: Two teams were organized and, after much debate, names were chosen:

NARRATOR 2: The Sparkle Ponies would stay on the beach, tend to the wounded, and try to salvage whatever they could from the wreckage.

NARRATOR 1: The Lost Girls would soldier into the jungle in the hopes of finding survivors. (Chapter 2)

NARRATOR 2: The Lost Girls set off down the beach. Taylor led the way. Adina, Petra, Mary Lou and Tiara followed.

NARRATOR 1: The jungle gave way to a small clearing. Enormous totems rose next to the trees. With their angry mouths, jagged teeth, and blood-red, pupilless eyes, they were clearly meant to frighten. *********

MARY LOU: Holy moly . . . You think there might be cannibals here? (They hear something from the jungle)

TAYLOR: Grab whatever you can. Follow my lead. (Taylor holds up 3 fingers, counting down to 1) Now! (Girls launch sticks and rocks at the jungle. Hiss of pain from jungle) Lost Girls, hold your fire.

NARRATOR 2: A willowy girl stepped out into the open, moaning. Her skin was the same deep brown as the carved figures.

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

NARRATOR 1: CLASSIFIED. ISLAND. 22:00 Hours . . .

NARRATOR 2: Sheltered by the dark, the agent watched the girls sleeping on the beach and shook his head. This was not good, not at all. (Picks up phone and dials) *********

BOSS: This better be good.

AGENT: We’ve got a problem.

BOSS: Agent Jones, in six weeks, Operation Peacock is a go. Nothing can interfere. Nothing. A rescue mission to the island will mean attention. We don’t want attention.

AGENT: I understand. What about the girls?

BOSS: Six weeks is a long time, Agent. And it’s a hostile island. They’ll be lucky to last two days. The official word is that there were no survivors. Operation Peacock goes on as scheduled. (Chapter 5)
```

---

## IC-0562: Between the Lines

- Title: Between the Lines
- Author (byline): James Still
- Work: Scenes and Monologues for Young Actors
- Publisher: Dramatic Publishing
- Publication date as stated: 2000
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JENNY, RAN
- Teaser before the introduction: Yes
- Spoken words (computed): 947
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Still
Book: Scenes and Monologues for Young Actors
ISBN: 0871299585
Publisher: Dramatic Publishing
Date(Month/Year): 2000
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Dealing with an older sibling leaving for college, can be a difficult adjustment.

ACTRESS 2: The experts say to skip the whole act where you pretend that you "don't care" about where they're going and that you won't say goodbye. Truth is: you're in denial.

ACTRESS 1: You don't want to admit that life as you know it is about to end.

ACTRESS 2: You should realize that your sibling, while definitely excited to embark on this new adventure, is probably really scared and could definitely use your support.

ACTRESS 1: The worst thing you could do is pretend that you don't care because they might think that you don't care about them.

TOGETHER: It’s hard for everyone to read Between the Lines by James Still
```

### Performance text (classify this)

```text
Jenny: Almost 18 Ran: Her sister, 14 (or younger).

At Rise: Jenny looks around the room, distracted. She packs a couple of suitcases, rolls up posters, chooses CDs. There’s a knock at the door.

JENNY: Yeah?

RAN: Jenny? It’s me.

JENNY: Hi, me (Continues packing. She looks over at the closed door.) Ran? What are you doing?

RAN: Nothing.

JENNY: Then stop spying on me and com in.

RAN: Okay. (Ran comes in the room, plops on the bed)

JENNY: Why are you being so weird?

RAN: I’m not being weird. And I wasn’t spying.

JENNY: Okay.

RAN: What are you doing?

JENNY: What does it look like I’m doing? I’m packing.

RAN: Oh.

JENNY: And I don’t need any help, because I’m almost finished.

RAN: That’s good, because I wasn’t planning on helping. (Beat) Are you nervous?

JENNY: No. Are you?

RAN: Why should I be nervous? You’re the one who’s leaving. I’m the one who’s staying.

JENNY: Maybe that’s why you’re nervous

RAN: I’m not nervous.

JENNY: Then stop tapping your foot. (Ran looks at her foot unconsciously tapping the floor. She stops tapping). Think you’re going to miss me? (Ran doesn’t answer. Jenny looks at her, smiles, lets it pass.) I found a book that was due six months ago. It was under my bed next to a piece of pizza that looked like a dead animal.

RAN: Gross.

JENNY: It still tasted pretty good. (Ran looks at Jenny, horrified. Jenny laughs loud). Gotcha! (beat)

RAN: What do you think it’ll be like?

JENNY: What?

RAN: College.

JENNY: How should I know? I’ve never been to college. (Ran starts tapping her foot again. Jenny walks over and puts her hand on her foot to stop it from tapping.) It’ll probably be like high school – only harder.

RAN: And more fun.

JENNY: Hopefully.

RAN: What if you don’t like your roommate?

JENNY: I don’t know. But after sharing this room with you for most of my life, I think I’m ready for anything.

RAN: Am I really that bad?

JENNY: The best.

RAN: The best?

JENNY: The best at being bad.

RAN: The best at being bad. I like that. (Beat) Remember when I brought that tarantula home?

JENNY: The one you named “Kevin”?

RAN: Right. He just looked like a Kevin, you know?

JENNY: He just looked like a big, hairy, poisonous spider, you know?

RAN: Kinda like that guy you had a crush on in tenth grade. (Beat) I’m not going to miss you, Jenny. But if I did, it would be awful. I mean, what if you left and I felt really, really bad and I couldn’t stand the idea of not sharing a room with you, of not talking to you late at night when Mom and Dad thought we were asleep . . . of not having somebody . . . (her voice trails off).

JENNY: Com on, Ran, how many times have you wished you could have this room all to yourself?

RAN: Six thousand two hundred and eighty-six times. At least.

JENNY: Well . . . careful what you wish for.

RAN: Remember when you used to lock me out –

JENNY: And you’d climb on the roof –

RAN: And come in through the window –

JENNY: Wearing a mask that looked like the pope.

RAN: I think I had green hair then too.

JENNY: Oh yeah – Ran’s Green Hair.

RAN: I liked it.

JENNY: I know you did. But sometimes I’d wake up in the middle of the night because a bright light was shining in my eyes. Only it turned out to be your neon green hair glowing in the dark.

RAN: My green hair glowed in the dark? Cool. (Beat) Maybe I’ll paint the walls black. After you’re gone.

JENNY: Why?

RAN: Why not? (Jenny laughs) What’s so funny?

JENNY: We’re really different, you know?

RAN: Remember when you had me convinced that I was adopted?

JENNY: It was a joke!

RAN: I know, but I believed you. And so I started asking everybody in town if they knew who my real parents were. I went right up to the Methodist minister and said, “Are you my father?”

JENNY: I thought Mom was going to die of embarrassment.

RAN: Well, they never had the blood tests. Who knows? Maybe it’s true.

JENNY: No way. You’re definitely my sister.

RAN: Why?

JENNY: I don’t know. It’s just something you know. It’s something you can feel. It’s like you share something – even though you don’t know what it is. It’s just something inside, you know? Something that feels . . . connected.

RAN: Connected to what?

JENNY: Ran!

RAN: I’m just trying to understand what you’re talking about.

JENNY: Forget it.

RAN: Are you mad at me?

JENNY: Do you want me to be?

RAN: What is that supposed to mean?

JENNY: Oh come on, Ran. You always act so tough, it’s like you’re daring me to be mean or something. And now I’m moving away and going to college – and I think you want me to be mean so you can be made at me.

RAN: Whatever.

JENNY: Because it’s a lot easier not to miss somebody if you’re mad at them.

RAN: (Angry) I am not mad at you!

JENNY: (Stares at Ran.) Okay. (Picks up an old stuffed animal and looks at it tenderly.) Do you want this?

RAN: You don’t want it?

JENNY: I thought you liked it.

RAN: I used to. When I was like, six. (A horn honks off-stage).

JENNY: I guess Dad is ready to go.

RAN: Either that or he’s just checking to make sure the horn still works. (Beat)

JENNY: You could still come, you know.

RAN: (Thinks about it) No. It’s your day. Besides, I hate it when Mom cries.

JENNY: Do you think she’s going to cry?

RAN: Duh. I heard her crying last night. She’s going to really really miss you. (Beat)

JENNY: So

RAN: So this is it. You’re shipping out. College girl.

JENNY: Woman

RAN: Whatever

JENNY: (Taking a look around the room.) Are you really going to paint the room black after I’m gone?

RAN: No.

JENNY: Good

RAN: I’m going to paint it hot pink. With psychedelic murals on every wall. And on the ceiling, I’m going to paint the solar system. All the planets and all the moons and all the stars. And if I’m in the mood, I’ll paint some extra planets and give them names like “Popcorn” and “secrets” and . . . “Jenny.”

JENNY: Okay. (She reaches out to give Ran a hug and Ran slips away and starts circling Jenny). What are you doing?

RAN: I’m a moon. Orbiting around Planet Jenny. I’m an asteroid! (She crashed into Jenny and manages to turn it into an awkward hug. Ran doesn’t want to let go.)

JENNY: You’re a nut.

RAN: Does that mean you’re not going to go?

JENNY: Ran . . .

RAN: You could stay. I could bring you food, you could write all my papers and do my homework for me. I’ll keep my side of the room spotless. . . (The horn honks again. Ran finally lets go of Jenny. Jenny picks up the stuffed animal and gives it to Ran)

JENNY: Look after him for me. (To the stuffed animal) You’re going to miss me, aren’t you? I hope somebody does. (She grabs her suitcases and exits the room. Ran cradles the animal)

RAN: (To herself) Somebody does.
```

---

## IC-0563: The Big House

- Title: The Big House
- Author (byline): Ira Brodsky and Barbara Lhota
- Work: 35 Original Comedic Plays for tow Females (Forensic Duo Series) Volume 3
- Publisher: Smith and Kraus
- Publication date as stated: September 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CLAIRE, ELISA
- Teaser before the introduction: No
- Spoken words (computed): 1894
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ira Brodsky and Barbara Lhota
Book: 35 Original Comedic Plays for tow Females (Forensic Duo Series) Volume 3
ISBN: 1575253801
Publisher: Smith and Kraus
Date (Month/Year): September 2004
```

### Introduction (context only: never use it for content warnings)

```text
CLAIRE: Elisa, a sweet girl from Utah and a big fan of reality TV, has submitted an audition video for an upcoming reality TV show that I am co-producing. Elisa's tape has passed through to the final round.

ELISA: Today, Claire has invited all the finalists in for an interview. Claire's goal is to determine which applicants are the right fit for the show's premise and will represent the right demographic in the total chemistry of the show.

CLAIRE: When you are a Reality TV Star, you have to be versatile. Will Elisa pass the test? TOGETHER: The Big House by Ira Brodsky and Barbara Lhota.
```

### Performance text (classify this)

```text
CLAIRE: OK, first things first. (Putting out her hand.) Claire Handal! I'm the producer of this new reality show we're developing for CBS.

ELISA: I'm so excited, Ms. Handal!

CLAIRE: Claire, please. I understand. This is very exciting, but this is not the end of the process. You are a finalist, but you're not a house guest. Yet. So where are you from again, Elisa?

ELISA: I live in Ogden, Utah, where nothing ever happens! At least nothing exciting.

CLAIRE: Well, I'm sure that's an exaggeration. I mean, exciting things happen everywhere. So how did you hear about us?

ELISA: Well, my friend Monica Evans from college. We were reading the recap of the rat pit on the Web site of Fear, Fear, Fear and we saw the advertisement for house guests and (Claps her hand.) wham I sent in a video. And wham I'm here. I love all of those shows: Loser Love Island, Phobia, Stamina, Let's Get Divorced. They're all so fun!

CLAIRE: Yes, they are, Elisa. Nothing more fun than watching your fellow man get tortured, taunted, and rejected, is there?

ELISA: Yeah. No. . . I mean, I wouldn't exactly say they're tortured. I mean, you can win a lot of money and there's always a Jacuzzi.

CLAIRE: Yes, that's true. Staying on an island with scantily clad women whose sole purpose is to steal your fiancé, starving in ninety-plus humidity while a bunch of sweaty type-A personalities force you to join their clique, and eating buffalo testicles is fun. Isn't it? Kinda like camp. . . Now, you've read our liability agreement and signed the paperwork?

ELISA: Well, they said I couldn't get through to the interview process if I didn't sign

CLAIRE: Either you're a serious contestant or you're wasting my time.

ELISA: I'm serious as Kelly Clarkson on the first season of American Idol. But I do have a tiny question.

CLAIRE: Really? Regarding?

ELISA: Well, about your having no liability for wounds, maims, burns, loss of limb, decapitation, or depression? Well, is that likely to happen?

CLAIRE: Is it likely that Michael Jackson will become a Buddhist monk? That Julia Roberts will be happily married? That Dan Rather will correct his lisp? My sense is, no, not likely, but I cannot know in all certainty, can I, Elisa?

ELISA: No. Well. . . it might be good if I knew what this one's about? What's the concept? Are we on an island, a beach house, in a studio, what?

CLAIRE: In due time. This will be very different. We don't want just everyone knowing our business. We want this show to stand out from all the rest.

ELISA: That's great! It's going to be different?

CLAIRE: Yes, very different. Groundbreaking. Unlike anything that's ever been done.

ELISA: Wow. You mean, the contestants won't meet every week to vote someone off?

CLAIRE: Well, no, we'll have that.

ELISA: No sexy hot tub scenes, flip-flop alliances and, when the ratings are lagging, some contestant that turns out to be wanted in three states?

CLAIRE: Oh no. We'll have all that. But we won't give out any money.

ELISA: Oh, wow! That is different. But why would we do it then?

CLAIRE: (Patronizing.) Now, Elisa, is this all about the money for you?

ELISA: (Pause.) . . . Yeah. (Beat.) Oh. I get it. This is one of those shows where the twist surprise at the end is that you actually do earn the money? Right? But you don't want to tell us.

CLAIRE: Well, if there's a twist, I obviously couldn't tell you!

ELISA: Well, I'd like to be on TV. That guy whose pet ferret went up his pants during his wedding ceremony on Funny Video ended up with his very own ferret Web site.

CLAIRE: Sure, there's the fame involved, and then if you were to get invited on the show, you would have the opportunity to live for free, with twelve other adults, in an environment that is cleverly devised by our creative team to be absolutely fun, interesting, and hot-Disneyland for adults. Bunk beds, a bathroom, a basketball court. And you'll get meals too.

ELISA: Oh, nice. Meals? How about a Jacuzzi?

CLAIRE: Of course! That goes without saying. Where will we have the steamy make-out scenes? (Laughs.)

ELISA: But I have a fiancé.

CLAIRE: Even better. Is he the jealous type? (Elisa nods.) Perfect. But don't worry, you only get to the hot tub if you get off for good behavior and that doesn't seem like you.

ELISA: Good behavior? What does that mean?

CLAIRE: All in good time, Elisa, when I explain the concept. Our goal is to get a very broad spectrum of viewpoints, a wide group of very difficult people who can . . . Oh! God. Did I say difficult? I meant diverse people, of course.

ELISA: I'm difficult. I'm very difficult! Diverse, too!

CLAIRE: That's OK, I was in no way saying that you have to be difficult-how so?

ELISA: Well. . . well, I . . . I'm whiney.

CLAIRE: (Unimpressed.) Yes?

ELISA: And I'm very angry.

CLAIRE: In general or . . . ?

ELISA: Well, I get very angry when people steal my stuff.

CLAIRE: Dh-huh. (Fishing.) And when else?

ELISA: No, that's it.

CLAIRE: Elisa. Don't most people get angry when people steal their stuff? What if I were looking for a truly difficult type-the kind who steals away her best friend's boyfriend or bosses around her very old, lame aunt.

ELISA: Well, I did that! I'm difficult! I . . . stole my old aunt's boyfriend!

CLAIRE: You did?!

ELISA: Well, it wasn't exactly stealing. And he wasn't exactly my old aunt's boyfriend. He walked her dog, but she had a little crush on him. And my old aunt's not lame, but she did have kidney stones.

CLAIRE: Oh-kay, Elisa, let's erase all this. We aren't just looking for difficult people. We need all types. Just be yourself. We want to capture various types that fit the wide demographics of our audience. That even means some happy, nice people like you. So long as they're between the ages of nineteen and twenty-five and have stellar bodies.

ELISA: I work out daily. I can dye my hair. I have a lot of cut-off tops too. I have a nice flat stomach. You want to see it?

CLAIRE: Not necessary. We collect our essential information before you get this far.

We're professionals here. I just have to tell you that you cannot second-guess what we need here, Elisa. It's all group chemistry. We might need a fat one, we might need an urban type. We might need a very wild and flakey type.

ELISA: (Raises her hand.) That's me! Fla-key!

CLAIRE: Dh-huh. I had a feeling. Now, let's discuss some of your fears. Just to keep things interesting. And fun! Look right over my right shoulder and say, "Fears."

ELISA: (Looks over her right shoulder.) "Fears." (She smiles.) Why did I do that? (Realizing.) Oh my God. Is this being taped? (Fixing her hair.) Oh gee. Do I look all right?

CLAIRE: Don't worry. We tape all the interviews so we can go back and look through our potentials. Also we use excerpts on the show if anything juicy comes up.

ELISA: Juicy? I've got juicy. Do I have juicy! Midgets!

CLAIRE: What?

ELISA: You know midgets, little people. I'm afraid of them. How's that for a juicy fear?

CLAIRE: Looks up intrigued.) Interesting. (Writes it down.) Anything else?

ELISA: You didn't like the midget thing?

CLAIRE: O, it was fine, but Phobia already did that.

ELISA: They did midget fears?!

CLAIRE: Yep. It blew. People were bored, offended. Got any other fears?

ELISA: Well, sure, I have tons! You name it, I'm afraid of it! Is that what you're looking for, a fearful person?

CLAIRE: Maybe. Is that you?

ELISA: Yes, indeed! I'm afraid of it all. Closed-in spaces, aliens, baby diapers. Big crowds, little rodents, eating flies, flying snakes, ugly dogs, vampires, cable TV, hockey naked!

CLAIRE: Naked? Did you say you were fearful of hockey naked?

ELISA: Yes! Yes, I am! Is that good?!

CLAIRE: No, but it is weird. Unfortunately, that would get us thrown right off the air.

ELISA: Wait a minute. Are you telling me the sensors will allow tarantula torture cells, snake pits, and eating pig rectums, but somehow naked hockey crosses over the line?

CLAIRE: Unfortunately, Elisa, I'm getting a vibe about all this. I just don't think you're right for our show.

ELISA: What?! Because of the naked hockey?!

CLAIRE: No, no. It's just you seem a little too perky.

ELISA: Perky?! I'm not perky! (Lowers the Pitch of her voice and affects cool boredom.) I'm not perky. I was just doin' "perky" because I thought that's what you wanted, man. Actually, I'm very (Yawns.) tired and bored. (She slouches extravagantly.)

CLAIRE: No, I'm looking for the real you, the you that you are. Just be yourself.

ELISA: (Calmly.) OK, OK, I see what you're saying. Here I am. I'm not overly perky. I'm pretty down-to-earth and low-key. I eat a lot of frozen yogurt. I'm really not afraid of anything. I don't have any embarrassing moments or weird old boyfriends.

CLAIRE: No, no, you don't understand, that's worse. I'm not looking for low-key either.

ELISA: Well, what are you looking for then?!

CLAIRE: Prisoners. Look, I'm looking for a group who will fit well into a prison setting. Our show is called The Big House. It's a prison environment. But I'm thinking you're too small-town. I'm looking for prison types.

ELISA: Prison? Well, that's great! People from small towns don't go to prison? Have you not heard of white trash, red necks? I've had tattoos. Now granted they were cereal box prizes, but I'll go permanent. I'm perfect for a prison. I should have been locked up long ago. (Swaggers.) Do you know how many times I've torn the "under penalty of law, do not remove" tag off of pillowcases? Do you know how many times I've made a U-turn over the double yellow lines? Wear my seat belt? Pff. Doesn't happen.

CLAIRE: Yes, but you seem to adapt too easily, Elisa. I mean, I want to put people together in the cells, in the bunk beds, and I don't want adapting happening.

ELISA: I don't adapt {Yells.} I don't do bunk beds! What am I nine?! See? I'm rigid.

CLAIRE: Can you give some examples of that?

ELISA: Sure, I'd be happy to. . . {Realizing. High-pitched.} No. Hah. No. I can't give examples of that, Claire, or anything else because I don't give answers, you little loser!

CLAIRE: How dare you talk to me like that!

ELISA: Tough! How dare you say I'm adaptable?!

CLAIRE: I'm in charge of this show! {Stands.} Do you want me to call security?

ELISA: Call security! Security-Smi-Sma-eerity. {Confused, trying to make this work.} Security-Smeerity. Whatever. That's hard to rhyme. My point is that you aren't the only one who gets to ask questions. What fears do you have, huh, huh!?

CLAIRE: I don't really have any big fears.

ELISA: That's a crock! Everybody knows that anyone sick enough to create the very different-NOT -Big House reality show is full of neurotic tendencies. Vile, disgusting ideas crowd your head. I see it now. Yes, control, entrapment, jeal-ousy, boxed potatoes, and sweaty men playing basketball all summed up by a perky, patronizing host! I don't want to be on your stupid, hot-headed, reality rip-off so you can use me until I'm sucked dry and unable to return to my bor-ing, but pleasant existence. I don't need you, you Hollywood hack, you pursed-lipped, tight-buttocks, Prozac-treated ninny! I'm better than you. I'm better than all of you! You can't handle me, Ms. Handal!!

CLAIRE: {Blown away, pause.} Wow. You have a lot of nerve.

ELISA: I've never done that before. I, I don't know what. . . came over me.

CLAIRE: I don't know either, but, I'll tell you this, you are absolutely, positively, not getting away from The Big House. We start taping next week.
```

---

## IC-0564: Black Pearl Sings!

- Title: Black Pearl Sings!
- Author (byline): Frank Higgins
- Work: Plays for Two
- Publisher: Vintage
- Publication date as stated: March 2014
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: PEARL, SUSANNAH
- Teaser before the introduction: Yes
- Spoken words (computed): 1390
- Already set (do not supply): none

### Source block (context only)

```text
Author: Frank Higgins
Book: Plays for Two
ISBN: 978-0345804549
Publisher: Vintage
Date (Month/Year): March 2014
```

### Introduction (context only: never use it for content warnings)

```text
Actress playing Pearl: It’s 1933, and an ambitious song collector for the Library of Congress visits a Texas prison

Actress playing Savannah: There she meets Pearl, an African-American woman with a soulful voice and steely spirit.

Actress playing Pearl: This play explores what it means to be black in a white world

Actress playing Savannah: A woman in a man’s world, and fighting for one’s soul in a world where anyone can be a commodity.

Together: Black Pearl Sings! By Frank Higgins
```

### Performance text (classify this)

```text
Setting: a warden’s office at a prison farm during a fierce Texas summer day in 1933. Susannah is packing up to leave, but hesitates when she hears Pearl

PEARL: (Pg 147-149) (Pearl begins to sing Off stage) Down on me, Lord, Down on me.
Seems like everybody in this whole wide world is down on me.
Down on me, dear Lord, Down on me.
https://www.youtube.com/watch?v=6Br7GDLbxqo

SUSANNAH: Hey! I want whoever that is singing brought in here. (Pearl enters in black and -white prison strips. Her ankles are shackled together, and she carries a ball and chain.)

PEARL: You be on the parole board? Don’t let this thing fool you; I be a good person.

SUSANNAH: No, I don’t give paroles – It’s okay to look me in the eye. What’s your name?

PEARL: Alberta Johnson. Friends call me Pearl.

SUSANNAH: Why you’re in prison is none of my business. But you sing better than the other women. My name is Susannah Mullally; I work for the Library of Congress. I go around the country to find songs from the people. I’ve found that prisons are a good place to look for old songs. My biggest dream is to find a song that goes back before slavery time; that came here from Africa.

SUSANNAH: (Pg 149-151) If I can find a song that came here on the slave ships, you know what that would do? We can prove to the world that a song can be stronger than even slavery chains. Were either of your parents slaves?

PEARL: Yessum. [But] I don’t wanna sing to no private. I wanna sing to a general who can do somethin’ for me. And since you want somethin’ I got . . . (Pearls starts to leave)

SUSANNAH: Wait. Wait! . . . (Pg 153) Do you know any old songs or not?

PEARL: I know some play songs I learnt when I was a chil’. My mama learnt ‘em when she was a girl too.

SUSANNAH: That get us back to slavery time. (Pg 156) I think you sang that song “Down on Me” knowing I’d hear it, knowing I’d like it, knowing I’d invite you in here. (Pg 155) Sing me the oldest song you know.

PEARL: (Pg 156-157) (sings – Troubles so Hard) Oh Lawdy now, troubles so hard / Don’t nobody know my troubles but God / Went in the room, didn’t stay long, looked on the bed and mother was dead. Oh Lawdy now, troubles so hard. https://www.youtube.com/watch?v=r9SENzRLk_M

SUSANNAH: Well, I guess I better get some men to lug in that recording machine. **********

SUSANNAH: (Pg 159) (excited) The people at the Library of Congress listened to the recordings we made. (reads a telegram to Pearl) “Oh, Susannah, all of us here thrilled!” – exclamation point – “Pearl is a pearl. Authentic doorway to the past. Make more recordings ASAP”

PEARL: (Pg 160) I ain’t makin’ no more recordin’s for you. (Pg 161) You tell me how you come to be here. Or you get nothin’ more from me.

SUSANNAH: [When I started] . . I haul that machine up into the Southern mountains on a mule, alone. The other song collectors are too afraid they’ll get shot. I turn in the recording to the man in charge. He sends it to D.C. But he takes credit for it.

PEARL: Why you didn’t tell folks the way it was?

SUSANNAH: I did. But he was older – well-known. He was a man. I thought I’d be the first woman to get a job at Harvard. I’d be able to send out a hundred collectors to save songs. Instead, he gets the Ivy League job and I get offered ten dollars a month if I’ll be quiet.

PEARL: (Pg 162) How this be anything but bad news for me? You an outcast.

SUSANNAH: I have a plan – (Pg 163) gets you out of her legally. (Pg 164) Get you a parole. We write up a convincing case to the governor. We point out that you are a model prisoner and that you are a doorway to our past. The governor would be happy to have one less mouth to feed. The governor is more inclined to parole a woman who has gentle qualities. What are you in for?

PEARL: I took a knife and killed a man. (Susasnnah looks stricken) (Pg 165) But I wouldn’t kill no man ‘less he needed it.

SUSANNAH: (taken aback for a moment) Well . . . we’ll try to make that a positive. (Pg 168) We’ll record a song just for the governor. (Pg 169) Make it a good choice: we’ll only get one chance.

PEARL: . . . There be an old song we sung in the cotton fields when I was a young’un. This be what the slaves be singin’ together in the field. Maybe in the fields owned by the ancestors of this gov’ner. (Pearl sings “Reap What you Sow”) You Gonna Reap What you Sow / Sowin’ on the mountain, sowin’ in the valley/ You will reap just what you sow https://www.youtube.com/watch?v=rNB7nbbFDjI **********

SUSANNAH: (Pg 172) The governor is looking over you file right now. He’ll make his decision within the hour.

PEARL: (Pg 176) Pray with me, Miss Susannah?

SUSANNAH: It’s just . .. . when I used to pray, the things I prayed for, I never got them.

PEARL: Maybe God did answer your prayers. But his answer was no. . . I say somethin’ wrong?

SUSANNAH: What is it with people who pary all the time? You think God sits around and says, “Ah, Pearl is thanking me for . . . God doesn’t care.

PEARL: My God cares.

SUSANNAH: (Pg 177) As an adult, there’s what I’ve learned: if I have to pray, then I haven’t done enough preparation. Preparation is my way of praying. If we get the parole, it will be because of my preparation. If I have to pray, then I didn’t prepare well enough.

PEARL: What you pray for before? To be a wife and mother?

SUSANNAH: Why would I want to be married? And end up like my mother?

PEARL: But with no kids, when you die you don’t just die. You die out.

SUSANNAH: Not if the songs I’ve save live on

PEARL: Ah’m gonna sing now. Lord, I’m not askin’ you this for my soul, but for Miss Susannah. (Pearl sings) (Pg 178) Do Lord, Do Lord, Lord, Remember Me. https://www.youtube.com/watch?v=g-etAyjh9co

SUSANNAH: (Susannah interrupts) Pearl, Don’t

PEARL: Do Lord, Do Lord, Lord, Remember me.

SUSANNAH: (Susannah interrupts) I want you to stop.

PEARL: Do Lord, Do Lord, Lord, Remember me.

SUSANNAH: I told you to stop it, didn’t I?! It’s a beautiful song. We’ll record it. You can sing it for me then. But don’t you dare sing it about me

PEARL: (Pg 179) Why you think you don’t deserve God’s love? (the telephone rings and startles the women – Susannah answers)

SUSANNAH: (Pg 182-183) (on the phone) Hello? – Yes. Let me have it --- (listens and give Pearl the thumbs-up signal) Thank you. I want the parole to start today. The women will be working on a chain gang clearing out a swamp. (Pause) You’re sentencing this great singer to three days of leeches! (Pause) No, your’e right. It’s foolish of me to question you. I’m sorry. Yes, we still want the parole . . . . Yes (Susannah hangs up)

PEARL: Thank you, Miz Susannah.

SUSANNAH: Pearl, your parole is not unconditional. I made a case to the governor that you are special. So there are things that we’re supposed to do during your parole.

PEARL: (Pg 184) So what are the strings?

SUSANNAH: It’s important to present you, and your songs, to people who matter. (Pg 185) The governor expects us to go to New York. (Pg 184) The real power is in New York.

PEARL: (Pg 185) I be a free woman. I go wherever I want to now and the gov’ner won’t know.

SUSANNAH: Not exactly. (Pg 186) You’ve been paroled into my custody.

PEARL: So I be your slave girl now.

SUSANNAH: You are not a slave. And don’t you ever say that to me.

PEARL: I have to go where you say? Do what you say? That be a slave

SUSANNAH: Everything I’ve done is to help you.

PEARL: And help yourself too. I ain’t goin’ to no New York. What you gonna do? Put me back in prison? (Silence while Pearl considers her options) There are only two kinds of people in this world. There’s a few people who look to the future, and there’s everybody else. So maybe I look to the future too. I’ll go to New York. ************

SUSANNAH: (Pg 208) (Off stage – Voice Over by way of introduction) Just as Paul and Silas were imprisoned but then sang and were set free, so has Pearl Johnson been set free. And this pearl is real; She’s a black pearl, and the Black Pearl Sings! (Pg 196) (Actresses step up to the apron and the sound of an audience applauding is heard)

SUSANNAH: (To the audience) Thank you. For the final song of the night, we’ve chosen one that was composed after the Civil War. Its author is lot to history, and the song was almost lost as well. But thanks to Pearl, the song and the people it is sung about live one. And thanks to the Carnegie Foundation’s grant to the Library, it will live forever.

PEARL: (Pg 199) (Sings) Kum ba yah . . . . . . kum ba yah . . . . (This does not sound corny like the “Kum Ba Ya” that contemporary audiences know). (Pearl explains) These be words that mean “come by here.” (Susannah joins to the song and both begin to clap, stomp and move the music in celebration. Susannah has opened her heart to the Lord and shows it in her singing) Me Mother need you lord, (Kum ba Yah) Me Father need you, lord (Kum ba Yah) Me Daughter need you, Lord

(Kum ba Yah) Oh Lord Kum Ba Yah. https://www.youtube.com/watch?v=XxzO4jByMvY
```

---

## IC-0565: Blushing Pilgrims

- Title: Blushing Pilgrims
- Author (byline): Ira Brodsky and Barbara Lhota
- Work: Duo Practice and Competition: 35 8-10 Minute Original Comedic Plays for Two Females
- Publisher: Smith & Kraus
- Publication date as stated: September 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: REBECCA, DIANE
- Teaser before the introduction: No
- Spoken words (computed): 2341
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ira Brodsky and Barbara Lhota
Book: Duo Practice and Competition: 35 8-10 Minute Original Comedic Plays for Two
Females
ISBN: 978-1575253800
Publisher: Smith & Kraus
Date (Month/Year): September 2004
```

### Introduction (context only: never use it for content warnings)

```text
REBECCA: Romeo and Juliet has become mandatory reading in most high school English classes.

DIANE: Teachers use this classic tragedy to display brilliant prose, beautiful poetry and heightened style.

REBECCA: And yet¸ I think they’re trying to teach us a little bit more…

DIANE: about life.

REBECCA: about love. (their eyes meet)

DIANE: Two classmatess explore the beauty of Shakespeare

REBECCA: and truly embody Romeo and Juliet in

BOTH: “Blushing Pilgrims”

DIANE: by Ira Brodsky and Barbara Lhota
```

### Performance text (classify this)

```text
REBECCA: (As Romeo, takes Diane's hand. Rebecca's reading is clear but she overly stresses the iambic pentameter.) "If I profane with my unworthiest hand / This holy shrine, (Diane giggles, shakes out her hand.) the gentle sin is this: / My lips, two blushing pilgrims, ready stand to smooth that rough touch with a tender kiss. "

DIANE: (As Juliet, stumbles through the speech, mispronouncing words.) "Good pilgrim, you do ring your hand

REBECCA: "Wrong!"

DIANE: Huh?

REBECCA: "You do wrong-not ring-your hand too much."

DIANE: Oh, I thought you were saying I was wrong.

REBECCA: Well, yes, no. "Ring" not "wrong": The line is "You do wrong your hand too much."

DIANE: OK, OK. "Good pilgrim, you do wrong your hand too much." Excuse me!

REBECCA: Yes?

DIANE: What is that, "You do wrong your hand?" She saying he's using the wrong hand?

REBECCA: No. Wrong is a verb here. It means like "harm" or "insult." Juliet is telling Romeo that he shouldn't criticize his own hand just for touching her. That there's nothing wrong in that.

DIANE: So she's kind of a slut?

REBECCA: How can you say that?

DIANE: Well, she is. He's a player, and she's playing right into him.

REBECCA: This is the greatest love story in the English language. This is the story that sets the bar for every other love story ever written.

DIANE: Hardly. Have you seen Pretty Woman? Now that's a classic. Julia Roberts!

REBECCA: But she was a prostitute.

DIANE: Yes, and then she meets Richard Gere, a ruthless, lonely millionaire, and he rescues her from a life of crime. And she rescues him through the power of love. And they both live happily ever after. I loved the shopping spree on Rodeo Drive.

REBECCA: Let's get back to work. I've gotta get to my French horn practice.

DIANE: Fine, fine. I'm just letting you know what I think.

REBECCA: I appreciate it.

DIANE: No, you don't, but that's OK.

REBECCA: Look, let's just get through this. I need my A, and I'm trying to make the best of it. I'm sorry Mr. Davis forced you to work with me.

DIANE: What you mean is you're sorry he put you with me. But that's OK. Let's get to it.

REBECCA: Take it from your line, "Good pilgrim."

DIANE: "Good pilgrim, you do wrong your hand"-If you're so smart, explain this pilgrim business. It makes no sense to me.

REBECCA: Here we go again.

DIANE: Humor me.

REBECCA: (Dryly.) You know what pilgrims are, right?

DIANE: I may not be a "student scholar" and member of the debating team, but I'm not an idiot. I know about the Pilgrims, the Mayflower, the first Thanksgiving with the Indians. Eating food off of Mom's prized Noritake china after she sighs for several hours about how she is expected to bleed for her family, Dad drinking too much and yelling about the football game. Me bursting into hysterics when my brother threw a hot candied apple at my sister and man-aged to hit me smack in the face. It's not about love. It's about carb overload.

REBECCA: Ooh, I'm sorry. But not those Pilgrims. This is back in Italy during the Renaissance, the rebirth and flowering of classic civilization that had died with the fall of the Roman Empire. Pilgrims are spiritual travelers who go on long, holy trips-pilgrimages-to religious sites in order to show their devotion and thanks to God.

DIANE: Freaky, man.

REBECCA: Well it was a big deal back then. To trek to the Holy Land, make a pilgrimage. I mean, they didn't have Club Med, you know.

DIANE: Well, aren't you the smarty-pants.

REBECCA: It's like this experience-this meeting of the two young lovers-is so beautiful that it is like a religious communion.

DIANE: Now that is so creepy.

REBECCA: How come? What's creepy.

DIANE: OK, imagine this. You're at a party.

REBECCA: A masquerade party, in fact, where all the participants are in costumes and with their faces hidden behind painted masks.

DIANE: Even worse. A total stranger dressed up as God-knowswhat starts slobbering all over your hand. What are you going to do? Start making jokes about pilgrims and saints?

REBECCA: Yeah, I kinda see what you mean. But that's because you're looking at it the wrong way. His face is hidden because he's a Montague, and it would be death to be caught at this party.

DIANE: I don't care if he's dressed up like the pope. You're gonna go up to Joe Player and say, "Beat it, perv!" And if that doesn't do it, you're gonna kick him in the 'nads. I don't know what this Shakespeare dude was thinking, but he sure didn't know women.

REBECCA: But I think there's a difference because this guy is the one.

DIANE: Yeah, and how do you know?

REBECCA: You just know. It's magic. It's true love.

DIANE: How come? He's got the right breath mint? You like the way his butt looks?

REBECCA: It's gotta be more than that. I mean, to live up to "true love."

DIANE: This play was written by a guy, right?

REBECCA: William Shakespeare, the greatest playwright and poet in the English language. Born April 1564, died 1616.

DIANE: And guys want one thing only, right? Sex.

REBECCA: Well, some guys. OK, all high school guys. But Shakespeare was out of school when he wrote this.

DIANE: You watch TV right? Go to the movies? All guys want one thing.

REBECCA: Well, maybe.

DIANE: So what could be cooler to guys than a story where the gorgeous babe not only takes your line, but actually eggs you on to go further. Of course, with how sheltered they were back then, she was probably pretty desperate.

REBECCA: (Exasperated.) Can we get back to work?

DIANE: OK. I'll say the words, but I think the play sucks. (Laying on the sexiness.) "Good pilgrim, you do wrong your hand too much, / Which mannerly devotion shows in this; / For saints have hands that pilgrims' hands do touch, / And palm to palm is holy palmers' kiss."

REBECCA: (Seriously, but still with too much stress.) "Have not saints lips, and holy palmers too?

DIANE: (Even sexier.) "Ay, pilgrim, lips that they must use in prayer."

REBECCA: Wait, hold!

DIANE: What? What? I'm doing what you asked-encouraging him!

REBECCA: Well, yeah, but there's a change here. Don't you see it?

DIANE: No.

REBECCA: OK. Romeo's trying to heat things up. He's got Juliet on the hand thing, so now he's working up to the lips.

DIANE: Right, I should have known.

REBECCA: But Juliet's blowing him off.

DIANE: Finally.

REBECCA: But nicely. She's like, pilgrims can touch hands, but they don't touch lips. Lips are for praying.

DIANE: Talk to the palm 'cause the lips ain't listening, girlfriend.

REBECCA: Exactly! Except that she's totally hooked. So while she wants to slow him down, she doesn't want to blow him off.

DIANE: You're really like into this Shakespeare, aren't you?

REBECCA: I guess. I hate to think that the greatest playwright of all time kind of sucks in his knowledge of love.

DIANE: Have you ever like really been in love?

REBECCA: (Desperate.] Can we please get to it!? I told you about my French horn practice.

DIANE: How can you act love if you don't know love?

REBECCA: This is for English class! It doesn't matter! You just want to pronounce the words and look like you know what you're talking about.

DIANE: Being in love doesn't matter? When you're trying to act out the "greatest love story of all time"!?

REBECCA: Well, I've been very busy: studying, music lessons, forensics.

DIANE: Sounds boring.

REBECCA: I assure you, it isn't. I have big plans for my future, and I'm very focused.

DIANE: Kinda lonely, huh?

REBECCA: I'm concentrating on my career goals first.

DIANE: Now I get it!

REBECCA: What do you get?

DIANE: This "You do wring your hand too much"

REBECCA: "Wrong you hand."

DIANE: This is all you know about love!

REBECCA: This is so totally incorrect and unjust.

DIANE: Well, what do you know?

REBECCA: Jane Austen.

DIANE: Oh, we swing that way, do we? How twenty-first century!

REBECCA: No. She's an eighteenth-century British author, Pride and Prejudice.

DIANE: Oh. Eighteenth century, huh? That's a few years back. And she was well experienced in love?

REBECCA: Actually she lived and died in her father's house in a small village in England. Never married.

DIANE: So all you know about love comes from books and stuff, and one of your so-called experts is a dead virgin spinster!

REBECCA: I know more than what's in books! I've been around.

DIANE: Oh, have you?

REBECCA: Yeah.

DIANE: Have you ever been there in the clinch, where it's dark and you're alone with some guy and all you smell is his cologne and under that, the real smell of his sweat? (Pause. Rebecca listens intently.) And even though he's shaved all nicely, his face is a little rough against your skin, and he's clinging to you and trying to unpeel you, to get to you physically and mentally. And part of you knows you should stop him because he's just all worked up with testosterone, but part of you loves the feeling of his power and the feeling of your own power-that he wants and needs you so much. He wants to possess you, become you. And everything is sweaty and warm and smooth, his lips, his skin, his leather jacket.

REBECCA: Holy ...

DIANE: Oh, God. It can be a religious experience.

REBECCA: You're a poet.

DIANE: Nah, hardly. I just got carried away.

REBECCA: That's what poets do. They get carried away by life, and they take us along. That's what Shakespeare does. He knows love and life, and he serves it up on a silver platter, just like you did. Crap!

DIANE: What?

REBECCA: All I do is work and read and go to meetings. I get up early every morning, and run for a mile. I go to class and fix sandwiches for the homeless and tutor inner-city kids. And by the time I finish homework and practice and review my notes from the day, I just fall dead asleep.

DIANE: But when do you have time to shop, to get your makeup and nails done?

(Rebecca gestures to her plain style.) Oh, I see. But at least people respect you.

REBECCA: Like who? The only guy in my life is Pete Weiner, and he only likes me for my knowledge of baseball trivia and my collection of early computer games.

DIANE: Well, one day some real Romeo will come along, and he'll love you totally. Not just because he's all jazzed up and you're looking cute-but because he really knows you and that's who he wants to get inside and be a part of.

REBECCA: That's nice of you, Diane. But I know what I look like. I don't excite that kind of passion. But that's OK.

DIANE: You think because I got the nice butt and the boobs-?

REBECCA: Not just that. It's the whole quesadilla: the face, the bod, the spirit burning deep within you.

DIANE: Don't be so sure.

REBECCA: But you told me what it's like in the clinch. That passion, that intensity. I mean, I've never ...

DIANE: Well, sure-that's what it should be like, what it could be like. But usually ...

REBECCA: What usually?

DIANE: Usually it's midnight in somebody's crummy basement party. You're a little buzzed because the guy you really like is making out with some other girl. So you're with some loser who smells like pizza, and keeps saying, "You're hot, baby. You're really hot." And maybe you fool around a little because you get the stupid idea that it'll make the other one jealous. Until all at once, pepperoni breath goes to grab something he shouldn't, you dodge and he knocks over the potato chip dip in the metal bowl which falls onto the floor. The party givers' father suddenly screams from upstairs, "Everybody get out-now!"

REBECCA: Oh.

DIANE: Yeah.

REBECCA: So maybe it could be worse than Pete Weiner.

DIANE: I guess. (Imitating his loud, squeaky voice.) But doesn't his voice kinda grate on your nerves like nails on a chalkboard?

REBECCA: He doesn't talk that much. I just wish he wanted to hold me and possess me, like you talked about. We mostly play Magic cards and computer simulation games. His new goal's to memorize enough digits of pi to make it into Ripley's Believe It or Not.

DIANE: Maybe his hormones haven't kicked in yet. Maybe you have to help him out.

REBECCA: What do you mean?

DIANE: Encourage him. You know like Juliet in the play.

REBECCA: Except my Romeo hasn't even made the first move yet.

DIANE: Yeah, some guys need a little help getting started. Just a signal or two.

REBECCA: I never thought of that.

DIANE: Girls have to be sharp.

REBECCA: Yeah, they do. Thanks.

DIANE: My pleasure. It's not very often that anyone thinks I have anything to teach.

REBECCA: Are you kidding? Your life is like a novel. Full of passion and heartache.

DIANE: I'm surprised to say it, but it'll happen to you one day.

REBECCA: You think?

DIANE: Yeah, you don't show it off, but you have something inside.

REBECCA: You really think it could happen?

DIANE: Sure. But it wouldn't hurt if you did something with your hair and wore lipstick.

REBECCA: Hey, I have an idea.

DIANE: What?

REBECCA: Let's switch places.

DIANE: You want to start cheerleading and have me join the debating team?

REBECCA: Nah. You be Romeo. I want to try Juliet.

DIANE: OK. Actually, I think I get this Romeo dude. (She positions herself and takes Rebecca's hand. While she still stumbles over the occasional word, her reading is spot on. She has Romeo's quiet intensity.) "If I profane with my unworthiest hand / This holy shrine, the gentle sin is this: / My lips, two blushing pilgrims, ready stand to smooth that rough touch with a tender kiss."

REBECCA: (Takes Diane's hand and holds it tenderly. She speaks normally, without the exaggerated stresses.) "Good pilgrim, you do wrong your hand too much, / Which mannerly devotion shows in this; / For saints have hands that pilgrims' hands do touch, / And palm to palm is holy palmers' kiss."

DIANE: "Have not saint lips, and holy palmers too?"

REBECCA: "Ay, pilgrim, lips that they must use in prayer."

DIANE: "0 then, dear saint, let lips do what hands do. / They pray; grant thou, lest faith turn to despair."

REBECCA: "Saints do not move, though grant for prayers' sake."

DIANE: "Then move not while my prayer's effect I take."

REBECCA: (Looking at the book.) It says here that Romeo kisses- (Diane kisses Rebecca.)

REBECCA: Oh. (Pause. Quietly.) So that's how it's supposed to be.

DIANE: We are pretty good actors, huh?

REBECCA: (Not what she meant.) Yeah, yeah.

DIANE: And that Shakespeare ain't completely bogus either.

REBECCA: Do you think it ever goes like that in real life? I mean the kiss? Love?

DIANE: I don't know. I really don't. But I bet you get your A.

REBECCA: Not that grades are everything.

DIANE: You're right.

REBECCA: Hey! What do you say about a hamburger break?

DIANE: Sure, I'm starved, but I thought you had music practice?

REBECCA: Yeah, but I think there's time for everything. (Smiling.) What do you say, good pilgrim?

DIANE: (Puts her arm through Rebecca's.} Let's motor-dear saint.
```

---

## IC-0566: Breakfast

- Title: Breakfast
- Author (byline): Norman A. Bert
- Work: More One-Act Plays for Acting Students
- Publisher: Meriwether Publishing
- Publication date as stated: July 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: WAITRESS, CUSTOMER
- Teaser before the introduction: Yes
- Spoken words (computed): 1409
- Already set (do not supply): none

### Source block (context only)

```text
Author: Norman A Bert
Book: More One-Act Plays for Acting Students
ISBN: 1566080878
Publisher: Meriwether Publishing
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
WAITRESS: So many choices

CUSTOMER: selections

WAITRESS: options

CUSTOMER: alternatives

WAITRESS: And it’s only…

BOTH: Breakfast

CUSTOMER: by Norman A. Bert
```

### Performance text (classify this)

```text
(A CUSTOMER enters the coffee shop. She pauses only long enough to see the table before going to sit at it. The WAITRESS approaches.)

WAITRESS: Good morning.

CUSTOMER: Hi.

WAITRESS: Would you like to see a menu?

CUSTOMER: No, that won't be necessary; I know exactly what I want.

WAITRESS: (Taking her order pad and pencil from a hip pocket) Fine. Coffee - or tea?

CUSTOMER: Coffee, please.

WAITRESS: Regular of decaf?

CUSTOMER: Regular.

WAITRESS: White or black?

CUSTOMER: White, please.

WAITRESS: Milk, cream, or non-dairy whitener?

CUSTOMER: Milk.

WAITRESS: Whole, skim, or two-per?

CUSTOMER: Two-per.

WAITRESS: Sugar?

CUSTOMER: Artificial sweetener, please.

WAITRESS: Liquid or powder?

CUSTOMER: Oh, you have liquid sweetener? Yes, liquid, please.

WAITRESS: (Writing it down) Fine. And now, something to eat?

CUSTOMER: Yes. Cold cereal, please.

WAITRESS: (Writing it down) Cold cereal. What kind, ma'am?

CUSTOMER: Oh, it doesn't matter. Just bring anything.

WAITRESS: I'm sorry, but I can't do that. My job is to serve you; your job is to make the decisions. I don't get paid enough to make customers' decisions.

CUSTOMER: OK. No problem. What have you got?

WAITRESS: Well, we're not a supermarket. We have a limited selection of the most popular brands. Just tell me what you want; chances are, we got it.

CUSTOMER: No, no, no. Tempt me. Come on, give me the list.

WAITRESS: (Sighing) OK. We got granola and milled. Natural, regular, and strictly artificial. Oat, wheat, rice, corn, barley, and combinations. With fruit and without. Sugared and not sugared. With saccharin and/or Nutrasweet. Kellogg's, Post, Quaker, General Mills, Checker-Board- Square, Nabisco, Malt-O-Meal, and generic.

CUSTOMER: That's a limited selection?

WAITRESS: This ain't New York, lady. What can I tell ya? If it's not enough choices, a new shipment comes in on Tuesday.

CUSTOMER: Well, I can't cope with all that. Just bring me some bran cereal.

WAITRESS: Bran.

CUSTOMER: Yeah. You have bran?

WAITRESS: Yeah, we got bran. Flakes or "all-bran" variety?

CUSTOMER: What?

WAITRESS: Do ya want the kinda bran that's in flakes, or do ya want the kinda wormy looking stuff. Sorry. Not a nice choice of words, but that's always what it looks like to me.

CUSTOMER: Oh, the cat-food-looking stuff.

WAITRESS: Yeah, that's it. Cat food. Gotta remember that. Sounds better than "wormy looking."

CUSTOMER: Yes. That's fine. I'll take that kind. I mean, that's the real thing, isn't it? I mean, if you're going to eat healthy, you might as well go all the way, huh?

WAITRESS: Yeah, well, that's up to you. Me, I eat to live. Live and enjoy. Far as I can see, if you eat what you like, you'll eventually get it all, you know?

CUSTOMER: Maybe. I'm not so sure. Anyhow, I'll have the wormy kind of bran.

WAITRESS: Good. That narrows it down. Now we got your Real Bran, your Extra Bran, and your Total Bran.

CUSTOMER: Oh my God. What's the difference? Just bring me one of them!

WAITRESS: Like I said, lady. They don't pay me to make decisions. It can only get me in trouble.

CUSTOMER: OK. So what are they again?

WAITRESS: Real Bran, Extra Bran, and Total Bran.

CUSTOMER: I don't know. What's the difference?

WAITRESS: Well, for one thing, they differ in the amount of dietary fiber which is the bulk stuff why people eat bran in the first place.

CUSTOMER: Yeah?

WAITRESS: Yeah. Now your Total Bran has twelve grams of fiber per serving while your Extra Bran only has ten and your Real Bran's got only nine.

CUSTOMER: Well, that solves it then, doesn't it? I'll take the ...

WAITRESS: Hold it, hold it. Don't you want to know about the sugar? I mean, if you're gonna be healthy, you ought to consider the sugar, too, right?

CUSTOMER: Yeah, OK. So tell me about the sugar.

WAITRESS: Well, they all got it in one form or another. Extra Bran's got six grams per serving; Real Bran's got five grams, and Total Bran's only got two grams.

CUSTOMER: Well, that settles it then for sure.

WAITRESS: Maybe.

CUSTOMER: Maybe?

WAITRESS: Take it from me, the Total Bran needs more sugar. I watch the customers, see, and most of the Total Bran eaters, after one or two bites, they put on a little sugar. They're pretty sneaky about it, but I don't miss much. You put a half teaspoon of sugar on, and you're right up there with the Real Bran and Extra.

CUSTOMER: Oh, wow. Well, let me see. I...

WAITRESS: Yeah, and while you're working on that, you might also consider that your Real Bran's got two hundred sixty milligrams of sodium while your Extra and Total have a hundred and ninety milligrams and two hundred thirty, respectively. Not counting the milk, that is. 'Course I don't know if you're concerned about that or not.

CUSTOMER: No, I'm not.

WAITRESS: Fine. They're your arteries. Anyhow, like I always say, how can soft food make hard arteries, right?

CUSTOMER: So, you mean to choose my cereal, I have to strike some kind of a balance between my bowels, my heart, and my arteries?

WAITRESS: Yeah, that's it. Least that's one way to look at it. Or you can think of it this way - choosing between going fast with a coronary, being paralyzed then zapped again for good with a stroke, or sort of lengthening it out with cancer, you know?

CUSTOMER: This is getting harder and harder. Say you know what you ought to do? You ought to make up a chart with the various kinds of cereal and all the variables so people could see it all at a glance and make up their minds that way.

WAITRESS: Do you know how much space that would take up, lady? It'd be a book. I mean we haven't even started on the various vitamin contents and all. And then, if we got into the fruities and sweeties and spookies and other novelty cereals, well, it would just be impossible.

CUSTOMER: Maybe you could computerize it. I mean, you could get rich. Put all the cereals in this program and sell it to restaurants.

WAITRESS: I dunno. You know what kind of turn-over there is in the cereal market? Every month there are a few new ones and a couple of the old ones bite the dust.

CUSTOMER: So much the better. For an annual fee, you agree to up-date everyone's program monthly. Just think of the possibilities. You could get out of this joint and be on your own.

WAITRESS: What's the matter with this joint? I sort of like it here. Besides, how many restaurants got computers anyway?

CUSTOMER: You might be surprised. And if they haven't got them now, they'll get them soon.

WAITRESS: Dunno much about computers, but I can tell you one reason it wouldn't work: taste. When everything's said and done, most people choose a cereal 'cause they just like it. That's individual. You can't computerize taste.

CUSTOMER: I think you could quantify it. You just ask the customer, "On a scale of one to ten, how crunchy do you like your cereal, with one being over-cooked oatmeal, and ten being dry granola?" And then you punch the answer in and say, "OK, and on a scale of one to ten with ten being pure sugar and one being like water, how sweet do you like your cereal?" Then you punch that in and...

WAITRESS: OK, I get the point. Maybe it's possible.

CUSTOMER: It's just a choice. If it's a choice, you can quantify it. Choices come from a balancing of variables. Computers can handle variables.

WAITRESS: Dunno. I still think the customer should be able to decide.

CUSTOMER: And speaking of choices, I'd design it for the IBM Pc.

WAITRESS: IBM PC?

CUSTOMER: Yeah, the computer, you know?

WAITRESS: Oh, the IBM PC's a computer.

CUSTOMER: Yeah. Although you might want to consider Apple. There are millions of Macs out there. They're more userfriendly.

WAITRESS: User-friendly. Well, that should probably go into making the choice.

CUSTOMER: Oh yeah, for sure. 'Course if you want cheap, there's Dell. Or Compaq. And then there's Gateway and Toshiba and Cybertron and Alienware and Packard-Bell and H-P and N-E-C and A-B-S and ...

WAITRESS: Hold it, hold it, hold it. I can't get into this! I got enough problems. Forget the computers.

CUSTOMER: You mean you choose to ignore the whole wave of the future?

WAITRESS: Yeah. Should I feel guilty or something?

CUSTOMER: No. That's cool. It's your choice.

WAITRESS: Fine. Now can we get back to your cereal?

CUSTOMER: Look I can't deal with this cereal thing. Just bring me an egg and toast.

WAITRESS: (Scratching off "cereal" on her order pad and writing "egg w/T") OK. You want that egg over, up, scrambled, poached, or boiled?

CUSTOMER: Uh. Up, I think. No - over. Yes, definitely over.

WAITRESS: Hard or runny?

CUSTOMER: Just so the white won't and the yolk will, if you know what I mean.

WAITRESS: No problem. White, wheat, or rye toast, bran muffin, English muffin, or bagel?

CUSTOMER: Wheat toast.

WAITRESS: Anything else?

CUSTOMER: No, that should be just fine.

WAITRESS: Fine. Be back with your coffee in a minute.

CUSTOMER: Thanks. (The WAITER exits.)
```

---

## IC-0567: Breath Sounds

- Title: Breath Sounds
- Author (byline): Jane Nicolaas
- Work: Breath Sounds
- Publisher: SpeechGeek
- Publication date as stated: 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1383
- Already set (do not supply): none

### Source block (context only)

```text
Breath Sounds by Jane Nicholaas
ISBN: 978-1-61387-041-9
Copyright 2013 by SpeechGeek.
Free performance of this play for high school and college level
competitive forensics is permitted. All other rights reserved.
This PDF version of this selection, e-published in 2013, is identical to the
printed published version of this same publication dated 2013. This
statement along with the entire printed PDF of this publication must be
presented at any National Forensic League District or National event for the
script to comply with NFL rules per the request of the Executive Director.
This and other selections of quality performance literature for competitive
oral interpretation are published by SpeechGeek.
For more information and performance rights, contact SpeechGeek.
SpeechGeek
248 Arlington Park Dr.
Hot Springs, AR 71901
Phone: 1-888-742-2028
Email: thegeek@speechgeek.com
Web: www.speechgeek.com
Facebook: www.facebook.com/speechgeek
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
SCENE ONE PAIGE. (PAIGE directly addresses the audience.) They tell you in med school that your first year as a doctor is the hardest. You learn the most. You lose the most. If you’re lucky, you find what you love. By the time I arrived at my internal medicine rotation, I was sure I had it all figured out. Life and death. Luck and love. These were all very separate parts. Then I met Evan.

PAIGE. (PAIGE is now “in-scene” and addresses EVAN off-handedly.) Okay, I’m sorry for the wait.

EVAN. It’s no problem. I’ve got all the time in the world.

PAIGE. (looks at him with surprise and mild annoyance before rifling through papers) Right. (She finds his chart and reads the list of answers aloud without realizing what she’s saying.) You are Evan Carter, a 24-year-old male, son of Fred and Wilma Flintstone, presents with advanced (beat) menstrual cramps.

EVAN. Do go on.

PAIGE. Okay. (turns to leave) Have a nice day, Mr. Carter.

EVAN. You’re leaving?

PAIGE. I have a lot of patients to see--patients with medical histories that aren’t a big joke.

EVAN. It’s not all a big joke.

PAIGE. Some of the answers are drawings.

EVAN. Well, my name is Evan Carter, and I’m dying of cystic fibrosis. I guess the details are sort of a joke.

PAIGE. (addressing the audience) Now, I know that doctors are typically meant to heal. We close wounds. We don’t open them. But I don’t think there was anything typical about this whole thing.

SCENE TWO PAIGE. (addressing the audience) As a Doctor, you never want to see your patients return time and again, but every time he came back to the hospital I felt something in me. It felt suspiciously like joy.

PAIGE. (returns to scene) Hello again, Mr. Carter.

EVAN. What’s up, doc?

PAIGE. (looks over his chart) Back so soon? I don’t think I like that.

EVAN. Not even a little?

PAIGE. Maybe we should switch your medication regimen.

EVAN. Nah, I’m ok. I just like it here. You guys have got cable.

PAIGE. (running tests on him) Well, you’ve got good timing. Breathe in. Detroit is playing Chicago tonight. Breathe out.

EVAN. You like football?

PAIGE. I love football, now shush and breathe in.

EVAN. Do you like pizza?

PAIGE. Breathe out. I do. I also like breath sounds so stop talking.

EVAN. I’ll make you a deal. I will shut up and pay for pizza if you come watch the game with me tonight.

PAIGE. I can’t.

EVAN. Well in that case…(proceeds to sing loudly) la la la…you get no breath sounds…la la la.

PAIGE. Evan. Evan! Ugh, fine! I’ll stop by if I can. You’re so annoying.

SCENE THREE PAIGE. (addresses audience) He was like that song on the radio. You don’t want to like it, but it’s happy, catchy, and always there. And before I knew what I was doing, I was humming along.

EVAN. (both hunched over a chess board) You can’t do that.

PAIGE. Yes I can.

EVAN. No, the horsey moves…

PAIGE. (laughs) The horsey?

EVAN. Yes, he moves in an L shape. You can’t. (They start to tussle over the chess piece. They are laughing hysterically until EVAN launches into an intense coughing fit that leads to him hyperventilating. She is quick to react. PAIGE moves behind him and quickly grabs the breathing mask. She puts it on him. He continues to breathe erratically as she cradles him against her.)

PAIGE. Shhh. Evan. Shh. Listen to me. Breathe when I breathe. (They breathe together. He slowly calms down until they are left silently breathing. They share a moment that is intimate, heated, and doomed. PAIGE stands to leave but EVAN holds on to her hand. She stares at it for a moment and then slips away.)

SCENE FOUR PAIGE. (addresses audience) I fought to stay away from him. I really did, but what can I say? It was Evan. He was nothing if not a fighter.

EVAN. Hey, doc, wait! (chases her out, wheezing) Don’t you know it’s cruel to make a guy with cystic fibrosis run?

PAIGE. Mr. Carter. I’m a doctor. I’m busy. What do you need?

EVAN. I guess I need some forceps to remove the I.V. stand from up your butt.

PAIGE. Have a good day, Mr. Carter.

EVAN. Whoa, make that the jaws of life! What is your problem?

PAIGE. You’re making a scene. (drags him into a storage closet)

EVAN. You dragged me into the storage closet. Now who’s making a scene?

PAIGE. Stop, Evan. Just stop. This isn’t a joke.

EVAN. She said standing by the enema bags.

PAIGE. Don’t you get it? I am not allowed to do this.

EVAN. You’re not allowed to do what?

PAIGE. (exasperated) I’m not allowed to feel like this.

EVAN. You’re not allowed to feel? Are you sure this isn’t a joke?

PAIGE. (She relents into laughter.)

EVAN. You have a beautiful smile.

PAIGE. (She sighs and lets her guard down.) What are we doing? You’re stage four CF, and you’ve only got 33% lung function.

EVAN. And I’m highly accident-prone. I can’t take anything seriously. Oh, and I cheat at chess.

PAIGE. You cheat at chess?

EVAN. The point is: I don’t have a point. Maybe, it’s just me breathing when you breathe for as long as I can.

SCENE FIVE PAIGE. (addresses audience) That’s the sickest part of all of this. He knew. We both knew from minute one exactly how this would end. But over the next five months we did what people in impossible situations do, we fell hopelessly in love.

EVAN. (PAIGE returns to the scene. EVAN’s breathing is noticeably more labored.) Did you always want to be a doctor?

PAIGE. Always.

EVAN. (He laughs but it prompts a painful fit of coughing.)

PAIGE. Evan?

EVAN. (He ignores the coughing and pushes through to talk.) I can totally see you, “I need 50cc’s of Kool-Aid and a teddy bear… STAT!” (He coughs again. He is frustrated and in pain.)

PAIGE. (tries to soothe him) Evan.

EVAN. I’m fine. (EVAN continues coughing. PAIGE gets his breathing mask but he pushes it away.) I’m fine!

PAIGE. Okay, you’re fine. (EVAN takes the mask and shoves it on his face. PAIGE sighs and then tries to lighten up.) What did you want to be when you grew up?

EVAN. Alive.

PAIGE. Don’t say that.

EVAN. It was a joke.

PAIGE. Well it’s not a funny joke, Evan.

EVAN. Whoa, calm down, doc.

PAIGE. I hate that. You make these awful jokes and then act like there’s something wrong with me for not giggling, “Oh, ha-ha, you’re dying. Ha-ha!”

EVAN. Well, excuse me for not crying about it all the time.

PAIGE. All the time? Try doing it once.

EVAN. That’s not how I deal with it.

PAIGE. Do you deal with it?

EVAN. (stares at her) I wanted to be Big Bird.

PAIGE. (smiles a little) You could be a great Big Bird.

EVAN. Yeah, but I’m running out of time. (awkward moment) Mitt Romney’s going to fire him soon.

PAIGE. Yeah.

SCENE SIX PAIGE. (addresses audience) It was getting worse. Sometimes it sounded like a single laugh would be enough to break him in half. But he kept on laughing, which made it all seem better and worse.

PAIGE. (PAIGE sneaks in. EVAN has his breathing mask on.) Hey.

EVAN. (starts to remove the mask)

PAIGE. No, no. It’s ok. Leave it.

EVAN. (He relaxes. His breathing is heavy and painful.) What’s up, doc?

PAIGE. (She struggles a bit.) Ugh, how many times do I have to call you to call me Paige. It’s weird that you call me “doc.”

EVAN. (He tries to calm her as she is clearly losing it.) Hey. What’s going on?

PAIGE. Your tests came back, Ev. It’s not good news.

EVAN. It was never going to be.

PAIGE. (starts to cry)

EVAN. Shh… Paige…

PAIGE. This is stupid. I am stupid. I am sitting here right now, and every moment you get closer to dying I fall more in love with you.

EVAN. Shhh… Paige…shh. Listen to me: breathe when I breathe. (She slowly calms down.) I love you, too.

PAIGE. What am I going to do when you leave me?

EVAN. I won’t ever leave you, Paige. You’ll breathe and you’ll feel me breathing with you.

PAIGE. That’s romantic.

EVAN. Romantic? I’m talking about haunting you as a ghost.

PAIGE. You’re annoying.

SCENE SEVEN PAIGE. (addresses audience) It was a matter of time. It always is.

PAIGE. (on the phone) Hello. Is this Paul Carter? Hi, this is Dr. Paige. (gets interrupted on the other end)

Oh, Evan’s told me a lot about you, too.

Well, I’m…I’m calling with some bad news.

(stops for a moment to compose herself) The respiratory drugs we had your son on caused a blood clot to form in his lungs. It got into his bloodstream and traveled into his brain. Evan had a stroke this morning and—Yes, sir. I was there with him. I was holding his hand. I—we—did everything we could.

PAIGE. (addresses audience) And just like that, in the blink of an eye, in the space of one breath, it all came tumbling down.

SCENE EIGHT PAIGE. (PAIGE enters the room and EVAN is still in the hospital bed. A respirator has replaced his breathing. It is hard for her to see him like this. She goes and reads his chart out of habit. A letter falls out.) What is this? “Dear Paige,” Oh god. (sits down) “Dear –“

EVAN. Paige. I don’t know when or how I went, but I promise I fought to stay. I thought about writing out another medical history, maybe something like, “presents with advanced death.” But you were right: not everything is a joke. We were never a joke. Maybe I didn’t say it enough, maybe you thought I was joking, or maybe you just needed to know once and for all that you are the love of my life. I am grateful for every breath.

SCENE NINE PAIGE. (addresses audience) Your first year as a doctor you definitely learn the most, you lose the most, and—if you’re lucky—you find what you love. I don’t know if a lot of people would consider me lucky, but I do. I found joy in sadness. I found laughter in tears. I still feel him when I breathe in and when I breathe out. I feel him and that makes me feel very lucky.
```

---

## IC-0568: The Cake

- Title: The Cake
- Author (byline): Bekah Brunstetter
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: March 2018
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS 1, ACTRESS 2, MACY, JEN, DELLA
- Teaser before the introduction: Yes
- Spoken words (computed): 1447
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bekah Brunstetter
ISBN: 978-0573706875
Publisher: Samuel French, Inc.
Date (Month/Year): March 2018
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: In today’s political climate, it is easy to demonize those who think differently . . .

ACTRESS 2: . . . Particularly when we believe their beliefs infringe on others' rights.

ACTRESS 1: The right to refuse service to members of the LGBTQ community has become explosive.

ACTRESS 2: A legal matter? Perhaps . . . But it’s the individual emotional turmoil surrounding this issue that may never be resolved.

ACTRESS 1: This selection whittles the right to refuse service for religious reasons down to the most personal of human connections.

ACTRESS 2: And in doing so, it welcomes you to see Della, the baker in our story, as a real person.

ACTRESS 1: You may agree or disagree with her struggle to find the best path, but the need for relationships as we navigate this crazy world is universal.

TOGETHER: The Cake by Bekah Brunstetter
```

### Performance text (classify this)

```text
NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

ACTRESS 1: Macy and Della (In the original script Macy is African-American)

ACTRESS 2: Jen

(Scene opens with Macy and Jen walking down the main street of Jen’s hometown in North Carolina – It is quaint and filled with Southern charm. NOTE: Both Jen and Della should have varying degrees of a southern drawl, while Macy is definitely from NYC but may or may not have an NY accent)

MACY: (Pg 33) I drove down through here, in high school, it was my first time going anywhere south of Philly. When my mom dropped me off at the bus that morning, she was like, “Careful down there. It’s different down there.” The more south we got, the billboards started to change. They were all lit up like beach t-shirts. “Evolution is a fairy tale for grown-ups.” “’Don’t make me come down there.’ – God.” Or just “JESUS!”

JEN: That’s one’s my favorite.

MACY: They were all paid for by churches. That’s when I realized that [in North Carolina], church is just another chain store.

JEN: Well, that’s a generalization. (Diverting) At least down here, you can have a real house. With countertops. And CLOSETS. A whole closet just for winter coats. If we lived here, we could have a staircase and a big yard with a dogwood tree and a tire swing and a little creek out back –

MACY: Here? For actual life? Nope.

JEN: (Looks around her old hometown) (Beat) (Pg 57-58) It was a good part of my life. For so long . . . Every time someone says that God doesn’t exist, a little something inside of me burns – it goes DING. But with fire. I’m of two different minds. [New York and North Carolina] All the time.

MACY: (Pg 59) Does it ding when you kiss me? (Jen can’t respond) Does it?

JEN: . . . Not every time, but - (A horrible confession. Macy and Jen stare at each other in silence)

(The women reach their destination – Della’s Cake shop)

JEN: (Pg 19-21) The Cake! Cake, cake, cake. (Her excitement is palpable)

MACY: (A sad huzzah) Cake. Does it really matter?

JEN: I just want it to be perfect!

MACY: Can we pleeeeeease just go to the Food Tiger where it’s thirty bucks and nobody asks questions?

JEN: It’s a Food Lion. [And, no] I want to get it from here.

MACY: Ma’am, can I get your eyes for a second, like your full eyes? (Jen looks at her fully) There’s already enough drama doing this here. I’m just asking, why do we have to?

JEN: She was my mom’s best friend. There are just things that I . . . my mom would’ve . . . I just want to do it like we talked about doing it. Even though she’s not . . . (She has tears in her eyes)

MACY: (Comforting) Okay . . . Hey. We’ll get it from here. (They enter the store as Della emerges from the back – Actress shifts roles from Macy to Della)

DELLA: Is that . . ? No! Jenny Penny?! OH MY GOODNESS! It’s you! (so excited to see her)

JEN: It’s me! (They hug as long-lost friends, then Della notices Macy)

DELLA: How’s your daddy?

JEN: He’s good! He got a boat! He named it Debra after Mom . . . (Pg 22-25) OH! When do you go on the show? (to Macy) Della’s about to be a contestant on The Big American Bake-Off!

DELLA: Six weeks I’m going! But get this, once I get there I am sworn to SECRECY. I can’t tell anyone if I won or not ‘til they air it!

JEN: Well, I’m gonna watch you every week and cheer you on.

DELLA: Thanks, sweetheart, we’ll see, we’ll see. I’m trying not to think about it! So, what’re you up to this visit? (Jen waves her engagement ring so Della can see) You’re getting married?! AHHHHHHHHH! (Screams in excitement)

JEN: I know!

DELLA: I didn’t even know you were seeing anybody, why didn’t you tell me! Lemme see that diamond, girl, gimme that bling. It’s a beautiful ring. So you’re doin’ it down here?

JEN: Yup!

DELLA: Your mama is dying all over again right now!! She is watching and she is so stinkin’ mad she is not here. I am gonna make your cake! Now what’re your colors?

JEN: Emerald and midnight blue.

DELLA: Well, I wanna hear all about him! (Jen panics, looks to Macy) . . .

JEN: (Pg 21) This is my – this is Macy. She’s with me.

DELLA: (Pg 23-24) . . . Beg pardon? (Della realizes what Jen is saying) . . . Oh!

JEN: Macy’s my . . . I’m sorry to spring it on you, but – yeah! So . . .

DELLA: (Trying) Well, congratulations to you two. When, ah. When is the wedding?

JEN: I didn’t want a super long engagement, so we’re just kind of throwing it together. [Six months]. (She senses Della’s discomfort. It kills her)

DELLA: Well . . . October, is it?

JEN: I know it’s late notice . . . I – I shoulda called. (To Macy) She gets a lot of orders. (To Della) If you don’t – I’m sure you’re super busy –

DELLA: You know what, I am so sorry, but you’re right. I think I am all backed up, around that time.

JEN: It’s okay – I understand . . It’s fine, it’s so fine, we can get it somewhere else . .

DELLA: It’s not – because – it’s just I have a lot - I am so sorry –

JEN: (Humiliated) No, I’m sorry, it’s totally fine, its . . .

DELLA: Stop by again and see me, whenever you . . .

JEN: . . . Definitely (Macy and Jen leave the shop) ***** Later that night ******

MACY: (Pg 35-36) She’s wrong. The Cake Lady.

JEN: Della . . she has every right to say no if she’s not comfortable.

MACY: She is wrong.

JEN: She doesn’t think she is.

MACY: Look at me. . . SHE IS WRONG.

JEN: (Jen is quiet, puts her head in her hands, a long pause) I shouldn’t’ve gone there. You shouldn’t’ve seen that.

MACY: (Softly) What’d you think was going to happen?

JEN: I had this whole speech prepared. I had lines. I was going to say them to her. I kept imagining myself saying it, all calm and confident. But then I saw her face. And I just. I couldn’t. I feel like such a tiny piece of shit.

MACY: You’re not shit. You’re hopeful.

JEN: Hope is stupid. (defeated)

MACY: . . . You could change her.

JEN: Della? No, thank you.

MACY: But if you don’t push her to change then they never will . . .

JEN: They?

MACY: All of them.

JEN: I’m not talking about all of them. I am talking about one person, who I love, who I know.

MACY: I’m just asking – do we really have to do this here?

JEN: YES. My mom wanted me to get married here. Yes. We have to.

MACY: We do not “have” to do anything, okay? We are shoving ourselves through some narrow system that was not even designed to support us!

JEN: All I ask is that you just try and be respectful of the people down here.

MACY: . . . I don’t respect these people.

JEN: . . . But I’m one of them.

MACY: No . . . you’re not

JEN: (Softly) I kinda am. ****** The next day*******

(Jen returns to Della’s Cake Shop by herself)

JEN: (Pg 39-41) You still open?

DELLA: Where’s your . . . . ?

JEN: She’s at Starbucks. She thinks I’m looking at [wedding] favors. Which is of course my next stop. (long awkward silence) I’m sorry I haven’t been down. As much.

DELLA: Oh, sweetie, that’s alright. You got your life up there . . A whole other life. (Beat. She tries) How, ah. Is your daddy excited about the wedding?

JEN: He’s trying to be. (awkward silence) (Pg 42) I totally get it. I don’t want you to think that I don’t get it. Why you can’t – why you’re too busy.

DELLA: I am so sorry, I looked again, and October is just going to be impossible

JEN: Della. It’s okay. (Pg 44) I know you don’t think it’s right.

DELLA: What do you think?

JEN: . . . That I love her. But I can’t stop wondering how my mom would feel.

DELLA: Sweetie . . .

JEN: I keep ignoring it, but it’s a question. (Beat) What do you think she would’ve said? . . . Just tell me. Please. What she would think. (Beat)

DELLA: (Pg 46) It’s – It’s not what God intended . . . (Pg 44) I think it would break her heart. (This stabs at Jen. It kills her)

JEN: . . . Yeah (Tears come. She fights them, but can’t keep them back) **** Cut away to Macy, speaking to the audience ******

MACY: (Pg 45) She’s really a good person. She’s warm and she’s giving and she won’t ever think of herself first. Sometimes I just want to shake her, think of yourself, it comes so naturally to everyone else, but she won’t eat until everyone is fed. When I get a cold she makes me garlic tea even though she hates garlic, it makes her gag. When her mom was sick she dropped everything and moved back down here. . . . She has nightmares she’s falling into flames . . . Because of people like . . (Pg 48) Jesus, I am so tired of tolerating this. I am so tired of being nice. Why do you hate me?! (She starts to tear up) Why . . . why . . . why. ****** Back to Jen and Della in Della’s Cake Shop ********

JEN: (Pg 61-62) (Composing herself) I used to have nightmares. I said goddamn in front of my mom and it made her skin melt off her face. That’s how scared I was. Of a WORD. She’s been gone almost five years and I’m still terrified of disappointing her. That’s on me

DELLA: (Gently) (Pg 47-48) It’s just the way I see it – and I’m just trying to explain – if God intended everybody to love on everybody, there would be means . . . The Bible made it very clear. (Firmly) It’s God’s WORD. He says so, in Romans 1:26. *

JEN: (Pg 62-63) (completely distraught) Macy’s the only person I ever loved. I tried not to love her, but I do. She is beautiful and she’s wonderful and she’s strong. We’re a family. And I pushed her away because I am so ripped in two. I am straddling two worlds. . . I’m so SICK of being scared.

DELLA: (Heart breaking) Jenny . . . . I would love more than anything, truly anything in this world, to make your cake. But . . .

JEN: I don’t need you to make me a cake. I need you to love me.

DELLA: I do love you. I have really been searching through my heart. But I just. I can’t support. What you’re doing. I am so sorry to say that.

JEN: I tried not to love her. But I do. I love her so much, I love her . . .

DELLA: I know, sweetie. But still. It just - does not sit right with me. (Beat)

JEN: Well, then I don’t know if I can have you in my life anymore.

DELLA: Oh, no, sweetie – please –

JEN: No, I think that’s how it’s gotta be right now.

DELLA: (closes her eyes. Lets it sting) I am very sorry to hear that.

JEN: Me too. (Neither is sure what to do.) . . . Bye, Della. (Jen leaves. And Della stands alone, the breath knocked out of her)
```

---

## IC-0569: Carrie

- Title: Carrie
- Author (byline): Stephen King
- Work: Not specified
- Publisher: Pocket
- Publication date as stated: Nov 2002
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MARGARET, CARRIE, MARGARTE
- Teaser before the introduction: No
- Spoken words (computed): 961
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephen King
ISBN: 978-0671039721
Publisher: Pocket
Date (Month/Year): Nov 2002
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Carrie White’s mother Margaret White gave birth to her daughter September 21, 1963 under circumstances that can only be termed bizarre.

ACTRESS 2: In fact, an overview of the Carrie White case leaves the careful student with one feeling ascendant over all others: that Carrie was the only issue of a family as odd as any that has ever been brought to popular attention.

ACTRESS 1: We know that Carrie was the victim of her mother’s religious mania

ACTRESS 2: We know that she possessed a latent telekinetic talent, commonly referred to as TK.

ACTRESS 1: How apparent was Carrie's “wild talent” and what did Margaret White, with her extreme Christian ethic, think of it?

ACTRESS 2: We shall probably never know. But one is tempted to believe that Mrs. White's reaction must have been extreme . . .

TOGETHER: Carrie by Stephen King
```

### Performance text (classify this)

```text
Dinner time at the White’s house . . .

MARGARET: You haven’t touched your pie, Carrie. It’s homemade.

CARRIE: It makes me have pimples, Momma.

MARGARET: Your pimples are the Lord’s way of chastising you. Now eat your pie.

CARRIE: Momma?

MARGARET: Yes?

CARRIE: I’ve been invited to the Spring Ball next Friday by Tommy Ross -- (Margaret stares at her with wide my-ears-are-deceiving-me eyes. Her nostrils flare. Carrie gets a lump in her throat and is visibly afraid) – and he’s a very nice boy. He’s promised to stop in and meet you before and . . .

MARGARET: No.

CARRIE: -- to have me in by eleven. I’ve –

MARGARET: No, no, no!

CARRIE: --accepted. Momma, please see that I have to start to . . . to try and get along with the world. I’m not like you. I’m funny – I mean the kids think I’m funny. I don’t want to be. I want to try and be a whole person before it’s too late to . . . (Margaret throws her tea in Carrie’s face and sits trembling. Her face frozen except for her nostrils which continue to flare. Abruptly she throws back her head and screams at the ceiling)

MARGARET: God! God! God! (Carrie does not move. Margaret hands hook into shaking class. Her face is half-mad – compassion mixed with hate). The closet. Go to your closet and pray. And God made Eve from the rib of Adam. Let us pray. Let us pray to Jesus for our woman-weak, wicked, sinning souls.

CARRIE: (sobbing quietly) Momma . . .

MARGARET: And Eve was weak and loosed the raven on the world, and the first Sin was Intercourse, And the Lord visited Eve with a Curse, and the Curse was the Curse of Blood. And Adam and Eve were driven out of the Garden and into the World and Eve found that her belly had grown big with child.

CARRIE: Momma! Momma, please listen. It wasn’t my fault! . . . You should have told me!!

MARGARET: O Lord, help this sinning woman beside me here see the sin of her days and ways. Show her that if she had remained sinless the Curse of Blood never would have come on her.

CARRIE: No: Let me go!

MARGARTE: Show here that this is Your kind, vengeful hand at work and Your sign that she must walk the straight and narrow from her on out if she is to avoid the flaming agoinies of the Eternal Pit. Amen . . . (a beat then quietly) Boys. Yes, boys come next. After the blood the boys come. Like sniffing dogs, grinning and slobbering, trying to find out where that smell is. That . . . smell! (She swings her whole arm into the blow and slaps Carrie’s face. Carrie remains seated although her upper body sways. The mark on her check is first white, then blood red.) The mark . . . (Her eyes are large but blank. She is breathing rapidly and seems to be talking to herself as she pulls Carrie out of her chair). I’ve seen it, all right. Oh, yes. But. I. Never. Did. But for him. He. Took. Me . . . .

CARRIE: (Terrified) Momma . . .

MARGARET: In cars. Oh, I know where they take you in their cars. City limits. Roadhouses. Whiskey. Smelling . . . oh they smell it on you! (her voice rises to a scream. Tendons stand out in her neck and her head twists in a questing upward rotation)

CARRIE: Momma, you better stop. (Margaret snaps back to some kind of hazy reality)

MARGARET: The closet. Go to your closet and pray.

CARRIE: No. (Momma raises her hand to strike) No! (her hand stops in the dead air – Carrie is controlling it with her TK) I’m going, Momma! (Margaret drops to her knees with her hands over her head)

MARGARET: (moaning) Devil’s child. Devil’s child. Satan spawn . . .

CARRIE: Momma, stand up.

MARGARET: lust and licentiousness, the cravings of the flesh . . .

CARRIE: Stand up! (Margaret’s voice stops, but she stand with her hands still on her head, like a prisoner of war. Her lips move as if reciting the Lord’s Prayer) I don’t want to fight with you, Momma. (her voice breaks, but she tries to control it) I only want to be let to live my own life. I . . . don’t like yours. (She stops – horrified – she has spoken the ultimate blasphemy)

MARGARET: (Whispering) Witch. It says in the Lord’s Book: Thou shalt not suffer a witch to live. Your father did the Lord’s work . .

CARRIE: (her mouth trembling) Momma

MARGARET: I should have killed myself when he put it in me. After the first time, before we were married, he promised. Never again. He said we just . . . slipped. I believed him. I fell down and I lost the baby and that was God’s judgment. I felt that the sin had been expiated. By Blood. But sin never dies. Sin . . . never . . . dies!

CARRIE: (dropping to her knees and rocking herself for comfort. She has heard this ranting story before) Momma. I . . .

MARGARET: At first it was all right. We lived sinlessly. We slept in the same bed, belly to belly sometimes, and o, I could feel the presence of the Serpent, but we . never did . until . (Margaret begins to grin, a hard, terrible grin) And that night I could see him looking at me That Way. We got down on our knees to pray for strength and he . . . touched me. In that place. That woman place. And I sent him out of the house. He was gone for hours, and I prayed for him. I could see him in my mind’s eye, walking the midnight streets, wrestling with the devil as Jacob wrestled with the Angel of the Lord. And when he came back my heard was filled with thanksgiving.

CARRIE: Momma, I don’t want to hear it!

MARGARET: It wasn’t until he came in that I smelled the whisky on his breath. And he took me. Took me! With the stink of filthy roadhouse whiskey sill on him he took me . . and I liked it! (screaming out the last words at the ceiling)

CARRIE: MOMMA! (Margaret breaks off as if slapped and blinks at her daughter. She continues in a more normal tone of voice.)

MARGARET: I almost killed myself. And Ralph wept and talked about atonement and I didn’t and then he was dead and I thought God had visited me with cancer; that he was turning my female parts into something as black and rotten as my sinning soul. But that would have been too easy. The Lord words in mysterious ways His wonders to perform. I see that now. When the pains began I went and got a knife (picks up a carving knife from the dinner table) this knife (holds it up) and waited for you to come so I could make my sacrifice. But I was weak and backsliding. I took this knife in hand again when you were three, and I backslid again. So now the devil has come home. (she holds up the knife her eyes fastened hypnotically on the blade)

CARRIE: It’s not right, Momma. It’s not . . .

MARGARET: Let’s pray. For the last time, let us pray!

CARRIE: Oh, Momma help me! (Carrie bows her head in prayer as Margaret lifts the knife to bring it down in a shining arc. At the last moment, Carrie jerks back and once again controls her mother’s descending hand with the power of TK. Her hand stops in mid air. They stare at each other in silence, then Carrie speaks softly) I’m going to give you a present, Momma.

MARGARET: What are you doing?

CARRIE: I’m picturing your heart, Momma. It’s easier when you see things in your mind. Hour heart is a big red muscle. Mine goes faster when I use my power. But yours is going a little slower now. Slower. Things are going to change around her, Momma. (Margaret is whispering to herself again – it is not the Lord’s Prayer. It is the Prayer of Exorcism from Deuteronomy). Slower, Momma. Do you know what the present is, Momma? What you always wanted. Darkness. And whatever God lives there.”

MARGARET: (whispering, having difficulty breathing) Our Father, Who art in heaven . . .

CARRIE: Slower, Momma, Slower. MARGARET . . . hallowed by They name . . .

CARRIE: I can see the blood draining back into you. Slower.

MARGARET: . . . Thy kingdom come . . .

CARRIE: Your feet and hands like marble, like alabaster. White.

MARGARET: . . . Thy will be done . . .

CARRIE: MY will, Momma. Slower.

MARGARET: on earth

CARRIE: Slower

MARGARET: as . . . as . . . as it . . . (she collapses, hands twitching) as it is in heaven

CARRIE: (whispering) Full stop. (Carrie gradually comes back to her senses and notices her mother on the ground – she crumples into tears over her mother’s dead body)
```

---

## IC-0570: Chiaroscuro

- Title: Chiaroscuro
- Author (byline): Lisa Dillman
- Work: 35 in 10: Thirty-five Ten-minute Plays
- Publisher: Dramatic Publishing
- Publication date as stated: 2005
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JEN, MOTHER
- Teaser before the introduction: No
- Spoken words (computed): 1479
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lisa Dillman
Book: 35 in 10: Thirty-five Ten-minute Plays
ISBN: 1583422838
Publisher: Dramatic Publishing
Date(Month/Year): 2005
```

### Introduction (context only: never use it for content warnings)

```text
Chiaroscuro is a term in art for a contrast between light and dark. The term is usually applied to bold contrasts affecting a whole composition. From the perspective of Lisa Dillman, it is the perfect word to describe the before and after of Alzheimer’s Disease.

When Alzheimer's disease begins to destroy brain cells, no outward symptoms are evident. After a while, small memory lapses appear and grow more serious. The afflicted individual may forget the names of familiar people or places, the words to express what they want to say, or the location of everyday objects. For a mother and daughter who built their relationship on the power of words, the loss of verbal ability is even more devastating. Chiaroscuro by Lisa Dillman
```

### Performance text (classify this)

```text
JEN: In the beginning. A woman with red, red lipstick and a voice full of jumps and trills and wonder tells me story after story night after night.

MOTHER: “ . . . Soon the princess came to a clearing in the woods. And there, hunched upon a craggy stump, sat a gnome of questionable breeding. He had a wart the size of an egg on the tip of his nose and he was hairy from top to toe. Some might call him matted. He took one look at our princess and found her so enticing that for a moment he was tempted not to put a curse on her. But alas! Evil gnome tradition won the day. ‘Oh, thou pretty aimless wench. Sit ye on my splintery bench. Bethink all words ye’ve spake before. From this day on ye’ll speak no more.’”

JEN: Later . . . She and my stepfather yak away all through dinner – their conversations, their banter erupting out of them, surging, blasting, spluttering. They warble. They chortle. They tease. They research and excavate each other’s day. Words are king and queen and the rest of the royal family too. Words are the real food; what’s on their plates is just an excuse. During a pause that many wouldn’t recognize as such, I break in. “Hey, what’s that? What’s chiaroscuro?” They look perplexed for a moment – Did you just hear something? What was that sound? -- and, squinting, tell me I’d better just go look it up.

MOTHER: Keep up or give up.

JEN: I begin bringing the dictionary to the table with me. With the extra four inches, I am almost as tall as they are. It’s massive, a weighty tome – an abridged OED. Abridged, yes, but that’s OK by me – it’s the perfect height and I like the elevation. I hop on and off it at will, finding, then absorbing the words. The words. Torrents, deluges of them. Great avalanches and whirling siroccos of words. Words all day and late into the night. I believe God invented sleeping just to shut us up a while. Later . . . We play Poem-itation.

MOTHER: Whose socks these are I think I know . . . She’s chucked them on the sofa though. (Barest pause.)

JEN: But Ma won’t mid I leave them there . . . Since I’m a lazy so-and-so.

MOTHER: And yet she does not think it queer . . . To always lob her socks right there.

JEN: One: split infinitive. Two: Frost is too easy. And while we’re at it, Gray’s Elegy blows big juicy chunks.

MOTHER: There stands and sneers the tiny-minded queen . . . it’s true she knows it all at age thirteen . . .

JEN: I’m only twelve.

MOTHER: Don’t mess with meter (Regroups.) Tom Gray is not a chucklefest, it’s true . . . Still, he’s a well-loved poet, unlike you.

JEN: Talk is incessant. Silence means you have nothing to say. Of course there are things we don’t talk about. (She sneak a glance at Mother, who stands rubbing her temples gently, in obvious pain.) And times when all talk suddenly ceases for days on end. And question marks bank up in the corners of the rooms. When my mother wanders the house noiselessly through the night. Then sleeps in patches through the following day in her shaded room, with the door closed and locked. And if I have to ask her something . . . (She taps the floor lightly with her foot – a knock)

MOTHER: What?

JEN: Absolute specificity is vital. Or she will whimper and gnash at her pillow. (Beat. Then with great deliberation). I was hoping I could borrow your car. For tonight. To leave approximately seven p.m. and return at midnight or before. With no driving over sixty-five miles per hour on the highways - - certainly much less than that on the byways – an no alcohol or drug consumption taking place during the hours the car is entrusted to my care (Beat.)

MOTHER: Take it.

JEN: Later . . . My stepfather takes his leave. Conversation-wise he’d already been gone a while. Dinners had become cacophonous with the sounds of mastication – his and mine, usually, since my mother was so often among the disappeared. His voiceless but very present wish to be elsewhere sucked all words out of the dinner hour. I took the opportunity to catalog his faults. His baldness. His lack of energy. His haunted, hopeless eyes. His habit of sniffing the back of his hand. Obsessively. But most of all, his silence. There he sat – balding, sniffing inertia personified. A husk. Then on e evening he didn’t come to the table. And soon it was apparent he’d cleared out for good. Later. . . My mother returns to the world. She drinks more wine than before. We play Limerick Impromptu.

MOTHER: There once was a man from Toledo . . . Who looked awfully good in his Speedo . . . He’d prance all around . . . Then pull the thing down . . While the ladies all swooned, “Oh how neato!”

JEN: Aren’t you bawdy.

MOTHER: Limericks are traditionally filthy. I cleaned it up because we’re eating. Your turn. Go ahead.

JEN: I’d rather not.

MOTHER: Oh, come on!

JEN: There once was a mom from Seattle . . . About the male member she’d prattle . . . She’d slurp up her wine . . . Then sit there and pine . . . ‘Cuz finding a man’s such a battle.

MOTHER: There once was a mean, heartless daughter . . .

JEN: Yes?

MOTHER: That’s enough for tonight. Consume your comestibles, you.

JEN: Meaning she’s had enough to drink that the necessary end rhymes would be an impossible feat. Meaning I hurt her feelings. Meaning something else too. Something so integral to our relationship that I can’t name it until years later: I bore her. The occasional limerick is a poor replacement for densely layered stories from the heady landscape of my school day. Since she can build an epic out of a fifteen-minute to the grocery store, she can’t see why I don’t do the same. She figures that I must be living the life of a veritable Candide out there in the world. And what a withholding little gob-shite I am for not laying out the rich tapestry of my misadventures. The truth is I’m not picaresque. And words don’t thrill me anymore.

MOTHER: Oh, Jen! Tell Marcia about that Dickensian math teacher of yours! She does a drop-dead impression of this guy, Marcia. Go on, honey. Tell it.

JEN: You tell it. (Mother turns away. With great animation she silently mimes the impression and tells the story.) And then she does. And she tells it better than I could have. And she imitates the math teacher – she’s only met him once – better than I can after having sat in his class a semester and a half.

MOTHER: I’ve just about decided you’re shy.

JEN: Well, I’m not.

MOTHER: You won’t let anyone know you.

JEN: You know me.

MOTHER: Is that true, sweetie? Do I know you? (Beat.)

JEN: Don’t you? (Beat.) Later (Beat.) Years later. I am home. Alone. It’s been a long day. My feet hurt. I’m on my third glass of merlot. The phone.

MOTHER: It’s me.

JEN: Hello, you.

MOTHER: Listen . . . do you . . . ? What does splungeree mean?

JEN: Umm. Something to do with exploring caves?

MOTHER: I’m not sure.

JEN: Well, where di you hear it? Give me some context.

MOTHER: I went to the door to see the postman today, and when he forked over my mail I said to him, “Oh, nuts. Just a bunch of splungeree.” (Jen laughs). I couldn’t think of the word for catalogs. I was standing there with a fistful of the things and I couldn’t think of the word. Splungeree. I went inside and wrote it down. I had to sit and meditate to get the word catalog to come back to me. It was floating out there in the mist for such a long time.

JEN: Later.

MOTHER: It happened again.

JEN: We began to keep a list. We call it the List in the Mist. Splungeree. Altocram. Zlit. Oppley.

MOTHER: Eggoline. Fedabush. Croomuttle.

JEN: Hohorgan. Denkaptu. Argenbach. Joroist.

MOTHER: Cabblefan. Chickley. That thing you boil water in. The trattalot. I can’t remember anything. I burned the bottom out of my trattalot this morning.

JEN: We play List/Mist/Gist (Reciting.) In last week’s o’erlooked splungeree . . . I found a trattalot . . . I knew it was the one for me . . . I’d wrecked my old teapot.

MOTHER: A teapot . . the word comes to me . . . not always, but just now . . .

JEN: I long to make a spot of tea . . . But I’ve forgotten how (Beat.) Later. A specialist informs her she’s suffered a series of tiny strokes. Probably over a period of years. Painless. But finally measurable.

MOTHER: Don’t let me get away with anything. Correct me. Tell me what it’s supposed to be.

JEN: Yes. I will . Later . . . She gives up driving and spends most of her time in her garden. Her conversation for the most part makes sense. But she speaks in facts now.

MOTHER: It’s your. Birthday. I sent you a card.

JEN: And then there are the holes. The ones less and less-often filled by even her transitory invented language.

MOTHER: Today I . . . ssssssss. . . I . . . ohhh. Nothing.

JEN: I think of her often just before sleep But she is young and her red, red mouth is a vivid patch in perpetual motion. I see her take a step away from me. Waving. And then another. Still waving.

MOTHER: The lilacs. Are early this year.

JEN: And the mist rolls up around her feet. She is blurred around the edges. But still she is waving.
```

---

## IC-0571: Code Broken

- Title: Code Broken
- Author (byline): Olivia Cline
- Work: Code Broken
- Publisher: SpeechGeek
- Publication date as stated: 2019
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2217
- Already set (do not supply): none

### Source block (context only)

```text
Code Broken by Olivia Cline
ISBN: 978-1-61387-117-1
Copyright 2019 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2019, is identical to the printed published
version of this same publication dated 2019. This statement along with the entire printed
PDF of this publication must be presented at any National Speech and Debate Association
District or National event for the script to comply with NSDA rules per the request of the
Executive Director.
This and other selections of quality performance literature for competitive oral
interpretation are published by SpeechGeek.
For more information and performance rights, contact SpeechGeek.
SpeechGeek
248 Arlington Park Dr.
Hot Springs, AR 71901
Phone: 1-888-742-2028
Email: thegeek@speechgeek.com
Web: www.speechgeek.com
Facebook: www.facebook.com/speechgeek
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
JANE. (sings) Send him victorious! Happy and glorious! Long to reign

over us; God save the king! All right, Bethy? You look like you’ve

seen a ghost.
BETH. Jane? Get in here before someone sees you!
JANE. This your house? Lovely.
BETH. What are you doing here?
JANE. What? Can’t I stop in for a hello? Just two old mates catching up.
BETH. Two old mates from where? Jane, you’re not supposed to be here.
JANE. Afraid Pete’ll come home and start interviewing me from whence

and wheres we met? BETH. No. Pete won’t be home ‘til half seven. But my kids will be in an

hour. JANE. Kids? That’s brilliant. Didn’t waste any time, did ya? Soon as the

war was over you started “celebrating.” BETH. Don’t be crude. We have a boy and a girl, 8 and 7. (beat) Jane,

it’s been years. What do you need?
JANE. To talk.
BETH. About what? What could you and I have to talk about anymore?
JANE. All of it. Us. The war. Bletchley Park.
BETH. No. We’re not allowed to talk about it.
JANE. What? You and I both already know about it. It’s not like we’re

revealing ultra-secret government information; we’d just be, like,

reminiscing about ultra-secret government information. BETH. Why? JANE. I just need to! I just need to know it happened, that I’m not crazy. I

can’t talk to anyone else. BETH. I know what you mean. You’re not crazy. JANE. You and me. We was there—important. We helped win the war. BETH. The war is over, Jane. It ended a long time ago, remember? JANE. Oh believe me, I remember.

While our traditional view of WWII is one of a war fought by men with tanks, U-boats, and bombs, there is another side to history. The women who contributed to military intelligence played a crucial role in winning battles, intercepting information, and breaking top secret Nazi codes. And no mission was more secret or more important in 1940’s Britain than Bletchley Park. Hundreds of women worked tirelessly as code breakers to decipher Nazi messages and save lives. However, at war’s end, these heroic women were sworn to secrecy, only allowed to reveal their involvement 30 years after the fact. Playwright Olivia Cline attempts to decipher the contributions and costs of their silent legacy asking the question: if history erases someone, can we still appreciate their contribution? Code Broken by Olivia Cline, based on the BBC interviews of Fiona Bruce.

TRANSITION TO 1954

JANE. Cup of tea? BETH. Of course. So, what happened? I tried to imagine you were just

off seeing the world and got lost in your adventure. Then you

stopped sending the postcards. They just...stopped. JANE. What was the point? You weren’t coming.

BETH. The last one was from Africa. Where else did you go?
JANE. All the places we talked about.
BETH. Was it how we thought? The big adventure?
JANE. A lot of chasing.
BETH. Chasing?
JANE. Yeah, chasing. Chasing work, chasing money, chasing men.
BETH. Sounds glamourous, all that freedom.
JANE. Does it? You didn’t used to fancy such... abandon.
BETH. (pours the tea)
JANE. What’s this then? Sunday Times Codebreaker puzzles. Old habits,

die hard, eh?

TRANSITION TO 1942

BETH. (trying to get someone’s attention) Excuse me? Pardon me. I’m

looking for... Hello?
JANE. You look lost. Where are you headed?
BETH. I’m...I don’t think I am permitted to say.
JANE. Right. Is that your assignment letter? (steals the letter)
BETH. Hey! Give that back!
JANE. “Ms. Elizabeth Caldwell.” From Chelsea. How posh!

Commissioned civilian brigade. How did they commission ya,

then?
BETH. I... I won a contest, in The Times. A puzzle.
JANE. So you’re a brain, are ya?
BETH. No. I mean, maybe. They just told me to come here.
JANE. And you always do what you’re told. I see. Well, you’re in luck,

Bethy. You’re in Section G. With me, please.
BETH. Elizabeth. And what is section G?
JANE. Told you nothing, did they?
BETH. Not a thing. I got a that letter in the mail along with a rail pass. I

haven’t the faintest idea what a girl like me could possibly do for

the British Royal Naval Service.
JANE. Codebreaking.
BETH. I beg your pardon?
JANE. We break German codes. Well, we try to.
BETH. German codes? Does that mean we can help...people?
JANE. You got a sweetheart, eh? On the front?
BETH. Pete. We were going to get married. Are. We are going to get

married. JANE. Uh-huh. BETH. Then we’ll live with his mother in Chelsea and start our family

straight away.
JANE. Of course you are.
BETH. You’re making fun?
JANE. ‘Course I am. Well, just you wait. By the end of this, Pete’s gonna

bash de Fuhrer’s face ‘til he gone look like a shriveled raisin

bulldog mess. BETH. ...I think he already does look it.

JANE. Bethy...we’ll get along fine.

TRANSITION TO 1942

JANE. (comes in smoking a cigarette) Ugh. Why you listening to that

rubbish?
BETH. I’m working.
JANE. Working, my bum!
BETH. I hate listening to it, but I feel like I need to.
JANE. Need to?
BETH. It’s ridiculous. It’s not as if I’m going to hear about Pete on this

thing, but still... JANE. Hey, we only get a fifteen-minute break, no sense spending it in

tears. Come on, Bethy. Your nose is going to stay shriveled like

that if you don’t learn how to have a little fun! BETH. Yes, Sergeant Major! We were uhh...just taking our fifteen, sir.

Smoking? No, sir. No smoking allowed in the house, we know

that. Would you like to smell my breath? Yes, we will have those

done for you by end of day, sir. Very good, sir. JANE. (trying not to let smoke out of her mouth) God save the king. (they

watch him leave and dissolve into laughter)
BETH. I thought we’d had it for sure! If your smoking gets us sacked...
JANE. Us? Never! They need us too much.
BETH. They need codebreakers. They don’t need us.
JANE. (sarcastically) Right. Beth you’re the most brilliant girl here. With

your brain, we could have the whole world.
BETH. How did you get here?
JANE. Back stairs. They never check this time of day.
BETH. No, I mean here—Bletchley.
JANE. Oh, well, I volunteered.
BETH. You did? Wow. You must be very brave. Didn’t you worry they

would send you to the front? As a nurse or secretary?
JANE. No. I signed up for an adventure.
BETH. But as a woman—
JANE. The way I see it, war’s the best time for women. Men stop looking

at your chests and start letting ya get your hands dirty. This war

ain’t just about beatin the Germans, Bethy. This war is about

beatin’ the old way of life. Wherever that takes me is alright.

What about you? I mean, you’ve obviously thought a little about

what would happen if...you needed to…start over. BETH. You mean if Pete doesn’t come home. JANE. Sure. Or maybe you decide that you’re meant for a bigger life

than housework. What then? BETH. I’ve never thought of any other kind of life. Until now. Is that awful

to say? JANE. No, not awful. But you know we can do it, Bethy. Together we can

change the world. BETH. Just like my Pete... Well, come on then. Give us a smoke.

TRANSITION T0 1954

BETH. Please, don’t light that. Pete can’t stand the smell of smoke. Too

many bad memories, he says. JANE. Well. Wouldn’t want to put Pete out of temper. Tell me, did

you...ever tell him? BETH. About Bletchley? No. And he doesn't ask. JANE. Of course he doesn’t. But I’m sure you know what he did in the

war.
BETH. He was artillery.
JANE. Lucky him.
BETH. Pete suffers a great deal from his time in the war.
JANE. We all do.
BETH. I think it’s different.
JANE. It is different. They did the fighting. We were the heroes.
BETH. That’s...a subversive opinion.
JANE. Why? Didn’t women make the bullets that he fought with, send

the supplies that saved his life again and again? Didn’t we

provide the key to his success? BETH. Very well, you’re right. We all did our part. JANE. And you’re right. It’s not the same. Pete can talk about it any

bloody time he wants. But if I even try to whisper the word

Fallschirm— BETH. Don’t. JANE. —that happens. You would think it was our greatest shame. Our

greatest shame that we were brilliant, too.

TRANSITION TO 1944

JANE. 2311 542 227 BETH. I...R...M. That’s...that’s impossible. JANE. What? (takes the paper, tries to read it) Oh for God’s sake, I’m

rubbish at German! BETH. It says that the division transfers to Fallschirm on the 3rd. JANE. Fallschirm. There’s not a city in Germany named Fallschirm. BETH. It’s not a city. It’s a luftwaffe panzer division. Jane, if the cypher’s

correct, then we know where the German army is going to be in

thirteen days’ time.
JANE. Bloody hell. You’re a genius.
BETH. We need to tell the Sergeant Major. The Colonels!
JANE. After this we should be the Colonels!
BETH. My god. Not bad for two ordinary girls.
JANE. Ordinary girls? I couldn’t be ordinary if I tried.
BETH. No, you certainly couldn’t.
JANE. This could be our ticket, Bethy.
BETH. To what?
JANE. Who knows? They see this and they start thinking them two girls

got it figured out. Send them to Whitehall in London, the West

Indies, Australia, Somaliland! And we’ll go won’t we? We’ll see

the whole world!
BETH. But don’t you want to go home?
JANE. Of course not! That’s the whole point, isn’t it?
BETH. The point was to win the war—to get our boys back safe. Then we

go home. JANE. Right. But surely they won’t just let us go home, after we’ve made

such an important contribution. Wait ‘til I tell mum.
BETH. No. Jane. The Secrets Act, we signed it.
JANE. So?
BETH. It means we won’t talk about it, not for 30 years.
JANE. Alright, so I won’t tell mum. But she’ll figure it out when she gets

the postcard from Africa. Maybe I’ll even sign it Eunice

Dankworth, Royal Naval Services. She’d die.
BETH. No, Jane. I’m not going to Africa.
JANE. What about our plans to see the world?
BETH. Those were never my plans.
JANE. So that’s it then? You’ll go home and marry Pete. Whatever’s left

of him. BETH. Don’t say that. JANE. You’ll become some dull, empty-headed housewife and never do

nothing else? BETH. I’ll get what I wanted. JANE. How can that be what you want now that you’ve seen what you

can do? You’d rather be used as a baby factory or— BETH. —as someone’s ticket to adventure-land? You only care about

yourself and your plans. You’ve only wanted me along because

you’re not smart enough to do this on your own. JANE. I’ve been a good friend to you since day one, Bethy. You know

what, fine. Stay here. I hope you enjoy your worthless life. I’m

going to get what I wanted. BETH. I hope you enjoy your adventures alone.

TRANSITION TO 1954

BETH. I never forgave you for leaving. JANE. I never forgave you for staying. BETH. But you had your adventure—you traveled to all those amazing

places. JANE. I was chasing after an adventure we'd already had, that we could

never top, and could never speak of. BETH. What was so wrong with wanting a normal life? This. Here. My

family. They are my adventure. But that was never good enough

for you. JANE. What was so wrong with wanting more? With wanting some

respect and recognition for winning the damn war! BETH. You want credit? You want a title? Well congratulations, god save

Queen Jane! JANE. They used us, Beth. And then they shut us up. BETH. No. We did our part. We were sworn to secrecy!

JANE. We were sworn to invisibility! Then they stole our purpose. BETH. I still have purpose. JANE. What? Wiping arses and making roasts? You’re happy with that? BETH. Of course I’m not happy! I’m miserable! But what am I supposed

to say? That I miss the war? That I hate my life? That I’ve already

tried to end it twice? But you already know what they feels like,

don’t you? JANE. Bethy… BETH. Don’t! I’ve no use for your pity. But you left me...you were gone.

And now I’m just some crazy person whose house is filled with

ghost stories. This is the way things are. And it’s not perfect. And

it’s not wonderful. But at least we aren’t all speaking German.
JANE. ...I’m rubbish at German.
BETH. I know.
JANE. I am so sorry. I had no idea.
BETH. I know you think they took away our meaning. Ordinary is—
JANE. —not enough.
BETH. It’s what we fought for though, isn’t it?
JANE. How do you mean?

(door opens) BETH. Ah, there you are. Hello darlings… Wash up before tea. And,

Janey, you’ve forgotten your puzzle (hands her the Sunday

Times).
JANE. She’s doing the puzzles now?
BETH. (nods) I save them all for her. She’s brilliant.
JANE. ‘Course she is.
BETH. Her teachers think she has quite a bright future. We did that.

She...is what we fought for... JANE. Not bad for two ordinary girls. BETH. Not bad at all.
```

---

## IC-0572: Commencing

- Title: Commencing
- Author (byline): Jane Shepard
- Work: Kickass Plays for Women
- Publisher: Samuel French, Inc.
- Publication date as stated: Nov 2008
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: KELLI, ARLIN
- Teaser before the introduction: Yes
- Spoken words (computed): 1895
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jane Shepard
Book: Kickass Plays for Women
ISBN: 978-0573663437
Publisher: Samuel French, Inc.
Date (Month/Year): Nov 2008
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Gay, Bi-sexual, Transgendered

ACTRESS 2: Some people would like you to believe that if you belong in one of these categories, you are too different from the rest of us to be accepted. You require some very important restrictions:

ACTRESS 1: You shouldn’t be able to join the military

ACTRESS 2: You shouldn’t be able to get married

ACTRESS 1: You shouldn’t be able to adopt a child

ACTRESS 2: You just shouldn’t . . . be

ACTRESS 1: But what if it were possible to focus on our similarities rather than our differences?

ACTRESS 2: What if it were possible to see each person for who they truly are rather than seeing only a label?

TOGETHER: Commencing by Jane Shepard
```

### Performance text (classify this)

```text
(A knock on the door. KELLI hurries out, putting on earrings. She checks her watch, her look, grabs jacket, answers door. SHE stops. A WOMAN in a parka stands holding an elaborate bouquet.)

KELLI: (Pg 37-42) Oh . . . I was expecting someone else . . . Flowers! Oh God, I'm such a gleeb, come on in! [from] Arlin, right? Let me get my wallet. (KELLI returns with her purse.) Those are magnificent!

ARLIN: Hothouse Lilies.

KELLI: Wow, expensive! (Taking flowers.) This is a very good start! (Hands her bills.) I haven't had a date in six months, and tonight, not only have I lost ten pounds and fit in this dress again but, because of a friend at the office, I have a blind date with a guy who sends me very expensive flowers! Take this ten and this twenty, and when you get off work take somebody out and buy them some really expensive flowers! (KELLI sees ARLIN to the door.)

ARLIN: I already did. I bought those exact flowers.

KELLI: Well, good choice, worked for me!

ARLIN: Um . . . Your date . . .

KELLI: Wait a minute. He’s not coming is he? So these are because -- Oh no, no no no! I am so gonna kill Maria tomorrow! She and her friends, who had this guy who would be so 'perfect' for me . . . (Pushes flowers at ARLIN.) I'm sorry, just take these back to their point of origin and give them to an orphanage or something. God, I give up, Really, I give up! (ARLIN is still standing there.) Show's over, you can go now.

ARLIN: A lot of this is because I have a hard time speaking up. I gave you the wrong impression.

(THEY stare at each other. KELLI finally gets it.)

KELLI: No. You're Arlin? (ARLIN nods.) The date Arlin? . . . So now no guy is showing up, and at least one person in the office thinks I'm a lesbian!

ARLIN: Oh, how horrible.

KELLI: No offense, but I'm not a lesbian.

ARLIN: No offense, but I am. (Arlin turns to leave)

KELLI: Wait. Wait a minute, I'm sorry. Um, look, obviously this is very awkward for us both. You should, you should. . . another time maybe -- I mean no, um, bye! (KELLI closes door on ARLIN and cringes.) Oooh my Goood! (Picks up phone & dials.) Lees, hi it's me, worst date night of all time! Blind date, from the office, comes to the door, it's a woman!! Somebody set me up with a woman, can you believe it! (Screams) AAAAA! (A KNOCK on the door, SHE freezes. Whispering) Someone’s at the door. Could be the lesbian, gotta go, call me!

KELLI: (Pg 42 – 52) (Another knock, louder. KELLI answers it.) Hi -- (ARLIN bursts in, throwing flowers at KELLI.)

ARLIN: Here! Those are yours! I bought them for you, and even if you don't want them you can at least have the good grace to pretend until I'm out of sight (ARLIN stomps OUT. SHE stomps back IN.) And I don't know who you are that you should be so narrow minded about who your date turns out to be! What if I'd been a handsome guy who just wasn't that bright, or a really handsome guy who showed up in a wheelchair? (pause) It's just a shame . . . we could have laughed about this and gone to dinner anyway -- you do go to dinner with friends don't you? But no -- (ARLIN turns to exit.)

KELLI: Hey! I'm not the bad guy here! Why didn't you just say something!

ARLIN: I was trying!

KELLI: You're a woman, in a big parka, which of those is supposed to tell me you're my date?

ARLIN: This is my coat, what do you wear? I suppose you have some incredibly cute little "date coat."

KELLI: Don't make fun of me! Why didn't you just say you were the date?

ARLIN: I was a little taken aback, okay? I'm not accustomed to being handed a tip in the first ten seconds that I meet someone.

KELLI: Oh . . . (sheepishly) and I do have a date coat. (Holds up little jacket.) It's not real warm. I'm always cold on dates.

ARLIN: I think one of the most asinine things you can do is go out to have fun, and purposely wear some-thing that makes you uncomfortable. Not so much you personally, but straight women in general -- you wear those little tight clothes & the little pointy shoes. I mean, if you're gonna go out & hang loose & live large . . . it wouldn't hurt you to get a decent pair of shoes with some support. Don't teeter around in those little pin-pricks. (Pause. KELLI looks at her.)

KELLI: Men love it when you teeter.

ARLIN: Oh, they sure do. It's just so sexy when a woman is struggling at all times just to keep her balance. That is so sexy.

KELLI: (Spinning to show off her outfit) If you were a man you wouldn't want to take me out?

ARLIN: I'm a woman and I wanted to take you out!

KELLI: So you get the point!

ARLIN: Why do straight women like to do that? There's a little part of you that just can't resist trying to see if we find you attractive. Just to see.

KELLI: And why are you allowed to make these generalizations?! How come if I say, "You lesbians love coming on to straight women," it sounds like a horrible ignorant stereotype! But if you say, "Straight women love coming on to gays," it comes off like some hip, witty little insight! Why are you allowed to get away with that?

ARLIN: Gee I dunnow, maybe it's compensation for the last couple centuries. It hasn't been that long since it was still legally a mental illness. And they could do anything, have you committed, perform lobotomies, sterilize you, whatever! Ancient history, right? Except right now in Connecticut there's a case pending of a woman trying to regain custody of her son, which she lost simply for being a lesbian!

KELLI: Earth to person, lighten up! Take a pill or something. And you better either leave or take off that parka 'cause you're so red you look like you're gonna explode. You want some water or something?

(ARLIN nods yes and takes her coat off. KELLI gets the water.)

ARLIN: I'm not gonna stay or anything.

KELLI: Well good, because I don't think we're going to come to a deeper understanding through love and laughter. (Hands Arlin the water, which she drinks)

ARLIN: Thanks (Awkward pause.) I should be taking off pretty quick.

KELLI: Don't get all shy on me now, dudette, you've thrown stuff at me and had a tizzy in my living room. Don't get all weird now just 'cause you took off your parka.

ARLIN: Doesn't this feel sort of date-like all of a sudden? Y'know, those awkward moments at the start of dates.

KELLI: Yeah, especially blind dates. What's your name again? Harley?

ARLIN: Arlin. Why?

KELLI: It's just funny, because Arlin could be a man or a woman's name, and you're . . .

ARLIN: A man or a woman? . . . (Pg 61) Do you have any pretzels?

KELLI: I thought you weren't staying.

ARLIN: I'm not, I just thought we'd be at dinner by now and I haven't eaten.

KELLI: I have Fritos.

ARLIN: Thank you. (KELLI gets them.) I'm not staying, I just need something to bring my blood sugar up. (Puts a handful of Fritos in her mouth)

KELLI: (Pg 64) Can I ask you something? (a skeptical look from Arlin) C’mon, you’re eating my Fritos

ARLIN: So not worth it!

KELLI: (Pg 52-53) I'm gonna have a real drink now, do you mind?

ARLIN: No.

KELLI: Oh good. Because some people, if they're officially "non-drinkers", they can't handle it if you wanna have any fun . . . Are you officially a non-drinker?

ARLIN: Mm-hm.

KELLI: Are you alcoholic?

ARLIN: Yes.

KELLI: Man. I'm sorry, I can't believe I just asked you that. Really, I apologize, I just, for some reason, things come blurting out of my mouth with you that I would never normally say. It's really weird. Anyway, I'm sorry.

ARLIN: . . . Are you afraid you drink too much? Is that why you're asking?

KELLI: (Pg 54-56) Well, my blind date blew apart and I'm spending the evening with a perfectly nice alcoholic lesbian, I think that rates . . . Johnnie Walker. (Silence. SHE looks at ARLIN.) I meant that jovially . . . (ARLIN doesn't reply.) (Kelly downs the shot of Johnnie Walker) I'm sorry. Don't mind what I say. (ARLIN puts down her drink and gets her parka.) What? Oh come on, don't do that, I didn't mean anything. Don't go away angry -- what's your name? (SHE goes to get herself another drink . . . and downs that as well)

ARLIN: Arlin!

KELLI: Look. The thing is, I just don't know whether you're coming on to me or not. And I just have no idea how to respond, you know, because I don't know what's what. God, don't be mad. I'm just being honest.

ARLIN: Well trust me, I'm not putting the moves on you. (Kelli gets herself another drink . . and downs that as well)

KELLI: (Pg 58) I'm not an alcoholic, Arlin. It's not a problem for me, okay? (starting to slur her words a bit – looks Arlin up and down) (Pg 66-78) Suffice it to say, I am not attracting quite the same dating scene I did before.

ARLIN: Before what?

KELLI: Before they redrew the map. The everything map. Before you have any idea that this kind of thing can happen. Before that time, you live in, whatsit, ignorant bliss! Before the mail comes in, Arlin. Before the mail comes in. That's where I went wrong! If anybody ever leaves you, don't open the mail! It was 'Before', before I opened the mail! After that, it was nothing but 'After.'

ARLIN: You know, I think Mr. Johnnie Walker is beginning to --

KELLI: Once you open the mail, you can never go back to ignorant bliss. Once you see the statement, you can never go back and not know what it looks like when someone has maxed out your credit cards. And you never want to know that your bank accounts can read sudden zero. (Kelli gets herself another drink . . and downs that as well) Keep your finances separate, Arlin, that's all I can say. If you're gonna get married, don't combine.

ARLIN: Not likely to be a problem.

KELLI: Keep everything separate! Bank accounts, charge cards, loans, -- even if it's more costly. Don't get married, because it completely changes the definition of the phrase "getting screwed"!

ARLIN: I'm sorry. I see you're still very, very hurt. (Long pause) They say in A. A. not to bother bandying words with a drunk, because only one of you will remember it in the morning.

KELLI: (Aggressively and bitterly) That me? The drunk? (Kelli, jabs her finger against Arlin’s check to emphasize key words) The sheen coming off your A. A. tiara is giving me a migraine.

(Frustrated, ARLIN hurls her water glass against a wall, it shatters, her head jerks back, struck by flying glass. KELLI sees that ARLIN is injured and sobers immediately) Are you hurt? Lemme see.

ARLIN: A piece of glass ricocheted. Did I get blood on your floor?

KELLI: (looks at the shattered glass) A little with the glass, it'll come up.

ARLIN: (stops Kelli with a hand on her arm, scared) Lemme do it.

KELLI: Don't worry about it, go wash your face.

ARLIN: You should use rubber gloves. If that's my blood, you should use rubber gloves.

KELLI: Well why, it's not like you have . . .

(KELLI stops. ARLIN watches her response warily. It hits KELLI hard, this reality. That Arlin's blood is not safe. What that means. THEY stand staring at one another, emotions running beneath frozen exteriors. Finally ARLIN moves.)

ARLIN: As a precaution. Use some gloves.

KELLI: (Softly) Okay.

(ARLIN goes OFF into bathroom. KELLI goes OFF into kitchen, comes back wearing rubber gloves, cleans up, still stunned.) (ARLIN emerges with a Band-Aid, putting it on her own face.)

KELLI: You missed. (KELLI points to Arlin's Band-Aid. ARLIN adjusts the Band-Aid on her cheek.)

ARLIN: Okay?

KELLI: Not quite. (Hesitantly, KELLI reaches up and tries to fix it, but it's tricky with rubber gloves on.) It's uh . . . Here. (KELLI pulls her gloves off and adjusts the bandage.) Now, this is not a come-on.

(SHE sits beside ARLIN, puts the Band-Aid on her, sticking its edges to Arlin's face carefully, tenderly. SHE traces the outline of the Band-Aid, touches Arlin's face. ARLIN closes her eyes. KELLI holds Arlin's face in her hand. Not so much sexually as intimately, with the knowledge of Arlin's mortality hanging over them, and loneliness hovering around them, and all that has passed between them. A long moment. THEY break apart simultaneously.)

KELLI: Well . . .

ARLIN: (softly) Hey c'mon, don't get all shy on me now, dudette. You've shouted at me & thrown me out, don't get all weird now just because I bled in your house.

KELLI: (near tears) It makes me sad. It really makes me sad, Arlin. (pause) I'm sorry.

ARLIN: (humor abandoned, Arlin speaks honestly and frankly) Because I have HIV? I get scared sometimes. And I'm lonely a lot of the time. But mostly, I wouldn't trade it, Kelli. Not even to have all my health back, I wouldn't, I wouldn't go back where you are now. (long pause then she begins again) On the wall at the planetarium it says, "A man can reach the stars if he can dream of it!" What about women? And they say, "Oh, well, by Man we mean everyone, all Mankind!" I don't think of [myself] as Mankind, I just feel left out. But hey, when you run the language, you call the shots. Who decided we were Mankind? It's not our story, it's history! It's all male-oriented. And it sounds like small stuff, but it's subtle. [It’s] like HIV. Once it's in the blood, it effects everything . . . (thoughtfully) Except one word. I know one female-rooted word!

KELLI: What?

ARLIN: Commence. Co-mensing, as in menstruation? Meaning to flow forward together. Isn't that nice? Let us commence.

KELLI: Nice?! Something in your [world] is actually nice?

ARLIN: (Wryly) Yeah. One thing. (shrugs her shoulders) It's a start. Let us commence. [After all] my date was a bust.

KELLI: (smiling) No it wasn't. It wasn't even a date.

ARLIN: No? What was it?

KELLI: It was . . . . (holds out hand to Arlin, who takes it in her own) a commencement! (they smile at one another)
```

---

## IC-0573: Cookin’ Up the Competition

- Title: Cookin’ Up the Competition
- Author (byline): Ira Brodsky and Barbara Lhota
- Work: Duo Practice and Competition, Volume 3 (Pg 163-172)
- Publisher: Smith and Kraus
- Publication date as stated: Sept 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: STEPHANIE, GRACE
- Teaser before the introduction: Yes
- Spoken words (computed): 1367
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ira Brodsky and Barbara Lhota
Book: Duo Practice and Competition, Volume 3 (Pg 163-172)
ISBN: 978-1575253800
Publisher: Smith and Kraus
Date (Month/Year): Sept 2004
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: It’s been a longstanding view that women are fiercely competitive with each other.

ACTRESS 2: Where does this need to compete come from? The most commonly held belief is that it comes from feelings of insecurity.

ACTRESS 1: When the media is hell bent on portraying the “ideal” female body as model thin:

ACTRESS 2: 5 foot 8 and 115 pounds (Stands on tiptoes and sucks in, then exhales) Yeah, right!

ACTRESS 1: It’s easy to feel threatened by the beauty and talent of other women.

ACTRESS 2: According to Emily Gordon, the author of the book, Super You: Release Your Inner Superhero, “We look at other women and see a version of ourselves that is better, prettier, smarter, something more.”

ACTRESS 1: We are in constant competition with ourselves! And it has to stop!

ACTRESS 2: Today, we’re blowing the doors off this crazy one-upsman-ship with . . .

TOGETHER: Cookin’ Up the Competition by Ira Brodsky and Barbara Lhota
```

### Performance text (classify this)

```text
Grace and Stephanie are successful career women and mothers who often feel the need to compete with each other. Grace is jealous of Stephanie's culinary talents and Stephanie envies Grace's skill at home decorating. Today, they find out that perhaps their jealousies are unjusti-fied.

(Grace reaches for a box of cake mix and begins reading the directions.)

STEPHANIE: Why do you have these eggs on the radiator?

GRACE: It calls for them to be room temperature.

STEPHANIE: Room temperature, yes, not roasting toxic salmonella eggs.

GRACE: Well, I don't know. That's why I asked you to come over here and advise.

STEPHANIE: Grace, you are not a cook. You will never be a cook. Stop cooking. Look what happened last time.

GRACE: A little mishap. Pfff. It all worked out.

STEPHANIE: Yeah, three fire trucks and several smoke inhalations later.

GRACE: You exaggerate. Nothing caught fire.

STEPHANIE: Except your cat.

GRACE: I forgot about that. But she rolled herself out immediately, and now she's fine. (Beat) I'm not talking to you. I'm putting away the eggs. (Beat) So did you see the little thing I threw up in the front foyer?

STEPHANIE: The gorgeous, embroidered wall hanging? How could I miss it? I suppose you made it yourself.

GRACE: Well ... Don't go on and on about it. You just embarrass me. So you liked it?

STEPHANIE: Yes, it's gorgeous and not little. So let's bag the baking-the-cake thing. We all have our skills. Baking's not yours.

GRACE: Look, just this once. I want to bake Mike a birthday cake from scratch.

STEPHANIE: I hate to break this, Grace, but a Betty Crocker cake is not exactly from scratch.

GRACE: Look, I break an egg. I put it in the oven. For me, that's baking.

STEPHANIE: Tell you what. We go to a nice bakery. We mess up the frosting so it's not perfect and everyone will think we-you-made it from scratch. It'll be real nice.

GRACE: That doesn't sound nice. In fact, it sounds downright dishonest.

STEPHANIE: Well, it's the thought that counts anyway!

GRACE: Thought-schmought. I want to make a big, honkin' homemade cake with fresh fruit something and to-die-for layers, a whipped icing-oozing thing! The sort of masterpiece that you're always making for us. That fresh vegetable lasagna you made last time we visited? Mike wrote an original song singing its praises. He probably would have given our first-born child for an extra slice.

STEPHANIE: You only have the one.

GRACE: I know. You want to compete on that too?

STEPHANIE: I'm not competing! Who said I'm competing?

GRACE: O,h come on. Look at the evidence. First you have a second child- Then you buy a bigger house

STEPHANIE: Well, we had a smaller house than you to begin with.

GRACE: See?! Then while holding down an impressive job, you finish your law degree.

STEPHANIE: Well, you're writing your dissertation. You're almost finished.

GRACE: Yeah, and I've been almost finished since like, like 1999. And then you make an incredible lasagna that turns my husband into Rodgers and Hammerstein.

STEPHANIE: Look, I wouldn't be forced to impress you with my baking if I wasn't so moved by the way you decorate every charmed room in your house. You know, even Drew comments. He asked me why our house can't look that good.

GRACE: Oh come on!

STEPHANIE: I'm serious, making all those slipcovers, and pillows, and your color sense. And then the embroidering! It's all so unbelievably talented that the least I could do is throw together flour and eggs into something incredible. (Awkward silence)

GRACE: (taking a picture off the fridge) You should see my little Lincoln! His teacher says he's such a good artist he'll probably be an architect. He got the class award in art.

STEPHANIE: Umm. That's wonderful. Chrissy is doing well too. She's just a crackerjack with words. The teacher said she's gifted. She's starting to read.

GRACE: At her age? That's advanced.

STEPHANIE: Isn't Lincoln?

GRACE: Well, sometimes they say it's better to develop the spatial brain first. A lot of times, it gives kids a good grounding. They become better in math.

STEPHANIE: Yes, that's true, but then there's communication. Reading. Verbal abilities. Chrissy's a great communicator. She has three good friends already, and even a boyfriend. How's Lincoln on that score?

GRACE: Well, he has friends. He has lots of friends. (More quietly) Some of them are imaginary, but I think that's healthy.

STEPHANIE: Well, children all develop at their own pace. For instance, it took Lincoln several months longer to turn over.

GRACE: I knew it! I knew you were going to go there!

STEPHANIE: What's the matter? That's not a bad thing.

GRACE: So he took a month longer to turn over! He was examining the carpet fibers. He could be an engineer someday.

STEPHANIE: Sure, or a carpet ... inspector.

GRACE: He's probably more focused. Not flipping every which way. Flitting about and chatting it up with every preschool boy he meets.

STEPHANIE: You make her sound like a bubble-headed flirt.

GRACE: Well, you make him sound like a social *reject*!

STEPHANIE: Look, I don't need this! I just came over to help.

GRACE: Help?! All you do is make me feel bad about myself! (Mimicing) Drew got a promotion. Chrissy's a genius. I bake Martha Stewart cakes and you never will!

STEPHANIE: I never said you never will! (Grace gives her a look) OK, maybe I did say that, but I didn't mean it.

GRACE: You always have to one up me.

STEPHANIE: That's ridiculous! That's what you do to me.

GRACE: So Chrissy's a social whiz kid! And my Lincoln'll end up a carpet cleaner!

STEPHANIE: Well, at least your son doesn't eat paste and stuff it up her friend's nose.

GRACE: What? Chrissy? Well-adjusted, social-whiz Chrissy?

STEPHANIE: Yes! Well-adjusted when she's not stuffing paste up her friend's nose and dining on it. I could have died. Her "guide" teacher asked me what I was feeding her-What is her sugar quotient? I told her I gave her apples, and apple sauce occasionally, but only if I processed fresh apples in our own food processor-most of the time.

GRACE: Oh, that was a good answer. That'll keep 'em off you.

STEPHANIE: Yeah, except she locked onto "most of the time." She finally got it out of me that I occasionally give her storebought. Jeez. I guess I'm a bad mother.

GRACE: Me too, because sometimes I give him (Whispers) McDonald's. We're great moms, loving and caring. And you especially! With all that cooking you do! Chrissy's gonna grow up knowing her mom really cares.

STEPHANIE: Well, I do, of course, care. A lot. But I don't really cook very much.

GRACE: What?!

STEPHANIE: Look, I can't be bothered with it all. I just buy stuff like from the international food store, heat it up, and throw it on the plates with a sprig of parsley.

GRACE: You're kidding? But you ... But we ... But Mike . . . So you can't cook?!

STEPHANIE: I'm worse than you.

GRACE: No-And the lasagna?

STEPHANIE: Mario's Frozen Italian Dinners. Straight from Farmer Jack's.

GRACE: Oh my God!

STEPHANIE: Yes. I'm sorry. I can't live the lie anymore. I just wanted you to think I could do something domestic right since you sew so incredibly well.

GRACE: Steph? I have something to admit to you. I don't sew.

STEPHANIE: At all?! (Grace shakes her head no) But what about all those pillows and the wall hanging and those colors you put to-

GRACE: My decorator and my mother.

STEPHANIE: No! (beat) God, I feel better about myself.

GRACE: Me too!

STEPHANIE: So what else have you been lying about?

GRACE: I don't know. Well, my workout schedule.

STEPHANIE: Oh my God! Me too. So it's not five times a week?

GRACE: Once if I'm lucky. And you? How's the running?

STEPHANIE: Fine, but mostly to the fridge. And I didn't actually lose anything on Weight Watchers either.

GRACE: I gained!

STEPHANIE: Me too! And what about the-? (Refers to her breasts) Did you have a little enhancement?

GRACE: Gel-filled bras.

STEPHANIE: Are you kidding? I can't afford the designer stuff.

GRACE: Designer? Where do you think I shop?

STEPHANIE: I don't know ... Target?

GRACE: Bull's-eye!

STEPHANIE: Oh my God! Me too! By the way, you know how I finished with my law degree? I don't even want to be a lawyer anymore.

GRACE: Oh my God, Stephanie, but the loans on that.

STEPHANIE: I know.

GRACE: Oh, honey, I'm so sorry ... and I'm so happy ... I mean, I'm kind of relieved ...

STEPHANIE: Knock it off. I know what you mean. I have an idea. Let's go to the bakery and find the most gorgeous cake we can.

GRACE: And we'll tell Mike I made it!

STEPHANIE: He'll think I'm the greatest teacher in the world!
```

---

## IC-0574: Defying Gravity

- Title: Defying Gravity
- Author (byline): Jane Anderson
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS 1, ACTRESS 2, RADIO ANNOUNCER, TEACHER, ELIZABETH, ELIABETH, NASA VOICE ON RADIO 1, NASA VOICE ON RADIO 2, TV NEWSCASTER, GRANDMOTHER, BEACH COMBER
- Teaser before the introduction: Yes
- Spoken words (computed): 1433
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jane Anderson
ISBN: 978-0573601330
Publisher: Samuel French, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: On January 28, 1986, NASA and the American people were rocked as tragedy unfolded 73 seconds into the flight of Space Shuttle Challenger’s mission.

ACTRESS 2: An explosion – the result of a leak that ignited the main liquid fuel tank – instantly killed the seven-man crew.

ACTRESS 1: Among the dead was Christa McAuliffe, a gifted teacher who could communicate with students from space.

ACTRESS 2: It is in part because of the excitement over McAuliffe’s presence on the Challenger that the accident had such a significant impact on the nation.

ACTRESS 1: But the public record can’t begin to describe the personal stories behind the headlines.

ACTRESS 2: Defying Gravity by Jane Anderson re-imagines the tragedy from the point of view of Elizabeth, the teacher’s daughter, who lost her mother at the age of 5.

TOGETHER: Defying Gravity by Jane Anderson
```

### Performance text (classify this)

```text
Suggested Roles:

ACTRESS 1: Radio Announcer, Elizabeth, NASA voice on the Radio 2,

ACTRESS 2: Teacher (aka Elizabeth’s Mom), NASA voice on the Radio 1, TV Newscaster, CB, Grandmother’s echo, Beachcomber

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

RADIO ANNOUNCER: (Pg 12) The Discovery touched down today after a successful 13-day mission. The six crew members had a special guest on board. Ariadne the Spider, who successfully spun a web in zero-gravity. Way to go, Ariadne. In January of next year they plan to send a teacher into space. You’re listening to K-FARM 101, easy listening for the Dakotas.

(Teacher is standing in front audience aka her class, teaching about the Cathedral of Rouen)

TEACHER: (Pg 14-15) Heather, would you change the slide? . . . All the towns were competing with each other to see who could build the tallest cathedral. For a long time, you could only build to a certain height before the pull of gravity would cause the whole thing to collapse. But then they invented the flying buttress (beat) Butt, very funny, Jason. I broadened the base of the cathedral so the walls could rise hundreds of feet into the air. People always believed if you defied gravity, you were that much closer to God. (gesturing to the slide) If you follow the lines of the pillars up, you are led to what many people thought was heaven. Before the airplane, this was the closest that we ever came to the experience of flight. (beat) Do you think it was worth it? (beat) Anyone? *****Scene*****

ELIZABETH: (Pg 23-25) (as an adult) That Christmas, I asked my mother for a Cabbage Patch Doll But she didn’t have time to get me one. All the presents that year were from the NASA gift shop: (holds up a toy space shuttle) A plastic space shuttle and a package of astronaut ice cream. My mother was going to read me How the Grinch Stole Christmas but she kept getting phone calls. (Elizabeth morphs into her 5-year-old self and begins banging the space shuttle on the floor)

TEACHER: (into phone) Well, as I’ve been telling everyone, I’m more nervous about getting in the car and driving on the freeway. It’s a chance in a lifetime. (Elizabeth throws the shuttle at the Teacher who dodges) Can I call you back? (hangs up, then to Elizabeth) What’s gotten into you?

(phone rings and the Teacher answers)

ELIZABETH: (as an adult) I hated the shuttle. I hated space. I think at that moment, I hated her.

TEACHER: (into phone) Well, as I’ve been telling everyone . . .

TEACHER and ELIZABETH: I’m more nervous about getting in the car and driving on the freeway.

TEACHER: It’s a chance in a lifetime.

ELIABETH: It’s a chance in a lifetime. . . (long beat) (Pg 9-10) The last time I saw my mother was in a visiting room next to the launch pad at Cape Canaveral. I remember we got there very early in the morning. They had donuts and hot chocolate waiting for us. Reporters kept coming in. I asked my father if we were waiting for my mother to come back from space. He said that she hadn’t even left yet. Then my grandmother gave me a coloring book and a new box of crayons to keep me busy. I broke the point on the blue crayon and I started to cry. (gets down on the floor as a 5-year old coloring with crayons)

TEACHER: (Pg 9) All right, Honey, time for bed. Would you put your crayons away, please?

ELIABETH: See what I did? (Elizabeth shows a piece of paper filled with crayon scribbles)

TEACHER: I see, that’s very pretty

ELIZABETH: You know what it is? – It’s an impressed painting. You know, from the book. The painting in the book.

TEACHER: Oh, you mean Impressionist?

ELIZABETH: Yeah. Guess what it is?

TEACHER: Honey, that’s wonderful. Is it a flower garden?

ELIZABETH: No.

TEACHER: Water lilies?

ELIZABETH: Noooo. It’s spaghetti!

TEACHER: Ohhhh. I see. Come on, kiddo, it’s time for bed. *****Scene*****

ELIZABETH: (Pg 38) (as an adult) I remember a reporter asked me what I thought of my mother going into space. I didn't want to answer so I hid my face behind my grandmother's purse. My brother laughed at me so I hit him on the arm. My grandmother gave us Lifesavers to quiet us down. I put it in my pocket for later. Then my mother joined us and she let me hold her hand while she talked to the reporters. She showed the reporters some of the things she was taking up to space. She had a journal and in the journal was a bookmark that I made for her. I had drawn a rocket and stars and Saturn with the rings and I ironed it between two pieces of wax paper so it would be protected from the gamma rays. I wanted to give her something else, so I took out the Lifesaver. It was fuzzy from the lining of my pocket. While my mother and the reporters talked, I tried to make the Lifesaver presentable. I told myself I had to pick all the lint off the Lifesaver or my mother wouldn't come back. Finally, my mother crouched down next to me. She was wearing her blue space suit. I touched the patches on her shoulders. She looked so beautiful. Suddenly I couldn't grasp that this was the woman who every morning sliced banana on my granola. My grandmother kept saying, “say good-bye, honey, say good-bye to your mother.” But all I could manage was to hold out the Lifesaver which was sticky from the sweat of my hand. My mother took it and put it in her pocket and I knew everything would be all right.

NASA VOICE ON RADIO 1: (Pg 39) . . . T-minus thirty minutes and counting. ****On the shuttle*****

TEACHER: (Pg 39) (to audience as if they were the crew, holding up the Elizabeth’s bookmark) Did you see this? My little girl made it for me. (looks at it proudly) Oh my God, I didn’t see that. She wrote her name. I’ve been trying to help her learn it, but she said she couldn’t because I gave her a name with too many letters in it.

NASA VOICE ON RADIO 2: . . . T-minus 15 seconds and counting / no unexpected errors.

TEACHER: (distraught) I need to see her. I need to see my little girl. (the bookmark slips out of the Teachers hand and falls to the floor)

NASA VOICE ON RADIO 1: (Pg 41) 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 . . and lift off. Challenger, go with throttle up.

ELIZABETH: (Pg 34) (as a child) MOMMEEE! GIVE ME BACK MY MOMMY! (sobbing, then an explosion) ****Scene*****

ELIZABETH: (Pg 53) (as an adult) When I watched my mother’s ship take off, I saw it go straight into the sky and disappear. When my grandmother told me that my mother went to heaven, I thought that was a part of outer space. I was excited because I thought she'd come back with all kinds of neat presents like a plastic harp or a pair of angel wings. I went to the mailbox everyday looking for a postcard from her that would have clouds or a 3D picture of God.

TEACHER: (Pg 15) (echoing) People always believed if you defied gravity, you were that much closer to God.

ELIZABETH: (Pg 53) I waited for her to call long distance. When I didn't hear from her I got very angry. I told my father I hated her for being away so long. He told me she had “perished” in the rocket. I told him that wasn't true, that she was alive.

TV NEWSCASTER: (voice over) Reports today from NASA have given us new evidence on the Shuttle disaster. The cockpit has been recovered and the bodies have been found.

ELIZABETH: That she had left us and found a family she liked better. He asked me why did I think she was still alive. And I said, “because I never saw her dead.” CB (MEMBER OF NASA GROUND CREW): (Pg 46-47) At T minus nine minutes they couldn’t get the handle off one of the hatches. They had to get this special drill. But someone used it and didn’t bother to replace the batteries. Let me explain. See, I borrowed the drill to fix the door on my van. I stuck a note on it saying to change the batteries. But I guess the post-it didn’t stay on. I should of just changed the batteries myself, but in order to do that I would have had to fill out a form explaining why I needed the new batteries and then I’d have to run it over to another building to get it approved, then wait an hour to have it processed, then run to another building to pick the batteries up. Then I would have had to get a guy to supervise me while I put the batteries in. (beat) I was at the end of a 20 hour shift and my next shift was in 5 hours. So . . . I’m sorry. I never meant to take your mommy away from you.

TEACHER: (Pg 65-66) (softly) Gravity is the force that pulls us towards the center of the Earth.

NASA VOICE ON RADIO 2: . . . T-minus 10, 9, 8 . . .

TEACHER: There is also another definition of gravity: Graveness or seriousness; solemnity, heaviness.

ELIZABETH: (Pg 53) [But I knew none of this.] These are the reasons I gave myself for why my mother didn't come back. One: I hit my brother on the arm. Two: I didn't say thank you to my grandmother for the coloring book.

GRANDMOTHER: (Pg 38) (echoing) “Say good-bye, honey, say good-bye to your mother.”

ELIZABETH: (Pg 53) And Three: I didn't get all the lint off the Lifesaver.

BEACH COMBER: (Pg 48-49) Honey, what is that? Maybe it’s a piece of the shuttle. Oh, my god, let’s see. (examines it) Huh. No, it isn’t anything. It’s just a . . . .

ELIZABETH: (Pg 53) Lifesaver. (beat) I didn't get all the lint off the Lifesaver.
```

---

## IC-0575: Disney Mom Group Therapy

- Title: Disney Mom Group Therapy
- Author (byline): Mo Gaffney and Kathy Najimy
- Work: Parallel Lives: The Kathy & Mo Show, Pg 67-72
- Publisher: Dramatists Play Service
- Publication date as stated: Jan 1993
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DR. KINCAID, MONIQUE, ALL, DOLORES, BETTY, CORAL, ETHEL, MRS. JUMBO, BARBRA, CRUELLA
- Teaser before the introduction: Yes
- Spoken words (computed): 1260
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mo Gaffney and Kathy Najimy
Book: Parallel Lives: The Kathy & Mo Show, Pg 67-72
ISBN: 978-0822213086
Publisher: Dramatists Play Service
Date (Month/Year): Jan 1993
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Let’s face it . . . no one is more in need of a support group than the poor mothers of Disney characters.

ACTRESS 2: When the first question asked upon entering the room is “Are you alive?” you know you may be in for a bumpy ride.

ACTRESS 1: Let’s listen in and find out a bit more about DMGT.

ACTRESS 2: For those of you opposed to acronyms, that’s Disney Mom Group Therapy by

TOGETHER: Mo Gaffney and Kathy Najimy.
```

### Performance text (classify this)

```text
Suggested Roles: Actress 1: Dr. Kincaid, Dolores, Coral, Barbra

Actress 2: Monique, Betty, Ethel, Ms. Jumbo, Cruella

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

DR. KINCAID: (Pg 67-72) Hello everybody, welcome to the Disney Mom’s Support Group. Are we all here?

MONIQUE: Excuse me, am I in zee right room?

DR. KINCAID: Are you alive?

MONIQUE: Well, yes . . . I suppose . . .

DR. KINCAID: I mean in the movie, are you alive or do you die in the beginning or are you dead when it starts?

MONIQUE: Well, they never actually make mention of me.

DR. KINCAID: I bet you’re already dead then. And your name is?

MONIQUE: Monique. Monique Andthebeast.

DR. KINCAID: Everybody, this is Monique Andthebeast.

ALL: WELCOME MONIQUE!

DR. KINCAID: And you’re the mother of . . . ?

MONIQUE: Belle, well Beauty. Walt has some kind of Jones for renaming his girls “Beauty.” A lot to live up to if you ask me . . .

DOLORES: Ya got that right, sister . . .

MONIQUE: It’s like being named “Stacked.” Sacre Blue – her name is Belle. And no, the only women in the film are a witch, a teapot and a hutch . . . (She starts to cry) He had her being raised by a pot and some old furniture. . .

DOLORES: My name is Dolores . . . Dolores Deer, mother of Bambi . . . My son was raised by a rabbit, Monique!

MONIQUE: No, Dolores!

DOLORES: And a skunk for Christ’s sake.

MONIQUE: Ooh, I just want to find that Waltsicle and thaw his *butt* out!

DR. KINCAID: No, now . . . you’re among others like you . . . you’re not alone . . . Most of the Disney girls were not raised by their mothers. Right, ladies? (group murmurs) We are delighted to have you in the group, Monique.

MONIQUE: (Sings) Bonjour, bonjour, it’s nice to meet you.

DR. KINCAID: Why don’t we all do introductions and then we can start? . . . Betty? Why don’t you start? (Snickers)

BETTY: (Sings) I’m wishing, for the one I love, to find me . . .

DOLORES: Shut it, Bet-tee!!!

BETTY: Sorry. I’m Betty. Mother of Snow, Betty White. (Snickering) I know, I know, I’ve heard all the jokes. Dead at the beginning.

ALL: WELCOME, BETTY!

CORAL: Hi, I’m Coral Clownfish, mommy to Nemo. I horrifically die at the beginning as well. I brought some Shark sugar cookies, if anyone’s interested.

ALL: WELCOME, CORAL!

DOLORES: Dolores Deer, mother of Bambi. Shot dead in the first then minutes. Yeah, yeah I know, “Welcome Dolores.”

ETHEL: (Sings) Hello, Dolly!

DOLORES: All right, Ethel . . .

ETHEL: I’m Ethel, Ethel Mermaid, mother of Ariel. I’m dead from the beginning. And there’s some fried calamari on the table as well.

ALL: WELCOME, ETHEL!

MRS. JUMBO: (Elephant trumpet) Jumbo, I am Mrs. Jumbo.

ALL: WELCOME, MRS. JUMBO!

DR. KINCAID: Okay, that’s everybody, let’s get started. Oh, and just so you all know, Habiba and Whaddad, Jasmine’s and Aladdin’s moms, couldn’t be here because they are at a burqa burning. (Cheers) Okay then, why don’t we start with a free form? And again, Betty White, could you start? Last week you were telling us how traumatic it was when they took Snow to the forest.

BETTY: Well, Doctor, for starters my daughter’s name is Snow WHITE and they send her out to the forest with no sunscreen, and you’re gonna think I am making this up, Doc. . . but Walt has her meet and move in with seven little men, clean and cook for them all, whistle the s*** out of herself, east a Jim Jones apple, fall asleep and then of course . . .

ALL: A handsome prince comes and kisses her and they live happily ever after! (Pause . . . then they all burst out laughing)

BETTY: A teenage girl and seven little men! You find that kind of *crap* on the Internet.

DR. KINCAID: Thank you, Betty, that’s a good start. Coral Clownfish, why don’t you go next?

ETHEL: Sing out, Coral!

CORAL: I just want to say, “NOT how it happened!” Would I show a hungry barracuda my nest? No!!! “Hey, big mean killer, come on in, eviscerate my children, then slice me open like a lute fish!” Oh, and just so you know that coffee is hot and I baked some fresh biscuits.

ETHEL: (Sings) There’s no biscuits like fresh biscuits . . .

DR. KINCAID: Ethel Mermaid, it seems like you have something to say?

ETHEL: Okay, well, again, I’m Ethel Mermaid, mother of Ariel. First off, I would NEVER let my daughter give up her voice and half her body for some . . . for some guy she’d never even met. I mean, she saw him on a boat! He could have been Dahmer on a day cruise for the love of stage right. What’s up with that?

DR. KINCAID: Okay, Ethel, we hear you. Dolores, you look raring to go.

DOLORES: Ya think? Well, first off I’m killed in front of my baby . . . yep . . . by some damn hunter. Now there’s a challenging SPORT huh? There I am – an innocent, graceful doe drinking crystal water out of a sparkling stream and some A-hole sneaks up from behind, takes a bead on me and blam! Pops a cap! And can I just say “Great Prince of the Forest?” The guy lit out the second the kid was born! I mean you can’t see that *stuff* on Rikki!

MONIQUE: Oh, Dolores, that is horrible . . .

DR. KINCAID: It’s good to get it out. Oh, look who’s here. Barbra – Welcome.

BARBRA: (Drunk) Sorry, (to Ethel) did I step on your tail? Sorry, sorry . . . It’s a b*** to park a pumpkin in a compact space . . . Waddya bet my door’s gonna get bruised . . . again! My name is Barbra and I’m an alcoholic . . .

ALL: WELCOME, BARBRA!

DOLORES: Wrong meeting Barb . . . This is the Disney thing . . .

BARBRA: Ooops. Sorry. My name is Barbra, my daughter is Cinder . . . I’m Barbra Rella and my daughter Cinder was allergic to manimals . . . he had her singing her guts out in a tiny room with birds and mice crawling all over her getting her dressed . . .

DOLORES: I hate mice!

BARBRA: Me too! And they went on and on about how much she missed her father . . . What about me? What about me?

CORAL: Can I get you some coffee?

BARBRA: Yes, just a drop of Kahlua . . . And how about all those jabs from Walt about me? She turns to s*** at twelve o’clock? Cinder runs down the 12 STEPS? Got it Walt! (To Coral) Thank you . . . and to top it all off, she runs off with that picky Prince with a shoe fetish . . . Only feet that can fit the shoe – Only feet that can fit the slipper!

DR. KINCAID: Thanks for that Barbra, that was very revealing. All right, who hasn’t gone yet. .? Mrs. Jumbo? What’s wrong, Aristocat got your tongue?

ETHEL: Sing it, Jumby!

MRS. JUMBO: Ohhh, Lordy . . . it was so long ago it’s hard to remember . . .

ETHEL: But you’re an elephant . . . you’re supposed to –

MRS. JUMBO: No stereotypes please, Ethel! I was a proud young elephant . . . ripped from the jungle by THE MAN and brought shackled to the circus to “perform.” It was humiliating. Then my boy was born . . . beautiful. Big trunk, big ears, big . . . he was beautiful. And just because he didn’t look like some small-featured ferret they made fun of him. The last straw was when some little brat tugged on his ears and I lost my s***! They labeled me “crazy” and sent me to the slammer. I didn’t even make it through the first twenty pages, man.

ETHEL: Say it from your soul, sister!

MRS. JUMBO: That’s my story

DR. KINCAID: Thank you, Mrs. Jumbo, that was truly moving. Now, I have to say I certainly sympathize with you women, but I must remind you that Disney wasn’t the original author on most of your stories . . .

CRUELLA: Yes, but he picked them and he edited the wretched things!

DR. KINCAID: I’m sorry, you are?

CRUELLA: Cruella DeVille, Jumbo’s lover. We met in the big house. (Mrs. Jumbo makes an elephant noise) Darlings.

ALL: WELCOME, CRUELLA!

DR. KINCAID: Okay, last thing on the agenda: Princes (Groans and ad-lib reactions to the following questions) How many daughters kissed by the handsome prince? How many taken away on a horse? How many never spoke to the guy before they married him? On, two . . . slow down, ladies . . . slow down. Oh gosh, time’s up. Great session today, Ladies. And now it’s time for . . . meds!

BARBRA: WOOHOO!

DR. KINCAID: And don’t forget, a spoonful of sugar . . .

ALL: Helps the medicine go down! (Hums “Spoonful of Sugar”)
```

---

## IC-0576: Dolores

- Title: Dolores
- Author (byline): Edward Allan Baker
- Work: The Best Short Plays 1989, Pgs 175-196
- Publisher: Applause Theatre Books
- Publication date as stated: Dec 1991
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DOLORES, SANDRA
- Teaser before the introduction: No
- Spoken words (computed): 1759
- Already set (do not supply): none

### Source block (context only)

```text
Author: Edward Allan Baker
Book: The Best Short Plays 1989, Pgs 175-196
ISBN: 978-1557830456
Publisher: Applause Theatre Books
Date (Month/Year): Dec 1991
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Sandra is home alone, enjoying her weekly break from her husband and kids, when her older sister Dolores shows up with a black eye, courtesy of the latest in her string of bad husbands.

ACTRESS 2: Dolores is the story of siblings and spouses, bruises and bullets, in which two sisters with two very different kinds of heartache must confront the anguish behind every routine that life imposes.

ACTRESS 1: It takes the punishing love of family and one shocking act of violence to remind them that every kind of love has its own darkness and that every plea for mercy is one for understanding.

TOGETHER: Dolores by Edward Allen Baker

As scene opens, Sandra is dancing and singing to the *Will You Love Me Tomorrow? by the Shirelles while removing items from a shopping bag atop the table. Enter Dolores.
```

### Performance text (classify this)

```text
DOLORES: (Pg 175-196) Uh . . . Sandra?

SANDRA: (Sandra spins and sees Dolores, then quickly turns off the music; angrily) NO! OUT!

DOLORES: Please! I gotta stay here! He wants to kill me!

SANDRA: I'm sick a' this, Dolores! Out!

DOLORES: He's afta' me!

SANDRA: I don't care!

DOLORES: What is wrong with you?! He wants ta' kill me! You think I'm kiddin'?!

SANDRA: I don't want to get involved! I mean it! I'm sick a' only seein' you when you got problems!

DOLORES: Let me stay for a little while till . . .

SANDRA: NO! Whenever I help you, it turns into a horror show!

DOLORES: I'm scared, Sandra!

SANDRA: When are you gonna' learn?! Huh? How many more f****ed-up guys you goin' ta' marry?! An don't pull the tears on me! This is my only time alone. Sunday aftanoon Vinnie takes the kids to the park, then to his Mother's, an' it's my only time away from all the aggravation, ya' unda'stand?

DOLORES: (removes sunglasses, revealing a black eye) Just for a little while, then I'll go, okay? (Sandra looks at black eye) I don't want to get hit no more or yelled at . . . I'm so tired of bein' yelled at an' . . .

SANDRA: (manages to break free from Dolores) An' whose fault is it, Dolores? You pick these nuts ta marry an afta' six months you come runnin' to everybody! We all try to tell you not to marry these *idiots*, but you never listened. Then we go to your stupid weddings an' listen to the same song you pick out as you're walkin' down the aisle . . . "We've Only Just Begun."

DOLORES: (softly, wiping her eyes) I love that song . . .

SANDRA: But we're all laughin'. Don't ya' know that?

DOLORES: Let me stay just for tonight and . . .

SANDRA: (cuts her off) No! Vinnie would never have you stay here, an' me an' him been gettin' along pretty good lately an' I don't wanna break it. I don't need 'im seein' you here 'cause he'll turn right around an' split, an' I don't need that shit on top a' everything else! I got my little house with my little kitchen where I feed my little kids an' Vinnie brings home his little paycheck an' if there's a little extra on Fridays we go out to Valle's by the Airport for a little steak an' salad, then to a show. I got three Dustbusters, a coupon drawer an' I'm savin' stamps for a VCR!

DOLORES: (after a beat) You're so lucky . . . Does Vinnie ever hit you?

SANDRA: Of course not. Shove here, a shove there . . .

DOLORES: We all get shoved, Sandra. I'm talkin' about whacked, kicked, pushed down stairs, hair pulled back, woken up in the middle of the night for hard sex, insulted in a restaurant, pushed outta' a car . . . What if he's out there waitin' for me?!

SANDRA: I don't know. Talk it out with him. He doesn't seem that bad. Except for his crooked eye, he seems normal so just figure it out for ya'self! Go to the police!

DOLORES: Forget that! They don't do nothin'! I been through it before, an' they come an' usually stick up for the guy. Unless there's a knife comin' outta your heart! You're not really goin' to throw me out there, are you?

SANDRA: Dolores . . . I got . . . I got my own life here, an' stuff you get involved in is so way above my head. I mean . . . he hit you an' well, you gotta work it out with him. Vinnie an' I get along fine 'cause most times we walk around here an' we just don't talk. We watch television an' on Fridays he gets what he wants an' we just go on and . . .

DOLORES: (cuts Sandra off) I don't want that! I want more than that, for Chrissakes. No talkin' an watchin' TV . . . if I wanted that I never woulda' left Frankie!

SANDRA: Oh c'mon . . . Frankie ate his spaghetti an' meatballs with his hands an' couldn't talk straight!

DOLORES: (Looks away) When I first met Jerry . . . I was, was down in the pits. I felt I had no family, I had no kids, no nothin' an' I was thirty years old. Goin' to the bars lookin' around at other thirty-year-old women. I couldn't watch TV no more 'cause family scenes made me sob and the music on the radio, especially Carly Simon songs, made me all soft inside . . . like I was dyin' for somebody to just touch my hand! I'd . . . I'd look at some guy, you know, an' think to myself, "oh, please let him say something nice to me 'cause I'm the one for him . . . " an' I would just pray he could pick it up in my eyes, but too many times nothin' like that ever happened. I'd look in the mirra' an'-an' my face always looked dirty and I would scrub it till it was red! Then one night I looked over an' saw Jerry lookin' at me . . . an' I forgot bein' lonely an' the family, an' other women! Help me! Help me get through this, Sandra!

SANDRA: (snaps) WHAT?! WHAT DO YOU WANT ME TO DO?! What?! Put you in the cellar?! Hide you in the closet?!

DOLORES: I need some help, I need support. I'm good, Sandra, an' everybody comes down on me 'cause I don't like gettin' beat up! I'm supposed ta put up with it 'cause Ma did?! That's not what my shrink told me.

SANDRA: (surprised) You see a shrink? Where do you get money to see a shrink?

DOLORES: It's only a buck a week or whatever you can afford, kinda like welfare shrinks in this clinic on Cranston Street. They listen for half an hour an' ya get stuff out, but I don't feel any different. It's like when you're a kid leavin' confession an' ya' feel good for about twenty minutes. I try things this woman says, but I don't know if I really believe in all that *crap*,

SANDRA: Okay, okay. Does this shrink say any thin' about him an' what you should do about it?

DOLORES: Oh, yeah. That I should . . . uh . . . confront him more an' make him aware of problems that I have with him. Stuff you read in Seventeen magazine, an' I tell her "Yeah, easy for you ta say cause you're not in front of the mean green eye a' his" an' she says "true."

SANDRA: Hold it. Have you talked ta Jerry like she said you should?

DOLORES: If you got a problem with Vinnie, say he did some disgustin' thing that pissed you off, do you sit down with him to discuss it? Do you say "Gee, Vin . . . you look so ugly in ya' boxer shorts an' ya' gettin fat"

SANDRA: Wait a . . .

DOLORES: (continuing) Or "Gee, Vin . . . are you as confused about God as me, an' do you think that we're slowly becomin' the parents we fought with?" You ever see Ma an' Dad talk when we were kids? (A beat) What do you do, Sandra, when you got a problem with "The Big Vin?" Huh? What clues do you give 'im that something's wrong? Maybe slide his plate in front of him a little harda' than usual?

SANDRA: We . . . just get by it . . . and . . .

DOLORES: An' it disappears, right?

SANDRA: Look . . . we . . . I don't have the problems you have, Dolores. The kids take up a lotta time and . . . (angrily) I think you should go now! Really . . . put ya' coat on an' leave! Of everybody who deals with you, I am the straightest when it comes to tellin' you stuff!

(throws Dolores her coat, moving her to the door)

DOLORES: (holds her hand up) SSSH!

SANDRA: Don't tell me to . . .

DOLORES: (waves) Be quiet for a . . . (Sandra watches Dolores walk to the door and listen; she reaches for her Dustbuster and holds it like weapon) You hear something?

SANDRA: (close to Dolores) No . . . I . . .

DOLORES: SSSH! (beat) There's someone out there . . . (returning to table) Footsteps. First one .

. . then another. (beat) Oh god . . . I'm sorry . . . (they face each other) Do you think it's nut house time?

SANDRA: I . . .

DOLORES: I might not have a choice . . .

SANDRA: (softly) A nut house might be good.

DOLORES: You think?

SANDRA: Maybe.

DOLORES: People be there to help.

SANDRA: True . . .

DOLORES: On Sunday afta'noons you could come an' sing to me . . . (sings, softly) "Will you still love me tomorrow?" (beat)

SANDRA: (crosses in front of Dolores) Uh . . . so listen . . . if Vinnie does come home . . . I'm goin' to tell him that, uh . . . you're here an' that I talked you into gettin' help at a, you know . . . a head hospital, all right? If he comes in, all right? That way there'll be no trouble or yellin' an' he'll understand. (beat) An' I lied before about when I said that, uh, Vinnie only shoved me. He's hit me. It started with the dog. He really used to go *off* on the dog an' sometimes for no reason. Just start beltin' it an' gettin' mean. (beat) One time last year me an' Vinnie was drivin' back from his mother's an' we were at a light over on Atwells Avenue, an' this motorcycle pulled up next to my window and I looked over an' saw this good-lookin' guy on the bike . . . kinda like Al Pacino with blue eyes an' he had on a brown leather jacket, pair a' ripped-up jeans an' boots. An' he smiled at me, then winked . . . just like in a TV commercials! I couldn't take my eyes off a' him . . ., an' then . . . I felt my hair bein' pulled an' before I knew it, my head was on the seat, an' I was bein' punched in the face! Not slapped, but punched! Same way he used to hit the dog and I . . . I could hear the motorcycle way off in the distance . . . (pause) Something went away with that guy . . .

(shakes it off, rubbing her eyes)

DOLORES: Don't worry about it . . .

SANDRA: That's it! You're staying here! I'll take care a' Vinnie. I'll take care a' him . . .

DOLORES: Sandra. . .

SANDRA: (angry, upset) I mean you're my sista', damn it! (beat) If we can't even . . . (beat) What's the point?!

DOLORES: I . . . I shot him, Sandra. This mornin.' I shot him. He hit me too many times, an' he won't let me outta his sight . . .

SANDRA: No, you didn't . . . tell me ya' didn't . . .

DOLORES: I couldn't take it no more an' Jerry was readin' the paper at the table an' I had his gun that I took from his coat an' I aimed it at a picture of Reagan that was on the front page, and I shot through the picture an' Jerry went flyin' back onto the floor an' he . . . he was laughin' . . . his shoulder was bleedin' and I ran out an' heard him say that he could kill me now, and I ran down the middle of Holmewood Street an' heard him in the car beepin' the horn and I kept runnin' an' could see people goin' to church and pickin' up their papers an' I cut . . . I cut through the Kentucky Fried Chicken place an' ran up the hill to Whitmarsh Street an' got on a bus. . . an' then I came here . . .

SANDRA: . . . uh oh, God . . . (confused) Uh . . . why didn't you (Dolores looks up at Sandra) I didn't know it was that bad. (silence) Shit, Dolores . . . I don't know what to say . . . I . . .

(Phone rings. Sandra is shocked for a beat then answers) Hello . . . (beat) Yeah . . . she's here . . . what? (takes a deep breath) I guess so right, right . . . I know . . . I'll bring her an' shut up, Mary Ann! 'Cause I'm bringin' her! Fine . . . right bye . . . (hangs up phone and turns to Dolores, who appears drained of all emotion) Police found Jerry in his car . . . dead. Bled to death on Broad street. (A chill passes through Dolores. She takes a deep breath and slowly exhales)
```

---

## IC-0577: Dos Corazones (Two Hearts)

- Title: Dos Corazones (Two Hearts)
- Author (byline): Richard Helleson
- Work: The Best 10-Minutes Plays: 2012
- Publisher: Smith and Kraus
- Publication date as stated: June 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ANA, CHERYL
- Teaser before the introduction: No
- Spoken words (computed): 2000
- Already set (do not supply): none

### Source block (context only)

```text
Author: Richard Helleson
Book: The Best 10-Minutes Plays: 2012
ISBN: 978-1575257938
Publisher: Smith and Kraus
Date (Month/Year): June 2013
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Cheryl, in the throes of what appears to be postpartum depression, pours her heart out to Ana, another new mother who shares her room.

ACTRESS 2: She discovers that Ana speaks only Spanish, while Cheryl speaks only English.

ACTRESS 1: The two begin to communicate around language rather than exclusively through it.

ACTRESS 2: Ana, who has almost nothing, cannot understand why Cheryl-who appears to have almost everything-is so upset over becoming a mother. In particular, she seems most bitter over a gift from her husband: a necklace featuring a pendant of two hearts.

ACTRESS 1: Cheryl ultimately reveals the source-and depth-of her frustration and her fears, and learns from Ana the real meaning of . . .

TOGETHER: Dos Corazones by Richard Helleson

In the dark, a woman humming a lullaby. CHERYL lays there, asleep. - no makeup, exhausted eyes, hair which has long since been given up on - she is moving-in the throes of an increasingly intense dream. ANA the other mother-stops rocking and returns her baby to his tray. She settles the baby, then turns her attention to CHERYL, who thrashes and ultimately cries out. The cry wakes her; she seems to be gasping for air, then is startled by ANA’s presence. She exhales deeply, and sinks back into her pillow. A moment, as she appears to be holding back tears; then she turns to ANA, who simply watches.

CHERYL: I’m . . . I'm sorry. (Sighs; shakes her head. Then she looks at ANA for a moment,

who is still silent. Tired and somewhat mystified:) I was . . . . swimming. In some
```

### Performance text (classify this)

```text
sort of lake-I was way out there. And I got so tired of kicking . . . . my legs just got heavier and heavier, and I started to sink. I tried to fight it, but the harder I tried, the faster I went down. (Slight pause) And then I remembered . . . that the human body floats. Right If you just let it go, it floats. So I just . . . . let everything go. . . (Pause) Finally I decided that I would just drift back to the shore. Only there wasn't any shore. I looked around, and there wasn't any land at all. I thought, my God, nobody knows where I am. (Tears up.)

Nobody knows. (She deals with the tears, but there is a long pause. ANA continues to look at her; CHERYL responds with a half-smile.)

ANA: Tu bebe esta bien? [Is your baby alright?] (CHERYL and ANA look at each other. More deliberately) Tu be be . . . [Your baby . . . ] Esta bien? [Is she alright?]

CHERYL: (Slight pause; nods a bit too much.) Um . . . . Yes, she's mine . . . . Definitely mine . . . (Smiles at ANA, who smiles back and nods. Indicates ANA’S baby.) Yours?

ANA: Era un poco malo al principio-pero, es mejor ahora. [He was a little sick at first-but he's better now.]

CHERYL: (Who hasn't understood a word, nods.) Ah. (pause) Listen, um . . . (Louder, as though that would help.) I'm sorry I woke you up. I'm sorry, OK? (More to herself) I'm sorry about everything.

ANA: No hablo mucho Ingles- [I don't speak much English-]

CHERYL: Oh. Um, whatever . . .

ANA: -pero, algunas veces puedo entender. Sabes? [-but I can understand it sometimes. You know?] (Gestures to her ear and her head.) lngles? [English?]

CHERYL: You . . . . hear it OK?

ANA: Mas 0 menos. Hablas Espanol? Un poco? [Sort of. You speak Spanish? A little?]

CHERYL: Um, yeah, un poco. El Espafiol de High School, but . . . (Gestures as of language flying out of her head.) Ffftt. Adios.

ANA: Otra lengua---es muy dificil. [Another language-it's very hard.] (With great effort) "Have a nice day."

CHERYL: Oh, the basics, huh? Um . . . "Dos margaritas, por favor."

ANA: Eso no estuviera mal . . . [That wouldn't be so bad . . . ] "Big Mac with fries."

CHERYL: "Hola, Paco! Que tal?"

ANA: "I am having a baby."

CHERYL: I am having a baby . . . (Her smile fades.)

ANA: Esta bien? [Is that O.K.?]

CHERYL: Sure. Perfecto. (She sniffles again and reaches for Kleenex. ANA watches her for a moment.)

ANA: Tu hija es muy bonita. [Your daughter is very beautiful.] (Slight pause.)

CHERYL: Oh. A girl. You have a little boy?

ANA: Si. [Yes.]

CHERYL: Your first? Primero?

ANA: (Pause; nods slowly.) Si. Nuestro primero. Til tambien? [Yes. Our first. You too?]

CHERYL: Mmm-hmm.

ANA: Como se llama? [What's her name?]

CHERYL: Um . . . Me Ilamo Cheryl.

ANA: Mucho gusto. Me llamo Ana. (Slight pause) ( Y la bebe? [And your baby?]

CHERYL: (as though she's just discovered the name herself) Clare. It's Clare.

ANA: Clare. Bonito. [Clare. Pretty.]

CHERYL: How about yours? Como se llama?

ANA: Martin.

CHERYL: Marteen. That's a nice name . . . You must be happy to have a son. Very proud.

(Does "proud)]

ANA: Si. [Yes.]

CHERYL: I think Nate wanted a boy. He didn't say anything, but . . . (Begins absently fingering necklace she wears.)

ANA: (after a moment) Tu collar es muy bonito. [Your necklace is very pretty.]

CHERYL: (in her own thoughts) Hmmm?

ANA: (pointing) Tu collar [Your necklace]

CHERYL: This?

ANA: Si. Es tan bonito. Tu esposo te lo regalo? [Yes. It's so pretty. Your husband gave it to you?]

CHERYL: Yeah. It's from my esposo.

ANA: Dos corazones. [Two hearts.]

CHERYL: Dos . . .

ANA: Corazones. [Hearts.] (Does the "heart" beating in her chest.)

CHERYL: Hearts. Yes.

ANA: Ah . . . . que bueno. [Ah . . . . Nice.]

CHERYL: (flatly) Yes it is. (Pause; begins to cry again.) This is so stupid . . .

ANA: Que te pasa? [What's the matter?]

CHERYL: I just . . . . never mind.

ANA: (after a pause) Por que estas tan triste? [Why are you so sad?] (Slight pause; CHERYL looks away.) Tienes un bebe bonita - es un tiempo feliz - pero estas triste. Por que? [You have a beautiful baby--it's a happy time--but you're so sad. Why?]

CHERYL: Porque . . . . .It's all such a lie! Everything they tell you, everything they say is going to happen to you . . . . no es verdad, you know?

ANA: (puzzled) "No es verdad"? ["It's not true?"]

CHERYL: It's just -- this is the answer to the question, right? One of the questions. "How much weight have you gained?" Four hundred pounds - go away. "When are you due?" When, when, when. My God, there it is, just staring at you! . . . And then it's next week, and then it's this week, and then it's tomorrow . . . and then it's today . . . And then it's . . . yesterday, and then it's last week, and then . . . it happens. And it's such a lie.

ANA: No entiendo . . . [I don't understand . . . ]

CHERYL: Here. Por ejemplo. (Retrieves magazine from table, opens it to a page, shows ANA.) Look at that. Tell me that's the truth. She just had a baby? Right. I mean, look at her! She's so . . . Sexy! She looks sexy! Like, "That was fun -- wanna start on another one?" Look at me! I lost thirty pounds in thirty seconds -- I feel like some kind of cow. (ANA looks through the magazine some more.) But that's the way you're supposed to be, right? Glowing - like the moon. (Slight pause) And nobody cares. Nobody. Except the nurses, and all they want to know is "How are your stitches? (Shakes her head, sniffling.) Everything was supposed to stop and wait-and it just kept going. Just kept right on going, like, So what? You thought you were special? (Pause) Yes. I thought I was. Kind of forgot to tell me about the triste, huh?

ANA: (Nods quietly, almost to herself) "En tristeza tendras hijos." ["In sorrow thou shalt bring forth children."]

CHERYL: Hmmm?

ANA: En el Biblio? Dios? Es . . . su primero castigado. En todas las madres-tristeza. "En tristeza tendras hijos." [In the Bible? God? It's . . . his first punishment. On all the mothers yet to come - sorrow. "In sorrow thou shalt bring forth children."]

CHERYL: I guess.

ANA: Pues . . . . Por que tuviste un bebe? [So . . . . why did you have a baby?] (A pause; CHERYL shrugs.) (Pero, si la quieres, no? Si la querias? [But you wanted her, didn't you? You must have wanted her . . . ]

CHERYL: I don't know . . . I don't remember .

ANA: No entiendo . . . . [Tienes un bebe, y eres tan resentida! [I just don't understand . . . . You have a baby, and you're so . . . resentful!]

CHERYL: Look-

ANA: Por que? Tienes flores, y globos, y tienes una hija saludable! [Why? You have flowers, and balloons, and a healthy child!]

CHERYL: I DON'T REMEMBER, OK? I DON'T REMEMBER WHY. Just . . . (quieter) I don't remember. (ANA turns away. CHERYL looks over at her, after a long pause:) Part of me . . . por mi madre, maybe. (Slight pause) And . . . por mi esposo. To have . . . something more between us. Mas . . . . amor . . . (fingering the necklace again) And Nate was incredible. He really was-the whole preg-nancy. We took those classes-clases? De childbirth? We'd do these pretend delivery room scenes, and he was totally in charge! "No monitors." "We're not gonna have drugs." "Get that LV. away from her!" I felt so safe. (Slight pause) And then this morning . . . He didn't say a word all the way to the hospital. We get here. . . . And you know what he does? He leaves. Hasta la vista. My labor takes off, and he goes to the bathroom! I couldn't believe it! (A sniffle or two.) Oh, and then? When he finally comes back? All this crap from the childbirth books finally kicks in. "Honey! I'm so proud of you! Thank you for working so hard!" (Pause; quieter) And then it's over. And I hold out my hand for him . . . . and I look up to see his face. What depth of love that I've never seen before will I see in his eyes? And you know what? I don't know. Because he's across the room looking through the video camera which he's holding about six inches over the baby. "Isn't this great? God, this is so great!" (tearing up again) He never even looked at me. (Pause; playing with the necklace again) And mi wonderful esposo . . . . went away for a long time, and then he came back-and he gave me this. (Tears up again.) He thought I was crying because I was happy.

ANA: (referring to the necklace.) No le gusta? [Don't you like it?]

CHERYL: I have no idea what it means! You want to know "por que"? Well so do I! Por que this?! It doesn't make any sense!

ANA: Dos corazones. [Two hearts.]

CHERYL: I know that, but . . . . Which two?! (ANA shakes her head slightly, that she doesn't completely understand.) Una familia? But that's three hearts, not two! Or, it's him and me? Like when you get married, it's two hearts with an arrow through them or something? Only it's not him and me anymore! That's over. (Sniffles a bit.) Or maybe it's something about what he loves-the baby and me. But he should be wearing that, not me! I don't know what it means! He's hanging it around my neck, and I don't know what it means!

ANA: Y tu? [And you?]

CHERYL: What about me.

ANA: Tuviste el bebe por tu mama . . . y por tu esposo . . . . No la tuviste por ti? [You had a child for your mother, and for your husband. What about for yourself?]

CHERYL: I told you, I don't remember! No recuerdo.

ANA: Pero . . . cuando la abrazas . . . No te acuerdas por que la tuviste? [But . . . . when you hold her . . . . You remember then, don't you? Why you wanted a child?] (Cradles an imaginary baby.) Cuando la abrazas . . . [When you hold her . . . ]

CHERYL: When I hold her . . . ?

ANA: Si. Cuando estan aqui . . . . Te acuerdas por que la querias? [Yes. When they're right here . . . You remember why you wanted her?] (ANA looks at CHERYL, who is silently crying.) Cuando la abrazas? [When you hold her?] (CHERYL shakes her head, trying not to sob.) No? (CHERYL shakes her head again; very gently:) Por que? [Why not?]

CHERYL: Because I've never held her. (ANA looks at her, not quite understanding.) I've never . . . (Imitates the action of holding the baby, then throws her hands up.)

ANA: No has abrazado? [You've never held her?]

CHERYL: I can't . . . I just . . . . (Lets herself cry.) I wanted her so much-and then . . . . Everybody else had her. She was stressed, during the delivery-they took her down to the ICU for awhile . . . I never even got to touch her. I was so afraid . . . what if she was dead, or . . . ?

ANA: No, no.

CHERYL: But when they brought her back later . . . I didn't want to touch her . . . I wanted them to take her away. Something in me . . . I wanted her to be dead.

(She continues to weep. ANA climbs into CHERYL's bed and puts her arms around her.) How can I be her mother? I can't even hold her!

ANA: Ssshhhhh . . .

CHERYL: I want her so much . . .

ANA: Alli esta, [But she's there.]

CHERYL: Here. I want her here. (Her womb.) I want her inside, where she's safe, and . . . . she's mine . . . and I can hold her with my whole body, all the time-not out where they can take her away . . .

ANA: Esta bien . . . [It's alright . . . ]

CHERYL: I want her on the inside, and Nate and me on the outside and nothing would change. But she's gone . . . And he's . . . . And I'm . . . . (Looks at ANA for a moment; then, a tearful laugh.) And you don't understand a thing I'm saying do you? God . . .

ANA: Yo no-? [I don't?]

CHERYL: Usted . . . no conoces . . . . Never mind.

ANA: Pero sf te entiendo. [But I do understand.]

CHERYL: No, you don't .

ANA: No, no, no---escuchas . . . [No, no, no---now listen . . . . ] (Backs off so that CHERYL can see her full face.) Nos entendemos aqui. [We understand each other here.] (Her heart.) Es la unica cosa que importa. [That's the only thing that matters.] (indicating the babies) Porque tenemos nuestros nifios. Porque somos madres, ahora. Y creo . . . .. Los hombres-si?- [Because we have our children. Because we are mothers, now. And I think . . . . Men-yes?]

CHERYL: Men.

ANA: Hablan de "corazones rompidos." Sabes? [They talk about "broken hearts." You know?] (Makes a breaking motion with her hands.) Corazones rompidos.

CHERYL: Broken hearts?

ANA: Todo el tiempo-los hombres: [All the time-men] (Doing despairing male voice) "[Ay! Ella se rompio mi corazon, iVOY a morir!" ["Oh! She broke my heart. I'm going to die!"] (CHERYL smiles.) Los corazones de los hombres nunca se rompen. Rompen sus cabezas--sus abrazos- [Men's hearts never really break. They break their heads-their arms-] (A dismissive gesture. Slight pause.) Pero, por nosotros . . . . en eso . . . [But for us . . . . in this . . . ] (Gestures around the room, the babies.) El corazon de la mujer en verdad se rompe. [The heart of a woman truly breaks.] (The breaking motion again, using her own heart.) Rompe a la mitad. [Breaks in half.] (using each fist as a heart) Y eso es que sabe solamente las madres: como siente tener dos corazones en un cuerpo. Uno aqui- [That's what only mothers know: how it feels to have two hearts in one body. One here-] (her chest}-y uno aqui. [-and one here.] (her womb) Y un corazon siempre pulsa cerca la otra. Aunque cuando se vaya de su cuerpo. [And that heart always beats near your own heart. Even when it goes out of you.]

(Indicates the second heart leaving her body.) Aunque cuando se pierda . . . . Aunque si se morio su nifio, tienes dos corazones. Siempre. [Even when you lose it. Even if your child dies, you have two hearts. Always.]

CHERYL: (Slight pause; getting sense of the last part.) Wait . . . ? mono . . . .

ANA: (touching the necklace) Creo que tu esposo te quiere mucho--- [I think that your husband must love you very much-] -para te entiende tan bien. [-to understand you so well.] (She slowly returns to her own bed.)

CHERYL: Morio . . . dies? A child-dies? (ANA says nothing.) What-que nifio? (ANA says nothing.) Martin . . . . Es your first-your primero . . .

ANA: (looking at her baby, and nodding) Si. El primero. [Yes. The first.]

CHERYL: How many . . . . Sus nifios. How many have . . . morio. (Pause; ANA holds up three fingers. A long moment, then:)

ANA: Dos . . . [Two . . . ] (Gestures as of something flushing out of her body.) Eso ya paso. Ellos no viviera-nunca seran bebes. [It happens. They wouldn't have lived-they were never really babies anyway.] (Slight pause) La tercera . . . Su cuerpo nacio-s-pero su espiritu [The third one. Her body was born-but her soul] (Indicates a soul flying up=-gone.) Ya se fue. [Was already gone.} (Smiles slightly.) Era muy pequefia, pero . . . . era tan linda. [She was very small, but . . . . she was so pretty.] (Again, cradles an imaginary baby.) La abraze por tanto tiempo como pude. Pretend! que ella estaba durmiendo. [I held her as long as they'd let me. I pretended that she was just sleeping . . . ] (She begins to hum the lullaby-first without words, then adding the words quietly. After a moment, ANA sees CHERYL staring at her, and stops singing abruptly.) Perd6name---es tarde. [I'm sorry-it's late.]

CHERYL: No . . . It's a beautiful song. (Looks down, holding the necklace in the palm of her hand.)

ANA: No te preocupe que significa el collar. [Don't worry about what it means.] (indicating the baby.) Abrazala. Mientes puedes. [Hold her. While you can.] (A pause. ANA checks on her own baby; as she does, CHERYL slowly and painfully moves to the edge of her bed. ANA begins humming the tune again. CHERYL walks hesitantly over to her baby, then stands and looks down at her. The room light, and then the moonlight, fade out.)
```

---

## IC-0578: Drop Dead Gorgeous - Screenplay

- Title: Drop Dead Gorgeous - Screenplay
- Author (byline): Lona Williams
- Work: Not specified
- Publisher: New Line Cinema
- Publication date as stated: 1999
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS 1, ACTRESS 2, GLADYS, BECKY, TESS, AMBER, TOGETHER, ACTERSS 1, VOICE OVER, JOHN, HAROLD, JEAN, LESLIE, IRIS, LISA, MAYOR, PASTOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1185
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lona Williams
ISBN: N/A
Publisher: New Line Cinema
Date (Month/Year): 1999
Full Screenplay available online at
https://cemp.ac.uk/scriptzone/script.php?type=download&id=182
Or purchased from Scriptfly.com
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: In the heart of small-town Minnesota, where the American Dream wears a sash and heels, the American Teen Princess Pageant isn’t just a competition — it’s survival.

ACTRESS 2: Every year girls with big hair and even bigger dreams take the stage.

ACTRESS 1: For some, it’s tradition. For others, it’s escape. For one… it’s destiny.

ACTRESS 2: And somewhere between patriotic speeches, talent routines, and suspicious “accidents,” we begin to realize that in Mount Rose . . .

ACTRESS 2: Winning isn’t everything.
```

### Performance text (classify this)

```text
Suggested Roles:

ACTRESS 1: Gladys, Amber’s Mom (Annette), Tess, John, Harold, Jean, Iris, Mayor

ACTRESS 2: Becky, Amber, Voice Over, Leslie, Lisa, Pastor

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

GLADYS: (Pg 48) Welcome to the Mount Rose American Teen Princess Pageant. Every contestant you'll meet tonight is special and unique, [and] they all have one thing in common. They're all "Proud - to - be - an - American!" (Pg 4-5) I know what some of you say, "Pageants are old fashioned" and "demeaning" to the girls -- things are different here in Mount Rose! (Pg 9-10) When I was seventeen, I was crowned American Teen Princess. And this year. . . drum roll please, my daughter, Rebecca Ann Leeman is competin'.

BECKY: (holding a 9 mm which she loads while she is speaking) Hi, I’m Rebeca Leeman, [president of the] Lutheran Sisterhood Gun Club. My mom gave me this nine-mil for my 13th birthday. I'll always remember what she wrote in the card: “Jesus loves winners.” That’s why, no matter what I do . . . (shoves magazine back into her pistol) I aim to win. (smiles to camera, then kisses her 9 mm)

TESS: (Pg 11) (holding a dachshund) Tess Weinhaus (fake smile as Kenny licks her face) This is Kenny. Spike, my German Sheperd, went to live with on a farm after he attacked me. (quick to reassure) It wasn't his fault. I had beef jerky in my front pocket. (pulls up shirt) They re-made my belly with skin from my butt.

AMBER: (Pg 9) (sweet as pie, with a wide-eyed expression) Hi, I'm Amber Atkins. (Pg 20-21) I got dreams of getting’ out of Mount Rose and bein’ a big-time reporter like Diane Sawyer. I mean, guys get out of Mount Rose all the time for hockey scholarships or prison. But the pageant’s kinda my only chance. (she’s interrupted)

AMBER’S MOM, ANNETTE: (off stage, yelling, coughing) Hey, Amber, y'get my smokes?

AMBER: (fake smile) That’s my mom. (yelling offstage) I'll get them in a sec!

GLADYS: (Pg 46) Tomorrow night, all but one of these girls will walk out of here a loser.

TOGETHER: It’s the only thing.

ACTRESS 2: Welcome to Drop Dead Gorgeous; screenplay by Lona Williams

ACTERSS 1: . . . where the smiles are bright, and the competition is fierce.

VOICE OVER: (music plays) (Pg 24-25) Judge #1 John Dough!

JOHN: Never judged a pageant before in my life. Nope. Never around young girls. Even if I was, why would I wanna be, y'know? I-I-I don't get off on that kinda . . .

VOICE OVER: Judge #2: Harold Vilmes!

HAROLD: I get made a judge, then the furniture store hires us to paint the whole damn thing. (removing cap) We're gonna use the money to get our mamma a proper headstone. Oh, and move her out to the cemetery.

VOICE OVER: Judge #3: Jean Kangas!

JEAN: (meek, middle-aged – she simply waves to the audience)

GLADYS: (Pg 23) The “Judges Interview -- (to girls) Remember the judges are as nervous as you are.

VOICE OVER: [What makes you] (Pg 48) proud to be an American?

BECKY: Mount Rushmore, because to live in a country where you can take an ugly old mountain and put faces on it, faces of great Americans, who did so much to make our country super great, well that makes me -- Rebecca Leeman – PROUD TO BE AN AMERICAN!

TESS: (Pg 50) (awkwardly) Uh . . . my Uncle Phil’s World’s Largest Ball of Twine, in Bundy Minnesota, makes me . . . um . . . it makes me proud I’m American. (embarrassed) I kinda misunderstood the assignment.

HAROLD: (Pg 42) [Okay, next question] (looking at his clipboard, has trouble reading) Uh . . . If you could be any tree in the woods, what kind of tree would you be?

TESS: (long pause, then brightly) Dogwood! (barks)

BECKY: One with a strong roots, a solid Christian trunk and long leafy branches to provide shade for handicap kids on a hot summer day.

HAROLD: (Pg 44) Amber Atkins . . . Name and spell all the United States in alphabetical order.

AMBER: Seriously? (can’t believe what she’s hearing) Well, Alabama: A-L-A-B-A-M-A . . .

(continues spelling in fast motion, silently, then a bit out of breath) . . . Wyoming: W-Y-O-M- I-N-G (Harold hoots and hollers, gives Amber a standing ovation, clapping awkwardly) **** The Talent Competition***

LESLIE: (Pg 55-56) (in her cheerleading uniform performs an amazingly “sexy” wrestling cheer) Roll him over (clap, clap, clap) Lay him flat (clap, clap, clap) Pin his shoulders (clap, clap, clap) To the mat (clap, clap, clap) Yeahhhh! (jumps and kicks) (applause!)

GLADYS: (Pg 57) (backstage) Amber, I hate to be the bearer of bad news, but rules state that a costume must be okay’d at least a week in advance. And this . . . (pointing at Amber’s costume) This is why we have the rule. I couldn’t allow this on stage! We have kids in the audience!

AMBER: (Pg 56-57) This, this . . . This is bulls***!

IRIS: Amber Atkins! That is not American Teen Princess language!

AMBER: Good, because this isn't an American Teen Princess Pageant -- it’s, it’s Nazi Germany! (Pg 9) [I only] signed up because two of my favorite people in the world competed. My mom and Diane Sawyer . . . I hope I end up more like Diane Sawyer than my mom.

AMBER’S MOM, ANNETTE: (overhearing) Amber! (storms off)

AMBER: (Pg 35) (as camera’s swoop in, Amber readjusts for the audience, sweet as pie again) Oh no! Is my mom okay? (exits to find her mother)

GLADYS: (Pg 56-57) (motions the cameras to follow as the returns to the stage) Now, with overwhelming pride, I introduce contestant number 6 – Rebecca Ann Leeman! (Pg 23) She’s been singin’ and dancin’ since she was knee high to a pig’s eye.

BECKY: (applause as Becky takes the stage with a mic. She wears a poodle skirt, sweater . . . music) I've got a very special fella in my life. I do . . . And if nobody minds, I’d like to sing a little song, just for him. (to the tune of I Can’t Take My Eyes Off You, she sings) You're just too good to be true. / Can't take my eyes off of you. You'd be like Heaven to touch. I wanna hold you so much . . . (time lapse)

GLADYS: (Pg 60) Boy, I’d hate to follow that. Wow! (Pg 54) Our next contestant . . Tess Weinhaus!

TESS: (droning on at the microphone) The beagle is known for it's howl. "Aaauuuhhh." The Pekinese has it's own distinctive bark. "Yip, yip, yip." Not to be confused with the Chihuahua's, "Yap, yap, yap." ****Cut to Backstage****

AMBER: (Pg 37-39) Mom, uh . . . . I’m – I’m – oh God . . . (starts to cry)

AMBER’S MOM, ANNETTE: (always with her cigarette) Oh-Jesus-Mary-n-Joseph, pregnant!? If you are, sweetie . . .

AMBER: Mom!!! First of all, I'm not pregnant. (deep breath) Okay. I’m thinkin’ . . . I-I-I’m gonna quit the pageant. (softly) It’s scary.

AMBER’S MOM, ANNETTE: Let me tell you “scary,” Amber. Look at me. I’m a “lifer” here. Best I can hope for is to end up in a decent “raisin ranch” where they’ll change me twice a day. (smiling) Amber, this pageant is your ticket out of here. I know you can win! I love you so much.

***** Back on-stage******

GLADYS: (Pg 60) (pauses as Iris runs on stage and whispers something in her ear) I was just told that contestant number 7, Lisa Swenson, has quit the pageant.

LISA: (runs out on stage) (Pg 59) And since my costume was okay’d a month ago, I’m givin’ it to Amber!

GLADYS: (with no other option) (Pg 61) . . . Number 8, Amber Atkins . . . (Music)

AMBER: (steps to center stage and performs an amazing tap dance routine. May include moon walking, River Dancing and moves never seen before. Make this hilarious) **** Final Awards Ceremony in progress****

GLADYS: (Pg 63) (DRUM ROLL; opens envelope) And the 1st runner-up is . . . contestant #8, Amber Atkins. (shock and disbelief, but then Amber steps forward to take the trophy)

AMBER: (Pg 65) (tearing up) Well, at least, y’know, I got to perform. And Mom got to see me.

GLADYS: (Pg 63-64) (ushers Amber aside) And finally, the moment I know I've been waiting for . . . she'll be competin' for the title of Minnesota American Teen Princess . . . my daughter – Number 7, Rebecca Ann Leeman!

BECKY: (Pg 65) (almost manically rushes forward) Goodness-gracious, it hardly seems real, y'know? I mean, I won! I'm the winner! (with each photo she changes her smile and expression. She loves this) AMBER’S MOM, ANNETTE: (Pg 64) (from the audience, still chain smoking) We was robbed! ***** The next day: Main Steet – Pageant Parade*****

MAYOR: (Pg 67) (into bullhorn) Welcome to our first ever American Teen Princess Parade – which also happens to be the unveiling of our new sewer system! While Becky gets on her float, any questions about the new sewer?

BECKY: (Pg 68) (as Gladys helps her climb onto the float) It smells funny. Like gasoline. My dress’ll reek.

GLADYS: C’mon, Rebecca. This [swan float] cost your dad a pretty penny. Now get your a** up there and show me some teeth!

AMBER’S MOM, ANNETTE: (Pg 64) (near the float, still chain smoking) We was robbed!

(creepy, sinister smile; then takes out lighter to light another cigarette) . . . (Suddenly, like a gasoline soaked pinata, the float EXPLODES!) ***** Days later – Funeral*****

PASTOR: (Pg 71-72) That’s why, dear Lord, it’s with such great sorrow that we turn over to you a young woman whose dream of ridin’ on a giant swan brought about her untimely death.

IRIS: (approaches Amber) As actin’ President of the Mount Rose Civil Servettes, it’s my duty since Becky can’t fulfill her duties – cause she’s dead-n-all – to make you Mount Rose American Teen Princess. (puts tiara on Amber)

AMBER: (Pg 73) Oh my God . . . Okay, okay . . . (squeals) I only got four days . . . I gotta practice! (turns to cameras) (Pg 49) Living in a country where no matter who you are or where you come from, you can grow up and become what you've always dreamed of, makes me, Amber Atkins, proud to be an American!

AMBER’S MOM, ANNETTE: (off stage, yelling, coughing) Hey, Amber, y'get my smokes?
```

---

## IC-0579: Eleemosynary

- Title: Eleemosynary
- Author (byline): Lee Blessing
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ECHO, DOROTHEA, ARTIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1850
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lee Blessing
ISBN: 978-0822203544
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
Actress 2: That’s Echo. She’s amazing – a true genius and so young. Through a series of flashbacks, you’ll find out more about her, her mother and her grandmother soon - a character study in triplicate. None of these women are exactly like me or you, or probably anyone we know, but you’ll find bits of them in all of us. And perhaps enough information to contemplate some questions.

As women, how do we make our way through life? How do we behave as parents? How do we become who we are because of or in spite of our parents? Let’s rejoin Echo now in

Eleemosynary by Lee Blessing
```

### Performance text (classify this)

```text
Suggested Roles: Actress 1: Dorothea and Echo

Actress 2: Artie

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

ECHO: (Pg 7) (to audience) Eleemosynary. E-L-E-E-M-O-S-Y-N-A-R-Y. Eleemosynary. It's my favorite word. Not just because I won with it, either. Eleemosynary: "Of or pertaining to alms; charitable." Eleemosynary. (slowly approaches the imagined image of Dorothea laying in bed, studies her for a moment) This is my grandmother. She had a stroke. (opening the drapes) She can't really talk. I can hear her, though. At least I think I can. She's seventy-five years old . . .

ECHO: (Pg 7-9) (to audience) My grandmother believed she could fly using only a pair of homemade wings. In 1958 she made a movie of herself and her daughter, my mother, trying it out. Mom was only fifteen then. (Echo steps into the scene as Dorothea)

DOROTHEA: (Speaking with force and assurance, as though to a film camera) Hello. I am Dorothea Wesbrook. Today I am going to prove that man - or, in this case, woman - can fly without the aid of any motor of any kind, using only the simple pair of wings you see my daughter, Artemis, wearing here. (Artie begins to edge off camera. Dorothea stops her gently without interrupting her speech) We will try two experiments today. First, the very steep hill, and second, the wooden tower. (turns to Artie, suddenly shouting) Flap! For God's sake, you call that flapping?! You're being filmed!

ARTIE: (running, flapping) It's not working! I'm not flying!

DOROTHEA: You will! Keep trying! Concentrate!

ARTIE: (suddenly drops the wings and speaks like a 30-year-old woman to the audience) Never have a daughter. Never have a child, for that matter, but never have a daughter. She won't like you.

DOROTHEA: Keep flapping! (Artie wails picks up her wings and begins flapping) (to camera) (Pg 11-13) Well, the very steep hill seems not to have done the trick. We are moving on, therefore, to the wooden tower. (Artie gives an "Are you serious?" look then climbs a ladder to the platform of a wooden tower while Dorothea watches) My daughter is now, oh, about twelve feet above the ground, and . . . Let go of the railing, dear.

ARTIE: (eyes closed) No!

DOROTHEA: Don't be stubborn. You want to fly, don't you?

ARTIE: No!

ECHO: (Dorothea steps out of scene to narrate as Echo) I do . . . I fly with words. Oh, I know it sounds stupid to say, but it's true. When I was still in my crib, my grandmother was constantly shoving words and numbers in front of me. My grandmother made me love words. My mom helped, too. A little. (steps back into the scene as Dorothea)

DOROTHEA: Why are you so afraid to make history, Artie? (to the camera, embarrassed) Well. . . it appears we will not be able to complete our experiment today.

ARTIE: (eyes closed, holding on) Damn right. You are nuts! And now you're nuts on film! (freezes)

ECHO: (Dorothea steps out of the scene to narrate as Echo) Dorothea was one of the notable eccentrics of her time. She went on to other projects: communication with the dead, spontaneous combustion, astral projection - but she never filmed those. I can feel my grandmother in me. My mother, too - a little. *****Scene*****

ARTIE: (Pg 16-17) (to audience) My mother made sure I had tutors from the age of four. My father worried that too much learning would hurt my hopes for marriage. But Dorothea told him a smart girl can hide what she knows, so there's still a chance for happiness. (Dorothea.)

DOROTHEA: (breaks in, to audience) Well, that's true in a way . . .

ARTIE: I'm telling this. (turning to audience) When I was eighteen, I got pregnant.

DOROTHEA: It was an accident . . .

ARTIE: Mother! In fourteen years of tutoring, no one - including my mother - ever brought up the facts of life. I didn't know anything about the men 'til I went out with one of them.

DOROTHEA: (speaking to an 18-year-old Artie) You can't be pregnant! You can't! You're eighteen. Your college career . . .

ARTIE: What college career? I'm going to be a mother.

DOROTHEA: No. No, you're not. You don't have to be. Think about it. (beat)

ARTIE: What - you mean give it up for adoption?

DOROTHEA: No. That would mean your father finding out. If he knew about this, he'd have you married to someone in five minutes - and no college, either. You have to do something else.

ARTIE: What? (beat) That's illegal!

DOROTHEA: In this state. But if you go . . .

ARTIE: No! I won't do that. It's a life. (beat)

DOROTHEA: (quiet, steadfast) It's that life or yours. . . If you keep it, none of our plans, none of your potential . . . You won't be you anymore. You'll just be something a child needs.

ARTIE: I don't want to be anything more.

DOROTHEA: When a soldier in battle suddenly has to kill someone, we say that's all right. It's his life or someone else's. Well, you have a choice, too. Between living your life or someone else's. And you have to choose now.

ARTIE: (to audience) I waited. A little while, anyway. But finally we crossed the state line, and (beat) I ran away right after that. Across three state lines. I lied about my age and got a job teaching at a private school. *****Scene***** [Many years passed. Finally, Artie called her mother]

ARTIE: (Pg 26-28) (on phone) Mom? I'm going to have a baby.

DOROTHEA: Is this your way of telling me you're married?

ARTIE: Yes . . . um, his name is Richard [and] I've finished grad school - Biochem.

DOROTHEA: That's lovely. When's the baby due?

ARTIE: Six months. (to audience) A week later, there she was. She bought a house on our block. I couldn't function with her around. She'd come over with some theory for making toads fly. . .

DOROTHEA: Don't get upset, dear. I'll be down the street when you need me.

ARTIE: (to audience) When I had my baby, she took me to the hospital.

DOROTHEA: (holds a baby in her arms) A girl. (suddenly lifts the baby high above her) This one will fly. I can feel it.

ARTIE: (to audience) One month after Echo was born, my husband died in a car accident.

ECHO: (Dorothea steps out of scene to narrate as Echo) When my father died, Mom didn't talk for days. That's what Grandma said, anyway. Not even to ask for food or anything. I think she really loved him. *****Scene*****

DOROTHEA: (Pg 14) (to Echo) Are we all waked up from our nap? We're all waked up and we're three months old, and we're ready to go to school. (tickling Echo) Do we like school? Of course we do. Listen, Artie - she's laughing.

ARTIE: She's laughing because you're tickling her.

DOROTHEA: Well, I'm sure that's part of it. (to Echo, playing with a toy alphabet over the crib) Do we know this letter? That's "A." Can you say "A?" All right, how about this one? "B."

ARTIE: Mom, she's three months old. She can't talk yet. It's physiologically impossible.

DOROTHEA: (smiling) Echo? Try these (dangling another string of letters) This is "Alpha." Can you say that? And this is "Beta."

ARTIE: (to audience) Those baby alphabets are the same ones she had over my crib. Pink for Latin, blue for Greek.

ECHO: (Pg 29) (Dorothea steps out of scene to narrate as Echo) When I was a year old, the three of us moved back East into Grandma's house [and for a year everything was fine . . . then]. *****Scene*****

ARTIE: (Pg 30-31) (beat) I have a job offer [in] Europe.

DOROTHEA: Are you planning to take Echo with you? (beat)

ARTIE: I want you to keep her.

DOROTHEA: Keep her? For how long?

ARTIE: For good. I want you to keep her for good.

ECHO: (Pg 11) (Dorothea steps out of scene to narrate as Echo) Dorothea raised me from the time I was two. *****Scene***** 5 years later

ARTIE: (Pg 33-37) I called up my mother once - from Europe - when Echo was seven. I had some news. (on the phone) I'm coming back. I have a job opportunity in the states. I won't come visit.

DOROTHEA: Call then. You can call us anytime. Do you want Echo back? (long beat)

ARTIE: No. (to audience) Once I got settled, I started to call my mother and Echo now and then. Things went on this way for . . . six years, actually.

ECHO: [Over time] Mom suggested spelling bees. It got pretty important. She ended up calling me a lot more. At twelve, I decided to be the greatest speller in history. For life!

ARTIE: (on the phone) I'll find one. Just a minute. (paging through a dictionary) Metamorphosis. You know that one, huh? Ok, how about . . . Syllepsis? You know that? (Listening, nodding.) What do you mean that's not a hard one? Oppugun is a hard one. Spell it.

ECHO: (dutifully) Oppugn. O-P-P-U-G-N. Oppugn. (beat, to audience) It was strange suddenly talking to her so much. (beat) I decided I was going to get Mom to the National Spelling Bee finals. Dorothea was coming. I wanted them both in the audience when I won it. To see that no matter what they'd done - no matter how they'd done it - they'd produced someone that was completely . . . all right. Someone with perspective. P-E-R-S-P-E-C-T-I-V-E. Perspective. *****Scene***** [At the national spelling bee – The final round – Only Echo and one boy are left]

ECHO: (Pg 37-39) Glunch. G-L-U-N-C-H. Glunch. (quickly) I knew I was right! Glunch is such an easy word. (beat) What's he getting? Donzel?! (suddenly outraged) He guessed! He guessed and he got it! (suddenly her public self) Yes, Ma'am, I'm ready. (listens) Palinode. P-A-L-I-N-O-D-E. Palinode. (her inner thoughts) This can't go on forever, buddy. I'm going to crack you like an egg.

ARTIE: Echo was a little different than I thought she'd be. I mean, she was terrific and everything, but she seemed so . . . desperate.

ECHO: (with great intensity) Come on, miss it! You don't know it. You know you don't. (eyes widen, in a whisper of awe) He missed it! Dear God, please let me win! Please! Just five minutes when I'm the most famous child in America, and Mom and Dorothea see it! (her public self again) Excuse me, could you repeat the word?

ARTIE: I didn't know why she was behaving that way, so competitive.

ECHO: Eleemosynary. E-L-E-E-M-O-S-Y-N-A-R . . . Y. (raises her arms in triumph)

ARTIE: I slowly made my way to the front of the room. Echo was being mobbed, but all I could look at was the boy she'd beaten. He looked like a dead mouse.

ECHO: (Pg 41) (to audience) Eleemosynary. That's the one I won with. (beat) I thought having both of them there would be a good thing. But it wasn't. It made me realize that I was just like them. I was just a very intelligent, vicious person. (beat) I called Mom a few times after the spelling bee. She was always civil, but . . . she was different. I stopped calling after a while. For two years we hardly talked at all. Then Dorothea had a stroke. So Mom came home. *****Scene*****

ECHO: (Pg 44-45) What's wrong with me? Why do you keep leaving me!?

ARTIE: Echo . . . ECHO: Why!?

ARTIE: (tiredly) I used to teach you wrong things. Do you know that? When you were little. Dorothea was with you every day, waggling those . . . goddamn letters and cooing. The two of you got along great. (sighs) So I taught you the wrong names for things. When you were starting to talk, I'd point at the floor and say, "ceiling." I'd point at the door and say, "window." And you'd smile and say ceiling and window, and I began to hope if I could just . . . retard you a little . . .

ECHO: Retard me?!

ARTIE: Just to be normal. I thought if you didn't seem so bright, she might get disinterested and leave us alone. But she didn't. She accused me of "intellectual child abuse." That sounds ridiculous, but it was true. I was angry at you. For picking her. For wanting her more.

ECHO: I wanted you both.

ARTIE: You couldn't have both. You got her. She was better for you than I could've been.

ECHO: Did you love me? When you left me with her? Did you?

ARTIE: Whether I loved you then or now ...

ECHO: Did you love me? Do you?

ARTIE: (beat) Yes. And no. It's always yes and no.

ECHO: (Pg 46-47) (beat) Maybe the smartest thing would be to forget you completely. And Grandma. After all, what did I ever get from the two of you, except a good education? You especially - what were you ever to me, except a voice on the phone now and then? Hiding behind spelling words, making excuses. Just a sound that said, "I love you, and I failed you." I hate that sound. And I will never settle for it, because no one failed me. No one ever failed me. Not Grandma and not you. I'm your daughter. That's what I choose to be. (beat) No matter what we've done - no matter how we've done it - we're all three of us, in our own way, completely . . . eleemosynary. E-L-E-E-M-O-S-Y-N-A-R-Y
```

---

## IC-0580: Fin and Euba

- Title: Fin and Euba
- Author (byline): Audrey Cefaly
- Work: The Best American Short Plays 2004-2005
- Publisher: Applause Books
- Publication date as stated: Aug 2008
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: FIN, EUBA
- Teaser before the introduction: No
- Spoken words (computed): 2180
- Already set (do not supply): none

### Source block (context only)

```text
Author: Audrey Cefaly
Book: The Best American Short Plays 2004-2005
ISBN: 978-1557837127
Publisher: Applause Books
Date (Month/Year): Aug 2008
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Fin and Euba are friends and co-workers at a paper mill in Cantonment, Florida.

ACTRESS 2: They also share space in a rooming house, which they are desperately trying to escape, due to the tyrannical landlady who has a penchant for strict rules and tacky yard art.

ACTRESS 1: Unbeknownst to Euba, Fin submits some of Euba's amateur photos to Life Magazine.

ACTRESS 2: Euba receives a reply from Life, but is reluctant to open it for fear or rejection, or worse…acceptance.

ACTRESS 1: Fin and Euba sit on the porch contemplating their lives and their plans for escape.

TOGETHER: Fin and Euba by Audrey Cefaly
```

### Performance text (classify this)

```text
note to actors Fin and Euba are poor and scrappy. They say and do things that may seem surreal or comical, but in all things there is a truth to their ways ... they are not caricatures. That is to say ... they are very real people with real problems. Every effort should be made to make them as human and as genuine as possible, to identify their core beliefs and to portray them honestly . . .

FIN: Hey.

EUBA: Hey. [They stare out at the highway. An occasional car speeds by.]

FIN: It's gettin' cold.

EUBA: Yeah, it's gettin' cold. [Silence.]

FIN: Bernice told me you got a letter in mail-call today.

EUBA: [Somewhat annoyed.] Yeah.

FIN: From Life magazine?

EUBA: Bernice talks too much.

FIN: Well, ain't you gonna tell me what it says? You been waitin' for that letter since June.

EUBA: No.

FIN: No?

EUBA: I ain't read it.

FIN: Why not?

EUBA: Personal reasons.

FIN: Oooh. Oh, I see. OK Alright. That's fine ... you don't want to tell me.

EUBA: Good.

FIN: Your best friend.

EUBA: Yup.

FIN: The only person you could trust in the whole wide world.

EUBA: Yup.

FIN: But if you don't want to tell me

EUBA: Nope [Silence.]

FIN: [Annoyed.] I shoulda' worn my jacket.

EUBA: Mnnn hmn.

FIN: Two weeks til' Thanksgiving ... can you believe that?

EUBA: Double shifts again all next week.

FIN: You're kiddin'?!

EUBA: Fat Charlie told Thelma-'n' Thelma told me.

FIN: Good! I need the money.

EUBA: I need sleep more than I need the money.

FIN: That's the truth. [Pause.] I heard something, but you ain't gon' like it.

EUBA: What?

FIN: Miss Vera's fixin' to raise the rent next month.

EUBA: Where'd you hear that?!

FIN: Bernice. Said she overheard her talkin' about it on the phone to Brother Herbert.

EUBA: How much?

FIN: I don't know. [Pause.]

EUBA: [Bravery.] You know I'd move in a heartbeat.

FIN: Me too.

EUBA: Too many rules.

FIN: I know it! Let's do it.

EUBA: What?

FIN: Move.

EUBA: You're crazy.

FIN: I'm serious!

EUBA: It's too far, Fin. The next rooming house is two miles down ... that's way too far to walk to work.

FIN: Lou Anne lives down there at Scooter's. We could ride in with her. And he don't have no rules, neither, except cash only.

EUBA: Cash only?

FIN: Cash only. And no pets.

EUBA: What about a fish? [Pause.] Could I have fish?

FIN: I bet you could have a fish. What like a goldfish?

EUBA: No .. one of them pretty ones ... with the pretty colors.

FIN: Oh yeah! I like them. Fish are good. [Pause.] What do you think?

EUBA: I don't know.

FIN: Let's just think on it.

EUBA: OK

FIN: We'll just think on it. That's what we'll do.

EUBA: [Trying to close the subject.1 OK Let's think on it.

FIN: [Overlapping.] OK [Pause.] I'm thinkin'. [They both sit quietly for a moment trying to work through the details.]

FIN: You alright?

EUBA: Yup.

FIN: They got a new foreman comin' in next week.

EUBA: Where's Lila?

FIN: Fat Charlie sent her home. She couldn't keep up.

EUBA: [Amused.] When's the baby due?

FIN: Any day.

EUBA: How's she look?

FIN: She looks good. She looks real good. Big.

EUBA: I miss havin' her on my shift.

EUBA: She'll be back.

FIN: Nuh uh! She's movin'.

EUBA: What?

FIN: Well, you remember how her husband went through basic training last summer?

EUBA: Yeah.

FIN: They just assigned him to a unit at Ft. Bragg and they're movin' soon as the baby's born.

EUBA: What?

FIN: She's mad as a hornet too. She just got the baby's room all fixed up and everything. [The front porch light flashes.] [To Euba.] 15 minutes. [Calling.] Yes, ma 'am!

EUBA: God, I can't stand that woman!

FIN: [Overlapping.] She gives me the creeps! Her and them 13 cats.

EUBA: Seventeen. Ginger had her litter this mornin'.

FIN: [A warning.] That's it! We're movin' to Scooters. [Pause.] I mean it, Euba! I'm callin' Scooter tomorrow. [Pause.] Euba?

EUBA: Yeah?

FIN: When you gon' open that letter?

EUBA: [Grimacing.] Life magazine does not care about any of the stupid pictures I took in high school, Fin. Get real.

FIN: I didn't send 'em those, Miss smartie pants. I sent 'em the ones you took at the plant during the strike last year.

EUBA: [EUBA has a moment of hope, but quickly dismisses it.] Whatever.

FIN: What if it's a job offer?

EUBA: Oh, get serious, Fin. You think you can just send my pictures to some big shot at Life magazine and expect a job offer?

FIN: [Overlapping.] Oh, give me a little more credit, will ya? I did not just send them to any old big shot. [Proudly.] I sent them to the Executive Editor, if you must know. I took his name right off the inside cover.

EUBA: [Sarcastically.] Now, that makes all the difference, don't it?

FIN: [Staring at EUBA blankly.] You are so negative. Negative. Negative. Negative.

EUBA: [Overlapping.] Realistic.

FIN: Yes. That too! And negative. [Pause.] I bet it's a job offer! What do ya think?

EUBA: I don't know and I don't care.

FIN: Don't lie.

EUBA: I ain't lyin.' I don't want to know.

FIN: Why?

EUBA: It's better not knowing.

FIN: Better?

EUBA: I didn't send the pictures, Fin! You did!

FIN: It's what you wanted.

EUBA: No, Fin. It's what you wanted.

FIN: You said. You dreamed about it.

EUBA: No I didn't.

FIN: Don't lie! Euba. You have been dreamin' about taking pictures for Life magazine ever since high school.

EUBA: OK, yeah, alright. Yeah, I dreamed about it, but that don't mean I want it. [Pause.]

FIN: [Annoyed.] That don't make no sense, Euba. Dreamin' ... wantin' ... same thing.

EUBA: No, it ain't. Dreamin' is dreamin,' that's all it is. Wantin' means you're willin' to work for it and I ain't and that's all.

FIN: What are you talking about?

EUBA: Do I dream about it? Yes! Of course, I do. When I'm out there on that line all day and my feet are so swole up I can't think straight? I dream about it. Or when Bugger James comes into my room stead of his own at 4 a.m. cuz he's so blind from drunk. I dream about it. Or how bout, every mornin' scrambling for a warm shower 'stead of ice cold, cuz I slept in two minutes late. Fin, I dream about getting out every minute of every day of my life.

FIN: Well, what are you waitin' for? [Holding up the letter.] This is your chance, Euba.

EUBA: [Taking the letter.] Because. If I open this letter. And it says what I know it's gonna say ...

FIN: What?

EUBA: ... then I have nothin'.

FIN: But what if they want you!?

EUBA: What if they don't?

FIN: What if they do?

EUBA: What if they don't?! What if I open that letter, and it tells me I'm no better than anybody else in this-

FIN: Oh, come on!!! If! had half your talent, I'd march right down to that office and I'd tell thatJat-bastard Charlie to kiss my ass. I'd quit. With no notice! And I'd start walking til' I hit Atlanta. And you wanna know what else?!?! I WOULDN'T LOOK BACK!!! I'D NEVER LOOK BACK! Not even for you, baby. Not even for you.

EUBA: Well, thanks a lot.

FIN: It's nothing personal.

EUBA: I know it.

FIN: Open the letter!

EUBA: Stop it!

FIN: Euba!

EUBA: Leave it alone, Fin.

FIN: It's a sin what you're doin.' Throwin' away your God-given talent.

EUBA: How come you can't just drop it?!

FIN: No, I won't. And you wanna know why?

EUBA: 'Cause you ain't got any dreams of your own, that's why! [Pause.]

FIN: [Stung.] Nice. Turn it back on me why don't you?

EUBA: [Overlapping.] I didn't mean it, I'm sorry.

FIN: [Overlapping.] Oh, save it, Euba! I know what I want. And you can call it dreamin', wantin' WHATEVER. Kids? Yep. On the list. One girl. One boy. And a husband some day, if! can find one who'll have me. Somebody to love. Somebody who will love me back. A white house, with a little wrap around porch ... on a little quiet street-

EUBA: [Overlapping.] Don't forget the white picket fence.

FIN: [Continuing defiantly.] in a little quiet city-that don't smell like ... something dead. And just maybe, when I'm old and ugly, I want a bloodhound named Jake ... who knows his name, who will come when I call him and who will love me, no matter what, cuz that's what dogs do.

EUBA: [Softening up now.] Sounds like you got it all planned out.

FIN: [Sincerely.] Yeah, well, I ain't special like you, Euba.

EUBA: Oh, come on-

FIN: No, no, it don't bother me. You bother me. You say you want a fish, but you don't even know what kind!

EUBA: Fish? Fish? We're talking about fish now? I know what kind of fish, Fin, I just can't think of the name, that's all.

FIN: My point exactly.

EUBA: I know what I want.

FIN: No, you don't.

EUBA: Yes, I-

FIN: No! No you don't, Euba. You sit here and [complain] and you moan about this place ... about gettin' out. But it's all just words, idn't it? You never do anything. You never do anything about it.

EUBA: I'm happy right where I am, thank you very much.

FIN: [Aghast.] Don't say that! Don't you ever say that!

EUBA: Leave it alone, Fin.

FIN: As long as you can live with it. [Pause.] Come Sunday morning and you're sittin' there, 7th row center at Southside Baptist. Trying to explain to the Good Lord why you took the gifts-the gifts-he gave you and THREW THEM ALL AWAY! You hear me?!?! Just threw 'em away. Now what do you think he would have to say about that?

EUBA: I can't speak for Jesus, Fin.

FIN: Well, I can. [Pause.] And I'll tell you what he'd say. Shame. On. You! Shaammme on you, Yolanda Eubanks! [EUBA quickly pulls out the letter and starts ripping it up.] Stop it! What are you doing?!?! Are you insane?!?! Euba!! [EUBA holds a lighter up to the letter in warning. A cold menacing demeanor washes over her.]

FIN: You wouldn't! [EUBA flicks the lighter "on. '1

EUBA: You wanna take that chance?

FIN: Don't do it. You'll never live it down, Euba.

EUBA: [Overlapping.] You better get back, Fin! Now, I need you to leave me be on this, you hear me?!?!

FIN: Euba, please!

EUBA: BACK AWAY! I'll torch it!

FIN: I believe you would. I do. I'm backing away ... see me ... I'm back. Now put the lighter down.

EUBA: [Pointedly.] Now, this is my life. My life. And it's mine for me to decide if I want to throw it away, you got it?

FIN: Yes!

EUBA: No more TALK! No more nothin'!!

FIN: [Overlapping.] OK Yes. Yes. OK I'm sorry. Please ... just ... just ... just ... put the lighter down. [Overlapping. EUBA accidentally burns herself on the lighter. She drops the lighter and the papers on the ground.]

EUBA: Ow! [Silence.] [A realization.] I'm crazy. I am. I'm crazy. That's the only explanation.

FIN: No. No.

EUBA: I mean it, Fin. Whatever this is ... It ain't normal. It ain't- something's wrong with me.

FIN: Euba?

EUBA: [Overlapping.] I'm scared, Fin. You hear me? I'm scared!

FIN: Of what? A letter?

EUBA: No! Of ... of everything. Afraid to go. Afraid to stay. Livin'. Dyin'. Stuck in this house with that crazy witch. No car. No phone. With no nothin', Fin, when you think about it. We work in a mill that spits poison twenty-four seven .... And the smell, God, that smell ... it turns my stomach, Fin. I can't get away from it. It's in my clothes, it's in my hair, it's in my sheets! Fin! It's in my sheets! I've probably got some sort of deadly disease ... eatin' away at me on the inside .... For Christ's sake, Fin, we have to wait for a northern wind to barbecue! God, I hate it here! I hate this place.

FIN: Then leave!

EUBA: [Quietry.] What if the next place is no better? Ya ever thinka that?

FIN: Wha-

EUBA: What if the next place ... is worse ... than this?

FIN: [FIN takes in her surroundings.i That's a scary thought, Euba.

EUBA: You make it all sound so easy. Just pick up .... Go somewhere ... do something ... I know there's better places, Fin. Don't think I don't know that. But, Fin ... I can't. I can't ... move. I can't I'm-I'm stuck.

FIN: You are NOT stuck. You listen to me. You are NOT stuck. Ain't none of us stuck.

EUBA: Yeah, I am. Oh, God, I can't breathe!

FIN: Shh shh ... OK, OK, caaallmmm down. Calm down. Take a deep breath. Take another one. Sit down here for a second and catch your breath. Whooo whooaa OK, now keeeep breathing .... Don't forget to breathe. Everything's gon' be back to normal here ... now just keep breathing. You OK? [EUBA nods yes. They sit in silence for a minute. FIN pats EUBA’s back and pushes the hair back from her eyes.] It's tough. I know. But ... it might help if you remember ... God never gives us more than we can handle. [E UBA slowly turns and stares blankly at FIN] [Backpedaling.] Well, sometimes. Sometimes he does. Sometimes, it is just a little bit more than we can handle. [Pause.] But that's why we have each other. [EUBA gathers the pieces of the letter and stands for a moment looking down at them. She is resolved now. She lights the papers.

FIN:. [FIN puts the blanket around her and sits. The lull of the crickets and heaviness of the air envelope them both. They resume once again to staring out at the lonely highway.] It's getting' cold out here.

EUBA: Yeah.

FIN: Don't you think it's gettin' cold?

EUBA: Yeah. [Pause.] Yeah, it's gettin' cold.
```

---

## IC-0581: Final Placement

- Title: Final Placement
- Author (byline): Ara Watson
- Work: Win/Lose/Draw
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MARY, LUELLEN
- Teaser before the introduction: Yes
- Spoken words (computed): 1534
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ara Watson
Book: Win/Lose/Draw
ISBN: 978-0822212621
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Placements in foster care have dramatically increased over the past 10 years. Today over 500,000 children in the U.S. currently reside in some form of foster care.

ACTRESS 2: What leads to such drastic measures by social service workers? Simply put, many of these children have suffered some form of serious abuse or neglect— removal of these children from their homes is a protective measure.

ACTRESS 1: The situation is stressful for all involved . . . parents, children and the social workers who attempt to intervene in the best interest of the child. Stress often leads to parental violence directed toward the social workers themselves. In fact, Seventy (70) percent of front-line caseworkers have been victims of violence or received threats of violence.

ACTRESS 2: In protecting children from domestic violence, the very people who intervene become targets themselves.

TOGETHER: Final Placement by Ara Watson.
```

### Performance text (classify this)

```text
MARY: (To Audience/Dictation) Last name: James. First name: Jimmy. Age: four years. Date: October ten, 1981. This office was contacted by Dr. Timothy Bowman of the Northside Medical Clinic concerning four-year-old Jimmy James. Dr. Bowman reported that he has treated Jimmy twice in the last six weeks-once for a cut over the eye and once for a broken wrist. The parents attributed both injuries to accidents. On each of the visits, Dr. Bowman noted the child had a number of bruises on his body which the mother explained resulted from Jimmy's-quote-"always falling down"-end quote. On the second of these visits with Jimmy, Dr. Bowman also noted burn marks on the child's buttocks which he believed were caused by a cigarette. He determined at this point to contact this office and request an investigation of the situation by the Department.

MARY: What are-? (A moment’s hesitation.) Hello. You . . . you startled me.

LUELLEN: There wasn't no one at the front desk.

MARY: Oh? Well, she. . . she must have stepped away a minute.

LUELLEN: I heard your voice, so I followed it, but I didn't want to disturb you. Boy, sure is quiet up here.

MARY: Yes. Yes, I guess it is.

LUELLEN: Where is everybody anyway? Looks like you're the only one in the whole place.

MARY: (quickly lying) No. Everybody's here. They're all . . . just busy. . . keeping their heads down. But. . . they're all here. I like your hair like that.

LUELLEN: Needs cuttin'.

MARY: No, I like it longer. Makes you look . . .It's nice. (Slight pause.) How is . . . Are you all right?

LUELLEN: I walked all the way here.

MARY: From your house?

LUELLEN: Must be ten miles, I bet. Don't you think it's about that? 'Bout ten miles?

MARY: Well . . . It's certainly longer than I'd care to walk, anyway. Especially today. Did you. . . come just co see me or . . . ? (Luellen nods but avoids looking at Mary.) Well, I'm glad to see you, Luellen, but, you know, it might have been better if you'd called me first . . . to make sure I was in, that I didn't have a client with me . . . (Luellen still doesn't look at her.) You lucked out, I guess.

MARY: (To Audience/Dictation) The worker has visited twice weekly with Jimmy since his removal from the James home and his subsequent placement in foster care on October 19. Mr. and Ms. James have remained in group therapy, and it is that group leader's judgment that both, but especially Ms. James, have made substantial progress. As a result, the court has ordered that supervised trial visits between Jimmy and his natural parents begin immediately with the goal of eventual reintegration of the James family.

MARY: Luellen, you walked a very long way on a very hot day to see me . . . Luellen? . . . (Luellen looks at her quickly and then away.) I would like to know why - what I can do to help you - but you are going to have to tell me. (No response.) Will you? (No response.) Well. I'm sorry, I wish I had more time, but I do have this appointment, so, if you'll let me get my things together, I'll take you . . .

LUELLEN: (quickly and with a new energy) No, but, see, see, I got this real good idea. It's real good, too. See, I'm fixin' to move out on Ol' Ray. He just don't know it yet, but I am. I'm goin' to get me a place to live and I'm goin' to get me a job maybe with the phone company maybe. My girlfriend works for the phone company. Or a waitress. I could do that.

MARY: Jobs are a little hard to find these days, but. . . but that sounds. . . I think you'd enjoy working . . .

LUELLEN: (big smile) I think I would, too; and my girlfriend lives in a duplex and her neighbors is goin' to move maybe and I could move in there if they did. It's got a fenced-in backyard and a big side yard and I wouldn't even let Ol' Ray even come visit only if he got over doin' them things.

MARY: (realizing) Wait a minute

LUELLEN: (going on) I know he don't mean to. He just loses his temper sometimes is all, but he's gettin' a whole lot better 'bout it since we went to that group. I sure to 'preciate you makin' us go to them meetin's. See, we had a lot of pressure on us and we was probably just takin' it out on . . .

MARY: Luellen. Wait a minute here.

LUELLEN: No, no. I still wouldn't let him' come and stay. Not no matter how much he yelled at me or how much 'he begged me, he couldn't. A daddy don't need to be with his son like a mama does. (Slightly choked, but going on.) A mama needs to be with her child. You know that, don't you? I know you do and I'm goin' to get a place for me and Jimmy to live and you can . . .

MARY: You know that's . . .

LUELLEN: (going on) And you could come visit Jimmy ever'day. You could take him out in your car and you could buy him a Coke and ask him questions. . . I'd share him with you. We could share him. (She looks pleadingly at Mary. Pause.)

MARY: Luellen, please don't do this to yourself.

LUELLEN: I ain't

MARY: You're hurting yourself with this. You're building up a fantasy that

LUELLEN: It ain't a fantasy. I thought it all out.

MARY: Thinking it out doesn't mean it can happen that way.

LUELLEN: (a protest) Yes!

MARY: No. I'm sorry.

LUELLEN: (looks at her a moment quietly) You ain't sorry.

MARY: Yes, I am. I'm sorry for how you feel right now. I know how very

LUELLEN: You know what? You know what it's like to have your kid stole by the Welfare? To sit in a room and remember that your little boy ain't bein' quiet 'cause he's sleepin' or into somethin', but that he's bein' quiet 'cause he ain't even there no more. And you don't know where he is or when he's comin' back? You don't know.

MARY: No. I guess. . . no one can. . . really. . . but you have to. . .

LUELLEN: (watching her coldly) What? I have to what? Forget about him? You ain't got no kids, do you?

MARY: No.

LUELLEN: No. You want one?

MARY: Someday. . .

LUELLEN: Like my Jimmy? (Mary doesn't answer this.) I know you like him a whole lot. You like him better than the other ones? He your favorite? You know what Ol' Ray told me once after you'd come out to visit? He said, “You better watch out, Lu girl. That woman wants your baby for herself and she's a' gonna get him, too." That's what he said, but I didn't believe him. Sometimes, though, that Ray knows what he's talkin' 'bout. You got him?

MARY: What?

LUELLEN: You got him at your house, ain't you?

MARY: No. That's

LUELLEN: You don't want me to know where you live 'cause

MARY: This is a state agency. There are rules here, Luellen. Even if I wanted to do something like-

LUELLEN: Oh, you want to. You want to and you did. (The two look at each other a long moment.)

MARY: (reasonably) No matter how much I care about Jimmy -- and I do, I care about him -- that simply isn't the reason he was taken out of your home. You know that. I did not "steal" him. He is not at my house. O.K.? Now. I want you to tell me precisely what it is you think I can do, so I can answer you in as clear a way as possible. . . so we understand each other.

LUELLEN: (trying to be "reasonable" in turn) I want to see Jimmy.

MARY: I understand that, but what do you want me to do?

LUELLEN: I want you to go get him.

MARY: I can't do that. I don't have that authority. It's out of my hands.

LUELLEN: You go get him and bring him here.

MARY: I can't

LUELLEN: Go get him.

MARY: You were in the courtroom. You heard what the judge said.

LUELLEN: Then call him.

MARY: Who?

LUELLEN: Call that judge. Right now. Tell him I can have my baby back.

MARY: I'm not going to argue with you

LUELLEN: Call him.

MARY: This interview is ended.

LUELLEN: Call him. (She moves in on Mary.)

MARY: I can't call the judge!

LUELLEN: Yes, you can! (Continuing to move in on Mary -- cold and menacing.) And you better.

MARY: (backing away, fear showing) Luellen.

LUELLEN: You better do it. (She is almost in Mary's face.)

MARY: Get out of my face.

LUELLEN: (fists clenched) I mean it!

MARY: Now . . . stop this!

LUELLEN: If you don't, I'll do something. I'll hurt you. I can. I ain't kiddin' either.

MARY: God-damn-it! God-damn-it! (Turns on Luellen who steps back) Just who the hell do you think you are? What do you think you're doing here? You can't ever-not ever in this life-see that child again. Not ever.

LUELLEN: (more of a cry) Yes, I can. .

MARY: Do you think the state or the judge would put that little boy back after what you did?

LUELLEN: I didn't. . . I never done -- Ray. Ray done it.

MARY: You! You! Face that reality at least. You. You admitted it to me, to the judge

LUELLEN: (shaking her head) Ray.

MARY: Ray may have done a lot of it, but not that last, Luellen.

LUELLEN: (childlike) Well . . . he made me.

MARY: He made you hold that child's hands on a hot stove till he had first- and second-degree burns? I'll tell you one thing, Ray couldn't have made me do that!

LUELLEN: (meekly) We was just teaching him

MARY: (going on) And, then, you ran off and left him, just left him -- and in all the months we've had him in foster care, you haven't contacted me once, not one time, to find out how he was doing. So why today? Why do you people suddenly turn up out of the blue and think -- Christ. (Takes a breath to calm herself) We explained everything to you six months ago. (Brief pause.) You could hold a gun to my head or a knife to my throat and it still wouldn't get him back for you. (Pause.)

MARY: (To Audience/Dictation) Jimmy was taken to the State Office for final adoptive placement with his new family on September 3, 1982.
```

---

## IC-0582: Four Good Days - Screenplay

- Title: Four Good Days - Screenplay
- Author (byline): Eli Saslow and Rodrigo Garcia
- Work: Not specified
- Publisher: Vertical Entertainment
- Publication date as stated: 2020
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MOLLY, MOM, NURSE, DOCTOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1627
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eli Saslow and Rodrigo Garcia
ISBN: N/A
Publisher: Vertical Entertainment
Date (Month/Year): 2020
* the full transcript of the screenplay can be found on Scraps from the Loft.com at
https://scrapsfromtheloft.com/movies/four-good-days-transcript/
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: On the verge of collapse, Molly shows up at her mother’s house seeking help.

ACTRESS 2: Ten painful years of estrangement, drug use, and addiction have taken a toll on their already fragile relationship.

ACTRESS 1: You see, Molly has been through detox more than a dozen times, yet the brutal heroin addiction shows no signs of waning.

ACTRESS 2: Research advancements may offer Molly a shred of hope--a monthly shot of an opioid antagonist that prevents toxic substances from binding to the central nervous system.

ACTRESS 1: But, there's a catch: Molly must stay clean for four excruciating days to receive the treatment.

ACTRESS 2: Can Molly go the distance this time?

TOGETHER: Four Good Days by Eli Saslow and Rodrigo Garcia
```

### Performance text (classify this)

```text
Suggested Roles: Actress 1: Molly Actress 2: Mom, Nurse, Doctor

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

MOLLY: (knocking on door, she is in rough shape) Mom, it’s me. (knocking) Mom! (trying her key in the lock) Uh, my key doesn’t work.

MOM: No, we, uh. . . We changed the locks last year after you and Eric stole the guitars. The deal was you wouldn’t come back until you were clean.

MOLLY: (gasps) Wait, wait, wait. (stuttering) That is why I’m here. I’m . . . I’m done. I wanna come home. I ended it with Eric. He’s gone. I’ve been thinking about all the things that you said to me since I was a little girl and I’ve had these, like, realizations like, these big, big realizations that I wanna go back to school and I wanna get a job and I wanna get my kids back. . .

MOM: Molly, stop. Just stop. I’ve heard this speech for 10 years.

MOLLY: (crying) Mom, I need to be home.

MOM: (resolute) No. Come back when you’re clean.

MOLLY: No, Mom, please. (knocking intensifies) It’s me! (Mom opens the door, but doesn’t allow Molly in)

MOM: Don’t make me call the police.

MOLLY: Just money for a hotel then. I need some place safe that I can get clean.

MOM: You want me to give you money? Are you crazy? Like the money you needed for shoes or for glasses? Or for, uh, oh, online cosmetology classes? How much heroin have I paid for?

MOLLY: (sudden anger; she tries a guilt trip) You’re right. I’ll just detox under a highway with prostitutes and rats, ’cause that’s a much better plan, Mom. (quick change of emotion to tears again) Can I please just have a pillow and a blanket? It gets really cold at night.

MOM: If you’re hoping for pity, there’s none coming. (beat, sighs in frustration) Oh, God damn it. If you’re serious, I’ll drive you to detox right now.

NURSE: Name?

MOLLY: Molly Wheeler Margaret

NURSE: What drugs are you using?

MOLLY: (nonchalant) Heroin, methadone and some crack.

NURSE: Have you ever been through detox?

MOLLY: (almost proudly) Fourteen times.

NURSE: Mm-hmm. Okay, so you know the drill. Medicaid pays for three nights. You get a cot, two towels, three meals a day, if you can tolerate them. Muscle spasms, cold sweats, fever, vomiting, paranoia, insomnia. All that’s normal. But if you start to have trouble breathing, speak up. Sign here.

MOLLY: (to Mom) Okay. You’ve made your point. Can I please come home now?

MOM: No. I’ll pick you up in three days. (turns to exit)

MOLLY: Really? You’re not gonna help? (crying) You’re gonna walk away?

MOM: (steps out of scene to speak to the audience – matter-of-factly) She’s in hell right now. In pain from head to toe and I kicked her to the curb. (sighs softly) Sometimes I get the feeling that. . . I don’t want to love her anymore. ***The Detox Exit interview*****

DOCTOR: I’m gonna level with you, Molly, because you don’t have time for more bull. Heroin has a 97 percent relapse rate. You’ve already blown through the veins in your arms, your ankles, hands, feet. Yeah, you stayed away from your neck so far, but most people go there sooner or later. You have put yourself in quite a situation. What are your triggers?

MOLLY: Boredom, anxiety, shame, loneliness. My life. Basically, my life’s a trigger. I’m 31 years old, and I’ve done nothing but go down in life. So I can sit around and feel all of that, or I can do something about it and feel good and numb.

DOCTOR: Let’s talk about our options. Hmm? Do you know what an opioid antagonist is? It’s a shot we give you once a month. It blocks opioids from getting into your system. Heroin, Oxy, Narcotics. The shot essentially makes you immune to getting high.

MOLLY: Is it safe?

MOM: Are you kidding me? You’ve spent 10 years shooting up heroin laced with what, rat poison and baby powder and God knows what else. And now, all of a sudden, your body’s a temple. Is it safe? Jesus, Molly.

MOLLY: It’s my call Mom . . .

DOCTOR: Yes, it’s safe. FDA approved. You have to be clean for at least a week. If you still have drugs in your system when you get this shot, it puts you into something called rapid withdrawal. That’s very dangerous. Emergency room stuff.

MOLLY: (sighs) Fine. Yeah, okay.

DOCTOR: You have been in detox four days already. You should do four more to be safe.

MOLLY: Four more days?

DOCTOR: You need to be somewhere not alone and away from other users . . . *****At Mom’s house *****

MOLLY: (to audience as Mom is doing some activity in the background) I’m always thinking about the past or worrying about the future. You know, even before I did drugs, I remember worrying about what was next. Like, I just couldn’t live with the uncertainty. I just want now to be now. (long pause-steps into scene with Mom and speaks to her) [Remember] the time you left for, like, (air quotes) a couple of weeks. It was just so sudden. You know, one day you were. . . putting notes in my lunch box, and then the next, you disappeared on your little two-year hiatus. I thought you couldn’t stand to be around us, around me.

MOM: That wasn’t it. You know that’s not true. I got pregnant with your sister. Unplanned. And in a couple of months, I found myself with a baby, and I quit my job, and I was married to a man who I really didn’t know very well, and he was. . . (sighs) He was difficult. And when your sister was eight, I got pregnant again and we were really happy about that. We were. . . I think we were at a pretty good point. Me and your dad, you know, for a moment. Then for 15 years, I held everything together. . . trying not to disappoint, swallowing your father’s temper tantrums, his moods. And then one night I came home and I heard him start to rev up one of his fits. . . and I just. . . That was it. I left that night.

MOLLY: You were the head of the PTA. You were so put together.

MOM: I was pretending. (scoffs) I just. . . I am so sorry for causing you so much pain, but I can’t apologize for trying to survive. I just can’t. That would be lying. (long beat) You think it’s my fault you’re an addict. (Molly shrugs and exits; Mom to audience) She sits around smoking, twitching, and I am there watching her like a hawk and pretending that I’m not. Pale, thin. Toothless. But, you know, pretty damn good under the circumstances. I think she might make it this time. If she can only hang on for a couple more days. Then she could get the shot, and one month clean will turn into two months and two months into six. ****AA Meeting****

MOLLY: (speaks to the audience) So, I, uh. . . I was a straight A student who never graduated high school. I live at home with my mom, but last week I was sleeping on the streets. Don’t have a job. Or any job skills or a dollar to my name. See that, um, that lady in the back. It’s my mom. She drove me here today because I, uh. . . my license was suspended because of so many DUIs. But even if I did have my license, she wouldn’t trust me with her car. Because I have. . . I have robbed her blind. Money, jewelry, credit cards. And I have. . . degraded myself for drugs, in ways. . .in ways that you don’t want to know. (she hears a comment from the audience and responds) Excuse me? Do you know how many times I have told myself that? That I’m not going to let myself steal to get high? That I’m not gonna let myself lose custody of my children to get high? That I’m not gonna let myself stab a needle into my arm? I’m so sorry, Mom.

MOM: (after the meeting) I haven’t seen you like that for so long. Confident, honest. Taking full responsibility. Just. . . I don’t know. Just being yourself. You should have seen the way they were looking at you. Just riveted. If there’s anyone who has the strength to break free of this, it’s you. I really believe that. (long beat) You know, I’ve been wanting to ask you something, but I do not want you to take it in the wrong way. I just. . . No judgement. Did you ever. . . prostitute yourself?

MOLLY: I never had sex for money, but I have had sex for drugs.

MOM: Well, that’s not prostitution. No, That’s, uh, a sick person trying to survive.

MOLLY: (picking a fight) Yeah, but if I had had sex for money to buy drugs, would that make me a prostitute? So, what’s the verdict, Mom? Whore? Not whore? (Molly’s phone vibrates and she answers; her words ring false) Yeah, this is Molly. We already scheduled the shot for 9:00 am Friday. No! No, I can’t wait. Are you serious? Yeah, we’ll see you on Monday.

MOM: Okay. So what was that?

MOLLY: Three more days. They’re waiting for my insurance papers to go through.

MOM: Three days is an eternity.

MOLLY: Jesus. You’re not helping. (growling in frustration)

MOM: (suspicious) Why didn’t I hear your phone ring?

MOLLY: What?

MOM: (growing anger as she realizes Molly is lying) Your phone? Why didn’t I hear it ring? And why is the office still open. It’s after 6 o’clock. I want to see your phone. Give me your phone.

MOLLY: Are you crazy?

MOM: How many fake phone calls have you made? Lies from the very beginning.

MOLLY: Are you doing this to me right now? Oh, my God. You’re such a trigger!

MOM: (angrily) It just goes on and on.

MOLLY: I am so sorry that my drug addiction is so incredibly difficult on you. Look, I, I am not going to make it to Monday if I stay here. I’m gonna go to Sean’s, I’m gonna go stay with Sean. He. . . he said that he can pick me up.

MOM: The same Sean who wanted you to score for him? Do you hear yourself? I mean, do you hear yourself? Do you? (washes her hands of the situation) All right. Do what you’re gonna do. (Molly exits, Mom talks aloud to herself, contemplating) How did I get here? What did I do? You know, maybe it’s just the way her brain is wired. You know? Maybe she’d taken the pills the year before, or a year after, she wouldn’t have gotten hooked. Or if you’d stayed in your bad marriage, she would have been an even bigger addict. Or if you bought her those blue shoes that time when she was three, instead of the red. It’s none of that . . . Because maybe, the moment her father’s sperm reached your egg, she was already an addict, waiting to happen.
```

---

## IC-0583: Frozen

- Title: Frozen
- Author (byline): Bryony Lavery
- Work: Not specified
- Publisher: Faber and Faber, Inc.
- Publication date as stated: April 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NANCY, AGNETHA, RALPH
- Teaser before the introduction: Yes
- Spoken words (computed): 1705
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bryony Lavery
ISBN: 978-0571217380
Publisher: Faber and Faber, Inc.
Date (Month/Year): April 2003
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 2: Frozen by Bryony Lavery is much more than a story of child abduction and murder.

ACTRESS 1: It is a story of the struggle to understand and to forgive when the very act of forgiveness seems absurd.

ACTRESS 2: Malcolm Gladwell once wrote: “The difference between a crime of evil and a crime of illness is the difference between a sin and a symptom . . .”*

ACTRESS 1: An illness can be forgiven . . . .but can someone who is inherently evil?

ACTRESS 2: And how do you determine the difference?

ACTRESS 1: In this selection Nancy, the mother of a murdered child and Agnetha, a psychologist, work through the struggle 20 years after Rhona disappears.

TOGETHER: Frozen by Byrony Lavery
```

### Performance text (classify this)

```text
Suggested Roles: Actress 1: Nancy, Ralph (in scenes with Agnetha)

Actress 2: Agnetha, Ralph (in scenes with Nancy)

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NANCY: (Pg 22-23) (in a school hall, to audience) On April 17th, 1980, my daughter, Rhona walked out of my house to go to her Grandma’s house. She never got there. She never came back. She was ten. She’s been missing for five years. She will be fifteen years old tonight. I know she’s alive, I have Faith. Every night I pray that whatever reason is stopping her coming home will be removed and that she’ll phone or write or just knock on the door and say “Mum, it’s me.”

NANCY: (Pg 28-29) Four days ago, two young policeman say . . . “We have apprehended a man in the unsuccessful attempted abduction of a young girl . . . subsequent inquiries have uncovered a lock-up shed. The earth floor contains the remains of other children. The man is now giving us names. One of them, he says, is Rhona.” All this time I’ve been growing her up she’s been -- He’s had her buried away . . .

******* A large, academic hall *****

AGNETHA: (Pg 34-35) (in “lecture mode – to audience) "Serial Killing ... A Forgivable Act?" It is a critical examination of the differences between crimes of evil and crimes of illness. I base my critique upon a psychiatric and neurological study of the criminal brain. My name is Dr. Agnetha Gottmundsdottir. I am a psychiatric explorer. My chosen expedition -- the Arctic frozen sea that is . . . the criminal brain. (Ralph's head lit as if it is an exhibit) Let us take a look. (walks over to stand behind Ralph, gesturing around his head, but not touching)

The cortex is the thick covering of grey matter on the upper part of every human brain and the function of the cortex, in particular, the frontal lobes, is to modulate the impulses that surge up from within the brain. To provide judgement, to learn and stick to rules of everyday life. They are responsible for making us human.

Ralph Ian Wantage is currently in Long Larron Maximum Security Prison serving a life sentence for the abduction, sexual assault and murder of 7 young girls over a period of 21 years. ****** Agnetha and Ralph, prison cell*****

AGNETHA: (Pg 37) I’m not gonna harm you. I’m gonna tap you on the nose . . . (She the bridge of his nose.

RALPH: (blinks rapidly, distressed) Hey, hey, hey, hey . . .

AGNETHA: (moves away, showing us on her own nose) When you tap someone on the bridge of the nose, it's reasonable for the person to blink a coupla times because there is a threat from outside. When it's clear there is no threat, a person should be able to accommodate that. But if the subject blinks more than three times, that's what we call "insufficiency of suppression" which may show frontal lobe disfunction. You can't adapt to a new situation. There's a certain rigidity there. Like the person is ice-bound ******* Nancy’s house******

NANCY: (Pg 38) You can go and be there when they die . . . murderers. They show you the electric chair, how it all works. And then, you can be present, members of the victims’ families at that final moment. (Pg 37) I’d like to see him die. Watch him suffer. He wouldn’t suffer like she suffered. But it would be something. An eye for an eye. ******* A large, academic hall *****

AGNETHA: (Pg 46) (in “lecture” mode – to audience) Over the years Dr. Nabkus and myself have studied more than 250 dangerous criminals. In significant numbers, these men have incurred physical damage to the brain. After Dr. Nabkus has finished his medical history, I look for evidence of child abuse (Pg 50) [It] causes profound and pathological changes in the structure of the brain as surely as does physical injury. We brain scanned the children of severe neglect [and] found that entire structures of their cortex never properly developed. (Pg 51-52) What you get is a kind of erraticness -- they can be very different in one situation compared to another. There is a sense that they don't have a larger moral compass. ***** Ralph and Agnetha, prison cell*****

AGNETHA: (Pg 62) No remorse then, Ralphie?

RALPH: Remorse. So what is that . . . remorse?

AGNETHA: Like Regret. But more. You repent your sin. You feel sorrow, pity, compassion. A sort of . . . tender feeling.

RALPH: I can’t say I do. (pause, thinks) The only thing I’m sorry about is that it’s not legal

AGNETHA: What’s not legal?

RALPH: Killing girls. ****** Nancy meets with Agnetha *****

NANCY: (Pg 59-61) I’m “in a very bad space.” I know that. I know I’m ready.

AGNETHA: How?

NANCY: He . . . (she has to do this) forced her into the van. And, and, and he. . . wrapped her in polythene sheeting. She was unconscious but she wasn’t dead then. He took her to a shed and we think he sexually assaulted her before he held the polythene on her face and suffocated her. (short of breath)

AGNETHA: Breathe. (both inhale and exhale; Nancy following Agnetha)

NANCY: I’m accepting she’s dead. But (pause. somehow an awful admission of guilt) I’m not! And I need to (hand gesture of moving forward) So he’s the next step. I want to know why. I want to know why her. She’s 10! I want him to know what he’s done. I want him to know how I feel. I want to understand. If I could understand why . . . I might be able to (hand gesture of moving forward) They said you could help. It’s time -- I want a visit. ******* The following are separate monologues from Agnetha and Nancy interspersed – they are not talking to one another.

AGNETHA: (Pg 67) (calm, clinical) Most forensic psychiatrists tend to buy into the notion of evil. I don’t. I can’t. I find no evidence that people are born evil. To be evil is to be “morally depraved.” That bespeaks having conscious control over something. The serial murders I have tested are not in that category. Their deeds themselves are bizarre, grotesque, life-destroying -- but not evil. They are driven by forces beyond their control.

NANCY: (Pg 65) (angry) I’d swing that bloody American doctor woman round by her. . . (quotes) “The experiment is unviable! The components unstable!" Who does she think she is? I've written some letters made some phone calls. I'll get that visit!

AGNETHA: (Pg 67) (calm, clinical) The difference between a crime of evil and a crime of illness is the difference between a sin and a symptom.

NANCY: (Pg 55-56) (incensed) If I go to see him, I’m taking a gun. Blow his brains all over the wall. I’m taking a knife; slice his thing off. Stick the blade through his eye and take out his brains! What he thought to do -- what he did . . . She was my little girl! And she said (pause) forgive that monster. I can’t do that. How can I do that? It’s too much. (long pause as she battles with her emotions)

AGNETHA: (Pg 67-68) (somewhat judgy) I guess as a moral society -- as a punishment society . . . We can’t let the notion of these deeds being “symptoms” intrude in the relationship between murderers and the rest of us.

NANCY: (Pg 39) (deep breath) I can forgive. But I can’t forget. *****Prison visiting room -- Nancy enters*****

NANCY: (Pg 68-73) (to guard) That’s him? (goes to stand in front of Ralph) Ralph Wantage? (he looks up; barely nods) Nancy Shirley. You got my letter. You agreed to see me.

RALPH: She was your kid . . . one of them.

NANCY: Rhona RALPH: Rhona. (pause)

NANCY: I want you to know I forgive you for killing my daughter. (silence -- Ralph abruptly covers his eyes with both hands) I don’t hate you. I used to, but I don’t anymore. (silence, Ralph has nothing to say) I’ve brought some photographs, would you like to see them?

RALPH: Of . . . her?

NANCY: Rhona (she gets them out. A small dog-eared selection, hands them to him in turn) As a baby. (next) That’s me holding her. Her cat is Fluff. (next) This is Rhona dressed as an octopus for a fancy-dress competition.

RALPH: Did she win?

NANCY: She came third behind Little Miss Muffet and a Loch Ness Monster.

RALPH: She should have won. (beat) I don’t think I hurt her . . .

NANCY: You did.

RALPH: I don’t think she was frightened at all . . .

NANCY: She must have been. She must have been frightened! (Ralph thinks . . . Nancy watches him carefully. When he looks up suddenly, she holds his gaze. He looks away . . . she touches his arm) Your dad? What did he do?

RALPH: My dad, well, he was the disciplinarian obviously.

NANCY: Made you behave, did he?

RALPH: Oh, yes! Say you swore filthy language . . . He’s got you by the hair here (back of neck) And you’re in the washing up water. Wash your mouth out with soap water! Or you done wrong . . . anything . . . he’s (in Dad’s voice) “See it in my eyes? Can you see it, you little pillock? I’m looking into you and I’m seeing shit! You keep yourself clean! You hear me?

(sound of a thump on flesh . . . Ralph registers it, side of head) You deaf little bugger! (another thump, same side of head) You listening to me? (tap on forehead) You sand still and don’t move one muscle! Not one! You don’t even blink until you know I mean what I say. See it in my eyes?” (blinking rapidly)

NANCY: Frightening bugger. (Ralph nods) Hurt you a lot. (beat, then another nod) Can you see it hurt Rhona then? Can you see it frightened her? What you did.

RALPH: (Ralph thinks impassive for a long time, then) Yes. (nods, tears in his eyes . . . he wipes them fiercely. Violently. Dry painful sobs start. Nancy watches. He holds his chest in pain as the sobs subside. Calmly Nancy takes out a tissue and hands it to him) (harshly) Don’t come and bother me again. (Nancy exits) ***** Agnetha and Ralph – Prison cell*******

AGNETHA: (Pg 76-78) Well, Ralph. This is my last visit. I wondered if you wanted to tell me anything more. And I came to say “Goodbye.”

RALPH: (cautiously) I’ve been wanting to tell you things. I think I caught cancer or something. (motions to his chest) Here. That’s lungs right? Lung cancer.

AGNETHA: What does the doctor say?

RALPH: Says it’s just stress! Stress is in here (motions to his forehead) I know where stress is! This gnawing, here! (motions to his chest) Not stress!

AGNETHA: That’s your heart, Ralph. How long have you been in pain?

RALPH: It started . . . night after that mother of that girl Rhona I done came . . . That was Thursday . . . so (Counts on his fingers) It’s been a bit.

AGNETHA: Mrs. Shirley came to see you? I recommended she . . .

RALPH: Well, you were overruled by the Doctor-in-Charge!

AGNETHA: And she visited with you?

RALPH: She’s forgive me, actually. (spasm in his chest)

AGNETHA: (thoughtfully) What you are feeling may be psychological. What you are feeling may be remorse and that will be very painful for you, Ralph.

RALPH: (hardens again, he speaks to himself) It’s a question of finding a window of opportunity ***** Ralph, alone in his cell******

RALPH: (Pg 79) (Ralph, in his cell, sweating. Fashioning a noose with his belt and a long cloth. He slings it over the pull up bar and stands on his chair) Gnawed to death? I don’t think so.

(completes his preparations. Kicks the chair away from him. He hangs, choking, jerking) ***** Graveside – Ralph’s funeral******

(Nancy stands at the gravesite. Athena, entering, watches her for a few seconds)

AGNETHA: (Pg 79-82) Not a big funeral . . .

NANCY: (sarcastically) Bit of a surprise . . . person with his talent for putting sunshine in everybody’s life.

AGNETHA: You went to see him.

NANCY: And you tried to stop me.

AGNETHA: I was trying to protect everybody

NANCY: Him. AGNETHA: Everybody

NANCY: Him. How much time and energy did you give him? And me? (beat) You look upset. Were you fond of (beat) Ralph?

AGNETHA: It’s not for Ralph . . . It’s for somebody else. For me.

NANCY: Me as well. I couldn’t feel much for him really . . .

AGNETHA: No. It was . . . not easy. (Both nod thoughtfully)

NANCY: Do you think he did it . . . the . . . suicide . . . because I went to see him?

AGNETHA: (long silence) Yes. (long silence, then in a rare show of emotion) My colleague and best friend, David, died three months ago. Stupid accident – wearing a seat belt, observing the speed limit. A truck goes out of control – smashes the care. The truck driver is unhurt. David – I worked with him every day for 10 years. Two days before he died I slept with him. It just happened. His wife is a very good friend. Why am I telling you this?

NANCY: Why are you?

AGNETHA: Do I tell her?

NANCY: No. You just suffer. “The difference between a crime of evil and a crime of illness is the difference between a sin and a symptom . . .” Your words. I read your thesis. You knew what you were doing. Live with it.
```

---

## IC-0584: Gidion’s Knot

- Title: Gidion’s Knot
- Author (byline): Johnna Adams
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: March 2014
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CORRYN, HEATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 2103
- Already set (do not supply): none

### Source block (context only)

```text
Author: Johnna Adams
ISBN: 978-0822229674
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): March 2014
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Gidion’s Knot . . . a reference to a legendary chapter in the life of Alexander the Great in which he is tasked with unraveling several knots so tightly entangled that it is impossible to see how they are fastened.

ACTRESS 2: Since then, the phrase “Gordian Knot” has been used to describe a complex or unsolvable problem.

ACTRESS 1: Gidion's Knot by Johnna Adams turns out to be as difficult to unravel as the Gordian one for which it's named.

ACTRESS 2: You see, this is a play about the death of a child.

ACTRESS 1: It is also a play about the right to freedom of expression and whether it is limited by society’s needs.

ACTRESS 2: And it is a play about the support a mother must and will give her child.

ACTRESS 1: Ultimately it is the story of a confrontation between a mother and a teacher.

TOGETHER: Gidion’s Knot by Johnna Adams.
```

### Performance text (classify this)

```text
Setting: A 5th grade classroom in a public school in the Lake Forest suburb of Chicago.

CORRYN: I missed open house. So we never got to meet.

HEATHER: You’re Gidion’s mother.

CORRYN: You can call me Corryn. You sent a note home with my son. Asking to meet with me. . . . Telling me he was suspended.

HEATHER: I’m so sorry. I’m so sorry. I’m so very, very sorry.

CORRYN: The reason you suspended him? I’d really like to know. I’ve been wondering. Your note was vague. The voicemail was cryptic. I’ve been up for about 72 hours. I can’t sleep. I can’t sleep because I’ve been playing this conversation out over and over again in my mind, wondering how it will go. You were more vocal in these little fantasies. You contributed. You explained . . . I don’t know why you . . . did this to him. I don’t know what happened.

HEATHER: . . .

CORRYN: He looked devastated. When he handed me the note. He was shaking. He—

HEATHER: God! . . . oh god . . . I didn’t think you’d keep the appointment. It never occurred to me that you would keep the appointment.

CORRYN: He’s my son.

HEATHER: I didn’t think you’d still want to talk about—

CORRYN: About my son?

HEATHER: That it might be painful to. . . To talk about him so soon after his death. I’m really very sorry—

CORRYN: You’ve said so.

HEATHER: . . .

CORRYN: Thank you. . . . I’m sorry I missed open house. Gidion’s father is dead. I’m a single mother. Getting a babysitter on a school night is like squeezing milk from stones. Do you have children?

HEATHER: No.

CORRYN: How long have you been teaching?

HEATHER: Two years. Maybe we should reschedule. Find a time when the principal can join us. You should be with family now.

CORRYN: I’m exactly where I should be. You sent a note home with my son. You suspended him. Five days.

HEATHER: Yes. You should take some time to grieve before . . . this. We all should take some time—

CORRYN: Who’s Jake?

HEATHER: He’s a boy in the sixth grade.

CORRYN: Is he one of the children that Gidion made angry? On Friday? The day he died? . . . There’s a Jake on facebook who left comments on Gidion’s facebook page over the weekend saying “You’re a faggot” and “You’re a lying faggot.” After Gidion was dead, in fact, so-- . . . untimely.

HEATHER: He couldn’t have known Gidion was dead. The kids didn’t know until this morning. Jake’s been troubled lately. It’s out of character if he did that. . . Can I get you something to drink? The faculty lounge is just down the hall.

CORRYN: No thank you. I’m fine . . . Do you want to know what I do? You won’t see this coming . . .

I’m a teacher.

HEATHER: What do you teach?

CORRYN: Literature. At Northwestern. In the graduate program. . . Jesus Christ. What the hell happened? I thought this would be largely a transactional exchange. I ask, you give. Even-- well, correct me if I’m wrong-- you have two years of professional experience, but, even if the circumstances around my son’s suspension weren’t . . . charged, let’s say, by the fact of his death, I would expect the reasons for his suspension to have at least come up

HEATHER: . . . . (Heather pulls out a key ring. She finds a key and unlocks a drawer. She takes out a folder covered in comic book superheroes and sets it on her desk.)

CORRYN: What is it?

HEATHER: What got Gidion suspended. She offers the folder to Corryn. Corryn doesn’t take it.

HEATHER: It’s something Gidion wrote . . . A story.

CORRYN: You have got to be kidding me. You suspended my son over a story?

HEATHER: It’s disturbing.

CORRYN: I have a feeling there are miles between what you and I find disturbing.

HEATHER: Read it and we’ll see. (Heather starts to leave.)

CORRYN: Don’t. . . I want you to explain things to me. I don’t want to sit alone here. I didn’t come here for that. I don’t want to figure things out. I want them explained! I want you to read it to me.

HEATHER: It’s not the way you want your son remembered.

CORRYN: You don’t know what I want.

HEATHER: Trust me.

CORRYN: Read it.

HEATHER: I’m sorry. I honestly can’t read that again. And certainly not out loud.

CORRYN: As bad as all that?

HEATHER: Yes.

CORRYN: As bad as facing what you did?

HEATHER: That’s not fair. . . That is not fair. I know you’re angry with me. I can’t imagine how angry you must be with me. And you want to punish me. . . I don’t know what went on in your house. . . Once he left this classroom my responsibility ended. This-- this is not a product of my classroom. He learned this (gesturing to the folder) in your house.

CORRYN: I can’t read it. I need you to do this. . . Because it’s in his handwriting . . . And I can’t read his handwriting without seeing his suicide note in my hands. Please? (Corryn holds the folder out to Heather. Heather takes it and opens it.)

HEATHER: It began during a war, as things do. We all formed tribes and began killing the teachers. I cut Mr. Shawn apart myself with a hunting knife my grandfather gave me the last time he took me hunting. We needed his entrails for our weavers and our poets. I think Mr. Shawn was grateful. A group of sixth graders had caught him in the cafeteria earlier, by the vending machines, and cut out his eyes, flayed him. He was spitting blood up because of something they’d broken in him and I think he loved me for cutting him open. I took a broomstick out of the janitor’s closet and nailed one end of his intestines to it and then rolled the rest of his intestines out of his stomach, twisting them around the broomstick-- they stretched more than 25 feet when I was done. Mr. Shawn had told me that intestines were that long in science class a month ago, but I didn’t believe him until we started collecting them for the weavers and the poets. He was lucky. Most kids wouldn’t have killed him first. I put the thick roll of Mr. Shawn’s intestines over my shoulder and started walking to the gym, which is the room where we kept the weavers.

Around the corner in the hall outside the nurse’s office, the nurse, Carole from the office and the fat principal were hanging from the walls by nails punched through their wrists and ankles and knees and shoulders. Their bodies were just gaping, empty bags. No entrails to salvage.

The broomstick was heavy and I had enough guts, so I made my way to the gym, where the weavers worked. Since the weavers started working, the gym stopped smelling like a gym and started smelling like a butchers’ shop and a toilet. All those entrails being braided and woven. You wondered how the weavers could stand it, but when they changed into weavers, maybe they lost their sense of smell. We had been in home period, in Ms. Clark’s room when the first weaver was chosen. We don’t know by who, some think there are aliens on earth like the body snatchers and some think God did it. But whoever did it, in the middle of class this girl suddenly screamed and her eyes turned into balls of blue glass and her arms stretched out like poles and her hands grew new fingers and grew big. This was happening in other classes, but we didn’t know that. And she started asking for entrails. Not to eat, but to make things with. So we put her and the others in the gym and they started making looms out of the janitor’s supplies. And we started killing for them. We had to give the weavers what they needed. Some of us sort of hung back to see what the weavers were making from the teachers’ entrails before we started killing and gutting. But when the first cloak was made and the first poet climbed the hill, I knew I had to kill however many teachers I needed to so that I could have one.

I gave a weaver my last pile of entrails and she tied them onto the ends of the other entrails I had brought her and started weaving. The cloth the weavers make from the teachers’ entrails is like nothing you’ve ever seen. It’s like a river and a taste of salt. It’s like an ocean with fish moving through black water. When the weaver finished my gut-cloak she put it around my shoulders and I felt the pull. And I walked out of the building to the soccer field where the tribes who kept the first through third grade kids as slaves had made them build a mountain. And I climbed the mountain and joined the poets there. We watch the war and we write about the great deeds done or the horrors done. And that is how God remembers you-- the way we write you. And no other way. (Heather shuts the folder and puts it in front of Corryn on a desk.)

He was passing it around. To the other students. It’s my responsibility to-- . . . I’m sure you understand. I can’t imagine what it-- . . . . I don’t think, at heart, that he-- . . . . Well. . . . I know this isn’t all there was to him.

CORRYN: This is magnificent! This is wonderful writing. Strong. Fearless. Fierce. Brave. Cruel. Remarkable. This is a wonderful story. About art and its purpose. About man and divine judgement. Oh god. God, it’s beautiful.

HEATHER: I disagree.

CORRYN: Why?

HEATHER: I have a responsibility to my students. To protect them.

CORRYN: From what?

HEATHER: From things like this. Damaging things.

CORRYN: Poetry?

HEATHER: Hate-filled, poisonous attacks. He passed this around to a room full of children . . .

CORRYN: Oh, God. I put him here. Into a pit. Full of the unenlightened. Into the hands of the conventional. Who the hell are you to tell my son what not to write about?

HEATHER: His teacher.

CORRYN: What were you teaching him? How to disappear into some mold you wanted to pour him into?

HEATHER: This decision wasn’t about him. It was about the other children. Their well-being. This is a fifth-grade classroom.

CORRYN: This is a small box. Full of smaller boxes. One of which you tried to keep my son in. And when he couldn’t fit inside it, he shot himself in the head. Over not fitting in a box cut to your dimensions. I blame you for this. He wanted to be a writer. He was going to be one.

He didn’t die because of what he wrote, or because you suspended him. He died because he couldn’t face telling me about it-- . . . god damn it . . . He could have told me this. God. I’m not a good mother. . . There are so many things that could go wrong-- so many ways I could ruin things-- but this? This? This was my good mother moment. What happened? He could have told me this. I would have told him: “This is magnificent. You are a poet. You’re perfect. They’re wrong.” My good mother moment. The one time-- the one time I would have been the mother he needed and not just the one he got.

HEATHER: . . .

CORRYN: I don’t know what I did to make him think he couldn’t tell me. . . This. (Motioning to the folder) It’s based on a story I used to tell him when he was little. About the Great Poet's war. Once upon a time in the green hills of ancient Gaul, two warring clans met on the battlefield of Ballycrief. Each clan had a master poet and a poet's apprentice. And they sent their poets to the top of the hill. So they could see" Because men aren't afraid of dying, but they are afraid of not being remembered.

HEATHER: . . .

CORRYN: Sign this. (taking the suspension notice out of her purse) You sent this home with him. I’m supposed to meet with you and get it signed. Unless it is no longer important . . . I was grading papers when he gave it to me. I knew it was something big. He couldn’t look at me. He was shaking. I saw what it was and told him everything would be all right. Asked him if he wanted to talk about it. He shook his head no. He went up to his room. I didn’t hear him go into the garage. I called him to come down for dinner. He didn’t answer so I started up the stairs to go get him and I heard the gun shot. I thought he was upstairs still and I couldn’t imagine-- I called out again and told him to stay in his room and then I went into the garage. He had taken garbage bags-- the ones for gathering dead leaves, and taped them in a large rectangle on the floor. Like a tarp. But, he didn’t understand. Because he put the gun under his chin. So, nothing. . . nothing landed on the tarp. So. He didn’t leave behind the tidy mess he thought he would.

HEATHER: . . .

CORRYN: He left a note. (takes another slip of paper from her purse)

HEATHER: . . .

CORRYN: “I’ve gone to stand with the poets.”

HEATHER: . . . That’s beautiful.

CORRYN: When someone tells you what her child’s suicide note says, you aren’t supposed to say “that’s beautiful.” It really isn’t appropriate. But you said it. Because you felt it . . . Thank you.
```

---

## IC-0585: Goblin

- Title: Goblin
- Author (byline): Rachel Harrison
- Work: Bad Dolls, Pgs 64-81 *
- Publisher: Titan Books
- Publication date as stated: Sept 2023
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MEG, DANI, ACTRESS 1, ACTRESS 2, TOGETHER, AD VOICE, DANI’S GOBLIN, MEG’S GOBLIN, BOTH GOBLINS, PHONE AUDIO, GOBLIN
- Teaser before the introduction: Yes
- Spoken words (computed): 1482
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rachel Harrison
Book: Bad Dolls, Pgs 64-81 *
ISBN: 978-1803363936
Publisher: Titan Books
Date (Month/Year): Sept 2023
```

### Introduction (context only: never use it for content warnings)

```text
(As if on a weight-loss advertisement)
```

### Performance text (classify this)

```text
Suggested Roles: Actress 1: Meg Actress 2: All other Roles:

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

MEG: (Pg 64-81) It was Dani's idea to download the Goblin. We were in the dressing room at H&M and she kept sending me out for different sizes.

DANI: None of my clothes fit. I found this incredible dress to wear to Michelle and Ben's wedding, but I don't feel good in it.

MEG: I passed her multiple pairs of the same jeans through the curtain as the attendant disapproved from behind a rack of unwanted clothes.

DANI: I need to lose five pounds. Will you do it with me? I heard it's super easy. You just download the app and you get a Goblin.

MEG: Is it tech or magic? (to audience) Some people are good at saying no. Toddlers are good at saying no. I am not good at saying no.

ACTRESS 1: Are you tired of weight loss apps that promise results but leave you frustrated?

ACTRESS 2: YES! Does losing weight feel like running a marathon on a treadmill set too fast?

ACTRESS 1: YES! Well, look no further, glutinous humans!

ACTRESS 2: Download your personalized GOBLIN weight loss assistant today!

ACTRESS 1: Guaranteed to keep you away from food just when you need it the most!

ACTRESS 2: With GOBLIN say Goodbye Chubby, Hello Hubby!

ACTRESS 1: Gotta Get a Goblin, today!

TOGETHER: Goblin by Rachel Harrison

MEG: Later that night I thought about calling Dani and politely backing out of the diet. The only problem was my plucky past self had stuffed the RSVP in the mail with the arrogance of a white-collar criminal. Four months ago, this was the perfect opportunity to prove to myself that I was finally over Ben. I wasn't feeling so confident now. But it was too late. I'd committed. Chosen salmon over chicken. What would they think if I didn't show? Dani came over to download the app. In ads, the Goblin looked cute and animated. Smurf-esque.

AD VOICE: Gotta get a Goblin!

MEG: It's four ninety-nine? DANI: Meg.

MEG: Okay, okay. (presses phone keys to download; then to audience) Two tiny green Goblins appeared, each about six inches tall. Dani's was wearing a nightcap and glittery shoes with little bells.

DANI’S GOBLIN: (twirling, shaking its hips side to side and giving Dani a thumbs-up)

DANI: (giggling) Cute! MEG: (to Dani) Mine looks angry.

MEG’S GOBLIN: (arms crossed over his chest, he hisses and shows his fangs)

MEG: [He] was stocky; his head was shiny and bald except for three thick, curly black hairs spiraling up like springs. And he had fangs!

DANI: He's just serious. Means business. (to the Goblins) Hello, little ones.

BOTH GOBLINS: (Meg’s Goblin is bored, taps his foot – then POOF – the Goblins disappear, Dani’s Goblin waiving a joyful goodbye)

DANI: They'll come back when we need them. When we're about to make a bad choice -- like ordering Chinese. ***** later that night*****

MEG’S GOBLIN: (off stage) Crash. Bang. Slam.

MEG: (wakes from her sleep, frightened – she picks up her phone from the nightstand)

PHONE AUDIO: Hi, Gorgeous! Your Goblin is visiting, doing some Goblin good!

MEG: (creeps out of her bedroom -- to audience) The light was on in the kitchen. I paused in the doorway, and there it was, ripping through my cabinets. It poured out a box of Cheez-lts and started stomping, crushing them into orange dust. (to Goblin) Hey!

GOBLIN: (stomps a few more times, then wipes its hand, narrows its eyes, hops over to the fridge and pulls the door open, begins to throw food into the garbage)

MEG: I watched as the Goblin tossed a chocolate bar into the garbage, along with a bag of frozen chicken fingers, a half-empty jar of Alfredo sauce, ranch dip, and a carton of chocolate milk.

GOBLIN: (dusting off his hands, makes a rude gesture and noise to Meg, then vanishes - POOF) ***** later that week*****

MEG: (to audience) [Hunger] spawned in my gut around 8:30 every morning that first week. My lunch was three plain rice cakes and nonfat peach yogurt. I didn't want the Goblin to come back. [But] on Sunday I went to McDonald's. Fast and dirty. I stood in line salivating at the smell of salt and crackling hot oil. (wipes the corners of her mouth) I ordered a ten-piece chicken nugget and ate them on the walk home. I was on my 3rd when the Goblin appeared.

GOBLIN: Hey! (slaps the nugget out of her hand his voice is gruff and ugly as he begins throwing the nuggets onto the ground one by one)

MEG: (shoves the last two into her mouth) Jerk!

GOBLIN: (hands on his hips glaring) B****! (muttering to himself then disappears - POOF)

MEG: (takes out phone while continuing to walk home) I called Dani.

DANI: (out of breath) I'm on the elliptical. What's up?

MEG: My Goblin called me a b****!

DANI: (laughing) Mine doesn't say anything. Maybe you get the Goblin that suits you. You respond better to tough love.

MEG: No, I don't. (hangs up, then to audience) I moped home and found my workout clothes laid out for me on my bed. The dress for the wedding was hanging on my closet door, slinky and beautiful and small. I saw the Goblin out of the corner of my eye, a smear of green. ***** a few weeks later*****

MEG: (to audience) The group text could not be escaped. An invitation to dinner and drinks. I wasn't going. Going would mean a guaranteed appearance of the Goblin, and at least 2,000 calories. I made soup instead. Kale and chickpea soup. I was hungry again in twenty minutes. I decided to make toast. Whole wheat. I left it in the toaster too long and it was dry. Jam, I thought. A little sugar-free raspberry jam. But I didn't have any jam. I did have organic coconut spread. It was terrible. I dipped the knife back into the container.

MEG’S GOBLIN: (appears and knocks the knife out her hand) Cow! (disappears - POOF)

MEG: The toast went into the garbage. I searched the internet for the best juice cleanse. A 6-day cleanse delivered to my door. $375.00. If I missed chewing, I could have some celery. ***** a confession to the audience*****

MEG’S GOBLIN: (stalks around threateningly behind Meg during her confession, he becomes giddy when hearing of her previous eating disorder and his stalking turns into a victory dance)

MEG: (to audience) For me, hunger was nostalgia -- like visiting an old friend I'd forgotten how much I hated. I had overcome hunger before. I knew I could starve. When I was sixteen a few girls went to the guidance counselor, who told my parents, all of my teachers and my soccer coach. It bothered me that everyone knew. It made me feel raw, unsafe.

I didn't understand how it was a surprise. I did damage. I deprived myself. I was a bone. Part of me was hurt that they hadn't said anything sooner, that they hadn't shown any concern. I had to pinch my nose to get the vitamin shakes they gave me down. I imagined what they'd look like coming up. Probably the same. ***** the day of the wedding*****

MEG: (to audience) The day of the wedding, Dani and I sat eating mushy grapes out of a plastic bag. I skinned each grape with my teeth and sucked on it to make it last as long as possible.

DANI: Is this going to be weird for you?

MEG: (laughing) No. Ben and I were together for, like, five minutes. [He] was always in love with Michelle. It's not like I didn't know. I'm glad they ended up together.

DANI: (snorts) You're either a great liar or a much better person than I am.

MEG: (to audience) There were violins. Michelle in her mermaid gown, cathedral veil, [with] a collection of pretty bridesmaids. There were vows.

DANI: (to audience) He promised to love her always, to put her first, and never to ask her why she needs so many shoes. There were drinks and bacon-wrapped shrimp and mini quiches. There were candles and a taco bar and a pizza station.

MEG: (to audience) There was more, but I was too busy willing my stomach to stop howling to pay attention. Salad arrived on art deco china. I unfolded my napkin and reached for my silverware. My hands were shaking. I was woozy. The only solid food I'd eaten in days was the grapes earlier that morning.

MEG’S GOBLIN: (whispering in her ear) Are you sad? Are you angry? Are you heartbroken?

MEG: (brushes the Goblin away; to audience) The truth was all I felt was hunger. I skewered a tomato. It was only a tomato. Harmless. (relishes in chewing) I had forgotten the simple pleasure of flavor. [Then] I ate the entire entree when it arrived. A slab of salmon pink, mashed potatoes, soft stalks of asparagus. A golden pool of butter gathered on one side of the plate. I sopped it up with a dinner roll. (blissfully stuffs the roll into her mouth)

DANI: (offering her roll) You want mine? I'm deleting my Goblin. I'm just not gonna eat bread.

MEG’S GOBLIN: (POOFs in and locks its fangs around Meg’s ankle)

MEG: As soon as I heard "Goblin," the pain registered. I looked down and saw it there, fangs dripping blood. The shame came swiftly. A searing, all-consuming embarrassment. (to Dani) I have to go. (exits quickly to the bathroom and stares at herself in the mirror, horrified) My skin was sallow, my hair damp. My carefully applied eyeliner was smudged and uneven.

MEG’S GOBLIN: (takes another bite of her ankle)

MEG: (looks down as she speaks to audience) I couldn't feel anything, but I could hear it gnawing. I could see the small puncture wounds, the thin streams of blood. (kicking her leg to dislodge the Goblin) Stop! Please! (to audience, holding her stomach) All that food. I ate so much!

GOBLIN: (opens the door to the bathroom stall and lifts the toilet seat lid) Do it . . .

MEG: (sticks her finger down her throat, throws up repeatedly while the Goblin chuckles with glee) When I was done, it flushed for me. Then stood on the back of the toilet with its arms crossed, looking smug and mean. (to Goblin, exhausted) Go away! (begins to cry)

GOBLIN: (arms crossed and very demanding) Again!

MEG: (complies, Goblin holds back her hair while she forces herself to throw up again; beat, then to audience) And I knew. Even if my life were different, even if this were my wedding day, I would still be alone in the bathroom, hunched over a toilet.(to Goblin) I can't do this anymore. I'm deleting you.

GOBLIN: (snickering) You can't, stupid. You need me.

MEG: No. I don't. (stands up and steps out of the bathroom stall)

GOBLIN: (growls and lunges at Meg)

MEG: (leans away, narrowly avoiding it; then to audience) It face-planted on the floor. (stomps her food down on the Goblin) I half expected it to have disappeared, but there it was, its little legs snapped in different directions, one eye dangling free of its socket. It was hideous.

GOBLIN: (moans softly)

MEG: (crouches down to examine the damage) For a moment, I felt sorry for it.

GOBLIN: (cackles maniacally) You need me.

MEG: I grabbed it. Flesh. A pulse.

GOBLIN: (screaming in pain and fear)

MEG: My grip tightened to stop it from thrashing around. (squeezes the Goblin until the screaming stops; beat) I always imagined rage to be a red, chaotic state. But it's quiet and translucent and euphoric. A sister to freedom.

(breaks off a Goblin leg and begins to eat it, speaks with her mouth full) I ate the legs first. They were chewy. (wipes mouth with back of hand, then twirls back and forth in front of the mirror) I visualized the way I wanted other people to see me -- really see me-- and know that I was beautiful and that I mattered. . . I'll make it up tomorrow -- gym and juice cleanse. Tomorrow.
```

---

## IC-0586: The Golden Door

- Title: The Golden Door
- Author (byline): Robert Mauro
- Work: Two Character Plays for Student Actors, Pg 147-156
- Publisher: Meriwether Publishing Ltd.
- Publication date as stated: 1988
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MS. WILSON, ANNA
- Teaser before the introduction: No
- Spoken words (computed): 1498
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Mauro
Book: Two Character Plays for Student Actors, Pg 147-156
ISBN: 978-0916260538
Publisher: Meriwether Publishing Ltd.
Date (Month/Year): 1988
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: The debate over immigration has existed for many years, but the intensity of the argument both for and against immigrants to the U.S. seems to be consistently increasing.

ACTRESS 2: Immigration gives struggling people all over the world an opportunity for a better life. This country was built on immigrants who sought opportunity, political & religious freedom, etc.

ACTRESS 1: More immigrants mean more opportunity for terrorists, drug dealers, and other criminals to enter the country.

ACTRESS 2: Some of the most intelligent and ambitious individuals, who are unsatisfied with their own countries, bring their skills to America.

ACTRESS 1: The national identity and language is disappearing. The great "melting pot" is being replaced by divisive multiculturism.

ACTRESS 2: The debate has no easy answers, but one fact remains certain: People from other countries will continue to knock on our Golden Door

ACTRESS 1: by Robert Mauro.
```

### Performance text (classify this)

```text
MS. WILSON: (Pg 147-156) (looks over the folder and shakes her head) Another one. Everyone wants to be a U.S. citizen. They just keep coming and coming and coming. (Looks offstage) Next! (ANNA enters) Have a sea t. . . So you want to be an American, a U.S. citizen?

ANNA: (With an accent) Oh, yes. Yes, I do. Ever since I little girl, I want to be citizen of this wonderful country.

MS. WILSON: Yeah. That's what they all say.

ANNA: It not true? That this is a most wonderful country?

MS. WILSON: (Ironically) Oh, it's just great. Terrific.

ANNA: Yes. I know. Most terrific country in the world. One with the great golden door.

MS. WILSON: Golden door? What golden door?

ANNA: (Surprised that MS. WILSON doesn't know) You know, the lady's door.

MS. WILSON: Lady? What lady?

ANNA: The big lady. Statue lady.

MS. WILSON: Oh, yeah. You mean the Statue of Liberty.

ANNA: Yeah. The big lady with the golden door.

MS. WILSON: Well, I don't know about any golden door. If the door was gold, it would have been ripped off by now, or, at the very least, covered with graffiti. There is no golden door.

ANNA: No, no. I have piece of paper that say it golden. (ANNA looks in her bag and all her pockets for the paper. She finds it in her breast pocket.) I find it. I keep it safe right by my heart.

MS. WILSON: (Impatient, ironic) Wonderful, terrific, but can we get on with this interview? It's been a long day and it's only. . . (Checks her watch) Good lord, only 9:25.

ANNA: You don't want to hear about the golden door?

MS. WILSON: It's really not one of the main priorities in my life - unlike getting this interview over with. Do you understand what I'm saying?

ANNA: (Apologetic) No. My English. It not too good.

MS. WILSON: So what else is new?

ANNA: (Pointing to her, very excited) Oh, I know! I know! New York, New Jersey, New Mexico

MS. WILSON: What?

ANNA: (laughing) Yes. Yes. It very funny. A joke. I hear it on boat coming to this great country. You like my joke?

MS. WILSON: (Very bored) Can we continue?

ANNA: Yes. So about that golden door. . .

MS. WILSON: Are we still on that?

ANNA: Oh, yes. It very beautiful.

MS. WILSON: Next I'll probably hear the one about the streets being paved with gold.

ANNA: (Excitedly) Yes! I hear that, too.

MS. WILSON:I knew it.

ANNA: But it's not true. You have to be very careful where you walk in city street. Many dogs in this city. Many big dogs.

MS. WILSON: You found that out, did you?

ANNA: Yes. But to me streets are still paved with gold. Many jobs! We all work. My brothers, my sisters, my mother, my papa, my whole family. In our country no jobs. Here - many jobs.

MS. WILSON: You do have your work permits?

ANNA: Work permit?

MS. WILSON: Yes. You, as an immigrant, are not allowed to work in this country without a permit. It's the law.

ANNA: But how do we eat or live if we can't work. None of my family is lazy. We all work. It's the American way. No?

MS. WILSON: Look, no permit, no work. Do you understand?

ANNA: No. Do you?

MS. WILSON: (Getting really annoyed) It's not my job to understand! My job is to enforce the immigration laws of this country.

ANNA: The land of the free and the home of the brave.

MS. WILSON: Yeah, right. The one in which you need a permit to work.

ANNA: You have one?

MS. WILSON: Do I have what?

ANNA: This work permit.

MS. WILSON: I don't need one. I'm a citizen. You're not.

ANNA: Oh. So where I get this wonderful permit? Through the golden door?

MS. WILSON: Cute. Very cute. Listen, do you know we can deport you for not having a work permit? Do you realize that?

ANNA: But everyone is entitled to life, liberty and the pursuit of happiness in this great country. Right? And to my whole, entire family, work is happiness. Is this not true?

MS. WILSON: Look, I don't know anything about happiness

ANNA: (Cutting her off, shocked) You don't? But you so lucky. You are citizen. You have job. You have office that is your office. You have much happiness. It is not true?

MS. WILSON: (Pages through the folder) Can we get on with this interview? Is that all right with you?

ANNA: I have to tell you about the golden door.

MS. WILSON: I don't have the time. Do you see all these files? (ANNA nods) All right. Well, these are just todays. I have a lot of people out there waiting to get in. They all want to be citizens. Do you understand?

ANNA: Oh, yes. They all want to be citizen of this great country. From when we were little children we hear stories about Miss Liberty and life, freedom, the great golden door. Yes. I understand this very well. But do you?

MS. WILSON: What do you mean, do I? I'm an American, a citizen. Of course, I understand. What makes you think I don't?

ANNA: The way you speak about us. You sound like you don't like us.

MS. WILSON: What ever gave you that idea?

ANNA: You don't speak to me very nice. My name is right there. But you don't say, "Hello, Anna, welcome to our wonderful country where the streets are paved with gold, where there is a wonderful Statue of Liberty that welcomes you, where there is life, liberty, and the pursuit of happiness. Where there is a golden door. We welcome you, Anna." You don't say that, Ms. Wilson. You sound so unhappy. But you should be happy to live where these things exist. They are not everywhere.

MS. WILSON: Look, Anna, it's just that I'm (a momentary sign of weakness, but she steels herself) Why am I trying to explain myself to you? Just let me get to the questions I have to ask you.

ANNA: But why don't you answer my question? You like it here?

MS. WILSON: Yes. Where else can I shop in Bloomingdale's, Macy's and Sears - and still not find the right blouse? (Anna looks confused; she begins to soften) Look, Anna. . . I don't mean to be rude, but I have a job to do.

ANNA: Yes. You are the doorkeeper.

MS. WILSON: What?

ANNA: Yes. You are the doorkeeper, to the golden door.

MS. WILSON: h, I give up. Will you get it through your head that there is no such thing as a golden door.

ANNA: (Holding up paper) But it says so right here. Miss Emma Lazarus says so. America's greatest poet!

MS. WILSON: (Brushing her aside) Never mind.

ANNA: Wait, wait. You like her. She wrote this poem.

MS. WILSON: We do not have time for a poetry reading. This is the busiest immigration office in the country.

ANNA: And you don't know who Emma Lazarus is?! (Does "shame, shame" gesture with her finger) Shame, shame, Ms. Wilson. You should have big copy of this poem on your door.

MS. WILSON: My door?

ANNA: Yes. Your door. It is the golden door. No?

MS. WILSON: ell, I never looked at it that way.

ANNA: That's because you are on this side of it. You are inside looking out. We, out there, are outside. We are looking in.

MS. WILSON: Listen, why don't we just begin the interview. OK?

ANNA: You the boss.

MS. WILSON: You sure?

ANNA: You have a big office. All these folders. You must be a boss. No?

MS. WILSON: Me? I am the low man on the totem pole around here.

ANNA: Low man? You not a woman? You a man?!

MS. WILSON: No, I am a woman! "Low man on the totem pole" is just an expression. Like "land of the free and the home of the brave," or "life, liberty, and the pursuit of happiness," even "the golden door." They are all just expressions.

ANNA: No, no. They are the truth. You just don't see this.

MS. WILSON: (Checking her watch) All I see is that it's getting late and we have to get on with this interview - golden door or no golden door.

ANNA: Funny you should mention golden door. (Unfolds her poem)

MS. WILSON: Oh, no. You're not going to give me a poetry reading, are you?

ANNA: If you insist.

MS. WILSON: Oh, please, please. I am all ears.

ANNA: (Looking at her ears) No. You have nice little ears.

MS. WILSON: It was just another expression.

ANNA: Oh. You have a lot of them. Don't you? America has much of everything.

MS. WILSON: Especially expressions.

ANNA: You ain't whistling Dixie.

MS. WILSON: (Pointing at ANNA) Very good.

ANNA: See. I make a good American. No?

MS. WILSON: I must admit, you do seem to like this country.

ANNA: No. I love her. And Emma Lazarus. She must have been a wonderful lady. (ANNA puts on her glasses then reads lovingly.)

The New Colossus
Not like the brazen giant of Greek fame,
With conquering limb astride from land to land;
Here at our sea-washed, sunset gates shall stand
A mighty woman with a torch, whose flame
Is the imprisoned lightening, and her name
Mother of exiles, from her beacon-hand
Glows world-wide welcome; her mild eyes command
The air-bridged harbor that twin cities frame,
'Keep ancient lands, your storied pomp!' cries she
With silent lips, 'Give me your tired, your poor,
Your huddled masses yearning to breathe free,
The wretched refuse of your teeming shore,
Send these, the homeless, tempest-tost to me,
I lift my lamp beside the golden door!

ANNA: You like?

MS. WILSON: (moved) I like very much. In fact, I would like to make a copy of that and hang it on my door.

ANNA: Right. The golden door. (Offers MS. WILSON the poem)

MS. WILSON: Yes. (Takes poem) I guess we take a lot of this for granted after being here a while.

ANNA: (proudly) Not me. (beat) So, Ms. Wilson, I make a good citizen?

MS. WILSON: Yes. I'm sure.

ANNA: Ms. Wilson, can I ask you a question?

MS. WILSON: Well, actually, I am supposed to be asking you the questions, Anna, but . . . what the heck, go ahead. Shoot.

ANNA: Shoot?! But I have no gun - (She sees MS. WILSON smiling) Oh . . .

ANNA and MS. WILSON: (Together) An expression!

MS. WILSON: Exactly. So what's your question, Anna?

ANNA: The golden door . . . Some people say they are going to put a lock on it. Is this true? (They look at each other in silence – end scene)
```

---

## IC-0587: The Good Times are Killing Me

- Title: The Good Times are Killing Me
- Author (byline): Lynda Barry
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: March 1999
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: EDNA, BONNA, MRS. WILLIS, EARL, BONITA, MOM, AUNT MARGARET, UNCLE DON, THERESA, TOGETHER, KIMMY
- Teaser before the introduction: Yes
- Spoken words (computed): 1842
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lynda Barry
ISBN: 978-0573693953
Publisher: Samuel French, Inc.
Date (Month/Year): March 1999
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 2: 12-year old Bonna Willis likes to give “beatings” to those who deserve it.

ACTRESS 1: And Edna Arkins might just be someone who deserves it. But that’s before and after.

ACTRESS 2: Before and after their friendship, that is – a friendship isn’t exactly allowed because

ACTRESS 1: Bonna is black and

ACTRESS 2: Edna is white.

ACTRESS 1: And while things might be changing in Seattle in the late 1960’s,

ACTRESS 2: it hasn’t changed enough for these two girls to be friends forever.

TOGETHER: The Good Times are Killing Me by Lynda Barry
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

EDNA: (Pg 9) My name is Edna Arkins. Do you ever wonder what is music? Who invented it and what for and all that? And why just hearing a certain song can make a whole entire time of your life suddenly just rise up and stick in your brain? There was a lot of music on my street. The best time you could hear it was after dinner in the summer when the radios were on and the front doors were open and you hear all the people on their porches (Pg 11) (Sings a few lines from “UnCloudy Day”)

EDNA: (Pg 14) I remember the exact first time I ever saw Bonna Willis. I stood up and shouted “Excuse me girl!” but she didn’t answer me, so I figured either she was hard of hearing or boy was she ever stuck up.

BONNA: I heard you.

MRS. WILLIS: Bonna Willia! You better get back over here! Don’t let me have to tell you twice! *****

EDNA: (Pg 15) Sings: The hills are alive, with the sound of music . . . (to audience) The first best movie I ever saw and the first best music I ever heard. All I ever wanted to be in life was the star of that show. Someone who sang like a record and ran and twirled in the mountains. Someone so perfect that even the nuns couldn’t understand her. (Notices Bonna again) (Pg 30) The first time I ever saw Bonna Willis close up – the main thing I noticed about her was that for earrings she had little pieces of broom straws with the ends burnt off stuck through her ears. I asked her way later what was the first thing she noticed about me.

BONNA: (almost flirtatiously) How much you looked like the what-me-worry guy off of Mad Magazine. I’m not saying it to be cold. You can’t control the first thing you notice about somebody. (Pg 34-36) (To a boy off stage) Mess with my brother again and I’ll knock you upside your nappy little head (Bonna stomps her foot like she is going to run after him)

EDNA: Back then, all I knew about Bonna Willis was that I had to watch out for her.

BONNA: Everybody did. (to boy off stage) Laugh all you want to, fool (She runs after him)

EDNA: She would get after you, swearing to beat the a**es off everyone in our neighborhood on a rotating basis. And it wasn’t just all talk and no action either.

EARL: (looks on stage to see that Bonna is gone, then enters with Bonita)

BONITA: Uh huh. Then where she at?

EARL: Like I told you. She run home crying. She come out here all trying to mess with me like she really something. I had to just laugh in her face. I say “Listen girl.

You just a squirrel in my world!” I do my foot just like this . . . (Earl stomps his foot imitating Bonna) You should have seen her running. (Sees Edna) Ain’t that right?

EDNA: OOOOOOooooo! Bonna can beat you’re a** any day! (Edna takes off running)

EARL: Don’t you let me catch you on this street alone!

BONITA: (Deadpan) “. . . and then I said ‘Listen girl. You just a squirrel in my world.’

MOM: What was all that shouting out there?

EDNA: Nothing.

MOM: I don’t want you getting mixed up with those people you understand me?

EDNA: I know. *******

EDNA: (pg 31) My father came home one day with a present I thought was going to change my life! It was my very own record player! (pg 37-38) In honor of [the] new record player, I created The Record Player Night Club down in the basement. It was probably the best place ever invented. (Edna runs a distance from the room and acts like she’s entering for the first ime) Ohhh! Oh! This place is incredible (In a British accent) This place is totally mod, luv! (puts on a record and begins swaying to music that we can’t hear) (Pg 40-41) (Pounding on the door – Bonna enters with her own records) Bonna!

BONNA: Heard you got a record player . . . can I play it?

EDNA: I didn’t know what I was supposed to do because we still had the rule of No Negro Kids Can Come In Our House. I didn’t know how I was going to explain the rule to Bonna. Then I figured out we were in the basement so it would be OK with mom as long as [she] didn’t come inside the real part of our house.

(Bonna puts on a record “I’m Black and I’m Proud” – she sings and dances along) Bonna’s records had a screaming sound that I had never heard before.

BONNA: James Brown. (sings) Say it loud. I’m Black and I’m proud (Bonna does a black power fist. Edna has no idea what it is and briefly does a lame and low version of it back)

EDNA: (Pg 42) I had never heard of being proud about being a Negro before so I wondered, is this a joke song or what? She also told me that Blank Panthers were coming to beat the whitey’s, and I didn’t know what she was talking about. (To Bonna) I know that. Who doesn’t know that? (Bonna puts on a new record “The Tighten Up” and begins to move to the music)

BONNA: (To Edna) Come on. I’m going to show you my cousin’s dance called The Tighten Up

EDNA: I already know that dance.

BONNA: Prove it.

EDNA: Maybe I don’t feel like it.

BONNA: You lie you die.

EDNA: Shut up.

BONNA: Come on. I just got it from my cousin in DC so I know no one here knows it yet. – Stand over here. (Impossibly fast) Go sideways like this and move your hand like this and your other one like this then when they go “Now make it mellow” move your arms like this.

MRS. WILLIS: (off stage) Where are you? Bonna! Bonna Willis!

BONNA: Gotta go (she takes off)

EDNA: That night I imagined me and Bonna becoming best friends. What that would be like and how everyone in the neighborhood would start to be afraid of me the same way they were afraid of her. (Edna begins dancing the way Bonna had shown her) I saw myself being able to do The Tighten Up so perfectly that people would faint from amazement. Me and Bonna in front of the lunchroom during assembly, doing the Tighten Up.

******

(pg 65-66) (Edna and Bonna on the porch – singing together to “Weak Spot”)

EDNA: Gotta go.

BONNA: No. Street lights not even on yet. Your mom says you don’t have to go back ‘til the street light comes on. Ask your mom can you stay over!

EDNA: Stay overnight?

BONNA: Yeah. My mom don’t care.

EDNA: Bonna. Wait . . . Uh . . .

BONNA: What?

EDNA: You can probably stay over at my house.

BONNA: Why can’t you stay over at mine? . . . . Because she doesn’t like me.

EDNA: She dos so. She just acts that way because she . . . she . . she . . . gets headaches. Walk me!

BONNA: Forget you!

EDNA: Come on. I’m always walking you. Come on! (To audience) Everyday it was like that. I would get up every morning and go to her house of if she got up first she would come to mine and we would just spend the day together doing it didn’t matter what. She was all I thought about. Every day I would say it in my head. “My Best Friend Bonna.”

BONNA: Hey! My mom just called your mom and she said you could stay over. (Edna looks at her astonished) AAAAAAaaaahhh! Psyched you out! I got you! OOOOOooo psych on Edna!

EDNA: Every night she would walk me to my house . . .

BONNA: Then we would turn around . . .

EDNA: And I would walk her to hers . . .

BONNA: then we would turn around and . . .

EDNA: I remember standing on my front porch watching her and waving goodbye until the last possible second. And I thought it was going to be like that forever. I thought we would grow up, get married to twins, and live next door to each other for the rest of our lives. ******

EDNA: (Pg 76-77) In the middle of summer my aunt Margaret saw a TV special on racial prejudice. From then on for about two weeks, her new hobby was . . .

AUNT MARGARET: Improving the life of the underprivileged Negro. Everyone must do their part or the ones in our area are going to get as mad as the ones I saw on TV and burn everything we own right to the ground.

UNCLE DON: Well, everyone agrees it was a mistake to bring them here in the first place and they aren’t happy, so why not send them back?

EDNA: Bonna, do you want to go back to Africa?

BONNA: Edna, sometimes you can be so stupid. *************

EDNA: (Singing Kumbiaya) The song of all Girls Scouts was the first song I ever got sick of in my whole life. Ever since I first knew about Girl Scouts I had always wanted to be one. If I joined Girl Scouts I would get to hang around Joycie Mercer, our troop’s most popular girl. She had a canopy bed. She was my dream.

BONNA: Joyie Mercer!

THERESA: Edna, Joycie Mercer says she wants to talk to you

BONNA: Don’t she got legs? Can’t she come over here and tell us her own self?

THERESA: Excuse me but I’m afraid I was talking to Edna. . . It’s about her party.

BONNA: What Party?

THERESA: It’s going to be a blast! (She walks off)

BONNA: (to Edna) What party?

EDNA: Don’t ask me. I don’t know. (Stares off in the direction of Joycie Mercer)

BONNA: If you want to talk to her so bad, then just go.

EDNA: Bonna.

BONNA: I’m quitting Girl Scouts. I am. I hate it. I always hated it. I’m sick of [wearing] ugly uniforms and sell[ing] nasty cookies.

EDNA: If you hate it so much then why’d you even join?

BONNA: You asked me to, remember?

EDNA: Bonna! Will you quite being so weird? It’s not like I can control who Joycie Merer invites in her life! (Bonna leaves) Bonna! For the rest of the summer it was like that. Whenever I saw her I got this feeling in my stomach of two magnets pointing the wrong way and I couldn’t get them to point back right.

(They catch each other’s eye and quickly turn away) ********

TOGETHER: SEVENTH GRADE:

BONNA: Every kid from my old school, all of us who had ever lived on the same street together and played together all our lives stopped talking and walking with each other.

EDNA: From second we walked through those school doors we all automatically split into groups of who was alike. Everyone knew exactly what to do. We had to constantly read books and poems about equality in English and I wondered sometimes if Bonna thought of me in the way I thought of her when I read them. To Kill a Mockingbird. A Raisin in the Sun.

BONNA: “What happens to a dream deferred?” Yeah. I thought of you.

EDNA: We had to write out own stories and poems and discuss them. We could each write [our own] answer and the answer was always the same.

BONNA: Love each other, love each other, love each other.

EDNA: And we really through that things could change until the bell would ring, and we would go back into the hallway and know there is no way some puny little poem or story could change anything. (A black girl walks up behind Edna and runs into her)

KIMMY: Get your big behind out of my way.

EDNA: I’m not in your way.

KIMMY: What’d you just say to me? Girl, I’m talking to you. (Edna turns to walk away and Kimmy shoves her. Bonna watches without saying anything)

EDNA: (To Bonna) Why don’t you tell them? Why don’t you do something, stupid? (Bonna squares off against Edna) I couldn’t believe she was really going to hit me because I knew that inside we were still friends. We are! (Bonna slaps Edna hard) Don’t you even remember? I know your mother and father! I know the color of the walls in your room.

BONNA: The next thing I knew we were snatched by the arms and dragged down to the office just like I had seen girls being dragged every day since I got there.

EDNA: We sat in chairs waiting for the vice principal to come. I tried looking at Bonna but she kept staring straight ahead. I could see the streaks on her face.

BONNA: I heard Edna crying but I couldn’t look at her. Seems like we sat there forever.

EDNA: We acted like we had never met. Like all it was any black girl slapping any white girl that mouthed off to her. Something that happened every single day and would just keep on happening would without end. When he called my mother to tell her, she never knew that the girl they were talking about was Bonna. Just like Bonna’s father never knew that the other girl was me.

BONNA and EDNA: (Sing Uncloudy Day)
```

---

## IC-0588: Grace and Glorie

- Title: Grace and Glorie
- Author (byline): Tom Ziegler
- Work: Not specified
- Publisher: Doubleday
- Publication date as stated: Feb 1997
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GRACE, GLORIA
- Teaser before the introduction: Yes
- Spoken words (computed): 2053
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tom Ziegler
ISBN: 978-1568652726
Publisher: Doubleday
Date (Month/Year): Feb 1997
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Two women -- Two lives that could not be more different.

ACTRESS 2: One is 90 years old. She is weathered by loss, sustained by faith, and preparing for the final chapter of her life.

ACTRESS 1: The other built a life of success in the city—educated, accomplished, and certain she understood how the world worked… until tragedy shattered everything she believed.

ACTRESS 2: In a small farmhouse, surrounded by pain, memory, anger, and hope, two strangers confront questions that follow every life:

ACTRESS 1: Why do we suffer?

ACTRESS 2: What do we hold onto when everything is gone?

ACTRESS 1: And what does it mean to let go?

TOGETHER: Grace and Glorie by Tom Ziegler
```

### Performance text (classify this)

```text
GRACE: (Pg 50) (singing softly to herself*) “He will give me grace and glory and go with me all the way.”

GLORIA: (Pg 5-8) Hi. I’m Gloria Whitmore (waiting for some recognition, getting none) You probably don’t remember, but we met briefly at the hospital last week.

GRACE: I remember. Wha’cha think, I’m senile?

GLORIA: No, of course not. Is there anyone here with you? Is your grandson here?

GRACE: Roy? He’ll be back this evenin’. You need to talk to Roy?

GLORIA: You should have someone here with you – to care for you.

GRACE: Roy takes care of me. Cuts my fire wood, fetches me things from the IGA. I gotta pay him. Roy don’t do nothin’ for free.

GLORIA: I’m not here to talk to Roy, Mrs. Stiles, I’m here to see you. When you left the hospital this morning you forgot your medication. Here. (taking a package from her bag)

GRACE: You must think I’m a mighty forgetful ol’ lady! Well, I’m not! Told the doctor I didn’t want none o’ that stuff. You people and your drugs. I’ve been doin’ it your way for mor’n a year now, and all I can say is enough’s enough!

GLORIA: (a breath) I’m a volunteer with an organization – it’s called Hospice. Your doctor said he told you all about us.

GRACE: Listen, honey, I don’t mean to be unfriendly, but whatever it is you’re sellin’, I’m sure I’m way past needin’ it. (Pg 14) Broke my hip last year. Had to go to the hospital. That’s when they found the cancer. (Pg 17) I’m dying -- got a few weeks. Honey, when you’re 90 years old, death don’t come as no surprise. I buried my parents, my husband, and all of my five boys. If there’s one thing I know about its death. You do this for a living, help people die?

GLORIA: Why are you making this seem so ridiculous? You know, you’re a perfect example of what Hospice is all about! Your grandson, he picks you up from the hospital and dumps you here. You have no one to turn to for help. And believe me, Mrs. Stiles, you’re going to need help!

GRACE: But I’m not alone. The good Lord’s here with me.

GLORIA: Look, this hospice booklet. There are several stories in here about women just like you. Won’t you at least read it?

GRACE: I don’t think so. In the first place I’m not interested! In the second (she can’t read) – we’ll just stop with the first place.

GLORIA: Mrs Stiles, do you – You don’t do you? My, God, that explains everything.

GRACE: Don’t you have a family at home to take care of? Or a job. Thought all you young women nowadays had jobs!

GLORIA: I had a job in New York. I’ve looked for something around here, but there isn’t anything – That’s when I heard about this new hospice program, that they were desperate for volunteers with professional skills. I have an MBA from Harvard!

GRACE: Just tell me one thing. What do you get out of this?

GLORIA: Nothing! Okay, let’s just say I’m interested in –

GRACE: Death? You can’t even say the word.

GLORIA: Death. (Pg 25) And my name is Gloria. (Pg 37) [My] son. Danny. He was killed in an automobile accident a couple of years ago.

GRACE: These young people today and their automobiles. Why do they insist on driving so fast?

GLORIA: Danny was only twelve years old. He wasn’t driving. I was.

GRACE: Ter’ble thing to lose a child. My Carroll died when he was a baby. Went in to check on him one morning and he wasn’t breathin’. Doctor come. Said these things just happen. Few years later Duane was out huntin’ with his Daddy. Tripped over some barbed wire buried under the snow? Gun went off. He was 10 years old. Got so I hated to let the little ones out o’ my sight. Thought I was goin’ to lose ‘em all. Guess I did, though, didn’t I? Guess my only comfort is I’ll be seein’ ‘em all real soon now.

GLORIA: Do you really believe that? About seein’ your children in another life?

GRACE: Course I do, don’t you?

GLORIA: I . . . No.

GRACE: S’pose next you’re goin’ to say you don’t believe in God. (Pg 50) When I was just a girl, there was this hymn my Mama liked to sing. Called “Where He Leads Me.” (singing*) “He will give me grace and glory, and go with me all the way.” Mama used to laugh “We got our little Grace,” she’d say. “Now all we need is a little Glorie.” (Pg 52) (irritably) Why don’t you go home?

GLORIA: I’m not leaving you here alone. Are you going to let me put you to bed?

GRACE: No! (Pg 53) I don’t want to be asleep when He comes.

GLORIA: When who comes?

GRACE: Death. Oh, I’m afraid of Him, I am. But it’s like this time my Daddy hauled us kids all the way to Richmond to the State Fair. They had this Ferris wheel there. Looked to be least a mile high. I wanted to ride that thing mor’n anything in the world, but I was too scared. My whole life’s been like that. Always too scared. But this time I’m ready to be lifted up into that Promised Place (breaking down) where I won’t hurt or be afraid ever again. (Gloria goes to her but Grace, embarrassed pushes her away)

GLORIA: (Pg 55) (backing away) Okay, okay.

GRACE: I regretted not havin’ a daughter. Always felt I had so much to give, so many secrets to share. Boy children, they ain’t interested in learnin’ nothin’. All they want to do is break away. Get out and tear up the earth. You know I’ve always marveled the human race has been able to survive long as it has in the hands of men.

GLORIA: You sound like a liberated woman, Grace. I’m impressed.

GRACE: Sure, I’m liberated all right. Ain’t been mor’n fifty miles from this farm since the day I got married . . . (quiet for a moment) What I just said, ‘bout boy children tearing up the earth? I wasn’t talkin’ ‘bout your little boy. He wasn’t like that, was he?

GLORIA: No.

GRACE: What was his name? Danny? (Gloria nods) Bet he was smart.

GLORIA: Yes. (beat) But he was still very much a boy. My husband saw to that. But for every jock thing Peter pushed Danny into, I insisted on equal time. Like with his piano. I mean he was only 12 years old and already developing his own style. He reminded me of – me when I was his age.

GRACE: Just look at your face. All lit up. Wondered if I’d ever see you smile like that.

GLORIA: Oh, Grace, that was such a time in my life. I had just moved to a very large [law] firm, brought in, I might add, as full partner. I finally had power, Grace. And money. I bought a car. An expensive car . . . (tapers off, lost in thought; shakes it off and changes the subject) Your children. The ones you lost when they were small. How did you deal with . . . losing them?

GRACE: Deal with it? I’m not sure I know what you mean. I grieved. Still do. But it was the good Lord’s will.

GLORIA: And you didn’t question it? The good Lord’s will.

GRACE: What I don’t think a person like you understands, people like us, people tied to the earth, we’re used to death. You civilized people. You’ve moved so far away from death you forget it’s as much a part of life as being born -- these things just happen.

GLORIA: (moving away) Oh yes, it certainly did happen. One warm, September afternoon

GRACE: Honey, don’t –

GLORIA: . . . it had been Danny’s first day at school. I decided to pick him up. In the new car. We were heading back across town. I don’t know where it came from. The newspaper truck. When it hit us, we were pinned inside the wreck for more than an hour. Danny was on my lap. And as I held him, I could feel his life slowly slipping from his body. And there was nothing I could do. . . so we buried him. This gentle, gifted boy. Disposed of his clothes, his – things. And then, I just shut down. ouldn’t go to work. Wouldn’t answer the phone. Wouldn’t even go outside. Peter dragged me from one doctor to another. We ended up with a shrink who suggested a change, somewhere far from the city. So now here I am . . . Okay, maybe I did deserve to get slapped down. I mean, I had become a little lofty, a little full of myself. But if these were my sins, MY SINS, why was it Danny who paid for them? You talk about God? What kind of God is this? Look at your life. Haven’t you ever asked yourself . . . (stops. gropes for control) I’m sorry. I don’t know why I’m doing this.

GRACE: My life. What about my life? Say it.

GLORIA: (trying to push it back but can’t) You buried not one child, but five! You have a grandson. Who are you to him? A woman he charges to run errands and cut wood. Haven’t you ever asked yourself what your life’s been for? Here you are a sick old woman, ravaged with pain, without a soul in the world to even care whether you live or – Grace, I – I think I’d better go home after all.

GRACE: I never have asked myself that question. What’s my life been for – Maybe I should. I sure ain’t left my mark on much o’ nothin’.

GLORIA: Grace, I’m sorry.

GRACE: Why should you be sorry for my miserable life? Got nothin’ to do with you. I’d still like to know what you’re doin’ here, messin’ with death. So, you lost a child.

GLORIA: Things happen . . . just happen. No rhyme, no reason. No one pulling the strings.

GRACE: I didn’t say there was no reason.

GLORIA: Then what is it?

GRACE: How should I know? You accept each day as it comes. You don’t question. Something like this happens, you start over. Good heavens, honey, either you do a thing or you don’t. What other choice you got?

GLORIA: Oh, I’ve got choices. At least a few.

GRACE: Like what? (slowly) Oh. Oh, I see. That what this is, this volunteerin’ you do? You here to try Death on for size ‘fore you go off and kill yourself? Is that it? IS IT!

GLORIA: IT SHOULDN’T HAVE HAPPENED, GODDAMNIT! He was a brilliant, innocent boy with his whole life in front of him. You’re the one with the faith, you tell me! What heavenly purpose was served by crushing his body and leaving it on my lap to die? All I want is an answer, Grace! One lousy reason! (beat) Except there is no answer, is there? I’m sorry, but whatever this – game is, I can’t play it anymore!

GRACE: (Pg 70) (long pause) I don’t like what’s happenin’ to me [either]. Ain’t sayin’ I’m doubtin’. Never doubted the good Lord one second o’ my life. But you got me wonderin’. So many things. (Pg 80) You said it yourself. My life’s been for nothin’! Absolutely nothin’! I’m an illiterate, backwards old woman! (Pg 95) (freezes. takes a quick breath. her face goes blank)

GLORIA: Grace? Grace, what is it?

GRACE: Pain . . . Goin’ to be bad.

GLORIA: Grace?

GRACE: Oh, sweet Jesus.

GLORIA: (reaching for the morphine in her bag) Listen to me. Grace, this is morphine.

GRACE: NO! NO DRUGS! . . . Oh, sweet Jesus!

GLORIA: DAMNIT, GRACE! THERE IS NO REASON TO SUFFER LIKE THIS!

GRACE: I DON’T CARE! WON’T DO NO GOOD! (Gloria holds Grace’s mouth open, administers the drops. Grace pulls away) Only fools believe in God. That’s what I am. A FOOL! All the times I was cold and hungry and hurtin’ and wantin’ to run away from this miserable farm. But I though this is where God wanted me to be. Is that what you come here for? (shouting) TO TELL ME MY WHOLE LIFE WAS FOR NOTHIN’?!

GLORIA: Grace, please.

GRACE: Honey, I know I’m ignorant, but I’ve been happy in my ignorance! WHY COULDN’T YOU O’ JUST LET ME DIE THAT WAY? I DON’T WANT YOU HERE! GET OUT! I’m an old woman. Why can’t you understand that? Go on, get out of here! I don’t need you!

GLORIA: Yes, you do! (beat) Grace, I’ll probably never believe in the same things you do. But you’ve shown me . . . that it might be possible to believe in something again. Are you listening to me? Grace?

GRACE: (a little surprised) Pain’s goin’ away. It’s that morphine ain’t it? (Gloria nods) (Pg 101) (thinking, then speaks) I think that’s all God wants any of us to do . . . hold on to each other with all our might. (tears) Look at me, cryin’ like a baby! (long pause) (Pg 102) If I take a nap, you think I’ll wake up? (Gloria’s eyes fill with tears) (Pg 103) You cryin’, honey? Why?

GLORIA: I don’t know.

GRACE: (holding out her hand) Maybe you’re grievin’ for me already . . . That’s what this is, this messin’ with death you do. You think if you stop grievin’ you’ll finally have to let go of your little boy.

GLORIA: (takes Grace’s hand) I loved him so much, Grace.

GRACE: ‘Course you did. But, honey, it wasn’t death tied you and that little boy together, it was life. (closes her eyes and falls asleep)

GLORIA: (kneels by her side, holding her hand; sings softly) “He will give me grace and glory, and go with me all the way.”*
```

---

## IC-0589: Grandpa

- Title: Grandpa
- Author (byline): Mary Krell-Oishi
- Work: Perspectives: Relevant Scenes for Teens, Pgs 167-176
- Publisher: Merriwether Publishing, Ltd
- Publication date as stated: March 1997
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: KATHY, JULIA
- Teaser before the introduction: No
- Spoken words (computed): 2106
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mary Krell-Oishi
Book: Perspectives: Relevant Scenes for
Teens, Pgs 167-176
ISBN: 978-156608030
Publisher: Merriwether Publishing, Ltd
Date (Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: When a loved one is diagnosed with Alzheimer's disease, the effects on the family can be overwhelming.

ACTRESS 2: The reality that someone you love has such a devastating illness can trigger a range of emotions — including fear, sadness, confusion and anger.

ACTRESS 1: Conflicts are common as family members struggle to deal with the situation.

ACTRESS 2: In this selection Kathy and her younger sister Julia struggle to understand each other and the process.

TOGETHER: Grandpa by Mary Krell-Oishi
```

### Performance text (classify this)

```text
KATHY: (Pgs 167-176) Julia, is Mom home yet?

JULIA: Not yet.

KATHY: Did she say when she'd get home?

JULIA: Nope.

KATHY: Great. Have you started dinner?

JULIA: No. Was I supposed to? No one told me.

KATHY: Just once it would be really nice if you did something without having to be told.

JULIA: (a beat) Yeah. OK.

KATHY: You are something else, you know that? Did you at least clean up the dishes?

JULIA: No, Kathy, I didn't clean up the dishes.

KATHY: Good grief, you are beyond belief.

JULIA: I'll do it, OK. I was planning on doing it later. Not everything has to be done on some mythical schedule you've decided on.

KATHY: Well, please, -don't put yourself out. God forbid that you might actually help out around here without having to be told. Forget it. I'll take care of them. God knows I take care of everything else around here lately.

JULIA: Martyr mode. Good.

KATHY: And just what does that mean?

JULIA: Just that you're at your happiest when you can do it all and make sure that everyone knows you're the one doing it.

KATHY: Someone's got to follow through around here. It's for sure that it isn't going to be you.

JULIA: Fine! You want them done now, I'll do them now!

KATHY: Good! Do it!

JULIA: What are you going to do?

KATHY: Well, I can assume that there is still laundry sitting on the washer that has yet to be done, the carpets need vacuuming, and dinner needs to be started. So, I guess that will keep me busy, unless, of course, you managed to take care of at least some of the chores. (No response from JULIA) Just as I thought.

JULIA: I said I'd take care of the dishes for you.

KATHY: What do you mean for me? You are not doing me any favors, you know. Why, all of a sudden, are you thinking you're doing the dishes for me?

JULIA: Forget it. (begins to exit)

KATHY: And clean up your crap from the room.

JULIA: Why don't you quit telling me what to do?

KATHY: Because if I don't, nothing gets done. And Mom doesn't need to come home to the house looking like this.

JULIA: She won't even notice.

KATHY: The hell she won't.

JULIA: She doesn't notice anything anymore. We could not even be here and she wouldn't miss us.

KATHY: For once in your life, quit thinking about yourself and think about someone else. Mom is going through enough right now without you throwing your attitude at her.

JULIA: I don't know why she has to be at the hospital all the time.

KATHY: Because her father is dying. Grandpa is dying.

JULIA: He's been dying. Why doesn't he get it over with?

KATHY: (a beat) I can't believe you just said that.

JULIA: (quietly) Well, I did. And I mean it, too.

KATHY: I have never in my life heard anything so awful come out of your mouth. I've known you to be unbelievably selfish, self-centered and wrapped up completely in your own needs, but this is out of control, even for you.

JULIA: Why is it selfish? Honestly, why? He's going to die anyway, isn't he?

KATHY: He's had bad times before and pulled out of them. He'll pull out of this one, too.

JULIA: Take off the rose-colored glasses, Kathy. Join the real world. Grandpa is dying. He's been sick for a long time and dying a little bit more everyday. He's done nothing but get worse.

KATHY: He has good days.

JULIA: When? When was the last good day he had? A year ago? Maybe longer?

KATHY: How would you know? When was the last time you went to see him?

JULIA: What's the point? He doesn't even remember who we are anymore.

KATHY: He does too remember. Maybe not our names, but he knows we are family. His eyes light up when we come in the room and hug him.

JULIA: His eyes light up whenever anyone walks in the room and gives him a hug. He's a friendly guy. However, whether you want to accept this or not, he has no idea who we are.

KATHY: You are so cold.

JULIA: No, I'm not. I'm realistic. I've watched Grandpa shuffling around, looking at all of us without really knowing who we are, unable to complete a coherent sentence, and then I watch Mom get sadder and sadder. There is no point to this.

KATHY: God does not give us more than we can bear. What does not kill us makes us stronger.

JULIA: Well, I feel better now. Cliches sure can brighten up a cloudy day. Why don't you tell Mom that when she comes back from watching her father deteriorate into an empty shell.

KATHY: (looks at JULIA for a moment, then quietly) I have things to take care of.

JULIA: Yes, do what you always do. Walk away from reality. For God's sake, don't face what is happening.

KATHY: Oh, be like you? Wish Grandpa right into his grave.

JULIA: If you had any compassion, you would.

KATHY: Compassion? You talk to me about compassion? Who makes sure things are taken care of? Not you. Who tries to comfort Mom when she feels down about everything that is going on? Not you. Who goes to visit Grandpa in the home? Not you.

JULIA: I do my share, dammit. Maybe I'm not as vigilant about dusting the nooks and crannies of this house, but I do help out. And I do try to talk to Mom, but it's hard.

KATHY: And visiting Grandpa? What about that?

JULIA: I can't. I just can't. It's too hard to take.

KATHY: Ah, here we go. Now we're getting down to it. It's too hard to take for poor little Julia. Never mind the times he was there for you. Let's just forget all about that. Forget about the Disneyland trips, the donut hunts, dancing at parties, basketball games. Let's just forget everything we ever did with Grandpa and take care of ourselves. That is just so typical of you.

JULIA: You don't get it, do you? Don't you see that those are the memories I want to keep alive? I want to remember that man that I loved, that I looked up to, the way he was then, not the way he is right now. I don't even know this person.

KATHY: Well, you better try to know him while there's still time to do so.

JULIA: That's just it. There is no time anymore. I didn't tell you this, but I did go down to see him about a month ago. I went down to the home after school one day to see how he was. It had been a long time, at least a couple months since I'd been down there. You know what he did? He looked at me. No, he looked through me.

KATHY: Did you tell him who you were?

JULIA: I shouldn't have to tell him who I am. I'm his granddaughter for God's sake. He was in the delivery room when I was born. He should know who I am.

KATHY: He can't help what is happening to him.

JULIA: I know that, I'm not stupid. But it gets worse. I stayed for just a few minutes, and then he said he had to use the bathroom.

KATHY: Did you call someone to help him?

JULIA: It was too late. He had gone already. He looked so helpless, so confused. Then, when the nurse came to get him, he smiled at her like he smiled at me and he just walked away with her.

He just walked right away with her as if he had completely forgotten I was there. And he probably had.

KATHY: I didn't know he had lost control over his bodily functions.

JULIA: Why don't you just say it? He peed all over himself. That's what he did. And I had to stand there and watch. Just watch and there was nothing, not a damned thing I could do. And if it makes me feel this bad, how do you think it makes Mom feel? It's her father, the man who raised her, who taught her about life, who changed her diapers. Now she has to change his. It's just not fair.

KATHY: No, it's not, but it has to be dealt with.

JULIA: Why? Why does it have to be dealt with like this? Do you remember Duchess?

KATHY: The cat?

JULIA: Let's say Grandpa was drowning and so was Duchess the cat. Who would you try to save?

KATHY: Grandpa, of course.

JULIA: SO you love Grandpa more, OK?

KATHY: OK. What's your point?

JULIA: How did Duchess die?

KATHY: We had to put her to sleep because she...

JULIA: We put her to sleep because she got old and sick and "lost control of her bodily functions."

KATHY: Duchess was a cat.

JULIA: SO why is a cat allowed to die with dignity? Why is it humans are forced to live a life of degradation?

KATHY: I said I don't want to talk about this.

JULIA: How do you think Grandpa would feel if he knew what was going on? Do you think he'd want to live like this?

KATHY: I don't know.

JULIA: The hell you don't. Would you want to? I know I wouldn't.

KATHY: You can't say that.

JULIA: Yes, I can. Let me tell you right now, sister dear, that if I should come down with this horrible humiliating disease called Alzheimer's, put a pillow over my face and call it a day. There is no way I'd want to live like that.

KATHY: So what do you suggest we do? Smother Grandpa in his bed? Take him out of the home on a trip and leave him on some city street? Maybe throw him in front of an oncoming car. What do you think would be the humane thing?

JULIA: I have no idea. But I do know that this is all wrong. There is nothing right about what he is going through.

KATHY: Well, just thank God our family has enough money to provide a good place for him to live comfortably.

JULIA: And that's another thing. What about people that don't have that kind of money? You didn't go with Mom when she had to finally make the decision to put Grandpa in a home. You should have seen some of those places. Dirty, disgusting, smelly. Some of those old people were walking around with clothes that reeked of urine. Not nearly enough caretakers for the patients. How do you think those families feel who can't afford what we can in the way of care and they have to visit their mothers, fathers, grandparents? And what about us? Grandpa is only sixty-seven years old. He could live for another ten years like this, lingering in and out of consciousness, that dull vacant look in his eyes when he does come around. Financially this could wipe Mom and Dad out.

KATHY: And what if it's hereditary? I'll be honest with you. I have thought about all of this. Maybe that's why I'm so obsessed with doing everything around here. It's my way of not thinking.

JULIA: Thinking about what?

KATHY: About that this might be genetic. Mom could get it, then it could be us. Then what?

JULIA: It won't happen. They'll have a cure by then.

KATHY: You think? I don't. There's tons of money going for cancer and for AIDS. But what about Alzheimer's? You never hear anything about it. There won't be a cure if there is no research.

JULIA: There will be. There has to be.

KATHY: I'm scared all the time. Every time Mom comes in a room and forgets why she came in, it scares me. When she misplaces something, it freaks me out.

JULIA: Everyone does that. We all forget things. It doesn't mean...

KATHY: I know it doesn't. Intellectually I know. But emotionally...

JULIA: I thought you were the strong one through all this.

KATHY: That's what I try to be. I keep thinking that if I keep busy, if 1 keep things going here in the house and make sure that everyone is taken care of, then maybe nothing will happen.

JULIA: You can't stop things from happening. Like I said, Grandpa is going to die. He should get it over with. And I don't mean that in a cruel way.

KATHY: I know.

JULIA: He should have dropped dead of a heart attack five years ago on the basketball court. That's how he would have liked to go. That's a memory I would have loved. Grandpa's last days being who he was - active, fun, and doing what he loved. Not this shell of a man who just stares into space.

KATHY: It would have been better. Better than this.

JULIA: Yeah. (they sit for a moment in silence) I'll do the dishes.

KATHY: OK. Mom should be home pretty soon.

JULIA: I think we should talk to her.

KATHY: Why?

JULIA: Because she probably feels exactly what we are feeling, but is too guilty to talk about it. She needs to be able to talk about it. Like we just did.

KATHY: Yeah. I guess so. Yeah. God, this sucks.

JULIA: It does, doesn't it?
```

---

## IC-0590: Grey Gardens

- Title: Grey Gardens
- Author (byline): Doug Wright, Scott Frankel and Michael Korie
- Work: Not specified
- Publisher: Dramatists Play Service Inc.
- Publication date as stated: May 2008
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: EDITH, EDIE, ACTRESS 1, ACTRESS 2
- Teaser before the introduction: Yes
- Spoken words (computed): 1233
- Already set (do not supply): none

### Source block (context only)

```text
Author: Doug Wright, Scott Frankel and Michael Korie
ISBN: 978-0822221814
Publisher: Dramatists Play Service Inc.
Date (Month/Year): May 2008
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Welcome to the private world of the Beale ladies, outcasts of a wealthy and famously dysfunctional branch of the Kennedy dynasty—the Bouvier-Beales.

ACTRESS 2: Little Edie, born in 1917 was the family beauty, “surpassing even the dark charm of Jacqueline,” She was her mother’s crown jewel.

ACTRESS 1: Her debutante party in New York City was covered by The New York Times.

ACTRESS 2: She dated Howard Hughes and turned down proposals from JFK’s oldest brother Joe Jr. and millionaire J. Paul Getty.

ACTRESS 1: They lived the life of American Royalty until Little Edie’s father left; divorcing her mother by telegram, from Mexico.

ACTRESS 2: He left his ex-wife Grey Gardens, a spectacular 28-room mansion with a view of the ocean.

ACTRESS 1: And this is where the story becomes something from a gothic novel.

TOGETHER: Grey Gardens by Doug Wright, Scott Frankel and Michael Korie
```

### Performance text (classify this)

```text
EDITH: (Pg 62) Edie? Edie!!

EDIE: (Pg 2) I’ve found it, Mother Darling! I found your old record! (puts record on the
record player and begins singing)
She is the girl
Who has everything.

EDITH: EVERRRYTHING!!

EDIE: She has the world on a string

EDITH: ON A STRRR-ING!

EDIE: (appears from off stage. She primps, looking at herself in a hand mirror) Isn’t it wonderful?

EDITH: I recorded it in 1941. I was very serious about my singing; loved it!

EDIE: (Pg 69) Just listen to this! (as Edie speaks, Edith begins to prepare dinner for the feral cats living in their house) The Hamptons Bee. July 1972. “The elderly, bed-ridden Aunt of former first lady Jacqueline Kennedy, Mrs. Edith Bouvier Beale and her adult daughter, Miss Edie Beale, a former debutante, are living on Long Island in a garbage-ridden, filthy, 28-room room house with fifty-two cats, fleas, cobwebs, and virtually no plumbing. After vociferous complaints from neighbors, the Board of Health took legal action against the reclusive pair” (Pg 3) They’re calling us “cat ladies.”

EDITH: Here kitty!

EDIE: And our house. They’re saying Grey Gardens is a “public eyesore.”

EDITH: Grey Gardens is one of the most renowned homes in America! (singing again) SHE IS THE GIRL WHO HAS EVERYTHING . . .

EDIE: Remember? You sang this song for me. I was “The Girl Who Had Everything” . . . once.

*****(Flashback to 1941 – Little Edie’s engagement party)*****

EDITH: (Pg 4-6) SHE IS THE GIRL WHO HAS EVERYTHING . . .
TALENT AND BEAUTY SUBLIME . . . .!
. . . THE CROWDS AND THE CLAMOR
AROUSED BY HER GLAMOR
WILL FADE LIKE THE ECHO OF A CHIME

EDIE: (Jumps up and applauds) Mother Darling, what a charming song!

EDITH: The gift of music for your special day.

EDIE: It’s almost too much. Truly. Promise you won’t perform it for anyone but me.

EDITH: Why, Edie, whatever do you mean?

EDIE: Well, “The Girl Who Has Everything?” Honestly! What would people think! (Pg 8) (Edie speaks to the audience) She stopped my cotillion cold and performed all three arias from Faust. My graduation tea . . Carmen with a rose in her teeth. My birthday . . . she danced Salome! Wouldn’t it be an odd thing if – on your death certificate – it actually said that you died of shame? (Pg 16-17) (She notices a recital brochure on top of the piano)

EDIE: (holding it up) Why, Mother Darling, what’s this?

EDITH: Oh dear. You weren’t supposed to see that. It was meant to be a surprise – (She takes the brochure and admires it) (Pg 9) A musical recital in honor of Miss Edith Bouvier Beal and Mr. Joseph Patrick Kennedy, Jr. the 12th of July, 1941!

EDIE: You’re planning to sing?

EDITH: (Pg 18) Who knows if we’ll ever have another party?

EDIE: It’s just that Joe’s parents are coming, and they’re so terribly New England. I don’t expect they listen to music at all.

EDITH: Nonsense! I’m sure they’d be delighted. (Both characters overlapping)

EDIE: (Pg 19) Decorum, Mother, that’s all I ask! . . .

EDITH: Decorum? Oh, that’s rich! You’re a fine one to lecture me about propriety!

EDIE: When she doesn’t get exactly what she wants, she positively spits venom!

EDITH: Wearing lipstick to school- “temptation red” - at only thirteen; the whole town was talking!

EDIE: Pish posh, mother! You’ll say anything to be a dramatic, anything to garner attention.

EDITH: This very house was positively blanketed in adolescent shame.

EDIE: (Pg 20) Who’s engagement is this anyway? (Beat, then regretfully) (Pg 39-40) Mother, I-

EDITH: Don’t! (She puts down the brochure quietly on the table, spirit broken)

EDIE: (Edie feels horrible and picks up some sheet music from the piano – softly) Is this [one] on the bill? It’s one of my favorites.

EDITH: (Interrupting) Edie. Please.

EDIE: It’s the very first song you ever taught me. We used to sing it together.
EDIE and EDITH: (Pg 41) (Singing; shared line by line – Edith perks up throughout the song)
WE’RE A BOWL OF PEACHES AND CREAM
THE DODGERS AND BROOKLYN
A PERMANENT TEAM
INDIA AND GANDHI
DAGWOOD AND HIS BLONDIE
TWO PEAS IN A POD

EDITH: (Pg 43) Oh, Edie. I’ve been monstrously selfish. All eyes should be on you, darling. You and Mr. Kennedy. (Edie exits – While Edith entertains the crowd including EDIE’s fiancée with a story) (Pg 50) Exquisite diver, our Edie . . . Her swimming costume clung to her like skin on a peach. Well, she went sailing into the water . . . and the seams split. Well, a lesser girl would’ve shrieked and run for cover. But not Edie! She swam the length of the pool. Twice! And when she climbed out, Mr. Kennedy, no one offered her even a towel. Edie walked right past them! She became the most talked about girl in town!

EDIE: (to audience - horrified) (Pg 52) What? No! She didn’t . . . she wouldn’t!

TRANSITION

ACTRESS 1: From 1947 to 1952 Little Edie lived in New York City, hoping to land her “big break” in show business.

ACTRESS 2: Max Gordon, the successful Broadway producer, saw potential in Edie and invited her to audition for the Theatre Guild. But it was not to be.

ACTRESS 1: In 1952, her mother called on Little Edie to return home. Her health was poor and she needed someone to take care of her.

ACTRESS 2: For the next two decades, Edie and her mother lived in a fantasy world of their own creation. Re-living the past and ignoring the squalor.

EDIE: (she speaks to the audience as she is feeding a hoard of cats) (Pg 79) I think the saddest thing was my not marrying. I missed out on everything . . .

EDITH: (Pg 83) Edieee!!!!

EDIE: I’m feeding the cats!! . . . (to herself) When am I going to get OUT of here??

EDITH: (Pg 84) EDIEEEE! (Pg 102) You know what I’d like? Some music. I’m happier when I’m singing than anything I’ve ever done since I was born. See if you can find . . . that song. The one I just adore . . .

EDIE: Oh, sure. (bitterly) “The Girl Who has Everything”

EDITH: No, heaven’s no . . . the flipside (Edith sings mean-spiritedly)

(Pg 80) IS IT MY FAULT THAT
YOUR CAKE FELL FLAT?
THAT YOU’RE UNMARRIED
BALD AND FAT?
AS THE WORLD WALTZED BY
AND EDIE SAT . . . .

EDIE: (Pg 80) Sometimes I think I have the saddest life . . .

EDITH: (Pg 128) Oh, Edie! Wouldn’t you like a cup of soup? With some oyster crackers? Wouldn’t it be too divine? Have a cup of soup with your mother won’t you?

EDIE: Which would you like, Mother Darling? The cream of tomato or the bisque?

EDITH: You choose.

(Edie notices the old record player and crosses to it, raises the lid, flips the record over and drops the arm. She then turns to her mother. She sways to the music and sings with a recording of her younger self)

EDIE: Will youuuu? (Pg 112) The last time I performed this song . . . when was it?

EDIE and EDITH TOGEHER: Will youuuuu? (Edith stops singing. She looks at Edie disapproving)

EDITH: You’re singing it incorrectly. Very ugly.

EDIE: Will youuuuuu?

EDITH: (pg 113) That’s not it! You’re waaaaay off. Go to the bottom of the class! Everything is perfectly disgusting on account of you! Bring me my radio? I have got to have some professional music!

EDIE: (Edie deliberately yanks the needle across the record, scratching it. The music stops) I stood for you all these years.

EDITH: Well, of course you did! You’d no place else to go –

EDIE: Not true! I was going to the White House! (Edith shakes her head) I was! With Mr. Joseph Patrick Kennedy.

EDITH: (Pg 114) Pick up a fresh paper: that’s yesterday’s news!

EDIE: He was keen for me, but you got rid of him because he came from a celebrated family.

EDITH: That’s the way! Pin it all on Mama!

EDIE: You got rid of him in fifteen minutes flat

EDITH: You did all that by yourself

EDIE: (To audience) She’s very mean to me!

EDITH: (Pg 115) I didn’t want my child to be taken from me! I’d be entirely alone!

EDIE: (Pg 116-118) I took care of you! I took care of this damn house for twenty-five years!

EDITH: You didn’t have to! After [your father] got his Mexican divorce, I wanted him to come home -- back to Grey Gardens! (Following lines are spoken over one another as each focuses on their narrative)

EDIE: As long as my father was alive –

EDITH: So we could be a family again, like other families

EDIE: He wanted to ruin my life!

EDITH: But Edie said “No”

EDIE: I was scared to death of him-

EDITH: She said she’d “leave the house forever”

EDIE: I didn’t want him here – screaming at me all the time: Take off that lipstick

EDITH: If Mr. Beale ever came back to Grey Gardens!

EDIE: Wash off that perfume

EDITH: She actually threatened to run away

EDIE: How dare you wear high heels

EDITH: If my husband - her father - came back!

EDIE: I didn’t need the humiliation

EDITH: Tell the truth, Edie

EDIE: I knew if [he] came back, I’d never get married!

EDITH: That’s not the reason!

EDIE: I’d never find a man!

EDITH: That’s not it at all!

EDIE: Mother please!

EDITH: (angrily warning) Edie! (delicately now) You needed to come home . . .

EDIE: (Steely and silent. Too much has been said. She plucks the radio up and takes it to her mother. Her voice is strained) Your radio, Mother Darling. (Edie exits)

EDIE: (Pg 123) (In the front yard, she stops at the garden gate)
Sings:
NEW WORLD AWAIT
JUST FLIP THE LATCH
AND THROUGH THE GATE
GO THROUGH THE GATE
THE GARDEN GATE
MY MOTHER’S GATE

(She stands, frozen. Try as she might, she cannot bring herself to flip the gate latch)

EDITH: (Pg 127) (As Edie stands mute and silent, from upstairs, we hear the familiar cry) Edie! What have you done? Where have you gone? (The call cuts through EDIE like a knife, but she does her damnedest to ignore it) I’m all alone! Edie! The radio; it’s gone dead. (Edie shudders in the evening air) Edie! I’m starving! I want my supper. I need your help!

EDIE: (A sigh of resignation and then) Coming, Mother Darling!
```

---

## IC-0591: Gwen and Gwen

- Title: Gwen and Gwen
- Author (byline): Nancy Kiefer
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: April 2017
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GWEN, GWEN II, MOTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 2067
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nancy Kiefer
ISBN: 978-0573630408
Publisher: Samuel French, Inc.
Date (Month/Year): April 2017
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: The voice . . . HER voice was back. Stronger than ever. And now Gwen not only could hear her . . . she could see her too.

ACTRESS 2: Life is often hard, but it’s even harder when you are battling a mental illness.

TOGETHER: Gwen and Gwen by Nancy Kiefer
```

### Performance text (classify this)

```text
Suggested Roles -- Actress 1: Gwen Actress 2: Gwen II and Mother

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Gwen stands in the center of the room, very nervous and waiting expectantly for something; phone rings; she takes the receiver off the hook, but it continues to ring. She grabs a broom to frantically sweep the floor. A pounding at the door; she looks at her watch)

GWEN: (Pg 15-17) Seven o’clock . . . seven o’clock . . . Estelle’ll call at nine . . . at nine. (Faces the door directly) I got nothing to say to you! I got my own apartment now! You’d just make fun of it, but it’s mine! And a job! A job you’d laugh at, but I got a job! (Pounding continues; phone begins to ring again) And I got a friend! Estelle is my friend, and you can say anything you want, but she’s my friend! And I’m gonna get my kids back, too! You can pound on the door and let the phone ring all night, but I won’t talk to you! I won’t!

(pounding on the door and the phone ringing stop; the door suddenly bursts open. Gwen II is standing in the doorway, annoyed. She enters the apartment and slams the door behind her)

GWEN II: What’s with you, Gweny? Don’t you believe in answering your phone anymore? Your neighbors aren’t going to appreciate it if you let your goddam phone ring all the time. They’ll report you and you’ll get your ass thrown out. Besides . . . what if it was him? What if he was trying to call you?

GWEN: (Weakly) . . . please . . . please go away.

GWEN II: Like hell! I need a home just as much as you do! You know what you are, Gwen? You are inconsiderate. You found a home for your kids. You found a padded cell for yourself to hide in. What about me, huh?

GWEN: I was not in a padded cell. I was in a group home.

GWEN II: (critically surveys the room) What a crummy dump this is. You’re in big trouble, Gweny.

(Looks at Gwen for a long time)

GWEN II: (Pg 17-18) You’re looking well, Gwen. Certainly better than when we parted company a year ago. So how’s the kids? They been split up and put into foster homes yet?

GWEN: Get out of here! This is my apartment.

GWEN II: Tell me about this Estelle woman.

GWEN: She was my social worker at the home. And she’s . . . she’s my friend.

GWEN II: If they took her paycheck away, would she still come around? Would she still be your friend? Let’s get her fired and find out.

GWEN: She’s going to call me at nine.

GWEN II: So what? Is that supposed to intimidate me? Am I supposed to be scared or something (Laughs) (Pg 20-21) So what happened to that broad who was supposed to move in here with you? How come she didn’t, huh?

GWEN: Billie . . . her name was Billie. She was . . . sad. She couldn’t take care of her children. Billie had to go back to the hospital. She had a relapse. But before that we shared a room in the group home. We talked a lot . . . watched television at night.

GWEN II: (cuts her off) Sounds like a real drag. Two losers who deserted their kids sittin’ around watchin’ the idiot tube and poppin’ antidepressants.

GWEN: You haven’t changed a bit, have you?

GWEN II: (Intensely) Did you really think you could put me in permanent cold storage, Gwen? That a few months in a padded cell with some soggy social worker tellin’ you that you’re really not a *screw*-up would get rid of me? (menacing whisper) All I did was wait . . . I just waited. (Gwen laughs nervously) (Pg 22) (threateningly) And don’t laugh at me, or I’ll slap that smile off your ugly face. Don’t laugh at me and don’t abandon me again. (Pg 25) (Hits Gwen across the face) Don’t you ever again pay some jailor to suppress me into nothingness so you can pretend for a few months that you’re sane! (She calms herself)

GWEN: (Pg 23) You are so jealous . . . so jealous!

GWEN II: (Pg 26) Yes, Gwen. I’m jealous . . . of everyone whose parents are kind and wise and who grew up smart and pretty and loved. I’m jealous of every woman he touched, every woman he wanted. (Pg 30) You are the guilt and I am the jealousy. You were always the one who felt certain that every time somebody got shit on, it was your fault. You were the one who took the blame and I was the one who hated. You were the martyr and I was avenger. What a pair, what a team.

GWEN: Get out! Just get out of here! ****** one week later******

GWEN II: (Pg 36-37) (tenses up and looks around the room, sniffing) I smell a rat! Someone’s coming.

GWEN: (Panicky) My mother?! My mother?! I don’t want to see her! I don’t want to talk to her! What should I do? (firm knock on the door) Go away! Go into the bathroom! Don’t talk to me! (GWEN II complies and exits) (Gwen answers the door) Mom . . . Mom . . . you didn’t call . . . I wasn’t expecting you.

MOTHER: (looks critically around the room) Good lord! (Pg 38-39) I know the rent’s cheap, but really Gwen. There must be rats and roaches here. No matter where we lived, Gwen, I always kept it clean. You’ve been here for over a week. Don’t tell me you haven’t had time to clean.

GWEN: Mom . . . it’s been hard for me. Hard to go back to work. I guess when I come home, I feel . . . I feel . . . depressed.

MOTHER: (Starting to clean) Everybody gets depressed, Gwen. Do you think you’re the only person? Besides, I thought that year you spent in that . . . home was supposed to make you well again. Your sister took your children in for an entire year!

GWEN: (Pg 40-41) I know I’ve been a big inconvenience to everyone, Mom. (Pg 41) I never expected Kathleen to take care of the kids forever.

MOTHER: Well, I should hope not. You had them, Gwen. You married a man I begged you not to marry and had children with him. I warned you he’d never support you. You wouldn’t listen, and now those children are your responsibility. Not your sister’s and certainly not mine.

GWEN: I can change . . .

MOTHER: . . . I hope so, Gwen. Men have affairs and leave their wives all the time. Life has to go on. I have never been able to understand why you allowed yourself to fall to pieces like you did.

GWEN: Mom . . . Mom . . I guess . . it was more than that. (starts to cry)

MOTHER: (Pg 42-43) (stops cleaning and looks critically and unsympathetically at GWEN) Snap out of it, Gwen. I did not come here to listen to you whine.

GWEN: I’m sorry. I’ve just . . .just got a lot of problems, Mom.

MOTHER: Well don’t blame them on me. You can’t go through life blaming other people for your problems, Gwen. At some point you have to take responsibility and shape up – or ship out.

GWEN: You’re right . . . you’re right (trying to stop crying) I’m grateful for everything you’ve done for me.

MOTHER: You’ve had your year of relaxation! Now it’s time to get back to work.

GWEN: (Astonished) I wasn’t relaxing, Mom. (Confused) Mom . . . Exactly what do you want me to do?

MOTHER: (Pg 44) I want you to stop thinking about yourself, Gwen. Think of your children. They are far more important than you . . . You were always look[ing] for attention. I think you’ve had enough for one year, don’t you? Your sister’s divorced and she’s been jilted by men, but she didn’t abandon her children. (a long beat)

GWEN: (Pg 45) (obviously fighting to remain civil) Mom . . . you getter go home. Dad might need you. I can finish this.

MOTHER: (Relieved Mother grabs her coats and prepares to leave) But will you? (Smiles coldly at her) I didn’t raise my children to live in pig pens. (Exits)

GWEN II: (explodes out of the bathroom) Get outta here, you bitch!!! (to Gwen) Just because there’s some obscure code of human ethics that says you’re supposed to feel gratitude towards your parents, you don’t have to go along with it! Name one thing she ever did for you! I hate her! Parenting skills of a f***** rattlesnake. People like her shouldn’t be allowed to breed.

GWEN: (Pg 47) I’m not like you . . . I can’t talk like you. (Pg 48-49) (repeating a litany she’s clearly said over and over) My mother is kind. She is thoughtful and caring. I’m not going to let you destroy the progress I made.

GWEN II: Progress? Look around you, Gweny. Look at this mess. Does this look like the home of a woman who’s made progress?

GWEN: (looks around her and then closes her eyes) . . . yes. Because all it means is that I’m out of the group home and on my own.. It doesn’t matter what the place looks like.

GWEN II: Where are your kids? You haven’t got the guts to call them! You still can’t stand up to your mother. You call that progress? (Pg 50) I get [so] tired of you, Gwen. I get tired of what a spineless, uninteresting loser you are! (to herself) Damn her. Damn her to hell!

GWEN: (Pg 51) (softly to herself, overlapping Gwen II’s last line) . . . and I’m going to get them back just as soon as I can . . .just as soon as I can . . . just as soon . . . (Pg 56) I want to see them . . . I do . . . [but] I don’t want them to see me like this.

***** one month later *****

GWEN II: (Pg 59) You’re stupid and you’re also a pathological liar!

GWEN: (Pg 60) Why do you talk like that?

GWEN II: I beg your pardon. I don’t talk like that. You talk like that. If somebody walked in here right now, who would they see? Just you, sittin’ around talkin’ to yourself. You’re becoming dysfunctional.

GWEN: (Angrily) Alright! Alright! And why am I dysfunctional? Does it have anything to do with your existence?

GWEN II: I come in when you let me in. I come in when you hate yourself and when your guilt is eating you up like a cancer. I’m all that’s left of your dreams. I’m the only one who can help you. (Pg 61-62) Did you ever read your chart in the nut house?

GWEN: No, they didn’t let us . . . why?

GWEN II: Well, I did. . . A serious personality disorder due to critically low feelings of self-worth who is potentially homicidal. (she looks dangerous)

GWEN: (Frightened) What’s that supposed to mean?

GWEN II: It means that son of a bitch who dumped us and got married to Miss Mummy Face with her CPA and her Volvo is finally, finally going to care about us when I point a gun in his stinking face!

GWEN: (Terrified) No . . . I couldn’t kill anybody . . . not anybody! (changing the subject) I want you to tell me why I don’t want to see my kids.

GWEN II: (Pg 63-64) You don’t want to see your kids, Gwen, because you hate your kids. You convinced yourself that he dumped you because of the kids. He was never a family man. You knew that. You got yourself knocked up twice, thinking that would make him stay with you, but it didn’t!

GWEN: (with increasing rage) . . . get out . . . get out of my house! Get out of my house!

GWEN II: Remember what you did that night you called him and she answered?

GWEN: I cried myself to sleep.

GWEN II: (Scoffs) You slapped the girl across the face, told her it was all her fault that he left you, and you didn’t feed either one of ‘em for three days. The girl went to school bruised and wearing dirty clothes. The boy sat in a corner and cried while you laid in bed in a drunken stupor, moaning over the fact that stupid asshole left you. The school called the county child abuse authorities and next stop, Estelle’s nut house!

GWEN: (Pg 65) I do not hate my children!

GWEN II: (Pg 68) (dismissively) Get hold of yourself, Gweny. We need to think of something to do for entertainment this evening. Um . . . I know! Let’s tell each other secrets.

GWEN: I don’t have any secrets.

GWEN II: True. But I’ve got a few. They’re just oozing out of me. (She goes to the bed and reaches in between the mattress and pulls out a handgun.) Secret number one. (waves the gun in Gwen’s face) Remember this?

GWEN: (backs away in fear) No!

GWEN II: Sure you do. Last month? Meeting at the nut house. Sneak upstairs afterwards hopin’ that crazy Billie forgot to take her gun from beneath the floorboards. Well she forgot! (Pg 74-76) (forcing the gun into Gwen’s hands.)

GWEN: (Starts to cry) . . . I’m . . . I’m afraid . . . of you.

GWEN II: (Grabs Gwen’s hands and tries to get her to aim the gun at her head) Do it! Get it over with!

GWEN: (Struggling) No!

GWEN II: You’re a loser, Gwen, A Loser. He’s gone. He’s married . . .and he ain’t ever gonna call you again. Do it, Gwen. Put a dignified end to this . . this joke . . . this farce we’ve become.

GWEN: (in a very weak voice that begins to gain strength as she speaks) . . . things can change . . . people can make things change . . . we . . . we can reunite.

GWEN II: It takes a powerful chop to cut a person in two like this, but when it happens, there’s no point in going on.

GWEN: . . . people still fall in love . . . people still fall in love . . .

GWEN II: But not people like you . . . not people like us. (Gwen slowly raises the gun and points it at Gwen II. She shoots her) Now you’ve only got one bullet left. . . don’t miss. Embed it in what’s left of your brain. I’ll survive for a short time after you’re gone. I shall speak the last word. (Pg 77) A name . . . what’s the last name you want me to say, Gwen?

GWEN: (In control now . . . a long beat) Alright. Say your children’s names!

GWEN II: (turns away defiantly) I don’t have any children.

GWEN: (Pg 78) You are a woman with two children, a son and a daughter. (She tosses the gun on the bed and commands) Say their names!

GWEN II: Say them yourself.

GWEN: (Pg 79-80) Say YOUR name . . . SAY IT!

GWEN II: (battling to stay in control she forces out the words) I am Gwen Kessler. I just got out of the nut house. My life has been an abysmal failure and I possess no foreseeable future. I am angry. I abused and neglected my children. I have a gun with one bullet in it . . .

GWEN: (Shoves her away) I am Gwen Kessler . . . and I have two children . . . Diane and David (Pg 82) I’m going to call my children!

GWEN II: (Pg 83) (Desperately trying to maintain control) You abandoned them! They hate you! You said it was their fault he left you! You wished you never had them!

GWEN: (with conviction) My children love me . . .and I’m going to call them.

GWEN II: (weakly) But what will we say? We hurt them! What will we say?

GWEN: (with strength as GWEN II fades) . . . we’ll say their names (Picks up the phone and begins to dial)
```

---

## IC-0592: Haiku

- Title: Haiku
- Author (byline): Katherine Snodgrass
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 1989
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS 1, NELL, LOUISE, BILLIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1960
- Already set (do not supply): none

### Source block (context only)

```text
Author: Katherine Snodgrass
ISBN: 978-0573632549
Publisher: Samuel French, Inc.
Date (Month/Year): 1989
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: A haiku is a short poem that expresses a single feeling or impression and typically contains three unrhymed lines of five, seven, and five syllables.

ACTRESS 2 (as Lulu): (in a sing-song voice, rocking and flapping) May not have the words / to share my experience / Understand me still

ACTRESS 1: See . . . that was a haiku . . . In this selection, haikus becomes a bridge between a severely mentally handicapped daughter and her mother -- A way for Lulu to make a connection with reality and release the artist trapped inside her damaged mind.

ACTRESS 2 (as Lulu): (in a sing-song voice, rocking and flapping) May not have the words / to share my experience / Understand me still

ACTRESS 1: If only they can convince Lulu’s sister, Bebe, that it’s true

TOGETHER: Haiku by Katherine Snodgrass
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested character assignments:

ACTRESS 1: Nell (50’s mother to Billie and Louise) / ACTRESS 2: Billie (Bebe) and Louise

(Lulu) – Both in their late 20s to early 30s

Scene opens with Louise rocking and flapping her hands. She is lost in her own mentally disabled word. Nell begins speaking . . . almost to herself rather than to Louise.

NELL: You were born in early winter. A breech baby. You tried to back into the world. I remember, the doctor had to pull you out. It was night when they finally brought you to me.

LOUISE: (still rocking and flapping – in a sing-song voice) November evening. / Blackbirds scull across the moon. / My breath warms my hands. (Nell write down Louise’s haiku, then check what she has written holding the paper two inches from her eyes)

NELL: John said you were too beautiful to live. It was true. You and Bebe together, you were like china dolls. Delicate, perfect. And then . . . I sensed it that day when I saw you through the window. Billie was on the swingset, and you were there. Outside. You were so quiet. You’d stared before, of course . . . as all children do. But this time, you were . . . different. I had to get down on my knees beside you. I touched your hair and then your face. . . Funny, I don’t remember being afraid.

LOUISE: (less rocking and flapping –sing-song voice is dying out to be replaced with a normal tone) Chainmetal swings clanging / In the empty schoolyard. / Silent summer rain.

(Nell writes down this haiku and goes through the same process as before) (in a normal voice – Louise is fully present) Tell me again about John. You haven’t talked about John in a long time.

NELL: John. All right then. John was tall and thin like Icabod Crane, only not so scared.

LOUISE: John wasn’t scared of anything. And [he] would rub Bebe’s back until she went to sleep. He smelled of soap and something . . . sweet?

NELL: (Drily) Sweet! Cigars. From Havana.

LOUISE: (retreating into her own world again as she repeats with Nell’s exact inflection – beginning to rock) Cigars. From Havana.

NELL: (Looks at her sharply) Let’s stop now. I think I should give you your medicine.

LOUISE: (struggles to stop rocking and maintain her connection - normal voice again) I’m not ready to go back. Please, not yet. I want to do more.

NELL: We’ve got to be careful.

LOUISE: (haltingly – she is clearly battling to maintain her clarity) But I can do it! I promise. Please, Momma, It’s like being smothered. Everything is so dim, and I can’t hear you properly. Or see you or touch you or . . . (Louise sees a bruise on Nell’s arm) Did I do that?

NELL: It’s not bad. (Nell touches the bandage on Louise’s forehead) Does this still hurt?

LOUISE: That was before, before I knew what to do. I can stop it, I know I can. I need to practice, you said so yourself. (beginning to rock and flap as she become more distressed)

NELL: Yes, I know what I said, but . . .

LOUISE: Let me see Bebe first.

NELL: Billie! My God, what time is it?

LOUISE: (Repeating) My God, what time is it? (Nell fishes in her pocket for a bottle of pills, urgently)

NELL: She’ll be here any minute. Sit quietly. You know we can’t wait too long. You’ll hurt yourself.

LOUISE: (sing-song voice) You’ll hurt yourself. (again pulls herself back) I mean no, I won’t and you promised I could talk to Bebe. You said I had to talk to her this time. That we could show her.

NELL: We will, we will. But she’ll be here any moment. (Holding out pills) I want you to take this now. (Louise retreats into her world and begins to rock and flap in ernest)

(Billie enters in a whirlwind)

BILLIE: Whew, I made it. (To Nell, ignoring Louise) How are you? You look exhausted. I knew you’d be surprised. Oh, and look what I found in a little shop in Boston. They had all three of your books, is that unbelievable? I brought something for Lulu, too. (Billing brings out a package from her bag and hands it to Nell.)

NELL: You did? Why, that was thoughtful. It’s wrapped so prettily, why don’t you let Lulu open it?

BILLIE: (Laughing nervously) Do we have time before dinner?

NELL: Billie.

BILLIE: I’m sorry. It’s just that she’ll like the wrapping paper better than the music box. (Crosses to Lulu) My God, what happened to her forehead? Is she banging her had again?

NELL: No, no, of course not. We just had a little accident.

BILLIE: Isn’t the medicine working? (Noticing Nell’s bruise) Did you get that bruise at the same time?

NELL: (Lying) Oh, this? This is nothing. I don’t even remember where it got it.

LOUISE: (Holding up her hands for a hug) Bebe.

BILLIE: God lord. Lulu, my love, you amaze me. (Louise and Billie hug)

NELL: She’s different than when you saw her last, isn’t she?

BILLIE: Because she hugged me? At least the medicine is doing that for her.

NELL: But don’t you think she’s really getting better thought? Honestly, look at her. Isn’t she more alert? She knew you, Billie. She wanted to touch you.

BILLIE: (Laughing) Mother. No! (to Louise) You never change, do you? (To Nell) No, I don’t see any difference, no, she’s not more alert, and no, she’s not getting any better.

NELL: You don’t understand. You can’t possibly know, you don’t see her every day. (long beat) I’m glad you’re here, Billie. I’m glad you came. I’ve been wanting to talk to you, but I haven’t had the courage until now. (silence, then frustrated) It’s my eyes.

BILLIE: Yes. That’s why I’m here. Doctor Dave called me. Don’t look so horrified. What did you expect him to do? Ignore it? (beat) What are we going to do? Will Daddy’s trust fund cover a nurse for Lulu?

NELL: No, and even if it would, I don’t want some stranger in my house caring for Lulu. I’ll do it myself.

BILLIE: How? How will you measure her medicine? What if she dirties her clothes? What if she has a reaction to the medicine? What if you were to fall, what would happen to Lulu? She couldn’t help you. She wouldn’t know what to do. Why, she wouldn’t even understand that anything was wrong.

NELL: I do not have to have someone here. I’ve managed this long. Besides . . . Lulu understands more than you know. Billie . . . I don’t write the haikus . . . Louise does . . .

BILLIE: That’s impossible

NELL: I swear it. It started two years ago. Right after we changed to that new medication. I was reading and Lulu was sitting next to the window and suddenly I realized that I’d forgotten to give her her pill. She turned to me and looked at me . . . really looked at me for the first time.

LOUISE: Mama? Do you forgive me Mama? Don’t mean to hurt you, but I get so scared as if . . . I get trapped, Mama. I try and I try, but I’m moving so slowly. I can’t tell you . . . (she gets stuck and there’s a growing panic to her voice and her demeanor – gradually increase of rocking and flailing) I can’t . . . I can’t . . . I can’t!

NELL: I had to give her her medicine then, but Louise had been there! She was so frightened. And then I remembered . . . The medicine . . . on that day it was late. So on the third day, again, I held back the pill, and again she was Louise!

BILLIE: This happened two years ago? Why didn’t you tell me? And the poetry?

NELL: It was October, just about dusk . . . I said to her “Concentrate, Lulu, you can stay if you want to. Look how beautiful the colors are . . (sing-song) Autumn evening:

LOUISE: (with same sing-song inflection - rocking) Autumn evening . . .

NELL: (sing-song) Woodsmoke

LOUISE: (imitate) Woodsmoke . .

NELL: (sing-song) Curling up wood . . .

LOUISE: (imitate) Curling up wood . . . (then finish without sing-song as the rocking and flapping ceases) swallows circle . . . . overhead.

NELL: She had finished it for me, you see. A Haiku. After that Lulu began making them up all on her own. Now I simply sit and talk and she creates. Billie, it’s as if she sees my thoughts, my innermost feelings, and then she translates them into images.

BILLIE: I thought they were yours.

NELL: I know you did. But no, I’m only the catalyst.

BILLIE: Catalyst. Is this every day? (Nell shakes her head) How long does it last?

NELL: Half an hour at the most. But she’s trying very hard. She wants to practice. She wants to be . . .

BILLIE: . . . Normal?

NELL: No. More than that. She wants to be extraordinary. And she is.

BILLIE: Mother, if this is true . . .

NELL: If . . . ?

BILLIE: I mean, when this happens . . . Why haven’t you told Dr. Dave about it?

NELL: No doctors and no more hospitals. They brought on this problem in the first place. If I hadn’t rushed her to the doctors so quickly, maybe she would have come out of it. If they didn’t have her taking all these drugs . . . Nobody knows what might have happened!

BILLIE: If that’s what you believe, take her off the drugs. We could put her in the hospital and have the drug levels monitored.

NELL: No. I told you, no hospitals.

BILLIE: But they could wean her off the drugs slowly, and then we could . . (Nell is shaking her head) Why not? Why not?

NELL: She needs the drugs. She’s not herself yet, so she needs them to . . . to protect her until . . .

BILLIE: What do you mean, protect her from what?

NELL: I told her you wouldn’t understand. I warned her, but she wanted me to tell you. She said we had to tell you.

BILLIE: I don’t believe it . . . .

(Flashback to BILLIE AND LULU as teens – Billie is teaching Louise about makeup.)

BILLIE: (To imaginary mirror) Now then, we need this, and this, and this. Okay, now you take the lipstick and you put in on like . . . that. See? Okay. Pucker up. (Billie puckers and Louise imitates her as Billie applies lipstick to Louise’s mouth then to her own) M-m-m-, luscious pink! Now then, you take this pencil. And don’t put it in your eye!

LOUISE: (Sing-song with lots of rocking and flapping) Don’t put it in your eye!

BILLIE: (To mirror, applying makeup to herself) You draw around the eye . . . underneath . . . above . . . but not too much. There. See?

LOUISE: (Sing-song with lots of rocking and flapping) Don’t put it in your eye!

BILLIE: Right. And now for the shadow. What color shall we use? Let’s use turquoise, or what about this purple? Yeah, let’s use the purple.

LOUISE: Yeah, let’s use the purple! (Billie puts it on for the mirror while Louise picks up turquoise and draws circles over her face, her cheeks and above her eyes).

BILLIE: Now, then, what’s next?

LOUISE: Now, then, what’s next? (Billie looks at Louise, whose face is covered with makeup) Oh, you!

NELL: (Enters) Billie, how could you! I thought you knew better than this. What were you thinking? Oh, Lulu, such a mess. It’ll take days for these colors to wear off. Why on earth? Here, hold her hands while I clean off this mess. For the final time, do not take it upon yourself to teach her. You leave that to me, or you can leave this house. Do you understand? (Billie runs off stage) I have no time to clean up after the both of you. Look at this, just look at it! Lulu, be still! Billie!

(End Flashback)

BILLIE: What do you want me to do?

NELL: I want for you, I need for you to write down the poems. To listen to her and believe in her so that she can be . . . who she is. The doctors don’t understand. The illness is still in control, so it’s only sheer will power that allows her to get out at all. If you don’t believe me, let me show you . . . . You can talk to her. We can help her, I know it. Louise? (There is no sign from Louise) Louise. (Louise still does not respond)

BILLIE: She doesn’t hear you.

NELL: Billie’s here, and you wanted to talk to her. Remember? (Nell turns Louise’s head toward Billie) You see? There. Now, Bebe, say something to her. Go on.

BILLIE: (Hesitantly) Lulu. It’s Billie.

LOUISE: Bebe.

BILLIE: Yes. Is it really you?

LOUISE: Is it really you?

BILLIE: I mean, is it true?

LOUISE: True?

BILLIE: (Trying again after looking at Nell for encouragement) It’s been a long time since I’ve seen you, Lulu. How . . . How are you?

LOUISE: How are you?

BILLIE: I’ve been fine, but how are you?

LOUISE: I’ve been fine.

BILLIE: (Giving up) She’s just repeating, Mother . . . No, no, say something else. Say anything else. Make up a poem. Can you do that for me, Lulu? Make up a poem. Please do that. (To Nell) What if I point out the window, will that help? (To Louise) Look, look out there. Winter’s nearly over. Mr. Turner’s daffodils are in bloom see?

NELL: Keep going, she’s listening.

BILLIE: One gray cloud lies just . . . over the trees across the southwest.

LOUISE: Over the trees one gray cloud lies . . .

BILLIE: She’s mimicking me.

LOUISE: . . . in my sister’s eyes.

NELL: There! Bravo, Lulu! Good girl! (Nell turns to Billie and sees her face) What.

BILLIE: She’s repeating. She says nursery rhymes with the same rhythm. She’s repeating what I say and what you say.

NELL: No. Louise? Help me now. We’ve got to make Bebe understand. Louise? Try just a little harder, baby. Concentrate now.

BILLIE: Please, please don’t! I’m asking you to stop.

NELL: Louise, answer me. Look at me and answer.

BILLIE: (Shouting) Mother stop! (Louise is startled by the shout and begins screaming and banging her head against her chair) Where is her medicine?

NELL: On the desk. Get the water. (Billie instead crosses to where she has put the music box and opens it for Louise to see. Louise immediately stops the banging and screaming and focuses on the music. Billie brings the pill and water glass to Nell) Now take this, Lulu. There. (Louise takes the pill calmly, fascinated with the music box).

BILLIE: Is this what always happens?

NELL: No, but sometimes we wait too long . . . I hate so to see her leave. (Beat) I know what you’re going to say. But every word I’ve told you is true. You heard it, but you didn’t want to believe.

BILLIE: That’s not true. I want to believe. Just don’t ask me to see something that isn’t’ there. Momma, I’m sorry, but I’ve tried before. I can’t keep trying and have it not be . . . not be true. It hurts too much. You talk to her as if . . .

NELL: . . . as if she’s real, as if she’s a person. And she is. Let me try tomorrow . . . I’m only asking you to let me try. Wait and see. You’ll do that, won’t you? Just that? For me?

BILLIE: (resigned and defeated) Yes, Momma. I think I can do that. (Billie crosses to the window and stands, looking out) I wish Daddy could be here. (Exits scene)

LOUISE: (alone on stage) Walking in his garden / Suddenly in the twilight / White hydrangea
```

---

## IC-0593: Harriet Tubman Visits a Therapist

- Title: Harriet Tubman Visits a Therapist
- Author (byline): Carolyn Gage
- Work: Under Thirty: Plays for a New Generation
- Publisher: Vintage Books
- Publication date as stated: Oct 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: HARRIET, THERAPIST
- Teaser before the introduction: No
- Spoken words (computed): 2034
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carolyn Gage
Book: Under Thirty: Plays for a New Generation
ISBN: 978-1400076161
Publisher: Vintage Books
Date (Month/Year): Oct 2004
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Harriet Tubman, suspected of planning an escape on the Underground Railroad, has been sent to the Therapist for an evaluation.

ACTRESS 2: The Therapist, another African American woman, warns Harriet about the dangers of radical action

ACTRESS 1: Two women who share the same oppression, but whose definitions of survival are in direct conflict . . .

TOGETHER: Harriet Tubman Visits a Therapist by Carolyn Gage

(At Rise: The THERAPIST is reviewing HARRIET's file. She is a ligh-tskinned African American woman who wears the clothing of a contemporary middle-class therapist. There is a soft knock on the door.)

THERAPIST: Come in. (There is another knock, and she crosses to the door and opens it.

HARRIET TUBMAN stands in the doorway. HARRIET's speech and movements

are deliberately slow and dull at first. She stands waiting for orders, head
```

### Performance text (classify this)

```text
bowed.) Come in. Harriet Tubman? You're right on time. (She gestures into the room. HARRIET lifts her eyes briefly. Her face is expressionless. There is a long silence. The THERAPIST sighs and smiles at HARRIET.) Harriet, do you know why you're here?

HARRIET: Massuh Edward done sent me.

THERAPIST: Do you know why?

HARRIET: Cain't sell no nigga like me.

THERAPIST: I don't think that's why. (HARRIET looks down.) I understand why you feel that way. That's a very natural conclusion for a slave to draw. But in this case, I think Mr. Brodas is genuinely concerned about you. I think Mr. Brodas likes you. He speaks about you with a great deal of pride. He's allowed you to choose your own husband, and John Tubman is a free man. That's a very unusual thing for a slaveowner to do. And he lets you hire out to a shipbuilder-

HARRIET: He take alluh money.

THERAPIST: Well, that's not exactly true. I understand that you get to keep what you make over what you owe him. (HARRIET snorts.) I understand you've been able to buy yourself a pair of oxen. That's pretty impressive. You could even buy your freedom someday.

HARRIET: Time I'ze daid.

THERAPIST: (The THERAPIST studies HARRIET for a moment.) You know I share your feelings about slavery. All day long I listen to women tell me stories that make me sick. Stories of rape- raping children, of beating-beating pregnant women, stories of murder, or torture, of live burnings, of babies being sold away from their mothers, of chain gangs ... (HARRIET looks away.) But I'm not going to change it, and neither are you. We can drive ourselves crazy thinking about it. We can kill ourselves fighting it. Or we can make the most of what is possible.

HARRIET: (Eyes down.) Nat Turner. (Looking at the THERAPIST for the first time as she speaks. HARRIET drops the dull-witted act.) Nat Turner. He killed fifty-- seven whitefolks.

THERAPIST: (Taken aback by HARRIET5 intensity.) They hanged Nat Turner.

HARRIET: (Looking at her hands, acting again.) Hanged a man las' week over to Bucktown for stealin' chickens.

THERAPIST: (Losing her temper.) Nat Turner is the reason you can't read. Did you know that? After his uprising, they made it illegal to teach slaves to read or write. After Nat Turner, we couldn't even meet to go to church, unless a white man was the preacher. After Nat Turner, they wouldn't let us talk to each other in the fields, but they wouldn't let us just work either. Oh, no. After Nat Turner, we all had to sing while we worked-oh, except of course, "Go Down, Moses." Now, thanks to Nat Turner, you can die for singing that song.

HARRIET: (Singing.) GO DOWN, MOSES, / WAY DOWN IN EGYPT'S LAND . . .

THERAPIST: You think I'm an Uncle Tom, don't you? You think I sold out.

HARRIET: (Continues singing. Closing her eyes, she raises her voice.) TELL OLE PHARAOH, LET MY PEOPLE GO . . . (HARRIET looks at the THERAPIST, who is silent now.) Didn't hab no gun. Prophet Turner. A sword. Can you see dat? Had hissef a sword! (She laughs.) What he gonna do wid a sword? Slit open de sow's belly?

THERAPIST: Are you thinking of killing someone? (HARRIET looks at her hands. – no response) I'm going to be frank with you. Mr. Brodas has sent you to me, because he's afraid you're going to run away.

HARRIET: (Bursts out laughing.) Oh, he skeered! He tell you dat Harriet bin lookin' mighty greazy. Gonna slip herself th'oo de massuh's han's.

(She laughs again.)

THERAPIST: (Smiling along with the joke.) Your husband seems to think you've been "lookin' mighty greazy," too.

HARRIET: (She stops laughing.) John say dat? He tell you dat?

THERAPIST: He told Mr. Brodas. (HARRIET is stunned.) Harriet, nobody's against you here. Your husband loves you and Mr. Brodas has a great deal of respect for you. But, if you run away, neither one of them is going to be able to save you from the slave catchers-or their dogs. You've got too much to live for to throw your life away like that.

HARRIET: John bin talkin' to Massuh Edward?

THERAPIST: Harriet, I want to help you. You are in a very serious situation. Mr. Brodas has asked me to determine whether or not I think you're going to run. (HARRIET looks at her.) I'm going to tell him that I'd like to see you for a few more visits, but after that, unless there's a change in your attitude, I will have to tell him the truth. I doubt he'll let you hire out after that. (HARRIET says nothing). You're so busy dreaming about a world you don't have, you're missing out on the one right here. Learn to focus on the things you can change, learn to appreciate what you have right now. Little by little, one day at a time, your life will get better. (HARRIET says nothing.) I knew a woman once who decided to run. One night, she took her two daughters - - one was six and the other twelve-and she ran. (HARRIET is keenly interested) They caught her, of course, as they catch most runaways.

HARRIET: How far she git?

THERAPIST: To the Delaware border. (HARRIET nods. The THERAPIST narrates the rest if her story with clinical detachment.) It was the hounds that got her. By the time they called off the dogs, her daughter-the six-year-old-was already dead. And then they took turns raping the twelve-year-old while they made the mother watch. After that, she wouldn't have anything to do with the child. She wouldn't touch her, wouldn't talk to her. She treated her like she didn't exist. Right up until the girl was sold down South. (HARRIET says nothing.) Do you think this woman made a wise decision?

HARRIET: She didn't hab no gun?

THERAPIST: What if she did? She was outnumbered. Or do you think she should have shot her daughters?

HARRIET: (Shrugging.) Lib in de no'th or die in de South.

THERAPIST: You would shoot your own children?

HARRIET: I seen mah sistuhs-Linah and Soph-seen 'em sol' off on de chain gang, an' dat day I wisht dey wuz daid, an' I bin prayin' dey was daid ev'y day aftuh dat, too. Ain't no livin' when dey kin do yo' body any way dey like.

THERAPIST: (Vehement.) Oh, yes, there is! We are so much more than our physical bodies-

HARRIET: (Cutting her off ) Look! Now, you look! (She pulls her shirt out and pulls up the back.) Heah-you look at dat. You look at what de white man done.

THERAPIST: (Turning away.) I've seen plenty of scars.

HARRIET: No, you look, cuz you ain't seen dis 'oman's scars. You therapizin' on me, you look. You stan' up heah, an' you look. (The THERAPIST looks.) You see dat? Dat is a fiel' o' flesh been ploughed by de debil's own han'.

THERAPIST: But you don't have to let it scar your soul.

HARRIET: What you talkin' 'bout? Mah soul? Dis heah is mah soul! Dis black Ashanti skin is mah soul! (She turns to face the THERAPIST. )

THERAPIST: (Becoming very clinical.) And what does it do for you to keep remembering?

HARRIET: (HARRIET starts to respond with anger, but she stops herself. A smile spreads slowly over her face.) You is sleepin' wid de massuh.

THERAPIST: (Hesitating, she chooses her words carefully.) Sometimes Mr. Brodas visits with me. (HARRIET is still smiling.) That doesn't affect my belief that your running away would be suicidal. And it doesn't affect the fact that I want to help you.

HARRIET: (Mumbling.- lowers her eyes) No'm.

THERAPIST: You don't have to put on an act for me. (HARRIET looks up, puzzled.) I know what you're doing. (Silence.) You don't have to please me. (Starting over.) I sleep with Mr. Brodas ... (Hesitating.) He's a kind man.

HARRIET: Oh, yas'm, dat he is. He be de bes' massuh in de world! Dat's des what I allus say, dat Massuh Edward, he-

THERAPIST: (Cutting her off) I hate him . . . I hate him, because he's white, because he's a slaveowner, because he's a drunkard, because he's a coward and a liar, I hate him because he uses women, I hate him because he doesn't bother to wash when he comes to me. I hate him so much, believe it or not, he doesn't bother me. I hate him so much, I don't let him have anything.

HARRIET: He got yo' body.

THERAPIST: I'm not in it. (HARRIET says nothing.) I haven't been in it since I was twelve and I watched the dogs tear my little sister to pieces. I had already left my body before the first white man climbed on top of me. And I wasn't in my body when they raped my mother. I wasn't in my body when they sold me down South. And I wasn't in my body when I had a white man's baby at thirteen. I wasn't in my body when they sold her five years later. And I wasn't in my body when Mr. Brodas made his proposition. I keep myself alive . . .

HARRIET: While you is larnin' de other women to be de slaves.

THERAPIST: I teach them how to survive. I have helped women, Harriet. Maybe not you. But I have helped women. (She pauses. HARRIET says nothing. )You think this is bullshit. (HARRIET says nothing.) How many women could live day to day with your level of rage? You don't have children. What do you think that anger would do to a child? And how long do you think you're going to be able to live like this? Oh, you can make a run for it, all right. But Pennsylvania is a long way off. Do you really think you're going to have the stamina to make it? It takes a cool head to go the distance, and I can tell you right now, Harriet Tubman, you don't have it. Your rage will get you over the county line, maybe. But the Delaware border? Unh-unh. Never.

HARRIET: (The THERAPIST has hit a nerve, and HARRIET reconsiders.) You bin up no'th.

THERAPIST: I was captured.

HARRIET: You bin to Delaware.

THERAPIST: To the border.

HARRIET: Draw me dat map.

THERAPIST: I can't do that. (HARRIET looks at her.) I don't encourage my clients to take reckless chances with their lives.

HARRIET: (Angry) I got two rights-de right to freedom and de right to die.

THERAPIST: (The THERAPIST rises.) I have the right to live.

HARRIET: Libbin'! What you talkin', 'oman? You ain't eben inside yo' own skin!

(HARRIET, enraged, turns to go. She opens the door, but is seized by a fit of narcolepsy. The THERAPIST watches HARRIET for a moment, and then closes the door.)

THERAPIST: You want the map? All right, Harriet Tubman, I'll give you the map ... Harriet, listen to me. We don't have very much time, and I want you to listen and remember. You are standing in the middle of a field. It's the field behind the Brodas plantation. It's nighttime, Harriet, and you are alone. You are leaving tonight. John is asleep in the cabin. Can you see the cabin where John Tubman is sleeping? (Slowly, HARRIET nods.) It's a clear night and the stars are out. Look up, and see if you can see one star that's brighter than the others -- that's the North Star. You're going to keep that in front of this shoulder. (gestures to Harriet’s shoulder) You stay on the edge of the swamp, Harriet. And now the swamp is opening up, widening. And you're over the Choptank River. Follow the Choptank, Harriet, about seventy miles on the Choptank River. (HARRIET nods.) You're very close to the Delaware border now. There's a farm on the other side of the border, the Cowgill farm in Willow Grove, and that's all you need to know, because once you get to the Cowgill farm, they'll take care of you the rest of the way into Pennsylvania. All you have to do is get to the farm. You understand? (HARRIET nods.) And now, I'm going to count backwards from five-

HARRIET: (Breaking through with great effort, but still in a trance.) I see dem! I see dem! De women wid de lights. I see dem in de trees aroun' me. I see dem stretchin' out they han's to me. Dey is callin' my name, an' I am reachin' out my han's to dem -

THERAPIST: There aren't any women with you. You are alone.

HARRIET: No, dat I ain't. Dey is shinin' wid glory, dese black women, an' dey is gonna pull me up offa dat groun', gonna snatch me right 'way fum de han's of de whiteman. Doan matter I forget de way doan matter, 'cuz dese women, dey been heah befo' and dey gonna bring me on acrost. Dey is shinin' an' laughin' an' dey is takin' me by de han' to freedom.

THERAPIST: Harriet, these women don't exist.

HARRIET: Oh, yes, dey do. Dese is de women dat lib so good dey cain't die. Dese is de women fum Africa, de women who pitch deysefs off de ship, rather die dan lib in de chains ob slavery. Dese is de women who kilt dey own chilrun 'fo' dey see dem sol' on de auction block . . . de women who kilt dey massuhs wid dey bare han's, de women dey cain't skeer no mo' cause dey already done do de wors' an' dey still alibe.

Dese is de African women, de Ashanti women. (Smiling in her trance, HARRIET begins to sing, and the THERAPIST talks, over her singing.) GO DOWN, MOSES / WAY DOWN IN EGYPT'S LAND / TELL OLE PHARAOH / LET MY PEOPLE GO.

THERAPIST: Harriet, I'm going to count backwards from five. And when I say "one," you will open your eyes. You will not remember any of this experience. Five ... four ... three ... two ... ONE. (HARRIET opens her eyes, and the two women look at each other. The THERAPIST smiles.) Harriet, I am going to have to recommend to Mr. Brodas that you be removed from your present position and put in the fields to work where there is closer supervision.

HARRIET: Put me in de prison-I'ze gone. All de chains in de wod' cain't keep me now. My freedom ain't in the han's of you or Massuh Edward or eben in mah own han's. (The THERAPIST is busy writing. HARRIET crosses to the door, and looks back. She exits, leaving the THERAPIST standing. Blackout.)
```

---

## IC-0594: Having Our Say: The Delaney Sisters’ First 100 Years

- Title: Having Our Say: The Delaney Sisters’ First 100 Years
- Author (byline): Emily Mann
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: May 1997
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SADIE, BESSIE, BESSIE AND SADIE
- Teaser before the introduction: Yes
- Spoken words (computed): 2731
- Already set (do not supply): none

### Source block (context only)

```text
Author: Emily Mann
ISBN: 978-0822215028
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): May 1997
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Having Our Say:

ACTRESS 2: The Delaney Sisters’ First 100 Years

TOGETHER: by Emily Mann
```

### Performance text (classify this)

```text
Lights come up slowly on Sadie Delany. She stands straight and tall, addressing the audience.

SADIE: Bessie and I have been together since time began, or so it seems. Bessie is my little sister, only she's not so little. She is 101 years old, and I am 103. (Bessie enters.) You know, neither one of us ever married and we've lived together most all of our lives, and probably know each other better than any two human beings on this Earth. After so long, we are in some ways like one person.

BESSIE: How do you do! I'm Dr. Delany. Make yourself comfortable. Stay as long as you like. We won't charge you rent. (Bessie looks to the audience, eyes fiercely penetrating. They both laugh uproariously) Truth is, I never thought I'd see the day when people would be interested in what two old Negro women have to say. Life still surprises me. So maybe the last laugh is on me.

SADIE: You know, Bessie and I were in helping professions - she was a dentist and I was a high school teacher -

BESSIE: so we're not rich, but we get by.

SADIE: Papa always taught us that with every dollar you earn, the first ten cents goes to the Lord . . . The second ten cents -

BESSIE: . . . goes in the bank for hard times . . .

SADIE: And the rest is yours, but you better spend it wisely. Well, it's a good thing we listened because we're living on that

BESSIE and SADIE: (Together.) hard-time money now,

SADIE: and not doing too badly. We have lived in New York for the last seventy-five years, but Raleigh

BESSIE and SADIE: (Together.) will always be home.

BESSIE: Raleigh is where Mama and Papa met, as students at Saint Augustine's School,

SADIE: which was a school for Negroes. They got married in the campus chapel and raised all ten of us children right there at -

BESSIE and SADIE: (Together.) good old "Saint Aug's."

BESSIE: Papa became vice-principal and Mama was the matron, which meant she ran things day-to-day at the school. Our Papa became the first elected Negro bishop of the Episcopal Church, U.S.A.

SADIE: That's a long way for a man who was born a slave on a Georgia plantation, but if you had known Papa, you wouldn't be surprised. He was always improving himself, and he and Mama brought us up to

BESSIE and SADIE: (Together.) reach high.

SADIE: Bessie was what we used to call a "feeling child"; she was sensitive and emotional. She was quick to anger, and very outspoken.

BESSIE: And Sadie was a "mama's child."

SADIE: Yes, I followed my Mama around like a shadow. I always did what I was told. I was calm and agreeable.

BESSIE: She was shy.

SADIE: The way I see it, there's room in the world for both me and Bessie We kind of balance each other out. People learned not to mess with me from Day One.

SADIE: It's a wonder she wasn't lynched.

BESSIE: Well, I almost was, but that's another story. The thing is I know Sadie's going to get into Heaven, but I'm not so sure about me. I'm working on it, but it sure is hard to change.

SADIE: She has trouble with the idea of forgiving and forgetting.

BESSIE: That's right. You see, I can forgive, but I can't seem to forget. And I'm not sure the Lord would approve of that at all. I remember things that happened long, long ago that still make me madder than a hornet. I wish they didn't. Most of the people I'm still mad at are long dead and there are things I can tell you . . . (She stops herself) but Sadie will say, "Now Bessie, of the dead -

BESSIE and SADIE: (Together.) . . . say nothing Evil."

BESSIE: So . . . I try to be good. But the rebby boys tend to stand out, make themselves known. You don't know what a rebby boy is.

SADIE: That's what we call white racist men. It's short for rebel.

BESSIE: I'll tell you, the way those rebby types treat colored folks - well, it just makes me sick. Those rebby types don't give colored folks credit for a thing. They learn early to hate. Why, colored folks built this country, and that is the truth. We were the laborers, honey! We were the backbone of this country (She stops herself) Now, Sadie doesn't get all agitated like this. It's been a little harder for me, partly because I'm darker than she is, and the darker you are, honey, the harder it is. I wish I were more like her but I'm afraid I am a naughty little darky! Ha hal (Bessie laughs.) I know it's not fashionable to use some of the words from our heyday, but that's who I am! And who is going to stop me? Nobody, that's who! Ain't nobody going to censor me, no sir! I'm a hundred-and-one years old and at my age, honey, I can say what I want! The beginning of Jim Crow in North Carolina was the day that everything Changed.

SADIE: We already knew we were second-class citizens but those Jim Crow laws set it in stone.

BESSIE: At that time, many white people didn't think Negroes had souls. They wanted to believe that.

SADIE: And powerful white people were getting more and more nervous with the way colored people, after the Civil War, were beginning to get their piece of the pie.

BESSIE: The pecking order was like this: white men were the most powerful, followed by white women.

SADIE: Colored people were absolutely below them

BESSIE: and if you think it was hard for colored men, honey, colored women were on the bottom. Yes, sir! Colored women took it from all angles! We encountered Jim Crow laws for the first time on a summer Sunday afternoon.

SADIE: We were about five and seven years old at the time. There was a place in Raleigh not just for whites but for the whole city, called Pullen Park. The spring where you got water had a big wooden sign across the middle. (They gesture with their hands.)

BESSIE: On one side, the word "white" was painted,

SADIE: and on the other, the word "colored." What in the world was all this about?

BESSIE: We may have been little children but, honey, we got the message loud and clear.

SADIE: (Laughing.) But when nobody was looking, Bessie took the tin dipper and leaned over and scooped some water from the other side and said, "I'm goin' get me some white water!"

BESSIE: It tasted just the same. (They laugh. A beat.)

SADIE: Yes it did, but I'll tell you how I handled Jim Crow. There was a shoe store in Raleigh called Heller's. The owner was a Jewish man, very nice. If you were colored, you had to go in the back to try on shoes, and the white people sat in the front. It wasn't Mr. Heller's fault; this was the Jim Crow law. I would go in there and say, "Good morning, Mr. Heller, I would like to try on those shoes in the window." And he would say, 'That's fine, Miss Delany, go on and sit in the back." And I would say, "Where, Mr. Heller?" And he would say, "Back there." And I would say, "Back where?" Well, I'd just worry that man to death. Finally, he'd say, 'Just sit anywhere, Miss Delany!" And so I would sit myself down in the white section, and smile.

BESSIE: Lord! I hate when you play dumb like that! (Sadie laughs) Every time I encountered prejudice which was rubbed in my face under Jim Crow - I would feel it down to my core. (Very upset.) The words used to describe us most often were colored, Negro, black, and nigger. I've also been called jiggerboo, pickaninny, coon - you name it, honey. Some of these words are worse than others, and how mean they are depends on who is saying them and why. Personally, I don't use the word black very often to describe myself and my sister. To us, black was a person who was, well, black, and honey, I mean black as your shoe. I'm not black, I'm brown! Actually, the best word to describe me, I think, is colored. I am a colored woman or a Negro woman. Either one is OK. People dislike those words now. Today they use this term African American. It wouldn't occur to us to use that. We prefer to think of ourselves as Americans, that's all!

SADIE: There was an attitude among some Negroes that to be lighter-skinned was more desirable. But it was not something that was even discussed in our household. We were different shades, and it didn't make a bit of difference if you were white, black,

BESSIE and SADIE: (Together.) grizzly, or gray, you were you.

SADIE: Now Mama and Papa tried to protect us when we were small, but we were quite young when we learned colored folks were being murdered.

BESSIE: They were being lynched.

SADIE: Yes - we would hear the teachers talking among themselves about some poor Negro just walking down the side of the road, in the wrong place, at the wrong time.

BESSIE: Those rebby boys would just grab him and hang him from a tree, just for fun.

SADIE: It was like entertainment to those fellas.

BESSIE: The rebby boys would come in the middle of the night, and get him out of his bed and hang him up, in front of his wife and children. Sometimes they'd hang his whole family. Why, there was one story we heard of a pregnant colored woman who was hung from her feet, and they slit her abdomen open and let the fetus fall out -

SADIE: (Quietly overlaps Bessie) Lord have mercy!

BESSIE: and she and her unborn baby just died right there, like that.

SADIE: I don't understand any of this. I sometimes think maybe we were a little too sheltered. Why, I was almost afraid of men, really. I wasn't allowed to go downtown by myself until I was a grown girl and then I was always kind of jittery. You can imagine that when it came time for me to graduate from Saint Aug's, I didn't want to leave. The campus was the only home I'd ever known. But on graduation day, Papa said to me, "Daughter, you are college material. You owe it to your nation, your race, and yourself to go. And if you don't, then shame on you!" Well, it seemed to me that I had no choice but to go on with my schooling. But Papa said to me, to both of us, "Daughters, I have no money, and you mustn't take a scholarship. If you take a scholarship, you will be beholden to the people who gave you the money. You must make your own way." So I started looking for teaching jobs.

BESSIE: When we were teaching, we saw for the first time what life was really like for our people.

SADIE: Yes, Lord.

BESSIE: It made our hearts bleed.

SADIE: I realized I was a child of privilege and I had to share my good fortune. I kept remembering what Papa always said: ''Your mission . . . "

BESSIE and SADIE: (Together.) “. . . is to help somebody."

SADIE: Yes, those words kept me going.

BESSIE: This was just forty-five years after the Surrender, and most of these Negroes were in bad shape, honey. They needed help with the basics.

SADIE: You see, oftentimes, learning to read and write for the children was not the top priority. Teaching people about food preparation - like how to can food - was more important.

BESSIE: A lot of the time what those folks needed was inspiration.

SADIE: Yes, a little encouragement. That goes a long way.

BESSIE: I remember when I left home to teach. I was twenty years old. I'd never been away from home. Papa took me to the train station in Raleigh and I put on a brave front. But when that train pulled away from the station and I looked back and saw my Papa standing there, watching me, I thought I was going to die. I started to sob. I cried so hard that the people from the white car came to the colored car to get a look at this little darky just carrying on! Well, I'm embarrassed to say I created quite a commotion. The conductor came along and said, "What's the matter, did somebody die?" Now what'd he have to go and say that for? It was my girlhood that was dying and I knew it.

SADIE: Well it turned out you were the most exciting thing to happen to Boardman, North Carolina, in about a hundred years. Child, they'd never seen the likes of her! She'd walk through that town and the colored men would just stop and stare. They wouldn't say a word, they'd just take off their hats when she walked by.

BESSIE: (Laughs.) One time, I turned and said, 'Just what are you looking at?" They didn't answer. Finally, one of them said, "Why Miss Delany, we can't help it; you look just like a slice of Heaven." And I said, "Well, I ain't your slice of Heaven, so put your eyes back in yo' head. (Beat) We are not old maids. We are maiden ladies.

SADIE: Well, whatever we are, I have no regrets about it. I've had a good life, child . . . (thoughtful beat) Remember, it was on your way to your job in Brunswick - you came close to being lynched -

BESSIE: Oh, yes . . . that's right. I had to change trains in Waycross, Georgia. I was sitting in the little colored waiting room at the station, and I took my hair down and was combing it.

SADIE: She had hair down to here. (She indicates her knee.)

BESSIE: I was fixing myself up. I was going to my new job, and I wanted to look nice. There was no one in there except me and two colored teachers from New York who were traveling with me to Brunswick.

SADIE: So, there she was with her long hair down when this white man opened the door to the colored waiting room.

BESSIE: The white man stuck his head in and started, well, leering at me. He was drunk, and he smelled bad, and he started mumbling things. And I said, "Oh, why don't you shut up and go wait with your own kind in the white waiting room?"

SADIE: (Overlapping.) hmmmm . . . hmmmmmm . . . hm ... hmmmmmm . . . hmmmmmmm . . .

BESSIE: He slammed the door and I could hear him shouting at the top of his lungs outside, "The nigger bitch insulted me! The nigger bitch insulted me!"

SADIE: The two colored teachers slipped out the back and made a beeline for the woods.

BESSIE: Yes! They hid in the woods! I guess I can't blame them. Well, I could see a crowd begin to gather on the platform, and I knew I was in big trouble.

SADIE: Papa always said, "If you see a crowd, you go the other way."

BESSIE: I was just waiting for somebody to get a rope. Thousands of Negroes had been lynched for far less than what I had just done. But I just continued to sit on the bench, combing my hair, while that white man was a-carrying on! You see, if you act real scared, sometimes that spurs them on. Two things saved me: that glorious, blessed train rounded the bend, breaking up the crowd and giving me my way to get on out of there. And it helped that the white man was drunk as a skunk, and that turned off some of the white people. But I wasn't afraid to die! I know you ain't got to die but once, and it seemed as good a reason to die as any. I was ready. Lord, help me, I was ready.

SADIE: You were a fool to provoke that white man. You should have ignored him.

BESSIE: How do you ignore some drunk, smelly white man treating you like trash?

SADIE: Sometimes, it's better to put up with it, and live to tell about it. At the very least you should have run off into the woods with those other two teachers.

BESSIE: (To the audience.) I told you: I would rather die than back down, honey . . .

SADIE: You are lucky to be alive.

BESSIE: (After a beat) Sadie! You know what I’ve been thinking lately? All those people who were mean to us in our lives . . . Why, they’ve turned to dust, and here we are –

BESSIE AND SADIE: (Togther) Still here!

BESSIE: They’re turning in their graves while me and sweet sister Sadie are getting the last word . . . We’re having our say, giving our opinion.

SADIE: Lord ain’t it good to be an American.

BESSIE: I’ll tell you a little secret: I’m starting to feel optimistic. Maybe I’ll get into Heaven after all. I do have some redeeming qualities. I may have to hang on to Sadie’s heels, but I’ll get there.
```

---

## IC-0595: The Help - Screenplay

- Title: The Help - Screenplay
- Author (byline): Tate Taylor (based on the novel by Kathryn Stockett)
- Work: Not specified
- Publisher: Scriptfly.com
- Publication date as stated: 2011
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SKEETER, AIBILEEN, MAE MOBLEY, ELIZABETH, AIBLEEN, HILLY, VOICE OVER, MINNY, HILLY’S MOTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1365
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tate Taylor; based on the novel by Kathryn Stockett
ISBN: N/A
Publisher: Scriptfly.com
Date (Month/Year): 2011
Cut from this on-line transcript:
https://www.screenwritersnetwork.org/wp-content/uploads/2021/03/The-Help-Script.pdf
*Original Screenplay can be purchased from Scripfly.com
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Three unforgettable women from Jackson Mississippi, circa 1963

ACTRESS 2: 22-year old Skeeter has just returned home after graduating from Ole Miss.

ACTRESS 1: Aibileen, a black maid – wise and regal and Minney, Aibileen’s best friend – perhaps the sassiest woman in Mississippi. She can cook like nobody’s business.

ACTRESS 1: As different from one another as they can be, these women will nonetheless come together for a clandestine project that will put them all at risk. And why?

ACTRESS 2: Because they are suffocating within the lines that define their town and their times. And sometimes . . .

TOGETHER: . . . lines are made to be crossed and the truth will set you free.

ACTRESS 1: The Help Screenplay by Tate Taylor

ACTRESS 2: Based on the novel by Kathyrn Stockett
```

### Performance text (classify this)

```text
Suggested Roles: Actress 1: Skeeter, Mae Mobley, Elizabeth Leefolt (Aibileen’s employer), Hilly Holbrook (Minny’s employer), Bookstore Clerk, Hilly’s Mother

Actress 2: Aibileen, Minny, Voice Over

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

(Skeeter is on the phone, while Aibileen is tending to her duties – they do not interact)

SKEETER: (Pg 33) Miss Stein, you said to write about what disturbs me, particularly if it bothers no one else . . .

AIBILEEN: (Pg 2) (going about her household chores; dusting etc.) I done raised seventeen kids in my life. Lookin' after white babies, that's what I do . . .

SKEETER: (Pg 33-34) I'd like to write something from the point of view of the help. These colored women raise white children, and then in twenty years those children become the boss. We love them and they love us, but they can't even use the toilets in our houses . . .

AIBILEEN: (Pg 4) I do all the cooking, cleaning, washing, ironing and grocery shopping, but mostly. . . (Pg 2) I know how to get them babies asleep, stop cryin', and go in the toilet bowl before they mommas even get outta bed in the mornin'. (She wakes up Mae Mobley and cradles her in her arms; affection for the child is clear)

SKEETER: (Pg 34) Margaret Mitchell glorified the mammy figure who dedicates her whole life to a white family but no one. . .ever asked Mammy how she felt about it. Nobody ever talks about it down here.

AIBILEEN: (Pg 3) Oh, Baby Girl. You is kind. You is smart. You is important. (Pg 2) That I know.

MAE MOBLEY: (Pg 43) (Mae Mobley lovingly glides her hand down Aibileen’s cheek) You’re my real mama, Aibee.

AIBILEEN: (Snuggles Mae Mobley) Baby Girl!

ELIZABETH: (Pg 4) Aibileen, bridge club! (Pg 13) The girls are pulling up, and the table isn't set!

AIBILEEN: (Pg 19) No, ma'am.

ELIZABETH: (Pg 4) Set out the dessert forks, please.

AIBILEEN: (Pg 19) Yes, ma'am. (Aibileen bustles around filling glasses of tea, etc, she exits to the kitchen – Skeeter enters)

SKEETER: (Pg 23) (whispering) Aibileen?

AIBLEEN: (Pg 45) [Miss Skeeter], ma’am. Everything okay? (Aibileen becomes nervous – white ladies don’t fraternize with the help)

SKEETER: Oh, yeah, I just wanted to talk to you. (Pg 37-38) I want to interview you . . . about working for white families. . .

AIBILEEN: (keeping her head down) You know what’d happen if Miss knew I was tellin’ stories on her?

SKEETER: . . . (oblivious) To show what y’all get paid, and the babies, and the bathrooms, the good and the bad.

AIBILEEN: (Pg 45) They set my cousin’s car on fire just cause she went down to the voting station.

SKEETER: I know it’s scary

AIBLEEN: I do this with you, I might as well burn my own house down.

SKEETER: (pleading) [But . . .] A book like this has never been written before!

AIBILEEN: (Pg 51) (gathers herself) Miss Skeeter, what if you don’t like what I got to say? About white peoples?

SKEETER: This isn’t about me. It doesn’t matter how I feel.

ELIZABETH: (Enters the kitchen angrily) (Pg 21) Aibileen, Go check on Mae Mobley (Aibileen rushes off) **** Back to bridge club****

HILLY: (Pg 22-23) (in mid conversation to the women at her bridge table; she speaks with “privilege” ) . . . If Aibileen uses the guest bath, I’m sure she uses yours too. (Aibileen enters and begins refilling tea glasses and organizing the snack table – Hilly continues as if she is not there) It’s just plain dangerous. They carry different diseases than we do. (Aibileen hears reacts non-verbally; out of site of the women) That’s why I’ve drafted The Home Health Sanitation Initiative. A disease preventative bill that requires every white home to have a separate bathroom for the colored help. (She gives Aibileen a look and motions for her to refill her cup – before she can do so, Hilly covers her cup and speaks pointedly to Aibileen) I’ll do whatever it takes to protect our children. **** The next evening – Skeeter is at Aibileen’s house**** There is a knock at the kitchen door. Aibileen quickly opens it and waves Skeeter inside.

AIBILEEN: (Pg 50-51) Quick. Come in quick.

SKEETER: I parked way up on State Street and caught a cab here like you asked. I know now that it's against the law what we're doin'.

VOICE OVER: (Pg 47) From “The Mississippi Code of Conduct for Non-whites” -- Any person printin', publishin' or circulating written matter urgin' for public acceptance of social equality between whites and negroes is subject to imprisonment.

AIBILEEN: (Pg 51) You gone have to change my name. Mine, Miss Leefolt's, everbody's.

SKEETER: (Pg 54) (nodding) You have no idea how much I appreciate your doing this with me. What changed your mind?

AIBILEEN: God. And Miss Hilly Holbrook.

SKEETER: (Pg 1) (taking out a notebook, she begins the interview) Did you know as a girl, growing up, that one day you'd be a maid?

AIBILEEN: Yes, ma'am. I did. My momma was a maid. My grandmomma was a house slave.

SKEETER: What does it feel like, to raise a white child when your own child's at home. . . being looked after by somebody else?

AIBILEEN: (Pg 11) (this is difficult for her) I lost my own boy, four years ago. (she begins to cry) (Pg 78-79) They killed my son. He fell carrying two by fours at the mill. Truck run over him, crushed his lungs. (sadness is overtaken by anger) That white foreman threw his body on the back of a truck. Drove to the colored hospital and dumped him there and honked the horn. There was nothin' they could do . . . so I brought my baby home. Laid him down on that sofa right there. He died right in front of me. Just twenty-four years old, Miss Skeeter. Best part of a person's life. Anniversary of his death come every year and I can't breathe. But to y'all it's just another day of bridge. (a quiet silence – Skeeter takes Aibileen’s hand)

MINNY: (Pg 66-68) (barges through the kitchen door hysterical) Aibileen! Aibileen! They done set off a bomb in Medgar Evers’ carport. (Minny stops cold in her tracks at the sight of Skeeter- Her face hardens) Yule May told me what y'all was up to. I didn't wanna believe it.

(Minny storms out the door)

HILLY: (Pg 42) You are fired, Minny Jackson!

MINNY: (stops suddenly and re-enters) (Pg 67) All right . . . I’m gone do it. (Pg 104) It's time to tell you both "the terrible awful" I did to Miss Hilly. (Pg 47) She's done told every white lady in town I'm a thief. Oh, I got her back. ****Flashback to Hilly Holbrook’s house*****

MINNY: (Pg 48) (stands on Hilly's porch holding a chocolate pie – she rings the bell.. Hilly answers the door and Minny presents the pie) I am sorry.

HILLY: (Pg 104 – 106) (motions her inside, and speaks while she serves herself up a slice of Minny’s famous pie) So. Nobody wanted to hire a sassmouthin', thievin' nigra, did they?

(Hilly licks her fingers. Minny can barely contain a smile as Hilly swallows another mouthful) [Chocolate] Pie's as good as always, Minny.

MINNY: (Smiling knowingly) I’m glad you like it

HILLY: (Taking a large bite of pie, she speaks with her mouth full) What do you put in here that makes it taste so good?

MINNY: That good vanilla from Mexico. . . And. . . something else real special.

HILLY: (arrogantly) If. . . I take you back, I'll have to cut your pay five dollars a week.

MINNY: (fumes, quickly losing control) Eat my shit.

HILLY: What did you say?

MINNY: I said Eat . . . My . . . Shit . . .!

HILLY: Have you lost your mind?

MINNY: No, Ma’am. But you’re about to, ‘cause you just did.

HILLY: Did what? (Minny nods smugly as she looks down at Hilly's pie. Hilly starts to
hyperventilate as everything sinks in. She runs to the kitchen, gagging)
**** Back in Aibileen’s Kitchen*****
Aibileen and Skeeter are speechless. Aibileen looks to Skeeter, shaking her head.

MINNY: (Pg 107) I've done asked God to forgive me. But more for what happened to [Hilly’s poor mama]. Miss Hilly threw her in that nursing home just for laughing. (awkward silence, then all break out laughing)

AIBILEEN: (Pg 104) The world done gone crazy, Miss Skeeter! And I'm scared! What if people find out what we writing? Figure out "Niceville" really Jackson. (Pg 107) If people find out "The Terrible Awful" was you and Miss Hilly, we're in trouble there ain't words for!

SKEETER: No, no. That's too dangerous.

MINNY: All right, y'all two brought me into this, but I'm gonna finish it! Either put it in or pull my parts out all together. Y'all pick!

SKEETER: (Pg 116) (thoughtful beat) Well, I have one more story to type before I put it in the mail. **** 6 months later*****

(Pg 122) (The display window of a bookstore. A clerk sets down a stack of books beside. She takes one and sets it vertically atop the stack for display)

AIBLEEN: (Pg 125) There it is!

SKEETER: (Pg 122) . . . The Help, by Anonymous.

AIBILEEN: They printed a few thousand copies. (Pg 123-124) They sent Miss Skeeter six hundred dollars. She broke the money up and gave it to each of us.

HILLY’S MOTHER: (reads The Help aloud to a group of women in the nursing home) "She fired me for using the inside toilet. Put me out in a storm and told me never to come back. But I did come back. I came back with a pie I had baked to say I'm sorry. I watched her eat..." (She turns a page and suddenly freezes. Reading to herself now, a satisfied smile begins to form) **** The next day at the Leefolt Home*****

(Pg 138-140) (Aibileen enters to find Elizabeth and Hilly staring at her)

HILLY: Aibileen, the silver I lent Elizabeth last week . . . When you returned it, three pieces were missing.

AIBILEEN: (flustered) Lemme . . . lemme go check in the kitchen. Maybe I left some behind.

HILLY: You know as well as I do that silver's not in the kitchen. It behooves me to inform you that you are fired, Aibileen. And I'll be calling the police. Elizabeth can take care of her own children.

AIBILEEN: I didn’t steal no silver.

HILLY: Maybe I can’t send you to jail for what you wrote, but I can send you for being a thief.

AIBILEEN: (quickly – she finally stands up for herself) I know something about you. Don’t you forget that. (Hilly narrows her eyes) And they’s a lot a time to write letters from jail. Plenty of time to write the truth about you.

HILLY: Nobody would believe what you wrote.

AIBILEEN: I don’t know. I been told I’m a pretty good writer! Already sold a lot a books!

HILLY: Call the police, Elizabeth.

AIBILEEN: All you do is scare and lie to get what you want. You a godless woman. Ain't you tired, Miss Hilly? Ain't you tired? (Hilly storms off)

MAE MOBLEY: (Pg 141-143) Don’t go Aibee.

AIBILEEN: I gots to, baby. I am so sorry. I don’t want to leave you, but . . . it’s time for me to retire. You my last little girl.

MAE MOBLEY: Noooo! (she cries)

AIBILEEN: Baby, I need you to remember ever thing I told you. Do you remember?

MAE MOBLEY: You is kind. You is smart. You is important.

AIBILEEN: That’s right, Baby Girl. (Aibileen walks away) (to audience) Mae Mobley was my last baby. In just ten minutes, the only life I knew was done.

MAE MOBLEY: (Mae Mobley runs to the living room window crying. She beats on the glass from inside. Aibileen never turns) Aibeeee! Don’t go!

AIBILEEN: God says we need to love our enemies (long beat) It hard to do . . . But it can start by telling the truth. No one had ever asked me what it felt like to be me. Once I told the truth about that . . . I felt free.
```

---

## IC-0596: Her Daddy’s Eyes

- Title: Her Daddy’s Eyes
- Author (byline): Gary E. Parker
- Work: Not specified
- Publisher: Fleming H. Revell
- Publication date as stated: April 2006
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GLADYS, ALLIE
- Teaser before the introduction: No
- Spoken words (computed): 1257
- Already set (do not supply): none

### Source block (context only)

```text
Author: Gary E. Parker
ISBN: 0800731239
Publisher: Fleming H. Revell
Date(Month/Year): April 2006
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Thirty years after Vietnam, the trauma of the war continues to haunt another generation of men and women - the estimated 120,000 sons and daughters who never saw action.

ACTRESS 2: For many families dealing with post-traumatic stress disorder in a time before it was recognized by the medical community, life with veteran fathers was a time bomb.

ACTRESS 1: Once loving fathers returned from war, snapping at the drop of a hat with no explanation . . . no warning. One minute a normal father and the next minute someone unrecognizable. How does a family cope?

ACTRESS 2: In Her Daddy’s Eyes by Gary E. Parker, Allie Wilson, now 33 and her mother Gladys try to find the answers to a family that never was.

Allie Wilson sits on the floor of her childhood bedroom in a pair of lightweight cotton pajamas. The tiny image of a blond-haired, green- finned mermaid--repeated over and over again-- decorates the pajamas. The hems of the legs and the cuffs on the sleeves are frayed, thinned by years of wear and tear. A stack of books, picture frames, shoes, old baseball caps, and a cluster of other assorted items surround her on the floor. Allie hears footsteps and looks up as her mom, Gladys, enters the room.
```

### Performance text (classify this)

```text
GLADYS: I like your pajamas. [pointing to Allie's frayed nightwear.]

ALLIE: You should. You gave them to me.

GLADYS: Christmas--when you were thirteen.

ALLIE: [smiling] I always liked mermaids.

GLADYS: [sitting beside her] They're a bit snug in the backside now, I expect.

ALLIE: And a little short in the legs but not too bad.

GLADYS: You got most of your height that year. Five ten by thirteen.

ALLIE: I'm wearing them for old times' sake.

GLADYS: I'm surprised you found them.

ALLIE: They were stuck in the back of a dresser drawer. You know me. I never throw anything away.

GLADYS: You're the queen of the pack rats.

ALLIE: [surveying the clutter] Until now.

GLADYS: [surprised] You're finally cleaning things out?

ALLIE: About time, don't you think?

GLADYS: [laughing] I guess a wedding in three weeks causes a girl to do all kinds of strange things.

ALLIE: [holding up a pair of high heels] You know anybody who can use these? I want to give away what I don't need anymore.

GLADYS: You can search the neighborhood for a tall Cinderella, I guess, but no short girl can wear these skis.

ALLIE: I bought those heels, what...twelve years ago?

GLADYS: The year you graduated from Furman.

ALLIE: I wore them the first game I ever coached; they made me taller than any of my players.

GLADYS: I'm glad you were never ashamed of your height.

ALLIE: You taught me not to slump.

GLADYS: It's a good thing Trey is six three.

ALLIE: When he proposed he said. . . "It will make every guy I know green with envy. My marrying a woman who looks like a model, long and willowy, raven hair, eyes the color of black olives.” But until recently I always said “I'm not ready yet,” You know why.

GLADYS: Let me see, could it be that your father's abandonment of us when you were just four has caused you to become distrustful of the entire male species? [Thoughtful silence for both women]

GLADYS: [changing the subject] You plan to leave anything here?

ALLIE: [goes to closet and hauls out a stack of boxes from the far corner, then sits with Gladys to go through the contents. A bunch of pictures lay inside. Allie flipped quickly through the photos, most of them showing her in various states of shooting a basketball.] I was a skinny thing.

GLADYS: Like a young filly. Still are, though you're not such a young filly anymore.

ALLIE: Hey, I'm just thirty-three!

GLADYS: Close to over-the-hill; in my day if a woman didn't marry by the time she turned thirty, she officially entered the ranks of the old maids.

ALLIE: Heaven forbid that should happen. [Allie flips the top off another box. An old corsage, its flower long since dried, rests inside. Allie holds it to her nose, takes a breath, and imagines she can still smell the scent of the bloom.] Tenth grade.

GLADYS: What was that boy's name?

ALLIE: Bill Stone. He moved away a couple of years later. Wonder what happened to him.

GLADYS: A keeper or a goner? [pointing to the corsage]

ALLIE: [waving it away] "Bill Stone is a goner.

GLADYS: [smiling] You really are cleaning out, aren't you?"

ALLIE: [opening another box with more pictures in it, black and white ones this time. Her brow furrowed as she fingers the top photo--a picture of her grandmom and granddad standing in front of the house where she now sits.] What are these?

GLADYS: [eyes widening] I thought I'd lost these.

ALLIE: Have I ever seen these?

GLADYS: [taking pictures as Allie passes them one by one] I don't know.

ALLIE: [thumbing through more pictures. Her fingers freeze as she stares at one in the middle of the stack. . . . softly] It's Dad.

GLADYS: Let me have those! They're just old pictures . . No reason to drag them out now. [Allie stands, keeping the photos from Gladys] Give me the pictures. They're mine! [reaching for the photos Allie is now holding over her head out of reach]

ALLIE: Why don't you want me to see them?

GLADYS: It's just...there's no reason to drag out old memories, that's all.

ALLIE: [Allie hands the pictures to Gladys] I'd like to see them, but I'll do what you want. [Gladys holds the photos for several seconds, then sighs and hands them back to Allie]

GLADYS: It's Jack just before he left for Vietnam.

ALLIE: I've never seen this picture.

GLADYS: You weren't born yet. I didn't even know I was pregnant at the time.

ALLIE: You're pregnant in this?

GLADYS: Just barely. I was nineteen years old, your dad too.

ALLIE: So he's the same age as you. Hard to believe.

GLADYS: You've never seen any of those. [Allie thumbs through more pictures, then . . .]

ALLIE: It's me. How old was I?

GLADYS: Three.

ALLIE: The year before dad left us?

GLADYS: Yes.

ALLIE: Do you have other pictures of me with dad?

GLADYS: Not many, perhaps a few.

ALLIE: Can I see them?

GLADYS: Of course you can.

ALLIE: Why haven't you shown them to me?

GLADYS: Didn't want you to remember bad things, to conjure up the fact that Jack left us. You want to see them now?

ALLIE: [thinks for a moment then shakes her head] Another time maybe.

GLADYS: Whenever you want.

ALLIE: Why did Dad leave us?

GLADYS: He had some troubles . . Brought them back from the war.

ALLIE: What kind of troubles?

GLADYS: He never really told me.

ALLIE: Where did he go when he left us?

GLADYS: I don't know. He used to write every now and again.

ALLIE: [softly] I wish he could be here for my wedding

GLADYS: I wish he could have been here for a lot of things for you.

ALLIE: [near tears] What happened to him, Mom?

GLADYS: I wish I knew more, but I don't. He came back from Vietnam a broken man. Suffered nightmares, sweats, the shakes, took to drinking, maybe some drugs too. I never knew all of it.

ALLIE: Did he ever say what happened to him over there?

GLADYS: Not much. Just that it was rough.

ALLIE: Do you think he really loved us?

GLADYS: I know it's hard to believe since he left us, but I know he did. He used to tell me over and over again that we were the only things that kept him alive. He sent money to us for years after he left, even after he stopped writing. He loved us. I believe that even though I don't have a lot of ways to prove it.

ALLIE: Maybe he left us because he loved us.

GLADYS: How do you figure that?

ALLIE: Maybe he didn't want to put us through what we'd have to endure if he stayed around. A man on alcohol and drugs can cause a lot of trouble for loved ones. Maybe Dad figured leaving might hurt us less than staying. At least with him gone we could get on with our lives.

GLADYS: That's one way to look at it.

ALLIE: [looking again at the pictures] Were his eyes as black as they look?

GLADYS: His eyes were as black as yours, like hockey pucks. Never seen anybody with eyes as dark as the two of you.

ALLIE: I've got his eyes.

GLADYS: I know, I just never wanted to tell you.

ALLIE: You think he's still alive?

GLADYS: I have no way of knowing.

ALLIE: I wish I knew one way or the other. [Thoughtful silence for both Allie and Gladys]

GLADYS: [breaking the silence] You planning on spending the night?

ALLIE: Why not. I'm already in my pajamas.

GLADYS: Good to have you home. [the women hug, Allie carefully puts the picture of her dad where she can see it on the night stand and returns to her cleaning, Gladys watches with a wistful smile on her face] . . . well, I need to clean up the kitchen. [Gladys exits]

ALLIE: [speaking to her father’s picture] I'm getting married . . . . Kind of scary.
```

---

## IC-0597: Heritage, Her-i-tage, and Hair-i-tage

- Title: Heritage, Her-i-tage, and Hair-i-tage
- Author (byline): Adrienne Dawes
- Work: Laugh Lines: Short Comic Plays, Pgs 91-98
- Publisher: Vintage
- Publication date as stated: April 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: REBEKAH, NPO 1, NPO 2, VOICE ON WALKIE-TALKIE
- Teaser before the introduction: Yes
- Spoken words (computed): 760
- Already set (do not supply): none

### Source block (context only)

```text
Author: Adrienne Dawes
Book: Laugh Lines: Short Comic Plays, Pgs 91-98
ISBN: 978-0307277138
Publisher: Vintage
Date (Month/Year): April 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Despite the natural hair movement of the past decade which has led black and mixed-race women to abandon chemical straighteners, for some women, dealing with curly and tightly coiled hair feels like a daily chore.

ACTRESS 2: Mothers teach their daughter the best way to deal with this very specific type of hair . . . at least most mothers do.

ACTRESS 2: Not Rebekah’s though. Rebekah has been left to figure it out for herself.

ACTRESS 1: That is . . . until the Nap Patrol arrives on the scene.

TOGETHER: Heritage, Her-i-tage and Hair-i-tage by Adrienne Dawes
```

### Performance text (classify this)

```text
Suggested Roles: Actress 1: Rebekah and Nap Patrol Officer (NPO) 2

Actress 2: Nap Patrol Officer (NPO) 1 and Voice on Walkie-Talkie

NOTE: This cutting asks students to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

(Pg 91-98) (REBEKAH, sixteen, confronts herself in the mirror. Mounds of bobby pins, barrettes, rubber bands, a variety of creams, oils, combs, brushes, and spray bottles litter the floor. REBEKAH attacks her mass of thick curls, running a huge comb through it awkwardly. Large clumps of curls fall around her. REBEKAH snatches them disgustedly.)

REBEKAH: Eww ... nasty.

(REBEKAH throws the clumps away and returns to. the mirror. She waters her hair down with a spray bottle of moisturizer, then coughs loudly from the fumes. Determined, she dips her fingers into a huge jar of curl activator and glops it onto her scalp. Large puddles of golden glop fall around her. She begins to lose her patience as she tries to mold her goopy, damp hair into a ponytail.)

REBEKAH: (on the verge of tears.) Maybe I should just cut it all off!

(As REBEKAH reaches for a pair of scissors, loud sirens flare. NPO 1 enters stage left, dressed in a police uniform, her pressed hair greased and molded in an intricate bun on the top of her hair. Various black hair supplies hang from her belt like weapons. NPO 1 points a hair dryer at REBEKAH menacingly.)

NPO 1: Giiiirrrrl, I know you did not just say you wanted to cut your hair!!

REBEKAH: (bewildered) Who are you?

NPO 1: (holding out a badge) Nap Patrol Officer Shateequa Williams, Division 8, District 21.

NPO 1: How many times a week do you wash your hair? (She carefully confiscates the scissors from REBEKAH)

REBEKAH: Two, three times? Sometimes four if I have volleyball practice.

NPO 1: What in God's name are you trying to do to yourself? Didn't your mama teach you nothing about yo hair?

REBEKAH: (quietly) Uh, well . . . no. We're learning how . . .

NPO 1: Didn't nobody in your family ever learn you to take care of they hair?

REBEKAH: (hesitantly) Well, my mom is white and . . .

NPO 1: (falls over in disbelief) Oh, giiiiirrrrrrllll!!! (into walkie-talkie.) Jamilla? We've got ourselves a 911 sit-u-ation here. I need some backup pronto. Girlfriend needs a relaxer and some pink lotion ASAP!

NPO 2: (offstage, on walkie-talkie.) Why can't her mama do her hair like everybody else's?

NPO 1: Cuz her mama's white! (NPO1 looks at REBEKAH sympathetically) Bring some copies of Ebony for her too. The girl looks like she don't know nothing 'bout her heritage!

REBEKAH: Officer, I know about-

NPO 1: (cuts her off) Yeah, yeah, let me look at this hair . . . (takes a huge clump of REBEKAH’s hair in her hands, looking at each strand in amazement) Just as I suspected . . . Your hair ain't never been relaxed or pressed before!

REBEKAH: The chemicals are disgusting and the heat will just make my hair frizzle. My mom told me that.

NPO 1: Your mama don't know nothin' about black hair! And apparently your daddy isn't around enough to make sure his child ain't cutting off a perfectly good head of hair!

(Sirens blare then cut off. NPO 2 rushes onstage, dressed in an identical uniform, her hair long, luxurious, and straight. She carries a box filled with beauty supplies and Ebony magazines, which she dumps in REBEKAH’s lap.)

NPO 2: (to NPO1, ignoring REBEKAH.) I came as fast as I could. Some idiot threw his cigarette and it hit some poor brother's head, and sweet Jesus, it was all flames and fire and chaos! I had to perform an emergency Jeri curl revival! (hands latex gloves to NPO1, then puts on a pair herself, moving to REBEKAH) Okay, let's have a look. (They pick through her hair roughly. REBEKAH winces.)

NPO 1: (in amazement.) Raw hair-never had nothin' done to it. Feel how soft it is -- and thick! (roughly pulls REBEKAH's hair. REBEKAH winces in pain) Look, no dandruff or nothing!

NPO 2: (to REBEKAH) Sweetie, how old are you? (astonished) You never once thought in all those years to straighten your hair?

NPO 1: Her mama told her the chemicals were too harsh for her! (They shake their heads and tsk in disapproval. NPO 1 begins to straighten REBEKAH's hair)

NPO 2: Please! Your white mama told you nothing but lies. No chemical is too harsh. You just gotta grin and bear it, like the rest of us. 'Sides, it only burns if you scratch your scalp . . . (suddenly suspicious) Have you been scratching your scalp? (The OFFICERS exchange a look.)

NPO 1: (cackling loudly) Oh, giiirl, it's gonna burn! It's gonna burn, it's gonna burn like hell! You'll be all right, though, and you'll know for the next time-

NPO 2: (matter-of-factly) You gotta keep straightening the hair or it'll all break off and -- Oh, but it'll look so good, girl, it'll look pretty just like mine. Look at it. (NPO 2 flips her greasy straightened hair over her shoulder and offers a strand for REBEKAH to inspect as she smiles at herself in the mirror)

NPO 1: You see that? You'll look so pretty with hair like that-especially since yours· is so long. All Jamilla has is a weave, her natural hair is only one inch long all around --

NPO 2: Now why did you have to go and tell her that?!

NPO 1: Well, it's true! (aside to REBEKAH) She looks like a sick porcupine without her weave-

NPO 2: Oh shut up, you're the one who had those ugly-ass braids in for like five years. Your hair line's receding too-gonna be bald before you're forty! (the OFFICERS stand on either side of REBEKAH, ready to fight. REBEKAH has to push them apart)

REBEKAH: Wait, wait, back to the part where my hair breaks off. How often do I have to get this done?

NPO 2: Only every six weeks-if you wanna keep it looking good. (NPO1 scowls, walks over to REBEKAH again and looks at her hair)

NPO 1: (to NPO 2) Mmm-e-relaxer's starting to take. It'll look so nice-especially since yours is au naturale! (beat, to REBEKAH.) 'Bout time you started looking like the rest of us! (suddenly NPO 2’s walkie-talkie beeps loudly.)

VOICE ON WALKIE-TALKIE: (Offstage.) Jamilla, we got a messy Weave. Disaster spread across the Beautifully Black salon about two blocks from you! We need backup hair extensions, pronto! The beautician passed out from hair spray fumes and some of the women are about to leave the building without they weaves!

NPO 2: (into walkie-talkie) I'm on it. (to the others) I gotta go. See you around, Shateequa. You too, girl. You take good care of that hair of yours.

(NPO 2 runs offstage. Sirens blare, then fade into the distance. NPO1 paces behind REBEKAH, swinging her hair dryer. REBEKAH sits, reading the magazine and twitching.)

NPO 1: (smiling widely) How you doin', girl?

REBEKAH: Uh . . . okay.

NPO 1: (notices the page REBEKAH is reading) That's Maya Angelou on that page there. She's a writer.

REBEKAH: (dully) Yes, I know who Maya Angelou is (suddenly REBEKAH turns bright red. screaming) FIRE!! FIRE!! MY SCALP IS ON FIRE!

NPO 1: (groans) Just keep it cool, girl. It'll be over in, like . . . (checks her watch.) Thirty minutes.

REBEKAH: THIRTY MINUTES?! I CAN'T WAIT THAT LONG. TAKE IT OFF! I'M GOING TO DIE! (REBEKAH makes a lunge for her hair spray bottle. NPO1 quickly hits the bottle away, then· hauls REBEKAH back to her seat.)

NPO 1: IT'S JUST A RELAXER. You're gonna be fine if you just shut up and sit down!! (they struggle)

REBEKAH: TAKE THE RELAXER OFF! TAKE IT OFF! I DON'T WANT STRAIGHT HAIR!

NPO 1: No! Now you are going to sit through it like everyone else, and you are going to be proud of your beautiful black hair-i-tagel

REBEKAH: AAAAAAAAHHHHHHHHH!

(sirens flash and NAP PATROL OFFICER I disappears, Lights darken around REBEKAH, who· has turned bright red, screaming and pulling at her hair. Smoke billows around her and swallows her. Blackout.)
```

---

## IC-0598: Hillary: A Modern Greek Tragedy With a (Somewhat) Happy Ending

- Title: Hillary: A Modern Greek Tragedy With a (Somewhat) Happy Ending
- Author (byline): Wendy Weiner
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Oct 2009
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CHORUS, ATHENA, APHRODITE, HILLARY, BILL, NEWSCASTER, ACTRESS 2, ACTRESS 1
- Teaser before the introduction: Yes
- Spoken words (computed): 2205
- Already set (do not supply): none

### Source block (context only)

```text
Author: Wendy Weiner
ISBN: 978-0822223757
Publisher: Dramatists Play Service
Date (Month/Year): Oct 2009
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Hillary Rodham Clinton - a woman determined to succeed and achieve her dreams in a world in which the deck is stacked against her and the rules of the game thwart her at every turn.

ACTRESS 2: Today we call it “karma” . . . in ancient Greece, they called it “the power of the gods.” Perhaps it is as author Wendy Weiner envisions it, a bit of both.

TOGETHER: Hillary: A Modern Greek Tragedy with a (Somewhat) Happy Ending by Wendy Weiner
```

### Performance text (classify this)

```text
Suggested Roles: Actress 1 – Shared Chorus lines and Hillary Actress 2 – Shared Chorus lines, Athena, Aphrodite, Bill, Newscaster

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

CHORUS: (1) Bolt the doors. / Close the curtains. / Turn off your cell phones. / For you are the few selected to finally hear the truth. (2) In a time before Travelgate / And even Watergate, / When humans knew that it was not they - / but the gods - who ruled the earth, (1) There was a pair even more famous than Hillary and Bill. (2) More talked about. / More dissected. / We know - it doesn't seem possible.

(They gesture to the heavens. Lights come up on Olympus. In two separate areas stand the goddesses: Athena, strong and majestic, wearing a breastplate and holding a spear. Aphrodite, exquisitely beautiful, in golden toga and sandals. The Chorus introduces them.)

CHORUS: (1) Athena –

ATHENA: Goddess of wisdom, victory - and olives.

CHORUS: (1) And Aphrodite -

APHRODITE: The goddess of love and beauty. Obviously.

CHORUS: (1) That's cool, you might be thinking, / But what does it have to do with ME? (2) Let us take you then, to our tale, / Which does not unfold in ancient Greece / But in the United States of America. (1) A country which espouses freedom, liberty, and happiness for all / Yet also a place where a woman has never been president (2) In this land lived a girl who, at fourteen, / Was desperate to know all there was to know, (1) She wrote a letter to her country's prestigious space-travel program / Asking them how to apply to become an astronaut. (2) The letter she received back told her not to bother – girls could not apply.

(Lights come up on Hillary, at age fourteen)

HILLARY: (Letter in hand.) This is so unfair! . . . I'm not crying! I never cry!

CHORUS: (2) It was then that Hillary came up with her mantra. . .

HILLARY: Emotions are stupid and I am smart, Emotions are stupid and I am smart, Emotions are stupid and I am smart . . .

CHORUS: (2) Hillary walked many miles to Illinois' famed shrines / Where the altars of Athena and Aphrodite sat side by side.

(As Hillary arrives at the shrines, both goddesses go on alert to see whose shrine she'll go to. After some hesitation, Hillary goes to Athena's shrine and looks at it solemnly. She kneels in front of the altar.)

HILLARY: O, Athena, Please help me make our world a place where girls can use all the gifts given to them by the gods and become doctors and presidents and even (Painful for her to say.) astronauts. Help me ascend to the male seat of power, The White House. (Sound of a lightning bolt. Hillary and Athena react.) Get me to Washington and let me rule and I promise to protect girls and right our world's wrongs against them. (Lights fade on Olympus as Athena descends to earth. She stands in front of Hillary, accompanied by a blaze of glorious light. Hillary is dazzled)

ATHENA: What you want, Hillary, is not something the world wants for you. Do you understand that?

HILLARY: That doesn't scare me.

ATHENA: It should. For deep-rooted beliefs are a far more insidious enemy than any dragon and change is far more frightening to the human spirit than a twenty-foot woman with snakes for hair.

CHORUS: (1) With her fine mind and Athena's guidance, / Hillary easily obtained entrance to Wellesley, / Where she became the first student speaker at a college graduation in the history of the country. (2) Hillary and her speech appeared in the pages of Life magazine / So when she arrived at Yale Law School, / She was already a bit of a star. (1) All was going exceedingly well for young Hillary / Until one night:

(Hillary, with her hair pulled back and wearing thick glasses, sits reading and taking notes on a legal pad. Aphrodite enters.)

APHRODITE: Behold Aphrodite, goddess of love and beauty!

HILLARY: (Looking up only briefly.) I don't have time. (Aphrodite is shocked. She's never received such a greeting.)

APHRODITE: Perhaps you didn't hear me. I said- Behold

HILLARY: Ssssshhhh! This is a library. I don't know how information is disseminated in Olympus, but I've devoted myself to Athena. Alone.

APHRODITE: (Excited.) Do you realize that, with a small makeover and a few lessons in the social graces, I could get you any man on this campus?

HILLARY: That is so sexist. It's the 1970s, Aphrodite. Get over yourself.

APHRODITE: How dare you! (Hillary shakes her head as she puts her glasses back on.) No woman defies the call of Aphrodite!

HILLARY: News flash: I'm not interested in being a wife, I'm interested in being a leader.

APHRODITE: You'll regret this. (Hillary rolls her eyes.)

CHORUS: (1) And so Hillary had made her first political mistake. (2) For Athena was not the only goddess / Who had been grooming mortals in her own image. /Aphrodite had her own disciple . . . (Aphrodite sticks an arrow in Hillary's back.)

HILLARY: Ow! (Hillary pulls the arrow out of her back and looks at it quizzically, then looks up and sees Bill. She is immediately lovestruck.) Who's that?

CHORUS: (2) William Jefferson Clinton. / Bill and Hillary started studying together. And then things got even hotter:

HILLARY: Bill, the exam is tomorrow.

BILL: Like you even need to study. You're smarter than every other student here. And when you smile, you're just about the most beautiful thing I ever seen.

CHORUS: (1) No one had ever called Hillary beautiful before. (2) Attractive, yes. Pretty, sometimes. Sturdy, sure. But beautiful? No.

HILLARY: (Flirtatiously.) You're a bad influence on me, Bill Clinton.

ATHENA: Aphrodite. You need to stop the games with Hillary. Now. She has important things to accomplish. I don't appreciate you wasting her time with this ridiculous romance. ******* Time passes *********

HILLARY: Working on the Watergate Committee was so exciting! The corruption in that administration is just - (She shakes her head.)

ATHENA: Obviously there was obstruction of justice. But how did you argue impeachment?

HILLARY: I argued for a broader definition of the legal justifications for impeachment. This is going to affect presidents for years to come!

ATHENA: You're on exactly the right track, Hillary. Now we need to talk about the next step.

HILLARY: I'm moving. Bill is running for congress in Arkansas this year. After that, he'll run for governor. He'll be the youngest governor in that state ever.

ATHENA: Which would make you the girlfriend of the youngest governor in Arkansas ever. Is that why you went to Wellesley? Is that why you went to Yale? Most people don't even know where Arkansas IS!

HILLARY: I'm going to marry Bill Clinton. (Athena is upset by this news, but gathers herself together.)

ATHENA: Hillary! Don't you see what's happening? This is the work of Aphrodite. She's using love to distract you from your real work.

HILLARY: Why can't I have both, just like men do? Isn't that what you and I are fighting for? I don't want to just be a high-powered attorney working hundred-hour weeks. I want someone to come home to. I want Bill to come home to.

ATHENA: I like Bill. He's a nice boy, but -

HILLARY: He's not just a nice boy. He's going to be president of the United States. (Athena is shocked.)

ATHENA: When you first came to me, you wanted to be president.

HILLARY: It's not the time, and you and I both know it. There's only one way I'm making it to the White House here and now, and that's on the arm of a man. But Bill is the right man. He doesn't want a first lady who just smiles at her husband's side. Bill and I will be the first president and first lady who are equals. We'll be two for the price of one. (Realizes.) That could be a good campaign slogan.

ATHENA: There's something you should know. About Bill.

HILLARY: (Quickly.) I know everything I need to know. With him, I don't have to pretend I don't have ideas and ambitions. He could've picked any number of non-threatening, yes-dear, it-takes-me-an-hour-to-put-on-my-eyelashes types from Arkansas. But he didn't. He chose ME. (With wonder.) He loves me.

CHORUS: (2) Hillary's time in Arkansas / Stretched out into eighteen long years. / As Bill was elected governor four times / And she stood behind him for speech after speech / Smiling, nodding, waving, smiling, / All the while preparing themselves / For an election only they believed they could win: (1 and 2) The presidential campaign of 1992. (1) But just as it looked like they might have a real chance, / Aphrodite decided it was time to remind Hillary who was really in charge ... (Aphrodite, wearing a wig of big blonde hair, stands behind a microphone, at a press conference.)

APHRODITE: (With strong Southern accent.) My name is Gennifer Flowers, and presidential candidate Bill Clinton and I have had an affair. (Hillary watches Aphrodite in horror.)

We have made sweet sweet love in my bedroom, in my foyer, on my kitchen table, in my pantry

HILLARY: It's lies! Republican lies! (to Athena) I can't bear listening to that woman. I can't worry that every time my husband leaves the house, he is - there must be some way you can help me! (Pause.)

ATHENA: I didn't want to do this. And yet, maybe it is still what a woman needs to do to succeed in this world. I can remove half your heart. In its place will be anger. An anger all heroes have felt, and it will serve as fuel for your journey. But it has other effects as well.

HILLARY: Such as?

ATHENA: Your ability to compromise . . . The classic female arts that give you social graces, the right tone of voice, the ability to hide a sword behind a smile, those things Lady Bird and Jackie were so very good at, these are strengths you will no longer have. You'll be a warrior. (Athena looks at Hillary. Hillary nods her assent.)

CHORUS: (1) And so that night the ravens came. / Their beaks sharpened by all the cruelty in the world. (2) Their cold, taloned feet perched on Hillary's chest / As they fought each other towards the prize: Half of her embattled heart.

HILLARY: (Colder and harsher than we've seen her before.) You know, I'm not sitting here - some little woman standing by my man like Tammy Wynette. I'm sitting here because I love him - and I respect him. And you know, if that's not enough for people, then heck, don't vote for him.

CHORUS: (2) And so it was with Great sacrifices / And a little celestial help - A lot of celestial help / Bill and Hillary made it to the White House at last. / Which is when Hillary's problems really began.

HILLARY: (Stiff ) Right now, thirty-seven million Americans do not have health-care. My plan will establish corporate "regional alliances" of health providers. My plan will ensure that, for the first time, women's health-care gets the same attention as men's. My plan -

CHORUS: (2) Her thirteen-hundred-page health-care plan died an ugly death on the floor of Congress.

HILLARY: Scum-sucking misogynist money-grubbing REPUBLICANS! I'm trying to stop people from DYING!

ATHENA: We misread our enemy. Politics isn't like the battlefield. You have to fight your enemy with one hand and stroke him with the other. (She pulls out a mass of computerized data.) According to my polls, right now, they describe you as: strong, intelligent -

HILLARY: (Pleased.) Really?

ATHENA: . . . dishonest and a bitch. (A dead raven with a rolled-up paper in its claws; it lands heavily at Hillary's feet.) A dead raven.

HILLARY: That doesn't seem like a good sign.

ATHENA: Traditionally ... no. (Athena reaches over, picks up the bird, and pulls out the paper from its claws. She reads its contents.)

HILLARY: What is it?

ATHENA: It's a front-page story about the president and a ... young lady.

HILLARY: What?! (scene change – Hillary confronts Bill) Tell me it's a lie. (No response from Bill.) This girl is only a few years older than Chelsea. (In a cold, attorney-like tone.) Who is she? Do you know her?

BILL: Of course. She's an intern at the White House. And a - a troubled young lady . . I swear. I did not have sexual relations with . . . that woman.

HILLARY: (Giddy with relief) Of course you didn't! What kind of idiot would believe you would take these kinds of risks when the Republicans are just WAITING for something to bring you down? Who would believe any man would throw away his family, his career, his country for - a moment of sleazy pleasure. That's exactly what I'm going to tell the press. (Lights down on them, then up on . . . Hillary sitting stiffly in a chair. A Newscaster, sits next to her.)

NEWSCASTER: (To Hillary.) The president has described to the American people what this relationship with Monica Lewinsky was not. Can you tell the audience watching today: What was it?

HILLARY: An intense political agenda at work! The true story is this vast right-wing conspiracy that has been conspiring against my husband since the day he announced for president.

NEWSCASTER: Let me take your husband out of this for a second . . . if an American president had an adulterous liaison in the White House and lied to cover it up, should the American people ask for his resignation?

HILLARY: Yes. That would be a very serious offense. In fact, what I implore the Congress to do - is appoint a special prosecutor to look into this. Let them unturn every rock, read every letter my husband has sent, ask every oracle! And if I am wrong, may I be struck down by the gods! (A thunderbolt. Hillary and the Newscaster start in surprise.)

CHORUS: (2) It was the first grand jury subpoena for a sitting president's testimony in U.S. history. The country was lit up from coast to coast by the sickly blue of television screens / As people waited to hear the truth. (Hillary stands alone.)

HILLARY: (To herself.) I will not cry. I will not show humiliation. I will be as strong as a man. I will be a block of marble. (Hillary goes to Bill.) Remember, only answer what they ask you. They're going to try and trip you up. If they can create even the appearance of perjury, it could cost us the presidency. Just keep it brief and stick to the truth and you'll be fine.

BILL: (to the cameras) It depends on what the meaning of the word "is" is. Now, if someone had asked me on that day, are you having any kind of sexual relations with Ms. Lewinsky, that is, asked me a question in the present tense, I would have said no. And it would have been completely true.

CHORUS: (1) Everyone in the country- and the world - Was buzzing with word of Hillary's humiliation.

HILLARY: Fear is stupid, and I am strong. Fear is stupid and I am strong. Goddamn you, Bill. I will not cry.

CHORUS: (2) One single tear. Fell to the ground / And was quickly drunk by the thirsty earth.

*****Time passes *****

CHORUS: (2) New York's next senator: Hillary Rodham Clinton! (The sound of raucous applause, hooting and howling. Hillary is loving it.)

HILLARY: Thank you all so much. This is amazing, thank you. There are people who said I couldn't do this, but they weren't counting on you. (Raucous applause.)

CHORUS: (2) Back in that spot / In the White House Rose Garden / Where Hillary's tear had fallen / Something happened to the flowers. / Their beauty grew sharper / And so did their thorns / Put there to protect their splendor / From an often unwelcoming world. / If you stand in the Rose Garden, even today, / And listen very closely, / You can still hear the faintest sound / Of a woman's voice:

HILLARY: . . . There was a time when a woman's dream of being a senator would have been called impossible. The year I was born, 1947, there were no women in the senate. But now I'm here. And I do believe that, one day, whether it be my generation or the next, we will have a female president. CLOSING

ACTRESS 2: And we all know how that turned out!

ACTRESS 1: Close . . . but no cigar!!

ACTRESS 1: Michelle Obama for PRESIDENT!
```

---

## IC-0599: Igloo Coup

- Title: Igloo Coup
- Author (byline): Ira Brodsky and Barbara Lhota
- Work: 35 Original Comedic Plays for tow Females (Forensic Duo Series) Volume 3
- Publisher: Smith and Kraus
- Publication date as stated: September 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MARCIE, DENISE
- Teaser before the introduction: Yes
- Spoken words (computed): 1855
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ira Brodsky and Barbara Lhota
Book: 35 Original Comedic Plays for tow Females (Forensic Duo Series) Volume 3
ISBN: 1575253801
Publisher: Smith and Kraus
Date (Month/Year): September 2004
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Denise has been dying to play the part of the Snow Princess at Northgate Mall's Christmas display since she was a child. This year, she convinced her roommate and fellow actress, Marcie, to go with her to the audition.

ACTRESS 2: Marcie was thrilled to be cast as a Candy Cane. Unfortunately, Denise was extremely unhappy to get the part of a Snowflake Helper, understudy to the Princess. The Snow Princess role went to a grossly ill-prepared girl who flirted mercilessly with the casting director.

ACTRESS 1: The Snow Princess makes out with the Toy Soldier in public, she burps and slouches, and treats the Snowflake Helpers like scum.

ACTRESS 2: Something has to be done! Christmas must be saved! Actresses everywhere unite!

TOGETHER: Igloo Coup by Ira Brodsky and Barbara Lhota.
```

### Performance text (classify this)

```text
(Marcie hands children candy canes as they head to Santa's castle.)

MARCIE: Now, now, keep that candy cane in your mouth. Don't poke your brother in the eye with that. All sticky. I'm a candy cane too and we don't like to be put in people's eyes. We like to be hung on a tree or eaten. Yum, yum. (To Denise.) OK, that sounded wrong. (To Denise, loudly so children can hear.} Hello, Snowflake! Look, it's our Snowflake Helper who's come to visit us in Candy Land.

DENISE: (To another child.) Hey, don't be naughty. Someone's got a list, and he's going to cross you off. So watch your hands. Chop, chop.

MARCIE: (To Denise.) Hey. What's with Ms. Snowflake? She sounds a little (Makes brrr sound.) coldish today, doesn't she? It's always coldish (Making brrr sound again.} in the North Pole. Coooollld. Brrr!

DENISE: (To Marcie.) I'm sorry. I'm just in a bad mood.

MARCIE: I know. I know. Snow Princess again? What's going on?

DENISE: She's got no respect for the part, Marcie. I have to see it day in and day out.

MARCIE: I know, I know. But we just gotta realize sometimes it's not about the talent, it's about who you know.

DENISE: I know. Her Santa connection got her right in. And that's all she needed.

MARCIE: So what's she up to this time?

DENISE: She was making out with a Toy Soldier in the hallway.

MARCIE: No way! You're kidding!? In costume? Did anyone see her?

DENISE: No, because luckily I was there to avert the children's eyes. I was turning kids toward Willy Wonka like crazy.

MARCIE: Oh, thank God, but he's a weirdo, huh? He told me he had channeled the great Gene Wilder to play the part. And he seemed thoroughly confused. And our Varuka is a little (Winds up hand to express crazy.} woo-hoo typecast.

DENISE: Oh, I know. Well, the whole Candy Land section was poorly directed and cast.

MARCIE: (Offended.) Hey! I'm part of Candy Land.

DENISE: Oh God, I didn't mean you. I've never seen anybody so committed.

MARCIE: Really? I was thinking my red-and-white thing was off. I wasn't feeling very stripy, you know? I'm just so one color typically. Today I thought I'd try not working so hard at being striped. No indicating. Is it working?

DENISE: Like a charm. I see you and stripes vibrate but very subtly. Not pushing at all. Really, I'm just. . . well, I'm so proud to be your fellow actor. I can see that our first semester of classes has already paid off. You seem very en-thusiastic and calming. Very red-and-white. Just like a candy cane should be.

MARCIE: Oh God. Really? I thought I was doing OK 'cause some kid licked my face this morning. But what about the sugary thing? Do I seem sugary enough?

DENISE: Let me see? Can you show me what you're doing with that? (Marcie puts her arms straight down in candy cane form but she smiles with her whole face, trying to look super sweet.)

DENISE: Oh, wow, wow, that is great. But don't push. (Marcie smiles but more gently this time, lifting her eyebrow suggestively.) Incredible, but don't bend from the waist. It makes you look like a disfigured candy cane. And that's a little disturbing.

MARCIE: So tell me, what's going down at the igloo?

DENISE: (Shakes her head.) It's a nightmare. The Princess thinks that just because we're Snowflake Helpers that we're her personal Flakes. She told me to get her a Diet Coke.

MARCIE: Who died and made her Prin-well, you know what I mean.

DENISE: Exactly. And it's totally wrong for the character. A Snow Princess would not drink a Diet Coke obviously. It's not classic Christmas. Hot cocoa would be an apropos choice.

MARCIE: Or hot cider?

DENISE: Yeah, yeah! (Marcie nods.} Well, no, too Halloween. See? Because we care, we bother to think the choices through. She doesn't care. She sweats even though she lives in an igloo. She slouches and hunches down in her throne drinking her Diet Coke, which she doesn't even hide. The kids walk in. Me, Marion, and Mike are very serious about being as unique as possible even though our costumes are very similar. Marion is a very light flake. George is very watery. And I'm a very big flake.

MARCIE: Wow. That's so great that you're differentiating.

DENISE: Mike thinks I've got big flake down pat. Anyway, we all bow down to her and call her "Your Majesty." We talk about her glistening ice shoes and her lovely gown and show the children the icicle water fountain. We're very proper. So what does she do? She asked some kid where she could buy a good CD burner, and then proceeded to light a cigarette and blow smoke up the igloo chimney. See what I'm dealing with. She said it made the chimney look realistic. I was horrified. I tried to call Jerry so that he could see what damage she was doing. So he could fire her. But she always makes nice-nice and hides her cigarettes and gum and pops and pretends to be a good Snow Princess when he's around. But I lost it this afternoon when I saw her with the Toy Soldier. It took me right over the edge. I didn't know if I could work with this false Princess anymore.

MARCIE: I don't blame you. I mean, a Princess should not be slinking around with the Toy Soldier. I mean, the Baby Doll and Soldier maybe, but

DENISE: I just wanted to quit!

MARCIE: (Gasps.) No. Don't do that! You know you need the experience. Besides, we've got that November phone bill and the 30 percent holiday discount. And more importantly, when they see how good you are, you could definitely be the Princess next year.

DENISE: I know, that's what got me thinking. (Quietly, whispering.) And then I got this other thought.

MARCIE: (Quietly.) What other thought?

DENISE: We could overthrow her. A coup, a coup.

MARCIE: Bless you.

DENISE: No! A coup! Nobody likes her over there in the igloo. The Jackin-the-Box is the only one. The flakes are all behind me. Even Baby Doll and the Sugar Plum want her out. And all of them know I was gypped out of the part. We get her fired by presenting some incriminating evidence. Smudge the Snow Princess's white reputation.

MARCIE: Oh gosh. So how you gonna do that?

DENISE: Well, you know how Baby Doll smokes, right? But she's real cool about it. She's trying to quit and wouldn't dare do it during a performance. Well, she's agreed to lure the Princess into the fire escape door and get her smoking in full costume, which is strictly against the rules. Now mind you, we have to wait to get the signal that Baby Doll's cigarette is out, and that's where you come in.

MARCIE: Oh no! I can't do anything cooish!

DENISE: It's not coup-ish. All you're doing is calling Jerry and showing him how the fire escape door was left open.

MARCIE: I don't know, Denise. I need this opportunity. Besides, I don't think Candy Canes are really talkative. I mean, maybe I should be mute.

DENISE: Well, fine, if you want to go that way, then just point then.

MARCIE: But I'm probably technically not supposed to have hands either. I've been shoddy with my homework. Besides, I just can't do this. They might suspect me.

DENISE: What are you talking about? No one's going to think you did anything. It's all very innocent.

MARCIE: I don't know. My station is very close to Santa Claus. If he catches word of this attack on his friend, the Snow Princess, you know I'm gonna go down.

DENISE: Jeez, Marcie, I thought we were in this together. You're gonna let this Diet Coke-drinking, heavy-smoking witch represent the Snow Princess in the upcoming Northgate Mall parade? You're going to let the sleaze suck face with Toy Soldiers in front of the innocent tots as they wave to Santa?

MARCIE: Well, well, I know, but. . . Why don't you do it?

DENISE: Don't you see? If I do it, it'll look obvious. I'm the understudy. It'll look like I set her up.

MARCIE: No, it won't. (Beat.) Well, didn't you?

DENISE: Yes, that's why I don't want it to look like it!

MARCIE: You don't understand. I need this part, Denise. You've shown Jerry your range, as the Pilgrim Lady and the Fourth of July Hat. This is the first part I've landed. I just don't want to screw it up.

DENISE: Honey, you won't. I promise. The reason I am so frustrated and distraught is because of my experience. I've been a Candy Cane. I've been the Pilgrim. I've been a Pumpkin. I know what it takes to be a good Snow Princess, and that bimbo just stole the part from under me. Because she knew the big, fat red guy. Sure, if she cared about the performance, about the truth of the role, like you and I care, I wouldn't mind. I'd applaud and bow to her and give her my Snowflake offerings, but she doesn't. She spits in my face! She laughs at me and even mocked me. She said I'm a flake ball. Not a snow ball. That wouldn't offend, but a flake ball. To her all I am is a Flake! She told me! And even though I am, I knew what she meant. Do you see how that hurts? Do you see how that destroys my confidence?

MARCIE: Sure. But what about the other Flakes? Can't they help?

DENISE: There are only three of us. Someone would notice if we all left our station. With the Candy Canes there are plenty of you. Nobody will even notice. Please, please, when she mocks me, don't you see? She mocks all of us who care.

MARCIE: Ohhh. I don't know. It's so hard. Sometimes I think this business is so shallow and empty. I mean, I wonder if we're not all fighting for something ridiculous. I mean, vying for the big part. And what is the big part really, but some fancy costume in a made-up world of department sales. I know it sounds cynical, but what is more cynical than our commercialization and mass marketing of complicated historical and religious events like Christmas that we simplify and destroy in order to sell sofas and wall-to-wall carpeting?

DENISE: Yeah, but you get to be in a parade. Did I mention that she said all the Candy Canes sucked?

MARCIE: (Shocked.) What! But she doesn't even watch us. What did she mean by that?

DENISE: She said none of you had any acting ability at all. You all sucked!

MARCIE: (Face drops.) Maybe she could argue with our interpretation, but that little

DENISE: And she makes ten dollars an hour to our seven fifty!

MARCIE: Oh my-this is outrageous!

DENISE: So you'll do it?

MARCIE: I will. Proudly. I'm going out on a limb. I'm thinking a Candy Cane could point, as long as it does it with its whole Candy Cane self.

DENISE: Wow. Now, that I've seen you enraged like this, I see it in you. You're gonna be a great actress, Marcie. You could play the Snow Princess someday too.

MARCIE: And then Blanche DuBois, Lady Macbeth!

DENISE: Let's not jump ahead, but certainly Dainty Duck for Easter or one of the Cratchet's daughters next Christmas.

MARCIE: (Cringes as a kid licks her.) Ahh! Some kid just licked my knee.

DENISE: See? See. See! You are the Candy Cane! You have power and subtlety. The essence of red-and-white.

MARCIE: OK, Snowflake, my nonexistent Candy Cane feet are gonna kick some Princess butt.

DENISE: Bravo! Get your sugar content up! The battle begins!
```

---

## IC-0600: The Insanity of Mary Girard

- Title: The Insanity of Mary Girard
- Author (byline): Lanie Robertson
- Work: The Best Short Plays 1978, Pgs 66-99
- Publisher: Chilton Book Company
- Publication date as stated: Jan 1978
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: FURIES, MARY, ACTRESS 2, WARDER, MRS. LUM, STEPHEN
- Teaser before the introduction: Yes
- Spoken words (computed): 2025
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lanie Robertson
Book: The Best Short Plays 1978, Pgs 66-99
ISBN: 978-0801966422
Publisher: Chilton Book Company
Date (Month/Year): Jan 1978
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: In the late 1700’s women were expected to be dutiful, subservient housewives, to take care of the children, and to keep order in the house.

ACTRESS 2: Men made all the decisions; women were simply expected to listen and obey. Divorce was not an accepted practice.

ACTRESS 1: But if a woman behaved in a way that opposed her husband or brought him dishonor, he could legally have her declared insane and have her committed.

ACTRESS 2: In the 1700’s many perfectly sane women ended up in asylums.

ACTRESS 1: Mary Girard was both an opinionated and outspoken believer in equality. She railed against unjust practices.

ACTRESS 2: Today she would be called a leader; but in her time there were just vague whispers about . . .

TOGETHER: The Insanity of Mary Girard by Lanie Robertson
```

### Performance text (classify this)

```text
Suggested Roles: Actress 1: Mary Actress 2: Furies, Warder, Mrs. Lum, Stephen

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Mary Girard is bound in the Tranquilizing Chair – used for “excitable patients” who were believed to be insane. Leather straps bind down wrists, arms, chest and ankles. A square box swings down over the head. Mary is a very attractive woman, 29 years old. The Furies circle the chair and lift the box. Mary seems, at first, asleep or in a coma. Then she becomes agitated and strains against her bonds.

FURIES: (Pg 67) (tauntingly) Mary. Mary Girard. Mary. Girard.

MARY: (screams) Who are you? Stay away from me! No! Let me out of here. Set me free at once!

FURIES: Oh. She's so. Indignant. Quite the fine lady. Isn't she? No one would think. Her husband was. Well-to-do. Would they, Mary?

MARY: (Pg 68-69) Who are you? What are you? Tell me.

FURIES: We're no one. Nothing. Inmates of the asylum. Like you, Mary. Figments of your imagination. A puff. A poof. Of nothing. Nothing, nothing. (setting MARY free)

MARY: If you are nothing, then I must be mad. I can see you, hear you. (grabs at them but they elude her) Tell me where I am? And how long I've been here.

FURIES: (disappointed) That's too simple. It's no fun. You know that already. The Pennsylvania. Hospital. The same. As it was. This morning.

MARY: But I'm not crazy. You know I'm not.

FURIES: You must be! Mr. Girard had you admitted. As a lunatic, paying patient. The doctors have agreed. To keep you here. As long as Mr. Girard. Continues to pay. Quite a lucrative account.

ACTRESS 2: Based on a real-life story of a woman who spent the last 25 years of her life in a mental institution.

MARY: (Pg 69-70) (as the FURIES laugh at her frustration) It's all a misunderstanding. When I see the doctors, when I speak to Mr. Girard, it will all be corrected. It's a mistake, I tell you. And that chair. I thought I'd go mad.

FURIES: She will. In time. She sounds. Stark raving. Mad. That chair is one of the. Prized possessions. And inventions of. Dr. Rush. He positively. Loves it. And. So do we.

MARY: I couldn't move. I couldn't see anything. And then my eyes began to tear and I couldn't wipe them. And there was such a roaring in my ears. I thought I would go . . . that it would drive me . . .

FURIES: You were only here. Experiencing the effects. Of the Tranquilizing Chair. It's the. Proper treatment. For your type. Of madness. Dr. Rush. Has invented. Two appliances. To be used for. The treatment of. The mad. The gyrator. Or revolving machine. That shakes them up. The other is. The tranquilizing chair. For types like you. Ones subject to claims of. Sanity.

MARY: (furious) How dare you speak to me like that. I'm Mrs. Stephen Girard! I don't have to tolerate your taunts and jeers. (Pg 71) Tell me how to get out of here. Please. Please!

FURIES: We can only. Show you. You have to start. At the beginning. By seeing. The warder of. The cells. *****Scene*****

WARDER: (Pg 72-73) (enters, he is about Mary’s age) Here ye go. In here, Mary. That's yer name, ain't it?

MARY: (haughtily) My name is Mrs. Stephen Girard. You will call me by that name if you address me again.

WARDER: Oh no, I don't. I calls ye Mary. I was told by Mr. Girard hisself I was to so call ye.

MARY: You don't understand. I came to see the doctor about a personal condition. Where is he, sir? (pause) I demand that you take me to the doctor at once!

WARDER: Snooty, ain't ye? Wants to see the doctor at once, do she? Well, doctors don't come round at once. They're due sometime week after next. I guess ye'll wait till then, all right.

(exits the cell, closing the door)

MARY: (Pg 74-75) What are you doing?

WARDER: Lockin' the door to yer new home. It's customary.

MARY: You can't keep me here. Where am I? Is this a prison?

WARDER: That's real insultin', that is. This is the Pennsylvania Hospital. An' ye are in the ward fer the mentally deranged. The place fer lunaticks, in plain speech.

MARY: But I'm not a lunatic.

WARDER: That's not fer ye or me to say. That's fer Mr. Girard to say. He be yer legal guardian an' he's the one who put ye here. By law whenever a legal guardian says the one they's guardian over is lunatick then we picks 'em up and puts 'em here. We got lots of women folks here whose helpmates has writ out a little letter sayin' they's lunatick. Seems to happen more to women folks 'count of the delicacy of thar minds.

MARY: Well, this has to be a dreadful mistake because no one has examined me. My husband said I was to come with you to see a doctor.

WARDER: Yep. That's what we tell most of 'em. "Jest goin' to the hospital to see the doctor." Works nearly every time. Sometimes tell 'em they're goin' to see the dentist. Jest for variety's sake. Lots of crazy folks looks jus’ fine when they come in. I give you ‘bout a month . . . I won’t be able to tell you from any of those others. (exits; Mary cries; FURIES enter)

FURIES: (Pg 76) Don't be. Upset. Mary. Mary.

MARY: I have to get out of here. I have to see someone, talk with someone. When will they let me see someone?

FURIES: But we can let you. See anyone. Just name the name. And instantly you'll see them.

MARY: I want to see my mother. (FURIES exit, Mrs. Lum enters)

MRS. LUM: Madam, you sent for me?

MARY: (pleading) Mother, I need you. (Pg 77-79) My husband abuses me.

MRS. LUM: For shame that you should give him cause. And double shame that you be brazen enough to tell it. There is nothing unusual in a husband's abusing his wife. It is the woman's place to be clever enough to seem to do his will whether she do or no.

MARY: And must the wife always bend to her husband's will, whether it be right or wrong?

MRS. LUM: It is the husband's place to rule his wife. The woman's to obey her husband. It is the Law.

MARY: Whose Law?

MRS. LUM: God's Law. When you married you vowed to honor and obey your husband, madam, 'till death do you part. Do you dare question the Law of God Himself?

MARY: If this is God's Law, as you say it is, why didn't you explain this Law to me before I married Mr. Girard? I was sixteen years old!

MRS. LUM: You knew what you were doing. You got the home you wanted and much more.

MARY: I have nothing, Madam, nothing!

MRS. LUM: Then you can only blame yourself. A wise woman never lets her husband know the distaste she may feel for him. You should have dissembled more and hidden whatever loathing you may have felt behind a display of feigned affection.

MARY: I would have been a liar.

MRS. LUM: You would have fared better. (pause)

MARY: I asked you here because I have desperate news. (pause) I am with child.

MRS. LUM: This is wonderful! Nothing in all the world can do more to please a childless man. Mr. Girard must be overjoyed.

MARY: I haven't told him. I fear what he might do to me, mother. It is not Mr. Girard's child.

FURIES: (swooping in as Mrs. Lum exits) (Pg 84) Whose baby is it, Mary? Yes, tell us, Mary. Tell us who the father is. Tell us. Tell. Tell.

MARY: The father is unimportant. He was someone warm and affectionate to me.

FURIES: You were untrue, Mary. You betrayed your husband. And broke your marriage vows. For shame. Shame, Mary. You will give birth to an evil thing. Only evil comes from evil.

MARY: I don't believe it. I don't believe you. You're trying to drive me mad.

FURIES: (Pg 88) Oh. We got us some cures here, Mary. Icy baths in winter. Splinters under the thumbnails. A white-hot iron on the soles of the feet for sanity.

MARY: But they would not do that to me, for they know I'm sane.

FURIES: How could they. Possibly. Know that?

MARY: Because it's true. (Pg 90) Bring Stephen Girard. Bring him now into this cell.

FURIES: No, no. Oh no, we must. Not. We can. Not. No, no, no.

MARY: Bring him! *****Scene*****

MARY: (Pg 91) Why have you done this to me?

STEPHEN: I had no choice. You are insane.

MARY: Don't lie to me, Stephen. You know as well as I that I am sane. (Pg 92-93) When we met, I was sixteen, a servant carrying water through the streets. I laughed at everything then. And I was happy without even knowing it. Do you remember that girl, Stephen?

STEPHEN: She does not exist, madam.

MARY: No. We destroyed her, you and I. (pause) Didn't you ever love her?

STEPHEN: (nonchalantly) She was pretty. People noticed her. She was innocent, a trait few women have.

MARY: Innocent! And then she married you and thought she had gained the whole world, and in reality gained only this little room.

STEPHEN: She had everything she should have wanted.

MARY: The cost was too great. I was prepared to give you everything, but you wanted nothing. What good is reason without affection?

STEPHEN: If you wanted affection, you should have told me instead of making a public display of yourself.

MARY: Stephen, I made no attempt to hide my behavior from you. We differed in only one way. I didn't bring my lovers under your roof. I always maintained a respect for you and your pride. Perhaps I should not have done the things I did. But in that I am not alone. (Pg 94-96) When I was childless you blamed me. I felt I had cheated you out of a son. But it wasn't me. You couldn't put life in my body! (pause) I got more warmth from a stranger than you could ever give. It isn't my child that is loathsome to you, Mr. Girard, but the freedom of my mind. May God have pity on you, sir.

STEPHEN: God? (pause; very calmly) I do not know if God exists. If I thought he did I would pray that he keep you here forever. As I cannot be sure of him, I will see to it myself that you endure a hell on earth. (exits)

MARY: (shouting after him) All right! But my baby will live!

FURIES: She thinks her child . . . Will give her comfort. Not so, Mary. Oh no, no. No. You betrayed your husband. And broke your marriage vows. For shame. Shame, Mary. You will give birth to an evil thing. We will now show you what is yet to be. (FURIES place a bundle in MARY'S arms)

MARY: She is so . . . so lovely. (to the child) If I ever doubted that you were worth so much suffering, forgive me. (To FURIES who gleeful) Why are you . . . laughing . . . laughing? Tell me. She will live, won't she?

FURIES: Oh yes. Doubtlessly. Most definitely. The question. However. Is. How long? It will not be. A longish. Life. Months. Mary. Yes. Months. Five. Five months. Yes. Yes.

MARY: No! Oh no! My little one.

FURIES: Five months. Is. Quite enough. Then buried. In an unmarked grave. That you will have in common. Mary. You too will be buried in an unmarked grave. Here. On the hospital grounds. You'll never leave these walls. Mary.

MARY: Good! That at least I delight to hear. The sooner the better will best suit me. If God has any mercy it will be soon. Tell me.

FURIES: Oh no, you'll have to guess.

MARY: A year? Two? Five? Surely no more than five.

FURIES: Yes, five! So clever is our Mary. Five. And twenty. Twenty. More.

MARY: Twenty more? Five and twenty years? I could not stand it.

FURIES: Well, most of it. Will be. There. In this chair. The Tranquilizing chair. The restraining chair. Bound down. Like the evil. Thing you are.

MARY: No! No! God would not permit it. He would not keep me living here in this hell hole for five and twenty years. (praying) Please dear God, sweet, sweet Jesus, be merciful to me and let me not stay here for such an age.

FURIES: Oh, isn't she funny! God won't hear you, Mary. Why should He? He's too busy. Besides He's set you up for it. It's God's jest, Mary. And the fool is. You!

MARY: Get away from me! I won't listen to you. (shouting her prayer) Please God, please!

FURIES: He made you beautiful. And you made the mistake of believing in your own beauty. It's been your doing. And your undoing.

MARY: (still praying) God, help me. Help me! (Pg 97) Where are you God? Please answer me.

FURIES: (taunting) Please answer me! Oh. Where. Are. You. God. God. God.

MARY: Stop it. Damn you. All of you. Where is He? And who is He? Is He another man? Then I'll have nothing to do with such a God. Damn you, God. I damn you!
```
